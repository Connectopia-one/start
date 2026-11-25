# -*- coding: utf-8 -*-
"""Uitdaging Nederlands 🚀 Boost doorstroom (25 november 2026), in de vormen
van het examen van de Examencommissie: 40 vragen die alle hoofdstukken door
elkaar halen. Een lezersbrief en een verhaalfragment om op te klikken,
tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde, invulvragen en
een korte schrijfopdracht. Geen nieuwe leerstof: alles staat in de
hoofdstukken van Nederlands Boost doorstroom. De prenten tekent
inhoud/uitdaging/maak_prenten_boost_nederlands.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-doorstroom"
VAK = "Nederlands"
BESTAND = "boost-nederlands-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/nederlands-boost-uitdaging"
BRIEF = "lezersbrief-schoolstraat.svg"
VERHAAL = "verhaal-jonas.svg"

# klikvakken: _blad.zone(i, 6)
Z = {1: [2, 13.4, 96, 13.7], 2: [2, 27.1, 96, 13.7], 3: [2, 40.8, 96, 13.7],
     4: [2, 54.5, 96, 13.7], 5: [2, 68.2, 96, 13.7], 6: [2, 81.8, 96, 13.7]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Lezersbrief (prent)
    klik("Lees de lezersbrief over de schoolstraat. Klik op de zin met een drogreden.",
         BRIEF, [Z[4]],
         "Zin 4 verdraait de mening van de tegenstanders tot iets absurds: niemand wil dat kinderen omvergereden worden. Dat is een stroman."),
    klik("Klik op de zin die de conclusie van de schrijver geeft.",
         BRIEF, [Z[6]],
         "'Daarom' kondigt het besluit aan dat de schrijver uit zijn argumenten afleidt."),
    klik("Klik op de zin die een feit geeft dat je kan nagaan.",
         BRIEF, [Z[2]],
         "Het aantal ongevallen kan je controleren bij de politie. Zin 3 is een mening, zin 5 een verwachting."),
    met_prent(BRIEF, keuze(
        "Zin 2 steunt op [[*een autoriteit|een vergelijking|een persoonlijke aanval]]. Het woord 'Bovendien' in zin 5 kondigt [[*een extra argument|een tegenargument|een tijdsverband]] aan.",
        "De politie is een bevoegde bron over ongevallen. 'Bovendien' voegt een nieuw argument toe aan de vorige.")),
    met_prent(BRIEF, mk(
        "Tot welke tekstsoort hoort deze lezersbrief vooral?",
        ["argumentatief", "narratief", "prescriptief", "informatief, zonder mening"],
        0,
        "De schrijver neemt een standpunt in en onderbouwt het met argumenten. Dat maakt de tekst argumentatief.")),

    # Verhaal (prent)
    klik("Lees het verhaalfragment over Jonas. Klik op de zin waar een flashback begint.",
         VERHAAL, [Z[2]],
         "Jonas denkt terug aan een zomer van vroeger: het verhaal springt even terug in de tijd."),
    klik("Klik op de zin met een personificatie.",
         VERHAAL, [Z[3]],
         "'Het hele dorp lachte': een dorp krijgt een menselijke eigenschap. Dat is een personificatie."),
    klik("Klik op de zin met een metafoor.",
         VERHAAL, [Z[4]],
         "Het huis wordt een natte spons genoemd zonder 'als' of 'zoals'. Dat is een metafoor. Met 'leek … wel' sluit ze dicht aan bij een vergelijking, maar er staat geen vergelijkingswoord."),
    met_prent(VERHAAL, keuze(
        "Het verhaal eindigt met een [[*cliffhanger|flashback|clou]]: je weet niet wie er voor de deur staat. Het verhaal wordt verteld door een [[*hij-verteller|ik-verteller]].",
        "Een cliffhanger stopt op een spannend moment. De verteller spreekt over Jonas in de derde persoon.")),

    # Communicatie en tekstsoorten
    koppel(
        "Koppel het communicatiebegrip aan het voorbeeld.",
        [
            ["externe ruis", "een lawaaierige bus tijdens een telefoongesprek"],
            ["interne ruis", "je bent zo moe dat je de uitleg niet volgt"],
            ["kanaal", "je stuurt het bericht via mail"],
            ["effect", "de ontvanger stopt echt met roken"],
        ],
        ["de zender kiest een formeel register"],
        "Ruis stoort de boodschap, van buiten of binnenin. Het kanaal is het middel, het effect is wat de boodschap teweegbrengt."),
    tabel(
        "Tot welke tekstsoort hoort deze Nederlandse tekst?",
        [
            ("Een recept uit een kookboek", "Prescriptief"),
            ("Een reclamefilmpje voor frisdrank", "Persuasief"),
            ("Een reisverslag van drie weken Peru", "Narratief"),
            ("Een recensie van een nieuwe film", "Opiniërend"),
        ],
        "Prescriptief schrijft voor, persuasief wil overtuigen, narratief vertelt en opiniërend geeft een oordeel.",
        kolommen=["Prescriptief", "Persuasief", "Narratief", "Opiniërend"]),

    # Structuur
    sorteer(
        "Sorteer deze Nederlandse signaalwoorden volgens het verband.",
        ["Oorzaak of reden", "Gevolg", "Tegenstelling", "Doel"],
        [
            ["immers", "Oorzaak of reden"],
            ["daardoor", "Gevolg"],
            ["toch", "Tegenstelling"],
            ["opdat", "Doel"],
            ["want", "Oorzaak of reden"],
        ],
        "Immers en want geven een reden, daardoor een gevolg, toch een tegenstelling en opdat een doel."),
    keuze(
        "'Het onderwerp' zeg je in [[*één of enkele woorden|één volledige zin]]. De hoofdgedachte zet je in [[*één zin|één woord]].",
        "Het onderwerp is waarover de tekst gaat. De hoofdgedachte is wat de tekst daarover zegt."),

    # Argumenteren
    koppel(
        "Koppel de drogreden aan het voorbeeld.",
        [
            ["vals dilemma", "Ofwel verbieden we alle auto's, ofwel laten we het klimaat stikken."],
            ["glijdende schaal", "Als we dit ene keer toestaan, eindigt het in totale chaos."],
            ["persoonlijke aanval", "Luister niet naar haar, ze heeft zelf niet eens een diploma."],
        ],
        ["Volgens de politie gebeurden er zes ongevallen."],
        "De laatste zin is een gewoon feit met een bevoegde bron, geen drogreden."),
    tabel(
        "Is deze uitspraak een feit of een mening?",
        [
            ("Antwerpen ligt aan de Schelde.", "Feit"),
            ("Antwerpen is de mooiste stad van België.", "Mening"),
            ("In 2025 telde de school 840 leerlingen.", "Feit"),
            ("Huiswerk is zinloos.", "Mening"),
        ],
        "Een feit kan je nagaan. Een mening is een persoonlijk oordeel.",
        kolommen=["Feit", "Mening"]),

    # Bronnen
    keuze(
        "Een tekst die met opzet maar één kant van de zaak toont om een politieke mening te verspreiden, heet [[*propaganda|een recensie]]. Bewust een invalshoek kiezen die de lezer in een richting duwt, heet [[*framing|ironie]].",
        "Propaganda is eenzijdig en wil sturen. Framing zit vooral in woordkeuze en invalshoek."),
    mk("Twee kranten berichten over dezelfde betoging: 'Duizenden op straat voor het klimaat' en 'Klimaatbetoging legt verkeer plat'. Wat zie je hier?",
       ["framing", "een sonnet", "een flashback", "een eufemisme dat verzacht"],
       0,
       "Dezelfde gebeurtenis krijgt telkens een andere invalshoek. Dat is framing."),

    # Register en taalvariatie
    tabel(
        "Formeel, neutraal of informeel register?",
        [
            ("Geachte heer, mevrouw", "Formeel"),
            ("Hoi! Alles goed?", "Informeel"),
            ("Met vriendelijke groeten", "Formeel"),
            ("Groetjes en tot snel!", "Informeel"),
        ],
        "In een sollicitatie of een mail naar een onbekende kies je een formeel register. Aan een vriend schrijf je informeel.",
        kolommen=["Formeel", "Neutraal", "Informeel"]),
    keuze(
        "Iemand praat anders op café dan op een begrafenis. Dat is een [[*situationele|regionale]] variëteit. Dialect is een [[*regionale|situationele]] variëteit.",
        "Situationele variatie hangt af van de situatie, regionale variatie van de streek."),

    # Woordsoorten
    tabel(
        "Welke woordsoort is dit woord uit de zin 'Er stonden veertien oude fietsen in het rek'?",
        [
            ("veertien", "Telwoord"),
            ("oude", "Bijvoeglijk naamwoord"),
            ("fietsen", "Zelfstandig naamwoord"),
            ("in", "Voorzetsel"),
        ],
        "Veertien is een telwoord, oude zegt iets over fietsen, fietsen is een zelfstandig naamwoord en in is een voorzetsel.",
        kolommen=["Telwoord", "Bijvoeglijk naamwoord", "Zelfstandig naamwoord", "Voorzetsel"]),
    keuze(
        "In 'Hij wast zich' is 'zich' een [[*wederkerend|bezittelijk|aanwijzend]] voornaamwoord. 'Wie' in 'Wie komt er mee?' is een [[*vragend|betrekkelijk]] voornaamwoord.",
        "Zich verwijst terug naar het onderwerp. In een vraag is wie een vragend voornaamwoord."),

    # Werkwoorden en spelling
    tabel(
        "Benoem de werkwoordstijd van deze zin.",
        [
            ("Ik had de hele dag gelopen.", "Voltooid verleden tijd"),
            ("Zij zal morgen komen.", "Onvoltooid toekomende tijd"),
            ("We wandelden door het bos.", "Onvoltooid verleden tijd"),
        ],
        "Had + voltooid deelwoord is de voltooid verleden tijd. Zal + infinitief is de onvoltooid toekomende tijd.",
        kolommen=["Voltooid verleden tijd", "Onvoltooid toekomende tijd", "Onvoltooid verleden tijd"]),
    keuze(
        "Gisteren [[*verhuisde|verhuisden|verhuisdde]] mijn tante. Er is iets [[*gebeurd|gebeurt]]. Er [[*gebeurt|gebeurd]] nu iets vreemds.",
        "Verhuizen heeft een z in de infinitief; z zit niet in 't kofschip, dus -de. Gebeurd is het voltooid deelwoord, gebeurt is de persoonsvorm."),
    inv("Wat is het meervoud van 'lid'? Schrijf één woord.",
        ["leden"],
        "Lid heeft een onregelmatig meervoud: leden."),
    sorteer(
        "Is dit woord een samenstelling of een afleiding?",
        ["Samenstelling", "Afleiding"],
        [
            ["boekenkast", "Samenstelling"],
            ["vriendelijk", "Afleiding"],
            ["voetbalveld", "Samenstelling"],
            ["schoonheid", "Afleiding"],
        ],
        "Een samenstelling bestaat uit twee bestaande woorden. Een afleiding krijgt een voor- of achtervoegsel zoals -lijk of -heid."),

    # Zinsdelen
    tabel(
        "Welk zinsdeel is het? 'De postbode bracht mijn oma gisteren een pakje.'",
        [
            ("De postbode", "Onderwerp"),
            ("mijn oma", "Meewerkend voorwerp"),
            ("een pakje", "Lijdend voorwerp"),
            ("gisteren", "Bijwoordelijke bepaling"),
        ],
        "Wie brengt? de postbode. Wat wordt gebracht? een pakje. Aan wie? mijn oma. Wanneer? gisteren.",
        kolommen=["Onderwerp", "Meewerkend voorwerp", "Lijdend voorwerp", "Bijwoordelijke bepaling"]),
    mk("Hoe luidt 'De gemeente heeft het plein heraangelegd' in de lijdende vorm?",
       ["Het plein is door de gemeente heraangelegd.", "De gemeente is door het plein heraangelegd.", "Het plein heeft de gemeente zelf heraangelegd.", "De gemeente wordt door het plein heraangelegd."],
       0,
       "Het lijdend voorwerp wordt onderwerp en de handelende persoon komt erachter met 'door'."),
    keuze(
        "In 'Hoewel hij doodmoe was, ging hij toch trainen' is '[[*Hoewel hij doodmoe was|ging hij toch trainen]]' de bijzin. In een bijzin staat de persoonsvorm [[*achteraan|op de tweede plaats]].",
        "Een bijzin begint met een onderschikkend voegwoord en heeft de persoonsvorm achteraan."),

    # Leestekens
    keuze(
        "Hoewel het goot[[*,|.|:]] gingen we toch buiten spelen. Ze zei[[*:|,|;]] 'Ik kom morgen.'",
        "Een komma scheidt de bijzin van de hoofdzin. Een dubbele punt kondigt de letterlijke woorden aan."),

    # Beeldspraak en gevoelswaarde
    koppel(
        "Koppel de vorm van gevoelswaarde of beeldspraak aan het voorbeeld.",
        [
            ["eufemisme", "Opa is ingeslapen."],
            ["dysfemisme", "Die nieuwe wet is een gedrocht."],
            ["ironie", "Wat een prachtig weertje!, terwijl het giet."],
            ["spreekwoord", "Wie het kleine niet eert, is het grote niet weerd."],
        ],
        ["Het regent hard."],
        "Een eufemisme verzacht, een dysfemisme maakt erger, ironie zegt het omgekeerde en een spreekwoord bevat een levensles."),

    # Verhaal en literatuur
    keuze(
        "De hoofdpersoon van een verhaal is de [[*protagonist|antagonist]]. Een verteller die in het hoofd van alle personages kijkt, is een [[*alwetende verteller|ik-verteller]].",
        "De protagonist is de hoofdpersoon, de antagonist is de tegenspeler."),
    tabel(
        "Klopt dit over poëzie en drama?",
        [
            ("Een sonnet telt veertien versregels.", J),
            ("Een kwatrijn is een strofe van vier versregels.", J),
            ("Een tragedie loopt goed af.", F),
            ("Een limerick is een grappig gedicht van vijf regels.", J),
        ],
        "Een tragedie loopt slecht af, een komedie goed."),
    sleep(
        "Het herhalen van dezelfde beginmedeklinker, zoals in 'wie wind zaait', heet [[alliteratie]]. Het herhalen van dezelfde klinkerklank heet [[assonantie]].",
        ["enjambement", "terzine"],
        "Alliteratie: beginklank. Assonantie: klinkerklank. Een enjambement loopt over de versgrens heen."),
    volgorde(
        "Zet de opbouw van een klassiek verhaal in de juiste volgorde.",
        ["beginsituatie", "probleem of conflict", "spanning stijgt", "climax", "afloop"],
        "Een klassieke verhaallijn bouwt de spanning op tot een hoogtepunt (climax) en eindigt met de afloop."),

    mk("'Er lagen zes appels op tafel. Ze waren helemaal rijp.' Naar wat verwijst 'ze'?",
       ["de appels", "de tafel", "de lezer", "zes mensen"],
       0,
       "Een verwijswoord verwijst naar iets wat eerder genoemd werd: hier de appels, want de tafel is enkelvoud."),
    mk("Je leest een artikel op een site die je niet kent. Welke vraag stel je eerst?",
       ["Wie is de zender en wat wil die bereiken?", "Hoeveel foto's staan er allemaal bij het artikel?", "Is de tekst wel langer dan één bladzijde?", "Welk lettertype gebruikt de website?"],
       0,
       "Om de betrouwbaarheid in te schatten, vraag je eerst wie de tekst maakte en met welk doel."),
    keuze(
        "Het meervoud van 'stad' is [[*steden|stadden|staden]]. In 'schaapskooi' hoor je een [[*tussenklank|doffe klank|leenwoord]].",
        "Stad heeft een onregelmatig meervoud. De -s- in schaapskooi is een tussenklank."),
    tabel(
        "Klopt dit over standaardtaal en tussentaal?",
        [
            ("Standaardtaal is in heel het taalgebied gepast in formele situaties.", J),
            ("'Ik kom ni naar school' is standaardtaal.", F),
            ("Jongerentaal wordt sterk beïnvloed door het Engels en sociale media.", J),
        ],
        "Standaardtaal begrijpt iedereen in het taalgebied. 'Ni' is tussentaal, geen standaardtaal."),
    sorteer(
        "Hoort dit bij de verbale of de non-verbale communicatie?",
        ["Verbaal", "Non-verbaal"],
        [
            ["je woordkeuze", "Verbaal"],
            ["oogcontact", "Non-verbaal"],
            ["je gebaren", "Non-verbaal"],
            ["de zinnen die je zegt", "Verbaal"],
        ],
        "Verbale communicatie gebruikt woorden. Non-verbale communicatie gaat over houding, gebaren, mimiek en oogcontact."),
    # Schrijfopdracht
    open_("Schrijf een korte formele mail (60 à 80 woorden) aan de directie van je school. Vraag of er in de middagpauze een stille studieruimte kan komen en geef één argument.",
          "Geachte directie\n\nIk ben leerling van het vijfde jaar en ik wil u iets vragen. Zou er in de middagpauze een stille studieruimte kunnen komen? Veel leerlingen willen dan rustig hun lessen herhalen, maar in de refter is het te lawaaierig om zich te concentreren. Een stil lokaal zou ons helpen om beter voorbereid naar de toetsen te gaan.\n\nAlvast bedankt voor uw antwoord.\n\nMet vriendelijke groeten\nNoor Peeters",
          "Een goed antwoord heeft een formele aanspreking en afsluiter, een duidelijke vraag, één onderbouwd argument en correcte spelling."),
]

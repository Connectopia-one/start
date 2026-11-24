"""Lees- en luisterstrategieën en notities nemen — pittig (Beyond dubbele finaliteit, Nederlands).

Eigen vragen binnen nl_strategie: leesdoel, voorkennis, voorspellen, scannen en skimmen, intensief lezen, markeren, notities bij luisterteksten en nagaan of je begrepen hebt."""
from ..beyond_nederlands_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

VRAGEN = [
    casus(
        "Je krijgt voor een taak een artikel van vier bladzijden: « Energiedrankjes: een gevaar voor tieners? ». "
        "Het artikel heeft vijf tussenkoppen, twee grafieken en een kader met tips. Je hebt drie opdrachten:\n"
        "1. Zoek hoeveel cafeïne een blikje bevat.\n2. Zeg in één zin waar het artikel over gaat.\n3. Bereid je voor op een toets over de gevolgen voor je gezondheid.",
        [
            tabel("Welke strategie past bij elke opdracht?", [
                ("opdracht 1", "scannen"), ("opdracht 2", "skimmen"), ("opdracht 3", "intensief lezen"),
            ], "Elk leesdoel vraagt een andere strategie.", kolommen=["scannen", "skimmen", "intensief lezen"]),
            mk("Wat bekijk je bij opdracht 2 zeker?",
               ["de titel en de tussenkoppen", "alle cijfers in de grafieken", "elke zin van de tekst, woord voor woord", "de naam van de fotograaf"], 0,
               "Skimmen geeft een globaal beeld."),
            keuze("Voor je begint, denk je na over wat je al weet over energiedrankjes. Dat heet je [[*voorkennis activeren|scannen|samenvatten]].", "Wat je al weet, helpt je nieuwe informatie te plaatsen."),
            mk("Bij opdracht 3 markeer je bijna elke zin. Wat is het probleem?",
               ["Als alles gemarkeerd is, valt niets meer op.", "Markeren is op een toets of examen altijd verboden.", "Gemarkeerde zinnen vergeet je juist veel sneller dan andere.", "Markeren werkt alleen bij luisterteksten."], 0,
               "Markeer enkel de kern."),
        ],
    ),
    sorteer("Scannen of skimmen?", ["scannen", "skimmen"], [
        ["de vertrekuren van een trein opzoeken", "scannen"], ["snel zien of een boek over je onderwerp gaat", "skimmen"],
        ["een telefoonnummer zoeken op een website", "scannen"], ["de krant doorbladeren om te zien wat er vandaag in staat", "skimmen"],
        ["in een recept zoeken hoeveel eieren je nodig hebt", "scannen"],
    ], "Scannen zoekt één gegeven, skimmen geeft een overzicht."),
    volgorde("Zet de stappen van een strategische aanpak van een studietekst in volgorde.", [
        "het leesdoel bepalen en je voorkennis activeren", "de tekst overlopen: titel, tussenkoppen, afbeeldingen", "intensief lezen en de kern markeren", "samenvatten in je eigen woorden", "nagaan of je de tekst kan navertellen",
    ], "Van overzicht naar detail en dan controleren."),
    mk("Je hoort een lezing van twintig minuten. Hoe noteer je het best?",
       ["in steekwoorden, met ruimte om later aan te vullen", "elk woord dat de spreker zegt, in volledige zinnen", "niets, want je onthoudt het achteraf toch wel", "enkel de grappige voorbeelden van de spreker"], 0,
       "Bij luisteren kan je niet terugspoelen, dus noteer je kort."),
    tabel("Klopt dit over goede notities bij een les?", [
        ("Eigen afkortingen die je altijd gebruikt, maken notities sneller.", J),
        ("Notities van iemand anders werken even goed als je eigen notities.", F),
        ("Je leest je notities best meteen na de les na en vult ze aan.", J),
        ("Bij een luistertekst noteer je best volledige zinnen.", F),
    ], "Jouw notities dragen jouw denkstappen."),
    keuze("Op basis van de titel « Waarom we te weinig slapen » [[*voorspel|scan|vat samen]] je dat de tekst oorzaken van slaaptekort zal geven.", "Voorspellen maakt je lezen gerichter."),
    mk("Je leest een alinea en begrijpt ze niet. Wat doe je eerst?",
       ["de alinea opnieuw lezen en in eigen woorden navertellen", "meteen stoppen met de hele tekst", "de alinea overslaan en hopen dat het later duidelijk wordt", "alleen de laatste zin onthouden"], 0,
       "Wat je kan navertellen, heb je begrepen."),
    koppel("Koppel elke strategie aan wat je doet.", [
        ["voorkennis activeren", "nagaan wat je al over het onderwerp weet"], ["voorspellen", "uit titel en beelden raden wat komt"],
        ["intensief lezen", "langzaam en nauwkeurig, met aandacht voor elk verband"], ["samenvatten", "de kern in kortere vorm herformuleren"],
    ], ["zo snel mogelijk de laatste bladzijde lezen"], "Elke strategie dient een ander moment van het lezen."),
    tabel("Hoort dit in een samenvatting?", [
        ("de hoofdgedachte", J), ("de hoofdpunten", J), ("een grappig voorbeeld uit de tekst", F), ("je eigen mening over het onderwerp", F),
    ], "Een samenvatting geeft de kern van de tekst, niet jouw mening."),
    inv("Hoe noem je het doel waarmee je aan een tekst begint, met één woord?", ["leesdoel", "het leesdoel"], "Het leesdoel bepaalt je strategie."),
    mk("Je leesdoel verandert tijdens het lezen. Wanneer gebeurt dat?",
       ["Je zoekt één gegeven, maar de tekst blijkt veel nuttiger.", "Je hebt de tekst nog niet geopend of bekeken.", "Je hebt de titel gelezen en verder nog helemaal niets.", "Een leesdoel kan nooit veranderen, het ligt vooraf vast."], 0,
       "Dan schakel je over van scannen naar intensief lezen."),
    sleep("Bij een luistertekst kan je niet [[terugkeren]], dus noteer je [[steekwoorden]]. Meteen na afloop vul je je notities [[aan]].",
          ["markeren", "volledige zinnen"], "Luisteren vraagt een eigen aanpak."),
    tabel("Welke zaken zet je best in de marge van een studietekst?", [
        ("een kernwoord per alinea", J), ("een vraagteken waar je iets niet snapt", J), ("een pijl naar een verband met een andere alinea", J), ("een volledige kopie van de alinea", F),
    ], "De marge is voor korte wegwijzers."),
    mk("Een spreker zegt: « Ik bespreek drie oorzaken. » Wat doe je met je notities?",
       ["Je zet al drie nummers klaar.", "Je stopt met noteren tot hij klaar is.", "Je noteert enkel de derde oorzaak.", "Je schrijft de zin volledig over."], 0,
       "Sprekers kondigen hun structuur vaak aan: gebruik die."),
    keuze("Een schema of mindmap is [[*wel|geen]] een geldige manier om een tekst met veel verbanden samen te vatten.", "Een schema toont de verbanden in beeld."),
    open_("Je moet een krantenartikel lezen om er in de klas over te discussiëren. Beschrijf in drie stappen hoe je dat aanpakt.",
          "Eerst bepaal ik mijn leesdoel en kijk ik naar de titel en tussenkoppen. Dan lees ik het artikel intensief en markeer ik de hoofdgedachte en de argumenten. Tot slot noteer ik kort mijn eigen mening met een argument.",
          "Leesdoel, intensief lezen, verwerken."),
    keuze("Een luistertekst gaat te snel. Je noteert [[*enkel de kernwoorden|alles wat je hoort|niets]] en vult de rest achteraf aan.", "Zo verlies je de draad niet."),
    inv("Welke strategie gebruik je om in een jaarverslag van vijftig bladzijden het aantal leden te vinden?", ["scannen"], "Je zoekt één gegeven."),
    tabel("Lees- of luistertekst: wanneer helpt dit het meest?", [
        ("terugbladeren naar een vorige alinea", "leestekst"), ("letten op de intonatie en pauzes van de spreker", "luistertekst"),
        ("tussenkoppen bekijken", "leestekst"), ("letten op aankondigingen als « mijn tweede punt is »", "luistertekst"),
    ], "Elk soort tekst geeft andere houvast.", kolommen=["leestekst", "luistertekst"]),
    keuze("Bij een moeilijke studietekst begin je met de tekst te [[*overlopen om de opbouw te zien|uit het hoofd te leren|samen te vatten]].", "Wie de opbouw kent, kan de details plaatsen."),
    mk("Een klasgenoot leest elke tekst even grondig, van de eerste tot de laatste letter. Wat raad je aan?",
       ["Eerst het leesdoel bepalen en dan een strategie kiezen.", "Nog trager en aandachtiger lezen om zeker niets te missen.", "Alleen nog de titels en de tussenkoppen lezen, nooit meer.", "Elke tekst twee keer volledig lezen."], 0,
       "Niet elke tekst vraagt dezelfde aanpak."),
    sorteer("Doe je dit vóór, tijdens of na het lezen?", ["vóór", "tijdens", "na"], [
        ["je leesdoel bepalen", "vóór"], ["de kern markeren", "tijdens"], ["de tekst samenvatten", "na"],
        ["je voorkennis activeren", "vóór"], ["verwijswoorden controleren", "tijdens"],
    ], "Lezen is een proces met een begin, midden en einde."),
    mk("Welke vraag stel je jezelf na het lezen om te controleren of je de tekst begrepen hebt?",
       ["Kan ik de hoofdgedachte in één zin zeggen?", "Hoeveel bladzijden telde de tekst?", "Welk lettertype gebruikte de schrijver?", "Hoe lang heb ik precies gelezen?"], 0,
       "Wie de kern kan verwoorden, heeft de tekst begrepen."),
    tabel("Past deze strategie bij het leesdoel « een recept volgen »?", [
        ("eerst de lijst met ingrediënten overlopen", J), ("de stappen in volgorde nauwkeurig lezen", J), ("enkel de titel van het recept lezen", F),
    ], "Een instructie lees je stap voor stap."),
    keuze("Bij een luistertekst kan je [[*wel|geen]] voorkennis activeren, bijvoorbeeld op basis van de titel van de lezing.", "Ook vooraf weet je vaak waarover het zal gaan."),
    mk("Je markeert in een tekst over klimaat de zin « Bovendien stijgt de zeespiegel. » Wat noteer je best in de marge?",
       ["zeespiegel stijgt", "bovendien", "een uitroepteken zonder woord", "de hele zin opnieuw"], 0,
       "Een kernwoord per alinea is genoeg."),
    sleep("Een tekst die je op een toets moet kennen, lees je [[intensief]]. Je [[markeert]] de kern en maakt daarna een [[samenvatting]] in je eigen woorden.",
          ["snel", "scant"], "Studeren vraagt een grondige aanpak."),
]

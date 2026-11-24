"""Onderzoeken en ontwerpen, STEM en samenleving — pittig
(🌍 Beyond doorstroom, natuurwetenschappen).

Deels overgenomen uit de pittige vragen natuurwetenschappen Boost doorstroom
(zelfde leerstof), aangevuld met eigen vragen op het niveau van Beyond.
"""
from ..boost_do_nw_themas import onderzoek as O
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus, open_

OVER = [O.VRAGEN[i] for i in (11, 12, 13, 14, 15, 16, 18, 19, 21, 23, 24, 25, 27)]

EIGEN = [
    casus(
        "Milan onderzoekt of zout de kooktemperatuur van water verhoogt. Hij kookt "
        "drie potten water: zonder zout, met 10 g zout en met 20 g zout. De eerste pot "
        "zet hij op een groot vuur, de andere twee op een klein vuur. Hij meet telkens "
        "één keer met dezelfde thermometer.",
        [
            mk("Wat is de onafhankelijke variabele in Milans proef?",
               ["de hoeveelheid zout", "de kooktemperatuur", "de grootte van het vuur", "de thermometer"], 0,
               "Dat is wat Milan zelf bewust verandert. De kooktemperatuur meet hij: dat is de afhankelijke variabele."),
            tabel("Klopt dit over de opzet van Milan?", [
                ("Het vuur had voor elke pot hetzelfde moeten zijn.", J),
                ("De pot zonder zout dient als controleproef.", J),
                ("Eén meting per pot is genoeg voor een betrouwbaar besluit.", F),
                ("Hij verandert maar één grootheid tegelijk.", F),
            ], "Door ook het vuur te veranderen weet hij niet meer wat het verschil veroorzaakt. Herhalen maakt het resultaat betrouwbaarder."),
            keuze("De pot zonder zout dient om [[*mee te vergelijken|de hypothese te bewijzen|de thermometer te ijken]].",
                  "Een controleproef zonder behandeling toont wat er gebeurt zonder zout."),
        ],
    ),
    tabel("Is dit een goede, onderzoekbare onderzoeksvraag?", [
        ("Hoe hangt de remweg van een fiets af van de snelheid?", J),
        ("Is fysica leuk?", F),
        ("Welke invloed heeft de hoeveelheid licht op de lengte van een kiemplant na tien dagen?", J),
        ("Waarom bestaat de wereld?", F),
    ], "Een goede onderzoeksvraag kan je met metingen beantwoorden en noemt wat je verandert en wat je meet."),
    sorteer("Hoort dit bij onderzoeken of bij ontwerpen?", ["Onderzoeken", "Ontwerpen"], [
        ["een hypothese opstellen", "Onderzoeken"],
        ["criteria voor een oplossing vastleggen", "Ontwerpen"],
        ["een prototype bouwen en testen", "Ontwerpen"],
        ["een besluit trekken over een verband", "Onderzoeken"],
    ], "Onderzoeken beantwoordt een vraag, ontwerpen lost een probleem op met een product of systeem."),
    koppel("Koppel elke stap van een onderzoek aan wat je erin doet.", [
        ["hypothese", "je schrijft op wat je verwacht en waarom"],
        ["onderzoeksplan", "je kiest materiaal, stappen en variabelen"],
        ["verwerking", "je zet je metingen in een tabel en een grafiek"],
        ["reflectie", "je bekijkt wat er beter kon aan je opzet"],
    ], ["je vraagt een collega om je gelijk te geven"],
       "Elke stap bouwt verder op de vorige."),
    mk("Een leerling meet vijf keer de valtijd: 0,45 s, 0,46 s, 0,44 s, 0,82 s en 0,45 s. Wat doe je best met 0,82 s?",
       ["Je vermeldt ze, zoekt de oorzaak en verklaart je keuze",
        "Je schrapt ze zonder iets te zeggen, want ze past niet bij je verwachting",
        "Je rekent ze gewoon mee in het gemiddelde zonder iets te zeggen",
        "Je herhaalt de hele proef tot alle metingen precies gelijk zijn"], 0,
       "Een uitschieter verberg je niet. Je bespreekt ze en verklaart waarom je ze wel of niet meetelt."),
    inv("Iemand meet 12,0 cm, 12,4 cm en 12,2 cm. Wat is het gemiddelde, in cm?", ["12,2", "12.2", "12,2 cm"],
        "Tel op (36,6) en deel door drie."),
    tabel("Welke variabele is dit in een proef over hoe snel een tablet oplost in water van verschillende temperatuur?", [
        ("de temperatuur van het water", "onafhankelijk"),
        ("de tijd tot het tablet weg is", "afhankelijk"),
        ("de hoeveelheid water", "constant"),
        ("de soort tablet", "constant"),
    ], "Je verandert één grootheid, meet het gevolg en houdt de rest gelijk.", kolommen=["onafhankelijk", "afhankelijk", "constant"]),
    keuze("Een hypothese die je resultaten tegenspreken, is [[*toch nuttig, want je leert eruit|een mislukt onderzoek|een reden om de metingen aan te passen]].",
          "Ook een weerlegde hypothese levert kennis op."),
    volgorde("Zet de stappen van een ontwerpproces in de juiste volgorde.", [
        "het probleem en de criteria vastleggen",
        "mogelijke oplossingen bedenken en kiezen",
        "een prototype bouwen",
        "het prototype testen aan de criteria",
        "het ontwerp bijsturen",
    ], "Ontwerpen gaat in rondjes: na het testen volgt vaak bijsturen en opnieuw testen."),
    tabel("Klopt dit over criteria bij een ontwerp?", [
        ("Criteria leg je vast voor je begint te bouwen.", J),
        ("Een oplossing die aan één criterium voldoet, is altijd goed.", F),
        ("Met de criteria vergelijk je twee werkende ontwerpen.", J),
    ], "Criteria zijn de meetlat: vooraf vastgelegd en achteraf gebruikt om te beoordelen."),
    sleep("Wat je in een proef zelf verandert, is de [[onafhankelijke]] variabele. Wat je meet, is de [[afhankelijke]] variabele. Alles wat je gelijk houdt, noem je [[constanten]].",
          ["hypothesen", "criteria"], "Zo kan je een verschil aan één oorzaak toeschrijven."),
    mk("Een bedrijf ontwikkelt een slimme rolstoel. Welke combinatie van STEM-disciplines is nodig?",
       ["Alle vier de STEM-disciplines samen",
        "Enkel techniek, want het gaat om een toestel",
        "Enkel wiskunde, want het gaat om berekeningen",
        "Enkel natuurwetenschappen, want het gaat om het menselijk lichaam"], 0,
       "Krachten, elektronica, ontwerp en berekeningen grijpen in elkaar. Eén discipline volstaat niet."),
    open_("Een school wil minder energie verbruiken. Beschrijf hoe je dat met de stappen van een ontwerpproces aanpakt.",
          "Ik leg eerst het probleem en de criteria vast (bijvoorbeeld 10 procent minder verbruik, betaalbaar). Dan bedenk ik oplossingen zoals ledlampen of tijdschakelaars, kies er één, test ze een maand en meet het verbruik. Haal ik het criterium niet, dan stuur ik bij."),
]

VRAGEN = OVER + EIGEN

# -*- coding: utf-8 -*-
"""Wetenschappelijk onderzoek, ontwerpen en STEM — 🌍 Beyond, chemie.

Deel 1 gaat over de stappen van een onderzoek: van de onderzoeksvraag en de
hypothese naar de proefopzet met zijn variabelen, de controleproef, het meten en
herhalen, het besluit dat op de vraag antwoordt, en het rapporteren. Deel 2 gaat
over ontwerpen en over STEM in de samenleving: de ontwerpvraag, criteria en
randvoorwaarden, het opsplitsen in deelproblemen, het prototype en het
bijsturen, en de vragen die bij een nieuwe toepassing horen.

De voorbeelden komen uit de chemie, zodat de stappen altijd aan een echte proef
hangen in plaats van los in de lucht.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een goede onderzoeksvraag?",
        opties=[
            "een vraag die je met een meting kan beantwoorden",
            "een vraag waarop iedereen het antwoord al kent",
            "een vraag waarop meerdere meningen mogelijk zijn",
            "een vraag die met ja of nee te beantwoorden is",
        ],
        antwoord=0,
        uitleg="Ze moet nauwkeurig afgebakend en meetbaar zijn. Hoe los het zout op is "
        "geen onderzoeksvraag, hoeveel gram per 100 mL water wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een hypothese?",
        opties=[
            "een onderbouwd vermoeden dat je kan testen",
            "een vaste conclusie na een reeks metingen",
            "een willekeurige gok zonder enige uitleg",
            "een vraag waarop het onderzoek antwoordt",
        ],
        antwoord=0,
        uitleg="Ze zegt wat je verwacht en waarom. Een hypothese die door de meting "
        "verworpen wordt, is geen mislukking maar een resultaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt hoe de temperatuur de reactiesnelheid beïnvloedt. Wat is de onafhankelijke variabele?",
        opties=[
            "de temperatuur, want die stel jij zelf in",
            "de reactiesnelheid, want die meet je af",
            "de concentratie, want die houd je gelijk",
            "het volume, want dat verandert onderweg",
        ],
        antwoord=0,
        uitleg="Wat jij instelt, is onafhankelijk; wat je meet, is afhankelijk. Al de "
        "rest houd je constant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke variabelen houd je bij die proef constant? Kruis alles aan wat juist is.",
        opties=[
            "de concentratie van de oplossing",
            "de hoeveelheid vaste stof per proef",
            "de temperatuur van het mengsel",
            "de tijd die de reactie nodig heeft",
        ],
        antwoord=[0, 1],
        uitleg="De temperatuur is net wat je laat variëren en de tijd is wat je meet. "
        "Alles wat je gelijk houdt, heet een constante.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een controleproef?",
        opties=[
            "om te zien wat er zonder de behandeling gebeurt",
            "om te zien of het toestel wel juist afgelezen is",
            "om te zien of de hypothese wel goed geschreven is",
            "om te zien of de proef wel veilig genoeg verloopt",
        ],
        antwoord=0,
        uitleg="Zonder dat vergelijkingspunt weet je niet of het verschil van jouw ingreep "
        "komt. Daarom hoort er bij een katalysatorproef altijd een buis zonder "
        "katalysator.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom herhaal je een meting meerdere keren?",
        opties=[
            "om toevallige afwijkingen te kunnen uitvlakken",
            "om het resultaat dichter bij de hypothese te krijgen",
            "om het toestel de kans te geven op te warmen",
            "om zeker te zijn dat de stof helemaal opgebruikt is",
        ],
        antwoord=0,
        uitleg="Een toevallige fout valt bij een gemiddelde grotendeels weg. Een "
        "systematische fout verdwijnt daar juist niet mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een toevallige en een systematische fout?",
        opties=[
            "een systematische fout wijkt altijd naar dezelfde kant af",
            "een systematische fout treedt altijd maar één enkele keer op",
            "een systematische fout komt enkel bij een digitaal toestel voor",
            "een systematische fout kan je met een gemiddelde wel wegwerken",
        ],
        antwoord=0,
        uitleg="Een balans die 0,2 g te veel aangeeft, doet dat elke keer. Herhalen helpt "
        "dan niet, kalibreren wel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de variabele die je in een proef zelf instelt?",
        antwoord=["onafhankelijke", "de onafhankelijke", "onafhankelijke variabele"],
        uitleg="Wat je daarna meet, is de afhankelijke variabele. Al de rest houd je "
        "constant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort in een besluit van een onderzoek?",
        opties=[
            "een antwoord op de onderzoeksvraag, met de meting erbij",
            "een opsomming van alles wat er onderweg misgelopen is",
            "een nieuwe hypothese die nog niet getest geweest is",
            "een beschrijving van elke handeling in de juiste volgorde",
        ],
        antwoord=0,
        uitleg="Het besluit zegt of de hypothese klopt en waaruit je dat besluit. De "
        "werkwijze hoort eerder in het verslag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over reproduceerbaarheid zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "iemand anders moet hetzelfde resultaat kunnen krijgen",
            "daarvoor moet je werkwijze nauwkeurig beschreven zijn",
            "een resultaat is al geldig als het bij jou één keer lukte",
            "daarvoor mag de werkwijze geheim gehouden worden",
        ],
        antwoord=[0, 1],
        uitleg="Pas als het resultaat bij iemand anders terugkomt, is het betrouwbaar. "
        "Daarom staat de werkwijze zo precies in een artikel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hypothese die verworpen wordt, maakt het onderzoek waardeloos.",
        antwoord=False,
        uitleg="Ook dat is een antwoord op de vraag: het vermoeden klopte niet. Dat is "
        "even bruikbaar als een bevestiging.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grafiek hoort een titel en op beide assen een eenheid te krijgen.",
        antwoord=True,
        uitleg="Zonder eenheid betekent een getal niets. De as met wat je instelde komt "
        "liggend, de as met wat je meette staand.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag een meting die niet in je verwachting past, gewoon weglaten.",
        antwoord=False,
        uitleg="Je noteert ze en zoekt uit waar ze van komt. Een uitschieter schrappen "
        "omdat hij stoort, is geen wetenschap.",
    ),
    dict(
        type="waarofniet",
        vraag="Peer review betekent dat vakgenoten het werk nakijken voor het verschijnt.",
        antwoord=True,
        uitleg="Zij gaan de werkwijze en het besluit na. Dat maakt een artikel niet "
        "onfeilbaar, maar wel een heel stuk betrouwbaarder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij een onderzoek? Kruis alles aan wat juist is.",
        opties=[
            "een onderzoeksvraag opstellen",
            "de resultaten rapporteren",
            "het besluit vooraf vastleggen",
            "de metingen aanpassen aan de hypothese",
        ],
        antwoord=[0, 1],
        uitleg="De laatste twee draaien de zaak om. Het besluit volgt uit de metingen, "
        "niet omgekeerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noteer je bij een proef ook wat er misliep?",
        opties=[
            "omdat dat de afwijking in je resultaat kan verklaren",
            "omdat je anders geen punten op je verslag krijgt",
            "omdat je de proef dan niet moet herhalen",
            "omdat je hypothese dan niet verworpen kan worden",
        ],
        antwoord=0,
        uitleg="Een gemorste druppel of een buis die te warm stond, verklaart soms de "
        "hele uitschieter. Zonder die nota blijft het raden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de proef zonder de behandeling, waarmee je vergelijkt?",
        antwoord=["de controleproef", "controleproef", "blanco"],
        uitleg="Soms heet dat ook de blanco. Zonder dat vergelijkingspunt weet je niet "
        "waar het verschil van komt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen nauwkeurig en precies meten?",
        opties=[
            "nauwkeurig ligt dicht bij de echte waarde, precies dicht bij elkaar",
            "nauwkeurig ligt dicht bij elkaar, precies dicht bij de echte waarde",
            "nauwkeurig gaat over het toestel, precies over de persoon die meet",
            "nauwkeurig gaat over de eenheid, precies over het aantal cijfers",
        ],
        antwoord=0,
        uitleg="Vijf metingen die mooi samen liggen maar alle vijf 0,3 g te hoog, zijn "
        "precies maar niet nauwkeurig. Dat wijst op een systematische fout.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de variabele die je in een proef meet?",
        antwoord=["afhankelijke", "de afhankelijke", "afhankelijke variabele"],
        uitleg="Ze hangt af van wat je instelde. Die ingestelde grootheid is de "
        "onafhankelijke variabele.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een meting die sterk afwijkt van de andere metingen?",
        antwoord=["een uitschieter", "uitschieter", "outlier"],
        uitleg="Je noteert ze en zoekt de oorzaak. Schrappen mag enkel als je kan zeggen "
        "wat er fout ging.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een ontwerpvraag?",
        opties=[
            "een vraag naar iets wat je moet maken of oplossen",
            "een vraag naar een verband dat je wil meten",
            "een vraag naar een mening over een toepassing",
            "een vraag naar een stof die nog niet bestaat",
        ],
        antwoord=0,
        uitleg="Een onderzoeksvraag zoekt kennis, een ontwerpvraag zoekt een oplossing. "
        "Maak een filter die zand uit water haalt, is een ontwerpvraag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een criterium bij een ontwerp?",
        opties=[
            "een eis waaraan de oplossing moet voldoen",
            "een beperking van tijd, geld of materiaal",
            "een stap in de werkwijze van het ontwerp",
            "een meting die je aan het eind uitvoert",
        ],
        antwoord=0,
        uitleg="Het filter moet minstens 90 % van het zand tegenhouden: dat is een "
        "criterium. Je hebt maar één lesuur: dat is een randvoorwaarde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een randvoorwaarde bij een ontwerp?",
        opties=[
            "een beperking waarbinnen je moet blijven werken",
            "een eis waaraan het eindresultaat moet voldoen",
            "een vermoeden over hoe het ontwerp zal werken",
            "een meting waarmee je het ontwerp beoordeelt",
        ],
        antwoord=0,
        uitleg="Het budget, de tijd en de beschikbare materialen zijn randvoorwaarden. Wat "
        "het resultaat moet kunnen, zijn criteria.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over criteria zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze zijn best meetbaar opgeschreven",
            "je legt ze vast voor je begint te bouwen",
            "je past ze aan zodra het ontwerp niet lukt",
            "ze gaan over het budget en de beschikbare tijd",
        ],
        antwoord=[0, 1],
        uitleg="Criteria achteraf versoepelen zodat je ontwerp wel slaagt, is geen "
        "ontwerpen. Budget en tijd zijn randvoorwaarden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom splits je een ontwerpopdracht in deelproblemen?",
        opties=[
            "omdat je elk stuk apart kan oplossen en testen",
            "omdat je dan minder criteria moet opschrijven",
            "omdat je dan geen prototype meer nodig hebt",
            "omdat je dan sneller aan het bouwen kan gaan",
        ],
        antwoord=0,
        uitleg="Bij een waterzuivering zijn het bezinken, het filtreren en het ontsmetten "
        "elk een eigen probleem. Samen vormen ze de oplossing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een prototype?",
        opties=[
            "een eerste bouwsel waarmee je het idee uittest",
            "een afgewerkt toestel dat zo verkocht kan worden",
            "een tekening op schaal van het hele ontwerp",
            "een verslag waarin je het ontwerp beschrijft",
        ],
        antwoord=0,
        uitleg="Het mag ruw zijn en van karton en tape. De bedoeling is leren wat werkt, "
        "niet iets afleveren.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het ruwe eerste bouwsel waarmee je een ontwerp uittest?",
        antwoord=["een prototype", "prototype", "het prototype"],
        uitleg="Het mag mislukken: dat is net waar het voor dient. Daarna stuur je bij en "
        "test je opnieuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als een prototype niet aan de criteria voldoet?",
        opties=[
            "nagaan waar het faalt en het bijsturen",
            "de criteria versoepelen tot het wel lukt",
            "het ontwerp opgeven en iets anders kiezen",
            "het als eindresultaat afgeven met een nota",
        ],
        antwoord=0,
        uitleg="Ontwerpen gaat in rondes: bouwen, testen, bijsturen, opnieuw testen. Elke "
        "mislukking zegt waar je volgende versie beter moet zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij een ontwerpproces? Kruis alles aan wat juist is.",
        opties=[
            "de criteria en randvoorwaarden vastleggen",
            "het prototype testen en bijsturen",
            "het besluit over de hypothese schrijven",
            "de onafhankelijke variabele vastleggen",
        ],
        antwoord=[0, 1],
        uitleg="Een hypothese en variabelen horen bij onderzoek, niet bij ontwerpen. Een "
        "ontwerp wordt beoordeeld aan zijn criteria.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de letters van STEM?",
        opties=[
            "science, technology, engineering en mathematics",
            "science, techniek, ervaring en mathematics",
            "studie, techniek, engineering en meten",
            "science, technologie, ethiek en meten",
        ],
        antwoord=0,
        uitleg="De vier horen samen: een technisch probleem vraagt wetenschap, techniek, "
        "ontwerp en rekenwerk tegelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ontwerp is pas af als het aan elk opgeschreven criterium voldoet.",
        antwoord=True,
        uitleg="Daarvoor schrijf je ze vooraf op. Haalt het ontwerp een criterium niet, "
        "dan is er nog een ronde nodig.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij ontwerpen hoort één poging, want anders was je plan niet goed.",
        antwoord=False,
        uitleg="Meerdere rondes zijn juist normaal. Elke test wijst aan wat de volgende "
        "versie beter moet doen.",
    ),
    dict(
        type="waarofniet",
        vraag="De kostprijs van een proces kan bepalen of een reactie in de industrie gebruikt wordt.",
        antwoord=True,
        uitleg="Een reactie die chemisch mooi werkt maar te duur is, haalt de fabriek "
        "niet. Daarom zoekt men naar goedkopere katalysatoren en grondstoffen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een wetenschappelijke vondst is altijd meteen klaar voor gebruik.",
        antwoord=False,
        uitleg="Tussen het labo en een product zitten jaren van opschalen, testen en "
        "goedkeuren. Veel vondsten halen die weg nooit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen horen bij het beoordelen van een nieuwe chemische toepassing? Kruis alles aan wat juist is.",
        opties=[
            "wat gebeurt er met de stof na gebruik",
            "wie draagt het risico en wie het voordeel",
            "hoe mooi de verpakking eruitziet",
            "hoe snel de uitvinder bekend wordt",
        ],
        antwoord=[0, 1],
        uitleg="Het gaat over gezondheid, milieu en wie de gevolgen draagt. Die vragen "
        "lossen de cijfers alleen niet op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is opschalen van labo naar fabriek niet vanzelfsprekend?",
        opties=[
            "warmte en menging gedragen zich anders in het groot",
            "de reactievergelijking verandert bij een groter volume",
            "de atoomeconomie daalt altijd bij een groter volume",
            "de reagentia worden zuiverder bij een groter volume",
        ],
        antwoord=0,
        uitleg="In een reactor van duizend liter raak je de warmte veel moeilijker kwijt. "
        "De vergelijking blijft natuurlijk wel dezelfde.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een eis waaraan een ontwerp moet voldoen?",
        antwoord=["een criterium", "criterium", "criteria"],
        uitleg="Een beperking van tijd, geld of materiaal heet een randvoorwaarde. Beide "
        "schrijf je op voor je begint.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen onderzoeken en ontwerpen?",
        opties=[
            "onderzoeken zoekt kennis, ontwerpen zoekt een oplossing",
            "onderzoeken zoekt een oplossing, ontwerpen zoekt kennis",
            "onderzoeken gebeurt in een labo, ontwerpen op papier",
            "onderzoeken gebruikt metingen, ontwerpen gebruikt geen",
        ],
        antwoord=0,
        uitleg="Ook een ontwerper meet natuurlijk. Maar hij meet om na te gaan of zijn "
        "oplossing de criteria haalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hoort een risicoafweging bij een nieuw product?",
        opties=[
            "omdat het voordeel moet opwegen tegen wat het kan kosten",
            "omdat elk nieuw product bij de wet verboden zou zijn",
            "omdat het risico na een afweging volledig verdwijnt",
            "omdat de kostprijs daarmee meteen berekend wordt",
        ],
        antwoord=0,
        uitleg="Geen enkele toepassing is volledig zonder risico. De vraag is of het "
        "voordeel groot genoeg is en wie het risico draagt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een beperking van tijd, geld of materiaal bij een ontwerp?",
        antwoord=["een randvoorwaarde", "randvoorwaarde", "randvoorwaarden"],
        uitleg="Wat het resultaat moet kunnen, is een criterium. De randvoorwaarden zeggen "
        "waarbinnen je moet blijven.",
    ),
]

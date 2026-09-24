# -*- coding: utf-8 -*-
"""De vragen voor "Onderwerp, hoofdgedachte en hoofdpunten" (✨ Spark, Nederlands).

Uit de vakfiche, deel Lezen en luisteren: het onderwerp van een tekst bepalen
in één of enkele woorden, de hoofdgedachte in één zin, de hoofdpunten die die
hoofdgedachte ondersteunen, relevante informatie selecteren uit één of meer
teksten, en notities nemen die je daarna nog kan gebruiken.

Deel 1 legt het verschil tussen onderwerp, hoofdgedachte en hoofdpunt, en
oefent notities nemen. Deel 2 past dat toe op langere fragmenten: hoofdpunt
tegenover detail, samenvatten, en onbekende woorden aanpakken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Een tekst gaat helemaal over hoe je een lekke fietsband herstelt. Hoe noem je dat waarover een tekst gaat?",
        opties=["Het onderwerp", "De hoofdgedachte", "Het besluit", "De inleiding"],
        antwoord=0,
        uitleg="Het onderwerp is waarover de tekst gaat. Je zegt het in één of enkele woorden: hier 'een fietsband herstellen'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de hoofdgedachte van een tekst?",
        opties=[
            "De belangrijkste boodschap, in één zin",
            "Het eerste woord van de titel",
            "Alles wat er in de tekst staat",
            "De mening van de lezer",
        ],
        antwoord=0,
        uitleg="De hoofdgedachte vat in één zin samen wat de tekst over het onderwerp zegt.",
    ),
    dict(
        type="invultekst",
        vraag="Het onderwerp van een tekst zeg je in één of enkele ___.",
        antwoord="woorden",
        uitleg="Het onderwerp is kort: 'huidverzorging', 'zwerfvuil', 'de bus van tien over acht'.",
    ),
    dict(
        type="waarofniet",
        vraag="Het onderwerp van een tekst schrijf je altijd op in een volledige zin.",
        antwoord=False,
        uitleg="Het onderwerp is één of enkele woorden. De hoofdgedachte schrijf je wél in een volledige zin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn onderwerpen en geen hoofdgedachten?",
        opties=[
            "Huidverzorging bij kinderen",
            "Zwerfvuil in onze straat",
            "Elektrische steps",
            "Kinderen smeren te veel crème, en dat is soms ongezond.",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie zijn korte onderwerpen. De laatste is een volledige zin met een boodschap erin: dat is een hoofdgedachte.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een tekst lees je: 'Steeds meer kinderen gebruiken dure gezichtscrèmes. Dat is meestal niet nodig en soms zelfs ongezond.' Wat is de hoofdgedachte?",
        opties=[
            "Kinderen gebruiken veel huidverzorging, terwijl dat niet nodig en soms ongezond is",
            "Gezichtscrème is duur",
            "Huidverzorging",
            "Influencers verdienen geld met reclame",
        ],
        antwoord=0,
        uitleg="De hoofdgedachte is de belangrijkste boodschap in één zin. 'Huidverzorging' is maar het onderwerp, en de prijs is een detail.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn de hoofdpunten van een tekst?",
        opties=[
            "De inhoudelijke elementen die de hoofdgedachte ondersteunen",
            "De moeilijke woorden",
            "De zinnen met een uitroepteken",
            "De tussentitels, letterlijk overgeschreven",
        ],
        antwoord=0,
        uitleg="De hoofdpunten zijn de stukken inhoud waarmee de tekst zijn hoofdgedachte waarmaakt.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoofdpunten ondersteunen de hoofdgedachte van een tekst.",
        antwoord=True,
        uitleg="Ze geven de redenen, de voorbeelden en de gevolgen waarmee de schrijver zijn boodschap onderbouwt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom neem je notities terwijl je naar een reportage luistert?",
        opties=[
            "Om de belangrijkste informatie vast te houden en er daarna mee te werken",
            "Om te tonen dat je aan het opletten bent",
            "Om alles woord voor woord te kunnen herhalen",
            "Omdat dat sneller gaat dan luisteren",
        ],
        antwoord=0,
        uitleg="Je notities moeten duidelijk genoeg zijn om er nadien een samenvatting mee te maken of een vraag mee te beantwoorden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij goede notities?",
        opties=[
            "Afkortingen gebruiken",
            "Symbolen en pijlen gebruiken",
            "In telegramstijl schrijven",
            "Elke zin volledig overschrijven",
        ],
        antwoord=[0, 1, 2],
        uitleg="Notities mogen kort: afkortingen, symbolen en telegramstijl. Alles volledig overschrijven lukt niet en helpt niet.",
    ),
    dict(
        type="invultekst",
        vraag="Een schema waarin je vanuit één centraal woord vertakkingen tekent, heet een ___.",
        antwoord="mindmap",
        uitleg="Een mindmap, een tabel of een schema zijn handige vormen om notities te ordenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zoekt in een lange tekst het antwoord op één bepaalde vraag. Wat noteer je?",
        opties=[
            "Alleen de informatie die met je vraag te maken heeft",
            "De hele tekst, voor het geval dat",
            "Enkel de eerste alinea",
            "De woorden die je niet kent",
        ],
        antwoord=0,
        uitleg="Relevante informatie selecteren betekent: kiezen wat je nodig hebt en de rest laten staan.",
    ),
    dict(
        type="waarofniet",
        vraag="De titel van een tekst geeft je vaak al een idee van het onderwerp.",
        antwoord=True,
        uitleg="De titel, de tussentitels en de afbeeldingen zijn hulpmiddelen om het onderwerp snel te vatten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je het best vóór je een lange tekst helemaal leest?",
        opties=[
            "Je kijkt naar de titel, de tussentitels en de afbeeldingen",
            "Je leest meteen de laatste zin",
            "Je zoekt alle onbekende woorden op",
            "Je telt het aantal alinea's",
        ],
        antwoord=0,
        uitleg="Zo weet je vooraf waarover het gaat, en kan je je afvragen wat je er zelf al over weet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar vind je de hoofdgedachte van een tekst meestal terug?",
        opties=[
            "In de inleiding of in het slot",
            "Altijd in de laatste alinea",
            "In de voorbeelden",
            "In het onderschrift bij een foto",
        ],
        antwoord=0,
        uitleg="Veel teksten kondigen hun boodschap aan in de inleiding en herhalen ze in het slot.",
    ),
    dict(
        type="invultekst",
        vraag="Het besluit van een tekst vind je meestal in het ___.",
        antwoord="slot",
        uitleg="Inleiding, midden en slot: in het slot staat vaak het besluit of de conclusie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke hulpmiddelen in een tekst helpen je om de inhoud te vatten?",
        opties=[
            "De titel en de tussentitels",
            "Woorden die vet gedrukt staan",
            "Een foto of een grafiek bij de tekst",
            "Het aantal letters per zin",
        ],
        antwoord=[0, 1, 2],
        uitleg="Titels, benadrukte woorden en beeld zijn visuele hulpmiddelen. De zinslengte zegt niets over de inhoud.",
    ),
    dict(
        type="waarofniet",
        vraag="Een alinea bevat meestal één kerngedachte.",
        antwoord=True,
        uitleg="Daarom kan je een tekst vaak samenvatten door per alinea één zin te noteren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je luistert naar een reportage over sluikstorten. Welke notitie is het bruikbaarst?",
        opties=[
            "sluikstort kost stad 200 000 euro/jaar",
            "de reporter praatte snel",
            "sluikstorten is niet fijn",
            "de reportage duurde acht minuten",
        ],
        antwoord=0,
        uitleg="Een bruikbare notitie bevat concrete informatie uit de tekst, niet je indruk van de spreker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen het onderwerp en de hoofdgedachte?",
        opties=[
            "Het onderwerp is waarover het gaat, de hoofdgedachte is wat de tekst daarover zegt",
            "Er is geen verschil",
            "Het onderwerp staat altijd in de titel, de hoofdgedachte nooit",
            "De hoofdgedachte is korter dan het onderwerp",
        ],
        antwoord=0,
        uitleg="Onderwerp: 'sluikstorten'. Hoofdgedachte: 'Sluikstorten kost de stad veel geld en de boetes helpen te weinig.'",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Een tekst zegt: veel jongeren slapen te weinig door hun gsm; het blauwe licht houdt hen wakker en meldingen onderbreken hun slaap; wie te weinig slaapt, presteert slechter op school. Wat is de hoofdgedachte?",
        opties=[
            "Jongeren slapen te weinig door hun gsm, en dat heeft gevolgen op school",
            "Blauw licht bestaat",
            "Jongeren kijken graag naar hun gsm",
            "Scholen zouden later moeten beginnen",
        ],
        antwoord=0,
        uitleg="De hoofdgedachte vat oorzaak én gevolg samen. De andere zinnen zijn een detail of iets wat er niet staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij diezelfde tekst: welke zin is een detail en geen hoofdpunt?",
        opties=[
            "De onderzoekers ondervroegen 1 204 leerlingen",
            "Blauw licht houdt je wakker",
            "Meldingen onderbreken je slaap",
            "Wie te weinig slaapt, presteert slechter op school",
        ],
        antwoord=0,
        uitleg="Het precieze aantal ondervraagden is een detail. De drie andere zinnen dragen de hoofdgedachte.",
    ),
    dict(
        type="meerkeuze",
        vraag="De hoofdgedachte is: 'Fietsen naar school is gezonder en sneller dan met de auto gebracht worden.' Welke zinnen zijn hoofdpunten daarbij?",
        opties=[
            "Wie fietst, beweegt elke dag een half uur",
            "In de ochtendspits sta je met de auto stil",
            "Fietsers komen wakkerder toe in de les",
            "De fietsenstalling is blauw geschilderd",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie ondersteunen 'gezonder' en 'sneller'. De kleur van de stalling doet er niets toe.",
    ),
    dict(
        type="waarofniet",
        vraag="In een samenvatting van een tekst zet je ook wat jij er zelf van vindt.",
        antwoord=False,
        uitleg="Een samenvatting geeft de inhoud van de tekst weer. Je mening hoort in een reactie of een recensie, niet in de samenvatting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je komt in een tekst het woord 'wateroverlast' tegen en je kent het niet. Wat doe je eerst?",
        opties=[
            "Je leidt de betekenis af uit de rest van de zin en uit de twee delen van het woord",
            "Je slaat de hele alinea over",
            "Je zoekt elk onbekend woord meteen op",
            "Je vraagt het aan je buur",
        ],
        antwoord=0,
        uitleg="'Water' plus 'overlast': de bouw van het woord en de context geven je de betekenis. Opzoeken doe je voor woorden die je echt nodig hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kan je de betekenis van een onbekend woord afleiden?",
        opties=[
            "Uit de zinnen eromheen",
            "Uit wat je al over het onderwerp weet",
            "Uit de manier waarop het woord gevormd is",
            "Uit het aantal lettergrepen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Context, voorkennis en woordvorming helpen. Soms helpt ook je kennis van het Engels of het Frans. Het aantal lettergrepen zegt niets.",
    ),
    dict(
        type="invultekst",
        vraag="Een woord dat je écht nodig hebt om de tekst te begrijpen en dat je niet kan afleiden, zoek je op in een ___.",
        antwoord="woordenboek",
        uitleg="Op het examen mag je een digitaal woordenboek gebruiken, maar je hebt geen tijd om elk woord op te zoeken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt twee teksten over hetzelfde onderwerp en moet er samen één vraag mee beantwoorden. Wat doe je?",
        opties=[
            "Je zoekt in allebei de teksten wat op jouw vraag antwoordt en legt dat naast elkaar",
            "Je gebruikt alleen de langste tekst",
            "Je neemt de eerste tekst en negeert de tweede",
            "Je telt hoeveel keer een woord voorkomt",
        ],
        antwoord=0,
        uitleg="Relevante informatie selecteren mag ook uit meerdere teksten tegelijk: samen geven ze een vollediger antwoord.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke notitie is het bruikbaarst om achteraf mee te werken?",
        opties=[
            "oorzaak: te weinig slaap → gevolg: slechtere punten",
            "Het was een interessante tekst over slapen en school en de gsm.",
            "slaap",
            "De spreker zei dat het echt wel belangrijk is en dat vond ik ook.",
        ],
        antwoord=0,
        uitleg="Telegramstijl met een pijl houdt het verband vast. Eén los woord zegt te weinig, een volledige zin over je indruk zegt niets over de inhoud.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tekst heeft als titel 'Waarom slapen tieners te weinig?'. Wat verwacht je in die tekst?",
        opties=[
            "Uitleg en oorzaken",
            "Een recept",
            "Een verkoopadvertentie",
            "Een lijst met namen",
        ],
        antwoord=0,
        uitleg="Een vraagtitel die met 'waarom' begint, kondigt oorzaken en uitleg aan. Zo weet je vooraf wat je mag verwachten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen stel je jezelf vóór je begint te lezen of te luisteren?",
        opties=[
            "Wat weet ik hier al over?",
            "Waarover zou deze tekst kunnen gaan?",
            "Van wie is deze tekst en waarom is hij gemaakt?",
            "Hoeveel bladzijden telt de tekst?",
        ],
        antwoord=[0, 1, 2],
        uitleg="Voorkennis ophalen en het communicatiemodel toepassen helpen je begrijpen. Het aantal bladzijden helpt je niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hoofdpunt kan je weglaten zonder dat je de hoofdgedachte nog begrijpt.",
        antwoord=False,
        uitleg="Net niet: hoofdpunten dragen de hoofdgedachte. Wat je wél kan weglaten, zijn de details en de voorbeelden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet een tekst van twee bladzijden samenvatten in vijf zinnen. Wat neem je op?",
        opties=[
            "De hoofdgedachte en de belangrijkste hoofdpunten",
            "De eerste vijf zinnen van de tekst",
            "Alle cijfers uit de tekst",
            "De moeilijkste woorden met hun betekenis",
        ],
        antwoord=0,
        uitleg="Een samenvatting is de hoofdgedachte plus de punten die ze dragen, in je eigen woorden.",
    ),
    dict(
        type="invultekst",
        vraag="De belangrijkste woorden die je tijdens het lezen aanduidt, noem je ___.",
        antwoord="sleutelwoorden",
        uitleg="Sleutelwoorden en kernzinnen aanduiden is een leesstrategie: daarna vind je de inhoud in één oogopslag terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noteer je tijdens het luisteren en niet pas achteraf?",
        opties=[
            "Omdat je een luistertekst niet kan terugbladeren en je snel details vergeet",
            "Omdat je dan sneller klaar bent",
            "Omdat je anders niet mag luisteren",
            "Omdat notities achteraf verboden zijn",
        ],
        antwoord=0,
        uitleg="Een gesproken tekst gaat voorbij. Wie meteen kort noteert, houdt de hoofdpunten vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een tekst over voedselverspilling staat: 'In ons land gooit een gezin gemiddeld 60 kilo eten per jaar weg.' Wat is dit?",
        opties=[
            "Een hoofdpunt met een cijfer dat het ondersteunt",
            "De hoofdgedachte van de tekst",
            "Het onderwerp",
            "Een mening",
        ],
        antwoord=0,
        uitleg="Het is een vaststelling met een cijfer erbij: zo'n zin ondersteunt de boodschap dat er te veel voedsel verloren gaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee teksten over hetzelfde onderwerp kunnen een verschillende hoofdgedachte hebben.",
        antwoord=True,
        uitleg="Het onderwerp kan hetzelfde zijn ('elektrische steps'), terwijl de ene tekst ze aanraadt en de andere ze gevaarlijk noemt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort niet thuis in je notities bij een tekst?",
        opties=[
            "Je eigen oordeel over de stem van de spreker",
            "De cijfers die de spreker noemt",
            "De oorzaken die hij opsomt",
            "Het besluit dat hij trekt",
        ],
        antwoord=0,
        uitleg="Notities bevatten de inhoud van de tekst. Wat jij van de stem vindt, helpt je later niet verder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zinnen kan je gebruiken als kernzin van een alinea?",
        opties=[
            "Sluikstorten kost de gemeente elk jaar handenvol geld.",
            "Camera's blijken het probleem maar deels op te lossen.",
            "De gemeente zoekt daarom naar andere oplossingen.",
            "Het regende die dag pijpenstelen.",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een kernzin vat de alinea samen. Het weer is hier een detail dat niets met de boodschap te maken heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt de hoofdgedachte gevonden, maar één alinea past er niet bij. Wat doe je?",
        opties=[
            "Je herleest die alinea: misschien is het een tegenargument of een nuance",
            "Je schrapt de alinea uit je samenvatting",
            "Je verandert de hoofdgedachte in die van die ene alinea",
            "Je stopt met lezen",
        ],
        antwoord=0,
        uitleg="Teksten geven vaak ook de andere kant. Een tegenargument hoort bij de tekst, en signaalwoorden als 'maar' of 'hoewel' wijzen het aan.",
    ),
]

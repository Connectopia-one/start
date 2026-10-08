# -*- coding: utf-8 -*-
"""Een statistisch onderzoek met de rekenapps.

Het laatste thema van het onderdeel "Werken met grote datasets", en het
leerdoel dat alles samenbrengt:
    "Je analyseert grote datasets met behulp van de rekenapps in functie van
     een statistisch onderzoek."
    "Je interpreteert de resultaten van je statistische analyse in functie
     van een gegeven probleemstelling of onderzoeksvraag."

Daarom gaan de vragen hier niet over één techniek maar over de volgorde: wat
doe je eerst, wat kan je besluiten en waar stopt je besluit. Dat laatste is
het moeilijkst en wordt op het examen het vaakst gevraagd.

De fiche noemt zelf drie websites met datasets om mee te oefenen: de
geboortedatabank van de UHasselt, de open data van Statbel en de csv-datasets
van Kaggle. Ze verwijst ook naar de handleiding "gebruik van de rekenapps
voor statistiek derde graad" op haar eigen website, en zegt uitdrukkelijk dat
je die bij de voorbereiding van dit deel zeker moet gebruiken.

Over exact werken is de fiche streng, en daarover gaan de laatste vragen van
deel 2: je laat breuken, wortels en logaritmen staan als ze niet mooi
uitkomen, en je rekent met zo nauwkeurig mogelijke tussenresultaten. Hoe
onnauwkeuriger je tussenresultaten, hoe meer je eindantwoord afwijkt.

Deel 1 is de gang van een onderzoek.
Deel 2 is het besluit, het ICT-gebruik en het exact werken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de eerste stap van een statistisch onderzoek?",
        opties=[
            "een duidelijke onderzoeksvraag formuleren",
            "de centrummaten van de dataset berekenen",
            "een hypothesetoets uitvoeren op de gegevens",
            "de correlatiecoëfficiënt van twee variabelen berekenen",
        ],
        antwoord=0,
        uitleg="Zonder vraag weet je niet welke berekening zinvol is. Alles wat erna komt, hangt van die vraag af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een dataset van vijfduizend rijen. Wat doe je als tweede, na de onderzoeksvraag?",
        opties=[
            "de data verkennen met een grafiek en een paar kengetallen",
            "meteen een hypothesetoets opstellen en uitvoeren",
            "de dataset in twee helften splitsen en vergelijken",
            "de uitschieters verwijderen voor je begint te rekenen",
        ],
        antwoord=0,
        uitleg="De fiche noemt dat verkennen: groeperen, een frequentietabel maken en een grafiek bekijken. Pas daarna reken je verder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil weten of twee numerieke variabelen in je dataset samenhangen. Wat doe je?",
        opties=[
            "een spreidingsdiagram maken en de correlatiecoëfficiënt berekenen",
            "van elke variabele een boxplot maken en de medianen vergelijken",
            "een hypothesetoets uitvoeren op het gemiddelde van beide",
            "van beide variabelen de modus bepalen en vergelijken",
        ],
        antwoord=0,
        uitleg="Eerst de vorm bekijken, dan het getal berekenen. De fiche vraagt uitdrukkelijk de trendlijn en de correlatiecoëfficiënt samen.",
    ),
    dict(
        type="waarofniet",
        vraag="Je beoordeelt met een grafische voorstelling of de normale verdeling bij je data past.",
        antwoord=True,
        uitleg="Dat staat letterlijk als leerdoel in de fiche. Een histogram is daar het geschiktst voor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vraag stel je je voor je een hypothesetoets op een dataset uitvoert?",
        opties=[
            "zijn de voorwaarden van het formularium voldaan",
            "komt mijn verwachte besluit er wel uit",
            "is mijn dataset groter dan duizend rijen",
            "zijn alle variabelen in dezelfde eenheid",
        ],
        antwoord=0,
        uitleg="Zonder voldane voorwaarden mag je de normale benadering niet gebruiken en is je p-waarde niets waard.",
    ),
    dict(
        type="invultekst",
        vraag="Welke handleiding raadt de fiche aan voor dit onderdeel? Geef het kernwoord in één woord.",
        antwoord=["rekenapps", "rekenapp", "ICT"],
        uitleg="De handleiding gebruik van de rekenapps voor statistiek derde graad, op de website van de examencommissie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een statistisch onderzoek eindigt met de p-waarde of de correlatiecoëfficiënt.",
        antwoord=False,
        uitleg="Het eindigt met een besluit in de taal van de onderzoeksvraag. Een getal alleen is geen antwoord.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoeksvraag gaat over het verschil tussen twee groepen. Welke grafiek kies je om te verkennen?",
        opties=[
            "twee boxplots naast elkaar op dezelfde as",
            "één spreidingsdiagram met alle gegevens",
            "één lijndiagram met de twee groepen na elkaar",
            "één dotplot met beide groepen door elkaar",
        ],
        antwoord=0,
        uitleg="Dan zie je meteen of de centra en de spreidingen verschillen, en of er uitschieters meespelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet in je verkenning een duidelijke uitschieter. Wat doe je eerst?",
        opties=[
            "nagaan of het een invoerfout of een echt bijzonder geval is",
            "de uitschieter verwijderen zodat je analyse klopt",
            "de hele rij uit de dataset schrappen zonder te kijken",
            "de uitschieter vervangen door het gemiddelde",
        ],
        antwoord=0,
        uitleg="Een leeftijd van 250 jaar is een tikfout. Een inkomen van een miljoen kan echt zijn. Kijk altijd eerst.",
    ),
    dict(
        type="waarofniet",
        vraag="De fiche verwijst naar websites met datasets om een statistisch onderzoek op te oefenen.",
        antwoord=True,
        uitleg="Ze noemt de geboortedatabank van de UHasselt, de open data van Statbel en de datasets van Kaggle.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom maak je een grafiek vóór je kengetallen berekent?",
        opties=[
            "omdat een grafiek de vorm toont die een getal kan verbergen",
            "omdat een rekenapp zonder grafiek geen kengetallen geeft",
            "omdat een grafiek nauwkeuriger is dan een kengetal",
            "omdat de fiche een grafiek verplicht bij elke berekening",
        ],
        antwoord=0,
        uitleg="Twee toppen, een scheve staart of een uitschieter: dat zie je in een beeld en niet in een gemiddelde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze onderzoeksvragen is statistisch bruikbaar?",
        opties=[
            "is de gemiddelde slaapduur van zestienjarigen korter dan acht uur",
            "is slapen belangrijk voor jongeren in onze samenleving",
            "wat vindt de gemiddelde jongere van zijn eigen slaap",
            "hoe zou een goede nachtrust eruit moeten zien",
        ],
        antwoord=0,
        uitleg="Ze noemt een grootheid, een groep en een grens. Daar kan je een hypothesetoets op bouwen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het vooraf gekozen getal waarmee je de p-waarde vergelijkt? Twee woorden.",
        antwoord=["significantieniveau", "het significantieniveau", "significantie niveau"],
        uitleg="Het significantieniveau alfa, meestal nul komma nul vijf.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag je onderzoeksvraag aanpassen nadat je de resultaten gezien hebt.",
        antwoord=False,
        uitleg="Dan vind je altijd wel iets. Een vraag die je na de data verzint, kan je met die data niet meer toetsen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je dataset bevat lege cellen bij een paar honderd rijen. Wat is een verantwoorde aanpak?",
        opties=[
            "vermelden hoeveel gegevens ontbreken en zeggen hoe je ermee omgaat",
            "de lege cellen op nul zetten en gewoon verder rekenen",
            "de lege cellen vullen met het gemiddelde zonder het te melden",
            "de hele dataset weggooien en een nieuwe opvragen",
        ],
        antwoord=0,
        uitleg="Ontbrekende gegevens op nul zetten verlaagt je gemiddelde zonder dat iemand het ziet. Dat is het ergste van de vier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vindt r gelijk aan 0,78 tussen twee variabelen in een dataset. Wat besluit je?",
        opties=[
            "er is een sterk positief lineair verband, maar geen oorzaak aangetoond",
            "de ene variabele veroorzaakt duidelijk de andere",
            "er is helemaal geen verband tussen de twee, want 0,78 is kleiner dan één",
            "de twee variabelen zijn identiek aan elkaar",
        ],
        antwoord=0,
        uitleg="Boven 0,7 is de samenhang sterk volgens het formularium. Over oorzaak zegt r niets.",
    ),
    dict(
        type="waarofniet",
        vraag="Een onderzoek op een dataset van tienduizend rijen kan nog altijd een vertekend besluit geven.",
        antwoord=True,
        uitleg="Als de gegevens eenzijdig verzameld zijn, helpt omvang niet. Vraag je altijd af wie er in de dataset zit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stap hoort niet bij het verkennen van een dataset volgens de fiche?",
        opties=[
            "de nulhypothese verwerpen op basis van een eerste blik",
            "de gegevens groeperen in klassen",
            "een frequentietabel met absolute en relatieve frequenties opstellen",
            "de nodige grafische voorstellingen maken",
        ],
        antwoord=0,
        uitleg="Verkennen is kijken. Verwerpen komt pas na een toets met hypothesen, voorwaarden en een p-waarde.",
    ),
    dict(
        type="invultekst",
        vraag="Welke grafiek gebruik je om te beoordelen of de normale verdeling bij je data past? Eén woord.",
        antwoord=["histogram", "een histogram"],
        uitleg="Een histogram: daar zie je of de vorm klokvormig en symmetrisch is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling berekent twintig kengetallen voor hij zijn vraag stelt. Wat zou je hem zeggen?",
        opties=[
            "begin bij je vraag, dan weet je welke twee of drie getallen je nodig hebt",
            "twintig kengetallen zijn nooit genoeg voor een grote dataset",
            "hij moet eerst alle grafieken maken en dan de getallen",
            "hij moet de kengetallen met de hand controleren na de rekenapp",
        ],
        antwoord=0,
        uitleg="Alles berekenen en dan iets opvallends uitkiezen, is net de manier om een vals verband te vinden.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent exact werken volgens de vakfiche?",
        opties=[
            "een wiskundige uitdrukking niet benaderen of afronden",
            "met zoveel decimalen rekenen als je rekenapp toont",
            "elke tussenstap op twee decimalen afronden",
            "alle antwoorden in breukvorm noteren",
        ],
        antwoord=0,
        uitleg="Breuken, wortels en logaritmen laat je staan als ze niet mooi uitkomen. Dat staat letterlijk in de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom rekent de fiche met zo nauwkeurig mogelijke tussenresultaten?",
        opties=[
            "omdat afrondingsfouten in de tussenstappen doorwerken in je eindantwoord",
            "omdat een rekenapp anders een foutmelding geeft",
            "omdat je anders geen exact antwoord meer mag noteren in je besluit",
            "omdat de verbetering alleen decimalen nakijkt",
        ],
        antwoord=0,
        uitleg="De fiche zegt het zo: hoe onnauwkeuriger je tussenresultaten, hoe meer je eindresultaat kan afwijken.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een vraag met het icoon voor functioneel ICT-gebruik moet je nog altijd je tussenstappen uitschrijven.",
        antwoord=True,
        uitleg="De fiche vraagt dat bij allebei de iconen: je toont je werkwijze en je redenering en schrijft alle berekeningen uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke hulpmiddelen mag je volgens de fiche tijdens het examen gebruiken?",
        opties=[
            "de rekenapps, een online rekentoestel, een spellingcontrole en een woordenboek",
            "je eigen grafische rekentoestel, een woordenboek en een samenvatting op papier",
            "elk digitaal hulpmiddel zolang je geen internet gebruikt",
            "alleen een balpen en kladpapier, verder niets",
        ],
        antwoord=0,
        uitleg="De links zitten in het examen zelf. Andere ICT-middelen laat de examencommissie niet toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je besluit uit je toets: ik verwerp H0 op het niveau van vijf procent. Wat moet er nog bij?",
        opties=[
            "wat dat betekent voor de onderzoeksvraag waarmee je begon",
            "de volledige kansverdeling van je steekproefvariabele",
            "het aantal decimalen dat je rekenapp gaf",
            "een tweede toets op een ander significantieniveau",
        ],
        antwoord=0,
        uitleg="De fiche vraagt letterlijk dat je je resultaten interpreteert in functie van de gegeven probleemstelling.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel minuten duurt het examen statistiek? Geef het getal in cijfers.",
        antwoord=["150"],
        uitleg="Honderdvijftig minuten, in het examencentrum in Brussel.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een opgave met het icoon voor werken zonder ICT mag je je rekenapp toch voor het rekenwerk gebruiken.",
        antwoord=False,
        uitleg="Dan los je de vraag zonder ICT op. Het andere icoon, voor functioneel ICT-gebruik, laat de rekenapp wel toe ter ondersteuning van het rekenwerk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vindt een sterk verband tussen twee variabelen in een dataset over gemeenten. Wat mag je besluiten?",
        opties=[
            "dat de twee samenhangen in deze gemeenten, niets over oorzaak",
            "dat de ene variabele de andere veroorzaakt in deze gemeenten",
            "dat het verband ook voor individuele mensen geldt",
            "dat het verband in elk land ter wereld opgaat",
        ],
        antwoord=0,
        uitleg="Een verband tussen gemiddelden van groepen geldt niet automatisch voor de mensen in die groepen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noteer je bij een open vraag je werkwijze en niet enkel het antwoord?",
        opties=[
            "omdat het correcte gebruik van begrippen en notaties mee je resultaat bepaalt",
            "omdat een rekenapp het antwoord soms verkeerd berekent",
            "omdat de verbetering anders denkt dat je gegokt hebt",
            "omdat een antwoord zonder uitleg niet leesbaar is",
        ],
        antwoord=0,
        uitleg="Dat staat zo in de fiche, bij hoe het examen beoordeeld wordt. De begrippen uit de bijlage zijn de enige die gelden.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij sommige vragen van dit examen noteer je je antwoord op een schrijftablet met een digitale pen.",
        antwoord=True,
        uitleg="De fiche zegt dat erbij en verwijst naar de pagina over examens met een schrijftablet om te oefenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel weegt het onderdeel werken met grote datasets op het examen?",
        opties=["veertig procent", "zestig procent", "vijftig procent", "dertig procent"],
        antwoord=0,
        uitleg="Telproblemen, kansrekenen en statistiek weegt zestig procent, werken met grote datasets veertig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je rondt een tussenresultaat af op twee decimalen en je eindantwoord wijkt af van het model. Wat was de fout?",
        opties=[
            "te vroeg afronden, reken verder met de volle nauwkeurigheid",
            "het verkeerde kengetal kiezen voor deze opgave",
            "de rekenapp gebruiken in plaats van met de hand te rekenen",
            "het eindantwoord op twee decimalen noteren",
        ],
        antwoord=0,
        uitleg="Rond pas af op het einde. Twee decimalen in een tussenstap kan in het eindantwoord een eenheid schelen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel procent weegt het onderdeel telproblemen, kansrekenen en statistiek? Geef het getal in cijfers.",
        antwoord=["60", "60 procent"],
        uitleg="Zestig procent, tegen veertig voor het werken met grote datasets.",
    ),
    dict(
        type="waarofniet",
        vraag="Een opgave kan ook een probleem zijn dat je niet aan één hoofdstuk van de fiche kan koppelen.",
        antwoord=True,
        uitleg="De fiche onderscheidt een vraagstuk, dat bij één hoofdstuk hoort, van een probleem, waar je leerinhouden combineert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je analyse geeft geen significant resultaat. Wat schrijf je in je besluit?",
        opties=[
            "deze data geven te weinig bewijs voor het vermoeden",
            "het vermoeden is hiermee weerlegd",
            "er is zeker geen verschil tussen de groepen",
            "de dataset was ongeschikt voor dit soort onderzoek",
        ],
        antwoord=0,
        uitleg="Geen bewijs vinden is geen bewijs van geen effect. Dat onderscheid wordt nagekeken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee variabelen in je dataset hebben r gelijk aan 0,15. Wat is je besluit over de trendlijn?",
        opties=[
            "een trendlijn is hier weinig zinvol, de samenhang is zwak",
            "de trendlijn beschrijft de data hier uitstekend",
            "je moet de trendlijn door de oorsprong laten gaan",
            "je kan met deze trendlijn gerust ver vooruit voorspellen",
        ],
        antwoord=0,
        uitleg="Tussen nul en 0,3 is de samenhang zwak positief. Een rechte door zo'n wolk voorspelt bijna niets.",
    ),
    dict(
        type="waarofniet",
        vraag="Een antwoord dat enkel uit het resultaat van een rekenapp bestaat, is op dit examen voldoende.",
        antwoord=False,
        uitleg="De fiche vraagt bij open vragen altijd je werkwijze, je redenering en alle tussenstappen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een opgave met context en een opgave zonder context?",
        opties=[
            "met context vertrekt ze van een concrete situatie, zonder context niet",
            "met context mag je ICT gebruiken, zonder context niet",
            "met context is ze altijd moeilijker dan zonder context",
            "zonder context hoef je je werkwijze niet te noteren",
        ],
        antwoord=0,
        uitleg="De fiche vraagt je om op allebei voorbereid te zijn, en bij veel leerdoelen uitdrukkelijk op opgaven met context.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt een gemiddelde, een standaardafwijking, een p-waarde en een correlatiecoëfficiënt berekend. Wat zet je in je besluit?",
        opties=[
            "enkel de getallen die je onderzoeksvraag echt beantwoorden",
            "alle vier de getallen, want je hebt ze berekend",
            "enkel het getal met de kleinste waarde van de vier",
            "enkel de p-waarde, want die beslist alles",
        ],
        antwoord=0,
        uitleg="Een besluit is geen opsomming. Wat de vraag niet beantwoordt, hoort in je werkblad en niet in je conclusie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling meldt een p-waarde met acht decimalen en noemt dat exact werken. Wat zeg je?",
        opties=[
            "exact werken gaat over niet afronden, niet over veel decimalen",
            "acht decimalen zijn te weinig, de fiche vraagt er tien",
            "hij moet alle decimalen weglaten en afronden op een geheel getal",
            "hij heeft gelijk, hoe meer decimalen hoe exacter",
        ],
        antwoord=0,
        uitleg="Exact werken betekent een breuk of een wortel laten staan. Acht decimalen in een besluit helpen de lezer niet.",
    ),
]

# -*- coding: utf-8 -*-
"""Ongevallen herkennen en eerste hulp geven.

Het blok "ik reageer correct in een noodsituatie" weegt 7,5 procent en valt bij
ons uiteen in twee thema's. Dit is het eerste: de ongevallen zelf, de zes
basisprincipes, de vier stappen en de noodnummers.

Alles hieronder komt letterlijk uit de fiche. Verzin hier niets bij: dit is het
enige thema van het vak waar een verkeerd antwoord in het echte leven
gevaarlijk is.

De ongevallen en noodsituaties uit de fiche:
    bloeding; hart- en ademhalingsstilstand; letsels aan botten, spieren en
    gewrichten (botbreuk, kneuzing, ontwrichting, verstuiking); verdrinking;
    verslikking; wonden (huidwonde, brandwonde)

De zes basisprincipes van eerste hulp:
    blijf rustig in een noodsituatie; vermijd besmetting; handel als eerste
    hulpverlener; zorg voor het comfort van het slachtoffer; verleen
    psychosociale hulp; houd rekening met emotionele reacties achteraf

De vier stappen, in deze volgorde:
    1 zorg voor veiligheid
    2 beoordeel de toestand van het slachtoffer
    3 raadpleeg gespecialiseerde hulp
    4 verleen verdere eerste hulp

De noodnummers:
    101           politie
    112           ziekenwagen en brandweer
    070 245 245   antigifcentrum
    1733          huisarts of huisartsenwachtpost

De fiche vraagt niet enkel die rijtjes op te sommen, maar ook te beoordelen of
iemand ze in een gegeven situatie correct heeft toegepast. Daarom staan hier
veel situatievragen.

Deel 1 is de ongevallen en de noodnummers.
Deel 2 is de zes basisprincipes en de vier stappen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welk noodnummer bel je voor een ziekenwagen?",
        opties=["112", "101", "1733", "070 245 245"],
        antwoord=0,
        uitleg="112 is voor de ziekenwagen en de brandweer samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk noodnummer bel je voor de politie?",
        opties=["101", "112", "1733", "070 245 245"],
        antwoord=0,
        uitleg="101 is het nummer van de politie. 112 is de ziekenwagen en de brandweer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kind heeft een product uit de kelder gedronken. Welk nummer bel je volgens de fiche?",
        opties=["070 245 245", "1733", "101", "112"],
        antwoord=0,
        uitleg="070 245 245 is het antigifcentrum. Bij een bewusteloos kind bel je 112.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het is zondagavond en je hebt dringend een huisarts nodig, maar het is geen levensgevaar. Welk nummer bel je?",
        opties=["1733", "112", "101", "070 245 245"],
        antwoord=0,
        uitleg="1733 brengt je bij de huisarts of de huisartsenwachtpost.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke letsels aan botten, spieren en gewrichten noemt de fiche?",
        opties=[
            "botbreuk, kneuzing, ontwrichting en verstuiking",
            "botbreuk, bloeding, brandwonde en verslikking",
            "kneuzing, verdrinking, verstuiking en bloeding",
            "ontwrichting, huidwonde, brandwonde en verdrinking",
        ],
        antwoord=0,
        uitleg="De andere rijtjes mengen er noodsituaties en wonden bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een ontwrichting?",
        opties=[
            "een bot dat uit het gewricht geschoven is",
            "een bot dat in twee gebroken is",
            "een gekneusde spier zonder scheur",
            "een band rond een gewricht die uitgerekt is",
        ],
        antwoord=0,
        uitleg="Bij een verstuiking zijn de banden overrekt, bij een ontwrichting staat het bot uit het gewricht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een verstuiking?",
        opties=[
            "de banden rond een gewricht zijn te ver uitgerekt",
            "het bot is uit het gewricht geschoven",
            "het bot is gebroken maar de huid is heel",
            "de spier is tot bloedens toe geraakt",
        ],
        antwoord=0,
        uitleg="Een verstuiking zit in de banden, een ontwrichting in de stand van het bot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee soorten wonden noemt de fiche?",
        opties=[
            "de huidwonde en de brandwonde",
            "de open en de gesloten wonde",
            "de snijwonde en de schaafwonde",
            "de diepe en de oppervlakkige wonde",
        ],
        antwoord=0,
        uitleg="De fiche noemt enkel die twee bij wonden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand verslikt zich en kan niet meer praten of hoesten. Wat is dit volgens de fiche?",
        opties=[
            "een noodsituatie",
            "een letsel aan de spieren",
            "een huidwonde",
            "een kneuzing van de luchtweg",
        ],
        antwoord=0,
        uitleg="Verslikking staat in het rijtje van ongevallen en noodsituaties.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een hart- en ademhalingsstilstand?",
        opties=[
            "het hart pompt niet meer en de ademhaling valt stil",
            "het hart klopt te snel en de ademhaling versnelt",
            "de bloeddruk valt weg terwijl het hart doorklopt",
            "de ademhaling stokt even door schrik",
        ],
        antwoord=0,
        uitleg="Hart- en ademhalingsstilstand staat als één noodsituatie in de fiche.",
    ),
    dict(
        type="waarofniet",
        vraag="112 is in België het nummer voor de ziekenwagen en de brandweer.",
        antwoord=True,
        uitleg="Zo staat het in de fiche, naast 101 voor de politie.",
    ),
    dict(
        type="waarofniet",
        vraag="Je belt 101 als iemand zwaar bloedt en dringend een ziekenwagen nodig heeft.",
        antwoord=False,
        uitleg="101 is de politie. Voor een ziekenwagen bel je 112.",
    ),
    dict(
        type="waarofniet",
        vraag="Verdrinking staat in de fiche bij de ongevallen en noodsituaties.",
        antwoord=True,
        uitleg="Ze staat er naast bloeding, verslikking, wonden en de letsels aan botten en gewrichten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kneuzing en een botbreuk zijn volgens de fiche hetzelfde letsel.",
        antwoord=False,
        uitleg="Het zijn twee verschillende letsels in hetzelfde rijtje van vier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke noodsituaties noemt de fiche?",
        opties=["bloeding", "verslikking", "verdrinking", "uitdroging"],
        antwoord=[0, 1, 2],
        uitleg="Uitdroging staat niet in het rijtje. Bloeding, verslikking en verdrinking wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke nummers staan in de fiche als noodnummer?",
        opties=["101", "112", "1733", "100"],
        antwoord=[0, 1, 2],
        uitleg="100 staat niet in de fiche. Het vierde nummer dat er wel staat, is 070 245 245 van het antigifcentrum.",
    ),
    dict(
        type="invultekst",
        vraag="Welk nummer bel je voor de brandweer?",
        antwoord=["112"],
        uitleg="112 geldt voor de ziekenwagen en voor de brandweer.",
    ),
    dict(
        type="invultekst",
        vraag="Welk nummer bel je bij een vergiftiging zonder bewustzijnsverlies?",
        antwoord=["070 245 245", "070245245"],
        uitleg="Dat is het antigifcentrum. Bij bewustzijnsverlies bel je 112.",
    ),
    dict(
        type="invultekst",
        vraag="Welk nummer bel je als je buiten de uren een huisarts zoekt?",
        antwoord=["1733"],
        uitleg="1733 brengt je bij de huisarts of de huisartsenwachtpost.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand valt van een ladder en de arm staat in een vreemde hoek. Welk letsel vermoed je?",
        opties=[
            "een botbreuk of een ontwrichting",
            "een kneuzing van de huid",
            "een brandwonde aan de arm",
            "een verslikking door de schrik",
        ],
        antwoord=0,
        uitleg="Een vreemde stand wijst op een breuk of op een bot dat uit het gewricht staat.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel basisprincipes van eerste hulp noemt de fiche?",
        opties=["zes", "vier", "vijf", "zeven"],
        antwoord=0,
        uitleg="Zes basisprincipes, en daarnaast vier stappen. Verwar die twee aantallen niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het eerste basisprincipe van eerste hulp?",
        opties=[
            "blijf rustig in een noodsituatie",
            "bel onmiddellijk het noodnummer",
            "verplaats het slachtoffer naar een veilige plek",
            "zoek iemand met een diploma eerste hulp",
        ],
        antwoord=0,
        uitleg="Rustig blijven staat vooraan in het rijtje van zes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt de fiche met het basisprincipe vermijd besmetting?",
        opties=[
            "bescherm jezelf en het slachtoffer tegen overdracht van ziekten",
            "raak het slachtoffer helemaal niet aan",
            "houd andere mensen op afstand van de plaats",
            "desinfecteer de wonde met alcohol",
        ],
        antwoord=0,
        uitleg="Het gaat om besmetting in twee richtingen, van jou naar het slachtoffer en omgekeerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het basisprincipe verleen psychosociale hulp?",
        opties=[
            "sta het slachtoffer ook bij met woorden en nabijheid",
            "breng het slachtoffer naar een psycholoog",
            "vraag het slachtoffer wat er precies gebeurd is",
            "laat het slachtoffer alleen om te kalmeren",
        ],
        antwoord=0,
        uitleg="Naast de lichamelijke zorg vraagt de fiche ook aandacht voor hoe iemand zich voelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk basisprincipe gaat over wat er ná de noodsituatie gebeurt?",
        opties=[
            "houd rekening met emotionele reacties achteraf",
            "zorg voor het comfort van het slachtoffer",
            "handel als eerste hulpverlener",
            "vermijd besmetting",
        ],
        antwoord=0,
        uitleg="Ook jij als hulpverlener kan achteraf nog reageren. De fiche noemt dat als zesde principe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de eerste van de vier stappen in eerste hulp?",
        opties=[
            "zorg voor veiligheid",
            "beoordeel de toestand van het slachtoffer",
            "raadpleeg gespecialiseerde hulp",
            "verleen verdere eerste hulp",
        ],
        antwoord=0,
        uitleg="Veiligheid komt eerst, voor jezelf en voor het slachtoffer. Anders word jij het tweede slachtoffer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de tweede stap in eerste hulp?",
        opties=[
            "beoordeel de toestand van het slachtoffer",
            "zorg voor veiligheid",
            "raadpleeg gespecialiseerde hulp",
            "verleen verdere eerste hulp",
        ],
        antwoord=0,
        uitleg="Pas als het veilig is, kijk je hoe het slachtoffer eraan toe is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de derde stap in eerste hulp?",
        opties=[
            "raadpleeg gespecialiseerde hulp",
            "verleen verdere eerste hulp",
            "beoordeel de toestand van het slachtoffer",
            "zorg voor veiligheid",
        ],
        antwoord=0,
        uitleg="Hulp inroepen komt vóór de verdere zorg, zodat de ambulance onderweg is terwijl jij helpt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de vierde en laatste stap in eerste hulp?",
        opties=[
            "verleen verdere eerste hulp",
            "raadpleeg gespecialiseerde hulp",
            "zorg voor veiligheid",
            "beoordeel de toestand van het slachtoffer",
        ],
        antwoord=0,
        uitleg="Na het inroepen van hulp blijf je zelf verder helpen tot de hulpdiensten er zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een auto staat midden op de rijweg met een gewonde erin. Wat doe je eerst?",
        opties=[
            "zorgen dat de plaats veilig is",
            "de gewonde uit de auto halen",
            "de toestand van de gewonde beoordelen",
            "de gewonde comfortabel leggen",
        ],
        antwoord=0,
        uitleg="Stap 1 is veiligheid. Wie dat overslaat, loopt zelf gevaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Je beoordeelt de toestand van het slachtoffer vóór je voor veiligheid zorgt.",
        antwoord=False,
        uitleg="Omgekeerd: veiligheid is stap 1, de toestand beoordelen stap 2.",
    ),
    dict(
        type="waarofniet",
        vraag="Rustig blijven is volgens de fiche een van de zes basisprincipes.",
        antwoord=True,
        uitleg="Het staat als eerste in het rijtje.",
    ),
    dict(
        type="waarofniet",
        vraag="Gespecialiseerde hulp inroepen is de laatste van de vier stappen.",
        antwoord=False,
        uitleg="Het is de derde. Daarna verleen je nog verdere eerste hulp.",
    ),
    dict(
        type="waarofniet",
        vraag="Zorgen voor het comfort van het slachtoffer staat bij de zes basisprincipes.",
        antwoord=True,
        uitleg="Het staat er samen met psychosociale hulp en de emotionele reacties achteraf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn basisprincipes van eerste hulp volgens de fiche?",
        opties=[
            "vermijd besmetting",
            "handel als eerste hulpverlener",
            "verleen psychosociale hulp",
            "noteer de gegevens van de getuigen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Getuigen noteren hoort bij een schadegeval en een verzekering, niet bij de eerste hulp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn stappen in eerste hulp volgens de fiche?",
        opties=[
            "zorg voor veiligheid",
            "beoordeel de toestand van het slachtoffer",
            "raadpleeg gespecialiseerde hulp",
            "blijf rustig in een noodsituatie",
        ],
        antwoord=[0, 1, 2],
        uitleg="Rustig blijven is een basisprincipe, geen stap. De vierde stap is verdere eerste hulp verlenen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stap komt volgens de fiche altijd eerst in eerste hulp? Antwoord met één woord.",
        antwoord=["veiligheid", "veilig"],
        uitleg="Zorg voor veiligheid is stap 1 van de vier.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel stappen in eerste hulp noemt de fiche? Antwoord met een cijfer.",
        antwoord=["4", "vier"],
        uitleg="Vier stappen, naast de zes basisprincipes.",
    ),
    dict(
        type="invultekst",
        vraag="Welk basisprincipe gaat over ziekten die van de ene naar de andere kunnen overgaan?",
        antwoord=["vermijd besmetting", "besmetting"],
        uitleg="Vermijd besmetting is het tweede van de zes basisprincipes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand heeft eerste hulp gegeven maar is de gewonde zonder iets te zeggen voorbijgelopen om eerst een ambulance te bellen van thuis uit. Wat liep er mis?",
        opties=[
            "hij beoordeelde de toestand van het slachtoffer niet",
            "hij zorgde niet voor zijn eigen veiligheid",
            "hij verleende te veel verdere eerste hulp",
            "hij belde het verkeerde noodnummer",
        ],
        antwoord=0,
        uitleg="Stap 2 is overgeslagen, en zonder die beoordeling weet de centrale ook niet wat ze moet sturen.",
    ),
]

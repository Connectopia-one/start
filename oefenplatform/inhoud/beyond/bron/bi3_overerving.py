# -*- coding: utf-8 -*-
"""Overerving en de wetten van Mendel — 🌍 Beyond, biologie.

Deel 1 gaat over de experimenten van Mendel, over de drie wetten die hij
eruit afleidde, en over het rekenen met een kruisingsschema: monohybride en
dihybride kruisingen, genotype en fenotype, en de verhoudingen die je
verwacht. Deel 2 gaat over de gevallen die niet in het schema van Mendel
passen: intermediaire en codominante kenmerken, multipele allelen,
geslachtsgebonden en gekoppelde genen, letale allelen en polygenie, en over
het lezen van een stamboom.

De fiche vraagt uitdrukkelijk dat de leerling geneticavraagstukken oplost.
Daarom staat in beide delen een reeks vragen waar echt geteld moet worden in
een kruisingsschema, en niet alleen de namen van de wetten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarom was de erwtenplant geschikt voor de proeven van Mendel? Kruis alles aan wat juist is.",
        opties=[
            "haar kenmerken zijn duidelijk te onderscheiden",
            "ze kan zichzelf bestuiven",
            "ze heeft maar één chromosoom",
            "ze plant zich niet geslachtelijk voort",
        ],
        antwoord=[0, 1],
        uitleg="Kenmerken als geel of groen en rond of gerimpeld zijn goed te "
        "onderscheiden. Door zelfbestuiving kon hij bovendien raszuivere lijnen krijgen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een plant die voor een kenmerk twee dezelfde allelen heeft?",
        antwoord=["homozygoot", "raszuiver", "homozygoot plant"],
        uitleg="Homozygoot of raszuiver betekent twee dezelfde allelen, bijvoorbeeld AA of "
        "aa. Met twee verschillende allelen is een plant heterozygoot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een genotype en een fenotype?",
        opties=[
            "het genotype zijn de allelen, het fenotype het uitzicht",
            "het genotype is het uitzicht, het fenotype zijn de allelen",
            "het genotype geldt voor de ouders, het fenotype voor de kinderen",
            "er is geen verschil tussen de twee",
        ],
        antwoord=0,
        uitleg="Twee planten met genotype AA en Aa kunnen er precies hetzelfde uitzien. "
        "Hun fenotype is dus gelijk, hun genotype niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Kruis je twee raszuivere ouders met een verschillend kenmerk, wat zie je dan in de F1?",
        opties=[
            "alle nakomelingen lijken op elkaar",
            "de helft lijkt op elke ouder",
            "er komt een verhouding 3 op 1",
            "er komt een verhouding 9 op 3 op 3 op 1",
        ],
        antwoord=0,
        uitleg="Dat is de uniformiteitswet: de hele F1 is heterozygoot en toont het "
        "dominante kenmerk. De splitsing komt pas in de F2.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de wet die zegt dat de hele eerste generatie op elkaar lijkt?",
        antwoord=["uniformiteitswet", "de uniformiteitswet", "eerste wet"],
        uitleg="De uniformiteitswet geldt als je start van twee raszuivere ouders. Daarna "
        "volgen de splitsingswet en de onafhankelijkheidswet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verhouding van fenotypes verwacht je in de F2 van een monohybride kruising met een dominant kenmerk?",
        opties=[
            "3 op 1",
            "1 op 1",
            "1 op 2 op 1",
            "9 op 3 op 3 op 1",
        ],
        antwoord=0,
        uitleg="Van de vier vakjes in het schema tonen er drie het dominante kenmerk. De "
        "verhouding van de genotypes is daar 1 op 2 op 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verhouding van genotypes hoort bij die F2?",
        opties=[
            "1 AA, 2 Aa en 1 aa",
            "3 AA en 1 aa",
            "2 AA en 2 aa",
            "4 Aa",
        ],
        antwoord=0,
        uitleg="Aa gekruist met Aa geeft AA, Aa, Aa en aa. Daardoor zien drie van de vier "
        "er dominant uit, terwijl maar één van de vier raszuiver dominant is.",
    ),
    dict(
        type="waarofniet",
        vraag="Een plant met genotype Aa geeft bij de meiose twee soorten gameten: A en a.",
        antwoord=True,
        uitleg="De twee allelen gaan naar verschillende gameten, elk in de helft van de "
        "gevallen. Dat is de kern van de splitsingswet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de onafhankelijkheidswet?",
        opties=[
            "twee kenmerken erven onafhankelijk van elkaar over",
            "twee kenmerken erven altijd samen over",
            "een dominant allel wordt altijd doorgegeven",
            "de F1 is altijd raszuiver",
        ],
        antwoord=0,
        uitleg="De wet geldt voor genen op verschillende chromosomen. Liggen twee genen op "
        "hetzelfde chromosoom, dan erven ze vaak gekoppeld over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verhouding verwacht je in de F2 van een dihybride kruising met twee dominante kenmerken?",
        opties=[
            "9 op 3 op 3 op 1",
            "3 op 1",
            "1 op 2 op 1",
            "1 op 1 op 1 op 1",
        ],
        antwoord=0,
        uitleg="Het schema heeft dan zestien vakjes. Negen tonen beide dominante "
        "kenmerken, drie en drie telkens één ervan, en één de twee recessieve.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel soorten gameten maakt een plant met genotype AaBb?",
        opties=[
            "vier",
            "twee",
            "drie",
            "zestien",
        ],
        antwoord=0,
        uitleg="De combinaties zijn AB, Ab, aB en ab, elk in een kwart van de gameten. "
        "Daarom heeft een dihybrid kruisingsschema vier rijen en vier kolommen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het vierkante schema waarin je de gameten van beide ouders tegen elkaar uitzet?",
        antwoord=["punnettvierkant", "punnett vierkant", "kruisingsschema"],
        uitleg="In een Punnettvierkant staan de gameten van de ene ouder boven en die van "
        "de andere links. In elk vakje schrijf je de combinatie die dan ontstaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Kruis Aa met aa. Welk deel van de nakomelingen toont het recessieve kenmerk?",
        opties=[
            "de helft",
            "een kwart",
            "drie kwart",
            "niemand",
        ],
        antwoord=0,
        uitleg="De gameten zijn A en a tegenover a en a. Twee van de vier vakjes geven aa, "
        "dus de helft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe weet je of een plant met een dominant uitzicht AA of Aa is?",
        opties=[
            "door ze te kruisen met een recessieve plant",
            "door ze met zichzelf te kruisen in de F1",
            "door haar fenotype nauwkeurig te meten",
            "dat is onmogelijk te weten",
        ],
        antwoord=0,
        uitleg="Komt er bij een kruising met aa ook maar één recessieve nakomeling, dan was "
        "de plant Aa. Zijn ze allemaal dominant, dan was ze waarschijnlijk AA.",
    ),
    dict(
        type="waarofniet",
        vraag="Een recessief kenmerk kan alleen te zien zijn bij een homozygoot recessief genotype.",
        antwoord=True,
        uitleg="Eén dominant allel volstaat om het dominante kenmerk te tonen. Pas met aa "
        "komt het recessieve kenmerk tevoorschijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt voor twee homologe chromosomen bij de overerving? Kruis alles aan wat juist is.",
        opties=[
            "ze dragen hetzelfde gen op dezelfde locus",
            "de allelen op die locus kunnen verschillen",
            "ze komen allebei van dezelfde ouder",
            "ze gaan samen naar één gameet",
        ],
        antwoord=[0, 1],
        uitleg="Op dezelfde locus zit hetzelfde gen, maar niet noodzakelijk hetzelfde "
        "allel. Bij de meiose gaan de twee homologen naar verschillende gameten.",
    ),
    dict(
        type="waarofniet",
        vraag="Mendel kende de chromosomen en het DNA al toen hij zijn wetten opstelde.",
        antwoord=False,
        uitleg="Hij werkte met wat hij erffactoren noemde en kende de chromosomen niet. Pas "
        "veertig jaar later werd zijn werk met de chromosomen in verband gebracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de P-generatie in een kruisingsschema?",
        opties=[
            "de ouders waarmee je start",
            "de eerste generatie nakomelingen",
            "de tweede generatie nakomelingen",
            "de gameten van de ouders",
        ],
        antwoord=0,
        uitleg="P staat voor de parentale generatie, de ouders. Hun kinderen zijn de F1, "
        "hun kleinkinderen de F2.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hybride is homozygoot voor het kenmerk dat je volgt.",
        antwoord=False,
        uitleg="Een hybride is juist heterozygoot: ze komt van twee verschillende "
        "raszuivere lijnen. De F1 van twee raszuivere ouders bestaat volledig uit "
        "hybriden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikte Mendel grote aantallen planten? Kruis alles aan wat juist is.",
        opties=[
            "een verhouding klopt alleen bij veel nakomelingen",
            "het toeval van één kruising zegt te weinig",
            "zo kreeg hij meer dominante allelen",
            "zo verdween de invloed van de recessieve allelen",
        ],
        antwoord=[0, 1],
        uitleg="Bij vier nakomelingen krijg je zelden exact 3 op 1. Pas bij honderden "
        "planten komt de verwachte verhouding er duidelijk uit.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat zie je bij een intermediair kenmerk in de F1?",
        opties=[
            "iets tussen de twee ouderkenmerken",
            "alleen het kenmerk van de moeder",
            "alleen het dominante kenmerk",
            "de twee kenmerken naast elkaar",
        ],
        antwoord=0,
        uitleg="Bij een rode en een witte ouder geeft dat roze nakomelingen. Geen van de "
        "twee allelen is er volledig dominant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verhouding van fenotypes verwacht je in de F2 bij een intermediair kenmerk?",
        opties=[
            "1 op 2 op 1",
            "3 op 1",
            "9 op 3 op 3 op 1",
            "1 op 1",
        ],
        antwoord=0,
        uitleg="Omdat elk genotype zijn eigen uitzicht geeft, volgt het fenotype hier de "
        "genotypes: één rode, twee roze en één witte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt bij codominantie? Kruis alles aan wat juist is.",
        opties=[
            "je ziet de twee kenmerken naast elkaar",
            "geen van de twee allelen wordt verborgen",
            "er ontstaat één egale tussenkleur",
            "één van de twee allelen is volledig dominant",
        ],
        antwoord=[0, 1],
        uitleg="Codominant geeft bijvoorbeeld een rund met rode én witte haren door elkaar. "
        "Een egale tussenkleur zou juist op een intermediair kenmerk wijzen.",
    ),
    dict(
        type="invultekst",
        vraag="Welk bloedgroepsysteem bij de mens is een voorbeeld van multipele allelen?",
        antwoord=["ABO", "ABO-systeem", "het ABO-systeem"],
        uitleg="Voor dat ene gen bestaan er drie allelen: A, B en O. A en B zijn "
        "codominant tegenover elkaar en dominant over O.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee ouders hebben bloedgroep AB en O. Welke bloedgroepen kunnen hun kinderen hebben?",
        opties=[
            "alleen A of B",
            "alleen AB of O",
            "alleen O",
            "A, B, AB of O",
        ],
        antwoord=0,
        uitleg="De gameten zijn A of B tegenover O en O. Elk kind krijgt dus AO of BO, en "
        "dat geeft bloedgroep A of B.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom komt kleurenblindheid vaker voor bij mannen?",
        opties=[
            "het allel ligt op het X-chromosoom en zij hebben er één",
            "het allel ligt op het Y-chromosoom",
            "mannen hebben meer allelen voor dat gen",
            "bij vrouwen is het allel dominant",
        ],
        antwoord=0,
        uitleg="Een man met het recessieve allel op zijn enige X heeft geen tweede X om "
        "het te verbergen. Een vrouw moet het van beide ouders krijgen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een kenmerk waarvan het gen op een geslachtschromosoom ligt?",
        antwoord=[
            "geslachtsgebonden",
            "geslachtsgebonden kenmerk",
            "X-gebonden",
        ],
        uitleg="De meeste geslachtsgebonden kenmerken liggen op het X-chromosoom. Daardoor "
        "verschilt de kans tussen mannen en vrouwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vrouw is draagster van hemofilie en de vader is gezond. Wat geldt voor hun kinderen?",
        opties=[
            "de helft van de zonen heeft hemofilie",
            "alle zonen hebben hemofilie",
            "de helft van de dochters heeft hemofilie",
            "geen enkel kind kan drager zijn",
        ],
        antwoord=0,
        uitleg="Een zoon krijgt haar ene X, dus heeft hij vijftig procent kans. Een dochter "
        "krijgt ook de gezonde X van haar vader en wordt dus hoogstens draagster.",
    ),
    dict(
        type="waarofniet",
        vraag="Het is de eicel die bepaalt of een kind een jongen of een meisje wordt.",
        antwoord=False,
        uitleg="Een eicel draagt altijd een X. De zaadcel brengt een X of een Y mee, en "
        "daarmee ligt het geslacht vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn gekoppelde genen?",
        opties=[
            "genen die op hetzelfde chromosoom liggen",
            "genen die hetzelfde kenmerk bepalen",
            "genen met meer dan twee allelen",
            "genen die alleen bij mannen werken",
        ],
        antwoord=0,
        uitleg="Omdat ze samen in één chromosoom zitten, gaan ze meestal samen naar één "
        "gameet. Daardoor geldt de onafhankelijkheidswet niet voor hen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan gekoppelde genen toch van elkaar scheiden?",
        opties=[
            "een crossing-over tussen de twee loci",
            "een mitose in een lichaamscel",
            "de bevruchting van de eicel",
            "een fout bij de replicatie",
        ],
        antwoord=0,
        uitleg="Ligt er een chiasma tussen de twee genen, dan wisselen ze van chromosoom. "
        "Hoe verder de genen van elkaar liggen, hoe vaker dat gebeurt.",
    ),
    dict(
        type="waarofniet",
        vraag="Gekoppelde genen die ver van elkaar liggen, worden vaker door crossing-over gescheiden.",
        antwoord=True,
        uitleg="Tussen twee verafgelegen loci is er meer plaats voor een chiasma. Daarmee "
        "wordt de afstand tussen genen zelfs gemeten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt voor een letaal allel? Kruis alles aan wat juist is.",
        opties=[
            "homozygoot is het dodelijk",
            "je vindt het nooit homozygoot bij een levend dier",
            "het komt nooit tot expressie",
            "het ligt altijd op het X-chromosoom",
        ],
        antwoord=[0, 1],
        uitleg="Omdat de homozygote nakomelingen niet geboren worden, zie je in de "
        "nakomelingschap een verhouding 2 op 1 in plaats van 3 op 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken zijn polygeen? Kruis alles aan wat juist is.",
        opties=[
            "de lichaamslengte",
            "de huidkleur",
            "de bloedgroep in het ABO-systeem",
            "kleurenblindheid",
        ],
        antwoord=[0, 1],
        uitleg="Bij polygenie werken verschillende genen samen aan één kenmerk. Daardoor "
        "krijg je een vloeiende reeks in plaats van enkele scherp onderscheiden groepen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het samenwerken van meerdere genen aan één kenmerk?",
        antwoord=["polygenie", "de polygenie", "polygene overerving"],
        uitleg="Lengte, huidkleur en gewicht zijn polygeen. Daarbij speelt ook de omgeving "
        "nog mee, zoals voeding bij de lengte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee gezonde ouders hebben een kind met een aandoening. Wat weet je dan?",
        opties=[
            "het allel is recessief en de ouders zijn drager",
            "het allel is dominant en kwam van één ouder",
            "het allel ligt zeker op het Y-chromosoom",
            "het kind heeft een nieuw chromosoom erbij",
        ],
        antwoord=0,
        uitleg="Een dominant allel zou je bij minstens één ouder zien. Twee gezonde ouders "
        "met een ziek kind wijzen dus op een recessief allel bij twee dragers.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan zie je in een stamboom dat een kenmerk X-gebonden recessief is? Kruis alles aan wat juist is.",
        opties=[
            "veel meer mannen dan vrouwen zijn aangetast",
            "een aangetaste man geeft het aan alle dochters als draagster",
            "elke generatie heeft minstens één aangetaste",
            "de aandoening gaat altijd van vader naar zoon",
        ],
        antwoord=[0, 1],
        uitleg="Een vader geeft zijn X aan al zijn dochters en zijn Y aan zijn zonen. "
        "Daardoor gaat een X-gebonden kenmerk juist nooit van vader naar zoon.",
    ),
    dict(
        type="waarofniet",
        vraag="In een stamboom wordt een vrouw met een vierkant aangeduid.",
        antwoord=False,
        uitleg="Een vierkant staat voor een man, een cirkel voor een vrouw. Een gevulde "
        "vorm betekent dat de persoon het kenmerk heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een aandoening komt in elke generatie voor en zowel bij mannen als bij vrouwen. Wat is het meest waarschijnlijk?",
        opties=[
            "een dominant allel op een lichaamschromosoom",
            "een recessief allel op een lichaamschromosoom",
            "een recessief allel op het X-chromosoom",
            "een allel op het Y-chromosoom",
        ],
        antwoord=0,
        uitleg="Een dominant allel hoeft maar van één ouder te komen en slaat dus geen "
        "generatie over. Een recessief kenmerk duikt juist op na een of meer generaties "
        "zonder.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kenmerk dat een generatie overslaat, wijst eerder op een recessief dan op een dominant allel.",
        antwoord=True,
        uitleg="Dragers hebben het allel zonder het te tonen en geven het toch door. "
        "Daardoor lijkt het kenmerk te verdwijnen en later weer op te duiken.",
    ),
]

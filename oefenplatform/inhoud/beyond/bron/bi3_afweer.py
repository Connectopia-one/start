# -*- coding: utf-8 -*-
"""Niet-specifieke en specifieke afweer — 🌍 Beyond, biologie.

Deel 1 gaat over waarom het immuunsysteem nodig is, over de organen van het
lymfatisch systeem en over de eerste twee lijnen: de fysische en chemische
barrières en de niet-specifieke afweer. Deel 2 gaat over de specifieke afweer,
met de celtypes en de moleculen die erbij horen, en over het verschil tussen de
primaire en de secundaire immuunrespons.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waartegen beschermt het immuunsysteem? Kruis alles aan wat juist is.",
        opties=[
            "bacteriën en virussen",
            "eigen cellen die ontspoord zijn",
            "een tekort aan vitaminen",
            "een breuk in een bot",
        ],
        antwoord=[0, 1],
        uitleg="Het immuunsysteem keert zich tegen ziekteverwekkers en ruimt ook eigen "
        "cellen op die beschadigd of kankerachtig zijn. Een vitaminetekort of een breuk "
        "valt daarbuiten.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een ziekteverwekker, met één woord?",
        antwoord=["pathogeen", "een pathogeen", "ziekteverwekker"],
        uitleg="Een pathogeen is een organisme of virus dat ziekte kan veroorzaken: een "
        "bacterie, een virus, een schimmel of een parasiet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een antigeen?",
        opties=[
            "een stof die het immuunsysteem als vreemd herkent",
            "een eiwit dat een ziekteverwekker onschadelijk maakt",
            "een witte bloedcel die vreemde cellen opeet",
            "een orgaan van het lymfatisch systeem",
        ],
        antwoord=0,
        uitleg="Een antigeen is meestal een eiwit of een suikerketen op het oppervlak van "
        "een indringer. Het antilichaam is wat ons lichaam ertegen maakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de incubatietijd van een infectieziekte?",
        opties=[
            "de tijd tussen de besmetting en de eerste klachten",
            "de tijd dat iemand besmettelijk blijft",
            "de tijd die een vaccin nodig heeft om te werken",
            "de tijd die een wonde nodig heeft om te sluiten",
        ],
        antwoord=0,
        uitleg="Tijdens de incubatietijd vermenigvuldigt de ziekteverwekker zich al, "
        "terwijl je nog niets voelt. Toch kan je dan al besmettelijk zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Een infectie en een infectieziekte zijn hetzelfde.",
        antwoord=False,
        uitleg="Een infectie is het binnendringen en vermenigvuldigen van een pathogeen. "
        "Pas als dat klachten geeft, spreek je van een infectieziekte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke barrière is een fysische barrière?",
        opties=[
            "de opperhuid",
            "het lysozym in tranen",
            "de zuurmantel van de huid",
            "het maagzuur",
        ],
        antwoord=0,
        uitleg="De opperhuid is een muur van dode, verhoornde cellen. Lysozym, zuurmantel "
        "en maagzuur werken met stoffen en zijn dus chemisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet lysozym in tranen en in speeksel?",
        opties=[
            "de celwand van bacteriën kapotmaken",
            "virussen uit de lucht filteren",
            "het oog vochtig houden",
            "antilichamen aanmaken",
        ],
        antwoord=0,
        uitleg="Lysozym is een enzym dat peptidoglycaan afbreekt. Zonder celwand barst de "
        "bacterie open.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het geheel van onschadelijke micro-organismen dat van nature op en in ons leeft?",
        antwoord=["microbioom", "het microbioom", "microbiota"],
        uitleg="Het microbioom neemt plaats en voedsel in, zodat pathogenen minder kans "
        "krijgen. Het hoort bij de niet-specifieke afweer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom beschermen slijmvliezen ons?",
        opties=[
            "ze vangen deeltjes op en voeren ze af",
            "ze maken antilichamen op maat",
            "ze doden alle bacteriën onmiddellijk",
            "ze vormen een harde laag dode cellen",
        ],
        antwoord=0,
        uitleg="Slijm plakt stof en bacteriën vast, en het trilhaarepitheel duwt dat naar "
        "de keel. Een harde laag dode cellen is de opperhuid.",
    ),
    dict(
        type="waarofniet",
        vraag="De niet-specifieke afweer werkt tegen elke indringer op dezelfde manier.",
        antwoord=True,
        uitleg="Ze maakt geen onderscheid tussen de ene en de andere bacterie, en ze "
        "staat meteen klaar. Daarom heet ze ook de aangeboren immuniteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor de specifieke afweer? Kruis alles aan wat juist is.",
        opties=[
            "ze is op één antigeen gericht",
            "ze bouwt een geheugen op",
            "ze komt meteen volledig op gang",
            "ze werkt zonder lymfocyten",
        ],
        antwoord=[0, 1],
        uitleg="De specifieke afweer heeft dagen nodig om op gang te komen, maar is "
        "precies gericht en onthoudt de indringer. Daarom heet ze verworven immuniteit.",
    ),
    dict(
        type="invultekst",
        vraag="In welk orgaan rijpen de T-lymfocyten?",
        antwoord=["thymus", "de thymus", "zwezerik"],
        uitleg="De T van T-lymfocyt komt van thymus. Dat orgaan achter het borstbeen is "
        "bij een kind groot en wordt bij een volwassene kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar worden alle bloedcellen, en dus ook de witte, aangemaakt?",
        opties=["in het beenmerg", "in de milt", "in de lever", "in de thymus"],
        antwoord=0,
        uitleg="Uit de stamcellen in het rode beenmerg komen alle bloedcellen. De B van "
        "B-lymfocyt verwijst naar bone marrow.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doen de lymfeknopen?",
        opties=[
            "lymfe filteren en afweercellen samenbrengen",
            "lymfe aanmaken uit het bloedplasma van de aders",
            "oude rode bloedcellen uit de bloedbaan halen",
            "hormonen vanuit de klieren in het bloed brengen",
        ],
        antwoord=0,
        uitleg="In een lymfeknoop ontmoeten antigenen en lymfocyten elkaar. Daarom zwellen "
        "de klieren in je hals op als je ziek bent.",
    ),
    dict(
        type="waarofniet",
        vraag="De milt hoort bij het lymfatisch systeem.",
        antwoord=True,
        uitleg="De milt filtert bloed in plaats van lymfe, breekt oude rode bloedcellen "
        "af en bevat veel lymfocyten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke verschijnselen horen bij een ontsteking? Kruis alles aan wat juist is.",
        opties=[
            "roodheid en warmte",
            "zwelling en pijn",
            "een lagere lichaamstemperatuur",
            "een trager hartritme",
        ],
        antwoord=[0, 1],
        uitleg="De bloedvaten ter plaatse worden wijder en doorlaatbaarder, dus komt er "
        "meer bloed en vocht bij. Dat geeft rood, warm, gezwollen en pijnlijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is koorts nuttig bij een infectie?",
        opties=[
            "de afweer werkt sneller en de indringer trager",
            "de indringer krijgt dan geen voedsel meer",
            "de huid wordt er dikker door",
            "er komen dan minder witte bloedcellen",
        ],
        antwoord=0,
        uitleg="Een hogere temperatuur versnelt de afweerreacties en remt de "
        "vermenigvuldiging van veel bacteriën en virussen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stof in het bloed stijgt sterk bij een ontsteking en wordt daarom gemeten?",
        antwoord=["CRP", "crp", "C-reactief proteïne"],
        uitleg="CRP of C-reactief proteïne wordt door de lever gemaakt bij een "
        "ontsteking. Een arts leest aan dat getal af hoe fel de reactie is.",
    ),
    dict(
        type="waarofniet",
        vraag="De drie lijnen van onze afweer zijn barrières, niet-specifieke afweer en specifieke afweer.",
        antwoord=True,
        uitleg="Eerst houden huid en slijmvliezen tegen, dan pakt de niet-specifieke "
        "afweer wat erdoor is, en pas daarna komt de specifieke afweer op gang.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie een infectie doormaakt, bouwt daar nooit bescherming tegen op.",
        antwoord=False,
        uitleg="De specifieke afweer laat geheugencellen achter. Een tweede ontmoeting "
        "met hetzelfde antigeen wordt daardoor veel sneller afgehandeld.",
    ),
]

DEEL2 = [
    dict(
        type="invultekst",
        vraag="Hoe noemt men alle witte bloedcellen samen, met één woord?",
        antwoord=["leukocyten", "leucocyten", "witte bloedcellen"],
        uitleg="Leukocyten is de verzamelnaam. Daaronder vallen de granulocyten, de "
        "monocyten en de lymfocyten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een macrofaag?",
        opties=[
            "indringers opeten en verwerken",
            "antilichamen uitscheiden",
            "histamine vrijzetten bij een allergie",
            "rode bloedcellen aanmaken",
        ],
        antwoord=0,
        uitleg="Een macrofaag is een grote fagocyt. Ze neemt de indringer op en breekt "
        "hem met haar lysosomen af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke cel is de eerste fagocyt die in grote aantallen naar een ontsteking trekt?",
        opties=[
            "de neutrofiel",
            "de plasmacel",
            "de B-geheugencel",
            "de rode bloedcel",
        ],
        antwoord=0,
        uitleg="Neutrofielen zijn de talrijkste granulocyten. Ze komen snel ter plaatse "
        "en vormen samen met dood weefsel de pus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een natural killer cel?",
        opties=[
            "besmette of ontspoorde eigen cellen doden",
            "stukjes antigeen aan de T-cellen voorstellen",
            "antilichamen tegen één antigeen aanmaken",
            "de lymfe door de lymfevaten pompen",
        ],
        antwoord=0,
        uitleg="Een natural killer cel hoort bij de niet-specifieke afweer. Ze doorboort "
        "het membraan van een verdachte cel, zodat die sterft.",
    ),
    dict(
        type="waarofniet",
        vraag="Een dendritische cel stelt een stuk van de indringer voor aan de lymfocyten.",
        antwoord=True,
        uitleg="Een dendritische cel eet de indringer op en zet een stukje antigeen op "
        "haar MHC-II-eiwitten. Zo brengt ze de specifieke afweer op gang.",
    ),
    dict(
        type="invultekst",
        vraag="Welke stof zetten mestcellen vrij bij een allergische reactie?",
        antwoord=["histamine"],
        uitleg="Histamine maakt de bloedvaten wijder en doorlaatbaarder. Dat geeft "
        "zwelling, jeuk en een loopneus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de taak van een T-helperlymfocyt?",
        opties=[
            "de andere afweercellen aanzetten met cytokines",
            "besmette lichaamscellen zelf doorboren en doden",
            "antilichamen in grote aantallen uitscheiden",
            "oude rode bloedcellen in de milt afbreken",
        ],
        antwoord=0,
        uitleg="De T-helpercel is de dirigent. Ze erkent het antigeen op een MHC-II-eiwit "
        "en stuurt met cytokines de B-cellen en de cytotoxische T-cellen aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een cytotoxische T-lymfocyt?",
        opties=[
            "een besmette eigen cel doden",
            "antilichamen in het bloed brengen",
            "het complementsysteem aanmaken",
            "antigenen voorstellen aan B-cellen",
        ],
        antwoord=0,
        uitleg="Ze herkent het antigeen op een MHC-I-eiwit van een besmette cel en brengt "
        "die cel tot celdood. Zo wordt de virusfabriek stilgelegd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een plasmacel?",
        opties=[
            "antilichamen aanmaken",
            "indringers opeten",
            "antigenen voorstellen",
            "bloedplasma aanmaken",
        ],
        antwoord=0,
        uitleg="Een plasmacel is een B-lymfocyt die zich helemaal op productie heeft "
        "gezet. Ze giet duizenden antilichamen per seconde in het bloed.",
    ),
    dict(
        type="waarofniet",
        vraag="Antilichamen worden aangemaakt door de macrofagen.",
        antwoord=False,
        uitleg="Antilichamen, ook immunoglobulines genoemd, komen van de B-lymfocyten en "
        "hun plasmacellen. Een macrofaag eet op, maar maakt geen antilichamen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een antilichaam met een antigeen? Kruis alles aan wat juist is.",
        opties=[
            "het klit eraan vast en maakt het onschadelijk",
            "het maakt de indringer herkenbaar voor fagocyten",
            "het breekt het antigeen af met zijn eigen enzymen",
            "het verandert het DNA van de indringer blijvend",
        ],
        antwoord=[0, 1],
        uitleg="Antilichamen neutraliseren en klonteren indringers samen. Afbreken doen "
        "de fagocyten en het complementsysteem.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het samenklonteren van antigenen door antilichamen?",
        antwoord=["agglutinatie", "agglutineren"],
        uitleg="Bij agglutinatie binden antilichamen meerdere deeltjes aan elkaar. Dat "
        "maakt ze onbeweeglijk en makkelijker op te ruimen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet het complementsysteem?",
        opties=[
            "het membraan van een bacterie doorboren",
            "antigenen voorstellen aan T-cellen",
            "antilichamen aanmaken",
            "koorts opwekken in de hersenen",
        ],
        antwoord=0,
        uitleg="Het complementsysteem is een reeks eiwitten in het bloedplasma. Ze vormen "
        "samen een porie in het membraan van de indringer, die daardoor barst.",
    ),
    dict(
        type="waarofniet",
        vraag="Interferonen worden vrijgezet door cellen die door een virus besmet zijn.",
        antwoord=True,
        uitleg="Een besmette cel waarschuwt met interferonen haar buren. Die maken zich "
        "dan klaar om een virus tegen te houden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarin verschillen MHC-I- en MHC-II-eiwitten?",
        opties=[
            "MHC-I staat op bijna elke cel, MHC-II enkel op afweercellen",
            "MHC-I staat enkel op de afweercellen, MHC-II op elke cel",
            "MHC-I zit in de kern van de cel, MHC-II in het cytoplasma",
            "MHC-I is een suikerketen en MHC-II een vetzuurstaart",
        ],
        antwoord=0,
        uitleg="Op MHC-I toont elke cel wat er binnen in haar gebeurt, voor de "
        "cytotoxische T-cellen. MHC-II zit op de antigeenpresenterende cellen, voor de "
        "T-helpercellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom duurt de primaire immuunrespons dagen?",
        opties=[
            "de juiste lymfocyt moet zich eerst vermenigvuldigen",
            "het antigeen moet eerst helemaal afgebroken worden",
            "de huid moet zich eerst volledig herstellen",
            "de koorts moet eerst helemaal gezakt zijn",
        ],
        antwoord=0,
        uitleg="Er is maar één lymfocyt op miljoenen die op dat antigeen past. Die moet "
        "zich eerst delen tot een hele groep, voor er genoeg antilichamen zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom verloopt de secundaire immuunrespons sneller en krachtiger? Kruis alles aan wat juist is.",
        opties=[
            "er zijn al geheugencellen aanwezig",
            "die geheugencellen reageren meteen",
            "het antigeen is dan onschadelijk geworden",
            "de huid laat het antigeen dan niet door",
        ],
        antwoord=[0, 1],
        uitleg="De B- en T-geheugencellen van de eerste keer staan klaar. Ze slaan toe "
        "voor je iets voelt, en daarom word je een tweede keer vaak niet ziek.",
    ),
    dict(
        type="waarofniet",
        vraag="Een B-geheugencel scheidt onafgebroken antilichamen af, jaren na de infectie.",
        antwoord=False,
        uitleg="Een geheugencel wacht af. Pas als het antigeen terugkomt, deelt ze zich "
        "snel tot plasmacellen die wel antilichamen maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de rol van cytokines?",
        opties=[
            "boodschappen doorgeven tussen afweercellen",
            "bacteriën met een porie rechtstreeks doden",
            "losse antigenen tot klompjes samenklitten",
            "extra zuurstof naar de wonde brengen",
        ],
        antwoord=0,
        uitleg="Cytokines zijn signaalstoffen. Ze lokken cellen naar de plaats van de "
        "infectie en zetten andere afweercellen aan tot delen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een arts vindt in het bloed van iemand antilichamen tegen een virus, maar geen virus. Wat besluit ze?",
        opties=[
            "die persoon heeft het virus gehad of is gevaccineerd",
            "die persoon is op dit moment zelf besmettelijk",
            "die persoon heeft een immuunsysteem dat niet werkt",
            "die persoon zal nooit meer een infectie oplopen",
        ],
        antwoord=0,
        uitleg="Antilichamen zonder virus wijzen op een eerdere ontmoeting, door ziekte "
        "of door een vaccin. Het virus zelf is dan opgeruimd.",
    ),
]

# -*- coding: utf-8 -*-
"""DNA-technologie en gentechnologie — 🌍 Beyond, biologie.

Deel 1 gaat over het genetisch materiaal van een bacterie, over de natuurlijke
genoverdracht (transformatie, conjugatie en transductie), over de
lambdabacteriofaag, en over het gereedschap van de gentechnologie:
restrictie-enzymen, ligase, vectoren en de manieren om DNA in een cel te
brengen. Deel 2 gaat over de technieken zelf (PCR, gelelektroforese,
fingerprint, sequencing en CRISPR-Cas), over de vormen van klonering, en over
de toepassingen.

Een bacterie kan haar plasmiden uitwisselen, en daar zit ook de verspreiding
van antibioticumresistentie in. Die lijn loopt door beide delen, omdat ze
tegelijk het principe van de natuurlijke genoverdracht uitlegt en laat zien
waarom het onderwerp buiten het labo telt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe ziet het chromosoom van een bacterie eruit?",
        opties=[
            "als een gesloten ring, vrij in het cytoplasma",
            "als een rechte draad in een celkern",
            "als een draad rond histonen gewonden",
            "als losse stukjes in de celwand",
        ],
        antwoord=0,
        uitleg="Een bacterie heeft één ringvormig chromosoom en geen kern. Daarnaast kan "
        "ze kleine losse ringetjes hebben: de plasmiden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het kleine losse ringetje DNA naast het chromosoom van een bacterie?",
        antwoord=["plasmide", "een plasmide", "plasmiden"],
        uitleg="Een plasmide draagt extra genen, bijvoorbeeld voor "
        "antibioticumresistentie. Ze wordt apart gekopieerd en kan doorgegeven worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt voor een plasmide? Kruis alles aan wat juist is.",
        opties=[
            "ze kan van de ene bacterie naar de andere",
            "ze kan een resistentiegen dragen",
            "ze bevat alle genen die de bacterie nodig heeft",
            "ze zit altijd in de kern van de bacterie",
        ],
        antwoord=[0, 1],
        uitleg="De levensnoodzakelijke genen zitten op het chromosoom. Een bacterie heeft "
        "geen kern, dus ligt alles vrij in het cytoplasma.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij transformatie?",
        opties=[
            "een bacterie neemt vrij DNA uit haar omgeving op",
            "een bacterie geeft DNA door via een pilus",
            "een virus brengt DNA in een bacterie",
            "een bacterie deelt zich in twee dochtercellen",
        ],
        antwoord=0,
        uitleg="Sterft er een bacterie, dan komt haar DNA vrij. Een andere bacterie kan dat "
        "opnemen en inbouwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij conjugatie?",
        opties=[
            "twee bacteriën wisselen DNA uit via een brug",
            "een bacterie neemt los DNA op uit het water",
            "een virus brengt bacterieel DNA over",
            "een bacterie kopieert haar eigen chromosoom",
        ],
        antwoord=0,
        uitleg="Via een pilus komt er een verbinding tussen twee cellen. Daarlangs gaat "
        "meestal een kopie van een plasmide.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de genoverdracht waarbij een virus bacterieel DNA meeneemt naar een andere bacterie?",
        antwoord=["transductie", "de transductie"],
        uitleg="Bij het verpakken van nieuwe fagen raakt er soms bacterieel DNA in. Die "
        "faag brengt dat dan in de volgende bacterie binnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een bacteriofaag?",
        opties=[
            "een virus dat bacteriën besmet",
            "een bacterie die virussen opeet",
            "een enzym dat bacterieel DNA knipt",
            "een plasmide met een resistentiegen",
        ],
        antwoord=0,
        uitleg="Een faag is een virus en dus een obligate parasiet: zonder gastheer kan hij "
        "zich niet vermenigvuldigen. De lambdafaag besmet E. coli.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de lytische cyclus van een faag?",
        opties=[
            "de cel maakt nieuwe fagen en barst open",
            "het faag-DNA wordt in het chromosoom ingebouwd",
            "de bacterie deelt zich mét het faag-DNA",
            "de faag verlaat de cel zonder schade",
        ],
        antwoord=0,
        uitleg="De faag kaapt de machinerie van de bacterie en laat kopieën van zichzelf "
        "maken. Daarna breekt de cel open en komen de nieuwe fagen vrij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de lysogene cyclus? Kruis alles aan wat juist is.",
        opties=[
            "het faag-DNA wordt in het bacteriële chromosoom ingebouwd",
            "het faag-DNA wordt bij elke deling mee gekopieerd",
            "de bacterie barst meteen open",
            "de faag verliest zijn erfelijk materiaal",
        ],
        antwoord=[0, 1],
        uitleg="In de lysogene cyclus blijft de faag verborgen meeliften. Pas later kan hij "
        "alsnog in de lytische cyclus overgaan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een virus kan zich alleen in een levende gastheercel vermenigvuldigen.",
        antwoord=True,
        uitleg="Een virus heeft geen eigen stofwisseling of ribosomen. Daarom is het een "
        "obligate parasiet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een enzym dat DNA op een vaste plaats in de sequentie doorknipt?",
        antwoord=["restrictie-enzym", "restrictie enzym", "restrictie-enzymen"],
        uitleg="Een restrictie-enzym zoals EcoRI herkent een korte sequentie en knipt daar. "
        "Bacteriën gebruiken die enzymen zelf tegen binnendringend faag-DNA.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn sticky ends handig bij gentechnologie?",
        opties=[
            "ze passen op elk stuk dat met hetzelfde enzym geknipt is",
            "ze plakken aan elk willekeurig stuk DNA vast",
            "ze beletten dat het DNA opnieuw sluit",
            "ze maken het DNA bestand tegen enzymen",
        ],
        antwoord=0,
        uitleg="Een schuine knip laat enkelstrengige uiteinden achter. Twee stukken die "
        "zo geknipt zijn, passen met hun complementaire uiteinden aan elkaar.",
    ),
    dict(
        type="invultekst",
        vraag="Welk enzym hecht twee geknipte stukken DNA definitief aan elkaar?",
        antwoord=["ligase", "het ligase", "DNA-ligase"],
        uitleg="Ligase sluit de suiker-fosfaatketen. Pas dan is het recombinant DNA één "
        "geheel.",
    ),
    dict(
        type="waarofniet",
        vraag="Recombinant DNA is DNA dat met een restrictie-enzym in gelijke stukken geknipt is.",
        antwoord=False,
        uitleg="Recombinant DNA is DNA waarin stukken van verschillende herkomst "
        "samengebracht zijn, zoals een plasmide met een menselijk gen erin. Dat is het "
        "uitgangspunt van de hele gentechnologie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een vector in de gentechnologie?",
        opties=[
            "een drager die DNA in een cel brengt",
            "een enzym dat het DNA doorknipt",
            "een cel die het nieuwe eiwit maakt",
            "een apparaat dat DNA uitleest",
        ],
        antwoord=0,
        uitleg="Een plasmide, een virus of een liposoom kan als vector dienen. Zonder "
        "drager raakt het DNA niet binnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke methoden brengen DNA rechtstreeks in een cel? Kruis alles aan wat juist is.",
        opties=[
            "micro-injectie met een fijne naald",
            "elektroporatie met een stroomstoot",
            "verhitten tot boven honderd graden",
            "centrifugeren van de cellen",
        ],
        antwoord=[0, 1],
        uitleg="Bij micro-injectie wordt het DNA ingespoten, bij elektroporatie gaan de "
        "poriën even open. Bij planten wordt ook een genenkanon gebruikt.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Ti-plasmide van een bodembacterie wordt gebruikt om planten te veranderen.",
        antwoord=True,
        uitleg="Die bacterie brengt van nature een stuk T-DNA in een plantencel. Door daar "
        "het gewenste gen in te zetten, wordt ze een vector.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een cisgeen en een transgeen organisme?",
        opties=[
            "bij cisgeen komt het gen van een verwante soort",
            "bij cisgeen komt het gen van een andere soort",
            "bij transgeen is er geen gen toegevoegd",
            "er is geen verschil tussen de twee",
        ],
        antwoord=0,
        uitleg="Cisgeen blijft binnen soorten die ook natuurlijk kunnen kruisen. Transgeen "
        "haalt een gen over die grens heen, bijvoorbeeld van een bacterie naar een plant.",
    ),
    dict(
        type="waarofniet",
        vraag="Een menselijk gen kan niet werken in een bacterie.",
        antwoord=False,
        uitleg="De genetische code is bijna universeel, dus leest een bacterie dat gen "
        "gewoon. Daarom kan menselijke insuline door bacteriën gemaakt worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe maakt men een bacterie die menselijke insuline produceert?",
        opties=[
            "het insulinegen wordt in een plasmide gezet en ingebracht",
            "de bacterie wordt met insuline gevoed tot ze het namaakt",
            "het insulinegen wordt in het faag-DNA verwijderd",
            "de bacterie wordt met een menselijke cel versmolten",
        ],
        antwoord=0,
        uitleg="Het gen wordt met een restrictie-enzym geknipt en met ligase in een "
        "plasmide gezet. De bacterie neemt dat plasmide op en maakt het eiwit.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een PCR?",
        opties=[
            "een stukje DNA miljoenen keren vermenigvuldigen",
            "de volledige volgorde van de basen uitlezen",
            "stukken DNA op grootte scheiden",
            "een gen uit een chromosoom knippen",
        ],
        antwoord=0,
        uitleg="Met een PCR maak je van een piepklein staal genoeg DNA om mee te werken. "
        "Pas daarna volgt het uitlezen of het scheiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen herhaalt een PCR telkens opnieuw? Kruis alles aan wat juist is.",
        opties=[
            "verhitten tot de strengen loskomen",
            "afkoelen zodat de primers kunnen binden",
            "het DNA met ligase aan elkaar hechten",
            "het DNA op een gel laten lopen",
        ],
        antwoord=[0, 1],
        uitleg="Elke cyclus bestaat uit opwarmen, afkoelen en verlengen. Na dertig cycli "
        "zijn er al meer dan een miljard kopieën.",
    ),
    dict(
        type="invultekst",
        vraag="Wat meet een kwantitatieve PCR, naast de aanwezigheid van het DNA?",
        antwoord=["de hoeveelheid", "hoeveelheid", "het aantal kopieën"],
        uitleg="Een qPCR volgt het signaal tijdens het vermenigvuldigen. Daardoor weet je "
        "ook hoeveel virus of bacterie er in het staal zat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe scheidt gelelektroforese stukken DNA?",
        opties=[
            "kleine stukken schuiven verder door de gel",
            "grote stukken schuiven verder door de gel",
            "de stukken worden op kleur gescheiden",
            "de stukken worden op temperatuur gescheiden",
        ],
        antwoord=0,
        uitleg="DNA is negatief geladen en wandelt naar de pluspool. Kleine stukken komen "
        "makkelijker door de gel en raken dus verder.",
    ),
    dict(
        type="waarofniet",
        vraag="DNA beweegt in een gel naar de minpool, want het is positief geladen.",
        antwoord=False,
        uitleg="De fosfaatgroepen maken het DNA juist negatief, dus wandelt het naar de "
        "pluspool. Elk fragment gaat dezelfde kant op, alleen niet even snel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een DNA-fingerprint van elke mens verschillend?",
        opties=[
            "iedereen heeft een eigen aantal herhalingen in zijn DNA",
            "iedereen heeft andere genen voor zijn eiwitten",
            "iedereen heeft een ander aantal chromosomen",
            "iedereen heeft een eigen aantal basen in zijn genoom",
        ],
        antwoord=0,
        uitleg="Op bepaalde plaatsen staan korte stukjes die een wisselend aantal keer "
        "herhaald worden. Dat patroon van bandjes is bij iedereen anders, behalve bij een "
        "eeneiige tweeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor wordt een DNA-fingerprint gebruikt? Kruis alles aan wat juist is.",
        opties=[
            "het vaststellen van wie de vader is",
            "het vergelijken van een spoor met een verdachte",
            "het uitlezen van de volledige basenvolgorde",
            "het vermenigvuldigen van een stukje DNA",
        ],
        antwoord=[0, 1],
        uitleg="Een fingerprint vergelijkt patronen van bandjes. Het uitlezen van de "
        "volgorde is sequencing, het vermenigvuldigen is PCR.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de techniek waarmee de volledige basenvolgorde van een stuk DNA uitgelezen wordt?",
        antwoord=["sequencing", "DNA-sequencing", "sequenering"],
        uitleg="Sequencing geeft de letters zelf, base per base. Daarmee worden genen "
        "opgespoord en worden virussen tot op de variant herkend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de CRISPR-Cas techniek?",
        opties=[
            "een gen op een gekozen plaats aanpassen",
            "een gen miljoenen keren kopiëren",
            "alle genen van een cel uitlezen",
            "een cel tot een volledig organisme laten groeien",
        ],
        antwoord=0,
        uitleg="Een stukje RNA wijst de plaats aan en het Cas-enzym knipt daar. De cel "
        "herstelt de knip, en daarbij wordt het gen gewijzigd.",
    ),
    dict(
        type="waarofniet",
        vraag="CRISPR-Cas komt oorspronkelijk uit het afweersysteem van bacteriën.",
        antwoord=True,
        uitleg="Bacteriën bewaren stukjes faag-DNA en herkennen daarmee een volgende "
        "aanval. Dat systeem is tot een gereedschap omgebouwd.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men, met de Engelse term, het gericht wijzigen van een bestaand gen op zijn eigen plaats in het DNA?",
        antwoord=["gene editing", "gene-editing", "genoomeditie"],
        uitleg="Bij gene editing wordt er niets vreemds ingebracht, maar een letter ter "
        "plaatse veranderd. Dat is preciezer dan het inbouwen van een heel gen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe maakt men een gewas dat insecten weerstaat?",
        opties=[
            "er wordt een bacterieel gen voor een gifstof ingebouwd",
            "de plant wordt met insecticiden besproeid en bewaard",
            "de insecten worden genetisch gewijzigd",
            "de plant wordt tegen de insecten ingeënt",
        ],
        antwoord=0,
        uitleg="Een gen uit een bodembacterie laat de plant zelf een stof maken die "
        "rupsen doodt. Zo is er minder bespuiting nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is reproductief klonen?",
        opties=[
            "een volledig nieuw individu maken dat genetisch gelijk is",
            "weefsel kweken om iemand mee te behandelen na een ziekte",
            "een stuk DNA in een bacterie vermenigvuldigen",
            "twee soorten met elkaar kruisen",
        ],
        antwoord=0,
        uitleg="De kern van een lichaamscel wordt in een ontkernde eicel gebracht. Zo werd "
        "het schaap Dolly gemaakt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het kweken van weefsel of cellen om een patiënt te behandelen?",
        antwoord=[
            "therapeutisch klonen",
            "therapeutisch kloneren",
            "therapeutische klonering",
        ],
        uitleg="Er wordt geen nieuw individu gemaakt, enkel weefsel met hetzelfde DNA als "
        "de patiënt. Daardoor stoot het lichaam het niet af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een voorbeeld van natuurlijk klonen?",
        opties=[
            "een eeneiige tweeling",
            "een twee-eiige tweeling",
            "een kind met een donoreicel",
            "een kruising tussen twee rassen",
        ],
        antwoord=0,
        uitleg="Bij een eeneiige tweeling splitst één bevruchte eicel in twee. De twee "
        "kinderen hebben daardoor precies hetzelfde DNA.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is moleculair klonen?",
        opties=[
            "een stuk DNA in een gastheercel vermenigvuldigen",
            "een volledig dier namaken uit één lichaamscel van een ander",
            "het DNA van twee soorten vergelijken",
            "een gen uit het genoom verwijderen",
        ],
        antwoord=0,
        uitleg="Het gen wordt in een plasmide gezet en de bacterie doet de rest. Elke "
        "deling levert meer kopieën van dat ene stuk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kloon van een dier is ook in zijn gedrag precies hetzelfde dier.",
        antwoord=False,
        uitleg="Het DNA is gelijk, maar de omgeving niet. Een kloon is als een eeneiige "
        "tweeling die veel later geboren wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor wordt DNA-technologie in de geneeskunde gebruikt? Kruis alles aan wat juist is.",
        opties=[
            "het opsporen van afwijkingen voor de geboorte",
            "het herkennen van een micro-organisme in een staal",
            "het bepalen van iemands bloeddruk",
            "het meten van de lichaamstemperatuur",
        ],
        antwoord=[0, 1],
        uitleg="Prenataal onderzoek, infectiediagnostiek en kankeronderzoek leunen zwaar "
        "op PCR en sequencing. Bloeddruk en temperatuur worden gewoon gemeten.",
    ),
    dict(
        type="waarofniet",
        vraag="Het overdragen van plasmiden tussen bacteriën helpt antibioticumresistentie verspreiden.",
        antwoord=True,
        uitleg="Zit het resistentiegen op een plasmide, dan kan het via conjugatie naar een "
        "andere soort. Daardoor gaat resistentie veel sneller rond dan via mutatie alleen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom worden ggo's maatschappelijk besproken?",
        opties=[
            "de gevolgen op lange termijn zijn niet voor iedereen even duidelijk",
            "de techniek werkt in het labo niet betrouwbaar",
            "de genetische code verschilt te veel per soort",
            "er bestaat geen wetgeving voor",
        ],
        antwoord=0,
        uitleg="Het gaat om vragen over het milieu, de voedselvoorziening en wie de "
        "zaden bezit. De techniek zelf werkt, het debat gaat over het gebruik ervan.",
    ),
]

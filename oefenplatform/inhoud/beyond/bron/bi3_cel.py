# -*- coding: utf-8 -*-
"""De cel, de organellen en de biologische membranen — 🌍 Beyond, biologie.

Deel 1 gaat over de organisatieniveaus, het verschil tussen een prokaryote en
een eukaryote cel, en de organellen met hun functie. Deel 2 gaat over de
plastiden, het cytoskelet, het verschil tussen een plantaardige en een
dierlijke cel, de endosymbiosetheorie, de bouw en de functie van een
biologische membraan, en de celwand.

De fiche vraagt de organellen één per één te kunnen situeren en hun structuur
aan hun functie te kunnen koppelen, dus gaan de vragen verder dan het benoemen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke reeks zet de biologische organisatieniveaus van klein naar groot?",
        opties=[
            "atoom, molecule, organel, cel, weefsel, orgaan, organisme",
            "cel, atoom, molecule, organel, weefsel, orgaan, organisme",
            "molecule, atoom, cel, organel, orgaan, weefsel, organisme",
            "organel, atoom, molecule, cel, orgaan, weefsel, organisme",
        ],
        antwoord=0,
        uitleg="De reeks loopt van atoom tot biosfeer. Een atoom zit in een molecule, "
        "moleculen vormen een organel, organellen een cel, cellen een weefsel, "
        "weefsels een orgaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat heeft een prokaryote cel niet? Kruis alles aan wat juist is.",
        opties=[
            "een kern met een kernmembraan",
            "mitochondria",
            "ribosomen",
            "een celmembraan",
        ],
        antwoord=[0, 1],
        uitleg="Een prokaryote cel heeft geen kernmembraan en geen membraanorganellen, "
        "dus ook geen mitochondria. Ribosomen en een celmembraan heeft ze wel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het organel waarin de ribosomen gemaakt worden? Het ligt in de kern.",
        antwoord=["nucleolus", "kernlichaampje"],
        uitleg="De nucleolus of het kernlichaampje is de plaats in de kern waar het "
        "ribosomaal RNA gemaakt wordt en waar de ribosomen in elkaar gezet worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk organel breekt versleten celonderdelen af met behulp van enzymen?",
        opties=[
            "het lysosoom",
            "het ribosoom",
            "het centrosoom",
            "het transportblaasje",
        ],
        antwoord=0,
        uitleg="Een lysosoom is een blaasje vol afbrekende enzymen. Het ruimt versleten "
        "organellen en opgenomen deeltjes op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ribosoom is een organel zonder membraan.",
        antwoord=True,
        uitleg="Een ribosoom bestaat uit rRNA en eiwitten, zonder membraan erom. Daarom "
        "hebben ook prokaryote cellen ribosomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarin verschilt het ruw endoplasmatisch reticulum van het gladde?",
        opties=[
            "er zitten ribosomen op het ruwe",
            "het ruwe ligt altijd buiten de cel",
            "het ruwe heeft geen membraan",
            "het ruwe bevat het DNA van de cel",
        ],
        antwoord=0,
        uitleg="De ribosomen op het ruw ER maken het korrelig onder de microscoop. Daar "
        "worden eiwitten gemaakt; het glad ER maakt vooral lipiden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet het Golgi-apparaat?",
        opties=[
            "het werkt eiwitten af en verpakt ze in blaasjes",
            "het maakt het DNA van de cel na",
            "het breekt glucose af tot pyruvaat",
            "het vangt zonlicht op voor de fotosynthese",
        ],
        antwoord=0,
        uitleg="Het Golgi-apparaat werkt eiwitten uit het ER verder af, sorteert ze en "
        "stuurt ze in transportblaasjes naar hun bestemming.",
    ),
    dict(
        type="invultekst",
        vraag="In welk organel gebeuren de Krebscyclus en de eindoxidaties?",
        antwoord=["mitochondrion", "mitochondrie", "mitochondriën"],
        uitleg="Het mitochondrion is de plaats van de aerobe celademhaling. De "
        "Krebscyclus speelt in de matrix, de eindoxidaties op de cristae.",
    ),
    dict(
        type="waarofniet",
        vraag="De vacuole van een plantencel houdt mee de stevigheid van de cel in stand.",
        antwoord=True,
        uitleg="Een volle vacuole duwt met haar waterdruk tegen de celwand. Die turgor "
        "houdt het blad stevig; valt ze weg, dan verslapt de plant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een cel maakt heel veel eiwitten om uit te scheiden. Welke organellen zijn dan rijk aanwezig? Kruis alles aan wat juist is.",
        opties=[
            "het ruw endoplasmatisch reticulum",
            "het Golgi-apparaat",
            "de chloroplasten",
            "de celwand",
        ],
        antwoord=[0, 1],
        uitleg="Het ruw ER maakt de eiwitten en het Golgi-apparaat werkt ze af en "
        "verpakt ze. Een kliercel heeft daar veel van. Chloroplasten en een celwand "
        "horen bij een plantencel, niet bij uitscheiding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de functie van een centriool?",
        opties=[
            "de spoeldraden vastmaken bij een celdeling",
            "de cel van energie voorzien",
            "het afval van de cel afbreken",
            "de eiwitten van de cel sorteren",
        ],
        antwoord=0,
        uitleg="De twee centriolen van het centrosoom vormen het aangrijpingspunt van de "
        "microtubuli die de chromosomen uit elkaar trekken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een transportblaasje of vesikel verplaatst stoffen binnen de cel.",
        antwoord=True,
        uitleg="Een vesikel is een membraanblaasje. Het brengt stoffen van het ER naar "
        "het Golgi-apparaat, en van daar naar het celmembraan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft een cel een kernmembraan?",
        opties=[
            "om het DNA van het cytoplasma te scheiden",
            "om de cel haar stevigheid te geven",
            "om zonlicht op te vangen",
            "om de cel te laten bewegen",
        ],
        antwoord=0,
        uitleg="Het kernmembraan houdt het DNA apart, zodat de transcriptie in de kern "
        "gebeurt en de translatie pas erbuiten. Zo kan de cel de twee stappen apart "
        "regelen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de openingen in het kernmembraan waarlangs het mRNA de kern verlaat?",
        antwoord=["kernporiën", "kernporen", "kernporie"],
        uitleg="Door de kernporiën gaan mRNA en ribosomale onderdelen naar buiten en "
        "enzymen naar binnen. Het membraan is daardoor niet dicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een cel is bijzonder rijk aan mitochondria. Wat zegt dat over die cel?",
        opties=[
            "ze verbruikt veel energie",
            "ze maakt veel suiker aan",
            "ze deelt zich bijna nooit",
            "ze heeft geen kern",
        ],
        antwoord=0,
        uitleg="Mitochondria leveren ATP. Een spiercel of een zenuwcel heeft er veel, "
        "want die verbruiken onafgebroken energie.",
    ),
    dict(
        type="waarofniet",
        vraag="Het cytoplasma is alles binnen het celmembraan, de kern inbegrepen.",
        antwoord=False,
        uitleg="Het cytoplasma is alles binnen het celmembraan buiten de kern. De kern "
        "wordt er dus niet bij gerekend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband tussen structuur en functie klopt?",
        opties=[
            "de cristae van een mitochondrion vergroten het oppervlak voor de eindoxidaties",
            "de cristae van een mitochondrion houden het DNA van de cel bij elkaar",
            "de cristae van een mitochondrion maken de cel stevig",
            "de cristae van een mitochondrion vangen het licht op",
        ],
        antwoord=0,
        uitleg="De cristae zijn de inplooiingen van het binnenmembraan. Meer oppervlak "
        "betekent plaats voor meer elektronentransportketens en ATP-synthase.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lysosoom en een vacuole doen in een cel precies hetzelfde.",
        antwoord=False,
        uitleg="Een lysosoom breekt af met enzymen. Een vacuole slaat vooral water en "
        "stoffen op en zorgt bij een plant voor de turgor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraak over het celmembraan is juist?",
        opties=[
            "het laat sommige stoffen door en andere niet",
            "het laat alle stoffen even goed door",
            "het laat helemaal niets door",
            "het bestaat uit cellulose",
        ],
        antwoord=0,
        uitleg="Het celmembraan is semi-permeabel of halfdoorlaatbaar. Water en kleine "
        "apolaire moleculen gaan er zelf door, ionen en grote moleculen niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het geheel van vezels dat de cel haar vorm geeft en haar organellen op hun plaats houdt?",
        antwoord=["cytoskelet"],
        uitleg="Het cytoskelet bestaat uit microtubuli, microfilamenten en intermediaire "
        "filamenten. Het geeft vorm, houdt organellen vast en laat beweging toe.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke plastide slaat zetmeel op?",
        opties=[
            "de amyloplast",
            "de chloroplast",
            "de chromoplast",
            "het lysosoom",
        ],
        antwoord=0,
        uitleg="Amylum is het Latijnse woord voor zetmeel. In een aardappelknol zitten "
        "de amyloplasten vol zetmeelkorrels.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke plastiden geven een vrucht of een bloem haar kleur?",
        opties=[
            "de chromoplasten",
            "de leukoplasten",
            "de amyloplasten",
            "de lysosomen",
        ],
        antwoord=0,
        uitleg="Chromoplasten bevatten gele, oranje en rode pigmenten. Een rijpe tomaat "
        "krijgt haar kleur doordat chloroplasten tot chromoplasten omgevormd worden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een leukoplast is een kleurloze plastide.",
        antwoord=True,
        uitleg="Leukos betekent wit. Een leukoplast heeft geen pigment en dient vooral "
        "om voorraad op te slaan; een amyloplast is er een soort van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderdelen van het cytoskelet zijn de dikste en dienen als spoeldraad bij een celdeling?",
        opties=[
            "de microtubuli",
            "de microfilamenten",
            "de intermediaire filamenten",
            "de plasmodesmata",
        ],
        antwoord=0,
        uitleg="Microtubuli zijn holle buisjes van tubuline. Ze vormen de spoelfiguur en "
        "liggen ook in trilharen en in de staart van een zaadcel.",
    ),
    dict(
        type="invultekst",
        vraag="Welk eiwit vormt de microfilamenten van het cytoskelet?",
        antwoord=["actine"],
        uitleg="Microfilamenten bestaan uit actine. Ze liggen vooral net onder het "
        "celmembraan en zorgen voor vormverandering en beweging van de cel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat heeft een plantencel wel en een dierlijke cel niet? Kruis alles aan wat juist is.",
        opties=[
            "een celwand",
            "chloroplasten",
            "mitochondria",
            "een celmembraan",
        ],
        antwoord=[0, 1],
        uitleg="Een celwand en chloroplasten horen bij een plantencel. Mitochondria en "
        "een celmembraan heeft een dierlijke cel evengoed.",
    ),
    dict(
        type="waarofniet",
        vraag="Een dierlijke cel heeft nooit een vacuole.",
        antwoord=False,
        uitleg="Een dierlijke cel heeft wel kleine blaasjes die als vacuole werken. Wat "
        "ze mist, is de ene grote centrale vacuole van een plantencel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarop steunt de endosymbiosetheorie? Kruis alles aan wat juist is.",
        opties=[
            "een mitochondrion heeft zijn eigen DNA",
            "een mitochondrion heeft een dubbel membraan",
            "een mitochondrion wordt door het Golgi-apparaat gemaakt",
            "een mitochondrion ontstaat uit het kernmembraan",
        ],
        antwoord=[0, 1],
        uitleg="Eigen DNA, eigen ribosomen, een dubbel membraan en deling door "
        "tweedeling wijzen erop dat mitochondria en chloroplasten ooit vrij levende "
        "bacteriën waren die door een grotere cel opgenomen werden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het model dat de bouw van een biologische membraan beschrijft?",
        antwoord=["vloeibaar mozaïekmodel", "mozaïekmodel", "vloeibaar mozaiekmodel"],
        uitleg="Het vloeibaar mozaïekmodel ziet het membraan als een dubbellaag "
        "fosfolipiden waarin eiwitten als stukjes van een mozaïek liggen en kunnen "
        "bewegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vormen fosfolipiden in water van zichzelf een dubbellaag?",
        opties=[
            "hun kop is hydrofiel en hun staarten zijn hydrofoob",
            "ze zijn allemaal volledig hydrofiel",
            "ze zijn allemaal volledig hydrofoob",
            "ze hebben een positieve lading over hun hele lengte",
        ],
        antwoord=0,
        uitleg="De fosfaatkoppen gaan naar het water, de vetzuurstaarten keren zich van "
        "het water af. Twee lagen met de staarten naar elkaar is dan de stabielste vorm.",
    ),
    dict(
        type="waarofniet",
        vraag="Cholesterol in een dierlijk membraan regelt mee hoe vloeibaar dat membraan is.",
        antwoord=True,
        uitleg="Cholesterol schuift tussen de vetzuurstaarten. Het houdt het membraan "
        "soepel bij lage temperatuur en stijver bij hoge.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk eiwit van het membraan steekt helemaal door de dubbellaag?",
        opties=[
            "het transmembraaneiwit",
            "het perifere eiwit",
            "het ribosomale eiwit",
            "het histon",
        ],
        antwoord=0,
        uitleg="Een transmembraaneiwit loopt van de ene kant naar de andere en kan zo "
        "een kanaal of een pomp vormen. Een perifeer eiwit ligt alleen tegen één kant aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de functie van de glycocalyx aan de buitenkant van een cel?",
        opties=[
            "cellen laten herkennen door andere cellen",
            "ATP aanmaken voor de cel",
            "het DNA van de cel verdubbelen",
            "water uit de cel pompen",
        ],
        antwoord=0,
        uitleg="De glycocalyx is de laag suikerketens op de membraaneiwitten en "
        "-lipiden. Daar steunt onder meer de herkenning van bloedgroepen op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een receptoreiwit in het membraan vangt een signaalstof op.",
        antwoord=True,
        uitleg="Een receptoreiwit past op één signaalstof, bijvoorbeeld een hormoon. "
        "Past die erin, dan geeft het eiwit het signaal door naar binnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaruit bestaat de celwand van een plant?",
        opties=["cellulose", "peptidoglycaan", "chitine", "cholesterol"],
        antwoord=0,
        uitleg="Een plantencelwand bestaat vooral uit cellulose. Een bacterie gebruikt "
        "peptidoglycaan en een schimmel chitine.",
    ),
    dict(
        type="invultekst",
        vraag="Waaruit bestaat de celwand van een schimmel?",
        antwoord=["chitine"],
        uitleg="Chitine is dezelfde stof als in het uitwendig skelet van een insect. "
        "Een plant gebruikt cellulose en een bacterie peptidoglycaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn plasmodesmata?",
        opties=[
            "openingen tussen twee plantencellen",
            "de pigmenten van een chloroplast",
            "de enzymen van een lysosoom",
            "de staartjes van een zaadcel",
        ],
        antwoord=0,
        uitleg="Plasmodesmata zijn kanaaltjes door de celwand heen. Daardoor staat het "
        "cytoplasma van naburige plantencellen met elkaar in verbinding.",
    ),
    dict(
        type="waarofniet",
        vraag="De celwand van een plant is halfdoorlaatbaar en bepaalt welke stoffen de cel in mogen.",
        antwoord=False,
        uitleg="De celwand is vooral stevig en laat water en opgeloste stoffen gewoon "
        "door. Het celmembraan eronder beslist wat er binnen mag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een membraan dat vloeibaar is nuttig voor de cel?",
        opties=[
            "de eiwitten erin kunnen zich verplaatsen",
            "het membraan kan dan geen stoffen tegenhouden",
            "de cel heeft dan geen cytoskelet meer nodig",
            "het membraan hoeft dan geen lipiden te bevatten",
        ],
        antwoord=0,
        uitleg="Omdat de lipiden langs elkaar schuiven, kunnen de eiwitten bewegen, kan "
        "het membraan zich herstellen en kan het blaasjes afsnijden of opnemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een biologische membraan zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het omgeeft ook organellen binnen de cel",
            "het is opgebouwd uit twee lagen lipiden",
            "het bestaat uit één laag eiwitten",
            "het komt enkel bij plantencellen voor",
        ],
        antwoord=[0, 1],
        uitleg="Niet alleen het celmembraan maar ook het kernmembraan en de membranen "
        "van de organellen zijn zulke dubbellagen. Ze komen bij elke cel voor.",
    ),
]

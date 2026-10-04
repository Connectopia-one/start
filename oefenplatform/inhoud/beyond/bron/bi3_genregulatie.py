# -*- coding: utf-8 -*-
"""Genregulatie, epigenetica en nature of nurture — 🌍 Beyond, biologie.

Deel 1 gaat over het aan- en uitzetten van genen: het lac-operon bij E. coli
als voorbeeld bij een prokaryoot, de niveaus waarop een eukaryote cel haar
genen regelt, en RNA-interferentie met micro-RNA. Deel 2 gaat over epigenetica
(DNA-methylering, histonacetylering en chromatine remodeling) en over de vraag
wat aanleg en wat omgeving is.

De fiche vraagt dat de leerling bij een gegeven voorbeeld uitlegt welke factor
voor het fenotype verantwoordelijk kan zijn. Daarom zijn de vragen over nature
en nurture in deel 2 telkens aan een concreet geval opgehangen, en niet aan de
definitie alleen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarom zet een cel niet al haar genen tegelijk aan?",
        opties=[
            "ze heeft maar een deel van die eiwitten nodig",
            "ze heeft maar een deel van haar DNA gekregen",
            "haar ribosomen kunnen maar één eiwit maken",
            "haar kernporiën gaan maar één keer open",
        ],
        antwoord=0,
        uitleg="Eiwitten maken kost energie en grondstoffen. Een cel leest dus alleen de "
        "genen die ze op dat moment nodig heeft.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een groep genen bij een bacterie die samen aan- of uitgezet worden?",
        antwoord=["operon", "een operon", "het operon"],
        uitleg="In een operon liggen de genen voor één taak naast elkaar, achter dezelfde "
        "promotor en operator. Het lac-operon is daarvan het bekendste voorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor codeert het lac-operon van E. coli?",
        opties=[
            "voor de eiwitten die lactose afbreken",
            "voor de eiwitten die glucose maken",
            "voor de repressor zelf",
            "voor het DNA-polymerase",
        ],
        antwoord=0,
        uitleg="Het operon draagt de genen voor het opnemen en splitsen van lactose. Die "
        "eiwitten zijn alleen nuttig als er lactose is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de repressor als er geen lactose aanwezig is?",
        opties=[
            "hij bindt op de operator en blokkeert de transcriptie",
            "hij bindt op de promotor en start de transcriptie",
            "hij breekt het mRNA van het operon af",
            "hij knipt het operon uit het chromosoom",
        ],
        antwoord=0,
        uitleg="Zolang de repressor op de operator zit, kan RNA-polymerase niet voorbij. De "
        "genen blijven dan uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er als er lactose in het milieu komt?",
        opties=[
            "lactose bindt op de repressor, die loslaat",
            "lactose bindt op de operator, die opengaat",
            "lactose breekt de repressor af",
            "lactose vervangt de promotor",
        ],
        antwoord=0,
        uitleg="Lactose werkt als inductor: ze verandert de vorm van de repressor. Die past "
        "dan niet meer op de operator, en het operon gaat aan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een stof die een operon aanzet, zoals lactose bij het lac-operon?",
        antwoord=["inductor", "een inductor", "de inductor"],
        uitleg="Een inductor haalt de repressor van de operator. Daardoor maakt de bacterie "
        "de afbrekende enzymen pas als er iets af te breken valt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarop codeert het regulatorgen?",
        opties=[
            "op de repressor",
            "op de operator",
            "op de promotor",
            "op het lactose zelf",
        ],
        antwoord=0,
        uitleg="Het regulatorgen ligt buiten het operon en wordt doorlopend afgelezen. "
        "Daardoor is er altijd repressor aanwezig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt E. coli liever glucose dan lactose?",
        opties=[
            "glucose is zonder extra enzymen bruikbaar",
            "glucose levert meer ATP dan lactose",
            "lactose beschadigt de celwand",
            "lactose kan niet door het membraan",
        ],
        antwoord=0,
        uitleg="Glucose gaat meteen de glycolyse in. Zolang er glucose is, blijft het "
        "lac-operon daarom grotendeels uit, ook al is er lactose.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bacterie maakt de enzymen voor lactose altijd, of er nu lactose is of niet.",
        antwoord=False,
        uitleg="Dat zou grondstoffen verspillen. Ze maakt die enzymen pas als lactose de "
        "repressor losmaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welke niveaus kan een eukaryote cel haar genexpressie regelen? Kruis alles aan wat juist is.",
        opties=[
            "bij de transcriptie van het gen",
            "bij de afbraak van het mRNA",
            "bij de replicatie van het chromosoom",
            "bij de deling van de kern",
        ],
        antwoord=[0, 1],
        uitleg="Regulatie kan aangrijpen op het chromatine, de transcriptie, de splicing, "
        "de levensduur van het mRNA, de translatie en het afwerken van het eiwit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is celspecifieke genexpressie?",
        opties=[
            "elk celtype gebruikt zijn eigen deel van het genoom",
            "elk celtype heeft zijn eigen chromosomen",
            "elke cel maakt alle eiwitten van het lichaam",
            "elke cel kopieert haar DNA op haar eigen manier",
        ],
        antwoord=0,
        uitleg="Een spiercel en een levercel hebben hetzelfde DNA. Dat ze anders werken, "
        "komt doordat ze andere genen aanzetten.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het afremmen van een gen door kleine stukjes RNA?",
        antwoord=["RNA-interferentie", "RNA interferentie", "rna-interferentie"],
        uitleg="Bij RNA-interferentie bindt een klein RNA op het mRNA. Dat mRNA wordt dan "
        "niet vertaald of meteen afgebroken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een micro-RNA?",
        opties=[
            "het bindt op een mRNA en legt de translatie stil",
            "het bindt op het DNA en start de transcriptie",
            "het brengt aminozuren naar het ribosoom",
            "het knipt introns uit het pre-mRNA",
        ],
        antwoord=0,
        uitleg="Een micro-RNA is maar een twintigtal nucleotiden lang. Het past op een "
        "stukje van het mRNA en houdt dat mRNA tegen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij RNA-interferentie wordt het gen zelf uit het DNA geknipt.",
        antwoord=False,
        uitleg="Het gen blijft gewoon staan en wordt nog getranscribeerd. Alleen het mRNA "
        "wordt tegengehouden, dus is het effect omkeerbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is regulatie op het niveau van het mRNA nuttig voor een cel?",
        opties=[
            "de cel kan snel stoppen met een eiwit te maken",
            "de cel hoeft haar DNA dan niet te kopiëren",
            "de cel krijgt er extra chromosomen bij",
            "de cel kan haar genen dan wissen",
        ],
        antwoord=0,
        uitleg="Een mRNA afbreken werkt sneller dan een gen uitzetten en wachten tot het "
        "oude mRNA op is. Zo stuurt een cel van minuut tot minuut bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Transcriptiefactoren kunnen een gen zowel aanzetten als tegenhouden.",
        antwoord=True,
        uitleg="Er zijn activerende en remmende transcriptiefactoren. Welke er op de "
        "promotor binden, beslist of polymerase aan de slag kan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leverkel moet plots veel van een ontgiftend enzym maken. Wat verandert er het eerst?",
        opties=[
            "het gen voor dat enzym wordt vaker afgelezen",
            "de cel krijgt een kopie van dat gen erbij",
            "het enzym verandert zelf van vorm",
            "de cel deelt zich om meer enzym te maken",
        ],
        antwoord=0,
        uitleg="Meer mRNA geeft meer eiwit. Daarom begint regulatie meestal bij de "
        "transcriptie.",
    ),
    dict(
        type="waarofniet",
        vraag="Ook bij een bacterie zijn er genen die doorlopend aanstaan.",
        antwoord=True,
        uitleg="Genen voor de ribosomen of voor de glycolyse zijn altijd nodig. Alleen de "
        "genen voor wisselende taken worden geregeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het voordeel van een operon voor een bacterie?",
        opties=[
            "alle genen van één taak gaan samen aan",
            "elk gen kan apart gelezen worden",
            "de genen hoeven niet gekopieerd te worden",
            "het DNA wordt er korter door",
        ],
        antwoord=0,
        uitleg="Eén signaal volstaat om de hele reeks enzymen te maken. Dat is sneller dan "
        "elk gen apart aansturen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat geldt voor de operator en de promotor? Kruis alles aan wat juist is.",
        opties=[
            "de promotor is de aanlegplaats van polymerase",
            "de operator is de plaats waar de repressor past",
            "beide coderen voor een eiwit",
            "beide liggen op het mRNA",
        ],
        antwoord=[0, 1],
        uitleg="Het zijn allebei stukjes DNA met een regelfunctie, geen genen. Ze worden "
        "dus niet in een eiwit vertaald.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat bestudeert de epigenetica?",
        opties=[
            "veranderingen in de genexpressie zonder verandering van het DNA",
            "veranderingen in de volgorde van de nucleotiden",
            "het aantal chromosomen in een cel",
            "de bouw van de ribosomen",
        ],
        antwoord=0,
        uitleg="De letters van het DNA blijven dezelfde; alleen de leesbaarheid verandert. "
        "Daarom spreekt men van boven op de genetica.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet DNA-methylering meestal met een gen?",
        opties=[
            "ze legt het gen stil",
            "ze zet het gen harder aan",
            "ze verandert de volgorde van de basen",
            "ze knipt het gen uit het chromosoom",
        ],
        antwoord=0,
        uitleg="Een methylgroep op het DNA houdt de transcriptiefactoren weg. Het gen "
        "blijft aanwezig, maar wordt niet meer gelezen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke kleine groep wordt bij methylering op het DNA gezet?",
        antwoord=["methylgroep", "een methylgroep", "CH3"],
        uitleg="De methylgroep komt vooral op cytosinen terecht. Dat patroon kan bij een "
        "celdeling meegegeven worden aan de dochtercellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet histonacetylering?",
        opties=[
            "ze maakt het chromatine losser, zodat genen leesbaar worden",
            "ze maakt het chromatine vaster, zodat genen stilvallen",
            "ze verwijdert de histonen uit de kern",
            "ze vervangt de histonen door methylgroepen",
        ],
        antwoord=0,
        uitleg="Een acetylgroep vermindert de aantrekking tussen histon en DNA. Het "
        "chromatine komt losser te liggen en de enzymen kunnen erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke veranderingen horen bij epigenetica? Kruis alles aan wat juist is.",
        opties=[
            "DNA-methylering",
            "histonacetylering",
            "een substitutie in een codon",
            "een extra chromosoom in de cel",
        ],
        antwoord=[0, 1],
        uitleg="Methylering en acetylering veranderen de verpakking, niet de letters. Een "
        "substitutie of een chromosoom te veel is een echte mutatie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het verschuiven en herschikken van de nucleosomen, waardoor genen beter of slechter leesbaar worden?",
        antwoord=[
            "chromatine remodeling",
            "chromatineremodeling",
            "remodeling",
        ],
        uitleg="Eiwitcomplexen schuiven de nucleosomen opzij of dichterbij. Zo beslist een "
        "cel welk stuk van haar DNA open ligt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een epigenetische verandering kan ongedaan gemaakt worden.",
        antwoord=True,
        uitleg="Methyl- en acetylgroepen kunnen er weer af. Daarom is epigenetica veel "
        "beweeglijker dan een mutatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hebben een spiercel en een zenuwcel van dezelfde mens een ander uitzicht?",
        opties=[
            "hun chromatine ligt anders open, dus andere genen staan aan",
            "ze hebben elk een ander stuk van het DNA gekregen",
            "ze hebben elk een ander aantal chromosomen",
            "hun DNA is tijdens de deling veranderd",
        ],
        antwoord=0,
        uitleg="Bij de celdifferentiatie wordt een deel van het genoom vastgezet en een "
        "ander deel opengelegd. Het DNA zelf blijft gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan een epigenetisch patroon beïnvloeden? Kruis alles aan wat juist is.",
        opties=[
            "voeding",
            "langdurige stress",
            "de bloedgroep",
            "het aantal chromosomen",
        ],
        antwoord=[0, 1],
        uitleg="Voeding, stress, roken en gifstoffen laten sporen na in het "
        "methyleringspatroon. De bloedgroep en het chromosomenaantal liggen in het DNA "
        "zelf vast.",
    ),
    dict(
        type="waarofniet",
        vraag="Epigenetische merktekens worden altijd aan de kinderen doorgegeven.",
        antwoord=False,
        uitleg="Bij het vormen van de gameten wordt het patroon grotendeels gewist. Een "
        "deel ervan lijkt toch door te gaan, maar dat is de uitzondering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met nature?",
        opties=[
            "de aanleg die in het DNA ligt",
            "de invloed van de omgeving",
            "de opvoeding thuis",
            "het toeval bij de bevruchting",
        ],
        antwoord=0,
        uitleg="Nature is wat je meekrijgt in je genen, nurture is alles wat de omgeving "
        "daarbij doet. In de praktijk werken ze samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee eeneiige tweelingen worden apart opgevoed en verschillen in lengte. Wat verklaart dat?",
        opties=[
            "de omgeving, want hun DNA is gelijk",
            "hun genen, want die verschillen licht",
            "hun chromosomenaantal",
            "hun bloedgroep",
        ],
        antwoord=0,
        uitleg="Eeneiige tweelingen hebben hetzelfde DNA. Elk verschil tussen hen moet dus "
        "van buitenaf komen, zoals voeding of ziekte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand erft de aanleg voor een hoge bloeddruk, maar krijgt ze pas na jaren ongezond eten. Wat zie je hier?",
        opties=[
            "aanleg en omgeving werken samen",
            "alleen de aanleg telt",
            "alleen de omgeving telt",
            "geen van beide speelt een rol",
        ],
        antwoord=0,
        uitleg="De genen bepalen de gevoeligheid, de levensstijl bepaalt of het zover komt. "
        "De meeste kenmerken werken zo.",
    ),
    dict(
        type="waarofniet",
        vraag="De bloedgroep van een mens hangt mee van zijn voeding af.",
        antwoord=False,
        uitleg="De bloedgroep ligt volledig in het DNA vast. Dat is een van de weinige "
        "kenmerken waar de omgeving niets aan verandert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken hangen sterk van de omgeving af? Kruis alles aan wat juist is.",
        opties=[
            "de taal die iemand spreekt",
            "het lichaamsgewicht",
            "de oogkleur",
            "het geslacht",
        ],
        antwoord=[0, 1],
        uitleg="Taal is helemaal aangeleerd en gewicht hangt van voeding en beweging af. "
        "Oogkleur en geslacht liggen in de genen vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een plant uit hetzelfde zaad groeit in de schaduw veel kleiner. Hoe noem je dat?",
        opties=[
            "een invloed van de omgeving op het fenotype",
            "een mutatie in het genotype",
            "een epigenetische mutatie van het zaad",
            "een verandering van de genetische code",
        ],
        antwoord=0,
        uitleg="Het genotype is gelijk gebleven; alleen het fenotype verschilt. Licht, "
        "water en grond sturen mee hoe een plant uitgroeit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men alles wat je aan een organisme kunt waarnemen, in tegenstelling tot zijn genotype?",
        antwoord=["fenotype", "het fenotype"],
        uitleg="Het fenotype is het resultaat van het genotype én de omgeving. Daarom "
        "kunnen twee planten met hetzelfde genotype er anders uitzien.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de meeste kenmerken valt niet te zeggen dat alleen de genen of alleen de omgeving tellen.",
        antwoord=True,
        uitleg="Lengte, gewicht, gezondheid en gedrag hangen van beide af. De vraag is "
        "meestal hoeveel elk van de twee bijdraagt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is epigenetica een brug tussen nature en nurture?",
        opties=[
            "de omgeving verandert mee welke genen gelezen worden",
            "de omgeving verandert de volgorde van de genen",
            "de genen bepalen welke omgeving je krijgt",
            "de genen verdwijnen door de omgeving",
        ],
        antwoord=0,
        uitleg="Voeding, stress en gifstoffen zetten merktekens op het DNA. Zo grijpt de "
        "omgeving in op de aanleg zonder de letters te veranderen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men met één woord de invloed van de opvoeding en de omgeving?",
        antwoord=["nurture", "de nurture"],
        uitleg="Nurture staat tegenover nature, de aanleg. De twee samen bepalen het "
        "fenotype.",
    ),
]

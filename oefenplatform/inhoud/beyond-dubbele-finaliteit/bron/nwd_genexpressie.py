# -*- coding: utf-8 -*-
"""🌍 Beyond dubbele finaliteit — Van DNA naar eiwit: genexpressie.

Biologie, de onderkop "Genexpressie" van de kop "Genetica" uit de vakfiche
natuurwetenschappen 3DU. Deel 1 gaat over de bouw van de dubbele helix, de
basen, het verschil tussen een gen en een allel en tussen DNA en RNA. Deel 2
gaat over de weg van DNA naar eiwit, over genotype en fenotype, over erfelijke
en niet-erfelijke eigenschappen, en over veredeling en gentechnologie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waaruit bestaan de twee lange zijkanten van de DNA-helix?",
        opties=[
            "uit suikers en fosfaatgroepen",
            "uit aminozuren aan elkaar",
            "uit vetzuren met een lange staart",
            "uit vier soorten organische basen",
        ],
        antwoord=0,
        uitleg="De zijkanten zijn een afwisseling van de suiker desoxyribose en een fosfaatgroep: de suiker-fosfaat ruggengraat. De basen hangen daar naar binnen aan vast en vormen de sporten van de ladder.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de vorm van het DNA-molecule, met twee strengen die om elkaar draaien?",
        antwoord=["dubbele helix", "een dubbele helix", "dubbelhelix"],
        uitleg="Twee strengen draaien als een gedraaide ladder om elkaar heen. Die vorm heet de dubbele helix.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke basen horen in DNA? Er zijn er vier.",
        opties=[
            "adenine",
            "cytosine",
            "guanine",
            "thymine",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg="DNA werkt met A, C, G en T. Uracil of U hoort niet in DNA thuis; die komt alleen in RNA voor, in de plaats van thymine.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke base staat in DNA altijd tegenover adenine?",
        opties=[
            "thymine",
            "guanine",
            "cytosine",
            "uracil",
        ],
        antwoord=0,
        uitleg="A paart met T en C paart met G. Door die vaste paring ligt de ene streng helemaal vast zodra je de andere kent, en daarom kan DNA zichzelf laten kopiëren.",
    ),
    dict(
        type="waarofniet",
        vraag="Tegenover cytosine staat in DNA altijd guanine.",
        antwoord=True,
        uitleg="C en G horen bij elkaar, net zoals A en T. Tussen C en G liggen drie waterstofbruggen, tussen A en T maar twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een gen?",
        opties=[
            "een stuk DNA met de code voor één eigenschap",
            "een volledig chromosoom in de celkern",
            "een eiwit dat de celdeling regelt",
            "een losse base in de DNA-streng",
        ],
        antwoord=0,
        uitleg="Een gen is een stuk van de DNA-streng dat de informatie draagt voor één erfelijke eigenschap, meestal via een eiwit. Een chromosoom draagt honderden tot duizenden genen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een gen en een allel?",
        opties=[
            "een allel is één van de mogelijke versies van een gen",
            "een allel is de losse bouwsteen van een gen",
            "een allel is een gen op het Y-chromosoom",
            "een allel is een gen dat niet werkt",
        ],
        antwoord=0,
        uitleg="Het gen voor oogkleur staat bij iedereen op dezelfde plaats. Welke versie je daar hebt staan, bruin of blauw, dat is het allel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de verschillende versies van hetzelfde gen?",
        antwoord=["allelen", "allel", "erffactoren"],
        uitleg="Allelen, in het Nederlands ook erffactoren genoemd. Je krijgt er van elk gen één van je vader en één van je moeder.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk gen ligt bij elke mens op dezelfde plaats van hetzelfde chromosoom.",
        antwoord=True,
        uitleg="De plaats van een gen ligt vast voor de hele soort. Wat verschilt, is welk allel daar staat, en juist daardoor lijken mensen op elkaar én verschillen ze.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke suiker zit in RNA?",
        opties=[
            "ribose",
            "desoxyribose",
            "glucose",
            "fructose",
        ],
        antwoord=0,
        uitleg="RNA bevat ribose, DNA bevat desoxyribose. Desoxy betekent met één zuurstofatoom minder, en dat ene atoom is het hele verschil in de naam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarin verschilt RNA van DNA? Er zijn er drie.",
        opties=[
            "RNA heeft maar één streng",
            "RNA bevat uracil in plaats van thymine",
            "RNA bevat ribose in plaats van desoxyribose",
            "RNA bevat helemaal geen fosfaatgroepen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Eén streng, uracil en ribose: dat zijn de drie verschillen. Een suiker-fosfaat ruggengraat heeft RNA net zo goed, anders zouden de bouwstenen niet aan elkaar hangen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke base neemt in RNA de plaats in van thymine?",
        antwoord=["uracil", "U", "uracil (U)"],
        uitleg="In RNA staat uracil tegenover adenine. De drie andere basen, A, C en G, zijn in DNA en RNA dezelfde.",
    ),
    dict(
        type="waarofniet",
        vraag="RNA bestaat net als DNA uit twee strengen die om elkaar draaien.",
        antwoord=False,
        uitleg="RNA heeft maar één streng. Dat is ook handig: zo kan het de kern uit en langs een ribosoom schuiven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het genotype van een organisme?",
        opties=[
            "het geheel van zijn erfelijk materiaal",
            "alles wat je aan de buitenkant ziet",
            "de som van zijn omgevingsfactoren",
            "het aantal chromosomen in zijn cellen",
        ],
        antwoord=0,
        uitleg="Het genotype is wat er in de genen staat. Wat daar uiteindelijk van te zien of te meten is, heet het fenotype.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken horen bij het fenotype? Er zijn er twee.",
        opties=[
            "de kleur van je ogen",
            "je lengte op volwassen leeftijd",
            "de twee allelen die je voor oogkleur draagt",
            "de volgorde van de basen in een gen",
        ],
        antwoord=[0, 1],
        uitleg="Het fenotype is wat je kan waarnemen of meten. De allelen en de basenvolgorde staan in het DNA zelf en horen dus bij het genotype.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee mensen met hetzelfde genotype voor een kenmerk hebben altijd exact hetzelfde fenotype.",
        antwoord=False,
        uitleg="De omgeving telt mee. Twee planten met hetzelfde genotype worden niet even groot als de ene in de volle zon staat en de andere in de schaduw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bepaalt mee je fenotype, naast je genen?",
        opties=[
            "de omgeving waarin je opgroeit",
            "het aantal chromosomen in je lichaamscellen",
            "de volgorde waarin je genen gelezen worden",
            "de grootte van je celkern",
        ],
        antwoord=0,
        uitleg="Voeding, zonlicht, beweging en ziekte sturen mee hoe de aanleg eruitkomt. Fenotype is dus altijd genen plus omgeving.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je alles wat je aan een organisme kan waarnemen of meten?",
        antwoord=["fenotype", "het fenotype"],
        uitleg="Fenotype komt van een Grieks woord voor tonen. Het is wat het organisme laat zien, het resultaat van genotype en omgeving samen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lichaamscel bevat maar één gen tegelijk.",
        antwoord=False,
        uitleg="In de kern van elke lichaamscel zit het volledige DNA, met tienduizenden genen. In een bepaalde cel staat alleen maar een deel daarvan aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lijkt een kind op allebei zijn ouders?",
        opties=[
            "het krijgt van elke ouder één allel per gen",
            "het krijgt al zijn genen van de moeder",
            "het kopieert het gedrag van zijn ouders",
            "het heeft dubbel zoveel chromosomen als zij",
        ],
        antwoord=0,
        uitleg="De eicel en de zaadcel brengen elk één exemplaar van elk chromosoom mee. Zo draagt het kind van elk gen één allel van zijn vader en één van zijn moeder.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent genexpressie?",
        opties=[
            "de informatie in een gen wordt omgezet in een eiwit",
            "een gen wordt letterlijk gekopieerd naar een nieuwe cel",
            "een gen verandert van plaats op het chromosoom",
            "een gen wordt uit het DNA geknipt en weggegooid",
        ],
        antwoord=0,
        uitleg="Een gen is pas tot uiting gekomen als zijn code echt een eiwit heeft opgeleverd. Dat omzetten van code naar eiwit heet genexpressie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar in de cel wordt het mRNA van het DNA afgelezen?",
        opties=[
            "in de celkern",
            "aan het ribosoom",
            "in het mitochondrion",
            "in het celmembraan",
        ],
        antwoord=0,
        uitleg="Het DNA blijft in de kern. Daar wordt van een gen een mRNA-kopie gemaakt, en dat mRNA verlaat de kern.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het molecule dat de code van het DNA uit de kern naar buiten brengt?",
        antwoord=["mRNA", "messenger-RNA", "boodschapper-RNA"],
        uitleg="De m staat voor messenger of boodschapper. Het mRNA draagt de boodschap van de kern naar het ribosoom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar wordt het eiwit zelf in elkaar gezet?",
        opties=[
            "aan het ribosoom",
            "in de celkern",
            "in de vacuole",
            "in het celmembraan",
        ],
        antwoord=0,
        uitleg="Het ribosoom schuift langs het mRNA en koppelt het ene aminozuur na het andere aan elkaar. Zo groeit de keten die het eiwit wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn de bouwstenen van een eiwit?",
        opties=[
            "aminozuren",
            "organische basen",
            "vetzuren",
            "enkelvoudige suikers",
        ],
        antwoord=0,
        uitleg="Een eiwit is een lange keten aminozuren. Welke aminozuren er in welke volgorde komen, staat in de code van het gen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een eiwit is opgebouwd uit aminozuren in een vaste volgorde.",
        antwoord=True,
        uitleg="Die volgorde bepaalt hoe de keten zich vouwt, en de vouwing bepaalt wat het eiwit kan. Eén aminozuur anders kan het eiwit al onbruikbaar maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zet de stappen op volgorde. Wat komt er tussen het aflezen van het gen en het klaar zijn van het eiwit?",
        opties=[
            "het mRNA reist naar een ribosoom",
            "het DNA verlaat de celkern",
            "het chromosoom verdubbelt zich",
            "de celkern lost op",
        ],
        antwoord=0,
        uitleg="Het DNA blijft altijd in de kern; alleen de mRNA-kopie reist. Die gaat naar een ribosoom, en daar wordt ze vertaald in een keten aminozuren.",
    ),
    dict(
        type="waarofniet",
        vraag="Het DNA zelf verlaat de celkern om bij het ribosoom te geraken.",
        antwoord=False,
        uitleg="Het DNA blijft veilig in de kern. Er wordt een mRNA-kopie van gemaakt, en die gaat op reis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke eigenschappen zijn erfelijk? Er zijn er twee.",
        opties=[
            "je bloedgroep",
            "je natuurlijke haarkleur",
            "een litteken op je knie",
            "een tatoeage op je arm",
        ],
        antwoord=[0, 1],
        uitleg="Bloedgroep en natuurlijke haarkleur staan in je genen. Een litteken en een tatoeage komen van buitenaf en gaan dus niet over op je kinderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een litteken geen erfelijke eigenschap?",
        opties=[
            "het verandert niets aan het DNA in je geslachtscellen",
            "het zit niet diep genoeg in de huid",
            "het verdwijnt altijd na een aantal jaren",
            "het ontstaat pas na de geboorte",
        ],
        antwoord=0,
        uitleg="Alleen wat in het DNA van de eicel of de zaadcel staat, gaat door naar een kind. Een wonde in de huid raakt die cellen niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het bewust veranderen van het erfelijk materiaal van een organisme?",
        antwoord=["genetische manipulatie", "genetische modificatie", "gentechnologie"],
        uitleg="Bij genetische manipulatie of modificatie wordt er doelgericht een stuk DNA bijgezet, weggehaald of veranderd. Dat gaat veel sneller en gerichter dan kruisen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is recombinant DNA-technologie?",
        opties=[
            "DNA van verschillende organismen wordt samengebracht",
            "DNA wordt in het labo volledig van nul opgebouwd",
            "DNA wordt tot de helft van zijn lengte ingekort",
            "DNA wordt met warmte uit de cel verwijderd",
        ],
        antwoord=0,
        uitleg="Er wordt een gen uit het ene organisme in het DNA van een ander gebracht. Zo maken bacteriën met het menselijke insulinegen echte insuline aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is veredeling?",
        opties=[
            "doelgericht kruisen en de beste nakomelingen uitkiezen",
            "een gen uit een ander organisme inbrengen",
            "planten in het labo van nul opbouwen",
            "zaden bestralen tot ze niet meer kiemen",
        ],
        antwoord=0,
        uitleg="Veredeling werkt met gewone voortplanting: kruisen, de beste nakomelingen kiezen, en opnieuw. Het duurt generaties, maar er komt geen vreemd DNA aan te pas.",
    ),
    dict(
        type="waarofniet",
        vraag="Veredeling en genetische modificatie zijn twee namen voor hetzelfde.",
        antwoord=False,
        uitleg="Veredeling kiest uit wat de natuurlijke voortplanting oplevert. Genetische modificatie grijpt rechtstreeks in het DNA in, en kan ook genen van een andere soort inbrengen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bacteriën die menselijke insuline aanmaken: welke techniek is dat?",
        opties=[
            "recombinant DNA-technologie",
            "veredeling door kruisen",
            "natuurlijke selectie",
            "kunstmatige inseminatie",
        ],
        antwoord=0,
        uitleg="Het menselijke insulinegen is in het DNA van de bacterie gebracht. De bacterie leest dat gen af alsof het van haarzelf is en maakt het eiwit aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gen dat in een cel aanwezig is, staat in die cel ook altijd aan.",
        antwoord=False,
        uitleg="Elke lichaamscel draagt al je genen, maar gebruikt er maar een deel van. In een spiercel staan andere genen aan dan in een huidcel, en daarom zien die cellen er anders uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ziet een spiercel er anders uit dan een huidcel, terwijl ze hetzelfde DNA hebben?",
        opties=[
            "in elke cel staan andere genen aan",
            "de spiercel heeft meer chromosomen",
            "de huidcel mist een deel van het DNA",
            "de spiercel heeft geen celkern meer",
        ],
        antwoord=0,
        uitleg="Het DNA is overal hetzelfde, maar niet overal even actief. Welke genen tot expressie komen, bepaalt wat de cel wordt en doet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het proces waarbij het ribosoom aminozuren aan elkaar koppelt tot een eiwit?",
        antwoord=["eiwitsynthese", "de eiwitsynthese", "translatie"],
        uitleg="Synthese betekent opbouwen. Bij de eiwitsynthese wordt de code van het mRNA vertaald in een keten aminozuren.",
    ),
    dict(
        type="waarofniet",
        vraag="Omgevingsfactoren kunnen mee bepalen hoe sterk een gen tot uiting komt.",
        antwoord=True,
        uitleg="Voeding, temperatuur en licht sturen mee welke genen hoe hard aanstaan. Zo wordt een Siamese kat donkerder op de koelste plekken van haar lichaam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een gen zonder eiwit meestal zonder gevolg?",
        opties=[
            "het eiwit doet het werk in de cel",
            "het gen is dan nog niet gekopieerd",
            "het gen zit dan op het verkeerde chromosoom",
            "het gen is dan nog niet doorgegeven",
        ],
        antwoord=0,
        uitleg="Een gen is enkel een voorschrift. Pas het eiwit bouwt, transporteert of versnelt iets, en daarom is genexpressie de stap die telt.",
    ),
]

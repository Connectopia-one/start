# -*- coding: utf-8 -*-
"""De vragen voor "Het menselijk lichaam" (✨ Spark, natuurwetenschappen).

Uit de vakfiche, deel biologie, "Belang van stofomzettingen, stofuitwisselingen
en energieomzettingen voor het functioneren van dierlijke organismen": de
onderdelen en de werking van het ademhalings-, het spijsverterings-, het
transport- en het uitscheidingsstelsel, de bestanddelen van het bloed, de
stofomzettingen in de spijsvertering, de functie van de voedingsstoffen, de
celademhaling en het beoordelen van eet- en bewegingspatronen met de actieve
voedings- en bewegingsdriehoek.

Deel 1 gaat over de onderdelen en hun functie. Deel 2 gaat over de
samenwerking tussen de stelsels, over wat er precies waar omgezet wordt, en
over het beoordelen van een voedingspatroon.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarvoor heeft je lichaam voedsel nodig?",
        opties=[
            "Als brandstof, als bouwstof en als beschermstof",
            "Alleen om je maag te vullen",
            "Alleen om warm te blijven",
        ],
        antwoord=0,
        uitleg="Voedingsstoffen zijn brandstof (energie), bouwstof (groeien en herstellen) of beschermstof (goed blijven werken, zoals vitaminen en mineralen).",
    ),
    dict(
        type="meerkeuze",
        vraag="Zet de weg van het voedsel in de juiste volgorde.",
        opties=[
            "mond – slokdarm – maag – dunne darm – dikke darm",
            "mond – maag – slokdarm – dikke darm – dunne darm",
            "mond – slokdarm – dunne darm – maag – dikke darm",
        ],
        antwoord=0,
        uitleg="Na de mond gaat het voedsel door de keel en de slokdarm naar de maag, dan door de twaalfvingerige darm en de dunne darm, en ten slotte door de dikke darm naar de endeldarm en de aars.",
    ),
    dict(
        type="invultekst",
        vraag="Het vocht in je mond dat al begint met verteren, heet ___.",
        antwoord="speeksel",
        uitleg="Speeksel komt uit de speekselklieren. Het maakt het voedsel glad en begint zetmeel af te breken, nog voor je geslikt hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij het spijsverteringsstelsel?",
        opties=["De maag", "De lever", "De longen", "De nieren"],
        antwoord=[0, 1],
        uitleg="Maag, lever, galblaas, alvleesklier en de darmen horen bij de spijsvertering. De longen horen bij de ademhaling en de nieren bij de uitscheiding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar komt de zuurstof uit de lucht in je bloed terecht?",
        opties=["In de longblaasjes", "In de luchtpijp", "In de maag"],
        antwoord=0,
        uitleg="De longblaasjes zijn piepkleine blaasjes met een heel dunne wand, omringd door haarvaten. Daar gaat zuurstof naar het bloed en koolstofdioxide eruit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de strottenklep als je slikt?",
        opties=[
            "Ze sluit de luchtpijp af",
            "Ze opent de luchtpijp",
            "Ze sluit de slokdarm af",
        ],
        antwoord=0,
        uitleg="De strottenklep klapt over de luchtpijp zodat voedsel in de slokdarm gaat. Lukt dat niet, dan schiet je in je verkeerde keelgat en moet je hoesten.",
    ),
    dict(
        type="invultekst",
        vraag="De spier onder je longen die je helpt ademen, is het ___.",
        antwoord="middenrif",
        uitleg="Het middenrif is een platte spier onder de longen. Trekt hij samen, dan wordt de borstkas groter en stroomt er lucht naar binnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit hoeveel holtes bestaat het hart?",
        opties=["Vier: twee boezems en twee kamers", "Twee", "Drie"],
        antwoord=0,
        uitleg="Het hart heeft een linker- en een rechterboezem en een linker- en een rechterkamer. De boezems vangen het bloed op, de kamers pompen het weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een slagader en een ader?",
        opties=[
            "Een slagader voert bloed weg van het hart, een ader ernaartoe",
            "Een slagader voert bloed naar het hart, een ader ervandaan",
            "Er is geen verschil",
        ],
        antwoord=0,
        uitleg="Slagaders vertrekken bij het hart en hebben een dikke, gespierde wand. Aders brengen het bloed terug en hebben kleppen die terugstromen tegengaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bestanddelen zitten er in bloed?",
        opties=["Plasma", "Rode bloedcellen", "Witte bloedcellen", "Bloedplaatjes"],
        antwoord=[0, 1, 2, 3],
        uitleg="Bloed bestaat uit plasma (de vloeistof) met daarin rode bloedcellen, witte bloedcellen en bloedplaatjes. Alle vier zijn ze nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doen de rode bloedcellen?",
        opties=["Ze vervoeren zuurstof", "Ze doden bacteriën", "Ze laten een wonde stollen"],
        antwoord=0,
        uitleg="Rode bloedcellen nemen zuurstof op in de longen en geven die af aan de cellen. Witte bloedcellen bestrijden ziektekiemen en bloedplaatjes laten je bloed stollen.",
    ),
    dict(
        type="waarofniet",
        vraag="Haarvaten zijn de allerdunste bloedvaten.",
        antwoord=True,
        uitleg="Haarvaten hebben een wand van één cellaag dik. Juist daardoor kunnen zuurstof, voedingsstoffen en afvalstoffen erdoor naar de cellen en terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk orgaan maakt urine?",
        opties=["De nier", "De blaas", "De lever"],
        antwoord=0,
        uitleg="De nieren filteren afvalstoffen uit het bloed en maken daar urine van. De blaas bewaart die urine alleen maar tot je naar het toilet gaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij het uitscheidingsstelsel?",
        opties=["De nieren", "De zweetklieren", "De longen", "De maag"],
        antwoord=[0, 1, 2],
        uitleg="Afvalstoffen verlaten je lichaam langs de nieren (urine), de zweetklieren (zweet) en de longen (koolstofdioxide en waterdamp). De maag verteert, maar scheidt niet uit.",
    ),
    dict(
        type="invultekst",
        vraag="Het buisje dat de urine van de nier naar de blaas brengt, is de ___.",
        antwoord="urineleider",
        uitleg="Elke nier heeft een urineleider naar de blaas. Van de blaas naar buiten loopt daarna één urinebuis.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de dunne darm?",
        opties=[
            "De verteerde voedingsstoffen gaan het bloed in",
            "Het voedsel wordt fijngekauwd",
            "Het water wordt eruit gehaald",
        ],
        antwoord=0,
        uitleg="In de dunne darm is de vertering klaar en worden de voedingsstoffen opgenomen in het bloed. Dat opnemen heet absorptie. De dikke darm haalt daarna vooral water eruit.",
    ),
    dict(
        type="waarofniet",
        vraag="De maag maakt maagsap.",
        antwoord=True,
        uitleg="Maagsap bevat zuur en verteringssappen. Het doodt bacteriën en begint met het afbreken van eiwitten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voedingsstoffen zijn vooral bouwstoffen?",
        opties=["Eiwitten", "Suikers", "Vitaminen"],
        antwoord=0,
        uitleg="Eiwitten leveren de bouwstenen voor spieren, huid en bloed. Suikers en vetten zijn vooral brandstof; vitaminen en mineralen zijn beschermstoffen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn voedingsvezels?",
        opties=[
            "Delen van voedsel die je niet verteert maar die je darmen op gang houden",
            "De suikers uit fruit",
            "De eiwitten uit vlees",
        ],
        antwoord=0,
        uitleg="Vezels uit groenten, fruit en volkoren producten worden niet verteerd. Ze geven je darmen werk en houden je stoelgang vlot.",
    ),
    dict(
        type="waarofniet",
        vraag="Water is een voedingsstof.",
        antwoord=True,
        uitleg="Water levert geen energie, maar je lichaam kan er niet zonder: het vervoert stoffen, regelt je temperatuur en voert afval af.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke stofomzetting gebeurt er bij de vertering van eiwitten?",
        opties=[
            "Eiwitten worden aminozuren",
            "Eiwitten worden glucose",
            "Eiwitten worden glycerol en vetzuren",
        ],
        antwoord=0,
        uitleg="Eiwitten worden afgebroken tot aminozuren, suikers zoals zetmeel tot glucose, en vetten tot glycerol en drie vetzuren.",
    ),
    dict(
        type="invultekst",
        vraag="Bij de vertering wordt zetmeel omgezet in ___.",
        antwoord="glucose",
        uitleg="Zetmeel is een lange keten van glucosemoleculen. Speeksel en darmsap knippen die keten in losse glucosemoleculen, klein genoeg om in het bloed te gaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarin wordt een vet gesplitst bij de vertering?",
        opties=[
            "In glycerol en drie vetzuren",
            "In twee aminozuren",
            "In glucose en water",
        ],
        antwoord=0,
        uitleg="Elk vetmolecuul valt uiteen in één glycerol en drie vetzuren. Gal maakt de vetdruppels daarvoor eerst heel klein.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet gal?",
        opties=[
            "Het verdeelt vetten in kleine druppeltjes",
            "Het verteert eiwitten",
            "Het neemt zuurstof op",
        ],
        antwoord=0,
        uitleg="Gal wordt in de lever gemaakt en in de galblaas bewaard. In de twaalfvingerige darm maakt het van vet heel kleine druppeltjes, zodat de verteringssappen er beter bij kunnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke sappen helpen bij de vertering?",
        opties=["Maagsap", "Alvleessap", "Darmsap", "Zweet"],
        antwoord=[0, 1, 2],
        uitleg="Speeksel, maagsap, gal, alvleessap en darmsap horen bij de vertering. Zweet is een uitscheidingsproduct en heeft er niets mee te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke omzetting gebeurt er bij de celademhaling?",
        opties=[
            "Glucose en zuurstofgas worden koolstofdioxide, water en energie",
            "Koolstofdioxide en water worden glucose",
            "Eiwitten worden aminozuren",
        ],
        antwoord=0,
        uitleg="Celademhaling is de verbranding van glucose in de mitochondriën. De energie die vrijkomt, gebruikt de cel om te werken; de rest gaat verloren als warmte.",
    ),
    dict(
        type="waarofniet",
        vraag="Celademhaling gebeurt in de longen.",
        antwoord=False,
        uitleg="Celademhaling gebeurt in élke cel, in de mitochondriën. De longen zorgen alleen voor de aanvoer van zuurstof en de afvoer van koolstofdioxide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stelsels moeten samenwerken om één spiercel aan het werk te houden?",
        opties=[
            "Het ademhalingsstelsel, voor de zuurstof",
            "Het spijsverteringsstelsel, voor de glucose",
            "Het transportstelsel, dat allebei aanvoert",
            "Het beenderstelsel, dat de energie levert",
        ],
        antwoord=[0, 1, 2],
        uitleg="De cel krijgt zuurstof van de longen en glucose uit de darmen, en het bloed brengt ze allebei. Beenderen dragen je lichaam, maar leveren geen energie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de kleine bloedsomloop?",
        opties=[
            "De weg van het hart naar de longen en terug",
            "De weg van het hart naar de rest van het lichaam en terug",
            "De weg van de darmen naar de lever",
        ],
        antwoord=0,
        uitleg="In de kleine bloedsomloop gaat zuurstofarm bloed via de longslagader naar de longen en komt het als zuurstofrijk bloed via de longader terug.",
    ),
    dict(
        type="waarofniet",
        vraag="In de longslagader stroomt zuurstofarm bloed.",
        antwoord=True,
        uitleg="Een slagader heet zo omdat ze van het hart wegvoert, niet omdat er zuurstofrijk bloed in zit. De longslagader brengt net zuurstofarm bloed naar de longen.",
    ),
    dict(
        type="invultekst",
        vraag="De grootste slagader van het lichaam, die uit de linkerkamer vertrekt, is de ___.",
        antwoord="aorta",
        uitleg="De aorta vervoert zuurstofrijk bloed naar het hele lichaam. De holle aders brengen het zuurstofarme bloed daarna terug naar de rechterboezem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderdelen vind je in een nier?",
        opties=["De schors", "Het merg", "Het nierbekken", "De boezem"],
        antwoord=[0, 1, 2],
        uitleg="Een nier bestaat van buiten naar binnen uit het kapsel, de schors, het merg met zijn piramides, en het bekken waar de urine samenkomt. Een boezem is een deel van het hart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft je lichaam bloedplaatjes nodig?",
        opties=[
            "Om een wonde te laten stollen",
            "Om zuurstof te vervoeren",
            "Om voedsel te verteren",
        ],
        antwoord=0,
        uitleg="Bloedplaatjes klitten bij een wonde samen en vormen een propje. Zonder bloedplaatjes zou een kleine snee blijven bloeden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je loopt hard. Waarom ga je sneller ademen én sneller met je hart kloppen?",
        opties=[
            "Je spiercellen hebben meer zuurstof en glucose nodig, en het afval moet sneller weg",
            "Je longen worden groter",
            "Je bloed wordt dunner",
        ],
        antwoord=0,
        uitleg="Meer celademhaling betekent meer verbruik van zuurstof en glucose en meer koolstofdioxide. De ademhaling en de bloedsomloop versnellen om dat bij te houden.",
    ),
    dict(
        type="waarofniet",
        vraag="Onverteerde resten verlaten je lichaam via de endeldarm en de aars.",
        antwoord=True,
        uitleg="Wat niet verteerd of opgenomen is, gaat als voedselresten door de dikke darm naar de endeldarm. Dat is iets anders dan uitscheiding van afvalstoffen uit het bloed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er onderaan, in het donkergroene deel van de actieve voedingsdriehoek?",
        opties=[
            "Water, groenten, fruit en volle granen",
            "Vlees en vis",
            "Koek en frisdrank",
        ],
        antwoord=0,
        uitleg="De driehoek zet plantaardige voeding en water onderaan: daar eet je het meest van. Hoe hoger je komt, hoe minder je er best van eet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand eet elke dag frieten en drinkt frisdrank, en zit de hele dag stil. Welke aanpassingen maken dat patroon gezonder?",
        opties=[
            "Meer groenten en fruit eten",
            "Water drinken in plaats van frisdrank",
            "Elke dag bewegen",
            "Meer koeken eten om aan energie te komen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De actieve voedings- en bewegingsdriehoek zegt: meer plantaardig, minder bewerkt, water als drank, en zo weinig mogelijk lang stilzitten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat lang stilzitten in de rode bol van de bewegingsdriehoek?",
        opties=[
            "Omdat het ongezond is en je het beter zo veel mogelijk onderbreekt",
            "Omdat het de beste vorm van beweging is",
            "Omdat het alleen voor sporters geldt",
        ],
        antwoord=0,
        uitleg="De rode bol is wat je best vermijdt. Lang stilzitten is ongezond, ook als je daarnaast sport; sta dus regelmatig even recht.",
    ),
    dict(
        type="invultekst",
        vraag="Het opnemen van verteerde voedingsstoffen in het bloed heet ___.",
        antwoord="absorptie",
        uitleg="De absorptie gebeurt in de dunne darm, door de darmvlokken heen. Die vlokken maken het oppervlak van de darm enorm groot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk van deze is een ademhalingsproduct?",
        opties=["Koolstofdioxide", "Urine", "Voedselresten"],
        antwoord=0,
        uitleg="Koolstofdioxide en waterdamp adem je uit. Urine is een uitscheidingsproduct en voedselresten zijn wat er van de vertering overblijft.",
    ),
]

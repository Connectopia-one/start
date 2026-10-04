# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Homeostase en waterhuishouding bij planten.

Eerste kop van de vakfiche biologie 2de graad doorstroomfinaliteit, voor de
studierichting natuurwetenschappen. Dat onderdeel weegt 10 % van het examen.

Deel 1 gaat over homeostase zelf, het feedbacksysteem van de plant en de drie
stappen van de waterhuishouding. Deel 2 gaat over de organen en weefsels van
de plant, het transport van water en assimilaten, de band met de fotosynthese,
en over prikkels bij planten: nastie, tropie en de plantenhormonen.

De fiche zet die prikkels bij planten onder dezelfde noemer als de
waterhuishouding ("homeostase en prikkels bij planten"), vandaar dat ze hier
staan en niet bij het zenuwstelsel.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent homeostase bij een plant?",
        opties=[
            "haar inwendig milieu binnen nauwe grenzen houden terwijl de omgeving verandert",
            "haar bladeren afwerpen van zodra de temperatuur buiten begint te dalen",
            "haar wortels zo diep mogelijk door de lagen van de bodem laten groeien",
            "haar groei helemaal stilleggen zodra er een periode van droogte aanbreekt",
        ],
        antwoord=0,
        uitleg="Homeostase is het in stand houden van een inwendig evenwicht. De omgeving van een plant wisselt voortdurend, en met regelsystemen houdt ze haar eigen milieu toch stabiel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke omgevingsfactoren beïnvloeden de waterhuishouding van een plant? Kruis alles aan wat juist is.",
        opties=[
            "de lichtsterkte die op de bladeren valt",
            "de temperatuur van de lucht rondom de plant",
            "de vochtigheidsgraad van de bodem en van de lucht",
            "de kleur die de bloemblaadjes van de plant hebben",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt licht, temperatuur en de vochtigheidsgraad van bodem en lucht. De kleur van de bloemblaadjes speelt geen rol in de waterhuishouding.",
    ),
    dict(
        type="waarofniet",
        vraag="In een feedbacksysteem gebruikt de plant het gevolg van een proces om dat proces zelf bij te sturen.",
        antwoord=True,
        uitleg="Dat is precies wat terugkoppeling betekent. Verliest een blad te veel water, dan sluiten de huidmondjes en daalt het verlies weer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit welke drie stappen bestaat de waterhuishouding van een plant?",
        opties=[
            "wateropname, watertransport en transpiratie",
            "wateropname, verbranding en vervolgens uitscheiding",
            "verdamping, bevriezing en daarna opnieuw ontdooien",
            "watertransport, bloei en tot slot de vorming van zaden",
        ],
        antwoord=0,
        uitleg="De plant neemt water op in de wortel, vervoert het naar boven en laat het als damp ontsnappen. Die drie stappen samen vormen de waterhuishouding.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de druk van het vocht in de vacuole waardoor een plantencel stevig blijft staan?",
        antwoord=["turgor", "turgordruk", "de turgor"],
        uitleg="Een cel vol water duwt tegen haar celwand. Die druk heet turgor, en zij houdt een niet-houtige plant rechtop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kamerplant die te lang geen water kreeg, hangt slap. Hoe verklaar je dat?",
        opties=[
            "de vacuolen zijn leeggelopen, waardoor de turgor wegvalt",
            "de celwanden zijn door het watergebrek helemaal opgelost",
            "de chloroplasten hebben hun groene kleurstof losgelaten",
            "de wortels hebben zich van de stengel losgemaakt",
        ],
        antwoord=0,
        uitleg="Zonder water loopt de vacuole leeg, duwt de cel niet meer tegen haar wand en zakt de plant in elkaar. Geef je water, dan komt de turgor terug.",
    ),
    dict(
        type="waarofniet",
        vraag="Transpiratie bij een plant is het verlies van water in de vorm van waterdamp.",
        antwoord=True,
        uitleg="Transpiratie is verdamping: vloeibaar water in het blad wordt damp en ontsnapt door de huidmondjes naar buiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee cellen vormen samen een huidmondje en regelen of het open of dicht staat?",
        opties=[
            "de sluitcellen",
            "de wortelharen",
            "de zeefvatcellen",
            "de pigmentcellen",
        ],
        antwoord=0,
        uitleg="Een huidmondje bestaat uit twee sluitcellen. Vullen ze zich met water, dan bollen ze op en gaat de opening ertussen open.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij droogte zet een plant haar huidmondjes juist verder open om sneller water op te nemen.",
        antwoord=False,
        uitleg="Omgekeerd: bij droogte sluit de plant haar huidmondjes, want zo verliest ze minder water. Ze kiest dorst boven uitdroging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is worteldruk?",
        opties=[
            "de druk waarmee de wortel water de houtvaten in duwt",
            "de druk waarmee de bodem op de wortel van buiten drukt",
            "de druk van de wind die de stengel doet doorbuigen",
            "de druk waarmee het blad suikers naar beneden perst",
        ],
        antwoord=0,
        uitleg="De wortel neemt water op en duwt het van onderaf de houtvaten in. Die duwkracht heet worteldruk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke krachten helpen het water in een plant omhoog? Kruis alles aan wat juist is.",
        opties=[
            "de worteldruk die van onderaf duwt",
            "de transpiratiezuiging die van bovenaf trekt",
            "de capillariteit in de nauwe houtvaten",
            "de zwaartekracht die op de waterkolom werkt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Duwen van onder, trekken van boven en de hechting in nauwe buisjes werken samen. De zwaartekracht werkt juist tegen: zij trekt het water naar beneden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het opstijgen van water in heel nauwe buisjes, zoals in de houtvaten?",
        antwoord=["capillariteit", "capillaire werking"],
        uitleg="In een nauw buisje hecht water zich aan de wand en kruipt het vanzelf omhoog. Dat verschijnsel heet capillariteit.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe warmer en droger de lucht rond een blad, hoe sterker de transpiratie.",
        antwoord=True,
        uitleg="Warme, droge lucht neemt makkelijker waterdamp op. Daarom verdampt een plant op een warme winderige dag veel meer dan in vochtige lucht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de transpiratie niet enkel verlies voor de plant?",
        opties=[
            "ze trekt water en mineralen mee omhoog en koelt het blad af",
            "ze maakt in het blad rechtstreeks nieuwe suikers aan",
            "ze zorgt ervoor dat de wortels zich kunnen vertakken",
            "ze geeft de bladeren hun groene kleur in de zomer",
        ],
        antwoord=0,
        uitleg="De zuiging die door de verdamping ontstaat, trekt de waterkolom omhoog en voert zo mineralen aan. Daarbij koelt het verdampen het blad af.",
    ),
    dict(
        type="waarofniet",
        vraag="De vochtigheidsgraad van de bodem is voor de plant een biotische factor.",
        antwoord=False,
        uitleg="Vocht leeft niet, dus is het een abiotische factor. Biotisch zijn de levende factoren, zoals andere planten en de dieren eromheen.",
    ),
    dict(
        type="invultekst",
        vraag="In welk celonderdeel van een plantencel wordt het meeste vocht opgeslagen?",
        antwoord=["vacuole", "de vacuole", "centrale vacuole"],
        uitleg="Bij een rijpe plantencel neemt de centrale vacuole het grootste deel van het volume in. Daarin zit het vocht dat voor de turgor zorgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar liggen de huidmondjes van een gewoon blad meestal?",
        opties=[
            "vooral aan de onderkant van het blad",
            "vooral aan de bovenkant van het blad",
            "gelijk verdeeld over beide zijden",
            "enkel op de bladnerven zelf",
        ],
        antwoord=0,
        uitleg="Aan de onderkant is het koeler en schaduwrijker, dus verdampt daar minder water. Daarom liggen de meeste huidmondjes net daar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een plant staat in de volle zon en de bodem droogt uit. Wat gebeurt er achtereenvolgens?",
        opties=[
            "de huidmondjes sluiten, de transpiratie daalt en de fotosynthese vertraagt",
            "de huidmondjes gaan verder open en de fotosynthese versnelt",
            "de worteldruk stijgt zodat de plant meer water uit de lucht haalt",
            "de vacuolen vullen zich extra ver zodat de plant stevig blijft",
        ],
        antwoord=0,
        uitleg="Sluiten de huidmondjes, dan houdt de plant water binnen maar komt er ook minder koolstofdioxide binnen. De fotosynthese valt daardoor grotendeels stil.",
    ),
    dict(
        type="waarofniet",
        vraag="Een plant die haar huidmondjes sluit, kan daarna even goed verder fotosynthetiseren.",
        antwoord=False,
        uitleg="Door de gesloten huidmondjes komt er nauwelijks nog koolstofdioxide binnen, en zonder die grondstof valt de fotosynthese grotendeels stil.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de zuigkracht die in het blad ontstaat doordat daar water verdampt?",
        antwoord=["transpiratiezuiging", "zuigkracht", "transpiratiezuigkracht"],
        uitleg="Verdampt er water uit het blad, dan trekt dat als een draad aan de hele waterkolom in de houtvaten. Die kracht heet transpiratiezuiging.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke vier organen onderscheidt men bij een bloeiende plant?",
        opties=[
            "wortel, stengel, blad en bloem",
            "wortel, knol, schors en zaad",
            "stengel, doorn, hars en vrucht",
            "blad, nerf, steeltje en kiem",
        ],
        antwoord=0,
        uitleg="De fiche noemt vier plantenorganen: de wortel, de stengel, het blad en de bloem. Elk heeft zijn eigen taak in de plant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke weefsels horen bij het huidweefsel van een plant? Kruis alles aan wat juist is.",
        opties=[
            "de epidermis",
            "de cuticula of waslaag",
            "de bast",
            "het xyleem",
        ],
        antwoord=[0, 1, 2],
        uitleg="Epidermis, cuticula en bast bedekken de plant aan de buitenkant. Het xyleem is transportweefsel en ligt juist binnenin.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het dunne waslaagje bovenop de epidermis van een blad?",
        antwoord=["cuticula", "de cuticula", "waslaag"],
        uitleg="De cuticula is een waterafstotend laagje dat het blad tegen uitdroging beschermt. Daarom glanst een blad vaak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat vervoert het xyleem of de houtvaten?",
        opties=[
            "water en opgeloste mineralen vanuit de wortel",
            "suikers vanuit het blad naar de rest van de plant",
            "zuurstofgas vanuit de lucht naar de wortels",
            "hormonen vanuit de bloem naar de vruchten",
        ],
        antwoord=0,
        uitleg="Het xyleem is de weg omhoog: water en mineralen gaan van de wortel naar het blad. De suikers gaan door het floëem.",
    ),
    dict(
        type="waarofniet",
        vraag="Het floëem of de zeefvaten vervoeren de suikers die bij de fotosynthese gemaakt zijn.",
        antwoord=True,
        uitleg="De suikers uit het blad heten assimilaten, en het floëem brengt ze naar waar de plant ze nodig heeft of opslaat.",
    ),
    dict(
        type="waarofniet",
        vraag="In het floëem gaan de suikers altijd van boven naar beneden.",
        antwoord=False,
        uitleg="Het transport gaat naar waar de plant de suiker nodig heeft. In het voorjaar gaat het net omhoog, van een wortelknol naar de ontluikende knoppen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het geheel waarin xyleem en floëem samen liggen?",
        antwoord=["vaatbundel", "de vaatbundel", "vaatbundels"],
        uitleg="Xyleem en floëem liggen naast elkaar in één streng, de vaatbundel. In een blad zie je die als een nerf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de taak van het vulweefsel in een plant?",
        opties=[
            "het vult de ruimte tussen de andere weefsels en slaat stoffen op",
            "het vangt als enige weefsel het zonlicht voor de fotosynthese op",
            "het pompt met samentrekkende cellen het water naar boven",
            "het vormt de buitenste beschermlaag rond de hele plant",
        ],
        antwoord=0,
        uitleg="Vulweefsel of grondweefsel vult de ruimte op tussen huid- en transportweefsel, en dient daarbij voor opslag en uitwisseling van stoffen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke reactievergelijking hoort bij de fotosynthese?",
        opties=[
            "6 CO₂ + 6 H₂O geeft C₆H₁₂O₆ + 6 O₂",
            "C₆H₁₂O₆ + 6 O₂ geeft 6 CO₂ + 6 H₂O",
            "6 O₂ + 6 H₂O geeft C₆H₁₂O₆ + 6 CO₂",
            "C₆H₁₂O₆ geeft 6 CO₂ + 6 H₂O + 6 O₂",
        ],
        antwoord=0,
        uitleg="Koolstofdioxide en water worden met lichtenergie omgezet in glucose, en daarbij komt zuurstofgas vrij. De tweede vergelijking is net de celademhaling.",
    ),
    dict(
        type="invultekst",
        vraag="In welk celorganel van een bladcel gebeurt de fotosynthese?",
        antwoord=["chloroplast", "de chloroplast", "bladgroenkorrel"],
        uitleg="De chloroplast of bladgroenkorrel bevat het chlorofyl dat het licht opvangt. Daar start de fotosynthese.",
    ),
    dict(
        type="waarofniet",
        vraag="De glucose die bij de fotosynthese ontstaat, noemen we een assimilaat.",
        antwoord=True,
        uitleg="Assimilaten zijn de stoffen die de plant zelf opbouwt uit anorganische grondstoffen. Glucose is daarvan het bekendste voorbeeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een goede waterhuishouding nodig voor de fotosynthese? Kruis alles aan wat juist is.",
        opties=[
            "water is zelf een grondstof van de fotosynthese",
            "open huidmondjes laten de koolstofdioxide binnen",
            "het watertransport brengt mineralen naar het blad",
            "water geeft het blad zijn groene kleurstof",
        ],
        antwoord=[0, 1, 2],
        uitleg="Water is grondstof, de huidmondjes staan alleen open als er water genoeg is, en de waterstroom voert mineralen aan. De groene kleur komt van chlorofyl, niet van water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een fotoreceptor bij een plant?",
        opties=[
            "een structuur die licht opvangt en zo een prikkel doorgeeft",
            "een klier die suikers rechtstreeks in de bodem afgeeft",
            "een cel die de temperatuur van de bodem meet",
            "een opening waardoor water uit het blad ontsnapt",
        ],
        antwoord=0,
        uitleg="Een receptor vangt een prikkel op. Een fotoreceptor doet dat met licht en zet zo een reactie van de plant in gang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een nastie en een tropie bij een plant?",
        opties=[
            "bij een tropie hangt de richting van de beweging af van de richting van de prikkel",
            "bij een nastie hangt de richting van de beweging af van de richting van de prikkel",
            "een nastie gebeurt enkel 's nachts en een tropie enkel overdag",
            "een tropie komt alleen bij wortels voor en een nastie alleen bij bladeren",
        ],
        antwoord=0,
        uitleg="Een tropie is gericht: de plant groeit naar de prikkel toe of ervan weg. Bij een nastie is de beweging altijd dezelfde, waar de prikkel ook vandaan komt.",
    ),
    dict(
        type="waarofniet",
        vraag="Dat een wortel naar beneden groeit en een stengel naar boven, is een voorbeeld van tropie.",
        antwoord=True,
        uitleg="Dat is geotropie, de reactie op de zwaartekracht. De richting van de prikkel bepaalt de richting van de groei, dus is het een tropie.",
    ),
    dict(
        type="invultekst",
        vraag="Welk plantenhormoon zorgt voor celstrekking en laat een stengel naar het licht buigen?",
        antwoord=["auxine", "het auxine", "auxines"],
        uitleg="Auxine hoopt zich op aan de schaduwzijde en laat de cellen daar sterker uitrekken. Daardoor buigt de stengel naar het licht toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk hormoon speelt een hoofdrol bij het rijpen van vruchten?",
        opties=[
            "ethyleen",
            "abscisinezuur",
            "insuline",
            "thyroxine",
        ],
        antwoord=0,
        uitleg="Ethyleen is een gasvormig plantenhormoon dat het rijpen versnelt. Daarom rijpt fruit sneller in een gesloten zak bij een rijpe appel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet abscisinezuur bij droogte?",
        opties=[
            "het laat de huidmondjes sluiten zodat de plant water spaart",
            "het laat de huidmondjes verder opengaan voor meer koeling",
            "het versnelt de bloei zodat er snel zaden gevormd worden",
            "het zet de wortels aan om zich boven de grond te vertakken",
        ],
        antwoord=0,
        uitleg="Abscisinezuur is het stresshormoon van de plant. Het geeft de sluitcellen het signaal om dicht te gaan, en zo daalt het waterverlies.",
    ),
    dict(
        type="waarofniet",
        vraag="Plantenhormonen werken enkel in de bloem en nergens anders in de plant.",
        antwoord=False,
        uitleg="Ze werken overal: bij de wortelgroei, de vorming van zijscheuten, het bladverlies, de celstrekking en de waterhuishouding.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een plant gaat een prikkel langs zenuwen naar een centrale hersenstructuur.",
        antwoord=False,
        uitleg="Een plant heeft geen zenuwen en geen hersenen. Haar coördinatie verloopt met hormonen die traag door de plant verspreid worden.",
    ),
]

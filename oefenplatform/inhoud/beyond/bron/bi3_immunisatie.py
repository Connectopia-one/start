# -*- coding: utf-8 -*-
"""Immunisatie, bloedgroepen en falende afweer — 🌍 Beyond, biologie.

Deel 1 gaat over immunisatie: het verschil tussen actief en passief, tussen
natuurlijk en kunstmatig, en het ABO-bloedgroepensysteem met de gevolgen voor
een bloedtransfusie. Deel 2 gaat over de resusfactor bij een zwangerschap en
over een immuunsysteem dat faalt: allergie, auto-immuunziekte en hiv.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is immunisatie?",
        opties=[
            "immuniteit verwerven tegen een bepaald antigeen",
            "een ontsteking in een wonde onderdrukken met zalf",
            "het aantal rode bloedcellen in het bloed verhogen",
            "de temperatuur van het lichaam kunstmatig verlagen",
        ],
        antwoord=0,
        uitleg="Bij immunisatie krijgt iemand bescherming tegen één antigeen, door zelf "
        "antilichamen te maken of door ze te ontvangen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor actieve immunisatie? Kruis alles aan wat juist is.",
        opties=[
            "je maakt zelf antilichamen aan",
            "je bouwt geheugencellen op",
            "de bescherming is onmiddellijk volledig",
            "je krijgt kant-en-klare antilichamen",
        ],
        antwoord=[0, 1],
        uitleg="Bij actieve immunisatie doet je eigen afweer het werk. Dat duurt langer, "
        "maar levert geheugencellen en dus langdurige bescherming op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor passieve immunisatie? Kruis alles aan wat juist is.",
        opties=[
            "je krijgt antilichamen van buitenaf",
            "de bescherming werkt onmiddellijk",
            "je maakt zelf geheugencellen aan",
            "je afweer leert het antigeen zelf kennen",
        ],
        antwoord=[0, 1],
        uitleg="Bij passieve immunisatie krijg je kant-en-klare antilichamen. Die werken "
        "meteen, maar verdwijnen na weken en laten geen geheugen achter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kind maakt mazelen door en is daarna beschermd. Welke immunisatie is dat?",
        opties=[
            "natuurlijke actieve immunisatie",
            "kunstmatige actieve immunisatie",
            "natuurlijke passieve immunisatie",
            "kunstmatige passieve immunisatie",
        ],
        antwoord=0,
        uitleg="Het kind maakte zelf antilichamen, dus actief, en zonder dat iemand "
        "ingreep, dus natuurlijk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men kunstmatige actieve immunisatie, met het gewone woord?",
        antwoord=["vaccinatie", "inenting", "vaccineren"],
        uitleg="Bij een vaccinatie krijg je een onschadelijk gemaakte of afgezwakte vorm "
        "van het antigeen. Je afweer maakt daar zelf antilichamen en geheugencellen tegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een baby krijgt via de placenta antilichamen van zijn moeder. Welke immunisatie is dat?",
        opties=[
            "natuurlijke passieve immunisatie",
            "natuurlijke actieve immunisatie",
            "kunstmatige passieve immunisatie",
            "kunstmatige actieve immunisatie",
        ],
        antwoord=0,
        uitleg="De baby krijgt de antilichamen kado, dus passief, en op een natuurlijke "
        "weg. Borstvoeding werkt op dezelfde manier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand wordt gebeten door een dier en krijgt onmiddellijk antilichamen ingespoten. Welke immunisatie is dat?",
        opties=[
            "kunstmatige passieve immunisatie",
            "kunstmatige actieve immunisatie",
            "natuurlijke passieve immunisatie",
            "natuurlijke actieve immunisatie",
        ],
        antwoord=0,
        uitleg="Dat is serumtherapie: kant-en-klare antilichamen van buitenaf. Het werkt "
        "meteen, wat nodig is als er geen tijd is om zelf antilichamen te maken.",
    ),
    dict(
        type="waarofniet",
        vraag="De bescherming die een baby via borstvoeding krijgt, verdwijnt na een tijd.",
        antwoord=True,
        uitleg="Het zijn geleende antilichamen, zonder geheugencellen. Na enkele maanden "
        "zijn ze afgebroken en moet het kind zijn eigen afweer opbouwen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vaccin bevat altijd levende, volledig besmettelijke ziekteverwekkers.",
        antwoord=False,
        uitleg="Een vaccin bevat een afgezwakte of dode verwekker, een stukje ervan of "
        "enkel de boodschap om dat stukje te maken. Ziek word je er niet van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom beschermt een hoge vaccinatiegraad ook wie zelf niet gevaccineerd is?",
        opties=[
            "de verwekker vindt bijna geen nieuwe gastheer meer",
            "de verwekker verdwijnt dan uit alle dieren tegelijk",
            "iedereen krijgt dan automatisch antilichamen",
            "de verwekker verliest dan zijn eigen erfelijk materiaal",
        ],
        antwoord=0,
        uitleg="Als bijna iedereen beschermd is, stokt de besmettingsketen. Dat heet "
        "groepsimmuniteit en beschermt wie te jong of te ziek is om zich te laten inenten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarop steunt het ABO-bloedgroepensysteem?",
        opties=[
            "de antigenen op de rode bloedcellen",
            "het aantal witte bloedcellen in het bloed",
            "de hoeveelheid hemoglobine per cel",
            "de dikte van het membraan van de cellen",
        ],
        antwoord=0,
        uitleg="Op de rode bloedcellen staan suikerketens A, B, beide of geen van beide. "
        "Dat bepaalt de bloedgroep A, B, AB of O.",
    ),
    dict(
        type="invultekst",
        vraag="Welke antigenen staan er op de rode bloedcellen van iemand met bloedgroep AB?",
        antwoord=["A en B", "A en B", "AB"],
        uitleg="Bloedgroep AB heeft beide antigenen. Daarom heeft die persoon geen "
        "anti-A- en geen anti-B-antilichamen in zijn plasma.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke antilichamen zitten in het plasma van iemand met bloedgroep A?",
        opties=["anti-B", "anti-A", "anti-A en anti-B", "geen van de twee"],
        antwoord=0,
        uitleg="Je maakt antilichamen tegen wat je zelf niet hebt. Bloedgroep A heeft dus "
        "anti-B in het plasma.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is bloedgroep O de universele donor voor rode bloedcellen?",
        opties=[
            "haar cellen hebben geen A- en geen B-antigeen",
            "haar plasma bevat geen enkel antilichaam",
            "haar cellen hebben beide antigenen",
            "haar cellen hebben helemaal geen membraan",
        ],
        antwoord=0,
        uitleg="Zonder A- en B-antigeen is er niets waaraan de antilichamen van de "
        "ontvanger zich kunnen vastklitten.",
    ),
    dict(
        type="invultekst",
        vraag="Welke bloedgroep is de universele ontvanger?",
        antwoord=["AB", "ab", "bloedgroep AB"],
        uitleg="Bloedgroep AB heeft geen anti-A en geen anti-B in haar plasma. Daardoor "
        "kan ze rode bloedcellen van elke groep aannemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij een transfusie met incompatibel bloed? Kruis alles aan wat juist is.",
        opties=[
            "de rode bloedcellen klitten samen",
            "de rode bloedcellen gaan kapot",
            "het plasma verandert van bloedgroep",
            "de ontvanger krijgt een nieuwe bloedgroep",
        ],
        antwoord=[0, 1],
        uitleg="De antilichamen van de ontvanger laten de gegeven cellen agglutineren en "
        "daarna hemolyseren. De klompjes verstoppen bloedvaten; dat is levensgevaarlijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Hemolyse is het kapotgaan van rode bloedcellen.",
        antwoord=True,
        uitleg="Bij hemolyse barst de cel en komt de hemoglobine vrij in het plasma. Dat "
        "belast onder meer de nieren zwaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand met bloedgroep B krijgt bloed van groep A. Waarom loopt dat fout?",
        opties=[
            "de anti-A van de ontvanger valt de cellen aan",
            "de anti-B van de ontvanger valt de cellen aan",
            "de ontvanger heeft geen antilichamen in zijn plasma",
            "de gegeven cellen hebben geen enkel antigeen",
        ],
        antwoord=0,
        uitleg="Bloedgroep B heeft anti-A in het plasma. Komen er cellen met A-antigeen "
        "binnen, dan klitten die samen.",
    ),
    dict(
        type="waarofniet",
        vraag="De bloedgroep van iemand verandert in de loop van zijn leven.",
        antwoord=False,
        uitleg="De bloedgroep staat in het DNA en blijft dezelfde. Enkel na een "
        "beenmergtransplantatie kan ze mee veranderen met het nieuwe beenmerg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom mag plasma van groep O niet zonder meer aan iedereen gegeven worden?",
        opties=[
            "het bevat anti-A en anti-B",
            "het bevat geen enkel antilichaam",
            "het bevat A- en B-antigenen",
            "het bevat geen enkel eiwit meer",
        ],
        antwoord=0,
        uitleg="Voor rode bloedcellen is O de universele donor, voor plasma net niet: "
        "daar zitten juist beide antilichamen in. Voor plasma is AB de universele donor.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent resuspositief?",
        opties=[
            "er staat een D-antigeen op de rode bloedcellen",
            "er staat geen enkel antigeen op de rode bloedcellen",
            "er zitten anti-D-antilichamen in het plasma",
            "er zitten geen antilichamen in het plasma",
        ],
        antwoord=0,
        uitleg="De resusfactor is het D-antigeen. Wie het heeft, is resuspositief; wie "
        "het niet heeft, is resusnegatief.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het antigeen van de resusfactor?",
        antwoord=["D-antigeen", "D", "het D-antigeen"],
        uitleg="Het D-antigeen bepaalt of iemand resuspositief of resusnegatief is. Een "
        "resusnegatieve persoon kan er anti-D-antilichamen tegen maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan een resusnegatieve moeder met een resuspositief kind een probleem krijgen?",
        opties=[
            "ze kan anti-D-antilichamen aanmaken",
            "haar bloedgroep verandert door de zwangerschap",
            "haar kind maakt anti-D tegen haar bloed",
            "haar plasma verliest al zijn antilichamen",
        ],
        antwoord=0,
        uitleg="Komt bloed van het kind in haar bloedbaan, dan ziet haar afweer het "
        "D-antigeen als vreemd. Dat geeft anti-D-antilichamen en geheugencellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom loopt het eerste resuspositieve kind meestal geen gevaar?",
        opties=[
            "de antilichamen ontstaan pas rond de bevalling",
            "het eerste kind heeft nog geen D-antigeen",
            "de moeder maakt in het begin geen enkel antilichaam",
            "de placenta laat helemaal geen antilichamen door",
        ],
        antwoord=0,
        uitleg="De bloedmenging gebeurt vooral tijdens de bevalling. Het eerste kind is "
        "dan al geboren; een volgend kind loopt wel gevaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe wordt het resusprobleem bij een zwangerschap voorkomen?",
        opties=[
            "de moeder krijgt een anti-D-inspuiting",
            "het kind krijgt een vaccin tegen resus",
            "de moeder krijgt bloed van groep O",
            "het kind krijgt extra ijzer toegediend",
        ],
        antwoord=0,
        uitleg="De anti-D-inspuiting ruimt de cellen van het kind op voor de moeder zelf "
        "antilichamen kan maken. Zo blijft er geen geheugen achter.",
    ),
    dict(
        type="waarofniet",
        vraag="Antilichamen van de moeder kunnen de placenta over en in het bloed van het kind komen.",
        antwoord=True,
        uitleg="Daarom beschermt een moeder haar baby de eerste maanden, maar daarom "
        "kunnen anti-D-antilichamen ook de rode bloedcellen van het kind aanvallen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een allergie?",
        opties=[
            "een overdreven afweer tegen iets onschuldigs",
            "een afweer die zich tegen eigen cellen keert",
            "een afweer die helemaal niet meer werkt",
            "een tekort aan rode bloedcellen in het bloed",
        ],
        antwoord=0,
        uitleg="Bij een allergie reageert de afweer hevig op stuifmeel, huisstofmijt of "
        "een voedingsmiddel. De stof zelf is niet gevaarlijk.",
    ),
    dict(
        type="invultekst",
        vraag="Welk soort antilichaam speelt de hoofdrol bij een allergie?",
        antwoord=["IgE", "ige", "IgE-antilichamen"],
        uitleg="IgE-antilichamen gaan op de mestcellen zitten. Komt het allergeen "
        "opnieuw, dan zetten die mestcellen histamine vrij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke klachten komen van de histamine bij een allergische reactie? Kruis alles aan wat juist is.",
        opties=[
            "een loopneus en tranende ogen",
            "zwelling en jeuk van de huid",
            "een blijvend lagere bloeddruk na jaren",
            "een tekort aan witte bloedcellen",
        ],
        antwoord=[0, 1],
        uitleg="Histamine maakt de bloedvaten wijder en doorlaatbaarder en zet klieren "
        "aan het werk. Vandaar het vocht, de zwelling en de jeuk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een anafylactische shock blijft beperkt tot de huid rond de prikplaats.",
        antwoord=False,
        uitleg="Een anafylactische shock treft het hele lichaam: de bloedvaten worden "
        "overal wijder, de bloeddruk valt en de luchtwegen vernauwen. Dat vraagt "
        "onmiddellijk adrenaline.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een auto-immuunziekte?",
        opties=[
            "de afweer valt eigen gezonde cellen aan",
            "de afweer reageert te hevig op stuifmeel",
            "de afweer wordt door een virus uitgeschakeld",
            "de afweer maakt geen enkel antilichaam meer",
        ],
        antwoord=0,
        uitleg="Bij een auto-immuunziekte leest het immuunsysteem eigen cellen als vreemd. "
        "Het onderscheid tussen eigen en vreemd is dan stuk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke aandoeningen zijn auto-immuunziekten? Kruis alles aan wat juist is.",
        opties=[
            "multiple sclerose",
            "de ziekte van Crohn",
            "een allergie voor pinda's",
            "een infectie met het griepvirus",
        ],
        antwoord=[0, 1],
        uitleg="Bij multiple sclerose valt de afweer de isolatielaag van de zenuwen aan, "
        "bij Crohn de darmwand. Psoriasis hoort er ook bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe wordt een auto-immuunziekte meestal behandeld?",
        opties=[
            "door de afweerreactie te onderdrukken",
            "door de afweerreactie juist te versterken",
            "door een vaccin tegen de eigen cellen",
            "door een bloedtransfusie van groep O",
        ],
        antwoord=0,
        uitleg="Met ontstekingsremmers of middelen die de afweer onderdrukken, wordt de "
        "aanval geremd. De keerzijde is meer kans op infecties.",
    ),
    dict(
        type="waarofniet",
        vraag="Een auto-immuunziekte kan meestal volledig genezen worden.",
        antwoord=False,
        uitleg="De meeste zijn chronisch: de behandeling houdt de klachten onder "
        "controle, maar de oorzaak blijft.",
    ),
    dict(
        type="invultekst",
        vraag="Welk soort virus is hiv, dat zijn RNA in DNA laat omzetten?",
        antwoord=["retrovirus", "een retrovirus"],
        uitleg="Een retrovirus draagt RNA en maakt met omgekeerde transcriptase een "
        "DNA-kopie, die in het DNA van de gastheercel wordt ingebouwd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke cel valt hiv aan?",
        opties=[
            "de T-helperlymfocyt",
            "de rode bloedcel",
            "de plasmacel",
            "de zenuwcel",
        ],
        antwoord=0,
        uitleg="Hiv dringt de T-helpercellen binnen. Omdat die de hele afweer aansturen, "
        "stort het systeem in als hun aantal daalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor de chronische fase van een hiv-infectie? Kruis alles aan wat juist is.",
        opties=[
            "er zijn jarenlang weinig of geen klachten",
            "het aantal T-helpercellen daalt traag",
            "er is meteen een zware longontsteking",
            "het virus verdwijnt helemaal uit het lichaam",
        ],
        antwoord=[0, 1],
        uitleg="Na een korte acute fase volgt een lange stille periode. Het virus blijft "
        "zich vermenigvuldigen en het aantal T-helpercellen daalt traag.",
    ),
    dict(
        type="waarofniet",
        vraag="Seropositief betekent dat er antilichamen tegen hiv in het bloed zitten.",
        antwoord=True,
        uitleg="Een test zoekt die antilichamen. Ze verschijnen pas enkele weken na de "
        "besmetting, dus kan een test in het begin nog negatief zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom sterft iemand met aids meestal aan een andere infectie?",
        opties=[
            "de afweer kan die infectie niet meer aan",
            "het hiv-virus valt zelf de longen aan",
            "de rode bloedcellen worden afgebroken",
            "het beenmerg maakt geen bloed meer aan",
        ],
        antwoord=0,
        uitleg="Zonder T-helpercellen krijgen verwekkers die een gezond lichaam makkelijk "
        "opruimt, vrij spel. Dat zijn de opportunistische infecties.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom bestaat er nog geen vaccin tegen hiv?",
        opties=[
            "het virus verandert voortdurend zijn oppervlak",
            "het virus heeft geen enkel antigeen",
            "het virus leeft buiten het lichaam verder",
            "het virus is te groot voor een antilichaam",
        ],
        antwoord=0,
        uitleg="Hiv muteert heel snel, dus past een antilichaam na een tijd niet meer. "
        "Daarbij schakelt het net de cellen uit die de afweer moeten aansturen.",
    ),
]

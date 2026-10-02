# -*- coding: utf-8 -*-
"""🌍 Beyond dubbele finaliteit — Vruchtbaarheid, anticonceptie en kinderwens.

Biologie, de onderkop "Vruchtbaarheid" van de kop "Voortplanting bij de mens"
uit de vakfiche natuurwetenschappen 3DU. Deel 1 gaat over de methoden om de
vruchtbaarheid te regelen: natuurlijk of kunstmatig, hormonaal of niet, hoe
betrouwbaar ze zijn en welke ook tegen soa's beschermen. Deel 2 gaat over
onvruchtbaarheid, de technieken om de vruchtbaarheid te stimuleren, en wat
leefgewoonten en omgevingsfactoren met de vruchtbaarheid doen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarop berust de kalendermethode?",
        opties=[
            "op het schatten van de vruchtbare dagen uit vorige cycli",
            "op het meten van de lichaamstemperatuur elke ochtend",
            "op het bekijken van het slijm van de baarmoederhals",
            "op het innemen van een hormoon elke dag",
        ],
        antwoord=0,
        uitleg="Je telt terug vanaf de verwachte menstruatie om te schatten wanneer de eisprong valt. Omdat de cyclus kan verschuiven, is dat een ruwe schatting en dus weinig betrouwbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke methoden zijn natuurlijk, dus zonder middel of ingreep? Er zijn er drie.",
        opties=[
            "de kalendermethode",
            "de temperatuurmethode",
            "de ovulatiemethode",
            "het koperspiraal",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie lezen alleen het lichaam af: de kalender, de ochtendtemperatuur en het slijm van de baarmoederhals. Een koperspiraal is een voorwerp dat in de baarmoeder geplaatst wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat merk je bij de temperatuurmethode?",
        opties=[
            "de temperatuur stijgt licht na de eisprong",
            "de temperatuur zakt scherp na de eisprong",
            "de temperatuur stijgt pas bij de menstruatie",
            "de temperatuur blijft de hele cyclus gelijk",
        ],
        antwoord=0,
        uitleg="Progesteron doet de basale lichaamstemperatuur met ongeveer een halve graad stijgen. Je ziet de eisprong dus pas nadat hij gebeurd is, en dat is meteen de zwakte van de methode.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de methode waarbij je het slijm van de baarmoederhals bekijkt om de eisprong te herkennen?",
        antwoord=["ovulatiemethode", "de ovulatiemethode", "billingsmethode"],
        uitleg="Rond de eisprong wordt het slijm helder en rekbaar, zodat zaadcellen er vlot door kunnen. Daarna wordt het weer dik en ondoordringbaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Coïtus interruptus is een betrouwbare methode om zwangerschap te voorkomen.",
        antwoord=False,
        uitleg="Nog vóór de zaadlozing komt er al vocht vrij waarin zaadcellen kunnen zitten. Daarom mislukt de methode vaak, en tegen soa's beschermt ze helemaal niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke anticonceptiemiddelen werken met hormonen? Er zijn er drie.",
        opties=[
            "de combinatiepil",
            "het hormoonstaafje",
            "de vaginale ring",
            "het pessarium of diafragma",
        ],
        antwoord=[0, 1, 2],
        uitleg="De pil, het staafje en de ring geven hormonen af die de eisprong tegenhouden. Een pessarium is een rubberen kapje dat de baarmoederhals mechanisch afsluit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe voorkomt de combinatiepil een zwangerschap?",
        opties=[
            "ze houdt de eisprong tegen",
            "ze doodt de zaadcellen in de schede",
            "ze sluit de eileiders af",
            "ze maakt de eicellen onvruchtbaar",
        ],
        antwoord=0,
        uitleg="De pil houdt oestrogeen en progesteron kunstmatig op peil. De hypofyse geeft dan geen LH-piek meer, en zonder LH-piek is er geen eisprong.",
    ),
    dict(
        type="invultekst",
        vraag="Welk metaal in een spiraaltje maakt zaadcellen onbeweeglijk, zonder hormonen?",
        antwoord=["koper", "het koper"],
        uitleg="Het koperspiraal geeft koperionen af die de zaadcellen verlammen en de baarmoederwand ongeschikt maken voor innesteling. Er komen dus geen hormonen aan te pas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke methoden beschermen ook tegen soa's? Er zijn er twee.",
        opties=[
            "het mannencondoom",
            "het vrouwencondoom",
            "de combinatiepil",
            "de hormoonspiraal",
        ],
        antwoord=[0, 1],
        uitleg="Alleen een condoom legt een echte barrière tussen de slijmvliezen. Hormonale middelen regelen enkel de vruchtbaarheid en houden geen enkele ziekteverwekker tegen.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie de pil neemt, heeft daarnaast geen enkele bescherming tegen soa's nodig.",
        antwoord=False,
        uitleg="De pil doet niets tegen soa's. Bij wisselende partners blijft een condoom nodig, naast de pil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke methode is het betrouwbaarst?",
        opties=[
            "sterilisatie",
            "de kalendermethode",
            "een zaaddodend middel alleen",
            "coïtus interruptus",
        ],
        antwoord=0,
        uitleg="Sterilisatie onderbreekt de zaadleiders of de eileiders en is zo goed als volledig betrouwbaar, maar ook zo goed als onomkeerbaar. De andere drie zijn juist de minst betrouwbare.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij een sterilisatie bij de man?",
        opties=[
            "de zaadleiders worden onderbroken",
            "de teelballen worden weggenomen",
            "de aanmaak van testosteron stopt",
            "de zaadcellen worden onvruchtbaar gemaakt",
        ],
        antwoord=0,
        uitleg="De zaadleiders worden doorgeknipt of afgebonden, zodat er geen zaadcellen meer in het sperma komen. De teelballen blijven gewoon werken, dus het hormoon en de zin veranderen niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zaaddodend middel gebruik je het best samen met een barrièremethode.",
        antwoord=True,
        uitleg="Op zichzelf laat zo'n middel te veel zaadcellen door. Samen met een pessarium of een condoom vult het de barrière aan, en dan stijgt de betrouwbaarheid.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de pil die je ná onbeschermd vrijen inneemt om een zwangerschap nog te voorkomen?",
        antwoord=["morning-afterpil", "noodanticonceptie", "de morning-afterpil"],
        uitleg="De morning-afterpil stelt de eisprong uit of verhindert hem. Hoe sneller je hem neemt, hoe beter hij werkt, en hij is bedoeld als noodoplossing en niet als gewone methode.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de minipil en de combinatiepil?",
        opties=[
            "de minipil bevat maar één soort hormoon",
            "de minipil bevat helemaal geen hormonen",
            "de minipil werkt alleen ná de eisprong",
            "de minipil neem je maar één keer per week",
        ],
        antwoord=0,
        uitleg="De minipil bevat alleen een progestageen, de combinatiepil ook een oestrogeen. Daardoor kan de minipil ook gebruikt worden door wie geen oestrogeen verdraagt, maar ze luistert nauwer qua uur.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hormoonstaafje in de arm werkt enkele jaren.",
        antwoord=True,
        uitleg="Het staafje zit onder de huid van de bovenarm en geeft jarenlang een kleine hoeveelheid hormoon af. Je hoeft er dus niet dagelijks aan te denken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke methoden zijn barrièremethoden, die de zaadcellen mechanisch tegenhouden? Er zijn er drie.",
        opties=[
            "het mannencondoom",
            "het vrouwencondoom",
            "het pessarium of diafragma",
            "de hormoonpleister",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een barrière is een wand tussen de zaadcellen en de eicel. De hormoonpleister doet iets heel anders: ze geeft hormonen af via de huid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de betrouwbaarheid in de praktijk vaak lager dan op papier?",
        opties=[
            "omdat een methode verkeerd of onregelmatig gebruikt wordt",
            "omdat de middelen na een jaar vanzelf uitgewerkt zijn",
            "omdat het lichaam na een tijd gewend raakt aan de hormonen",
            "omdat de cijfers alleen voor jonge mensen gelden",
        ],
        antwoord=0,
        uitleg="De cijfers bij perfect gebruik liggen altijd hoger dan die bij gewoon gebruik. Een vergeten pil of een verkeerd aangebracht condoom verklaart het verschil.",
    ),
    dict(
        type="waarofniet",
        vraag="Een prikpil werkt ongeveer drie maanden.",
        antwoord=True,
        uitleg="De prik wordt om de drie maanden gezet. Juist die lange werking maakt haar handig, maar ook moeilijk terug te draaien als je ze niet verdraagt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is anticonceptie een keuze die bij de persoon zelf past?",
        opties=[
            "omdat gezondheid, leeftijd en levensritme per persoon verschillen",
            "omdat elke methode voor iedereen even betrouwbaar is",
            "omdat alleen de prijs het verschil maakt",
            "omdat elke methode ook tegen soa's beschermt",
        ],
        antwoord=0,
        uitleg="Wie geen oestrogeen verdraagt, wie moeilijk aan een dagelijkse pil denkt of wie wisselende partners heeft, komt telkens bij een andere methode uit. Daarom bestaat er niet één beste keuze.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wanneer spreekt men van onvruchtbaarheid?",
        opties=[
            "als er na een jaar onbeschermd vrijen geen zwangerschap is",
            "als er na een maand onbeschermd vrijen geen zwangerschap is",
            "als er ooit een miskraam geweest is",
            "als de cyclus niet precies achtentwintig dagen duurt",
        ],
        antwoord=0,
        uitleg="De afspraak is een jaar regelmatig en onbeschermd vrijen zonder zwangerschap. Pas dan wordt er onderzoek gedaan, want ook bij vruchtbare koppels lukt het vaak niet meteen.",
    ),
    dict(
        type="waarofniet",
        vraag="Onvruchtbaarheid ligt ongeveer even vaak bij de man als bij de vrouw.",
        antwoord=True,
        uitleg="Ongeveer een derde van de gevallen ligt bij de man, een derde bij de vrouw en een derde bij beiden of bij geen van beiden duidelijk. Daarom worden altijd beide partners onderzocht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het doel van hormonale stimulatie bij een kinderwens?",
        opties=[
            "de eierstok aanzetten om eicellen te laten rijpen",
            "de baarmoederwand dikker maken dan gewoonlijk",
            "de zaadcellen in het labo sneller doen zwemmen",
            "de bevalling een paar weken vroeger op gang trekken",
        ],
        antwoord=0,
        uitleg="Met hormonen wordt de eierstok aangezet om een of meer follikels te laten rijpen. Dat is vaak de eerste stap, nog vóór er aan een techniek zoals IVF gedacht wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij kunstmatige inseminatie of KI?",
        opties=[
            "sperma wordt rechtstreeks in de baarmoeder gebracht",
            "een eicel wordt in het labo buiten het lichaam bevrucht",
            "één zaadcel wordt met een naald in een eicel geprikt",
            "een embryo van enkele dagen wordt teruggeplaatst",
        ],
        antwoord=0,
        uitleg="Bij KI wordt het sperma met een dun buisje in de baarmoeder gebracht, rond het moment van de eisprong. De bevruchting zelf gebeurt gewoon in het lichaam, in de eileider.",
    ),
    dict(
        type="invultekst",
        vraag="Waarvoor staat de afkorting IVF?",
        antwoord=["in vitro fertilisatie", "in-vitrofertilisatie", "in vitrofertilisatie"],
        uitleg="In vitro betekent in glas, fertilisatie betekent bevruchting. Eicel en zaadcellen worden dus buiten het lichaam samengebracht, in het labo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen IVF en ICSI?",
        opties=[
            "bij ICSI wordt één zaadcel in de eicel geprikt",
            "bij ICSI gebeurt alles in het lichaam zelf",
            "bij ICSI worden geen hormonen gebruikt",
            "bij ICSI wordt er geen embryo teruggeplaatst",
        ],
        antwoord=0,
        uitleg="Bij IVF liggen eicel en zaadcellen samen in een schaaltje en moet een zaadcel zelf binnenraken. Bij ICSI wordt één zaadcel met een naald ingebracht, wat helpt als het sperma te traag of te schaars is.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij IVF groeit de vrucht de hele zwangerschap in het labo.",
        antwoord=False,
        uitleg="Alleen de bevruchting en de eerste paar dagen gebeuren in het labo. Daarna wordt het embryo in de baarmoeder geplaatst en verloopt de zwangerschap gewoon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gewoonten verlagen de vruchtbaarheid bij man én vrouw? Er zijn er drie.",
        opties=[
            "roken",
            "veel alcohol drinken",
            "drugsgebruik",
            "elke dag matig bewegen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Roken, alcohol en drugs tasten zowel de aanmaak van zaadcellen als de cyclus aan. Matig bewegen werkt juist de andere kant op en helpt het gewicht op peil houden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom verlaagt de leeftijd van de vrouw de kans op zwangerschap?",
        opties=[
            "de voorraad eicellen daalt en hun kwaliteit neemt af",
            "de baarmoeder wordt stilaan te klein voor een vrucht",
            "de hypofyse stopt van de ene dag op de andere met FSH",
            "de eileiders groeien na verloop van tijd vanzelf dicht",
        ],
        antwoord=0,
        uitleg="Een meisje wordt geboren met haar hele voorraad eicellen. Die voorraad daalt levenslang, en vanaf ongeveer vijfendertig jaar neemt ook de kwaliteit duidelijk af.",
    ),
    dict(
        type="waarofniet",
        vraag="Alleen overgewicht kan de cyclus verstoren, ondergewicht niet.",
        antwoord=False,
        uitleg="Allebei kunnen ze dat. Vetweefsel speelt mee in de hormoonhuishouding, dus zowel te weinig als te veel vet brengt de cyclus uit balans en kan de eisprong doen uitblijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is warmte slecht voor de aanmaak van zaadcellen?",
        opties=[
            "zaadcellen rijpen het best net onder de lichaamstemperatuur",
            "warmte doet het sperma te snel indikken en stollen",
            "warmte jaagt de hoeveelheid testosteron veel te hoog op",
            "warmte sluit de zaadleiders een tijdlang volledig af",
        ],
        antwoord=0,
        uitleg="De teelballen hangen buiten de buikholte, want zaadcellen rijpen het best bij een paar graden onder de lichaamstemperatuur. Langdurige warmte, bijvoorbeeld van een laptop op de schoot, remt die rijping.",
    ),
    dict(
        type="invultekst",
        vraag="Welke behandeling tegen kanker kan de vruchtbaarheid blijvend aantasten?",
        antwoord=["chemotherapie", "bestraling", "radiotherapie"],
        uitleg="Chemotherapie en bestraling raken ook de snel delende cellen in de eierstok en de teelbal. Daarom wordt vooraf vaak voorgesteld om eicellen of sperma in te vriezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke invloeden van buitenaf kunnen de vruchtbaarheid aantasten? Er zijn er twee.",
        opties=[
            "zware metalen zoals lood en cadmium",
            "langdurige, zware stress",
            "voldoende slaap",
            "een gevarieerde voeding",
        ],
        antwoord=[0, 1],
        uitleg="Zware metalen en aanhoudende stress verstoren de hormoonhuishouding. Slaap en gevarieerde voeding doen net het omgekeerde en ondersteunen ze.",
    ),
    dict(
        type="waarofniet",
        vraag="Een soa die niet behandeld wordt, kan tot onvruchtbaarheid leiden.",
        antwoord=True,
        uitleg="Een infectie zoals chlamydia verloopt vaak zonder klachten en kan intussen de eileiders beschadigen of dichtmaken. Daarom zijn testen en snel behandelen belangrijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat onderzoekt men bij de man eerst als een zwangerschap uitblijft?",
        opties=[
            "het sperma, op aantal en beweeglijkheid",
            "de hoeveelheid oestrogeen in het bloed",
            "de dikte van het baarmoederslijmvlies",
            "de doorgankelijkheid van de eileiders",
        ],
        antwoord=0,
        uitleg="Een spermaonderzoek is eenvoudig en zegt meteen veel: hoeveel zaadcellen er zijn, hoe goed ze bewegen en hoe ze gebouwd zijn. De twee laatste onderzoeken horen bij de vrouw.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het moment waarop de eierstokken stoppen met werken en de menstruatie wegblijft?",
        antwoord=["menopauze", "de menopauze", "overgang"],
        uitleg="Rond de vijftig raakt de voorraad follikels op. De eisprong blijft weg, de hormonen zakken en de menstruatie stopt: de menopauze.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom worden er bij IVF vaak meerdere eicellen gehaald?",
        opties=[
            "omdat niet elke eicel bevrucht raakt of goed doorgroeit",
            "omdat er op die manier altijd een tweeling komt",
            "omdat een losse eicel helemaal niet bewaard kan worden",
            "omdat elke eicel maar één keer bekeken mag worden door het labo",
        ],
        antwoord=0,
        uitleg="Niet elke eicel laat zich bevruchten en niet elk embryo ontwikkelt goed. Met meerdere eicellen stijgt de kans dat er één geschikt embryo overblijft, en kunnen er ook ingevroren worden.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie met een kinderwens rookt, stopt het best pas als de zwangerschap er is.",
        antwoord=False,
        uitleg="Roken verlaagt de vruchtbaarheid zelf, bij man en vrouw. Stoppen vóór de zwangerschap helpt dus al, en vermijdt meteen de schade in de eerste, gevoeligste weken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het doel van eicellen of sperma invriezen?",
        opties=[
            "de vruchtbaarheid bewaren voor later",
            "de kans op een tweeling vergroten",
            "de bevruchting sneller laten verlopen",
            "het geslacht van het kind kiezen",
        ],
        antwoord=0,
        uitleg="Door in te vriezen bewaar je geslachtscellen van vandaag voor een later moment. Dat gebeurt vooral vóór een behandeling die de vruchtbaarheid kan aantasten.",
    ),
    dict(
        type="waarofniet",
        vraag="Hormonale stimulatie verhoogt de kans op een meerling.",
        antwoord=True,
        uitleg="Als er meer dan één follikel tegelijk rijpt, kunnen er ook meerdere eicellen bevrucht raken. Daarom wordt de stimulatie met echo's nauw opgevolgd.",
    ),
]

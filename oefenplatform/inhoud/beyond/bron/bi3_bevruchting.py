# -*- coding: utf-8 -*-
"""Bevruchting, embryo en foetus — 🌍 Beyond, biologie.

Deel 1 gaat over de weg van de zaadcel naar de eicel, de fasen van de
bevruchting, de klievingsdelingen, de innesteling en de vorming van de
kiemschijven. Deel 2 gaat over de placenta en de navelstreng, de fasen van de
geboorte, het opsporen van aandoeningen en de invloed van gezondheidsgedrag en
van besmettingen op embryo en foetus.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waar in het vrouwelijk voortplantingsstelsel gebeurt de bevruchting meestal?",
        opties=[
            "in de eileider",
            "in de baarmoeder",
            "in de eierstok",
            "in de baarmoederhals",
        ],
        antwoord=0,
        uitleg="De eicel wordt in het eerste derde van de eileider bevrucht. De bevruchte "
        "eicel reist daarna nog dagen naar de baarmoeder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke barrières moet een zaadcel overwinnen op weg naar de eicel? Kruis alles aan wat juist is.",
        opties=[
            "het zure milieu van de vagina",
            "de slijmprop van de baarmoederhals",
            "het baarmoederslijmvlies van de vorige cyclus",
            "de celwand van de eicel",
        ],
        antwoord=[0, 1],
        uitleg="De zuurtegraad, de slijmprop, de lengte van de weg en de afweercellen "
        "onderweg laten maar enkele honderden zaadcellen over. Een eicel heeft geen celwand.",
    ),
    dict(
        type="waarofniet",
        vraag="Een eicel is na de ovulatie ongeveer een dag bevruchtbaar.",
        antwoord=True,
        uitleg="De eicel leeft nog ongeveer 12 tot 24 uur. Zaadcellen houden het langer "
        "uit, drie tot vijf dagen, dus is de vruchtbare periode breder dan één dag.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het openbreken van het blaasje op de kop van de zaadcel?",
        antwoord=["acrosoomreactie", "de acrosoomreactie"],
        uitleg="Bij de acrosoomreactie komen de enzymen vrij die een weg banen door de "
        "corona radiata en de zona pellucida.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de corticale reactie in de eicel?",
        opties=[
            "beletten dat een tweede zaadcel binnendringt",
            "de eerste celdeling van de zygote starten",
            "de eicel naar de baarmoeder voeren",
            "het acrosoom van de zaadcel openen",
        ],
        antwoord=0,
        uitleg="De corticale granulen storten hun inhoud uit en vormen het "
        "bevruchtingsmembraan. Daardoor kan er geen tweede zaadcel meer in.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het samensmelten van de kern van de zaadcel met die van de eicel?",
        antwoord=["amfimixie", "de amfimixie"],
        uitleg="Bij de amfimixie komen de twee haploïde kernen samen. Vanaf dat moment is "
        "er één diploïde cel: de zygote.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een zygote?",
        opties=[
            "de bevruchte eicel met 46 chromosomen",
            "de onbevruchte eicel in de eileider",
            "het bolletje cellen dat zich innestelt",
            "het blaasje met enzymen op de zaadcel",
        ],
        antwoord=0,
        uitleg="De zygote is de eerste cel van het nieuwe organisme, diploïd en met de "
        "helft van het DNA van elke ouder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor de klievingsdelingen? Kruis alles aan wat juist is.",
        opties=[
            "de cellen delen zonder te groeien",
            "het geheel wordt niet groter",
            "elke cel wordt groter na elke deling",
            "er komt bij elke deling DNA bij",
        ],
        antwoord=[0, 1],
        uitleg="Het klompje blijft even groot en de cellen worden dus kleiner. Ze leven "
        "van de voorraad uit de eicel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het compacte bolletje cellen dat na enkele klievingsdelingen ontstaat?",
        antwoord=["morula", "de morula"],
        uitleg="Morula betekent moerbei, naar de vorm. Daarna vormt zich een holte en "
        "wordt het een blastula of blastocyst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk deel van de blastocyst wordt later het embryo?",
        opties=[
            "de embryoblast of kiemknop",
            "de trofoblast",
            "de blastulaholte",
            "de zona pellucida",
        ],
        antwoord=0,
        uitleg="De embryoblast of kiemknop is het klompje binnenin. De trofoblast is de "
        "buitenlaag en wordt het foetale deel van de placenta.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de trofoblast bij de innesteling?",
        opties=[
            "met enzymen in het slijmvlies binnendringen",
            "de eerste zenuwcellen van het embryo vormen",
            "de navelstreng van het embryo aanleggen",
            "het hart van het embryo laten kloppen",
        ],
        antwoord=0,
        uitleg="De trofoblast maakt lytische enzymen die het baarmoederslijmvlies "
        "openmaken. Zo graaft de blastocyst zich erin; dat is de innesteling.",
    ),
    dict(
        type="waarofniet",
        vraag="De innesteling gebeurt pas ongeveer een maand na de bevruchting.",
        antwoord=False,
        uitleg="De blastocyst reist eerst enkele dagen door de eileider. Al rond dag zes "
        "of zeven nestelt ze zich in het baarmoederslijmvlies in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke lagen vormt een driebladige kiemschijf?",
        opties=[
            "ectoderm, mesoderm en endoderm",
            "epiblast, trofoblast en morula",
            "amnion, chorion en placenta",
            "zona pellucida, corona radiata en glashuid",
        ],
        antwoord=0,
        uitleg="De gastrulatie maakt van twee bladen drie. Uit elk blad komen andere "
        "organen, en dat heet organogenese.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er uit het ectoderm?",
        opties=[
            "de huid en het zenuwstelsel",
            "de spieren en het skelet",
            "de darm en de longen",
            "de placenta en de navelstreng",
        ],
        antwoord=0,
        uitleg="Ecto betekent buiten: huid en zenuwstelsel. Mesoderm geeft spieren, bot "
        "en bloedvaten, endoderm het darmkanaal en de longen.",
    ),
    dict(
        type="invultekst",
        vraag="Welk kiemblad levert de spieren, het skelet en de bloedvaten?",
        antwoord=["mesoderm", "het mesoderm"],
        uitleg="Het mesoderm is het middelste blad. Meso betekent midden, en daar komen "
        "spieren, bot, bloed en nieren uit.",
    ),
    dict(
        type="waarofniet",
        vraag="Tijdens de gastrulatie verplaatsen cellen zich en ontstaat er een derde kiemblad.",
        antwoord=True,
        uitleg="Cellen schuiven naar binnen en vormen tussen de twee bestaande bladen het "
        "mesoderm. Daarmee ligt de bouwplan van het lichaam vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat beschermt het embryo tegen schokken?",
        opties=[
            "het vruchtwater in de amnionholte",
            "de zona pellucida rond de eicel",
            "de slijmprop van de baarmoederhals",
            "het bevruchtingsmembraan",
        ],
        antwoord=0,
        uitleg="Het amnionvlies houdt het vruchtwater vast. Dat water vangt schokken op "
        "en laat het kind vrij bewegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer spreekt men van een foetus in plaats van een embryo?",
        opties=[
            "vanaf ongeveer de negende week",
            "vanaf de innesteling",
            "vanaf de eerste klievingsdeling",
            "pas vanaf de geboorte",
        ],
        antwoord=0,
        uitleg="De eerste acht weken is het een embryo: dan worden de organen aangelegd. "
        "Daarna heet het een foetus en gaat het vooral om groei en afwerking.",
    ),
    dict(
        type="waarofniet",
        vraag="Het hart van een embryo begint pas in de derde maand te kloppen.",
        antwoord=False,
        uitleg="Het hart begint rond de derde of vierde week te kloppen, nog voor de "
        "moeder iets voelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn de eerste acht weken de gevoeligste periode van een zwangerschap?",
        opties=[
            "dan worden alle organen aangelegd",
            "dan is het kind het grootst",
            "dan werkt de placenta nog niet",
            "dan is er nog geen vruchtwater",
        ],
        antwoord=0,
        uitleg="Een stoornis tijdens de organogenese raakt de bouw van een orgaan zelf. "
        "Later gaat het vooral om groei, en is de schade meestal beperkter.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat doet de placenta? Kruis alles aan wat juist is.",
        opties=[
            "voedingsstoffen en zuurstof doorgeven",
            "afvalstoffen van het kind afvoeren",
            "het bloed van moeder en kind mengen",
            "het kind van vruchtwater voorzien",
        ],
        antwoord=[0, 1],
        uitleg="Stoffen gaan door de placentabarrière heen, maar de twee bloedsomlopen "
        "blijven gescheiden. De placenta maakt ook hormonen, onder meer progesteron.",
    ),
    dict(
        type="waarofniet",
        vraag="Het bloed van de moeder en dat van het kind komen in de placenta rechtstreeks samen.",
        antwoord=False,
        uitleg="Ze stromen langs elkaar, gescheiden door de placentabarrière. Stoffen "
        "wisselen door die barrière; bloedcellen blijven aan hun kant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel bloedvaten zitten er in een navelstreng?",
        opties=[
            "twee slagaders en één ader",
            "één slagader en één ader",
            "twee slagaders en twee aders",
            "drie aders en geen slagader",
        ],
        antwoord=0,
        uitleg="Twee navelstrengslagaders brengen zuurstofarm bloed naar de placenta, en "
        "één navelstrengader brengt zuurstofrijk bloed terug naar het kind.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de placenta in gewone taal?",
        antwoord=["moederkoek", "de moederkoek"],
        uitleg="De moederkoek bestaat uit een foetaal deel uit de trofoblast en een "
        "moederlijk deel uit het baarmoederslijmvlies.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke reeks geeft de fasen van de geboorte in de juiste orde?",
        opties=[
            "indaling, ontsluiting, uitdrijving, nageboorte",
            "ontsluiting, indaling, nageboorte, uitdrijving",
            "uitdrijving, indaling, ontsluiting, nageboorte",
            "nageboorte, ontsluiting, indaling, uitdrijving",
        ],
        antwoord=0,
        uitleg="Het kind daalt in, de baarmoederhals verstrijkt en opent, het kind wordt "
        "uitgedreven en daarna komt de placenta.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er tijdens de ontsluiting?",
        opties=[
            "de baarmoederhals opent zich",
            "het kind wordt naar buiten geduwd",
            "de placenta laat los van de wand",
            "het kind draait met zijn hoofd naar boven",
        ],
        antwoord=0,
        uitleg="De weeën laten de baarmoederhals verstrijken en opengaan tot ongeveer "
        "tien centimeter. Dat is de langste fase van een bevalling.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de laatste fase van de bevalling, waarin de placenta eruit komt?",
        antwoord=["nageboorte", "de nageboorte"],
        uitleg="De naweeën laten de placenta loskomen en uitdrijven. Blijft er een stukje "
        "achter, dan geeft dat bloedverlies en infectiegevaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Het breken van de vruchtvliezen betekent dat het vruchtwater wegvloeit.",
        antwoord=True,
        uitleg="Het amnionvlies scheurt en het vruchtwater loopt weg. Dat gebeurt meestal "
        "tijdens de ontsluiting, soms al ervoor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk onderzoek tijdens de zwangerschap gebruikt geluidsgolven?",
        opties=[
            "de echografie",
            "de vruchtwaterpunctie",
            "de vlokkentest",
            "de bloedtest op hCG",
        ],
        antwoord=0,
        uitleg="Een echografie werkt met ultrageluid en is niet invasief. Ze toont de "
        "bouw en de groei, maar niet de chromosomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderzoeken halen cellen van het kind weg en geven dus een klein risico? Kruis alles aan wat juist is.",
        opties=[
            "de vruchtwaterpunctie",
            "de vlokkentest",
            "de echografie",
            "het meten van de bloeddruk",
        ],
        antwoord=[0, 1],
        uitleg="Bij een punctie of een vlokkentest wordt met een naald materiaal "
        "weggenomen. Dat geeft een kleine kans op een miskraam, maar levert wel het "
        "karyogram.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een beperking van prenataal onderzoek?",
        opties=[
            "het vindt niet elke aandoening",
            "het kan de bloedgroep niet bepalen",
            "het werkt alleen na de geboorte",
            "het geeft nooit een uitslag",
        ],
        antwoord=0,
        uitleg="Een test zoekt naar bepaalde afwijkingen, niet naar alles. Daarbij bestaan "
        "er valse uitslagen, en een gevonden afwijking is meestal niet te behandelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een niet-invasieve prenatale test onderzoekt DNA van het kind dat in het bloed van de moeder zit.",
        antwoord=True,
        uitleg="Er circuleren kleine stukjes foetaal DNA in haar bloed. Een bloedstaal "
        "volstaat dus, zonder risico voor het kind.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een stof die een afwijking bij een embryo kan veroorzaken?",
        antwoord=["teratogeen", "teratogene stof", "een teratogeen"],
        uitleg="Een teratogene stof grijpt in op de ontwikkeling. Alcohol, bepaalde "
        "medicijnen en sommige zware metalen zijn voorbeelden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wordt een zwangere vrouw aangeraden foliumzuur te nemen?",
        opties=[
            "het verkleint de kans op een open rug",
            "het verhoogt het gewicht van het kind",
            "het beschermt tegen toxoplasmose",
            "het versnelt de bevalling",
        ],
        antwoord=0,
        uitleg="Foliumzuur is nodig bij het sluiten van de neurale buis, in de eerste "
        "weken. Daarom start men er het best al voor de zwangerschap mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen kan alcohol tijdens de zwangerschap hebben? Kruis alles aan wat juist is.",
        opties=[
            "een lager geboortegewicht",
            "een blijvende ontwikkelingsachterstand",
            "een hogere kans op een tweeling",
            "een snellere bevalling",
        ],
        antwoord=[0, 1],
        uitleg="Alcohol gaat vlot door de placenta en treft vooral de hersenen. Er is geen "
        "veilige ondergrens bekend, dus is helemaal niet drinken het advies.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is roken tijdens de zwangerschap schadelijk?",
        opties=[
            "het kind krijgt minder zuurstof",
            "het kind krijgt te veel ijzer binnen",
            "de placenta maakt dan geen hormonen",
            "het vruchtwater wordt dan te zout",
        ],
        antwoord=0,
        uitleg="Koolstofmonoxide bezet de hemoglobine en nicotine vernauwt de bloedvaten. "
        "Dat geeft een lager geboortegewicht en meer kans op vroeggeboorte.",
    ),
    dict(
        type="waarofniet",
        vraag="Een zwangere vrouw moet beter helemaal niet bewegen.",
        antwoord=False,
        uitleg="Matig bewegen is juist goed voor de bloeddruk, het gewicht en de bevalling. "
        "Alleen zware schokken en valrisico zijn af te raden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom mag een zwangere vrouw geen rauw vlees eten?",
        opties=[
            "om toxoplasmose te vermijden",
            "om rubella te vermijden",
            "om het zikavirus te vermijden",
            "om een te hoge bloeddruk te vermijden",
        ],
        antwoord=0,
        uitleg="De toxoplasmoseparasiet zit in rauw vlees en in kattenuitwerpselen. Bij "
        "een eerste besmetting tijdens de zwangerschap kan het kind schade oplopen.",
    ),
    dict(
        type="invultekst",
        vraag="Tegen welk virus, dat rode hond veroorzaakt, worden meisjes gevaccineerd om hun latere zwangerschap te beschermen?",
        antwoord=["rubella", "rubellavirus", "rodehondvirus"],
        uitleg="Een rubella-infectie in de eerste maanden kan doofheid, blindheid en "
        "hartafwijkingen geven. Vaccinatie voor de zwangerschap voorkomt dat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen uit onze omgeving kunnen via de placenta de ontwikkeling storen? Kruis alles aan wat juist is.",
        opties=[
            "zware metalen zoals lood",
            "hormoonverstorende stoffen",
            "vezels uit volkoren brood",
            "zuurstof uit de ingeademde lucht",
        ],
        antwoord=[0, 1],
        uitleg="Zware metalen, hormoonverstoorders, pesticiden en microplastics halen de "
        "placenta en kunnen de ontwikkeling raken. Vezels en zuurstof zijn gewone voeding "
        "en gewone ademhaling.",
    ),
]

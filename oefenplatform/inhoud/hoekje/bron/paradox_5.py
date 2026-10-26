# -*- coding: utf-8 -*-
"""🔭 Uitdagingshoek — Paradoxen en weetjes, deel 5: Gemini-reeks 4 van Kim, aangevuld.

Van de tien vragen uit Kims Gemini-reeks 4 (26 oktober 2026) stonden er drie
al in deel 1 tot 4: het schip van Theseus, het Monty Hall-probleem en de
paradox van Olbers. De zeven nieuwe (Banach-Tarski, uien, Mpemba, de
bootstrap-paradox, de raven van Hempel, Coriolis en Perkin) staan hier, met
dertien eigen vragen erbij. De typfouten uit Gemini ("beschreeft",
"zwavelzuur" bij de uien) zijn verbeterd.
"""

VAK = "Paradoxen en weetjes"
BESTAND = "paradoxen-en-weetjes.json"
TITEL = "Raadsels, raven en rare proefjes"
VOLGORDE = 5

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": "Volgens de stelling van Banach en Tarski kun je in de wiskunde een bol in stukjes knippen en die anders samenleggen. Wat krijg je dan?",
        "opties": [
            "Twee bollen die elk precies even groot zijn als de eerste",
            "Eén bol die precies half zo groot is als de eerste bol",
            "Een kubus met exact dezelfde inhoud als de oude bol",
            "Een bol met een gat erin dat je nooit meer dicht krijgt",
        ],
        "antwoord": 0,
        "uitleg": r"Het klinkt als toveren, en in de echte wereld lukt het ook niet: de stukjes zijn zo oneindig grillig dat je ze met geen mes kunt snijden, en ze hebben zelfs geen inhoud die je kunt meten. Op papier, met oneindig veel punten, klopt het wel. De Poolse wiskundigen Stefan Banach en Alfred Tarski bewezen het in \(1924\). Het toont vooral hoe raar oneindigheid zich gedraagt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom krijg je tranen in je ogen als je een ui snijdt?",
        "opties": [
            "Door het snijden komt een zwavelhoudend gas vrij dat je ogen prikkelt",
            "De ui bevat fijne pepertjes die bij het snijden de lucht in stuiven",
            "De sterke geur laat je hersenen denken dat je verdrietig bent",
            "De ui geeft koude damp af die je ogen in een paar tellen uitdroogt",
        ],
        "antwoord": 0,
        "uitleg": "Zolang de ui heel is, zitten twee stoffen netjes apart in de cellen. Snijd je ze kapot, dan komen ze samen en maken ze een vluchtig gas met zwavel erin. Dat bereikt je ogen, en die spoelen het weg met tranen. Het is de verdediging van de ui tegen dieren die hem willen opeten. Een koude ui en een scherp mes helpen: minder kapotte cellen, minder gas.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is het Mpemba-effect, genoemd naar een scholier uit Tanzania?",
        "opties": [
            "Warm water kan soms sneller bevriezen dan koud water",
            "Koud water komt in dezelfde pot sneller aan de kook",
            "Zout water bevriest sneller dan gewoon kraantjeswater",
            "IJsblokjes smelten in de ruimte veel sneller dan hier",
        ],
        "antwoord": 0,
        "uitleg": r"In \(1963\) merkte Erasto Mpemba bij het maken van ijsjes dat zijn warme mengsel eerder bevroor dan dat van zijn klasgenoten. Zijn leraar lachte hem uit, maar een professor deed de proef na en schreef er samen met hem over. Wetenschappers zijn het vandaag nog steeds niet eens wanneer en waarom het gebeurt: verdamping, opgeloste lucht en het vriesvak zelf spelen allemaal mee. Zout water bevriest trouwens net trager, daarom strooit men zout in de winter.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een tijdreiziger geeft de jonge Shakespeare een boek met al zijn toneelstukken, die Shakespeare dan overschrijft en uitbrengt. Wat is daar zo vreemd aan?",
        "opties": [
            "Niemand heeft die toneelstukken ooit echt zelf bedacht",
            "Shakespeare zou dan twee keer tegelijk op aarde bestaan",
            "De tijdreiziger zou zo zijn eigen geboorte verhinderen",
            "Het boek zou dan jonger zijn dan het papier waarop het staat",
        ],
        "antwoord": 0,
        "uitleg": "Het boek komt uit de toekomst, waar het gedrukt werd naar het werk van Shakespeare, die het zelf uit het boek had. De tekst draait in een kringetje zonder begin: dat heet de bootstrap-paradox, naar de baron van Münchhausen die zichzelf aan zijn eigen laarzen uit het moeras zou trekken. Het is iets anders dan de grootvaderparadox, waar je je eigen bestaan onmogelijk maakt.",
    },
    {
        "type": "meerkeuze",
        "vraag": "De zin alle raven zijn zwart betekent logisch hetzelfde als: alles wat niet zwart is, is geen raaf. Wat volgt daar vreemd genoeg uit?",
        "opties": [
            "Een witte schoen zou een bewijsje zijn dat alle raven zwart zijn",
            "Een zwarte kat zou bewijzen dat er toch ook witte raven bestaan",
            "Een zwarte raaf zou dan niets meer zeggen over de andere raven",
            "Een witte raaf zou dan mogen bestaan zonder de zin te breken",
        ],
        "antwoord": 0,
        "uitleg": "Dit is de ravenparadox van de Duitse filosoof Carl Hempel. Elke zwarte raaf steunt de zin een klein beetje. Maar dan steunt elk niet-zwart ding dat geen raaf is, ook de tweede zin, en die betekent hetzelfde. Een witte schoen in je kast bewijst dus iets over raven. Veel denkers zeggen: ja, maar zo weinig dat het niet telt, want er zijn veel meer niet-zwarte dingen dan raven.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Orkanen draaien op het noordelijk halfrond tegen de klok in en op het zuidelijk halfrond met de klok mee. Waarom?",
        "opties": [
            "De draaiing van de aarde buigt bewegende lucht af, aan elke kant anders",
            "De zon staat op het zuidelijk halfrond aan de andere kant van de hemel",
            "De oceanen stromen op beide halfronden in een vaste, andere richting",
            "Het magneetveld van de aarde trekt de wolken in een kring rond de pool",
        ],
        "antwoord": 0,
        "uitleg": "Aan de evenaar draait de grond veel sneller mee dan bij de polen. Lucht die naar het noorden of zuiden stroomt, neemt haar oude snelheid mee en buigt daardoor af: het Corioliseffect. Bij een orkaan stroomt lucht van alle kanten naar het midden en gaat ze zo draaien. Voor een lavabo of een wc is het effect veel te klein: daar bepalen de vorm van de kom en hoe het water erin kwam welke kant het op draait.",
    },
    {
        "type": "meerkeuze",
        "vraag": r"In \(1856\) zocht de achttienjarige William Perkin een geneesmiddel tegen malaria. Wat vond hij per ongeluk?",
        "opties": [
            "De eerste kunstmatige kleurstof, een felle paarse",
            "Het eerste antibioticum, dat later penicilline heette",
            "De eerste kunststof, waar later bakeliet uit groeide",
            "Het eerste verdovingsmiddel voor bij de tandarts",
        ],
        "antwoord": 0,
        "uitleg": "Perkin probeerde kinine na te maken uit steenkoolteer, en hield een zwart goedje over. Toen hij het met alcohol oploste, werd het prachtig paars. Paars was tot dan de duurste kleur die er bestond, gemaakt uit duizenden zeeslakken. Perkin opende een fabriek, koningin Victoria droeg zijn mauve, en de chemische industrie was geboren. Penicilline kwam pas in 1928, en bakeliet in 1907.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Twee bewakers staan bij twee deuren: één naar de vrijheid, één naar de kerker. De ene liegt altijd, de andere spreekt altijd de waarheid, maar je weet niet wie wie is. Je mag één vraag stellen aan één bewaker. Welke vraag helpt?",
        "opties": [
            "Welke deur zou de andere bewaker aanwijzen? En dan neem je de andere deur",
            "Ben jij de bewaker die altijd liegt? En dan neem je de deur achter hem",
            "Welke deur leidt naar de vrijheid? En dan neem je precies die deur",
            "Is twee plus twee vier? En dan neem je de deur rechts als hij ja zegt",
        ],
        "antwoord": 0,
        "uitleg": "Vraag je het aan de eerlijke, dan vertelt hij eerlijk wat de leugenaar zou zeggen: de verkeerde deur. Vraag je het aan de leugenaar, dan liegt hij over wat de eerlijke zou zeggen: ook de verkeerde deur. Hoe dan ook wijst het antwoord dus naar de kerker, en neem je de andere. Op de vraag of iemand de leugenaar is, zeggen ze trouwens allebei nee.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat was er eerst: de kip of het ei?",
        "opties": [
            "Het ei, want er legden al dieren eieren lang voor er kippen waren",
            "De kip, want zonder kip kan er nooit een ei gelegd worden",
            "Allebei tegelijk, want het ene kan niet bestaan zonder het andere",
            "Niemand weet het, want van eieren bestaan er geen fossielen",
        ],
        "antwoord": 0,
        "uitleg": "Dinosaurussen, vissen en reptielen legden al honderden miljoenen jaren eieren voor er ook maar één kip rondliep. Er zijn zelfs fossiele dinosauruseieren gevonden, met babydino's erin. En wil je het per se over een kippenei: de eerste echte kip kwam uit een ei dat gelegd werd door een vogel die nog net geen kip was.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoeveel weegt een gewone stapelwolk van een kilometer breed, hoog en diep?",
        "opties": [
            "Honderden tonnen, zoveel als een kudde van honderd olifanten",
            "Bijna niets, hooguit een paar kilo aan waterdamp en lucht",
            "Ongeveer zoveel als één gewone gezinsauto, zo'n anderhalve ton",
            "Helemaal niets, want wolken hebben geen enkel gewicht",
        ],
        "antwoord": 0,
        "uitleg": r"In zo'n wolk zweven ontelbare piepkleine waterdruppeltjes, samen ruwweg een half miljoen kilo. Ze vallen niet naar beneden omdat ze zo klein zijn dat de opstijgende warme lucht ze makkelijk draagt, zoals stof in een zonnestraal. Pas als druppeltjes samenklitten tot grotere druppels, wordt het regen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een mier valt van een hoge flat en wandelt beneden gewoon verder. Hoe komt dat?",
        "opties": [
            "Ze is zo licht voor haar oppervlak dat de lucht haar val sterk afremt",
            "Ze heeft een hard pantser dat elke klap volledig voor haar opvangt",
            "Lichte dingen worden door de aarde minder hard aangetrokken",
            "Ze zweeft mee op de warme lucht die langs de gevel opstijgt",
        ],
        "antwoord": 0,
        "uitleg": "Wordt een dier twee keer zo groot, dan wordt zijn huid vier keer zo groot, maar zijn gewicht acht keer zo zwaar. Kleine dieren hebben dus heel veel oppervlak voor heel weinig gewicht, en de lucht remt ze af tot een rustig tempo. Een mier valt nooit veel sneller dan een kilometer of zes per uur. Zonder lucht zou ze wel even snel vallen als een olifant: de zwaartekracht trekt aan alles op dezelfde manier.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je hebt een gekookt en een rauw ei, en je laat ze allebei tollen op tafel. Hoe weet je welk het gekookte is?",
        "opties": [
            "Het gekookte tolt vlot door, in het rauwe klotst het vocht en remt af",
            "Het rauwe tolt vlot door, in het gekookte zit de dooier scheef en remt af",
            "Het gekookte is zwaarder, dus dat tolt altijd een stuk langzamer",
            "Het rauwe tolt de andere kant op, door de luchtbel die erin zit",
        ],
        "antwoord": 0,
        "uitleg": "Een gekookt ei is vanbinnen vast en draait als één geheel. In een rauw ei moet het vloeibare binnenwerk telkens mee op gang komen, en dat werkt als een rem. Leg je vinger heel even op een tollend rauw ei en laat los, dan begint het zelfs opnieuw te draaien: het vocht binnenin draaide gewoon door.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je kijkt een halve minuut naar een rode vlek en daarna naar een witte muur. Je ziet dan een groenblauwe vlek. Waarom?",
        "opties": [
            "De cellen die rood zien raken moe, dus de andere kleuren winnen even",
            "Je oog maakt zelf groen licht aan om het rode weer op te heffen",
            "De muur weerkaatst het tegenovergestelde van rood naar je oog",
            "Je hersenen keren een beeld dat blijft hangen om naar de tegenkleur",
        ],
        "antwoord": 0,
        "uitleg": "In je netvlies zitten cellen voor rood, groen en blauw. Kijk je lang naar rood, dan raken de roodcellen even uitgeput. Wit licht bevat alle kleuren, maar nu reageren vooral de groen- en blauwcellen: je ziet een naschaduw in de tegenkleur. Na een paar tellen zijn de roodcellen bijgekomen en verdwijnt de vlek.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je hebt honderd kilo aardappelen die voor negenennegentig procent uit water bestaan. Je laat ze wat drogen, tot er nog achtennegentig procent water in zit. Hoeveel wegen ze nu?",
        "opties": [
            r"\(50\) kilo",
            r"\(98\) kilo",
            r"\(99\) kilo",
            r"\(90\) kilo",
        ],
        "antwoord": 0,
        "uitleg": r"Eerst is er \(1\) kilo droge stof en \(99\) kilo water. Die ene kilo droge stof blijft. Als het water nog \(98\) procent is, dan is die kilo droge stof \(2\) procent van het geheel. En \(1\) kilo is \(2\) procent van \(50\) kilo. Eén procentje minder water, en de helft van het gewicht is weg. Dit heet de aardappelparadox.",
    },
    {
        "type": "waarofniet",
        "vraag": "Haaien zwommen al in de zee voor er ook maar één boom op aarde groeide.",
        "antwoord": True,
        "uitleg": "De oudste haaiensporen zijn zo'n vierhonderdvijftig miljoen jaar oud. De eerste echte bomen verschenen pas ongeveer vijftig miljoen jaar later. Haaien hebben dus ook alle massa-uitstervingen overleefd, ook die van de dinosaurussen.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een goudvis onthoudt iets maar drie seconden lang.",
        "antwoord": False,
        "uitleg": "Proeven tonen dat goudvissen dingen maanden kunnen onthouden. Ze leren dat er eten komt bij een bepaald geluid, op een bepaald uur of in een bepaalde hoek van de kom. Sommige leren zelfs een hendeltje duwen voor eten. Het verhaal van drie seconden is een fabeltje.",
    },
    {
        "type": "waarofniet",
        "vraag": "De bliksem slaat nooit twee keer op dezelfde plek in.",
        "antwoord": False,
        "uitleg": "De bliksem zoekt de makkelijkste weg naar de grond, en een hoge toren blijft dat bij elk onweer. Het Empire State Building in New York wordt elk jaar zo'n twintig keer geraakt. Daarom hebben hoge gebouwen een bliksemafleider: die vangt de inslag op en leidt de stroom veilig de grond in.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een bananenplant is eigenlijk geen boom, maar een reusachtig kruid.",
        "antwoord": True,
        "uitleg": "Een bananenplant heeft geen houten stam. Wat op een stam lijkt, zijn opgerolde bladstelen die strak om elkaar heen zitten. Zodra ze vruchten gedragen heeft, sterft die bovengrondse plant af en groeit er uit de wortelstok een nieuwe. Daarmee is ze een van de grootste kruiden ter wereld.",
    },
    {
        "type": "invultekst",
        "vraag": "Hoeveel mensen moet je minstens samenbrengen om zeker te zijn dat er twee op dezelfde dag verjaren? Tel 29 februari mee als mogelijke verjaardag.",
        "antwoord": "367",
        "uitleg": r"Een jaar heeft met schrikkeldag \(366\) mogelijke verjaardagen. Met \(366\) mensen kan het in het slechtste geval nog net dat iedereen een andere dag heeft. De \(367\)ste moet dan wel een dag delen. Dat heet het duivenhokprincipe: meer duiven dan hokjes, dan zitten er ergens twee samen. Voor een kans van één op twee volstaan er al \(23\), maar voor zekerheid heb je er \(367\) nodig.",
    },
    {
        "type": "invultekst",
        "vraag": "Een slak zit onderaan een put van tien meter diep. Elke dag kruipt ze drie meter omhoog, en elke nacht glijdt ze twee meter terug. Op de hoeveelste dag bereikt ze de rand?",
        "antwoord": ["8", "achtste", "8ste", "de achtste"],
        "uitleg": r"Na elke volle dag en nacht staat ze één meter hoger. Na zeven dagen en nachten zit ze dus op zeven meter. Op de achtste dag kruipt ze drie meter en haalt ze de tien meter, nog vóór ze 's nachts kan terugglijden. Wie snel rekent, zegt tien, maar de laatste dag telt anders dan de andere.",
    },
]

# -*- coding: utf-8 -*-
"""De vragen voor "Voortplanting" (✨ Spark, natuurwetenschappen).

Uit de vakfiche, deel biologie, "Voortplantingswijzen van planten en dieren" en
"Verloop van de voortplanting bij de mens": het verschil tussen aseksuele en
seksuele voortplanting met hun voor- en nadelen, de onderdelen van de bloem, de
onderdelen en de functie van het mannelijke en het vrouwelijke
voortplantingsstelsel, de fasen van de voortplanting in de juiste volgorde, de
menstruatiecyclus, de primaire en secundaire geslachtskenmerken en de
voorbehoedsmiddelen, ook als bescherming tegen soa's.

Deel 1 gaat over planten en dieren en over de onderdelen bij de mens. Deel 2
gaat over het verloop: de cyclus, de fasen, de hormonen en de bescherming.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen aseksuele en seksuele voortplanting?",
        opties=[
            "Bij aseksuele voortplanting is er maar één ouder, bij seksuele zijn er twee geslachtscellen nodig",
            "Bij aseksuele voortplanting zijn er altijd twee ouders",
            "Er is geen verschil, het zijn twee woorden voor hetzelfde",
        ],
        antwoord=0,
        uitleg="Aseksueel of ongeslachtelijk: één ouder maakt een kopie van zichzelf. Seksueel of geslachtelijk: een eicel en een zaadcel versmelten, dus er komt erfelijk materiaal van twee kanten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn vormen van aseksuele voortplanting bij planten?",
        opties=["Stekken", "Uitlopers", "Bestuiving door een bij", "Zaadjes zaaien"],
        antwoord=[0, 1],
        uitleg="Stekken, enten, oculeren, scheuren, uitlopers, bollen en knollen zijn ongeslachtelijk: er komt geen zaadcel aan te pas. Bestuiving en zaad horen bij de seksuele voortplanting.",
    ),
    dict(
        type="invultekst",
        vraag="Een stukje van een plant afsnijden en het laten wortelen, heet ___.",
        antwoord="stekken",
        uitleg="Bij stekken groeit er uit een stukje stengel of blad een volledige nieuwe plant. Die is erfelijk identiek aan de moederplant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gist plant zich voort door knopvorming. Wat gebeurt er dan?",
        opties=[
            "Er groeit een uitstulping aan de cel die loskomt als een nieuw individu",
            "Twee gistcellen versmelten",
            "De gist legt eitjes",
        ],
        antwoord=0,
        uitleg="Bij knopvorming ontstaat er een knopje aan de ouder dat uitgroeit en loslaat. Het is aseksueel: het nieuwe individu heeft hetzelfde erfelijk materiaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk deel van de bloem is het mannelijke deel?",
        opties=["De meeldraad", "De stamper", "Het vruchtbeginsel"],
        antwoord=0,
        uitleg="De meeldraad bestaat uit een helmdraad met bovenaan een helmknop, waarin het stuifmeel zit. De stamper is het vrouwelijke deel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit welke onderdelen bestaat de stamper?",
        opties=["De stempel", "De stijl", "Het vruchtbeginsel", "De helmknop"],
        antwoord=[0, 1, 2],
        uitleg="De stamper heeft bovenaan een kleverige stempel, daaronder de stijl en onderaan het vruchtbeginsel met de zaadbeginsels. De helmknop hoort bij de meeldraad.",
    ),
    dict(
        type="invultekst",
        vraag="Stuifmeel dat op de stempel van een bloem terechtkomt: dat noem je ___.",
        antwoord="bestuiving",
        uitleg="Bestuiving gebeurt door de wind of door insecten. Pas daarna kan de bevruchting volgen, als de zaadcel bij de eicel in het zaadbeginsel raakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is bevruchting?",
        opties=[
            "Het versmelten van een zaadcel en een eicel",
            "Het vervoeren van stuifmeel",
            "Het openen van een bloem",
        ],
        antwoord=0,
        uitleg="Bij de bevruchting versmelten de twee geslachtscellen tot één bevruchte eicel. Daaruit groeit bij een plant een zaadje met een kiemplantje erin.",
    ),
    dict(
        type="waarofniet",
        vraag="Een eicel en een zaadcel zijn allebei geslachtscellen.",
        antwoord=True,
        uitleg="Geslachtscellen of voortplantingscellen zijn de enige cellen die bij een bevruchting versmelten. Bij dieren en de mens heten ze eicel en zaadcel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar worden bij de man zaadcellen gemaakt?",
        opties=["In de teelballen", "In de prostaat", "In de zaadblaasjes"],
        antwoord=0,
        uitleg="De teelballen maken de zaadcellen. Ze rijpen verder in de bijballen; de prostaat en de zaadblaasjes maken het vocht waarin de zaadcellen zwemmen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderdelen horen bij het vrouwelijke voortplantingsstelsel?",
        opties=["De eierstokken", "De eileiders", "De baarmoeder", "De zaadleiders"],
        antwoord=[0, 1, 2],
        uitleg="Eierstokken, eileiders met hun eitrechters, baarmoeder, baarmoederhals, vagina, clitoris en schaamlippen. De zaadleiders horen bij het mannelijke stelsel.",
    ),
    dict(
        type="invultekst",
        vraag="De eicellen van een vrouw rijpen in de ___.",
        antwoord="eierstokken",
        uitleg="In de twee eierstokken rijpt er telkens één eicel per cyclus. Bij de eisprong komt die vrij en wordt ze door de eitrechter opgevangen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar groeit een baby tijdens de zwangerschap?",
        opties=["In de baarmoeder", "In de eileider", "In de eierstok"],
        antwoord=0,
        uitleg="Na de bevruchting in de eileider reist de bevruchte eicel naar de baarmoeder en nestelt zich in het baarmoederslijmvlies. Daar groeit ze uit tot embryo, foetus en baby.",
    ),
    dict(
        type="waarofniet",
        vraag="Sperma is het vocht waarin zaadcellen zitten.",
        antwoord=True,
        uitleg="Sperma is een mengsel van zaadcellen en vocht van de prostaat en de zaadblaasjes. Dat vocht voedt en beschermt de zaadcellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn primaire geslachtskenmerken?",
        opties=[
            "De geslachtsorganen waarmee je geboren wordt",
            "De kenmerken die in de puberteit verschijnen",
            "De kleur van je haar",
        ],
        antwoord=0,
        uitleg="Primaire geslachtskenmerken zijn de voortplantingsorganen zelf. Secundaire geslachtskenmerken, zoals een zwaardere stem of borstontwikkeling, komen er in de puberteit bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn secundaire geslachtskenmerken?",
        opties=["Schaamhaar", "Een zwaardere stem", "De teelballen", "De eierstokken"],
        antwoord=[0, 1],
        uitleg="Schaamhaar, een zwaardere stem, bredere heupen en borstontwikkeling komen in de puberteit door de geslachtshormonen. Teelballen en eierstokken zijn primaire kenmerken.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij maagdelijke voortplanting groeit er uit een onbevruchte eicel toch een nieuw individu.",
        antwoord=True,
        uitleg="Sommige dieren, zoals bladluizen en bepaalde hagedissen, doen dat. Het is een vorm van aseksuele voortplanting: er komt geen zaadcel aan te pas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is enten bij planten?",
        opties=[
            "Een deel van de ene plant op de stam van een andere laten vergroeien",
            "Een plant in twee stukken scheuren",
            "Zaad van twee planten mengen",
        ],
        antwoord=0,
        uitleg="Bij enten zet je een twijg van een goede soort op de wortelstam van een andere. Fruittelers doen dat om elk jaar dezelfde appels te oogsten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat groeit er uit een zaadje?",
        opties=["Een kiemplant", "Een bloem zonder stengel", "Een knol"],
        antwoord=0,
        uitleg="In het zaadje zit een kiemplantje met een voorraad voedsel. Bij genoeg water en warmte kiemt het en groeit het uit tot een nieuwe plant.",
    ),
    dict(
        type="invultekst",
        vraag="Een tulp plant zich ongeslachtelijk voort met een ___ onder de grond.",
        antwoord="bol",
        uitleg="Een bol is een ondergrondse voorraadkast waaruit elk jaar een nieuwe plant groeit. Aardappelen doen hetzelfde met knollen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Zet de fasen in de juiste volgorde: bevruchting, eisprong, innesteling, geboorte.",
        opties=[
            "eisprong – bevruchting – innesteling – geboorte",
            "bevruchting – eisprong – innesteling – geboorte",
            "eisprong – innesteling – bevruchting – geboorte",
        ],
        antwoord=0,
        uitleg="Eerst komt de eicel vrij (eisprong), dan versmelt ze met een zaadcel in de eileider (bevruchting), dan nestelt ze zich in de baarmoeder (innesteling), en na ongeveer negen maanden volgt de geboorte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoelang duurt een menstruatiecyclus gemiddeld?",
        opties=["Ongeveer 28 dagen", "Ongeveer 7 dagen", "Ongeveer 90 dagen"],
        antwoord=0,
        uitleg="Gemiddeld 28 dagen, maar tussen 21 en 35 dagen is normaal. De eerste dag van de menstruatie is dag 1 van de cyclus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij de eisprong?",
        opties=[
            "Een rijpe eicel komt vrij uit de eierstok",
            "Het baarmoederslijmvlies wordt afgestoten",
            "Er worden zaadcellen gemaakt",
        ],
        antwoord=0,
        uitleg="De eisprong valt ongeveer halverwege de cyclus, rond dag 14. De eicel wordt opgevangen door de eitrechter en kan daar ongeveer een dag bevrucht worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gebeurtenissen horen bij een menstruatiecyclus?",
        opties=[
            "De eicelrijping",
            "De verdikking van het baarmoederslijmvlies",
            "De eisprong",
            "De geboorte",
        ],
        antwoord=[0, 1, 2],
        uitleg="Rijpen van een eicel, verdikken van het slijmvlies, eisprong en, als er geen bevruchting is, de menstruatie. De geboorte hoort bij een zwangerschap, niet bij de cyclus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom verdikt het baarmoederslijmvlies elke cyclus?",
        opties=[
            "Om een bevruchte eicel te kunnen opvangen",
            "Om de eicel te laten rijpen",
            "Om zaadcellen te maken",
        ],
        antwoord=0,
        uitleg="Een dik, goed doorbloed slijmvlies is nodig voor de innesteling. Komt er geen bevruchte eicel, dan wordt het afgestoten: dat is de menstruatie.",
    ),
    dict(
        type="invultekst",
        vraag="Het afstoten van het baarmoederslijmvlies heet de ___.",
        antwoord="menstruatie",
        uitleg="De menstruatie duurt meestal drie tot zeven dagen en is meteen het begin van een nieuwe cyclus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke hormonen spelen een rol bij de voortplanting?",
        opties=["Oestrogeen", "Progesteron", "Testosteron", "Insuline"],
        antwoord=[0, 1, 2],
        uitleg="Oestrogeen en progesteron sturen de cyclus en de zwangerschap; testosteron stuurt de mannelijke ontwikkeling. Insuline regelt de suiker in je bloed en heeft er niets mee te maken.",
    ),
    dict(
        type="waarofniet",
        vraag="De vruchtbare periode is de periode rond de eisprong.",
        antwoord=True,
        uitleg="Zaadcellen kunnen enkele dagen overleven en de eicel ongeveer één dag. De vruchtbare periode loopt dus van een paar dagen vóór tot een dag na de eisprong.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zet de ontwikkeling in de juiste volgorde: baby, embryo, bevruchte eicel, foetus.",
        opties=[
            "bevruchte eicel – embryo – foetus – baby",
            "embryo – bevruchte eicel – foetus – baby",
            "bevruchte eicel – foetus – embryo – baby",
        ],
        antwoord=0,
        uitleg="De bevruchte eicel deelt zich tot een embryo. Vanaf ongeveer acht weken spreken we van een foetus, en bij de geboorte van een baby.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voorbehoedsmiddel beschermt óók tegen soa's?",
        opties=["Het condoom", "De anticonceptiepil", "Het koperspiraaltje"],
        antwoord=0,
        uitleg="Alleen een condoom of een vrouwencondoom houdt lichaamsvochten tegen en beschermt zo tegen soa's. Hormonale middelen en spiraaltjes voorkomen enkel een zwangerschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn hormonale voorbehoedsmiddelen?",
        opties=[
            "De anticonceptiepil",
            "De vaginale ring",
            "Het hormonenstaafje",
            "Het condoom",
        ],
        antwoord=[0, 1, 2],
        uitleg="De pil, de pleister, de ring, de prikpil, het staafje en het hormonenspiraaltje werken met hormonen. Het condoom en het koperspiraaltje niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe zorgt de anticonceptiepil ervoor dat er geen zwangerschap komt?",
        opties=[
            "De hormonen in de pil houden de eisprong tegen",
            "De pil doodt de zaadcellen in de baarmoeder",
            "De pil sluit de eileiders af",
        ],
        antwoord=0,
        uitleg="Zonder eisprong is er geen eicel om te bevruchten. De hormonen maken ook het slijm in de baarmoederhals dikker, zodat zaadcellen moeilijker passeren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een condoom is maar één keer te gebruiken.",
        antwoord=True,
        uitleg="Een condoom gebruik je één keer en gooi je daarna weg. Hergebruik maakt het onbetrouwbaar, zowel tegen zwangerschap als tegen soa's.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een voordeel van seksuele voortplanting?",
        opties=[
            "De nakomelingen verschillen van elkaar, dus de soort past zich makkelijker aan",
            "Er is maar één ouder nodig",
            "Het gaat veel sneller dan aseksuele voortplanting",
        ],
        antwoord=0,
        uitleg="Erfelijk materiaal van twee ouders geeft variatie. Verandert de omgeving of komt er een ziekte, dan is er meer kans dat sommige nakomelingen het overleven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn voordelen van aseksuele voortplanting?",
        opties=[
            "Je hebt geen partner nodig",
            "Het gaat snel en er komen veel nakomelingen",
            "De nakomelingen verschillen sterk van elkaar",
            "De soort past zich beter aan een nieuwe ziekte aan",
        ],
        antwoord=[0, 1],
        uitleg="Zonder partner en snel: dat is het voordeel. Het nadeel is net dat alle nakomelingen identiek zijn, dus één ziekte kan ze allemaal treffen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een plant die door stekken ontstaat, is erfelijk identiek aan de moederplant.",
        antwoord=True,
        uitleg="Bij aseksuele voortplanting is er geen versmelting van geslachtscellen, dus het erfelijk materiaal wordt gewoon gekopieerd. Zo houdt een kweker een ras zuiver.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft een windbestuivende plant zoals gras geen opvallende bloemen?",
        opties=[
            "Ze moet geen insecten lokken, want de wind doet het werk",
            "Ze heeft geen stuifmeel nodig",
            "Ze plant zich niet seksueel voort",
        ],
        antwoord=0,
        uitleg="Insectenbestuivers lokken met kleur, geur en nectar. Windbestuivers maken in de plaats daarvan enorm veel licht stuifmeel — waar hooikoortspatiënten last van hebben.",
    ),
    dict(
        type="invultekst",
        vraag="De buis waarlangs een zaadcel de teelbal verlaat richting de urinebuis, is de ___.",
        antwoord="zaadleider",
        uitleg="Vanuit de bijbal gaat de zaadleider naar de urinebuis. Onderweg voegen de zaadblaasjes en de prostaat hun vocht toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar gebeurt de bevruchting bij de mens meestal?",
        opties=["In de eileider", "In de baarmoeder", "In de vagina"],
        antwoord=0,
        uitleg="De zaadcellen zwemmen door de baarmoeder tot in de eileider en ontmoeten daar de eicel. De bevruchte eicel reist daarna naar de baarmoeder om zich in te nestelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over soa's kloppen?",
        opties=[
            "Ze worden doorgegeven bij seksueel contact",
            "Een condoom vermindert het risico sterk",
            "Je ziet altijd meteen dat iemand een soa heeft",
            "De pil beschermt ertegen",
        ],
        antwoord=[0, 1],
        uitleg="Soa's geef je door bij seksueel contact en een condoom is de beste bescherming. Veel soa's geven in het begin geen klachten, en hormonale middelen beschermen er niet tegen.",
    ),
]

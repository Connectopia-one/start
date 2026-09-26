# -*- coding: utf-8 -*-
"""De vragen voor "Zinsdelen, zinssoorten en congruentie" (✨ Spark, Nederlands).

Uit de vakfiche, Inzicht in het taalsysteem: de zinssoorten (bevestigend en
ontkennend; mededelend, vragend, bevelend en uitroepend; enkelvoudig en
samengesteld) en de zinsdelen (onderwerp, gezegde met de doen- en de
zijn-relatie, persoonsvorm, lijdend voorwerp, meewerkend voorwerp en
bijwoordelijke bepaling), plus de congruentie tussen onderwerp en
persoonsvorm.

Deel 1 leert de zinsdelen vinden met de vraagjes die erbij horen. Deel 2 gaat
over de zijn-relatie, samengestelde zinnen en de valstrikken bij congruentie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="In 'De buurvrouw wast haar auto' — wie of wat doet er iets?",
        opties=["de buurvrouw", "haar auto", "wast", "haar"],
        antwoord=0,
        uitleg="Het onderwerp vind je met 'wie of wat' plus het werkwoord: wie wast? De buurvrouw.",
    ),
    dict(
        type="invultekst",
        vraag="Het werkwoord dat van vorm verandert als je de zin in een andere tijd zet, is de ___.",
        antwoord="persoonsvorm",
        uitleg="'Hij loopt' wordt 'hij liep': 'loopt' verandert mee, dus dat is de persoonsvorm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je de persoonsvorm in een zin?",
        opties=[
            "Je zet de zin in een andere tijd en kijkt welk werkwoord verandert",
            "Je neemt het langste werkwoord",
            "Je neemt het laatste woord",
            "Je neemt het woord na het onderwerp",
        ],
        antwoord=0,
        uitleg="Een tweede trucje: maak er een ja-neevraag van. Het werkwoord dat dan vooraan springt, is de persoonsvorm.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'Tom geeft zijn zus een boek' — wat is het lijdend voorwerp?",
        opties=["een boek", "Tom", "zijn zus", "geeft"],
        antwoord=0,
        uitleg="Wie of wat geeft Tom? Een boek. Het lijdend voorwerp ondergaat de handeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="In diezelfde zin 'Tom geeft zijn zus een boek' — wat is het meewerkend voorwerp?",
        opties=["zijn zus", "een boek", "Tom", "geeft"],
        antwoord=0,
        uitleg="Aan wie geeft hij het boek? Aan zijn zus. Je kan er 'aan' voor zetten: dat is het teken van een meewerkend voorwerp.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor een lijdend voorwerp kan je meestal 'aan' of 'voor' zetten.",
        antwoord=False,
        uitleg="Niet juist. Dat geldt voor het meewerkend voorwerp: hij geeft (aan) zijn zus een boek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk zinsdeel zegt waar, wanneer of hoe iets gebeurt?",
        opties=[
            "De bijwoordelijke bepaling",
            "Het onderwerp",
            "Het lijdend voorwerp",
            "De persoonsvorm",
        ],
        antwoord=0,
        uitleg="'Morgen', 'in de tuin', 'met veel geduld': bijwoordelijke bepalingen geven de omstandigheden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zinsdelen zijn bijwoordelijke bepalingen in 'Gisteren fietste hij rustig naar school'?",
        opties=["gisteren", "rustig", "naar school", "hij"],
        antwoord=[0, 1, 2],
        uitleg="Wanneer, hoe en waarheen: drie bepalingen. 'Hij' is het onderwerp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin is een vragende zin?",
        opties=[
            "Komt hij morgen mee?",
            "Hij komt morgen mee.",
            "Kom morgen mee!",
            "Wat een verrassing!",
        ],
        antwoord=0,
        uitleg="Mededelend, vragend, bevelend en uitroepend: aan de vorm en het leesteken zie je welke soort het is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin is een bevelende zin?",
        opties=[
            "Sluit het raam.",
            "Sluit hij het raam?",
            "Hij sluit het raam.",
            "Wat een tocht!",
        ],
        antwoord=0,
        uitleg="Een bevelende zin begint met de gebiedende wijs en heeft geen onderwerp.",
    ),
    dict(
        type="invultekst",
        vraag="'Wat een lawaai maakt die machine!' is een ___ zin.",
        antwoord="uitroepende",
        uitleg="Een uitroepende zin drukt verbazing of een sterk gevoel uit en eindigt op een uitroepteken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin is ontkennend?",
        opties=[
            "Ik heb geen tijd.",
            "Ik heb veel tijd.",
            "Heb ik tijd?",
            "Neem je tijd.",
        ],
        antwoord=0,
        uitleg="Woorden als 'niet', 'geen', 'nooit' en 'niemand' maken van een bevestigende zin een ontkennende.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke woorden maken een zin ontkennend?",
        opties=["niet", "geen", "nooit", "altijd"],
        antwoord=[0, 1, 2],
        uitleg="'Altijd' bevestigt net. De eerste drie draaien de betekenis om.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een enkelvoudige zin?",
        opties=[
            "Een zin met één persoonsvorm",
            "Een zin met één woord",
            "Een korte zin",
            "Een zin zonder komma",
        ],
        antwoord=0,
        uitleg="Eén persoonsvorm betekent één zin. Twee persoonsvormen maken er een samengestelde zin van.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin is samengesteld?",
        opties=[
            "Hij bleef thuis omdat hij ziek was.",
            "Hij bleef de hele dag thuis.",
            "Hij bleef thuis.",
            "Blijf thuis!",
        ],
        antwoord=0,
        uitleg="'Bleef' en 'was' zijn twee persoonsvormen, dus twee zinnen aan elkaar geschreven met 'omdat'.",
    ),
    dict(
        type="waarofniet",
        vraag="Het aantal persoonsvormen vertelt je uit hoeveel zinnen een samengestelde zin bestaat.",
        antwoord=True,
        uitleg="Tel de persoonsvormen: twee persoonsvormen betekenen twee deelzinnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin klopt?",
        opties=[
            "De leerlingen wachten op de bus.",
            "De leerlingen wacht op de bus.",
            "De leerling wachten op de bus.",
            "De leerlingen wachtte op de bus.",
        ],
        antwoord=0,
        uitleg="Een meervoudig onderwerp vraagt een meervoudige persoonsvorm. Dat heet congruentie.",
    ),
    dict(
        type="invultekst",
        vraag="Dat het onderwerp en de persoonsvorm bij elkaar passen in enkelvoud of meervoud, heet ___.",
        antwoord="congruentie",
        uitleg="'De hond blaft' tegenover 'de honden blaffen': de persoonsvorm past zich aan het onderwerp aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'Mijn zus is verpleegkundige' — wat voor soort gezegde staat er?",
        opties=[
            "Een gezegde met een zijn-relatie",
            "Een gezegde met een doen-relatie",
            "Er staat geen gezegde",
            "Twee gezegdes",
        ],
        antwoord=0,
        uitleg="Het onderwerp doet niets: het wordt gelijkgesteld aan iets anders. Dat is de zijn-relatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'Mijn zus repareert fietsen' — wat voor soort gezegde staat er?",
        opties=[
            "Een gezegde met een doen-relatie",
            "Een gezegde met een zijn-relatie",
            "Een bevelende zin",
            "Een bijwoordelijke bepaling",
        ],
        antwoord=0,
        uitleg="Het onderwerp voert een handeling uit: dat is de doen-relatie.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke werkwoorden horen bij de zijn-relatie?",
        opties=["zijn", "worden", "blijven", "fietsen"],
        antwoord=[0, 1, 2],
        uitleg="Zijn, worden, blijven, blijken, lijken, schijnen en heten koppelen het onderwerp aan een eigenschap of een naam.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'Het weer wordt beter' — welk woord zegt wat het onderwerp wordt?",
        opties=["beter", "het weer", "wordt", "er"],
        antwoord=0,
        uitleg="'Beter' is het naamwoordelijk deel: samen met 'wordt' vormt het het gezegde.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'De directeur heeft de brief gisteren ondertekend' — wat is de persoonsvorm?",
        opties=["heeft", "ondertekend", "brief", "gisteren"],
        antwoord=0,
        uitleg="Zet de zin in de tegenwoordige tijd: 'heeft' wordt 'had'. Het deelwoord 'ondertekend' verandert niet mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="In diezelfde zin: wat is het lijdend voorwerp?",
        opties=["de brief", "de directeur", "gisteren", "ondertekend"],
        antwoord=0,
        uitleg="Wie of wat heeft hij ondertekend? De brief.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke zin heeft een lijdend voorwerp.",
        antwoord=False,
        uitleg="Niet juist. 'Hij slaapt' heeft er geen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin bevat een meewerkend voorwerp?",
        opties=[
            "Ze stuurde haar vriendin een kaartje.",
            "Ze stuurde een kaartje.",
            "Ze fietste naar huis.",
            "Ze was moe.",
        ],
        antwoord=0,
        uitleg="Aan wie stuurde ze het? Aan haar vriendin. Dat is het meewerkend voorwerp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin is juist? Let op de congruentie.",
        opties=[
            "De doos met boeken staat in de gang.",
            "De doos met boeken staan in de gang.",
            "De dozen met boeken staat in de gang.",
            "De doos met boek staan in de gang.",
        ],
        antwoord=0,
        uitleg="Het onderwerp is 'de doos', enkelvoud. 'Met boeken' is maar een bepaling en verandert daar niets aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zinnen kloppen qua congruentie?",
        opties=[
            "Een van de leerlingen heeft het gezien.",
            "De groep kinderen speelt buiten.",
            "Mijn ouders werken allebei in Hasselt.",
            "De rij wachtenden staan tot aan de hoek.",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het onderwerp is telkens 'een', 'de groep' en 'mijn ouders'. In de laatste zin is het onderwerp 'de rij', dus moet het 'staat' zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'Op zaterdag traint de ploeg in Genk' — wat is het onderwerp?",
        opties=["de ploeg", "op zaterdag", "in Genk", "traint"],
        antwoord=0,
        uitleg="Wie traint? De ploeg. Dat het onderwerp achter de persoonsvorm staat, verandert niets aan zijn functie.",
    ),
    dict(
        type="invultekst",
        vraag="In 'Hij is de beste van de klas' noem je 'de beste van de klas' het ___ deel van het gezegde.",
        antwoord="naamwoordelijk",
        uitleg="Bij een zijn-relatie bestaat het gezegde uit een koppelwerkwoord plus het naamwoordelijk deel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel persoonsvormen staan er in 'Ik wist niet dat je ziek was, dus ik belde niet'?",
        opties=["Drie", "Twee", "Eén", "Vier"],
        antwoord=0,
        uitleg="'Wist', 'was' en 'belde': drie persoonsvormen, dus drie deelzinnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zinssoort is 'Zou je het raam even willen sluiten?'",
        opties=[
            "Een vragende zin die eigenlijk een vraag om iets te doen is",
            "Een bevelende zin",
            "Een uitroepende zin",
            "Een ontkennende zin",
        ],
        antwoord=0,
        uitleg="De vorm is vragend, de bedoeling is een verzoek. Zo klinkt het beleefder dan 'sluit het raam'.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bevelende zin begint altijd met het onderwerp.",
        antwoord=False,
        uitleg="Niet juist. In 'Kom hier!' staat helemaal geen onderwerp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zinnen zijn samengesteld?",
        opties=[
            "Ik blijf thuis, want het regent.",
            "Toen hij thuiskwam, was het al donker.",
            "Ze zei dat ze later zou komen.",
            "Na de training ging hij meteen slapen.",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie hebben twee persoonsvormen. De laatste zin heeft er maar één: 'ging'.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'De kinderen kregen van de directeur een diploma' — wat is het meewerkend voorwerp?",
        opties=[
            "Er is er geen; 'van de directeur' is een bepaling",
            "van de directeur",
            "een diploma",
            "de kinderen",
        ],
        antwoord=0,
        uitleg="De kinderen zijn hier het onderwerp, het diploma het lijdend voorwerp, en 'van de directeur' zegt van wie ze het kregen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is 'De regering hebben een beslissing genomen' fout?",
        opties=[
            "'De regering' is enkelvoud, dus moet het 'heeft' zijn",
            "'Beslissing' moet in het meervoud",
            "'Genomen' is fout gespeld",
            "Er ontbreekt een komma",
        ],
        antwoord=0,
        uitleg="Een groep mensen die je als één geheel noemt, is enkelvoud: de regering heeft, de ploeg speelt, de klas luistert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vraag gebruik je om het onderwerp te vinden?",
        opties=[
            "Wie of wat + persoonsvorm?",
            "Wie of wat + persoonsvorm + onderwerp?",
            "Aan wie?",
            "Waar of wanneer?",
        ],
        antwoord=0,
        uitleg="Voor het lijdend voorwerp gebruik je 'wie of wat' plus de persoonsvorm plus het onderwerp. Voor bepalingen vraag je waar, wanneer of hoe.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'Mijn broer blijft rustig onder druk' — welke woorden vormen samen het gezegde?",
        opties=["blijft en rustig", "blijft alleen", "rustig alleen", "onder druk"],
        antwoord=0,
        uitleg="'Blijven' is een koppelwerkwoord, dus 'blijft rustig' is samen het naamwoordelijk gezegde. 'Onder druk' is een bepaling.",
    ),
    dict(
        type="waarofniet",
        vraag="In een zin met 'er' kan het onderwerp achter de persoonsvorm staan, zoals in 'Er komen drie gasten'.",
        antwoord=True,
        uitleg="Het onderwerp is 'drie gasten', meervoud, dus 'komen'. 'Er' vult alleen de eerste plaats in de zin op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom helpt zinsontleding je bij het schrijven?",
        opties=[
            "Omdat je er lange zinnen mee kan controleren op congruentie en samenhang",
            "Omdat je dan mooiere woorden kiest",
            "Omdat je dan sneller typt",
            "Omdat het op het examen apart getest wordt",
        ],
        antwoord=0,
        uitleg="Wie bij een lange zin het onderwerp terugvindt, ziet meteen of de persoonsvorm klopt. Dat is ondersteunende kennis.",
    ),
]

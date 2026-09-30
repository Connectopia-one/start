# -*- coding: utf-8 -*-
"""De vragen voor "Zinsdelen en samengestelde zinnen" (🚀 Boost doorstroom, Nederlands).

Uit het syntactisch domein van allebei de vakfiches: congruentie tussen
onderwerp en persoonsvorm, de woordvolgorde in hoofdzin en bijzin, inversie, de
zinsdelen (onderwerp, persoonsvorm, werkwoordelijk en naamwoordelijk gezegde,
lijdend, meewerkend, voorzetsel- en handelend voorwerp, bijwoordelijke
bepaling) en de soorten zinnen.

Deel 1 ontleedt de zin in zinsdelen. Deel 2 gaat over soorten zinnen: actief en
passief, enkelvoudig en samengesteld, onderschikking en nevenschikking.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="In 'De postbode bracht mijn oma een pakje', wat is het lijdend voorwerp?",
        opties=["een pakje", "mijn oma", "de postbode", "bracht"],
        antwoord=0,
        uitleg="Vraag: wie of wat bracht de postbode? Een pakje. 'Mijn oma' is de ontvanger en dus meewerkend voorwerp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het gezegde in 'De kinderen zijn moe'?",
        opties=[
            "zijn moe, een naamwoordelijk gezegde",
            "zijn, een werkwoordelijk gezegde",
            "moe, een bijwoordelijke bepaling",
            "de kinderen zijn, een onderwerp met persoonsvorm",
        ],
        antwoord=0,
        uitleg="Bij een koppelwerkwoord hoort het naamwoordelijk deel bij het gezegde. Samen zeggen ze wat het onderwerp is of wordt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het zinsdeel dat antwoord geeft op 'wie of wat plus de persoonsvorm'?",
        antwoord=["het onderwerp", "onderwerp", "subject"],
        uitleg="Het onderwerp bepaalt ook de vorm van de persoonsvorm. Dat heet congruentie.",
    ),
    dict(
        type="waarofniet",
        vraag="Het gezegde van 'Zij is verpleegkundige' is naamwoordelijk.",
        antwoord=True,
        uitleg="'Is' is een koppelwerkwoord en 'verpleegkundige' zegt iets over het onderwerp. Samen vormen ze een naamwoordelijk gezegde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zinsdelen noemt de vakfiche?",
        opties=[
            "lijdend voorwerp",
            "meewerkend voorwerp",
            "voorzetselvoorwerp",
            "rijmend voorwerp",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt ook het handelend voorwerp en de bijwoordelijke bepaling. Een rijmend voorwerp bestaat niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'Hij wacht al een uur op de trein', wat is 'op de trein'?",
        opties=[
            "een voorzetselvoorwerp",
            "een bijwoordelijke bepaling van plaats",
            "een lijdend voorwerp",
            "een handelend voorwerp",
        ],
        antwoord=0,
        uitleg="Het voorzetsel ligt vast bij het werkwoord: je wacht óp iets. Je kan het niet vervangen door 'onder' of 'naast'.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het zinsdeel dat in een lijdende zin met 'door' aangeeft wie de handeling uitvoert?",
        antwoord=["het handelend voorwerp", "handelend voorwerp"],
        uitleg="In 'De brief werd door de directeur ondertekend' is dat 'door de directeur'.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bijwoordelijke bepaling is altijd verplicht in de zin.",
        antwoord=False,
        uitleg="Ze is juist meestal weglaatbaar. 'Gisteren fietste ze naar school' blijft een zin zonder 'gisteren'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel bijwoordelijke bepalingen staan er in 'Gisteren fietste ze door de regen naar school'?",
        opties=["drie", "twee", "één", "vier"],
        antwoord=0,
        uitleg="Gisteren (tijd), door de regen (omstandigheid) en naar school (richting). Alle drie kan je weglaten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een werkwoordelijk en een naamwoordelijk gezegde?",
        opties=[
            "een naamwoordelijk gezegde bevat een koppelwerkwoord en zegt iets over het onderwerp",
            "een naamwoordelijk gezegde bestaat alleen uit naamwoorden zonder werkwoord",
            "een werkwoordelijk gezegde staat altijd achteraan in de zin",
            "een werkwoordelijk gezegde komt alleen in bijzinnen voor",
        ],
        antwoord=0,
        uitleg="'Hij loopt' is werkwoordelijk: er gebeurt iets. 'Hij is moe' is naamwoordelijk: er wordt iets over hem gezegd.",
    ),
    dict(
        type="waarofniet",
        vraag="Je vindt het onderwerp door te vragen: wie of wat plus de persoonsvorm.",
        antwoord=True,
        uitleg="Wie of wat blaft? De hond van de buren. Dat hele stuk is het onderwerp, niet alleen 'de hond'.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'De brief werd door de directeur ondertekend', wat is 'door de directeur'?",
        opties=[
            "het handelend voorwerp",
            "het onderwerp",
            "het lijdend voorwerp",
            "een bijwoordelijke bepaling van plaats",
        ],
        antwoord=0,
        uitleg="Het onderwerp is 'de brief'. Wie de handeling écht uitvoert, staat in de door-groep.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het zinsdeel waarop de handeling van het werkwoord overgaat?",
        antwoord=["het lijdend voorwerp", "lijdend voorwerp"],
        uitleg="Vandaar de naam: het lijdt de handeling. In de lijdende vorm wordt het het onderwerp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je het lijdend voorwerp in een zin?",
        opties=[
            "je vraagt: wie of wat plus persoonsvorm plus onderwerp",
            "je neemt het zinsdeel dat achteraan staat",
            "je neemt het zinsdeel met een voorzetsel ervoor",
            "je vraagt: waar of wanneer plus persoonsvorm",
        ],
        antwoord=0,
        uitleg="Wie of wat bracht de postbode? Een pakje. Die vraag onderscheidt het lijdend voorwerp van het onderwerp.",
    ),
    dict(
        type="waarofniet",
        vraag="Elk zinsdeel bestaat uit precies één woord.",
        antwoord=False,
        uitleg="'De hond van de buren' is één zinsdeel van vijf woorden. Je verplaatst een zinsdeel altijd in zijn geheel.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'Mijn broer geeft zijn beste vriend een boek', wat is 'zijn beste vriend'?",
        opties=[
            "het meewerkend voorwerp",
            "het lijdend voorwerp",
            "het onderwerp",
            "het handelend voorwerp",
        ],
        antwoord=0,
        uitleg="Je kan er 'aan' voor zetten: hij geeft een boek aan zijn beste vriend. Dat is de proef voor het meewerkend voorwerp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke woordgroepen zijn bijwoordelijke bepalingen in 'Morgen ga ik met de fiets naar de markt'?",
        opties=["morgen", "met de fiets", "naar de markt", "ik"],
        antwoord=[0, 1, 2],
        uitleg="'Ik' is het onderwerp. De drie andere zeggen wanneer, hoe en waarheen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat onderscheidt een voorzetselvoorwerp van een bijwoordelijke bepaling met een voorzetsel?",
        opties=[
            "bij een voorzetselvoorwerp ligt het voorzetsel vast bij het werkwoord",
            "een voorzetselvoorwerp staat altijd vooraan in de zin",
            "een bijwoordelijke bepaling bevat nooit een voorzetsel",
            "een voorzetselvoorwerp bestaat uit precies twee woorden",
        ],
        antwoord=0,
        uitleg="Je rekent óp iemand, je twijfelt áán iets. In 'hij zit op de bank' kan het voorzetsel wel wisselen, dus daar is het een bepaling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk zinsdeel ontbreekt nooit in een Nederlandse mededelende zin?",
        opties=[
            "de persoonsvorm",
            "het lijdend voorwerp",
            "het meewerkend voorwerp",
            "de bijwoordelijke bepaling",
        ],
        antwoord=0,
        uitleg="Zonder persoonsvorm heb je geen zin maar een woordgroep. De drie andere zinsdelen kunnen allemaal ontbreken.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'De hond van de buren blaft de hele nacht', wat is het onderwerp?",
        opties=[
            "de hond van de buren",
            "de hond",
            "de buren",
            "de hele nacht",
        ],
        antwoord=0,
        uitleg="Het hele stuk hoort bij elkaar. Dat merk je als je de zin omdraait: 'De hele nacht blaft de hond van de buren.'",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="In welke vorm staat 'De brief wordt door de secretaresse getypt'?",
        opties=[
            "de lijdende vorm",
            "de bedrijvende vorm",
            "de gebiedende wijs",
            "de voltooid verleden tijd",
        ],
        antwoord=0,
        uitleg="In de lijdende vorm wordt het lijdend voorwerp het onderwerp, en verschijnt de echte uitvoerder in een door-groep.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de lijdende vorm van 'De hond bijt de postbode'?",
        opties=[
            "De postbode wordt door de hond gebeten.",
            "De hond wordt door de postbode gebeten.",
            "De postbode bijt de hond niet.",
            "Door de hond bijt de postbode.",
        ],
        antwoord=0,
        uitleg="Het lijdend voorwerp 'de postbode' wordt onderwerp, en het oude onderwerp komt in een door-groep te staan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een zin met maar één persoonsvorm?",
        antwoord=["een enkelvoudige zin", "enkelvoudige zin", "enkelvoudig"],
        uitleg="Tel de persoonsvormen: één betekent enkelvoudig, meer dan één betekent samengesteld.",
    ),
    dict(
        type="waarofniet",
        vraag="In een bijzin staat de persoonsvorm altijd op de tweede plaats.",
        antwoord=False,
        uitleg="Dat geldt voor de hoofdzin. In een bijzin schuift de persoonsvorm juist naar achteren: 'omdat het de hele dag regende'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soorten zinnen noemt de vakfiche?",
        opties=["mededelende", "bevelende", "uitroepende", "rijmende"],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt ook vragende zinnen, en daarnaast het onderscheid bevestigend of ontkennend. Rijmende zinnen zijn geen zinssoort.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Kom onmiddellijk hier!' Wat voor zin is dat?",
        opties=[
            "een bevelende zin",
            "een uitroepende zin",
            "een vragende zin",
            "een mededelende zin",
        ],
        antwoord=0,
        uitleg="De persoonsvorm staat in de gebiedende wijs en er is geen onderwerp. Het uitroepteken maakt er nog geen uitroepende zin van.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het koppelen van twee gelijkwaardige hoofdzinnen?",
        antwoord=["nevenschikking", "de nevenschikking", "nevenschikkend"],
        uitleg="En, maar, of, want en dus verbinden twee zinnen die allebei op eigen benen kunnen staan.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij onderschikking hangt de ene zin van de andere af.",
        antwoord=True,
        uitleg="'Omdat het regende' kan niet alleen staan. Zo'n zin heeft een hoofdzin nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'Ik blijf thuis omdat het regent', wat voor verband is er tussen de twee delen?",
        opties=[
            "onderschikking",
            "nevenschikking",
            "inversie",
            "congruentie",
        ],
        antwoord=0,
        uitleg="'Omdat' is een onderschikkend voegwoord: het maakt van het tweede deel een bijzin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke woorden zijn nevenschikkende voegwoorden?",
        opties=["en", "maar", "want", "omdat"],
        antwoord=[0, 1, 2],
        uitleg="'Omdat' is onderschikkend. Een geheugensteun voor de nevenschikkende: en, maar, of, want, dus.",
    ),
    dict(
        type="waarofniet",
        vraag="Inversie betekent dat het onderwerp achter de persoonsvorm komt te staan.",
        antwoord=True,
        uitleg="Zodra er iets anders dan het onderwerp vooraan staat, draait de volgorde om: 'Morgen ga ik'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zeg je 'Morgen ga ik naar de markt' en niet 'Morgen ik ga naar de markt'?",
        opties=[
            "omdat de persoonsvorm in een hoofdzin op de tweede plaats blijft",
            "omdat 'morgen' een bijzin inleidt",
            "omdat het onderwerp nooit vooraan mag staan",
            "omdat de zin anders in de verleden tijd zou staan",
        ],
        antwoord=0,
        uitleg="In een Nederlandse hoofdzin staat de persoonsvorm altijd op plaats twee. Staat er iets anders op één, dan schuift het onderwerp erachter.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een zin met meer dan één persoonsvorm?",
        antwoord=["een samengestelde zin", "samengestelde zin", "samengesteld"],
        uitleg="Zo'n zin bestaat uit meerdere deelzinnen, neven- of ondergeschikt aan elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kan een lijdende zin het handelend voorwerp weglaten?",
        opties=[
            "omdat het onderwerp al bezet is door het lijdend voorwerp",
            "omdat een lijdende zin geen werkwoord nodig heeft",
            "omdat het handelend voorwerp nooit belangrijk is",
            "omdat een lijdende zin altijd in de verleden tijd staat",
        ],
        antwoord=0,
        uitleg="'De ramen werden gelapt' is een volledige zin. Wie het deed, hoef je niet te zeggen, en dat is precies waarom de vorm zo populair is.",
    ),
    dict(
        type="waarofniet",
        vraag="Elke vragende zin begint met een vragend voornaamwoord.",
        antwoord=False,
        uitleg="'Ga jij mee?' begint met de persoonsvorm. Vragen met een vraagwoord en vragen zonder vraagwoord bestaan allebei.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat verandert er als je 'De gemeente heeft het plein heraangelegd' in de lijdende vorm zet?",
        opties=[
            "'het plein' wordt het onderwerp en 'de gemeente' komt in een door-groep",
            "de zin wordt vragend in plaats van mededelend",
            "de zin verandert van verleden naar tegenwoordige tijd",
            "het werkwoord verdwijnt uit de zin",
        ],
        antwoord=0,
        uitleg="Het resultaat is: 'Het plein is door de gemeente heraangelegd.' De inhoud blijft, de nadruk verschuift.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zinnen zijn samengesteld?",
        opties=[
            "Ik blijf thuis omdat het regent.",
            "Hij belde aan en zij deed open.",
            "Toen ik binnenkwam, was iedereen al weg.",
            "De hond van de buren blaft de hele nacht.",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie hebben twee persoonsvormen. De laatste heeft er maar één en is dus enkelvoudig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruiken ambtelijke teksten vaak de lijdende vorm?",
        opties=[
            "omdat je dan niet hoeft te zeggen wie iets gedaan heeft",
            "omdat lijdende zinnen altijd korter zijn",
            "omdat de lijdende vorm minder spelfouten oplevert",
            "omdat een lijdende zin geen onderwerp nodig heeft",
        ],
        antwoord=0,
        uitleg="'Uw aanvraag werd afgewezen' verzwijgt wie besliste. Dat maakt zulke teksten ook moeilijker leesbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'Hoewel hij doodmoe was, ging hij toch trainen', welk deel is de bijzin?",
        opties=[
            "Hoewel hij doodmoe was",
            "ging hij toch trainen",
            "hij toch trainen",
            "doodmoe was",
        ],
        antwoord=0,
        uitleg="Je herkent de bijzin aan het onderschikkend voegwoord vooraan en aan de persoonsvorm achteraan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat voor zin is 'Wat is dat mooi!'?",
        opties=[
            "een uitroepende zin",
            "een vragende zin",
            "een bevelende zin",
            "een ontkennende zin",
        ],
        antwoord=0,
        uitleg="De zin begint met een vraagwoord maar vraagt niets. Hij drukt verwondering uit, en dat is uitroepend.",
    ),
]

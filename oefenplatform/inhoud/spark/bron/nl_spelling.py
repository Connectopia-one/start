# -*- coding: utf-8 -*-
"""De vragen voor "Spelling, leestekens en werkwoordsvormen" (✨ Spark, Nederlands).

Uit de vakfiche, Inzicht in het taalsysteem: de spellingregels van het
Nederlands (woorden met een vast en een veranderlijk woordbeeld, werkwoorden,
hoofdletters), de diakritische tekens trema, koppelteken en apostrof, de
interpunctietekens, korte en lange klanken, het onderscheid tussen klank- en
schriftbeeld, en de werkwoordstijden: ottt, vtt, ovt, vvt, otkt en de
gebiedende wijs.

Deel 1 oefent de regels één voor één. Deel 2 legt de valstrikken voor die een
spellingcontrole niet vindt: gebeurt of gebeurd, vind of vindt, ligt of legt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welk woord is juist geschreven?",
        opties=["hij wordt", "hij word", "hij wort", "hij wordd"],
        antwoord=0,
        uitleg="In de tegenwoordige tijd krijgt het werkwoord bij hij, zij of het een -t achter de stam: word + t.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de stam van een werkwoord?",
        opties=[
            "Het hele werkwoord min -en",
            "Het werkwoord met -t erbij",
            "De verleden tijd",
            "Het voltooid deelwoord",
        ],
        antwoord=0,
        uitleg="Werken min -en geeft werk. De stam is je vertrekpunt voor alle vormen.",
    ),
    dict(
        type="invultekst",
        vraag="Vul aan: ik werk, jij werkt, hij ___.",
        antwoord="werkt",
        uitleg="Bij hij, zij of het komt er altijd een -t bij de stam, ook als het woord daardoor raar oogt.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke zin staat het werkwoord juist?",
        opties=[
            "Word jij ook moe van dat lawaai?",
            "Wordt jij ook moe van dat lawaai?",
            "Word jij ook moe van dat lawaai.",
            "Wort jij ook moe van dat lawaai?",
        ],
        antwoord=0,
        uitleg="Staat 'jij' of 'je' áchter het werkwoord, dan valt de -t weg: 'word jij'. Vóór het werkwoord blijft ze: 'jij wordt'.",
    ),
    dict(
        type="invultekst",
        vraag="Het ezelsbruggetje met de medeklinkers t, k, f, s, ch en p heet ___.",
        antwoord="kofschip",
        uitleg="'t Kofschip: eindigt de stam op een van die klanken, dan krijg je -te(n) in de verleden tijd en -t in het voltooid deelwoord.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de verleden tijd van 'werken'?",
        opties=["werkte", "werkde", "werkt", "gewerkt"],
        antwoord=0,
        uitleg="De stam werk eindigt op k, een letter van 't kofschip, dus -te: werkte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de verleden tijd van 'leren'?",
        opties=["leerde", "leerte", "leert", "geleerd"],
        antwoord=0,
        uitleg="De stam leer eindigt op r, en die zit niet in 't kofschip, dus -de: leerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voltooide deelwoorden zijn juist?",
        opties=["gewerkt", "geleerd", "gefietst", "gebeurdt"],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie volgen 't kofschip. 'Gebeurd' schrijf je met een d en nooit met dt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een voltooid deelwoord eindigt nooit op -dt.",
        antwoord=True,
        uitleg="Het is gebeurd, geleerd, gewerkt. De combinatie -dt komt alleen voor bij een stam op -d plus de -t van de tegenwoordige tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk woord heeft een lange klank?",
        opties=["maan", "man", "kat", "pot"],
        antwoord=0,
        uitleg="'Maan' heeft de lange aa-klank, 'man' de korte a. Dat verschil bepaalt hoe je het meervoud schrijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het meervoud van 'man'?",
        opties=["mannen", "manen", "mans", "mannens"],
        antwoord=0,
        uitleg="Bij een korte klank verdubbel je de medeklinker: mannen. 'Manen' zijn de haren van een paard.",
    ),
    dict(
        type="invultekst",
        vraag="Het meervoud van 'maan' is ___.",
        antwoord="manen",
        uitleg="Bij een lange klank in een open lettergreep schrijf je maar één a: ma-nen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke woorden schrijf je met een hoofdletter?",
        opties=["Nederlands", "België", "Antwerpen", "maandag"],
        antwoord=[0, 1, 2],
        uitleg="Talen, landen en plaatsen krijgen een hoofdletter. Dagen en maanden in het Nederlands niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk leesteken zet je aan het einde van een vraag?",
        opties=["Een vraagteken", "Een punt", "Een komma", "Een dubbele punt"],
        antwoord=0,
        uitleg="Punt, vraagteken en uitroepteken sluiten een zin af, elk met hun eigen bedoeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je een dubbele punt?",
        opties=[
            "Om een opsomming of een citaat aan te kondigen",
            "Om een zin af te sluiten",
            "Om een vraag te stellen",
            "Om twee woorden aan elkaar te plakken",
        ],
        antwoord=0,
        uitleg="'Neem mee: je boek, je pen en je agenda.' Na de dubbele punt komt wat aangekondigd werd.",
    ),
    dict(
        type="invultekst",
        vraag="De twee puntjes op de e in 'zeeën' heten een ___.",
        antwoord="trema",
        uitleg="Een trema zegt: begin hier een nieuwe klank. Zonder trema zou je 'zeeen' als één lange klank lezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke woorden schrijf je met een apostrof in het meervoud?",
        opties=["foto's", "taxi's", "baby's", "huizen"],
        antwoord=[0, 1, 2],
        uitleg="Eindigt een woord op een losse a, i, o, u of y, dan zet je een apostrof voor de s, zodat de klank lang blijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schrijf je 'zee-eend' met een koppelteken?",
        opties=[
            "Omdat er anders drie e's botsen en je het woord verkeerd leest",
            "Omdat het twee dieren zijn",
            "Omdat het een lang woord is",
            "Omdat het een eigennaam is",
        ],
        antwoord=0,
        uitleg="Bij klinkerbotsing zet je een koppelteken: zee-eend, auto-ongeluk, na-apen.",
    ),
    dict(
        type="waarofniet",
        vraag="Tussen twee woorden van een samenstelling staat meestal geen spatie.",
        antwoord=True,
        uitleg="Het is 'schoolreglement' en 'handdoek', niet 'school reglement'. Dat is het verschil met het Engels.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin is juist geïnterpungeerd?",
        opties=[
            "Kom je mee, of blijf je hier?",
            "Kom je mee of blijf je hier.",
            "kom je mee, of blijf je hier?",
            "Kom je mee of, blijf je hier?",
        ],
        antwoord=0,
        uitleg="Hoofdletter aan het begin, komma voor 'of' tussen twee zinnen, vraagteken op het einde.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke zin over iets van gisteren is juist?",
        opties=[
            "Het is gisteren gebeurd.",
            "Het is gisteren gebeurt.",
            "Het is gisteren gebeurdt.",
            "Het is gisteren gebeurden.",
        ],
        antwoord=0,
        uitleg="Na 'is' staat een voltooid deelwoord, en dat eindigt hier op een d: gebeurd. Vergelijk: 'het gebeurt elke dag'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin over iets dat zich herhaalt, is juist?",
        opties=[
            "Dat gebeurt elke week opnieuw.",
            "Dat gebeurd elke week opnieuw.",
            "Dat gebeurdt elke week opnieuw.",
            "Dat gebeuren elke week opnieuw.",
        ],
        antwoord=0,
        uitleg="Tegenwoordige tijd, derde persoon: stam gebeur + t. De d hoort alleen bij het voltooid deelwoord.",
    ),
    dict(
        type="invultekst",
        vraag="Vul in met de juiste vorm van 'vinden': Wat ___ jij daarvan?",
        antwoord="vind",
        uitleg="'Jij' staat áchter het werkwoord, dus valt de -t weg: vind jij. Voor het werkwoord zou het 'jij vindt' zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin met het werkwoord 'antwoorden' is juist?",
        opties=[
            "Hij antwoordt altijd meteen.",
            "Hij antwoord altijd meteen.",
            "Hij antwoordde altijd meteen op de vraag van gisteren en nu ook.",
            "Hij antwoordt gisteren meteen.",
        ],
        antwoord=0,
        uitleg="De stam is antwoord; met de -t erbij wordt dat antwoordt. De derde zin mengt twee tijden, de vierde ook.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke werkwoordsvormen staan in de onvoltooid verleden tijd?",
        opties=["hij fietste", "wij leerden", "zij speelden", "hij heeft gefietst"],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie zijn ovt. 'Heeft gefietst' is de voltooid tegenwoordige tijd: hulpwerkwoord plus deelwoord.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke tijd staat 'Ik had mijn huiswerk al gemaakt'?",
        opties=[
            "Voltooid verleden tijd",
            "Voltooid tegenwoordige tijd",
            "Onvoltooid verleden tijd",
            "Onvoltooid tegenwoordige tijd",
        ],
        antwoord=0,
        uitleg="'Had' plus een voltooid deelwoord is de vvt: iets was al afgelopen op een moment in het verleden.",
    ),
    dict(
        type="invultekst",
        vraag="'Ik zal morgen komen' staat in de onvoltooid ___ tijd.",
        antwoord="toekomende",
        uitleg="Met 'zullen' plus een infinitief maak je de otkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin staat in de gebiedende wijs?",
        opties=[
            "Sluit de deur.",
            "Hij sluit de deur.",
            "De deur is gesloten.",
            "Zou je de deur sluiten?",
        ],
        antwoord=0,
        uitleg="De imperatief is de kale stam, zonder onderwerp. Je geeft er een bevel of een instructie mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke woorden hebben een veranderlijk woordbeeld?",
        opties=["hond (honden)", "web (webben)", "huis (huizen)", "boek (boeken)"],
        antwoord=[0, 1, 2],
        uitleg="Bij hond hoor je een t maar schrijf je een d, bij web een p maar schrijf je een b, bij huis wordt de s een z. Bij boek verandert er niets.",
    ),
    dict(
        type="waarofniet",
        vraag="Je hoort het verschil tussen 'hij wordt' en 'hij word'.",
        antwoord=False,
        uitleg="Je hoort maar één t. Daarom is dit een regel die je met je hoofd moet toepassen, niet met je oor: klankbeeld en schriftbeeld lopen hier uit elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin met 'liggen' of 'leggen' is juist?",
        opties=[
            "De kat ligt op de mat.",
            "De kat legt op de mat.",
            "De kat liggt op de mat.",
            "De kat leggt op de mat.",
        ],
        antwoord=0,
        uitleg="Liggen doe je zelf; leggen doe je met iets anders: 'ik leg het boek op tafel'. Een spellingcontrole ziet dit verschil niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zinnen bevatten een fout die een spellingcontrole niet aanduidt?",
        opties=[
            "Het is gisteren gebeurt.",
            "Hij word morgen veertien.",
            "Ik leg al een uur in bed.",
            "Ik heb een neiuwe fiets.",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie bestaan als woord, dus de controle zwijgt. 'Neiuwe' bestaat niet en wordt wel aangeduid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk meervoud is juist?",
        opties=["knieën", "knieen", "knie's", "kniën"],
        antwoord=0,
        uitleg="Na een ie-klank schrijf je -ën met een trema, zodat je de e apart leest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verkleinwoord is juist?",
        opties=["baby'tje", "babytje", "baby-tje", "babietje"],
        antwoord=0,
        uitleg="Eindigt een woord op een losse klinker, dan komt er een apostrof voor het verkleinsuffix: baby'tje, tv'tje.",
    ),
    dict(
        type="waarofniet",
        vraag="In 'Ik spreek Frans met mijn Franse buurvrouw' krijgen allebei de woorden een hoofdletter.",
        antwoord=True,
        uitleg="Namen van talen en afleidingen van aardrijkskundige namen schrijf je met een hoofdletter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar hoort in deze zin een komma? 'Als het morgen regent blijven we thuis.'",
        opties=[
            "Na 'regent'",
            "Na 'als'",
            "Na 'morgen'",
            "Er hoort geen komma in",
        ],
        antwoord=0,
        uitleg="Tussen de bijzin en de hoofdzin zet je een komma: 'Als het morgen regent, blijven we thuis.'",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin gebruikt aanhalingstekens correct?",
        opties=[
            "Hij zei: 'Ik kom morgen.'",
            "Hij zei: ik kom morgen.",
            "Hij zei 'Ik kom morgen'",
            "Hij zei: 'Ik kom morgen",
        ],
        antwoord=0,
        uitleg="Een letterlijk citaat krijgt een dubbele punt, aanhalingstekens en een punt binnen de aanhaling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vormen van 'hebben' passen bij de voltooid tegenwoordige tijd van 'lopen'?",
        opties=[
            "ik heb gelopen",
            "jij hebt gelopen",
            "wij hebben gelopen",
            "ik had gelopen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vtt gebruikt de tegenwoordige tijd van hebben of zijn. Met 'had' krijg je de voltooid verleden tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schrijf je 'hij verwacht' zonder extra t?",
        opties=[
            "Omdat de stam al op een t eindigt",
            "Omdat het een lang woord is",
            "Omdat het een uitzondering is",
            "Omdat er een voorvoegsel voor staat",
        ],
        antwoord=0,
        uitleg="De stam van verwachten is verwacht. Er komt geen tweede t bij: nooit 'verwachtt'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt je tekst geschreven en de spellingcontrole meldt niets. Wat doe je?",
        opties=[
            "Je leest zelf na op werkwoordsvormen en op woorden die bestaan maar hier fout zijn",
            "Je dient meteen in",
            "Je verandert alles wat onderstreept staat",
            "Je zet er nog wat komma's bij",
        ],
        antwoord=0,
        uitleg="Een spellingcontrole vindt onbestaande woorden. Gebeurt of gebeurd, ligt of legt, word of wordt: dat blijft jouw werk.",
    ),
]

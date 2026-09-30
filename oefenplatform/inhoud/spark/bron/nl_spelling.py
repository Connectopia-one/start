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
        vraag="Tussen de twee woorden van een samenstelling staat meestal een spatie.",
        antwoord=False,
        uitleg="Niet juist. In het Nederlands schrijf je een samenstelling aan elkaar: voetbalploeg, niet voetbal ploeg.",
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


# ────────────────────────────────────────────────────────────────────────────
# Wisselende woorden
#
# Een testgezin vroeg op 29 september 2026 of een kind dat een hoofdstuk
# opnieuw maakt andere woorden kan krijgen. Kim bakende dat een dag later af:
# enkel bij spelling. Haar woorden: "Voor alle normale vragen en oefeningen
# moet dit helemaal niet. Want de leerstof is de leerstof. Maar bij spelling
# kan ik me wel inbeelden dat meer wisselende woorden beter is."
#
# Dat klopt: bij spelling zit de leerstof in de régel, niet in het woord. De
# woorden hieronder vallen stuk voor stuk onder dezelfde regel als de vraag
# waar ze bij staan, dus ze toetsen precies hetzelfde. Een vraag die over een
# begrip gaat ('t kofschip, wat een trema is, waarvoor een dubbele punt dient)
# krijgt geen varianten: daar valt niets te wisselen.
#
# De eerste beurt is de vraag zelf; deze lijst is beurt twee en verder. Alles
# met de hand geschreven en nagelezen, nooit door een taalmodel bedacht: de
# welkomstbrief aan de testgezinnen belooft uitdrukkelijk geen AI in de
# oefeningen.
#
# De sleutel is de vraagtekst hierboven, letterlijk.
# ────────────────────────────────────────────────────────────────────────────

VARIANTEN = {
    # ── deel 1 ──────────────────────────────────────────────────────────────
    "Welk woord is juist geschreven?": [
        dict(
            vraag="Welk woord is juist geschreven?",
            opties=["hij vindt", "hij vind", "hij vint", "hij vindd"],
            antwoord=0,
            uitleg="De stam is vind. Bij hij, zij of het komt daar een -t bij: vind + t = vindt. Dat je het niet hoort, verandert niets.",
        ),
        dict(
            vraag="Welk woord is juist geschreven?",
            opties=["hij houdt", "hij houd", "hij hout", "hij houdt niet"],
            antwoord=0,
            uitleg="De stam is houd. Bij hij, zij of het komt daar een -t bij: houd + t = houdt. 'Hout' is een ander woord.",
        ),
        dict(
            vraag="Welk woord is juist geschreven?",
            opties=["hij rijdt", "hij rijd", "hij rijt", "hij rijdd"],
            antwoord=0,
            uitleg="De stam is rijd. Bij hij, zij of het komt daar een -t bij: rijd + t = rijdt.",
        ),
        dict(
            vraag="Welk woord is juist geschreven?",
            opties=["zij snijdt", "zij snijd", "zij snijt", "zij snijdd"],
            antwoord=0,
            uitleg="De stam is snijd. Bij hij, zij of het komt daar een -t bij: snijd + t = snijdt.",
        ),
    ],
    "Vul aan: ik werk, jij werkt, hij ___.": [
        dict(vraag="Vul aan: ik leer, jij leert, hij ___.", antwoord="leert",
             uitleg="Bij hij, zij of het komt er altijd een -t bij de stam."),
        dict(vraag="Vul aan: ik speel, jij speelt, hij ___.", antwoord="speelt",
             uitleg="Bij hij, zij of het komt er altijd een -t bij de stam."),
        dict(vraag="Vul aan: ik loop, jij loopt, hij ___.", antwoord="loopt",
             uitleg="Bij hij, zij of het komt er altijd een -t bij de stam."),
        dict(vraag="Vul aan: ik bak, jij bakt, hij ___.", antwoord="bakt",
             uitleg="Bij hij, zij of het komt er altijd een -t bij de stam."),
    ],
    "In welke zin staat het werkwoord juist?": [
        dict(
            vraag="In welke zin staat het werkwoord juist?",
            opties=[
                "Vind jij dat ook zo raar?",
                "Vindt jij dat ook zo raar?",
                "Vind jij dat ook zo raar.",
                "Vint jij dat ook zo raar?",
            ],
            antwoord=0,
            uitleg="Staat 'jij' of 'je' áchter het werkwoord, dan valt de -t weg: 'vind jij'. Vóór het werkwoord blijft ze: 'jij vindt'.",
        ),
        dict(
            vraag="In welke zin staat het werkwoord juist?",
            opties=[
                "Rijd jij morgen met ons mee?",
                "Rijdt jij morgen met ons mee?",
                "Rijd jij morgen met ons mee.",
                "Rijt jij morgen met ons mee?",
            ],
            antwoord=0,
            uitleg="Staat 'jij' of 'je' áchter het werkwoord, dan valt de -t weg: 'rijd jij'. Vóór het werkwoord blijft ze: 'jij rijdt'.",
        ),
        dict(
            vraag="In welke zin staat het werkwoord juist?",
            opties=[
                "Houd jij de deur even open?",
                "Houdt jij de deur even open?",
                "Houd jij de deur even open.",
                "Hout jij de deur even open?",
            ],
            antwoord=0,
            uitleg="Staat 'jij' of 'je' áchter het werkwoord, dan valt de -t weg: 'houd jij'. Vóór het werkwoord blijft ze: 'jij houdt'.",
        ),
        dict(
            vraag="In welke zin staat het werkwoord juist?",
            opties=[
                "Word je daar niet moe van?",
                "Wordt je daar niet moe van?",
                "Word je daar niet moe van.",
                "Wort je daar niet moe van?",
            ],
            antwoord=0,
            uitleg="Staat 'jij' of 'je' áchter het werkwoord, dan valt de -t weg: 'word je'. Vóór het werkwoord blijft ze: 'je wordt'.",
        ),
    ],
    "Wat is de verleden tijd van 'werken'?": [
        dict(
            vraag="Wat is de verleden tijd van 'fietsen'?",
            opties=["fietste", "fietsde", "fietst", "gefietst"],
            antwoord=0,
            uitleg="De stam fiets eindigt op een s, en die zit in 't kofschip. Dus -te en niet -de.",
        ),
        dict(
            vraag="Wat is de verleden tijd van 'stappen'?",
            opties=["stapte", "stapde", "stapt", "gestapt"],
            antwoord=0,
            uitleg="De stam stap eindigt op een p, en die zit in 't kofschip. Dus -te en niet -de.",
        ),
        dict(
            vraag="Wat is de verleden tijd van 'blaffen'?",
            opties=["blafte", "blafde", "blaft", "geblaft"],
            antwoord=0,
            uitleg="De stam blaf eindigt op een f, en die zit in 't kofschip. Dus -te en niet -de.",
        ),
        dict(
            vraag="Wat is de verleden tijd van 'lachen'?",
            opties=["lachte", "lachde", "lacht", "gelachen"],
            antwoord=0,
            uitleg="De stam lach eindigt op ch, en die zit in 't kofschip. Dus -te en niet -de.",
        ),
    ],
    "Wat is de verleden tijd van 'leren'?": [
        dict(
            vraag="Wat is de verleden tijd van 'spelen'?",
            opties=["speelde", "speelte", "speelt", "gespeeld"],
            antwoord=0,
            uitleg="De stam speel eindigt op een l, en die zit niet in 't kofschip. Dus -de en niet -te.",
        ),
        dict(
            vraag="Wat is de verleden tijd van 'horen'?",
            opties=["hoorde", "hoorte", "hoort", "gehoord"],
            antwoord=0,
            uitleg="De stam hoor eindigt op een r, en die zit niet in 't kofschip. Dus -de en niet -te.",
        ),
        dict(
            vraag="Wat is de verleden tijd van 'bouwen'?",
            opties=["bouwde", "bouwte", "bouwt", "gebouwd"],
            antwoord=0,
            uitleg="De stam bouw eindigt op een w, en die zit niet in 't kofschip. Dus -de en niet -te.",
        ),
        dict(
            vraag="Wat is de verleden tijd van 'delen'?",
            opties=["deelde", "deelte", "deelt", "gedeeld"],
            antwoord=0,
            uitleg="De stam deel eindigt op een l, en die zit niet in 't kofschip. Dus -de en niet -te.",
        ),
    ],
    "Welke voltooide deelwoorden zijn juist?": [
        dict(
            vraag="Welke voltooide deelwoorden zijn juist?",
            opties=["gestapt", "gehoord", "gelachen", "gebouwdt"],
            antwoord=[0, 1, 2],
            uitleg="Stap zit in 't kofschip, dus gestapt met een t. Hoor niet, dus gehoord met een d. Lachen is sterk: gelachen. Gebouwdt bestaat niet: nooit -dt achter een voltooid deelwoord.",
        ),
        dict(
            vraag="Welke voltooide deelwoorden zijn juist?",
            opties=["gefietst", "gespeeld", "gedeeld", "geleerdt"],
            antwoord=[0, 1, 2],
            uitleg="Fiets zit in 't kofschip, dus gefietst met een t. Speel en deel niet, dus met een d. Geleerdt bestaat niet: nooit -dt achter een voltooid deelwoord.",
        ),
        dict(
            vraag="Welke voltooide deelwoorden zijn juist?",
            opties=["geblaft", "gebouwd", "gewerkt", "gehoordt"],
            antwoord=[0, 1, 2],
            uitleg="Blaf zit in 't kofschip, dus geblaft. Bouw niet, dus gebouwd. Werk zit er weer wel in, dus gewerkt. Gehoordt bestaat niet.",
        ),
    ],
    "Welk woord heeft een lange klank?": [
        dict(
            vraag="Welk woord heeft een lange klank?",
            opties=["boom", "bom", "kip", "pet"],
            antwoord=0,
            uitleg="Twee gelijke klinkers in een gesloten lettergreep geven de lange klank: boom. Bij bom, kip en pet hoor je de korte.",
        ),
        dict(
            vraag="Welk woord heeft een lange klank?",
            opties=["muur", "mus", "kar", "bel"],
            antwoord=0,
            uitleg="Twee gelijke klinkers in een gesloten lettergreep geven de lange klank: muur. Bij mus, kar en bel hoor je de korte.",
        ),
        dict(
            vraag="Welk woord heeft een lange klank?",
            opties=["peer", "pen", "rok", "vis"],
            antwoord=0,
            uitleg="Twee gelijke klinkers in een gesloten lettergreep geven de lange klank: peer. Bij pen, rok en vis hoor je de korte.",
        ),
        dict(
            vraag="Welk woord heeft een lange klank?",
            opties=["raam", "ram", "bus", "top"],
            antwoord=0,
            uitleg="Twee gelijke klinkers in een gesloten lettergreep geven de lange klank: raam. Bij ram, bus en top hoor je de korte.",
        ),
    ],
    "Wat is het meervoud van 'man'?": [
        dict(
            vraag="Wat is het meervoud van 'kat'?",
            opties=["katten", "katen", "kats", "kattens"],
            antwoord=0,
            uitleg="De korte klank blijft kort, dus de medeklinker wordt verdubbeld: katten. Met één t zou je 'katen' lezen, met een lange aa.",
        ),
        dict(
            vraag="Wat is het meervoud van 'pot'?",
            opties=["potten", "poten", "pots", "pottens"],
            antwoord=0,
            uitleg="De korte klank blijft kort, dus de medeklinker wordt verdubbeld: potten. 'Poten' is het meervoud van poot, met een lange oo.",
        ),
        dict(
            vraag="Wat is het meervoud van 'bus'?",
            opties=["bussen", "busen", "bus'en", "bussens"],
            antwoord=0,
            uitleg="De korte klank blijft kort, dus de medeklinker wordt verdubbeld: bussen.",
        ),
        dict(
            vraag="Wat is het meervoud van 'vis'?",
            opties=["vissen", "visen", "vis's", "vissens"],
            antwoord=0,
            uitleg="De korte klank blijft kort, dus de medeklinker wordt verdubbeld: vissen.",
        ),
    ],
    "Het meervoud van 'maan' is ___.": [
        dict(vraag="Het meervoud van 'boom' is ___.", antwoord="bomen",
             uitleg="De lange klank blijft lang in een open lettergreep, dus valt er één o weg: bo-men."),
        dict(vraag="Het meervoud van 'raam' is ___.", antwoord="ramen",
             uitleg="De lange klank blijft lang in een open lettergreep, dus valt er één a weg: ra-men."),
        dict(vraag="Het meervoud van 'peer' is ___.", antwoord="peren",
             uitleg="De lange klank blijft lang in een open lettergreep, dus valt er één e weg: pe-ren."),
        dict(vraag="Het meervoud van 'muur' is ___.", antwoord="muren",
             uitleg="De lange klank blijft lang in een open lettergreep, dus valt er één u weg: mu-ren."),
    ],
    "Welke woorden schrijf je met een hoofdletter?": [
        dict(
            vraag="Welke woorden schrijf je met een hoofdletter?",
            opties=["Frans", "Parijs", "Europa", "dinsdag"],
            antwoord=[0, 1, 2],
            uitleg="Talen, steden en werelddelen krijgen een hoofdletter. Dagen van de week niet, in het Nederlands.",
        ),
        dict(
            vraag="Welke woorden schrijf je met een hoofdletter?",
            opties=["Duits", "Hasselt", "Afrika", "zomer"],
            antwoord=[0, 1, 2],
            uitleg="Talen, steden en werelddelen krijgen een hoofdletter. Seizoenen niet.",
        ),
        dict(
            vraag="Welke woorden schrijf je met een hoofdletter?",
            opties=["Engels", "Limburg", "Azië", "januari"],
            antwoord=[0, 1, 2],
            uitleg="Talen, provincies en werelddelen krijgen een hoofdletter. Maanden niet, in het Nederlands.",
        ),
        dict(
            vraag="Welke woorden schrijf je met een hoofdletter?",
            opties=["Spaans", "Gent", "België", "woensdag"],
            antwoord=[0, 1, 2],
            uitleg="Talen, steden en landen krijgen een hoofdletter. Dagen van de week niet.",
        ),
    ],
    "De twee puntjes op de e in 'zeeën' heten een ___.": [
        dict(vraag="De twee puntjes op de e in 'knieën' heten een ___.", antwoord="trema",
             uitleg="Een trema zegt dat je hier opnieuw moet beginnen lezen, zodat je knie-ën leest en niet 'knieen'."),
        dict(vraag="De twee puntjes op de e in 'reeën' heten een ___.", antwoord="trema",
             uitleg="Een trema zegt dat je hier opnieuw moet beginnen lezen, zodat je ree-ën leest."),
        dict(vraag="De twee puntjes op de e in 'België' heten een ___.", antwoord="trema",
             uitleg="Een trema zegt dat je hier opnieuw moet beginnen lezen, zodat je Bel-gi-ë leest en niet 'Belgie'."),
        dict(vraag="De twee puntjes op de e in 'poëzie' heten een ___.", antwoord="trema",
             uitleg="Een trema zegt dat je hier opnieuw moet beginnen lezen, zodat je po-ë-zie leest en niet 'poe'."),
    ],
    "Welke woorden schrijf je met een apostrof in het meervoud?": [
        dict(
            vraag="Welke woorden schrijf je met een apostrof in het meervoud?",
            opties=["auto's", "menu's", "paraplu's", "tafels"],
            antwoord=[0, 1, 2],
            uitleg="Eindigt een woord op een losse a, i, o, u of y, dan komt er een apostrof voor de meervouds-s, anders lees je de klank verkeerd. Tafel eindigt daar niet op.",
        ),
        dict(
            vraag="Welke woorden schrijf je met een apostrof in het meervoud?",
            opties=["pyjama's", "ski's", "ruzie's", "boeken"],
            antwoord=[0, 1],
            uitleg="Pyjama en ski eindigen op een losse a en i, dus komt er een apostrof. Ruzie eindigt op een e en wordt ruzies, en boek krijgt gewoon -en.",
        ),
        dict(
            vraag="Welke woorden schrijf je met een apostrof in het meervoud?",
            opties=["baby's", "hobby's", "pony's", "stoelen"],
            antwoord=[0, 1, 2],
            uitleg="Eindigt een woord op een losse y, dan komt er een apostrof voor de meervouds-s. Stoel eindigt daar niet op.",
        ),
    ],
    "Waarom schrijf je 'zee-eend' met een koppelteken?": [
        dict(
            vraag="Waarom schrijf je 'na-apen' met een koppelteken?",
            opties=[
                "Omdat er anders drie a's botsen en je het woord verkeerd leest",
                "Omdat het twee werkwoorden zijn",
                "Omdat het een lang woord is",
                "Omdat het een eigennaam is",
            ],
            antwoord=0,
            uitleg="Klinkers die tegen elkaar botsen, krijgen een koppelteken. 'Naapen' zou je als één klank lezen.",
        ),
        dict(
            vraag="Waarom schrijf je 'zo-even' met een koppelteken?",
            opties=[
                "Omdat de o en de e anders als één klank gelezen worden",
                "Omdat het over tijd gaat",
                "Omdat het een lang woord is",
                "Omdat het een eigennaam is",
            ],
            antwoord=0,
            uitleg="Klinkers die tegen elkaar botsen, krijgen een koppelteken. 'Zoeven' zou je als 'zoe-ven' lezen.",
        ),
        dict(
            vraag="Waarom schrijf je 'auto-ongeluk' met een koppelteken?",
            opties=[
                "Omdat de o's anders tegen elkaar botsen en je het woord verkeerd leest",
                "Omdat het twee zelfstandige naamwoorden zijn",
                "Omdat het een lang woord is",
                "Omdat het een eigennaam is",
            ],
            antwoord=0,
            uitleg="Klinkers die tegen elkaar botsen, krijgen een koppelteken. 'Autoongeluk' leest niemand vlot.",
        ),
        dict(
            vraag="Waarom schrijf je 'mede-eigenaar' met een koppelteken?",
            opties=[
                "Omdat de e's anders tegen elkaar botsen en je het woord verkeerd leest",
                "Omdat er twee eigenaars zijn",
                "Omdat het een lang woord is",
                "Omdat het een eigennaam is",
            ],
            antwoord=0,
            uitleg="Klinkers die tegen elkaar botsen, krijgen een koppelteken. 'Medeeigenaar' zou je verkeerd lezen.",
        ),
    ],
    # ── deel 2 ──────────────────────────────────────────────────────────────
    "Welke zin over iets van gisteren is juist?": [
        dict(
            vraag="Welke zin over iets van gisteren is juist?",
            opties=[
                "Hij heeft het gisteren beloofd.",
                "Hij heeft het gisteren belooft.",
                "Hij heeft het gisteren beloofdt.",
                "Hij heeft het gisteren beloven.",
            ],
            antwoord=0,
            uitleg="Het is een voltooid deelwoord. De stam beloof eindigt niet op een klank uit 't kofschip, dus -d: beloofd. Nooit -dt.",
        ),
        dict(
            vraag="Welke zin over iets van gisteren is juist?",
            opties=[
                "Wij zijn vorig jaar verhuisd.",
                "Wij zijn vorig jaar verhuist.",
                "Wij zijn vorig jaar verhuisdt.",
                "Wij zijn vorig jaar verhuizen.",
            ],
            antwoord=0,
            uitleg="Het is een voltooid deelwoord van verhuizen. De z van de infinitief wordt een d in het deelwoord: verhuisd.",
        ),
        dict(
            vraag="Welke zin over iets van gisteren is juist?",
            opties=[
                "Zij heeft alles geregeld.",
                "Zij heeft alles geregelt.",
                "Zij heeft alles geregeldt.",
                "Zij heeft alles regelen.",
            ],
            antwoord=0,
            uitleg="Het is een voltooid deelwoord. De stam regel eindigt op een l, die niet in 't kofschip zit, dus -d: geregeld.",
        ),
    ],
    "Welke zin over iets dat zich herhaalt, is juist?": [
        dict(
            vraag="Welke zin over iets dat zich herhaalt, is juist?",
            opties=[
                "Hij belooft het elke keer opnieuw.",
                "Hij beloofd het elke keer opnieuw.",
                "Hij beloofdt het elke keer opnieuw.",
                "Hij beloven het elke keer opnieuw.",
            ],
            antwoord=0,
            uitleg="Tegenwoordige tijd bij hij: stam beloof plus -t. Het voltooid deelwoord beloofd hoort bij 'heeft', niet hier.",
        ),
        dict(
            vraag="Welke zin over iets dat zich herhaalt, is juist?",
            opties=[
                "Zij regelt dat elke maand zelf.",
                "Zij regeld dat elke maand zelf.",
                "Zij regeldt dat elke maand zelf.",
                "Zij regelen dat elke maand zelf.",
            ],
            antwoord=0,
            uitleg="Tegenwoordige tijd bij zij: stam regel plus -t. Het voltooid deelwoord geregeld hoort bij 'heeft'.",
        ),
        dict(
            vraag="Welke zin over iets dat zich herhaalt, is juist?",
            opties=[
                "Hij verhuist bijna elk jaar.",
                "Hij verhuisd bijna elk jaar.",
                "Hij verhuisdt bijna elk jaar.",
                "Hij verhuizen bijna elk jaar.",
            ],
            antwoord=0,
            uitleg="Tegenwoordige tijd bij hij: stam verhuis plus -t. Het voltooid deelwoord verhuisd hoort bij 'is'.",
        ),
    ],
    "Vul in met de juiste vorm van 'vinden': Wat ___ jij daarvan?": [
        dict(vraag="Vul in met de juiste vorm van 'worden': Wat ___ jij later?", antwoord="word",
             uitleg="Staat 'jij' áchter het werkwoord, dan valt de -t weg. Vóór het werkwoord zou het 'jij wordt' zijn."),
        dict(vraag="Vul in met de juiste vorm van 'houden': Waarvan ___ jij het meest?", antwoord="houd",
             uitleg="Staat 'jij' áchter het werkwoord, dan valt de -t weg. Vóór het werkwoord zou het 'jij houdt' zijn."),
        dict(vraag="Vul in met de juiste vorm van 'rijden': Waarheen ___ jij morgen?", antwoord="rijd",
             uitleg="Staat 'jij' áchter het werkwoord, dan valt de -t weg. Vóór het werkwoord zou het 'jij rijdt' zijn."),
        dict(vraag="Vul in met de juiste vorm van 'antwoorden': Wat ___ jij daarop?", antwoord="antwoord",
             uitleg="Staat 'jij' áchter het werkwoord, dan valt de -t weg. Vóór het werkwoord zou het 'jij antwoordt' zijn."),
    ],
    "Welke zin met het werkwoord 'antwoorden' is juist?": [
        dict(
            vraag="Welke zin met het werkwoord 'branden' is juist?",
            opties=[
                "Het licht brandt nog altijd.",
                "Het licht brand nog altijd.",
                "Het licht brandde vroeger ook al de hele nacht door.",
                "Het licht brandt gisteren nog.",
            ],
            antwoord=0,
            uitleg="Stam brand plus -t bij het: brandt. De derde zin is juist gespeld maar staat in de verleden tijd, de vierde mengt een tegenwoordige vorm met 'gisteren'.",
        ),
        dict(
            vraag="Welke zin met het werkwoord 'houden' is juist?",
            opties=[
                "Zij houdt niet van wachten.",
                "Zij houd niet van wachten.",
                "Zij hield vroeger ook al helemaal niet van lang wachten.",
                "Zij houdt gisteren de deur open.",
            ],
            antwoord=0,
            uitleg="Stam houd plus -t bij zij: houdt. De derde zin is juist gespeld maar staat in de verleden tijd, de vierde mengt een tegenwoordige vorm met 'gisteren'.",
        ),
        dict(
            vraag="Welke zin met het werkwoord 'rijden' is juist?",
            opties=[
                "Hij rijdt elke dag met de bus.",
                "Hij rijd elke dag met de bus.",
                "Hij reed vroeger elke dag helemaal alleen met de bus naar school.",
                "Hij rijdt gisteren met de bus.",
            ],
            antwoord=0,
            uitleg="Stam rijd plus -t bij hij: rijdt. De derde zin is juist gespeld maar staat in de verleden tijd, de vierde mengt een tegenwoordige vorm met 'gisteren'.",
        ),
    ],
    "Welk meervoud is juist?": [
        dict(
            vraag="Welk meervoud is juist?",
            opties=["zeeën", "zeeen", "zee's", "zeën"],
            antwoord=0,
            uitleg="Een trema op de e zegt dat je opnieuw moet beginnen lezen: zee-ën. Zonder trema lees je 'zeeen' als één brij.",
        ),
        dict(
            vraag="Welk meervoud is juist?",
            opties=["ideeën", "ideeen", "idee's", "ideën"],
            antwoord=0,
            uitleg="Een trema op de e zegt dat je opnieuw moet beginnen lezen: idee-ën.",
        ),
        dict(
            vraag="Welk meervoud is juist?",
            opties=["reeën", "reeen", "ree's", "reën"],
            antwoord=0,
            uitleg="Een trema op de e zegt dat je opnieuw moet beginnen lezen: ree-ën.",
        ),
    ],
    "Welk verkleinwoord is juist?": [
        dict(
            vraag="Welk verkleinwoord is juist?",
            opties=["hobby'tje", "hobbytje", "hobby-tje", "hobbietje"],
            antwoord=0,
            uitleg="Een woord dat op een losse y eindigt, krijgt een apostrof voor het verkleinwoord, anders lees je de y verkeerd.",
        ),
        dict(
            vraag="Welk verkleinwoord is juist?",
            opties=["pony'tje", "ponytje", "pony-tje", "ponietje"],
            antwoord=0,
            uitleg="Een woord dat op een losse y eindigt, krijgt een apostrof voor het verkleinwoord.",
        ),
        dict(
            vraag="Welk verkleinwoord is juist?",
            opties=["ski'tje", "skitje", "ski-tje", "skietje"],
            antwoord=0,
            uitleg="Een woord dat op een losse i eindigt, krijgt een apostrof voor het verkleinwoord, anders lees je de i kort.",
        ),
    ],
    "Welke zin met 'liggen' of 'leggen' is juist?": [
        dict(
            vraag="Welke zin met 'liggen' of 'leggen' is juist?",
            opties=[
                "De krant ligt op tafel.",
                "De krant legt op tafel.",
                "De krant liggt op tafel.",
                "De krant leggt op tafel.",
            ],
            antwoord=0,
            uitleg="Liggen is waar iets zelf is, leggen is iets ergens neerzetten. De stam is lig, dus ligt met één g.",
        ),
        dict(
            vraag="Welke zin met 'liggen' of 'leggen' is juist?",
            opties=[
                "Hij legt zijn jas over de stoel.",
                "Hij ligt zijn jas over de stoel.",
                "Hij leggt zijn jas over de stoel.",
                "Hij liggt zijn jas over de stoel.",
            ],
            antwoord=0,
            uitleg="Hier doet hij iets mét de jas, dus leggen. De stam is leg, dus legt met één g.",
        ),
        dict(
            vraag="Welke zin met 'liggen' of 'leggen' is juist?",
            opties=[
                "De hond ligt voor de haard.",
                "De hond legt voor de haard.",
                "De hond liggt voor de haard.",
                "De hond leggt voor de haard.",
            ],
            antwoord=0,
            uitleg="De hond is er gewoon, hij zet niets neer, dus liggen. De stam is lig, dus ligt met één g.",
        ),
    ],
    "Waarom schrijf je 'hij verwacht' zonder extra t?": [
        dict(
            vraag="Waarom schrijf je 'hij wacht' zonder extra t?",
            opties=[
                "Omdat de stam al op een t eindigt",
                "Omdat het een kort woord is",
                "Omdat het een uitzondering is",
                "Omdat er geen voorvoegsel voor staat",
            ],
            antwoord=0,
            uitleg="De stam is wacht. Er komt wel een -t bij, maar je schrijft nooit twee t's na elkaar.",
        ),
        dict(
            vraag="Waarom schrijf je 'hij praat' zonder extra t?",
            opties=[
                "Omdat de stam al op een t eindigt",
                "Omdat het een kort woord is",
                "Omdat het een uitzondering is",
                "Omdat er geen voorvoegsel voor staat",
            ],
            antwoord=0,
            uitleg="De stam is praat. Er komt wel een -t bij, maar je schrijft nooit twee t's na elkaar.",
        ),
        dict(
            vraag="Waarom schrijf je 'hij zit' zonder extra t?",
            opties=[
                "Omdat de stam al op een t eindigt",
                "Omdat het een kort woord is",
                "Omdat het een uitzondering is",
                "Omdat er geen voorvoegsel voor staat",
            ],
            antwoord=0,
            uitleg="De stam is zit. Er komt wel een -t bij, maar je schrijft nooit twee t's na elkaar.",
        ),
    ],
}

for _lijst in (DEEL1, DEEL2):
    for _vraag in _lijst:
        _extra = VARIANTEN.get(_vraag["vraag"])
        if _extra:
            _vraag["varianten"] = _extra

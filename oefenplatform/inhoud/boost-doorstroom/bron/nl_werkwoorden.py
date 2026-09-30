# -*- coding: utf-8 -*-
"""De vragen voor "Werkwoorden, tijden en woordvorming" (🚀 Boost doorstroom, Nederlands).

Uit het morfologisch domein van allebei de vakfiches: het werkwoord met zijn
soorten (zelfstandig, hulp- en koppelwerkwoord), het voltooid deelwoord en de
infinitief, de zes werkwoordstijden en de imperatief, en daarnaast de
woordvorming: samenstellingen en afleidingen, voor- en achtervoegsel, stam,
uitgang, tussenklank, meervoud, verkleinwoord, verbuiging en vervoeging.

Deel 1 is het werkwoord. Deel 2 is de woordvorming.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="In welke tijd staat 'Ik had de hele dag gelopen'?",
        opties=[
            "voltooid verleden tijd",
            "voltooid tegenwoordige tijd",
            "onvoltooid verleden tijd",
            "onvoltooid toekomende tijd",
        ],
        antwoord=0,
        uitleg="Voltooid omdat er een deelwoord staat, verleden omdat het hulpwerkwoord 'had' in de verleden tijd staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze werkwoordstijden bestaan?",
        opties=[
            "onvoltooid tegenwoordige tijd",
            "voltooid verleden tijd",
            "onvoltooid toekomende tijd",
            "gebiedende toekomende tijd",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt zes tijden plus de imperatief. Een gebiedende toekomende tijd bestaat niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de vorm 'lopen', zonder persoon en zonder tijd?",
        antwoord=["infinitief", "de infinitief", "het hele werkwoord"],
        uitleg="De infinitief is de vorm die in het woordenboek staat. Alle andere vormen leid je ervan af.",
    ),
    dict(
        type="waarofniet",
        vraag="De imperatief is de aanvoegende wijs.",
        antwoord=False,
        uitleg="De imperatief is de gebiedende wijs: 'Kom hier', 'Let op'. Hij heeft geen onderwerp bij zich.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'Zij wordt verpleegkundige', welk soort werkwoord is 'wordt'?",
        opties=[
            "een koppelwerkwoord",
            "een zelfstandig werkwoord",
            "een hulpwerkwoord van de lijdende vorm",
            "een wederkerend werkwoord",
        ],
        antwoord=0,
        uitleg="Het koppelt het onderwerp aan een naamwoord dat iets over dat onderwerp zegt. Samen heet dat een naamwoordelijk gezegde.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'Hij heeft zijn boterhammen opgegeten', wat is 'heeft'?",
        opties=[
            "een hulpwerkwoord",
            "een koppelwerkwoord",
            "een zelfstandig werkwoord",
            "een voltooid deelwoord",
        ],
        antwoord=0,
        uitleg="'Heeft' helpt hier de voltooide tijd vormen. In 'Hij heeft een fiets' is hetzelfde woord wel zelfstandig werkwoord.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het werkwoord dat in persoon en getal met het onderwerp meegaat?",
        antwoord=["persoonsvorm", "de persoonsvorm"],
        uitleg="De persoonsvorm verandert als je de zin in een andere tijd zet. Zo vind je hem terug.",
    ),
    dict(
        type="waarofniet",
        vraag="In elke deelzin staat precies één persoonsvorm.",
        antwoord=True,
        uitleg="Een samengestelde zin heeft er dus meerdere: één per hoofdzin en één per bijzin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze werkwoorden kunnen koppelwerkwoord zijn?",
        opties=["zijn", "worden", "blijven", "lopen"],
        antwoord=[0, 1, 2],
        uitleg="De koppelwerkwoorden zijn zijn, worden, blijven, blijken, lijken, schijnen, heten, dunken en voorkomen. 'Lopen' hoort er niet bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vind je de persoonsvorm in een zin terug?",
        opties=[
            "je zet de zin in een andere tijd en kijkt welk werkwoord verandert",
            "je neemt altijd het eerste werkwoord van de zin",
            "je neemt altijd het langste werkwoord van de zin",
            "je neemt het werkwoord dat achteraan staat",
        ],
        antwoord=0,
        uitleg="'Hij heeft gelopen' wordt 'Hij had gelopen'. Alleen 'heeft' verandert, dus dat is de persoonsvorm.",
    ),
    dict(
        type="waarofniet",
        vraag="De stam van een werkwoord is hetzelfde als de infinitief.",
        antwoord=False,
        uitleg="De stam krijg je door -en van de infinitief te halen: wandelen wordt wandel. Daarop bouw je de vervoeging.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke tijd staat 'Wij werkten de hele zomer'?",
        opties=[
            "onvoltooid verleden tijd",
            "voltooid verleden tijd",
            "onvoltooid tegenwoordige tijd",
            "voltooid tegenwoordige tijd",
        ],
        antwoord=0,
        uitleg="Er staat geen deelwoord bij, dus onvoltooid. De vorm 'werkten' is verleden tijd.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het stukje dat achter de stam komt, zoals de -t in 'hij werkt'?",
        antwoord=["de uitgang", "uitgang"],
        uitleg="Stam plus uitgang samen vormen de vervoegde vorm. De uitgang draagt de persoon en het getal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is 'De doos met oude boeken staan in de gang' fout?",
        opties=[
            "het onderwerp is enkelvoud, dus de persoonsvorm ook",
            "'met' mag niet voor een meervoud staan",
            "'oude' moet 'oud' zijn zonder e",
            "de zin heeft geen lijdend voorwerp",
        ],
        antwoord=0,
        uitleg="Het onderwerp is 'de doos', niet 'boeken'. Dat heet congruentie tussen onderwerp en persoonsvorm.",
    ),
    dict(
        type="waarofniet",
        vraag="Het voltooid deelwoord van een zwak werkwoord eindigt op -d of -t.",
        antwoord=True,
        uitleg="Gewerkt, gehoord, gebeld. Sterke werkwoorden veranderen van klinker: gelopen, gezongen, gevonden.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke tijd staat 'Zij zal morgen komen'?",
        opties=[
            "onvoltooid toekomende tijd",
            "voltooid toekomende tijd",
            "onvoltooid tegenwoordige tijd",
            "voltooid tegenwoordige tijd",
        ],
        antwoord=0,
        uitleg="'Zullen' plus infinitief maakt de toekomende tijd. Er staat geen deelwoord bij, dus onvoltooid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vormen zijn voltooide deelwoorden?",
        opties=["gewerkt", "gelopen", "gezien", "werken"],
        antwoord=[0, 1, 2],
        uitleg="'Werken' is de infinitief. De drie andere beginnen met ge- en horen bij een voltooide tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zin is correct gespeld?",
        opties=[
            "Hij wordt morgen zestien jaar.",
            "Hij word morgen zestien jaar.",
            "Hij wordt morgen zestien jaar geworden.",
            "Hij worden morgen zestien jaar.",
        ],
        antwoord=0,
        uitleg="Derde persoon enkelvoud krijgt stam plus t: word plus t wordt 'wordt'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vraagzin is correct gespeld?",
        opties=[
            "Word jij daar niet moe van?",
            "Wordt jij daar niet moe van?",
            "Wordt jou daar niet moe van?",
            "Word jou daar niet moe van?",
        ],
        antwoord=0,
        uitleg="Bij 'je' of 'jij' achter de persoonsvorm valt de -t weg. Dat heet inversie.",
    ),
    dict(
        type="meerkeuze",
        vraag="In 'Ik heb het boek helemaal uitgelezen', welk werkwoord is het zelfstandig werkwoord?",
        opties=["uitgelezen", "heb", "het", "helemaal"],
        antwoord=0,
        uitleg="'Heb' is hier alleen hulpwerkwoord. De betekenis van de zin zit in 'uitgelezen'.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat voor woord is 'boekenkast'?",
        opties=[
            "een samenstelling",
            "een afleiding",
            "een verkleinwoord",
            "een leenwoord",
        ],
        antwoord=0,
        uitleg="Twee bestaande woorden, boek en kast, worden aan elkaar geschreven. Dat is een samenstelling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat voor woord is 'onvriendelijk'?",
        opties=[
            "een afleiding",
            "een samenstelling",
            "een verkleinwoord",
            "een tussenwerpsel",
        ],
        antwoord=0,
        uitleg="'On-' is geen zelfstandig woord maar een voorvoegsel. Een woord dat met een voor- of achtervoegsel gevormd is, heet een afleiding.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de -en- in het midden van 'pannenkoek'?",
        antwoord=["tussenklank", "de tussenklank", "tussenletters"],
        uitleg="De tussenklank lijmt de twee delen van een samenstelling aan elkaar. Hij hoort bij geen van beide woorden apart.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een samenstelling zet je twee bestaande woorden aan elkaar.",
        antwoord=True,
        uitleg="Allebei de delen kunnen los bestaan: tafel en poot, voetbal en veld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke woorden zijn samenstellingen?",
        opties=["tafelpoot", "voetbalveld", "regenjas", "vriendelijk"],
        antwoord=[0, 1, 2],
        uitleg="'Vriendelijk' is gevormd met het achtervoegsel -lijk en is dus een afleiding.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het voorvoegsel in 'herlezen'?",
        opties=["her-", "-lezen", "-en", "le-"],
        antwoord=0,
        uitleg="'Her-' betekent opnieuw. Het kan niet alleen staan, dus het is een voorvoegsel en geen woord.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het stukje achteraan een woord dat er een nieuw woord van maakt, zoals -heid en -baar?",
        antwoord=["achtervoegsel", "een achtervoegsel", "suffix"],
        uitleg="Schoon wordt schoonheid, lees wordt leesbaar. Het woord verandert van woordsoort of van betekenis.",
    ),
    dict(
        type="waarofniet",
        vraag="'Onmogelijk' is een samenstelling.",
        antwoord=False,
        uitleg="Het is een afleiding: er komt een voorvoegsel bij een bestaand woord. Bij een samenstelling zijn allebei de delen zelfstandige woorden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke meervouden zijn correct?",
        opties=["kinderen", "paden", "leden", "stoelens"],
        antwoord=[0, 1, 2],
        uitleg="Het meervoud van stoel is stoelen. Een meervoud op -s krijgt nooit nog eens -en erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verkleinwoord van 'koning'?",
        opties=["koninkje", "koningje", "koningtje", "koningetje"],
        antwoord=0,
        uitleg="Na -ing wordt de g een k en volgt -je. Dezelfde regel geldt bij woning en leerling.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle Nederlandse meervouden eindigen op -en of -s.",
        antwoord=False,
        uitleg="Er zijn uitzonderingen zoals musea, kinderen met een tussenvoeging, en eieren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schrijf je 'een mooi huis' maar 'het mooie huis'?",
        opties=[
            "omdat het bijvoeglijk naamwoord verbogen wordt",
            "omdat het bijvoeglijk naamwoord vervoegd wordt",
            "omdat 'huis' in het tweede geval meervoud is",
            "omdat de tweede zin in de verleden tijd staat",
        ],
        antwoord=0,
        uitleg="Verbuiging is de vormverandering van naamwoorden en bijvoeglijke naamwoorden. Vervoeging is hetzelfde, maar dan bij werkwoorden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het aanpassen van een werkwoord aan persoon, getal en tijd?",
        antwoord=["vervoeging", "de vervoeging", "vervoegen"],
        uitleg="Ik werk, jij werkt, wij werkten: telkens dezelfde stam, telkens een andere vervoeging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een samenstelling en een afleiding?",
        opties=[
            "bij een samenstelling kunnen beide delen los bestaan, bij een afleiding niet",
            "een samenstelling is altijd langer dan een afleiding",
            "een samenstelling komt alleen bij naamwoorden voor",
            "een afleiding wordt altijd met een koppelteken geschreven",
        ],
        antwoord=0,
        uitleg="Deurklink bestaat uit deur en klink, allebei echte woorden. Leesbaar bestaat uit lees plus -baar, en -baar is geen woord.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een afleiding komt er een voor- of achtervoegsel bij een bestaand woord.",
        antwoord=True,
        uitleg="Ver- plus dwalen wordt verdwalen, schoon plus -heid wordt schoonheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welk woord zit een tussenklank?",
        opties=["pannenkoek", "tafelpoot", "schoolbord", "raamkozijn"],
        antwoord=0,
        uitleg="Tussen pan en koek staat -en-. De drie andere samenstellingen plakken de twee delen rechtstreeks aan elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke woorden zijn afleidingen?",
        opties=["schoonheid", "leesbaar", "ontdekken", "deurklink"],
        antwoord=[0, 1, 2],
        uitleg="Deurklink is een samenstelling van twee echte woorden. De drie andere gebruiken een voor- of achtervoegsel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit hoeveel woorden is 'schoonmaakbedrijf' samengesteld?",
        opties=["drie", "twee", "vier", "één"],
        antwoord=0,
        uitleg="Schoon, maak en bedrijf. Samenstellingen kunnen uit meer dan twee delen bestaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het meervoud van 'lid'?",
        opties=["leden", "lidden", "lids", "lidderen"],
        antwoord=0,
        uitleg="Een handvol woorden verandert van klinker in het meervoud: lid wordt leden, schip wordt schepen, stad wordt steden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk woord is géén samenstelling?",
        opties=["vriendelijkheid", "boekenkast", "voetbalveld", "regenjas"],
        antwoord=0,
        uitleg="Vriendelijkheid is twee keer afgeleid: vriend wordt vriendelijk, vriendelijk wordt vriendelijkheid. Er komt geen tweede woord bij.",
    ),
]

# -*- coding: utf-8 -*-
"""Klank, klemtoon, intonatie en de spelling van frequente woorden.

De vakfiche van dubbele finaliteit zet onder de grammatica een rij die op de
doorstroomfiches niet zo staat: fonologische elementen en spelling. Zes dingen
horen erbij:

    uitspraak van klanken en klankencombinaties
    gebruik van woordaccent
    articulatie
    intonatie
    relatie klank- en schriftbeeld
    spelling van frequente woorden

Vijf daarvan gaan over geluid, en geluid kan dit platform niet maken. Wat het
wél kan, is alles wat je erover moet wéten en wat je aan het schriftbeeld kan
zien: op welke lettergreep de klemtoon valt, welke letters je niet hoort,
wanneer -ed een extra lettergreep wordt, welke woorden hetzelfde klinken maar
anders geschreven worden, en hoe de spelling van de frequente woorden gaat.
Het horen zelf oefen je met de luisterfragmenten van je methode.

Deel 1 gaat over klank en klemtoon. Deel 2 gaat over spelling.

Het ERK-niveau is A2, dus het blijven frequente woorden.
"""

DEEL1 = [
    dict(type="meerkeuze",
         vraag="Op welke lettergreep ligt de klemtoon in 'computer'?",
         opties=["op de tweede: com-PU-ter",
                 "op de eerste: COM-pu-ter",
                 "op de derde: com-pu-TER",
                 "er ligt geen klemtoon op"],
         antwoord=0,
         uitleg="Het Engels legt de klemtoon hier op PU. Leg je ze op COM, dan klinkt het woord "
                "voor een Engelstalige meteen vreemd."),
    dict(type="meerkeuze",
         vraag="In welke woorden ligt de klemtoon op de eerste lettergreep?",
         opties=["table", "water", "open", "about"],
         antwoord=[0, 1, 2],
         uitleg="TA-ble, WA-ter en O-pen hebben de klemtoon vooraan. In a-BOUT ligt ze op de "
                "tweede lettergreep."),
    dict(type="invultekst",
         vraag="In 'knee' schrijf je een letter die je niet hoort. Welke letter is dat?",
         antwoord=["k", "de k"],
         uitleg="De k van knee, knife en know hoor je niet. Je ziet hem wel staan, en dat is "
                "precies wat met klank- en schriftbeeld bedoeld wordt."),
    dict(type="meerkeuze",
         vraag="In welk woord hoor je de eerste letter niet?",
         opties=["hour", "house", "happy", "hotel"],
         antwoord=0,
         uitleg="'Hour' begint met een klinkerklank, daarom zeg je ook 'an hour'. In house, happy "
                "en hotel hoor je de h wel."),
    dict(type="waarofniet",
         vraag="Het woord 'island' heeft een letter die je niet uitspreekt.",
         antwoord=True,
         uitleg="De s van island hoor je niet. Zo zijn er meer: listen, castle, half en talk."),
    dict(type="meerkeuze",
         vraag="Hoe klinkt de -ed van 'wanted'?",
         opties=["als een extra lettergreep: want-id",
                 "als een korte t achter want",
                 "als een korte d achter want",
                 "je hoort de -ed helemaal niet"],
         antwoord=0,
         uitleg="Na een t of een d wordt -ed een lettergreep op zich. Daarom heeft 'wanted' twee "
                "lettergrepen en 'worked' er maar één."),
    dict(type="meerkeuze",
         vraag="Bij welke werkwoorden spreek je de -ed uit als een extra lettergreep?",
         opties=["wanted", "needed", "started", "played"],
         antwoord=[0, 1, 2],
         uitleg="Wanted, needed en started eindigen op een t- of d-klank, dus komt er een "
                "lettergreep bij. 'Played' blijft één lettergreep."),
    dict(type="meerkeuze",
         vraag="Hoe klinkt de meervouds-s in 'dogs'?",
         opties=["als een z", "als een s", "als een extra lettergreep", "je hoort ze niet"],
         antwoord=0,
         uitleg="Na een stemhebbende klank klinkt de s als een z: dogs, pens, cars. Na een "
                "stemloze klank blijft ze een s: cats, books, cups."),
    dict(type="invultekst",
         vraag="Hoeveel lettergrepen hoor je in 'boxes'? Antwoord met een getal.",
         antwoord=["2", "twee"],
         uitleg="Box heeft er één, boxes heeft er twee. Na een sisklank komt de meervouds-s er als "
                "een eigen lettergreep bij."),
    dict(type="waarofniet",
         vraag="Bij een vraag die je met yes of no beantwoordt, gaat je stem aan het eind omhoog.",
         antwoord=True,
         uitleg="Dat is intonatie. 'Are you coming?' eindigt hoger; 'Where are you going?' eindigt "
                "net wat lager."),
    dict(type="meerkeuze",
         vraag="Wat wordt er met intonatie bedoeld?",
         opties=["hoe je stem stijgt en daalt in een zin",
                 "hoe luid je een hele zin uitspreekt",
                 "hoe snel je achter elkaar doorspreekt",
                 "hoeveel woorden je in een zin zet"],
         antwoord=0,
         uitleg="Intonatie is de melodie van je zin. Ze laat horen of je iets vraagt, vaststelt of "
                "verbaasd bent."),
    dict(type="meerkeuze",
         vraag="Wat wordt er met articulatie bedoeld?",
         opties=["hoe duidelijk je de klanken vormt",
                 "hoe hard je tijdens het spreken kijkt",
                 "hoe lang je zinnen in een gesprek zijn",
                 "hoe goed je woordenschat gekozen is"],
         antwoord=0,
         uitleg="Articuleren is de klanken afmaken in plaats van ze in te slikken. Daardoor "
                "verstaat je gesprekspartner je zonder moeite."),
    dict(type="waarofniet",
         vraag="De verleden tijd 'read' en de kleur 'red' klinken verschillend.",
         antwoord=False,
         uitleg="Ze klinken net hetzelfde: 'I read it yesterday' klinkt als red. De tegenwoordige "
                "tijd 'read' klinkt wel anders, als 'reed'."),
    dict(type="meerkeuze",
         vraag="Welke paren klinken hetzelfde maar worden anders geschreven?",
         opties=["their en there", "to en two", "write en right", "ship en sheep"],
         antwoord=[0, 1, 2],
         uitleg="De eerste drie zijn gelijkklinkend; je hoort het verschil niet, je ziet het. Ship "
                "en sheep klinken wel verschillend."),
    dict(type="meerkeuze",
         vraag="Waarin verschillen 'ship' en 'sheep'?",
         opties=["in de lengte van de klinker",
                 "in de klemtoon van het woord",
                 "in de klank van de eerste letter",
                 "in het aantal lettergrepen"],
         antwoord=0,
         uitleg="Sheep heeft een lange ie-klank, ship een korte. Allebei hebben ze één lettergreep "
                "en dezelfde beginklank."),
    dict(type="invultekst",
         vraag="Welk woord klinkt hetzelfde als 'two' en betekent 'ook'?",
         antwoord=["too"],
         uitleg="Too, to en two klinken alle drie gelijk. 'Me too' betekent 'ik ook'."),
    dict(type="waarofniet",
         vraag="Elke letter heeft in het Engels altijd maar één klank.",
         antwoord=False,
         uitleg="Vergelijk de a van cat, car, cake en about: vier keer dezelfde letter, vier keer "
                "een andere klank. Daarom is het schriftbeeld geen betrouwbare gids."),
    dict(type="meerkeuze",
         vraag="In welk woord klinkt de 'th' zoals in 'think'?",
         opties=["thank", "this", "that", "they"],
         antwoord=0,
         uitleg="Think en thank hebben de stemloze th. This, that en they hebben de stemhebbende, "
                "waarbij je stembanden meetrillen."),
    dict(type="meerkeuze",
         vraag="Waarom helpt het woordaccent je bij het luisteren?",
         opties=["de beklemtoonde lettergrepen hoor je het duidelijkst",
                 "de klemtoon valt altijd op het laatste woord",
                 "de klemtoon verandert de betekenis van elke zin",
                 "de klemtoon maakt elke zin even lang in tijd"],
         antwoord=0,
         uitleg="Engelstaligen slikken onbeklemtoonde lettergrepen half in. Wie op de klemtonen "
                "mikt, haalt de inhoud van een zin er het snelst uit."),
    dict(type="meerkeuze",
         vraag="'Present' kan een zelfstandig naamwoord of een werkwoord zijn. Wat verandert er?",
         opties=["de plaats van de klemtoon verschuift",
                 "de eerste letter wordt een hoofdletter",
                 "het woord krijgt er een lettergreep bij",
                 "de spelling van het woord verandert mee"],
         antwoord=0,
         uitleg="Het cadeau is een PRE-sent, iets voorstellen is pre-SENT. Zo zijn er meer: "
                "RE-cord tegenover re-CORD."),
]

DEEL2 = [
    dict(type="meerkeuze",
         vraag="Welke spelling van het woord voor adres is juist?",
         opties=["address", "adress", "addres", "adres"],
         antwoord=0,
         uitleg="Address heeft twee keer een dubbele letter: dd en ss. Het Nederlandse adres heeft "
                "er geen enkele, en daar gaat het mis."),
    dict(type="meerkeuze",
         vraag="Welke korte vormen zijn juist geschreven?",
         opties=["don't", "can't", "I'm", "wont"],
         antwoord=[0, 1, 2],
         uitleg="De apostrof staat waar de letters weggevallen zijn. 'Wont' zonder apostrof is een "
                "ander woord; de korte vorm van will not is won't."),
    dict(type="invultekst",
         vraag="Schrijf de verleden tijd van 'to study'.",
         antwoord=["studied"],
         uitleg="Een y achter een medeklinker wordt ie voor je -d zet: study wordt studied, carry "
                "wordt carried."),
    dict(type="meerkeuze",
         vraag="Wanneer verandert de y aan het eind van een woord in een i?",
         opties=["als er een medeklinker voor de y staat",
                 "als er een klinker voor de y staat",
                 "als het woord met een s begint",
                 "als het woord twee lettergrepen heeft"],
         antwoord=0,
         uitleg="Baby wordt babies, maar boy blijft boys, want daar staat een klinker voor de y."),
    dict(type="waarofniet",
         vraag="Bij 'make' valt de laatste e weg als je er -ing achter zet.",
         antwoord=True,
         uitleg="Make wordt making, write wordt writing, dance wordt dancing. De stomme e aan het "
                "eind verdwijnt."),
    dict(type="meerkeuze",
         vraag="Welke spelling van het voegwoord voor 'omdat' is juist?",
         opties=["because", "becouse", "becuase", "bacause"],
         antwoord=0,
         uitleg="Because is een van de meest geschreven woorden van het Engels, en een van de "
                "meest verkeerd geschreven. Onthoud de volgorde: be-cause."),
    dict(type="meerkeuze",
         vraag="Welke woorden zijn juist gespeld?",
         opties=["friend", "beautiful", "necessary", "recieve"],
         antwoord=[0, 1, 2],
         uitleg="'Recieve' is fout: het is receive, want na een c komt ei en niet ie."),
    dict(type="invultekst",
         vraag="Het ezelsbruggetje zegt: i before e except after … . Welke letter hoort op de "
               "puntjes?",
         antwoord=["c", "de c"],
         uitleg="Believe en field hebben ie, maar receive en ceiling hebben ei, want er staat een "
                "c voor. Er zijn uitzonderingen, maar de regel helpt."),
    dict(type="waarofniet",
         vraag="'Their', 'there' en 'they're' mag je door elkaar gebruiken, want ze klinken hetzelfde.",
         antwoord=False,
         uitleg="Ze klinken gelijk maar betekenen iets anders: hun, daar en zij zijn. Een lezer "
                "ziet de fout meteen."),
    dict(type="meerkeuze",
         vraag="Welke zin gebruikt 'its' juist?",
         opties=["The dog hurt its paw.",
                 "Its a long way home.",
                 "Its raining again today.",
                 "I think its too late now."],
         antwoord=0,
         uitleg="'Its' zonder apostrof betekent 'zijn' of 'haar'. 'It's' met apostrof is de korte "
                "vorm van it is."),
    dict(type="meerkeuze",
         vraag="Wat is het verschil tussen 'your' en 'you're'?",
         opties=["your betekent jouw, you're betekent jij bent",
                 "your is formeel en you're is informeel",
                 "your gebruik je enkel in een vraagzin",
                 "er is geen verschil, allebei zijn juist"],
         antwoord=0,
         uitleg="'Your book' is jouw boek. 'You're late' is de korte vorm van you are late."),
    dict(type="invultekst",
         vraag="Schrijf het meervoud van 'baby'.",
         antwoord=["babies"],
         uitleg="De y achter een medeklinker wordt ies: baby wordt babies, city wordt cities."),
    dict(type="waarofniet",
         vraag="Sommige woorden op -f krijgen in het meervoud -ves, zoals leaf dat leaves wordt.",
         antwoord=True,
         uitleg="Leaf wordt leaves, knife wordt knives, wife wordt wives. Niet allemaal: roof "
                "wordt gewoon roofs."),
    dict(type="meerkeuze",
         vraag="Wat is het meervoud van 'box'?",
         opties=["boxes", "boxs", "boxies", "boxen"],
         antwoord=0,
         uitleg="Na een sisklank komt er -es bij: box wordt boxes, watch wordt watches, bus wordt "
                "buses."),
    dict(type="meerkeuze",
         vraag="Welke woorden krijgen in het Engels altijd een hoofdletter?",
         opties=["Monday", "English", "July", "winter"],
         antwoord=[0, 1, 2],
         uitleg="Dagen, talen, landen en maanden krijgen een hoofdletter. De seizoenen niet: "
                "winter, spring, summer en autumn blijven klein."),
    dict(type="meerkeuze",
         vraag="Hoe schrijf je 'to carry' bij he, she of it?",
         opties=["carries", "carrys", "carryes", "carryies"],
         antwoord=0,
         uitleg="Dezelfde regel als bij het meervoud: de y achter een medeklinker wordt ies. "
                "Vergelijk met 'he plays', want daar staat een klinker voor de y."),
    dict(type="waarofniet",
         vraag="De dagen van de week schrijf je in het Engels met een kleine letter.",
         antwoord=False,
         uitleg="Monday, Tuesday en Wednesday krijgen een hoofdletter, ook midden in een zin. In "
                "het Nederlands is dat net niet zo."),
    dict(type="meerkeuze",
         vraag="Je mag op het examen een spellingcontrole gebruiken. Waarvoor dient die?",
         opties=["om je tekst achteraf na te kijken",
                 "om je zinnen voor je te schrijven",
                 "om woorden te vertalen die je zoekt",
                 "om je tekst korter te laten maken"],
         antwoord=0,
         uitleg="Een spellingcontrole vindt je typfouten, maar ze bedenkt niets voor jou en ze "
                "ziet niet dat je 'their' schreef waar 'there' moest staan."),
    dict(type="meerkeuze",
         vraag="Welke spelling van het woord voor 'zeker' is juist?",
         opties=["definitely", "definately", "definetly", "definatly"],
         antwoord=0,
         uitleg="Er zit het woord 'finite' in: de-FINITE-ly. Zo onthoud je dat er een i staat waar "
                "veel mensen een a schrijven."),
    dict(type="meerkeuze",
         vraag="Waarom kosten spelfouten je niet meteen al je punten?",
         opties=["ze tellen pas mee als ze het begrip in de weg staan",
                 "ze tellen alleen mee in het mondelinge deel",
                 "ze tellen niet mee omdat je een computer gebruikt",
                 "ze tellen alleen mee bij de allerlaatste opdracht"],
         antwoord=0,
         uitleg="Spelfouten en fouten tegen leestekens mogen het tekstbegrip niet in de weg staan. "
                "Een lezer die moet raden wat je bedoelt, kost je wel punten."),
]

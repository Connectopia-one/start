"""Pittige hoofdstukken bij Engels 🌱 Start.

Engels is een taalvak: invulantwoorden worden streng vergeleken
(zie lib/taalvak.ts). Elk invulantwoord is daarom één woord dat maar op
één manier geschreven kan worden.
"""

NIVEAU = "start"
VAK = "Engels"
BESTAND = "start-engels-pittig.json"

WOORDEN = [
    {
        "type": "meerkeuze",
        "vraag": "Wat betekent “It is raining cats and dogs”?",
        "opties": [
            "het giet",
            "er lopen veel dieren op straat buiten",
            "het is prachtig weer om te wandelen",
            "de dieren moeten binnen blijven vandaag",
        ],
        "antwoord": 0,
        "uitleg": "Een uitdrukking vertaal je nooit woord voor woord. Deze betekent gewoon: het regent heel hard.",
    },
    {
        "type": "invultekst",
        "vraag": "Wat is het meervoud van child? Antwoord met één Engels woord.",
        "antwoord": "children",
        "uitleg": "Child is onregelmatig: geen childs maar children. Zo ook man/men, woman/women, foot/feet, tooth/teeth.",
    },
    {
        "type": "waarofniet",
        "vraag": "Het Engelse woord actually betekent eigenlijk, niet actueel.",
        "antwoord": True,
        "uitleg": "Klopt. Actually is een valse vriend: het lijkt op actueel maar betekent eigenlijk. Actueel is current.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welk woord betekent niet hetzelfde als de andere drie?",
        "opties": [
            "tired",
            "exhausted",
            "sleepy",
            "worn out",
        ],
        "antwoord": 3,
        "uitleg": "Tired, exhausted en sleepy gaan alle drie over moe zijn van jezelf. Worn out kan dat ook, maar wordt vooral gezegd van versleten spullen.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul in: my brother’s daughter is my ... Antwoord met één Engels woord.",
        "antwoord": "niece",
        "uitleg": "De dochter van je broer is je nicht: niece. De zoon van je broer is je nephew.",
    },
    {
        "type": "waarofniet",
        "vraag": "In het Engels schrijf je de namen van de dagen en de maanden met een hoofdletter.",
        "antwoord": True,
        "uitleg": "Klopt: Monday, Tuesday, January, July. In het Nederlands net niet, daar blijft maandag klein.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat betekent “to borrow”?",
        "opties": [
            "lenen van iemand",
            "iets uitlenen aan iemand anders",
            "iets voorgoed weggeven zonder iets terug",
            "iets kopen in een gewone winkel",
        ],
        "antwoord": 0,
        "uitleg": "To borrow is lenen van iemand, to lend is uitlenen aan iemand. Can I borrow your pen? Yes, I will lend it to you.",
    },
    {
        "type": "invultekst",
        "vraag": "Wat is het tegenovergestelde van expensive? Antwoord met één Engels woord.",
        "antwoord": "cheap",
        "uitleg": "Expensive is duur, cheap is goedkoop. Een ander woord is inexpensive, maar cheap is het gewone woord.",
    },
    {
        "type": "waarofniet",
        "vraag": "Het Engelse woord eventually betekent eventueel.",
        "antwoord": False,
        "uitleg": "Niet waar, dat is nog een valse vriend. Eventually betekent uiteindelijk. Eventueel is possibly.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je hebt honger en je zegt: “I could eat a horse.” Wat bedoel je?",
        "opties": [
            "je hebt enorme honger",
            "je vindt paardenvlees erg lekker",
            "je bent een goede ruiter geworden",
            "je wil graag naar een boerderij gaan",
        ],
        "antwoord": 0,
        "uitleg": "Alweer een uitdrukking. Je zegt dat je zo veel honger hebt dat je een paard zou opeten.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul in: the opposite of always is ... Antwoord met één Engels woord.",
        "antwoord": "never",
        "uitleg": "Always is altijd, never is nooit. Daartussen: sometimes, often, usually.",
    },
    {
        "type": "waarofniet",
        "vraag": "Fifty en fifteen zijn twee verschillende getallen.",
        "antwoord": True,
        "uitleg": "Klopt: fifteen is 15, fifty is 50. De klemtoon verschilt: fifTEEN achteraan, FIFty vooraan.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welk woord hoort bij het weer?",
        "opties": [
            "cloudy",
            "cloudless mountains far away",
            "clover in the green field",
            "clothes hanging on a line",
        ],
        "antwoord": 0,
        "uitleg": "Cloudy is bewolkt, van cloud: wolk. De andere drie lijken erop maar gaan over iets anders.",
    },
    {
        "type": "invultekst",
        "vraag": "Wat is het meervoud van mouse (het dier)? Antwoord met één Engels woord.",
        "antwoord": "mice",
        "uitleg": "Onregelmatig: one mouse, two mice. Voor de muis van een computer zegt men tegenwoordig ook mouses.",
    },
    {
        "type": "waarofniet",
        "vraag": "In het Engels zeg je twelve hundred voor 1200.",
        "antwoord": True,
        "uitleg": "Klopt, dat mag. One thousand two hundred kan ook. Bij jaartallen is twelve hundred zelfs het gewoonste.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is een winkel waar je brood koopt?",
        "opties": [
            "a bakery",
            "a butcher with meat and sausages",
            "a library full of books to read",
            "a grocery for fruit and vegetables",
        ],
        "antwoord": 0,
        "uitleg": "A bakery is een bakkerij. Let op library: dat is een bibliotheek, geen boekenwinkel.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul in: a baby cat is a ... Antwoord met één Engels woord.",
        "antwoord": "kitten",
        "uitleg": "Een jonge kat is a kitten, een jonge hond a puppy, een jong paard a foal.",
    },
    {
        "type": "waarofniet",
        "vraag": "Het woord homework krijgt in het Engels nooit een s.",
        "antwoord": True,
        "uitleg": "Klopt. Homework is ontelbaar, net als information, advice en furniture. Je zegt a lot of homework, geen homeworks.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat betekent “once in a blue moon”?",
        "opties": [
            "heel zelden",
            "elke maand op dezelfde dag opnieuw",
            "wanneer het volle maan is buiten",
            "altijd wanneer het donker wordt",
        ],
        "antwoord": 0,
        "uitleg": "Een blue moon is een zeldzame tweede volle maan in één maand. De uitdrukking betekent dus: bijna nooit.",
    },
    {
        "type": "invultekst",
        "vraag": "Wat is het tegenovergestelde van to remember? Antwoord met één Engels woord.",
        "antwoord": "forget",
        "uitleg": "To remember is onthouden of zich herinneren, to forget is vergeten. Verleden tijd: forgot.",
    },
]

VOORSTELLEN = [
    {
        "type": "meerkeuze",
        "vraag": "Iemand vraagt “How do you do?”. Wat antwoord je?",
        "opties": [
            "How do you do?",
            "I am doing my homework right now",
            "I do it every day after school",
            "Yes, I do that quite often actually",
        ],
        "antwoord": 0,
        "uitleg": "How do you do is geen echte vraag maar een heel formele begroeting. Je herhaalt ze gewoon.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul in: I ... from Belgium. Antwoord met één Engels woord.",
        "antwoord": "am",
        "uitleg": "Bij I hoort am: I am from Belgium. Bij he, she, it hoort is, bij you, we en they hoort are.",
    },
    {
        "type": "waarofniet",
        "vraag": "Je schrijft het woord I in het Engels altijd met een hoofdletter, ook midden in een zin.",
        "antwoord": True,
        "uitleg": "Klopt, altijd: yesterday I went home. Alleen bij I is dat zo, niet bij you of he.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe vraag je beleefd naar iemands leeftijd?",
        "opties": [
            "How old are you?",
            "How many years do you have?",
            "What is your number of years?",
            "How much old are you now?",
        ],
        "antwoord": 0,
        "uitleg": "In het Engels bén je een leeftijd, je hébt ze niet: I am eleven. “How many years do you have” is vertaald Nederlands.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul in: this is my sister. ... name is Emma. Antwoord met één Engels woord.",
        "antwoord": "her",
        "uitleg": "Bij een meisje of vrouw hoort her, bij een jongen of man his. Het gaat om wie iets bezit, niet om het ding zelf.",
    },
    {
        "type": "waarofniet",
        "vraag": "In het Engels zeg je I have twelve years om te zeggen dat je twaalf bent.",
        "antwoord": False,
        "uitleg": "Niet waar. Je zegt I am twelve, of voluit I am twelve years old.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welke vraag past bij het antwoord “I live in Hasselt”?",
        "opties": [
            "Where do you live?",
            "How do you live over there?",
            "When are you living in that city?",
            "Why do you live in a town?",
        ],
        "antwoord": 0,
        "uitleg": "Where vraagt naar een plaats. How vraagt hoe, when wanneer, why waarom.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul in: my father and my mother are my ... Antwoord met één Engels woord.",
        "antwoord": "parents",
        "uitleg": "Parents zijn de ouders. Let op: parents zijn niet de familieleden in het algemeen, dat is relatives.",
    },
    {
        "type": "waarofniet",
        "vraag": "Nice to meet you zeg je de eerste keer dat je iemand ontmoet.",
        "antwoord": True,
        "uitleg": "Klopt. Zie je die persoon later terug, dan zeg je nice to see you again.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat betekent “What do you do?” aan een volwassene gevraagd?",
        "opties": [
            "wat is je beroep",
            "wat ben je op dit moment aan het doen",
            "wat ga je later nog allemaal doen",
            "wat doe je het liefst in je vrije tijd",
        ],
        "antwoord": 0,
        "uitleg": "What do you do vraagt naar je werk. Wil je weten wat iemand nu doet, dan vraag je what are you doing.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul in: I have got two brothers, but I ... got any sisters. Antwoord met twee Engelse woorden.",
        "antwoord": "have not",
        "uitleg": "In een ontkennende zin komt not achter have: I have not got. Verkort is dat haven’t got.",
    },
    {
        "type": "waarofniet",
        "vraag": "Je achternaam heet in het Engels je surname of je last name.",
        "antwoord": True,
        "uitleg": "Klopt, allebei mag. Je voornaam is je first name of given name.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe stel je je zus voor aan een vriend?",
        "opties": [
            "This is my sister.",
            "Here you have my sister there.",
            "That one over there is a sister.",
            "She is being my sister right now.",
        ],
        "antwoord": 0,
        "uitleg": "Iemand voorstellen doe je met this is. Bij iets verder weg zeg je that is.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul in: ... old is your brother? Antwoord met één Engels woord.",
        "antwoord": "how",
        "uitleg": "How old vraagt naar de leeftijd. How past voor veel woorden: how tall, how many, how often.",
    },
    {
        "type": "waarofniet",
        "vraag": "Je mag in een formele brief beginnen met Dear Mr Smith.",
        "antwoord": True,
        "uitleg": "Klopt, dat is de gewone formele aanhef. Ken je de naam niet, dan schrijf je Dear Sir or Madam.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Iemand zegt “I am an only child”. Wat betekent dat?",
        "opties": [
            "hij heeft geen broers of zussen",
            "hij is het enige kind in de hele klas",
            "hij is nog maar een heel klein kind",
            "hij is het jongste kind van het gezin",
        ],
        "antwoord": 0,
        "uitleg": "An only child is een enig kind. Het jongste kind is the youngest.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul in: my hobby is football. I ... playing football. Antwoord met één Engels woord.",
        "antwoord": "like",
        "uitleg": "Na like komt een werkwoord met -ing of met to: I like playing, I like to play. Allebei is juist.",
    },
    {
        "type": "waarofniet",
        "vraag": "Goodbye is formeler dan bye.",
        "antwoord": True,
        "uitleg": "Klopt. Bye en see you zijn losjes, goodbye is netter. Nog formeler: have a nice day.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Welke zin is juist?",
        "opties": [
            "She is my best friend.",
            "She is my more best friend.",
            "She is my most good friend.",
            "She is my gooder friend there.",
        ],
        "antwoord": 0,
        "uitleg": "Good wordt onregelmatig vergeleken: good, better, best. Dus nooit gooder of most good.",
    },
    {
        "type": "invultekst",
        "vraag": "Vul in: nice to ... you. Zeg je bij een eerste ontmoeting. Antwoord met één Engels woord.",
        "antwoord": "meet",
        "uitleg": "To meet is ontmoeten. Nice to meet you bij de eerste keer, nice to see you als je elkaar al kent.",
    },
]

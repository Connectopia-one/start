# -*- coding: utf-8 -*-
"""🔭 Uitdagingshoek — Paradoxen en weetjes, deel 1: paradoxen."""

VAK = "Paradoxen en weetjes"
BESTAND = "paradoxen-en-weetjes.json"
TITEL = "Paradoxen die je hoofd kraken"
VOLGORDE = 1

VRAGEN = [
    {
        "type": "meerkeuze",
        "vraag": "De paradox van Olbers vraagt: als het heelal oneindig vol sterren staat, waarom is de nacht dan donker?",
        "opties": [
            "Het heelal is niet oneindig oud, dus niet alle sterlicht is hier al",
            "Het stof tussen de sterren houdt het meeste licht onderweg tegen",
            "Er staan gewoon te weinig sterren om de hemel op te vullen",
            "Onze dampkring laat 's nachts maar een deel van het licht door",
        ],
        "antwoord": 0,
        "uitleg": "In elke richting zou je op een ster moeten uitkomen, dus zou de hele hemel moeten gloeien. De uitweg: het heelal is zo'n 13,8 miljard jaar oud, dus verder licht is nog onderweg, en door de uitdijing is het licht van de verste stelsels bovendien uit het zichtbare gerekt. Stof helpt niet: dat zou zelf gaan gloeien.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom bedacht Erwin Schrödinger zijn kat die tegelijk dood en levend zou zijn?",
        "opties": [
            "Om te tonen hoe raar het wordt als je kwantumregels op grote dingen loslaat",
            "Om te bewijzen dat katten echt in twee toestanden tegelijk kunnen zijn",
            "Om uit te leggen hoe je met gif een deeltje kunt opmeten",
            "Om aan te tonen dat niemand ooit iets met zekerheid kan weten",
        ],
        "antwoord": 0,
        "uitleg": "Het was spot, geen voorspelling. Een atoom kan wel degelijk in twee toestanden tegelijk zitten, en Schrödinger vroeg zich af wat dat zou betekenen als je zo'n atoom aan een kat vastkoppelt. Zijn punt: dan klopt er iets niet aan onze uitleg.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je vervangt aan een schip elke plank, één voor één, tot er geen origineel stuk meer over is. Wat is de vraag van Theseus?",
        "opties": [
            "Of het nog steeds hetzelfde schip is",
            "Of het schip nog wel kan blijven drijven",
            "Wie de eigenaar van de oude planken is",
            "Hoeveel planken je mag vervangen voor het te duur wordt",
        ],
        "antwoord": 0,
        "uitleg": "En als iemand alle oude planken opraapt en er opnieuw een schip van bouwt, welk van de twee is dan het echte? Het is geen strikvraag maar een vraag over wat identiteit eigenlijk is. In je eigen lichaam worden ook voortdurend cellen vervangen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hilberts hotel heeft oneindig veel kamers en zit helemaal vol. Er komt nog een gast. Wat nu?",
        "opties": [
            "Iedereen schuift één kamer op, en kamer 1 komt vrij",
            "De nieuwe gast moet wachten tot er iemand vertrekt",
            "De gast deelt een kamer met wie er al ligt",
            "Er wordt een extra kamer aan het einde bijgebouwd",
        ],
        "antwoord": 0,
        "uitleg": "De gast uit kamer 1 gaat naar 2, die uit 2 naar 3, enzovoort. Niemand valt uit de boot, want er is geen laatste kamer. Bij oneindigheid werkt vol niet zoals bij eindige dingen, en daar was het David Hilbert net om te doen.",
    },
    {
        "type": "waarofniet",
        "vraag": "Er zijn evenveel even getallen als er natuurlijke getallen zijn.",
        "antwoord": True,
        "uitleg": "Je kunt ze twee aan twee koppelen: 1 met 2, 2 met 4, 3 met 6, en zo door. Niemand blijft over aan beide kanten, dus zijn de twee verzamelingen even groot. Dat de even getallen er maar de helft van zijn, is bij oneindige verzamelingen geen tegenspraak.",
    },
    {
        "type": "meerkeuze",
        "vraag": "In een groep van 23 mensen: hoe groot is de kans dat er twee op dezelfde dag jarig zijn?",
        "opties": [
            "Ongeveer de helft",
            "Ongeveer één op tien",
            "Ongeveer één op honderd",
            "Bijna zeker, meer dan negen op tien",
        ],
        "antwoord": 0,
        "uitleg": "Veel mensen gokken veel lager, en daarom heet het de verjaardagsparadox. Het gaat niet om jouw verjaardag maar om élk paar in de groep, en bij 23 mensen zijn dat er al 253. Vanaf 70 mensen is de kans groter dan 99 procent.",
    },
    {
        "type": "meerkeuze",
        "vraag": "In een spel kies je één van drie deuren. De presentator opent een andere deur met een geit erachter en biedt je aan te wisselen. Wat doe je best?",
        "opties": [
            "Wisselen, want dan win je in twee van de drie gevallen",
            "Blijven, want dan win je in twee van de drie gevallen",
            "Het maakt niet uit: de kans is nu vijftig om vijftig",
            "Wisselen, maar alleen als je eerst de middelste koos",
        ],
        "antwoord": 0,
        "uitleg": "Je eerste keuze was in één op drie gevallen juist, en dat verandert niet. Dus zit de prijs in twee op drie gevallen achter een van de twee andere deuren, en de presentator heeft de foute daarvan net voor je weggehaald. Duizenden mensen schreven de wiskundige die dit uitlegde aan dat ze zich vergiste.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Volgens Zeno haalt de snelle Achilles een schildpad met voorsprong nooit in. Waar wringt zijn redenering?",
        "opties": [
            "Oneindig veel stapjes kunnen samen toch een eindige tijd duren",
            "Achilles loopt in werkelijkheid niet sneller dan een schildpad",
            "De schildpad moet ook stoppen om te rusten onderweg",
            "Een voorsprong telt niet mee als de afstand groot genoeg is",
        ],
        "antwoord": 0,
        "uitleg": "Telkens Achilles het vorige punt van de schildpad bereikt, is die alweer een eindje verder. Dat zijn oneindig veel stappen, maar ze worden zó snel kleiner dat hun som eindig is: een halve plus een kwart plus een achtste blijft onder de één.",
    },
    {
        "type": "waarofniet",
        "vraag": "Het getal 0,999... met eindeloos veel negens is precies gelijk aan 1.",
        "antwoord": True,
        "uitleg": "Niet bijna, maar exact. Eén derde is 0,333..., en drie keer een derde is één, dus 0,999... is één. Of anders: als ze verschillend waren, moest er een getal tussen passen, en dat bestaat niet.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Wat is er zo lastig aan de zin: deze zin is vals?",
        "opties": [
            "Is ze waar, dan is ze vals, en is ze vals, dan is ze waar",
            "Ze bevat een spelfout waardoor je ze niet kunt beoordelen",
            "Ze verwijst naar een andere zin die er niet bij staat",
            "Ze is te kort om er iets zinnigs over te kunnen zeggen",
        ],
        "antwoord": 0,
        "uitleg": "De leugenaarsparadox draait al meer dan tweeduizend jaar rond. Het probleem zit in het spreken over zichzelf. Kurt Gödel gebruikte diezelfde truc in 1931 om iets veel diepers te bewijzen over de grenzen van de wiskunde.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Je reist terug in de tijd en verhindert dat je grootouders elkaar ooit ontmoeten. Waarom is dat een paradox?",
        "opties": [
            "Dan word jij nooit geboren, en kun je dus ook niet terugreizen",
            "Dan zou je twee keer op dezelfde plaats tegelijk bestaan",
            "Dan zou je ouder worden dan je eigen grootouders zijn",
            "Dan verdwijnt de tijdmachine voordat je ermee vertrekt",
        ],
        "antwoord": 0,
        "uitleg": "Het argument bijt zichzelf in de staart, en daarom denken veel natuurkundigen dat reizen naar het verleden onmogelijk moet zijn. Anderen opperen dat de natuur zoiets gewoon niet zou laten gebeuren, hoe je het ook probeert.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Een tweeling: eentje blijft thuis, de ander maakt een razendsnelle ruimtereis. Wat is er bij de terugkeer aan de hand?",
        "opties": [
            "De reiziger is minder oud geworden dan wie thuisbleef",
            "Wie thuisbleef is minder oud geworden dan de reiziger",
            "Ze zijn allebei precies even oud gebleven als voordien",
            "De reiziger is juist twee keer zo snel ouder geworden",
        ],
        "antwoord": 0,
        "uitleg": "Bij snelheden dicht bij die van het licht loopt de tijd trager. Het lijkt onrechtvaardig, want vanuit de raket ziet de aarde er net zo goed snel uit. Het verschil zit erin dat alleen de reiziger moet afremmen en keren, en dat breekt de symmetrie.",
    },
    {
        "type": "waarofniet",
        "vraag": "Een extra weg aanleggen kan het verkeer voor iedereen trager maken.",
        "antwoord": True,
        "uitleg": "Dat heet de paradox van Braess. Als iedereen apart voor de snelste route kiest, kan die nieuwe weg zo druk worden dat het geheel er slechter van wordt. In Seoel en New York werd verkeer juist vlotter nadat een weg gesloten werd.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Eén zandkorrel is geen hoop. Voeg er telkens één bij en het blijft geen hoop. Toch heb je op een bepaald moment een hoop. Waar zit het probleem?",
        "opties": [
            "Het woord hoop heeft geen scherpe grens",
            "Zandkorrels verschillen te veel in grootte",
            "De redenering telt ergens één korrel dubbel",
            "Een hoop hangt af van de vorm, niet van het aantal",
        ],
        "antwoord": 0,
        "uitleg": "De sorites-paradox laat zien dat veel alledaagse woorden vage randen hebben: jong, kaal, warm, rijk. Dat is geen fout in de taal maar een eigenschap ervan, en het maakt wetten schrijven soms bijzonder lastig.",
    },
    {
        "type": "meerkeuze",
        "vraag": "De Fermi-paradox vat één vraag samen. Welke?",
        "opties": [
            "Zoveel sterren met planeten, en toch geen spoor van anderen",
            "Waarom licht van verre sterren ons nooit lijkt te bereiken",
            "Hoe leven kon ontstaan uit stoffen die zelf niet leven",
            "Waarom wij als enige soort op aarde kunnen spreken",
        ],
        "antwoord": 0,
        "uitleg": "Alleen al onze Melkweg telt honderden miljarden sterren, veel ervan met planeten, en het heelal bestaat al lang. Waar is iedereen dan, vroeg Enrico Fermi. Misschien is leven zeldzaam, of luisteren we verkeerd, of houdt beschaving het niet lang vol.",
    },
    {
        "type": "waarofniet",
        "vraag": "Bij het roulettespel wordt rood waarschijnlijker als er tien keer na elkaar zwart viel.",
        "antwoord": False,
        "uitleg": "Het balletje heeft geen geheugen: elke beurt begint opnieuw. Dat heet de gokkersmisvatting. Ze is verraderlijk, want een lange reeks voelt aan alsof er iets moet rechtgezet worden, en casino's leven daarvan.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Waarom keert een spiegel links en rechts om, maar niet boven en onder?",
        "opties": [
            "Ze keert eigenlijk voor en achter om, wij draaien onszelf erbij",
            "Onze ogen staan naast elkaar en niet boven elkaar",
            "Het licht kaatst horizontaal anders dan verticaal",
            "Ze keert wel degelijk ook boven en onder om",
        ],
        "antwoord": 0,
        "uitleg": "Je spiegelbeeld steekt zijn neus naar jou toe waar jij die van de spiegel wegsteekt: dat is de as die omkeert. Wij denken in links en rechts omdat we ons voorstellen dat we zelf omdraaien. Ga eens op je zij liggen voor een spiegel, en de verwarring is meteen opgelost.",
    },
    {
        "type": "meerkeuze",
        "vraag": "Hoe bewijst de wiskunde dat er oneindig veel priemgetallen zijn?",
        "opties": [
            "Door aan te nemen dat er eindig veel zijn en dan een nieuw te maken",
            "Door ze allemaal op te sommen tot je niet meer verder kunt",
            "Door te tonen dat elk even getal er twee bevat",
            "Door te meten dat ze steeds dichter bij elkaar gaan liggen",
        ],
        "antwoord": 0,
        "uitleg": "Euclides deed dat al meer dan tweeduizend jaar geleden. Vermenigvuldig alle priemgetallen van je zogezegd volledige lijst en tel er één bij op. Dat nieuwe getal is door geen enkel getal uit je lijst deelbaar, dus je lijst was niet volledig.",
    },
    {
        "type": "waarofniet",
        "vraag": "Op een lijn van één kilometer liggen meer punten dan op een lijn van één centimeter.",
        "antwoord": False,
        "uitleg": "Leg de korte lijn schuin onder de lange en trek stralen vanuit één punt: elk punt van de ene komt precies overeen met één punt van de andere. Lengte en aantal punten zijn dus twee verschillende dingen.",
    },
    {
        "type": "meerkeuze",
        "vraag": "De kosmische kalender perst de hele geschiedenis van het heelal in één jaar. Wanneer verschijnt de mens?",
        "opties": [
            "Pas in de laatste minuten van 31 december",
            "Ergens rond het midden van de maand november",
            "Kort na de zomer, begin september",
            "Bij het begin van het jaar, in januari",
        ],
        "antwoord": 0,
        "uitleg": "De oerknal valt op 1 januari, de aarde ontstaat pas eind augustus, de dinosauriërs sterven uit op 30 december. Alles wat ooit is opgeschreven, van de eerste kleitabletten tot vandaag, past in de laatste halve minuut van oudejaarsavond.",
    },
]

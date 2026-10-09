# -*- coding: utf-8 -*-
"""Het persoonlijk budget en je administratie.

Het tweede thema uit "ik beheer mijn financiën". Twee rijtjes van de fiche
staan hier centraal, en beide hebben een valkuil.

De soorten inkomsten en uitgaven:

    inkomsten   terugkerend, toevallig
    uitgaven    variabel, vast, onvoorzien, uitzonderlijk

De valkuil zit bij de uitgaven: vier soorten, niet twee. Een vaste uitgave is
elke maand hetzelfde bedrag (huur, abonnement). Een variabele uitgave keert
wel terug maar wisselt in hoogte (boodschappen, brandstof). Een onvoorziene
uitgave komt plots (een herstelling). Een uitzonderlijke uitgave zie je wel
aankomen maar ze komt zelden (een nieuwe wasmachine, een reis).

De zeven factoren waarmee je een aankoopkeuze verantwoordt, letterlijk uit de
fiche en alfabetisch zoals ze er staan:

    de aankoopkost, de duurzaamheid, de financieringskost, de inflatie,
    de noodzakelijkheid, de spaarbuffer, de terugbetalingscapaciteit

En de persoonlijke administratie: het aankoopbewijs (factuur, kasticket,
aankoopovereenkomst), het garantiebewijs, het rekeninguittreksel, de
verzekeringspolis, de loonstrook of individuele rekening.

Deel 1 is de inkomsten en de uitgaven, en het budgetplan.
Deel 2 is de zeven factoren en de administratie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke twee soorten inkomsten noemt de fiche?",
        opties=[
            "terugkerende en toevallige inkomsten",
            "vaste en variabele inkomsten",
            "netto- en bruto-inkomsten",
            "eigen en geleende inkomsten",
        ],
        antwoord=0,
        uitleg="Vast en variabel gaat over de uitgaven, niet over de inkomsten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vier soorten uitgaven noemt de fiche?",
        opties=[
            "variabele, vaste, onvoorziene en uitzonderlijke uitgaven",
            "vaste en variabele uitgaven",
            "noodzakelijke en overbodige uitgaven",
            "maandelijkse, jaarlijkse en eenmalige uitgaven",
        ],
        antwoord=0,
        uitleg="Vier, niet twee. Onvoorzien en uitzonderlijk worden het vaakst vergeten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je loon komt elke maand binnen. Welke soort inkomst is dat?",
        opties=[
            "een terugkerende inkomst",
            "een toevallige inkomst",
            "een vaste uitgave",
            "een uitzonderlijke inkomst",
        ],
        antwoord=0,
        uitleg="Wat regelmatig terugkomt, is terugkerend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verkoopt eenmalig je oude fiets. Welke soort inkomst is dat?",
        opties=[
            "een toevallige inkomst",
            "een terugkerende inkomst",
            "een uitzonderlijke uitgave",
            "een aanvullend inkomen",
        ],
        antwoord=0,
        uitleg="Ze komt één keer en je kan er niet op rekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je huur van 750 euro per maand. Welke soort uitgave is dat?",
        opties=[
            "een vaste uitgave",
            "een variabele uitgave",
            "een onvoorziene uitgave",
            "een uitzonderlijke uitgave",
        ],
        antwoord=0,
        uitleg="Elke maand hetzelfde bedrag op dezelfde dag. Dat is vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je boodschappen, die de ene maand meer kosten dan de andere. Welke soort uitgave is dat?",
        opties=[
            "een variabele uitgave",
            "een vaste uitgave",
            "een onvoorziene uitgave",
            "een toevallige inkomst",
        ],
        antwoord=0,
        uitleg="Ze komen elke maand terug, maar het bedrag wisselt. Dat is variabel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ketel valt vandaag stuk en moet hersteld worden. Welke soort uitgave is dat?",
        opties=[
            "een onvoorziene uitgave",
            "een uitzonderlijke uitgave",
            "een vaste uitgave",
            "een variabele uitgave",
        ],
        antwoord=0,
        uitleg="Je zag ze niet aankomen. Daarvoor dient je spaarbuffer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je plant volgend jaar een grote reis. Welke soort uitgave is dat?",
        opties=[
            "een uitzonderlijke uitgave",
            "een onvoorziene uitgave",
            "een vaste uitgave",
            "een variabele uitgave",
        ],
        antwoord=0,
        uitleg="Ze komt zelden maar je ziet ze aankomen, dus je kan ervoor sparen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een onvoorziene en een uitzonderlijke uitgave?",
        opties=[
            "een onvoorziene zie je niet aankomen, een uitzonderlijke wel",
            "een onvoorziene is altijd groter",
            "een uitzonderlijke komt elke maand terug",
            "er is geen verschil",
        ],
        antwoord=0,
        uitleg="Daarom kan je voor een uitzonderlijke uitgave sparen en voor een onvoorziene enkel een buffer houden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een budgetplan?",
        opties=[
            "zicht krijgen op je inkomsten en uitgaven en zien hoeveel je kan sparen",
            "je belastingen voor het afgelopen jaar tot op de euro juist berekenen",
            "een krediet aanvragen bij de bank zonder dat je iets moet bewijzen",
            "je werkgever overtuigen om je loon volgend jaar flink te verhogen",
        ],
        antwoord=0,
        uitleg="De fiche zegt letterlijk: om inzicht te krijgen en te berekenen hoeveel je kan sparen.",
    ),
    dict(
        type="waarofniet",
        vraag="De fiche onderscheidt vier soorten uitgaven.",
        antwoord=True,
        uitleg="Variabel, vast, onvoorzien en uitzonderlijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een variabele uitgave keert niet terug.",
        antwoord=False,
        uitleg="Ze keert wel terug, maar met een wisselend bedrag.",
    ),
    dict(
        type="waarofniet",
        vraag="Een budgetplan toont hoeveel je kan sparen.",
        antwoord=True,
        uitleg="Inkomsten min uitgaven is wat er overblijft.",
    ),
    dict(
        type="waarofniet",
        vraag="Terugkerend en toevallig zijn volgens de fiche de twee soorten uitgaven.",
        antwoord=False,
        uitleg="Dat zijn de twee soorten inkomsten. De uitgaven zijn er vier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitgaven noemt de fiche?",
        opties=[
            "vaste uitgaven",
            "variabele uitgaven",
            "onvoorziene uitgaven",
            "vrijwillige uitgaven",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vierde soort is de uitzonderlijke uitgave. Vrijwillig staat er niet.",
    ),
    dict(
        type="invultekst",
        vraag="Je verdient 1.750 euro en geeft 1.480 euro uit. Hoeveel kan je sparen? Antwoord met een getal.",
        antwoord=["270"],
        uitleg="1.750 min 1.480 is 270 euro.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een uitgave die elke maand hetzelfde bedrag is? Vul aan: een ... uitgave.",
        antwoord=["vaste", "vast"],
        uitleg="Een variabele uitgave keert ook terug, maar met een wisselend bedrag.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een uitgave die je niet zag aankomen? Vul aan: een ... uitgave.",
        antwoord=["onvoorziene", "onvoorzien"],
        uitleg="Een uitzonderlijke uitgave zie je wel aankomen, maar ze komt zelden.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een budgetplan staan 2.100 euro inkomsten, 900 euro vaste uitgaven en 650 euro variabele uitgaven. Hoeveel blijft er over?",
        opties=["550 euro", "1.200 euro", "1.450 euro", "250 euro"],
        antwoord=0,
        uitleg="2.100 min 900 min 650 is 550 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand rekent in zijn budget enkel met zijn vaste uitgaven. Wat loopt er mis?",
        opties=[
            "hij houdt geen rekening met variabele, onvoorziene en uitzonderlijke uitgaven",
            "hij telt zijn loon twee keer mee en komt op een veel te hoog bedrag",
            "hij vergeet de toevallige inkomsten die er in een jaar nog bijkomen",
            "hij rekent met zijn brutoloon in plaats van met wat hij echt ontvangt",
        ],
        antwoord=0,
        uitleg="Drie van de vier soorten uitgaven ontbreken, dus zijn plan klopt niet.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel factoren noemt de fiche om een aankoopkeuze te verantwoorden?",
        opties=["zeven", "vier", "vijf", "negen"],
        antwoord=0,
        uitleg="Aankoopkost, duurzaamheid, financieringskost, inflatie, noodzakelijkheid, spaarbuffer en terugbetalingscapaciteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de terugbetalingscapaciteit?",
        opties=[
            "hoeveel je maandelijks kan afbetalen zonder in de problemen te komen",
            "het totale bedrag dat je volgens de bank in je hele leven mag lenen",
            "de rente die je elke maand op een lopende lening moet betalen",
            "het bedrag van de lening dat je op dit moment al hebt afbetaald",
        ],
        antwoord=0,
        uitleg="De bank kijkt ernaar, maar jij zou er eerst zelf naar moeten kijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een spaarbuffer?",
        opties=[
            "geld dat je opzij houdt voor onverwachte kosten",
            "de rente die je op je spaarrekening krijgt",
            "het maximum dat je per maand mag sparen",
            "een lening die je bij jezelf afsluit",
        ],
        antwoord=0,
        uitleg="Zonder buffer wordt elke onvoorziene uitgave een krediet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt de fiche met de noodzakelijkheid als factor?",
        opties=[
            "heb je dit echt nodig of wil je het gewoon graag",
            "hoe lang het product meegaat",
            "hoeveel het kost om het te financieren",
            "of de prijs volgend jaar zal stijgen",
        ],
        antwoord=0,
        uitleg="De eerste vraag bij elke grote aankoop, en de goedkoopste besparing die bestaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt de fiche met duurzaamheid als factor bij een aankoop?",
        opties=[
            "hoelang het product meegaat en wat het voor het milieu betekent",
            "of je het in schijven kan afbetalen zonder extra rente te betalen",
            "of de prijs van het product de komende jaren stabiel blijft",
            "of je het achteraf makkelijk kan doorverkopen aan iemand anders",
        ],
        antwoord=0,
        uitleg="Een goedkoop toestel dat twee jaar meegaat kan duurder uitvallen dan een duur dat tien jaar meegaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de financieringskost?",
        opties=[
            "wat het je extra kost om de aankoop te lenen in plaats van te betalen",
            "de prijs die op het etiket van het product zelf staat, zonder extra kosten",
            "de btw die de verkoper in de prijs van de aankoop verrekent",
            "de kost om het product tot bij je thuis te laten leveren",
        ],
        antwoord=0,
        uitleg="Dat is de meerprijs van het krediet, de totale rente over de looptijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat de inflatie bij de factoren?",
        opties=[
            "omdat geld na verloop van tijd minder waard wordt",
            "omdat producten elk jaar goedkoper worden",
            "omdat je loon meestal daalt",
            "omdat de btw mee stijgt",
        ],
        antwoord=0,
        uitleg="Wachten met kopen kan dus duurder uitvallen, en sparen levert minder op dan het lijkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke documenten noemt de fiche als aankoopbewijs?",
        opties=[
            "de factuur, het kasticket en de aankoopovereenkomst",
            "het garantiebewijs en de verzekeringspolis",
            "het rekeninguittreksel en de loonstrook",
            "de arbeidsovereenkomst en het arbeidsreglement",
        ],
        antwoord=0,
        uitleg="De andere documenten staan wel in het rijtje van je administratie, maar zijn geen aankoopbewijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hou je je garantiebewijs bij?",
        opties=[
            "om een defect binnen de garantieperiode te laten herstellen",
            "om je belastingaangifte voor dat jaar correct in te vullen",
            "om tegenover je werkgever je loon van die maand te bewijzen",
            "om bij de bank een krediet voor een nieuwe aankoop aan te vragen",
        ],
        antwoord=0,
        uitleg="Zonder bewijs is een beroep op de garantie veel moeilijker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een individuele rekening in het rijtje van je administratie?",
        opties=[
            "het jaaroverzicht van wat je werkgever je betaalde",
            "je rekening bij de bank",
            "het overzicht van je kredieten",
            "je persoonlijke belastingaangifte",
        ],
        antwoord=0,
        uitleg="De fiche noemt ze samen met de loonstrook, als bewijs van wat je verdiende.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kasticket geldt volgens de fiche als aankoopbewijs.",
        antwoord=True,
        uitleg="Naast de factuur en de aankoopovereenkomst.",
    ),
    dict(
        type="waarofniet",
        vraag="Een spaarbuffer dient om een vaste uitgave te betalen.",
        antwoord=False,
        uitleg="Vaste uitgaven zitten in je budget. De buffer is er voor wat je niet zag aankomen.",
    ),
    dict(
        type="waarofniet",
        vraag="De duurzaamheid van een product is volgens de fiche een factor bij je aankoopkeuze.",
        antwoord=True,
        uitleg="Ze staat in het rijtje van zeven, naast de aankoopkost en de noodzakelijkheid.",
    ),
    dict(
        type="waarofniet",
        vraag="De financieringskost is hetzelfde als de aankoopkost.",
        antwoord=False,
        uitleg="De aankoopkost is wat het product kost, de financieringskost wat het lenen erbovenop kost.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke factoren noemt de fiche bij het verantwoorden van een aankoopkeuze?",
        opties=[
            "de noodzakelijkheid",
            "de spaarbuffer",
            "de terugbetalingscapaciteit",
            "de mening van je vrienden",
        ],
        antwoord=[0, 1, 2],
        uitleg="De andere vier zijn de aankoopkost, de duurzaamheid, de financieringskost en de inflatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort volgens de fiche bij je persoonlijke administratie?",
        opties=[
            "het garantiebewijs",
            "het rekeninguittreksel",
            "de verzekeringspolis",
            "het arbeidsreglement van je bedrijf",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het arbeidsreglement is van het bedrijf. Het aankoopbewijs en de loonstrook staan wel in het rijtje.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het geld dat je opzij houdt voor onverwachte kosten?",
        antwoord=["spaarbuffer", "een spaarbuffer", "de spaarbuffer"],
        uitleg="Ze staat in het rijtje van zeven factoren.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het bedrag dat je maandelijks kan afbetalen zonder in de problemen te komen?",
        antwoord=["terugbetalingscapaciteit", "de terugbetalingscapaciteit"],
        uitleg="Kijk daar eerst naar, voor de bank het voor je doet.",
    ),
    dict(
        type="invultekst",
        vraag="Welk document bewijst dat je iets gekocht hebt in een winkel, zonder factuur?",
        antwoord=["kasticket", "het kasticket"],
        uitleg="De fiche noemt het naast de factuur en de aankoopovereenkomst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand twijfelt tussen een wasmachine van 400 euro die zes jaar meegaat en een van 700 euro die vijftien jaar meegaat. Welke factor weegt hier het zwaarst?",
        opties=[
            "de duurzaamheid",
            "de inflatie",
            "de spaarbuffer",
            "de terugbetalingscapaciteit",
        ],
        antwoord=0,
        uitleg="Per jaar kost de duurste minder, en dat is precies wat duurzaamheid in deze factor betekent.",
    ),
]

# -*- coding: utf-8 -*-
"""De vragen voor "Productie, toegevoegde waarde en het bbp" (🚀 Boost
doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
"economische groei", eerste stuk: de begrippen productie, toegevoegde waarde en
bruto binnenlands product, de bedrijfskolom, en het rekenwerk met nominaal en
reëel bbp, bbp per capita en groeicijfers.

Deel 1 gaat over de begrippen en de bedrijfskolom: wat produceren is, hoe je de
toegevoegde waarde van een schakel berekent, en waarom je die optelt in plaats
van de omzet.
Deel 2 gaat over het rekenwerk: nominaal en reëel bbp, bbp per capita, nominale
en reële groei, en het lezen van statistieken van Statbel en de Nationale Bank
van België.

Afspraak in dit thema: elke rekenvraag geeft alle cijfers in de vraag zelf, en
een jaartal is altijd een voorbeeldjaar, nooit iets dat een kind uit het hoofd
moet kennen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent produceren in economische zin?",
        opties=[
            "Waarde toevoegen aan goederen of diensten",
            "Een voorwerp maken met de hand of met een machine",
            "Goederen kopen om ze later duurder te verkopen",
            "Grondstoffen uit de natuur halen en verwerken",
        ],
        antwoord=0,
        uitleg="Produceren is waarde toevoegen. Ook een kapper, een leerkracht of een transportbedrijf produceert, want ze maken iets meer waard dan het ervoor was, ook zonder er een voorwerp bij te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de toegevoegde waarde van een bedrijf?",
        opties=[
            "De omzet min de waarde van wat het bij anderen aankocht",
            "De omzet min de lonen die het aan zijn werknemers betaalde",
            "De winst plus de belastingen die het aan de overheid betaalde",
            "De verkoopprijs van zijn producten maal het aantal stuks",
        ],
        antwoord=0,
        uitleg="Toegevoegde waarde is wat een bedrijf zelf aan waarde heeft toegevoegd: de verkoopwaarde min de intermediaire aankopen bij andere bedrijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een meubelmaker koopt voor 400 euro hout en verkoopt een kast voor 1 100 euro. Hoeveel bedraagt zijn toegevoegde waarde?",
        opties=[
            "700 euro",
            "1 100 euro",
            "1 500 euro",
            "400 euro",
        ],
        antwoord=0,
        uitleg="1 100 min 400 is 700 euro. Dat is het stuk dat hij zelf heeft toegevoegd met zijn arbeid, zijn machines en zijn vakkennis.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de keten van bedrijven van grondstof tot eindproduct? Schrijf één woord.",
        antwoord=["bedrijfskolom", "bedrijfskolommen"],
        uitleg="Een bedrijfskolom zet alle opeenvolgende schakels op een rij, van grondstof over verwerking en groothandel tot de verkoop aan de eindverbruiker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom tel je in een bedrijfskolom de toegevoegde waarden op en niet de omzetten?",
        opties=[
            "Anders tel je dezelfde waarde meerdere keren mee",
            "Anders komen de lonen van de werknemers er niet in voor",
            "Anders vergeet je de belasting die elke schakel betaalt",
            "Anders zit de winst van de laatste schakel er dubbel in",
        ],
        antwoord=0,
        uitleg="De omzet van de bakker bevat ook de waarde van het meel dat hij kocht. Tel je alle omzetten op, dan telt het meel twee keer mee. Daarom tel je alleen wat elke schakel zelf toevoegde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijfskolom: de boer verkoopt graan voor 200, de maalderij meel voor 350, de bakker brood voor 800. Hoe groot is de toegevoegde waarde van de maalderij?",
        opties=[
            "150",
            "350",
            "450",
            "550",
        ],
        antwoord=0,
        uitleg="350 min 200 is 150. De maalderij kocht voor 200 graan en verkocht voor 350 meel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Dezelfde kolom: boer 200, maalderij 350, bakker 800. Hoe groot is de totale toegevoegde waarde?",
        opties=[
            "800",
            "1 350",
            "600",
            "450",
        ],
        antwoord=0,
        uitleg="200 plus 150 plus 450 is 800. Dat is ook precies de prijs van het eindproduct: de som van de toegevoegde waarden is de waarde van het eindproduct.",
    ),
    dict(
        type="waarofniet",
        vraag="De som van alle toegevoegde waarden in een bedrijfskolom is gelijk aan de waarde van het eindproduct.",
        antwoord=True,
        uitleg="Elke schakel voegt een stukje toe, en samen vormen die stukjes precies de prijs van het eindproduct.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het bruto binnenlands product van een land?",
        opties=[
            "De som van alle toegevoegde waarden die in dat land in een jaar gemaakt zijn",
            "De som van alle inkomens die de inwoners van dat land in een jaar kregen",
            "De waarde van alles wat de bedrijven van dat land in een jaar verkochten",
            "De waarde van alle goederen die een land in een jaar heeft uitgevoerd",
        ],
        antwoord=0,
        uitleg="Het bbp telt alle toegevoegde waarden op die binnen de grenzen van een land geproduceerd zijn, in één jaar. Waar de eigenaar van het bedrijf vandaan komt, maakt daarbij niet uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een Duits bedrijf produceert in een fabriek in Gent. Waar telt die productie mee? Duid alles aan wat juist is.",
        opties=[
            "In het Belgische bbp, want ze gebeurt op Belgisch grondgebied",
            "Niet in het Duitse bbp, want ze gebeurt niet in Duitsland",
            "In de Belgische statistieken van Statbel",
            "In het Duitse bbp, want het bedrijf is Duits",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het woord binnenlands slaat op de plaats van de productie, niet op de eigenaar. Alles wat op Belgisch grondgebied geproduceerd wordt, telt mee in het Belgische bbp.",
    ),
    dict(
        type="waarofniet",
        vraag="Werk dat je gratis thuis doet, zoals koken voor je gezin, telt mee in het bbp.",
        antwoord=False,
        uitleg="Alleen productie die via een markt verloopt, komt in het bbp. Huishoudelijk werk en vrijwilligerswerk zijn wel waardevol, maar ze worden niet geteld. Dat is een bekende beperking van het bbp.",
    ),
    dict(
        type="invultekst",
        vraag="Waar staat de afkorting bbp voor? Schrijf drie woorden.",
        antwoord=["bruto binnenlands product"],
        uitleg="Bbp is het bruto binnenlands product: de som van de toegevoegde waarden binnen de landsgrenzen in een jaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over toegevoegde waarde kloppen? Duid alles aan wat juist is.",
        opties=[
            "Ze wordt verdeeld onder de productiefactoren, als loon, intrest, pacht en winst",
            "Ze is de omzet min de aankopen bij andere bedrijven",
            "Ze wordt opgeteld om tot het bbp te komen",
            "Ze is altijd gelijk aan de winst van het bedrijf",
        ],
        antwoord=[0, 1, 2],
        uitleg="De toegevoegde waarde is wat er te verdelen valt over wie meewerkte: lonen, intresten, pacht en winst. De winst is dus maar een deel ervan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een transportbedrijf dat goederen van de haven naar een winkel brengt, voegt waarde toe.",
        antwoord=True,
        uitleg="Diensten zijn ook productie. Een goed dat in de winkel ligt, is meer waard dan hetzelfde goed in de haven: dat verschil is de toegevoegde waarde van het transport.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bedrijf met veel omzet heeft altijd ook een grote toegevoegde waarde.",
        antwoord=False,
        uitleg="Een handelaar kan enorm veel omzet draaien en toch weinig toevoegen, als hij bijna alles duur inkoopt en met een kleine marge doorverkoopt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat telt niet mee in het bbp van dit jaar?",
        opties=[
            "De verkoop van een tweedehandswagen tussen twee particulieren",
            "De bouw van een nieuw huis dit jaar",
            "De knipbeurt bij een kapper deze maand",
            "Het loon van een leerkracht dit schooljaar",
        ],
        antwoord=0,
        uitleg="Een tweedehandswagen werd in zijn bouwjaar al meegeteld. Hem doorverkopen voegt geen nieuwe productie toe; alleen de commissie van een handelaar zou meetellen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de omzet min de aankopen bij andere bedrijven? Schrijf twee woorden.",
        antwoord=["toegevoegde waarde"],
        uitleg="Dat is de toegevoegde waarde: het deel van de waarde dat dit bedrijf er zelf bij gemaakt heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat het woord bruto in bruto binnenlands product?",
        opties=[
            "Omdat de slijtage van machines en gebouwen er nog niet is afgetrokken",
            "Omdat de belastingen er nog niet zijn afgetrokken",
            "Omdat de invoer uit het buitenland er nog in zit",
            "Omdat de lonen er nog niet zijn uitbetaald",
        ],
        antwoord=0,
        uitleg="Bruto wil zeggen vóór afschrijvingen. Trek je de waardevermindering van de kapitaalgoederen af, dan krijg je het netto binnenlands product.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een garagist koopt onderdelen voor 1 200 euro, betaalt 2 000 euro lonen en factureert 4 500 euro aan klanten. Hoe groot is zijn toegevoegde waarde?",
        opties=[
            "3 300 euro",
            "1 300 euro",
            "2 500 euro",
            "4 500 euro",
        ],
        antwoord=0,
        uitleg="4 500 min 1 200 aankopen is 3 300 euro. De lonen trek je niet af: die worden net uit de toegevoegde waarde betaald.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het bbp een stroomgrootheid en geen voorraadgrootheid?",
        opties=[
            "Omdat het een hoeveelheid per periode meet, namelijk per jaar",
            "Omdat het geld meet dat door de economie stroomt tussen de actoren",
            "Omdat het alleen de uitvoer en de invoer van een land optelt",
            "Omdat het van jaar tot jaar verandert en nooit gelijk blijft",
        ],
        antwoord=0,
        uitleg="Een stroomgrootheid hoort bij een tijdvak: het bbp is altijd het bbp van een jaar. Een voorraadgrootheid hoort bij een moment, zoals het vermogen op 31 december.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen het nominale en het reële bbp?",
        opties=[
            "Het reële bbp is gecorrigeerd voor de prijzen, het nominale niet",
            "Het reële bbp telt alleen de goederen mee, het nominale ook alle diensten",
            "Het nominale bbp is per inwoner, het reële voor het hele land",
            "Het nominale bbp is van vorig jaar, het reële van dit jaar",
        ],
        antwoord=0,
        uitleg="Het nominale bbp rekent met de prijzen van het jaar zelf. Het reële bbp rekent met de prijzen van een vast basisjaar, zodat je ziet of er écht meer geproduceerd is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een land produceert dit jaar evenveel stuks als vorig jaar, maar alle prijzen stegen met 4 %. Wat gebeurt er?",
        opties=[
            "Het nominale bbp stijgt en het reële bbp blijft gelijk",
            "Allebei stijgen ze met 4 %",
            "Het reële bbp stijgt en het nominale blijft gelijk",
            "Allebei blijven ze gelijk",
        ],
        antwoord=0,
        uitleg="In euro's van dit jaar is alles 4 % duurder, dus het nominale bbp stijgt. In hoeveelheid is er niets bij gekomen, dus het reële bbp blijft gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het nominale bbp stijgt met 5 % en de prijzen stijgen met 2 %. Hoe groot is de reële groei ongeveer?",
        opties=[
            "Ongeveer 3 %",
            "Ongeveer 7 %",
            "Ongeveer 2,5 %",
            "Ongeveer 10 %",
        ],
        antwoord=0,
        uitleg="Je trekt de prijsstijging van de nominale groei af: 5 min 2 is ongeveer 3 % reële groei. Dat is het stuk dat echt meer productie is.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het bbp gedeeld door het aantal inwoners? Schrijf drie woorden.",
        antwoord=["bbp per capita", "bbp per inwoner"],
        uitleg="Het bbp per capita is het bbp per inwoner. Daarmee kan je landen van heel verschillende grootte met elkaar vergelijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een land heeft een bbp van 600 miljard euro en 12 miljoen inwoners. Hoe groot is het bbp per capita?",
        opties=[
            "50 000 euro",
            "5 000 euro",
            "72 000 euro",
            "500 000 euro",
        ],
        antwoord=0,
        uitleg="600 miljard gedeeld door 12 miljoen is 50 000 euro per inwoner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vergelijk je landen liever met het bbp per capita dan met het bbp zelf?",
        opties=[
            "Omdat een groot land anders rijker lijkt dan een klein land",
            "Omdat het bbp per capita de stijging van de prijzen uitschakelt",
            "Omdat het bbp zelf de diensten niet meetelt",
            "Omdat het bbp per capita ook het zwartwerk meetelt",
        ],
        antwoord=0,
        uitleg="India heeft een veel groter bbp dan Luxemburg, maar ook veel meer inwoners. Per inwoner ligt de verhouding net omgekeerd.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stijging van het nominale bbp betekent altijd dat er meer geproduceerd is.",
        antwoord=False,
        uitleg="Het nominale bbp kan alleen stijgen doordat de prijzen stegen. Pas het reële bbp zegt of er écht meer geproduceerd is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het bbp van een land gaat van 400 naar 420 miljard euro. Hoeveel bedraagt de groei?",
        opties=[
            "5 %",
            "20 %",
            "4,8 %",
            "2 %",
        ],
        antwoord=0,
        uitleg="De aangroei is 20 miljard op 400 miljard, en 20 gedeeld door 400 is 0,05, dus 5 %.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen zet je om de reële groei te berekenen? Duid alles aan wat juist is.",
        opties=[
            "Je rekent de bbp-cijfers om naar de prijzen van hetzelfde basisjaar",
            "Je berekent daarna de procentuele verandering tussen de twee jaren",
            "Je zet dat cijfer naast de nominale groei om het prijseffect te zien",
            "Je deelt het bbp van beide jaren eerst door het aantal inwoners",
        ],
        antwoord=[0, 1, 2],
        uitleg="Reële groei vraagt dezelfde prijzen in beide jaren. Delen door het aantal inwoners geeft het bbp per capita, en dat is een andere berekening.",
    ),
    dict(
        type="waarofniet",
        vraag="Als het nominale bbp met 2 % stijgt en de prijzen met 3 %, dan is de reële groei negatief.",
        antwoord=True,
        uitleg="2 min 3 is min 1 %. In euro's is er meer, maar in hoeveelheid is er minder geproduceerd dan het jaar ervoor.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de Belgische overheidsdienst voor de statistiek? Schrijf één woord.",
        antwoord=["statbel"],
        uitleg="Statbel publiceert de officiële Belgische statistieken. De Nationale Bank van België publiceert de cijfers over de economie en de financiën.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je de cijfers van de Nationale Bank van België?",
        opties=[
            "Om de Belgische economie en de financiële gegevens op te volgen",
            "Om te weten hoeveel elk bedrijf in België aan zijn eigen werknemers betaalt",
            "Om de prijzen van de winkels in elke gemeente te vergelijken",
            "Om te berekenen hoeveel belasting jij persoonlijk moet betalen",
        ],
        antwoord=0,
        uitleg="De Nationale Bank publiceert onder meer de groei, de inflatie en de balansen die bedrijven er neerleggen. Individuele lonen en gemeentelijke prijzen vind je er niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een tabel staat: 2026 bbp 500, 2027 bbp 530, prijsstijging 2 %. Wat kan je besluiten?",
        opties=[
            "De nominale groei is 6 % en de reële groei ongeveer 4 %",
            "De nominale groei is 4 % en de reële groei ongeveer 6 %",
            "De nominale en de reële groei zijn allebei 6 %",
            "Er is geen groei, want de prijzen stegen ook",
        ],
        antwoord=0,
        uitleg="30 op 500 is 6 % nominale groei. Daar haal je de prijsstijging van 2 % af, en dan hou je ongeveer 4 % reële groei over.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het vergelijken van het bbp van twee jaren moet je altijd met dezelfde prijzen rekenen.",
        antwoord=True,
        uitleg="Anders meet je deels de inflatie in plaats van de productie. Daarom werkt men met het reële bbp, uitgedrukt in de prijzen van een basisjaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het bbp van een land stijgt met 2 %, de bevolking met 3 %. Wat gebeurt er met het bbp per capita?",
        opties=[
            "Het daalt",
            "Het stijgt",
            "Het blijft gelijk",
            "Dat kan je met deze gegevens niet weten",
        ],
        antwoord=0,
        uitleg="De koek groeit trager dan het aantal eters, dus er blijft per inwoner minder over. Het bbp per capita daalt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het jaar waarvan je de prijzen gebruikt om reëel te rekenen? Schrijf één woord.",
        antwoord=["basisjaar", "referentiejaar"],
        uitleg="In het basisjaar zijn het nominale en het reële bbp aan elkaar gelijk, want daar reken je met de prijzen van dat jaar zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke beperkingen heeft het bbp als maatstaf? Duid alles aan wat juist is.",
        opties=[
            "Het telt onbetaald werk niet mee",
            "Het zegt niets over hoe de welvaart verdeeld is",
            "Het houdt geen rekening met schade aan het milieu",
            "Het is te moeilijk om van jaar tot jaar te vergelijken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het bbp meet productie, niet geluk of rechtvaardigheid. Vergelijken over de jaren heen gaat net wél, zolang je het reële bbp gebruikt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Na een storm worden er veel daken hersteld. Wat doet dat met het bbp?",
        opties=[
            "Het bbp stijgt, ook al is het land er niet beter aan toe",
            "Het bbp daalt, want er is schade aangericht aan de gebouwen van het land",
            "Het bbp blijft gelijk, want herstellen is geen echte productie",
            "Het bbp daalt eerst en stijgt daarna weer tot hetzelfde punt",
        ],
        antwoord=0,
        uitleg="Herstellingen zijn betaalde productie, dus ze tellen mee. Dat toont meteen de beperking: een hoger bbp betekent niet automatisch dat het beter gaat.",
    ),
    dict(
        type="waarofniet",
        vraag="In het basisjaar ligt het reële bbp altijd hoger dan het nominale bbp.",
        antwoord=False,
        uitleg="In het basisjaar zijn ze precies aan elkaar gelijk: je rekent dan met de prijzen van dat jaar zelf, dus er valt niets te corrigeren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe lees je een grafiek met de jaarlijkse groeicijfers van een land het best?",
        opties=[
            "Je let op het teken: een lagere staaf is nog altijd groei",
            "Je leest elke staaf die daalt als een krimp van de hele economie",
            "Je vergelijkt alleen de hoogste en de laagste staaf met elkaar",
            "Je telt alle staven op om het bbp van dat land te krijgen",
        ],
        antwoord=0,
        uitleg="Een groeicijfer dat van 3 % naar 1 % zakt, betekent dat de economie trager groeit, niet dat ze krimpt. Pas bij een negatief cijfer is er krimp.",
    ),
]

# -*- coding: utf-8 -*-
"""Ontwikkeling: de humanistische en de systemische benadering.

De laatste twee van de zes benaderingen. De humanistische vertrekt bij wat een
mens zelf wil worden, de systemische bij alles wat rond iemand staat.

De namen en de lijstjes staan letterlijk in de fiche:

    humanistische benadering
        motivatietheorie: Abraham Maslow
        client centered therapy: Carl Rogers
    systemische benadering
        bio-ecologisch model: Urie Bronfenbrenner - microsysteem,
            mesosysteem, exosysteem, macrosysteem, chronosysteem, directe en
            indirecte interacties, structurele kenmerken van de omgeving
        sociaal-culturele theorie: Lev Vygotsky - comfortzone, angstzone,
            zone van de naaste ontwikkeling, groeizone, scaffolding,
            interiorisatieproces

Het bio-ecologisch model van Bronfenbrenner komt in deze fiche twee keer voor:
hier als systemische benadering van ontwikkeling, en later bij pedagogiek als
pedagogisch model. De vijf systemen zijn dus dubbel nuttig om te kennen.

De fiche zet comfortzone, angstzone, zone van de naaste ontwikkeling en
groeizone naast elkaar als vier begrippen van Vygotsky. De vragen hieronder
vragen daarom wat elke zone betekent, en niet welke zone nu precies dezelfde
is als een andere.

Deel 1 is de humanistische benadering.
Deel 2 is de systemische benadering.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waar vertrekt de humanistische benadering van ontwikkeling?",
        opties=[
            "bij wat een mens zelf wil worden",
            "bij wat de genen van een mens vastleggen",
            "bij de beloning die op gedrag volgt",
            "bij de cultuur waarin iemand opgroeit",
        ],
        antwoord=0,
        uitleg="De humanistische benadering gaat ervan uit dat een mens zelf richting geeft aan zijn leven en wil groeien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee theorieën horen volgens de fiche bij de humanistische benadering?",
        opties=[
            "de motivatietheorie",
            "de client centered therapy",
            "de rijpingstheorie",
            "de sociaal-culturele theorie",
        ],
        antwoord=[0, 1],
        uitleg="De motivatietheorie van Maslow en de client centered therapy van Rogers.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de motivatietheorie?",
        opties=[
            "Abraham Maslow",
            "Carl Rogers",
            "Urie Bronfenbrenner",
            "Lev Vygotsky",
        ],
        antwoord=0,
        uitleg="Maslow. Zijn motivatietheorie zet de behoeften van een mens in een orde, van de meest basale tot de hoogste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de client centered therapy?",
        opties=[
            "Carl Rogers",
            "Abraham Maslow",
            "Sigmund Freud",
            "Albert Bandura",
        ],
        antwoord=0,
        uitleg="Rogers. Client centered betekent dat de persoon zelf het midden van de begeleiding is, en niet de methode.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke behoefte staat bij Maslow onderaan, en moet dus eerst vervuld zijn?",
        opties=[
            "de lichamelijke behoeften, zoals eten en slapen",
            "de behoefte aan waardering en erkenning van anderen",
            "de behoefte om jezelf te ontplooien",
            "de behoefte aan contact met vrienden",
        ],
        antwoord=0,
        uitleg="Onderaan staan de lichamelijke behoeften. Wie honger heeft of niet slaapt, komt niet aan de hogere behoeften toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke behoefte staat bij Maslow bovenaan?",
        opties=[
            "de behoefte om jezelf te ontplooien",
            "de behoefte aan veiligheid en zekerheid",
            "de behoefte aan eten en slapen",
            "de behoefte aan contact met anderen",
        ],
        antwoord=0,
        uitleg="Bovenaan staat de zelfontplooiing: worden wie je kan worden. Maslow noemt dat zelfactualisatie.",
    ),
    dict(
        type="invultekst",
        vraag="De naam uit de fiche bij de motivatietheorie is Abraham ...",
        antwoord=["Maslow"],
        uitleg="Abraham Maslow. Zijn theorie wordt vaak als een piramide van behoeften getekend.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Maslow komt een kind pas aan leren en zich ontplooien toe als zijn lagere behoeften genoeg vervuld zijn.",
        antwoord=True,
        uitleg="Waar. Daarom is deze theorie zo bruikbaar op school: een kind dat honger heeft of zich onveilig voelt, leert moeilijk.",
    ),
    dict(
        type="waarofniet",
        vraag="De humanistische benadering geeft op de tweede basisvraag vooral een antwoord in de richting van nature.",
        antwoord=False,
        uitleg="Niet waar. Ze geeft veel plaats aan zelfbepaling: een mens kiest zelf mee welke richting hij neemt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een begeleider zegt: ik ga niet voorschrijven wat jij moet doen, ik volg waar jij naartoe wil. Bij welke theorie sluit dat aan?",
        opties=[
            "de client centered therapy van Rogers",
            "de operante conditionering van Skinner",
            "de psychoanalyse van Freud",
            "de rijpingstheorie van Gesell",
        ],
        antwoord=0,
        uitleg="Bij Rogers staat de persoon zelf in het midden. De begeleider gaat mee, in plaats van een plan voor te schrijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke houdingen horen bij de begeleider in de client centered therapy van Rogers?",
        opties=[
            "de ander aanvaarden zoals hij is",
            "echt en open zijn over jezelf",
            "je kunnen inleven in de ander",
            "voor de ander beslissen wat goed is",
        ],
        antwoord=[0, 1, 2],
        uitleg="Rogers noemt aanvaarding, echtheid en inleving. Beslissen voor de ander hoort er juist niet bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling in een vluchtwoning kan zich niet op school concentreren omdat hij niet weet waar hij volgende maand woont. Welke behoefte van Maslow is hier niet vervuld?",
        opties=[
            "de behoefte aan veiligheid en zekerheid",
            "de behoefte aan waardering",
            "de behoefte aan zelfontplooiing",
            "de lichamelijke behoeften",
        ],
        antwoord=0,
        uitleg="Niet weten waar je gaat wonen raakt de veiligheid en de zekerheid, de tweede laag bij Maslow.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een bezwaar dat vaak tegen de theorie van Maslow wordt ingebracht?",
        opties=[
            "de orde van de behoeften klopt niet bij iedereen",
            "ze noemt alleen lichamelijke en sociale behoeften",
            "ze geeft geen plaats aan zelfontplooiing",
            "ze is nooit op mensen toegepast",
        ],
        antwoord=0,
        uitleg="Mensen zetten soms een hogere behoefte voorop terwijl een lagere niet vervuld is. De vaste orde houdt dus niet altijd stand.",
    ),
    dict(
        type="waarofniet",
        vraag="Zelfontplooiing bij Maslow betekent dat iemand meer wil zijn dan de anderen.",
        antwoord=False,
        uitleg="Niet waar. Het betekent worden wie je zelf kan worden. Het is geen vergelijking met anderen.",
    ),
    dict(
        type="waarofniet",
        vraag="Maslow en Rogers horen beide bij de humanistische benadering.",
        antwoord=True,
        uitleg="Waar. De fiche zet precies die twee namen bij de humanistische benadering.",
    ),
    dict(
        type="invultekst",
        vraag="De therapievorm van Rogers waarin de persoon zelf het midden is, heet in de fiche de client ... therapy.",
        antwoord=["centered"],
        uitleg="Client centered therapy. De fiche gebruikt de Engelse naam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk antwoord geeft de humanistische benadering op de eerste basisvraag?",
        opties=[
            "eerder continu, want groeien gaat bij haar geleidelijk",
            "eerder discontinu, want ze werkt met vaste stadia en fasen",
            "ze geeft er geen antwoord op",
            "even continu als discontinu",
        ],
        antwoord=0,
        uitleg="Maslow en Rogers werken niet met vaste stadia maar met een groei die doorloopt. Dat is eerder continu.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het grote verschil tussen de humanistische en de behavioristische benadering?",
        opties=[
            "bij de ene kiest de mens zelf, bij de andere de omgeving",
            "bij de ene bestaat leren niet, bij de andere wel",
            "de ene werkt met fasen, de andere met geheugen",
            "de ene geldt voor kinderen, de andere voor volwassenen",
        ],
        antwoord=0,
        uitleg="Het behaviorisme legt de sturing buiten de persoon, bij prikkels en gevolgen. De humanistische benadering legt ze bij de persoon zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een school zorgt eerst voor een ontbijt en een vast klasritme, en pas daarna voor extra uitdaging. Welke theorie zie je aan het werk?",
        opties=[
            "de motivatietheorie van Maslow",
            "de klassieke conditionering van Pavlov",
            "de theorie van Piaget",
            "het bio-ecologisch model",
        ],
        antwoord=0,
        uitleg="Eerst de lagere behoeften, dan de hogere: dat is precies de orde van Maslow.",
    ),
    dict(
        type="invultekst",
        vraag="Het begrip van Maslow voor worden wie je kan worden, bovenaan zijn piramide, is zelf...",
        antwoord=["ontplooiing", "zelfontplooiing", "actualisatie"],
        uitleg="Zelfontplooiing, ook zelfactualisatie genoemd. Het is de hoogste laag van zijn motivatietheorie.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waar kijkt de systemische benadering van ontwikkeling naar?",
        opties=[
            "naar alles wat rond iemand staat en op hem inwerkt",
            "naar de genen en de rijping van het lichaam",
            "naar de krachten binnen in iemand",
            "naar het gedrag dat beloond of bestraft wordt",
        ],
        antwoord=0,
        uitleg="Een systeem is een geheel waar iemand in zit: het gezin, de klas, de buurt, de samenleving. Die systemen beïnvloeden elkaar ook.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee theorieën horen volgens de fiche bij de systemische benadering?",
        opties=[
            "het bio-ecologisch model",
            "de sociaal-culturele theorie",
            "de motivatietheorie",
            "de informatieverwerkingstheorie",
        ],
        antwoord=[0, 1],
        uitleg="Het bio-ecologisch model van Bronfenbrenner en de sociaal-culturele theorie van Vygotsky.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel systemen onderscheidt Bronfenbrenner?",
        opties=[
            "vijf",
            "drie",
            "vier",
            "zes",
        ],
        antwoord=0,
        uitleg="Vijf: het micro-, het meso-, het exo-, het macro- en het chronosysteem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het gezin en de klas van een kind horen bij welk systeem van Bronfenbrenner?",
        opties=[
            "het microsysteem",
            "het mesosysteem",
            "het exosysteem",
            "het macrosysteem",
        ],
        antwoord=0,
        uitleg="Het microsysteem is waar het kind zelf dagelijks in zit. Daar zijn de interacties direct.",
    ),
    dict(
        type="meerkeuze",
        vraag="De juf belt met de ouders van Sara over haar huiswerk. Welk systeem van Bronfenbrenner is dit?",
        opties=[
            "het mesosysteem",
            "het microsysteem",
            "het exosysteem",
            "het chronosysteem",
        ],
        antwoord=0,
        uitleg="Het mesosysteem is de verbinding tussen twee microsystemen. Hier school en gezin, die met elkaar in contact staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="De vader van Tom krijgt op zijn werk nachtdienst, waardoor Tom hem minder ziet. Welk systeem van Bronfenbrenner is dit?",
        opties=[
            "het exosysteem",
            "het microsysteem",
            "het macrosysteem",
            "het mesosysteem",
        ],
        antwoord=0,
        uitleg="Het exosysteem werkt indirect: Tom zit niet zelf op dat werk, maar ondervindt er wel de gevolgen van.",
    ),
    dict(
        type="meerkeuze",
        vraag="De wetten en de waarden van een land horen bij welk systeem van Bronfenbrenner?",
        opties=[
            "het macrosysteem",
            "het exosysteem",
            "het mesosysteem",
            "het chronosysteem",
        ],
        antwoord=0,
        uitleg="Het macrosysteem is de grote laag errond: de cultuur, de wetten, de waarden van een samenleving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kind groeit op in een tijd waarin iedereen een smartphone heeft, terwijl zijn ouders zonder opgroeiden. Welk systeem van Bronfenbrenner is dit?",
        opties=[
            "het chronosysteem",
            "het macrosysteem",
            "het exosysteem",
            "het microsysteem",
        ],
        antwoord=0,
        uitleg="Het chronosysteem gaat over de tijd: wat verandert in de loop van iemands leven en tussen generaties.",
    ),
    dict(
        type="invultekst",
        vraag="Het systeem van Bronfenbrenner dat over de tijd en over veranderingen gaat, is het ...systeem.",
        antwoord=["chrono", "chronosysteem"],
        uitleg="Het chronosysteem. Chronos is het Griekse woord voor tijd.",
    ),
    dict(
        type="waarofniet",
        vraag="In het microsysteem zijn de interacties direct, in het exosysteem indirect.",
        antwoord=True,
        uitleg="Waar. De fiche noemt directe en indirecte interacties apart. In het microsysteem zit het kind zelf, in het exosysteem niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Bronfenbrenner werken de systemen één na één op een kind in, zonder elkaar te raken.",
        antwoord=False,
        uitleg="Niet waar. Ze werken juist door elkaar. Een wet uit het macrosysteem verandert het werk van een ouder, en dat verandert het gezin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de sociaal-culturele theorie?",
        opties=[
            "Lev Vygotsky",
            "Urie Bronfenbrenner",
            "Jean Piaget",
            "Carl Rogers",
        ],
        antwoord=0,
        uitleg="Vygotsky. Hij legt de nadruk op leren samen met anderen en op de rol van de cultuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is bij Vygotsky de comfortzone?",
        opties=[
            "wat iemand al zelfstandig kan",
            "wat iemand met hulp kan",
            "wat voor iemand nog veel te moeilijk is",
            "wat iemand van iemand anders nadoet",
        ],
        antwoord=0,
        uitleg="In de comfortzone lukt het al alleen. Daar zit geen leerwinst meer, want er valt niets bij te leren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er volgens Vygotsky als een opdracht in de angstzone valt?",
        opties=[
            "het leren valt stil, want het is te moeilijk",
            "het leren gaat sneller, want de spanning helpt",
            "het leren blijft gelijk, maar duurt langer",
            "het leren lukt alleen nog met een beloning",
        ],
        antwoord=0,
        uitleg="In de angstzone is de afstand te groot. Een kind blokkeert en leert niets meer bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt Vygotsky met de zone van de naaste ontwikkeling?",
        opties=[
            "wat iemand nog niet alleen kan, maar wel met hulp",
            "wat iemand ook zonder enige hulp al alleen kan",
            "wat iemand nooit zal kunnen",
            "wat iemand vorig jaar al kon",
        ],
        antwoord=0,
        uitleg="De zone van de naaste ontwikkeling is de ruimte tussen wat een kind alleen kan en wat het met hulp kan. Daar zit de leerwinst.",
    ),
    dict(
        type="invultekst",
        vraag="De hulp die je geeft en stap voor stap weer afbouwt, zoals een steiger aan een gebouw, heet bij Vygotsky ...",
        antwoord=["scaffolding"],
        uitleg="Scaffolding, van het Engelse woord voor steiger. De steun gaat weg zodra het kind het zelf kan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het interiorisatieproces bij Vygotsky?",
        opties=[
            "wat eerst samen met anderen gebeurt, wordt eigen denken",
            "wat eerst eigen denken is, wordt later samen gedaan",
            "wat je leert, verdwijnt na een tijd weer",
            "wat je ziet, doe je onmiddellijk na",
        ],
        antwoord=0,
        uitleg="Interioriseren betekent naar binnen nemen. Een kind telt eerst luidop met de juf, en later in zijn hoofd.",
    ),
    dict(
        type="waarofniet",
        vraag="Scaffolding betekent dat je de hulp zo lang mogelijk blijft geven.",
        antwoord=False,
        uitleg="Niet waar. Een steiger gaat weg als het gebouw staat. De hulp wordt juist stap voor stap afgebouwd.",
    ),
    dict(
        type="waarofniet",
        vraag="Vygotsky geeft op de derde basisvraag eerder het antwoord dat ontwikkeling cultureel bepaald is.",
        antwoord=True,
        uitleg="Waar. Zijn theorie heet sociaal-cultureel: wat een kind leert en hoe het leert, hangt af van de cultuur rond hem.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerkracht geeft een leerling eerst een voorbeeld, dan een half voorbeeld, en dan niets meer. Welke twee begrippen van Vygotsky zie je hier?",
        opties=[
            "scaffolding",
            "de zone van de naaste ontwikkeling",
            "het chronosysteem",
            "de erogene lichaamszone",
        ],
        antwoord=[0, 1],
        uitleg="De hulp die afgebouwd wordt is scaffolding, en de opdracht lag net boven wat de leerling alleen kon: de zone van de naaste ontwikkeling.",
    ),
]

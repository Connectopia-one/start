# -*- coding: utf-8 -*-
"""De vragen voor "Facturen, kortingen en btw" (🚀 Boost doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
bedrijfswetenschappen: het controleren en berekenen van een aankoop- en
verkoopfactuur met handelskorting, financiële korting, bijkomende of
doorgerekende kosten, terugstuurbare verpakking en btw, de creditnota en de
indeling van de aankopen. Het boeken zelf staat in [[bw_boekhouden]].

Deel 1 gaat over de twee kortingen en over de maatstaf van heffing.
Deel 2 gaat over de doorgerekende kosten, de terugstuurbare verpakking, de btw,
de creditnota en de soorten aankopen.

De orde van rekenen is altijd dezelfde: brutoprijs, min handelskorting, min
financiële korting, plus de doorgerekende kosten. Dat is de maatstaf van
heffing. Daarop komt de btw, en de terugstuurbare verpakking komt pas na de btw
bij het totaal. Het tarief in de vragen is 21 procent.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een handelskorting?",
        opties=[
            "Een korting op de prijs",
            "Een korting omdat je snel betaalt",
            "Een vergoeding voor het vervoer van goederen",
            "Een waarborg die je voor de verpakking betaalt",
        ],
        antwoord=0,
        uitleg="Een handelskorting is een vermindering van de prijs zelf, bijvoorbeeld bij een grote afname of voor een vaste klant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welk bedrag reken je de financiële korting?",
        opties=[
            "Op de prijs na de handelskorting",
            "Op de brutoprijs zoals in de catalogus",
            "Op het factuurtotaal met de btw erbij",
            "Op het bedrag van de terugstuurbare verpakking",
        ],
        antwoord=0,
        uitleg="Eerst gaat de handelskorting eraf, daarna reken je de financiële korting op wat er dan overblijft.",
    ),
    dict(
        type="waarofniet",
        vraag="Een handelskorting verlaagt het bedrag waarop je btw rekent.",
        antwoord=True,
        uitleg="De handelskorting gaat eraf voor je de btw berekent. Minder prijs betekent dus ook minder btw.",
    ),
    dict(
        type="waarofniet",
        vraag="Een financiële korting trek je enkel van de btw-basis af als de klant er echt gebruik van maakt.",
        antwoord=False,
        uitleg="De financiële korting gaat altijd van de maatstaf van heffing af, ook als de klant later gewoon het volle bedrag betaalt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het bedrag waarop je de btw berekent?",
        antwoord=["maatstaf van heffing", "maatstaf", "heffingsmaatstaf"],
        uitleg="Dat is de maatstaf van heffing: de prijs na de kortingen en met de doorgerekende kosten erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="De goederen kosten 1 000 euro. De leverancier geeft 10 procent handelskorting. Wat blijft er over?",
        opties=[
            "900 euro",
            "100 euro na de korting",
            "990 euro na de korting erop",
            "1 100 euro met de korting erbij",
        ],
        antwoord=0,
        uitleg="10 procent van 1 000 euro is 100 euro korting. Er blijft 1 000 − 100 = 900 euro over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Na de handelskorting blijft er 900 euro over. De financiële korting is 2 procent. Hoeveel is die korting?",
        opties=[
            "18 euro",
            "20 euro op de brutoprijs",
            "180 euro, een tiende van het bedrag",
            "2 euro, want het tarief is 2 procent",
        ],
        antwoord=0,
        uitleg="2 procent van 900 euro is 18 euro. Na beide kortingen blijft er 882 euro over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat verlaagt de maatstaf van heffing? Duid alles aan wat juist is.",
        opties=[
            "De handelskorting",
            "De financiële korting",
            "De doorgerekende vervoerkosten",
            "De btw op de factuur",
        ],
        antwoord=[0, 1],
        uitleg="De twee kortingen gaan eraf vóór de btw. Doorgerekende kosten doen de maatstaf juist stijgen, en de btw is het resultaat, geen onderdeel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom geeft een leverancier een financiële korting?",
        opties=[
            "Om snel betaald te worden",
            "Om een grotere hoeveelheid te verkopen",
            "Om de vervoerkosten te kunnen doorrekenen",
            "Om de verpakking niet terug te moeten nemen",
        ],
        antwoord=0,
        uitleg="Wie binnen enkele dagen betaalt, krijgt een kleine korting. De leverancier heeft zijn geld sneller en loopt minder risico.",
    ),
    dict(
        type="waarofniet",
        vraag="Een handelskorting kan op de factuur staan in procent of in euro.",
        antwoord=True,
        uitleg="Beide komen voor: 10 procent korting of 100 euro korting. Het effect op de maatstaf van heffing is hetzelfde.",
    ),
    dict(
        type="waarofniet",
        vraag="Een financiële korting is hetzelfde als een handelskorting.",
        antwoord=False,
        uitleg="Een handelskorting hangt af van de aankoop zelf, een financiële korting van het moment van betalen. Ze volgen ook in die orde op de factuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="De brutoprijs is 2 000 euro, de handelskorting 25 procent. Wat blijft er over?",
        opties=[
            "1 500 euro",
            "500 euro na de korting",
            "1 975 euro na de korting erop",
            "2 500 euro met de korting erbij",
        ],
        antwoord=0,
        uitleg="25 procent van 2 000 euro is 500 euro. Er blijft 2 000 − 500 = 1 500 euro over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er op een aankoopfactuur? Duid alles aan wat juist is.",
        opties=[
            "De goederen met hun prijs",
            "De btw",
            "De vervaldag",
            "De winst van de leverancier",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een factuur vermeldt wat er geleverd is, tegen welke prijs, met welke kortingen, kosten en btw, en tegen wanneer je moet betalen. Wat de leverancier eraan verdient, staat er niet op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel is 20 procent handelskorting op 500 euro?",
        opties=[
            "100 euro",
            "20 euro, het tarief zelf",
            "400 euro, wat er overblijft",
            "480 euro, de prijs na de korting",
        ],
        antwoord=0,
        uitleg="20 procent van 500 euro is 100 euro korting. De prijs na de korting is 400 euro, maar de vraag was naar de korting zelf.",
    ),
    dict(
        type="invultekst",
        vraag="Welke korting krijg je als je de factuur snel betaalt?",
        antwoord=["financiële", "financiele", "financiële korting", "financiele korting"],
        uitleg="Dat is de financiële korting, ook korting voor contante betaling genoemd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bedragen gaan van de prijs af vóór je de btw berekent? Duid alles aan wat juist is.",
        opties=[
            "De handelskorting",
            "De financiële korting",
            "De terugstuurbare verpakking",
            "De doorgerekende verzekering",
        ],
        antwoord=[0, 1],
        uitleg="Enkel de twee kortingen gaan eraf. De verpakking staat buiten de btw maar komt pas na de btw bij het totaal, en een doorgerekende verzekering verhoogt de maatstaf.",
    ),
    dict(
        type="meerkeuze",
        vraag="De maatstaf van heffing is 1 000 euro. Hoeveel btw komt daarbij aan 21 procent?",
        opties=[
            "210 euro",
            "21 euro, want het tarief is 21",
            "790 euro, het bedrag min de btw",
            "1 210 euro, het totaal van de factuur",
        ],
        antwoord=0,
        uitleg="21 procent van 1 000 euro is 210 euro btw. Het factuurtotaal wordt dan 1 210 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leverancier geeft 5 procent korting omdat de klant een grote hoeveelheid afneemt. Wat is dat?",
        opties=[
            "Een handelskorting",
            "Een financiële korting voor snel betalen",
            "Een waarborg op de terugstuurbare kratten",
            "Een doorgerekende kost voor het vervoer",
        ],
        antwoord=0,
        uitleg="Een korting die met de aankoop zelf te maken heeft, is een handelskorting. Ze gaat als eerste van de brutoprijs af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom geeft een leverancier een handelskorting? Duid alles aan wat juist is.",
        opties=[
            "Bij een grote hoeveelheid",
            "Aan een vaste klant",
            "Tijdens een actie",
            "Om geen btw te moeten aanrekenen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Hoeveelheid, trouwe klanten en tijdelijke acties zijn de gewone redenen. De btw ontlopen kan niet: de korting verlaagt de maatstaf, maar het tarief blijft gelden.",
    ),
    dict(
        type="meerkeuze",
        vraag="De brutoprijs is 1 000 euro, met 10 procent handelskorting en daarna 2 procent financiële korting. Wat is de maatstaf van heffing?",
        opties=[
            "882 euro",
            "880 euro na beide kortingen",
            "900 euro, enkel na de eerste korting",
            "1 000 euro, kortingen tellen niet mee",
        ],
        antwoord=0,
        uitleg="1 000 − 100 = 900 euro, en daarvan 2 procent is 18 euro. 900 − 18 = 882 euro. Let op: de tweede korting reken je op 900, niet op 1 000.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat doen doorgerekende vervoerkosten met de maatstaf van heffing?",
        opties=[
            "Ze verhogen die",
            "Ze verlagen die met hetzelfde bedrag",
            "Ze veranderen die helemaal niet",
            "Ze komen pas na de btw bij het totaal",
        ],
        antwoord=0,
        uitleg="Kosten die de leverancier doorrekent, horen bij de prijs van de levering. Ze komen dus bij de maatstaf en er zit btw op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de btw op een terugstuurbare verpakking?",
        opties=[
            "Er komt geen btw op",
            "Er komt 21 procent btw op",
            "Er komt een half tarief btw op",
            "De btw wordt later apart gefactureerd",
        ],
        antwoord=0,
        uitleg="Een terugstuurbare verpakking is geen verkoop maar een waarborg: je krijgt het bedrag terug als de kratten terugkeren. Daarom blijft ze buiten de maatstaf van heffing.",
    ),
    dict(
        type="waarofniet",
        vraag="Op doorgerekende vervoerkosten betaal je btw.",
        antwoord=True,
        uitleg="Die kosten horen bij de levering en verhogen dus de maatstaf van heffing, waarop de btw gerekend wordt.",
    ),
    dict(
        type="waarofniet",
        vraag="Op een terugstuurbare verpakking reken je ook btw.",
        antwoord=False,
        uitleg="Ze staat apart op de factuur, zonder btw, en komt pas na de btw bij het totaal.",
    ),
    dict(
        type="invultekst",
        vraag="Welk btw-tarief is in België het gewone tarief? Schrijf enkel het getal.",
        antwoord=["21", "21%"],
        uitleg="Het gewone tarief is 21 procent. Er bestaan ook verlaagde tarieven van 6 en 12 procent, onder meer voor voeding en voor woningwerken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een factuur vermeldt 1 000 euro goederen en 100 euro doorgerekend vervoer. Wat is de maatstaf van heffing?",
        opties=[
            "1 100 euro",
            "900 euro, het vervoer gaat eraf",
            "1 000 euro, het vervoer telt niet mee",
            "1 331 euro, met de btw er al bij",
        ],
        antwoord=0,
        uitleg="Doorgerekende kosten komen bij de prijs: 1 000 + 100 = 1 100 euro. De btw van 21 procent daarop is 231 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat verhoogt de maatstaf van heffing? Duid alles aan wat juist is.",
        opties=[
            "Doorgerekend vervoer",
            "Een doorgerekende verzekering",
            "Verpakking die niet terugkeert",
            "De handelskorting",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alles wat de leverancier mee aanrekent voor de levering, verhoogt de maatstaf. Een handelskorting doet het omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een klant stuurt de kratten terug. Wat gebeurt er met het bedrag van de verpakking?",
        opties=[
            "Hij krijgt het terug",
            "Hij verliest het definitief",
            "Het wordt omgezet in een korting",
            "Het blijft als schuld openstaan",
        ],
        antwoord=0,
        uitleg="Een terugstuurbare verpakking werkt als een waarborg. Komen de kratten terug, dan komt het bedrag terug, zonder btw-correctie.",
    ),
    dict(
        type="meerkeuze",
        vraag="De maatstaf van heffing is 950 euro. Hoeveel btw komt daarbij aan 21 procent?",
        opties=[
            "199,50 euro",
            "95 euro, een tiende ervan",
            "209 euro, afgerond op de euro",
            "1 149,50 euro, het hele totaal",
        ],
        antwoord=0,
        uitleg="950 × 0,21 = 199,50 euro. Het factuurtotaal wordt dan 1 149,50 euro, met de terugstuurbare verpakking er eventueel nog bij.",
    ),
    dict(
        type="waarofniet",
        vraag="Een creditnota corrigeert een factuur die al verstuurd is.",
        antwoord=True,
        uitleg="Een factuur mag je niet aanpassen. Wil je iets rechtzetten, dan maak je een creditnota die het te veel aangerekende bedrag terugneemt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een creditnota bevat nooit btw.",
        antwoord=False,
        uitleg="Draait de creditnota een verkoop met btw terug, dan staat de btw er ook op. Anders zou de staat te veel btw houden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer maakt een leverancier een creditnota? Duid alles aan wat juist is.",
        opties=[
            "Bij een terugzending",
            "Bij een te hoog bedrag",
            "Bij een korting achteraf",
            "Bij elke betaling van een factuur",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een creditnota zet iets recht: goederen die terugkomen, een rekenfout, of een korting die men vergeten was. Een gewone betaling vraagt er geen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze is een aankoop van diensten en diverse goederen?",
        opties=[
            "Een verzekeringspremie",
            "Goederen om door te verkopen",
            "Een bestelwagen voor de leveringen",
            "Een machine die tien jaar meegaat",
        ],
        antwoord=0,
        uitleg="Diensten en diverse goederen zijn werkingskosten: verzekering, huur, telefoon, onderhoud. Ze gaan niet door naar de klant en gaan niet jaren mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een aankoop van handelsgoederen?",
        opties=[
            "Goederen om door te verkopen",
            "Een machine voor de productie",
            "Een verzekering voor het gebouw",
            "Een computer die vijf jaar meegaat",
        ],
        antwoord=0,
        uitleg="Handelsgoederen koopt een onderneming aan om ze onveranderd verder te verkopen. Daarom staan ze apart van de werkingskosten en de investeringen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een document dat een eerder verzonden factuur verbetert?",
        antwoord=["creditnota", "een creditnota"],
        uitleg="Dat is een creditnota. Komt ze van je leverancier, dan heet ze een inkomende creditnota; stuur je ze zelf, dan is ze uitgaand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kosten kan een leverancier doorrekenen op zijn factuur? Duid alles aan wat juist is.",
        opties=[
            "Het vervoer",
            "Een verzekering",
            "Verpakking die niet terugkomt",
            "De btw van zijn eigen aankopen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Vervoer, verzekering en verloren verpakking mag hij aanrekenen, en er komt btw op. Zijn eigen aftrekbare btw vordert hij terug van de staat en rekent hij niet door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een factuur vermeldt 500 euro goederen, 21 procent btw en 60 euro terugstuurbare verpakking. Wat is het totaal?",
        opties=[
            "665 euro",
            "605 euro zonder de verpakking",
            "678,60 euro met btw op alles",
            "560 euro, de btw komt later",
        ],
        antwoord=0,
        uitleg="De btw is 21 procent van 500 euro, dus 105 euro. Daarna komt de verpakking erbij: 500 + 105 + 60 = 665 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat controleer je op een aankoopfactuur? Duid alles aan wat juist is.",
        opties=[
            "De kortingen",
            "De doorgerekende kosten",
            "De btw",
            "Het loon van de chauffeur",
        ],
        antwoord=[0, 1, 2],
        uitleg="Je gaat na of de afgesproken kortingen erop staan, of de aangerekende kosten kloppen en of de btw juist berekend is. Wat de leverancier zijn personeel betaalt, is zijn zaak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf koopt een computer die vijf jaar meegaat. Welke soort aankoop is dat?",
        opties=[
            "Een investeringsgoed",
            "Een handelsgoed om te verkopen",
            "Een dienst van een leverancier",
            "Een divers goed voor de werking",
        ],
        antwoord=0,
        uitleg="Wat jaren meegaat, is een investering. Hij komt bij de vaste activa en wordt over die jaren afgeschreven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een factuur met vervaldag over dertig dagen?",
        opties=[
            "Je hebt dertig dagen om te betalen",
            "Je moet binnen dertig dagen leveren",
            "De korting geldt nog dertig dagen lang",
            "De factuur vervalt na dertig dagen volledig",
        ],
        antwoord=0,
        uitleg="De vervaldag is de uiterste betaaldatum. Betaal je later, dan kan de leverancier verwijlintresten aanrekenen.",
    ),
]

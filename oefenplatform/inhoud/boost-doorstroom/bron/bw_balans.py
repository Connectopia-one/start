# -*- coding: utf-8 -*-
"""De vragen voor "De balans en de resultatenrekening" (🚀 Boost doorstroom,
economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
bedrijfswetenschappen, "dubbel boekhouden": de structuur van de balans, de
structuur van de resultatenrekening en de berekening van het bedrijfsresultaat,
het financieel resultaat en het resultaat van de onderneming. Het boeken zelf
staat in [[bw_boekhouden]].

Deel 1 gaat over de balans: actief en passief, vaste en vlottende activa, eigen
vermogen en schulden, en het evenwicht tussen beide kanten.
Deel 2 gaat over de resultatenrekening: bedrijfsresultaat, financieel resultaat,
resultaat voor en na belastingen.

In de rekenvragen staan alle bedragen in de vraag zelf.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat staat er aan de linkerkant van een balans?",
        opties=[
            "De bezittingen",
            "De schulden van de onderneming",
            "De kosten van het afgelopen jaar",
            "De opbrengsten van het afgelopen jaar",
        ],
        antwoord=0,
        uitleg="De linkerkant is het actief: alles wat de onderneming bezit, van gebouwen tot het geld op de rekening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er aan de rechterkant van een balans?",
        opties=[
            "De financiering",
            "De bezittingen van de onderneming",
            "De omzet die het bedrijf gehaald heeft",
            "De kosten en de opbrengsten van het jaar",
        ],
        antwoord=0,
        uitleg="De rechterkant is het passief: waar het geld vandaan komt. Dat is eigen vermogen of schuld.",
    ),
    dict(
        type="waarofniet",
        vraag="Het totaal van het actief is altijd gelijk aan het totaal van het passief.",
        antwoord=True,
        uitleg="Elk bezit is met iets betaald, dus staat aan beide kanten hetzelfde totaal. Daarom heet het een balans.",
    ),
    dict(
        type="waarofniet",
        vraag="Een machine staat bij de vlottende activa.",
        antwoord=False,
        uitleg="Een machine blijft jaren in de onderneming en hoort dus bij de vaste activa. Vlottende activa zijn voorraden, vorderingen en geld.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de linkerkant van een balans?",
        antwoord=["actief", "het actief", "activa"],
        uitleg="De linkerkant heet het actief. Daar staat wat de onderneming bezit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn vaste activa? Duid alles aan wat juist is.",
        opties=[
            "Een gebouw",
            "Een machine",
            "Een bestelwagen",
            "De voorraad handelsgoederen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Vaste activa blijven langer dan een jaar in de onderneming. De voorraad is er juist om snel verkocht te worden en hoort bij de vlottende activa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn vlottende activa? Duid alles aan wat juist is.",
        opties=[
            "De voorraad",
            "De handelsvorderingen",
            "Het geld op de rekening",
            "Het gebouw van de zaak",
        ],
        antwoord=[0, 1, 2],
        uitleg="Vlottende activa veranderen snel: goederen worden verkocht, klanten betalen, geld gaat eruit en erin. Een gebouw blijft staan en is een vast actief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het eigen vermogen?",
        opties=[
            "Het geld van de eigenaars",
            "Het geld dat de bank heeft uitgeleend",
            "Het bedrag dat de klanten nog moeten betalen",
            "Het bedrag dat aan de leveranciers verschuldigd is",
        ],
        antwoord=0,
        uitleg="Het eigen vermogen is wat de eigenaars zelf hebben ingebracht, plus de winst die in de onderneming gebleven is. Het moet niet terugbetaald worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar staat een lening op tien jaar op de balans?",
        opties=[
            "Bij de schulden op meer dan één jaar",
            "Bij de vaste activa aan de linkerkant",
            "Bij de vlottende activa aan de linkerkant",
            "Bij de schulden op ten hoogste één jaar",
        ],
        antwoord=0,
        uitleg="Het passief splitst de schulden volgens looptijd. Wat pas na meer dan een jaar moet terugbetaald worden, staat bij de schulden op meer dan één jaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Een handelsvordering is geld dat een klant nog moet betalen.",
        antwoord=True,
        uitleg="Een vordering is een recht op geld. Zodra de klant betaalt, verdwijnt de vordering en stijgt het geld op de rekening.",
    ),
    dict(
        type="waarofniet",
        vraag="Het kapitaal van een vennootschap staat bij het actief.",
        antwoord=False,
        uitleg="Kapitaal is geen bezit maar financiering: het staat bij het eigen vermogen, aan de passiefzijde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het actief van een bedrijf is 150 000 euro. Het eigen vermogen is 60 000 euro. Hoeveel schulden heeft het?",
        opties=[
            "90 000 euro",
            "210 000 euro in totaal",
            "60 000 euro, net als het eigen vermogen",
            "150 000 euro, want dat is het hele actief",
        ],
        antwoord=0,
        uitleg="Actief is gelijk aan eigen vermogen plus schulden, dus 150 000 − 60 000 = 90 000 euro schulden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderdelen vind je aan de passiefzijde? Duid alles aan wat juist is.",
        opties=[
            "Het eigen vermogen",
            "De schulden op lange termijn",
            "De schulden op korte termijn",
            "De voorraden in het magazijn",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het passief toont eigen vermogen en schulden, opgesplitst volgens looptijd. Voorraden zijn een bezit en staan links.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn liquide middelen?",
        opties=[
            "Geld in kas en op de bank",
            "Goederen die klaarliggen om verkocht te worden",
            "Bedragen die klanten binnenkort zullen betalen",
            "Machines die binnen het jaar verkocht zullen worden",
        ],
        antwoord=0,
        uitleg="Liquide middelen zijn het geld dat onmiddellijk beschikbaar is: de kas en de zichtrekening. Ze staan onderaan bij de vlottende activa.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de rechterkant van een balans?",
        antwoord=["passief", "het passief", "passiva"],
        uitleg="De rechterkant heet het passief. Daar staat waarmee de bezittingen gefinancierd zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een balans altijd in evenwicht?",
        opties=[
            "Elk bezit is ergens mee betaald",
            "Omdat de boekhouder de cijfers zo kiest",
            "Omdat de belastingdienst dat zo oplegt",
            "Omdat de winst altijd aan nul gelijk is",
        ],
        antwoord=0,
        uitleg="Achter elk bezit zit een bron: eigen inbreng, winst of schuld. Daarom staat links en rechts altijd hetzelfde totaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn schulden op ten hoogste één jaar? Duid alles aan wat juist is.",
        opties=[
            "Te betalen leveranciers",
            "Te betalen btw",
            "Te betalen lonen",
            "Een lening op twintig jaar",
        ],
        antwoord=[0, 1, 2],
        uitleg="Leveranciers, btw en lonen zijn binnen weken of maanden te betalen. Een lening op twintig jaar hoort bij de schulden op meer dan één jaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze is een immaterieel vast actief?",
        opties=[
            "Een softwarelicentie",
            "Een bestelwagen van de zaak",
            "De voorraad in het magazijn",
            "Het geld op de zichtrekening",
        ],
        antwoord=0,
        uitleg="Immateriële vaste activa kan je niet aanraken en toch zijn ze jaren bruikbaar: software, een octrooi, een merknaam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Over welke periode gaat een balans?",
        opties=[
            "Over één dag",
            "Over het hele afgelopen boekjaar",
            "Over de komende twaalf maanden",
            "Over de vijf jaar sinds de oprichting",
        ],
        antwoord=0,
        uitleg="Een balans is een foto op één bepaalde dag, meestal 31 december. De resultatenrekening gaat wel over een hele periode.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf heeft 200 000 euro activa en 120 000 euro schulden. Hoeveel is het eigen vermogen?",
        opties=[
            "80 000 euro",
            "320 000 euro in totaal",
            "120 000 euro, gelijk aan de schulden",
            "200 000 euro, want dat is het hele actief",
        ],
        antwoord=0,
        uitleg="Eigen vermogen is actief min schulden: 200 000 − 120 000 = 80 000 euro.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat toont een resultatenrekening?",
        opties=[
            "De kosten en de opbrengsten",
            "De bezittingen en de schulden op één dag",
            "Het geld dat op de bankrekening staat vandaag",
            "De namen van alle klanten en alle leveranciers",
        ],
        antwoord=0,
        uitleg="De resultatenrekening zet de opbrengsten en de kosten van een hele periode naast elkaar en toont zo of er winst of verlies is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je het bedrijfsresultaat?",
        opties=[
            "Bedrijfsopbrengsten min bedrijfskosten",
            "De som van alle opbrengsten van het hele jaar",
            "Het resultaat na aftrek van de belastingen erop",
            "De opbrengsten min de intresten op de leningen",
        ],
        antwoord=0,
        uitleg="Het bedrijfsresultaat komt uit de gewone werking: omzet en andere bedrijfsopbrengsten min de bedrijfskosten. Intresten en belastingen komen daarna.",
    ),
    dict(
        type="waarofniet",
        vraag="De omzet is een bedrijfsopbrengst.",
        antwoord=True,
        uitleg="De omzet is wat de onderneming met haar verkopen binnenhaalt en hoort dus bij de bedrijfsopbrengsten.",
    ),
    dict(
        type="waarofniet",
        vraag="De intrest op een lening is een bedrijfskost.",
        antwoord=False,
        uitleg="Intrest is een financiële kost. Hij komt niet bij het bedrijfsresultaat maar bij het financieel resultaat.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschil tussen de financiële opbrengsten en de financiële kosten?",
        antwoord=["financieel resultaat", "het financieel resultaat"],
        uitleg="Dat is het financieel resultaat. Het bevat onder meer de betaalde en ontvangen intresten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn bedrijfskosten? Duid alles aan wat juist is.",
        opties=[
            "De aankoop van handelsgoederen",
            "De lonen van het personeel",
            "De afschrijvingen",
            "De intrest op een lening",
        ],
        antwoord=[0, 1, 2],
        uitleg="Aankopen, lonen en afschrijvingen horen bij de gewone werking. Intrest is een financiële kost.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij het financieel resultaat? Duid alles aan wat juist is.",
        opties=[
            "De intrest die je betaalt",
            "De intrest die je ontvangt",
            "Een dividend dat je ontvangt",
            "Het loon van het personeel",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alles wat met geld lenen en geld beleggen te maken heeft, komt in het financieel resultaat. Lonen zijn een bedrijfskost.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf heeft 500 000 euro bedrijfsopbrengsten en 440 000 euro bedrijfskosten. Wat is het bedrijfsresultaat?",
        opties=[
            "60 000 euro winst",
            "60 000 euro verlies dat jaar",
            "940 000 euro, de som van beide",
            "440 000 euro, gelijk aan de kosten",
        ],
        antwoord=0,
        uitleg="500 000 − 440 000 = 60 000 euro. De opbrengsten zijn hoger dan de kosten, dus is het een winst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het bedrijfsresultaat is 60 000 euro, het financieel resultaat is 10 000 euro negatief. Wat is het resultaat voor belastingen?",
        opties=[
            "50 000 euro",
            "70 000 euro in totaal",
            "10 000 euro, enkel het financiële deel",
            "60 000 euro, het financiële deel telt niet mee",
        ],
        antwoord=0,
        uitleg="Je telt de twee resultaten samen: 60 000 − 10 000 = 50 000 euro voor belastingen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een afschrijving is een kost, ook al vertrekt er dat jaar geen geld.",
        antwoord=True,
        uitleg="Het geld ging eruit bij de aankoop. De afschrijving verdeelt die kost over de jaren waarin het goed meegaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een resultatenrekening geldt voor één bepaalde dag.",
        antwoord=False,
        uitleg="Ze gaat over een hele periode, meestal een boekjaar. De balans is wel een foto op één dag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een balans en een resultatenrekening?",
        opties=[
            "De balans is een foto",
            "De balans gaat over een hele periode",
            "De resultatenrekening telt enkel bezittingen",
            "De resultatenrekening wordt niet neergelegd",
        ],
        antwoord=0,
        uitleg="De balans toont de toestand op één dag, de resultatenrekening de beweging over een periode. Samen vormen ze de jaarrekening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke resultaten vind je in een resultatenrekening? Duid alles aan wat juist is.",
        opties=[
            "Het bedrijfsresultaat",
            "Het financieel resultaat",
            "Het resultaat voor belastingen",
            "Het totaal van het actief",
        ],
        antwoord=[0, 1, 2],
        uitleg="De resultatenrekening werkt in stappen: eerst het bedrijfsresultaat, dan het financieel resultaat, samen het resultaat voor belastingen en na belastingen. Het totaal van het actief staat op de balans.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het resultaat van het boekjaar?",
        opties=[
            "Het resultaat na belastingen",
            "De omzet van het hele afgelopen jaar",
            "Het bedrijfsresultaat van het eerste kwartaal",
            "Het verschil tussen het actief en het passief",
        ],
        antwoord=0,
        uitleg="Onderaan de resultatenrekening staat het resultaat van het boekjaar: het resultaat voor belastingen min de belastingen erop.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschil tussen de bedrijfsopbrengsten en de bedrijfskosten?",
        antwoord=["bedrijfsresultaat", "het bedrijfsresultaat"],
        uitleg="Dat is het bedrijfsresultaat: het resultaat van de gewone werking, zonder de intresten en de belastingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer maakt een onderneming verlies?",
        opties=[
            "Als de kosten hoger zijn",
            "Als de omzet stijgt tegenover vorig jaar",
            "Als het actief groter is dan het passief",
            "Als ze meer belastingen betaalt dan vorig jaar",
        ],
        antwoord=0,
        uitleg="Verlies betekent dat de kosten groter zijn dan de opbrengsten. Een hoge omzet met nog hogere kosten geeft nog altijd verlies.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan je uit een resultatenrekening halen? Duid alles aan wat juist is.",
        opties=[
            "Of er winst gemaakt is",
            "Waar de grootste kosten zitten",
            "Hoe zwaar de intresten wegen",
            "Hoeveel klanten de winkel had",
        ],
        antwoord=[0, 1, 2],
        uitleg="De resultatenrekening toont de kosten en opbrengsten per soort, dus ook waar het geld naartoe gaat en wat de leningen kosten. Het aantal klanten staat er niet in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Het resultaat voor belastingen is 50 000 euro. De belasting bedraagt 25 procent. Wat blijft er over?",
        opties=[
            "37 500 euro",
            "12 500 euro na de belasting",
            "25 000 euro, de helft van het resultaat",
            "50 000 euro, want belasting is geen kost",
        ],
        antwoord=0,
        uitleg="25 procent van 50 000 euro is 12 500 euro belasting. Er blijft 50 000 − 12 500 = 37 500 euro over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een afschrijving met de kost van een machine?",
        opties=[
            "Ze spreidt die over de jaren",
            "Ze boekt die volledig in het aankoopjaar",
            "Ze haalt die helemaal uit de boekhouding weg",
            "Ze schuift die naar het laatste jaar van gebruik",
        ],
        antwoord=0,
        uitleg="Een machine die tien jaar meegaat, kost elk van die tien jaar een stuk. Zo staat de kost in hetzelfde jaar als de opbrengst die ze helpt maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke klasse van het MAR gebruik je voor de kosten?",
        opties=[
            "Klasse 6",
            "Klasse 7, net als de opbrengsten",
            "Klasse 2, net als de vaste activa",
            "Klasse 5, net als de liquide middelen",
        ],
        antwoord=0,
        uitleg="In het minimum algemeen rekeningstelsel zijn de kosten klasse 6 en de opbrengsten klasse 7. Die twee klassen vormen samen de resultatenrekening.",
    ),
]

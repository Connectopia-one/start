# -*- coding: utf-8 -*-
"""De vragen voor "Dubbel boekhouden: redeneerschema, journaal en grootboek"
(🚀 Boost doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
bedrijfswetenschappen, "dubbel boekhouden": het registreren van verrichtingen
volgens het redeneerschema, in het journaal en in het grootboek, met gebruik van
het MAR. De structuur van de balans en de resultatenrekening staat in
[[bw_balans]], het narekenen van facturen in [[bw_facturen]].

Deel 1 gaat over debet en credit, het redeneerschema en het MAR.
Deel 2 gaat over het journaal en het grootboek, met concrete aankopen,
verkopen, creditnota's en betalingen.

Het btw-tarief in de vragen is 21 procent, het gewone tarief.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent debet?",
        opties=[
            "De linkerkant",
            "De rechterkant van een rekening",
            "Het verschil tussen de twee kanten",
            "Het totaal van alle kosten van het jaar",
        ],
        antwoord=0,
        uitleg="Debet is de linkerkant van een rekening, credit de rechterkant. Die twee woorden zeggen niets over goed of slecht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent credit?",
        opties=[
            "De rechterkant",
            "De linkerkant van een rekening",
            "Een schuld aan een leverancier",
            "Het geld dat je van de bank leent",
        ],
        antwoord=0,
        uitleg="Credit is gewoon de rechterkant van een rekening. Of daar een schuld of een opbrengst staat, hangt van de rekening af.",
    ),
    dict(
        type="waarofniet",
        vraag="In elke boeking is het totaal in het debet gelijk aan het totaal in het credit.",
        antwoord=True,
        uitleg="Dat is de kern van het dubbel boekhouden. Klopt het niet, dan zit er een fout in de boeking.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kost boek je altijd in het credit.",
        antwoord=False,
        uitleg="Een kost komt in het debet. Opbrengsten komen in het credit.",
    ),
    dict(
        type="invultekst",
        vraag="Aan welke kant boek je een stijging van een actiefrekening?",
        antwoord=["debet", "in het debet", "links"],
        uitleg="Een actief dat stijgt, boek je in het debet. Daalt het, dan komt het in het credit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen stel je in het redeneerschema? Duid alles aan wat juist is.",
        opties=[
            "Welke rekeningen spelen mee",
            "Welke soort rekening het is",
            "Stijgt ze of daalt ze",
            "Hoeveel winst het bedrijf maakt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het redeneerschema loopt vast: welke rekeningen, van welke soort, stijgen of dalen ze, en dus debet of credit. De winst volgt pas op het einde van het boekjaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een actiefrekening daalt. Waar boek je dat?",
        opties=[
            "In het credit",
            "In het debet van die rekening",
            "In het debet én in het credit samen",
            "Nergens, een daling boek je niet mee",
        ],
        antwoord=0,
        uitleg="Een actief stijgt in het debet en daalt in het credit. Betaalt een klant zijn factuur, dan daalt de vordering dus in het credit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een passiefrekening stijgt. Waar boek je dat?",
        opties=[
            "In het credit",
            "In het debet van die rekening",
            "In het debet én in het credit samen",
            "Nergens, een passief verandert nooit",
        ],
        antwoord=0,
        uitleg="Een passief stijgt in het credit en daalt in het debet. Een nieuwe schuld aan een leverancier komt dus in het credit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar boek je een opbrengst?",
        opties=[
            "In het credit",
            "In het debet van de rekening",
            "Bij de vaste activa op de balans",
            "Bij de schulden op meer dan één jaar",
        ],
        antwoord=0,
        uitleg="Opbrengsten komen in het credit, kosten in het debet. Bij een verkoop staat de rekening Verkopen dus in het credit.",
    ),
    dict(
        type="waarofniet",
        vraag="Het MAR geeft elke rekening een eigen nummer.",
        antwoord=True,
        uitleg="Het minimum algemeen rekeningstelsel nummert alle rekeningen in klassen. Daardoor boekt iedereen dezelfde verrichting op dezelfde rekening.",
    ),
    dict(
        type="waarofniet",
        vraag="Klasse 2 van het MAR is de klasse van de opbrengsten.",
        antwoord=False,
        uitleg="Klasse 2 zijn de vaste activa. De opbrengsten zitten in klasse 7 en de kosten in klasse 6.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke klassen van het MAR komen op de balans terecht? Duid alles aan wat juist is.",
        opties=[
            "Klasse 1",
            "Klasse 2",
            "Klasse 5",
            "Klasse 6",
        ],
        antwoord=[0, 1, 2],
        uitleg="De klassen 1 tot 5 vormen de balans: eigen vermogen en lange schulden, vaste activa, voorraden, vorderingen en korte schulden, geld. Klasse 6 en 7 vormen de resultatenrekening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke klasse van het MAR gebruik je voor de opbrengsten?",
        opties=[
            "Klasse 7",
            "Klasse 6, net als de kosten",
            "Klasse 3, net als de voorraden",
            "Klasse 1, net als het eigen vermogen",
        ],
        antwoord=0,
        uitleg="Klasse 7 zijn de opbrengsten, met vooraan de rekening Verkopen en dienstprestaties. Klasse 6 zijn de kosten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf koopt handelsgoederen op factuur. Welke rekening komt in het debet?",
        opties=[
            "Aankopen handelsgoederen",
            "Verkopen van handelsgoederen",
            "Leveranciers aan wie nog te betalen is",
            "Handelsvorderingen op klanten van de zaak",
        ],
        antwoord=0,
        uitleg="De aankoop is een kost en komt in het debet. De schuld aan de leverancier staat in het credit.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het boek waarin je elke verrichting op datum registreert?",
        antwoord=["journaal", "het journaal", "dagboek"],
        uitleg="In het journaal komt elke verrichting in datumorde, met de rekeningen in debet en credit. Daarna gaat ze naar het grootboek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een klant betaalt zijn factuur op de bankrekening. Wat verandert er? Duid alles aan wat juist is.",
        opties=[
            "De bank stijgt",
            "De handelsvordering daalt",
            "De omzet stijgt opnieuw",
            "Er komt een kost bij",
        ],
        antwoord=[0, 1],
        uitleg="Bij een betaling verschuift er alleen iets binnen het actief: het geld komt binnen, de vordering verdwijnt. De omzet was al geboekt bij de verkoop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rekening gebruik je voor de btw op je aankopen?",
        opties=[
            "Terug te vorderen btw",
            "Te betalen btw aan de staat",
            "Aankopen van handelsgoederen",
            "Diverse diensten en goederen",
        ],
        antwoord=0,
        uitleg="De btw die je aan je leverancier betaalt, mag je terugvorderen van de staat. Ze staat dus als een vordering in het debet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een grootboekrekening?",
        opties=[
            "Eén rekening apart",
            "Een lijst van alle facturen van het jaar",
            "Een overzicht van alle verrichtingen op datum",
            "Het totaal van de kosten en de opbrengsten",
        ],
        antwoord=0,
        uitleg="Het grootboek houdt per rekening bij wat er in debet en in credit geboekt is. Zo zie je in één oogopslag het saldo van bijvoorbeeld de bank.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rekeningen horen bij klasse 6 van het MAR? Duid alles aan wat juist is.",
        opties=[
            "Bezoldigingen",
            "Aankopen handelsgoederen",
            "Huur van het gebouw",
            "Verkopen handelsgoederen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Klasse 6 zijn de kosten: lonen, aankopen, huur, afschrijvingen. Verkopen zijn een opbrengst en zitten in klasse 7.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heet het dubbel boekhouden?",
        opties=[
            "Elke verrichting komt twee keer",
            "Omdat je alles twee keer moet narekenen",
            "Omdat er twee boekhouders nodig zijn per bedrijf",
            "Omdat elk bedrag met twee vermenigvuldigd wordt",
        ],
        antwoord=0,
        uitleg="Elke verrichting raakt minstens twee rekeningen: één in het debet en één in het credit, voor hetzelfde bedrag. Daarom blijft de balans in evenwicht.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat staat er in het journaal?",
        opties=[
            "Elke verrichting op datum",
            "Alle bedragen per rekening gegroepeerd",
            "Alleen de facturen van de leveranciers",
            "Het eindtotaal van de balans per boekjaar",
        ],
        antwoord=0,
        uitleg="Het journaal is chronologisch: verrichting na verrichting, in de orde waarin ze gebeurd zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er in het grootboek?",
        opties=[
            "Alles per rekening",
            "Alle verrichtingen in datumorde",
            "Alleen de betalingen via de bank",
            "Het overzicht van de kosten per maand",
        ],
        antwoord=0,
        uitleg="Het grootboek sorteert dezelfde boekingen per rekening, zodat je het saldo van elke rekening ziet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een boeking in het journaal komt daarna ook in het grootboek.",
        antwoord=True,
        uitleg="Het zijn twee manieren om dezelfde boekingen te bekijken: het journaal op datum, het grootboek per rekening.",
    ),
    dict(
        type="waarofniet",
        vraag="In het grootboek staan de verrichtingen enkel in datumorde bij elkaar.",
        antwoord=False,
        uitleg="Dat is net het journaal. Het grootboek groepeert per rekening.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschil tussen de debetkant en de creditkant van een grootboekrekening?",
        antwoord=["saldo", "het saldo"],
        uitleg="Dat verschil is het saldo. Staat het grootste bedrag in het debet, dan spreekt men van een debetsaldo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een aankoopfactuur van handelsgoederen vermeldt 1 000 euro goederen en 21 procent btw. Welk bedrag komt bij de leverancier in het credit?",
        opties=[
            "1 210 euro",
            "1 000 euro zonder de btw erbij",
            "210 euro, enkel het btw-bedrag zelf",
            "790 euro, de goederen min de btw erop",
        ],
        antwoord=0,
        uitleg="De leverancier krijgt het hele factuurbedrag: 1 000 euro goederen plus 210 euro btw, samen 1 210 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rekeningen gebruik je bij een aankoopfactuur van handelsgoederen? Duid alles aan wat juist is.",
        opties=[
            "Aankopen handelsgoederen",
            "Terug te vorderen btw",
            "Leveranciers",
            "Verkopen handelsgoederen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Aankopen en de terug te vorderen btw komen in het debet, de schuld aan de leverancier in het credit. Verkopen heeft hier niets te zoeken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rekeningen gebruik je bij een verkoopfactuur van handelsgoederen? Duid alles aan wat juist is.",
        opties=[
            "Verkopen handelsgoederen",
            "Te betalen btw",
            "Handelsvorderingen",
            "Aankopen handelsgoederen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De vordering op de klant komt in het debet, de verkoop en de btw die je aan de staat moet doorstorten in het credit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je betaalt een aankoopfactuur via de bank. Wat gebeurt er met de rekening Leveranciers?",
        opties=[
            "Ze daalt",
            "Ze stijgt met hetzelfde bedrag",
            "Ze verandert niet door een betaling",
            "Ze verdwijnt volledig uit het grootboek",
        ],
        antwoord=0,
        uitleg="De schuld wordt kleiner, dus boek je de leverancier in het debet. De bank daalt in het credit.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de betaling van een aankoopfactuur verandert er niets aan de kosten.",
        antwoord=True,
        uitleg="De kost stond al in de boeken bij de factuur. De betaling verschuift enkel geld en schuld.",
    ),
    dict(
        type="waarofniet",
        vraag="Een creditnota van een leverancier verhoogt je schuld aan die leverancier.",
        antwoord=False,
        uitleg="Een inkomende creditnota verlaagt je schuld. Ze corrigeert een eerdere factuur, bijvoorbeeld bij een terugzending.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een inkomende creditnota?",
        opties=[
            "Een correctie van een aankoop",
            "Een tweede factuur voor dezelfde levering",
            "Een herinnering dat je nog moet betalen",
            "Een bewijs dat je de factuur betaald hebt",
        ],
        antwoord=0,
        uitleg="Een creditnota van je leverancier zet een deel of het geheel van een aankoopfactuur terug, bijvoorbeeld na een terugzending of een korting achteraf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verkoopt voor 2 000 euro goederen met 21 procent btw. Wat is het factuurtotaal?",
        opties=[
            "2 420 euro",
            "2 000 euro, de btw komt later",
            "420 euro, enkel het btw-bedrag zelf",
            "1 580 euro, de goederen min de btw erop",
        ],
        antwoord=0,
        uitleg="21 procent van 2 000 euro is 420 euro. Het totaal is 2 000 + 420 = 2 420 euro, en dat is wat de klant moet betalen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een uitgaande creditnota? Duid alles aan wat juist is.",
        opties=[
            "De verkoop daalt",
            "De vordering daalt",
            "De te betalen btw daalt",
            "De bankrekening stijgt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een creditnota aan een klant draait een stuk van de verkoop terug, met de btw erbij. Er komt geen geld binnen, dus de bank blijft ongemoeid.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de rekening waarop staat wat klanten nog moeten betalen?",
        antwoord=["handelsvorderingen", "handelsvordering", "klanten"],
        uitleg="Dat zijn de handelsvorderingen, in het dagelijks taalgebruik de klanten. Het is een vlottend actief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een klant betaalt op de bankrekening. Welke rekening komt in het debet?",
        opties=[
            "De bank",
            "De handelsvordering op die klant",
            "De verkopen van handelsgoederen",
            "De te betalen btw aan de overheid",
        ],
        antwoord=0,
        uitleg="De bank is een actief dat stijgt, dus debet. De vordering daalt en komt in het credit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom boek je de btw op een aparte rekening?",
        opties=[
            "Het is geld van de staat",
            "Omdat de btw een kost van het bedrijf is",
            "Omdat de klant de btw niet moet betalen",
            "Omdat de leverancier dat zo vraagt op zijn factuur",
        ],
        antwoord=0,
        uitleg="De btw die je aanrekent, stort je door aan de staat; de btw die je betaalt, vorder je terug. Ze hoort dus niet bij je kosten of je opbrengsten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soorten aankopen onderscheidt een boekhouder? Duid alles aan wat juist is.",
        opties=[
            "Handelsgoederen",
            "Diensten en diverse goederen",
            "Investeringsgoederen",
            "Aankopen van personeel",
        ],
        antwoord=[0, 1, 2],
        uitleg="Handelsgoederen gaan door naar de klant, diensten en diverse goederen zijn werkingskosten, investeringsgoederen gaan jaren mee. Personeel koop je niet aan; dat is een loonkost.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar boek je de aankoop van een bestelwagen voor de zaak?",
        opties=[
            "Bij de investeringen",
            "Bij de aankopen van handelsgoederen",
            "Bij de diensten en de diverse goederen",
            "Bij de schulden op ten hoogste één jaar",
        ],
        antwoord=0,
        uitleg="Een bestelwagen gaat jaren mee en komt dus bij de materiële vaste activa, in klasse 2. De kost volgt via de afschrijvingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je boekt een aankoopfactuur. Welke kant krijgt de rekening Leveranciers?",
        opties=[
            "Het credit",
            "Het debet van die rekening",
            "Zowel het debet als het credit",
            "Geen van beide, pas bij de betaling",
        ],
        antwoord=0,
        uitleg="De schuld aan de leverancier stijgt, en een passief dat stijgt komt in het credit. Bij de betaling daalt ze en komt ze in het debet.",
    ),
]

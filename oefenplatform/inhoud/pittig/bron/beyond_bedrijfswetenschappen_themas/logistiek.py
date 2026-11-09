"""Logistiek en supply chain management — pittig (🌍 Beyond, bedrijfswetenschappen en recht)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import vv_zone, vk_zone

PRENTEN = [
    dict(bestand="voorraadverloop.svg", zelf=True,
         wat="Zaagtandgrafiek van een voorraad fietsbanden over 90 dagen, met maximum- en minimumvoorraad.",
         vragen="klikvragen en rekenvragen over het voorraadverloop"),
    dict(bestand="voorraadkosten.svg", zelf=True,
         wat="Grafiek met drie krommen (A, B, C) van de voorraadkosten volgens de bestelgrootte.",
         vragen="klikvraag op de beste bestelgrootte en een tabel over de krommen"),
]

VRAGEN = [
    klik(
        "Klik op de lijn van de minimumvoorraad: de buffer die er altijd moet zijn.",
        "voorraadverloop.svg",
        [vv_zone("min")],
        "De minimumvoorraad is 100 stuks: de buffer die er altijd moet zijn.",
    ),
    klik(
        "Klik op het moment van de eerste levering van fietsbanden.",
        "voorraadverloop.svg",
        [vv_zone("levering")],
        "Op dag 30 springt de voorraad in één keer van 100 naar 600 stuks: dan komt de levering binnen.",
    ),
    met_prent("voorraadverloop.svg", mk(
        "Hoeveel fietsbanden worden er telkens geleverd?",
        ["500", "600", "100", "700"],
        0,
        "De voorraad gaat van het minimum (100) naar het maximum (600): 600 − 100 = 500 stuks.",
    )),
    met_prent("voorraadverloop.svg", mk(
        "Hoeveel fietsbanden verkoopt Velo nv gemiddeld per dag?",
        ["Ongeveer 16,7", "20", "Ongeveer 13,3", "500"],
        0,
        "In 30 dagen daalt de voorraad met 500 stuks: 500 / 30 ≈ 16,7 per dag.",
    )),
    klik(
        "Klik op de lijn van de maximumvoorraad.",
        "voorraadverloop.svg",
        [vv_zone("max")],
        "De maximumvoorraad is 600 stuks: meer houdt Velo nv niet aan.",
    ),
    klik(
        "Klik op het punt dat de beste bestelgrootte aangeeft: daar zijn de totale voorraadkosten het laagst.",
        "voorraadkosten.svg",
        [vk_zone("optimum")],
        "Het laagste punt van de totale kosten (kromme C) ligt boven het snijpunt van de bewaarkosten en de bestelkosten.",
    ),
    met_prent("voorraadkosten.svg", tabel(
        "Welke kosten stelt elke kromme voor?",
        [
            ("Kromme A: stijgt naarmate je meer per keer bestelt", "Bewaarkosten"),
            ("Kromme B: daalt naarmate je meer per keer bestelt", "Bestelkosten"),
            ("Kromme C: de som van A en B", "Totale voorraadkosten"),
        ],
        "Grote bestellingen: veel voorraad, dus hoge bewaarkosten, maar weinig bestellingen, dus lage bestelkosten.",
        kolommen=["Bewaarkosten", "Bestelkosten", "Totale voorraadkosten"],
    )),
    mk(
        "Technische voorraad 800 stuks, besteld bij de leverancier 300 stuks, gereserveerd voor klanten 250 stuks. Hoeveel is de beschikbare voorraad?",
        ["850 stuks", "750 stuks", "1 350 stuks", "250 stuks"],
        0,
        "Beschikbaar = technisch + besteld − gereserveerd = 800 + 300 − 250 = 850.",
    ),
    tabel(
        "Waar of niet waar over voorraden?",
        [
            ("De gereserveerde voorraad ligt in het magazijn, maar is al beloofd aan een klant.", J),
            ("De technische voorraad is wat fysiek in het magazijn ligt.", J),
            ("Hoe groter elke bestelling, hoe lager de bewaarkosten.", F),
            ("De interest op het geld dat in de voorraad vastzit, is een voorraadkost.", J),
            ("Reclamekosten zijn voorraadkosten.", F),
            ("Met Just In Time hou je een grote voorraad aan.", F),
        ],
        "Voorraad kost geld: huur, verzekering, interest, bederf en veroudering. Just In Time probeert die voorraad zo klein mogelijk te houden.",
    ),
    tabel(
        "Welke grondvorm van productie is het?",
        [
            ("Een raffinaderij maakt uit ruwe olie benzine, diesel en asfalt", "Divergent"),
            ("Een fabriek bouwt laptops uit honderden onderdelen", "Convergent"),
            ("Een bakkerij bakt op drie aparte lijnen brood, taart en koekjes", "Parallel"),
        ],
        "Divergent: uit één naar veel. Convergent: uit veel naar één. Parallel: aparte lijnen naast elkaar.",
        kolommen=["Divergent", "Convergent", "Parallel"],
    ),
    keuze(
        "Een sportmerk laat klanten online de kleuren en de naam op hun schoenen kiezen en maakt ze daarna in grote aantallen op een automatische lijn. Dat heet [[*mass customisation|serieproductie|divergente productie]].",
        "Op maat van de klant, maar aan de kostprijs van massaproductie.",
    ),
    tabel(
        "Welk soort magazijn is het?",
        [
            ("Pakjes worden binnen enkele uren van de ene vrachtwagen in de andere geladen", "Crossdock"),
            ("Een opslagplaats die ruimte verhuurt aan verschillende bedrijven", "Public warehouse"),
            ("Kleine zendingen van verschillende bedrijven worden samengevoegd tot één volle vrachtwagen", "Groupagecentrum"),
            ("Een winkelketen bevoorraadt van hieruit al haar winkels", "Distributiecentrum"),
        ],
        "Elk magazijn heeft een andere rol in de logistieke keten.",
        kolommen=["Crossdock", "Public warehouse", "Groupagecentrum", "Distributiecentrum"],
    ),
    volgorde(
        "Zet de fasen van het inkoopproces in de juiste volgorde.",
        [
            "Specifiëren wat je nodig hebt",
            "Leveranciers selecteren",
            "Onderhandelen",
            "Een aankooporder plaatsen",
            "De levering controleren",
            "De factuur controleren en betalen",
        ],
        "Eerst weten wat je wil, dan de leverancier kiezen, afspraken maken, bestellen en tot slot nagaan of alles klopt.",
    ),
    tabel(
        "Welk soort inkoop is het?",
        [
            ("Beslissen om voor vijf jaar met één vaste leverancier van staal samen te werken", "Strategisch"),
            ("Een gewone bestelling van kantoorpapier plaatsen", "Operationeel"),
            ("Beslissen om voortaan enkel nog gerecycleerd karton te kopen bij leveranciers uit Europa", "Strategisch"),
            ("De wekelijkse levering van schroeven en bouten bestellen", "Operationeel"),
        ],
        "Strategisch: keuzes op lange termijn. Operationeel: de dagelijkse bestellingen.",
        kolommen=["Strategisch", "Operationeel"],
    ),
    tabel(
        "Waar ligt het klantorderontkoppelingspunt (KOOP)?",
        [
            ("Een supermarkt verkoopt blikken soep uit de rekken", "Bij de klant"),
            ("Een schrijnwerker maakt een kast op maat met hout uit zijn voorraad", "Bij de grondstoffen"),
            ("Een kleermaker naait een maatpak met stof die al in zijn atelier ligt", "Bij de grondstoffen"),
            ("Een boekhandel verkoopt boeken die al in de rekken staan", "Bij de klant"),
        ],
        "Vóór het KOOP wordt op voorraad gewerkt, erna op bestelling.",
        kolommen=["Bij de klant", "Bij de grondstoffen"],
    ),
    sorteer(
        "Push- of pullmodel?",
        ["Push", "Pull"],
        [
            ["Een fabriek maakt elke maand 10 000 stuks op basis van een verkoopvoorspelling", "Push"],
            ["Een fietsenmaker bouwt een fiets pas als de klant ze besteld heeft", "Pull"],
            ["Een kledingmerk vult de winkels voor het seizoen met de nieuwe collectie", "Push"],
            ["Een drukkerij drukt een boek pas als iemand het online koopt", "Pull"],
        ],
        "Push: produceren op voorspelling en de goederen naar de markt duwen. Pull: de vraag van de klant trekt de productie op gang.",
    ),
    mk(
        "Waarom heeft een bedrijf met een pullmodel meestal minder voorraad dan een bedrijf met een pushmodel?",
        [
            "Het produceert pas als er een bestelling is",
            "Het mag wettelijk geen voorraad hebben",
            "Het verkoopt minder producten",
            "Het betaalt geen bewaarkosten",
        ],
        0,
        "Wat niet gevraagd is, wordt niet gemaakt, dus er blijft weinig op de plank liggen.",
    ),
    tabel(
        "Waar of niet waar over Just In Time?",
        [
            ("De voorraadkosten dalen.", J),
            ("Een staking bij een leverancier kan de productie snel stilleggen.", J),
            ("Je hebt geen afspraken met leveranciers nodig.", F),
        ],
        "Weinig voorraad betekent weinig kosten, maar ook weinig buffer als er iets misloopt.",
    ),
    mk(
        "Een fabrikant van fietsen laat het vervoer van zijn fietsen over aan een transportbedrijf. Hoe heet dit?",
        ["Outsourcing", "Just In Time", "Crossdocking", "Mass customisation"],
        0,
        "Outsourcing: een activiteit laten doen door een gespecialiseerde externe partner.",
    ),
    tabel(
        "Is het een voordeel of een nadeel van outsourcing?",
        [
            ("Het bedrijf kan zich op zijn kerntaak toeleggen", "Voordeel"),
            ("Het bedrijf wordt afhankelijk van een externe partner", "Nadeel"),
            ("De partner heeft meer kennis en schaalvoordelen", "Voordeel"),
            ("Het bedrijf heeft minder controle over de kwaliteit", "Nadeel"),
        ],
        "Uitbesteden kan kosten besparen, maar je geeft ook een stuk controle uit handen.",
        kolommen=["Voordeel", "Nadeel"],
    ),
    mk(
        "Land X heeft een LPI-score van 4,1, land Y een score van 2,6. Waar zal een internationaal transportbedrijf het liefst een distributiecentrum bouwen, als de rest gelijk is?",
        ["In land X", "In land Y", "Het maakt niets uit", "In geen van beide"],
        0,
        "Een hogere score betekent betere infrastructuur, vlottere douane en betrouwbaardere leveringen.",
    ),
    inv(
        "De minimumvoorraad heeft nog een andere naam, omdat ze een buffer vormt als er iets misloopt. Welke?",
        "veiligheidsvoorraad",
        "Ze vangt een late levering of een plotse piek in de verkoop op.",
    ),
    mk(
        "Wat geeft de Logistics Performance Index een land een hoge score?",
        [
            "Goede wegen en havens, een vlotte douane en betrouwbare leveringen",
            "Veel inwoners en een groot grondgebied",
            "Een hoge winst van de transportbedrijven in dat land",
            "Een lage prijs van diesel aan de pomp",
        ],
        0,
        "De LPI meet hoe goed de logistiek van een land werkt, niet hoe groot of rijk het is.",
    ),
    mk(
        "Wat is het verschil tussen logistiek management en supply chain management?",
        [
            "Logistiek gaat over de goederenstroom in één bedrijf, supply chain over de hele keten van leverancier tot klant",
            "Supply chain gaat enkel over de verkoop aan de klant",
            "Logistiek gaat enkel over vrachtwagens, supply chain over schepen",
            "Er is geen verschil: het zijn twee namen voor hetzelfde",
        ],
        0,
        "Supply chain management stemt alle schakels samen af, ook die buiten het eigen bedrijf.",
    ),
    sleep(
        "Een [[logistieke flow]] is de stroom van goederen, informatie en geld door de keten. Wie die hele keten van leverancier tot klant op elkaar afstemt, doet aan [[supply chain management]].",
        ["outsourcing", "crossdocking"],
        "Niet enkel goederen bewegen: ook bestellingen en betalingen.",
    ),
    mk(
        "Wat is een bevoorradingsmagazijn?",
        [
            "Een magazijn met grondstoffen en onderdelen voor de eigen productie",
            "Een magazijn dat ruimte verhuurt aan verschillende bedrijven",
            "Een magazijn waar pakjes meteen worden overgeladen",
            "Een magazijn van waaruit alle winkels van een keten bevoorraad worden",
        ],
        0,
        "Het heet ook productiemagazijn: het levert aan de eigen productielijn.",
    ),
    open_(
        "Een webwinkel in speelgoed verkoopt in december drie keer zoveel als in de rest van het jaar. Leg uit waarom een vaste, kleine minimumvoorraad hier een risico is, en wat de winkel kan doen.",
        "In december loopt de voorraad veel sneller leeg, zodat de buffer te klein is om te overbruggen tot de volgende levering. De winkel kan de minimumvoorraad tijdelijk verhogen, vroeger of vaker bestellen of afspraken maken met leveranciers over snellere leveringen.",
        "De minimumvoorraad moet passen bij het verbruik en de levertijd.",
    ),
    casus(
        "Velo nv verkoopt fietsbanden. Zie de grafiek van het voorraadverloop.",
        [
            met_prent("voorraadverloop.svg", mk(
                "Velo verkoopt plots dubbel zo snel als in de grafiek. Na hoeveel dagen zakt de voorraad dan van het maximum tot het minimum?",
                ["15 dagen", "30 dagen", "60 dagen", "10 dagen"],
                0,
                "In de grafiek duurt dat 30 dagen. Dubbel zo snel verkopen halveert die tijd: 15 dagen.",
            )),
            met_prent("voorraadverloop.svg", mk(
                "Velo verhoogt de minimumvoorraad naar 150 stuks. Het maximum blijft 600. Hoeveel stuks moet een levering dan nog bevatten?",
                ["450", "500", "600", "750"],
                0,
                "De levering vult aan van het minimum tot het maximum: 600 − 150 = 450.",
            )),
            tabel(
                "De leverancier levert een keer 5 dagen te laat. Wat klopt?",
                [
                    ("Velo gebruikt dan een deel van de minimumvoorraad.", J),
                    ("Daarvoor dient de minimumvoorraad net.", J),
                    ("De voorraad zakt meteen naar nul.", F),
                ],
                "In 5 dagen gaan er ongeveer 83 banden weg: de buffer van 100 vangt dat op.",
            ),
        ],
    ),
]

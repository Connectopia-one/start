# -*- coding: utf-8 -*-
"""De vragen voor "Ik beheer mijn financiën" (✨ Spark, samenleving en economie).

Uit de vakfiche 1ste graad A-stroom, onderdeel "ik beheer mijn financiën"
(15 % van het examen).

Deel 1 gaat over je keuzegedrag (het verschil tussen een reële en een gecreëerde
behoefte, de factoren die je koopgedrag beïnvloeden), over een budgetplan en
sparen, en over lenen met al zijn onderdelen. Deel 2 gaat over de zes
verkoopkanalen en de zeven betaalmiddelen van de fiche, met telkens hun
veiligheid, risico's en kosten, en over fraude met betaalmiddelen.

De rekenvragen blijven met opzet klein en zonder komma's: het examen geeft je
bronmateriaal met cijfers, maar hier gaat het om het inzicht en niet om het
rekenwerk.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een reële behoefte?",
        opties=[
            "Iets dat je echt nodig hebt om te leven of te functioneren",
            "Iets dat je graag wil hebben omdat je het ergens gezien hebt",
            "Iets dat je koopt omdat het net in de aanbieding is",
            "Iets dat al je vrienden hebben en jij nog niet",
        ],
        antwoord=0,
        uitleg="Eten, kleren, een dak boven je hoofd en schoolgerief zijn reële behoeften. Ze zijn er ook zonder dat iemand je ervan moet overtuigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een gecreëerde behoefte?",
        opties=[
            "Een behoefte die pas ontstaat door reclame of door je omgeving",
            "Een behoefte waarvoor je eerst nog moet sparen",
            "Een behoefte die je alleen in een bepaald seizoen van het jaar hebt",
            "Een behoefte die maar één keer per jaar terugkomt",
        ],
        antwoord=0,
        uitleg="Een gecreëerde behoefte is opgewekt: je gsm werkt nog prima, maar het nieuwe model doet je toch iets willen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn reële behoeften?",
        opties=[
            "Eten en drinken",
            "Een warme jas in de winter",
            "Een plek om te wonen",
            "De nieuwste kleur van een sneaker die je al hebt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie heb je nodig. De vierde is een gecreëerde behoefte: je schoenen doen het nog.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gecreëerde behoefte is altijd iets slechts waar je nooit aan mag toegeven.",
        antwoord=False,
        uitleg="Je mag gerust eens iets kopen dat je niet strikt nodig hebt. Het punt is dat je weet waaróm je het koopt en dat het in je budget past.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze kunnen je koopgedrag beïnvloeden?",
        opties=[
            "Reclame en influencers",
            "Wat je vrienden hebben of vinden",
            "Een korting of een aanbod dat bijna stopt",
            "Het weer van vorige maand",
        ],
        antwoord=[0, 1, 2],
        uitleg="Reclame, je omgeving, de prijs, een korting, een merk of een aftellende klok duwen je richting een aankoop. Ze zijn er om je te doen kopen.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een webshop staat: nog 2 op voorraad, aanbod verloopt in 5 minuten. Wat gebeurt hier?",
        opties=[
            "Je wordt onder tijdsdruk gezet om snel te beslissen",
            "De webshop moet dat wettelijk vermelden bij elk product",
            "Het is een teken dat de webshop betrouwbaar is",
            "Het betekent dat je de laagste prijs van het jaar krijgt",
        ],
        antwoord=0,
        uitleg="Tijdsdruk en schaarste zijn verkooptrucs: ze halen het nadenken eruit. Neem juist dan even afstand.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je vooraf nadenkt of je iets echt nodig hebt, koop je doorgaans doordachter.",
        antwoord=True,
        uitleg="Klopt. Wie zich eerst afvraagt of het een reële of een gecreëerde behoefte is, laat zich minder meesleuren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een budgetplan?",
        opties=[
            "Een overzicht van je inkomsten en je uitgaven",
            "Een lijst van alles wat je nog graag wil kopen",
            "Een afspraak met de bank over een lening",
            "Een berekening van hoeveel rente je moet betalen",
        ],
        antwoord=0,
        uitleg="In een budgetplan zet je naast elkaar wat er binnenkomt en wat eruit gaat. Wat overblijft, kan je sparen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt 40 euro zakgeld per maand en je geeft er 25 euro van uit. Hoeveel kan je sparen?",
        opties=[
            "15 euro",
            "25 euro",
            "40 euro",
            "65 euro",
        ],
        antwoord=0,
        uitleg="40 min 25 is 15. Wat je van je inkomsten niet uitgeeft, kan je sparen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil een fiets van 300 euro en je spaart 25 euro per maand. Hoelang duurt dat?",
        opties=[
            "Twaalf maanden",
            "Tien maanden",
            "Vijftien maanden",
            "Acht maanden",
        ],
        antwoord=0,
        uitleg="300 gedeeld door 25 is 12. Een spaardoel wordt zo ineens heel concreet.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie elke maand een klein bedrag opzij zet, heeft een buffer voor onvoorziene uitgaven.",
        antwoord=True,
        uitleg="Klopt. Een spaarpotje voorkomt dat je moet lenen als de wasmachine stukgaat of de fiets hersteld moet worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een lening?",
        opties=[
            "Geld dat je van iemand krijgt en later moet terugbetalen",
            "Geld dat je van de overheid krijgt als je het nodig hebt",
            "Geld dat je op je spaarrekening opzij hebt gezet",
            "Geld dat je van een familielid geschonken krijgt",
        ],
        antwoord=0,
        uitleg="Bij een lening krijg je nu geld en betaal je het later terug, meestal in maandelijkse stukken en met rente erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is rente?",
        opties=[
            "De prijs die je betaalt om geld te mogen lenen",
            "Het bedrag dat je in totaal geleend hebt",
            "De tijd waarover je de lening afbetaalt",
            "Het deel van de lening dat je al afbetaald hebt",
        ],
        antwoord=0,
        uitleg="Rente is wat lenen kost. Hoe hoger de rentevoet en hoe langer de looptijd, hoe meer je in totaal betaalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn onderdelen van een lening?",
        opties=[
            "De looptijd",
            "De rentevoet",
            "Het maandelijks afbetalingsbedrag",
            "De naam van je bankkantoor",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt zeven onderdelen: het geleende bedrag, de looptijd, de rentevoet, de totale rente, de totale terugbetaling, het maandelijks afbetalingsbedrag en de nog openstaande schuld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leende 1000 euro en betaalt in totaal 1150 euro terug. Wat is de totale rente?",
        opties=[
            "150 euro",
            "1150 euro",
            "1000 euro",
            "50 euro",
        ],
        antwoord=0,
        uitleg="1150 min 1000 is 150. De totale rente is wat je bovenop het geleende bedrag betaalt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de nog openstaande schuld?",
        opties=[
            "Het deel van de lening dat je nog moet terugbetalen",
            "Het volledige bedrag dat je in het begin geleend hebt",
            "De rente die je al betaald hebt aan de bank",
            "Het bedrag dat je elke maand moet afbetalen",
        ],
        antwoord=0,
        uitleg="De openstaande schuld daalt met elke afbetaling. Wanneer ze op nul staat, is de lening afgelopen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een lening met een langere looptijd kost in totaal meestal meer, ook al is het maandbedrag lager.",
        antwoord=True,
        uitleg="Klopt. Je betaalt langer rente, dus de totale terugbetaling loopt op. Een lager maandbedrag is niet automatisch goedkoper.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn de risico's van te veel lenen?",
        opties=[
            "Je kan je afbetalingen niet meer volgen",
            "Je moet steeds meer rente betalen",
            "Je kan in een schuldenspiraal terechtkomen",
            "Je spaargeld brengt minder rente op",
        ],
        antwoord=[0, 1, 2],
        uitleg="Wie te veel leent, betaalt meer rente, raakt achterop en leent soms bij om af te betalen. Dat is een schuldenspiraal.",
    ),
    dict(
        type="waarofniet",
        vraag="Lenen om iets te kopen dat je eigenlijk niet nodig hebt, is een verstandige keuze.",
        antwoord=False,
        uitleg="Dan betaal je rente voor een gecreëerde behoefte. Sparen kost je niets extra en het wachten helpt je bovendien beslissen of je het echt wil.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we de prijs die je betaalt om geld te mogen lenen?",
        antwoord=["rente", "de rente"],
        uitleg="De rente is wat lenen kost. Ze wordt berekend met een rentevoet, een percentage per jaar.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn verkoopkanalen?",
        opties=[
            "Een fysieke winkel",
            "Een webshop",
            "Sociale media",
            "Een spaarrekening",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt zes verkoopkanalen: evenementen, de fysieke winkel, de webshop, de markt, sociale media en teleshopping.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een voordeel van kopen in een fysieke winkel?",
        opties=[
            "Je ziet en voelt het product voor je betaalt",
            "Je hebt er veertien dagen bedenktijd na je aankoop",
            "Je betaalt er nooit btw op wat je meeneemt",
            "Je kan er altijd achteraf over de prijs onderhandelen",
        ],
        antwoord=0,
        uitleg="In de winkel weet je meteen wat je koopt. De veertien dagen bedenktijd gelden juist bij aankopen op afstand, zoals online.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een online aankoop heb je in principe veertien dagen bedenktijd om ze terug te sturen.",
        antwoord=True,
        uitleg="Klopt, dat is het herroepingsrecht bij verkoop op afstand. Voor sommige zaken, zoals een pasgemaakt product, geldt het niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar moet je op letten bij een webshop die je niet kent?",
        opties=[
            "Of er een adres en een telefoonnummer op de site staan",
            "Of de prijs niet verdacht veel lager is dan elders",
            "Of het webadres met https begint en juist gespeld is",
            "Of de site mooie foto's van het product gebruikt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Contactgegevens, een realistische prijs en een correct webadres zeggen iets. Mooie foto's zeggen niets: die kan iedereen kopiëren.",
    ),
    dict(
        type="waarofniet",
        vraag="Iemand die op sociale media iets verkoopt, geeft je dezelfde garantie als een winkel.",
        antwoord=False,
        uitleg="Bij een particulier heb je geen wettelijke garantie en vaak geen enkel spoor. Daarom is dat kanaal risicovoller.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn betaalmiddelen volgens de fiche?",
        opties=[
            "Cash geld",
            "De debetkaart",
            "De kredietkaart",
            "Het kasticket van de winkel",
        ],
        antwoord=[0, 1, 2],
        uitleg="De zeven betaalmiddelen zijn cash geld, contactloos betalen, de debetkaart, de kredietkaart, de overschrijving, een mobiele betaalapp en de prepaidkaart. Een kasticket is een bewijs, geen betaalmiddel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een debetkaart en een kredietkaart?",
        opties=[
            "Bij een debetkaart gaat het geld meteen van je rekening, bij een kredietkaart later",
            "Bij een debetkaart betaal je altijd rente, bij een kredietkaart betaal je nooit rente",
            "Een debetkaart werkt alleen in het buitenland en online",
            "Een kredietkaart kan je alleen bij de bank zelf gebruiken",
        ],
        antwoord=0,
        uitleg="Een debetkaart neemt het geld van je eigen rekening. Bij een kredietkaart schuift de afrekening op, dus kan je makkelijker te veel uitgeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een risico van cash geld?",
        opties=[
            "Kwijt of gestolen is definitief weg",
            "Je kan het niet gebruiken in een winkel",
            "Je betaalt er kosten op bij elke aankoop",
            "Je moet er altijd je code bij invoeren",
        ],
        antwoord=0,
        uitleg="Cash heeft geen spoor en geen blokkering. Tegelijk is het wel veilig tegen online fraude, want er is geen kaartnummer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een prepaidkaart?",
        opties=[
            "Een kaart waarop je eerst geld zet en dan pas kan betalen",
            "Een kaart die je pas na de aankoop moet opladen",
            "Een kaart waarmee je onbeperkt kan lenen bij de bank",
            "Een kaart die de winkel je gratis geeft als klant",
        ],
        antwoord=0,
        uitleg="Bij een prepaidkaart kan je nooit meer verliezen dan wat erop staat. Daarom is ze handig om online voorzichtig te betalen.",
    ),
    dict(
        type="waarofniet",
        vraag="Contactloos betalen van een klein bedrag kan doorgaans zonder je pincode.",
        antwoord=True,
        uitleg="Klopt, en dat is precies het risico: wie je kaart vindt, kan tot een bepaald bedrag betalen. Blokkeer een verloren kaart dus meteen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een overschrijving naar een onbekende verkoper riskant?",
        opties=[
            "Het geld is na de overschrijving heel moeilijk terug te halen",
            "Je bank rekent er hoge kosten voor aan bij elke poging",
            "De verkoper ziet je pincode zodra je de betaling doet",
            "Een overschrijving komt pas na een maand bij de verkoper",
        ],
        antwoord=0,
        uitleg="Bij een overschrijving stuur je het geld zelf weg. Is de verkoper een bedrieger, dan heb je geen product en geen geld.",
    ),
    dict(
        type="waarofniet",
        vraag="Een mobiele betaalapp is beveiligd met een code, je vingerafdruk of je gezicht.",
        antwoord=True,
        uitleg="Klopt, dat maakt ze vrij veilig. Het risico zit bij een toestel zonder schermvergrendeling of bij een app op een geleende gsm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een bericht dat je bankkaart geblokkeerd is en dat je via een link je gegevens moet bevestigen. Wat doe je?",
        opties=[
            "Niets op de link klikken en zelf je bank contacteren",
            "Je kaartnummer en code invullen zodat het snel opgelost is",
            "Het bericht doorsturen naar je vrienden als waarschuwing",
            "Antwoorden met de vraag wie het bericht gestuurd heeft",
        ],
        antwoord=0,
        uitleg="Dit is phishing. Een bank vraagt nooit je codes via een link. Ga zelf naar de app of het nummer dat je al kende.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn signalen van bedrog bij een betaling?",
        opties=[
            "Je moet betalen buiten het systeem van de website om",
            "Er wordt haast op gezet en je krijgt geen tijd",
            "Er wordt naar je pincode of je codes gevraagd",
            "De verkoper geeft je een factuur met een btw-nummer",
        ],
        antwoord=[0, 1, 2],
        uitleg="Buiten het systeem betalen, haast en vragen naar codes zijn alarmsignalen. Een factuur met btw-nummer is juist een teken van een echte verkoper.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag je pincode aan de telefoon doorgeven als iemand zegt dat hij van je bank is.",
        antwoord=False,
        uitleg="Nooit. Je pincode geef je aan niemand, ook niet aan iemand die zegt dat hij van de bank of van de politie is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je merkt dat er geld van je rekening verdwenen is. Wat doe je eerst?",
        opties=[
            "Je kaart laten blokkeren en je bank verwittigen",
            "Wachten of het bedrag de volgende dag terugkomt",
            "Je rekening zelf afsluiten via de app",
            "Een bericht plaatsen op sociale media",
        ],
        antwoord=0,
        uitleg="Blokkeer eerst, zodat het niet erger wordt, en verwittig je bank. Daarna doe je aangifte bij de politie.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij fraude met een betaalmiddel is aangifte doen bij de politie zinloos.",
        antwoord=False,
        uitleg="Het is net nodig: zonder aangifte kan je bank je meestal niet vergoeden en kan de fraude niet opgespoord worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarop let je als je betaalmiddel kiest voor een aankoop bij een onbekende verkoper?",
        opties=[
            "Of je de betaling kan laten terugdraaien als er iets misloopt",
            "Of er kosten aan het betaalmiddel verbonden zijn",
            "Of je niet meer kan verliezen dan het bedrag van de aankoop",
            "Of het betaalmiddel er mooi uitziet in je app",
        ],
        antwoord=[0, 1, 2],
        uitleg="Terugdraaien, kosten en je maximale verlies zijn de drie dingen die tellen. Daarom is een prepaidkaart of een betaling via de website zelf veiliger dan een overschrijving.",
    ),
    dict(
        type="waarofniet",
        vraag="Een aankoop op een markt of op een evenement betaal je vaak cash, zonder bewijs.",
        antwoord=True,
        uitleg="Klopt, en daarom is terugkomen op die aankoop lastig. Vraag altijd een ticket of een bewijs, ook bij een kleine verkoper.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemen we een vals bericht of een valse mail die je gegevens of je codes wil bemachtigen?",
        antwoord=["phishing", "phising"],
        uitleg="Bij phishing doet een bedrieger zich voor als je bank, een webshop of de overheid. Klik nooit op de link, ga zelf naar de echte app of website.",
    ),
]

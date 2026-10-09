# -*- coding: utf-8 -*-
"""De totale aankoopkost en het consumentenkrediet.

Het eerste van drie thema's uit "ik beheer mijn financiën", dat vijftien
procent weegt.

De fiche vraagt hier echt rekenwerk, dus dit thema staat vol getallen. Drie
berekeningen staan er letterlijk in: de nog openstaande schuld, de totale
rente (de fiche noemt die ook de meerprijs van de financiering) en de totale
terugbetaling.

De formules die hieronder gebruikt worden:

    totale terugbetaling = maandbedrag maal het aantal maanden
    totale rente         = totale terugbetaling min het geleende bedrag
    nog te betalen       = maandbedrag maal het aantal maanden dat nog rest

De totale aankoopkost is iets anders dan de prijs op het etiket:

    prijs min de commerciële korting
      plus de eenmalige bijkomende kosten (inschrijving, levering)
      plus de terugkerende bijkomende kosten (abonnement, verzekering)
      plus de btw volgens het tarief dat geldt

De vier consumentenkredieten van de fiche:
    de verkoop op afbetaling; de lening op afbetaling; de kredietopening via
    een kaart of een geoorloofde debetstand; de financieringshuur of leasing

En het verschil dat de fiche apart vraagt: de rentevoet is enkel de rente, het
jaarlijks kostenpercentage telt álle kosten van het krediet mee. Daarom is het
JKP het enige getal waarmee je twee kredieten eerlijk kan vergelijken.

Deel 1 is de totale aankoopkost en de verkoopovereenkomst.
Deel 2 is het consumentenkrediet, met het rekenwerk.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de totale kostprijs van een aankoop?",
        opties=[
            "de prijs na korting, met alle bijkomende kosten en de btw erbij",
            "de prijs die op het etiket staat",
            "de prijs zonder btw",
            "het bedrag dat je per maand afbetaalt",
        ],
        antwoord=0,
        uitleg="De fiche vraagt uitdrukkelijk de korting, de bijkomende kosten en de btw mee te rekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een commerciële korting?",
        opties=[
            "een vermindering die de verkoper zelf toestaat",
            "een korting die de overheid oplegt",
            "het deel van de prijs dat btw is",
            "een vergoeding voor het terugbrengen van een oud toestel",
        ],
        antwoord=0,
        uitleg="Ze gaat van de prijs af voor je de rest berekent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bijkomende kosten noemt de fiche eenmalig?",
        opties=[
            "de inschrijvingskost en de leveringskost",
            "het abonnement en de verzekering",
            "de btw en de accijnzen",
            "de rente en het jaarlijks kostenpercentage",
        ],
        antwoord=0,
        uitleg="Eenmalig betaal je één keer. Een abonnement en een verzekering keren terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bijkomende kosten noemt de fiche terugkerend?",
        opties=[
            "het abonnement en de verzekering",
            "de inschrijvingskost en de leveringskost",
            "de korting en de btw",
            "de rentevoet en de looptijd",
        ],
        antwoord=0,
        uitleg="Ze komen elke maand of elk jaar terug, en dus moet je ze meetellen over de hele periode.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fiets kost 800 euro, met 10 procent korting en 25 euro leveringskost. Wat is de totale kostprijs?",
        opties=["745 euro", "775 euro", "720 euro", "825 euro"],
        antwoord=0,
        uitleg="800 min 80 is 720, en daar komt 25 euro levering bij: 745 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een toestel kost 240 euro, met 15 euro inschrijvingskost en een abonnement van 12 euro per maand gedurende een jaar. Wat kost het je het eerste jaar?",
        opties=["399 euro", "267 euro", "255 euro", "384 euro"],
        antwoord=0,
        uitleg="240 plus 15 plus twaalf maal 12, dus 240 plus 15 plus 144 is 399 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hangt de btw af van het product dat je koopt?",
        opties=[
            "omdat er verschillende tarieven bestaan",
            "omdat elke winkel zijn eigen tarief mag kiezen",
            "omdat de btw per gemeente verschilt",
            "omdat dure producten geen btw hebben",
        ],
        antwoord=0,
        uitleg="De fiche zegt: de btw, afhankelijk van het btw-percentage.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een recht van de koper in een verkoopovereenkomst?",
        opties=[
            "een product krijgen dat is wat er beloofd werd",
            "het product op tijd betalen",
            "het product zorgvuldig gebruiken",
            "de verkoper op de hoogte houden",
        ],
        antwoord=0,
        uitleg="De andere drie zijn plichten van de koper, geen rechten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een plicht van de verkoper in een verkoopovereenkomst?",
        opties=[
            "leveren wat is afgesproken, in de afgesproken staat",
            "de prijs op tijd betalen",
            "het product goed onderhouden na de verkoop",
            "de koper een krediet aanbieden",
        ],
        antwoord=0,
        uitleg="De plicht van de koper is betalen, die van de verkoper leveren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een laptop kost 600 euro, met 50 euro korting en een verplichte verzekering van 5 euro per maand voor twee jaar. Wat betaal je in totaal?",
        opties=["670 euro", "550 euro", "610 euro", "720 euro"],
        antwoord=0,
        uitleg="600 min 50 is 550, plus vierentwintig maal 5, dus 550 plus 120 is 670 euro.",
    ),
    dict(
        type="waarofniet",
        vraag="De prijs op het etiket is altijd de totale kostprijs.",
        antwoord=False,
        uitleg="Levering, inschrijving, een abonnement of een verzekering kunnen er nog bijkomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een leveringskost is volgens de fiche een eenmalige bijkomende kost.",
        antwoord=True,
        uitleg="Ze staat er samen met de inschrijvingskost.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verzekering bij een aankoop is een terugkerende bijkomende kost.",
        antwoord=True,
        uitleg="Ze komt elke maand of elk jaar terug, net als een abonnement.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle producten hebben hetzelfde btw-tarief.",
        antwoord=False,
        uitleg="Er bestaan verschillende tarieven, en de fiche vraagt daar rekening mee te houden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat telt mee in de totale kostprijs van een aankoop?",
        opties=[
            "de commerciële korting",
            "de eenmalige bijkomende kosten",
            "de terugkerende bijkomende kosten",
            "het loon van de verkoper",
        ],
        antwoord=[0, 1, 2],
        uitleg="En de btw. Het loon van de verkoper zit al in de prijs verwerkt.",
    ),
    dict(
        type="invultekst",
        vraag="Een stoel kost 150 euro met 20 procent korting. Hoeveel betaal je? Antwoord met een getal.",
        antwoord=["120"],
        uitleg="20 procent van 150 is 30, dus je betaalt 120 euro.",
    ),
    dict(
        type="invultekst",
        vraag="Een abonnement kost 9 euro per maand. Hoeveel is dat op een jaar? Antwoord met een getal.",
        antwoord=["108"],
        uitleg="Twaalf maal 9 is 108 euro. Terugkerende kosten tel je over de hele periode.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een vermindering die de verkoper zelf toestaat? Vul aan: een ... korting.",
        antwoord=["commerciële", "commercieel"],
        uitleg="Ze gaat van de prijs af voor je de bijkomende kosten optelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee winkels verkopen dezelfde printer. De ene vraagt 180 euro met gratis levering, de andere 165 euro met 20 euro levering. Welke is voordeliger?",
        opties=[
            "de eerste, want 180 is minder dan 185",
            "de tweede, want 165 is minder dan 180",
            "ze zijn even duur",
            "dat valt niet te berekenen",
        ],
        antwoord=0,
        uitleg="165 plus 20 is 185. De totale kostprijs beslist, niet de prijs op het etiket.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vraagt de fiche naar de totale kostprijs en niet naar de prijs alleen?",
        opties=[
            "omdat je pas met de totale kost een eerlijke keuze kan maken",
            "omdat de prijs op het etiket vaak verkeerd staat",
            "omdat de btw niet altijd betaald moet worden",
            "omdat kortingen verboden zijn",
        ],
        antwoord=0,
        uitleg="Het leerdoel vraagt keuzes te beargumenteren met de totale kostprijs en de financieringskost erbij.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke vier consumentenkredieten noemt de fiche?",
        opties=[
            "verkoop op afbetaling, lening op afbetaling, kredietopening en financieringshuur",
            "hypotheek, lening, overschrijving en leasing",
            "kredietkaart, debetkaart, spaarrekening en termijnrekening",
            "lening, gift, voorschot en borgstelling",
        ],
        antwoord=0,
        uitleg="De kredietopening gaat via een kaart of een geoorloofde debetstand, de financieringshuur heet ook leasing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je koopt een wasmachine in de winkel en betaalt ze in twaalf maandelijkse schijven af. Welk krediet is dat?",
        opties=[
            "een verkoop op afbetaling",
            "een lening op afbetaling",
            "een kredietopening",
            "een financieringshuur",
        ],
        antwoord=0,
        uitleg="Het krediet hangt vast aan dat ene product dat je koopt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leent een bedrag bij de bank en betaalt het in vaste schijven terug, los van wat je ermee doet. Welk krediet is dat?",
        opties=[
            "een lening op afbetaling",
            "een verkoop op afbetaling",
            "een kredietopening",
            "een financieringshuur",
        ],
        antwoord=0,
        uitleg="Bij een lening op afbetaling krijg je geld, niet een bepaald product.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je mag met je kaart tot een bepaald bedrag onder nul gaan en betaalt rente op wat je gebruikt. Welk krediet is dat?",
        opties=[
            "een kredietopening",
            "een lening op afbetaling",
            "een verkoop op afbetaling",
            "een financieringshuur",
        ],
        antwoord=0,
        uitleg="De fiche noemt dat een kredietopening via een kaart of een geoorloofde debetstand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je huurt een wagen voor vier jaar en kan hem op het einde overkopen. Welk krediet is dat?",
        opties=[
            "een financieringshuur of leasing",
            "een verkoop op afbetaling",
            "een kredietopening",
            "een lening op afbetaling",
        ],
        antwoord=0,
        uitleg="Financieringshuur en leasing zijn in de fiche twee woorden voor hetzelfde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderdelen van een consumentenkrediet noemt de fiche?",
        opties=[
            "de looptijd, de rentevoet, het geleende bedrag, het JKP en het maandbedrag",
            "de prijs, de korting, de btw en de levering",
            "het loon, de uitgaven, de spaarbuffer en de inflatie",
            "de premie, de franchise en het verzekerd risico",
        ],
        antwoord=0,
        uitleg="Vijf onderdelen. De andere rijtjes horen bij andere thema's van de fiche.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de rentevoet en het jaarlijks kostenpercentage?",
        opties=[
            "het JKP telt alle kosten van het krediet mee, de rentevoet enkel de rente",
            "de rentevoet telt alle kosten mee, het JKP enkel de rente",
            "het JKP geldt per maand en de rentevoet per jaar",
            "er is geen verschil",
        ],
        antwoord=0,
        uitleg="Daarom is het JKP het enige getal waarmee je twee kredieten eerlijk vergelijkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leent 3.000 euro en betaalt 36 maanden lang 95 euro. Wat is de totale terugbetaling?",
        opties=["3.420 euro", "3.000 euro", "420 euro", "3.095 euro"],
        antwoord=0,
        uitleg="36 maal 95 is 3.420 euro.",
    ),
    dict(
        type="meerkeuze",
        vraag="En hoeveel rente betaal je in dat voorbeeld in totaal?",
        opties=["420 euro", "3.420 euro", "95 euro", "3.000 euro"],
        antwoord=0,
        uitleg="3.420 min 3.000 is 420 euro. De fiche noemt dat de meerprijs van de financiering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt van die 36 maanden er al 12 betaald. Hoeveel moet je nog betalen?",
        opties=["2.280 euro", "1.140 euro", "3.420 euro", "1.860 euro"],
        antwoord=0,
        uitleg="Er resten 24 maanden van 95 euro, dus 2.280 euro.",
    ),
    dict(
        type="waarofniet",
        vraag="Het jaarlijks kostenpercentage ligt nooit lager dan de rentevoet.",
        antwoord=True,
        uitleg="Het JKP bevat de rente plus de andere kosten, dus het kan er enkel gelijk aan of hoger zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een leasing ben je meteen eigenaar van het goed.",
        antwoord=False,
        uitleg="Je huurt het, met vaak een mogelijkheid om het op het einde over te kopen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een langere looptijd maakt je maandbedrag kleiner maar je totale kost groter.",
        antwoord=True,
        uitleg="Je betaalt langer rente, dus de meerprijs van de financiering loopt op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verkoop op afbetaling en een lening op afbetaling zijn hetzelfde.",
        antwoord=False,
        uitleg="Bij de eerste koop je een bepaald product, bij de tweede krijg je geld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatregelen helpen financiële problemen te vermijden?",
        opties=[
            "een spaarbuffer aanleggen voor onverwachte kosten",
            "je uitgaven en inkomsten opvolgen in een budgetplan",
            "kredieten vergelijken op hun JKP voor je tekent",
            "zo veel mogelijk kredieten tegelijk afsluiten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Kredieten stapelen is net wat je in de problemen brengt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn mogelijke gevolgen van te veel lenen?",
        opties=[
            "je raakt je maandelijkse aflossingen niet meer betaald",
            "je komt in een schuldenspiraal terecht",
            "je moet beroep doen op schuldbemiddeling",
            "je rentevoet daalt vanzelf",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een rentevoet daalt niet omdat je in de problemen zit, eerder omgekeerd.",
    ),
    dict(
        type="invultekst",
        vraag="Welk percentage telt alle kosten van een krediet mee? Antwoord met de afkorting.",
        antwoord=["JKP", "jkp"],
        uitleg="Het jaarlijks kostenpercentage, het enige eerlijke vergelijkingsgetal.",
    ),
    dict(
        type="invultekst",
        vraag="Je leent 1.200 euro en betaalt 24 maanden lang 55 euro. Hoeveel betaal je in totaal terug? Antwoord met een getal.",
        antwoord=["1320", "1.320"],
        uitleg="24 maal 55 is 1.320 euro.",
    ),
    dict(
        type="invultekst",
        vraag="En hoeveel rente is dat in totaal? Antwoord met een getal.",
        antwoord=["120"],
        uitleg="1.320 min 1.200 is 120 euro meerprijs.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee kredieten voor hetzelfde bedrag: het ene heeft een rentevoet van 4 procent en een JKP van 7, het andere een rentevoet van 5 procent en een JKP van 6. Welk is voordeliger?",
        opties=[
            "het tweede, want zijn JKP ligt lager",
            "het eerste, want zijn rentevoet ligt lager",
            "ze kosten evenveel",
            "dat hangt af van de bank",
        ],
        antwoord=0,
        uitleg="Het JKP bevat alle kosten. Een lage rentevoet met veel dossierkosten blijft duur.",
    ),
]

# -*- coding: utf-8 -*-
"""De vragen voor "De arbeidsmarkt en de collectieve afspraken" (🚀 Boost
doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
"marktwerking", tweede stuk: het marktmechanisme op de arbeidsmarkt, de
factoren die erop inwerken, en de collectieve afspraken: cao, ipa en
minimumloon. De product- en dienstenmarkt staat in [[ec_markt]].

Deel 1 gaat over vraag en aanbod van arbeid: wie vraagt, wie biedt aan, hoe het
evenwichtsloon tot stand komt, en welke factoren de curven verschuiven
(technologie, de goederenmarkt, de samenstelling van de bevolking,
bevolkingsgroei).
Deel 2 gaat over de collectieve afspraken: de cao, het interprofessioneel
akkoord, het minimumloon en hun invloed op het marktmechanisme.

Afspraak in dit thema: op de arbeidsmarkt vragen de bedrijven en bieden de
gezinnen aan. Dat staat in elke vraag waar verwarring mogelijk is met zoveel
woorden.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wie vraagt er arbeid op de arbeidsmarkt?",
        opties=[
            "De bedrijven",
            "De gezinnen",
            "De werkzoekenden",
            "De vakbonden",
        ],
        antwoord=0,
        uitleg="Op de arbeidsmarkt draaien de rollen om: de bedrijven zijn de vragers en de gezinnen de aanbieders.",
    ),
    dict(
        type="waarofniet",
        vraag="De prijs op de arbeidsmarkt is de pacht.",
        antwoord=False,
        uitleg="De prijs van arbeid is het loon. Pacht is de vergoeding voor grond. Vraag en aanbod bepalen samen het evenwichtsloon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom daalt de vraagcurve naar arbeid?",
        opties=[
            "Bij een lager loon willen bedrijven meer mensen aanwerven",
            "Bij een lager loon willen meer mensen gaan werken",
            "Bij een hoger loon stijgt de productiviteit",
            "Bij een hoger loon dalen de kosten",
        ],
        antwoord=0,
        uitleg="Arbeid is voor een bedrijf een kost. Hoe goedkoper, hoe meer uren het inzet, zolang die uren genoeg opbrengen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom stijgt de aanbodcurve van arbeid?",
        opties=[
            "Bij een hoger loon willen meer mensen gaan werken",
            "Bij een hoger loon werven bedrijven meer mensen aan",
            "Bij een lager loon stijgt de vrije tijd",
            "Bij een lager loon komen er meer banen bij",
        ],
        antwoord=0,
        uitleg="Een hoger loon maakt werken aantrekkelijker tegenover vrije tijd of studeren. Daarom biedt men meer uren aan.",
    ),
    dict(
        type="waarofniet",
        vraag="Op de arbeidsmarkt zijn de gezinnen de aanbieders.",
        antwoord=True,
        uitleg="Zij bieden hun arbeid aan en krijgen er loon voor. Op de goederenmarkt zijn ze net de vragers.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het loon waarbij vraag en aanbod van arbeid gelijk zijn? Schrijf één woord.",
        antwoord=["evenwichtsloon", "evenwichtsprijs"],
        uitleg="Bij het evenwichtsloon is het aantal gevraagde uren precies gelijk aan het aangeboden aantal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er als het loon boven het evenwicht ligt? Duid alles aan wat juist is.",
        opties=[
            "Er is meer aanbod dan vraag",
            "Er ontstaat werkloosheid",
            "Bedrijven werven minder mensen aan",
            "Er ontstaat een tekort aan arbeidskrachten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een te hoog loon maakt werken aantrekkelijk en aanwerven duur. Het overschot aan aanbod heet op deze markt werkloosheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een nieuwe technologie vervangt routinetaken. Wat gebeurt er met de vraag naar die arbeid?",
        opties=[
            "Ze daalt voor die taken, maar kan stijgen voor andere",
            "Ze stijgt voor alle soorten arbeid",
            "Ze blijft precies gelijk",
            "Ze verdwijnt volledig uit de economie",
        ],
        antwoord=0,
        uitleg="Technologie vervangt sommige taken en vult andere aan. Wie de machines bedient, onderhoudt en programmeert, wordt juist meer gevraagd.",
    ),
    dict(
        type="meerkeuze",
        vraag="De verkoop van auto's stijgt sterk. Wat gebeurt er op de arbeidsmarkt van de autosector?",
        opties=[
            "De vraag naar arbeid stijgt",
            "Het aanbod van arbeid stijgt",
            "De vraag naar arbeid daalt",
            "Er verandert niets",
        ],
        antwoord=0,
        uitleg="De vraag naar arbeid is afgeleid: ze volgt uit de vraag naar het product. Meer auto's verkopen betekent meer mensen nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de vraag naar arbeid die volgt uit de vraag naar producten? Schrijf twee woorden.",
        antwoord=["afgeleide vraag", "indirecte vraag"],
        uitleg="Niemand werft iemand aan om het aanwerven zelf. De vraag naar arbeid is afgeleid van de vraag naar wat het bedrijf maakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke factoren verschuiven het aanbod van arbeid? Duid alles aan wat juist is.",
        opties=[
            "De samenstelling van de bevolking, zoals vergrijzing",
            "Migratie",
            "De groei van de totale bevolking",
            "De vraag van de consument naar een bepaald product",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alles wat het aantal mensen op arbeidsleeftijd verandert, verschuift het aanbod. De vraag naar een product werkt net op de vraagzijde in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet vergrijzing met de arbeidsmarkt?",
        opties=[
            "Het aanbod van arbeid krimpt, want meer mensen gaan met pensioen",
            "De vraag naar arbeid krimpt, want er is minder werk",
            "Het aanbod van arbeid stijgt, want mensen werken langer",
            "Er verandert niets aan vraag of aanbod",
        ],
        antwoord=0,
        uitleg="Er gaan meer mensen uit dan er jongeren bijkomen. Daardoor verschuift de aanbodcurve naar links en komt het loon onder opwaartse druk.",
    ),
    dict(
        type="waarofniet",
        vraag="Migratie kan het aanbod van arbeid doen stijgen.",
        antwoord=True,
        uitleg="Komen er mensen op arbeidsleeftijd bij, dan schuift de aanbodcurve naar rechts. Bij emigratie gebeurt het omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom verschilt het loon sterk tussen beroepen?",
        opties=[
            "Omdat vraag en aanbod per beroep verschillen",
            "Omdat de overheid per beroep een loon vastlegt",
            "Omdat elk beroep evenveel opleiding vraagt",
            "Omdat alle bedrijven hetzelfde betalen",
        ],
        antwoord=0,
        uitleg="Een schaars beroep met veel vraag levert een hoog loon op. Is er veel aanbod en weinig vraag, dan ligt het loon lager.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een knelpuntberoep?",
        opties=[
            "Een beroep waarvoor bedrijven moeilijk mensen vinden",
            "Een beroep met een laag loon",
            "Een beroep dat binnenkort verdwijnt",
            "Een beroep waarvoor geen opleiding bestaat",
        ],
        antwoord=0,
        uitleg="Bij een knelpuntberoep is de vraag groter dan het aanbod. Dat duwt het loon omhoog en zet scholen aan om er meer mensen voor op te leiden.",
    ),
    dict(
        type="waarofniet",
        vraag="De arbeidsmarkt is één markt met één loon voor iedereen.",
        antwoord=False,
        uitleg="Ze valt uiteen in vele deelmarkten per beroep en per streek, elk met een eigen vraag, aanbod en loon.",
    ),
    dict(
        type="meerkeuze",
        vraag="De vraag naar arbeid is Qv = 1 000 − 20W en het aanbod Qa = 400 + 10W. Wat is het evenwichtsloon?",
        opties=[
            "20",
            "30",
            "40",
            "15",
        ],
        antwoord=0,
        uitleg="1 000 min 20W is gelijk aan 400 plus 10W geeft 600 is 30W, dus W is 20.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zelfde functies. Hoeveel arbeid wordt er in evenwicht gevraagd?",
        opties=[
            "600",
            "400",
            "1 000",
            "200",
        ],
        antwoord=0,
        uitleg="Vul W is 20 in: 1 000 min 400 is 600, en 400 plus 200 is ook 600.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf werft iemand aan zolang die meer opbrengt dan hij kost. Hoe heet die redenering?",
        opties=[
            "De marginale redenering, ook hier toegepast",
            "De gemiddelde redenering over alle werknemers",
            "De collectieve redenering van de sector",
            "De redenering van het break-evenpunt",
        ],
        antwoord=0,
        uitleg="Het is dezelfde logica als bij de productie: je zet er één bij zolang de extra opbrengst de extra kost dekt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom stijgt het loon in een sector waar bedrijven om dezelfde mensen vechten?",
        opties=[
            "Omdat de vraag groter is dan het aanbod",
            "Omdat de overheid dat oplegt",
            "Omdat de bedrijven dat onderling afspreken",
            "Omdat het aanbod groter is dan de vraag",
        ],
        antwoord=0,
        uitleg="Wie te weinig biedt, vindt niemand. Dat tekort duwt het loon omhoog tot vraag en aanbod weer gelijklopen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een collectieve arbeidsovereenkomst?",
        opties=[
            "Een akkoord over loon en arbeidsvoorwaarden",
            "Een contract tussen één werkgever en één van zijn werknemers",
            "Een wet die de overheid voor alle sectoren maakt",
            "Een afspraak tussen twee bedrijven over hun prijzen",
        ],
        antwoord=0,
        uitleg="Een cao wordt gesloten tussen werkgeversorganisaties en vakbonden, voor een hele sector of voor één bedrijf. Ze geldt dan voor alle werknemers die eronder vallen.",
    ),
    dict(
        type="invultekst",
        vraag="Waar staat de afkorting cao voor? Schrijf drie woorden.",
        antwoord=["collectieve arbeidsovereenkomst", "collectieve arbeidsovereenkomsten"],
        uitleg="Een cao is een collectieve arbeidsovereenkomst: een afspraak voor een hele groep werknemers tegelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een interprofessioneel akkoord?",
        opties=[
            "Een akkoord over alle sectoren heen",
            "Een akkoord binnen één bedrijf",
            "Een akkoord tussen twee vakbonden",
            "Een akkoord tussen België en zijn vier buurlanden",
        ],
        antwoord=0,
        uitleg="Het ipa wordt op nationaal niveau gesloten tussen de werkgevers- en de werknemersorganisaties. Het legt onder meer de marge vast waarbinnen de lonen mogen stijgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat regelt een cao zoal? Duid alles aan wat juist is.",
        opties=[
            "Het loon in een sector",
            "De arbeidsduur",
            "Extra voordelen zoals een vergoeding voor woon-werkverkeer",
            "De verkoopprijs van de producten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een cao gaat over de arbeidsvoorwaarden: loon, uren, verlof en vergoedingen. Over verkoopprijzen gaat ze niet, dat zou zelfs verboden overleg zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het minimumloon?",
        opties=[
            "Een wettelijke ondergrens voor het loon",
            "Het laagste loon dat in een bedrijf betaald wordt",
            "Het gemiddelde loon van de laagste functies",
            "Het loon van een beginnende werknemer",
        ],
        antwoord=0,
        uitleg="Het minimumloon is een bodem: lager betalen mag niet. Op de grafiek is het precies een minimumprijs, maar dan op de arbeidsmarkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een minimumloon ligt boven het evenwichtsloon. Wat gebeurt er volgens het model? Duid alles aan wat juist is.",
        opties=[
            "Er wordt meer arbeid aangeboden",
            "Er wordt minder arbeid gevraagd",
            "Er ontstaat werkloosheid",
            "Er ontstaat een tekort aan arbeidskrachten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het is een minimumprijs boven het evenwicht, en dat geeft een overschot. Op de arbeidsmarkt heet dat overschot werkloosheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Een minimumloon onder het evenwichtsloon verandert niets aan de markt.",
        antwoord=True,
        uitleg="De markt betaalt dan al meer dan het minimum. Zo'n bodem is niet bindend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom bestaat er toch een minimumloon?",
        opties=[
            "Om te vermijden dat werkenden niet rondkomen",
            "Om de winst van de bedrijven te verhogen",
            "Om de werkloosheid te doen stijgen",
            "Om de prijzen in de winkel wat te verlagen",
        ],
        antwoord=0,
        uitleg="Het is een keuze tussen bescherming en mogelijke werkloosheid aan de onderkant. De wetgever vindt die bescherming de moeite waard.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het overschot aan arbeidsaanbod? Schrijf één woord.",
        antwoord=["werkloosheid", "werkloos"],
        uitleg="Wie wil werken aan het geldende loon maar geen werk vindt, is werkloos. In het model is dat het overschot op de arbeidsmarkt.",
    ),
    dict(
        type="waarofniet",
        vraag="Over een cao onderhandelen de vakbonden en de werkgeversorganisaties.",
        antwoord=True,
        uitleg="Dat zijn de sociale partners: de vakbonden langs de ene kant en de werkgeversorganisaties langs de andere.",
    ),
    dict(
        type="waarofniet",
        vraag="Een cao geldt alleen voor wie bij een vakbond aangesloten is.",
        antwoord=False,
        uitleg="Ze geldt voor alle werknemers die onder dat paritair comité vallen, ook voor wie niet aangesloten is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe beïnvloeden collectieve afspraken het marktmechanisme?",
        opties=[
            "Ze leggen het loon deels vast",
            "Ze maken het loon op de markt volledig vrij",
            "Ze verhogen altijd de vraag naar arbeid",
            "Ze verlagen altijd het aanbod van arbeid",
        ],
        antwoord=0,
        uitleg="Het loon wordt dan deels bepaald door onderhandeling in plaats van door de markt alleen. Daardoor beweegt het trager mee met schommelingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de automatische indexering van de lonen?",
        opties=[
            "De lonen stijgen mee wanneer de prijzen stijgen",
            "De lonen stijgen elk jaar met een vast percentage",
            "De lonen stijgen met de winst van het bedrijf",
            "De lonen stijgen met de leeftijd van de werknemer",
        ],
        antwoord=0,
        uitleg="De index koppelt het loon aan de levensduurte, zodat de koopkracht bewaard blijft. Dat is in België bijzonder: veel landen hebben het niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke argumenten worden tegen een hoog minimumloon gebruikt? Duid alles aan wat juist is.",
        opties=[
            "Bedrijven werven minder laaggeschoolden aan",
            "Sommige banen verdwijnen naar het buitenland",
            "Automatisering wordt aantrekkelijker dan mensen inzetten",
            "De koopkracht van de laagste lonen daalt erdoor",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie zijn de gebruikelijke bezwaren. De koopkracht van wie het minimumloon krijgt, stijgt er juist door: dat is net het doel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een interprofessioneel akkoord wordt per bedrijf afzonderlijk gesloten.",
        antwoord=False,
        uitleg="Het ipa geldt over alle sectoren heen, op nationaal niveau. Afspraken per bedrijf gebeuren in een bedrijfs-cao.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een sector spreekt in een cao een loonsverhoging van 3 % af. Wat is het gevolg voor de bedrijven?",
        opties=[
            "Hun loonkosten stijgen",
            "Hun loonkosten dalen met hetzelfde percentage",
            "Hun verkoopprijzen dalen automatisch",
            "Hun productie stijgt vanzelf met 3 %",
        ],
        antwoord=0,
        uitleg="Arbeid wordt duurder, dus sommige bedrijven werven minder aan of investeren in machines. Of dat echt gebeurt, hangt af van hoeveel die arbeid opbrengt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de vakbonden en de werkgeversorganisaties samen? Schrijf twee woorden.",
        antwoord=["sociale partners", "de sociale partners"],
        uitleg="De sociale partners voeren het sociaal overleg, van het bedrijf tot het nationale niveau.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebeurt loonvorming in België niet volledig via de markt?",
        opties=[
            "Omdat één werknemer zwak staat tegenover een werkgever",
            "Omdat de bedrijven dan te weinig winst zouden overhouden",
            "Omdat de markt geen lonen kan berekenen",
            "Omdat de prijzen anders te snel zouden dalen",
        ],
        antwoord=0,
        uitleg="Eén werknemer staat zwak tegenover een werkgever. Door collectief te onderhandelen, wegen beide kanten zwaarder door.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een technologische doorbraak verhoogt de productiviteit sterk. Wat is een mogelijk gevolg voor de lonen?",
        opties=[
            "De lonen kunnen stijgen zonder hogere kost per stuk",
            "De lonen moeten dan noodzakelijk gaan dalen",
            "De lonen blijven altijd precies gelijk",
            "De lonen worden dan door de overheid vastgelegd",
        ],
        antwoord=0,
        uitleg="Als elke werknemer meer maakt, kan een hoger loon uit diezelfde productie betaald worden. Daarom koppelt het ipa de loonmarge aan de productiviteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men de arbeidsmarkt bijzonder, anders dan de markt voor een gewoon goed?",
        opties=[
            "Omdat het om mensen gaat en niet om voorraad",
            "Omdat er geen vraag en aanbod op bestaat",
            "Omdat de prijs er niet bestaat",
            "Omdat er in een land maar één werkgever is",
        ],
        antwoord=0,
        uitleg="Arbeid kan je niet bewaren en niet losmaken van de persoon. Daarom gelden er afspraken en bescherming die je bij tarwe of staal niet nodig hebt.",
    ),
]

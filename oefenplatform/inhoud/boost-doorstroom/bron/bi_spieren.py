# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — De spieren en de klieren.

Hoort bij "waarnemen en verwerken van prikkels" van de vakfiche biologie
2de graad doorstroomfinaliteit: de effectoren aan het einde van de weg van
prikkel naar reactie.

Deel 1 gaat over de spieren, van de drie soorten spierweefsel tot de
microscopische bouw die de fiche uitdrukkelijk vraagt: Z-plaat, lichte en
donkere band, sarcomeer, actine- en myosinefilament. Deel 2 gaat over de
klieren en de hormonen, met de eilandjes van Langerhans en hun alfa- en
bètacellen als uitgewerkt voorbeeld.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke drie soorten spierweefsel onderscheidt men bij de mens?",
        opties=[
            "skeletspierweefsel, glad spierweefsel en hartspierweefsel",
            "skeletspierweefsel, kraakbeenweefsel en beenweefsel",
            "glad spierweefsel, peesweefsel en gewrichtsbanden",
            "hartspierweefsel, zenuwweefsel en vetweefsel",
        ],
        antwoord=0,
        uitleg="Skeletspieren bewegen je botten, glad spierweefsel zit in de organen en hartspierweefsel vormt het hart. Pezen en kraakbeen zijn geen spier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is kenmerkend voor skeletspierweefsel? Kruis alles aan wat juist is.",
        opties=[
            "je kan het met je wil aansturen",
            "het ziet onder de microscoop gestreept uit",
            "het hecht met pezen aan de botten vast",
            "het trekt samen zonder dat je het kan beslissen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een skeletspier is willekeurig: jij beslist. Dat laatste geldt juist voor glad spierweefsel en voor de hartspier.",
    ),
    dict(
        type="waarofniet",
        vraag="Glad spierweefsel komt onder meer in de wand van de darmen en de bloedvaten voor.",
        antwoord=True,
        uitleg="Daar duwt het de darminhoud voort of vernauwt het een bloedvat. Dat gebeurt buiten je wil om.",
    ),
    dict(
        type="invultekst",
        vraag="Waarmee is een skeletspier aan een bot vastgemaakt?",
        antwoord=["pees", "een pees", "pezen"],
        uitleg="Een pees is stevig bindweefsel zonder rekbaarheid. Daardoor gaat de kracht van de spier helemaal naar het bot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een antagonistisch spierpaar?",
        opties=[
            "twee spieren die tegengesteld werken, zoals de buiger en de strekker van de arm",
            "twee spieren die altijd samen samentrekken en dus dezelfde beweging maken",
            "een spier en de pees waarmee hij aan het bot van een gewricht vastzit",
            "een spier die aan twee botten tegelijk vastzit en er geen tegenspeler heeft",
        ],
        antwoord=0,
        uitleg="Een spier kan enkel trekken, niet duwen. Daarom is er voor elke beweging een tegenspeler die het gewricht de andere kant op trekt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een spier kan zowel trekken als duwen.",
        antwoord=False,
        uitleg="Een spier wordt korter en trekt dus. Om terug te gaan is altijd een tegenspeler of de zwaartekracht nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de kleinste eenheid die in een spiervezel samentrekt, tussen twee Z-platen?",
        antwoord=["sarcomeer", "een sarcomeer", "het sarcomeer"],
        uitleg="Een spiervezel is een lange rij sarcomeren achter elkaar. Worden ze allemaal een beetje korter, dan wordt de hele spier merkbaar korter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat begrenst een sarcomeer aan beide kanten?",
        opties=[
            "een Z-plaat",
            "een pees",
            "een celmembraan",
            "een myelineschede",
        ],
        antwoord=0,
        uitleg="De Z-platen zijn de dwarse schotjes waar de dunne filamenten aan vasthangen. Van de ene Z-plaat tot de volgende is één sarcomeer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee soorten filamenten liggen in een sarcomeer?",
        opties=[
            "actinefilamenten en myosinefilamenten",
            "collageenfilamenten en elastinefilamenten",
            "xyleemfilamenten en floëemfilamenten",
            "dendrietfilamenten en axonfilamenten",
        ],
        antwoord=0,
        uitleg="De dunne actinefilamenten hangen aan de Z-platen, de dikke myosinefilamenten liggen in het midden. Hun samenspel maakt de samentrekking.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe wordt een sarcomeer korter?",
        opties=[
            "de myosinefilamenten trekken de actinefilamenten naar het midden toe",
            "de actinefilamenten worden zelf korter en dikker",
            "de Z-platen lossen op en vormen zich op een nieuwe plaats",
            "er komt vocht bij, waardoor het sarcomeer opbolt",
        ],
        antwoord=0,
        uitleg="De filamenten blijven even lang. De myosinekopjes grijpen de actine vast en trekken die erlangs, zodat de Z-platen naar elkaar schuiven.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een samentrekking worden de actine- en myosinefilamenten zelf niet korter.",
        antwoord=True,
        uitleg="Ze schuiven alleen verder langs elkaar. Daarom heet dit het schuiffilamentmodel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zie je in een spiervezel onder de microscoop als een donkere band?",
        opties=[
            "de zone waar de dikke myosinefilamenten liggen",
            "de zone waar enkel actinefilamenten liggen",
            "de Z-plaat zelf, van opzij gezien",
            "de pees die aan de spiervezel vastzit",
        ],
        antwoord=0,
        uitleg="Waar de dikke filamenten liggen, gaat minder licht door en ziet het donker. In de lichte band liggen alleen de dunne actinefilamenten.",
    ),
    dict(
        type="invultekst",
        vraag="In welke band van het sarcomeer liggen enkel actinefilamenten?",
        antwoord=["lichte band", "de lichte band", "lichte"],
        uitleg="De lichte band ligt rond de Z-plaat, waar de dikke filamenten niet komen. Bij een samentrekking wordt net die band smaller.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een samentrekking wordt de lichte band van een sarcomeer breder.",
        antwoord=False,
        uitleg="Ze wordt juist smaller. De actine schuift verder tussen de myosine, dus blijft er minder plaats over waar enkel actine ligt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat heeft een spiervezel nodig om te kunnen samentrekken? Kruis alles aan wat juist is.",
        opties=[
            "een prikkel van een motorische zenuwcel",
            "energie uit de celademhaling",
            "calciumionen in de cel",
            "licht dat op de vezel valt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een zenuwsignaal laat calcium vrijkomen, en met energie uit de celademhaling kan de myosine dan werken. Licht komt er niet bij te pas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft spierweefsel veel mitochondriën?",
        opties=[
            "daar wordt de energie vrijgemaakt die een samentrekking kost",
            "daar worden de actinefilamenten van het sarcomeer aangemaakt",
            "daar wordt de prikkel van de motorische zenuwcel opgevangen",
            "daar wordt het bloed door de vezels van de spier gepompt",
        ],
        antwoord=0,
        uitleg="Een mitochondrion is de plaats van de celademhaling. Een spier die veel werkt, heeft dus veel mitochondriën nodig.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij zwaar inspannen werkt een spier een tijdje door zonder genoeg zuurstof, en dan vormt zich melkzuur.",
        antwoord=True,
        uitleg="Zonder genoeg zuurstof schakelt de spier over op een omweg die melkzuur oplevert. Dat geeft het branderige gevoel in je benen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de hartspier een apart soort spierweefsel?",
        opties=[
            "hij is gestreept zoals een skeletspier maar werkt buiten je wil, en zijn cellen zijn met elkaar verbonden",
            "hij bestaat niet uit sarcomeren maar uit losse vezels die elk op zichzelf samentrekken en weer verslappen",
            "hij kan zowel trekken als duwen en heeft daardoor geen tegenspeler nodig",
            "hij hecht met pezen aan de ribben vast en trekt de borstkas bij elke slag samen",
        ],
        antwoord=0,
        uitleg="De hartspier combineert het beste van de twee andere: de kracht van gestreept weefsel met de onvermoeibaarheid van onwillekeurig weefsel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de plaats waar een motorische zenuwcel een spiervezel aanspreekt?",
        antwoord=["motorische eindplaat", "eindplaat", "neuromusculaire synaps"],
        uitleg="Op de motorische eindplaat geeft het eindknopje zijn boodschapperstof af aan de spiervezel. Die vezel trekt dan samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je houdt een boek stil in je uitgestrekte hand, en na een tijd begint je arm te trillen. Hoe verklaar je dat?",
        opties=[
            "de spiervezels werken in ploegen en de overgangen vallen bij vermoeidheid niet meer gelijk",
            "de botten in je arm beginnen door het gewicht van het boek lichtjes te buigen",
            "de pees laat tijdelijk los van het bot en schiet er daarna weer tegenaan",
            "de sarcomeren worden steeds langer tot de spiervezel uiteindelijk scheurt",
        ],
        antwoord=0,
        uitleg="Niet alle vezels werken tegelijk; ze lossen elkaar af zodat de spier het langer uithoudt. Raken ze vermoeid, dan verloopt dat aflossen minder vloeiend en trilt de arm.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een klier met afvoergang en een klier zonder afvoergang?",
        opties=[
            "een klier zonder afvoergang geeft haar stof rechtstreeks aan het bloed af",
            "een klier zonder afvoergang maakt zelf helemaal geen stoffen aan",
            "een klier met afvoergang zit altijd in of net onder de hersenen",
            "een klier met afvoergang werkt enkel bij kinderen en valt later stil",
        ],
        antwoord=0,
        uitleg="Klieren met afvoergang, zoals de zweetklier, lozen naar buiten of in een holte. Klieren zonder afvoergang geven hormonen aan het bloed.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een boodschapperstof die een klier aan het bloed afgeeft?",
        antwoord=["hormoon", "een hormoon", "hormonen"],
        uitleg="Een hormoon reist met het bloed door het hele lichaam, maar werkt enkel op de cellen die er de juiste receptor voor hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn klieren zonder afvoergang? Kruis alles aan wat juist is.",
        opties=[
            "de schildklier",
            "de bijnier",
            "de eilandjes van Langerhans in de pancreas",
            "de zweetklier in de huid",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie geven hun hormoon rechtstreeks aan het bloed. Een zweetklier heeft wel een afvoergang en loost op de huid.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hormoon werkt enkel op cellen die er de passende receptor voor hebben.",
        antwoord=True,
        uitleg="Het hormoon komt wel overal, maar enkel een cel met het juiste slot reageert erop. Daarom is een hormoon toch doelgericht.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de groepjes hormoonvormende cellen in de pancreas?",
        antwoord=["eilandjes van langerhans", "eilandje van langerhans"],
        uitleg="Die eilandjes liggen als eilandjes verspreid in de pancreas, tussen het weefsel dat spijsverteringssappen maakt. Zij regelen het bloedglucosegehalte.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk hormoon maken de bètacellen van de eilandjes van Langerhans aan?",
        opties=[
            "insuline",
            "glucagon",
            "adrenaline",
            "auxine",
        ],
        antwoord=0,
        uitleg="De bètacellen maken insuline, dat het bloedglucosegehalte doet dalen. De alfacellen maken glucagon, dat het laat stijgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet insuline?",
        opties=[
            "het laat de cellen glucose uit het bloed opnemen, zodat het bloedglucosegehalte daalt",
            "het laat de lever glucose aan het bloed afgeven, zodat het gehalte stijgt",
            "het verhoogt de hartslag bij een schrikreactie",
            "het laat de huidmondjes van een plant sluiten",
        ],
        antwoord=0,
        uitleg="Na een maaltijd zit er veel glucose in het bloed. Insuline zet de deur van de cellen open en laat de lever glucose opslaan.",
    ),
    dict(
        type="invultekst",
        vraag="Welk hormoon van de alfacellen laat het bloedglucosegehalte stijgen?",
        antwoord=["glucagon", "het glucagon"],
        uitleg="Zit er te weinig glucose in het bloed, dan geeft glucagon de lever het signaal om haar voorraad weer af te breken.",
    ),
    dict(
        type="waarofniet",
        vraag="Insuline en glucagon werken tegengesteld op het bloedglucosegehalte.",
        antwoord=True,
        uitleg="Het een doet het gehalte dalen, het ander stijgen. Samen houden ze het binnen nauwe grenzen, en dat is homeostase.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je eet een boterham met confituur. Wat gebeurt er daarna?",
        opties=[
            "het bloedglucosegehalte stijgt, de bètacellen geven insuline af en het gehalte daalt weer",
            "het bloedglucosegehalte stijgt, de alfacellen geven glucagon af en het gehalte stijgt verder",
            "het bloedglucosegehalte daalt, de bètacellen geven insuline af",
            "het bloedglucosegehalte blijft gelijk, want hormonen werken enkel bij inspanning",
        ],
        antwoord=0,
        uitleg="Stijgt het gehalte, dan treedt insuline op. Dat is een feedbacksysteem: het gevolg van het eten stuurt zelf de bijsturing aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is er bij diabetes type 1 aan de hand?",
        opties=[
            "de bètacellen maken geen of te weinig insuline meer aan",
            "de alfacellen maken te veel glucagon aan",
            "de lever kan geen glucose meer opslaan",
            "de darmen nemen geen glucose meer op uit het eten",
        ],
        antwoord=0,
        uitleg="Bij type 1 zijn de bètacellen beschadigd, vaak door het eigen afweersysteem. Daarom moet de insuline van buiten toegediend worden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een feedbacksysteem met hormonen houdt een waarde in het lichaam binnen nauwe grenzen.",
        antwoord=True,
        uitleg="Dat is precies homeostase: wijkt de waarde af, dan komt er een hormoon dat haar terugbrengt. Zo blijft het inwendig milieu stabiel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk hormoon van de bijnier zet het lichaam bij schrik of gevaar in actie?",
        opties=[
            "adrenaline",
            "insuline",
            "thyroxine",
            "ethyleen",
        ],
        antwoord=0,
        uitleg="Adrenaline laat je hart sneller slaan, je ademhaling versnellen en je pupillen wijder worden. Zo is je lichaam klaar om te vluchten of te vechten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke veranderingen horen bij een stoot adrenaline? Kruis alles aan wat juist is.",
        opties=[
            "de hartslag versnelt",
            "de pupillen worden groter",
            "er komt glucose uit de lever vrij",
            "de spijsvertering versnelt sterk",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alles wat voor onmiddellijke actie dient, gaat omhoog. De spijsvertering gaat net op een lager pitje, want die kan wachten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hormoon werkt sneller dan een zenuwimpuls.",
        antwoord=False,
        uitleg="Een hormoon moet met het bloed meereizen en doet er seconden tot minuten over. Een zenuwimpuls is er in milliseconden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men de hypofyse soms de dirigent van de klieren?",
        opties=[
            "ze geeft hormonen af die andere klieren aanzetten of afremmen",
            "ze maakt alle hormonen van het lichaam in haar eigen cellen aan",
            "ze ligt midden tussen alle andere klieren van het lichaam in",
            "ze voert alle hormonen na gebruik weer uit het bloed af",
        ],
        antwoord=0,
        uitleg="De hypofyse ligt onder de hersenen en stuurt onder andere de schildklier en de geslachtsklieren aan. Zo verbindt ze het zenuwstelsel met de hormonen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke klier in de hals regelt met haar hormoon de snelheid van de stofwisseling?",
        antwoord=["schildklier", "de schildklier"],
        uitleg="De schildklier maakt thyroxine. Te weinig maakt traag en koud, te veel maakt onrustig en doet vermageren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een klier is ofwel effector van het zenuwstelsel, ofwel zender van hormonen, nooit beide.",
        antwoord=False,
        uitleg="De bijnier is beide tegelijk: een zenuwsignaal laat haar adrenaline afgeven. Zenuwstelsel en hormonen werken dus samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het zinvol dat het zenuwstelsel en het hormonale stelsel samenwerken?",
        opties=[
            "het zenuwstelsel reageert snel en kort, de hormonen houden de reactie langer aan",
            "ze doen precies hetzelfde, dus is er een reserve",
            "hormonen kunnen geen enkele spier bereiken",
            "het zenuwstelsel werkt enkel bij dag en de hormonen enkel bij nacht",
        ],
        antwoord=0,
        uitleg="Bij schrik trekt je lichaam meteen samen door de zenuwen, en adrenaline houdt je daarna nog minuten paraat. Snel en lang, elk zijn deel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een sportarts vindt bij een atleet een laag bloedglucosegehalte na een lange inspanning. Welke reactie van het lichaam verwacht je?",
        opties=[
            "de alfacellen geven glucagon af en de lever breekt haar voorraad af",
            "de bètacellen geven meer insuline af zodat de cellen nog meer opnemen",
            "de schildklier legt de stofwisseling helemaal stil",
            "de bijnier stopt met het afgeven van adrenaline",
        ],
        antwoord=0,
        uitleg="Bij een te laag gehalte treedt glucagon op. De lever geeft glucose vrij en het gehalte komt weer binnen de grenzen.",
    ),
]

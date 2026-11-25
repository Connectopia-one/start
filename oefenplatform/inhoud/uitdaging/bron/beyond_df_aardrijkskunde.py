# -*- coding: utf-8 -*-
"""Uitdaging Aardrijkskunde 🌍 Beyond dubbele finaliteit (25 november 2026), in
de vormen van het examen van de Examencommissie: 40 vragen die alle
hoofdstukken door elkaar halen. Een klimatogram en de baan van de aarde om op
te klikken, tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde,
rekenvragen en een korte schrijfopdracht. Geen nieuwe leerstof: alles staat in
de hoofdstukken van Aardrijkskunde Beyond dubbele finaliteit.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_df_aardrijkskunde.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-dubbele-finaliteit"
VAK = "Aardrijkskunde"
BESTAND = "beyond-df-aardrijkskunde-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/aardrijkskunde-beyond-df-uitdaging"
KLIM = "klimatogram-kuststad.svg"
BAAN = "baan-aarde.svg"

# klikvakken uit maak_prenten_beyond_df_aardrijkskunde.py
JULI = [50.0, 18.3, 6.3, 71.7]
NOVEMBER = [75.3, 18.3, 6.3, 71.7]
JANUARI = [12.0, 18.3, 6.3, 71.7]
A = [9.2, 45.2, 9.6, 19.4]
B = [45.2, 75.8, 9.6, 19.4]
C = [81.2, 45.2, 9.6, 19.4]
D = [45.2, 14.5, 9.6, 19.4]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Klimatogram (prent)
    klik("Bekijk het klimatogram. Klik op de droogste maand.",
         KLIM, [JULI],
         "In juli valt maar 5 mm neerslag: de laagste staaf."),
    klik("Klik op de natste maand.",
         KLIM, [NOVEMBER],
         "In november valt 110 mm: de hoogste staaf."),
    klik("Klik op de koudste maand.",
         KLIM, [JANUARI],
         "De temperatuurlijn is het laagst in januari: 9 °C."),
    met_prent(KLIM, tabel(
        "Lees af en reken.",
        [
            ("Temperatuur van de warmste maand (°C)", "26"),
            ("Jaarlijkse temperatuuramplitude (°C)", "17"),
            ("Totale jaarneerslag (mm)", "675"),
        ],
        "Warmste maand 26 °C, koudste 9 °C: amplitude 17 °C. Neerslag: 80 + 70 + 60 + 55 + 35 + 15 + 5 + 10 + 45 + 95 + 110 + 95 = 675 mm.",
        kolommen=["17", "26", "675"])),
    met_prent(KLIM, mk(
        "Welk klimaattype past bij dit klimatogram?",
        ["Mediterraan: droge, hete zomer en zachte, natte winter.", "Gematigd zeeklimaat: het hele jaar neerslag en koele zomers.", "Tropisch regenwoudklimaat: elke maand warm en zeer nat.", "Woestijnklimaat: het hele jaar door bijna geen neerslag van betekenis."],
        0,
        "Alle maanden zijn boven 0 °C, de zomer is heet en droog en de meeste regen valt in de herfst en winter: typisch mediterraan.")),
    met_prent(KLIM, keuze(
        "De droge zomer komt doordat de stad dan onder invloed ligt van een [[*subtropisch hogedrukgebied|lagedrukgebied van de poolfront|moessonwind]]. Typische vegetatie is [[*maquis met olijfbomen|tropisch regenwoud|toendra]].",
        "In de zomer schuift de subtropische hogedrukgordel naar het noorden. Planten met harde, kleine bladeren zijn aangepast aan droogte.")),

    # Baan van de aarde (prent)
    klik("Bekijk de baan van de aarde. Klik op de aarde op 21 juni.",
         BAAN, [A],
         "Op 21 juni helt de noordpool naar de zon toe. Dat is in positie A: de as wijst daar naar de zon."),
    klik("Klik op de aarde op 21 december.",
         BAAN, [C],
         "Op 21 december helt de noordpool van de zon weg. Dan is het winter op het noordelijk halfrond."),
    klik("Klik op een positie waarop dag en nacht overal op aarde ongeveer even lang zijn.",
         BAAN, [B, D],
         "Bij de equinoxen (rond 21 maart en 23 september) helt geen van beide polen naar de zon: overal ongeveer 12 uur licht."),
    met_prent(BAAN, tabel(
        "Klopt dit over de seizoenen en de baan van de aarde?",
        [
            ("De seizoenen ontstaan door de schuine stand van de aardas.", J),
            ("In positie A staat de zon loodrecht boven de Kreeftskeerkring.", J),
            ("In positie C is het zomer in Australië.", J),
            ("De seizoenen ontstaan omdat de afstand tot de zon sterk verandert.", F),
        ],
        "De hellingshoek van 23,5° zorgt voor wisselende invalshoeken. De afstand tot de zon verandert maar weinig en is niet de oorzaak.")),

    # Situeren en heelal
    tabel(
        "Op welk halfrond ligt de plaats?",
        [
            ("50° NB, 5° OL", "Noordelijk en oostelijk"),
            ("34° ZB, 18° OL", "Zuidelijk en oostelijk"),
            ("40° NB, 74° WL", "Noordelijk en westelijk"),
        ],
        "NB en ZB geven de breedte (noord of zuid van de evenaar), OL en WL de lengte (oost of west van de nulmeridiaan).",
        kolommen=["Noordelijk en oostelijk", "Zuidelijk en oostelijk", "Noordelijk en westelijk"]),
    inv("Het is 12 uur in Greenwich (0°). Hoe laat is het zonnetijd op 45° OL? Geef het uur als getal.",
        ["15"],
        "De aarde draait 15° per uur. 45° oost is 3 uur later: 15 uur."),
    volgorde(
        "Rangschik van klein naar groot.",
        ["Maan", "Aarde", "Jupiter", "Zon", "Melkweg"],
        "De maan is kleiner dan de aarde, Jupiter is de grootste planeet, de zon is een ster en de Melkweg bevat miljarden sterren."),
    sorteer(
        "Is dit een binnenplaneet (rotsplaneet) of een buitenplaneet (gasreus)?",
        ["Rotsplaneet", "Gasreus"],
        [
            ["Mars", "Rotsplaneet"],
            ["Saturnus", "Gasreus"],
            ["Venus", "Rotsplaneet"],
            ["Neptunus", "Gasreus"],
        ],
        "Mercurius, Venus, aarde en Mars zijn klein en rotsachtig. Jupiter, Saturnus, Uranus en Neptunus zijn grote gasreuzen."),
    keuze(
        "Een komeet bestaat vooral uit [[*ijs en stof|gesmolten metaal|waterstofgas]] en krijgt een staart als ze [[*dicht bij de zon|ver van de zon]] komt.",
        "Bij de zon verdampt het ijs. De zonnewind blaast gas en stof weg in een staart die van de zon af wijst."),

    # Atmosfeer, wind en neerslag
    tabel(
        "In welke laag van de atmosfeer?",
        [
            ("Hier gebeurt het weer en daalt de temperatuur met de hoogte.", "Troposfeer"),
            ("Hier ligt de ozonlaag.", "Stratosfeer"),
            ("Hier stijgt de temperatuur met de hoogte doordat ozon uv opvangt.", "Stratosfeer"),
            ("Hier vormen zich bijna alle wolken.", "Troposfeer"),
        ],
        "De troposfeer is de onderste laag met wolken en neerslag. In de stratosfeer houdt ozon uv-straling tegen.",
        kolommen=["Troposfeer", "Stratosfeer"]),
    keuze(
        "Wind waait van een [[*hogedrukgebied|lagedrukgebied]] naar een [[*lagedrukgebied|hogedrukgebied]]. Op het noordelijk halfrond buigt de corioliskracht de wind naar [[*rechts|links]] af.",
        "Lucht stroomt van hoge naar lage druk. Door de draaiing van de aarde wijkt ze op het noordelijk halfrond naar rechts af."),
    inv("De temperatuur aan zee is 20 °C. Hoe warm is het ongeveer op 2000 m hoogte als de temperatuur 0,6 °C per 100 m daalt?",
        ["8"],
        "2000 m / 100 m = 20 · 0,6 = 12 °C kouder: 20 − 12 = 8 °C."),
    tabel(
        "Welk soort neerslag is dit?",
        [
            ("Vochtige lucht stijgt tegen een gebergte op.", "Stuwingsregen"),
            ("Warme lucht stijgt boven een opgewarmd land op een zomerse namiddag.", "Convectieregen"),
            ("Warme lucht schuift over koude lucht bij een front.", "Frontale regen"),
        ],
        "Lucht koelt af bij het stijgen, waterdamp condenseert en er vormen wolken. De oorzaak van het stijgen bepaalt het soort neerslag.",
        kolommen=["Stuwingsregen", "Convectieregen", "Frontale regen"]),

    # Klimaten en zeestromen
    mk("Waarom heeft West-Europa zachtere winters dan Canada op dezelfde breedte?",
       ["Door de warme Golfstroom en de westenwinden van over zee.", "Doordat West-Europa dichter bij de evenaar ligt dan Canada.", "Door de hoge bergen die de koude lucht uit het noorden houden.", "Doordat de zon in West-Europa elke dag langer schijnt."],
       0,
       "De Golfstroom en de Noord-Atlantische Drift brengen warm water mee. De westenwinden voeren die zachte zeelucht aan land."),
    koppel(
        "Koppel het bioom aan het klimaat.",
        [
            ["tropisch regenwoud", "het hele jaar warm en nat"],
            ["savanne", "warm met een natte en een droge tijd"],
            ["taiga", "lange koude winters, korte zomers"],
            ["toendra", "zeer koud, bevroren ondergrond"],
        ],
        ["mediterraan, met zachte winters"],
        "De temperatuur en de neerslag over het jaar bepalen welke vegetatie groeit."),

    # Geologie
    tabel(
        "Welk soort plaatgrens?",
        [
            ("Midden-Atlantische Rug", "Divergent"),
            ("Andesgebergte", "Convergent"),
            ("San Andreasbreuk", "Transform"),
            ("Himalaya", "Convergent"),
        ],
        "Bij een divergente grens schuiven platen uit elkaar, bij een convergente botsen ze, en bij een transformbreuk schuiven ze langs elkaar.",
        kolommen=["Divergent", "Convergent", "Transform"]),
    keuze(
        "Langs een subductiezone vind je vaak [[*explosieve stratovulkanen|vlakke schildvulkanen]] en [[*zware aardbevingen|helemaal geen aardbevingen]].",
        "Bij subductie ontstaat taai, gasrijk magma: explosieve vulkanen. De wrijving tussen de platen veroorzaakt aardbevingen."),
    sorteer(
        "Is dit een stollingsgesteente, een afzettingsgesteente of een metamorf gesteente?",
        ["Stollingsgesteente", "Afzettingsgesteente", "Metamorf gesteente"],
        [
            ["graniet", "Stollingsgesteente"],
            ["zandsteen", "Afzettingsgesteente"],
            ["marmer", "Metamorf gesteente"],
            ["basalt", "Stollingsgesteente"],
            ["kalksteen", "Afzettingsgesteente"],
            ["leisteen", "Metamorf gesteente"],
        ],
        "Stollingsgesteenten komen uit magma, afzettingsgesteenten uit lagen sediment, metamorfe gesteenten ontstaan door druk en hitte."),
    mk("Welke vorm van verwering zie je als water in een rotsspleet bevriest en de rots openbreekt?",
       ["Vorstverwering", "Chemische verwering", "Biologische verwering", "Wortelverwering"],
       0,
       "Water zet uit als het bevriest. Telkens opnieuw vriezen en dooien wrikt de rots open: mechanische vorstverwering."),

    # Erosie
    tabel(
        "Door welk proces ontstond deze landvorm?",
        [
            ("U-vormig dal", "Gletsjer"),
            ("V-vormig dal", "Rivier"),
            ("Zandduinen", "Wind"),
            ("Delta", "Rivier"),
        ],
        "Gletsjers schuren brede U-dalen uit, rivieren snijden V-dalen in en zetten aan de monding sediment af, wind stapelt zand op tot duinen.",
        kolommen=["Rivier", "Gletsjer", "Wind"]),

    # Klimaatverandering
    tabel(
        "Klopt dit over de huidige klimaatverandering?",
        [
            ("CO₂ uit fossiele brandstoffen versterkt het broeikaseffect.", J),
            ("Smeltend landijs doet de zeespiegel stijgen.", J),
            ("Het broeikaseffect is op zich schadelijk en zou volledig moeten verdwijnen.", F),
            ("Een gat in de ozonlaag is de hoofdoorzaak van de opwarming.", F),
        ],
        "Zonder natuurlijk broeikaseffect zou de aarde ijskoud zijn. Het probleem is de versterking door extra broeikasgassen. De ozonlaag is een ander verhaal."),
    sorteer(
        "Is dit mitigatie of adaptatie?",
        ["Mitigatie", "Adaptatie"],
        [
            ["Zonnepanelen plaatsen", "Mitigatie"],
            ["Dijken verhogen", "Adaptatie"],
            ["Minder vlees eten", "Mitigatie"],
            ["Meer groen in de stad tegen hitte", "Adaptatie"],
        ],
        "Mitigatie beperkt de uitstoot van broeikasgassen. Adaptatie past de samenleving aan de gevolgen aan."),

    # Ruimte en landschap
    keuze(
        "Als mensen uit de stad naar dorpen in de rand verhuizen, spreek je van [[*suburbanisatie|urbanisatie|reürbanisatie]]. Dat leidt vaak tot meer [[*pendelverkeer|landbouwgrond|open ruimte]].",
        "Bij suburbanisatie wonen mensen buiten de stad maar werken ze er nog vaak. Dat zorgt voor meer verkeer en verharding."),
    mk("Wat is een gevolg van veel verharde oppervlakte in Vlaanderen?",
       ["Regenwater dringt minder in de bodem: meer kans op wateroverlast.", "Het grondwaterpeil stijgt elk jaar omdat er meer regen in de bodem zakt.", "Er komen vanzelf meer bossen bij omdat de grond beter beschermd is.", "De temperatuur in steden daalt omdat stenen de warmte wegnemen."],
       0,
       "Beton en asfalt laten geen water door. Het water loopt snel af naar de riolering en de rivieren, terwijl het grondwater minder wordt aangevuld."),
    tabel(
        "Is dit een natuurlijk of een cultuurlandschapselement?",
        [
            ("Een kanaal", "Cultuur"),
            ("Een rivierduin", "Natuurlijk"),
            ("Een bomenrij langs een akker", "Cultuur"),
            ("Een moeras", "Natuurlijk"),
        ],
        "Cultuurelementen zijn door de mens gemaakt of gevormd. Natuurlijke elementen ontstonden zonder ingreep van de mens.",
        kolommen=["Natuurlijk", "Cultuur"]),

    # Gemengd
    inv("Op een kaart met schaal 1 : 50 000 meet je 6 cm. Hoeveel kilometer is dat in werkelijkheid? Enkel het getal.",
        ["3"],
        "6 · 50 000 = 300 000 cm = 3000 m = 3 km."),
    keuze(
        "De maan draait in ongeveer [[*een maand|een dag|een jaar]] rond de aarde. Bij volle maan staat de maan [[*aan de andere kant van de aarde dan de zon|tussen de aarde en de zon]].",
        "Bij volle maan zien we de volledig verlichte kant. Staat de maan tussen aarde en zon, dan is het nieuwe maan."),
    mk("Waarom komen er in IJsland veel vulkanen voor?",
       ["Het ligt op de Midden-Atlantische Rug, waar platen uiteenwijken.", "IJsland ligt op een subductiezone waar twee oceaanplaten botsen.", "IJsland ligt midden op een grote plaat, ver van elke plaatgrens.", "IJsland ligt langs een transformbreuk zoals de San Andreasbreuk."],
       0,
       "IJsland ligt op een divergente plaatgrens (en een hotspot). Daar stijgt magma op tussen de uiteenwijkende platen."),

    tabel(
        "In welk era van de geologische tijdschaal hoort dit?",
        [
            ("De dinosaurussen leven op aarde.", "Mesozoïcum"),
            ("De ijstijden en de eerste mensen", "Cenozoïcum"),
            ("De eerste vissen en landplanten", "Paleozoïcum"),
        ],
        "Het Paleozoïcum is het oudste van de drie, daarna volgt het Mesozoïcum van de dinosaurussen, en we leven nu in het Cenozoïcum.",
        kolommen=["Paleozoïcum", "Mesozoïcum", "Cenozoïcum"]),
    keuze(
        "Een getijde ontstaat vooral door de aantrekkingskracht van de [[*maan|zon alleen|wind]]. Er zijn per dag ongeveer [[*twee|één|vier]] keer hoogwater.",
        "De maan trekt het water aan aan de kant die naar haar toe ligt; aan de andere kant ontstaat ook een waterbult. Zo zijn er twee vloeden per dag."),
    inv("Op een weerkaart liggen de isobaren van 1000 hPa en 1020 hPa 400 km uit elkaar. Hoeveel hPa daalt de luchtdruk per 100 km?",
        ["5"],
        "20 hPa over 400 km is 5 hPa per 100 km."),
    mk("Wat verklaart dat het in Gabon, op de evenaar, het hele jaar warm is?",
       ["De zonnestralen vallen er altijd bijna loodrecht in.", "De evenaar ligt het dichtst bij de zon van alle plaatsen.", "Er waait aan de evenaar het hele jaar door een warme wind.", "Aan de evenaar zijn de nachten veel korter dan de dagen."],
       0,
       "Bij een loodrechte inval valt de zonne-energie op een kleine oppervlakte. Dag en nacht zijn er ongeveer even lang."),
    sorteer(
        "Hoort dit bij een hogedrukgebied of bij een lagedrukgebied?",
        ["Hogedrukgebied", "Lagedrukgebied"],
        [
            ["Dalende lucht en weinig wolken", "Hogedrukgebied"],
            ["Stijgende lucht en neerslag", "Lagedrukgebied"],
            ["Op het noordelijk halfrond draait de wind wijzerzin rond", "Hogedrukgebied"],
            ["Fronten met warme en koude lucht", "Lagedrukgebied"],
        ],
        "In een hogedrukgebied daalt de lucht en lossen wolken op. In een lagedrukgebied stijgt de lucht en ontstaan wolken en fronten."),

    # Schrijfopdracht
    open_("Je gemeente wil een nieuwe verkaveling bouwen op een overstromingsgevoelige weide naast een beek. Schrijf in 4 à 6 zinnen een advies: welke risico's zie je en welke alternatieven stel je voor?",
          "Op een overstromingsgevoelige weide lopen de huizen kans op wateroverlast. Door de verharding kan het regenwater ook minder in de bodem, wat de overstromingen stroomafwaarts erger maakt. De weide is nu een natuurlijke buffer die water opvangt. Ik stel voor om eerder in het centrum te verdichten of leegstaande gebouwen te renoveren. Wil men toch bouwen, dan moet er een wadi of waterbuffer bij en zo weinig mogelijk verharding.",
          "Een goed antwoord noemt het overstromingsrisico en het gevolg van verharding, ziet de weide als waterbuffer, en stelt een alternatief voor zoals verdichting in de kern, hergebruik van gebouwen of waterbuffering."),
]

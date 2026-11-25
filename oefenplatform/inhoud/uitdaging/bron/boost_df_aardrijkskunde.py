# -*- coding: utf-8 -*-
"""Uitdaging Aardrijkskunde 🚀 Boost dubbele finaliteit (25 november 2026), in
de vormen van het examen van de Examencommissie: 40 vragen die alle
hoofdstukken door elkaar halen, van situeren en bevolking tot mondialisering,
duurzaamheid en het versterkte broeikaseffect. Een kaart van een verzonnen
gemeente en zes verzonnen krantenkoppen om op te klikken, tabellen,
keuzelijsten, slepen, koppelen, sorteren, volgorde, een casus en een open
vraag. Geen nieuwe leerstof: alles staat in de hoofdstukken van dit vak.
De prenten tekent inhoud/uitdaging/maak_prenten_boost_df_aardrijkskunde.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-dubbele-finaliteit"
VAK = "Aardrijkskunde"
BESTAND = "boost-df-aardrijkskunde-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/aardrijkskunde-boost-df-uitdaging"
KAART = "kaart-gemeente.svg"
KOPPEN = "zes-krantenkoppen.svg"
# klikvakken: zie maak_prenten_boost_df_aardrijkskunde.py
G = {1: [40.0, 34.5, 21.0, 18.4], 2: [9.0, 14.5, 25.0, 19.7], 3: [36.0, 59.9, 30.0, 10.5],
     4: [77.0, 39.5, 17.0, 18.4], 5: [9.0, 52.6, 19.0, 14.5], 6: [43.0, 13.2, 25.0, 15.8]}
K = {1: [2, 13.4, 96, 13.7], 2: [2, 27.1, 96, 13.7], 3: [2, 40.8, 96, 13.7],
     4: [2, 54.5, 96, 13.7], 5: [2, 68.2, 96, 13.7], 6: [2, 81.8, 96, 13.7]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Kaart van de gemeente
    klik("Bekijk de kaart van de gemeente. Na een week zware regen treedt de rivier buiten haar oevers. Klik op het gebied dat het eerst onder water loopt.",
         KAART, [G[3]],
         "Gebied 3 is laag weiland vlak langs de rivier. Bij hoog water loopt dat het eerst onder. Daarom bouw je daar beter niet."),
    klik("Een webwinkel zoekt in deze gemeente een plaats voor een groot distributiecentrum. Klik op het gebied dat het best past.",
         KAART, [G[4]],
         "Een distributiecentrum zoekt goedkope grond en een goede aansluiting op het wegennet. Gebied 4 ligt naast de afrit van de snelweg en buiten het centrum."),
    klik("Op welk gebied moet de bodem waarschijnlijk eerst gesaneerd worden voor er woningen kunnen komen? Klik erop.",
         KAART, [G[5]],
         "Op een oude fabriekssite zit vaak vervuiling in de bodem. Die verdwijnt niet vanzelf: eerst saneren, dan pas opnieuw bouwen."),
    klik("Klik op het gebied waar de open ruimte het laatst verloren ging aan bebouwing.",
         KAART, [G[2]],
         "Gebied 2 is een nieuwe verkaveling op vroeger akkerland. Zo groeit de bebouwing het platteland in en verdwijnt open ruimte."),
    met_prent(KAART, tabel(
        "De gemeente wil 200 nieuwe woningen. Welke keuze is het duurzaamst? Kijk naar de kaart.",
        [
            ("Woningen bouwen op de gesaneerde fabriekssite 5 spaart open ruimte.", J),
            ("Woningen bouwen in gebied 3 is veilig, want het ligt dicht bij de rivier.", F),
            ("Het bos in gebied 6 kappen voor woningen helpt de biodiversiteit.", F),
        ],
        "Een oude site hergebruiken spaart akkerland en natuur. Het weiland langs de rivier loopt onder bij hoog water, en een bos kappen schaadt de biodiversiteit.")),

    # Krantenkoppen
    klik("Bekijk de zes krantenkoppen. Klik op de kop die over de-industrialisatie gaat.",
         KOPPEN, [K[1]],
         "De-industrialisatie is het verdwijnen van de industrie uit een streek: de mijnen sluiten, daarna de fabrieken, en de banen gaan verloren."),
    klik("Klik op de kop die een voorbeeld van landgrabbing geeft.",
         KOPPEN, [K[2]],
         "Landgrabbing is het opkopen of langdurig huren van grote stukken landbouwgrond in een ander land."),
    klik("Klik op de kop die braindrain beschrijft.",
         KOPPEN, [K[4]],
         "Bij braindrain trekken hoogopgeleide mensen weg uit hun land. Het land van vertrek verliest kennis en vakmensen, zoals hier artsen."),
    klik("Klik op de kop die over ontvolking gaat.",
         KOPPEN, [K[5]],
         "Ontvolking is het leeglopen van een streek: werk en voorzieningen verdwijnen en de inwoners trekken weg."),
    met_prent(KOPPEN, keuze(
        "Kop 3 toont de [[*versnippering|verharding|ontvolking]] van de open ruimte. Kop 6 hoort bij de [[*mondialisering|de-industrialisatie]], want de container maakt zeetransport goedkoop.",
        "Een weg die een bos in twee stukken snijdt, versnippert de open ruimte. Containers uit Azië tonen de wereldwijde handel.")),

    # Situeren en kaarten
    tabel(
        "Absoluut of relatief gesitueerd?",
        [
            ("Antwerpen ligt op 51° NB en 4° OL.", "absoluut"),
            ("De haven ligt ten noorden van de stad.", "relatief"),
            ("Het dorp ligt aan de kust, vlak bij de grens.", "relatief"),
        ],
        "Absoluut situeren doe je met geografische coördinaten. Relatief situeren doe je ten opzichte van iets anders.",
        kolommen=["absoluut", "relatief"]),
    mk("Twee vrienden tekenen elk uit het hoofd hun weg naar school. De kaarten verschillen sterk. Wat hebben ze getekend?",
       ["Elk een mentale kaart, gekleurd door wat ze zelf beleven",
        "Elk een thematische kaart met een eigen legende en schaal",
        "Elk een topografische kaart met de juiste afstanden erop",
        "Elk een digitale kaart met andere lagen die ze hebben aangezet"],
       0,
       "Een mentale kaart is het beeld van een gebied in je hoofd. Ze hangt af van je persoonlijke context en klopt dus niet precies."),
    keuze(
        "De nulmeridiaan loopt door [[*Greenwich|Parijs|Brussel]]. Plaatsen op dezelfde meridiaan hebben op hetzelfde moment dezelfde [[*zonnetijd|breedteligging]].",
        "De meridiaan van 0° loopt door Greenwich bij Londen. Op één meridiaan staat de zon op hetzelfde moment even hoog."),

    # Bevolking
    inv("Een land heeft een geboortecijfer van 21 ‰ en een sterftecijfer van 8 ‰. Hoe groot is de natuurlijke aangroei in ‰? Een getal.",
        ["13"],
        "Natuurlijke aangroei = geboortecijfer min sterftecijfer: \\(21 - 8 = 13\\) ‰."),
    inv("Een provincie van 2 500 km² telt 1 000 000 inwoners. Hoeveel inwoners per km² is de bevolkingsdichtheid? Een getal.",
        ["400"],
        "Bevolkingsdichtheid = aantal inwoners gedeeld door de oppervlakte: \\(1\\,000\\,000 : 2\\,500 = 400\\) inwoners per km²."),
    sorteer(
        "Is dit een pushfactor of een pullfactor voor iemand die migreert?",
        ["pushfactor", "pullfactor"],
        [
            ["oorlog in het eigen land", "pushfactor"],
            ["werk en hogere lonen in het nieuwe land", "pullfactor"],
            ["langdurige droogte die de oogst vernielt", "pushfactor"],
            ["familie die al in het nieuwe land woont", "pullfactor"],
        ],
        "Een pushfactor duwt mensen weg uit hun streek. Een pullfactor trekt hen aan naar een nieuwe plaats."),
    tabel(
        "Een land vergrijst sterk. Klopt dit gevolg?",
        [
            ("Er zijn meer pensioenen te betalen.", J),
            ("Er is meer nood aan zorg voor ouderen.", J),
            ("Er komen vanzelf meer jonge werkkrachten bij.", F),
        ],
        "Bij vergrijzing stijgt het aandeel ouderen. De kosten voor pensioenen en zorg stijgen, terwijl er relatief minder mensen werken."),
    mk("In een land daalt het sterftecijfer snel door betere zorg, maar het geboortecijfer blijft hoog. Wat gebeurt er?",
       ["De bevolking groeit snel aan",
        "De bevolking blijft ongeveer even groot als voordien",
        "De bevolking krimpt, want er sterven nog altijd te veel mensen",
        "De bevolking vergrijst snel, want ouderen leven langer"],
       0,
       "Als er veel meer mensen geboren worden dan er sterven, is de natuurlijke aangroei groot en groeit de bevolking snel."),

    tabel(
        "Is dit een fysische of een sociaaleconomische factor bij de keuze waar mensen wonen?",
        [
            ("het klimaat", "fysisch"),
            ("werkgelegenheid", "sociaaleconomisch"),
            ("de vruchtbaarheid van de bodem", "fysisch"),
            ("scholen en ziekenhuizen in de buurt", "sociaaleconomisch"),
        ],
        "Fysische factoren komen uit de natuur: klimaat, bodem, reliëf, water. Sociaaleconomische factoren komen van de mens: werk, voorzieningen, welvaart.",
        kolommen=["fysisch", "sociaaleconomisch"]),
    keuze(
        "Als de welvaart in een land stijgt, daalt het geboortecijfer meestal. Kinderen gaan langer naar [[*school|het werk]] en ouders hebben voor hun oude dag minder kinderen [[*nodig|over]].",
        "Met meer welvaart gaan kinderen langer naar school en zorgt het pensioen voor de oude dag. Gezinnen worden kleiner."),
    sleep(
        "Planten halen bij [[fotosynthese]] koolstof uit de lucht. Steenkool, aardolie en aardgas zijn [[fossiele]] brandstoffen: koolstof die miljoenen jaren geleden uit de lucht werd gehaald.",
        ["verbranding", "hernieuwbare"],
        "Fotosynthese slaat koolstof op in planten. Bij het verbranden van fossiele brandstoffen komt die koolstof als CO₂ terug in de atmosfeer."),

    # Stad en platteland
    koppel(
        "Koppel het begrip aan de juiste omschrijving.",
        [
            ["sociale segregatie", "groepen wonen gescheiden in andere wijken van de stad"],
            ["verharding", "de bodem wordt bedekt met beton, asfalt en daken"],
            ["functiewijziging", "een gebouw of wijk krijgt een ander gebruik"],
        ],
        ["de open ruimte valt uiteen in kleine stukken"],
        "Segregatie gaat over wie waar woont. Verharding houdt regenwater tegen. Bij een functiewijziging wordt bijvoorbeeld een fabriek een woonblok."),
    mk("Een gemeente breekt een betonnen plein open en plant er bomen. Wat lost ze daarmee niet op?",
       ["Het tekort aan woningen in het centrum",
        "Regenwater dat niet meer in de bodem kan dringen",
        "De hitte die blijft hangen tussen beton en steen",
        "Het gebrek aan groen en aan schaduw op het plein"],
       0,
       "Ontharden laat water weer in de bodem lopen en geeft groen, schaduw en verkoeling. Woningen bouwt het niet."),

    # Grondstoffen en industrie
    sorteer(
        "Is dit een hernieuwbare of een niet-hernieuwbare energiebron?",
        ["hernieuwbaar", "niet-hernieuwbaar"],
        [
            ["windenergie", "hernieuwbaar"],
            ["aardgas", "niet-hernieuwbaar"],
            ["zonne-energie", "hernieuwbaar"],
            ["steenkool", "niet-hernieuwbaar"],
            ["waterkracht", "hernieuwbaar"],
        ],
        "Wind, zon en water raken niet op. Steenkool en aardgas zijn fossiele brandstoffen die miljoenen jaren nodig hadden om te ontstaan."),
    keuze(
        "Vroeger lag de zware industrie vlak bij de [[*steenkoolmijnen|toeristische kusten]]. Vandaag zoekt industrie vooral goedkope grond en een goede aansluiting op het [[*wegennet|platteland]].",
        "Steenkool was zwaar en duur om te vervoeren, dus bouwde men de fabrieken ernaast. Nu telt vooral de bereikbaarheid."),

    # Landbouw, handel en toerisme
    tabel(
        "Intensieve of extensieve landbouw?",
        [
            ("Veel kunstmest en machines op een klein stuk grond", "intensief"),
            ("Grote kudde die vrij graast op uitgestrekte weiden", "extensief"),
            ("Serres met verwarming en bewatering", "intensief"),
        ],
        "Intensieve landbouw haalt met veel middelen veel op per hectare. Extensieve landbouw gebruikt veel grond met weinig middelen.",
        kolommen=["intensief", "extensief"]),
    sleep(
        "Een winkel die rechtstreeks aan de consument verkoopt, hoort bij de [[kleinhandel]]. Wie in grote hoeveelheden aan winkels levert, doet aan [[groothandel]]. Handel en toerisme horen samen bij de [[dienstensector]].",
        ["landbouwsector", "industrie"],
        "Kleinhandel verkoopt aan de consument, groothandel aan andere bedrijven. Handel, toerisme en vervoer maken niets, ze verlenen diensten."),

    # Mondialisering
    koppel(
        "Koppel de organisatie aan wat ze vooral doet.",
        [
            ["NAVO", "militair bondgenootschap"],
            ["Verenigde Naties", "vrede en samenwerking tussen bijna alle landen"],
            ["Mercosur", "handelsblok van landen in Zuid-Amerika"],
        ],
        ["munt van de Europese landen"],
        "De NAVO is militair, de VN werkt aan vrede en samenwerking, Mercosur is een handelsblok in Zuid-Amerika."),
    tabel(
        "Klopt dit over mondialisering?",
        [
            ("Landen worden er meer afhankelijk van elkaar door.", J),
            ("Ze heeft voor elk land dezelfde gevolgen.", F),
            ("Ook gewone mensen doen eraan mee, via reizen en sociale media.", J),
            ("De container maakte zeetransport veel duurder.", F),
        ],
        "Mondialisering verbindt landen, bedrijven en mensen. De gevolgen verschillen per land en groep. De container maakte transport juist goedkoper."),

    # Duurzaamheid
    koppel(
        "Koppel de P van duurzame ontwikkeling aan een voorbeeld.",
        [
            ["Planet", "een bos beschermen tegen bebouwing"],
            ["People", "iedereen toegang geven tot onderwijs en zorg"],
            ["Prosperity", "eerlijk werk met een goed loon"],
            ["Partnership", "landen werken samen aan de doelen"],
        ],
        [],
        "De vijf P's zijn People, Planet, Prosperity, Peace en Partnership. Samen vormen ze de basis van de duurzame ontwikkelingsdoelen."),
    mk("Iemand rijdt elke dag ver met de auto, vliegt vaak en eet veel vlees. Wat zegt dat over die persoon?",
       ["Die heeft een grote ecologische voetafdruk",
        "Die heeft een kleine ecologische voetafdruk, want vlees is natuurlijk",
        "Die heeft geen invloed op het milieu, want het is maar één persoon",
        "Die haalt de duurzame ontwikkelingsdoelen al in zijn eentje"],
       0,
       "De ecologische voetafdruk is de oppervlakte aarde die nodig is voor iemands verbruik en afval. Veel rijden, vliegen en vlees vergroten die."),

    # Broeikaseffect
    volgorde(
        "Zet de stappen in de juiste volgorde: hoe draagt een gekapt en verbrand bos bij aan de opwarming?",
        ["Het bos wordt gekapt en verbrand.",
         "De koolstof uit het hout komt als CO₂ in de atmosfeer.",
         "Er zit meer broeikasgas in de lucht.",
         "De atmosfeer houdt meer warmte vast."],
        "Bij verbranding gaat de opgeslagen koolstof naar de atmosfeer. Meer CO₂ versterkt het broeikaseffect."),
    sorteer(
        "In welke sfeer zit dit?",
        ["atmosfeer", "hydrosfeer", "biosfeer"],
        [
            ["CO₂ in de lucht", "atmosfeer"],
            ["water in de oceanen", "hydrosfeer"],
            ["een bos", "biosfeer"],
            ["ijs op de polen", "hydrosfeer"],
        ],
        "De atmosfeer is de lucht, de hydrosfeer al het water en ijs, de biosfeer alles wat leeft."),
    tabel(
        "Gevolg van het versterkte broeikaseffect?",
        [
            ("De zeespiegel stijgt.", J),
            ("De klimaatzones schuiven naar de polen.", J),
            ("Het natuurlijke broeikaseffect verdwijnt.", F),
            ("Er komen vaker hittegolven en droogte.", J),
        ],
        "Door de opwarming smelt ijs en zet zeewater uit. Klimaatzones schuiven poolwaarts. Het natuurlijke broeikaseffect blijft bestaan: zonder zou het ijskoud zijn."),
    mk("Smeltend ijs laat de aarde nog sneller opwarmen, waardoor nog meer ijs smelt. Hoe noem je dat?",
       ["Een terugkoppeling in het klimaatsysteem",
        "Het natuurlijke broeikaseffect van de aarde",
        "De koolstofkringloop tussen de vier sferen",
        "Een verschuiving van de klimaatzones naar de evenaar"],
       0,
       "Bij een terugkoppeling versterkt een gevolg zijn eigen oorzaak. Zo gaat de opwarming steeds sneller."),

    # Onderzoek
    volgorde(
        "Zet de stappen van een geografisch onderzoek in de juiste volgorde.",
        ["Een onderzoeksvraag stellen",
         "Een hypothese opschrijven",
         "Gegevens verzamelen met kaarten en terreinwerk",
         "Een besluit trekken en de hypothese toetsen"],
        "Je begint met een vraag en een verwachting, verzamelt gegevens en toetst daarna je hypothese."),
    keuze(
        "In Geopunt bepaal je wat je ziet door [[*lagen|kleuren]] aan of uit te zetten. Welke kleur of welk symbool wat betekent, lees je in de [[*legende|schaal]].",
        "Op een digitale kaart kies je zelf de lagen. De legende verklaart de kleuren en symbolen."),

    casus(
        "Een gemeente aan een rivier groeit snel. Op twintig jaar tijd verdween een derde van het akkerland onder nieuwe verkavelingen en parkings. Bij elke zware onweersbui lopen nu kelders onder in de lage wijken.",
        [
            mk("Wat is de belangrijkste oorzaak van de wateroverlast?",
               ["Door de verharding kan regenwater niet meer in de bodem dringen",
                "De rivier is door de opwarming in twintig jaar veel breder geworden",
                "Akkerland houdt minder water vast dan beton en asfalt doen",
                "Er wonen meer mensen, en die gebruiken samen meer water in huis"],
               0,
               "Beton, asfalt en daken laten geen water door. Het regenwater stroomt meteen naar de lage delen en de riolen."),
            mk("Welke maatregel helpt het meest?",
               ["Verharde stukken ontharden en ruimte geven aan water",
                "Nog meer parkings bouwen zodat auto's hoger kunnen staan",
                "Alle akkers die overblijven ook verkavelen en volbouwen",
                "De riolen dichtmaken zodat het water niet kan terugkomen"],
               0,
               "Ontharden en ruimte voor water laat regen weer in de bodem lopen en vermindert de overlast."),
        ]),

    open_("Kies uit de kaart van de gemeente één plaats voor een nieuw zwembad. Leg uit waarom die plaats past, met minstens twee argumenten: één over de ligging en één over duurzaamheid.",
          "Ik kies gebied 5, de oude fabriekssite. De plaats ligt dicht bij het centrum, zodat veel mensen te voet of met de fiets kunnen komen. Na sanering hergebruik je een oude site, zodat je geen akkerland of bos opoffert.",
          "Een goed antwoord kiest een plaats op de kaart, geeft een argument over de ligging (bereikbaarheid, overstromingsgevaar) en een over duurzaamheid (open ruimte sparen, hergebruik)."),
]

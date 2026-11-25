# -*- coding: utf-8 -*-
"""Uitdaging Biologie 🚀 Boost doorstroom (25 november 2026), in de vormen van
het examen van de Examencommissie: 40 vragen die alle hoofdstukken door elkaar
halen. Een energiepiramide en de weg van een reflex om op te klikken, tabellen,
keuzelijsten, slepen, koppelen, sorteren, volgorde, rekenvragen en een korte
schrijfopdracht. Geen nieuwe leerstof: alles staat in de hoofdstukken van
Biologie Boost doorstroom. De prenten tekent
inhoud/uitdaging/maak_prenten_boost_biologie.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "boost-doorstroom"
VAK = "Biologie"
BESTAND = "boost-biologie-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/biologie-boost-uitdaging"
PIR = "energiepiramide.svg"
REF = "reflexboog.svg"

# klikvakken uit maak_prenten_boost_biologie.py
NIV = {"eikenbladeren": [7.0, 71.0, 86.0, 16.1], "rupsen": [18.0, 53.2, 64.0, 16.1],
       "mezen": [29.0, 35.5, 42.0, 16.1], "sperwer": [40.0, 17.7, 20.0, 16.1]}
VAK_R = {1: [3.0, 31.0, 16.8, 45.2], 2: [22.8, 31.0, 16.8, 45.2], 3: [42.6, 31.0, 16.8, 45.2],
         4: [62.4, 31.0, 16.8, 45.2], 5: [82.2, 31.0, 16.8, 45.2]}


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Energiepiramide (prent)
    klik("Bekijk de energiepiramide van het eikenbos. Klik op het niveau van de producenten.",
         PIR, [NIV["eikenbladeren"]],
         "De eik maakt met fotosynthese zelf zijn voedsel uit licht, water en koolstofdioxide. Hij is autotroof en dus producent."),
    klik("Klik op het niveau van de consumenten van de tweede orde.",
         PIR, [NIV["mezen"]],
         "Rupsen eten bladeren en zijn consumenten van de eerste orde. Mezen eten rupsen en zijn dus consumenten van de tweede orde."),
    klik("Een giftige stof die niet wordt afgebroken, komt in de eikenbladeren terecht. Klik op het niveau waar die stof zich het sterkst ophoopt.",
         PIR, [NIV["sperwer"]],
         "Zo'n stof hoopt zich op naar de top van de voedselketen: elk dier eet veel prooien en houdt het gif telkens vast."),
    met_prent(PIR, inv(
        "De eikenbladeren bevatten 50 000 kJ energie. Ongeveer een tiende gaat telkens naar het volgende niveau. Hoeveel kJ bereikt de sperwer? Enkel het getal.",
        ["50"],
        "50 000 → 5000 (rupsen) → 500 (mezen) → 50 kJ (sperwer).")),
    met_prent(PIR, keuze(
        "De piramide wordt naar boven [[*smaller|breder]], omdat elk niveau een groot deel van de energie [[*verliest als warmte bij de celademhaling|doorgeeft aan de producenten]].",
        "Organismen gebruiken het grootste deel van hun energie zelf. Die energie verdwijnt als warmte en gaat niet naar het volgende niveau.")),

    # Reflex (prent)
    klik("Bekijk de weg van de reflex. Klik op het vak waar de prikkel wordt omgezet in een impuls.",
         REF, [VAK_R[1]],
         "Een receptor vangt de prikkel op (hier warmte) en zet die om in een impuls."),
    klik("Klik op het vak dat de effector is.",
         REF, [VAK_R[5]],
         "De effector voert de reactie uit. Hier trekt de spier de arm weg van de hete pan."),
    klik("Klik op het vak waar de impuls omschakelt zonder eerst langs de grote hersenen te gaan.",
         REF, [VAK_R[3]],
         "Bij een reflex loopt de korte weg via het ruggemerg. Daardoor trek je je hand weg nog voor je de pijn bewust voelt."),
    met_prent(REF, tabel(
        "Klopt dit over de reflex op de prent?",
        [
            ("Vak 2 voert impulsen naar het centrale zenuwstelsel toe.", J),
            ("Vak 4 voert impulsen van het centrale zenuwstelsel naar de spier.", J),
            ("Met wat oefening kan je deze reflex altijd onderdrukken.", F),
            ("De impuls springt in een synaps over van het ene neuron naar het volgende.", J),
        ],
        "Sensorische zenuwen gaan naar het centrale zenuwstelsel, motorische zenuwen ervan weg. Een reflex is snel en onbewust.")),

    # Planten
    tabel(
        "Wat vervoert dit vatenweefsel?",
        [
            ("Water met opgeloste mineralen, van de wortel naar het blad", "Xyleem"),
            ("Suikers uit de fotosynthese, naar alle delen van de plant", "Floëem"),
            ("Het vocht dat opstijgt door worteldruk en zuigkracht", "Xyleem"),
        ],
        "Het xyleem of de houtvaten vervoeren water en mineralen. Het floëem of de zeefvaten vervoeren de assimilaten.",
        kolommen=["Xyleem", "Floëem"]),
    keuze(
        "Bij droogte maakt een plant het hormoon [[*abscisinezuur|auxine|ethyleen]] aan. Daardoor gaan de huidmondjes [[*dicht|verder open]] en verliest ze minder water.",
        "Abscisinezuur laat de sluitcellen de huidmondjes sluiten. Auxine zorgt voor celstrekking, ethyleen voor het rijpen van vruchten."),
    mk("Een stengel buigt naar het raam toe. Hoe verklaar je dat?",
       ["Aan de schaduwkant strekken de cellen zich meer door auxine.", "Aan de lichtkant groeien de cellen sneller dan aan de schaduwkant.", "De plant trekt zich met haar wortels naar het licht toe.", "De huidmondjes aan de lichtkant sluiten zich plots."],
       0,
       "Auxine verzamelt zich aan de schaduwkant. Daar strekken de cellen zich meer, zodat de stengel naar het licht buigt. Dat is een tropie."),

    # Zenuwstelsel
    koppel(
        "Koppel het deel van de hersenen aan zijn taak.",
        [
            ["grote hersenen", "bewust denken, plannen en leren"],
            ["kleine hersenen", "bewegingen en evenwicht afstemmen"],
            ["hersenstam", "ademhaling en hartslag regelen"],
        ],
        ["licht omzetten in impulsen"],
        "Licht omzetten in impulsen gebeurt in het netvlies van het oog, niet in de hersenen."),
    keuze(
        "De korte uitlopers van een neuron die signalen opvangen, heten [[*dendrieten|axonen]]. De [[*myelineschede|synaps]] rond het axon laat de impuls sneller lopen.",
        "Dendrieten vangen op, het axon geeft door. De myelineschede isoleert het axon en de impuls springt van insnoering naar insnoering."),

    # Oog en oor
    volgorde(
        "Zet de weg van het licht door het oog in de juiste volgorde.",
        ["hoornvlies", "pupil", "lens", "glasachtig lichaam", "netvlies"],
        "Het licht gaat door het hoornvlies, de pupil en de lens, dan door het glasachtig lichaam tot op het netvlies."),
    tabel(
        "Welk soort lichtgevoelige cel in het netvlies past bij deze beschrijving?",
        [
            ("Laten je kleuren zien", "Kegeltjes"),
            ("Werken vooral in het halfduister", "Staafjes"),
            ("Liggen dicht opeen in de gele vlek", "Kegeltjes"),
        ],
        "Kegeltjes zien kleur en scherp detail, vooral in de gele vlek. Staafjes zijn erg lichtgevoelig maar zien geen kleur.",
        kolommen=["Staafjes", "Kegeltjes"]),
    mk("Iemand ziet ver weg wazig maar dichtbij scherp. Welke bril helpt?",
       ["Een bril met holle lenzen", "Een bril met bolle lenzen", "Een bril met gekleurde glazen", "Een bril met vlakke glazen"],
       0,
       "Dat is bijziendheid: het beeld valt vóór het netvlies. Een holle lens spreidt het licht, zodat het beeld verder naar achteren valt."),
    volgorde(
        "Zet de weg van het geluid in het oor in de juiste volgorde.",
        ["oorschelp", "gehoorgang", "trommelvel", "gehoorbeentjes", "slakkenhuis"],
        "De oorschelp vangt het geluid op, de gehoorgang leidt het naar het trommelvel, de gehoorbeentjes versterken de trilling en in het slakkenhuis zetten haarcellen ze om."),
    keuze(
        "Na lang ronddraaien en plots stoppen blijf je duizelig. De vloeistof in de [[*halfcirkelvormige kanaaltjes|gehoorgang|buis van Eustachius]] blijft door haar [[*traagheid|kleur]] nog even doorstromen.",
        "De vloeistof beweegt nog even na en de haarcellen melden een draai, terwijl je stilstaat."),

    # Spieren en klieren
    sorteer(
        "Laat dit het bloedglucosegehalte stijgen of dalen?",
        ["Stijgen", "Dalen"],
        [
            ["glucagon uit de alfacellen", "Stijgen"],
            ["insuline uit de bètacellen", "Dalen"],
            ["een boterham met confituur eten", "Stijgen"],
            ["een lange inspanning", "Dalen"],
        ],
        "Insuline laat cellen glucose opnemen. Glucagon laat de lever glucose vrijgeven. Eten verhoogt het gehalte, inspanning verbruikt glucose."),
    mk("Wat gebeurt er met een sarcomeer bij een samentrekking?",
       ["Actine schuift tussen de myosinefilamenten.", "De myosinefilamenten worden zelf een stuk korter en dikker.", "De Z-platen schuiven verder uit elkaar, weg van het midden.", "De lichte band wordt breder dan voordien."],
       0,
       "De filamenten zelf worden niet korter. Ze schuiven over elkaar, zodat de Z-platen dichter bij elkaar komen en de lichte band smaller wordt."),
    sleep(
        "Een klier zonder afvoergang geeft zijn [[hormoon]] af aan het [[bloed]].",
        ["spier", "darmkanaal"],
        "Hormonen reizen met het bloed door het lichaam en werken enkel op cellen met de passende receptor."),

    # Voortplanting
    koppel(
        "Koppel het hormoon aan wat het doet in de menstruatiecyclus.",
        [
            ["LH", "lokt de ovulatie uit"],
            ["progesteron", "houdt het baarmoederslijmvlies in stand"],
            ["oestrogeen", "laat het slijmvlies in de eerste helft opbouwen"],
        ],
        ["laat het bloedglucosegehalte dalen"],
        "Insuline laat het bloedglucosegehalte dalen. De andere drie sturen de cyclus."),
    inv("Een cyclus duurt 28 dagen en de ovulatie valt 14 dagen voor de volgende menstruatie. Op welke dag valt de ovulatie bij een cyclus van 32 dagen?",
        ["18"],
        "De luteale fase duurt vrij vast ongeveer 14 dagen. 32 − 14 = 18: de folliculaire fase is langer."),
    tabel(
        "Klopt dit over de zwangerschap?",
        [
            ("De bevruchting gebeurt meestal in de eileider.", J),
            ("In de placenta vermengt het bloed van moeder en kind zich.", F),
            ("Alcohol kan via de placenta het kind bereiken.", J),
        ],
        "In de placenta liggen de bloedvaten van moeder en kind dicht bij elkaar, maar het bloed vermengt zich niet. Stoffen gaan er wel door."),

    # Biodiversiteit en micro-organismen
    sorteer(
        "Werkt een antibioticum hiertegen of niet?",
        ["Werkt wel", "Werkt niet"],
        [
            ["een bacteriële keelontsteking", "Werkt wel"],
            ["griep", "Werkt niet"],
            ["een gewone verkoudheid", "Werkt niet"],
            ["een ontstoken wonde met bacteriën", "Werkt wel"],
        ],
        "Antibiotica werken tegen bacteriën, niet tegen virussen. Griep en verkoudheid komen door virussen."),
    keuze(
        "Een vaccin bevat een onschadelijke vorm van de ziekteverwekker. Het lichaam maakt dan [[*antistoffen|hormonen|enzymen]] en onthoudt die indringer, zodat het bij een echte besmetting [[*sneller|trager]] reageert.",
        "Een vaccin traint de afweer zonder dat je eerst ziek moet worden."),
    mk("Waarom is versnippering van een leefgebied schadelijk, ook als de totale oppervlakte gelijk blijft?",
       ["Dieren kunnen niet meer vrij tussen de stukken trekken.", "Er komt per stuk meer zonlicht binnen dan in een groot gebied.", "Planten groeien beter in kleine stukjes dan in een groot bos.", "Versnippering zorgt altijd voor meer soorten per hectare."],
       0,
       "Populaties raken geïsoleerd. Ze worden kleiner en kwetsbaarder, en er is minder uitwisseling van erfelijk materiaal."),

    # Gedrag
    tabel(
        "Is dit gedrag aangeboren of geleerd? Duid telkens aan.",
        [
            ("Een pasgeboren baby zuigt aan een speen", "Aangeboren"),
            ("Een hond kwijlt bij het rinkelen van zijn voerbak", "Geleerd"),
            ("Een mees eet een bepaalde rups niet meer nadat die vies smaakte", "Geleerd"),
            ("Een kat trekt zijn poot terug van iets heets", "Aangeboren"),
        ],
        "Reflexen en zuigen zijn aangeboren. Conditionering en leren uit ervaring zijn vormen van geleerd gedrag.",
        kolommen=["Aangeboren", "Geleerd"]),
    koppel(
        "Koppel de interactie aan het voorbeeld.",
        [
            ["predatie", "een sperwer vangt een mees"],
            ["parasitisme", "een teek zuigt bloed bij een hond"],
            ["competitie", "twee mezen vechten om dezelfde nestkast"],
        ],
        ["een eik maakt suikers met zonlicht"],
        "Fotosynthese is geen interactie tussen twee organismen."),

    # Ecosysteem en kringlopen
    keuze(
        "Bij daglicht geeft een plant netto [[*zuurstofgas|koolstofdioxide]] af, omdat de fotosynthese dan [[*sneller|trager]] verloopt dan de celademhaling.",
        "Een plant doet altijd celademhaling. Overdag wint de fotosynthese het; in het donker is er enkel celademhaling."),
    volgorde(
        "Zet de stappen van eutrofiëring in een vijver in de juiste volgorde.",
        ["Mest spoelt met nitraten en fosfaten de vijver in", "Algen groeien explosief", "Algen sterven en worden afgebroken", "Reducenten verbruiken veel zuurstofgas", "Vissen sterven door zuurstoftekort"],
        "Te veel voedingsstoffen geven een algenbloei. De afbraak van al die dode algen verbruikt het zuurstofgas in het water."),
    sorteer(
        "Haalt dit proces CO₂ uit de lucht of brengt het CO₂ in de lucht?",
        ["Haalt CO₂ uit de lucht", "Brengt CO₂ in de lucht"],
        [
            ["fotosynthese", "Haalt CO₂ uit de lucht"],
            ["celademhaling", "Brengt CO₂ in de lucht"],
            ["verbranding van aardolie", "Brengt CO₂ in de lucht"],
            ["groei van een jong bos", "Haalt CO₂ uit de lucht"],
        ],
        "Planten leggen koolstof vast in organische stof. Ademhaling en verbranding brengen die koolstof terug als CO₂."),
    mk("Waarom kan een stuk land meer mensen voeden met graan dan met vlees?",
       ["Per trofisch niveau gaat zo'n 90 % energie verloren.", "Vee eet enkel gras dat mensen ook zouden kunnen eten en verteren.", "Graan bevat altijd meer eiwitten per gram dan vlees van koeien.", "Vlees bederft sneller, waardoor er onderweg veel verloren gaat."],
       0,
       "Wie graan eet, staat een niveau lager in de keten. Er gaat dan minder energie verloren dan wanneer het graan eerst door vee wordt opgegeten."),

    # Levensreddend handelen
    volgorde(
        "Zet de eerste stappen bij iemand die op straat in elkaar zakt in de juiste volgorde.",
        ["Zorg voor veiligheid", "Ga na of het slachtoffer reageert", "Ga na of het normaal ademt", "Bel 112 en laat een AED halen", "Start met 30 borstcompressies"],
        "Eerst veiligheid, dan bewustzijn, dan ademhaling. Ademt het slachtoffer niet normaal, dan bel je 112 en start je met reanimeren."),
    tabel(
        "Juist of fout bij eerste hulp?",
        [
            ("Een brandwond koel je ongeveer 20 minuten met lauw stromend water.", J),
            ("Een blaar bij een brandwond prik je best zelf open.", F),
            ("Bij een hevige bloeding druk je de wonde stevig dicht.", J),
            ("Een slachtoffer in shock geef je best veel te drinken.", F),
        ],
        "Koelen en druk zetten helpen. Een blaar beschermt de wonde, en iemand in shock geef je niets te drinken."),

    # Onderzoek
    casus(
        "Een leerling zet 10 bonenplantjes bij 20 °C en 10 bonenplantjes bij 30 °C. Alle plantjes krijgen evenveel water en licht. Na twee weken meet ze de lengte.",
        [
            mk("Wat is de onafhankelijke variabele in deze proef?",
               ["de temperatuur", "de lengte van de plantjes", "de hoeveelheid water", "het aantal plantjes"],
               0,
               "De onafhankelijke variabele verander je zelf bewust: hier de temperatuur. De lengte meet je; dat is de afhankelijke variabele."),
            mk("Waarom gebruikt ze 10 plantjes per groep en niet 1?",
               ["Zo weegt een toevallige uitschieter minder door.", "Zo groeien de plantjes sneller omdat ze elkaar steunen.", "Zo hoeft ze geen controlegroep meer te maken voor de proef.", "Zo kan ze de temperatuur gemakkelijker constant houden."],
               0,
               "Met meerdere plantjes per groep wordt het gemiddelde betrouwbaarder."),
        ]),
    inv("Je kijkt door een oculair van 10× en een objectief van 40×. Hoeveel keer wordt het preparaat in totaal vergroot? Enkel het getal.",
        ["400"],
        "De totale vergroting is oculair × objectief = 10 · 40 = 400."),

    # Schrijfopdracht
    open_("In een gebied verdwijnen de bijen. Leg in 4 à 6 zinnen uit welke gevolgen dat heeft voor het ecosysteem en voor de mens.",
          "Bijen bestuiven veel planten. Als ze verdwijnen, vormen veel planten minder vruchten en zaden. Daardoor hebben dieren die van die vruchten en zaden leven minder voedsel, en dat werkt door in heel het voedselweb. Ook de mens oogst minder fruit en groenten. De biodiversiteit daalt en het ecosysteem wordt minder stabiel.",
          "Een goed antwoord noemt de bestuiving, het gevolg voor planten, het doorwerken in het voedselweb en het gevolg voor de mens."),
]

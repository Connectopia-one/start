# -*- coding: utf-8 -*-
"""Licht, geluid en het elektromagnetisch spectrum — 🌍 Beyond, fysica.

Deel 1 gaat over licht en over het elektromagnetisch spectrum: het
stralenmodel, de regelmatige en de diffuse weerkaatsing, het beeld in een
vlakke spiegel, kern- en bijschaduw met de verduisteringen, de bolle lens met
haar brandpunt en haar reëel of virtueel beeld, de ordening van radiogolven
tot gammastraling, het foton met zijn energie, en de proef van Young. Deel 2
gaat over geluid: de geluidssnelheid in verschillende stoffen en bij een
andere temperatuur, toonhoogte, toonsterkte en klankkleur, infrasoon en
ultrasoon, de decibelschaal met de gehoorschade die erbij hoort, de
grondfrequentie met haar boventonen, en het dopplereffect.

De rode draad is dat licht en geluid allebei golven zijn, met dezelfde
eigenschappen, maar van een heel verschillende soort: het ene
elektromagnetisch en het andere mechanisch. Omdat er hier geen stralengang
getekend kan worden, vragen de vragen naar de kenmerken van het beeld in
woorden.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een elektromagnetische golf?",
        opties=[
            "een transversale golf die in vacuüm met de lichtsnelheid loopt",
            "een longitudinale golf die in vacuüm met de lichtsnelheid loopt",
            "een transversale golf die lucht nodig heeft om te lopen",
            "een trilling van de deeltjes van de stof zelf",
        ],
        antwoord=0,
        uitleg="Ze heeft geen stof nodig, want het zijn de elektrische en magnetische velden "
        r"die trillen. In vacuüm is \(c = 3{,}00 \times 10^{8}\ \text{m/s}\).",
    ),
    dict(
        type="invultekst",
        vraag="Hoe groot is de lichtsnelheid in vacuüm, in meter per seconde?",
        antwoord=["300000000", "3 · 10⁸", "ongeveer 300000 km/s"],
        uitleg=r"Preciezer is \(c = 2{,}998 \times 10^{8}\ \text{m/s}\). In glas of water gaat "
        r"licht langzamer.",
    ),
    dict(
        type="waarofniet",
        vraag="Licht gaat in water langzamer dan in vacuüm.",
        antwoord=True,
        uitleg=r"Daarom heeft water \(n > 1\), want \(n = \dfrac{c}{v}\). Dat vertragen is net "
        r"wat de breking veroorzaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen regelmatige en diffuse weerkaatsing?",
        opties=[
            "bij een ruw oppervlak kaatsen de stralen alle kanten op",
            "bij een glad oppervlak kaatsen de stralen alle kanten op",
            "bij een ruw oppervlak gaat alle licht de stof binnen",
            "bij een glad oppervlak wordt alle licht geabsorbeerd",
        ],
        antwoord=0,
        uitleg="Een spiegel kaatst de stralen netjes dezelfde kant op, een blad papier niet. "
        "Daarom zie je in papier geen beeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken heeft het beeld in een vlakke spiegel? Kruis alles aan wat juist is.",
        opties=[
            "het is virtueel",
            "het staat rechtop",
            "het is even groot als het voorwerp",
            "het staat omgekeerd",
        ],
        antwoord=[0, 1, 2],
        uitleg="Links en rechts lijken wel verwisseld, maar boven en onder niet. Het beeld "
        "ligt even ver achter de spiegel als het voorwerp ervoor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een virtueel beeld?",
        opties=[
            "een beeld dat je niet op een scherm kan opvangen",
            "een beeld dat je wel op een scherm kan opvangen",
            "een beeld dat altijd omgekeerd staat",
            "een beeld dat altijd kleiner is dan het voorwerp",
        ],
        antwoord=0,
        uitleg="De stralen komen er niet echt samen, ze lijken er enkel vandaan te komen. "
        "Een reëel beeld kan je wel op een scherm vangen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ontstaat een kernschaduw?",
        opties=[
            "daar komt geen licht van de bron meer toe",
            "daar komt het licht van een deel van de bron toe",
            "daar komt het licht van de hele bron toe",
            "daar wordt het licht door de lucht weerkaatst",
        ],
        antwoord=0,
        uitleg="In de bijschaduw komt het licht van een stuk van de bron wel toe. Een "
        "puntbron geeft daarom alleen kernschaduw.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een maansverduistering staat de maan tussen de zon en de aarde.",
        antwoord=False,
        uitleg="Dan staat de aarde ertussen en valt haar schaduw op de maan. Staat de maan "
        "ertussen, dan krijg je een zonsverduistering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het brandpunt van een bolle lens?",
        opties=[
            "het punt waar stralen langs de optische as samenkomen",
            "het punt waar de lens het dikst is",
            "het punt waar het voorwerp moet staan",
            "het punt waar de lens het licht weerkaatst",
        ],
        antwoord=0,
        uitleg=r"De afstand van de lens tot dat punt is de brandpuntsafstand \(f\). Een bolle "
        r"lens heeft er een aan elke kant.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een voorwerp staat verder dan \(2f\) van een bolle lens. Welk beeld krijg je?",
        opties=[
            "een reëel, omgekeerd en kleiner beeld",
            "een reëel, rechtopstaand en groter beeld",
            "een virtueel, rechtopstaand en groter beeld",
            "een virtueel, omgekeerd en kleiner beeld",
        ],
        antwoord=0,
        uitleg=r"Dat is wat de lens van een fototoestel doet. Staat het voorwerp binnen \(f\), "
        r"dan krijg je een virtueel en groter beeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe liggen de soorten elektromagnetische straling van lage naar hoge frequentie?",
        opties=[
            "radiogolven, microgolven, infrarood, licht, uv, röntgen, gamma",
            "gamma, röntgen, uv, licht, infrarood, microgolven, radiogolven",
            "licht, infrarood, uv, radiogolven, microgolven, röntgen, gamma",
            "microgolven, radiogolven, licht, infrarood, uv, gamma, röntgen",
        ],
        antwoord=0,
        uitleg="Hoe hoger de frequentie, hoe kleiner de golflengte en hoe groter de energie "
        "per foton. Zichtbaar licht is maar een smalle strook in het midden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband bestaat er tussen de energie van een foton en de golf?",
        opties=[
            r"de energie stijgt met \(f\) en daalt met \(\lambda\)",
            r"de energie daalt met \(f\) en stijgt met \(\lambda\)",
            r"de energie stijgt met zowel \(f\) als \(\lambda\)",
            r"de energie hangt enkel van de amplitude \(A\) af",
        ],
        antwoord=0,
        uitleg=r"Daarom is gammastraling zo gevaarlijk en een radiogolf niet. De formule is "
        r"\(E = h\,f\), met \(h = 6{,}63 \times 10^{-34}\ \text{J}\cdot\text{s}\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stralingen zijn ioniserend? Kruis alles aan wat juist is.",
        opties=[
            "röntgenstraling",
            "gammastraling",
            "hoogenergetische uv-straling",
            "radiogolven",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie hebben genoeg energie per foton om een elektron uit een atoom te "
        "slaan. Radiogolven en microgolven kunnen dat niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Microgolven worden in een magnetron gebruikt omdat ze ioniserend zijn.",
        antwoord=False,
        uitleg="Ze zijn juist niet ioniserend, en ze verwarmen door de watermoleculen te "
        "laten trillen. Hun energie per foton is daar veel te klein voor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men radiogolven voor communicatie over grote afstand?",
        opties=[
            "ze hebben een groot doordringend vermogen en buigen goed af",
            "ze hebben de hoogste energie per foton van alle golven",
            "ze lopen sneller dan de andere elektromagnetische golven",
            "ze worden door de lucht helemaal niet geabsorbeerd",
        ],
        antwoord=0,
        uitleg="Hun grote golflengte laat ze rond obstakels buigen. Alle "
        "elektromagnetische golven lopen even snel in vacuüm.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatregelen beschermen tegen hoogenergetische straling? Kruis alles aan wat juist is.",
        opties=[
            "zonnecrème en een zonnebril tegen uv-straling",
            "een loden schort bij een röntgenfoto",
            "zo weinig en zo kort mogelijk blootgesteld worden",
            "een gewone bril van glas tegen gammastraling",
        ],
        antwoord=[0, 1, 2],
        uitleg="Gammastraling gaat door glas heen alsof het er niet is; daar heb je lood of "
        "beton voor nodig. Afstand, tijd en afscherming zijn de drie sleutels.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat laat de proef van Young zien?",
        opties=[
            "dat licht zich als een golf gedraagt",
            "dat licht uit kleine deeltjes bestaat",
            "dat licht in vacuüm langzamer gaat",
            "dat licht door een lens gebogen wordt",
        ],
        antwoord=0,
        uitleg="Achter twee smalle spleten verschijnt een patroon van lichte en donkere "
        "strepen. Dat is interferentie, en dat kan alleen een golf.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor interferentie van licht heb je twee coherente bronnen nodig.",
        antwoord=True,
        uitleg="Ze moeten dezelfde frequentie en een vast faseverschil hebben. In de proef "
        "van Young zorgt één bron achter twee spleten daarvoor.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het kleinste pakketje energie van licht?",
        antwoord=["een foton", "foton", "lichtkwantum"],
        uitleg=r"De energie ervan is \(E = h\,f\). Licht gedraagt zich dus zowel als een golf "
        r"als als een deeltje.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke straling gebruikt een bagagescanner op de luchthaven?",
        opties=[
            "röntgenstraling",
            "radiogolven",
            "infraroodstraling",
            "zichtbaar licht",
        ],
        antwoord=0,
        uitleg="Ze dringt door de koffer maar niet door metaal. Een nachtkijker en een "
        "warmtecamera werken wel met infrarood.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="In welke stof loopt geluid het snelst?",
        opties=[
            "in staal",
            "in water",
            "in lucht",
            "in vacuüm",
        ],
        antwoord=0,
        uitleg="Hoe steviger de deeltjes aan elkaar hangen, hoe sneller ze de beweging "
        "doorgeven. In vacuüm loopt geluid helemaal niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Geluid loopt in warme lucht sneller dan in koude lucht.",
        antwoord=True,
        uitleg=r"De deeltjes bewegen daar sneller en geven de stoot vlugger door. Rond "
        r"\(20\ ^\circ\text{C}\) is \(v = 343\) m/s.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Je ziet een bliksem en hoort de donder \(6{,}0\) s later. Hoe ver is het onweer ongeveer?",
        opties=[
            r"ongeveer \(2\) km",
            r"ongeveer \(6\) km",
            r"ongeveer \(340\) m",
            r"ongeveer \(20\) km",
        ],
        antwoord=0,
        uitleg=r"Met \(v = 340\) m/s is \(d = v\,t = 340 \times 6{,}0 = 2040\) m. Het licht is "
        r"er zo goed als meteen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband bestaat er tussen de frequentie en wat je hoort?",
        opties=[
            "een hogere frequentie geeft een hogere toon",
            "een hogere frequentie geeft een luidere toon",
            "een hogere frequentie geeft een andere klankkleur",
            "een hogere frequentie geeft een lagere toon",
        ],
        antwoord=0,
        uitleg="De amplitude bepaalt hoe luid het klinkt. De vorm van het patroon in de tijd "
        "bepaalt de klankkleur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan hoor je het verschil tussen een viool en een fluit op dezelfde toon?",
        opties=[
            "aan de klankkleur, dus aan de vorm van het patroon",
            "aan de toonhoogte, dus aan de frequentie",
            "aan de toonsterkte, dus aan de amplitude",
            "aan de snelheid waarmee het geluid aankomt",
        ],
        antwoord=0,
        uitleg="De grondtoon is dezelfde, maar de boventonen verschillen. Dat samen heet "
        "klankkleur of timbre.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de klankkleur van een geluid met een ander woord?",
        antwoord=["timbre", "het timbre", "klankfarbe"],
        uitleg="Ze komt van de boventonen die naast de grondtoon meeklinken. Daarom klinkt "
        "elk instrument anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke frequenties kan een mens normaal horen?",
        opties=[
            r"van \(20\) Hz tot \(20\,000\) Hz",
            r"van \(2\) Hz tot \(2000\) Hz",
            r"van \(200\) Hz tot \(200\,000\) Hz",
            r"van \(20\) Hz tot \(200\) Hz",
        ],
        antwoord=0,
        uitleg=r"Met de jaren verdwijnt de bovenkant van dat gebied. Onder \(20\) Hz heet het "
        r"infrasoon, erboven ultrasoon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is ultrasoon geluid?",
        opties=[
            r"geluid met \(f > 20\,000\) Hz",
            r"geluid met \(f < 20\) Hz",
            "geluid dat luider is dan de pijndrempel",
            "geluid dat sneller loopt dan in lucht",
        ],
        antwoord=0,
        uitleg=r"Een vleermuis en een echografie werken ermee. Onder \(20\) Hz heet het "
        r"infrasoon, en dat voel je eerder dan dat je het hoort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke toepassingen gebruiken ultrasoon geluid? Kruis alles aan wat juist is.",
        opties=[
            "een echografie bij de dokter",
            "een vleermuis die zijn weg zoekt",
            "een sonar die de diepte van de zee meet",
            "een radio die een programma uitzendt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie meten een afstand uit de tijd die de echo nodig heeft. Een radio "
        "werkt met elektromagnetische golven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar ligt de gehoordrempel van een mens op de decibelschaal?",
        opties=[
            r"bij \(0\) dB",
            r"bij \(20\) dB",
            r"bij \(80\) dB",
            r"bij \(120\) dB",
        ],
        antwoord=0,
        uitleg=r"Rond \(80\) dB ligt de gevaargrens en rond \(120\) dB de pijndrempel. De "
        r"schaal begint dus bij het zachtste wat we nog horen.",
    ),
    dict(
        type="invultekst",
        vraag="Vanaf hoeveel decibel spreekt men van de gevaargrens voor het gehoor?",
        antwoord=["80", "80 dB", "tachtig"],
        uitleg=r"Daarboven kan langdurige blootstelling schade geven. De pijndrempel ligt rond "
        r"\(120\) dB.",
    ),
    dict(
        type="waarofniet",
        vraag="Gehoorschade hangt zowel van het geluidsniveau als van de duur van de blootstelling af.",
        antwoord=True,
        uitleg="Een uur op een fuif kan erger zijn dan een korte knal. Daarom staan er in de "
        "geluidsnorm grenzen voor beide.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe ontstaat blijvende gehoorschade in het binnenoor?",
        opties=[
            "de trilhaartjes van de haarcellen breken af en groeien niet terug",
            "het trommelvel scheurt en groeit daarna krom weer dicht",
            "de gehoorbeentjes raken los van elkaar",
            "de gehoorgang raakt verstopt door te veel oorsmeer",
        ],
        antwoord=0,
        uitleg="Die haarcellen zetten de trilling in een signaal om. Wat weg is, komt niet "
        "terug, dus is voorkomen het enige dat helpt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatregelen voorkomen gehoorschade op een fuif? Kruis alles aan wat juist is.",
        opties=[
            "oordopjes dragen die het geluid gelijkmatig dempen",
            "verder van de luidspreker gaan staan",
            "tussendoor een pauze nemen op een stillere plek",
            "even heel luid meezingen om de oren te ontlasten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Meezingen helpt niets, en je stem is bovendien dicht bij je eigen oren. "
        "Afstand, tijd en demping zijn de drie die werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je gaat twee keer zo dicht bij een geluidsbron staan. Wat gebeurt er met de geluidsintensiteit?",
        opties=[
            "ze wordt vier keer zo groot",
            "ze wordt twee keer zo groot",
            "ze wordt twee keer zo klein",
            "ze blijft ongeveer dezelfde",
        ],
        antwoord=0,
        uitleg=r"Het vermogen verdeelt zich over een boloppervlak, dus \(I \sim \dfrac{1}{r^{2}}\). "
        r"Halveer je \(r\), dan verviervoudigt \(I\).",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een geluid van \(60\) dB is twee keer zo intens als een geluid van \(30\) dB.",
        antwoord=False,
        uitleg=r"De decibelschaal is logaritmisch: elke \(10\) dB is tien keer zo intens. "
        r"\(60\) dB tegenover \(30\) dB is dus \(10^{3}\) keer zo intens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de grondfrequentie van een snaar?",
        opties=[
            "de laagste frequentie waarop ze als staande golf kan trillen",
            "de hoogste frequentie waarop ze kan trillen",
            "de frequentie waarop ze het luidst klinkt",
            "de frequentie van de tweede boventoon",
        ],
        antwoord=0,
        uitleg="De boventonen zijn er veelvouden van. Samen bepalen ze de klankkleur van het "
        "instrument.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een snaar heeft een grondfrequentie van \(220\) Hz. Welke frequentie heeft de derde harmonische?",
        opties=[
            r"\(660\) Hz",
            r"\(440\) Hz",
            r"\(223\) Hz",
            r"\(73\) Hz",
        ],
        antwoord=0,
        uitleg=r"\(f_{n} = n\,f_{1}\), dus \(f_{3} = 3 \times 220 = 660\) Hz. De tweede zou "
        r"\(440\) Hz zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het dopplereffect bij geluid?",
        opties=[
            "de waargenomen frequentie verschilt als bron en waarnemer bewegen",
            "de waargenomen amplitude verschilt als bron en waarnemer bewegen",
            "de geluidssnelheid verschilt als de bron beweegt",
            "de klankkleur verschilt als de waarnemer beweegt",
        ],
        antwoord=0,
        uitleg="Komt de bron naar je toe, dan hoor je een hogere toon. Rijdt ze weg, dan "
        "hoor je een lagere.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het dopplereffect verandert de frequentie die de bron zelf uitzendt.",
        antwoord=False,
        uitleg="De bron blijft hetzelfde uitzenden; alleen wat de waarnemer ontvangt, "
        "verschuift. Daarom hoort de bestuurder van de ziekenwagen de sirene niet dalen.",
    ),
]

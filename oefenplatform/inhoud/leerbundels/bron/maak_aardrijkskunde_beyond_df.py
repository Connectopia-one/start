# -*- coding: utf-8 -*-
"""De leerbundels van aardrijkskunde voor 🌍 Beyond dubbele finaliteit.

    python3 -I maak_alles.py aardrijkskunde

Zestien bundels, één per thema van `inhoud/beyond-dubbele-finaliteit/aardrijkskunde.json`.

Gebaseerd op de vakfiche aardrijkskunde 3DU van de derde graad dubbele
finaliteit, geldig vanaf 1 januari 2027. Ze geldt voor de basisvorming van de
dubbele finaliteit en voor commerciële organisatie. Het examen is digitaal,
duurt 120 minuten en bestaat enkel uit gesloten vraagvormen; er is geen
giscorrectie. Toegelaten: de atlas van Plantyn, Geopunt, een rekenapp,
spellingcontrole en een eenvoudig woordenboek.

De stof overlapt grotendeels met 🌍 Beyond doorstroom, maar een leerling van de
dubbele finaliteit ziet enkel de vakken van zijn eigen niveau. Daarom liggen de
bundels van doorstroom hier aan de basis, en worden ze hier opnieuw geschikt:
eenentwintig thema's van doorstroom worden hier zestien, met de secties anders
verdeeld. Wat deze fiche extra vraagt, krijgt een eigen sectie.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De sleutels eindigen op "-beyond-dubbele-finaliteit". Aardrijkskunde bestaat
ook op 🚀 Boost en op 🌍 Beyond doorstroom, en daar komen thematitels in voor
die hier bijna gelijk klinken.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag.
"""
import copy
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))

import bundel
import svg
import maak_aardrijkskunde_beyond as door

VAK = "Aardrijkskunde"
DF = "🌍 Beyond dubbele finaliteit — 5de en 6de middelbaar"
NA = "-beyond-dubbele-finaliteit"
tabel = bundel.tabel

BUNDELS = {}


def sectie(sleutel, kop, extra=()):
    """Eén sectie uit een bundel van 🌍 Beyond doorstroom, met blokken erbij."""
    for s in door.BUNDELS[sleutel + "-beyond"]["secties"]:
        if s["kop"] == kop:
            s = copy.deepcopy(s)
            s["blokken"] = list(s["blokken"]) + list(extra)
            return s
    raise KeyError(f"{sleutel}: {kop}")


def zet(sleutel, titel, onder, secties):
    BUNDELS[sleutel + NA] = dict(vak=VAK, niveau=DF, titel=titel,
                                 onder=onder, secties=secties)


# ───────────────────── 1. Situeren op aarde en de aardse sferen
HET_EXAMEN = dict(kop="Het examen, en wat erbij mag", blokken=[
    ("p", "Het examen aardrijkskunde is <strong>digitaal</strong>, duurt <strong>120 minuten</strong> "
          "en bestaat <strong>enkel uit gesloten vraagvormen</strong>: meerkeuze, juist of fout, "
          "aanduiden en koppelen. Je schrijft dus <strong>geen open tekst</strong> waarin je zelf een "
          "antwoord uitlegt. Er is <strong>geen giscorrectie</strong>, dus een fout antwoord kost je "
          "niets extra: laat nooit een vraag open."),
    ("p", "Je mag een aantal hulpmiddelen gebruiken, en dat is geen detail: een deel van de vragen "
          "is net bedoeld om op te <strong>zoeken</strong> in plaats van vanbuiten te kennen."),
    ("p", tabel(["Wat je mag gebruiken", "Waarvoor"], [
        ["de <strong>atlas van Plantyn</strong>", "coördinaten, reliëf, klimaat, bevolking opzoeken"],
        ["<strong>Geopunt</strong>", "de kaartendienst van de Vlaamse overheid, met luchtfoto's en kaartlagen"],
        ["een <strong>rekenapp</strong>", "schaal, dichtheid en verschillen uitrekenen"],
        ["<strong>spellingcontrole</strong> en een eenvoudig woordenboek", "voor de taal van de vraag"],
    ])),
    ("kader", "<strong>Aardrijkskunde ligt op het raakvlak van de natuurwetenschappen en de "
              "menswetenschappen.</strong> Je bestudeert even goed gesteenten en wind als steden en "
              "bevolking, en vooral hoe die twee op elkaar inwerken."),
])

DE_WERELDKAART = dict(kop="Je plaats op de wereldkaart", blokken=[
    ("p", "Een deel van de vragen gaat simpelweg over <strong>waar iets ligt</strong>. Je zoekt dat op "
          "in de atlas, maar het gaat sneller als je de grote lijnen al kent."),
    ("p", tabel(["Vraag", "Antwoord"], [
        ["het werelddeel dat het dichtst bij België ligt", "<strong>Afrika</strong>, over de Middellandse Zee"],
        ["de oceaan tussen Europa en Amerika", "de <strong>Atlantische Oceaan</strong>"],
        ["de rivier die bij Nederland in de Noordzee uitmondt", "de <strong>Rijn</strong>"],
        ["reliëfeenheden in Europa", "de <strong>Alpen</strong>, de <strong>Pyreneeën</strong>, de <strong>Ardennen</strong>"],
        ["een reliëfeenheid die niét in Europa ligt", "de <strong>Andes</strong>, in Zuid-Amerika"],
    ])),
    ("p", "Van de steden die je vaak tegenkomt, ligt <strong>Moskou</strong> het verst naar het "
          "<strong>oosten</strong>: ongeveer 37° oosterlengte, tegenover 5° OL voor Hasselt, 2° OL voor "
          "Parijs en 0° voor Londen. Hoe hoger de oosterlengte, hoe verder naar het oosten."),
    ("weetje", "Een plaats op 10° NB en 10° WL ligt niet in Azië maar in <strong>Afrika</strong>: "
               "westerlengte brengt je vanuit Greenwich naar de Atlantische Oceaan en West-Afrika toe, "
               "niet naar het oosten."),
])

zet("situeren-op-aarde-en-de-aardse-sferen",
    "Situeren op aarde en de aardse sferen",
    "Het gradennet tot op de minuut, absoluut en relatief situeren, het gereedschap van de geograaf "
    "en de sferen van het systeem aarde.",
    [
        sectie("situeren-kaarten-en-observatie", "Breedte en lengte, tot op de minuut", extra=[
            ("p", "Drie <strong>breedtecirkels dragen een eigen naam</strong>: de <strong>evenaar</strong> "
                  "op 0°, de <strong>keerkringen</strong> op 23,5° en de <strong>poolcirkels</strong> op "
                  "66,5°. De nulmeridiaan is géén breedtecirkel maar een meridiaan. Op <strong>21 juni</strong> "
                  "staat de zon in het zenit boven de <strong>Kreeftskeerkring</strong>, de noordelijke "
                  "keerkring; op 22 december boven de Steenbokskeerkring."),
            ("p", "Bij een coördinaat schrijf je altijd <strong>N of Z</strong> en <strong>O of W</strong> erbij. "
                  "Zonder die letters zijn er telkens <strong>twee halfronden mogelijk</strong>: 30° breedte "
                  "zonder meer kan zowel boven als onder de evenaar liggen. 30° <strong>zuider</strong>breedte "
                  "ligt onder de evenaar."),
            ("kader", "Een <strong>graad breedte</strong> is overal op aarde ongeveer <strong>111 km</strong>, "
                      "want alle meridianen zijn even lang. Een <strong>graad lengte</strong> is dat "
                      "<strong>niet</strong>: aan de evenaar is hij ook 111 km, maar hoe dichter bij de pool, "
                      "hoe korter, tot nul aan de pool zelf. De breedtecirkels worden immers kleiner naar "
                      "de polen toe."),
        ]),
        sectie("situeren-kaarten-en-observatie", "Absoluut en relatief situeren", extra=[
            ("p", "Dezelfde twee groepen heten op deze fiche <strong>fysischgeografisch</strong> en "
                  "<strong>sociaalgeografisch</strong>. Een oceaan, een rivier en een klimaatzone zijn "
                  "<strong>fysischgeografisch</strong>; een stad, een taal en armoede zijn "
                  "<strong>sociaalgeografisch</strong>. Een godsdienst hoort dus bij de tweede groep, "
                  "niet bij de eerste, en een reliëfeenheid bij de eerste, niet bij de tweede."),
            ("kader", "Bij een <strong>absolute plaatsbepaling</strong> horen drie dingen: de "
                      "<strong>breedte</strong>, de <strong>lengte</strong>, en de letters "
                      "<strong>noord of zuid en oost of west</strong>. De afstand tot de kust hoort er "
                      "niet bij: dat is relatief situeren. Zo ligt <strong>51° noorderbreedte en 5° "
                      "oosterlengte</strong> in <strong>Limburg</strong>."),
        ]),
        sectie("situeren-kaarten-en-observatie", "Kaarten lezen"),
        sectie("situeren-kaarten-en-observatie", "Het gereedschap van de geograaf", extra=[
            ("p", "Voor de <strong>landschapsanalyse</strong> noemt de fiche daarnaast "
                  "<strong>geologische doorsnedes</strong> en <strong>GIS-viewers</strong>. Een "
                  "<strong>geologische doorsnede</strong> is een zijaanzicht van de ondergrond: je ziet "
                  "er de <strong>lagen onder de grond</strong> op, en hoe ze geplooid of gebroken zijn. "
                  "Een microscoop hoort daar niet bij; die gebruik je in het labo, niet in het landschap."),
            ("p", "<strong>GIS</strong> staat voor geografisch informatiesysteem: een systeem dat "
                  "<strong>kaartlagen over elkaar legt</strong> en ze samen laat rekenen. Je kiest zelf "
                  "welke laag bovenop komt: luchtfoto, wegen, overstromingsgevoelig gebied, bodemtype. "
                  "<strong>Geopunt</strong> is zo'n GIS-viewer van de Vlaamse overheid, en je mag hem op "
                  "het examen gebruiken."),
        ]),
        sectie("situeren-kaarten-en-observatie", "Het systeem aarde: de sferen", extra=[
            ("p", "De <strong>biosfeer</strong> is de sfeer van <strong>al het leven op aarde</strong>. "
                  "Dat de sferen <strong>in interactie staan</strong>, betekent dat ze "
                  "<strong>elkaar beïnvloeden</strong>: ze liggen niet netjes gestapeld en ze bestaan niet "
                  "los van elkaar. Aan een <strong>rivieroever</strong> raken de <strong>hydrosfeer</strong> "
                  "(het water), de <strong>geosfeer</strong> (de oever zelf) en de <strong>biosfeer</strong> "
                  "(het riet en de vissen) elkaar tegelijk. De Kuipergordel hoort niet bij de sferen van de "
                  "aarde maar bij het zonnestelsel."),
        ]),
        DE_WERELDKAART,
        HET_EXAMEN,
    ])


# ───────────────────── 2. Het heelal en de plaats van de aarde
DE_SFEREN_KORT = dict(kop="De sferen, en de atmosfeer als schild", blokken=[
    ("p", "Het systeem aarde bestaat uit <strong>sferen</strong>. De <strong>atmosfeer</strong> is de "
          "sfeer die <strong>uit lucht</strong> bestaat, de <strong>hydrosfeer</strong> die van al het "
          "water, de <strong>geosfeer</strong> die van het gesteente, en de <strong>biosfeer</strong> "
          "die van al het leven. Ze raken elkaar voortdurend: aan een <strong>rivieroever</strong> "
          "liggen de hydrosfeer, de geosfeer en de biosfeer tegen elkaar aan."),
    ("p", "De atmosfeer is ook een <strong>schild</strong>. Kleine <strong>meteoroïden</strong> die de "
          "aarde naderen, <strong>verbranden erin</strong> door de wrijving met de lucht. Zonder "
          "atmosfeer zou elke brok de grond raken, zoals op de maan te zien is."),
])

zet("het-heelal-en-de-plaats-van-de-aarde",
    "Het heelal en de plaats van de aarde",
    "De oerknal, de afstanden in het heelal, het adres van ons zonnestelsel, en hoe we dat allemaal "
    "waarnemen.",
    [
        sectie("het-heelal-ontstaan-en-afstanden", "De Big Bangtheorie"),
        sectie("het-heelal-ontstaan-en-afstanden", "Drie vaststellingen die voor een uitdijend heelal pleiten"),
        sectie("het-heelal-ontstaan-en-afstanden", "Hoe het heelal veranderde"),
        sectie("het-heelal-ontstaan-en-afstanden", "Afstanden in en rond het zonnestelsel", extra=[
            ("kader", "<strong>Lichtjaar, astronomische eenheid en kilometer zijn alle drie "
                      "afstandsmaten</strong>, elk op een andere schaal. Een <strong>zeemijl</strong> is "
                      "ook een afstand, maar die gebruik je op zee en niet in het heelal. Een "
                      "<strong>kilometer per uur</strong> is géén afstand maar een snelheid."),
        ]),
        sectie("het-heelal-ontstaan-en-afstanden", "Lichtjaren, en het adres van de aarde", extra=[
            ("p", "De <strong>Melkweg is niet het enige sterrenstelsel</strong>: er zijn er honderden "
                  "miljarden. De Andromedanevel is er één die je bij donker weer met het blote oog ziet."),
            ("kader", "Een sterrenstelsel heet ook een <strong>galaxie</strong>. De fiche noemt drie "
                      "delen van het heelal bij naam: de <strong>galaxie</strong>, de "
                      "<strong>cluster</strong> en de <strong>supercluster</strong>. Van klein naar "
                      "groot: <strong>planetenstelsel, galaxie, cluster, supercluster</strong>. De "
                      "atmosfeer hoort daar niet bij; dat is een sfeer van de aarde."),
        ]),
        sectie("de-zon-en-het-zonnestelsel", "Hoe het zonnestelsel ontstond", extra=[
            ("kader", "Dat de aarde in lagen uiteenviel, komt doordat <strong>het zwaarste naar het "
                      "midden zonk</strong>: het ijzer naar de kern, het lichtere gesteente erboven. De "
                      "<strong>eerste atmosfeer had dus niet dezelfde samenstelling als de lucht van "
                      "nu</strong>: er zat waterdamp, koolstofdioxide en stikstof in, en nog bijna geen "
                      "zuurstof."),
        ]),
        sectie("situeren-kaarten-en-observatie", "Sterren, planeten en manen", extra=[
            ("p", "Een <strong>maan</strong> draait <strong>rond een planeet</strong> en dus niet "
                  "rechtstreeks rond de zon. De <strong>aardas</strong> is de lijn waarrond de aarde "
                  "draait; op het noordelijk halfrond wijst ze naar het <strong>noorden</strong>, bijna "
                  "precies naar de poolster."),
            ("kader", "De zon staat <strong>alleen tussen de keerkringen</strong> ooit in het zenit. "
                      "Hasselt ligt op bijna 51° noorderbreedte, ver boven de Kreeftskeerkring, dus "
                      "<strong>bij ons staat de zon nooit loodrecht boven je hoofd</strong>, ook niet op "
                      "21 juni."),
        ]),
        sectie("situeren-kaarten-en-observatie", "Waarnemen: telescopen en satellieten", extra=[
            ("p", "De fiche noemt drie <strong>observatietechnieken</strong>: de <strong>optische "
                  "telescoop</strong>, de <strong>radiotelescoop</strong> en de <strong>satelliet</strong>. "
                  "Een <strong>seismograaf</strong> hoort daar niet bij: die meet trillingen in de aarde, "
                  "geen straling uit het heelal."),
            ("p", "Grote telescopen staan <strong>hoog in de bergen</strong> omdat er daar "
                  "<strong>minder lucht boven je hoofd zit en minder licht van steden</strong> is. Hoger "
                  "staan brengt je niet merkbaar dichter bij de sterren; de winst zit in de heldere, "
                  "droge en donkere lucht."),
            ("p", "De twee telescopen vullen elkaar aan. Met een <strong>optische telescoop</strong> "
                  "bekijk je <strong>planeten</strong>, de kraters van de maan, de ringen van Saturnus en "
                  "de manen van Jupiter; <strong>radiogolven zie je er niet mee</strong>, daarvoor heb je "
                  "een radiotelescoop nodig. Die laatste werkt dan weer <strong>door de wolken heen en "
                  "ook overdag</strong>."),
            ("p", "Een ruimtetelescoop zoals <strong>Hubble</strong> staat in een baan om de aarde, en "
                  "het punt daarvan is dat hij <strong>boven de atmosfeer</strong> staat. Hij staat niet "
                  "merkbaar dichter bij de sterren en hij is ook niet goedkoper dan een grote spiegel op "
                  "de grond; hij kijkt gewoon door niets heen."),
        ]),
        sectie("de-zon-en-het-zonnestelsel", "Zonnevlekken, protuberansen en de zonnewind", extra=[
            ("p", "De <strong>zonnecyclus</strong> is dus <strong>de schommeling van de "
                  "zonneactiviteit</strong>, niet de baan van de zon door de Melkweg en niet haar "
                  "levensloop als ster."),
        ]),
        DE_SFEREN_KORT,
    ])


# ───────────────────── 3. Het zonnestelsel en zijn kleine lichamen
PLANETEN_VERGELEKEN = dict(kop="De planeten vergeleken", blokken=[
    ("p", "De planeten draaien <strong>allemaal in dezelfde zin</strong> rond de zon en bijna in "
          "hetzelfde vlak: niet de ene links- en de andere rechtsom. Dat komt doordat ze uit één "
          "draaiende schijf van gas en stof zijn gegroeid."),
    ("p", "Hoe verder van de zon, hoe langer de baan en hoe trager de planeet. De aarde doet er "
          "<strong>365,25 dagen</strong> over, en daarom hebben we elke vier jaar een "
          "<strong>schrikkeldag</strong>. <strong>Een jaar op Jupiter duurt veel langer dan een jaar "
          "op aarde</strong>: bijna twaalf aardse jaren."),
    ("p", tabel(["Vraag", "Antwoord", "Waarom"], [
        ["waarom is <strong>Venus</strong> warmer dan Mercurius?",
         "haar <strong>dikke atmosfeer</strong>",
         "die van koolstofdioxide houdt de warmte vast; Mercurius heeft er bijna geen"],
        ["waarom heeft <strong>Mars</strong> geen dichte atmosfeer meer?",
         "zijn <strong>zwaartekracht is te klein</strong>",
         "hij kon de gassen niet vasthouden en ze zijn weggelekt"],
        ["waarom heeft de <strong>aarde</strong> vloeibaar water en Venus niet?",
         "de aarde is <strong>koeler</strong>",
         "op Venus is het zo heet dat water enkel als damp bestaat"],
    ])),
    ("p", "Niet alleen Saturnus heeft <strong>ringen</strong>: <strong>Jupiter</strong> en "
          "<strong>Uranus</strong> hebben er ook, alleen veel dunner en nauwelijks te zien. "
          "<strong>Mars</strong> heeft geen ringen. De aarde heeft <strong>één</strong> maan; Mars "
          "heeft er twee kleine, de gasreuzen tientallen."),
    ("kader", "De zon bestaat <strong>niet uit steen en ijzer</strong> maar bijna helemaal uit gas: "
              "waterstof en helium. Ze staat ongeveer <strong>150 miljoen kilometer</strong> van de "
              "aarde, en in haar <strong>kern smelt waterstof samen</strong> tot helium. Dat is "
              "kernfusie, geen vuur: er brandt niets op."),
])

BROKSTUKKEN = dict(kop="Brokstukken, kraters en inslagen", blokken=[
    ("p", "Een <strong>planetoïde</strong> en een <strong>meteoroïde</strong> zijn allebei brokken "
          "steen of metaal in de ruimte. Het verschil zit in de <strong>grootte</strong>, niet in het "
          "materiaal: een planetoïde is groot, een meteoroïde klein. IJs hoort bij een komeet, niet "
          "bij een meteoroïde."),
    ("p", "<strong>De meeste meteoroïden die de aarde naderen, verbranden in de atmosfeer.</strong> "
          "Enkel de grootste halen de grond. Een <strong>meteorenzwerm</strong> of sterrenregen is dan "
          "ook precies dat: <strong>veel vallende sterren in enkele nachten</strong>, omdat de aarde "
          "het stofspoor van een komeet kruist."),
    ("p", "Haalt een brok wél de grond en slaat hij een kuil, dan heet die kuil een "
          "<strong>krater</strong> of inslagkrater. <strong>Op de maan zie je er veel meer dan op "
          "aarde, omdat de maan geen atmosfeer heeft</strong>: daar verbrandt niets, en er is geen "
          "wind of water om de kraters weer uit te wissen."),
    ("p", "Een grote inslag laat sporen in de geschiedenis van het leven. De inslag van een grote "
          "<strong>planetoïde</strong> bij Mexico, 66 miljoen jaar geleden, wordt in verband gebracht "
          "met <strong>het einde van de dinosauriërs</strong>."),
    ("weetje", "<strong>Jupiter vangt veel brokken weg.</strong> Met zijn enorme massa trekt hij "
               "kometen en planetoïden naar zich toe of slingert ze het zonnestelsel uit. Zonder "
               "Jupiter zou de aarde vermoedelijk vaker geraakt worden."),
])

DWERGPLANETEN = dict(kop="Pluto, Ceres en de andere dwergplaneten", blokken=[
    ("p", "Sinds 2006 is <strong>Pluto geen planeet meer</strong>, en de reden is scherp: hij "
          "<strong>heeft zijn baan niet vrijgemaakt</strong>. Een planeet is groot genoeg om alles in "
          "haar omgeving opgeruimd of weggeslingerd te hebben; Pluto deelt zijn baan met duizenden "
          "andere ijsbrokken van de Kuipergordel. Hij is dus niet gekrompen en hij draait nog altijd "
          "rond de zon: enkel de afspraak over het woord planeet is veranderd."),
    ("p", "Een <strong>dwergplaneet</strong> is dus <strong>een bol die zijn baan niet vrij heeft</strong>. "
          "<strong>Ceres</strong> is de enige in de <strong>planetoïdengordel</strong> tussen Mars en "
          "Jupiter; <strong>Pluto</strong>, <strong>Eris</strong> en Makemake liggen alle drie "
          "<strong>voorbij Neptunus</strong>, in de Kuipergordel. Ook de <strong>kometen met een lange "
          "omloop</strong> komen van daar en van nog verder, uit de Oortwolk."),
])

zet("het-zonnestelsel-en-zijn-kleine-lichamen",
    "Het zonnestelsel en zijn kleine lichamen",
    "De zon en haar acht planeten, en wat er verder nog rondvliegt: planetoïden, dwergplaneten, "
    "kometen en meteorieten.",
    [
        sectie("de-zon-en-het-zonnestelsel", "De lagen van de zon"),
        sectie("de-zon-en-het-zonnestelsel", "De acht planeten"),
        PLANETEN_VERGELEKEN,
        sectie("de-zon-en-het-zonnestelsel", "Gordels, dwergplaneten en kometen"),
        DWERGPLANETEN,
        BROKSTUKKEN,
    ])


# ───────────────────── 4. De bewegingen van de aarde
ROTATIE_OF_REVOLUTIE = dict(kop="Hoort het bij de rotatie of bij de revolutie?", blokken=[
    ("p", "Veel vragen draaien om één onderscheid: komt dit van de aarde die om haar <strong>as</strong> "
          "draait, of van de aarde die rond de <strong>zon</strong> draait?"),
    ("p", tabel(["Bij de rotatie (24 uur)", "Bij de revolutie (365,25 dagen)"], [
        ["dag en nacht", "de seizoenen"],
        ["het <strong>corioliseffect</strong>", "de <strong>zonnewende</strong> en de <strong>nachtevening</strong>"],
        ["de <strong>uurgordels</strong>", "het <strong>eclipticavlak</strong>"],
        ["de <strong>datumgrens</strong>", "het <strong>perihelium</strong> en het <strong>aphelium</strong>"],
        ["de afplatting aan de polen", "de schrikkeldag"],
    ])),
    ("kader", "De <strong>seizoenen horen dus bij de revolutie</strong>, niet bij de rotatie. Dat is de "
              "val in bijna elke vraag over dit thema: de rotatie geeft dag en nacht, de revolutie met "
              "een <strong>scheve</strong> as geeft de seizoenen."),
])

KLOK_EN_TIJD = dict(kop="Rekenen met de klok", blokken=[
    ("p", "De aarde heeft <strong>24 uurgordels</strong> van elk 15 graden lengte. Reis je naar het "
          "<strong>oosten</strong>, dan gaat de <strong>klok vooruit</strong>; naar het westen gaat ze "
          "achteruit."),
    ("p", "<strong>In België loopt de klok in de winter gelijk met de zonnetijd van de "
          "nulmeridiaan.</strong> Onze wintertijd is immers precies die van Greenwich, hoewel we op "
          "ongeveer 4 à 5 graden oosterlengte liggen. In de lente zetten we de klok een uur "
          "<strong>vooruit</strong>, niet achteruit, en dan lopen we een uur voor op Greenwich."),
    ("p", "Een voorbeeld dat vaak terugkomt: is het in <strong>Brussel</strong> twaalf uur in de "
          "winter, dan is het in <strong>New York zes uur in de ochtend</strong>. New York ligt zes "
          "uurgordels westelijker, en het westen loopt achter."),
])

DE_ZON_OP_JE_HELLING = dict(kop="Waarom de hoek van de zon alles bepaalt", blokken=[
    ("p", "<strong>Hoe steiler de zonnestralen invallen, hoe meer ze een oppervlak opwarmen.</strong> "
          "Staat de zon laag, dan verdeelt dezelfde bundel licht zich over een veel groter stuk grond, "
          "en wordt elke vierkante meter dus minder warm. Dat is de enige reden die je nodig hebt om de "
          "seizoenen, de klimaatgordels en zelfs het verschil tussen een zuid- en een noordhelling te "
          "begrijpen."),
    ("p", "Daaruit volgt ook waarom het <strong>aan de evenaar het hele jaar warm</strong> is: de zon "
          "staat er <strong>altijd hoog</strong>. Niet omdat de evenaar dichter bij de zon ligt, en niet "
          "omdat de dagen er langer zijn: die duren er net het hele jaar ongeveer twaalf uur."),
    ("p", tabel(["Klimaatgordel", "Waar"], [
        ["de <strong>tropische</strong>", "tussen de twee keerkringen"],
        ["de <strong>gematigde</strong>", "<strong>tussen de keerkring en de poolcirkel</strong>"],
        ["de <strong>polaire</strong>", "voorbij de poolcirkel"],
    ])),
    ("p", "De <strong>poolnacht</strong> is <strong>een etmaal waarop de zon niet opkomt</strong>. Op de "
          "<strong>Noordpool is de daglengte op 22 december dus nul uur</strong>, en op 21 juni "
          "vierentwintig uur. Bij ons in Hasselt zijn dag en nacht alleen rond 21 maart en 23 september "
          "even lang: op 21 juni duurt de dag bijna zestien uur en is de nacht veel korter."),
])

zet("de-bewegingen-van-de-aarde",
    "De bewegingen van de aarde",
    "De rotatie en haar gevolgen, de uurgordels, en de scheve as die ons de seizoenen geeft.",
    [
        sectie("de-bewegingen-van-de-aarde", "De rotatie: de aarde draait om haar as"),
        sectie("de-bewegingen-van-de-aarde", "Het corioliseffect", extra=[
            ("p", "Het corioliseffect bepaalt ook hoe een <strong>depressie</strong> draait. Op het "
                  "<strong>noordelijk halfrond</strong> draait de wind rond een lagedrukgebied "
                  "<strong>tegen de klok in</strong>, dus niet met de klok mee; rond een hogedrukgebied "
                  "draait hij met de klok mee."),
        ]),
        sectie("de-bewegingen-van-de-aarde", "Uurgordels en de datumgrens"),
        KLOK_EN_TIJD,
        sectie("de-bewegingen-van-de-aarde", "Dezelfde parallel, dezelfde zon"),
        sectie("de-bewegingen-van-de-aarde", "De revolutie: de aarde draait rond de zon"),
        sectie("de-bewegingen-van-de-aarde", "De schuine as en de seizoenen"),
        sectie("de-bewegingen-van-de-aarde", "Van de tropen tot de poolnacht"),
        DE_ZON_OP_JE_HELLING,
        ROTATIE_OF_REVOLUTIE,
    ])


# ───────────────────── 5. De atmosfeer en de temperatuur op aarde
ZEE_OF_LAND = dict(kop="Zeeklimaat, landklimaat en de kleine schaal", blokken=[
    ("p", "<strong>Water warmt trager op en koelt trager af dan land.</strong> Daarmee verklaar je "
          "bijna alles over temperatuur in onze streken."),
    ("p", tabel(["Klimaat", "Waar", "Hoe het voelt"], [
        ["<strong>maritiem</strong> of zeeklimaat",
         "dicht bij de zee, zoals Oostende",
         "kleine verschillen: koelere zomer, zachtere winter"],
        ["<strong>continentaal</strong> of landklimaat",
         "ver in het binnenland, zoals Moskou",
         "hete zomers en strenge winters"],
    ])),
    ("p", "Daarom is het in <strong>Oostende</strong> in juli <strong>koeler dan in Hasselt</strong>: "
          "de zee koelt de lucht af. En daarom wordt de jaarschommeling van de temperatuur klein als je "
          "<strong>dicht bij de zee</strong> ligt, <strong>dicht bij de evenaar</strong> ligt of een "
          "<strong>warme zeestroom langs je kust</strong> hebt. Ver in het binnenland liggen doet net "
          "het omgekeerde. Van twee steden op dezelfde breedte heeft een <strong>kuststad in "
          "Ierland</strong> dus de zachtste winter, zachter dan een stad midden in Rusland, in het "
          "binnenland van Canada of hoog in de bergen."),
    ("p", "Op kleine schaal werken nog drie dingen mee. Een <strong>zuidhelling</strong> is in België "
          "warmer dan een noordhelling, <strong>omdat de zon er steiler op valt</strong>. Een "
          "<strong>bewolkte nacht is zachter dan een heldere nacht</strong>, want de wolken houden de "
          "uitgestraalde warmte vast, dus niet kouder. En de <strong>hoogste temperatuur van de dag "
          "valt niet om twaalf uur</strong> maar in de namiddag, omdat <strong>de grond eerst moet "
          "opwarmen</strong> voordat hij de lucht verwarmt."),
    ("p", "Een <strong>temperatuurinversie</strong> is de omkering van het gewone beeld: "
          "<strong>koude lucht onder warme lucht</strong>. Dat gebeurt op een heldere winternacht in "
          "een vallei, en dan blijven mist en vuile lucht er hangen."),
    ("kader", "In de <strong>Sahara</strong> is het 's nachts vaak koud, en de reden is "
              "<strong>droogte</strong>: er zit <strong>geen waterdamp in de lucht</strong> om de warmte "
              "vast te houden, dus straalt de hitte 's nachts weg. Om dezelfde reden liggen de "
              "<strong>hoogste gemeten temperaturen op aarde niet op de evenaar</strong> maar in de "
              "woestijnen rond de keerkringen: op de evenaar hangen wolken en valt regen."),
])

TEMPERATUUR_KAART = dict(kop="Isothermen lezen", blokken=[
    ("p", "<strong>Isothermen</strong> verbinden op een kaart de plaatsen met <strong>dezelfde "
          "temperatuur</strong>. Twee dingen lees je eraan af."),
    ("p", "Liggen de isothermen <strong>dicht bij elkaar</strong>, dan <strong>verandert de "
          "temperatuur snel</strong> over een korte afstand. Liggen ze ver uit elkaar, dan is het "
          "overal ongeveer even warm."),
    ("p", "En hun <strong>richting</strong> verraadt het seizoen. In <strong>juli</strong> lopen de "
          "isothermen over Europa ongeveer <strong>oost-west</strong>, netjes met de breedte mee. In "
          "<strong>januari</strong> lopen ze veel meer <strong>noord-zuid</strong>, want dan is de zee "
          "in het westen zacht en het binnenland in het oosten ijskoud: het verschil tussen oost en "
          "west is dan groter dan dat tussen noord en zuid."),
    ("kader", "In de troposfeer daalt de temperatuur met <strong>ongeveer zes graden per "
              "kilometer</strong> hoogte. Daarom is het op een berg kouder dan in de vallei, hoewel je "
              "er iets dichter bij de zon zit: <strong>de lucht is er dunner en houdt de warmte "
              "minder vast</strong>. Die paar kilometer naar de zon toe stellen niets voor naast 150 "
              "miljoen kilometer."),
])

zet("de-atmosfeer-en-de-temperatuur-op-aarde",
    "De atmosfeer en de temperatuur op aarde",
    "De lagen van de atmosfeer, waar de lucht uit bestaat, en wat de temperatuur van een plaats bepaalt.",
    [
        sectie("de-opbouw-van-de-atmosfeer", "De lagen, van beneden naar boven"),
        sectie("de-opbouw-van-de-atmosfeer", "Waar de lucht uit bestaat"),
        sectie("de-opbouw-van-de-atmosfeer", "Ozon: nuttig boven, schadelijk beneden"),
        sectie("de-opbouw-van-de-atmosfeer", "De stralingsbalans en het albedo"),
        sectie("de-opbouw-van-de-atmosfeer", "Wat de temperatuur van een plaats bepaalt"),
        ZEE_OF_LAND,
        sectie("de-opbouw-van-de-atmosfeer", "Isothermen en het hitte-eiland"),
        TEMPERATUUR_KAART,
    ])


# ───────────────────── 6. Luchtdruk, wind en de grote circulatie
STORM = dict(kop="Van zuidwestenwind tot orkaan", blokken=[
    ("p", "Een wind wordt genoemd naar <strong>waar hij vandaan komt</strong>, niet naar waarheen hij "
          "waait. Een <strong>zuidwestenwind</strong> komt dus uit het zuidwesten, en dat is bij ons de "
          "meest voorkomende wind: hij <strong>komt over de oceaan</strong>, <strong>brengt zachte "
          "lucht</strong> mee en <strong>brengt vaak regen</strong>."),
    ("p", "De <strong>windkracht</strong> geeft men op de schaal van <strong>Beaufort</strong>, van 0 "
          "(windstil) tot 12 (orkaankracht)."),
    ("p", "Een <strong>orkaan</strong> of <strong>tropische cycloon</strong> is een storm die "
          "<strong>boven warm zeewater</strong> ontstaat: het water moet minstens 26 graden zijn, "
          "want de warme, vochtige lucht is de brandstof. In het <strong>oog</strong>, het midden van "
          "zo'n storm, is het <strong>bijna windstil</strong> en breekt de zon zelfs door, terwijl er "
          "rondom orkaankracht staat."),
    ("p", "Een stevige <strong>depressie</strong> bij ons brengt <strong>veel wind</strong>, "
          "<strong>veel bewolking</strong> en <strong>neerslag</strong>. <strong>Nachtvorst</strong> "
          "hoort daar niet bij: die krijg je juist bij hoge druk, als de hemel 's nachts opheldert."),
    ("kader", "De wind aan het aardoppervlak waait <strong>niet precies langs de isobaren</strong>. "
              "Hoog in de lucht doet hij dat bijna wel, maar aan de grond remt de wrijving hem af, en "
              "daardoor draait hij schuin naar het lage drukgebied toe."),
])

zet("luchtdruk-wind-en-de-grote-circulatie",
    "Luchtdruk, wind en de grote circulatie",
    "Hoge en lage druk, de drukgordels en de cellen van de aarde, en de winden die eruit volgen.",
    [
        sectie("luchtdruk-en-winden", "Wat luchtdruk is"),
        sectie("luchtdruk-en-winden", "Hoge en lage druk"),
        sectie("luchtdruk-en-winden", "De drukgordels van de aarde"),
        sectie("luchtdruk-en-winden", "Passaten, ITCZ en de straalstroom", extra=[
            ("p", "Elk halfrond heeft <strong>drie circulatiecellen</strong>: de "
                  "<strong>Hadleycel</strong> tussen de evenaar en de keerkring, de "
                  "<strong>Ferrelcel</strong> in onze breedten en de <strong>poolcel</strong> daarboven. "
                  "Een Coriolliscel bestaat niet; coriolis is een effect, geen cel. In de "
                  "<strong>Hadleycel</strong> <strong>stijgt warme lucht op</strong> aan de evenaar en "
                  "<strong>daalt ze koud neer</strong> boven de keerkring: dat is de opstijgende en de "
                  "dalende tak."),
            ("p", "De <strong>straalstroom</strong> zit <strong>hoog in de troposfeer</strong>, op "
                  "ongeveer tien kilometer, net waar lijnvliegtuigen vliegen. Omdat hij van west naar "
                  "oost waait, <strong>vliegt een vliegtuig van Brussel naar New York langer dan "
                  "terug</strong>: op de heenreis vliegt het <strong>tegen de straalstroom in</strong>, "
                  "op de terugreis duwt die mee."),
        ]),
        sectie("luchtdruk-en-winden", "Zeewind, landwind en moesson"),
        STORM,
    ])


# ───────────────────── 7. Water in de lucht en de neerslag
WATERVOORRAAD = dict(kop="Hoeveel water, en waar het zit", blokken=[
    ("p", "<strong>Bijna al het water op aarde is zout</strong>: het zoete water is maar ongeveer "
          "<strong>drie procent</strong> van het totaal. En van dat zoete water zit <strong>het meeste "
          "vast in ijs</strong>, op Antarctica en Groenland. Het water op aarde <strong>neemt niet elk "
          "jaar toe</strong>: het is altijd dezelfde voorraad die rondgaat."),
    ("p", "In die kringloop zitten meer stappen dan verdampen en regenen. <strong>Transpiratie</strong> "
          "is het water dat planten via hun <strong>bladeren</strong> laten verdampen, nadat hun wortels "
          "het uit de bodem haalden. <strong>Infiltratie</strong> is het <strong>insijpelen van "
          "regenwater in de bodem</strong>. Valt de regen op een <strong>verharde oprit</strong>, dan "
          "kan hij niet infiltreren en <strong>stroomt hij af naar de riool</strong>."),
    ("kader", "<strong>Verwering hoort niet bij de hydrologische cyclus.</strong> Verdamping, "
              "condensatie en neerslag wel; verwering is het afbrokkelen van gesteente, en dat is een "
              "ander verhaal."),
])

FRONTEN_EN_MOESSON = dict(kop="Fronten, moessons en waar de regen valt", blokken=[
    ("p", "Een <strong>front</strong> is de <strong>grens tussen twee luchtmassa's</strong> met een "
          "andere temperatuur en vochtigheid. Aan een <strong>warmtefront</strong> schuift "
          "<strong>de warme lucht</strong> over de koude heen en <strong>stijgt dus op</strong>; aan "
          "een koufront duwt de koude lucht de warme omhoog. In beide gevallen stijgt de warme lucht, "
          "en dus valt er regen. <strong>Bij ons komt de meeste neerslag van fronten uit het "
          "westen</strong>, meegevoerd door depressies over de oceaan."),
    ("p", "Een <strong>moesson</strong> is <strong>een wind die van seizoen omkeert</strong>: in de "
          "zomer van de koele zee naar het warme land, met zware regens, en in de winter andersom, "
          "droog. Het is dus geen storm en geen droogteperiode."),
    ("p", "De <strong>ITCZ</strong>, de zone waar de passaten samenkomen, is de plek waar "
          "<strong>convectieregens het hele jaar</strong> vallen. Daarom valt <strong>de meeste "
          "neerslag op aarde rond de evenaar</strong>."),
    ("p", tabel(["Droog gebied", "Waarom"], [
        ["de <strong>Sahara</strong>, de <strong>Kalahari</strong>, de woestijnen van <strong>Australië</strong>",
         "hoge luchtdruk: de lucht <strong>daalt er en warmt op</strong>, en dalende lucht geeft geen wolken"],
        ["het binnenland van <strong>Azië</strong>",
         "de <strong>zee ligt er heel ver weg</strong>, dus er komt geen vochtige lucht meer toe"],
        ["de <strong>polen</strong>",
         "zo koude lucht kan bijna geen waterdamp bevatten; het zijn <strong>droge</strong> gebieden, ondanks al het ijs"],
        ["de kust bij een <strong>koude zeestroom</strong>",
         "koud water geeft weinig verdamping, dus wordt die kust <strong>droger</strong> en niet natter"],
    ])),
    ("p", "Het <strong>Amazonewoud</strong> hoort niet in die lijst: daar stijgt de lucht juist op, en "
          "dus regent het er voortdurend. Zakt lucht over een bergketen weer naar beneden, dan "
          "<strong>warmt ze op en droogt ze uit</strong>: dat is de reden voor de regenschaduw achter "
          "elke bergrug."),
    ("kader", "In <strong>België</strong> valt gemiddeld ongeveer <strong>800 millimeter</strong> "
              "neerslag per jaar, en die is over alle maanden verdeeld: <strong>bij ons valt de meeste "
              "regen niet in de zomer</strong>, de herfst en de winter zijn natter. In de "
              "<strong>Ardennen</strong> valt wel meer dan in Limburg, want <strong>de lucht moet daar "
              "omhoog</strong> over het hoogland."),
])

zet("water-in-de-lucht-en-de-neerslag",
    "Water in de lucht en de neerslag",
    "De kringloop van het water, hoe een wolk ontstaat, de soorten neerslag en wat de regen over de "
    "aarde verdeelt.",
    [
        sectie("neerslag-en-de-kringloop-van-het-water", "De hydrologische cyclus"),
        WATERVOORRAAD,
        sectie("neerslag-en-de-kringloop-van-het-water", "Vochtigheid, dauwpunt en wolken"),
        sectie("neerslag-en-de-kringloop-van-het-water", "Neerslag meten"),
        sectie("neerslag-en-de-kringloop-van-het-water", "Drie soorten regen"),
        sectie("neerslag-en-de-kringloop-van-het-water", "Wat de neerslag op aarde verdeelt"),
        FRONTEN_EN_MOESSON,
    ])


# ───────────────────── 8. Klimaten, biomen en zeestromen
KLIMAATTYPES = dict(kop="De klimaattypes, en een klimatogram lezen", blokken=[
    ("p", "Een <strong>klimatogram</strong> toont <strong>twaalf</strong> maanden, één per maand van "
          "het jaar: de staven zijn de <strong>neerslag</strong>, de lijn is de "
          "<strong>temperatuur</strong>. Die twee samen zijn genoeg om het klimaat van een plaats te "
          "benoemen."),
    ("p", tabel(["Klimaat", "Waaraan je het herkent", "Waar"], [
        ["<strong>tropisch regenwoud</strong>", "warm en nat het hele jaar, vlakke temperatuurlijn",
         "rond de evenaar"],
        ["<strong>savanne</strong>", "<strong>een regenseizoen en een droog seizoen</strong>",
         "Afrika tussen woud en woestijn"],
        ["<strong>woestijn</strong>", "<strong>bijna geen neerslagstaven</strong>",
         "rond de keerkringen"],
        ["<strong>mediterraan</strong>", "<strong>droge, hete zomers</strong> en milde, natte winters",
         "Zuid-Spanje, Zuid-Italië, Griekenland"],
        ["<strong>gematigd zeeklimaat</strong>", "regen in alle maanden, kleine schommeling",
         "België, Ierland, de Britse eilanden"],
        ["<strong>gematigd landklimaat</strong>", "grote schommeling, hete zomer, strenge winter",
         "Polen, Rusland"],
        ["<strong>poolklimaat</strong>", "koud het hele jaar, <strong>weinig neerslag</strong>",
         "voorbij de poolcirkel"],
        ["<strong>hooggebergteklimaat</strong>", "<strong>koud door de hoogte</strong>, niet door de breedte",
         "de Alpen, de Andes"],
    ])),
    ("p", "<strong>Zuid-Zweden</strong> heeft dus géén mediterraan klimaat, en een "
          "<strong>poolklimaat is geen nat gebied</strong>: er ligt veel ijs, maar er valt bijna geen "
          "neerslag. Een temperatuurlijn die <strong>nauwelijks schommelt</strong>, betekent dat de "
          "plaats <strong>dicht bij de evenaar</strong> ligt; midden in een continent schommelt ze juist "
          "sterk."),
    ("p", "De indeling van <strong>Köppen</strong> geeft elk klimaat een letter. De "
          "<strong>tropische klimaten krijgen de letter A</strong>, de droge B, de gematigde C, de "
          "koude landklimaten D en de poolklimaten E."),
    ("p", "<strong>België heeft een gematigd zeeklimaat.</strong> Daarom staan in een klimatogram van "
          "<strong>Oostende de neerslagstaven in juli lager dan in december</strong>: onze zomer is "
          "niet onze natste maand. In <strong>Madrid</strong> is het <strong>droger dan bij ons</strong>, "
          "zijn <strong>de zomers heet</strong> en ligt de stad <strong>ver van de zee</strong>; er valt "
          "er dus minder regen dan in Bergen, de natste stad van Noorwegen. En <strong>Moskou</strong> "
          "is in januari veel kouder dan Londen omdat het <strong>ver van de oceaan</strong> ligt, niet "
          "omdat het noordelijker of hoger ligt."),
    ("kader", "Een klimatogram van het <strong>zuidelijk halfrond</strong> heeft zijn "
              "<strong>warmste maanden aan de rand van de grafiek</strong>, bij januari en december, "
              "en zijn koudste in het midden. Op het noordelijk halfrond is het net omgekeerd."),
])

BIOOM_BIJ_KLIMAAT = dict(kop="Welk bioom bij welk klimaat", blokken=[
    ("p", "Een <strong>bioom</strong> is <strong>een groot gebied met eigen plant- en "
          "diergroepen</strong>, bepaald door het klimaat. Bij ons gematigd zeeklimaat hoort het "
          "<strong>loofbos</strong>."),
    ("p", "Onze bomen <strong>verliezen in de winter hun blad om water en energie te sparen</strong>: "
          "met een bevroren bodem kunnen de wortels weinig water opnemen, en bladeren verdampen water. "
          "Het is dus geen kwestie van te zwaar worden of geen licht meer nodig hebben."),
    ("p", "De <strong>taiga</strong> is het naaldbos van <strong>Siberië en Canada, net onder de "
          "toendra</strong>. In de <strong>toendra</strong> groeien geen bomen, en de reden is de "
          "<strong>bevroren bodem</strong>: de <strong>permafrost</strong> blijft het hele jaar "
          "bevroren, dus kan een wortel er niet in. Het <strong>tropisch regenwoud</strong> heeft de "
          "<strong>grootste verscheidenheid aan soorten</strong> van alle biomen. Een "
          "<strong>hooiland</strong> is géén bioom maar een stuk landbouwgrond."),
])

ZEESTROMEN_EXTRA = dict(kop="Wat een zeestroom doet met een kust", blokken=[
    ("p", "<strong>Zeestromen</strong> zijn <strong>grote waterstromen in de oceaan</strong>, niet de "
          "getijden en niet de golven. Ze verdelen de warmte over de aarde; zeggen dat ze daar geen "
          "invloed op hebben, is dus fout."),
    ("p", tabel(["Zeestroom", "Warm of koud", "Waar"], [
        ["de <strong>Golfstroom</strong>", "warm", "uit de Golf van Mexico"],
        ["de <strong>Noord-Atlantische Drift</strong>", "warm", "het verlengde ervan, langs West-Europa"],
        ["de <strong>Labradorstroom</strong>", "koud", "langs Oost-Canada"],
        ["de <strong>Humboldtstroom</strong>", "koud", "langs Chili en Peru"],
        ["de <strong>Benguelastroom</strong>", "koud", "langs Namibië"],
    ])),
    ("p", "Daarom is het in <strong>Noorwegen</strong> in de winter zachter dan in Canada op dezelfde "
          "breedte: <strong>er loopt een warme zeestroom langs</strong>. Een zeestroom bepaalt mee de "
          "<strong>temperatuur</strong>, de <strong>neerslag</strong> en de <strong>bewolking</strong> "
          "van een kust; de breedteligging bepaalt hij natuurlijk niet, die ligt vast."),
    ("p", "Bij een <strong>koude zeestroom hoort vaak een woestijn aan de kust</strong>: de Atacama bij "
          "de Humboldtstroom, de Namib bij de Benguelastroom. Koud water verdampt weinig, en de lucht "
          "erboven warmt van onderen niet op, dus stijgt ze niet en regent het niet."),
    ("p", "De <strong>rijkste visgronden</strong> liggen <strong>waar koud water opwelt</strong>: dat "
          "water brengt voedingsstoffen van de diepte mee naar boven. En een <strong>warme zeestroom is "
          "niet altijd een snelle zeestroom</strong>: temperatuur en snelheid zijn twee verschillende "
          "dingen."),
])

zet("klimaten-biomen-en-zeestromen",
    "Klimaten, biomen en zeestromen",
    "Weer tegenover klimaat, de klimaattypes op een klimatogram, de biomen die erbij horen, en de "
    "zeestromen die het beeld verschuiven.",
    [
        sectie("klimaatgebieden-biomen-en-zeestromen", "Weer en klimaat"),
        KLIMAATTYPES,
        sectie("klimaatgebieden-biomen-en-zeestromen", "De biomen"),
        BIOOM_BIJ_KLIMAAT,
        sectie("klimaatgebieden-biomen-en-zeestromen", "Zeestromen"),
        ZEESTROMEN_EXTRA,
        sectie("klimaatgebieden-biomen-en-zeestromen", "De thermohaliene circulatie"),
    ])


# ───────────────────── 9. De bouw van de aarde en de platentektoniek
zet("de-bouw-van-de-aarde-en-de-platentektoniek",
    "De bouw van de aarde en de platentektoniek",
    "De lagen van de aarde en hoe we ze kennen, en de platen die erover schuiven.",
    [
        sectie("de-opbouw-van-de-geosfeer", "De chemische indeling: korst, mantel en kern", extra=[
            ("p", "Het midden van de aarde ligt ongeveer <strong>6370 kilometer</strong> diep. De "
                  "<strong>mantel</strong> is daarvan <strong>de dikste laag</strong>: hij "
                  "<strong>bestaat uit vast gesteente</strong> dat <strong>heel traag kan "
                  "vloeien</strong>, als stroop. De <strong>zwaarste</strong> laag is hij niet; dat is "
                  "de kern, van ijzer en nikkel. Hoe dieper je gaat, hoe <strong>hoger de "
                  "temperatuur</strong>."),
            ("kader", "Op schaal is de korst <strong>dunner</strong> dan de schil van een appel, niet "
                      "dikker: tegenover 6370 kilometer is een korst van 10 tot 70 kilometer bijna "
                      "niets. En de mantel is <strong>geen zee van vloeibare lava</strong>; magma zit "
                      "alleen in plaatselijke kamers."),
            ("p", "Het <strong>magneetveld</strong> van de aarde komt van de <strong>stromingen in de "
                  "vloeibare buitenkern</strong>: bewegend, geleidend ijzer wekt het op. Niet van de "
                  "ijzerertsen in de korst, en niet van de maan."),
        ]),
        sectie("de-opbouw-van-de-geosfeer", "De fysische indeling: lithosfeer en asthenosfeer"),
        sectie("de-opbouw-van-de-geosfeer", "Hoe we dat weten: seismische golven"),
        sectie("de-opbouw-van-de-geosfeer", "Twee soorten korst"),
        sectie("de-opbouw-van-de-geosfeer", "Isostasie"),
        sectie("platentektoniek-en-reliefvorming", "Pangea en de drift van de continenten", extra=[
            ("p", "<strong>Alfred Wegener</strong> bedacht als eerste, rond 1912, dat de continenten "
                  "bewogen hebben. Zijn sterkste argument lag voor het grijpen: de "
                  "<strong>vorm</strong> van de kustlijnen van Afrika en Zuid-Amerika past als een "
                  "<strong>puzzel</strong> in elkaar. Daarbij kwamen dezelfde fossielen en dezelfde "
                  "gesteentelagen aan weerszijden van de oceaan. <strong>Gondwana</strong> is de naam "
                  "van het zuidelijke deel van Pangea; een riftster en een isotherm hebben met "
                  "plaatbewegingen niets te maken."),
            ("kader", "De platen bewegen <strong>enkele centimeter per jaar</strong>, niet een meter: "
                      "ongeveer zo snel als je nagels groeien. Over miljoenen jaren wordt dat wel een "
                      "oceaan breed."),
        ]),
        sectie("platentektoniek-en-reliefvorming", "Wat de platen beweegt"),
        sectie("platentektoniek-en-reliefvorming", "Drie soorten plaatbeweging"),
        sectie("platentektoniek-en-reliefvorming", "Mantelpluimen en hotspots"),
        sectie("platentektoniek-en-reliefvorming", "Het reliëf van de oceaanbodem"),
        sectie("platentektoniek-en-reliefvorming", "Plooien, slenken en gebergten"),
        sectie("platentektoniek-en-reliefvorming", "Vulkanen en aardbevingen tekenen de platen uit"),
    ])


# ───────────────────── 10. Vulkanen en aardbevingen
CALDERA_EN_SCHALEN = dict(kop="Caldera, Ring of Fire en de schalen", blokken=[
    ("p", "Een <strong>caldera</strong> is <strong>een ingestorte vulkaankrater</strong>: na een zware "
          "uitbarsting is de magmakamer leeg, en het dak zakt erin. Zo ontstaat een ketel van "
          "kilometers breed, soms met een meer erin."),
    ("p", "De <strong>Ring of Fire</strong> is de kring van vulkanen rond de <strong>Stille "
          "Oceaan</strong>, waar de ene plaat na de andere wegduikt. De <strong>Vesuvius</strong> ligt "
          "in Italië, <strong>bij Napels</strong>; de Etna ligt op Sicilië, de Fuji in Japan en de "
          "Krakatau in Indonesië."),
    ("p", tabel(["Schaal", "Wat ze meet"], [
        ["de schaal van <strong>Richter</strong>", "de kracht van de beving zelf, uit de uitslag van de seismograaf"],
        ["de <strong>momentmagnitudeschaal</strong>", "dezelfde kracht, nauwkeuriger bij zware bevingen; die wordt vandaag gebruikt"],
        ["de schaal van <strong>Mercalli</strong>", "de <strong>schade</strong> en wat mensen voelden, van I tot XII"],
    ])),
    ("p", "De schaal van <strong>Beaufort</strong> hoort daar niet bij: die is voor windkracht. Over "
          "Richter geldt: een <strong>2 voel je niet</strong>, <strong>elke eenheid is tien keer "
          "meer</strong> uitslag, en <strong>schade begint rond een 5</strong>. De schaal "
          "<strong>stopt niet bij een 10</strong>: er is geen bovengrens, het gesteente zelf begrenst "
          "hem. De grafiek die een seismograaf tekent, heet een <strong>seismogram</strong>."),
])

RISICO_EN_SCHADE = dict(kop="Wat je ertegen doet, en wat je niet kan", blokken=[
    ("p", "In <strong>Japan</strong> staan huizen en bruggen op <strong>rubberen blokken</strong> en "
          "veren. Dat is geen isolatie en geen besparing: het gebouw kan daardoor "
          "<strong>meebewegen met de bodem</strong> in plaats van te breken. Om dezelfde reden gaan "
          "<strong>zwakke huizen het eerst stuk</strong>: ze <strong>kunnen niet meebewegen</strong>."),
    ("p", "Langs bergwegen hangen <strong>netten tegen de wand</strong> om <strong>afstortend puin "
          "tegen te houden</strong>."),
    ("p", "<strong>Aardbevingen kan men niet op dag en uur voorspellen</strong>, en dat komt niet door "
          "te zwakke toestellen: <strong>de spanning in het gesteente breekt onvoorspelbaar</strong>. "
          "Men weet wel heel goed wáár ze zullen gebeuren, en men bouwt daarop. Ook "
          "<strong>in België komen aardbevingen voor</strong>, zij het lichte: de breukzone van de "
          "Roerdalslenk loopt onder Limburg door, en in 1992 was er bij Roermond een beving van 5,8 "
          "die ook hier schade gaf."),
    ("p", "<strong>Vulkanische as is gevaarlijk voor vliegtuigen</strong> omdat ze "
          "<strong>in de motoren smelt</strong> en daar als glas vastkoekt. Daarom sluit men het "
          "luchtruim bij een aswolk. En <strong>een grote uitbarsting kan het klimaat van de hele "
          "aarde een paar jaar afkoelen</strong>: de zwavel hoog in de stratosfeer weerkaatst het "
          "zonlicht."),
    ("p", "Een <strong>lahar</strong> is <strong>een modderstroom van as en water</strong>, vaak "
          "smeltend sneeuw of gletsjerijs vermengd met verse as. Hij stroomt sneller dan lava en is "
          "daarom vaak dodelijker."),
])

TSUNAMI = dict(kop="Van beving tot tsunami", blokken=[
    ("p", "Een <strong>tsunami</strong> ontstaat doordat <strong>de zeebodem plots omhoog schokt</strong> "
          "bij een beving onder zee, en de hele waterkolom erboven meeneemt. Wind, maan of een schip "
          "hebben er niets mee te maken."),
    ("p", "<strong>Midden op de oceaan is een tsunami géén hoge golf</strong>: daar is hij misschien een "
          "halve meter hoog, maar honderden kilometer lang, en hij haalt de snelheid van een "
          "vliegtuig. Pas in ondiep water loopt hij op tot een muur van water."),
    ("kader", "Het <strong>voorteken</strong> aan de kust is dat <strong>de zee zich plots "
              "terugtrekt</strong>, veel verder dan bij eb. Wie dat ziet, heeft enkele minuten om "
              "hoger te klimmen. Ga dus nooit kijken naar de droge zeebodem."),
    ("p", "Een <strong>naschok</strong> komt <strong>na de hoofdschok en is meestal zwakker</strong>, "
          "maar hij kan al beschadigde gebouwen alsnog doen instorten. Een aardbeving kan verder "
          "<strong>gebouwen doen instorten</strong>, een <strong>tsunami</strong> veroorzaken en "
          "<strong>aardverschuivingen</strong> op gang brengen; een uitdijend heelal hoort daar "
          "natuurlijk niet bij."),
])

zet("vulkanen-en-aardbevingen",
    "Vulkanen en aardbevingen",
    "Waar een beving begint en hoe je haar meet, wat een vulkaan uitwerpt, en hoe mensen met het "
    "risico leven.",
    [
        sectie("aardbevingen-en-vulkanisme", "Waar een beving begint"),
        sectie("aardbevingen-en-vulkanisme", "De kracht meten"),
        CALDERA_EN_SCHALEN,
        sectie("aardbevingen-en-vulkanisme", "Wat een beving aanricht"),
        TSUNAMI,
        sectie("aardbevingen-en-vulkanisme", "Magma, lava en de delen van een vulkaan"),
        sectie("aardbevingen-en-vulkanisme", "Twee soorten vulkanen"),
        sectie("aardbevingen-en-vulkanisme", "Wat een vulkaan uitwerpt", extra=[
            ("p", "De brokken worden benoemd naar hun grootte. <strong>As</strong> is het fijnste, "
                  "<strong>lapilli</strong> zijn de steentjes van 2 tot 64 millimeter, en de brokken "
                  "<strong>groter dan vierenzestig millimeter</strong> die een vulkaan wegslingert heten "
                  "<strong>vulkanische bommen</strong>. <strong>Lapilli zijn dus niet de grootste "
                  "brokken</strong> maar de middelste."),
            ("kader", "<strong>Een vulkaan die duizend jaar niet uitbrak, is niet zeker gedoofd.</strong> "
                      "Een vulkaan heet <em>gedoofd</em> ("
                      "<em>extinct</em>) pas als er geen magma meer onder zit; daartussen ligt "
                      "<em>sluimerend</em>. De Vesuvius zweeg eeuwen en begroef in 79 na Christus "
                      "Pompeï."),
        ]),
        sectie("aardbevingen-en-vulkanisme", "Toch wonen op een vulkaan"),
        RISICO_EN_SCHADE,
    ])


# ───────────────────── 11. Gesteenten en de geologische tijd
LITHOLOGIE = dict(kop="Lithologie: de taal van de gesteenten", blokken=[
    ("p", "<strong>Lithologie</strong> is <strong>de studie van gesteenten</strong>: waaruit ze "
          "bestaan, hoe ze ontstonden en hoe je ze benoemt. Een paar woorden heb je daarvoor nodig."),
    ("p", tabel(["Woord", "Wat het betekent"], [
        ["<strong>diagenese</strong>",
         "het <strong>samenpersen en verkitten van losse deeltjes tot gesteente</strong>; zo wordt zand zandsteen"],
        ["<strong>dagzomen</strong>",
         "<strong>aan de oppervlakte komen</strong>: een laag die je zonder te graven kan zien"],
        ["<strong>intrusie</strong>",
         "<strong>magma dat in oudere lagen dringt</strong> en daar afkoelt"],
        ["<strong>breuk</strong>",
         "een <strong>scheur in de ondergrond waarlangs lagen verschoven</strong> zijn"],
        ["een <strong>stratigrafische kaart</strong>",
         "een kaart die toont <strong>welke lagen waar dagzomen</strong>, niet hoe hoog het reliëf is"],
    ])),
    ("kader", "<strong>Diagenese hoort niet bij de processen die van gesteente los materiaal "
              "maken.</strong> Verwering, erosie en transport doen dat; diagenese doet net het "
              "omgekeerde en maakt van los materiaal weer gesteente."),
])

BELGIE_ONDERGROND = dict(kop="De ondergrond van België, in de tijd", blokken=[
    ("p", "De gesteenten onder onze voeten zijn in heel verschillende tijden ontstaan, en de fiche "
          "verwacht dat je die twee niet verwart."),
    ("p", tabel(["Waar", "Wat", "Wanneer"], [
        ["de <strong>Kempen</strong>, in de diepte",
         "<strong>steenkool</strong>, uit plantenresten in moerassen",
         "het <strong>Carboon</strong>, ongeveer 310 miljoen jaar geleden"],
        ["de <strong>Maasvallei</strong> en de Ardennen",
         "<strong>kalksteen</strong>, uit schelpen en koraal in een warme, ondiepe zee",
         "vooral het <strong>Devoon</strong> en het Carboon"],
    ])),
    ("p", "<strong>De steenkool van Limburg en de kalksteen van de Maasvallei zijn dus niet in "
          "dezelfde tijd ontstaan</strong>, en ook niet in hetzelfde milieu: het ene in een moeras, "
          "het andere onder zee. Dat <strong>België onder een warme, ondiepe zee lag</strong>, geldt "
          "voor <strong>het Carboon en het Devoon</strong> — toen lag ons land trouwens bij de "
          "evenaar."),
    ("p", "De <strong>Ardennen</strong> zijn geplooid door de <strong>Hercynische</strong> plooiing, "
          "niet door de Alpiene. Van de drie plooiingen die de fiche noemt — de "
          "<strong>Caledonische</strong>, de <strong>Hercynische</strong> en de "
          "<strong>Alpiene</strong> — is de <strong>Alpiene de jongste, en die duurt nog voort</strong>: "
          "<strong>de Himalaya groeit nog altijd</strong>, een paar millimeter per jaar. Een "
          "Atlantische plooiing bestaat niet."),
])

GEOLOGISCHE_TIJD = dict(kop="De geologische tijdschaal", blokken=[
    ("p", "De <strong>geologische tijdschaal</strong> is <strong>de indeling van de geschiedenis van "
          "de aarde</strong>. Haar grenzen liggen niet op ronde getallen maar <strong>op grote "
          "veranderingen in het leven</strong>: op het moment dat veel soorten tegelijk verdwijnen of "
          "verschijnen. De aarde is ongeveer <strong>4,6 miljard jaar</strong> oud."),
    ("p", tabel(["Era", "Wanneer", "Waarvan ze de tijd is"], [
        ["het <strong>Precambrium</strong>", "4,6 miljard tot 541 miljoen jaar geleden", "eencellig leven, dan de eerste dieren"],
        ["het <strong>Paleozoïcum</strong>", "541 tot 252 miljoen jaar geleden", "vissen, de eerste landplanten, de steenkoolwouden"],
        ["het <strong>Mesozoïcum</strong>", "252 tot 66 miljoen jaar geleden", "de <strong>dinosauriërs</strong>"],
        ["het <strong>Cenozoïcum</strong>", "66 miljoen jaar geleden tot nu", "de <strong>zoogdieren</strong>, en helemaal achteraan de mens"],
    ])),
    ("p", "Het <strong>Holoceen</strong> is géén era maar een heel klein tijdvak binnen het "
          "Cenozoïcum: de laatste 11 700 jaar, sinds het einde van de laatste ijstijd. "
          "<strong>De mens bestaat dus niet sinds de tijd van de dinosauriërs</strong>: daar zit "
          "ruim 60 miljoen jaar tussen."),
    ("p", "Een <strong>massa-extinctie</strong> is <strong>het uitsterven van veel soorten "
          "tegelijk</strong>. De bekendste ligt op de grens van het Mesozoïcum en het Cenozoïcum: "
          "<strong>66 miljoen jaar geleden stierven de dinosauriërs uit</strong>. "
          "<strong>Pangea</strong> lag in één stuk <strong>rond het einde van het Paleozoïcum</strong>, "
          "en begon in het Mesozoïcum uiteen te vallen."),
    ("kader", "<strong>De oudste gesteenten van de oceaanbodem zijn nergens ouder dan ongeveer "
              "tweehonderd miljoen jaar</strong>, terwijl op de continenten gesteente van vier miljard "
              "jaar ligt. De reden is de platentektoniek: <strong>de oceaanbodem wordt steeds "
              "vernieuwd</strong>, aangemaakt aan de ruggen en weer weggeslikt in de trogen."),
])

DATEREN = dict(kop="Dateren: hoe oud is dit?", blokken=[
    ("p", "<strong>Relatieve datering</strong> is <strong>bepalen wat ouder of jonger is</strong>, "
          "zonder een getal. Absolute datering geeft wel een getal, in jaren, en werkt met het "
          "verval van radioactieve elementen."),
    ("p", "Een <strong>halveringstijd</strong> is <strong>de tijd waarin de helft van een "
          "radioactief element vervalt</strong>. <strong>Elk element heeft zijn eigen "
          "halveringstijd</strong>, en daarom reikt elke methode anders ver: ze reiken dus niet alle "
          "even ver terug."),
    ("p", tabel(["Methode", "Waarvoor", "Hoe ver terug"], [
        ["<strong>koolstof-14</strong>", "resten van <strong>hout en bot</strong>, alles wat geleefd heeft",
         "tot ongeveer <strong>50 000 jaar</strong>"],
        ["<strong>uranium-lood</strong>", "<strong>oud gesteente</strong>, kristallen in graniet",
         "tot miljarden jaren"],
    ])),
    ("p", "Een <strong>gidsfossiel</strong> is een soort die kort bestond en wijd verspreid was. "
          "<strong>Daarmee herken je lagen van dezelfde ouderdom</strong>, zelfs op verschillende "
          "continenten. En waarom je <strong>in graniet geen fossielen vindt</strong>: "
          "<strong>graniet ontstond uit magma</strong>, en in gesmolten gesteente blijft van een "
          "plant of dier niets over."),
])

zet("gesteenten-en-de-geologische-tijd",
    "Gesteenten en de geologische tijd",
    "De drie groepen gesteenten en hun kringloop, de lagen lezen, en de tijdschaal van de aarde.",
    [
        sectie("gesteenten-mineralen-en-datering", "Drie groepen"),
        LITHOLOGIE,
        sectie("gesteenten-mineralen-en-datering", "Magmatische gesteenten"),
        sectie("gesteenten-mineralen-en-datering", "Sedimentaire gesteenten"),
        sectie("gesteenten-mineralen-en-datering", "Metamorfe gesteenten"),
        sectie("gesteenten-mineralen-en-datering", "De gesteentecyclus"),
        sectie("gesteenten-mineralen-en-datering", "Relatieve datering: de lagen lezen"),
        sectie("gesteenten-mineralen-en-datering", "Fossielen"),
        DATEREN,
        sectie("gesteenten-mineralen-en-datering", "Absolute datering en de geologische tijdschaal"),
        GEOLOGISCHE_TIJD,
        sectie("gesteenten-mineralen-en-datering", "Gebergtevormingen"),
        BELGIE_ONDERGROND,
    ])


# ───────────────────── 12. Verwering en massatransport
zet("verwering-en-massatransport",
    "Verwering en massatransport",
    "Hoe gesteente ter plaatse uiteenvalt, wat kalksteen met water doet, en wat er met de "
    "zwaartekracht een helling afgaat.",
    [
        sectie("verwering-karst-en-massatransport", "Verwering, erosie, sedimentatie"),
        sectie("verwering-karst-en-massatransport", "Drie soorten verwering", extra=[
            ("p", "<strong>Zoutverwering</strong> is een vierde vorm die bij de fysische hoort: "
                  "<strong>zoutkristallen groeien in de poriën</strong> van het gesteente en wrikken het "
                  "van binnenuit open, net zoals ijs dat doet. Je ziet het langs de kust en in "
                  "woestijnen, waar zout water opstijgt en verdampt. Het zout lost het gesteente dus "
                  "niet op."),
        ]),
        sectie("verwering-karst-en-massatransport", "Karst", extra=[
            ("p", "Een <strong>zinkgat</strong> ontstaat <strong>als het dak van een ondergrondse holte "
                  "instort</strong>. Boven de grond zie je dan plots een ronde put, soms met een huis "
                  "of een weg erin. Dat is het duidelijkste teken dat er onder je voeten kalksteen is "
                  "weggelost."),
            ("p", "In <strong>België liggen de grotten in de Maasvallei en de Ardennen</strong>, waar "
                  "de kalksteen aan de oppervlakte komt: Han-sur-Lesse, Remouchamps, Dinant. In de "
                  "Kempen, aan de kust en in Haspengouw zit geen kalksteen in de ondergrond, dus "
                  "liggen er ook geen grotten."),
            ("p", "Dat <strong>regenwater licht zuur</strong> is, komt doordat het "
                  "<strong>koolstofdioxide uit de lucht opneemt</strong>. Dat beetje koolzuur is "
                  "genoeg om kalksteen langzaam weg te lossen, en daar komt heel het "
                  "<strong>karstlandschap</strong> met zijn <strong>zinkgaten</strong> en "
                  "<strong>verdwijnrivieren</strong> uit voort."),
        ]),
        sectie("verwering-karst-en-massatransport", "Massatransport"),
        sectie("verwering-karst-en-massatransport", "Wanneer gaat een helling schuiven"),
        sectie("verwering-karst-en-massatransport", "Wat mensen eraan doen, in beide richtingen"),
    ])


# ───────────────────── 13. Erosie door water, ijs en wind
RIVIERVORMEN = dict(kop="Van bron tot delta", blokken=[
    ("p", "Een rivier doet onderweg drie dingen: ze <strong>erodeert</strong>, ze "
          "<strong>transporteert</strong> en ze <strong>sedimenteert</strong>. Welke van de drie "
          "overheerst, hangt af van haar snelheid, en die hangt af van het verval."),
    ("p", tabel(["Vorm", "Wat het is", "Waar"], [
        ["een <strong>ravijn</strong>", "een <strong>diepe kerf van stromend water</strong> in een helling",
         "op steile, kale hellingen"],
        ["een <strong>kloofdal</strong>", "een nauw dal waar de rivier zich snel insnijdt in hard gesteente",
         "in de bovenloop"],
        ["een <strong>meander</strong>", "een bocht die zich uitholt aan de holle en opbouwt aan de bolle oever",
         "in de midden- en benedenloop"],
        ["een <strong>alluviale vlakte</strong>", "een vlakte van <strong>rivierafzettingen</strong>",
         "in de benedenloop"],
        ["een <strong>delta</strong>", "een vertakte monding vol eilandjes van afzetting",
         "waar de rivier in zee komt"],
    ])),
    ("p", "Een <strong>delta</strong> ontstaat doordat <strong>de rivier vertraagt en haar last "
          "afzet</strong>: in stil water blijft niets meer zweven. Om dezelfde reden zet een rivier bij "
          "een overstroming <strong>slib</strong> af op de vlakte: <strong>buiten de bedding gaat het "
          "water trager</strong>, en wat het niet meer kan dragen, zakt. Dat slib is precies waarom "
          "riviervlakten zo vruchtbaar zijn."),
    ("kader", "Het <strong>verval</strong> is het hoogteverschil per kilometer, en dat is in de "
              "<strong>bovenloop het grootst</strong>, niet in de middenloop. Het <strong>debiet</strong> "
              "is iets anders: <strong>de hoeveelheid water per seconde</strong>. Dat "
              "<strong>wisselt met het seizoen</strong>, en <strong>bij een hoog debiet erodeert een "
              "rivier meer</strong>."),
])

IJS_EN_WIND = dict(kop="Wat het ijs en de wind achterlaten", blokken=[
    ("p", "Een <strong>crevasse</strong> of gletsjerkloof is <strong>een spleet in het ijs</strong> "
          "zelf, die openscheurt waar de gletsjer over een bult of een bocht moet. Niet te verwarren "
          "met de <strong>gletsjerkrassen</strong>, de <strong>groeven in het gesteente</strong> eronder."),
    ("kader", "<strong>Het landijs van de laatste ijstijd bereikte België niet.</strong> Het stopte in "
              "Nederland, ongeveer ter hoogte van de grote rivieren; bij ons was het wel permafrost en "
              "toendra. De stuwwallen van Nijmegen en Arnhem zijn de randen van dat ijs. Zwerfkeien die "
              "je hier vindt, zijn meestal door rivieren of door mensen aangevoerd."),
    ("p", "De wind werkt vooral <strong>in droge gebieden met weinig plantengroei</strong>, want "
          "elders houdt de vegetatie het zand vast. Daarom <strong>plant men helmgras op de duinen</strong> "
          "aan onze kust: <strong>het houdt het zand vast</strong> met zijn lange wortels. Een "
          "<strong>duin ontstaat dus net waar de wind zand aanvoert en laat liggen</strong>, niet waar "
          "hij het wegblaast."),
    ("p", "<strong>Differentiële erosie</strong> betekent dat <strong>harde lagen blijven staan</strong> "
          "terwijl zachte wegslijten. Zo krijgt een <strong>paddenstoelrots</strong> zijn vorm, en zo "
          "steken in een landschap net de harde banken als richels boven het maaiveld uit."),
])

zet("erosie-door-water-ijs-en-wind",
    "Erosie door water, ijs en wind",
    "Wat een rivier van bron tot monding doet, welke vormen een gletsjer uitschuurt, en wat de wind "
    "in een droog gebied achterlaat.",
    [
        dict(kop="Drie erosievormen naast elkaar", blokken=[
            ("p", "De fiche noemt de <strong>erosievormen</strong> samen: het "
                  "<strong>massatransport</strong> door de zwaartekracht, de "
                  "<strong>watererosie</strong> door rivieren en regen, de <strong>glaciale "
                  "erosie</strong> door ijs en de winderosie. <strong>Chemische verwering</strong> "
                  "hoort daar niet bij: verweren is ter plaatse uiteenvallen, eroderen is weggevoerd "
                  "worden."),
            ("p", "Watererosie zie je ook op een akker bij ons: na een onweer staat er "
                  "<strong>een modderstroom op de weg</strong> onder een steile akker, want "
                  "<strong>het water neemt de bodem mee</strong>. Een vruchtbare bodem of een lage "
                  "ligging heeft er niets mee te maken; de helling en de kale grond hebben dat wel."),
        ]),
        sectie("erosie-door-water-ijs-en-wind", "Het stroombekken"),
        sectie("erosie-door-water-ijs-en-wind", "Boven-, midden- en benedenloop"),
        RIVIERVORMEN,
        sectie("erosie-door-water-ijs-en-wind", "Transport en het Hjülströmdiagram"),
        sectie("erosie-door-water-ijs-en-wind", "Meanders en differentiële erosie"),
        sectie("erosie-door-water-ijs-en-wind", "Overstromen"),
        sectie("erosie-door-water-ijs-en-wind", "Wat een gletsjer achterlaat"),
        sectie("erosie-door-water-ijs-en-wind", "De wind"),
        IJS_EN_WIND,
    ])


# ───────────────────── 14. De huidige klimaatverandering
GEVOLGEN_DICHTBIJ = dict(kop="Wat je er zelf van ziet, en wat je zelf kan doen", blokken=[
    ("p", "<strong>Lachgas</strong> hoort bij de broeikasgassen die de fiche noemt, naast "
          "koolstofdioxide en methaan. Het komt vooral van <strong>kunstmest op de akkers</strong>. "
          "<strong>Stikstof</strong> is géén broeikasgas, hoewel het bijna heel onze lucht vult: het "
          "houdt geen warmtestraling tegen."),
    ("p", "De <strong>koolstofvoetafdruk</strong> van een gezin is <strong>de uitstoot die het "
          "veroorzaakt</strong>, alles meegerekend: verwarming, auto, vliegtuig, voeding en spullen. "
          "Wat een gezin zelf kan doen, is vooral <strong>minder vliegen en minder vlees eten</strong>, "
          "en zijn huis beter isoleren."),
    ("p", tabel(["Gevolg", "Waarom"], [
        ["het <strong>noordpoolgebied warmt sneller op</strong> dan de rest",
         "<strong>smeltend ijs maakt het oppervlak donker</strong>, en donker water neemt meer warmte op"],
        ["een <strong>koraalrif verbleekt en sterft af</strong>",
         "bij te warm water stoot de koraalpoliep zijn algen uit, en die geven hem zijn kleur én zijn voedsel"],
        ["<strong>arme landen worden harder getroffen</strong>",
         "ze <strong>kunnen zich minder goed beschermen</strong>: minder geld voor dijken, irrigatie en "
         "verzekeringen, terwijl ze zelf het minst uitstootten"],
        ["<strong>België</strong> voelt <strong>meer hittegolven</strong>, <strong>drogere zomers</strong> "
         "en <strong>zwaardere buien</strong>",
         "warmere lucht houdt meer waterdamp vast, dus valt de regen in kortere, zwaardere buien"],
    ])),
    ("p", "<strong>Smeltend zeeijs op de Noordpool doet de zeespiegel niet stijgen</strong>: dat ijs "
          "drijft al in het water en verplaatst zijn eigen gewicht. Het landijs van Groenland en "
          "Antarctica doet dat wél, en daar komt de uitzetting van opwarmend zeewater bij."),
    ("p", "Het <strong>hitte-eilandeffect</strong> is dat <strong>een stad warmer is dan het "
          "platteland</strong>, 's nachts nog meer dan 's dags. Het geeft <strong>warmere "
          "nachten</strong>, <strong>meer gezondheidsklachten</strong> en <strong>meer koeling "
          "nodig</strong>; met luchtvervuiling heeft het niets te maken, en die wordt er niet minder "
          "van. Een <strong>groene stad is koeler omdat planten water verdampen</strong>, en verdampen "
          "kost warmte."),
    ("kader", "<strong>Een windmolen bouwen gebeurt niet helemaal zonder uitstoot.</strong> Staal, "
              "beton en transport kosten energie. Een windmolen verdient die uitstoot wel terug, "
              "gewoonlijk binnen het jaar, en draait daarna twintig jaar bijna uitstootvrij. Daarom "
              "<strong>hoort windmolens bouwen op zee niet bij de oorzaken</strong> van meer "
              "broeikasgassen, maar bij de oplossingen."),
])

zet("de-huidige-klimaatverandering",
    "De huidige klimaatverandering",
    "Het versterkt broeikaseffect, wat we meten, hoe we weten dat het de mens is, en wat mitigatie en "
    "adaptatie betekenen.",
    [
        sectie("de-huidige-klimaatverandering", "Het broeikaseffect"),
        sectie("de-huidige-klimaatverandering", "Wat we nu al meten"),
        sectie("klimaat-doorheen-de-geologische-tijd", "Het klimaat is altijd veranderd", extra=[
            ("p", "<strong>Het grote verschil met de klimaatveranderingen uit het verleden is de "
                  "snelheid van de verandering.</strong> Wat vroeger duizenden jaren duurde, gebeurt nu "
                  "in een eeuw. Niet de richting en niet de grootte in graden zijn uitzonderlijk: het "
                  "tempo is dat wel, en dat is net wat planten, dieren en mensen geen tijd geeft om mee "
                  "te schuiven."),
        ]),
        sectie("klimaat-doorheen-de-geologische-tijd", "Hoe we dat weten", extra=[
            ("p", "Uit <strong>ijskernen</strong> die men uit het landijs boort, lezen we het klimaat "
                  "van <strong>het geologische verleden</strong>: <strong>de lucht van toen zit in de "
                  "luchtbellen</strong> in het ijs, dus kan men de koolstofdioxide van honderdduizenden "
                  "jaren geleden rechtstreeks meten. Niet de dikte en niet de kleur van het ijs geven "
                  "dat, en fossielen van planten zitten er niet in."),
        ]),
        sectie("klimaat-doorheen-de-geologische-tijd", "De andere natuurlijke oorzaken"),
        sectie("de-huidige-klimaatverandering", "Hoe we weten dat het de mens is"),
        sectie("de-huidige-klimaatverandering", "Terugkoppelingen"),
        sectie("de-huidige-klimaatverandering", "Scenario's en doelen"),
        sectie("de-huidige-klimaatverandering", "Mitigatie en adaptatie", extra=[
            ("p", "<strong>Mitigatie</strong> is dus <strong>minder fossiele brandstof "
                  "gebruiken</strong>, <strong>huizen beter isoleren</strong> en <strong>bossen "
                  "aanplanten</strong>. <strong>Dijken verhogen</strong> is géén mitigatie maar "
                  "adaptatie: het verandert niets aan de oorzaak. En <strong>een maatregel kan zowel "
                  "adaptatie als mitigatie zijn</strong>: een bos in de stad legt koolstof vast én geeft "
                  "schaduw."),
        ]),
        GEVOLGEN_DICHTBIJ,
        sectie("de-huidige-klimaatverandering", "Een kwestie van rechtvaardigheid"),
    ])


# ───────────────────── 15. Verstedelijking en het ruimtelijk beleid
HET_BELEID = dict(kop="Wie beslist, en met welk plan", blokken=[
    ("p", "In Vlaanderen beslist <strong>de overheid</strong> over de bestemming van de grond, niet de "
          "eigenaar, de bouwfirma of de buren. Wie een perceel bezit, mag er niet zomaar op bouwen: "
          "de bestemming bepaalt wat er mag."),
    ("p", tabel(["Plan", "Wanneer", "Wat het deed"], [
        ["het <strong>gewestplan</strong>", "vanaf de jaren zeventig",
         "legde <strong>de bestemming van elk perceel</strong> vast: woongebied, landbouw, industrie, natuur"],
        ["het <strong>RSV</strong>, het Ruimtelijk Structuurplan Vlaanderen", "1997",
         "volgde het gewestplan op en wou de groei in de steden en de kernen houden"],
        ["het <strong>BRV</strong>, het Beleidsplan Ruimte Vlaanderen", "vanaf 2018",
         "wil <strong>geen open ruimte meer innemen</strong>: bouwen binnen wat al bebouwd is"],
    ])),
    ("p", "Het <strong>gewestplan kleurde juist véél meer woongebied in dan er nodig was</strong>, en "
          "royaal verspreid over het hele gewest. Daar komt onze lintbebouwing grotendeels uit."),
    ("p", "De omslag naar bouwen binnen het bestaande ruimtebeslag heet de "
          "<strong>bouwshift</strong>, in de kranten vaak de <strong>betonstop</strong>. "
          "<strong>Dat betekent niet dat er niets meer gebouwd wordt</strong>: er wordt evenveel "
          "gebouwd, maar op een andere plek, namelijk in de kernen. Dat heet "
          "<strong>kernversterking</strong>: <strong>er wordt in de kern bijgebouwd</strong>, en "
          "daardoor hoeft er geen veld meer aangesneden te worden."),
    ("p", "De <strong>kernkwaliteiten</strong> van het BRV zijn <strong>nabijheid</strong>, "
          "<strong>veerkracht</strong>, een <strong>gezonde leefomgeving</strong> en ruimte-efficiëntie. "
          "Zo veel mogelijk vrije grond bebouwen staat er natuurlijk niet in."),
    ("p", "De <strong>nodaliteit</strong> of knooppuntwaarde van een plek zegt <strong>hoe goed ze "
          "ontsloten is</strong>: hoeveel je er te voet, met de bus en met de trein kan bereiken. Hoog "
          "bouwen doe je op een plek met een hoge nodaliteit, en niet in een veld waar enkel een auto "
          "komt. Met het instrument <strong>Geopunt</strong> van de Vlaamse overheid bekijk je zelf de "
          "<strong>bestemming van een perceel</strong>."),
    ("kader", "<strong>Hoe dichter de bebouwing, hoe mínder kilometers mensen met de auto rijden.</strong> "
              "In een kern liggen de school, de winkel en de bus dichtbij; in een lint of een "
              "verkaveling moet je voor alles de auto nemen. Daarom is <strong>lintbebouwing ook duur "
              "voor de gemeenschap</strong>: <strong>de nutsleidingen, de riolering en de postronde "
              "moeten verder</strong>, voor evenveel gezinnen."),
])

DIEREN_EN_RUIMTE = dict(kop="Versnippering en het ecoduct", blokken=[
    ("p", "<strong>Versnippering</strong> of <strong>fragmentatie</strong> is <strong>het opdelen van "
          "natuur in losse stukken door wegen en bebouwing</strong>. Voor dieren betekent dat drie "
          "dingen: <strong>ze kunnen niet meer doortrekken</strong>, <strong>hun gebied wordt te "
          "klein</strong> om in te leven, en <strong>ze komen vaker onder een auto</strong>. Meer "
          "voedsel vinden ze er zeker niet."),
    ("p", "Een <strong>ecoduct</strong> is <strong>een brug of een tunnel waarlangs dieren een weg "
          "kunnen oversteken</strong>. In Vlaanderen liggen er een paar over de E314 en de E19. Het is "
          "dus geen woonvorm: bij de <strong>woontypologieën</strong> horen een "
          "<strong>rijhuis</strong>, een <strong>appartement</strong> en "
          "<strong>halfopen bebouwing</strong>, niet een ecoduct."),
])

zet("verstedelijking-en-het-ruimtelijk-beleid",
    "Verstedelijking en het ruimtelijk beleid",
    "Hoe de stad en haar rand groeiden, wat dat met de open ruimte deed, en met welke plannen "
    "Vlaanderen het wil bijsturen.",
    [
        sectie("verstedelijking-en-ruimtegebruik", "Vier fasen"),
        sectie("verstedelijking-en-ruimtegebruik", "Hoe een Vlaamse stad en haar rand eruitzien"),
        sectie("verstedelijking-en-ruimtegebruik", "De nevelstad"),
        sectie("verstedelijking-en-ruimtegebruik", "Ruimtebeslag, verharding en versnippering"),
        DIEREN_EN_RUIMTE,
        sectie("verstedelijking-en-ruimtegebruik", "Het hitte-eiland", extra=[
            ("p", "De gevolgen van het hitte-eiland zijn <strong>warmere nachten</strong>, "
                  "<strong>meer gezondheidsklachten</strong> bij ouderen en zieken, en "
                  "<strong>meer koeling nodig</strong> in gebouwen. <strong>Minder "
                  "luchtvervuiling</strong> hoort er niet bij; die wordt er eerder meer van. De "
                  "<strong>ingreep die een straat het meest afkoelt, is bomen planten</strong>: schaduw "
                  "én verdamping. Zwart asfalt en betegelde voortuinen doen net het omgekeerde."),
        ]),
        sectie("verstedelijking-en-ruimtegebruik", "Wie beslist over de ruimte"),
        HET_BELEID,
        sectie("verstedelijking-en-ruimtegebruik", "Wie waar woont"),
        sectie("duurzaam-ruimtegebruik", "Intensivering"),
        sectie("duurzaam-ruimtegebruik", "Hergebruik en verweving", extra=[
            ("p", "<strong>Verweving van functies</strong> is <strong>wonen en werken door "
                  "elkaar</strong>: een winkel onder woningen, een kleine werkplaats in een woonstraat. "
                  "Het omgekeerde is zonering, waarbij elke functie haar eigen zone krijgt."),
            ("p", "Bij <strong>duurzaam ruimtegebruik</strong> horen dus drie maatregelen: "
                  "<strong>intensiever gebruiken wat er is</strong>, <strong>oude gebouwen "
                  "hergebruiken</strong> en <strong>functies verweven in één gebied</strong>. Nieuwe "
                  "verkavelingen in het veld horen er net niet bij."),
        ]),
        sectie("duurzaam-ruimtegebruik", "Tijdelijk ruimtegebruik", extra=[
            ("p", "<strong>Tijdelijk ruimtegebruik</strong> is <strong>leegstand even nuttig "
                  "gebruiken</strong>: een pand dat op een bouwvergunning wacht, wordt een paar jaar "
                  "een repetitieruimte of een buurttuin."),
        ]),
        sectie("duurzaam-ruimtegebruik", "Water en ontharden", extra=[
            ("p", "Een <strong>wadi houdt regenwater tijdelijk vast zodat het kan infiltreren</strong> "
                  "in de bodem, in plaats van meteen de riool in te gaan. <strong>Verharding geeft "
                  "wateroverlast omdat regen niet in de bodem zakt</strong>: al dat water komt in een "
                  "keer in de riool en in de beek terecht."),
        ]),
    ])


# ───────────────────── 16. Het landschap lezen en duurzaam ruimtegebruik
BEELDEN_LEZEN = dict(kop="Beelden en kaarten lezen", blokken=[
    ("p", tabel(["Bron", "Wat je eruit haalt"], [
        ["een <strong>orthofoto</strong>",
         "een <strong>rechtgezette luchtfoto</strong>: elk punt staat op zijn juiste plaats, dus je kan erop meten"],
        ["een satellietbeeld in <strong>ware kleuren</strong>",
         "<strong>wat je oog ook zou zien</strong>"],
        ["een <strong>valsekleurenbeeld</strong>",
         "ook <strong>infrarood</strong>, dat ons oog niet ziet; gezonde plantengroei komt er <strong>rood</strong> op"],
        ["een <strong>topografische kaart</strong>",
         "de hoogte, met <strong>hoogtelijnen</strong> of <strong>isohypsen</strong>"],
        ["een <strong>digitaal hoogtemodel</strong>",
         "een <strong>hoogtekaart</strong> uit lasermetingen, waarop je oude dijken en holle wegen ziet"],
        ["een <strong>bodemkaart</strong>", "de <strong>bodemsoort</strong>: zand, leem, klei"],
        ["een <strong>geologische doorsnede</strong>", "een <strong>kijk in de ondergrond</strong>"],
    ])),
    ("p", "Een <strong>valsekleurenbeeld heeft geen verkeerde kleuren om je te misleiden</strong>: het "
          "geeft kleuren aan straling die je niet kan zien, net om méér te laten zien dan een gewone "
          "foto."),
    ("p", "Een <strong>profiel</strong> door een landschap is een doorsnede van het reliëf: het "
          "<strong>brengt de hoogte in beeld</strong>, van links naar rechts, zoals je ze zou zien als "
          "je het landschap doormidden zaagde."),
    ("p", "Aan het beeld zelf lees je de geschiedenis af. Een <strong>natuurlijke rivier</strong> "
          "herken je <strong>aan haar bochten</strong>; een rechte lijn door het veld is gegraven. Een "
          "<strong>verkaveling</strong> herken je <strong>aan de gelijke huizen</strong> op gelijke "
          "percelen. En <strong>rechte percelen en brede wegen wijzen juist op een jong, "
          "heraangelegd landschap</strong>, niet op een eeuwenoud: een oud landschap is onregelmatig, "
          "met kromme wegen en percelen van alle vormen. Op een <strong>luchtfoto van vijftig jaar "
          "oud</strong> zie je dan ook meteen hoeveel bebouwing er sindsdien bijkwam."),
])

DUURZAME_DOELEN = dict(kop="De 5 P's en de zeventien doelen", blokken=[
    ("p", "De <strong>5 P's</strong> van duurzame ontwikkeling zijn <strong>people</strong>, "
          "<strong>planet</strong>, <strong>prosperity</strong>, <strong>peace</strong> en "
          "<strong>partnership</strong>. <strong>Petroleum</strong> hoort er dus niet bij."),
    ("p", "De Verenigde Naties stelden in 2015 <strong>zeventien</strong> duurzame "
          "ontwikkelingsdoelen op, de <strong>SDG's</strong>. Ze <strong>gelden voor alle landen</strong>, "
          "rijk en arm: ook België haalt er heel wat nog niet."),
    ("p", tabel(["Doel", "Waarover het gaat"], [
        ["<strong>duurzame steden</strong> en gemeenschappen (11)", "wonen, mobiliteit en groen in de stad"],
        ["<strong>klimaatactie</strong> (13)", "de uitstoot omlaag en je wapenen tegen de gevolgen"],
        ["<strong>duurzame energie</strong> (7)", "schone energie voor iedereen"],
        ["<strong>leven op het land</strong> (15)", "bodem, bossen en biodiversiteit"],
    ])),
    ("p", "<strong>Gendergelijkheid</strong> (5) is ook een doel, maar het raakt het klimaat niet "
          "rechtstreeks. En <strong>een maatregel kan goed zijn voor het ene doel en slecht voor het "
          "andere</strong>: een windmolenpark is klimaatactie, maar het neemt ruimte in. Daarom weeg je "
          "ze tegen elkaar af in plaats van er één te volgen."),
    ("p", "<strong>Duurzaam omgaan met de ruimte</strong> betekent <strong>ook voor later ruimte "
          "laten</strong>: wie nu alle open ruimte bebouwt, neemt de keuze van de volgende generatie "
          "weg."),
])

RUIMTE_SLIM = dict(kop="Meer doen met dezelfde ruimte", blokken=[
    ("p", tabel(["Begrip", "Wat het betekent"], [
        ["<strong>intensivering</strong>", "<strong>meer doen op dezelfde plek</strong>"],
        ["<strong>verdichten</strong>", "<strong>meer mensen op dezelfde oppervlakte</strong> laten wonen"],
        ["<strong>hergebruik</strong> of <strong>herbestemming</strong>",
         "<strong>een leegstaand gebouw opnieuw gebruiken</strong>, met een nieuwe functie"],
        ["een <strong>brownfield</strong>", "<strong>een oud bedrijfsterrein</strong> dat op herontwikkeling wacht"],
        ["<strong>verweving</strong>", "<strong>wonen en werken door elkaar</strong>, bijvoorbeeld een winkel onder woningen"],
        ["<strong>ontharden</strong>", "<strong>beton en asfalt weghalen zodat regen weer in de grond kan</strong>"],
    ])),
    ("p", "Het <strong>aansnijden van open ruimte</strong> geeft <strong>minder "
          "landbouwgrond</strong>, <strong>meer versnippering</strong> en <strong>meer "
          "verharding</strong>. Meer ruimte voor natuur geeft het niet; dat is net wat je verliest."),
    ("p", "Een <strong>landschap is een systeem</strong> omdat <strong>de delen op elkaar "
          "inwerken</strong>: de bodem bepaalt de landbouw, de landbouw bepaalt de percelen, de "
          "percelen bepalen de wegen. <strong>Systeemdenken</strong> betekent dan ook dat "
          "<strong>alles aan elkaar hangt</strong>; in een systeemdenkschema zet je met pijlen "
          "<strong>de verbanden</strong>, niet de jaartallen. Ook <strong>mobiliteit hoort bij het "
          "ruimtelijk beleid</strong>, want <strong>waar je woont bepaalt je verkeer</strong>."),
    ("p", "De omslag naar bouwen binnen het bestaande ruimtebeslag heet de "
          "<strong>bouwshift</strong>. <strong>De bouwshift wil niet dat er in Vlaanderen niets meer "
          "gebouwd wordt</strong>: ze wil dat er op een andere plek gebouwd wordt, in de kernen in "
          "plaats van in het veld. Over de <strong>bestemming van de grond beslist in Vlaanderen de "
          "overheid</strong>, niet de eigenaar, de bouwfirma of de buren."),
    ("p", "Bij een <strong>landschapsanalyse</strong> stel je drie vragen: <strong>wat zie ik?</strong>, "
          "<strong>waarom ligt het hier?</strong> en <strong>hoe is het zo geworden?</strong> Je werkt "
          "met een <strong>luchtfoto</strong>, een <strong>oude kaart</strong> en een "
          "<strong>veldbezoek</strong>; een klimatogram van Rome helpt je daar niet bij."),
])

zet("het-landschap-lezen-en-duurzaam-ruimtegebruik",
    "Het landschap lezen en duurzaam ruimtegebruik",
    "Hoe een landschap geworden is wat het is, hoe je het leest op beelden en kaarten, en hoe je er "
    "duurzaam mee omgaat.",
    [
        sectie("het-landschap-lezen", "Landschapsgenese"),
        sectie("het-landschap-lezen", "De hand van de mens"),
        sectie("het-landschap-lezen", "Een landschap stap voor stap lezen"),
        sectie("het-landschap-lezen", "Kijken van boven"),
        sectie("het-landschap-lezen", "GIS en Geopunt"),
        BEELDEN_LEZEN,
        sectie("duurzaam-ruimtegebruik", "Het omgevingsdenken"),
        sectie("duurzaam-ruimtegebruik", "Intensivering"),
        sectie("duurzaam-ruimtegebruik", "Hergebruik en verweving"),
        sectie("duurzaam-ruimtegebruik", "Tijdelijk ruimtegebruik"),
        RUIMTE_SLIM,
        sectie("het-landschap-lezen", "Duurzame ontwikkeling"),
        DUURZAME_DOELEN,
        sectie("het-landschap-lezen", "Systeemdenken"),
    ])

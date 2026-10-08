# -*- coding: utf-8 -*-
"""De leerbundels van Engels voor 🌍 Beyond dubbele finaliteit.

    python3 -I maak_alles.py engels

Zestien bundels, één per thema van `inhoud/beyond-dubbele-finaliteit/engels.json`.

Gebaseerd op de twee vakfiches Engels 1 en Engels 2 van de derde graad dubbele
finaliteit, geldig vanaf 1 januari 2027. Ze gelden voor de basisvorming van de
dubbele finaliteit en voor commerciële organisatie. Het ERK-niveau is
**A2+**, een stap lager dan de B1 van de doorstroomrichtingen. Engels 1 is een
digitaal examen van 120 minuten over lezen en luisteren; Engels 2 bestaat uit
een spreekopdracht die je thuis opneemt, schrijfopdrachten op het digitale
examen en een gesprek.

De grammaticalijst van deze fiche is korter dan die van doorstroom: **geen
gerund, geen semi-auxiliaries, geen indirecte rede, geen passieve vorm en geen
past perfect**. Die secties van de doorstroombundels worden hier dus
weggelaten. Wat er wél in staat: de present perfect simple en continuous, de
past simple en continuous, de drie manieren om over de toekomst te spreken, de
modalen, en de conditionals zero en first.

Twee thema's bestaan niet op doorstroom en zijn hier nieuw geschreven: de
Engelstalige wereld met haar gewoontes en het reizen, en het thema over
schrijven, spreken en literatuurbeleving.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De sleutels eindigen op "-beyond-dubbele-finaliteit". Engels bestaat ook op
🌱 Start, ✨ Spark, 🚀 Boost en 🌍 Beyond doorstroom, en daar komen thematitels
in voor die hier bijna gelijk klinken.

Geen enkel citaat in deze bundels komt van een bestaand boek of een bestaande
schrijver. Elke voorbeeldzin is zelf geschreven.
"""
import copy
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))

import bundel
import maak_engels_beyond as door

VAK = "Engels"
DF = "🌍 Beyond dubbele finaliteit — 5de en 6de middelbaar"
NA = "-beyond-dubbele-finaliteit"
BUITEN = "Oefen dit ook buiten het scherm"
tabel = bundel.tabel

BUNDELS = {}


def spreken(opdracht):
    """Het vaste slotkader: wat je niet achter een scherm leert."""
    return dict(kop=BUITEN, blokken=[
        ("p", "Op dit platform oefen je <strong>lezen</strong>, woordenschat en grammatica. Maar "
              "<strong>luisteren</strong> is de helft van het examen Engels 1, en Engels 2 bestaat uit "
              "<strong>schrijven</strong>, een <strong>spreekopdracht die je thuis opneemt</strong> en "
              "een <strong>gesprek</strong>. Die drie kan een platform met tekstvragen niet nabootsen, "
              "en ze wegen samen zwaarder dan alles wat je hier leest."),
        ("kader", "<strong>Deze week:</strong> " + opdracht + " Doe het één keer, en let daarna op wat "
                  "je miste of niet gezegd kreeg. Dat is precies je volgende oefening."),
    ])


def secties(sleutel, weglaten=()):
    """Alle secties van een doorstroombundel, zonder het slotkader en zonder
    wat deze fiche niet vraagt."""
    uit = []
    for s in door.BUNDELS[sleutel + "-beyond"]["secties"]:
        if s["kop"] == BUITEN or s["kop"] in weglaten:
            continue
        uit.append(copy.deepcopy(s))
    assert len(uit) + 1 + len(weglaten) == len(door.BUNDELS[sleutel + "-beyond"]["secties"]), sleutel
    return uit


def sectie(sleutel, kop, extra=()):
    for s in door.BUNDELS[sleutel + "-beyond"]["secties"]:
        if s["kop"] == kop:
            s = copy.deepcopy(s)
            s["blokken"] = list(s["blokken"]) + list(extra)
            return s
    raise KeyError(f"{sleutel}: {kop}")


def zet(sleutel, titel, onder, secties_):
    BUNDELS[sleutel + NA] = dict(vak=VAK, niveau=DF, titel=titel,
                                 onder=onder, secties=secties_)


# ───────────────────── 1. Een Engelse tekst lezen
zet("een-engelse-tekst-lezen",
    "Een Engelse tekst lezen",
    "Het onderwerp en de hoofdgedachte vinden, gericht zoeken, tussen de regels lezen en een onbekend "
    "woord aanpakken.",
    secties("een-engelse-tekst-analyseren") + [
        dict(kop="Voor je begint te lezen", blokken=[
            ("p", "Drie vragen stel je jezelf <strong>voor</strong> je begint: <strong>waarover gaat "
                  "dit?</strong>, <strong>wat weet ik hier al over?</strong> en <strong>wat moet ik uit "
                  "deze tekst halen?</strong> Die laatste staat in de opdracht, dus lees de vraag voor "
                  "de tekst."),
            ("p", "Daarbij helpen de <strong>visuele hulpmiddelen</strong> van een tekst: de "
                  "<strong>titel en de tussentitels</strong>, de <strong>foto's en hun "
                  "onderschrift</strong>, de <strong>grafieken en tabellen</strong>, en de woorden die "
                  "in het vet staan. Die lees je eerst; samen vertellen ze je al bijna waarover het "
                  "gaat."),
            ("p", "Bij het <strong>communicatiemodel</strong> vraag je je vier dingen af: "
                  "<strong>wie schrijft of spreekt</strong> (de zender), <strong>voor wie</strong> (de "
                  "ontvanger), <strong>wat de boodschap is</strong>, en <strong>via welk "
                  "kanaal</strong> ze komt: een krant, een mail, een podcast of een affiche. Ook een "
                  "<strong>geschreven</strong> tekst heeft een zender en een ontvanger, ook als je die "
                  "niet ziet."),
            ("kader", "<strong>Je moet niet elk onbekend woord in een tekst opzoeken.</strong> Dat "
                      "kost tijd die je op het examen niet hebt, en het is vaak niet nodig: uit de "
                      "zin errond, uit de delen van het woord en uit "
                      "<strong>je kennis van het Nederlands</strong> raad je er heel veel. "
                      "<em>Transport</em>, <em>information</em> en <em>problem</em> lijken niet "
                      "toevallig op onze woorden. Zoek alleen op wat je nodig hebt voor de vraag."),
        ]),
        dict(kop="Signaalwoorden op een rij", blokken=[
            ("p", "<strong>Signaalwoorden helpen je de gedachtegang van een tekst te volgen</strong>: "
                  "ze zeggen wat er komt, nog voor je het leest."),
            ("p", tabel(["Wat het aankondigt", "Engelse signaalwoorden"], [
                ["een <strong>opsomming</strong> of een orde",
                 "<strong>first</strong>, <strong>firstly</strong>, <strong>secondly</strong>, "
                 "then, next, also, <strong>finally</strong>"],
                ["een <strong>tegenstelling</strong>",
                 "<strong>but</strong>, <strong>however</strong>, although, on the other hand"],
                ["een <strong>oorzaak of reden</strong>", "because, because of, since, as"],
                ["een <strong>gevolg</strong>", "so, therefore, as a result"],
                ["een <strong>voorbeeld</strong>", "for example, for instance, such as"],
                ["een <strong>samenvatting</strong>", "in short, to sum up, all in all"],
            ])),
            ("kader", "<strong>Finally kondigt geen tegenstelling aan maar het laatste punt</strong> "
                      "van een opsomming. Het woord dat een tegenstelling aankondigt en met een h "
                      "begint, is <strong>however</strong>."),
        ]),
        spreken("zet een Engelse serie op met Engelse ondertitels, kijk één aflevering en schrijf na "
                "elke scène in één Engelse zin op wat er gebeurde."),
    ])


# ───────────────────── 2. Tekstsoorten en de bedoeling van een tekst
zet("tekstsoorten-en-de-bedoeling-van-een-tekst",
    "Tekstsoorten en de bedoeling van een tekst",
    "Welke soort tekst je voor je hebt, wat de schrijver ermee wil, en het verschil tussen een feit en "
    "een mening.",
    secties("tekstsoorten-en-de-bedoeling-van-een-tekst") + [
        dict(kop="De namen die deze fiche gebruikt", blokken=[
            ("p", "Deze fiche noemt de tekstsoorten met iets andere woorden dan je elders tegenkomt. "
                  "Dit zijn de namen die in de vragen staan."),
            ("p", tabel(["Soort", "Wat de tekst wil", "Voorbeelden"], [
                ["<strong>informatief</strong>", "iets te weten geven",
                 "een nieuwsbericht, een encyclopedie, een tekst over een land"],
                ["<strong>prescriptief</strong>", "<strong>uitleggen wat of hoe je iets moet doen</strong>",
                 "een recept, een gebruiksaanwijzing, de spelregels"],
                ["<strong>persuasief</strong>", "<strong>je overtuigen om iets te doen of te kopen</strong>",
                 "een <strong>reclamefilmpje</strong>, een <strong>campagne</strong> om minder snel te "
                 "<strong>rijden</strong>, een affiche voor een <strong>sportevenement</strong>"],
                ["<strong>opiniërend</strong>", "<strong>iemands mening geven</strong>",
                 "een <strong>recensie</strong> van een boek of een hotel, een opiniestuk, een lezersbrief"],
                ["<strong>narratief</strong>", "een verhaal vertellen, met een verloop in de tijd",
                 "een reisverslag, een <strong>podcast</strong> waarin iemand iets navertelt"],
                ["<strong>literair</strong>", "iets maken met taal",
                 "een gedicht, een roman, een <strong>kortverhaal</strong>"],
            ])),
            ("p", "<strong>Persuasief en opiniërend liggen dicht bij elkaar</strong>, en het verschil "
                  "is wat de schrijver van jóu wil. Een <strong>recensie</strong> geeft een mening en "
                  "is dus <strong>opiniërend</strong>; <em>Vote for Hannah!</em> wil dat je iets doet "
                  "en is <strong>persuasief</strong>."),
            ("p", "Een <strong>cartoon hoort niet bij de informatieve teksten</strong>: een "
                  "spotprent geeft een mening of maakt een punt, dus opiniërend. Een "
                  "<strong>interview is geen literaire tekst</strong> maar een informatieve. Een "
                  "<strong>nieuwsitem op de radio</strong> is <strong>informatief</strong>, en "
                  "<strong>een podcast kan narratief zijn</strong> als er een verhaal in verteld wordt."),
            ("kader", "Een <strong>prescriptieve tekst herken je</strong> aan drie dingen: "
                      "<strong>bevelende vormen</strong> (<em>Mix</em>, <em>Add</em>, <em>Keep out "
                      "of reach of children</em>), een <strong>stappenplan</strong> met nummers of "
                      "streepjes, en <strong>signaalwoorden van orde</strong>: <em>first</em>, "
                      "<em>then</em>, <em>next</em>, <em>finally</em>."),
            ("p", "Een mening zet je in het Engels vaak in met <strong>in my opinion</strong> of "
                  "<strong>I think</strong>. Woorden die een mening verraden, zijn de "
                  "waardewoorden: <em>beautiful</em>, <em>the best</em>, <strong><em>terrible</em></strong>, "
                  "<em>boring</em>, <em>too expensive</em>. <strong>Een tekst kan feiten en meningen "
                  "door elkaar bevatten</strong>, en dat is net het geval in de meeste recensies."),
            ("p", "Het <strong>kanaal</strong> van een tekst in het communicatiemodel is "
                  "<strong>de weg waarlangs de boodschap komt</strong>: een krant, een mail, een "
                  "affiche, een podcast, een gesprek. Dezelfde boodschap klinkt anders in een mail dan "
                  "in een gesprek, en net dat bepaalt je toon."),
            ("p", "Een <strong>gepast register betekent niet dat je altijd zo formeel mogelijk "
                  "schrijft</strong>: het betekent dat je toon bij je lezer past. Aan een vriend is "
                  "<em>Hiya! Fancy a pizza tonight?</em> precies goed; aan een werkgever niet. In een "
                  "<strong>formele mail</strong> passen woorden als <strong>Dear</strong>, "
                  "<em>I am writing to…</em>, <strong>in advance</strong> (<em>Thank you in "
                  "advance</em>), <strong>regards</strong> (<em>Kind regards</em>) en <em>Yours "
                  "sincerely</em>."),
            ("kader", "<strong>Vermijd in het Engels woorden die als een scheldwoord kunnen "
                      "klinken</strong>, ook als ze onschuldig bedoeld zijn. Je hoort in series veel "
                      "wat je in een mail of op een examen niet schrijft; bij twijfel kies je het "
                      "neutrale woord. En bij een <strong>spreekopdracht moet je op een "
                      "gesprekspartner reageren</strong>: je monoloog afdraaien volstaat niet, je moet "
                      "ook antwoorden op wat de ander zegt."),
            ("p", "De <strong>aanspreking</strong> van een formele Engelse brief of mail begint met "
                  "<strong>Dear</strong>: <em>Dear Mr Smith,</em> of <em>Dear Sir or Madam,</em> als je "
                  "de naam niet kent. Een <strong>goed opgebouwde tekst</strong> bestaat uit drie "
                  "delen: een <strong>inleiding</strong>, een <strong>midden</strong> en een "
                  "<strong>slot</strong>."),
        ]),
        spreken("zoek in een Engelse webwinkel drie reviews van hetzelfde product en zeg voor elke "
                "review luidop of de schrijver iets wil verkopen, waarschuwen of gewoon vertellen."),
    ])


# ───────────────────── 3. De Engelstalige wereld: gewoontes en reizen
zet("de-engelstalige-wereld-gewoontes-en-reizen",
    "De Engelstalige wereld: gewoontes en reizen",
    "Waar Engels de taal is, welke gewoontes je er tegenkomt, en de woorden die je op reis nodig hebt.",
    [
        dict(kop="Waar men Engels spreekt", blokken=[
            ("p", "Engels is de taal van veel meer landen dan Engeland. Bij de Engelstalige wereld "
                  "horen <strong>Ierland</strong>, <strong>Australië</strong>, <strong>Nieuw-Zeeland</strong>, "
                  "Canada, de Verenigde Staten, Zuid-Afrika en India. <strong>Oostenrijk</strong> hoort "
                  "er niet bij: daar spreekt men Duits."),
            ("kader", "<strong>Great Britain en the United Kingdom betekenen niet hetzelfde.</strong> "
                      "<em>Great Britain</em> is het eiland met <em>England</em>, <em>Scotland</em> en "
                      "<em>Wales</em>. Het <em>United Kingdom</em> is dat plus <em>Northern Ireland</em>, "
                      "dus <strong>vier landen en niet twee</strong>. En <em>the British Isles</em> is "
                      "nog ruimer: daar hoort ook Ierland bij, dat een eigen staat is."),
            ("p", tabel(["Vraag", "Antwoord"], [
                ["de hoofdstad van <strong>Scotland</strong>", "<strong>Edinburgh</strong>, niet Glasgow"],
                ["de hoofdstad van Northern Ireland", "Belfast"],
                ["de munt van het Verenigd Koninkrijk", "het <strong>pond</strong> (<em>the pound</em>), niet de euro"],
                ["een inwoner van Schotland", "<strong>a Scot</strong>, en het bijvoeglijk naamwoord is <em>Scottish</em>"],
                ["de regeringsleider", "<strong>the Prime Minister</strong>"],
                ["<strong>NHS</strong>", "de <strong>gezondheidszorg</strong>: <em>National Health Service</em>"],
            ])),
        ]),
        dict(kop="Gewoontes die je zal opvallen", blokken=[
            ("p", "De fiche vraagt dat je de gewoontes van de Engelstalige wereld kent, en ze komen "
                  "ook in leesteksten terug."),
            ("p", tabel(["In het Verenigd Koninkrijk", "In de Verenigde Staten"], [
                ["men rijdt <strong>links</strong>", "men rijdt rechts, zoals bij ons"],
                ["afstanden staan in <strong>mijlen</strong> op de borden (1 mijl = 1,6 km)",
                 "ook in mijlen"],
                ["<strong>netjes in de rij staan</strong> (<em>to queue</em>) hoort erbij",
                 "in een restaurant geef je een <strong>tip</strong>, gewoonlijk 15 tot 20 procent"],
                ["<strong>thee met melk</strong> drinken", "men spreekt je vaak meteen met je "
                 "<strong>voornaam</strong> aan, ook iemand die je net ontmoet hebt"],
                ["op veel scholen draag je een <strong>uniform</strong>",
                 "het eerste jaar aan de universiteit heet <strong>freshman year</strong>"],
                ["<strong>small talk over het weer</strong> is een gewone manier om een gesprek te "
                 "beginnen", "<strong>Thanksgiving</strong> valt in <strong>november</strong>"],
            ])),
            ("p", "Met de fiets naar school gaan is geen Britse gewoonte maar een Vlaamse; in het "
                  "Verenigd Koninkrijk gaan de meeste leerlingen met de bus of worden ze gebracht."),
            ("p", tabel(["Engels", "Nederlands"], [
                ["a <strong>pub</strong>", "het café waar men iets gaat drinken"],
                ["a <strong>bank holiday</strong>", "een <strong>vrije dag</strong>, een wettelijke feestdag"],
                ["<strong>Boxing Day</strong>", "de dag <strong>na Kerstmis</strong>, 26 december"],
                ["a <strong>fortnight</strong>", "<strong>twee weken</strong>, dus geen nacht en geen veertien uur"],
            ])),
            ("kader", "Een <strong>datum schrijf je in het Engels niet zoals in het "
                      "Nederlands</strong>. Brits: <em>5 March 2027</em> of <em>5/3/2027</em>. "
                      "Amerikaans zet de maand vooraan: <em>March 5, 2027</em> of <em>3/5/2027</em>. "
                      "Datzelfde <em>3/5</em> is dus 3 mei in Londen en 5 maart in New York; schrijf de "
                      "maand uit als het ergens op aankomt."),
            ("p", "Bij <strong>lichaamstaal</strong> horen <strong>je houding</strong>, "
                  "<strong>je blik</strong> en <strong>je handen</strong>. De woorden die je kiest horen "
                  "daar net niet bij: dat is je taal, niet je lichaamstaal. Toch telt lichaamstaal mee "
                  "bij een spreekopdracht, want ze bepaalt hoe je overkomt."),
        ]),
        dict(kop="Op reis: vervoer en bagage", blokken=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["a <strong>plane</strong>, an <strong>aeroplane</strong>", "een vliegtuig"],
                ["a <strong>coach</strong>", "een touringcar of autobus voor langere ritten"],
                ["a <strong>ferry</strong>", "een veerboot"],
                ["the <strong>underground</strong>, the tube", "de metro in Londen"],
                ["<strong>luggage</strong>", "<strong>bagage</strong> (ontelbaar: <em>my luggage is heavy</em>)"],
                ["a <strong>suitcase</strong>", "een koffer"],
                ["a <strong>passport</strong>", "een paspoort"],
                ["a <strong>ticket</strong>", "een kaartje"],
                ["a <strong>return ticket</strong>", "een ticket <strong>heen en terug</strong>; enkel heen is <em>a single</em>"],
            ])),
            ("p", "Een <strong>cottage</strong> is géén vervoermiddel maar een huisje op het "
                  "platteland, en <em>a frying pan</em> is een braadpan: die hoort in de keuken, niet in "
                  "je koffer."),
            ("kader", "Je zegt <strong>niet</strong> <em>I go with the train</em>. In het Engels gebruik "
                      "je <strong>by</strong>: <em>I go <strong>by</strong> train</em>, <em>by bus</em>, "
                      "<em>by car</em>, <em>by plane</em>. Te voet is <em>on foot</em>."),
        ]),
        sectie("woordvelden-kunst-literatuur-politiek-en-reizen", "Reizen"),
        dict(kop="Op reis: verblijf, landschap en wat er misgaat", blokken=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["<strong>accommodation</strong>", "een <strong>verblijf</strong>, een plaats om te slapen"],
                ["a <strong>bed and breakfast</strong>", "een <strong>kamer met ontbijt</strong> bij mensen thuis"],
                ["to <strong>book a room</strong>", "een kamer <strong>reserveren</strong>"],
                ["a <strong>seaside resort</strong>", "een <strong>badplaats</strong>"],
                ["a <strong>city break</strong>", "een <strong>korte stadsreis</strong> van een paar dagen"],
                ["a <strong>sightseeing tour</strong>", "een <strong>toeristische rondrit</strong> langs de bezienswaardigheden"],
                ["the <strong>countryside</strong>", "het <strong>platteland</strong>"],
                ["the <strong>landscape</strong>, the <strong>scenery</strong>", "het <strong>landschap</strong>"],
                ["<strong>abroad</strong>", "in het <strong>buitenland</strong>"],
            ])),
            ("p", "<strong>A journey en a trip betekenen allebei een reis</strong>, met een nuance: "
                  "<em>a journey</em> is vooral de verplaatsing zelf, <em>a trip</em> het hele uitje. "
                  "<strong>A tourist en a traveller zijn niet precies hetzelfde</strong>: een "
                  "<em>tourist</em> gaat voor zijn plezier kijken, een <em>traveller</em> is gewoon "
                  "iemand die onderweg is, ook voor zijn werk."),
            ("p", tabel(["Als het misloopt", "Nederlands"], [
                ["a <strong>delay</strong>", "een vertraging"],
                ["a <strong>strike</strong>", "een staking"],
                ["a <strong>diversion</strong>", "een omleiding"],
            ])),
            ("p", "Een <strong>souvenir</strong> hoort daar niet bij: dat is net het aandenken dat je "
                  "meebrengt als alles goed ging."),
        ]),
        spreken("plan in het Engels een weekend in Edinburgh: zoek een trein, een bed and breakfast en "
                "drie dingen om te zien, en vertel het daarna luidop in vijf zinnen aan iemand thuis."),
    ])


# ───────────────────── 4. Schrijven, spreken en je beleving bij een tekst
zet("schrijven-spreken-en-je-beleving-bij-een-tekst",
    "Schrijven, spreken en je beleving bij een tekst",
    "Hoe je een Engelse tekst opbouwt, welk register erbij past, wat je in een gesprek doet als het "
    "vastloopt, en hoe je zegt wat een verhaal bij je doet.",
    [
        dict(kop="Voor je begint te schrijven", blokken=[
            ("p", "Een schrijfopdracht begint niet bij de eerste zin maar bij vier vragen. "
                  "<strong>Waarom schrijf ik?</strong> <strong>Voor wie is dit?</strong> "
                  "<strong>Welk kanaal gebruik ik</strong>, een mail, een post of een brief? En "
                  "<strong>hoeveel tijd heb ik nog?</strong>"),
            ("p", "Daarna maak je een <strong>schrijfplan</strong>: <strong>een lijstje "
                  "kernwoorden</strong>, geen volledige tekst in het klad. Dat lijstje mag je op het "
                  "examen op je blad zetten; het is één van de hulpmiddelen die je mag gebruiken, "
                  "naast een <strong>online woordenboek</strong> en <strong>spellingcontrole</strong>. "
                  "Een samenvatting die je thuis maakte, mag je niet meebrengen."),
            ("p", "<strong>Taakvoltooiing</strong> betekent dat <strong>je doel bereikt is</strong>: "
                  "wie je tekst leest, weet of doet wat je wou. Dat is iets anders dan foutloos zijn. "
                  "<strong>Je schrijfopdracht moet niet helemaal foutloos zijn</strong> — op A2+ mag er "
                  "iets fout staan zolang de boodschap aankomt — maar <strong>de opgegeven lengte moet "
                  "je wel respecteren</strong>."),
            ("kader", "<strong>Weet je niet hoe je iets moet formuleren, zeg het dan met wat je al "
                      "kent.</strong> Niet overslaan, niet in het Nederlands schrijven, en geen lange "
                      "zin bouwen waarin je verdwaalt. <em>I could not sleep because of the noise</em> "
                      "is te moeilijk? Schrijf dan <em>The noise was loud. I did not sleep.</em> Twee "
                      "korte zinnen die kloppen, zijn beter dan één lange die niet klopt."),
        ]),
        dict(kop="De tekst zelf: structuur en lay-out", blokken=[
            ("p", "De fiche verwacht een tekst met een <strong>inleiding, een midden en een slot</strong>, "
                  "en geen rij losse zinnen. Het midden verdeel je in <strong>alinea's</strong>: "
                  "stukjes met een <strong>witregel</strong> ertussen, elk over één ding."),
            ("p", "Bij een goede <strong>lay-out</strong> horen een <strong>titel</strong>, "
                  "<strong>alinea's</strong> en <strong>witruimte tussen de delen</strong>. Zo veel "
                  "mogelijk kleuren horen er niet bij: dat maakt een tekst niet duidelijker maar "
                  "rommeliger."),
            ("p", "Je houdt de tekst aan elkaar met <strong>signaalwoorden</strong>: "
                  "<strong>first</strong>, then, also, <strong>however</strong>, because, "
                  "<strong>finally</strong>. <em>Pizza</em> is geen signaalwoord, hoe lekker ook."),
            ("kader", "<strong>Het laatste wat je met je tekst doet, is hem nalezen.</strong> Niet nog "
                      "een alinea bijschrijven en niet alles in het net herschrijven: lees na op de drie "
                      "dingen die het vaakst fout gaan, de <em>-s</em> bij <em>he, she, it</em>, de "
                      "tijd van het werkwoord, en de spelling van de woorden die je zelf twijfelachtig "
                      "vindt."),
        ]),
        dict(kop="Register: formeel of informeel", blokken=[
            ("p", "Het <strong>register</strong> is <strong>het soort taalgebruik dat bij je lezer "
                  "past</strong>. Aan een onbekende schrijf je <strong>neutraal en hoffelijk</strong>, "
                  "dus niet zo kort als het kan, niet met afkortingen en niet in spreektaal met emoji."),
            ("p", tabel(["Informeel, aan een vriend", "Formeel, aan een onbekende"], [
                ["<strong>Hi Tom,</strong> / Hello Sarah,", "<strong>Dear Sir or Madam,</strong> (naam onbekend)"],
                ["Thanks! / Cheers,", "Dear Mr Brown, (naam gekend)"],
                ["See you soon, / Bye for now,", "<strong>Yours sincerely</strong> (naam gekend)"],
                ["Lots of love, (familie)", "Yours faithfully (naam onbekend)"],
            ])),
            ("p", "Eén woord doet in het Engels veel werk: <strong>please</strong>. "
                  "<em>Could you send me the form, <strong>please</strong>?</em> klinkt hoffelijk waar "
                  "<em>Send me the form</em> als een bevel klinkt."),
            ("p", tabel(["Wat je wil doen", "Zinnen die dat doen"], [
                ["<strong>informatie geven</strong>",
                 "<em>The campsite opens in May.</em> / <em>You can book online.</em> / <em>Take a warm sleeping bag.</em>"],
                ["<strong>informatie vragen</strong>",
                 "<em>Could you tell me the time?</em> / <em>What time does it open?</em>"],
                ["<strong>overtuigen</strong>",
                 "<em>This is cheaper.</em> / <em>It saves time.</em> / <em>You should try it.</em>"],
            ])),
            ("kader", "<strong>Je mening geven en iemand overtuigen is niet hetzelfde.</strong> Een "
                      "mening zegt wat jij vindt (<em>I liked it</em>); overtuigen wil dat de ander iets "
                      "doet of denkt, en daarvoor geef je <strong>redenen</strong> (<em>It is cheaper "
                      "and it saves time</em>). <strong>Bij een uitleg mag je wel een voorbeeld "
                      "geven</strong>; dat maakt een uitleg juist beter."),
        ]),
        dict(kop="Spreken en een gesprek voeren", blokken=[
            ("p", "De <strong>spreekopdracht</strong> neem je thuis op, dus die kan je voorbereiden. "
                  "<strong>Een gesprek kan je niet altijd op voorhand voorbereiden</strong>: je weet "
                  "niet wat de ander zal zeggen. Wat je wél kan voorbereiden, zijn de reddingsboeien."),
            ("p", tabel(["Wat er gebeurt", "Wat je zegt of doet"], [
                ["je hebt de vraag niet begrepen",
                 "<strong>vragen om te herhalen</strong>: <em>Sorry, could you say that again?</em>"],
                ["je merkt dat de ander jóu niet begrijpt",
                 "<strong>het anders zeggen</strong>, met andere woorden; niet net hetzelfde herhalen en niet harder praten"],
                ["je kent het woord niet",
                 "omschrijven: <em>the thing you use to open a bottle</em>"],
                ["je hebt even tijd nodig",
                 "<em>Well, let me think…</em> / <em>That's a good question.</em>"],
            ])),
            ("p", "Gewoon <em>yes</em> antwoorden op iets wat je niet begrepen hebt, is de slechtste "
                  "keuze: je komt er een vraag later op vast te zitten. En <strong>je lichaamstaal "
                  "telt mee</strong>: rechtop zitten en iemand aankijken maakt je verstaanbaarder dan "
                  "je denkt."),
            ("p", "Over de toekomst spreken doe je met <em>going to</em> voor plannen: "
                  "<strong><em>I am going to Spain in July</em></strong> vertelt je vakantieplannen. "
                  "<em>I went to Spain last year</em> gaat over het verleden, en <em>Spain is a big "
                  "country</em> vertelt niets over jou."),
        ]),
        dict(kop="Literatuurbeleving: wat doet de tekst met jou", blokken=[
            ("p", "<strong>Literatuurbeleving</strong> is <strong>zeggen wat een tekst bij je "
                  "doet</strong>. Het is geen gedicht vanbuiten leren, geen levensverhaal van de "
                  "schrijver en geen foutenjacht."),
            ("p", "De vragen die erbij horen: <strong>waarom spreekt dit me aan?</strong>, "
                  "<strong>wie van de personages lijkt op mij?</strong> en <strong>welk gevoel roept "
                  "dit op?</strong> Hoeveel bladzijden het boek heeft, hoort daar niet bij. "
                  "<strong>Je mag zeggen dat een tekst je niet aanspreekt</strong>, als je er een "
                  "reden bij geeft: dat is ook beleving."),
            ("p", "Een mening over een boek begin je met een reden: <strong><em>I liked it "
                  "because…</em></strong>. <em>The book has 300 pages</em> en <em>It was published in "
                  "2019</em> zijn feiten, geen mening."),
            ("p", tabel(["Engels", "Nederlands"], [
                ["a <strong>story</strong>, a tale", "een verhaal"],
                ["a <strong>poem</strong>", "een gedicht"],
                ["a <strong>character</strong>", "een <strong>personage</strong>"],
                ["the <strong>plot</strong>", "de <strong>verhaallijn</strong>: wat er gebeurt"],
                ["the <strong>setting</strong>", "<strong>waar en wanneer</strong> het verhaal speelt"],
                ["a <strong>review</strong>", "een <strong>recensie</strong>"],
                ["a <strong>vlog</strong>", "een <strong>dagboek in beeld</strong>"],
                ["to <strong>identify with a character</strong>", "<strong>je in een personage herkennen</strong>"],
            ])),
            ("kader", "Bij een verhaal kan de fiche je vragen om <strong>zelf een einde te "
                      "verzinnen</strong>, of om te vertellen hoe het verder zou gaan. Dat is geen "
                      "strafwerk: het is de eenvoudigste manier om te laten zien dat je het verhaal "
                      "begrepen hebt."),
        ]),
        spreken("neem met je telefoon één minuut op waarin je in het Engels vertelt wat je deze zomer "
                "gaat doen, met <em>I am going to…</em>. Beluister het daarna zelf en schrijf op welk "
                "woord je miste."),
    ])


# ───────────────────── 5. Woordvelden: dagelijks leven, eten en wonen
zet("woordvelden-dagelijks-leven-eten-en-wonen",
    "Woordvelden: dagelijks leven, eten en wonen",
    "Huren en wonen, het huishouden, samenleven, eten en een restaurant, en wat je in je vrije tijd doet.",
    secties("woordvelden-wonen-eten-en-vrije-tijd") + [
        dict(kop="Familie, maaltijden en wat je thuis zegt", blokken=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["a <strong>relative</strong>", "een <strong>familielid</strong>"],
                ["a <strong>cousin</strong>", "een neef of een nicht, het kind van je tante of nonkel"],
                ["a <strong>nephew</strong>, a <strong>niece</strong>", "de zoon of de dochter van je broer of zus"],
                ["an <strong>aunt</strong>, an <strong>uncle</strong>", "een tante, een nonkel"],
                ["a <strong>tenant</strong>", "een <strong>huurder</strong>; de huisbaas is <em>a landlord</em>"],
            ])),
            ("p", tabel(["Engels", "Nederlands"], [
                ["<strong>breakfast</strong>", "het <strong>ontbijt</strong>"],
                ["<strong>lunch</strong>", "het middagmaal"],
                ["<strong>dinner</strong>, <strong>supper</strong>", "het <strong>avondmaal</strong>, de warme maaltijd"],
                ["a <strong>snack</strong>", "een <strong>tussendoortje</strong>"],
                ["<strong>spicy</strong>", "<strong>pikant</strong>, scherp gekruid"],
            ])),
            ("kader", "<strong>A chip is in het Verenigd Koninkrijk een frietje</strong>, zoals in "
                      "<em>fish and chips</em>. In de Verenigde Staten is <em>a chip</em> net een "
                      "chipje uit een zakje, en heet een frietje <em>a French fry</em>. Eén woord, twee "
                      "borden."),
            ("p", tabel(["Engels", "Nederlands"], [
                ["to <strong>get on well with someone</strong>", "goed met iemand <strong>overeenkomen</strong>"],
                ["to be <strong>fed up with something</strong>", "er <strong>genoeg</strong> van hebben"],
                ["to have a <strong>lie-in</strong>", "<strong>uitslapen</strong>"],
                ["to <strong>do the washing-up</strong>", "<strong>afwassen</strong>"],
                ["to <strong>tidy up</strong>", "<strong>opruimen</strong>"],
                ["to <strong>move house</strong>", "<strong>verhuizen</strong>"],
                ["a <strong>hobby</strong>", "een <strong>vrijetijdsbesteding</strong>"],
            ])),
            ("p", "Bij een <strong>feest</strong> horen <strong>a candle</strong> (een kaars), "
                  "<strong>a present</strong> (een cadeau), <em>a cake</em> en <em>balloons</em>."),
            ("kader", "Drie vaste vormen waar het vaak op misgaat. Je zegt <strong>to make a "
                      "mistake</strong>, niet <em>to do a mistake</em>. <strong>Advice</strong> is "
                      "ontelbaar, dus <strong>niet</strong> <em>two advices</em> maar <em>two pieces of "
                      "advice</em>. En je gaat <strong>by bus</strong> naar de cinema, dus "
                      "<strong>niet</strong> <em>I am going to the cinema <s>with</s> the bus</em>."),
        ]),
        dict(kop="Het huis van kelder tot zolder", blokken=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["a <strong>flat</strong>", "een <strong>appartement</strong> (in het Verenigd Koninkrijk; de VS zeggen <em>an apartment</em>)"],
                ["a <strong>cottage</strong>", "een <strong>huisje op het platteland</strong>, dus geen groot huis in de stad"],
                ["a <strong>cellar</strong>", "een <strong>kelder</strong>"],
                ["an <strong>attic</strong>, a <strong>loft</strong>", "een <strong>zolder</strong>"],
                ["the <strong>landing</strong>", "de <strong>overloop</strong> boven de trap"],
                ["the <strong>hall</strong>", "de inkomhal"],
                ["the <strong>loo</strong>", "het <strong>toilet</strong> (spreektaal; netter is <em>the toilet</em>)"],
            ])),
            ("p", tabel(["Engels", "Nederlands"], [
                ["a <strong>kettle</strong>", "een waterkoker"],
                ["a <strong>bin</strong>", "een <strong>vuilnisbak</strong>"],
                ["a <strong>curtain</strong>, <strong>curtains</strong>", "een <strong>gordijn</strong>, gordijnen"],
                ["a <strong>boiler</strong>", "de <strong>verwarmingsketel</strong> die je water opwarmt"],
                ["<strong>cosy</strong>", "<strong>gezellig</strong>, behaaglijk"],
            ])),
            ("kader", "<strong>Furniture is geen meervoud.</strong> Waar wij \"meubels\" zeggen, is "
                      "<em>furniture</em> in het Engels <strong>ontelbaar</strong>: <em>the furniture "
                      "<strong>is</strong> new</em>, en één stuk is <em>a piece of furniture</em>. En je "
                      "zegt <strong>at home zonder lidwoord</strong>: <em>I am at home</em>, niet "
                      "<em>at the home</em>."),
        ]),
        spreken("beschrijf in het Engels je eigen keuken, hardop, in tien zinnen. Zoek achteraf de "
                "drie woorden op die je miste en schrijf ze in je woordenschrift."),
    ])


# ───────────────────── 6. Woordvelden: gezondheid, natuur en duurzaamheid
zet("woordvelden-gezondheid-natuur-en-duurzaamheid",
    "Woordvelden: gezondheid, natuur en duurzaamheid",
    "Naar de dokter, je geestelijke gezondheid, natuur en dieren, het klimaat en duurzaamheid.",
    secties("woordvelden-gezondheid-natuur-en-duurzaamheid") + [
        dict(kop="Bij de dokter en in het ziekenhuis", blokken=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["a <strong>sore throat</strong>", "<strong>keelpijn</strong>"],
                ["a <strong>fever</strong>, a <strong>temperature</strong>", "<strong>koorts</strong>"],
                ["a <strong>plaster</strong>", "een <strong>pleister</strong>"],
                ["a <strong>prescription</strong>", "een <strong>voorschrift</strong> van de dokter"],
                ["a <strong>chemist's</strong>, a <strong>pharmacy</strong>", "de <strong>apotheek</strong> (de VS zeggen <em>a drugstore</em>)"],
                ["a <strong>check-up</strong>", "een <strong>controle</strong> bij de dokter"],
                ["to <strong>recover</strong>", "<strong>herstellen</strong>, genezen"],
                ["an <strong>ambulance</strong>", "een ziekenwagen"],
                ["an <strong>operation</strong>", "een operatie"],
                ["a <strong>ward</strong>", "een afdeling in het ziekenhuis"],
            ])),
            ("p", "Een <strong>balanced diet</strong> is een <strong>gevarieerde voeding</strong>, en "
                  "niet een dieet om te vermageren; dat laatste is <em>to be on a diet</em>."),
        ]),
        dict(kop="Hoe je je voelt", blokken=[
            ("p", "<strong>Mental health gaat over je geest, niet over je lichaam.</strong> De fiche "
                  "vraagt er woorden voor, want erover kunnen spreken is het punt."),
            ("p", tabel(["Engels", "Nederlands"], [
                ["<strong>lonely</strong>", "eenzaam"],
                ["<strong>nervous</strong>", "zenuwachtig"],
                ["<strong>exhausted</strong>", "<strong>uitgeput</strong>, helemaal op"],
                ["to be <strong>stressed out</strong>", "<strong>overspannen</strong> zijn"],
                ["to <strong>feel blue</strong>", "zich wat <strong>triest</strong> voelen"],
                ["to <strong>take it easy</strong>", "het <strong>rustig</strong> aan doen"],
                ["<strong>sleep</strong>", "de <strong>slaap</strong> (het naamwoord; het werkwoord is <em>to sleep</em>)"],
            ])),
        ]),
        dict(kop="Natuur, weer en duurzaamheid", blokken=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["a <strong>squirrel</strong>", "een eekhoorn"],
                ["a <strong>hedgehog</strong>", "een egel"],
                ["an <strong>owl</strong>", "een uil"],
                ["a <strong>stream</strong>", "een <strong>beek</strong>"],
                ["to <strong>cut down a tree</strong>", "een boom <strong>omhakken</strong>"],
                ["to <strong>go extinct</strong>", "<strong>uitsterven</strong>"],
                ["<strong>deciduous</strong>", "bladverliezend: een boom die zijn <strong>bladeren in de winter verliest</strong>"],
                ["<strong>evergreen</strong>", "altijdgroen, zoals een naaldboom"],
            ])),
            ("p", "Bij het <strong>weer</strong> horen <strong>a breeze</strong> (een briesje), "
                  "<strong>a shower</strong> (een regenbui) en <strong>a thunderstorm</strong> (een "
                  "onweer). <strong>Climate en weather betekenen niet hetzelfde</strong>: "
                  "<em>weather</em> is het weer van vandaag, <em>climate</em> het gemiddelde over "
                  "dertig jaar."),
            ("p", tabel(["Engels", "Nederlands"], [
                ["<strong>sustainable</strong>", "<strong>duurzaam</strong>"],
                ["<strong>renewable energy</strong>", "<strong>hernieuwbare energie</strong>: zon, wind, water"],
                ["to <strong>recycle</strong>", "<strong>hergebruiken</strong>, recycleren"],
                ["<strong>waste</strong>, <strong>rubbish</strong>", "<strong>afval</strong> (de VS zeggen <em>garbage</em> of <em>trash</em>)"],
                ["<strong>emissions</strong>", "de uitstoot"],
                ["<strong>pollution</strong>", "de vervuiling"],
                ["a <strong>carbon footprint</strong>", "een <strong>koolstofvoetafdruk</strong>"],
                ["a <strong>flood</strong>", "een <strong>overstroming</strong>"],
            ])),
        ]),
        spreken("vertel in het Engels aan iemand thuis wat je zou zeggen bij een dokter in Londen: wat "
                "er scheelt, sinds wanneer, en wat je al genomen hebt."),
    ])


# ───────────────────── 7. Woordvelden: school, werk, geld en verkeer
zet("woordvelden-school-werk-geld-en-verkeer",
    "Woordvelden: school, werk, geld en verkeer",
    "School, werk zoeken en werken, winkelen en betalen, sparen en lenen, en het verkeer.",
    secties("woordvelden-school-werk-geld-en-verkeer") + [
        dict(kop="School en werk", blokken=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["a <strong>teacher</strong>", "een <strong>leerkracht</strong>"],
                ["a <strong>report</strong>", "een <strong>rapport</strong>"],
                ["a <strong>timetable</strong>", "een <strong>lessenrooster</strong>"],
                ["a <strong>subject</strong>", "een vak"],
                ["to <strong>pass an exam</strong>", "<strong>slagen</strong> voor een examen; mislukken is <em>to fail</em>"],
            ])),
            ("kader", "<strong>Homework is ontelbaar.</strong> Dus <em>I have a lot of "
                      "<strong>homework</strong></em> en niet <em>homeworks</em>; één opdracht is "
                      "<em>a piece of homework</em> of <em>an assignment</em>. Hetzelfde geldt voor "
                      "<em>information</em>, <em>advice</em> en <em>furniture</em>."),
            ("p", tabel(["Engels", "Nederlands"], [
                ["a <strong>shop assistant</strong>", "een winkelbediende"],
                ["a <strong>plumber</strong>", "een <strong>loodgieter</strong>"],
                ["a <strong>trainee</strong>", "iemand die <strong>opgeleid</strong> wordt, een stagiair"],
                ["a <strong>salary</strong>", "het <strong>maandloon</strong>; een weekloon of uurloon is <em>wages</em>"],
                ["a <strong>skill</strong>", "een <strong>vaardigheid</strong>, iets wat je kan"],
                ["a <strong>part-time job</strong>", "<strong>deeltijds</strong> werk; volledig is <em>full-time</em>"],
                ["<strong>unemployed</strong>, <strong>jobless</strong>", "<strong>werkloos</strong>"],
            ])),
            ("p", "Bij <strong>werk zoeken</strong> horen <strong>a vacancy</strong> (een vacature), "
                  "<strong>an application</strong> (een sollicitatie), <em>an interview</em> en een "
                  "<strong>CV</strong>: <strong>een overzicht van je loopbaan</strong> en je diploma's."),
            ("kader", "<strong>To be made redundant betekent niet promotie krijgen maar ontslagen "
                      "worden</strong>, omdat je job wegvalt. Promotie krijgen is <em>to get a "
                      "promotion</em>."),
        ]),
        dict(kop="Winkelen en het verkeer", blokken=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["a <strong>customer</strong>", "een <strong>klant</strong>"],
                ["a <strong>receipt</strong>", "een <strong>kassabon</strong> (de p zwijgt: je zegt <em>riesiet</em>)"],
                ["a <strong>trolley</strong>", "een winkelkar"],
                ["the <strong>checkout</strong>", "de kassa"],
                ["to <strong>refund</strong>", "<strong>terugbetalen</strong>"],
            ])),
            ("p", tabel(["Engels", "Nederlands"], [
                ["a <strong>driving licence</strong>", "een <strong>rijbewijs</strong> (de VS schrijven <em>driver's license</em>)"],
                ["<strong>petrol</strong>", "<strong>benzine</strong> (de VS zeggen <em>gas</em>)"],
                ["a <strong>motorway</strong>", "een <strong>snelweg</strong> (de VS zeggen <em>a highway</em>)"],
                ["a <strong>zebra crossing</strong>", "een <strong>zebrapad</strong>, dus geen dierentuin"],
                ["the <strong>pavement</strong>", "het <strong>voetpad</strong> in het Verenigd Koninkrijk, niet het wegdek"],
                ["a <strong>lorry</strong>", "een <strong>vrachtwagen</strong> (de VS zeggen <em>a truck</em>)"],
                ["to <strong>commute</strong>", "<strong>pendelen</strong> naar je werk"],
                ["<strong>rush hour</strong>", "het <strong>spitsuur</strong>"],
            ])),
        ]),
        spreken("schrijf in het Engels een sollicitatiemail van tien regels voor een vakantiejob, en "
                "lees hem daarna luidop voor om te horen of hij vlot klinkt."),
    ])


# ───────────────────── 8. Woordvelden: kunst, geschiedenis en de samenleving
GESCHIEDENIS = dict(kop="Geschiedenis", blokken=[
    ("p", tabel(["Engels", "Nederlands"], [
        ["a <strong>century</strong>", "een <strong>eeuw</strong>"],
        ["<strong>ancient</strong>", "<strong>heel oud</strong>, uit de oudheid"],
        ["an <strong>empire</strong>", "een <strong>rijk</strong>"],
        ["an <strong>heir</strong>", "een <strong>erfgenaam</strong> (de h zwijgt: je zegt <em>an air</em>)"],
        ["a <strong>war</strong>", "een oorlog"],
        ["a <strong>treaty</strong>", "een verdrag"],
        ["a <strong>revolution</strong>", "een omwenteling"],
        ["a <strong>battle</strong>", "een veldslag"],
    ])),
    ("p", "Een <strong>saucer</strong> hoort niet in dit rijtje: dat is het schoteltje onder je kopje."),
])

THEATER_EN_MUZIEK = dict(kop="Theater, muziek en het meesterwerk", blokken=[
    ("p", tabel(["Engels", "Nederlands"], [
        ["a <strong>stage</strong>", "een <strong>podium</strong>"],
        ["an <strong>audience</strong>, a crowd", "het <strong>publiek</strong>, de zaal"],
        ["a <strong>performance</strong>", "een voorstelling"],
        ["to <strong>rehearse</strong>", "<strong>repeteren</strong>, dus oefenen vóór de voorstelling"],
        ["a <strong>conductor</strong>", "een <strong>dirigent</strong>, en niét een componist; een componist is <em>a composer</em>"],
        ["a <strong>masterpiece</strong>", "een <strong>meesterwerk</strong>"],
        ["a <strong>sculpture</strong>, a statue", "een <strong>beeldhouwwerk</strong>"],
        ["a <strong>painting</strong>", "een <strong>schilderij</strong>; een tekening is <em>a drawing</em>"],
    ])),
    ("kader", "Twee woorden die vaak verward worden. <strong>A rhyme is een rijm</strong>, niet een "
              "ritme in de muziek; dat laatste is <em>a rhythm</em>. En <strong>a plot</strong> is in "
              "een verhaal de <strong>verhaallijn</strong>, maar buiten een verhaal een "
              "<strong>complot</strong>: <em>a plot to overthrow the king</em>."),
    ("p", "Bij een museum horen <strong>an exhibition</strong> (een tentoonstelling), "
          "<strong>a gallery</strong> (een zaal of een galerie) en <strong>an entrance fee</strong> "
          "(het inkomgeld). <em>A referee</em> is de scheidsrechter en hoort bij de sport."),
])

zet("woordvelden-kunst-geschiedenis-en-de-samenleving",
    "Woordvelden: kunst, geschiedenis en de samenleving",
    "Boeken en theater, de woorden van de geschiedenis, de politiek en de samenleving.",
    [
        sectie("woordvelden-kunst-literatuur-politiek-en-reizen", "Een boek en een verhaal"),
        sectie("woordvelden-kunst-literatuur-politiek-en-reizen", "Kunst en erfgoed"),
        dict(kop="Het boek zelf", blokken=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["an <strong>author</strong>", "de <strong>schrijver</strong> van een boek"],
                ["a <strong>novel</strong>", "een <strong>roman</strong>, dus niet iets nieuws"],
                ["a <strong>chapter</strong>", "een <strong>hoofdstuk</strong>"],
                ["<strong>fiction</strong>", "<strong>verzonnen verhalen</strong>; waargebeurde boeken zijn <em>non-fiction</em>"],
                ["a <strong>biography</strong>", "het verhaal van <strong>iemands leven</strong>"],
            ])),
            ("p", "De <strong>Prime Minister</strong> is in het <strong>Verenigd Koninkrijk</strong> "
                  "de <strong>regeringsleider</strong>; een staatshoofd heeft het land niet, daar is de "
                  "koning of de koningin."),
        ]),
        THEATER_EN_MUZIEK,
        GESCHIEDENIS,
        sectie("woordvelden-kunst-literatuur-politiek-en-reizen", "Politiek in Groot-Brittannië", extra=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["an <strong>election</strong>", "een <strong>verkiezing</strong>"],
                ["a <strong>party</strong>", "een partij (en ook een feest)"],
                ["a <strong>minister</strong>", "een minister"],
                ["<strong>parliament</strong>", "het parlement"],
                ["a <strong>law</strong>, an <strong>act</strong>", "een <strong>wet</strong>"],
                ["a <strong>citizen</strong>", "een <strong>burger</strong> van een land"],
                ["to <strong>protest</strong>", "<strong>betogen</strong>"],
                ["a <strong>council</strong>", "een <strong>gemeenteraad</strong>"],
            ])),
            ("p", "<em>A bargain</em> hoort hier niet bij: dat is een koopje in de winkel."),
        ]),
        sectie("woordvelden-kunst-literatuur-politiek-en-reizen", "De samenleving", extra=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["<strong>poverty</strong>", "armoede"],
                ["<strong>equality</strong>", "gelijkheid; het tegendeel is <em>inequality</em>"],
                ["a <strong>charity</strong>", "een <strong>goed doel</strong>, een vereniging die geld inzamelt"],
                ["to <strong>volunteer</strong>", "<strong>vrijwillig helpen</strong>"],
                ["a <strong>refugee</strong>", "een <strong>vluchteling</strong>"],
                ["<strong>discrimination</strong>", "<strong>ongelijke behandeling</strong>"],
                ["a <strong>majority</strong>", "een <strong>meerderheid</strong>; een minderheid is <em>a minority</em>"],
                ["<strong>human rights</strong>", "de <strong>mensenrechten</strong>"],
                ["a <strong>tax</strong>, taxes", "een <strong>belasting</strong>"],
                ["the <strong>media</strong>", "de <strong>pers en de omroepen</strong>"],
                ["a <strong>survey</strong>", "een <strong>enquête</strong>"],
                ["a <strong>border control</strong>", "een <strong>grenscontrole</strong>"],
            ])),
            ("p", "Bij het <strong>recht</strong> horen <strong>a judge</strong> (een rechter), "
                  "<strong>a court</strong> (een rechtbank) en <strong>a lawyer</strong> (een advocaat). "
                  "<em>A landlord</em> hoort bij het wonen: dat is je huisbaas. En "
                  "<strong>a trade union is een vakbond</strong>, geen handelsbeurs; een handelsbeurs is "
                  "<em>a trade fair</em>. <em>A receipt</em> is het kasticket en hoort bij het winkelen."),
        ]),
        spreken("lees een kort artikel op de site van een Britse krant over een verkiezing of een "
                "betoging, en vat het daarna in vijf Engelse zinnen samen voor iemand thuis."),
    ])


# ───────────────────── 9. Woordvelden: wetenschap, techniek en taal
zet("woordvelden-wetenschap-techniek-en-taal",
    "Woordvelden: wetenschap, techniek en taal",
    "Onderzoek, techniek en computers, en hoe je zelf een onbekend woord uit elkaar haalt.",
    secties("woordvelden-wetenschap-techniek-en-taal") + [
        dict(kop="Techniek en de computer", blokken=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["a <strong>laboratory</strong>, a lab", "een <strong>labo</strong>"],
                ["a <strong>vaccine</strong>", "een <strong>vaccin</strong>"],
                ["a <strong>battery</strong>", "een <strong>batterij</strong>; de <strong>lader</strong> is <em>a charger</em>"],
                ["to <strong>charge a phone</strong>", "een gsm <strong>opladen</strong>"],
                ["a <strong>gadget</strong>", "een <strong>handig toestelletje</strong>"],
                ["a <strong>screenshot</strong>", "een <strong>schermafbeelding</strong>"],
                ["a <strong>spreadsheet</strong>", "een <strong>rekenblad</strong>, zoals Excel; geen laken"],
            ])),
            ("p", "<strong>To download en to upload zijn het omgekeerde van elkaar</strong>: "
                  "binnenhalen tegenover versturen."),
        ]),
        dict(kop="Sport en vrije tijd", blokken=[
            ("p", tabel(["Engels", "Nederlands"], [
                ["a <strong>match</strong>", "een <strong>wedstrijd</strong>, een voetbalmatch"],
                ["a <strong>referee</strong>", "een scheidsrechter"],
                ["to <strong>score a goal</strong>", "een <strong>doelpunt</strong> maken"],
                ["a <strong>draw</strong>", "een <strong>gelijkspel</strong>"],
                ["<strong>chess</strong>", "het <strong>schaakspel</strong>"],
                ["a <strong>jigsaw</strong>", "een legpuzzel"],
                ["a <strong>board game</strong>", "een gezelschapsspel"],
            ])),
        ]),
        dict(kop="Voor- en achtervoegsels, en woorden die lijken", blokken=[
            ("p", "Een woord dat je niet kent, valt vaak uiteen in stukken die je wél kent."),
            ("p", tabel(["Stuk", "Wat het doet", "Voorbeeld"], [
                ["<strong>un-</strong>", "<strong>ontkent</strong> wat erna komt",
                 "<strong>unhealthy</strong> = ongezond, <strong>unfair</strong> = onrechtvaardig"],
                ["<strong>dis-</strong>", "ontkent ook", "<strong>disagree</strong> = niet akkoord gaan"],
                ["<strong>im-</strong>, <strong>in-</strong>", "ontkent ook", "<strong>impossible</strong> = onmogelijk"],
                ["<strong>-ful</strong>", "<strong>vol van</strong>", "<strong>helpful</strong> = behulpzaam, <em>careful</em> = zorgvuldig"],
                ["<strong>-less</strong>", "zonder", "<em>useless</em> = nutteloos"],
                ["<strong>-ly</strong>", "maakt van een bijvoeglijk naamwoord een <strong>bijwoord</strong>",
                 "slow → <strong>slowly</strong>, careful → carefully"],
            ])),
            ("p", "Een <strong>samenstelling</strong> is één woord uit twee woorden: "
                  "<strong>football</strong>, <strong>homework</strong>, "
                  "<strong>sunglasses</strong>, <em>bedroom</em>, <em>timetable</em>."),
            ("p", tabel(["Woord", "Betekent", "Niet"], [
                ["<strong>sympathetic</strong>", "<strong>meelevend</strong>, begripvol", "sympathiek (dat is <em>nice</em> of <em>likeable</em>)"],
                ["to <strong>control</strong>", "<strong>besturen</strong>, beheersen", "controleren (dat is <em>to check</em>)"],
                ["a <strong>library</strong>", "een <strong>bibliotheek</strong>", "een <strong>boekhandel</strong> (dat is <em>a bookshop</em>)"],
                ["to <strong>realise</strong>", "<strong>beseffen</strong>", "realiseren in de zin van verwezenlijken"],
                ["to <strong>make sense</strong>", "<strong>logisch</strong> zijn, steek houden", "iets voelen"],
            ])),
            ("kader", "<strong>Woordparen die vaak verward worden:</strong> <em>its</em> (van hem of "
                      "haar) en <em>it's</em> (it is) — <em>The dog wagged <strong>its</strong> "
                      "tail</em>; <em>their</em>, <em>there</em> en <em>they're</em>; <em>your</em> en "
                      "<em>you're</em>; <em>lose</em> en <em>loose</em>; <em>then</em> en <em>than</em>."),
            ("p", tabel(["Brits", "Amerikaans"], [
                ["<strong>autumn</strong>", "<strong>fall</strong> (de herfst)"],
                ["a <strong>biscuit</strong>", "a <strong>cookie</strong> (een koekje)"],
                ["a <strong>lift</strong>", "an <strong>elevator</strong>; <em>a lorry</em> is geen lift maar een vrachtwagen"],
                ["<strong>colour</strong>, favourite, centre", "<strong>color</strong>, favorite, center"],
            ])),
            ("p", "<strong>Colour en color zijn allebei juist</strong>, elk in een andere "
                  "<strong>variant</strong> van het Engels. Kies er één en blijf erbij in dezelfde "
                  "tekst."),
        ]),
        spreken("kies een Engelse handleiding van een toestel dat je thuis hebt, lees één bladzijde en "
                "leg daarna in het Engels uit hoe je het toestel aanzet."),
    ])


# ───────────────────── 10. Naamwoorden, lidwoorden en hoeveelheden
zet("naamwoorden-lidwoorden-en-hoeveelheden",
    "Naamwoorden, lidwoorden en hoeveelheden",
    "Het meervoud, telbaar en ontelbaar, de bezitsvorm, de lidwoorden, en hoeveelheden, getallen en "
    "datums.",
    secties("naamwoorden-lidwoorden-en-hoeveelheden") + [
        dict(kop="Getallen, rangtelwoorden en landen", blokken=[
            ("p", tabel(["Getal", "Rangtelwoord", "Let op"], [
                ["one", "<strong>first</strong> (1st)", "onregelmatig"],
                ["two", "<strong>second</strong> (2nd)", "onregelmatig"],
                ["three", "<strong>third</strong> (3rd)", "onregelmatig"],
                ["five", "<strong>fifth</strong> (5th)", "de <em>e</em> valt weg"],
                ["eight", "<strong>eighth</strong> (8th)", "één t, niet twee"],
                ["nine", "<strong>ninth</strong> (9th)", "de <em>e</em> valt weg"],
                ["twelve", "<strong>twelfth</strong> (12th)", "ve wordt f"],
                ["twenty", "<strong>twentieth</strong> (20th)", "y wordt ie"],
            ])),
            ("p", "De andere rangtelwoorden maak je gewoon met <strong>-th</strong>: <em>fourth</em>, "
                  "<em>sixth</em>, <em>tenth</em>, <em>hundredth</em>."),
            ("p", "Een <strong>jaartal</strong> lees je in twee helften: <strong>1975 = nineteen "
                  "seventy-five</strong>, 1912 = nineteen twelve, 2027 = twenty twenty-seven. Een "
                  "<strong>breuk</strong> lees je met een rangtelwoord: <strong>3/4 = three "
                  "quarters</strong>, 1/3 = a third, 2/5 = two fifths."),
            ("kader", "<strong>Je zegt niet the Belgium.</strong> De meeste landen krijgen geen "
                      "lidwoord: <em>Belgium</em>, <em>France</em>, <em>Scotland</em>. Alleen een "
                      "meervoud of een samenstelling krijgt er een: <em>the Netherlands</em>, "
                      "<em>the United Kingdom</em>, <em>the United States</em>."),
            ("p", "Het lidwoord <strong>an</strong> staat voor een <strong>klank</strong> als een "
                  "klinker, niet voor een letter. Dus <strong>an umbrella</strong>, <strong>an "
                  "hour</strong> en <strong>an honest woman</strong> (de h zwijgt), maar <em>a "
                  "university</em> en <em>a European city</em> (je hoort er een j)."),
            ("p", "Eindigt een woord op een consonant plus <strong>-y</strong>, dan wordt het meervoud "
                  "<strong>-ies</strong>: baby → <strong>babies</strong>, city → cities, story → "
                  "stories. Staat er een klinker voor de y, dan niet: boy → boys."),
        ]),
        spreken("vertel in het Engels wat er in je koelkast staat, met <em>some</em>, <em>a lot of</em> "
                "en <em>a few</em> erin, en let op wat telbaar is en wat niet."),
    ])


# ───────────────────── 11. Voornaamwoorden en betrekkelijke bijzinnen
zet("voornaamwoorden-en-betrekkelijke-bijzinnen",
    "Voornaamwoorden en betrekkelijke bijzinnen",
    "Wie doet wat met wie, van wie iets is, en hoe je twee zinnen met who, which of that aan elkaar "
    "hangt.",
    secties("voornaamwoorden-en-betrekkelijke-bijzinnen") + [
        dict(kop="De namen van de voornaamwoorden", blokken=[
            ("p", "In de vragen staan de Nederlandse namen. Dit is welke vorm bij welke naam hoort."),
            ("p", tabel(["Naam", "Vormen", "Voorbeeld"], [
                ["<strong>persoonlijk voornaamwoord</strong>, onderwerp",
                 "I, you, he, she, it, we, they",
                 "<em><strong>She</strong> is my sister.</em> — <em>my sister</em> wordt <strong>she</strong>"],
                ["<strong>persoonlijk voornaamwoord</strong>, voorwerp",
                 "me, you, him, her, it, us, them",
                 "<em>Tom helped me, so I thanked <strong>him</strong>.</em>"],
                ["<strong>bezittelijk voornaamwoord</strong>",
                 "my, your, his, her, <strong>its</strong>, <strong>our</strong>, their",
                 "<em><strong>Our</strong> house is small.</em> — bij <em>we</em> hoort <strong>our</strong>, bij <em>it</em> hoort <strong>its</strong>"],
                ["<strong>aanwijzend voornaamwoord</strong>",
                 "<strong>this, that, these, those</strong>",
                 "<em><strong>These</strong> books are mine.</em>"],
                ["<strong>wederkerend voornaamwoord</strong>",
                 "myself, yourself, himself, herself, <strong>itself</strong>, ourselves, themselves",
                 "<em>The cat washed <strong>itself</strong>.</em>"],
                ["<strong>onbepaald voornaamwoord</strong>",
                 "someone, <strong>anybody</strong>, <strong>anything</strong>, nothing, everyone",
                 "<em>Is there <strong>anybody</strong> in the room?</em>"],
                ["<strong>betrekkelijk voornaamwoord</strong>",
                 "<strong>who</strong> (personen), which (dingen), that, <strong>whose</strong> (bezit), where, when",
                 "<em>the girl <strong>whose</strong> bike was stolen</em>"],
            ])),
            ("p", "<strong>By myself betekent alleen</strong>, zonder hulp: <em>I did it by "
                  "myself.</em> En <strong>to enjoy oneself betekent zich amuseren</strong>: <em>They "
                  "enjoyed <strong>themselves</strong> at the party.</em>"),
            ("kader", "<strong>Voor jullie bestaat er in het Engels geen apart woord.</strong> "
                      "<em>You</em> is zowel jij als jullie, en het werkwoord verandert niet mee. Wil je "
                      "duidelijk maken dat je meer mensen bedoelt, dan zeg je <em>you all</em> of "
                      "<em>all of you</em>."),
            ("p", "<strong>How much</strong> vraagt naar een hoeveelheid die je niet kan tellen of "
                  "naar een prijs (<em>How much is it?</em>), <strong>how many</strong> naar een aantal "
                  "(<em>How many people?</em>). Verder vragen <strong>how long</strong>, "
                  "<strong>how far</strong> en <strong>how old</strong> naar een maat."),
        ]),
        spreken("beschrijf in het Engels drie mensen uit je klas zonder hun naam te noemen, met "
                "<em>the one who…</em>, en laat iemand raden wie je bedoelt."),
    ])


# ───────────────────── 12. Bijvoeglijke naamwoorden, bijwoorden en voorzetsels
zet("bijvoeglijke-naamwoorden-bijwoorden-en-voorzetsels",
    "Bijvoeglijke naamwoorden, bijwoorden en voorzetsels",
    "Hoe iets is, hoe iets gebeurt, de trappen van vergelijking, en de voorzetsels die je vanbuiten "
    "moet kennen.",
    secties("bijvoeglijke-naamwoorden-bijwoorden-en-voorzetsels") + [
        dict(kop="Voorzetsels die vastliggen", blokken=[
            ("p", "Sommige werkwoorden en bijvoeglijke naamwoorden hebben in het Engels een vast "
                  "voorzetsel, en dat is een ander dan in het Nederlands. Die moet je uit het hoofd "
                  "kennen."),
            ("p", tabel(["Engels", "Nederlands"], [
                ["to <strong>listen to</strong> something", "naar iets luisteren — <strong>nooit zonder <em>to</em></strong>"],
                ["to <strong>wait for</strong> someone", "op iemand wachten"],
                ["to <strong>look at</strong>", "naar iets kijken"],
                ["to <strong>depend on</strong>", "van iets afhangen"],
                ["to be <strong>good at</strong>", "goed zijn in"],
                ["to be <strong>interested in</strong>", "geïnteresseerd zijn in"],
                ["to <strong>arrive at</strong> a station, <strong>in</strong> a city", "aankomen"],
            ])),
            ("p", "Een <strong>voorzetselgroep</strong> is een voorzetsel van meer dan één woord: "
                  "<strong>because of</strong> (wegens), <strong>instead of</strong> (in plaats van), "
                  "<strong>in front of</strong> (voor), <em>next to</em>, <em>out of</em>. Let op: "
                  "<em>because</em> alleen is geen voorzetsel maar een voegwoord."),
            ("p", "Voorzetsels van <strong>plaats</strong>: in, on, under, above, behind, between, "
                  "<strong>around</strong> (<em>The shop is <strong>around</strong> the corner</em>), "
                  "opposite. Van <strong>tijd</strong>: at (een uur), on (een dag), in (een maand of "
                  "een jaar, en ook <em>in five minutes</em> voor iets wat straks gebeurt)."),
            ("kader", "<strong>Enough staat achter het bijvoeglijk naamwoord</strong>, niet ervoor: "
                      "<em>This box is not <strong>light enough</strong> to carry alone.</em> Bij een "
                      "naamwoord staat het er wel voor: <em>enough time</em>."),
            ("p", "Een <strong>bijwoord van frequentie</strong> zoals <strong>always</strong>, "
                  "<strong>usually</strong>, <strong>often</strong>, <strong>sometimes</strong> en "
                  "<em>never</em> staat <strong>vóór het hoofdwerkwoord</strong> maar <strong>achter "
                  "een vorm van to be</strong>: <em>She <strong>always</strong> walks to school</em> en "
                  "<em>She is <strong>always</strong> late</em>."),
        ]),
        spreken("vergelijk in het Engels luidop drie steden: welke is <em>bigger</em>, welke is "
                "<em>the most expensive</em>, en welke ligt <em>further</em> van hier."),
    ])


# ───────────────────── 13. De tegenwoordige tijden en de present perfect
zet("de-tegenwoordige-tijden-en-de-present-perfect",
    "De tegenwoordige tijden en de present perfect",
    "Present simple tegenover present continuous, do en does, there is en there are, en de present "
    "perfect met since en for.",
    secties("de-tegenwoordige-tijden-en-de-present-perfect") + [
        dict(kop="De spelling van de -ing-vorm, en de emphatic do", blokken=[
            ("p", tabel(["Regel", "Voorbeeld"], [
                ["gewoon -ing erbij", "play → <strong>playing</strong>, read → reading"],
                ["een stomme <em>-e</em> valt weg", "make → <strong>making</strong>, write → <strong>writing</strong>, come → coming"],
                ["één klinker plus één consonant: de consonant verdubbelt",
                 "swim → <strong>swimming</strong>, run → running, sit → sitting, get → getting"],
                ["<em>-ie</em> wordt <em>-y</em>", "lie → lying, die → dying"],
            ])),
            ("p", "Dus <em>swimming</em>, <em>making</em> en <em>writing</em> zijn juist gespeld, en "
                  "<em>swiming</em>, <em>makeing</em> en <em>writting</em> niet."),
            ("p", "De <strong>emphatic do</strong> gebruik je om iets te <strong>benadrukken</strong> "
                  "in een bevestigende zin: <em>I <strong>do</strong> like it!</em> of <em>She "
                  "<strong>does</strong> know the answer.</em> Je spreekt de <em>do</em> dan met nadruk "
                  "uit; in gewone zinnen laat je hem weg."),
            ("kader", "<strong>Bij een vast uurrooster gebruik je de present simple</strong>, ook als "
                      "het over de toekomst gaat: <em>The train <strong>leaves</strong> at six</em>, "
                      "<em>The film <strong>starts</strong> at half past eight</em>. Dat is precies "
                      "zoals wij het zeggen: \"de trein vertrekt om zes uur\"."),
        ]),
        spreken("vertel in het Engels wat je elke dag doet (present simple) en wat je nú aan het doen "
                "bent (present continuous), vijf zinnen van elk, en hoor het verschil."),
    ])


# ───────────────────── 14. De verleden tijden
zet("de-verleden-tijden",
    "De verleden tijden",
    "De past simple met haar onregelmatige werkwoorden, vragen en ontkenningen, en de past continuous.",
    secties("de-verleden-tijden", weglaten=("De past perfect",)) + [
        dict(kop="Past simple of past continuous", blokken=[
            ("p", "De twee verleden tijden van deze fiche werken samen in één zin. De "
                  "<strong>past continuous</strong> schetst wat <strong>bezig was</strong>, de "
                  "<strong>past simple</strong> zegt wat er <strong>gebeurde</strong>."),
            ("p", "<em>I <strong>was walking</strong> home when it <strong>started</strong> to "
                  "rain.</em> Het wandelen was bezig, de regen kwam erin. Omgekeerd klopt het niet: "
                  "<em>I walked home when it was starting to rain</em> vertelt een ander verhaal."),
            ("kader", "De <strong>past perfect</strong> (<em>I had seen</em>) staat niet op deze "
                      "fiche. Je hebt dus genoeg aan de past simple en de past continuous; wil je zeggen "
                      "dat iets eerder gebeurde, dan doe je dat met <em>first</em>, <em>before</em> of "
                      "<em>earlier</em>."),
        ]),
        dict(kop="De spelling van de past simple, en wat niet in de past continuous past", blokken=[
            ("p", tabel(["Regel", "Voorbeeld"], [
                ["gewoon -ed erbij", "work → <strong>worked</strong>, <strong>played</strong>, opened"],
                ["een stomme <em>-e</em>: enkel -d", "close → <strong>closed</strong>, live → lived"],
                ["consonant plus <em>-y</em>: y wordt i",
                 "carry → <strong>carried</strong>, study → <strong>studied</strong>, try → tried"],
                ["één klinker plus één consonant: verdubbelen", "stop → stopped, plan → planned"],
            ])),
            ("p", "<strong>Play wordt played</strong> en niet <em>plaied</em>: voor de y staat een "
                  "klinker. En de onregelmatige werkwoorden volgen geen regel: <strong>to think wordt "
                  "thought</strong> en niet <em>thinked</em>, <em>go → went</em>, <em>see → saw</em>, "
                  "<em>buy → bought</em>, <em>bring → brought</em>."),
            ("kader", "Na <strong>did</strong> en <strong>didn't</strong> staat de "
                      "<strong>kale vorm</strong>, want <em>did</em> draagt de verleden tijd al: "
                      "<em>I <strong>didn't know</strong> the answer</em>, niet <em>I didn't "
                      "<s>knew</s></em>."),
            ("p", "Een verhaal zet de <strong>achtergrond</strong> in de past continuous en de "
                  "gebeurtenissen in de past simple: <em>The sun <strong>was shining</strong> and the "
                  "birds <strong>were singing</strong>. Then the door <strong>opened</strong>.</em> "
                  "Twee handelingen die samen bezig waren, staan <strong>allebei in de past "
                  "continuous</strong>: <em>She was reading while he was cooking.</em>"),
            ("p", "Het voegwoord voor de lange handeling is <strong>while</strong> (ook geschreven als "
                  "<em>whilst</em>), en voor de korte <strong>when</strong>: <em>She fell "
                  "<strong>while</strong> she was running down the stairs.</em>"),
            ("kader", "<strong>Werkwoorden die een toestand uitdrukken, staan zelden in een "
                      "continuous vorm:</strong> <strong>to know</strong>, <strong>to "
                      "believe</strong>, to understand, to like, to want, to need. Je zegt dus "
                      "<em>I <strong>knew</strong> him well</em> en niet <em>I <s>was knowing</s> him "
                      "well</em>."),
        ]),
        spreken("vertel in het Engels in tien zinnen wat je gisteren deed, en gebruik minstens drie "
                "onregelmatige werkwoorden: <em>went</em>, <em>saw</em>, <em>had</em>, <em>made</em>."),
    ])


# ───────────────────── 15. De toekomende tijd en de modale hulpwerkwoorden
zet("de-toekomende-tijd-en-de-modale-hulpwerkwoorden",
    "De toekomende tijd en de modale hulpwerkwoorden",
    "Will, going to en de present continuous voor de toekomst, de modalen, en de gebiedende wijs.",
    secties("de-toekomst-de-modale-hulpwerkwoorden-en-de-gerund",
            weglaten=("De semi-auxiliaries", "Gerund of infinitief")) + [
        dict(kop="De korte vormen, de bevelen en de wederkerende werkwoorden", blokken=[
            ("p", tabel(["Volle vorm", "Korte vorm"], [
                ["I will", "I'll"],
                ["<strong>will not</strong>", "<strong>won't</strong>"],
                ["<strong>must not</strong>", "<strong>mustn't</strong> = het mág niet"],
                ["<strong>do not have to</strong>", "<strong>don't have to</strong> = het <strong>hoeft</strong> niet"],
                ["cannot", "can't"],
            ])),
            ("kader", "<strong>Mustn't en don't have to betekenen niet hetzelfde</strong>, en dat is "
                      "de valstrik. <em>You <strong>mustn't</strong> touch that</em> is een verbod. "
                      "<em>You <strong>don't have to</strong> come</em> betekent dat je mag, maar niet "
                      "moet. Vandaar ook <em>You <strong>don't have to</strong> worry, everything is "
                      "fine.</em>"),
            ("p", "Een <strong>ontkennend bevel</strong> maak je met <strong>don't</strong>: "
                  "<em><strong>Don't</strong> touch that!</em> Een gewoon bevel heeft geen onderwerp en "
                  "gebruikt de kale vorm: <em>Close the door.</em>"),
            ("p", "<strong>May I come in?</strong> betekent <strong>mag ik binnenkomen?</strong> "
                  "<em>May</em> en <em>could</em> klinken hoffelijker dan <em>can</em>: "
                  "<strong>could is hoffelijker dan can</strong>."),
            ("p", "Een <strong>wederkerend werkwoord</strong> heeft een voornaamwoord op "
                  "<em>-self</em> bij zich: <em>She enjoyed <strong>herself</strong></em>, <em>He hurt "
                  "<strong>himself</strong></em>, <em>They taught <strong>themselves</strong> to "
                  "cook</em>. <strong>To enjoy oneself betekent zich amuseren.</strong>"),
            ("p", "En een vraag die je op reis nodig hebt: <em>Can you tell me <strong>how to "
                  "get</strong> to the station?</em> Na <em>how</em> komt de infinitief met "
                  "<strong>to</strong>."),
        ]),
        spreken("vraag iemand thuis in het Engels om hulp met <em>Could you…?</em>, geef daarna een "
                "raad met <em>You should…</em>, en beloof iets met <em>I will…</em>."),
    ])


# ───────────────────── 16. Zinsbouw, zinsdelen en de voorwaardelijke bijzin
ZINSDELEN = dict(kop="De zinsdelen op een rij", blokken=[
    ("p", "De fiche noemt vier zinsdelen: het <strong>onderwerp</strong>, de "
          "<strong>persoonsvorm</strong>, het <strong>lijdend voorwerp</strong> en het "
          "<strong>meewerkend voorwerp</strong>. Een bijvoeglijk naamwoord is géén zinsdeel maar een "
          "woordsoort."),
    ("p", tabel(["Zinsdeel", "Vraag die je stelt", "In <em>She gave her brother a present</em>"], [
        ["het <strong>onderwerp</strong>", "wie of wat doet het?", "<strong>she</strong>"],
        ["de <strong>persoonsvorm</strong>", "welk werkwoord verandert mee met het onderwerp?", "<strong>gave</strong>"],
        ["het <strong>lijdend voorwerp</strong>", "wie of wat ondergaat de handeling?", "<strong>a present</strong>"],
        ["het <strong>meewerkend voorwerp</strong>", "aan wie of voor wie?", "<strong>her brother</strong>"],
    ])),
    ("p", "In <em>My little sister plays the violin</em> is het hele stuk <strong>my little "
          "sister</strong> het onderwerp, niet alleen <em>sister</em>. En in <em>The children "
          "<strong>were</strong> playing outside</em> is <strong>were</strong> de persoonsvorm: dat is "
          "het werkwoord dat met het onderwerp meeverandert, niet <em>playing</em>."),
    ("kader", "Het <strong>lijdend voorwerp staat in het Engels vlak achter het werkwoord</strong>, en "
              "de tijd komt pas daarna: <em>I bought <strong>a book</strong> yesterday.</em> Niet "
              "<em>I bought yesterday a book.</em> Dat is een van de verschillen met het Nederlands die "
              "op het examen terugkomen."),
])

CONDITIONALS = dict(kop="De conditionals zero en first", blokken=[
    ("p", "Een <strong>voorwaardelijke bijzin</strong> begint met <strong>if</strong>. Deze fiche "
          "vraagt er twee, en het verschil zit in wat je bedoelt."),
    ("p", tabel(["Soort", "Vorm", "Voorbeeld", "Wat het zegt"], [
        ["<strong>zero conditional</strong>", "<strong>if + present, present</strong>",
         "<em>If you press this, the light <strong>goes</strong> on.</em>",
         "een regel die altijd geldt"],
        ["<strong>first conditional</strong>", "<strong>if + present, will</strong>",
         "<em>If I see her, I <strong>will</strong> tell her.</em>",
         "iets wat echt kan gebeuren"],
    ])),
    ("kader", "<strong>In een first conditional staat will nooit achter if.</strong> Dus "
              "<em>If I <strong>see</strong> her…</em> en niet <em>If I will see her…</em> Hetzelfde "
              "geldt voor <em>If you <strong>work</strong> hard, you will pass</em> en <em>If the "
              "weather <strong>is</strong> nice tomorrow, we will cycle</em>: na <em>if</em> staat de "
              "tegenwoordige tijd, ook als het over morgen gaat."),
    ("p", "Een voorwaarde kan je ook inleiden met <strong>unless</strong> (tenzij) of "
          "<strong>as long as</strong> (zolang). <strong>However</strong> is geen voorwaarde maar een "
          "tegenstelling. En <strong>na unless zet je geen tweede ontkenning</strong>: <em>unless</em> "
          "is zelf al ontkennend. <em>Unless you hurry, you will miss the bus</em> betekent: als je je "
          "niet haast, mis je de bus."),
    ("p", "De <strong>voorwaardelijke bijzin kan vooraan of achteraan staan</strong>. Staat hij "
          "vooraan, dan komt er een komma: <em>If it rains, we stay in.</em> Staat hij achteraan, dan "
          "niet: <em>We stay in if it rains.</em>"),
])

ZINSSOORTEN = dict(kop="Vier soorten zinnen", blokken=[
    ("p", tabel(["Soort", "Voorbeeld", "Waaraan je het ziet"], [
        ["<strong>bevestigend</strong>", "<em>The shop is open.</em>", "gewone woordorde, punt"],
        ["<strong>ontkennend</strong>", "<em>I <strong>don't</strong> like coffee.</em>", "<em>not</em> of <em>n't</em>"],
        ["<strong>vragend</strong>", "<em><strong>Did</strong> she call you?</em>", "hulpwerkwoord vooraan, vraagteken"],
        ["<strong>uitroepend</strong>", "<em><strong>What a</strong> lovely day!</em>", "<em>what</em> of <em>how</em>, uitroepteken"],
        ["<strong>bevelend</strong>", "<em><strong>Close</strong> the door, please.</em>", "geen onderwerp, kale vorm van het werkwoord"],
    ])),
    ("p", "<strong>Een bevelende zin heeft in het Engels geen onderwerp</strong> en gebruikt de kale "
          "vorm: <em>Close the door</em>, niet <em>Closes</em>, <em>Closing</em> of <em>To close</em>."),
    ("kader", "<strong>Twee ontkenningen in één zin mag niet in het Engels.</strong> <em>I don't know "
              "nothing</em> is fout; het moet <em>I don't know <strong>anything</strong></em> zijn, of "
              "<em>I know nothing</em>. In het Nederlands hoor je die dubbele ontkenning soms wel, en "
              "net daar gaat het mis."),
])

zet("zinsbouw-zinsdelen-en-de-voorwaardelijke-bijzin",
    "Zinsbouw, zinsdelen en de voorwaardelijke bijzin",
    "De delen van een zin, de woordorde, het werkwoord dat bij het onderwerp past, de voegwoorden en "
    "de conditionals zero en first.",
    [
        sectie("zinsbouw-indirecte-rede-en-de-passieve-vorm", "De delen van een zin"),
        ZINSDELEN,
        sectie("zinsbouw-indirecte-rede-en-de-passieve-vorm", "De woordorde"),
        ZINSSOORTEN,
        sectie("zinsbouw-indirecte-rede-en-de-passieve-vorm", "Het werkwoord bij het onderwerp"),
        sectie("zinsbouw-indirecte-rede-en-de-passieve-vorm", "Voegwoorden"),
        sectie("zinsbouw-indirecte-rede-en-de-passieve-vorm", "De voorwaardelijke zinnen"),
        CONDITIONALS,
        dict(kop="Nevenschikking, onderschikking en congruentie", blokken=[
            ("p", "Twee hoofdzinnen naast elkaar is <strong>nevenschikking</strong>; een bijzin bij een "
                  "hoofdzin is <strong>onderschikking</strong>."),
            ("p", tabel(["Soort voegwoord", "Woorden", "Voorbeeld"], [
                ["<strong>nevenschikkend</strong>", "<strong>and</strong>, <strong>but</strong>, "
                 "<strong>so</strong>, or, <strong>yet</strong>",
                 "<em>It rained, <strong>so</strong> we stayed in.</em>"],
                ["<strong>onderschikkend</strong>", "<strong>because</strong>, "
                 "<strong>although</strong>, <strong>while</strong>, <strong>if</strong>, when, unless, as long as",
                 "<em>He is tired, <strong>but</strong> he will finish the work.</em>"],
            ])),
            ("p", "<strong>And is nevenschikkend, niet onderschikkend.</strong> En "
                  "<strong>yet kan wél een voegwoord zijn</strong>, met de betekenis van <em>but</em>: "
                  "<em>It was late, yet nobody left.</em> Het voegwoord dat een tegenstelling "
                  "aankondigt en <strong>nochtans of echter</strong> betekent, is "
                  "<strong>however</strong>; het voegwoord voor een reden is <strong>because</strong>, "
                  "en voor een voorwaarde <strong>if</strong>."),
            ("p", "<strong>Congruentie betekent dat het werkwoord bij het onderwerp past.</strong> "
                  "<em>My friends <strong>live</strong> nearby</em> (meervoud), <em>My friend "
                  "<strong>lives</strong> nearby</em> (enkelvoud)."),
            ("p", tabel(["Lastig onderwerp", "Welk werkwoord", "Waarom"], [
                ["<strong>everybody</strong>, everyone, nobody", "<strong>is</strong>", "enkelvoud, ook al gaat het over veel mensen"],
                ["the <strong>news</strong>", "<strong>is</strong>", "enkelvoud, ondanks de s"],
                ["the <strong>people</strong>", "<strong>are</strong>", "meervoud, ook zonder s"],
                ["the <strong>team</strong>, the family", "<strong>is</strong> of <strong>are</strong>",
                 "allebei juist: <em>is</em> als je de groep als geheel ziet, <em>are</em> als je de leden bedoelt"],
            ])),
            ("kader", "<strong>In het Engels staat de persoonsvorm in een bijzin op dezelfde plaats "
                      "als in een hoofdzin</strong>, dus vlak achter het onderwerp. Niet achteraan zoals "
                      "bij ons: <em>She said that she <strong>was</strong> tired</em>, en niet <em>She "
                      "said that she tired <s>was</s></em>. Dat is een van de fouten die een "
                      "Nederlandstalige het vaakst maakt."),
        ]),
        spreken("schrijf in het Engels vijf huisregels voor je eigen kamer met <em>If…, you will…</em>, "
                "en lees ze luidop voor."),
    ])

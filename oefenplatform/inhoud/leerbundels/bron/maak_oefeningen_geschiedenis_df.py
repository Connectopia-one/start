# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij geschiedenis 🚀 Boost dubbele finaliteit.

Net als bij de leerbundels nemen we de doorstroomversie over en zetten we er de
verschillen in; zie `maak_geschiedenis_df.py` voor waarom. De ingrepen hangen
aan een stuk tekst van de oefening die ze raken, en elke ingreep moet precies
één oefening raken. Verandert er iets aan de doorstroombundel, dan stopt dit
script in plaats van er stil overheen te gaan.

De sleutels dragen het voorvoegsel "oefenbundel-" en eindigen op
"-boost-dubbele-finaliteit".
"""
import copy
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import maak_oefeningen_geschiedenis_boost as doorstroom
import maak_geschiedenis_df as leerbundels

VAK = "Geschiedenis"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"

OUD = "-boost-doorstroom"
NIEUW = "-boost-dubbele-finaliteit"
W, WW, WL = "120px", "185px", "250px"

# (sleutel zonder voorvoegsel en categorie, haak, wat, oefeningen)
PATCHES = [
    # ── 3. Standen, domein en stad
    (
        "standen-domein-en-stad",
        "In welk maatschappelijk domein hoort het ontstaan van de geldeconomie",
        "vervang",
        [
            ("open", "In welk maatschappelijk domein horen de ambachten en gilden in de eerste plaats "
                     "thuis, en welk ander domein raken ze ook? Leg uit.",
             "In de eerste plaats economisch: ze gaan over werken, produceren en verkopen, en ze regelen "
                     "wie een beroep mag uitoefenen. Ze raken ook het culturele domein, want een gilde "
                     "onderhield een altaar in de kerk en vierde een eigen feestdag.", 6),
        ],
    ),
    (
        "standen-domein-en-stad",
        "Stad en platteland stonden in de middeleeuwen volledig los van elkaar.",
        "na",
        [
            ("kies", "Welk product hoort bij de langeafstandshandel en niet bij de lokale handel?",
             ["specerijen uit Azië", "brood van de bakker om de hoek",
              "groenten van de boer uit het dorp"], 0),
        ],
    ),
    # ── 5. De 'Nieuwe' Wereld en de driehoekshandel
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "Hoe heet het systeem waarbij een kolonist arbeid mocht opeisen",
        "vervang",
        [
            ("kort", "Onder welke twee vlaggen voer de eerste kolonisatiegolf?",
             "onder Spaanse en Portugese vlag", "260px"),
        ],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "Leg uit hoe de demografische inzinking, het encomiendasysteem",
        "vervang",
        [
            ("open", "Leg uit hoe de demografische inzinking van de precolumbiaanse bevolking, de "
                     "Afro-Amerikaanse slavenhandel en de driehoekshandel samenhangen. Schrijf het als "
                     "een ketting.",
             "De inheemse bevolking sterft grotendeels weg. Daardoor valt de arbeidskracht in de kolonies "
                     "weg, terwijl de mijnen en de velden blijven. Die arbeid wordt dan van elders "
                     "gehaald, uit Afrika, en dat is het been van de driehoekshandel tussen Afrika en "
                     "Amerika.", 6),
        ],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "Hoe heet de oversteek van Afrika naar Amerika?",
        "na",
        [
            ("open", "Twee bronnen geven een heel ander standpunt over de slavenhandel: een handelaar "
                     "schrijft over zijn winst, een tot slaaf gemaakte vertelt over de overtocht. Wat doe "
                     "je met dat verschil?",
             "Je gooit er geen van beide weg. Je gaat van elke bron na wie ze maakte en met welke "
                     "bedoeling, en je weegt de twee standpunten tegen elkaar af. Ze schrijven allebei de "
                     "waarheid van hun kant; wie ze naast elkaar legt, ziet net daarom meer.", 6),
        ],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "meer uitvoeren dan invoeren, om edelmetaal binnen te halen",
        "vervang",
        [
            ("rij", [("een papier waarmee je hier betaalt en daar het geld ophaalt", "een wisselbrief"),
                     ("een handelaar levert grondstof aan gezinnen die thuis werken", "huisnijverheid"),
                     ("arbeiders werken samen op één plaats, onder toezicht", "een manufactuur"),
                     ("het kapitaal is in verhandelbare delen verdeeld", "een handelscompagnie")],
             "Welk begrip?", WL),
        ],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "Noem drie kenmerken van het handelskapitalisme.",
        "vervang",
        [
            ("open", "Welke drie organisatievormen van ondernemingen horen bij de commerciële "
                     "revolutie? Zet er bij elk in één zin bij wat ze is.",
             "De handelscompagnie: het kapitaal is in verhandelbare delen verdeeld. De manufactuur: de "
                     "arbeiders werken samen op één plaats, onder toezicht, nog altijd met de hand. De "
                     "huisnijverheid: een handelaar levert grondstof aan gezinnen die thuis werken.", 6),
        ],
    ),
    (
        "de-nieuwe-wereld-en-de-driehoekshandel",
        "Het mercantilisme wil vrije handel met alle landen.",
        "vervang",
        [
            ("waar", "Bij huisnijverheid werken de arbeiders samen in één grote fabriek van de "
                     "ondernemer.", False),
            ("open", "Wat is het verband tussen de landbouwproductiviteit en de technische "
                     "vernieuwingen?",
             "Betere werktuigen en betere methodes laten dezelfde grond meer opbrengen. Een andere ploeg, "
                     "een ander vruchtwisselstelsel of een nieuw gewas: telkens haalt dezelfde akker meer "
                     "voedsel op, en telkens kunnen er meer monden mee gevoed worden.", 5),
        ],
    ),
    # ── 6. Humanisme, Reformatie, renaissance en barok
    ("humanisme-reformatie-renaissance-en-barok", "Een nieuwe wetenschappelijke methode", "schrap-sectie", []),
    # ── 9. Het Ottomaanse Rijk en samenlevingen vergelijken
    (
        "het-ottomaanse-rijk-en-samenlevingen-vergelijken",
        "Waarom werk je met vaste kenmerken en niet zomaar met wat opvalt?",
        "na",
        [
            ("open", "Langs welke drie wegen liep het contact tussen moslims en christenen?",
             "De zijderoutes, de ontmoeting tussen de Arabische cultuur en de cultuur van christelijk "
                     "Europa, en de kruistochten.", 4),
        ],
    ),
]

VERBODEN = leerbundels.VERBODEN


def tekst_van(oef) -> str:
    return " ".join(str(d) for d in oef)


def pas_toe(bundels: dict):
    for kort, haak, wat, nieuw in PATCHES:
        sleutel = "oefenbundel-" + kort + NIEUW
        if sleutel not in bundels:
            raise SystemExit(f"Onbekende bundel in PATCHES: {sleutel}")
        reeksen = bundels[sleutel]["reeksen"]
        if wat == "schrap-sectie":
            raak = [i for i, r in enumerate(reeksen) if r["kop"] == haak]
            if len(raak) != 1:
                raise SystemExit(f"{sleutel}: {len(raak)} reeksen heten {haak!r}, verwacht 1")
            reeksen.pop(raak[0])
            continue
        raak = [
            (i, j)
            for i, r in enumerate(reeksen)
            for j, o in enumerate(r["oefeningen"])
            if haak in tekst_van(o)
        ]
        if len(raak) != 1:
            raise SystemExit(f"{sleutel}: {len(raak)} oefeningen bevatten {haak!r}, verwacht 1")
        i, j = raak[0]
        if wat == "vervang":
            reeksen[i]["oefeningen"][j : j + 1] = nieuw
        elif wat == "na":
            reeksen[i]["oefeningen"][j + 1 : j + 1] = nieuw
        else:
            raise SystemExit(f"Onbekende ingreep: {wat}")


def bouw() -> dict:
    uit = {}
    for sleutel, b in doorstroom.OEFENBUNDELS.items():
        if not sleutel.endswith(OUD):
            raise SystemExit(f"Doorstroomsleutel zonder categorie: {sleutel}")
        nieuw = copy.deepcopy(b)
        nieuw["niveau"] = DF
        uit[sleutel[: -len(OUD)] + NIEUW] = nieuw
    pas_toe(uit)
    for sleutel, b in uit.items():
        alles = " ".join(
            [b["onder"]]
            + list(b.get("hoe", []))
            + [r["kop"] + " " + r.get("opdracht", "") for r in b["reeksen"]]
            + [tekst_van(o) for r in b["reeksen"] for o in r["oefeningen"]]
        ).lower()
        for woord in VERBODEN:
            if woord in alles:
                raise SystemExit(f"{sleutel} gebruikt nog {woord!r}, dat staat niet op de DF-fiche")
    return uit


OEFENBUNDELS = bouw()

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-het-historisch-referentiekader-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zoek bij elke gebeurtenis eerst een jaartal of een eeuw, en kijk dan tussen welke twee grenzen die valt. De grenzen die je moet kennen: 3000 v.C. (schrift), 476 (val van het West-Romeinse Rijk), 1453 of 1492, 1789 en 1945.",
            waarom=[
                "De piramide van Cheops dateert van rond 2560 v.C., dus na de uitvinding van het schrift: het oude nabije oosten. Rotstekeningen zijn van vóór het schrift, dus prehistorie. Augustus regeerde rond het begin van onze jaartelling, dus klassieke oudheid.",
                "1648 ligt tussen 1492 en 1789, dus vroegmoderne tijd. De eerste Belgische spoorlijn (1835) ligt tussen 1789 en 1945, dus moderne tijd. De val van de Muur (1989) ligt na 1945, dus hedendaagse tijd.",
            ],
        ),
        dict(
            aanpak="Chronologie is volgorde: wat kwam eerst? Periodisering is indelen en een naam geven: welke stukken onderscheid ik, en hoe noem ik ze?",
            waarom=[
                "Een tijdlijn ordenen is volgorde, dus chronologie.",
                "Een stuk tijd afbakenen en er een naam aan geven, is precies wat periodisering is.",
                "De vraag wat er eerst kwam, is zuivere volgorde.",
                "Namen geven aan stukken tijd, hier dynastieën, is periodisering. Zie ook oefening 16: elke periodisering is een keuze.",
            ],
        ),
        dict(
            aanpak="Rekenen met jaartallen heeft twee valkuilen: er is geen jaar nul, en jaartallen voor Christus lopen achterwaarts. Teken bij twijfel een pijl en zet de twee jaartallen erop.",
            waarom=[
                "Voor de eeuw tel je bij de eerste twee cijfers één op, behalve als het jaartal op 00 eindigt. 1302 wordt dus de 14de eeuw (die loopt van 1301 tot 1400), maar 1600 blijft de 16de eeuw, want de 16de loopt van 1501 tot 1600.",
                "Binnen de tijd voor Christus loopt alles achterstevoren: 400 v.C. is vroeger dan 200 v.C. Je trekt dus af in plaats van op te tellen. Gaat het over een jaartal voor én na Christus, dan tel je wel op, maar trek je er één af, want er is geen jaar nul.",
            ],
        ),
        dict(
            aanpak="Zes begrippen in drie paren. Continuïteit tegenover verandering: blijft het of niet? Gelijktijdigheid tegenover ongelijktijdigheid: gebeurt het tegelijk of niet? Evolutie tegenover revolutie: traag of plots?",
            waarom=[
                "Let op het verschil tussen evolutie en revolutie: allebei zijn het verandering, maar evolutie gaat traag en geleidelijk, revolutie plots en ingrijpend.",
                "Ongelijktijdigheid betekent dat hetzelfde verschijnsel op verschillende plaatsen op een ander moment opduikt. Dat is een belangrijk begrip, want het haalt het idee onderuit dat Europa overal eerst was.",
            ],
        ),
        dict(
            aanpak="De vier domeinen zijn politiek (macht en bestuur), economisch (werken, handel, geld), sociaal (groepen en hun verhouding) en cultureel (geloof, kunst, kennis, gewoontes). Bijna elke gebeurtenis raakt er twee.",
            waarom=[
                "Het is bijna nooit maar één domein, en daar krijg je ook punten voor: je uitleg telt zwaarder dan het etiket. Zeg dus altijd waaróm je dat domein kiest.",
            ],
        ),
        dict(
            aanpak="Schaalniveaus gaan van klein naar groot: lokaal (een stad of dorp), regionaal (een streek of graafschap), nationaal (een land), continentaal (een werelddeel) en mondiaal (de hele wereld).",
            waarom=[
                "Let op: het graafschap Vlaanderen is regionaal, niet nationaal. België bestond toen nog niet, en het schaalniveau kies je naar de grootte van het gebied, niet naar de naam.",
                "Ruraal betekent op het platteland. In de stad is urbaan. De twee worden vaak verwisseld.",
                "Dat is net het verschil met een gewone kaart: een historische kaart geeft de toestand van toen weer, dus met grenzen en namen die vandaag niet meer bestaan.",
            ],
        ),
        dict(
            aanpak="Een periodegrens is nooit een feit maar een keuze. Op een examen word je niet beoordeeld op welke je kiest, maar op de argumenten waarmee je ze verdedigt.",
            waarom=[
                "Beide jaartallen zijn verdedigbaar, en dat is net het punt. Geef twee argumenten die iets zeggen over een blijvende verandering, niet alleen over de gebeurtenis zelf.",
                "De drie beperkingen die je moet kennen: periodisering selecteert (wat je niet kiest, valt weg), ze suggereert een scherpe breuk die er in het echte leven niet was, en ze is westers bedacht en past niet overal even goed.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-van-rome-naar-de-franken-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een interne oorzaak zit binnen de samenleving zelf; een externe komt van buiten. Vraag je telkens af vanuit wiens standpunt je kijkt, want dezelfde gebeurtenis kan voor de een intern en voor de ander extern zijn.",
            waarom=[
                "Het leger is een onderdeel van het rijk zelf, dus intern. Dat Germanen in dat leger dienden, verzwakte de band tussen het leger en de staat.",
                "De Hunnen kwamen van buiten het rijk, en zelfs van buiten het gebied van de Germanen. Een duwtje van ver weg dus: zij dreven anderen voor zich uit.",
                "Let op de wissel van standpunt. Vanaf hier kijk je naar de migraties van de Germanen, niet meer naar Rome. Bevolkingsgroei is bij hen intern.",
                "En de rijkdom van Rome is voor de Germanen juist extern: een aantrekkingskracht van buiten. Historici noemen dat een pull-factor, tegenover de push-factor van oefening 3.",
            ],
        ),
        dict(
            aanpak="Zes jaartallen die samen het verhaal dragen. Leer ze als een reeks, want elke gebeurtenis volgt uit de vorige.",
            waarom=[
                "Het verhaal in één lijn: Rome valt (476), de Franken worden christelijk (doop van Clovis), de hofmeier neemt de kroon over (751), het rijk wordt een keizerrijk (800), het valt uiteen (843) en wordt van buitenaf belaagd (9de eeuw). Dat laatste leidt naar het leenstelsel.",
            ],
        ),
        dict(
            aanpak="Namen en begrippen leer je het best met de functie erbij: wat deed die persoon of dat ding precies? Dan onthoud je ze ook als de vraag anders gesteld wordt.",
            waarom=[
                "De missi dominici zijn letterlijk de gezanten van de heer: ze reisden per twee, een geestelijke en een leek, om de graven te controleren. Dat was nodig omdat een graaf ver van Aken deed wat hij wou.",
                "De spotnaam vadsige koningen komt van de Karolingers zelf, die de macht overnamen en hun voorgangers graag zwak voorstelden. Dat is meteen een les over bronnen: wie schreef dit, en waarom?",
            ],
        ),
        dict(
            aanpak="Let bij een waar-of-nietwaarvraag op het woordje dat de uitspraak te streng maakt (altijd, alleen) en op namen die in de verkeerde tijd staan.",
            waarom=[
                "Het Oost-Romeinse of Byzantijnse Rijk viel pas in 1453 met de val van Constantinopel. Dat is bijna duizend jaar na 476, en net daarom is 1453 een periodegrens.",
                "Het Frankische erfrecht verdeelde het rijk ónder de zonen. Dat is precies waarom het rijk telkens opnieuw uiteenviel, zie oefening 13.",
                "De Karolingische renaissance was een zaak van kloosters, scholen en het hof. Een boer merkte er niets van, en dat is een goed voorbeeld van hoe een omwenteling niet iedereen tegelijk raakt.",
                "De Mongolen kwamen pas in de 13de eeuw, en tot Hongarije en Polen. In de 9de eeuw waren het de Noormannen, de Saracenen en de Hongaren.",
                "Dat is precies de oorzaak van het leenstelsel: een verre koning kon niet beschermen, een nabije heer wel.",
            ],
        ),
        dict(
            aanpak="Bij een oorzaak-gevolgvraag zoek je niet wat er daarna gebeurde, maar wat er dóór gebeurde. Schrijf je antwoord als een zin die begint met daardoor.",
            waarom=[
                "Elke generatie opnieuw verdelen betekent elke generatie kleinere stukken. Het Verdrag van Verdun in 843 is daar het bekendste voorbeeld van.",
                "Dit is de kern van het leenstelsel: bescherming in ruil voor dienst en grond. De macht verschuift van de koning naar de lokale heer.",
                "Clovis koos niet het arianisme van de andere Germaanse koningen maar het katholieke geloof van de bevolking die hij ging besturen. Dat was een politieke zet, geen toeval.",
            ],
        ),
        dict(
            aanpak="Bij een bron stel je altijd dezelfde vier vragen: wie schreef dit, wanneer, voor wie, en met welk doel? Een oordeel in de tekst (beminde, achtte, goede naam) verraadt het standpunt van de schrijver.",
            waarom=[
                "Twee aanwijzingen samen: een monnik in de 9de eeuw, en het woord keizer met een paleis. Karel de Grote was keizer vanaf 800.",
                "Dit is de kern van bronnenkritiek. Een bron is zelden een leugen, maar bijna nooit neutraal. Zoek de woorden die een waardering uitdrukken, en vraag je af wie de schrijver was en van wie hij afhing.",
                "Een zalving raakt twee domeinen tegelijk, en op een examen moet je ze allebei uitleggen. Dat de paus de macht bevestigt, is politiek; dat het een godsdienstige plechtigheid is, is cultureel.",
            ],
        ),
        dict(
            aanpak="Bij een vergelijking is de bouw belangrijker dan de inhoud: noem eerst wat hetzelfde is, dan wat verschilt, en zorg dat je allebei over hetzelfde onderwerp hebt.",
            waarom=[
                "De val zit in het vergelijken van twee verschillende dingen. Hou vast aan één onderwerp, hier de koninklijke macht, en bekijk die bij allebei. Zeg dus niet dat de ene dynastie vroeger was dan de andere: dat is geen vergelijking.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-standen-domein-en-stad-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De drie standen hebben elk een taak, en die taak rechtvaardigde de hele indeling: bidden, strijden, werken. Leer bij elke stand wie erin zat en wat zijn taak was.",
            waarom=[
                "De derde stand was veruit de grootste, meer dan negentig procent, en droeg de twee andere. Dat is het punt van de indeling: ze lijkt een verdeling van taken, maar ze is ook een verdeling van voorrechten.",
                "Sociale mobiliteit betekent dat je van de ene groep naar de andere kan. In een standensamenleving kon dat bijna niet, want je plaats hing aan je geboorte. De geestelijkheid was de enige weg omhoog die soms openstond.",
            ],
        ),
        dict(
            aanpak="Het verschil tussen een horige en een slaaf is de kern van deze reeks. Een horige was niet vrij, maar hij was ook geen bezit: hij had rechten, een eigen huis en een eigen akker.",
            waarom=[
                "Een horige was aan de grond gebonden: hij mocht niet zomaar vertrekken en ook niet zomaar trouwen buiten het domein.",
                "Dit is precies het verschil met een slaaf. Een horige werd met het land mee overgedragen als het domein van eigenaar veranderde, maar hij kon niet apart verkocht worden zoals een voorwerp.",
                "Het vroonland is het deel van het domein dat de heer voor zichzelf hield. Herendiensten waren het werk dat de horigen daar gratis moesten doen, bovenop het werk op hun eigen akker.",
                "Dat heet autarkie: zelfvoorziening. Alleen zout, ijzer en wat luxe kwamen van buiten. Dat verandert pas als de handel weer op gang komt.",
                "Dat heette het banrecht: de heer had het alleenrecht op de molen, de oven en de wijnpers, en liet zich daarvoor betalen. Een voorbeeld van hoe macht en geld in elkaar grepen.",
            ],
        ),
        dict(
            aanpak="Drie uitvindingen die samen één gevolg hadden: meer voedsel van dezelfde grond. Leer bij elke vernieuwing waaróm ze meer opbracht.",
            waarom=[
                "De drie werken op drie manieren. Het drieslagstelsel laat de grond rusten en benut toch twee derde in plaats van de helft. De keerploeg keert de zware kleigrond van het noorden echt om. Het haam laat een paard trekken met zijn schouders in plaats van met zijn keel, waardoor het niet meer stikt en dus veel sterker trekt dan een os.",
                "Zet je antwoord als een ketting: overschot, markt, bevolkingsgroei, arbeidskrachten die vrijkomen, ambacht en handel, stad. Op een examen krijg je punten voor die ketting, niet voor het eindpunt alleen.",
            ],
        ),
        dict(
            aanpak="Rond de stad draaien een paar vaste begrippen: keure, poorter, ambacht, patriciër, belfort. Leer ze met hun betekenis, want ze komen in elke vraag over de middeleeuwse stad terug.",
            waarom=[
                "De drie factoren samen: meer voedsel, meer veiligheid, en een goede ligging. Noem ze alle drie, want de vraag vraagt er drie.",
                "Een paard met een kar deed enkele tientallen kilometers per dag en kon weinig dragen; een schip op een rivier droeg het veelvoud. Daarom liggen bijna alle oude handelssteden aan water.",
                "Een keure is het stadsrecht: de vorst legt vast welke vrijheden en rechten de stad krijgt, meestal in ruil voor geld. Vandaar de uitdrukking dat stadslucht vrij maakt.",
                "Een ambacht of gilde bepaalde ook de prijzen, de kwaliteit en wie het beroep mocht uitoefenen. Het was dus meer dan een vereniging: het was een monopolie.",
                "Let op de laatste stap: geld. De meesterproef was een echte drempel, maar het kapitaal voor een eigen werkplaats was er een grotere. Daardoor bleven de ambachten steeds meer in dezelfde families.",
            ],
        ),
        dict(
            aanpak="De stad was vrijer dan het platteland, maar niet gelijker. Let bij zo'n uitspraak op het woord alle: één tegenvoorbeeld volstaat om ze te weerleggen.",
            waarom=[
                "Patriciërs zijn de rijke koopliedenfamilies die het bestuur in handen hielden. Poorters zijn alle volwaardige stadsbewoners met burgerrecht, dus een veel ruimere groep.",
                "Het belfort is het teken van de stadsvrijheid: de klok regelde de werkdag en de oorkonden in de toren bewezen de rechten van de stad. Vandaar dat het belfort zo hoog moest zijn als de kerktoren, of hoger.",
                "Twee argumenten volstaan, maar maak ze concreet: alleen patriciërs bestuurden, en er waren arme loonwerkers zonder enig recht. De opstanden van de ambachten in de 14de eeuw bewijzen dat de ongelijkheid gevoeld werd.",
            ],
        ),
        dict(
            aanpak="De pest is het schoolvoorbeeld van hoe een ramp de machtsverhoudingen omkeert. Redeneer met vraag en aanbod: wat er schaars wordt, wordt duur.",
            waarom=[
                "De zwarte dood bereikte West-Europa in 1347 en doodde in enkele jaren naar schatting een derde tot de helft van de bevolking.",
                "Dit is een economische redenering die je op een examen moet kunnen maken: minder aanbod van arbeid bij gelijke vraag betekent een hogere prijs voor arbeid, dus hogere lonen. Het verklaart mee waarom de horigheid in West-Europa verdween.",
            ],
        ),
        dict(
            aanpak="Bij deze laatste vragen leg je verbanden tussen de domeinen en tussen stad en platteland. Denk nooit in gescheiden vakjes: dat is net wat deze vragen testen.",
            waarom=[
                "Een gilde is economisch én cultureel, en dat laatste vergeten de meesten. Een gilde had een patroonheilige, een eigen altaar en een eigen feestdag, en ze speelde mee in de processies.",
                "Ze hadden elkaar nodig: de stad at het graan van het platteland, en de boeren kochten in de stad hun gereedschap en verkochten er hun overschot. Zonder platteland geen stad.",
                "Langeafstandshandel gaat over waren die veel waard zijn in verhouding tot hun gewicht: specerijen, zijde, zilver. Brood en groenten zijn te zwaar en te bederfelijk om ver te vervoeren.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-geloof-kunst-en-macht-in-de-middeleeuwen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De Kerk was in de middeleeuwen geen gewone instelling maar het enige netwerk dat heel Europa bestreek. Leer haar bouw van boven naar onder, en onthoud wat elke laag deed.",
            waarom=[
                "Onder de paus staan de bisschoppen met elk hun bisdom, en daaronder de pastoors in de parochies. Alleen de pastoor zag de gewone mensen echt; de paus was voor hen een naam.",
                "Drie taken, en let op wat er níét bij hoort. Munten slaan was een recht van de vorst, geen kloostertaak. Het kopiëren van teksten is historisch het belangrijkste: zonder de kloosters was bijna geen enkele antieke tekst bewaard gebleven.",
                "Dit heet bekering van bovenaf, en het verklaart waarom de doop van één vorst in de boeken staat. Het zegt ook iets over hoe dun dat christendom in het begin was: de mensen volgden hun heer, niet hun overtuiging.",
            ],
        ),
        dict(
            aanpak="Romaans en gotisch verschillen in één ding: hoe het gewicht van het dak gedragen wordt. Alle andere kenmerken volgen daaruit. Leer dus eerst de techniek, dan de look.",
            waarom=[
                "Bij een rondboog duwt het gewicht naar buiten, dus moet de muur dik zijn en blijven de vensters klein. Vandaar de donkere, zware indruk.",
                "Bij een spitsboog gaat de kracht meer naar beneden dan naar buiten, dus kan de muur dunner. Vandaar de grote ramen.",
                "Luchtbogen staan buiten het gebouw en vangen de zijwaartse druk op. Zij maken de hoge, open gotische kerken mogelijk.",
                None,
                "Noem de drie technieken samen: spitsboog, kruisribgewelf en luchtboog. Samen dragen die het gewicht naar punten en naar buiten, zodat de muur niet meer de drager is. Dat is wat je op een examen moet kunnen uitleggen: niet de versiering maar de constructie.",
            ],
        ),
        dict(
            aanpak="Middeleeuwse kunst lees je niet als een foto maar als een boodschap. Grootte, plaats en kleur betekenen iets, en wie dat weet, kan een afbeelding als bron gebruiken.",
            waarom=[
                "Dit noemt men de biblia pauperum, de bijbel van de armen. Het verklaart waarom zoveel middeleeuwse kerken zo rijk versierd zijn: het was onderwijs.",
                "De Vlaamse primitieven is een naam die pas in de 19de eeuw bedacht werd, en primitief betekent hier vroeg, niet onbeholpen. Hun olieverf was juist technisch heel verfijnd.",
                "Dat heet een betekenisperspectief of rangschikking naar belangrijkheid. Pas in de renaissance komt het meetkundige perspectief, waar de grootte de afstand aangeeft. Zie ook het hoofdstuk over de renaissance.",
            ],
        ),
        dict(
            aanpak="Frankrijk en Engeland gaan in de late middeleeuwen twee verschillende kanten op: in Frankrijk wordt de koning sterker, in Engeland wordt hij ingeperkt. Dat verschil loopt eeuwen door.",
            waarom=[
                "Het Engelse parlement groeit uit de raad van edelen en krijgt vooral macht over de belastingen. Wie het geld bepaalt, bepaalt veel.",
                "De Franse koning kocht, erfde en veroverde stukje bij beetje de gebieden van zijn leenmannen terug. Dat is het begin van de latere absolute monarchie.",
                "De Magna Carta van 1215 deed het omgekeerde: ze legde de koning beperkingen op en gaf de edelen rechten. Ze geldt als een eerste stap naar een grondwet.",
            ],
        ),
        dict(
            aanpak="De Guldensporenslag is een goed voorbeeld van twee dingen tegelijk: een gebeurtenis die in meer dan één domein thuishoort, en een gebeurtenis die later een heel andere betekenis kreeg.",
            waarom=[
                "11 juli 1302, bij Kortrijk. Let op het jaartal: 1302 ligt in de 14de eeuw, zie de rekenoefening in het eerste hoofdstuk.",
                "Noem allebei de domeinen met een eigen uitleg. Politiek is de strijd om de macht over Vlaanderen; sociaal is de strijd tussen de ambachten en de patriciërs binnen de steden zelf.",
                "Beeldvorming is een kernbegrip: de betekenis die een latere tijd aan een gebeurtenis geeft. De 19de eeuw zocht een Vlaams verhaal en vond het hier. Dat zegt meer over de 19de eeuw dan over 1302.",
            ],
        ),
        dict(
            aanpak="Let bij deze vragen op twee dingen: tempo (iets dat eeuwen duurde wordt vaak voorgesteld als plots) en richting (wie gaf wat aan wie?).",
            waarom=[
                "Mohammed leefde van ongeveer 570 tot 632; de islam ontstaat dus in de 7de eeuw, rond 600 tot 630.",
                "De uitbreiding duurde meer dan een eeuw, en op sommige plaatsen eeuwen. Dat een geloof zich snel verspreidde, betekent niet dat het overal tegelijk aankwam: dat is ongelijktijdigheid.",
                "Dit is de belangrijkste les van deze reeks. Aristoteles en andere Griekse teksten waren in West-Europa verloren en kwamen terug via Arabische vertalingen en via Spanje. De kennisstroom liep dus van oost naar west, niet omgekeerd.",
                "Noem er twee die er wel vandaan komen en zeg uitdrukkelijk wat er niet vandaan komt. De boekdrukkunst met losse letters is van Gutenberg, rond 1450; in Korea en China bestond blokdruk al veel vroeger, maar dat is een ander procedé.",
                "De kruisvaardersstaten hielden het geen twee eeuwen vol. De blijvende gevolgen lagen elders: handel, kennis, en een wederzijds wantrouwen dat lang nawerkte.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-de-nieuwe-wereld-en-de-driehoekshandel-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De drie motieven van de ontdekkingsreizen worden samengevat als goud, God en glorie: economisch, godsdienstig en politiek. Bij bijna elke reis spelen ze alle drie mee.",
            waarom=[
                "Let op de eerste en de vierde: allebei economisch, maar ze zeggen hetzelfde van twee kanten. Een eigen weg zoeken en de tussenhandelaars uitschakelen is één en dezelfde zaak.",
                "Elke tussenschakel wil winst, en de specerijen gingen via Arabische en Venetiaanse handelaars. Een eigen zeeweg betekende dus niet alleen minder risico maar vooral veel meer winst.",
            ],
        ),
        dict(
            aanpak="Zonder techniek geen ontdekkingsreizen. Je moet bij elk instrument kunnen zeggen welk probleem het oploste: richting houden, of weten waar je bent.",
            waarom=[
                "Het kompas geeft de richting, het astrolabium en de jakobsstaf geven de breedtegraad met de stand van de zon of de poolster. De lengtegraad was het grote onopgeloste probleem: dat lukte pas in de 18de eeuw met een nauwkeurig uurwerk. En de scheepsmotor bestond nog niet: men voer op de wind, met het karveel en later het galjoen.",
            ],
        ),
        dict(
            aanpak="Vier namen, vier verschillende prestaties. Let erop dat niet iedereen in de lijst een ontdekkingsreiziger is: Cortés was een veroveraar.",
            waarom=[
                "Columbus bereikte de Caraïben in 1492 en dacht tot zijn dood dat hij in Azië was. Da Gama bereikte als eerste Indië over zee in 1498, rond Afrika. De vloot van Magellaan voer als eerste rond de wereld, maar hij zelf stierf onderweg.",
                "Dit onderscheid moet je kunnen maken: Portugal wilde de handel beheersen met steunpunten langs de kust, Spanje wilde het land zelf en veroverde het binnenland. Dat verklaart meteen waarom Latijns-Amerika vandaag Spaans spreekt en de Portugese invloed zich tot Brazilië en een rij kusthavens beperkt.",
            ],
        ),
        dict(
            aanpak="De gevolgen voor de inheemse bevolking zijn de kern van dit hoofdstuk. Reken niet met oorlog alleen: de grootste sterfte kwam van ziekten.",
            waarom=[
                "Pokken, mazelen en griep waren in Europa al eeuwen aanwezig, maar in Amerika volkomen nieuw. Daardoor stierf naar schatting negentig procent van de bevolking in een eeuw tijd. De oorlogen kwamen daar bovenop.",
                "Het Incarijk in de Andes, veroverd door Pizarro. In Mexico was het het Azteekse rijk, veroverd door Cortés.",
                "De eerste golf was Spaans en Portugees, en zij verdeelden de wereld onder elkaar in het Verdrag van Tordesillas (1494). De Nederlanders, Engelsen en Fransen komen pas in de tweede golf.",
                "Schrijf dit als een ketting, want daar krijg je de punten voor: bevolking sterft weg, arbeid valt weg, arbeid wordt elders gehaald, dus slavenhandel. Dat is een oorzakelijk verband en niet alleen een volgorde.",
            ],
        ),
        dict(
            aanpak="De driehoekshandel heeft drie benen, en je moet van elk kunnen zeggen wat er vervoerd werd. Let erop dat één been over mensen gaat, en benoem dat ook zo.",
            waarom=[
                "Elk been leverde winst op, en dat is waarom het systeem bleef bestaan. Europa verkocht wapens en textiel, Afrika leverde arbeid onder dwang, Amerika leverde suiker, katoen en tabak.",
                "De middenpassage is het middelste been van de driehoek. Naar schatting één op de zes mensen overleefde die overtocht niet.",
                "Dit is een vraag over bronnenkritiek, en het antwoord is nooit dat je er één weggooit. Je vraagt bij elke bron wie ze maakte, wanneer en waarom, en je legt de twee naast elkaar. Twee standpunten geven samen meer dan één.",
                "Het antwoord dat punten haalt, noemt de domeinen uitdrukkelijk: economisch én sociaal, want achter de handelsstroom staan mensen die tot koopwaar gemaakt werden.",
            ],
        ),
        dict(
            aanpak="De commerciële revolutie gaat over hóé er gehandeld en geproduceerd wordt. Leer de drie organisatievormen uit elkaar te houden: wie werkt waar, en wie bezit wat?",
            waarom=[
                "Het verschil tussen huisnijverheid en manufactuur is de plaats: thuis tegenover samen op één plek. Het verschil tussen manufactuur en fabriek is de machine: in een manufactuur werkt men nog met de hand.",
                "Noem ze alle drie met één zin uitleg. De handelscompagnie is de belangrijkste nieuwigheid: door het kapitaal in delen te verdelen, kon je een dure reis financieren en het risico spreiden. Dat is het begin van het aandeel.",
                "Het antwoord zit in het woord systematisch: winst wordt opnieuw geïnvesteerd in plaats van opgedaan. En de macht verschuift van wie grond bezit naar wie kapitaal bezit. Dat is een breuk, want de spelregels zelf veranderen.",
                "Bij huisnijverheid werken de gezinnen juist thuis, elk apart. Dat is net het verschil met de manufactuur.",
                "Het verband is wederzijds: betere techniek geeft meer voedsel, en meer voedsel maakt mensen vrij voor ander werk, wat weer techniek oplevert. Zie ook de ketting in het hoofdstuk over de steden.",
            ],
        ),
        dict(
            aanpak="De sporen van de kolonisatie zijn vandaag nog zichtbaar, en dat is net wat deze vragen willen laten zien. Denk aan taal, godsdienst, grenzen en landbouw.",
            waarom=[
                "Brazilië spreekt Portugees omdat het bij de verdeling van 1494 aan Portugal toeviel; de rest van Zuid- en Midden-Amerika spreekt Spaans. Een grens van vijfhonderd jaar oud die je vandaag nog hoort.",
                "Dit is een vraag over standpunt. Nieuw is het altijd voor iemand, en hier voor de Europeanen. Daarom spreken historici liever van precolumbiaanse volkeren dan van de Nieuwe Wereld.",
                "Monocultuur maakt een gebied rijk zolang de prijs hoog is, en kwetsbaar zodra ze valt of de oogst mislukt. Suiker, katoen en koffie zijn de schoolvoorbeelden, en de gevolgen ervan zijn in sommige landen nog altijd voelbaar.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-humanisme-reformatie-renaissance-en-barok-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Het humanisme is een manier van denken, geen stijl. Het draait om drie dingen: de mens, de oudheid en het zelf onderzoeken van de bronnen.",
            waarom=[
                "Noem ze alle drie. Het derde is het minst bekende en het belangrijkste: humanisten gingen terug naar de oorspronkelijke tekst, in het Grieks of het Hebreeuws, in plaats van op een vertaling te vertrouwen. Dat is precies de houding die later de Reformatie mogelijk maakt.",
                "De humanisten waren bijna allemaal gelovig en wilden de Kerk verbeteren, niet afschaffen. Erasmus bleef katholiek en keerde zich uitdrukkelijk tegen de breuk van Luther.",
                "De Lof der Zotheid (1511) is zijn bekendste werk. Erasmus laat daarin de Zotheid zelf aan het woord, en zo kan hij alles bespotten zonder het zelf te beweren: een slimme vorm.",
                "Geld, contacten en resten van de oudheid, alle drie tegelijk aanwezig. De handelsfamilies, zoals de Medici in Florence, waren de opdrachtgevers; zonder hun geld geen kunst en geen geleerden.",
                "Noem de boekdrukkunst én de reden. Niet het drukken op zich telde, maar dat een idee niet meer kon verdwijnen als één bisschop het verbood: er waren te veel exemplaren.",
            ],
        ),
        dict(
            aanpak="De Reformatie begint bij een concreet misbruik en eindigt bij een breuk over de vraag wie er tussen de mens en God staat. Leer de twee Latijnse kernzinnen, want daarop komt alles neer.",
            waarom=[
                "Een aflaat was oorspronkelijk een kwijtschelding van kerkelijke straf. Het misbruik was dat ze verkocht werd, onder meer om de Sint-Pietersbasiliek te betalen. Dat is wat Luther over de streep trok.",
                "31 oktober 1517 aan de slotkerk van Wittenberg. Of hij ze echt aan de deur sloeg, is onzeker; dat hij ze opstuurde naar zijn bisschop staat wel vast.",
                "Vijfennegentig stellingen, in het Latijn, bedoeld als uitnodiging tot een academisch debat. Dat ze binnen enkele weken in heel Duitsland circuleerden, is te danken aan de boekdrukkunst.",
                "Dit is de kern van het hele hoofdstuk. Als geloof alleen volstaat en de Bijbel de enige bron is, dan zijn aflaten, heiligenverering en de bemiddeling van priesters overbodig. Daarom was dit geen meningsverschil maar een breuk.",
            ],
        ),
        dict(
            aanpak="Drie protestantse strekkingen, elk met een eigen oorsprong. Luthers leer kwam uit een theologisch conflict, het calvinisme ging verder in dezelfde lijn, en het anglicanisme ontstond uit een politieke ruzie.",
            waarom=[
                "De predestinatie is het kenmerk van Calvijn: God heeft vooraf bepaald wie gered wordt. Het anglicanisme ontstond toen Hendrik VIII geen toestemming kreeg voor zijn scheiding en zichzelf tot hoofd van de Kerk van Engeland maakte: een politieke breuk, geen leerstellige.",
                "Dit is een belangrijk inzicht: achter een godsdienstige keuze zat vaak een wereldse winst. Wie protestant werd, kon kloosters en kerkelijke gronden in beslag nemen en hoefde niets meer naar Rome af te dragen.",
            ],
        ),
        dict(
            aanpak="De Contrareformatie is het antwoord van de katholieke Kerk: eigen misbruiken aanpakken, de leer opnieuw vastleggen en zich verdedigen. Let op wat er níét bij hoort.",
            waarom=[
                "Het Concilie van Trente (1545-1563) legde zowel de leer vast als de hervormingen die nodig waren: geen aflatenverkoop meer, en bisschoppen moesten in hun bisdom wonen.",
                "Vóór Trente kon bijna iedereen priester worden, zonder opleiding. De seminaries waren het antwoord op precies die klacht van de hervormers.",
                "De Index van verboden boeken en de inquisitie horen bij de verdedigende kant van de Contrareformatie. De Index werd pas in 1966 afgeschaft.",
                "De mis afschaffen is juist een protestantse maatregel. De katholieke Kerk hield de mis en de sacramenten uitdrukkelijk vast; dat was het geschilpunt.",
                "Noem er drie, en spreid ze over Europa: Frankrijk (de godsdienstoorlogen met Bartholomeusnacht en het Edict van Nantes), Duitsland (de Dertigjarige Oorlog, 1618-1648) en de Nederlanden (de Opstand, met de scheiding tussen noord en zuid als gevolg).",
            ],
        ),
        dict(
            aanpak="Renaissance en barok zijn twee stijlen met een verschillend doel. De renaissance zoekt evenwicht en rust, de barok wil je meeslepen. Dat verschil zie je in elk kenmerk terug.",
            waarom=[
                "Rust, symmetrie en heldere verhoudingen: de renaissance kijkt naar de Griekse en Romeinse bouwkunst.",
                "De barok hoort bij de Contrareformatie: een kerk moest de gelovige overdonderen en meeslepen. Vandaar het drama, de beweging en de sterke contrasten.",
                "Het perspectief wordt in de renaissance ontdekt, in Florence, en is meteen hét kenmerk van die kunst.",
                None,
                "Leg het concreet uit: alle lijnen die in werkelijkheid evenwijdig lopen, komen op het schilderij samen in één verdwijnpunt, en dingen worden kleiner naarmate ze verder staan. Zo wordt een plat vlak een ruimte.",
                "Dit is de beste samenvatting van het hele hoofdstuk: de middeleeuwen schikken naar betekenis, de renaissance naar het oog. Geef er een concreet voorbeeld bij, zoals de figuur die het grootst is omdat hij het belangrijkst is.",
            ],
        ),
        dict(
            aanpak="Vier namen om uit elkaar te houden, en het verschil zit in de tijd: drie Italianen uit de 15de en 16de eeuw, en één Vlaming uit de 17de.",
            waarom=[
                "Michelangelo, Leonardo en Rafaël horen bij de Italiaanse renaissance; Rubens leefde een eeuw later en is dé barokschilder van onze streken. Kijk bij twijfel naar de eeuw.",
                "Twee kenmerken die je aan het beeld zelf ziet, dus geen jaartallen. Het bestudeerde naakt en de rustige, klassieke verhoudingen zijn de goede antwoorden; het ontbreken van een aureool hoort er ook bij, want de mens zelf is het onderwerp.",
                "Allebei zochten ze de natuur, maar langs een andere weg: de Vlamingen met olieverf en oog voor het detail, de Italianen met klassieke verhoudingen en perspectief. Zeg dus niet dat de ene beter was dan de andere.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-vorsten-opstand-en-de-verlichting-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag beslist bij elk kenmerk: is er iets of iemand die de koning kan tegenhouden? Is er niets, dan is het absolutisme. Is er een parlement of een grondwet, dan is het een parlementaire monarchie.",
            waarom=[
                "Geen verantwoording betekent geen tegenmacht. Dat is de kern van het absolutisme.",
                "Het belastingrecht is de sleutel: wie het geld mag toestaan, kan de koning tegenhouden. Daarom draait de hele Engelse strijd van de 17de eeuw daarrond.",
                "De Franse Staten-Generaal kwamen tussen 1614 en 1789 niet meer samen. Dat is 175 jaar zonder standenvergadering, en precies daarom is de bijeenroeping van 1789 zo explosief.",
                None,
                "Droit divin betekent goddelijk recht. De koning ontvangt zijn macht rechtstreeks van God, dus kan geen mens ze betwisten. Dat is de redenering waarop het absolutisme steunt.",
            ],
        ),
        dict(
            aanpak="Versailles is geen paleis maar een machtsinstrument. Vraag je bij elk onderdeel af wat het voor de koning opleverde.",
            waarom=[
                "Noem er drie, en vergeet de belangrijkste niet: de adel aan het hof binden. Wie in Versailles om de gunst van de koning streed, was niet in zijn eigen gewest aan het samenzweren.",
                "Het antwoord zit in het geld. De oorlogen en het hof kostten meer dan het rijk opbracht, en adel en geestelijkheid betaalden bijna geen belasting. Die rekening komt in 1789 op tafel.",
            ],
        ),
        dict(
            aanpak="De Glorious Revolution heet glorieus omdat ze zonder veel bloedvergieten verliep. Let op dat ze drie oorzaken had, waarvan er twee godsdienstig en politiek door elkaar lopen.",
            waarom=[
                "Noem ze alle drie, en zie hoe ze samenhangen: een koning die zonder parlement wil regeren én katholiek is, in een protestants land dat zijn parlement wil houden.",
                "De Bill of Rights van 1689: geen belastingen en geen leger zonder parlement, vrije verkiezingen en vrije meningsuiting in het parlement. Dat is het begin van de parlementaire monarchie.",
                "Dit is de zin die het hele hoofdstuk samenvat: dezelfde eeuw, twee tegengestelde uitkomsten. Frankrijk krijgt zijn afrekening pas in 1789.",
            ],
        ),
        dict(
            aanpak="De Opstand duurde tachtig jaar en had drie soorten oorzaken tegelijk: politiek (de privileges), godsdienstig (de vervolging) en economisch (de belastingen). Noem er altijd drie.",
            waarom=[
                "De volgorde van de jaartallen is belangrijker dan de jaartallen zelf: eerst de Beeldenstorm (1566), dan het begin van de oorlog (1568), dan de afzwering van Filips II (1581), en pas in 1648 de erkenning.",
                "Alle drie noemen, want ze horen in drie verschillende domeinen thuis. Dat is precies wat een examenvraag wil zien.",
                "De kern van de uitleg: wat voor de vorst doelmatig bestuur is, is voor een stad het afnemen van haar rechten. Centralisatie is dus niet neutraal, en daarom botst ze.",
                "De sluiting van de Schelde is het zwaarste gevolg: Antwerpen verliest zijn zeehandel aan Amsterdam, en met de kooplui en geleerden vertrekt ook het kapitaal en de kennis. Daar begint de Gouden Eeuw van het noorden.",
            ],
        ),
        dict(
            aanpak="Twee bronnen over dezelfde man, uit de twee kampen. Zoek niet welke de waarheid is, maar wie wat waarom opschreef.",
            waarom=[
                "Let op de woorden zelf: orde en ware godsdienst tegenover bloedhertog en recht zonder recht. Dat zijn waarderingen, en ze verraden het kamp van de schrijver.",
                "Dit is de kern van bronnenkritiek, en het antwoord is bijna altijd hetzelfde: twee bronnen die elkaar tegenspreken, vragen om een vergelijking. Allebei kunnen ze eerlijk zijn en toch iets anders belangrijk vinden.",
            ],
        ),
        dict(
            aanpak="Vijf denkers, vijf ideeën. Leer bij elke naam één begrip, dan kan je elke vraag erover beantwoorden.",
            waarom=[
                "Koppel elke naam aan één woord: Locke aan natuurlijke rechten, Voltaire aan verdraagzaamheid, Montesquieu aan de scheiding der machten, Rousseau aan de volkssoevereiniteit en Kant aan durf zelf te denken.",
                "Noem de drie machten én het doel. De scheiding dient opdat de ene de andere kan tegenhouden: dat heet checks and balances. Ze betekent dus niet dat de regering de rechtbanken leidt, maar juist het omgekeerde.",
                "De meeste verlichte denkers wilden de monarchie hervormen, niet afschaffen. Sommigen hoopten zelfs op een verlicht despoot, een vorst die hun ideeën van bovenaf zou invoeren, zoals Jozef II.",
            ],
        ),
        dict(
            aanpak="De begrippen van deze reeks komen rechtstreeks uit de Verlichting en staan vandaag in de grondwet. Leer ze met een voorbeeld uit het heden, dan onthoud je ze beter.",
            waarom=[
                "Let op het verschil tussen rechtsgelijkheid en rechtszekerheid. Gelijkheid gaat over dezelfde wet voor iedereen; zekerheid gaat over vooraf weten waar je aan toe bent, dus geen straffen met terugwerkende kracht.",
                "Empirisme en rationalisme zijn twee wegen naar kennis: waarnemen tegenover redeneren. De Verlichting gebruikt ze allebei, en het vooruitgangsoptimisme is het geloof dat die kennis de samenleving beter maakt.",
                "Noem er drie en zeg erbij waar ze staan. De scheiding der machten, de gelijkheid voor de wet en de vrijheden van godsdienst, mening en vereniging staan alle drie in de Belgische grondwet van 1831, die toen een van de meest vooruitstrevende van Europa was.",
                "Dit is de kern: het gezag komt niet meer van God maar van het volk. En wie zegt dat de macht van het volk komt, zegt ook dat ze teruggenomen kan worden. Daar komen de revoluties uit voort.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-amerika-frankrijk-en-de-industriele-omwenteling-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De Amerikaanse Revolutie draait om één politieke vraag: wie mag beslissen? Let erop dat de kolonisten niet tegen belasting op zich waren.",
            waarom=[
                "Dit onderscheid is het halve antwoord: niet de belasting zelf werd betwist, maar het recht van een parlement waarin ze niet zetelden om ze op te leggen. Dat maakt er een politieke eis van, geen financiële.",
                "4 juli 1776, in Philadelphia. Het is nog altijd de nationale feestdag van de Verenigde Staten.",
                "Noem er drie, en zeg uitdrukkelijk wat er níét is: geen erfelijke koning. Republiek, federale staat en strikte scheiding der machten zijn de drie kenmerken.",
                "Een goede vraag over spanning in een bron. De tekst zegt dat alle mensen gelijk geboren worden, terwijl de slavernij bleef bestaan en vrouwen, inheemse volkeren en wie geen bezit had, geen stem kregen. Benoem die spanning: dat is wat een examen wil zien.",
            ],
        ),
        dict(
            aanpak="Zoek bij elke uitspraak of ze iets zegt over de toestand vóór 1789. Een oorzaak werkt al langer; een aanleiding is de vonk. En let op uitspraken die gewoon niet kloppen.",
            waarom=[
                "De oorlogen, waaronder de steun aan de Amerikaanse opstandelingen, hadden de kas leeggemaakt. Geld is de directe aanleiding voor het bijeenroepen van de Staten-Generaal.",
                "Dit is de politieke én sociale oorzaak: de derde stand was 98 procent van de bevolking, betaalde bijna alle belastingen en werd bij stemming per stand telkens overstemd.",
                "De misoogsten van 1788 maakten brood onbetaalbaar. Honger verklaart waarom gewone mensen de straat op gingen; ideeën alleen doen dat zelden.",
                "Frankrijk was in 1789 niet bezet. De oorlogen met de buurlanden komen pas ná de revolutie, vanaf 1792.",
                "De aanleiding is de bijeenroeping van de Staten-Generaal, en het breekpunt is de stemwijze: per hoofd of per stand. Met stemming per hoofd had de derde stand de meerderheid, en net daarom weigerde de koning.",
                "Dit is dezelfde les als bij de Guldensporenslag: de betekenis van een gebeurtenis kan veel zwaarder wegen dan de gebeurtenis zelf. De Bastille stond voor willekeur, en dat is wat men bestormde.",
            ],
        ),
        dict(
            aanpak="De revolutie verloopt in drie fasen, en die zijn niet rechtlijnig. Hou vast aan de volgorde en aan wat er in elke fase verandert aan wie er regeert.",
            waarom=[
                "De volgorde: eerst de grondwettelijke monarchie (1789-1792), dan de republiek met de Terreur (1792-1794), dan het Directoire en Napoleon. Het absolutisme van voor 1789 keerde nooit terug, ook niet onder Napoleon.",
                "Dit is een belangrijke vraag omdat ze een revolutie niet als louter goed voorstelt. Duizenden terechtstellingen zonder behoorlijk proces zijn precies de schending van de rechtszekerheid die de revolutie zelf op haar vaandel schreef.",
                "Het antwoord in één zin: standen maken plaats voor burgers die gelijk zijn voor de wet. Zet er de nuance bij die punten oplevert: de ongelijkheid verdwijnt niet, maar ze staat niet langer in de wet.",
                "Olympe de Gouges schreef in 1791 de Verklaring van de rechten van de vrouw en de burgeres. Dat ze in 1793 onthoofd werd, hoort bij het antwoord: het toont hoe ver de gelijkheid reikte.",
            ],
        ),
        dict(
            aanpak="Twee revoluties, dezelfde ideeën. Let erop dat je bij een vergelijking echt over hetzelfde spreekt: hier over de politieke oorzaken, niet over het verloop.",
            waarom=[
                "Alle drie noemen: verlichte ideeën, geen vertegenwoordiging, en rechten vastgelegd in een geschreven tekst. Dat laatste is nieuw in de geschiedenis.",
                "Lafayette is de naam die je moet kennen: hij vocht in Amerika mee en werkte daarna mee aan de Franse Verklaring van de Rechten van de Mens. Het bewijs dát het kon, woog even zwaar als het idee.",
                "Drie Franse sporen die er vandaag nog zijn: de burgerlijke stand, de Code civil als basis van ons burgerlijk recht, en het metriek stelsel. Alle drie dateren ze van rond 1800 en gebruiken we nog elke dag.",
                "Het Frans werd de bestuurstaal, niet het Nederlands. Dat is een van de oorzaken van de latere taalstrijd in België.",
            ],
        ),
        dict(
            aanpak="De industriële revolutie verandert twee dingen: de techniek en de organisatie van het werk. Hou die twee uit elkaar, want een examenvraag vraagt er meestal maar één.",
            waarom=[
                "Groot-Brittannië, vanaf ongeveer 1750 tot 1780. Dat het daar begon, verklaar je met de aanbod- en vraagfactoren van de laatste reeks.",
                "Noem er drie en zeg welke er níét bij hoort. De verbrandingsmotor komt pas rond 1880, dus die hoort bij de tweede industriële revolutie, samen met elektriciteit en staal.",
                "Het verschil is de aandrijving. Samen werken op één plaats deed men al in de manufactuur; nieuw is dat machines, eerst op water en daarna op stoom, het zware werk doen.",
                "De drie organisatorische vernieuwingen: arbeidsverdeling, werken in de fabriek, en de vaste werkuren van de machine. Zeg er ook bij wat verdwijnt: de vakman die een stuk van begin tot eind maakt.",
                "Dit is dezelfde redenering als bij de commerciële revolutie. Revolutie slaat hier op de diepte van de verandering, niet op de snelheid.",
            ],
        ),
        dict(
            aanpak="Aanbodfactoren zijn wat je nodig hebt om te kúnnen produceren: grondstoffen, kapitaal, arbeid, techniek. Vraagfactoren zijn wie het koopt: de eigen bevolking en de koloniën.",
            waarom=[
                "Grondstoffen zijn aanbod: zonder steenkool en ijzererts geen stoommachine en geen staal.",
                "Koloniën zijn afzetmarkt én grondstofleverancier, maar hier gaat het om het kopen, dus vraag.",
                "Kapitaal is wat je nodig hebt om een fabriek te bouwen, dus aanbod. Het kwam grotendeels uit de handel en de koloniën van de eeuwen ervoor.",
                "Meer mensen die kopen, is vraag. De bevolkingsgroei werkt dus langs twee kanten: meer arbeid (aanbod) en meer kopers (vraag).",
                "De enclosures zijn de omheiningen van de gemene gronden. Ze maakten de landbouw productiever, maar ze duwden kleine boeren van het land.",
                "Dit is de brug tussen landbouw en industrie, en ze is dubbel: minder handen nodig op het land, meer handen beschikbaar voor de fabriek, en tegelijk meer voedsel om een stadsbevolking te voeden.",
                "Noem er drie, en zeg er de nuance bij: de ongelijkheid verdween niet, ze kreeg een nieuwe vorm. Van standen naar klassen.",
                "Een vraag over bronnen. Cijfers, kaarten en onderzoeksverslagen zijn bronnen uit die tijd zelf, en het laatste zijn de rijkste: de verslagen van de Engelse parlementscommissies over kinderarbeid staan vol getuigenissen. Een hedendaagse roman is geen bron over die tijd maar over onze kijk erop.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-het-ottomaanse-rijk-en-samenlevingen-vergelijken-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Het Ottomaanse Rijk hoort in de leerstof omdat het tegelijk met het Europa van de vroegmoderne tijd bestond. Vergelijk dus steeds met wat je over Frankrijk weet.",
            waarom=[
                "1453, de val van Constantinopel, het einde van het Byzantijnse Rijk. Dat jaartal ken je al als mogelijke grens tussen de middeleeuwen en de vroegmoderne tijd.",
                "Noem de vier gebieden én het besluit: Europa, Azië en Afrika tegelijk. Het rijk lag rond de oostelijke Middellandse Zee, en daarom beheerste het de routes tussen Europa en Azië.",
                "Het verschil is wezenlijk: de sultan is zelf ook godsdienstig hoofd, terwijl een Franse koning de Kerk gebruikte maar de paus boven zich wist. Geestelijke en wereldlijke macht vallen dus in het ene geval samen en in het andere niet.",
                "En de gelijkenis is even belangrijk: alle macht bij één persoon, zonder verkiezing, zonder grondwet, zonder parlement. Op een examen word je gevraagd allebei te zien.",
            ],
        ),
        dict(
            aanpak="Over minderheden en handel bestaat een hardnekkig beeld dat niet klopt. Toets elke uitspraak aan de feiten: er werd volop gehandeld, en minderheden hadden een eigen plaats.",
            waarom=[
                "Het millet-stelsel gaf elke godsdienstige gemeenschap, joden en verschillende christelijke kerken, een eigen bestuur over eigen zaken zoals huwelijk en erfenis, met een eigen hoofd dat verantwoording aflegde aan de sultan.",
                "Zet er de nuance bij die het antwoord sterk maakt: gelijkheid was het niet, want niet-moslims betaalden een hoofdelijke belasting en hadden niet dezelfde rechten. Maar er was een plaats, en dat verschil met het Spanje van 1492 is scherp.",
                "Er werd volop gehandeld: Venetië, Genua en later Frankrijk hadden er handelshuizen, en de capitulaties regelden dat. Zie oefening 12.",
                "Dit verband moet je kunnen leggen: de Ottomaanse greep op de landroutes is een van de redenen waarom Portugal en Spanje een zeeweg zochten. Zo hangt dit hoofdstuk vast aan dat over de ontdekkingsreizen.",
            ],
        ),
        dict(
            aanpak="Het contact met Europa liep langs drie wegen tegelijk: oorlog, handel en diplomatie. Wie alleen de oorlogen kent, houdt een scheef beeld over.",
            waarom=[
                "Suleyman I regeerde van 1520 tot 1566 en heet in het westen de Prachtlievende, bij de Ottomanen de Wetgever. Twee namen, twee standpunten: ook dat is beeldvorming.",
                "Wenen, in 1529, en opnieuw in 1683. Beide keren hield de stad stand, en die twee belegeringen markeren het verste punt van de Ottomaanse uitbreiding in Europa.",
                "Het antwoord in één zin: politiek belang woog zwaarder dan geloof. Frans I zocht een bondgenoot tegen Karel V, die hem langs alle kanten omsingelde.",
                "De capitulaties waren voorrechten voor Europese kooplui, onder meer eigen rechtspraak en lagere tarieven. Later, toen het rijk verzwakte, werden ze een middel om het economisch in de tang te houden.",
                "Noem alle drie de wegen en trek het besluit: oorlog, handel en diplomatie. Daarom mag je het rijk niet alleen als vijand beschrijven.",
                "De 16de eeuw is het hoogtepunt, niet het verval. Dat begint pas later, en het beeld van de zieke man van Europa stamt uit de 19de eeuw: ook dat is beeldvorming, en van een heel andere tijd.",
            ],
        ),
        dict(
            aanpak="Bij bouwkunst moet je kenmerken kunnen noemen die je aan het gebouw zelf ziet, met één voorbeeld erbij.",
            waarom=[
                "Noem drie kenmerken én een gebouw. Dat er geen mensenfiguren afgebeeld worden, is het opvallendste verschil met de christelijke kunst van dezelfde eeuw: sierschrift en meetkundige patronen nemen hun plaats in.",
            ],
        ),
        dict(
            aanpak="Vergelijken doe je met vaste punten, en die punten horen bij de vier domeinen. Zoek bij elk vergelijkingspunt in welk domein het hoort.",
            waarom=[
                "Bestuur is politiek, migratie en slavernij zijn sociaal, kunst en levensbeschouwing zijn cultureel, en landbouw en handel zijn economisch. Dat zijn precies de vier domeinen uit het eerste hoofdstuk.",
                "Imperialisme gaat over macht, dus politiek. De gelaagde samenleving staat hier bij het culturele omdat de ordening met godsdienst en wereldbeeld gerechtvaardigd werd; ze heeft natuurlijk ook een sociale kant, en op een examen mag je dat uitdrukkelijk zeggen, als je het maar uitlegt.",
                "De afstand tot de evenaar is aardrijkskunde, geen vergelijkingspunt voor samenlevingen. Klimaat kan wel een verklarende factor zijn, maar het is geen kenmerk van de samenleving zelf.",
                "Het verschil in één zin: imperialisme is het streven naar macht over andere gebieden, kolonialisme is daar één vorm van, met vestiging en bestuur ter plaatse. Alle kolonialisme is imperialisme, niet omgekeerd.",
            ],
        ),
        dict(
            aanpak="Een vergelijkende tabel is de beste voorbereiding op een examenvraag. Vul hem rij per rij in, en zorg dat je bij elk punt over allebei iets schrijft.",
            waarom=[
                "Let op de rij over godsdienst: dat is het grootste verschil tussen de twee. En de laatste rij is bij allebei leeg: geen parlement, geen grondwet. Dat is óók een vergelijkingsresultaat.",
                "Noem er drie, en let erop dat ze allemaal over de bouw van de samenleving gaan: een kleine top leeft van een grote basis, godsdienst rechtvaardigt de ordening, en je geboorte bepaalt je leven. Dat is wat een gelaagde samenleving betekent.",
            ],
        ),
        dict(
            aanpak="De laatste reeks gaat over de methode zelf. Die vragen komen op een examen terug in een andere vorm, dus leer ze echt in plaats van ze over te slaan.",
            waarom=[
                "Het antwoord zit in de tweede zin: wat opvalt is vaak enkel wat vreemd is aan ons. Met vaste punten vergelijk je hetzelfde met hetzelfde en zie je ook wat je anders over het hoofd zou zien.",
                "Drie wegen: de zijderoutes, de ontmoeting met de Arabische cultuur in Spanje en Sicilië, en de kruistochten. Alleen de laatste is een conflict; de andere twee waren uitwisseling.",
                "Vergelijken is nooit alleen verschillen zoeken. Wie alleen verschillen noemt, komt uit bij een lijst tegenstellingen in plaats van bij een vergelijking.",
                "Periodisering ken je uit het eerste hoofdstuk: in stukken verdelen én namen en grenzen geven. Dat laatste is altijd een keuze.",
                "Een anachronisme is iets uit de verkeerde tijd: een Romein met een horloge, maar ook de middeleeuwen beoordelen met de maatstaven van vandaag. Dat tweede is de valkuil waar een examen op let.",
                "Weerleg met een concreet voorbeeld. Vergelijken over periodes heen (de Egyptische en de middeleeuwse samenleving) én binnen eenzelfde periode (het Ottomaanse Rijk en Frankrijk) hebben allebei zin, en het tweede toont net dat dezelfde eeuw heel verschillende samenlevingen voortbrengt.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-redeneren-met-historische-bronnen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een onderzoekbare vraag is afgebakend in tijd, in ruimte en in domein, en er moeten bronnen voor bestaan. Toets elke vraag op die vier dingen.",
            waarom=[
                "Zie wat er telkens ontbreekt. Mensen vroeger is niet afgebakend in tijd, ruimte of domein. Waarom gingen mensen op ontdekkingstocht mist wie, wanneer en van waar. En de laatste vraagt om een moreel oordeel, geen onderzoek: daarvoor bestaat geen bron die het kan beslissen.",
                "Vijf criteria, en noem ze alle vijf: tijd, ruimte, domein, het bestaan van bronnen, en de bruikbaarheid van die bronnen. De laatste twee worden het vaakst vergeten.",
                "Dit is de kern van de methode. Zonder vraag weet je niet waarnaar je in een bron moet kijken, en dan lees je er vooral in wat je al dacht.",
            ],
        ),
        dict(
            aanpak="Een primaire bron komt uit de tijd zelf, een secundaire is er later over gemaakt. Vraag je telkens af wanneer de bron ontstond, niet waarover ze gaat.",
            waarom=[
                None,
                "De documentaire gaat over 1914 maar is in 2020 gemaakt, dus secundair. Let op: de beelden ín die documentaire kunnen wel primair zijn.",
                "Ook voorwerpen zijn bronnen: een munt vertelt over de vorst, de economie en de techniek van zijn tijd.",
                None,
                "Dit is de belangrijkste uitspraak van de reeks. Een ooggetuige kan zich vergissen, liegen of maar één hoek zien. Een historicus die honderd bronnen vergeleek, kan betrouwbaarder zijn dan iemand die erbij was.",
            ],
        ),
        dict(
            aanpak="Vier vormen: geschreven, mondeling, materieel en audiovisueel. Elke vorm heeft zijn eigen sterkte, en samen dekken ze gaten die de andere laten vallen.",
            waarom=[
                None,
                "Dit is een belangrijk inzicht: geschreven bronnen komen bijna altijd van de kleine groep die kon schrijven, dus van de top. Scherven, botten en huizen vertellen over iedereen.",
                "Een ooggetuige zag het zelf; een tijdgenoot leefde toen maar was er niet bij en hoorde het van anderen. Dat verschil telt bij het wegen van een bron.",
            ],
        ),
        dict(
            aanpak="Een bron ontleden gaat in vaste stappen: situeren in tijd, ruimte en domein, dan kijken wat er staat, en dan hoe het gezegd wordt. Die laatste stap levert het meest op.",
            waarom=[
                "Situeren betekent alle drie: wanneer, waar, en in welk domein. Hier zijn het er zelfs twee: economisch en politiek, en die hangen in 1585 samen.",
                "Wijs ze letterlijk aan in de tekst, dat is wat gevraagd wordt. Alle eerlijke lieden is een veralgemening; ofwel lui ofwel een verrader is een stereotype, want het drukt een hele groep in twee vakjes.",
                "Standplaatsgebondenheid is het kernbegrip van dit hoofdstuk: iedereen vertelt vanuit zijn eigen plaats, tijd en belangen. Een gekleurde bron is daarom niet waardeloos; ze is een bron over die kleur. Je leert er de blik van een Antwerpse koopman in 1585 uit kennen.",
            ],
        ),
        dict(
            aanpak="Bruikbaarheid gaat over jouw vraag: helpt deze bron mij vooruit? Betrouwbaarheid gaat over de bron zelf: kan ik erop af? Dat zijn twee verschillende vragen.",
            waarom=[
                None,
                "Afhankelijkheid van de maker raakt de betrouwbaarheid: wie betaald wordt door wie hij beschrijft, schrijft zelden ongunstig.",
                "Afstand in tijd raakt ook de betrouwbaarheid: een herinnering die dertig jaar later opgeschreven wordt, is door al die jaren gekleurd.",
                None,
                "Dit is de kern: bruikbaarheid hangt altijd van je vraag af. Een perfect betrouwbare kloosterrekening helpt je niets als je vraag over zeeslagen gaat.",
                "De lengte zegt niets. Een korte oorkonde kan betrouwbaarder zijn dan een lang pamflet. Wat telt is wie, wanneer en waarom.",
            ],
        ),
        dict(
            aanpak="Drie denkfouten die op elkaar lijken. Een veralgemening trekt uit enkele gevallen een besluit over allen. Een stereotype is een vast, te eenvoudig beeld van een groep. Een vooroordeel is een oordeel vóór je gekeken hebt.",
            waarom=[
                "Zie het onderscheid: de eerste trekt iets door naar iedereen, de tweede plakt een vast beeld op een volk, en de derde weigert zelfs te kijken. Dat laatste is het gevaarlijkst voor een historicus.",
                "Iedereen, altijd en overal zijn de drie alarmwoorden. Kom je er een tegen, in een bron of in je eigen zin, kijk dan twee keer.",
            ],
        ),
        dict(
            aanpak="Een beargumenteerd antwoord is meer dan een samenvatting: het is een standpunt dat met bronnen gestaafd wordt. Leer de vier redeneerwijzen, want ze komen in elke examenvraag terug.",
            waarom=[
                "Twee redenen, en noem ze allebei: elke bron is standplaatsgebonden, en elke bron is onvolledig. Wat twee onafhankelijke bronnen allebei zeggen, staat sterker.",
                "Een samenvatting herhaalt wat de bronnen zeggen. Een beargumenteerd antwoord neemt een standpunt in over je vraag en staaft dat met wat je in de bronnen vond. Dat verschil is waar op een examen punten op staan.",
                "Vier redeneerwijzen: bewijs gebruiken, actualiseren, historisch contextualiseren en onbedoelde gevolgen zien. Contextualiseren is daarvan de moeilijkste: iets begrijpen vanuit zijn eigen tijd in plaats van vanuit de onze.",
                "Een goed voorbeeld noemt de bedoeling én het gevolg, en laat zien dat ze niet samenvallen. Columbus zocht Azië en veroorzaakte de kolonisatie van Amerika: hij hield tot zijn dood vol dat hij in Azië was.",
                "Het antwoord is ja, en de reden is belangrijk: niet omdat alles maar een mening is, maar omdat begrippen als Europa verschillend ingevuld kunnen worden. Wat telt, is of je antwoord door de bronnen gedragen wordt. Dat is het verschil met alles mag.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-beeldvorming-en-het-verleden-vandaag-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Beeldvorming is het beeld dat iemand van het verleden maakt. Hou één onderscheid vast: wat gebeurd is, ligt vast; het beeld ervan is gemaakt en kan veranderen.",
            waarom=[
                "Noem de vier keuzes: selecteren, afleiden, interpreteren en samenhang zoeken. Elk van die stappen is een keuze, en dat is waarom twee historici tot een ander beeld kunnen komen.",
                "Dit is het onderscheid dat alles draagt. Het verleden zelf ligt vast, maar wij kennen het alleen via bronnen, en die zijn onvolledig. Dat is geen reden om te zeggen dat alles maar een mening is.",
                "Twee redenen: nieuwe bronnen, en nieuwe vragen aan oude bronnen. Dat tweede is vaak belangrijker. Toen men vragen begon te stellen over vrouwen of over slavernij, bleken bestaande bronnen plots veel te vertellen.",
                "Let op de tweede helft van het antwoord, want daar zit de grens. Verschillende beelden zijn normaal; een beeld dat de bronnen tegenspreekt, is fout. Niet alles is dus even waar.",
            ],
        ),
        dict(
            aanpak="Standplaatsgebondenheid heeft twee lagen: de persoonlijke context van de maker, en de maatschappelijke context waarin hij werkt. Vraag je telkens af of het over die ene persoon gaat of over de tijd en de samenleving errond.",
            waarom=[
                None,
                None,
                "Wie het onderzoek betaalt, hoort bij de maatschappelijke context: het gaat niet over de persoon van de maker maar over de omstandigheden waarin hij werkt.",
                "Ook een schoolboek van vandaag is standplaatsgebonden. Dat is geen verwijt: het is de reden waarom je ook bij een hedendaagse tekst mag vragen wie hem schreef en wanneer.",
                "Leg het verschil concreet uit: dezelfde gebeurtenis, twee tegengestelde betekenissen, omdat de makers aan een andere kant stonden. Het bloedbad zelf wordt in beide soorten bronnen vermeld; het oordeel erover niet.",
                "Het gevaar is dat je de blik van die ene kant overneemt zonder het te merken. Daarom legt een historicus bronnen van beide kanten naast elkaar.",
            ],
        ),
        dict(
            aanpak="Bij een beeld stel je altijd dezelfde vier vragen. De derde en de vierde worden het vaakst vergeten, en ze leveren het meeste op.",
            waarom=[
                "Vier vragen: wie en wanneer, op welke bronnen, wat wordt er níét verteld, en wie gaf de opdracht. Die laatste twee gaan over wat buiten beeld blijft, en dat is vaak even veelzeggend als wat erin staat.",
                "Pas hier de methode van de vorige bundel toe: steunt de uitspraak op meer dan enkele gevallen? Hier klopt ze gewoon niet, want geleerden wisten al in de oudheid dat de aarde rond was. Dat ze toch blijft terugkomen, is zelf een voorbeeld van beeldvorming.",
                "Een standbeeld, een schilderij, een film of een game doen even hard aan beeldvorming als een tekst, en vaak sterker, want een beeld blijft hangen.",
            ],
        ),
        dict(
            aanpak="Eén gebeurtenis, drie tijden, drie betekenissen. Dat is de beste oefening op beeldvorming die er bestaat, want je ziet het beeld onder je ogen veranderen terwijl de feiten dezelfde blijven.",
            waarom=[
                "Vul de drie rijen echt anders in. Voor de tijdgenoten ging het om macht en om de strijd tussen ambachten en patriciërs. De 19de eeuw maakte er een Vlaams verhaal van, in een tijd die een eigen identiteit zocht. En de feestdag van 11 juli is een keuze uit de 20ste eeuw.",
                "In één zin: een herdenking zegt vooral iets over wie herdenkt. Wát we herdenken en hóé, kiest het heden.",
                "Geef twee concrete voorbeelden, geen algemene zin. Een feestdag, een standbeeld, een lied op school: dat zijn de dragers van een gedeelde herinnering.",
            ],
        ),
        dict(
            aanpak="Identiteit heeft lagen, en die sluiten elkaar niet uit. En begrijpen is niet hetzelfde als goedkeuren: dat onderscheid moet je kunnen uitleggen.",
            waarom=[
                "Noem de lagen én de slotzin: een mens heeft niet één identiteit. Vlaams, Belgisch, westers, je sociaaleconomische positie en je levensbeschouwing bestaan tegelijk.",
                "Dit is de belangrijkste nuance van het hele vak. Het verleden met de maatstaf van vandaag beoordelen heet anachronisme, en het verhindert je te begrijpen waarom iets toen vanzelfsprekend leek. Maar begrijpen is niet goedkeuren, en dat moet je er uitdrukkelijk bij zeggen.",
            ],
        ),
        dict(
            aanpak="Een kunstwerk analyseer je in vier stappen, en de volgorde is de helft van het werk: eerst situeren, dan beschrijven, dan duiden, dan verwoorden.",
            waarom=[
                "De volgorde telt: eerst situeren (wie, wanneer, waar), dan beschrijven wat je ziet, dan pas uitleggen wat het betekent en wat de bedoeling was, en ten slotte je analyse verwoorden. Wie met stap 3 begint, ziet alleen wat hij verwachtte.",
                "De lijst is ruim met opzet: niet alleen schilderijen en beelden, maar ook bouwwerken, films, games, graffiti en liederen. Ook een game doet aan beeldvorming over het verleden.",
                "Noem er vier uit de lijst, en zet erbij dat er meestal meerdere tegelijk spelen. Een barokke kerk informeert, decoreert, bevestigt het geloof en toont de macht van de opdrachtgever, alle vier tegelijk.",
                "De verkoopprijs van vandaag zegt niets over het werk in zijn eigen tijd. Stap 1 gaat over de maker, de tijd en de plaats van ontstaan.",
            ],
        ),
        dict(
            aanpak="De laatste reeks brengt vorm en bedoeling samen. Vraag je telkens af wat de maker met de kijker wilde doen, en hoe de vorm daarbij helpt.",
            waarom=[
                "Leg het verband tussen vorm en doel: beweging, licht en grote gebaren zijn er om de kijker mee te slepen. De Contrareformatie wilde het geloof laten voelen, niet uitleggen, en de barok is daar de vorm van.",
                "De context verklaart de keuze. Een Mariabeeld uit 1650 in Antwerpen is een antwoord op de Beeldenstorm van bijna een eeuw eerder: juist dát onderwerp, juist daar, juist dan.",
                "Er is geen juist antwoord, maar de laatste zin van de bundel is de kern van het hele vak: niet alles is even waar, en niet niets is kenbaar. Een beeld van het verleden is gemaakt, en je mag altijd vragen door wie en waarom.",
            ],
        ),
    ]
)

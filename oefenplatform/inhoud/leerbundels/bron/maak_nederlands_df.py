# -*- coding: utf-8 -*-
"""De leerbundels voor Nederlands op 🚀 Boost dubbele finaliteit.

Gebaseerd op de vakfiche Nederlands 2de graad dubbele finaliteit, geldig vanaf
1 januari 2027. Eén fiche voor bedrijf en organisatie en voor maatschappij en
welzijn.

Negen bundels komen uit de doorstroomversie: die leerstof staat woord voor
woord ook op de DF-fiche. Drie zijn hier nieuw geschreven, want de
doorstroomversie past niet:

  * **Argumenteren.** Doorstroom draait om drogredenen. De DF-fiche kent die
    niet en vraagt feit en mening, stelling, standpunt, argument en conclusie.
  * **Literatuur.** Doorstroom heeft verteller, verteltijd, rijmschema en
    literaire stromingen. De DF-fiche vraagt enkel fictie, non-fictie,
    personages, verhaallijn, tijd en ruimte, en je eigen beleving.
  * **Communiceren.** De DF-fiche zet leerstof bij het spreken die doorstroom
    zo niet heeft: non-verbale communicatie, beleefdheidsconventies en de
    criteria waaraan je tekst of je spreekopdracht moet voldoen.

Drie bundels van doorstroom vallen weg: argumenteren met de drogredenen,
verhalen ontleden, en poëzie, drama en literaire stromingen.

De ingrepen in de overgenomen bundels staan in PATCHES, één regel per ingreep,
met de tekst waarop ze aanhaakt. Elke ingreep moet precies één blok raken;
raakt ze er geen of meerdere, dan stopt het script.
"""
import copy
import sys, pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel
import maak_nederlands_boost as doorstroom

VAK = "Nederlands"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"
tabel = bundel.tabel

OUD = "-boost-doorstroom"
NIEUW = "-boost-dubbele-finaliteit"

# Deze drie thema's bestaan bij dubbele finaliteit niet.
WEG = [
    "argumenteren-stelling-argumentsoort-en-drogreden",
    "verhalen-ontleden-verteller-tijd-en-ruimte",
    "poezie-drama-en-literaire-stromingen",
]

# Het vaste slotkader staat in elke overgenomen bundel en noemt de gewichten
# van doorstroom. Bij dubbele finaliteit wegen spreken (8 %) en gesprekken
# (16 %) samen 24 %, en het examen Nederlands is er één, geen twee.
GEWICHTEN_OUD = (
    "Maar op het examen Nederlands 1 "
    "wegen <strong>spreken</strong> (10 %) en <strong>gesprekken</strong> (30 %) samen "
    "<strong>40 %</strong>, en dat leer je niet achter een scherm."
)
GEWICHTEN_NIEUW = (
    "Maar op het examen Nederlands "
    "wegen <strong>spreken</strong> (8 %) en <strong>gesprekken</strong> (16 %) samen "
    "<strong>24 %</strong>, en dat leer je niet achter een scherm."
)

TEKSTFIXES = [
    (GEWICHTEN_OUD, GEWICHTEN_NIEUW, 9),
]

PATCHES = [
    # ── De woordsoorten: de DF-fiche somt de soorten voornaamwoorden niet op.
    #    Ze noemt enkel "voornaamwoord, zelfstandig en bijvoeglijk gebruikt".
    #    De acht zijn nog altijd de acht, maar niet omdát de fiche ze noemt.
    (
        "de-woordsoorten-op-een-rij",
        "De vakfiche noemt er acht: <strong>persoonlijk</strong>",
        "vervang",
        [
            ("p", "Er zijn er acht: <strong>persoonlijk</strong>, <strong>bezittelijk</strong>, "
                  "<strong>aanwijzend</strong>, <strong>vragend</strong>, <strong>betrekkelijk</strong>, "
                  "<strong>onbepaald</strong>, <strong>wederkerend</strong> en <strong>wederkerig</strong>. "
                  "'Bijwoordelijk' staat er niet bij."),
        ],
    ),
    # ── Spelling: de DF-fiche noemt zeven interpunctietekens, niet negen.
    (
        "spelling-leestekens-en-klanken",
        "De vakfiche noemt deze <strong>interpunctietekens</strong>",
        "vervang",
        [
            ("p", "De vakfiche noemt zeven <strong>interpunctietekens</strong>: de <strong>punt</strong>, de "
                  "<strong>komma</strong>, het <strong>vraagteken</strong>, het <strong>uitroepteken</strong>, "
                  "de <strong>dubbele punt</strong>, de <strong>spatie</strong> en het "
                  "<strong>aanhalingsteken</strong>. Het <strong>beletselteken</strong> en het "
                  "<strong>gedachtestreepje</strong> staan er niet bij, maar je komt ze wel tegen in teksten. "
                  "Een accentteken staat er evenmin bij: dat is een uitspraakteken."),
        ],
    ),
    # ── Betekenis, beeldspraak en gevoelswaarde: de DF-fiche noemt drie vormen
    #    van humor, en parodie en taalhumor horen er niet bij.
    (
        "betekenis-beeldspraak-en-gevoelswaarde",
        "De vakfiche noemt drie vormen: <strong>ironie</strong>",
        "vervang",
        [
            ("p", "Er zijn drie vormen van humor die je moet kennen: <strong>ironie</strong>, "
                  "<strong>overdrijving</strong> en <strong>woordspeling</strong>."),
        ],
    ),
    (
        "betekenis-beeldspraak-en-gevoelswaarde",
        "Een <strong>woordspeling</strong> speelt met de dubbele betekenis",
        "vervang",
        [
            ("p", "Een <strong>woordspeling</strong> speelt met de dubbele betekenis van een woord. Ze leunt "
                  "vaak op homoniemen, en werkt daarom <strong>zelden in een andere taal</strong>: ze hangt "
                  "vast aan de klank en de betekenissen van precies dat woord. <em>'Ik ga naar de kapper, "
                  "want mijn haar zit in de knoop'</em> werkt enkel omdat 'knoop' twee dingen kan betekenen."),
        ],
    ),
    (
        "betekenis-beeldspraak-en-gevoelswaarde",
        "Let op: een <strong>personificatie</strong> is beeldspraak, geen humor",
        "vervang",
        [
            ("p", "Let op: een <strong>personificatie</strong> en een <strong>metafoor</strong> zijn "
                  "beeldspraak, geen humor. Ze staan in een ander lijstje dan ironie, overdrijving en "
                  "woordspeling, en dat onderscheid wordt op het examen gevraagd."),
        ],
    ),
]


def gesprek(opdracht):
    """Het vaste slotkader over oefenen in het echte leven, met de DF-gewichten."""
    return dict(kop="Oefen dit ook buiten het scherm", blokken=[
        ("p", "Op dit platform oefen je wat je moet <em>kennen</em>. " + GEWICHTEN_NIEUW +
              " Je leert het door het te doen, met echte mensen, die terugpraten, je onderbreken en niet "
              "altijd begrijpen wat je bedoelt."),
        ("kader", "<strong>Deze week:</strong> " + opdracht + " Doe het één keer, en vraag daarna "
                  "aan de andere of je boodschap aankwam. Dat laatste is de helft van de oefening."),
    ])


def tekst_van(blok) -> str:
    return " ".join(str(d) for d in blok[1:])


def fix_teksten(ding, oud: str, nieuw: str):
    """Vervangt oud door nieuw, hoe diep het ook zit, en telt hoe vaak."""
    if isinstance(ding, str):
        return ding.replace(oud, nieuw), ding.count(oud)
    if isinstance(ding, dict):
        aantal = 0
        for k, v in ding.items():
            ding[k], n = fix_teksten(v, oud, nieuw)
            aantal += n
        return ding, aantal
    if isinstance(ding, (list, tuple)):
        stuks, aantal = [], 0
        for v in ding:
            v, n = fix_teksten(v, oud, nieuw)
            stuks.append(v)
            aantal += n
        return type(ding)(stuks), aantal
    return ding, 0


def pas_toe(bundels: dict):
    for kort, haak, wat, nieuw in PATCHES:
        sleutel = kort + NIEUW
        if sleutel not in bundels:
            raise SystemExit(f"Onbekende bundel in PATCHES: {sleutel}")
        secties = bundels[sleutel]["secties"]
        raak = [
            (i, j)
            for i, s in enumerate(secties)
            for j, b in enumerate(s["blokken"])
            if haak in tekst_van(b)
        ]
        if len(raak) != 1:
            raise SystemExit(f"{sleutel}: {len(raak)} blokken bevatten {haak!r}, verwacht 1")
        i, j = raak[0]
        if wat == "vervang":
            secties[i]["blokken"][j : j + 1] = nieuw
        elif wat == "na":
            secties[i]["blokken"][j + 1 : j + 1] = nieuw
        else:
            raise SystemExit(f"Onbekende ingreep: {wat}")


def overgenomen() -> dict:
    uit = {}
    weg = set()
    for sleutel, b in doorstroom.BUNDELS.items():
        if not sleutel.endswith(OUD):
            raise SystemExit(f"Doorstroomsleutel zonder categorie: {sleutel}")
        kort = sleutel[: -len(OUD)]
        if kort in WEG:
            weg.add(kort)
            continue
        nieuw = copy.deepcopy(b)
        nieuw["niveau"] = DF
        uit[kort + NIEUW] = nieuw
    if weg != set(WEG):
        raise SystemExit(f"Deze bundels staan niet (meer) bij doorstroom: {set(WEG) - weg}")
    pas_toe(uit)
    for oud, nieuw, hoevaak in TEKSTFIXES:
        uit, aantal = fix_teksten(uit, oud, nieuw)
        if aantal != hoevaak:
            raise SystemExit(f"{oud[:40]!r} staat {aantal} keer in de bundels, verwacht {hoevaak}")
    return uit


BUNDELS = overgenomen()

# ───────────────────────── Feit en mening, stelling, argument en conclusie
BUNDELS["feit-en-mening-stelling-argument-en-conclusie" + NIEUW] = dict(
    vak=VAK, niveau=DF, titel="Feit en mening, stelling, argument en conclusie",
    onder="Hoe je een betoog uit elkaar haalt, en hoe je er zelf een opbouwt dat standhoudt.",
    secties=[
        dict(kop="Feit of mening", blokken=[
            ("p", "Een <strong>feit</strong> is een uitspraak die je kan <strong>nagaan</strong>: opzoeken, "
                  "meten of tellen. <em>'Een dagpas kost 7,50 euro.'</em> Een <strong>mening</strong> is wat "
                  "iemand ervan vindt. <em>'De bus is veel te duur voor jongeren.'</em>"),
            ("p", "Het verschil zit niet in waar de zin staat of hoe zeker hij klinkt. Een mening in een krant "
                  "blijft een mening; een feit op een forum blijft een feit. De vraag is telkens dezelfde: "
                  "<strong>kan ik dit controleren?</strong>"),
            ("p", "Een mening is niet minderwaardig. Een goede opiniërende tekst ondersteunt zijn mening juist "
                  "met feiten. Wat je wél moet zien, is <em>welke</em> van de twee je voor je hebt, zodat je "
                  "niet meegaat in een oordeel dat als feit gebracht wordt."),
            ("kader", "Vraag bij elke zin: kan ik dit opzoeken of meten? Ja is een feit, nee is een mening. "
                      "Woorden als <em>te duur</em>, <em>schandalig</em> en <em>prachtig</em> verraden een oordeel."),
        ]),
        dict(kop="De vier woorden van een betoog", blokken=[
            ("p", tabel(["Begrip", "Wat is het?", "Voorbeeld"], [
                ["stelling", "de uitspraak waarover het gaat", "De schooldag moet later beginnen."],
                ["standpunt", "of jij voor of tegen bent", "Ik ben daarvoor."],
                ["argument", "de reden voor je standpunt", "Tieners slapen 's ochtends te kort."],
                ["conclusie", "wat er uit de argumenten volgt", "Daarom moet de school om negen uur starten."],
            ])),
            ("p", "<strong>Stelling</strong> en <strong>standpunt</strong> worden vaak door elkaar gehaald. De "
                  "stelling is het punt waarover gediscussieerd wordt, en die is voor iedereen dezelfde. Het "
                  "standpunt is de kant die jij kiest, en die kan van persoon tot persoon verschillen."),
            ("p", "Een <strong>argument</strong> beantwoordt de vraag <em>waarom vind je dat?</em> Zonder "
                  "argument is een standpunt enkel een uitroep. Herkennen doe je ze vaak aan een signaalwoord: "
                  "<strong>want</strong>, <strong>omdat</strong>, <strong>daarom</strong>, <strong>dus</strong>."),
            ("p", "De <strong>conclusie</strong> is geen samenvatting. Ze trekt de lijn dóór: omdat dit en dat "
                  "waar is, moet er dit gebeuren. Ze staat meestal in het <strong>slot</strong> van de "
                  "IMS-structuur, en ze voegt geen nieuw argument meer toe. Een ander woord voor de "
                  "conclusie is het <strong>besluit</strong>."),
        ]),
        dict(kop="Een argumentatieve tekst uit elkaar halen", blokken=[
            ("p", "Een <strong>argumentatieve tekst</strong> is een tekst waarin iemand argumenten geeft ter "
                  "ondersteuning van een standpunt: een pleidooi, een betoog, een debat. Verwar hem niet met "
                  "een <strong>opiniërende tekst</strong>: daarin geeft iemand zijn mening, maar die hoeft "
                  "niet als redenering opgebouwd te zijn. Een recensie mag bij een oordeel blijven. Een "
                  "<strong>opiniestuk</strong> zit daar tussenin: het geeft een mening, maar een goed "
                  "opiniestuk onderbouwt die met argumenten."),
            ("p", "Lees zo'n tekst in deze volgorde. Eerst: waarover gaat de discussie, wat is de "
                  "<strong>stelling</strong>? Dan: aan welke kant staat de schrijver, wat is zijn "
                  "<strong>standpunt</strong>? Dan: welke <strong>argumenten</strong> geeft hij, en steunen "
                  "die echt zijn standpunt? Ten slotte: welke <strong>conclusie</strong> trekt hij, en volgt "
                  "die uit wat ervoor stond?"),
            ("p", "Let op het <strong>tegenargument</strong>. Als een schrijver het sterkste bezwaar zelf "
                  "noemt en daarna weerlegt, is hij niet van mening veranderd. Hij maakt zijn tekst net "
                  "sterker, want de lezer die dat bezwaar had, voelt zich gehoord."),
            ("weetje", "Vijf argumenten die naast de kwestie liggen, wegen minder dan één argument dat "
                       "precies over de stelling gaat. Een lezer telt niet, een lezer weegt."),
        ]),
        dict(kop="Zelf argumenteren", blokken=[
            ("p", "Begin niet bij je gevoel maar bij wat je weet. Zoek uit wat de <strong>bronnen</strong> "
                  "erover zeggen, bepaal dan je standpunt, en zoek er argumenten bij die je kan verdedigen als "
                  "iemand tegenwerpingen heeft."),
            ("p", "Een goed argument is <strong>controleerbaar</strong>, het gaat <strong>echt over de "
                  "stelling</strong>, en het geldt voor <strong>meer mensen dan jij alleen</strong>. Je eigen "
                  "ervaring mag je gebruiken, en ze maakt je tekst levendig, maar zet er iets naast dat breder "
                  "geldt: één ervaring zegt nog niets over iedereen."),
            ("p", "Wil je iemand echt <strong>overtuigen</strong>, dan telt ook hóé je het zegt. Bij een "
                  "<strong>onbekende volwassene</strong> kies je een <strong>formeel register</strong>: je "
                  "spreekt hem aan met <em>u</em> en je sluit af met een nette <strong>slotgroet</strong>, "
                  "niet met <em>groetjes</em>. Een sterk argument in de verkeerde toon komt niet aan."),
            ("p", "Bouw je tekst op als <strong>stelling, argumenten, conclusie</strong>, in die volgorde. "
                  "Zo kan je lezer je volgen: eerst weten waarover het gaat, dan waarom, dan wat eruit volgt."),
            ("kader", "Lees je eigen tekst na met drie vragen. Staat mijn stelling er duidelijk in? "
                      "Onderbouwt elk argument echt mijn standpunt? Volgt mijn conclusie uit wat ervoor staat? "
                      "Lengte is geen antwoord op geen van de drie."),
        ]),
        dict(kop="In dialoog over een maatschappelijk thema", blokken=[
            ("p", "Op het examen ga je in <strong>dialoog</strong> over een maatschappelijk thema. Je mag je "
                  "argumenten uit <strong>één of enkele bronnen</strong> halen, en je reageert "
                  "<strong>respectvol en oplossingsgericht</strong> op je gesprekspartner."),
            ("p", "<strong>Oplossingsgericht</strong> betekent dat je samen zoekt naar iets waar jullie allebei "
                  "mee verder kunnen, in plaats van naar gelijk. Geeft de ander een argument dat klopt en dat "
                  "je nog niet kende, dan erken je dat en pas je zo nodig je standpunt aan. Dat is geen "
                  "verlies; het is net wat een gesprek voor heeft op een ruzie."),
            ("p", "Lees je twee bronnen die elkaar tegenspreken, ga dan na <strong>wie de zender is</strong>, "
                  "<strong>wanneer het geschreven is</strong> en <strong>welke bronnen erin gebruikt "
                  "worden</strong>. Dat zijn dezelfde criteria waarmee je beoordeelt of een tekst betrouwbaar, "
                  "correct en bruikbaar is."),
        ]),
        gesprek("verdedig aan tafel een standpunt met twee argumenten, en vraag de ander om er één tegen in "
                "te brengen."),
    ],
    onthoud=[
        "Feit = na te gaan, mening = wat iemand ervan vindt. De vraag is niet waar het staat maar of je het kan controleren.",
        "Stelling = de uitspraak, standpunt = jouw kant, argument = de reden, conclusie = wat eruit volgt.",
        "Want, omdat, daarom en dus kondigen een argument aan.",
        "De conclusie staat in het slot en voegt geen nieuw argument meer toe.",
        "Een goed argument is controleerbaar, gaat over de stelling, en geldt breder dan jouw eigen geval.",
        "In een gesprek reageer je respectvol en oplossingsgericht; gelijk krijgen is niet het doel.",
    ],
)

# ───────────────────────── Fictie, personages, verhaallijn, tijd en ruimte
BUNDELS["fictie-personages-verhaallijn-tijd-en-ruimte" + NIEUW] = dict(
    vak=VAK, niveau=DF, titel="Fictie, personages, verhaallijn, tijd en ruimte",
    onder="De begrippen waarmee je over een boek praat, en hoe je je eigen beleving onder woorden brengt.",
    secties=[
        dict(kop="Fictie en non-fictie", blokken=[
            ("p", "<strong>Fictie</strong> is verzonnen, ook al lijkt het echt. <strong>Non-fictie</strong> "
                  "gaat over wat echt bestaat of echt gebeurd is: een biografie, een reisverslag, een boek "
                  "over de geschiedenis van je stad."),
            ("p", "Het onderscheid hangt niet aan het onderwerp. Een roman over een echte staking blijft "
                  "fictie zodra de schrijver personages en gesprekken bedenkt. Een ware aanleiding maakt een "
                  "boek nog geen non-fictie."),
            ("kader", "Vraag jezelf af: heeft de schrijver dit <em>gevonden</em> of <em>bedacht</em>? "
                      "Gevonden is non-fictie, bedacht is fictie. 'Gebaseerd op ware feiten' betekent bedacht."),
        ]),
        dict(kop="Wat is een literaire tekst?", blokken=[
            ("p", "Een <strong>literaire tekst</strong> heeft een <strong>esthetische waarde</strong> en "
                  "speelt vaak in op <strong>emoties</strong>. Op het examen kan je er een tegenkomen in heel "
                  "verschillende vormen: een <strong>strip</strong>, een <strong>lied</strong>, een "
                  "<strong>gedicht</strong>, een <strong>verhaal</strong>, een <strong>blog</strong>."),
            ("p", "De vorm zegt niets over het gewicht. Er bestaan strips over oorlog, ziekte en rouw, en er "
                  "bestaan dikke boeken die nergens over gaan. Een bijsluiter is géén literaire tekst: die "
                  "geeft instructies en is prescriptief. <strong>Literatuur</strong> lezen kan je leven "
                  "verrijken: je maakt kennis met andere mensen, ideeën, ervaringen en zienswijzen. Een "
                  "blog kan trouwens tegelijk non-fictie én literatuur zijn."),
            ("p", "Een <strong>gedicht</strong> en een <strong>lied</strong> liggen dicht bij elkaar; het "
                  "verschil is dat een lied gemaakt is om gezongen te worden. Rijm komt in allebei voor, of "
                  "net niet."),
        ]),
        dict(kop="Personages", blokken=[
            ("p", "Een <strong>personage</strong> is iemand die in het verhaal voorkomt en er iets doet. De "
                  "schrijver staat buiten het verhaal, de personages staan erin. Het "
                  "<strong>hoofdpersonage</strong> is degene rond wie het verhaal vooral draait; dat hoeft "
                  "geen aardig of dapper iemand te zijn."),
            ("p", "Goede vragen over personages zijn: <strong>wie verandert er</strong> in de loop van het "
                  "verhaal, <strong>wie staat tegenover wie</strong>, en <strong>wie neemt de beslissing</strong> "
                  "waar alles op draait."),
            ("weetje", "Een personage dat helemaal niet verandert, kan net het punt van een boek zijn: "
                       "iedereen om hem heen groeit en hij blijft staan. Dan zegt dat stilstaan iets."),
        ]),
        dict(kop="De verhaallijn", blokken=[
            ("p", "De <strong>verhaallijn</strong> is de lijn van gebeurtenissen die het verhaal aflegt: wat "
                  "er gebeurt, van begin tot eind, en in welke volgorde."),
            ("p", "Een verhaal kan <strong>meer dan één verhaallijn</strong> hebben. Veel boeken volgen twee "
                  "of drie personages afwisselend; die lijnen komen vaak pas op het einde samen."),
            ("p", "De volgorde van het vertellen hoeft niet de volgorde van de gebeurtenissen te zijn. Een "
                  "verhaal kan beginnen bij het einde, of geregeld terugspringen naar de jeugd van het "
                  "hoofdpersonage. Zulke sprongen laten je begrijpen waarom iemand vandaag doet wat hij doet."),
        ]),
        dict(kop="Tijd en ruimte", blokken=[
            ("p", "De <strong>ruimte</strong> is de plaats of de plaatsen waar het verhaal speelt: een "
                  "zolderkamer, een dorp aan zee, een ruimteschip. De <strong>tijd</strong> zegt wanneer het "
                  "speelt en hoeveel tijd het beslaat: één nacht of twintig jaar."),
            ("p", "Tijd en ruimte zijn geen decor. Ze leggen vast wat er kán gebeuren. In een dorp waar "
                  "iedereen elkaar kent, is een geheim moeilijk te bewaren. Een verhaal in één huis tijdens "
                  "één storm heeft een beperkte ruimte en een korte tijd, en wordt daar benauwd en gespannen "
                  "van."),
            ("kader", "Vier vragen die je bij elk boek kan stellen: <strong>wie</strong> (personages), "
                      "<strong>wat</strong> (verhaallijn), <strong>waar</strong> (ruimte), <strong>wanneer</strong> "
                      "(tijd). Daarna pas komt je oordeel."),
        ]),
        dict(kop="Je eigen beleving verwoorden", blokken=[
            ("p", "Voor het examen lees of beluister je <strong>twee boeken</strong> die je kiest uit de "
                  "boekenlijst in de bijlage. De literaire competentie komt aan bod in een van de gesprekken. "
                  "Je moet er je <strong>eigen beleving en interpretatie</strong> over kunnen verwoorden."),
            ("p", "Beleving is wat het boek met jóú deed. De verhaallijn navertellen laat vooral zien dát je "
                  "het gelezen hebt. Gevraagd wordt wat je ervan vond en waarom. Denk tijdens het lezen na "
                  "over vragen als: waarom spreken bepaalde aspecten me aan, of net niet? Welke "
                  "<strong>boodschap</strong> zit erin? Waarom herken ik me in een bepaald personage? Hoe zou "
                  "ik zelf reageren? Waarom roept de tekst die emotie op? Wat vond ik van het taalgebruik?"),
            ("p", "De <strong>boodschap</strong> staat er zelden letterlijk. Je leidt ze af uit wat er gebeurt "
                  "en hoe het verteld wordt. Twee lezers kunnen daarom hetzelfde boek anders interpreteren en "
                  "allebei een goed antwoord geven, zolang ze hun lezing aan de tekst kunnen ophangen."),
            ("p", "Een vraag naar het <strong>taalgebruik</strong> gaat over hoe het boek klinkt en leest: "
                  "zijn de zinnen kort of lang, lazen de woorden vlot of moeilijk, past die stijl bij het "
                  "verhaal? Je mag gerust zeggen dat een boek je niet aansprak, zolang je uitlegt waarom."),
        ]),
        gesprek("vertel iemand over het laatste boek dat je las, in drie minuten, zonder de verhaallijn na te "
                "vertellen."),
    ],
    onthoud=[
        "Fictie is bedacht, non-fictie is gevonden. 'Gebaseerd op ware feiten' blijft fictie.",
        "Een literaire tekst heeft esthetische waarde en speelt in op emoties; een strip en een lied horen erbij.",
        "Personages staan in het verhaal, de schrijver staat erbuiten.",
        "De verhaallijn is wat er gebeurt en in welke volgorde; er kunnen er meerdere zijn.",
        "De ruimte is waar, de tijd is wanneer en hoelang. Allebei bepalen ze wat er kan gebeuren.",
        "Beleving verwoorden = zeggen wat je raakte én waardoor. Navertellen is geen beleving.",
    ],
)

# ───────────────────────── Lichaamstaal, beleefdheid en een tekst die werkt
BUNDELS["lichaamstaal-beleefdheid-en-een-tekst-die-werkt" + NIEUW] = dict(
    vak=VAK, niveau=DF, titel="Lichaamstaal, beleefdheid en een tekst die werkt",
    onder="Wat je zegt zonder woorden, hoe je je taal aanpast, en de criteria waarop je tekst beoordeeld wordt.",
    secties=[
        dict(kop="Non-verbale communicatie", blokken=[
            ("p", "<strong>Non-verbale communicatie</strong> is alles wat je overbrengt náást de woorden. Ze "
                  "valt uiteen in vier groepen:"),
            ("p", tabel(["Groep", "Wat hoort erbij"], [
                ["je lichaam", "lichaamstaal, mimiek, oogcontact, houding, afstand, bewegingen"],
                ["je stem", "intonatie, articulatie, tempo, volume"],
                ["je voorkomen", "kleding en uiterlijk"],
                ["op een scherm", "emoji's"],
            ])),
            ("p", "<strong>Mimiek</strong> is wat je gezicht laat zien. <strong>Intonatie</strong> is het "
                  "stijgen en dalen van je stem; daaraan hoor je of een zin een vraag is of ironisch bedoeld. "
                  "<strong>Articulatie</strong> is hoe duidelijk je de klanken vormt, <strong>tempo</strong> "
                  "hoe snel je gaat en <strong>volume</strong> hoe luid."),
            ("p", "Ook op een scherm communiceer je non-verbaal. Een hele zin in <strong>hoofdletters</strong> "
                  "op een forum leest als schreeuwen. En wie tijdens een presentatie alles <strong>afleest</strong>, "
                  "kijkt naar zijn blad in plaats van naar de mensen, en verliest de connectie met de luisteraar."),
            ("weetje", "Lichaamstaal van een ander lezen helpt je inschatten of je boodschap aankomt. Of "
                       "iemand liegt, lees je er níét aan af; dat is een hardnekkig misverstand."),
        ]),
        dict(kop="Beleefdheid en register", blokken=[
            ("p", "Je past je taalgebruik aan je <strong>ontvanger</strong> aan. Je verandert niet wát je "
                  "zegt, maar hóé: de toon, het register, de aanspreking. Dezelfde boodschap komt anders aan "
                  "bij een vriend dan bij een directeur."),
            ("p", "Een <strong>onbekende volwassene</strong> spreek je aan met <strong>u</strong>. Het gaat "
                  "daarbij niet om leeftijd alleen maar om afstand: je oom van veertig blijf je tutoyeren. Een "
                  "<strong>formele mail</strong> sluit je niet af met <em>groetjes</em>, en smileys horen er "
                  "niet in. In een WhatsAppbericht aan vrienden ondersteunt diezelfde smiley je boodschap net."),
            ("p", "Tot de <strong>beleefdheidsconventies</strong> in een gesprek horen: je gesprekspartner "
                  "<strong>laten uitspreken</strong>, <strong>interesse tonen</strong> in wat hij zegt, en een "
                  "<strong>gepaste toon</strong> kiezen. Wachten tot iemand uitgesproken is, betekent niet dat "
                  "je hem gelijk geeft; wat jij weet, kan een zin later ook nog."),
            ("p", "Een gesprek voeren is drie dingen kunnen: het <strong>beginnen</strong>, het <strong>gaande "
                  "houden</strong> en het <strong>beëindigen</strong>. Die drie zijn aparte vaardigheden, en "
                  "de laatste wordt het vaakst vergeten."),
        ]),
        dict(kop="De criteria waarop je beoordeeld wordt", blokken=[
            ("p", "Voor elke schrijf- of spreekopdracht gelden vijf criteria, en voor schrijven en spreken "
                  "komen er nog een paar bij:"),
            ("p", tabel(["Criterium", "Wat wordt er bedoeld?"], [
                ["taakvoltooiing", "je tekstdoel is bereikt, je boodschap komt volledig over"],
                ["woordenschat", "ook minder frequente woorden en figuurlijke taal"],
                ["grammatica en zinsbouw", "correcte zinnen, en variatie in hoe je ze bouwt"],
                ["tekststructuur en samenhang", "inleiding, midden, slot, met signaalwoorden"],
                ["register en beleefdheid", "formeel of informeel, passend bij de ontvanger"],
            ])),
            ("p", tabel(["Enkel bij schrijven", "Enkel bij spreken"], [
                ["spelling en leestekengebruik", "lichaamstaal en oogcontact"],
                ["tekstopbouw en lay-out", "vlotheid"],
                ["titels en alinea-indeling", "uitspraak en intonatie"],
            ])),
            ("p", "<strong>Taakvoltooiing</strong> is het zwaarste criterium en het makkelijkst te missen: een "
                  "tekst zonder één spelfout die zijn doel niet bereikt, voldoet niet. <strong>Variatie in "
                  "zinsbouw</strong> betekent dat je niet elke zin op dezelfde manier opbouwt; vijf zinnen na "
                  "elkaar die met hetzelfde woord beginnen, lezen vlak."),
            ("p", "Een <strong>gepaste lay-out</strong> heeft niet altijd tussentitels nodig. <em>Indien "
                  "nodig</em> gebruik je titels of tussentitels; in een korte mail zouden ze net vreemd staan. "
                  "Wat wél altijd geldt: per <strong>alinea</strong> één deelonderwerp."),
        ]),
        dict(kop="Wat je met taal doet", blokken=[
            ("p", "Bij een <strong>spreekopdracht</strong> ben je alleen aan het woord. Met "
                  "<strong>interactie</strong> wordt bedoeld dat je <strong>schriftelijk reageert</strong> op "
                  "anderen of in <strong>gesprek</strong> gaat met iemand. Schriftelijke interactie is "
                  "bijvoorbeeld reageren op een discussie op een forum; een verhaal voorlezen voor een klas "
                  "is dat niet."),
            ("p", "Er zijn zeven dingen die je met taal moet kunnen doen:"),
            ("p", tabel(["Wat je doet", "Voorbeeld"], [
                ["informatie geven en vragen", "een nieuwsbrief schrijven, iets vragen in een winkel"],
                ["iemand iets uitleggen", "een korte handleiding voor een beamer, een stappenplan"],
                ["je mening geven", "een product beoordelen, je standpunt over een probleem geven"],
                ["iemand overtuigen", "een antirookpamflet, onderhandelen met je ouders"],
                ["iets vertellen", "een mail over een uitstap, vertellen wat je meemaakte"],
                ["in dialoog gaan", "samen bepalen welk goed doel je steunt"],
                ["creatief zijn met taal", "een verhaal, een gedicht, een reclameboodschap"],
            ])),
            ("p", "<strong>Creatief zijn met taal</strong> betekent dat je technieken gebruikt: "
                  "<strong>rijm</strong>, <strong>ritme</strong>, <strong>spanningsopbouw</strong>, "
                  "<strong>humor</strong>, <strong>stijlfiguren</strong>, <strong>spelen met tijd en "
                  "ruimte</strong>. Zo veel mogelijk moeilijke woorden gebruiken hoort daar níét bij; dat "
                  "mist meestal zijn doel."),
            ("p", "Op het examen neem je de <strong>spreekopdracht thuis op</strong> en dien je ze in tot "
                  "drie dagen voor je digitale examen. Voor de <strong>mondelinge opdrachten</strong> krijg "
                  "je vijftien minuten <strong>voorbereidingstijd</strong> voor twee opdrachten, maar je "
                  "moet ook <strong>spontaan</strong> kunnen reageren: wat je gesprekspartner zegt, staat "
                  "niet op je blad."),
        ]),
        dict(kop="Strategieën", blokken=[
            ("p", "Bij <strong>lezen en luisteren</strong>: stel jezelf eerst vragen over wat je al weet; "
                  "gebruik het <strong>communicatiemodel</strong> (van wie is de tekst, waarom, voor wie?); "
                  "gebruik de <strong>visuele hulpmiddelen</strong> zoals de titel, de tussentitels, benadrukte "
                  "woorden, een foto of een grafiek; let op <strong>structuuraanduiders</strong>, dat zijn "
                  "<strong>verwijswoorden</strong> zoals <em>zij, hem, deze, hun</em> en "
                  "<strong>signaalwoorden</strong> zoals <em>maar, ten eerste, tot slot, dus, want, "
                  "hoewel, als</em>; maak "
                  "onderscheid tussen <strong>hoofd- en bijzaken</strong>; let op ironie en op objectieve of "
                  "subjectieve taal."),
            ("p", "Kom je een <strong>onbekend woord</strong> tegen, leid de betekenis dan eerst af uit de "
                  "<strong>context</strong>, uit je voorkennis of uit de manier waarop het woord "
                  "<strong>gevormd</strong> is: misschien is het een afleiding of een samenstelling, of helpt "
                  "je kennis van een vreemde taal. Zoek enkel op wat je echt nodig hebt; je hebt op het examen "
                  "geen tijd om elk woord op te zoeken."),
            ("p", "Bij <strong>spreken en schrijven</strong>: maak een <strong>plan met kernwoorden</strong>, "
                  "niet met uitgeschreven zinnen, anders lees je af. Pas je taal aan de ontvanger aan. Speel "
                  "in op wat je gesprekspartner zegt. Zit je vast, zoek dan een omschrijving of herlees een "
                  "stukje; je doel bereiken op een andere manier mag."),
            ("p", "Op het examen mag je een <strong>online woordenboek</strong> en een "
                  "<strong>spellingcontrole</strong> gebruiken; de links staan in je examen zelf. Oefen er "
                  "thuis mee. Lees je tekst voor je hem indient grondig na: is de communicatie "
                  "<strong>helder, gepast, correct en vlot</strong>?"),
        ]),
        dict(kop="Notities nemen", blokken=[
            ("p", "Je moet <strong>notities</strong> kunnen nemen bij een tekst die je leest of beluistert. Er "
                  "is maar één eis: ze sluiten aan bij de inhoud en ze zijn achteraf nog <strong>bruikbaar</strong>, "
                  "bijvoorbeeld om er een samenvatting mee te maken of een vraag mee te beantwoorden."),
            ("p", "Volledige zinnen hoeven niet. <strong>Afkortingen</strong>, <strong>symbolen</strong> en "
                  "<strong>telegramstijl</strong> mogen, en een <strong>schema</strong>, een "
                  "<strong>tabel</strong> of een <strong>mindmap</strong> laat verbanden vaak sneller zien dan "
                  "losse zinnen."),
            ("kader", "Alles opschrijven is geen notitie nemen maar overschrijven. Wie alles noteert, luistert "
                      "niet meer. Noteer wat je straks nodig hebt, en niets anders."),
        ]),
        gesprek("bel zelf naar een winkel of een gemeentedienst om iets te vragen, en let daarbij op je tempo "
                "en je aanspreking."),
    ],
    onthoud=[
        "Non-verbaal = je lichaam, je stem, je voorkomen en je emoji's.",
        "Mimiek = gezicht, intonatie = stijgen en dalen, articulatie = duidelijkheid, tempo = snelheid, volume = luidheid.",
        "Hoofdletters op een forum lezen als schreeuwen; alles aflezen kost je de connectie met je publiek.",
        "U bij een onbekende volwassene. Geen groetjes en geen smileys in een formele mail.",
        "Taakvoltooiing is het zwaarste criterium: een foutloze tekst die zijn doel mist, voldoet niet.",
        "Spelling en lay-out gelden enkel voor schrijven; vlotheid, uitspraak en intonatie enkel voor spreken.",
        "Notities mogen in telegramstijl, als je er achteraf nog iets mee kan.",
    ],
)

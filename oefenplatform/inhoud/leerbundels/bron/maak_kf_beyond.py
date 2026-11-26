# -*- coding: utf-8 -*-
"""Leerbundels, oefenbundels en uitlegbladen bij kunstbeschouwing en filosofie
🌍 Beyond doorstroom.

Gebaseerd op de vakfiche `Kunstbeschouwing_en_filosofie_3DDO` (humane
wetenschappen). Het vak deelt twaalf filosofiethema's met filosofie en recht:
die bundels nemen we hier woord voor woord over uit `maak_filorecht.py` en
`maak_oefeningen_filorecht.py`, enkel met de vaknaam van dit vak, zodat ze in
de juiste map en zip komen. Nieuw zijn de zeven kunstthema's, de zijnsleer en
de twee thema's politieke filosofie.

De afspraak blijft: een bundel dekt de vragen van zijn hoofdstuk
(`../../beyond/kunstbeschouwing-en-filosofie.json`), met dezelfde woorden.
Kunstwerken worden beschreven, niet afgebeeld: geen foto's van bestaande
werken, enkel eigen schema's.
"""
import sys, pathlib, copy
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Kunstbeschouwing en filosofie"
BEYOND = "🌍 Beyond doorstroom — 5de en 6de middelbaar"
tabel = bundel.tabel

W = "130px"
WW = "200px"
WL = "260px"

BUNDELS = {}
OEFENBUNDELS = {}
UITLEGBLADEN = {}

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een ongezien werk: noem niet alleen de stroming, maar ook waaraan je ze herkent.",
    "Lees bij twee begrippen die op elkaar lijken eerst nog eens wat ze onderscheidt.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]


def sleutel(titel):
    return bundel_slug(titel) + "-beyond-doorstroom"


def bundel_slug(t):
    import re, unicodedata
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


# ═════════════════════════ 1. Kunst, cultuur en de kunstvormen
S1 = sleutel("Kunst, cultuur en de kunstvormen")
BUNDELS[S1] = dict(
    vak=VAK, niveau=BEYOND, titel="Kunst, cultuur en de kunstvormen",
    onder="Cultuur in enge en brede betekenis, de kunstvormen, en de middelen van vormgeving met de bouwstenen per kunstvorm.",
    secties=[
        dict(kop="Kunst als deel van een cultuur", blokken=[
            ("p", tabel(["Betekenis van cultuur", "Wat hoort erbij?", "Voorbeeld"], [
                ["eng", "vooral kunst: wat men vroeger de hogere vormen van beschaving noemde", "een symfonie, een roman, een schilderij"],
                ["breed", "alles wat een groep mensen aanleert en doorgeeft: taal, waarden, gewoonten, kleding, eten en ook kunst", "drie kussen als begroeting, het zondagse eten"],
            ])),
            ("kader", "<strong>Kunst groeit uit een cultuur en zegt er iets over.</strong> Ze toont wat een "
                      "groep belangrijk vindt, en kan die cultuur ook mee vormen of in vraag stellen."),
        ]),
        dict(kop="De kunstvormen", blokken=[
            ("p", tabel(["Kunstvorm", "Wat is het?", "Voorbeelden"], [
                ["architectuur en design", "vorm die ook moet werken en een doel dienen", "een gebouw, een stoel"],
                ["audiovisuele kunsten", "met beeld en geluid, of met een camera gemaakt", "film, fotografie, videokunst"],
                ["beeldende kunsten", "kunst die je bekijkt als voorwerp", "schilderkunst, beeldhouwkunst"],
                ["conceptuele kunst", "het idee is het eigenlijke werk, het voorwerp is bijzaak", "een bordje met een opdracht"],
                ["installatiekunst", "de kunstenaar richt een hele ruimte in, de bezoeker staat erin", "een hal vol lichtjes en geluid"],
                ["literatuur", "kunst met taal als materiaal", "romans, gedichten, toneelteksten"],
                ["podiumkunsten", "live uitgevoerd voor een publiek", "dans, theater, muziek"],
            ])),
            ("kader", "<strong>Let op:</strong> in deze indeling hoort fotografie bij de audiovisuele kunsten, "
                      "niet bij de beeldende kunsten."),
        ]),
        dict(kop="De middelen van vormgeving", blokken=[
            ("p", "Elk werk wordt gemaakt met drie middelen: de <strong>bouwstenen</strong>, het "
                  "<strong>materiaal</strong> (waarmee) en de <strong>techniek</strong> (hoe). Brons is "
                  "een materiaal, gieten in een mal is een techniek. De opdrachtgever is geen middel: die "
                  "hoort bij de context."),
            ("p", tabel(["Kunstvorm", "Bouwstenen"], [
                ["beeld", "vorm, kleur, licht, textuur, lijn, ruimte, compositie"],
                ["dans", "ruimte, tijd, kracht, vorm, relatie"],
                ["drama", "rol, ruimte, tijd, structuur, samenspel"],
                ["media", "kader, licht, geluid, camera, montage"],
                ["muziek", "ritme, melodie, dynamiek, tempo, klankkleur, harmonie, structuur"],
            ])),
            ("p", tabel(["Bouwsteen", "Waar kijk je naar?"], [
                ["licht (beeld)", "heldere of donkere indruk, schaduwen, contrast tussen licht en donker"],
                ["textuur", "ruw of glad oppervlak, de drager, het instrument: penseel, paletmes, spons, spuitbus"],
                ["ruimte (beeld)", "perspectief, ruimtelijk effect van schaduw, afgesneden figuren aan de rand"],
                ["compositie", "spreiding en rangschikking, denkbeeldige figuren zoals een driehoek of cirkel"],
                ["kracht (dans)", "energie: slappe, vloeiende, krachtige of hoekige bewegingen"],
                ["relatie (dans)", "synchroon of niet, inspelen op elkaar, interactie met het publiek"],
                ["structuur (drama)", "begin, verloop en einde; makkelijke of moeilijke verhaallijn"],
                ["kader (media)", "long shot, medium shot, close-up; vogel-, kikker- of ooghoogteperspectief"],
                ["montage (media)", "cuts of naadloze overgangen (dissolve), fades, slow motion"],
                ["klankkleur (muziek)", "welk instrument of welke stem de melodie brengt"],
                ["dynamiek (muziek)", "sterk of zacht, crescendo of decrescendo"],
            ])),
        ]),
    ],
    onthoud=[
        "Enge betekenis van cultuur: vooral kunst. Brede betekenis: alles wat een groep aanleert en doorgeeft.",
        "Fotografie hoort bij de audiovisuele kunsten; dans, theater en muziek bij de podiumkunsten.",
        "Installatiekunst: de ruimte is het werk. Conceptuele kunst: het idee is het werk.",
        "Drie middelen van vormgeving: bouwstenen, materiaal, techniek.",
        "Tempo hoort bij kunstvormen die in de tijd verlopen: muziek, dans, drama. Compositie hoort bij beeld.",
    ],
)

OEFENBUNDELS["oefenbundel-" + S1] = dict(
    vak=VAK, niveau=BEYOND, titel="Kunst, cultuur en de kunstvormen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Cultuur en kunstvormen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("een opera", "eng"), ("de gewoonte om elkaar drie kussen te geven", "breed"),
                          ("een roman", "eng"), ("wat een familie op zondag eet", "breed")],
                  "Cultuur in de enge of de brede betekenis?", W),
                 ("rij", [("een documentaire", "audiovisueel"), ("een balletvoorstelling", "podiumkunst"),
                          ("een marmeren beeld", "beeldend"), ("een reeks zwart-witfoto's", "audiovisueel")],
                  "Welke kunstvorm?", WW),
                 ("open", "Leg het verschil uit tussen installatiekunst en conceptuele kunst.",
                  "Bij installatiekunst richt de kunstenaar een hele ruimte in en staat de bezoeker er middenin. "
                  "Bij conceptuele kunst is het idee het eigenlijke werk en is het voorwerp bijzaak.", 3),
             ]),
        dict(kop="Bouwstenen",
             opdracht="Bij welke bouwsteen hoort het?",
             oefeningen=[
                 ("rij", [("veel of weinig contrast tussen licht en donker", "licht"),
                          ("een ruw oppervlak, met een paletmes", "textuur"),
                          ("figuren in een denkbeeldige driehoek", "compositie"),
                          ("afgesneden figuren aan de rand", "ruimte")],
                  "Beeld", WW),
                 ("rij", [("een crescendo", "dynamiek"), ("een trompet speelt de melodie", "klankkleur"),
                          ("intro, strofe, refrein", "structuur"), ("de muziek versnelt", "tempo")],
                  "Muziek", WW),
                 ("tabel", ["Kunstvorm", "Twee bouwstenen"],
                  [["dans", None], ["drama", None], ["media", None]],
                  "bv. kracht en relatie; rol en samenspel; kader en montage", WL),
             ]),
        dict(kop="Middelen van vormgeving",
             opdracht="Duid aan of vul aan.",
             oefeningen=[
                 ("rij", [("brons", "materiaal"), ("gieten in een mal", "techniek"),
                          ("olieverf", "materiaal"), ("in dunne lagen schilderen", "techniek")],
                  "Materiaal of techniek?", W),
                 ("kies", "Welke is geen middel van vormgeving?", ["bouwstenen", "materiaal", "techniek", "opdrachtgever"], 3),
                 ("kort", "Een harde overgang tussen twee shots heet een ...", "cut", W),
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-" + S1] = dict(reeksen=[
    dict(aanpak="Vraag je af: is het kunst, of een gewoonte van een groep? Kunst is eng én breed, een gewoonte enkel breed.",
         waarom=[None, "Fotografie staat bij de audiovisuele kunsten, ook al hangt een foto aan de muur.",
                 "Zoek het verschil in wat het werk is: de ruimte of het idee."]),
    dict(aanpak="Leer de bouwstenen per kunstvorm als een rijtje, en koppel er telkens één voorbeeld aan.",
         waarom=["Driehoek en cirkel horen bij compositie, niet bij vorm.", None,
                 "Elke kunstvorm heeft eigen bouwstenen. Tempo en ruimte komen bij meer kunstvormen voor."]),
    dict(aanpak="Waarmee is materiaal, hoe is techniek.",
         waarom=[None, "De opdrachtgever hoort bij de context.", "Een naadloze overgang is een dissolve."]),
])


# ═════════════════════════ 2. Inhoud, functies en context
S2 = sleutel("Inhoud, functies en context van een kunstuiting")
BUNDELS[S2] = dict(
    vak=VAK, niveau=BEYOND, titel="Inhoud, functies en context van een kunstuiting",
    onder="Het onderwerp en de zeven functies van kunst, en de context: tijd, ruimte, politiek, sociaal, cultureel en persoonlijk.",
    secties=[
        dict(kop="De inhoud: onderwerp en functies", blokken=[
            ("p", "De <strong>inhoud</strong> van een kunstuiting bestaat uit twee delen: het "
                  "<strong>onderwerp</strong> (wat je ziet of hoort) en de <strong>functies</strong> "
                  "(waarvoor het werk dient)."),
            ("p", tabel(["Functie", "Het werk wil vooral ...", "Voorbeeld"], [
                ["decoratief", "versieren, een ruimte of voorwerp mooier maken", "een tapijt in een kasteelzaal, een tegelpatroon"],
                ["economisch", "geld opbrengen", "beeldjes die meteen online verkocht worden"],
                ["filosofisch", "doen nadenken over grote vragen", "een werk over de zin van het leven of de dood"],
                ["maatschappijkritisch", "iets in de samenleving aanklagen", "graffiti tegen de consumptiemaatschappij"],
                ["narratief", "een verhaal vertellen", "een strip, een glasraam met het leven van een heilige"],
                ["ontspannend", "plezier geven", "een popsong om op te dansen"],
                ["politiek", "macht tonen of mensen overtuigen", "een ruiterstandbeeld, propaganda-affiche"],
            ])),
            ("kader", "<strong>Een werk kan meerdere functies tegelijk hebben.</strong> Een glasraam vertelt en "
                      "versiert, een spotprent ontspant en geeft kritiek."),
        ]),
        dict(kop="De context", blokken=[
            ("p", tabel(["Context", "Wat bedoel je?", "Voorbeeld"], [
                ["tijd", "de periode waarin het werk ontstond en wat toen gewoon, nieuw of verboden was", "een werk uit de 15de eeuw, toen olieverf nieuw was"],
                ["ruimte", "de plaats of streek waar en waarvoor het werk gemaakt werd", "een fresco voor één bepaalde kapel"],
                ["politiek", "macht, oorlog, censuur", "een lied tegen de bezetter"],
                ["sociaal", "hoe mensen samenleven: armoede, klassen", "foto's van boerengezinnen in een crisis"],
                ["cultureel", "waarden en gewoonten, wat als kunst geldt", "geen mensen afbeelden in heilige gebouwen"],
                ["persoonlijk", "wat de kunstenaar zelf meemaakte", "donkere werken na de dood van een kind"],
            ])),
            ("kader", "<strong>Valkuilen.</strong> Ruimte gaat niet over de lege plekken op het doek of de zaal "
                      "waar het werk vandaag hangt. Tijd gaat niet over hoe lang een film duurt. En de persoonlijke "
                      "context verklaart nooit alles: ook de tijd, de plaats en de samenleving vormen een werk."),
        ]),
        dict(kop="Samenhang", blokken=[
            ("p", "Inhoud, functie, context en vormgeving beïnvloeden elkaar. <strong>De context verklaart de "
                  "functie, en de functie verklaart de vormgeving.</strong> Een groot schilderij van een leider "
                  "tussen juichende mensen (inhoud) wil overtuigen (politieke functie) omdat het uit een "
                  "dictatuur komt (context), en is daarom groots en duidelijk geschilderd (vormgeving)."),
        ]),
    ],
    onthoud=[
        "Inhoud = onderwerp + functies.",
        "Zeven functies: decoratief, economisch, filosofisch, maatschappijkritisch, narratief, ontspannend, politiek.",
        "Context: tijd, ruimte, politiek-sociaal-cultureel, persoonlijk.",
        "Ruimte is de plaats waarvoor het werk gemaakt werd, niet de lege plekken op het doek.",
        "De context verklaart de functie, de functie verklaart de vormgeving.",
    ],
)

OEFENBUNDELS["oefenbundel-" + S2] = dict(
    vak=VAK, niveau=BEYOND, titel="Inhoud, functies en context van een kunstuiting",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Functies",
             opdracht="Welke functie staat voorop?",
             oefeningen=[
                 ("rij", [("een spotprent op bankiers", "maatschappijkritisch"), ("een vrolijke popsong", "ontspannend"),
                          ("een groot ruiterstandbeeld van een koning", "politiek"), ("een strip over een ridder", "narratief")],
                  "Functie?", WW),
                 ("waar", "Een werk heeft altijd maar één functie.", False),
                 ("kort", "Een tegelpatroon dat een muur versiert, heeft een ... functie.", "decoratieve", WW),
             ]),
        dict(kop="Context",
             opdracht="Over welk deel van de context gaat het?",
             oefeningen=[
                 ("rij", [("geschilderd in 1937", "tijd"), ("voor het Spaanse paviljoen in Parijs", "ruimte"),
                          ("tijdens de Spaanse Burgeroorlog", "politiek"), ("na de dood van zijn vrouw", "persoonlijk")],
                  "Context?", WW),
                 ("kies", "Wat bedoelt men met de ruimte als context?",
                  ["de plaats waarvoor het werk gemaakt werd", "de lege plekken op het doek",
                   "de afmetingen van het doek", "de zaal waar het werk nu hangt"], 0),
                 ("open", "Waarom vertelt de persoonlijke context niet altijd alles over een werk?",
                  "Een werk wordt ook gevormd door de tijd, de plaats en de samenleving rond de kunstenaar.", 2),
             ]),
        dict(kop="Samenhang",
             opdracht="Leg uit.",
             oefeningen=[
                 ("open", "Guernica is enkel in zwart, wit en grijs geschilderd. Leg het verband uit tussen context, functie en vormgeving.",
                  "De context is het bombardement in de Spaanse Burgeroorlog. Het werk klaagt de gruwel aan "
                  "(maatschappijkritische functie). De sombere kleuren en gebroken vormen versterken die pijn.", 4),
                 ("rij", [("een moeder met een kind", "onderwerp"), ("de kijker doen nadenken over armoede", "functie"),
                          ("drie appels op een tafel", "onderwerp")],
                  "Onderwerp of functie?", W),
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-" + S2] = dict(reeksen=[
    dict(aanpak="Vraag je af wat het werk vooral wil doen: versieren, vertellen, kritiek geven, overtuigen, ontspannen, doen nadenken of geld opbrengen.",
         waarom=["Een standbeeld van een vorst toont macht: politiek.", "Een glasraam vertelt en versiert tegelijk.", None]),
    dict(aanpak="Jaartal: tijd. Plaats: ruimte. Oorlog of censuur: politiek. Eigen leven: persoonlijk.",
         waarom=[None, "Ruimte is de plaats waarvoor het gemaakt werd, niet de lege plekken.", None]),
    dict(aanpak="Leg de ketting: context, dan functie, dan vormgeving.",
         waarom=["Noem de drie stappen, elk met een voorbeeld uit het werk.", "Wat je ziet, is het onderwerp."]),
])


# ═════════════════════════ 3. Prehistorie, Egypte en klassieke oudheid
S3 = sleutel("Kunst van de prehistorie, Egypte en de klassieke oudheid")
BUNDELS[S3] = dict(
    vak=VAK, niveau=BEYOND, titel="Kunst van de prehistorie, Egypte en de klassieke oudheid",
    onder="Context, vormelijke kenmerken en bekendste werken van de prehistorie, Egypte en het nabije Oosten, Griekenland en Rome.",
    secties=[
        dict(kop="Prehistorie en Egypte", blokken=[
            ("p", tabel(["", "Prehistorie", "Egypte en het nabije Oosten"], [
                ["context", "jagers en verzamelaars, zonder schrift", "farao als god, geloof in een leven na de dood"],
                ["vormelijke kenmerken", "jachtdieren op grotwanden; oker, houtskool en aarde, verf soms geblazen door een buis", "frontaal, symmetrisch, stijf; hoofd en benen van opzij, oog en schouders van voren; de belangrijkste figuur het grootst"],
                ["bekende werken", "Lascaux, Altamira, de Venus van Willendorf (zo'n 11 cm, vruchtbaarheid?)", "de piramiden van Gizeh (grafmonumenten), hiërogliefen; ziggoerat en Ishtarpoort (blauwe geglazuurde bakstenen) in Mesopotamië"],
            ])),
            ("kader", "<strong>Waarom grotschilderingen?</strong> Zeker weten we het niet: er zijn geen geschreven "
                      "bronnen. Men denkt aan rituelen of magie rond de jacht. <strong>Waarom bleef Egyptische "
                      "kunst duizenden jaren gelijk?</strong> Vaste regels en het streven naar eeuwigheid."),
        ]),
        dict(kop="Griekse kunst", blokken=[
            ("p", "In stadstaten zoals Athene stonden de mens en de rede centraal. Beeldhouwers zochten een "
                  "<strong>ideaal, harmonieus lichaam</strong> met perfecte verhoudingen. Vroege Griekse beelden "
                  "leken nog op Egyptische; in de klassieke periode kwam het <strong>contrapposto</strong>: het "
                  "gewicht op één been, heupen en schouders tegengesteld gekanteld."),
            ("p", tabel(["Bouworde", "Kenmerk"], [
                ["Dorisch", "sober, eenvoudig kapiteel, geen voet (het Parthenon)"],
                ["Ionisch", "voluten of krullen aan het kapiteel"],
                ["Korinthisch", "kapiteel vol acanthusbladeren"],
            ])),
            ("p", "Bekende namen: <strong>Phidias</strong> (beeldhouwwerk van het Parthenon), <strong>Myron</strong> "
                  "(de Discuswerper), <strong>Polykleitos</strong> (de Doryphoros of speerdrager, de canon). Griekse "
                  "beelden waren oorspronkelijk beschilderd; veel bronzen originelen kennen we via Romeinse kopieën."),
        ]),
        dict(kop="Romeinse kunst", blokken=[
            ("p", "De Romeinen namen de bouworden en het beeldhouwen over, maar voegden eigen dingen toe. Hun "
                  "portretten zijn <strong>realistisch</strong>, met rimpels en eigen trekken. Met de "
                  "<strong>rondboog</strong>, de <strong>koepel</strong> en <strong>beton</strong> bouwden ze "
                  "aquaducten, het <strong>Pantheon</strong> (koepel met oculus) en het <strong>Colosseum</strong> "
                  "(amfitheater). Kunst en bouwkunst dienden het rijk: nuttig en indrukwekkend."),
            ("kader", "<strong>Parthenon of Pantheon?</strong> Het Parthenon is Grieks, op de Akropolis in Athene. "
                      "Het Pantheon is Romeins, in Rome, met een betonnen koepel."),
        ]),
    ],
    onthoud=[
        "Prehistorie: jachtdieren, natuurlijke pigmenten, geen schrift.",
        "Egypte: frontaal, aspectief, hiërarchische grootte, gericht op eeuwigheid.",
        "Grieks: ideaal lichaam, contrapposto, Dorisch-Ionisch-Korinthisch.",
        "Romeins: realistisch portret, rondboog, koepel, beton.",
        "Myron: Discuswerper. Polykleitos: Doryphoros. Phidias: Parthenon.",
    ],
)

OEFENBUNDELS["oefenbundel-" + S3] = dict(
    vak=VAK, niveau=BEYOND, titel="Kunst van de prehistorie, Egypte en de klassieke oudheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Herken de periode",
             opdracht="Uit welke kunst komt het?",
             oefeningen=[
                 ("rij", [("hoofd van opzij, oog van voren", "Egypte"), ("een oud borstbeeld met rimpels", "Rome"),
                          ("bizons in oker op een grotwand", "prehistorie"), ("een atleet in contrapposto", "Griekenland")],
                  "Periode?", WW),
                 ("kort", "De trapvormige tempeltoren uit Mesopotamië heet een ...", "ziggoerat", WW),
                 ("waar", "Egyptische kunstenaars gebruikten een verdwijnpunt.", False),
             ]),
        dict(kop="Griekse bouworden en namen",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Bouworde", "Kenmerk"], [["Dorisch", None], ["Ionisch", None], ["Korinthisch", None]],
                  "sober, geen voet; voluten; acanthusbladeren", WL),
                 ("rij", [("de Discuswerper", "Myron"), ("de Doryphoros", "Polykleitos"), ("het Parthenon", "Phidias")],
                  "Wie?", WW),
             ]),
        dict(kop="Vergelijk",
             opdracht="Leg uit.",
             oefeningen=[
                 ("open", "Vergelijk een Egyptisch beeld met een klassiek Grieks beeld: één verschil in vorm, één in context.",
                  "Vorm: Egyptisch is stijf en frontaal, Grieks staat los in contrapposto. Context: Egyptische kunst was "
                  "gericht op eeuwigheid en het leven na de dood, Griekse kunst op de mens en de rede.", 4),
                 ("kies", "Welk gebouw heeft een betonnen koepel met een oculus?",
                  ["het Pantheon", "het Parthenon", "het Colosseum", "de Ishtarpoort"], 0),
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-" + S3] = dict(reeksen=[
    dict(aanpak="Zoek het opvallendste kenmerk: aspectief en stijf is Egypte, ideaal en los is Griekenland, realistisch portret is Rome.",
         waarom=[None, None, "Het perspectief met verdwijnpunt komt pas in de renaissance."]),
    dict(aanpak="Van sober naar rijk: Dorisch, Ionisch, Korinthisch.",
         waarom=[None, "De Doryphoros is van Polykleitos, de Discuswerper van Myron."]),
    dict(aanpak="Zet telkens vorm tegenover vorm en context tegenover context.",
         waarom=[None, "Parthenon is Grieks, Pantheon Romeins."]),
])


# ═════════════════════════ 4. Middeleeuwen, renaissance en barok
S4 = sleutel("Middeleeuwen, renaissance en barok")
BUNDELS[S4] = dict(
    vak=VAK, niveau=BEYOND, titel="Middeleeuwen, renaissance en barok",
    onder="Romaans, gotiek, Vlaamse primitieven, renaissance en barok: context, kenmerken en bekende namen.",
    secties=[
        dict(kop="Romaans en gotiek", blokken=[
            ("p", "In de middeleeuwen was de <strong>kerk</strong> de grootste opdrachtgever. Kunst moest het "
                  "geloof uitleggen aan mensen die niet konden lezen: de bijbel van de armen."),
            ("p", tabel(["", "Romaans", "Gotiek"], [
                ["muren en ramen", "dikke muren, kleine ramen, eerder donker", "dunnere muren, enorme glasramen en roosvensters"],
                ["bogen", "rondboog", "spitsboog"],
                ["steun", "de muren dragen het gewicht", "luchtbogen en steunberen vangen de druk op"],
                ["doel", "stevig en beschermend", "hoogte en licht, naar de hemel en God"],
                ["voorbeeld", "", "de Notre-Dame van Parijs, de kathedraal van Chartres"],
            ])),
        ]),
        dict(kop="De Vlaamse primitieven", blokken=[
            ("p", "In de 15de eeuw werkten in rijke handelssteden zoals Brugge en Gent schilders met "
                  "<strong>olieverf in dunne lagen</strong>. Ze toonden stoffen, juwelen, glas en spiegelingen tot in "
                  "het kleinste detail. Het onderwerp bleef vaak religieus, maar de wereld errond werd realistisch, "
                  "met kamers en doorkijkjes naar steden. Vroeger kregen heiligen een <strong>gouden achtergrond</strong> "
                  "zonder diepte."),
            ("p", "<strong>Jan van Eyck</strong> schilderde met zijn broer Hubert het <strong>Lam Gods</strong> "
                  "(Sint-Baafskathedraal, Gent), een veelluik, en het <strong>Arnolfiniportret</strong> met de bolle spiegel."),
            ("kader", "<strong>Primitief</strong> betekent hier: de eersten van een nieuwe schilderkunst, niet ongeschoold."),
        ]),
        dict(kop="Renaissance en barok", blokken=[
            ("p", tabel(["", "Renaissance", "Barok"], [
                ["context", "wedergeboorte van de oudheid, humanisme, Italië (Florence, Medici)", "contrareformatie: de kerk wil ontroeren"],
                ["kenmerken", "rust, symmetrie, lijnperspectief met één verdwijnpunt, de mens centraal", "beweging, diagonalen, emotie, clair-obscur, rijke versiering"],
                ["namen", "Leonardo da Vinci (Mona Lisa, sfumato), Michelangelo (David, Sixtijnse Kapel), Rafaël", "Rubens (Antwerpen), Rembrandt (Nachtwacht), Caravaggio, Bernini (beelden, Sint-Pietersplein)"],
            ])),
            ("kader", "<strong>Stromingen als reactie:</strong> de renaissance reageert op de middeleeuwen door terug "
                      "te grijpen naar de oudheid. De barok breekt de rust van de renaissance open met beweging en drama."),
        ]),
    ],
    onthoud=[
        "Romaans: rondboog, dikke muren, kleine ramen. Gotiek: spitsboog, luchtbogen, glasramen.",
        "Vlaamse primitieven: olieverf in dunne lagen, details, Van Eyck.",
        "Renaissance: perspectief, rust, humanisme. Sfumato bij Leonardo.",
        "Barok: beweging, emotie, clair-obscur. Rubens, Rembrandt, Caravaggio, Bernini.",
        "De barok was een middel van de contrareformatie.",
    ],
)

OEFENBUNDELS["oefenbundel-" + S4] = dict(
    vak=VAK, niveau=BEYOND, titel="Middeleeuwen, renaissance en barok",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Romaans of gotisch",
             opdracht="Duid aan.",
             oefeningen=[
                 ("rij", [("spitsbogen", "gotisch"), ("dikke muren, kleine ramen", "romaans"),
                          ("luchtbogen", "gotisch"), ("rondbogen", "romaans")],
                  "Romaans of gotisch?", W),
                 ("open", "Waarom konden gotische kerken grotere ramen hebben?",
                  "Luchtbogen en steunberen vangen de druk van het gewelf op aan de buitenkant. Zo hoeft de muur "
                  "niet alles te dragen.", 3),
             ]),
        dict(kop="Wie maakte het?",
             opdracht="Schrijf de kunstenaar.",
             oefeningen=[
                 ("rij", [("het Lam Gods", "Van Eyck"), ("de Mona Lisa", "Leonardo da Vinci"),
                          ("de Nachtwacht", "Rembrandt"), ("de Kruisafneming", "Rubens")],
                  "Kunstenaar?", WW),
                 ("kort", "Zachte, wazige overgangen bij Leonardo heten ...", "sfumato", W),
                 ("kort", "Het sterke contrast tussen licht en donker heet ...", "clair-obscur", WW),
             ]),
        dict(kop="Renaissance of barok",
             opdracht="Duid aan of leg uit.",
             oefeningen=[
                 ("rij", [("rust en symmetrie", "renaissance"), ("diagonale beweging", "barok"),
                          ("één verdwijnpunt", "renaissance"), ("drama en emotie", "barok")],
                  "Stroming?", WW),
                 ("waar", "Primitief betekent bij de Vlaamse primitieven ongeschoold.", False),
                 ("open", "Waarom liet de kerk in de barok zoveel indrukwekkende kunst maken?",
                  "Als antwoord op de reformatie wilde de kerk gelovigen ontroeren en de pracht van het geloof "
                  "tonen. Dat heet de contrareformatie.", 3),
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-" + S4] = dict(reeksen=[
    dict(aanpak="Kijk naar de boog: rond is romaans, spits is gotisch.",
         waarom=[None, "Noem de luchtbogen en wat ze doen."]),
    dict(aanpak="Leer elk werk samen met één kenmerk van de kunstenaar.",
         waarom=[None, "Sfumato betekent als rook.", "Caravaggio en Rembrandt gebruikten het vaak."]),
    dict(aanpak="Rust is renaissance, beweging is barok.",
         waarom=[None, "Primitief betekent hier de eersten.", None]),
])


# ═════════════════════════ 5. Van romantiek tot popart
S5 = sleutel("Van romantiek tot popart: moderne en hedendaagse kunst")
BUNDELS[S5] = dict(
    vak=VAK, niveau=BEYOND, titel="Van romantiek tot popart: moderne en hedendaagse kunst",
    onder="Van het neoclassicisme tot het postmodernisme: wat elke stroming wilde, waaraan je ze herkent, en hoe stromingen op elkaar reageren.",
    secties=[
        dict(kop="Van neoclassicisme tot impressionisme", blokken=[
            ("p", tabel(["Stroming", "Wat wilde ze?", "Herken je aan", "Namen"], [
                ["neoclassicisme", "terug naar de rust en de deugd van de oudheid", "strakke lijnen, heldere compositie, helden uit de oudheid", "Jacques-Louis David"],
                ["romantiek", "gevoel, verbeelding en de kracht van de natuur", "stormen, ruïnes, dramatisch licht, de eenzame mens", "Delacroix, Friedrich, Turner"],
                ["realisme", "het gewone leven tonen zoals het is", "arbeiders en boeren, zonder mooimakerij", "Courbet, Millet"],
                ["impressionisme", "de indruk van een moment, het wisselende licht", "losse zichtbare toetsen, buiten geschilderd, lichte kleuren", "Monet, Renoir, Degas"],
            ])),
        ]),
        dict(kop="De moderne kunst rond 1900", blokken=[
            ("p", tabel(["Stroming", "Kern", "Namen"], [
                ["postimpressionisme", "eigen weg na het impressionisme: kleur, gevoel of vaste vorm", "Van Gogh, Cézanne, Gauguin"],
                ["expressionisme", "innerlijk gevoel, felle onnatuurlijke kleuren, vervormde figuren", "Munch (De Schreeuw), Kirchner, Ensor"],
                ["fauvisme", "pure felle kleur, los van de werkelijkheid", "Matisse"],
                ["kubisme", "een voorwerp van verschillende kanten tegelijk, opgedeeld in vlakken", "Picasso, Braque"],
                ["futurisme", "snelheid, techniek en beweging", "Boccioni"],
                ["abstracte kunst", "geen herkenbare voorwerpen, enkel vorm en kleur", "Kandinsky, Mondriaan"],
            ])),
        ]),
        dict(kop="Na de Eerste Wereldoorlog en na 1945", blokken=[
            ("p", tabel(["Stroming", "Kern", "Namen"], [
                ["dadaïsme", "protest tegen de oorlog en tegen de kunst zelf; readymades", "Duchamp (Fontein)"],
                ["surrealisme", "de droom en het onbewuste, onmogelijke beelden", "Dalí, Magritte"],
                ["abstract expressionisme", "grote doeken, het schilderen zelf als daad", "Pollock (drip painting)"],
                ["popart", "beelden uit reclame, strips en massaproductie", "Warhol, Lichtenstein"],
                ["postmodernisme", "mengen, citeren en spelen met stijlen, geen enige waarheid", ""],
            ])),
            ("kader", "<strong>Stromingen als reactie.</strong> De romantiek reageert op de koele rede van het "
                      "neoclassicisme, het realisme op het dromerige van de romantiek, het impressionisme op de strakke "
                      "academie, het dadaïsme op de oorlog. Zo kan je een stroming uitleggen vanuit wat eraan voorafging."),
            ("weetje", "De fotografie maakte het minder nodig om de werkelijkheid precies na te bootsen. Mee daardoor "
                       "zochten schilders naar licht, gevoel en vorm."),
        ]),
    ],
    onthoud=[
        "Neoclassicisme: rede en oudheid. Romantiek: gevoel en natuur. Realisme: het gewone leven.",
        "Impressionisme: licht en het moment, losse toetsen.",
        "Expressionisme: gevoel, felle kleur. Kubisme: meerdere kanten tegelijk.",
        "Dada: protest en readymade. Surrealisme: droom. Popart: reclame en massacultuur.",
        "Elke stroming is ook een reactie op de vorige.",
    ],
)

OEFENBUNDELS["oefenbundel-" + S5] = dict(
    vak=VAK, niveau=BEYOND, titel="Van romantiek tot popart: moderne en hedendaagse kunst",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Herken de stroming",
             opdracht="Bij welke stroming past de beschrijving?",
             oefeningen=[
                 ("rij", [("een gezicht van voren en opzij tegelijk, in vlakken", "kubisme"),
                          ("een smeltende klok in een droomlandschap", "surrealisme"),
                          ("een zeefdruk van een soepblik", "popart"),
                          ("een haven in de ochtendnevel, losse toetsen", "impressionisme")],
                  "Stroming?", WW),
                 ("rij", [("boeren aan het werk, zonder mooimakerij", "realisme"),
                          ("een eenzame figuur bij een stormachtige zee", "romantiek"),
                          ("een urinoir als kunstwerk", "dadaïsme"),
                          ("enkel rechte lijnen en vlakken in primaire kleuren", "abstract")],
                  "Stroming?", WW),
             ]),
        dict(kop="Wie hoort waar?",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Kunstenaar", "Stroming"],
                  [["Monet", None], ["Munch", None], ["Picasso", None], ["Warhol", None]],
                  "impressionisme; expressionisme; kubisme; popart", WW),
                 ("kort", "Pollock liet verf op het doek druppelen. Dat heet ...", "drip painting", WW),
             ]),
        dict(kop="Reactie op elkaar",
             opdracht="Leg uit.",
             oefeningen=[
                 ("open", "Leg uit waarom de romantiek een reactie is op het neoclassicisme.",
                  "Het neoclassicisme zette de rede, de orde en de oudheid voorop. De romantiek stelde daar gevoel, "
                  "verbeelding en de wilde natuur tegenover.", 3),
                 ("waar", "Het dadaïsme was een protest tegen de oorlog en tegen de gevestigde kunst.", True),
                 ("kies", "Welke stroming gebruikt beelden uit reclame en strips?",
                  ["popart", "fauvisme", "futurisme", "realisme"], 0),
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-" + S5] = dict(reeksen=[
    dict(aanpak="Zoek het opvallendste kenmerk en koppel het aan één stroming: vlakken, droom, reclame, licht.",
         waarom=[None, "Mondriaan maakte abstracte werken met lijnen en primaire kleuren."]),
    dict(aanpak="Leer per stroming één naam en één werk.",
         waarom=["De Schreeuw van Munch is het bekendste expressionistische werk.", None]),
    dict(aanpak="Zet tegenover elkaar wat de vorige stroming belangrijk vond en wat de nieuwe ertegenover stelde.",
         waarom=[None, None, None]),
])


# ═════════════════════════ 6. Niet-westerse invloeden
S6 = sleutel("Niet-westerse invloeden en kunsthistorische elementen")
BUNDELS[S6] = dict(
    vak=VAK, niveau=BEYOND, titel="Niet-westerse invloeden en kunsthistorische elementen",
    onder="Hoe kunst van buiten Europa westerse kunstenaars beïnvloedde, en elementen die je door de hele kunstgeschiedenis volgt.",
    secties=[
        dict(kop="Invloeden van buiten Europa", blokken=[
            ("p", tabel(["Invloed", "Wat namen kunstenaars over?", "Bij wie?"], [
                ["Japanse houtsneden (ukiyo-e)", "vlakke kleurvlakken, sterke contouren, afgesneden beelden, ongewone standpunten", "Van Gogh, Monet, Degas (japonisme)"],
                ["Afrikaanse maskers en beelden", "vereenvoudigde, hoekige vormen en sterke uitdrukking", "Picasso (Les Demoiselles d'Avignon), het kubisme"],
                ["kunst uit Oceanië en Polynesië", "felle vlakke kleur, het verlangen naar een ongerepte wereld", "Gauguin op Tahiti"],
                ["islamitische kunst", "geometrische patronen en arabesken, geen afbeeldingen van mensen in heilige ruimtes", "Matisse, de hoefijzerboog in Spaanse gebouwen"],
            ])),
            ("kader", "<strong>Kritisch kijken.</strong> Westerse kunstenaars zagen die kunst vaak als 'primitief' en "
                      "kenden de betekenis ervan niet. Veel voorwerpen kwamen naar Europa via de koloniale overheersing. "
                      "Vandaag spreekt men over teruggave en over wie het verhaal mag vertellen."),
        ]),
        dict(kop="Kunsthistorische elementen door de tijd", blokken=[
            ("p", "Sommige elementen keren in veel periodes terug. Als je ze herkent, kan je een werk "
                  "plaatsen en vergelijken."),
            ("p", tabel(["Element", "Door de tijd"], [
                ["het menselijk lichaam", "Egyptisch stijf, Grieks ideaal, middeleeuws verborgen, renaissance anatomisch, expressionisme vervormd"],
                ["perspectief", "Egypte zonder diepte, middeleeuwen gouden achtergrond, renaissance één verdwijnpunt, kubisme meerdere standpunten"],
                ["de boog", "Romeinse rondboog, romaans, gotische spitsboog, islamitische hoefijzerboog"],
                ["de opdrachtgever", "farao, kerk, vorst en adel, rijke burgers, de kunstmarkt en musea"],
                ["het naakt en het portret", "telkens ander ideaal en andere rol"],
            ])),
        ]),
    ],
    onthoud=[
        "Japonisme: Japanse houtsneden bij Van Gogh en Monet.",
        "Afrikaanse beelden beïnvloedden Picasso en het kubisme.",
        "Gauguin trok naar Tahiti en zocht een ongerepte wereld.",
        "Veel niet-westerse voorwerpen kwamen naar Europa via kolonisatie.",
        "Volg een element door de tijd: lichaam, perspectief, boog, opdrachtgever.",
    ],
)

OEFENBUNDELS["oefenbundel-" + S6] = dict(
    vak=VAK, niveau=BEYOND, titel="Niet-westerse invloeden en kunsthistorische elementen",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Invloeden",
             opdracht="Welke invloed past erbij?",
             oefeningen=[
                 ("rij", [("Van Gogh kopieert prenten met vlakke kleuren en sterke contouren", "Japans"),
                          ("Picasso schildert hoekige, maskerachtige gezichten", "Afrikaans"),
                          ("Gauguin schildert vrouwen in felle vlakke kleuren op een eiland", "Oceanië"),
                          ("een muur vol geometrische sterpatronen", "islamitisch")],
                  "Invloed?", WW),
                 ("kort", "De westerse liefde voor Japanse kunst rond 1900 heet ...", "japonisme", WW),
                 ("open", "Waarom kijkt men vandaag kritisch naar hoe westerse kunstenaars niet-westerse kunst gebruikten?",
                  "Ze kenden de betekenis vaak niet en zagen de kunst als primitief. Veel voorwerpen kwamen naar "
                  "Europa via kolonisatie.", 3),
             ]),
        dict(kop="Elementen door de tijd",
             opdracht="Zet in de juiste volgorde of vul aan.",
             oefeningen=[
                 ("rij", [("gouden achtergrond zonder diepte", "middeleeuwen"),
                          ("één verdwijnpunt", "renaissance"),
                          ("meerdere standpunten tegelijk", "kubisme")],
                  "Perspectief: welke periode?", WW),
                 ("rij", [("rondboog", "Romeins of romaans"), ("spitsboog", "gotiek"), ("hoefijzerboog", "islamitisch")],
                  "Welke boog?", WW),
                 ("waar", "De kerk bleef tot vandaag de grootste opdrachtgever van kunst.", False),
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-" + S6] = dict(reeksen=[
    dict(aanpak="Kijk naar de vorm: vlakke kleur en contour is Japans, hoekige maskers zijn Afrikaans.",
         waarom=[None, None, "Denk aan de betekenis en aan hoe de voorwerpen in Europa kwamen."]),
    dict(aanpak="Volg één element en noem per periode het verschil.",
         waarom=[None, None, "Later werden vorsten, burgers en de kunstmarkt belangrijker."]),
])


# ═════════════════════════ 7. Kunstanalyse en kunstreflectie
S7 = sleutel("Kunstanalyse en kunstreflectie")
BUNDELS[S7] = dict(
    vak=VAK, niveau=BEYOND, titel="Kunstanalyse en kunstreflectie",
    onder="Een ongezien werk stap voor stap analyseren met richtvragen, en erover nadenken vanuit verschillende perspectieven.",
    secties=[
        dict(kop="Een werk analyseren in stappen", blokken=[
            ("p", tabel(["Stap", "Richtvraag"], [
                ["1. beschrijven", "Wat zie of hoor ik? Welk onderwerp, welke kunstvorm?"],
                ["2. vormgeving", "Welke bouwstenen, welk materiaal, welke techniek vallen op?"],
                ["3. context", "Wanneer, waar en voor wie werd het gemaakt? Wat gebeurde er toen?"],
                ["4. functie en betekenis", "Waarvoor dient het werk? Wat wil het zeggen?"],
                ["5. samenhang", "Hoe versterken vorm, inhoud en context elkaar?"],
                ["6. eigen oordeel", "Wat vind ik ervan, en waarom? Steun op wat ik zag."],
            ])),
            ("kader", "<strong>Eerst kijken, dan oordelen.</strong> Een oordeel zonder beschrijving zegt meer over jou "
                      "dan over het werk. Begin altijd bij wat je ziet."),
        ]),
        dict(kop="Factoren die een werk bepalen", blokken=[
            ("p", "Een werk ontstaat niet vanzelf. Mee bepalend zijn de <strong>kunstenaar</strong> (talent, "
                  "levensloop), de <strong>opdrachtgever</strong> en het <strong>publiek</strong>, de "
                  "<strong>beschikbare materialen en technieken</strong>, en de <strong>tijdgeest</strong>."),
        ]),
        dict(kop="Kunstreflectie: verschillende perspectieven", blokken=[
            ("p", tabel(["Perspectief", "Vraag"], [
                ["vormelijk", "Is het werk goed gemaakt, sterk gecomponeerd?"],
                ["inhoudelijk", "Wat vertelt of betekent het?"],
                ["historisch", "Wat was er nieuw of anders voor zijn tijd?"],
                ["maatschappelijk", "Wat zegt het over de samenleving, en wat doet het met ons?"],
                ["persoonlijk", "Wat roept het bij mij op?"],
            ])),
            ("p", "Vragen bij reflectie: Wat is kunst? Moet kunst mooi zijn? Wie beslist wat kunst is: de kunstenaar, "
                  "het museum, de markt of het publiek? Mag kunst choqueren?"),
        ]),
    ],
    onthoud=[
        "Analyse: beschrijven, vormgeving, context, functie, samenhang, oordeel.",
        "Eerst beschrijven, dan pas oordelen, en je oordeel steunen op wat je ziet.",
        "Factoren: kunstenaar, opdrachtgever en publiek, materialen, tijdgeest.",
        "Een werk kan je vanuit verschillende perspectieven bekijken.",
    ],
)

OEFENBUNDELS["oefenbundel-" + S7] = dict(
    vak=VAK, niveau=BEYOND, titel="Kunstanalyse en kunstreflectie",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Stappen",
             opdracht="Bij welke stap hoort de vraag?",
             oefeningen=[
                 ("rij", [("Wie betaalde het werk?", "context"), ("Welke kleuren overheersen?", "vormgeving"),
                          ("Wat stelt het voor?", "beschrijven"), ("Waarom vind ik het sterk?", "oordeel")],
                  "Stap?", WW),
                 ("waar", "Bij een analyse begin je best met je eigen oordeel.", False),
             ]),
        dict(kop="Perspectieven",
             opdracht="Welk perspectief?",
             oefeningen=[
                 ("rij", [("Het werk was het eerste met dit perspectief.", "historisch"),
                          ("Het werk doet me denken aan mijn grootvader.", "persoonlijk"),
                          ("Het werk klaagt armoede aan.", "maatschappelijk"),
                          ("De compositie is in evenwicht.", "vormelijk")],
                  "Perspectief?", WW),
             ]),
        dict(kop="Analyseer zelf",
             opdracht="Beantwoord in een paar zinnen.",
             oefeningen=[
                 ("open", "Een groot doek toont een uitgeputte arbeider die stenen kapt, in bruine en grijze tinten. "
                          "Het werd in de 19de eeuw gemaakt. Bij welke stroming past het, en welke functie heeft het?",
                  "Het past bij het realisme: het gewone, harde leven zonder mooimakerij. De functie is vooral "
                  "maatschappijkritisch: het toont de zware arbeid.", 4),
                 ("open", "Wie beslist volgens jou wat kunst is? Geef één argument.",
                  "Eigen antwoord, bv. het publiek, want kunst bestaat pas als iemand ernaar kijkt; of het museum, "
                  "want dat kiest wat getoond wordt.", 3),
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-" + S7] = dict(reeksen=[
    dict(aanpak="Wat zie ik is beschrijven, hoe is het gemaakt is vormgeving, wanneer en voor wie is context.",
         waarom=[None, "Eerst beschrijven, het oordeel komt op het einde."]),
    dict(aanpak="Vraag je af vanuit welke bril iemand kijkt: vorm, geschiedenis, samenleving of zichzelf.",
         waarom=[None]),
    dict(aanpak="Steun elke bewering op iets wat je in het werk ziet.",
         waarom=[None, "Er is geen enkel juist antwoord: het gaat om een argument."]),
])


# ═════════════════════════ 8. Zijnsleer
S8 = sleutel("Zijnsleer: schijn en werkelijkheid, worden en zijn")
BUNDELS[S8] = dict(
    vak=VAK, niveau=BEYOND, titel="Zijnsleer: schijn en werkelijkheid, worden en zijn",
    onder="Wat is echt? Van Parmenides en Heraclitus via Plato en Aristoteles tot Kant, Spinoza, Hume, Hegel, Sartre en Camus.",
    secties=[
        dict(kop="Worden of zijn?", blokken=[
            ("p", tabel(["Denker", "Standpunt"], [
                ["Heraclitus", "alles stroomt, alles is worden; je stapt nooit twee keer in dezelfde rivier"],
                ["Parmenides", "het zijn is één en onveranderlijk; verandering is schijn van de zintuigen"],
            ])),
        ]),
        dict(kop="Schijn en werkelijkheid", blokken=[
            ("p", tabel(["Denker", "Kern"], [
                ["Plato", "twee werelden: de zichtbare wereld van schaduwen en de wereld van de ideeën, die echt en eeuwig is (allegorie van de grot)"],
                ["Aristoteles", "de vorm zit in de dingen zelf; een ding is stof en vorm; verandering is van mogelijkheid naar werkelijkheid (de eikel en de eik)"],
                ["Kant", "we kennen de dingen enkel zoals ze aan ons verschijnen (fenomeen), niet het ding op zich (noumenon)"],
                ["Spinoza", "er is maar één substantie: God of de natuur; geest en lichaam zijn twee kanten ervan"],
                ["Hume", "we zien geen oorzaak, enkel gewoonte: na elkaar is nog geen door elkaar"],
                ["Hegel", "de werkelijkheid ontwikkelt zich in de geschiedenis: these, antithese, synthese"],
            ])),
            ("kader", "<strong>Plato tegenover Aristoteles:</strong> Plato zoekt het echte buiten de dingen, in de "
                      "ideeënwereld. Aristoteles zoekt het in de dingen zelf."),
        ]),
        dict(kop="Bestaan en zin: existentialisme en het absurde", blokken=[
            ("p", "<strong>Sartre</strong>: bij de mens gaat het bestaan vooraf aan de essentie. Er is geen vooraf "
                  "bepaalde natuur: de mens maakt zichzelf door zijn keuzes en is daarvoor verantwoordelijk. "
                  "<strong>Camus</strong>: de wereld geeft geen antwoord op onze vraag naar zin; dat botsen is het "
                  "absurde. Toch moeten we ons Sisyphus gelukkig voorstellen: in opstand blijven leven."),
        ]),
    ],
    onthoud=[
        "Heraclitus: alles stroomt. Parmenides: het zijn verandert niet.",
        "Plato: ideeënwereld en grot. Aristoteles: stof en vorm, mogelijkheid en werkelijkheid.",
        "Kant: fenomeen en ding op zich. Spinoza: één substantie, God of natuur.",
        "Hume: oorzaak is gewoonte. Hegel: these, antithese, synthese.",
        "Sartre: het bestaan gaat vooraf aan de essentie. Camus: het absurde en Sisyphus.",
    ],
)

OEFENBUNDELS["oefenbundel-" + S8] = dict(
    vak=VAK, niveau=BEYOND, titel="Zijnsleer: schijn en werkelijkheid, worden en zijn",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Wie zei het?",
             opdracht="Schrijf de filosoof.",
             oefeningen=[
                 ("rij", [("Je stapt nooit twee keer in dezelfde rivier.", "Heraclitus"),
                          ("De echte wereld is die van de ideeën.", "Plato"),
                          ("Het bestaan gaat vooraf aan de essentie.", "Sartre"),
                          ("Er is maar één substantie: God of de natuur.", "Spinoza")],
                  "Filosoof?", WW),
                 ("rij", [("Een eikel is in mogelijkheid een eik.", "Aristoteles"),
                          ("We kennen het ding op zich niet.", "Kant"),
                          ("Oorzaak is een gewoonte van de geest.", "Hume"),
                          ("We moeten ons Sisyphus gelukkig voorstellen.", "Camus")],
                  "Filosoof?", WW),
             ]),
        dict(kop="Begrippen",
             opdracht="Vul aan of duid aan.",
             oefeningen=[
                 ("kort", "Hegels ontwikkeling: these, antithese, ...", "synthese", W),
                 ("waar", "Parmenides vond dat verandering echt is en het zijn schijn.", False),
                 ("open", "Leg het verschil uit tussen Plato en Aristoteles over waar het echte zit.",
                  "Plato zoekt het echte in een aparte wereld van ideeën buiten de dingen. Aristoteles vindt de vorm "
                  "in de dingen zelf.", 3),
                 ("open", "Wat bedoelt Camus met het absurde?",
                  "Het botsen tussen onze vraag naar zin en een wereld die geen antwoord geeft.", 2),
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-" + S8] = dict(reeksen=[
    dict(aanpak="Koppel elke filosoof aan één beeld: de rivier, de grot, de eikel, het ding op zich, Sisyphus.",
         waarom=[None, None]),
    dict(aanpak="Lees eerst wat de filosoof vooropstelt: worden of zijn, buiten of in de dingen.",
         waarom=[None, "Bij Parmenides is het net andersom.", None, None]),
])


# ═════════════════════════ 9. Politieke filosofie 1
S9 = sleutel("Politieke filosofie: individu, gemeenschap en legitimiteit")
BUNDELS[S9] = dict(
    vak=VAK, niveau=BEYOND, titel="Politieke filosofie: individu, gemeenschap en legitimiteit",
    onder="Liberalisme, socialisme, egalitair liberalisme en communitarisme, Locke tegenover Rousseau, en wanneer macht legitiem is.",
    secties=[
        dict(kop="Vier visies op individu en gemeenschap", blokken=[
            ("p", tabel(["Visie", "Kern", "Denker"], [
                ["liberalisme", "het individu heeft natuurlijke rechten (leven, vrijheid, eigendom); de staat beschermt die en blijft beperkt", "Locke"],
                ["socialisme", "de economie verdeelt mensen in klassen; de arbeider wordt uitgebuit; gelijkheid vraagt een andere verdeling van de productiemiddelen", "Marx"],
                ["egalitair liberalisme", "vrijheid, maar ongelijkheid mag enkel als ze ook de zwaksten ten goede komt", "Rawls"],
                ["communitarisme", "de mens is geen los individu: wie je bent groeit uit een gemeenschap, haar tradities en waarden", "Sandel, Taylor, MacIntyre"],
            ])),
        ]),
        dict(kop="Locke tegenover Rousseau", blokken=[
            ("p", tabel(["", "Locke", "Rousseau"], [
                ["natuurtoestand", "mensen hebben al natuurlijke rechten", "de mens is van nature goed, de samenleving bederft hem"],
                ["sociaal contract", "de staat beschermt de rechten die we al hadden", "we geven ons over aan de algemene wil en worden zo samen vrij"],
                ["als het misloopt", "het volk mag een regering die rechten schendt afzetten", "de algemene wil is meer dan de som van de privébelangen"],
            ])),
        ]),
        dict(kop="Wanneer is macht legitiem?", blokken=[
            ("p", tabel(["Denker", "Antwoord"], [
                ["Aristoteles", "de mens is een politiek dier; een goede regering streeft het algemeen belang na, een ontaarde enkel het eigen belang"],
                ["Hobbes", "zonder staat is het leven een oorlog van allen tegen allen; we geven onze macht aan een sterke soeverein (Leviathan) voor veiligheid"],
                ["Schmitt", "soeverein is wie beslist over de uitzonderingstoestand; politiek draait om vriend en vijand"],
            ])),
            ("kader", "<strong>Legitiem</strong> is macht die mensen als terecht aanvaarden, niet enkel macht die de "
                      "sterkste heeft. Kritisch: Schmitts denken werd misbruikt om een dictatuur te rechtvaardigen."),
        ]),
    ],
    onthoud=[
        "Locke: natuurlijke rechten, beperkte staat. Marx: klassenstrijd en uitbuiting.",
        "Rawls: ongelijkheid enkel als de zwaksten erop vooruitgaan.",
        "Communitarisme: de gemeenschap vormt wie je bent.",
        "Rousseau: algemene wil. Hobbes: Leviathan voor veiligheid.",
        "Schmitt: soeverein is wie beslist over de uitzondering.",
    ],
)

OEFENBUNDELS["oefenbundel-" + S9] = dict(
    vak=VAK, niveau=BEYOND, titel="Politieke filosofie: individu, gemeenschap en legitimiteit",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Visies",
             opdracht="Welke visie past bij de uitspraak?",
             oefeningen=[
                 ("rij", [("De staat moet vooral mijn eigendom beschermen en zich verder niet moeien.", "liberalisme"),
                          ("Wie ik ben, leerde ik in mijn dorp en mijn vereniging.", "communitarisme"),
                          ("De fabriekseigenaar wordt rijk van het werk van anderen.", "socialisme"),
                          ("Een hoger loon voor artsen mag, als ook de armsten er beter van worden.", "egalitair liberalisme")],
                  "Visie?", WL),
             ]),
        dict(kop="Denkers",
             opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["Denker", "Kernbegrip"],
                  [["Hobbes", None], ["Rousseau", None], ["Schmitt", None], ["Aristoteles", None]],
                  "Leviathan of oorlog van allen tegen allen; algemene wil; uitzonderingstoestand; politiek dier of algemeen belang", WL),
                 ("waar", "Volgens Locke mag het volk een regering die de rechten schendt afzetten.", True),
                 ("waar", "Volgens Rousseau is de mens van nature slecht.", False),
             ]),
        dict(kop="Legitimiteit",
             opdracht="Leg uit.",
             oefeningen=[
                 ("open", "Wat is het verschil tussen macht en legitieme macht?",
                  "Macht is het vermogen om je wil op te leggen. Legitieme macht wordt door de mensen als terecht aanvaard.", 2),
                 ("open", "Vergelijk de natuurtoestand bij Hobbes en bij Locke.",
                  "Bij Hobbes is het een oorlog van allen tegen allen. Bij Locke hebben mensen er al natuurlijke rechten.", 3),
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-" + S9] = dict(reeksen=[
    dict(aanpak="Zoek waar de uitspraak de nadruk legt: eigen rechten, gemeenschap, klassen of eerlijke ongelijkheid.",
         waarom=[None]),
    dict(aanpak="Leer per denker één beeld of begrip.",
         waarom=[None, None, "Rousseau vond de mens van nature goed."]),
    dict(aanpak="Denk aan aanvaarding: legitiem betekent als terecht erkend.",
         waarom=[None, None]),
])


# ═════════════════════════ 10. Politieke filosofie 2
S10 = sleutel("Politieke filosofie: rechtvaardigheid, gelijkheid en vrijheid")
BUNDELS[S10] = dict(
    vak=VAK, niveau=BEYOND, titel="Politieke filosofie: rechtvaardigheid, gelijkheid en vrijheid",
    onder="Rechtvaardigheid bij Aristoteles en Rawls, individuele en culturele gelijkheid, vrijheid bij Mill, Berlin en Arendt, en de kritiek van Tronto.",
    secties=[
        dict(kop="Rechtvaardigheid", blokken=[
            ("p", tabel(["Denker", "Kern"], [
                ["Aristoteles", "gelijken gelijk behandelen, ongelijken ongelijk; verdelende rechtvaardigheid volgens verdienste en herstellende rechtvaardigheid bij schade"],
                ["sociaal contract", "rechtvaardig is wat vrije mensen samen zouden afspreken"],
                ["Rawls", "achter een sluier van onwetendheid, zonder te weten wie je wordt, kies je twee principes: gelijke basisvrijheden voor iedereen, en ongelijkheid enkel als de minstbedeelden erop vooruitgaan (verschilprincipe)"],
            ])),
        ]),
        dict(kop="Gelijkheid", blokken=[
            ("p", tabel(["Soort", "Betekenis", "Voorbeeld"], [
                ["individuele gelijkheid", "elke persoon heeft dezelfde rechten en kansen", "gelijk stemrecht, gelijk loon voor gelijk werk"],
                ["culturele gelijkheid", "groepen mogen hun eigen cultuur, taal of geloof beleven en worden gelijk erkend", "onderwijs in de eigen taal, erkenning van feestdagen"],
            ])),
            ("kader", "<strong>Spanning:</strong> wat een groep als eigen gewoonte ziet, kan soms botsen met de "
                      "rechten van een individu binnen die groep."),
        ]),
        dict(kop="Vrijheid", blokken=[
            ("p", tabel(["Denker", "Kern"], [
                ["Mill", "schadebeginsel: de staat mag je vrijheid enkel beperken om schade aan anderen te voorkomen, niet om je tegen jezelf te beschermen"],
                ["Berlin", "negatieve vrijheid = vrij van inmenging; positieve vrijheid = vrij om je eigen leven echt zelf te sturen"],
                ["Arendt", "vrijheid toont zich in samen handelen en spreken in het publieke leven; totalitarisme vernietigt die ruimte"],
            ])),
        ]),
        dict(kop="De kritiek van Tronto", blokken=[
            ("p", "<strong>Joan Tronto</strong> verwijt de klassieke politieke filosofie dat ze uitgaat van "
                  "onafhankelijke, gezonde volwassenen. Iedereen is echter afhankelijk van <strong>zorg</strong>. "
                  "Wie macht heeft, kan zorg doorschuiven naar anderen (vaak vrouwen, migranten, laagbetaalden) en "
                  "er niet over nadenken. Dat noemt ze <strong>bevoorrechte onverantwoordelijkheid</strong>. "
                  "Zorg moet daarom een politieke kwestie zijn."),
        ]),
    ],
    onthoud=[
        "Aristoteles: verdelende en herstellende rechtvaardigheid.",
        "Rawls: sluier van onwetendheid, gelijke vrijheden, verschilprincipe.",
        "Individuele gelijkheid: dezelfde rechten per persoon. Culturele: erkenning van groepen.",
        "Mill: schadebeginsel. Berlin: negatieve en positieve vrijheid. Arendt: samen handelen.",
        "Tronto: zorg is politiek; bevoorrechte onverantwoordelijkheid.",
    ],
)

OEFENBUNDELS["oefenbundel-" + S10] = dict(
    vak=VAK, niveau=BEYOND, titel="Politieke filosofie: rechtvaardigheid, gelijkheid en vrijheid",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=HOE,
    reeksen=[
        dict(kop="Rechtvaardigheid",
             opdracht="Vul aan of duid aan.",
             oefeningen=[
                 ("kort", "Bij Rawls kies je je principes achter een sluier van ...", "onwetendheid", WW),
                 ("rij", [("een schadevergoeding na een ongeval", "herstellend"),
                          ("prijzen volgens wie het best presteerde", "verdelend")],
                  "Verdelende of herstellende rechtvaardigheid?", WW),
                 ("open", "Leg het verschilprincipe van Rawls uit met een voorbeeld.",
                  "Ongelijkheid mag enkel als ook de minstbedeelden erop vooruitgaan. Bv. een hoger loon voor artsen "
                  "is aanvaardbaar als iedereen daardoor betere zorg krijgt.", 3),
             ]),
        dict(kop="Gelijkheid en vrijheid",
             opdracht="Duid aan.",
             oefeningen=[
                 ("rij", [("iedereen één stem bij verkiezingen", "individueel"),
                          ("scholen in de eigen taal van een minderheid", "cultureel")],
                  "Individuele of culturele gelijkheid?", WW),
                 ("rij", [("niemand verbiedt je te reizen", "negatief"),
                          ("je hebt genoeg geld en kennis om echt te reizen", "positief")],
                  "Negatieve of positieve vrijheid (Berlin)?", WW),
                 ("waar", "Volgens Mill mag de staat roken verbieden om rokers tegen zichzelf te beschermen.", False),
             ]),
        dict(kop="Arendt en Tronto",
             opdracht="Leg uit.",
             oefeningen=[
                 ("open", "Wat bedoelt Tronto met bevoorrechte onverantwoordelijkheid?",
                  "Wie macht heeft, schuift zorg door naar anderen en hoeft er niet over na te denken.", 2),
                 ("kies", "Waar toont vrijheid zich volgens Arendt vooral?",
                  ["in samen handelen in het publieke leven", "in zo weinig mogelijk wetten",
                   "in het innerlijk denken", "in eigendom"], 0),
             ]),
    ],
)

UITLEGBLADEN["oefenbundel-" + S10] = dict(reeksen=[
    dict(aanpak="Verdelend gaat over wie wat krijgt, herstellend over schade goedmaken.",
         waarom=[None, None, "Noem altijd wie erop vooruitgaat."]),
    dict(aanpak="Vrij van iets is negatief, vrij om iets is positief.",
         waarom=[None, None, "Mill wil enkel ingrijpen bij schade aan anderen."]),
    dict(aanpak="Bij Arendt staat het publieke samen handelen centraal, bij Tronto de zorg.",
         waarom=[None, None]),
])


# ═════════════════════════ De twaalf gedeelde filosofiethema's
import maak_filorecht as _fr
import maak_oefeningen_filorecht as _fro

GEDEELD = [
    "de-eigenheid-van-de-filosofie",
    "lichaam-en-geest-monisme-en-dualisme",
    "cultuur-en-natuur-mens-dier-en-machine",
    "vrijheid-en-determinisme-van-de-oudheid-tot-de-19de-eeuw",
    "vrijheid-en-determinisme-in-de-20ste-eeuw",
    "ethiek-basisbegrippen-en-vier-benaderingen",
    "gevolgenethiek-en-plichtethiek",
    "deugdethiek-en-zorgethiek",
    "ethiek-en-geluk",
    "bronnen-van-kennis-rationalisme-en-empirisme",
    "van-natuurfilosofie-naar-wetenschap-falsificatie-en-demarcatie",
    "argumentatieleer-redeneervormen-en-drogredenen",
]
for _s in GEDEELD:
    _k = _s + "-beyond-doorstroom"
    BUNDELS[_k] = dict(copy.deepcopy(_fr.BUNDELS[_k]), vak=VAK)
    OEFENBUNDELS["oefenbundel-" + _k] = dict(copy.deepcopy(_fro.OEFENBUNDELS["oefenbundel-" + _k]), vak=VAK)
    UITLEGBLADEN["oefenbundel-" + _k] = copy.deepcopy(_fro.UITLEGBLADEN["oefenbundel-" + _k])

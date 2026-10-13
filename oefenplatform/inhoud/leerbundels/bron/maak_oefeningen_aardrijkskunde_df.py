# -*- coding: utf-8 -*-
"""De oefenbundels van aardrijkskunde voor 🚀 Boost dubbele finaliteit.

    python3 bron/maak_oefeningen_aardrijkskunde_df.py

Tien bundels, één per thema. Ze liggen naast de leerbundels van
`maak_aardrijkskunde_df.py` en naast de fiche zelf, en ze gebruiken ándere
oefeningen dan de online vragen.

De rubrieken zijn dezelfde als bij doorstroom, dus de oefenbundels van
doorstroom liggen hier aan de basis. Wat deze fiche niet vraagt, gaat eruit:
de Human Development Index, het migratiesaldo, het demografisch transitiemodel
met zijn fasen, de hiërarchie van steden, inbreiding, stadslandbouw,
reconversie, bodemerosie en het albedo. In de plaats komen de
ontwikkelingsgraad zonder index, de bevolkingsdichtheid uit bronnen lezen, en
de scholingsgraad als sociaaleconomische factor.

Onderaan loopt dezelfde woordenscan als bij de leerbundels.
"""
import copy

import maak_aardrijkskunde_df as leerbundels
import maak_oefeningen_aardrijkskunde_boost as doorstroom
import oefenbundel

VAK = leerbundels.VAK
DF = leerbundels.DF
VERBODEN = leerbundels.VERBODEN
VOOR = "oefenbundel-"
OUD = "-boost"
NIEUW = "-boost-dubbele-finaliteit"

W, WW, WL = "120px", "185px", "250px"

ORDE = leerbundels.ORDE


def tekst_van(oef) -> str:
    stukken = []
    for d in oef[1:]:
        if isinstance(d, str):
            if d.endswith("px"):
                continue
            stukken.append(d)
        elif isinstance(d, (list, tuple)):
            for rij in d:
                if isinstance(rij, (list, tuple)):
                    stukken += [str(x) for x in rij if x is not None]
                else:
                    stukken.append(str(rij))
        elif d is not None:
            stukken.append(str(d))
    return " ".join(stukken)


# ─────────────────────────────────────────────────────────────
# De nieuwe reeksen.
# ─────────────────────────────────────────────────────────────
ONTWIKKELINGSGRAAD_OEF = dict(
    kop="De ontwikkelingsgraad",
    opdracht="Vul aan of leg uit.",
    oefeningen=[
        ("open", "Welke drie dingen bedoelt men samen met de ontwikkelingsgraad van een land?",
         "Hoe lang mensen er gemiddeld leven, hoeveel jaar ze naar school gaan, en hoeveel "
         "welvaart er is.", 3),
        ("kort", "Hoe noem je het opleidingsniveau van de mensen in een streek?",
         "de scholingsgraad", WW),
        ("waar", "Een land met veel grondstoffen heeft daarom ook een hoge ontwikkelingsgraad.",
         False),
        ("open", "Land C heeft een hoog inkomen per inwoner maar weinig scholen en ziekenhuizen. "
                 "Wat verwacht je van zijn ontwikkelingsgraad in vergelijking met een land met "
                 "hetzelfde inkomen maar goed onderwijs en goede zorg? Leg uit.",
         "Lager. De ontwikkelingsgraad gaat over gezondheid en onderwijs naast het inkomen, dus "
         "een land dat enkel op inkomen scoort, komt lager uit. Daarom zegt geld alleen te "
         "weinig.", 5),
    ],
)

BRON_OEF = dict(
    kop="Een bron kritisch bekijken",
    opdracht="Leg in volledige zinnen uit.",
    oefeningen=[
        ("open", "Je krijgt een kaart van de bevolkingsdichtheid zonder jaartal en zonder "
                 "bronvermelding. Noem drie dingen die je wil weten voor je er iets uit besluit.",
         "Van welk jaar de cijfers zijn, wie ze verzameld heeft, en welke klassen de legende "
         "gebruikt. Door de klassen anders te kiezen ziet dezelfde kaart er heel anders uit.", 4),
        ("open", "Waarom zegt de dichtheid van een heel land weinig over één bepaalde streek "
                 "erin?",
         "Het is een gemiddelde over het hele land. In veel landen wonen de mensen samengepakt in "
         "enkele streken, en dat verschil verdwijnt in dat ene cijfer.", 4),
        ("waar", "Een dunbevolkte streek is altijd een arme streek.", False),
    ],
)

VERLOOP_OEF = dict(
    kop="Wat gebeurt er met deze bevolking?",
    opdracht="Schrijf op wat er met de bevolking gebeurt, en waarom.",
    oefeningen=[
        ("tabel", ["land", "geboorte", "sterfte", "wat gebeurt er", "waarom"],
         [["land A", "41 ‰", "37 ‰", None, None],
          ["land B", "36 ‰", "10 ‰", None, None],
          ["land C", "22 ‰", "9 ‰", None, None],
          ["land D", "10 ‰", "9 ‰", None, None]],
         "A blijft ongeveer gelijk (beide hoog, de cijfers liggen dicht bij elkaar). B groeit "
         "zeer snel (de sterfte is gedaald, de geboorten blijven hoog). C groeit nog flink (de "
         "geboorten zijn aan het dalen). D blijft ongeveer gelijk, maar veroudert (beide laag).",
         "110px"),
    ],
)

STAD_OEF = dict(
    kop="Wat verandert er in de stad?",
    opdracht="Schrijf het juiste woord, of leg uit.",
    oefeningen=[
        ("rij", [("een fabriek wordt een woonblok", "functiewijziging"),
                 ("een dorp waar de laatste school sluit", "ontvolking"),
                 ("stadsbewoners verhuizen naar de rand", "stadsvlucht")],
         "Welk woord?", WL),
        ("kort", "Hoe noem je het opdelen van de open ruimte in kleine, gescheiden stukken?",
         "versnippering", WW),
        ("open", "Waarom trekt Brussel zoveel internationale bedrijven en organisaties aan?",
         "Door de Europese instellingen en de NAVO komen er diplomaten, lobbyisten en "
         "hoofdkantoren naartoe. Die banen trekken op hun beurt opnieuw mensen aan.", 4),
    ],
)

VERANDERING_OEF = dict(
    kop="Welke verandering is het?",
    opdracht="Kies uit: verstedelijking van het platteland, ontvolking, groei van de steden, "
             "veranderende mobiliteit.",
    oefeningen=[
        ("rij", [("drie nieuwe verkavelingen rond een dorpskern", "verstedelijking van het platteland"),
                 ("een dorp waar de laatste bakker sluit", "ontvolking"),
                 ("een nieuwe wijk op akkerland aan de stadsrand", "groei van de steden"),
                 ("een nieuwe fietssnelweg naar het centrum", "veranderende mobiliteit")],
         "Welke verandering?", WL),
    ],
)


# ─────────────────────────────────────────────────────────────
# De ingrepen. Dezelfde soorten als bij de leerbundels.
# ─────────────────────────────────────────────────────────────
INGREPEN = [
    ("waar-wonen-de-mensen", "vervang-reeks", "De Human Development Index", ONTWIKKELINGSGRAAD_OEF),
    ("waar-wonen-de-mensen", "vervang-reeks", "Een bron kritisch bekijken", BRON_OEF),

    ("hoe-een-bevolking-verandert", "vervang-oefening", "Migratiesaldo?", [
        ("rij", [("immigratie 40 000, emigratie 25 000", "+15 000 inwoners"),
                 ("immigratie 12 000, emigratie 31 000", "−19 000 inwoners")],
         "Hoeveel erbij of eraf?", WW),
    ]),
    ("hoe-een-bevolking-verandert", "vervang-oefening", "een migratiesaldo van +6 ‰", [
        ("open", "Een land heeft een natuurlijke aangroei van −2 ‰, en er komen per duizend "
                 "inwoners 6 meer mensen bij dan er vertrekken. Groeit of krimpt de bevolking? "
                 "Leg uit met een bewerking.",
         "De totale groei is −2 + 6 = +4 ‰, dus de bevolking groeit. Dat de natuurlijke aangroei "
         "negatief is, wordt meer dan goedgemaakt door de migratie.", 4),
    ]),
    ("hoe-een-bevolking-verandert", "vervang-reeks", "In welke fase zit dit land?", VERLOOP_OEF),

    ("stad-en-platteland", "schrap-reeks", "Economisch, cultureel of politiek?", None),
    ("stad-en-platteland", "reeks-vooraan", None, STAD_OEF),
    ("stad-en-platteland", "vervang-reeks", "Welke verandering is het?", VERANDERING_OEF),

    ("grondstoffen-energie-en-industrie", "vervang-oefening", "de Human Development Index", [
        ("rij", [("de stabiliteit van het land", "G"),
                 ("het reliëf van de streek", "F"),
                 ("de verloning van de werknemers", "S"),
                 ("de samenwerkingsverbanden met andere landen", "G"),
                 ("de grondstoffen in de bodem", "F"),
                 ("de afzetmarkt van het product", "S"),
                 ("de staatsvorm", "G"),
                 ("de scholingsgraad van de mensen", "S")],
         "G, F of S?", W),
    ]),
    ("grondstoffen-energie-en-industrie", "kop", "Industrialisatie, de-industrialisatie, reconversie",
     "Industrialisatie of de-industrialisatie?"),
    ("grondstoffen-energie-en-industrie", "vervang-oefening", "op de oude mijnsite komt een wetenschapspark", [
        ("rij", [("de mijnen sluiten en het werk verdwijnt", "de-industrialisatie"),
                 ("er komen nieuwe fabrieken bij in de streek", "industrialisatie"),
                 ("de laatste textielfabriek van de streek sluit", "de-industrialisatie")],
         "Welk begrip?", WW),
    ]),

    ("landbouw-handel-en-toerisme", "vervang-oefening", "Hoe noem je het wegspoelen van de vruchtbare bovenlaag?", [
        ("kort", "Hoe noem je het kappen van bos om er landbouwgrond van te maken?",
         "ontbossing", WW),
    ]),
    ("landbouw-handel-en-toerisme", "vervang-oefening", "een hoge Human Development Index", [
        ("rij", [("veel zonuren en een kust met stranden", "fysisch"),
                 ("een stabiele politieke situatie", "geopolitiek"),
                 ("bergen die lang sneeuw houden", "fysisch"),
                 ("hotelpersoneel met talenkennis", "sociaaleconomisch")],
         "Welke soort factor?", WL),
    ]),

    ("het-versterkte-broeikaseffect", "vervang-oefening", "Leg uit wat albedo is", [
        ("open", "Leg uit hoe de koolstofcyclus meespeelt in het versterkte broeikaseffect.",
         "Koolstof schuift tussen de geosfeer, de biosfeer, de atmosfeer en de hydrosfeer heen en "
         "weer. Verbranden we fossiele brandstoffen of kappen we bos, dan verhuist koolstof die "
         "lang opgeslagen lag naar de lucht. Hoe meer koolstofdioxide in de atmosfeer, hoe meer "
         "warmte er wordt vastgehouden.", 6),
    ]),
]


def pas_toe(bundels: dict):
    for kort, soort, waar, inhoud in INGREPEN:
        if kort not in bundels:
            raise SystemExit(f"Onbekende bundel in INGREPEN: {kort}")
        reeksen = bundels[kort]["reeksen"]
        if soort == "kop":
            raak = [r for r in reeksen if r["kop"] == waar]
            if len(raak) != 1:
                raise SystemExit(f"{kort}: {len(raak)} reeksen heten {waar!r}, verwacht 1")
            raak[0]["kop"] = inhoud
        elif soort == "schrap-reeks":
            raak = [i for i, r in enumerate(reeksen) if r["kop"] == waar]
            if len(raak) != 1:
                raise SystemExit(f"{kort}: {len(raak)} reeksen heten {waar!r}, verwacht 1")
            reeksen.pop(raak[0])
        elif soort == "vervang-reeks":
            raak = [i for i, r in enumerate(reeksen) if r["kop"] == waar]
            if len(raak) != 1:
                raise SystemExit(f"{kort}: {len(raak)} reeksen heten {waar!r}, verwacht 1")
            reeksen[raak[0]] = copy.deepcopy(inhoud)
        elif soort == "reeks-vooraan":
            reeksen.insert(0, copy.deepcopy(inhoud))
        elif soort == "reeks-achteraan":
            reeksen.append(copy.deepcopy(inhoud))
        elif soort == "vervang-oefening":
            raak = [
                (i, j)
                for i, r in enumerate(reeksen)
                for j, o in enumerate(r["oefeningen"])
                if waar in tekst_van(o)
            ]
            if len(raak) != 1:
                raise SystemExit(f"{kort}: {len(raak)} oefeningen met {waar!r}, verwacht 1")
            i, j = raak[0]
            reeksen[i]["oefeningen"][j:j + 1] = list(inhoud)
        else:
            raise SystemExit(f"Onbekende ingreep: {soort}")


def bouw() -> dict:
    uit = {}
    for kort in ORDE:
        sleutel = VOOR + kort + OUD
        if sleutel not in doorstroom.OEFENBUNDELS:
            raise SystemExit(f"Onbekende doorstroombundel: {sleutel}")
        b = copy.deepcopy(doorstroom.OEFENBUNDELS[sleutel])
        b["niveau"] = DF
        uit[kort] = b
    pas_toe(uit)

    for kort, b in uit.items():
        alles = " ".join(
            [b["titel"], b.get("onder", "")]
            + [r["kop"] for r in b["reeksen"]]
            + [r.get("opdracht", "") for r in b["reeksen"]]
            + [tekst_van(o) for r in b["reeksen"] for o in r["oefeningen"]]
        ).lower()
        for woord in VERBODEN:
            if woord in alles:
                raise SystemExit(f"{kort} gebruikt nog {woord!r}, dat staat niet op deze fiche")
        aantal = sum(len(r["oefeningen"]) for r in b["reeksen"])
        if aantal < 10:
            raise SystemExit(f"{kort} heeft maar {aantal} oefeningen")

    return {VOOR + kort + NIEUW: uit[kort] for kort in ORDE}


OEFENBUNDELS = bouw()

if __name__ == "__main__":
    for sleutel, b in OEFENBUNDELS.items():
        oefenbundel.schrijf(b, sleutel)
        print(" ", sleutel)

# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-waar-ligt-het-en-hoe-weet-je-dat-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Hou twee soorten lijnen uit elkaar. Breedtecirkels lopen horizontaal en evenwijdig met de evenaar; meridianen lopen van pool tot pool. Breedte zegt hoe ver je van de evenaar bent, lengte hoe ver van Greenwich.",
            waarom=[
                "Onthoud de vier getallen: 0° is de evenaar, 23,5° zijn de keerkringen en 66,5° de poolcirkels. Die graden zijn geen toeval: 23,5° is precies de scheefstand van de aardas, en daarom liggen de keerkringen juist daar.",
                "De Kreeftskeerkring ligt in het noorden, de Steenbokskeerkring in het zuiden. Een steuntje: de steenbok klimt naar beneden, naar het zuiden. En de datumlijn ligt rond 180°, aan de andere kant van de nulmeridiaan, met bochten om eilandengroepen niet te doorsnijden.",
            ],
        ),
        dict(
            aanpak="Absoluut situeren doe je met coördinaten: graden noorder- of zuiderbreedte en ooster- of westerlengte. Relatief situeren doe je ten opzichte van iets anders: een rivier, een stad, een gebergte.",
            waarom=[
                None,
                "Aan het Albertkanaal en ten noorden van Hasselt zijn allebei verwijzingen naar iets anders. Dat maakt het relatief, hoe precies het ook klinkt.",
                None,
                "Graden breedte en lengte, dus absoluut. Let op de letters: ZB is zuiderbreedte, OL is oosterlengte. Vergeet die nooit, want zonder de letters wijst 12° 47° naar vier verschillende plaatsen op aarde.",
            ],
        ),
        dict(
            aanpak="Fysischgeografisch gaat over de natuur: reliëf, water, klimaat, plantengroei. Sociaaleconomisch gaat over mensen: bevolking, taal, economie, politiek. Vraag je af of het er ook zonder mensen zou zijn.",
            waarom=[
                "De test die altijd werkt: zou dit er ook zijn als er geen mensen waren? De Rijn, de Alpen en de klimaatzones wel, dus F. De Europese Unie, analfabetisme en talen niet, dus S.",
            ],
        ),
        dict(
            aanpak="Drie soorten afstand: de werkelijke in kilometers, de ervaren in hoe lang of hoe zwaar het voelt, en de mentale in hoe ver je denkt dat iets ligt.",
            waarom=[
                "De mentale afstand zit in je hoofd en klopt vaak niet. Marokko ligt dichter bij ons dan Turkije, maar velen denken het omgekeerde, want Turkije voelt Europeser.",
                "Er is geen juist antwoord, maar je uitleg moet wel naar een oorzaak wijzen: comfort, drukte, het weer of hoe goed je de weg kent. Een weg die je kent, voelt korter dan dezelfde weg de eerste keer.",
            ],
        ),
        dict(
            aanpak="Een kaart is geen foto van de aarde maar een gemaakt beeld. Elke kaart maakt keuzes, en elke platte wereldkaart vervormt. De vraag is niet óf ze vervormt maar wát ze vervormt.",
            waarom=[
                "Dat het noorden boven staat, is een afspraak uit de Europese kaartentraditie, geen natuurwet. In de ruimte is er geen boven. Zo'n kaart voelt vreemd omdat ze tegen je mentale kaart ingaat.",
                "Je kan een bol niet plat maken zonder iets op te offeren. De bekendste wereldkaart houdt de hoeken kloppend, wat handig is om te varen, en rekt daarvoor alles bij de polen uit. Groenland lijkt daardoor zo groot als Afrika, terwijl Afrika er in werkelijkheid ongeveer veertien keer in past.",
                "Die bestaat niet, en dat is wiskundig bewezen. Elke projectie moet kiezen wat ze juist houdt: de vormen, de oppervlakten of de afstanden. Daarom kies je een kaart bij je vraag.",
                "Een kaart met Europa in het midden en een kaart met de Stille Oceaan in het midden zijn allebei juist. Die keuze bepaalt mee hoe je de wereld ziet, en dat is zelf het bestuderen waard.",
            ],
        ),
        dict(
            aanpak="Bij elke aardrijkskundige vraag hoort een eigen soort kaart of grafiek. Vraag je af wat je wil weten, en kies dan pas je bron.",
            waarom=[
                "Koppel de vraag aan de bron: klimaat vraagt een klimaatkaart of een klimatogram, hoogte en landvorm vragen een reliëfkaart, plantengroei vraagt een vegetatiekaart. Op een examen scheelt die keuze veel tijd.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-waar-wonen-de-mensen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Bevolkingsdichtheid is inwoners gedeeld door oppervlakte, en de eenheid is inwoners per vierkante kilometer. Schrijf altijd de bewerking op en zet de eenheid erbij: daar staan punten op.",
            waarom=[
                "Deel de nullen eerst weg, dan reken je sneller. 6 000 000 : 20 000 is hetzelfde als 6 000 : 20, dus 300. En 250 000 : 500 is 2 500 : 5, dus 500.",
                "Dit is de kern van het hoofdstuk: veel inwoners betekent niet dicht bevolkt. Land A heeft zeven keer meer inwoners en toch veertig keer minder dichtheid, want het is driehonderd keer zo groot. Reken altijd, schat nooit.",
            ],
        ),
        dict(
            aanpak="Waar mensen wonen, hangt vooral af van drie dingen: water en klimaat, de vruchtbaarheid van de bodem, en het reliëf. Te droog, te koud, te steil of te arm betekent bijna altijd dun bevolkt.",
            waarom=[
                "Zie het patroon: dun bevolkt waar een van de drie tegenzit (te droog in de Sahara, te koud in Noord-Canada, te steil in het hooggebergte), dicht bevolkt waar water én vruchtbare grond samenkomen (de Nijl, de Ganges-delta). Rivierdelta's zijn daarom al duizenden jaren de dichtstbevolkte plekken van de aarde.",
            ],
        ),
        dict(
            aanpak="Een dichtheid is een gemiddelde, en een gemiddelde verbergt altijd iets. Vraag je bij elk cijfer af wat het níét laat zien.",
            waarom=[
                "Dit is de belangrijkste beperking van het cijfer: het zegt niets over het patroon. Dezelfde 300 inwoners per km² kan een compact dorp zijn of lintbebouwing over tien kilometer, en dat scheelt wegen, riolering en autokilometers.",
                "Zie de vergelijking in oefening 2. Een land met veel inwoners op een heel groot oppervlak is dun bevolkt.",
                "Dichtheid zegt niets over welvaart. Bangladesh is heel dicht bevolkt en arm, Monaco is heel dicht bevolkt en rijk, Australië is dun bevolkt en rijk.",
            ],
        ),
        dict(
            aanpak="De ontwikkelingsgraad meet drie dingen samen: hoe lang mensen leven, hoeveel ze naar school gaan, en hoeveel welvaart er is. Geld alleen volstaat dus niet.",
            waarom=[
                "Noem alle drie: gezondheid, onderwijs en welvaart. Dat is precies waarom er een aparte maat voor bestaat naast het inkomen.",
                "De scholingsgraad is het opleidingsniveau van de bevolking. Verwar het niet met de alfabetiseringsgraad, dat is het aandeel mensen dat kan lezen en schrijven.",
                "Grondstoffen zijn geen ontwikkeling. Er zijn landen vol olie of mineralen waar de bevolking er weinig van merkt, omdat de opbrengst bij een kleine groep of in het buitenland terechtkomt.",
                "De uitleg moet naar de drie onderdelen verwijzen: wie alleen op inkomen scoort en niet op gezondheid en onderwijs, komt lager uit. Dat is net waarom men niet met het inkomen alleen werkt.",
            ],
        ),
        dict(
            aanpak="Een kaart of een cijfer kritisch bekijken gaat altijd over dezelfde drie dingen: van wanneer is het, wie maakte het, en hoe is het ingedeeld?",
            waarom=[
                "De derde is de minst voor de hand liggende en de belangrijkste: de klassen van de legende. Door de grenzen van de klassen anders te leggen, kan dezelfde dataset een heel ander beeld geven. Daar wordt in de praktijk ook mee gestuurd.",
                "Dit is dezelfde les als in oefening 4, maar een schaalniveau hoger: een landgemiddelde verbergt de verschillen binnen het land. In Egypte woont bijna iedereen langs de Nijl, en het landgemiddelde zegt daar niets over.",
                "Dun bevolkt zegt niets over arm of rijk. IJsland, Canada en Australië zijn dun bevolkt en welvarend.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-hoe-een-bevolking-verandert-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een bevolking verandert langs twee wegen: geboorte min sterfte (de natuurlijke aangroei) en inwijking min uitwijking (het migratiesaldo). De twee samen geven de totale groei.",
            waarom=[
                "Het promille-teken ‰ betekent per duizend inwoners, niet per honderd. Trek gewoon af en hou het teken: 9 min 12 is min 3, dus de bevolking krimpt op eigen kracht.",
                "Hier gaat het om echte aantallen, niet om promille. Immigratie min emigratie, en een min mag.",
                "Dit is het patroon van veel West-Europese landen vandaag: de natuurlijke aangroei is negatief, en toch groeit de bevolking door migratie. Tel de twee saldi gewoon op: min 2 plus 6 is plus 4.",
            ],
        ),
        dict(
            aanpak="Een bevolkingshistogram lees je van onder naar boven: onderaan de jongsten, bovenaan de oudsten. De vorm vertelt het verhaal van de laatste tachtig jaar.",
            waarom=[
                "Drie vormen, drie verhalen. Een piramide betekent veel geboorten en een jonge bevolking. Een urn betekent weinig geboorten en een oude bevolking. Een klok betekent dat het geboortecijfer al jaren stabiel is.",
                "Een deuk in een histogram is altijd een gebeurtenis uit het verleden. Reken terug: wie nu 75 tot 80 is, werd rond 1945 tot 1950 geboren. Zo'n deuk schuift elk jaar één balkje omhoog.",
                "Migranten zijn meestal jongvolwassenen, want men trekt weg voor werk of studie. Daarom zie je bij veel immigratie bredere balken tussen twintig en veertig, en vaak ook meer mannen dan vrouwen in die groep.",
            ],
        ),
        dict(
            aanpak="Vergelijk telkens geboortecijfer en sterftecijfer met elkaar. Liggen ze dicht bij elkaar, dan verandert er weinig. Ligt de geboorte veel hoger, dan groeit de bevolking snel.",
            waarom=[
                "Dit is het demografische transitiemodel in vier stappen. De snelste groei komt niet doordat er meer kinderen geboren worden, maar doordat de sterfte daalt terwijl de geboorten nog hoog blijven. Dat is het inzicht dat deze vraag test.",
            ],
        ),
        dict(
            aanpak="Pushfactoren duwen je weg uit je eigen streek, pullfactoren trekken je naar een andere. Vraag je telkens af waar de factor zich afspeelt: hier of daar.",
            waarom=[
                "Zie het patroon: push gaat over wat er misloopt waar je woont (droogte, oorlog, werkloosheid), pull over wat er elders lonkt (familie, onderwijs, werk). Vaak werken ze als een paar: werkloosheid hier en werk daar.",
                "Dit is een belangrijke correctie op een hardnekkig beeld. Verreweg de meeste mensen die vluchten, blijven in de eigen regio, omdat een verre reis geld, papieren en netwerken vraagt die ze net niet hebben.",
            ],
        ),
        dict(
            aanpak="Drie begrippen die bij elkaar horen: vergrijzing, braindrain en braingain. Leer bij elk niet alleen de betekenis maar ook de gevolgen.",
            waarom=[
                "Braindrain is letterlijk het wegvloeien van hersenen. Het land dat voor de opleiding betaalde, plukt er de vruchten niet van.",
                None,
                "Noem er drie, en let op het laatste stuk: scholen komen juist leeg te staan. Vergrijzing verandert niet alleen de uitgaven maar ook waaraan het geld besteed wordt.",
                "Voor het land van vertrek is het vooral een nadeel: het verliest artsen, verpleegkundigen en ingenieurs die het zelf opleidde. Er is één tegengewicht, namelijk het geld dat migranten naar huis sturen, maar dat weegt het verlies meestal niet op.",
                "Vergrijzing betekent dat het aandeel ouderen stijgt, niet dat het aantal inwoners daalt. Een land kan tegelijk vergrijzen en groeien, bijvoorbeeld door migratie.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-stad-en-platteland-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De woorden van dit hoofdstuk lijken op elkaar. Hou vast waar de beweging naartoe gaat: stadsvlucht is vanuit de stad naar buiten, verstedelijking is vanuit de stad naar het platteland toe, ontvolking is wegtrekken zonder dat er iemand bijkomt.",
            waarom=[
                "Een functiewijziging is hetzelfde gebouw met een andere bestemming, en dat is vandaag heel gewoon: een fabriek wordt een woonblok, een kerk een bibliotheek, een schoolgebouw een woonzorgcentrum.",
                "Versnippering betekent dat de open ruimte in losse stukken valt, door wegen, verkavelingen en bedrijventerreinen. Het gevolg: dieren kunnen zich niet meer verplaatsen en een landbouwer moet van perceel naar perceel rijden.",
                "Let op de tweede zin: de banen trekken opnieuw mensen aan. Dat heet een zelfversterkend effect, en het verklaart waarom grote steden blijven groeien.",
            ],
        ),
        dict(
            aanpak="Vier veranderingen, elk met een eigen plaats. Vraag je af wáár het gebeurt: op het platteland, aan de stadsrand, of in de verbinding tussen de twee.",
            waarom=[
                "Let op het verschil tussen de eerste en de derde. Verkavelingen rond een dorpskern maken het platteland stedelijker; een nieuwe wijk op akkerland aan de stadsrand is de stad die uitbreidt. De plaats beslist, niet het soort huizen.",
            ],
        ),
        dict(
            aanpak="Multiculturaliteit en segregatie worden vaak door elkaar gehaald. De eerste gaat over wie er woont, de tweede over hoe ze verdeeld wonen.",
            waarom=[
                "De kernzin is de laatste: een stad kan heel divers zijn en tegelijk sterk gescheiden. Diversiteit op papier betekent niet dat mensen elkaar tegenkomen.",
                "Dit is het antwoord dat punten haalt: de woningprijs. Segregatie ontstaat in West-Europa zelden door een regel, maar door wat mensen kunnen betalen. Zo ontstaat scheiding zonder dat iemand ze oplegt, en net daarom is ze moeilijk te doorbreken.",
            ],
        ),
        dict(
            aanpak="Verharding is beton en asfalt in plaats van grond. Twee gevolgen moet je kunnen uitleggen: het wordt warmer, en het water kan niet weg.",
            waarom=[
                "Noem twee problemen én leg bij elk uit hoe het werkt, want daar staan de punten op. Bomen koelen op twee manieren: schaduw, en verdamping van water langs hun bladeren. En onverharde grond laat regen insijpelen in plaats van naar de riool te sturen.",
                "Het hitte-eilandeffect kan in een stadskern vijf tot acht graden schelen met het platteland eromheen, vooral 's nachts, want beton geeft overdag opgeslagen warmte weer af.",
                "Zelfde woord als in oefening 2. Versnippering komt in dit vak zo vaak terug dat het de moeite is om het echt vast te zetten.",
                "Verstedelijking is meer dan meer inwoners: het is ook de stedelijke manier van leven en bouwen die zich over het platteland verspreidt. Een dorp met verkavelingen, een winkelcentrum en pendelaars is verstedelijkt, ook zonder dat de stad groeide.",
            ],
        ),
        dict(
            aanpak="Twee beelden van dezelfde plaats op twee momenten is de beste bron voor ruimtelijke verandering. Let bij het vergelijken altijd op de voorwaarden: zelfde schaal, zelfde seizoen.",
            waarom=[
                "De tweede helft is het echte antwoord. Een foto in de zomer en een in de winter geven een ander beeld van hetzelfde landschap, en een andere schaal maakt elke vergelijking waardeloos.",
                "Een woondorp is een dorp dat alleen nog woonfunctie heeft. Noem ook het gevolg: alles wat je nodig hebt ligt elders, dus de autoafhankelijkheid en het pendelverkeer nemen toe. Precies dat is het probleem van veel Vlaamse dorpen.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-grondstoffen-energie-en-industrie-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Twee paren naast elkaar. Groeve tegenover mijn gaat over diep of ondiep; traditioneel tegenover modern gaat over handen of machines. Die twee paren staan los van elkaar.",
            waarom=[
                "Dagbouw is een groeve in open lucht; een mijn werkt met schachten en gangen. En let erop dat een moderne ontginning ook een groeve kan zijn: de twee paren kruisen elkaar.",
                "Noem twee voordelen én het nadeel, want de vraag vraagt allebei. Goedkoper en veiliger tegenover een landschap dat verdwijnt: dat is de afweging die bij elke ontginning gemaakt wordt.",
            ],
        ),
        dict(
            aanpak="Hernieuwbaar betekent dat de bron zichzelf aanvult binnen een menselijke tijdspanne. Vraag je af: is dit over honderd jaar nog altijd aanwezig?",
            waarom=[
                "Wind, water en zon vullen zichzelf aan. Steenkool, aardgas en uranium moeten ontgonnen worden en raken op. Let op: biomassa staat hier niet bij, en die is hernieuwbaar zolang er niet meer gekapt wordt dan er bij groeit.",
                "Dit is de kern van de vraag: hernieuwbaar gaat over de bron, niet over de uitstoot. Kernenergie is koolstofarm maar niet hernieuwbaar. Twee verschillende eigenschappen dus, en ze worden voortdurend door elkaar gehaald.",
            ],
        ),
        dict(
            aanpak="Waar iets komt te staan, hangt af van wat het nodig heeft. Vraag je bij elke installatie af welke natuurlijke voorwaarde of welke aanvoer bepalend is.",
            waarom=[
                "Zie het patroon: energie uit de natuur volgt de natuur (wind op zee, zon waar veel zonuren zijn, water waar hoogteverschil is), en industrie volgt de aanvoer (een haven voor wie grondstoffen per schip binnenkrijgt). Dat onderscheid is het hele antwoord.",
            ],
        ),
        dict(
            aanpak="Drie soorten factoren. Geopolitiek gaat over de staat en zijn verhoudingen, fysisch over de natuur, sociaaleconomisch over mensen en markt.",
            waarom=[
                "De test: zou dit er zonder mensen zijn (fysisch), gaat het over de staat en haar betrekkingen (geopolitiek), of over mensen en markt (sociaaleconomisch)? Stabiliteit, bondgenootschappen en de staatsvorm zijn geopolitiek; reliëf en bodemrijkdom zijn fysisch; lonen, afzetmarkt en scholing zijn sociaaleconomisch.",
            ],
        ),
        dict(
            aanpak="Industrialisatie is fabrieken erbij, de-industrialisatie is fabrieken weg. Let bij de gevolgen op dat je er drie noemt en dat ze echt verschillen van elkaar.",
            waarom=[
                "Het voorvoegsel de betekent terug of weg. Limburg na de mijnsluitingen en de textielstreken van Noord-Frankrijk zijn de schoolvoorbeelden van de-industrialisatie bij ons.",
                "Noem er drie uit verschillende hoeken: werkloosheid (economisch), wegtrekkende jongeren (sociaal en demografisch) en een leeg terrein (ruimtelijk). Zo'n verlaten industrieterrein heet een brownfield, en het opnieuw gebruiken ervan spaart open ruimte.",
                "Noem het voordeel én het nadeel, want de vraag vraagt allebei. Goedkope grond en vlotte ontsluiting tegenover werk dat uit de kernen verdwijnt en open ruimte die versnippert.",
                "Dit heet de grondstoffenval: landen met veel grondstoffen presteren economisch vaak slechter dan verwacht, doordat de opbrengst bij een kleine groep terechtkomt en de rest van de economie niet ontwikkelt. Zie ook de vraag over de ontwikkelingsgraad.",
            ],
        ),
    ]
)

UITLEGBLADEN["oefenbundel-landbouw-handel-en-toerisme-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een gewas groeit waar het klimaat past. Denk bij elk gewas aan twee dingen: hoeveel warmte heeft het nodig, en wanneer heeft het water nodig?",
            waarom=[
                "Zie hoe elk gewas zijn klimaat verraadt. Rijst vraagt warmte én veel water in het groeiseizoen, dus de moessongebieden. Olijven vragen juist een dróge zomer, en dat is precies het mediterrane klimaat. En koffie groeit in de tropen, maar in de hooglanden, want in het hete laagland is het te warm.",
                "Zwarte aarde of tsjernozjom is een van de vruchtbaarste bodems ter wereld, rijk aan humus. Noem ook het vlakke reliëf: dat maakt machinale bewerking op grote schaal mogelijk.",
            ],
        ),
        dict(
            aanpak="Intensief betekent veel inzet per hectare: veel arbeid, veel kapitaal of allebei. Extensief betekent veel grond en weinig inzet per hectare. Kijk dus naar de verhouding, niet naar de totale opbrengst.",
            waarom=[
                "Let op dat intensief twee gedaantes heeft: intensief met arbeid (rijstterrassen met de hand) en intensief met kapitaal (verwarmde serres). Allebei intensief, maar met een heel andere inzet.",
                "Dit is een van de nuttigste onderscheiden van het hele vak. Per hectare haalt handwerk vaak het meest; per werkende haalt de machine het ruim. Welk cijfer je kiest, bepaalt welke landbouw er productief uitziet, en dus hoe een kaart of een grafiek eruitziet.",
            ],
        ),
        dict(
            aanpak="Duurzaam betekent dat je de grond zo gebruikt dat je er over twintig jaar nog van kan leven. Vraag je bij elke praktijk af wat ze met de bodem en met het water doet.",
            waarom=[
                "De rode draad: alles wat de bodem bedekt en vasthoudt is duurzaam, alles wat hem blootlegt of uitput niet. De derde is de minst bekende: ploegen in de richting van de helling maakt geultjes waarlangs de regen de bovenlaag meeneemt. Ploeg dwars op de helling, dan houden de voren het water tegen.",
                "Ontbossing gebeurt vandaag vooral voor landbouw: soja, palmolie en veeteelt. Het kost niet alleen bos maar ook bodem, want tropische grond is zonder bos snel uitgeput.",
                "Schaalvergroting betekent minder bedrijven die elk groter worden. Het maakt de landbouw efficiënter per werkende, maar het doet ook kleine bedrijven en hagen en houtkanten verdwijnen.",
            ],
        ),
        dict(
            aanpak="Groothandel levert aan winkels, kleinhandel aan de consument, en de dienstensector is alles wat geen goederen maakt. Die drie samen vormen het grootste deel van onze economie.",
            waarom=[
                "De dienstensector is bij ons goed voor ongeveer driekwart van de werkgelegenheid. Onderwijs, zorg, transport, toerisme, bank en overheid horen er allemaal bij.",
                "Twee redenen: oppervlakte en bereikbaarheid. En let op de tweede zin, want dat is het ruimtelijke gevolg: online winkelen verplaatst werk van de winkelstraat naar een loods langs de snelweg.",
            ],
        ),
        dict(
            aanpak="Waarom er toerisme is, en wat het aanricht, zijn twee verschillende vragen. Voor de eerste gebruik je dezelfde drie soorten factoren als bij industrie: fysisch, geopolitiek en sociaaleconomisch.",
            waarom=[
                "Zon, kust en sneeuw zijn natuur, dus fysisch. Stabiliteit is geopolitiek: een onveilig land krijgt geen toeristen, hoe mooi het ook is. En personeel met talenkennis is sociaaleconomisch.",
                "Noem er drie, en zorg dat ze echt ruimtelijk zijn: bebouwing die open ruimte opslorpt, druk op het drinkwater, en woningen die voor de eigen bewoners onbetaalbaar worden. Dat laatste is in de Vlaamse kustgemeenten een reëel probleem.",
                "Het antwoord is eenzijdigheid. Een streek die op één sector steunt, verliest bij een crisis alles tegelijk, en toerisme is daarbij extra gevoelig: het is het eerste waarop mensen besparen.",
                "Stadstoerisme draait op erfgoed, musea, evenementen en gastronomie. Brugge, Praag en Firenze liggen geen van drie aan zee.",
            ],
        ),
    ]
)


UITLEGBLADEN["oefenbundel-mondialisering-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een productieketen loopt van de grondstof tot in de winkel. Zoek eerst waar het materiaal uit de grond komt, dan wat er met dat materiaal gebeurt, dan waar het toestel in elkaar gaat, dan het vervoer, en pas als laatste de verkoop.",
            waarom=[
                "De orde volgt het materiaal: eerst ertsen uit de grond, dan die ertsen tot metaal verwerken, dan de onderdelen samenvoegen, dan het vervoer en als laatste de winkel. Het vervoer staat niet vooraan: pas als er een toestel is, valt er iets te verschepen.",
                None,
            ],
        ),
        dict(
            aanpak="Vier stromen gaan de wereld rond: goederen (spullen), kapitaal (geld), mensen en informatie. Vraag je bij elk voorbeeld af wat er eigenlijk beweegt.",
            waarom=[
                "Geld dat migranten naar huis sturen is kapitaal, ook al zijn de mensen zelf eerder verhuisd: wat nu over de grens gaat, is geld. En toeristen zijn een stroom van mensen, ook al blijven ze maar twee weken.",
                "Remittances zijn voor een land als de Filipijnen of Marokko een grotere inkomstenbron dan de ontwikkelingshulp die het krijgt.",
            ],
        ),
        dict(
            aanpak="Een gevolg van mondialisering is zelden alleen goed of alleen slecht. Zeg dus altijd voor wie het een voordeel is en voor wie niet, want dezelfde verandering valt voor een koper anders uit dan voor een producent.",
            waarom=[
                "Let op de derde rij: een wereldwijde besmetting of een haperende aanvoerketen heeft voor niemand een voordeel. Niet elke rij heeft dus twee kanten; dat is geen fout in de oefening.",
            ],
        ),
        dict(
            aanpak="Vraag je af of de mens iets met dat verschijnsel te maken heeft. Reliëf, seizoenen en klimaat zijn natuurlijke gegevens; winkelketens, aanvoerlijnen en callcenters zijn door mensen en handel gemaakt.",
            waarom=[
                "Aardbeien in de winter is een gevolg van mondialisering: ze komen uit Spanje, Marokko of Egypte, waar het seizoen anders loopt. De seizoenen zelf zijn natuurlijk, dus N.",
                "De winst van de wereldhandel ligt heel ongelijk verdeeld. Sommige landen leveren enkel grondstoffen tegen een lage prijs, en de winst op het eindproduct blijft elders.",
                "Zijderoute, specerijenhandel en de scheepvaart waren vroege vormen. Wat nieuw is, is de snelheid en de omvang: een container en een zeekabel doen in dagen wat vroeger maanden kostte.",
            ],
        ),
        dict(
            aanpak="Invloed is niet hetzelfde als macht. Een bedrijf mag geen wetten maken, maar het beslist wel waar het bouwt en waar het sluit, en daar hangen veel gezinnen van af.",
            waarom=[
                "Het gaat om afhankelijkheid, niet om personeelsaantallen of om wetten. Wie beslist over duizenden jobs, weegt zwaar op een streek, ook zonder enige bevoegdheid.",
                "De sterkste hefboom is samenwerken: één gemeente of één klein land staat alleen, een groep landen die dezelfde regels afspreekt niet.",
            ],
        ),
    ]
)


UITLEGBLADEN["oefenbundel-duurzaam-omgaan-met-de-ruimte-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De drie p's: people gaat over de mensen (werk, loon, gezondheid, meespreken), planet over de natuur (water, bodem, lucht, leven) en profit over het geld (rendabel blijven). Zoek bij elk voorbeeld wie of wat er beter van wordt.",
            waarom=[
                "De buurt horen bij een plan is people: het gaat over mensen die meespreken. Een bodem die water doorlaat is planet, want dat raakt het grondwater en de natuur, niet rechtstreeks een persoon.",
                None,
            ],
        ),
        dict(
            aanpak="Verharding betekent dat regen niet meer in de bodem kan. Volg het water: waar gaat het heen als de grond het niet opneemt, en wat gebeurt er met het water dat er dan niet meer in zit?",
            waarom=[
                "Verharding doet twee tegengestelde dingen tegelijk: te veel water op het verkeerde moment (wateroverlast na een bui) en te weinig water op het verkeerde moment (een lagere grondwatertafel in de zomer).",
                "Steen en asfalt nemen de warmte van de dag op en geven ze 's nachts weer af, en er is weinig groen dat verkoelt. Een stad koelt daardoor 's nachts minder af dan het platteland eromheen.",
                "Versnippering is meer dan ruimteverlies: een dier dat niet van het ene stuk natuur naar het andere kan, zit in een eiland dat te klein is om in te overleven.",
            ],
        ),
        dict(
            aanpak="Bij een ruimtelijk conflict zet je eerst alle betrokkenen op een rij en pas daarna je eigen mening. Vraag bij elke partij: wat verliest ze, en wat wint ze? Dan zie je waar een compromis mogelijk is.",
            waarom=[
                "Het gemeentebestuur staat bewust als verdeeld in het antwoord: het moet werk en inkomsten afwegen tegen open ruimte en tegen inwoners die ook kiezers zijn. Een bestuur dat enkel ja of enkel nee zegt, negeert de ene of de andere kant.",
                "Een goede aanpassing verlegt het probleem niet. Een bufferstrook en waterdoorlatende parking laten het bedrijf bouwen én houden water en groen gedeeltelijk overeind; het afval of de vervuiling elders dumpen lost niets op.",
            ],
        ),
        dict(
            aanpak="Vraag je af of het probleem echt kleiner wordt, of enkel ergens anders terechtkomt. Verschuiven voelt als een oplossing omdat je het hier niet meer ziet, maar de vervuiling of het afval bestaat nog.",
            waarom=[
                "Afval verschepen en een fabriek naar lossere regels verhuizen hebben hetzelfde probleem: de uitstoot en het afval blijven bestaan, maar bij iemand anders, vaak in een land dat zich minder kan verweren.",
                "Duurzaam gaat over hoe je verandert, niet over niets veranderen. Een landschap bevriezen kan zelfs tegen de drie p's ingaan, want ook wonen en werken hebben ruimte nodig.",
                "Ook een goede keuze heeft nadelen. Dat is precies waarom je de drie p's naast elkaar legt in plaats van één maatregel als de oplossing te verkopen.",
            ],
        ),
    ]
)


UITLEGBLADEN["oefenbundel-het-versterkte-broeikaseffect-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Houd de twee soorten straling apart: zonlicht komt binnen, warmtestraling gaat buiten. Broeikasgassen laten het eerste door en houden het tweede gedeeltelijk tegen. Dat verschil is het hele effect.",
            waarom=[
                "De gassen houden de warmte niet tegen zoals een deksel: ze nemen de warmtestraling op en stralen ze in alle richtingen weer uit, dus ook naar beneden. Daarom blijft het aan het oppervlak warmer.",
                "Nu is het gemiddeld ongeveer 15 °C, dus het natuurlijke broeikaseffect levert zowat 33 graden. Zonder die gassen was de aarde een ijsbol.",
                "Zonder het natuurlijke effect was er geen vloeibaar water en geen leven zoals wij het kennen. Het probleem is het versterkte effect: de extra gassen die wij er bovenop zetten.",
            ],
        ),
        dict(
            aanpak="Elk gas heeft zijn eigen bronnen. Zoek bij elk gas de bedrijfstak waar het vandaan komt, dan onthoud je het beter dan uit een lijstje.",
            waarom=[
                "Methaan en lachgas zitten in veel kleinere hoeveelheden in de lucht dan CO₂, maar houden per molecule veel meer warmte vast. Daarom tellen de landbouw en de veeteelt mee, ook al zijn het geen schoorstenen.",
                "Waterdamp is een versterkende terugkoppeling, geen oorzaak: warmere lucht houdt meer damp vast, en die damp warmt weer op. Je kan er niets aan doen door minder damp uit te stoten; je kan er wel iets aan doen door de opwarming zelf te remmen.",
            ],
        ),
        dict(
            aanpak="Een terugkoppeling is een gevolg dat op de oorzaak terugslaat. Versterkend wil zeggen dat het de opwarming nog groter maakt, dempend dat het ze afremt. Vraag je af: wordt het hierdoor nog warmer of juist minder warm?",
            waarom=[
                "Zee-ijs is wit en kaatst het zonlicht terug; de zee eronder is donker en neemt het op. Smelt het ijs, dan neemt de aarde meer warmte op en smelt er nog meer ijs. Dat heet het albedo-effect.",
                "Koolstof die miljoenen jaren in steenkool en olie onder de grond lag, komt bij verbranding in enkele jaren in de atmosfeer terecht. De cyclus zelf is natuurlijk; wat wij doen is één voorraad veel te snel leegmaken.",
            ],
        ),
        dict(
            aanpak="Zet elk gevolg op een plek waar je het kan uitleggen. Een gevolg valt het hardst waar de streek er al kwetsbaar voor was: laaggelegen land bij een stijgende zee, een droog gebied bij minder regen.",
            waarom=[
                "De gletsjers zijn niet enkel een landschap: miljoenen mensen in Azië en in de Alpenlanden halen hun zomerwater uit smeltwater dat in de winter als sneeuw werd opgeslagen.",
                "Dat is de kern van het rechtvaardigheidsvraagstuk op de klimaattoppen: wie het minst heeft uitgestoten, heeft het minst geld om zich te beschermen en wordt het eerst getroffen.",
            ],
        ),
        dict(
            aanpak="Milderen pakt de uitstoot aan, aanpassen pakt de gevolgen aan. De vraag is dus niet of het helpt, maar waar het ingrijpt: aan het begin of aan het einde van de ketting.",
            waarom=[
                "Bomen in de stad staan hier bij aanpassen, want ze bestrijden de hitte die er al is. Ze nemen ook een beetje CO₂ op, maar dat is niet waarvoor je ze in een straat plant.",
                "Er zit vertraging in het systeem: de uitstoot van vandaag werkt nog decennia door, en de opwarming die al gebeurd is, verdwijnt niet door minder uit te stoten. Daarom lopen de twee sporen naast elkaar.",
            ],
        ),
    ]
)


UITLEGBLADEN["oefenbundel-een-geografisch-onderzoek-voeren-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een onderzoek begint bij een vraag en eindigt bij een blik op je eigen werk. Daartussen: gegevens zoeken, ze verwerken tot iets wat je kan lezen, en dan pas besluiten.",
            waarom=[
                "Verwerken komt vóór besluiten: uit een ruwe lijst cijfers haal je niets, uit een kaart of grafiek wel. Wie eerst besluit en daarna een grafiek maakt, zoekt bevestiging in plaats van een antwoord.",
                None,
            ],
        ),
        dict(
            aanpak="Een bruikbare onderzoeksvraag is afgebakend in ruimte en in tijd, en vraagt naar iets wat je kan meten of tellen. Vraagt ze naar een mening of naar iets vaags, dan kan je nooit zeggen of je antwoord klopt.",
            waarom=[
                "Let op de verbeteringen: ze maken de vraag niet moeilijker maar nauwer. 'Hoe is de open ruimte veranderd' blijft vaag; 'tussen 1990 en 2020, in onze gemeente, in hectare' kan je nagaan.",
            ],
        ),
        dict(
            aanpak="Kies je bron bij wat je zoekt. Cijfers over mensen staan in statistiekdatabanken, hoogte en ligging op Geopunt of een topografische kaart, de toestand van vroeger op oude kaarten en luchtfoto's. Bestaat de meting nog niet, dan moet je ze zelf doen.",
            waarom=[
                "Verkeer tellen is het enige waar je zelf op straat moet staan: er bestaat geen databank met het aantal auto's in jouw straat op een dinsdagochtend.",
                "Een bron zonder datum en zonder afzender kan je niet controleren, en dus ook niet verdedigen als iemand je besluit in twijfel trekt. Dat geldt ook voor een kaart die er professioneel uitziet.",
            ],
        ),
        dict(
            aanpak="Twee gegevens die samen stijgen, hangen samen; dat is niet hetzelfde als dat de ene de andere veroorzaakt. Zoek altijd eerst of er een derde oorzaak is die beide verklaart.",
            waarom=[
                "Meer inwoners betekent meer fietsen én meer daders én meer meldingen. Het aantal diefstallen per duizend inwoners zou pas iets zeggen; de ruwe aantallen niet.",
                "Samenhang is geen oorzaak. Een derde factor kan beide verklaren, of het kan toeval zijn; soms loopt het verband zelfs andersom dan je denkt.",
                "Het gaat over twee valkuilen tegelijk: te weinig metingen in de tijd (één namiddag) en te weinig metingen in de ruimte (één punt). Een vaststelling heeft herhaling nodig, en metingen die op dezelfde manier gebeuren.",
            ],
        ),
        dict(
            aanpak="Op een kaart met schaal 1 : n is één centimeter op papier n centimeter in het echt. Reken dus eerst in centimeter en zet pas daarna om naar meter of kilometer: 100 000 cm is 1 km.",
            waarom=[
                "Reken mee bij de derde: 700 m is 70 000 cm, en 70 000 gedeeld door 10 000 is 7 cm. Wie van meter naar meter deelt, komt op 0,07 uit en dat klopt niet.",
                "Verwarrend maar waar: 1 : 10 000 heet een grote schaal en 1 : 500 000 een kleine. Kijk naar de breuk, want een tienduizendste is groter dan een vijfhonderdduizendste. Grote schaal is dus klein gebied met veel detail.",
            ],
        ),
    ]
)

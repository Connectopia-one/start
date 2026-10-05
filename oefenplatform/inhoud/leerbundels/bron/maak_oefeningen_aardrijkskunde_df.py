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

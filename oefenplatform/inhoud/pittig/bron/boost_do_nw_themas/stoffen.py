"""Enkelvoudige en samengestelde stoffen, en chemische reacties — pittig (🚀 Boost doorstroom, natuurwetenschappen)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, GROEN, LICHTGROEN, BLAUW, ORANJE, GRIJS, DONKER, GEEL, ROOD, PAARS

# Twee energiediagrammen --------------------------------------------------
ED = Prent("energiediagrammen", "Twee energiediagrammen", "energiediagram van een exo-energetische (A) en een endo-energetische reactie (B)")
def _diagram(x0, hoog_begin, hoog_eind, letter):
    ED.lijn(x0, 540, x0 + 380, 540, DONKER, 2)
    ED.lijn(x0, 540, x0, 110, DONKER, 2)
    ED.tekst(x0 - 6, 100, "energie", 16, "start")
    ED.tekst(x0 + 375, 572, "verloop van de reactie", 16, "end")
    yb, ye = 540 - hoog_begin, 540 - hoog_eind
    ED.lijn(x0 + 30, yb, x0 + 130, yb, BLAUW, 6)
    ED.lijn(x0 + 250, ye, x0 + 350, ye, ORANJE, 6)
    ED.pad(f"M{x0+130} {yb} C {x0+170} {min(yb, ye)-120}, {x0+210} {min(yb, ye)-120}, {x0+250} {ye}", "none", DONKER, 2)
    ED.lijn(x0 + 300, yb, x0 + 300, ye, "#999999", 2, True)
    ED.pijl(x0 + 300, yb, x0 + 300, ye, ROOD, 3)
    ED.letter(x0 + 190, 600, letter)
    return yb, ye
ya, yae = _diagram(80, 300, 120, "A")
yb, ybe = _diagram(540, 130, 310, "B")
Z_ENDO = Prent.zone(530, 90, 400, 540)
Z_EXO = Prent.zone(60, 90, 400, 540)
Z_REAG_A = Prent.zone(100, ya - 20, 120, 40)
Z_PROD_B = Prent.zone(780, ybe - 20, 120, 40)
Z_PIJL_A = Prent.zone(365, ya - 5, 30, yae - ya + 10)

VRAGEN = [
    klik(
        "Klik op het diagram van een reactie waarbij de beker kouder aanvoelt.",
        ED.bestand, [Z_ENDO],
        "Bij een endo-energetische reactie liggen de producten hoger: de reactie neemt energie op uit de omgeving.",
    ),
    klik(
        "Klik op het diagram dat bij een verbranding past.",
        ED.bestand, [Z_EXO],
        "Een verbranding geeft warmte en licht af. De producten liggen lager dan de reagentia.",
    ),
    klik(
        "Klik in diagram A op het niveau van de reagentia.",
        ED.bestand, [Z_REAG_A],
        "De reagentia staan links, aan het begin van het verloop.",
    ),
    klik(
        "Klik in diagram B op het niveau van de reactieproducten.",
        ED.bestand, [Z_PROD_B],
        "De reactieproducten staan rechts, aan het einde van het verloop.",
    ),
    klik(
        "Klik in diagram A op de pijl die de reactie-energie toont.",
        ED.bestand, [Z_PIJL_A],
        "De reactie-energie is het hoogteverschil tussen reagentia en reactieproducten.",
    ),
    met_prent(ED.bestand, tabel(
        "Kijk naar de twee diagrammen. Klopt dit?",
        [
            ("Bij A komt er energie vrij.", J),
            ("Bij B liggen de producten lager dan de reagentia.", F),
            ("Verticaal staat de energie.", J),
            ("Een koudekompres werkt zoals reactie B.", J),
        ],
        "Een koudekompres haalt energie uit de omgeving: endo-energetisch.",
    )),
    sorteer(
        "Enkelvoudige of samengestelde stof?",
        ["Enkelvoudig", "Samengesteld"],
        [
            ["zuurstofgas O₂", "Enkelvoudig"],
            ["ozon O₃", "Enkelvoudig"],
            ["ijzer Fe", "Enkelvoudig"],
            ["water H₂O", "Samengesteld"],
            ["koolstofdioxide CO₂", "Samengesteld"],
            ["natriumchloride NaCl", "Samengesteld"],
        ],
        "Enkelvoudig: één soort atomen. Samengesteld: meer dan één soort.",
    ),
    koppel(
        "Koppel elk symbool aan zijn element.",
        [
            ("Na", "natrium"),
            ("K", "kalium"),
            ("Cu", "koper"),
            ("Au", "goud"),
            ("Ag", "zilver"),
            ("Fe", "ijzer"),
        ],
        ["koolstof"],
        "Veel symbolen komen uit het Latijn. Koolstof is C.",
    ),
    tabel(
        "Tel de atomen. Klopt het?",
        [
            ("In 3 H₂O staan 9 atomen.", J),
            ("In 2 H₂SO₄ staan 14 atomen.", J),
            ("In CO₂ zitten drie elementen.", F),
            ("In 2 CO₂ staan 4 zuurstofatomen.", J),
            ("In 4 NH₃ staan 7 waterstofatomen.", F),
        ],
        "Vermenigvuldig het aantal atomen in één molecule met de coëfficiënt. 4 NH₃ geeft 12 waterstofatomen.",
    ),
    inv(
        "Hoeveel atomen staan er in totaal in 3 CH₄?",
        ["15"],
        "Eén molecule telt 1 koolstof- en 4 waterstofatomen, samen 5. Drie moleculen geven 15 atomen.",
    ),
    tabel(
        "Metaal, niet-metaal of edelgas?",
        [
            ("koper", "Metaal"),
            ("kwik", "Metaal"),
            ("chloor", "Niet-metaal"),
            ("zuurstof", "Niet-metaal"),
            ("helium", "Edelgas"),
            ("neon", "Edelgas"),
        ],
        "Metalen geleiden en glanzen, niet-metalen geleiden slecht, edelgassen zijn inert.",
        kolommen=["Metaal", "Niet-metaal", "Edelgas"],
    ),
    casus(
        "Een onbekende stof is een glanzende vaste stof. Ze geleidt elektriciteit en warmte goed en laat zich tot dunne draad trekken. Ze heeft een roodbruine kleur.",
        [
            mk(
                "Welke stof is het?",
                ["Koper", "Kwik", "Chloor", "Grafiet"],
                0,
                "Kwik is vloeibaar, chloor is een geelgroen gas. De roodbruine kleur is typisch voor koper.",
            ),
            tabel(
                "Klopt dit over deze stof?",
                [
                    ("Het is een metaal.", J),
                    ("Het is een enkelvoudige stof.", J),
                    ("Ze is geschikt voor elektriciteitsdraden.", J),
                    ("Ze is een edelgas.", F),
                ],
                "Koper zit in elektriciteitsdraden en kookpotten.",
            ),
        ],
    ),
    casus(
        "Je maakt de vergelijking kloppend: H₂ + O₂ → H₂O. Een klasgenoot schrijft H₂ + O₂ → H₂O₂.",
        [
            mk(
                "Wat is er fout aan de oplossing van je klasgenoot?",
                [
                    "Hij veranderde een index",
                    "Hij voegde een coëfficiënt toe",
                    "Hij liet de pijl weg",
                    "Hij veranderde de reagentia",
                ],
                0,
                "Verander je de index, dan heb je een andere stof. Alleen de coëfficiënten mag je aanpassen.",
            ),
            sleep(
                "De juiste vergelijking is [[2]] H₂ + O₂ → [[2]] H₂O. Links en rechts staan dan [[4]] waterstofatomen en 2 zuurstofatomen.",
                ["3", "6"],
                "Een reactie herschikt alleen de atomen.",
            ),
        ],
    ),
    inv(
        "Maak kloppend: N₂ + 3 H₂ → … NH₃. Welke coëfficiënt hoort voor NH₃?",
        ["2"],
        "Links staan 2 stikstofatomen en 6 waterstofatomen. Met 2 NH₃ heb je rechts ook 2 stikstof- en 6 waterstofatomen.",
    ),
    tabel(
        "Synthese of analyse?",
        [
            ("Water valt door stroom uiteen in waterstofgas en zuurstofgas.", "Analyse"),
            ("Magnesium en zuurstofgas vormen magnesiumoxide.", "Synthese"),
            ("Stikstofgas en waterstofgas vormen ammoniak.", "Synthese"),
        ],
        "Bij een synthese ontstaat één nieuwe stof, bij een analyse valt één stof uiteen.",
        kolommen=["Synthese", "Analyse"],
    ),
    casus(
        "In een open schaal verbrandt Ruben een stukje hout. Na afloop weegt het overblijvende as veel minder dan het hout ervoor. Hij besluit dat de wet van behoud van massa hier niet geldt.",
        [
            mk(
                "Wat is er mis met zijn besluit?",
                [
                    "Er ontsnapten gassen die hij niet woog",
                    "De weegschaal is door de hitte helemaal stuk",
                    "Bij een verbranding verdwijnen atomen",
                    "Hout is een zuivere stof zonder massa",
                ],
                0,
                "De wet geldt altijd. Vang je ook de gassen op, dan klopt de balans weer.",
            ),
            keuze(
                "Doet Ruben de proef in een [[*afgesloten vat|open schaal|grotere schaal]], dan blijft de totale massa gelijk.",
                "In een gesloten vat kan er niets weg.",
            ),
        ],
    ),
    tabel(
        "Exo- of endo-energetisch?",
        [
            ("een kaars die brandt", "Exo"),
            ("een koudekompres dat koud wordt", "Endo"),
            ("een reactie die licht uitzendt", "Exo"),
            ("een beker die kouder aanvoelt na het mengen", "Endo"),
        ],
        "Energie afstaan is exo, energie opnemen is endo.",
        kolommen=["Exo", "Endo"],
    ),
    koppel(
        "Koppel elke stof aan een toepassing.",
        [
            ("helium", "ballonnen vullen"),
            ("neon", "lichtreclame"),
            ("zuurstofgas", "lassen en ademhulp"),
            ("kwik", "oude thermometers"),
        ],
        ["blussen van vuur"],
        "Helium is veilig, want het reageert zo goed als nergens mee.",
    ),
    tabel(
        "Klopt dit over stoffen?",
        [
            ("Grafiet en diamant bestaan allebei uit koolstof.", J),
            ("Ozon dicht bij de grond is gezond voor je longen.", F),
            ("Chloorgas is geelgroen.", J),
            ("Edelgassen hebben een volle buitenste schil.", J),
            ("Niet-metalen geleiden elektriciteit goed.", F),
        ],
        "Ozon is hoog in de atmosfeer nuttig, dicht bij de grond schadelijk.",
    ),
    mk(
        "Waarom verschillen grafiet en diamant zo sterk, als ze allebei uit koolstof bestaan?",
        [
            "Hun atomen zitten anders aan elkaar",
            "Diamant bevat ook zuurstofatomen",
            "Grafiet is een mengsel van metalen",
            "Diamant is een edelgas in vaste vorm",
        ],
        0,
        "Diamant heeft een stevig ruimtelijk rooster, grafiet losse lagen.",
    ),
    keuze(
        "Keukenzout is de [[*triviale|IUPAC-|officiële]] naam van natriumchloride.",
        "De triviale naam is de dagelijkse naam.",
    ),
    tabel(
        "Klopt dit over de reactievergelijking 2 Mg + O₂ → 2 MgO?",
        [
            ("Links en rechts staan twee magnesiumatomen.", J),
            ("Magnesium en zuurstofgas zijn de reagentia.", J),
            ("Rechts staan vier zuurstofatomen.", F),
            ("Het is een synthese.", J),
        ],
        "Links en rechts staan 2 Mg en 2 O. Uit twee stoffen ontstaat één nieuwe.",
    ),
    mk(
        "Waarom is een chemische reactie iets anders dan mengen?",
        [
            "Er ontstaan nieuwe stoffen",
            "Er verdwijnen atomen uit het mengsel",
            "Bij mengen komt altijd licht vrij",
            "De massa wordt bij een reactie groter",
        ],
        0,
        "Na mengen heb je dezelfde stoffen, na een reactie nieuwe stoffen met andere eigenschappen.",
    ),
    tabel(
        "Kan deze vorm van energie vrijkomen bij een chemische reactie?",
        [
            ("warmte", J),
            ("licht", J),
            ("elektrische energie", J),
            ("massa", F),
        ],
        "Massa is geen vorm van energie. Een batterij geeft elektrische energie.",
    ),
    keuze(
        "In 3 H₂O is de 2 de [[*index|coëfficiënt|reactie-energie]] en de 3 de coëfficiënt.",
        "De index staat klein achter een symbool, de coëfficiënt vooraan.",
    ),
    sleep(
        "Links van de pijl staan de [[reagentia]], rechts de [[reactieproducten]]. De pijl geeft de [[richting]] van de omzetting aan.",
        ["coëfficiënten", "edelgassen"],
        "Uit de reagentia worden de reactieproducten gevormd.",
    ),
    open_(
        "Leg met de wet van behoud van massa uit waarom je bij het kloppend maken van een reactievergelijking enkel de coëfficiënten mag aanpassen.",
        "Bij een reactie verdwijnen er geen atomen en komen er geen bij; ze worden alleen anders geschikt. Daarom moet links en rechts van elk element evenveel atomen staan. Dat los je op met coëfficiënten. Verander je de index, dan schrijf je een andere stof op en klopt de reactie niet meer.",
    ),
]

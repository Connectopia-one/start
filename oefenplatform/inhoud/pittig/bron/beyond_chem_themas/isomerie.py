"""Isomerie en chiraliteit — pittig (⚗️ Beyond doorstroom, chemie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, BLAUW, ORANJE, DONKER, ROOD, GROEN, PAARS, GRIJS, GEEL

# Z/E bij een dubbele binding ----------------------------------------------
ZE = Prent("z-e-isomeren", "Drie alkenen met vier koolstofatomen", "drie tekeningen van een C=C met groepen eraan; letters P, Q en R")


def _alkeen(p, x, links, rechts):
    """links/rechts: (boven, onder) groepen."""
    p.lijn(x - 50, 300, x + 50, 300, DONKER, 3)
    p.lijn(x - 50, 310, x + 50, 310, DONKER, 3)
    p.tekst(x - 62, 313, "C", 24, vet=True)
    p.tekst(x + 62, 313, "C", 24, vet=True)
    for (gx, gy, t, x1, y1, x2, y2) in (
        (x - 105, 215, links[0], x - 72, 290, x - 95, 230),
        (x - 105, 405, links[1], x - 72, 320, x - 95, 385),
        (x + 105, 215, rechts[0], x + 72, 290, x + 95, 230),
        (x + 105, 405, rechts[1], x + 72, 320, x + 95, 385),
    ):
        p.lijn(x1, y1, x2, y2, DONKER, 3)
        p.tekst(gx, gy, t, 22, vet=True, kleur=BLAUW if t != "H" else DONKER)


_alkeen(ZE, 170, ("CH₃", "H"), ("CH₃", "H"))
_alkeen(ZE, 500, ("CH₃", "H"), ("H", "CH₃"))
_alkeen(ZE, 810, ("H", "H"), ("CH₂CH₃", "H"))
for k, x in zip("PQR", (170, 500, 810)):
    ZE.letter(x, 520, k)
ZZE = {k: [Prent.zone(x - 140, 170, 280, 270), Prent.rond(x, 520, 22)] for k, x in zip("PQR", (170, 500, 810))}

# Asymmetrisch koolstofatoom -----------------------------------------------
AS = Prent("chloorbutaan", "Structuurformule van een halogeenalkaan", "vier koolstofatomen op een rij, aan het tweede hangt een chlooratoom; letters A tot D bij de koolstofatomen")
XS = [180, 380, 580, 780]
LAB = ["CH₃", "C", "CH₂", "CH₃"]
for i, x in enumerate(XS):
    AS.rect(x - 50, 290, 100, 60, "#fbf6ea", DONKER, 10, 2)
    AS.tekst(x, 330, LAB[i], 24, vet=True)
    if i < 3:
        AS.lijn(x + 50, 320, XS[i + 1] - 50, 320, DONKER, 3)
    AS.letter(x, 440, "ABCD"[i])
AS.lijn(380, 290, 380, 225, DONKER, 3)
AS.tekst(380, 210, "Cl", 24, vet=True, kleur=GROEN)
AS.lijn(380, 350, 380, 395, DONKER, 3)
AS.tekst(410, 395, "H", 22, vet=True)
ZAS = {k: [Prent.zone(XS[i] - 50, 290, 100, 60), Prent.rond(XS[i], 440, 22)] for i, k in enumerate("ABCD")}

VRAGEN = [
    klik(
        "Klik op de E-vorm van but-2-een.",
        ZE.bestand, ZZE["Q"],
        "Bij E staan de twee methylgroepen aan een andere kant van de dubbele binding.",
    ),
    klik(
        "Klik op het alkeen dat geen Z/E-isomerie kan hebben.",
        ZE.bestand, ZZE["R"],
        "Het linkse koolstofatoom draagt twee keer H: niet twee verschillende groepen.",
    ),
    met_prent(ZE.bestand, tabel(
        "Kijk naar de drie alkenen. Klopt dit?",
        [
            ("P is de Z-vorm van but-2-een.", J),
            ("P en Q zijn stereo-isomeren.", J),
            ("R is but-1-een.", J),
            ("P en Q zijn ketenisomeren.", F),
        ],
        "Bij stereo-isomeren is de volgorde van de atomen gelijk, alleen hun plaats in de ruimte verschilt.",
    )),
    met_prent(ZE.bestand, mk(
        "Waarom kan P niet vanzelf in Q overgaan door te draaien?",
        [
            "De dubbele binding kan niet vrij draaien",
            "P en Q hebben een andere brutoformule",
            "De methylgroepen zijn te zwaar om te draaien",
            "P is een alkaan en Q een alkeen",
        ],
        0,
        "Rond een enkelvoudige binding kan een molecule wel vrij draaien.",
    )),
    klik(
        "Klik op het asymmetrische koolstofatoom.",
        AS.bestand, ZAS["B"],
        "Het draagt vier verschillende groepen: Cl, H, CH₃ en CH₂CH₃.",
    ),
    met_prent(AS.bestand, tabel(
        "Kijk naar 2-chloorbutaan. Klopt dit?",
        [
            ("De molecule is chiraal.", J),
            ("Er zijn twee spiegelbeeldisomeren.", J),
            ("C is ook asymmetrisch.", F),
            ("De twee spiegelbeelden hebben hetzelfde kookpunt.", J),
        ],
        "C draagt twee waterstofatomen: niet vier verschillende groepen.",
    )),
    tabel(
        "Welk soort isomerie is dit?",
        [
            ("butaan en 2-methylpropaan", "Keten"),
            ("propaan-1-ol en propaan-2-ol", "Plaats"),
            ("ethanol en methoxymethaan", "Functie"),
            ("propanal en propanon", "Functie"),
            ("but-1-een en but-2-een", "Plaats"),
        ],
        "Bij functie-isomerie verandert de stofklasse.",
        kolommen=["Keten", "Plaats", "Functie"],
    ),
    tabel(
        "Hoeveel structuurisomeren bestaan er?",
        [
            ("C₃H₈", "1"),
            ("C₄H₁₀", "2"),
            ("C₅H₁₂", "3"),
            ("CH₄", "1"),
        ],
        "Pas vanaf vier koolstofatomen kan een keten vertakken.",
        kolommen=["1", "2", "3"],
    ),
    inv(
        "Hoeveel stereo-isomeren horen bij een molecule met vier asymmetrische koolstofatomen?",
        ["16", "zestien"],
        "2 tot de vierde = 16.",
    ),
    sorteer(
        "Structuurisomerie of stereo-isomerie?",
        ["Structuurisomerie", "Stereo-isomerie"],
        [
            ("ketenisomerie", "Structuurisomerie"),
            ("Z/E-isomerie", "Stereo-isomerie"),
            ("spiegelbeeldisomerie", "Stereo-isomerie"),
            ("functie-isomerie", "Structuurisomerie"),
            ("plaatsisomerie", "Structuurisomerie"),
        ],
        "Bij stereo-isomerie zitten de atomen in dezelfde volgorde aan elkaar.",
    ),
    tabel(
        "Gelijk of verschillend voor twee spiegelbeeldisomeren?",
        [
            ("het smeltpunt", "Gelijk"),
            ("de molaire massa", "Gelijk"),
            ("de draairichting van gepolariseerd licht", "Verschillend"),
            ("de werking in het lichaam", "Verschillend"),
        ],
        "Receptoren in het lichaam voelen de ruimtelijke vorm.",
        kolommen=["Gelijk", "Verschillend"],
    ),
    casus(
        "Een farmabedrijf maakt een geneesmiddel met één asymmetrisch koolstofatoom. Na de synthese heeft het een racemisch mengsel.",
        [
            keuze(
                "In dat mengsel zitten [[*evenveel|meer Z- dan E-|alleen]] spiegelbeeldisomeren van beide soorten.",
                "Racemisch: 50 % van elk.",
            ),
            tabel(
                "Klopt dit over het racemisch mengsel?",
                [
                    ("Het draait het vlak van gepolariseerd licht niet.", J),
                    ("Mogelijk werkt maar de helft zoals bedoeld.", J),
                    ("De twee isomeren hebben een andere molaire massa.", F),
                ],
                "De draaiingen van beide helften heffen elkaar op.",
            ),
            mk(
                "Waarom kunnen de twee spiegelbeelden anders werken in het lichaam?",
                [
                    "Receptoren passen op één vorm",
                    "Ze bevatten elk andere soorten atomen",
                    "Het ene is een zuur, het andere een base",
                    "Het ene lost op in water, het andere nooit",
                ],
                0,
                "Zoals een linkerhand niet in een rechterhandschoen past.",
            ),
        ],
    ),
    mk(
        "Waarom bestaan er van propaan-2-ol geen twee spiegelbeeldisomeren?",
        [
            "Het middelste C draagt twee CH₃",
            "Het heeft helemaal geen OH-groep",
            "Het heeft een dubbele binding in de keten",
            "Het bevat maar twee koolstofatomen",
        ],
        0,
        "Voor chiraliteit moeten alle vier de groepen verschillen.",
    ),
    tabel(
        "Kan deze stof Z/E-isomerie vertonen?",
        [
            ("but-2-een", J),
            ("propeen", F),
            ("etheen", F),
            ("pent-2-een", J),
        ],
        "Elk koolstofatoom van de dubbele binding moet twee verschillende groepen dragen.",
    ),
    koppel(
        "Koppel elk begrip aan zijn betekenis.",
        [
            ("Z", "de voorrangsgroepen staan aan dezelfde kant"),
            ("E", "de voorrangsgroepen staan aan de overkant"),
            ("racemisch", "evenveel van beide spiegelbeelden"),
            ("chiraal", "niet over zijn spiegelbeeld te leggen"),
        ],
        ["dezelfde brutoformule en dezelfde bouw"],
        "Dezelfde formule en bouw: dan is het dezelfde stof.",
    ),
    tabel(
        "Klopt dit over isomeren?",
        [
            ("Ze hebben dezelfde brutoformule.", J),
            ("Ze kunnen een ander kookpunt hebben.", J),
            ("Ze kunnen anders ruiken.", J),
            ("Ze hebben altijd dezelfde stofklasse.", F),
        ],
        "Functie-isomeren horen tot een andere stofklasse.",
    ),
    mk(
        "2-methylpropaan kookt lager dan butaan. Waarom?",
        [
            "Vertakte moleculen raken elkaar minder",
            "2-methylpropaan heeft minder atomen in totaal",
            "Butaan heeft een dubbele binding",
            "2-methylpropaan is een ionverbinding",
        ],
        0,
        "Minder contactoppervlak geeft zwakkere krachten tussen de moleculen.",
    ),
    sleep(
        "Een koolstofatoom met [[vier]] verschillende groepen heet [[asymmetrisch]]. Een molecule met zo'n atoom is meestal [[chiraal]].",
        ["drie", "symmetrisch", "verzadigd"],
        "Met één asymmetrisch koolstofatoom is de molecule altijd chiraal.",
    ),
    tabel(
        "Welke stofklassen kunnen bij deze brutoformule horen?",
        [
            ("C₃H₈O", "Alcohol of ether"),
            ("C₃H₆O", "Aldehyde of keton"),
            ("C₃H₆O₂", "Carbonzuur of ester"),
            ("C₂H₆O", "Alcohol of ether"),
        ],
        "Telkens functie-isomeren.",
        kolommen=["Alcohol of ether", "Aldehyde of keton", "Carbonzuur of ester"],
    ),
    inv(
        "Hoeveel plaatsisomeren heeft een alcohol met de onvertakte keten van pentaan?",
        ["3", "drie"],
        "Pentaan-1-ol, pentaan-2-ol en pentaan-3-ol. De OH op C4 is hetzelfde als op C2.",
    ),
    keuze(
        "Met [[*gepolariseerd|ultraviolet|infrarood]] licht onderscheid je twee spiegelbeeldisomeren.",
        "Ze draaien het trillingsvlak even ver, maar naar de andere kant.",
    ),
    tabel(
        "Klopt dit over Z/E-isomeren?",
        [
            ("Het zijn stereo-isomeren.", J),
            ("Ze kunnen een ander kookpunt hebben.", J),
            ("Z komt van het Duitse zusammen.", J),
            ("Het zijn structuurisomeren.", F),
        ],
        "De volgorde van de atomen is gelijk.",
    ),
    mk(
        "Hoeveel asymmetrische koolstofatomen heeft 2-chloorpropaan?",
        [
            "nul",
            "één",
            "twee",
            "drie",
        ],
        0,
        "Het middelste C-atoom draagt twee methylgroepen: twee gelijke groepen.",
    ),
    inv(
        "Een molecule heeft 8 stereo-isomeren door asymmetrische koolstofatomen. Hoeveel van die atomen heeft ze?",
        ["3", "drie"],
        "2 tot de derde = 8.",
    ),
    tabel(
        "Klopt dit over methaan, ethaan en propaan?",
        [
            ("Methaan heeft geen isomeren.", J),
            ("Propaan kan niet vertakken.", J),
            ("Butaan heeft een ketenisomeer.", J),
            ("Propaan heeft twee ketenisomeren.", F),
        ],
        "Een zijketen aan het middelste C-atoom van propaan geeft gewoon weer butaan.",
    ),
    keuze(
        "Twee isomeren die elkaars spiegelbeeld zijn, heten ook [[*enantiomeren|ketenisomeren|functie-isomeren]].",
        "Ze passen niet op elkaar, zoals een linker- en een rechterhand.",
    ),
    tabel(
        "Klopt dit over plaatsisomeren?",
        [
            ("Ze horen tot dezelfde stofklasse.", J),
            ("De functionele groep zit op een andere plaats.", J),
            ("Butaan-1-ol en butaan-2-ol zijn plaatsisomeren.", J),
            ("Een plaatsisomeer heeft een andere brutoformule.", F),
        ],
        "Isomeren hebben altijd dezelfde brutoformule.",
    ),
    open_(
        "Leg uit waarom but-2-een een Z- en een E-vorm heeft, maar butaan niet.",
        "In but-2-een zit een dubbele binding die niet vrij kan draaien. Elk koolstofatoom van die binding draagt twee verschillende groepen (CH₃ en H), dus kunnen de methylgroepen aan dezelfde kant (Z) of aan de overkant (E) staan. In butaan zijn er enkel enkelvoudige bindingen: die draaien vrij, zodat er geen vaste Z- of E-vorm bestaat.",
    ),
]

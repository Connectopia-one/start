"""De psychosociale ontwikkeling volgens Erikson — pittig (🚀 Boost doorstroom, sociale en gedragswetenschappen).

Eigen vragen strikt binnen sg_erikson: de acht conflicten, de
levensloopfase van elk, welke pool bereikt wordt en of het conflict opgelost
is, met de krachten. Met een zelfgetekende levenstrap."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, LICHTGROEN

TR = Prent("levenstrap", "Een levenstrap met acht treden", "een trap met acht treden, elk met een levensloopfase en een letter A tot H")
FASEN = ["babytijd", "peutertijd", "kleutertijd", "lagere school", "adolescentie", "vroege volw.", "midden volw.", "late volw."]
TREDE = {}
for i, (t, naam) in enumerate(zip("ABCDEFGH", FASEN)):
    x = 50 + i * 112; y = 560 - (i + 1) * 58
    TR.rect(x, y, 112, 560 - y, "#eef3e6" if i % 2 == 0 else "#dfe9d2", DONKER, 0, 2)
    TR.tekst(x + 56, y + 26, naam, 15)
    TR.letter(x + 56, y - 30, t)
    TREDE[t] = (x, y)
TR.lijn(30, 560, 970, 560, DONKER, 3)
U = "levenstrap.svg"
Z = {t: [Prent.zone(x, y - 60, 112, 100)] for t, (x, y) in TREDE.items()}

OMA = ("Lees het verhaal.\n\n"
       "Oma Rita is 82. Ze bladert met haar kleindochter door een oud fotoalbum. « Niet alles liep zoals ik wou, » zegt ze, « maar ik ben blij met hoe mijn leven gelopen is. » "
       "Haar buurman Jef, ook 82, zit vaak alleen. Hij zegt: « Ik heb zoveel gemist, en nu is het te laat. »")

VRAGEN = [
    klik("Bekijk de levenstrap. Klik op de letter bij de fase van initiatief versus schuld.", U, Z["C"], "De kleuter verzint plannen en wil ze uitvoeren."),
    klik("Klik op de letter bij de fase van intimiteit versus isolatie.", U, Z["F"], "Je durven binden in de vroege volwassenheid."),
    klik("Klik op de letter bij de fase van generativiteit versus stagnatie.", U, Z["G"], "Iets doorgeven aan wie na je komt."),
    klik("Klik op de letter bij de fase van handvaardigheid versus minderwaardigheid.", U, Z["D"], "Lezen, rekenen en sporten leren."),
    casus(OMA, [
        keuze("Oma Rita en Jef zitten in de fase van integriteit versus [[*wanhoop|isolatie|schuld]].", "De late volwassenheid."),
        sorteer("Welke pool bereikt hij of zij?", ["integriteit", "wanhoop"],
                [("oma Rita", "integriteit"), ("Jef", "wanhoop")],
                "Met vrede terugkijken tegenover het gevoel dat het te laat is."),
        mk("Welke kracht groeit bij oma Rita uit deze fase?",
           ["wijsheid", "hoop, de kracht van de allereerste fase", "trouw, de kracht van de adolescentie", "doelgerichtheid, de kracht van de kleutertijd"],
           0, "Met afstand naar je eigen leven kunnen kijken."),
        keuze("Integriteit betekent hier [[*met vrede terugkijken op je leven als geheel|eerlijk zijn tegen anderen|nooit fouten maken]].", "Niet de gewone betekenis van het woord."),
    ]),
    volgorde("Zet deze conflicten in de volgorde van de levensloop.",
             ["vertrouwen versus wantrouwen", "autonomie versus twijfel en schaamte", "initiatief versus schuld", "handvaardigheid versus minderwaardigheid", "identiteit versus identiteitsverwarring"],
             "Van de babytijd tot de adolescentie."),
    koppel("Koppel het conflict aan de kracht die eruit groeit.",
           [("vertrouwen versus wantrouwen", "hoop"), ("autonomie versus twijfel", "wil"), ("identiteit versus verwarring", "trouw"), ("intimiteit versus isolatie", "liefde"), ("generativiteit versus stagnatie", "zorg")],
           ["gehoorzaamheid"], "Elke opgeloste fase levert een kracht op."),
    sorteer("Welk conflict speelt hier?", ["autonomie versus twijfel", "initiatief versus schuld", "identiteit versus verwarring", "intimiteit versus isolatie"],
            [("Een peuter wil zelf zijn schoenen aandoen.", "autonomie versus twijfel"), ("Een kleuter bedenkt een spel en verdeelt de rollen.", "initiatief versus schuld"), ("Een jongere probeert elke maand een andere stijl.", "identiteit versus verwarring"), ("Iemand van dertig durft zich niet te binden.", "intimiteit versus isolatie")],
            "Benoem eerst de fase, dan het conflict."),
    tabel("Klopt dit over Erikson?",
          [("Een conflict moet volledig naar één pool overhellen.", F), ("Een beetje wantrouwen is nuttig.", J), ("De fasen stoppen na de puberteit.", F), ("Een latere ervaring kan een oude pool nog verschuiven.", J)],
          "Het gaat om een gezond overwicht."),
    mk("Een kind faalt op school keer op keer. Welk risico ziet Erikson?",
       ["minderwaardigheid", "isolatie, want het zal nooit een relatie hebben", "wanhoop, want het kijkt terug op een mislukt leven", "stagnatie, want het geeft niets door aan anderen"],
       0, "Succeservaring op school telt in die fase."),
    keuze("Een vrouw van 50 leidt op het werk jonge collega's op. Ze bereikt de pool [[*generativiteit|stagnatie|isolatie]].", "Doorgeven aan een volgende generatie."),
    mk("Waarom hangt intimiteit samen met het conflict van de adolescentie?",
       ["eerst moet je weten wie je bent", "omdat je in de adolescentie al getrouwd moet zijn", "omdat beide over je schoolresultaten gaan", "omdat beide pas na de pensioenleeftijd spelen"],
       0, "Zonder identiteit is intimiteit moeilijk."),
    keuze("Een baby die getroost wordt als hij huilt, bereikt de pool [[*vertrouwen|wantrouwen|twijfel]].", "De wereld is betrouwbaar."),
    inv("Een kleuter die zijn plannen mag uitvoeren, ontwikkelt volgens Erikson een kracht. Welke? Eén woord.", ["doelgerichtheid"], "Een plan maken en het durven uitvoeren."),
    tabel("Welke kracht hoort bij welke fase?",
          [("babytijd", "hoop"), ("lagere school", "competentie"), ("adolescentie", "trouw"), ("late volwassenheid", "wijsheid")],
          "Elke fase haar kracht.", ["hoop", "competentie", "trouw", "wijsheid"]),
    keuze("Een kleuter bouwt een hut en krijgt telkens straf omdat hij niet eerst toestemming vroeg. Dan dreigt de pool [[*schuld|isolatie|wanhoop]].", "Initiatief versus schuld."),
    keuze("Erikson noemde identiteitsverwarring ook een [[*identiteitscrisis|midlifecrisis|hechtingscrisis]].", "Geen eigen lijn, geen richting."),
    sleep("Een conflict is [[opgelost]] als de goede pool het [[overwicht]] heeft. Er blijft altijd iets van de [[andere]] pool over.",
          ["verdwenen", "eerste"], "Niet alles of niets."),
    mk("Je krijgt op het examen een kort verhaal over iemand. Wat benoem je dan volgens Erikson?",
       ["fase, pool en oplossing benoemen", "enkel de leeftijd van de persoon opschrijven", "zeggen of de persoon goed of slecht handelt", "het stadium van Piaget erbij zoeken"],
       0, "Welke fase, welke pool, en is het conflict opgelost."),
    tabel("Speelt dit conflict pas vanaf de volwassenheid?",
          [("intimiteit versus isolatie", J), ("generativiteit versus stagnatie", J), ("integriteit versus wanhoop", J), ("identiteit versus verwarring", F)],
          "Identiteit hoort bij de adolescentie."),
    keuze("Een peuter die nooit iets zelf mag proberen, loopt het risico op twijfel en [[*schaamte|wanhoop|stagnatie]].", "Autonomie versus twijfel en schaamte."),
    inv("Hoeveel conflicten onderscheidt Erikson? Schrijf het getal.", ["8", "acht"], "Eén per levensloopfase."),
    keuze("Stagnatie is de negatieve pool van [[*generativiteit|intimiteit|integriteit]]: het gevoel dat je niets nalaat.", "De kracht van die fase is zorg."),
    mk("Waarom hangt Erikson elk conflict aan een levensloopfase?",
       ["elke leeftijd stelt eigen eisen", "omdat hij enkel kinderen bestudeerde in zijn werk", "omdat alle conflicten tegelijk spelen in elke fase", "omdat het conflict van een fase nooit nog verandert"],
       0, "Een peuter krijgt andere eisen dan een scholier."),
    tabel("Hoort deze pool bij de negatieve kant?",
          [("wantrouwen", J), ("autonomie", F), ("minderwaardigheid", J), ("isolatie", J), ("identiteit", F)],
          "Twee polen per conflict."),
    keuze("Een jongen van 15 zegt elke week iets anders over wat hij later wil doen en weet niet wie hij is. Hij zit nu aan de kant van de [[*identiteitsverwarring|integriteit|generativiteit]].", "Uitproberen hoort erbij, maar zonder eigen lijn dreigt verwarring."),
    open_("Bedenk een voorbeeld van een adolescent en leg uit welk conflict van Erikson speelt, welke pool bereikt wordt en of het opgelost is.",
          "Sam (16) probeert verschillende vriendengroepen en stijlen uit, maar kiest na een tijd zelf welke studie en welke waarden bij hem passen. Het conflict is identiteit versus identiteitsverwarring. Hij bereikt de pool identiteit; het conflict is opgelost, en daaruit groeit trouw aan wie hij is."),
]

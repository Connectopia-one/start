"""Kunst van de prehistorie, Egypte en de klassieke oudheid — pittig
(🌍 Beyond doorstroom, kunstbeschouwing en filosofie). Strikt binnen
beyond/bron/kfb_oudheid.py: context, vormelijke kenmerken en bekendste
vertegenwoordigers, en die kenmerken toepassen op ongeziene werken."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS, LICHTGROEN, BLAUW, ORANJE, GEEL

# Prent 1: drie zuilen ----------------------------------------------------------
ZU = Prent("drie-zuilen", "Drie Griekse zuilen",
           "drie zuilen naast elkaar: A met een eenvoudig, vlak kapiteel en zonder voet; B met twee krullen aan het kapiteel en een voet; C met een kapiteel vol bladeren en een voet")
ZUIL = {}


def zuil(letter, x, voet=True):
    ZU.rect(x - 45, 200, 90, 320, "#f4f1e8", DONKER, 0, 3)
    for dx in (-25, -8, 8, 25):
        ZU.lijn(x + dx, 205, x + dx, 515, GRIJS, 2)
    if voet:
        ZU.rect(x - 65, 520, 130, 30, "#f4f1e8", DONKER, 4, 3)
    ZU.letter(x, 600, letter)
    ZUIL[letter] = (x - 90, 90, 180, 470)


zuil("A", 180, voet=False)
ZU.rect(110, 165, 140, 35, "#f4f1e8", DONKER, 0, 3)
ZU.rect(125, 150, 110, 15, "#f4f1e8", DONKER, 0, 3)
zuil("B", 500)
ZU.rect(430, 170, 140, 30, "#f4f1e8", DONKER, 0, 3)
ZU.cirkel(430, 190, 22, "#f4f1e8", DONKER, 3)
ZU.cirkel(430, 190, 9, "none", DONKER, 2)
ZU.cirkel(570, 190, 22, "#f4f1e8", DONKER, 3)
ZU.cirkel(570, 190, 9, "none", DONKER, 2)
zuil("C", 820)
ZU.pad("M 755 200 L 745 110 L 895 110 L 885 200 Z", "#f4f1e8", DONKER, 3)
for i, x in enumerate((765, 795, 825, 855, 880)):
    ZU.pad(f"M {x} 200 Q {x - 12} 160 {x + 4} 130 Q {x + 14} 165 {x + 8} 200", LICHTGROEN, DONKER, 2)

# Prent 2: twee staande figuren -----------------------------------------------
TF = Prent("twee-houdingen", "Twee staande beelden in schema",
           "A een stijve figuur, frontaal, schouders en heupen recht, armen tegen het lichaam, één voet iets naar voren; B een figuur met het gewicht op één been, de heup naar één kant gekanteld en de schouders tegengesteld")
FIG = {}


def lijf(x, kantel):
    # kantel > 0: heupen en schouders tegengesteld scheef
    sh = (x - 60, 210 - kantel, x + 60, 210 + kantel)
    hp = (x - 45, 360 + kantel, x + 45, 360 - kantel)
    TF.cirkel(x + kantel * 0.6, 150, 38, "#efe6d2", DONKER, 3)
    TF.pad(f"M {sh[0]} {sh[1]} L {sh[2]} {sh[3]} L {hp[2]} {hp[3]} L {hp[0]} {hp[1]} Z", "#efe6d2", DONKER, 3)
    TF.lijn(sh[0] - 20, sh[1] - kantel / 3, sh[2] + 20, sh[3] + kantel / 3, ORANJE, 3, stippel=True)
    TF.lijn(hp[0] - 20, hp[1] + kantel / 2, hp[2] + 20, hp[3] - kantel / 2, ORANJE, 3, stippel=True)
    return sh, hp


sh, hp = lijf(270, 0)
TF.lijn(sh[0], sh[1] + 5, sh[0] - 5, 350, DONKER, 12)
TF.lijn(sh[2], sh[3] + 5, sh[2] + 5, 350, DONKER, 12)
TF.lijn(hp[0] + 15, hp[1], 245, 560, DONKER, 14)
TF.lijn(hp[2] - 15, hp[3], 310, 580, DONKER, 14)
TF.letter(270, 610, "A")
FIG["A"] = (150, 90, 240, 500)

sh, hp = lijf(720, 14)
TF.lijn(sh[0], sh[1] + 5, sh[0] - 25, 340, DONKER, 12)
TF.lijn(sh[2], sh[3] + 5, sh[2] + 10, 330, DONKER, 12)
TF.lijn(hp[2] - 15, hp[3], 750, 575, DONKER, 14)
TF.lijn(hp[0] + 15, hp[1], 665, 560, DONKER, 14)
TF.letter(720, 610, "B")
FIG["B"] = (600, 90, 240, 500)


def zz(l):
    return [Prent.zone(*ZUIL[l])]


def fz(l):
    return [Prent.zone(*FIG[l])]


VRAGEN = [
    klik("Klik op de zuil in de Dorische orde.", ZU.bestand, zz("A"),
         "De Dorische orde is de soberste: een eenvoudig kapiteel en geen voet onder de zuil."),
    klik("Klik op de zuil in de Korinthische orde.", ZU.bestand, zz("C"),
         "Het Korinthische kapiteel zit vol acanthusbladeren."),
    met_prent(ZU.bestand, keuze("Zuil B heeft krullen of voluten: dat is de [[*Ionische|Dorische|Korinthische]] orde. Het Parthenon in Athene is gebouwd in de [[*Dorische|Ionische|Korinthische]] orde.",
              "Dorisch is sober, Ionisch heeft voluten, Korinthisch acanthusbladeren.")),
    klik("Klik op het beeld in contrapposto.", TF.bestand, fz("B"),
         "Het gewicht rust op één been. Heupen en schouders kantelen tegengesteld."),
    met_prent(TF.bestand, keuze("Beeld A is stijf en frontaal, met de armen tegen het lichaam. Dat past bij [[*Egyptische|klassieke Griekse|Romeinse]] beeldhouwkunst en bij de vroegste Griekse beelden. Beeld B past bij de [[*klassieke Griekse|Egyptische|prehistorische]] beeldhouwkunst.",
              "De vroege Griekse beelden leken nog op de Egyptische. In de klassieke periode kwam het losse contrapposto.")),
    sorteer("Bij welke kunst hoort dit kenmerk?", ["prehistorie", "Egypte", "Griekenland", "Rome"], [
        ["jachtdieren op grotwanden in oker en houtskool", "prehistorie"],
        ["hoofd en benen van opzij, oog en schouders van voren", "Egypte"],
        ["een ideaal lichaam met perfecte verhoudingen", "Griekenland"],
        ["een realistisch portret met rimpels", "Rome"],
        ["een klein vrouwenbeeldje met grote buik en heupen", "prehistorie"],
        ["een koepel van beton met een opening bovenaan", "Rome"],
        ["de farao groter dan de andere mensen", "Egypte"],
        ["zuilen in Dorische, Ionische of Korinthische orde", "Griekenland"],
    ], "Elke periode heeft eigen vormelijke kenmerken die je bij een ongezien werk kunt herkennen."),
    koppel("Koppel het werk aan de kunstenaar of de periode.", [
        ["de Discuswerper", "Myron"],
        ["de Doryphoros of speerdrager", "Polykleitos"],
        ["het beeldhouwwerk van het Parthenon", "Phidias"],
        ["de Venus van Willendorf", "prehistorie"],
    ], ["Michelangelo"], "Michelangelo is een renaissancekunstenaar, veel later."),
    tabel("Klopt dit over Griekse en Egyptische kunst?", [
        ("Griekse beelden waren oorspronkelijk vaak beschilderd.", J),
        ("Veel Griekse bronzen beelden kennen we vooral via Romeinse kopieën in marmer.", J),
        ("Egyptische kunstenaars gebruikten een perspectief met één verdwijnpunt.", F),
        ("De Ishtarpoort is een Griekse tempel in Athene.", F),
    ], "Het perspectief met verdwijnpunt komt pas in de renaissance. De Ishtarpoort staat in Babylon, in het nabije Oosten."),
    casus(
        "In een museum zie je een ongezien reliëf. Een man met een hoge kroon is veel groter dan de mensen rondom hem. Alle figuren staan in rijen. "
        "Hun hoofd en benen zie je van opzij, maar het oog en de schouders van voren. Tussen de figuren staan kleine tekentjes van vogels, ogen en golflijnen.",
        [
            mk("Uit welke kunst komt dit reliëf wellicht?",
               ["Egyptische kunst", "Romeinse kunst", "Griekse kunst", "prehistorische kunst"], 0,
               "Aspectieve weergave, hiërarchische grootte en hiërogliefen wijzen op Egypte."),
            keuze("Dat de man met de kroon het grootst is, noem je een [[*hiërarchische|realistische|perspectivische]] weergave. De tekentjes zijn [[*hiërogliefen|grotschilderingen|voluten]].",
                  "De belangrijkste figuur is de grootste. Hiërogliefen zijn het Egyptische beeldschrift."),
            tabel("Is dit een kenmerk van de context of van de vorm?", [
                ("figuren van opzij met het oog van voren", "vorm"),
                ("het geloof in een leven na de dood", "context"),
                ("de figuren in rijen, strak en symmetrisch", "vorm"),
            ], "Basiskenmerken zijn context en vormelijke kenmerken.",
               kolommen=["vorm", "context"]),
        ],
    ),
    mk("Waarom staan er op prehistorische grotwanden vooral jachtdieren?",
       ["men denkt aan rituelen of magie rond de jacht", "de grotten waren winkels voor dierenhuiden",
        "het waren portretten van huisdieren", "dieren waren het enige wat in het donker te zien was"], 0,
       "Zeker weten we het niet, want er zijn geen geschreven bronnen."),
    mk("Wat is de functie van het Colosseum?",
       ["een amfitheater voor spelen en gevechten", "een grafmonument voor de keizer",
        "een tempel met een koepel voor alle goden", "een poort met blauwe tegels voor een stad"], 0,
       "Het Pantheon is de tempel met de koepel. De Ishtarpoort is de poort met tegels."),
    keuze("Het Pantheon in Rome heeft een enorme koepel van [[*beton|marmer|hout]] met bovenaan een ronde opening, het [[*oculus|kapiteel|reliëf]].",
          "Beton, bogen en koepels maakten grote Romeinse gebouwen mogelijk."),
    sleep("De Romeinen namen van de Grieken de [[bouworden]] over, maar bouwden zelf met de [[rondboog]] en de koepel.",
          ["spitsboog", "ziggoerat"], "De spitsboog is gotisch, de ziggoerat Mesopotamisch."),
    volgorde("Zet in de tijd, van oud naar jonger.", [
        "de grotschilderingen van Lascaux",
        "de piramiden van Gizeh",
        "het Parthenon in Athene",
        "het Colosseum in Rome",
    ], "Prehistorie, dan Egypte, dan de klassieke Griekse en daarna de Romeinse tijd."),
    inv("Hoe heet de trapvormige tempeltoren uit Mesopotamië?", ["ziggoerat", "ziggurat", "zigurat"],
        "Op de top stond een heiligdom voor de god van de stad."),
    inv("Hoe heet de houding met het gewicht op één been?", ["contrapposto"],
        "Contrapposto betekent tegenstelling: heupen en schouders kantelen tegengesteld."),
    tabel("Grieks of Romeins?", [
        ("een jonge atleet met een tijdloos, ideaal lichaam", "Grieks"),
        ("een borstbeeld van een oude senator met diepe rimpels", "Romeins"),
        ("een aquaduct met rijen rondbogen", "Romeins"),
        ("een tempel met Dorische zuilen op de Akropolis", "Grieks"),
    ], "Grieks: het ideaal. Romeins: realisme en grote, nuttige bouwwerken.",
       kolommen=["Grieks", "Romeins"]),
    mk("Welke context verklaart het best waarom Griekse beelden een ideaal menselijk lichaam tonen?",
       ["in Athene stonden de mens en de rede centraal", "de farao wilde na zijn dood eeuwig leven",
        "jagers wilden geluk bij de jacht op bizons en paarden", "de keizer wilde zijn grote rijk besturen"], 0,
       "Het ideale lichaam past bij het denken van de Griekse stadstaten."),
    mk("Waarom bleef de Egyptische kunst duizenden jaren opvallend gelijk?",
       ["vaste regels, en de kunst moest eeuwig zijn", "Egyptenaren kenden maar één soort verf en steen",
        "de priesters van de Nijl verboden elk nieuw beeld", "er waren in heel Egypte maar enkele kunstenaars"], 0,
       "Het streven naar eeuwigheid en vaste regels zorgden voor weinig verandering."),
    keuze("De Ishtarpoort van Babylon is bekleed met [[*blauwe geglazuurde bakstenen|witte marmeren platen|gouden mozaïeken]] met leeuwen, stieren en draken in [[*reliëf|perspectief|contrapposto]].",
          "De Ishtarpoort is een bekend werk uit het nabije Oosten."),
    tabel("Klopt dit over de prehistorie?", [
        ("Prehistorische mensen bliezen soms verf door een holle buis.", J),
        ("De Venus van Willendorf is een levensgroot marmeren beeld.", F),
        ("Uit de prehistorie bestaan geen geschreven bronnen.", J),
    ], "De Venus van Willendorf is maar zo'n 11 centimeter hoog."),
    mk("Je ziet een ongezien marmeren beeld: een jonge man in een losse houding, het gewicht op één been, met perfecte verhoudingen en een rustig gezicht. Wat past het best?",
       ["klassieke Griekse kunst", "Egyptische kunst van het Oude Rijk", "prehistorische kunst", "kunst van het nabije Oosten"], 0,
       "Contrapposto, het ideale lichaam en rust zijn typisch voor de klassieke Griekse beeldhouwkunst."),
    mk("Welk werk hoort niet bij de klassieke oudheid?",
       ["de Venus van Willendorf", "het Parthenon in Athene", "het Pantheon in Rome", "de Discuswerper van Myron"], 0,
       "De Venus van Willendorf is prehistorisch. De andere drie zijn Grieks of Romeins."),
    tabel("Hoort dit bij het Parthenon of bij het Pantheon?", [
        ("staat op de Akropolis in Athene", "Parthenon"),
        ("heeft een betonnen koepel met een oculus", "Pantheon"),
        ("beeldhouwwerk onder leiding van Phidias", "Parthenon"),
        ("Romeins bouwwerk", "Pantheon"),
    ], "Het Parthenon is Grieks, het Pantheon Romeins. De namen lijken op elkaar, de gebouwen niet.",
       kolommen=["Parthenon", "Pantheon"]),
    keuze("Prehistorische kunstenaars schilderden met [[*oker en houtskool|olieverf in tubes|acrylverf]]. Over hun bedoeling hebben we enkel [[*vermoedens|geschreven verslagen|brieven van de kunstenaars]].",
          "Prehistorie is de tijd vóór het schrift."),
    mk("Wat toont de grootte van de piramiden over de Egyptische samenleving?",
       ["de farao had macht over duizenden werkers", "elke Egyptenaar bouwde zijn eigen piramide",
        "de piramiden waren woningen voor gewone gezinnen", "de Egyptenaren wilden vooral toeristen lokken"], 0,
       "Kunst en bouwkunst tonen hier de macht van de farao en het geloof in het leven na de dood."),
    tabel("Welke Griekse orde zie je?", [
        ("een sober kapiteel, geen voet onder de zuil", "Dorisch"),
        ("twee krullen of voluten aan het kapiteel", "Ionisch"),
        ("een kapiteel vol acanthusbladeren", "Korinthisch"),
    ], "Van sober naar rijk versierd: Dorisch, Ionisch, Korinthisch.",
       kolommen=["Dorisch", "Ionisch", "Korinthisch"]),
    open_("Vergelijk een Egyptisch beeld met een klassiek Grieks beeld. Noem een verschil in vorm en een verschil in context.",
          "Vorm: een Egyptisch beeld is stijf, frontaal en symmetrisch, met de armen tegen het lichaam. Een klassiek Grieks beeld staat losser, in contrapposto, met een ideaal lichaam. Context: Egyptische kunst was gemaakt voor de eeuwigheid en het leven na de dood van de farao. Griekse kunst ontstond in stadstaten waar de mens en zijn verstand centraal stonden."),
]

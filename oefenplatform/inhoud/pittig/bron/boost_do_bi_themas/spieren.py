"""De spieren en de klieren — pittig (🚀 Boost doorstroom, biologie).

Pittige vragen van natuurwetenschappen Boost doorstroom (met de prenten van het sarcomeer en de glucosegrafiek) die binnen bi_spieren passen, plus eigen vragen over klieren met en zonder afvoergang, de hypofyse en de schildklier."""
from ..boost_do_nw_themas import spieren as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 16, 17, 18, 19, 22, 25, 26],
              {"Dwarsgestreepte spieren": "Skeletspieren", "Dwarsgestreept": "Skeletspier"})
VRAGEN += [
    sorteer("Klier met of zonder afvoergang?", ["Met afvoergang", "Zonder afvoergang"],
            [("de zweetklier", "Met afvoergang"), ("de schildklier", "Zonder afvoergang"), ("de traanklier", "Met afvoergang"), ("de hypofyse", "Zonder afvoergang"), ("de speekselklier", "Met afvoergang"), ("de bijnier", "Zonder afvoergang")],
            "Een klier zonder afvoergang geeft haar hormoon rechtstreeks aan het bloed; een klier met afvoergang brengt haar stof via een buisje naar buiten of naar een holte."),
    mk("Waarom noemt men de hypofyse de dirigent van de klieren?",
       ["Ze geeft hormonen die andere klieren aanzetten of afremmen.", "Ze maakt zelf alle hormonen die het lichaam nodig heeft.", "Ze is de grootste klier en ligt in het midden van de buik.", "Ze stuurt via zenuwen elke spier van het lichaam aan."], 0,
       "Ze regelt de andere klieren, zoals een dirigent het orkest."),
    casus("Na een lange fietstocht zonder eten voelt Jana zich slap en duizelig. Haar bloedglucosegehalte is gedaald.", [
        mk("Welke cellen worden nu actief?",
           ["de alfacellen, die glucagon afgeven", "de bètacellen, die insuline afgeven", "de cellen van de schildklier", "de motorische eindplaten in haar beenspieren"], 0,
           "Glucagon laat het bloedglucosegehalte weer stijgen."),
        tabel("Klopt dit over wat er bij Jana gebeurt?",
              [("Glucagon laat de lever glucose vrijgeven.", J), ("Insuline zou haar gehalte nog verder laten dalen.", J), ("Een feedbacksysteem probeert het gehalte binnen grenzen te houden.", J), ("Het hormoon werkt sneller dan een zenuwimpuls.", F)],
              "Homeostase: het lichaam stuurt bij tot de waarde weer klopt; hormonen werken trager dan zenuwen."),
    ]),
    tabel("Skeletspier, glad spierweefsel of hartspier?",
          [("werkt buiten je wil en is niet gestreept", "glad"), ("is gestreept en werkt buiten je wil", "hartspier"), ("is gestreept en stuur je met je wil", "skeletspier")],
          "De hartspier is gestreept als een skeletspier, maar werkt vanzelf zoals glad spierweefsel.", ["skeletspier", "glad", "hartspier"]),
    keuze("De klier in de hals die met haar hormoon de snelheid van de stofwisseling regelt, is de [[*schildklier|bijnier|hypofyse]].",
          "De schildklier regelt hoe snel je cellen energie verbruiken."),
    mk("Je houdt een zware tas lang in een gestrekte arm. Na een tijd begint je arm te trillen. Waarom?",
       ["De spiervezels raken uitgeput en wisselen elkaar af.", "De pees laat los van het bot en schiet terug.", "Het gladde spierweefsel neemt het werk over.", "De schildklier geeft te veel hormoon af in je arm."], 0,
       "Uitgeputte vezels haken af; anderen nemen het over, en dat zie je als trillen."),
]

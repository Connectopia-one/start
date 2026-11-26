# -*- coding: utf-8 -*-
"""Ready aardrijkskunde: De wereld (werelddelen, oceanen, wereldbol en evenaar,
klimaat: warm, koud, droog en nat; leven elders). Doelen einde 4de leerjaar."""
from vr import mk, inv, wn

TITEL = "De wereld"
UITLEG_1 = "Werelddelen en oceanen."
UITLEG_2 = "Warm en koud, nat en droog: leven op aarde."

DEEL_1 = [
    mk("In welk werelddeel ligt België?", ["Europa", "Afrika", "Azië", "Amerika"], 0, "België ligt in Europa."),
    inv("Hoeveel werelddelen zijn er? ___", "6", "Europa, Azië, Afrika, Amerika, Oceanië en Antarctica: zes werelddelen. Soms telt men Noord- en Zuid-Amerika apart.", 6),
    mk("Welk werelddeel is het grootst?", ["Azië", "Europa", "Oceanië", "Antarctica"], 0, "Azië is het grootste werelddeel, met landen zoals China en India."),
    mk("Wat is de grootste oceaan?", ["de Stille Oceaan", "de Atlantische Oceaan", "de Indische Oceaan", "de Noordzee"], 0, "De Stille Oceaan ligt tussen Amerika en Azië."),
    wn("De aarde is voor het grootste deel bedekt met water.", True, "Ongeveer 7 van de 10 delen van de aarde zijn water."),
    mk("Welk werelddeel ligt rond de zuidpool en is bedekt met ijs?", ["Antarctica", "Afrika", "Europa", "Azië"], 0, "Antarctica is het koudste werelddeel."),
    mk("Welke oceaan ligt tussen Europa en Amerika?", ["de Atlantische Oceaan", "de Stille Oceaan", "de Indische Oceaan", "de Noordelijke IJszee"], 0, "Wie van België naar Amerika vliegt, vliegt over de Atlantische Oceaan."),
    inv("De denkbeeldige lijn rond het midden van de aarde heet de ___. (e...)", ["evenaar"], "De evenaar verdeelt de aarde in een noordelijke en een zuidelijke helft."),
    wn("Australië ligt in Oceanië.", True, "Australië is het grootste land van Oceanië."),
    mk("In welk werelddeel ligt Egypte?", ["Afrika", "Azië", "Europa", "Amerika"], 0, "Egypte ligt in het noordoosten van Afrika, aan de Nijl."),
    wn("China ligt in Europa.", False, "China ligt in Azië."),
    mk("In welk werelddeel ligt Brazilië?", ["Zuid-Amerika", "Afrika", "Europa", "Noord-Amerika"], 0, "Brazilië is het grootste land van Zuid-Amerika."),
    mk("Waarop zie je de hele aarde rond?", ["een wereldbol", "een stadsplan", "een plattegrond van de school", "een thermometer"], 0, "Een wereldbol is rond, net zoals de aarde."),
    wn("Op een wereldkaart zie je de hele aarde in één keer, plat.", True, "Een wereldkaart is de aarde plat getekend."),
    inv("Het koude gebied helemaal boven op de aarde heet de ___pool.", ["noord", "noordpool"], "De noordpool ligt bovenaan, de zuidpool onderaan."),
    mk("Welk land is een buurland van België en ligt ook in Europa?", ["Frankrijk", "Canada", "Japan", "Kenia"], 0, "Frankrijk ligt in Europa, naast België."),
    wn("Afrika is kleiner dan Europa.", False, "Afrika is veel groter dan Europa."),
    mk("Wat is een continent?", ["een werelddeel", "een lange rivier", "een stad", "een berg"], 0, "Continent is een ander woord voor werelddeel."),
    wn("Er leven pinguïns op Antarctica.", True, "Pinguïns leven in het zuiden, onder andere op Antarctica."),
    wn("De evenaar loopt door België.", False, "De evenaar loopt veel zuidelijker, onder meer door Afrika en Zuid-Amerika."),
]

DEEL_2 = [
    mk("Waar is het het hele jaar warm?", ["dicht bij de evenaar", "aan de noordpool", "op de zuidpool", "hoog in de bergen"], 0, "Bij de evenaar staat de zon hoog en is het altijd warm."),
    mk("Hoe noem je een gebied waar bijna nooit regen valt?", ["een woestijn", "een regenwoud", "een moeras", "een meer"], 0, "In een woestijn is het heel droog."),
    wn("In een tropisch regenwoud regent het veel en is het warm.", True, "Regenwouden liggen dicht bij de evenaar."),
    mk("Welk dier leeft in de woestijn?", ["een kameel", "een ijsbeer", "een pinguïn", "een walrus"], 0, "Een kameel kan lang zonder water."),
    mk("Welk dier leeft in het koude noordpoolgebied?", ["een ijsbeer", "een kameel", "een giraf", "een papegaai"], 0, "Een ijsbeer heeft een dikke vacht tegen de kou."),
    inv("De Sahara is de grootste hete ___ van de wereld. (w...)", ["woestijn"], "De Sahara ligt in het noorden van Afrika."),
    wn("In België hebben we vier seizoenen.", True, "Lente, zomer, herfst en winter."),
    mk("Hoe is het klimaat in België?", ["gematigd", "het hele jaar door heel heet", "altijd ijskoud", "altijd droog"], 0, "België heeft een gematigd klimaat met regen in elk seizoen."),
    wn("Overal op de wereld is het op hetzelfde moment winter.", False, "Als het bij ons winter is, is het in Australië zomer."),
    mk("Waarom bouwen mensen in warme landen vaak huizen met witte muren?", ["Wit kaatst de zon terug en houdt het huis koel.", "Wit is goedkoper.", "Wit zie je in het donker.", "Wit is verplicht."], 0, "Een witte muur wordt minder warm in de zon."),
    inv("Een hoge berg heeft bovenaan vaak ___, ook in de zomer. (s...)", ["sneeuw"], "Hoe hoger je komt, hoe kouder het wordt."),
    wn("Hoe hoger je in de bergen komt, hoe warmer het wordt.", False, "Hoe hoger, hoe kouder."),
    mk("Hoe heet het hoogste gebergte van de wereld?", ["de Himalaya", "de Ardennen", "de Alpen", "de Pyreneeën"], 0, "In de Himalaya ligt de Mount Everest, de hoogste berg op aarde."),
    mk("Hoe heet een gebergte in Europa waar veel mensen gaan skiën?", ["de Alpen", "de Sahara", "de Amazone", "de Nijl"], 0, "De Alpen liggen onder meer in Zwitserland, Oostenrijk, Frankrijk en Italië."),
    wn("De Amazone is een grote rivier in Zuid-Amerika.", True, "De Amazone stroomt door het grootste regenwoud van de wereld."),
    mk("Wat dragen mensen in een heel koud land?", ["dikke, warme kleren", "korte broeken en T-shirts", "badpakken", "sandalen"], 0, "Warme kleren houden je lichaamswarmte vast."),
    inv("De langste rivier van Afrika heet de ___. (N...)", ["Nijl"], "De Nijl stroomt door Egypte naar de Middellandse Zee."),
    wn("Kinderen overal op de wereld gaan op dezelfde manier naar school.", False, "Sommige kinderen gaan te voet, met de boot of zelfs op een ezel. Elk land is anders."),
    mk("Waarom wonen er weinig mensen in de woestijn?", ["Er is weinig water.", "Er is te veel sneeuw.", "Er zijn te veel bomen.", "Er is te veel regen."], 0, "Zonder water kunnen mensen, dieren en planten moeilijk leven."),
    wn("Een regenwoud is een goede plek voor veel verschillende dieren en planten.", True, "In regenwouden leven meer soorten dan waar ook op aarde."),
]

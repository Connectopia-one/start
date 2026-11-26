# -*- coding: utf-8 -*-
"""Ready aardrijkskunde: Kaarten lezen (plattegrond, legende, windrichtingen, kompas,
schaal in eenvoudige vorm, routes beschrijven). Doelen einde 4de leerjaar."""
from vr import mk, inv, wn

TITEL = "Kaarten lezen"
UITLEG_1 = "Een plattegrond is een kaart van bovenaf."
UITLEG_2 = "Noord, oost, zuid en west, en de weg vinden."

DEEL_1 = [
    mk("Wat is een plattegrond?", ["een tekening van bovenaf", "een foto van de zijkant van een huis", "een schilderij van een huis", "een lijst met namen van straten"], 0, "Op een plattegrond kijk je van boven naar beneden, zoals een vogel."),
    mk("Hoe heet het lijstje dat uitlegt wat de tekentjes op een kaart betekenen?", ["de legende", "de titel", "het register", "de inhoud"], 0, "In de legende staat bijvoorbeeld: blauw = water, groen = bos."),
    wn("Op een kaart is water meestal blauw.", True, "Rivieren, meren en de zee kleur je blauw."),
    mk("Welke kleur heeft een bos meestal op een kaart?", ["groen", "rood", "blauw", "geel"], 0, "Groen staat vaak voor bos of park."),
    inv("Een plattegrond van je klas teken je zoals je hem ziet van ___. (b...)", ["boven", "bovenaf"], "Van bovenaf zie je de tafels als rechthoeken."),
    wn("Op een plattegrond zie je de daken en niet de muren van de zijkant.", True, "Je kijkt van bovenaf, dus je ziet de bovenkant."),
    mk("Hoe ziet een ronde tafel eruit op een plattegrond?", ["als een cirkel", "als een vierkant", "als een driehoek", "als een lijn"], 0, "Van boven zie je de ronde vorm van het tafelblad."),
    wn("Een kaart is altijd even groot als de echte plaats.", False, "Een kaart is veel kleiner. Alles wordt verkleind getekend."),
    mk("Waarom zet men op een kaart tekentjes in plaats van foto's?", ["Zo blijft de kaart duidelijk.", "Omdat foto's op kaarten verboden zijn.", "Omdat tekentjes duurder zijn.", "Omdat niemand foto's kan maken."], 0, "Kleine tekentjes maken een kaart overzichtelijk."),
    inv("Hoe heet een boek vol kaarten? Een ___. (a...)", ["atlas"], "In een atlas vind je kaarten van België en de hele wereld."),
    mk("Wat toont een stadsplan?", ["de straten van een stad", "de sterren aan de hemel", "het weer van morgen", "de bloemen in je tuin"], 0, "Met een stadsplan vind je je weg in een stad."),
    wn("Een wereldbol is een ronde kaart van de aarde.", True, "Een globe of wereldbol toont de aarde zoals ze echt is: rond."),
    mk("Welk tekentje gebruik je vaak voor een kerk op een kaart?", ["een kruisje", "een vis", "een boom", "een golflijn"], 0, "Een kruisje staat vaak voor een kerk."),
    wn("De legende staat altijd in het midden van de kaart.", False, "De legende staat meestal in een hoek of naast de kaart."),
    mk("Wat zie je op een kaart als een dikke rode of gele lijn?", ["een grote weg", "een rivier", "een bos", "een meer"], 0, "Grote wegen en autosnelwegen tekent men vaak met kleur en dikke lijnen."),
    inv("Een kaart toont alles kleiner. Dat noem je ver___. (k...)", ["kleind", "verkleind"], "Alles wordt even veel verkleind, zodat de kaart klopt."),
    wn("Op een plattegrond van je kamer kan je je bed tekenen als een rechthoek.", True, "Van bovenaf is een bed een rechthoek."),
    mk("Wat heb je het best nodig om op een wandeling in het bos je weg te vinden?", ["een wandelkaart", "een kookboek", "een woordenboek", "een strip"], 0, "Op een wandelkaart staan de paden."),
    wn("Een gsm kan ook een kaart tonen.", True, "Met een kaartenapp zie je waar je bent."),
    wn("Op een kaart worden huizen getekend zoals je ze van voren ziet.", False, "Op een kaart kijk je van bovenaf."),
]

DEEL_2 = [
    mk("Wat zijn de vier windrichtingen?", ["noord, oost, zuid, west", "links, rechts, voor, achter", "boven, onder, binnen, buiten", "dag, nacht, ochtend, avond"], 0, "Noord, oost, zuid en west. Onthoud: Nooit Oost Zonder Wortelen."),
    mk("Waar is het noorden meestal op een kaart?", ["bovenaan", "onderaan", "links", "rechts"], 0, "Op de meeste kaarten wijst het noorden naar boven."),
    wn("Op een kaart met het noorden boven is het oosten rechts.", True, "Noord boven, oost rechts, zuid onder, west links."),
    inv("Als het noorden boven is, dan is het westen ___.", ["links"], "West staat links, oost rechts."),
    mk("Welk toestel wijst altijd naar het noorden?", ["een kompas", "een thermometer", "een klok", "een weegschaal"], 0, "De naald van een kompas wijst naar het noorden."),
    mk("In welke richting komt de zon 's morgens op?", ["in het oosten", "in het westen", "in het noorden", "in het zuiden"], 0, "De zon komt op in het oosten en gaat onder in het westen."),
    wn("De zon gaat onder in het oosten.", False, "De zon gaat onder in het westen."),
    mk("Brugge ligt links van Brussel op de kaart. In welke richting ligt Brugge dan van Brussel uit?", ["het westen", "het oosten", "het noorden", "het zuiden"], 0, "Links op de kaart is het westen."),
    inv("Tussen noord en oost ligt het ___. (n... o...)", ["noordoosten", "noordoost"], "Tussen noord en oost: noordoost."),
    wn("Nederland ligt ten noorden van België.", True, "Op de kaart ligt Nederland boven België."),
    mk("Welk land ligt ten zuiden van België?", ["Frankrijk", "Nederland", "Engeland", "Noorwegen"], 0, "Frankrijk ligt onder België op de kaart."),
    mk("Je loopt naar het noorden en draait rechtsom. Naar waar loop je nu?", ["het oosten", "het westen", "het zuiden", "het noorden"], 0, "Na noord komt rechtsom oost."),
    wn("Een routebeschrijving vertelt hoe je ergens geraakt.", True, "Bijvoorbeeld: ga rechtdoor, dan de tweede straat links."),
    mk("Op een rooster staat de school in vak C2 en het park in vak C4. Wat is waar?", ["Ze liggen in dezelfde kolom.", "Ze liggen in dezelfde rij.", "Ze liggen in hetzelfde vak.", "Ze liggen in verschillende landen."], 0, "Allebei kolom C, maar een andere rij."),
    inv("Op een kaart met een schaal staat: 1 cm = 1 km. Twee plaatsen liggen 3 cm uit elkaar. In het echt is dat ___ km.", "3", "Elke cm op de kaart is 1 km in het echt: 3 km.", 3),
    wn("De zee ligt in het oosten van België.", False, "De Belgische kust ligt in het westen, aan de Noordzee."),
    mk("Waarom wijst de naald van een kompas naar het noorden?", ["De aarde werkt als een grote magneet.", "De wind duwt ze.", "Ze is zo vastgelijmd.", "Er zit een batterij in."], 0, "De naald is een kleine magneet die zich richt naar de magnetische noordpool."),
    wn("Op elke kaart staat het noorden onderaan.", False, "Meestal staat het noorden bovenaan. Soms toont een pijltje met een N waar het noorden is."),
    mk("Wat betekent een pijltje met een N op een kaart?", ["Daar is het noorden.", "Daar is een nooduitgang.", "Daar is niets.", "Daar is een nieuwe straat."], 0, "De N wijst naar het noorden."),
    wn("In het zuiden van België liggen de Ardennen.", True, "De Ardennen liggen in het zuiden en zuidoosten van België."),
]

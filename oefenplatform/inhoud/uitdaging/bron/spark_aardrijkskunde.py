# -*- coding: utf-8 -*-
"""Uitdaging aardrijkskunde ✨ Spark (11 november 2026), in de vormen van het
examen van de Examencommissie: 30 vragen die alle hoofdstukken door elkaar
halen, met een tabel, keuzelijsten, slepen, koppelen, sorteren, volgorde,
twee klikvragen op een zelf getekende prent, een casus en een open vraag.

Geen nieuwe leerstof: alles staat in de leerbundels van aardrijkskunde Spark.
De prenten tekent inhoud/uitdaging/maak_prenten_spark_aardrijkskunde.py.
"""
NIVEAU = "spark"
VAK = "Aardrijkskunde"
BESTAND = "spark-aardrijkskunde-uitdaging.json"
AANTAL = 30
J, F = True, False
MAP = "/examenvormen/aardrijkskunde-spark"


def mk(vraag, opties, plaats, uitleg):
    """opties[0] is het juiste antwoord; plaats is waar het komt te staan."""
    rest = list(opties[1:])
    rest.insert(plaats, opties[0])
    return {"type": "meerkeuze", "vraag": vraag, "opties": rest, "antwoord": plaats, "uitleg": uitleg}


def iv(vraag, antwoord, uitleg):
    return {"type": "invultekst", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def wn(vraag, antwoord, uitleg):
    return {"type": "waarofniet", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def tabel(vraag, rijen, uitleg):
    return {"type": "tabel", "vraag": vraag, "rijen": [r for r, _ in rijen], "antwoord": [a for _, a in rijen], "uitleg": uitleg}


def keuze(vraag, uitleg):
    return {"type": "keuzelijst", "vraag": vraag, "uitleg": uitleg}


def volgorde(vraag, stappen, uitleg):
    return {"type": "volgorde", "vraag": vraag, "opties": stappen, "uitleg": uitleg}


def koppel(vraag, paren, extra, uitleg):
    return {"type": "koppelen", "vraag": vraag, "paren": paren, "extra": extra, "uitleg": uitleg}


def sorteer(vraag, kolommen, items, uitleg):
    return {"type": "sorteren", "vraag": vraag, "kolommen": kolommen, "items": items, "uitleg": uitleg}


def sleep(vraag, extra, uitleg):
    return {"type": "sleepzin", "vraag": vraag, "extra": extra, "uitleg": uitleg}


def klik(vraag, prent, zones, uitleg):
    return {"type": "hotspot", "vraag": vraag, "afbeelding_url": f"{MAP}/{prent}", "zones": zones, "uitleg": uitleg}


def open_(vraag, voorbeeld, uitleg=None):
    v = {"type": "open", "vraag": vraag, "antwoord": voorbeeld}
    if uitleg:
        v["uitleg"] = uitleg
    return v


def casus(tekst, vragen):
    return {"casus": tekst, "vragen": vragen}


VRAGEN = [
    mk("Op een kaart met schaal 1 : 25 000 meet je 4 cm tussen twee kerken. Hoe ver liggen ze in werkelijkheid uit elkaar?",
       ["1 km", "100 m", "10 km", "400 m"], 2,
       "Bij 1 : 25 000 is 1 cm op de kaart 250 m in het echt. 4 keer 250 m is 1000 m, dus 1 km."),
    tabel("Lees elke uitspraak over kaarten. Is ze juist of fout?",
          [("Een plan toont een klein gebied met veel details.", J),
           ("Bij schaal 1 : 100 000 is 1 cm op de kaart 1 km in het echt.", J),
           ("Hoogtelijnen die ver uit elkaar liggen, wijzen op een steile helling.", F),
           ("Een bochtige weg meet je het best met een touwtje.", J),
           ("Een luchtfoto heeft altijd een legende die de tekens uitlegt.", F)],
          "Lijnen ver uiteen betekent een flauwe helling, dicht bijeen een steile. Een luchtfoto toont het gebied zoals het is en heeft geen legende; een kaart toont tekens en heeft er wel een."),
    klik("Klik op de plaats waar de helling van deze heuvel het steilst is.",
         "hoogtelijnen-heuvel.svg", [[13, 30, 14, 40]],
         "Aan de westkant liggen de hoogtelijnen het dichtst bij elkaar. Daar overbrug je dezelfde 10 meter hoogte over de kortste afstand, dus is het daar het steilst."),
    wn("Twee hoogtelijnen van 20 m en 30 m kunnen elkaar kruisen als een helling heel steil is.", F,
       "Hoogtelijnen kruisen elkaar nooit. Een punt kan niet tegelijk 20 m en 30 m hoog liggen."),
    mk("Een plaats ligt op 50° N en 5° O. Welke uitspraak klopt?",
       ["Ze ligt op het noordelijk halfrond, ten oosten van de nulmeridiaan.",
        "Ze ligt op het zuidelijk halfrond, ten oosten van de nulmeridiaan.",
        "Ze ligt op het noordelijk halfrond, ten westen van de nulmeridiaan.",
        "Ze ligt op de evenaar, ten oosten van de datumlijn."], 1,
       "Eerst komt de breedte: 50° N is ten noorden van de evenaar. Dan de lengte: 5° O is ten oosten van de nulmeridiaan door Greenwich. Zo ligt ongeveer België."),
    keuze("België ligt op het [[*noordelijk|zuidelijk]] halfrond, in het werelddeel [[*Europa|Afrika|Azië]]. Tussen Europa en Amerika ligt de [[*Atlantische Oceaan|Stille Oceaan|Indische Oceaan]].",
          "België ligt op ongeveer 50° noorderbreedte, in Europa. De Atlantische Oceaan scheidt Europa van Amerika."),
    mk("Je staat rond de middag in Vlaanderen met de zon recht voor je. Welke kant kijk je uit?",
       ["het zuiden", "het noorden", "het oosten", "het westen"], 3,
       "Rond de middag staat de zon bij ons in het zuiden."),
    mk("Je kaart ligt voor je, maar de noordpijl wijst niet naar het noorden. Wat doe je eerst?",
       ["Ik draai de kaart tot de noordpijl naar het noorden wijst.",
        "Ik lees de kaart gewoon zoals hij nu voor me ligt.",
        "Ik draai mezelf tot ik naar het zuiden kijk.",
        "Ik zoek op de kaart eerst de legende en de schaal."], 0,
       "Een kaart oriënteren betekent ze draaien tot de noordpijl naar het echte noorden wijst. Pas dan klopt links en rechts op de kaart met het terrein."),
    keuze("Een aardbeving ontstaat diep in de grond, in de [[*haard|krater|delta]]. Het punt recht daarboven aan het oppervlak heet het [[*epicentrum|magma|transect]].",
          "De haard ligt in de diepte, het epicentrum aan het oppervlak er recht boven. Een krater hoort bij een vulkaan, een delta bij een rivier."),
    sleep("Water bevriest in een barst en zet uit: dat is [[vorstverwering]]. Stromend water voert het losse materiaal weg: dat is [[erosie]]. Waar de rivier traag stroomt, zet ze het af: dat is [[sedimentatie]].",
          ["irrigatie", "verharding", "vulkanisme"],
          "Verwering breekt ter plaatse af, erosie voert weg en sedimentatie zet elders af."),
    mk("Een rivier slijt hoog in de bergen een dal uit en zet zand af aan haar monding. Welke twee processen zie je hier, in die volgorde?",
       ["erosie en daarna sedimentatie", "sedimentatie en daarna erosie",
        "verwering en daarna irrigatie", "vulkanisme en daarna verwering"], 1,
       "Eerst voert de rivier materiaal weg (erosie), verderop zet ze het af waar ze traag stroomt (sedimentatie). Zo ontstaat ook een delta."),
    wn("Een gletsjer slijpt een U-vormig dal uit, een rivier een V-vormig dal.", J,
       "Bewegend ijs schuurt een breed dal met steile wanden uit; een rivier snijdt een smal V-dal."),
    koppel("Koppel elk meettoestel aan wat het meet.",
           [["Thermometer", "de temperatuur in graden Celsius"],
            ["Barometer", "de luchtdruk in hectopascal"],
            ["Regenmeter", "de neerslag in millimeter"],
            ["Anemometer", "de wind"]],
           ["de trillingen van een aardbeving"],
           "De trillingen van een aardbeving meet je met een seismograaf, en dat is geen weertoestel."),
    iv("In een regenmeter staat na een bui 12 millimeter water. Hoeveel liter regen viel er op 1 vierkante meter? Antwoord met een getal.", "12",
       "1 millimeter neerslag is 1 liter per vierkante meter. 12 millimeter is dus 12 liter."),
    wn("Een weerkaart toont boven België een gebied met hoge luchtdruk. Dan verwacht je eerder rustig en droog weer dan regen.", J,
       "Bij hoge druk zakt de lucht en vormen zich weinig wolken. Bij lage druk stijgt de lucht en krijg je wolken en regen."),
    casus("Hieronder staat het klimatogram van een plaats in West-Europa. De rode lijn is de temperatuur, de blauwe staafjes zijn de neerslag. In januari is het er gemiddeld 3 °C, in juli en augustus 19 °C. Er valt elke maand neerslag, tussen 48 en 96 millimeter.",
          [klik("Klik in het klimatogram op de droogste maand.",
                "klimatogram-west-europa.svg", [[31.2, 12.0, 7.1, 76.0]],
                "De droogste maand heeft het kortste staafje. Dat is april (A), met ongeveer 48 millimeter."),
           iv("Hoeveel graden verschil is er tussen de warmste en de koudste maand? Antwoord met een getal.", "16",
              "De warmste maanden zijn 19 °C, de koudste 3 °C. 19 min 3 is 16."),
           mk("In welke klimaatzone ligt deze plaats het waarschijnlijkst?",
              ["gematigd", "warm", "koud"], 1,
              "Zachte winters boven nul, zomers rond 19 °C en het hele jaar neerslag: dat is een gematigd klimaat, zoals in België.")]),
    sorteer("Is dit een natuurlijke of een menselijke laag van het landschap?",
            ["Natuurlijk", "Menselijk"],
            [["het reliëf", "Natuurlijk"], ["de bodem", "Natuurlijk"], ["de vegetatie", "Natuurlijk"],
             ["het klimaat", "Natuurlijk"], ["de bebouwing", "Menselijk"], ["de transportwegen", "Menselijk"],
             ["het landgebruik", "Menselijk"], ["de ontginning", "Menselijk"]],
            "Reliëf, klimaat, water, bodem, ondergrond en vegetatie zijn er van nature. Landgebruik, bebouwing, transportwegen en ontginning komen van de mens."),
    mk("Waarom liggen veel oude dorpskernen op een lichte hoogte?",
       ["Daar bleef het droger bij regen", "Daar was de bodem vruchtbaarder",
        "Daar waaide meer wind voor molens", "Daar lag de rivier dichterbij"], 2,
       "Water loopt naar lager gelegen grond. Op een lichte hoogte bleven de huizen droog."),
    iv("Hoeveel vierkante meter is 2,5 hectare? Antwoord met een getal.", ["25000", "25 000", "25.000"],
       "Eén hectare is 10 000 vierkante meter. 2,5 keer 10 000 is 25 000."),
    mk("Een land heeft 2 miljoen inwoners op 100 000 vierkante kilometer. Wat is de bevolkingsdichtheid?",
       ["20 inwoners per km²", "200 inwoners per km²", "2 inwoners per km²", "50 inwoners per km²"], 0,
       "Bevolkingsdichtheid is het aantal inwoners gedeeld door de oppervlakte: 2 000 000 gedeeld door 100 000 is 20."),
    iv("Hoe heet het hoogste punt van België? Vul aan: het Signaal van ...", "Botrange",
       "Het Signaal van Botrange (694 m) ligt op het Plateau van de Hoge Venen, in het zuidoosten van België."),
    volgorde("Zet de stappen van een onderzoek met kaartlagen in de juiste volgorde.",
             ["Een onderzoeksvraag stellen", "De juiste kaartlagen kiezen",
              "De lagen analyseren en vergelijken", "Een besluit schrijven en je bronnen noemen"],
             "Eerst de vraag, dan de lagen kiezen, dan analyseren, en tot slot besluiten: het antwoord, waarop je het baseert en of je hypothese klopte."),
    mk("Op een kaart vallen overstromingen vaak samen met sterk verharde wijken. Wat mag je daaruit besluiten?",
       ["Het is een aanwijzing, geen bewijs.", "De verharding is zeker de oorzaak.",
        "Er kan geen enkel verband zijn.", "De kaart bevat vast een fout."], 3,
       "Samenvallen op de kaart is een aanwijzing, geen bewijs van oorzaak en gevolg. Daarvoor moet je verder onderzoeken."),
    wn("Als drijvend zee-ijs smelt, stijgt de zeespiegel daar nauwelijks door.", J,
       "Drijvend ijs verplaatst al evenveel water als het smeltwater inneemt. De zeespiegel stijgt door ijs dat op het land smelt en doordat warmer water uitzet."),
    wn("Steenkool, aardolie en aardgas zijn hernieuwbare energiebronnen.", F,
       "Het zijn fossiele brandstoffen. Ze raken op en geven bij verbranding CO2. Wind, zon en waterkracht zijn hernieuwbaar."),
    mk("Welke keuze vermindert de uitstoot van CO2?",
       ["met de fiets naar school gaan in plaats van met de auto",
        "een extra rijstrook aanleggen op de drukke snelweg",
        "de verwarming in de klas een graad hoger zetten",
        "meer rundvlees eten van boerderijen uit de streek"], 1,
       "Een fiets verbrandt geen brandstof. Meer rijstroken trekken meer auto's aan, warmer stoken vraagt meer energie, en veeteelt geeft het broeikasgas methaan."),
    wn("De Heuvelruggen van de Condroz zijn vlak, net zoals een plateau.", F,
       "In de Condroz wisselen ruggen en dalen elkaar af. Een plateau ligt hoog en is wel vlak."),
    open_("Leg in twee stappen uit waarom een volledig verharde tuin of speelplaats de kans op wateroverlast vergroot.",
          "Stap 1: op verharding kan regenwater niet in de bodem sijpelen. Stap 2: al dat water stroomt in één keer naar de riolering en de lager gelegen plaatsen, die het niet snel genoeg kunnen afvoeren. Ontharden of een wadi helpt het water weer insijpelen.",
          "Verharding sluit de bodem af. Ontharding opent hem weer, en een wadi laat regenwater insijpelen."),
]

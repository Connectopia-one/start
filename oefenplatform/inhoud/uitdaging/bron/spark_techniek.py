# -*- coding: utf-8 -*-
"""Uitdaging techniek ✨ Spark (11 november 2026), in de vormen van het examen
van de Examencommissie: 30 vragen die alle hoofdstukken door elkaar halen, met
een casus over een nachtlampje, een tabel, een keuzelijst, slepen, koppelen,
sorteren, volgorde, twee klikvragen op een zelf getekende prent (tandwielen en
rekjes) en een open vraag. Geen nieuwe leerstof.
De prenten tekent inhoud/uitdaging/maak_prenten_spark_techniek.py.
"""
NIVEAU = "spark"
VAK = "Techniek"
BESTAND = "spark-techniek-uitdaging.json"
AANTAL = 30
J, F = True, False
MAP = "/examenvormen/techniek-spark"


def mk(vraag, opties, plaats, uitleg):
    """opties[0] is het juiste antwoord; plaats is waar het komt te staan."""
    rest = list(opties[1:])
    rest.insert(plaats, opties[0])
    return {"type": "meerkeuze", "vraag": vraag, "opties": rest, "antwoord": plaats, "uitleg": uitleg}


def iv(vraag, antwoord, uitleg):
    return {"type": "invultekst", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def wn(vraag, antwoord, uitleg):
    return {"type": "waarofniet", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}


def tabel(vraag, rijen, uitleg, kolommen=None):
    v = {"type": "tabel", "vraag": vraag, "rijen": [r for r, _ in rijen], "antwoord": [a for _, a in rijen], "uitleg": uitleg}
    if kolommen:
        # antwoorden als kolomnummer, zoals bij de pittige hoofdstukken
        v["kolommen"] = kolommen
        v["antwoord"] = [kolommen.index(a) for a in v["antwoord"]]
    return v


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
    casus("Noor bouwt een nachtlampje voor haar kamer. Het lampje moet vanzelf aangaan als het donker wordt en mag maar weinig stroom verbruiken. Ze gebruikt een batterij van 9 volt, een lichtsensor, een kleine chip die beslist, een LED en een weerstand. Het kastje maakt ze uit hout. De onderdelen schroeft ze vast, zodat ze de batterij later kan vervangen.",
          [sorteer("Is dit onderdeel van het nachtlampje input, verwerking of output?",
                   ["Input", "Verwerking", "Output"],
                   [["de lichtsensor", "Input"], ["een drukknop om het lampje aan te zetten", "Input"],
                    ["de chip die beslist of het donker is", "Verwerking"], ["de LED", "Output"]],
                   "Een sensor of druktoets geeft input, de chip verwerkt, en de LED doet iets: dat is de output, de actuator."),
           mk("Waarom zit er een weerstand bij de LED?",
              ["Hij remt de stroom, zodat de LED niet stukgaat.", "Hij maakt de stroom sterker, zodat het fel brandt.",
               "Hij zet de gelijkspanning om in wisselspanning.", "Hij meet hoeveel licht er in de kamer is."], 3,
              "Een weerstand remt de stroom. Zonder weerstand loopt er te veel stroom door de LED en brandt ze door."),
           wn("De batterij van Noor levert wisselspanning.", F,
              "Een batterij is een gelijkspanningsbron. Een generator levert wisselspanning."),
           mk("Waarom schroeft Noor de onderdelen vast in plaats van ze te lijmen?",
              ["Een schroef kan je later weer losmaken.", "Lijm houdt niet op hout.", "Schroeven geleiden de stroom.", "Lijm is altijd giftig."], 0,
              "Een schroefverbinding is losneembaar, lijmen niet. Zo kan Noor de batterij later vervangen."),
           volgorde("Zet de vijf fasen van het technisch proces in de juiste volgorde, zoals Noor ze doorloopt.",
                    ["Het probleem onderzoeken", "Ontwerpen", "Maken", "In gebruik nemen en testen", "Evalueren"],
                    "Eerst het probleem en de criteria, dan ontwerpen, maken, testen en evalueren. Voldoet het niet, dan keer je terug naar ontwerpen of maken.")]),
    klik("Tandwiel A drijft B aan, en B drijft C aan. Klik op het tandwiel dat het snelst ronddraait.",
         "drie-tandwielen.svg", [[53, 28, 15, 40]],
         "Groot drijft klein aan, dus het wordt telkens sneller. Het kleinste tandwiel, C met 10 tanden, draait het snelst."),
    klik("Klik op het rekje dat niet scheef kan trekken als je er opzij tegen duwt.",
         "drie-rekjes.svg", [[37, 10, 26, 80]],
         "Een rechthoek trekt scheef. Met een schuine balk erin maak je twee driehoeken, en een driehoek vervormt niet. Een horizontale balk helpt niet."),
    koppel("Welke kracht werkt vooral op elk onderdeel?",
           [["de ophangkabel van een brug", "trek"], ["een pilaar onder een dak", "druk"],
            ["een schroevendraaier die je ronddraait", "torsie"], ["een plank waarop je in het midden staat", "buiging"]],
           ["wrijving"],
           "Een kabel wordt uitgerokken (trek), een pilaar samengeduwd (druk), een schroevendraaier verdraaid (torsie) en een plank buigt door (buiging)."),
    tabel("Is elk metaal ferro of non-ferro?",
          [("staal", "Ferro"), ("aluminium", "Non-ferro"), ("koper", "Non-ferro"), ("gietijzer", "Ferro"), ("lood", "Non-ferro")],
          "Ferro bevat ijzer, wordt aangetrokken door een magneet en kan roesten. Aluminium, koper en lood bevatten geen ijzer.",
          kolommen=["Ferro", "Non-ferro"]),
    keuze("Spanning meet je in [[*volt|ampère|watt]], stroomsterkte in [[*ampère|volt|ohm]] en vermogen in [[*watt|ohm|volt]].",
          "Spanning U in volt, stroomsterkte I in ampère, weerstand R in ohm en vermogen P in watt."),
    sleep("Een windmolen zet [[bewegingsenergie]] om in [[elektrische energie]]. Bij een gloeilamp gaat veel energie verloren als [[warmte]].",
          ["chemische energie", "geluid", "potentiële energie"],
          "Een windmolen maakt van beweging elektriciteit. Een gloeilamp geeft licht, maar het grootste deel wordt niet-nuttige warmte."),
    sorteer("Kan je deze verbinding later weer losmaken?",
            ["Losneembaar", "Niet losneembaar"],
            [["bout en moer", "Losneembaar"], ["rits", "Losneembaar"], ["klittenband", "Losneembaar"], ["magneet", "Losneembaar"],
             ["lassen", "Niet losneembaar"], ["lijmen", "Niet losneembaar"], ["solderen", "Niet losneembaar"]],
            "Bout en moer, schroef, rits, klittenband en magneet maak je los. Lassen, lijmen en solderen niet zonder iets kapot te maken."),
    open_("Leg uit waarom er staal in een betonnen balk zit die moet doorbuigen.",
          "Beton verdraagt veel druk maar weinig trek. Als een balk doorbuigt, wordt de onderkant uitgerokken: daar werkt trek. Het staal vangt die trekkracht op, zodat de balk niet scheurt. Dat heet gewapend beton.",
          "Gewapend beton is beton met staal erin. Staal is goed voor trek, beton voor druk."),
    mk("Tandwiel A met 10 tanden drijft tandwiel B met 30 tanden aan. A draait 6 keer rond. Hoeveel keer draait B rond?",
       ["2 keer", "18 keer", "3 keer", "6 keer"], 2,
       "B heeft drie keer zoveel tanden, dus draait het drie keer trager. 6 gedeeld door 3 is 2."),
    iv("Hoeveel liter past er in een bak van 2 dm lang, 3 dm breed en 5 dm hoog? Antwoord met een getal.", "30",
       "Volume balk = l · b · h = 2 · 3 · 5 = 30 dm³. 1 dm³ is 1 liter, dus 30 liter."),
    wn("In een serieschakeling blijven de andere lampjes branden als er één stukgaat.", F,
       "In serie is er maar één weg voor de stroom: één lampje stuk en alles is uit. In parallel branden de andere door."),
    mk("Waarom hangen de lampjes van een kerstboom het best in parallel?",
       ["Als er één stukgaat, branden de andere door.", "Dan branden ze allemaal veel feller.",
        "Dan is er maar één draad nodig.", "Dan heb je geen stekker meer nodig."], 1,
       "In parallel heeft elk lampje zijn eigen weg voor de stroom. Eén lampje stuk en de rest blijft branden."),
    mk("Met welke proef weet je of een metaal ferro of non-ferro is?",
       ["met de magneetproef", "met de geleidingsproef", "met de onderdompelingsmethode", "met de breekproef"], 3,
       "Een magneet trekt ferrometalen aan. De geleidingsproef zegt alleen of iets een metaal is."),
    wn("Koelen en invriezen doden de bacteriën in voedsel.", F,
       "Koelen remt de bacteriën, invriezen legt ze stil. Geen van beide doodt ze. Daarvoor heb je warmte nodig, zoals bij pasteuriseren."),
    mk("Op een pot yoghurt staat 'te gebruiken tot'. Wat betekent dat?",
       ["Het gaat om veiligheid: na die datum eet je het niet meer.", "Het gaat om smaak: na die datum is het minder lekker.",
        "Het gaat om de prijs: na die datum is het in solden.", "Het gaat om de verpakking: die mag dan bij het pmd."], 0,
       "Te gebruiken tot gaat over veiligheid. Ten minste houdbaar tot gaat over kwaliteit: daarna kan het nog goed zijn."),
    iv("Een EN-poort krijgt aan de ene ingang 1 en aan de andere 0. Wat is de uitgang? Antwoord met 0 of 1.", "0",
       "Een EN-poort geeft alleen 1 als álle ingangen 1 zijn. Hier is één ingang 0, dus de uitgang is 0."),
    iv("Een OF-poort krijgt aan de ene ingang 0 en aan de andere 1. Wat is de uitgang? Antwoord met 0 of 1.", "1",
       "Een OF-poort geeft al 1 zodra één ingang 1 is."),
    wn("De waarheidstabel van een poort met twee ingangen heeft vier rijen.", J,
       "Twee ingangen geven vier mogelijkheden: 00, 01, 10 en 11."),
    mk("Een tekening staat op schaal 2:1. Wat betekent dat?",
       ["De tekening is dubbel zo groot als het voorwerp.", "De tekening is half zo groot als het voorwerp.",
        "De tekening is even groot als het voorwerp.", "Het voorwerp is dubbel zo groot als de tekening."], 2,
       "2:1 betekent: 2 cm op de tekening is 1 cm in het echt. De tekening is dus vergroot."),
    mk("Je wil een doosje uit één stuk karton knippen en plooien. Welke tekening heb je nodig?",
       ["een ontvouwing", "een isometrisch perspectief", "een conceptschets", "een detailontwerp"], 1,
       "Een ontvouwing is het platte patroon van het voorwerp: precies wat je uit het karton knipt voor je plooit."),
    wn("Een stoel met een brede voet en een laag zwaartepunt valt minder snel om.", J,
       "Een brede voet en een laag zwaartepunt maken een constructie stabieler."),
    mk("Met welk gereedschap haal je de isolatie van een elektrische draad?",
       ["met een striptang", "met een zijsnijtang", "met een soldeerbout", "met een kroonsteentje"], 3,
       "Een striptang stript de draad. Een zijsnijtang knipt, een soldeerbout verbindt met tin en een kroonsteentje klemt draden vast."),
    wn("Beitsen kleurt het hout, maar je ziet de nerf nog.", J,
       "Beits legt geen dekkende laag: het kleurt het hout en de nerf blijft zichtbaar."),
    mk("Welke van deze is een algoritme?",
       ["een recept met genummerde stappen", "een foto van een taart", "een lijst met je lievelingsgerechten", "een prijskaartje in de winkel"], 2,
       "Een algoritme is een stappenplan met instructies in een vaste volgorde, zoals een recept."),
    mk("Welke energiebron is hernieuwbaar, maar levert niet altijd evenveel?",
       ["wind", "aardgas", "steenkool", "aardolie"], 1,
       "Wind raakt niet op, maar het waait niet altijd even hard. Aardgas, steenkool en aardolie zijn fossiel."),
]

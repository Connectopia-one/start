"""Sociale beïnvloeding: conformisme, inwilliging en gehoorzaamheid — pittig
(🌍 Beyond doorstroom, sociale en gedragswetenschappen). Eigen vragen en eigen
tekeningen (een glijdende schaal, de lijnen van een groepsproef), zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Het continuüm van sociale druk ---------------------------------------------------------
CO = Prent("druk-continuum", "Sociale druk als glijdende schaal", "een brede pijl van links (lichte druk) naar rechts (zware druk) met drie lege vakjes A, B en C van links naar rechts")
CO.pad("M80 280 L820 240 L820 210 L920 300 L820 390 L820 360 L80 320 Z", "#e2eadb", DONKER, 2)
CO.tekst(90, 230, "lichte druk", 22, "start")
CO.tekst(910, 450, "zware druk", 22, "end")
SCHAAL = {"A": 230, "B": 470, "C": 710}
for k, x in SCHAAL.items():
    CO.rect(x - 60, 260, 120, 80, "#ffffff", DONKER, 10, 2)
    CO.letter(x, 300, k)


def schaal(k):
    return [Prent.zone(SCHAAL[k] - 60, 260, 120, 80)]


# De lijnen bij een groepsproef ----------------------------------------------------------
LN = Prent("lijnen-groepsproef", "De lijnen bij een groepsproef", "links een voorbeeldlijn; rechts drie lijnen A, B en C, waarvan B duidelijk even lang is als de voorbeeldlijn, A korter en C veel langer")
LN.tekst(180, 120, "voorbeeld", 22)
LN.lijn(180, 160, 180, 460, DONKER, 8)
for k, x, h in [("A", 480, 200), ("B", 640, 300), ("C", 800, 400)]:
    LN.lijn(x, 560 - h, x, 560, DONKER, 8)
    LN.letter(x, 600, k)

VRAGEN = [
    klik("Klik op de plaats van gehoorzaamheid op deze schaal.", CO.bestand, schaal("C"),
         "Bij gehoorzaamheid komt de druk van iemand met gezag: de zwaarste druk."),
    klik("Klik op de plaats van conformisme op deze schaal.", CO.bestand, schaal("A"),
         "Bij conformisme vraagt niemand iets: de lichtste druk."),
    met_prent(CO.bestand, keuze("Op plaats B hoort [[*inwilliging|gehoorzaamheid|conformisme]].",
              "Bij inwilliging is er een concreet verzoek, maar geen bevel.")),
    met_prent(CO.bestand, mk("Waarom teken je sociale beïnvloeding als een glijdende schaal?",
              ["de druk loopt van licht tot zwaar",
               "er zijn precies drie losse soorten druk",
               "de druk is voor iedereen altijd even groot",
               "de druk verdwijnt na een tijd vanzelf"], 0,
              "Een continuüm is een glijdende schaal.")),
    met_prent(LN.bestand, keuze("De zes anderen zeggen luid 'lijn C'. Een proefpersoon die dan ook C zegt, toont [[*normatief|informatief]] conformisme.",
              "Het juiste antwoord is duidelijk zichtbaar; hij gaat mee om niet op te vallen.")),
    met_prent(LN.bestand, inv("Van wie is deze proef met lijnen? Familienaam.", ["Asch", "Solomon Asch"],
              "Solomon Asch toonde dat velen een zichtbaar fout antwoord van de groep overnamen.")),
    met_prent(LN.bestand, tabel("Wat zorgt ervoor dat de proefpersoon minder meegaat met het foute antwoord?", [
        ("één andere deelnemer geeft wel het juiste antwoord", J),
        ("de groep is groter en volledig eensgezind", F),
        ("hij mag zijn antwoord op een briefje schrijven in plaats van luid zeggen", J),
    ], "Eén medestander breekt de druk; een grote eensgezinde groep verhoogt ze.")),
    tabel("Informatief of normatief conformisme?", [
        ("Op een buitenlandse markt betaal je wat de anderen betalen, want zij kennen de prijzen.", "informatief"),
        ("Je lacht mee met een grap die je niet grappig vindt, omdat iedereen lacht.", "normatief"),
        ("Je kiest in een restaurant hetzelfde gerecht als je vrienden die er al vaak waren.", "informatief"),
        ("Je draagt hetzelfde merk sneakers als je klas om erbij te horen.", "normatief"),
    ], "Meegaan omdat anderen het beter weten, of omdat je erbij wil horen.",
       kolommen=["informatief", "normatief"]),
    tabel("Welke beïnvloedingstechniek is dit?", [
        ("Eerst vraagt een buur of je even zijn plant water geeft, later of je twee weken zijn hond uitlaat.", "voet-tussen-de-deur"),
        ("Een vriend vraagt honderd euro te leen, je weigert, dan vraagt hij er twintig.", "deur-in-het-gezicht"),
        ("Je boekt een reis van 300 euro en bij de betaling komen er nog 40 euro dossierkosten bij.", "zodra-de-bal-aan-het-rollen-is"),
        ("'Deze jas kost 80 euro, en ik doe er nog een sjaal bij.'", "dat-is-nog-niet-alles"),
    ], "Klein dan groot, groot dan klein, slechtere voorwaarde na het ja, of iets extra voor je antwoordt.",
       kolommen=["voet-tussen-de-deur", "deur-in-het-gezicht", "zodra-de-bal-aan-het-rollen-is", "dat-is-nog-niet-alles"]),
    sorteer("Toegeven of weerstand bieden?", ["Toegeven", "Weerstand bieden"], [
        ["conformisme", "Toegeven"],
        ["assertiviteit", "Weerstand bieden"],
        ["gehoorzaamheid", "Toegeven"],
        ["trotseren", "Weerstand bieden"],
        ["inwilliging", "Toegeven"],
        ["onafhankelijkheid", "Weerstand bieden"],
    ], "Drie vormen van toegeven en drie van weerstand bieden."),
    casus(
        "Op een druk perron valt een man flauw. Tientallen mensen kijken, maar niemand doet iets. Lotte roept: "
        "'U daar, met de rode jas, bel 112!' De man met de rode jas belt meteen.",
        [
            inv("Hoe heet het verschijnsel dat niemand helpt omdat er veel omstanders zijn?", ["omstandereffect", "het omstandereffect"],
                "Darley en Latané beschreven het omstandereffect."),
            mk("Waarom helpt niemand?",
               ["de verantwoordelijkheid verspreidt zich",
                "de mensen zijn allemaal slecht van karakter",
                "de mensen kennen de man niet persoonlijk",
                "er is geen gezagsfiguur in de buurt"], 0,
               "Iedereen denkt dat iemand anders wel zal ingrijpen."),
            keuze("Lotte doorbreekt het effect door iemand [[*persoonlijk aan te spreken|harder te roepen|zelf weg te gaan]].",
                  "Wie persoonlijk aangesproken wordt, kan de verantwoordelijkheid niet meer doorschuiven."),
        ],
    ),
    koppel("Koppel elk experiment aan wat het toonde.", [
        ["Sherif", "in het donker schoven schattingen naar elkaar toe"],
        ["Asch", "mensen namen een zichtbaar fout antwoord over"],
        ["Milgram", "mensen gingen ver op bevel van een gezagsfiguur"],
        ["Zimbardo", "een toegewezen rol veranderde het gedrag sterk"],
    ], ["kinderen sloegen een opblaaspop"], "Vier klassieke experimenten over sociale beïnvloeding."),
    keuze("Bij Sherif was het juiste antwoord [[*onduidelijk|duidelijk zichtbaar]], daarom hoort zijn experiment bij informatief conformisme.",
          "Wie het niet weet, gebruikt de groep als bron."),
    tabel("Verhoogt dit de gehoorzaamheid aan een gezagsfiguur?", [
        ("de gezagsfiguur staat vlak naast je", J),
        ("er staat een gerespecteerde instelling achter", J),
        ("je ziet iemand anders weigeren", F),
    ], "Nabijheid en een gerespecteerde instelling verhogen gehoorzaamheid; een voorbeeld van weigeren verlaagt ze."),
    keuze("Je zegt rustig: 'Nee, ik doe niet mee, maar ik begrijp dat jullie het leuk vinden.' Dat is [[*assertiviteit|trotseren|inwilliging]].",
          "Voor jezelf opkomen zonder de ander aan te vallen."),
    mk("Je past je kleren aan je klas aan, terwijl niemand iets vroeg. Waarom is dat geen inwilliging?",
       ["er is geen verzoek",
        "alleen bij conformisme is er een bevel",
        "bij inwilliging gaat het om een groep",
        "bij conformisme komt de druk van boven"], 0,
       "Bij conformisme vraagt niemand iets."),
    tabel("Klopt dit?", [
        ("Milgram en Zimbardo tonen dat enkel slechte mensen zo handelen.", F),
        ("Beide experimenten zouden vandaag niet meer zo mogen.", J),
        ("Beïnvloedingstechnieken werken mee omdat mensen hun ja achteraf goedpraten.", J),
        ("De deur-in-het-gezicht begint met een klein verzoek.", F),
    ], "Gewone mensen gingen heel ver; de deur in het gezicht begint groot."),
    inv("Hoeveel beïnvloedingstechnieken zijn er in de leerstof? Schrijf het getal.", ["4", "vier"],
        "Voet-tussen-de-deur, deur-in-het-gezicht, zodra-de-bal-aan-het-rollen-is en dat-is-nog-niet-alles."),
    sleep("Bij [[gehoorzaamheid]] komt de druk van iemand met gezag. Bij [[conformisme]] vraagt niemand iets.",
          ["assertiviteit", "trotseren"], "Twee uitersten van de schaal."),
    volgorde("Zet de stappen van de voet-tussen-de-deur-techniek in de juiste volgorde.", [
        "een klein verzoek stellen",
        "de ander zegt ja",
        "een groter verzoek stellen",
        "de ander zegt makkelijker opnieuw ja",
    ], "Wie op iets kleins ja zegt, zegt daarna makkelijker ja op iets groters."),
    mk("Wat onderzocht Zimbardo met het Stanford gevangenisexperiment?",
       ["wat een rol met gedrag doet",
        "hoe lang mensen in het donker schatten",
        "hoeveel mensen een fout antwoord overnemen",
        "hoe snel een dier op een knop leert duwen"], 0,
       "Studenten kregen de rol van bewaker of gevangene."),
    keuze("Een leerling zegt luid 'Dat doe ik niet!' en doet expres het tegenovergestelde van wat de groep wil. Dat is [[*trotseren|assertiviteit|onafhankelijkheid]].",
          "Trotseren is openlijk ingaan tegen de druk."),
    inv("Hoe heet de onderzoeker van het experiment met steeds zwaardere stroomstoten op bevel? Familienaam.", ["Milgram", "Stanley Milgram"],
        "Stanley Milgram onderzocht gehoorzaamheid."),
    tabel("Welke vorm van sociale beïnvloeding is dit?", [
        ("Een soldaat voert een bevel uit van zijn officier.", "gehoorzaamheid"),
        ("Je collega vraagt of je zijn dienst wil overnemen en je zegt ja.", "inwilliging"),
        ("Iedereen op het feest danst, dus jij ook, hoewel niemand het vroeg.", "conformisme"),
    ], "Bevel, verzoek of geen vraag.", kolommen=["conformisme", "inwilliging", "gehoorzaamheid"]),
    keuze("De beïnvloedingstechnieken horen bij [[*inwilliging|gehoorzaamheid|conformisme]], omdat er telkens een verzoek is.",
          "Inwilliging is ja zeggen op een verzoek."),
    mk("Welke namen horen bij het omstandereffect?",
       ["Darley en Latané", "Sherif en Asch", "Milgram en Zimbardo", "Heider en Weiner"], 0,
       "John Darley en Bibb Latané."),
    keuze("Een kleinere en minder eensgezinde groep [[*verlaagt|verhoogt]] de kans dat iemand conformeert.",
          "Grootte en eensgezindheid van de groep verhogen de druk."),
    open_("Leg uit wat het verschil is tussen het experiment van Sherif en dat van Asch, en welk soort conformisme bij elk past.",
          "Bij Sherif was het antwoord onduidelijk: mensen gebruikten de groep als bron, dat is informatief conformisme. Bij Asch was het juiste antwoord duidelijk zichtbaar en gingen mensen toch mee om niet op te vallen: normatief conformisme."),
]

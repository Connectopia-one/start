# -*- coding: utf-8 -*-
"""Uitdaging samenleving en economie ✨ Spark (11 november 2026), in de vormen
van het examen van de Examencommissie: 30 vragen die alle hoofdstukken door
elkaar halen, met een casus over een budget, tabellen, keuzelijsten, slepen,
koppelen, sorteren, volgorde, twee klikvragen op een zelf getekende prent
(een mailvenster en een rekenblad) en een open vraag. Geen nieuwe leerstof.
De prenten tekent inhoud/uitdaging/maak_prenten_spark_samenleving.py.
"""
NIVEAU = "spark"
VAK = "Samenleving en economie"
BESTAND = "spark-samenleving-en-economie-uitdaging.json"
AANTAL = 30
J, F = True, False
MAP = "/examenvormen/samenleving-spark"


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
    casus("Lotte is dertien. Ze krijgt elke maand 30 euro zakgeld. Voor haar verjaardag kreeg ze één keer 50 euro van haar oma. Elke maand betaalt ze 10 euro voor haar gsm-abonnement, en ze geeft ongeveer 8 euro uit aan snoep en tijdschriften. In een webshop ziet ze sneakers van 90 euro, met de melding: 'Nog maar 2 paar! Deze aanbieding eindigt over 10 minuten.'",
          [sorteer("Sleep elk bedrag van Lotte naar de juiste kolom.",
                   ["Terugkerende inkomst", "Toevallige inkomst", "Vaste uitgave", "Variabele uitgave"],
                   [["30 euro zakgeld per maand", "Terugkerende inkomst"], ["50 euro van oma", "Toevallige inkomst"],
                    ["10 euro gsm-abonnement", "Vaste uitgave"], ["snoep en tijdschriften", "Variabele uitgave"]],
                   "Zakgeld komt elke maand terug, het geld van oma één keer. Het abonnement is elke maand hetzelfde (vast), wat ze aan snoep uitgeeft, verschilt (variabel)."),
           iv("Hoeveel euro houdt Lotte elke maand over van haar zakgeld als ze haar gewone uitgaven betaald heeft? Antwoord met een getal.", "12",
              "30 euro zakgeld min 10 euro voor de gsm en 8 euro voor snoep en tijdschriften is 12 euro. Dat kan ze sparen."),
           mk("Wat zijn 'Nog maar 2 paar!' en 'eindigt over 10 minuten'?",
              ["verkooptrucs met schaarste en tijdsdruk", "eerlijke informatie over de voorraad",
               "een wettelijke regel voor elke webshop", "de bedenktijd die de winkel je geeft"], 2,
              "Schaarste (nog maar 2) en tijdsdruk (nog 10 minuten) moeten je snel doen kopen, zonder na te denken of je het echt nodig hebt."),
           wn("Als Lotte de sneakers online koopt, heeft ze veertien dagen bedenktijd.", J,
              "Bij een aankoop online heb je veertien dagen bedenktijd. In een gewone winkel niet.")]),
    klik("Je stuurt een mail naar veertig ouders die elkaar niet kennen. Klik op het vak waar je hun adressen zet, zodat niemand de andere adressen ziet.",
         "mailvenster.svg", [[2, 37, 96, 11]],
         "Adressen in BCC ziet niemand anders. Adressen in Aan en CC ziet iedereen die de mail krijgt."),
    klik("Klik in het rekenblad op de cel met de uitgaven van februari.", "rekenblad.svg", [[44.5, 37.5, 18.5, 12.5]],
         "De uitgaven staan in kolom C, februari staat in rij 3. Het celadres is dus C3."),
    mk("Welke formule telt de cellen B2 tot en met B6 op?",
       ["=SOM(B2:B6)", "SOM(B2:B6)", "=SOM(B2+B6)", "=B2:B6"], 1,
       "Elke formule begint met een gelijkheidsteken. De dubbele punt betekent tot en met: B2:B6 is het hele bereik."),
    koppel("Koppel elke macht aan wie ze uitoefent.",
           [["De wetgevende macht", "het parlement"], ["De uitvoerende macht", "de regering"], ["De rechterlijke macht", "de rechters"]],
           ["de koning"],
           "Het parlement maakt de wetten, de regering voert ze uit, de rechters spreken recht. De koning is staatshoofd, maar bestuurt niet."),
    tabel("Wie is bevoegd? Kies voor elke taak het juiste bestuursniveau.",
          [("onderwijs", "Gemeenschap"), ("milieu", "Gewest"), ("defensie", "Federale overheid"),
           ("cultuur", "Gemeenschap"), ("mobiliteit", "Gewest"), ("pensioenen", "Federale overheid")],
          "Een gemeenschap gaat over personen en taal (onderwijs, cultuur, welzijn). Een gewest over grondgebied (milieu, wonen, mobiliteit). Justitie, defensie en pensioenen zijn federaal.",
          kolommen=["Gemeenschap", "Gewest", "Federale overheid"]),
    keuze("In een gemeente beslist de [[*gemeenteraad|deputatie|provincieraad]]. Het [[*college van burgemeester en schepenen|Vlaams Parlement|federaal parlement]] voert uit. In een provincie wordt de [[*gouverneur|burgemeester|schepen]] benoemd en niet verkozen.",
          "Op elk niveau beslist een verkozen raad en voert een bestuur uit. In de gemeente zijn dat de gemeenteraad en het college. De gouverneur van een provincie wordt benoemd."),
    volgorde("Zet de vier stappen van eerste hulp in de juiste volgorde.",
             ["Zorgen voor veiligheid", "De toestand van het slachtoffer beoordelen", "Hulp raadplegen, bijvoorbeeld 112 bellen", "Verdere hulp verlenen"],
             "Eerst veiligheid, zodat er geen tweede slachtoffer valt. Dan kijk je hoe het met het slachtoffer gaat, haal je hulp en help je verder."),
    sleep("Bij pesten gebeurt het [[herhaaldelijk]] en is er een [[machtsverschil]]. Bij plagen gaat het [[over en weer]].",
          ["één keer", "toevallig", "per ongeluk"],
          "Plagen gaat over en weer en blijft leuk voor iedereen. Pesten gaat één kant op, herhaalt zich en er is een machtsverschil."),
    sorteer("In welke sector werkt elk van deze?",
            ["Primair", "Secundair", "Tertiair", "Quartair"],
            [["een visser", "Primair"], ["een akkerbouwer", "Primair"], ["een autofabriek", "Secundair"], ["een staalbedrijf", "Secundair"],
             ["een kapper", "Tertiair"], ["een bank", "Tertiair"], ["de politie", "Quartair"], ["een openbare school", "Quartair"]],
            "Primair haalt grondstoffen, secundair verwerkt ze, tertiair levert diensten met winst, quartair diensten zonder winstoogmerk."),
    mk("Iemand ligt bewusteloos op de grond, maar ademt normaal. De omgeving is veilig. Wat doe je?",
       ["in stabiele zijligging leggen, 112 bellen en blijven", "rechtop zetten en water laten drinken",
        "op de rug laten liggen en weggaan om hulp", "flink door elkaar schudden tot hij wakker wordt"], 2,
       "Bewusteloos maar normaal ademend: stabiele zijligging, zodat de luchtweg vrij blijft. Dan bel je 112 en blijf je bij het slachtoffer."),
    mk("Je belt 112. Wat doe je pas op het einde van het gesprek?",
       ["inleggen", "zeggen waar het is", "zeggen wat er gebeurd is", "zeggen hoeveel slachtoffers er zijn"], 0,
       "Je zegt waar, wat, hoeveel slachtoffers en in welke toestand. Je legt nooit als eerste neer: de hulpdienst zegt wanneer het gesprek gedaan is."),
    wn("Op een verse brandwonde leg je best meteen ijs, rechtstreeks op de huid.", F,
       "Een brandwonde koel je tien tot twintig minuten met lauw stromend water. IJs op de blote huid beschadigt ze nog meer."),
    mk("In een land zijn er elke vijf jaar verkiezingen, maar er mag maar één partij meedoen. Wat voor land is dat?",
       ["een dictatuur", "een democratie", "een gemeenschap", "een gewest"], 1,
       "In een dictatuur zijn er soms verkiezingen, maar ze zijn niet vrij. Vrije verkiezingen zijn een van de principes van een democratie."),
    wn("In België worden de rechters verkozen door het volk.", F,
       "Rechters worden benoemd, niet verkozen. Zo staan ze los van de politieke partijen."),
    mk("Een overheid geeft meer uit dan ze ontvangt. Wat is het gevolg?",
       ["Ze moet lenen, en dat kost rente.", "Ze moet minder belastingen vragen.", "Ze krijgt het verschil vanzelf terug.", "Ze moet de bedrijven sluiten."], 0,
       "Wie meer uitgeeft dan hij ontvangt, moet het verschil lenen. Op een lening betaal je rente."),
    mk("Iemand verliest zijn werk en krijgt een werkloosheidsuitkering. Wat voor uitkering is dat?",
       ["een vervangingsuitkering", "een aanvullende uitkering", "een investeringsgoed", "een consumentengoed"], 1,
       "Een vervangingsuitkering komt in de plaats van een loon. Een aanvullende uitkering komt bovenop een loon."),
    mk("Je wil een bestand op je computer houden en er ook een exemplaar van op je usb-stick zetten. Wat doe je?",
       ["kopiëren", "verplaatsen", "herbenoemen", "verwijderen"], 2,
       "Kopiëren laat het origineel staan. Verplaatsen haalt het weg op de oude plaats."),
    iv("Je krijgt een sms met een link om 'je pakje te volgen', maar het is oplichting. Hoe heet die vorm van fraude? Antwoord met één woord.", "smishing",
       "Phishing gaat via mail, smishing via sms, quishing via een QR-code en vishing via de telefoon."),
    wn("'Zomer2026' is een sterk wachtwoord.", F,
       "Er staat geen speciaal teken in, en het is makkelijk te raden. Een sterk wachtwoord heeft 8 tot 24 karakters met een hoofdletter, een kleine letter, een cijfer en een teken."),
    mk("Je ziet dat iemand je bankkaart misbruikt heeft. Wat doe je eerst?",
       ["de kaart blokkeren en je bank verwittigen", "aangifte doen bij de politie",
        "een nieuw wachtwoord kiezen voor je mail", "wachten tot het volgende rekeninguittreksel"], 1,
       "Eerst blokkeren en je bank verwittigen, zodat er niet nog meer geld verdwijnt. Daarna doe je aangifte."),
    iv("Hoe heet de tekenopmaak waarmee je de 2 in m² hoger zet? Antwoord met één woord.", "superscript",
       "Superscript zet een teken hoger (m²), subscript lager (H₂O)."),
    wn("Een omstaander die meelacht met een pestkop, helpt het pesten mee in stand houden.", J,
       "Wie meelacht, geeft de pestkop publiek en steun. Zo blijft het pesten duren."),
    mk("Wanneer telt toestemming?",
       ["Als ze vrijwillig en gelijkwaardig gegeven wordt.", "Als iemand na lang aandringen toch ja zegt.",
        "Als de oudste van de twee beslist.", "Als niemand uitdrukkelijk nee zegt."], 3,
       "Toestemming telt alleen als ze vrijwillig en gelijkwaardig is. Onder druk telt ze niet, en geen nee is nog geen ja."),
    wn("Brussel hoort bij de provincie Vlaams-Brabant.", F,
       "België heeft tien provincies, en Brussel hoort bij geen enkele."),
    wn("Bij elke goederenstroom in de economische kringloop loopt er meestal een geldstroom in de omgekeerde richting.", J,
       "Gezinnen leveren arbeid en krijgen loon. Bedrijven leveren goederen en krijgen er geld voor."),
    open_("Leg uit waarom de drie machten in een democratie gescheiden zijn. Geef een voorbeeld.",
          "Als de machten gescheiden zijn, kunnen ze elkaar controleren en kan niemand alle macht in handen nemen. Een voorbeeld: de regering mag zelf geen wetten maken, dat doet het parlement. En een rechter kan een minister veroordelen als die de wet overtreedt.",
          "Wetgevend is het parlement, uitvoerend de regering en rechterlijk de rechters. Ze houden elkaar in evenwicht."),
]

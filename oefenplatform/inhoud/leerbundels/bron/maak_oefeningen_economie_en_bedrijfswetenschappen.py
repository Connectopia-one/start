# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij economie en bedrijfswetenschappen
🚀 Boost dubbele finaliteit.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde stof
met andere opgaven, dus gaat dezelfde pdf bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die op het scherm: andere
bedragen, andere ondernemingen en opdrachten die je enkel op papier kan maken —
een kostentabel aanvullen, een loonfiche narekenen, een organogram tekenen.
Wie hier iets bijschrijft, legt het eerst naast
`../../boost-dubbele-finaliteit/economie-en-bedrijfswetenschappen.json` en naast
`maak_economie_en_bedrijfswetenschappen.py`.

Elk bedrag in dit bestand is nagerekend. Wie een getal verandert, rekent het
antwoord opnieuw uit en zet het ook op het antwoordblad goed.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost-dubbele-finaliteit".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

VAK = "Economie en bedrijfswetenschappen"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"
NIVEAU = "-boost-dubbele-finaliteit"
VOOR = "oefenbundel-"

W = "110px"
WW = "185px"
WL = "250px"

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."

HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Zet bij elk bedrag het euroteken en twee decimalen.",
    "Schrijf bij een berekening de tussenstap op, niet alleen het eindbedrag.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

OEFENBUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", DF)
    b.setdefault("onder", ONDER)
    b.setdefault("hoe", HOE)
    OEFENBUNDELS[VOOR + slug + NIVEAU] = b


# ============================================================
zet("behoeften-schaarste-en-soorten-goederen",
    titel="Behoeften, schaarste en soorten goederen",
    reeksen=[
        dict(kop="Soorten behoeften",
             opdracht="Zet achter elke behoefte of ze primair of secundair is.",
             oefeningen=[
                 ("rij", [("eten en drinken", "primair"),
                          ("een dak boven je hoofd", "primair"),
                          ("een festivalticket", "secundair"),
                          ("kledij tegen de kou", "primair"),
                          ("een derde paar sneakers", "secundair"),
                          ("drinkbaar water", "primair")],
                  "Primair of secundair?", W),
                 ("open", "Waarom verschilt de grens tussen primair en secundair van land tot "
                          "land en van tijd tot tijd?",
                  "Wat je echt nodig hebt om mee te kunnen doen hangt af van de samenleving "
                  "waarin je leeft. Een gsm was dertig jaar geleden een luxe en is nu voor "
                  "school en werk bijna onmisbaar.", 3),
             ]),
        dict(kop="Soorten goederen",
             opdracht="Vul het juiste begrip in.",
             oefeningen=[
                 ("rij", [("lucht om te ademen", "vrij goed"),
                          ("een brood in de winkel", "economisch goed"),
                          ("een machine in een fabriek", "productiegoed"),
                          ("een ijsje dat je opeet", "verbruiksgoed, eenmalig"),
                          ("een fiets die jaren meegaat", "duurzaam consumptiegoed"),
                          ("een knipbeurt bij de kapper", "dienst")],
                  "Welk soort goed?", WL),
                 ("rij", [("brood en beschuit", "substitutiegoederen"),
                          ("printer en inktpatroon", "complementaire goederen"),
                          ("thee en koffie", "substitutiegoederen"),
                          ("auto en benzine", "complementaire goederen"),
                          ("boter en margarine", "substitutiegoederen"),
                          ("gsm en oplader", "complementaire goederen")],
                  "Vervangend of aanvullend?", WL),
             ]),
        dict(kop="Schaarste en kiezen",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Leg uit waarom schaarste niet hetzelfde is als zeldzaam zijn.",
                  "Schaarste betekent dat er minder van is dan er gevraagd wordt. Zand is "
                  "niet zeldzaam en toch schaars, want wie het wil moet ervoor betalen.", 3),
                 ("open", "Je hebt 60 euro en kiest tussen een concertticket van 55 euro of "
                          "een paar schoenen van 55 euro. Wat zijn je alternatieve kosten als "
                          "je het ticket koopt?",
                  "De schoenen die je daardoor niet koopt. Alternatieve kosten zijn altijd het "
                  "beste alternatief dat je laat vallen, niet het bedrag.", 3),
                 ("open", "Waarom moet ook een rijk land kiezen?",
                  "Ook daar zijn arbeid, grondstoffen en tijd beperkt. Elke euro aan "
                  "wegenwerken is een euro die niet naar scholen gaat.", 3),
             ]),
    ])


# ============================================================
zet("nut-voorkeuren-en-de-vraag-van-de-consument",
    titel="Nut, voorkeuren en de vraag van de consument",
    reeksen=[
        dict(kop="Totaal nut en grensnut",
             opdracht="Vul de tabel aan. Het grensnut is het extra nut van de volgende "
                      "pannenkoek.",
             oefeningen=[
                 ("tabel",
                  ["Aantal pannenkoeken", "Totaal nut", "Grensnut"],
                  [["1", "20", None],
                   ["2", "36", None],
                   ["3", "46", None],
                   ["4", "50", None],
                   ["5", "48", None]],
                  "Grensnut: 20 — 16 — 10 — 4 — −2. Het totaal nut stijgt tot de vierde "
                  "pannenkoek en daalt daarna; het grensnut daalt vanaf de eerste.",
                  "95px"),
                 ("open", "Bij welke pannenkoek stopt een verstandige eter, en waarom?",
                  "Na de vierde. De vijfde heeft een negatief grensnut, dus die maakt hem "
                  "minder tevreden dan wanneer hij ermee ophield.", 3),
                 ("open", "Hoe heet de wet die zegt dat elk volgend stuk minder extra nut "
                          "geeft?",
                  "De wet van het afnemende grensnut.", 2),
             ]),
        dict(kop="De vraagcurve",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de prijs stijgt, de gevraagde hoeveelheid", "daalt"),
                          ("de richting van de vraagcurve", "dalend"),
                          ("de vraag naar brood als het inkomen stijgt", "blijft ongeveer gelijk"),
                          ("de vraag naar restaurantbezoek als het inkomen stijgt", "stijgt"),
                          ("de vraag naar thee als koffie duurder wordt", "stijgt"),
                          ("de vraag naar printerpapier als printers duurder worden", "daalt")],
                  "Wat gebeurt er?", WL),
                 ("open", "Wat is het verschil tussen een beweging langs de vraagcurve en een "
                          "verschuiving van de hele curve?",
                  "Langs de curve beweeg je als alleen de prijs van het goed verandert. De "
                  "hele curve verschuift als iets anders verandert: het inkomen, de prijs van "
                  "een ander goed, de smaak of het aantal consumenten.", 3),
                 ("teken", "Teken een vraagcurve en zet er een tweede naast die een gestegen "
                           "inkomen voorstelt. Benoem de assen.",
                  "De assen: prijs verticaal, hoeveelheid horizontaal. Twee dalende lijnen, "
                  "de tweede volledig rechts van de eerste, want bij elke prijs wordt er meer "
                  "gevraagd.", 55),
             ]),
        dict(kop="Rekenen aan de vraag",
             opdracht="Reken uit en schrijf de tussenstap op.",
             oefeningen=[
                 ("kort", "Een winkel verkoopt 400 broden per week aan 2,50 euro. Wat is de "
                          "weekomzet?", "1 000,00 euro", W),
                 ("kort", "De prijs gaat naar 2,80 euro en de verkoop zakt naar 360 broden. "
                          "Wat is de nieuwe weekomzet?", "1 008,00 euro", W),
                 ("open", "Was die prijsverhoging een goede zet? Leg uit met de cijfers.",
                  "De omzet stijgt met 8 euro, dus nauwelijks. Er gaan wel 40 broden minder "
                  "over de toonbank, dus de kosten dalen ook. Of het een goede zet is hangt "
                  "af van de winst per brood, niet van de omzet alleen.", 3),
             ]),
    ])


# ============================================================
zet("de-productiefactoren-en-de-productie",
    titel="De productiefactoren en de productie",
    reeksen=[
        dict(kop="De vier productiefactoren",
             opdracht="Zet bij elk voorbeeld de productiefactor.",
             oefeningen=[
                 ("rij", [("de bakker die om vier uur begint", "arbeid"),
                          ("het weiland van de boer", "natuur"),
                          ("de oven in de bakkerij", "kapitaal"),
                          ("wie beslist welk brood er komt", "ondernemerschap"),
                          ("de bestelwagen", "kapitaal"),
                          ("het ijzererts in de mijn", "natuur")],
                  "Welke productiefactor?", WW),
                 ("rij", [("de vergoeding voor arbeid", "loon"),
                          ("de vergoeding voor natuur", "pacht of huur"),
                          ("de vergoeding voor kapitaal", "intrest"),
                          ("de vergoeding voor ondernemerschap", "winst"),
                          ("de factor die het risico draagt", "ondernemerschap"),
                          ("de factor die zelf gemaakt is", "kapitaal")],
                  "Vul aan.", WW),
             ]),
        dict(kop="Sectoren en productie",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de visser", "primaire sector"),
                          ("de conservenfabriek", "secundaire sector"),
                          ("de viswinkel", "tertiaire sector"),
                          ("het ziekenhuis", "quartaire sector"),
                          ("de staalfabriek", "secundaire sector"),
                          ("de boekhouder", "tertiaire sector")],
                  "Welke sector?", WW),
                 ("open", "Een brood kost in de winkel 2,80 euro. Noem drie schakels die elk "
                          "een deel van die prijs verdienen.",
                  "De landbouwer voor het graan, de molenaar voor het meel, de bakker voor het "
                  "bakken en de winkel voor het verkopen. Elke schakel voegt waarde toe.", 3),
                 ("open", "Wat betekent arbeidsverdeling in een bakkerij met acht mensen?",
                  "Iedereen doet één deel van het werk: deeg maken, bakken, afwerken, "
                  "verkopen. Daardoor gaat het sneller en beter, maar het werk wordt ook "
                  "eentoniger en men wordt afhankelijk van elkaar.", 3),
             ]),
        dict(kop="Productiviteit",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [("240 broden in 8 uur, per uur", "30 broden"),
                          ("240 broden door 3 bakkers, per bakker", "80 broden"),
                          ("na een nieuwe oven 300 broden in 8 uur, per uur", "37,5 broden"),
                          ("de stijging van 30 naar 37,5 in procent", "25 %"),
                          ("360 stuks met 4 werknemers in 6 uur, per werknemer per uur",
                           "15 stuks"),
                          ("de productiviteit als 4 werknemers 480 stuks in 6 uur halen",
                           "20 stuks per uur")],
                  "Wat is het antwoord?", WW),
                 ("open", "Noem twee manieren om de arbeidsproductiviteit te verhogen zonder "
                          "harder te werken.",
                  "Betere machines, een betere werkorganisatie, opleiding, of de arbeid "
                  "verdelen zodat ieder doet waar hij goed in is.", 3),
             ]),
    ])


# ============================================================
zet("de-kosten-van-de-producent",
    titel="De kosten van de producent",
    reeksen=[
        dict(kop="Vast of variabel?",
             opdracht="Zet achter elke kost of ze vast of variabel is.",
             oefeningen=[
                 ("rij", [("de huur van het atelier", "vast"),
                          ("het leer voor de schoenen", "variabel"),
                          ("de verzekering van het gebouw", "vast"),
                          ("de elektriciteit voor de machines", "variabel"),
                          ("het loon van de zaakvoerder", "vast"),
                          ("de verpakking per stuk", "variabel")],
                  "Vast of variabel?", W),
                 ("open", "Waarom is de huur ook een kost in een maand zonder enige verkoop?",
                  "Een vaste kost hangt niet af van de productie. Je betaalt hem ook als de "
                  "machines stilstaan.", 2),
             ]),
        dict(kop="De kostentabel",
             opdracht="Vul de tabel aan. De vaste kosten zijn 1 200 euro, de variabele kost "
                      "is 8 euro per stuk.",
             oefeningen=[
                 ("tabel",
                  ["Aantal", "Vaste kosten", "Variabele kosten", "Totale kosten",
                   "Kostprijs per stuk"],
                  [["100", "1 200", None, None, None],
                   ["200", "1 200", None, None, None],
                   ["400", "1 200", None, None, None],
                   ["600", "1 200", None, None, None]],
                  "100 stuks: 800 — 2 000 — 20,00 euro. 200 stuks: 1 600 — 2 800 — "
                  "14,00 euro. 400 stuks: 3 200 — 4 400 — 11,00 euro. 600 stuks: 4 800 — "
                  "6 000 — 10,00 euro.",
                  "88px"),
                 ("open", "Waarom daalt de kostprijs per stuk terwijl de variabele kost per "
                          "stuk gelijk blijft?",
                  "De vaste kosten worden over meer stuks verdeeld. Dat is het "
                  "schaalvoordeel.", 3),
                 ("kort", "Hoeveel bedraagt de vaste kost per stuk bij 600 stuks?",
                  "2,00 euro", W),
             ]),
        dict(kop="Break-even",
             opdracht="Reken uit en schrijf de tussenstap op.",
             oefeningen=[
                 ("kort", "De verkoopprijs is 20 euro, de variabele kost 8 euro. Wat is de "
                          "brutowinst per stuk?", "12,00 euro", W),
                 ("kort", "Hoeveel stuks moet de zaak verkopen om de vaste kosten van "
                          "1 200 euro te dekken?", "100 stuks", W),
                 ("kort", "Wat is de omzet bij dat break-evenpunt?", "2 000,00 euro", W),
                 ("kort", "Hoeveel winst maakt de zaak bij 300 verkochte stuks?",
                  "3 600,00 euro brutowinst min 1 200,00 euro vaste kosten = 2 400,00 euro",
                  WW),
                 ("open", "De huur stijgt met 300 euro per maand. Hoeveel stuks moet de zaak "
                          "nu verkopen om break-even te draaien?",
                  "1 500 gedeeld door 12 is 125 stuks.", 2),
             ]),
    ])


# ============================================================
zet("opbrengsten-optimale-productiegrootte-en-aanbod",
    titel="Opbrengsten, optimale productiegrootte en aanbod",
    reeksen=[
        dict(kop="Begrippen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("prijs maal aantal", "de omzet of totale opbrengst"),
                          ("de opbrengst van één stuk extra", "de marginale opbrengst"),
                          ("de kost van één stuk extra", "de marginale kost"),
                          ("omzet min totale kosten", "de winst"),
                          ("de hoeveelheid met de hoogste winst", "de optimale productiegrootte"),
                          ("de omzet gedeeld door het aantal", "de gemiddelde opbrengst")],
                  "Hoe noemen we dit?", WL),
                 ("open", "Bij welke hoeveelheid is de winst het grootst, als je naar de "
                          "marginale cijfers kijkt?",
                  "Daar waar de marginale opbrengst gelijk is aan de marginale kost. Zolang "
                  "een stuk extra meer opbrengt dan het kost, blijf je produceren.", 3),
             ]),
        dict(kop="Rekenen aan de winst",
             opdracht="Vul de tabel aan. De prijs is 15 euro per stuk, de vaste kosten zijn "
                      "600 euro.",
             oefeningen=[
                 ("tabel",
                  ["Aantal", "Omzet", "Totale kosten", "Winst"],
                  [["50", None, "1 000", None],
                   ["100", None, "1 400", None],
                   ["150", None, "1 900", None],
                   ["200", None, "2 600", None]],
                  "50: omzet 750, verlies 250. 100: omzet 1 500, winst 100. 150: omzet "
                  "2 250, winst 350. 200: omzet 3 000, winst 400.",
                  "95px"),
                 ("open", "Tussen welke twee hoeveelheden stijgt de winst het minst, en wat "
                          "zegt dat?",
                  "Tussen 150 en 200 stuks: 50 euro extra winst voor 50 stuks extra. De "
                  "marginale kost loopt op, dus het optimum is in zicht.", 3),
             ]),
        dict(kop="Het aanbod",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de prijs stijgt, het aanbod", "stijgt"),
                          ("de richting van de aanbodcurve", "stijgend"),
                          ("de grondstof wordt duurder, het aanbod", "daalt"),
                          ("een betere machine, het aanbod", "stijgt"),
                          ("er komen producenten bij, het aanbod", "stijgt"),
                          ("waar vraag en aanbod kruisen", "de evenwichtsprijs")],
                  "Wat gebeurt er?", WW),
                 ("teken", "Teken een vraagcurve en een aanbodcurve in één assenstelsel. Zet "
                           "een kruisje op het evenwicht en benoem de assen.",
                  "Prijs verticaal, hoeveelheid horizontaal. De vraag daalt, het aanbod "
                  "stijgt, het kruispunt is de evenwichtsprijs met de evenwichtshoeveelheid.",
                  55),
                 ("open", "Wat gebeurt er als de overheid de prijs onder het evenwicht "
                          "vastlegt?",
                  "Er wordt meer gevraagd dan aangeboden, dus er komt een tekort met "
                  "wachtlijsten.", 3),
             ]),
    ])


# ============================================================
zet("soorten-ondernemingen-en-hun-verplichtingen",
    titel="Soorten ondernemingen en hun verplichtingen",
    reeksen=[
        dict(kop="Welke vorm?",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("één persoon, geen aparte rechtspersoon", "de eenmanszaak"),
                          ("de meest gebruikte vennootschap met beperkte aansprakelijkheid",
                           "de bv"),
                          ("de vorm voor een beursgenoteerd bedrijf", "de nv"),
                          ("de vorm zonder winstoogmerk", "de vzw"),
                          ("de vorm waar de leden ook de eigenaars zijn", "de cv"),
                          ("de vorm waar je privévermogen meespeelt", "de eenmanszaak")],
                  "Welke rechtsvorm?", WL),
                 ("open", "Wat betekent beperkte aansprakelijkheid concreet als de zaak over "
                          "kop gaat?",
                  "De schuldeisers kunnen alleen aan het vermogen van de vennootschap, niet "
                  "aan het huis of de spaarrekening van de oprichters.", 3),
                 ("open", "Geef twee voordelen van een eenmanszaak boven een bv.",
                  "Ze is eenvoudiger en goedkoper op te richten, je beslist alleen, en de "
                  "boekhouding mag vereenvoudigd blijven onder een bepaalde omzet.", 3),
             ]),
        dict(kop="Van start gaan",
             opdracht="Zet de stappen in de juiste orde, van 1 tot 6.",
             oefeningen=[
                 ("rij", [("een ondernemingsrekening openen", "3"),
                          ("je inschrijven in de KBO en een ondernemingsnummer krijgen", "2"),
                          ("je aansluiten bij een sociaal verzekeringsfonds", "5"),
                          ("je btw-nummer laten activeren", "4"),
                          ("nagaan of je beroep een vergunning vraagt", "1"),
                          ("je verzekeringen afsluiten", "6")],
                  "Welke stap?", W),
                 ("open", "Waarom moet je als zelfstandige zelf sociale bijdragen betalen?",
                  "Je hebt geen werkgever die dat voor je doet. Met die bijdragen bouw je "
                  "pensioen, ziekteverzekering en kinderbijslag op.", 3),
             ]),
        dict(kop="Verplichtingen",
             opdracht="Waar of niet waar?",
             oefeningen=[
                 ("waar", "Een bv moet elk jaar een jaarrekening neerleggen bij de Nationale "
                          "Bank.", True),
                 ("waar", "Een eenmanszaak met een kleine omzet mag een vereenvoudigde "
                          "boekhouding houden.", True),
                 ("waar", "Boekhoudstukken mogen na drie jaar weg.", False),
                 ("waar", "Een vzw mag geen winst uitkeren aan haar leden.", True),
                 ("waar", "Wie een bv opricht, heeft een notariële akte nodig.", True),
                 ("waar", "Een onderneming zonder personeel moet zich niet bij de RSZ "
                          "aanmelden.", True),
             ]),
    ])


# ============================================================
zet("de-organisatiestructuur-van-een-onderneming",
    titel="De organisatiestructuur van een onderneming",
    reeksen=[
        dict(kop="Begrippen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de tekening van wie onder wie staat", "het organogram"),
                          ("het aantal mensen onder één leidinggevende", "de spanwijdte"),
                          ("het aantal lagen van boven naar onder", "het aantal niveaus"),
                          ("beslissen gebeurt bovenaan", "centralisatie"),
                          ("beslissen gebeurt lager in de organisatie", "decentralisatie"),
                          ("de regels over wie wat mag beslissen", "de bevoegdheden")],
                  "Hoe noemen we dit?", WL),
                 ("open", "Wat is het voordeel en wat het nadeel van een grote spanwijdte?",
                  "Er zijn minder leidinggevenden nodig en de lijnen zijn kort, maar elke "
                  "leidinggevende heeft minder tijd per medewerker.", 3),
             ]),
        dict(kop="Soorten structuren",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("elke medewerker heeft precies één chef", "de lijnorganisatie"),
                          ("er staan specialisten naast de lijn, met advies",
                           "de lijn-staforganisatie"),
                          ("je werkt voor een afdeling én voor een project",
                           "de matrixorganisatie"),
                          ("de indeling per afdeling: aankoop, verkoop, productie",
                           "functionele structuur"),
                          ("de indeling per product of per land", "divisiestructuur"),
                          ("de structuur met heel weinig lagen", "de platte organisatie")],
                  "Welke structuur?", WL),
                 ("open", "Wat is het grootste risico van een matrixorganisatie?",
                  "Je hebt twee chefs die elk iets anders willen. Zonder duidelijke afspraken "
                  "over wie voorgaat, zit de medewerker tussen twee vuren.", 3),
                 ("teken", "Teken het organogram van een bakkerij met een zaakvoerder, twee "
                           "bakkers, een verkoopster en een boekhouder in bijberoep als "
                           "stafmedewerker.",
                  "De zaakvoerder bovenaan; onder hem met volle lijnen de twee bakkers en de "
                  "verkoopster; de boekhouder hangt met een stippellijn naast de zaakvoerder, "
                  "want hij adviseert en geeft geen bevelen.", 60),
             ]),
        dict(kop="Formeel en informeel",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Wat is de informele organisatie en waarom is ze belangrijk?",
                  "Dat zijn de contacten die niet op het organogram staan: wie met wie "
                  "babbelt, wie het echt weet. Informatie gaat er vaak sneller door dan langs "
                  "de officiële weg.", 3),
                 ("open", "Een nieuwe medewerker krijgt opdrachten van drie verschillende "
                          "mensen. Welk principe wordt hier geschonden?",
                  "De eenheid van bevel: één medewerker krijgt zijn opdrachten van één chef.",
                  2),
             ]),
    ])


# ============================================================
zet("de-afdelingen-en-hun-samenwerking",
    titel="De afdelingen en hun samenwerking",
    reeksen=[
        dict(kop="Wie doet wat?",
             opdracht="Zet achter elke taak de afdeling.",
             oefeningen=[
                 ("rij", [("prijzen vergelijken bij drie leveranciers", "aankoop"),
                          ("de facturen inboeken", "boekhouding"),
                          ("een vacature opstellen", "personeel"),
                          ("de nieuwe folder laten ontwerpen", "marketing"),
                          ("de planning van de machines", "productie"),
                          ("de goederen klaarzetten voor vertrek", "logistiek")],
                  "Welke afdeling?", WW),
                 ("rij", [("de voorraad opvolgen", "magazijn of logistiek"),
                          ("de klant bellen die niet betaalt", "boekhouding"),
                          ("een klacht over een kapot toestel afhandelen", "naverkoopdienst"),
                          ("de loonfiches maken", "personeel"),
                          ("beslissen of de zaak een tweede filiaal opent", "directie"),
                          ("een nieuw product uittesten", "onderzoek en ontwikkeling")],
                  "Welke afdeling?", WW),
             ]),
        dict(kop="Waar het misloopt",
             opdracht="Schrijf bij elk geval welke twee afdelingen beter hadden moeten "
                      "overleggen.",
             oefeningen=[
                 ("rij", [("de folder belooft een kleur die niet gemaakt wordt",
                           "marketing en productie"),
                          ("de verkoper verkoopt wat niet op voorraad is",
                           "verkoop en magazijn"),
                          ("er is personeel tekort in het drukste seizoen",
                           "personeel en productie"),
                          ("de grondstof komt te laat en de lijn staat stil",
                           "aankoop en productie"),
                          ("een klant krijgt twee keer dezelfde factuur",
                           "verkoop en boekhouding"),
                          ("de bestelwagen rijdt halfleeg", "logistiek en verkoop")],
                  "Welke twee afdelingen?", WL),
                 ("open", "Waarom is overleg tussen aankoop en boekhouding nodig voor de "
                          "betaaltermijn?",
                  "Aankoop onderhandelt de termijn, de boekhouding moet het geld op dat moment "
                  "hebben. Een korte termijn bedingen terwijl de kas krap staat, zet de zaak "
                  "in de problemen.", 3),
             ]),
        dict(kop="De documentenstroom in huis",
             opdracht="Zet de stappen in de juiste orde, van 1 tot 6.",
             oefeningen=[
                 ("rij", [("de verkoop neemt de bestelling op", "1"),
                          ("het magazijn maakt de goederen klaar", "3"),
                          ("de verkoop kijkt na of de klant kredietwaardig is", "2"),
                          ("de goederen vertrekken met een verzendnota", "4"),
                          ("de boekhouding maakt de factuur", "5"),
                          ("de boekhouding volgt de betaling op", "6")],
                  "Welke stap?", W),
             ]),
    ])


# ============================================================
zet("werving-selectie-en-de-werkplek",
    titel="Werving, selectie en de werkplek",
    reeksen=[
        dict(kop="Begrippen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("zoeken binnen het eigen personeel", "interne werving"),
                          ("zoeken buiten de onderneming", "externe werving"),
                          ("de beschrijving van wat de job inhoudt", "de functiebeschrijving"),
                          ("de beschrijving van wie je zoekt", "het profiel"),
                          ("de dienst van de Vlaamse overheid voor werk", "de VDAB"),
                          ("een bureau dat tijdelijk personeel levert", "een uitzendbureau")],
                  "Hoe noemen we dit?", WL),
                 ("open", "Geef één voordeel van interne werving en één van externe werving.",
                  "Intern ken je de persoon al en is het goedkoper; extern breng je nieuwe "
                  "ideeën en vaardigheden binnen.", 3),
             ]),
        dict(kop="Mag dat gevraagd worden?",
             opdracht="Zet achter elke vraag of ze op een sollicitatiegesprek mag of niet.",
             oefeningen=[
                 ("rij", [("Welke opleiding heb je gevolgd?", "mag"),
                          ("Wil je binnenkort kinderen?", "mag niet"),
                          ("Kan je een ploegenstelsel aan?", "mag"),
                          ("Wat is je religie?", "mag niet"),
                          ("Heb je een rijbewijs B?", "mag, als de job dat vraagt"),
                          ("Bent u lid van een vakbond?", "mag niet")],
                  "Mag of mag niet?", WL),
                 ("open", "Waarom mag een werkgever niet naar een zwangerschapswens vragen?",
                  "Dat is discriminatie op grond van geslacht. Het heeft niets te maken met de "
                  "vraag of iemand de job kan doen.", 3),
             ]),
        dict(kop="Veilig op de werkplek",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("de dienst die waakt over veiligheid en gezondheid",
                           "de interne dienst voor preventie"),
                          ("het overlegorgaan met vakbond en directie", "de ondernemingsraad"),
                          ("wat je draagt op een bouwwerf", "een helm en veiligheidsschoenen"),
                          ("het blad met de gevaren van een product", "de veiligheidsfiche"),
                          ("wat je doet na een arbeidsongeval", "aangifte bij de verzekeraar"),
                          ("de periode waarin je je werkplek leert kennen", "het onthaal")],
                  "Wat is het antwoord?", WL),
                 ("open", "Noem drie dingen die in het onthaal van een nieuwe medewerker "
                          "horen.",
                  "Een rondleiding, de veiligheidsvoorschriften en de nooduitgangen, uitleg "
                  "over de taken, en iemand aanwijzen bij wie hij terecht kan.", 3),
             ]),
    ])


# ============================================================
zet("aanwerving-en-de-arbeidsovereenkomst",
    titel="Aanwerving en de arbeidsovereenkomst",
    reeksen=[
        dict(kop="Soorten overeenkomsten",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("zonder einddatum", "van onbepaalde duur"),
                          ("met een einddatum", "van bepaalde duur"),
                          ("voor één opdracht, bijvoorbeeld een oogst",
                           "voor een duidelijk omschreven werk"),
                          ("minder uren dan een volledige week", "deeltijds"),
                          ("de overeenkomst met een uitzendbureau", "uitzendovereenkomst"),
                          ("de overeenkomst van een student in juli", "studentenovereenkomst")],
                  "Welke overeenkomst?", WL),
                 ("open", "Wat moet er verplicht schriftelijk vastliggen bij een deeltijdse "
                          "overeenkomst, en waarom?",
                  "Het aantal uren en het werkrooster. Anders kan niemand nakijken of er niet "
                  "meer gewerkt wordt dan overeengekomen is.", 3),
             ]),
        dict(kop="Wat staat erin?",
             opdracht="Waar of niet waar?",
             oefeningen=[
                 ("waar", "Een overeenkomst van onbepaalde duur moet schriftelijk zijn.",
                  False),
                 ("waar", "Een overeenkomst van bepaalde duur moet schriftelijk zijn, en "
                          "uiterlijk bij de start.", True),
                 ("waar", "Het loon mag lager zijn dan het minimum van de sector als de "
                          "werknemer daarmee instemt.", False),
                 ("waar", "De plaats van het werk hoort in de overeenkomst.", True),
                 ("waar", "Een concurrentiebeding geldt automatisch, ook als het er niet in "
                          "staat.", False),
                 ("waar", "Een werknemer heeft recht op een afschrift van zijn overeenkomst.",
                  True),
             ]),
        dict(kop="Arbeider of bediende",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("hoofdzakelijk handenarbeid", "arbeider"),
                          ("hoofdzakelijk hoofdarbeid", "bediende"),
                          ("de vakbondsafvaardiging die hen vertegenwoordigt",
                           "de syndicale delegatie"),
                          ("de overeenkomst per sector over lonen",
                           "de collectieve arbeidsovereenkomst"),
                          ("het orgaan dat die cao's sluit", "het paritair comité"),
                          ("wie de cao moet naleven", "elke werkgever van de sector")],
                  "Wat is het antwoord?", WL),
                 ("open", "Waarom is het verschil tussen arbeider en bediende de laatste jaren "
                          "kleiner geworden?",
                  "De wet heeft de opzegtermijnen en de regels bij ziekte gelijkgetrokken, "
                  "omdat het onderscheid als discriminatie gezien werd.", 3),
             ]),
    ])


# ============================================================
zet("schorsing-en-einde-van-de-arbeidsovereenkomst",
    titel="Schorsing en einde van de arbeidsovereenkomst",
    reeksen=[
        dict(kop="Schorsing",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de overeenkomst loopt door, het werk valt stil", "schorsing"),
                          ("ziekte van de werknemer", "een schorsing"),
                          ("het loon van de eerste weken bij ziekte", "het gewaarborgd loon"),
                          ("het bewijs dat je moet binnenbrengen", "het ziekteattest"),
                          ("de periode rond de geboorte voor de moeder", "het moederschapsverlof"),
                          ("het verlof voor de andere ouder", "het geboorteverlof")],
                  "Hoe noemen we dit?", WL),
                 ("rij", [("jaarlijkse vakantie", "schorsing"),
                          ("tijdelijke werkloosheid wegens weerverlet", "schorsing"),
                          ("ontslag met opzegtermijn", "einde"),
                          ("staking", "schorsing"),
                          ("pensioen", "einde"),
                          ("ontslag om dringende reden", "einde")],
                  "Schorsing of einde?", WW),
             ]),
        dict(kop="Einde van de overeenkomst",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("beide partijen zijn het eens", "onderling akkoord"),
                          ("de werkgever zegt op met een termijn", "opzegging"),
                          ("de werkgever betaalt in plaats van een termijn te laten werken",
                           "een opzeggingsvergoeding"),
                          ("een zware fout, zonder termijn en zonder vergoeding",
                           "dringende reden"),
                          ("de einddatum van een tijdelijk contract is bereikt",
                           "het verstrijken van de termijn"),
                          ("het document met de reden van het einde", "het C4")],
                  "Hoe noemen we dit?", WL),
                 ("open", "Binnen welke termijn moet een ontslag om dringende reden gegeven "
                          "worden?",
                  "Binnen drie werkdagen nadat de werkgever het feit kent, en de reden moet "
                  "binnen drie werkdagen daarna aangetekend meegedeeld worden.", 3),
                 ("open", "Waarom bestaat er een opzegtermijn?",
                  "Zo heeft de werknemer tijd om ander werk te zoeken en de werkgever tijd om "
                  "een vervanger te vinden.", 2),
             ]),
        dict(kop="Rekenen",
             opdracht="Reken uit en schrijf de tussenstap op.",
             oefeningen=[
                 ("kort", "Een werknemer verdient 2 600 euro bruto per maand. Hoeveel is "
                          "dat per week, als je rekent met 52 weken op 12 maanden?",
                  "2 600 maal 12 gedeeld door 52 is 600,00 euro per week", WL),
                 ("kort", "Zijn opzegtermijn is 9 weken en de werkgever verbreekt "
                          "onmiddellijk. Hoeveel bedraagt de vergoeding, zonder de extra's?",
                  "5 400,00 euro", WW),
                 ("open", "Waarom zit er meestal meer in zo'n vergoeding dan het brutoloon "
                          "alleen?",
                  "De vergoeding bevat ook het vakantiegeld, de eindejaarspremie en de "
                  "voordelen in natura over die periode.", 3),
             ]),
    ])


# ============================================================
zet("de-loonfiche-en-de-loonberekening",
    titel="De loonfiche en de loonberekening",
    reeksen=[
        dict(kop="Van bruto naar netto",
             opdracht="Zet de stappen in de juiste orde, van 1 tot 5.",
             oefeningen=[
                 ("rij", [("het brutoloon", "1"),
                          ("de persoonlijke RSZ-bijdrage van 13,07 % eraf", "2"),
                          ("het belastbaar loon", "3"),
                          ("de bedrijfsvoorheffing eraf", "4"),
                          ("het nettoloon", "5"),
                          ("de werkgeversbijdrage, die de werkgever er bovenop betaalt",
                           "staat niet in deze reeks")],
                  "Welke stap?", WL),
                 ("open", "Wat is het verschil tussen de persoonlijke RSZ-bijdrage en de "
                          "werkgeversbijdrage?",
                  "De persoonlijke bijdrage gaat van het brutoloon van de werknemer af. De "
                  "werkgeversbijdrage komt er bovenop en kost de werkgever extra; de "
                  "werknemer ziet die niet op zijn rekening.", 3),
             ]),
        dict(kop="Reken de fiche na",
             opdracht="Het brutoloon is 2 400,00 euro. De RSZ-bijdrage is 13,07 %, de "
                      "bedrijfsvoorheffing is 410,00 euro. Vul de tabel aan.",
             oefeningen=[
                 ("tabel",
                  ["Lijn", "Bedrag"],
                  [["Brutoloon", "2 400,00"],
                   ["RSZ 13,07 %", None],
                   ["Belastbaar loon", None],
                   ["Bedrijfsvoorheffing", "410,00"],
                   ["Nettoloon", None]],
                  "RSZ: 313,68 euro. Belastbaar loon: 2 086,32 euro. Nettoloon: "
                  "1 676,32 euro.",
                  "120px"),
                 ("kort", "Hoeveel procent van het brutoloon houdt deze werknemer netto "
                          "over?", "ongeveer 69,8 %", W),
                 ("kort", "De werkgeversbijdrage is 25 %. Wat kost deze werknemer de "
                          "werkgever die maand?", "3 000,00 euro", WW),
             ]),
        dict(kop="De fiche lezen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("het loon voor de gewerkte uren", "het basisloon"),
                          ("de vergoeding voor een feestdag", "feestdagloon"),
                          ("het extra voor avond- of nachtwerk", "een ploegen- of nachtpremie"),
                          ("het bedrag voor de treinrit naar het werk",
                           "de woon-werkvergoeding"),
                          ("het bedrag dat één keer per jaar komt", "de eindejaarspremie"),
                          ("de 92 % extra die in mei komt", "het dubbel vakantiegeld")],
                  "Welke lijn?", WL),
                 ("open", "Waarom staat er op de fiche van december vaak een veel hogere "
                          "bedrijfsvoorheffing?",
                  "De eindejaarspremie wordt als een uitzonderlijke vergoeding apart en tegen "
                  "een hoger tarief ingehouden.", 3),
             ]),
    ])


# ============================================================
zet("de-marketingmix",
    titel="De marketingmix",
    reeksen=[
        dict(kop="De vier p's",
             opdracht="Zet achter elke beslissing welke p het is.",
             oefeningen=[
                 ("rij", [("de verpakking vernieuwen", "product"),
                          ("een korting van 10 % bij twee stuks", "prijs"),
                          ("ook via een webwinkel verkopen", "plaats of distributie"),
                          ("een advertentie op de radio", "promotie"),
                          ("een tweede smaak toevoegen", "product"),
                          ("de folder in de bus", "promotie")],
                  "Welke p?", WW),
                 ("rij", [("enkel in eigen winkels verkopen", "exclusieve distributie"),
                          ("in elke supermarkt liggen", "intensieve distributie"),
                          ("bij een beperkt aantal gekozen winkels", "selectieve distributie"),
                          ("zonder tussenhandel aan de klant", "directe verkoop"),
                          ("de weg van producent tot klant", "het distributiekanaal"),
                          ("de winkel die van de groothandel koopt", "de kleinhandel")],
                  "Welke vorm?", WL),
             ]),
        dict(kop="Prijs bepalen",
             opdracht="Reken uit en schrijf de tussenstap op.",
             oefeningen=[
                 ("kort", "De aankoopprijs is 18,00 euro. De winkel rekent 60 % marge op de "
                          "aankoopprijs. Wat is de verkoopprijs zonder btw?",
                  "28,80 euro", W),
                 ("kort", "Met 21 % btw erbij, wat betaalt de klant?", "34,85 euro", W),
                 ("kort", "Een ander product kost de winkel 12,00 euro en gaat voor 19,99 euro "
                          "zonder btw over de toonbank. Hoeveel procent marge is dat op de "
                          "aankoopprijs?", "ongeveer 66,6 %", WW),
                 ("open", "Wat is psychologische prijszetting, en waarom werkt 19,99 euro?",
                  "Je zet de prijs net onder een rond getal, omdat de klant het eerste cijfer "
                  "leest en de prijs als negentien euro ervaart in plaats van twintig.", 3),
             ]),
        dict(kop="Marktonderzoek",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("rij", [("cijfers die al bestaan opzoeken", "deskresearch"),
                          ("zelf mensen bevragen", "fieldresearch"),
                          ("een gesprek met tien klanten samen", "een focusgroep"),
                          ("de groep die je wil bereiken", "de doelgroep"),
                          ("de markt in stukken verdelen", "segmenteren"),
                          ("de plaats die je product in het hoofd van de klant inneemt",
                           "de positionering")],
                  "Hoe noemen we dit?", WL),
                 ("open", "Je vraagt op je eigen Instagram of mensen je nieuwe product zouden "
                          "kopen en 90 % zegt ja. Waarom is dat geen betrouwbaar onderzoek?",
                  "Je volgers zijn geen willekeurige steekproef, ze kennen je en willen "
                  "aardig zijn, en zeggen dat je iets zou kopen is niet hetzelfde als het "
                  "kopen.", 3),
             ]),
    ])


# ============================================================
zet("soorten-klanten-en-het-verkoopgesprek",
    titel="Soorten klanten en het verkoopgesprek",
    reeksen=[
        dict(kop="De fasen van het gesprek",
             opdracht="Zet de fasen in de juiste orde, van 1 tot 6.",
             oefeningen=[
                 ("rij", [("de klant begroeten en contact maken", "1"),
                          ("vragen stellen om de behoefte te kennen", "2"),
                          ("het product voorstellen dat daarbij past", "3"),
                          ("de bezwaren beantwoorden", "4"),
                          ("de verkoop afsluiten", "5"),
                          ("afscheid nemen en de klant uitlaten", "6")],
                  "Welke fase?", W),
                 ("open", "Waarom stel je eerst vragen in plaats van meteen het duurste "
                          "toestel te tonen?",
                  "Je weet nog niet wat de klant nodig heeft. Wie meteen verkoopt, verkoopt "
                  "vaak het verkeerde en krijgt het terug.", 3),
             ]),
        dict(kop="Open of gesloten vraag",
             opdracht="Zet achter elke vraag of ze open of gesloten is.",
             oefeningen=[
                 ("rij", [("Waarvoor wil u het toestel gebruiken?", "open"),
                          ("Wil u het in het zwart?", "gesloten"),
                          ("Wat vindt u van deze stof?", "open"),
                          ("Betaalt u met kaart?", "gesloten"),
                          ("Hoe heeft u het tot nu toe opgelost?", "open"),
                          ("Is dit uw eerste keer bij ons?", "gesloten")],
                  "Open of gesloten?", W),
                 ("open", "Wanneer is een gesloten vraag juist de beste keuze?",
                  "Aan het einde, om een beslissing vast te leggen, of om een detail te "
                  "bevestigen.", 2),
             ]),
        dict(kop="Bezwaren",
             opdracht="Schrijf bij elk bezwaar één antwoord op dat de klant niet wegduwt.",
             oefeningen=[
                 ("open", "Ik vind het te duur.",
                  "Vraag waarmee de klant vergelijkt, en zet er dan wat hij ervoor krijgt "
                  "naast: de garantie, de levensduur, de service. Nooit zeggen dat het niet "
                  "duur is.", 3),
                 ("open", "Ik moet er nog eens over nadenken.",
                  "Vraag wat er nog ontbreekt om te beslissen. Zo weet je of er een echt "
                  "bezwaar achter zit, en spreek je af wanneer je terugkomt.", 3),
                 ("open", "Bij de concurrent is het goedkoper.",
                  "Vraag welk toestel dat precies is. Vaak is het een ander model of zonder "
                  "service. Zeg wat er bij jou wel in zit.", 3),
                 ("open", "Waarom is tegenspreken bijna altijd een slecht idee?",
                  "De klant moet dan zijn gezicht verliezen om nog ja te zeggen. Wie het "
                  "bezwaar eerst erkent, houdt het gesprek open.", 3),
             ]),
    ])


# ============================================================
zet("commerciele-documenten-en-de-documentenstroom",
    titel="Commerciële documenten en de documentenstroom",
    reeksen=[
        dict(kop="Welk document?",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de klant vraagt wat het zou kosten", "de prijsaanvraag"),
                          ("de verkoper antwoordt met een prijs", "de offerte of prijsopgave"),
                          ("de klant bestelt", "de bestelbon of order"),
                          ("de verkoper bevestigt de bestelling", "de orderbevestiging"),
                          ("het blad dat met de goederen meerijdt", "de verzendnota"),
                          ("het blad waarmee de klant de levering aftekent", "de leveringsbon")],
                  "Welk document?", WL),
                 ("rij", [("de vraag om te betalen", "de factuur"),
                          ("de factuur die te veel aanrekende rechtzetten", "de creditnota"),
                          ("een bijkomende aanrekening", "een debetnota"),
                          ("de herinnering na de vervaldag", "de aanmaning"),
                          ("het bewijs van betaling", "het rekeninguittreksel"),
                          ("de lijst van wat nog niet betaald is",
                           "de openstaande postenlijst")],
                  "Welk document?", WL),
             ]),
        dict(kop="Wat hoort op een factuur?",
             opdracht="Waar of niet waar?",
             oefeningen=[
                 ("waar", "Een factuur moet een opeenvolgend nummer dragen.", True),
                 ("waar", "Het btw-nummer van de verkoper én van de klant moeten erop staan "
                          "bij een verkoop tussen ondernemingen.", True),
                 ("waar", "De datum van de factuur mag ontbreken als de vervaldag erop "
                          "staat.", False),
                 ("waar", "Een factuur moet de eenheidsprijs en het aantal vermelden.", True),
                 ("waar", "Een verkoop aan een particulier in een winkel vraagt altijd een "
                          "factuur.", False),
                 ("waar", "Een factuur mag elektronisch bewaard worden.", True),
             ]),
        dict(kop="Een factuur narekenen",
             opdracht="Reken uit en schrijf de tussenstap op. 20 stuks aan 45,00 euro, 10 % "
                      "handelskorting, 2 % contantkorting, btw 21 %, verzendkosten 25,00 euro "
                      "met 21 % btw.",
             oefeningen=[
                 ("kort", "Wat is het brutobedrag van de goederen?", "900,00 euro", W),
                 ("kort", "Hoeveel is de handelskorting?", "90,00 euro", W),
                 ("kort", "Wat is het bedrag na handelskorting?", "810,00 euro", W),
                 ("kort", "Hoeveel is de contantkorting van 2 %?", "16,20 euro", W),
                 ("kort", "Wat is de maatstaf van heffing, met de verzendkosten erbij?",
                  "818,80 euro", W),
                 ("kort", "Hoeveel btw komt erbij?", "171,95 euro", W),
                 ("kort", "Wat moet de klant betalen?", "990,75 euro", W),
             ]),
    ])


# ============================================================
zet("transport-expeditie-en-logistiek",
    titel="Transport, expeditie en logistiek",
    reeksen=[
        dict(kop="Vervoerswijzen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de snelste manier over grote afstand", "het vliegtuig"),
                          ("de goedkoopste manier voor grote volumes over zee", "het schip"),
                          ("het vervoersmiddel dat tot aan de deur komt", "de vrachtwagen"),
                          ("vervoer van olie en gas zonder voertuig", "de pijpleiding"),
                          ("vervoer over het water in het binnenland", "het binnenschip"),
                          ("twee wijzen combineren in één rit", "intermodaal vervoer")],
                  "Welke wijze?", WL),
                 ("rij", [("de begeleidende brief bij een vrachtwagen", "de CMR-vrachtbrief"),
                          ("het document bij vervoer per zeeschip", "het cognossement"),
                          ("de doos waarin containers gestapeld staan",
                           "de container zelf, 20 of 40 voet"),
                          ("de houten plaat waarop goederen gestapeld staan", "de pallet"),
                          ("wie het vervoer organiseert zonder zelf te rijden",
                           "de expediteur"),
                          ("wie het vervoer uitvoert", "de vervoerder")],
                  "Hoe noemen we dit?", WL),
             ]),
        dict(kop="Rekenen aan vervoer",
             opdracht="Reken uit en schrijf de tussenstap op.",
             oefeningen=[
                 ("kort", "Een pallet is 1,20 m op 0,80 m. Hoeveel pallets passen er naast "
                          "elkaar in een laadruimte van 2,40 m breed, als je ze met de lange "
                          "zijde dwars zet?", "2 pallets", W),
                 ("kort", "Een vrachtwagen laadt 33 pallets van 420 kg. Wat is het "
                          "laadgewicht?", "13 860 kg", WW),
                 ("kort", "Het vervoer kost 1,35 euro per kilometer over 480 km. Wat kost de "
                          "rit?", "648,00 euro", W),
                 ("kort", "Wat kost het vervoer per pallet, bij 33 pallets?",
                  "19,64 euro", W),
                 ("open", "Waarom rijdt een vervoerder liever niet leeg terug?",
                  "De kosten lopen door: brandstof, loon en afschrijving. Een retourlading "
                  "maakt de rit pas rendabel.", 3),
             ]),
        dict(kop="Voorraad",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("de voorraad waaronder je niet wil zakken", "de veiligheidsvoorraad"),
                          ("het niveau waarop je opnieuw bestelt", "het bestelpunt"),
                          ("de tijd tussen bestellen en leveren", "de levertijd"),
                          ("leveren net voor het nodig is, zonder voorraad", "just in time"),
                          ("het eerst binnengekomen gaat het eerst eruit", "fifo"),
                          ("hoe vaak de voorraad per jaar vernieuwd wordt",
                           "de omloopsnelheid")],
                  "Hoe noemen we dit?", WL),
                 ("kort", "Een zaak verkoopt 40 stuks per week en de levertijd is 2 weken. Bij "
                          "welke voorraad bestelt ze, met een veiligheidsvoorraad van "
                          "30 stuks?", "110 stuks", WW),
                 ("open", "Geef één voordeel en één risico van just in time.",
                  "Je hebt bijna geen geld in voorraad zitten en geen opslagkosten, maar één "
                  "staking of één file bij de leverancier legt je productie stil.", 3),
             ]),
    ])


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-behoeften-schaarste-en-soorten-goederen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Primair is wat je nodig hebt om te leven en mee te kunnen doen, secundair is "
                   "wat daarbovenop komt. Let op het woordje derde in het derde paar sneakers: "
                   "kledij is primair, maar een derde paar van hetzelfde niet. Het is dus niet "
                   "het soort goed dat beslist maar de hoeveelheid die je al hebt.",
            waarom=[
                None,
                "Dit is het punt van de hele reeks: de grens is niet natuurlijk maar "
                "maatschappelijk. Daarom spreekt men van relatieve armoede, gemeten aan wat in "
                "een land nodig is om mee te doen, en niet enkel aan overleven.",
            ],
        ),
        dict(
            aanpak="Houd twee indelingen uit elkaar. De eerste gaat over wie het gebruikt: een "
                   "productiegoed dient om mee te maken, een consumptiegoed om te gebruiken, en "
                   "dat laatste kan eenmalig of duurzaam zijn. De tweede gaat over de verhouding "
                   "tussen twee goederen: vervangen ze elkaar of hebben ze elkaar nodig?",
            waarom=[
                "Let op het verschil tussen een vrij en een economisch goed. Lucht is vrij omdat "
                "er genoeg van is voor iedereen; zodra er een prijs op staat, is het economisch. "
                "Datzelfde goed kan dus van categorie veranderen, zoals drinkwater in een droog "
                "land.",
                "De toets is eenvoudig: wordt het andere goed meer of minder gevraagd als dit "
                "duurder wordt? Meer betekent vervangend, minder betekent aanvullend. Daarmee "
                "kan je elk paar zelf nagaan zonder het rijtje te kennen.",
            ],
        ),
        dict(
            aanpak="Schaarste, kiezen en alternatieve kosten horen bij elkaar: omdat er niet "
                   "genoeg is, moet je kiezen, en elke keuze kost je wat je niet koos. Antwoord "
                   "bij alternatieve kosten dus nooit met een bedrag maar met het alternatief "
                   "zelf.",
            waarom=[
                "Zeldzaam is een eigenschap van het goed, schaars een verhouding tussen "
                "hoeveelheid en vraag. Een maansteen is zeldzaam maar economisch oninteressant; "
                "zand is overal en toch schaars omdat er zo veel van gevraagd wordt.",
                "Let op de laatste zin van het antwoord: de 55 euro is niet de alternatieve kost. "
                "Dat geld had je al; wat je echt verliest, zijn de schoenen. Zo meet een "
                "econoom de kost van een keuze.",
                "Dit is het verschil tussen schaarste en armoede. Een rijk land heeft meer "
                "middelen maar nog altijd een beperkt aantal uren, mensen en grondstoffen, en "
                "dus blijft elke keuze een keuze tegen iets anders.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-nut-voorkeuren-en-de-vraag-van-de-consument-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Totaal nut en grensnut zijn twee kolommen van dezelfde tabel. Het grensnut "
                   "is altijd het verschil tussen twee opeenvolgende totalen, dus reken van rij "
                   "tot rij en niet vanaf het begin. Daalt het totaal, dan is het grensnut "
                   "negatief.",
            waarom=[
                "Reken mee: de grensnutten zijn 20, 16, 10, 4 en −2, en dat zijn telkens de "
                "verschillen tussen twee totalen. Merk op dat het grensnut al daalt vanaf de "
                "eerste pannenkoek terwijl het totaal nog stijgt; dat is precies het verschil "
                "tussen de twee kolommen.",
                "De grens ligt waar het grensnut door nul gaat. Alles met een positief grensnut "
                "voegt nog iets toe, hoe weinig ook; de vijfde haalt er iets af.",
                None,
            ],
        ),
        dict(
            aanpak="Houd twee bewegingen uit elkaar. Verandert de prijs van het goed zelf, dan "
                   "schuif je langs de curve. Verandert iets anders, dan verschuift de hele "
                   "curve. Vraag je bij elke lijn dus eerst af: gaat dit over de prijs van dit "
                   "goed, of over iets anders?",
            waarom=[
                "Vergelijk brood met restaurantbezoek: bij een hoger inkomen eet je niet meer "
                "brood, maar ga je wel vaker uit eten. Daarom noemt men brood een noodzakelijk "
                "goed en een restaurantbezoek een luxegoed.",
                None,
                "Let bij je tekening op twee dingen: de prijs hoort op de verticale as, en de "
                "tweede curve ligt volledig naast de eerste en kruist ze niet. Een gestegen "
                "inkomen verandert immers bij elke prijs de gevraagde hoeveelheid.",
            ],
        ),
        dict(
            aanpak="Omzet is altijd prijs maal hoeveelheid. Reken de twee situaties apart uit en "
                   "vergelijk daarna; reken nooit met het verschil in prijs alleen, want de "
                   "hoeveelheid verandert mee.",
            waarom=[
                "400 × 2,50 = 1 000 euro.",
                "360 × 2,80 = 1 008 euro. Merk op dat de prijs met 12 procent steeg en de "
                "verkoop met 10 procent zakte; daarom blijft de omzet bijna gelijk.",
                "Het punt van deze oefening is de laatste zin: omzet is geen winst. Veertig "
                "broden minder bakken kost ook minder meel, energie en werk, dus kan de winst "
                "stijgen terwijl de omzet nauwelijks beweegt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-productiefactoren-en-de-productie-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vier factoren, en bij elk hoort één vergoeding: arbeid krijgt loon, natuur "
                   "pacht of huur, kapitaal intrest, ondernemerschap winst. Leer die vier paren "
                   "samen, dan heb je de twee rijen van deze reeks in één keer.",
            waarom=[
                "Kapitaal is in de economie niet hetzelfde als geld. Het is alles wat zelf "
                "gemaakt is om verder mee te produceren: een oven, een bestelwagen, een gebouw. "
                "Het weiland is natuur, want niemand maakte het.",
                "Let op de vergoeding voor ondernemerschap. Winst is geen vast bedrag zoals een "
                "loon of een huur: ze kan ook negatief zijn, en dat is net waarom deze factor "
                "het risico draagt.",
            ],
        ),
        dict(
            aanpak="De sectoren volgen de weg van een product: winnen, verwerken, verkopen, en "
                   "daarnaast de niet-commerciële diensten. Let op de quartaire sector, die "
                   "vaak vergeten wordt: zorg, onderwijs en overheid.",
            waarom=[
                "De vier vislijnen staan er bewust in dezelfde orde: visser, fabriek, winkel, "
                "ziekenhuis. Zo zie je dat niet het product maar de bewerking de sector bepaalt.",
                "Drie schakels volstaan. Het punt is de laatste zin: elke schakel voegt waarde "
                "toe, en de prijs in de winkel is de som van al die toevoegingen. Dat is ook de "
                "gedachte achter de belasting over de toegevoegde waarde.",
                "Let op het tweede deel van het antwoord, want dat wordt het vaakst vergeten. "
                "Arbeidsverdeling maakt sneller en beter werk mogelijk, maar ook eentoniger werk "
                "en een grotere afhankelijkheid: valt er één schakel weg, dan staat alles stil.",
            ],
        ),
        dict(
            aanpak="Productiviteit is altijd een deling: hoeveel per eenheid. Lees goed per wat "
                   "er gevraagd wordt, want per uur, per werknemer en per werknemer per uur zijn "
                   "drie verschillende getallen. Bij een stijging in procent neem je het verschil "
                   "gedeeld door het oude getal.",
            waarom=[
                "Reken de laatste twee na: 360 gedeeld door 4 werknemers gedeeld door 6 uur is "
                "15 stuks, en 480 gedeeld door 24 uren werk is 20 stuks. Deel dus altijd door "
                "het aantal werknemers én het aantal uren als beide in de vraag staan. De "
                "stijging van 30 naar 37,5 is 7,5 gedeeld door 30, dus 25 procent.",
                "Twee van de genoemde manieren volstaan. Ze hebben alle iets gemeen: niet de "
                "inspanning verandert maar de omstandigheden errond. Dat is ook het antwoord op "
                "de vraag waarom een land rijker wordt zonder dat men langer werkt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-kosten-van-de-producent-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag beslist: verandert deze kost als je één stuk meer maakt? Zo ja, "
                   "dan is ze variabel; zo niet, dan is ze vast. Let op de elektriciteit, want "
                   "die hangt ervan af waarvoor ze dient: stroom voor de machines is variabel, "
                   "de verlichting van het atelier zou vast zijn.",
            waarom=[
                "Het loon van de zaakvoerder staat hier bij de vaste kosten, en het loon van wie "
                "per stuk werkt zou variabel zijn. Het is dus niet de soort kost maar de band "
                "met de productie die beslist.",
                "Dit is ook waarom vaste kosten gevaarlijk zijn voor een jonge zaak. In een "
                "slechte maand lopen ze gewoon door, en daar moet de spaarpot voor dienen.",
            ],
        ),
        dict(
            aanpak="Werk de tabel kolom per kolom af. De variabele kost is het aantal maal 8, de "
                   "totale kost is dat plus 1 200, en de kostprijs per stuk is de totale kost "
                   "gedeeld door het aantal. Reken de laatste kolom altijd uit de totale kost en "
                   "niet uit de vorige rij.",
            waarom=[
                "Reken één rij na om te zien of je het goed hebt: 400 × 8 = 3 200; plus 1 200 is "
                "4 400; gedeeld door 400 is 11 euro per stuk. Merk op dat de kostprijs per stuk "
                "van 20 naar 10 euro daalt terwijl er niets aan de werkwijze verandert.",
                "Dit is het schaalvoordeel in één zin. Je kan het ook aan de getallen zien: de "
                "vaste kost per stuk gaat van 12 euro bij 100 stuks naar 2 euro bij 600, en de "
                "variabele 8 euro blijft gewoon staan.",
                "1 200 gedeeld door 600 = 2 euro. Tel er de variabele 8 euro bij en je hebt weer "
                "de 10 euro uit de tabel; dat is een goede controle op je hele kolom.",
            ],
        ),
        dict(
            aanpak="Het break-evenpunt is één deling: de vaste kosten gedeeld door de brutowinst "
                   "per stuk. Reken dus altijd eerst die brutowinst uit, dus de prijs min de "
                   "variabele kost per stuk, en deel daarna. Verandert een vaste kost, dan "
                   "verandert alleen de teller.",
            waarom=[
                "20 − 8 = 12 euro. Deze marge heet ook de dekkingsbijdrage: elk verkocht stuk "
                "draagt 12 euro bij om de vaste kosten te dekken.",
                "1 200 gedeeld door 12 = 100 stuks. Tel na: 100 × 12 = 1 200, dus de vaste "
                "kosten zijn precies gedekt en de winst is nul.",
                "100 × 20 = 2 000 euro. Merk op dat de omzet in het break-evenpunt gelijk is aan "
                "de totale kosten uit de tabel hierboven, en dat is ook de betekenis van "
                "break-even.",
                "300 × 12 = 3 600; min 1 200 = 2 400 euro winst. Reken nooit 300 × 20 min 1 200, "
                "want dan vergeet je de variabele kosten.",
                "De brutowinst per stuk blijft 12 euro, alleen de vaste kosten stijgen tot "
                "1 500. Dus 1 500 / 12 = 125 stuks: vijfentwintig stuks meer om dezelfde 300 "
                "euro huur te dragen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-opbrengsten-optimale-productiegrootte-en-aanbod-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Let op het woord marginaal: dat gaat altijd over één stuk extra, niet over "
                   "het geheel en niet over het gemiddelde. Drie soorten cijfers dus: totaal, "
                   "gemiddeld en marginaal. De optimale productiegrootte vind je enkel met de "
                   "marginale cijfers.",
            waarom=[
                None,
                "Je kan de regel zelf nagaan. Brengt een stuk extra meer op dan het kost, dan "
                "stijgt je winst, dus maak je het. Kost het meer dan het opbrengt, dan daalt je "
                "winst. Op het punt waar ze gelijk zijn, kan het niet beter meer.",
            ],
        ),
        dict(
            aanpak="Vul de tabel in twee kolommen: eerst de omzet als aantal maal 15, dan de "
                   "winst als omzet min totale kosten. Let op dat de variabele kost per stuk hier "
                   "niet gelijk blijft; bij grotere aantallen loopt ze op, en dat is net wat de "
                   "tabel wil laten zien.",
            waarom=[
                "Reken de eerste rij na: 50 × 15 = 750 euro omzet, en met 1 000 euro kosten is "
                "dat 250 euro verlies. Merk op dat verlies niet betekent dat de zaak slecht "
                "werkt: bij 50 stuks zijn de vaste kosten van 600 euro simpelweg nog niet "
                "verdeeld.",
                "Reken de stappen na: van 100 naar 150 stuks stijgt de winst met 250 euro, van "
                "150 naar 200 nog maar met 50 euro. De opbrengst per stuk blijft 15 euro, dus "
                "het is de kost per extra stuk die oploopt. Daarom nadert het optimum.",
            ],
        ),
        dict(
            aanpak="Het aanbod werkt omgekeerd aan de vraag: een hogere prijs maakt produceren "
                   "aantrekkelijker, dus de aanbodcurve stijgt. Vraag je bij elke lijn af of het "
                   "om de prijs van het goed gaat of om de kosten van de producent; het eerste "
                   "beweegt langs de curve, het tweede verschuift ze.",
            waarom=[
                None,
                "Let bij je tekening op de twee richtingen: de vraag daalt, het aanbod stijgt, en "
                "ze kruisen in één punt. Zet op beide assen de eenheid, want zonder eenheden zegt "
                "een evenwichtspunt niets.",
                "Dit is een maximumprijs, en het antwoord geldt algemeen: onder het evenwicht "
                "ontstaat een tekort, boven het evenwicht een overschot. Daarom gaan "
                "prijsplafonds bijna altijd met wachtlijsten of met een zwarte markt samen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-soorten-ondernemingen-en-hun-verplichtingen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De rechtsvormen verschillen op twee punten: is er een aparte rechtspersoon, "
                   "en loopt je privévermogen risico? Bij een eenmanszaak is er geen scheiding, "
                   "bij een bv of nv wel. De vzw en de cv verschillen van de rest niet in "
                   "aansprakelijkheid maar in doel.",
            waarom=[
                "De eenmanszaak staat twee keer in deze rij, als eerste en als laatste. Dat is "
                "bewust: het ontbreken van een rechtspersoon en het meespelen van het "
                "privévermogen zijn twee kanten van hetzelfde.",
                "Let op het woord concreet in de vraag. Het antwoord moet dus niet de definitie "
                "herhalen maar zeggen waar de schuldeisers wel en niet aan kunnen. Een "
                "uitzondering bestaat wel: een bestuurder die duidelijke fouten maakte, kan "
                "alsnog persoonlijk aansprakelijk zijn.",
                "Twee van de genoemde voordelen volstaan. Zet er in gedachten altijd het nadeel "
                "naast, want dat is wat de keuze echt maakt: je staat met je eigen vermogen in "
                "voor de schulden.",
            ],
        ),
        dict(
            aanpak="De orde van de opstartstappen volgt een logica: eerst nagaan of je het beroep "
                   "mag uitoefenen, dan bestaan als onderneming, dan een rekening, dan de btw, "
                   "dan het sociaal statuut, dan de verzekeringen. Het ondernemingsnummer komt "
                   "vroeg, want je hebt het voor bijna elke volgende stap nodig.",
            waarom=[
                "Merk op waarom de vergunning vooraan staat. Blijkt dat je beroep een "
                "erkenning vraagt die je niet haalt, dan heb je aan een ondernemingsnummer en "
                "een rekening niets.",
                "Dit is het grote verschil tussen een werknemer en een zelfstandige. Bij een "
                "werknemer houdt de werkgever alles af; als zelfstandige betaal je zelf, per "
                "kwartaal, en in het begin op een geschat inkomen dat later herzien wordt.",
            ],
        ),
        dict(
            aanpak="Zes uitspraken over verplichtingen. Toets ze aan twee vragen: geldt dit voor "
                   "elke onderneming of enkel voor een vennootschap, en gaat het over een "
                   "termijn die je moet kennen? Let op de uitspraken met een getal erin, want "
                   "daar zit de fout meestal.",
            waarom=[
                "Waar, en die jaarrekening is openbaar. Iedereen kan ze opvragen, ook een "
                "concurrent of een leverancier die wil weten of je gezond bent. Een eenmanszaak "
                "moet dat niet.",
                None,
                "Niet waar. De boekhoudwet vraagt zeven jaar, en de fiscale bewaartermijn werd "
                "ondertussen verlengd tot tien jaar voor recente boekjaren. Houd dus tien jaar "
                "aan; drie jaar is in elk geval veel te kort.",
                "Waar, en dat is de kern van een vzw. Ze mag wel winst maken, en dat verrast "
                "velen; ze mag die alleen niet uitkeren maar moet ze opnieuw voor haar doel "
                "gebruiken.",
                "Waar. Dat is ook meteen een stuk van de kosten en de drempel om een "
                "vennootschap op te richten; voor een eenmanszaak heb je geen notaris nodig.",
                "Waar. De RSZ gaat over werknemers, dus zonder personeel sluit je je enkel aan "
                "bij een sociaal verzekeringsfonds voor zelfstandigen. Neem je één werknemer "
                "aan, dan komt de RSZ er wel bij.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-organisatiestructuur-van-een-onderneming-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Twee begrippenparen die bij elkaar horen: spanwijdte en aantal niveaus gaan "
                   "over de vorm van de organisatie, centralisatie en decentralisatie over waar "
                   "beslist wordt. Let op dat de twee samenhangen: een grote spanwijdte geeft "
                   "weinig niveaus en dus een plattere organisatie.",
            waarom=[
                None,
                "Er is geen beste spanwijdte, en dat is het antwoord dat ze willen horen. Werkt "
                "iedereen hetzelfde en zelfstandig, dan kan één leidinggevende er veel aan; is "
                "het werk moeilijk of nieuw voor de mensen, dan kan hij er maar enkele begeleiden.",
            ],
        ),
        dict(
            aanpak="Vijf structuren, en elk is een antwoord op de vraag waarop je indeelt: op "
                   "gezagslijn, op specialisme, op afdeling, op product of op niets. Houd de "
                   "lijn-staf en de matrix uit elkaar: een stafmedewerker geeft advies, in een "
                   "matrix hebben twee mensen echt gezag.",
            waarom=[
                "Let op het verschil tussen de functionele structuur en de divisiestructuur. "
                "Dezelfde onderneming kan op beide manieren ingedeeld worden, en grote bedrijven "
                "doen het vaak dubbel: per land én per afdeling. Dan is het een matrix.",
                "Het risico is niet de drukte maar de tegenstrijdige opdracht. Daarom spreekt men "
                "af wie voorgaat bij een conflict; zonder die afspraak werkt een matrix niet.",
                "Let bij je tekening op de stippellijn. Die is het hele punt van de oefening: de "
                "boekhouder staat naast de lijn en geeft advies, dus hij hangt niet boven de "
                "bakkers en hij kan hun niets opdragen.",
            ],
        ),
        dict(
            aanpak="De laatste reeks gaat over het verschil tussen de tekening en de "
                   "werkelijkheid. Het organogram toont het gezag, de informele organisatie toont "
                   "de echte wegen van informatie. Bij de laatste oefening moet je het geschonden "
                   "principe bij naam noemen.",
            waarom=[
                "De informele organisatie is niet iets wat je moet bestrijden. Een goede "
                "leidinggevende kent ze en gebruikt ze, want wie echt weet hoe iets werkt, staat "
                "zelden bovenaan het organogram.",
                "De eenheid van bevel is een van de oudste beginselen van organisatieleer. Merk "
                "op dat het niet tegen samenwerking is: je mag met tien mensen overleggen, maar "
                "je opdrachten en je beoordeling komen van één persoon.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-afdelingen-en-hun-samenwerking-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zoek bij elke taak wie het eigenaarschap heeft en niet wie erbij betrokken "
                   "is. Bijna elke taak raakt meerdere afdelingen, maar één afdeling voert ze "
                   "uit. Twee paren worden vaak verwisseld: aankoop koopt in, logistiek "
                   "verplaatst; marketing maakt bekend, verkoop sluit af.",
            waarom=[
                None,
                "Let op de klant bellen die niet betaalt: dat is boekhouding en niet verkoop. De "
                "opvolging van de betaling hoort bij wie de factuur maakte, al zal de verkoper "
                "er wel van willen weten voor hij opnieuw levert.",
            ],
        ),
        dict(
            aanpak="Bij elk geval is de vraag welke twee afdelingen iets van elkaar moesten "
                   "weten. Zoek dus de twee uiteinden van de informatie: wie beloofde iets, en "
                   "wie moest het waarmaken. Dat is bijna altijd het paar dat men vraagt.",
            waarom=[
                "Merk op dat geen enkel van deze zes gevallen een fout van één persoon is. Het is "
                "telkens informatie die niet doorgegeven werd, en dat is precies waarom een "
                "onderneming vast overleg tussen afdelingen organiseert.",
                "Deze vraag gaat eigenlijk over de kas, dus over liquiditeit. Een korte "
                "betaaltermijn bij de leverancier is goedkoper, maar enkel als je het geld dan "
                "ook hebt; daarom moeten die twee afdelingen samen beslissen.",
            ],
        ),
        dict(
            aanpak="De documentenstroom in huis volgt de goederen, met twee controles errond: "
                   "eerst kijken of de klant mag kopen op krediet, achteraan of hij ook betaalt. "
                   "Zet de kredietcontrole dus vooraan, nog voor het magazijn iets klaarzet.",
            waarom=[
                "Let op stap 2, want die wordt het vaakst te laat gezet. Een klant die niet "
                "kredietwaardig is, kijk je na voor de goederen het huis uit zijn; daarna heb je "
                "enkel nog een onbetaalde factuur en geen goederen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-werving-selectie-en-de-werkplek-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Houd twee documenten uit elkaar: de functiebeschrijving gaat over de job, "
                   "het profiel over de persoon. En twee wegen: intern zoek je bij je eigen "
                   "mensen, extern buiten de deur. Die twee woorden, functie en profiel, "
                   "verwarren het meest.",
            waarom=[
                None,
                "Er is bij elk ook een nadeel dat je mag noemen: intern blijft het bedrijf in "
                "zijn eigen gewoonten zitten en komt er een plaats elders vrij, extern duurt het "
                "langer en weet je minder zeker wat je krijgt.",
            ],
        ),
        dict(
            aanpak="Eén vraag beslist of iets gevraagd mag worden: heeft dit met de job te maken? "
                   "Alles wat over de taken, de uren of de vereiste bekwaamheid gaat, mag. Alles "
                   "wat over je persoon gaat zonder band met de job, mag niet: geloof, "
                   "gezinsplannen, afkomst, gezondheid, lidmaatschap.",
            waarom=[
                "Let op het rijbewijs. Dat is het enige antwoord met een voorwaarde erbij, en dat "
                "is net de regel in actie: voor een chauffeur mag het gevraagd worden, voor een "
                "bureaufunctie niet.",
                "Noem in je antwoord de twee delen: het is discriminatie op grond van geslacht, "
                "én het zegt niets over de bekwaamheid. Dat tweede is de toets die je bij elke "
                "andere vraag opnieuw kan gebruiken.",
            ],
        ),
        dict(
            aanpak="Veiligheid op het werk is geregeld met vaste namen en vaste stappen. Onthoud "
                   "de drie die het vaakst terugkomen: de interne dienst voor preventie en "
                   "bescherming, de veiligheidsfiche bij een gevaarlijk product, en de aangifte "
                   "bij de verzekeraar na een ongeval.",
            waarom=[
                "Let op het verschil tussen de preventiedienst en de ondernemingsraad. De eerste "
                "is een dienst die waakt over veiligheid, de tweede een overlegorgaan tussen "
                "vakbond en directie. Een onderneming heeft ze pas vanaf een bepaald aantal "
                "werknemers.",
                "Drie van de genoemde volstaan. Het laatste punt is het belangrijkste en wordt "
                "het vaakst vergeten: iemand aanwijzen bij wie de nieuwe medewerker terecht kan. "
                "Een onthaal zonder aanspreekpunt is een rondleiding en niets meer.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-aanwerving-en-de-arbeidsovereenkomst-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De soorten overeenkomsten verschillen op twee punten: hoe lang ze duren en "
                   "hoeveel uren je werkt. Deeltijds is dus geen soort naast bepaalde duur maar "
                   "iets wat erbij komt: je kan deeltijds werken met een contract van onbepaalde "
                   "duur.",
            waarom=[
                None,
                "Dit is de reden waarom een deeltijdse overeenkomst strenger geregeld is dan een "
                "volledige. Zonder vast rooster op papier kan niemand nagaan of er geen uren "
                "zwart bij gewerkt worden, en dan verliest de werknemer zijn bescherming.",
            ],
        ),
        dict(
            aanpak="Zes uitspraken over wat er in een overeenkomst hoort. Twee regels geven de "
                   "meeste antwoorden: wat afwijkt van de gewone regel moet op papier, en van een "
                   "minimum kan je nooit geldig afwijken, ook niet met instemming.",
            waarom=[
                "Niet waar, en dat verrast de meesten. Een contract van onbepaalde duur mag in "
                "België mondeling, want de wet vult alles zelf aan. Het is natuurlijk wel "
                "verstandig om het te schrijven.",
                "Waar, en let op het woord uiterlijk. Komt het pas later op papier, dan geldt het "
                "als een overeenkomst van onbepaalde duur, en dat verandert alles bij het einde.",
                "Niet waar. Dat is net wat een cao doet: ze legt een minimum vast waarvan je niet "
                "naar beneden kan afwijken. Instemming van de werknemer verandert dat niet, want "
                "anders zou de bescherming niets waard zijn.",
                None,
                "Niet waar. Een concurrentiebeding moet er uitdrukkelijk in staan, en er hangen "
                "nog voorwaarden aan, zoals een vergoeding en een beperking in tijd en plaats. "
                "Wat niet in het contract staat, geldt dus niet.",
                None,
            ],
        ),
        dict(
            aanpak="Arbeider en bediende hangen samen met het hele overlegstelsel: per sector zit "
                   "een paritair comité, dat sluit cao's, en die gelden voor elke werkgever van "
                   "die sector. Onthoud die keten van drie, want ze komt op het examen terug.",
            waarom=[
                "Let op de laatste lijn: een cao geldt voor elke werkgever van de sector, ook "
                "voor wie er niet bij was en er niet mee instemt. Dat is net de kracht van het "
                "systeem.",
                "Men spreekt van het eenheidsstatuut. Het verschil is kleiner geworden maar niet "
                "verdwenen: de paritaire comités blijven apart, en dus ook de lonen en de "
                "premies per sector.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-schorsing-en-einde-van-de-arbeidsovereenkomst-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Houd één onderscheid vast: bij een schorsing blijft de overeenkomst bestaan "
                   "en valt enkel het werk weg, bij een einde is de overeenkomst zelf voorbij. "
                   "Vraag je dus bij elk geval af: moet deze werknemer daarna terugkomen? Zo ja, "
                   "dan is het een schorsing.",
            waarom=[
                None,
                "Staking staat hier bij de schorsingen, en dat is het verrassende antwoord van "
                "deze rij. Wie staakt, verbreekt zijn contract niet: hij werkt die dagen niet en "
                "krijgt geen loon van de werkgever, maar de overeenkomst loopt door.",
            ],
        ),
        dict(
            aanpak="Vijf manieren waarop een overeenkomst eindigt, en bij elk hoort een eigen "
                   "gevolg: met een termijn, met een vergoeding, of met niets. Het C4 is geen "
                   "manier van eindigen maar het document dat je achteraf nodig hebt bij de "
                   "uitbetalingsinstelling.",
            waarom=[
                "Let op het verschil tussen de opzegtermijn en de opzeggingsvergoeding. Het is "
                "hetzelfde recht in twee vormen: je werkt de termijn uit, of je krijgt het loon "
                "van die periode in één keer.",
                "Let op dat er twee keer drie werkdagen zijn, en dat is de klassieke valkuil. "
                "Eerst drie dagen om te ontslaan, dan nog drie om de reden aangetekend te laten "
                "weten. Wie één van die twee termijnen mist, verliest de dringende reden.",
                "Merk op dat de termijn beide partijen beschermt. Daarom geldt hij ook als de "
                "werknemer zelf opzegt, al is zijn termijn korter.",
            ],
        ),
        dict(
            aanpak="Reken altijd eerst het weekloon uit, want een opzegtermijn staat in weken en "
                   "een loon in maanden. Het weekloon is het maandloon maal twaalf gedeeld door "
                   "tweeënvijftig; deel nooit gewoon door vier, want een maand heeft meer dan "
                   "vier weken.",
            waarom=[
                "2 600 × 12 = 31 200, en gedeeld door 52 is dat 600 euro per week. Deel je door "
                "4, dan kom je op 650 euro uit, en dat is 50 euro per week te veel.",
                "9 × 600 = 5 400 euro. Reken dus altijd met het weekloon en niet met het "
                "maandloon gedeeld door iets.",
                "Dit is waarom een verbrekingsvergoeding hoger uitvalt dan je op het eerste "
                "gezicht zou rekenen. Men spreekt van het lopend loon en de voordelen verworven "
                "krachtens de overeenkomst, en daar zit alles in wat de werknemer die periode "
                "zou gekregen hebben.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-loonfiche-en-de-loonberekening-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De weg van bruto naar netto heeft twee aftrekkingen, in deze orde: eerst de "
                   "RSZ van 13,07 procent, dan de bedrijfsvoorheffing. Die orde telt, want de "
                   "belasting wordt op het belastbaar loon gerekend en niet op het brutoloon. De "
                   "werkgeversbijdrage komt in dit rijtje niet voor.",
            waarom=[
                "Merk op dat de laatste lijn er bewust buiten valt. De werkgeversbijdrage staat "
                "niet op de weg van bruto naar netto, want ze gaat niet van het loon van de "
                "werknemer af.",
                "Dit verschil verklaart waarom een werknemer veel meer kost dan hij netto "
                "overhoudt. De werknemer ziet zijn brutoloon als het begin, terwijl de werkgever "
                "van een bedrag vertrekt dat nog een kwart hoger ligt.",
            ],
        ),
        dict(
            aanpak="Reken de fiche in drie stappen na, telkens met het bedrag van de vorige "
                   "stap. Eerst 13,07 procent van het bruto, dan dat eraf voor het belastbaar "
                   "loon, dan de voorheffing eraf voor het netto. Rond pas aan het einde van elke "
                   "stap af op twee cijfers.",
            waarom=[
                "Reken mee: 13,07 % van 2 400 = 313,68; 2 400 − 313,68 = 2 086,32; 2 086,32 − "
                "410 = 1 676,32 euro netto.",
                "1 676,32 gedeeld door 2 400 = 0,6985, dus ongeveer 69,8 procent. Zo'n "
                "verhouding is nuttig om te onthouden: van een bruto maandloon blijft bij een "
                "gewone werknemer ruwweg twee derde over.",
                "25 % van 2 400 = 600, dus 2 400 + 600 = 3 000 euro. Zet dat naast het netto: de "
                "werkgever betaalt 3 000 euro, de werknemer houdt 1 676,32 euro over. Dat is de "
                "loonwig waar in het nieuws over gesproken wordt.",
            ],
        ),
        dict(
            aanpak="Een loonfiche leest van boven naar beneden: eerst het loon voor gewerkte "
                   "uren, dan de premies en vergoedingen, dan de inhoudingen. Let op de "
                   "bedragen die maar één keer per jaar komen, want die vallen op een fiche "
                   "meteen op: de eindejaarspremie in december en het dubbel vakantiegeld in mei.",
            waarom=[
                "Het dubbel vakantiegeld is bij een bediende 92 procent van één maandloon. Dat "
                "percentage is geen afspraak van je werkgever maar een wettelijk bedrag, en het "
                "komt bovenop het gewone loon van die maand.",
                "Dit is een vraag die veel mensen in december stellen. Het hogere tarief op een "
                "premie is geen vergissing en geen extra belasting: het is een voorschot dat bij "
                "de afrekening van je belastingen verrekend wordt.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-marketingmix-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vier p's, en bij elk een eigen vraag. Product: wat verkoop je? Prijs: wat "
                   "kost het? Plaats: waar is het te krijgen? Promotie: hoe weet de klant het? "
                   "Let op dat een korting prijs is en geen promotie, ook al heet het in de "
                   "winkel een actie.",
            waarom=[
                "De verpakking hoort bij product en niet bij promotie, en dat is het lastigste "
                "van deze rij. Een verpakking is deel van wat de klant koopt; een folder over die "
                "verpakking is promotie.",
                "De drie vormen van distributie verschillen enkel in het aantal verkooppunten: "
                "exclusief is bij één, selectief bij enkele gekozen, intensief bij zo veel "
                "mogelijk. Een merk kiest dat bewust, want overal te koop zijn maakt een product "
                "ook minder bijzonder.",
            ],
        ),
        dict(
            aanpak="Let goed op waarop de marge gerekend wordt. Marge op de aankoopprijs betekent "
                   "dat je bij de aankoopprijs optelt; marge op de verkoopprijs zou een andere "
                   "uitkomst geven. En zet de btw er altijd als laatste bij, op de verkoopprijs "
                   "zonder btw.",
            waarom=[
                "18 × 1,60 = 28,80 euro. Reken dus 18 + 60 % van 18, en niet 18 gedeeld door "
                "0,40, want dat laatste zou een marge op de verkoopprijs zijn.",
                "28,80 × 1,21 = 34,848, afgerond 34,85 euro. Merk op dat de btw geen deel van de "
                "marge is: de winkel houdt er niets van over.",
                "Hier gaat de rekening de andere kant op: (19,99 − 12) gedeeld door 12 = 0,666, "
                "dus ongeveer 66,6 procent. Deel altijd door de aankoopprijs, want dat is waarop "
                "de marge gerekend wordt.",
                "Dat dit werkt, is nagegaan in onderzoek, en het is ook de reden waarom bijna "
                "geen enkele prijs op een rond getal eindigt. Let wel: bij dure of luxueuze "
                "producten doet men het net niet, want 19,99 doet goedkoop aan.",
            ],
        ),
        dict(
            aanpak="Houd twee soorten onderzoek uit elkaar: deskresearch gebruikt cijfers die al "
                   "bestaan, fieldresearch maakt nieuwe. Daarnaast drie stappen die op elkaar "
                   "volgen: segmenteren, een doelgroep kiezen, en je positioneren.",
            waarom=[
                None,
                "Noem in je antwoord alle drie de problemen, want het zijn drie verschillende "
                "fouten. De steekproef is vertekend, de antwoorden zijn sociaal gewenst, en "
                "zeggen is nog niet doen. Dat laatste is het hardnekkigst: ook een eerlijke ja "
                "wordt vaak geen aankoop.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-soorten-klanten-en-het-verkoopgesprek-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De zes fasen volgen een vaste logica: eerst contact, dan luisteren, dan pas "
                   "voorstellen. Wie fase drie voor fase twee zet, verkoopt op gok. Onthoud dat "
                   "de bezwaren een eigen fase zijn en geen ongeluk: ze horen bij elk gesprek.",
            waarom=[
                None,
                "Dit is de kern van het hele hoofdstuk. Een verkoop die niet past, komt terug, "
                "en dan heb je de omzet verloren én de klant. Luisteren is dus geen hoffelijkheid "
                "maar het goedkoopste deel van het werk.",
            ],
        ),
        dict(
            aanpak="Een open vraag kan niet met ja of nee beantwoord worden en begint vaak met "
                   "wat, hoe of waarvoor. Een gesloten vraag kan dat wel. Lees dus naar het "
                   "eerste woord van de vraag en niet naar de lengte.",
            waarom=[
                None,
                "Een gesprek gaat dus van open naar gesloten: open om te weten te komen, "
                "gesloten om af te sluiten. Wie het omgekeerd doet, hoort enkel ja en nee en "
                "weet aan het einde nog niets.",
            ],
        ),
        dict(
            aanpak="Bij elk bezwaar is de werkwijze dezelfde drie stappen: erkennen, een vraag "
                   "stellen om te weten wat er echt achter zit, en dan pas antwoorden. Nooit "
                   "tegenspreken en nooit het bezwaar klein maken.",
            waarom=[
                "Te duur betekent bijna nooit ik heb het geld niet, maar ik zie de waarde niet. "
                "Daarom vraag je eerst waarmee de klant vergelijkt: zonder dat antwoord weet je "
                "niet wat je naast de prijs moet zetten.",
                "Dit bezwaar is vaak een hoffelijke nee. Door te vragen wat er nog ontbreekt, "
                "krijg je het echte bezwaar te horen, en dat kan je wel beantwoorden.",
                "Let op dat je in dit antwoord nooit de concurrent afbreekt. Je vraagt naar het "
                "precieze model, want vaak vergelijkt de klant twee verschillende dingen, en dat "
                "mag hij zelf vaststellen.",
                "Dat de klant zijn gezicht zou moeten verliezen, is hier de echte reden. Het "
                "gaat dus niet om hoffelijkheid maar om de uitkomst: wie gelijk haalt in de "
                "discussie, verliest de verkoop.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-commerciele-documenten-en-de-documentenstroom-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De documenten volgen de handel in twee reeksen: eerst alles rond de "
                   "bestelling en de levering, dan alles rond het geld. Twee paren verwar je het "
                   "makkelijkst: de offerte komt van de verkoper en de bestelbon van de klant; de "
                   "verzendnota rijdt mee en de leveringsbon wordt afgetekend.",
            waarom=[
                None,
                "Houd creditnota en debetnota uit elkaar met de richting: een creditnota haalt "
                "iets van de factuur af, een debetnota rekent iets bij. De creditnota komt het "
                "vaakst voor, bij een retour of een te hoog aangerekend bedrag.",
            ],
        ),
        dict(
            aanpak="Zes uitspraken over de wettelijke vermeldingen. Twee regels helpen: elk stuk "
                   "moet terug te vinden en te dateren zijn, dus nummer en datum zijn nooit "
                   "optioneel; en een particulier is geen onderneming, dus voor hem gelden andere "
                   "regels.",
            waarom=[
                "Het opeenvolgende nummer is er niet voor de orde maar voor de controle: aan een "
                "ontbrekend nummer ziet de fiscus dat er een factuur weg is.",
                None,
                "Niet waar. De datum beslist in welk btw-tijdvak de factuur valt en wanneer de "
                "betaaltermijn begint te lopen. Een vervaldag zonder factuurdatum is dus "
                "onbruikbaar.",
                None,
                "Niet waar. Bij een verkoop aan een particulier volstaat een kasticket; een "
                "factuur moet enkel in bepaalde gevallen, bijvoorbeeld bij een wagen of bij "
                "werken aan een woning. De klant kan er wel altijd om vragen.",
                "Waar, en dat is vandaag de gewoonte. Voorwaarde is dat de factuur leesbaar en "
                "ongewijzigd bewaard blijft gedurende de hele bewaartermijn.",
            ],
        ),
        dict(
            aanpak="Reken een factuur van boven naar beneden en schrijf elk tussenbedrag op. De "
                   "orde is vast: brutobedrag, handelskorting, contantkorting, dan de "
                   "verzendkosten erbij, en dat is de maatstaf van heffing. De btw komt daar "
                   "helemaal op het einde bij.",
            waarom=[
                "20 × 45 = 900 euro.",
                "10 % van 900 = 90 euro.",
                "900 − 90 = 810 euro. Dit is het bedrag waarop de contantkorting gerekend wordt, "
                "en niet de 900.",
                "2 % van 810 = 16,20 euro. Reken de twee kortingen dus na elkaar; samen 12 "
                "procent van 900 zou 108 euro geven en dat is te veel.",
                "810 − 16,20 = 793,80; plus 25 euro verzendkosten = 818,80 euro. De "
                "verzendkosten zitten in de maatstaf omdat ze aan dezelfde btw onderworpen zijn.",
                "21 % van 818,80 = 171,948, afgerond 171,95 euro.",
                "818,80 + 171,95 = 990,75 euro. Toets je uitkomst: ze ligt onder de 900 euro aan "
                "goederen plus btw, want de kortingen wogen zwaarder dan de verzendkosten.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-transport-expeditie-en-logistiek-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Elke vervoerswijze heeft één sterkte: het vliegtuig snelheid, het schip "
                   "prijs per volume, de vrachtwagen bereik tot aan de deur. Houd bij de "
                   "documenten de twee namen uit elkaar: CMR hoort bij de weg, het cognossement "
                   "bij de zee. En expediteur is niet hetzelfde als vervoerder.",
            waarom=[
                None,
                "Het verschil tussen de expediteur en de vervoerder is het belangrijkste van "
                "deze rij. De expediteur organiseert en heeft zelf geen vrachtwagens; hij zoekt "
                "de weg, de papieren en de douane uit. Daarom staat hij ook op andere documenten.",
            ],
        ),
        dict(
            aanpak="Reken altijd met de maten en de eenheden die in de vraag staan, en schrijf "
                   "elke tussenstap op. Bij een kost per pallet deel je de ritprijs door het "
                   "aantal pallets; bij een gewicht vermenigvuldig je. Let op de stand van de "
                   "pallet, want daarvan hangt af hoeveel er naast elkaar passen.",
            waarom=[
                "2,40 gedeeld door 1,20 = 2 pallets. Zet je ze gedraaid, met de korte zijde "
                "dwars, dan passen er 2,40 / 0,80 = 3 naast elkaar, maar dan nemen ze meer "
                "lengte in. Daarom beslist de stand hoeveel er in de wagen gaan.",
                "33 × 420 = 13 860 kg. Toets of dat kan: een vrachtwagen mag in België tot 44 ton "
                "totaal, met ongeveer 25 ton lading, dus dit past ruim.",
                "1,35 × 480 = 648 euro.",
                "648 gedeeld door 33 = 19,636, afgerond 19,64 euro per pallet. Dat soort cijfer "
                "is wat een vervoerder echt gebruikt: niet de ritprijs maar de prijs per pallet "
                "of per kilo.",
                "Reken het mee: rijdt hij leeg terug, dan kost elke pallet het dubbele, want "
                "dezelfde 648 euro moet dan over één richting gedragen worden. Daarom zoeken "
                "expediteurs retourladingen.",
            ],
        ),
        dict(
            aanpak="Het bestelpunt reken je met één formule: het verbruik tijdens de levertijd "
                   "plus de veiligheidsvoorraad. Let erop dat het verbruik en de levertijd in "
                   "dezelfde eenheid staan, hier allebei in weken.",
            waarom=[
                "Let op fifo. Het is niet alleen een ordeningsregel maar ook een "
                "houdbaarheidskwestie: wie het nieuwste vooraan zet, vindt achteraan vervallen "
                "voorraad terug.",
                "40 × 2 = 80 stuks tijdens de levertijd, plus 30 veiligheidsvoorraad = 110 "
                "stuks. Zonder die veiligheidsvoorraad kom je precies op nul uit op de dag van "
                "de levering, en dan is één dag vertraging al een probleem.",
                "Just in time is dus een afweging tussen geld en risico. Dat is geen theorie: "
                "tijdens de pandemie en bij de blokkade van het Suezkanaal lagen fabrieken "
                "wereldwijd stil omdat er bewust geen voorraad was.",
            ],
        ),
    ],
)

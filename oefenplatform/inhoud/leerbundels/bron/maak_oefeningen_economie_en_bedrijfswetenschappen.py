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

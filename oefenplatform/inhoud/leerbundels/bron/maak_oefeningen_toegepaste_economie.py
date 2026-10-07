# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij toegepaste economie 🚀 Boost dubbele finaliteit.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde stof
met andere opgaven, dus gaat dezelfde pdf bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die op het scherm: andere
bedragen, andere documenten en opdrachten die je enkel op papier kan maken —
een balans aanvullen, een boeking uitschrijven, een scherm natekenen. Wie hier
iets bijschrijft, legt het eerst naast
`../../boost-dubbele-finaliteit/toegepaste-economie.json` en naast
`maak_toegepaste_economie.py`.

Elk bedrag in dit bestand is nagerekend. Wie een getal verandert, rekent het
antwoord opnieuw uit en zet het ook op het antwoordblad goed.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost-dubbele-finaliteit".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import oefenbundel

VAK = "Toegepaste economie"
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
zet("waarom-boekhouden-en-hoe-het-werkt",
    titel="Waarom boekhouden en hoe het werkt",
    reeksen=[
        dict(kop="Waarom boekhouden?",
             opdracht="Schrijf bij elke reden op wie er belang bij heeft.",
             oefeningen=[
                 ("rij", [("weten of de zaak winst maakt", "de ondernemer"),
                          ("de belastingaangifte kunnen invullen", "de fiscus"),
                          ("weten of de onderneming haar lening kan afbetalen", "de bank"),
                          ("zien of de werkgelegenheid veilig is", "de werknemers"),
                          ("beslissen of men nog levert op factuur", "de leveranciers"),
                          ("beslissen of men geld in de zaak steekt", "de aandeelhouders")],
                  "Wie heeft hier belang bij?", WW),
                 ("open", "Noem de twee grote doelen van een boekhouding.",
                  "Een intern doel: de ondernemer informatie geven om te sturen. En een extern "
                  "doel: verantwoording afleggen aan de fiscus, de bank en andere "
                  "belanghebbenden.", 3),
             ]),
        dict(kop="Begrippen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("alles wat de onderneming bezit", "de activa"),
                          ("alles waarmee ze dat betaalt", "de passiva"),
                          ("het bewijsstuk van een verrichting", "het verantwoordingsstuk"),
                          ("het boek waarin alles chronologisch komt", "het dagboek / journaal"),
                          ("het boek waarin alles per rekening komt", "het grootboek"),
                          ("de lijst van alle rekeningen met hun saldo", "de proefbalans")],
                  "Hoe noemen we dit?", WW),
                 ("open", "Waarom moet elke boeking op een bewijsstuk steunen?",
                  "Zonder bewijsstuk kan niemand nagaan of de boeking klopt. De fiscus en de "
                  "boekhoudwet eisen dat elke verrichting bewijsbaar is.", 3),
                 ("waar", "Een kasticket van tien euro is ook een verantwoordingsstuk.", True),
             ]),
        dict(kop="Het dubbel boekhouden",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Leg uit wat men bedoelt met dubbel boekhouden.",
                  "Elke verrichting wordt twee keer geboekt: één keer op de debetzijde en één "
                  "keer op de creditzijde, voor hetzelfde bedrag. Zo blijft het geheel altijd in "
                  "evenwicht.", 4),
                 ("open", "Een klant betaalt een factuur van 1 210 euro op de bankrekening. "
                          "Welke twee rekeningen bewegen, en in welke richting?",
                  "De bankrekening stijgt met 1 210 euro aan de debetzijde, en de vordering op "
                  "de klant daalt met 1 210 euro aan de creditzijde.", 4),
                 ("open", "Waarom blijft de balans in evenwicht, wat je ook boekt?",
                  "Omdat elke boeking even veel debet als credit boekt. Een verrichting "
                  "verschuift dus alleen iets binnen de balans of laat beide zijden even veel "
                  "groeien of krimpen.", 4),
             ]),
    ])


# ============================================================
zet("de-balans-en-de-resultatenrekening",
    titel="De balans en de resultatenrekening",
    reeksen=[
        dict(kop="Links of rechts op de balans?",
             opdracht="Schrijf activa of passiva op.",
             oefeningen=[
                 ("rij", [("een bestelwagen", "activa"), ("een banklening op 5 jaar", "passiva"),
                          ("de voorraad handelsgoederen", "activa"),
                          ("het kapitaal", "passiva"),
                          ("een openstaande factuur van een klant", "activa"),
                          ("een nog te betalen factuur van een leverancier", "passiva")],
                  "Activa of passiva?", WW),
                 ("open", "Leg uit waarom de activa altijd gelijk zijn aan de passiva.",
                  "De activa tonen wat er is, de passiva waarmee het betaald is. Elke euro "
                  "bezit heeft een herkomst, dus de twee zijden zijn per definitie even "
                  "groot.", 3),
             ]),
        dict(kop="Een balans aanvullen",
             opdracht="Vul de ontbrekende bedragen in.",
             oefeningen=[
                 ("tabel", ["activa", "bedrag", "passiva", "bedrag"],
                  [["gebouw", "150 000", "kapitaal", "120 000"],
                   ["bestelwagen", "25 000", "lening op 5 jaar", None],
                   ["voorraad", "18 000", "leveranciers", "14 000"],
                   ["klanten", "12 000", "", ""],
                   ["bank", "9 000", "", ""],
                   ["totaal", None, "totaal", None]],
                  "totaal activa 214 000 · lening 80 000 · totaal passiva 214 000", "90px"),
                 ("open", "Toon hoe je de ontbrekende lening berekent.",
                  "Totaal activa = 150 000 + 25 000 + 18 000 + 12 000 + 9 000 = 214 000. "
                  "De gekende passiva zijn 120 000 + 14 000 = 134 000. De lening is dus "
                  "214 000 − 134 000 = 80 000 euro.", 4),
             ]),
        dict(kop="Kosten en opbrengsten",
             opdracht="Schrijf kost of opbrengst op.",
             oefeningen=[
                 ("rij", [("de aankoop van handelsgoederen", "kost"),
                          ("de verkoop van handelsgoederen", "opbrengst"),
                          ("de huur van het magazijn", "kost"),
                          ("de lonen", "kost"),
                          ("ontvangen intresten op een spaarrekening", "opbrengst"),
                          ("de elektriciteitsfactuur", "kost")],
                  "Kost of opbrengst?", WW),
                 ("open", "Een onderneming had in één jaar 480 000 euro opbrengsten en "
                          "415 000 euro kosten. Hoe groot is het resultaat, en waar komt het "
                          "op de balans terecht?",
                  "480 000 − 415 000 = 65 000 euro winst. De winst komt op de passiefzijde van "
                  "de balans, bij het eigen vermogen.", 4),
                 ("open", "Waarom staat de winst aan de passiefzijde en niet aan de "
                          "actiefzijde?",
                  "De passiva tonen waar het geld vandaan komt. Winst is geld dat de "
                  "onderneming zelf voortbracht en dat aan de eigenaars toekomt, dus het hoort "
                  "bij het eigen vermogen.", 4),
             ]),
    ])


# ============================================================
zet("het-mar-en-het-redeneerschema",
    titel="Het MAR en het redeneerschema",
    reeksen=[
        dict(kop="De klassen van het MAR",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("klasse 1", "eigen vermogen, voorzieningen en schulden op lange "
                           "termijn"),
                          ("klasse 2", "oprichtingskosten, vaste activa"),
                          ("klasse 3", "voorraden en bestellingen in uitvoering"),
                          ("klasse 4", "vorderingen en schulden op ten hoogste één jaar"),
                          ("klasse 5", "geldbeleggingen en liquide middelen"),
                          ("klasse 6 en 7", "kosten en opbrengsten")],
                  "Wat staat er in deze klasse?", WL),
                 ("rij", [("400 Handelsdebiteuren", "klasse 4"),
                          ("440 Leveranciers", "klasse 4"),
                          ("550 Kredietinstellingen", "klasse 5"),
                          ("604 Aankopen handelsgoederen", "klasse 6"),
                          ("700 Verkopen", "klasse 7"),
                          ("100 Kapitaal", "klasse 1")],
                  "In welke klasse hoort deze rekening?", W),
             ]),
        dict(kop="Het redeneerschema",
             opdracht="Beantwoord de vier vragen van het schema voor elke verrichting.",
             oefeningen=[
                 ("open", "De onderneming koopt handelsgoederen voor 2 000 euro, op krediet.",
                  "Welke rekeningen? 604 Aankopen handelsgoederen en 440 Leveranciers. "
                  "Soort? een kostenrekening en een schuldenrekening. Stijgt of daalt? beide "
                  "stijgen. Debet of credit? 604 debet 2 000, 440 credit 2 000.", 5),
                 ("open", "Een klant betaalt 1 500 euro op de bankrekening.",
                  "Rekeningen 550 Kredietinstellingen en 400 Handelsdebiteuren. 550 is een "
                  "actiefrekening die stijgt, dus debet 1 500; 400 is een actiefrekening die "
                  "daalt, dus credit 1 500.", 5),
                 ("open", "De onderneming betaalt 900 euro huur via de bank.",
                  "Rekeningen 610 Huur (kost, stijgt, debet 900) en 550 Kredietinstellingen "
                  "(actief, daalt, credit 900).", 4),
             ]),
        dict(kop="Debet of credit?",
             opdracht="Vul de regel aan.",
             oefeningen=[
                 ("tabel", ["soort rekening", "stijgt aan", "daalt aan"],
                  [["actief", None, None], ["passief", None, None],
                   ["kosten", None, None], ["opbrengsten", None, None]],
                  "actief: debet / credit · passief: credit / debet · "
                  "kosten: debet / credit · opbrengsten: credit / debet", "90px"),
                 ("open", "Waarom staan kosten aan dezelfde kant als de activa?",
                  "Een kost verbruikt middelen van de onderneming; ze gedraagt zich dus als een "
                  "toename aan de debetzijde, net als een actief.", 3),
             ]),
    ])


# ============================================================
zet("aankopen-documenten-kortingen-en-btw",
    titel="Aankopen: documenten, kortingen en btw",
    reeksen=[
        dict(kop="De documentenstroom",
             opdracht="Zet de documenten in de juiste volgorde, 1 tot 6.",
             oefeningen=[
                 ("rij", [("de prijsaanvraag", "1"), ("de offerte", "2"),
                          ("de bestelbon", "3"), ("de leveringsbon", "4"),
                          ("de factuur", "5"), ("de betaling", "6")],
                  "Welk nummer?", "60px"),
                 ("open", "Wat is het verschil tussen een leveringsbon en een factuur?",
                  "De leveringsbon toont wat er geleverd is en gaat mee met de goederen; de "
                  "factuur is de vraag tot betaling en vermeldt de bedragen en de btw.", 3),
             ]),
        dict(kop="Kortingen berekenen",
             opdracht="Reken uit. Rond af op twee decimalen.",
             oefeningen=[
                 ("open", "Brutoprijs 1 200 euro, handelskorting 10 %, daarna 2 % korting "
                          "contant. Wat is het bedrag waarop de btw berekend wordt?",
                  "1 200 − 120 = 1 080; daarvan 2 % is 21,60; 1 080 − 21,60 = 1 058,40 euro.",
                  4),
                 ("open", "Reken op dat bedrag 21 % btw. Wat is het te betalen bedrag?",
                  "Btw 21 % van 1 058,40 = 222,26. Totaal 1 058,40 + 222,26 = 1 280,66 euro.",
                  4),
                 ("rij", [("500 euro met 6 % btw", "530,00"),
                          ("800 euro met 21 % btw", "968,00"),
                          ("1 000 euro met 12 % btw", "1 120,00"),
                          ("brutoprijs 400, korting 25 %", "300,00"),
                          ("netto 242 inclusief 21 % btw, bedrag excl. btw", "200,00"),
                          ("netto 318 inclusief 6 % btw, bedrag excl. btw", "300,00")],
                  "Wat is het bedrag?", WW),
                 ("open", "Toon hoe je van 242 euro inclusief 21 % btw terugrekent naar het "
                          "bedrag zonder btw.",
                  "Je deelt door 1,21: 242 / 1,21 = 200 euro. De btw is dan 42 euro.", 3),
             ]),
        dict(kop="Een factuur nakijken",
             opdracht="Lees en antwoord.",
             oefeningen=[
                 ("tekst",
                  "<table class='invul'><tr><th>omschrijving</th><th>aantal</th>"
                  "<th>eenheidsprijs</th><th>bedrag</th></tr>"
                  "<tr><td>fietshelm</td><td>20</td><td>35,00</td><td>700,00</td></tr>"
                  "<tr><td>fietsslot</td><td>30</td><td>18,00</td><td>540,00</td></tr>"
                  "<tr><td colspan='3'>handelskorting 10 %</td><td>124,00</td></tr>"
                  "<tr><td colspan='3'>maatstaf van heffing</td><td>?</td></tr>"
                  "<tr><td colspan='3'>btw 21 %</td><td>?</td></tr>"
                  "<tr><td colspan='3'>te betalen</td><td>?</td></tr></table>"),
                 ("kort", "Wat is het totaal voor korting?", "1 240,00 euro", W),
                 ("open", "Is de handelskorting juist berekend? Toon je berekening.",
                  "10 % van 1 240 is 124. Dat klopt.", 2),
                 ("kort", "Wat is de maatstaf van heffing?", "1 116,00 euro", W),
                 ("kort", "Hoeveel bedraagt de btw?", "234,36 euro", W),
                 ("kort", "Wat is het te betalen bedrag?", "1 350,36 euro", W),
                 ("open", "Noem drie vermeldingen die wettelijk op elke factuur moeten staan.",
                  "De datum en het volgnummer, de naam, het adres en het btw-nummer van beide "
                  "partijen, en de maatstaf van heffing met het btw-tarief en het btw-bedrag.",
                  4),
             ]),
    ])


# ============================================================
zet("verkopen-en-de-verkoopfactuur",
    titel="Verkopen en de verkoopfactuur",
    reeksen=[
        dict(kop="De verkoopkant",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de rekening waarop de verkoop komt", "700 Verkopen"),
                          ("de rekening van de klant die nog moet betalen",
                           "400 Handelsdebiteuren"),
                          ("de btw die je aan de klant aanrekent", "451 Verschuldigde btw"),
                          ("het document als de klant goederen terugstuurt", "een creditnota"),
                          ("het document dat de levering begeleidt", "de leveringsbon"),
                          ("de korting die je geeft bij snelle betaling", "korting contant")],
                  "Hoe noemen we dit?", WL),
                 ("open", "Waarom is de verschuldigde btw geen opbrengst voor de "
                          "onderneming?",
                  "Je int ze alleen voor de staat en moet ze doorstorten. Ze is dus een schuld, "
                  "geen winst.", 3),
             ]),
        dict(kop="Een verkoopfactuur opmaken",
             opdracht="Vul aan. Btw-tarief 21 %.",
             oefeningen=[
                 ("tabel", ["omschrijving", "aantal", "prijs", "bedrag"],
                  [["bureaustoel", "8", "145,00", None],
                   ["bureaulamp", "12", "39,50", None],
                   ["handelskorting 5 %", "", "", None],
                   ["maatstaf van heffing", "", "", None],
                   ["btw 21 %", "", "", None],
                   ["te betalen", "", "", None]],
                  "stoelen 1 160,00 · lampen 474,00 · korting 81,70 · maatstaf 1 552,30 · "
                  "btw 325,98 · te betalen 1 878,28", "100px"),
                 ("open", "De klant stuurt twee stoelen terug. Hoeveel bedraagt de creditnota, "
                          "inclusief btw, als de korting van 5 % mee verrekend wordt?",
                  "Twee stoelen is 290,00; min 5 % is 275,50; btw 21 % is 57,86; samen "
                  "333,36 euro.", 4),
             ]),
        dict(kop="Boeken",
             opdracht="Schrijf de boeking op: rekening, debet of credit, en het bedrag.",
             oefeningen=[
                 ("open", "Verkoopfactuur van 1 000 euro plus 210 euro btw.",
                  "400 Handelsdebiteuren debet 1 210; 700 Verkopen credit 1 000; "
                  "451 Verschuldigde btw credit 210.", 4),
                 ("open", "De klant betaalt die factuur via de bank.",
                  "550 Kredietinstellingen debet 1 210; 400 Handelsdebiteuren credit 1 210.", 3),
                 ("open", "Creditnota van 100 euro plus 21 euro btw voor teruggestuurde "
                          "goederen.",
                  "700 Verkopen debet 100; 451 Verschuldigde btw debet 21; "
                  "400 Handelsdebiteuren credit 121.", 4),
             ]),
    ])


# ============================================================
zet("de-btw-en-de-btw-aangifte",
    titel="De btw en de btw-aangifte",
    reeksen=[
        dict(kop="De tarieven",
             opdracht="Schrijf het tarief op: 0, 6, 12 of 21 procent.",
             oefeningen=[
                 ("rij", [("brood en melk", "6 %"), ("een fiets", "21 %"),
                          ("een boek", "6 %"), ("sociale woningbouw", "12 %"),
                          ("een krant (dagblad)", "0 %"), ("een gsm", "21 %")],
                  "Welk tarief?", W),
                 ("open", "Waarom hanteert de overheid verlaagde tarieven?",
                  "Om basisbehoeften zoals voeding, boeken en wonen betaalbaar te houden; de "
                  "btw treft anders de lage inkomens het zwaarst.", 3),
             ]),
        dict(kop="Btw berekenen",
             opdracht="Reken uit.",
             oefeningen=[
                 ("rij", [("btw op 2 400 euro aan 21 %", "504,00"),
                          ("btw op 950 euro aan 6 %", "57,00"),
                          ("bedrag incl. btw van 2 400 aan 21 %", "2 904,00"),
                          ("uit 605 euro incl. 21 %: btw", "105,00"),
                          ("uit 605 euro incl. 21 %: excl. btw", "500,00"),
                          ("uit 1 060 euro incl. 6 %: btw", "60,00")],
                  "Wat is het bedrag?", WW),
                 ("open", "Leg uit hoe je uit een bedrag inclusief 21 % btw het btw-bedrag "
                          "haalt.",
                  "Je deelt het bedrag door 1,21 om het bedrag zonder btw te krijgen, en trekt "
                  "dat af van het totaal. Of korter: bedrag × 21 / 121.", 3),
             ]),
        dict(kop="De aangifte",
             opdracht="Werk de aangifte van één kwartaal uit.",
             oefeningen=[
                 ("tekst",
                  "<p><em>In het tweede kwartaal verkocht een onderneming voor 84 000 euro "
                  "(alles aan 21 %) en kocht ze voor 52 000 euro aan goederen en diensten "
                  "(ook alles aan 21 %).</em></p>"),
                 ("kort", "Hoeveel verschuldigde btw op de verkopen?", "17 640,00 euro", W),
                 ("kort", "Hoeveel aftrekbare btw op de aankopen?", "10 920,00 euro", W),
                 ("kort", "Hoeveel moet de onderneming doorstorten?", "6 720,00 euro", W),
                 ("open", "Wat gebeurt er als de aftrekbare btw groter is dan de "
                          "verschuldigde?",
                  "Dan heeft de onderneming een tegoed: ze krijgt het verschil terug of mag het "
                  "overdragen naar het volgende tijdvak.", 3),
                 ("open", "Waarom drukt de btw uiteindelijk op de eindconsument en niet op de "
                          "onderneming?",
                  "Een onderneming trekt de btw die ze betaalt af van de btw die ze int. Alleen "
                  "de laatste schakel, de consument, kan niets aftrekken en draagt dus de hele "
                  "belasting.", 4),
                 ("waar", "Een onderneming moet haar btw-aangifte altijd per maand indienen.",
                  False),
             ]),
    ])


# ============================================================
zet("aankopen-verkopen-en-bankverrichtingen-boeken",
    titel="Aankopen, verkopen en bankverrichtingen boeken",
    reeksen=[
        dict(kop="Welke rekening?",
             opdracht="Vul het rekeningnummer en de naam in.",
             oefeningen=[
                 ("rij", [("aankoop handelsgoederen", "604 Aankopen handelsgoederen"),
                          ("schuld aan de leverancier", "440 Leveranciers"),
                          ("aftrekbare btw", "411 Terug te vorderen btw"),
                          ("verkoop", "700 Verkopen"),
                          ("vordering op de klant", "400 Handelsdebiteuren"),
                          ("de bankrekening", "550 Kredietinstellingen")],
                  "Welke rekening?", WL),
             ]),
        dict(kop="Boekingen uitschrijven",
             opdracht="Schrijf per verrichting de rekeningen op met debet, credit en bedrag.",
             oefeningen=[
                 ("open", "Aankoopfactuur: 3 000 euro goederen plus 630 euro btw.",
                  "604 debet 3 000; 411 debet 630; 440 credit 3 630.", 3),
                 ("open", "Verkoopfactuur: 5 000 euro plus 1 050 euro btw.",
                  "400 debet 6 050; 700 credit 5 000; 451 credit 1 050.", 3),
                 ("open", "Betaling aan de leverancier van 3 630 euro via de bank.",
                  "440 debet 3 630; 550 credit 3 630.", 3),
                 ("open", "Ontvangst van een klant van 6 050 euro op de bank.",
                  "550 debet 6 050; 400 credit 6 050.", 3),
                 ("open", "De bank houdt 45 euro kosten in.",
                  "656 Bankkosten debet 45; 550 Kredietinstellingen credit 45.", 3),
                 ("open", "De onderneming betaalt 1 800 euro lonen via de bank.",
                  "620 Bezoldigingen debet 1 800; 550 Kredietinstellingen credit 1 800.", 3),
             ]),
        dict(kop="Een rekeninguittreksel verwerken",
             opdracht="Lees en antwoord.",
             oefeningen=[
                 ("tekst",
                  "<table class='invul'><tr><th>datum</th><th>omschrijving</th>"
                  "<th>debet</th><th>credit</th></tr>"
                  "<tr><td>03/05</td><td>beginsaldo</td><td></td><td>8 400,00</td></tr>"
                  "<tr><td>05/05</td><td>betaling klant Peeters</td><td></td>"
                  "<td>2 420,00</td></tr>"
                  "<tr><td>09/05</td><td>betaling leverancier Dupont</td><td>1 815,00</td>"
                  "<td></td></tr>"
                  "<tr><td>15/05</td><td>bankkosten</td><td>18,50</td><td></td></tr>"
                  "<tr><td>28/05</td><td>huur magazijn</td><td>950,00</td><td></td></tr>"
                  "</table>"),
                 ("kort", "Wat is het eindsaldo?", "8 036,50 euro", WW),
                 ("open", "Welke twee verrichtingen raken een kostenrekening?",
                  "De bankkosten en de huur van het magazijn.", 2),
                 ("open", "Welke verrichting verandert alleen de samenstelling van de activa "
                          "en niet het totaal?",
                  "De betaling van klant Peeters: de vordering daalt en de bank stijgt met "
                  "hetzelfde bedrag.", 3),
             ]),
    ])


# ============================================================
zet("van-proefbalans-tot-eindbalans",
    titel="Van proefbalans tot eindbalans",
    reeksen=[
        dict(kop="De stappen",
             opdracht="Zet de stappen in volgorde, 1 tot 6.",
             oefeningen=[
                 ("rij", [("verrichtingen boeken in het dagboek", "1"),
                          ("overboeken naar het grootboek", "2"),
                          ("de proef- en saldibalans opmaken", "3"),
                          ("de eindejaarsverrichtingen boeken", "4"),
                          ("het resultaat bepalen", "5"),
                          ("de eindbalans opmaken", "6")],
                  "Welk nummer?", "60px"),
                 ("open", "Waarvoor dient een proefbalans?",
                  "Ze controleert of het totaal van alle debetbewegingen gelijk is aan dat van "
                  "alle creditbewegingen. Zo zie je of er een boeking scheef zit.", 3),
                 ("open", "Een proefbalans die in evenwicht is, bewijst nog niet dat de "
                          "boekhouding juist is. Waarom niet?",
                  "Een boeking op de verkeerde rekening, of een bedrag dat tweemaal verkeerd "
                  "maar even groot geboekt werd, houdt het evenwicht in stand.", 3),
             ]),
        dict(kop="Saldo's bepalen",
             opdracht="Bereken het saldo en zeg of het debet of credit is.",
             oefeningen=[
                 ("rij", [("550 Bank: debet 24 000, credit 19 500", "4 500 debet"),
                          ("400 Klanten: debet 31 000, credit 27 400", "3 600 debet"),
                          ("440 Leveranciers: debet 18 200, credit 22 900", "4 700 credit"),
                          ("700 Verkopen: debet 0, credit 96 000", "96 000 credit"),
                          ("604 Aankopen: debet 61 500, credit 1 200", "60 300 debet"),
                          ("100 Kapitaal: debet 0, credit 50 000", "50 000 credit")],
                  "Welk saldo?", WW),
             ]),
        dict(kop="Het resultaat en de eindbalans",
             opdracht="Werk uit.",
             oefeningen=[
                 ("tekst",
                  "<p><em>Op het einde van het jaar staan de kosten op 78 400 euro en de "
                  "opbrengsten op 96 000 euro. Het eigen vermogen voor verwerking van het "
                  "resultaat bedraagt 50 000 euro.</em></p>"),
                 ("kort", "Hoe groot is het resultaat?", "17 600 euro winst", WW),
                 ("kort", "Hoe groot is het eigen vermogen na verwerking?",
                  "67 600 euro", WW),
                 ("open", "Wat zou er met het eigen vermogen gebeuren bij een verlies van "
                          "9 000 euro?",
                  "Het daalt tot 41 000 euro: verlies vermindert het eigen vermogen.", 3),
                 ("open", "Noem twee eindejaarsverrichtingen die nog geboekt moeten worden "
                          "voor de eindbalans klopt.",
                  "De afschrijvingen op de vaste activa, en de aanpassing van de voorraad aan "
                  "de werkelijke eindvoorraad.", 3),
             ]),
    ])


# ============================================================
zet("tekstverwerking-klavier-opmaak-en-stijlen",
    titel="Tekstverwerking: klavier, opmaak en stijlen",
    reeksen=[
        dict(kop="Sneltoetsen",
             opdracht="Schrijf de sneltoets op.",
             oefeningen=[
                 ("rij", [("kopiëren", "ctrl + c"), ("plakken", "ctrl + v"),
                          ("knippen", "ctrl + x"), ("ongedaan maken", "ctrl + z"),
                          ("alles selecteren", "ctrl + a"), ("bewaren", "ctrl + s")],
                  "Welke sneltoets?", W),
                 ("rij", [("zoeken", "ctrl + f"), ("vet", "ctrl + b"),
                          ("cursief", "ctrl + i"), ("onderstrepen", "ctrl + u"),
                          ("een nieuwe pagina beginnen", "ctrl + enter"),
                          ("afdrukken", "ctrl + p")],
                  "Welke sneltoets?", W),
             ]),
        dict(kop="Teken- of alineaopmaak?",
             opdracht="Schrijf teken of alinea op.",
             oefeningen=[
                 ("rij", [("vet", "teken"), ("regelafstand", "alinea"),
                          ("lettergrootte", "teken"), ("uitlijnen", "alinea"),
                          ("inspringen", "alinea"), ("tekstkleur", "teken")],
                  "Teken- of alineaopmaak?", WW),
                 ("open", "Waarom hoef je bij alineaopmaak de tekst niet te selecteren?",
                  "Je cursor staat al in de alinea, en alineaopmaak werkt op de hele alinea "
                  "tegelijk.", 2),
             ]),
        dict(kop="Stijlen",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Noem twee voordelen van werken met stijlen in plaats van met "
                          "handmatige opmaak.",
                  "Je past één stijl aan en het hele document volgt, en je kan automatisch een "
                  "inhoudstafel laten opbouwen uit de kopstijlen.", 3),
                 ("open", "Je wil dat elk hoofdstuk op een nieuwe bladzijde begint. Waarom is "
                          "een pagina-einde beter dan tien keer op enter duwen?",
                  "Enters schuiven mee zodra je tekst toevoegt of weghaalt; een pagina-einde "
                  "blijft op zijn plaats.", 3),
                 ("rij", [("de ruimte tussen de tekst en de rand", "de marge"),
                          ("een tekst die bovenaan elke bladzijde terugkeert", "de koptekst"),
                          ("de automatische nummering van de bladzijden", "paginanummering"),
                          ("staand of liggend", "de afdrukstand"),
                          ("A4 of A5", "het papierformaat"),
                          ("een lijst met opsommingstekens", "een opsomming")],
                  "Hoe noemen we dit?", WW),
                 ("open", "Je krijgt een document van een collega waarin elke titel met de "
                          "hand vet en groot gemaakt is. Wat doe je om er een inhoudstafel in "
                          "te kunnen zetten?",
                  "Je geeft elke titel de stijl Kop 1 of Kop 2, en voegt daarna een "
                  "automatische inhoudstafel in die uit die kopstijlen opgebouwd wordt.", 4),
             ]),
    ])


# ============================================================
zet("illustraties-schema-s-en-tabellen",
    titel="Illustraties, schema's en tabellen",
    reeksen=[
        dict(kop="Een tabel bewerken",
             opdracht="Schrijf op wat je doet.",
             oefeningen=[
                 ("rij", [("een rij erbij onderaan", "in de laatste cel op tab duwen"),
                          ("twee cellen tot één maken", "cellen samenvoegen"),
                          ("één cel in twee delen", "cellen splitsen"),
                          ("de kolom breder maken", "de scheidingslijn verslepen"),
                          ("de tekst in een cel centreren", "uitlijnen in de cel"),
                          ("een kader rond elke cel", "randen instellen")],
                  "Wat doe je?", WL),
                 ("open", "Een tabel loopt over twee bladzijden. Hoe zorg je dat de kopregel "
                          "bovenaan de tweede bladzijde herhaald wordt?",
                  "Je selecteert de kopregel en zet de eigenschap aan die zegt dat ze als "
                  "kopregel op elke pagina herhaald moet worden.", 3),
             ]),
        dict(kop="Afbeeldingen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de tekst loopt rond de afbeelding", "tekstterugloop"),
                          ("de verhouding tussen breedte en hoogte", "de beeldverhouding"),
                          ("een afbeelding bijknippen", "bijsnijden"),
                          ("de opmaak waarin de afbeelding op een vaste plaats blijft",
                           "verankeren / vaste positie"),
                          ("het bestandstype met doorzichtige achtergrond", "png"),
                          ("het bestandstype voor foto's", "jpg")],
                  "Hoe noemen we dit?", WW),
                 ("open", "Waarom mag je een afbeelding niet met de zijgreep uitrekken?",
                  "Dan klopt de beeldverhouding niet meer en wordt alles uitgerekt. Sleep aan "
                  "een hoekgreep, dan blijft de verhouding bewaard.", 3),
                 ("open", "Je voegt een foto van 4 MB in en het document wordt traag. Wat kan "
                          "je doen?",
                  "De afbeeldingen comprimeren tot een resolutie die voor afdrukken of voor het "
                  "scherm volstaat.", 2),
             ]),
        dict(kop="Een schema opbouwen",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Je moet de structuur van een bedrijf tonen met de directeur "
                          "bovenaan en drie afdelingen eronder. Welk soort schema kies je?",
                  "Een organogram, dus een hiërarchisch schema met één blok bovenaan en drie "
                  "blokken op de laag eronder, verbonden door lijnen.", 3),
                 ("teken", "Teken dat organogram.",
                  "Eén blok bovenaan met daaronder drie blokken, elk met een lijn naar het "
                  "bovenste blok.", 55),
                 ("open", "Wat is het verschil tussen een stroomschema en een organogram?",
                  "Een organogram toont wie onder wie staat; een stroomschema toont de volgorde "
                  "van stappen in een proces, met beslissingen onderweg.", 3),
             ]),
    ])


# ============================================================
zet("het-rekenblad-cellen-bereiken-en-opmaak",
    titel="Het rekenblad: cellen, bereiken en opmaak",
    reeksen=[
        dict(kop="De structuur",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("het vakje waarin je typt", "de cel"),
                          ("de naam van dat vakje", "het celadres"),
                          ("een groep cellen samen", "een bereik"),
                          ("het blad waarop je werkt", "het werkblad"),
                          ("het bestand met alle bladen samen", "de werkmap"),
                          ("de notatie van A1 tot C5", "A1:C5")],
                  "Hoe noemen we dit?", WW),
                 ("rij", [("hoeveel cellen in A1:A10", "10"),
                          ("hoeveel cellen in B2:D5", "12"),
                          ("hoeveel cellen in A1:C3", "9"),
                          ("hoeveel rijen in B2:D5", "4"),
                          ("hoeveel kolommen in B2:D5", "3"),
                          ("het adres rechtsonder in A1:E8", "E8")],
                  "Wat is het antwoord?", W),
             ]),
        dict(kop="Getalnotatie",
             opdracht="Schrijf op welke notatie je kiest.",
             oefeningen=[
                 ("rij", [("1 250 euro met twee decimalen", "valuta, 2 decimalen"),
                          ("0,25 tonen als 25 %", "percentage, 0 decimalen"),
                          ("14 maart 2027", "datum"),
                          ("09:30", "tijd"),
                          ("een artikelnummer met voorloopnullen", "tekst"),
                          ("een groot getal met een spatie per duizendtal",
                           "getal met scheidingsteken")],
                  "Welke notatie?", WL),
                 ("open", "Je typt 007 in een cel en er verschijnt 7. Hoe los je dat op?",
                  "Je zet de notatie van de cel op tekst, of je typt een apostrof voor het "
                  "getal.", 2),
                 ("open", "Een cel toont ##### in plaats van een getal. Wat is er aan de hand?",
                  "De kolom is te smal voor het getal. Maak de kolom breder.", 2),
             ]),
        dict(kop="Opmaak en vulgreep",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Wat doet de vulgreep als je in A1 het getal 1 en in A2 het getal 2 "
                          "zet, beide selecteert en naar beneden sleept?",
                  "Hij herkent de reeks en vult 3, 4, 5 en verder aan.", 2),
                 ("open", "Wat is voorwaardelijke opmaak? Geef een voorbeeld uit een "
                          "puntenlijst.",
                  "Opmaak die alleen verschijnt als de inhoud aan een voorwaarde voldoet, "
                  "bijvoorbeeld elke score onder 50 rood kleuren.", 3),
                 ("open", "Je wil de titel over vier kolommen laten lopen en centreren. Hoe "
                          "doe je dat?",
                  "Je selecteert de vier cellen en gebruikt samenvoegen en centreren.", 2),
             ]),
    ])


# ============================================================
zet("formules-en-functies-in-een-rekenblad",
    titel="Formules en functies in een rekenblad",
    reeksen=[
        dict(kop="Formules schrijven",
             opdracht="Schrijf de formule op, met het gelijkteken vooraan.",
             oefeningen=[
                 ("rij", [("B2 keer C2", "=B2*C2"),
                          ("de som van A1 tot A20", "=SOM(A1:A20)"),
                          ("het gemiddelde van B2 tot B11", "=GEMIDDELDE(B2:B11)"),
                          ("de hoogste waarde in C1:C30", "=MAX(C1:C30)"),
                          ("de laagste waarde in C1:C30", "=MIN(C1:C30)"),
                          ("A1 plus B1, maal 2", "=(A1+B1)*2")],
                  "Welke formule?", WW),
                 ("open", "Waarom staat er in =(A1+B1)*2 een haakje?",
                  "Zonder haakjes wordt eerst B1 maal 2 gerekend, want vermenigvuldigen gaat "
                  "voor optellen. De haakjes dwingen de optelling eerst af.", 3),
             ]),
        dict(kop="Absolute en relatieve adressering",
             opdracht="Vul aan.",
             oefeningen=[
                 ("open", "In B2 staat =A2*$D$1. Je kopieert die formule naar B3. Wat staat "
                          "er dan?",
                  "=A3*$D$1: A2 schuift mee naar A3, maar $D$1 blijft staan.", 3),
                 ("open", "Wanneer gebruik je een absolute verwijzing?",
                  "Als je in elke rij naar dezelfde cel wil verwijzen, bijvoorbeeld naar één "
                  "btw-tarief of één wisselkoers.", 3),
                 ("rij", [("A1 wordt gekopieerd naar beneden", "A2, A3, ..."),
                          ("$A$1 wordt gekopieerd", "blijft $A$1"),
                          ("A$1 wordt naar beneden gekopieerd", "blijft A$1"),
                          ("$A1 wordt naar rechts gekopieerd", "blijft $A1"),
                          ("de toets om het dollarteken te zetten", "F4"),
                          ("de formule =B2*$E$1 in C2, gekopieerd naar C5", "=B5*$E$1")],
                  "Wat is het resultaat?", WW),
             ]),
        dict(kop="ALS en VERT.ZOEKEN",
             opdracht="Schrijf de formule op of leg uit.",
             oefeningen=[
                 ("open", "In B2 staat een score. Schrijf een formule die geslaagd of niet "
                          "geslaagd toont, met 50 als grens.",
                  "=ALS(B2>=50;\"geslaagd\";\"niet geslaagd\")", 2),
                 ("open", "In C2 staat een bedrag. Schrijf een formule die 10 % korting geeft "
                          "vanaf 500 euro en anders niets.",
                  "=ALS(C2>=500;C2*0,1;0)", 2),
                 ("open", "Wat doet VERT.ZOEKEN, in je eigen woorden?",
                  "Het zoekt een waarde in de eerste kolom van een tabel en geeft de waarde "
                  "terug die in dezelfde rij in een andere kolom staat.", 3),
                 ("open", "Je hebt een prijslijst in A2:C50 met het artikelnummer in kolom A "
                          "en de prijs in kolom C. Schrijf de formule die de prijs opzoekt "
                          "van het nummer in F2.",
                  "=VERT.ZOEKEN(F2;$A$2:$C$50;3;ONWAAR)", 3),
                 ("open", "Waarom zet je het laatste argument op ONWAAR?",
                  "Dan zoekt hij exact; met WAAR zoekt hij bij benadering en dat geeft bij "
                  "artikelnummers een verkeerd resultaat.", 3),
             ]),
    ])


# ============================================================
zet("grafieken-maken-en-lezen",
    titel="Grafieken maken en lezen",
    reeksen=[
        dict(kop="Welke grafiek?",
             opdracht="Schrijf op welk soort grafiek hier het best past.",
             oefeningen=[
                 ("rij", [("de omzet van januari tot december", "lijngrafiek"),
                          ("de omzet per filiaal, vijf filialen", "staafgrafiek"),
                          ("het aandeel van elke kostenpost in het totaal", "cirkelgrafiek"),
                          ("het verband tussen prijs en aantal verkochte stuks",
                           "spreidingsdiagram"),
                          ("de verkoop per maand voor drie jaren naast elkaar",
                           "gegroepeerde staafgrafiek"),
                          ("de opbouw van de totale omzet per kwartaal",
                           "gestapelde staafgrafiek")],
                  "Welk soort grafiek?", WL),
                 ("open", "Waarom is een cirkelgrafiek met twaalf stukjes bijna altijd een "
                          "slechte keuze?",
                  "De stukjes worden te klein om te vergelijken. Met meer dan vijf of zes "
                  "delen leest een staafgrafiek veel beter.", 3),
             ]),
        dict(kop="Een grafiek afwerken",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de tekst boven de grafiek", "de titel"),
                          ("de tekst langs de assen", "de asbenaming"),
                          ("het kadertje dat de kleuren uitlegt", "de legende"),
                          ("de getallen bij de staven", "de gegevenslabels"),
                          ("de horizontale as", "de x-as"),
                          ("de verticale as", "de y-as")],
                  "Hoe noemen we dit?", WW),
                 ("open", "Waarom zet je bij een grafiek met één reeks geen legende?",
                  "Een legende met één item voegt niets toe; de titel zegt al wat er staat.",
                  2),
                 ("open", "Wanneer zet je de waarden boven de staven?",
                  "Als het exacte getal telt, of als één staaf er zo ver boven uitsteekt dat "
                  "je de andere niet meer kan vergelijken.", 3),
             ]),
        dict(kop="Een grafiek die misleidt",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Een staafgrafiek begint op de y-as niet bij 0 maar bij 95. Wat is "
                          "het gevolg?",
                  "Kleine verschillen lijken enorm. Een staafgrafiek hoort bij 0 te beginnen.",
                  3),
                 ("open", "Mag een lijngrafiek wel bij een ander getal dan 0 beginnen?",
                  "Ja, want een lijn toont het verloop en niet de omvang. Zet er dan duidelijk "
                  "bij waar de as begint.", 3),
                 ("open", "Een cirkelgrafiek telt op tot 108 %. Wat is er fout?",
                  "De delen zijn niet uit één geheel genomen, of iemand is dubbel geteld. Een "
                  "cirkelgrafiek kan alleen delen van hetzelfde geheel tonen.", 3),
             ]),
    ])


# ============================================================
zet("afdrukken-kopieren-en-scannen",
    titel="Afdrukken, kopiëren en scannen",
    reeksen=[
        dict(kop="Afdrukken instellen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("staand of liggend papier", "de afdrukstand"),
                          ("op beide zijden van het blad", "dubbelzijdig afdrukken"),
                          ("de ruimte rond de tekst", "de marge"),
                          ("eerst zien hoe het eruit komt", "het afdrukvoorbeeld"),
                          ("twee bladzijden op één blad", "2 pagina's per vel"),
                          ("de bladzijden in de juiste volgorde per exemplaar",
                           "sorteren")],
                  "Hoe noemen we dit?", WL),
                 ("open", "Je rekenblad komt op zeven bladen uit, met één kolom alleen op het "
                          "laatste. Wat stel je in?",
                  "Je zet het afdrukbereik aan op één bladzijde breed, of je kiest de "
                  "liggende afdrukstand en kleinere marges.", 3),
                 ("open", "Waarom druk je bij een lange tabel de kop op elke bladzijde af?",
                  "Anders weet de lezer vanaf blad twee niet meer wat er in welke kolom "
                  "staat.", 2),
             ]),
        dict(kop="Kopiëren en scannen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("van papier naar papier", "kopiëren"),
                          ("van papier naar een bestand", "scannen"),
                          ("van een bestand naar papier", "afdrukken"),
                          ("de scherpte van een scan", "de resolutie, in dpi"),
                          ("de maat die 300 dpi oplevert voor tekst", "goed leesbaar"),
                          ("de bestandssoort voor een gescande factuur", "pdf")],
                  "Wat is het antwoord?", WL),
                 ("open", "Waarom is 1200 dpi voor een gescande brief overdreven?",
                  "Het bestand wordt heel groot zonder dat de tekst beter leesbaar wordt. "
                  "Voor tekst is 300 dpi genoeg.", 3),
                 ("open", "Wat is tekstherkenning bij een scan en waarom is dat nuttig?",
                  "De scanner zet het beeld van de letters om in echte tekst, zodat je in het "
                  "bestand kan zoeken en de tekst kan kopiëren.", 3),
             ]),
        dict(kop="In één keer juist",
             opdracht="Waar of niet waar?",
             oefeningen=[
                 ("waar", "Een afdrukvoorbeeld bekijken kost minder dan een herdruk.", True),
                 ("waar", "Een pdf ziet er op elke computer hetzelfde uit.", True),
                 ("waar", "Een scan in kleur van een zwart-witte brief is even groot als een "
                          "scan in grijswaarden.", False),
                 ("waar", "Dubbelzijdig afdrukken halveert het aantal bladen.", True),
                 ("waar", "Wie een kopie maakt van een volledig handboek mag dat gewoon, want "
                          "het is voor de les.", False),
                 ("waar", "Bij een kopieermachine op het werk hoort een code of een badge, "
                          "zodat de kosten per dienst geteld worden.", True),
             ]),
    ])


# ============================================================
zet("bestanden-beheren-en-bewaren",
    titel="Bestanden beheren en bewaren",
    reeksen=[
        dict(kop="Mappen en namen",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("de volledige weg naar een bestand", "het pad"),
                          ("de drie letters na de punt", "de extensie"),
                          ("een map in een map", "een submap"),
                          ("een verwijzing naar een bestand elders", "een snelkoppeling"),
                          ("de map waar verwijderde bestanden landen", "de prullenbak"),
                          ("wat je terugvindt met de zoekfunctie",
                           "bestanden op naam of inhoud")],
                  "Hoe noemen we dit?", WL),
                 ("rij", [(".docx", "tekstdocument"),
                          (".xlsx", "rekenblad"),
                          (".pdf", "vast opgemaakt document"),
                          (".csv", "tabel als platte tekst"),
                          (".jpg", "foto"),
                          (".zip", "samengeperste map")],
                  "Wat voor bestand is dit?", WL),
                 ("open", "Waarom is factuur.docx een slechte bestandsnaam in een map met "
                          "driehonderd facturen?",
                  "Je kan ze niet van elkaar onderscheiden en niet sorteren. Beter is "
                  "2027-03-14-factuur-0142-vandenberghe.docx.", 3),
                 ("open", "Waarom zet je een datum als 2027-03-14 en niet als 14-03-2027 in "
                          "een bestandsnaam?",
                  "Met het jaar vooraan staan de bestanden bij sorteren op naam meteen in de "
                  "juiste tijdsorde.", 3),
             ]),
        dict(kop="Bewaren en back-up",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Wat is het verschil tussen opslaan en opslaan als?",
                  "Opslaan schrijft over het bestaande bestand; opslaan als maakt een nieuw "
                  "bestand met een andere naam of op een andere plaats.", 3),
                 ("open", "Leg de regel van drie kopieën uit.",
                  "Je houdt drie kopieën van je gegevens, op twee verschillende dragers, "
                  "waarvan één op een andere plaats.", 3),
                 ("open", "Waarom is een back-up op dezelfde computer geen echte back-up?",
                  "Bij brand, diefstal of een kapotte schijf verlies je het origineel en de "
                  "kopie samen.", 3),
                 ("open", "Een map staat in de cloud en wordt gesynchroniseerd. Je verwijdert "
                          "er per ongeluk een bestand uit. Wat gebeurt er?",
                  "Het verdwijnt ook op de andere toestellen. Je haalt het terug uit de "
                  "prullenbak of de versiegeschiedenis van de clouddienst.", 3),
             ]),
        dict(kop="Veilig werken",
             opdracht="Waar of niet waar?",
             oefeningen=[
                 ("waar", "Een bestand met persoonsgegevens mag je op een onbeveiligde "
                          "usb-stick meenemen.", False),
                 ("waar", "Een wachtwoord op een zipbestand is een vorm van beveiliging.",
                  True),
                 ("waar", "Wie een bestand in de prullenbak zet, heeft het definitief gewist.",
                  False),
                 ("waar", "Boekhoudstukken moeten in België zeven jaar bewaard worden.", True),
                 ("waar", "Een gedeelde map op het werk hoeft geen afspraken over namen, want "
                          "de zoekfunctie vindt alles.", False),
                 ("waar", "Een versienummer in de naam, zoals -v3, voorkomt dat je aan het "
                          "verkeerde bestand werkt.", True),
             ]),
    ])


# ============================================================
zet("presenteren-en-gegevens-in-een-databank",
    titel="Presenteren en gegevens in een databank",
    reeksen=[
        dict(kop="Een presentatie opbouwen",
             opdracht="Antwoord kort.",
             oefeningen=[
                 ("rij", [("het blad waarop je iets zet", "de dia"),
                          ("de vaste opmaak van alle dia's", "het dia-model of thema"),
                          ("de tekst die enkel jij ziet", "de notities"),
                          ("de overgang van de ene dia naar de andere", "de overgang"),
                          ("beweging binnen één dia", "de animatie"),
                          ("de weergave waarmee je voor de klas staat",
                           "de presentatieweergave")],
                  "Hoe noemen we dit?", WL),
                 ("open", "Waarom zet je niet je volledige tekst op de dia?",
                  "Het publiek leest dan mee en luistert niet meer. Op de dia staan "
                  "steekwoorden, de uitleg komt van jou.", 3),
                 ("open", "Geef twee redenen waarom lichtgrijze tekst op wit een slechte keuze "
                          "is op een beamer.",
                  "Het contrast is te laag en een beamer verliest nog contrast door het licht "
                  "in de zaal, zodat de achterste rijen niets lezen.", 3),
             ]),
        dict(kop="Een databank",
             opdracht="Vul aan.",
             oefeningen=[
                 ("rij", [("één rij met alle gegevens van één klant", "een record"),
                          ("één kolom, bijvoorbeeld de postcode", "een veld"),
                          ("de verzameling records samen", "een tabel"),
                          ("het veld dat elke rij uniek maakt", "de primaire sleutel"),
                          ("een vraag aan de databank", "een query"),
                          ("het scherm om een record in te vullen", "een formulier")],
                  "Hoe noemen we dit?", WL),
                 ("rij", [("een klantnummer", "geheel getal of tekst"),
                          ("een naam", "tekst"),
                          ("een geboortedatum", "datum"),
                          ("een prijs", "valuta of decimaal getal"),
                          ("al betaald of niet", "ja/nee"),
                          ("een opmerking van vijf regels", "lange tekst of memo")],
                  "Welk veldtype?", WL),
                 ("open", "Waarom is een naam geen goede primaire sleutel?",
                  "Twee klanten kunnen dezelfde naam hebben, en een naam kan veranderen. Een "
                  "sleutel moet uniek zijn en blijven.", 3),
             ]),
        dict(kop="Van rekenblad naar databank",
             opdracht="Antwoord in enkele zinnen.",
             oefeningen=[
                 ("open", "Wanneer kies je een databank in plaats van een rekenblad?",
                  "Als er veel records zijn, als meerdere mensen tegelijk werken, en als de "
                  "gegevens in verschillende tabellen horen die naar elkaar verwijzen.", 3),
                 ("open", "Wat is het nadeel van de volledige adresgegevens van de klant in "
                          "elke verkooplijn te herhalen?",
                  "Je typt alles meerdere keren en bij een verhuis moet je het op tien "
                  "plaatsen aanpassen, dus je gegevens gaan uit elkaar lopen.", 3),
                 ("open", "Hoe los je dat op met twee tabellen?",
                  "Een tabel klanten met het klantnummer als sleutel, en een tabel verkopen "
                  "die alleen dat klantnummer bijhoudt.", 3),
                 ("open", "Je wil alle klanten uit Hasselt die vorig jaar iets kochten. Hoe "
                          "pak je dat aan?",
                  "Met een query over de twee tabellen, met de gemeente en het jaartal als "
                  "voorwaarde.", 3),
             ]),
    ])

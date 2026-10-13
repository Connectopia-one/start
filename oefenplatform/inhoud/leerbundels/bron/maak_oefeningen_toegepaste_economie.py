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


# ============================================================
# De uitlegbladen: één los blad per oefenbundel, met dezelfde nummers.
# Per reeks een aanpak, en per oefening een waarom waar het antwoord op zich
# niet genoeg zegt. Een None laat het blad die oefening overslaan.
# ============================================================

UITLEGBLADEN = {}

UITLEGBLADEN["oefenbundel-waarom-boekhouden-en-hoe-het-werkt-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vraag je bij elke reden af wie de informatie nodig heeft om een beslissing "
                   "te nemen. Dat is telkens iemand anders, en daarom moet een boekhouding meer "
                   "dan één publiek dienen. Zoek dus niet wie er iets mee te maken heeft, maar "
                   "wie er iets mee beslist.",
            waarom=[
                "De leveranciers en de bank lijken op elkaar, maar hun beslissing is niet "
                "dezelfde. De bank vraagt zich af of je een lening over jaren kan afbetalen, de "
                "leverancier of je de factuur binnen dertig dagen betaalt.",
                "Let op dat het twee verschillende doelen zijn en niet twee keer hetzelfde. "
                "Intern mag een cijfer een vermoeden zijn waarmee je stuurt; extern moet het "
                "volgens vaste regels opgemaakt zijn, want anderen rekenen erop.",
            ],
        ),
        dict(
            aanpak="Zes woorden die je door elkaar kan halen. Houd de drie boeken uit elkaar met "
                   "hun ordening: het dagboek staat op datum, het grootboek per rekening, de "
                   "proefbalans is enkel de eindstand van elke rekening. Het is dus drie keer "
                   "dezelfde informatie, anders geordend.",
            waarom=[
                "Activa en passiva zijn geen bezit en schuld. De passiva bevatten ook het "
                "kapitaal, en dat is geen schuld aan een vreemde maar aan de eigenaars. Daarom "
                "zegt men beter: alles wat ze bezit en waarmee ze dat betaald heeft.",
                "Dat er bewezen moet kunnen worden, is niet alleen een eis van de fiscus. Zonder "
                "stuk kan je ook zelf achteraf niet meer nagaan wat er precies gebeurd is.",
                "Waar, en dat is belangrijker dan het lijkt. Een bewijsstuk hoeft geen factuur "
                "te zijn: een kasticket, een bankuittreksel of een creditnota doet hetzelfde "
                "werk. Het bedrag beslist niet of iets een bewijsstuk is.",
            ],
        ),
        dict(
            aanpak="Dubbel boekhouden betekent niet dat je twee keer hetzelfde schrijft, maar dat "
                   "je elke verrichting van twee kanten bekijkt: waar komt het geld terecht en "
                   "waar komt het van. Voor elke oefening: zoek eerst welke twee rekeningen "
                   "bewegen, dan in welke richting, en pas daarna debet of credit.",
            waarom=[
                None,
                "Hier wordt de onderneming niet rijker. Ze had al een vordering van 1 210 euro, "
                "en die wordt nu geld. Er verschuift dus alleen iets binnen de activa, en het "
                "balanstotaal blijft hetzelfde.",
                "Je kan het ook omgekeerd zeggen: de balans is niet in evenwicht omdat ze goed "
                "ingevuld is, maar omdat ze niet anders kan. Loopt ze niet gelijk, dan is er "
                "ergens maar één kant van een boeking opgeschreven.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-balans-en-de-resultatenrekening-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Eén vraag beslist alles: is dit iets wat de onderneming heeft, of iets "
                   "waarmee ze het betaald heeft? Het eerste staat links bij de activa, het "
                   "tweede rechts bij de passiva. Let op de twee facturen in deze rij: een "
                   "factuur die een klant nog moet betalen is bezit, een factuur die jij nog "
                   "moet betalen is herkomst.",
            waarom=[
                "Die twee facturen zijn het klassieke struikelpunt. Hetzelfde woord factuur "
                "staat één keer links en één keer rechts; wat beslist, is wie wie nog moet "
                "betalen.",
                "Let erop dat dit geen regel is die men ooit zo afgesproken heeft. Het evenwicht "
                "is een gevolg van wat de twee zijden betekenen, en daarom kan je er altijd een "
                "ontbrekend bedrag mee berekenen.",
            ],
        ),
        dict(
            aanpak="Een ontbrekend bedrag op een balans bereken je altijd op dezelfde manier: "
                   "tel de zijde op die je volledig kent, en haal daar de gekende posten van de "
                   "andere zijde van af. Werk met een vaste orde, van boven naar beneden, zodat "
                   "je geen post vergeet.",
            waarom=[
                None,
                "Reken mee: de activa tellen op tot 214 000. De gekende passiva zijn 134 000, "
                "dus blijft er 80 000 over voor de lening. Het totaal van de passiva is dus "
                "geen uitkomst die je berekent maar iets wat je van de activa overneemt.",
            ],
        ),
        dict(
            aanpak="Een kost gaat weg en komt niet terug, een opbrengst komt binnen. Pas op met "
                   "de aankoop van handelsgoederen: dat is een kost, ook al heb je er nog "
                   "voorraad voor in huis. En reken intresten die je ontvangt bij de "
                   "opbrengsten, ook als het maar een paar euro is.",
            waarom=[
                "De eerste twee lijnen staan er bewust naast elkaar: dezelfde goederen zijn een "
                "kost bij de aankoop en een opbrengst bij de verkoop. Het verschil tussen die "
                "twee is waar de onderneming van leeft.",
                "480 000 − 415 000 = 65 000 euro winst. Let op het tweede deel van de vraag, "
                "want daar gaat het echt om: de resultatenrekening vertelt hoe het jaar liep, "
                "en haar uitkomst belandt op de balans.",
                "Het helpt om het van de eigenaars uit te bekijken: de winst is geld dat in de "
                "zaak zit en dat aan hen toekomt. Dat is dus een herkomst, net als het kapitaal "
                "dat ze er zelf in staken.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-mar-en-het-redeneerschema-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Het MAR is geordend op looptijd en op soort, niet op belangrijkheid. De "
                   "klassen 1 tot 5 zijn de balans, de klassen 6 en 7 zijn de "
                   "resultatenrekening. Onthoud dat 4 over ten hoogste één jaar gaat en 1 over "
                   "meer dan één jaar; met dat ene onderscheid plaats je de meeste rekeningen al.",
            waarom=[
                "Merk op dat klasse 1 en klasse 4 beide schulden bevatten. Het enige verschil is "
                "de looptijd: een lening op vijf jaar staat in 1, een leverancier die je deze "
                "maand betaalt in 4.",
                "Het eerste cijfer van het rekeningnummer is de klasse. Dat is geen toeval maar "
                "de hele opzet van het MAR, en het is het snelste hulpmiddel dat je hebt: 604 "
                "begint met een 6, dus is het een kost.",
            ],
        ),
        dict(
            aanpak="Het redeneerschema werkt altijd in vier stappen, in deze orde: welke "
                   "rekeningen, welk soort, stijgt of daalt, en dan pas debet of credit. Sla de "
                   "derde stap nooit over, want debet of credit volgt uit het soort én de "
                   "richting samen, niet uit het soort alleen.",
            waarom=[
                "Let erop dat de goederen hier nog niet betaald zijn. De kost staat er wel al, "
                "want de onderneming heeft de goederen gekregen; de betaling is een tweede, "
                "latere verrichting.",
                "Hier dalen noch stijgen de activa in totaal. Een vordering wordt geld, dus 550 "
                "stijgt en 400 daalt met hetzelfde bedrag.",
                "Vergelijk deze met de vorige: ook hier verdwijnt er geld van de bank, maar nu "
                "komt er geen bezit in de plaats. Daarom staat er tegenover de daling van 550 "
                "een kost en geen actief.",
            ],
        ),
        dict(
            aanpak="Deze tabel is de kern van het hele vak. Hij staat in twee kolommen: welke "
                   "kant een toename neemt, en welke kant een afname. Activa en kosten nemen toe "
                   "aan de debetzijde, passiva en opbrengsten aan de creditzijde. Ken je dat "
                   "rijtje, dan hoef je nooit meer te raden.",
            waarom=[
                None,
                "Je kan het ook via de balans zien: een kost maakt het eigen vermogen kleiner, "
                "en het eigen vermogen staat aan de creditzijde. Kleiner worden aan de "
                "creditzijde is boeken aan de debetzijde, en daar staat de kost dus.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-aankopen-documenten-kortingen-en-btw-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De zes documenten volgen de twee vragen die een handel altijd stelt: eerst "
                   "wat kost het, dan geef mij dat. Vraag en aanbod vooraan, dan de bestelling, "
                   "dan de goederen, en pas achteraan het geld. Een document dat over geld gaat, "
                   "komt dus nooit voor de levering.",
            waarom=[
                None,
                "Het verschil is niet dat het ene document goederen vermeldt en het andere geld. "
                "Beide noemen de goederen; het verschil is dat de factuur een vraag tot betaling "
                "is, met de btw erop, en daarmee ook een stuk voor de fiscus.",
            ],
        ),
        dict(
            aanpak="Kortingen tellen altijd na elkaar, nooit samen opgeteld. Eerst de "
                   "handelskorting op de brutoprijs, dan de korting contant op wat er overblijft. "
                   "En onthoud de twee richtingen van de btw: erbij doe je met × 1,21, eruit "
                   "haal je met ÷ 1,21. Nooit 21 % van een bedrag dat de btw al bevat.",
            waarom=[
                "Let op de volgorde: 10 % en dan 2 % is niet hetzelfde als 12 % in één keer. "
                "Reken mee: 1 200 − 120 = 1 080, en 2 % daarvan is 21,60. Twaalf procent van "
                "1 200 zou 144 zijn, dus je zou 2,40 euro te veel aftrekken.",
                "Het bedrag na alle kortingen is de maatstaf van heffing: op dat bedrag en geen "
                "ander wordt de btw berekend. 21 % van 1 058,40 is 222,264, afgerond 222,26.",
                "Kijk naar de twee laatste lijnen: daar wordt teruggerekend. 242 / 1,21 = 200 en "
                "318 / 1,06 = 300. Wie daar 21 % of 6 % van het totaal neemt, komt bij 191,18 en "
                "298,92 uit, en dat is telkens te laag.",
                "Dat je met 21 / 121 in één stap tot de btw komt, is dezelfde rekening in het "
                "kort: het bedrag inclusief btw bestaat uit 121 delen, waarvan 21 belasting zijn.",
            ],
        ),
        dict(
            aanpak="Een factuur controleer je van boven naar beneden en je rekent elke lijn "
                   "zelf na: eerst de lijnen, dan het totaal, dan de korting, dan de maatstaf, "
                   "dan de btw, dan het te betalen bedrag. Elke lijn hangt aan de vorige, dus "
                   "een fout bovenaan loopt door tot onderaan.",
            waarom=[
                "20 × 35 = 700 en 30 × 18 = 540, samen 1 240 euro. Reken de lijnen zelf na en "
                "neem het bedrag niet over: een fout in een eenheidsprijs is het vaakst "
                "voorkomende probleem op een factuur.",
                None,
                "1 240 − 124 = 1 116. Dat is de maatstaf van heffing, dus het bedrag waarop de "
                "btw gerekend wordt, en niet het te betalen bedrag.",
                "21 % van 1 116 = 234,36 euro.",
                "1 116 + 234,36 = 1 350,36 euro. Toets je uitkomst: ze moet tussen de maatstaf en "
                "de maatstaf plus een vijfde liggen, anders heb je de btw op het verkeerde bedrag "
                "gerekend.",
                "Drie van de opgesomde vermeldingen volstaan. Het btw-nummer van beide partijen "
                "is daarbij het belangrijkste: zonder dat nummer kan de koper de btw niet "
                "aftrekken, en dan is de factuur voor hem veel geld waard.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-verkopen-en-de-verkoopfactuur-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De verkoopkant is de spiegel van de aankoopkant. Waar bij een aankoop 604 en "
                   "440 bewegen, bewegen bij een verkoop 700 en 400. Onthoud de nummers aan hun "
                   "klasse: 7 is een opbrengst, 4 is een vordering of een schuld op korte termijn.",
            waarom=[
                "Let op het verschil tussen een creditnota en een korting contant. Een creditnota "
                "haalt een verkoop gedeeltelijk terug, een korting contant verlaagt ze bij de "
                "betaling. Het eerste is een nieuw document, het tweede staat al op de factuur.",
                "Dit is het hele idee achter de btw. Je bent een doorgeefluik: je int geld dat "
                "nooit het jouwe was. Daarom staat 451 bij de schulden en niet bij de "
                "opbrengsten, en daarom mag je dat geld ook niet als winst beschouwen.",
            ],
        ),
        dict(
            aanpak="Een verkoopfactuur maak je in vaste orde: eerst de lijnen, dan de som, dan "
                   "de korting, dan de maatstaf van heffing, dan de btw, dan het totaal. Reken "
                   "elke lijn als aantal maal eenheidsprijs en pas de korting op de som toe, "
                   "niet per lijn.",
            waarom=[
                "Reken mee: 1 160 + 474 = 1 634; 5 % daarvan is 81,70; blijft 1 552,30 als "
                "maatstaf; 21 % daarvan is 325,98; samen 1 878,28 euro.",
                "Let op de drie stappen in deze vraag. Eerst de goederen terug, dan dezelfde "
                "korting als op de factuur, en pas dan de btw. 290 − 5 % = 275,50 en 21 % "
                "daarvan is 57,86. Vergeet je de korting, dan krijgt de klant 17,54 euro te veel "
                "terug.",
            ],
        ),
        dict(
            aanpak="Elke boeking in deze reeks heeft drie of twee rekeningen, en debet moet "
                   "altijd gelijk zijn aan credit. Werk zo: schrijf eerst de bedragen op, dan "
                   "de rekeningen, en tel daarna de twee kolommen na. Kloppen ze niet, dan is er "
                   "een rekening vergeten.",
            waarom=[
                "Merk op dat de klant 1 210 euro moet betalen terwijl de opbrengst maar 1 000 "
                "euro is. Die 210 euro is de btw en gaat naar de staat, niet naar de "
                "onderneming. Daarom staat de vordering hoger dan de verkoop.",
                None,
                "Deze boeking is de eerste in spiegelbeeld: wat bij de verkoop credit stond, "
                "staat nu debet. Dat is de vaste manier om iets terug te draaien, en het is ook "
                "een goede controle op je eerste boeking.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-de-btw-en-de-btw-aangifte-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Vier tarieven in België, en de regel erachter: hoe noodzakelijker, hoe lager. "
                   "Voeding, boeken en geneesmiddelen aan 6 procent, sociale woningbouw en "
                   "bepaalde werken aan 12, al de rest aan 21. Dagbladen zitten op 0 procent, "
                   "een uitzondering die je apart moet onthouden.",
            waarom=[
                "Een boek staat op 6 procent en een krant op 0, en dat lijkt vreemd. De "
                "gedachte erachter is de persvrijheid: een dagblad dat minstens achtenveertig "
                "keer per jaar verschijnt, is vrijgesteld. Een tijdschrift valt daar niet onder.",
                "Dit is het punt achter de verlaagde tarieven. Iedereen betaalt op brood "
                "hetzelfde percentage, maar wie weinig verdient, geeft een veel groter deel van "
                "zijn inkomen aan eten uit. Daarom weegt een vlakke belasting zwaarder op de "
                "lage inkomens.",
            ],
        ),
        dict(
            aanpak="Twee richtingen, en je moet altijd weten in welke je zit. Van een bedrag "
                   "zonder btw naar het totaal: × 1,21 of × 1,06. Van een totaal terug: ÷ 1,21 "
                   "of ÷ 1,06. Staat er inclusief in de opgave, dan deel je; staat er niets, "
                   "dan is het bedrag zonder btw.",
            waarom=[
                "Vergelijk de vierde lijn met de eerste. Uit 605 euro inclusief btw komt 105 euro "
                "btw, niet 127,05. Wie 21 % van 605 neemt, rekent de btw over de btw mee, en dat "
                "is de meest gemaakte fout van dit hoofdstuk.",
                "De korte weg × 21 / 121 geeft hetzelfde: van de 121 delen van een bedrag "
                "inclusief btw zijn er 21 belasting. Voor 6 procent wordt dat × 6 / 106.",
            ],
        ),
        dict(
            aanpak="Een aangifte is één aftrekking: de btw die je op je verkopen inde, min de "
                   "btw die je op je aankopen betaalde. Reken dus eerst de twee bedragen apart "
                   "uit en trek ze dan af. Let erop dat je de btw neemt en niet de omzet.",
            waarom=[
                "21 % van 84 000 = 17 640 euro. Dat is de btw die de onderneming van haar "
                "klanten kreeg, en dus voor de staat in handen heeft.",
                "21 % van 52 000 = 10 920 euro. Dat is btw die ze zelf betaalde en mag "
                "terugvragen.",
                "17 640 − 10 920 = 6 720 euro. Merk op dat dit 21 % is van de toegevoegde waarde "
                "van 32 000 euro: daar komt de naam belasting over de toegevoegde waarde van.",
                "Een tegoed is niets uitzonderlijks. Een onderneming die veel investeert of veel "
                "uitvoert, heeft het bijna elk kwartaal.",
                "Dit is het hele systeem in één antwoord. Elke schakel betaalt enkel over wat zij "
                "toevoegde; de keten schuift de belasting door tot bij wie niet meer kan "
                "aftrekken.",
                "Niet waar. Veel kleinere ondernemingen dienen per kwartaal in; per maand is "
                "verplicht vanaf een hoge omzet of in bijzondere gevallen. De casus hierboven "
                "ging ook over een kwartaal.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-aankopen-verkopen-en-bankverrichtingen-boeken-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zes rekeningen die in bijna elke boeking van dit hoofdstuk terugkomen. Let "
                   "op het paar 411 en 451: 411 is btw die je terugvraagt bij een aankoop, 451 "
                   "is btw die je moet doorstorten bij een verkoop. Het eerste is een vordering, "
                   "het tweede een schuld.",
            waarom=[
                "Houd de twee kanten uit elkaar met het rekeningnummer: bij een aankoop 604, 411 "
                "en 440, bij een verkoop 700, 451 en 400. Ken je die twee rijtjes van drie, dan "
                "heb je de helft van dit hoofdstuk al.",
            ],
        ),
        dict(
            aanpak="Elke boeking volgt hetzelfde patroon. Bij een factuur bewegen drie "
                   "rekeningen, want de btw hoort erbij. Bij een betaling bewegen er twee, want "
                   "de btw is al geboekt bij de factuur. Controleer altijd of debet en credit "
                   "even groot zijn.",
            waarom=[
                "Let op het bedrag van 440: dat is 3 630 euro en niet 3 000. De leverancier "
                "vraagt de btw mee, dus de schuld is het bedrag inclusief btw, terwijl de kost "
                "enkel 3 000 euro is.",
                None,
                "Hier staat geen btw bij, en dat is geen vergetelheid. De btw zat al in de "
                "factuur van hierboven; bij de betaling verdwijnt alleen de schuld.",
                None,
                "Bankkosten zijn een kost en gaan dus bij de klasse 6 horen. Merk op dat de bank "
                "het geld zelf afhoudt: je ziet zo'n verrichting enkel op het uittreksel en "
                "krijgt er geen factuur voor.",
                "De lonen staan hier vereenvoudigd als één bedrag. In werkelijkheid splitst een "
                "loonboeking in brutoloon, bedrijfsvoorheffing en sociale bijdragen, en dat komt "
                "in een later hoofdstuk.",
            ],
        ),
        dict(
            aanpak="Een rekeninguittreksel lees je van boven naar beneden: begin bij het "
                   "beginsaldo en tel elke lijn erbij of eraf. Let erop dat het uittreksel van "
                   "de bank gezien is: wat voor jou een inkomst is, staat er bij credit.",
            waarom=[
                "Reken mee: 8 400 + 2 420 = 10 820; − 1 815 = 9 005; − 18,50 = 8 986,50; − 950 = "
                "8 036,50 euro. Werk lijn per lijn met een tussensaldo, niet met twee grote "
                "sommen, want dan vind je bij een fout ook waar ze zit.",
                "De andere drie lijnen raken geen kost: het beginsaldo is geen verrichting, en "
                "de twee betalingen vereffenen enkel een vordering of een schuld die er al stond.",
                "Dit is de kern van het hoofdstuk. De onderneming wordt niet rijker als een klant "
                "betaalt: ze had dat geld al staan, alleen als vordering. Pas bij de verkoop "
                "zelf werd ze rijker.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-van-proefbalans-tot-eindbalans-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Zes stappen van een boekjaar, en de orde is logisch: eerst alles opschrijven, "
                   "dan ordenen, dan controleren, dan de eindejaarsverrichtingen, dan het "
                   "resultaat, dan de balans. Het resultaat komt pas op de vijfde plaats, want "
                   "zonder afschrijvingen en voorraad is het nog niet juist.",
            waarom=[
                None,
                "De proefbalans is enkel een rekenkundige controle. Ze telt bewegingen op, geen "
                "saldo's, en zegt dus alleen of elke boeking twee even grote kanten had.",
                "Dit is de belangrijkste nuance van het hoofdstuk. Een proefbalans vangt een "
                "half geboekte verrichting, maar niet een verkeerde rekening: huur die je op "
                "elektriciteit boekt, houdt het evenwicht perfect in stand en is toch fout.",
            ],
        ),
        dict(
            aanpak="Een saldo is het verschil tussen de debet- en de creditzijde van één "
                   "rekening, en het staat aan de kant die het grootste is. Reken dus eerst het "
                   "verschil en kijk dan welke kolom zwaarder was. Een actief- of kostenrekening "
                   "eindigt normaal debet, een passief- of opbrengstenrekening credit.",
            waarom=[
                "Toets elk saldo aan het soort rekening. 440 Leveranciers eindigt credit, en dat "
                "hoort: het is een schuld. Zou je daar een debetsaldo vinden, dan heb je meer "
                "betaald dan je moest of staat er een boeking scheef.",
            ],
        ),
        dict(
            aanpak="Het resultaat is opbrengsten min kosten, en het komt daarna bij het eigen "
                   "vermogen. Winst erbij, verlies eraf. Werk telkens in twee stappen en reken "
                   "het eigen vermogen pas uit als je het resultaat hebt.",
            waarom=[
                "96 000 − 78 400 = 17 600 euro winst. Let op de richting: opbrengsten min "
                "kosten, en niet omgekeerd.",
                "50 000 + 17 600 = 67 600 euro. Zo komt de resultatenrekening in de balans "
                "terecht: het hele jaar aan kosten en opbrengsten eindigt als één bedrag bij het "
                "eigen vermogen.",
                "Reken mee: 50 000 − 9 000 = 41 000 euro. Bij verlies gaat het eigen vermogen "
                "dus achteruit, en als dat jaar na jaar gebeurt, kan het negatief worden. Dan is "
                "de onderneming meer verschuldigd dan ze bezit.",
                "Twee van deze volstaan. Beide hebben hetzelfde doel: de cijfers laten kloppen "
                "met de werkelijkheid op de laatste dag van het jaar. Een bestelwagen is minder "
                "waard geworden, en de voorraad in het rek is zelden precies wat de boeken zeggen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-tekstverwerking-klavier-opmaak-en-stijlen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="De meeste sneltoetsen zijn de eerste letter van het Engelse woord: copy, "
                   "paste, find, bold, italic, underline, print, save. Alleen knippen en "
                   "ongedaan maken volgen dat niet; die liggen links onderaan op het klavier, "
                   "naast elkaar, zodat je ze met één hand haalt.",
            waarom=[
                None,
                "Let op ctrl + enter: dat is een pagina-einde en niet gewoon een nieuwe regel. "
                "Het is de toets die de derde reeks van deze bundel nodig heeft.",
            ],
        ),
        dict(
            aanpak="Eén vraag beslist: kan dit op één letter gelden? Vet, kleur en lettergrootte "
                   "kunnen dat, dus zijn het tekenopmaak. Regelafstand, uitlijnen en inspringen "
                   "gelden nooit op één letter maar op het hele blok, dus zijn het alineaopmaak.",
            waarom=[
                None,
                "Dat is ook de snelste manier om de twee uit elkaar te houden in de praktijk: "
                "lukt het zonder te selecteren, dan was het alineaopmaak.",
            ],
        ),
        dict(
            aanpak="De laatste reeks gaat over documenten die blijven kloppen als je ze "
                   "aanpast. De rode draad: laat het programma het werk doen in plaats van het "
                   "met de hand na te bootsen. Stijlen in plaats van vet, een pagina-einde in "
                   "plaats van enters, een automatische inhoudstafel in plaats van een getypte.",
            waarom=[
                "Er is nog een derde voordeel dat je mag noemen: een document met kopstijlen is "
                "voor een blinde lezer en voor een zoekprogramma leesbaar als structuur, en niet "
                "alleen als grote letters.",
                "Je ziet het verschil pas als je iets toevoegt. Een titel die met tien enters op "
                "zijn plaats staat, schuift met de eerste bijgevoegde alinea naar de verkeerde "
                "bladzijde.",
                None,
                "Merk op waarom dit werkt: een inhoudstafel leest geen opmaak maar stijlen. Vet "
                "en groot zeggen het programma niets; Kop 1 zegt dit is een titel van het eerste "
                "niveau.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-illustraties-schema-s-en-tabellen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een tabel bewerk je bijna altijd door eerst te selecteren wat je wil "
                   "veranderen: een cel, een rij of een kolom. Twee bewerkingen hebben een eigen "
                   "naam die je moet kennen: samenvoegen maakt van meerdere cellen één, splitsen "
                   "doet het omgekeerde.",
            waarom=[
                "De eerste is de nuttigste om te onthouden: tab in de laatste cel maakt een "
                "nieuwe rij. Zo kan je een tabel aanvullen zonder je handen van het klavier te "
                "halen.",
                "Dit is geen opmaak die je met de hand nabootst door de kopregel een tweede keer "
                "te typen. Zodra er een rij bij komt, schuift zo'n getypte kopregel mee naar het "
                "midden van de tabel.",
            ],
        ),
        dict(
            aanpak="Bij afbeeldingen gaat het telkens over de verhouding tot de tekst en over "
                   "het bestand zelf. Houd de twee bestandstypes uit elkaar met één kenmerk: png "
                   "kan doorzichtig zijn en is geschikt voor logo's en tekeningen, jpg kan dat "
                   "niet en is geschikt voor foto's.",
            waarom=[
                "Het verschil tussen verankeren en tekstterugloop is dat het ene over de plaats "
                "gaat en het andere over de tekst eromheen. Een afbeelding die ongewild door een "
                "document springt, heeft bijna altijd een probleem met de verankering.",
                "Dat alleen een hoekgreep de verhouding bewaart, is de ene regel die je hier "
                "echt moet onthouden. Een uitgerekt logo is meteen zichtbaar en staat slordig op "
                "een brief die naar een klant gaat.",
                "Comprimeren is niet hetzelfde als kleiner slepen op het blad. Een foto die je "
                "visueel klein maakt, blijft in het bestand even zwaar; comprimeren haalt de "
                "overtollige pixels er echt uit.",
            ],
        ),
        dict(
            aanpak="Kies je schema naar wat je wil tonen: een rangorde of een verloop. Een "
                   "organogram toont wie boven wie staat, een stroomschema toont wat na wat komt. "
                   "Teken altijd eerst de blokken en pas daarna de lijnen, zodat je ruimte goed "
                   "verdeeld is.",
            waarom=[
                None,
                "Let bij je tekening op de onderlinge afstand: de drie onderste blokken horen "
                "even groot te zijn en op dezelfde hoogte te staan, want ze staan ook in het "
                "bedrijf op hetzelfde niveau. Een schema dat dat niet toont, zegt iets anders dan "
                "je bedoelt.",
                "Je herkent het verschil aan de lijnen: in een organogram betekent een lijn geeft "
                "leiding aan, in een stroomschema betekent ze komt daarna. Hetzelfde plaatje met "
                "een andere betekenis van de pijlen is dus een ander schema.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-het-rekenblad-cellen-bereiken-en-opmaak-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een bereik tel je uit met kolommen maal rijen. Reken de kolommen in letters "
                   "en de rijen in cijfers apart uit, en vermenigvuldig dan. Let op: van rij 2 "
                   "tot rij 5 zijn het vier rijen en geen drie, want je telt de eerste mee.",
            waarom=[
                None,
                "B2:D5 is drie kolommen (B, C, D) maal vier rijen (2, 3, 4, 5) en dus twaalf "
                "cellen. Dat is de fout die iedereen één keer maakt: 5 − 2 = 3 geeft het aantal "
                "stappen, niet het aantal rijen.",
            ],
        ),
        dict(
            aanpak="De notatie verandert alleen hoe een getal eruitziet, niet wat er in de cel "
                   "staat. Daarom zijn er twee gevallen om goed te kennen: 0,25 als 25 procent "
                   "tonen is opmaak, maar een artikelnummer met voorloopnullen moet als tekst "
                   "opgeslagen worden, anders is de nul echt weg.",
            waarom=[
                "Merk op dat percentage een vermenigvuldiging met honderd laat zien. In de cel "
                "blijft 0,25 staan, en daarmee rekent het blad verder; wie 25 typt en percentage "
                "kiest, krijgt 2 500 procent.",
                "Dit is de reden waarom een artikelnummer of een rekeningnummer geen getal is. "
                "Je rekent er nooit mee, en de nullen vooraan horen erbij.",
                "Dat ##### geen fout in je formule is, is hier het punt: het getal is er wel, de "
                "kolom is enkel te smal. Dubbelklik op de scheidingslijn en de kolom past zich "
                "aan.",
            ],
        ),
        dict(
            aanpak="De laatste reeks gaat over werk dat het blad voor je doet. De vulgreep vult "
                   "reeksen aan, voorwaardelijke opmaak kleurt op voorwaarde, en samenvoegen en "
                   "centreren zet een titel over meerdere kolommen.",
            waarom=[
                "Let op dat je twee cellen moet selecteren. Sleep je alleen de 1 naar beneden, "
                "dan krijg je tien keer een 1: het blad kan uit één getal niet raden welke reeks "
                "je bedoelt.",
                "Voorwaardelijke opmaak is sterker dan met de hand kleuren omdat ze mee verandert "
                "met de cijfers. Verbeter je een score van 48 naar 55, dan verdwijnt het rood van "
                "zelf.",
                None,
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-formules-en-functies-in-een-rekenblad-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een formule begint altijd met een gelijkteken, en daarna verwijs je naar "
                   "cellen in plaats van naar getallen te typen. Dat is de hele winst van een "
                   "rekenblad: verandert de cel, dan verandert de uitkomst mee. Ken de vier "
                   "basisfuncties SOM, GEMIDDELDE, MAX en MIN met een bereik ertussen.",
            waarom=[
                "Merk op dat een functie met een bereik werkt en een gewone formule met losse "
                "cellen. =SOM(A1:A20) blijft juist als er een rij bij komt binnen dat bereik; "
                "=A1+A2+A3 moet je dan zelf aanvullen.",
                "Reken het na met getallen: staat er 2 in A1 en 3 in B1, dan geeft =(A1+B1)*2 "
                "tien en =A1+B1*2 acht. De rekenregels van de wiskunde gelden hier gewoon.",
            ],
        ),
        dict(
            aanpak="Een adres zonder dollarteken schuift mee als je de formule kopieert, een "
                   "adres met dollartekens blijft staan. Het dollarteken staat telkens voor wat "
                   "het vasthoudt: $D voor de kolom, $1 voor de rij. Vraag je dus bij elke "
                   "formule af wat mee moet schuiven en wat niet.",
            waarom=[
                "Reken mee wat er verschuift: je kopieert één rij naar beneden, dus A2 wordt A3. "
                "$D$1 heeft twee dollartekens en blijft volledig staan.",
                "Het btw-tarief in één cel zetten en er absoluut naar verwijzen is ook gewoon "
                "beter werk: verandert het tarief, dan pas je één cel aan in plaats van vijftig "
                "formules.",
                "Let op de derde en de vierde lijn, waar maar één helft vastgezet is. A$1 naar "
                "beneden kopiëren verandert niets, want enkel de rij staat vast en de kolom "
                "schuift niet mee naar beneden. Sleep je hem naar rechts, dan wordt het wel B$1.",
            ],
        ),
        dict(
            aanpak="ALS heeft drie delen, in deze orde: de voorwaarde, wat er moet gebeuren als "
                   "ze waar is, en wat er moet gebeuren als ze niet waar is. Tekst tussen "
                   "aanhalingstekens, getallen zonder. VERT.ZOEKEN heeft vier delen: wat je "
                   "zoekt, waar je zoekt, de hoeveelste kolom, en of het exact moet zijn.",
            waarom=[
                "Let op >= en niet >: met 50 als grens is precies 50 geslaagd. Dat is de fout "
                "die bij puntenlijsten het vaakst voorkomt, en ze treft net de leerling die het "
                "nodig heeft.",
                "Deze formule geeft het kortingsbedrag, niet de te betalen prijs. Wil je dat "
                "laatste, dan wordt het =ALS(C2>=500;C2*0,9;C2). Lees dus goed wat er gevraagd "
                "wordt.",
                None,
                "Let op de twee dollartekens rond het bereik. Kopieer je deze formule naar "
                "beneden zonder die, dan schuift de prijslijst mee en zoekt de laatste rij in "
                "een bereik dat al voorbij de tabel ligt. De 3 is de kolom binnen het bereik, "
                "dus kolom C.",
                "Benaderend zoeken werkt alleen als de eerste kolom gesorteerd is, en het geeft "
                "dan de dichtstbijzijnde lagere waarde. Bij een artikelnummer betekent dat de "
                "prijs van een ander artikel, zonder enige foutmelding.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-grafieken-maken-en-lezen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Kies je grafiek naar de vraag die je stelt. Een verloop in de tijd wordt een "
                   "lijn, een vergelijking tussen groepen een staaf, een aandeel in een geheel "
                   "een cirkel, en een verband tussen twee getallen een spreidingsdiagram. Zoek "
                   "in de opgave dus naar de woorden per maand, per filiaal, aandeel of verband.",
            waarom=[
                "Let op het verschil tussen de laatste twee. Gegroepeerd zet de staven naast "
                "elkaar, zodat je ze onderling kan vergelijken; gestapeld zet ze op elkaar, "
                "zodat je het totaal ziet. De vraag beslist: vergelijken of optellen.",
                "Dat maximum van vijf of zes is geen smaak maar iets wat je kan nagaan: een stuk "
                "van vijf procent is op een cirkel nauwelijks van een stuk van zeven te "
                "onderscheiden, terwijl twee staafjes dat verschil meteen tonen.",
            ],
        ),
        dict(
            aanpak="Een grafiek is pas afgewerkt als iemand ze kan lezen zonder jouw uitleg. "
                   "Dat betekent minstens een titel, de eenheden bij de assen, en een legende "
                   "zodra er meer dan één reeks is. Alles wat niets toevoegt, laat je weg.",
            waarom=[
                None,
                "Dit is de regel achter de hele reeks: een element dat geen informatie toevoegt, "
                "haalt informatie weg, want het publiek moet het eerst lezen om te zien dat het "
                "niets zegt.",
                "Let op het tweede geval, want dat is het nuttigste. Staat er één staaf van "
                "duizend naast vier van vijftig, dan zijn die vier onleesbaar klein; de getallen "
                "erbij zetten maakt de grafiek weer bruikbaar.",
            ],
        ),
        dict(
            aanpak="Een grafiek kan kloppen en toch een verkeerd beeld geven. Controleer altijd "
                   "drie dingen: begint de as bij nul, zijn de afstanden op de as gelijk, en telt "
                   "een cirkel op tot honderd procent. Op die drie punten gaat bijna elke "
                   "misleidende grafiek de mist in.",
            waarom=[
                "Reken het na met getallen: 96 en 100 lijken op een as vanaf 95 een verschil van "
                "een op vijf, terwijl het er in werkelijkheid een op vijfentwintig is. De "
                "oppervlakte van een staaf moet de grootte tonen, en daarvoor moet ze bij nul "
                "beginnen.",
                "Dit is de nuance die vaak ontbreekt: wat bij een staafgrafiek fout is, mag bij "
                "een lijngrafiek wel. Een lijn toont een beweging, en bij een temperatuur of een "
                "beurskoers zou je vanaf nul niets meer zien.",
                "Dat is een goede controle die je altijd kan doen: tel de percentages op. Komt "
                "er meer dan honderd uit, dan zaten de delen niet in één geheel, bijvoorbeeld "
                "omdat mensen meer dan één antwoord mochten geven.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-afdrukken-kopieren-en-scannen-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Bij afdrukken gaat het over het blad: de stand, de marges, hoeveel "
                   "bladzijden per vel, en of de bladzijden per exemplaar gesorteerd worden. Het "
                   "afdrukvoorbeeld is de stap die je nooit overslaat, want daar zie je alles "
                   "samen voor er papier door de machine gaat.",
            waarom=[
                "Let op sorteren. Druk je drie exemplaren van tien bladzijden zonder sorteren, "
                "dan komen er drie keer blad één, drie keer blad twee, en moet je ze zelf "
                "schikken.",
                "Dit is de meest voorkomende afdrukergernis bij een rekenblad. De instelling "
                "één bladzijde breed houdt de kolommen samen en laat het blad in de hoogte "
                "verder lopen, wat bij een lange lijst precies is wat je wil.",
                None,
            ],
        ),
        dict(
            aanpak="Drie richtingen om uit elkaar te houden: kopiëren is papier naar papier, "
                   "scannen is papier naar bestand, afdrukken is bestand naar papier. Bij "
                   "scannen beslist de resolutie in dpi over de scherpte, en voor tekst is 300 "
                   "dpi de gewoonte.",
            waarom=[
                None,
                "Reken even mee waarom dat oploopt: vier keer meer dpi betekent zestien keer "
                "meer pixels, want het geldt in de breedte en in de hoogte. Een brief van een "
                "halve megabyte wordt zo acht megabyte.",
                "Tekstherkenning heet ook ocr. Het verschil is groot in de praktijk: zonder ocr "
                "is een gescande factuur een foto waarin je niets kan zoeken, met ocr kan je er "
                "een bedrag of een naam in terugvinden.",
            ],
        ),
        dict(
            aanpak="Zes uitspraken, en bij elk dezelfde vraag: klopt dit altijd? Een uitspraak "
                   "met gewoon, altijd of hoeft geen erin is bijna nooit waar. Lees ook goed wat "
                   "er precies vergeleken wordt, zoals bij de scan in kleur tegenover "
                   "grijswaarden.",
            waarom=[
                None,
                "Waar, en dat is precies waarvoor pdf gemaakt is: de opmaak en de lettertypes "
                "zitten in het bestand zelf. Een docx verschuift wel als de andere computer het "
                "lettertype niet heeft.",
                "Niet waar. Kleur bewaart drie waarden per pixel, grijswaarden maar één, dus is "
                "een kleurenscan ongeveer drie keer zo zwaar. Voor een zwart-witte brief is dat "
                "verspilde ruimte.",
                "Waar in de praktijk, met één nuance: bij een oneven aantal bladzijden blijft de "
                "laatste zijde leeg, dus bij elf bladzijden heb je zes bladen en niet vijf en "
                "een half.",
                "Niet waar. Dat het voor de les is, maakt het niet vrij: een volledig handboek "
                "kopiëren valt niet onder wat het auteursrecht toestaat, ook niet op school. Een "
                "beperkt deel voor eigen gebruik kan wel.",
                "Waar, en de reden is boekhoudkundig. Zo komt de kost van het kopiëren bij de "
                "juiste dienst terecht, en dat is precies wat een kostenverdeling in een "
                "onderneming moet doen.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-bestanden-beheren-en-bewaren-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Een bestand vind je terug aan drie dingen: waar het staat (het pad), hoe het "
                   "heet, en wat het is (de extensie). Een goede naam maakt het pad bijna "
                   "overbodig, en daarom gaan de laatste twee oefeningen over het benoemen zelf.",
            waarom=[
                None,
                "Let op csv tegenover xlsx. Een csv is een tabel als platte tekst, zonder "
                "formules en zonder opmaak. Daarom is het de gewone manier om gegevens tussen "
                "twee programma's door te geven, en niet om je werk in te bewaren.",
                "Een goede naam heeft een vaste orde: eerst de datum, dan wat het is, dan het "
                "nummer of de naam van de tegenpartij. Zo sorteert de map zich van zelf en kan "
                "je zoeken op elk van die drie.",
                "Reken het na met een lijstje: 14-03-2027 en 02-11-2026 sorteren op dag en "
                "komen dus in de verkeerde orde. Met het jaar vooraan valt de tijdsorde samen "
                "met de alfabetische orde, en dat is de hele truc.",
            ],
        ),
        dict(
            aanpak="Bewaren gaat over twee vragen: hoe hou je het juiste bestand, en hoe hou je "
                   "het als er iets misloopt. Onthoud de regel van drie kopieën met haar drie "
                   "getallen: drie kopieën, twee dragers, één elders.",
            waarom=[
                "Merk op waar het misgaat: wie opslaan gebruikt waar hij opslaan als bedoelde, "
                "heeft het origineel overschreven. Werk je aan een versie van iemand anders, "
                "begin dan altijd met opslaan als.",
                None,
                "Het woord elders in de regel van drie kopieën is net het belangrijkste woord. "
                "Een tweede schijf naast je computer beschermt tegen een kapotte schijf, niet "
                "tegen brand of diefstal.",
                "Dit is de val van synchroniseren: een cloudmap is geen back-up maar een "
                "spiegel. Wat je wist, wist je overal. De versiegeschiedenis is wel een echte "
                "bescherming, en daarom moet je weten dat ze bestaat.",
            ],
        ),
        dict(
            aanpak="Zes uitspraken over veilig en ordelijk werken. Twee ervan gaan over "
                   "persoonsgegevens en de wet, de andere over afspraken in een team. Toets ze "
                   "aan dezelfde vraag als altijd: geldt dit ook als er iets misgaat of als "
                   "iemand anders het bestand nodig heeft?",
            waarom=[
                "Niet waar, en dit is de belangrijkste van de zes. Een usb-stick raakt kwijt, en "
                "met persoonsgegevens erop is dat een datalek dat de onderneming moet melden. "
                "Versleutel de stick, of werk op een beveiligde netwerkschijf.",
                None,
                "Niet waar. Een bestand in de prullenbak staat er nog, en zelfs na het legen "
                "blijft het vaak terug te halen. Dat is goed nieuws als je je vergist, en slecht "
                "nieuws als je een computer weggeeft.",
                "Waar volgens de boekhoudwet, maar met een nuance die je in de praktijk nodig "
                "hebt: de fiscale bewaartermijn werd verlengd en bedraagt voor recente "
                "boekjaren tien jaar. Wie boekhoudstukken bewaart, houdt dus beter tien jaar aan.",
                "Niet waar. Een zoekfunctie vindt wat jij geformuleerd hebt, maar niet wat je "
                "collega anders noemde. Afspraken over namen zijn juist nodig omdat er meerdere "
                "mensen in dezelfde map werken.",
                "Waar, en het werkt enkel als iedereen zich eraan houdt. Zet het nummer dan "
                "achteraan en met een vast aantal cijfers, zoals -v03, want anders komt -v10 bij "
                "sorteren voor -v3 te staan.",
            ],
        ),
    ],
)

UITLEGBLADEN["oefenbundel-presenteren-en-gegevens-in-een-databank-boost-dubbele-finaliteit"] = dict(
    reeksen=[
        dict(
            aanpak="Bij een presentatie hoort alles wat het publiek niet mag zien in de notities "
                   "en niet op de dia. Houd overgang en animatie uit elkaar: een overgang zit "
                   "tussen twee dia's, een animatie binnen één dia.",
            waarom=[
                None,
                "Dit is de reden waarom een volle dia erger is dan een lege: je publiek kan niet "
                "tegelijk lezen en luisteren, en lezen gaat sneller. Ze zijn dus al bij je "
                "laatste punt terwijl jij nog bij het eerste bent.",
                "Twee redenen zijn gevraagd, en de tweede is de minst bekende: een beamer "
                "verliest contrast door het omgevingslicht. Wat op je scherm nog net leesbaar "
                "is, is in een zaal met de gordijnen open onleesbaar.",
            ],
        ),
        dict(
            aanpak="De woorden van een databank hebben een vaste verhouding: een veld is een "
                   "kolom, een record is een rij, en een tabel is alles samen. Een query is een "
                   "vraag aan die tabel, een formulier is een scherm om erin te typen. Vergelijk "
                   "het met een rekenblad, dan zie je record en veld meteen terug.",
            waarom=[
                None,
                "Let op de eerste en de laatste. Een klantnummer waarmee je nooit rekent, mag "
                "tekst zijn, en dat is zelfs beter als er voorloopnullen in staan. En een lange "
                "opmerking hoort in een memoveld, want een gewoon tekstveld is in lengte beperkt.",
                "De eis aan een sleutel is dubbel: uniek én blijvend. Een naam faalt op beide, "
                "een e-mailadres is uniek maar verandert, en daarom gebruikt men meestal een "
                "nummer dat verder niets betekent.",
            ],
        ),
        dict(
            aanpak="De laatste reeks is de brug tussen de twee programma's. De rode draad: "
                   "gegevens die je op meer dan één plaats herhaalt, gaan vroeg of laat uit "
                   "elkaar lopen. De oplossing is altijd dezelfde: elk gegeven één keer bewaren "
                   "en er elders naar verwijzen.",
            waarom=[
                None,
                "Dat je het meerdere keren moet typen is het kleinste bezwaar. Het echte "
                "probleem is het tweede: na een verhuis staan er twee verschillende adressen van "
                "dezelfde klant in je bestand, en niemand weet nog welk het juiste is.",
                "Dit heet een relatie tussen twee tabellen, met het klantnummer als sleutel. Het "
                "adres staat dan één keer, en een verhuis is één aanpassing.",
                "Merk op dat de vraag over twee tabellen gaat: de gemeente staat bij de klanten, "
                "het jaartal bij de verkopen. Net daarom heb je een query nodig die de twee "
                "tabellen samen leest.",
            ],
        ),
    ],
)

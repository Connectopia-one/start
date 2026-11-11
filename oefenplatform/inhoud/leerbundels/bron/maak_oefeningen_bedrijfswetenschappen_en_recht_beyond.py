# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij bedrijfswetenschappen en recht 🌍 Beyond doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde stof
met andere vragen, dus gaat dezelfde pdf bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere cijfers, andere gevallen, en opdrachten die je enkel op papier
kan maken. Wie hier iets bijschrijft, legt het eerst naast
`../../beyond/bedrijfswetenschappen-en-recht.json` en naast
`maak_bedrijfswetenschappen_en_recht_beyond.py`.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel, svg

VAK = "Bedrijfswetenschappen en recht"
BEYOND = "🌍 Beyond doorstroom — 5de en 6de middelbaar"

W = "110px"
WW = "170px"
WL = "250px"

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."
HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een berekening: schrijf de formule en de tussenstap op, niet alleen de uitkomst.",
    "Bij een boeking: rekeningnummer, naam en bedrag, debet eerst.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

OEFENBUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BEYOND)
    b.setdefault("onder", ONDER)
    b.setdefault("hoe", HOE)
    OEFENBUNDELS["oefenbundel-" + slug + "-beyond-doorstroom"] = b


# ============================================================ 1
zet("ondernemingsvormen-vergelijken",
    titel="Ondernemingsvormen vergelijken",
    reeksen=[
        dict(kop="De tabel", opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["", "eenmanszaak", "bv", "nv", "cv"],
                  [["minimum aantal oprichters", "één", None, None, None],
                   ["minimumkapitaal", "geen", None, None, None],
                   ["aansprakelijkheid", None, "beperkt", None, None],
                   ["belasting op de winst", None, None, None, "vennootschapsbelasting"]],
                  "Oprichters: bv één, nv één, cv drie. Kapitaal: bv geen, nv 61 500 euro, cv geen. Aansprakelijkheid: eenmanszaak onbeperkt, nv en cv beperkt. Belasting: eenmanszaak personenbelasting, bv en nv vennootschapsbelasting.", "120px"),
             ]),
        dict(kop="Kies de beste vorm", opdracht="Welke ondernemingsvorm past het best? Zeg ook waarom.",
             oefeningen=[
                 ("open", "Jonas start alleen een fietsherstelzaak. Hij wil niet met zijn huis instaan voor de schulden.", "Een bv: één oprichter volstaat en de aansprakelijkheid is beperkt.", 2),
                 ("open", "Vijf boeren willen samen een hoevewinkel uitbaten. Ze willen geen buitenstaanders als aandeelhouder.", "Een cv: samenwerking met minstens drie oprichters, beperkt overdraagbare aandelen, beperkte aansprakelijkheid.", 2),
                 ("open", "Twee tandartsen willen samenwerken, zonder notaris en zonder veel kosten.", "Een maatschap: onderhandse akte, geen minimumkapitaal, fiscaal transparant.", 2),
                 ("open", "Een groot bedrijf wil zijn aandelen op de beurs brengen.", "Een nv: de aandelen zijn vrij overdraagbaar.", 2),
             ]),
        dict(kop="Begrippen", opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("Wat vervangt bij de bv het minimumkapitaal?", "een toereikend aanvangsvermogen en een financieel plan"),
                          ("Waar leggen vennootschappen hun jaarrekening neer?", "bij de Nationale Bank"),
                          ("Hoe heet de aansprakelijkheid van oprichters bij een faillissement binnen drie jaar met te weinig aanvangsvermogen?", "oprichtersaansprakelijkheid"),
                          ("Welke boekhouding mag een kleine eenmanszaak voeren?", "een enkelvoudige (vereenvoudigde) boekhouding")], "Vul in.", WL),
                 ("kies", "Wat kan een aandeelhouder van een bv hoogstens verliezen?", ["zijn inbreng", "zijn privévermogen", "zijn huis"], 0),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een maatschap heeft rechtspersoonlijkheid.", False),
                 ("waar", "Voor een eenmanszaak heb je een notaris nodig.", False),
                 ("waar", "Een nv kan door één persoon opgericht worden.", True),
                 ("waar", "De winst van een eenmanszaak valt onder de progressieve personenbelasting.", True),
                 ("waar", "Bij een bv kunnen de statuten de aandelen vrijer overdraagbaar maken.", True),
             ]),
    ])


# ============================================================ 2
zet("de-personenbelasting",
    titel="De personenbelasting",
    reeksen=[
        dict(kop="Soorten inkomsten", opdracht="Welke soort inkomsten is het?",
             oefeningen=[
                 ("rij", [("het loon van een verpleegkundige", "beroepsinkomsten"), ("de huur van een appartement dat je verhuurt", "onroerende inkomsten"),
                          ("de interest op een spaarrekening", "roerende inkomsten"), ("de winst van een bakker met een eenmanszaak", "beroepsinkomsten"),
                          ("dividenden van aandelen", "roerende inkomsten"), ("een occasionele winst", "diverse inkomsten")], "Vul in.", WW),
             ]),
        dict(kop="Jaren en documenten", opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("Je verdient je loon in 2027. Aanslagjaar?", "2028"),
                          ("Het document met de berekening van je belasting", "het aanslagbiljet"),
                          ("De onlinetoepassing om aangifte te doen", "Tax-on-web"),
                          ("Het voorschot dat de werkgever op je loon inhoudt", "de bedrijfsvoorheffing")], "Vul in.", WW),
             ]),
        dict(kop="Rekenen met schijven", opdracht="Schijven: tot 15 000 euro aan 25 %, van 15 000 tot 26 000 euro aan 40 %, daarboven 45 %. Reken zonder belastingvrije som, tenzij anders gevraagd.",
             oefeningen=[
                 ("kort", "Belasting op 10 000 euro?", "2 500 euro", WW),
                 ("kort", "Belasting op 22 000 euro?", "3 750 + 7 000 · 0,40 = 6 550 euro", WL),
                 ("kort", "Belasting op 36 000 euro?", "3 750 + 4 400 + 10 000 · 0,45 = 12 650 euro", WL),
                 ("kort", "Hoeveel belasting blijft er bij 36 000 euro over met een belastingvrije som van 10 000 euro, verrekend aan 25 %?", "12 650 − 2 500 = 10 150 euro", WL),
                 ("kort", "Je inkomen stijgt van 30 000 naar 32 000 euro. Hoeveel extra belasting?", "2 000 · 0,45 = 900 euro", WL),
                 ("open", "Iemand zegt: 'Ik verdien 30 000 euro, dus ik betaal 45 % op alles.' Klopt dat?", "Nee. De 45 % geldt enkel voor het deel boven 26 000 euro. Op 30 000 euro betaal je 9 950 euro, dat is ongeveer 33 %.", 2),
             ]),
        dict(kop="Aanslagbiljet", opdracht="Gegeven: berekende belasting 7 450 euro, ingehouden bedrijfsvoorheffing 8 100 euro.",
             oefeningen=[
                 ("kort", "Moet de persoon bijbetalen of krijgt hij geld terug? Hoeveel?", "terugkrijgen: 650 euro", WL),
                 ("kort", "En als de bedrijfsvoorheffing 6 900 euro was?", "bijbetalen: 550 euro", WL),
             ]),
        dict(kop="Aftrek of vermindering?", opdracht="Leg uit in een zin.",
             oefeningen=[
                 ("open", "Wat is het verschil tussen een belastingaftrek en een belastingvermindering?", "Een aftrek verlaagt het belastbaar inkomen, een vermindering verlaagt de berekende belasting.", 2),
                 ("open", "Noem drie uitgaven die je personenbelasting kunnen verlagen.", "Giften aan een erkende instelling (met fiscaal attest), pensioensparen, kosten van erkende kinderopvang.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De belastingvrije som wordt hoger als je kinderen ten laste hebt.", True),
                 ("waar", "De personenbelasting wordt berekend op het brutoloon.", False),
                 ("waar", "De gemeentebelasting is een percentage van de personenbelasting.", True),
                 ("waar", "Bij een voorstel van vereenvoudigde aangifte moet je altijd alles opnieuw invullen.", False),
             ]),
    ])


# ============================================================ 3
zet("de-vennootschapsbelasting-en-de-voorafbetalingen",
    titel="De vennootschapsbelasting en de voorafbetalingen",
    reeksen=[
        dict(kop="Belasting berekenen", opdracht="Bereken de vennootschapsbelasting.",
             oefeningen=[
                 ("rij", [("winst 120 000 euro, tarief 25 %", "30 000 euro"), ("winst 45 000 euro, tarief 20 %", "9 000 euro"),
                          ("kleine vennootschap, winst 130 000 euro: 20 % op de eerste 100 000 euro, 25 % op de rest", "20 000 + 7 500 = 27 500 euro"),
                          ("idem, winst 80 000 euro", "16 000 euro")], "Vul in.", WL),
             ]),
        dict(kop="Aanslagjaar", opdracht="Welk aanslagjaar hoort bij het boekjaar?",
             oefeningen=[
                 ("rij", [("1 januari tot 31 december 2027", "2028"), ("1 oktober 2026 tot 30 september 2027", "2027"), ("1 juli 2027 tot 30 juni 2028", "2028")], "Vul in.", W),
             ]),
        dict(kop="Voorafbetalingen", opdracht="Vermeerdering 9 %. Voordeel: VA1 12 %, VA2 10 %, VA3 8 %, VA4 6 %.",
             oefeningen=[
                 ("kort", "Belasting 30 000 euro, geen voorafbetalingen. Vermeerdering?", "2 700 euro", WW),
                 ("kort", "Belasting 30 000 euro, VA1 10 000 euro en VA3 10 000 euro. Vermeerdering?", "2 700 − (1 200 + 800) = 700 euro", WL),
                 ("kort", "Belasting 30 000 euro, VA1 25 000 euro. Vermeerdering?", "2 700 − 3 000: 0 euro (niet negatief)", WL),
                 ("kort", "Op welke datums vallen de vier voorafbetalingen?", "10 april, 10 juli, 10 oktober, 20 december", WL),
                 ("open", "Een zaakvoerder kan 10 000 euro voorafbetalen in april of in december. Wat raad je aan en waarom?", "In april: een vroege voorafbetaling krijgt een hoger percentage voordeel en verlaagt de vermeerdering meer.", 2),
             ]),
        dict(kop="Eenmanszaak of vennootschap", opdracht="Antwoord in een zin.",
             oefeningen=[
                 ("open", "Waarom is een vennootschap vaak voordeliger bij een winst van 150 000 euro?", "Het vaste tarief van de vennootschapsbelasting ligt lager dan de hoogste schijven van de progressieve personenbelasting.", 2),
                 ("open", "Wat is een bonificatie en bij welke belasting hoort ze?", "Een voordeel voor voorafbetalingen in de personenbelasting (zelfstandigen).", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De vennootschapsbelasting wordt berekend op de omzet.", False),
                 ("waar", "Voorafbetalingen zijn voorschotten op de belasting.", True),
                 ("waar", "Een kleine startende vennootschap krijgt de eerste drie boekjaren geen vermeerdering.", True),
                 ("waar", "Een eenmanszaak dient een aangifte vennootschapsbelasting in.", False),
             ]),
    ])


# ============================================================ 4
BOEK = ["rekening", "naam", "debet", "credit"]
zet("aankopen-boeken-facturen-kortingen-kosten-en-btw",
    titel="Aankopen boeken: facturen, kortingen, kosten en btw",
    reeksen=[
        dict(kop="Debet of credit?", opdracht="Vul D of C in.",
             oefeningen=[
                 ("rij", [("een stijging van een actiefrekening", "D"), ("een stijging van een schuld", "C"), ("een kost", "D"),
                          ("41100 bij een aankoopfactuur", "D"), ("44000 bij een inkomende creditnota", "D")], "Vul in.", W),
             ]),
        dict(kop="Welke rekening?", opdracht="Geef de rekening of rekeningklasse.",
             oefeningen=[
                 ("rij", [("aankoop van handelsgoederen", "60400"), ("factuur van de waterleverancier", "klasse 61"), ("aankoop van een vrachtwagen", "klasse 2"),
                          ("btw op de aankoop van een machine", "41100"), ("de schuld aan de leverancier", "44000")], "Vul in.", WW),
             ]),
        dict(kop="Factuur 1", opdracht="Handelsgoederen 4 000 euro, handelskorting 10 %, vervoerskosten 150 euro, btw 21 %, geen financiële korting.",
             oefeningen=[
                 ("kort", "Bedrag op 60400?", "3 600 + 150 = 3 750 euro", WW),
                 ("kort", "Btw?", "787,50 euro", W),
                 ("tabel", BOEK, [[None, None, None, None], [None, None, None, None], [None, None, None, None]],
                  "60400 Aankopen handelsgoederen D 3 750,00; 41100 Terug te vorderen btw D 787,50; 44000 Leveranciers C 4 537,50", "120px"),
             ]),
        dict(kop="Factuur 2: financiële korting", opdracht="Netto handelsgoederen 2 500 euro, financiële korting 2 % bij betaling binnen 8 dagen, btw 21 %.",
             oefeningen=[
                 ("kort", "Op welk bedrag bereken je de btw?", "2 450 euro", W),
                 ("kort", "Btw?", "514,50 euro", W),
                 ("kort", "Bedrag op 44000 bij ontvangst van de factuur?", "2 500 + 514,50 = 3 014,50 euro", WW),
                 ("open", "Waarom boek je de financiële korting nog niet bij ontvangst van de factuur?", "Ze is nog niet verworven: pas bij de betaling blijkt of je op tijd betaalt.", 2),
             ]),
        dict(kop="Creditnota", opdracht="Je stuurt voor 500 euro handelsgoederen terug, btw 21 %. Boek de inkomende creditnota.",
             oefeningen=[
                 ("tabel", BOEK, [[None, None, None, None], [None, None, None, None], [None, None, None, None]],
                  "44000 Leveranciers D 605,00; 60400 Aankopen handelsgoederen C 500,00; 41100 Terug te vorderen btw C 105,00", "120px"),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Het grootboek zet alle boekingen in de volgorde van de datum.", False),
                 ("waar", "Op terugstuurbare verpakking wordt geen btw aangerekend.", True),
                 ("waar", "Een handelskorting boek je apart op een opbrengstrekening.", False),
                 ("waar", "In een correcte boeking is het totaal debet gelijk aan het totaal credit.", True),
             ]),
    ])


# ============================================================ 5
zet("verkopen-betalingen-en-geldbewegingen-boeken",
    titel="Verkopen, betalingen en geldbewegingen boeken",
    reeksen=[
        dict(kop="Verkoopfactuur", opdracht="Handelsgoederen 6 000 euro, handelskorting 10 %, btw 21 %, geen financiële korting.",
             oefeningen=[
                 ("rij", [("Bedrag op 70000", "5 400 euro"), ("Btw", "1 134 euro"), ("Bedrag op 40000", "6 534 euro")], "Vul in.", WW),
                 ("tabel", BOEK, [[None, None, None, None], [None, None, None, None], [None, None, None, None]],
                  "40000 Handelsdebiteuren D 6 534,00; 70000 Verkopen handelsgoederen C 5 400,00; 45100 Te betalen btw C 1 134,00", "120px"),
             ]),
        dict(kop="Met financiële korting", opdracht="Netto 3 000 euro, financiële korting 2 % mogelijk, btw 21 %.",
             oefeningen=[
                 ("rij", [("Maatstaf voor de btw", "2 940 euro"), ("Btw", "617,40 euro"), ("Vordering op 40000", "3 617,40 euro"),
                          ("Bedrag dat de klant betaalt binnen de termijn", "3 617,40 − 60 = 3 557,40 euro")], "Vul in.", WL),
             ]),
        dict(kop="Uitgaande creditnota", opdracht="Een klant stuurt voor 400 euro goederen terug, btw 21 %. Boek de creditnota.",
             oefeningen=[
                 ("tabel", BOEK, [[None, None, None, None], [None, None, None, None], [None, None, None, None]],
                  "70000 Verkopen handelsgoederen D 400,00; 45100 Te betalen btw D 84,00; 40000 Handelsdebiteuren C 484,00", "120px"),
             ]),
        dict(kop="Dagontvangsten", opdracht="Btw 21 % inbegrepen. Bereken de verkoop zonder btw en de btw.",
             oefeningen=[
                 ("rij", [("605 euro", "500 euro en 105 euro"), ("3 630 euro", "3 000 euro en 630 euro"), ("1 452 euro", "1 200 euro en 252 euro")], "Vul in.", WL),
             ]),
        dict(kop="Bank en kas", opdracht="Welke rekening staat debet en welke credit?",
             oefeningen=[
                 ("rij", [("Een klant betaalt een factuur via de bank", "D 55000, C 40000"),
                          ("Je betaalt een leverancier via de bank", "D 44000, C 55000"),
                          ("Je brengt 800 euro van de kas naar de bank: het kasstuk", "D 58000, C 57000"),
                          ("Idem: het bankuittreksel", "D 55000, C 58000")], "Vul in.", WW),
                 ("open", "Waarom gebruik je 58000 Interne overboekingen?", "Kas en bank boeken elk in hun eigen dagboek. Zo boek je dezelfde verrichting niet twee keer; na beide boekingen is 58000 nul.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De btw op een verkoop is een opbrengst.", False),
                 ("waar", "Een toegekende financiële korting is voor de verkoper een kost.", True),
                 ("waar", "Op doorgerekende vervoerskosten komt ook btw.", True),
                 ("waar", "Een opname van de bank voor de kas verhoogt de liquide middelen.", False),
             ]),
    ])


# ============================================================ 6
zet("investeringen-leningen-lonen-en-btw-boeken",
    titel="Investeringen, leningen, lonen en btw boeken",
    reeksen=[
        dict(kop="Een lening", opdracht="Een onderneming leent op 1 januari 60 000 euro, af te lossen in drie gelijke jaarlijkse delen. Interest het eerste jaar: 2 400 euro.",
             oefeningen=[
                 ("kort", "In welke rekeninggroep boek je de lening bij ontvangst?", "17 Schulden op meer dan een jaar", WL),
                 ("kort", "Hoeveel verhuist er eind van het jaar naar groep 42?", "20 000 euro", WW),
                 ("kort", "Hoeveel betaal je bij de eerste aflossing, en welk deel is een kost?", "22 400 euro; enkel de 2 400 euro interest (groep 65)", WL),
                 ("open", "Verandert de aflossing van het kapitaal het eigen vermogen? Leg uit.", "Nee: de bank en de schuld dalen allebei met hetzelfde bedrag. Enkel de interest is een kost.", 2),
             ]),
        dict(kop="Loon berekenen", opdracht="RSZ werknemer 13,07 %.",
             oefeningen=[
                 ("rij", [("Brutoloon 3 200 euro: RSZ werknemer", "418,24 euro"),
                          ("Bedrijfsvoorheffing 520 euro: nettoloon", "3 200 − 418,24 − 520 = 2 261,76 euro"),
                          ("Werkgeversbijdrage 25 %: totale loonkost", "4 000 euro")], "Vul in.", WL),
                 ("kort", "Een arbeider: netto 1 650 euro, voorschot halverwege de maand 500 euro. Hoeveel nog uit te betalen?", "1 150 euro", WW),
             ]),
        dict(kop="Loonsynthese", opdracht="Debet of credit in de loonsynthese?",
             oefeningen=[
                 ("rij", [("brutolonen", "D"), ("werkgeversbijdragen RSZ", "D"), ("ingehouden bedrijfsvoorheffing", "C"), ("RSZ-bijdragen te betalen", "C"), ("nettolonen te betalen", "C")], "Vul in.", W),
             ]),
        dict(kop="Btw-verrekening", opdracht="Wat is het saldo en wie betaalt wie?",
             oefeningen=[
                 ("rij", [("te betalen 12 500, terug te vorderen 9 300", "3 200 euro storten aan de staat"),
                          ("te betalen 3 100, terug te vorderen 4 600", "de staat betaalt 1 500 euro terug")], "Vul in.", WL),
                 ("kort", "Welke rekening staat debet bij de verrekening?", "45100 Te betalen btw", WW),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Bedienden krijgen een verplicht voorschot halverwege de maand.", False),
                 ("waar", "De werkgeversbijdrage RSZ wordt van het loon van de werknemer afgehouden.", False),
                 ("waar", "De factuur van het sociaal secretariaat boek je in klasse 61.", True),
                 ("waar", "Een lening ontvangen verhoogt de omzet.", False),
             ]),
    ])


# ============================================================ 7
zet("eindejaarsverrichtingen-en-de-saldibalans",
    titel="Eindejaarsverrichtingen en de saldibalans",
    reeksen=[
        dict(kop="Afschrijven", opdracht="Lineair afschrijven.",
             oefeningen=[
                 ("rij", [("machine 80 000 euro, 8 jaar, geen restwaarde: afschrijving per jaar", "10 000 euro"),
                          ("vrachtwagen 90 000 euro, restwaarde 10 000 euro, 4 jaar: per jaar", "20 000 euro"),
                          ("boekwaarde van die vrachtwagen na 3 jaar", "30 000 euro"),
                          ("laptop 1 800 euro, 3 jaar: boekwaarde na 1 jaar", "1 200 euro")], "Vul in.", WW),
                 ("open", "Waarom telt een afschrijving mee in de cashflow?", "Het is een kost zonder uitgave: de winst daalt, maar er gaat geen geld van de bank.", 2),
             ]),
        dict(kop="Voorraad", opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["aankopen", "beginvoorraad", "eindvoorraad", "voorraadwijziging", "kostprijs verkochte goederen"],
                  [["70 000", "15 000", "20 000", None, None], ["30 000", "6 000", "4 000", None, None]],
                  "rij 1: toename 5 000, kostprijs 65 000; rij 2: afname 2 000, kostprijs 32 000", "110px"),
             ]),
        dict(kop="Overlopende rekeningen", opdracht="Welke overlopende rekening gebruik je op 31 december?",
             oefeningen=[
                 ("rij", [("Huur voor januari al betaald in december", "over te dragen kosten"),
                          ("Telefoonfactuur van december komt in januari", "toe te rekenen kosten"),
                          ("Een huurder betaalt in december de huur van januari aan ons", "over te dragen opbrengsten"),
                          ("Interest van dit jaar, gestort in februari", "verkregen opbrengsten")], "Vul in.", WL),
                 ("kort", "Verzekering van 2 400 euro voor 12 maanden, betaald op 1 september. Hoeveel is over te dragen kost?", "8 maanden: 1 600 euro", WW),
             ]),
        dict(kop="Belasting en bestemming", opdracht="Winst voor belasting 160 000 euro, tarief 25 %, voorafbetalingen 30 000 euro.",
             oefeningen=[
                 ("rij", [("Geraamde belasting", "40 000 euro"), ("Nog te betalen", "10 000 euro"), ("Winst na belasting", "120 000 euro")], "Vul in.", WW),
                 ("open", "Noem drie mogelijke bestemmingen van die winst.", "Reserves aanleggen, dividenden uitkeren, overdragen naar het volgende jaar.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Dividenden zijn een kost voor de vennootschap.", False),
                 ("waar", "Een voorziening boek je als het bedrag precies vaststaat.", False),
                 ("waar", "Over te dragen kosten staan op de actiefzijde.", True),
                 ("waar", "De definitieve saldibalans maak je na de eindejaarsboekingen.", True),
             ]),
    ])


# ============================================================ 8
zet("de-balans-voor-financiele-analyse",
    titel="De balans voor financiële analyse",
    reeksen=[
        dict(kop="Waar hoort het?", opdracht="Langdurende activa (LA), courante activa (CA), eigen vermogen (EV), vreemd vermogen lange termijn (VVLT) of korte termijn (VVKT)?",
             oefeningen=[
                 ("rij", [("een bedrijfsgebouw", "LA"), ("voorraad grondstoffen", "CA"), ("reserves", "EV"), ("lening op 15 jaar", "VVLT"),
                          ("schulden aan leveranciers", "VVKT"), ("geld op de bank", "CA"), ("te betalen btw", "VVKT"), ("overgedragen winst", "EV"),
                          ("vordering op een klant, betaalbaar binnen 30 dagen", "CA"), ("een bestelwagen", "LA")], "Vul in.", W),
             ]),
        dict(kop="Een herschikte balans", opdracht="Langdurende activa 420 000, courante activa 180 000, eigen vermogen 260 000, vreemd vermogen lange termijn 200 000, vreemd vermogen korte termijn 140 000 euro.",
             oefeningen=[
                 ("rij", [("Balanstotaal", "600 000 euro"), ("Permanent vermogen", "460 000 euro"), ("NBK langs boven", "460 000 − 420 000 = 40 000 euro"),
                          ("NBK langs onder", "180 000 − 140 000 = 40 000 euro"), ("Eigen vermogen in de verticale analyse", "43,3 %")], "Vul in.", WL),
                 ("open", "Is dat NBK een goed teken? Leg uit.", "Ja, het is positief: alle langdurende activa en een deel van de courante activa zijn met permanent vermogen gefinancierd.", 2),
             ]),
        dict(kop="Horizontale analyse", opdracht="Bereken de procentuele wijziging.",
             oefeningen=[
                 ("rij", [("voorraad 60 000 → 75 000", "+25 %"), ("liquide middelen 50 000 → 40 000", "−20 %"), ("omzet 800 000 → 880 000", "+10 %")], "Vul in.", W),
             ]),
        dict(kop="Begrijpen", opdracht="Antwoord in een zin.",
             oefeningen=[
                 ("open", "Wat is het verschil tussen een verticale en een horizontale analyse?", "Verticaal: elke post als % van het balanstotaal in één jaar. Horizontaal: de evolutie van een post over de jaren.", 2),
                 ("open", "Waarom is een negatief NBK meestal een risico?", "Dan zijn langdurende activa deels met kortlopende schulden gefinancierd, die binnen het jaar terugbetaald moeten worden.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een balans toont de situatie over een heel jaar.", False),
                 ("waar", "Jaarrekeningen vind je in de balanscentrale van de Nationale Bank.", True),
                 ("waar", "Voorraden horen bij de langdurende activa.", False),
             ]),
    ])


# ============================================================ 9
zet("kerncijfers-liquiditeit",
    titel="Kerncijfers: liquiditeit",
    reeksen=[
        dict(kop="Current en quick ratio", opdracht="Voorraden 90 000, vorderingen op ten hoogste een jaar 70 000, geldbeleggingen 10 000, liquide middelen 30 000, vreemd vermogen op korte termijn 160 000 euro.",
             oefeningen=[
                 ("rij", [("Courante activa", "200 000 euro"), ("Current ratio", "1,25"), ("Quick ratio", "110 000 / 160 000 ≈ 0,69")], "Vul in.", WW),
                 ("open", "Beoordeel de liquiditeit.", "In ruime zin in orde (groter dan 1), maar zonder de voorraad te verkopen dekken de snelle middelen maar ongeveer 69 % van de kortlopende schulden.", 3),
             ]),
        dict(kop="Termijnen", opdracht="Btw 21 %. Rond af op een geheel getal.",
             oefeningen=[
                 ("rij", [("Handelsvorderingen 72 600, omzet 600 000 excl. btw: klantenkrediet", "72 600 / 726 000 · 365 = 36,5 ≈ 37 dagen"),
                          ("Handelsschulden 36 300, aankopen 300 000 excl. btw: leverancierskrediet", "36 300 / 363 000 · 365 ≈ 37 dagen"),
                          ("Gemiddelde voorraad 40 000, kostprijs verkochte goederen 292 000: omlooptijd voorraad", "50 dagen")], "Vul in.", WL),
                 ("kort", "Netto te financieren periode met omlooptijd 50, klantenkrediet 37 en leverancierskrediet 37 dagen?", "50 dagen", WW),
             ]),
        dict(kop="Maatregelen", opdracht="Wordt de netto te financieren periode langer of korter?",
             oefeningen=[
                 ("rij", [("klanten krijgen korting bij snelle betaling", "korter"), ("de voorraad wordt groter", "langer"),
                          ("leveranciers eisen betaling binnen 15 in plaats van 45 dagen", "langer"), ("de onderneming gebruikt factoring", "korter")], "Vul in.", W),
                 ("open", "Hoe kan een onderneming met winst toch een liquiditeitsprobleem hebben?", "Winst is niet hetzelfde als geld op de bank: klanten kunnen traag betalen of er zit veel geld vast in voorraad.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De quick ratio is altijd kleiner dan of gelijk aan de current ratio.", True),
                 ("waar", "Een current ratio van 4 is altijd ideaal.", False),
                 ("waar", "Een lening op lange termijn om voorraad te kopen verbetert de current ratio.", True),
                 ("waar", "Bij het klantenkrediet reken je de omzet zonder btw.", False),
             ]),
    ])


# ============================================================ 10
zet("kerncijfers-solvabiliteit-en-rendabiliteit",
    titel="Kerncijfers: solvabiliteit en rendabiliteit",
    reeksen=[
        dict(kop="Een onderneming", opdracht="Eigen vermogen 360 000, vreemd vermogen 840 000 euro. Winst na belasting 54 000 euro, interestkosten 30 000 euro.",
             oefeningen=[
                 ("rij", [("Totaal vermogen", "1 200 000 euro"), ("Solvabiliteit", "30 %"), ("Schuldgraad", "70 %"),
                          ("REV", "54 000 / 360 000 = 15 %"), ("RTV", "84 000 / 1 200 000 = 7 %"), ("Hefboomfactor", "15 / 7 ≈ 2,14")], "Vul in.", WL),
                 ("open", "De interestvoet op de leningen is 4 %. Is de hefboom positief of negatief? Leg uit.", "Positief: de RTV (7 %) is hoger dan de interestvoet (4 %). Het geleende geld brengt meer op dan het kost.", 2),
             ]),
        dict(kop="Wat gebeurt er met de solvabiliteit?", opdracht="Stijgt of daalt de solvabiliteit?",
             oefeningen=[
                 ("rij", [("een kapitaalsverhoging", "stijgt"), ("een nieuwe lening op 10 jaar", "daalt"), ("winst als reserve houden", "stijgt"), ("een jaar met verlies", "daalt")], "Vul in.", W),
             ]),
        dict(kop="Hefboom", opdracht="Wat gebeurt er met de REV als de onderneming meer leent?",
             oefeningen=[
                 ("rij", [("RTV 9 %, interestvoet 5 %", "stijgt"), ("RTV 3 %, interestvoet 6 %", "daalt"), ("RTV 5 %, interestvoet 5 %", "blijft gelijk")], "Vul in.", WW),
             ]),
        dict(kop="Begrijpen", opdracht="Antwoord in een zin.",
             oefeningen=[
                 ("open", "Waarom gebruik je bij de RTV de winst vóór interest?", "Het totaal vermogen komt van eigenaars en schuldeisers; beiden krijgen een vergoeding: winst en interest.", 2),
                 ("open", "Waarom vraagt een bank een minimale solvabiliteit?", "Bij een lage solvabiliteit is de onderneming sterk afhankelijk van schuldeisers en loopt de bank meer risico.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Rendabiliteit en liquiditeit betekenen hetzelfde.", False),
                 ("waar", "Een onderneming zonder vreemd vermogen heeft een solvabiliteit van 100 %.", True),
                 ("waar", "Meer lenen verhoogt altijd de REV.", False),
             ]),
    ])


# ============================================================ 11
zet("financieringsvormen",
    titel="Financieringsvormen",
    reeksen=[
        dict(kop="Indelen", opdracht="Eigen vermogen (EV), vreemd vermogen lange termijn (VVLT) of korte termijn (VVKT)?",
             oefeningen=[
                 ("rij", [("zelffinanciering", "EV"), ("obligatielening", "VVLT"), ("kaskrediet", "VVKT"), ("kapitaalsverhoging", "EV"),
                          ("hypothecaire lening", "VVLT"), ("straight loan", "VVKT"), ("leverancierskrediet", "VVKT"), ("investeringskrediet", "VVLT")], "Vul in.", W),
             ]),
        dict(kop="Welke financiering past?", opdracht="Kies de best passende financieringsvorm en zeg waarom.",
             oefeningen=[
                 ("open", "Een transportbedrijf koopt drie vrachtwagens die zeven jaar meegaan.", "Een investeringskrediet (of leasing): een langdurend actief financier je op lange termijn.", 2),
                 ("open", "Een speelgoedwinkel heeft in november tijdelijk geld nodig voor extra voorraad.", "Een kaskrediet of straight loan: een tijdelijke nood financier je op korte termijn.", 2),
                 ("open", "Een groot bedrijf wil 50 miljoen euro ophalen zonder nieuwe eigenaars.", "Een obligatielening: obligatiehouders zijn schuldeisers, geen eigenaars.", 2),
                 ("open", "Een bedrijf heeft veel openstaande facturen bij klanten en wil sneller geld.", "Factoring: de factor betaalt meteen het grootste deel van de vorderingen.", 2),
                 ("open", "Twee jonge ontwerpers willen een nieuw soort rugzak lanceren en testen of er interesse is.", "Crowdfunding: veel mensen betalen vooraf een klein bedrag, vaak met de rugzak als tegenprestatie.", 2),
             ]),
        dict(kop="Vergelijken", opdracht="Leg het verschil uit.",
             oefeningen=[
                 ("open", "Financiële leasing en operationele leasing", "Financieel: de leasingnemer draagt de risico's en kan op het einde kopen. Operationeel: de leasinggever blijft eigenaar en zorgt vaak voor onderhoud.", 2),
                 ("open", "Crowdfunding en crowdlending", "Crowdfunding is vaak een gift of voorverkoop; crowdlending is een lening met interest.", 2),
                 ("open", "Twee nadelen van een kapitaalsverhoging", "De zeggenschap wordt verdeeld en de winst wordt over meer aandelen verdeeld.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De interest op vreemd vermogen is fiscaal aftrekbaar.", True),
                 ("waar", "Een straight loan is geschikt om een gebouw te financieren.", False),
                 ("waar", "Leverancierskrediet is altijd gratis.", False),
                 ("waar", "Bij een hypothecaire lening dient het gebouw als waarborg.", True),
             ]),
    ])


# ============================================================ 12
zet("investeringsprojecten-beoordelen",
    titel="Investeringsprojecten beoordelen",
    reeksen=[
        dict(kop="Soort investering", opdracht="Welke soort investering is het?",
             oefeningen=[
                 ("rij", [("een bakker koopt een tweede oven om meer te bakken", "uitbreidingsinvestering"),
                          ("een kapotte vrachtwagen wordt vervangen door een gelijke", "vervangingsinvestering"),
                          ("een kassasysteem dat personeelskosten bespaart", "rationalisatie-investering"),
                          ("een licentie voor boekhoudsoftware", "immateriële investering"),
                          ("aandelen kopen van een leverancier", "financiële investering")], "Vul in.", WL),
             ]),
        dict(kop="Een project", opdracht="Investering 90 000 euro, levensduur 3 jaar, geen restwaarde. Verwachte nettowinst: jaar 1 10 000, jaar 2 15 000, jaar 3 20 000 euro. Rente 8 %.",
             oefeningen=[
                 ("tabel", ["jaar", "nettowinst", "afschrijving", "cashflow", "gecumuleerd"],
                  [["1", "10 000", None, None, None], ["2", "15 000", None, None, None], ["3", "20 000", None, None, None]],
                  "afschrijving telkens 30 000; cashflow 40 000, 45 000, 50 000; gecumuleerd 40 000, 85 000, 135 000", "100px"),
                 ("kort", "Terugverdientijd?", "na 2 jaar 85 000; 5 000 / 50 000 = 0,1 jaar: 2,1 jaar", WL),
                 ("kort", "ROI op de investering?", "gemiddelde winst 15 000 / 90 000 ≈ 16,7 %", WL),
                 ("kort", "Contante waarde van de cashflow van jaar 1?", "40 000 / 1,08 ≈ 37 037 euro", WL),
             ]),
        dict(kop="Contante waarde en NCW", opdracht="Bereken.",
             oefeningen=[
                 ("rij", [("5 500 euro over 1 jaar aan 10 %", "5 000 euro"), ("24 200 euro over 2 jaar aan 10 %", "20 000 euro"),
                          ("investering 45 000, contante waarde cashflows 43 800: NCW", "−1 200 euro")], "Vul in.", WW),
                 ("open", "Aanvaard je het project met NCW −1 200 euro? Maakt het project dan zeker verlies?", "Niet aanvaarden: het brengt minder op dan de vereiste rente. Het kan wel nog winst maken in de boekhouding.", 2),
             ]),
        dict(kop="Methodes vergelijken", opdracht="Antwoord in een zin.",
             oefeningen=[
                 ("open", "Wat is het grootste nadeel van de terugverdientijd?", "Ze houdt geen rekening met de cashflows na de terugverdientijd (en niet met de tijdswaarde van geld).", 2),
                 ("open", "Wat gebeurt er met de NCW als de rente stijgt? Waarom?", "Ze daalt: toekomstige cashflows zijn vandaag minder waard.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De cashflow is altijd gelijk aan de nettowinst.", False),
                 ("waar", "De NCW houdt rekening met de tijdswaarde van geld.", True),
                 ("waar", "Een desinvestering is een investering verkopen of afstoten.", True),
             ]),
    ])


# ============================================================ 13
zet("swot-stakeholders-en-het-ondernemingsplan",
    titel="SWOT, stakeholders en het ondernemingsplan",
    reeksen=[
        dict(kop="SWOT van een ijssalon", opdracht="Sterkte (S), zwakte (W), kans (O) of bedreiging (T)?",
             oefeningen=[
                 ("rij", [("zelfgemaakt ijs met verse melk van een boer uit de buurt", "S"), ("klein terras met maar acht tafels", "W"),
                          ("er komt een nieuw fietspad langs de zaak", "O"), ("een grote keten opent een ijszaak in het centrum", "T"),
                          ("de zomers worden warmer", "O"), ("de eigenaar heeft geen tijd voor sociale media", "W"), ("de melkprijs stijgt sterk", "T")], "Vul in.", W),
                 ("open", "Bedenk een strategie die een sterkte met een kans combineert.", "Bijvoorbeeld: met het lokale ijs fietsers lokken via het nieuwe fietspad (een fietsstop met ijs).", 2),
             ]),
        dict(kop="Stakeholders", opdracht="Intern of extern? Wat is hun belang?",
             oefeningen=[
                 ("tabel", ["stakeholder", "intern of extern", "belang"],
                  [["werknemers", None, None], ["buurtbewoners", None, None], ["de bank", None, None], ["aandeelhouders", None, None]],
                  "werknemers: intern, goed loon en werkzekerheid; buurtbewoners: extern, weinig overlast; bank: extern, terugbetaling van lening en interest; aandeelhouders: intern, winst en dividend", "150px"),
             ]),
        dict(kop="Missie, visie of strategie?", opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("'Wij herstellen fietsen snel en betaalbaar voor iedereen in de buurt.'", "missie"),
                          ("'In 2030 zijn wij de bekendste fietsenhersteller van de provincie.'", "visie"),
                          ("'Volgend jaar openen we een tweede atelier en starten we een herstelabonnement.'", "strategie")], "Vul in.", WW),
             ]),
        dict(kop="Ondernemingsplan", opdracht="Antwoord in een zin.",
             oefeningen=[
                 ("open", "Noem drie onderdelen van een financieel plan.", "Een openingsbalans, een resultatenbegroting en een liquiditeitsbegroting.", 2),
                 ("open", "Geef een voorbeeld van deskresearch en van fieldresearch voor een nieuwe koffiebar.", "Desk: cijfers over koffieconsumptie of concurrenten opzoeken. Field: een enquête bij voorbijgangers.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een onderneming kan haar kansen en bedreigingen zelf bepalen.", False),
                 ("waar", "Een missie verandert meestal elk jaar.", False),
                 ("waar", "Klanten zijn externe stakeholders.", True),
             ]),
    ])


# ============================================================ 14
zet("het-business-model-canvas-en-de-bcg-matrix",
    titel="Het Business Model Canvas en de BCG-matrix",
    reeksen=[
        dict(kop="BMC van een fietskoerier", opdracht="Bij welke bouwsteen van het BMC hoort het?",
             oefeningen=[
                 ("rij", [("pakjes binnen het uur, uitstootvrij geleverd", "waardeproposities"), ("webwinkels en apotheken in de stad", "klantsegmenten"),
                          ("een app waarmee klanten een rit bestellen", "kanalen"), ("cargofietsen en ervaren koeriers", "kernmiddelen"),
                          ("ritten plannen en pakjes leveren", "kernactiviteiten"), ("een fietsenmaker die de fietsen onderhoudt", "strategische partners"),
                          ("een prijs per rit en maandabonnementen", "inkomstenstromen"), ("lonen, onderhoud, verzekering", "kostenstructuur"),
                          ("een vaste contactpersoon voor grote klanten", "klantrelaties")], "Vul in.", WW),
             ]),
        dict(kop="Teken zelf", opdracht="Maak op een apart blad een BMC voor een schoolfuif of een eigen idee. Vul alle negen vakken in.",
             oefeningen=[
                 ("open", "Welke waardepropositie kies je, en voor welk klantsegment?", "Eigen antwoord, bv. een veilige fuif met goede dj voor leerlingen van 16 tot 18 jaar.", 2),
             ]),
        dict(kop="BCG-matrix", opdracht="Waar staat het product in de BCG-matrix, en welke strategie past?",
             oefeningen=[
                 ("tabel", ["product", "vak", "strategie"],
                  [["35 % van een markt die 1 % per jaar groeit", None, None],
                   ["4 % van een markt die 25 % per jaar groeit", None, None],
                   ["marktleider in een markt die 18 % per jaar groeit", None, None],
                   ["2 % van een krimpende markt", None, None]],
                  "cash cow, melken; question mark, kiezen (investeren of stoppen); star, investeren; dog, afstoten", "150px"),
                 ("open", "Waarom heeft een onderneming best ook cash cows in haar portfolio?", "Cash cows brengen geld op zonder veel investeringen; dat geld betaalt de groei van stars en question marks.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een webshop is een kanaal.", True),
                 ("waar", "Een star levert altijd meer geld op dan hij kost.", False),
                 ("waar", "Een relatief marktaandeel boven 1 betekent dat je marktleider bent.", True),
                 ("waar", "Kernactiviteiten en kernmiddelen zijn hetzelfde.", False),
             ]),
    ])


# ============================================================ 15
zet("marketingstrategie-en-de-marketingmix",
    titel="Marketingstrategie en de marketingmix",
    reeksen=[
        dict(kop="Begrippen", opdracht="Welk begrip hoort erbij?",
             oefeningen=[
                 ("rij", [("een bakker verkoopt brood aan een restaurant", "B2B"), ("je verkoopt je gamecomputer aan een klasgenoot via een app", "C2C"),
                          ("tandpasta die je koopt zonder te vergelijken", "convenience goed"), ("een laptop waarvoor je reviews leest", "shopping goed"),
                          ("een frisdrankmerk brengt een citroenversie uit", "lijnextensie"), ("een koffiemerk lanceert koffie-ijs", "merkextensie"),
                          ("een nieuwe smartphone eerst aan 1 200 euro, later goedkoper", "afroomprijsstrategie"), ("een nieuwe streamingdienst start met een heel lage prijs", "penetratieprijs")], "Vul in.", WW),
             ]),
        dict(kop="Marketingmix", opdracht="Een jonge onderneming verkoopt herbruikbare drinkflessen.",
             oefeningen=[
                 ("open", "Beschrijf een buyer persona voor dit product.", "Eigen antwoord, bv. Lotte, 17 jaar, sport drie keer per week, let op het milieu, koopt online.", 2),
                 ("open", "Vul de 4 P's in voor die persona.", "Eigen antwoord, bv. product: stevige fles in vrolijke kleuren; prijs: 20 euro; plaats: webshop en sportwinkels; promotie: Instagram en influencers.", 3),
                 ("open", "Kies je intensieve, selectieve of exclusieve distributie? Waarom?", "Bv. selectief: sportwinkels en de eigen webshop passen bij het imago.", 2),
             ]),
        dict(kop="Productlevenscyclus", opdracht="In welke fase zit het product?",
             oefeningen=[
                 ("rij", [("omzet laag, hoge reclamekosten, net gelanceerd", "introductie"), ("omzet stijgt snel, concurrenten volgen", "groei"),
                          ("omzet stabiel en hoog, veel concurrentie", "volwassenheid"), ("omzet daalt, klanten kiezen nieuwere producten", "neergang")], "Vul in.", WW),
             ]),
        dict(kop="Customer journey", opdracht="In welke fase zit de klant?",
             oefeningen=[
                 ("rij", [("ziet voor het eerst een advertentie", "bewustwording"), ("vergelijkt prijzen op drie sites", "overweging"),
                          ("belt de klantendienst omdat de fles lekt", "service"), ("koopt een tweede fles met zijn spaarpunten", "loyaliteit")], "Vul in.", WW),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "SEO en SEA betekenen hetzelfde.", False),
                 ("waar", "Bij een pullstrategie richt de producent zijn reclame op de consument.", True),
                 ("waar", "De diepte van een assortiment is het aantal productgroepen.", False),
             ]),
    ])


# ============================================================ 16
zet("de-arbeidsovereenkomst-begin-schorsing-en-einde",
    titel="De arbeidsovereenkomst: begin, schorsing en einde",
    reeksen=[
        dict(kop="Soort overeenkomst", opdracht="Welke soort arbeidsovereenkomst past?",
             oefeningen=[
                 ("rij", [("Sara vervangt een collega tijdens haar bevallingsverlof", "vervangingsovereenkomst"),
                          ("Tim werkt in juli in een pretpark", "studentenovereenkomst"),
                          ("Een schrijnwerker wordt aangeworven tot een keuken af is", "duidelijk omschreven werk"),
                          ("Een gepensioneerde kok helpt op zaterdag in een restaurant", "flexi-job")], "Vul in.", WL),
             ]),
        dict(kop="Schorsing", opdracht="Welke schorsing is het, en in hoofde van wie?",
             oefeningen=[
                 ("tabel", ["situatie", "schorsing", "werknemer of werkgever"],
                  [["Ahmed huwt en is twee dagen weg", None, None], ["Een dakwerker kan niet werken door storm", None, None],
                   ["Een fabriek krijgt veel minder bestellingen", None, None], ["Ilse is drie weken ziek", None, None],
                   ["De vakbond legt het werk neer", None, None]],
                  "klein verlet (werknemer); slecht weer (werkgever); economische werkloosheid (werkgever); ziekte (werknemer); staking (werknemer)", "150px"),
             ]),
        dict(kop="Einde", opdracht="Hoe eindigt de overeenkomst?",
             oefeningen=[
                 ("rij", [("Een werknemer wordt betrapt op diefstal", "ontslag om dringende reden"),
                          ("Werkgever en werknemer spreken samen een einddatum af", "onderling akkoord"),
                          ("Een contract van 1 maart tot 31 augustus loopt af", "einde van de termijn"),
                          ("De werkgever betaalt het loon zonder dat er nog gewerkt wordt", "verbrekingsvergoeding")], "Vul in.", WL),
                 ("kort", "Tabel: anciënniteit 2 tot 3 jaar geeft 9 weken. Hoe lang is de opzegtermijn bij 30 maanden anciënniteit?", "9 weken", WW),
             ]),
        dict(kop="Begrijpen", opdracht="Antwoord in een zin.",
             oefeningen=[
                 ("open", "Wat is het verschil tussen een staking en een lock-out?", "Bij een staking leggen de werknemers het werk neer, bij een lock-out sluit de werkgever hen uit.", 2),
                 ("open", "Noem de drie elementen van een arbeidsovereenkomst.", "Arbeid, loon en gezag.", 1),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De jaarlijkse vakantie beëindigt de arbeidsovereenkomst.", False),
                 ("waar", "Een deeltijdse overeenkomst moet schriftelijk.", True),
                 ("waar", "Verlof om dwingende redenen wordt altijd betaald.", False),
             ]),
    ])


# ============================================================ 17
zet("logistiek-en-supply-chain-management",
    titel="Logistiek en supply chain management",
    reeksen=[
        dict(kop="Begrippen", opdracht="Welk begrip past?",
             oefeningen=[
                 ("rij", [("Een brouwerij brouwt in de winter al bier voor de zomer, op basis van een voorspelling", "pushmodel"),
                          ("Een fietsfabrikant bouwt een fiets pas na de bestelling van de klant", "pullmodel"),
                          ("Uit aardolie maakt men benzine, diesel en plastic", "divergente productie"),
                          ("Uit honderden onderdelen wordt één vliegtuig gebouwd", "convergente productie"),
                          ("Een magazijn waar vrachtwagens meteen worden overgeladen", "crossdockmagazijn"),
                          ("Een bedrijf laat zijn lonen berekenen door een sociaal secretariaat", "outsourcing")], "Vul in.", WW),
             ]),
        dict(kop="Voorraad", opdracht="Technische voorraad 320 stuks, besteld bij de leverancier 180 stuks, gereserveerd voor klanten 90 stuks. Minimumvoorraad 100 stuks.",
             oefeningen=[
                 ("rij", [("Beschikbare voorraad", "410 stuks"), ("Hoeveel stuks kan je vandaag nog fysiek leveren aan een nieuwe klant zonder de minimumvoorraad aan te spreken?", "320 − 90 − 100 = 130 stuks")], "Vul in.", WL),
                 ("open", "Waarom stijgen de bewaarkosten als je grotere bestellingen plaatst?", "De gemiddelde voorraad wordt groter: meer magazijnruimte, verzekering, interest en risico op bederf.", 2),
                 ("open", "Geef een voordeel en een nadeel van Just In Time.", "Voordeel: lage voorraadkosten. Nadeel: weinig buffer, dus gevoelig voor te late leveringen.", 2),
             ]),
        dict(kop="KOOP", opdracht="Waar ligt het klantorderontkoppelingspunt?",
             oefeningen=[
                 ("rij", [("een bakker met brood klaar in de rekken", "bij de klant"), ("een maatkleermaker met stoffen in voorraad", "bij de grondstoffen"),
                          ("een autobouwer die auto's monteert volgens de keuze van de klant uit onderdelen op voorraad", "bij de assemblage (onderdelen)")], "Vul in.", WL),
             ]),
        dict(kop="Inkoopproces", opdracht="Zet in de juiste volgorde: bestellen, specifiëren, controleren, leverancier kiezen, onderhandelen, aanvraag.",
             oefeningen=[
                 ("kort", "Volgorde", "specifiëren, aanvraag, leverancier kiezen, onderhandelen, bestellen, controleren", WL),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een hogere LPI-score betekent een betere logistiek.", True),
                 ("waar", "Gereserveerde voorraad mag je vrij verkopen.", False),
                 ("waar", "Een public warehouse verhuurt opslagruimte aan verschillende bedrijven.", True),
             ]),
    ])


# ============================================================ 18
zet("human-resources-management",
    titel="Human-resources-management",
    reeksen=[
        dict(kop="Instroom, doorstroom of uitstroom?", opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("een vacature op sociale media plaatsen", "instroom"), ("een opleiding Excel voor de boekhouders", "doorstroom"),
                          ("een exitgesprek", "uitstroom"), ("een peter of meter voor nieuwe collega's", "instroom"),
                          ("een functioneringsgesprek", "doorstroom"), ("outplacement na een herstructurering", "uitstroom")], "Vul in.", WW),
             ]),
        dict(kop="Selectie", opdracht="Welke selectietool past?",
             oefeningen=[
                 ("rij", [("een kandidaat-verkoper speelt een verkoopgesprek na", "assessment (rollenspel)"), ("een programmeur lost een codeeropdracht op", "test"),
                          ("je belt met toestemming de vorige werkgever", "referentie")], "Vul in.", WW),
             ]),
        dict(kop="Belonen", opdracht="Financieel (F) of niet-financieel (NF)?",
             oefeningen=[
                 ("rij", [("een eindejaarspremie", "F"), ("een compliment van de baas tijdens de teamvergadering", "NF"), ("ecocheques", "F"),
                          ("zelf je werkuren kiezen", "NF"), ("winstdeelname", "F")], "Vul in.", W),
             ]),
        dict(kop="Hr-KPI's", opdracht="Bereken.",
             oefeningen=[
                 ("rij", [("Gemiddeld 80 werknemers, 12 vertrekken: personeelsverloop", "15 %"), ("120 werknemers, gemiddeld 6 ziek per dag: ziekteverzuim", "5 %")], "Vul in.", WW),
                 ("open", "Het verloop stijgt van 8 % naar 15 %. Stel twee hr-maatregelen voor.", "Bv. een beter onthaal, loopbaanplanning en opleiding, meer waardering of een cafetariaplan, exitgesprekken om de oorzaak te kennen.", 3),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Selectie gebeurt vóór werving.", False),
                 ("waar", "Een hoog ziekteverzuim is een positief signaal.", False),
                 ("waar", "Bij een cafetariaplan kiest de werknemer zelf voordelen uit een pakket.", True),
             ]),
    ])


# ============================================================ 19
zet("kostprijsberekening-en-break-even",
    titel="Kostprijsberekening en break-even",
    reeksen=[
        dict(kop="Soorten kosten", opdracht="Een meubelmakerij. Vast (V) of variabel (VA)? Direct (D) of indirect (I)?",
             oefeningen=[
                 ("rij", [("het eikenhout voor een tafel", "VA, D"), ("de huur van de werkplaats", "V, I"), ("de verwarming van de werkplaats", "V, I"),
                          ("de lijm en schroeven per kast", "VA, D"), ("het loon van de boekhouder", "V, I")], "Vul in.", W),
             ]),
        dict(kop="Indirecte kosten verdelen", opdracht="18 000 euro verwarmingskosten worden verdeeld volgens oppervlakte: zagen 200 m², monteren 250 m², verpakken 150 m².",
             oefeningen=[
                 ("rij", [("zagen", "6 000 euro"), ("monteren", "7 500 euro"), ("verpakken", "4 500 euro")], "Vul in.", WW),
             ]),
        dict(kop="Kostprijs en verkoopprijs", opdracht="Een stoel: directe grondstoffen 45 euro, directe lonen 30 euro, indirecte productiekosten 15 euro, verkoop- en administratiekosten 10 euro per stuk. Winstopslag 30 % op de verkoopkostprijs.",
             oefeningen=[
                 ("rij", [("Fabricagekostprijs", "90 euro"), ("Verkoopkostprijs", "100 euro"), ("Verkoopprijs zonder btw", "130 euro"), ("Verkoopprijs met 21 % btw", "157,30 euro")], "Vul in.", WW),
                 ("kort", "Eenvoudige opslagmethode: directe kosten 300 euro, opslag 35 %. Kostprijs?", "405 euro", WW),
             ]),
        dict(kop="Break-even", opdracht="Vaste kosten 48 000 euro, verkoopprijs 60 euro, variabele kosten 36 euro per stuk.",
             oefeningen=[
                 ("rij", [("Dekkingsbijdrage per stuk", "24 euro"), ("Break-evenafzet", "2 000 stuks"), ("Break-evenomzet", "120 000 euro"),
                          ("Winst bij 2 500 stuks", "500 · 24 = 12 000 euro"), ("Break-evenafzet als de prijs naar 66 euro stijgt", "48 000 / 30 = 1 600 stuks")], "Vul in.", WL),
                 ("open", "Teken op ruitjespapier de lijnen van de vaste kosten, de totale kosten en de opbrengsten, en duid het break-evenpunt aan.", "Vaste kosten: horizontaal op 48 000. Totale kosten: van 48 000 met helling 36. Opbrengsten: door de oorsprong met helling 60. Snijpunt bij 2 000 stuks en 120 000 euro.", 3),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Als de vaste kosten stijgen, daalt de break-evenafzet.", False),
                 ("waar", "De verkoopkostprijs is altijd minstens even hoog als de fabricagekostprijs.", True),
                 ("waar", "De break-evenomzet is het aantal stuks dat je moet verkopen.", False),
             ]),
    ])


# ============================================================ 20
zet("relationele-databanken",
    titel="Relationele databanken",
    reeksen=[
        dict(kop="Een databank voor een jeugdbeweging", opdracht="Tabellen: Leden (Lidnummer, Naam, Geboortedatum, Telefoon, Groep) en Betalingen (Betaalnummer, Lidnummer, Datum, Bedrag, Betaald).",
             oefeningen=[
                 ("rij", [("Primaire sleutel van Leden", "Lidnummer"), ("Primaire sleutel van Betalingen", "Betaalnummer"),
                          ("Soort relatie tussen Leden en Betalingen", "één-op-veel"), ("Primaire tabel", "Leden"), ("Gerelateerde tabel", "Betalingen")], "Vul in.", WW),
                 ("tabel", ["veld", "gegevenstype"],
                  [["Geboortedatum", None], ["Telefoon", None], ["Bedrag", None], ["Betaald", None], ["Lidnummer", None]],
                  "Datum/tijd; Korte tekst; Valuta; Ja/nee; AutoNummering (of getal)", "150px"),
             ]),
        dict(kop="Veldeigenschappen", opdracht="Welke veldeigenschap gebruik je?",
             oefeningen=[
                 ("rij", [("Groep wordt automatisch 'Welpen' bij een nieuw lid", "standaardwaarde"), ("Naam mag niet leeg blijven", "vereist"),
                          ("Bedrag moet groter dan 0 zijn", "validatieregel"), ("De kolom toont 'Tel. ouders' in plaats van 'Telefoon'", "bijschrift"),
                          ("Een postcode heeft precies vier cijfers", "invoermasker (of veldlengte 4)")], "Vul in.", WL),
             ]),
        dict(kop="Query's", opdracht="Welke query gebruik je?",
             oefeningen=[
                 ("rij", [("alle leden van de groep Gidsen tonen, gesorteerd op naam", "selectiequery"), ("het totaal betaald bedrag per groep", "totaalquery"),
                          ("het lidgeld van alle leden met 10 euro verhogen", "bijwerkquery"), ("alle betalingen van vóór 2022 wissen", "verwijderquery"),
                          ("een nieuwe tabel maken met enkel de leiding", "tabelmaakquery")], "Vul in.", WW),
             ]),
        dict(kop="Begrijpen", opdracht="Antwoord in een zin.",
             oefeningen=[
                 ("open", "Waarom zet je het adres van een lid niet bij elke betaling?", "Om redundantie te vermijden: anders staat het op meerdere plaatsen en krijg je fouten als je maar één plaats aanpast.", 2),
                 ("open", "Wat verhindert referentiële integriteit in deze databank?", "Een betaling voor een lid dat niet bestaat, of een lid met betalingen verwijderen.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een filter verwijdert de records die niet voldoen.", False),
                 ("waar", "Een rapport dient vooral om gegevens in te voeren.", False),
                 ("waar", "Een selectiequery wijzigt geen gegevens.", True),
             ]),
    ])

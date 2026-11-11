# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij algemene economie 🌍 Beyond doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde stof
met andere vragen, dus gaat dezelfde pdf bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere cijfers, andere gevallen, en opdrachten die je enkel op papier
kan maken. Wie hier iets bijschrijft, legt het eerst naast
`../../beyond/economie.json` en naast `maak_economie_beyond.py`.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel, svg

VAK = "Economie"
BEYOND = "🌍 Beyond doorstroom — 5de en 6de middelbaar"

W = "110px"
WW = "170px"
WL = "250px"

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."
HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een berekening: schrijf de formule en de tussenstap op, niet alleen de uitkomst.",
    "Zet er de eenheid bij: euro, miljard euro, procent.",
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
zet("de-economische-kringloop-en-de-macro-economische-identiteiten",
    titel="De economische kringloop en de macro-economische identiteiten",
    reeksen=[
        dict(kop="Welke markt?", opdracht="Schrijf bij elk geval de markt: arbeidsmarkt, productmarkt of kapitaalmarkt.",
             oefeningen=[
                 ("rij", [("Een student zoekt een vakantiejob", "arbeidsmarkt"),
                          ("Een gezin koopt een nieuwe wasmachine", "productmarkt"),
                          ("Een bedrijf geeft obligaties uit om een loods te bouwen", "kapitaalmarkt"),
                          ("De stad koopt nieuwe vuilniswagens", "productmarkt"),
                          ("Een ziekenhuis werft verpleegkundigen aan", "arbeidsmarkt")],
                  "Vul in.", WW),
             ]),
        dict(kop="Van wie naar wie?", opdracht="Vul de tabel aan: wie betaalt aan wie?",
             oefeningen=[
                 ("tabel", ["stroom", "van", "naar"],
                  [["kinderbijslag", None, None], ["vennootschapsbelasting", None, None],
                   ["intrest op een spaarrekening", None, None], ["betaling voor Belgische chocolade in Japan", None, None]],
                  "kinderbijslag: overheid → gezinnen · vennootschapsbelasting: bedrijven → overheid · "
                  "intrest: financiële instellingen → gezinnen · chocolade: buitenland → België (export)", "150px"),
             ]),
        dict(kop="Rekenen met de identiteiten", opdracht="Schrijf telkens de formule en de berekening op. Alle bedragen in miljard euro.",
             oefeningen=[
                 ("kort", "Y = 800, T = 220, S = 90. Hoeveel is C?", "C = 800 − 220 − 90 = 490", W),
                 ("kort", "C = 450, I = 150, G = 180, X = 520, M = 500. Hoeveel is Y?", "Y = 450 + 150 + 180 + 20 = 800", W),
                 ("kort", "Een gezin verdient 42 000 euro, betaalt 12 500 euro belastingen en spaart 4 000 euro. Hoeveel consumeert het?", "42 000 − 12 500 − 4 000 = 25 500 euro", W),
                 ("kort", "S = 180, I = 200, T = 310, G = 270. Hoeveel is X − M?", "(180 − 200) + (310 − 270) = −20 + 40 = 20", W),
                 ("kort", "I = 120, G = 260, X = 410, M = 430, T = 240. Hoeveel is S?", "S = 120 + 260 + (410 − 430) − 240 = 120", W),
             ]),
        dict(kop="De drie saldi", opdracht="Een land heeft deze cijfers (miljard euro): S = 250, I = 210, T = 330, G = 360, X = 600, M = 590.",
             oefeningen=[
                 ("tabel", ["saldo", "berekening", "overschot of tekort?"],
                  [["spaarsaldo S − I", None, None], ["begrotingssaldo T − G", None, None], ["handelsbalanssaldo X − M", None, None]],
                  "S − I = +40 (de particulieren sparen meer dan ze investeren) · T − G = −30 (begrotingstekort) · "
                  "X − M = +10 (handelsoverschot). Controle: 40 − 30 = 10.", "150px"),
                 ("open", "De overheid heeft een tekort, en toch heeft het land een handelsoverschot. Hoe kan dat?",
                  "De particuliere sector spaart veel meer dan ze investeert. Dat spaarsaldo is groter dan het tekort van de overheid, dus blijft er een positief handelsbalanssaldo over.", 3),
             ]),
        dict(kop="Welke letter?", opdracht="Schrijf bij elke gebeurtenis in België de letter of letters: C, I, G, X of M.",
             oefeningen=[
                 ("rij", [("Een gezin koopt een fiets van een Belgisch merk", "C"),
                          ("Een Belgische brouwerij koopt een bottellijn in Italië", "I en M"),
                          ("De overheid betaalt een aannemer voor een nieuwe brug", "G"),
                          ("Een Nederlands bedrijf koopt Belgische staalplaten", "X"),
                          ("Een gezin koopt een Japanse auto", "C en M")],
                  "Vul in.", W),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een gezin dat aandelen koopt, telt in de kringloop als investering (I).", False),
                 ("waar", "In een economie zonder overheid en zonder buitenland geldt S = I.", True),
                 ("waar", "Een positief begrotingssaldo betekent dat de overheid meer uitgeeft dan ze ontvangt.", False),
                 ("waar", "Mantelzorg voor een grootouder zit niet in het klassieke kringloopmodel.", True),
             ]),
    ])


# ============================================================ 2
zet("alternatieve-economische-modellen-mvo-en-de-sdg-s",
    titel="Alternatieve economische modellen, MVO en de SDG's",
    reeksen=[
        dict(kop="Welk model?", opdracht="Schrijf bij elk voorbeeld: circulaire economie, deeleconomie, sociale economie of donuteconomie.",
             oefeningen=[
                 ("rij", [("Een gsm-fabrikant neemt oude toestellen terug om onderdelen te hergebruiken", "circulaire economie"),
                          ("Buren delen samen één aanhangwagen via een app", "deeleconomie"),
                          ("Een fietsatelier leert langdurig werklozen fietsen herstellen", "sociale economie"),
                          ("Een stad meet haar succes aan wonen, zorg én CO₂-uitstoot in plaats van aan groei", "donuteconomie")],
                  "Vul in.", WL),
             ]),
        dict(kop="De volgorde van de circulaire economie", opdracht="Zet in de juiste volgorde, van eerste keuze naar laatste keuze.",
             oefeningen=[
                 ("tabel", ["plaats", "keuze"], [["1", None], ["2", None], ["3", None]],
                  "1 minder gebruiken · 2 herstellen en hergebruiken · 3 recycleren", "200px"),
                 ("open", "Waarom komt recycleren pas op de laatste plaats?",
                  "Recycleren kost energie en er gaat altijd materiaal verloren. Een product herstellen of hergebruiken bespaart meer.", 2),
             ]),
        dict(kop="People, Planet of Profit?", opdracht="Bij welke pijler van MVO hoort elke maatregel?",
             oefeningen=[
                 ("rij", [("Een bakkerij geeft haar personeel opleiding", "People"),
                          ("Een webshop gebruikt herbruikbare verzenddozen", "Planet"),
                          ("Een bedrijf houdt genoeg winst over om te investeren", "Profit"),
                          ("Een kledingmerk controleert de werkuren in de fabrieken van zijn leveranciers", "People"),
                          ("Een transportbedrijf legt zonnepanelen op zijn loods", "Planet")],
                  "Vul in.", W),
             ]),
        dict(kop="Welk SDG en welke P?", opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["maatregel", "SDG", "kernwaarde (P)"],
                  [["Een gemeente geeft meisjes en jongens dezelfde sporttoelagen", None, None],
                   ["Een land bouwt windmolens op zee", None, None],
                   ["Twee landen werken samen om scholen te bouwen", None, None]],
                  "gendergelijkheid – People · betaalbare en duurzame energie (of klimaatactie) – Prosperity (of Planet) · "
                  "partnerschap om de doelen te bereiken – Partnership", "150px"),
             ]),
        dict(kop="Greenwashing?", opdracht="Lees de reclame. Leg uit of het greenwashing kan zijn en waarom.",
             oefeningen=[
                 ("open", "Een frisdrankmerk zet een groen blad op zijn flessen met de tekst '100 % natuurlijk gevoel'. Er staat geen label op en de fles is van nieuw plastic.",
                  "Ja, waarschijnlijk: een vaag woord ('natuurlijk') en een groen beeld, zonder erkend label of bewijs dat de fles duurzamer is.", 3),
                 ("open", "Een autofabrikant zegt 'onze nieuwe wagen stoot 30 % minder CO₂ uit dan het vorige model' en verwijst naar een officiële meting.",
                  "Dit is geen greenwashing: de bewering is concreet en er is een controleerbaar bewijs.", 2),
             ]),
        dict(kop="De donut", opdracht="Schrijf telkens: onder het sociaal fundament, in de donut, of boven het ecologisch plafond.",
             oefeningen=[
                 ("rij", [("Een land waar een kwart van de kinderen niet naar school kan", "onder het sociaal fundament"),
                          ("Een land dat veel meer CO₂ uitstoot dan de aarde kan opnemen", "boven het ecologisch plafond"),
                          ("Een land waar iedereen genoeg heeft en de natuur niet uitgeput raakt", "in de donut")],
                  "Vul in.", WL),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De SDG's moeten tegen 2030 bereikt zijn.", True),
                 ("waar", "De SDG's zijn enkel bedoeld voor ontwikkelingslanden.", False),
                 ("waar", "Bij MVO mag een bedrijf geen winst maken.", False),
                 ("waar", "In de deeleconomie gaat het om toegang tot een product, niet om het bezit.", True),
             ]),
    ])


# ============================================================ 3
zet("het-bbp-economische-groei-en-welvaartsindicatoren",
    titel="Het bbp, economische groei en welvaartsindicatoren",
    reeksen=[
        dict(kop="Toegevoegde waarde", opdracht="Bereken telkens. Schrijf de berekening op.",
             oefeningen=[
                 ("kort", "Een brouwerij verkoopt bier voor 900 000 euro en koopt voor 350 000 euro mout, hop en flessen. Bruto toegevoegde waarde?", "900 000 − 350 000 = 550 000 euro", WW),
                 ("kort", "Ze schrijft 60 000 euro af op haar ketels. Netto toegevoegde waarde?", "550 000 − 60 000 = 490 000 euro", WW),
             ]),
        dict(kop="Een bedrijfskolom", opdracht="Katoenboer: katoen voor 40. Spinnerij: garen voor 90. Kledingfabriek: T-shirts voor 200. Winkel: verkoopt voor 320.",
             oefeningen=[
                 ("tabel", ["schakel", "toegevoegde waarde"],
                  [["katoenboer", None], ["spinnerij", None], ["kledingfabriek", None], ["winkel", None], ["samen", None]],
                  "40 · 50 · 110 · 120 · samen 320, de waarde van het finale product"),
                 ("open", "Iemand telt alle omzetten op en komt aan 650. Wat is er fout?",
                  "Dan tel je het katoen en het garen meerdere keren mee. Enkel de toegevoegde waarde van elke schakel telt.", 2),
             ]),
        dict(kop="Van factorprijzen naar marktprijzen", opdracht="Bereken.",
             oefeningen=[
                 ("kort", "Bbp tegen factorprijzen 520, indirecte belastingen 85, subsidies 15. Bbp tegen marktprijzen?", "520 + 85 − 15 = 590", W),
                 ("kort", "Bbp 450, primaire inkomens uit het buitenland 30, naar het buitenland 22. Bnp?", "450 + 30 − 22 = 458", W),
             ]),
        dict(kop="Nominaal en reëel", opdracht="Hoeveel groeide het reëel bbp ongeveer?",
             oefeningen=[
                 ("rij", [("nominaal +6 %, prijzen +4 %", "ongeveer +2 %"),
                          ("nominaal +3 %, prijzen +3 %", "ongeveer 0 %"),
                          ("nominaal +2 %, prijzen +5 %", "ongeveer −3 %")],
                  "Vul in.", W),
                 ("open", "Het nominaal bbp steeg. Kan je daaruit besluiten dat er meer geproduceerd werd? Leg uit.",
                  "Nee. Het nominaal bbp stijgt ook als enkel de prijzen stijgen. Je moet het reëel bbp vergelijken.", 2),
             ]),
        dict(kop="Bbp per capita", opdracht="Bereken het bbp per capita. Rond af op duizend euro.",
             oefeningen=[
                 ("tabel", ["land", "bbp", "inwoners", "bbp per capita"],
                  [["A", "540 miljard euro", "11,7 miljoen", None], ["B", "90 miljard euro", "2,1 miljoen", None]],
                  "A: ongeveer 46 000 euro · B: ongeveer 43 000 euro", "150px"),
                 ("open", "Land A heeft het hoogste bbp per capita. Noem twee redenen waarom de inwoners van land B er toch beter aan toe kunnen zijn.",
                  "Bijvoorbeeld: het inkomen is in B gelijker verdeeld; in B is er meer vrije tijd, betere gezondheid of minder milieuschade. Het bbp per capita meet dat niet.", 3),
             ]),
        dict(kop="Telt het mee in het bbp?", opdracht="Schrijf ja of nee.",
             oefeningen=[
                 ("rij", [("Een schrijnwerker plaatst een keuken bij een klant", "ja"),
                          ("Een grootvader past elke woensdag op zijn kleinkinderen", "nee"),
                          ("Een aannemer herstelt daken na een storm", "ja"),
                          ("Een vrijwilliger geeft gratis bijles", "nee")],
                  "Vul in.", W),
             ]),
        dict(kop="Welke indicator?", opdracht="Schrijf de juiste indicator: HDI, BNG, MEW of Better Life Index.",
             oefeningen=[
                 ("rij", [("Levensverwachting, onderwijs en inkomen per inwoner", "HDI"),
                          ("Je kiest zelf hoe zwaar elk onderdeel weegt", "Better Life Index"),
                          ("Het bbp gecorrigeerd voor vrije tijd, onbetaald werk en schade", "MEW"),
                          ("Bekend geworden door Bhutan", "BNG")],
                  "Vul in.", WW),
             ]),
    ])


# ============================================================ 4
zet("de-vraagcurve-en-de-prijselasticiteit-van-de-vraag",
    titel="De vraagcurve en de prijselasticiteit van de vraag",
    reeksen=[
        dict(kop="De marktvraag", opdracht="Vul de collectieve vraag aan.",
             oefeningen=[
                 ("tabel", ["prijs", "Lotte", "Mehdi", "Noor", "marktvraag"],
                  [["2 euro", "6", "8", "4", None], ["3 euro", "4", "6", "3", None], ["4 euro", "2", "5", "1", None]],
                  "18 · 13 · 8 stuks", "90px"),
             ]),
        dict(kop="Beweging of verschuiving?", opdracht="Schrijf: beweging op de curve, verschuiving naar rechts, of verschuiving naar links. Het gaat telkens om de vraagcurve van treinkaartjes.",
             oefeningen=[
                 ("rij", [("De prijs van een treinkaartje daalt", "beweging op de curve"),
                          ("De benzineprijs stijgt fors", "verschuiving naar rechts"),
                          ("Veel werknemers krijgen een bedrijfswagen", "verschuiving naar links"),
                          ("De inkomens dalen door een crisis (treinreizen is een normaal goed)", "verschuiving naar links")],
                  "Vul in.", WL),
             ]),
        dict(kop="Elasticiteit berekenen", opdracht="Bereken de prijselasticiteit. Schrijf ook of de vraag elastisch, inelastisch of unitair elastisch is.",
             oefeningen=[
                 ("kort", "De prijs stijgt met 5 %, de hoeveelheid daalt met 2 %.", "−0,4: inelastisch", WW),
                 ("kort", "De prijs daalt van 50 naar 45 euro, de hoeveelheid stijgt van 200 naar 230.", "+15 % / −10 % = −1,5: elastisch", WW),
                 ("kort", "De prijs stijgt van 8 naar 10 euro, de hoeveelheid daalt van 400 naar 300.", "−25 % / +25 % = −1: unitair elastisch", WW),
                 ("kort", "E = −0,8 en de prijs stijgt met 10 %. Met hoeveel procent daalt de hoeveelheid?", "8 %", W),
             ]),
        dict(kop="Wat gebeurt er met de omzet?", opdracht="Schrijf: stijgt, daalt of blijft gelijk.",
             oefeningen=[
                 ("rij", [("Elastische vraag, de prijs stijgt", "daalt"),
                          ("Inelastische vraag, de prijs stijgt", "stijgt"),
                          ("Elastische vraag, de prijs daalt", "stijgt"),
                          ("Unitair elastische vraag, de prijs daalt een beetje", "blijft gelijk")],
                  "Vul in.", W),
                 ("open", "Een zwembad heeft een elastische vraag en wil meer omzet. Wat raad je aan? Leg uit.",
                  "De prijs verlagen. Bij een elastische vraag stijgt de hoeveelheid procentueel meer dan de prijs daalt, dus stijgt de omzet.", 2),
             ]),
        dict(kop="Elastisch of inelastisch?", opdracht="Schrijf bij elk product of de vraag eerder elastisch of inelastisch is, en geef de reden.",
             oefeningen=[
                 ("tabel", ["product", "elastisch of inelastisch", "reden"],
                  [["één merk chips", None, None], ["water van de waterleiding", None, None],
                   ["een cruise", None, None], ["lucifers", None, None]],
                  "chips: elastisch, veel alternatieven · water: inelastisch, eerste levensbehoefte · "
                  "cruise: elastisch, luxe en groot deel van het budget · lucifers: inelastisch, klein deel van het budget", "150px"),
             ]),
        dict(kop="Substituut of complement?", opdracht="Schrijf bij elk paar: substituten of complementaire goederen.",
             oefeningen=[
                 ("rij", [("tennisrackets en tennisballen", "complementaire goederen"),
                          ("thee en koffie", "substituten"),
                          ("een spelconsole en games", "complementaire goederen"),
                          ("de bus en de tram", "substituten")],
                  "Vul in.", WL),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een perfect inelastische vraagcurve is horizontaal.", False),
                 ("waar", "Op lange termijn is de vraag meestal elastischer dan op korte termijn.", True),
                 ("waar", "Langs een rechte, dalende vraagcurve is de elasticiteit overal even groot.", False),
             ]),
    ])


# ============================================================ 5
zet("inkomenselasticiteit-de-aanbodcurve-en-de-elasticiteit-van-het-aanbod",
    titel="Inkomenselasticiteit, de aanbodcurve en de elasticiteit van het aanbod",
    reeksen=[
        dict(kop="Inkomenselasticiteit", opdracht="Bereken de inkomenselasticiteit en schrijf welk soort goed het is.",
             oefeningen=[
                 ("tabel", ["goed", "inkomen", "vraag", "E<sub>y</sub>", "soort goed"],
                  [["sushi", "+4 %", "+10 %", None, None], ["melk", "+5 %", "+1 %", None, None],
                   ["huismerk-pasta", "+6 %", "−3 %", None, None], ["lucifers", "+8 %", "0 %", None, None]],
                  "sushi 2,5 luxegoed · melk 0,2 noodzakelijk · huismerk-pasta −0,5 inferieur · lucifers 0 indifferent", "90px"),
                 ("kort", "E<sub>y</sub> van theaterbezoek is 1,8. Het inkomen daalt met 5 %. Wat gebeurt er met de vraag?", "daalt met 9 %", WW),
             ]),
        dict(kop="Het collectieve aanbod", opdracht="Vul aan.",
             oefeningen=[
                 ("tabel", ["prijs", "boer A", "boer B", "boer C", "marktaanbod"],
                  [["1 euro", "0", "20", "10", None], ["2 euro", "15", "30", "25", None], ["3 euro", "25", "40", "35", None]],
                  "30 · 70 · 100", "90px"),
             ]),
        dict(kop="Beweging of verschuiving?", opdracht="Wat gebeurt er met de aanbodcurve van aardbeien? Schrijf: beweging op de curve, naar rechts of naar links.",
             oefeningen=[
                 ("rij", [("De prijs van aardbeien stijgt", "beweging op de curve"),
                          ("Een nieuwe serre verdubbelt de opbrengst per m²", "naar rechts"),
                          ("De lonen van de plukkers stijgen sterk", "naar links"),
                          ("De overheid geeft 10 cent subsidie per bakje", "naar rechts"),
                          ("Een hagelbui vernielt de helft van de oogst", "naar links")],
                  "Vul in.", WW),
             ]),
        dict(kop="Elasticiteit van het aanbod", opdracht="Bereken en benoem.",
             oefeningen=[
                 ("kort", "De prijs stijgt met 10 %, het aanbod met 25 %.", "2,5: elastisch", WW),
                 ("kort", "De prijs stijgt met 12 %, het aanbod met 3 %.", "0,25: inelastisch", WW),
                 ("kort", "E<sub>a</sub> = 0,6. De prijs stijgt met 5 %. Met hoeveel stijgt het aanbod?", "3 %", W),
             ]),
        dict(kop="De vraag stijgt", opdracht="Wat gebeurt er met prijs en hoeveelheid?",
             oefeningen=[
                 ("tabel", ["aanbod", "prijs", "hoeveelheid"],
                  [["perfect elastisch", None, None], ["perfect inelastisch", None, None], ["inelastisch", None, None]],
                  "perfect elastisch: prijs gelijk, hoeveelheid stijgt · perfect inelastisch: prijs stijgt, hoeveelheid gelijk · "
                  "inelastisch: prijs stijgt sterk, hoeveelheid stijgt weinig", "150px"),
                 ("open", "Geef een eigen voorbeeld van een perfect inelastisch aanbod en leg uit.",
                  "Bijvoorbeeld de plaatsen in een concertzaal op de avond zelf, of een schilderij van een overleden schilder: er kan niets meer bij, wat de prijs ook is.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een inferieur goed is een goed van slechte kwaliteit.", False),
                 ("waar", "Op lange termijn is het aanbod meestal elastischer dan op korte termijn.", True),
                 ("waar", "Een vlakkere aanbodcurve wijst, bij dezelfde schaal, op een minder elastisch aanbod.", False),
             ]),
    ])


# ============================================================ 6
zet("consumenten-en-producentensurplus-en-het-welvaartsoptimum",
    titel="Consumenten- en producentensurplus en het welvaartsoptimum",
    reeksen=[
        dict(kop="Surplus per persoon", opdracht="Bereken het surplus.",
             oefeningen=[
                 ("kort", "Yasmine wil maximaal 70 euro voor sneakers en betaalt 55 euro. Consumentensurplus?", "15 euro", W),
                 ("kort", "Een imker wil minimaal 6 euro per pot en verkoopt voor 8,50 euro. Producentensurplus?", "2,50 euro", W),
                 ("kort", "Tom wil maximaal 20 euro betalen, de prijs is 20 euro. Consumentensurplus?", "0 euro", W),
             ]),
        dict(kop="Een markt doorrekenen", opdracht="Vraag P = 90 − 2Q, aanbod P = 10 + 2Q. Schrijf je berekening op.",
             oefeningen=[
                 ("kort", "Evenwichtshoeveelheid en evenwichtsprijs?", "90 − 2Q = 10 + 2Q, Q = 20, P = 50", WW),
                 ("kort", "Consumentensurplus?", "½ · 20 · (90 − 50) = 400", W),
                 ("kort", "Producentensurplus?", "½ · 20 · (50 − 10) = 400", W),
                 ("kort", "Totale welvaart?", "800", W),
             ]),
        dict(kop="Nog een markt", opdracht="Vraag Q<sub>v</sub> = 100 − P, aanbod Q<sub>a</sub> = P − 20.",
             oefeningen=[
                 ("kort", "Evenwicht?", "100 − P = P − 20, P = 60, Q = 40", WW),
                 ("kort", "Bij welke prijs is Q<sub>v</sub> = 0? En Q<sub>a</sub> = 0?", "100 en 20", W),
                 ("kort", "CS en PS?", "CS = ½ · 40 · 40 = 800 · PS = ½ · 40 · 40 = 800", WW),
             ]),
        dict(kop="Wat gebeurt er?", opdracht="Schrijf: stijgt, daalt of blijft gelijk.",
             oefeningen=[
                 ("rij", [("De prijs daalt, de curves blijven gelijk: consumentensurplus", "stijgt"),
                          ("De vraagcurve schuift naar rechts: producentensurplus", "stijgt"),
                          ("De aanbodcurve schuift naar links: totale welvaart", "daalt")],
                  "Vul in.", W),
             ]),
        dict(kop="Pareto", opdracht="Is het een Pareto-verbetering? Schrijf ja of nee en leg kort uit.",
             oefeningen=[
                 ("open", "Twee klasgenoten ruilen vrijwillig een stripboek tegen een spel. Allebei zijn ze blijer.",
                  "Ja: allebei gaan ze erop vooruit en niemand gaat erop achteruit.", 2),
                 ("open", "De overheid neemt 100 euro af van een rijke persoon en geeft dat aan een arme persoon.",
                  "Nee: de rijke persoon gaat erop achteruit. Het kan wel rechtvaardiger zijn, maar het is geen Pareto-verbetering.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Het producentensurplus is gelijk aan de winst van de producenten.", False),
                 ("waar", "Bij volkomen concurrentie is de totale welvaart het grootst in het marktevenwicht.", True),
                 ("waar", "Volgens Adam Smith moet de overheid overal ingrijpen om het welvaartsoptimum te bereiken.", False),
             ]),
    ])


# ============================================================ 7
zet("marktvormen-en-het-monopolie",
    titel="Marktvormen en het monopolie",
    reeksen=[
        dict(kop="Welke marktvorm?", opdracht="Schrijf: volkomen concurrentie, monopolistische concurrentie, oligopolie of monopolie.",
             oefeningen=[
                 ("rij", [("Duizenden graanboeren verkopen hetzelfde graan op de wereldmarkt", "volkomen concurrentie"),
                          ("Eén bedrijf heeft een patent op een nieuw vaccin", "monopolie"),
                          ("Drie grote bedrijven maken bijna alle spelconsoles", "oligopolie"),
                          ("Tientallen kapsalons in een stad, elk met een eigen stijl", "monopolistische concurrentie")],
                  "Vul in.", WL),
             ]),
        dict(kop="Kosten", opdracht="Vul de tabel aan. TCK = 120.",
             oefeningen=[
                 ("tabel", ["Q", "TVK", "TK", "GK", "GCK", "MK"],
                  [["10", "180", None, None, None, "—"], ["11", "200", None, None, None, None], ["12", "228", None, None, None, None]],
                  "Q 10: TK 300, GK 30, GCK 12 · Q 11: TK 320, GK 29,09, GCK 10,91, MK 20 · Q 12: TK 348, GK 29, GCK 10, MK 28", "70px"),
             ]),
        dict(kop="Opbrengsten van een monopolist", opdracht="De prijsafzetcurve is P = 80 − 4Q.",
             oefeningen=[
                 ("kort", "Schrijf de formule voor TO.", "TO = 80Q − 4Q²", WW),
                 ("kort", "Schrijf de formule voor MO.", "MO = 80 − 8Q", WW),
                 ("kort", "Bij welke Q is TO het grootst?", "MO = 0, dus Q = 10", WW),
             ]),
        dict(kop="De optimale productie", opdracht="P = 80 − 4Q, MK = 16 en GK bij de optimale hoeveelheid = 30.",
             oefeningen=[
                 ("kort", "Hoeveel stuks maakt de monopolist?", "80 − 8Q = 16, Q = 8", WW),
                 ("kort", "Welke prijs vraagt hij?", "80 − 32 = 48", W),
                 ("kort", "Hoeveel winst maakt hij?", "(48 − 30) · 8 = 144", WW),
                 ("kort", "Hoeveel zou er verhandeld worden bij volkomen concurrentie, en aan welke prijs?", "80 − 4Q = 16, Q = 16, P = 16", WL),
                 ("kort", "Hoe groot is het welvaartsverlies?", "½ · (16 − 8) · (48 − 16) = 128", WL),
             ]),
        dict(kop="Leg uit", opdracht="Antwoord in een of twee zinnen.",
             oefeningen=[
                 ("open", "Waarom kiest een monopolist niet de hoeveelheid waarbij zijn totale opbrengst het grootst is?",
                  "Omdat hij naar zijn winst kijkt, dus ook naar de kosten. De winst is het grootst waar MO = MK, niet waar MO = 0.", 2),
                 ("open", "Waarom vinden economen een monopolie ongunstig voor de welvaart?",
                  "Er wordt minder verhandeld aan een hogere prijs dan bij volkomen concurrentie. Het consumentensurplus daalt en er ontstaat een welvaartsverlies dat niemand krijgt.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Bij een monopolist zijn de marginale opbrengsten gelijk aan de prijs.", False),
                 ("waar", "De MK-curve snijdt de GK-curve in haar laagste punt.", True),
                 ("waar", "Bij volkomen concurrentie zijn de marginale opbrengsten gelijk aan de marktprijs.", True),
                 ("waar", "Een monopolist kan elke prijs vragen en toch evenveel verkopen.", False),
             ]),
    ])


# ============================================================ 8
zet("monopolistische-concurrentie-oligopolie-en-speltheorie",
    titel="Monopolistische concurrentie, oligopolie en speltheorie",
    reeksen=[
        dict(kop="Kenmerken", opdracht="Vul de tabel aan met veel, enkele of laag, hoog.",
             oefeningen=[
                 ("tabel", ["marktvorm", "aantal aanbieders", "toetredingsdrempels"],
                  [["monopolistische concurrentie", None, None], ["oligopolie", None, None]],
                  "monopolistische concurrentie: veel, laag · oligopolie: enkele, hoog", "130px"),
             ]),
        dict(kop="Korte en lange termijn", opdracht="Een nieuwe bubbelthee-zaak maakt grote winst in een stad met veel gelijkaardige zaken.",
             oefeningen=[
                 ("open", "Wat gebeurt er op lange termijn met het aantal zaken en met de winst? Leg uit.",
                  "Door de winst openen nieuwe zaken (de drempels zijn laag). Ze nemen klanten af, tot de prijs gelijk is aan de gemiddelde kosten en de winst nul is.", 3),
                 ("open", "Waarom maakt de zaak veel reclame?", "Om haar thee te onderscheiden van die van de concurrenten.", 1),
             ]),
        dict(kop="De geknikte prijsafzetcurve", opdracht="Drie supermarktketens verkopen merkfrisdrank.",
             oefeningen=[
                 ("open", "Keten A verhoogt de prijs. Wat doen de andere ketens en wat gebeurt er met de verkoop van A?",
                  "Ze volgen niet; A verliest veel klanten. Boven de knik is de vraag elastisch.", 2),
                 ("open", "Keten A verlaagt de prijs. Wat doen de andere ketens en wat wint A?",
                  "Ze volgen meteen; A wint weinig klanten. Onder de knik is de vraag inelastisch.", 2),
                 ("kort", "Hoe heet het verschijnsel dat de prijs daardoor lang gelijk blijft?", "prijsstarheid", WW),
             ]),
        dict(kop="Een spel oplossen", opdracht="Twee fietsenmakers kiezen of ze op zondag open zijn. Winst van A ; winst van B.",
             oefeningen=[
                 ("tekst", '<table class="invul"><tr><th></th><th>B open</th><th>B dicht</th></tr>'
                           '<tr><th>A open</th><td>6 ; 6</td><td>12 ; 3</td></tr>'
                           '<tr><th>A dicht</th><td>3 ; 12</td><td>9 ; 9</td></tr></table>'),
                 ("kort", "Best-response van A als B open is?", "open (6 > 3)", WW),
                 ("kort", "Best-response van A als B dicht is?", "open (12 > 9)", WW),
                 ("kort", "Heeft A een dominante strategie? Welke?", "ja, open", WW),
                 ("kort", "Wat is het Nash-evenwicht?", "beide open (6 ; 6)", WW),
                 ("open", "Is dit een gevangenendilemma? Leg uit.",
                  "Ja: elk kiest uit eigenbelang open, maar samen dicht zou elk 9 geven in plaats van 6.", 2),
             ]),
        dict(kop="Kartels", opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Waarom willen oligopolisten een kartel vormen?", "Samen een hoge prijs afspreken levert elk meer op dan het Nash-evenwicht.", 1),
                 ("open", "Waarom houdt een kartel vaak geen stand?", "Elk lid wint erbij door stiekem een lagere prijs te vragen.", 1),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Op lange termijn maakt een monopolistische concurrent een grote economische winst.", False),
                 ("waar", "Kartelafspraken zijn in de EU verboden.", True),
                 ("waar", "In een Nash-evenwicht heeft geen enkele speler spijt van zijn keuze, gegeven wat de ander deed.", True),
                 ("waar", "Een spel heeft enkel een Nash-evenwicht als elke speler een dominante strategie heeft.", False),
             ]),
    ])


# ============================================================ 9
zet("prijsregulering-quota-belastingen-en-subsidies",
    titel="Prijsregulering, quota, belastingen en subsidies",
    reeksen=[
        dict(kop="De markt", opdracht="Op een markt voor concerttickets is Q<sub>v</sub> = 120 − P en Q<sub>a</sub> = P − 40.",
             oefeningen=[
                 ("kort", "Bereken het evenwicht.", "120 − P = P − 40, P = 80, Q = 40", WL),
             ]),
        dict(kop="Maximum- en minimumprijs", opdracht="Gebruik dezelfde markt.",
             oefeningen=[
                 ("kort", "De overheid legt een maximumprijs van 70 op. Tekort of overschot, en hoe groot?", "Q<sub>v</sub> = 50, Q<sub>a</sub> = 30: tekort van 20", WL),
                 ("kort", "Hoeveel wordt er verhandeld?", "30", W),
                 ("kort", "Bij Q = 30 willen kopers 90 betalen. Hoe groot is het welvaartsverlies?", "½ · (40 − 30) · (90 − 70) = 100", WL),
                 ("kort", "Een maximumprijs van 95. Wat gebeurt er?", "niets: ze ligt boven het evenwicht", WL),
                 ("kort", "Een minimumprijs van 90. Tekort of overschot, en hoe groot?", "Q<sub>v</sub> = 30, Q<sub>a</sub> = 50: overschot van 20", WL),
             ]),
        dict(kop="Belasting en subsidie", opdracht="Zelfde markt. Schrijf je berekening op.",
             oefeningen=[
                 ("kort", "Belasting van 20 per stuk bij de producent. Nieuw aanbod?", "Q<sub>a</sub> = P − 60", WW),
                 ("kort", "Welke prijs betaalt de koper en hoeveel wordt er verhandeld?", "120 − P = P − 60, P = 90, Q = 30", WL),
                 ("kort", "Hoeveel houdt de producent per stuk over?", "70", W),
                 ("kort", "Hoeveel ontvangt de overheid?", "20 · 30 = 600", WW),
                 ("kort", "Hoe groot is het welvaartsverlies?", "½ · (40 − 30) · 20 = 100", WL),
                 ("kort", "Subsidie van 20 per stuk. Nieuwe prijs, hoeveelheid en kostprijs voor de overheid?", "Q<sub>a</sub> = P − 20: P = 70, Q = 50, kost 20 · 50 = 1 000", WL),
             ]),
        dict(kop="Wie draagt de belasting?", opdracht="Schrijf: vooral de consumenten of vooral de producenten.",
             oefeningen=[
                 ("rij", [("Accijns op sigaretten (de vraag is heel inelastisch)", "vooral de consumenten"),
                          ("Belasting op één merk chips (de vraag is heel elastisch)", "vooral de producenten")],
                  "Vul in.", WL),
             ]),
        dict(kop="Wat gebeurt er met de verhandelde hoeveelheid?", opdracht="Schrijf: stijgt, daalt of blijft gelijk.",
             oefeningen=[
                 ("rij", [("Een quotum onder de evenwichtshoeveelheid", "daalt"),
                          ("Een subsidie per stuk", "stijgt"),
                          ("Een indirecte belasting", "daalt"),
                          ("Een minimumprijs onder de evenwichtsprijs", "blijft gelijk")],
                  "Vul in.", WW),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een indirecte belasting doet de aanbodcurve naar rechts schuiven.", False),
                 ("waar", "De belastingontvangsten van de overheid tellen mee als welvaartsverlies.", False),
                 ("waar", "Een maximumhuurprijs ver onder de marktprijs leidt op lange termijn tot minder huurwoningen.", True),
             ]),
    ])


# ============================================================ 10
zet("marktmacht-marktfalen-externe-effecten-en-publieke-goederen",
    titel="Marktmacht, marktfalen, externe effecten en publieke goederen",
    reeksen=[
        dict(kop="Extern effect?", opdracht="Schrijf: negatief extern effect, positief extern effect of geen extern effect.",
             oefeningen=[
                 ("rij", [("Een buur renoveert zijn gevel en jouw huis wordt meer waard", "positief extern effect"),
                          ("Een luchthaven veroorzaakt lawaai in de omliggende dorpen", "negatief extern effect"),
                          ("Je koopt een fiets en betaalt de volle prijs", "geen extern effect"),
                          ("Iemand laat zich vaccineren tegen griep", "positief extern effect")],
                  "Vul in.", WL),
             ]),
        dict(kop="Gevolgen en oplossingen", opdracht="Antwoord kort.",
             oefeningen=[
                 ("kort", "Produceert de vrije markt te veel of te weinig bij een negatief extern effect?", "te veel", W),
                 ("kort", "Een chemisch bedrijf veroorzaakt 3 euro schade per liter. Hoe hoog is de Pigouviaanse heffing?", "3 euro per liter", WW),
                 ("open", "Leg uit hoe verhandelbare emissierechten de uitstoot verminderen waar dat het goedkoopst kan.",
                  "Bedrijven die goedkoop minder kunnen uitstoten, doen dat en verkopen hun rechten. Bedrijven voor wie verminderen duur is, kopen rechten bij.", 3),
                 ("kort", "Wat doet de overheid best bij een positief extern effect?", "subsidiëren of gratis aanbieden", WL),
             ]),
        dict(kop="Asymmetrische informatie", opdracht="Lees en antwoord.",
             oefeningen=[
                 ("open", "Bij een tweedehands smartphone weet de verkoper of de batterij nog goed is, de koper niet. Waarom kan dat ervoor zorgen dat goede toestellen van de markt verdwijnen?",
                  "Kopers weten niet welk toestel goed is en willen daarom maar een lage prijs betalen. Wie een goed toestel heeft, vindt die prijs te laag en verkoopt niet.", 3),
                 ("kort", "Noem twee manieren waarop de overheid dit beperkt.", "etiketten, keuringen of garanties", WL),
             ]),
        dict(kop="Soorten goederen", opdracht="Vul de tabel aan met ja of nee en het soort goed.",
             oefeningen=[
                 ("tabel", ["goed", "rivaliserend?", "uitsluitbaar?", "soort goed"],
                  [["een pizza", None, None, None], ["een vuurtoren", None, None, None], ["de nationale defensie", None, None, None]],
                  "pizza: ja, ja, privaat · vuurtoren: nee, nee, zuiver publiek · defensie: nee, nee, zuiver publiek", "90px"),
                 ("open", "Waarom zal een privébedrijf geen vuurtoren bouwen?", "Wie niet betaalt, kan je niet tegenhouden om het licht te gebruiken. Schepen liften mee, dus het bedrijf krijgt niet betaald.", 2),
             ]),
        dict(kop="Mededinging", opdracht="Wie doet het? Schrijf: BMA of Europese Commissie.",
             oefeningen=[
                 ("rij", [("Beboet twee Belgische bakkerijketens voor prijsafspraken", "BMA"),
                          ("Voert het antitrustbeleid van de Europese Unie uit", "Europese Commissie")],
                  "Vul in.", WW),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Bij een negatief extern effect is de privékost lager dan de maatschappelijke kost.", True),
                 ("waar", "Een patent zorgt voor meer concurrentie.", False),
                 ("waar", "Een groot marktaandeel is in de EU op zich al verboden.", False),
             ]),
    ])


# ============================================================ 11
zet("de-arbeidsmarkt-werkloosheid-en-arbeidsmarktindicatoren",
    titel="De arbeidsmarkt, werkloosheid en arbeidsmarktindicatoren",
    reeksen=[
        dict(kop="Indicatoren berekenen", opdracht="Een provincie telt 800 000 mensen op arbeidsleeftijd, 560 000 werkenden en 40 000 werklozen.",
             oefeningen=[
                 ("kort", "Hoe groot is de beroepsbevolking?", "600 000", WW),
                 ("kort", "Activiteitsgraad?", "600 000 / 800 000 = 75 %", WL),
                 ("kort", "Werkzaamheidsgraad?", "560 000 / 800 000 = 70 %", WL),
                 ("kort", "Werkloosheidsgraad (afgerond op één cijfer na de komma)?", "40 000 / 600 000 = 6,7 %", WL),
                 ("kort", "10 000 werklozen stoppen ontmoedigd met zoeken. Nieuwe werkloosheidsgraad?", "30 000 / 590 000 = 5,1 %", WL),
             ]),
        dict(kop="Loon en werkloosheid", opdracht="Bij een minimumloon van 14 euro per uur bieden 1 200 mensen arbeid aan en vragen werkgevers er 950.",
             oefeningen=[
                 ("kort", "Hoeveel mensen zijn werkloos?", "250", W),
                 ("kort", "Ligt het minimumloon boven of onder het evenwichtsloon?", "boven", W),
             ]),
        dict(kop="Welke werkloosheid?", opdracht="Schrijf: frictie, seizoen, conjunctureel, structureel of technisch.",
             oefeningen=[
                 ("rij", [("Een strandredder heeft in de winter geen werk", "seizoen"),
                          ("Een bank vervangt loketbedienden door een app", "technisch"),
                          ("Door een economische crisis ontslaan veel bouwbedrijven mensen", "conjunctureel"),
                          ("Er zijn veel vacatures voor informatici, maar de werklozen hebben een ander diploma", "structureel"),
                          ("Een verpleegster verhuist en zoekt drie weken een nieuwe job", "frictie")],
                  "Vul in.", WW),
             ]),
        dict(kop="Maatregelen", opdracht="Stijgt de vraag naar arbeid of het aanbod van arbeid?",
             oefeningen=[
                 ("rij", [("Lagere werkgeversbijdragen", "de vraag"),
                          ("Een hogere werkbonus", "het aanbod"),
                          ("Een loonsubsidie bij aanwerving van een langdurig werkloze", "de vraag"),
                          ("Opleidingen voor werkzoekenden", "het aanbod")],
                  "Vul in.", WW),
             ]),
        dict(kop="Indexering en loonnorm", opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "De prijzen stijgen met 4 %. Wat doet de automatische loonindexering, en wat is een voordeel en een nadeel?",
                  "De lonen stijgen mee met ongeveer 4 %. Voordeel: de koopkracht blijft behouden. Nadeel: de loonkosten van bedrijven stijgen, wat de concurrentiekracht raakt.", 3),
                 ("kort", "Wat is de loonnorm?", "de maximale loonstijging bovenop de index", WL),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een voltijdse student hoort bij de beroepsbevolking.", False),
                 ("waar", "Er kunnen tegelijk veel werklozen en veel openstaande vacatures zijn.", True),
                 ("waar", "De werkzaamheidsgraad kan hoger zijn dan de activiteitsgraad.", False),
             ]),
    ])


# ============================================================ 12
zet("geld-monetaire-aggregaten-en-geldschepping",
    titel="Geld, monetaire aggregaten en geldschepping",
    reeksen=[
        dict(kop="Functies van geld", opdracht="Welke functie van geld gebruik je?",
             oefeningen=[
                 ("rij", [("Je vergelijkt de prijs van twee laptops", "waardemeter en rekeneenheid"),
                          ("Je betaalt je busticket", "ruil- en betaalmiddel"),
                          ("Een bedrijf krijgt een lening om een machine te kopen", "kredietmiddel"),
                          ("Je spaart voor een rijbewijs", "spaar- en beleggingsmiddel")],
                  "Vul in.", WL),
             ]),
        dict(kop="Soorten geld", opdracht="Schrijf: chartaal geld, giraal geld, quasigeld, e-money of cryptovaluta.",
             oefeningen=[
                 ("rij", [("Een munt van 2 euro", "chartaal geld"),
                          ("Het saldo op je zichtrekening", "giraal geld"),
                          ("Een termijnrekening van drie maanden", "quasigeld"),
                          ("Ether", "cryptovaluta"),
                          ("Het tegoed op een prepaid betaalkaart", "e-money")],
                  "Vul in.", WW),
             ]),
        dict(kop="Wat gebeurt er met M1 en M2?", opdracht="Schrijf: stijgt, daalt of blijft gelijk.",
             oefeningen=[
                 ("tabel", ["gebeurtenis", "M1", "M2"],
                  [["Je stort 200 euro aan biljetten op je zichtrekening", None, None],
                   ["Je zet 500 euro van je zichtrekening op je spaarrekening", None, None],
                   ["Een bank geeft je een autolening van 8 000 euro op je zichtrekening", None, None],
                   ["Je betaalt een lening van 1 000 euro terug van je zichtrekening", None, None]],
                  "gelijk, gelijk · daalt, gelijk · stijgt, stijgt · daalt, daalt", "90px"),
             ]),
        dict(kop="Geldschepping", opdracht="Bereken.",
             oefeningen=[
                 ("kort", "Banken geven samen 2,5 miljoen euro nieuwe kredieten. Klanten betalen samen 1,8 miljoen terug. Hoe verandert het giraal geld?", "stijgt met 700 000 euro", WL),
                 ("open", "Waarom kunnen commerciële banken niet onbeperkt geld scheppen?", "Ze moeten reserves en kapitaal aanhouden.", 1),
             ]),
        dict(kop="Leg uit", opdracht="Antwoord in een of twee zinnen.",
             oefeningen=[
                 ("open", "Waarom is bitcoin een slechte waardemeter?", "Omdat de waarde sterk schommelt: een prijs in bitcoin zegt vandaag iets anders dan volgende week.", 2),
                 ("open", "Waarom aanvaard je een papieren biljet dat zelf bijna niets waard is?", "Omdat je erop vertrouwt dat anderen het ook aanvaarden.", 1),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een spaarrekening is giraal geld.", False),
                 ("waar", "M3 is het ruimste aggregaat.", True),
                 ("waar", "Bij geldsubstitutie ontstaat er nieuw geld.", False),
                 ("waar", "De centrale bank is de bank van de banken.", True),
             ]),
    ])


# ============================================================ 13
zet("de-financiele-markt-en-beleggen",
    titel="De financiële markt en beleggen",
    reeksen=[
        dict(kop="Welke markt?", opdracht="Schrijf: geldmarkt of kapitaalmarkt, en primair of secundair.",
             oefeningen=[
                 ("rij", [("Een bedrijf leent voor drie maanden om lonen te betalen", "geldmarkt"),
                          ("Een start-up geeft voor het eerst aandelen uit op de beurs", "kapitaalmarkt, primair"),
                          ("Je koopt via de beurs aandelen die een andere belegger verkoopt", "kapitaalmarkt, secundair"),
                          ("De overheid geeft een nieuwe staatsbon van 10 jaar uit", "kapitaalmarkt, primair")],
                  "Vul in.", WL),
             ]),
        dict(kop="De rente", opdracht="Stijgt of daalt de rente? Leg kort uit.",
             oefeningen=[
                 ("kort", "Door onzekerheid sparen gezinnen veel meer.", "daalt: het aanbod van financiële middelen stijgt", WL),
                 ("kort", "Veel bedrijven willen tegelijk investeren in nieuwe machines.", "stijgt: de vraag stijgt", WL),
             ]),
        dict(kop="Obligatie of aandeel?", opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["kenmerk", "obligatie of aandeel?"],
                  [["Je wordt mede-eigenaar van het bedrijf", None], ["Je krijgt een vaste coupon", None],
                   ["Je kan een dividend krijgen", None], ["Er is een vaste looptijd", None]],
                  "aandeel · obligatie · aandeel · obligatie", "150px"),
                 ("open", "Je hebt een obligatie met 2 % rente. De marktrente stijgt naar 4 %. Wat gebeurt er met de koers van je obligatie, en waarom?",
                  "De koers daalt: nieuwe obligaties geven 4 %, dus wil niemand nog de volle prijs betalen voor een obligatie die maar 2 % geeft.", 3),
             ]),
        dict(kop="Welk product past?", opdracht="Schrijf: Tak21, Tak23, ETF of obligatiefonds.",
             oefeningen=[
                 ("rij", [("Je wilt zeker je inleg terug, met een gewaarborgde rente", "Tak21"),
                          ("Je wilt een fonds dat een beursindex volgt en dat je elke dag kan verkopen", "ETF"),
                          ("Een verzekering die belegt in fondsen, zonder kapitaalgarantie", "Tak23"),
                          ("Een fonds met een zo klein mogelijk risico", "obligatiefonds")],
                  "Vul in.", WW),
             ]),
        dict(kop="ESG", opdracht="Bij welke letter hoort het: E, S of G?",
             oefeningen=[
                 ("rij", [("Een bedrijf halveert zijn CO₂-uitstoot", "E"),
                          ("Een bedrijf betaalt eerlijke lonen in zijn fabrieken in Azië", "S"),
                          ("De bonus van de CEO wordt goedgekeurd door onafhankelijke bestuurders", "G")],
                  "Vul in.", W),
                 ("kort", "Hoe heet het als een fonds zich groen noemt maar in steenkool belegt?", "greenwashing", WW),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De beurs hoort bij de geldmarkt.", False),
                 ("waar", "Een bedrijf moet elk jaar dividend uitkeren.", False),
                 ("waar", "Spreiden over verschillende beleggingen beperkt het risico.", True),
                 ("waar", "Een bevek heeft een veranderlijk kapitaal.", True),
             ]),
    ])


# ============================================================ 14
zet("inkomensongelijkheid-armoede-en-herverdeling",
    titel="Inkomensongelijkheid, armoede en herverdeling",
    reeksen=[
        dict(kop="Een Lorenzcurve lezen", opdracht="In een land heeft de armste 20 % samen 8 % van het inkomen, de armste 50 % samen 30 % en de armste 80 % samen 62 %.",
             oefeningen=[
                 ("kort", "Hoeveel procent van het inkomen heeft de rijkste 20 %?", "38 %", W),
                 ("kort", "Hoeveel procent zou de armste 50 % hebben bij perfecte gelijkheid?", "50 %", W),
                 ("kort", "De overheid verhoogt de laagste uitkeringen. Schuift de curve naar de diagonaal toe of ervan weg?", "naar de diagonaal toe", WL),
             ]),
        dict(kop="Gini", opdracht="Bereken en vergelijk.",
             oefeningen=[
                 ("kort", "De oppervlakte tussen diagonaal en Lorenzcurve is 0,2. Gini?", "0,2 / 0,5 = 0,4", WW),
                 ("kort", "De oppervlakte is 0,12. Gini?", "0,12 / 0,5 = 0,24", WW),
                 ("kort", "Welk van de twee landen is het gelijkst?", "het land met Gini 0,24", WL),
             ]),
        dict(kop="Armoede", opdracht="Het mediaaninkomen van een alleenstaande is 2 200 euro per maand.",
             oefeningen=[
                 ("kort", "Waar ligt de armoedegrens (AROP)?", "60 % van 2 200 = 1 320 euro", WL),
                 ("kort", "Loopt iemand met 1 250 euro een risico op monetaire armoede?", "ja", W),
                 ("open", "Waarom gebruikt men de mediaan en niet het gemiddelde?", "De mediaan reageert minder op enkele zeer hoge inkomens, die het gemiddelde omhoogtrekken.", 2),
             ]),
        dict(kop="Sociale zekerheid", opdracht="Schrijf: vervangingsinkomen of aanvulling op het inkomen.",
             oefeningen=[
                 ("rij", [("Een rustpensioen", "vervangingsinkomen"),
                          ("Het Groeipakket voor kinderen", "aanvulling op het inkomen"),
                          ("Een uitkering na een arbeidsongeval", "vervangingsinkomen")],
                  "Vul in.", WL),
                 ("kort", "Hoeveel takken telt de Belgische sociale zekerheid?", "zeven", W),
                 ("open", "Leg het verschil uit tussen het verzekeringsprincipe en het solidariteitsprincipe.",
                  "Verzekeringsprincipe: wie bijdraagt, is verzekerd tegen risico's. Solidariteitsprincipe: de sterkste schouders dragen de zwaarste lasten.", 3),
             ]),
        dict(kop="Belasting", opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Waarom verkleint een progressieve personenbelasting de ongelijkheid meer dan een vlaktaks?",
                  "Bij een progressieve belasting betalen hogere inkomens een groter percentage. Bij een vlaktaks betaalt iedereen hetzelfde percentage.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Armoede en ongelijkheid betekenen hetzelfde.", False),
                 ("waar", "Een land met een lage Gini kan toch arm zijn.", True),
                 ("waar", "Vermogen speelt geen rol in de inkomensongelijkheid.", False),
             ]),
    ])


# ============================================================ 15
zet("internationale-handel-en-samenwerkingsverbanden",
    titel="Internationale handel en samenwerkingsverbanden",
    reeksen=[
        dict(kop="Samenwerkingsverbanden", opdracht="Welke vorm van samenwerking is het?",
             oefeningen=[
                 ("rij", [("Geen invoerrechten onderling, één gemeenschappelijk buitentarief, verder niets", "douane-unie"),
                          ("Geen invoerrechten onderling, elk land kiest zijn eigen tarief naar buiten", "vrijhandelszone"),
                          ("Eén munt en één centrale bank", "monetaire unie"),
                          ("Vrij verkeer van goederen, diensten, personen en kapitaal", "gemeenschappelijke markt")],
                  "Vul in.", WW),
                 ("kort", "Welke stap volgt na een gemeenschappelijke markt?", "een economische unie", WW),
             ]),
        dict(kop="Handelsbalans en quotes", opdracht="Vul de tabel aan (in miljard euro).",
             oefeningen=[
                 ("tabel", ["land", "bbp", "export", "import", "saldo", "uitvoerquote", "invoerquote"],
                  [["A", "400", "340", "360", None, None, None], ["B", "2 000", "240", "200", None, None, None]],
                  "A: saldo −20, uitvoerquote 85 %, invoerquote 90 % · B: saldo +40, uitvoerquote 12 %, invoerquote 10 %", "60px"),
                 ("kort", "Welk land is het meest open, en welk land is waarschijnlijk het grootst?", "A is het meest open, B is waarschijnlijk het grootst", WL),
                 ("open", "Hoe kan een uitvoerquote groter zijn dan 100 %?", "De export bevat ook ingevoerde onderdelen, die niet in het bbp zitten.", 2),
             ]),
        dict(kop="Productie verplaatsen", opdracht="Schrijf: outsourcing, offshoring, nearshoring of reshoring.",
             oefeningen=[
                 ("rij", [("Een Belgische fietsfabrikant verplaatst de montage van Taiwan naar Roemenië", "nearshoring"),
                          ("Een speelgoedbedrijf haalt zijn productie terug uit China naar België", "reshoring"),
                          ("Een bank laat de schoonmaak van haar kantoren doen door een schoonmaakbedrijf", "outsourcing"),
                          ("Een textielbedrijf verplaatst zijn naaiatelier van België naar Bangladesh", "offshoring")],
                  "Vul in.", WW),
                 ("kort", "Geef twee redenen voor reshoring.", "hoge transportkosten, problemen in de toeleveringsketen", WL),
             ]),
        dict(kop="Gevolgen", opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Leg handelsverlegging uit met een eigen voorbeeld.",
                  "Bijvoorbeeld: België koopt textiel in Portugal (lid van de unie) in plaats van in Marokko, ook al produceert Marokko goedkoper, omdat er op Marokkaans textiel een invoerrecht zit.", 3),
                 ("open", "Noem een voordeel en een nadeel van een monetaire unie.",
                  "Voordeel: geen wisselkoersrisico en geen wisselkosten. Nadeel: een land kan zijn munt niet meer devalueren om goedkoper te exporteren.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Een positief saldo op de handelsbalans heet een handelstekort.", False),
                 ("waar", "Bij outsourcing blijft de taak altijd in hetzelfde land.", False),
                 ("waar", "België heeft een open economie.", True),
             ]),
    ])


# ============================================================ 16
zet("de-wisselmarkt-en-de-betalingsbalans",
    titel="De wisselmarkt en de betalingsbalans",
    reeksen=[
        dict(kop="Vraag of aanbod van euro?", opdracht="Schrijf: vraagt euro's of biedt euro's aan.",
             oefeningen=[
                 ("rij", [("Een Chinese toerist komt naar Gent", "vraagt euro's"),
                          ("Een Belgisch bedrijf koopt Amerikaanse software", "biedt euro's aan"),
                          ("Een Amerikaanse belegger koopt Belgische staatsobligaties", "vraagt euro's"),
                          ("Een Belgische student gaat op Erasmus in Zweden", "biedt euro's aan")],
                  "Vul in.", WW),
             ]),
        dict(kop="Rekenen met koersen", opdracht="Schrijf je berekening op.",
             oefeningen=[
                 ("kort", "1 euro = 1,20 dollar. Wat kost een Belgische fiets van 1 500 euro in dollar?", "1 500 · 1,20 = 1 800 dollar", WL),
                 ("kort", "1 euro = 1,20 dollar. Een Amerikaans boek kost 30 dollar. Hoeveel euro?", "30 / 1,20 = 25 euro", WL),
                 ("kort", "De koers gaat van 1,20 naar 1,05. Apprecieert of deprecieert de euro?", "deprecieert", WW),
                 ("kort", "Wat kost de fiets van 1 500 euro nu in dollar?", "1 500 · 1,05 = 1 575 dollar", WL),
             ]),
        dict(kop="Wat gebeurt er met de euro?", opdracht="Schrijf: apprecieert of deprecieert.",
             oefeningen=[
                 ("rij", [("De ECB verlaagt de rente", "deprecieert"),
                          ("De inflatie in de eurozone is lager dan in de VS", "apprecieert"),
                          ("Speculanten verwachten dat de euro zal dalen en verkopen euro's", "deprecieert"),
                          ("Europese wijnen worden heel populair in Azië", "apprecieert")],
                  "Vul in.", WW),
             ]),
        dict(kop="De betalingsbalans", opdracht="Op welke deelrekening en welke post?",
             oefeningen=[
                 ("rij", [("Een Belgische chocolatier verkoopt pralines in Japan", "lopende rekening, goederen"),
                          ("Een Franse familie huurt een vakantiehuis aan de Belgische kust", "lopende rekening, diensten"),
                          ("Een Belg krijgt intrest op een Duitse obligatie", "lopende rekening, primaire inkomens"),
                          ("Een Belgisch bedrijf koopt een fabriek in Spanje", "financiële rekening"),
                          ("Een Poolse werknemer in België stuurt geld naar zijn ouders", "lopende rekening, secundaire inkomens")],
                  "Vul in.", WL),
             ]),
        dict(kop="Instellingen", opdracht="Welke instelling? Schrijf: IMF, Wereldbank of OESO.",
             oefeningen=[
                 ("rij", [("Een land kan zijn buitenlandse schulden niet meer betalen en vraagt hulp", "IMF"),
                          ("Een lening voor waterleidingen in een arm land", "Wereldbank"),
                          ("Een rapport dat de onderwijssystemen van de lidstaten vergelijkt", "OESO")],
                  "Vul in.", W),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Bij een appreciatie van de euro wordt de Europese export goedkoper.", False),
                 ("waar", "De handelsbalans is een onderdeel van de lopende rekening.", True),
                 ("waar", "Bij vlottende wisselkoersen bepaalt de regering de koers.", False),
             ]),
    ])


# ============================================================ 17
zet("de-conjunctuur-conjunctuurindicatoren-en-de-begroting",
    titel="De conjunctuur, conjunctuurindicatoren en de begroting",
    reeksen=[
        dict(kop="Welke fase?", opdracht="Schrijf: expansie, boom, recessie, depressie of herstel.",
             oefeningen=[
                 ("rij", [("Het reëel bbp daalt al drie kwartalen; bedrijven ontslaan mensen", "recessie"),
                          ("Het dieptepunt: de productie is het laagst", "depressie"),
                          ("Na het dieptepunt neemt de groei voorzichtig weer toe", "herstel"),
                          ("Sterke groei, veel investeringen, de werkloosheid daalt", "expansie"),
                          ("Het hoogtepunt: fabrieken draaien op volle kracht en de prijzen stijgen", "boom")],
                  "Vul in.", WW),
             ]),
        dict(kop="Outputkloof", opdracht="Bereken de outputkloof en schrijf: onderbesteding, bestedingsevenwicht of overbesteding.",
             oefeningen=[
                 ("tabel", ["land", "reëel bbp", "potentieel bbp", "outputkloof", "situatie"],
                  [["A", "520", "500", None, None], ["B", "370", "400", None, None], ["C", "300", "300", None, None]],
                  "A: +20, overbesteding · B: −30, onderbesteding · C: 0, bestedingsevenwicht", "110px"),
             ]),
        dict(kop="Indicatoren", opdracht="Vul de tabel aan: voorlopend, gelijklopend of achterlopend, en kwalitatief of kwantitatief.",
             oefeningen=[
                 ("tabel", ["indicator", "wanneer?", "soort"],
                  [["het ondernemersvertrouwen", None, None], ["de werkloosheid", None, None], ["de BEL20-beursindex", None, None]],
                  "ondernemersvertrouwen: voorlopend, kwalitatief · werkloosheid: achterlopend, kwantitatief · BEL20: voorlopend, kwantitatief", "120px"),
             ]),
        dict(kop="Exogeen of endogeen?", opdracht="Schrijf exogeen of endogeen.",
             oefeningen=[
                 ("rij", [("Een vulkaanuitbarsting legt het luchtverkeer maanden stil", "exogeen"),
                          ("Na jaren van te veel kredieten moeten gezinnen hun schulden afbouwen", "endogeen")],
                  "Vul in.", W),
             ]),
        dict(kop="De begroting", opdracht="De overheid ontvangt 150 miljard aan directe belastingen, 90 miljard aan indirecte belastingen, 80 miljard aan sociale bijdragen en 10 miljard niet-fiscale inkomsten. Ze geeft 345 miljard uit.",
             oefeningen=[
                 ("kort", "Totale inkomsten?", "330 miljard", WW),
                 ("kort", "Begrotingssaldo? Tekort of overschot?", "−15 miljard: een tekort", WL),
                 ("kort", "Wat gebeurt er met de staatsschuld?", "ze stijgt", WW),
                 ("open", "Waarom verslechtert het saldo tijdens een recessie?", "Er komen minder belastingen binnen en de overheid betaalt meer uitkeringen.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "De btw is een directe belasting.", False),
                 ("waar", "Tijdens een hoogconjunctuur kan er overbesteding ontstaan.", True),
                 ("waar", "Een boom is het dieptepunt van de conjunctuurgolf.", False),
             ]),
    ])


# ============================================================ 18
zet("het-inkomensevenwicht-de-multiplicator-en-het-av-aa-schema",
    titel="Het inkomensevenwicht, de multiplicator en het AV-AA-schema",
    reeksen=[
        dict(kop="Het evenwichtsinkomen", opdracht="Gesloten economie zonder overheid: C = 40 + 0,75Y en I = 60.",
             oefeningen=[
                 ("kort", "Marginale consumptiequote?", "0,75", W),
                 ("kort", "Evenwichtsinkomen?", "Y = 40 + 0,75Y + 60, 0,25Y = 100, Y = 400", WL),
                 ("kort", "Multiplicator?", "1 / 0,25 = 4", WW),
                 ("kort", "De investeringen stijgen met 15. Nieuw evenwichtsinkomen?", "400 + 4 · 15 = 460", WL),
             ]),
        dict(kop="Multiplicatoren", opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["marginale consumptiequote", "marginale spaarquote", "multiplicator"],
                  [["0,5", None, None], ["0,8", None, None], ["0,6", None, None]],
                  "0,5: 0,5 en 2 · 0,8: 0,2 en 5 · 0,6: 0,4 en 2,5", "80px"),
                 ("kort", "De overheid verhoogt haar uitgaven met 8 miljard. De multiplicator is 2,5. Met hoeveel stijgt het inkomen?", "20 miljard", WL),
                 ("open", "Leg uit waarom het inkomen meer stijgt dan de extra uitgave, en wat de lekken zijn.",
                  "De uitgave wordt inkomen voor anderen, die er weer een deel van besteden, enzovoort. Bij elke ronde lekt er iets weg naar sparen en belastingen.", 3),
             ]),
        dict(kop="Schokken in het AV-AA-schema", opdracht="Welke curve verschuift, en naar links of naar rechts?",
             oefeningen=[
                 ("rij", [("Gezinnen geven door onzekerheid veel minder uit", "AV naar links"),
                          ("De gasprijs verdubbelt", "AA naar links"),
                          ("Robots verhogen de productiviteit sterk", "AA naar rechts"),
                          ("De buitenlandse vraag naar Belgische producten stijgt", "AV naar rechts")],
                  "Vul in.", WW),
                 ("kort", "Hoe heet een situatie met hogere prijzen en minder productie?", "stagflatie", WW),
             ]),
        dict(kop="Beleid", opdracht="Budgettair of monetair? Expansief of restrictief?",
             oefeningen=[
                 ("rij", [("De ECB verhoogt de rente", "monetair, restrictief"),
                          ("De regering bouwt extra scholen", "budgettair, expansief"),
                          ("De regering verhoogt de btw", "budgettair, restrictief"),
                          ("De ECB verlaagt de rente", "monetair, expansief")],
                  "Vul in.", WL),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Met belastingen erbij is de multiplicator groter dan zonder.", False),
                 ("waar", "Op lange termijn is de AA-curve verticaal bij het potentieel bbp.", True),
                 ("waar", "Een restrictief beleid doet de AV-curve naar rechts schuiven.", False),
             ]),
    ])


# ============================================================ 19
zet("inflatie-deflatie-en-prijsstabiliteit",
    titel="Inflatie, deflatie en prijsstabiliteit",
    reeksen=[
        dict(kop="Welke inflatie?", opdracht="Schrijf: bestedingsinflatie, kosteninflatie, importinflatie, monetaire inflatie, krimpflatie of beknibbelflatie.",
             oefeningen=[
                 ("rij", [("Een reep chocolade gaat van 200 naar 170 gram, de prijs blijft gelijk", "krimpflatie"),
                          ("Ingevoerde koffiebonen worden 40 % duurder", "importinflatie"),
                          ("Door een sterke loonstijging verhogen bakkers hun prijzen", "kosteninflatie"),
                          ("Een hotel schrapt de dagelijkse schoonmaak, de prijs blijft gelijk", "beknibbelflatie"),
                          ("De centrale bank drukt veel geld bij terwijl de productie gelijk blijft", "monetaire inflatie"),
                          ("Iedereen wil tegelijk bouwen en de aannemers kunnen het werk niet aan", "bestedingsinflatie")],
                  "Vul in.", WW),
             ]),
        dict(kop="Rekenen", opdracht="Schrijf je berekening op.",
             oefeningen=[
                 ("kort", "De CPI gaat van 140 naar 147. Inflatie?", "7 / 140 · 100 = 5 %", WL),
                 ("kort", "De CPI gaat van 160 naar 156. Prijsverandering?", "−4 / 160 · 100 = −2,5 %", WL),
                 ("kort", "Een pak koekjes gaat van 300 naar 250 gram aan dezelfde prijs. Hoeveel procent steeg de prijs per gram?", "300 / 250 = 1,2, dus 20 %", WL),
                 ("kort", "Fisher: V en T blijven gelijk en M stijgt met 50 %. Wat gebeurt er met P?", "P stijgt met 50 %", WL),
             ]),
        dict(kop="Indexen", opdracht="Welke index? Schrijf: CPI, HICP, gezondheidsindex, spilindex of bbp-deflator.",
             oefeningen=[
                 ("rij", [("Je wilt de inflatie in België en Italië vergelijken", "HICP"),
                          ("De index zonder tabak, alcohol en brandstof", "gezondheidsindex"),
                          ("Een drempel voor het aanpassen van uitkeringen", "spilindex"),
                          ("De prijzen van alles wat in België geproduceerd wordt", "bbp-deflator")],
                  "Vul in.", WW),
             ]),
        dict(kop="Gevolgen en beleid", opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Lena heeft 5 000 euro op een spaarrekening met 1 % rente. De inflatie is 4 %. Wint of verliest ze koopkracht? Leg uit.",
                  "Ze verliest ongeveer 3 % koopkracht: haar geld groeit met 1 %, maar de prijzen stijgen met 4 %.", 2),
                 ("open", "Waarom kan deflatie de economie verder afremmen?",
                  "Consumenten stellen aankopen uit omdat het later goedkoper wordt. Daardoor daalt de vraag nog meer.", 2),
                 ("kort", "Welk inflatiedoel heeft de ECB?", "2 % op middellange termijn", WL),
                 ("kort", "Wat doet de ECB bij een te hoge inflatie?", "de beleidsrente verhogen", WL),
                 ("rij", [("De overheid verlaagt de btw op elektriciteit", "onrechtstreeks"),
                          ("De overheid legt een maximumprijs op voor gas", "rechtstreeks")],
                  "Rechtstreeks of onrechtstreeks prijsbeleid?", WW),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Bij deflatie wordt een schuld met vaste rente lichter om te dragen.", False),
                 ("waar", "De ECB kan de Belgische btw-tarieven verlagen.", False),
                 ("waar", "De bbp-deflator houdt ook rekening met investeringsgoederen.", True),
             ]),
    ])


# ============================================================ 20
zet("economisch-onderzoek-onderzoeksvraag-methode-en-besluit",
    titel="Economisch onderzoek: onderzoeksvraag, methode en besluit",
    reeksen=[
        dict(kop="De onderzoekscyclus", opdracht="In welke fase doe je dit?",
             oefeningen=[
                 ("rij", [("Je maakt een planning en kiest een enquête als methode", "voorbereiden"),
                          ("Je schrijft je onderzoeksvraag op", "oriënteren"),
                          ("Je neemt de enquête af bij 120 jongeren", "uitvoeren"),
                          ("Je stelt je resultaten voor aan de klas", "rapporteren"),
                          ("Je bedenkt dat je steekproef te klein was", "reflecteren")],
                  "Vul in.", WW),
             ]),
        dict(kop="Wat loopt er mis?", opdracht="Welke eis voldoet niet? Schrijf: open, objectief, enkelvoudig of onderzoekbaar. Herschrijf daarna de vraag.",
             oefeningen=[
                 ("open", "Zijn de huurprijzen in Hasselt gestegen?", "Niet open. Beter: Hoe evolueerden de huurprijzen in Hasselt sinds 2020?", 2),
                 ("open", "Waarom zijn supermarkten veel te duur?", "Niet objectief. Beter: Hoe evolueerden de prijzen in Belgische supermarkten tegenover die in Nederland?", 2),
                 ("open", "Hoeveel verdienen jongeren met een bijbaan en waarom werken ze?", "Niet enkelvoudig. Beter: twee aparte vragen, bv. Hoeveel verdienen jongeren met een bijbaan per maand?", 2),
                 ("open", "Hoe rijk zou België zijn zonder de Eerste Wereldoorlog?", "Niet onderzoekbaar. Beter: Hoe groeide het Belgische bbp tussen 1920 en 1940?", 2),
             ]),
        dict(kop="Welke methode?", opdracht="Schrijf: deskresearch, enquête, interview, observatie of experiment.",
             oefeningen=[
                 ("rij", [("Je zoekt de werkloosheidscijfers op bij Statbel", "deskresearch"),
                          ("Je vraagt 200 leerlingen hoeveel ze per week online uitgeven", "enquête"),
                          ("Je praat een uur met een winkeluitbater over waarom hij stopt", "interview"),
                          ("Je telt hoeveel mensen met cash betalen aan een kassa", "observatie"),
                          ("Een café verlaagt de prijs van koffie op maandag en vergelijkt met dinsdag", "experiment")],
                  "Vul in.", WW),
             ]),
        dict(kop="Steekproef en variabelen", opdracht="Je onderzoekt of jongeren in Limburg meer sparen als ze meer zakgeld krijgen.",
             oefeningen=[
                 ("kort", "Wat is de populatie?", "alle jongeren in Limburg", WL),
                 ("kort", "Wat is de onafhankelijke variabele?", "het zakgeld", WW),
                 ("kort", "Wat is de afhankelijke variabele?", "het gespaarde bedrag", WW),
                 ("open", "Je bevraagt enkel jongeren uit je eigen sportclub. Wat is het probleem?", "De steekproef is niet representatief: ze is geen goede afspiegeling van alle Limburgse jongeren.", 2),
                 ("open", "Je ziet: wie meer zakgeld krijgt, spaart meer. Bewijst dat dat meer zakgeld de oorzaak is? Leg uit.",
                  "Nee. Samen stijgen is geen bewijs van oorzaak; er kan een andere verklaring zijn, zoals ouders die zelf veel sparen.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan.",
             oefeningen=[
                 ("waar", "Bij een observatie stel je de deelnemers vragen.", False),
                 ("waar", "In het besluit horen ook de beperkingen van het onderzoek.", True),
                 ("waar", "Literatuuronderzoek is een vorm van fieldresearch.", False),
                 ("waar", "Kwalitatief en kwantitatief onderzoek kan je combineren.", True),
             ]),
    ])

# -*- coding: utf-8 -*-
"""De afdrukbare oefenbundels bij economie 🚀 Boost doorstroom.

Eén bundel per thema, niet per deel: deel 1 en deel 2 behandelen dezelfde stof
met andere vragen, dus gaat dezelfde pdf bij allebei.

De oefeningen zijn met opzet ándere opgaven dan die van het hoofdstuk op het
scherm: andere cijfers om mee te rekenen, andere gevallen om in te delen, en
opdrachten die je enkel op papier kan maken — een tabel aanvullen, een schema
invullen, een berekening in stappen opschrijven. Wie hier iets bijschrijft,
legt het eerst naast `../../boost-doorstroom/economie.json` en naast
`maak_economie_boost.py`.

De sleutels dragen het voorvoegsel "oefenbundel-" en het achtervoegsel
"-boost-doorstroom", zoals bij de andere Boost-vakken.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, oefenbundel, svg

VAK = "Economie"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"

W = "110px"
WW = "170px"
WL = "250px"

ONDER = "{aantal} oefeningen op papier, met een antwoordblad achteraan."
HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen en opnieuw proberen.",
    "Bij een berekening: schrijf de tussenstap op, niet alleen het eindbedrag.",
    "Bij een bedrag: zet er euro bij, en bij een groei een procentteken.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]

OEFENBUNDELS = {}

def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BOOST)
    b.setdefault("onder", ONDER)
    b.setdefault("hoe", HOE)
    OEFENBUNDELS["oefenbundel-" + slug + "-boost-doorstroom"] = b


# ============================================================ 1
zet("de-economische-kringloop", titel="De economische kringloop",
    reeksen=[
        dict(kop="Wie is wie?", opdracht="Schrijf bij elk geval de actor: gezin, bedrijf of overheid.",
             oefeningen=[
                 ("rij", [("Een loodgieter met twee werknemers", "bedrijf"),
                          ("Een gepensioneerde met een uitkering", "gezin"),
                          ("De dienst Openbare Werken van een stad", "overheid"),
                          ("Een zelfstandige fotograaf zonder personeel", "gezin"),
                          ("Een supermarktketen", "bedrijf")],
                  "Vul in.", WW),
             ]),
        dict(kop="Geld of reëel?", opdracht="Zet bij elke pijl of het een geldstroom of een reële stroom is.",
             oefeningen=[
                 ("rij", [("Het loon van een verpleegkundige", "geldstroom"),
                          ("De uren die zij werkt", "reële stroom"),
                          ("Een pakje koffie in de winkel", "reële stroom"),
                          ("De btw die de winkel doorstort", "geldstroom"),
                          ("De knipbeurt bij de kapper", "reële stroom")],
                  "Vul in.", WW),
             ]),
        dict(kop="Vergoedingen", opdracht="Welke vergoeding hoort bij welke productiefactor?",
             oefeningen=[
                 ("tabel", ["productiefactor", "vergoeding"],
                  [["arbeid", None], ["kapitaal", None], ["natuur", None], ["ondernemerschap", None]],
                  "arbeid: loon · kapitaal: intrest · natuur: pacht · ondernemerschap: winst"),
             ]),
        dict(kop="Lek of injectie?", opdracht="Duid aan of het geld uit de binnenlandse kringloop weggaat of erin komt.",
             oefeningen=[
                 ("rij", [("Een gezin spaart 200 euro", "lek"),
                          ("De overheid bouwt een brug", "injectie"),
                          ("Een bedrijf voert wijn in uit Italië", "lek"),
                          ("Een bedrijf verkoopt machines aan Canada", "injectie"),
                          ("Een gezin betaalt personenbelasting", "lek"),
                          ("Een fabriek koopt een nieuwe robot", "injectie")],
                  "Vul in.", W),
             ]),
        dict(kop="Rekenen", opdracht="Schrijf de berekening op.",
             oefeningen=[
                 ("open", "Een gezin krijgt 3 200 euro loon, betaalt 850 euro belasting en spaart 450 euro. Hoeveel blijft er over om te besteden?",
                  "3 200 − 850 − 450 = 1 900 euro", 2),
                 ("open", "Leg in twee zinnen uit waarom de uitgave van de ene actor het inkomen van een andere is.",
                  "Wat de ene betaalt, ontvangt de andere. Geeft het gezin minder uit, dan daalt de omzet van het bedrijf en dus ook het loon dat het kan betalen.", 3),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan en verbeter wat fout is.",
             oefeningen=[
                 ("waar", "In de kringloop zijn de gezinnen alleen verbruikers.", False),
                 ("waar", "Invoer is een lek uit de binnenlandse kringloop.", True),
                 ("waar", "Een werkloosheidsuitkering loopt van de overheid naar de gezinnen.", True),
                 ("waar", "Het buitenland staat in het eenvoudige binnenlandse schema.", False),
             ]),
    ])

# ============================================================ 2
zet("productie-toegevoegde-waarde-en-het-bbp",
    titel="Productie, toegevoegde waarde en het bbp",
    reeksen=[
        dict(kop="Toegevoegde waarde", opdracht="Bereken telkens de toegevoegde waarde.",
             oefeningen=[
                 ("kort", "Omzet 2 400 euro, aankopen bij andere bedrijven 900 euro", "1 500 euro", W),
                 ("kort", "Omzet 18 000 euro, aankopen 7 500 euro, lonen 6 000 euro", "10 500 euro", W),
                 ("kort", "Een schrijnwerker koopt 650 euro hout en verkoopt een kast voor 1 900 euro", "1 250 euro", W),
             ]),
        dict(kop="Een bedrijfskolom", opdracht="De boer verkoopt melk voor 300, de zuivelfabriek kaas voor 700, de winkel verkoopt voor 1 000.",
             oefeningen=[
                 ("tabel", ["schakel", "toegevoegde waarde"],
                  [["boer", None], ["zuivelfabriek", None], ["winkel", None], ["samen", None]],
                  "boer 300 · zuivelfabriek 400 · winkel 300 · samen 1 000, gelijk aan de waarde van het eindproduct"),
                 ("open", "Waarom tel je de toegevoegde waarden op en niet de omzetten?",
                  "Anders tel je de melk drie keer mee: ze zit al in de prijs van de kaas en van wat de winkel verkoopt.", 2),
             ]),
        dict(kop="Telt het mee in het bbp?", opdracht="Schrijf ja of nee.",
             oefeningen=[
                 ("rij", [("Een kapper knipt een klant", "ja"),
                          ("Je kookt thuis voor je gezin", "nee"),
                          ("Een Franse fabriek in Luik maakt staal", "ja"),
                          ("Iemand verkoopt zijn oude fiets", "nee"),
                          ("Een aannemer bouwt een school", "ja"),
                          ("Een klusjesman werkt in het zwart", "nee")],
                  "Vul in.", W),
             ]),
        dict(kop="Nominaal en reëel", opdracht="Reken en schrijf de stap op.",
             oefeningen=[
                 ("kort", "Nominaal bbp +6 %, prijzen +2 %. Reële groei?", "ongeveer +4 %", W),
                 ("kort", "Nominaal bbp +1 %, prijzen +3 %. Reële groei?", "ongeveer −2 %", W),
                 ("kort", "Bbp van 250 naar 265 miljard. Groei?", "6 %", W),
                 ("kort", "Bbp 720 miljard euro, 9 miljoen inwoners. Bbp per capita?", "80 000 euro", W),
             ]),
        dict(kop="Uitleggen", opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom staat het woord bruto in bruto binnenlands product?",
                  "Omdat de afschrijvingen er nog niet af zijn: de slijtage van machines en gebouwen is niet in mindering gebracht.", 2),
                 ("open", "Het bbp stijgt met 1 %, de bevolking met 2 %. Wat gebeurt er met het bbp per capita?",
                  "Dat daalt: de koek groeit trager dan het aantal mensen dat ze deelt.", 2),
                 ("open", "Noem twee zaken die het bbp niet meet.",
                  "Bijvoorbeeld: de verdeling van de welvaart, het milieu, onbetaald werk en vrije tijd.", 2),
             ]),
    ])

# ============================================================ 3
zet("economische-groei-welvaart-en-welzijn",
    titel="Economische groei, welvaart en welzijn",
    reeksen=[
        dict(kop="Welke oorzaak?", opdracht="Schrijf welke oorzaak van groei hier speelt.",
             oefeningen=[
                 ("rij", [("Een school start een opleiding lassen", "menselijk kapitaal"),
                          ("Een bedrijf koopt een snellere machine", "kapitaalvorming"),
                          ("Een bakker bakt met dezelfde ploeg meer brood", "arbeidsproductiviteit"),
                          ("Er komen meer jonge gezinnen in het land wonen", "bevolkingsgroei"),
                          ("Een labo vindt een goedkoper procedé", "technologische ontwikkeling")],
                  "Vul in.", WL),
             ]),
        dict(kop="Rekenen", opdracht="Bereken de arbeidsproductiviteit.",
             oefeningen=[
                 ("kort", "5 werknemers maken samen 900 stuks per dag", "180 stuks per werknemer", W),
                 ("kort", "Daarna maken dezelfde 5 werknemers 1 050 stuks", "210 stuks per werknemer", W),
                 ("kort", "Met hoeveel procent is de productiviteit gestegen?", "ongeveer 16,7 %", W),
             ]),
        dict(kop="Welvaart of welzijn?", opdracht="Zet achter elk gegeven of het vooral de welvaart of vooral het welzijn raakt.",
             oefeningen=[
                 ("rij", [("Een hoger loon", "welvaart"),
                          ("Properdere lucht in de stad", "welzijn"),
                          ("Een tweede auto", "welvaart"),
                          ("Meer vrije tijd", "welzijn"),
                          ("Een veiliger buurt", "welzijn")],
                  "Vul in.", WW),
             ]),
        dict(kop="Beoordelen", opdracht="Antwoord in twee of drie zinnen, met een begrip erin.",
             oefeningen=[
                 ("open", "Het bbp van een land stijgt met 4 %, maar de rivieren worden vuiler. Hoe beoordeel je dat?",
                  "De welvaart stijgt, maar het welzijn gaat erop achteruit. Het bbp meet de vervuiling niet mee, dus zegt dit cijfer alleen niet of de mensen er beter van worden.", 3),
                 ("open", "Waarom kan groei niet eindeloos uit bevolkingsgroei alleen komen?",
                  "Als het aantal mensen even snel groeit als de productie, blijft het bbp per inwoner gelijk. Er komt dan wel meer bij, maar niemand gaat erop vooruit.", 3),
                 ("open", "Wat is duurzame groei?",
                  "Groei die rekening houdt met de generaties na ons: ze gebruikt grondstoffen en milieu niet sneller op dan die zich herstellen.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan en verbeter wat fout is.",
             oefeningen=[
                 ("waar", "Welvaart en welzijn betekenen hetzelfde.", False),
                 ("waar", "Het bbp per capita zegt niets over de verdeling.", True),
                 ("waar", "Een hoger bbp betekent dat iedereen erop vooruitgaat.", False),
                 ("waar", "De primaire inkomensverdeling bestaat uit loon, intrest, pacht en winst.", True),
             ]),
    ])


# ============================================================ 4
zet("behoeften-schaarste-en-soorten-goederen",
    titel="Behoeften, schaarste en soorten goederen",
    reeksen=[
        dict(kop="Primair, secundair of tertiair?", opdracht="Schrijf welke soort behoefte het is.",
             oefeningen=[
                 ("rij", [("Een bord soep", "primair"), ("Een dak boven je hoofd", "primair"),
                          ("Een smartphone", "secundair"), ("Een privéjet", "tertiair"),
                          ("Een fiets om naar school te gaan", "secundair")],
                  "Vul in.", W),
             ]),
        dict(kop="Indelen", opdracht="Vul de tabel aan met ja of nee.",
             oefeningen=[
                 ("tabel", ["goed", "tastbaar?", "verbruiksgoed?", "investeringsgoed?"],
                  [["een brood", None, None, None],
                   ["een oven in een bakkerij", None, None, None],
                   ["een kappersbeurt", None, None, None],
                   ["een laptop van een gezin", None, None, None]],
                  "brood: ja, ja, nee · oven: ja, nee, ja · kappersbeurt: nee, ja, nee · laptop: ja, nee, nee"),
             ]),
        dict(kop="Alternatieve kost", opdracht="Schrijf wat er opgegeven wordt.",
             oefeningen=[
                 ("open", "Een gemeente bouwt met haar budget een zwembad in plaats van een bibliotheek. Wat is de alternatieve kost?",
                  "De bibliotheek die er niet komt: de waarde van het beste alternatief dat opgegeven wordt.", 2),
                 ("open", "Jij kiest ervoor om een zaterdag te gaan werken in plaats van te gaan zwemmen met vrienden. Wat is je alternatieve kost?",
                  "De namiddag zwemmen met je vrienden. Je loon is de opbrengst, het gemiste plezier de kost.", 2),
             ]),
        dict(kop="Individueel of collectief?", opdracht="Schrijf het antwoord en zeg bij een collectief goed waarom.",
             oefeningen=[
                 ("rij", [("Straatverlichting", "collectief"), ("Een paar schoenen", "individueel"),
                          ("Een dijk aan de kust", "collectief"), ("Een treinabonnement", "individueel"),
                          ("De politie", "collectief")],
                  "Vul in.", W),
                 ("open", "Waarom zorgt de overheid meestal voor collectieve goederen?",
                  "Omdat je er niemand van kan uitsluiten. Niemand zou ervoor willen betalen als hij er toch gebruik van kan maken, dus zou niemand ze aanbieden.", 3),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan en verbeter wat fout is.",
             oefeningen=[
                 ("waar", "Drinkbaar leidingwater is een vrij goed.", False),
                 ("waar", "Schaarste verdwijnt in een rijk land.", False),
                 ("waar", "Hetzelfde goed kan voor de ene een investeringsgoed zijn en voor de andere een consumptiegoed.", True),
                 ("waar", "Intermediaire goederen tellen apart mee in het bbp.", False),
             ]),
    ])

# ============================================================ 5
zet("nut-preferentie-en-de-indifferentiecurve",
    titel="Nut, preferentie en de indifferentiecurve",
    reeksen=[
        dict(kop="Totaal nut en grensnut", opdracht="Vul de tabel aan. Het grensnut staat gegeven.",
             oefeningen=[
                 ("tabel", ["stuk", "grensnut", "totaal nut"],
                  [["1", "9", None], ["2", "6", None], ["3", "4", None],
                   ["4", "1", None], ["5", "−3", None]],
                  "totaal nut: 9 · 15 · 19 · 20 · 17"),
                 ("kort", "Bij welk stuk is het totale nut het grootst?", "bij het vierde stuk", W),
                 ("open", "Wat zegt het grensnut van −3 bij het vijfde stuk?",
                  "Dat het vijfde stuk het totale nut verlaagt. De consument stopt beter na het vierde.", 2),
             ]),
        dict(kop="Begrippen", opdracht="Schrijf het juiste woord.",
             oefeningen=[
                 ("rij", [("Twee combinaties even goed vinden", "indifferentie"),
                          ("De ene combinatie verkiezen", "preferentie"),
                          ("Het nut van de laatste eenheid", "marginaal nut of grensnut"),
                          ("Alle curven van één consument samen", "indifferentiemap"),
                          ("De verhouding waarin je wil ruilen", "marginale substitutievoet")],
                  "Vul in.", WL),
             ]),
        dict(kop="De curve lezen", opdracht="Antwoord in één of twee zinnen.",
             oefeningen=[
                 ("open", "Waarom daalt een indifferentiecurve?",
                  "Krijg je van het ene goed meer, dan moet je van het andere iets afgeven om even goed te blijven zitten.", 2),
                 ("open", "Waarom is ze bol naar de oorsprong en geen rechte?",
                  "Door het afnemende grensnut: wie al veel van een goed heeft, geeft er makkelijker van af. De ruilverhouding is dus niet overal gelijk.", 3),
                 ("open", "Waarom kunnen twee curven van dezelfde consument elkaar niet snijden?",
                  "In het snijpunt zou dezelfde combinatie twee verschillende nutsniveaus geven, en dat kan niet.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan en verbeter wat fout is.",
             oefeningen=[
                 ("waar", "Een dalend grensnut betekent dat het totale nut daalt.", False),
                 ("waar", "De curve die het verst van de oorsprong ligt, geeft het meeste nut.", True),
                 ("waar", "Nut kan je voor iedereen in dezelfde euro's uitdrukken.", False),
                 ("waar", "Uit een indifferentiemap alleen weet je wat iemand zal kopen.", False),
             ]),
    ])

# ============================================================ 6
zet("de-budgetlijn-en-de-optimale-goederencombinatie",
    titel="De budgetlijn en de optimale goederencombinatie",
    reeksen=[
        dict(kop="De budgetvergelijking", opdracht="Een consument heeft 90 euro. Een boek kost 15 euro, een ticket 9 euro.",
             oefeningen=[
                 ("kort", "Schrijf de budgetvergelijking", "15b + 9t = 90", WW),
                 ("kort", "Hoeveel boeken als hij niets anders koopt?", "6 boeken", W),
                 ("kort", "Hij koopt 4 boeken. Hoeveel tickets nog?", "30 euro over, dus 3 tickets", WW),
                 ("kort", "Hoeveel tickets als hij geen boeken koopt?", "10 tickets", W),
             ]),
        dict(kop="Waar snijdt de lijn?", opdracht="Bereken de snijpunten met de assen.",
             oefeningen=[
                 ("tabel", ["budget", "prijs x", "prijs y", "snijpunt x-as", "snijpunt y-as"],
                  [["200 euro", "10 euro", "25 euro", None, None],
                   ["150 euro", "5 euro", "15 euro", None, None],
                   ["120 euro", "8 euro", "6 euro", None, None]],
                  "20 en 8 · 30 en 10 · 15 en 20"),
             ]),
        dict(kop="Wat gebeurt er met de lijn?", opdracht="Schrijf: schuift parallel naar buiten, naar binnen, kantelt, of verandert niet.",
             oefeningen=[
                 ("rij", [("Het budget stijgt, de prijzen blijven gelijk", "schuift parallel naar buiten"),
                          ("Alleen de prijs van x daalt", "kantelt"),
                          ("Budget en prijzen stijgen alle drie met 10 %", "verandert niet"),
                          ("Het budget daalt, de prijzen blijven gelijk", "schuift parallel naar binnen"),
                          ("Alleen de prijs van y stijgt", "kantelt")],
                  "Vul in.", WL),
             ]),
        dict(kop="Het optimum", opdracht="Antwoord in volle zinnen.",
             oefeningen=[
                 ("open", "Waarom ligt het optimum altijd óp de budgetlijn en niet eronder?",
                  "Onder de lijn houdt de consument geld over. Daarmee kan hij nog iets kopen en dus een hogere indifferentiecurve bereiken.", 3),
                 ("open", "Waarom raakt de budgetlijn de curve in het optimum in plaats van ze te snijden?",
                  "Bij een snijpunt ligt er nog een stuk budgetlijn aan de andere kant van de curve. Er is dan een hogere curve haalbaar, dus is het snijpunt niet het beste punt.", 3),
                 ("kort", "Iemand besteedt 180 euro, x kost 15 euro en y 10 euro. In zijn optimum koopt hij 8 stuks x. Hoeveel y?",
                  "120 euro aan x, 60 euro over, dus 6 stuks y", WL),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan en verbeter wat fout is.",
             oefeningen=[
                 ("waar", "Alle punten op de budgetlijn geven evenveel nut.", False),
                 ("waar", "Een prijswijziging van één goed verandert de helling.", True),
                 ("waar", "Twee consumenten met hetzelfde budget kiezen altijd dezelfde combinatie.", False),
                 ("waar", "Een punt boven de budgetlijn kan de consument niet betalen.", True),
             ]),
    ])


# ============================================================ 7
zet("productiefactoren-productiefunctie-en-meeropbrengsten",
    titel="Productiefactoren, productiefunctie en meeropbrengsten",
    reeksen=[
        dict(kop="Welke productiefactor?", opdracht="Schrijf de productiefactor en de vergoeding erbij.",
             oefeningen=[
                 ("tabel", ["voorbeeld", "productiefactor", "vergoeding"],
                  [["de uren van een verkoopster", None, None],
                   ["de heftruck in het magazijn", None, None],
                   ["de akker die een boer huurt", None, None],
                   ["de zaakvoerder die het risico draagt", None, None],
                   ["het ijzererts in de grond", None, None]],
                  "arbeid/loon · kapitaal/intrest · natuur/pacht · ondernemerschap/winst · natuur/pacht"),
             ]),
        dict(kop="TP, MP en gemiddelde productie", opdracht="Vul de tabel aan.",
             oefeningen=[
                 ("tabel", ["werknemers", "TP", "MP", "gemiddelde productie"],
                  [["1", "12", None, None], ["2", "30", None, None], ["3", "54", None, None],
                   ["4", "68", None, None], ["5", "75", None, None], ["6", "72", None, None]],
                  "MP: 12, 18, 24, 14, 7, −3 · gemiddelde: 12 · 15 · 18 · 17 · 15 · 12"),
                 ("kort", "Bij welke werknemer is MP het grootst?", "bij de derde", W),
                 ("kort", "Bij welke werknemer bereikt TP zijn maximum?", "bij de vijfde", W),
                 ("open", "Wat gebeurt er bij de zesde werknemer en hoe heet dat?",
                  "MP wordt negatief, dus TP daalt. Dat is het afnemende deel van de wet van de toe- en afnemende meeropbrengsten.", 3),
             ]),
        dict(kop="Korte of lange termijn?", opdracht="Schrijf kort of lang.",
             oefeningen=[
                 ("rij", [("Een extra chauffeur aanwerven", "kort"),
                          ("Een tweede fabriekshal bouwen", "lang"),
                          ("Meer grondstoffen bestellen", "kort"),
                          ("Alle machines vervangen", "lang")],
                  "Vul in.", W),
             ]),
        dict(kop="Uitleggen", opdracht="Antwoord in twee of drie zinnen.",
             oefeningen=[
                 ("open", "Waarom stijgt MP in het begin?",
                  "Omdat mensen kunnen samenwerken en zich specialiseren. Twee bakkers samen doen meer dan twee keer één.", 2),
                 ("open", "Waarom daalt MP vanaf een bepaald punt?",
                  "Omdat de vaste factor te klein wordt. Er is maar één oven, dus staat de zevende bakker te wachten.", 2),
                 ("open", "Waarom is geen geld een productiefactor?",
                  "Met geld koop je productiefactoren, maar geld zelf maakt niets. Het is een ruilmiddel, geen middel om mee te produceren.", 2),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan en verbeter wat fout is.",
             oefeningen=[
                 ("waar", "Een dalende MP betekent dat het bedrijf minder produceert.", False),
                 ("waar", "Op lange termijn kan een bedrijf al zijn productiefactoren aanpassen.", True),
                 ("waar", "Machines horen bij de productiefactor natuur.", False),
                 ("waar", "De wet van de toe- en afnemende meeropbrengsten geldt alleen op korte termijn.", True),
             ]),
    ])

# ============================================================ 8
zet("de-kosten-en-de-opbrengstencurven",
    titel="De kosten- en de opbrengstencurven",
    reeksen=[
        dict(kop="Constant of variabel?", opdracht="Schrijf C of V.",
             oefeningen=[
                 ("rij", [("De huur van de werkplaats", "C"), ("Het garen voor de kleren", "V"),
                          ("De verzekering van het gebouw", "C"), ("De stroom voor de machines", "V"),
                          ("De afschrijving van de bestelwagen", "C"), ("De verpakking per stuk", "V")],
                  "Vul in.", W),
             ]),
        dict(kop="Rekenen met kosten", opdracht="Een bedrijf heeft 3 600 euro constante kosten en 4 euro variabele kost per stuk.",
             oefeningen=[
                 ("tabel", ["aantal stuks", "TCK", "TVK", "TK", "GK"],
                  [["300", None, None, None, None],
                   ["600", None, None, None, None],
                   ["1 200", None, None, None, None]],
                  "300: 3 600 · 1 200 · 4 800 · 16 euro — 600: 3 600 · 2 400 · 6 000 · 10 euro — 1 200: 3 600 · 4 800 · 8 400 · 7 euro"),
                 ("open", "Waarom daalt de gemiddelde kost als de productie stijgt?",
                  "De constante kosten worden over meer stuks verdeeld, dus daalt de gemiddelde constante kost.", 2),
             ]),
        dict(kop="Marginale kost", opdracht="Bereken MK.",
             oefeningen=[
                 ("kort", "200 stuks kosten 2 500 euro, 201 stuks kosten 2 512 euro", "12 euro", W),
                 ("kort", "50 stuks kosten 980 euro, 51 stuks kosten 987 euro", "7 euro", W),
                 ("kort", "Ligt MK onder GK, wat doet GK dan?", "GK daalt", W),
             ]),
        dict(kop="Opbrengsten bij volkomen concurrentie", opdracht="De marktprijs is 8 euro.",
             oefeningen=[
                 ("tabel", ["aantal stuks", "TO", "GO", "MO"],
                  [["100", None, None, None], ["250", None, None, None], ["400", None, None, None]],
                  "800 · 8 · 8 — 2 000 · 8 · 8 — 3 200 · 8 · 8"),
                 ("open", "Waarom zijn GO en MO hier allebei gelijk aan de prijs?",
                  "Het bedrijf is te klein om de prijs te beïnvloeden. Elk stuk brengt dus hetzelfde op, ook het laatste.", 2),
             ]),
        dict(kop="Winst", opdracht="Bereken de winst of het verlies.",
             oefeningen=[
                 ("kort", "TO 12 000 euro, TK 11 400 euro", "600 euro winst", W),
                 ("kort", "TO 9 500 euro, TK 10 200 euro", "700 euro verlies", W),
                 ("open", "300 stuks aan 25 euro, 4 000 euro constante kosten en 14 euro variabele kost per stuk. Winst of verlies?",
                  "TO = 7 500 euro, TK = 4 000 + 4 200 = 8 200 euro, dus 700 euro verlies.", 3),
             ]),
    ])

# ============================================================ 9
zet("de-optimale-productiegrootte-en-winstmaximalisatie",
    titel="De optimale productiegrootte en winstmaximalisatie",
    reeksen=[
        dict(kop="Het optimum zoeken", opdracht="De marktprijs is 12 euro. Hieronder staat de marginale kost.",
             oefeningen=[
                 ("tabel", ["aantal stuks", "MK", "meer of minder produceren?"],
                  [["6", "7 euro", None], ["7", "9 euro", None], ["8", "12 euro", None],
                   ["9", "15 euro", None]],
                  "6: meer · 7: meer · 8: dit is het optimum, MK = MO · 9: minder"),
                 ("kort", "Wat is de optimale hoeveelheid?", "8 stuks", W),
             ]),
        dict(kop="Break-even", opdracht="Bereken de kritische hoeveelheid.",
             oefeningen=[
                 ("kort", "Constante kosten 6 000 euro, prijs 25 euro, variabele kost 15 euro", "600 stuks", WW),
                 ("kort", "Constante kosten 2 700 euro, prijs 18 euro, variabele kost 9 euro", "300 stuks", WW),
                 ("kort", "Hoe noem je het verschil tussen prijs en variabele kost per stuk?", "de marge", WW),
             ]),
        dict(kop="Winst aflezen", opdracht="Bereken de totale winst.",
             oefeningen=[
                 ("kort", "1 500 stuks, prijs 20 euro, GK 17 euro", "4 500 euro", W),
                 ("kort", "800 stuks, prijs 11 euro, GK 12 euro", "800 euro verlies", W),
                 ("kort", "900 stuks, prijs 7 euro, totale kosten 5 400 euro", "900 euro winst", W),
             ]),
        dict(kop="Doorgaan of sluiten?", opdracht="Schrijf doorgaan of sluiten, en zeg waarom in één zin.",
             oefeningen=[
                 ("open", "Prijs 9 euro, GVK 7 euro, GK 11 euro. Korte termijn?",
                  "Doorgaan: de prijs ligt boven de gemiddelde variabele kost, dus dekt elke verkoop haar eigen kost en nog een stuk van de constante kosten.", 3),
                 ("open", "Prijs 5 euro, GVK 6 euro, GK 9 euro. Korte termijn?",
                  "Sluiten: elk stuk brengt minder op dan het aan grondstof en energie kost, dus doorgaan vergroot het verlies.", 3),
                 ("open", "Prijs 10 euro, GVK 8 euro, GK 12 euro. Lange termijn?",
                  "Stoppen: op lange termijn moeten ook de constante kosten gedekt zijn, en de prijs blijft onder de gemiddelde kost.", 3),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan en verbeter wat fout is.",
             oefeningen=[
                 ("waar", "MK = MO betekent dat het bedrijf winst maakt.", False),
                 ("waar", "De stijgende tak van de MK-curve is de aanbodcurve van het bedrijf.", True),
                 ("waar", "In het optimum is de totale opbrengst het hoogst.", False),
                 ("waar", "Een bedrijf dat zijn omzet verdubbelt, verdubbelt zijn winst.", False),
             ]),
    ])


# ============================================================ 10
zet("de-markt-met-volkomen-concurrentie-en-de-overheid",
    titel="De markt met volkomen concurrentie en de overheid",
    reeksen=[
        dict(kop="Rekenen met functies", opdracht="De vraag is Qv = 180 − 3P, het aanbod Qa = 30 + 2P.",
             oefeningen=[
                 ("kort", "Wat is de evenwichtsprijs?", "P = 30", W),
                 ("kort", "Wat is de evenwichtshoeveelheid?", "90", W),
                 ("kort", "Hoeveel wordt er gevraagd bij een prijs van 40?", "60", W),
                 ("kort", "Hoeveel wordt er aangeboden bij een prijs van 40?", "110", W),
                 ("kort", "Overschot of tekort bij 40, en hoe groot?", "een overschot van 50", WW),
             ]),
        dict(kop="Langs de curve of de curve zelf?", opdracht="Schrijf: beweging langs de curve, vraagcurve verschuift, of aanbodcurve verschuift.",
             oefeningen=[
                 ("rij", [("De prijs van koffie stijgt", "beweging langs de curve"),
                          ("Het inkomen van de gezinnen stijgt", "vraagcurve verschuift"),
                          ("De koffiebonen worden duurder", "aanbodcurve verschuift"),
                          ("Koffie komt plots in de mode", "vraagcurve verschuift"),
                          ("Er komen nieuwe branderijen bij", "aanbodcurve verschuift")],
                  "Vul in.", WL),
             ]),
        dict(kop="Wat gebeurt er met prijs en hoeveelheid?", opdracht="Schrijf voor beide: stijgt, daalt of blijft gelijk.",
             oefeningen=[
                 ("tabel", ["gebeurtenis", "prijs", "hoeveelheid"],
                  [["de vraag stijgt", None, None], ["de vraag daalt", None, None],
                   ["het aanbod stijgt", None, None], ["het aanbod daalt", None, None]],
                  "vraag stijgt: prijs ↑ hoeveelheid ↑ · vraag daalt: ↓ ↓ · aanbod stijgt: prijs ↓ hoeveelheid ↑ · aanbod daalt: prijs ↑ hoeveelheid ↓"),
             ]),
        dict(kop="Maximum- en minimumprijzen", opdracht="Het evenwicht ligt bij 12 euro.",
             oefeningen=[
                 ("rij", [("Een maximumprijs van 9 euro", "tekort"),
                          ("Een maximumprijs van 15 euro", "verandert niets"),
                          ("Een minimumprijs van 15 euro", "overschot"),
                          ("Een minimumprijs van 9 euro", "verandert niets")],
                  "Vul in.", WW),
                 ("open", "Noem twee gevolgen van een tekort door een maximumprijs.",
                  "Bijvoorbeeld wachtlijsten, rantsoenering of een zwarte markt waar toch meer betaald wordt.", 2),
                 ("open", "Waarom legt een overheid soms toch een maximumprijs op?",
                  "Om een goed betaalbaar te houden voor wie het nodig heeft, bijvoorbeeld bij huur, energie of geneesmiddelen.", 2),
             ]),
        dict(kop="Volkomen concurrentie", opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Noem de vier kenmerken.",
                  "Veel kleine aanbieders en vragers, een homogeen product, volledige informatie, en vrije toe- en uittreding.", 3),
                 ("open", "Waarom is een aanbieder daar een prijsnemer?",
                  "Het product is overal hetzelfde en hij is te klein om de prijs te beïnvloeden. Vraagt hij meer, dan koopt niemand bij hem.", 3),
             ]),
    ])

# ============================================================ 11
zet("de-arbeidsmarkt-en-de-collectieve-afspraken",
    titel="De arbeidsmarkt en de collectieve afspraken",
    reeksen=[
        dict(kop="Vraag of aanbod?", opdracht="Schrijf wie vraagt en wie aanbiedt.",
             oefeningen=[
                 ("rij", [("Een ziekenhuis zoekt verpleegkundigen", "vraag naar arbeid"),
                          ("Een pas afgestudeerde solliciteert", "aanbod van arbeid"),
                          ("Een fabriek neemt twintig mensen aan", "vraag naar arbeid"),
                          ("Een gepensioneerde gaat weer deeltijds werken", "aanbod van arbeid")],
                  "Vul in.", WL),
             ]),
        dict(kop="Rekenen", opdracht="De vraag is Qv = 900 − 15W, het aanbod Qa = 300 + 10W.",
             oefeningen=[
                 ("kort", "Wat is het evenwichtsloon?", "W = 24", W),
                 ("kort", "Hoeveel arbeid wordt er dan ingezet?", "540", W),
                 ("kort", "De overheid legt een minimumloon van 30 op. Hoeveel vraag is er dan?", "450", W),
                 ("kort", "Hoeveel aanbod is er bij 30?", "600", W),
                 ("kort", "Hoe groot is het overschot aan arbeid?", "150", W),
             ]),
        dict(kop="Wat verschuift er?", opdracht="Schrijf: vraag naar arbeid of aanbod van arbeid, en stijgt of daalt.",
             oefeningen=[
                 ("rij", [("De bevolking vergrijst sterk", "aanbod daalt"),
                          ("De verkoop in de sector trekt aan", "vraag stijgt"),
                          ("Er komen arbeidsmigranten bij", "aanbod stijgt"),
                          ("Machines nemen routinewerk over", "vraag daalt"),
                          ("De studieduur wordt langer", "aanbod daalt")],
                  "Vul in.", WL),
             ]),
        dict(kop="Begrippen", opdracht="Schrijf het juiste woord of de afkorting.",
             oefeningen=[
                 ("rij", [("Een akkoord over loon en voorwaarden in een sector", "cao"),
                          ("Een akkoord over alle sectoren heen", "ipa"),
                          ("De vakbonden en de werkgeversorganisaties", "de sociale partners"),
                          ("Een beroep met een blijvend tekort", "knelpuntberoep"),
                          ("De automatische aanpassing van de lonen aan de prijzen", "indexering")],
                  "Vul in.", WL),
             ]),
        dict(kop="Uitleggen", opdracht="Antwoord in twee of drie zinnen.",
             oefeningen=[
                 ("open", "Wat betekent het dat de vraag naar arbeid een afgeleide vraag is?",
                  "Een bedrijf vraagt arbeid niet voor zichzelf, maar omdat het goederen of diensten wil verkopen. Loopt die verkoop terug, dan daalt de vraag naar arbeid mee.", 3),
                 ("open", "Waarom onderhandelen werknemers samen in plaats van elk apart?",
                  "Eén werknemer staat zwak tegenover een werkgever. Met duizenden achter zich weegt een vakbond even zwaar.", 2),
                 ("open", "Waarom drukt indexering soms de vraag naar arbeid?",
                  "De loonkosten stijgen mee met de prijzen. Stijgt de productiviteit niet mee, dan wordt arbeid duurder en nemen bedrijven minder mensen aan.", 3),
             ]),
    ])

# ============================================================ 12
zet("internationale-handel-en-handelsbelemmeringen",
    titel="Internationale handel en handelsbelemmeringen",
    reeksen=[
        dict(kop="Hoe heet het?", opdracht="Schrijf: invoer, uitvoer, intracommunautaire verwerving of intracommunautaire levering.",
             oefeningen=[
                 ("rij", [("Een Belgische winkel koopt wijn in Frankrijk", "intracommunautaire verwerving"),
                          ("Een Belgisch bedrijf verkoopt staal aan Japan", "uitvoer"),
                          ("Een Belgische fabriek verkoopt aan een klant in Italië", "intracommunautaire levering"),
                          ("Een Belgische winkel koopt thee in India", "invoer")],
                  "Vul in.", WL),
             ]),
        dict(kop="Handelsbalans", opdracht="Bereken en zeg of het een overschot of een tekort is.",
             oefeningen=[
                 ("kort", "Uitvoer 410, invoer 380 miljard euro", "overschot van 30 miljard", WW),
                 ("kort", "Uitvoer 275, invoer 310 miljard euro", "tekort van 35 miljard", WW),
                 ("kort", "Uitvoer van 150 naar 165 miljard. Groei?", "10 %", W),
             ]),
        dict(kop="Welke belemmering?", opdracht="Schrijf: invoerquotum, importheffing, uitvoersubsidie of niet-tarifaire belemmering.",
             oefeningen=[
                 ("rij", [("Hoogstens 50 000 ton per jaar mag binnen", "invoerquotum"),
                          ("Een extra keuring aan de grens voor elk toestel", "niet-tarifaire belemmering"),
                          ("12 % belasting op elk ingevoerd stuk", "importheffing"),
                          ("De staat legt geld bij wie naar Azië verkoopt", "uitvoersubsidie"),
                          ("Een verplicht label in de landstaal", "niet-tarifaire belemmering")],
                  "Vul in.", WL),
             ]),
        dict(kop="Rekenen", opdracht="Bereken wat de koper betaalt.",
             oefeningen=[
                 ("kort", "Prijs 200 euro, importheffing 20 %", "240 euro", W),
                 ("kort", "Prijs 80 euro, importheffing 5 %", "84 euro", W),
                 ("kort", "Prijs 350 euro, importheffing 12 %", "392 euro", W),
             ]),
        dict(kop="Wie wint, wie verliest?", opdracht="Vul de tabel in met wint of verliest.",
             oefeningen=[
                 ("tabel", ["bij een importheffing", "wint of verliest?"],
                  [["de binnenlandse producent", None], ["de binnenlandse koper", None],
                   ["de overheid", None], ["de buitenlandse verkoper", None]],
                  "producent wint · koper verliest · overheid wint · buitenlandse verkoper verliest"),
                 ("open", "Wat doet een handelsakkoord met de prijs van ingevoerde goederen, en waarom?",
                  "De prijs daalt: zonder heffing schuift het aanbod naar beneden. De consument wint, de binnenlandse producent krijgt meer concurrentie.", 3),
             ]),
    ])


# ============================================================ 13
zet("ondernemingsvormen-en-aansprakelijkheid",
    titel="Ondernemingsvormen en aansprakelijkheid",
    reeksen=[
        dict(kop="De tabel invullen", opdracht="Vul aan voor elke vorm.",
             oefeningen=[
                 ("tabel", ["punt", "eenmanszaak", "bv", "nv"],
                  [["rechtspersoon?", None, None, None],
                   ["oprichtingsakte", None, None, None],
                   ["minimumkapitaal", None, None, None],
                   ["aansprakelijkheid", None, None, None],
                   ["aandelen", None, None, None],
                   ["belasting", None, None, None]],
                  "rechtspersoon: nee, ja, ja · akte: geen, notarieel, notarieel · kapitaal: geen, geen vast bedrag, 61 500 euro · "
                  "aansprakelijkheid: onbeperkt, beperkt, beperkt · aandelen: bestaan niet, besloten, vrij overdraagbaar · "
                  "belasting: personenbelasting, vennootschapsbelasting, vennootschapsbelasting"),
             ]),
        dict(kop="Welke vorm past?", opdracht="Schrijf eenmanszaak, bv of nv en zeg waarom in één zin.",
             oefeningen=[
                 ("open", "Een kapster start alleen, met weinig startgeld en zo weinig mogelijk papierwerk.",
                  "Een eenmanszaak: geen notaris en geen kapitaal nodig, al is ze dan wel onbeperkt aansprakelijk.", 2),
                 ("open", "Drie zussen starten samen en willen zelf bepalen wie er aandeelhouder kan worden.",
                  "Een bv: het besloten karakter maakt dat aandelen niet zonder toestemming van de anderen overgaan.", 2),
                 ("open", "Een bedrijf wil naar de beurs met duizenden aandeelhouders.",
                  "Een nv: de aandelen zijn vrij overdraagbaar, wat op de beurs nodig is.", 2),
             ]),
        dict(kop="Rekenen met aansprakelijkheid", opdracht="Schrijf wie wat betaalt.",
             oefeningen=[
                 ("open", "Een eenmanszaak heeft 70 000 euro schulden; in de zaak zit 25 000 euro. Wat gebeurt er met de rest?",
                  "De eigenaar staat met zijn privévermogen in voor de overige 45 000 euro: de aansprakelijkheid is onbeperkt.", 3),
                 ("open", "Een bv gaat failliet met 70 000 euro schulden; een aandeelhouder bracht 5 000 euro in. Wat verliest hij?",
                  "Hoogstens zijn inbreng van 5 000 euro. Zijn privévermogen blijft buiten schot.", 3),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan en verbeter wat fout is.",
             oefeningen=[
                 ("waar", "Een bv heeft minstens twee oprichters nodig.", False),
                 ("waar", "Een nv heeft 61 500 euro kapitaal nodig.", True),
                 ("waar", "Een eenmanszaak heeft een notariële akte nodig.", False),
                 ("waar", "Een vennootschap blijft bestaan als een oprichter overlijdt.", True),
             ]),
    ])

# ============================================================ 14
zet("de-balans-en-de-resultatenrekening",
    titel="De balans en de resultatenrekening",
    reeksen=[
        dict(kop="Waar op de balans?", opdracht="Schrijf: vaste activa, vlottende activa, eigen vermogen, schulden > 1 jaar of schulden ≤ 1 jaar.",
             oefeningen=[
                 ("rij", [("Een bestelwagen", "vaste activa"),
                          ("De voorraad in het magazijn", "vlottende activa"),
                          ("Een lening op vijftien jaar", "schulden > 1 jaar"),
                          ("Te betalen btw", "schulden ≤ 1 jaar"),
                          ("Het kapitaal", "eigen vermogen"),
                          ("Geld op de zichtrekening", "vlottende activa"),
                          ("Een softwarelicentie", "vaste activa"),
                          ("Een klant die nog moet betalen", "vlottende activa")],
                  "Vul in.", WL),
             ]),
        dict(kop="Rekenen met de balans", opdracht="Vul aan.",
             oefeningen=[
                 ("tabel", ["actief", "eigen vermogen", "schulden"],
                  [["320 000 euro", "140 000 euro", None],
                   ["95 000 euro", None, "60 000 euro"],
                   [None, "210 000 euro", "190 000 euro"]],
                  "180 000 euro · 35 000 euro · 400 000 euro"),
             ]),
        dict(kop="Bedrijfs- of financieel?", opdracht="Schrijf bij welk resultaat het hoort.",
             oefeningen=[
                 ("rij", [("De omzet", "bedrijfs"), ("De lonen", "bedrijfs"),
                          ("De intrest op een lening", "financieel"),
                          ("De afschrijvingen", "bedrijfs"),
                          ("Ontvangen intrest op een belegging", "financieel")],
                  "Vul in.", WW),
             ]),
        dict(kop="De resultatenrekening doorrekenen", opdracht="Een bedrijf heeft 840 000 euro bedrijfsopbrengsten en 760 000 euro bedrijfskosten. De financiële kosten zijn 25 000 euro, de financiële opbrengsten 5 000 euro. De belasting is 25 %.",
             oefeningen=[
                 ("tabel", ["stap", "bedrag"],
                  [["bedrijfsresultaat", None], ["financieel resultaat", None],
                   ["resultaat voor belastingen", None], ["belastingen", None],
                   ["resultaat van het boekjaar", None]],
                  "80 000 · −20 000 · 60 000 · 15 000 · 45 000 euro"),
             ]),
        dict(kop="Uitleggen", opdracht="Antwoord in twee zinnen.",
             oefeningen=[
                 ("open", "Waarom is een afschrijving een kost, ook al vertrekt er dat jaar geen geld?",
                  "Het geld ging eruit bij de aankoop. De afschrijving verdeelt die kost over de jaren waarin het goed meegaat, zodat de kost in hetzelfde jaar staat als de opbrengst.", 3),
                 ("open", "Wat is het verschil tussen een balans en een resultatenrekening?",
                  "De balans is een foto op één dag, de resultatenrekening gaat over een hele periode.", 2),
             ]),
    ])

# ============================================================ 15
zet("dubbel-boekhouden-redeneerschema-journaal-en-grootboek",
    titel="Dubbel boekhouden: redeneerschema, journaal en grootboek",
    reeksen=[
        dict(kop="Debet of credit?", opdracht="Schrijf D of C.",
             oefeningen=[
                 ("rij", [("Een actiefrekening stijgt", "D"), ("Een actiefrekening daalt", "C"),
                          ("Een passiefrekening stijgt", "C"), ("Een passiefrekening daalt", "D"),
                          ("Een kost", "D"), ("Een opbrengst", "C")],
                  "Vul in.", W),
             ]),
        dict(kop="Het redeneerschema", opdracht="Vul in voor elke verrichting.",
             oefeningen=[
                 ("tabel", ["verrichting", "welke rekeningen", "debet", "credit"],
                  [["aankoop handelsgoederen op factuur", None, None, None],
                   ["verkoop handelsgoederen op factuur", None, None, None],
                   ["betaling aan een leverancier via de bank", None, None, None],
                   ["ontvangst van een klant op de bank", None, None, None]],
                  "aankoop: aankopen + terug te vorderen btw in D, leverancier in C · "
                  "verkoop: handelsvordering in D, verkopen + te betalen btw in C · "
                  "betaling: leverancier in D, bank in C · ontvangst: bank in D, handelsvordering in C"),
             ]),
        dict(kop="Het MAR", opdracht="Schrijf de klasse.",
             oefeningen=[
                 ("rij", [("Vaste activa", "2"), ("Kosten", "6"), ("Opbrengsten", "7"),
                          ("Voorraden", "3"), ("Liquide middelen", "5"),
                          ("Eigen vermogen en lange schulden", "1")],
                  "Vul in.", W),
             ]),
        dict(kop="Rekenen", opdracht="Het btw-tarief is 21 %.",
             oefeningen=[
                 ("kort", "Aankoop van 1 500 euro goederen. Bedrag voor de leverancier?", "1 815 euro", WW),
                 ("kort", "Hoeveel komt er op terug te vorderen btw?", "315 euro", W),
                 ("kort", "Verkoop van 4 000 euro goederen. Factuurtotaal?", "4 840 euro", W),
                 ("kort", "Hoeveel komt er op te betalen btw?", "840 euro", W),
             ]),
        dict(kop="Juist of fout?", opdracht="Kruis aan en verbeter wat fout is.",
             oefeningen=[
                 ("waar", "Het journaal groepeert de boekingen per rekening.", False),
                 ("waar", "Bij de betaling van een factuur verandert er niets aan de kosten.", True),
                 ("waar", "Een inkomende creditnota verhoogt je schuld aan de leverancier.", False),
                 ("waar", "In elke boeking is het totaal debet gelijk aan het totaal credit.", True),
             ]),
    ])


# ============================================================ 16
zet("facturen-kortingen-en-btw", titel="Facturen, kortingen en btw",
    reeksen=[
        dict(kop="De orde van rekenen", opdracht="Zet de stappen in de juiste volgorde: btw · doorgerekende kosten · financiële korting · handelskorting · terugstuurbare verpakking.",
             oefeningen=[
                 ("tabel", ["stap", "wat je doet"],
                  [["1", None], ["2", None], ["3", None], ["4", None], ["5", None], ["6", None]],
                  "1 brutoprijs · 2 handelskorting eraf · 3 financiële korting eraf · 4 doorgerekende kosten erbij "
                  "(= maatstaf van heffing) · 5 btw erop · 6 terugstuurbare verpakking erbij"),
             ]),
        dict(kop="Kortingen berekenen", opdracht="Bereken het bedrag.",
             oefeningen=[
                 ("kort", "15 % handelskorting op 800 euro", "120 euro korting, 680 euro blijft", WL),
                 ("kort", "Daarna 2 % financiële korting op 680 euro", "13,60 euro korting, 666,40 euro blijft", WL),
                 ("kort", "30 % handelskorting op 2 500 euro", "750 euro korting, 1 750 euro blijft", WL),
             ]),
        dict(kop="Een hele factuur", opdracht="Goederen 2 000 euro, 10 % handelskorting, 100 euro doorgerekend vervoer, 21 % btw, 150 euro terugstuurbare verpakking.",
             oefeningen=[
                 ("tabel", ["stap", "bedrag"],
                  [["na de handelskorting", None], ["maatstaf van heffing", None],
                   ["btw", None], ["factuurtotaal", None]],
                  "1 800 euro · 1 900 euro · 399 euro · 1 800 + 100 + 399 + 150 = 2 449 euro"),
             ]),
        dict(kop="Btw erop of niet?", opdracht="Schrijf ja of nee.",
             oefeningen=[
                 ("rij", [("Doorgerekend vervoer", "ja"), ("Terugstuurbare verpakking", "nee"),
                          ("Een doorgerekende verzekering", "ja"), ("Verpakking die niet terugkomt", "ja"),
                          ("De handelskorting", "nee, die gaat er juist af")],
                  "Vul in.", WL),
             ]),
        dict(kop="Soorten aankopen", opdracht="Schrijf: handelsgoederen, diensten en diverse goederen, of investeringsgoed.",
             oefeningen=[
                 ("rij", [("Een vrachtwagen voor de leveringen", "investeringsgoed"),
                          ("Dozen koffie voor de winkelrekken", "handelsgoederen"),
                          ("De brandverzekering", "diensten en diverse goederen"),
                          ("Een machine die tien jaar meegaat", "investeringsgoed"),
                          ("De maandelijkse huur", "diensten en diverse goederen")],
                  "Vul in.", WL),
                 ("open", "Wanneer maakt een leverancier een creditnota? Noem twee gevallen.",
                  "Bijvoorbeeld bij een terugzending, bij een te hoog aangerekend bedrag of bij een korting achteraf.", 2),
             ]),
    ])

# ============================================================ 17
zet("bedrijfsstrategie-missie-visie-swot-en-stakeholders",
    titel="Bedrijfsstrategie: missie, visie, SWOT en stakeholders",
    reeksen=[
        dict(kop="Missie, visie of doelstelling?", opdracht="Schrijf wat het is.",
             oefeningen=[
                 ("rij", [("Wij herstellen fietsen voor wie in de stad woont", "missie"),
                          ("Tegen 2032 rijden al onze bestelwagens elektrisch", "visie"),
                          ("Dit kwartaal 50 fietsen meer herstellen", "doelstelling"),
                          ("Wij leveren altijd eerlijk advies", "kernwaarde"),
                          ("Binnen tien jaar de bekendste fietshersteller van de provincie zijn", "visie")],
                  "Vul in.", WW),
             ]),
        dict(kop="Een SWOT invullen", opdracht="Een kleine chocolatier. Zet elk gegeven in het juiste vak.",
             oefeningen=[
                 ("tabel", ["gegeven", "S, W, O of T?"],
                  [["een eigen recept dat niemand heeft", None],
                   ["de cacaoprijs stijgt sterk", None],
                   ["de winkel heeft maar één verkooppunt", None],
                   ["toeristen ontdekken de stad", None],
                   ["een ervaren chocolatier in dienst", None],
                   ["een nieuwe keten opent twee straten verder", None],
                   ["de koelinstallatie is twintig jaar oud", None],
                   ["webshops groeien snel", None]],
                  "S: eigen recept, ervaren chocolatier · W: één verkooppunt, oude koelinstallatie · "
                  "O: toeristen, groeiende webshops · T: cacaoprijs, nieuwe keten"),
             ]),
        dict(kop="Intern of extern?", opdracht="Schrijf intern of extern.",
             oefeningen=[
                 ("rij", [("Een sterkte", "intern"), ("Een kans", "extern"),
                          ("Een zwakte", "intern"), ("Een bedreiging", "extern")],
                  "Vul in.", W),
             ]),
        dict(kop="Stakeholders", opdracht="Schrijf bij elke stakeholder zijn belang, en of hij intern of extern is.",
             oefeningen=[
                 ("tabel", ["stakeholder", "belang", "intern of extern"],
                  [["het personeel", None, None], ["de aandeelhouders", None, None],
                   ["de buurt", None, None], ["de leveranciers", None, None]],
                  "personeel: loon, veiligheid, werkzekerheid — intern · aandeelhouders: winst en dividend — intern · "
                  "buurt: weinig lawaai en verkeer — extern · leveranciers: op tijd betaald worden — extern"),
                 ("open", "Geef een voorbeeld van twee stakeholders met een botsend belang.",
                  "Bijvoorbeeld het personeel dat een hoger loon wil en de aandeelhouders die een hoger dividend willen; of een uitbreiding van de fabriek tegenover de rust van de buurt.", 3),
             ]),
        dict(kop="Uitleggen", opdracht="Antwoord in twee of drie zinnen.",
             oefeningen=[
                 ("open", "Waarom verhoogt een strategie de succeskansen?",
                  "Iedereen trekt dezelfde kant uit en keuzes worden makkelijker, ook de keuze wat je niet doet. Zo versnippert een bedrijf zijn krachten niet.", 3),
                 ("open", "Kan een zwakte aangepakt worden? En een bedreiging?",
                  "Een zwakte zit in het bedrijf zelf en kan het aanpakken, bijvoorbeeld met opleiding of nieuwe machines. Een bedreiging komt van buiten; daar kan het enkel op inspelen.", 3),
             ]),
    ])

# ============================================================ 18
zet("marktonderzoek-doelgroep-en-de-marketingmix",
    titel="Marktonderzoek, doelgroep en de marketingmix",
    reeksen=[
        dict(kop="Welk soort onderzoek?", opdracht="Schrijf twee dingen: primair of secundair, en kwantitatief of kwalitatief.",
             oefeningen=[
                 ("tabel", ["onderzoek", "primair of secundair", "kwantitatief of kwalitatief"],
                  [["een eigen enquête bij 800 klanten", None, None],
                   ["een groepsgesprek met zes klanten", None, None],
                   ["bevolkingscijfers van de overheid lezen", None, None],
                   ["een rapport van een studiebureau over de sector", None, None]],
                  "primair/kwantitatief · primair/kwalitatief · secundair/kwantitatief · secundair/kwalitatief of kwantitatief, "
                  "naargelang het rapport"),
             ]),
        dict(kop="B2B, B2C, C2C of C2B?", opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("Een groothandel levert aan een café", "B2B"),
                          ("Iemand verkoopt zijn fiets op een platform", "C2C"),
                          ("Een webshop verkoopt een jas aan een gezin", "B2C"),
                          ("Een fotograaf verkoopt beelden aan een merk", "C2B"),
                          ("Een drukkerij maakt folders voor een school", "B2B")],
                  "Vul in.", W),
             ]),
        dict(kop="Welke P?", opdracht="Schrijf product, prijs, plaats of promotie.",
             oefeningen=[
                 ("rij", [("Een actie van twee halen, één betalen", "promotie"),
                          ("Een nieuwe verpakking in gerecycleerd karton", "product"),
                          ("Levering aan huis binnen 24 uur", "plaats"),
                          ("Een korting voor wie een abonnement neemt", "prijs"),
                          ("Een filmpje op sociale media", "promotie"),
                          ("Een winkel openen in het station", "plaats")],
                  "Vul in.", WW),
             ]),
        dict(kop="De vier C's", opdracht="Zet de juiste C bij elke P.",
             oefeningen=[
                 ("tabel", ["P", "C"],
                  [["product", None], ["prijs", None], ["plaats", None], ["promotie", None]],
                  "product: customer value · prijs: cost · plaats: convenience · promotie: communication"),
                 ("open", "Wat is het verschil tussen promotie en communication?",
                  "Promotie vertrekt van het bedrijf dat zendt. Communication is een gesprek in twee richtingen, waarin de klant ook antwoordt.", 3),
             ]),
        dict(kop="Segmenteren", opdracht="Antwoord kort.",
             oefeningen=[
                 ("open", "Noem drie kenmerken waarop een bedrijf kan segmenteren.",
                  "Bijvoorbeeld leeftijd, woonplaats, inkomen, gezinssamenstelling, levensstijl of gedrag.", 2),
                 ("open", "Wat gebeurt er met een boodschap die voor iedereen bedoeld is?",
                  "Ze raakt niemand echt: ze valt nergens op en het reclamegeld rendeert slecht.", 2),
             ]),
    ])

# ============================================================ 19
zet("producten-merken-prijsstrategie-en-distributie",
    titel="Producten, merken, prijsstrategie en distributie",
    reeksen=[
        dict(kop="Welk soort goed?", opdracht="Schrijf convenience, shopping, speciality of unsought.",
             oefeningen=[
                 ("rij", [("Een krant", "convenience"), ("Een bankstel", "shopping"),
                          ("Een grafzerk", "unsought"), ("Een designtas van één merk", "speciality"),
                          ("Een fles water", "convenience"), ("Een brandverzekering", "unsought")],
                  "Vul in.", WW),
             ]),
        dict(kop="Breedte of diepte?", opdracht="Schrijf wat er groeit.",
             oefeningen=[
                 ("rij", [("Een bakker verkoopt voortaan ook soep en belegde broodjes", "breedte"),
                          ("Een bakker bakt zijn brood nu in vier formaten", "diepte"),
                          ("Een winkel neemt een hele lijn babyvoeding erbij", "breedte"),
                          ("Een merk brengt zijn yoghurt in zes smaken uit", "diepte")],
                  "Vul in.", W),
             ]),
        dict(kop="Merkbeleid", opdracht="Schrijf lijnextensie, merkextensie, multibrands of nieuw merk.",
             oefeningen=[
                 ("rij", [("Een koekjesmerk brengt dezelfde koek in een variant met minder suiker", "lijnextensie"),
                          ("Een sportmerk begint met horloges onder dezelfde naam", "merkextensie"),
                          ("Eén fabrikant heeft drie eigen waspoedermerken in het rek", "multibrands"),
                          ("Een fabrikant start met een nieuwe naam in een nieuwe sector", "nieuw merk")],
                  "Vul in.", WW),
             ]),
        dict(kop="De levenscyclus", opdracht="Schrijf de fase.",
             oefeningen=[
                 ("rij", [("Er is nog geen verkoop, enkel kosten", "ontwikkelingsfase"),
                          ("De verkoop stijgt het snelst", "groeifase"),
                          ("De verkoop blijft hoog maar vlak, de concurrentie is scherp", "volwassenheidsfase"),
                          ("De verkoop loopt terug", "neergangsfase"),
                          ("Het product komt net op de markt", "introductiefase")],
                  "Vul in.", WW),
             ]),
        dict(kop="Prijs en distributie", opdracht="Vul in.",
             oefeningen=[
                 ("rij", [("Hoog beginnen en de prijs later laten dalen", "afroomstrategie"),
                          ("Laag beginnen om snel marktaandeel te pakken", "penetratiestrategie"),
                          ("De kostprijs plus een vaste marge", "cost-plus pricing"),
                          ("Een hoge prijs om kwaliteit uit te stralen", "premium pricing"),
                          ("Een treinticket is duurder in de spits", "prijsdifferentiatie"),
                          ("Studenten betalen minder voor dezelfde film", "prijsdiscriminatie"),
                          ("In zoveel winkels als mogelijk liggen", "intensieve distributie"),
                          ("Eén verkooppunt per streek", "exclusieve distributie")],
                  "Vul in.", WL),
                 ("open", "Wat is het verschil tussen een push- en een pullstrategie?",
                  "Bij push duwt de producent zijn product bij de winkelier binnen met kortingen en premies. Bij pull trekt hij de consument aan met reclame, zodat die er zelf naar vraagt.", 3),
             ]),
    ])


if __name__ == "__main__":
    for naam, b in OEFENBUNDELS.items():
        oefenbundel.schrijf(b, naam)

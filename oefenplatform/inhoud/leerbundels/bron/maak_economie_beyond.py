# -*- coding: utf-8 -*-
"""De leerbundels voor algemene economie op 🌍 Beyond doorstroom-niveau.

Gebaseerd op de vakfiche algemene economie 3de graad doorstroom
(2027_algemene_economie_3DDO_3DDG), voor economie-wiskunde en
bedrijfswetenschappen. Dezelfde twintig thema's als de vragen in
`../../beyond/economie.json` (gebouwd door `../../beyond/bron/bouw_economie.py`).

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde stof met andere vragen. Kim laadt de bundel dus twee keer
op, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../beyond/economie.json` doet daar
het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-beyond-doorstroom", zodat het beheer de
categorie uit de bestandsnaam haalt.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, svg

VAK = "Economie"
BEYOND = "🌍 Beyond doorstroom — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}


def grafiek(lijnen=(), vlakken=(), punten=(), breedte=300, hoogte=210,
            xlabel="hoeveelheid", ylabel="prijs", titel=None):
    """Een kleine grafiek op een vlak van 0 tot 10 op beide assen.

    lijnen:  (x1, y1, x2, y2, kleur, label) met kleur "v" (groen), "a" (amber)
             of "g" (grijs, stippel)
    vlakken: ([(x, y), ...], kleur, label) — een gekleurd vlak, bv. een surplus
    punten:  (x, y, label) — een punt met hulplijntjes naar de assen
    """
    d, x, y = svg._as_vlak(breedte, hoogte, xlabel, ylabel)
    kleur = {"v": svg.FOREST, "a": svg.AMBER, "g": svg.DIM}
    for pts, k, label in vlakken:
        pad = " ".join(f"{x(px):.1f},{y(py):.1f}" for px, py in pts)
        d.insert(0, f'<polygon points="{pad}" fill="{kleur[k]}" fill-opacity=".22" stroke="none"/>')
        if label:
            cx = sum(px for px, _ in pts) / len(pts)
            cy = sum(py for _, py in pts) / len(pts)
            d.append(svg._tekst(x(cx), y(cy) + 4, label, 10, svg.INK, "middle", True))
    for x1, y1, x2, y2, k, label in lijnen:
        stip = ' stroke-dasharray="6 4"' if k == "g" else ""
        d.append(f'<line x1="{x(x1):.1f}" y1="{y(y1):.1f}" x2="{x(x2):.1f}" y2="{y(y2):.1f}" '
                 f'stroke="{kleur[k]}" stroke-width="2.2"{stip}/>')
        if label:
            d.append(svg._tekst(x(x2) + 5, y(y2) + 4, label, 11, kleur[k], "start", True))
    for px, py, label in punten:
        d.append(f'<line x1="{x(0):.1f}" y1="{y(py):.1f}" x2="{x(px):.1f}" y2="{y(py):.1f}" '
                 f'stroke="{svg.DIM}" stroke-width="1" stroke-dasharray="3 3"/>')
        d.append(f'<line x1="{x(px):.1f}" y1="{y(0):.1f}" x2="{x(px):.1f}" y2="{y(py):.1f}" '
                 f'stroke="{svg.DIM}" stroke-width="1" stroke-dasharray="3 3"/>')
        d.append(f'<circle cx="{x(px):.1f}" cy="{y(py):.1f}" r="3.6" fill="{svg.INK}"/>')
        if label:
            d.append(svg._tekst(x(px) + 6, y(py) - 6, label, 10.5, svg.INK, "start", True))
    if titel:
        d.append(svg._tekst(breedte / 2 + 24, 12, titel, 11, svg.DARK, "middle", True))
    return svg._svg(breedte, hoogte, "".join(d))


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BEYOND)
    BUNDELS[slug + "-beyond-doorstroom"] = b


# ───────────────────────── 1. De economische kringloop en de macro-economische identiteiten
zet("de-economische-kringloop-en-de-macro-economische-identiteiten",
    titel="De economische kringloop en de macro-economische identiteiten",
    onder="Vijf actoren, drie markten, en de gelijkheden waarmee je ontbrekende cijfers uitrekent.",
    secties=[
        dict(kop="Vijf actoren en drie markten", blokken=[
            ("p", "In de 2de graad zag je de eenvoudige kringloop met gezinnen, bedrijven en overheid. De "
                  "<strong>uitgebreide economische kringloop</strong> heeft er <strong>vijf actoren</strong>: "
                  "<strong>gezinnen, bedrijven, overheid, financiële instellingen en buitenland</strong>."),
            ("p", "Die actoren ontmoeten elkaar op markten. Gezinnen bieden hun <strong>arbeid</strong> aan op de "
                  "<strong>arbeidsmarkt</strong>. Ze kopen goederen en diensten op de <strong>productmarkt</strong>. "
                  "Een bedrijf dat geld leent voor een nieuwe fabriek, doet dat op de <strong>kapitaalmarkt</strong>."),
            ("kader", tabel(["markt", "wat er verhandeld wordt", "wie vraagt, wie biedt aan"],
                            [["arbeidsmarkt", "arbeid", "bedrijven en overheid vragen, gezinnen bieden aan"],
                             ["productmarkt", "goederen en diensten",
                              "gezinnen, bedrijven en overheid kopen er allemaal; bedrijven verkopen"],
                             ["kapitaalmarkt", "spaargeld en kredieten",
                              "spaarders bieden aan, wie investeert leent"]])),
            ("p", "Op de productmarkt zijn dus <strong>gezinnen, bedrijven en de overheid</strong> actief: "
                  "gezinnen kopen voor hun consumptie, bedrijven kopen machines en grondstoffen, de overheid "
                  "koopt bijvoorbeeld wegenwerken."),
        ]),
        dict(kop="Twee stromen, altijd tegengesteld", blokken=[
            ("fig", svg.kringloop(), "De kringloop: tegenover elke reële stroom staat een geldstroom."),
            ("p", "De <strong>reële stroom</strong> bestaat uit goederen, diensten en productiefactoren zoals "
                  "arbeid. Een reële stroom is dus <strong>geen stroom van geld</strong>. De "
                  "<strong>geldstroom</strong> is de betaling ervoor en loopt in de <strong>omgekeerde richting</strong> "
                  "van de goederen- en dienstenstroom."),
            ("p", "Werkt iemand bij een bedrijf, dan gaat <strong>arbeid van het gezin naar het bedrijf</strong> "
                  "en gaat het <strong>loon van het bedrijf naar het gezin</strong>."),
            ("kader", tabel(["van", "naar", "geldstroom"],
                            [["gezinnen", "overheid", "belastingen en sociale bijdragen"],
                             ["overheid", "gezinnen", "uitkeringen en lonen van ambtenaren"],
                             ["buitenland", "België", "betalingen voor de Belgische export"],
                             ["België", "buitenland", "betalingen voor de import"]])),
            ("p", "De <strong>financiële instellingen</strong> zijn de <strong>schakel tussen wie spaart en wie "
                  "investeert</strong>: ze nemen spaargeld in en lenen het uit."),
        ]),
        dict(kop="Wat de letters betekenen", blokken=[
            ("kader", tabel(["letter", "betekenis"],
                            [["Y", "het nationaal inkomen (of de productie)"],
                             ["C", "consumptie van de gezinnen"],
                             ["S", "sparen"],
                             ["T", "belastingen (en sociale bijdragen)"],
                             ["I", "investeringen van bedrijven: machines, gebouwen, voorraden"],
                             ["G", "overheidsbestedingen"],
                             ["X en M", "export en import"],
                             ["NX = X − M", "de netto-export"]])),
            ("weetje", "<strong>Investeringen (I)</strong> zijn in de economie aankopen van kapitaalgoederen "
                       "door bedrijven, zoals een machine of een fabriek. Een gezin dat aandelen koopt, "
                       "investeert in het dagelijkse spraakgebruik, maar in de kringloop is dat sparen."),
        ]),
        dict(kop="De identiteiten: wat binnenkomt, gaat ook buiten", blokken=[
            ("p", "Bij elke actor is <strong>wat binnenkomt gelijk aan wat buitengaat</strong>. Daarom kan je de "
                  "kringloop gebruiken om <strong>ontbrekende cijfers te berekenen</strong>."),
            ("p", "<strong>Langs de kant van de gezinnen</strong>: het inkomen gaat naar belastingen, consumptie "
                  "en sparen. <strong>Y = T + C + S</strong>. Een gezin dat 50 000 euro verdient, 15 000 euro "
                  "belastingen betaalt en 30 000 euro consumeert, spaart 50 000 − 15 000 − 30 000 = "
                  "<strong>5 000 euro</strong>. Zo vind je ook C: met Y = 1 000, T = 300 en S = 150 is "
                  "C = 1 000 − 300 − 150 = <strong>550</strong>."),
            ("p", "<strong>Langs de kant van de bestedingen</strong>: alles wat geproduceerd wordt, wordt door "
                  "iemand gekocht. <strong>Y = C + I + G + (X − M)</strong>. Met C = 600, I = 200, G = 250, "
                  "X = 400 en M = 350 is Y = 600 + 200 + 250 + 50 = <strong>1 100</strong>."),
            ("p", "Een <strong>stijging van de import</strong> doet, als de rest gelijk blijft, het binnenlands "
                  "inkomen Y <strong>dalen</strong>: dat geld wordt in het buitenland besteed."),
            ("p", "Koopt een Belgisch bedrijf een machine in Duitsland, dan is dat in de kringloop van België "
                  "<strong>een investering (I) én een import (M)</strong>."),
            ("p", "In een <strong>gesloten economie zonder overheid</strong> zijn er alleen gezinnen en bedrijven. "
                  "Dan geldt <strong>S = I</strong>: wat gespaard wordt, wordt via de banken geïnvesteerd."),
        ]),
        dict(kop="De drie saldi", blokken=[
            ("p", "Bij de financiële instellingen komt alles samen. Daar geldt "
                  "<strong>S + T = I + G + X − M</strong>. Schuif je de termen wat op, dan krijg je:"),
            ("kader", "<p style=\"text-align:center;font-size:12pt\"><strong>(S − I) + (T − G) = (X − M)</strong></p>" +
                      tabel(["saldo", "naam", "positief betekent"],
                            [["S − I", "het spaarsaldo van de particuliere sector",
                              "de particulieren sparen meer dan ze investeren"],
                             ["T − G", "het begrotingssaldo van de overheid",
                              "de overheid ontvangt meer dan ze uitgeeft (overschot)"],
                             ["X − M", "het handelsbalanssaldo",
                              "het land exporteert meer dan het importeert"]])),
            ("p", "De saldi van de particuliere sector en de overheid zijn <strong>samen gelijk aan het "
                  "handelsbalanssaldo</strong>. Uit de cijfers van een kringloop kan je dus het spaarsaldo, het "
                  "begrotingssaldo en het handelsbalanssaldo afleiden."),
            ("p", "Het <strong>begrotingssaldo is negatief</strong> als de overheid meer uitgeeft dan ze "
                  "ontvangt. T = 400 en G = 420 betekent een <strong>begrotingstekort van 20</strong>. Een "
                  "<strong>negatief handelsbalanssaldo</strong> betekent dat een land <strong>meer importeert dan "
                  "het exporteert</strong>."),
            ("p", "Voorbeelden. S = 300, I = 250, T = 400, G = 420 geeft (300 − 250) + (400 − 420) = 50 − 20 = "
                  "<strong>X − M = 30</strong>. Is het spaarsaldo +40 en het handelsbalanssaldo +10, dan is "
                  "T − G = 10 − 40 = <strong>−30</strong>. Met I = 200, G = 300, X = 500, M = 450 en T = 280 "
                  "vind je S uit S + 280 = 200 + 300 + 50, dus <strong>S = 270</strong>."),
            ("p", "Een land kan dus een <strong>overheidstekort</strong> hebben en toch een <strong>positief "
                  "handelsbalanssaldo</strong>, als de particuliere sector veel meer spaart dan ze investeert. "
                  "En omgekeerd: heeft een land een <strong>handelsoverschot</strong>, dan moeten de particuliere "
                  "sector en de overheid samen meer sparen dan er geïnvesteerd en besteed wordt."),
        ]),
        dict(kop="Wat het model niet ziet", blokken=[
            ("p", "Het klassieke kringloopmodel telt alleen wat met geld betaald wordt. Een "
                  "<strong>tekortkoming</strong> is dat het <strong>de grenzen van grondstoffen en het afval "
                  "negeert</strong>. Ook <strong>vervuiling en afval</strong> en <strong>onbetaald werk zoals "
                  "mantelzorg</strong> zitten er niet in. In het thema over alternatieve economische modellen "
                  "zie je hoe economen dat proberen op te lossen."),
        ]),
    ],
    onthoud=[
        "Vijf actoren: gezinnen, bedrijven, overheid, financiële instellingen en buitenland.",
        "Arbeid op de arbeidsmarkt, goederen op de productmarkt, leningen op de kapitaalmarkt.",
        "De geldstroom loopt tegengesteld aan de reële stroom.",
        "Gezinnen: Y = T + C + S. Bestedingen: Y = C + I + G + (X − M).",
        "(S − I) + (T − G) = (X − M): spaarsaldo plus begrotingssaldo is het handelsbalanssaldo.",
        "Zonder overheid en buitenland geldt S = I.",
        "Het model negeert grondstoffen, afval en onbetaald werk.",
    ])


# ───────────────────────── 2. Alternatieve economische modellen, MVO en de SDG's
zet("alternatieve-economische-modellen-mvo-en-de-sdg-s",
    titel="Alternatieve economische modellen, MVO en de SDG's",
    onder="Wat het klassieke groeimodel mist, en hoe economen, bedrijven en landen het anders aanpakken.",
    secties=[
        dict(kop="Waarom andere modellen?", blokken=[
            ("p", "Het <strong>klassieke groeimodel</strong> gaat ervan uit dat de productie "
                  "<strong>onbeperkt kan blijven groeien</strong>. Het klassieke kringloopmodel telt enkel wat met "
                  "geld betaald wordt. Daardoor <strong>ziet het model de schade aan natuur en mens niet</strong>: "
                  "uitgeputte grondstoffen, afval, vervuiling of mensen die uit de boot vallen."),
            ("p", "<strong>Duurzame ontwikkeling</strong> betekent: <strong>voorzien in de behoeften van nu zonder "
                  "die van later in gevaar te brengen</strong>. De alternatieve modellen hieronder proberen dat "
                  "elk op hun manier."),
        ]),
        dict(kop="De circulaire economie", blokken=[
            ("p", "De kern van de <strong>circulaire economie</strong>: <strong>grondstoffen zo lang mogelijk "
                  "hergebruiken in plaats van ze weg te gooien</strong>. De lineaire economie werkt als "
                  "nemen, maken, weggooien; de circulaire economie sluit de kring."),
            ("p", "Er is een vaste volgorde van voorkeur. Eerst <strong>minder gebruiken</strong>, dan "
                  "<strong>herstellen en hergebruiken</strong>, en pas als dat niet meer kan "
                  "<strong>recycleren</strong>. Recycleren is dus <strong>niet</strong> de eerste keuze: het "
                  "kost energie en er gaat altijd materiaal verloren."),
            ("p", "Een fabrikant die <strong>wasmachines verhuurt</strong> in plaats van ze te verkopen, en ze "
                  "terugneemt om te herstellen, werkt circulair: hij heeft er zelf belang bij dat het toestel "
                  "lang meegaat. Voordelen: <strong>minder afval</strong> en <strong>minder nood aan nieuwe "
                  "grondstoffen</strong>."),
        ]),
        dict(kop="De donuteconomie", blokken=[
            ("p", "De <strong>donuteconomie</strong> van Kate Raworth tekent twee ringen: een "
                  "<strong>sociaal fundament</strong> (binnenring) en een <strong>ecologisch plafond</strong> "
                  "(buitenring). De economie moet in de donut zelf blijven, daartussen."),
            ("kader", tabel(["waar", "wat het betekent", "voorbeelden"],
                            [["onder het sociaal fundament", "tekorten", "honger, geen toegang tot onderwijs of zorg"],
                             ["in de donut", "veilig en rechtvaardig", "iedereen heeft genoeg, de planeet houdt het"],
                             ["boven het ecologisch plafond", "overschrijding van de grenzen van de planeet",
                              "klimaatverandering, verlies aan biodiversiteit"]])),
            ("p", "In de donuteconomie is economische groei <strong>op zich niet het doel</strong>, en succes "
                  "wordt <strong>niet</strong> vooral gemeten met de groei van het bbp, maar met hoe goed een land "
                  "tussen de twee ringen blijft."),
        ]),
        dict(kop="De deeleconomie en de sociale economie", blokken=[
            ("p", "In de <strong>deeleconomie</strong> gaat het meer om <strong>toegang tot een product dan om het "
                  "bezit</strong> ervan. Voorbeelden: een <strong>autodeelsysteem</strong> waarbij je een auto per "
                  "uur huurt, of een <strong>gereedschapsbibliotheek</strong> waar inwoners een boor of ladder "
                  "lenen. Dat is duurzamer, omdat <strong>er minder producten nodig zijn voor hetzelfde "
                  "gebruik</strong>."),
            ("p", "In de <strong>sociale economie</strong> staat <strong>werk voor mensen die moeilijk een job "
                  "vinden</strong> centraal. Een <strong>maatwerkbedrijf</strong> dat mensen met een "
                  "arbeidshandicap tewerkstelt, hoort erbij. Het voordeel: die mensen krijgen een job en een "
                  "inkomen."),
            ("weetje", "Een <strong>kringwinkel</strong> hoort bij twee modellen tegelijk: hij verkoopt "
                       "tweedehands spullen (circulair) en geeft werk aan mensen die moeilijk een job vinden "
                       "(sociaal)."),
        ]),
        dict(kop="Maatschappelijk verantwoord ondernemen (MVO)", blokken=[
            ("p", "<strong>MVO</strong> betekent dat een bedrijf <strong>rekening houdt met de gevolgen van zijn "
                  "activiteiten voor mens en milieu</strong>. In de economie betekenen <strong>duurzaam "
                  "ondernemen en MVO ongeveer hetzelfde</strong>. MVO steunt op drie pijlers, de drie P's:"),
            ("kader", tabel(["pijler", "waarover", "voorbeelden"],
                            [["People", "mensen", "goede werkomstandigheden, eerlijke lonen bij leveranciers"],
                             ["Planet", "milieu", "minder verpakkingsmateriaal, elektrische bedrijfswagens"],
                             ["Profit", "winst", "het bedrijf moet gezond blijven en mag winst maken"]])),
            ("p", "Bij MVO mag een bedrijf dus wel <strong>winst</strong> maken: het gaat om een evenwicht "
                  "tussen de drie P's."),
        ]),
        dict(kop="Greenwashing herkennen", blokken=[
            ("p", "<strong>Greenwashing</strong>: een bedrijf <strong>doet zich groener voor dan het is</strong>. "
                  "Een kledingketen die 'bewuste collectie' op een klein deel van haar kleren zet en daar zwaar "
                  "mee adverteert, terwijl de rest niet verandert, doet aan greenwashing."),
            ("p", "Je herkent het aan <strong>vage woorden zoals 'natuurlijk' of 'eco' zonder bewijs</strong>, aan "
                  "<strong>een groen logo zonder erkend label</strong>, of aan <strong>een groot groen beeld zonder "
                  "bewijs</strong>. Belooft een vliegmaatschappij 'klimaatneutraal vliegen' omdat je voor twee "
                  "euro bomen kan laten planten, zonder te zeggen hoe ze dat controleert, dan kan het "
                  "greenwashing zijn."),
        ]),
        dict(kop="De zeventien SDG's", blokken=[
            ("p", "De Verenigde Naties legden <strong>17 duurzame ontwikkelingsdoelen</strong> vast, de "
                  "<strong>SDG's</strong> (Sustainable Development Goals). Ze moeten tegen <strong>2030</strong> "
                  "bereikt zijn en gelden voor <strong>alle landen</strong>, niet enkel voor arme landen."),
            ("p", "De SDG's worden gegroepeerd in vijf kernwaarden, de <strong>5 P's</strong>: "
                  "<strong>People, Planet, Prosperity, Peace en Partnership</strong>."),
            ("kader", tabel(["kernwaarde", "voorbeelden van doelen"],
                            [["People", "geen armoede, geen honger, goed onderwijs, gendergelijkheid"],
                             ["Planet", "klimaatactie, leven in het water en op het land"],
                             ["Prosperity", "waardig werk en economische groei, betaalbare en duurzame energie"],
                             ["Peace", "vrede, justitie en sterke instellingen"],
                             ["Partnership", "partnerschap om de doelen te bereiken"]])),
            ("p", "Voorbeelden. Een school die gratis ontbijt geeft aan kinderen die zonder eten komen: "
                  "<strong>geen honger</strong>. Een bedrijf dat zijn uitstoot van broeikasgassen halveert: "
                  "<strong>klimaatactie</strong>. Een chocoladebedrijf dat cacaoboeren een eerlijke prijs betaalt: "
                  "<strong>geen armoede</strong>."),
        ]),
    ],
    onthoud=[
        "Het klassieke groeimodel gaat uit van onbeperkte groei en ziet de schade aan natuur en mens niet.",
        "Circulair: grondstoffen zo lang mogelijk hergebruiken; herstellen gaat vóór recycleren.",
        "Donut: tussen een sociaal fundament en een ecologisch plafond; groei is geen doel op zich.",
        "Deeleconomie: toegang in plaats van bezit. Sociale economie: werk voor wie moeilijk een job vindt.",
        "MVO steunt op People, Planet en Profit; winst maken mag.",
        "Greenwashing: groener lijken dan je bent, met vage woorden en zonder bewijs.",
        "17 SDG's tegen 2030, voor alle landen, in vijf P's: People, Planet, Prosperity, Peace, Partnership.",
    ])


# ───────────────────────── 3. Het bbp, economische groei en welvaartsindicatoren
zet("het-bbp-economische-groei-en-welvaartsindicatoren",
    titel="Het bbp, economische groei en welvaartsindicatoren",
    onder="Hoe je het bbp op drie manieren berekent, wat reële groei is, en wat het bbp niet meet.",
    secties=[
        dict(kop="Wat het bbp is", blokken=[
            ("p", "Het <strong>bruto binnenlands product (bbp)</strong> is <strong>de waarde van alle finale "
                  "goederen en diensten die een jaar lang in een land gemaakt worden</strong>. 'Binnenlands' wil "
                  "zeggen: alles wat binnen de grenzen geproduceerd wordt, wie het ook maakt. Een "
                  "<strong>Nederlander die in Antwerpen werkt</strong>, draagt dus bij aan het Belgische bbp."),
            ("p", "In België publiceert de <strong>Nationale Bank van België</strong> de officiële cijfers over het "
                  "bbp."),
        ]),
        dict(kop="Drie berekeningswijzen", blokken=[
            ("p", "Je kan het bbp op drie manieren berekenen. Ze komen op hetzelfde uit, omdat elke euro die "
                  "besteed wordt, voor iemand een inkomen is en bij iemand toegevoegde waarde."),
            ("kader", tabel(["benadering", "wat je optelt"],
                            [["bestedingsbenadering", "bbp = C + I + G + (X − M)"],
                             ["inkomensbenadering", "de lonen, interesten, huren en winsten"],
                             ["productiebenadering", "de toegevoegde waarde van alle bedrijven"]])),
            ("p", "In de <strong>bestedingsbenadering</strong> tellen aankopen van finale goederen mee: een gezin "
                  "dat een nieuwe fiets koopt (C), een bedrijf dat een nieuwe machine koopt (I)."),
        ]),
        dict(kop="Toegevoegde waarde en de bedrijfskolom", blokken=[
            ("p", "De <strong>bruto toegevoegde waarde</strong> is de omzet min de aankopen bij andere bedrijven. "
                  "Een bakker die brood verkoopt voor 50 000 euro en voor 20 000 euro bloem en andere "
                  "grondstoffen kocht, heeft een bruto toegevoegde waarde van <strong>30 000 euro</strong>."),
            ("p", "Trek je daar de <strong>afschrijvingen</strong> af, de slijtage van zijn oven bijvoorbeeld, dan "
                  "krijg je de <strong>netto toegevoegde waarde</strong>. Met 5 000 euro afschrijvingen is dat "
                  "<strong>25 000 euro</strong>. Het verschil tussen bruto en netto zijn dus de afschrijvingen."),
            ("p", "In een <strong>bedrijfskolom</strong> mag je de omzetten van elke schakel <strong>niet</strong> "
                  "optellen: dan tel je het hout drie keer. De boswachter verkoopt hout voor 100, de zagerij "
                  "planken voor 250, de meubelmaker de tafel voor 600. De toegevoegde waarden zijn 100, 150 en "
                  "350, samen <strong>600</strong>: precies de waarde van het finale product."),
        ]),
        dict(kop="Factorprijzen en marktprijzen, bbp en bnp", blokken=[
            ("p", "Het <strong>bbp tegen factorprijzen</strong> is wat de productiefactoren verdienen. Het "
                  "<strong>bbp tegen marktprijzen</strong> is wat de koper betaalt. Je gaat van het eerste naar het "
                  "tweede door de <strong>indirecte belastingen erbij te tellen en de subsidies af te trekken</strong>. "
                  "Met 480 tegen factorprijzen, 70 indirecte belastingen en 10 subsidies is het bbp tegen "
                  "marktprijzen 480 + 70 − 10 = <strong>540</strong>. Omdat de belastingen meestal groter zijn dan "
                  "de subsidies, is het bbp tegen marktprijzen meestal groter."),
            ("p", "Het <strong>bruto nationaal product (bnp)</strong> kijkt naar de inwoners in plaats van naar het "
                  "grondgebied. Het telt wel de <strong>inkomens die inwoners verdienen in het buitenland</strong>:"),
            ("kader", "<p style=\"text-align:center\"><strong>bnp = bbp + primaire inkomens uit het buitenland "
                      "− primaire inkomens naar het buitenland</strong></p>"),
            ("p", "Trek je van het bnp de afschrijvingen af, dan krijg je het netto nationaal product. Het "
                  "<strong>nationaal inkomen</strong> is <strong>het netto nationaal product tegen "
                  "factorkosten</strong>."),
        ]),
        dict(kop="Nominaal en reëel bbp", blokken=[
            ("p", "Het <strong>nominaal bbp</strong> rekent in de prijzen van dat jaar. Het kan dus ook stijgen "
                  "omdat alles duurder werd, zonder dat er meer geproduceerd wordt. Het <strong>reëel bbp</strong> "
                  "is <strong>het bbp in constante prijzen</strong>: de prijsstijging is eruit gehaald."),
            ("p", "Stijgt het nominaal bbp met 5 % en de prijzen met 3 %, dan groeide het reëel bbp met "
                  "<strong>ongeveer 2 %</strong>. Wil je weten of de economie echt groeide, dan "
                  "<strong>vergelijk je het reëel bbp van beide jaren</strong>."),
            ("p", "<strong>Innovatie</strong> heet een motor van economische groei: <strong>nieuwe technieken laten "
                  "toe met dezelfde middelen meer of betere producten te maken</strong>. Innovatie is ook een "
                  "<strong>disruptieve factor</strong>: een vernieuwing kan bestaande bedrijven of beroepen "
                  "overbodig maken."),
        ]),
        dict(kop="Bbp per capita: wat het wel en niet zegt", blokken=[
            ("p", "Om welvaart te vergelijken, gebruik je het <strong>bbp per capita</strong>, omdat <strong>landen "
                  "verschillend veel inwoners hebben</strong>. Een bbp van 600 miljard euro en 12 miljoen inwoners "
                  "geeft 600 000 000 000 / 12 000 000 = <strong>50 000 euro</strong> per inwoner."),
            ("p", "Het bbp per capita heeft tekortkomingen:"),
            ("kader", "<ul><li>het zegt <strong>niets over hoe het inkomen verdeeld is</strong>: een hoger bbp per "
                      "capita betekent dus niet altijd dat de meeste inwoners er beter aan toe zijn;</li>"
                      "<li><strong>onbetaald werk</strong> zoals vrijwilligerswerk of <strong>een ouder die thuis voor "
                      "de kinderen zorgt</strong>, telt niet mee;</li>"
                      "<li>het houdt <strong>geen rekening met de schade aan het milieu</strong>;</li>"
                      "<li>herstel na een ramp telt als productie: <strong>het opruimen na een overstroming doet het "
                      "bbp stijgen</strong>.</li></ul>"),
            ("p", "<strong>Welvaart</strong> en <strong>welzijn</strong> zijn in de economie niet hetzelfde. "
                  "Welvaart gaat over de materiële behoeften die je met geld kan vervullen; welzijn is ruimer: "
                  "gezondheid, vrije tijd, geluk, een veilige omgeving."),
        ]),
        dict(kop="Andere welvaartsindicatoren", blokken=[
            ("kader", tabel(["indicator", "wat ze meet"],
                            [["HDI (Human Development Index)", "levensverwachting, onderwijs en inkomen per inwoner"],
                             ["BNG (Bruto Nationaal Geluk)", "geluk en welzijn; bekend gemaakt door Bhutan"],
                             ["MEW (Measure of Economic Welfare)",
                              "past het bbp aan voor vrije tijd, onbetaald werk en schade"],
                             ["Better Life Index (OESO)", "je kiest zelf hoe zwaar elk onderdeel doorweegt"],
                             ["SDG Dashboard en SDG Index",
                              "hoe ver een land staat met het halen van de duurzame ontwikkelingsdoelen"]])),
            ("p", "De <strong>HDI</strong> en het <strong>BNG</strong> meten meer dan alleen materiële welvaart. "
                  "Een land met een gemiddeld bbp per capita kan zo toch een hoge HDI hebben, als levensverwachting "
                  "en onderwijs goed scoren."),
        ]),
    ],
    onthoud=[
        "Bbp: de waarde van alle finale goederen en diensten die een jaar lang in een land gemaakt worden.",
        "Drie benaderingen: bestedingen (C + I + G + X − M), inkomens (lonen, interesten, huren, winsten), productie (toegevoegde waarde).",
        "Bruto min afschrijvingen is netto. Tel in een bedrijfskolom de toegevoegde waarden op, niet de omzetten.",
        "Marktprijzen = factorprijzen + indirecte belastingen − subsidies.",
        "Bnp telt ook de inkomens van inwoners uit het buitenland.",
        "Reëel bbp = bbp in constante prijzen; reële groei ≈ nominale groei − inflatie.",
        "Bbp per capita mist verdeling, onbetaald werk en milieuschade; HDI, BNG, MEW en Better Life Index meten breder.",
    ])


# ───────────────────────── 4. De vraagcurve en de prijselasticiteit van de vraag
zet("de-vraagcurve-en-de-prijselasticiteit-van-de-vraag",
    titel="De vraagcurve en de prijselasticiteit van de vraag",
    onder="Van één consument naar de hele markt, en hoe sterk de vraag reageert op de prijs.",
    secties=[
        dict(kop="De vraagcurve", blokken=[
            ("p", "Een gewone vraagcurve verloopt <strong>dalend: hoe hoger de prijs, hoe kleiner de gevraagde "
                  "hoeveelheid</strong>."),
            ("p", "De <strong>individuele vraagcurve</strong> leid je af uit de optimale goederencombinatie van één "
                  "consument: <strong>je laat de prijs van een goed veranderen en noteert telkens de gekozen "
                  "hoeveelheid</strong>. De <strong>collectieve vraagcurve</strong> (de marktvraag) vind je door "
                  "<strong>bij elke prijs de gevraagde hoeveelheden van alle consumenten op te tellen</strong>. "
                  "Vraagt An bij 4 euro 3 stuks, Bram 5 en Charlotte 2, dan is de collectieve vraag bij 4 euro "
                  "<strong>10 stuks</strong>."),
        ]),
        dict(kop="Beweging op de curve of verschuiving van de curve?", blokken=[
            ("p", "Verandert de <strong>prijs van het goed zelf</strong>, dan is er een <strong>beweging op de "
                  "vraagcurve</strong>: de curve blijft liggen, je schuift er langs naar een ander punt. Stijgt de "
                  "prijs van koffie, dan beweeg je op de vraagcurve van koffie."),
            ("p", "Verandert iets anders, dan <strong>verschuift</strong> de hele curve. Een daling van het inkomen "
                  "geeft dus geen beweging op de curve, maar een verschuiving."),
            ("fig", grafiek(lijnen=[(1, 9, 8, 2, "v", "V"), (3, 9, 10, 2, "g", "V′")]),
             "Naar rechts: bij elke prijs wordt er meer gevraagd."),
            ("kader", tabel(["de vraagcurve van een normaal goed verschuift naar rechts als ...", "naar links als ..."],
                            [["het inkomen van de consumenten stijgt", "het inkomen daalt"],
                             ["het goed populairder wordt, bv. door een goede reclamecampagne", "het goed uit de mode raakt"],
                             ["de prijs van een substituut stijgt", "de prijs van een substituut daalt"],
                             ["de prijs van een complementair goed daalt", "de prijs van een complementair goed stijgt"]])),
            ("p", "<strong>Substituten</strong> vervangen elkaar, zoals boter en margarine. Stijgt de prijs van "
                  "boter sterk, dan <strong>verschuift de vraagcurve van margarine naar rechts</strong>. "
                  "<strong>Complementaire goederen</strong> gebruik je samen, zoals een printer en inkt. Daalt de "
                  "prijs van smartphones, dan verschuift de vraagcurve van smartphonehoesjes naar rechts. Stijgt de "
                  "prijs van een complementair goed, dan daalt de vraag naar het goed zelf."),
        ]),
        dict(kop="De prijselasticiteit van de vraag", blokken=[
            ("p", "De <strong>prijselasticiteit van de vraag</strong> zegt hoe sterk de gevraagde hoeveelheid "
                  "reageert op een prijsverandering:"),
            ("kader", "<p style=\"text-align:center\"><strong>E<sub>p</sub> = procentuele verandering van de "
                      "gevraagde hoeveelheid / procentuele verandering van de prijs</strong></p>"),
            ("p", "Omdat prijs en hoeveelheid tegengesteld bewegen, is de uitkomst negatief. Voorbeelden:"),
            ("kader", "<ul><li>De prijs stijgt met 10 %, de hoeveelheid daalt met 20 %: E = −20 / 10 = "
                      "<strong>−2</strong>.</li>"
                      "<li>De prijs daalt van 10 naar 8 euro (−20 %), de hoeveelheid stijgt van 100 naar 110 "
                      "(+10 %): E = 10 / −20 = <strong>−0,5</strong>.</li>"
                      "<li>De prijs stijgt van 20 naar 22 euro (+10 %), de hoeveelheid daalt van 500 naar 450 "
                      "(−10 %): E = <strong>−1</strong>.</li>"
                      "<li>Omgekeerd: E = −1,5 en de prijs stijgt met 4 %, dan daalt de hoeveelheid met "
                      "1,5 × 4 = <strong>6 %</strong>.</li></ul>"),
        ]),
        dict(kop="Elastisch, inelastisch en de omzet", blokken=[
            ("kader", tabel(["elasticiteit (zonder teken)", "naam", "prijs omhoog, dan de omzet ..."],
                            [["groter dan 1", "elastisch", "daalt"],
                             ["gelijk aan 1", "unitair elastisch", "blijft ongeveer gelijk"],
                             ["kleiner dan 1, bv. −0,4", "inelastisch", "stijgt"],
                             ["0", "perfect inelastisch: verticale curve", "stijgt evenredig"],
                             ["oneindig", "perfect elastisch: horizontale curve", "valt weg"]])),
            ("fig", svg.naast_elkaar([grafiek(lijnen=[(5, 9, 5, 1, "v", "V")], breedte=200, hoogte=160,
                                              titel="perfect inelastisch"),
                                      grafiek(lijnen=[(1, 5, 9, 5, "v", "V")], breedte=200, hoogte=160,
                                              titel="perfect elastisch")]),
             "Links: E = 0, de hoeveelheid verandert nooit. Rechts: bij een hogere prijs verkoop je niets meer."),
            ("p", "Een perfect inelastische vraag heeft dus een elasticiteit van <strong>0</strong>, niet −1. Die "
                  "vraag wordt het minst beïnvloed door een prijsstijging. Een perfect elastische vraag komt voor "
                  "bij <strong>een producent die heel veel concurrenten heeft met hetzelfde product</strong>."),
            ("p", "Bij dezelfde schaal wijst een <strong>steilere vraagcurve</strong> op een minder elastische "
                  "vraag. Langs een rechte, dalende vraagcurve <strong>verandert de elasticiteit</strong>: bovenaan "
                  "is de vraag elastisch, onderaan inelastisch."),
            ("p", "Daalt de prijs met 5 % en stijgt de hoeveelheid met 5 %, dan blijft de omzet ongeveer gelijk. "
                  "Wil een <strong>bioscoop</strong> meer omzet terwijl de vraag naar tickets elastisch is, dan "
                  "<strong>verlaagt ze best de prijs</strong>."),
        ]),
        dict(kop="Waarom is de ene vraag elastischer dan de andere?", blokken=[
            ("kader", tabel(["de vraag is elastischer als ...", "voorbeelden"],
                            [["er veel alternatieven zijn", "een merk frisdrank met veel concurrenten in de winkel"],
                             ["het product een groot deel van het budget inneemt", "een auto, een reis"],
                             ["het een luxeproduct is", "juwelen, een citytrip"],
                             ["je lang de tijd hebt om je aan te passen", "op lange termijn eerder dan op korte termijn"]])),
            ("kader", tabel(["de vraag is inelastisch als ...", "voorbeelden"],
                            [["het een eerste levensbehoefte is", "brood, elektriciteit"],
                             ["er geen alternatief is", "insuline voor een diabetespatiënt"],
                             ["er een verslavingseffect is", "sigaretten"],
                             ["het maar een klein deel van het budget inneemt", "zout"]])),
            ("p", "Daarom werkt het als een overheid de <strong>accijns op tabak</strong> verhoogt om meer "
                  "belastinginkomsten te krijgen: de vraag is inelastisch, dus <strong>de verkoop daalt maar "
                  "weinig</strong>."),
        ]),
    ],
    onthoud=[
        "De vraagcurve daalt. De marktvraag is de som van de individuele vragen bij elke prijs.",
        "Prijs van het goed zelf: beweging op de curve. Inkomen, mode, substituten, complementen: verschuiving.",
        "E = % verandering hoeveelheid / % verandering prijs; meestal negatief.",
        "Elastisch (> 1): prijs omhoog, omzet omlaag. Inelastisch (< 1): prijs omhoog, omzet omhoog. Unitair: omzet gelijk.",
        "Perfect inelastisch = verticaal (E = 0), perfect elastisch = horizontaal.",
        "Elastischer bij veel alternatieven, groot budgetaandeel, luxe en op lange termijn.",
    ])


# ───────────────────────── 5. Inkomenselasticiteit, de aanbodcurve en de elasticiteit van het aanbod
zet("inkomenselasticiteit-de-aanbodcurve-en-de-elasticiteit-van-het-aanbod",
    titel="Inkomenselasticiteit, de aanbodcurve en de elasticiteit van het aanbod",
    onder="Hoe de vraag reageert op het inkomen, en hoe sterk producenten reageren op de prijs.",
    secties=[
        dict(kop="De inkomenselasticiteit van de vraag", blokken=[
            ("kader", "<p style=\"text-align:center\"><strong>E<sub>y</sub> = procentuele verandering van de "
                      "gevraagde hoeveelheid / procentuele verandering van het inkomen</strong></p>"),
            ("p", "Stijgt het inkomen met 5 % en de vraag naar restaurantbezoeken met 10 %, dan is de "
                  "inkomenselasticiteit 10 / 5 = <strong>2</strong>. Is de inkomenselasticiteit van brood 0,2 en "
                  "stijgt het inkomen met 10 %, dan stijgt de vraag naar brood met 0,2 × 10 = <strong>2 %</strong>."),
            ("kader", tabel(["inkomenselasticiteit", "soort goed", "voorbeeld"],
                            [["kleiner dan 0 (negatief)", "inferieur goed", "busritten, als mensen met meer geld een auto kopen"],
                             ["0", "indifferent goed: de vraag verandert niet als het inkomen verandert", "zout"],
                             ["tussen 0 en 1", "noodzakelijk goed", "brood, elektriciteit"],
                             ["groter dan 1", "luxegoed", "een verre vakantie, restaurantbezoeken"]])),
            ("p", "<strong>Noodzakelijke goederen</strong> en <strong>luxegoederen</strong> zijn allebei "
                  "<strong>normale goederen</strong>: de vraag stijgt als het inkomen stijgt. Een goed met een "
                  "inkomenselasticiteit van 0,8 is dus noodzakelijk, geen luxe."),
            ("p", "Een <strong>inferieur goed</strong> is <strong>geen</strong> goed van slechte kwaliteit dat "
                  "niemand wil. Het is een goed dat je minder koopt als je meer verdient, omdat je dan iets anders "
                  "kiest. Stijgt het inkomen met 10 % en daalt de vraag naar busritten met 3 %, dan zijn busritten "
                  "een inferieur goed. Een goed kan voor de ene consument normaal zijn en voor een andere "
                  "inferieur."),
        ]),
        dict(kop="De aanbodcurve", blokken=[
            ("p", "Een gewone aanbodcurve verloopt <strong>stijgend: bij een hogere prijs wil men meer "
                  "aanbieden</strong>. Bij volkomen concurrentie leid je de individuele aanbodcurve van een "
                  "producent af uit <strong>het stijgende deel van de marginale kostencurve</strong>. Elk punt "
                  "op die curve is <strong>de optimale productiegrootte bij die prijs</strong>. Ligt de prijs "
                  "<strong>onder het minimum van de gemiddelde variabele kosten</strong>, dan biedt de producent "
                  "op korte termijn niets aan."),
            ("p", "Het <strong>collectieve aanbod</strong> vind je door <strong>bij elke prijs de aangeboden "
                  "hoeveelheden van alle producenten op te tellen</strong>. Bieden drie bakkers bij 3 euro 40, 50 "
                  "en 30 broden aan, dan is het collectieve aanbod <strong>120</strong>."),
            ("p", "Stijgt de marktprijs van tomaten, dan is er een <strong>beweging op</strong> de aanbodcurve, "
                  "geen verschuiving. De curve zelf verschuift door andere oorzaken:"),
            ("kader", tabel(["naar rechts (meer aanbod)", "naar links (minder aanbod)"],
                            [["een nieuwe, goedkopere productietechniek", "de prijs van grondstoffen stijgt sterk"],
                             ["er komen meer producenten bij", "producenten stoppen"],
                             ["een subsidie per geproduceerd stuk", "een belasting per stuk"],
                             ["een uitzonderlijk goede oogst", "een strenge vorst vernielt de appeloogst"]])),
        ]),
        dict(kop="De prijselasticiteit van het aanbod", blokken=[
            ("kader", "<p style=\"text-align:center\"><strong>E<sub>a</sub> = procentuele verandering van de "
                      "aangeboden hoeveelheid / procentuele verandering van de prijs</strong></p>"),
            ("p", "Prijs en aangeboden hoeveelheid bewegen in dezelfde richting, dus de elasticiteit van het "
                  "aanbod is <strong>meestal positief</strong>. Stijgt de prijs met 8 % en de aangeboden "
                  "hoeveelheid met 4 %, dan is E<sub>a</sub> = 4 / 8 = <strong>0,5</strong>. Is E<sub>a</sub> = 1,5 "
                  "en stijgt de prijs met 6 %, dan stijgt de hoeveelheid met <strong>9 %</strong>."),
            ("kader", tabel(["E<sub>a</sub>", "naam", "curve"],
                            [["groter dan 1, bv. 2", "elastisch", "vlak"],
                             ["1", "unitair elastisch", "bv. een rechte door de oorsprong"],
                             ["kleiner dan 1", "inelastisch", "steil"],
                             ["0", "perfect inelastisch", "verticaal"],
                             ["oneindig", "perfect elastisch", "horizontaal"]])),
            ("p", "Bij dezelfde schaal wijst een <strong>vlakkere</strong> aanbodcurve op een elastischer aanbod. "
                  "Een voorbeeld van een perfect inelastisch aanbod: <strong>de zitplaatsen in een uitverkocht "
                  "stadion op de dag van de match</strong>. Er kunnen er niet meer bij, wat de prijs ook is."),
            ("p", "Het aanbod is elastischer als <strong>de producent voorraad heeft</strong> of als er <strong>vrije "
                  "productiecapaciteit</strong> is. Op <strong>lange termijn</strong> is het aanbod elastischer dan "
                  "op korte termijn: een bedrijf kan dan een nieuwe fabriek bouwen."),
        ]),
        dict(kop="Wat als de vraag stijgt?", blokken=[
            ("fig", svg.naast_elkaar([
                grafiek(lijnen=[(1, 8, 7, 2, "v", "V"), (3, 9, 9, 3, "g", "V′"), (1, 5, 9, 5, "a", "A")],
                        punten=[(4, 5, ""), (6, 5, "")], breedte=220, hoogte=170, titel="perfect elastisch"),
                grafiek(lijnen=[(1, 8, 7, 2, "v", "V"), (3, 9, 9, 3, "g", "V′"), (5, 1, 5, 9, "a", "A")],
                        punten=[(5, 4, ""), (5, 6, "")], breedte=220, hoogte=170, titel="perfect inelastisch")]),
             "Links stijgt enkel de hoeveelheid, rechts enkel de prijs."),
            ("p", "Hoe <strong>inelastischer het aanbod</strong>, hoe sterker de prijs stijgt als de vraag stijgt. "
                  "Bij een <strong>perfect elastisch</strong> aanbod stijgt de hoeveelheid en blijft de prijs "
                  "gelijk. Bij een <strong>perfect inelastisch</strong> aanbod stijgt de prijs en blijft de "
                  "hoeveelheid gelijk."),
        ]),
    ],
    onthoud=[
        "E_y = % verandering hoeveelheid / % verandering inkomen.",
        "Negatief: inferieur. 0: indifferent. Tussen 0 en 1: noodzakelijk. Groter dan 1: luxe.",
        "De aanbodcurve stijgt; ze is het stijgende deel van de marginale kostencurve boven de minimale GVK.",
        "Eigen prijs: beweging op de curve. Techniek, aantal producenten, grondstofprijzen, subsidies: verschuiving.",
        "E_a = % verandering aangeboden hoeveelheid / % verandering prijs; meestal positief.",
        "Verticaal = perfect inelastisch, horizontaal = perfect elastisch; op lange termijn elastischer.",
    ])


# ───────────────────────── 6. Consumenten- en producentensurplus en het welvaartsoptimum
zet("consumenten-en-producentensurplus-en-het-welvaartsoptimum",
    titel="Consumenten- en producentensurplus en het welvaartsoptimum",
    onder="Wie wint er bij een markt, hoeveel, en waarom het evenwicht het beste punt is.",
    secties=[
        dict(kop="Twee soorten surplus", blokken=[
            ("p", "Het begrip consumentensurplus werd voor het eerst gebruikt door <strong>Alfred Marshall</strong>."),
            ("p", "Het <strong>consumentensurplus</strong> is <strong>het verschil tussen wat consumenten maximaal "
                  "willen betalen en de marktprijs</strong>. Wil je maximaal 15 euro betalen voor een "
                  "concertticket en betaal je 9 euro, dan is je consumentensurplus <strong>6 euro</strong>. Een "
                  "consument die net de marktprijs wil betalen, heeft een surplus van nul. Het consumentensurplus "
                  "is dus <strong>niet</strong> het bedrag dat consumenten aan de producenten betalen."),
            ("p", "Het <strong>producentensurplus</strong> is <strong>het verschil tussen de marktprijs en de "
                  "minimumprijs waarvoor producenten willen verkopen</strong>. Wil een producent minimaal 4 euro "
                  "en verkoopt hij voor 9 euro, dan is zijn surplus <strong>5 euro</strong>. Het producentensurplus "
                  "is <strong>niet hetzelfde als de winst</strong>: de vaste kosten zijn er niet van afgetrokken."),
            ("fig", grafiek(lijnen=[(0, 10, 10, 0, "v", "V"), (0, 2, 8, 10, "a", "A")],
                            vlakken=[([(0, 10), (0, 6), (4, 6)], "v", "CS"), ([(0, 6), (0, 2), (4, 6)], "a", "PS")],
                            punten=[(4, 6, "E")], breedte=320, hoogte=220),
             "CS ligt onder de vraagcurve en boven de prijs, PS boven de aanbodcurve en onder de prijs."),
            ("p", "De <strong>totale welvaart</strong> op een markt zonder overheid is de som van het "
                  "consumentensurplus en het producentensurplus. Uit het evenwicht halen dus "
                  "<strong>consumenten die meer wilden betalen dan de prijs</strong> en <strong>producenten die "
                  "voor minder wilden verkopen dan de prijs</strong> voordeel."),
        ]),
        dict(kop="Rekenen met driehoeken", blokken=[
            ("p", "Bij rechte curven is elk surplus een driehoek: <strong>½ · basis · hoogte</strong>. De basis is de "
                  "verhandelde hoeveelheid, de hoogte het verschil tussen de prijs en het punt waar de curve de "
                  "prijsas snijdt."),
            ("kader", "<p><strong>Voorbeeld 1.</strong> Vraag P = 100 − Q, aanbod P = 20 + Q.</p>"
                      "<ul><li>Evenwicht: 100 − Q = 20 + Q, dus 2Q = 80 en <strong>Q = 40</strong>, P = 60.</li>"
                      "<li>CS = ½ · 40 · (100 − 60) = <strong>800</strong>.</li>"
                      "<li>PS = ½ · 40 · (60 − 20) = <strong>800</strong>.</li>"
                      "<li>Totale welvaart = <strong>1 600</strong>.</li></ul>"),
            ("kader", "<p><strong>Voorbeeld 2.</strong> Vraag Q<sub>v</sub> = 120 − 2P, aanbod Q<sub>a</sub> = 3P − 30.</p>"
                      "<ul><li>Evenwicht: 120 − 2P = 3P − 30, dus 5P = 150 en <strong>P = 30</strong>, Q = 60.</li>"
                      "<li>Q<sub>v</sub> = 0 bij P = 60: vanaf <strong>60</strong> wil niemand nog kopen.</li>"
                      "<li>Q<sub>a</sub> = 0 bij P = 10.</li>"
                      "<li>CS = ½ · 60 · (60 − 30) = <strong>900</strong>; PS = ½ · 60 · (30 − 10) = <strong>600</strong>; "
                      "samen <strong>1 500</strong>.</li></ul>"),
            ("p", "Zo ook: de marktprijs is 50, de vraagcurve snijdt de prijsas bij 80 en er worden 30 stuks "
                  "verhandeld. CS = ½ · 30 · 30 = <strong>450</strong>. Snijdt de aanbodcurve de prijsas bij 20, "
                  "dan is PS = ½ · 30 · 30 = <strong>450</strong>."),
        ]),
        dict(kop="Wanneer stijgt of daalt het surplus?", blokken=[
            ("kader", "<ul><li>De marktprijs <strong>daalt</strong> terwijl de curves gelijk blijven en er meer "
                      "verhandeld wordt: het consumentensurplus <strong>stijgt</strong>. Stijgt de prijs, dan wordt "
                      "het consumentensurplus <strong>kleiner</strong>.</li>"
                      "<li>De vraag stijgt (vraagcurve naar rechts): het producentensurplus <strong>stijgt</strong>.</li>"
                      "<li>Een technologische vooruitgang die het aanbod vergroot, kan zowel consumenten als "
                      "producenten meer surplus geven.</li>"
                      "<li>De aanbodcurve verschuift naar links: de totale welvaart daalt meestal.</li></ul>"),
        ]),
        dict(kop="Het welvaartsoptimum", blokken=[
            ("p", "Bij volkomen concurrentie is de totale welvaart het grootst <strong>in het marktevenwicht</strong>. "
                  "Ligt de prijs boven of onder de evenwichtsprijs, dan wordt er minder verhandeld en is de "
                  "totale welvaart kleiner. Er gaat welvaart verloren omdat <strong>er ruilen niet plaatsvinden "
                  "waarbij koper en verkoper allebei voordeel zouden hebben</strong>."),
            ("p", "Een <strong>Pareto-optimum</strong>: <strong>niemand kan beter worden zonder dat iemand anders "
                  "slechter wordt</strong>. Een <strong>Pareto-verbetering</strong> maakt minstens één persoon beter "
                  "af zonder iemand slechter af te maken. Bij volkomen concurrentie is het marktevenwicht een "
                  "Pareto-optimum. Maar een Pareto-optimum is <strong>niet altijd rechtvaardig</strong>: ook een "
                  "zeer ongelijke verdeling kan efficiënt zijn."),
            ("p", "<strong>Adam Smith</strong> sprak van <strong>de onzichtbare hand</strong>: wie zijn eigenbelang "
                  "volgt, dient via de markt ook het algemeen belang. Volgens Smith zorgt dus de markt voor het "
                  "welvaartsoptimum, en niet een overheid die overal ingrijpt."),
        ]),
    ],
    onthoud=[
        "CS = maximale betalingsbereidheid − marktprijs; PS = marktprijs − minimale verkoopprijs.",
        "CS ligt onder de vraagcurve en boven de prijs, PS boven de aanbodcurve en onder de prijs.",
        "Totale welvaart = CS + PS; een driehoek bereken je met ½ · basis · hoogte.",
        "PS is niet hetzelfde als winst; CS is niet wat je betaalt.",
        "Bij volkomen concurrentie is de welvaart het grootst in het evenwicht: een Pareto-optimum.",
        "Pareto-efficiënt is niet hetzelfde als rechtvaardig. Smith: de onzichtbare hand.",
    ])


# ───────────────────────── 7. Marktvormen en het monopolie
zet("marktvormen-en-het-monopolie",
    titel="Marktvormen en het monopolie",
    onder="Hoe het aantal aanbieders de prijs bepaalt, en hoe een monopolist zijn beste hoeveelheid kiest.",
    secties=[
        dict(kop="Marktvormen", blokken=[
            ("p", "Hoe er op een markt geconcurreerd wordt, hangt vooral af van <strong>het aantal marktpartijen</strong> "
                  "en van <strong>de toetredingsmogelijkheden</strong>: hoe gemakkelijk een nieuwe aanbieder kan "
                  "beginnen. Ook <strong>markttransparantie</strong> speelt mee: kopers en verkopers hebben een goed "
                  "overzicht van prijzen en kwaliteit."),
            ("kader", tabel(["marktvorm", "aanbieders", "invloed op de prijs"],
                            [["atomische markt (volkomen concurrentie)", "zoveel kleine aanbieders dat niemand de prijs kan beïnvloeden", "geen: prijsnemer"],
                             ["monopolistische concurrentie", "veel aanbieders van gelijkaardige maar verschillende producten", "een beetje"],
                             ["oligopolie", "enkele grote aanbieders", "veel"],
                             ["monopolie", "één aanbieder van een product zonder goede vervangers", "groot: prijszetter"]])),
            ("p", "Een monopolie ontstaat bijvoorbeeld als <strong>één spoorbedrijf als enige een net mag uitbaten</strong> "
                  "of als <strong>een farmabedrijf een patent heeft op een geneesmiddel</strong>. De toetredingsmogelijkheden "
                  "voor nieuwe aanbieders zijn dan <strong>klein</strong>."),
        ]),
        dict(kop="Kosten op een rij", blokken=[
            ("kader", tabel(["afkorting", "betekenis"],
                            [["TCK", "totale constante kosten: veranderen niet als de productie verandert"],
                             ["TVK", "totale variabele kosten: stijgen met de productie"],
                             ["TK", "totale kosten = TCK + TVK"],
                             ["GK", "gemiddelde kosten = TK / Q = GCK + GVK"],
                             ["GCK", "gemiddelde constante kosten = TCK / Q; dalen als Q stijgt"],
                             ["GVK", "gemiddelde variabele kosten = TVK / Q"],
                             ["MK", "marginale kosten: de extra kosten van één stuk meer maken"]])),
            ("p", "Voorbeeld: TCK = 200 en TVK = 400 bij 20 stuks. Dan is GK = 600 / 20 = <strong>30</strong>. "
                  "Kost 10 stuks 500 euro en 11 stuks 540 euro, dan zijn de marginale kosten van het elfde stuk "
                  "<strong>40 euro</strong>."),
            ("p", "De MK-curve verloopt meestal <strong>eerst dalend, daarna stijgend</strong>, en ze snijdt de "
                  "GK-curve <strong>in haar laagste punt</strong>."),
        ]),
        dict(kop="De opbrengsten van een monopolist", blokken=[
            ("p", "Een monopolist is een <strong>prijszetter</strong>: hij kiest zelf de prijs. Maar hij kan niet "
                  "eender welke prijs vragen en toch evenveel verkopen. Zijn <strong>prijsafzetcurve is dalend</strong>: "
                  "het is de vraagcurve van de hele markt."),
            ("kader", "<p>Prijsafzetcurve <strong>P = 100 − 2Q</strong>.</p>"
                      "<ul><li>Totale opbrengst: TO = P · Q = <strong>100Q − 2Q²</strong>.</li>"
                      "<li>Gemiddelde opbrengst: GO = TO / Q = P. Bij een monopolist is GO <strong>gelijk aan de prijs</strong>.</li>"
                      "<li>Marginale opbrengst: <strong>MO = 100 − 4Q</strong>. De MO-curve ligt <strong>onder</strong> de "
                      "prijsafzetcurve en daalt <strong>twee keer zo snel</strong>. MO is dus <strong>niet</strong> gelijk aan de prijs.</li>"
                      "<li>TO is het grootst waar MO = 0, dus bij <strong>Q = 25</strong>.</li></ul>"),
            ("p", "Bij volkomen concurrentie is het anders: daar zijn de marginale opbrengsten van een producent "
                  "<strong>gelijk aan de marktprijs</strong>, want hij kan zoveel verkopen als hij wil aan die prijs."),
        ]),
        dict(kop="De optimale productiegrootte", blokken=[
            ("p", "Een monopolist maakt de meeste winst <strong>waar MO = MK</strong>. Dat is niet de hoeveelheid met de "
                  "grootste totale opbrengst: hij moet ook naar zijn kosten kijken."),
            ("fig", grafiek(lijnen=[(0, 10, 9, 1, "v", "P"), (0, 10, 4.5, 1, "a", "MO"), (0, 2, 10, 2, "g", "MK")],
                            vlakken=[([(4, 6), (4, 2), (8, 2)], "a", "")],
                            punten=[(4, 6, "monopolie"), (8, 2, "")], breedte=340, hoogte=230),
             "P = 100 − 2Q, MO = 100 − 4Q, MK = 20. Het gekleurde driehoekje is het welvaartsverlies."),
            ("kader", "<p><strong>Rekenvoorbeeld.</strong> P = 100 − 2Q en MK = 20.</p>"
                      "<ul><li>MO = MK: 100 − 4Q = 20, dus <strong>Q = 20</strong>.</li>"
                      "<li>De prijs lees je af <strong>boven het snijpunt van MO en MK, op de prijsafzetcurve</strong>: "
                      "P = 100 − 2 · 20 = <strong>60</strong>.</li>"
                      "<li>Winst = (P − GK) · Q. Met GK = 30: (60 − 30) · 20 = <strong>600</strong>. In de grafiek is dat "
                      "de rechthoek tussen de prijs en de GK, over de breedte van de verkochte hoeveelheid.</li></ul>"),
        ]),
        dict(kop="Monopolie tegenover volkomen concurrentie", blokken=[
            ("p", "Bij volkomen concurrentie zou de prijs gelijk zijn aan MK: 100 − 2Q = 20, dus <strong>Q = 40</strong> en "
                  "P = 20. De monopolist vraagt dus <strong>een hogere prijs voor een kleinere hoeveelheid</strong>."),
            ("p", "Daardoor <strong>daalt het consumentensurplus</strong>. Een deel ervan gaat naar de monopolist, en een "
                  "deel verdwijnt helemaal: het <strong>welvaartsverlies</strong>, de welvaart die niemand krijgt, niet de "
                  "consument en niet de producent. Hier is dat de driehoek ½ · (40 − 20) · (60 − 20) = <strong>400</strong>. "
                  "Het gaat dus niet zo dat er producentensurplus naar de consument gaat; het omgekeerde gebeurt."),
            ("weetje", "Daarom vinden economen een monopolie ongunstig voor de welvaart: er wordt minder verhandeld aan "
                       "een hogere prijs dan bij volkomen concurrentie."),
        ]),
    ],
    onthoud=[
        "Marktvorm hangt af van het aantal aanbieders en de toetredingsmogelijkheden.",
        "Monopolie: één aanbieder, geen goede vervangers, prijszetter, dalende prijsafzetcurve.",
        "GK = GCK + GVK; GCK daalt als Q stijgt; MK snijdt GK in haar laagste punt.",
        "Bij P = a − bQ is MO = a − 2bQ: onder de prijsafzetcurve, twee keer zo steil.",
        "Optimale productie: MO = MK; de prijs lees je af op de prijsafzetcurve. Winst = (P − GK) · Q.",
        "Monopolie: hogere prijs, kleinere hoeveelheid, minder consumentensurplus en een welvaartsverlies.",
    ])


def matrix(a, b, cellen, rij="A", kol="B"):
    """Een uitbetalingsmatrix: cellen[i][j] = (winst rij, winst kolom)."""
    th = ("border:1px solid #e4ded0;background:rgba(47,93,80,.09);padding:6px 10px;"
          "color:#234539;font-weight:600;")
    td = "border:1px solid #e4ded0;padding:6px 10px;text-align:center;"
    h = (f'<table style="border-collapse:collapse;margin:0 auto;font-size:10.5pt;">'
         f'<tr><th style="{th}"></th>' + "".join(f'<th style="{th}">{kol} {k}</th>' for k in b) + "</tr>")
    for i, r in enumerate(a):
        h += f'<tr><th style="{th}">{rij} {r}</th>' + "".join(
            f'<td style="{td}">{x} ; {y}</td>' for x, y in cellen[i]) + "</tr>"
    return h + "</table>"


# ───────────────────────── 8. Monopolistische concurrentie, oligopolie en speltheorie
zet("monopolistische-concurrentie-oligopolie-en-speltheorie",
    titel="Monopolistische concurrentie, oligopolie en speltheorie",
    onder="De marktvormen tussen volkomen concurrentie en monopolie, en hoe bedrijven elkaars zetten voorspellen.",
    secties=[
        dict(kop="Monopolistische concurrentie", blokken=[
            ("p", "Bij monopolistische concurrentie zijn er <strong>veel aanbieders van gelijkaardige maar verschillende "
                  "producten</strong>. Denk aan honderden restaurants in een stad, elk met een eigen keuken en sfeer. De "
                  "toetredingsdrempels zijn <strong>laag</strong>."),
            ("p", "Omdat elk product een beetje anders is, heeft elke aanbieder <strong>een dalende prijsafzetcurve</strong>. "
                  "Bedrijven doen veel aan <strong>reclame</strong>, om hun product te onderscheiden van dat van de concurrent."),
            ("kader", "<ul><li><strong>Korte termijn:</strong> zoals een monopolist produceert hij waar <strong>MO = MK</strong>, "
                      "en hij kan winst maken.</li>"
                      "<li><strong>Lange termijn:</strong> door die winst <strong>treden nieuwe aanbieders toe</strong>, tot "
                      "de winst verdwenen is. De prijsafzetcurve raakt dan de GK-curve: <strong>de prijs is gelijk aan "
                      "de gemiddelde kosten, dus de winst is nul</strong>.</li></ul>"),
        ]),
        dict(kop="Oligopolie", blokken=[
            ("p", "Bij een oligopolie zijn er <strong>enkele grote aanbieders die van elkaar afhankelijk zijn</strong>, met "
                  "<strong>hoge toetredingsdrempels</strong>. Voorbeelden: de drie grote operatoren voor mobiele "
                  "abonnementen in België, of twee grote vliegtuigbouwers die de wereldmarkt verdelen. Oligopolisten "
                  "houden bij elke beslissing <strong>rekening met de reactie van hun concurrenten</strong>."),
            ("p", "Monopolie, oligopolie en monopolistische concurrentie hebben iets gemeen: <strong>de aanbieders hebben "
                  "wat invloed op de prijs</strong> en <strong>de prijsafzetcurve van een aanbieder daalt</strong>. De "
                  "meest elastische prijsafzetcurve voor één aanbieder vind je bij <strong>volkomen concurrentie</strong>: "
                  "die is horizontaal."),
        ]),
        dict(kop="De geknikte prijsafzetcurve", blokken=[
            ("fig", grafiek(lijnen=[(0, 7, 5, 6, "v", ""), (5, 6, 7.5, 1, "v", "P"), (0, 7, 5, 5, "a", ""),
                                    (5, 3.2, 6.4, 0.6, "a", "MO"), (5, 5, 5, 3.2, "g", "")],
                            punten=[(5, 6, "knik")], breedte=320, hoogte=220),
             "Boven de knik is de vraag elastisch, eronder inelastisch. De MO-curve maakt een sprong."),
            ("p", "Bij oligopolie is er vaak <strong>prijsstarheid</strong>: de prijs blijft lang gelijk, ook als de kosten "
                  "veranderen. De verklaring is de <strong>geknikte prijsafzetcurve</strong>: "
                  "<strong>concurrenten volgen wel een prijsdaling, maar geen prijsstijging</strong>."),
            ("kader", "<ul><li>Verhoogt één bedrijf zijn prijs, dan volgen de anderen niet en verliest het veel klanten: "
                      "<strong>boven de knik is de vraag elastisch</strong>.</li>"
                      "<li>Verlaagt het de prijs, dan volgen de anderen meteen en wint het weinig klanten: <strong>onder "
                      "de knik is de vraag inelastisch</strong>.</li>"
                      "<li>Door de knik maakt <strong>de MO-curve een sprong</strong>. Schuift de MK-curve een beetje, dan "
                      "snijdt ze MO nog altijd in die sprong: de prijs verandert niet.</li></ul>"),
            ("p", "Zo verklaar je ook twee tankstations naast elkaar: verlaagt het ene de prijs, dan volgt het andere "
                  "meteen; verhoogt het de prijs, dan volgt het andere niet."),
        ]),
        dict(kop="Kartels", blokken=[
            ("p", "Een <strong>kartel</strong> is <strong>een afspraak tussen aanbieders over prijzen of markten</strong>. In "
                  "de Europese Unie zijn kartelafspraken <strong>verboden</strong>, ook als ze geheim blijven."),
        ]),
        dict(kop="Speltheorie", blokken=[
            ("p", "Speltheorie bestudeert beslissingen waarbij <strong>je uitkomst afhangt van wat de ander doet</strong>. "
                  "Ze is dus vooral nuttig bij oligopolie, niet bij volkomen concurrentie."),
            ("kader", tabel(["begrip", "betekenis"],
                            [["best-response strategie", "de beste keuze voor een speler, gegeven wat de andere speler doet"],
                             ["dominante strategie", "een strategie die het beste is, wat de andere speler ook doet"],
                             ["Nash-evenwicht", "geen speler wint iets door in zijn eentje te veranderen; niemand heeft spijt van zijn keuze, gegeven wat de ander deed"],
                             ["gevangenendilemma", "eigenbelang leidt tot een slechtere uitkomst voor beide"]])),
            ("fig", matrix(["hoog", "laag"], ["hoog", "laag"], [[(10, 10), (2, 15)], [(15, 2), (5, 5)]]),
             "Winst van A ; winst van B bij een hoge of lage prijs."),
            ("kader", "<ul><li>Kiest B hoog, dan is laag het beste voor A (15 &gt; 10). Kiest B laag, dan ook (5 &gt; 2). "
                      "Laag is dus een <strong>dominante strategie</strong> voor A, en net zo voor B.</li>"
                      "<li>Het <strong>Nash-evenwicht</strong> is <strong>beide laag</strong>: elk 5.</li>"
                      "<li>Samen zouden ze meer halen met beide hoog (elk 10). Het Nash-evenwicht geeft dus "
                      "<strong>niet</strong> de hoogste winst samen: dat is het gevangenendilemma.</li></ul>"),
            ("p", "Zo verklaart speltheorie waarom bedrijven <strong>een kartel willen</strong>: samen een hoge prijs afspreken "
                  "levert elk meer op dan het Nash-evenwicht. En ook waarom een kartel <strong>vaak niet stabiel</strong> is: "
                  "<strong>elk lid wint erbij door stiekem een lagere prijs te vragen</strong>."),
            ("p", "Een spel kan ook een Nash-evenwicht hebben <strong>zonder</strong> dat een speler een dominante strategie heeft."),
        ]),
    ],
    onthoud=[
        "Monopolistische concurrentie: veel aanbieders, verschillende producten, lage drempels; op lange termijn winst nul.",
        "Oligopolie: enkele grote aanbieders, hoge drempels, afhankelijk van elkaars reactie.",
        "Geknikte prijsafzetcurve: een daling wordt gevolgd, een stijging niet; daardoor prijsstarheid.",
        "Een kartel is een prijs- of marktafspraak en is in de EU verboden.",
        "Dominante strategie: altijd de beste. Nash-evenwicht: niemand wint iets door alleen te veranderen.",
        "Gevangenendilemma: eigenbelang geeft beide een slechtere uitkomst; daarom zijn kartels onstabiel.",
    ])


# ───────────────────────── 9. Prijsregulering, quota, belastingen en subsidies
zet("prijsregulering-quota-belastingen-en-subsidies",
    titel="Prijsregulering, quota, belastingen en subsidies",
    onder="Wat er gebeurt als de overheid ingrijpt op een markt, en wie daarvoor betaalt.",
    secties=[
        dict(kop="Waarom grijpt de overheid in?", blokken=[
            ("p", "Soms vindt de overheid <strong>de marktprijs of de hoeveelheid niet wenselijk</strong>: huren die te hoog "
                  "zijn, boeren die te weinig verdienen, een product dat ongezond is. Ze kan dan ingrijpen met een "
                  "maximumprijs, een minimumprijs, een quotum, een belasting of een subsidie."),
            ("kader", "<p>In dit thema rekenen we telkens met dezelfde markt:</p>"
                      "<p style=\"text-align:center\"><strong>Q<sub>v</sub> = 100 − P</strong> en "
                      "<strong>Q<sub>a</sub> = P − 20</strong>, met evenwicht <strong>P = 60</strong> en <strong>Q = 40</strong>.</p>"),
        ]),
        dict(kop="Maximumprijs en minimumprijs", blokken=[
            ("p", "Een <strong>maximumprijs</strong> heeft enkel effect <strong>als ze onder de evenwichtsprijs ligt</strong>. "
                  "Een maximumprijs boven de evenwichtsprijs verandert niets."),
            ("fig", grafiek(lijnen=[(0, 10, 10, 0, "v", "V"), (0, 2, 8, 10, "a", "A"), (0, 5, 7, 5, "g", "max 50")],
                            vlakken=[([(3, 7), (3, 5), (4, 6)], "a", "")],
                            punten=[(3, 5, ""), (5, 5, "")], breedte=330, hoogte=230),
             "Bij 50 bieden producenten 30 aan en willen kopers 50: een tekort van 20."),
            ("kader", "<p><strong>Maximumprijs van 50.</strong></p><ul>"
                      "<li>Q<sub>v</sub> = 100 − 50 = 50 en Q<sub>a</sub> = 50 − 20 = 30: een <strong>tekort</strong> van <strong>20</strong>.</li>"
                      "<li>Er wordt maar <strong>30</strong> verhandeld, minder dan in het evenwicht. Bij Q = 30 willen kopers 70 "
                      "betalen. Het welvaartsverlies is de driehoek ½ · (40 − 30) · (70 − 50) = <strong>100</strong>.</li></ul>"),
            ("p", "Gevolgen van een maximumprijs: <strong>wachtrijen</strong> (er zijn meer kopers dan goederen aan die prijs) "
                  "en een <strong>zwarte markt</strong>. Een maximumhuurprijs ver onder de marktprijs geeft op lange termijn "
                  "<strong>minder huurwoningen en lange wachtlijsten</strong>."),
            ("p", "Een <strong>minimumprijs</strong> heeft enkel effect <strong>als ze boven de evenwichtsprijs ligt</strong>. Ze "
                  "wordt vaak gebruikt om <strong>producenten, zoals landbouwers, te beschermen</strong>. Bij een minimumprijs van "
                  "70 is Q<sub>v</sub> = 30 en Q<sub>a</sub> = 50: een <strong>overschot</strong> van <strong>20</strong>. Er wordt "
                  "minder verhandeld dan in het evenwicht, dus de totale welvaart stijgt <strong>niet</strong>. Het overschot "
                  "<strong>koopt de overheid vaak op</strong> en slaat ze op of verwerkt ze."),
        ]),
        dict(kop="Een productiequotum", blokken=[
            ("p", "Een <strong>productiequotum</strong> is <strong>een maximale hoeveelheid die mag worden geproduceerd</strong>. "
                  "Ligt het onder de evenwichtshoeveelheid, dan <strong>stijgt de prijs en wordt er minder verhandeld</strong>, met "
                  "een welvaartsverlies."),
            ("p", "Quotum van 30: kopers willen dan 100 − 30 = <strong>70</strong> betalen. Volgens hun aanbodcurve zouden de "
                  "producenten bij 30 stuks maar 50 vragen. <strong>De producenten met een quotum winnen</strong>: ze krijgen een "
                  "hogere prijs."),
        ]),
        dict(kop="Een belasting per stuk", blokken=[
            ("p", "<strong>Indirecte belastingen</strong> zijn belastingen op goederen, zoals <strong>de btw</strong> en "
                  "<strong>accijnzen op tabak</strong>. Een belasting per stuk bij de producent doet de aanbodcurve <strong>naar "
                  "boven (naar links)</strong> verschuiven, met het bedrag van de belasting. Niet naar rechts."),
            ("fig", grafiek(lijnen=[(0, 10, 10, 0, "v", "V"), (0, 2, 8, 10, "g", "A"), (0, 3, 7, 10, "a", "A + t")],
                            vlakken=[([(3.5, 6.5), (3.5, 5.5), (4, 6)], "a", "")],
                            punten=[(3.5, 6.5, "65"), (3.5, 5.5, "55")], breedte=330, hoogte=230),
             "Belasting 10: de koper betaalt 65, de producent houdt 55 over."),
            ("kader", "<p><strong>Belasting van 10 euro per stuk.</strong> Het nieuwe aanbod is Q<sub>a</sub> = P − 30.</p><ul>"
                      "<li>100 − P = P − 30, dus de koper betaalt <strong>P = 65</strong> en Q = <strong>35</strong>.</li>"
                      "<li>De producent houdt per stuk 65 − 10 = <strong>55</strong> over.</li>"
                      "<li>De overheid ontvangt 10 · 35 = <strong>350</strong>. Die ontvangsten zijn <strong>geen</strong> "
                      "welvaartsverlies: ze gaan naar de overheid.</li>"
                      "<li>Welvaartsverlies: de driehoek tussen vraag en aanbod, van de nieuwe tot de oude hoeveelheid: "
                      "½ · (40 − 35) · 10 = <strong>25</strong>.</li></ul>"),
            ("p", "Wie draagt de belasting? Hier allebei de helft: de koper 5 meer, de producent 5 minder. De consument draagt "
                  "dus niet altijd alles. Is de vraag <strong>heel inelastisch</strong>, dan dragen <strong>de consumenten</strong> "
                  "het grootste deel. Is de vraag <strong>heel elastisch</strong>, dan <strong>de producenten</strong>. Hoe "
                  "<strong>elastischer</strong> vraag en aanbod, hoe <strong>groter</strong> het welvaartsverlies."),
        ]),
        dict(kop="Een subsidie per stuk", blokken=[
            ("p", "Een subsidie per stuk aan de producent doet de aanbodcurve <strong>naar rechts</strong> schuiven: <strong>een "
                  "lagere prijs en een grotere hoeveelheid</strong>. De consumenten betalen minder dan in het oorspronkelijke "
                  "evenwicht."),
            ("p", "Subsidie van 10: het nieuwe aanbod is Q<sub>a</sub> = P − 10. 100 − P = P − 10 geeft P = 55 en "
                  "<strong>Q = 45</strong>. De subsidie kost de overheid 10 · 45 = <strong>450</strong>."),
            ("weetje", "Ook een subsidie veroorzaakt op een competitieve markt zonder externe effecten een welvaartsverlies: "
                       "er wordt meer gemaakt dan wat kopers waard vinden."),
        ]),
    ],
    onthoud=[
        "Maximumprijs werkt enkel onder het evenwicht: tekort, wachtrijen, zwarte markt.",
        "Minimumprijs werkt enkel boven het evenwicht: overschot, vaak opgekocht door de overheid.",
        "Quotum onder het evenwicht: hogere prijs, minder verhandeld, welvaartsverlies.",
        "Belasting per stuk: aanbod naar boven/links; koper betaalt meer, producent houdt minder over.",
        "Belastingontvangsten zijn geen welvaartsverlies; het verlies is de driehoek tussen oude en nieuwe hoeveelheid.",
        "Inelastische vraag: de consument draagt het meest. Subsidie: aanbod naar rechts, lagere prijs.",
    ])


# ───────────────────────── 10. Marktmacht, marktfalen, externe effecten en publieke goederen
zet("marktmacht-marktfalen-externe-effecten-en-publieke-goederen",
    titel="Marktmacht, marktfalen, externe effecten en publieke goederen",
    onder="Wanneer de vrije markt niet tot het beste resultaat leidt, en wat de overheid dan kan doen.",
    secties=[
        dict(kop="Marktfalen", blokken=[
            ("p", "Er is <strong>marktfalen</strong> als de vrije markt niet tot de grootste welvaart leidt. Oorzaken zijn "
                  "<strong>marktmacht</strong>, <strong>externe effecten</strong>, <strong>asymmetrische informatie</strong> en "
                  "<strong>publieke goederen</strong>."),
            ("p", "<strong>Marktmacht</strong> (zoals bij een monopolie) zorgt ervoor dat <strong>er minder verhandeld wordt aan "
                  "een hogere prijs</strong>. Een <strong>patent of octrooi</strong> geeft zo'n tijdelijke marktmacht: de overheid "
                  "geeft het <strong>om uitvinders tijdelijk te belonen</strong>. Een patent zorgt dus net voor <strong>minder</strong> "
                  "concurrentie op de markt van die uitvinding."),
        ]),
        dict(kop="Externe effecten", blokken=[
            ("kader", tabel(["", "negatief extern effect", "positief extern effect"],
                            [["wat", "schade aan derden die niet in de marktprijs zit", "voordeel voor derden dat niet in de marktprijs zit"],
                             ["voorbeeld", "een fabriek die de lucht vervuilt", "bijen van een imker die ook de buren bestuiven; een vaccin dat ook niet-gevaccineerden beschermt"],
                             ["vrije markt", "produceert <strong>te veel</strong>", "produceert <strong>te weinig</strong>"],
                             ["overheid", "Pigouviaanse heffing, emissierechten, normen", "subsidies, gratis aanbieden"]])),
            ("fig", grafiek(lijnen=[(0, 10, 10, 0, "v", "V"), (0, 2, 7.5, 9.5, "g", "privé"), (0, 4, 4.8, 8.8, "a", "maatsch.")],
                            vlakken=[([(3, 7), (4, 8), (4, 6)], "a", "")],
                            punten=[(3, 7, "optimum"), (4, 6, "markt")], breedte=340, hoogte=230),
             "Privé = de kost voor de producent, maatsch. = de maatschappelijke kost, met de schade aan derden erbij. De markt produceert tot het snijpunt met de privékost. Het welvaartsverlies is de driehoek voorbij het maatschappelijk optimum."),
            ("p", "Bij een negatief extern effect is de <strong>maatschappelijke kost hoger dan de privékost</strong> van de "
                  "producent. De vervuiler betaalt op een vrije markt <strong>niet</strong> automatisch voor de schade aan de buren. "
                  "Daardoor is de vrije marktprijs <strong>te laag</strong> en wordt er te veel geproduceerd. Het welvaartsverlies "
                  "ligt <strong>in de driehoek voorbij het maatschappelijk optimum</strong>."),
        ]),
        dict(kop="Wat kan de overheid doen?", blokken=[
            ("kader", "<ul><li><strong>Pigouviaanse heffing:</strong> een belasting <strong>gelijk aan de schade aan derden</strong>. "
                      "Veroorzaakt elk stuk 5 euro schade, dan is de heffing 5 euro per stuk. <strong>De prijs stijgt en de "
                      "hoeveelheid daalt</strong>, tot het maatschappelijk optimum. Zo <strong>verkleint</strong> het welvaartsverlies.</li>"
                      "<li><strong>Emissiehandel:</strong> bedrijven <strong>kopen en verkopen beperkte uitstootrechten</strong>. "
                      "Wie goedkoop minder kan uitstoten, verkoopt zijn rechten. Zo wordt de uitstoot verminderd <strong>waar dat "
                      "het goedkoopst kan</strong>.</li>"
                      "<li><strong>Regulering:</strong> bijvoorbeeld een <strong>uitstootnorm voor nieuwe auto's</strong>.</li>"
                      "<li><strong>Subsidies</strong> voor positieve externe effecten.</li></ul>"),
        ]),
        dict(kop="Asymmetrische informatie", blokken=[
            ("p", "Er is <strong>asymmetrische informatie</strong> als <strong>de ene partij meer weet dan de andere</strong>. Een "
                  "verkoper van een tweedehandsauto kent de gebreken, de koper niet. Kopers willen dan niet veel betalen, en "
                  "daardoor kunnen <strong>goede producten van de markt verdwijnen</strong>. De overheid beperkt dat met "
                  "<strong>etiketten, keuringen en garanties</strong>."),
        ]),
        dict(kop="Publieke goederen", blokken=[
            ("kader", tabel(["soort goed", "rivaliserend?", "uitsluitbaar?", "voorbeeld"],
                            [["privaat goed", "ja", "ja", "een broodje"],
                             ["zuiver publiek goed", "nee", "nee", "straatverlichting, landsverdediging, een dijk die een stad beschermt"],
                             ["quasipubliek goed", "deels", "deels", "onderwijs"]])),
            ("p", "<strong>Niet-rivaliserend</strong>: als ik het gebruik, kan jij het nog evengoed gebruiken. <strong>Niet-uitsluitbaar</strong>: "
                  "wie niet betaalt, kan je niet tegenhouden. De vrije markt biedt zuiver publieke goederen daarom niet of te "
                  "weinig aan: <strong>niemand kan verplicht worden te betalen, dus mensen liften mee</strong>. Een "
                  "<strong>meelifter</strong> (free rider) is iemand die gebruikt zonder te betalen."),
            ("p", "Een <strong>collectieve behoefte</strong> is een behoefte die je <strong>best samen invult</strong>, zoals veiligheid. "
                  "Daarom zorgt de overheid ervoor, betaald met belastingen."),
        ]),
        dict(kop="Mededinging bewaken", blokken=[
            ("kader", tabel(["wie", "wat"],
                            [["Belgische Mededingingsautoriteit (BMA)", "spoort kartels en machtsmisbruik op en kan boetes opleggen voor prijsafspraken"],
                             ["Dienst voor Mededinging (FOD Economie)", "bewaakt eerlijke concurrentie in België"],
                             ["Europese Commissie", "voert het antitrustbeleid van de EU uit"]])),
            ("p", "Het Europese mededingingsrecht verbiedt <strong>kartelafspraken tussen bedrijven</strong> en <strong>misbruik van "
                  "een dominante positie</strong>. Een groot marktaandeel op zich is <strong>niet</strong> verboden; het misbruik ervan wel."),
        ]),
    ],
    onthoud=[
        "Marktfalen: marktmacht, externe effecten, asymmetrische informatie, publieke goederen.",
        "Negatief extern effect: te veel geproduceerd, prijs te laag. Positief: te weinig geproduceerd.",
        "Pigouviaanse heffing = de schade aan derden per stuk; emissiehandel verdeelt beperkte uitstootrechten.",
        "Asymmetrische informatie: de ene partij weet meer; etiketten, keuringen en garanties helpen.",
        "Zuiver publiek goed: niet-rivaliserend en niet-uitsluitbaar; meeliften; de overheid zorgt ervoor.",
        "BMA en Europese Commissie bestraffen kartels en misbruik van een dominante positie.",
    ])


# ───────────────────────── 11. De arbeidsmarkt, werkloosheid en arbeidsmarktindicatoren
zet("de-arbeidsmarkt-werkloosheid-en-arbeidsmarktindicatoren",
    titel="De arbeidsmarkt, werkloosheid en arbeidsmarktindicatoren",
    onder="Vraag en aanbod van arbeid, hoe je werkloosheid meet, en wat ertegen helpt.",
    secties=[
        dict(kop="Vraag en aanbod van arbeid", blokken=[
            ("p", "Op de arbeidsmarkt is het een beetje omgekeerd: <strong>de werkgevers vragen arbeid</strong>, de werknemers "
                  "bieden arbeid aan. De prijs van arbeid is het loon."),
            ("fig", grafiek(lijnen=[(1, 9, 9, 1, "v", "vraag"), (1, 1, 9, 9, "a", "aanbod"), (0, 7, 9, 7, "g", "")],
                            punten=[(5, 5, "evenwicht"), (3, 7, ""), (7, 7, "")],
                            xlabel="arbeid", ylabel="loon", breedte=330, hoogte=220),
             "Een loon boven het evenwicht: meer aanbod dan vraag, dus werkloosheid."),
            ("kader", "<ul><li>De <strong>vraagcurve daalt</strong>: bij een hoger loon vragen werkgevers minder arbeid.</li>"
                      "<li>De <strong>aanbodcurve stijgt</strong>: bij een hoger loon willen meer mensen werken.</li>"
                      "<li>Het snijpunt geeft <strong>het evenwichtsloon en de evenwichtstewerkstelling</strong>.</li></ul>"),
            ("p", "Ligt het loon <strong>boven</strong> het evenwichtsloon, bijvoorbeeld door een hoog minimumloon, dan ontstaat er "
                  "<strong>werkloosheid</strong>. Bieden bij 15 euro per uur 900 mensen arbeid aan en vragen werkgevers er 700, "
                  "dan zijn er <strong>200</strong> werklozen. Ligt het loon <strong>onder</strong> het evenwichtsloon, dan is er een "
                  "<strong>tekort aan arbeidskrachten</strong>."),
        ]),
        dict(kop="Arbeidsmarktindicatoren", blokken=[
            ("p", "De <strong>beroepsbevolking</strong> zijn <strong>de werkenden en de werklozen</strong> samen. Een gepensioneerde of "
                  "een voltijdse student hoort er niet bij."),
            ("kader", tabel(["indicator", "formule"],
                            [["activiteitsgraad", "beroepsbevolking / bevolking op arbeidsleeftijd"],
                             ["werkzaamheidsgraad", "werkenden / bevolking op arbeidsleeftijd"],
                             ["werkloosheidsgraad", "werklozen / <strong>beroepsbevolking</strong> (niet de hele bevolking)"]])),
            ("kader", "<p><strong>Voorbeeld.</strong> 1 000 000 mensen op arbeidsleeftijd, 700 000 werkenden en 50 000 werklozen.</p><ul>"
                      "<li>Beroepsbevolking: 750 000. Activiteitsgraad: 750 000 / 1 000 000 = <strong>75 %</strong>.</li>"
                      "<li>Werkzaamheidsgraad: 700 000 / 1 000 000 = <strong>70 %</strong>.</li>"
                      "<li>Werkloosheidsgraad: 50 000 / 750 000 = <strong>6,7 %</strong>.</li></ul>"
                      "<p>Beroepsbevolking 5 miljoen en 400 000 werklozen: werkloosheidsgraad <strong>8 %</strong>.</p>"),
            ("p", "De werkzaamheidsgraad is dus <strong>nooit hoger</strong> dan de activiteitsgraad, want de werkenden zijn een deel van "
                  "de beroepsbevolking. Opgelet: als <strong>ontmoedigde werklozen stoppen met zoeken</strong>, tellen ze niet meer mee "
                  "in de beroepsbevolking. De werkloosheidsgraad kan dan dalen zonder dat er meer mensen werken."),
        ]),
        dict(kop="Soorten werkloosheid", blokken=[
            ("kader", tabel(["soort", "wat", "voorbeeld"],
                            [["frictiewerkloosheid", "korte werkloosheid tussen twee jobs", "iemand die net ontslag nam en volgende maand ergens anders begint"],
                             ["seizoenswerkloosheid", "werk dat maar een deel van het jaar bestaat", "een skileraar in de zomer"],
                             ["conjuncturele werkloosheid", "werkloosheid door een laagconjunctuur", "een recessie: bedrijven verkopen minder en ontslaan mensen"],
                             ["structurele werkloosheid", "het profiel van werkzoekenden past niet bij de vacatures", "veel werklozen én veel openstaande vacatures"],
                             ["technische werkloosheid", "machines nemen het werk over", "kassiers vervangen door zelfscankassa's"]])),
            ("p", "Er kunnen dus wel degelijk <strong>veel werklozen en tegelijk veel openstaande vacatures</strong> zijn. Een "
                  "<strong>knelpuntberoep</strong> is een beroep waarvoor werkgevers moeilijk mensen vinden."),
        ]),
        dict(kop="Wat helpt?", blokken=[
            ("kader", tabel(["maatregel", "werkt op", "vooral tegen"],
                            [["omscholing en opleiding van werkzoekenden", "het aanbod van arbeid", "structurele werkloosheid"],
                             ["een vacaturedatabank die werkzoekenden en werkgevers sneller samenbrengt", "het zoeken", "frictiewerkloosheid"],
                             ["de bestedingen stimuleren in een recessie", "de vraag naar goederen, dus naar arbeid", "conjuncturele werkloosheid"],
                             ["lagere werkgeversbijdragen voor sociale zekerheid, loonsubsidies bij aanwerving van langdurig werklozen", "de <strong>vraag</strong> naar arbeid", "werkloosheid door hoge loonkosten"],
                             ["een hogere werkbonus, zodat werken lonender is dan een uitkering", "het <strong>aanbod</strong> van arbeid", "inactiviteit"]])),
        ]),
        dict(kop="Lonen in België", blokken=[
            ("p", "Door de <strong>automatische loonindexering</strong> stijgen de lonen automatisch mee met de prijzen. Dat "
                  "<strong>beschermt de koopkracht</strong> van werknemers. Maar bij inflatie <strong>stijgen ook de loonkosten</strong> "
                  "voor bedrijven, en dat raakt hun concurrentiekracht."),
            ("p", "Daarom is er de <strong>loonnorm</strong>: <strong>de maximale loonstijging bovenop de index</strong>. Ze bestaat "
                  "<strong>om de concurrentiekracht van Belgische bedrijven te beschermen</strong> tegenover de buurlanden."),
        ]),
    ],
    onthoud=[
        "Werkgevers vragen arbeid (dalende curve), werknemers bieden aan (stijgende curve).",
        "Loon boven het evenwicht: werkloosheid. Loon onder het evenwicht: tekort aan arbeidskrachten.",
        "Beroepsbevolking = werkenden + werklozen.",
        "Activiteitsgraad = beroepsbevolking / arbeidsleeftijd; werkzaamheidsgraad = werkenden / arbeidsleeftijd; werkloosheidsgraad = werklozen / beroepsbevolking.",
        "Frictie, seizoen, conjunctureel, structureel, technisch: elk met een eigen oplossing.",
        "Indexering beschermt de koopkracht; de loonnorm beschermt de concurrentiekracht.",
    ])


# ───────────────────────── 12. Geld, monetaire aggregaten en geldschepping
zet("geld-monetaire-aggregaten-en-geldschepping",
    titel="Geld, monetaire aggregaten en geldschepping",
    onder="Waarvoor geld dient, welke soorten er zijn, en hoe banken nieuw geld maken.",
    secties=[
        dict(kop="Waarom geld?", blokken=[
            ("p", "Bij <strong>ruilhandel</strong> zonder geld moest je <strong>iemand vinden die wilde wat jij had</strong> en die "
                  "tegelijk had wat jij wilde. Geld lost dat op. Papieren biljetten hebben zelf weinig waarde: mensen aanvaarden "
                  "ze omdat <strong>ze vertrouwen dat anderen ze ook aanvaarden</strong>."),
            ("kader", tabel(["functie", "voorbeeld"],
                            [["ruil- en betaalmiddel", "je betaalt een broodje"],
                             ["waardemeter en rekeneenheid", "elke prijs staat in euro, zodat je kan vergelijken"],
                             ["spaar- en beleggingsmiddel", "je zet elke maand 50 euro opzij"],
                             ["kredietmiddel", "een bank leent geld aan een gezin dat een huis koopt"]])),
            ("p", "Een <strong>hoge inflatie</strong> tast vooral de functie als <strong>spaarmiddel</strong> aan: je gespaarde geld "
                  "wordt minder waard."),
        ]),
        dict(kop="Soorten geld", blokken=[
            ("kader", tabel(["soort", "wat", "voorbeeld"],
                            [["chartaal geld", "munten en bankbiljetten", "het briefje van 20 in je portefeuille"],
                             ["giraal geld", "tegoeden op zichtrekeningen", "betalen met je bankkaart"],
                             ["quasigeld", "tegoeden die je snel kan omzetten", "een spaarrekening, een termijnrekening van zes maanden"],
                             ["e-money", "elektronisch geld op een kaart of in een app", "een prepaid betaalkaart"],
                             ["cryptovaluta", "digitale munten zonder centrale bank", "bitcoin"]])),
            ("p", "Een spaarrekening is dus <strong>geen</strong> giraal geld maar quasigeld. In de eurozone is "
                  "<strong>giraal geld</strong> het grootste deel van M1, niet het chartale geld."),
            ("p", "Cryptovaluta worden <strong>niet</strong> uitgegeven door de Europese Centrale Bank en zijn <strong>geen wettig "
                  "betaalmiddel</strong> in België: een winkel moet ze niet aanvaarden. Bitcoin is ook een slechte "
                  "<strong>waardemeter</strong>, want <strong>de waarde schommelt sterk</strong>."),
        ]),
        dict(kop="Monetaire aggregaten", blokken=[
            ("kader", tabel(["aggregaat", "inhoud"],
                            [["M1", "chartaal geld + giraal geld (zichtrekeningen)"],
                             ["M2", "M1 + secundaire liquiditeiten (zoals spaar- en korte termijnrekeningen)"],
                             ["M3", "M2 + nog wat minder liquide tegoeden: het <strong>ruimste</strong> aggregaat"]])),
            ("p", "Elk aggregaat bevat het vorige, dus M1 is het kleinst. De zichtrekeningen zitten in <strong>M1, M2 en M3</strong>."),
        ]),
        dict(kop="Geldsubstitutie en geldschepping", blokken=[
            ("p", "<strong>Geldsubstitutie</strong> is <strong>een soort geld omzetten in een andere soort</strong>. Er ontstaat "
                  "<strong>geen</strong> nieuw geld."),
            ("kader", "<ul><li>Je stort 100 euro aan biljetten op je zichtrekening: chartaal wordt giraal, <strong>M1 blijft gelijk</strong>.</li>"
                      "<li>Je haalt 50 euro af aan de automaat: ook geldsubstitutie.</li>"
                      "<li>Je zet 1 000 euro van je zichtrekening op je spaarrekening: <strong>M1 daalt</strong>, <strong>M2 blijft gelijk</strong> "
                      "(het geld zit nog altijd in M2).</li></ul>"),
            ("p", "<strong>Geldschepping</strong> is <strong>het ontstaan van nieuw geld</strong>. <strong>Commerciële banken "
                  "scheppen giraal geld met kredieten</strong>. Geeft een bank een lening van 10 000 euro en zet ze dat bedrag op "
                  "de zichtrekening van de klant, dan <strong>stijgt M1 met 10 000 euro</strong>. Een woonkrediet of een "
                  "investeringskrediet voor een bedrijf zijn dus geldschepping."),
            ("p", "Omgekeerd: als een lening wordt <strong>terugbetaald</strong>, <strong>verdwijnt</strong> er giraal geld. Geeft een "
                  "bank 1 miljoen euro nieuwe kredieten terwijl klanten 400 000 euro terugbetalen, dan stijgt het girale geld met "
                  "<strong>600 000 euro</strong>."),
        ]),
        dict(kop="De centrale bank", blokken=[
            ("p", "In de eurozone geeft <strong>het Eurosysteem</strong> (de ECB en de nationale centrale banken) de bankbiljetten "
                  "uit. De centrale bank is <strong>de bank van de banken</strong>. Ze <strong>stuurt de geldhoeveelheid bij met de "
                  "rente</strong>."),
            ("p", "Commerciële banken kunnen niet onbeperkt geld scheppen: <strong>ze moeten reserves en kapitaal aanhouden</strong>."),
        ]),
    ],
    onthoud=[
        "Functies: ruil- en betaalmiddel, waardemeter, spaarmiddel, kredietmiddel.",
        "Chartaal = munten en biljetten; giraal = zichtrekeningen; quasigeld = snel om te zetten tegoeden.",
        "M1 = chartaal + giraal; M2 = M1 + secundaire liquiditeiten; M3 is het ruimst.",
        "Geldsubstitutie: een soort geld in een andere, geen nieuw geld.",
        "Geldschepping: banken scheppen giraal geld met kredieten; terugbetalen doet geld verdwijnen.",
        "Het Eurosysteem geeft biljetten uit; de centrale bank stuurt bij met de rente.",
    ])


# ───────────────────────── 13. De financiële markt en beleggen
zet("de-financiele-markt-en-beleggen",
    titel="De financiële markt en beleggen",
    onder="Waar spaargeld en kredieten samenkomen, en welke beleggingen er zijn.",
    secties=[
        dict(kop="De markt van financiële middelen", blokken=[
            ("p", "Op de markt van financiële middelen komen spaarders en ontleners samen. De prijs op die markt is "
                  "<strong>de intrest</strong> (de rente)."),
            ("kader", tabel(["", "wie", "voorbeeld"],
                            [["aanbod", "spaarders", "gezinnen die sparen, pensioenfondsen"],
                             ["vraag", "ontleners", "gezinnen die een huis kopen, bedrijven die investeren, de overheid"]])),
            ("kader", "<ul><li>Gezinnen gaan <strong>meer sparen</strong>: het aanbod stijgt en <strong>de rente daalt</strong>.</li>"
                      "<li>De overheid <strong>leent veel meer</strong> om een tekort te financieren: de vraag stijgt en <strong>de "
                      "rente stijgt</strong>.</li></ul>"),
            ("p", "<strong>Banken</strong> staan tussen spaarders en kredietnemers: ze <strong>verzamelen spaargeld en lenen het uit</strong>. "
                  "Een <strong>pensioenfonds</strong> of een verzekeraar is een <strong>professionele belegger</strong>. Een particulier "
                  "die zelf aandelen koopt, is dat <strong>niet</strong>."),
        ]),
        dict(kop="Geldmarkt en kapitaalmarkt", blokken=[
            ("kader", tabel(["", "betekenis"],
                            [["geldmarkt", "geld voor <strong>korte</strong> termijn (tot een jaar)"],
                             ["kapitaalmarkt", "geld voor <strong>lange</strong> termijn, zoals aandelen en obligaties"],
                             ["primaire markt", "<strong>nieuwe</strong> effecten worden uitgegeven, bv. een bedrijf dat naar de beurs gaat"],
                             ["secundaire markt", "beleggers verhandelen <strong>bestaande</strong> effecten onder elkaar, bv. de beurs"]])),
            ("p", "De beurs hoort dus bij de <strong>kapitaalmarkt</strong>, niet bij de geldmarkt."),
        ]),
        dict(kop="Obligaties en aandelen", blokken=[
            ("kader", tabel(["", "obligatie", "aandeel"],
                            [["wat", "een <strong>lening met rente</strong> aan een bedrijf of overheid", "een <strong>deel van de eigendom</strong> van een bedrijf"],
                             ["kenmerken", "een looptijd en een rentevoet (coupon)", "stemrecht, eventueel dividend"],
                             ["rendement", "de coupon, en de koers", "een <strong>dividend</strong> en een <strong>koersstijging</strong>"],
                             ["risico", "kleiner, maar niet nul", "groter: <strong>de koersen schommelen sterker</strong>"]])),
            ("p", "<strong>Stijgt de marktrente</strong>, dan <strong>daalt de koers</strong> van een bestaande obligatie met vaste rente: "
                  "nieuwe obligaties geven meer, dus wil niemand nog de volle prijs betalen voor de oude. Het rendement van een "
                  "obligatie hangt af van <strong>de evolutie van de marktrente</strong> en van <strong>de kredietwaardigheid van de "
                  "uitgever</strong>. Een obligatie is dus niet zonder risico."),
            ("p", "Het rendement van een aandeel hangt vooral af van <strong>de verwachte winst van het bedrijf</strong>. Een bedrijf is "
                  "<strong>niet verplicht</strong> om elk jaar dividend uit te keren."),
        ]),
        dict(kop="Fondsen en verzekeringen", blokken=[
            ("kader", tabel(["product", "wat"],
                            [["beleggingsfonds (ICB)", "een fonds dat geld van veel beleggers samen belegt"],
                             ["bevek / bevak", "bevek: veranderlijk kapitaal; bevak: vast kapitaal"],
                             ["ETF", "een indexfonds dat je, zoals een aandeel, op elk moment op de beurs verhandelt"],
                             ["obligatiefonds", "belegt in obligaties: meestal het minst risicovol"],
                             ["gemengd fonds", "belegt in aandelen én obligaties"],
                             ["Tak21-verzekering", "gewaarborgd kapitaal met een gewaarborgde rente"],
                             ["Tak23-verzekering", "rendement hangt af van beleggingsfondsen, <strong>zonder kapitaalgarantie</strong>: je kan minder terugkrijgen"]])),
            ("p", "Wie zeker wil zijn dat hij zijn inleg terugkrijgt, kiest best een <strong>Tak21</strong>. Beleggers "
                  "<strong>spreiden</strong> hun geld over verschillende beleggingen <strong>om het risico te beperken</strong>."),
        ]),
        dict(kop="Duurzaam beleggen", blokken=[
            ("kader", tabel(["letter", "staat voor", "voorbeeld"],
                            [["E", "Environment (milieu)", "weinig uitstoot"],
                             ["S", "Social", "kinderarbeid bij leveranciers weren"],
                             ["G", "Governance (bestuur)", "een onafhankelijke raad van bestuur, eerlijke beloning van de top"]])),
            ("p", "De <strong>ESG-score</strong> van een fonds zegt <strong>hoe duurzaam de bedrijven zijn</strong> waarin het belegt. "
                  "Beleggingen in bedrijven met <strong>hoge uitstoot</strong> of <strong>corruptieschandalen</strong> verlagen de score. "
                  "Duurzaam beleggen betekent dus dat je niet enkel naar het hoogste rendement kijkt."),
            ("p", "Heet een fonds 'groen' maar belegt het grotendeels in olie en gas, dan spreek je van <strong>greenwashing</strong>."),
        ]),
    ],
    onthoud=[
        "De prijs op de markt van financiële middelen is de intrest; meer sparen doet de rente dalen, meer lenen doet ze stijgen.",
        "Geldmarkt: korte termijn. Kapitaalmarkt: lange termijn. Primair: nieuwe effecten. Secundair: bestaande (beurs).",
        "Obligatie = lening met rente; stijgt de marktrente, dan daalt haar koers.",
        "Aandeel = eigendom; rendement via dividend en koersstijging; riskanter.",
        "Tak21: kapitaal gewaarborgd. Tak23: geen garantie. ETF: indexfonds op de beurs.",
        "ESG = Environment, Social, Governance; greenwashing = groen lijken zonder het te zijn.",
    ])


def lorenz(punten, breedte=300, hoogte=230, titel=None):
    """Een Lorenzcurve: punten op 0..10 (10 = 100 %)."""
    lijnen = [(0, 0, 10, 10, "g", "")]
    vorig = (0, 0)
    for p in punten:
        lijnen.append((vorig[0], vorig[1], p[0], p[1], "v", ""))
        vorig = p
    vlak = [(0, 0), *punten, (10, 10)]
    return grafiek(lijnen=lijnen, vlakken=[(vlak[::-1] + [(0, 0)], "a", "")],
                   xlabel="% bevolking", ylabel="% inkomen", breedte=breedte, hoogte=hoogte, titel=titel)


# ───────────────────────── 14. Inkomensongelijkheid, armoede en herverdeling
zet("inkomensongelijkheid-armoede-en-herverdeling",
    titel="Inkomensongelijkheid, armoede en herverdeling",
    onder="Hoe je ongelijkheid en armoede meet, en hoe de overheid inkomen herverdeelt.",
    secties=[
        dict(kop="Twee soorten inkomensverdeling", blokken=[
            ("kader", tabel(["", "toont"],
                            [["personele inkomensverdeling", "hoe het inkomen verdeeld is over <strong>personen of gezinnen</strong>"],
                             ["categoriale inkomensverdeling", "hoe het inkomen verdeeld is over <strong>de productiefactoren</strong> (loon, intrest, huur, winst)"]])),
        ]),
        dict(kop="De Lorenzcurve", blokken=[
            ("fig", lorenz([(2, 0.6), (4, 1.8), (6, 3.6), (8, 6), (10, 10)]),
             "Stippellijn: de diagonaal van perfecte gelijkheid. Het gekleurde vlak toont de ongelijkheid."),
            ("p", "Op de assen van een Lorenzcurve staan <strong>het cumulatieve percentage van de bevolking</strong> (van arm naar "
                  "rijk) en <strong>het cumulatieve percentage van het inkomen</strong>. Een punt (20 %, 6 %) betekent: de armste 20 % "
                  "heeft samen 6 % van het inkomen."),
            ("p", "Bij een <strong>perfect gelijke</strong> verdeling valt de curve <strong>samen met de diagonaal</strong>: de armste 20 % "
                  "heeft dan 20 % van het inkomen. Hoe <strong>verder van de diagonaal</strong>, hoe <strong>ongelijker</strong>. Herverdeelt "
                  "de overheid van rijk naar arm, dan <strong>schuift de curve dichter naar de diagonaal</strong>."),
        ]),
        dict(kop="De Gini-coëfficiënt", blokken=[
            ("kader", "<p style=\"text-align:center\"><strong>Gini = oppervlakte tussen diagonaal en Lorenzcurve / oppervlakte "
                      "onder de diagonaal</strong></p>"),
            ("p", "De oppervlakte onder de diagonaal is 0,5. Is de oppervlakte tussen diagonaal en curve 0,15, dan is de Gini "
                  "0,15 / 0,5 = <strong>0,3</strong>."),
            ("p", "Gini <strong>0</strong> betekent <strong>perfecte gelijkheid</strong>, Gini dicht bij <strong>1</strong> een "
                  "<strong>grote ongelijkheid</strong>. Land X met 0,26 is gelijker dan land Y met 0,45. Stijgt de Gini jaar na jaar, "
                  "dan <strong>neemt de ongelijkheid toe</strong>. België heeft in vergelijking met veel andere landen een "
                  "<strong>relatief lage</strong> Gini."),
            ("weetje", "Een lage Gini zegt niets over hoe rijk een land is. Een land kan een lage Gini hebben en toch arm zijn: "
                       "iedereen heeft dan ongeveer even weinig."),
        ]),
        dict(kop="Oorzaken van ongelijkheid", blokken=[
            ("p", "Oorzaken zijn onder meer <strong>verschillen in opleiding en beroep</strong> en <strong>verschillen in vermogen</strong>: "
                  "vermogen levert zelf inkomen op (huur, intrest, dividend). Ook <strong>het sociaal milieu</strong> speelt mee, via "
                  "<strong>kansen op onderwijs, netwerk en steun thuis</strong>. De <strong>genderloonkloof</strong> is het verschil in "
                  "gemiddeld loon tussen mannen en vrouwen."),
        ]),
        dict(kop="Armoede meten", blokken=[
            ("p", "Armoede en ongelijkheid zijn <strong>niet hetzelfde</strong>. Ongelijkheid gaat over verschillen, armoede over wie "
                  "te weinig heeft."),
            ("kader", tabel(["indicator", "meet"],
                            [["AROP", "risico op monetaire armoede: inkomen <strong>onder 60 % van het mediaaninkomen</strong>"],
                             ["SMSD", "ernstige materiële en sociale deprivatie: je kan je basisdingen niet veroorloven"],
                             ["LWI", "gezinnen met een lage werkintensiteit"],
                             ["AROPE", "wie met <strong>minstens één van de drie</strong> te maken heeft"]])),
            ("p", "Een AROP van 13 % betekent dat 13 % van de bevolking onder de armoedegrens leeft. Men gebruikt het "
                  "<strong>mediaaninkomen</strong> en niet het gemiddelde, omdat <strong>de mediaan minder reageert op enkele hoge "
                  "inkomens</strong>."),
        ]),
        dict(kop="Herverdeling", blokken=[
            ("p", "De <strong>personenbelasting</strong> in België is <strong>progressief</strong>: <strong>elke hogere inkomensschijf "
                  "krijgt een hoger tarief</strong>. Hogere inkomens betalen dus een groter percentage, en dat verkleint de "
                  "ongelijkheid. Een <strong>vlaktaks</strong>, waarbij iedereen hetzelfde percentage betaalt, doet dat minder sterk."),
            ("p", "De <strong>sociale zekerheid</strong> telt <strong>zeven takken</strong>: pensioenen, werkloosheid, ziekte- en "
                  "invaliditeitsverzekering, arbeidsongevallen, beroepsziekten, gezinsbijslag en jaarlijkse vakantie."),
            ("kader", tabel(["principe", "betekenis"],
                            [["verzekeringsprincipe", "wie bijdraagt, is verzekerd tegen risico's"],
                             ["solidariteitsprincipe", "de sterkste schouders dragen de zwaarste lasten"]])),
            ("kader", tabel(["", "voorbeeld"],
                            [["vervangingsinkomen", "een werkloosheidsuitkering, een pensioen"],
                             ["aanvulling op het inkomen", "de gezinsbijslag (het Groeipakket)"]])),
            ("p", "Tegen armoede helpen ook een <strong>leefloon</strong> voor wie geen inkomen heeft en <strong>sociale woningen</strong>. "
                  "Door belastingen en sociale zekerheid <strong>daalt de Gini</strong>."),
        ]),
    ],
    onthoud=[
        "Personele verdeling: over personen. Categoriale verdeling: over productiefactoren.",
        "Lorenzcurve: cumulatief % bevolking tegen % inkomen; hoe verder van de diagonaal, hoe ongelijker.",
        "Gini = oppervlakte tussen diagonaal en curve / 0,5; 0 = gelijk, dicht bij 1 = zeer ongelijk.",
        "AROP: onder 60 % van het mediaaninkomen. AROPE: AROP, SMSD of LWI.",
        "Progressieve belasting en sociale zekerheid (7 takken) verkleinen de ongelijkheid.",
        "Pensioen en werkloosheidsuitkering vervangen inkomen; gezinsbijslag vult aan.",
    ])


# ───────────────────────── 15. Internationale handel en samenwerkingsverbanden
zet("internationale-handel-en-samenwerkingsverbanden",
    titel="Internationale handel en samenwerkingsverbanden",
    onder="Hoe landen samenwerken, hoe je de handel van een land meet, en waarom bedrijven productie verplaatsen.",
    secties=[
        dict(kop="Vijf stappen van samenwerking", blokken=[
            ("p", "Van minst naar meest verregaand. Elke stap bevat alles van de vorige, plus iets nieuws."),
            ("kader", tabel(["stap", "wat komt erbij"],
                            [["1. vrijhandelszone", "geen invoerrechten onderling; elk land kiest <strong>zelf</strong> zijn tarieven naar buiten"],
                             ["2. douane-unie", "een <strong>gemeenschappelijk buitentarief</strong>"],
                             ["3. gemeenschappelijke markt", "<strong>vrij verkeer</strong> van goederen, diensten, personen en kapitaal"],
                             ["4. economische unie", "de landen stemmen ook hun <strong>economisch beleid</strong> op elkaar af"],
                             ["5. monetaire unie", "<strong>één munt</strong> met één centrale bank"]])),
            ("p", "De <strong>Europese Unie</strong> is minstens een gemeenschappelijke markt; de eurozone is een monetaire unie. De "
                  "<strong>vier vrijheden</strong> van de Europese interne markt zijn het vrij verkeer van goederen, diensten, "
                  "personen en kapitaal."),
        ]),
        dict(kop="Gevolgen van samenwerking", blokken=[
            ("kader", "<ul><li>Invoerrechten vallen weg, dus <strong>goederen uit de partnerlanden worden goedkoper</strong>.</li>"
                      "<li><strong>Meer concurrentie</strong>, <strong>grotere afzetmarkten en schaalvoordelen</strong>.</li>"
                      "<li><strong>Handelsverlegging</strong> bij een douane-unie: landen kopen bij een lid van de unie, ook als een "
                      "land buiten de unie goedkoper produceert.</li>"
                      "<li>Een monetaire unie geeft bedrijven <strong>geen wisselkoersrisico en geen wisselkosten</strong>. Maar een "
                      "land kan zijn munt niet meer <strong>devalueren</strong> om goedkoper te exporteren.</li></ul>"),
        ]),
        dict(kop="De handelsbalans", blokken=[
            ("p", "De <strong>handelsbalans</strong> is het overzicht van de <strong>export en de import</strong> van een land. Het saldo "
                  "is export min import."),
            ("kader", "<ul><li>Export 300, import 260: saldo <strong>+40</strong>, een <strong>handelsoverschot</strong>.</li>"
                      "<li>Export 420, import 450: saldo <strong>−30</strong>, een <strong>handelstekort</strong>: het land importeert "
                      "meer dan het exporteert.</li></ul>"),
            ("p", "Daalt de export terwijl de rest gelijk blijft, dan <strong>daalt</strong> het saldo. Een handelstekort kan "
                  "ontstaan doordat <strong>de eigen producten duur zijn tegenover buitenlandse</strong>. Duurt het lang, dan "
                  "<strong>moet het land lenen bij het buitenland</strong>. Een handelsoverschot is ook niet altijd en zonder "
                  "uitzondering goed (andere landen hebben dan een tekort, en de eigen munt kan duur worden)."),
        ]),
        dict(kop="Uitvoerquote en invoerquote", blokken=[
            ("kader", "<p style=\"text-align:center\"><strong>uitvoerquote = export / bbp · 100</strong> &nbsp;·&nbsp; "
                      "<strong>invoerquote = import / bbp · 100</strong></p>"),
            ("p", "Bbp 500 en import 400: invoerquote <strong>80 %</strong>. Bbp 600 en export 480: uitvoerquote <strong>80 %</strong>. "
                  "Stijgt de import bij een gelijk bbp, dan stijgt de invoerquote."),
            ("p", "Een hoge quote wijst op een <strong>open economie</strong>. België is zo'n open economie. Grote landen zoals de "
                  "Verenigde Staten hebben meestal een <strong>lagere</strong> quote dan kleine landen. Land B met een invoerquote "
                  "van 85 % is opener dan land A met 20 %."),
            ("weetje", "Een uitvoerquote kan <strong>groter zijn dan 100 %</strong>: de export bevat ook ingevoerde onderdelen, en die "
                       "tellen niet mee in het bbp. Statistieken over de Belgische buitenlandse handel vind je bij het "
                       "<strong>Agentschap voor Buitenlandse Handel</strong>."),
        ]),
        dict(kop="Productie verplaatsen", blokken=[
            ("kader", tabel(["begrip", "betekenis", "voorbeeld"],
                            [["outsourcing", "een taak <strong>uitbesteden aan een ander bedrijf</strong>, in binnen- of buitenland", "de boekhouding laten doen door een kantoor"],
                             ["offshoring", "productie verplaatsen naar een <strong>ver land</strong>, vooral voor <strong>lagere loonkosten</strong>", "van België naar China"],
                             ["nearshoring", "productie verplaatsen naar een land <strong>dichterbij</strong>", "van China naar Portugal"],
                             ["reshoring", "productie <strong>terughalen</strong> naar het eigen land", "terug naar België"]])),
            ("p", "Redenen voor reshoring zijn onder meer <strong>hoge transportkosten</strong> en <strong>problemen in de "
                  "toeleveringsketen</strong>."),
        ]),
    ],
    onthoud=[
        "Vrijhandelszone → douane-unie → gemeenschappelijke markt → economische unie → monetaire unie.",
        "Douane-unie: gemeenschappelijk buitentarief. Gemeenschappelijke markt: vier vrijheden.",
        "Handelsbalans = export − import; negatief = handelstekort.",
        "Uitvoerquote = export / bbp · 100; hoge quotes = open economie (België).",
        "Outsourcing: uitbesteden. Offshoring: ver weg. Nearshoring: dichterbij. Reshoring: terug.",
    ])


# ───────────────────────── 16. De wisselmarkt en de betalingsbalans
zet("de-wisselmarkt-en-de-betalingsbalans",
    titel="De wisselmarkt en de betalingsbalans",
    onder="Hoe de koers van de euro tot stand komt, wat die koers doet met de handel, en hoe een land zijn rekening met het buitenland bijhoudt.",
    secties=[
        dict(kop="De wisselmarkt", blokken=[
            ("p", "Op de wisselmarkt (valutamarkt) worden munten verhandeld. Het is een markt met <strong>volkomen concurrentie</strong>: "
                  "<strong>veel kopers en verkopers van een homogeen product</strong>. Actief zijn onder meer <strong>exporteurs en "
                  "importeurs</strong>, <strong>beleggers en speculanten</strong>, toeristen en centrale banken."),
            ("kader", tabel(["wie vraagt euro's?", "wie biedt euro's aan?"],
                            [["Amerikaanse bedrijven die Belgische producten kopen", "Belgische bedrijven die Amerikaanse producten kopen"],
                             ["een Japanse toerist in Brugge", "een Belgische toerist in Japan (die vraagt yen)"],
                             ["buitenlandse beleggers in Europese aandelen", "Europese beleggers in Amerikaanse aandelen"]])),
            ("fig", grafiek(lijnen=[(1, 9, 8, 2, "g", "V"), (3, 9, 10, 2, "v", "V′"), (1, 2, 9, 9, "a", "A")],
                            punten=[(4.73, 5.27, ""), (5.8, 6.2, "")], xlabel="hoeveelheid euro", ylabel="koers in dollar",
                            breedte=330, hoogte=220),
             "De vraag naar euro stijgt: de vraagcurve schuift naar rechts en de koers stijgt."),
        ]),
        dict(kop="Appreciatie en depreciatie", blokken=[
            ("p", "Gaat de koers EUR/USD van 1,10 naar 1,20, dan krijg je meer dollar voor een euro: de euro "
                  "<strong>apprecieert</strong>. Daalt de koers, dan <strong>deprecieert</strong> de euro."),
            ("kader", tabel(["", "Europese producten voor Amerikanen", "Amerikaanse producten voor Europeanen", "gevolg"],
                            [["euro apprecieert", "duurder", "goedkoper", "export daalt, import stijgt"],
                             ["euro deprecieert", "goedkoper", "duurder", "export stijgt, import daalt"]])),
            ("kader", "<ul><li>1 euro = 1,25 dollar: een product van 80 euro kost een Amerikaan 80 · 1,25 = <strong>100 dollar</strong>.</li>"
                      "<li>1 euro = 1,10 dollar: een factuur van 5 500 dollar kost een Belgische importeur 5 500 / 1,10 = "
                      "<strong>5 000 euro</strong>.</li></ul>"),
            ("p", "Het <strong>wisselkoersrisico</strong> is het risico dat een koerswijziging verlies oplevert. Een exporteur die later "
                  "in dollar betaald wordt, <strong>wint</strong> als de dollar intussen stijgt: hij krijgt dan meer euro's."),
        ]),
        dict(kop="Waarom verandert de koers?", blokken=[
            ("kader", tabel(["gebeurtenis", "gevolg voor de euro"],
                            [["hogere inflatie in de eurozone dan in de VS", "deprecieert"],
                             ["de ECB verhoogt de rente", "vraag naar euro stijgt: apprecieert"],
                             ["de rente in de eurozone daalt", "deprecieert"],
                             ["het inkomen in de VS stijgt: Amerikanen kopen meer Europese producten", "apprecieert"],
                             ["het inkomen in de eurozone stijgt: Europeanen importeren meer, het aanbod van euro stijgt", "deprecieert"],
                             ["consumenten wereldwijd verkiezen Europese producten", "apprecieert"],
                             ["speculanten verwachten een stijging en kopen nu euro's", "stijgt al"]])),
        ]),
        dict(kop="Vlottende of vaste koersen", blokken=[
            ("p", "Een <strong>vlottende wisselkoers</strong> wordt <strong>vrij bepaald door vraag en aanbod</strong>; de regering bepaalt "
                  "hem niet elke dag. Een <strong>vaste wisselkoers</strong> geeft bedrijven <strong>minder wisselkoersrisico</strong>."),
        ]),
        dict(kop="De betalingsbalans", blokken=[
            ("p", "De betalingsbalans is het overzicht van <strong>alle transacties van een land met het buitenland</strong>. Ze bestaat "
                  "uit drie deelrekeningen: de <strong>lopende rekening</strong>, de <strong>kapitaalrekening</strong> en de "
                  "<strong>financiële rekening</strong>."),
            ("kader", tabel(["deelrekening", "post", "voorbeeld"],
                            [["lopende rekening", "goederen (= de handelsbalans)", "een Belgisch bedrijf verkoopt machines aan Duitsland"],
                             ["", "diensten", "een Nederlandse toerist betaalt een hotel in Brugge"],
                             ["", "primaire inkomens", "dividend dat een Belg krijgt van een buitenlands bedrijf"],
                             ["", "secundaire inkomens", "een werknemer stuurt geld naar familie in Marokko"],
                             ["financiële rekening", "beleggingen en investeringen", "een Belg koopt Amerikaanse aandelen; een Belgisch bedrijf bouwt een fabriek in Polen"]])),
            ("p", "Een groot <strong>tekort op de lopende rekening</strong> kan bij vlottende koersen de munt doen <strong>depreciëren</strong>. "
                  "Die depreciatie kan dan weer helpen om het tekort te verkleinen, want de export wordt goedkoper."),
        ]),
        dict(kop="Internationale instellingen", blokken=[
            ("kader", tabel(["instelling", "taak"],
                            [["IMF (Internationaal Monetair Fonds)", "landen met betalingsbalansproblemen helpen"],
                             ["Wereldbank", "armoede bestrijden met ontwikkelingsleningen (ze bepaalt geen wisselkoersen)"],
                             ["OESO", "onderzoek en beleidsadvies voor haar lidstaten"]])),
        ]),
    ],
    onthoud=[
        "Wie euro's nodig heeft, vraagt euro's; wie euro's omwisselt in een andere munt, biedt euro's aan.",
        "Appreciatie: de euro wordt duurder; export daalt, import stijgt. Depreciatie: omgekeerd.",
        "Hogere rente of meer vraag naar Europese producten: euro apprecieert. Hogere inflatie: euro deprecieert.",
        "Vlottend: vraag en aanbod. Vast: minder wisselkoersrisico.",
        "Betalingsbalans: lopende rekening (goederen, diensten, primaire en secundaire inkomens), kapitaal- en financiële rekening.",
        "IMF helpt bij betalingsbalansproblemen, Wereldbank bestrijdt armoede, OESO geeft advies.",
    ])


def conjunctuurgolf(breedte=420, hoogte=230):
    """Een golf rond een stijgende trendlijn, met de fasen erbij."""
    import math
    d, x, y = svg._as_vlak(breedte, hoogte, "tijd", "reëel bbp")
    trend = lambda t: 2.2 + 0.45 * t
    golf = lambda t: trend(t) + 1.4 * math.sin(t * 0.95)
    d.append(f'<line x1="{x(0):.1f}" y1="{y(trend(0)):.1f}" x2="{x(10):.1f}" y2="{y(trend(10)):.1f}" '
             f'stroke="{svg.DIM}" stroke-width="1.6" stroke-dasharray="6 4"/>')
    pts = " ".join(f"{x(t/10):.1f},{y(golf(t/10)):.1f}" for t in range(0, 101))
    d.append(f'<polyline points="{pts}" fill="none" stroke="{svg.FOREST}" stroke-width="2.4"/>')
    d.append(svg._tekst(x(9.6), y(trend(9.6)) + 16, "trend", 10, svg.DIM, "middle", True))
    for t, label, boven in [(1.65, "boom", True), (3.3, "recessie", True), (4.95, "depressie", False), (6.6, "herstel", False)]:
        yy = y(golf(t)) + (-9 if boven else 17)
        d.append(f'<circle cx="{x(t):.1f}" cy="{y(golf(t)):.1f}" r="3.4" fill="{svg.AMBER}"/>')
        d.append(svg._tekst(x(t), yy, label, 10, svg.INK, "middle", True))
    return svg._svg(breedte, hoogte, "".join(d))


# ───────────────────────── 17. De conjunctuur, conjunctuurindicatoren en de begroting
zet("de-conjunctuur-conjunctuurindicatoren-en-de-begroting",
    titel="De conjunctuur, conjunctuurindicatoren en de begroting",
    onder="Hoe de economie op en neer golft, hoe je dat vooraf ziet aankomen, en wat het doet met de begroting.",
    secties=[
        dict(kop="Trend en conjunctuur", blokken=[
            ("p", "De <strong>trend</strong> is <strong>de groeilijn op lange termijn</strong>. De <strong>conjunctuur</strong> zijn "
                  "<strong>de schommelingen van de economische activiteit rond die trend</strong>."),
            ("fig", conjunctuurgolf(), "De conjunctuurgolf rond de trend."),
            ("kader", tabel(["fase", "wat gebeurt er"],
                            [["expansie (opgaande fase)", "sterke groei, hoge investeringen, dalende werkloosheid"],
                             ["boom", "het <strong>hoogtepunt</strong>: hoogconjunctuur, soms overbesteding"],
                             ["crisis", "een plotse en scherpe omslag naar een neergang"],
                             ["recessie / contractie (neergaande fase)", "het reëel bbp daalt <strong>twee kwartalen na elkaar</strong>; de werkloosheid stijgt en de faillissementen nemen toe"],
                             ["depressie", "het <strong>dieptepunt</strong>"],
                             ["herstel", "volgt op de depressie: de groei komt terug"]])),
            ("p", "Tijdens een <strong>hoogconjunctuur stijgen</strong> de investeringen meestal, ze dalen niet."),
        ]),
        dict(kop="Potentieel bbp en outputkloof", blokken=[
            ("p", "Het <strong>potentieel bbp</strong> is <strong>wat de economie normaal kan produceren</strong>. De "
                  "<strong>outputkloof</strong> is <strong>het verschil tussen het reëel bbp en het potentieel bbp</strong>."),
            ("kader", tabel(["situatie", "outputkloof", "wat"],
                            [["onderbesteding", "negatief", "de vraag is kleiner dan wat de economie kan produceren"],
                             ["bestedingsevenwicht", "ongeveer nul", "vraag en productiecapaciteit zijn in evenwicht"],
                             ["overbesteding", "positief", "de vraag is groter dan de productiecapaciteit, met prijsstijgingen tot gevolg"]])),
            ("p", "Reëel bbp 480 en potentieel bbp 500 (miljard euro): een <strong>negatieve outputkloof van 20</strong>, dus "
                  "onderbesteding."),
        ]),
        dict(kop="Waar komen de conjunctuurschommelingen vandaan?", blokken=[
            ("kader", tabel(["verklaring", "oorzaak", "voorbeeld"],
                            [["exogene verklaring", "van <strong>buiten</strong> de economie", "een pandemie, een oorlog die de olieprijs doet stijgen"],
                             ["endogene verklaring", "<strong>binnen</strong> de economie zelf", "bedrijven die te veel investeren en daarna moeten afbouwen"]])),
        ]),
        dict(kop="Conjunctuurindicatoren", blokken=[
            ("kader", tabel(["soort", "betekenis", "voorbeelden"],
                            [["voorlopend", "verandert <strong>voor</strong> de economie", "consumentenvertrouwen, ondernemersvertrouwen, beursindices"],
                             ["gelijklopend", "verandert <strong>samen met</strong> de economie", "de industriële productie"],
                             ["achterlopend", "verandert <strong>na</strong> de economie", "de werkloosheid"]])),
            ("p", "<strong>Kwalitatieve</strong> indicatoren meten verwachtingen en gevoelens, via enquêtes: het consumenten- en het "
                  "ondernemersvertrouwen. <strong>Kwantitatieve</strong> indicatoren tellen iets, zoals <strong>het aantal "
                  "faillissementen</strong>."),
            ("p", "<strong>Beursindices</strong> stijgen vaak al voor de economie zich herstelt. Daalt het <strong>ondernemersvertrouwen</strong> "
                  "sterk, dan verwacht je de komende maanden <strong>minder investeringen en minder groei</strong>."),
        ]),
        dict(kop="De begroting", blokken=[
            ("kader", "<p style=\"text-align:center\"><strong>begrotingssaldo = overheidsinkomsten − overheidsuitgaven</strong></p>"),
            ("p", "Ontvangt de overheid 280 miljard en geeft ze 300 miljard uit, dan is het saldo <strong>−20</strong>: een "
                  "<strong>begrotingstekort</strong>. Bij een <strong>begrotingsoverschot</strong> ontvangt de overheid meer dan ze uitgeeft. "
                  "Een tekort moet de overheid lenen, dus de staatsschuld <strong>stijgt</strong>."),
            ("kader", tabel(["overheidsinkomsten", "voorbeelden"],
                            [["directe belastingen (fiscaal)", "personenbelasting, vennootschapsbelasting"],
                             ["indirecte belastingen (fiscaal)", "btw, accijnzen"],
                             ["sociale bijdragen", "bijdragen voor de sociale zekerheid"],
                             ["niet-fiscale inkomsten", "de verkoop van een overheidsgebouw"]])),
            ("p", "Overheidsuitgaven zijn bijvoorbeeld <strong>de lonen van leerkrachten</strong>, uitkeringen en investeringen in wegen. "
                  "Tijdens een recessie <strong>verslechtert</strong> het begrotingssaldo: <strong>minder belastinginkomsten en meer "
                  "uitkeringen</strong>."),
        ]),
    ],
    onthoud=[
        "Trend = groeilijn op lange termijn; conjunctuur = schommelingen eromheen.",
        "Expansie → boom (hoogtepunt) → recessie → depressie (dieptepunt) → herstel.",
        "Recessie: reëel bbp daalt twee kwartalen na elkaar.",
        "Outputkloof = reëel − potentieel bbp; negatief = onderbesteding, positief = overbesteding.",
        "Voorlopend: vertrouwen, beurs. Achterlopend: werkloosheid. Exogeen = van buiten, endogeen = van binnen.",
        "Begrotingssaldo = inkomsten − uitgaven; in een recessie verslechtert het.",
    ])


# ───────────────────────── 18. Het inkomensevenwicht, de multiplicator en het AV-AA-schema
zet("het-inkomensevenwicht-de-multiplicator-en-het-av-aa-schema",
    titel="Het inkomensevenwicht, de multiplicator en het AV-AA-schema",
    onder="Hoe de bestedingen het inkomen bepalen, waarom een extra uitgave meer oplevert dan zichzelf, en hoe schokken prijzen en productie veranderen.",
    secties=[
        dict(kop="Het vereenvoudigd model", blokken=[
            ("p", "In het vereenvoudigd model van een gesloten economie blijven <strong>de prijzen, de geldhoeveelheid en de rente "
                  "constant</strong>. Het evenwichtsinkomen wordt dan bepaald door de <strong>effectieve vraag</strong>: de bestedingen "
                  "<strong>waarvoor ook koopkracht is</strong>. Er is <strong>inkomensevenwicht</strong> als de effectieve vraag gelijk is "
                  "aan het inkomen Y."),
            ("kader", "<p><strong>Voorbeeld.</strong> C = 50 + 0,8Y en I = 100 (zonder overheid).</p><ul>"
                      "<li>Evenwicht: Y = C + I = 50 + 0,8Y + 100, dus 0,2Y = 150 en <strong>Y = 750</strong>.</li>"
                      "<li>De <strong>marginale consumptiequote</strong> is <strong>0,8</strong>: van elke extra euro inkomen wordt 80 cent "
                      "besteed. De marginale spaarquote is 0,2.</li></ul>"),
            ("fig", grafiek(lijnen=[(0, 0, 10, 10, "g", "45°"), (0, 3, 10, 7, "v", "C + I"), (0, 4.5, 10, 8.5, "a", "C + I′")],
                            punten=[(5, 5, "Y"), (7.5, 7.5, "Y′")], xlabel="inkomen Y", ylabel="bestedingen",
                            breedte=330, hoogte=230),
             "Op de 45°-lijn zijn de bestedingen gelijk aan Y. Stijgen de investeringen, dan schuift de bestedingslijn omhoog."),
            ("p", "De <strong>45°-lijn</strong> toont <strong>de punten waar de bestedingen gelijk zijn aan Y</strong>. Het evenwicht ligt "
                  "waar de bestedingslijn die lijn snijdt. Stijgen de autonome investeringen, dan <strong>schuift de bestedingslijn "
                  "omhoog en stijgt het evenwichtsinkomen</strong>."),
        ]),
        dict(kop="De multiplicator", blokken=[
            ("kader", "<p style=\"text-align:center\"><strong>multiplicator = 1 / (1 − marginale consumptiequote)</strong></p>"
                      "<p>Gaat het om extra investeringen, dan spreek je van de <strong>investeringsmultiplicator</strong>; het "
                      "verschijnsel zelf heet het <strong>multiplicatoreffect</strong>.</p>"),
            ("kader", tabel(["marginale consumptiequote", "multiplicator"],
                            [["0,8", "1 / 0,2 = <strong>5</strong>"],
                             ["0,75", "1 / 0,25 = <strong>4</strong>"],
                             ["0,9", "1 / 0,1 = <strong>10</strong> (niet 0,9)"]])),
            ("p", "Stijgen de autonome investeringen met 20 bij een multiplicator van 5, dan stijgt het inkomen met "
                  "<strong>100</strong>. Verhoogt de overheid haar uitgaven met 10 miljard bij een multiplicator van 2,5, dan stijgt "
                  "het inkomen met <strong>25 miljard</strong>. Het werkt ook omgekeerd: een daling van de investeringen doet het "
                  "inkomen met <strong>meer</strong> dan die daling dalen."),
            ("p", "Waarom meer? <strong>De uitgave wordt inkomen voor anderen, die verder besteden.</strong> Maar bij elke ronde lekt er "
                  "iets weg:"),
            ("kader", "<ul><li>het <strong>spaarlek</strong>: het deel van het extra inkomen dat gespaard wordt;</li>"
                      "<li>het <strong>belastinglek</strong>: het deel van het extra inkomen voor belastingen.</li></ul>"
                      "<p>Hoe groter de marginale spaarquote, hoe <strong>kleiner</strong> de multiplicator. Met belastingen erbij is de "
                      "multiplicator dus <strong>kleiner</strong> dan zonder.</p>"),
        ]),
        dict(kop="Het AV-AA-schema", blokken=[
            ("p", "Op de assen staan <strong>het algemeen prijspeil</strong> en <strong>het reëel bbp</strong>. Hier mogen de prijzen wel "
                  "veranderen."),
            ("fig", svg.naast_elkaar([
                grafiek(lijnen=[(1, 9, 8, 2, "v", "AV"), (3, 9, 10, 2, "g", "AV′"), (1, 2, 9, 9, "a", "AA")],
                        punten=[(4.73, 5.27, ""), (5.8, 6.2, "")], xlabel="reëel bbp", ylabel="prijspeil", breedte=240, hoogte=190),
                grafiek(lijnen=[(1, 9, 8, 2, "v", "AV"), (1, 2, 9, 9, "a", "AA"), (0, 3.5, 7, 9.6, "g", "AA′")],
                        punten=[(4.73, 5.27, ""), (3.47, 6.53, "")], xlabel="reëel bbp", ylabel="prijspeil", breedte=240, hoogte=190)]),
             "Links een positieve vraagschok: AV naar rechts, prijspeil en bbp stijgen. Rechts een negatieve aanbodschok: AA naar links, hogere prijzen en minder productie."),
            ("kader", tabel(["curve", "verloop"],
                            [["AV (aggregatieve vraag)", "<strong>dalend</strong>"],
                             ["AA op korte termijn", "<strong>stijgend</strong>: bij een hoger prijspeil wordt er meer geproduceerd"],
                             ["AA op lange termijn", "<strong>verticaal</strong> bij het potentieel bbp"]])),
            ("p", "Het macro-economisch evenwicht op korte termijn ligt <strong>op het snijpunt van AV en AA op korte termijn</strong>."),
        ]),
        dict(kop="Schokken", blokken=[
            ("kader", tabel(["schok", "voorbeeld", "gevolg"],
                            [["positieve vraagschok", "meer bestedingen", "AV naar rechts: prijspeil en reëel bbp stijgen"],
                             ["negatieve vraagschok", "het consumentenvertrouwen stort in", "AV naar links"],
                             ["negatieve aanbodschok", "de olieprijs stijgt fors", "AA naar links: kan leiden tot <strong>stagflatie</strong>, hogere prijzen en minder productie"],
                             ["positieve aanbodschok", "een technologische doorbraak", "AA naar rechts"]])),
            ("p", "Op lange termijn, met een verticale AA-curve, keert na een positieve vraagschok <strong>het bbp terug naar het "
                  "potentieel</strong> en <strong>blijft het prijspeil hoger</strong>."),
        ]),
        dict(kop="Beleid", blokken=[
            ("kader", tabel(["", "budgettair beleid", "monetair beleid"],
                            [["wie", "de overheden (federaal, Vlaams ...)", "voor België: de <strong>Europese Centrale Bank</strong>"],
                             ["middel", "uitgaven en belastingen", "de rente"],
                             ["expansief", "meer investeren in wegen en scholen, belastingen verlagen", "de rente verlagen"],
                             ["effect van expansief", "AV naar rechts", "AV naar rechts"]])),
            ("p", "Een <strong>renteverhoging</strong> is een <strong>restrictief</strong> monetair beleid, en een restrictief beleid "
                  "doet de AV-curve naar <strong>links</strong> schuiven. De Vlaamse regering kan de rente in de eurozone niet zelf "
                  "verlagen: dat doet enkel de ECB."),
        ]),
    ],
    onthoud=[
        "Inkomensevenwicht: effectieve vraag = Y. Bij C = a + cY en I: Y = (a + I) / (1 − c).",
        "Multiplicator = 1 / (1 − marginale consumptiequote); lekken (sparen, belastingen) maken hem kleiner.",
        "AV daalt; AA stijgt op korte termijn en is verticaal op lange termijn.",
        "Vraagschok: AV verschuift. Aanbodschok: AA verschuift; olieprijs omhoog kan stagflatie geven.",
        "Budgettair beleid: uitgaven en belastingen. Monetair beleid: rente, door de ECB.",
    ])


# ───────────────────────── 19. Inflatie, deflatie en prijsstabiliteit
zet("inflatie-deflatie-en-prijsstabiliteit",
    titel="Inflatie, deflatie en prijsstabiliteit",
    onder="Waarom prijzen stijgen of dalen, hoe je dat meet, en wat de ECB en de overheid ertegen doen.",
    secties=[
        dict(kop="Begrippen", blokken=[
            ("kader", tabel(["begrip", "betekenis"],
                            [["inflatie", "een <strong>algemene en aanhoudende</strong> stijging van het prijspeil"],
                             ["deflatie", "een algemene daling van het prijspeil"],
                             ["stagflatie", "inflatie samen met een stilstaande economie en werkloosheid"],
                             ["krimpflatie (shrinkflation)", "de verpakking wordt kleiner, de prijs blijft gelijk"],
                             ["beknibbelflatie", "de kwaliteit of service daalt, de prijs blijft gelijk"]])),
            ("p", "Krimpflatie zie je dus <strong>niet</strong> aan een hogere prijs op het etiket. Een fles shampoo die van 500 ml "
                  "naar 400 ml gaat voor dezelfde prijs, is per milliliter <strong>25 %</strong> duurder geworden (500 / 400 = 1,25)."),
        ]),
        dict(kop="Soorten inflatie", blokken=[
            ("kader", tabel(["soort", "oorzaak", "voorbeeld"],
                            [["bestedingsinflatie", "de vraag is groter dan wat er geproduceerd kan worden", "sterk stijgende overheidsuitgaven tijdens een hoogconjunctuur"],
                             ["kosteninflatie", "lonen en grondstoffen worden duurder en bedrijven rekenen dat door", "een loonstijging in de bouw"],
                             ["importinflatie", "ingevoerde goederen worden duurder", "de prijs van ingevoerd aardgas verdubbelt"],
                             ["monetaire inflatie", "de geldhoeveelheid stijgt sneller dan de productie", "een land dat geld bijdrukt"],
                             ["conjuncturele inflatie", "volgt de hoog- en laagconjunctuur", ""],
                             ["structurele inflatie", "blijvende kenmerken van een economie", "weinig concurrentie, automatische koppelingen"]])),
        ]),
        dict(kop="De ruilvergelijking van Fisher", blokken=[
            ("kader", "<p style=\"text-align:center\"><strong>M · V = P · T</strong></p>"
                      "<p>M = geldhoeveelheid, V = <strong>omloopsnelheid van het geld</strong>, P = prijspeil, T = het aantal "
                      "transacties.</p>"),
            ("p", "Blijven V en T gelijk en verdubbelt de geldhoeveelheid, dan <strong>verdubbelt het prijspeil</strong>. Zo verklaart "
                  "Fisher monetaire inflatie."),
        ]),
        dict(kop="Inflatie meten", blokken=[
            ("kader", tabel(["index", "meet"],
                            [["consumptieprijsindex (CPI)", "de prijzen van wat gezinnen kopen"],
                             ["HICP", "geharmoniseerde CPI, om de inflatie <strong>tussen EU-landen te vergelijken</strong>"],
                             ["gezondheidsindex", "de CPI <strong>zonder tabak, alcohol, benzine en diesel</strong>"],
                             ["afgevlakte gezondheidsindex", "het gemiddelde van de laatste vier maanden"],
                             ["spilindex", "een drempel: overschrijdt de afgevlakte gezondheidsindex hem, dan worden uitkeringen en ambtenarenlonen aangepast"],
                             ["bbp-deflator", "de prijzen van <strong>alles wat in een land geproduceerd wordt</strong>, ook investeringsgoederen en overheidsdiensten"]])),
            ("kader", "<p style=\"text-align:center\"><strong>inflatie = (nieuwe index − oude index) / oude index · 100</strong></p>"
                      "<ul><li>CPI van 120 naar 126: 6 / 120 · 100 = <strong>5 %</strong>.</li>"
                      "<li>CPI van 150 naar 147: −3 / 150 · 100 = <strong>−2 %</strong> (deflatie).</li></ul>"),
            ("p", "Voor de loonindexering gebruikt België de gezondheidsindex, <strong>om te vermijden dat duurdere tabak, alcohol en "
                  "brandstof de lonen opdrijven</strong>. De spilindex heeft niets met beurskoersen te maken."),
        ]),
        dict(kop="Gevolgen", blokken=[
            ("kader", "<ul><li>Inflatie van 3 % en een loon dat niet stijgt: de <strong>koopkracht daalt met ongeveer 3 %</strong>.</li>"
                      "<li>Bij een onverwacht hoge inflatie verliezen <strong>spaarders met een lage rente</strong> en <strong>mensen met een "
                      "vast inkomen dat niet geïndexeerd wordt</strong>.</li>"
                      "<li>Stijgen de prijzen sneller dan in het buitenland, dan wordt de <strong>export duurder</strong> en daalt de "
                      "concurrentiekracht.</li>"
                      "<li>Bij <strong>deflatie</strong> stellen consumenten aankopen vaak uit, wat de economie verder afremt. Een schuld met "
                      "vaste rente wordt dan <strong>zwaarder</strong> om te dragen, niet lichter. Oorzaken van deflatie zijn bijvoorbeeld "
                      "een sterke daling van de vraag in een crisis of sterk dalende grondstofprijzen.</li></ul>"),
        ]),
        dict(kop="Prijsstabiliteit", blokken=[
            ("p", "De <strong>ECB</strong> streeft een inflatie na van <strong>2 % op middellange termijn</strong>. Is de inflatie te hoog, "
                  "dan <strong>verhoogt ze de beleidsrente</strong>. De ECB kan de btw in België niet verlagen: dat doet de "
                  "nationale overheid."),
            ("kader", tabel(["prijsbeleid van de overheid", "voorbeeld"],
                            [["rechtstreeks", "een maximumprijs voor energie vastleggen"],
                             ["onrechtstreeks", "de btw op energie verlagen, meer concurrentie op een markt toelaten"]])),
            ("weetje", "Stagflatie is lastig: een renteverhoging remt de inflatie af, maar remt ook de groei. Ze kan niet tegelijk "
                       "tegen de inflatie en voor meer groei werken."),
        ]),
    ],
    onthoud=[
        "Inflatie: algemene en aanhoudende prijsstijging. Deflatie: algemene daling. Stagflatie: inflatie + stilstand.",
        "Bestedings-, kosten-, import-, monetaire, conjuncturele en structurele inflatie.",
        "Fisher: M · V = P · T.",
        "Inflatie = (nieuw − oud) / oud · 100. Gezondheidsindex zonder tabak, alcohol en brandstof.",
        "ECB: 2 % op middellange termijn; te hoge inflatie → rente omhoog.",
        "Inflatie treft spaarders en vaste inkomens; deflatie maakt schulden zwaarder.",
    ])


# ───────────────────────── 20. Economisch onderzoek: onderzoeksvraag, methode en besluit
zet("economisch-onderzoek-onderzoeksvraag-methode-en-besluit",
    titel="Economisch onderzoek: onderzoeksvraag, methode en besluit",
    onder="Hoe je zelf een economisch onderzoek opzet, van een goede vraag tot een eerlijk besluit.",
    secties=[
        dict(kop="De onderzoekscyclus", blokken=[
            ("fig", svg.stappen(["oriënteren|de vraag", "voorbereiden|de methode", "uitvoeren|de gegevens",
                                 "rapporteren|het verslag", "reflecteren|terugblikken"], breedte=520),
             "De vijf fasen van de onderzoekscyclus."),
            ("kader", tabel(["fase", "wat doe je"],
                            [["oriënteren", "je verkent het onderwerp en <strong>formuleert je onderzoeksvraag</strong>"],
                             ["voorbereiden", "je <strong>kiest je methode</strong> en maakt een planning"],
                             ["uitvoeren", "je verzamelt en verwerkt de gegevens"],
                             ["rapporteren", "je verwerkt je resultaten in een <strong>verslag of presentatie</strong>"],
                             ["reflecteren", "je kijkt terug: wat ging goed en wat kan beter?"]])),
        ]),
        dict(kop="Een goede onderzoeksvraag", blokken=[
            ("kader", tabel(["eis", "betekenis", "zo niet"],
                            [["open", "niet te beantwoorden met ja of nee", "Is de jeugdwerkloosheid gestegen?"],
                             ["objectief", "geen mening in de vraag", "Waarom is de btw op energie veel te hoog?"],
                             ["enkelvoudig", "één vraag tegelijk", "Hoe evolueerde de inflatie en waarom stegen de lonen?"],
                             ["onderzoekbaar", "je kan ze met gegevens beantwoorden", "Wat zou de werkloosheid zijn als de euro nooit had bestaan?"],
                             ["haalbaar", "te beantwoorden met de tijd en middelen die je hebt", "alle bedrijven van Europa bevragen"],
                             ["relevant", "levert nuttige kennis op voor een bepaalde doelgroep", ""]])),
            ("p", "Een goed voorbeeld: <em>Hoe evolueerde de jeugdwerkloosheid in Limburg sinds 2020?</em>"),
        ]),
        dict(kop="Methodes", blokken=[
            ("kader", tabel(["", "betekenis"],
                            [["kwantitatief onderzoek", "onderzoek <strong>met cijfers</strong>, vaak bij veel mensen"],
                             ["kwalitatief onderzoek", "onderzoek naar <strong>het waarom</strong>, diepgaand bij weinig mensen"]])),
            ("p", "Je kan beide <strong>combineren</strong> in één onderzoek."),
            ("kader", tabel(["methode", "soort", "voorbeeld"],
                            [["deskresearch (bureauonderzoek, literatuuronderzoek)", "<strong>bestaande</strong> gegevens opzoeken", "cijfers van Statbel en de Nationale Bank"],
                             ["enquête", "fieldresearch: elke deelnemer krijgt <strong>dezelfde vragen</strong>", "Hoeveel euro zakgeld krijg je per maand?"],
                             ["interview", "fieldresearch: diepgaand gesprek, goed voor het waarom", "waarom kiezen jongeren voor een bijbaan?"],
                             ["observatie", "fieldresearch: je <strong>kijkt</strong> naar gedrag, zonder vragen te stellen", "een week klanten tellen aan de zelfscankassa"],
                             ["experiment", "fieldresearch: je verandert één ding en vergelijkt", "een prijs aanpassen in de helft van de filialen"]])),
            ("p", "Een interview is dus niet geschikt om duizenden mensen te bevragen. Een <strong>gesuggereerde vraag</strong> zoals "
                  "'Vind jij ook dat de prijzen te hoog zijn?' maakt een enquête minder objectief."),
        ]),
        dict(kop="Populatie, steekproef en variabelen", blokken=[
            ("p", "De <strong>populatie</strong> is <strong>de hele groep waarover je iets wil weten</strong>. Een <strong>steekproef</strong> "
                  "is <strong>het deel van de populatie dat je bevraagt</strong>. Ze is <strong>representatief</strong> als ze een goede "
                  "afspiegeling is van de populatie. Wil je iets weten over Limburgse jongeren en bevraag je enkel je eigen klas, dan "
                  "is je steekproef niet representatief. En uit 10 mensen kan je geen besluit trekken over heel België."),
            ("p", "Een <strong>variabele</strong> is <strong>een kenmerk dat verschillende waarden kan aannemen</strong>. Onderzoek je of de "
                  "prijs van frisdrank invloed heeft op de verkochte hoeveelheid, dan is <strong>de prijs</strong> de onafhankelijke "
                  "variabele en de hoeveelheid de afhankelijke."),
            ("weetje", "Als twee variabelen samen stijgen, bewijst dat <strong>niet</strong> dat de ene de oorzaak is van de andere. In de "
                       "zomer stijgen de verkoop van ijsjes en het aantal zonnebrandflessen samen, maar het ene veroorzaakt het andere niet."),
        ]),
        dict(kop="Het besluit en de bronnen", blokken=[
            ("p", "In het besluit staat <strong>een antwoord op de onderzoeksvraag</strong> en <strong>de beperkingen van het "
                  "onderzoek</strong>."),
            ("p", "Vermeld altijd je bronnen: zo kan <strong>de lezer je gegevens nakijken</strong> en toon je <strong>welk werk van "
                  "anderen komt</strong>."),
        ]),
    ],
    onthoud=[
        "Oriënteren → voorbereiden → uitvoeren → rapporteren → reflecteren.",
        "Een goede onderzoeksvraag is open, objectief, enkelvoudig, onderzoekbaar, haalbaar en relevant.",
        "Kwantitatief = cijfers; kwalitatief = het waarom.",
        "Deskresearch = bestaande gegevens; fieldresearch = enquête, interview, observatie, experiment.",
        "Een representatieve steekproef weerspiegelt de populatie; samen stijgen is geen oorzaak.",
        "Besluit: antwoord + beperkingen. Altijd bronnen vermelden.",
    ])

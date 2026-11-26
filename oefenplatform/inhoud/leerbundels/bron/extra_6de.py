# -*- coding: utf-8 -*-
"""Leer- en oefenbundels bij de zes extra Start-hoofdstukken
"Nog meer voor het 6de leerjaar" (26 november 2026).

Die hoofdstukken vullen Start aan met wat nog ontbrak naast de officiële
minimumdoelen voor het einde van het 6de leerjaar (brochure Minimumdoelen en
visieteksten ... 4de en 6de jaar lager onderwijs, Vlaamse overheid, stand
25/11/2026). De vragen staan in ../../start/bron/*_extra_6de.py.

Alle zes de hoofdstukken heten hetzelfde, dus de bestanden ook: per vak komt
er een nog-meer-voor-het-6de-leerjaar.pdf in de map van dat vak (leerbundels)
en een oefenbundel-nog-meer-voor-het-6de-leerjaar.pdf (oefenbundels). Omdat de
namen gelijk zijn, staat dit niet in een maak_-bestand (maak_alles.py zou ze
over elkaar schrijven) maar heeft het zijn eigen main:

    python3 extra_6de.py
"""
import pathlib, subprocess, sys
HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
import bundel, oefenbundel, svg
from maak_alles import slug

tabel = bundel.tabel
TITEL = "Nog meer voor het 6de leerjaar"
NAAM = "nog-meer-voor-het-6de-leerjaar"
DARK = "#2f4a22"
W, WW = "120px", "200px"


def _svg(b, h, inhoud):
    return f'<svg viewBox="0 0 {b} {h}" width="{b}" xmlns="http://www.w3.org/2000/svg" font-family="Nunito, sans-serif">{inhoud}</svg>'


def assenstelsel():
    """Rooster 0-6 met punt A(3,5) en B(5,2)."""
    s, x0, y0 = 34, 40, 230
    d = []
    for i in range(7):
        d.append(f'<line x1="{x0+i*s}" y1="{y0}" x2="{x0+i*s}" y2="{y0-6*s}" stroke="#d8d2c2"/>')
        d.append(f'<line x1="{x0}" y1="{y0-i*s}" x2="{x0+6*s}" y2="{y0-i*s}" stroke="#d8d2c2"/>')
        d.append(f'<text x="{x0+i*s}" y="{y0+16}" font-size="12" text-anchor="middle">{i}</text>')
        if i:
            d.append(f'<text x="{x0-10}" y="{y0-i*s+4}" font-size="12" text-anchor="end">{i}</text>')
    d.append(f'<line x1="{x0}" y1="{y0}" x2="{x0+6*s+12}" y2="{y0}" stroke="{DARK}" stroke-width="2"/>')
    d.append(f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0-6*s-12}" stroke="{DARK}" stroke-width="2"/>')
    for (px, py, n) in [(3, 5, "A (3, 5)"), (5, 2, "B (5, 2)")]:
        cx, cy = x0 + px * s, y0 - py * s
        d.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="#c4622d"/>')
        d.append(f'<text x="{cx+8}" y="{cy-8}" font-size="13" font-weight="700" fill="{DARK}">{n}</text>')
    d.append(f'<path d="M{x0} {y0-4} h{3*s}" stroke="#7a5aa6" stroke-width="3" fill="none"/>')
    d.append(f'<path d="M{x0+3*s} {y0} v-{5*s}" stroke="#7a5aa6" stroke-width="3" stroke-dasharray="5 4" fill="none"/>')
    return _svg(300, 260, "".join(d))


def ontvouwing_kubus():
    """Kruisvormige bouwplaat van een kubus."""
    s, d = 46, []
    vakjes = [(1, 0), (0, 1), (1, 1), (2, 1), (3, 1), (1, 2)]
    for (c, r) in vakjes:
        d.append(f'<rect x="{20+c*s}" y="{10+r*s}" width="{s}" height="{s}" fill="#e5f4e4" stroke="{DARK}" stroke-width="2"/>')
    return _svg(230, 160, "".join(d))


def maanfasen():
    namen = ["nieuwe maan", "eerste kwartier", "volle maan", "laatste kwartier"]
    d = []
    for i, n in enumerate(namen):
        cx = 60 + i * 110
        d.append(f'<circle cx="{cx}" cy="50" r="30" fill="#3d3d3d" stroke="{DARK}" stroke-width="1.5"/>')
        if i == 2:
            d.append(f'<circle cx="{cx}" cy="50" r="30" fill="#f5e7a8" stroke="{DARK}" stroke-width="1.5"/>')
        elif i == 1:
            d.append(f'<path d="M{cx} 20 A30 30 0 0 1 {cx} 80 Z" fill="#f5e7a8"/>')
        elif i == 3:
            d.append(f'<path d="M{cx} 20 A30 30 0 0 0 {cx} 80 Z" fill="#f5e7a8"/>')
        d.append(f'<text x="{cx}" y="100" font-size="12" text-anchor="middle">{n}</text>')
    return _svg(460, 110, "".join(d))


def zender_ontvanger():
    d = []
    vakken = [("zender", 20), ("boodschap", 170), ("ontvanger", 320)]
    for t, x in vakken:
        d.append(f'<rect x="{x}" y="20" width="120" height="44" rx="12" fill="#e5f4e4" stroke="{DARK}" stroke-width="2"/>')
        d.append(f'<text x="{x+60}" y="47" font-size="14" text-anchor="middle" font-weight="700" fill="{DARK}">{t}</text>')
    for x in (140, 290):
        d.append(f'<path d="M{x+4} 42 h22 m-7 -6 l7 6 l-7 6" stroke="{DARK}" stroke-width="2" fill="none"/>')
    d.append(f'<text x="230" y="90" font-size="12" text-anchor="middle">via een kanaal: stem, brief, gsm, radio ...  Ruis kan storen.</text>')
    return _svg(460, 100, "".join(d))


# ================================================================
# LEERBUNDELS
# ================================================================
BUNDELS = {}

BUNDELS["Wiskunde"] = dict(
    vak="Wiskunde", titel=TITEL,
    onder="Ggd en kgv, rekenen met breuken, bruto en netto, meetkunde en de mediaan.",
    secties=[
        dict(kop="Delers, veelvouden, ggd en kgv", blokken=[
            ("p", r"Een <strong>deler</strong> past precies in een getal: \(4\) is een deler van \(12\). "
                  r"Een <strong>veelvoud</strong> krijg je door te vermenigvuldigen: \(12\) is een veelvoud van \(4\)."),
            ("fig", tabel(["", "Wat je zoekt", "Hoe", "Voorbeeld met 8 en 12"], [
                ["ggd", "grootste gemeenschappelijke deler", "schrijf de delers van allebei op, neem de grootste die in beide rijen staat", r"delers \(8\): 1, 2, 4, 8 — delers \(12\): 1, 2, 3, 4, 6, 12 → ggd = 4"],
                ["kgv", "kleinste gemeenschappelijk veelvoud", "schrijf veelvouden op tot je er een tegenkomt die in beide rijen staat", r"8, 16, 24 … en 12, 24 … → kgv = 24"],
            ]), "Ggd gebruik je om eerlijk te verdelen, kgv om te weten wanneer iets weer samenvalt."),
            ("weetje", "Verdeel je zoveel mogelijk gelijke pakketjes zonder iets over te houden? Dan zoek je de ggd. "
                       "Wanneer vertrekken twee bussen weer tegelijk? Dan zoek je het kgv."),
        ]),
        dict(kop="Breuken met een andere noemer", blokken=[
            ("p", "Breuken optellen of aftrekken kan pas als de noemers gelijk zijn. Zoek een noemer die bij allebei past "
                  "(vaak het kgv van de noemers) en pas teller en noemer aan."),
            ("kader", r"<p style='margin:0 0 4px'><strong>\(\tfrac{1}{3} + \tfrac{1}{4} = \tfrac{4}{12} + \tfrac{3}{12} = \tfrac{7}{12}\)</strong></p>"
                      r"<p style='margin:0'><strong>\(\tfrac{5}{6} - \tfrac{1}{2} = \tfrac{5}{6} - \tfrac{3}{6} = \tfrac{2}{6} = \tfrac{1}{3}\)</strong></p>"),
            ("p", r"<strong>Vermenigvuldigen</strong>: teller maal teller, noemer maal noemer. \(\tfrac{2}{3} \times \tfrac{3}{4} = \tfrac{6}{12} = \tfrac{1}{2}\)."),
            ("p", r"<strong>Delen door een breuk</strong>: tel hoeveel keer de breuk erin past, of vermenigvuldig met het omgekeerde. "
                  r"\(2 : \tfrac{1}{3} = 2 \times 3 = 6\), want in elk geheel passen drie derden."),
            ("weetje", "Noemers tel je nooit op. Twee halve pizza's zijn één pizza, geen 2/4."),
        ]),
        dict(kop="Bruto, netto, tarra en hectare", blokken=[
            ("fig", tabel(["Woord", "Betekenis", "Voorbeeld: pot confituur"], [
                ["bruto", "alles samen, met verpakking", "550 g"],
                ["tarra", "de verpakking", "200 g (de glazen pot)"],
                ["netto", "wat je echt koopt", "350 g confituur"],
            ], "90%"), "Bruto = netto + tarra."),
            ("p", r"Een <strong>are</strong> is \(100\) m², een <strong>hectare</strong> is \(10\,000\) m²: een vierkant van \(100\) m op \(100\) m. "
                  "Velden, bossen en parken meet je in hectare."),
            ("p", "Een <strong>trimester</strong> is 3 maanden, een <strong>semester</strong> 6 maanden. Een jaar heeft 4 trimesters of 2 semesters. "
                  "Een decennium is 10 jaar, een eeuw 100 jaar, een millennium 1000 jaar."),
        ]),
        dict(kop="Hoeken, bouwplaten en coördinaten", blokken=[
            ("p", "Met een <strong>geodriehoek</strong> meet je een hoek tot op de graad: leg het midden op het hoekpunt en de nullijn op één been. "
                  "Scherp is kleiner dan 90°, recht is 90°, stomp ligt tussen 90° en 180°, gestrekt is 180°. "
                  "De drie hoeken van een driehoek zijn samen altijd 180°."),
            ("fig", ontvouwing_kubus(), "Een bouwplaat (ontvouwing) van een kubus: zes gelijke vierkanten. Er bestaan elf verschillende."),
            ("p", "Een balk vouw je uit zes rechthoeken, een cilinder uit twee cirkels en een rechthoek."),
            ("fig", assenstelsel(), "Eerst naar rechts (eerste getal), dan naar boven (tweede getal)."),
        ]),
        dict(kop="Verhoudingstabel, gemiddelde en mediaan", blokken=[
            ("fig", tabel(["schriften", "1", "3", "6", "9"], [["prijs (euro)", "1,50", "4,50", "9,00", "13,50"]], "80%"),
             "In een verhoudingstabel doe je boven en onder telkens hetzelfde: maal 3, maal 2, plus ..."),
            ("p", "Het <strong>gemiddelde</strong>: tel alles op en deel door het aantal. "
                  "De <strong>mediaan</strong>: zet de getallen op volgorde en neem het middelste. Bij een even aantal neem je het midden van de twee middelste."),
            ("kader", r"<p style='margin:0'>Scores \(4, 6, 7, 8, 20\): gemiddelde \(45 : 5 = 9\), mediaan \(7\). Eén uitschieter trekt het gemiddelde omhoog, de mediaan niet.</p>"),
        ]),
    ],
    onthoud=[
        "Ggd: de grootste deler die in beide getallen past. Kgv: het kleinste getal waarin beide passen.",
        "Breuken optellen: eerst de noemers gelijk maken.",
        "Delen door een breuk = vermenigvuldigen met het omgekeerde.",
        "Bruto = netto + tarra. 1 hectare = 10 000 m².",
        "Hoeken van een driehoek: samen 180°.",
        "Coördinaat (3, 5): 3 naar rechts, 5 naar boven.",
        "Mediaan = het middelste getal na het ordenen.",
    ])

BUNDELS["Nederlands"] = dict(
    vak="Nederlands", titel=TITEL,
    onder="Woordrelaties, voorwerpen en gezegdes, hoofdzin en bijzin, communicatie en taalvariatie.",
    secties=[
        dict(kop="Overkoepelende woorden", blokken=[
            ("p", "Sommige woorden zijn een verzamelnaam voor andere: <strong>fruit</strong> is het overkoepelende woord voor appel, peer en banaan. "
                  "Appel, peer en banaan zijn de ondergeschikte woorden. Zo vind je sneller het juiste woord en vermijd je herhaling."),
            ("fig", tabel(["Overkoepelend woord", "Ondergeschikte woorden"], [
                ["gereedschap", "hamer, zaag, tang"], ["instrument", "gitaar, trommel, fluit"], ["meubel", "kast, stoel, bed"]], "80%")),
        ]),
        dict(kop="Voorwerpen en gezegdes", blokken=[
            ("p", "Het <strong>lijdend voorwerp</strong> vind je met: wie of wat + gezegde + onderwerp? "
                  "Het <strong>meewerkend voorwerp</strong> vind je met: aan of voor wie? "
                  "In 'Mama leest mijn zus een verhaal voor' is 'een verhaal' het lijdend voorwerp en 'mijn zus' het meewerkend voorwerp."),
            ("p", "Het <strong>werkwoordelijk gezegde</strong> bestaat uit alle werkwoorden in de zin en zegt wat er gebeurt: 'heeft gelezen'. "
                  "Bij een <strong>naamwoordelijk gezegde</strong> zegt de zin hoe iemand of iets is. Het werkwoord is dan een koppelwerkwoord: "
                  "zijn, worden, blijven, lijken, schijnen, blijken, heten. 'De soep <em>is warm</em>.'"),
        ]),
        dict(kop="Hoofdzin, bijzin en soorten zinnen", blokken=[
            ("p", "Een <strong>hoofdzin</strong> kan alleen staan. Een <strong>bijzin</strong> niet: die hangt aan een hoofdzin en begint vaak met "
                  "omdat, als, dat, wanneer, terwijl of die. In een bijzin staat de persoonsvorm achteraan: '... omdat het <em>regent</em>.'"),
            ("p", "Een <strong>samengestelde zin</strong> bestaat uit meerdere zinnen, aan elkaar gekoppeld met en, maar, want, omdat ..."),
            ("p", "In de <strong>gebiedende wijs</strong> geef je een opdracht. Je gebruikt de stam, zonder onderwerp: 'Kom hier!', 'Word wakker!'"),
            ("p", "De <strong>toekomende tijd</strong> maak je met zullen: 'Ik zal komen.' Voltooid toekomend: 'Ik zal het gedaan hebben.'"),
        ]),
        dict(kop="Communicatie", blokken=[
            ("fig", zender_ontvanger(), "Het communicatiemodel"),
            ("p", "Pas je taal aan wie je ontvanger is: aan een vriend schrijf je informeel, aan de directeur formeel ('Geachte ...')."),
        ]),
        dict(kop="Taal in Vlaanderen en in de wereld", blokken=[
            ("p", "<strong>Standaardnederlands</strong> begrijpt iedereen; je hoort het op het nieuws. Een <strong>dialect</strong> hoort bij één streek. "
                  "<strong>Tussentaal</strong> zit ertussen: 'Hedde gij da gezien?'"),
            ("p", "Talen zijn familie van elkaar. Nederlands, Duits en Engels zijn <strong>Germaanse</strong> talen. "
                  "Frans, Spaans en Italiaans zijn <strong>Romaanse</strong> talen: ze stammen af van het Latijn."),
        ]),
        dict(kop="Informatie opzoeken en verhalen lezen", blokken=[
            ("p", "Vooraan in een boek toont de <strong>inhoudsopgave</strong> de hoofdstukken. Achteraan zoek je één woord op in het <strong>register</strong>. "
                  "Een <strong>legende</strong> legt de tekens van een kaart of grafiek uit. Controleer bij een website wie de tekst schreef en wanneer."),
            ("p", "Een <strong>ik-verteller</strong> maakt het verhaal zelf mee. Een verteller die buiten het verhaal staat, vertelt over 'hij' of 'zij'. "
                  "Een <strong>samenvatting</strong> geeft kort de hoofdzaken, in je eigen woorden, zonder mening."),
        ]),
    ],
    onthoud=[
        "Lijdend voorwerp: wie of wat? Meewerkend voorwerp: aan of voor wie?",
        "Naamwoordelijk gezegde = koppelwerkwoord + hoe iemand of iets is.",
        "Bijzin: persoonsvorm achteraan, kan niet alleen staan.",
        "Gebiedende wijs = de stam: kom, word, ga.",
        "Zender, boodschap, kanaal, ontvanger, ruis.",
        "Dialect, tussentaal, Standaardnederlands.",
    ])

BUNDELS["Wetenschap en techniek"] = dict(
    vak="Wetenschap en techniek", titel=TITEL,
    onder="Dieren en planten indelen, voortplanting, eerlijk onderzoek, energie, duurzaamheid en techniek.",
    secties=[
        dict(kop="Dieren en planten indelen", blokken=[
            ("fig", tabel(["Groep", "Kenmerk", "Voorbeelden"], [
                ["zoogdieren", "haar, jongen drinken melk", "hond, walvis, vleermuis"],
                ["vogels", "veren, snavel, eieren", "mus, pinguïn"],
                ["reptielen", "droge huid met schubben, eieren met schaal", "hagedis, slang, schildpad"],
                ["amfibieën", "naakte vochtige huid, leven in water en op land", "kikker, salamander"],
                ["vissen", "kieuwen, vinnen, schubben", "zalm, haai"],
                ["geleedpotigen (ongewerveld)", "pantser en poten in stukjes", "insecten (6 poten), spinnen (8 poten), krabben"],
            ])),
            ("p", "Planten met bloemen maken <strong>zaden</strong>. Varens en mossen maken <strong>sporen</strong>."),
        ]),
        dict(kop="Voortplanting", blokken=[
            ("p", "<strong>Geslachtelijk</strong>: twee ouders. Bij bloemen komt stuifmeel van de meeldraden op de stamper (bestuiving); daarna groeit er een zaad. "
                  "<strong>Ongeslachtelijk</strong>: één ouder, het jong is een kopie. Denk aan uitlopers van een aardbei of een stek van een geranium."),
            ("p", "Bij de mens versmelten een <strong>zaadcel</strong> en een <strong>eicel</strong> (bevruchting). De baby groeit ongeveer negen maanden in de "
                  "<strong>baarmoeder</strong> en krijgt voedsel en zuurstof via de <strong>navelstreng</strong>. In de <strong>puberteit</strong> verandert een kinderlichaam in dat van een volwassene."),
        ]),
        dict(kop="Onderzoeken als een wetenschapper", blokken=[
            ("fig", svg.stappen(["Vraag|wat wil je weten?", "Hypothese|wat denk je?", "Experiment|testen en meten", "Besluit|klopte het?"]),
             "De onderzoekscyclus"),
            ("p", "Een <strong>eerlijke proef</strong>: verander maar één ding tegelijk en houd de rest gelijk. Herhaal de proef om toeval uit te sluiten. "
                  "Klopt je hypothese niet? Ook dat is een uitkomst."),
        ]),
        dict(kop="Energie en duurzaamheid", blokken=[
            ("p", "Energie kan je niet maken of vernietigen, alleen omzetten. Een batterij bevat <strong>chemische energie</strong>, een kerncentrale haalt energie uit "
                  "het splitsen van uraniumkernen (<strong>kernenergie</strong>), zon en wind raken nooit op."),
            ("p", "Je <strong>ecologische voetafdruk</strong> toont hoeveel van de aarde jouw manier van leven gebruikt. Herstellen, recycleren, lokale seizoensgroenten "
                  "en minder verspillen maken die kleiner. Duurzaam leven betekent: zo leven dat ook later nog genoeg is."),
        ]),
        dict(kop="Techniek: overbrengen, onderhouden en herstellen", blokken=[
            ("fig", svg.hefboom(), "Een hefboom draait rond een draaipunt: zo heb je minder kracht nodig."),
            ("p", "Een <strong>katrol</strong> helpt je een last op te hijsen. Een <strong>ketting</strong> of <strong>riem</strong> brengt een draaiing over. "
                  "Drijft een groot tandwiel een klein aan, dan draait het kleine sneller."),
            ("p", "Onderhoud houdt een toestel langer goed: een ketting smeren, banden oppompen. Wie iets herstelt, trekt eerst de stekker uit en demonteert stap voor stap."),
        ]),
    ],
    onthoud=[
        "Insect: 6 poten. Spin: 8 poten. Allebei geleedpotigen.",
        "Zaadplanten en sporenplanten.",
        "Ongeslachtelijk = één ouder, het jong is een kopie.",
        "Vraag, hypothese, experiment, besluit. Verander één ding tegelijk.",
        "Energie wordt omgezet, niet gemaakt.",
        "Groot tandwiel drijft klein aan: het kleine draait sneller.",
    ])

BUNDELS["Aardrijkskunde"] = dict(
    vak="Aardrijkskunde", titel=TITEL,
    onder="Een aarde in beweging, mensen en welvaart, weer en klimaat, maan en zon, kaarten.",
    secties=[
        dict(kop="Een aarde in beweging", blokken=[
            ("p", "De aardkorst bestaat uit grote <strong>platen</strong> die elk jaar enkele centimeter schuiven. Waar platen botsen of langs elkaar schuren, "
                  "ontstaan <strong>aardbevingen</strong> en <strong>vulkanen</strong>. Rond de Stille Oceaan ligt de <strong>Ring van Vuur</strong> (onder meer Japan, Indonesië, Chili). "
                  "Een beving onder de zee kan een <strong>tsunami</strong> veroorzaken."),
            ("p", "<strong>Delfstoffen</strong> haalt men uit de bodem: steenkool (vroeger in de Limburgse mijnen), aardolie, aardgas, zand, ijzererts."),
        ]),
        dict(kop="Mensen op aarde", blokken=[
            ("p", r"<strong>Bevolkingsdichtheid</strong> = aantal inwoners : oppervlakte in km². België is dichtbevolkt; woestijnen, poolgebieden en hooggebergte niet."),
            ("p", "<strong>Migratie</strong> is verhuizen naar een andere streek of een ander land: voor werk, familie, studie, of op de vlucht voor oorlog en rampen. "
                  "Steeds meer mensen wonen in steden (<strong>verstedelijking</strong>)."),
            ("p", "<strong>Welvaart</strong> gaat over hoe goed mensen kunnen leven: werk, inkomen, onderwijs, zorg, proper water. Die is ongelijk verdeeld over de wereld."),
        ]),
        dict(kop="Weer en klimaat", blokken=[
            ("p", "Het <strong>weer</strong> is hoe het vandaag is. Het <strong>klimaat</strong> is het gemiddelde weer over vele jaren."),
            ("fig", tabel(["Zone", "Waar", "Hoe"], [
                ["tropisch", "tussen de keerkringen, rond de evenaar", "het hele jaar warm"],
                ["gematigd", "tussen keerkring en poolcirkel (ook België)", "vier seizoenen, zacht"],
                ["pool", "voorbij de poolcirkels", "het hele jaar koud"],
            ])),
            ("p", "Extreem weer: orkaan (tyfoon in Azië), hittegolf, zware regen en overstroming, droogte. Door de opwarming van de aarde komt het vaker voor."),
        ]),
        dict(kop="Aarde, maan en zon", blokken=[
            ("fig", maanfasen(), "De maanfasen: in ongeveer een maand zien we telkens een ander stuk van de verlichte helft."),
            ("p", "De maan zorgt voor <strong>eb en vloed</strong>. Bij een <strong>zonsverduistering</strong> schuift de maan tussen aarde en zon; bij een "
                  "<strong>maansverduistering</strong> valt de schaduw van de aarde op de maan."),
            ("p", "Een rondje rond de zon duurt 365 dagen en ongeveer 6 uur: daarom is er om de 4 jaar een <strong>schrikkeljaar</strong>. "
                  "Door de <strong>schuine aardas</strong> zijn er seizoenen, en zijn ze op het zuidelijk halfrond omgekeerd."),
        ]),
        dict(kop="Kaarten en beelden", blokken=[
            ("p", "Een <strong>thematische kaart</strong> toont één onderwerp: neerslag, bevolking, talen. Een <strong>satellietbeeld</strong> is een opname vanuit de ruimte."),
            ("fig", svg.schaalbalk(), "Schaal 1 : 100 000 betekent: 1 cm op de kaart is 100 000 cm = 1 km in het echt."),
        ]),
    ],
    onthoud=[
        "Platen schuiven: aardbevingen en vulkanen, vooral in de Ring van Vuur.",
        "Bevolkingsdichtheid = inwoners : km².",
        "Weer = vandaag, klimaat = gemiddelde over vele jaren.",
        "Nieuwe maan, eerste kwartier, volle maan, laatste kwartier.",
        "Schuine aardas: seizoenen. Schrikkeljaar: om de 4 jaar.",
    ])

BUNDELS["Geschiedenis"] = dict(
    vak="Geschiedenis", titel=TITEL,
    onder="De zes periodes, de hedendaagse tijd, bronnen, perspectieven, democratie en erfgoed.",
    secties=[
        dict(kop="De zes periodes", blokken=[
            ("fig", tabel(["Periode", "Ongeveer", "Bijvoorbeeld"], [
                ["prehistorie", "tot 3000 v.Chr.", "jagers en verzamelaars, eerste boeren, brons en ijzer"],
                ["oudheid", "3000 v.Chr. – 500", "Egypte, Grieken, Romeinen"],
                ["middeleeuwen", "500 – 1500", "burchten, kloosters, steden"],
                ["vroegmoderne tijd", "1500 – 1750", "ontdekkingsreizen, boekdrukkunst, Karel V"],
                ["moderne tijd", "1750 – ongeveer 1950", "stoommachine, fabrieken, wereldoorlogen"],
                ["hedendaagse tijd", "vanaf ongeveer 1950", "Europese samenwerking, internet, ruimtevaart"],
            ]), "De grenzen zijn afspraken: veranderingen gaan geleidelijk."),
        ]),
        dict(kop="De prehistorie", blokken=[
            ("p", "De eerste mensen leefden in Afrika (de Riftvallei). Van daaruit trokken ze over de wereld: de eerste <strong>migraties</strong>. "
                  "Neanderthalers en Homo sapiens leefden een tijd naast elkaar. Later leerde men <strong>brons</strong> maken (koper + tin) en daarna <strong>ijzer</strong>."),
        ]),
        dict(kop="De hedendaagse tijd", blokken=[
            ("p", "Tijdens de Tweede Wereldoorlog was het <strong>Fort van Breendonk</strong> een gevangenkamp en werden vanuit de <strong>Kazerne Dossin</strong> in Mechelen "
                  "Joden en Roma weggevoerd. Er waren <strong>verzetsstrijders</strong> en <strong>collaborateurs</strong>."),
            ("p", "Na de oorlog: de <strong>Verenigde Naties</strong> (1945), de Europese samenwerking (België van bij het begin), de <strong>Muur van Berlijn</strong> (1961–1989)."),
            ("p", "Gelijke rechten: <strong>Rosa Parks</strong> (1955) en de burgerrechtenbeweging, stemrecht voor vrouwen in België (1948), het homohuwelijk. "
                  "<strong>Gastarbeiders</strong> uit onder meer Italië, Marokko en Turkije kwamen werken in mijnen en fabrieken."),
            ("p", "Techniek: <strong>Neil Armstrong</strong> op de maan (1969), het <strong>internet</strong> (vanaf de jaren 1990 overal)."),
        ]),
        dict(kop="Bronnen en perspectieven", blokken=[
            ("fig", tabel(["Soort bron", "Voorbeelden"], [
                ["geschreven", "krant, brief, verdrag, overlijdensbericht"],
                ["materieel", "huis, fabrieksgebouw, graf, voorwerp"],
                ["mondeling", "lied, spreekwoord, gezegde"],
                ["audiovisueel", "film, documentaire, nieuws"],
            ], "85%")),
            ("p", "Een <strong>feit</strong> kan je nagaan, een <strong>mening</strong> niet. Vraag je altijd af wie de bron maakte en waarom. "
                  "Mensen bekijken dezelfde gebeurtenis vanuit een ander <strong>perspectief</strong>: winnaar of verliezer, rijk of arm, man of vrouw."),
            ("weetje", "Rond 1500 was Afonso I koning van het koninkrijk Kongo. Hij had contact met Portugal en zijn zoon werd bisschop."),
        ]),
        dict(kop="Democratie en erfgoed", blokken=[
            ("fig", tabel(["Wie", "Doet wat"], [
                ["parlement", "maakt en stemt de wetten"],
                ["regering", "bestuurt het land en voert de wetten uit"],
                ["rechtbank", "oordeelt onafhankelijk of iemand de wet overtrad"],
                ["grondwet", "de belangrijkste wet, met de rechten van de burgers (sinds 1831)"],
            ], "85%")),
            ("p", "<strong>Erfgoed</strong> is wat we uit het verleden bewaren omdat het mooi of belangrijk is: gebouwen, voorwerpen, maar ook feesten, liederen en recepten."),
        ]),
    ],
    onthoud=[
        "Prehistorie, oudheid, middeleeuwen, vroegmoderne tijd, moderne tijd, hedendaagse tijd.",
        "Breendonk en Kazerne Dossin: plaatsen van herinnering aan de Tweede Wereldoorlog.",
        "Rosa Parks, vrouwenstemrecht 1948, Neil Armstrong 1969.",
        "Geschreven, materiële, mondelinge en audiovisuele bronnen.",
        "Parlement maakt wetten, regering bestuurt, rechtbank oordeelt.",
    ])

BUNDELS["Frans"] = dict(
    vak="Frans", titel=TITEL,
    onder="Passé composé, futur proche, ontkennen, vragen stellen, vrouwelijk en meervoud, de Franstalige wereld.",
    secties=[
        dict(kop="Vroeger, nu en straks", blokken=[
            ("fig", tabel(["Tijd", "Hoe", "Voorbeeld"], [
                ["présent (nu)", "stam + uitgang", "je joue — ik speel"],
                ["passé composé (al gebeurd)", "avoir + voltooid deelwoord", "j'ai joué — ik heb gespeeld"],
                ["futur proche (straks)", "aller + heel werkwoord", "je vais jouer — ik ga spelen"],
            ])),
            ("p", "Het voltooid deelwoord van een werkwoord op -er eindigt op -é: parler → parlé, manger → mangé. "
                  "Bij aller gebruik je être: je suis allé(e)."),
            ("fig", tabel(["", "avoir", "aller"], [
                ["je", "j'ai", "je vais"], ["tu", "tu as", "tu vas"], ["il / elle", "il a", "il va"],
                ["nous", "nous avons", "nous allons"], ["vous", "vous avez", "vous allez"], ["ils / elles", "ils ont", "ils vont"]], "70%")),
        ]),
        dict(kop="Ontkennen en vragen stellen", blokken=[
            ("p", "<strong>ne ... pas</strong> staat rond het werkwoord: je ne parle pas. Voor een klinker: je n'aime pas."),
            ("p", "Een ja-neevraag maak je met <strong>est-ce que</strong> vooraan, of door je stem te laten stijgen: Est-ce que tu viens? / Tu viens?"),
        ]),
        dict(kop="Vrouwelijk en meervoud schrijven", blokken=[
            ("p", "Vrouwelijk: + e (petit → petite). Meervoud: + s (petit → petits). Allebei: + es (petites). "
                  "Die letters hoor je vaak niet, maar je schrijft ze wel."),
        ]),
        dict(kop="De Franstalige wereld", blokken=[
            ("p", "Frans spreekt men in Wallonië en Brussel, in Frankrijk, Zwitserland, Luxemburg, Québec (Canada) en in veel landen in Afrika, zoals Senegal en Congo. "
                  "Wereldwijd zijn dat ongeveer 300 miljoen mensen."),
            ("weetje", "Op 14 juli vieren de Fransen hun nationale feestdag, ter herinnering aan de bestorming van de Bastille in 1789."),
        ]),
    ],
    onthoud=[
        "j'ai joué = al gebeurd, je vais jouer = straks.",
        "ne ... pas rond het werkwoord.",
        "est-ce que maakt een ja-neevraag.",
        "+ e voor vrouwelijk, + s voor meervoud.",
    ])


# ================================================================
# OEFENBUNDELS (andere vragen dan op het scherm)
# ================================================================
HOE = [
    "Schrijf met potlood, dan kan je gerust iets uitgommen.",
    "Het antwoordblad zit achteraan. Scheur het eraf voor je begint.",
]
OEFEN = {}

OEFEN["Wiskunde"] = dict(
    vak="Wiskunde", titel=TITEL, onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE,
    reeksen=[
        dict(kop="Ggd en kgv", opdracht="Schrijf eerst de delers of veelvouden op.", oefeningen=[
            ("rij", [("ggd van 16 en 24", "8"), ("ggd van 9 en 15", "3"), ("ggd van 14 en 21", "7"), ("ggd van 25 en 40", "5")], "Zoek de ggd."),
            ("rij", [("kgv van 6 en 8", "24"), ("kgv van 5 en 7", "35"), ("kgv van 9 en 12", "36"), ("kgv van 4 en 10", "20")], "Zoek het kgv."),
            ("open", "Een vuurtoren flitst om de 6 seconden, een andere om de 9 seconden. Nu flitsen ze samen. Na hoeveel seconden flitsen ze weer samen?", "kgv van 6 en 9 = 18 seconden", 2),
            ("open", "Je hebt 18 rode en 30 blauwe ballonnen. Je maakt zoveel mogelijk gelijke trossen zonder ballonnen over te houden. Hoeveel trossen, en wat zit er in elke tros?", "ggd = 6 trossen, elk 3 rode en 5 blauwe", 2),
        ]),
        dict(kop="Rekenen met breuken", opdracht="Maak de noemers eerst gelijk. Vereenvoudig je antwoord.", oefeningen=[
            ("rij", [(r"\(\tfrac{1}{2} + \tfrac{1}{4}\)", "3/4"), (r"\(\tfrac{2}{3} + \tfrac{1}{6}\)", "5/6"), (r"\(\tfrac{3}{5} - \tfrac{1}{10}\)", "5/10 = 1/2"), (r"\(\tfrac{3}{4} - \tfrac{2}{3}\)", "1/12")]),
            ("rij", [(r"\(\tfrac{1}{2} \times \tfrac{4}{5}\)", "4/10 = 2/5"), (r"\(\tfrac{2}{3} \times \tfrac{3}{8}\)", "6/24 = 1/4"), (r"\(4 : \tfrac{1}{2}\)", "8"), (r"\(\tfrac{3}{4} : \tfrac{1}{8}\)", "6")]),
            ("waar", r"\(\tfrac{1}{3} + \tfrac{1}{3} = \tfrac{2}{6}\)", False),
            ("open", r"Een fles bevat \(\tfrac{3}{4}\) liter. Hoeveel glaasjes van \(\tfrac{1}{8}\) liter kan je ermee vullen?", r"\(\tfrac{3}{4} : \tfrac{1}{8} = 6\) glaasjes", 2),
        ]),
        dict(kop="Bruto, netto, tarra en oppervlakte", oefeningen=[
            ("tabel", ["bruto", "tarra", "netto"], [["750 g", "150 g", None], [None, "80 g", "420 g"], ["2 kg", None, "1 750 g"]], "600 g · 500 g · 250 g", "80px"),
            ("rij", [("3 ha = ... m²", "30 000"), ("25 000 m² = ... ha", "2,5"), ("1 ha = ... are", "100")], "Zet om.", "90px"),
            ("rij", [("2 trimesters = ... maanden", "6"), ("3 semesters = ... maanden", "18"), ("2 eeuwen = ... jaar", "200")], "", "70px"),
        ]),
        dict(kop="Meetkunde", oefeningen=[
            ("rij", [("hoek A = 40°, hoek B = 75°, hoek C = ?", "65°"), ("hoek A = 90°, hoek B = 35°, hoek C = ?", "55°")], "Bereken de derde hoek van de driehoek.", "70px"),
            ("kies", "Welke hoek is stomp?", ["45°", "90°", "120°", "180°"], 2),
            ("teken", "Teken een andere bouwplaat van een kubus dan het kruis uit de leerbundel. Kleur de twee vlakken die tegenover elkaar komen te liggen in dezelfde kleur.", "Er zijn 11 mogelijke bouwplaten; controleer door hem uit te knippen en te vouwen.", 55),
            ("teken", "Teken een assenstelsel van 0 tot 6 en zet de punten P (1, 4), Q (4, 4) en R (4, 1). Verbind ze. Welke figuur krijg je als je er punt S (1, 1) bij zet?", "een vierkant", 60),
        ]),
        dict(kop="Verhoudingen en statistiek", oefeningen=[
            ("tabel", ["liter verf", "2", "4", "10"], [["m² muur", "12", None, None]], "24 · 60", "60px"),
            ("rij", [("mediaan van 3, 9, 4, 8, 6", "6"), ("mediaan van 10, 2, 7, 5", "6"), ("gemiddelde van 4, 6, 8, 10, 12", "8")], "", "60px"),
            ("open", "Vijf kinderen sparen 2, 3, 3, 4 en 28 euro. Geeft het gemiddelde of de mediaan het beste beeld van wat een kind meestal spaart? Leg uit.", "Mediaan 3 euro; het gemiddelde (8 euro) wordt omhooggetrokken door de 28 euro.", 3),
        ]),
    ])

OEFEN["Nederlands"] = dict(
    vak="Nederlands", titel=TITEL, onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE,
    reeksen=[
        dict(kop="Overkoepelende woorden", oefeningen=[
            ("rij", [("eik, beuk, den", "bomen"), ("wortel, prei, sla", "groenten"), ("rok, broek, trui", "kleren"), ("merel, uil, reiger", "vogels")], "Schrijf het overkoepelende woord.", WW),
            ("rij", [("bloem", "bv. tulp, roos, lelie"), ("sport", "bv. tennis, judo, zwemmen")], "Schrijf er drie ondergeschikte woorden bij.", "260px"),
        ]),
        dict(kop="Zinsdelen", opdracht="Onderstreep het gevraagde zinsdeel en schrijf het op.", oefeningen=[
            ("kort", "Lijdend voorwerp: De bakker verkoopt verse broodjes.", "verse broodjes", WW),
            ("kort", "Meewerkend voorwerp: Ik leen mijn buurjongen mijn fiets.", "mijn buurjongen", WW),
            ("kort", "Meewerkend voorwerp: De juf geeft elk kind een rapport.", "elk kind", WW),
            ("kies", "Welke zin heeft een naamwoordelijk gezegde?", ["Mijn opa wandelt elke dag.", "Mijn opa wordt tachtig.", "Mijn opa leest de krant.", "Mijn opa belt mij op."], 1),
            ("kort", "Werkwoordelijk gezegde: Wij zijn gisteren naar zee gereden.", "zijn gereden", WW),
        ]),
        dict(kop="Hoofdzin en bijzin", oefeningen=[
            ("kort", "Onderstreep de bijzin: Als het morgen mooi weer is, gaan we fietsen.", "Als het morgen mooi weer is", "260px"),
            ("open", "Maak één samengestelde zin van: Ik ben moe. Ik heb slecht geslapen. Gebruik 'omdat'.", "Ik ben moe, omdat ik slecht geslapen heb.", 2),
            ("rij", [("(lopen) ... niet zo snel!", "Loop"), ("(worden) ... nu maar wakker!", "Word"), ("(zijn) ... stil!", "Wees")], "Zet in de gebiedende wijs.", "90px"),
            ("rij", [("Ik ... morgen bellen.", "zal"), ("Jullie ... het zien.", "zullen"), ("Zij ... het gedaan hebben.", "zal")], "Vul de vorm van zullen in.", "80px"),
        ]),
        dict(kop="Communicatie en taal", oefeningen=[
            ("tabel", ["Situatie", "Zender", "Ontvanger", "Kanaal"], [["Oma stuurt jou een kaartje.", None, None, None], ["De burgemeester spreekt op tv.", None, None, None]],
             "oma · jij · kaartje (post) / de burgemeester · de kijkers · tv", "100px"),
            ("open", "Herschrijf in Standaardnederlands: 'Ge moet da ni doen, gast!'", "Je moet dat niet doen, jongen!", 2),
            ("rij", [("Duits", "Germaans"), ("Spaans", "Romaans"), ("Engels", "Germaans"), ("Italiaans", "Romaans")], "Germaans of Romaans?", WW),
        ]),
        dict(kop="Opzoeken en lezen", oefeningen=[
            ("kies", "Je zoekt in een dierenboek op welke bladzijde het woord 'vleermuis' staat. Waar kijk je?", ["in de inhoudsopgave", "op de kaft", "in het register", "in het voorwoord"], 2),
            ("open", "Schrijf een samenvatting van twee zinnen van een sprookje dat je goed kent.", "Eigen antwoord: alleen de hoofdzaken, geen mening.", 3),
            ("kies", "'Ze opende de doos en hield haar adem in.' Welke verteller is dit?", ["een ik-verteller", "een verteller buiten het verhaal", "een dialoog", "een gedicht"], 1),
        ]),
    ])

OEFEN["Wetenschap en techniek"] = dict(
    vak="Wetenschap en techniek", titel=TITEL, onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE,
    reeksen=[
        dict(kop="Dieren en planten indelen", oefeningen=[
            ("rij", [("krokodil", "reptiel"), ("salamander", "amfibie"), ("mier", "geleedpotige / insect"), ("vleermuis", "zoogdier"), ("kreeft", "geleedpotige")], "Bij welke groep hoort dit dier?", WW),
            ("waar", "Een varen maakt zaden.", False),
            ("open", "Noem twee verschillen tussen een insect en een spin.", "insect 6 poten, spin 8; insect drie lichaamsdelen, spin twee; insect heeft voelsprieten", 2),
        ]),
        dict(kop="Voortplanting", oefeningen=[
            ("rij", [("aardbei met uitlopers", "ongeslachtelijk"), ("appelboom na bestuiving", "geslachtelijk"), ("stek van een vetplant", "ongeslachtelijk")], "Geslachtelijk of ongeslachtelijk?", WW),
            ("open", "Waarvoor dient de navelstreng?", "Ze brengt voedsel en zuurstof van de moeder naar de baby.", 2),
            ("kies", "Wat moet er gebeuren voor er een zaad groeit in een bloem?", ["stuifmeel op de stamper", "veel zon op de blaadjes", "water op de wortels", "een stek in de grond"], 0),
        ]),
        dict(kop="Een eerlijke proef", oefeningen=[
            ("open", "Lena wil weten of zout water sneller bevriest dan gewoon water. Schrijf haar onderzoeksvraag en een hypothese.", "Vraag: bevriest zout water sneller dan gewoon water? Hypothese: bv. zout water bevriest trager.", 3),
            ("open", "Wat moet Lena gelijk houden zodat haar proef eerlijk is? Noem er drie.", "evenveel water, dezelfde bakjes, dezelfde plaats in de diepvries, dezelfde tijd", 2),
            ("waar", "Als je proef iets anders oplevert dan je hypothese, mag je de uitkomst aanpassen.", False),
        ]),
        dict(kop="Energie en duurzaamheid", oefeningen=[
            ("rij", [("zonnepaneel", "licht → elektrisch"), ("batterij in een zaklamp", "chemisch → elektrisch → licht"), ("fietsdynamo", "beweging → elektrisch")], "Welke energie wordt in welke omgezet?", "220px"),
            ("open", "Noem drie dingen die jij deze week kan doen om je ecologische voetafdruk kleiner te maken.", "bv. fietsen i.p.v. auto, licht uit, herstellen, lokaal eten, minder verspillen", 3),
        ]),
        dict(kop="Techniek", oefeningen=[
            ("kies", "Een klein tandwiel drijft een groot tandwiel aan. Wat doet het grote?", ["het draait sneller", "het draait trager", "het staat stil", "het draait even snel"], 1),
            ("rij", [("notenkraker", "hefboom"), ("vlaggenmast", "katrol"), ("fiets", "ketting en tandwielen")], "Welke techniek zit erin?", WW),
            ("open", "Je fietslicht werkt niet meer. Schrijf in drie stappen hoe je zoekt wat er mis is.", "bv. 1) lampje controleren 2) draadjes en contacten nakijken 3) batterij of dynamo testen", 3),
        ]),
    ])

OEFEN["Aardrijkskunde"] = dict(
    vak="Aardrijkskunde", titel=TITEL, onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE + ["Een atlas mag je erbij nemen."],
    reeksen=[
        dict(kop="Een aarde in beweging", oefeningen=[
            ("rij", [("Japan", "ja"), ("Nederland", "nee"), ("Chili", "ja"), ("Indonesië", "ja")], "Ligt dit land in de Ring van Vuur?", "70px"),
            ("open", "Leg in je eigen woorden uit hoe een aardbeving ontstaat.", "Platen duwen of schuren tegen elkaar; de spanning bouwt op en komt plots vrij.", 3),
            ("rij", [("brandstof voor de auto", "aardolie"), ("glas maken", "zand"), ("vroeger uit de Limburgse mijnen", "steenkool")], "Welke delfstof?", WW),
        ]),
        dict(kop="Mensen op aarde", oefeningen=[
            ("tabel", ["Gebied", "Inwoners", "km²", "Inwoners per km²"], [["A", "6 000", "20", None], ["B", "900", "30", None]], "300 · 30", "70px"),
            ("open", "Noem twee redenen waarom mensen naar een ander land verhuizen.", "bv. werk, familie, studie, oorlog, rampen", 2),
            ("waar", "Welvaart is overal ter wereld even groot.", False),
        ]),
        dict(kop="Weer en klimaat", oefeningen=[
            ("rij", [("Het sneeuwt vandaag in Brussel.", "weer"), ("In de Sahara regent het bijna nooit.", "klimaat"), ("Morgen wordt het 25 graden.", "weer")], "Weer of klimaat?", "100px"),
            ("kies", "In welke zone ligt het tropisch regenwoud?", ["poolzone", "gematigde zone", "tropische zone", "woestijnzone"], 2),
        ]),
        dict(kop="Aarde, maan en zon", oefeningen=[
            ("teken", "Teken de vier maanfasen in de juiste volgorde, te beginnen bij nieuwe maan. Schrijf de naam eronder.", "nieuwe maan, eerste kwartier, volle maan, laatste kwartier", 40),
            ("rij", [("2028", "ja"), ("2030", "nee"), ("2032", "ja")], "Schrikkeljaar? (Tip: deelbaar door 4)", "60px"),
            ("open", "Als het in België zomer is, is het in Argentinië winter. Waarom?", "Argentinië ligt op het zuidelijk halfrond; door de schuine aardas zijn de seizoenen er omgekeerd.", 2),
        ]),
        dict(kop="Kaarten", oefeningen=[
            ("rij", [("schaal 1 : 50 000, 4 cm", "2 km"), ("schaal 1 : 10 000, 7 cm", "700 m"), ("schaal 1 : 200 000, 3 cm", "6 km")], "Hoeveel is dat in het echt?", WW),
            ("kies", "Welke kaart toon je om te zien waar in België het meest mensen wonen?", ["een fietskaart", "een thematische kaart", "een stratenplan", "een plattegrond"], 1),
        ]),
    ])

OEFEN["Geschiedenis"] = dict(
    vak="Geschiedenis", titel=TITEL, onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE,
    reeksen=[
        dict(kop="De zes periodes", oefeningen=[
            ("rij", [("eerste boeren", "prehistorie"), ("Romeinse legers", "oudheid"), ("burchten en ridders", "middeleeuwen"), ("Columbus vaart naar Amerika", "vroegmoderne tijd"), ("eerste fabrieken", "moderne tijd"), ("smartphones", "hedendaagse tijd")], "In welke periode hoort dit?", WW),
            ("open", "Zet in de juiste volgorde: moderne tijd, oudheid, hedendaagse tijd, prehistorie, vroegmoderne tijd, middeleeuwen.", "prehistorie, oudheid, middeleeuwen, vroegmoderne tijd, moderne tijd, hedendaagse tijd", 2),
        ]),
        dict(kop="De hedendaagse tijd", oefeningen=[
            ("rij", [("1948", "vrouwen mogen stemmen voor het parlement in België"), ("1955", "Rosa Parks weigert haar plaats op de bus af te staan"), ("1969", "Neil Armstrong op de maan"), ("1989", "de Muur van Berlijn valt")], "Wat gebeurde er?", "300px"),
            ("open", "Wat is het verschil tussen een verzetsstrijder en een collaborateur?", "Een verzetsstrijder vecht tegen de bezetter, een collaborateur werkt met de bezetter samen.", 2),
            ("open", "Vraag aan een (groot)ouder of je ooit een gastarbeider of een kind van gastarbeiders kende. Schrijf op wat je te weten kwam.", "Eigen antwoord.", 3),
        ]),
        dict(kop="Bronnen", oefeningen=[
            ("rij", [("een oud schoolschrift", "geschreven"), ("een kerkhof", "materieel"), ("een volksliedje", "mondeling"), ("journaalbeelden", "audiovisueel")], "Welke soort bron?", WW),
            ("rij", [("België werd onafhankelijk in 1830.", "feit"), ("Vroeger was alles beter.", "mening"), ("De Muur van Berlijn viel in 1989.", "feit")], "Feit of mening?", "90px"),
        ]),
        dict(kop="Democratie en erfgoed", oefeningen=[
            ("rij", [("stemt de wetten", "parlement"), ("oordeelt over een misdaad", "rechtbank"), ("bestuurt het land", "regering")], "Wie doet dit?", WW),
            ("open", "Noem een stuk erfgoed uit jouw gemeente of streek, en zeg waarom we het bewaren.", "Eigen antwoord, bv. een kerk, molen, mijnsite, stoet, gerecht.", 3),
        ]),
    ])

OEFEN["Frans"] = dict(
    vak="Frans", titel=TITEL, onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE,
    reeksen=[
        dict(kop="Passé composé", opdracht="Zet in de passé composé.", oefeningen=[
            ("rij", [("je chante", "j'ai chanté"), ("tu regardes", "tu as regardé"), ("nous jouons", "nous avons joué"), ("ils parlent", "ils ont parlé")], "", WW),
            ("kort", "Hier, elle ... (aller) à la piscine.", "est allée", WW),
        ]),
        dict(kop="Futur proche", opdracht="Zet in de futur proche: wat gaat er gebeuren?", oefeningen=[
            ("rij", [("je mange", "je vais manger"), ("vous dansez", "vous allez danser"), ("elles nagent", "elles vont nager")], "", WW),
            ("kies", "Welke zin gaat over straks?", ["J'ai fini.", "Je finis.", "Je vais finir.", "Je ne finis pas."], 2),
        ]),
        dict(kop="Ontkennen en vragen", oefeningen=[
            ("rij", [("Je regarde la télé.", "Je ne regarde pas la télé."), ("Il aime les chats.", "Il n'aime pas les chats."), ("Nous allons au parc.", "Nous n'allons pas au parc.")], "Maak ontkennend.", "260px"),
            ("rij", [("Tu as faim.", "Est-ce que tu as faim?"), ("Il joue au foot.", "Est-ce qu'il joue au foot?")], "Maak er een vraag van met est-ce que.", "260px"),
        ]),
        dict(kop="Vrouwelijk en meervoud", oefeningen=[
            ("rij", [("une robe (vert)", "verte"), ("des chiens (noir)", "noirs"), ("des fleurs (petit)", "petites"), ("un garçon (grand)", "grand")], "Schrijf het bijvoeglijk naamwoord juist.", "100px"),
        ]),
        dict(kop="De Franstalige wereld", oefeningen=[
            ("rij", [("Québec", "Canada"), ("Dakar", "Senegal"), ("Namen", "België"), ("Genève", "Zwitserland")], "In welk land ligt deze Franstalige stad?", WW),
            ("waar", "In Brussel spreken mensen zowel Frans als Nederlands.", True),
        ]),
    ])


def maak():
    gemaakt = []
    for soort, lijst, maker, basis, naam in (
        ("leerbundel", BUNDELS, bundel, HIER.parent, NAAM),
        ("oefenbundel", OEFEN, oefenbundel, HIER.parent.parent / "oefenbundels", "oefenbundel-" + NAAM),
    ):
        for vak, b in lijst.items():
            tijdelijk = f"{naam}-{slug(vak)}"
            maker.schrijf(b, tijdelijk)
            subprocess.run(["node", str(HIER / "pdf.js"), tijdelijk], cwd=HIER, check=True)
            doel = basis / slug(vak)
            doel.mkdir(parents=True, exist_ok=True)
            (doel / f"{naam}.pdf").write_bytes((HIER / f"{tijdelijk}.pdf").read_bytes())
            gemaakt.append(f"{doel.relative_to(HIER.parent.parent)}/{naam}.pdf")
    for g in gemaakt:
        print("  ", g)


if __name__ == "__main__":
    maak()

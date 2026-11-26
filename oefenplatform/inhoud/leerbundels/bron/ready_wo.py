# -*- coding: utf-8 -*-
"""Leer- en oefenbundels bij de Ready-hoofdstukken wereldoriëntatie (3de en 4de
leerjaar): wetenschap en techniek, aardrijkskunde en geschiedenis. De vragen op het
scherm staan in ../../ready/bron/wt_*.py, ak_*.py en gs_*.py.

    python3 ready_wo.py              # alles
    python3 ready_wo.py planten      # één hoofdstuk
"""
import math, sys
from ready_gemeen import met_prenten, maak, tabel, svg, READY, DARK, ORANJE, PAARS, GROEN

HOE = ["Schrijf met potlood, dan kan je gerust iets uitgommen.",
       "Lees elke opdracht eerst helemaal voor je begint.",
       "Het antwoordblad zit achteraan. Scheur het eraf voor je begint."]
B = "140px"
ON = "{aantal} oefeningen op papier, met een antwoordblad achteraan."


def plant(labels=True):
    t = (lambda x, y, s: f'<text x="{x}" y="{y}" font-size="13" fill="{DARK}">{s}</text>') if labels else (lambda x, y, s: f'<line x1="{x - 4}" y1="{y - 4}" x2="{x + 70}" y2="{y - 4}" stroke="#999" stroke-dasharray="3 3"/>')
    d = [f'<rect x="0" y="150" width="260" height="60" fill="#e9d8bf"/>',
         f'<path d="M100 150 L80 185 M100 150 L100 200 M100 150 L120 190 M90 168 L70 175" stroke="#8a5a2b" stroke-width="3" fill="none"/>',
         f'<line x1="100" y1="150" x2="100" y2="50" stroke="{GROEN}" stroke-width="5"/>',
         f'<ellipse cx="75" cy="110" rx="24" ry="10" fill="{GROEN}" transform="rotate(-25 75 110)"/>',
         f'<ellipse cx="125" cy="95" rx="24" ry="10" fill="{GROEN}" transform="rotate(25 125 95)"/>']
    for i in range(6):
        a = math.radians(i * 60)
        d.append(f'<circle cx="{100 + 13 * math.cos(a):.1f}" cy="{40 + 13 * math.sin(a):.1f}" r="10" fill="#f3b3c8"/>')
    d.append(f'<circle cx="100" cy="40" r="8" fill="#f2c94c"/>')
    d += [t(150, 44, "bloem"), t(150, 100, "blad"), t(150, 135, "stengel"), t(150, 190, "wortel")]
    d += [f'<line x1="146" y1="40" x2="114" y2="40" stroke="{DARK}"/>', f'<line x1="146" y1="96" x2="140" y2="96" stroke="{DARK}"/>',
          f'<line x1="146" y1="131" x2="104" y2="131" stroke="{DARK}"/>', f'<line x1="146" y1="186" x2="118" y2="186" stroke="{DARK}"/>']
    return svg(260, 210, "".join(d), 260)


def kompasroos(leeg=False):
    c = 80
    d = [f'<circle cx="{c}" cy="{c}" r="60" fill="#fff" stroke="{DARK}" stroke-width="2"/>',
         f'<polygon points="{c},{c - 55} {c + 10},{c} {c},{c + 55} {c - 10},{c}" fill="{ORANJE}"/>',
         f'<polygon points="{c - 55},{c} {c},{c - 10} {c + 55},{c} {c},{c + 10}" fill="{DARK}"/>']
    if not leeg:
        d += [f'<text x="{c}" y="14" font-size="16" font-weight="700" text-anchor="middle">N</text>',
              f'<text x="{c}" y="158" font-size="16" font-weight="700" text-anchor="middle">Z</text>',
              f'<text x="152" y="{c + 6}" font-size="16" font-weight="700" text-anchor="middle">O</text>',
              f'<text x="8" y="{c + 6}" font-size="16" font-weight="700" text-anchor="middle">W</text>']
    else:
        d.append(f'<text x="{c}" y="14" font-size="16" font-weight="700" text-anchor="middle">N</text>')
    return svg(160, 162, "".join(d), 170)


def tijdsbalk(punten, leeg=False):
    d = [f'<line x1="10" y1="40" x2="590" y2="40" stroke="{DARK}" stroke-width="3"/>',
         f'<polygon points="590,32 604,40 590,48" fill="{DARK}"/>']
    for i, (x, boven, onder) in enumerate(punten):
        d.append(f'<line x1="{x}" y1="30" x2="{x}" y2="50" stroke="{ORANJE}" stroke-width="3"/>')
        d.append(f'<text x="{x}" y="22" font-size="13" text-anchor="middle" fill="{DARK}">{boven}</text>')
        if not leeg:
            d.append(f'<text x="{x}" y="70" font-size="12" text-anchor="middle" fill="{DARK}">{onder}</text>')
    return svg(610, 80, "".join(d), 610)


def stroomkring(open_=False):
    d = [f'<rect x="20" y="60" width="60" height="30" rx="4" fill="#f2c94c" stroke="{DARK}" stroke-width="2"/>',
         f'<text x="50" y="80" font-size="12" text-anchor="middle">batterij</text>',
         f'<circle cx="220" cy="40" r="16" fill="#fff6c8" stroke="{DARK}" stroke-width="2"/>',
         f'<text x="220" y="16" font-size="12" text-anchor="middle">lampje</text>',
         f'<polyline points="80,70 140,70 140,40 204,40" fill="none" stroke="{ORANJE}" stroke-width="3"/>']
    if open_:
        d.append(f'<polyline points="236,40 260,40 260,110 170,110" fill="none" stroke="{ORANJE}" stroke-width="3"/>'
                 f'<polyline points="140,110 20,110 20,80" fill="none" stroke="{ORANJE}" stroke-width="3"/>'
                 f'<text x="155" y="130" font-size="12" text-anchor="middle">open</text>')
    else:
        d.append(f'<polyline points="236,40 260,40 260,110 20,110 20,80" fill="none" stroke="{ORANJE}" stroke-width="3"/>')
    return svg(280, 140, "".join(d), 260)


H = {}
# ================================================================ wetenschap en techniek
H["planten"] = ("planten-en-dieren-ready", "wetenschap-en-techniek", dict(
    vak="Wetenschap en techniek", niveau=READY, titel="Planten en dieren",
    onder="Delen van een plant, wat een plant nodig heeft, van zaadje tot plant, dieren groeperen en wie eet wie.",
    secties=[
        dict(kop="De delen van een plant", blokken=[("fig", plant()),
            ("fig", tabel(["Deel", "Wat doet het?"], [["wortel", "haalt water uit de grond en houdt de plant vast"], ["stengel", "brengt water naar boven en houdt de plant recht"],
                ["blad", "maakt voedsel met zonlicht"], ["bloem", "daaruit groeien vrucht en zaadjes"]], "100%"))]),
        dict(kop="Wat heeft een plant nodig?", blokken=[("p", "<strong>Water, licht, lucht</strong> en voedingsstoffen uit de grond. Zonder licht wordt een plant bleek en zwak."),
            ("p", "Van zaadje tot plant: <strong>zaadje → kiemen → groeien → bloeien → vrucht met nieuwe zaadjes</strong>. Bijen helpen door stuifmeel van bloem naar bloem te brengen.")]),
        dict(kop="Dieren groeperen", blokken=[("fig", tabel(["Groep", "Herken je aan", "Voorbeelden"], [
            ["zoogdieren", "haar, jongen drinken melk", "hond, koe, walvis"], ["vogels", "veren, eieren, vleugels", "mus, kip, pinguïn"],
            ["vissen", "schubben, kieuwen", "forel, haai"], ["amfibieën", "jong in water, later ook op land", "kikker, salamander"],
            ["reptielen", "droge schubben, eieren", "slang, hagedis"], ["insecten", "6 poten", "mier, bij, vlinder"]], "100%")),
            ("weetje", "Een spin heeft 8 poten. Ze is dus geen insect.")]),
        dict(kop="Wie eet wie?", blokken=[("p", "<strong>Planteneters</strong> eten planten (konijn), <strong>vleeseters</strong> eten dieren (vos), <strong>alleseters</strong> eten allebei (mens, varken)."),
            ("kader", "Voedselketen: gras → konijn → vos<br>De pijl betekent: wordt opgegeten door.")]),
    ],
    onthoud=["Wortel, stengel, blad, bloem.", "Een plant heeft water, licht en lucht nodig.", "Zoogdieren, vogels, vissen, amfibieën, reptielen, insecten.", "Gras → konijn → vos."]),
    dict(vak="Wetenschap en techniek", niveau=READY, titel="Planten en dieren", onder=ON, hoe=HOE, reeksen=[
        dict(kop="De plant", oefeningen=[("fig", [(plant(False), "bloem, blad, stengel, wortel")], "Schrijf bij elke streep het juiste deel van de plant."),
            ("rij", [("Wat haalt water uit de grond?", "de wortel"), ("Wat maakt voedsel met licht?", "het blad")], "", B)]),
        dict(kop="Van zaadje tot plant", oefeningen=[("open", "Zet in de juiste volgorde: bloeien – zaadje – vrucht – kiemen – groeien.", "zaadje – kiemen – groeien – bloeien – vrucht", 1),
            ("teken", "Doe een proef: leg een boon op nat watten in een potje. Teken wat je na 3 dagen en na 7 dagen ziet.", "eigen tekening: worteltje, daarna stengel en blaadjes", 45)]),
        dict(kop="Dieren groeperen", oefeningen=[("tekst", "Schrijf elk dier in de juiste kolom: koe – uil – forel – mier – dolfijn – eend – haai – bij"),
            ("tabel", ["zoogdier", "vogel", "vis", "insect"], [[None, None, None, None], [None, None, None, None]],
            "zoogdier: koe, dolfijn · vogel: uil, eend · vis: forel, haai · insect: mier, bij", "110px"),
            ("waar", "Een spin is een insect.", False), ("waar", "Een walvis is een zoogdier.", True)]),
        dict(kop="Levenscyclus", oefeningen=[("open", "Zet in volgorde: vlinder – rups – ei – pop.", "ei – rups – pop – vlinder", 1),
            ("open", "Zet in volgorde: kikker – kikkerdril – kikkervisje.", "kikkerdril – kikkervisje – kikker", 1)]),
        dict(kop="Wie eet wie?", oefeningen=[("rij", [("koe", "planteneter"), ("vos", "vleeseter"), ("mens", "alleseter"), ("konijn", "planteneter")], "Planteneter, vleeseter of alleseter?", B),
            ("open", "Maak een voedselketen met: uil – graan – muis.", "graan → muis → uil", 1)]),
    ]))

H["lichaam"] = ("mijn-lichaam-ready", "wetenschap-en-techniek", dict(
    vak="Wetenschap en techniek", niveau=READY, titel="Mijn lichaam",
    onder="Zintuigen, botten en spieren, hart en longen, en gezond leven.",
    secties=[
        dict(kop="Vijf zintuigen", blokken=[("fig", tabel(["Zintuig", "Lichaamsdeel", "Voorbeeld"], [["zien", "ogen", "kleuren en vormen"], ["horen", "oren", "een vogel die fluit"],
            ["ruiken", "neus", "verse koekjes"], ["proeven", "tong", "zoet, zout, zuur, bitter"], ["voelen", "huid", "warm, koud, ruw, zacht"]], "100%")),
            ("weetje", "Met een verstopte neus proef je minder: ruiken en proeven werken samen.")]),
        dict(kop="Botten en spieren", blokken=[("p", "Al je botten samen vormen je <strong>skelet</strong>. De <strong>schedel</strong> beschermt je hersenen, de <strong>ribben</strong> je hart en longen. Waar botten samenkomen, zit een <strong>gewricht</strong> (knie, elleboog)."),
            ("p", "<strong>Spieren</strong> trekken aan je botten. Zo kan je bewegen.")]),
        dict(kop="Hart en longen", blokken=[("p", "Je <strong>hart</strong> pompt bloed rond. Met je <strong>longen</strong> adem je zuurstof in. Na het lopen klopt je hart sneller: voel maar aan je pols.")]),
        dict(kop="Gezond leven", blokken=[("kader", "🥦 Veel groenten en fruit, water drinken<br>🏃 Elke dag bewegen<br>😴 9 tot 11 uur slapen<br>🪥 Twee keer per dag tanden poetsen<br>🧼 Handen wassen voor het eten en na het toilet")]),
    ],
    onthoud=["Zien, horen, ruiken, proeven, voelen.", "Skelet, spieren en gewrichten laten je bewegen.", "Hart pompt bloed, longen ademen.", "Gezond eten, bewegen, slapen en poetsen."]),
    dict(vak="Wetenschap en techniek", niveau=READY, titel="Mijn lichaam", onder=ON, hoe=HOE, reeksen=[
        dict(kop="Zintuigen", oefeningen=[("rij", [("de geur van soep", "ruiken, neus"), ("een zachte kat", "voelen, huid"), ("een zure citroen", "proeven, tong"), ("de bel van school", "horen, oren")], "Welk zintuig gebruik je? Met welk lichaamsdeel?", "170px")]),
        dict(kop="Mijn lichaam", oefeningen=[("rij", [("beschermt je hersenen", "schedel"), ("beschermen hart en longen", "ribben"), ("knie of elleboog", "gewricht"), ("pompt bloed rond", "hart")], "Welk woord past?", B),
            ("open", "Tel je hartslag 15 seconden aan je pols in rust. Spring dan 1 minuut en tel opnieuw. Wat merk je?", "Na het springen klopt je hart sneller.", 2)]),
        dict(kop="Gezond of niet?", opdracht="Telkens is één keuze gezond en één niet. Streep de ongezonde keuze door.", oefeningen=[
            ("invulwoord", [("water &nbsp; / &nbsp; cola", "water"), ("een appel &nbsp; / &nbsp; een zak chips", "een appel"), ("om 21 uur slapen &nbsp; / &nbsp; tot middernacht gamen", "om 21 uur slapen"),
                            ("buiten spelen &nbsp; / &nbsp; de hele dag zitten", "buiten spelen")], "")]),
        dict(kop="Schrijf zelf", oefeningen=[("open", "Schrijf drie dingen die jij elke dag doet om gezond te blijven.", "eigen antwoord", 3)]),
    ]))

H["stoffen"] = ("stoffen-en-materialen-ready", "wetenschap-en-techniek", dict(
    vak="Wetenschap en techniek", niveau=READY, titel="Stoffen en materialen",
    onder="Vast, vloeibaar en gas, smelten en bevriezen, drijven en zinken, magneten en materialen.",
    secties=[
        dict(kop="Vast, vloeibaar of gas", blokken=[("fig", tabel(["Vast", "Vloeibaar", "Gas"], [["houdt zijn vorm", "neemt de vorm van de beker aan", "vult de hele ruimte"], ["ijs, steen, hout", "water, melk, olie", "lucht, waterdamp"]], "100%")),
            ("kader", "ijs —<em>smelten</em>→ water —<em>verdampen</em>→ waterdamp<br>waterdamp —<em>afkoelen</em>→ water —<em>bevriezen</em>→ ijs")]),
        dict(kop="Drijven en zinken", blokken=[("p", "Een kurk en hout drijven. Een sleutel en een knikker zinken. Niet alleen het gewicht telt: een groot ijzeren schip drijft door zijn holle vorm.")]),
        dict(kop="Magneten", blokken=[("p", "Een magneet trekt <strong>ijzer</strong> aan, geen papier, hout of plastic. Elke magneet heeft een <strong>noordpool</strong> en een <strong>zuidpool</strong>: gelijke polen stoten af, verschillende trekken aan.")]),
        dict(kop="Materialen", blokken=[("fig", tabel(["Materiaal", "Eigenschap", "Gebruik"], [["glas", "doorzichtig", "venster"], ["metaal", "geleidt warmte", "kookpot"], ["plastic, rubber", "waterdicht", "regenjas, laarzen"], ["hout", "sterk, natuurlijk", "stoel, tafel"]], "100%")),
            ("p", "Zout en suiker <strong>lossen op</strong> in water, zand niet.")]),
    ],
    onthoud=["Vast, vloeibaar, gas.", "Smelten, bevriezen, verdampen.", "Magneet trekt ijzer aan.", "Elk materiaal heeft een eigenschap die past bij wat je ermee maakt."]),
    dict(vak="Wetenschap en techniek", niveau=READY, titel="Stoffen en materialen", onder=ON, hoe=HOE, reeksen=[
        dict(kop="Vast, vloeibaar of gas?", oefeningen=[("rij", [("sap", "vloeibaar"), ("een steen", "vast"), ("stoom", "gas"), ("boter in de koelkast", "vast"), ("olie", "vloeibaar"), ("lucht in een ballon", "gas")], "", B)]),
        dict(kop="Wat gebeurt er?", oefeningen=[("rij", [("ijs in de zon", "smelten"), ("water in de diepvries", "bevriezen"), ("een plas op een warme dag", "verdampen")], "Schrijf: smelten, bevriezen of verdampen.", B)]),
        dict(kop="Proef: drijven of zinken", opdracht="Voorspel eerst, test daarna in een kom water.", oefeningen=[
            ("tabel", ["Voorwerp", "Ik denk", "Ik zag"], [["kurk", None, None], ["sleutel", None, None], ["appel", None, None], ["knikker", None, None]], "kurk drijft · sleutel zinkt · appel drijft · knikker zinkt", "110px")]),
        dict(kop="Magneten", oefeningen=[("rij", [("een paperclip", "ja"), ("een gom", "nee"), ("een ijzeren spijker", "ja"), ("een houten blokje", "nee")], "Trekt een magneet het aan? Schrijf ja of nee.", "80px"),
            ("waar", "Twee noordpolen trekken elkaar aan.", False)]),
        dict(kop="Welk materiaal?", oefeningen=[("rij", [("een regenjas", "plastic of rubber"), ("een venster", "glas"), ("een kookpot", "metaal")], "Van welk materiaal maak je het best?", B),
            ("open", "Roer een lepel zout in water en een lepel zand in water. Wat zie je?", "Het zout lost op, het zand zakt naar de bodem.", 2)]),
    ]))

H["techniek"] = ("techniek-rondom-ons-ready", "wetenschap-en-techniek", dict(
    vak="Wetenschap en techniek", niveau=READY, titel="Techniek rondom ons",
    onder="Wiel, hefboom en katrol, een lampje laten branden en veilig omgaan met elektriciteit.",
    secties=[
        dict(kop="Machines die werk lichter maken", blokken=[("fig", tabel(["Machine", "Hoe helpt het?", "Voorbeeld"], [["wiel", "rollen gaat makkelijker dan schuiven", "kruiwagen, fiets"],
            ["hefboom", "met een lange arm til je zwaar met weinig kracht", "wip, schaar, flessenopener"], ["katrol", "je trekt naar beneden, de last gaat omhoog", "vlaggenmast, lift"],
            ["helling", "langer pad, minder kracht", "oprit voor een rolstoel"]], "100%"))]),
        dict(kop="Zelf iets maken", blokken=[("kader", "1. Bedenk en teken je plan.<br>2. Kies materialen en werktuigen.<br>3. Maak het.<br>4. Test het.<br>5. Verbeter wat niet goed werkt.")]),
        dict(kop="Een lampje laten branden", blokken=[("fig", stroomkring(), "een gesloten stroomkring: het lampje brandt"),
            ("p", "De stroom moet <strong>rondgaan</strong>: van de batterij, door de draad, door het lampje en terug. Een <strong>schakelaar</strong> opent of sluit de kring."),
            ("p", "<strong>Geleiders</strong> (metaal) laten stroom door. <strong>Isolatoren</strong> (plastic, hout, rubber) niet.")]),
        dict(kop="Veilig met elektriciteit", blokken=[("kader", "⚠️ Nooit met natte handen aan een stopcontact.<br>⚠️ Kapotte draad? Niet aankomen, zeg het aan een volwassene.<br>✅ Proeven doe je met kleine batterijen."),
            ("p", "Zonnepanelen en windmolens maken stroom uit zon en wind. Die raken nooit op.")]),
    ],
    onthoud=["Wiel, hefboom, katrol en helling maken werk lichter.", "Bedenken, maken, testen, verbeteren.", "Een lampje brandt in een gesloten kring.", "Metaal geleidt, plastic niet.", "Nooit met natte handen aan stroom."]),
    dict(vak="Wetenschap en techniek", niveau=READY, titel="Techniek rondom ons", onder=ON, hoe=HOE, reeksen=[
        dict(kop="Welke machine?", oefeningen=[("rij", [("een wip", "hefboom"), ("een kruiwagen", "wiel"), ("een vlaggenmast", "katrol"), ("een oprit voor een rolstoel", "helling")], "Wiel, hefboom, katrol of helling?", B)]),
        dict(kop="Brandt het lampje?", oefeningen=[("fig", [(stroomkring(), "ja, de kring is gesloten"), (stroomkring(True), "nee, de kring is open")], "Schrijf ja of nee en zeg waarom."),
            ("rij", [("een metalen lepel", "geleider"), ("een plastic lat", "isolator"), ("een aluminium folie", "geleider"), ("een houten potlood", "isolator")], "Geleider of isolator?", B)]),
        dict(kop="Veilig of gevaarlijk?", opdracht="Telkens is één keuze veilig en één gevaarlijk. Streep de gevaarlijke keuze door.", oefeningen=[
            ("invulwoord", [("droge handen &nbsp; / &nbsp; natte handen", "droge handen"), ("een batterij van 1,5 volt &nbsp; / &nbsp; het stopcontact", "een batterij van 1,5 volt"),
                            ("kapotte draad laten liggen &nbsp; / &nbsp; kapotte draad aanraken", "kapotte draad laten liggen")], "")]),
        dict(kop="Ontwerp zelf", oefeningen=[("teken", "Teken een wagentje dat kan rijden. Welke materialen gebruik je? Schrijf ze erbij.", "eigen ontwerp met wielen en assen", 55),
            ("open", "Hoe test je of je wagentje goed rijdt?", "bv. van een helling laten rollen en meten hoe ver het komt", 2)]),
    ]))

H["natuur"] = ("natuur-en-milieu-ready", "wetenschap-en-techniek", dict(
    vak="Wetenschap en techniek", niveau=READY, titel="Natuur en milieu",
    onder="Seizoenen, dag en nacht, het weer meten, de waterkringloop, afval sorteren en zorgen voor de natuur.",
    secties=[
        dict(kop="Seizoenen, dag en nacht", blokken=[("fig", tabel(["Lente", "Zomer", "Herfst", "Winter"], [["bloesems, jonge dieren", "lange, warme dagen", "bladeren vallen", "kort, koud, soms sneeuw"]], "100%")),
            ("p", "De aarde draait rond zichzelf: dag en nacht. De aarde draait in een jaar rond de zon. De maan draait rond de aarde. De zon is een <strong>ster</strong>.")]),
        dict(kop="Het weer meten", blokken=[("fig", tabel(["Toestel", "Meet"], [["thermometer", "temperatuur"], ["regenmeter", "hoeveel regen"], ["windvaan", "waar de wind vandaan komt"]], "70%")),
            ("kader", "De waterkringloop: zee → verdampen → wolk → regen → rivier → zee")]),
        dict(kop="Afval sorteren", blokken=[("fig", tabel(["Soort", "Wat?"], [["pmd (blauwe zak)", "plastic flessen, metalen blikjes, drankkartons"], ["gft", "groente-, fruit- en tuinafval"],
            ["papier en karton", "kranten, dozen"], ["glas", "flessen en bokalen"], ["restafval", "wat nergens anders bij hoort"], ["inzamelpunt", "batterijen, lampen"]], "100%")),
            ("weetje", "Minder afval: herstellen, hergebruiken, doorgeven of naar de kringwinkel brengen.")]),
        dict(kop="Zorgen voor de natuur", blokken=[("p", "Laat geen zwerfvuil achter, bespaar water en energie, en laat dieren en planten in een natuurgebied met rust. Bijen zijn belangrijk: zonder hen zijn er minder vruchten.")]),
    ],
    onthoud=["Lente, zomer, herfst, winter.", "Thermometer, regenmeter, windvaan.", "Verdampen, wolk, regen: de waterkringloop.", "Sorteren: pmd, gft, papier, glas, restafval."]),
    dict(vak="Wetenschap en techniek", niveau=READY, titel="Natuur en milieu", onder=ON, hoe=HOE, reeksen=[
        dict(kop="Seizoenen", oefeningen=[("rij", [("de bladeren vallen", "herfst"), ("de bomen bloeien", "lente"), ("het sneeuwt", "winter"), ("lange, warme dagen", "zomer")], "Welk seizoen?", B)]),
        dict(kop="Het weer", opdracht="Hou een week lang het weer bij.", oefeningen=[
            ("tabel", ["Dag", "Temperatuur", "Regen? (ja/nee)", "Zon, wolken of regen"], [["maandag", None, None, None], ["dinsdag", None, None, None], ["woensdag", None, None, None], ["donderdag", None, None, None], ["vrijdag", None, None, None]], "eigen metingen", "100px")]),
        dict(kop="Waterkringloop", oefeningen=[("open", "Zet in de juiste volgorde: regen – zee – wolk – verdampen – rivier.", "zee – verdampen – wolk – regen – rivier", 1)]),
        dict(kop="Afval sorteren", oefeningen=[("rij", [("een bananenschil", "gft"), ("een leeg blikje", "pmd"), ("een glazen bokaal", "glas"), ("een oude krant", "papier"), ("een lege batterij", "inzamelpunt"), ("een drankkarton", "pmd")], "Waar hoort het?", B)]),
        dict(kop="Zorg voor de natuur", oefeningen=[("open", "Schrijf drie dingen die jij kan doen om minder afval te maken.", "bv. boterhamdoos, drinkbus, spullen herstellen of doorgeven", 3)]),
    ]))

# ================================================================ aardrijkskunde
H["kaarten"] = ("kaarten-lezen-ready", "aardrijkskunde", dict(
    vak="Aardrijkskunde", niveau=READY, titel="Kaarten lezen",
    onder="Plattegrond en legende, windrichtingen, kompas en een eenvoudige schaal.",
    secties=[
        dict(kop="De plattegrond", blokken=[("p", "Een <strong>plattegrond</strong> is een kaart van bovenaf, zoals een vogel het ziet. Alles is <strong>verkleind</strong>."),
            ("fig", tabel(["Kleur of teken", "Betekent"], [["blauw", "water"], ["groen", "bos of park"], ["dikke gekleurde lijn", "grote weg"], ["kruisje", "kerk"]], "70%"), "een legende"),
            ("p", "De <strong>legende</strong> legt uit wat de kleuren en tekentjes betekenen. Een <strong>atlas</strong> is een boek vol kaarten.")]),
        dict(kop="Windrichtingen", blokken=[("fig", kompasroos()),
            ("p", "Noord boven, oost rechts, zuid onder, west links. De zon komt op in het <strong>oosten</strong> en gaat onder in het <strong>westen</strong>. Een <strong>kompas</strong> wijst naar het noorden."),
            ("weetje", "Onthoud de klok rond: Nooit Oost Zonder Wortelen.")]),
        dict(kop="Schaal", blokken=[("p", "Staat er 1 cm = 1 km, dan is elke centimeter op de kaart in het echt 1 kilometer.")]),
    ],
    onthoud=["Plattegrond: van bovenaf, verkleind.", "Legende: wat de tekens betekenen.", "N boven, O rechts, Z onder, W links.", "Zon op in het oosten, onder in het westen."]),
    dict(vak="Aardrijkskunde", niveau=READY, titel="Kaarten lezen", onder=ON, hoe=HOE, reeksen=[
        dict(kop="Windrichtingen", oefeningen=[("fig", [(kompasroos(True), "N boven, O rechts, Z onder, W links")], "Schrijf O, Z en W bij de juiste punt."),
            ("rij", [("De zon komt op in het ...", "oosten"), ("De zon gaat onder in het ...", "westen"), ("Nederland ligt ten ... van België.", "noorden"), ("Frankrijk ligt ten ... van België.", "zuiden")], "", B)]),
        dict(kop="Plattegrond tekenen", oefeningen=[("teken", "Teken een plattegrond van je kamer. Maak een legende met minstens drie tekens (bv. bed, kast, deur).", "eigen plattegrond met legende", 70)]),
        dict(kop="Schaal", oefeningen=[("rij", [("2 cm op de kaart", "2 km"), ("5 cm op de kaart", "5 km"), ("10 cm op de kaart", "10 km")], "1 cm = 1 km. Hoeveel is het in het echt?", B)]),
        dict(kop="Waar of niet waar?", oefeningen=[("waar", "Op een plattegrond kijk je van bovenaf.", True), ("waar", "Een kaart is even groot als de echte plaats.", False), ("waar", "Het westen staat rechts als het noorden boven is.", False)]),
    ]))

H["belgie"] = ("belgie-ready", "aardrijkskunde", dict(
    vak="Aardrijkskunde", niveau=READY, titel="België",
    onder="Gewesten en provincies met hun hoofdsteden, talen, buurlanden, rivieren, de kust en de Ardennen.",
    secties=[
        dict(kop="Gewesten en provincies", blokken=[("p", "België heeft drie gewesten: <strong>Vlaanderen</strong>, <strong>Wallonië</strong> en <strong>Brussel</strong>, en tien provincies. Brussel is de hoofdstad."),
            ("fig", tabel(["Provincie", "Hoofdstad", "Provincie", "Hoofdstad"], [["West-Vlaanderen", "Brugge", "Henegouwen", "Bergen"], ["Oost-Vlaanderen", "Gent", "Namen", "Namen"],
                ["Antwerpen", "Antwerpen", "Luik", "Luik"], ["Vlaams-Brabant", "Leuven", "Luxemburg", "Aarlen"], ["Limburg", "Hasselt", "Waals-Brabant", "Waver"]], "100%"), "links Vlaanderen, rechts Wallonië"),
            ("p", "Talen: <strong>Nederlands</strong> (Vlaanderen), <strong>Frans</strong> (Wallonië), <strong>Duits</strong> (Oostkantons). Brussel is tweetalig.")]),
        dict(kop="Buurlanden en landschappen", blokken=[("p", "Buurlanden: <strong>Nederland</strong> (noord), <strong>Duitsland</strong> (oost), <strong>Luxemburg</strong> (zuidoost), <strong>Frankrijk</strong> (zuid). In het westen ligt de <strong>Noordzee</strong>."),
            ("fig", tabel(["Streek", "Hoe ziet het eruit?"], [["kust", "strand en duinen, vlak"], ["polders", "laag, vlak land met dijken"], ["Kempen", "heide en bossen"], ["Ardennen", "heuvels, bossen, diepe dalen; het hoogste punt"]], "100%")),
            ("p", "Rivieren: de <strong>Schelde</strong> (Gent, Antwerpen) en de <strong>Maas</strong> (Namen, Luik). Ze stromen naar de Noordzee.")]),
    ],
    onthoud=["3 gewesten, 10 provincies, hoofdstad Brussel.", "Nederlands, Frans, Duits.", "Buurlanden: Nederland, Duitsland, Luxemburg, Frankrijk.", "Schelde en Maas. Kust in het westen, Ardennen in het zuiden."]),
    dict(vak="Aardrijkskunde", niveau=READY, titel="België", onder=ON, hoe=HOE, reeksen=[
        dict(kop="Provincies en hoofdsteden", oefeningen=[("tabel", ["Provincie", "Hoofdstad"], [["Limburg", None], ["West-Vlaanderen", None], ["Oost-Vlaanderen", None], ["Vlaams-Brabant", None], ["Antwerpen", None]], "Hasselt · Brugge · Gent · Leuven · Antwerpen", B),
            ("rij", [("Luik", "Wallonië"), ("Limburg", "Vlaanderen"), ("Namen", "Wallonië")], "Vlaanderen of Wallonië?", B)]),
        dict(kop="Buurlanden", oefeningen=[("rij", [("noord", "Nederland"), ("oost", "Duitsland"), ("zuid", "Frankrijk"), ("zuidoost", "Luxemburg")], "Welk buurland ligt in deze richting?", B)]),
        dict(kop="Landschappen", oefeningen=[("rij", [("strand en duinen", "kust"), ("heuvels en diepe dalen", "Ardennen"), ("heide en bossen", "Kempen"), ("laag land met dijken", "polders")], "Welke streek?", B)]),
        dict(kop="Mijn gemeente", oefeningen=[("open", "In welke gemeente en provincie woon jij? Welke rivier of beek stroomt in de buurt?", "eigen antwoord", 2)]),
    ]))

H["wereld"] = ("de-wereld-ready", "aardrijkskunde", dict(
    vak="Aardrijkskunde", niveau=READY, titel="De wereld",
    onder="Werelddelen en oceanen, evenaar en polen, warm en koud, nat en droog.",
    secties=[
        dict(kop="Werelddelen en oceanen", blokken=[("fig", tabel(["Werelddeel", "Bijvoorbeeld"], [["Europa", "België, Frankrijk"], ["Azië (grootste)", "China, India"], ["Afrika", "Egypte, Kenia"],
            ["Amerika", "Canada, Brazilië"], ["Oceanië", "Australië"], ["Antarctica", "ijs, pinguïns"]], "80%")),
            ("p", "De grootste oceaan is de <strong>Stille Oceaan</strong>. Tussen Europa en Amerika ligt de <strong>Atlantische Oceaan</strong>. De aarde is voor het grootste deel water.")]),
        dict(kop="Evenaar en polen", blokken=[("p", "De <strong>evenaar</strong> is een denkbeeldige lijn rond het midden van de aarde. Daar is het altijd warm. Aan de <strong>noordpool</strong> en <strong>zuidpool</strong> is het altijd koud.")]),
        dict(kop="Klimaat en leven", blokken=[("fig", tabel(["Gebied", "Weer", "Dieren"], [["woestijn", "heet en droog", "kameel"], ["regenwoud", "warm en nat", "papegaai, aap"], ["poolgebied", "ijskoud", "ijsbeer, pinguïn"], ["België", "gematigd, 4 seizoenen", "vos, egel"]], "100%")),
            ("p", "Hoe hoger in de bergen, hoe kouder. De Himalaya is het hoogste gebergte. De Nijl is de langste rivier van Afrika, de Amazone stroomt door het grootste regenwoud.")]),
    ],
    onthoud=["6 werelddelen, Azië is het grootst.", "Stille Oceaan is de grootste oceaan.", "Evenaar warm, polen koud.", "Woestijn droog, regenwoud nat."]),
    dict(vak="Aardrijkskunde", niveau=READY, titel="De wereld", onder=ON, hoe=HOE, reeksen=[
        dict(kop="Werelddelen", oefeningen=[("rij", [("België", "Europa"), ("China", "Azië"), ("Egypte", "Afrika"), ("Brazilië", "Amerika"), ("Australië", "Oceanië")], "In welk werelddeel ligt het?", B)]),
        dict(kop="Warm of koud?", oefeningen=[("rij", [("aan de evenaar", "warm"), ("op de noordpool", "koud"), ("in de Sahara", "warm"), ("hoog op een berg", "koud")], "", B)]),
        dict(kop="Wie woont waar?", oefeningen=[("rij", [("ijsbeer", "poolgebied"), ("kameel", "woestijn"), ("papegaai", "regenwoud"), ("egel", "België")], "", B)]),
        dict(kop="Zoek in de atlas", oefeningen=[("open", "Zoek in een atlas of op een wereldbol: welke oceaan moet je over om van België naar Amerika te vliegen?", "de Atlantische Oceaan", 1),
            ("open", "Kies een land ver weg. Schrijf in welk werelddeel het ligt en hoe het weer daar is.", "eigen antwoord", 2)]),
    ]))

# ================================================================ geschiedenis
H["tijd"] = ("tijd-en-vroeger-ready", "geschiedenis", dict(
    vak="Geschiedenis", niveau=READY, titel="Tijd en vroeger",
    onder="Jaren en eeuwen, de tijdsbalk, bronnen, vroeger en nu, en je familie.",
    secties=[
        dict(kop="Tijd meten", blokken=[("fig", tabel(["", "Duurt"], [["decennium", "10 jaar"], ["eeuw", "100 jaar"], ["millennium", "1 000 jaar"]], "50%")),
            ("p", "We leven nu in de <strong>21ste eeuw</strong> (2001 tot 2100).")]),
        dict(kop="De tijdsbalk", blokken=[("fig", tijdsbalk([(60, "2 000 jaar geleden", "Romeinen"), (230, "1 000 jaar geleden", "ridders"), (420, "1969", "mens op de maan"), (560, "nu", "jij")])),
            ("p", "Links staat wat het langst geleden is, rechts wat later kwam.")]),
        dict(kop="Bronnen over vroeger", blokken=[("p", "Een <strong>bron</strong> vertelt iets over vroeger: een oude foto, een brief, een munt, een verhaal van oma. In een <strong>museum</strong> zie je oude voorwerpen.")]),
        dict(kop="Vroeger en nu", blokken=[("fig", tabel(["Vroeger", "Nu"], [["griffel en lei", "schrift, laptop"], ["met de hand wassen", "wasmachine"], ["paard en kar, stoomtrein", "auto, elektrische trein"], ["kaarsen", "elektrisch licht"]], "80%")),
            ("p", "In een <strong>stamboom</strong> zie je je familie: ouders, grootouders, overgrootouders. Elke laag is een <strong>generatie</strong>.")]),
    ],
    onthoud=["Decennium 10, eeuw 100 jaar.", "Tijdsbalk: van links (vroeger) naar rechts (later).", "Bronnen vertellen over vroeger.", "Stamboom: generaties in je familie."]),
    dict(vak="Geschiedenis", niveau=READY, titel="Tijd en vroeger", onder=ON, hoe=HOE, reeksen=[
        dict(kop="Rekenen met tijd", oefeningen=[("rij", [("Hoeveel jaar is een eeuw?", "100"), ("Hoeveel jaar is een decennium?", "10"), ("Hoe oud word je in 2026 als je in 2017 geboren bent?", "9")], "", "80px")]),
        dict(kop="Mijn tijdsbalk", oefeningen=[("fig", [(tijdsbalk([(80, "geboren", ""), (250, "", ""), (420, "", ""), (560, "nu", "")], True), "eigen tijdsbalk")],
            "Schrijf het jaar waarin je geboren bent, en drie belangrijke dingen uit je leven (bv. eerste schooldag, broer of zus geboren)."),
            ("open", "Zet in volgorde: mens op de maan – Romeinen – jouw geboorte – ridders.", "Romeinen – ridders – mens op de maan – jouw geboorte", 1)]),
        dict(kop="Vroeger of nu?", opdracht="Telkens is één ding van vroeger en één van nu. Streep het ding van nu door.", oefeningen=[
            ("invulwoord", [("griffel en lei &nbsp; / &nbsp; tablet", "griffel en lei"), ("gsm &nbsp; / &nbsp; ganzenveer", "ganzenveer"), ("stoomtrein &nbsp; / &nbsp; elektrische auto", "stoomtrein")], "")]),
        dict(kop="Mijn stamboom", oefeningen=[("teken", "Teken je stamboom: jij onderaan, daarboven je ouders, daarboven je grootouders. Schrijf de namen erbij.", "eigen stamboom", 70)]),
        dict(kop="Interview", oefeningen=[("open", "Vraag aan een grootouder of een oudere buur: hoe ging jij vroeger naar school? Waarmee speelde je? Schrijf het antwoord op.", "eigen interview", 4)]),
    ]))

H["vroeger"] = ("hoe-leefden-mensen-vroeger-ready", "geschiedenis", dict(
    vak="Geschiedenis", niveau=READY, titel="Hoe leefden mensen vroeger?",
    onder="De eerste mensen, de Romeinen in onze streken en het leven in de middeleeuwen.",
    secties=[
        dict(kop="De eerste mensen", blokken=[("p", "In de <strong>prehistorie</strong>, de tijd vóór het schrift, leefden mensen als <strong>jagers en verzamelaars</strong>. Ze maakten werktuigen van steen, gebruikten vuur en maakten tekeningen in grotten."),
            ("p", "Later werden mensen <strong>boeren</strong>: ze bleven op één plaats wonen, zaaiden graan en hielden dieren.")]),
        dict(kop="De Romeinen", blokken=[("p", "De Romeinen kwamen uit <strong>Rome</strong>. Ze spraken <strong>Latijn</strong>, legden rechte wegen aan en bouwden met steen. <strong>Tongeren</strong> was een Romeinse stad en geldt als de oudste stad van België."),
            ("p", "<strong>Ambiorix</strong>, koning van de Eburonen, vocht tegen Julius Caesar. Zijn standbeeld staat in Tongeren."),
            ("fig", tabel(["I", "V", "X", "L", "C"], [["1", "5", "10", "50", "100"]], "60%"), "Romeinse cijfers")]),
        dict(kop="De middeleeuwen", blokken=[("p", "Ridders vochten te paard, in een harnas. Een <strong>kasteel</strong> had dikke muren, een gracht en een ophaalbrug. Het <strong>Gravensteen</strong> in Gent is zo'n burcht."),
            ("p", "De meeste mensen waren <strong>boeren</strong>. In de steden werkten ambachtslui in <strong>gilden</strong>. Monniken schreven boeken met de hand over. Het <strong>belfort</strong> was een uitkijktoren.")]),
    ],
    onthoud=["Prehistorie: jagers, verzamelaars, eerste boeren.", "Romeinen: Latijn, wegen, Tongeren.", "Middeleeuwen: ridders, kastelen, gilden, belforten.", "Volgorde: prehistorie, Romeinen, middeleeuwen."]),
    dict(vak="Geschiedenis", niveau=READY, titel="Hoe leefden mensen vroeger?", onder=ON, hoe=HOE, reeksen=[
        dict(kop="Welke tijd?", oefeningen=[("rij", [("grottekeningen", "prehistorie"), ("rechte wegen en Latijn", "Romeinen"), ("ridders en kastelen", "middeleeuwen"), ("stenen werktuigen", "prehistorie")], "Prehistorie, Romeinen of middeleeuwen?", B)]),
        dict(kop="Romeinse cijfers", oefeningen=[("rij", [("III", "3"), ("VI", "6"), ("IX", "9"), ("XII", "12"), ("XX", "20")], "Schrijf in gewone cijfers.", "70px")]),
        dict(kop="Het kasteel", oefeningen=[("teken", "Teken een middeleeuws kasteel met een gracht, een ophaalbrug en een toren. Schrijf de namen erbij.", "eigen tekening", 60)]),
        dict(kop="Waar of niet waar?", oefeningen=[("waar", "In de prehistorie konden mensen schrijven.", False), ("waar", "Tongeren was een Romeinse stad.", True),
            ("waar", "De meeste mensen in de middeleeuwen waren ridders.", False)]),
        dict(kop="Vroeger en nu", oefeningen=[("open", "Wat at een boer in de middeleeuwen? Wat eet jij vandaag? Schrijf een verschil.", "boer: brood, pap, groenten; nu: veel meer keuze", 2)]),
    ]))

H["samenleven"] = ("samenleven-ready", "geschiedenis", dict(
    vak="Geschiedenis", niveau=READY, titel="Samenleven",
    onder="Regels en afspraken, kinderrechten, de gemeente en België, feesten en gewoonten.",
    secties=[
        dict(kop="Regels en kinderrechten", blokken=[("p", "Regels en afspraken zorgen dat iedereen veilig en fijn kan samenleven. Een <strong>wet</strong> geldt voor iedereen in het land."),
            ("fig", tabel(["Elk kind heeft recht op"], [["onderwijs"], ["spelen en rusten"], ["bescherming, ook tegen pesten"], ["een eigen mening en gehoord worden"], ["gezondheidszorg"]], "60%")),
            ("p", "Op <strong>20 november</strong> is het Kinderrechtendag.")]),
        dict(kop="Wie bestuurt?", blokken=[("fig", tabel(["", "Wie?", "Waar?"], [["gemeente", "burgemeester en schepenen", "gemeentehuis"], ["België", "koning Filip, parlement en regering", "Brussel"]], "100%")),
            ("p", "Volwassenen kiezen bij <strong>verkiezingen</strong> wie bestuurt. Het noodnummer is <strong>112</strong>.")]),
        dict(kop="Feesten en gewoonten", blokken=[("fig", tabel(["Datum", "Feest"], [["6 december", "Sinterklaas"], ["25 december", "Kerstmis"], ["21 juli", "nationale feestdag"], ["11 november", "einde Eerste Wereldoorlog"], ["na de ramadan", "Suikerfeest"]], "70%")),
            ("p", "Niet iedereen viert dezelfde feesten. Iedereen is anders, en dat is oké.")]),
    ],
    onthoud=["Afspraken maken samenleven fijn.", "Kinderen hebben rechten.", "Burgemeester in de gemeente, koning en parlement in België.", "Feesten verschillen van gezin tot gezin."]),
    dict(vak="Geschiedenis", niveau=READY, titel="Samenleven", onder=ON, hoe=HOE, reeksen=[
        dict(kop="Klasafspraken", oefeningen=[("open", "Schrijf drie afspraken die jullie klas fijn maken.", "bv. we luisteren naar elkaar, we helpen elkaar, we ruimen samen op", 3)]),
        dict(kop="Kinderrechten", opdracht="Telkens is één zin een kinderrecht en één niet. Streep de foute zin door.", oefeningen=[
            ("invulwoord", [("recht om te spelen &nbsp; / &nbsp; recht om nooit te slapen", "recht om te spelen"), ("recht op onderwijs &nbsp; / &nbsp; recht om alles te kopen", "recht op onderwijs"),
                            ("recht op bescherming &nbsp; / &nbsp; recht om te pesten", "recht op bescherming")], "")]),
        dict(kop="Wie doet wat?", oefeningen=[("rij", [("leidt de gemeente", "burgemeester"), ("maakt de wetten", "parlement"), ("zorgt voor veiligheid", "politie"), ("blust branden", "brandweer")], "", B),
            ("rij", [("noodnummer", "112"), ("nationale feestdag", "21 juli"), ("Kinderrechtendag", "20 november")], "", B)]),
        dict(kop="Feesten", oefeningen=[("open", "Welk feest vieren jullie thuis graag? Wat doen jullie dan?", "eigen antwoord", 3)]),
    ]))


if __name__ == "__main__":
    for k in sys.argv[1:] or list(H):
        naam, vakmap, leer, oefen = H[k]
        met_prenten(leer, oefen, {"wetenschap-en-techniek": "wt_", "aardrijkskunde": "ak_", "geschiedenis": "gs_"}[vakmap] + k)
        maak(naam, vakmap, leer, oefen, grote_figuren=True)

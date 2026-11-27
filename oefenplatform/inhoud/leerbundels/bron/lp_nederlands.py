# -*- coding: utf-8 -*-
"""Leer- en oefenbundels bij de Launchpad-hoofdstukken Nederlands (1ste en 2de leerjaar).
De vragen op het scherm staan in ../../launchpad/bron/nederlands_*.py.

    python3 lp_nederlands.py            # alles
    python3 lp_nederlands.py klanken    # één hoofdstuk
"""
import sys
from lp_gemeen import maak, tabel, LP, HOE, ON

V = "Nederlands"; B = "110px"
H = {}


def L(titel, onder, secties, onthoud):
    return dict(vak=V, niveau=LP, titel=titel, onder=onder, secties=secties, onthoud=onthoud)


def O(titel, reeksen):
    return dict(vak=V, niveau=LP, titel=titel, onder=ON, hoe=HOE, reeksen=reeksen)


H["klanken"] = ("letters-en-klanken-launchpad", "nederlands-klanken", L("Letters en klanken", "De eerste en de laatste klank horen, woorden hakken en plakken, en rijmen.", [
    dict(kop="Klanken horen", blokken=[("p", "Zeg het woord heel traag: <strong>m – aa – n</strong>. De eerste klank is <strong>m</strong>, de laatste is <strong>n</strong>.")]),
    dict(kop="Hakken en plakken", blokken=[("fig", tabel(["hakken", "plakken"], [["r – oo – s", "roos"], ["k – i – p", "kip"], ["m – ui – s", "muis"]], "60%")),
        ("weetje", "Soms maken twee letters samen één klank: aa, oo, ee, uu, oe, ui, eu, ei, ij, ou, au.")]),
    dict(kop="Rijmen", blokken=[("p", "Woorden die rijmen, eindigen op dezelfde klank: <strong>kat – mat – rat</strong>, <strong>pop – top – kop</strong>.")]),
], ["Zeg het woord traag.", "Hakken: r – oo – s. Plakken: roos.", "Twee letters kunnen één klank zijn."]),
    O("Letters en klanken", [
        dict(kop="Eerste klank", oefeningen=[("rij", [("maan", "m"), ("sok", "s"), ("vis", "v"), ("raam", "r"), ("hek", "h"), ("bal", "b")], "Schrijf de eerste klank.", "60px")]),
        dict(kop="Laatste klank", oefeningen=[("rij", [("pen", "n"), ("tak", "k"), ("bus", "s"), ("boom", "m"), ("kip", "p"), ("jas", "s")], "Schrijf de laatste klank.", "60px")]),
        dict(kop="Plakken", oefeningen=[("rij", [("b – oo – m", "boom"), ("k – a – t", "kat"), ("m – ui – s", "muis"), ("v – oe – t", "voet")], "Schrijf het woord.", B)]),
        dict(kop="Hoeveel klanken?", oefeningen=[("rij", [("pen", "3"), ("ei", "1"), ("raam", "3"), ("touw", "2")], "", "60px")]),
        dict(kop="Rijmen", oefeningen=[("rij", [("kat", "bv. mat, rat"), ("pop", "bv. top, kop"), ("huis", "bv. muis, kruis"), ("boom", "bv. room, stoom")], "Schrijf een woord dat rijmt.", B)]),
    ]))

H["lezen"] = ("korte-woorden-lezen-launchpad", "nederlands-lezen", L("Korte woorden lezen", "Korte woorden en kleine zinnen lezen, en weten wat ze betekenen.", [
    dict(kop="Woorden lezen", blokken=[("p", "Lees klank per klank, en plak dan: <strong>b – oe – k</strong> → <strong>boek</strong>. Hoe vaker je een woord leest, hoe sneller het gaat.")]),
    dict(kop="Wat betekent het?", blokken=[("fig", tabel(["dier", "eten", "ding"], [["kip, koe, vis", "peer, brood, kaas", "pen, bal, stoel"]], "80%"))]),
    dict(kop="Zinnen lezen", blokken=[("p", "Een zin begint met een hoofdletter en stopt bij de punt. Lees de hele zin en vraag je af: <strong>wie</strong>? <strong>wat</strong>? <strong>waar</strong>?"),
        ("kader", "De hond rent in de tuin.<br>Wie? de hond · Wat doet hij? rennen · Waar? in de tuin")]),
], ["Klank per klank, dan plakken.", "Na het lezen: wie, wat, waar?"]),
    O("Korte woorden lezen", [
        dict(kop="Welk woord hoort er niet bij?", oefeningen=[("kies", "", ["appel", "peer", "fiets", "banaan"], 2), ("kies", "", ["koe", "boek", "kip", "hond"], 1)]),
        dict(kop="Lees en kies", oefeningen=[("kies", "Wat kan vliegen?", ["een uil", "een ui", "een uur"], 0), ("kies", "Waar woon je in?", ["een muis", "een huis", "een buis"], 1)]),
        dict(kop="Lees de zin", opdracht="Mia eet een rode appel in de tuin.", oefeningen=[("kort", "Wie eet?", "Mia", B), ("kort", "Wat eet ze?", "een appel", B), ("kort", "Waar?", "in de tuin", B)]),
        dict(kop="Waar of niet waar?", oefeningen=[("waar", "Een vis woont in het water.", True), ("waar", "Een boom kan lopen.", False), ("waar", "Met een pen kan je schrijven.", True)]),
        dict(kop="Teken", oefeningen=[("teken", "Lees en teken: een kat op een stoel.", "eigen tekening", 50)]),
    ]))

H["spelling"] = ("woorden-goed-schrijven-launchpad", "nederlands-spelling", L("Woorden goed schrijven", "Schrijven wat je hoort, korte en lange klanken, ei of ij, au of ou.", [
    dict(kop="Schrijf wat je hoort", blokken=[("p", "Hak het woord in klanken en schrijf elke klank: <strong>k – i – p</strong> → kip.")]),
    dict(kop="Kort of lang", blokken=[("fig", tabel(["kort", "lang"], [["man", "maan"], ["bom", "boom"], ["pen", "peen"]], "40%")),
        ("p", "Een lange klank in het midden schrijf je met twee letters: m<strong>aa</strong>n, b<strong>oo</strong>m.")]),
    dict(kop="Ei of ij, au of ou", blokken=[("fig", tabel(["ei", "ij", "au", "ou"], [["ei, trein, klein", "ijs, rijst, fijn", "auto, pauw, blauw", "touw, goud, koud"]], "100%")),
        ("weetje", "Bij ei/ij en au/ou hoor je geen verschil. Je moet het woord leren kennen.")]),
], ["Hak en schrijf elke klank.", "Lange klank: twee letters.", "ei/ij en au/ou: leer de woorden."]),
    O("Woorden goed schrijven", [
        dict(kop="Vul aan", opdracht="Schrijf de klank die ontbreekt.", oefeningen=[("invulwoord", [("b__s", "u"), ("m__n", "aa"), ("v__t", "oe"), ("m__s", "ui"), ("r__s", "oo"), ("n__s", "eu")], "")]),
        dict(kop="Ei of ij?", oefeningen=[("invulwoord", [("tr__n", "ei"), ("__s", "ij"), ("r__st", "ij"), ("kl__n", "ei")], "")]),
        dict(kop="Au of ou?", oefeningen=[("invulwoord", [("t__w", "ou"), ("__to", "au"), ("p__w", "au"), ("k__d", "ou")], "")]),
        dict(kop="Kort of lang?", opdracht="Omcirkel het goede woord.", oefeningen=[("invulwoord", [("Ik zie de (man / maan) aan de hemel.", "maan"), ("De (bom / boom) heeft groene blaadjes.", "boom")], "")]),
        dict(kop="Schrijf het woord", oefeningen=[("rij", [("k – a – t", "kat"), ("p – e – n", "pen"), ("h – oe – d", "hoed"), ("t – r – ei – n", "trein")], "", B)]),
    ]))

H["zinnen"] = ("zinnen-maken-launchpad", "nederlands-zinnen", L("Zinnen maken", "Hoofdletter en punt, vraagteken, en woorden in de goede volgorde.", [
    dict(kop="Een zin", blokken=[("kader", "<strong>D</strong>e kat slaapt<strong>.</strong><br>hoofdletter vooraan · punt achteraan"),
        ("p", "Een vraag krijgt een <strong>vraagteken</strong>: Waar woon jij?"), ("p", "Namen krijgen altijd een hoofdletter: Mia, Tom, Gent.")]),
    dict(kop="Goede volgorde", blokken=[("p", "Eerst <strong>wie</strong>, dan <strong>wat hij doet</strong>: Tom speelt buiten. Bij een vraag zet je het doe-woord vooraan: Speelt Tom buiten?")]),
], ["Hoofdletter vooraan, punt achteraan.", "Vraag: vraagteken.", "Namen met een hoofdletter."]),
    O("Zinnen maken", [
        dict(kop="Punt of vraagteken?", oefeningen=[("invulwoord", [("Ik eet een appel__", "."), ("Waar is mijn jas__", "?"), ("Mag ik mee__", "?"), ("De zon schijnt__", ".")], "")]),
        dict(kop="Hoofdletter", opdracht="Schrijf de zin goed over.", oefeningen=[("open", "de hond blaft.", "De hond blaft.", 1), ("open", "mijn vriend heet sam.", "Mijn vriend heet Sam.", 1)]),
        dict(kop="Goede volgorde", oefeningen=[("open", "eet / Ik / brood", "Ik eet brood.", 1), ("open", "speelt / buiten / Lien", "Lien speelt buiten.", 1)]),
        dict(kop="Maak een vraag", oefeningen=[("open", "Jij komt mee.", "Kom jij mee?", 1)]),
        dict(kop="Schrijf zelf", oefeningen=[("open", "Schrijf een zin over je huisdier of je lievelingsdier.", "eigen zin met hoofdletter en punt", 2)]),
    ]))

H["verhaal"] = ("verhaaltjes-begrijpen-launchpad", "nederlands-verhaal", L("Verhaaltjes begrijpen", "Een kort verhaal lezen of beluisteren, en zeggen wat eerst, daarna en op het einde gebeurt.", [
    dict(kop="Goed luisteren", blokken=[("p", "Kijk naar wie vertelt. Wees stil. Denk mee: wie? wat? waar?")]),
    dict(kop="Begin, midden, einde", blokken=[("fig", tabel(["eerst", "daarna", "op het einde"], [["Het sneeuwt.", "Ben maakt een sneeuwman.", "De sneeuwman smelt."]], "100%"))]),
    dict(kop="Gevoelens", blokken=[("fig", tabel(["blij 😊", "verdrietig 😢", "boos 😠", "bang 😨"], [["een cadeau", "je knuffel kwijt", "iemand pakt je speelgoed af", "onweer"]], "100%"))]),
], ["Eerst, daarna, op het einde.", "Wie, wat, waar?", "Hoe voelt iemand zich?"]),
    O("Verhaaltjes begrijpen", [
        dict(kop="Lees het verhaal", opdracht="Sara gaat met haar hond Max naar het park. Max rent achter een bal. Daarna drinken ze water.",
             oefeningen=[("kort", "Hoe heet de hond?", "Max", B), ("kort", "Waar gaan ze naartoe?", "naar het park", "140px"), ("kort", "Wat doen ze op het einde?", "water drinken", "140px")]),
        dict(kop="Wat eerst?", opdracht="Schrijf 1, 2 en 3.", oefeningen=[("rij", [("Je droogt je af.", "3"), ("Je vult het bad.", "1"), ("Je neemt een bad.", "2")], "", "60px"),
            ("rij", [("Er groeit een plantje.", "2"), ("Je plant een zaadje.", "1"), ("Er komt een bloem.", "3")], "", "60px")]),
        dict(kop="Hoe voelt hij zich?", oefeningen=[("rij", [("Tim krijgt een cadeau.", "blij"), ("Lies valt van haar fiets.", "verdrietig"), ("Het onweert.", "bang")], "Blij, verdrietig of bang?", B)]),
        dict(kop="Teken het verhaal", oefeningen=[("teken", "Teken in drie vakjes: eerst, daarna en op het einde. Kies zelf een verhaal.", "eigen tekening", 55)]),
    ]))


if __name__ == "__main__":
    for k in sys.argv[1:] or list(H):
        naam, module, leer, oefen = H[k]
        maak(naam, "nederlands", leer, oefen, module.replace("-", "_"))

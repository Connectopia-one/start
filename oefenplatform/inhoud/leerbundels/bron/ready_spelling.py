# -*- coding: utf-8 -*-
"""Leer- en oefenbundel bij het Ready-proefhoofdstuk Nederlands "Spelling"
(3de en 4de leerjaar, 26 november 2026). De vragen op het scherm staan in
../../ready/bron/nederlands_spelling.py; de oefenbundel vraagt andere woorden.

    python3 ready_spelling.py
"""
import pathlib, subprocess, sys
HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))
import bundel, oefenbundel

tabel = bundel.tabel
# Ready is voor kinderen van 8 en 9: grotere letters dan in Start.
GROOT = ("body{font-size:13.5pt;line-height:1.7}table{font-size:12pt}figcaption{font-size:11pt}"
         ".oef .vraagtekst,.rij .cel{font-size:13pt}.hoe li,.opdracht{font-size:12pt}"
         # Fijne motoriek is op deze leeftijd nog volop in ontwikkeling: hogere lijnen en grotere vakjes.
         ".lijn{height:54px}.vakje{height:38px;min-width:120px !important}.rij .cel{line-height:2.8}")
bundel.CSS += GROOT
oefenbundel.OEFEN_CSS += GROOT
READY = "🎒 Ready — 3de en 4de leerjaar"
NAAM = "spelling-ready"

BUNDEL = dict(
    vak="Nederlands", niveau=READY, titel="Spelling",
    onder="Klankgroepen, d/t en b/p op het einde, meervoud, verkleinwoord en hoofdletters.",
    secties=[
        dict(kop="Woorden om te onthouden: ei of ij, au of ou", blokken=[
            ("p", "Je hoort geen verschil tussen ei en ij, en ook niet tussen au en ou. Die woorden moet je <strong>onthouden</strong>. "
                  "Lees ze vaak en schrijf ze over."),
            ("fig", tabel(["ei", "ij", "au", "ou"], [
                ["trein", "ijs", "blauw", "koud"], ["klein", "vijf", "pauw", "zout"], ["geit", "tijd", "saus", "hout"],
                ["plein", "wijn", "auto", "vrouw"], ["reis", "prijs", "flauw", "goud"]], "100%")),
            ("weetje", "Een handig trucje voor ei: 'De kleine geit reist met de trein naar het plein.'"),
        ]),
        dict(kop="aai, oei, ooi, eeuw en ieuw", blokken=[
            ("p", "Na aa, oe en oo komt er een <strong>i</strong>. Na ee en ie komt er een <strong>uw</strong>."),
            ("fig", tabel(["aai", "oei", "ooi", "eeuw", "ieuw"], [
                ["haai", "koei", "mooi", "sneeuw", "nieuw"], ["kraai", "groei", "kooi", "leeuw", "kieuw"], ["draaien", "boei", "hooi", "meeuw", "—"]], "100%")),
        ]),
        dict(kop="ng of nk", blokken=[
            ("p", "Luister goed naar het einde. Hoor je een <strong>k</strong>, dan schrijf je <strong>nk</strong>: bank, drink, denk. "
                  "Hoor je geen k, dan schrijf je <strong>ng</strong>: ring, bang, koning."),
        ]),
        dict(kop="Verlengen: g of ch, d of t, b of p", blokken=[
            ("p", "Op het einde van een woord hoor je niet goed of het een g of ch is, een d of t, een b of p. "
                  "<strong>Maak het woord langer</strong>, dan hoor je het wel."),
            ("fig", tabel(["Woord", "Langer maken", "Je hoort"], [
                ["dag", "dagen", "g"], ["lach", "lachen", "ch"], ["hond", "honden", "d"],
                ["kat", "katten", "t"], ["web", "webben", "b"], ["kip", "kippen", "p"]], "100%")),
        ]),
        dict(kop="Meervoud", blokken=[
            ("p", "Meestal komt er <strong>-en</strong> achter (boek, boeken). Soms <strong>-s</strong> (tafel, tafels). "
                  "Eindigt een woord op a, o, u of i, dan komt er <strong>'s</strong> achter (auto's, oma's)."),
            ("fig", tabel(["Eén", "Meer", "Let op"], [
                ["boom", "bomen", "lange klank: één o is genoeg"], ["bal", "ballen", "korte klank: de l verdubbelt"],
                ["huis", "huizen", "s wordt z"], ["brief", "brieven", "f wordt v"]], "100%")),
        ]),
        dict(kop="Verkleinwoord", blokken=[
            ("fig", tabel(["Uitgang", "Voorbeelden"], [
                ["-je", "huisje, boekje"], ["-tje", "stoeltje, eitje"], ["-pje", "boompje, raampje"],
                ["-etje", "balletje, ringetje"], ["-kje", "koninkje"]], "100%")),
        ]),
        dict(kop="Hoofdletters", blokken=[
            ("p", "Een hoofdletter schrijf je aan het <strong>begin van een zin</strong> en bij <strong>namen</strong> van mensen, "
                  "dieren, steden en landen: Sara, Gent, België."),
            ("p", "Dagen en maanden krijgen <strong>geen</strong> hoofdletter: maandag, juli."),
        ]),
    ],
    onthoud=[
        "ei/ij en au/ou: onthouden, vaak lezen en overschrijven.",
        "aai, oei, ooi eindigen op i. eeuw en ieuw eindigen op w.",
        "nk: je hoort een k. ng: geen k.",
        "Twijfel je op het einde? Maak het woord langer: dagen, honden, webben.",
        "Meervoud: -en, -s of 's. Verkleinwoord: -je, -tje, -pje, -etje, -kje.",
        "Hoofdletter: begin van de zin en namen. Niet bij dagen en maanden.",
    ])

W = "80px"
OEFEN = dict(
    vak="Nederlands", niveau=READY, titel="Spelling",
    onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.",
    hoe=["Schrijf met potlood, dan kan je gerust iets uitgommen.",
         "Twijfel je op het einde van een woord? Maak het woord langer en luister.",
         "Het antwoordblad zit achteraan. Scheur het eraf voor je begint."],
    reeksen=[
        dict(kop="ei of ij", opdracht="Schrijf ei of ij in het hokje.", oefeningen=[
            ("invulwoord", [("kl__n (niet groot)", "klein"), ("r__st (eet je met kip)", "rijst"), ("pl__n (open plaats in de stad)", "plein"),
                     ("m__n (van mij)", "mijn"), ("r__s (op vakantie)", "reis"), ("wij z__n thuis", "zijn")], ""),
        ]),
        dict(kop="au of ou", opdracht="Schrijf au of ou in het hokje.", oefeningen=[
            ("invulwoord", [("h__t (van een boom)", "hout"), ("s__s (op je frietjes)", "saus"), ("g__d (een kostbaar metaal)", "goud"),
                     ("fl__w (niet sterk)", "flauw"), ("m__w (van je trui)", "mouw"), ("t__w (een dik koord)", "touw")], ""),
        ]),
        dict(kop="aai, oei, ooi, eeuw of ieuw", opdracht="Schrijf aai, oei, ooi, eeuw of ieuw in het hokje.", oefeningen=[
            ("invulwoord", [("een kr__ (zwarte vogel)", "kraai"), ("de gr__ (groter worden)", "groei"), ("het h__ (droog gras)", "hooi"),
                     ("een m__ (vogel aan zee)", "meeuw"), ("de k__ (van een vis)", "kieuw")], ""),
        ]),
        dict(kop="ng of nk", opdracht="Schrijf ng of nk in het hokje.", oefeningen=[
            ("invulwoord", [("de ri__", "ring"), ("ik de__ na", "denk"), ("de ba__ (om op te zitten)", "bank"), ("ik zi__ een liedje", "zing")], ""),
        ]),
        dict(kop="Juist of fout?", opdracht="Telkens is één woord juist en één fout geschreven. Streep het foute woord door.", oefeningen=[
            ("invulwoord", [("trein &nbsp; / &nbsp; trijn", "trein"),
                     ("blouw &nbsp; / &nbsp; blauw", "blauw"),
                     ("koei &nbsp; / &nbsp; koeij", "koei"),
                     ("sneew &nbsp; / &nbsp; sneeuw", "sneeuw"),
                     ("bank &nbsp; / &nbsp; bangk", "bank"),
                     ("berch &nbsp; / &nbsp; berg", "berg"),
                     ("hond &nbsp; / &nbsp; hont", "hond"),
                     ("webb &nbsp; / &nbsp; web", "web"),
                     ("bomen &nbsp; / &nbsp; boomen", "bomen"),
                     ("ballen &nbsp; / &nbsp; balen", "ballen"),
                     ("stoelje &nbsp; / &nbsp; stoeltje", "stoeltje"),
                     ("Gent &nbsp; / &nbsp; gent", "Gent")], ""),
        ]),
        dict(kop="Maak het woord langer", opdracht="Schrijf het lange woord en dan het juiste korte woord.", oefeningen=[
            ("tabel", ["Twijfel", "Langer", "Juist"], [["ber? (g of ch)", None, None], ["har? (d of t)", None, None],
                                                       ["kra? (b of p)", None, None], ["bro? (d of t)", None, None], ["we? (g of ch)", None, None]],
             "bergen, berg · harden, hard · krabben, krab · broden, brood · wegen, weg", "120px"),
        ]),
        dict(kop="Meervoud", opdracht="Schrijf het meervoud.", oefeningen=[
            ("rij", [("een maan", "manen"), ("een pot", "potten"), ("een oma", "oma's"), ("een muis", "muizen"),
                     ("een wolf", "wolven"), ("een appel", "appels")], "", "120px"),
        ]),
        dict(kop="Verkleinwoord", opdracht="Schrijf het verkleinwoord.", oefeningen=[
            ("rij", [("boek", "boekje"), ("raam", "raampje"), ("kar", "karretje"), ("tuin", "tuintje"), ("ring", "ringetje"), ("auto", "autootje")], "", "120px"),
        ]),
        dict(kop="Hoofdletters", oefeningen=[
            ("open", "Schrijf de zin juist over: op zaterdag gaat tom met zijn hond max naar antwerpen.",
             "Op zaterdag gaat Tom met zijn hond Max naar Antwerpen.", 2),
            ("waar", "In juli is het vakantie: juli schrijf je met een kleine letter.", True),
            ("waar", "De naam van een land schrijf je met een kleine letter.", False),
        ]),
        dict(kop="Dictee", opdracht="Laat iemand deze zinnen voorlezen. Schrijf ze op. Kijk daarna zelf na.", oefeningen=[
            ("open", "Zin 1 (voorlezer: zie antwoordblad)", "De kleine geit eet hooi in de koude sneeuw.", 2),
            ("open", "Zin 2 (voorlezer: zie antwoordblad)", "Mijn hond drinkt water uit een blauwe pot.", 2),
            ("open", "Zin 3 (voorlezer: zie antwoordblad)", "Op maandag reist Lien met de trein naar Brugge.", 2),
        ]),
    ])


def maak():
    from ready_gemeen import met_prenten
    met_prenten(BUNDEL, OEFEN, "nederlands_spelling")
    for maker, b, basis, naam in ((bundel, BUNDEL, HIER.parent, NAAM),
                                  (oefenbundel, OEFEN, HIER.parent.parent / "oefenbundels", "oefenbundel-" + NAAM)):
        tijdelijk = "ready-" + naam
        maker.schrijf(b, tijdelijk)
        subprocess.run(["node", str(HIER / "pdf.js"), tijdelijk], cwd=HIER, check=True)
        doel = basis / "nederlands" / f"{naam}.pdf"
        doel.write_bytes((HIER / f"{tijdelijk}.pdf").read_bytes())
        print("  ", doel.relative_to(HIER.parent.parent))


if __name__ == "__main__":
    maak()

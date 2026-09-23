# -*- coding: utf-8 -*-
"""De leerbundel bij het gratis proefhoofdstuk Spelling van Nederlands.

Dit is het hoofdstuk dat iedereen mag proberen zonder account. Het is dus ook
het enige wat een ouder van het platform te zien krijgt voor die beslist, en
daarom staat er hier meer in dan in een gewone bundel: tien stukken in plaats
van vijf of zes, en bij elke regel een voorbeeld dat je meteen kan nakijken.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel
tabel = bundel.tabel

BUNDELS = {}

BUNDELS["spelling"] = dict(
    vak="Nederlands", titel="Spelling",
    onder="De regels die je het vaakst nodig hebt, met bij elke regel een voorbeeld.",
    secties=[
        dict(kop="Spelling is luisteren én kijken", blokken=[
            ("p", "Veel woorden schrijf je gewoon zoals je ze hoort. Bij een aantal woorden lukt dat "
                  "niet: je hoort <i>hij wordt</i> en <i>hij word</i> precies hetzelfde. Voor die "
                  "woorden bestaan er regels, en die regels zijn er niet om je te pesten: ze zorgen "
                  "ervoor dat iedereen hetzelfde woord op dezelfde manier schrijft."),
            ("p", "Een woord bestaat uit <strong>lettergrepen</strong>: stukjes die je in één keer "
                  "uitspreekt. Klap maar eens mee: <i>va-kan-tie</i> is drie klappen, <i>school</i> "
                  "is er één. Bijna alle spellingregels beginnen bij die lettergrepen, dus het loont "
                  "om eerst te leren klappen."),
            ("kader", "<strong>Klinkers</strong> zijn a, e, i, o, u (en y). Alle andere letters zijn "
                      "<strong>medeklinkers</strong>. Elke lettergreep heeft minstens één klinker — "
                      "daarom kan je <i>str</i> niet uitspreken en <i>stra</i> wel."),
        ]),
        dict(kop="Open en gesloten lettergrepen", blokken=[
            ("p", "Verdeel een woord in lettergrepen en kijk naar de <strong>eerste</strong>. Eindigt "
                  "die op een klinker, dan is ze <strong>open</strong>. Eindigt ze op een medeklinker, "
                  "dan is ze <strong>gesloten</strong>. Dat verschil bepaalt of je een letter verdubbelt."),
            ("fig", svg.lettergrepen(),
             "Dezelfde letters, één medeklinker verschil, en een heel ander woord."),
            ("p", "In een <strong>open</strong> lettergreep klinkt de klinker lang, en schrijf je hem "
                  "toch maar één keer: <i>ra-men</i>, <i>bo-men</i>, <i>de-len</i>. In een "
                  "<strong>gesloten</strong> lettergreep klinkt hij kort, en verdubbel je de "
                  "medeklinker erachter: <i>ram-men</i>, <i>bom-men</i>, <i>bel-len</i>."),
            ("weetje", "Twijfel je? Zeg het meervoud hardop. Hoor je <i>raa-men</i> met een lange aa, "
                       "dan is het één m. Hoor je <i>ram-men</i> kort, dan zijn het er twee."),
        ]),
        dict(kop="De stam van een werkwoord", blokken=[
            ("p", "Om een werkwoord goed te schrijven, heb je de <strong>stam</strong> nodig. Die vind "
                  "je zo: neem het hele werkwoord en haal <i>-en</i> weg. <i>Werken</i> wordt "
                  "<i>werk</i>, <i>lopen</i> wordt <i>loop</i>, <i>bouwen</i> wordt <i>bouw</i>."),
            ("kader", "Let op bij <i>lopen</i>. Haal je <i>-en</i> weg, dan blijft <i>lop</i> over, en "
                      "dat is een gesloten lettergreep met een korte o. Je hoort een lange oo, dus "
                      "schrijf je de klinker dubbel: <strong>loop</strong>. Zo ook <i>eten → eet</i> "
                      "en <i>nemen → neem</i>."),
            ("p", "Nog een vuistregel: de stam is wat je zegt na <strong>ik</strong>. Ik werk, ik loop, "
                  "ik bouw, ik eet. Dat werkt bijna altijd, en het is sneller dan tellen."),
        ]),
        dict(kop="Werkwoorden in de tegenwoordige tijd", blokken=[
            ("p", "Gebeurt het nu, dan hangt het van de persoon af of er een <strong>-t</strong> "
                  "achter de stam komt."),
            ("fig", svg.werkwoord_nu(),
             "De derde regel is de lastigste: staat <i>jij</i> achter het werkwoord, dan valt de t weg."),
            ("p", "Die derde regel zie je vooral in vragen. <i>Jij wordt boos</i>, maar <i>word jij "
                  "boos?</i> En ook in een zin als <i>Wat word jij later?</i> — <i>jij</i> staat "
                  "achter het werkwoord, dus geen t."),
            ("weetje", "De fout die het vaakst gemaakt wordt is <i>hij vind</i> in plaats van "
                       "<i>hij vindt</i>. De stam is <i>vind</i>, en <i>hij</i> krijgt er een t bij. "
                       "Dat de d en de t naast elkaar staan, verandert daar niets aan."),
        ]),
        dict(kop="Werkwoorden in de verleden tijd", blokken=[
            ("p", "Gebeurde het vroeger, dan komt er <strong>-te(n)</strong> of <strong>-de(n)</strong> "
                  "achter de stam. Welke van de twee, dat verklapt een oud ezelsbruggetje: "
                  "<strong>'t kofschip</strong>."),
            ("fig", svg.kofschip(),
             "Eindigt de stam op t, k, f, s, ch of p, dan is het -te. In alle andere gevallen -de."),
            ("p", "Zo: <i>werken → ik werkte</i> (k zit in 't kofschip), <i>leren → ik leerde</i> "
                  "(r zit er niet in). Met meer dan één persoon wordt het <i>-ten</i> of <i>-den</i>: "
                  "<i>wij werkten</i>, <i>wij leerden</i>."),
            ("kader", "Luister naar de <strong>klank</strong> van de stam, niet naar de letter. "
                      "<i>Verhuizen</i> heeft als stam <i>verhuis</i>, maar de laatste klank is een z, "
                      "en die zit niet in 't kofschip: <i>ik verhuisde</i>. Zo ook <i>geloven → "
                      "ik geloofde</i>."),
        ]),
        dict(kop="Het voltooid deelwoord", blokken=[
            ("p", "Het voltooid deelwoord is de vorm na <i>heb</i>, <i>heeft</i>, <i>ben</i> of "
                  "<i>is</i>: <i>ik heb gewerkt</i>. Je maakt hem met <strong>ge-</strong> vooraan en "
                  "<strong>-d</strong> of <strong>-t</strong> achteraan, en welke van die twee zegt "
                  "opnieuw 't kofschip."),
            ("kader", tabel(["Werkwoord", "Stam", "Laatste klank", "Voltooid deelwoord"],
                            [["werken", "werk", "k — in 't kofschip", "gewerk<b>t</b>"],
                             ["leren", "leer", "r — niet erin", "geleer<b>d</b>"],
                             ["hopen", "hoop", "p — in 't kofschip", "gehoop<b>t</b>"],
                             ["reizen", "reis", "z-klank — niet erin", "gereis<b>d</b>"]])),
            ("weetje", "Twijfel je tussen <i>-d</i> en <i>-t</i>? Zet er een woord achter dat met een "
                       "klinker begint: <i>de geleerde man</i>, <i>het gewerkte uur</i>. Nu hoor je "
                       "het verschil wel."),
        ]),
        dict(kop="Meervoud", blokken=[
            ("p", "De meeste woorden krijgen <strong>-en</strong>: <i>boek → boeken</i>. Daarbij "
                  "gelden gewoon de regels van de lettergrepen, dus <i>bal → ballen</i> maar "
                  "<i>raam → ramen</i>."),
            ("kader", tabel(["Uitgang", "Wanneer", "Voorbeeld"],
                            [["-en", "de gewone manier", "boek → boeken"],
                             ["-s", "na -el, -em, -en, -er, -je", "tafel → tafels"],
                             ["'s", "na een losse a, i, o, u of y", "oma → oma's"],
                             ["-eren", "bij een handvol oude woorden", "kind → kinderen"]])),
            ("p", "Dat apostrofje bij <i>oma's</i> staat er om de klank te redden. Zonder streepje zou "
                  "je <i>omas</i> lezen met een korte a. Bij <i>auto's</i>, <i>menu's</i> en "
                  "<i>taxi's</i> is het net zo."),
        ]),
        dict(kop="Verkleinwoorden", blokken=[
            ("p", "Een verkleinwoord maak je met <strong>-je</strong>, maar afhankelijk van de klank "
                  "ervoor verandert die uitgang een beetje. Je hoort het meestal vanzelf."),
            ("fig", svg.verkleinwoorden(),
             "Zeg het woord hardop; bijna altijd kies je vanzelf de juiste uitgang."),
            ("p", "Een verkleinwoord is altijd <strong>het</strong>: het boekje, het stoeltje, het "
                  "meisje. Ook als het grondwoord <i>de</i> had — <i>de stoel</i>, maar "
                  "<i>het stoeltje</i>."),
        ]),
        dict(kop="Woorden die op elkaar lijken", blokken=[
            ("p", "Sommige klanken kan je op twee manieren schrijven. Daar helpt geen regel bij: die "
                  "woorden moet je leren kennen. Deze zie je het vaakst."),
            ("kader", tabel(["Klank", "De ene manier", "De andere manier"],
                            [["ei / ij", "ei: trein, klein, eind", "ij: tijd, wijs, blij"],
                             ["au / ou", "au: pauw, saus, blauw", "ou: koud, hout, vrouw"],
                             ["ch / g", "ch: lachen, nacht, echt", "g: dragen, vogel, groot"],
                             ["c / k", "c: cirkel, citroen, cent", "k: kat, kist, kost"]])),
            ("weetje", "De c spreek je uit als een s voor een e, i of y (<i>cent</i>, <i>cirkel</i>) en "
                       "als een k voor een a, o of u (<i>cacao</i>, <i>computer</i>). Dat is geen "
                       "toeval: die woorden komen uit het Latijn en het Frans."),
        ]),
        dict(kop="Hoofdletters en samenstellingen", blokken=[
            ("p", "Een <strong>hoofdletter</strong> zet je vooraan in een zin, bij namen van mensen, "
                  "plaatsen, landen en talen, en bij feestdagen. Dus: <i>Lien woont in Hasselt en "
                  "spreekt Nederlands.</i> Namen van dagen en maanden krijgen er in het Nederlands "
                  "géén: <i>maandag</i>, <i>april</i>."),
            ("p", "Twee woorden die samen één woord worden, schrijf je <strong>aan elkaar</strong>: "
                  "<i>voetbal</i>, <i>tandarts</i>, <i>schoolbus</i>. Soms komt er een letter tussen."),
            ("kader", "<strong>Tussen-n:</strong> denk aan het meervoud van het eerste woord. "
                      "Eén pan, veel pannen → <i>pannenkoek</i>. Eén zon maar, dus "
                      "<i>zonneschijn</i> — toch met n, want die uitzondering is afgesproken.<br>"
                      "<strong>Tussen-s:</strong> hoor je een s, dan schrijf je er een: "
                      "<i>stationschef</i>, <i>dorpsstraat</i>, <i>verkeersbord</i>."),
            ("fig", svg.stappen(["hoor je|één woord?", "schrijf het|aan elkaar",
                                 "hoor je een|tussenklank?", "schrijf die|erbij"]),
             "Bij twijfel: spreek de samenstelling uit en luister naar wat er in het midden gebeurt."),
        ]),
    ],
    onthoud=[
        "Open lettergreep = eindigt op een klinker = één medeklinker: ra-men.",
        "Gesloten lettergreep = eindigt op een medeklinker = verdubbelen: ram-men.",
        "De stam is het hele werkwoord min -en, of gewoon: wat je zegt na ik.",
        "Nu: ik = stam, jij/hij/zij/u = stam + t, wij/jullie/zij = hele werkwoord.",
        "Staat jij ná het werkwoord, dan valt de t weg: word jij?",
        "Vroeger: 't kofschip. Stam eindigt op t, k, f, s, ch of p → -te, anders -de.",
        "Voltooid deelwoord: ge- vooraan, en -t of -d volgens 't kofschip.",
        "Meervoud: meestal -en, na -el/-em/-en/-er/-je een -s, na een losse klinker 's.",
        "Een verkleinwoord is altijd het: het stoeltje, ook al is het de stoel.",
        "Hoofdletters bij namen, landen en talen; niet bij dagen en maanden.",
    ])


if __name__ == "__main__":
    for naam, b in BUNDELS.items():
        bundel.schrijf(b, naam)

# -*- coding: utf-8 -*-
"""Leer- en oefenbundels bij de Ready-hoofdstukken Nederlands (3de en 4de leerjaar),
behalve Spelling (zie ready_spelling.py). De vragen op het scherm staan in
../../ready/bron/nederlands_*.py; de oefenbundels vragen andere woorden en zinnen.
Alle leesteksten zijn eigen teksten.

    python3 ready_nederlands.py              # alles
    python3 ready_nederlands.py werkwoorden  # één hoofdstuk
"""
import sys
from ready_gemeen import maak, tabel, READY

HOE = ["Schrijf met potlood, dan kan je gerust iets uitgommen.",
       "Lees elke opdracht eerst helemaal voor je begint.",
       "Het antwoordblad zit achteraan. Scheur het eraf voor je begint."]
B = "130px"
H = {}

# ---------------------------------------------------------------- werkwoorden
H["werkwoorden"] = ("werkwoorden-ready", dict(
    vak="Nederlands", niveau=READY, titel="Werkwoorden",
    onder="De tegenwoordige tijd met ik, jij en hij, de vraag met jij, de verleden tijd en het voltooid deelwoord.",
    secties=[
        dict(kop="Wat is een werkwoord?", blokken=[
            ("p", "Een werkwoord zegt wat iemand <strong>doet</strong> of wat er <strong>gebeurt</strong>: lopen, eten, lachen, regenen."),
            ("p", "De <strong>stam</strong> vind je door het werkwoord met ik te zeggen: werken → ik werk. Stam = <strong>werk</strong>."),
        ]),
        dict(kop="Nu: de tegenwoordige tijd", blokken=[
            ("fig", tabel(["Wie?", "Regel", "werken", "worden", "lezen"], [
                ["ik", "stam", "ik werk", "ik word", "ik lees"],
                ["jij, je, u", "stam + t", "jij werkt", "jij wordt", "jij leest"],
                ["hij, zij, het", "stam + t", "hij werkt", "hij wordt", "zij leest"],
                ["wij, jullie, zij", "heel werkwoord", "wij werken", "wij worden", "wij lezen"]], "100%")),
            ("kader", "<strong>Let op bij een vraag!</strong> Staat <strong>jij</strong> achter het werkwoord, dan valt de t weg:<br>"
                      "jij werkt → <strong>werk jij?</strong> · jij wordt → <strong>word jij?</strong>"),
            ("weetje", "Bij hij wordt en hij vindt hoor je de t niet, maar je schrijft hem wel: stam + t."),
        ]),
        dict(kop="Vroeger: de verleden tijd", blokken=[
            ("p", "Wat al gebeurd is, vertel je in de <strong>verleden tijd</strong>. Veel werkwoorden krijgen <strong>-de</strong> of <strong>-te</strong>: ik speelde, ik werkte."),
            ("p", "Andere veranderen van klank. Die leer je vanbuiten:"),
            ("fig", tabel(["Nu", "Vroeger", "Nu", "Vroeger"], [["ik loop", "ik liep", "ik eet", "ik at"], ["ik ga", "ik ging", "ik drink", "ik dronk"],
                ["ik schrijf", "ik schreef", "ik kom", "ik kwam"], ["ik ben", "ik was", "ik heb", "ik had"]], "100%")),
        ]),
        dict(kop="Het voltooid deelwoord", blokken=[
            ("p", "Bij <strong>hebben</strong> of <strong>zijn</strong> hoort een voltooid deelwoord. Het begint vaak met <strong>ge</strong>: ik heb gespeeld, ik heb gewerkt, ik ben gelopen."),
            ("p", "Twijfel je tussen d en t op het einde? Maak het woord langer: de gespeelde match (d), het gewerkte uur (t)."),
        ]),
    ],
    onthoud=["Ik: stam. Jij en hij: stam + t. Wij: heel werkwoord.", "Jij achter het werkwoord: geen t (werk jij?).",
             "Verleden tijd: -de of -te, of een andere klank (liep, ging).", "Hebben of zijn + voltooid deelwoord: gespeeld, gelopen."]),
    dict(vak="Nederlands", niveau=READY, titel="Werkwoorden", onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE, reeksen=[
        dict(kop="Zoek het werkwoord", oefeningen=[
            ("rij", [("De hond blaft luid.", "blaft"), ("Wij zwemmen in het meer.", "zwemmen"), ("Oma bakt een taart.", "bakt"), ("Het regent al de hele dag.", "regent")], "Schrijf het werkwoord.", B),
        ]),
        dict(kop="Stam + t?", opdracht="Schrijf de juiste vorm in het hokje.", oefeningen=[
            ("invulwoord", [("ik ____ (lopen)", "loop"), ("hij ____ (lopen)", "loopt"), ("jij ____ (fietsen)", "fietst"), ("zij ____ (lachen, één meisje)", "lacht"),
                            ("wij ____ (zingen)", "zingen"), ("het ____ (sneeuwen)", "sneeuwt")], ""),
            ("invulwoord", [("ik ____ (worden)", "word"), ("hij ____ (worden)", "wordt"), ("ik ____ (vinden)", "vind"), ("Mila ____ (vinden)", "vindt"),
                            ("jij ____ (rijden)", "rijdt"), ("ik ____ (houden)", "houd")], ""),
        ]),
        dict(kop="Vraagzinnen met jij", opdracht="Schrijf de juiste vorm in het hokje. Kijk waar jij staat!", oefeningen=[
            ("invulwoord", [("____ jij mee? (spelen)", "Speel"), ("Jij ____ mee. (spelen)", "speelt"), ("____ jij morgen tien? (worden)", "Word"),
                            ("____ jij dat leuk? (vinden)", "Vind"), ("Wat ____ jij? (lezen)", "lees"), ("Jij ____ een boek. (lezen)", "leest")], ""),
        ]),
        dict(kop="Juist of fout?", opdracht="Telkens is één vorm juist en één fout. Streep de foute vorm door.", oefeningen=[
            ("invulwoord", [("hij word &nbsp; / &nbsp; hij wordt", "hij wordt"), ("ik vind &nbsp; / &nbsp; ik vindt", "ik vind"),
                            ("loopt jij? &nbsp; / &nbsp; loop jij?", "loop jij?"), ("zij leest &nbsp; / &nbsp; zij lees", "zij leest"),
                            ("wij lacht &nbsp; / &nbsp; wij lachen", "wij lachen"), ("ik heb gespeeld &nbsp; / &nbsp; ik heb gespeelt", "ik heb gespeeld")], ""),
        ]),
        dict(kop="Verleden tijd", oefeningen=[
            ("tabel", ["Nu", "Vroeger"], [["ik speel", None], ["ik loop", None], ["ik ga", None], ["ik eet", None], ["wij zijn", None], ["hij schrijft", None]],
             "ik speelde · ik liep · ik ging · ik at · wij waren · hij schreef", "170px"),
            ("open", "Schrijf deze zin in de verleden tijd: Ik drink melk en ik kom te laat.", "Ik dronk melk en ik kwam te laat.", 2),
        ]),
        dict(kop="Voltooid deelwoord", opdracht="Schrijf het voltooid deelwoord in het hokje.", oefeningen=[
            ("invulwoord", [("ik heb ____ (maken)", "gemaakt"), ("wij hebben ____ (zingen)", "gezongen"), ("ik ben ____ (lopen)", "gelopen"),
                            ("zij heeft ____ (fietsen)", "gefietst"), ("ik heb ____ (eten)", "gegeten"), ("hij heeft ____ (spelen)", "gespeeld")], ""),
        ]),
        dict(kop="Schrijf zelf", oefeningen=[
            ("open", "Schrijf drie zinnen over wat je gisteren gedaan hebt. Onderlijn telkens het werkwoord.", "eigen zinnen in de verleden tijd", 4),
        ]),
    ]))

# ---------------------------------------------------------------- woordsoorten
H["woordsoorten"] = ("woordsoorten-en-zinnen-ready", dict(
    vak="Nederlands", niveau=READY, titel="Woordsoorten en zinnen",
    onder="Zelfstandig naamwoord, lidwoord, bijvoeglijk naamwoord en werkwoord. Onderwerp, persoonsvorm en leestekens.",
    secties=[
        dict(kop="Vier soorten woorden", blokken=[
            ("fig", tabel(["Woordsoort", "Wat is het?", "Voorbeelden"], [
                ["zelfstandig naamwoord", "een mens, dier, ding of naam", "jongen, kat, fiets, Gent"],
                ["lidwoord", "staat voor een zelfstandig naamwoord", "de, het, een"],
                ["bijvoeglijk naamwoord", "zegt hoe iets is", "groot, rood, lief"],
                ["werkwoord", "zegt wat iemand doet", "lopen, eten, slapen"]], "100%")),
            ("p", "<strong>De grote hond blaft.</strong> de = lidwoord, grote = bijvoeglijk naamwoord, hond = zelfstandig naamwoord, blaft = werkwoord."),
        ]),
        dict(kop="De of het?", blokken=[
            ("p", "Zet het woord in een zinnetje en luister: de boom, het huis. Twee handige regels:"),
            ("kader", "Een <strong>verkleinwoord</strong> krijgt altijd <strong>het</strong>: het boompje, het meisje.<br>"
                      "Een <strong>meervoud</strong> krijgt altijd <strong>de</strong>: de huizen, de paarden."),
        ]),
        dict(kop="Onderwerp en persoonsvorm", blokken=[
            ("p", "De <strong>persoonsvorm</strong> vind je zo: zet de zin in een andere tijd. Het werkwoord dat verandert, is de persoonsvorm. Lies <u>fietst</u> → Lies <u>fietste</u>."),
            ("p", "Het <strong>onderwerp</strong> vind je met de vraag: <strong>wie of wat</strong> + persoonsvorm? Wie fietst? <strong>Lies</strong>."),
            ("weetje", "Het onderwerp staat niet altijd vooraan: In de zomer zwemt <strong>Noor</strong> in het meer."),
        ]),
        dict(kop="Soorten zinnen en leestekens", blokken=[
            ("fig", tabel(["Soort zin", "Leesteken", "Voorbeeld"], [["mededeling", ". (punt)", "Ik ben negen jaar."], ["vraag", "? (vraagteken)", "Hoe oud ben jij?"],
                ["uitroep", "! (uitroepteken)", "Wat een mooie dag!"]], "100%")),
            ("p", "Een <strong>komma</strong> zet je in een opsomming: appels, peren en bananen. Wat iemand zegt, zet je tussen <strong>aanhalingstekens</strong>: Mama zei: \"Kom eten!\""),
        ]),
    ],
    onthoud=["Zelfstandig naamwoord: mens, dier, ding. Lidwoord: de, het, een.", "Bijvoeglijk naamwoord: hoe iets is. Werkwoord: wat iemand doet.",
             "Verkleinwoord: het. Meervoud: de.", "Persoonsvorm: verandert van tijd. Onderwerp: wie of wat + persoonsvorm?", "Elke zin: hoofdletter vooraan, leesteken achteraan."]),
    dict(vak="Nederlands", niveau=READY, titel="Woordsoorten en zinnen", onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE, reeksen=[
        dict(kop="Sorteer de woorden", oefeningen=[
            ("tekst", "Schrijf elk woord in de juiste kolom: tafel – zacht – springen – poes – blauw – lezen – Anna – oud – slapen"),
            ("tabel", ["zelfstandig naamwoord", "bijvoeglijk naamwoord", "werkwoord"], [[None, None, None], [None, None, None], [None, None, None]],
             "zelfstandig naamwoord: tafel, poes, Anna · bijvoeglijk naamwoord: zacht, blauw, oud · werkwoord: springen, lezen, slapen", "150px"),
        ]),
        dict(kop="De of het?", opdracht="Schrijf de of het in het hokje.", oefeningen=[
            ("invulwoord", [("__ paard", "het"), ("__ stoel", "de"), ("__ boekje", "het"), ("__ bomen", "de"), ("__ raam", "het"), ("__ fiets", "de")], ""),
        ]),
        dict(kop="Bijvoeglijk naamwoord", oefeningen=[
            ("open", "Maak de zin mooier met twee bijvoeglijke naamwoorden: De ... kat slaapt op de ... mat.", "bv. De zwarte kat slaapt op de zachte mat.", 2),
        ]),
        dict(kop="Persoonsvorm en onderwerp", opdracht="Onderlijn de persoonsvorm en omcirkel het onderwerp.", oefeningen=[
            ("invulwoord", [("Tim eet een appel.", "persoonsvorm eet, onderwerp Tim"), ("De kinderen spelen buiten.", "persoonsvorm spelen, onderwerp de kinderen"),
                     ("Morgen gaat oma naar de markt.", "persoonsvorm gaat, onderwerp oma")], ""),
        ]),
        dict(kop="Leestekens", opdracht="Zet het juiste leesteken in het hokje.", oefeningen=[
            ("invulwoord", [("Waar woon jij__", "?"), ("Ik woon in Hasselt__", "."), ("Wat een grote taart__", "!"), ("Heb je honger__", "?")], ""),
            ("open", "Schrijf de zin juist over, met hoofdletters, komma's en een punt: op het feest waren tom lies sara en jonas",
             "Op het feest waren Tom, Lies, Sara en Jonas.", 2),
        ]),
        dict(kop="Juist of fout?", opdracht="Telkens is één zin juist en één fout. Streep de foute zin door.", oefeningen=[
            ("invulwoord", [("het boompje &nbsp; / &nbsp; de boompje", "het boompje"), ("de huizen &nbsp; / &nbsp; het huizen", "de huizen"),
                            ("ik woon in brugge. &nbsp; / &nbsp; Ik woon in Brugge.", "Ik woon in Brugge."), ("Kom je spelen? &nbsp; / &nbsp; Kom je spelen.", "Kom je spelen?")], ""),
        ]),
    ]))

# ---------------------------------------------------------------- lezen
TEKST_OEF = ("<strong>De nieuwe buurman</strong><br>Naast het huis van Yara woont sinds maandag een nieuwe buurman. Hij heet meneer Tijs en hij heeft een grote, "
             "grijze hond. De hond heet Wolk. 's Morgens wandelt meneer Tijs altijd met Wolk door het park. Yara mag soms mee. Ze gooit dan een tak, en Wolk "
             "brengt hem telkens terug. Op woensdag regende het zo hard dat ze thuisbleven. Wolk lag de hele middag te zuchten bij de deur.")
H["lezen"] = ("lezen-en-woordenschat-ready", dict(
    vak="Nederlands", niveau=READY, titel="Lezen en woordenschat",
    onder="Een tekst goed lezen, tussen de regels lezen, moeilijke woorden begrijpen, synoniemen, tegenstellingen en samenstellingen.",
    secties=[
        dict(kop="Zo lees je een tekst", blokken=[
            ("kader", "<strong>Voor het lezen:</strong> lees de titel en kijk naar de prenten. Waarover zal het gaan?<br>"
                      "<strong>Tijdens het lezen:</strong> wie doet mee? Waar en wanneer? Wat gebeurt er?<br>"
                      "<strong>Na het lezen:</strong> vertel in twee zinnen waarover het ging."),
        ]),
        dict(kop="Tussen de regels lezen", blokken=[
            ("p", "Niet alles staat letterlijk in de tekst. 'Lotte springt een gat in de lucht' betekent dat Lotte heel blij is. "
                  "'Wolk lag te zuchten bij de deur' vertelt dat de hond zich verveelde, ook al staat dat er niet."),
        ]),
        dict(kop="Een woord dat je niet kent", blokken=[
            ("p", "Lees de zin ervoor en erna. 'Na de lange wandeling was Mila <strong>uitgeput</strong>.' Na een lange wandeling ben je moe, dus uitgeput betekent heel moe."),
            ("weetje", "Lukt het niet? Zoek het woord op in een woordenboek of vraag het aan iemand."),
        ]),
        dict(kop="Woorden die bij elkaar horen", blokken=[
            ("fig", tabel(["", "Uitleg", "Voorbeelden"], [["synoniemen", "betekenen hetzelfde", "snel – vlug, mooi – prachtig, beginnen – starten"],
                ["tegenstellingen", "betekenen het omgekeerde", "groot – klein, open – dicht, vroeg – laat"],
                ["samenstellingen", "twee woorden aan elkaar", "tand + borstel = tandborstel, regen + jas = regenjas"],
                ["uitdrukkingen", "betekenen iets anders dan je denkt", "twee linkerhanden hebben = niet handig zijn"]], "100%")),
        ]),
    ],
    onthoud=["Lees eerst de titel.", "Vraag je af: wie, wat, waar, wanneer?", "Moeilijk woord: lees de zinnen errond.",
             "Synoniem = hetzelfde. Tegenstelling = het omgekeerde.", "Samenstelling: twee woorden worden één."]),
    dict(vak="Nederlands", niveau=READY, titel="Lezen en woordenschat", onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE, reeksen=[
        dict(kop="Lees de tekst", oefeningen=[
            ("tekst", TEKST_OEF),
            ("open", "Hoe heet de hond van meneer Tijs?", "Wolk", 1),
            ("open", "Wat doet Yara met Wolk in het park?", "Ze gooit een tak en Wolk brengt hem terug.", 2),
            ("waar", "Meneer Tijs woont al jaren naast Yara.", False),
            ("waar", "Op woensdag gingen ze niet naar het park.", True),
            ("open", "'Wolk lag de hele middag te zuchten bij de deur.' Hoe voelde Wolk zich, denk je? Waarom?", "Hij verveelde zich of was teleurgesteld, want hij wou naar buiten.", 2),
            ("open", "Bedenk een andere titel voor de tekst.", "eigen titel, bv. Wandelen met Wolk", 1),
        ]),
        dict(kop="Synoniemen", opdracht="Schrijf een woord dat hetzelfde betekent.", oefeningen=[
            ("rij", [("blij", "vrolijk"), ("snel", "vlug"), ("starten", "beginnen"), ("dapper", "moedig")], "", B),
        ]),
        dict(kop="Tegenstellingen", opdracht="Schrijf het omgekeerde.", oefeningen=[
            ("rij", [("warm", "koud"), ("vol", "leeg"), ("hoog", "laag"), ("winnen", "verliezen")], "", B),
        ]),
        dict(kop="Samenstellingen", opdracht="Plak de twee woorden aan elkaar.", oefeningen=[
            ("rij", [("voet + bal", "voetbal"), ("brood + doos", "brooddoos"), ("sneeuw + man", "sneeuwman"), ("school + tas", "schooltas")], "", B),
        ]),
        dict(kop="Welk woord past niet?", opdracht="Streep het woord door dat niet bij de groep past.", oefeningen=[
            ("invulwoord", [("hamer – zaag – lepel – tang", "lepel"), ("rood – blauw – stoel – groen", "stoel"),
                            ("hond – kat – konijn – tafel", "tafel"), ("lopen – springen – zacht – zwemmen", "zacht")], ""),
        ]),
        dict(kop="Uitdrukkingen", oefeningen=[
            ("rij", [("zo stil als een muis", "heel stil"), ("een gat in de lucht springen", "heel blij zijn"), ("twee linkerhanden hebben", "niet handig zijn")], "Wat betekent het?", "160px"),
        ]),
    ]))

# ---------------------------------------------------------------- taal en verhalen
H["taal"] = ("taal-en-verhalen-ready", dict(
    vak="Nederlands", niveau=READY, titel="Taal en verhalen",
    onder="Hoe een verhaal in elkaar zit, soorten teksten, een brief of uitnodiging schrijven, luisteren en spreken, alfabetische volgorde.",
    secties=[
        dict(kop="Hoe zit een verhaal in elkaar?", blokken=[
            ("fig", tabel(["Deel", "Wat lees je?", "Voorbeeld"], [["begin", "wie, waar en wanneer", "Op een koude winterdag liep Bas door het bos."],
                ["midden", "er gebeurt iets, vaak een probleem", "Plots hoorde hij een hondje janken."],
                ["slot", "hoe het afloopt", "Bas bracht het hondje veilig naar huis."]], "100%")),
            ("p", "De mensen of dieren in een verhaal heten <strong>personages</strong>. Het belangrijkste is het <strong>hoofdpersonage</strong>."),
            ("p", "De <strong>schrijver</strong> bedenkt het verhaal, de <strong>illustrator</strong> maakt de prenten."),
        ]),
        dict(kop="Soorten teksten", blokken=[
            ("fig", tabel(["Tekst", "Waarvoor?"], [["verhaal, sprookje, fabel", "om van te genieten"], ["recept, handleiding", "om te leren hoe je iets doet"],
                ["krantenbericht, informatieve tekst", "om iets te weten te komen"], ["brief, uitnodiging, bericht", "om iets te vragen of te vertellen aan iemand"],
                ["gedicht", "om met woorden te spelen, soms met rijm"]], "100%")),
        ]),
        dict(kop="Een brief of uitnodiging schrijven", blokken=[
            ("kader", "Hasselt, 3 mei<br><br>Lieve oma,<br><br>Ik wil je uitnodigen voor mijn verjaardagsfeest op zaterdag 10 mei om 14 uur, bij ons thuis.<br>"
                      "We gaan pannenkoeken bakken. Kom je ook?<br><br>Dikke kus,<br>Jonas"),
            ("p", "Bovenaan: plaats en datum. Dan de aanspreking. Dan je bericht. Onderaan een groet en je naam. Op een uitnodiging staat zeker <strong>wat, wanneer en waar</strong>."),
        ]),
        dict(kop="Luisteren en spreken", blokken=[
            ("p", "Goed luisteren: kijk de ander aan, laat die uitspreken en stel daarna een vraag. Iets vertellen: spreek rustig en duidelijk, en begin met waar en wanneer."),
        ]),
        dict(kop="Alfabetische volgorde", blokken=[
            ("p", "a b c d e f g h i j k l m n o p q r s t u v w x y z"),
            ("p", "Beginnen twee woorden met dezelfde letter, kijk dan naar de tweede letter: <strong>bal</strong> komt voor <strong>bed</strong>, want a komt voor e."),
        ]),
    ],
    onthoud=["Verhaal: begin (wie, waar, wanneer), midden (probleem), slot (afloop).", "Elke tekst heeft een doel.",
             "Brief: plaats en datum, aanspreking, bericht, groet en naam.", "Alfabet: kijk naar de eerste letter, dan de tweede."]),
    dict(vak="Nederlands", niveau=READY, titel="Taal en verhalen", onder="{aantal} oefeningen op papier, met een antwoordblad achteraan.", hoe=HOE, reeksen=[
        dict(kop="Begin, midden of slot?", opdracht="Schrijf begin, midden of slot.", oefeningen=[
            ("rij", [("Er was eens een prinses die in een toren woonde.", "begin"), ("En ze leefden nog lang en gelukkig.", "slot"),
                     ("Plots brak er een storm los en het schip begon te zinken.", "midden")], "", B),
        ]),
        dict(kop="Wat voor tekst?", opdracht="Schrijf welke soort tekst het is.", oefeningen=[
            ("rij", [("Neem 200 g bloem en 2 eieren. Meng alles goed.", "recept"), ("Kom naar mijn feest op zaterdag om 14 uur!", "uitnodiging"),
                     ("De vos sprak tegen de raaf: 'Wat zing je mooi!'", "fabel (verhaal)")], "", B),
        ]),
        dict(kop="Rijmen", opdracht="Schrijf een woord dat rijmt.", oefeningen=[
            ("rij", [("muis", "huis"), ("kat", "mat"), ("boom", "droom"), ("ster", "ver")], "", B),
            ("open", "Maak de zin af met een rijmwoord: Er zat een vogel in de boom, hij viel in slaap en had een ...", "droom", 1),
        ]),
        dict(kop="Alfabetische volgorde", oefeningen=[
            ("open", "Zet in alfabetische volgorde: zon – appel – kat – fiets – muis.", "appel – fiets – kat – muis – zon", 1),
            ("open", "Zet in alfabetische volgorde: bus – bal – bos – bed.", "bal – bed – bos – bus", 1),
        ]),
        dict(kop="Juist of fout?", opdracht="Telkens is één zin juist en één fout. Streep de foute zin door.", oefeningen=[
            ("invulwoord", [("De schrijver maakt de prenten. &nbsp; / &nbsp; De illustrator maakt de prenten.", "De illustrator maakt de prenten."),
                            ("Een recept legt uit hoe je iets kookt. &nbsp; / &nbsp; Een recept vertelt een sprookje.", "Een recept legt uit hoe je iets kookt.")], ""),
        ]),
        dict(kop="Schrijf zelf", oefeningen=[
            ("open", "Schrijf een uitnodiging voor een feestje. Vergeet niet: wat, wanneer, waar, een aanspreking, een groet en je naam.", "eigen uitnodiging", 6),
            ("open", "Schrijf een kort verhaal van drie zinnen: één voor het begin, één voor het midden en één voor het slot.", "eigen verhaal", 5),
        ]),
    ]))


if __name__ == "__main__":
    for k in sys.argv[1:] or list(H):
        naam, leer, oefen = H[k]
        maak(naam, "nederlands", leer, oefen)

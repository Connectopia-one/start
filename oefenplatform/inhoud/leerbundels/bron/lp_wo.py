# -*- coding: utf-8 -*-
"""Leer- en oefenbundels bij de Launchpad-hoofdstukken wereldoriëntatie (1ste en 2de
leerjaar). Vakken zoals bij Ready: wetenschap en techniek (lichaam, dieren en planten,
seizoenen), aardrijkskunde (verkeer) en geschiedenis (vroeger en nu, samenleven).
De vragen op het scherm staan in ../../launchpad/bron/wo_*.py.

    python3 lp_wo.py            # alles
    python3 lp_wo.py lichaam    # één hoofdstuk
"""
import sys
from lp_gemeen import maak, tabel, LP, HOE, ON
from ready_wo import plant

B = "130px"
H = {}


def L(vak, titel, onder, secties, onthoud):
    return dict(vak=vak, niveau=LP, titel=titel, onder=onder, secties=secties, onthoud=onthoud)


def O(vak, titel, reeksen):
    return dict(vak=vak, niveau=LP, titel=titel, onder=ON, hoe=HOE, reeksen=reeksen)


WT, AK, GS = "Wetenschap en techniek", "Aardrijkskunde", "Geschiedenis"

H["lichaam"] = ("mijn-lichaam-en-gezond-leven-launchpad", "wo-lichaam", "wetenschap-en-techniek", L(WT, "Mijn lichaam en gezond leven", "De delen van je lichaam, je vijf zintuigen en gezond leven.", [
    dict(kop="Vijf zintuigen", blokken=[("fig", tabel(["zien", "horen", "ruiken", "proeven", "voelen"], [["ogen 👀", "oren 👂", "neus 👃", "tong 👅", "huid ✋"]], "100%"))]),
    dict(kop="Mijn lichaam", blokken=[("p", "Hoofd, nek, schouders, armen, ellebogen, handen, buik, benen, knieën, voeten. Aan elke hand en elke voet zitten <strong>5</strong> vingers of tenen.")]),
    dict(kop="Gezond leven", blokken=[("kader", "🍎 groenten en fruit · 💧 water drinken<br>🏃 elke dag bewegen · 😴 op tijd slapen<br>🪥 's morgens en 's avonds poetsen · 🧼 handen wassen")]),
], ["Zien, horen, ruiken, proeven, voelen.", "Gezond eten, bewegen, slapen, poetsen, wassen."]),
    O(WT, "Mijn lichaam en gezond leven", [
        dict(kop="Welk zintuig?", oefeningen=[("rij", [("muziek", "horen"), ("een bloem", "ruiken"), ("een zure citroen", "proeven"), ("een zachte kat", "voelen"), ("een regenboog", "zien")], "", B)]),
        dict(kop="Teken jezelf", oefeningen=[("teken", "Teken jezelf. Schrijf erbij: hoofd, arm, been, voet, hand.", "eigen tekening", 70)]),
        dict(kop="Gezond of niet?", opdracht="Telkens is één keuze gezond. Omcirkel die.", oefeningen=[("invulwoord", [("water &nbsp; / &nbsp; cola", "water"), ("een appel &nbsp; / &nbsp; chips", "een appel"), ("buiten spelen &nbsp; / &nbsp; de hele dag tv", "buiten spelen")], "")]),
        dict(kop="Waar of niet waar?", oefeningen=[("waar", "Je poetst je tanden twee keer per dag.", True), ("waar", "Met je oren kan je ruiken.", False)]),
    ]))

H["dieren"] = ("dieren-en-planten-launchpad", "wo-dieren", "wetenschap-en-techniek", L(WT, "Dieren en planten", "Huisdieren, boerderijdieren en wilde dieren, en wat een plant nodig heeft.", [
    dict(kop="Dieren", blokken=[("fig", tabel(["huisdier", "boerderij", "wild"], [["hond, kat, konijn", "koe, kip, schaap, varken", "vos, egel, leeuw"]], "100%")),
        ("fig", tabel(["dier", "jong"], [["koe", "kalf"], ["kip", "kuiken"], ["paard", "veulen"], ["schaap", "lam"]], "40%"))]),
    dict(kop="Planten", blokken=[("fig", plant(), "wortel, stengel, blad en bloem"),
        ("p", "Een plant heeft <strong>water</strong>, <strong>licht</strong> en <strong>lucht</strong> nodig. Uit een zaadje groeit een nieuwe plant.")]),
], ["Huisdier, boerderijdier, wild dier.", "Wortel, stengel, blad, bloem.", "Een plant heeft water en licht nodig."]),
    O(WT, "Dieren en planten", [
        dict(kop="Waar woont het?", oefeningen=[("rij", [("koe", "boerderij"), ("vos", "bos"), ("vis", "water"), ("kat", "thuis")], "", B)]),
        dict(kop="Mama en jong", oefeningen=[("rij", [("koe", "kalf"), ("kip", "kuiken"), ("schaap", "lam"), ("paard", "veulen")], "", B)]),
        dict(kop="De plant", oefeningen=[("fig", [(plant(False), "bloem · blad · stengel · wortel")], "Schrijf bij elk streepje: bloem, blad, stengel of wortel.")]),
        dict(kop="Proef", oefeningen=[("teken", "Leg een boon op nat watten. Teken wat je na een week ziet.", "eigen tekening: worteltje en stengel", 50)]),
        dict(kop="Waar of niet waar?", oefeningen=[("waar", "Een spin heeft 8 poten.", True), ("waar", "Een plant groeit best in het donker.", False)]),
    ]))

H["seizoenen"] = ("seizoenen-en-weer-launchpad", "wo-seizoenen", "wetenschap-en-techniek", L(WT, "Seizoenen en weer", "De vier seizoenen, het weer en wat je aantrekt.", [
    dict(kop="Vier seizoenen", blokken=[("fig", tabel(["lente 🌷", "zomer ☀️", "herfst 🍂", "winter ❄️"], [["bloemen, lammetjes", "warm, lange dagen", "bladeren vallen", "koud, soms sneeuw"]], "100%"))]),
    dict(kop="Het weer", blokken=[("fig", tabel(["weer", "wat neem je mee?"], [["regen", "paraplu, laarzen"], ["zon", "pet, zonnecrème"], ["sneeuw", "muts, handschoenen"], ["wind", "een vlieger!"]], "70%")),
        ("weetje", "Een thermometer meet hoe warm het is.")]),
], ["Lente, zomer, herfst, winter.", "Kleed je naar het weer."]),
    O(WT, "Seizoenen en weer", [
        dict(kop="Welk seizoen?", oefeningen=[("rij", [("de bladeren vallen", "herfst"), ("sneeuwpret", "winter"), ("de eerste bloemen", "lente"), ("zomervakantie", "zomer")], "", B)]),
        dict(kop="Wat trek je aan?", oefeningen=[("rij", [("het regent", "regenjas, laarzen"), ("het sneeuwt", "muts, handschoenen"), ("de zon schijnt", "pet, T-shirt")], "", "170px")]),
        dict(kop="Mijn weerweek", oefeningen=[("tabel", ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag"], [[None, None, None, None, None]], "eigen weer (teken een zon, wolk of regen)", "70px")]),
        dict(kop="Teken", oefeningen=[("teken", "Teken een boom in jouw lievelingsseizoen.", "eigen tekening", 55)]),
    ]))

H["verkeer"] = ("verkeer-en-veilig-zijn-launchpad", "wo-verkeer", "aardrijkskunde", L(AK, "Verkeer en veilig zijn", "Veilig stappen en oversteken, in de auto en op de fiets, en veilig thuis.", [
    dict(kop="Veilig oversteken", blokken=[("kader", "1. Stop aan de rand van het voetpad.<br>2. Kijk links, rechts en nog eens links.<br>3. Steek recht over, op het zebrapad."),
        ("fig", tabel(["rood", "groen"], [["wachten", "kijken en oversteken"]], "40%"))]),
    dict(kop="Gezien worden", blokken=[("p", "Een <strong>fluohesje</strong> en lichtjes op je fiets zorgen dat chauffeurs je zien. Op de fiets draag je een <strong>helm</strong>. In de auto doe je je <strong>gordel</strong> om.")]),
    dict(kop="Veilig thuis", blokken=[("kader", "🔥 kookplaat en lucifers: niet aankomen<br>💊 medicijnen en poetsmiddel: geef ze aan een volwassene<br>☎️ noodnummer: 112")]),
], ["Links, rechts, links.", "Fluohesje, helm, gordel.", "Noodnummer 112."]),
    O(AK, "Verkeer en veilig zijn", [
        dict(kop="Wat doe je?", oefeningen=[("rij", [("het voetgangerslicht is rood", "wachten"), ("je stapt in de auto", "gordel om"), ("je gaat fietsen", "helm op")], "", B)]),
        dict(kop="Veilig of gevaarlijk?", opdracht="Omcirkel wat veilig is.", oefeningen=[("invulwoord", [("oversteken op het zebrapad &nbsp; / &nbsp; tussen auto's", "op het zebrapad"), ("spelen in de tuin &nbsp; / &nbsp; spelen op straat", "in de tuin")], "")]),
        dict(kop="Kleur", oefeningen=[("teken", "Teken een verkeerslicht en kleur rood, oranje en groen op de goede plaats.", "rood boven, oranje midden, groen onder", 55)]),
        dict(kop="Noodnummer", oefeningen=[("kort", "Welk nummer bel je bij brand?", "112", "90px")]),
    ]))

H["vroeger"] = ("vroeger-en-nu-launchpad", "wo-vroeger", "geschiedenis", L(GS, "Vroeger en nu", "Zo word je ouder, en hoe leefden opa en oma toen ze klein waren?", [
    dict(kop="Ouder worden", blokken=[("kader", "baby → kleuter → kind → tiener → volwassene → opa of oma"),
        ("p", "Vroeger is voorbij. Nu is vandaag. Later moet nog komen.")]),
    dict(kop="Vroeger en nu", blokken=[("fig", tabel(["vroeger", "nu"], [["kaars", "lamp"], ["telefoon met draad", "gsm"], ["paard en kar", "auto"], ["lei en griffel", "schrift en tablet"]], "70%"))]),
], ["Baby, kind, volwassene.", "Vroeger, nu, later.", "Vraag aan opa en oma hoe het vroeger was."]),
    O(GS, "Vroeger en nu", [
        dict(kop="In volgorde", opdracht="Schrijf 1, 2, 3.", oefeningen=[("rij", [("kind", "2"), ("baby", "1"), ("opa", "3")], "", "60px"), ("rij", [("gsm", "3"), ("kaars", "1"), ("gloeilamp", "2")], "", "60px")]),
        dict(kop="Vroeger of nu?", oefeningen=[("rij", [("tablet", "nu"), ("paard en kar", "vroeger"), ("lei en griffel", "vroeger"), ("gsm", "nu")], "", B)]),
        dict(kop="Vraag het aan opa of oma", oefeningen=[("open", "Met welk speelgoed speelde opa of oma als kind?", "eigen antwoord", 2)]),
        dict(kop="Teken", oefeningen=[("teken", "Teken jezelf als baby en zoals je nu bent.", "eigen tekening", 55)]),
    ]))

H["samen"] = ("ik-en-de-anderen-launchpad", "wo-samen", "geschiedenis", L(GS, "Ik en de anderen", "Gevoelens, familie en vrienden, samen in de klas en samen feest vieren.", [
    dict(kop="Gevoelens", blokken=[("p", "Iedereen is soms blij, verdrietig, boos of bang. Dat mag. Praat erover met iemand die je vertrouwt.")]),
    dict(kop="Familie", blokken=[("fig", tabel(["wie?", "is"], [["mama van mama", "oma"], ["broer van papa", "oom"], ["zus van mama", "tante"]], "50%")),
        ("p", "Elke familie is anders: groot of klein, met één of twee ouders.")]),
    dict(kop="Samen", blokken=[("kader", "✋ vinger opsteken · ⏳ om de beurt · 🧹 samen opruimen<br>🙏 alsjeblieft en dank je wel · 🛑 pesten? zeg het aan de juf"),
        ("fig", tabel(["feest", "wanneer"], [["Sinterklaas", "6 december"], ["Kerstmis", "25 december"], ["Pasen", "lente"], ["Suikerfeest", "na de ramadan"]], "60%"))]),
], ["Alle gevoelens mogen.", "Elke familie is anders.", "Om de beurt, samen opruimen, niet pesten."]),
    O(GS, "Ik en de anderen", [
        dict(kop="Hoe voel je je?", oefeningen=[("rij", [("je krijgt een cadeau", "blij"), ("je knuffel is kwijt", "verdrietig"), ("het onweert", "bang"), ("iemand pakt je bal af", "boos")], "", B)]),
        dict(kop="Mijn familie", oefeningen=[("teken", "Teken je familie. Schrijf bij elk de naam.", "eigen tekening", 60)]),
        dict(kop="Wat zeg je?", oefeningen=[("rij", [("iemand helpt je", "dank je wel"), ("je wil iets vragen", "alsjeblieft"), ("je deed iemand pijn", "sorry")], "", B)]),
        dict(kop="Feesten", oefeningen=[("open", "Welk feest vier jij graag? Wat doe je dan?", "eigen antwoord", 2)]),
    ]))


if __name__ == "__main__":
    for k in sys.argv[1:] or list(H):
        naam, module, vakmap, leer, oefen = H[k]
        maak(naam, vakmap, leer, oefen, module.replace("-", "_"), grote_figuren=True)

# -*- coding: utf-8 -*-
"""Zet de wisselende woorden bij de spellingvragen van 🌱 Start.

Zie lib/spellingvariant.ts. Met de hand geschreven en nagelezen, nooit door een
taalmodel bedacht: de welkomstbrief aan de testgezinnen belooft uitdrukkelijk
geen AI in de oefeningen.

De sleutel is het volgnummer van de vraag in het hoofdstuk, want "Welke zin is
juist?" staat er zeven keer.
"""
import json
import pathlib

BESTAND = pathlib.Path(__file__).resolve().parents[0]


def mv_lang(woord, meervoud, fout1, fout2):
    return dict(
        vraag=f"Wat is het meervoud van '{woord}'?",
        opties=[meervoud, fout1, fout2],
        antwoord=0,
        uitleg=f"{meervoud[:2]}-{meervoud[2:]}: de eerste lettergreep eindigt op een klinker, dus ze is open. Dan één medeklinker.",
    )


VARIANTEN = {
    1: [
        dict(vraag="Wat is het meervoud van 'boom'?", opties=["bomen", "bommen", "boomen"], antwoord=0,
             uitleg="Bo-men: de eerste lettergreep eindigt op een klinker, dus ze is open. Dan één m."),
        dict(vraag="Wat is het meervoud van 'peer'?", opties=["peren", "perren", "peeren"], antwoord=0,
             uitleg="Pe-ren: de eerste lettergreep eindigt op een klinker, dus ze is open. Dan één r."),
        dict(vraag="Wat is het meervoud van 'muur'?", opties=["muren", "murren", "muuren"], antwoord=0,
             uitleg="Mu-ren: de eerste lettergreep eindigt op een klinker, dus ze is open. Dan één r."),
        dict(vraag="Wat is het meervoud van 'vuur'?", opties=["vuren", "vurren", "vuuren"], antwoord=0,
             uitleg="Vu-ren: de eerste lettergreep eindigt op een klinker, dus ze is open. Dan één r."),
    ],
    2: [
        dict(vraag="Wat is het meervoud van 'man'?", opties=["manen", "mannen", "mannenen"], antwoord=1,
             uitleg="Man-nen: de korte a moet kort blijven, dus verdubbelt de n. 'Manen' hoort bij maan."),
        dict(vraag="Wat is het meervoud van 'kat'?", opties=["katen", "katten", "kattenen"], antwoord=1,
             uitleg="Kat-ten: de korte a moet kort blijven, dus verdubbelt de t."),
        dict(vraag="Wat is het meervoud van 'bus'?", opties=["busen", "bussen", "bussenen"], antwoord=1,
             uitleg="Bus-sen: de korte u moet kort blijven, dus verdubbelt de s."),
        dict(vraag="Wat is het meervoud van 'vis'?", opties=["visen", "vissen", "vissenen"], antwoord=1,
             uitleg="Vis-sen: de korte i moet kort blijven, dus verdubbelt de s."),
    ],
    3: [
        dict(vraag="Het meervoud van 'zon' is ___.", antwoord="zonnen",
             uitleg="Zon-nen: de korte o moet kort blijven, dus verdubbelt de n."),
        dict(vraag="Het meervoud van 'kar' is ___.", antwoord="karren",
             uitleg="Kar-ren: de korte a moet kort blijven, dus verdubbelt de r."),
        dict(vraag="Het meervoud van 'pop' is ___.", antwoord="poppen",
             uitleg="Pop-pen: de korte o moet kort blijven, dus verdubbelt de p."),
        dict(vraag="Het meervoud van 'ton' is ___.", antwoord="tonnen",
             uitleg="Ton-nen: de korte o moet kort blijven, dus verdubbelt de n."),
    ],
    4: [
        dict(vraag="Het meervoud van 'maan' is ___.", antwoord="manen",
             uitleg="Ma-nen: de eerste lettergreep is open, dus valt er één a weg."),
        dict(vraag="Het meervoud van 'paal' is ___.", antwoord="palen",
             uitleg="Pa-len: de eerste lettergreep is open, dus valt er één a weg."),
        dict(vraag="Het meervoud van 'veer' is ___.", antwoord="veren",
             uitleg="Ve-ren: de eerste lettergreep is open, dus valt er één e weg."),
        dict(vraag="Het meervoud van 'zaal' is ___.", antwoord="zalen",
             uitleg="Za-len: de eerste lettergreep is open, dus valt er één a weg."),
    ],
    5: [
        dict(vraag="In 'bo-men' is de eerste lettergreep open.", antwoord=True,
             uitleg="Bo eindigt op een klinker, dus de lettergreep is open. Daarom blijft de o lang met één o."),
        dict(vraag="In 'pe-ren' is de eerste lettergreep open.", antwoord=True,
             uitleg="Pe eindigt op een klinker, dus de lettergreep is open. Daarom blijft de e lang met één e."),
        dict(vraag="In 'kat-ten' is de eerste lettergreep open.", antwoord=False,
             uitleg="Kat eindigt op een medeklinker, dus de lettergreep is gesloten. Daarom verdubbelt de t."),
        dict(vraag="In 'man-nen' is de eerste lettergreep open.", antwoord=False,
             uitleg="Man eindigt op een medeklinker, dus de lettergreep is gesloten. Daarom verdubbelt de n."),
    ],
    7: [
        dict(vraag="Wat is het meervoud van 'rok'?", opties=["roken", "rokken", "rooken"], antwoord=1,
             uitleg="Rok-ken: de korte o moet kort blijven, dus verdubbelt de k. 'Roken' is iets anders."),
        dict(vraag="Wat is het meervoud van 'kip'?", opties=["kipen", "kippen", "kiepen"], antwoord=1,
             uitleg="Kip-pen: de korte i moet kort blijven, dus verdubbelt de p."),
        dict(vraag="Wat is het meervoud van 'pan'?", opties=["panen", "pannen", "paanen"], antwoord=1,
             uitleg="Pan-nen: de korte a moet kort blijven, dus verdubbelt de n."),
        dict(vraag="Wat is het meervoud van 'stap'?", opties=["stapen", "stappen", "staapen"], antwoord=1,
             uitleg="Stap-pen: de korte a moet kort blijven, dus verdubbelt de p."),
    ],
    8: [
        dict(vraag="De stam van 'fietsen' is ___.", antwoord="fiets", uitleg="Fietsen min -en geeft fiets."),
        dict(vraag="De stam van 'spelen' is ___.", antwoord="speel",
             uitleg="Spelen min -en geeft spel, maar de e moet lang blijven in een gesloten lettergreep, dus speel."),
        dict(vraag="De stam van 'bakken' is ___.", antwoord="bak",
             uitleg="Bakken min -en geeft bakk, en dubbele medeklinkers schrijf je niet op het eind: bak."),
        dict(vraag="De stam van 'zingen' is ___.", antwoord="zing", uitleg="Zingen min -en geeft zing."),
    ],
    9: [
        dict(vraag="De stam van 'horen' is ___.", antwoord="hoor",
             uitleg="Horen min -en geeft hor, maar de o moet lang blijven in een gesloten lettergreep, dus hoor."),
        dict(vraag="De stam van 'bouwen' is ___.", antwoord="bouw", uitleg="Bouwen min -en geeft bouw."),
        dict(vraag="De stam van 'delen' is ___.", antwoord="deel",
             uitleg="Delen min -en geeft del, maar de e moet lang blijven in een gesloten lettergreep, dus deel."),
        dict(vraag="De stam van 'leren' is ___.", antwoord="leer",
             uitleg="Leren min -en geeft ler, maar de e moet lang blijven in een gesloten lettergreep, dus leer."),
    ],
    10: [
        dict(vraag="Wat is de stam van 'lezen'?", opties=["lez", "lees", "leze"], antwoord=1,
             uitleg="Lezen min -en geeft lez. De e moet lang blijven in een gesloten lettergreep, dus lees."),
        dict(vraag="Wat is de stam van 'weten'?", opties=["wet", "weet", "wete"], antwoord=1,
             uitleg="Weten min -en geeft wet. De e moet lang blijven in een gesloten lettergreep, dus weet."),
        dict(vraag="Wat is de stam van 'nemen'?", opties=["nem", "neem", "neme"], antwoord=1,
             uitleg="Nemen min -en geeft nem. De e moet lang blijven in een gesloten lettergreep, dus neem."),
        dict(vraag="Wat is de stam van 'komen'?", opties=["kom", "koom", "kome"], antwoord=0,
             uitleg="Komen min -en geeft kom. Hier hoor je een korte o, dus er komt geen tweede o bij."),
    ],
    12: [
        dict(vraag="Vul in: ik ___ (spelen).", antwoord="speel", uitleg="Bij ik schrijf je gewoon de stam: speel."),
        dict(vraag="Vul in: ik ___ (horen).", antwoord="hoor", uitleg="Bij ik schrijf je gewoon de stam: hoor."),
        dict(vraag="Vul in: ik ___ (zingen).", antwoord="zing", uitleg="Bij ik schrijf je gewoon de stam: zing."),
        dict(vraag="Vul in: ik ___ (kopen).", antwoord="koop", uitleg="Bij ik schrijf je gewoon de stam: koop."),
    ],
    13: [
        dict(vraag="Welke zin is juist?", opties=["Hij vindt het leuk.", "Hij vind het leuk.", "Hij vint het leuk."], antwoord=0,
             uitleg="De stam is vind, en bij hij komt er een -t bij: vindt. Dat je het niet hoort, maakt niets uit."),
        dict(vraag="Welke zin is juist?", opties=["Hij houdt van zwemmen.", "Hij houd van zwemmen.", "Hij hout van zwemmen."], antwoord=0,
             uitleg="De stam is houd, en bij hij komt er een -t bij: houdt. 'Hout' is een ander woord."),
        dict(vraag="Welke zin is juist?", opties=["Zij rijdt heel voorzichtig.", "Zij rijd heel voorzichtig.", "Zij rijt heel voorzichtig."], antwoord=0,
             uitleg="De stam is rijd, en bij zij komt er een -t bij: rijdt."),
    ],
    14: [
        dict(vraag="Welke zin is juist?", opties=["Vind jij dat leuk?", "Vindt jij dat leuk?", "Vint jij dat leuk?"], antwoord=0,
             uitleg="Staat 'jij' áchter het werkwoord, dan valt de -t weg: vind jij."),
        dict(vraag="Welke zin is juist?", opties=["Houd jij van zwemmen?", "Houdt jij van zwemmen?", "Hout jij van zwemmen?"], antwoord=0,
             uitleg="Staat 'jij' áchter het werkwoord, dan valt de -t weg: houd jij."),
        dict(vraag="Welke zin is juist?", opties=["Rijd jij mee naar school?", "Rijdt jij mee naar school?", "Rijt jij mee naar school?"], antwoord=0,
             uitleg="Staat 'jij' áchter het werkwoord, dan valt de -t weg: rijd jij."),
    ],
    15: [
        dict(vraag="Welke zin is juist?", opties=["Ik wordt groot.", "Ik word groot.", "Ik wort groot."], antwoord=1,
             uitleg="Bij ik schrijf je de stam zonder -t: word."),
        dict(vraag="Welke zin is juist?", opties=["Ik houdt van muziek.", "Ik houd van muziek.", "Ik hout van muziek."], antwoord=1,
             uitleg="Bij ik schrijf je de stam zonder -t: houd."),
        dict(vraag="Welke zin is juist?", opties=["Ik rijdt met de bus.", "Ik rijd met de bus.", "Ik rijt met de bus."], antwoord=1,
             uitleg="Bij ik schrijf je de stam zonder -t: rijd."),
    ],
    16: [
        dict(vraag="Welke zin is juist?", opties=["Het licht brand nog.", "Het licht brandt nog.", "Het licht brant nog."], antwoord=1,
             uitleg="De stam is brand, en bij het komt er een -t bij: brandt."),
        dict(vraag="Welke zin is juist?", opties=["Zij red de hond.", "Zij redt de hond.", "Zij ret de hond."], antwoord=1,
             uitleg="De stam van redden is red, en bij zij komt er een -t bij: redt. Niet 'reddt'."),
        dict(vraag="Welke zin is juist?", opties=["Hij bind zijn veters.", "Hij bindt zijn veters.", "Hij bint zijn veters."], antwoord=1,
             uitleg="De stam is bind, en bij hij komt er een -t bij: bindt."),
    ],
    17: [
        dict(vraag="In 'Wat vind jij ervan?' hoort er een t achter vind.", antwoord=False,
             uitleg="'Jij' staat áchter het werkwoord, dus valt de -t weg. Vóór het werkwoord zou het 'jij vindt' zijn."),
        dict(vraag="In 'Waar rijd jij naartoe?' hoort er een t achter rijd.", antwoord=False,
             uitleg="'Jij' staat áchter het werkwoord, dus valt de -t weg. Vóór het werkwoord zou het 'jij rijdt' zijn."),
        dict(vraag="In 'Jij wordt later groot.' hoort er een t achter word.", antwoord=True,
             uitleg="Hier staat 'jij' vóór het werkwoord, dus blijft de -t staan: jij wordt."),
    ],
    18: [
        dict(vraag="Vul in: jij ___ (vinden) dat leuk.", antwoord="vindt",
             uitleg="'Jij' staat vóór het werkwoord, dus komt er een -t bij de stam: vindt."),
        dict(vraag="Vul in: jij ___ (houden) van zwemmen.", antwoord="houdt",
             uitleg="'Jij' staat vóór het werkwoord, dus komt er een -t bij de stam: houdt."),
        dict(vraag="Vul in: jij ___ (rijden) snel.", antwoord="rijdt",
             uitleg="'Jij' staat vóór het werkwoord, dus komt er een -t bij de stam: rijdt."),
    ],
    19: [
        dict(vraag="Vul in: ik ___ (worden) moe.", antwoord="word", uitleg="Bij ik schrijf je de stam zonder -t: word."),
        dict(vraag="Vul in: ik ___ (houden) van muziek.", antwoord="houd", uitleg="Bij ik schrijf je de stam zonder -t: houd."),
        dict(vraag="Vul in: ik ___ (rijden) met de fiets.", antwoord="rijd", uitleg="Bij ik schrijf je de stam zonder -t: rijd."),
    ],
    21: [
        dict(vraag="Welke zin is juist?", opties=["De kat miauwt.", "De kat miauwd.", "De kat miauw."], antwoord=0,
             uitleg="De stam is miauw, en bij de kat komt er een -t bij: miauwt."),
        dict(vraag="Welke zin is juist?", opties=["De haan kraait.", "De haan kraaid.", "De haan kraai."], antwoord=0,
             uitleg="De stam is kraai, en bij de haan komt er een -t bij: kraait."),
        dict(vraag="Welke zin is juist?", opties=["De koe loeit.", "De koe loeid.", "De koe loei."], antwoord=0,
             uitleg="De stam is loei, en bij de koe komt er een -t bij: loeit."),
    ],
    22: [
        dict(vraag="Wat is de verleden tijd van 'koken'?", opties=["ik kookte", "ik kookde", "ik kooktte"], antwoord=0,
             uitleg="De stam kook eindigt op een k, en die zit in 't kofschip. Dus -te."),
        dict(vraag="Wat is de verleden tijd van 'stappen'?", opties=["ik stapte", "ik stapde", "ik staptte"], antwoord=0,
             uitleg="De stam stap eindigt op een p, en die zit in 't kofschip. Dus -te."),
        dict(vraag="Wat is de verleden tijd van 'blaffen'?", opties=["ik blafte", "ik blafde", "ik blaftte"], antwoord=0,
             uitleg="De stam blaf eindigt op een f, en die zit in 't kofschip. Dus -te."),
        dict(vraag="Wat is de verleden tijd van 'lachen'?", opties=["ik lachte", "ik lachde", "ik lachtte"], antwoord=0,
             uitleg="De stam lach eindigt op ch, en die zit in 't kofschip. Dus -te."),
    ],
    23: [
        dict(vraag="Wat is de verleden tijd van 'spelen'?", opties=["ik speelte", "ik speelde", "ik speeldde"], antwoord=1,
             uitleg="De stam speel eindigt op een l, en die zit niet in 't kofschip. Dus -de."),
        dict(vraag="Wat is de verleden tijd van 'horen'?", opties=["ik hoorte", "ik hoorde", "ik hoordde"], antwoord=1,
             uitleg="De stam hoor eindigt op een r, en die zit niet in 't kofschip. Dus -de."),
        dict(vraag="Wat is de verleden tijd van 'delen'?", opties=["ik deelte", "ik deelde", "ik deeldde"], antwoord=1,
             uitleg="De stam deel eindigt op een l, en die zit niet in 't kofschip. Dus -de."),
    ],
    24: [
        dict(vraag="De verleden tijd van 'werken' is: ik ___.", antwoord="werkte",
             uitleg="De stam werk eindigt op een k, en die zit in 't kofschip. Dus -te."),
        dict(vraag="De verleden tijd van 'plukken' is: ik ___.", antwoord="plukte",
             uitleg="De stam pluk eindigt op een k, en die zit in 't kofschip. Dus -te."),
        dict(vraag="De verleden tijd van 'wassen' is: ik ___.", antwoord="waste",
             uitleg="De stam was eindigt op een s, en die zit in 't kofschip. Dus -te."),
    ],
    25: [
        dict(vraag="De verleden tijd van 'leren' is: ik ___.", antwoord="leerde",
             uitleg="De stam leer eindigt op een r, en die zit niet in 't kofschip. Dus -de."),
        dict(vraag="De verleden tijd van 'spelen' is: ik ___.", antwoord="speelde",
             uitleg="De stam speel eindigt op een l, en die zit niet in 't kofschip. Dus -de."),
        dict(vraag="De verleden tijd van 'wonen' is: ik ___.", antwoord="woonde",
             uitleg="De stam woon eindigt op een n, en die zit niet in 't kofschip. Dus -de."),
    ],
    27: [
        dict(vraag="Wat is de verleden tijd van 'reizen'?", opties=["ik reisde", "ik reiste", "ik reizde"], antwoord=0,
             uitleg="De z wordt een s in de stam, maar de klank hoort niet bij 't kofschip, dus -de: reisde."),
        dict(vraag="Wat is de verleden tijd van 'razen'?", opties=["ik raasde", "ik raaste", "ik raazde"], antwoord=0,
             uitleg="De z wordt een s in de stam, maar de klank hoort niet bij 't kofschip, dus -de: raasde."),
        dict(vraag="Wat is de verleden tijd van 'blozen'?", opties=["ik bloosde", "ik blooste", "ik bloozde"], antwoord=0,
             uitleg="De z wordt een s in de stam, maar de klank hoort niet bij 't kofschip, dus -de: bloosde."),
    ],
    30: [
        dict(vraag="Ik heb gisteren lang ___.", opties=["gefietst", "gefietsd", "gefietstt"], antwoord=0,
             uitleg="De stam fiets eindigt op een s uit 't kofschip, dus het voltooid deelwoord krijgt een t."),
        dict(vraag="Ik heb gisteren hard ___.", opties=["gelachen", "gelacht", "gelachd"], antwoord=0,
             uitleg="Lachen is een sterk werkwoord: het deelwoord is gelachen, niet gelacht."),
        dict(vraag="Ik heb hem gisteren ___.", opties=["geholpen", "gehelpt", "geholpt"], antwoord=0,
             uitleg="Helpen is een sterk werkwoord: het deelwoord is geholpen, met een andere klinker."),
    ],
    31: [
        dict(vraag="Zij heeft haar kamer goed ___.", opties=["gekuist", "gekuisd", "gekuistd"], antwoord=0,
             uitleg="De stam kuis eindigt op een s uit 't kofschip, dus een t."),
        dict(vraag="Hij heeft het huis zelf ___.", opties=["gebouwt", "gebouwd", "gebouwtd"], antwoord=1,
             uitleg="De stam bouw eindigt op een w, die niet in 't kofschip zit, dus een d."),
        dict(vraag="Wij hebben lang op je ___.", opties=["gewacht", "gewachd", "gewachtd"], antwoord=0,
             uitleg="De stam wacht eindigt al op een t, dus het deelwoord is gewacht."),
    ],
    32: [
        dict(vraag="Ik heb daar lang op ___ (wachten).", antwoord="gewacht",
             uitleg="De stam wacht eindigt al op een t, dus er komt er geen tweede bij."),
        dict(vraag="Wij hebben samen ___ (koken).", antwoord="gekookt",
             uitleg="De stam kook eindigt op een k uit 't kofschip, dus een t."),
        dict(vraag="Zij heeft het huis ___ (bouwen).", antwoord="gebouwd",
             uitleg="De stam bouw eindigt op een w, die niet in 't kofschip zit, dus een d."),
    ],
    36: [
        dict(vraag="Wat is het meervoud van 'auto'?", opties=["auto's", "autos", "autoos"], antwoord=0,
             uitleg="Eindigt een woord op een losse o, dan komt er een apostrof voor de meervouds-s."),
        dict(vraag="Wat is het meervoud van 'paraplu'?", opties=["paraplu's", "paraplus", "parapluus"], antwoord=0,
             uitleg="Eindigt een woord op een losse u, dan komt er een apostrof voor de meervouds-s."),
        dict(vraag="Wat is het meervoud van 'foto'?", opties=["foto's", "fotos", "fotoos"], antwoord=0,
             uitleg="Eindigt een woord op een losse o, dan komt er een apostrof voor de meervouds-s."),
    ],
    37: [
        dict(vraag="Het meervoud van 'stoel' is ___.", antwoord="stoelen",
             uitleg="De meeste Nederlandse woorden krijgen gewoon -en in het meervoud."),
        dict(vraag="Het meervoud van 'boek' is ___.", antwoord="boeken",
             uitleg="De meeste Nederlandse woorden krijgen gewoon -en in het meervoud."),
        dict(vraag="Het meervoud van 'huis' is ___.", antwoord="huizen",
             uitleg="De s van huis wordt een z tussen twee klinkers: hui-zen."),
    ],
    38: [
        dict(vraag="Het meervoud van 'ei' is ___.", antwoord="eieren",
             uitleg="Een paar woorden krijgen -eren in plaats van -en: ei wordt eieren, net als kind, blad en lied."),
        dict(vraag="Het meervoud van 'blad' is ___.", antwoord="bladeren",
             uitleg="Een paar woorden krijgen -eren in plaats van -en: blad wordt bladeren, net als kind, ei en lied."),
        dict(vraag="Het meervoud van 'lied' is ___.", antwoord="liederen",
             uitleg="Een paar woorden krijgen -eren in plaats van -en: lied wordt liederen, net als kind, ei en blad."),
    ],
    39: [
        dict(vraag="Het verkleinwoord van 'raam' is ___.", opties=["raamje", "raampje", "raamtje"], antwoord=1,
             uitleg="Na een lange klinker plus m komt -pje, anders zou je 'raamje' als één klank lezen."),
        dict(vraag="Het verkleinwoord van 'bloem' is ___.", opties=["bloemje", "bloempje", "bloemtje"], antwoord=1,
             uitleg="Na een lange klinker plus m komt -pje."),
        dict(vraag="Het verkleinwoord van 'duim' is ___.", opties=["duimje", "duimpje", "duimtje"], antwoord=1,
             uitleg="Na een tweeklank plus m komt -pje."),
    ],
    40: [
        dict(vraag="Het verkleinwoord van 'deur' is ___.", antwoord="deurtje",
             uitleg="Na een l, n of r komt gewoon -tje."),
        dict(vraag="Het verkleinwoord van 'bal' is ___.", antwoord="balletje",
             uitleg="Na een korte klank plus l verdubbelt de l en komt er -etje bij: balletje."),
        dict(vraag="Het verkleinwoord van 'boom' is ___.", antwoord="boompje",
             uitleg="Na een lange klinker plus m komt -pje: boompje."),
    ],
    42: [
        dict(vraag="Het verkleinwoord van 'ring' is ___.", opties=["ringje", "rinkje", "ringkje"], antwoord=1,
             uitleg="Na -ing met de klemtoon vooraan wordt de g een k: rinkje. Je hoort het ook zo."),
        dict(vraag="Het verkleinwoord van 'woning' is ___.", opties=["woningje", "woninkje", "woningkje"], antwoord=1,
             uitleg="Na -ing met de klemtoon vooraan wordt de g een k: woninkje."),
        dict(vraag="Het verkleinwoord van 'ketting' is ___.", opties=["kettingje", "kettinkje", "kettingkje"], antwoord=1,
             uitleg="Na -ing met de klemtoon vooraan wordt de g een k: kettinkje."),
    ],
    43: [
        dict(vraag="Welk woord is juist gespeld?", opties=["blij", "bley", "bly"], antwoord=0,
             uitleg="De klank ei of ij schrijf je hier met een lange ij. Dat moet je onthouden, horen kan je het niet."),
        dict(vraag="Welk woord is juist gespeld?", opties=["eiland", "ijland", "yland"], antwoord=0,
             uitleg="De klank ei of ij schrijf je hier met een korte ei. Dat moet je onthouden."),
        dict(vraag="Welk woord is juist gespeld?", opties=["wijs", "weis", "wys"], antwoord=0,
             uitleg="De klank ei of ij schrijf je hier met een lange ij. Dat moet je onthouden."),
    ],
    44: [
        dict(vraag="Welk woord is juist gespeld?", opties=["gaud", "goud", "gout"], antwoord=1,
             uitleg="De klank au of ou schrijf je hier met ou. Op het eind hoor je een t maar schrijf je een d, want in 'gouden' hoor je de d."),
        dict(vraag="Welk woord is juist gespeld?", opties=["blaw", "blauw", "blouw"], antwoord=1,
             uitleg="De klank au of ou schrijf je hier met au, en er hoort een w achter: blauw."),
        dict(vraag="Welk woord is juist gespeld?", opties=["vraw", "vrouw", "vrauw"], antwoord=1,
             uitleg="De klank au of ou schrijf je hier met ou, en er hoort een w achter: vrouw."),
    ],
    46: [
        dict(vraag="Hoe schrijf je het?", opties=["boekekast", "boekenkast", "boeken kast"], antwoord=1,
             uitleg="Een samenstelling schrijf je aan elkaar, en tussen de delen staat hier een tussen-n: boekenkast."),
        dict(vraag="Hoe schrijf je het?", opties=["sterrekijker", "sterrenkijker", "sterren kijker"], antwoord=1,
             uitleg="Een samenstelling schrijf je aan elkaar, en tussen de delen staat hier een tussen-n: sterrenkijker."),
        dict(vraag="Hoe schrijf je het?", opties=["kippehok", "kippenhok", "kippen hok"], antwoord=1,
             uitleg="Een samenstelling schrijf je aan elkaar, en tussen de delen staat hier een tussen-n: kippenhok."),
    ],
    47: [
        dict(vraag="Welke zin is juist?", opties=["Sam leert frans op school.", "Sam leert Frans op school."], antwoord=1,
             uitleg="Namen van talen krijgen in het Nederlands een hoofdletter."),
        dict(vraag="Welke zin is juist?", opties=["Wij gaan naar parijs.", "Wij gaan naar Parijs."], antwoord=1,
             uitleg="Namen van steden krijgen een hoofdletter."),
        dict(vraag="Welke zin is juist?", opties=["Zij woont in belgië.", "Zij woont in België."], antwoord=1,
             uitleg="Namen van landen krijgen een hoofdletter."),
    ],
}


def main():
    pad = pathlib.Path(__file__).resolve()
    doel = pathlib.Path("start/nederlands-spelling.json")
    data = json.loads(doel.read_text(encoding="utf-8"))
    hoofdstuk = data["hoofdstukken"][0]
    vragen = hoofdstuk["vragen"]
    for nummer, varianten in VARIANTEN.items():
        vraag = vragen[nummer - 1]
        for n, variant in enumerate(varianten, start=2):
            heel = {**{k: v for k, v in vraag.items() if k != "varianten"}, **variant}
            if heel["type"] == "meerkeuze":
                opties = heel["opties"]
                assert len(opties) == len(set(opties)), (nummer, n, "twee gelijke opties")
                assert isinstance(heel["antwoord"], int) and 0 <= heel["antwoord"] < len(opties), (nummer, n)
            elif heel["type"] == "waarofniet":
                assert isinstance(heel["antwoord"], bool), (nummer, n)
            else:
                assert isinstance(heel["antwoord"], str) and heel["antwoord"].strip(), (nummer, n)
                assert heel.get("opties") is None, (nummer, n, "invulvraag met opties")
            assert heel.get("uitleg"), (nummer, n, "geen uitleg")
        vraag["varianten"] = varianten
    doel.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tot = sum(len(v) for v in VARIANTEN.values())
    print(f"{len(VARIANTEN)} vragen met varianten, {tot} wisselende woorden in {doel}")
    print(pad.name)


if __name__ == "__main__":
    main()

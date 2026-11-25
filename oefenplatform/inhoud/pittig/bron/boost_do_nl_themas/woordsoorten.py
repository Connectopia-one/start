"""De woordsoorten op een rij — pittig (🚀 Boost doorstroom, Nederlands).

Eigen vragen strikt binnen nl_woordsoorten, met een zelfgetekende zin waarin
je op het juiste woord klikt."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, ROOD, BLAUW, GEEL

WZ = Prent("zin-in-blokjes", "Een zin in losse woorden", "twee regels met losse woorden in kaders: Oei, gisteren vond mijn zus drie oude munten onder de kast en ze gaf ze aan iemand")
RIJEN = [["Oei,", "gisteren", "vond", "mijn", "zus"], ["drie", "oude", "munten", "onder", "de", "kast"], ["en", "ze", "toonde", "ze", "aan", "iemand."]]
POS = {}
y = 130
for rij in RIJEN:
    breedtes = [len(w) * 17 + 34 for w in rij]
    x = (1000 - (sum(breedtes) + 12 * (len(rij) - 1))) / 2
    for w, b in zip(rij, breedtes):
        WZ.rect(x, y, b, 70, "#f3f6fb", DONKER, 10, 2)
        WZ.tekst(x + b / 2, y + 46, w, 28)
        POS.setdefault(w.strip(",."), []).append(Prent.zone(x, y, b, 70))
        x += b + 12
    y += 130
U = "zin-in-blokjes.svg"

def z(w, i=0):
    return [POS[w][i]]

VRAGEN = [
    klik("Klik op het tussenwerpsel.", U, z("Oei"), "Een tussenwerpsel drukt een gevoel uit en staat los van de zinsbouw."),
    klik("Klik op een voorzetsel.", U, z("onder") + z("aan"), "Onder en aan geven een verhouding aan."),
    klik("Klik op het bepaalde telwoord.", U, z("drie"), "Drie noemt een precies aantal."),
    klik("Klik op het bijvoeglijk naamwoord.", U, z("oude"), "'Oude' zegt iets over 'munten'."),
    klik("Klik op het voegwoord.", U, z("en"), "'En' verbindt twee zinnen."),
    klik("Klik op het bezittelijk voornaamwoord.", U, z("mijn"), "'Mijn' zegt bij wie de zus hoort."),
    klik("Klik op het onbepaald voornaamwoord.", U, z("iemand"), "Iemand noemt geen bepaalde persoon."),
    klik("Klik op het bijwoord van tijd.", U, z("gisteren"), "Bijwoorden zeggen iets over tijd, plaats, mate of manier."),
    sorteer("Welk soort lidwoord?", ["bepaald", "onbepaald", "ontkennend"],
            [("de", "bepaald"), ("een", "onbepaald"), ("geen", "ontkennend"), ("het", "bepaald")],
            "Geen is de ontkenning van een."),
    tabel("Bijvoeglijk naamwoord of bijwoord?",
          [("snel in 'Hij loopt snel'", "bijwoord"), ("snelle in 'de snelle loper'", "bijvoeglijk naamwoord"), ("gelukkig in 'Gelukkig regende het niet'", "bijwoord"), ("gelukkig in 'een gelukkig kind'", "bijvoeglijk naamwoord")],
          "Zegt het iets over een naamwoord, dan is het bijvoeglijk.", ["bijvoeglijk naamwoord", "bijwoord"]),
    tabel("Klopt dit over woordsoorten?",
          [("'Veel' is een onbepaald telwoord.", J), ("Een bijvoeglijk naamwoord zegt iets over een werkwoord.", F), ("Een tussenwerpsel kan je weglaten zonder dat de zin breekt.", J)],
          "Een woord dat iets over een werkwoord zegt, is een bijwoord."),
    sorteer("'over' in 'Welke woordsoort is het vetgedrukte woord? 'De kat sprong over de muur, maar ze viel bijna.''", ["voorzetsel", "voegwoord", "bijwoord"],
            [("over", "voorzetsel"), ("maar", "voegwoord"), ("bijna", "bijwoord")],
            "Bijna zegt iets over de mate."),
    mk("Je twijfelt tussen 'de gekleurde muur' en 'de muur is gekleurd'. Wat helpt je kiezen?",
       ["de woordsoort", "het aantal lettergrepen", "de hoofdgedachte van de tekst", "het register van de tekst"],
       0, "Of je 'gekleurde' of 'gekleurd' schrijft, hangt af van de woordsoort."),
    sorteer("Welk soort voornaamwoord is het?", ["persoonlijk", "bezittelijk", "aanwijzend", "onbepaald"],
            [("hem", "persoonlijk"), ("jouw", "bezittelijk"), ("deze", "aanwijzend"), ("niemand", "onbepaald"), ("men", "onbepaald"), ("ik", "persoonlijk")],
            "'Men' is onbepaald, geen persoonlijk voornaamwoord."),
    tabel("Welk soort voornaamwoord is het eerste woord tussen aanhalingstekens?",
          [("'zich' in 'Hij wast zich elke ochtend.'", "wederkerend"), ("'elkaar' in 'De zussen helpen elkaar.'", "wederkerig"), ("'dat' in 'Het boek dat ik las, was spannend.'", "betrekkelijk"), ("'Wie' in 'Wie heeft dat gedaan?'", "vragend")],
          "Een betrekkelijk voornaamwoord begint een bijzin.", ["wederkerend", "wederkerig", "betrekkelijk", "vragend"]),
    mk("'Ze wasten zich' en 'Ze wasten elkaar'. Wat is het verschil?",
       ["'zich': elk zichzelf; 'elkaar': over en weer", "er is helemaal geen verschil in betekenis tussen de twee", "'zich' is bezittelijk en 'elkaar' is een aanwijzend woord", "bij 'elkaar' wast er telkens maar één persoon"],
       0, "Wederkerend keert terug naar het onderwerp, wederkerig gaat over en weer."),
    tabel("Zelfstandig of bijvoeglijk gebruikt?",
          [("'Mijn' in 'Mijn fiets staat buiten.'", "bijvoeglijk"), ("'mijne' in 'De mijne staat buiten.'", "zelfstandig"), ("'Die' in 'Die van mij is groter.'", "zelfstandig"), ("'Dat' in 'Dat huis is te koop.'", "bijvoeglijk")],
          "Bijvoeglijk staat het voor een naamwoord, zelfstandig vervangt het een naamwoord.", ["zelfstandig", "bijvoeglijk"]),
    mk("Waarom schrijf je 'Ik zag hem' en niet 'Ik zag hij'?",
       ["het is hier geen onderwerp", "'hij' is een bezittelijk voornaamwoord", "'hem' is altijd een stuk beleefder dan 'hij'", "na 'zag' komt altijd eerst een lidwoord"],
       0, "Persoonlijke voornaamwoorden hebben een onderwerpsvorm en een andere vorm."),
    keuze("In 'De man die belde, was boos' is 'die' een [[*betrekkelijk|aanwijzend|vragend]] voornaamwoord.", "Het verwijst terug en begint een bijzin."),
    keuze("Verwijswoorden in een tekst zijn meestal [[*voornaamwoorden|voorzetsels|telwoorden]].", "Een voornaamwoord vervangt een naamwoord dat eerder stond."),
    sleep("In 'De [[twee]] kinderen speelden [[op]] het strand [[en]] bouwden een [[groot]] zandkasteel' staan een telwoord, een voorzetsel, een voegwoord en een bijvoeglijk naamwoord.",
          ["elkaar", "oei"],
          "Twee is een telwoord, op een voorzetsel, en een voegwoord, groot een bijvoeglijk naamwoord."),
    inv("Hoe noem je met twee woorden het woord dat een persoon, dier, ding of begrip benoemt?", ["zelfstandig naamwoord", "een zelfstandig naamwoord", "substantief"], "Een zelfstandig naamwoord."),
    keuze("'Kat sliep op mat' klinkt vreemd omdat de [[*lidwoorden|voorzetsels|werkwoorden]] ontbreken.", "'De kat sliep op de mat.'"),
    tabel("Bestaat dit als soort voornaamwoord?",
          [("wederkerend", J), ("betrekkelijk", J), ("bijwoordelijk", F), ("onbepaald", J)],
          "Er zijn acht soorten voornaamwoorden."),
    keuze("'Hun' in 'hun fietsen' is een [[*bezittelijk|persoonlijk|vragend]] voornaamwoord.", "Het zegt bij wie de fietsen horen."),
    keuze("In 'Er staat iemand aan de deur' is 'iemand' een [[*onbepaald|aanwijzend|wederkerig]] voornaamwoord.", "Net als niemand, iedereen en alles."),
    keuze("'Deze' en 'dit' wijzen naar iets wat [[*dichtbij|ver weg|onbekend]] is.", "Die en dat voor wat verder weg staat."),
    keuze("Bijwoorden zeggen iets over tijd, plaats, mate of [[*manier|bezit|aantal]].", "Gisteren, daar, nauwelijks, snel."),
    inv("Hoe noem je een woord als 'en', 'maar' of 'omdat'? Eén woord.", ["voegwoord", "een voegwoord"], "Een voegwoord."),
    open_("Leg met twee voorbeeldzinnen uit wanneer 'mooi' een bijvoeglijk naamwoord is en wanneer een bijwoord.",
          "In 'een mooi lied' zegt 'mooi' iets over het zelfstandig naamwoord 'lied': bijvoeglijk naamwoord. In 'Ze zingt mooi' zegt het iets over het werkwoord 'zingt': bijwoord."),
]

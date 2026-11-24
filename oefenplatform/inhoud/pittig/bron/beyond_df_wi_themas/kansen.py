"""Kansen en de wet van Laplace — pittig (Beyond dubbele finaliteit, wiskunde).

Enkele pittige vragen wiskunde basis Beyond binnen wi_kansen, verder eigen vragen."""
from ..beyond_wiskunde_basis_themas import kansen as K
from ..beyond_wiskunde_basis_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(K.VRAGEN, [9, 10, 12, 15, 18, 25, 26]) + [
    casus(
        "Een schoolfeest heeft een tombola met \\(400\\) loten. Daarvan winnen er \\(20\\) een kleine prijs en \\(4\\) een grote prijs. "
        "De rest wint niets. Je koopt één lot.",
        [
            inv("Wat is de kans dat je een grote prijs wint? Geef een kommagetal.", ["0,01", "0.01", "1 %", "1%"], "\\(4\\) gunstige op \\(400\\): \\(0{,}01\\)."),
            inv("Wat is de kans dat je iets wint? Geef een kommagetal.", ["0,06", "0.06", "6 %", "6%"], "\\(24\\) winnende loten op \\(400\\)."),
            mk("Wat is de kans dat je niets wint?",
               ["\\(0{,}94\\)", "\\(0{,}06\\)", "\\(0{,}99\\)", "\\(0{,}376\\)"], 0, "Met de complementregel: \\(1 - 0{,}06\\)."),
            keuze("Als iedereen een lot koopt en alle loten even goed gemengd zijn, mag je hier de wet van Laplace [[*wel|niet]] gebruiken.", "Elk lot heeft evenveel kans om getrokken te worden."),
        ],
    ),
    tabel("Hoe groot is de kans bij één worp met een eerlijke dobbelsteen?", [
        ("een getal kleiner dan \\(3\\)", "\\(\\tfrac{1}{3}\\)"), ("een priemgetal", "\\(\\tfrac{1}{2}\\)"),
        ("een veelvoud van \\(3\\)", "\\(\\tfrac{1}{3}\\)"), ("een getal groter dan \\(6\\)", "\\(0\\)"),
    ], "Priemgetallen op een dobbelsteen: \\(2\\), \\(3\\) en \\(5\\).", kolommen=["\\(0\\)", "\\(\\tfrac{1}{3}\\)", "\\(\\tfrac{1}{2}\\)"]),
    mk("Je gooit met twee dobbelstenen. Wat is de kans dat de som \\(10\\) of meer is?",
       ["\\(\\tfrac{1}{6}\\)", "\\(\\tfrac{1}{12}\\)", "\\(\\tfrac{3}{36}\\)", "\\(\\tfrac{1}{4}\\)"], 0,
       "Som \\(10\\): drie manieren, som \\(11\\): twee, som \\(12\\): één. Zes op zesendertig."),
    inv("Je gooit met twee dobbelstenen. Wat is de kans dat je géén dubbel gooit? Schrijf het als breuk.", ["5/6", "30/36", "vijf zesde"],
        "Zes dubbels op zesendertig, dus \\(1 - \\tfrac{6}{36} = \\tfrac{30}{36}\\)."),
    mk("Uit een kaartspel van \\(52\\) trek je één kaart. Wat is de kans op een aas of een harten?",
       ["\\(\\tfrac{16}{52}\\)", "\\(\\tfrac{17}{52}\\)", "\\(\\tfrac{4}{52}\\)", "\\(\\tfrac{13}{52}\\)"], 0,
       "Dertien harten en nog drie azen die geen harten zijn: \\(16\\) gunstige."),
    tabel("Is dit een uitkomst, een gebeurtenis of de uitkomstenverzameling?", [
        ("\\(\\{1, 2, 3, 4, 5, 6\\}\\) bij een dobbelsteen", "uitkomstenverzameling"), ("je gooit een \\(4\\)", "uitkomst"),
        ("je gooit een oneven getal", "gebeurtenis"), ("\\(\\{KK, KM, MK, MM\\}\\) bij twee keer een muntstuk", "uitkomstenverzameling"),
    ], "Een gebeurtenis is een deel van de uitkomstenverzameling.", kolommen=["uitkomst", "gebeurtenis", "uitkomstenverzameling"]),
    inv("Een vaas bevat rode en blauwe knikkers. De kans op rood is \\(0{,}35\\). Er zitten \\(13\\) blauwe knikkers in. Hoeveel knikkers zitten er in totaal in de vaas?", ["20", "twintig"],
        "Blauw heeft kans \\(0{,}65\\), dus \\(13 : 0{,}65 = 20\\)."),
    mk("Een leerling gooit een munt \\(10\\) keer en krijgt \\(7\\) keer kop. Wat is de beste conclusie?",
       ["Tien worpen zijn te weinig om iets over de munt te zeggen.", "De kans op kop is bij deze munt zeker \\(0{,}7\\).", "Bij de volgende worp komt zeker munt, om het goed te maken.", "De munt is vals, want de helft is vijf en niet zeven."], 0,
       "Pas bij heel veel worpen komt de relatieve frequentie dicht bij de kans."),
    keuze("Een relatieve frequentie [[*meet|berekent]] je met een experiment; een Laplacekans [[*berekent|meet]] je vooraf uit de gelijke uitkomsten.", "Bij veel herhalingen komen ze dicht bij elkaar."),
    inv("Een supermarkt telt op een week \\(2400\\) klanten, waarvan \\(360\\) met de fiets komen. Wat is de relatieve frequentie van fietsers? Geef een kommagetal.", ["0,15", "0.15", "15 %", "15%"],
        "\\(360 : 2400 = 0{,}15\\)."),
    mk("Welke kans is het grootst?",
       ["minstens één kop bij twee worpen met een munt", "een zes bij één worp met een dobbelsteen", "twee keer kop bij twee worpen met een munt", "een harten bij één kaart uit een spel van \\(52\\)"], 0,
       "\\(0{,}75\\) tegenover \\(\\tfrac{1}{6}\\), \\(0{,}25\\) en \\(0{,}25\\)."),
    volgorde("Zet deze gebeurtenissen van kleine naar grote kans.", [
        "met twee dobbelstenen som \\(2\\) gooien", "met één dobbelsteen een \\(6\\) gooien", "met één dobbelsteen een even getal gooien", "met één dobbelsteen geen \\(6\\) gooien",
    ], "\\(\\tfrac{1}{36}\\), \\(\\tfrac{1}{6}\\), \\(\\tfrac{1}{2}\\), \\(\\tfrac{5}{6}\\)."),
    sorteer("Kan dit een kans zijn?", ["kan een kans zijn", "kan geen kans zijn"], [
        ["\\(0\\)", "kan een kans zijn"], ["\\(0{,}75\\)", "kan een kans zijn"], ["\\(1\\)", "kan een kans zijn"],
        ["\\(1{,}2\\)", "kan geen kans zijn"], ["\\(-0{,}1\\)", "kan geen kans zijn"], ["\\(120\\,\\%\\)", "kan geen kans zijn"],
    ], "Een kans ligt altijd tussen \\(0\\) en \\(1\\), of tussen \\(0\\) en \\(100\\) procent."),
    mk("Een klas telt \\(28\\) leerlingen. De kans dat een willekeurige leerling een broer heeft, is \\(\\tfrac{3}{7}\\). Hoeveel leerlingen hebben een broer?",
       ["\\(12\\)", "\\(3\\)", "\\(16\\)", "\\(7\\)"], 0, "\\(\\tfrac{3}{7} \\cdot 28 = 12\\)."),
    tabel("Klopt dit?", [
        ("Bij een loterij met \\(1\\) winnend lot op \\(500\\) win je zeker als je \\(500\\) keer meedoet met nieuwe trekkingen.", F),
        ("Met \\(10\\) loten van één trekking met \\(500\\) loten is je winkans \\(0{,}02\\).", J),
        ("Een munt die vaak kop gaf, geeft daarna vaker munt.", F),
    ], "Bij elke nieuwe trekking begint alles opnieuw; een munt heeft geen geheugen."),
    open_("Leg uit waarom je de wet van Laplace niet mag gebruiken om de kans te berekenen dat een geroosterde boterham op de beboterde kant valt.",
          "Laplace mag enkel als alle uitkomsten even waarschijnlijk zijn. De boterham is niet symmetrisch, dus de twee kanten hebben niet zeker dezelfde kans. Je schat de kans beter met een experiment en de relatieve frequentie.",
          "Twee uitkomsten betekent niet automatisch een kans van één op twee."),
    inv("Je trekt een kaart uit een spel van \\(52\\). Wat is de kans dat het géén prentkaart is (boer, dame of heer)? Schrijf het als breuk.", ["40/52", "10/13", "tien dertiende"],
        "Twaalf prentkaarten, dus \\(40\\) andere."),
    mk("Een draaischijf heeft \\(8\\) gelijke vakken: \\(3\\) rood, \\(4\\) geel, \\(1\\) groen. Wat is de kans op niet-geel?",
       ["\\(0{,}5\\)", "\\(0{,}375\\)", "\\(0{,}125\\)", "\\(0{,}625\\)"], 0, "Vier van de acht vakken zijn niet geel."),
    koppel("Koppel elk begrip uit de kansrekening aan een voorbeeld bij één dobbelsteenworp.", [
        ["uitkomst", "je gooit een \\(5\\)"], ["gebeurtenis", "je gooit meer dan \\(4\\)"],
        ["complement van « een \\(6\\) gooien »", "je gooit \\(1\\), \\(2\\), \\(3\\), \\(4\\) of \\(5\\)"], ["zekere gebeurtenis", "je gooit een getal van \\(1\\) tot \\(6\\)"],
    ], ["je gooit een \\(7\\)"], "Een \\(7\\) gooien is een onmogelijke gebeurtenis."),
    inv("Je gooit drie keer met een muntstuk. Hoeveel uitkomsten telt de uitkomstenverzameling?", ["8", "acht"],
        "Twee mogelijkheden per worp: \\(2 \\cdot 2 \\cdot 2 = 8\\)."),
]

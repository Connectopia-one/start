"""Exponentiële functies — pittig (Beyond dubbele finaliteit, wiskunde).

Enkele pittige vragen wiskunde basis Beyond (met de prent van de grafieken) binnen wi_exponentieel, verder eigen vragen over f(x) = b · aˣ."""
from ..beyond_wiskunde_basis_themas import exponentieel as E
from ..beyond_wiskunde_basis_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(E.VRAGEN, [0, 16, 19, 22, 24]) + [
    casus(
        "Een tabel hoort bij een exponentiële functie \\(f(x) = b \\cdot a^{x}\\). Bij \\(x = 0\\), \\(1\\), \\(2\\) en \\(3\\) horen de waarden \\(80\\), \\(60\\), \\(45\\) en \\(33{,}75\\).",
        [
            inv("Wat is de beginwaarde \\(b\\)?", ["80", "tachtig"], "De waarde bij \\(x = 0\\)."),
            inv("Wat is de groeifactor \\(a\\)? Geef een kommagetal.", ["0,75", "0.75", "3/4"], "\\(60 : 80 = 0{,}75\\), en zo verder."),
            keuze("De functie is [[*dalend|stijgend|constant]], want de groeifactor ligt tussen \\(0\\) en \\(1\\).", "Elke stap wordt het een vierde minder."),
            inv("Wat is \\(f(4)\\)? Rond af op twee cijfers na de komma.", ["25,31", "25.31"], "\\(33{,}75 \\cdot 0{,}75 = 25{,}3125\\)."),
        ],
    ),
    tabel("Is de functie stijgend of dalend?", [
        ("\\(f(x) = 3 \\cdot 1{,}2^{x}\\)", "stijgend"), ("\\(f(x) = 100 \\cdot 0{,}9^{x}\\)", "dalend"),
        ("\\(f(x) = 0{,}5 \\cdot 4^{x}\\)", "stijgend"), ("\\(f(x) = 7 \\cdot \\left(\\tfrac{2}{3}\\right)^{x}\\)", "dalend"),
    ], "Alleen de groeifactor beslist, niet de beginwaarde.", kolommen=["stijgend", "dalend"]),
    mk("Een grafiek gaat door \\((0, 4)\\) en \\((1, 10)\\). Welk voorschrift hoort erbij?",
       ["\\(f(x) = 4 \\cdot 2{,}5^{x}\\)", "\\(f(x) = 10 \\cdot 4^{x}\\)", "\\(f(x) = 4 \\cdot 6^{x}\\)", "\\(f(x) = 2{,}5 \\cdot 4^{x}\\)"], 0,
       "Beginwaarde \\(4\\), groeifactor \\(10 : 4 = 2{,}5\\)."),
    inv("\\(f(x) = 3 \\cdot 2^{x}\\). Hoeveel is \\(f(-1)\\)? Geef een kommagetal.", ["1,5", "1.5", "3/2"], "\\(2^{-1} = \\tfrac{1}{2}\\)."),
    inv("\\(f(x) = 2 \\cdot 3^{x}\\). Voor welke \\(x\\) is \\(f(x) = 162\\)?", ["4", "vier"], "\\(3^{x} = 81 = 3^{4}\\)."),
    mk("Wat is het bereik van \\(f(x) = 5 \\cdot 0{,}5^{x}\\)?",
       ["alle positieve getallen", "alle reële getallen", "de getallen van \\(0\\) tot \\(5\\)", "alle getallen groter dan \\(5\\)"], 0,
       "De functie komt willekeurig dicht bij nul en wordt willekeurig groot naar links."),
    tabel("Klopt dit over \\(f(x) = b \\cdot a^{x}\\) met \\(b > 0\\)?", [
        ("De grafiek snijdt de \\(y\\)-as in \\((0, b)\\).", J),
        ("De grafiek snijdt de \\(x\\)-as.", F),
        ("Het domein is alle reële getallen.", J),
        ("Een negatieve groeifactor is toegelaten.", F),
    ], "Er is geen nulwaarde, en de groeifactor is positief en verschillend van \\(1\\)."),
    sorteer("Hoort deze rij bij lineaire of bij exponentiële groei?", ["lineair", "exponentieel"], [
        ["\\(5, 10, 20, 40\\)", "exponentieel"], ["\\(5, 10, 15, 20\\)", "lineair"], ["\\(81, 27, 9, 3\\)", "exponentieel"],
        ["\\(100, 90, 80, 70\\)", "lineair"], ["\\(100, 90, 81, 72{,}9\\)", "exponentieel"],
    ], "Deel elk getal door het vorige: blijft dat gelijk, dan is het exponentieel."),
    koppel("Koppel elk voorschrift aan zijn beschrijving.", [
        ["\\(f(x) = 2 \\cdot 3^{x}\\)", "beginwaarde \\(2\\), stijgend"], ["\\(f(x) = 3 \\cdot 2^{x}\\)", "beginwaarde \\(3\\), stijgend"],
        ["\\(f(x) = 3 \\cdot 0{,}2^{x}\\)", "beginwaarde \\(3\\), dalend"], ["\\(f(x) = 2 \\cdot 0{,}3^{x}\\)", "beginwaarde \\(2\\), dalend"],
    ], ["beginwaarde \\(0\\), stijgend"], "De beginwaarde staat voor de macht, de groeifactor is het grondtal."),
    mk("Twee functies hebben beginwaarde \\(10\\). De ene heeft groeifactor \\(1{,}1\\), de andere \\(1{,}5\\). Wat is juist?",
       ["Ze snijden in \\((0, 10)\\) en daarna stijgt de tweede sneller.", "De eerste stijgt sneller, want \\(1{,}1\\) is kleiner.", "Ze lopen evenwijdig, want de beginwaarde is gelijk.", "Ze snijden elkaar nergens, ook niet op de \\(y\\)-as."], 0,
       "Een grotere groeifactor geeft een steilere grafiek."),
    keuze("Verdubbel je de beginwaarde bij dezelfde groeifactor, dan wordt elke functiewaarde [[*twee keer zo groot|twee hoger|in het kwadraat genomen]].", "\\(2b \\cdot a^{x} = 2 \\cdot (b \\cdot a^{x})\\)."),
    inv("Een grafiek gaat door \\((0, 50)\\) en \\((2, 32)\\). Wat is de groeifactor? Geef een kommagetal.", ["0,8", "0.8"], "\\(a^{2} = 32 : 50 = 0{,}64\\), dus \\(a = 0{,}8\\)."),
    volgorde("Zet de functiewaarden van \\(f(x) = 4 \\cdot 2^{x}\\) van klein naar groot.", [
        "\\(f(-2)\\)", "\\(f(-1)\\)", "\\(f(0)\\)", "\\(f(1)\\)", "\\(f(3)\\)",
    ], "\\(1\\), \\(2\\), \\(4\\), \\(8\\) en \\(32\\)."),
    mk("Welke groeifactor hoort bij een functie die per stap \\(35\\) procent kleiner wordt?",
       ["\\(0{,}65\\)", "\\(0{,}35\\)", "\\(1{,}35\\)", "\\(-0{,}35\\)"], 0, "Er blijft \\(65\\) procent over."),
    tabel("Hoeveel is \\(f(x) = 64 \\cdot 0{,}5^{x}\\) in dit punt?", [
        ("\\(x = 1\\)", "\\(32\\)"), ("\\(x = 3\\)", "\\(8\\)"), ("\\(x = -1\\)", "\\(128\\)"),
    ], "Elke stap naar rechts halveert, elke stap naar links verdubbelt.", kolommen=["\\(8\\)", "\\(32\\)", "\\(128\\)"]),
    open_("Leg uit waarom de grafiek van \\(f(x) = 3 \\cdot 2^{x}\\) de \\(x\\)-as nooit snijdt.",
          "\\(2^{x}\\) is voor elke \\(x\\) positief, en drie keer een positief getal blijft positief. De functiewaarde wordt dus nooit nul, ook al komt ze er naar links heel dicht bij.",
          "Een positieve beginwaarde maal een positieve macht blijft positief."),
    mk("Een stijgende exponentiële functie heeft een toenemende stijging. Wat betekent dat?",
       ["Per stap komt er telkens meer bij dan de vorige keer.", "Per stap komt er telkens hetzelfde bij.", "De grafiek wordt na een tijd een horizontale rechte.", "De grafiek daalt eerst en stijgt daarna."], 0,
       "Je vermenigvuldigt met dezelfde factor, dus de toename groeit mee."),
    inv("\\(f(x) = 1000 \\cdot 0{,}9^{x}\\). Hoeveel is \\(f(2)\\)?", ["810", "achthonderdtien"], "\\(0{,}9^{2} = 0{,}81\\)."),
    keuze("Een exponentiële functie met groeifactor \\(1\\) zou [[*constant|stijgend|dalend]] zijn; daarom sluit men die groeifactor uit.", "Met factor één verandert er niets."),
    tabel("Hoort deze grafiekbeschrijving bij een lineaire of een exponentiële functie?", [
        ("een rechte die gelijkmatig stijgt", "lineair"), ("een kromme die traag begint en daarna steeds steiler wordt", "exponentieel"),
        ("een kromme die naar rechts steeds dichter bij de \\(x\\)-as kruipt", "exponentieel"),
    ], "Een exponentiële grafiek is nooit een rechte.", kolommen=["lineair", "exponentieel"]),
    mk("Hoe zie je in een tabel met gelijke stappen in \\(x\\) dat de functie exponentieel is?",
       ["Het quotiënt van twee opeenvolgende waarden is constant.", "Het verschil van twee opeenvolgende waarden is constant.", "De waarden worden altijd groter.", "De eerste waarde is altijd \\(1\\)."], 0,
       "Een constant verschil wijst op lineaire groei."),
    inv("\\(f(x) = b \\cdot 3^{x}\\) gaat door \\((2, 36)\\). Wat is de beginwaarde?", ["4", "vier"], "\\(b \\cdot 9 = 36\\)."),
]

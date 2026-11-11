"""Geld, monetaire aggregaten en geldschepping — pittig (🌍 Beyond, economie)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prentmaat import pix_zone, s_tekst, s_vak, GROEN, LICHT

# Drie geneste vakken: M3 rond M2 rond M1 (eigen tekening).
M3 = (90, 70, 820, 520)
M2 = (180, 140, 640, 400)
M1 = (290, 220, 420, 240)


def _aggregaten():
    d = []
    for (x, y, w, h), naam, vul in [(M3, "M3", "#f3efe2"), (M2, "M2", "#e6eedc"), (M1, "M1", "#fffdf7")]:
        d.append(s_vak(x, y, w, h, vul=vul, rand=GROEN, dikte=3, rond=26))
        d.append(s_tekst(x + 22, y + 38, naam, 28, anker="start", kleur=GROEN, vet=True))
    return d


def ring(buiten, binnen):
    """Klikvakken voor de rand tussen twee geneste vakken (boven, onder, links, rechts)."""
    bx, by, bw, bh = buiten
    ix, iy, iw, ih = binnen
    return [
        pix_zone(bx + 6, by + 50, ix - bx - 12, bh - 56),                # links
        pix_zone(ix + iw + 6, by + 50, bx + bw - ix - iw - 12, bh - 56),  # rechts
        pix_zone(ix, iy + ih + 6, iw, by + bh - iy - ih - 12),            # onder
    ]


GRAFIEKEN = [dict(naam="geld-monetaire-aggregaten", titel="De monetaire aggregaten", eigen=_aggregaten)]
PRENTEN = [dict(bestand="geld-monetaire-aggregaten.svg", zelf=True, wat="Drie geneste vakken M1, M2 en M3", vragen="klikvragen: waar hoort dit tegoed?")]
P = "geld-monetaire-aggregaten.svg"
M1_ZONE = pix_zone(M1[0] + 6, M1[1] + 50, M1[2] - 12, M1[3] - 56)

VRAGEN = [
    klik(
        "Klik op het kleinste aggregaat waar het briefje van 20 euro in je portefeuille al in zit.",
        P, [M1_ZONE],
        "Chartaal geld zit al in M1 (en dus ook in M2 en M3).",
    ),
    klik(
        "Klik op het kleinste aggregaat waar het geld op je spaarrekening al in zit.",
        P, ring(M2, M1),
        "Een spaarrekening is een secundaire liquiditeit: ze zit in M2, maar niet in M1.",
    ),
    klik(
        "Klik op het kleinste aggregaat waar het geld op je zichtrekening al in zit.",
        P, [M1_ZONE],
        "Zichtrekeningen zijn giraal geld en zitten al in M1, en dus ook in M2 en M3.",
    ),
    met_prent(P, mk(
        "Een gezin verplaatst 2 500 euro van zijn zichtrekening naar zijn spaarrekening. Wat gebeurt er met M1 en M2?",
        ["M1 daalt met 2 500 euro, M2 blijft gelijk", "M1 blijft gelijk, M2 stijgt met 2 500 euro",
         "M1 en M2 dalen allebei met 2 500 euro", "M1 en M2 blijven allebei gelijk"],
        0,
        "Het geld verlaat M1, maar het zit nog altijd in M2. Er ontstaat geen nieuw geld.",
    )),
    met_prent(P, tabel(
        "Waar of niet waar over de monetaire aggregaten?",
        [
            ("M1 is het kleinste aggregaat.", J),
            ("Chartaal geld zit niet in M3, enkel in M1.", F),
            ("M3 is het ruimste aggregaat.", J),
            ("M2 bevat chartaal geld, maar geen giraal geld.", F),
        ],
        "Elk aggregaat bevat het vorige: wat in M1 zit, zit ook in M2 en M3.",
    )),
    tabel(
        "Welke functie van geld zie je hier?",
        [
            ("Je betaalt een broodje met je bankkaart", "Ruil- en betaalmiddel"),
            ("Je vergelijkt twee fietsen omdat beide prijzen in euro staan", "Waardemeter"),
            ("Je zet elke maand 30 euro opzij voor je rijbewijs", "Spaarmiddel"),
            ("Een bank leent geld aan een bedrijf voor een nieuwe machine", "Kredietmiddel"),
        ],
        "Betalen, vergelijken, opzijzetten, uitlenen: de vier functies van geld.",
        kolommen=["Ruil- en betaalmiddel", "Waardemeter", "Spaarmiddel", "Kredietmiddel"],
    ),
    mk(
        "Welke functie van geld tast een hoge inflatie vooral aan?",
        ["Spaarmiddel: je gespaarde geld wordt minder waard", "Ruilmiddel: winkels aanvaarden geen geld meer",
         "Kredietmiddel: banken mogen geen leningen meer geven", "Rekeneenheid: prijzen staan niet meer in euro"],
        0,
        "Bij hoge inflatie koop je later minder met hetzelfde bedrag.",
    ),
    mk(
        "Wat was het grote probleem van ruilhandel zonder geld?",
        ["Je moest iemand vinden die wilde wat jij had en tegelijk had wat jij wilde",
         "Je mocht enkel ruilen met mensen uit je eigen dorp of je eigen stad, niet daarbuiten",
         "Er bestonden toen nog geen goederen die mensen konden ruilen",
         "De overheid legde een zware belasting op elke ruil tussen twee mensen of bedrijven"],
        0,
        "Geld lost dat op: je verkoopt aan de ene en koopt bij de andere.",
    ),
    mk(
        "Waarom aanvaarden mensen papieren biljetten, ook al heeft het papier zelf weinig waarde?",
        ["Ze vertrouwen erop dat anderen ze ook aanvaarden", "Ze kunnen ze altijd omruilen voor goud bij de bank",
         "Het papier van bankbiljetten is heel duur om te maken", "De overheid verplicht iedereen om elke dag te betalen"],
        0,
        "Geld werkt op vertrouwen.",
    ),
    tabel(
        "Welke soort geld is dit?",
        [
            ("Munten in je spaarpot", "Chartaal geld"),
            ("Het tegoed op je zichtrekening", "Giraal geld"),
            ("Een termijnrekening van zes maanden", "Quasigeld"),
            ("Een prepaid betaalkaart", "E-money"),
            ("Bitcoin", "Cryptovaluta"),
        ],
        "Munten en biljetten: chartaal. Zichtrekening: giraal. Snel om te zetten tegoed: quasigeld.",
        kolommen=["Chartaal geld", "Giraal geld", "Quasigeld", "E-money", "Cryptovaluta"],
    ),
    mk(
        "Een leerling zegt: 'Mijn spaarrekening is giraal geld.' Wat klopt?",
        ["Fout: een spaarrekening is quasigeld, giraal geld zijn de zichtrekeningen",
         "Juist: alles wat op een rekening bij een bank staat, is giraal geld, ook een spaarrekening",
         "Fout: een spaarrekening is chartaal geld, want je kan het altijd afhalen aan de automaat",
         "Juist: een spaarrekening zit in M1, net als de zichtrekening"],
        0,
        "Een spaarrekening kan je snel omzetten, maar ze is geen giraal geld. Ze zit in M2, niet in M1.",
    ),
    tabel(
        "Waar of niet waar over cryptovaluta?",
        [
            ("Bitcoin wordt uitgegeven door de Europese Centrale Bank.", F),
            ("Een winkel in België moet bitcoin niet aanvaarden.", J),
            ("Bitcoin is een goede waardemeter, want de waarde is heel stabiel.", F),
            ("Cryptovaluta zijn digitale munten zonder centrale bank.", J),
        ],
        "Cryptovaluta zijn geen wettig betaalmiddel in België en hun waarde schommelt sterk.",
    ),
    mk(
        "Welk deel van M1 is in de eurozone het grootst?",
        ["Het girale geld", "Het chartale geld", "Het quasigeld", "De cryptovaluta"],
        0,
        "De meeste betalingen gebeuren via rekeningen. Giraal geld is het grootste deel van M1.",
    ),
    sorteer(
        "Is dit geldsubstitutie of geldschepping?",
        ["Geldsubstitutie", "Geldschepping"],
        [
            ["Je stort 200 euro aan biljetten op je zichtrekening", "Geldsubstitutie"],
            ["Je haalt 40 euro af aan de automaat", "Geldsubstitutie"],
            ["Een bank geeft een woonkrediet en zet het bedrag op de zichtrekening van de klant", "Geldschepping"],
            ["Een bank geeft een investeringskrediet aan een bedrijf", "Geldschepping"],
            ["Je zet geld van je zichtrekening op je spaarrekening", "Geldsubstitutie"],
        ],
        "Bij substitutie verandert enkel de soort geld. Bij geldschepping ontstaat er nieuw geld, via een krediet.",
    ),
    mk(
        "Je stort 150 euro aan biljetten op je zichtrekening. Wat gebeurt er met M1?",
        ["M1 blijft gelijk: chartaal geld wordt giraal geld", "M1 stijgt met 150 euro: er komt giraal geld bij",
         "M1 daalt met 150 euro: er is minder chartaal geld", "M1 stijgt met 300 euro: het geld telt dubbel"],
        0,
        "Geldsubstitutie: de soort geld verandert, de hoeveelheid in M1 niet.",
    ),
    casus(
        "In een maand geeft een bank 3 miljoen euro nieuwe kredieten. Klanten betalen in die maand 1,8 miljoen euro aan leningen terug.",
        [
            mk("Wie schept hier giraal geld?", ["De commerciële bank, met kredieten", "De Europese Centrale Bank, met biljetten",
                                               "De klanten, door terug te betalen", "Niemand: geld kan je niet scheppen"], 0,
               "Commerciële banken scheppen giraal geld als ze een krediet op de zichtrekening van een klant zetten."),
            mk("Wat gebeurt er met het geld dat klanten terugbetalen?",
               ["Het verdwijnt: er is minder giraal geld", "Het wordt omgezet in chartaal geld bij de bank", "Het gaat rechtstreeks naar de centrale bank", "Het wordt automatisch een nieuw krediet"], 0,
               "Bij terugbetaling van een lening verdwijnt er giraal geld."),
            inv("Met hoeveel miljoen euro verandert het girale geld per saldo? Schrijf het getal met een komma.", "1,2",
                "3 − 1,8 = 1,2 miljoen euro meer."),
        ],
    ),
    mk(
        "Een bank wil zoveel mogelijk kredieten geven. Wat houdt haar tegen om onbeperkt giraal geld te scheppen?",
        ["Ze moet reserves en kapitaal aanhouden", "Ze mag enkel biljetten drukken met toestemming van de ECB",
         "Ze mag geen kredieten geven aan gezinnen", "Elke lening moet eerst door het parlement goedgekeurd worden"],
        0,
        "Reserves en kapitaal leggen een grens op het aantal kredieten.",
    ),
    koppel(
        "Wie doet wat?",
        [
            ["Het Eurosysteem", "Geeft de bankbiljetten uit in de eurozone"],
            ["Een commerciële bank", "Schept giraal geld met kredieten"],
            ["De centrale bank", "Stuurt de geldhoeveelheid bij met de rente"],
        ],
        ["Bepaalt de koers van bitcoin"],
        "Bitcoin heeft geen centrale bank. De ECB en de nationale centrale banken vormen samen het Eurosysteem.",
    ),
    sleep(
        "De centrale bank is de bank van de [[banken]]. Ze stuurt de geldhoeveelheid bij met de [[rente]].",
        ["gezinnen", "belastingen", "wisselkoers"],
        "Commerciële banken hebben zelf een rekening bij de centrale bank.",
    ),
    volgorde(
        "Zet de monetaire aggregaten van klein naar groot.",
        ["M1", "M2", "M3"],
        "Elk aggregaat bevat het vorige.",
    ),
    keuze(
        "M2 is M1 plus de [[*secundaire liquiditeiten|cryptovaluta]], zoals spaar- en korte termijnrekeningen.",
        "Secundaire liquiditeiten zijn tegoeden die je snel kan omzetten in giraal of chartaal geld.",
    ),
    open_(
        "Leg uit waarom een woonkrediet geldschepping is, maar geld afhalen aan de automaat niet.",
        "Bij een woonkrediet zet de bank een nieuw bedrag op de zichtrekening van de klant: er ontstaat giraal geld dat er voordien niet was, M1 stijgt. Aan de automaat zet je giraal geld om in chartaal geld: de soort verandert, maar er komt geen geld bij. Dat is geldsubstitutie.",
    ),
    inv(
        "Een bank geeft een lening van 25 000 euro en zet dat bedrag op de zichtrekening van de klant. Met hoeveel euro stijgt M1? Schrijf het getal zonder spaties.",
        "25000",
        "Geldschepping: er ontstaat 25 000 euro nieuw giraal geld.",
    ),
    mk(
        "Een stad heeft 6 miljoen euro chartaal geld en 14 miljoen euro op zichtrekeningen, plus 9 miljoen euro op spaarrekeningen. Hoe groot is M1?",
        ["20 miljoen euro", "29 miljoen euro", "14 miljoen euro", "23 miljoen euro"],
        0,
        "M1 = chartaal + giraal = 6 + 14 = 20 miljoen. De spaarrekeningen tellen pas mee in M2.",
    ),
    tabel(
        "Zit dit in M1?",
        [
            ("Biljetten en munten bij het publiek", "Wel"),
            ("Een termijnrekening van zes maanden", "Niet"),
            ("Het tegoed op de zichtrekening van een bedrijf", "Wel"),
        ],
        "M1 = chartaal geld + giraal geld. Een termijnrekening is quasigeld en zit pas in M2.",
        kolommen=["Wel", "Niet"],
    ),
    mk(
        "Waarom is bitcoin een slechte waardemeter?",
        ["De waarde schommelt sterk", "Je kan er niets mee kopen", "Er bestaan te veel bitcoins", "Het wordt uitgegeven door de ECB"],
        0,
        "Een waardemeter moet toelaten prijzen te vergelijken. Met een sterk schommelende waarde lukt dat slecht.",
    ),
    tabel(
        "Wat gebeurt er met M1?",
        [
            ("Je haalt 100 euro af aan de automaat", "Blijft gelijk"),
            ("Een gezin betaalt een lening van 5 000 euro terug", "Daalt"),
            ("Een bank geeft een krediet aan een bakker", "Stijgt"),
        ],
        "Afhalen is substitutie. Terugbetalen doet giraal geld verdwijnen. Een krediet schept nieuw giraal geld.",
        kolommen=["Stijgt", "Daalt", "Blijft gelijk"],
    ),
    keuze(
        "Geldsubstitutie is een soort geld omzetten in een [[*andere soort|nieuwe lening]]. Er ontstaat dan [[*geen|wel]] nieuw geld.",
        "Bij geldschepping ontstaat er wel nieuw geld.",
    ),
]

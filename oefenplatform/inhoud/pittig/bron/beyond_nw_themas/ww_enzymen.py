"""Welzijnswetenschappen: enzymen — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Deels overgenomen uit de pittige vragen biologie Beyond (zelfde leerstof,
zelfde prenten), aangevuld met eigen vragen over cofactoren, verzadiging,
inhibitoren en enzymen in het lichaam.
"""
from ..beyond_bio_themas import enzymen as E
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, casus

OVER = [E.VRAGEN[i] for i in (0, 1, 2, 8, 9, 10, 11, 12, 17, 18, 20, 22, 23, 25, 27)]

EIGEN = [
    tabel("Is dit een cofactor of een co-enzym?", [
        ("een zinkion", "cofactor"),
        ("een molecule afgeleid van vitamine B", "co-enzym"),
        ("een magnesiumion", "cofactor"),
        ("NAD, een organische helper", "co-enzym"),
    ], "Een co-enzym is een organische molecule, vaak afgeleid van een vitamine. Metaalionen noemt men cofactoren.",
       kolommen=["cofactor", "co-enzym"]),
    mk("Waarom kan een tekort aan bepaalde vitaminen enzymen trager laten werken?",
       ["Veel co-enzymen worden uit vitaminen gemaakt",
        "Vitaminen vormen het actief centrum van elk eiwit",
        "Vitaminen verhogen de lichaamstemperatuur tot het optimum",
        "Zonder vitaminen kan geen enkel substraat nog oplossen in water"], 0,
       "Zonder het co-enzym kan het enzym zijn werk niet doen, ook al is het enzym zelf in orde."),
    keuze("Als alle actieve centra bezet zijn, is het enzym [[*verzadigd|gedenatureerd|geremd]] en stijgt de snelheid niet meer.",
          "Meer substraat helpt dan niet. Meer enzym wel."),
    tabel("Wat gebeurt er met de reactiesnelheid?", [
        ("Je verhoogt de temperatuur van 20 °C naar 35 °C bij een menselijk enzym.", "stijgt"),
        ("Je verwarmt een menselijk enzym tot 80 °C.", "daalt"),
        ("Je voegt substraat toe terwijl alle actieve centra al bezet zijn.", "blijft gelijk"),
        ("Je voegt een inhibitor toe.", "daalt"),
    ], "Warmte tot het optimum versnelt, hitte denatureert, bij verzadiging helpt extra substraat niet en een remmer vertraagt.",
       kolommen=["stijgt", "daalt", "blijft gelijk"]),
    koppel("Koppel elk enzym aan de plaats waar het werkt.", [
        ["speekselamylase", "mondholte"],
        ["pepsine", "maag"],
        ["trypsine", "twaalfvingerige darm"],
        ["DNA-polymerase", "celkern"],
    ], ["galblaas"], "Elk enzym werkt waar zijn substraat is, en bij de pH van die plaats."),
    mk("Waarom maakt de maag pepsine eerst als pepsinogeen?",
       ["Zo verteert het enzym de cellen niet die het maken",
        "Pepsinogeen werkt sneller bij een neutrale pH dan pepsine",
        "Zo kan het enzym vetten afbreken voor het de eiwitten aanpakt",
        "Pepsinogeen is de vorm waarin het enzym door het bloed reist"], 0,
       "Pas in het zure maagsap wordt de inactieve vorm actief."),
    sleep("Een inhibitor die op het substraat lijkt, gaat in het [[actief centrum]] zitten. Hij remt dan het enzym, maar meer [[substraat]] kan hem verdringen.",
          ["co-enzym", "product"], "Het substraat en de remmer strijden om dezelfde plek."),
    inv("Een enzym zet 600 moleculen per seconde om. Hoeveel moleculen is dat in één minuut?", ["36000", "36 000"],
        "600 maal 60 seconden."),
    tabel("Klopt dit over de werking van enzymen?", [
        ("Een enzym verschuift het evenwicht naar meer product.", F),
        ("Een enzym laat het evenwicht sneller bereiken.", J),
        ("Na de reactie is het enzym opnieuw beschikbaar.", J),
        ("Elk enzym kan veel verschillende substraten omzetten.", F),
    ], "Een enzym versnelt heen en terug evenveel. Het is specifiek voor zijn substraat."),
    volgorde("Speekselamylase reist met een hap brood mee. Zet de plaatsen in de juiste volgorde.", [
        "mondholte: het enzym werkt goed",
        "slokdarm: het enzym werkt nog even verder",
        "maag: het zure midden stilt het enzym",
    ], "In de maag is de pH te laag voor speekselamylase."),
    sorteer("Werkt dit enzym het best in een zuur of in een licht basisch midden?", ["Zuur", "Licht basisch"], [
        ["pepsine", "Zuur"],
        ["trypsine", "Licht basisch"],
        ["lipase uit de alvleesklier", "Licht basisch"],
        ["het eiwitsplitsende enzym in het maagsap", "Zuur"],
    ], "De maag is zuur, de twaalfvingerige darm licht basisch door het natriumwaterstofcarbonaat."),
    mk("In een proef geef je amylase met zetmeel bij 0 °C, daarna zet je de buis op 37 °C. Wat zie je?",
       ["Het zetmeel wordt alsnog afgebroken",
        "Er gebeurt niets meer, want kou denatureert het enzym",
        "Het zetmeel verandert in eiwit door de grote temperatuurwissel",
        "Het enzym werkt pas weer na het toevoegen van nieuw substraat"], 0,
       "Kou vertraagt enkel. Het enzym is niet kapot."),
    keuze("Een enzym verlaagt de [[*activeringsenergie|reactie-energie|evenwichtsconstante]] van een reactie.",
          "Het geheel van begin en einde blijft gelijk; alleen de drempel zakt."),
]

VRAGEN = OVER + EIGEN

"""Het oog en het oor — pittig (🛠️ Boost dubbele finaliteit, gezondheidszorg en welzijn).

Klikvragen op de doorsneden van het oog en het oor uit natuurwetenschappen en
biologie Boost doorstroom, met eigen vragen strikt binnen gz_oog_oor."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..boost_do_bi_themas import oog as _g, oor as _o

OOG = "/examenvormen/natuurwetenschappen-boost-do/oog-doorsnede.svg"

VRAGEN = [_g.VRAGEN[i] for i in (11, 13, 14, 16)] + [_o.VRAGEN[i] for i in (0, 1, 2, 4, 5, 8, 19, 22)] + [
    {"type": "hotspot", "vraag": "Klik op het deel dat het licht buigt, zodat het beeld scherp op het netvlies valt.",
     "afbeelding_url": OOG, "zones": [[40.4, 39.1, 6.4, 25.0]],
     "uitleg": "De lens stelt scherp."},
    casus("Jens komt uit een donkere bioscoopzaal in het felle zonlicht.", [
        keuze("Zijn pupillen worden [[*kleiner|groter]].",
              "Zo valt er minder licht binnen: de pupilreflex."),
        keuze("De pupilreflex loopt via de [[*hersenstam|grote hersenen]], dus Jens beslist er niet zelf over.",
              "Een reflex gebeurt zonder dat je het wil."),
        keuze("Het gekleurde ringetje dat de pupil groter of kleiner maakt, is de [[*iris|lens|netvlies]].",
              "De iris regelt hoeveel licht binnenkomt."),
    ]),
    tabel("Staafjes of kegeltjes?",
          [("zien kleur", "kegeltjes"), ("werken bij weinig licht", "staafjes"), ("geven een scherp beeld bij veel licht", "kegeltjes"), ("zien geen kleur", "staafjes")],
          "Kegeltjes voor kleur, staafjes voor het donker.",
          kolommen=["staafjes", "kegeltjes"]),
    volgorde("Zet de weg van het licht in het oog in de juiste volgorde.",
             ["hoornvlies", "pupil", "lens", "netvlies", "oogzenuw"],
             "Van vooraan naar achteraan, en dan naar de hersenen."),
    tabel("Zit het aan de buitenkant van het oog?",
          [("het ooglid", J), ("de wimpers", J), ("het bindvlies", J), ("het netvlies", F)],
          "Het netvlies ligt binnenin, achteraan."),
    mk("Waarom schat je met één oog afstanden slechter in?",
       ["Dieptezicht komt van het verschil tussen twee beelden.", "Eén oog alleen heeft geen kegeltjes om kleur te kunnen zien.", "De pupil van één oog laat veel te weinig licht naar binnen.", "Met één oog staat het beeld op het netvlies niet meer op zijn kop."], 0,
       "Elk oog ziet een iets ander beeld; daaruit halen de hersenen de afstand."),
    sorteer("Buitenoor, middenoor of binnenoor?", ["buitenoor", "middenoor", "binnenoor"],
            [("de oorschelp", "buitenoor"), ("de gehoorbeentjes", "middenoor"), ("het slakkenhuis", "binnenoor"), ("de gehoorgang", "buitenoor"), ("het evenwichtsorgaan", "binnenoor")],
            "Het trommelvel ligt tussen het buitenoor en het middenoor."),
    tabel("Decibel of hertz?",
          [("hoe luid een geluid is", "decibel"), ("hoe hoog een toon is", "hertz"), ("het aantal trillingen per seconde", "hertz"), ("een festival haalt 100", "decibel")],
          "Decibel meet de sterkte, hertz de toonhoogte.",
          kolommen=["decibel", "hertz"]),
    casus("Nina gaat elk weekend naar een festival, altijd vlak bij de boxen, zonder oordopjes. Na een tijd hoort ze een fluittoon en verstaat ze slecht in een drukke ruimte.", [
        keuze("De schade zit in de [[*haarcellen van het orgaan van Corti|gehoorbeentjes|oorschelp]].",
              "Te veel lawaai beschadigt de haarcellen."),
        keuze("Die schade is [[*blijvend|tijdelijk]], want haarcellen groeien niet terug.",
              "Wat weg is, blijft weg."),
        keuze("Nina beschermt haar gehoor het best met [[*oordopjes|een muts|luidere muziek thuis]].",
              "Oordopjes dempen het geluid."),
    ]),
    keuze("Boven [[*tachtig|twintig]] decibel kan lang luisteren je gehoor beschadigen.",
          "Hoe luider, hoe korter je het veilig verdraagt."),
    inv("Hoeveel gehoorbeentjes zitten er in het middenoor? Een cijfer.", ["3", "drie"],
        "Hamer, aambeeld en stijgbeugel."),
    keuze("Het binnenoor zorgt naast het horen ook voor je [[*evenwicht|zicht|smaak]].",
          "Met het evenwichtsorgaan naast het slakkenhuis."),
    keuze("Het beeld op het netvlies staat [[*omgekeerd|rechtop]]; de hersenen draaien het recht.",
          "De lens keert het beeld om."),
    keuze("De buis van Eustachius verbindt het middenoor met de [[*keel|neus|hersenen]].",
          "Zo blijft de druk aan beide kanten van het trommelvel gelijk."),
]

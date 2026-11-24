"""Natuurlijke selectie en het ontstaan van soorten — pittig (Beyond dubbele finaliteit, natuurwetenschappen).

Pittige vragen biologie Beyond (zelfde prenten), enkel wat in nwd_selectie staat, plus eigen vragen."""
from ..beyond_bio_themas import evolutie as E, selectie as S
from ..beyond_bio_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

_V = {"De allelfrequentie van het resistentie-allel stijgt.": "Het resistentie-allel komt steeds vaker voor.",
      "De allelfrequentie verandert": "Het gunstige allel komt vaker voor",
      "de [[allelfrequentie]] van het donkere allel": "het [[aandeel]] van het donkere allel",
      "allopatrische soortvorming": "soortvorming door geografische isolatie",
      "door mixing en crossing-over bij de meiose": "door het herschikken van chromosomen bij de meiose",
      "Een kommervormig bekken hoort bij het rechtop lopen.": "Rechtop lopen maakte de handen vrij."}

VRAGEN = kies(E.VRAGEN, [10, 11, 12, 17, 19, 20, 23, 24], _V) + kies(S.VRAGEN, [2, 4, 13, 14, 19, 20, 22, 25], _V) + [
    tabel("Welke isolatie is dit?", [
        ("een rivier verandert van loop en splitst een populatie muizen", "geografisch"),
        ("twee kikkersoorten paren in verschillende maanden", "temporeel"),
        ("twee vogelsoorten herkennen elkaars baltsroep niet", "gedrag"),
        ("de bouw van de dieren maakt paren onmogelijk", "morfologisch"),
    ], "Isolatie houdt de genen van twee groepen gescheiden.", kolommen=["geografisch", "temporeel", "gedrag", "morfologisch"]),
    mk("Een populatie konijnen leeft in een gebied waar het steeds meer sneeuwt. Wat verwacht je na veel generaties?",
       ["Meer konijnen met een lichte vacht", "Elk konijn kleurt zijn vacht zelf wit", "Alle konijnen sterven meteen uit", "De vacht wordt donkerder om warmte op te nemen"], 0,
       "Lichte konijnen vallen minder op voor roofdieren en krijgen meer jongen."),
    mk("Een muildier is het jong van een paard en een ezel, maar het kan zelf geen jongen krijgen. Wat besluit je?",
       ["Paard en ezel zijn twee verschillende soorten.", "Paard en ezel zijn één soort met twee rassen.", "Muildieren vormen samen een nieuwe soort.", "Ezels zijn eigenlijk kleine wilde paarden."], 0,
       "Een soort krijgt onderling vruchtbare nakomelingen."),
    mk("Een pauw heeft een lange staart die hem trager maakt. Waarom bleef die staart toch bestaan?",
       ["Vrouwtjes kiezen mannetjes met een mooie staart.", "De staart helpt de pauw om sneller te vliegen.", "De staart beschermt de pauw tegen de kou.", "Pauwen kozen zelf om hun staart te laten groeien."], 0,
       "Seksuele selectie."),
    inv("Een antibioticum doodt 99 % van de bacteriën. Van 1 000 000 bacteriën, hoeveel overleven er?", ["10000", "10 000", "10.000"],
        "1 % van 1 000 000 = 10 000. Die kunnen resistent zijn en zich vermenigvuldigen."),
    keuze("Natuurlijke selectie [[*kiest uit wat er al is|maakt nieuwe eigenschappen aan]].", "Nieuwe allelen komen uit mutaties."),
    keuze("Een mutatie ontstaat [[*bij toeval|omdat het organisme ze nodig heeft]].", "Mutaties gebeuren los van wat nuttig is."),
    keuze("Een antibioticakuur vroegtijdig stoppen [[*vergroot|verkleint]] de kans op resistentie.", "De sterkste bacteriën blijven over."),
    keuze("Alleen [[*erfelijke|aangeleerde]] kenmerken spelen een rol bij natuurlijke selectie.", "Aangeleerde kenmerken gaan niet naar de jongen."),
    sorteer("Is dit een gedachte van Lamarck of van Darwin?", ["Lamarck", "Darwin"], [
        ["een dier past zich tijdens zijn leven aan en geeft dat door", "Lamarck"],
        ["binnen een soort bestaat er variatie", "Darwin"],
        ["er worden meer jongen geboren dan er overleven", "Darwin"],
        ["wat niet gebruikt wordt, verdwijnt en dat wordt doorgegeven", "Lamarck"],
    ], "Darwin: variatie en selectie. Lamarck: verworven eigenschappen doorgeven."),
    sleep("Australopithecus liep al [[rechtop]], terwijl zijn hersenen nog [[klein]] waren. Later leefden Homo sapiens en Homo [[neanderthalensis]] een tijd naast elkaar.",
          ["groot", "erectus-tijdperk"], "Rechtop lopen kwam eerst in de menswording."),
    open_("Leg uit waarom een kleine populatie een soort kwetsbaar maakt.",
          "Er is weinig variatie. Verandert de omgeving of komt er een nieuwe ziekte, dan is de kans klein dat er dieren zijn die toevallig goed aangepast zijn.",
          "Zonder variatie heeft selectie niets om uit te kiezen."),
]

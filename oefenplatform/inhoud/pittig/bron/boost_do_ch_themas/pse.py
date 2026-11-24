"""Het periodiek systeem der elementen — pittig (🚀 Boost doorstroom, chemie).

Klikvragen op een stuk periodiek systeem van natuurwetenschappen Boost doorstroom (met de prent), plus eigen vragen over hoofdgroepen, ionladingen, metaalkarakter en elektronegativiteit uit ch_pse."""
from ..boost_do_nw_themas import atoom as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [0, 1, 2, 3, 4, 5, 6, 15, 16, 18, 22, 23, 25])
VRAGEN += [
    casus("Een onbekend element X heeft de elektronenconfiguratie 2, 8, 6.", [
        tabel("Wat weet je over element X?",
              [("Het staat in periode 3.", J), ("Het staat in groep VIA.", J), ("Het is een metaal.", F), ("Het vormt een ion met lading 2−.", J)],
              "Drie schillen, zes valentie-elektronen: zwavel, een niet-metaal dat er twee opneemt."),
        mk("Met welk element lijkt X chemisch het meest?",
           ["zuurstof", "chloor", "fosfor", "argon"], 0,
           "Zuurstof staat in dezelfde groep VIA en heeft ook zes valentie-elektronen."),
    ]),
    koppel("Welke naam hoort bij elke hoofdgroep?",
           [("groep IA (zonder waterstof)", "alkalimetalen"), ("groep IIA", "aardalkalimetalen"), ("groep VIIA", "halogenen"), ("groep VIIIA", "edelgassen")],
           ["metalloïden", "zouten"], "Vier hoofdgroepen met een eigen naam."),
    tabel("Welke lading krijgt het ion van dit element?",
          [("kalium (groep IA)", "1+"), ("calcium (groep IIA)", "2+"), ("aluminium (groep IIIA)", "3+"), ("stikstof (groep VA)", "3−"), ("broom (groep VIIA)", "1−")],
          "Metalen geven hun valentie-elektronen af, niet-metalen vullen hun schil aan tot acht.", ["1+", "2+", "3+", "1−", "3−"]),
    mk("Welk element heeft de hoogste elektronegativiteit?",
       ["fluor", "natrium", "jood", "kalium"], 0,
       "Rechtsboven in het systeem (zonder edelgassen) is de elektronegativiteit het hoogst."),
    tabel("Klopt dit over hoe de elektronegativiteit verandert in het periodiek systeem?",
          [("Ze stijgt van links naar rechts in een periode.", J), ("Ze stijgt als je in een groep naar onder gaat.", F), ("Een lage elektronegativiteit hoort bij een sterk metaalkarakter.", J)],
          "Naar onder liggen de buitenste elektronen verder van de kern en worden ze minder sterk aangetrokken."),
    volgorde("Zet van laag naar hoog metaalkarakter.",
             ["chloor", "zwavel", "magnesium", "natrium"],
             "Het metaalkarakter neemt toe naar links in een periode."),
    inv("Kalium staat in periode 4. Hoeveel bezette schillen heeft een kaliumatoom?", ["4", "vier"],
        "Het periodenummer is het aantal bezette schillen: 2, 8, 8, 1."),
    mk("Een ion heeft 18 elektronen en een lading 2+. In welke groep staat het element?",
       ["groep IIA", "groep VIA", "groep VIIIA", "groep IA"], 0,
       "Twintig protonen: calcium, dat twee elektronen afgeeft."),
    sorteer("Geeft dit atoom eerder elektronen af of neemt het er op?", ["Geeft af", "Neemt op"],
            [("natrium", "Geeft af"), ("zuurstof", "Neemt op"), ("magnesium", "Geeft af"), ("chloor", "Neemt op"), ("lithium", "Geeft af"), ("stikstof", "Neemt op")],
            "Metalen geven af, niet-metalen nemen op tot hun buitenste schil vol is."),
    tabel("Klopt dit over de opbouw van het periodiek systeem?",
          [("Het atoomnummer stijgt van links naar rechts.", J), ("Elke periode telt evenveel elementen.", F), ("Waterstof staat linksboven, niet bij de edelgassen.", J), ("De niet-metalen staan vooral rechtsboven.", J)],
          "De eerste periode heeft maar twee elementen, de tweede en derde acht."),
    keuze("Het ion Na⁺ heeft dezelfde elektronenconfiguratie als het edelgas [[*neon|argon|helium]].",
          "Na⁺ heeft 2, 8: net als neon."),
    mk("Waarom lijken de halogenen chemisch op elkaar?",
       ["Ze hebben allemaal zeven valentie-elektronen.", "Ze hebben allemaal evenveel schillen.", "Ze zijn allemaal gassen bij kamertemperatuur.", "Ze hebben allemaal hetzelfde massagetal."], 0,
       "Hetzelfde aantal valentie-elektronen geeft gelijkaardig gedrag; broom is zelfs vloeibaar."),
    inv("Fosfor staat in groep VA. Hoeveel elektronen neemt een fosforatoom op om een ion te vormen?", ["3", "drie"],
        "Vijf valentie-elektronen plus drie maakt acht."),
    mk("Waarom vormen edelgassen bijna nooit ionen?",
       ["Hun buitenste schil is al vol.", "Ze hebben geen protonen in de kern.", "Ze staan helemaal links in het systeem.", "Ze zijn te zwaar om te reageren."], 0,
       "Een volle buitenste schil hoeft niets op te nemen of af te geven."),
    tabel("Klopt dit over een atoom links in het periodiek systeem?",
          [("Het heeft weinig valentie-elektronen.", J), ("Het vormt een positief ion.", J), ("Het heeft een hoge elektronegativiteit.", F)],
          "Links staan de metalen: weinig valentie-elektronen, makkelijk afgegeven."),
    sleep("Een verticale kolom heet een [[groep]]. Een horizontale rij heet een [[periode]]. De elektronen in de buitenste schil heten [[valentie-elektronen]].",
          ["isotopen", "halogenen"], "Drie begrippen om het periodiek systeem te lezen."),
]

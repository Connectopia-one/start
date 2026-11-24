"""Voortplanting en de menstruatiecyclus — pittig (🚀 Boost doorstroom, biologie).

Klikvragen op het vrouwelijk stelsel en de hormonengrafiek van natuurwetenschappen Boost doorstroom, zonder de hormonale regeling bij de man, plus eigen vragen over gameten, zwangerschap en de fasen van de cyclus."""
from ..boost_do_nw_themas import voortplanting as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 22, 23, 26, 27])
VRAGEN += [
    casus("Een vrouw is zes weken zwanger. Op de echografie ziet de dokter een klein vruchtje in de baarmoeder, met een koord naar de placenta.", [
        tabel("Kan deze stof via de placenta van de moeder naar het kind?",
              [("zuurstof", J), ("voedingsstoffen", J), ("alcohol", J), ("rode bloedcellen van de moeder", F)],
              "Stoffen gaan door het dunne laagje tussen beide bloedsomlopen; de bloedcellen zelf vermengen niet. Daarom raakt ook alcohol het kind."),
        mk("Hoe heet het koord tussen het kind en de placenta?",
           ["de navelstreng", "de eileider", "de baarmoederhals", "de buis van het vruchtwater"], 0,
           "In de navelstreng lopen de bloedvaten van het kind."),
        mk("Wat doet het vruchtwater?",
           ["Het beschermt het kind tegen stoten en houdt de warmte gelijk.", "Het brengt zuurstof rechtstreeks naar de longen van het kind.", "Het voert de hormonen van de hypofyse naar de baarmoeder.", "Het vormt na de geboorte de eerste melk voor het kind."], 0,
           "Het kind drijft in een beschermend kussen van vocht."),
    ]),
    sorteer("Menstruatiefase, folliculaire fase of luteale fase?", ["Menstruatiefase", "Folliculaire fase", "Luteale fase"],
            [("het baarmoederslijmvlies komt los", "Menstruatiefase"), ("een follikel rijpt in de eierstok", "Folliculaire fase"), ("het geel lichaam maakt progesteron", "Luteale fase"), ("het slijmvlies groeit weer aan onder invloed van oestrogeen", "Folliculaire fase"), ("na de eisprong blijft het slijmvlies dik", "Luteale fase")],
            "Na de menstruatie volgt de folliculaire fase tot de eisprong, daarna de luteale fase."),
    tabel("Klopt dit over gameten?",
          [("Een gameet heeft de helft van het aantal chromosomen van een lichaamscel.", J), ("Een zaadcel brengt 23 chromosomen mee.", J), ("Een zygote heeft de helft van de chromosomen van een lichaamscel.", F)],
          "Twee gameten met elk 23 chromosomen geven een zygote met 46."),
    volgorde("Zet de gebeurtenissen na de eisprong in de juiste volgorde, als er een bevruchting is.",
             ["De eicel komt in de eileider.", "Een zaadcel bevrucht de eicel.", "De zygote deelt zich op weg naar de baarmoeder.", "Het celklompje nestelt zich in het slijmvlies."],
             "Bevruchting in de eileider, innesteling in de baarmoeder."),
    mk("Twee tweelingzussen hebben precies hetzelfde erfelijk materiaal. Hoe zijn ze ontstaan?",
       ["Uit één bevruchte eicel die zich in tweeën splitste.", "Uit twee eicellen, bevrucht door twee zaadcellen.", "Uit één eicel die door twee zaadcellen bevrucht werd.", "Uit twee eicellen die in de eileider samengesmolten zijn."], 0,
       "Een eeneiige tweeling komt uit één zygote."),
    keuze("Bij de puberteit zet de [[*hypofyse|schildklier|placenta]] de geslachtsklieren aan om hormonen te maken.",
          "De hypofyse stuurt de eierstokken en de teelballen aan."),
    mk("Waarom lijkt een kind op allebei zijn ouders?",
       ["Het krijgt de helft van zijn chromosomen van elke ouder.", "Het krijgt alle chromosomen van de moeder en het bloed van de vader.", "De placenta mengt de kenmerken van beide ouders tijdens de zwangerschap.", "De vader bepaalt het uiterlijk en de moeder het karakter."], 0,
       "Eicel en zaadcel brengen elk 23 chromosomen mee."),
    inv("Hoe noem je het vastzetten van het celklompje in het baarmoederslijmvlies? Antwoord met één woord.",
        ["innesteling", "de innesteling", "nidatie"], "Na een week nestelt het celklompje zich in het dikke slijmvlies."),
    koppel("Welke taak hoort bij elk orgaan?",
           [("eierstok", "eicellen laten rijpen en oestrogeen maken"), ("teelbal", "zaadcellen vormen"), ("eileider", "plaats van de bevruchting"), ("baarmoeder", "plaats waar het kind groeit")],
           ["het kind van zuurstof voorzien", "het geluid opvangen"], "Vier organen van de voortplanting."),
    tabel("Klopt dit over de vruchtbare periode?",
          [("De kans op zwangerschap is het grootst rond de eisprong.", J), ("Een eicel leeft na de eisprong nog weken.", F), ("Zaadcellen kunnen enkele dagen overleven in het lichaam van de vrouw.", J)],
          "Een eicel leeft maar een dag; zaadcellen enkele dagen. Daarom ligt de vruchtbare periode rond de eisprong."),
]

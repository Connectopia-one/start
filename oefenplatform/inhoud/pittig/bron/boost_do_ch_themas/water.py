"""Stoffen in water: polariteit, oplossen en pH — pittig (🚀 Boost doorstroom, chemie).

Klikvragen op de pH-schaal en vragen over elektrolyten van natuurwetenschappen Boost doorstroom (met de prent), plus eigen vragen over intermoleculaire krachten en indicatoren uit ch_water."""
from ..boost_do_nw_themas import water as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 21, 22, 26])
VRAGEN += [
    koppel("Welke intermoleculaire kracht werkt vooral tussen deze deeltjes?",
           [("twee methaanmoleculen", "londonkracht"), ("twee HCl-moleculen", "dipoolkracht"), ("twee watermoleculen", "waterstofbrug"), ("een Na⁺-ion en watermoleculen", "ion-dipoolkracht")],
           ["ionbinding", "metaalbinding"], "Apolair: londonkracht; polair: dipoolkracht; H aan O, N of F: waterstofbrug; ion in water: ion-dipoolkracht."),
    volgorde("Zet de intermoleculaire krachten van zwak naar sterk.",
             ["londonkracht", "dipoolkracht", "waterstofbrug"],
             "De waterstofbrug is de sterkste van de krachten tussen moleculen, maar nog veel zwakker dan een binding."),
    casus("Een leerling test drie oplossingen met lakmoes en fenolftaleïne. Oplossing A: lakmoes rood, fenolftaleïne kleurloos. Oplossing B: lakmoes blauw, fenolftaleïne paars. Oplossing C: zuiver water.", [
        tabel("Zuur, neutraal of basisch?",
              [("oplossing A", "zuur"), ("oplossing B", "basisch"), ("oplossing C", "neutraal")],
              "Lakmoes rood in zuur, blauw in base; fenolftaleïne paars in base.", ["zuur", "neutraal", "basisch"]),
        mk("Welke stof kan in oplossing B zitten?",
           ["natriumhydroxide", "waterstofchloride", "azijnzuur", "suiker"], 0,
           "Een hydroxide geeft OH⁻-ionen en maakt de oplossing basisch."),
        tabel("Klopt dit over de oplossingen?",
              [("Oplossing A bevat meer H⁺ dan zuiver water.", J), ("De pH van oplossing B is lager dan 7.", F), ("Met een pH-meter meet je nauwkeuriger dan met een indicator.", J)],
              "Basisch betekent een pH boven 7; een indicator zegt enkel aan welke kant je zit."),
    ]),
    mk("Waarom is CO₂ apolair, terwijl de bindingen tussen C en O polair zijn?",
       ["De molecule is recht en symmetrisch, zodat de polariteiten elkaar opheffen.", "Koolstof en zuurstof hebben dezelfde elektronegativiteit.", "CO₂ is een ionverbinding zonder bindingen.", "Er zitten geen elektronen tussen koolstof en zuurstof."], 0,
       "De twee polaire bindingen wijzen in tegengestelde richting."),
    sorteer("Lost deze stof goed op in water of in wasbenzine?", ["Water", "Wasbenzine"],
            [("keukenzout", "Water"), ("vet", "Wasbenzine"), ("suiker", "Water"), ("kaarsvet", "Wasbenzine"), ("ethanol", "Water")],
            "Gelijk lost op in gelijk: polair in polair, apolair in apolair."),
    keuze("Het omhullen van een opgelost ion door watermoleculen heet [[*hydratatie|ionisatie|neutralisatie]].",
          "De watermoleculen draaien hun geladen kant naar het ion."),
    mk("Waarom kookt water bij 100 °C, veel hoger dan je bij zo'n kleine molecule verwacht?",
       ["Tussen watermoleculen zitten sterke waterstofbruggen.", "Water is een ionverbinding met een rooster.", "Watermoleculen zijn veel zwaarder dan andere moleculen.", "Water bevat opgeloste zouten die het kookpunt verhogen."], 0,
       "Om te koken moeten die bruggen eerst verbroken worden."),
    tabel("Klopt dit over polaire bindingen?",
          [("Een binding met een groot verschil in elektronegativiteit is polair.", J), ("Een molecule met polaire bindingen is altijd polair.", F), ("Londonkrachten werken tussen alle moleculen.", J)],
          "Een symmetrische molecule kan ondanks polaire bindingen apolair zijn."),
    inv("Hoeveel chloride-ionen ontstaan er als één formule-eenheid CaCl₂ dissocieert?", ["2", "twee"],
        "CaCl₂ → Ca²⁺ + 2 Cl⁻."),
    mk("Een vast blokje zout geleidt geen stroom, gesmolten zout wel. Waarom?",
       ["In de vloeistof kunnen de ionen bewegen.", "Bij het smelten ontstaan er vrije elektronen.", "Gesmolten zout bevat water.", "Bij het smelten worden de ionen neutraal."], 0,
       "In het rooster zitten de ionen vast; in de smelt kunnen ze lading verplaatsen."),
    sleep("Een stof die in water ionen vormt en stroom geleidt, is een [[elektrolyt]]. Suiker in water vormt geen ionen en is een [[niet-elektrolyt]]. Een zuur geeft in water [[H⁺]]-ionen.",
          ["OH⁻", "isolator"], "Drie begrippen over stoffen in water."),
    mk("Een oplossing heeft pH 2 en een andere pH 4. Wat klopt?",
       ["De eerste is honderd keer zuurder.", "De eerste is twee keer zuurder.", "De tweede is zuurder.", "Ze zijn even zuur."], 0,
       "Elke stap van één pH-eenheid is een factor tien: twee stappen is honderd keer."),
]

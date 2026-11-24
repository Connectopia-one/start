"""Taal en identiteit: stereotypen, inclusie en gevoelswaarde — pittig (Beyond dubbele finaliteit, Nederlands).

Pittige vragen Nederlands Beyond doorstroom die binnen nl_identiteit van dubbele finaliteit passen, aangevuld met eigen vragen over veralgemening, inclusie en gevoelswaarde."""
from ..beyond_nederlands_themas import identiteit as D
from ..beyond_nederlands_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(D.VRAGEN, [0, 1, 3, 4, 6, 11, 14, 15, 18, 19, 20, 23])
VRAGEN += [
    casus("Een lokaal krantje schrijft: \"Gisteren werd in de stationsbuurt opnieuw een fiets gestolen. Het gaat al jaren bergaf met die buurt. Bewoners vertellen dat ze 's avonds niet meer buiten durven.\" Er worden twee bewoners geciteerd, allebei van dezelfde straat.", [
        mk("Wat is het zwakste punt van dit stukje?",
           ["Twee bewoners staan voor de hele buurt.", "Er wordt een plaats genoemd waar de diefstal gebeurde.", "Het stukje vermeldt dat de fiets gisteren gestolen is.", "Er worden bewoners aan het woord gelaten in de krant."], 0,
           "Uit twee stemmen van één straat volgt niets over alle bewoners: dat is een veralgemening."),
        tabel("Welke woorden of zinsdelen kleuren het stukje negatief?",
              [("opnieuw", J), ("het gaat al jaren bergaf", J), ("die buurt", J), ("gisteren", F)], "'Opnieuw', 'bergaf' en 'die' geven een oordeel mee; 'gisteren' is enkel een tijdsaanduiding."),
        mk("Welke herschrijving is het eerlijkst?",
           ["Gisteren werd in de stationsbuurt een fiets gestolen. Twee bewoners van de Kerkstraat zeggen dat ze zich 's avonds onveilig voelen.",
            "Gisteren werd in de stationsbuurt alweer een fiets gestolen, zoals in die buurt wel vaker gebeurt.",
            "Iedereen in de stationsbuurt durft 's avonds niet meer buiten nu er weer een fiets weg is.",
            "De stationsbuurt blijft een probleem: gisteren verdween er weer eens een fiets."], 0,
           "Die versie zegt precies wat gebeurde en over wie de uitspraak gaat."),
    ]),
    sorteer("Neutraal of gekleurd?", ["Neutraal", "Gekleurd"],
            [("oudere werknemer", "Neutraal"), ("een oude zeur", "Gekleurd"), ("nieuwkomer", "Neutraal"), ("profiteur", "Gekleurd"), ("alleenstaande ouder", "Neutraal"), ("bende jongeren", "Gekleurd")],
            "Gekleurde woorden dragen een oordeel mee; neutrale woorden beschrijven enkel."),
    mk("Een woord dat vroeger gewoon was, wordt nu door de groep zelf als kwetsend ervaren. Wat doe je het best als schrijver?",
       ["Je kiest het woord dat de groep zelf verkiest.", "Je blijft het oude woord gebruiken omdat het in het woordenboek staat.", "Je vermijdt het om nog over die groep te schrijven.", "Je zet het oude woord tussen aanhalingstekens en laat het staan."], 0,
       "De groep zelf weet het best welk woord haar respecteert; dat volgen maakt je tekst niet zwakker."),
    tabel("Klopt dit over veralgemenen?",
          [("'Sommige leerlingen' is voorzichtiger dan 'de leerlingen'.", J), ("Een cijfer uit onderzoek maakt elke veralgemening terecht.", F), ("Ook een positieve veralgemening kan iemand in een hokje stoppen.", J), ("Je kan een veralgemening vaak herkennen aan woorden als 'altijd' of 'allemaal'.", J)],
          "Een cijfer zegt iets over een deel, niet over ieder lid van de groep."),
    keuze("Zuinig en gierig betekenen ongeveer hetzelfde, maar 'gierig' heeft een [[*negatieve|positieve|neutrale]] gevoelswaarde.",
          "Wie gierig genoemd wordt, krijgt meteen een verwijt mee."),
    koppel("Welk begrip past bij elk voorbeeld?",
           [("'Alle Italianen koken goed.'", "stereotype"), ("Een brochure legt moeilijke woorden uit in een kadertje.", "inclusief taalgebruik"), ("Twee vrienden praten in een taal die de derde niet verstaat.", "uitsluiting"), ("'Hij is koppig' tegenover 'hij is volhardend'.", "gevoelswaarde")],
           ["register", "jargon"], "Elk voorbeeld toont een andere manier waarop taal mensen raakt."),
    mk("Een reclame voor speelgoed toont enkel meisjes bij de poppen en enkel jongens bij de bouwdozen. Wat is het effect?",
       ["Kinderen leren dat sommig speelgoed niet voor hen is.", "Kinderen krijgen een eerlijk beeld van wie met wat speelt.", "Het effect is nul, omdat kinderen reclame niet zien.", "Ouders kopen daardoor meer verschillende soorten speelgoed."], 0,
       "Wat je steeds ziet, wordt gewoon; wie er nooit bij staat, voelt zich er niet bij horen."),
    tabel("Welke zinnen zijn inclusief geformuleerd?",
          [("Beste ouders en opvoeders,", J), ("Elke leerling brengt de eigen boeken mee.", J), ("Beste mama's,", F), ("Iedereen die wil meedoen, is welkom.", J)],
          "'Beste mama's' sluit papa's en andere opvoeders uit."),
    mk("Een krantenkop luidt: 'Jongeren steeds luier'. Het artikel gaat over een enquête bij 200 leerlingen. Welke kop is eerlijker?",
       ["Enquête: veel leerlingen sporten minder dan vroeger", "Jongeren steeds luier, zegt een nieuwe enquête", "Alle jongeren zijn luier dan hun ouders", "Luie jeugd baart onderzoekers zorgen"], 0,
       "Die kop noemt de bron en zegt niets over alle jongeren."),
    sleep("Een [[stereotype]] is een vast beeld van een groep. Wie het op elke persoon toepast, maakt een [[veralgemening]]. Taal die niemand onnodig buitensluit, heet [[inclusief]].",
          ["register", "exclusief"], "Drie begrippen die samen tonen hoe taal over groepen werkt."),
    mk("Waarom is 'Ik heb nog nooit een eerlijke verkoper gezien' een zwak argument?",
       ["Een eigen ervaring zegt niets over alle verkopers.", "Het is in de ik-vorm geschreven en dus te persoonlijk.", "Verkopers mogen in een argument niet genoemd worden.", "Het bevat geen woord met een negatieve gevoelswaarde."], 0,
       "Wat jij zag, is te weinig om iets over een hele beroepsgroep te zeggen."),
]

"""Soorten klanten en het verkoopgesprek — pittig (🛠️ Boost dubbele finaliteit, EBW).

Eigen vragen strikt binnen eb_verkoopgesprek."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

GESPREK = ("Lees het verkoopgesprek in een fietsenwinkel.\n\n"
           "1. Verkoper: Goeiemiddag! Ik zie dat u naar de elektrische fietsen kijkt.\n"
           "2. Klant: Ja, ik rijd elke dag twaalf kilometer naar mijn werk.\n"
           "3. Verkoper: Waarvoor gaat u de fiets vooral gebruiken, en hoe ziet uw rit eruit?\n"
           "4. Klant: Vooral woon-werk, met een steile helling. En ik wil niet bezweet aankomen.\n"
           "5. Verkoper: Dan raad ik dit model aan: de motor helpt tot 25 km per uur en de batterij haalt 80 km.\n"
           "6. Klant: Hm, 2 400 euro is wel veel geld.\n"
           "7. Verkoper: Ik begrijp het. Reken eens uit: u bespaart elke maand zo'n 120 euro aan brandstof en parking.\n"
           "8. Klant: Klopt. Hoe lang moet ik wachten als ik hem in het grijs wil?\n"
           "9. Verkoper: Hij staat in het magazijn. Zal ik hem voor zaterdag klaarzetten, met een gratis eerste nazicht?\n"
           "10. Klant: Graag!")

VRAGEN = [
    casus(GESPREK, [
        tabel("Welke fase van het verkoopgesprek zie je in deze zin?",
              [("zin 1", "aandacht"), ("zin 3", "behoefte"), ("zin 5", "argumenten"), ("zin 7", "bezwaar weerleggen"), ("zin 9", "afsluiting")],
              "Aandacht, behoefte, argumenten, bezwaren weerleggen, koopsignaal en afsluiting.",
              kolommen=["aandacht", "behoefte", "argumenten", "bezwaar weerleggen", "afsluiting"]),
        mk("In welke zin geeft de klant een koopsignaal?",
           ["zin 8", "zin 2", "zin 4", "zin 10"], 0,
           "Hij vraagt naar de levertijd in zijn kleur: hij wil kopen."),
        mk("Welk soort vraag stelt de verkoper in zin 3?",
           ["een open vraag", "een gesloten vraag", "een suggestieve vraag", "een strikvraag"], 0,
           "Een open vraag vraagt om uitleg en geeft meer terug dan ja of nee."),
        keuze("Zin 6 is een [[*bezwaar|koopsignaal|koopmotief]] van de klant.",
              "Hij vindt het te duur."),
        tabel("Is dit koopmotief van de klant rationeel of emotioneel?",
              [("dagelijks woon-werkverkeer", "rationeel"), ("niet bezweet aankomen", "emotioneel"), ("besparen op brandstof en parking", "rationeel"), ("de fiets in een mooie grijze kleur", "emotioneel")],
              "Een rationeel motief is een verstandige reden, een emotioneel motief een gevoelsreden.",
              kolommen=["rationeel", "emotioneel"]),
        keuze("In zin 7 [[*erkent|negeert]] de verkoper het bezwaar en legt hij de [[*waarde|prijs van de concurrent]] uit.",
              "Erkennen en dan antwoorden."),
        mk("Waarom stelt de verkoper in zin 9 meteen een afspraak voor?",
           ["Na een koopsignaal ga je naar de afsluiting.", "Hij wil vermijden dat de klant nog iets vraagt.", "Het gesprek duurde voor hem al te lang.", "Hij moet de fiets dringend kwijt uit het magazijn."], 0,
           "De klant is er klaar voor; nog meer uitleg kan nieuwe twijfel wekken."),
    ]),
    volgorde("Zet de fasen van een verkoopgesprek in de juiste volgorde.",
             ["de aandacht van de klant trekken", "een behoefte ontwikkelen", "argumenten geven", "bezwaren weerleggen", "koopsignalen ontdekken", "de aankoop afsluiten"],
             "Eerst de behoefte kennen, dan pas argumenten."),
    sorteer("Rationeel of emotioneel koopmotief?", ["rationeel", "emotioneel"],
            [("de garantie van drie jaar", "rationeel"), ("erbij willen horen", "emotioneel"), ("het lage verbruik", "rationeel"), ("het laatste nieuwe model van een bekend merk", "emotioneel"), ("de prijs", "rationeel"), ("iets gewoon mooi vinden", "emotioneel")],
            "Status, mode en erbij willen horen zijn gevoelsredenen."),
    tabel("Hoe ga je om met dit soort klant?",
          [("een stille klant", "open vragen stellen"), ("een veeleisende klant", "rustig en eerlijk blijven"), ("een klant die veel weet", "zijn kennis erkennen en aanvullen"), ("een twijfelende klant", "twee of drie duidelijke opties tonen")],
          "Elke klant vraagt een andere aanpak.",
          kolommen=["open vragen stellen", "rustig en eerlijk blijven", "zijn kennis erkennen en aanvullen", "twee of drie duidelijke opties tonen"]),
    tabel("Open of gesloten vraag?",
          [("Wilt u dit model?", "gesloten"), ("Waarvoor gaat u de laptop gebruiken?", "open"), ("Is zwart goed?", "gesloten"), ("Wat vindt u belangrijk aan een jas?", "open")],
          "Een open vraag vraagt om uitleg.",
          kolommen=["open", "gesloten"]),
    keuze("Een goede verkoper [[*luistert meer dan hij praat|praat meer dan hij luistert]]: zonder te weten wat de klant zoekt, is elk argument een gok.",
          "Vragen stellen en luisteren, zeker in het begin."),
    mk("Een klant zegt: \"Ik kom gewoon even kijken.\" Wat doe je?",
       ["Je laat hem kijken en zegt dat je er bent.", "Je volgt hem overal in de winkel om te helpen.", "Je somt meteen alle acties van deze week op.", "Je laat hem verder helemaal links liggen."], 0,
       "Je blijft beschikbaar zonder druk te zetten."),
    tabel("Is dit een koopsignaal?",
          [("Hoe lang is de garantie?", J), ("Bestaat hij ook in het blauw?", J), ("Ik kijk alleen wat rond.", F), ("Kan u hem volgende week leveren?", J)],
          "Wie naar garantie, kleur of levering vraagt, denkt al aan kopen."),
    keuze("Een klant die een bezwaar geeft, is vaak [[*geïnteresseerd|ongeïnteresseerd]]: wie niet wil kopen, neemt niet de moeite om tegen te spreken.",
          "Een bezwaar is een kans."),
    tabel("Hoe reageer je op het bezwaar \"Het is te duur\"?",
          [("de waarde uitleggen", J), ("een goedkoper alternatief tonen", J), ("vragen waarmee hij vergelijkt", J), ("doen alsof je het niet hoorde", F)],
          "Een bezwaar negeer je nooit; je erkent het en antwoordt eerlijk."),
    koppel("Welk begrip uit het verkoopgesprek past bij deze omschrijving?",
           [("koopmotief", "de reden waarom iemand iets koopt"), ("bezwaar", "een tegenargument van de klant"), ("koopsignaal", "een teken dat de klant wil kopen"), ("afsluiting", "het laatste deel waarin de klant beslist")],
           ["doelgroep"], "Vier begrippen uit het verkoopgesprek."),
    mk("Waarom past een verkoper zijn argumenten aan het koopmotief aan?",
       ["Elke klant vindt iets anders belangrijk.", "Dan hoeft hij geen vragen meer te stellen.", "Zo kan hij de prijs gewoon verhogen.", "Dat is verplicht volgens het arbeidsreglement."], 0,
       "Wie om zuinigheid geeft, hoort iets anders dan wie om design geeft."),
    tabel("Klopt dit over het verkoopgesprek?",
          [("Een klant kan meerdere koopmotieven tegelijk hebben.", J), ("Argumenten geef je best voor je de behoefte kent.", F), ("Wie te lang doorpraat na een koopsignaal, kan de verkoop verliezen.", J), ("Druk zetten levert een klant op die later afbelt.", J)],
          "De behoefte komt vóór de argumenten."),
    tabel("Hoort dit bij een goede afsluiting?",
          [("de afspraak bevestigen", J), ("de levering regelen", J), ("de klant bedanken", J), ("de klant onder druk zetten", F)],
          "Je maakt de afspraak concreet en bevestigt wat er geleverd wordt."),
    sleep("Mode en status zijn [[emotionele]] koopmotieven. De garantie en het verbruik zijn [[rationele]] koopmotieven.",
          ["verplichte", "collectieve"], "Gevoel tegenover verstand."),
    open_("Je observeert een verkoopgesprek waarin de verkoper meteen tien laptops toont, zonder vragen te stellen. Wat zou jij anders doen?",
          "Eerst open vragen stellen om de behoefte te kennen: waarvoor dient de laptop, wat mag hij kosten. Daarna twee of drie passende modellen tonen met argumenten die bij die behoefte horen, in plaats van tien.",
          "Een gesprek beoordeel je op luisteren, behoefte en bezwaren."),
    keuze("Een twijfelende klant help je met [[*twee of drie|tien of meer]] duidelijke opties.",
          "Te veel keuze maakt twijfel groter."),
    inv("Hoe noem je het teken dat een klant wil kopen? Schrijf één woord.", ["koopsignaal", "een koopsignaal", "koopsignalen"],
        "Een koopsignaal."),
    mk("Een stagiair kijkt een dag mee met een ervaren verkoopster. Wat haalt hij daar vooral uit?",
       ["Hij leert wat werkte en wat beter kon.", "Hij kan de klanten later zelf opbellen.", "Hij kent zo de exacte omzet van de dag.", "Hij mag dan elke afsluiting overnemen."], 0,
       "Je ziet wat je zelf anders zou doen."),
    casus("Lees de situatie.\n\nIn een gsm-winkel komt een klant binnen die meteen zegt: \"Ik wil de nieuwste gsm met de beste camera, zoals al mijn vrienden hebben. Hij moet ook twee dagen meegaan op één lading, want ik ben veel onderweg.\"", [
        tabel("Welk soort koopmotief zit in deze wens van de gsm-klant?",
              [("de nieuwste, zoals al zijn vrienden", "emotioneel"), ("twee dagen op één lading", "rationeel"), ("de beste camera om mee uit te pakken", "emotioneel")],
              "Erbij willen horen en status zijn gevoelsredenen; de batterij is een verstandige reden.",
              kolommen=["rationeel", "emotioneel"]),
        keuze("Deze klant heeft [[*meerdere koopmotieven tegelijk|geen enkel koopmotief]].",
              "Een gsm kan tegelijk mooi en praktisch moeten zijn."),
    ]),
    keuze("Bij een veeleisende klant neem je zijn vraag [[*ernstig|licht op]] en zeg je eerlijk wat kan en wat niet.",
          "Rustig en duidelijk blijven."),
    mk("Wanneer geef je best je argumenten?",
       ["nadat je de behoefte van de klant kent", "meteen bij het begin van het gesprek", "pas na de afsluiting van de verkoop", "enkel als de klant er zelf om vraagt"], 0,
       "Anders praat je over zaken waar de klant niets aan heeft."),
    tabel("Is dit een teken van een goed verkoopgesprek?",
          [("er is goed geluisterd", J), ("de behoefte is gevonden", J), ("de bezwaren zijn weerlegd", J), ("er werd veel druk gezet", F)],
          "Druk zetten is geen teken van een goed gesprek."),
]

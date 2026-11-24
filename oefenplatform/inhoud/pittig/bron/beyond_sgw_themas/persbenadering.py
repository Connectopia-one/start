"""Persoonlijkheid: van Freud over Bandura naar Rogers — pittig
(🌍 Beyond doorstroom, sociale en gedragswetenschappen). Eigen vragen en een eigen
tekening van de bewustzijnsniveaus, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# De bewustzijnsniveaus als ijsberg ------------------------------------------------------
IJ = Prent("bewustzijn-ijsberg", "De bewustzijnsniveaus als een ijsberg", "een ijsberg in het water: het kleine topje boven het water is A, het deel net onder de waterlijn is B, het grote diepe deel onderaan is C")
IJ.rect(60, 190, 880, 430, "#dde8ef", "none", 0, 0)
IJ.lijn(60, 190, 940, 190, "#6d8fa3", 3)
IJ.pad("M430 190 L470 90 L520 70 L560 120 L590 190 Z", "#ffffff", DONKER, 2)
IJ.pad("M430 190 L590 190 L660 280 L340 280 Z", "#f4f7f9", DONKER, 2)
IJ.pad("M340 280 L660 280 L760 420 L700 580 L300 590 L240 430 Z", "#eaf0f4", DONKER, 2)
IJ.letter(510, 150, "A")
IJ.letter(500, 240, "B")
IJ.letter(500, 440, "C")
NIVEAU = {"A": [Prent.zone(440, 70, 150, 120)], "B": [Prent.zone(350, 192, 300, 86)],
          "C": [Prent.zone(260, 282, 480, 300)]}

VRAGEN = [
    klik("Klik op het niveau waar volgens Freud verdrongen herinneringen terechtkomen.", IJ.bestand, NIVEAU["C"],
         "Verdringing duwt iets te pijnlijks naar het onbewuste."),
    klik("Klik op het niveau met wat je nu niet denkt, maar wel kan oproepen.", IJ.bestand, NIVEAU["B"],
         "Het voorbewuste of onderbewuste ligt net onder de waterlijn."),
    klik("Klik op het niveau waar je je nu van bewust bent.", IJ.bestand, NIVEAU["A"],
         "Het bewuste is maar het kleine topje."),
    met_prent(IJ.bestand, mk("Waarom tekent men de bewustzijnsniveaus van Freud als een ijsberg?",
              ["het grootste deel is onbewust",
               "het bewuste is het grootste deel",
               "de drie niveaus zijn precies even groot",
               "het onbewuste ligt boven het water"], 0,
              "Het onbewuste is groot, onzichtbaar en stuurt toch mee.")),
    met_prent(IJ.bestand, keuze("Het Es werkt grotendeels op niveau [[*C|A|B]].",
              "Het Es werkt grotendeels in het onbewuste.")),
    tabel("Es, Ich of Über-ich?", [
        ("'Ik wil dat nu, meteen!'", "Es"),
        ("'Dat hoort niet, schaam je.'", "Über-ich"),
        ("'Ik wacht tot de pauze om te eten.'", "Ich"),
        ("volgt het moraliteitsprincipe", "Über-ich"),
    ], "Lustprincipe, moraliteitsprincipe en realiteitsprincipe.", kolommen=["Es", "Ich", "Über-ich"]),
    koppel("Koppel elk deel aan zijn principe.", [
        ["Es of Id", "lustprincipe"],
        ["Ich of Ego", "realiteitsprincipe"],
        ["Über-ich of Superego", "moraliteitsprincipe"],
    ], ["gelijkheidsprincipe"], "Drie delen van de persoonlijkheidsstructuur."),
    keuze("De levensdrift heet bij Freud [[*eros|thanatos]], de doodsdrift [[*thanatos|eros]].",
          "Beide drifts zitten volgens Freud in het Es."),
    casus(
        "Wout staat in een winkel en heeft zin om een dure koptelefoon mee te nemen zonder te betalen. "
        "Een stemmetje zegt dat dat niet mag. Uiteindelijk spaart hij twee maanden en koopt hij ze dan. "
        "Later weet hij niet meer dat hij als kind ooit betrapt werd op stelen, al voelt hij zich in winkels altijd wat onrustig.",
        [
            keuze("De zin om ze mee te nemen komt van het [[*Es|Ich|Über-ich]].",
                  "Het Es wil nu wat het wil: lustprincipe."),
            keuze("Het stemmetje dat zegt dat het niet mag, is het [[*Über-ich|Es|Ich]].",
                  "Het geweten volgt het moraliteitsprincipe."),
            keuze("Sparen en later kopen is het werk van het [[*Ich|Es|Über-ich]].",
                  "Het Ich zoekt wat haalbaar is in de echte wereld."),
            inv("Hoe heet het afweermechanisme waardoor hij die kinderherinnering niet meer weet?", ["verdringing", "verdringen"],
                "Wat te pijnlijk is, wordt naar het onbewuste geduwd en werkt daar door."),
        ],
    ),
    tabel("Interne of externe locus of control?", [
        ("'Ik slaagde omdat ik elke dag studeerde.'", "intern"),
        ("'Die leerkracht heeft het op mij gemunt.'", "extern"),
        ("'Met geluk win je zo'n wedstrijd.'", "extern"),
        ("'Als ik vroeger begin, haal ik mijn deadline wel.'", "intern"),
    ], "Bij een interne locus heb je je leven zelf in handen.", kolommen=["intern", "extern"]),
    keuze("Een interne locus of control gaat vaak samen met [[*meer eigen initiatief|minder inzet|meer pech]].",
          "Wie denkt dat zijn inzet verschil maakt, zet ook eerder iets in gang."),
    mk("Ilias gelooft dat hij de fietsproef haalt en oefent elke dag. Hij slaagt. Hoe verklaar je dat met Bandura?",
       ["zijn geloof deed hem doorzetten",
        "wie gelooft dat hij het kan, hoeft niet meer te oefenen",
        "wie twijfelt aan zichzelf, krijgt altijd meer hulp",
        "wie gelooft dat hij het kan, zit in de comfortzone vast"], 0,
       "Het geloof stuurt het gedrag, en het gedrag het resultaat."),
    sleep("Bij Bandura beïnvloeden [[persoon]], [[omgeving]] en gedrag elkaar alle drie. Dat heet wederzijds determinisme.",
          ["toeval", "geweten"], "Drie pijlen in twee richtingen."),
    koppel("Koppel elke naam aan zijn begrip.", [
        ["Freud", "Es, Ich en Über-ich"],
        ["Bandura", "zelfeffectiviteit"],
        ["Rotter", "locus of control"],
        ["Rogers", "fenomenale veld"],
    ], ["arousal"], "Psychodynamisch, sociaal-cognitief en humanistisch."),
    tabel("Klopt dit over Rogers?", [
        ("Het actuele zelf is wie je nu bent.", J),
        ("Incongruentie is een grote afstand tussen actueel en ideaal zelf.", J),
        ("Twee mensen in dezelfde kamer hebben altijd hetzelfde fenomenale veld.", F),
        ("Onvoorwaardelijke aanvaarding maakt incongruentie groter.", F),
    ], "Aanvaarding helpt om dichter bij je actuele zelf te durven staan."),
    casus(
        "Sara ziet zichzelf als iemand die stil en onhandig is. Ze zou graag een zelfzekere zangeres zijn. "
        "Ze voelt zich daardoor vaak ongelukkig. Haar zangleraar aanvaardt haar zoals ze is en wijst haar op wat al goed gaat. "
        "Na een jaar zegt Sara: 'Ik ben misschien geen ster, maar ik zing graag en dat is goed genoeg.'",
        [
            tabel("Welk begrip van Rogers past?", [
                ("stil en onhandig, zoals ze zichzelf nu ziet", "actuele zelf"),
                ("een zelfzekere zangeres", "ideale zelf"),
                ("de grote afstand tussen die twee", "incongruentie"),
            ], "Wie je bent, wie je wil zijn, en de kloof ertussen.",
               kolommen=["actuele zelf", "ideale zelf", "incongruentie"]),
            keuze("Na een jaar is er meer [[*congruentie|incongruentie]].",
                  "Haar actuele en ideale zelf passen beter bij elkaar."),
            mk("Wat hielp volgens Rogers het meest?",
               ["de onvoorwaardelijke aanvaarding",
                "een strenger Über-ich bij Sara",
                "een externe locus of control",
                "beloning voor elk goed lied"], 0,
               "Wie zich aanvaard voelt, durft dichter bij zichzelf te staan."),
        ],
    ),
    keuze("Zelfactualisatie betekent [[*worden wie je ten volle kan zijn|beter zijn dan anderen|al je wensen meteen vervullen]].",
          "Je mogelijkheden waarmaken."),
    mk("Wat is het grote verschil tussen Freud en Rogers?",
       ["conflict binnenin tegenover groei",
        "geloof in jezelf tegenover toeval",
        "het brein tegenover de cultuur",
        "beloning tegenover straf"], 0,
       "De psychodynamische benadering ziet conflict, de humanistische groei."),
    inv("Hoeveel bewustzijnsniveaus onderscheidt Freud? Schrijf het getal.", ["3", "drie"],
        "Het onbewuste, het voorbewuste en het bewuste."),
    keuze("Het Über-ich ontstaat volgens Freud onder andere door [[*wat ouders en opvoeders meegeven|de genen van de grootouders|het realiteitsprincipe]].",
          "Normen van opvoeders worden het eigen geweten."),
    inv("Hoe heet de wereld zoals iemand die zelf ervaart, volgens Rogers? Vul aan: het ... veld.", ["fenomenale", "fenomenaal"],
        "Rogers vertrekt van hoe iemand de wereld beleeft."),
    tabel("Welke benadering van persoonlijkheid?", [
        ("conflict tussen Es en Über-ich", "psychodynamisch"),
        ("zelfeffectiviteit", "sociaal-cognitief"),
        ("incongruentie", "humanistisch"),
        ("locus of control", "sociaal-cognitief"),
    ], "Freud, Bandura en Rotter, Maslow en Rogers.",
       kolommen=["psychodynamisch", "sociaal-cognitief", "humanistisch"]),
    keuze("Noa zegt na een geslaagd examen 'ik had geluk'. Ze heeft een [[*externe|interne]] locus of control.",
          "Ze legt de oorzaak buiten zichzelf."),
    keuze("Bij Rotter is een locus of control een [[*vrij stabiele eigenschap|stemming van het moment|deel van het Es]].",
          "Ze wisselt niet volledig van situatie tot situatie."),
    open_("Leg uit hoe zelfeffectiviteit en een interne locus of control samen kunnen helpen bij het studeren voor een moeilijk examen.",
          "Wie gelooft dat hij de leerstof kan beheersen (zelfeffectiviteit), zet door bij moeilijke stukken. Wie denkt dat zijn resultaat afhangt van zijn eigen inzet (interne locus of control), begint op tijd en plant zelf. Samen leidt dat vaker tot slagen."),
]

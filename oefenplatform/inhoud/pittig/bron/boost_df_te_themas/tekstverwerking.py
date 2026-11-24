"""Tekstverwerking: klavier, opmaak en stijlen — pittig (🛠️ Boost dubbele finaliteit, toegepaste economie).

Pittige vragen uit Samenleving en economie Beyond (beyond_se_themas/word.py) die
binnen te_tekstverwerking vallen, met de bladzijde om op te klikken, aangevuld
met eigen vragen over het klavier, stijlen en sjablonen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ..beyond_se_themas import word as _w

VRAGEN = [_w.VRAGEN[i] for i in (0, 1, 2, 3, 6, 8, 10, 11, 12, 15, 18, 20, 26)] + [
    koppel("Welke sneltoets hoort bij welke opdracht?",
           [("ctrl + c", "kopiëren"), ("ctrl + v", "plakken"), ("ctrl + x", "knippen"), ("ctrl + a", "alles selecteren"), ("ctrl + z", "ongedaan maken")],
           ["afdrukken"], "Met sneltoetsen blijven je handen op het klavier."),
    tabel("Welke toets doet dit?",
          [("het teken links van de cursor wissen", "backspace"), ("het teken rechts van de cursor wissen", "delete"), ("naar het begin van de regel springen", "home"), ("wisselen tussen invoegen en overschrijven", "insert")],
          "Backspace wist naar links, delete naar rechts.",
          kolommen=["backspace", "delete", "home", "insert"]),
    keuze("Het euroteken en het apenstaartje typ je met de toets [[*alt gr|shift|caps lock]].",
          "Alt gr geeft het derde teken op een toets."),
    mk("Je wil de naam Janssens overal in een verslag van veertig bladzijden vervangen door Jansen. Wat gebruik je?",
       ["zoeken en vervangen", "de spellingcontrole", "een nieuwe stijl", "de knop alles weergeven"], 0,
       "Zoeken en vervangen wijzigt een woord in één keer door het hele document."),
    tabel("Stijl of sjabloon?",
          [("een voorbereid factuurdocument dat je enkel nog invult", "sjabloon"), ("een set opmaakkenmerken voor alle titels", "stijl"), ("een kant-en-klare sollicitatiebrief met vaste opbouw", "sjabloon"), ("Kop 1 met lettertype, grootte en kleur", "stijl")],
          "Een sjabloon is een voorbereid document, een stijl een set opmaak erin.",
          kolommen=["stijl", "sjabloon"]),
    mk("Je geeft twintig titels met de hand vet, blauw en 16 punt. Je baas wil ze toch groen. Wat had je beter gedaan?",
       ["een stijl gebruikt", "elke titel apart gekopieerd", "de titels als afbeelding ingevoegd", "de marges groter gezet"], 0,
       "Wijzig je de stijl, dan volgen alle titels meteen mee."),
    keuze("Met de knop Alles weergeven zie je [[*spaties, tabs en alineamarkeringen|alle afbeeldingen groter|de verborgen bladzijden]].",
          "Zo zie je waar de opmaak vandaan komt."),
    keuze("Een tab springt naar [[*een vaste positie|een willekeurige plaats]]; met spaties schuift alles scheef zodra je iets wijzigt.",
          "Gebruik tabs om netjes uit te lijnen."),
    tabel("Teken-, alinea- of paginaopmaak?",
          [("superscript", "teken"), ("de regelafstand", "alinea"), ("de marges", "pagina"), ("doorhalen", "teken"), ("een opsommingsteken", "alinea"), ("kolommen", "pagina")],
          "Tekenopmaak werkt op letters, alineaopmaak op hele alinea's, paginaopmaak op de bladzijde.",
          kolommen=["teken", "alinea", "pagina"]),
    keuze("Met een [[*sectie|stijl|tab]] kan één bladzijde liggend staan terwijl de rest staand blijft.",
          "Elke sectie heeft een eigen paginaopmaak."),
    sorteer("Commercieel document of personeelsdocument?", ["commercieel", "personeel"],
            [("een factuur", "commercieel"), ("een vacature", "personeel"), ("verkoopvoorwaarden", "commercieel"), ("een cv", "personeel"), ("een label voor een product", "commercieel"), ("een sollicitatiebrief", "personeel")],
            "Allebei maak je met een tekstverwerker."),
    tabel("Klopt dit over de tekstverwerker?",
          [("Paginanummers typ je met de hand op elke bladzijde.", F), ("Een kop- en voettekst herhaalt zich op elke bladzijde van de sectie.", J), ("Met shift typ je één hoofdletter.", J), ("De toets insert maakt een nieuw document.", F)],
          "Paginanummers voeg je één keer in. Een nieuw document is ctrl + n."),
    sleep("De witruimte rond de tekst op een blad heet de [[marge]]. Tekst onderaan elke bladzijde is de [[voettekst]].",
          ["koptekst", "sjabloon"], "Twee begrippen uit de paginaopmaak."),
    mk("Waarom zet een krant of een folder tekst in kolommen?",
       ["Smallere regels lezen vlotter.", "Zo past er minder tekst op het blad.", "Zo hoeft er geen marge te zijn.", "Kolommen vervangen de titels."], 0,
       "De tekst loopt in banen, zoals in een krant."),
]

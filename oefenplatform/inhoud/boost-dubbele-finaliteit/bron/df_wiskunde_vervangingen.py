# -*- coding: utf-8 -*-
"""De vragen die bij dubbele finaliteit anders moeten dan bij doorstroom.

De sleutel is de vráág van de doorstroomversie, woord voor woord.
`bouw_wiskunde.py` zoekt ze op en zet er deze vraag voor in de plaats; staat
een sleutel niet (meer) in de doorstroombestanden, dan stopt het script.

Het zijn er zeven. Het grote verschil tussen de twee fiches zit niet in losse
vragen maar in hele thema's: logica valt weg, en goniometrie, stelsels,
grafisch oplossen en misleiding zijn hier opnieuw geschreven (zie
`widf_*.py`). Wat overblijft:

  * **ICT-vaardigheid.** De DF-fiche noemt het online rekentoestel en de
    rekenapps, en zegt er uitdrukkelijk bij: "We staan geen andere
    ICT-middelen toe tijdens het examen." GeoGebra hoort daar dus niet bij.
  * **Wetenschappelijke notatie.** Die staat niet op de DF-fiche. Machten van
    tien wél, en die vragen blijven staan; de zes vragen die de notatie als
    begrip aanleren, zijn vervangen door leerstof die er wel op staat: de
    vormen van een getal en de intervalnotatie.

Elke vervanging houdt hetzelfde type, en bij waar of niet waar dezelfde
waarheidswaarde, zodat het evenwicht per hoofdstuk blijft kloppen.
"""

VERVANGINGEN = {
    # ── Een opgave aanpakken — deel 1
    "Welke vaardigheid noemt de fiche bij ICT-vaardigheid?": dict(
        type="meerkeuze",
        vraag="Welk hulpmiddel mag je op het examen gebruiken bij ICT-vaardigheid?",
        opties=[
            "het online rekentoestel en de rekenapps",
            "een verslag typen in een tekstverwerker",
            "je oplossing opzoeken op een website",
            "een grafiek fotograferen met je telefoon",
        ],
        antwoord=0,
        uitleg="Andere ICT-middelen zijn niet toegelaten. ICT is hulp bij het rekenen en het "
               "tekenen, geen vervanging van de redenering.",
    ),
    # ── Ordenen, afronden en intervallen — deel 2
    "Wat is de wetenschappelijke notatie van 45 000?": dict(
        type="meerkeuze",
        vraag="Hoe schrijf je de breuk 3 op 4 als procent?",
        opties=["75 procent", "34 procent", "0,75 procent", "7,5 procent"],
        antwoord=0,
        uitleg="3 gedeeld door 4 is 0,75, en 0,75 maal honderd is 75. Een procent is niets "
               "anders dan een breuk met honderd als noemer.",
    ),
    "Wat is de wetenschappelijke notatie van 0,00072?": dict(
        type="meerkeuze",
        vraag="Hoe schrijf je 0,125 als breuk in zijn eenvoudigste vorm?",
        opties=["1 op 8", "125 op 100", "1 op 4", "12 op 100"],
        antwoord=0,
        uitleg="0,125 is 125 op 1000. Teller en noemer allebei door 125 delen geeft 1 op 8.",
    ),
    "Welke van deze notaties is géén correcte wetenschappelijke notatie?": dict(
        type="meerkeuze",
        vraag="Welke van deze intervalnotaties klopt niet?",
        opties=["[5, 2]", "[2, 5]", "]2, 5]", "]2, +oneindig["],
        antwoord=0,
        uitleg="Een interval loopt altijd van de kleinste grens naar de grootste. [5, 2] "
               "beschrijft dus niets; dat moet [2, 5] zijn.",
    ),
    "In de wetenschappelijke notatie staat er precies één cijfer voor de komma, van 1 tot en met 9.": dict(
        type="waarofniet",
        vraag="Op een getallenas staat een groter getal altijd rechts van een kleiner getal.",
        antwoord=True,
        uitleg="Dat is precies waarvoor een getallenas dient: de volgorde wordt een plaats. "
               "Ook bij negatieve getallen geldt het, en daar verrast het vaak.",
    ),
    "Een negatieve exponent in de wetenschappelijke notatie betekent dat het getal negatief is.": dict(
        type="waarofniet",
        vraag="Het interval ]2, 5] bevat het getal 2.",
        antwoord=False,
        uitleg="Het haakje wijst bij de 2 naar buiten, dus die grens telt niet mee. De 5 wel: "
               "daar wijst het haakje naar binnen.",
    ),
    "Schrijf 6 200 000 in wetenschappelijke notatie. Typ bijvoorbeeld 3,4 x 10^5.": dict(
        type="invultekst",
        vraag="Hoe noem je een interval waarvan allebei de grenzen meetellen?",
        antwoord=["een gesloten interval", "gesloten interval", "gesloten"],
        uitleg="Bij een gesloten interval wijzen allebei de haakjes naar binnen: [2, 5]. "
               "Wijst er één naar buiten, dan is het halfopen.",
    ),
}

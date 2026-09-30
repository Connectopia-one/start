# -*- coding: utf-8 -*-
"""De vragen die bij dubbele finaliteit anders moeten dan bij doorstroom.

De sleutel is de vráág van de doorstroomversie, woord voor woord.
`bouw_nederlands.py` zoekt ze op en zet er deze vraag voor in de plaats; staat
een sleutel niet (meer) in de doorstroombestanden, dan stopt het script. Zo kan
een aanpassing aan de doorstroomvragen hier nooit stil voorbijgaan.

Het zijn er maar drie. Dat komt doordat het grote verschil tussen de twee
fiches niet in losse vragen zit maar in hele thema's: argumenteren, literatuur
en communiceren zijn hier opnieuw geschreven (zie `nldf_*.py`). Wat overblijft,
is de vormenlijst van de humor. De DF-fiche noemt er drie, ironie, overdrijving
en woordspeling, en kent parodie en taalhumor niet.

Elke vervanging houdt hetzelfde type en, bij meerdere juiste antwoorden, ook
dat er meerdere zijn, zodat de verhoudingen per hoofdstuk blijven kloppen.
"""

VERVANGINGEN = {
    # ── Betekenis, beeldspraak en gevoelswaarde — deel 2
    "Welke van deze horen bij de vormen van humor?": dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij de vormen van humor?",
        opties=[
            "ironie",
            "overdrijving",
            "een woordspeling",
            "een metafoor",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een metafoor is beeldspraak, geen humor. De fiche zet die twee in aparte lijstjes.",
    ),
    "Hoe noem je een grappige nabootsing van een bekende stijl of een bekend werk?": dict(
        type="invultekst",
        vraag="Hoe noem je een grapje dat steunt op de dubbele betekenis van een woord?",
        antwoord=["een woordspeling", "woordspeling"],
        uitleg="Een woordspeling werkt enkel als de lezer allebei de betekenissen tegelijk hoort.",
    ),
    "Wat is taalhumor?": dict(
        type="meerkeuze",
        vraag="Een krant schrijft over 'dat krot' waar gewoon een oud huis staat. Wat is dat?",
        opties=[
            "een dysfemisme",
            "een eufemisme",
            "een synoniem",
            "een antoniem",
        ],
        antwoord=0,
        uitleg="Een dysfemisme kiest een harder woord dan nodig. Een eufemisme doet het omgekeerde en verzacht.",
    ),
}

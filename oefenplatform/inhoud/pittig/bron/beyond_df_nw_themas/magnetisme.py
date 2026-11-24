"""Elektromagnetisme — pittig (Beyond dubbele finaliteit, natuurwetenschappen).

Pittige vragen fysica Beyond over magneten en het veld van draad en spoel (zonder formules), plus eigen vragen binnen nwd_magnetisme."""
from ..beyond_fys_themas import magneet as M
from ..beyond_fys_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(M.VRAGEN, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 19, 20, 23, 24, 25, 26, 27]) + [
    casus(
        "Een elektrische deurbel: als je op de knop duwt, sluit de kring. De stroom loopt door een spoel met een ijzeren kern. "
        "Die trekt een ijzeren hamertje aan, dat tegen een klankschaal slaat.",
        [
            keuze("Als je de knop loslaat, wordt de spoel [[*niet meer|nog sterker]] magnetisch.", "Een elektromagneet werkt alleen zolang er stroom loopt."),
            mk("Waarom zit er een ijzeren kern in de spoel?",
               ["Die maakt het magneetveld veel sterker.", "Die zorgt dat de stroom sneller door de spoel loopt.", "Die houdt de spoel koel tijdens het bellen.", "Die maakt het geluid van de bel luider."], 0,
               "De weissgebieden in het ijzer richten zich mee en versterken het veld."),
            keuze("Het hamertje is van ijzer, omdat ijzer [[*ferromagnetisch|niet magnetisch|elektrisch geladen]] is.", "Een hamertje van aluminium bleef liggen."),
        ],
    ),
    tabel("Is dit een permanente magneet of een elektromagneet?", [
        ("een bordmagneet op de koelkast", "permanent"), ("de magneet in een schrootkraan", "elektro"),
        ("een kompasnaald", "permanent"), ("de spoel in een relais", "elektro"),
    ], "Een elektromagneet heeft stroom nodig, een permanente magneet niet.", kolommen=["permanent", "elektro"]),
    mk("Waarom gebruikt een schrootkraan een elektromagneet?",
       ["Door de stroom uit te zetten valt het schroot los.", "Een elektromagneet trekt ook koper en aluminium aan.", "Een permanente magneet is te licht om schroot te tillen.", "Een elektromagneet werkt zonder elektriciteit."], 0,
       "Aan- en uitzetten is net het voordeel."),
    tabel("Wordt de elektromagneet hierdoor sterker?", [
        ("meer wikkelingen rond de spoel", J), ("een grotere stroom", J), ("een ijzeren kern in de spoel", J), ("de spoel een nacht in de koelkast leggen", F),
    ], "Wikkelingen, stroom en kern bepalen de sterkte."),
    keuze("De magnetische zuidpool van de aarde ligt bij de geografische [[*noordpool|zuidpool]].", "Daarom wijst de noordpool van een kompas naar het noorden."),
    mk("Een kompas ligt vlak naast een draad. Je zet de stroom aan en de naald draait. Wat bewijst dat?",
       ["Rond een stroomvoerende draad staat een magneetveld.", "De draad is van ijzer en dus ferromagnetisch.", "De naald is elektrisch geladen door de stroom.", "De stroom verwarmt de naald en doet die draaien."], 0,
       "Een stroom maakt een magneetveld."),
    koppel("Koppel elk toestel aan wat de elektromagneet erin doet.", [
        ["deurbel", "trekt een hamertje tegen een klankschaal"], ["relais", "zet met een kleine stroom een grote stroom aan"],
        ["luidspreker", "laat een conus heen en weer trillen"], ["automatische zekering", "onderbreekt de stroom als die te groot wordt"],
    ], ["laat een lamp feller branden"], "Telkens wordt een stroom omgezet in een kracht."),
    open_("Leg uit waarom je een stalen schroevendraaier magnetisch kan maken door er met een magneet langs te strijken, en hoe je dat weer ongedaan maakt.",
          "Door het strijken richten de weissgebieden in het staal zich in dezelfde zin, zodat de schroevendraaier zelf een magneet wordt. Door hem sterk te verhitten of er hard op te slaan raken de gebiedjes weer door elkaar.",
          "Magnetiseren richt de weissgebieden, demagnetiseren gooit ze weer door elkaar."),
]

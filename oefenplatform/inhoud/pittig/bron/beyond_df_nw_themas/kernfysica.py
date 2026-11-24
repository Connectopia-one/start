"""Kernfysica en ioniserende straling — pittig (Beyond dubbele finaliteit, natuurwetenschappen).

Pittige vragen natuurwetenschappen Beyond over kernen, verval, halfwaardetijd en bescherming binnen nwd_kernfysica, plus eigen vragen."""
from ..beyond_nw_themas import kernfysica as K
from ..beyond_fys_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(K.VRAGEN, [0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14, 16, 17, 19, 20, 22, 23, 25], {"halveringstijd": "halfwaardetijd"}) + [
    tabel("In welke categorie hoort dit radioactief afval?", [
        ("handschoenen uit een ziekenhuislabo, kortlevend en laagactief", "A"),
        ("verbruikte splijtstof uit een kerncentrale", "C"),
        ("afval dat lang radioactief blijft maar weinig warmte geeft", "B"),
    ], "A is het minst gevaarlijk, C het hoogactieve afval.", kolommen=["A", "B", "C"]),
    volgorde("Zet de stappen in een kerncentrale in de juiste volgorde.", [
        "uranium splijt in de reactor", "de warmte maakt stoom", "de stoom draait een turbine", "de generator maakt stroom",
    ], "De kernreactie maakt alleen warmte; de rest is zoals in een gewone centrale."),
    mk("Waarom duwt men bij een probleem de regelstaven dieper in de reactor?",
       ["Ze slorpen neutronen op en remmen de kettingreactie.", "Ze voegen extra uranium toe om de reactor te koelen.", "Ze maken de betonnen koepel dikker en dus sterker.", "Ze zetten de straling om in gewone warmte."], 0,
       "Minder vrije neutronen betekent minder splijtingen."),
    inv("Een kern heeft massagetal \\(60\\) en atoomnummer \\(27\\). Hoeveel neutronen heeft ze?", ["33", "drieëndertig"], "\\(60 - 27 = 33\\)."),
    keuze("De effectieve dosis in [[*sievert|gray|becquerel]] houdt rekening met de soort straling en met het weefsel.", "De gray meet enkel de geabsorbeerde energie."),
    mk("Twee bronnen geven evenveel energie af aan je lichaam, de ene alfa, de andere gamma. Welke effectieve dosis is groter?",
       ["die van de alfabron", "die van de gammabron", "ze zijn precies even groot", "dat hangt alleen af van je gewicht"], 0,
       "Alfastraling krijgt een hogere weegfactor."),
    tabel("Klopt dit over de halfwaardetijd?", [
        ("Na twee halfwaardetijden is er nog een kwart over.", J),
        ("Een lange halfwaardetijd betekent dat de stof snel onschadelijk is.", F),
        ("Na één halfwaardetijd is de helft van de kernen vervallen.", J),
    ], "Een lange halfwaardetijd betekent dat de stof lang straling blijft geven."),
    koppel("Koppel elke beschermingsmaatregel aan wat ze doet.", [
        ["jodiumpil", "vult de schildklier met gewoon jodium"], ["loodschort", "houdt röntgen- en gammastraling tegen"],
        ["afstand nemen", "verlaagt de dosis die je oploopt"], ["handschoenen en mondmasker", "voorkomt een besmetting"],
    ], ["maakt straling onschadelijk"], "Geen enkele maatregel maakt de straling zelf onschadelijk."),
    mk("Iemand werd bestraald bij een röntgenfoto. Is die persoon nu zelf radioactief?",
       ["Nee, de bron bleef buiten het lichaam.", "Ja, het lichaam geeft nog dagen straling af.", "Ja, maar alleen op de plaats van de foto.", "Nee, want röntgenstraling is niet ioniserend."], 0,
       "Bij bestraling blijft er geen radioactieve stof achter."),
]

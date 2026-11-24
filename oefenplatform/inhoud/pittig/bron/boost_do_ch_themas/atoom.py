"""De bouw van atomen en ionen — pittig (🚀 Boost doorstroom, chemie).

Klikvragen op het atoommodel en vragen over deeltjes, isotopen en massa van natuurwetenschappen Boost doorstroom (met de prent), plus eigen vragen uit ch_atoom."""
from ..boost_do_nw_themas import atoom as N
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(N.VRAGEN, [7, 8, 9, 10, 11, 12, 13, 14, 17, 19, 20, 21, 24, 26])
VRAGEN += [
    tabel("Vul de tabel aan: hoeveel deeltjes heeft dit atoom of ion?",
          [("³⁵Cl: aantal neutronen", "18"), ("Mg²⁺: aantal elektronen", "10"), ("²³Na: aantal protonen", "11"), ("O²⁻: aantal elektronen", "10")],
          "Neutronen = massagetal − atoomnummer; een positief ion heeft elektronen minder, een negatief ion meer.", ["10", "11", "18"]),
    mk("Een deeltje heeft 16 protonen, 16 neutronen en 18 elektronen. Wat is het?",
       ["een ion met lading 2−", "een neutraal atoom", "een ion met lading 2+", "een isotoop met lading 0"], 0,
       "Twee elektronen meer dan protonen: lading 2−. Het is het sulfide-ion."),
    keuze("De elektronenconfiguratie van aluminium (13 elektronen) is [[*2, 8, 3|2, 8, 2, 1|8, 2, 3]].",
          "De eerste schil 2, de tweede 8, de rest in de derde."),
    tabel("Klopt dit over de massa van een atoom?",
          [("Bijna de hele massa zit in de kern.", J), ("Een elektron is ongeveer even zwaar als een proton.", F), ("De relatieve atoommassa heeft geen eenheid.", J), ("De absolute massa druk je uit in u of in kilogram.", J)],
          "Een elektron is bijna tweeduizend keer lichter dan een proton."),
    inv("Hoeveel valentie-elektronen heeft fosfor, met 15 elektronen?", ["5", "vijf"],
        "Configuratie 2, 8, 5: vijf elektronen in de buitenste schil."),
    mk("Twee atomen hebben allebei 6 protonen, maar het ene heeft 6 en het andere 8 neutronen. Wat klopt?",
       ["Het zijn isotopen van koolstof.", "Het zijn twee verschillende elementen.", "Het tweede atoom is een ion.", "Het eerste atoom heeft een hoger atoomnummer."], 0,
       "Zelfde aantal protonen, zelfde element; enkel het massagetal verschilt."),
    sorteer("Welk deeltje is dit?", ["Proton", "Neutron", "Elektron"],
            [("positief geladen en in de kern", "Proton"), ("zonder lading en in de kern", "Neutron"), ("negatief geladen en rond de kern", "Elektron"), ("bepaalt het atoomnummer", "Proton"), ("zorgt voor binding met andere atomen", "Elektron")],
            "Protonen bepalen welk element het is, elektronen hoe het reageert."),
    mk("Waarom is een atoom als geheel neutraal?",
       ["Het heeft evenveel protonen als elektronen.", "Het heeft evenveel neutronen als protonen.", "De kern van een atoom heeft geen lading.", "De elektronen in de schillen hebben geen lading."], 0,
       "De positieve en negatieve ladingen heffen elkaar op."),
    inv("Een atoom heeft massagetal 27 en 14 neutronen. Wat is het atoomnummer?", ["13", "dertien"],
        "Atoomnummer = massagetal − neutronen = 27 − 14 = 13: aluminium."),
    tabel("Klopt dit over het atoommodel van Bohr?",
          [("De elektronen bewegen in schillen rond de kern.", J), ("De derde schil kan bij de eerste achttien elementen 8 elektronen bevatten.", J), ("De kern bestaat uit elektronen en neutronen.", F)],
          "De kern bevat protonen en neutronen; de elektronen zitten in schillen."),
    sleep("Het [[atoomnummer]] geeft het aantal protonen. Het [[massagetal]] is de som van protonen en neutronen. Atomen met evenveel protonen maar een ander aantal neutronen zijn [[isotopen]].",
          ["ionen", "valentie-elektronen"], "Drie begrippen om een atoom te beschrijven."),
    mk("Een ion heeft 10 elektronen en lading 1+. Hoeveel protonen heeft het?",
       ["11", "10", "9", "1"], 0,
       "Bij lading 1+ is er één elektron te weinig: 11 protonen, natrium."),
    mk("Waarom staat een atoom met configuratie 2, 8, 1 makkelijk een elektron af?",
       ["Dan houdt het een volle buitenste schil over.", "Dan krijgt het meer protonen in de kern.", "Dat ene elektron is zwaarder dan de andere.", "Dan wordt het een negatief geladen ion."], 0,
       "Na het afgeven blijft 2, 8 over: zoals het edelgas neon."),
]

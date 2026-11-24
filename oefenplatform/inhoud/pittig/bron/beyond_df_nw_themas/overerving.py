"""Overerving van kenmerken — pittig (Beyond dubbele finaliteit, natuurwetenschappen).

Pittige vragen biologie Beyond (zelfde prenten), enkel wat in nwd_overerving staat, plus eigen vragen."""
from ..beyond_bio_themas import overerving as O, celdeling as C, mutaties as M
from ..beyond_bio_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

_V = {"In de F2 van een monohybride kruising": "In de F2 van een kruising Aa x Aa",
      "Hoeveel chromatiden heeft de cel na de S-fase?": "Hoeveel chromatiden heeft de cel nadat het DNA verdubbeld is?"}

VRAGEN = (kies(O.VRAGEN, [0, 1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 15, 19, 21, 23, 24, 25, 26, 27], _V)
          + kies(C.VRAGEN, [7, 10, 24], _V) + kies(M.VRAGEN, [8], _V)) + [
    tabel("Klopt dit over de chromosomen van de mens?", [
        ("Een lichaamscel heeft 46 chromosomen.", J), ("Een zaadcel is diploïd.", F),
        ("Een vrouw heeft twee X-chromosomen.", J), ("Op een karyogram staan de chromosomen per paar.", J),
    ], "Geslachtscellen zijn haploïd: 23 chromosomen."),
    mk("De ziekte van Huntington erft dominant over. Een vader is heterozygoot en ziek, de moeder is gezond. Hoe groot is de kans dat een kind de ziekte erft?",
       ["50 %", "25 %", "75 %", "100 %"], 0, "Hh x hh: de helft krijgt H."),
    mk("Twee gezonde ouders krijgen een kind met mucoviscidose, een recessieve aandoening. Wat weet je over de ouders?",
       ["Ze zijn allebei drager.", "Eén van hen is zelf ziek.", "Het kind heeft een nieuwe mutatie.", "Ze zijn allebei homozygoot gezond."], 0,
       "Het kind kreeg van elke ouder een recessief allel."),
    open_("Leg uit waarom een mutatie in een huidcel niet aan je kinderen doorgegeven wordt.",
          "De mutatie zit enkel in die huidcel en haar dochtercellen. Je kinderen ontstaan uit een eicel en een zaadcel, en daarin zit die mutatie niet.",
          "Alleen mutaties in geslachtscellen zijn erfelijk."),
]

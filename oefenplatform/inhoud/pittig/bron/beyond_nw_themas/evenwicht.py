"""Chemisch evenwicht — pittig (🌍 Beyond doorstroom, natuurwetenschappen).

Deels overgenomen uit de pittige vragen chemie Beyond (zelfde leerstof,
zelfde prenten), enkel wat binnen de gewone hoofdstukken natuurwetenschappen
valt (geen evenwichtsconstante), aangevuld met eigen vragen.
"""
from ..beyond_chem_themas import evenwicht as E
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

OVER = [E.VRAGEN[i] for i in (0, 1, 2, 3, 4, 8, 12, 13, 16, 18, 19, 20, 24, 26)]

EIGEN = [
    casus(
        "In een proefbuis staat het evenwicht Fe³⁺ + SCN⁻ ⇌ FeSCN²⁺. De ijzerionen zijn lichtgeel, de thiocyanaationen kleurloos en het product FeSCN²⁺ bloedrood. "
        "Je verdeelt de oplossing over drie buisjes.",
        [
            tabel(
                "Hoe verandert de kleur na deze ingreep?",
                [
                    ("Je voegt in buisje 1 extra Fe³⁺ toe.", "donkerder rood"),
                    ("Je voegt in buisje 2 extra SCN⁻ toe.", "donkerder rood"),
                    ("Je haalt in buisje 3 met een andere stof Fe³⁺ weg.", "lichter"),
                ],
                "Extra reagens duwt het evenwicht naar rechts, reagens wegnemen naar links.",
                kolommen=["donkerder rood", "lichter"],
            ),
            keuze(
                "De kleur toont dat er in het evenwicht [[*een duidelijke hoeveelheid product|geen product meer]] aanwezig is.",
                "Bloedrood betekent: veel FeSCN²⁺.",
            ),
            mk(
                "Na de toevoeging in buisje 1 blijft de kleur na een tijd constant. Wat betekent dat?",
                ["Er is een nieuw evenwicht", "De reactie is helemaal afgelopen", "Alle Fe³⁺ is opgebruikt", "De reacties staan nu stil"],
                0,
                "Constant betekent niet: stilstaand.",
            ),
        ],
    ),
    casus(
        "Je laat 3 mol stof A reageren met 4 mol stof B volgens A + B → C. De reactie is aflopend.",
        [
            inv("Hoeveel mol C ontstaat er?", ["3"], "A raakt als eerste op: 3 mol A geeft 3 mol C."),
            keuze("Stof [[*A|B]] is het limiterend reagens.", "A is als eerste op."),
            inv("Hoeveel mol B blijft er over?", ["1"], "4 − 3 = 1 mol B in overmaat."),
        ],
    ),
    sorteer(
        "Gaat het om een aflopende reactie of om een evenwicht?",
        ["Aflopende reactie", "Evenwicht"],
        [
            ("een beginstof is helemaal opgebruikt", "Aflopende reactie"),
            ("de heen- en terugreactie gaan even snel", "Evenwicht"),
            ("je vertrekt ook van de producten en komt op hetzelfde uit", "Evenwicht"),
            ("er is een limiterend reagens en een reagens in overmaat", "Aflopende reactie"),
        ],
        "In een evenwicht blijven alle stoffen aanwezig.",
    ),
    tabel(
        "Een gasevenwicht A(g) + B(g) ⇌ 2 C(g). Verschuift het evenwicht door deze ingreep?",
        [
            ("Je verhoogt de druk.", F),
            ("Je voegt extra A toe.", J),
            ("Je haalt C weg.", J),
            ("Je voegt een katalysator toe.", F),
        ],
        "Links en rechts staan evenveel mol gas, dus de druk verandert niets.",
    ),
    mk(
        "In een evenwicht worden er nog altijd nieuwe productdeeltjes gevormd. Waarom stijgt hun concentratie dan niet?",
        ["Even veel worden er weer omgezet", "Er worden geen nieuwe deeltjes meer gemaakt", "Alle reagentia zijn al opgebruikt", "De katalysator breekt de deeltjes af"],
        0,
        "Heen- en terugreactie gaan even snel.",
    ),
    keuze(
        "Een fabriek koelt het mengsel van een exo-energetische evenwichtsreactie. Het evenwicht schuift dan [[*naar rechts|naar links]].",
        "Afkoelen bevoordeelt de richting die warmte afgeeft.",
    ),
    volgorde(
        "Zet in volgorde wat er gebeurt als je reagens toevoegt aan een evenwicht.",
        ["de concentratie van het reagens stijgt", "de heenreactie wordt sneller", "er ontstaat extra product", "beide snelheden worden opnieuw gelijk"],
        "Het evenwicht werkt de verstoring tegen.",
    ),
    sleep(
        "Bij een aflopende reactie raakt het [[limiterend reagens]] op. Van het andere reagens blijft er iets over: dat is in [[overmaat]].",
        ["evenwicht", "katalysator"],
        "Zo weet je hoeveel product er maximaal kan ontstaan.",
    ),
    open_(
        "Leg uit waarom een chemisch evenwicht dynamisch genoemd wordt, al lijkt er van buiten niets te gebeuren.",
        "In een evenwicht lopen de heen- en de terugreactie allebei door, even snel. Er worden dus voortdurend deeltjes omgezet en teruggevormd, maar de concentraties blijven gelijk. Daarom zie je van buiten geen verandering.",
    ),
]

EIGEN += [
    keuze(
        "Je mengt twee stoffen en de concentraties blijven vanaf het begin [[*gelijk|veranderen]]. Dan is er geen reactie.",
        "Geen enkele verandering: de stoffen reageren niet.",
    ),
    tabel(
        "Klopt dit over de snelheden op weg naar een evenwicht?",
        [
            ("De heenreactie wordt trager.", J),
            ("De terugreactie wordt sneller.", J),
            ("In het evenwicht zijn beide snelheden nul.", F),
        ],
        "De reagentia raken op, het product stapelt zich op, tot beide snelheden gelijk zijn.",
    ),
    mk(
        "Waarom gebruikt men bij een proef soms één reagens in overmaat?",
        ["Om het andere reagens volledig te laten reageren", "Om het evenwicht te laten verdwijnen", "Om de reactie trager te maken", "Om minder product te krijgen"],
        0,
        "Het dure of belangrijke reagens raakt dan zeker op.",
    ),
]

VRAGEN = OVER + EIGEN

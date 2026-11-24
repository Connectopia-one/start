"""Populatie, steekproef en representativiteit — pittig (Beyond dubbele finaliteit, wiskunde).

Pittige vragen wiskunde basis Beyond over steekproeven binnen wi_steekproef, plus eigen vragen."""
from ..beyond_wiskunde_basis_themas import steekproeven as S
from ..beyond_wiskunde_basis_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(S.VRAGEN, [3, 4, 5, 10, 11, 12, 13, 15, 20, 21, 22, 23]) + [
    casus(
        "Een jeugdhuis wil weten hoeveel jongeren uit de gemeente op zaterdag willen komen. De gemeente telt \\(1200\\) jongeren tussen \\(14\\) en \\(18\\) jaar. "
        "Het jeugdhuis bevraagt de \\(60\\) jongeren die op een vrijdagavond in het jeugdhuis zijn. \\(45\\) van hen zeggen ja.",
        [
            inv("Hoeveel procent van de bevraagde jongeren zegt ja?", ["75", "75 %", "75%"], "\\(45 : 60 = 0{,}75\\)."),
            keuze("De populatie is [[*de \\(1200\\) jongeren van de gemeente|de \\(60\\) bevraagde jongeren|alle jeugdhuizen]].", "De populatie is de hele groep waarover je iets wil weten."),
            mk("Waarom is deze steekproef vertekend?",
               ["Wie al naar het jeugdhuis komt, wil er ook vaker naartoe.", "Zestig jongeren zijn altijd veel te weinig voor eender welk besluit.", "Op een vrijdagavond zijn er nooit genoeg jongeren in een jeugdhuis.", "Jongeren antwoorden nooit eerlijk op een vraag."], 0,
               "Jongeren die nooit komen, zitten er niet in."),
            open_("Hoe kies je de steekproef beter?",
                  "Ik neem de lijst van alle \\(1200\\) jongeren en trek er aselect bijvoorbeeld \\(100\\) uit, zodat elke jongere evenveel kans heeft.",
                  "Aselect trekken uit de hele populatie maakt de steekproef representatief."),
        ],
    ),
    tabel("Populatie, steekproef of variabele?", [
        ("alle klanten van een supermarktketen", "populatie"), ("de \\(250\\) klanten die een vragenlijst invulden", "steekproef"),
        ("hoeveel euro een klant per week uitgeeft", "variabele"), ("de reistijd naar de winkel", "variabele"),
    ], "De variabele is het kenmerk dat je meet.", kolommen=["populatie", "steekproef", "variabele"]),
    mk("Een fabriek test elke vijftigste fles van de band. Wat voor steekproef is dat?",
       ["een systematische steekproef", "een vertekende steekproef door vrije keuze", "een steekproef met vrijwillige deelname", "geen steekproef maar de hele populatie"], 0,
       "Met vaste tussenstappen uit de hele productie."),
    inv("Een school van \\(650\\) leerlingen bevraagt er \\(130\\). Hoeveel procent van de school is dat?", ["20", "20 %", "20%"], "\\(130 : 650 = 0{,}2\\)."),
    tabel("Klopt dit?", [
        ("Een grotere aselecte steekproef geeft een betrouwbaarder besluit.", J),
        ("Een vertekende steekproef wordt goed door er meer mensen op dezelfde manier bij te nemen.", F),
        ("Ook een aselecte steekproef kan door toeval wat scheef uitvallen.", J),
        ("Statistiek geeft zekerheid over de hele populatie.", F),
    ], "Grootte helpt tegen toeval, niet tegen vertekening."),
    sorteer("Welke groep ontbreekt of is ondervertegenwoordigd?", ["mensen die overdag werken", "mensen zonder internet", "jonge mensen"], [
        ["een telefonische peiling op een werkdag om \\(11\\) uur", "mensen die overdag werken"],
        ["een enquête enkel via een website", "mensen zonder internet"],
        ["een bevraging in een rusthuis over vrije tijd in de gemeente", "jonge mensen"],
        ["een bevraging aan de schoolpoort om \\(14\\) uur over de avondmarkt", "mensen die overdag werken"],
    ], "Bekijk telkens wie de methode nooit bereikt."),
    mk("Een krant schrijft: « uit een bevraging van \\(40\\) mensen blijkt dat \\(60\\) % van de Belgen tegen het plan is. » Wat is je grootste bezwaar?",
       ["Veertig mensen is weinig, en we weten niet hoe ze gekozen zijn.", "Zestig procent kan wiskundig nooit kloppen bij precies veertig mensen.", "Een krant mag eigenlijk geen percentages gebruiken in een artikel.", "Er moeten minstens evenveel mensen voor als tegen zijn."], 0,
       "Vraag altijd naar de grootte en de manier van kiezen."),
    keuze("Een vraag als « Bent u ook tegen die dure plannen? » is [[*sturend|neutraal]], en dat kan het besluit [[*vertekenen|verbeteren]].", "Hoe je vraagt, beïnvloedt het antwoord."),
    inv("In een aselecte steekproef van \\(400\\) inwoners hebben \\(88\\) een elektrische fiets. Hoeveel van de \\(25\\,000\\) inwoners schat je met een elektrische fiets?", ["5500", "5 500"],
        "\\(88 : 400 = 0{,}22\\) en \\(0{,}22 \\cdot 25\\,000 = 5500\\)."),
    koppel("Koppel elk woord aan zijn betekenis.", [
        ["representatief", "lijkt in samenstelling op de populatie"], ["aselect", "iedereen heeft evenveel kans om gekozen te worden"],
        ["vertekend", "bepaalde groepen zijn bevoordeeld"], ["systematisch", "met een vaste stap uit een lijst gekozen"],
    ], ["meet het hele land"], "Aselect kiezen helpt om representatief te zijn."),
    mk("Een leerling wil de gemiddelde schermtijd van alle leerlingen van zijn school weten. Welke steekproef is het best?",
       ["uit elke klas lukraak twee leerlingen loten", "zijn eigen vriendengroep, na school op het plein", "alle leerlingen van de gamingclub op woensdag", "wie op Smartschool reageert op een oproep"], 0,
       "Uit elke klas, en het lot beslist."),
    tabel("Is dit een goede reden om met een steekproef te werken?", [
        ("De hele populatie bevragen kost te veel tijd en geld.", J),
        ("Bij een kwaliteitstest gaat het product kapot.", J),
        ("Met een steekproef ben je zeker van het juiste antwoord.", F),
    ], "Een steekproef geeft een onderbouwde schatting, geen zekerheid."),
    mk("Een onderzoek stuurt \\(2000\\) vragenlijsten op en krijgt er \\(160\\) terug. Waar zit het risico?",
       ["Wie terugstuurt, verschilt misschien van wie niet terugstuurt.", "\\(160\\) antwoorden zijn veel te veel om nog goed te verwerken.", "Een vragenlijst per post is altijd aselect, dus er is geen probleem.", "Er is geen risico, want \\(2000\\) is groot genoeg."], 0,
       "Maar \\(8\\) procent antwoordt; die groep kiest zichzelf."),
    open_("Leg uit waarom een steekproef van \\(1000\\) aselect gekozen Belgen meer zegt dan \\(50\\,000\\) reacties op een oproep op sociale media.",
          "De \\(1000\\) aselect gekozen mensen lijken op de hele bevolking. De \\(50\\,000\\) reacties komen van wie de oproep ziet en zelf wil reageren: dat is een vertekende groep, en die vertekening verdwijnt niet door er meer mensen bij te nemen.",
          "Hoe je kiest is belangrijker dan hoeveel je kiest."),
    keuze("Het gemiddelde van een steekproef noteer je met [[*een streepje boven de \\(x\\)|de Griekse letter mu]], dat van de populatie met [[*de Griekse letter mu|een streepje boven de \\(x\\)]].", "Zo zie je meteen waarover het getal gaat."),
]

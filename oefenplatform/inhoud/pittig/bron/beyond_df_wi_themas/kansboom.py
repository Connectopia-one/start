"""Kansbomen: product, som en complement — pittig (Beyond dubbele finaliteit, wiskunde).

Pittige vragen wiskunde basis Beyond over kansbomen (met de prent van de bus) binnen wi_kansboom, plus eigen vragen."""
from ..beyond_wiskunde_basis_themas import kansen as K
from ..beyond_wiskunde_basis_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(K.VRAGEN, [0, 1, 2, 3, 13, 14, 16, 17, 22, 23, 24], {"met de voorwaardelijke kansen": "met de kansen die daar gelden"}) + [
    casus(
        "Een basketter scoort een vrije worp met kans \\(0{,}7\\). Ze krijgt twee vrije worpen. De worpen hangen niet van elkaar af.",
        [
            inv("Wat is de kans dat ze twee keer scoort? Geef een kommagetal.", ["0,49", "0.49"], "\\(0{,}7 \\cdot 0{,}7\\)."),
            inv("Wat is de kans dat ze precies één keer scoort? Geef een kommagetal.", ["0,42", "0.42"], "Twee paden: \\(0{,}7 \\cdot 0{,}3 + 0{,}3 \\cdot 0{,}7\\)."),
            inv("Wat is de kans dat ze minstens één keer scoort? Geef een kommagetal.", ["0,91", "0.91"], "\\(1 - 0{,}3 \\cdot 0{,}3\\)."),
            keuze("De drie kansen twee keer, precies één keer en nooit scoren geven samen [[*\\(1\\)|\\(0{,}91\\)|\\(2\\)]].", "\\(0{,}49 + 0{,}42 + 0{,}09 = 1\\)."),
        ],
    ),
    mk("In een doos zitten \\(4\\) goede en \\(2\\) kapotte batterijen. Je neemt er twee zonder terugleggen. Wat is de kans dat beide kapot zijn?",
       ["\\(\\tfrac{1}{15}\\)", "\\(\\tfrac{1}{9}\\)", "\\(\\tfrac{2}{6}\\)", "\\(\\tfrac{4}{15}\\)"], 0,
       "\\(\\tfrac{2}{6} \\cdot \\tfrac{1}{5} = \\tfrac{2}{30}\\)."),
    inv("Uit diezelfde doos neem je twee batterijen zonder terugleggen. Wat is de kans dat er minstens één kapot is? Schrijf het als breuk.", ["9/15", "3/5", "18/30", "drie vijfde"],
        "Twee goede: \\(\\tfrac{4}{6} \\cdot \\tfrac{3}{5} = \\tfrac{12}{30}\\). Dus \\(1 - \\tfrac{12}{30} = \\tfrac{18}{30}\\)."),
    mk("Je gooit vier keer met een eerlijke dobbelsteen. Wat is de kans op minstens één zes?",
       ["ongeveer \\(0{,}52\\)", "ongeveer \\(0{,}67\\)", "precies \\(\\tfrac{4}{6}\\)", "ongeveer \\(0{,}48\\)"], 0,
       "\\(1 - \\left(\\tfrac{5}{6}\\right)^4 \\approx 1 - 0{,}48\\)."),
    tabel("Vermenigvuldig of tel je de kansen op?", [
        ("twee takken na elkaar op hetzelfde pad", "vermenigvuldigen"), ("twee verschillende paden die allebei goed zijn", "optellen"),
        ("eerst kop, dan een zes", "vermenigvuldigen"), ("kop-munt of munt-kop", "optellen"),
    ], "Langs een pad: maal. Tussen paden: plus.", kolommen=["vermenigvuldigen", "optellen"]),
    mk("Een trein is op tijd met kans \\(0{,}9\\). Wat is de kans dat hij op een week van \\(5\\) schooldagen elke dag op tijd is?",
       ["ongeveer \\(0{,}59\\)", "\\(0{,}9\\)", "\\(4{,}5\\)", "ongeveer \\(0{,}41\\)"], 0,
       "\\(0{,}9^5 \\approx 0{,}59\\)."),
    keuze("Bij trekken [[*zonder|met]] terugleggen verandert de kans bij de tweede tak, omdat er één voorwerp minder in zit.", "Met terugleggen blijft alles gelijk."),
    inv("In een klas zitten \\(10\\) meisjes en \\(5\\) jongens. Je kiest er willekeurig twee zonder terugleggen. Wat is de kans op twee jongens? Schrijf het als breuk.", ["2/21", "20/210", "4/42"],
        "\\(\\tfrac{5}{15} \\cdot \\tfrac{4}{14} = \\tfrac{20}{210}\\)."),
    tabel("Klopt dit over kansbomen?", [
        ("Alle paden samen hebben kans \\(1\\).", J),
        ("Een tak kan een kans groter dan \\(1\\) hebben.", F),
        ("Paden sluiten elkaar uit, dus je mag hun kansen optellen.", J),
        ("Binnen een pad tel je de takkansen op.", F),
    ], "Binnen een pad vermenigvuldig je."),
    mk("Een spel heeft winkans \\(0{,}2\\). Hoeveel keer moet je minstens spelen om meer dan de helft kans te hebben om minstens één keer te winnen?",
       ["\\(4\\) keer", "\\(3\\) keer", "\\(5\\) keer", "\\(2\\) keer"], 0,
       "\\(1 - 0{,}8^3 \\approx 0{,}49\\) en \\(1 - 0{,}8^4 \\approx 0{,}59\\)."),
    open_("Leg uit waarom je bij « minstens één » liever de complementregel gebruikt dan alle paden op te tellen.",
          "Minstens één omvat veel paden, maar het tegendeel is maar één pad: nooit. Dat ene pad reken je met de productregel uit en je trekt het af van \\(1\\).",
          "Eén pad uitrekenen gaat sneller en geeft minder kans op fouten."),
    inv("Een fabriek keurt \\(90\\) % van de stukken goed. Je neemt drie stukken. Wat is de kans dat er precies één afgekeurd wordt? Geef een kommagetal.", ["0,243", "0.243"],
        "Drie paden van \\(0{,}1 \\cdot 0{,}9 \\cdot 0{,}9 = 0{,}081\\)."),
    mk("Je trekt twee kaarten uit een spel van \\(52\\) zonder terugleggen. Wat is de kans op twee azen?",
       ["\\(\\tfrac{1}{221}\\)", "\\(\\tfrac{1}{169}\\)", "\\(\\tfrac{2}{52}\\)", "\\(\\tfrac{1}{13}\\)"], 0,
       "\\(\\tfrac{4}{52} \\cdot \\tfrac{3}{51} = \\tfrac{12}{2652} = \\tfrac{1}{221}\\)."),
    sleep("Langs één pad gebruik je de [[productregel]]. Voor meerdere paden samen gebruik je de [[somregel]]. Voor « minstens één » werk je het snelst met de [[complementregel]].",
          ["wet van Laplace", "relatieve frequentie"], "Maal, plus en één min."),
    inv("Een bus is te laat met kans \\(0{,}15\\). Wat is de kans dat hij twee dagen na elkaar op tijd is? Geef een kommagetal.", ["0,7225", "0.7225"],
        "\\(0{,}85 \\cdot 0{,}85\\)."),
    sorteer("Verandert de kans bij de tweede trekking of niet?", ["verandert", "verandert niet"], [
        ["twee knikkers trekken zonder terugleggen", "verandert"], ["twee keer met een dobbelsteen gooien", "verandert niet"],
        ["twee leerlingen na elkaar kiezen voor een taak", "verandert"], ["twee keer een kaart trekken met terugleggen", "verandert niet"],
    ], "Zonder terugleggen is er één voorwerp minder."),
]

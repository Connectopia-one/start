"""De morele ontwikkeling volgens Kohlberg — pittig (🚀 Boost doorstroom, sociale en gedragswetenschappen).

Eigen vragen strikt binnen sg_kohlberg: de morele ontwikkeling per
levensfase, de drie stadia en het stadium bepalen uit een redenering. Met
vier zelfgetekende tekstwolkjes."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS

PW = Prent("portefeuille-redenen", "Waarom geef je een gevonden portefeuille terug?", "vier tekstwolkjes met een reden, letters A tot D")
WOLK = [("A", 60, 80, ["Anders pakt de politie", "mij misschien op."]),
        ("B", 520, 80, ["Zo staat het in de wet,", "en zo hoort het nu eenmaal."]),
        ("C", 60, 350, ["Eerlijkheid is voor mij", "belangrijker dan wat", "ik ermee zou winnen."]),
        ("D", 520, 350, ["Misschien krijg ik", "wel een beloning."])]
for t, x, y, regels in WOLK:
    PW.rect(x, y, 420, 200, "#ffffff", DONKER, 30, 3)
    PW.pad(f"M {x+80} {y+200} L {x+70} {y+240} L {x+120} {y+200}", "#ffffff", DONKER, 3)
    PW.lijn(x + 82, y + 200, x + 118, y + 200, "#ffffff", 4)
    for i, r in enumerate(regels):
        PW.tekst(x + 200, y + 95 + i * 34 - (len(regels) - 1) * 17, r, 23)
    PW.letter(x + 385, y + 170, t)
U = "portefeuille-redenen.svg"
Z = {t: [Prent.zone(x, y, 420, 240)] for t, x, y, r in WOLK}

KAMP = ("Lees het voorval.\n\n"
        "Op schoolreis mogen de leerlingen 's avonds niet uit hun kamer. Drie vrienden blijven toch binnen. Na afloop vraagt de leerkracht waarom.\n\n"
        "Kobe: « Als ze ons betrappen, mogen we morgen niet mee naar het pretpark. »\n"
        "Femke: « De leiding heeft die regel gemaakt, en een goede leerling houdt zich daaraan. »\n"
        "Arne: « Ik vind dat je afspraken nakomt als ze er zijn om iedereen veilig te houden. Een regel die niemand beschermt, zou ik in vraag stellen. »")

VRAGEN = [
    klik("Bekijk de redenen om een gevonden portefeuille terug te geven. Klik op de reden van iemand in het conventionele stadium.", U, Z["B"], "De wet en de gewoonte geven de doorslag."),
    klik("Klik op de reden van iemand in het post-conventionele stadium.", U, Z["C"], "Een eigen beginsel weegt zwaarder dan het eigen voordeel."),
    klik("Klik op de reden die verdwijnt zodra niemand het ziet.", U, Z["A"], "Wie enkel straf vreest, houdt zich niet in zonder toezicht."),
    klik("Klik op de pre-conventionele reden die over iets krijgen gaat.", U, Z["D"], "Goed is wat beloond wordt."),
    casus(KAMP, [
        tabel("Welk stadium van Kohlberg toont deze redenering?",
              [("Kobe", "pre-conventioneel"), ("Femke", "conventioneel"), ("Arne", "post-conventioneel")],
              "De drie doen hetzelfde, maar om een andere reden.", ["pre-conventioneel", "conventioneel", "post-conventioneel"]),
        mk("Wat leert dit voorval over de methode van Kohlberg?",
           ["de reden bepaalt het stadium", "de daad zegt genoeg over het stadium van iemand", "wie de regel volgt, zit altijd in het hoogste stadium", "het stadium hangt af van hoe streng de leerkracht is"],
           0, "Twee mensen kunnen hetzelfde doen om een heel andere reden."),
        keuze("Arne denkt na over waarom de regel er is. Daarvoor is [[*abstract denken|een beloning|een reflex]] nodig.", "Het post-conventionele vraagt formeel-operationeel denken."),
    ]),
    volgorde("Zet de stadia van Kohlberg in de juiste volgorde.",
             ["pre-conventioneel", "conventioneel", "post-conventioneel"],
             "De orde ligt vast; een stadium overslaan kan niet."),
    sorteer("Welk stadium volgens Kohlberg?", ["pre-conventioneel", "conventioneel", "post-conventioneel"],
            [("'Ik deel mijn koek, dan krijg ik er een snoepje voor.'", "pre-conventioneel"), ("'Ik help mijn zus, want in een gezin helpt men elkaar.'", "conventioneel"), ("'Deze wet is onrechtvaardig, dus ik betoog ertegen.'", "post-conventioneel"), ("'Ik rook niet, mijn vrienden zouden dat stom vinden.'", "conventioneel"), ("'Ik gehoorzaam als de juf kijkt.'", "pre-conventioneel")],
            "Straf en beloning, de groep en de wet, eigen beginselen."),
    tabel("Klopt dit over Kohlberg?",
          [("Iedereen bereikt het post-conventionele stadium.", F), ("Veel volwassenen blijven in het conventionele stadium.", J), ("Onder druk kan je terugvallen op een lager stadium.", J), ("Kohlberg leest het stadium af uit de daad.", F)],
          "De redenering erachter telt."),
    mk("Wat bedoelt Kohlberg met 'conventies'?",
       ["afspraken en regels", "straffen en beloningen die je krijgt", "eigen beginselen boven de wet", "de genen die je van je ouders krijgt"],
       0, "Het conventionele stadium volgt de afspraken van de groep."),
    keuze("Een volwassene die zegt 'ik doe het niet, want ik wil geen last krijgen', redeneert [[*pre-conventioneel|conventioneel|post-conventioneel]].", "Ook een volwassene kan zo redeneren."),
    keuze("Het post-conventionele stadium betekent [[*dat je een regel afweegt tegen een beginsel|dat je alle regels mag overtreden|dat je enkel aan straf denkt]].", "Regels blijven belangrijk, maar worden afgewogen."),
    tabel("Is dit een moreel dilemma zoals Kohlberg ze gebruikte?",
          [("Een man steelt een duur medicijn voor zijn zieke vrouw.", J), ("Je kiest tussen pasta of pizza.", F), ("Je verklikt een vriend of je zwijgt.", J)],
          "Bij een dilemma kosten beide keuzes iets."),
    inv("Hoe heet de man uit het bekendste dilemma van Kohlberg? Eén naam.", ["Heinz", "heinz"], "Hij steelt een medicijn voor zijn vrouw."),
    keuze("De morele ontwikkeling hangt samen met de [[*cognitieve|fysieke|sensorische]] ontwikkeling.", "Over een beginsel redeneren vraagt abstract denken."),
    keuze("Een peuter weet nog niet dat slaan pijn doet bij een ander. Hij kan zich nog niet [[*in een ander verplaatsen|aan de wet houden|aan een beginsel houden]].", "Zonder perspectief nemen geen moreel oordeel."),
    koppel("Koppel het stadium aan wat goed is volgens dat stadium.",
           [("pre-conventioneel", "wat geen straf oplevert"), ("conventioneel", "wat de groep of de wet verwacht"), ("post-conventioneel", "wat strookt met een eigen beginsel")],
           ["wat het snelst gaat"], "Drie stadia, drie maatstaven."),
    keuze("Gilligan bekritiseerde Kohlberg: volgens haar weegt [[*zorgen voor elkaar|straf vermijden|de wet volgen]] even zwaar als rechtvaardigheid.", "De theorie weegt rechtvaardigheid het zwaarst."),
    sleep("In het [[pre-conventionele]] stadium sturen straf en beloning. In het [[conventionele]] stadium tellen de regels en de groep. In het [[post-conventionele]] stadium wegen eigen beginselen.",
          ["sensomotorische", "formele"], "Drie stadia."),
    keuze("Een kind dat zijn speelgoed opruimt omdat het anders geen tv mag kijken, zit in het [[*pre-conventionele|conventionele|post-conventionele]] stadium.", "Straf en beloning sturen het gedrag."),
    mk("Een buurt spreekt af dat niemand na tien uur lawaai maakt, en bijna iedereen houdt zich eraan. Welk stadium maakt zo'n afspraak sterk?",
       ["het conventionele", "het pre-conventionele, want iedereen vreest een boete", "het post-conventionele, want niemand denkt nog aan regels", "geen enkel stadium, want het gaat over lawaai"],
       0, "De meeste mensen volgen de regels van de groep."),
    keuze("Het pre-conventionele stadium zie je vooral bij [[*kleuters en jonge schoolkinderen|adolescenten|ouderen]].", "Maar ook een volwassene kan er soms in redeneren."),
    tabel("Past deze reden bij het post-conventionele stadium?",
          [("Een wet kan onrechtvaardig zijn.", J), ("Menselijke waardigheid gaat voor.", J), ("Ik krijg er iets voor terug.", F), ("Het staat zo in de wet.", F)],
          "Eigen beginselen wegen zwaar."),
    mk("Kohlberg vraagt in het dilemma van Heinz niet enkel of stelen mag. Wat vraagt hij nog?",
       ["waarom je dat vindt", "hoeveel het medicijn precies kost", "welke straf Heinz moet krijgen van de rechter", "of de apotheker een vriend van Heinz is"],
       0, "Het antwoord ja of nee zegt niets; de uitleg wel."),
    keuze("Een stadium van Kohlberg overslaan [[*kan niet|kan wel]].", "Zoals bij Piaget ligt de orde vast."),
    tabel("Hoort deze reden bij het conventionele stadium?",
          [("Zo hoort het nu eenmaal.", J), ("Mijn ouders verwachten het van mij.", J), ("Anders word ik gestraft.", F)],
          "Wat de groep of de wet verwacht."),
    keuze("Een jongere stelt een regel van thuis in vraag. Dat hoort bij de [[*overgang naar een volgend stadium|terugval naar het eerste stadium|sensomotorische ontwikkeling]].", "Een regel bevragen is een teken van groei."),
    keuze("Een kleuter deelt zijn koek omdat hij er een snoepje voor krijgt. Dat is eigenlijk [[*ruilen|een beginsel volgen|de wet volgen]].", "Pre-conventioneel: iets terugkrijgen."),
    open_("Bedenk een korte situatie en geef drie redenen voor dezelfde keuze: één per stadium van Kohlberg.",
          "Situatie: je ziet een vriend spieken. Je zegt het niet tegen de leerkracht. Pre-conventioneel: 'anders slaat hij me misschien'. Conventioneel: 'een goede vriend verklikt niet, zo hoort het in onze groep'. Post-conventioneel: 'ik vind trouw hier belangrijker, al weet ik dat eerlijkheid ook telt, en ik spreek hem er zelf over aan'."),
]

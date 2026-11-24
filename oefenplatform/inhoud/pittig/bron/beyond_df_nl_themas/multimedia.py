"""Multimediale elementen en non-verbale communicatie — pittig (Beyond dubbele finaliteit, Nederlands).

Pittige vragen Nederlands Beyond doorstroom over lichaamstaal, verder eigen vragen binnen nl_multimedia over beeld, geluid, kleur, lay-out en typografie."""
from ..beyond_nederlands_themas import identiteit as D
from ..beyond_nederlands_themas.vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._kies import kies

VRAGEN = kies(D.VRAGEN, [2, 7, 8, 10, 13, 16, 17, 21]) + [
    casus(
        "Een nieuwssite brengt een artikel met de titel « Werkloosheid daalt licht ». Bovenaan staat een grote foto van een lange rij mensen "
        "voor een kantoor van de VDAB, in grijze tinten. Onder de foto staat geen onderschrift. In het artikel staat een staafgrafiek waarvan de verticale as begint bij \\(5{,}8\\) procent.",
        [
            mk("Wat is het probleem met de foto?",
               ["Ze toont een ander beeld dan de daling uit de tekst.", "Een nieuwsartikel mag nooit een foto hebben.", "Grijze tinten zijn op een nieuwssite eigenlijk niet toegelaten.", "De foto is te klein voor het artikel."], 0,
               "Beeld en tekst sturen hier een andere kant op."),
            keuze("Een onderschrift zou zeggen [[*wat de foto toont en waar ze vandaan komt|hoe oud de fotograaf is|welke kleur de titel heeft]].", "Zonder onderschrift weet de lezer niet wat hij ziet."),
            mk("Wat doet de verticale as die bij \\(5{,}8\\) procent begint?",
               ["Een kleine daling lijkt veel groter dan ze is.", "De grafiek wordt daardoor nauwkeuriger.", "De cijfers kloppen dan niet meer.", "Er verandert niets aan hoe je de grafiek leest."], 0,
               "Een grafiek kan misleiden zonder één fout cijfer."),
        ],
    ),
    tabel("Welke functie heeft dit multimediale element vooral?", [
        ("een kaart bij een artikel over een overstroming", "informeren"), ("spannende muziek onder een trailer", "stemming"),
        ("een foto van een huilend kind bij een oproep om te doneren", "stemming"), ("een infographic met de cijfers van een enquête", "informeren"),
    ], "Sommige elementen geven informatie, andere zetten een stemming.", kolommen=["informeren", "stemming"]),
    koppel("Koppel elk lay-outelement aan wat het doet.", [
        ["tussenkop", "toont de indeling van de tekst"], ["vet gezet woord", "trekt de aandacht naar dat woord"],
        ["witregel", "scheidt twee delen van elkaar"], ["pictogram", "duidt zonder taal één ding aan"],
    ], ["maakt de tekst langer"], "Lay-out en typografie sturen het lezen."),
    mk("Een affiche tegen te snel rijden gebruikt rood, zwart en grote blokletters. Welk effect ligt het meest voor de hand?",
       ["waarschuwen en de aandacht trekken", "de lezer laten ontspannen en rustig maken", "het product goedkoop laten lijken", "informatie geven over de prijs van een boete"], 0,
       "Rood waarschuwt, blokletters vallen op."),
    tabel("Klopt dit over beelden?", [
        ("Een bewerkte foto blijft altijd een betrouwbare weergave.", F), ("Iemand koos de uitsnede en het moment van een foto.", J),
        ("Een beeld kan de boodschap van een tekst bijsturen.", J), ("Bij een beeld van een ander hoort een bronvermelding.", J),
    ], "Een foto is altijd een keuze."),
    mk("Een filmpje toont een politicus van onderaf gefilmd. Wat doet die camerahoek?",
       ["Hij laat de persoon groter en machtiger lijken.", "Hij laat de persoon kleiner, zwakker en onzeker lijken.", "Hij heeft geen enkel effect op de kijker.", "Hij laat de persoon jonger en vrolijker lijken dan hij is."], 0,
       "Een lage hoek maakt iemand indrukwekkend."),
    keuze("Een infographic zet [[*veel gegevens in één overzichtelijk beeld|één foto groot in beeld|een tekst om in een filmpje]].", "Cijfers, verhoudingen en verbanden in één oogopslag."),
    sorteer("Is dit verbale of non-verbale communicatie?", ["verbaal", "non-verbaal"], [
        ["de woorden van een toespraak", "verbaal"], ["een knipoog", "non-verbaal"], ["de armen kruisen", "non-verbaal"],
        ["een geschreven uitnodiging", "verbaal"], ["afstand houden tijdens een gesprek", "non-verbaal"],
    ], "Non-verbaal is alles behalve de woorden zelf."),
    mk("Welke regel geldt voor een goede dia bij een presentatie?",
       ["één gedachte per dia, in grote letters", "zoveel mogelijk tekst, zodat niets vergeten wordt", "elke dia een andere kleur en een ander lettertype", "de volledige tekst van je spreekbeurt"], 0,
       "De dia's steunen je woorden, ze vervangen ze niet."),
    tabel("Past het beeld bij de tekst?", [
        ("een bericht over een droogte, met een foto van een gebarsten akker", J), ("een bericht over armoede, met een foto van een feestend gezin", F),
        ("een artikel over een nieuwe fietsbrug, met een foto van die brug", J),
    ], "Je gaat na of het beeld de boodschap ondersteunt of tegenspreekt."),
    keuze("Wie « prima » zegt met een strak gezicht en afgewend hoofd, laat zien dat woorden en lichaamstaal [[*elkaar tegenspreken|hetzelfde zeggen]].", "Dan geloven mensen meestal de lichaamstaal."),
    mk("Je ziet een video waarin een politicus spreekt met donkere, dreigende muziek eronder. Wat doe je als kritische kijker?",
       ["Je vraagt je af wie de muziek koos en waarom.", "Je gelooft alles omdat de beelden echt zijn.", "Je zet het geluid luider om beter te luisteren.", "Je kijkt enkel naar de kleur van zijn kleren."], 0,
       "Muziek kan een boodschap kleuren."),
    sleep("Een [[pictogram]] werkt zonder taal. Een [[onderschrift]] zegt wat een beeld toont. Met [[typografie]] zoals vet en cursief stuur je de aandacht.",
          ["refrein", "voetnoot"], "Elk middel heeft een eigen taak."),
    tabel("Welk effect heeft deze kleur meestal op een affiche?", [
        ("rood", "waarschuwen"), ("groen", "geruststellen"), ("geel met zwart", "waarschuwen"), ("zachtblauw", "geruststellen"),
    ], "Kleuren hebben een gevoelswaarde.", kolommen=["waarschuwen", "geruststellen"]),
    open_("Een leerling maakt een affiche voor een benefietactie. Geef twee multimediale keuzes die het affiche duidelijker maken, en zeg waarom.",
          "Een grote titel in een opvallende kleur trekt de aandacht. Een foto van het goede doel met een kort onderschrift toont meteen waarvoor de actie dient.",
          "Elke keuze moet de boodschap dienen."),
    mk("Waarom kan een filmpje bij een artikel nuttig zijn?",
       ["Het kan informatie geven die niet in de tekst staat.", "Het maakt de hele tekst van het artikel overbodig.", "Een filmpje is altijd neutraler dan tekst.", "Het zorgt dat je het artikel niet hoeft te lezen."], 0,
       "Daarom hoort het filmpje bij wat je bekijkt."),
    keuze("Oogcontact betekent [[*niet in elke situatie of cultuur|in elke situatie en cultuur]] hetzelfde.", "Het kan belangstelling tonen, maar ook uitdaging."),
    tabel("Hoort dit bij non-verbale signalen van een goede spreker?", [
        ("de zaal rondkijken", J), ("rechtop staan", J), ("de hele tijd naar je blad staren", F), ("gebaren die je woorden ondersteunen", J),
    ], "Je lichaam versterkt je boodschap."),
    mk("Een reclame voor een auto toont die auto in een leeg berglandschap. Wat wil dat beeld oproepen?",
       ["vrijheid en avontuur", "de prijs van de auto", "het verbruik van de motor", "de veiligheid van de remmen"], 0,
       "Het beeld verbindt het product met een gevoel."),
]

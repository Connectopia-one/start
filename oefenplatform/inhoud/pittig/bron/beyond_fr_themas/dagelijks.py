"""Woordvelden mens, gezondheid, eten en wonen — pittig (🌍 Beyond doorstroom, Frans)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

TEKST1 = (
    "Lisez le message de Julie sur un forum.\n\n"
    "« Depuis lundi, je suis enrhumée et j'ai un peu de fièvre. Le médecin m'a donné une ordonnance, "
    "donc je suis passée à la pharmacie. Je dors beaucoup, mais je me sens encore fatiguée. "
    "Heureusement, ma voisine me rend service : elle fait les courses pour moi. "
    "J'espère me remettre avant samedi, parce que je m'entraîne pour un match de volley. »"
)

TEKST2 = (
    "Lisez l'annonce.\n\n"
    "À louer : T2 lumineux dans un immeuble calme, centre-ville de Lille. "
    "Une chambre, un séjour, une cuisine équipée et une salle de bains. "
    "Loyer : 650 € par mois, charges comprises. Bail d'un an minimum. "
    "Le propriétaire habite au rez-de-chaussée. Idéal pour un étudiant ou un jeune couple."
)

VRAGEN = [
    casus(
        TEKST1,
        [
            tabel(
                "Staat dit in het bericht van Julie?",
                [
                    ("Julie is verkouden.", J),
                    ("Ze heeft een voorschrift gekregen.", J),
                    ("Ze voelt zich al helemaal uitgerust.", F),
                    ("Haar buurvrouw doet boodschappen voor haar.", J),
                ],
                "Enrhumée, une ordonnance, encore fatiguée, ma voisine fait les courses.",
            ),
            mk(
                "Wat betekent « me remettre » in de laatste zin?",
                ["herstellen", "opnieuw beginnen met school", "iets terugbrengen naar de winkel", "de wedstrijd uitstellen"],
                0,
                "Se remettre: herstellen, beter worden.",
            ),
            keuze(
                "Julie wil zaterdag [[*een volleybalwedstrijd spelen|uitslapen]].",
                "Je m'entraîne pour un match de volley.",
            ),
            inv(
                "Welk Frans woord uit de tekst betekent buurvrouw?",
                ["voisine", "ma voisine", "la voisine"],
                "Une voisine, un voisin.",
            ),
        ],
    ),
    casus(
        TEKST2,
        [
            tabel(
                "Klopt dit volgens de huuradvertentie?",
                [
                    ("Het appartement heeft één slaapkamer.", J),
                    ("De kosten zitten in de 650 euro.", J),
                    ("Je mag het voor drie maanden huren.", F),
                    ("De eigenaar woont in hetzelfde gebouw.", J),
                ],
                "Une chambre, charges comprises, bail d'un an minimum, le propriétaire habite au rez-de-chaussée.",
            ),
            mk(
                "Wie betaalt « le loyer » in deze advertentie?",
                ["de huurder", "de eigenaar", "de buren van het gebouw", "de stad Lille"],
                0,
                "Le locataire betaalt le loyer aan le propriétaire.",
            ),
            keuze(
                "Een « T2 » heeft [[*twee kamers|twee badkamers]] naast keuken en bad.",
                "T + aantal kamers: hier een chambre en un séjour.",
            ),
        ],
    ),
    koppel(
        "Koppel de uitdrukking over hoe iemand zich voelt aan de betekenis.",
        [
            ("être en pleine forme", "zich uitstekend voelen"),
            ("avoir le moral", "goed in je vel zitten"),
            ("être mal à l'aise", "zich niet op zijn gemak voelen"),
            ("être stressé", "gestresseerd zijn"),
        ],
        ["verkouden zijn"],
        "Vaste uitdrukkingen over lichaam en gemoed.",
    ),
    sorteer(
        "Gaat het over eten en drinken of over wonen?",
        ["Eten en drinken", "Wonen"],
        [
            ("l'entrée", "Eten en drinken"),
            ("le plat du jour", "Eten en drinken"),
            ("le locataire", "Wonen"),
            ("le bail", "Wonen"),
            ("l'addition", "Eten en drinken"),
            ("un immeuble", "Wonen"),
        ],
        "Twee woordvelden uit het dagelijkse leven.",
    ),
    tabel(
        "In welke winkel koop je dit?",
        [
            ("une baguette", "la boulangerie"),
            ("un steak", "la boucherie"),
            ("des médicaments", "la pharmacie"),
            ("un croissant", "la boulangerie"),
        ],
        "Brood bij de bakker, vlees bij de slager, medicijnen bij de apotheek.",
        kolommen=["la boulangerie", "la boucherie", "la pharmacie"],
    ),
    volgorde(
        "Zet de ochtendroutine van Tom in een logische volgorde.",
        ["se réveiller", "se lever", "prendre une douche", "prendre le petit-déjeuner"],
        "Wakker worden, opstaan, douchen, ontbijten.",
    ),
    mk(
        "« Ce film est fatigant. » Wat bedoelt de spreker?",
        ["De film is vermoeiend", "De spreker is erg moe", "De film is heel grappig", "De film duurt maar kort"],
        0,
        "Fatigant: vermoeiend; fatigué: moe.",
    ),
    mk(
        "Je hebt genoeg gegeten op een Frans feest. Wat zeg je?",
        ["J'ai assez mangé, merci.", "Je suis plein, merci beaucoup.", "C'est bien, je ne veux plus rien.", "J'ai mal au ventre, au revoir."],
        0,
        "Je suis plein klinkt in het Frans vreemd; zeg j'ai assez mangé of je n'ai plus faim.",
    ),
    mk(
        "Welke zin over smaak is juist?",
        ["Cette soupe est très bonne.", "Cette soupe est très bien.", "Cette soupe est très sensible.", "Cette soupe est très fatiguée."],
        0,
        "Bon(ne) voor smaak.",
    ),
    mk(
        "Je vriend is « sensible ». Wat voor iemand is hij?",
        ["gevoelig", "verstandig", "sportief", "slaperig en lui"],
        0,
        "Sensible: gevoelig; raisonnable: verstandig.",
    ),
    mk(
        "Wat doe je als je « fais la grasse matinée »?",
        ["uitslapen", "het huis poetsen", "vet eten bij het ontbijt", "vroeg gaan sporten"],
        0,
        "Faire la grasse matinée: lang in bed blijven.",
    ),
    mk(
        "Welke zin past bij een bezoek aan de dokter?",
        ["J'ai mal au dos depuis hier.", "Je voudrais l'addition, s'il vous plaît.", "Le loyer est trop cher ici.", "Je fais du vélo le dimanche."],
        0,
        "Avoir mal à + lichaamsdeel.",
    ),
    keuze(
        "« Il s'est endormi » betekent dat hij [[*in slaap is gevallen|wakker is geworden]].",
        "S'endormir: in slaap vallen; se réveiller: wakker worden.",
    ),
    keuze(
        "Wie « fait le ménage », is aan het [[*poetsen|winkelen]].",
        "Faire le ménage: schoonmaken; faire les courses: boodschappen doen.",
    ),
    keuze(
        "« Elle s'entend mal avec son frère » betekent dat ze [[*slecht overeenkomt met|slecht hoort bij]] haar broer.",
        "S'entendre bien/mal avec quelqu'un.",
    ),
    keuze(
        "Een « entraîneur » is een [[*trainer|trein]].",
        "S'entraîner: trainen.",
    ),
    tabel(
        "Juist of fout over deze woorden?",
        [
            ("La joie is een gevoel.", J),
            ("La tristesse betekent vreugde.", F),
            ("Un rhume is een verkoudheid.", J),
            ("La santé betekent gezondheid.", J),
        ],
        "La tristesse is verdriet.",
    ),
    inv(
        "Vul aan met één Frans woord: « Je suis très ___ ; j'ai travaillé toute la journée. » (moe)",
        ["fatigué", "fatiguée"],
        "Fatigué(e): moe.",
    ),
    inv(
        "Vul aan met één Frans woord: « Le médecin m'a donné une ___ pour des médicaments. »",
        ["ordonnance"],
        "Une ordonnance: voorschrift.",
    ),
    inv(
        "Vul aan: « Le samedi, je fais ___ tennis avec mon père. » (één woord)",
        ["du"],
        "Faire du + sport.",
    ),
    sleep(
        "In het restaurant kies ik eerst [[l'entrée]], dan [[le plat du jour]]. Op het einde vraag ik [[l'addition]].",
        ["le loyer", "l'ordonnance"],
        "Voorgerecht, dagschotel, rekening.",
    ),
    sleep(
        "Ik huur een [[studio]] van één kamer. Elke maand betaal ik [[le loyer]] aan [[le propriétaire]].",
        ["la pharmacie", "le voisin"],
        "Woorden uit een huurcontract.",
    ),
    open_(
        "Schrijf in het Frans drie zinnen aan een vriend: je bent ziek, wat je hebt en wanneer je hoopt beter te zijn.",
        "Salut Léo, je suis malade depuis mardi. J'ai mal à la gorge et un peu de fièvre. J'espère me remettre avant le week-end.",
    ),
    mk(
        "Wat is « un locataire »?",
        ["de huurder", "de eigenaar van het huis", "de huur die je elke maand betaalt", "het huurcontract van een jaar"],
        0,
        "Le locataire huurt; le propriétaire verhuurt.",
    ),
    keuze(
        "« Prendre le petit-déjeuner » doe je [[*'s morgens|'s avonds]].",
        "Le petit-déjeuner: het ontbijt.",
    ),
]

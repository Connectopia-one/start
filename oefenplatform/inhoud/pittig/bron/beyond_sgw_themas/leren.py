"""Ontwikkeling: de behavioristische en de cognitieve benadering — pittig
(🌍 Beyond doorstroom, sociale en gedragswetenschappen). Eigen vragen en een eigen
schema van het geheugen, zoals op het digitale examen."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent
from .prent import Prent, DONKER, GRIJS

# Schema van het geheugen ----------------------------------------------------------------
GH = Prent("geheugen-schema", "Het geheugen volgens de informatieverwerkingstheorie", "een boomschema van boven naar onder: bovenaan een leeg vak A, een pijl naar een leeg vak B, dat splitst in twee lege vakken C (links) en D (rechts); onder C twee vakken met de woorden episodisch en semantisch; onder D een leeg vak G")
VAK = {"A": (400, 70), "B": (400, 190), "C": (220, 330), "D": (620, 330),
       "E": (110, 480), "F": (330, 480), "G": (620, 480)}
for k, (x, y) in VAK.items():
    GH.rect(x, y, 200, 70, "#ffffff", DONKER, 12, 2)
GH.tekst(210, 523, "episodisch", 22)
GH.tekst(430, 523, "semantisch", 22)
for k in "ABCDG":
    x, y = VAK[k]
    GH.letter(x + 100, y + 35, k)
GH.pijl(500, 140, 500, 186)
for a, b in [("B", "C"), ("B", "D"), ("C", "E"), ("C", "F"), ("D", "G")]:
    (x1, y1), (x2, y2) = VAK[a], VAK[b]
    GH.lijn(x1 + 100, y1 + 70, x2 + 100, y2, DONKER, 2)


def vak(k):
    x, y = VAK[k]
    return [Prent.zone(x, y, 200, 70)]


VRAGEN = [
    klik("Klik op het vak waarin het geheugen staat voor vaardigheden zoals fietsen.", GH.bestand, vak("G"),
         "Het procedureel geheugen hoort bij het impliciete deel van het langetermijngeheugen."),
    klik("Klik op het deel van het langetermijngeheugen dat je in woorden kan zeggen.", GH.bestand, vak("C"),
         "Het expliciete geheugen bevat het episodisch en het semantisch geheugen."),
    klik("Klik op het vak waar nieuwe informatie eerst binnenkomt.", GH.bestand, vak("A"),
         "Informatie gaat van het kortetermijngeheugen naar het langetermijngeheugen."),
    met_prent(GH.bestand, tabel("Welk vak hoort bij welk geheugen?", [
        ("langetermijngeheugen", "B"),
        ("impliciet geheugen", "D"),
        ("procedureel geheugen", "G"),
    ], "A is het kortetermijngeheugen; B splitst in expliciet (C) en impliciet (D).", kolommen=["B", "D", "G"])),
    tabel("Welk geheugen gebruik je?", [
        ("je herinnert je je eerste schooldag", "episodisch"),
        ("je weet dat water kookt bij honderd graden", "semantisch"),
        ("je typt zonder naar de toetsen te kijken", "procedureel"),
    ], "Gebeurtenissen, feiten of vaardigheden.", kolommen=["episodisch", "semantisch", "procedureel"]),
    casus(
        "Elke keer als Lien naar de tandarts gaat, hoort ze in de wachtzaal een zacht belletje en daarna "
        "doet de boor pijn. Na een paar bezoeken krijgt ze al buikpijn van schrik als ze in de winkel "
        "een gelijkaardig belletje hoort.",
        [
            tabel("Wat is wat in dit voorbeeld?", [
                ("de pijn van de boor", "ongeconditioneerde stimulus"),
                ("het belletje voor het eerste bezoek", "neutrale stimulus"),
                ("de schrik bij het belletje in de winkel", "geconditioneerde reflex"),
            ], "Wat vanzelf werkt, wat eerst niets deed, en de aangeleerde reactie.",
               kolommen=["ongeconditioneerde stimulus", "neutrale stimulus", "geconditioneerde reflex"]),
            keuze("Dit is een voorbeeld van [[*klassieke|operante]] conditionering.",
                  "Twee prikkels worden gekoppeld; het gevolg van eigen gedrag speelt geen rol."),
            mk("Bij welk bekend experiment lijkt dit het meest?",
               ["het Little Albert-experiment van Watson",
                "het Bobo doll experiment van Bandura",
                "de Skinner-box met de duwknop voor het voer",
                "de vier stadia van het denken van Piaget"], 0,
               "Ook Albert leerde bang zijn door een prikkel te koppelen aan iets angstaanjagends."),
        ],
    ),
    tabel("Positieve of negatieve bekrachtiging of straf?", [
        ("Een kind krijgt een compliment na het opruimen en ruimt vaker op.", "positieve bekrachtiging"),
        ("Wie zijn huiswerk af heeft, hoeft niet mee te helpen afwassen, en maakt het voortaan sneller.", "negatieve bekrachtiging"),
        ("Een tiener moet een extra klus doen na het roepen en roept minder.", "positieve straf"),
        ("Een kind verliest zijn speeltijd na het slaan en slaat minder.", "negatieve straf"),
    ], "Positief is toevoegen, negatief is wegnemen; bekrachtiging doet gedrag toenemen, straf doet het afnemen.",
       kolommen=["positieve bekrachtiging", "negatieve bekrachtiging", "positieve straf", "negatieve straf"]),
    keuze("Bij Skinner betekent 'negatief' [[*iets wegnemen|iets slechts|iets straffen]].",
          "Positief en negatief zijn geen oordelen maar toevoegen of wegnemen."),
    sleep("In het S-R-C-schema van Skinner staat S voor [[stimulus]], R voor [[respons]] en C voor [[consequentie]].",
          ["conditie", "reflex"], "Gedrag wordt gestuurd door wat erna komt."),
    volgorde("Zet de stadia van Piaget in de juiste volgorde.", [
        "sensomotorisch",
        "pre-operationeel",
        "concreet-operationeel",
        "formeel-operationeel",
    ], "Vier stadia in een vaste orde, zonder er een over te slaan."),
    tabel("In welk stadium van Piaget zit dit kind?", [
        ("Een baby ontdekt een rammelaar door ermee te schudden en erop te bijten.", "sensomotorisch"),
        ("Een kind van tien rekent vlot met knikkers maar niet met x en y.", "concreet-operationeel"),
        ("Een zeventienjarige bedenkt wat er zou gebeuren als er geen geld bestond.", "formeel-operationeel"),
    ], "Zintuigen en beweging, rekenen met echte dingen, abstract denken.",
       kolommen=["sensomotorisch", "concreet-operationeel", "formeel-operationeel"]),
    mk("Kinderen die een volwassene een opblaaspop zagen slaan, sloegen die daarna ook. Wat toont dat volgens Bandura?",
       ["leren kan ook door te kijken naar een model",
        "leren gebeurt enkel na een beloning of straf",
        "kinderen slaan omdat dat in hun genen zit",
        "kinderen kunnen pas abstract denken vanaf twaalf"], 0,
       "Modelleren of imitatieleren: gedrag overnemen door te kijken."),
    keuze("Bandura is een voorloper van de cognitieve benadering, omdat leren bij hem ook [[*zonder bekrachtiging|enkel met straf|enkel met beloning]] gebeurt.",
          "Kijken en nadenken volstaat al."),
    koppel("Koppel elke naam aan zijn bijdrage.", [
        ["Pavlov", "kwijlende honden en een belletje"],
        ["Watson", "het Little Albert-experiment"],
        ["Skinner", "bekrachtiging en straf in een kooitje met een knop"],
        ["Bandura", "het Bobo doll experiment"],
        ["Piaget", "vier stadia van het denken"],
    ], ["vijf fasen met erogene zones"], "Elke naam hoort bij één onderzoek of theorie."),
    sorteer("Behavioristisch of cognitief?", ["Behavioristisch", "Cognitief"], [
        ["het S-R-schema", "Behavioristisch"],
        ["kortetermijngeheugen", "Cognitief"],
        ["de Skinner-box", "Behavioristisch"],
        ["het formeel-operationele stadium", "Cognitief"],
    ], "Het behaviorisme kijkt naar zichtbaar gedrag, de cognitieve benadering naar wat in het hoofd gebeurt."),
    tabel("Klopt dit over de basisvragen bij het behaviorisme en Piaget?", [
        ("Het behaviorisme legt de nadruk op nurture.", J),
        ("Piaget geeft een discontinu antwoord, want hij werkt met stadia.", J),
        ("Bandura en Skinner leggen allebei sterk de nadruk op nature.", F),
    ], "Bijna alles is volgens hen geleerd: nurture."),
    inv("Hoe heet het kooitje waarin een dier leert door op een knop te duwen?", ["Skinner-box", "Skinnerbox", "skinner-box", "skinnerbox"],
        "De Skinner-box hoort bij de operante conditionering."),
    mk("Wat is het verschil tussen klassieke en operante conditionering?",
       ["klassiek koppelt prikkels, operant werkt via gevolgen",
        "klassiek werkt met straf, operant enkel met beloning",
        "klassiek is cognitief, operant is helemaal biologisch",
        "klassiek kwam van Skinner, operant kwam van Pavlov"], 0,
       "Bij operante conditionering stuurt het gevolg van het eigen gedrag."),
    keuze("Het Little Albert-experiment zou vandaag [[*niet|wel]] door een ethische commissie geraken.",
          "Een kind opzettelijk bang maken kan niet."),
    keuze("Een tiener die over een wet nadenkt die nog niet bestaat, zit in het [[*formeel-operationele|concreet-operationele|pre-operationele]] stadium.",
          "Abstract denken over wat nog niet bestaat."),
    inv("Welke letter komt er bij Skinner bij het S-R-schema? Eén letter.", ["C", "c"],
        "C voor consequentie."),
    mk("Een leerkracht wil dat een kind vaker zijn vinger opsteekt. Wat is positieve bekrachtiging?",
       ["een compliment geven als het zijn vinger opsteekt",
        "het kind strafwerk geven als het door de klas roept",
        "de speeltijd afnemen als het kind door de klas roept",
        "het kind negeren tot het vanzelf ophoudt met roepen"], 0,
       "Iets aangenaams toevoegen zodat het gedrag vaker voorkomt."),
    keuze("Het vlees bij de hond van Pavlov is een [[*ongeconditioneerde|neutrale|geconditioneerde]] stimulus.",
          "Het vlees werkt vanzelf, zonder dat de hond iets moest leren."),
    tabel("Klopt dit over het geheugen?", [
        ("Het episodisch geheugen bewaart gebeurtenissen uit je eigen leven.", J),
        ("Het procedureel geheugen hoort bij het expliciete geheugen.", F),
        ("Het semantisch geheugen bewaart kennis los van wanneer je ze leerde.", J),
    ], "Procedureel is impliciet: je doet het zonder erbij na te denken."),
    inv("Hoe heet het stadium van Piaget dat net voor het concreet-operationele komt?", ["pre-operationeel", "het pre-operationele", "pre-operationele", "preoperationeel"],
        "Sensomotorisch, pre-operationeel, concreet-operationeel, formeel-operationeel."),
    keuze("Een hond die een standje krijgt na op de zetel springen en het minder doet, is [[*positieve straf|negatieve straf|negatieve bekrachtiging]].",
          "Er komt iets onaangenaams bij en het gedrag neemt af."),
    mk("Waarom kijkt het behaviorisme niet naar gedachten?",
       ["het wil enkel wat je kan zien en meten",
        "het vindt dat gedachten in de genen zitten",
        "het werkt enkel met baby's en peuters",
        "het onderzoekt alleen het geheugen"], 0,
       "Behaviour is gedrag: van buitenaf zichtbaar en meetbaar."),
    open_("Leg uit waarom Bandura geen zuivere behaviorist is, met het Bobo doll experiment als voorbeeld.",
          "De kinderen sloegen de pop nadat ze een volwassene dat zagen doen, zonder dat ze zelf beloond werden. Ze leerden dus door te kijken en na te denken, niet door bekrachtiging. Daarom is Bandura een voorloper van de cognitieve benadering."),
]

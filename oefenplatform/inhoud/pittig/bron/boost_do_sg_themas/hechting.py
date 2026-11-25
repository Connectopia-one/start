"""De sociale ontwikkeling en de gehechtheid — pittig (🚀 Boost doorstroom, sociale en gedragswetenschappen).

Eigen vragen strikt binnen sg_hechting: de sociale en emotionele
ontwikkeling met haar mijlpalen, gehechtheid, de vier hechtingspatronen,
scheidingsangst en angst voor vreemden. Met vier zelfgetekende
observatiekaartjes."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik
from .prent import Prent, DONKER, GRIJS, GEEL, BLAUW

OK = Prent("vier-herenigingen", "Vier kinderen van één jaar: mama komt terug in de speelkamer", "vier observatiekaartjes, letters A tot D")
KAART = [("A", 50, 70, ["Mila kijkt niet op als mama", "binnenkomt. Ze speelt verder", "en draait zich weg.", "Haar hartslag gaat wel omhoog."]),
         ("B", 510, 70, ["Tuur huilde toen mama wegging.", "Nu kruipt hij naar haar toe,", "laat zich troosten en", "gaat snel weer spelen."]),
         ("C", 50, 345, ["Jana steekt haar armpjes uit,", "klampt zich vast en", "duwt mama dan boos weg.", "Ze is lang niet te troosten."]),
         ("D", 510, 345, ["Lars loopt naar mama, blijft", "halverwege stokstijf staan", "en kijkt verward rond.", "Dan gaat hij op de grond zitten."])]
for t, x, y, regels in KAART:
    OK.rect(x, y, 440, 240, "#ffffff", DONKER, 10, 2)
    OK.rect(x + 18, y + 18, 34, 54, "#e8dcc0", DONKER, 3, 2); OK.cirkel(x + 44, y + 47, 3, DONKER, DONKER, 1)
    for i, r in enumerate(regels):
        OK.tekst(x + 70, y + 55 + i * 40, r, 21, "start")
    OK.letter(x + 405, y + 205, t)
U = "vier-herenigingen.svg"
Z = {t: [Prent.zone(x, y, 440, 240)] for t, x, y, r in KAART}

OPVANG = ("Lees het verslag van een onthaalouder.\n\n"
          "Zoë is negen maanden. Sinds een paar weken huilt ze hard als haar papa haar 's morgens afgeeft. Als de buurvrouw haar wil vastnemen, verstopt ze haar gezicht. "
          "Bij de onthaalouder zelf, die ze al maanden kent, kalmeert ze snel. Na een kwartier kruipt ze rond en komt af en toe terug om even tegen haar aan te leunen.")

VRAGEN = [
    klik("Bekijk de vier kaartjes. Klik op het kind met een veilige hechting.", U, Z["B"], "Verdriet bij het weggaan, troost bij de terugkeer, en dan weer verkennen."),
    klik("Klik op het kind met een angstig-vermijdende hechting.", U, Z["A"], "Het lijkt onverschillig, maar van binnen is er spanning."),
    klik("Klik op het kind met een angstig-ambivalente hechting.", U, Z["C"], "Vastklampen en wegduwen wisselen af."),
    klik("Klik op het kind met een gedesorganiseerde hechting.", U, Z["D"], "Er is geen vaste strategie: bevriezen en verwarring."),
    casus(OPVANG, [
        sorteer("Welk gevolg van hechting zie je?", ["scheidingsangst", "angst voor vreemden", "veilig verkennen"],
                [("Zoë huilt als papa weggaat.", "scheidingsangst"), ("Zoë verstopt haar gezicht voor de buurvrouw.", "angst voor vreemden"), ("Zoë kruipt rond en komt af en toe terug.", "veilig verkennen")],
                "Allemaal normale gevolgen van hechting."),
        mk("Wat zegt het huilen van Zoë over haar hechting?",
           ["het is normaal bij hechting", "het bewijst dat Zoë onveilig gehecht is aan haar papa", "het toont dat de onthaalouder iets fout doet", "het betekent dat Zoë nooit zal leren verkennen"],
           0, "Scheidingsangst is een normaal gevolg van hechting rond die leeftijd."),
        keuze("Zoë kalmeert bij de onthaalouder. Een kind kan zich hechten aan [[*meer dan één persoon|enkel zijn moeder|niemand buiten het gezin]].", "Wel meestal met één hoofdfiguur."),
        keuze("De angst voor vreemden komt rond [[*acht maanden|drie jaar|zes weken]], samen met de persoonspermanentie.", "Het kind herkent wie vertrouwd is en wie niet."),
    ]),
    volgorde("Zet deze vormen van spel in de volgorde waarin ze meestal verschijnen.",
             ["alleen spelen met een rammelaar", "parallel spel naast een ander kind", "samen doen-alsof spelen met rollen"],
             "Parallel spel komt voor het samen spelen."),
    sorteer("Prosociaal of antisociaal gedrag?", ["prosociaal", "antisociaal"],
            [("een vriendje troosten dat gevallen is", "prosociaal"), ("een klasgenoot uitlachen", "antisociaal"), ("je koek delen", "prosociaal"), ("met opzet een toren van een ander omstoten", "antisociaal")],
            "Gedrag dat anderen helpt tegenover gedrag dat anderen schaadt."),
    koppel("Koppel de mijlpaal aan de fase.",
           [("de sociale glimlach", "babytijd"), ("parallel spel", "peutertijd"), ("samen spelen met rollen", "kleutertijd"), ("de peergroep wordt het belangrijkst", "adolescentie")],
           ["late volwassenheid"], "De orde ligt vrij vast, het tempo niet."),
    tabel("Helpt dit een veilige hechting?",
          [("voorspelbaar reageren", J), ("warm reageren", J), ("soms troosten en soms negeren", F), ("afgestemd reageren op signalen", J)],
          "Onvoorspelbaarheid maakt een kind waakzaam."),
    mk("Een papa werkt lange dagen, maar reageert altijd warm als zijn baby huilt. Waaruit groeit de band met de baby vooral?",
       ["uit antwoorden op signalen", "uit het aantal uren dat de verzorger in huis is", "uit de genen die het kind van zijn ouders krijgt", "uit het speelgoed dat het kind krijgt"],
       0, "Een baby huilt en er komt troost. Die herhaling bouwt vertrouwen op."),
    keuze("Een peuter krijgt een woedebui in de winkel. Het gevoel is er wel, maar de [[*emotieregulatie|sociale glimlach|objectpermanentie]] nog niet.", "Je gevoel kunnen sturen."),
    keuze("De grootste stap in de emotieregulatie komt in de [[*kleutertijd|babytijd|late volwassenheid]], samen met de taal.", "Benoemen helpt sturen."),
    tabel("Klopt dit over hechting?",
          [("Een hechtingspatroon ligt na het eerste jaar voorgoed vast.", F), ("Er zijn drie vormen van onveilige hechting.", J), ("Scheidingsangst wijst altijd op onveilige hechting.", F), ("Hechting vormt het beeld van latere relaties.", J)],
          "Een hechtingspatroon is taai maar niet onveranderlijk."),
    mk("In het park speelt Tuur steeds een beetje verder van zijn mama. Waarom durft hij dat?",
       ["het weet dat het kan terugkeren", "het heeft geen angst meer, nooit en voor niemand", "het vindt zijn verzorger niet belangrijk", "het heeft nog geen persoonspermanentie"],
       0, "De veilige haven maakt verkennen mogelijk."),
    inv("Hoe heet de groep leeftijdsgenoten die in de adolescentie het belangrijkst wordt? Eén woord.", ["peergroep", "de peergroep", "leeftijdsgenoten"], "Spiegelen aan leeftijdsgenoten helpt je zoeken wie je bent."),
    keuze("Een baby huilt en wordt soms getroost en soms genegeerd. De hechting die dan voor de hand ligt, is [[*angstig-ambivalent|veilig|angstig-vermijdend]].", "Het kind wordt waakzaam en klampt zich vast."),
    keuze("De klassieke proef met een scheiding en een hereniging is de vreemde-situatieproef van [[*Ainsworth|Piaget|Kohlberg]].", "De reactie bij de hereniging zegt het meest."),
    tabel("Hoort dit bij de socio-emotionele ontwikkeling?",
          [("leren omgaan met je gevoelens", J), ("een vriendje kiezen", J), ("langer worden", F), ("prosociaal gedrag", J)],
          "Langer worden is fysiek."),
    keuze("Een kind van acht troost een vriendje. Daarvoor moet het een ander kunnen [[*begrijpen|ontwijken|nadoen]]: de sociale ontwikkeling hangt samen met het denken.", "Perspectief nemen is een cognitieve stap."),
    sleep("Gehechtheid is een [[duurzame]] band met een verzorger. Ze ontstaat in het [[eerste]] levensjaar. Een veilig gehecht kind gebruikt de verzorger als [[veilige]] haven.",
          ["korte", "tiende"], "Een band die blijft, ook als de verzorger even weg is."),
    keuze("Eén late mijlpaal zegt [[*weinig|alles]], want de spreiding tussen kinderen is groot.", "Pas als er meerdere uitblijven, kijk je beter."),
    keuze("Rond zes weken lacht een baby naar een gezicht. Dat is de [[*sociale glimlach|reflexglimlach|peergroep]].", "Een glimlach gericht op een ander."),
    tabel("Is dit een vorm van onveilige hechting?",
          [("angstig-vermijdend", J), ("angstig-ambivalent", J), ("gedesorganiseerd", J), ("veilig", F)],
          "Drie onveilige vormen naast de veilige."),
    mk("Een baby van twee maanden voelt al iets. Wat kan hij nog niet?",
       ["zijn gevoel benoemen", "huilen als hij honger heeft en zich niet goed voelt", "lachen naar een vertrouwd gezicht vlak bij hem", "schrikken van een hard en onverwacht geluid"],
       0, "Benoemen komt pas met de taal."),
    keuze("De socio-emotionele ontwikkeling [[*loopt door na|stopt na]] de adolescentie: een relatie, ouder worden en afscheid nemen vragen nieuwe stappen.", "Het hele leven lang."),
    inv("Een baby van tien maanden zet het op een huilen zodra zijn mama de kamer uit gaat. Hoe heet die angst? Eén woord.", ["scheidingsangst", "de scheidingsangst"], "Ze begint rond acht maanden."),
    open_("Leg uit hoe een verzorger kan helpen om veilige hechting op te bouwen. Geef een voorbeeld.",
          "De verzorger reageert voorspelbaar, warm en afgestemd op de signalen van het kind. Bijvoorbeeld: als de baby huilt, neemt de verzorger hem op, praat rustig en zoekt wat er scheelt. Zo leert het kind dat anderen betrouwbaar zijn en durft het later verkennen."),
]

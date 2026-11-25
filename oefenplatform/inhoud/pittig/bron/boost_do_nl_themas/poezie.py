"""Poëzie, drama en literaire stromingen — pittig (🚀 Boost doorstroom, Nederlands).

Eigen gedichtjes en vragen strikt binnen nl_poezie."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik

GEDICHT = ("Lees het gedicht.\n\n"
           "De wind waait wild door weide en wei,\n"
           "de reiger staat stil aan de rand van de sloot.\n"
           "Hij wacht en hij wacht, en het water is grijs,\n"
           "tot plots in het riet een kikker vlucht.\n\n"
           "Dan gaat hij - zo traag als de tijd -\n"
           "weer verder, alleen,\n"
           "naar het eind van de dag.")

VRAGEN = [
    casus(GEDICHT, [
        keuze("In 'De wind waait wild door weide en wei' staat [[*alliteratie|assonantie|een refrein]].", "Dezelfde beginmedeklinker in woorden vlak na elkaar."),
        keuze("De eerste strofe telt vier versregels: een [[*kwatrijn|terzine|sextet]].", "Een kwatrijn telt vier regels."),
        keuze("'Zo traag als de tijd' is een [[*vergelijking|metafoor|personificatie]].", "Er staat 'als'."),
        mk("Waarom is dit gedicht een vrij vers?",
           ["geen vast rijm of vaste maat", "het telt precies veertien regels", "de beginletters vormen samen een woord", "het heeft drie regels van 5, 7 en 5 lettergrepen"],
           0, "Een vrij vers laat rijm en maat los."),
        keuze("'Hij wacht en hij wacht' is de stijlfiguur [[*herhaling|overdrijving|ironie]].", "De herhaling laat het wachten lang aanvoelen."),
    ]),
    sorteer("Welke dichtvorm is het?", ["sonnet", "haiku", "limerick", "acrostichon"],
            [("veertien regels, verdeeld in een octaaf en een sextet", "sonnet"), ("drie regels van vijf, zeven en vijf lettergrepen", "haiku"), ("een grappig gedicht van vijf regels met rijmschema aabba", "limerick"), ("de beginletters vormen samen een naam", "acrostichon")],
            "Ook de ballade en het vrije vers zijn dichtvormen."),
    tabel("Welk rijmschema?",
          [("gepaard rijm", "aabb"), ("gekruist rijm", "abab"), ("omarmend rijm", "abba")],
          "Bij omarmend rijm sluiten de buitenste regels de binnenste in.", ["aabb", "abab", "abba"]),
    casus("Lees de strofe.\n\nIk zag de zon,\ndie zakte in zee,\nde dag die begon\nnam alle licht mee.", [
        keuze("Het rijmschema van deze strofe is [[*abab|aabb|abba]].", "Zon en begon rijmen, zee en mee rijmen."),
        keuze("Dat rijm heet [[*gekruist|gepaard|omarmend]] rijm.", "Het rijm springt telkens een regel over."),
    ]),
    koppel("Koppel de strofe aan het aantal regels.",
           [("terzine", "drie"), ("kwatrijn", "vier"), ("sextet", "zes"), ("octaaf", "acht")],
           ["twaalf"],
           "Een sonnet is een octaaf plus een sextet."),
    sorteer("Alliteratie of assonantie?", ["alliteratie", "assonantie"],
            [("ruisend riet", "alliteratie"), ("de koele, bolle bomen", "assonantie"), ("tussen twee torens", "alliteratie"), ("een lange, zware dag", "assonantie")],
            "Alliteratie herhaalt de beginmedeklinker, assonantie de klinker."),
    mk("In het gedicht over de reiger loopt een zin door over het einde van de regel. Wat doet dat enjambement?",
       ["nadruk leggen rond de breuk", "het rijmschema volledig verbergen", "het gedicht een stuk korter maken", "er een refrein van maken dat terugkeert"],
       0, "Je oog valt van de regel af terwijl de zin nog doorloopt."),
    tabel("Klopt dit over poëzie?",
          [("Een vers is één regel, een strofe een groepje regels.", J), ("Een vrij vers heeft een vast rijmschema.", F), ("Een refrein keert telkens terug.", J), ("Een enjambement is een stijlfiguur zoals herhaling.", F)],
          "Een enjambement hoort bij het ritme."),
    sorteer("Welk subgenre van het drama?", ["tragedie", "komedie", "klucht", "muziektheater"],
            [("De hoofdpersoon gaat ten onder door zijn eigen trots.", "tragedie"), ("Na veel verwarring trouwen de geliefden toch.", "komedie"), ("Een kort stuk vol verkleedpartijen en grove grappen.", "klucht"), ("Een musical over een jonge zangeres.", "muziektheater")],
            "Een komedie loopt goed af, een tragedie slecht."),
    sorteer("Welk element van de opvoeringsanalyse is dit?", ["decor", "rekwisieten", "kostumering", "grime"],
            [("een geschilderde achtergrond van een bos", "decor"), ("de brief die de actrice openscheurt", "rekwisieten"), ("de lange zwarte mantel van de koning", "kostumering"), ("de rimpels die een jonge acteur oud maken", "grime")],
            "De kleren heten kostumering."),
    mk("Een personage zegt 'Het gaat prima' met angst op zijn gezicht. Waarom is dat sterk op het toneel?",
       ["gezicht en woorden botsen", "de decorbouwer heeft zo een stuk minder werk", "de tekst van het stuk wordt er korter van", "het publiek hoort de woorden veel beter"],
       0, "Mimiek kan iets anders zeggen dan de tekst."),
    mk("Eén lichtbundel valt op één speler op een donker podium. Wat doet die belichting?",
       ["ze stuurt de aandacht", "ze vervangt het decor helemaal", "ze toont hoe laat het is in de zaal", "ze maakt het stuk een klucht"],
       0, "Belichting stuurt de aandacht en bepaalt de sfeer."),
    tabel("Hoort dit bij een opvoeringsanalyse?",
          [("de belichting", J), ("het geluid", J), ("het rijmschema", F), ("de mimiek", J)],
          "Je kijkt naar alles wat de tekst níét is."),
    sorteer("Bij welke stroming past dit?", ["middeleeuwen", "romantiek", "realisme"],
            [("getallensymboliek", "middeleeuwen"), ("een nuchtere beschrijving van kinderarbeid", "realisme"), ("dromerig verlangen van een eenzaam individu", "romantiek"), ("de ridder die zijn dame van op afstand vereert", "middeleeuwen"), ("sociale wantoestanden aanklagen", "realisme")],
            "De hoofse liefde hoort bij de middeleeuwen."),
    mk("Een middeleeuws verhaal over de belegering van een kasteel gaat eigenlijk over een ridder die een dame het hof maakt. Hoe heet dat?",
       ["dubbele gelaagdheid", "getallensymboliek", "een enjambement", "een cliffhanger op het einde"],
       0, "Onder het verhaal ligt een tweede betekenis."),
    keuze("Minneliederen zijn middeleeuwse liederen over [[*de liefde|de oorlog|het geloof]].", "Minne is het middeleeuwse woord voor liefde."),
    mk("Waarom is een realistisch verhaal over kinderarbeid nog altijd relevant?",
       ["literatuur zegt iets over toen én nu", "kinderarbeid bestaat helemaal niet meer", "het verhaal is volledig verzonnen", "realisme gebruikt veel getallensymboliek"],
       0, "Je gaat na in welke mate een tekst relevant is voor onze samenleving."),
    inv("Hoe noem je de Japanse dichtvorm van drie regels met vijf, zeven en vijf lettergrepen? Eén woord.", ["haiku", "een haiku", "de haiku"], "Een haiku."),
    keuze("Een tragedie loopt [[*slecht|goed]] af voor de hoofdpersoon.", "Vaak door een eigenschap die hem eerst groot maakte."),
    tabel("Is dit een dichtvorm?",
          [("ballade", J), ("klucht", F), ("sonnet", J), ("vrij vers", J)],
          "Een klucht is een toneelvorm."),
    keuze("Bij een opvoering heten de voorwerpen die de spelers gebruiken, zoals een glas of een brief, de [[*rekwisieten|kostumering|grime]].", "De kleren heten kostumering."),
    keuze("Een limerick eindigt met de clou in de [[*laatste|eerste|derde]] regel.", "Het rijmschema is aabba."),
    inv("Hoeveel versregels telt een sonnet? Een getal.", ["14", "veertien"], "Veertien: een octaaf en een sextet."),
    keuze("Drie, zeven en twaalf duiken in middeleeuwse teksten niet toevallig op: dat is [[*getallensymboliek|assonantie|realisme]].", "Getallen kregen een betekenis."),
    open_("Schrijf een acrostichon van drie regels met het woord ZEE.",
          "Zon zakt traag in het water,\nEen meeuw roept nog één keer,\nEen golf neemt alles mee.",
          "De beginletters van de regels vormen samen het woord."),
]

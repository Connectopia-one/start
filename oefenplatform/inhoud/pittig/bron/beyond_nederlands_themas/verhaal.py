"""Verhaalkenmerken en vertelperspectief — pittig (🌍 Beyond doorstroom, Nederlands)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus

FRAG1 = (
    "Lees het fragment.\n\n"
    "\"De sirene loeide toen ik de trap af rende. Het water stond al tot aan de derde trede. Ik dacht aan mijn grootmoeder, "
    "aan hoe zij in 1953 ook zo'n nacht had beleefd en me erover verteld had bij de kachel, met haar handen rond een kop thee. "
    "Nu was het mijn beurt. Ik greep de zaklamp en trok de deur open.\""
)

FRAG2 = (
    "Lees het fragment.\n\n"
    "\"Meneer Verbiest telde elke avond zijn muntjes, twee keer, voor hij het licht uitdeed. Kaarsen kocht hij niet; "
    "hij las bij het schijnsel van de straatlamp. Toen zijn neef om een lening kwam vragen, deed hij de deur niet eens open.\""
)

VRAGEN = [
    casus(
        FRAG1,
        [
            tabel(
                "Welk verteltechnisch begrip past bij elk stuk?",
                [
                    ("\"De sirene loeide toen ik de trap af rende.\"", "In medias res"),
                    ("de herinnering aan de grootmoeder in 1953", "Flashback"),
                    ("\"Ik greep de zaklamp en trok de deur open.\"", "Cliffhanger"),
                ],
                "Midden in de actie beginnen, terugspringen in de tijd en afbreken op het spannendste moment.",
                kolommen=["In medias res", "Flashback", "Cliffhanger"],
            ),
            mk(
                "Welke verteller is dit?",
                [
                    "Een belevende ik-verteller",
                    "Een auctoriële verteller",
                    "Een vertellende ik-verteller die jaren later terugblikt",
                    "Een meervoudig perspectief",
                ],
                0,
                "De ik staat er middenin en vertelt terwijl het gebeurt.",
            ),
            keuze(
                "Het water dat stijgt tot aan de derde trede werkt als [[*sfeerscheppende ruimte|sociale ruimte|motto]].",
                "De plaats schept dreiging en spanning.",
            ),
            tabel(
                "Klopt dit over de tijd in dit fragment?",
                [
                    ("De vertelde tijd is enkele seconden, met een sprong naar 1953.", J),
                    ("Het fragment wordt strikt chronologisch verteld.", F),
                    ("De verteltijd is ongeveer even lang als de vertelde tijd van de actie.", J),
                ],
                "De flashback doorbreekt de chronologie.",
            ),
        ],
    ),
    casus(
        FRAG2,
        [
            mk(
                "Wat voor personage is meneer Verbiest?",
                ["Een type", "Een antiheld", "Een rond personage", "Een ik-verteller"],
                0,
                "Hij valt helemaal samen met één eigenschap: gierigheid.",
            ),
            keuze(
                "Een personage met één eigenschap dat niet verandert, heet [[*vlak|rond|personaal]].",
                "Tegenover het vlakke staat het ronde personage, dat meerdere kanten heeft en verandert.",
            ),
            mk(
                "Welke verteller hoor je hier?",
                [
                    "Een verteller in de derde persoon",
                    "Een belevende ik-verteller die het meemaakt",
                    "Een onbetrouwbare ik-verteller",
                    "Een monologue intérieur",
                ],
                0,
                "Er is geen ik; meneer Verbiest wordt van buitenaf beschreven.",
            ),
        ],
    ),
    tabel(
        "Versnelling of vertraging?",
        [
            ("Twintig jaar worden samengevat in één bladzijde.", "Versnelling"),
            ("Eén minuut voor een penalty beslaat tien bladzijden.", "Vertraging"),
            ("\"De jaren gingen voorbij.\"", "Versnelling"),
        ],
        "Veel vertelde tijd in weinig verteltijd is versnelling, en omgekeerd.",
        kolommen=["Versnelling", "Vertraging"],
    ),
    volgorde(
        "Zet de delen van de spanningsboog in de juiste volgorde.",
        ["Expositie", "Stijgende actie", "Climax", "Dalende actie", "Ontknoping"],
        "De spanning bouwt op naar de climax en loopt dan af.",
    ),
    koppel(
        "Welk vertelperspectief hoort bij elke omschrijving?",
        [
            ["Buiten het verhaal, alwetend, met commentaar", "Auctoriële verteller"],
            ["Derde persoon, meekijken over de schouder van één personage", "Personale verteller"],
            ["Een ik die dingen verzwijgt of verdraait", "Onbetrouwbare verteller"],
            ["Het verhaal wisselt van personage naar personage", "Meervoudig perspectief"],
        ],
        ["Lyrische verteller", "Protagonist"],
        "Vier perspectieven uit de termenlijst.",
    ),
    tabel(
        "Thema, motief of symbool?",
        [
            ("eenzaamheid, als kerngedachte van het boek", "Thema"),
            ("een gesloten raam dat telkens terugkomt", "Motief"),
            ("een duif die voor vrede staat", "Symbool"),
        ],
        "Het thema is waar het over gaat, een motief keert terug, een symbool staat voor iets abstracts.",
        kolommen=["Thema", "Motief", "Symbool"],
    ),
    casus(
        "Lees het fragment.\n\n"
        "\"Ik heb haar fiets niet aangeraakt. Echt niet. Goed, ik stond die avond bij het rek. En ja, mijn handen waren zwart van het vet. "
        "Maar dat was van mijn eigen ketting. Denk ik.\"",
        [
            mk(
                "Welk vertelperspectief is dit?",
                [
                    "Een onbetrouwbare verteller",
                    "Een auctoriële verteller",
                    "Een personale verteller",
                    "Een meervoudig perspectief met veel personages",
                ],
                0,
                "De lezer gaat twijfelen aan wat hij te horen krijgt. Dat effect zoekt de schrijver.",
            ),
            tabel(
                "Welke details doen je twijfelen?",
                [
                    ("\"Echt niet.\"", J),
                    ("de zwarte handen", J),
                    ("\"Denk ik.\"", J),
                    ("\"Ik heb haar fiets niet aangeraakt.\"", F),
                ],
                "De ontkenning zelf is neutraal; de rest ondergraaft ze.",
            ),
        ],
    ),
    tabel(
        "Klopt dit over de structuur van een verhaal?",
        [
            ("Een open einde laat de lezer met vragen.", J),
            ("Een cyclisch verhaal eindigt waar het begon.", J),
            ("Een niet-chronologisch verhaal is slecht opgebouwd.", F),
            ("Een pointe zet op het einde alles in een ander licht.", J),
        ],
        "Het doorbreken van de chronologie is een bewuste keuze.",
    ),
    mk(
        "Een hoofdpersoon is laf, twijfelt voortdurend en doet weinig heldhaftigs. Toch draagt hij het verhaal. Wat is hij?",
        ["Een antiheld", "Een antagonist", "Een type", "Een motief"],
        0,
        "Een antiheld is niet de tegenstander, hij is de hoofdfiguur zonder heldhaftige trekken.",
    ),
    sorteer(
        "Welke soort ruimte is het vooral?",
        ["Sociale ruimte", "Symbolische ruimte", "Geografische ruimte"],
        [
            ["een villawijk tegenover een achterbuurt", "Sociale ruimte"],
            ["een kamer zonder ramen voor een personage dat zich opgesloten voelt", "Symbolische ruimte"],
            ["het verhaal speelt in Oostende in 1920", "Geografische ruimte"],
        ],
        "Waar iemand woont en zich beweegt, tekent mee wie hij is.",
    ),
    mk(
        "Wat betekent epische concentratie?",
        [
            "Het verhaal beperkt zich tot wat ertoe doet",
            "Het verhaal heeft heel veel personages en verhaallijnen",
            "Het verhaal speelt op één dag",
            "Het verhaal wordt in verzen verteld",
        ],
        0,
        "Alles wat er niet toe doet, valt weg. Daardoor krijgt elk detail gewicht.",
    ),
    sleep(
        "Bij een [[personale]] verteller kijk je mee met één personage in de derde persoon. Een [[vertellende]] ik-verteller kijkt jaren later terug. De ononderbroken gedachtestroom heet een monologue [[intérieur]].",
        ["auctoriële", "belevende"],
        "Drie begrippen rond perspectief.",
    ),
    mk(
        "Een roman begint met een citaat van een dichter, vóór het eerste hoofdstuk. Hoe heet dat?",
        ["Een motto", "Een motief", "Een pointe", "Een epiloog"],
        0,
        "Een motto geeft de lezer een sleutel of een stemming mee.",
    ),
    tabel(
        "Klopt dit over intertekstualiteit?",
        [
            ("Een tekst verwijst naar een andere tekst.", J),
            ("Wie de verwijzing herkent, leest een laag extra.", J),
            ("Het is hetzelfde als plagiaat.", F),
        ],
        "Een citaat, een naam of een scène die een ander boek oproept.",
    ),
    keuze(
        "Een negentiende-eeuws personage verveelt zich, is zwaarmoedig en ziet geen doel meer. Dat heet [[*spleen|tijdsgeest|pointe]].",
        "Spleen is verveling en melancholie tegelijk.",
    ),
    tabel(
        "Twee verhaallijnen worden om beurten verteld: een moeder in het ziekenhuis en haar zoon op weg ernaartoe, op dezelfde avond. Klopt dit?",
        [
            ("Er is gelijktijdigheid.", J),
            ("De verteller moet ze toch na elkaar brengen.", J),
            ("Dit is een flashforward.", F),
        ],
        "Gebeurtenissen vallen samen in de vertelde tijd.",
    ),
    casus(
        "Lees het fragment.\n\n"
        "\"Toen Jonas veertig werd, stond hij weer op hetzelfde perron als op zijn tiende. Dezelfde bank, dezelfde klok. "
        "De trein waarop hij toen wachtte, was nooit gekomen. Hij ging zitten en wachtte opnieuw.\"\n\n"
        "Het boek begon met: \"Jonas was tien en wachtte op het perron.\"",
        [
            mk(
                "Welke structuur heeft het boek?",
                [
                    "Een cyclische structuur",
                    "Een strikt chronologische structuur",
                    "Een structuur in medias res",
                    "Een structuur met een open begin",
                ],
                0,
                "Het verhaal eindigt waar het begon: dezelfde plaats en dezelfde scène.",
            ),
            tabel(
                "Wat kan het perron in dit boek zijn?",
                [
                    ("een motief, want het keert terug", J),
                    ("een symbool voor een leven dat stilstaat", J),
                    ("de antagonist van Jonas", F),
                ],
                "Een terugkerend beeld is een motief; een concreet ding kan voor iets abstracts staan.",
            ),
            keuze(
                "Tussen het begin en het einde liggen dertig jaar. Dat is veel [[*vertelde tijd|verteltijd|epische concentratie]].",
                "Vertelde tijd is de duur in het verhaal, verteltijd is de leestijd.",
            ),
        ],
    ),
    inv(
        "Het personage dat de protagonist tegenwerkt, heet de ... Antwoord met één woord.",
        ["antagonist", "de antagonist"],
        "De antagonist levert de weerstand.",
    ),
    tabel(
        "Klopt dit over de ik-verteller?",
        [
            ("Hij weet alleen wat hij zelf meemaakt en denkt.", J),
            ("Hij kent de gedachten van alle personages.", F),
            ("Hij kan belevend of vertellend zijn.", J),
        ],
        "Alwetend is de auctoriële verteller, niet de ik.",
    ),
    mk(
        "Een thriller laat in hoofdstuk één al zien dat het hoofdpersonage aan het einde in een cel zit. Daarna begint het verhaal bij het begin. Wat is dat eerste hoofdstuk?",
        ["Een flashforward", "Een flashback", "Een epiloog", "Een monologue intérieur"],
        0,
        "De lezer krijgt al iets te zien van wat later zal gebeuren.",
    ),
    tabel(
        "Een roman in de derde persoon volgt enkel wat Sara ziet, denkt en voelt. Klopt dit?",
        [
            ("Het is een personale verteller.", J),
            ("De lezer weet wat de andere personages denken.", F),
            ("Het verhaal staat toch in de derde persoon.", J),
        ],
        "Je kijkt mee over de schouder van één personage.",
    ),
    open_(
        "Kies een boek of film die je kent. Benoem de protagonist, de antagonist en het vertelperspectief, en leg uit waarom het personage rond of vlak is.",
        "Voorbeeld: in een jeugdroman over een meisje dat een pestkop te slim af is, is het meisje de protagonist en de pestkop de antagonist. Het verhaal wordt verteld door een belevende ik-verteller. Het meisje is een rond personage: ze begint verlegen en wordt gaandeweg zelfzeker.",
    ),
]

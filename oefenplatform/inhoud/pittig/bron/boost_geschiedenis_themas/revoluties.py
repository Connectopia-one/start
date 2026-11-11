"""Amerika, Frankrijk en de industriële omwenteling — pittig (🚀 Boost doorstroom)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="tijdlijn-1700-1900.svg", zelf=True,
         wat="Tijdlijn van 1700 tot 1900, een groot streepje om de vijftig jaar, een klein om de vijf jaar.",
         vragen="klikvragen op 1776, 1789 en het begin van de industriële revolutie"),
    dict(bestand="bestorming-bastille.jpg", zelf=False,
         wat="Schilderij van de bestorming van de Bastille door Jean-Pierre Houël (1789).",
         waar="Wikimedia Commons, zoek op 'Prise de la Bastille Houel' (publiek domein).",
         vragen="tabelvraag over de Bastille"),
    dict(bestand="coalbrookdale.jpg", zelf=False,
         wat="Coalbrookdale by Night van Philip James de Loutherbourg (1801): ijzerovens die 's nachts gloeien.",
         waar="Wikimedia Commons, zoek op 'Coalbrookdale by Night' (publiek domein).",
         vragen="meerkeuzevraag over steenkool"),
]

TL = "tijdlijn-1700-1900.svg"

VRAGEN = [
    # --- Amerikaanse Revolutie
    sorteer(
        "Was dit een oorzaak van de Amerikaanse Revolutie of niet?",
        ["Oorzaak", "Geen oorzaak"],
        [
            ["belastingen zonder vertegenwoordiging in Londen", "Oorzaak"],
            ["Londen bepaalde met wie de kolonies mochten handelen", "Oorzaak"],
            ["verlichte ideeën over vrijheid en natuurlijke rechten", "Oorzaak"],
            ["een grote hongersnood in de kolonies", "Geen oorzaak"],
        ],
        "Belastingen, handelsregels en verlichte ideeën. Van een hongersnood was geen sprake.",
    ),
    mk(
        "Wat betwistten de kolonisten met de leuze no taxation without representation?",
        [
            "Niet de belasting zelf, maar wie ze mocht opleggen",
            "Dat er ooit nog enige belasting op thee betaald moest worden",
            "Dat de Engelse koning een katholiek geloof aanhing",
            "Dat de kolonisten zelf soldaten moesten leveren aan Engeland",
        ],
        0,
        "Wie geen vertegenwoordigers in het parlement heeft, mag er ook niet belast worden. Dat is een politieke vraag.",
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin de Onafhankelijkheidsverklaring ondertekend wordt.",
        TL, [[36.9, 25, 2.6, 55]],
        "Op 4 juli 1776, in Philadelphia.",
    ),
    tabel(
        "Klopt elke uitspraak over de Amerikaanse Onafhankelijkheidsverklaring?",
        [
            ("Ze stelt dat alle mensen met gelijke rechten geboren worden.", J),
            ("Ze noemt het recht op leven, vrijheid en het streven naar geluk.", J),
            ("Ze schafte meteen de slavernij af.", F),
        ],
        "De slavernij bleef bestaan. Dat maakt de spanning in die tekst meteen zichtbaar.",
    ),
    tabel(
        "Klopt elke uitspraak over de nieuwe Amerikaanse staat?",
        [
            ("Het is een republiek met een verkozen president.", J),
            ("Bevoegdheden liggen bij de staten én bij de unie.", J),
            ("De grondwet scheidt de machten strikt.", J),
            ("Aan het hoofd staat een erfelijke koning.", F),
        ],
        "Een federale republiek met een strikte scheiding der machten, zonder koning.",
    ),
    mk(
        "Wie kreeg volgens de eerste Amerikaanse grondwet geen stemrecht? (meerdere antwoorden)",
        ["Vrouwen", "Tot slaaf gemaakte mensen", "Inheemse volkeren", "Witte mannen met bezit"],
        [0, 1, 2],
        "Vrouwen, tot slaaf gemaakte mensen en inheemse volkeren bleven uitgesloten. In veel staten moest je bezit hebben.",
    ),
    # --- Franse Revolutie
    sorteer(
        "Was dit een oorzaak van de Franse Revolutie of niet?",
        ["Oorzaak", "Geen oorzaak"],
        [
            ["de staatskas was leeg na dure oorlogen", "Oorzaak"],
            ["de derde stand betaalde de belastingen maar had niets te zeggen", "Oorzaak"],
            ["misoogsten deden de broodprijs stijgen", "Oorzaak"],
            ["Frankrijk was bezet door een vreemd leger", "Geen oorzaak"],
        ],
        "Geld, ongelijkheid en honger. Bezet was Frankrijk niet.",
    ),
    volgorde(
        "Zet deze stappen in de juiste volgorde.",
        [
            "De koning roept de Staten-Generaal samen om geld",
            "De derde stand eist stemming per hoofd in plaats van per stand",
            "De derde stand verklaart zich tot Nationale Vergadering",
            "De Bastille wordt bestormd",
        ],
        "De vraag om geld liep uit de hand: de derde stand nam zelf het woord, en daarna volgde de straat.",
    ),
    met_prent(
        "bestorming-bastille.jpg",
        tabel(
            "Bekijk het schilderij van de bestorming van de Bastille. Klopt elke uitspraak?",
            [
                ("Het gebouw stond voor de willekeur van de koning.", J),
                ("Er zaten honderden politieke gevangenen opgesloten.", F),
                ("De bestorming werd een symbool van de revolutie.", J),
            ],
            "Er zaten nauwelijks gevangenen, maar het gebouw stond voor de willekeur van de koning.",
        ),
        volgt=True,
    ),
    klik(
        "Klik op de tijdlijn op het jaar waarin de Bastille bestormd wordt.",
        TL, [[42.5, 25, 2.6, 55]],
        "Op 14 juli 1789.",
    ),
    tabel(
        "Klopt elke uitspraak over de Verklaring van de Rechten van de Mens en de Burger?",
        [
            ("Mensen worden vrij en gelijk in rechten geboren.", J),
            ("De soevereiniteit berust bij de natie.", J),
            ("Ze waarborgt de vrijheid van mening en van godsdienst.", J),
            ("Ze gaf vrouwen dezelfde politieke rechten als mannen.", F),
        ],
        "Vrouwen kregen geen gelijke politieke rechten. Daarom schreef een vrouw in 1791 een eigen verklaring.",
    ),
    inv(
        "Wie schreef in 1791 een eigen verklaring voor de rechten van de vrouw en werd twee jaar later onthoofd?",
        ["Olympe de Gouges", "de Gouges"],
        "Olympe de Gouges.",
    ),
    volgorde(
        "Zet de fasen van de Franse Revolutie in de juiste volgorde.",
        [
            "een grondwettelijke monarchie",
            "een republiek met de Terreur",
            "het Directoire",
            "de machtsovername van Napoleon",
        ],
        "Een terugkeer naar het absolutisme van voor de revolutie kwam er nooit.",
    ),
    mk(
        "Waarom is de Terreur een tegenspraak binnen de revolutie?",
        [
            "Een revolutie die rechtszekerheid wilde, liet mensen zonder proces terechtstellen",
            "De Terreur gaf de koning zijn absolute macht van voor de revolutie volledig terug",
            "Tijdens de Terreur werden de voorrechten van de adel opnieuw ingevoerd",
            "Tijdens de Terreur werd niemand gestraft, zelfs niet wie echt iets misdaan had",
        ],
        0,
        "Duizenden werden zonder behoorlijk proces terechtgesteld. Robespierre eindigde onder dezelfde guillotine.",
    ),
    mk(
        "Wat is het grootste verschil tussen de Franse samenleving voor en na de revolutie?",
        [
            "Standen met voorrechten maken plaats voor burgers die gelijk zijn voor de wet",
            "Na de revolutie is er geen enkele ongelijkheid meer tussen rijk en arm",
            "Na de revolutie mag enkel nog de adel stemmen, de derde stand verliest elk recht",
            "Na de revolutie is Frankrijk een land zonder wetten, rechtbanken of bestuur",
        ],
        0,
        "Ongelijkheid verdwijnt daarmee niet, maar ze staat niet langer in de wet.",
    ),
    tabel(
        "Wat hebben de Amerikaanse en de Franse Revolutie gemeen? Klopt elke uitspraak?",
        [
            ("Allebei beroepen ze zich op verlichte ideeën.", J),
            ("Allebei verwerpen ze een gezag waarin de bevolking niet vertegenwoordigd is.", J),
            ("Allebei leggen ze rechten vast in een geschreven tekst.", J),
            ("Allebei eindigen ze met een keizer.", F),
        ],
        "Een keizer komt er enkel in Frankrijk, en pas achteraf.",
    ),
    mk(
        "Hoe beïnvloedde de Amerikaanse Revolutie Frankrijk?",
        [
            "Franse officieren vochten mee en kwamen terug met de ideeën en het bewijs dat het kon",
            "De Amerikanen stuurden een groot leger over zee om de Franse koning af te zetten",
            "Ze had geen enkele invloed, want Frankrijk en Amerika hadden toen helemaal geen contact",
            "De Franse koning nam de Amerikaanse grondwet over",
        ],
        0,
        "Onder wie Lafayette vocht in Amerika mee.",
    ),
    sorteer(
        "Is dit een blijvend spoor van het Franse bestuur in onze streken of niet?",
        ["Blijvend spoor", "Geen spoor"],
        [
            ["de burgerlijke stand, waar geboorte en huwelijk geregistreerd worden", "Blijvend spoor"],
            ["een wetboek aan de basis van ons burgerlijk recht", "Blijvend spoor"],
            ["het metriek stelsel", "Blijvend spoor"],
            ["het Nederlands als bestuurstaal", "Geen spoor"],
        ],
        "Burgerlijke stand, wetboek en meter en kilogram bleven. Bestuurstaal werd het Frans.",
    ),
    # --- industriële revolutie
    klik(
        "Klik op de tijdlijn op de periode waarin de industriële revolutie in Groot-Brittannië begint.",
        TL, [[22.5, 25, 8.7, 55]],
        "Vanaf ongeveer 1750. Het is een proces, geen gebeurtenis met een vaste datum.",
    ),
    tabel(
        "Klopt elke uitspraak over de industriële revolutie in België?",
        [
            ("België volgde als een van de eerste landen op het vasteland.", J),
            ("Ze groeide rond Luik, Charleroi en Gent.", J),
            ("In Seraing bouwde Cockerill een bedrijf dat zijn eigen machines maakte.", J),
            ("Ze begon in België nog vóór Groot-Brittannië.", F),
        ],
        "Groot-Brittannië ging voor, België volgde snel.",
    ),
    sorteer(
        "Hoort deze vernieuwing bij de eerste industriële revolutie of komt ze pas veel later?",
        ["Eerste industriële revolutie", "Pas veel later"],
        [
            ["de stoommachine", "Eerste industriële revolutie"],
            ["machines om te spinnen en te weven", "Eerste industriële revolutie"],
            ["cokes in plaats van houtskool bij het ijzer", "Eerste industriële revolutie"],
            ["de verbrandingsmotor", "Pas veel later"],
        ],
        "Stoom, textielmachines en cokes. De verbrandingsmotor komt pas veel later.",
    ),
    koppel(
        "Wat deed elke uitvinder met de stoommachine?",
        [
            ["Newcomen", "bouwde er een om water uit mijnen te pompen"],
            ["Watt", "maakte ze veel zuiniger"],
        ],
        ["bouwde er de eerste auto mee"],
        "Een stoommachine zet warmte om in beweging.",
    ),
    met_prent(
        "coalbrookdale.jpg",
        mk(
            "Bekijk dit schilderij van gloeiende ijzerovens in de nacht. Waarom draaide alles in deze tijd op steenkool?",
            [
                "Ze stookte de stoomketels en maakte, als cokes, beter ijzer",
                "Ze was de enige brandstof die de Kerk toeliet in de fabrieken",
                "Ze werd uit de koloniën ingevoerd en was dus goedkoop",
                "Ze verving het water als aandrijving van de molens",
            ],
            0,
            "Steenkool was de brandstof voor de stoom en voor het ijzer.",
        ),
        volgt=True,
    ),
    tabel(
        "Hoe veranderde de organisatie van het werk? Klopt elke uitspraak?",
        [
            ("Het werk wordt opgesplitst in kleine, vaste handelingen.", J),
            ("Arbeiders werken samen in een fabriek in plaats van thuis.", J),
            ("Er wordt op vaste uren gewerkt, op het ritme van de machine.", J),
            ("Eén arbeider maakt een product van begin tot eind.", F),
        ],
        "Dat één arbeider alles van begin tot eind maakt, is net wat verdwijnt.",
    ),
    mk(
        "Een manufactuur wordt een fabriek. Wat is daarbij echt nieuw?",
        [
            "Machines doen het zware werk",
            "Arbeiders werken voor het eerst samen op één en dezelfde plaats",
            "Arbeiders werken voortaan thuis, met grondstof van een handelaar",
            "Arbeiders krijgen voor het eerst een loon in geld in plaats van in natura",
        ],
        0,
        "Samen werken op één plaats deed men al in de manufactuur. Nieuw is de aandrijving, eerst water en daarna stoom.",
    ),
    sorteer(
        "Is dit een aanbodfactor of een vraagfactor van de industriële revolutie in Groot-Brittannië?",
        ["Aanbodfactor", "Vraagfactor"],
        [
            ["steenkool en ijzererts in eigen bodem", "Aanbodfactor"],
            ["kapitaal uit handel en koloniën", "Aanbodfactor"],
            ["arbeidskrachten die vrijkwamen door landbouwvernieuwing", "Aanbodfactor"],
            ["een groeiende bevolking thuis", "Vraagfactor"],
            ["een groot koloniaal afzetgebied", "Vraagfactor"],
        ],
        "Aanbod maakt de productie mogelijk, vraag gaat over wie het koopt. Je hebt beide nodig.",
    ),
    mk(
        "Hoe hangen de enclosures samen met de fabrieken?",
        [
            "Kleine boeren werden van het land geduwd en belandden in de fabrieken",
            "Op de omheinde velden werden de eerste grote fabrieken en arbeiderswijken gebouwd",
            "De enclosures waren de mijnen die de steenkool voor de fabrieken leverden",
            "De fabrieken maakten de hekken voor de enclosures",
        ],
        0,
        "Minder handen op het land betekent meer handen voor de fabriek.",
    ),
    mk(
        "Waarom spreekt men van een revolutie, terwijl het meer dan een eeuw duurde?",
        [
            "De gevolgen grijpen zo diep in dat de samenleving een andere wordt",
            "Het begon met een gewapende opstand van arbeiders tegen de fabriekseigenaars",
            "Alle belangrijke machines werden in hetzelfde jaar in Engeland uitgevonden",
            "De koning schafte in één dag de landbouw af",
        ],
        0,
        "Het gaat niet om snelheid. De technieken groeiden geleidelijk, maar de manier van leven veranderde ingrijpend.",
    ),
    casus(
        "Sara maakt een werkstuk over het leven van fabrieksarbeiders in de 19de eeuw.",
        [
            tabel(
                "Welke bronnen helpen haar? Klopt elke uitspraak?",
                [
                    ("verslagen van onderzoekscommissies over de arbeidsomstandigheden", J),
                    ("cijfers over steenkoolproductie en bevolkingsgroei", J),
                    ("kaarten met kolenvelden, kanalen en spoorlijnen", J),
                    ("een roman die vorig jaar over die tijd verscheen", F),
                ],
                "Een hedendaagse roman is geen bron over die tijd zelf.",
            ),
            tabel(
                "Wat zal Sara vinden over de sociale gevolgen? Klopt elke uitspraak?",
                [
                    ("De steden groeiden snel en raakten overbevolkt.", J),
                    ("Er ontstond een nieuwe groep fabrieksarbeiders.", J),
                    ("Kinderarbeid en werkdagen van meer dan twaalf uur waren gewoon.", J),
                    ("De sociale ongelijkheid verdween.", F),
                ],
                "De ongelijkheid kreeg een nieuwe vorm: fabriekseigenaars en loonarbeiders.",
            ),
        ],
    ),
]

# -*- coding: utf-8 -*-
"""Uitdaging Nederlands 🌍 Beyond doorstroom (25 november 2026), in de vormen
van het examen van de Examencommissie: 40 vragen die alle hoofdstukken door
elkaar halen (Kim: "misschien zelfs 40 vragen bij de hogere graden"). Casussen,
tabellen, keuzelijsten, slepen, koppelen, sorteren, volgorde, vier klikvragen
op twee zelf geschreven teksten en een open schrijfopdracht. Geen nieuwe
leerstof: alles staat in de hoofdstukken van Nederlands Beyond doorstroom.
De prenten tekent inhoud/uitdaging/maak_prenten_beyond_nederlands.py.
"""
from ._ex import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus
from ._ex import klik as _klik, met_prent as _met_prent

NIVEAU = "beyond-doorstroom"
VAK = "Nederlands"
BESTAND = "beyond-nederlands-uitdaging.json"
AANTAL = 40
MAP = "/examenvormen/nederlands-beyond-uitdaging"
BRIEF = "opiniestuk-deelfietsen.svg"
GEDICHT = "gedicht-novemberstation.svg"


def regel(i, n):
    """Klikvak van regel i (vanaf 1) op een prent met n regels (zie maak_prenten)."""
    h = 90 + n * 92 + 30
    return [2, round((90 + (i - 1) * 92) / h * 100, 1), 96, round(92 / h * 100, 1)]


def klik(vraag, prent, zones, uitleg):
    return _klik(MAP, vraag, prent, zones, uitleg)


def met_prent(prent, vraag):
    return _met_prent(MAP, prent, vraag)


VRAGEN = [
    # Lezersbrief (prent): argumentatie en drogredenen
    klik("Lees de lezersbrief. Klik op de zin waarin de schrijver de persoon aanvalt in plaats van het standpunt.",
         BRIEF, [regel(4, 6)],
         "Zin 4 zegt niets over deelfietsen, maar wel iets over wie tegen is. Dat is een persoonlijke aanval: je maakt de tegenstander verdacht in plaats van zijn argument te weerleggen."),
    klik("Klik in dezelfde lezersbrief op de zin die doet alsof er maar twee mogelijkheden bestaan.",
         BRIEF, [regel(6, 6)],
         "Zin 6 is een vals dilemma: deelfietsen of een verstopte binnenstad. Er zijn nog andere oplossingen, zoals betere bussen of meer fietsenstallingen."),
    met_prent(BRIEF, mk(
        "Op welk soort argument steunt zin 3 van de lezersbrief?",
        ["een argument op gezag van een deskundige", "een argument met een vergelijking", "een argument uit cijfers van een onderzoek", "een argument dat inspeelt op angst"],
        1,
        "De schrijver vergelijkt met Gent. Zo'n vergelijking is pas sterk als beide steden echt op elkaar lijken, en dat toont de schrijver niet aan.")),
    met_prent(BRIEF, keuze(
        "In zin 5 kondigt het woord 'bovendien' een [[*extra argument|tegenargument|besluit]] aan. Het argument zelf steunt op [[*een onderzoek|een vergelijking|een persoonlijke ervaring]].",
        "Bovendien is een signaalwoord van opsomming: er komt nog een reden bij. Die reden steunt op een studie van de universiteit, een argument uit onderzoek.")),
    met_prent(BRIEF, tabel(
        "Klopt dit over de lezersbrief?",
        [
            ("Zin 2 is het standpunt van de schrijver.", J),
            ("Zin 1 is een mening en geen feit.", F),
            ("De brief is een betogende tekst.", J),
            ("Het woord 'kortom' kondigt een besluit aan.", J),
        ],
        "Zin 1 kun je natellen, dus het is een feit. Zin 2 begint met 'daarom' en zegt wat er moet gebeuren: dat is het standpunt. Wie de lezer wil overtuigen van een standpunt, schrijft een betoog.")),

    tabel(
        "Welke vaste tekststructuur heeft elke tekst?",
        [
            ("een stappenplan om een fietsband te plakken", "Handelingsstructuur"),
            ("een artikel over hoe de gsm in dertig jaar veranderde", "Ontwikkelingsstructuur"),
            ("een test van drie laptops op prijs, gewicht en batterij", "Vergelijkingsstructuur"),
            ("een tekst die uitlegt waarom het bliksemt", "Verklaringsstructuur"),
        ],
        "Stappen: handeling. Verandering door de tijd: ontwikkeling. Dingen naast elkaar zetten: vergelijking. Uitleggen hoe of waarom: verklaring.",
        kolommen=["Handelingsstructuur", "Ontwikkelingsstructuur", "Vergelijkingsstructuur", "Verklaringsstructuur"]),

    # Gedicht (prent): poëzie en stijlfiguren
    klik("Lees het gedicht 'Novemberstation'. Klik op het vers waarin twee zintuigen door elkaar lopen.",
         GEDICHT, [regel(6, 8)],
         "Licht zie je, maar in vers 6 ruikt het licht. Een zintuig wordt met een ander beschreven: dat is synesthesie."),
    klik("Klik in hetzelfde gedicht op het vers met een vergelijking.",
         GEDICHT, [regel(4, 8)],
         "Vers 4 zegt 'zo stil als een koffer'. Door het woord 'als' worden de twee dingen naast elkaar gezet: een vergelijking, geen metafoor."),
    met_prent(GEDICHT, mk(
        "De zin van vers 2 loopt door in vers 3, zonder pauze aan het einde van de regel. Hoe heet dat?",
        ["een enjambement", "een gekruist rijm", "een alliteratie", "een retorische vraag"],
        0,
        "Bij een enjambement loopt de zin over het einde van het vers heen. Zo blijft de lezer even hangen bij 'de nacht'.")),
    met_prent(GEDICHT, tabel(
        "Klopt dit over 'Novemberstation'?",
        [
            ("In vers 1 krijgt de trein iets menselijks.", J),
            ("Verzen 7 en 8 zetten vertrekken en blijven tegenover elkaar.", J),
            ("Het gedicht heeft een vast rijmschema.", F),
            ("Een strofe van acht verzen heet een kwatrijn.", F),
        ],
        "Een trein die kreunt is een personificatie. Verzen 7 en 8 vormen een antithese. Rijm is er niet. Acht verzen is een octaaf, vier verzen een kwatrijn.")),

    # Verhaalfragment: verhaal en vertelperspectief
    casus(
        "Lees het fragment.\n\n"
        "\"Ik was twaalf toen we verhuisden. Achteraf begrijp ik dat mijn moeder die zomer elke avond huilde, maar toen hoorde ik alleen de krekels. "
        "De jaren daarna gingen voorbij in een waas van nieuwe scholen. Pas toen ik zelf kinderen had, vond ik op zolder de rode sjaal terug die ze die eerste avond "
        "om mijn nek had geknoopt.\"",
        [
            mk("Welk vertelperspectief heeft dit fragment?",
               ["een belevende ik-verteller midden in de gebeurtenissen", "een vertellende ik-verteller die terugkijkt", "een alwetende verteller buiten het verhaal", "een personale verteller in de derde persoon"],
               1,
               "Woorden als 'achteraf begrijp ik' tonen dat de ik ouder is en terugkijkt. Een belevende ik weet dat nog niet."),
            mk("'De jaren daarna gingen voorbij in een waas van nieuwe scholen.' Wat gebeurt er hier met de tijd?",
               ["De verteller vertraagt en beschrijft één moment heel lang.", "De verteller springt terug naar een vroeger moment.", "De verteller versnelt en vat jaren samen in één zin.", "De verteller vertelt alles precies zo lang als het duurde."],
               2,
               "Jaren in één zin: de vertelde tijd is veel langer dan de verteltijd. Dat is een versnelling."),
            keuze(
                "De rode sjaal komt terug aan het einde en staat voor de band met de moeder. Zo'n voorwerp met een diepere betekenis is een [[*symbool|decor|motto]].",
                "Een voorwerp dat voor iets groters staat, is een symbool. Komt een element telkens terug, dan spreek je van een motief."),
        ],
    ),

    # Nepnieuws: bronnen en framing
    casus(
        "Een bericht van een anoniem account gaat rond op sociale media:\n\n"
        "\"SCHANDAAL: school verbiedt smartphones VOLLEDIG!!! Leerlingen worden behandeld als gevangenen. Deel dit voor het te laat is! Lees meer op www.supergoedkope-gsms-nu.be\"",
        [
            tabel(
                "Welke kenmerken van dit bericht wijzen op nepnieuws?",
                [
                    ("Er staat geen auteur of bron bij.", J),
                    ("Het gebruikt hoofdletters en veel uitroeptekens.", J),
                    ("Het vraagt je dringend om het te delen.", J),
                    ("Het verschijnt op sociale media.", F),
                ],
                "Sociale media op zich bewijzen niets: ook betrouwbare kranten posten er. Een anoniem account, schreeuwerige opmaak en druk om te delen zijn wel waarschuwingssignalen."),
            mk("Het bericht noemt leerlingen 'gevangenen'. Wat doet de schrijver daarmee?",
               ["Hij brengt neutraal verslag uit van wat er gebeurde.", "Hij geeft een bron die je zelf kunt nakijken.", "Hij geeft een voorbeeld van een cirkelredenering.", "Hij framet het verbod als iets wreeds."],
               3,
               "Met één beladen woord zie je het verbod als iets wreeds. Dat is framing: het onderwerp zo voorstellen dat je het op een bepaalde manier bekijkt."),
            mk("Waarom maakt de link onderaan het bericht nog minder betrouwbaar?",
               ["Ze leidt naar een winkel die iets wil verkopen.", "Ze is te kort om bij een echte nieuwssite te horen.", "Ze eindigt op .be in plaats van op het betrouwbare .com.", "Ze staat helemaal onderaan, waar niemand ze opmerkt."],
               0,
               "Wie geld verdient aan je klik, heeft een eigen belang. Dat maakt het bericht verdacht, los van hoe de link eruitziet."),
        ],
    ),

    # Mail aan een leerkracht: register en tussentaal
    casus(
        "Een leerling stuurt deze mail aan een leerkracht:\n\n"
        "\"Hey mevrouw, ik kon gister ni komen want ik was ziek. Kunde de taak nog eens doorsturen? thx\"",
        [
            keuze(
                "Het register van deze mail is [[*te informeel|te formeel|precies goed]] voor een bericht aan een leerkracht.",
                "Tegen een leerkracht schrijf je in een verzorgd register: een aanspreking, standaardtaal en een beleefde afsluiting."),
            tabel(
                "Is dit woord uit de mail tussentaal of standaardtaal?",
                [
                    ("gister", "Tussentaal"),
                    ("ni", "Tussentaal"),
                    ("Kunde", "Tussentaal"),
                    ("doorsturen", "Standaardtaal"),
                ],
                "In standaardtaal schrijf je gisteren, niet en kunt u. Doorsturen is gewoon standaardtaal.",
                kolommen=["Tussentaal", "Standaardtaal"]),
            open_("Herschrijf de mail zodat hij past voor een leerkracht. Gebruik een aanspreking, een volledige zin en een afsluiting.",
                  "Beste mevrouw Peeters, gisteren kon ik niet naar school komen omdat ik ziek was. Zou u de taak nog eens willen doorsturen? Alvast bedankt. Met vriendelijke groeten, Lena",
                  "Let op: een beleefde aanspreking, standaardtaal (gisteren, niet, u), een vraag met 'zou u' en een groet met je naam."),
        ],
    ),

    # Zinsontleding en werkwoorden
    casus(
        "Lees de zin.\n\n\"Gisteren heeft de nieuwe directeur de leerlingen van het vijfde jaar een lange brief geschreven.\"",
        [
            sleep(
                "In deze zin is [[de nieuwe directeur]] het onderwerp. [[een lange brief]] is het lijdend voorwerp en [[de leerlingen van het vijfde jaar]] is het meewerkend voorwerp.",
                ["gisteren", "heeft geschreven"],
                "Wie schrijft? De directeur: onderwerp. Wat wordt er geschreven? Een brief: lijdend voorwerp. Aan wie? Aan de leerlingen: meewerkend voorwerp."),
            mk("Welk zinsdeel is 'gisteren'?",
               ["het naamwoordelijk deel van het gezegde", "een bijwoordelijke bepaling van tijd", "het meewerkend voorwerp", "een bijvoeglijke bepaling"],
               1,
               "Gisteren zegt wanneer iets gebeurt: een bijwoordelijke bepaling van tijd."),
            mk("Waarom staat de persoonsvorm 'heeft' vóór het onderwerp?",
               ["Omdat de zin met een ander zinsdeel begint: inversie.", "Omdat het een vraagzin is waarop iemand moet antwoorden.", "Omdat het onderwerp uit meer dan twee woorden bestaat.", "Omdat het een bijzin is die bij een hoofdzin hoort."],
               0,
               "Begint een mededelende zin met een ander zinsdeel dan het onderwerp, dan wisselen persoonsvorm en onderwerp van plaats: inversie."),
            keuze(
                "'Heeft geschreven' staat in de [[*voltooid tegenwoordige tijd|onvoltooid verleden tijd|voltooid verleden tijd]].",
                "Een vorm van hebben in de tegenwoordige tijd plus een voltooid deelwoord: voltooid tegenwoordige tijd. 'Had geschreven' zou voltooid verleden tijd zijn."),
        ],
    ),

    # Losse vragen door elkaar
    volgorde(
        "Zet deze stromingen in de juiste tijdsvolgorde, van oud naar nieuw.",
        ["hoofse literatuur", "renaissance", "verlichting", "romantiek", "naturalisme", "Vijftigers", "postmodernisme"],
        "Middeleeuwen (hoofse literatuur), vroegmoderne tijd (renaissance, verlichting), 19de eeuw (romantiek, naturalisme) en de 20ste eeuw (Vijftigers, postmodernisme)."),
    koppel(
        "Welke stroming past bij elke omschrijving?",
        [
            ["gevoel en verbeelding tegenover de rede", "romantiek"],
            ["de mens bepaald door erfelijkheid en milieu", "naturalisme"],
            ["kunst om de kunst", "Tachtigers"],
            ["de vergankelijkheid van alles in rijke beelden", "barok"],
        ],
        ["verlichting", "rederijkers"],
        "De verlichting zet net de rede voorop. De rederijkers waren stedelijke dichtersgilden aan het einde van de middeleeuwen."),
    tabel(
        "Welke tekstsoort is elke tekst?",
        [
            ("een bijsluiter bij medicijnen", "Prescriptief"),
            ("een recensie van een nieuwe film", "Opiniërend"),
            ("een krantenbericht over een overstroming", "Informatief"),
            ("een reclamefolder van een supermarkt", "Persuasief"),
        ],
        "Een bijsluiter zegt wat je moet doen, een recensie geeft een oordeel, een bericht informeert en reclame wil je overhalen.",
        kolommen=["Informatief", "Opiniërend", "Persuasief", "Prescriptief"]),
    sorteer(
        "Is dit beeldspraak of een stijlfiguur van herhaling of zinsbouw?",
        ["Beeldspraak", "Herhaling of zinsbouw"],
        [
            ["Zij is een vulkaan als ze boos wordt.", "Beeldspraak"],
            ["Het hele stadion zong mee.", "Beeldspraak"],
            ["Veni, vidi, vici: kwam, zag, overwon.", "Herhaling of zinsbouw"],
            ["Zwijgend zat hij, zat hij zwijgend.", "Herhaling of zinsbouw"],
            ["Wie niet waagt, die niet wint.", "Herhaling of zinsbouw"],
        ],
        "Een metafoor (vulkaan) en een metonymie (stadion voor de mensen) zijn beeldspraak. Een opsomming, een chiasme en parallellisme spelen met herhaling of zinsbouw."),
    keuze(
        "Gisteren [[*antwoordde|antwoorde|antwoordden]] hij niet. Wat [[*vind|vindt]] je van zijn reactie? Het [[*geplande|geplanden|gepland]] uitstapje gaat niet door.",
        "Antwoorden: stam antwoord + de = antwoordde. Bij inversie met je valt de t weg: vind je. Een voltooid deelwoord als bijvoeglijk naamwoord krijgt -e: het geplande uitstapje."),
    mk("Welk woord is een afleiding en geen samenstelling?",
       ["voetbalstadion", "schoolbordwisser", "vriendelijkheid", "verjaardagstaart"],
       2,
       "In een samenstelling zitten twee woorden die ook los bestaan (voetbal + stadion). Vriendelijkheid is vriend met de achtervoegsels -elijk en -heid: een afleiding."),
    mk("Een bedrijf schrijft 'we gaan afscheid nemen van enkele medewerkers' in plaats van 'we ontslaan mensen'. Wat is dat?",
       ["een hyperbool die alles groter maakt", "een eufemisme dat iets verzacht", "een paradox die zichzelf tegenspreekt", "een alliteratie met dezelfde beginklank"],
       1,
       "Een onaangename boodschap mooier verwoorden is een eufemisme."),
    tabel(
        "Is dit externe of interne ruis?",
        [
            ("Een bouwwerf naast het klaslokaal", "Externe ruis"),
            ("Je bent heel moe na een slechte nacht", "Interne ruis"),
            ("Het wifi-signaal valt weg tijdens een videogesprek", "Externe ruis"),
            ("Je zit met je hoofd bij een ruzie", "Interne ruis"),
        ],
        "Externe ruis komt van buitenaf. Interne ruis zit in de persoon zelf.",
        kolommen=["Externe ruis", "Interne ruis"]),
    sleep(
        "In het communicatiemodel stuurt de [[zender]] een [[boodschap]] via een [[kanaal]] naar de [[ontvanger]]. Die laat met [[feedback]] weten hoe ze aankwam.",
        ["ruis", "register"],
        "Zender, boodschap, kanaal, ontvanger en feedback zijn de vaste onderdelen. Ruis is een storing, geen onderdeel dat de boodschap draagt."),
    mk("'Als we vandaag de gsm toelaten in de klas, zitten leerlingen straks de hele dag te gamen en haalt niemand nog zijn diploma.' Welke drogreden is dit?",
       ["een hellend vlak", "een cirkelredenering", "een beroep op een autoriteit", "een persoonlijke aanval"],
       0,
       "Uit één kleine stap volgt volgens de spreker meteen een hele reeks rampen, zonder bewijs. Dat is een hellend vlak."),
    mk("'Dit is de beste smartphone, want geen enkele andere smartphone is beter.' Wat is er mis met die redenering?",
       ["Ze valt de persoon aan in plaats van het product.", "Ze maakt een kleine stap groter dan hij is.", "Het argument herhaalt gewoon het standpunt.", "Ze steunt op een deskundige die er niets van kent."],
       2,
       "Beste en geen andere is beter betekent hetzelfde. Het argument herhaalt het standpunt: een cirkelredenering."),
    mk("In een toneelstuk staan twee personages die ruzie hebben, steeds verder uit elkaar op het podium. Welk theaterteken wordt hier gebruikt?",
       ["de mimiek van de spelers", "het decor achter de spelers", "de proxemiek op het podium", "de rekwisieten in hun handen"],
       2,
       "Proxemiek gaat over de afstand tussen spelers. Meer afstand toont hier hoe ver ze van elkaar af staan."),
    mk("Een tekst gaat over schermtijd bij jongeren. Welke zin is de hoofdgedachte en niet alleen het onderwerp?",
       ["de schermtijd van Belgische jongeren tussen twaalf en achttien jaar", "jongeren en hun smartphone", "veel schermtijd gaat ten koste van de nachtrust van jongeren", "schermtijd"],
       2,
       "Het onderwerp zegt waarover het gaat. De hoofdgedachte zegt wat de tekst erover beweert, in een volledige zin."),
    tabel(
        "Welke relatie hebben de twee woorden?",
        [
            ("bank (om op te zitten) en bank (voor geld)", "Homoniemen"),
            ("snel en vlug", "Synoniemen"),
            ("warm en koud", "Antoniemen"),
            ("beginnen en starten", "Synoniemen"),
        ],
        "Homoniemen klinken en schrijf je hetzelfde maar betekenen iets anders. Synoniemen betekenen (bijna) hetzelfde, antoniemen het tegenovergestelde.",
        kolommen=["Homoniemen", "Synoniemen", "Antoniemen"]),
    mk("De woorden 'huis' en 'thuis' verwijzen naar hetzelfde gebouw, maar 'thuis' roept warmte en geborgenheid op. Hoe noem je die extra gevoelswaarde?",
       ["de denotatie", "de connotatie", "de woordherkomst", "de definitie"],
       1,
       "De denotatie is de kale betekenis. De connotatie is wat een woord daarbovenop oproept."),
    inv("Een vriend zegt: 'Ik heb wel duizend keer gebeld!' terwijl hij drie keer belde. Welke stijlfiguur is dat? Antwoord met één woord.",
        ["hyperbool", "overdrijving"],
        "Bewust overdrijven om iets kracht bij te zetten heet een hyperbool."),
    open_("Bedenk één tegenargument tegen de lezersbrief over deelfietsen en weerleg het daarna in één zin.",
          "Tegenargument: deelfietsen kosten de stad veel geld. Weerlegging: dat geld komt terug, want er zijn minder auto's en dus minder herstellingen aan de wegen.",
          "Een goede weerlegging neemt het tegenargument ernstig en toont waarom het standpunt toch overeind blijft."),
]

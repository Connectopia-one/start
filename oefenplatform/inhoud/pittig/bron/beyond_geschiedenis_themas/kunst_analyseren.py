"""Kunst en cultuur analyseren met het stappenplan — pittig (🌍 Beyond)."""
from .vormen import J, F, mk, inv, tabel, keuze, volgorde, koppel, sorteer, sleep, open_, casus, klik, met_prent

PRENTEN = [
    dict(bestand="delacroix-vrijheid.webp", zelf=False,
         wat="Eugène Delacroix, 'De Vrijheid leidt het volk' (1830).",
         waar="Wikimedia Commons, zoek op 'Delacroix Liberty Leading the People'. Publiek domein.",
         vragen="het hele stappenplan op één werk: info verzamelen, beschrijven, interpreteren, klikken op een beeldelement"),
    dict(bestand="millet-arenleesters.webp", zelf=False,
         wat="Jean-François Millet, 'De arenleesters' (1857).",
         waar="Wikimedia Commons, zoek op 'Millet The Gleaners'. Publiek domein.",
         vragen="onderwerp, doelpubliek en bedoeling bepalen, verband met de context"),
    dict(bestand="justitiepaleis-brussel.webp", zelf=False,
         wat="Een foto van het Justitiepaleis in Brussel (Poelaert, 1866-1883), van buiten, liefst het hele gebouw.",
         waar="Wikimedia Commons, zoek op 'Palais de Justice Brussels'. Kies een foto met CC BY-SA of CC0 en noteer de naam van de fotograaf.",
         vragen="een bouwwerk analyseren: bedoeling en context van een jonge staat"),
]
# Film, game, graffiti en lied: geen vrije beelden of geluid, die komen er als beschrijving in tekst.

VRAGEN = [
    # ------------------------------------------------ het stappenplan
    volgorde(
        "Zet de stappen om een kunst- of cultuuruiting te analyseren in de juiste volgorde.",
        [
            "Informatie verzamelen: tijd, ruimte, context, maker, titel en soort",
            "Beschrijven wat je ziet of hoort",
            "Interpreteren: onderwerp, doelpubliek en bedoeling, en hoe vorm en inhoud samenhangen",
            "Je analyse toelichten in een eigen tekst",
        ],
        "Eerst de feiten, dan kijken en luisteren, dan pas betekenis geven, en ten slotte alles verwoorden.",
    ),
    sorteer(
        "Bij welke stap van het stappenplan hoort deze richtvraag?",
        ["Stap 1: informatie", "Stap 2: beschrijven", "Stap 3: interpreteren"],
        [
            ["Wie heeft het gemaakt, en wanneer?", "Stap 1: informatie"],
            ["Welke materialen worden er gebruikt?", "Stap 2: beschrijven"],
            ["Welk ritme en tempo hoor je?", "Stap 2: beschrijven"],
            ["Voor wie werd het gemaakt?", "Stap 3: interpreteren"],
            ["Welke invloed heeft de maatschappelijke context op de bedoeling?", "Stap 3: interpreteren"],
        ],
        "Stap 1 gaat over feiten rond het werk, stap 2 over wat je waarneemt, stap 3 over de betekenis.",
    ),
    tabel(
        "Kan je deze uiting volgens het examen met het stappenplan analyseren?",
        [
            ("Een computerspel", J),
            ("Een graffitiwerk op een muur", J),
            ("Een protestlied", J),
            ("Een tabel met cijfers over de bevolking", F),
        ],
        "Schilderijen, beelden, gebouwen, films, games, graffiti en liederen zijn allemaal kunst- of cultuuruitingen. Een tabel met cijfers is een gewone historische bron.",
    ),
    sorteer(
        "Is dit beschrijven (stap 2) of al interpreteren (stap 3)?",
        ["Beschrijven", "Interpreteren"],
        [
            ["Op de voorgrond liggen drie lichamen.", "Beschrijven"],
            ["De achtergrond is in grijze en bruine tinten geschilderd.", "Beschrijven"],
            ["Het licht valt van links op de centrale figuur.", "Beschrijven"],
            ["De maker wil de oorlog aanklagen.", "Interpreteren"],
            ["Het werk is bedoeld voor een rijk publiek in de stad.", "Interpreteren"],
        ],
        "Beschrijven kan iedereen controleren door te kijken. Zodra je een bedoeling of een publiek invult, interpreteer je.",
    ),
    koppel(
        "Welke bedoeling past het best bij elke uiting?",
        [
            ["Een spotprent die een minister belachelijk maakt", "Bekritiseren"],
            ["Een standbeeld van de koning op een groot plein", "Bevestigen"],
            ["Een sierlijk behangpapier met bloemen", "Decoreren"],
            ["Een volkslied dat op school gezongen wordt", "Identiteit vormgeven"],
        ],
        ["Praktisch gebruiken"],
        "Praktisch gebruiken past bij een stoel of een brug: dingen die vooral een functie hebben.",
    ),
    mk(
        "Wat is het verschil tussen het onderwerp en de bedoeling van een kunstwerk?",
        [
            "Het onderwerp is waarover het gaat, de bedoeling is waarom het gemaakt werd",
            "Het onderwerp is de titel, de bedoeling is de prijs die ervoor betaald werd",
            "Het onderwerp kies je zelf als kijker, de bedoeling staat altijd in de titel",
            "Er is geen verschil, beide woorden betekenen precies hetzelfde",
        ],
        0,
        "Een werk over armoede (onderwerp) kan willen aanklagen, ontroeren of informeren (bedoeling).",
    ),
    mk(
        "Een schilderij toont een man in bed, omringd door huilende familieleden en een priester. Welk onderwerp uit het stappenplan herken je?",
        ["De dood", "Gender", "Het onrecht", "De liefde"],
        0,
        "Een sterfbed is een klassiek voorbeeld. Dat er ook verdriet en familie in zit, verandert het hoofdonderwerp niet.",
    ),
    # ------------------------------------------------ De Vrijheid leidt het volk
    met_prent("delacroix-vrijheid.webp", mk(
        "Eugène Delacroix schilderde dit in 1830, in Parijs. Welke maatschappelijke context hoort er bij stap 1?",
        [
            "De Julirevolutie, waarin Parijzenaars de koning Karel X verdreven",
            "De Franse Revolutie van 1789 en de bestorming van de Bastille",
            "De Eerste Wereldoorlog en de slag aan de Marne",
            "De Commune van Parijs na de oorlog met Pruisen",
        ],
        0,
        "Drie dagen straatgevechten in juli 1830 joegen Karel X weg. Hetzelfde jaar volgde de Belgische Revolutie.",
    ), volgt=True),
    met_prent("delacroix-vrijheid.webp", tabel(
        "Stap 2. Wat zie je op het schilderij?",
        [
            ("Een vrouw met een driekleurige vlag.", J),
            ("Mensen van verschillende standen: een man met hoge hoed, een arbeider, een jongen met pistolen.", J),
            ("Gesneuvelde mannen op de voorgrond.", J),
            ("Een koning op een troon in een paleiszaal.", F),
        ],
        "Delacroix toont het volk in al zijn lagen, samen achter de vlag, over de doden heen.",
    ), volgt=True),
    mk(
        "In De Vrijheid leidt het volk loopt een vrouw met ontblote borst en een Frygische muts voorop. Wie stelt zij voor?",
        [
            "Een allegorie: de Vrijheid zelf, die Frankrijk verbeeldt",
            "De koningin van Frankrijk, die de opstand steunde",
            "Een bekende Parijse marktvrouw die bij de gevechten sneuvelde",
            "De vrouw van de schilder, die altijd model stond",
        ],
        0,
        "Ze is geen echt persoon maar een idee in mensengedaante. In Frankrijk heet die figuur Marianne.",
    ),
    keuze(
        "De figuren staan in een [[*piramide|cirkel|rechte rij]], met de [[*vlag|zon|kerk]] op het hoogste punt. Zo trekt het belangrijkste symbool meteen de aandacht.",
        "De schikking stuurt je blik: van de doden onderaan naar de vlag bovenaan.",
    ),
    mk(
        "Welke bedoeling past het best bij De Vrijheid leidt het volk?",
        [
            "Het volk eren dat samen voor de vrijheid vecht",
            "De opstandelingen afschilderen als misdadigers",
            "Een rustig landschap tonen om een kamer te versieren",
            "Reclame maken voor een nieuw soort vlag",
        ],
        0,
        "Delacroix verheerlijkt de strijd. Hij schreef zijn broer dat hij, als hij niet voor zijn land had gevochten, er dan toch voor wou schilderen.",
    ),
    mk(
        "De Franse staat kocht het schilderij in 1831, maar hing het al snel weg uit het zicht. Wat is de meest waarschijnlijke reden?",
        [
            "Een opstand verheerlijken was voor de nieuwe koning te gevaarlijk",
            "Het schilderij was zwaar beschadigd geraakt bij het transport",
            "Niemand in Parijs vond het schilderij mooi of interessant",
            "Het was te klein voor de zalen van het museum",
        ],
        0,
        "Wat de revolutie viert, kan een nieuwe heerser schrik aanjagen. De context bepaalt mee hoe een werk ontvangen wordt.",
    ),
    # ------------------------------------------------ De arenleesters
    met_prent("millet-arenleesters.webp", tabel(
        "Jean-François Millet, De arenleesters, 1857. Stap 2: wat zie je?",
        [
            ("Drie vrouwen die zich bukken om achtergebleven aren op te rapen.", J),
            ("Op de achtergrond grote hopen graan en een volle kar.", J),
            ("Een man te paard die het werk in de verte overziet.", J),
            ("Felle, onnatuurlijke kleuren zoals paars en knalgroen.", F),
        ],
        "Millet gebruikt warme aardetinten en zacht licht. Het contrast tussen voor- en achtergrond is groot.",
    ), volgt=True),
    mk(
        "Wat maakt de schikking van De arenleesters vooral duidelijk?",
        [
            "Het verschil tussen de armen en de overvloed van anderen",
            "Dat de drie vrouwen de eigenaars van de rijke oogst zijn",
            "Dat de oogst een vrolijk feest is voor het hele dorp",
            "Dat de man te paard de vrouwen straks komt helpen rapen",
        ],
        0,
        "Het contrast toont ongelijkheid. Arenlezen was het recht van de armsten om na de oogst wat over was op te rapen.",
    ),
    mk(
        "Sommige kijkers vonden De arenleesters in 1857 verontrustend. Welke context verklaart dat?",
        [
            "De angst voor een nieuwe opstand zoals in 1848",
            "Een nieuwe wet die schilderijen over boeren en arbeiders verbood",
            "Een oorlog met Engeland die toen volop bezig was",
            "Het verbod op graanhandel in Frankrijk",
        ],
        0,
        "Na de opstanden van 1848 leken arme arbeiders in groot formaat voor sommigen een politieke dreiging.",
    ),
    keuze(
        "Het onderwerp van De arenleesters is [[*het alledaagse|de liefde|de dood]] van arme boerenvrouwen. Toch kan je er ook [[*onrecht|gender|entertainment]] in lezen.",
        "Een alledaags tafereel, maar de keuze om dit te schilderen op groot formaat is al een boodschap.",
    ),
    mk(
        "De Arenleesters hing in 1857 op de Salon, de grote kunsttentoonstelling in Parijs. Wie was daar het doelpubliek?",
        [
            "Kunstkenners, critici en welgestelde kopers uit de stad",
            "De arme boerenvrouwen die op het doek staan",
            "Kinderen die er leerden lezen en schrijven",
            "Soldaten die op weg waren naar het front",
        ],
        0,
        "Het werk toont armen, maar werd bekeken door rijken. Net dat maakte het zo scherp.",
    ),
    keuze(
        "Op De Vrijheid leidt het volk valt het felste [[*licht|schaduw|donker]] op de [[*vrouw met de vlag|gesneuvelden|huizen op de achtergrond]], terwijl de achtergrond in rook en stof verdwijnt.",
        "Licht en schaduw sturen de blik naar de belangrijkste figuur.",
    ),
    mk(
        "Waarom is stap 1 bij graffiti vaak moeilijker dan bij een schilderij in een museum?",
        [
            "De maker is vaak onbekend en een datum ontbreekt",
            "Graffiti heeft nooit kleuren of figuren",
            "Graffiti mag je volgens de wet niet bestuderen",
            "Bij graffiti is er nooit een maatschappelijke context",
        ],
        0,
        "Graffiti is vaak anoniem en verdwijnt of wordt overschilderd. Dan moet je de context uit andere bronnen halen.",
    ),
    # ------------------------------------------------ het Justitiepaleis
    met_prent("justitiepaleis-brussel.webp", tabel(
        "Stap 1. Juist of fout? Het Justitiepaleis in Brussel.",
        [
            ("Architect Joseph Poelaert ontwierp het, de bouw liep van 1866 tot 1883.", J),
            ("Het werd gebouwd op een heuvel boven de volksbuurt de Marollen.", J),
            ("Het werd gebouwd in opdracht van Napoleon.", F),
            ("Bij de bouw was het een van de grootste gebouwen van Europa.", J),
        ],
        "België bestond toen pas een paar decennia. Het gebouw is groter dan de Sint-Pietersbasiliek in Rome.",
    ), volgt=True),
    mk(
        "Welke bedoeling had de jonge Belgische staat met zo een reusachtig gerechtsgebouw?",
        [
            "Het gezag van de wet en de staat tonen",
            "Zo goedkoop mogelijk extra ruimte maken voor de rechtbanken van het land",
            "Een woning bouwen voor de koninklijke familie",
            "Werk verschaffen aan buitenlandse arbeiders",
        ],
        0,
        "Een gebouw kan ook iets zeggen. Hier spreekt het van macht, orde en de ambitie van een jong land.",
    ),
    mk(
        "Voor de bouw werd een deel van de Marollen afgebroken. Wat leer je als je ook dat perspectief meeneemt?",
        [
            "Wat voor de staat prestige was, kostte arme bewoners hun huis",
            "Het gebouw werd in de Marollen even geliefd als in de rest van het land",
            "De bewoners van de Marollen hadden zelf om het gebouw gevraagd bij de koning",
            "De afbraak had niets met het gebouw te maken",
        ],
        0,
        "In de Marollen werd architect lang een scheldwoord. Een kunstwerk kan voor verschillende groepen iets heel anders betekenen.",
    ),
    # ------------------------------------------------ film, lied, graffiti en game
    casus(
        "Charlie Chaplin, Modern Times, 1936. In deze zwart-witfilm draait een fabrieksarbeider zo lang moertjes vast aan de lopende band dat hij zelf in de machine wordt opgeslokt. Later belandt hij in de werkloosheid en in de gevangenis.",
        [
            mk(
                "Welke maatschappelijke context hoort bij deze film?",
                [
                    "De crisis van de jaren dertig en het werk aan de lopende band",
                    "De Koude Oorlog en de wapenwedloop tussen de grootmachten",
                    "De dekolonisatie van Afrika en Azië na de oorlog",
                    "De val van de Berlijnse Muur",
                ],
                0,
                "Massaproductie en de werkloosheid na de beurskrach van 1929 zijn het decor.",
            ),
            tabel(
                "Welke bedoelingen passen bij Modern Times?",
                [
                    ("Entertainen: het is een komische film.", J),
                    ("Bekritiseren: de mens wordt een onderdeel van de machine.", J),
                    ("Decoreren: de film moest een kamer mooier maken.", F),
                ],
                "Humor en kritiek gaan hier samen. Een werk kan meerdere bedoelingen hebben.",
            ),
        ],
    ),
    mk(
        "Het lied We Shall Overcome werd in de jaren zestig massaal gezongen op betogingen in de Verenigde Staten. Welke bedoeling had het daar?",
        [
            "Moed geven in de strijd tegen rassenscheiding",
            "Het publiek amuseren in de nachtclubs van New York",
            "De regering bevestigen in haar beleid",
            "Reclame maken voor een platenmaatschappij",
        ],
        0,
        "Een lied geeft een beweging een stem en een gevoel van samenhorigheid: identiteit vormgeven.",
    ),
    tabel(
        "Op de resten van de Berlijnse Muur maakten kunstenaars in 1990 meer dan honderd schilderingen. Welke vragen horen bij stap 2?",
        [
            ("Welke materialen zijn gebruikt, zoals verf uit spuitbussen op beton?", "Stap 2"),
            ("Welke figuren en kleuren zie je?", "Stap 2"),
            ("Wat wilden de kunstenaars zeggen over de val van de Muur?", "Niet stap 2"),
            ("Hoe zijn de beeldelementen op de muur geschikt?", "Stap 2"),
        ],
        "Wat de kunstenaars wilden zeggen, is een vraag naar de bedoeling. Die hoort bij stap 3.",
        kolommen=["Stap 2", "Niet stap 2"],
    ),
    mk(
        "In het computerspel This War of Mine (2014) speel je geen soldaat, maar burgers die in een belegerde stad proberen te overleven. Welke bedoeling past daarbij het best?",
        [
            "Laten voelen wat oorlog voor gewone mensen betekent",
            "Spelers leren hoe je een leger leidt",
            "Een oorlog verheerlijken als een avontuur",
            "Reclame maken voor het leger",
        ],
        0,
        "Het spel is geïnspireerd op het beleg van Sarajevo. Ook een game kan informeren en bekritiseren.",
    ),
    open_(
        "Stap 4. Licht in een korte tekst je analyse van De Vrijheid leidt het volk toe. Gebruik wat je in de vorige stappen vond.",
        "Bijvoorbeeld: De Vrijheid leidt het volk is een schilderij van Eugène Delacroix uit 1830, gemaakt na de Julirevolutie in Parijs. Je ziet een vrouw met de driekleur die mensen uit alle standen over gesneuvelden heen vooruit leidt, in een piramidevorm met de vlag als hoogste punt. De vrouw is een allegorie van de vrijheid. Het onderwerp is de revolutie, de bedoeling is het volk en de vrijheidsstrijd verheerlijken. Doordat de figuren in beweging zijn en de vlag bovenaan staat, ondersteunt de vorm die boodschap.",
    ),
    open_(
        "Waarom heb je bij elke kunst- of cultuuruiting de maatschappelijke context nodig? Leg uit met een voorbeeld uit dit hoofdstuk.",
        "Zonder context begrijp je de bedoeling niet. Bijvoorbeeld: De arenleesters lijkt een rustig boerentafereel, maar wie weet dat het in 1857 gemaakt werd, kort na de opstanden van 1848, begrijpt waarom rijke kijkers het als een aanklacht en een dreiging zagen.",
    ),
]

# -*- coding: utf-8 -*-
"""De vragen voor "Hoofdgedachte, alinea en structuuraanduiders" (🚀 Boost doorstroom, Nederlands).

Uit de vakfiche van Nederlands 2 (lezen en luisteren) en uit het stuk over
tekstopbouw dat in allebei de fiches staat: onderwerp, hoofdgedachte,
hoofdpunten, hoofd- en bijzaken, notities, de IMS-structuur, alinea's,
tussentitels en de structuuraanduiders.

Deel 1 gaat over wat een tekst zegt en hoe hij opgebouwd is. Deel 2 gaat over
de woordjes die de gedachtegang verraden: verwijswoorden en signaalwoorden, en
welk verband ze precies leggen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Je zegt in één of enkele woorden waarover een tekst gaat. Wat heb je dan bepaald?",
        opties=[
            "het onderwerp",
            "de hoofdgedachte",
            "de hoofdpunten",
            "het tekstdoel",
        ],
        antwoord=0,
        uitleg="Het onderwerp vat je in een paar woorden: sport, migratie, slaap. De hoofdgedachte vraagt een hele zin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tekst gaat over sport. De zin 'Jongeren moeten meer sporten' is de kern van wat de schrijver wil zeggen. Wat is die zin?",
        opties=[
            "de hoofdgedachte",
            "het onderwerp",
            "een hoofdpunt",
            "een signaalwoord",
        ],
        antwoord=0,
        uitleg="De hoofdgedachte is de belangrijkste boodschap, in één zin. 'Sport' alleen is het onderwerp.",
    ),
    dict(
        type="invultekst",
        vraag="Alle inhoudelijke elementen die de hoofdgedachte ondersteunen, heten de ___.",
        antwoord=["hoofdpunten", "de hoofdpunten"],
        uitleg="Bij de hoofdgedachte 'Jongeren moeten meer sporten' zijn hoofdpunten bijvoorbeeld: sport is goed voor je lichaam, en sport doet je mentaal deugd.",
    ),
    dict(
        type="waarofniet",
        vraag="De hoofdgedachte van een tekst kan je in één zin zetten.",
        antwoord=True,
        uitleg="Net dat onderscheidt haar van het onderwerp, dat in enkele woorden past, en van de hoofdpunten, die met meerdere zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke visuele hulpmiddelen van een tekst helpen je om snel te zien waarover hij gaat?",
        opties=[
            "de titel en de tussentitels",
            "de vetgedrukte woorden",
            "de foto of de grafiek erbij",
            "de marge rond de bladspiegel",
        ],
        antwoord=[0, 1, 2],
        uitleg="Titel, tussentitels, benadrukte woorden en beeldmateriaal sturen je lezen. De breedte van de marge zegt niets over de inhoud.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welk deel van een tekst met de IMS-structuur vind je meestal het besluit?",
        opties=["in het slot", "in de inleiding", "in het midden", "in de titel"],
        antwoord=0,
        uitleg="IMS staat voor inleiding, midden en slot. Het besluit sluit de gedachtegang af en staat dus achteraan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar staat de afkorting IMS voor?",
        opties=[
            "inleiding, midden en slot",
            "idee, mening en stelling",
            "inhoud, motief en structuur",
            "inleiding, mening en samenvatting",
        ],
        antwoord=0,
        uitleg="Elke goed gestructureerde tekst, gesproken of geschreven, heeft die drie delen.",
    ),
    dict(
        type="waarofniet",
        vraag="In één alinea behandel je in principe één deelonderwerp.",
        antwoord=True,
        uitleg="Daarom kan je een tekst vaak samenvatten door per alinea één zin te schrijven.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een tekstdeel dat één deelonderwerp behandelt en met een witregel of een insprong begint?",
        antwoord=["een alinea", "alinea"],
        uitleg="Alinea's zijn tekstopbouwende elementen: ze maken een tekst toegankelijker voor je lezer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je neemt notities bij een luistertekst. Wat is daarbij verstandig?",
        opties=[
            "afkortingen en symbolen gebruiken in telegramstijl",
            "elke zin letterlijk en volledig opschrijven",
            "pas achteraf uit je hoofd alles noteren",
            "alleen de woorden noteren die je niet kent",
        ],
        antwoord=0,
        uitleg="Je moet mee kunnen met het tempo. Telegramstijl, afkortingen en symbolen houden je notities kort én bruikbaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Notities zijn pas bruikbaar als het volledige zinnen zijn.",
        antwoord=False,
        uitleg="Notities moeten aansluiten bij de inhoud en duidelijk genoeg zijn om er later mee te werken. Volledige zinnen hoeft niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke vormen kan je notities ordenen?",
        opties=["in een schema", "in een tabel", "in een mindmap", "in een rijmschema"],
        antwoord=[0, 1, 2],
        uitleg="Een rijmschema beschrijft hoe de rijmklanken in een gedicht lopen. Dat is geen manier om notities te ordenen.",
    ),
    dict(
        type="invultekst",
        vraag="Wat echt telt in een tekst tegenover wat er alleen maar bij komt: dat is het onderscheid tussen hoofd- en ___.",
        antwoord=["bijzaken", "bijzaak"],
        uitleg="Hoofd- en bijzaken scheiden is de eerste stap naar een goede samenvatting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest: 'Steeds meer scholen schaffen de smartphone af. Leerkrachten zien rustigere speeltijden. Ook de resultaten gaan erop vooruit. Het verbod werkt dus.' Wat is de hoofdgedachte?",
        opties=[
            "Een smartphoneverbod op school heeft een goed effect.",
            "Leerkrachten zien rustigere speeltijden op de speelplaats.",
            "Steeds meer scholen nemen een beslissing over de smartphone.",
            "De resultaten van leerlingen gaan er dit jaar op vooruit.",
        ],
        antwoord=0,
        uitleg="De laatste zin vat het samen. De andere drie zijn hoofdpunten die de hoofdgedachte ondersteunen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet uit drie teksten relevante informatie selecteren voor één vraag. Wat doe je?",
        opties=[
            "je houdt enkel wat een antwoord op die vraag helpt geven",
            "je neemt uit elke tekst evenveel zinnen over",
            "je neemt de hele eerste alinea van elke tekst",
            "je kiest de tekst die het kortste is en laat de rest liggen",
        ],
        antwoord=0,
        uitleg="Relevant betekent: dienstig voor jouw doel. Wat mooi of opvallend is maar de vraag niet beantwoordt, laat je vallen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het onderwerp van een tekst en de titel zijn altijd hetzelfde.",
        antwoord=False,
        uitleg="Een titel wil vaak vooral je aandacht trekken. 'Het einde van de stilte' kan gaan over lawaaihinder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dienen tussentitels in een lange tekst?",
        opties=[
            "ze verdelen de tekst in herkenbare stukken",
            "ze geven de mening van de schrijver weer",
            "ze vervangen de inleiding van de tekst",
            "ze tonen welke bronnen gebruikt zijn",
        ],
        antwoord=0,
        uitleg="Tussentitels zijn tekstopbouwende elementen. Ze laten je de structuur zien nog voor je alles gelezen hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de lay-out van een geschreven tekst?",
        opties=[
            "de indeling in alinea's",
            "het gebruik van tussentitels",
            "de witruimte op de bladzijde",
            "de hoofdgedachte van de tekst",
        ],
        antwoord=[0, 1, 2],
        uitleg="Lay-out gaat over hoe de tekst eruitziet. De hoofdgedachte is inhoud, geen vormgeving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een artikel over hoe treinvertragingen ontstaan. Wat is het onderwerp?",
        opties=[
            "treinvertragingen",
            "De trein komt te vaak te laat aan.",
            "Reizigers klagen over de spoorwegen.",
            "een informatieve tekst",
        ],
        antwoord=0,
        uitleg="Het onderwerp is één of enkele woorden. De tweede en derde optie zijn hele zinnen, dus eerder een hoofdgedachte, en de vierde is een tekstsoort.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het eerste deel van de IMS-structuur?",
        antwoord=["inleiding", "de inleiding"],
        uitleg="In de inleiding zet de schrijver het onderwerp neer en wekt hij je belangstelling.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoelen we met structuuraanduiders?",
        opties=[
            "verwijswoorden en signaalwoorden",
            "titels en tussentitels",
            "alinea's en witregels",
            "voetnoten en bronvermeldingen",
        ],
        antwoord=0,
        uitleg="Structuuraanduiders zijn woorden: verwijswoorden zoals zij, hem, deze en hun, en signaalwoorden zoals maar, dus, want en hoewel.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Hoewel het stortregende, gingen we toch wandelen.' Welk verband legt 'hoewel'?",
        opties=[
            "een toegeving",
            "een oorzaak",
            "een doel",
            "een opsomming",
        ],
        antwoord=0,
        uitleg="Bij een toegeving geef je iets toe dat je zou tegenhouden, en toch gebeurt het andere. Vergelijkbaar: ondanks, niettemin.",
    ),
    dict(
        type="invultekst",
        vraag="'Ten eerste, ten tweede, ten slotte' zijn signaalwoorden voor een ___.",
        antwoord=["opsomming", "een opsomming"],
        uitleg="In een instructie kom je die reeks bijna altijd tegen, omdat de stappen in volgorde moeten.",
    ),
    dict(
        type="waarofniet",
        vraag="'Zij', 'hem' en 'deze' zijn verwijswoorden.",
        antwoord=True,
        uitleg="Verwijswoorden wijzen terug naar iets dat eerder in de tekst stond. Daardoor hoef je het niet te herhalen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke woorden kondigen een tegenstelling aan?",
        opties=["maar", "daarentegen", "echter", "bovendien"],
        antwoord=[0, 1, 2],
        uitleg="'Bovendien' voegt iets toe in dezelfde richting. De drie andere draaien de richting om.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Mits je op tijd aan de halte staat, mag je mee.' Welk verband legt 'mits'?",
        opties=["een voorwaarde", "een gevolg", "een tegenstelling", "een besluit"],
        antwoord=0,
        uitleg="Mits betekent op voorwaarde dat. Verwante signaalwoorden: als, indien, tenzij.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Het vroor die nacht. Daardoor lagen de wegen er spiegelglad bij.' Welk verband legt 'daardoor'?",
        opties=["een gevolg", "een reden", "een voorwaarde", "een toegeving"],
        antwoord=0,
        uitleg="De vorst is de oorzaak, het gladde wegdek het gevolg. Had er 'want' gestaan, dan was de tweede zin de reden geweest.",
    ),
    dict(
        type="waarofniet",
        vraag="Een signaalwoord staat altijd helemaal vooraan in de zin.",
        antwoord=False,
        uitleg="Veel signaalwoorden staan middenin: 'Hij was immers ziek', 'Dat is echter niet zeker'.",
    ),
    dict(
        type="invultekst",
        vraag="'Want' en 'omdat' geven een ___ aan.",
        antwoord=["reden", "oorzaak", "een reden"],
        uitleg="Ze zeggen waarom iets zo is. Het omgekeerde verband, het gevolg, krijg je met dus, daarom of daardoor.",
    ),
    dict(
        type="meerkeuze",
        vraag="'De leerlingen kregen hun rapport. Zij waren behoorlijk zenuwachtig.' Naar wie verwijst 'zij'?",
        opties=["de leerlingen", "de rapporten", "de leerkrachten", "de ouders"],
        antwoord=0,
        uitleg="Een verwijswoord zoekt zijn plaats in de vorige zin. Hier is dat het meervoudige onderwerp.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke woorden kondigen een samenvatting of een besluit aan?",
        opties=["kortom", "samengevat", "al met al", "bovendien"],
        antwoord=[0, 1, 2],
        uitleg="'Bovendien' voegt nog een argument toe. De drie andere sluiten de reeks af.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verwijswoord kan ook naar een hele vorige zin verwijzen, niet alleen naar één woord.",
        antwoord=True,
        uitleg="'Hij kwam niet opdagen. Dat viel tegen.' 'Dat' slaat op de hele gebeurtenis uit de vorige zin.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Opdat iedereen mee zou kunnen, huurden we een bus.' Welk verband legt 'opdat'?",
        opties=["een doel", "een oorzaak", "een tegenstelling", "een voorwaarde"],
        antwoord=0,
        uitleg="Opdat zegt waarvóór je iets doet. Vergelijkbaar: zodat, om te.",
    ),
    dict(
        type="invultekst",
        vraag="'Bijvoorbeeld' en 'zoals' kondigen een ___ aan.",
        antwoord=["voorbeeld", "een voorbeeld", "voorbeelden"],
        uitleg="Ze maken een algemene uitspraak concreet. Handig bij het lezen: na zo'n woord komt geen nieuw argument.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn signaalwoorden nuttig als je leest?",
        opties=[
            "ze laten je de gedachtegang van de schrijver reconstrueren",
            "ze vertellen je hoe lang de tekst nog duurt",
            "ze verraden welk register de schrijver gebruikt",
            "ze geven aan wie de zender van de tekst is",
        ],
        antwoord=0,
        uitleg="Aan 'maar' zie je dat er een bocht komt, aan 'dus' dat er een besluit volgt. Zo volg je de redenering ook als de inhoud moeilijk is.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tekst zonder signaalwoorden kan onmogelijk een duidelijke structuur hebben.",
        antwoord=False,
        uitleg="Structuur zit ook in de volgorde, de alinea's en de tussentitels. Signaalwoorden maken die structuur alleen zichtbaarder.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Naarmate de avond vorderde, werd het stiller in de zaal.' Welk verband legt 'naarmate'?",
        opties=[
            "hoe meer van het ene, hoe meer van het andere",
            "een zuivere tegenstelling tussen twee zaken",
            "een voorwaarde waaraan voldaan moet zijn",
            "een besluit dat uit het voorgaande volgt",
        ],
        antwoord=0,
        uitleg="Naarmate koppelt twee zaken die samen opgaan of samen afnemen. Je kan het vervangen door 'hoe later het werd, hoe stiller'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze woorden zijn verwijswoorden?",
        opties=["deze", "hun", "die", "hoewel"],
        antwoord=[0, 1, 2],
        uitleg="'Hoewel' is een signaalwoord: het legt een verband. De andere drie wijzen naar iets in de tekst.",
    ),
    dict(
        type="meerkeuze",
        vraag="'Hij kwam niet naar de training. Hij was immers ziek.' Wat geeft 'immers' aan?",
        opties=["een reden", "een gevolg", "een doel", "een tegenstelling"],
        antwoord=0,
        uitleg="Immers hoort bij want en omdat: het legt uit waarom het voorgaande zo is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk signaalwoord past in: 'Het was bitter koud. ___ trokken we onze dikste jas aan.'?",
        opties=["Daarom", "Hoewel", "Bijvoorbeeld", "Tenzij"],
        antwoord=0,
        uitleg="De kou is de oorzaak, de jas het gevolg. 'Daarom' is het signaalwoord voor een gevolg.",
    ),
]

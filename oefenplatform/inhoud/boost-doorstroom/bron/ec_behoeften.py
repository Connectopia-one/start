# -*- coding: utf-8 -*-
"""De vragen voor "Behoeften, schaarste en soorten goederen" (🚀 Boost
doorstroom, economie).

Uit de vakfiche 2de graad doorstroom economische wetenschappen, rubriek
"keuzegedrag", eerste stuk: het keuzeprobleem van de consument, de soorten
behoeften en de soorten goederen. Het nut en de indifferentiecurve staan in
[[ec_nut]], de budgetlijn in [[ec_budget]].

Deel 1 gaat over behoeften en schaarste: waarom er gekozen moet worden, en hoe
de behoeften ingedeeld worden in economische en niet-economische, en in
primaire, secundaire en tertiaire.
Deel 2 gaat over de indelingen van goederen: individueel en collectief,
tastbaar en niet-tastbaar, verbruiks- en gebruiksgoederen, en consumptie- en
investeringsgoederen.

Afspraak in dit thema: elke indeling wordt altijd met haar twee of drie
tegenpolen samen gevraagd, zodat een kind het onderscheid leert en niet één
woord uit het hoofd.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een behoefte in economische zin?",
        opties=[
            "Een gevoel van gemis dat je wil opheffen",
            "Een product dat je in de winkel kan kopen",
            "Het bedrag dat je per maand te besteden hebt",
            "Een wens die je altijd kan vervullen",
        ],
        antwoord=0,
        uitleg="Een behoefte is een gevoel van gemis. Je probeert het op te heffen met een goed of een dienst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is schaarste?",
        opties=[
            "De middelen zijn beperkt tegenover de behoeften",
            "Een product is in geen enkele winkel nog te vinden",
            "Een product is heel duur geworden door de vraag",
            "Er zijn te weinig mensen om al het werk te doen",
        ],
        antwoord=0,
        uitleg="Schaarste is geen tekort aan één product, maar het algemene gegeven dat de middelen beperkt zijn en de behoeften niet. Daarom moet er altijd gekozen worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom heeft de consument een keuzeprobleem?",
        opties=[
            "Zijn budget is te klein om alles te kopen wat hij nuttig vindt",
            "Hij weet niet in welke winkel een product het goedkoopst is",
            "Er zijn te veel merken van hetzelfde product in de winkel",
            "Hij moet eerst sparen voor hij iets kan kopen",
        ],
        antwoord=0,
        uitleg="De consument heeft meer behoeften dan middelen. Hij moet dus kiezen welke behoeften hij eerst voldoet, en welke hij laat liggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen economische en niet-economische behoeften?",
        opties=[
            "Economische behoeften voldoe je met schaarse middelen, niet-economische niet",
            "Economische behoeften gaan over geld, niet-economische over gevoelens",
            "Economische behoeften zijn primair, niet-economische zijn secundair",
            "Economische behoeften kosten meer dan niet-economische",
        ],
        antwoord=0,
        uitleg="Alleen behoeften die je met schaarse middelen voldoet, zijn economisch. Lucht inademen is een echte behoefte, maar lucht is niet schaars, dus is ze niet-economisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze behoeften zijn economische behoeften? Duid alles aan wat juist is.",
        opties=[
            "Een brood kopen voor het avondeten",
            "Naar de kapper gaan",
            "Met het openbaar vervoer naar school gaan",
            "Buiten de lucht inademen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Brood, een knipbeurt en een busrit kosten schaarse middelen. Lucht is er gewoon, dus die behoefte is niet-economisch.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je behoeften die je met schaarse middelen moet voldoen? Schrijf één woord.",
        antwoord=["economische", "economisch"],
        uitleg="Dat zijn de economische behoeften. Alleen die bestudeert de economie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke behoefte is primair?",
        opties=[
            "Eten en drinken",
            "Op reis gaan",
            "Naar een concert gaan",
            "Een tweede wagen kopen",
        ],
        antwoord=0,
        uitleg="Primaire behoeften zijn die je moet voldoen om te overleven: eten, drinken, kleding en onderdak. De andere drie zijn secundair of tertiair.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over primaire, secundaire en tertiaire behoeften kloppen? Duid alles aan wat juist is.",
        opties=[
            "Primaire behoeften zijn nodig om te overleven",
            "Secundaire behoeften maken het leven comfortabeler",
            "Tertiaire behoeften gaan over luxe en zijn niet noodzakelijk",
            "De indeling is voor iedereen in elk land precies dezelfde",
        ],
        antwoord=[0, 1, 2],
        uitleg="De drie trappen gaan van overleven over comfort naar luxe. Waar de grens ligt, verschilt wel van tijd tot tijd en van land tot land: een gsm was ooit luxe.",
    ),
    dict(
        type="waarofniet",
        vraag="Wat voor de ene een luxe is, kan voor de andere een gewone behoefte zijn.",
        antwoord=True,
        uitleg="De indeling hangt af van de tijd, het land en de persoon. Daarom is ze nuttig om over te redeneren, maar niet absoluut.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een student kiest tussen een laptop en een weekend weg. Hij kan er maar één betalen. Hoe heet wat hij opgeeft?",
        opties=[
            "De alternatieve kost",
            "De vaste kost",
            "De marginale kost",
            "De variabele kost",
        ],
        antwoord=0,
        uitleg="De alternatieve kost of opportuniteitskost is de waarde van het beste alternatief dat je laat liggen. Kiezen is altijd ook iets opgeven.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de waarde van het beste alternatief dat je opgeeft? Schrijf twee woorden.",
        antwoord=["alternatieve kost", "opportuniteitskost", "alternatieve kosten"],
        uitleg="De alternatieve kost of opportuniteitskost maakt zichtbaar dat elke keuze ook een prijs heeft in wat je niet kiest.",
    ),
    dict(
        type="waarofniet",
        vraag="Zolang een land rijk genoeg is, verdwijnt de schaarste daar.",
        antwoord=False,
        uitleg="Ook in rijke landen zijn tijd, ruimte, grondstoffen en arbeidskrachten beperkt. Schaarste verdwijnt niet, ze verschuift naar andere behoeften.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie kiest, geeft daarmee ook altijd iets anders op.",
        antwoord=True,
        uitleg="Dat bedoelt men met kiezen is verliezen: bij elke keuze blijft het beste alternatief liggen. Die alternatieve kost hoort bij elke keuze, ook bij een goede.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke middelen zijn schaars in economische zin? Duid alles aan wat juist is.",
        opties=[
            "De tijd die je per dag hebt",
            "Het budget van een gezin",
            "De grond waarop je kan bouwen",
            "Het daglicht op een zomerdag",
        ],
        antwoord=[0, 1, 2],
        uitleg="Tijd, geld en grond zijn beperkt en hebben alternatieve aanwendingen. Daglicht kost niets en is voor iedereen beschikbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gezin verdient 3 000 euro en wil voor 3 600 euro kopen. Hoe heet dat probleem?",
        opties=[
            "Het keuzeprobleem van de consument",
            "Het schaarsteprobleem van de producent",
            "Het verdelingsprobleem van de overheid",
            "Het evenwichtsprobleem van de markt",
        ],
        antwoord=0,
        uitleg="De consument moet met een te klein budget beslissen welke behoeften hij eerst voldoet: dat is zijn keuzeprobleem.",
    ),
    dict(
        type="waarofniet",
        vraag="Een behoefte die je met een gratis goed voldoet, is een economische behoefte.",
        antwoord=False,
        uitleg="Alleen behoeften die schaarse middelen vragen, zijn economisch. Een vrij goed zoals buitenlucht valt erbuiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe kiest een consument volgens de economische theorie?",
        opties=[
            "Hij kiest de producten die zijn behoeften maximaal voldoen binnen zijn budget",
            "Hij koopt altijd eerst het goedkoopste product dat hij vindt",
            "Hij koopt altijd het product met het bekendste merk",
            "Hij verdeelt zijn budget in gelijke delen over alle producten",
        ],
        antwoord=0,
        uitleg="De consument streeft naar het hoogste nut binnen wat hij kan betalen. Dat is het uitgangspunt van heel de theorie over zijn keuzegedrag.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een behoefte die je moet voldoen om te overleven? Schrijf één woord.",
        antwoord=["primaire", "primair"],
        uitleg="Primaire behoeften zijn de eerste levensbehoeften: eten, drinken, kleding en onderdak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn behoeften volgens economen onbeperkt?",
        opties=[
            "Omdat er bij elke vervulde behoefte een nieuwe bijkomt",
            "Omdat niemand ooit genoeg geld heeft om iets te kopen",
            "Omdat er elk jaar meer producten op de markt komen",
            "Omdat de prijzen elk jaar blijven stijgen",
        ],
        antwoord=0,
        uitleg="Zodra de ene behoefte voldaan is, duikt de volgende op. Dat onbeperkte karakter, tegenover beperkte middelen, is precies wat schaarste veroorzaakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gemeente legt een park aan in plaats van een parking. Wat is hier de alternatieve kost?",
        opties=[
            "De parking die er niet komt",
            "De prijs van de grond van het park",
            "Het onderhoud van het park per jaar",
            "De belastingen die de inwoners betalen",
        ],
        antwoord=0,
        uitleg="De alternatieve kost is wat je opgeeft: de beste andere bestemming van dezelfde grond. Dat is hier de parking.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een individueel en een collectief goed?",
        opties=[
            "Een individueel goed gebruik je alleen, een collectief goed gebruikt iedereen samen",
            "Een individueel goed is duur, een collectief goed is goedkoop",
            "Een individueel goed is tastbaar, een collectief goed niet",
            "Een individueel goed koop je in de winkel, een collectief goed op het internet",
        ],
        antwoord=0,
        uitleg="Een broodje eet jij alleen op. Straatverlichting brandt voor iedereen tegelijk, en je kan niemand uitsluiten: dat is een collectief goed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zijn collectieve goederen? Duid alles aan wat juist is.",
        opties=[
            "De straatverlichting in een gemeente",
            "De dijken aan de kust",
            "Het leger van een land",
            "Een abonnement op een streamingdienst",
        ],
        antwoord=[0, 1, 2],
        uitleg="Verlichting, dijken en defensie gebruikt iedereen samen en niemand kan je ervan uitsluiten. Een abonnement is net wél individueel: wie niet betaalt, kijkt niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie zorgt meestal voor collectieve goederen, en waarom?",
        opties=[
            "De overheid, want niemand kan uitgesloten worden van het gebruik",
            "De bedrijven, want zij kunnen ze het goedkoopst van allemaal maken",
            "De gezinnen, want zij gebruiken ze het vaakst",
            "Het buitenland, want zulke goederen worden altijd ingevoerd",
        ],
        antwoord=0,
        uitleg="Als niemand uitgesloten kan worden, kan je er geen prijs voor vragen. Een bedrijf zou er dus niets aan verdienen, en daarom zorgt de overheid ervoor, betaald met belastingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een tastbaar en een niet-tastbaar goed?",
        opties=[
            "Een tastbaar goed kan je vastnemen, een niet-tastbaar niet",
            "Een tastbaar goed is altijd nieuw, een niet-tastbaar altijd tweedehands",
            "Een tastbaar goed koop je, een niet-tastbaar goed huur je",
            "Een tastbaar goed gaat lang mee, een niet-tastbaar goed niet",
        ],
        antwoord=0,
        uitleg="Een fiets is tastbaar, een fietsles niet. Niet-tastbare goederen noemen we diensten.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een niet-tastbaar goed met één woord?",
        antwoord=["dienst", "diensten"],
        uitleg="Een dienst is niet-tastbaar: een knipbeurt, een treinrit of een les.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een verbruiksgoed en een gebruiksgoed?",
        opties=[
            "Een verbruiksgoed verdwijnt bij het gebruik, een gebruiksgoed gaat langer mee",
            "Een verbruiksgoed is goedkoop, een gebruiksgoed is duur",
            "Een verbruiksgoed koop je bij een bedrijf, een gebruiksgoed bij een gezin",
            "Een verbruiksgoed is tastbaar, een gebruiksgoed niet",
        ],
        antwoord=0,
        uitleg="Benzine en brood zijn na één keer op: dat zijn verbruiksgoederen. Een fiets of een wasmachine gebruik je keer op keer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn verbruiksgoederen? Duid alles aan wat juist is.",
        opties=[
            "Een liter benzine",
            "Een brood",
            "Tandpasta",
            "Een wasmachine",
        ],
        antwoord=[0, 1, 2],
        uitleg="Benzine, brood en tandpasta gaan op bij het gebruik. Een wasmachine blijft bestaan en is dus een gebruiksgoed.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gebruiksgoed verdwijnt bij het eerste gebruik.",
        antwoord=False,
        uitleg="Dat is net een verbruiksgoed. Een gebruiksgoed, zoals een fiets of een gsm, gaat langere tijd mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een consumptiegoed en een investeringsgoed?",
        opties=[
            "Een consumptiegoed voldoet behoeften, een investeringsgoed produceert",
            "Een consumptiegoed is altijd goedkoop, een investeringsgoed altijd duur",
            "Een consumptiegoed is nieuw, een investeringsgoed tweedehands",
            "Een consumptiegoed koop je zelf, een investeringsgoed krijg je van de overheid",
        ],
        antwoord=0,
        uitleg="Het hangt af van wie het gebruikt en waarvoor. Dezelfde bestelwagen is een investeringsgoed voor een loodgieter en een consumptiegoed voor wie er mee op reis gaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bakker koopt een nieuwe oven. Hoe heet dat goed voor hem?",
        opties=[
            "Een investeringsgoed",
            "Een consumptiegoed",
            "Een collectief goed",
            "Een verbruiksgoed",
        ],
        antwoord=0,
        uitleg="Hij koopt de oven om mee te produceren, dus het is een investeringsgoed, ook wel kapitaalgoed genoemd.",
    ),
    dict(
        type="waarofniet",
        vraag="Hetzelfde goed kan voor de ene een investeringsgoed zijn en voor de andere een consumptiegoed.",
        antwoord=True,
        uitleg="Een auto is een investeringsgoed voor een taxichauffeur en een consumptiegoed voor een gezin. Het gebruik bepaalt de indeling.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een goed dat je gebruikt om mee te produceren? Schrijf één woord.",
        antwoord=["investeringsgoed", "kapitaalgoed", "investeringsgoederen"],
        uitleg="Een investerings- of kapitaalgoed dient niet om te verbruiken, maar om er andere goederen mee te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gezin koopt een auto om mee op vakantie te gaan. In welke indelingen past die auto? Duid alles aan wat juist is.",
        opties=[
            "Een individueel goed",
            "Een tastbaar goed",
            "Een gebruiksgoed",
            "Een collectief goed",
        ],
        antwoord=[0, 1, 2],
        uitleg="De auto is van dit gezin, je kan hem vastnemen, en hij gaat jaren mee. Collectief is hij niet: anderen kunnen er niet zomaar mee rijden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vrij goed is een goed dat er in overvloed is en dat niets kost.",
        antwoord=True,
        uitleg="Een vrij goed, zoals buitenlucht, is niet schaars. Daarom heeft het geen prijs en valt het buiten de economie.",
    ),
    dict(
        type="waarofniet",
        vraag="Drinkbaar leidingwater is een vrij goed.",
        antwoord=False,
        uitleg="Het moet opgepompt, gezuiverd en vervoerd worden, en dat kost schaarse middelen. Daarom betaal je ervoor: het is een economisch goed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een school is voor wie er leert een dienst. Hoe past onderwijs in de indelingen?",
        opties=[
            "Als een dienst die de overheid grotendeels collectief aanbiedt",
            "Als een tastbaar goed, want er staat een schoolgebouw op de speelplaats",
            "Als een verbruiksgoed, want een schooljaar is daarna op",
            "Als een investeringsgoed van het gezin, want het kost geld",
        ],
        antwoord=0,
        uitleg="Onderwijs is een dienst, dus niet-tastbaar, en de overheid biedt het grotendeels aan voor iedereen. Het gebouw is wel tastbaar, maar dat is niet wat je koopt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn deze indelingen nuttig?",
        opties=[
            "Ze tonen wie iets aanbiedt, wie betaalt en hoe lang het meegaat",
            "Ze bepalen welke prijs een product in de winkel uiteindelijk krijgt",
            "Ze beslissen welke producten een land mag invoeren",
            "Ze leggen vast hoeveel belasting op een product komt",
        ],
        antwoord=0,
        uitleg="De indelingen helpen redeneren: wie zorgt voor een goed, waarom de markt het al dan niet aanbiedt, en of het om verbruiken of produceren gaat.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een goed dat iedereen samen gebruikt en waarvan je niemand kan uitsluiten? Schrijf één woord.",
        antwoord=["collectief", "collectieve", "collectief goed"],
        uitleg="Een collectief goed, zoals straatverlichting of een dijk, wordt door de overheid aangeboden en met belastingen betaald.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een drukkerij koopt papier om er boeken mee te maken. Hoe noem je dat papier?",
        opties=[
            "Een intermediair goed, want het gaat op in een ander product",
            "Een consumptiegoed, want het wordt verbruikt",
            "Een collectief goed, want de boeken gaan naar veel mensen",
            "Een investeringsgoed, want de drukkerij gebruikt het om te produceren",
        ],
        antwoord=0,
        uitleg="Een intermediair goed wordt in de productie verwerkt tot iets anders. Een investeringsgoed, zoals de drukpers zelf, blijft bestaan en gaat er niet in op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom tellen intermediaire goederen niet apart mee in het bbp?",
        opties=[
            "Omdat hun waarde al in het eindproduct zit",
            "Omdat ze meestal uit het buitenland ingevoerd worden",
            "Omdat ze niet door de gezinnen gekocht worden",
            "Omdat ze te goedkoop zijn om te tellen",
        ],
        antwoord=0,
        uitleg="Anders tel je dezelfde waarde twee keer. Daarom werkt het bbp met toegevoegde waarden en niet met omzetten.",
    ),
]

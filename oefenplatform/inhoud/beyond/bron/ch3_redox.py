# -*- coding: utf-8 -*-
"""Oxidatiegetallen en redoxreacties — 🌍 Beyond, chemie.

Deel 1 gaat over het oxidatiegetal: de afspraken om het te bepalen in een
verbinding of een ion, ook bij koolstof in een organische stof, en over de
begrippen oxidatie, reductie, oxidator en reductor. Deel 2 gaat over de
reactievergelijking: de elektronenuitwisseling, het opstellen in zuur, basisch
en neutraal midden, en het voorspellen met de tabel van de normpotentialen of
een reactie tussen twee redoxkoppels spontaan doorgaat.

De tabel met normpotentialen krijgt het kind op het examen. Daarom staan de
nodige waarden in de vraag zelf, en gaat de vraag over wat je eruit afleidt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welk oxidatiegetal heeft een atoom in een enkelvoudige stof?",
        opties=[
            "nul",
            "plus een",
            "min een",
            "gelijk aan het groepsnummer",
        ],
        antwoord=0,
        uitleg="In O₂, Fe en Cl₂ is er geen enkel verschil tussen de atomen. Er is dus "
        "geen reden om elektronen aan de ene of de andere toe te wijzen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk oxidatiegetal heeft zuurstof in de meeste verbindingen?",
        opties=[
            "min twee",
            "min een",
            "plus twee",
            "nul",
        ],
        antwoord=0,
        uitleg="Enkel in een peroxide is het min een, want daar zit een O-O-brug. In OF₂ "
        "is het zelfs positief.",
    ),
    dict(
        type="invultekst",
        vraag="Welk oxidatiegetal heeft waterstof in een verbinding met een niet-metaal?",
        antwoord=["+I", "+1", "plus een"],
        uitleg="In een metaalhydride zoals NaH is het min een, want daar is waterstof het "
        "meest elektronegatieve atoom.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk oxidatiegetal heeft zwavel in zwavelzuur H₂SO₄?",
        opties=[
            "+VI",
            "+IV",
            "−II",
            "+II",
        ],
        antwoord=0,
        uitleg="Twee keer +I plus vier keer −II is −6. Zwavel moet dus +VI zijn om op nul "
        "uit te komen.",
    ),
    dict(
        type="waarofniet",
        vraag="De som van de oxidatiegetallen in een neutrale verbinding is nul.",
        antwoord=True,
        uitleg="Bij een ion is die som gelijk aan de lading van het ion. Dat is de "
        "controle waarmee je elk oxidatiegetal kan narekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk oxidatiegetal heeft mangaan in het permanganaation MnO₄⁻?",
        opties=[
            "+VII",
            "+VI",
            "+IV",
            "+II",
        ],
        antwoord=0,
        uitleg="Vier keer −II is −8, en het hele ion heeft lading −1. Mangaan moet dus "
        "+VII zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij een oxidatie?",
        opties=[
            "een deeltje staat elektronen af en zijn oxidatiegetal stijgt",
            "een deeltje neemt elektronen op en zijn oxidatiegetal daalt",
            "een deeltje staat een proton af aan een ander deeltje",
            "een deeltje neemt zuurstof op uit de lucht",
        ],
        antwoord=0,
        uitleg="Oxidatie heeft niet noodzakelijk met zuurstof te maken. Het gaat om het "
        "afstaan van elektronen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een oxidator zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "hij neemt elektronen op",
            "hij wordt zelf gereduceerd",
            "hij staat elektronen af",
            "hij wordt zelf geoxideerd",
        ],
        antwoord=[0, 1],
        uitleg="Een oxidator zorgt dat een ander deeltje oxideert, en ondergaat dus zelf "
        "de reductie. De reductor doet net het omgekeerde.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het deeltje dat elektronen afstaat in een redoxreactie?",
        antwoord=["reductor", "de reductor", "reducens"],
        uitleg="Door elektronen af te staan laat hij het andere deeltje reduceren. Zelf "
        "wordt hij geoxideerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk oxidatiegetal heeft koolstof in methaan CH₄?",
        opties=[
            "−IV",
            "+IV",
            "−II",
            "nul",
        ],
        antwoord=0,
        uitleg="Vier keer +I voor de waterstof moet weggewerkt worden. Koolstof is hier "
        "dus het meest gereduceerd dat het kan zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de verbranding van methaan wordt koolstof geoxideerd.",
        antwoord=True,
        uitleg="Koolstof gaat van −IV in CH₄ naar +IV in CO₂. Dat is acht eenheden "
        "stijging, en dus een oxidatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk oxidatiegetal heeft chroom in het dichromaation Cr₂O₇²⁻?",
        opties=[
            "+VI",
            "+III",
            "+VII",
            "+II",
        ],
        antwoord=0,
        uitleg="Zeven keer −II is −14, het ion heeft lading −2. De twee chroomatomen "
        "dragen dus samen +12.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke stoffen heeft zuurstof níet het oxidatiegetal −II? Kruis alles aan wat juist is.",
        opties=[
            "in waterstofperoxide H₂O₂",
            "in zuurstofgas O₂",
            "in water H₂O",
            "in koolstofdioxide CO₂",
        ],
        antwoord=[0, 1],
        uitleg="In een peroxide is het −I door de O-O-brug, en in de enkelvoudige stof "
        "nul. In water en CO₂ is het gewoon −II.",
    ),
    dict(
        type="invultekst",
        vraag="Welk oxidatiegetal heeft stikstof in het nitraation NO₃⁻?",
        antwoord=["+V", "+5", "plus vijf"],
        uitleg="Drie keer −II is −6, het ion heeft lading −1. Stikstof komt dus op +V uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="IJzer gaat van Fe²⁺ naar Fe³⁺. Wat is er gebeurd?",
        opties=[
            "het is geoxideerd en heeft een elektron afgestaan",
            "het is gereduceerd en heeft een elektron opgenomen",
            "het heeft een proton afgestaan aan het water",
            "het heeft een zuurstofatoom opgenomen uit de lucht",
        ],
        antwoord=0,
        uitleg="Het oxidatiegetal stijgt van +II naar +III. Elke stijging is een "
        "oxidatie, en daarbij gaan er elektronen weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een redoxreactie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "er is altijd een oxidatie en een reductie samen",
            "het aantal afgestane elektronen is gelijk aan het aantal opgenomen",
            "er kan een oxidatie gebeuren zonder reductie",
            "de oxidatiegetallen blijven allemaal gelijk",
        ],
        antwoord=[0, 1],
        uitleg="Elektronen kunnen niet los blijven rondzweven. Wat het ene deeltje "
        "afstaat, neemt het andere op.",
    ),
    dict(
        type="waarofniet",
        vraag="Koolstof heeft in elke organische verbinding hetzelfde oxidatiegetal.",
        antwoord=False,
        uitleg="In methanol is het −II, in methanal nul en in methaanzuur +II. Zo zie je "
        "dat de reeks alcohol, aldehyde en zuur telkens een oxidatie is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk oxidatiegetal heeft koolstof in koolstofdioxide?",
        opties=[
            "+IV",
            "−IV",
            "+II",
            "nul",
        ],
        antwoord=0,
        uitleg="Twee keer −II moet weggewerkt worden. Koolstof is hier dus zo sterk "
        "geoxideerd als het kan zijn, en dat is waarom CO₂ niet meer brandt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof die zuurstof opneemt, wordt altijd gereduceerd.",
        antwoord=False,
        uitleg="Net omgekeerd: zuurstof opnemen is meestal een oxidatie, want zuurstof "
        "trekt de elektronen naar zich toe.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de reactie waarbij een deeltje elektronen opneemt?",
        antwoord=["reductie", "een reductie", "reduceren"],
        uitleg="Het oxidatiegetal daalt daarbij. De oxidator is het deeltje dat die "
        "reductie zelf ondergaat.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is de eerste stap bij het opstellen van een redoxvergelijking?",
        opties=[
            "de oxidatiegetallen bepalen en zien welk atoom verandert",
            "de vergelijking meteen uitbalanceren met coëfficiënten",
            "water en hydroxoniumionen aan beide kanten bijzetten",
            "de normpotentialen van de twee koppels opzoeken",
        ],
        antwoord=0,
        uitleg="Pas als je weet wat oxideert en wat reduceert, kan je de halfreacties "
        "schrijven en het aantal elektronen gelijkstellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom moet je de twee halfreacties met een factor vermenigvuldigen?",
        opties=[
            "het aantal afgestane en opgenomen elektronen moet gelijk zijn",
            "de coëfficiënten moeten zo klein mogelijk gehouden worden",
            "de lading van de hele vergelijking moet nul worden",
            "het aantal watermoleculen links en rechts moet gelijk zijn",
        ],
        antwoord=0,
        uitleg="Staat de ene halfreactie twee elektronen af en neemt de andere er drie "
        "op, dan vermenigvuldig je met drie en met twee.",
    ),
    dict(
        type="invultekst",
        vraag="Welke deeltjes gebruik je om een redoxvergelijking in zuur midden in evenwicht te brengen?",
        antwoord=["water en H3O+", "H3O+ en water", "water en hydroxonium"],
        uitleg="In basisch midden gebruik je water en hydroxide-ionen. Zo klopt het aantal "
        "zuurstof- en waterstofatomen aan beide kanten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt een hoge normpotentiaal over een redoxkoppel?",
        opties=[
            "de geoxideerde vorm is een sterke oxidator",
            "de gereduceerde vorm is een sterke reductor",
            "de reactie verloopt heel snel in het labo",
            "het koppel reageert met elk ander koppel",
        ],
        antwoord=0,
        uitleg="Hoog in de tabel staat de sterkste oxidator. Onderaan staan de sterkste "
        "reductoren, zoals de alkalimetalen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een reactie tussen twee redoxkoppels gaat spontaan door als de sterkste oxidator met de sterkste reductor reageert.",
        antwoord=True,
        uitleg="Met de tabel erbij kan je dat voorspellen: de oxidator moet een hogere "
        "normpotentiaal hebben dan het koppel van de reductor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wordt koper niet aangetast door zoutzuur?",
        opties=[
            "het hydroxoniumion is een te zwakke oxidator voor koper",
            "koper is een te zwakke oxidator voor het chloride-ion",
            "zoutzuur is te verdund om koper aan te tasten",
            "koper vormt een laagje chloride dat de reactie stopt",
        ],
        antwoord=0,
        uitleg="Koper staat in de tabel boven waterstof. Salpeterzuur tast het wel aan, "
        "want het nitraation is een sterkere oxidator.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een halfreactie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze bevat de elektronen die afgestaan of opgenomen worden",
            "ze beschrijft enkel de oxidatie of enkel de reductie",
            "ze komt in de eindvergelijking met de elektronen erin",
            "ze bevat altijd evenveel deeltjes links als rechts",
        ],
        antwoord=[0, 1],
        uitleg="Bij het optellen van de twee halfreacties vallen de elektronen weg. "
        "Daarom staan ze niet meer in de eindvergelijking.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een reactie die spontaan doorgaat zonder spanningsbron?",
        antwoord=["spontaan", "spontane reactie", "een spontane reactie"],
        uitleg="Zo'n reactie levert energie. Een gedwongen reactie heeft een "
        "spanningsbron nodig, zoals bij elektrolyse.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je legt een stukje zink in een oplossing van kopersulfaat. Wat gebeurt er?",
        opties=[
            "het zink lost op en er slaat koper op het stukje neer",
            "het koper lost op en er slaat zink op het stukje neer",
            "er gebeurt niets, want beide zijn metalen",
            "er komt waterstofgas vrij uit de oplossing",
        ],
        antwoord=0,
        uitleg="Zink is de sterkere reductor en staat zijn elektronen af aan het "
        "koperion. Daarom ziet het stukje na een tijd roodbruin.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee koppels: Cu²⁺/Cu met +0,34 V en Zn²⁺/Zn met −0,76 V. Welke reactie gaat spontaan door?",
        opties=[
            "zink wordt geoxideerd en het koperion gereduceerd",
            "koper wordt geoxideerd en het zinkion gereduceerd",
            "beide metalen worden tegelijk geoxideerd",
            "er gaat geen enkele reactie spontaan door",
        ],
        antwoord=0,
        uitleg="Het koppel met de hoogste waarde levert de oxidator. Dus neemt Cu²⁺ de "
        "elektronen op en staat zink ze af.",
    ),
    dict(
        type="waarofniet",
        vraag="In de eindvergelijking van een redoxreactie mogen er nog losse elektronen staan.",
        antwoord=False,
        uitleg="Ze moeten precies tegen elkaar wegvallen. Blijft er toch een elektron "
        "staan, dan heb je de halfreacties niet goed vermenigvuldigd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een ionenreactievergelijking en een stoffenreactievergelijking?",
        opties=[
            "in de eerste laat je de ionen weg die niet meedoen",
            "in de eerste laat je de elektronen staan in de vergelijking",
            "in de tweede staan enkel de oxidatiegetallen vermeld",
            "in de tweede staat alleen de halfreactie van de oxidatie",
        ],
        antwoord=0,
        uitleg="Zo'n ion dat niets doet, heet een toeschouwerion. In de "
        "stoffenreactievergelijking schrijf je de volledige zouten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het opstellen in basisch midden zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "je gebruikt hydroxide-ionen om de lading te regelen",
            "je gebruikt water om de waterstofatomen te regelen",
            "je gebruikt hydroxoniumionen om de lading te regelen",
            "je laat de zuurstofatomen links en rechts verschillen",
        ],
        antwoord=[0, 1],
        uitleg="In zuur midden werk je met H₃O⁺, in basisch midden met OH⁻. Het aantal "
        "atomen van elk element moet altijd kloppen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een ion dat aan beide kanten van de vergelijking onveranderd staat?",
        antwoord=["toeschouwerion", "een toeschouwerion", "spectatorion"],
        uitleg="Zo'n ion mag je weglaten in de ionenreactievergelijking. Het doet niet mee "
        "aan de elektronenuitwisseling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je laat ijzer reageren met een oplossing van zoutzuur. Wat ontstaat er?",
        opties=[
            "ijzer(II)ionen en waterstofgas",
            "ijzer(III)ionen en zuurstofgas",
            "ijzeroxide en waterstofgas",
            "ijzerchloraat en chloorgas",
        ],
        antwoord=0,
        uitleg="IJzer staat onder waterstof in de tabel en is dus de sterkere reductor. "
        "Het hydroxoniumion wordt daarbij gereduceerd tot waterstofgas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom tast salpeterzuur koper wel aan en zoutzuur niet?",
        opties=[
            "het nitraation is een sterkere oxidator dan het hydroxoniumion",
            "salpeterzuur is een sterker zuur dan zoutzuur",
            "salpeterzuur is veel meer geconcentreerd te koop",
            "het chloride-ion beschermt het koper tegen de reactie",
        ],
        antwoord=0,
        uitleg="Bij die reactie ontstaat NO of NO₂. De sterkte van het zuur speelt hier "
        "dus geen rol, de oxidator wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel elektronen staat één aluminiumatoom af als het Al³⁺ wordt?",
        opties=[
            "drie",
            "een",
            "twee",
            "zes",
        ],
        antwoord=0,
        uitleg="Het oxidatiegetal gaat van nul naar +III. Elke eenheid stijging is één "
        "afgestaan elektron.",
    ),
    dict(
        type="waarofniet",
        vraag="De lading links en rechts van een ionenreactievergelijking moet gelijk zijn.",
        antwoord=True,
        uitleg="Niet nul, maar wel gelijk. Dat is naast het aantal atomen de tweede "
        "controle op je vergelijking.",
    ),
    dict(
        type="waarofniet",
        vraag="Een metaal boven waterstof in de tabel van normpotentialen lost op in een gewoon zuur.",
        antwoord=False,
        uitleg="Dan is het hydroxoniumion de te zwakke oxidator, zoals bij koper in "
        "zoutzuur. Een metaal ónder waterstof lost wel op, en dan komt er waterstofgas "
        "vrij.",
    ),
    dict(
        type="invultekst",
        vraag="Welke tabel gebruik je om te voorspellen of een redoxreactie spontaan doorgaat?",
        antwoord=["normpotentialen", "de normpotentialen", "potentiaaltabel"],
        uitleg="De oxidator moet in die tabel boven de reductor staan. Op het examen krijg "
        "je die tabel in de bijlage.",
    ),
]

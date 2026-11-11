# -*- coding: utf-8 -*-
"""Inkomensongelijkheid, armoede en herverdeling.

Fiche: personele en categoriale inkomensverdeling; Lorenzcurve en
Gini-coëfficiënt (voorstellen, interpreteren, vergelijken tussen landen en
in de tijd, berekening verklaren); oorzaken van ongelijkheid
(arbeidsmarktfactoren, persoonlijke eigenschappen, vermogen, sociaal
milieu); (gender)loonkloof; armoede tegenover ongelijkheid; indicatoren
AROP, LWI, SMSD, AROPE; maatregelen; fiscale en sociale herverdeling;
personenbelasting; de zeven takken van de sociale zekerheid,
verzekerings- en solidariteitsprincipe, vervangingsinkomen en aanvulling;
effect van herverdeling op Lorenzcurve en Gini-coëfficiënt.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat toont de personele inkomensverdeling?",
        opties=[
            "hoe het inkomen verdeeld is over personen of gezinnen",
            "hoe het inkomen verdeeld is over lonen, winsten, rente en huur",
            "hoe het inkomen verdeeld is over de gewesten",
            "hoe het inkomen verdeeld is over de sectoren",
        ],
        antwoord=0,
        uitleg="Bijvoorbeeld welk deel van het inkomen naar de rijkste 10 % gaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat toont de categoriale inkomensverdeling?",
        opties=[
            "hoe het inkomen verdeeld is over de productiefactoren",
            "hoe het inkomen verdeeld is over mannen en vrouwen in het hele land",
            "hoe het inkomen verdeeld is over jongeren en ouderen",
            "hoe het inkomen verdeeld is over de gemeenten",
        ],
        antwoord=0,
        uitleg="Lonen voor arbeid, rente voor kapitaal, huur voor grond, winst voor ondernemerschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat staat er op de assen van een Lorenzcurve?",
        opties=[
            "het cumulatieve % bevolking en inkomen",
            "de prijs en de hoeveelheid",
            "de tijd en het bbp per inwoner, per jaar",
            "het loon en de werkloosheid",
        ],
        antwoord=0,
        uitleg="Horizontaal de bevolking van arm naar rijk, verticaal het deel van het totale inkomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een perfect gelijke inkomensverdeling valt de Lorenzcurve samen met de diagonaal.",
        antwoord=True,
        uitleg="Dan heeft 20 % van de bevolking ook 20 % van het inkomen, en zo verder.",
    ),
    dict(
        type="meerkeuze",
        vraag="De Lorenzcurve van land A ligt verder van de diagonaal dan die van land B. Wat besluit je?",
        opties=[
            "in land A is het inkomen ongelijker verdeeld",
            "in land A is het inkomen gelijker verdeeld",
            "land A is rijker dan land B, gemeten in bbp per inwoner",
            "land A heeft minder inwoners",
        ],
        antwoord=0,
        uitleg="Hoe groter de buik tussen curve en diagonaal, hoe ongelijker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de Gini-coëfficiënt?",
        opties=[
            "de oppervlakte tussen diagonaal en Lorenzcurve, gedeeld door die onder de diagonaal",
            "het inkomen van de rijkste inwoner gedeeld door dat van de armste",
            "het gemiddelde inkomen gedeeld door het mediaaninkomen van het land",
            "het aantal armen gedeeld door het aantal inwoners van het land",
        ],
        antwoord=0,
        uitleg="Zo ligt de coëfficiënt tussen 0 en 1.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent een Gini-coëfficiënt van 0?",
        opties=["perfecte gelijkheid", "maximale ongelijkheid", "geen inkomen", "gemiddelde ongelijkheid"],
        antwoord=0,
        uitleg="Iedereen heeft hetzelfde inkomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een Gini-coëfficiënt dicht bij 1 wijst op een kleine ongelijkheid.",
        antwoord=False,
        uitleg="Dicht bij 1 is de ongelijkheid groot. Bij 1 zou één persoon al het inkomen hebben.",
    ),
    dict(
        type="meerkeuze",
        vraag="Land X heeft een Gini van 0,26, land Y een Gini van 0,45. Wat klopt?",
        opties=[
            "in land Y is het inkomen ongelijker verdeeld",
            "in land X is het inkomen ongelijker verdeeld",
            "land Y is armer dan land X",
            "beide landen zijn even ongelijk",
        ],
        antwoord=0,
        uitleg="Hoe hoger de Gini, hoe groter de ongelijkheid. Over rijkdom zegt de Gini niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zijn oorzaken van inkomensongelijkheid? Duid alle juiste antwoorden aan.",
        opties=["verschillen in opleiding en beroep", "verschillen in vermogen", "het aantal letters in je naam", "de kleur van je fiets"],
        antwoord=[0, 1],
        uitleg="Ook persoonlijke eigenschappen en het sociaal milieu spelen mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de genderloonkloof?",
        opties=[
            "het verschil in gemiddeld loon tussen mannen en vrouwen",
            "het verschil in loon tussen jongeren en ouderen in hetzelfde beroep",
            "het verschil tussen bruto- en nettoloon",
            "het verschil in loon tussen gewesten",
        ],
        antwoord=0,
        uitleg="Ze komt onder meer door deeltijds werk, beroepskeuze en ongelijke kansen.",
    ),
    dict(
        type="waarofniet",
        vraag="Armoede en inkomensongelijkheid betekenen hetzelfde.",
        antwoord=False,
        uitleg="Ongelijkheid gaat over de verdeling; armoede over mensen die te weinig hebben om waardig te leven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer loopt iemand een risico op monetaire armoede (AROP)?",
        opties=[
            "als zijn inkomen onder 60 % van de mediaan ligt",
            "als hij geen eigen woning heeft",
            "als hij minder verdient dan het gemiddelde van alle inwoners",
            "als hij geen auto heeft",
        ],
        antwoord=0,
        uitleg="Het mediaaninkomen is het middelste inkomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat meet de indicator LWI?",
        opties=[
            "gezinnen met een lage werkintensiteit",
            "gezinnen met een laag inkomen",
            "gezinnen met een hoge schuld bij de bank",
            "gezinnen zonder internet",
        ],
        antwoord=0,
        uitleg="De volwassenen in het gezin werken samen veel minder dan ze zouden kunnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat meet SMSD?",
        opties=[
            "ernstige materiële en sociale deprivatie",
            "het gemiddelde loon van werknemers",
            "de groei van het bbp per inwoner, per jaar",
            "het aantal werklozen per gewest",
        ],
        antwoord=0,
        uitleg="Bijvoorbeeld de woning niet kunnen verwarmen of geen onverwachte kosten kunnen betalen.",
    ),
    dict(
        type="waarofniet",
        vraag="AROPE telt wie te maken heeft met minstens één van de drie: monetaire armoede, ernstige deprivatie of lage werkintensiteit.",
        antwoord=True,
        uitleg="Het is de breedste Europese armoede-indicator.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met de Lorenzcurve als de overheid inkomen herverdeelt van rijk naar arm?",
        opties=[
            "ze schuift dichter naar de diagonaal",
            "ze schuift verder van de diagonaal",
            "ze verandert niet",
            "ze wordt een rechte horizontale lijn",
        ],
        antwoord=0,
        uitleg="De ongelijkheid daalt, dus de Gini daalt ook.",
    ),
    dict(
        type="waarofniet",
        vraag="Een land kan een lage Gini-coëfficiënt hebben en toch arm zijn.",
        antwoord=True,
        uitleg="De Gini meet enkel de verdeling, niet het niveau van het inkomen.",
    ),
    dict(
        type="invultekst",
        vraag="De oppervlakte tussen de diagonaal en de Lorenzcurve is 0,15. De hele oppervlakte onder de diagonaal is 0,5. Hoeveel is de Gini-coëfficiënt?",
        antwoord=["0,3", "0.3", "0,30"],
        uitleg="0,15 / 0,5 = 0,3.",
    ),
    dict(
        type="waarofniet",
        vraag="Als de armste 20 % van de bevolking 20 % van het inkomen heeft, is er sprake van grote ongelijkheid.",
        antwoord=False,
        uitleg="Dat punt ligt op de diagonaal: het past bij gelijkheid.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarom verkleint een progressieve personenbelasting de ongelijkheid?",
        opties=[
            "hogere inkomens betalen een groter percentage",
            "iedereen betaalt precies hetzelfde bedrag, hoe groot zijn inkomen ook is",
            "lage inkomens betalen meer dan hoge",
            "enkel bedrijven betalen belasting",
        ],
        antwoord=0,
        uitleg="Door de belastingschijven stijgt het tarief met het inkomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe wordt de personenbelasting in België berekend?",
        opties=[
            "elke hogere inkomensschijf krijgt een hoger tarief",
            "iedereen betaalt 25 % op het hele inkomen, zonder schijven",
            "enkel het inkomen boven 100 000 euro wordt belast",
            "het bedrag hangt enkel af van de leeftijd",
        ],
        antwoord=0,
        uitleg="Er is ook een belastingvrije som die niet belast wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zijn takken van de Belgische sociale zekerheid? Duid alle juiste antwoorden aan.",
        opties=["pensioenen", "werkloosheid", "onderwijs", "openbaar vervoer"],
        antwoord=[0, 1],
        uitleg="De zeven takken: pensioenen, werkloosheid, ziekte- en invaliditeitsverzekering, arbeidsongevallen, beroepsziekten, gezinsbijslagen en jaarlijkse vakantie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel takken telt de Belgische sociale zekerheid?",
        antwoord=["7", "zeven"],
        uitleg="Pensioenen, werkloosheid, ziekte en invaliditeit, arbeidsongevallen, beroepsziekten, gezinsbijslagen en jaarlijkse vakantie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verzekeringsprincipe in de sociale zekerheid?",
        opties=[
            "wie bijdraagt, is verzekerd tegen risico's",
            "iedereen krijgt hetzelfde bedrag, ook zonder bijdragen",
            "enkel rijken krijgen uitkeringen",
            "je kiest zelf of je bijdraagt",
        ],
        antwoord=0,
        uitleg="De uitkering hangt vaak af van het vroegere loon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het solidariteitsprincipe in de sociale zekerheid?",
        opties=[
            "de sterkste schouders dragen de zwaarste lasten",
            "iedereen betaalt precies wat hij later terugkrijgt",
            "elk gewest betaalt enkel voor zichzelf",
            "enkel werkenden hebben recht op hulp",
        ],
        antwoord=0,
        uitleg="Zo zijn er minimumuitkeringen en maximumbedragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voorbeeld is een vervangingsinkomen?",
        opties=["een werkloosheidsuitkering", "een groeipakket voor kinderen", "een loonsverhoging", "een terugbetaling van de huisarts"],
        antwoord=0,
        uitleg="Het vervangt het loon als je niet kan werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voorbeeld is een aanvulling op het inkomen?",
        opties=["de gezinsbijslag", "een pensioen", "een invaliditeitsuitkering", "een werkloosheidsuitkering"],
        antwoord=0,
        uitleg="De gezinsbijslag komt bovenop het loon en helpt de kosten van kinderen dragen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een pensioen is een vervangingsinkomen.",
        antwoord=True,
        uitleg="Het vervangt het loon na de loopbaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het effect van belastingen en sociale zekerheid op de Gini-coëfficiënt?",
        opties=["de Gini daalt", "de Gini stijgt", "de Gini blijft gelijk", "de Gini wordt negatief"],
        antwoord=0,
        uitleg="Na herverdeling is het inkomen gelijker verdeeld dan ervoor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatregelen bestrijden armoede? Duid alle juiste antwoorden aan.",
        opties=[
            "een leefloon voor wie geen inkomen heeft",
            "sociale woningen",
            "een hogere btw op voeding",
            "lagere kinderbijslagen",
        ],
        antwoord=[0, 1],
        uitleg="Een hogere btw op voeding treft net de laagste inkomens hard.",
    ),
    dict(
        type="waarofniet",
        vraag="België heeft, in vergelijking met veel andere landen, een relatief lage Gini-coëfficiënt.",
        antwoord=True,
        uitleg="Door de belastingen en de sociale zekerheid ligt de Belgische Gini rond 0,25.",
    ),
    dict(
        type="meerkeuze",
        vraag="De Gini-coëfficiënt van een land stijgt jaar na jaar. Wat betekent dat?",
        opties=[
            "de inkomensongelijkheid neemt toe",
            "de inkomensongelijkheid neemt af",
            "het land wordt rijker per inwoner",
            "het land wordt armer",
        ],
        antwoord=0,
        uitleg="Over het niveau van het inkomen zegt de Gini niets.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vlaktaks, waarbij iedereen hetzelfde percentage betaalt, verkleint de ongelijkheid sterker dan een progressieve belasting.",
        antwoord=False,
        uitleg="Bij een vlaktaks blijft de verhouding tussen de inkomens gelijk. Progressieve belasting verkleint de verschillen meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe beïnvloedt het sociaal milieu waarin je opgroeit je latere inkomen?",
        opties=[
            "via kansen op onderwijs, netwerk en steun thuis",
            "helemaal niet: iedereen start met dezelfde kansen",
            "enkel via de erfenis van een huis",
            "enkel via de keuze van de woonplaats",
        ],
        antwoord=0,
        uitleg="Kinderen uit kwetsbare gezinnen hebben gemiddeld minder kansen.",
    ),
    dict(
        type="waarofniet",
        vraag="Vermogen speelt geen rol in de inkomensongelijkheid, want vermogen is geen inkomen.",
        antwoord=False,
        uitleg="Vermogen levert inkomen op uit rente, dividenden of huur. Zo kan het de ongelijkheid vergroten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruikt men het mediaaninkomen en niet het gemiddelde inkomen voor de armoedegrens?",
        opties=[
            "de mediaan reageert minder op enkele hoge inkomens",
            "het gemiddelde is altijd lager dan de mediaan",
            "het mediaaninkomen is gemakkelijker uit te spreken",
            "het gemiddelde inkomen wordt nergens berekend",
        ],
        antwoord=0,
        uitleg="Enkele superrijken trekken het gemiddelde omhoog, de mediaan niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Het groeipakket voor kinderen is een vervangingsinkomen.",
        antwoord=False,
        uitleg="Het is een aanvulling op het inkomen, geen vervanging van het loon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze maatregelen is een fiscale maatregel om inkomen te herverdelen?",
        opties=["een progressieve personenbelasting", "een werkloosheidsuitkering voor wie zijn job verliest", "een pensioen", "een ziekte-uitkering"],
        antwoord=0,
        uitleg="De andere drie zijn sociale maatregelen via de sociale zekerheid.",
    ),
    dict(
        type="waarofniet",
        vraag="Een AROP-percentage van 13 % betekent dat 13 % van de bevolking een inkomen heeft onder de armoedegrens.",
        antwoord=True,
        uitleg="De grens ligt op 60 % van het mediaan besteedbaar inkomen.",
    ),
]

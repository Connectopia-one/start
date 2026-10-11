# -*- coding: utf-8 -*-
"""De vragen voor "Misleiding met cijfers en grafieken".

Nieuw geschreven voor dubbele finaliteit. De doorstroomversie van dit thema
gaat voor de helft over verbanden in een puntenwolk en over de
correlatiecoëfficiënt; die staan niet op de DF-fiche. Wat er wél op staat, is
een hele lijst manieren waarop cijfers je om de tuin kunnen leiden: assen
ongepast schalen, assen foutief ijken, onderdelen niet correct benoemen of
weergeven, vervormen en uitvergroten, informatie weglaten, en percentages
foutief interpreteren. De fiche zet er ook het verschil naast tussen de
mediaan en het rekenkundig gemiddelde.

Deel 1 gaat over het beeld: de assen, de schaal, de vorm. Deel 2 gaat over de
getallen zelf: percentages, procentpunt, en welk middelpunt je kiest.

De wiskundige notatie staat in de vragen zelf: een percentage als
\\(4\\,\\%\\), een groot getal met een smalle ruimte als \\(10\\,000\\) en een
komma als \\(0{,}5\\).
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag=r"Een staafdiagram begint niet bij \(0\) maar bij \(90\). Wat doet dat met het beeld?",
        opties=[
            "kleine verschillen lijken veel groter dan ze zijn",
            "grote verschillen lijken kleiner dan ze zijn",
            "de staven worden allemaal even hoog",
            "er verandert niets aan het beeld",
        ],
        antwoord=0,
        uitleg="Het onderste stuk van elke staaf is weggeknipt, dus wat overblijft verschilt "
               "verhoudingsgewijs veel sterker.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een staafdiagram hoort in principe bij \(0\) te beginnen.",
        antwoord=True,
        uitleg="De hoogte van een staaf stelt de grootte voor. Knip je het onderste stuk weg, dan "
               "klopt die verhouding niet meer.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Wat is er mis met een as die van \(0\) naar \(10\) naar \(100\) naar \(1000\) "
              r"loopt met gelijke tussenafstanden?",
        opties=[
            "gelijke afstanden staan niet voor gelijke verschillen",
            r"een as mag geen \(0\) bevatten",
            "er staan te weinig getallen op de as",
            "de getallen op de as zijn geen veelvouden van elkaar",
        ],
        antwoord=0,
        uitleg="Dat heet foutief ijken. Wie de as niet leest, ziet een rechte lijn waar een sprong zit.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een grafiek slaat op de tijdas de jaren \(2019\) en \(2020\) over. Waarom is dat "
              r"misleidend?",
        opties=[
            "de lijn loopt dan vlakker of steiler dan het verloop echt was",
            "de grafiek wordt dan te breed om af te drukken",
            "de jaartallen staan dan niet meer alfabetisch",
            "er komen dan te veel punten op de lijn",
        ],
        antwoord=0,
        uitleg="Ontbrekende stukken op een as hoor je te tonen, bijvoorbeeld met een breukteken, of "
               "je laat ze gewoon staan.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grafiek zonder titel en zonder namen bij de assen is even bruikbaar als een grafiek met die informatie.",
        antwoord=False,
        uitleg="Zonder namen weet je niet wat er gemeten is of in welke eenheid, en dan kan elk "
               "getal alles betekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een verkoopcijfer verdubbelt en wordt getoond met een plaatje dat twee keer zo breed "
              "én twee keer zo hoog is. Wat klopt daar niet aan?",
        opties=[
            "het lijkt vier keer zo groot in plaats van twee keer",
            "het plaatje lijkt half zo groot",
            "het plaatje staat aan de verkeerde kant van de as",
            "het plaatje mist een legende",
        ],
        antwoord=0,
        uitleg=r"Verdubbel je breedte én hoogte, dan wordt de oppervlakte \(2 \cdot 2 = 4\) keer "
               r"zo groot. Dat is uitvergroten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een cirkeldiagram in 3D vaak misleidend?",
        opties=[
            "de sectoren vooraan lijken groter dan die achteraan",
            "een cirkeldiagram mag geen kleuren hebben",
            r"de sectoren tellen dan niet meer op tot \(100\,\%\)",
            "3D-diagrammen mogen maar drie sectoren bevatten",
        ],
        antwoord=0,
        uitleg="Door het schuine perspectief krijgen de stukken vooraan meer oppervlakte op het "
               "blad, terwijl hun aandeel even groot is.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle sectoren van een cirkeldiagram horen delen van hetzelfde geheel te zijn.",
        antwoord=True,
        uitleg="Zet iemand er een stuk bij dat van een andere groep of een ander jaar komt, dan "
               "stelt de cirkel niets meer voor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een grafiek toont enkel de vier beste maanden van het jaar. Hoe heet die vorm van misleiding?",
        opties=["data weglaten", "de as foutief ijken", "uitvergroten",
                "onderdelen verkeerd benoemen"],
        antwoord=0,
        uitleg="Wat je niet toont, kan de lezer ook niet wegen. Vraag altijd welke periode of welke "
               "groep ontbreekt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een staafdiagram heeft staven die niet even breed zijn. Waarom is dat een probleem?",
        opties=[
            "de bredere staven trekken meer aandacht dan hun waarde verdient",
            "de staven passen dan niet meer op het blad",
            r"de as kan dan niet bij \(0\) beginnen",
            "de staven mogen dan geen kleur meer hebben",
        ],
        antwoord=0,
        uitleg="In een staafdiagram hoort enkel de hoogte iets te betekenen. Verschil in breedte "
               "voegt een tweede signaal toe dat er niet is.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het weergeven van een verdubbeling als een plaatje dat vier keer zo veel plaats inneemt?",
        antwoord=["uitvergroten", "uitvergroting"],
        uitleg="De oppervlakte groeit veel sneller dan het getal dat ze voorstelt.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee grafieken naast elkaar met een verschillende schaal kan je zomaar met elkaar vergelijken.",
        antwoord=False,
        uitleg="Kijk eerst naar de assen. Dezelfde helling betekent dan iets heel anders in de ene "
               "dan in de andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de eerste vraag die je stelt bij een grafiek die je op sociale media ziet?",
        opties=[
            "wat staat er op de assen en waar begint de schaal",
            "welke kleur hebben de staven",
            "hoeveel mensen hebben de grafiek al gedeeld en geliket",
            "wie heeft de grafiek het eerst geplaatst",
        ],
        antwoord=0,
        uitleg="De meeste misleiding zit in de assen. Daar kijk je dus als eerste.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een lijndiagram wordt smal getekend in plaats van breed. Wat gebeurt er met de lijn?",
        opties=[
            "ze lijkt steiler en de verandering lijkt heftiger",
            "ze lijkt vlakker en de verandering lijkt kleiner",
            "ze verandert van richting",
            "er verandert niets aan de indruk",
        ],
        antwoord=0,
        uitleg="Dezelfde cijfers in een smalle grafiek geven een dramatischer beeld. Dat heet "
               "ongepast schalen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grafiek hoort te vermelden waar de cijfers vandaan komen.",
        antwoord=True,
        uitleg="Zonder bron kan je niet nagaan of de cijfers kloppen en hoe ze verzameld zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een diagram staat bij de ene staaf 'omzet' en bij de andere 'winst'. Wat is daar mis mee?",
        opties=[
            "het zijn twee verschillende grootheden die je niet naast elkaar zet",
            "de staven staan in de verkeerde volgorde",
            "de woorden zijn te lang voor een diagram",
            "winst mag nooit in een staafdiagram",
        ],
        antwoord=0,
        uitleg="Onderdelen verkeerd benoemen of door elkaar zetten maakt een vergelijking zinloos. "
               "Omzet is altijd groter dan winst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de bedoeling van een legende bij een grafiek?",
        opties=[
            "uitleggen waar elke kleur of elk symbool voor staat",
            "de grafiek een titel geven",
            "de bron van de cijfers vermelden",
            "de schaal van de verticale as vastleggen voor de lezer",
        ],
        antwoord=0,
        uitleg="Ontbreekt de legende bij meerdere reeksen, dan weet je niet welke lijn bij welke "
               "groep hoort.",
    ),
    dict(
        type="invultekst",
        vraag="Waar hoort de verticale as van een staafdiagram in principe te beginnen?",
        antwoord=["bij nul", "nul", "op nul"],
        uitleg="Anders klopt de verhouding tussen de hoogtes van de staven niet meer.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een grafiek toont de stijging van een aantal zonder te zeggen hoe groot de groep is. Waarom is dat lastig?",
        opties=[
            r"\(2\) naar \(4\) zegt iets anders bij \(10\) dan bij \(10\,000\) mensen",
            "een aantal mag nooit in een grafiek",
            "een stijging is altijd positief nieuws voor de lezer",
            "je kan een aantal niet afronden",
        ],
        antwoord=0,
        uitleg="Zonder het totaal weet je niet of het om een uitzondering of om een echte trend gaat.",
    ),
    dict(
        type="waarofniet",
        vraag=r"Een grafiek waarvan de as niet bij \(0\) begint, is altijd bewust bedrog.",
        antwoord=False,
        uitleg="Soms is inzoomen zinvol, bijvoorbeeld bij lichaamstemperatuur. Het moet dan wel "
               "duidelijk aangegeven staan.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag=r"Een percentage stijgt van \(4\,\%\) naar \(6\,\%\). Met hoeveel procentpunt is dat "
              r"gestegen?",
        opties=[r"\(2\) procentpunt", r"\(50\) procentpunt", r"\(2\,\%\)", r"\(6\) procentpunt"],
        antwoord=0,
        uitleg=r"Procentpunt is het gewone verschil tussen de twee percentages: \(6 - 4 = 2\).",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Diezelfde stijging van \(4\,\%\) naar \(6\,\%\): met hoeveel procent is dat "
              r"gestegen?",
        opties=[r"\(50\,\%\)", r"\(2\,\%\)", r"\(6\,\%\)", r"\(150\,\%\)"],
        antwoord=0,
        uitleg=r"Ten opzichte van de \(4\) waar je van vertrok, is \(2\) erbij de helft meer. Dat "
               r"is een relatieve stijging van \(50\,\%\).",
    ),
    dict(
        type="waarofniet",
        vraag="Procentpunt en procent betekenen hetzelfde.",
        antwoord=False,
        uitleg="Procentpunt is een absoluut verschil tussen twee percentages, procent is een "
               "relatieve verandering. Wie ze verwisselt, maakt een cijfer veel groter of kleiner "
               "dan het is.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een jas van \(100\) euro krijgt eerst \(20\,\%\) korting en daarna nog eens "
              r"\(10\,\%\). Hoeveel korting is dat samen?",
        opties=[r"\(28\,\%\)", r"\(30\,\%\)", r"\(25\,\%\)", r"\(32\,\%\)"],
        antwoord=0,
        uitleg=r"Na de eerste korting betaal je \(80\) euro, en \(10\,\%\) daarvan is \(8\) euro. "
               r"Je betaalt \(72\) euro, dus \(28\) euro korting.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee kortingen na elkaar mag je gewoon bij elkaar optellen.",
        antwoord=False,
        uitleg="De tweede korting wordt op een al verlaagd bedrag gerekend, dus samen is het altijd "
               "iets minder dan de som.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een prijs stijgt met \(10\,\%\) en daalt daarna met \(10\,\%\). Wat is het "
              r"resultaat?",
        opties=[
            "de prijs ligt iets lager dan in het begin",
            "de prijs is precies dezelfde als in het begin",
            "de prijs ligt iets hoger dan in het begin",
            r"de prijs is met \(20\,\%\) gedaald",
        ],
        antwoord=0,
        uitleg=r"\(100\) wordt \(110\), en \(10\,\%\) van \(110\) is \(11\). Je eindigt op "
               r"\(99\), dus \(1\,\%\) onder de startprijs.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"In een bedrijf verdienen vier mensen \(2000\) euro en één persoon \(12\,000\) "
              r"euro. Wat is het rekenkundig gemiddelde?",
        opties=[r"\(4000\) euro", r"\(2000\) euro", r"\(7000\) euro", r"\(2800\) euro"],
        antwoord=0,
        uitleg=r"Samen is dat \(20\,000\) euro voor vijf mensen, dus \(4000\) euro per persoon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de mediaan van diezelfde vijf lonen?",
        opties=[r"\(2000\) euro", r"\(4000\) euro", r"\(12\,000\) euro", r"\(7000\) euro"],
        antwoord=0,
        uitleg=r"Zet ze op volgorde en neem het middelste: \(2000\), \(2000\), \(2000\), "
               r"\(2000\), \(12\,000\). Het derde getal is \(2000\) euro.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Dat bedrijf adverteert met 'bij ons verdien je gemiddeld \(4000\) euro'. Waarom is "
              r"dat misleidend?",
        opties=[
            "omdat vier van de vijf werknemers veel minder verdienen",
            "omdat een gemiddelde nooit in een advertentie mag",
            r"omdat \(4000\) euro een te rond getal is om te kloppen",
            "omdat een bedrijf enkel brutolonen mag vermelden",
        ],
        antwoord=0,
        uitleg="Het getal klopt, maar het beschrijft niemand. Eén hoog loon trekt het gemiddelde "
               "ver boven wat de meesten krijgen.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie lonen hoog wil laten lijken, kiest beter het rekenkundig gemiddelde dan de mediaan.",
        antwoord=True,
        uitleg="Allebei de getallen kloppen. Wie kiest welk getal hij toont, stuurt daarmee het verhaal.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het middelste getal van een reeks die je op volgorde hebt gezet?",
        antwoord=["de mediaan", "mediaan"],
        uitleg="Bij een even aantal getallen neem je het gemiddelde van de twee middelste.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een reclame zegt: 'negen op de tien tandartsen raden dit aan'. Welke vraag stel je?",
        opties=[
            "hoeveel tandartsen zijn er gevraagd en wie heeft de vraag gesteld",
            "hoe duur het product is",
            "of tandartsen wel getallen mogen gebruiken",
            r"of \(9\) een even getal is",
        ],
        antwoord=0,
        uitleg=r"Negen op tien kan \(10\) mensen betekenen, of \(1000\). Wie de vraag stelde, "
               r"bepaalt mee wie er geantwoord heeft.",
    ),
    dict(
        type="waarofniet",
        vraag="Een percentage zonder het aantal waarop het slaat, zegt weinig.",
        antwoord=True,
        uitleg=r"\(100\,\%\) van twee mensen klinkt indrukwekkend maar stelt weinig voor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een krant schrijft: 'het risico verdubbelt'. Wat wil je daar zeker bij weten?",
        opties=[
            "hoe groot het risico eerst was",
            "wanneer de krant is verschenen",
            "hoeveel bladzijden het artikel telt",
            "of de krant een website heeft",
        ],
        antwoord=0,
        uitleg=r"Van \(1\) op een miljoen naar \(2\) op een miljoen is ook een verdubbeling, en "
               r"dat is iets heel anders dan van \(10\,\%\) naar \(20\,\%\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Een enquête over sportgewoontes wordt enkel afgenomen aan de ingang van een fitnesszaal. Wat is het probleem?",
        opties=[
            "de bevraagde groep is niet representatief",
            "er zijn te veel vragen gesteld",
            "de vragen waren te moeilijk",
            "de resultaten zijn niet in procent uitgedrukt",
        ],
        antwoord=0,
        uitleg="Wie je bevraagt, bepaalt je antwoord. Deze groep sport per definitie meer dan gemiddeld.",
    ),
    dict(
        type="invultekst",
        vraag=r"Hoe noem je het verschil tussen twee percentages, bijvoorbeeld van \(4\,\%\) naar "
              r"\(6\,\%\)?",
        antwoord=["procentpunt", "in procentpunt", "2 procentpunt"],
        uitleg="Procentpunt is een absoluut verschil. Wil je het relatief uitdrukken, dan reken je "
               "ten opzichte van het startgetal.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een winkel adverteert met 'tot \(70\,\%\) korting'. Wat weet je zeker?",
        opties=[
            r"geen enkel artikel heeft meer dan \(70\,\%\) korting",
            r"elk artikel heeft \(70\,\%\) korting",
            r"de meeste artikelen hebben \(70\,\%\) korting",
            r"de korting bedraagt gemiddeld \(70\,\%\)",
        ],
        antwoord=0,
        uitleg="Het woordje 'tot' zet enkel een bovengrens. Misschien haalt één artikel die korting "
               "en de rest veel minder.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Een bedrijf meldt: 'onze winst groeide met \(200\,\%\)'. Wat betekent dat?",
        opties=[
            "de winst is verdrievoudigd",
            "de winst is verdubbeld",
            "de winst is twee keer zo klein geworden",
            r"de winst bedraagt nu \(200\,\%\) van de omzet",
        ],
        antwoord=0,
        uitleg="Er kwam twee keer het oorspronkelijke bedrag bij, dus samen met het origineel is "
               "dat drie keer zo veel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een cijfer dat helemaal juist is, kan nooit een verkeerde indruk geven.",
        antwoord=False,
        uitleg="Bijna alle misleiding met cijfers gebeurt met kloppende getallen. De keuze van de "
               "grafiek, de periode of het middelpunt doet het werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig om bij een cijfer altijd te vragen wie het naar buiten brengt?",
        opties=[
            "omdat wie belang heeft bij een uitkomst, de voorstelling kan kleuren",
            "omdat cijfers van een bedrijf nooit kloppen",
            "omdat alleen de overheid cijfers mag publiceren",
            "omdat een cijfer zonder naam ongeldig is",
        ],
        antwoord=0,
        uitleg="De cijfers zelf kunnen kloppen terwijl de keuze van de grafiek, de periode of de "
               "groep het verhaal stuurt.",
    ),
]

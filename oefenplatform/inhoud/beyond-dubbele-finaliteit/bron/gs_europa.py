# -*- coding: utf-8 -*-
"""De Europese eenmaking.

Uit de leerinhoud over de samenlevingen in de hedendaagse tijd: waarom de
Europese samenwerking na 1945 op gang kwam, welke verdragen haar vorm gaven, hoe
de Unie werkt en welke vragen erover gesteld worden.

Deel 1 gaat over het ontstaan en over de verdragen. Deel 2 gaat over de
instellingen, de euro, de uitbreiding en de kritiek.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke redenen lagen na 1945 aan de Europese samenwerking ten grondslag?",
        opties=[
            "een nieuwe oorlog tussen Frankrijk en Duitsland voorkomen",
            "de economie van het verwoeste werelddeel heropbouwen",
            "de kolonies van Europa in Afrika behouden",
            "een eigen Europees leger tegen de Verenigde Naties",
        ],
        antwoord=[0, 1],
        uitleg="Daar komt het zoeken naar gewicht tussen de Verenigde Staten en de Sovjet-Unie bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat stelde de Schuman-verklaring van 1950 voor?",
        opties=[
            "de kolen en het staal van Europa samen beheren",
            "één Europese munt voor alle landen invoeren",
            "een Europees leger onder één bevel oprichten",
            "de grenzen tussen alle landen meteen afschaffen",
        ],
        antwoord=0,
        uitleg="Juist die twee grondstoffen van de oorlogsindustrie. Wie ze samen beheert, kan elkaar niet verrassen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gemeenschap kwam uit de Schuman-verklaring?",
        opties=[
            "de Europese Gemeenschap voor Kolen en Staal",
            "de Europese Economische Gemeenschap",
            "de Europese Unie met haar euro",
            "de Noord-Atlantische Verdragsorganisatie",
        ],
        antwoord=0,
        uitleg="Zes landen deden mee. Daarmee was de eerste steen van de hele Europese bouw gelegd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zes landen richtten de eerste Europese gemeenschap op?",
        opties=[
            "België, Nederland en Luxemburg",
            "Frankrijk, Duitsland en Italië",
            "Groot-Brittannië, Ierland en Denemarken",
            "Spanje, Portugal en Griekenland",
        ],
        antwoord=[0, 1],
        uitleg="De Britten bleven er eerst buiten. Zij traden pas in 1973 toe, en in 2020 weer uit.",
    ),
    dict(
        type="invultekst",
        vraag="Welke twee grondstoffen gingen de zes landen in 1951 samen beheren?",
        antwoord=["kolen en staal", "steenkool en staal", "staal en kolen"],
        uitleg="Het waren de grondstoffen van de wapenindustrie. Daarom was juist dat zo'n sterke keuze.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat werd in 1957 in het Verdrag van Rome afgesproken?",
        opties=[
            "een gemeenschappelijke markt tussen de leden",
            "een gemeenschappelijke munt voor alle lidstaten",
            "een gemeenschappelijk leger voor heel Europa",
            "een gemeenschappelijke grondwet voor alle leden",
        ],
        antwoord=0,
        uitleg="Zo ontstond de Europese Economische Gemeenschap, met vrij verkeer van goederen, mensen en kapitaal als doel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een douane-unie?",
        opties=[
            "de leden heffen geen invoerrechten op elkaars goederen",
            "de leden heffen wel invoerrechten op elkaars goederen",
            "de leden gebruiken allemaal dezelfde munt",
            "de leden hebben samen één leger en één politie",
        ],
        antwoord=0,
        uitleg="Naar buiten geldt wel één gemeenschappelijk tarief. Dat maakt het verschil met een vrijhandelszone.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het gemeenschappelijk landbouwbeleid?",
        opties=[
            "Europa steunt de landbouw en regelt de prijzen",
            "Europa verbiedt de landbouw in de lidstaten volledig",
            "Europa laat elk land zijn eigen landbouwbeleid voeren",
            "Europa voert alle landbouwproducten uit Amerika in",
        ],
        antwoord=0,
        uitleg="Het moest de voedselvoorziening veilig stellen. Lang nam het het grootste deel van de begroting in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat werd in 1992 in het Verdrag van Maastricht beslist?",
        opties=[
            "de gemeenschap werd de Europese Unie",
            "de gemeenschap werd ontbonden en elk land ging zijn eigen weg",
            "de gemeenschap werd een militair bondgenootschap zoals de NAVO",
            "de gemeenschap nam alle landen van Afrika als lid op",
        ],
        antwoord=0,
        uitleg="Daar werd ook de gemeenschappelijke munt vastgelegd, samen met het Europese burgerschap.",
    ),
    dict(
        type="invultekst",
        vraag="In welke stad werd in 1992 het verdrag gesloten dat de Europese Unie oprichtte?",
        antwoord=["Maastricht", "in Maastricht"],
        uitleg="Het ligt in Nederlands Limburg, dicht bij de Belgische grens.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat regelt het verdrag van Schengen?",
        opties=[
            "het afschaffen van de grenscontroles",
            "het invoeren van één munt in alle deelnemende landen",
            "het verdelen van de landbouwsteun onder de lidstaten",
            "het oprichten van een gemeenschappelijk Europees leger",
        ],
        antwoord=0,
        uitleg="Niet elk EU-land doet eraan mee, en sommige landen buiten de Unie wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer kwamen de eurobiljetten en de euromunten in omloop?",
        opties=[
            "in 2002",
            "in 1992",
            "in 1979",
            "in 2010",
        ],
        antwoord=0,
        uitleg="Voor de banken en de boekhouding bestond de euro al vanaf 1999.",
    ),
    dict(
        type="waarofniet",
        vraag="De Europese samenwerking begon met kolen en staal, niet met een munt.",
        antwoord=True,
        uitleg="De munt kwam veertig jaar later. Men begon met iets klein en concreet dat de landen bond.",
    ),
    dict(
        type="waarofniet",
        vraag="Groot-Brittannië hoorde bij de zes stichters van de eerste Europese gemeenschap.",
        antwoord=False,
        uitleg="Het trad pas in 1973 toe en verliet de Unie in 2020.",
    ),
    dict(
        type="waarofniet",
        vraag="De Europese Unie heeft één munt die in al haar lidstaten geldt.",
        antwoord=False,
        uitleg="Niet elk land van de Unie heeft de euro. Denemarken, Polen en Zweden hebben hun eigen munt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een douane-unie betekent dat de leden tegenover de buitenwereld één tarief gebruiken.",
        antwoord=True,
        uitleg="Onderling verdwijnen de rechten, naar buiten komt er één gemeenschappelijk tarief in de plaats.",
    ),
    dict(
        type="waarofniet",
        vraag="Het verdrag van Schengen schafte de controles aan de binnengrenzen af.",
        antwoord=True,
        uitleg="Daardoor rijd je zonder stoppen van Hasselt naar Maastricht of naar Aken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de Europese eenmaking kloppen?",
        opties=[
            "ze begon met zes landen en groeide stap voor stap",
            "ze begon met economische samenwerking, niet met politiek",
            "ze begon met een gemeenschappelijke munt voor alle leden",
            "ze begon als militair bondgenootschap tegen de Sovjet-Unie",
        ],
        antwoord=[0, 1],
        uitleg="Dat militaire bondgenootschap bestond apart: dat was de NAVO, met ook landen van buiten Europa.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de Europese Unie en de Raad van Europa?",
        opties=[
            "de Raad van Europa staat los van de Unie",
            "de Raad van Europa is het parlement van de Europese Unie",
            "de Raad van Europa is de regering van de Europese Unie",
            "de Raad van Europa en de Europese Unie zijn hetzelfde",
        ],
        antwoord=0,
        uitleg="Zij waakt over de mensenrechten, heeft veel meer leden en een eigen hof in Straatsburg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband zie je tussen de twee wereldoorlogen en de Europese eenmaking?",
        opties=[
            "de eenmaking moest een nieuwe oorlog onmogelijk maken",
            "de eenmaking was al voor de Eerste Wereldoorlog voltooid",
            "de eenmaking had met de oorlogen niets te maken",
            "de eenmaking werd door de Volkenbond in 1920 opgezet",
        ],
        antwoord=0,
        uitleg="Twee oorlogen in dertig jaar tussen dezelfde buren: dat was het argument dat de zes over de brug haalde.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke instelling van de Europese Unie wordt door de burgers verkozen?",
        opties=[
            "het Europees Parlement",
            "de Europese Commissie",
            "het Hof van Justitie",
            "de Europese Centrale Bank",
        ],
        antwoord=0,
        uitleg="Sinds 1979 rechtstreeks, elke vijf jaar. In België valt die verkiezing samen met de andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de Europese Commissie?",
        opties=[
            "zij stelt wetgeving voor en voert het beleid uit",
            "zij verkiest de leden van het Europees Parlement",
            "zij spreekt recht over de verdragen van de Unie",
            "zij bepaalt de rentevoet van de euro",
        ],
        antwoord=0,
        uitleg="Elk land levert er een commissaris. De rentevoet is het werk van de Europese Centrale Bank.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie beslist samen met het Europees Parlement over de Europese wetgeving?",
        opties=[
            "de Raad van de ministers van de lidstaten",
            "het Hof van Justitie in Luxemburg",
            "de Europese Centrale Bank in Frankfurt",
            "de Raad van Europa in Straatsburg",
        ],
        antwoord=0,
        uitleg="Parlement en Raad samen: de ene verkozen door de burgers, de andere door de regeringen bezet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is subsidiariteit in de Europese Unie?",
        opties=[
            "wat lager geregeld kan worden, blijft daar",
            "elke beslissing wordt op het Europese niveau genomen",
            "elk land krijgt subsidies naar het aantal inwoners",
            "elke lidstaat mag elke Europese wet weigeren",
        ],
        antwoord=0,
        uitleg="Het is een begrenzing van de bevoegdheid. In de praktijk wordt er geregeld over geredetwist.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitbreidingen kende de Europese Unie?",
        opties=[
            "Groot-Brittannië en Ierland in 1973",
            "tien landen, waarvan de meeste uit Midden-Europa, in 2004",
            "Rusland en Oekraïne in de jaren negentig",
            "Marokko en Turkije in de jaren zestig",
        ],
        antwoord=[0, 1],
        uitleg="In 1973 trad ook Denemarken toe. De uitbreiding van 2004 was het gevolg van de val van het ijzeren gordijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk verband zie je tussen het einde van de Koude Oorlog en de Europese Unie?",
        opties=[
            "landen uit het vroegere Oostblok konden lid worden",
            "de Unie werd door de val van de Muur ontbonden",
            "de Unie verloor daardoor de helft van haar leden",
            "de Unie werd daardoor een militair bondgenootschap",
        ],
        antwoord=0,
        uitleg="Polen, Hongarije, Tsjechië en de Baltische staten traden in 2004 toe, vijftien jaar na 1989.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de Brexit?",
        opties=[
            "het Verenigd Koninkrijk verliet de Europese Unie",
            "het Verenigd Koninkrijk trad tot de eurozone toe",
            "het Verenigd Koninkrijk werd lid van de Unie",
            "het Verenigd Koninkrijk sloot zich bij Schengen aan",
        ],
        antwoord=0,
        uitleg="Na een volksstemming in 2016 en jaren onderhandelen gebeurde dat begin 2020.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het vertrek van het Verenigd Koninkrijk uit de Europese Unie?",
        antwoord=["de brexit", "brexit"],
        uitleg="Het was de eerste keer dat een lidstaat de Unie verliet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kritiek wordt op de Europese Unie geformuleerd?",
        opties=[
            "de beslissingen staan te ver van de burger af",
            "de lidstaten geven te veel bevoegdheid uit handen",
            "de Unie heeft geen enkel verkozen orgaan",
            "de Unie verbiedt haar leden onderling handel te drijven",
        ],
        antwoord=[0, 1],
        uitleg="Het Parlement is wel rechtstreeks verkozen, en de hele Unie draait juist rond onderlinge handel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voordeel wordt aan de gemeenschappelijke markt toegeschreven?",
        opties=[
            "bedrijven en mensen kunnen vrij over de grenzen werken",
            "elk land kan zijn eigen invoerrechten weer invoeren",
            "elk land kan zijn munt naar believen in waarde laten dalen",
            "elk land hoeft geen afspraken met de andere te maken",
        ],
        antwoord=0,
        uitleg="Diploma's, goederen en diensten worden over de grenzen erkend. Dat was voor 1958 niet zo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat deed de Europese Unie tijdens de eurocrisis na 2008?",
        opties=[
            "zij hielp landen in nood met leningen",
            "zij schafte de euro af en gaf elk land zijn munt terug",
            "zij sloot alle banken van de eurozone voor een jaar",
            "zij liet elke lidstaat haar eigen rentevoet bepalen",
        ],
        antwoord=0,
        uitleg="De begrotingsregels werden daarbij aangescherpt. Steun kwam met harde voorwaarden, en daarover is jaren betwisting geweest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rol heeft België in de Europese Unie?",
        opties=[
            "het is stichtend lid, met instellingen in Brussel",
            "het is geen lid en werkt enkel met de Benelux samen",
            "het trad pas in 2004 samen met Polen toe",
            "het weigerde de euro en hield zijn frank",
        ],
        antwoord=0,
        uitleg="De Commissie en de Raad zitten in Brussel; het Parlement vergadert in Brussel en in Straatsburg.",
    ),
    dict(
        type="invultekst",
        vraag="In welke Belgische stad zitten de Europese Commissie en de Raad?",
        antwoord=["Brussel", "in Brussel"],
        uitleg="Daardoor wonen en werken er duizenden mensen uit alle lidstaten.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Europees Parlement wordt rechtstreeks door de burgers verkozen.",
        antwoord=True,
        uitleg="Sinds 1979. Voordien stuurden de nationale parlementen hun eigen leden erheen.",
    ),
    dict(
        type="waarofniet",
        vraag="De Europese Commissie wordt door de burgers rechtstreeks verkozen.",
        antwoord=False,
        uitleg="Haar leden worden voorgedragen door de regeringen en door het Parlement goedgekeurd.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle landen van de Europese Unie nemen deel aan Schengen.",
        antwoord=False,
        uitleg="Niet allemaal, en Noorwegen en Zwitserland doen mee zonder lid van de Unie te zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Het Verenigd Koninkrijk is lid van de Europese Unie geweest en er weer uit gestapt.",
        antwoord=True,
        uitleg="Van 1973 tot 2020. Geen enkele andere lidstaat is dat voorbeeld gevolgd.",
    ),
    dict(
        type="waarofniet",
        vraag="De Europese Unie is een staat met één regering en één leger.",
        antwoord=False,
        uitleg="Zij is een verbond van staten die bevoegdheden samen uitoefenen. Defensie blijft grotendeels nationaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een opiniestuk dat Europa te ver van de mensen staat en dat de lidstaten te weinig te zeggen hebben. Wat is dat?",
        opties=[
            "een standpunt in het debat over de Europese Unie",
            "een officieel besluit van de Europese Commissie",
            "een uitspraak van het Hof van Justitie",
            "een artikel uit het Verdrag van Maastricht",
        ],
        antwoord=0,
        uitleg="Zo'n tekst lees je als een mening met argumenten, en niet als een beschrijving van de feiten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vergelijkt de Europese Unie met de Verenigde Naties. Welk verschil valt op?",
        opties=[
            "de Unie maakt wetten die in haar lidstaten gelden",
            "de Verenigde Naties maken wetten voor al hun leden",
            "beide organisaties hebben precies dezelfde leden",
            "beide organisaties hebben een eigen gemeenschappelijke munt",
        ],
        antwoord=0,
        uitleg="De Verenigde Naties werken met verdragen en resoluties; de Unie heeft een eigen rechtsorde.",
    ),
]

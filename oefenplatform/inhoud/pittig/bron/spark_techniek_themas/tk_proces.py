# -*- coding: utf-8 -*-
"""Pittige vragen bij "Het technisch proces" (✨ Spark, techniek).

Dezelfde leerstof als deel 1 en 2 (de vijf fasen, criteria, terugkeren naar fase 2 of 3,
probleemoplossend ontwerpen en STEM), maar toegepast op nieuwe schoolprojecten en met
oorzaak-gevolgredeneringen en veelgemaakte fouten.
"""

VRAGEN = [
    dict(
        type="meerkeuze",
        vraag=r"Bij de test van een vogelhuisje regent het binnen. Het ontwerp was goed, maar bij het in elkaar zetten werd de lijmnaad van het dak slordig gezet. Naar welke fase keer je terug?",
        opties=[
            r"Naar fase \(3\), want de uitvoering liep fout",
            r"Naar fase \(1\), want de behoefte moet opnieuw onderzocht worden",
            r"Naar fase \(2\), want elke fout begint altijd bij het ontwerp",
            r"Naar fase \(4\), want je moet het gewoon nog een keer testen",
        ],
        antwoord=0,
        uitleg=r"De fout zit in het maken, niet in de tekening, dus keer je terug naar fase \(3\). Terug naar fase \(1\) is niet nodig: de behoefte en de criteria staan al vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een pennenbak uit dun karton zakt in elkaar als je er een schaar en een lat in zet. Hij is precies gemaakt volgens de tekening en met het gekozen materiaal. Waar zat de fout?",
        opties=[
            r"In het ontwerp, dus je keert terug naar fase \(2\)",
            r"In het maken, dus je keert terug naar fase \(3\)",
            r"In de behoefte, dus je keert terug naar fase \(1\)",
            "Nergens: je past het criterium aan het resultaat aan",
        ],
        antwoord=0,
        uitleg=r"Het materiaal kies je in de ontwerpfase. Werd alles netjes volgens de tekening gemaakt, dan lag het niet aan het maken maar aan de keuze in fase \(2\). Een criterium aanpassen aan het resultaat doe je nooit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ontwerpt een fietslicht. Welke zinnen zijn echte criteria voor dat fietslicht (meerdere antwoorden mogelijk)?",
        opties=[
            "Het fietslicht moet tegen regen kunnen",
            "Het fietslicht mag niet meer dan een kilo wegen",
            "We zagen de stukken van de behuizing met een figuurzaag",
            "We beginnen er volgende maandag in de klas aan",
            "We maken eerst een schets op ruitjespapier",
        ],
        antwoord=[0, 1],
        uitleg="Een criterium is een eis waaraan het systeem zelf moet voldoen. Met welk gereedschap je werkt, wanneer je begint of hoe je schetst, zegt iets over je werkwijze en niet over wat het fietslicht moet kunnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een klas maakt een fietsenrek voor de school. A: een ontwerptekening maken. B: klasgenoten vragen hoeveel fietsen erin moeten. C: het rek uitproberen met echte fietsen. D: de buizen op maat zagen. Welke volgorde klopt?",
        opties=["B - A - D - C", "A - B - D - C", "B - D - A - C", "B - A - C - D"],
        antwoord=0,
        uitleg=r"Eerst onderzoek je de behoefte (B, fase \(1\)), dan ontwerp je (A, fase \(2\)), dan maak je (D, fase \(3\)) en pas dan test je (C, fase \(4\)). Wie eerst tekent en pas daarna vraagt wat nodig is, tekent misschien iets wat niemand vroeg.",
    ),
    dict(
        type="meerkeuze",
        vraag=r"Het criterium was dat het fietsenrek \(10\) fietsen houdt, maar er passen er maar \(6\) in. Een leerling zegt: 'We veranderen het criterium in \(6\), dan is het in orde.' Wat is daar fout aan?",
        opties=[
            "Criteria liggen vast voor je maakt; je stuurt het rek bij",
            "Niets, criteria mag je achteraf altijd vrij aanpassen",
            r"Je moet het criterium dan op \(8\) zetten, als compromis tussen beide",
            r"Je moet helemaal opnieuw beginnen bij het behoefteonderzoek in fase \(1\)",
        ],
        antwoord=0,
        uitleg=r"Criteria leg je vast in fase \(1\), vóór het maken, en ze komen uit wat de gebruikers nodig hebben. Voldoet het rek niet, dan pas je het ontwerp of de uitvoering aan, niet de eis.",
    ),
    dict(
        type="waarofniet",
        vraag="Een systeem dat bij de eerste test niet aan alle criteria voldoet, bewijst dat het technisch proces slecht gevolgd werd.",
        antwoord=False,
        uitleg="Evalueren en bijsturen is zelf een fase van het proces. Dat je na een test iets moet aanpassen, is dus net een teken dat je het proces goed volgt.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie zonder criteria aan een werkstuk begint, kan bij de evaluatie niet eerlijk beoordelen of het gelukt is.",
        antwoord=True,
        uitleg=r"In fase \(5\) leg je het resultaat naast de criteria van fase \(1\). Zijn er geen criteria, dan heb je niets om het resultaat mee te vergelijken.",
    ),
    dict(
        type="invultekst",
        vraag="Een groep merkt bij de evaluatie dat hun ontwerp niet klopt. Ze keren terug naar de juiste fase en doorlopen vanaf daar opnieuw alle fasen tot en met de evaluatie. Hoeveel fasen doorlopen ze opnieuw, de fase waarnaar ze terugkeren meegeteld? Antwoord met een getal.",
        antwoord="4",
        reken="5 - 2 + 1",
        uitleg=r"Klopt het ontwerp niet, dan keer je terug naar fase \(2\). Daarna volgen fase \(2\), \(3\), \(4\) en \(5\): vier fasen. Wie vijf antwoordt, ging ten onrechte terug naar fase \(1\).",
    ),
    dict(
        type="meerkeuze",
        vraag="Je maakt een plantenbak voor je oma. Je meet hoe breed haar vensterbank is en vraagt hoeveel plantjes erin moeten. In welke fase zit je?",
        opties=[
            "In de fase waarin je het probleem en de behoefte onderzoekt",
            "In de fase waarin je het systeem ontwerpt en tekent",
            "In de fase waarin je het systeem in gebruik neemt en test",
            "In de fase waarin je evalueert en bijstuurt waar nodig",
        ],
        antwoord=0,
        uitleg="Je zoekt uit wat oma echt nodig heeft en welke eisen er gelden: dat is het behoefteonderzoek van de eerste fase. Meten lijkt op ontwerpen, maar je tekent hier nog niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je twijfelt of je de zijkanten van een plantenbak zult schroeven of lijmen, en je beslist het op papier. In welke fase van het technisch proces zit je?",
        opties=[
            "In de ontwerpfase",
            "In de maakfase met het gereedschap",
            "In de fase van het behoefteonderzoek",
            "In de fase van het testen in gebruik",
        ],
        antwoord=0,
        uitleg="Welke verbindingstechniek je gebruikt, bepaal je in de ontwerpfase. In de maakfase voer je die keuze pas uit: dan schroef of lijm je echt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een groep maakt een nachtlampje dat vanzelf aangaat als het donker wordt. Welke beslissingen horen in de ontwerpfase (meerdere antwoorden mogelijk)?",
        opties=[
            "Welke sensor het donker zal meten",
            "Uit welk materiaal de kap gemaakt wordt",
            "Of de kap geschroefd of gelijmd wordt",
            "Of het lampje echt aangaat in een donkere kamer",
            "Hoe je tijdens het zagen veilig met de figuurzaag werkt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Sensoren, materiaal en verbindingen kies je in de ontwerpfase. Nagaan of het lampje echt aangaat is testen in fase \\(4\\), en veilig werken met gereedschap licht je toe in de maakfase.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het technisch proces kloppen (meerdere antwoorden mogelijk)?",
        opties=[
            "Het begint bij een behoefte of een probleem",
            "Je kan het ook voor een transportsysteem gebruiken",
            "De criteria leg je vast voor je iets maakt",
            "Het stappenplan stel je op voor je begint te maken",
            r"Voldoet het systeem niet, dan begin je terug bij fase \(1\)",
        ],
        antwoord=[0, 1, 2, 3],
        uitleg=r"Beginnen bij een behoefte, het proces gebruiken voor elk systeem, en criteria en stappenplan vastleggen vóór het maken: dat klopt allemaal. Terugkeren naar fase \(1\) is de bekende fout: je keert terug naar fase \(2\) of \(3\), want het probleem en de criteria staan al vast.",
    ),
    dict(
        type="meerkeuze",
        vraag="Tijdens de coronacrisis werkten de STEM-disciplines samen. Welke koppeling tussen een discipline en een taak klopt NIET?",
        opties=[
            "Wiskunde: het vaccin koel houden tijdens het vervoer",
            "Wetenschappen: het vaccin zelf ontwikkelen",
            "Wiskunde: de verspreiding van het virus in kaart brengen",
            "Technologie: het vaccin koel houden en vervoeren",
        ],
        antwoord=0,
        uitleg="Het vaccin koel houden en vervoeren vroeg technologische kennis. Wiskunde was nodig om de verspreiding van het virus te volgen; die twee taken haal je makkelijk door elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Leerlingen klagen: 'Het fietsenrek van de school is slecht.' Wat doe je als allereerste stap van probleemoplossend ontwerpen?",
        opties=[
            "Duidelijk omschrijven wat er precies mis is",
            "Meteen een groter en steviger rek gaan tekenen",
            "Het probleem opsplitsen in kleinere deelproblemen",
            "Het materiaal voor een nieuw rek al bestellen",
        ],
        antwoord=0,
        uitleg="'Slecht' is geen duidelijk probleem: is het te klein, te zwak of passen de banden niet? Pas als je dat weet, kan je criteria opstellen en opsplitsen. Meteen tekenen lost misschien het verkeerde probleem op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Brede fietsbanden passen niet in het fietsenrek omdat de gleuven te smal zijn. Het rek is verder stevig en groot genoeg. Welke aanpak past hier het best?",
        opties=[
            "De gleuven van het bestaande rek verbreden",
            "Een volledig nieuw rek ontwerpen, van nul af",
            "Het criterium aanpassen zodat smalle gleuven volstaan",
            "Niets doen, want het rek is stevig genoeg voor gewone fietsen",
        ],
        antwoord=0,
        uitleg="Soms volstaat het een bestaand systeem aan te passen in plaats van een nieuw te ontwerpen. Hier is alleen de breedte van de gleuven het probleem, dus is een helemaal nieuw rek overbodig werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een groep bouwt een robotje dat rijdt, piept en licht geeft. Elk lid werkt apart aan één onderdeel, maar op het einde passen de onderdelen niet op elkaar. Welke stap van probleemoplossend ontwerpen liep mis?",
        opties=[
            "De oplossingen samenvoegen tot één totaaloplossing",
            "Het probleem opsplitsen in kleinere deelproblemen",
            "De criteria opstellen voordat er iets gemaakt wordt",
            "Het probleem helemaal in het begin duidelijk bepalen",
        ],
        antwoord=0,
        uitleg="Het opsplitsen is net gelukt: elk deel werkt apart. Wat ontbreekt, is het integreren: de deeloplossingen moeten samen het hele probleem oplossen en dus op elkaar passen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een behoefteonderzoek voor een speelgoedauto voor je kleine broer doe je het best door zelf te bedenken wat jij het leukst zou vinden.",
        antwoord=False,
        uitleg="Een behoefteonderzoek gaat na wat de gebruiker echt nodig heeft, niet wat jij leuk vindt. Hier is je broer de gebruiker, dus moet je bij hem nagaan wat hij nodig heeft.",
    ),
    dict(
        type="waarofniet",
        vraag=r"In fase \(4\) kijk je of het systeem werkt in gebruik; pas in fase \(5\) leg je het resultaat naast de criteria.",
        antwoord=True,
        uitleg=r"Testen en evalueren zijn twee aparte fasen. Eerst probeer je het systeem uit, daarna beoordeel je of het voldoet aan de eisen uit fase \(1\) en stuur je bij.",
    ),
    dict(
        type="invultekst",
        vraag="Een leerling schilderde haar werkstuk eerst en boorde er pas daarna de gaten in, waardoor de verf beschadigd raakte. Welk plan, dat je vóór het maken opstelt, had dat moeten voorkomen? Antwoord met één woord.",
        antwoord="stappenplan",
        uitleg="Een stappenplan maak je vóór je begint, zodat je weet in welke volgorde je moet werken. Dan had boren vóór schilderen gestaan.",
    ),
    dict(
        type="invultekst",
        vraag="Een pennenzak blijkt bij de test lek, terwijl er als eis stond: 'Hij moet tegen water kunnen.' In welke fase werd die eis vastgelegd? Antwoord met een getal.",
        antwoord="1",
        uitleg=r"'Moet tegen water kunnen' is een criterium, en criteria leg je vast in fase \(1\). Bij de evaluatie in fase \(5\) controleer je ze alleen.",
    ),
]

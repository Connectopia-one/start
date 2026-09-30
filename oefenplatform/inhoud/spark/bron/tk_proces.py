# -*- coding: utf-8 -*-
"""De vragen voor "Het technisch proces" (✨ Spark, techniek).

Uit de vakfiche 1ste graad A-stroom, onderdeel "Technisch proces" (leerdoel
6.38, het leerdoel waar het hele examen op gebouwd is) en "Ontwerp van een
oplossing" met de interactie tussen de STEM-disciplines en de maatschappij.

Deel 1 gaat over de vijf fasen: de behoefte onderzoeken, ontwerpen, maken, in
gebruik nemen of testen, en evalueren en bijsturen.
Deel 2 gaat over probleemoplossend ontwerpen en over de wisselwerking tussen
wetenschappen, technologie, wiskunde en de maatschappij, met het voorbeeld van
de coronacrisis dat de fiche zelf geeft.

Wie niet voldoet aan de criteria keert terug naar fase 2 of 3, niet naar fase
1: dat staat zo in de fiche en wordt vaak fout onthouden.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel fasen heeft het technisch proces?",
        opties=["Vijf", "Drie", "Vier", "Zeven"],
        antwoord=0,
        uitleg="Behoefte onderzoeken, ontwerpen, maken, in gebruik nemen of testen, en evalueren en bijsturen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de eerste fase van het technisch proces?",
        opties=[
            "Je onderzoekt het probleem en de behoefte",
            "Je tekent hoe het systeem eruit zal zien",
            "Je maakt het technisch systeem in elkaar",
            "Je test of het systeem in gebruik werkt",
        ],
        antwoord=0,
        uitleg="Je kijkt wat de gebruiker nodig heeft en legt de eisen vast. Zonder die eerste stap maak je misschien iets wat niemand vraagt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de tweede fase van het technisch proces?",
        opties=[
            "Je ontwerpt en tekent het systeem",
            "Je onderzoekt eerst nog de behoefte",
            "Je maakt het technisch systeem zelf",
            "Je stuurt het afgewerkte systeem bij",
        ],
        antwoord=0,
        uitleg="In de ontwerpfase bedenk je oplossingen, maak je schetsen en kies je het materiaal, de verbindingen en het gereedschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de derde fase van het technisch proces?",
        opties=[
            "Je maakt het technisch systeem",
            "Je bedenkt het eerste idee ervoor",
            "Je neemt het systeem in gebruik",
            "Je evalueert het systeem achteraf",
        ],
        antwoord=0,
        uitleg="In de maakfase volg je je stappenplan en je ontwerp, en je werkt veilig met het gereedschap en de machines.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de vierde fase van het technisch proces?",
        opties=[
            "Je neemt het systeem in gebruik en test het",
            "Je tekent een eerste schets van het idee",
            "Je kiest het materiaal en het gereedschap",
            "Je schrijft het behoefteonderzoek uit",
        ],
        antwoord=0,
        uitleg="Nu pas blijkt of het echt werkt. Testen hoort bij het proces, het is geen extra stap die je kunt overslaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de vijfde fase van het technisch proces?",
        opties=[
            "Je evalueert en stuurt bij waar nodig",
            "Je maakt het werkstuk helemaal af",
            "Je koopt het materiaal in de winkel",
            "Je tekent de allereerste conceptschets",
        ],
        antwoord=0,
        uitleg="Je legt het resultaat naast de criteria van fase 1. Klopt er iets niet, dan pas je aan.",
    ),
    dict(
        type="invultekst",
        vraag="In de laatste fase ga je na of het systeem voldoet aan de opgestelde ___.",
        antwoord="criteria",
        uitleg="Criteria zijn de eisen die je in fase 1 hebt vastgelegd. Zonder criteria kan je achteraf niet beoordelen of het gelukt is.",
    ),
    dict(
        type="waarofniet",
        vraag="Een criterium is een eis waaraan je technisch systeem moet voldoen.",
        antwoord=True,
        uitleg="Bijvoorbeeld: het moet tegen water kunnen, het mag niet meer dan een kilo wegen, het moet door een kind te bedienen zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Voldoet je systeem in fase 5 niet, dan begin je altijd helemaal opnieuw bij fase 1.",
        antwoord=False,
        uitleg="De fiche zegt dat je teruggaat naar fase 2 of 3: je past het ontwerp aan of je maakt iets anders. De behoefte is intussen niet veranderd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de ontwerpfase?",
        opties=[
            "Een schets of een model maken",
            "Het materiaal kiezen",
            "Het gereedschap kiezen",
            "Het afgewerkte werkstuk verkopen",
        ],
        antwoord=[0, 1, 2],
        uitleg="In de ontwerpfase leg je alles vast wat je bij het maken nodig hebt. Verkopen hoort niet bij het technisch proces.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een behoefteonderzoek?",
        opties=[
            "Nagaan wat de gebruiker echt nodig heeft",
            "Nagaan hoeveel het materiaal in totaal kost",
            "Nagaan hoe lang het maken ongeveer duurt",
            "Nagaan wie het werkstuk in elkaar zet",
        ],
        antwoord=0,
        uitleg="Je vraagt het aan wie het gaat gebruiken, of je kijkt hoe het nu gaat. Uit dat onderzoek komen de criteria.",
    ),
    dict(
        type="waarofniet",
        vraag="Het stappenplan om het systeem te maken stel je pas op nadat het af is.",
        antwoord=False,
        uitleg="Het stappenplan hoort bij de maakfase zelf, vóór je begint. Het zegt juist in welke volgorde je moet werken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom maak je een stappenplan voor je begint te maken?",
        opties=[
            "Zo weet je in welke volgorde je moet werken",
            "Zo hoef je geen materiaal meer te kiezen",
            "Zo wordt het werkstuk mooier van kleur",
            "Zo hoef je onderweg niets meer te meten",
        ],
        antwoord=0,
        uitleg="Sommige stappen kunnen alleen in een bepaalde volgorde. Wie eerst schildert en dan pas boort, mag opnieuw beginnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bepaal je in de ontwerpfase over het technisch systeem?",
        opties=[
            "Welke verbindingstechnieken je gebruikt",
            "Welke sensoren of actuatoren nodig zijn",
            "Welke overbrengingen erin moeten komen",
            "Wie het werkstuk later gaat aankopen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alles wat je in de vorige hoofdstukken geleerd hebt, komt hier samen. Dat is precies wat de fiche met een technisch proces bedoelt.",
    ),
    dict(
        type="waarofniet",
        vraag="Het technisch proces begint bij een behoefte of een probleem.",
        antwoord=True,
        uitleg="Niet bij een idee of bij een materiaal, maar bij iets wat iemand nodig heeft. Daaruit volgt de rest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een technisch systeem voldoet niet aan de criteria. Wat doe je volgens de fiche?",
        opties=[
            "Je keert terug naar fase 2 of fase 3",
            "Je gooit het systeem helemaal weg",
            "Je past de criteria aan het resultaat aan",
            "Je slaat de laatste fase gewoon over",
        ],
        antwoord=0,
        uitleg="Terug naar het ontwerp of naar het maken. De criteria aanpassen zodat het toch lukt, is precies wat je niet doet.",
    ),
    dict(
        type="waarofniet",
        vraag="Het technisch proces kan alleen gebruikt worden voor een constructiesysteem.",
        antwoord=False,
        uitleg="Het werkt voor elk systeem uit de fiche, en ook voor een combinatie ervan: energie, informatieverwerkend, constructie, transport en biotechnisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke fase licht je toe hoe je veilig met het gereedschap werkt?",
        opties=[
            "In de maakfase",
            "In de ontwerpfase",
            "In de behoeftefase",
            "In de evaluatiefase",
        ],
        antwoord=0,
        uitleg="Bij fase 3 staat in de fiche dat je toelicht hoe je op een veilige en duurzame manier met gereedschap, machines en hulpmiddelen werkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de eerste fase van het technisch proces?",
        opties=[
            "Het probleem onderzoeken",
            "Een behoefteonderzoek doen",
            "De criteria vastleggen",
            "Het werkstuk netjes afwerken",
        ],
        antwoord=[0, 1, 2],
        uitleg="Fase 1 heet in de fiche letterlijk probleemstelling of behoefte onderzoeken. Afwerken hoort bij het maken.",
    ),
    dict(
        type="waarofniet",
        vraag="In de vierde fase neem je het systeem in gebruik of test je het.",
        antwoord=True,
        uitleg="Pas bij het gebruiken merk je of het echt doet wat je wilde. Daarna volgt de evaluatie.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent de E in STEM?",
        opties=["Engineering", "Energie", "Elektriciteit", "Ervaring"],
        antwoord=0,
        uitleg="Engineering is het Engelse woord voor techniek en ingenieurswerk. De S is science, de T technology en de M mathematics.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stappen horen bij probleemoplossend ontwerpen?",
        opties=[
            "Het probleem duidelijk bepalen",
            "Criteria opstellen voor de oplossing",
            "Het probleem opsplitsen in deelproblemen",
            "De prijs van het materiaal doen dalen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt ook: mogelijke oplossingen bedenken, ze in de totaaloplossing integreren, en evalueren en bijsturen.",
    ),
    dict(
        type="waarofniet",
        vraag="Soms volstaat het een bestaand systeem aan te passen in plaats van een nieuw te ontwerpen.",
        antwoord=True,
        uitleg="Dat staat zo in de fiche. Hangt af van het probleem: soms is een kleine aanpassing genoeg, soms moet alles opnieuw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het opsplitsen van een probleem in deelproblemen?",
        opties=[
            "Je pakt elk stuk apart aan",
            "Je laat het moeilijkste stuk gewoon vallen",
            "Je vraagt aan iemand anders om het op te lossen",
            "Je wacht af tot het probleem vanzelf verdwijnt",
        ],
        antwoord=0,
        uitleg="Een groot probleem is vaak onoverzichtelijk. In stukken geknipt kan je elk stuk apart oplossen en de oplossingen daarna samenvoegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruik je bij een ontwerp kennis uit wetenschappen én wiskunde?",
        opties=[
            "Omdat een goed ontwerp meer dan één invalshoek vraagt",
            "Omdat dat op het examen nu eenmaal verplicht is",
            "Omdat techniek op zichzelf helemaal niet bestaat",
            "Omdat wiskunde altijd het juiste antwoord geeft",
        ],
        antwoord=0,
        uitleg="Wil je een brug ontwerpen, dan heb je natuurkunde nodig voor de krachten en wiskunde voor de berekeningen. Techniek alleen volstaat niet.",
    ),
    dict(
        type="invultekst",
        vraag="De vier letters van STEM staan voor science, technology, engineering en ___.",
        antwoord=["mathematics", "wiskunde"],
        uitleg="Wetenschappen, technologie, techniek en wiskunde. De vier samen vormen de blik waarmee je een technisch probleem bekijkt.",
    ),
    dict(
        type="waarofniet",
        vraag="Criteria stel je op nadat het systeem al gemaakt is.",
        antwoord=False,
        uitleg="Criteria horen bij het begin. Achteraf eisen bedenken die toevallig passen bij wat je gemaakt hebt, zegt niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kennis was er tijdens de coronacrisis nodig om een vaccin te ontwikkelen?",
        opties=[
            "Wetenschappelijke kennis",
            "Uitsluitend wiskundige kennis",
            "Uitsluitend technologische kennis",
            "Geen enkele bijzondere kennis",
        ],
        antwoord=0,
        uitleg="Dat voorbeeld staat in de fiche. Voor het ontwikkelen van het vaccin zelf was wetenschappelijke kennis nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor was er tijdens de coronacrisis wiskundige kennis nodig?",
        opties=[
            "Om de verspreiding van het virus in kaart te brengen",
            "Om het vaccin tijdens het vervoer koel te houden",
            "Om het vaccin zelf in een labo uit te vinden",
            "Om de mondmaskers in een fabriek te naaien",
        ],
        antwoord=0,
        uitleg="Met wiskunde werden de cijfers gevolgd en werd voorspeld hoe snel het virus zich verder zou verspreiden.",
    ),
    dict(
        type="waarofniet",
        vraag="Technologische kennis was nodig om het vaccin koel te houden en te vervoeren.",
        antwoord=True,
        uitleg="Het vaccin moest bij een heel lage temperatuur bewaard blijven. Daar waren speciale koelinstallaties en transportdozen voor nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke disciplines zitten er in STEM?",
        opties=[
            "Wetenschappen",
            "Technologie",
            "Wiskunde",
            "Aardrijkskunde",
            "Geschiedenis",
        ],
        antwoord=[0, 1, 2],
        uitleg="Samen met engineering, de techniek zelf. Aardrijkskunde en geschiedenis zijn belangrijke vakken, maar ze horen niet bij STEM.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom ontstaan er steeds nieuwe technieken en materialen?",
        opties=[
            "Omdat de maatschappij voor nieuwe uitdagingen staat",
            "Omdat oude materialen na een tijd vanzelf verdwijnen",
            "Omdat fabrikanten zich anders zouden vervelen",
            "Omdat de wet dat elk jaar opnieuw verplicht maakt",
        ],
        antwoord=0,
        uitleg="Klimaat, gezondheid, energie, een ouder wordende bevolking: elke uitdaging vraagt om onderzoek en nieuwe oplossingen.",
    ),
    dict(
        type="waarofniet",
        vraag="Je evalueert je oplossing en stuurt ze bij als dat nodig is.",
        antwoord=True,
        uitleg="Evalueren en bijsturen staat als laatste stap zowel bij het technisch proces als bij het probleemoplossend ontwerpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als je oplossing niet aan de criteria voldoet?",
        opties=[
            "Je stuurt ze bij",
            "Je laat de criteria dan maar vallen",
            "Je stopt meteen met het hele project",
            "Je maakt er een heel ander product van",
        ],
        antwoord=0,
        uitleg="Bijsturen betekent aanpassen tot het wel voldoet. Dat hoort gewoon bij ontwerpen: bijna niets lukt in één keer.",
    ),
    dict(
        type="waarofniet",
        vraag="Een ontwerp is pas goed als je het probleem vanuit één vakgebied bekijkt.",
        antwoord=False,
        uitleg="Net omgekeerd: de fiche zegt dat je een goede oplossing enkel krijgt door het probleem vanuit de verschillende STEM-disciplines te bekijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de eerste stap bij het ontwerpen van een oplossing?",
        opties=[
            "Het probleem duidelijk omschrijven",
            "Het materiaal alvast gaan aankopen",
            "Het gereedschap al klaarleggen",
            "De prijs van het geheel berekenen",
        ],
        antwoord=0,
        uitleg="Wie niet precies weet wat het probleem is, lost meestal iets anders op. Daarom staat het definiëren van het probleem vooraan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom voeg je de oplossingen van de deelproblemen achteraf weer samen?",
        opties=[
            "Omdat ze samen het hele probleem moeten oplossen",
            "Omdat dat sneller werkt dan alles apart te houden",
            "Omdat er anders veel te veel schetsen ontstaan",
            "Omdat de leerkracht daar nu eenmaal om vraagt",
        ],
        antwoord=0,
        uitleg="Losse oplossingen die niet op elkaar passen, geven geen werkend systeem. Daarom heet die stap integreren in de totaaloplossing.",
    ),
    dict(
        type="waarofniet",
        vraag="STEM gaat alleen over techniek.",
        antwoord=False,
        uitleg="STEM is techniek samen met wetenschappen en wiskunde. Juist het samenspel van die drie maakt STEM tot wat het is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatschappelijke uitdagingen vragen om nieuwe techniek?",
        opties=[
            "De klimaatverandering",
            "Een tekort aan grondstoffen",
            "De zorg voor een ouder wordende bevolking",
            "De kleur van de auto's van volgend jaar",
        ],
        antwoord=[0, 1, 2],
        uitleg="Zulke uitdagingen zetten onderzoek in gang. Daar komen dan weer nieuwe materialen, methodes en systemen uit voort.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het als een ontwerp bijgestuurd wordt?",
        opties=[
            "Er wordt iets aan veranderd zodat het beter voldoet",
            "Het wordt in zijn geheel weggegooid en vergeten",
            "Het wordt aan iemand anders doorgegeven om af te maken",
            "Het wordt op een andere schaal opnieuw getekend",
        ],
        antwoord=0,
        uitleg="Bijsturen is een gewone stap in het proces, geen mislukking. Je verandert wat niet werkt en test opnieuw.",
    ),
]

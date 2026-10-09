# -*- coding: utf-8 -*-
"""Presenteren met PowerPoint.

Het derde van vier thema's uit "ik ben digitaal vaardig", het zwaarste blok
van de fiche met 17,5 procent.

Dezelfde zin uit de fiche bepaalt hoe dit thema geschreven is als bij Word en
Excel: "Je werkt niet met de programma's zelf, maar krijgt schermafdrukken
uit Windows 10 en MS Office 365." Je moet dus weten wat een knop doet en hoe
iets heet, niet zelf een presentatie maken.

Wat de fiche voor PowerPoint opsomt:
    een presentatie ontwerpen of aanpassen
    basisbewerkingen op dia's   nieuwe dia invoegen, de indeling en de opmaak
                                aanpassen, dia's verwijderen of dupliceren,
                                diaovergangen aanpassen, animaties toevoegen
                                of aanpassen
    op dia's                    tekstvakken invoegen, tekst invoegen en de
                                opmaak van de tekst veranderen, vormen
                                invoegen
    een hyperlink invoegen
    een actieknop toevoegen
    een diavoorstelling starten en dia's presenteren met verschillende
        weergaven
    een gepaste afdruk maken    hand-outs, overzichten, notitiepagina's
    bewaren in verschillende bestandsindelingen zoals pptx of ppsm

Twee verschillen lopen als een draad door dit thema, want daar gaat het mis:

  1. **Een diaovergang tegenover een animatie.** Een overgang zit tussen
     twee dia's, een animatie werkt op iets wat op de dia zelf staat.

  2. **Een hand-out tegenover een notitiepagina.** Een hand-out is voor het
     publiek, met meerdere dia's op één blad. Een notitiepagina is voor de
     spreker, met één dia en zijn notities eronder.

Deel 1 is ontwerpen, dia's, tekst en vormen.
Deel 2 is hyperlinks, actieknoppen, presenteren, afdrukken en bewaren.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een dia in PowerPoint?",
        opties=[
            "één bladzijde van je presentatie, die je straks op het scherm toont",
            "een afbeelding die je in een tekstvak van je presentatie plakt",
            "het effect bij het wisselen van de ene bladzijde naar de volgende",
            "het venster waarin je je presentatie op je computer bewaart",
        ],
        antwoord=0,
        uitleg="Een presentatie is een reeks dia's die je na elkaar toont.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de indeling van een dia?",
        opties=[
            "het vaste patroon van vakken voor een titel, tekst en beeld op die dia",
            "de plaats van die dia in de volgorde van de hele presentatie",
            "de achtergrondkleur die onder alle dia's van de reeks ligt",
            "de tijd die je tijdens het presenteren aan die dia besteedt",
        ],
        antwoord=0,
        uitleg="PowerPoint noemt dat de indeling of lay-out. Je kiest ze per dia en je kan ze achteraf nog wijzigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet dupliceren van een dia?",
        opties=[
            "er een exacte kopie van bij zetten, met dezelfde inhoud en opmaak",
            "de dia naar het einde van de presentatie verplaatsen",
            "de dia verwijderen en de volgende naar voren halen",
            "de inhoud van twee dia's tot één enkele dia samenvoegen",
        ],
        antwoord=0,
        uitleg="Handig als je een dia wil die bijna hetzelfde is: dupliceren en dan aanpassen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een diaovergang?",
        opties=[
            "het effect dat je ziet bij het wisselen naar de volgende dia",
            "het effect waarmee tekst op een dia verschijnt of verdwijnt",
            "de volgorde waarin je de dia's na elkaar wil laten zien",
            "de knop waarmee je de diavoorstelling start en stopt",
        ],
        antwoord=0,
        uitleg="De overgang zit tussen twee dia's. Het effect op de dia zelf heet een animatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een diaovergang en een animatie?",
        opties=[
            "een overgang werkt tussen twee dia's, een animatie op de dia zelf",
            "een overgang werkt op de dia zelf, een animatie tussen twee dia's",
            "een overgang geldt altijd voor de hele presentatie, een animatie nooit",
            "er is geen verschil, het zijn twee namen voor hetzelfde effect",
        ],
        antwoord=0,
        uitleg="Dit is het verschil waarop in schermafdrukken het vaakst getoetst wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een tekstvak op een dia?",
        opties=[
            "een kader waarin je tekst zet en dat je op de dia kan verplaatsen",
            "een kader waarin je enkel een afbeelding of een vorm kan zetten",
            "een kader dat op elke dia van de presentatie tegelijk verschijnt",
            "een kader waarin je de notities voor jezelf als spreker tikt",
        ],
        antwoord=0,
        uitleg="Zonder tekstvak kan je op een dia geen tekst zetten. Je kan het slepen en groter maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke basisbewerkingen op dia's noemt de fiche? Er zijn meerdere juiste antwoorden.",
        opties=[
            "een nieuwe dia invoegen",
            "de indeling en de opmaak van een dia aanpassen",
            "een dia verwijderen of dupliceren",
            "een dia in een ander bestand omzetten naar een tabel",
        ],
        antwoord=[0, 1, 2],
        uitleg="Ook diaovergangen aanpassen en animaties toevoegen horen bij het rijtje. Een dia naar een tabel omzetten staat er niet in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je verwijdert dia 3 uit een presentatie van tien dia's. Wat gebeurt er?",
        opties=[
            "de volgende dia's schuiven op, dia 4 wordt dia 3 en zo verder",
            "er blijft een lege dia 3 staan die je zelf nog moet opvullen",
            "de presentatie houdt tien dia's, want de nummering staat vast",
            "alle animaties van de hele presentatie gaan daardoor verloren",
        ],
        antwoord=0,
        uitleg="Je houdt negen dia's. De nummering past zich aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil op elke dia dezelfde achtergrond en hetzelfde lettertype. Wat gebruik je?",
        opties=[
            "een thema of ontwerp dat voor de hele presentatie geldt",
            "een animatie die je op elke dia afzonderlijk instelt",
            "een hyperlink van de eerste dia naar alle andere dia's",
            "een actieknop die de opmaak bij een klik overneemt",
        ],
        antwoord=0,
        uitleg="Zo blijft je presentatie één geheel en moet je het niet per dia doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor voeg je een vorm op een dia in?",
        opties=[
            "om met een pijl, kader of cirkel iets op de dia aan te duiden",
            "om de tekst van de dia in een opsomming te laten verschijnen",
            "om de dia bij het presenteren langer op het scherm te houden",
            "om de dia als een afzonderlijk bestand te kunnen bewaren",
        ],
        antwoord=0,
        uitleg="Een pijl naar het belangrijkste cijfer doet meer dan een zin erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een dia staat volgeschreven in kleine letters. Wat is de beste aanpassing?",
        opties=[
            "de tekst over meerdere dia's verdelen en groter laten staan",
            "de regelafstand kleiner zetten zodat er nog meer op past",
            "een animatie toevoegen zodat de tekst traag binnenkomt",
            "de dia dupliceren zodat het publiek ze twee keer ziet",
        ],
        antwoord=0,
        uitleg="Een dia is geen blad papier: wat je voorleest hoort niet voluit op het scherm.",
    ),
    dict(
        type="waarofniet",
        vraag="Een animatie werkt op iets wat op de dia staat, zoals een tekstvak of een vorm.",
        antwoord=True,
        uitleg="Daarom kan je op één dia verschillende animaties na elkaar laten lopen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een dia dupliceren is hetzelfde als een dia verwijderen.",
        antwoord=False,
        uitleg="Dupliceren zet er een kopie bij, verwijderen haalt de dia weg.",
    ),
    dict(
        type="waarofniet",
        vraag="De indeling van een dia kan je achteraf nog veranderen.",
        antwoord=True,
        uitleg="De fiche noemt het letterlijk bij de basisbewerkingen: de indeling en de opmaak aanpassen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een diaovergang kan je enkel voor alle dia's tegelijk instellen.",
        antwoord=False,
        uitleg="Je kan ze per dia kiezen, of met één knop op alle dia's toepassen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het effect bij het wisselen van de ene dia naar de volgende?",
        antwoord=["diaovergang", "overgang"],
        uitleg="Een diaovergang. Het effect op de dia zelf heet een animatie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het kader waarin je tekst op een dia zet?",
        antwoord=["tekstvak", "een tekstvak"],
        uitleg="Een tekstvak. Je kan het verplaatsen, vergroten en opmaken.",
    ),
    dict(
        type="invultekst",
        vraag="Welk woord gebruikt PowerPoint voor een exacte kopie van een dia bij zetten?",
        antwoord=["dupliceren", "een dia dupliceren"],
        uitleg="Dupliceren. De kopie komt meteen onder de oorspronkelijke dia.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het vaste patroon van vakken op een dia, in de woorden van de fiche?",
        antwoord=["indeling", "de indeling", "lay-out"],
        uitleg="De indeling, in het Engels de lay-out.",
    ),
    dict(
        type="invultekst",
        vraag="Wat voeg je toe als je wil dat de tekst op een dia één regel per keer verschijnt?",
        antwoord=["animatie", "een animatie", "animaties"],
        uitleg="Een animatie. Ze werkt op iets wat op de dia staat, niet tussen twee dia's.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat doet een hyperlink op een dia?",
        opties=[
            "je klikt erop en komt op een website of op een andere dia uit",
            "je klikt erop en de dia wordt als afbeelding op je computer bewaard",
            "je klikt erop en de hele diavoorstelling begint weer van vooraf",
            "je klikt erop en de tekst eronder verschijnt regel per regel",
        ],
        antwoord=0,
        uitleg="Een hyperlink kan naar buiten verwijzen, maar ook naar een dia in dezelfde presentatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een actieknop?",
        opties=[
            "een knop op de dia die bij een klik iets doet, zoals verder gaan",
            "een knop in de werkbalk waarmee je de presentatie laat starten",
            "een knop op je toetsenbord waarmee je naar de volgende dia gaat",
            "een knop die het geluid van de hele presentatie uitschakelt",
        ],
        antwoord=0,
        uitleg="Je zet hem zelf op de dia. Hij kan naar de volgende dia, naar een andere dia of naar een bestand gaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een notitiepagina als afdruk?",
        opties=[
            "een blad met één dia erop en jouw notities eronder, voor de spreker",
            "een blad met meerdere dia's naast elkaar, bedoeld voor het publiek",
            "een blad met enkel de titels van alle dia's in de juiste volgorde",
            "een blad met de instellingen van de overgangen en de animaties",
        ],
        antwoord=0,
        uitleg="De notitiepagina is voor jou als spreker. Met meerdere dia's per blad heet het een hand-out.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een hand-out?",
        opties=[
            "een afdruk met meerdere dia's op één blad, voor het publiek",
            "een afdruk met één dia per blad en jouw notities eronder",
            "een afdruk van enkel de tekst van de dia's, zonder beelden",
            "een afdruk van de presentatie in de vorm van een tabel",
        ],
        antwoord=0,
        uitleg="Zo kan je publiek meelezen en zelf iets bijschrijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat krijg je als je een presentatie als overzicht afdrukt?",
        opties=[
            "enkel de tekst van de dia's, zonder de beelden en de opmaak",
            "elke dia op een eigen blad, met de beelden en de opmaak erbij",
            "zes dia's per blad met lijntjes ernaast om op te schrijven",
            "een blad per dia met jouw notities voor de spreker eronder",
        ],
        antwoord=0,
        uitleg="Een overzicht is de tekststructuur van je presentatie, handig om je verhaal na te lezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een pptx en een ppsm?",
        opties=[
            "een pptx opent om te bewerken, een ppsm start als voorstelling",
            "een pptx start als voorstelling, een ppsm opent om te bewerken",
            "een pptx kan beelden bevatten en een ppsm enkel tekst en vormen",
            "een pptx is voor Windows en een ppsm werkt enkel op een tablet",
        ],
        antwoord=0,
        uitleg="De s staat voor show: een ppsm begint bij het openen meteen op volle schermgrootte. De m erachter staat voor macro's.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke soorten afdrukken van een presentatie noemt de fiche? Er zijn meerdere juiste antwoorden.",
        opties=[
            "hand-outs",
            "overzichten",
            "notitiepagina's",
            "adresetiketten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Hand-outs, overzichten en notitiepagina's. Etiketten horen bij een tekstverwerker, niet bij een presentatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil tijdens het presenteren je eigen notities zien, maar het publiek niet. Wat gebruik je?",
        opties=[
            "de presentatorweergave, met je notities op jouw eigen scherm",
            "de diasorteerder, met alle dia's als miniaturen naast elkaar",
            "een hand-out die je voor jezelf op papier hebt afgedrukt",
            "een extra dia achteraan waarop je je notities hebt gezet",
        ],
        antwoord=0,
        uitleg="Het publiek ziet de dia op de projector, jij ziet de dia met je notities erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil tijdens het presenteren met één klik naar een dia achteraan kunnen springen. Wat zet je klaar?",
        opties=[
            "een hyperlink of een actieknop naar die dia op je dia zetten",
            "die dia dupliceren en de kopie vooraan in de reeks zetten",
            "een animatie op die dia zetten zodat ze sneller verschijnt",
            "de diaovergang van alle dia's tussenin op nul zetten",
        ],
        antwoord=0,
        uitleg="Zo moet je niet door alle dia's ertussen klikken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke weergave gebruik je om de volgorde van je dia's te veranderen?",
        opties=[
            "de diasorteerder, waar alle dia's als miniaturen naast elkaar staan",
            "de presentatorweergave, met je notities naast de huidige dia",
            "de leesweergave, waarin je de presentatie in een venster bekijkt",
            "de afdrukweergave, waarin je de dia's op een blad ziet staan",
        ],
        antwoord=0,
        uitleg="In de diasorteerder sleep je een dia naar zijn nieuwe plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom bewaart iemand een presentatie als ppsm in plaats van als pptx?",
        opties=[
            "zodat ze bij het openen meteen als diavoorstelling begint",
            "zodat het bestand veel kleiner wordt dan in elke andere indeling",
            "zodat niemand de tekst van de dia's nog kan selecteren of kopiëren",
            "zodat de presentatie ook zonder PowerPoint te bewerken valt",
        ],
        antwoord=0,
        uitleg="Handig op een beurs of in een wachtzaal: dubbelklikken en het loopt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hyperlink op een dia kan ook naar een andere dia in dezelfde presentatie verwijzen.",
        antwoord=True,
        uitleg="Niet alleen naar een website dus. Zo bouw je een presentatie waarin je zelf kan kiezen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hand-out en een notitiepagina zijn twee namen voor dezelfde afdruk.",
        antwoord=False,
        uitleg="De hand-out is voor het publiek, de notitiepagina voor de spreker.",
    ),
    dict(
        type="waarofniet",
        vraag="Een diavoorstelling kan je starten vanaf de eerste dia of vanaf de dia waar je staat.",
        antwoord=True,
        uitleg="Handig bij het nakijken: je hoeft niet elke keer van vooraf te beginnen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een presentatie kan je enkel als pptx bewaren.",
        antwoord=False,
        uitleg="De fiche noemt zelf verschillende bestandsindelingen, zoals pptx en ppsm.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet een afdruk met meerdere dia's op één blad, bedoeld voor het publiek?",
        antwoord=["hand-out", "handout", "hand-outs"],
        uitleg="Een hand-out. Met jouw notities eronder heet het een notitiepagina.",
    ),
    dict(
        type="invultekst",
        vraag="Welke bestandsindeling uit de fiche start bij het openen meteen als diavoorstelling?",
        antwoord=["ppsm", "een ppsm"],
        uitleg="Een ppsm. De s staat voor show.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de verwijzing op een dia waarop je klikt om naar een website te gaan?",
        antwoord=["hyperlink", "een hyperlink"],
        uitleg="Een hyperlink. Hij kan ook naar een andere dia wijzen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de knop die je zelf op een dia zet en die bij een klik iets uitvoert?",
        antwoord=["actieknop", "een actieknop"],
        uitleg="Een actieknop. Je kiest zelf wat hij doet.",
    ),
    dict(
        type="invultekst",
        vraag="Welke afdruk zet één dia op een blad met jouw notities eronder?",
        antwoord=["notitiepagina", "een notitiepagina", "notitiepaginas"],
        uitleg="De notitiepagina, de afdruk voor de spreker.",
    ),
]

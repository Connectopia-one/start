# -*- coding: utf-8 -*-
"""Tekstverwerking met Word.

Het eerste van vier thema's uit "ik ben digitaal vaardig", het zwaarste blok
van de fiche met 17,5 procent.

Lees eerst deze zin uit de fiche, want ze bepaalt hoe dit thema geschreven is:
"Tijdens het examen krijg je gesloten vragen over de onderdelen van het
office-pakket, zoals Word, Excel en PowerPoint. Je werkt niet met de
programma's zelf, maar krijgt schermafdrukken uit Windows 10 en MS Office
365."

Je moet dus weten wat een knop doet en waar iets staat, niet zelf een
document maken. De vragen hieronder zijn daarom kennisvragen over de
functies, in de woorden die Office in het Nederlands gebruikt.

Wat de fiche voor Word opsomt:
    tekenopmaak      lettertype, tekengrootte, vet, cursief, onderstrepen,
                     tekstkleur, markeren, superscript en subscript, doorhalen
    alineaopmaak     regelafstand, uitlijning, inspringen, tekstdoorloop,
                     afstand tussen alinea's
    opsommingen
    paginaopmaak     marges, afdrukstand, formaat
    kop- en voettekst, automatische paginanummering
    tabellen         randen en arcering, uitlijnen, rijen en kolommen
                     toevoegen of verwijderen, cellen samenvoegen of splitsen
    afdrukken        sortering, enkel- of dubbelzijdig, kleur
    opslaan als PDF

Het verschil tussen tekenopmaak en alineaopmaak loopt als een draad door dit
thema: tekenopmaak werkt op de letters die je selecteert, alineaopmaak op de
hele alinea waar je cursor in staat.

Deel 1 is tekenopmaak, alineaopmaak en opsommingen.
Deel 2 is pagina's, tabellen, afdrukken en opslaan.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen tekenopmaak en alineaopmaak?",
        opties=[
            "tekenopmaak werkt op de geselecteerde letters, alineaopmaak op de hele alinea",
            "tekenopmaak werkt op de hele alinea, alineaopmaak op de letters",
            "tekenopmaak geldt voor het hele document",
            "er is geen verschil",
        ],
        antwoord=0,
        uitleg="Daarom hoef je voor regelafstand niets te selecteren: je cursor in de alinea volstaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze is tekenopmaak?",
        opties=["cursief", "regelafstand", "inspringen", "uitlijning"],
        antwoord=0,
        uitleg="De andere drie werken op de alinea, niet op de letters.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze is alineaopmaak?",
        opties=["regelafstand", "tekstkleur", "vet", "doorhalen"],
        antwoord=0,
        uitleg="Regelafstand geldt voor de hele alinea. De andere drie zijn tekenopmaak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is superscript?",
        opties=[
            "kleine tekens iets boven de regel, zoals bij m2",
            "kleine tekens iets onder de regel, zoals bij H2O",
            "tekst die doorstreept is",
            "tekst met een gekleurde achtergrond",
        ],
        antwoord=0,
        uitleg="Subscript staat onder de regel, superscript erboven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is subscript?",
        opties=[
            "kleine tekens iets onder de regel, zoals bij H2O",
            "kleine tekens iets boven de regel, zoals bij m2",
            "tekst in een kleinere lettergrootte",
            "tekst in een lichtere kleur",
        ],
        antwoord=0,
        uitleg="Het tegenovergestelde van superscript.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet markeren in Word?",
        opties=[
            "een gekleurde achtergrond achter de tekst zetten, als met een fluostift",
            "de letters zelf een andere kleur geven zonder de achtergrond te raken",
            "een streep door de tekst zetten zodat ze geschrapt lijkt",
            "de tekstkleur van de hele alinea in een keer veranderen",
        ],
        antwoord=0,
        uitleg="Tekstkleur verft de letters, markeren verft de achtergrond.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet doorhalen?",
        opties=[
            "een streep door de tekst zetten terwijl ze leesbaar blijft",
            "de tekst volledig uit het document verwijderen, zonder spoor",
            "een streepje onder de tekst zetten over de hele regel",
            "de tekst grijs maken zodat ze veel minder opvalt",
        ],
        antwoord=0,
        uitleg="Handig om te tonen wat geschrapt is zonder het weg te gooien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is uitvullen als uitlijning?",
        opties=[
            "de tekst sluit links én rechts netjes aan",
            "de tekst staat tegen de linkerkant",
            "de tekst staat in het midden",
            "de tekst staat tegen de rechterkant",
        ],
        antwoord=0,
        uitleg="Word rekt de spaties op zodat beide kanten recht zijn. Links, gecentreerd en rechts zijn de drie andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet inspringen?",
        opties=[
            "de alinea verder van de marge laten beginnen",
            "de regelafstand groter maken",
            "een lege regel invoegen",
            "de tekst centreren",
        ],
        antwoord=0,
        uitleg="Je kan links, rechts of enkel op de eerste regel laten inspringen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat regelt de afstand tussen alinea's?",
        opties=[
            "de witruimte boven en onder een alinea",
            "de ruimte tussen de regels binnen een alinea",
            "de breedte van de marges",
            "de grootte van de letters",
        ],
        antwoord=0,
        uitleg="De ruimte binnen de alinea is de regelafstand, die ertussen is iets anders.",
    ),
    dict(
        type="waarofniet",
        vraag="Voor regelafstand volstaat het dat je cursor in de alinea staat.",
        antwoord=True,
        uitleg="Regelafstand is alineaopmaak, en die geldt voor de hele alinea waar je cursor in staat.",
    ),
    dict(
        type="waarofniet",
        vraag="Markeren en tekstkleur veranderen doen hetzelfde.",
        antwoord=False,
        uitleg="Markeren kleurt de achtergrond, tekstkleur kleurt de letters.",
    ),
    dict(
        type="waarofniet",
        vraag="Superscript staat boven de regel en subscript eronder.",
        antwoord=True,
        uitleg="Denk aan m2 tegenover H2O.",
    ),
    dict(
        type="waarofniet",
        vraag="Een opsomming kan je achteraf niet meer wijzigen.",
        antwoord=False,
        uitleg="De fiche vraagt juist dat je een opsomming kan invoegen of wijzigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij de tekenopmaak?",
        opties=["vet", "tekstkleur", "doorhalen", "regelafstand"],
        antwoord=[0, 1, 2],
        uitleg="Regelafstand is alineaopmaak. Ook cursief, onderstrepen, markeren, lettertype, tekengrootte en super- en subscript zijn tekenopmaak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze horen bij de alineaopmaak?",
        opties=["uitlijning", "inspringen", "de afstand tussen alinea's", "de tekengrootte"],
        antwoord=[0, 1, 2],
        uitleg="De tekengrootte is tekenopmaak. Regelafstand en tekstdoorloop horen wel bij de alinea.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de opmaak die de letters iets boven de regel zet, zoals bij m2?",
        antwoord=["superscript", "superscript opmaak"],
        uitleg="Onder de regel heet het subscript.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de ruimte tussen de regels binnen één alinea?",
        antwoord=["regelafstand", "de regelafstand"],
        uitleg="De ruimte tussen twee alinea's is de afstand tussen alinea's.",
    ),
    dict(
        type="invultekst",
        vraag="Welke uitlijning laat de tekst zowel links als rechts netjes aansluiten?",
        antwoord=["uitvullen", "uitgevuld", "uitvullend"],
        uitleg="De andere drie zijn links, gecentreerd en rechts.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil dat één woord midden in een zin vet staat. Wat doe je?",
        opties=[
            "dat woord selecteren en op vet klikken",
            "je cursor in de alinea zetten en op vet klikken",
            "de hele alinea selecteren en op vet klikken",
            "de alineaopmaak aanpassen",
        ],
        antwoord=0,
        uitleg="Vet is tekenopmaak, dus het werkt enkel op wat je selecteert.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat regel je met de marges?",
        opties=[
            "de witte rand rond de tekst op een blad",
            "de ruimte tussen de alinea's",
            "de breedte van een tabel",
            "de grootte van de letters",
        ],
        antwoord=0,
        uitleg="Marges horen bij de paginaopmaak, samen met de afdrukstand en het formaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt Word met de afdrukstand?",
        opties=[
            "of het blad staand of liggend staat",
            "of je in kleur of in zwart-wit afdrukt",
            "of je enkel- of dubbelzijdig afdrukt",
            "in welke volgorde de bladen uit de printer komen",
        ],
        antwoord=0,
        uitleg="Staand heet ook portret, liggend ook landschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het formaat in de paginaopmaak?",
        opties=[
            "de bladgrootte, bijvoorbeeld A4 of A5",
            "het bestandstype waarin je opslaat",
            "de opmaak van de tekst",
            "het aantal kolommen op een blad",
        ],
        antwoord=0,
        uitleg="Marges, afdrukstand en formaat zijn samen de paginaopmaak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient een kop- en voettekst?",
        opties=[
            "tekst die bovenaan of onderaan op elke bladzijde terugkomt",
            "de titel van het document in een groot lettertype",
            "de eerste en de laatste alinea van een document",
            "de inhoudstafel van een document",
        ],
        antwoord=0,
        uitleg="Ideaal voor een paginanummer of de naam van het document.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruik je automatische paginanummering?",
        opties=[
            "de nummers passen zich aan als het document langer of korter wordt",
            "de nummers staan dan altijd netjes in het midden van de voettekst",
            "je document wordt er sneller door bij het openen en opslaan",
            "je kan dan geen kop- of voettekst meer gebruiken in het document",
        ],
        antwoord=0,
        uitleg="Zelf nummers typen betekent alles hertypen zodra er een bladzijde bijkomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is arcering in een tabel?",
        opties=[
            "een kleur of patroon als achtergrond van een cel",
            "de lijn rond een cel",
            "de uitlijning van de tekst in een cel",
            "de breedte van een kolom",
        ],
        antwoord=0,
        uitleg="Randen zijn de lijnen, arcering is de vulling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er als je twee cellen in een tabel samenvoegt?",
        opties=[
            "ze worden één grotere cel",
            "de inhoud van de tweede verdwijnt altijd",
            "er komt een extra rij bij",
            "de tabel wordt breder",
        ],
        antwoord=0,
        uitleg="Handig voor een titel die over meerdere kolommen loopt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt een tabel met vier rijen en wil er een vijfde onderaan. Wat doe je?",
        opties=[
            "een rij toevoegen onder de laatste rij",
            "een kolom toevoegen",
            "de cellen van de laatste rij samenvoegen",
            "de hele tabel opnieuw tekenen met vijf rijen",
        ],
        antwoord=0,
        uitleg="Rijen en kolommen toevoegen of verwijderen hoort bij de tabelindeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan je instellen bij het afdrukken, volgens de fiche?",
        opties=[
            "de sortering, enkel- of dubbelzijdig, en kleur",
            "de regelafstand en de uitlijning van een alinea",
            "het lettertype en de tekengrootte van de tekst",
            "de marges en de kop- en voettekst van de pagina",
        ],
        antwoord=0,
        uitleg="De andere drie zijn opmaak, geen afdrukinstellingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom sla je een document op als PDF?",
        opties=[
            "zodat de opmaak overal hetzelfde blijft en niemand het zomaar wijzigt",
            "zodat het bestand altijd kleiner wordt dan in elk ander bestandsformaat",
            "zodat je het nadien makkelijker kan bewerken in een ander programma",
            "zodat het bij het openen automatisch afgedrukt wordt",
        ],
        antwoord=0,
        uitleg="Daarom is PDF het formaat waarin je iets doorstuurt of laat drukken.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kop- en voettekst komt op elke bladzijde terug.",
        antwoord=True,
        uitleg="Daarom zet je er een paginanummer of de documentnaam in.",
    ),
    dict(
        type="waarofniet",
        vraag="Een PDF kan je in Word even makkelijk bewerken als een gewoon document.",
        antwoord=False,
        uitleg="PDF is net bedoeld om de opmaak vast te zetten.",
    ),
    dict(
        type="waarofniet",
        vraag="Marges, afdrukstand en formaat horen samen bij de paginaopmaak.",
        antwoord=True,
        uitleg="Zo staat het in de fiche.",
    ),
    dict(
        type="waarofniet",
        vraag="Cellen splitsen en cellen samenvoegen zijn hetzelfde.",
        antwoord=False,
        uitleg="Splitsen maakt van één cel meerdere, samenvoegen maakt van meerdere één.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij het tabelontwerp en de tabelindeling?",
        opties=[
            "randen en arcering",
            "rijen en kolommen toevoegen of verwijderen",
            "cellen samenvoegen of splitsen",
            "de marges van het blad",
        ],
        antwoord=[0, 1, 2],
        uitleg="De marges horen bij de paginaopmaak, niet bij de tabel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de witte rand rond de tekst op een blad?",
        antwoord=["marge", "marges", "de marges"],
        uitleg="Marges horen bij de paginaopmaak.",
    ),
    dict(
        type="invultekst",
        vraag="In welk bestandstype sla je op zodat de opmaak overal hetzelfde blijft? Antwoord met de afkorting.",
        antwoord=["PDF", "pdf"],
        uitleg="De fiche vraagt uitdrukkelijk dat je een document als PDF kan opslaan.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet de kleur of het patroon als achtergrond van een cel in een tabel?",
        antwoord=["arcering", "de arcering"],
        uitleg="De lijnen rond de cel heten randen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil een titel over de drie kolommen van je tabel laten lopen. Wat doe je?",
        opties=[
            "de drie cellen van de bovenste rij samenvoegen",
            "een rij toevoegen",
            "de randen van de bovenste rij verwijderen",
            "de kolombreedte van de eerste kolom vergroten",
        ],
        antwoord=0,
        uitleg="Samenvoegen maakt van die drie cellen één brede cel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je document telt twaalf bladzijden en je voegt er vooraan een toe. Wat gebeurt er met automatische paginanummering?",
        opties=[
            "alle nummers schuiven vanzelf op",
            "je moet alle nummers opnieuw typen",
            "de nummering begint opnieuw bij één op elke bladzijde",
            "de nummers verdwijnen",
        ],
        antwoord=0,
        uitleg="Dat is precies waarvoor automatische nummering dient.",
    ),
]

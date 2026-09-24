# -*- coding: utf-8 -*-
"""De vragen voor "Tekstsoorten en het communicatiemodel" (✨ Spark, Nederlands).

Uit de vakfiche: de zes soorten lees- en luisterteksten die je moet kunnen
begrijpen (informeren, overtuigen, een mening geven, instrueren, vertellen en
literaire teksten), en het communicatiemodel met zender, boodschap, ontvanger,
kanaal, context en doel, dat je bij elke lees-, luister- en schrijfopdracht
toepast.

Deel 1 herkent de tekstsoort aan een voorbeeld. Deel 2 past het
communicatiemodel toe en laat zien hoe doel en kanaal de tekst bepalen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Je leest een recept voor pannenkoeken. Wat wil die tekst vooral doen?",
        opties=[
            "Je stap voor stap iets leren doen",
            "Je overtuigen om pannenkoeken te kopen",
            "Zijn mening over pannenkoeken geven",
            "Een verhaal vertellen",
        ],
        antwoord=0,
        uitleg="Een recept is een instructieve tekst: hij legt uit hoe je iets doet, in stappen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke teksten willen je vooral informatie geven?",
        opties=[
            "Een krantenartikel",
            "Een stukje uit een leerboek",
            "Een interview",
            "Een reclamefilmpje",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie informeren. Een reclamefilmpje wil je overtuigen of beïnvloeden.",
    ),
    dict(
        type="invultekst",
        vraag="Een handleiding, een recept en een bijsluiter zijn teksten die je ___ geven.",
        antwoord="instructies",
        uitleg="Instructieve teksten vertellen je hoe je iets doet, meestal in genummerde stappen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een recensie van een boek op een website: wat voor tekst is dat?",
        opties=[
            "Een tekst waarin iemand zijn mening geeft",
            "Een instructie",
            "Een verhalende tekst",
            "Een handleiding",
        ],
        antwoord=0,
        uitleg="In een recensie of een beoordeling zegt iemand wat hij ervan vindt. Dat is een opiniërende tekst.",
    ),
    dict(
        type="waarofniet",
        vraag="Een folder van een politieke partij wil je overtuigen.",
        antwoord=True,
        uitleg="Reclame, propaganda, een campagne of een publireportage willen je overtuigen of beïnvloeden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke teksten vertellen vooral een verhaal?",
        opties=[
            "Een reisverslag",
            "Een videoblog over een weekend in Parijs",
            "Een podcast waarin iemand vertelt wat hij meemaakte",
            "Een veiligheidsvoorschrift in een bedrijf",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie vertellen wat er gebeurd is. Een veiligheidsvoorschrift geeft instructies.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een literaire tekst?",
        opties=[
            "Een tekst met een esthetische waarde, die vaak inspeelt op je gevoel",
            "Elke tekst die in een boek staat",
            "Een tekst met veel moeilijke woorden",
            "Een tekst zonder afbeeldingen",
        ],
        antwoord=0,
        uitleg="Een jeugdboek, een kortverhaal, een strip, een gedicht, een lied of stand-upcomedy: literaire teksten willen je raken, niet alleen informeren.",
    ),
    dict(
        type="invultekst",
        vraag="Wie een boodschap verstuurt, noem je in het communicatiemodel de ___.",
        antwoord="zender",
        uitleg="Zender, boodschap, ontvanger, kanaal, context en doel: dat zijn de zes delen van het communicatiemodel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Voor wie een tekst bedoeld is, noem je in het communicatiemodel de ...",
        opties=["ontvanger", "zender", "context", "boodschap"],
        antwoord=0,
        uitleg="De ontvanger is het publiek: een vriend, een leerkracht, de lezers van een krant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je stuurt een WhatsAppbericht naar je ploegmaats. Wat is het kanaal?",
        opties=["WhatsApp", "Jijzelf", "Je ploegmaats", "De training van morgen"],
        antwoord=0,
        uitleg="Het kanaal is de weg waarlangs je boodschap gaat: een mail, een blog, een telefoongesprek, een app.",
    ),
    dict(
        type="waarofniet",
        vraag="Het doel van een tekst is wat de zender met die tekst wil bereiken.",
        antwoord=True,
        uitleg="Informeren, overtuigen, instrueren, vermaken of iets vertellen: dat is het doel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een hotelbeoordeling op een reissite hoort bij welke soort tekst?",
        opties=[
            "Een tekst waarin iemand zijn mening geeft",
            "Een informatieve tekst",
            "Een literaire tekst",
            "Een instructie",
        ],
        antwoord=0,
        uitleg="Een beoordeling, een review of een reactie op een forum is de mening van één persoon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn kanalen?",
        opties=["Een e-mail", "Een blogbericht", "Een telefoongesprek", "Een vriendin"],
        antwoord=[0, 1, 2],
        uitleg="Een kanaal is het middel waarlangs de boodschap reist. Je vriendin is de ontvanger, niet het kanaal.",
    ),
    dict(
        type="invultekst",
        vraag="De situatie waarin je communiceert — waar je bent, wat er net gebeurd is — heet de ___.",
        antwoord="context",
        uitleg="De context bepaalt mee hoe je iets zegt: je bus is te laat, dus je belt je leerkracht beleefd op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stukje uit een leerboek is een instructieve tekst.",
        antwoord=False,
        uitleg="Een leerboek informeert. Instructies leggen uit hoe je iets doet, stap voor stap, zoals een handleiding of een recept.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een instructiefilmpje op YouTube over hoe je een band plakt: welk doel heeft de maker?",
        opties=[
            "Je leren hoe je iets doet",
            "Je overtuigen om fietsen te kopen",
            "Je zijn mening geven over fietsen",
            "Je een verhaal vertellen",
        ],
        antwoord=0,
        uitleg="Een instructiefilmpje is dezelfde tekstsoort als een handleiding, alleen met beeld in plaats van papier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de boodschap in het communicatiemodel?",
        opties=[
            "Wat de zender precies wil zeggen",
            "Het middel waarlangs de tekst verstuurd wordt",
            "De persoon voor wie de tekst bedoeld is",
            "De plaats waar je de tekst leest",
        ],
        antwoord=0,
        uitleg="De boodschap is de inhoud zelf: 'ik ben tien minuten te laat', 'dit product is de beste koop'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een protestlied hoort bij welke soort tekst?",
        opties=[
            "Een tekst waarin iemand zijn mening geeft",
            "Een informatieve tekst",
            "Een instructie",
            "Een zakelijke tekst",
        ],
        antwoord=0,
        uitleg="Een protestlied brengt een standpunt. Het is bovendien een literaire tekst, want het speelt in op je gevoel.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén tekst kan meer dan één doel hebben.",
        antwoord=True,
        uitleg="Een publireportage informeert én verkoopt. Daarom moet je altijd nagaan wie de zender is en wat hij wil bereiken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een schoolreglement. Wat voor tekst is dat?",
        opties=[
            "Een tekst die je zegt hoe het hoort",
            "Een verhalende tekst",
            "Een literaire tekst",
            "Een recensie",
        ],
        antwoord=0,
        uitleg="Een schoolreglement geeft regels en instructies: het zegt wat je moet doen en laten.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Je belt je leerkracht op om te zeggen dat je tien minuten te laat bent. Wie is de ontvanger?",
        opties=["Je leerkracht", "Jijzelf", "Het telefoongesprek", "De vertraagde bus"],
        antwoord=0,
        uitleg="Jij bent de zender, je leerkracht de ontvanger, de telefoon het kanaal, de vertraagde bus de context.",
    ),
    dict(
        type="meerkeuze",
        vraag="Dezelfde situatie: welke elementen van het communicatiemodel zijn juist benoemd?",
        opties=[
            "Kanaal: het telefoongesprek",
            "Boodschap: dat je tien minuten te laat bent",
            "Context: je bus is te laat",
            "Doel: je leerkracht overtuigen om de les uit te stellen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Je doel is informeren, niet overtuigen. Kanaal, boodschap en context kloppen wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je stuurt over diezelfde bus een bericht vol geïrriteerde emoji's naar je beste vriendin. Waarom is dat gepast en naar je leerkracht niet?",
        opties=[
            "Omdat de ontvanger en het register anders zijn",
            "Omdat emoji's altijd fout zijn",
            "Omdat het kanaal hetzelfde blijft",
            "Omdat de boodschap anders is",
        ],
        antwoord=0,
        uitleg="Dezelfde boodschap, een andere ontvanger: bij een vriendin mag het informeel, bij een leerkracht hoort een formeel register.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf maakt een filmpje dat eruitziet als een reportage, maar het gaat over hun eigen product. Wat is dat?",
        opties=[
            "Een publireportage: reclame die zich voordoet als informatie",
            "Een gewone reportage",
            "Een instructiefilmpje",
            "Een recensie",
        ],
        antwoord=0,
        uitleg="Kijk naar de zender en het doel. Is de zender de verkoper, dan is het doel verkopen, hoe informatief het er ook uitziet.",
    ),
    dict(
        type="invultekst",
        vraag="Reclame, propaganda en een campagne tegen te snel rijden willen je vooral ___.",
        antwoord="overtuigen",
        uitleg="Ze willen je gedrag of je mening veranderen. Dat is de tekstsoort 'overtuigen of beïnvloeden'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet een zoekertje schrijven om je oude gsm te verkopen. Wat is je doel?",
        opties=[
            "Informatie geven én iemand overtuigen om te kopen",
            "Alleen een verhaal vertellen",
            "Alleen instructies geven",
            "Je mening geven over gsm's",
        ],
        antwoord=0,
        uitleg="Een zoekertje geeft de feiten (model, leeftijd, prijs) en probeert tegelijk te overtuigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen stel je jezelf als je het communicatiemodel toepast op een tekst?",
        opties=[
            "Van wie is deze tekst?",
            "Voor wie is hij bedoeld?",
            "Waarom is hij gemaakt?",
            "Hoeveel woorden telt hij?",
        ],
        antwoord=[0, 1, 2],
        uitleg="Zender, ontvanger en doel zijn de drie vragen waarmee je begint. De lengte zegt niets over de bedoeling.",
    ),
    dict(
        type="waarofniet",
        vraag="Het kanaal kan de vorm van je boodschap veranderen.",
        antwoord=True,
        uitleg="Een mail schrijf je anders dan een appbericht, ook al vertel je hetzelfde. Kanaal en register hangen samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tekst begint met 'Beste ouders,' en eindigt met 'Met vriendelijke groeten, de directie'. Wat leid je daaruit af?",
        opties=[
            "De ontvangers zijn de ouders en de zender is de school",
            "De zender is een leerling",
            "Het is een literaire tekst",
            "Het kanaal is een telefoongesprek",
        ],
        antwoord=0,
        uitleg="Aanhef en ondertekening verraden zender en ontvanger. Het formele register past bij een schoolbrief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke teksten willen je vooral iets laten voelen of beleven?",
        opties=[
            "Een gedicht",
            "Een kortverhaal",
            "Een strip",
            "Een bijsluiter",
        ],
        antwoord=[0, 1, 2],
        uitleg="Literaire teksten spelen in op emoties. Een bijsluiter is een instructie: hij moet vooral duidelijk zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest op een forum: 'Deze koptelefoon ging bij mij al na twee maanden stuk.' Wat voor tekst is dat?",
        opties=[
            "Een mening van één gebruiker",
            "Een instructie",
            "Een objectieve productbeschrijving",
            "Een literaire tekst",
        ],
        antwoord=0,
        uitleg="Het is een ervaring en een oordeel van één persoon. Dat kan kloppen, maar het is geen algemeen onderzoek.",
    ),
    dict(
        type="waarofniet",
        vraag="Een interview is een informatieve tekst, ook al bestaat het uit vragen en antwoorden.",
        antwoord=True,
        uitleg="De vorm is een gesprek, maar het doel is je informatie geven over een onderwerp of een persoon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een reportage en een reclamefilmpje over hetzelfde product?",
        opties=[
            "De zender en het doel verschillen",
            "Alleen de lengte verschilt",
            "Er is geen verschil",
            "Een reportage is altijd korter",
        ],
        antwoord=0,
        uitleg="Bij een reportage is de zender een redactie die wil informeren; bij reclame is de zender de verkoper die wil verkopen.",
    ),
    dict(
        type="invultekst",
        vraag="Een tekst die vertelt wat iemand heeft meegemaakt, noem je een ___ tekst.",
        antwoord="verhalende",
        uitleg="Een reisverslag, een videoblog of een podcast waarin iemand vertelt: dat zijn verhalende teksten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schrijft een mail aan de gemeente over een kapot voetpad. Welk register kies je?",
        opties=[
            "Formeel, met 'u' en een nette slotgroet",
            "Informeel, met emoji's",
            "Dialect",
            "Jongerentaal",
        ],
        antwoord=0,
        uitleg="Een onbekende volwassene in een officiële rol: dan kies je het formele register.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het doel van een tekst kloppen?",
        opties=[
            "Het doel bepaalt mee hoe de tekst geschreven is",
            "Dezelfde informatie kan met een ander doel heel anders klinken",
            "Je kan het doel vaak afleiden uit wie de zender is",
            "Het doel staat altijd letterlijk in de eerste zin",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het doel zit meestal tussen de regels: je leidt het af uit de zender, de toon en het kanaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een campagne wil dat je minder snel rijdt. Wat is de ontvanger?",
        opties=["De bestuurders", "De overheid", "Het affiche", "De snelheid"],
        antwoord=0,
        uitleg="De overheid is de zender, het affiche het kanaal, de bestuurders zijn de ontvangers.",
    ),
    dict(
        type="waarofniet",
        vraag="Stand-upcomedy kan je een literaire tekst noemen.",
        antwoord=True,
        uitleg="De vakfiche rekent stand-upcomedy bij de literaire teksten: ze speelt met taal en met je gevoel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een tekst zonder titel en zonder naam van de auteur. Waaraan zie je toch welke soort tekst het is?",
        opties=[
            "Aan de opbouw en de toon: stappen, argumenten, feiten of een verhaal",
            "Aan het lettertype",
            "Aan het aantal alinea's",
            "Aan de lengte van de tekst",
        ],
        antwoord=0,
        uitleg="Genummerde stappen wijzen op een instructie, argumenten op overtuigen, gebeurtenissen op een verhaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig om te weten met welke tekstsoort je te maken hebt?",
        opties=[
            "Je weet dan wat je mag verwachten en waarop je moet letten",
            "Je hoeft de tekst dan niet meer te lezen",
            "Je kent dan meteen alle moeilijke woorden",
            "Je weet dan hoe lang de tekst is",
        ],
        antwoord=0,
        uitleg="Bij een overtuigende tekst let je op argumenten en op eenzijdigheid; bij een instructie op de volgorde van de stappen.",
    ),
]

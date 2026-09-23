# -*- coding: utf-8 -*-
"""De vragen voor "Wetenschappelijk onderzoek" (✨ Spark, natuurwetenschappen).

Uit de vakfiche, deel Onderzoek: de stappen van het wetenschappelijk onderzoek,
van de probleemstelling tot het reflecteren en communiceren; de criteria van een
goede onderzoeksvraag (open, enkelvoudig, objectief, haalbaar, onderzoekbaar en
relevant, zie bijlage 1); het gebruik van een model zoals een schets, een tabel,
een grafiek of een formule; gegevens uit grafieken en tabellen halen; formules
omvormen en combineren; en het onderzoeken van een recht of een omgekeerd
evenredig verband. Op het examen krijg je zo'n onderzoek als opgave, rond een
STEM-probleem of een maatschappelijke uitdaging.

Deel 1 gaat over de stappen en de woorden. Deel 2 laat je oordelen: is dit een
goede onderzoeksvraag, klopt deze conclusie, is deze proef eerlijk opgezet?
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarmee begint een wetenschappelijk onderzoek?",
        opties=[
            "Met een probleemstelling en een onderzoeksvraag",
            "Met de conclusie",
            "Met het maken van een grafiek",
        ],
        antwoord=0,
        uitleg="Eerst baken je het probleem af en stel je een onderzoeksvraag. Pas daarna bedenk je een hypothese en een plan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een hypothese?",
        opties=[
            "Een verwachting die je vooraf formuleert en die je gaat onderzoeken",
            "Het resultaat van je metingen",
            "De besluitende zin van je verslag",
        ],
        antwoord=0,
        uitleg="Een hypothese is een verwacht antwoord op je onderzoeksvraag, vaak in de vorm 'als ..., dan ...'. Ze mag achteraf gerust verkeerd blijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zet in de juiste volgorde: conclusie trekken, data verzamelen, onderzoeksvraag opstellen, onderzoeksplan maken.",
        opties=[
            "onderzoeksvraag – onderzoeksplan – data verzamelen – conclusie",
            "onderzoeksplan – onderzoeksvraag – conclusie – data verzamelen",
            "data verzamelen – onderzoeksvraag – onderzoeksplan – conclusie",
        ],
        antwoord=0,
        uitleg="Eerst de vraag, dan het plan, dan meten, dan analyseren en besluiten. Op het einde reflecteer je over je methode en communiceer je je resultaat.",
    ),
    dict(
        type="invultekst",
        vraag="Het overzicht van wat je gaat doen, met welk materiaal en in welke stappen, heet het ___.",
        antwoord="onderzoeksplan",
        uitleg="In een onderzoeksplan staat wat je meet, waarmee, hoe vaak en wat je constant houdt. Zo kan iemand anders je proef overdoen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke criteria moet een goede onderzoeksvraag halen?",
        opties=["Open", "Enkelvoudig", "Onderzoekbaar", "Grappig"],
        antwoord=[0, 1, 2],
        uitleg="De zes criteria uit de vakfiche zijn: open, enkelvoudig, objectief, haalbaar, onderzoekbaar en relevant. Die lijst krijg je ook op het examen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat een onderzoeksvraag 'enkelvoudig' moet zijn?",
        opties=[
            "Ze gaat over één onderwerp of één probleem",
            "Ze is kort geschreven",
            "Ze heeft één woord als antwoord",
        ],
        antwoord=0,
        uitleg="Onderzoek je twee dingen tegelijk, dan weet je achteraf niet welke van de twee je resultaat verklaart. Splits zo'n vraag dus in twee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent 'objectief' bij een onderzoeksvraag?",
        opties=[
            "Ze laat geen mening of overtuiging blijken",
            "Ze is met een toestel te meten",
            "Ze is door iedereen te begrijpen",
        ],
        antwoord=0,
        uitleg="'Waarom is zonne-energie de beste energiebron?' is niet objectief: het antwoord zit al in de vraag. Beter: 'Welke invloed heeft de stand van een zonnepaneel op de opbrengst?'",
    ),
    dict(
        type="waarofniet",
        vraag="Een onderzoeksvraag mag geen opzoekvraag zijn.",
        antwoord=True,
        uitleg="Onderzoekbaar betekent dat je het antwoord niet zomaar kan opzoeken of meteen weet: je moet er data voor verzamelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een variabele in een onderzoek?",
        opties=[
            "Iets dat kan veranderen en dat je meet of instelt",
            "Het besluit van je onderzoek",
            "Het materiaal dat je gebruikt",
        ],
        antwoord=0,
        uitleg="Je verandert er één (bijvoorbeeld de hoeveelheid licht), je meet er één (de groei) en alle andere houd je constant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom houd je in een proef alle andere omstandigheden gelijk?",
        opties=[
            "Anders weet je niet waardoor het verschil komt",
            "Omdat het sneller gaat",
            "Omdat de leerkracht dat vraagt",
        ],
        antwoord=0,
        uitleg="Verander je twee dingen tegelijk, dan kan je het resultaat aan geen van beide toeschrijven. Één variabele veranderen maakt je besluit geldig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom herhaal je een meting verschillende keren?",
        opties=[
            "Om toevallige fouten op te vangen en je resultaat betrouwbaarder te maken",
            "Om meer bladzijden te vullen",
            "Omdat één meting altijd fout is",
        ],
        antwoord=0,
        uitleg="Eén meting kan toevallig afwijken. Meet je meerdere keren en neem je het gemiddelde, dan weeg je die toevalligheden weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staat de afkorting STEM?",
        opties=[
            "Science, Technology, Engineering en Mathematics",
            "Studie, Techniek, Energie en Milieu",
            "Systeem, Test, Experiment en Model",
        ],
        antwoord=0,
        uitleg="Bij een STEM-opdracht zet je wetenschap, techniek, ontwerpen en wiskunde samen in om een probleem op te lossen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn modellen die je in een onderzoek kan gebruiken?",
        opties=["Een tabel", "Een grafiek", "Een schets", "Een gevoel"],
        antwoord=[0, 1, 2],
        uitleg="Een schets, een tabel, een grafiek, een formule of een vergelijking zijn manieren om je gegevens overzichtelijk voor te stellen.",
    ),
    dict(
        type="invultekst",
        vraag="De metingen en gegevens die je verzamelt, noem je samen je ___.",
        antwoord="data",
        uitleg="Data zijn je ruwe gegevens. Je verwerkt ze in een tabel of een grafiek, en pas daarna analyseer je ze.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zet je op de horizontale as van een grafiek?",
        opties=[
            "De grootheid die je zelf instelt of laat veranderen",
            "De grootheid die je meet",
            "Altijd de tijd",
        ],
        antwoord=0,
        uitleg="Op de x-as staat wat je zelf regelt, op de y-as wat daarvan afhangt. Bij een beweging is dat inderdaad vaak de tijd, maar niet altijd.",
    ),
    dict(
        type="waarofniet",
        vraag="Een conclusie moet een antwoord geven op je onderzoeksvraag.",
        antwoord=True,
        uitleg="De conclusie is de verklaring of het antwoord op je onderzoeksvraag, en ze steunt altijd op je data. Wat je niet gemeten hebt, staat er niet in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is reflecteren op het einde van een onderzoek?",
        opties=[
            "Terugkijken op je methode en je resultaten en zeggen wat beter kon",
            "Je resultaten opnieuw meten",
            "Je onderzoeksvraag veranderen tot ze klopt",
        ],
        antwoord=0,
        uitleg="Reflecteren betekent eerlijk zeggen wat er misliep en wat je zou aanpassen. Daarna communiceer je je resultaat, bijvoorbeeld in een verslag of een presentatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent 'haalbaar' bij een onderzoeksvraag?",
        opties=[
            "Je kan het onderzoek uitvoeren met de tijd en middelen die er zijn",
            "Je kent het antwoord al",
            "Iedereen vindt de vraag interessant",
        ],
        antwoord=0,
        uitleg="'Hoe evolueert de zeespiegel de komende honderd jaar?' is een mooie vraag, maar niet haalbaar voor een schoolonderzoek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit een tabel lees je: bij 10 °C duurt het 40 min, bij 20 °C 20 min, bij 40 °C 10 min. Wat is het verband?",
        opties=[
            "Hoe hoger de temperatuur, hoe korter de tijd",
            "Hoe hoger de temperatuur, hoe langer de tijd",
            "Er is geen verband",
        ],
        antwoord=0,
        uitleg="Gegevens uit een tabel halen is een vaardigheid op zich: kijk of de tweede kolom stijgt of daalt terwijl de eerste stijgt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grafiek met een rechte door de oorsprong wijst op een recht evenredig verband.",
        antwoord=True,
        uitleg="Recht evenredig betekent: wordt de ene twee keer zo groot, dan wordt de andere dat ook. Bij een omgekeerd evenredig verband krijg je een dalende kromme.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke vraag is een goede onderzoeksvraag?",
        opties=[
            "Welke invloed heeft de hoeveelheid water op de groei van tuinkers?",
            "Is tuinkers lekker?",
            "Hoeveel soorten tuinkers bestaan er?",
        ],
        antwoord=0,
        uitleg="De eerste is open, enkelvoudig, objectief en onderzoekbaar. De tweede vraagt een mening en de derde is een opzoekvraag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is 'Hoeveel poten heeft een spin?' geen goede onderzoeksvraag?",
        opties=[
            "Ze is niet onderzoekbaar: je kan het gewoon opzoeken",
            "Ze is niet relevant",
            "Ze is niet haalbaar",
        ],
        antwoord=0,
        uitleg="Onderzoekbaar betekent dat je er data voor moet verzamelen. Een vraag met een bekend antwoord is een opzoekvraag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is 'Is een elektrische auto niet beter dan een benzineauto?' geen goede onderzoeksvraag?",
        opties=[
            "Ze is niet open en niet objectief: het antwoord zit al in de vraag",
            "Ze is niet haalbaar",
            "Ze gaat over te weinig onderwerpen",
        ],
        antwoord=0,
        uitleg="Je kan ze met ja of nee beantwoorden en ze verraadt een mening. Beter: 'Welke invloed heeft de buitentemperatuur op het verbruik van een elektrische auto?'",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke fouten zitten er in de vraag 'Groeien planten sneller met meer licht en meer mest?'",
        opties=[
            "Ze is niet enkelvoudig: er staan twee variabelen in",
            "Ze is gesloten: je kan met ja of nee antwoorden",
            "Ze is niet haalbaar in een schooljaar",
            "Ze is niet relevant",
        ],
        antwoord=[0, 1],
        uitleg="Twee variabelen tegelijk en een ja-of-nee-vorm. Beter: 'Welke invloed heeft de hoeveelheid licht op de groei van een plant?', en mest onderzoek je apart.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je test of planten sneller groeien met meer licht. Welke dingen houd je gelijk?",
        opties=[
            "De hoeveelheid water",
            "De soort plant",
            "De temperatuur",
            "De hoeveelheid licht",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alles blijft gelijk behalve de ene variabele die je onderzoekt. De hoeveelheid licht is net wat je laat verschillen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling besluit: 'Mijn hypothese was juist, want ik vond het logisch.' Wat schort daaraan?",
        opties=[
            "Een conclusie moet op data steunen, niet op een gevoel",
            "Een hypothese mag nooit juist zijn",
            "Hij had geen hypothese mogen opstellen",
        ],
        antwoord=0,
        uitleg="Wetenschap is: meten, en je besluit halen uit wat je gemeten hebt. Ook een hypothese die niet uitkomt, is een goed resultaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Als je hypothese niet uitkomt, is je onderzoek mislukt.",
        antwoord=False,
        uitleg="Een weerlegde hypothese is een resultaat. Je hebt iets geleerd over hoe het níet zit, en dat hoort bij onderzoek doen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet de temperatuur van afkoelend water: 80 °C, 60 °C, 45 °C, 35 °C, 30 °C. Wat zie je in de grafiek?",
        opties=[
            "Een dalende kromme die steeds vlakker wordt",
            "Een rechte die stijgt",
            "Een horizontale rechte",
        ],
        antwoord=0,
        uitleg="De temperatuur daalt snel in het begin en trager naarmate ze de kamertemperatuur nadert. De daling per meting wordt dus kleiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit de formule v = Δx / Δt: hoe schrijf je Δt in functie van de andere?",
        opties=["Δt = Δx / v", "Δt = v × Δx", "Δt = v / Δx"],
        antwoord=0,
        uitleg="Een formule omvormen is een wiskundige vaardigheid die je hier nodig hebt: uit v = Δx / Δt volgt Δx = v × Δt en dus Δt = Δx / v.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit de formule ρ = m / V: hoe bereken je de massa?",
        opties=["m = ρ × V", "m = ρ / V", "m = V / ρ"],
        antwoord=0,
        uitleg="Vermenigvuldig beide kanten met V. Zo kan je uit dezelfde formule alle drie de grootheden halen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke situaties zijn recht evenredig?",
        opties=[
            "Het aantal broden en de prijs die je betaalt",
            "De tijd die je fietst en de afgelegde weg aan constante snelheid",
            "Het aantal werkers en de tijd om één klus af te maken",
            "De massa en het volume van eenzelfde stof",
        ],
        antwoord=[0, 1, 3],
        uitleg="Bij recht evenredig verdubbelt de ene als de andere verdubbelt. Meer werkers betekent net minder tijd: dat is omgekeerd evenredig.",
    ),
    dict(
        type="invultekst",
        vraag="Wordt de ene grootheid twee keer zo groot terwijl de andere halveert, dan is het verband ___ evenredig.",
        antwoord="omgekeerd",
        uitleg="Bij een omgekeerd evenredig verband blijft het product van de twee constant, bijvoorbeeld snelheid × tijdsduur bij een vaste afstand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker meet maar één plant en besluit dat alle planten zo groeien. Wat is er fout?",
        opties=[
            "Eén meting is te weinig om te veralgemenen",
            "Hij had een andere plant moeten kiezen",
            "Hij had een grafiek moeten maken",
        ],
        antwoord=0,
        uitleg="Met één plant kan een toevalligheid je hele besluit sturen. Meer herhalingen maken je conclusie betrouwbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort er in het verslag van je onderzoek?",
        opties=[
            "Je onderzoeksvraag en hypothese",
            "Je werkwijze en je resultaten",
            "Je conclusie en je reflectie",
            "Enkel de resultaten die je hypothese bevestigen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Communiceren betekent eerlijk en volledig rapporteren. Resultaten weglaten omdat ze niet passen, mag nooit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil weten welk isolatiemateriaal een beker koffie het langst warm houdt. Wat is je meetbare variabele?",
        opties=[
            "De temperatuur van de koffie na een bepaalde tijd",
            "De kleur van het materiaal",
            "De prijs van het materiaal",
        ],
        antwoord=0,
        uitleg="Je meet de temperatuur, je verandert het materiaal, en je houdt de hoeveelheid koffie, de begintemperatuur en de tijd gelijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een onderzoek over een maatschappelijk probleem mag je ook technische en wiskundige kennis gebruiken.",
        antwoord=True,
        uitleg="Dat is net de bedoeling van STEM: wetenschap, techniek, ontwerpen en wiskunde samen inzetten om tot een oplossing te komen.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een grafiek lees je bij 4 s een afstand van 20 m af. Wat is de snelheid als de lijn een rechte door de oorsprong is?",
        opties=["5 m/s", "80 m/s", "0,2 m/s"],
        antwoord=0,
        uitleg="Gegevens uit een grafiek halen: v = Δx / Δt = 20 : 4 = 5 m/s. Bij een rechte door de oorsprong geldt dat op elk punt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een waarneming en een besluit?",
        opties=[
            "Een waarneming is wat je ziet of meet, een besluit is wat je daaruit afleidt",
            "Er is geen verschil",
            "Een waarneming komt na het besluit",
        ],
        antwoord=0,
        uitleg="'Het water is 30 °C' is een waarneming. 'Het water koelt trager af met een deksel' is een besluit dat je uit meerdere waarnemingen haalt.",
    ),
    dict(
        type="invultekst",
        vraag="Een verwachting die je vooraf opschrijft en daarna toetst, heet een ___.",
        antwoord="hypothese",
        uitleg="Je schrijft ze op vóór je meet. Anders pas je je verwachting ongemerkt aan je resultaat aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt of een plant met mest sneller groeit, maar je zet die plant ook nog eens voor het raam. Wat is het probleem?",
        opties=[
            "Je verandert twee dingen tegelijk, dus je weet niet wat het verschil maakt",
            "Mest werkt niet voor het raam",
            "Je hebt te weinig planten nodig",
        ],
        antwoord=0,
        uitleg="Licht en mest lopen nu door elkaar. Zet beide planten op dezelfde plek en laat alleen de mest verschillen.",
    ),
]

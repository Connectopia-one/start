# -*- coding: utf-8 -*-
"""Kunstanalyse en kunstreflectie.

Zevende thema kunstbeschouwing (fiche 3DDO):

    kunstanalyse met richtvragen: hoe en waarmee (bouwstenen, materiaal,
    techniek), wat (inhoud), waarvoor (functie), wie, waar en wanneer
    (context), en de samenhang daartussen
    kunstreflectie: factoren die de interpretatie beïnvloeden (tijd en ruimte,
    persoonlijk referentiekader, veranderende kennis en technologie,
    modetrends) en perspectieven (persoonlijk, derde persoon: critici,
    groot publiek, musea en galerieën, en economisch)

Deel 1 is de kunstanalyse, deel 2 de kunstreflectie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke richtvraag hoort bij de middelen van vormgeving?",
        opties=[
            "hoe en waarmee is het werk gemaakt?",
            "waarvoor dient het werk?",
            "wie maakte het werk, waar en wanneer?",
            "wat stelt het werk voor?",
        ],
        antwoord=0,
        uitleg="Bij hoe en waarmee kijk je naar de bouwstenen, het materiaal en de techniek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke richtvraag hoort bij de functie van een kunstuiting?",
        opties=["waarvoor?", "wat?", "hoe en waarmee?", "wie, waar en wanneer?"],
        antwoord=0,
        uitleg="Bij waarvoor vraag je je af waarom het werk gemaakt werd: om te versieren, te vertellen, te overtuigen, te ontspannen, ...",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke richtvraag hoort bij de context?",
        opties=["wie, waar en wanneer?", "wat?", "waarvoor?", "hoe en waarmee?"],
        antwoord=0,
        uitleg="De context is de kunstenaar, de plaats, de tijd en de samenleving waarin het werk ontstond.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij hoe en waarmee een werk gemaakt is?",
        opties=[
            "de bouwstenen, zoals lijn, kleur, vorm of ritme",
            "het materiaal en de techniek",
            "het jaar waarin de kunstenaar geboren werd",
            "de reden waarom de opdrachtgever het werk bestelde",
        ],
        antwoord=[0, 1],
        uitleg="Het geboortejaar hoort bij de context, de reden van de opdrachtgever bij de functie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je beschrijft dat een schilderij een moeder met kind in een keuken toont. Welke richtvraag beantwoord je?",
        opties=["wat?", "waarvoor?", "hoe en waarmee?", "wie, waar en wanneer?"],
        antwoord=0,
        uitleg="Wat het werk voorstelt, is de inhoud.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je noteert: olieverf op doek, dikke penseelstreken, warme oranje en gele tinten. Welke richtvraag beantwoord je?",
        opties=["hoe en waarmee?", "wat?", "waarvoor?", "wie, waar en wanneer?"],
        antwoord=0,
        uitleg="Materiaal, techniek en kleur zijn middelen van vormgeving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je noteert: geschilderd in 1937 in Parijs, kort na het bombardement op een Spaans dorp. Welke richtvraag beantwoord je?",
        opties=["wie, waar en wanneer?", "hoe en waarmee?", "wat?", "waarvoor?"],
        antwoord=0,
        uitleg="Tijd, plaats en gebeurtenissen horen bij de context. Het gaat om Guernica van Picasso.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de samenhang tussen inhoud, functie, context en vormgeving belangrijk in een analyse?",
        opties=[
            "omdat je pas begrijpt waarom een werk er zo uitziet als je die vier aan elkaar koppelt",
            "omdat je dan enkel naar de kleuren moet kijken en de rest mag overslaan",
            "omdat de vier elementen altijd precies hetzelfde zeggen en je er dus één mag kiezen",
            "omdat een analyse anders te kort is voor een examen of een taak op school",
        ],
        antwoord=0,
        uitleg="Bijvoorbeeld: een oorlog (context) leidt tot een aanklacht (functie), met gebroken vormen en grijze kleuren (vormgeving).",
    ),
    dict(
        type="meerkeuze",
        vraag="Guernica van Picasso is enkel in zwart, wit en grijs geschilderd, met gebroken lichamen en schreeuwende figuren. Hoe hangt die vormgeving samen met de inhoud?",
        opties=[
            "de sombere kleuren en de vervormingen versterken de gruwel en de pijn van de oorlog",
            "de kleuren zijn toevallig gekozen en hebben niets met de inhoud te maken",
            "zwart en wit waren de enige kleuren die Picasso toen nog in zijn atelier had",
            "de vervormingen tonen dat Picasso de mensen niet goed kon tekenen",
        ],
        antwoord=0,
        uitleg="De vorm draagt de boodschap: geen kleur, geen schoonheid, enkel pijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met welke stap begin je best een kunstanalyse?",
        opties=[
            "goed kijken en beschrijven wat je ziet, nog zonder oordeel",
            "meteen zeggen of je het werk mooi of lelijk vindt",
            "opzoeken hoeveel het werk op een veiling heeft opgebracht",
            "het werk vergelijken met je eigen tekeningen van vroeger",
        ],
        antwoord=0,
        uitleg="Eerst beschrijf je, dan analyseer en interpreteer je. Een oordeel komt pas op het einde.",
    ),
    dict(
        type="invultekst",
        vraag="Bij de richtvraag wat? beschrijf je de ... van de kunstuiting.",
        antwoord=["inhoud"],
        uitleg="De inhoud is wat het werk voorstelt of waarover het gaat.",
    ),
    dict(
        type="invultekst",
        vraag="Bij de richtvraag waarvoor? zoek je de ... van de kunstuiting.",
        antwoord=["functie"],
        uitleg="Bijvoorbeeld een religieuze, decoratieve, verhalende of maatschappijkritische functie.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een analyse van een dansvoorstelling kun je dezelfde richtvragen gebruiken als bij een schilderij.",
        antwoord=True,
        uitleg="De richtvragen werken voor elke kunstvorm. Enkel de bouwstenen verschillen, zoals beweging en ruimte bij dans.",
    ),
    dict(
        type="waarofniet",
        vraag="Het materiaal van een beeld heeft geen invloed op hoe je het beeld ervaart.",
        antwoord=False,
        uitleg="Koud marmer, warm hout of glanzend staal geven elk een ander gevoel.",
    ),
    dict(
        type="waarofniet",
        vraag="De context van een werk kan verklaren waarom een kunstenaar voor bepaalde kleuren of vormen koos.",
        antwoord=True,
        uitleg="Zo hangen de sombere tinten van een oorlogsschilderij samen met de tijd waarin het ontstond.",
    ),
    dict(
        type="waarofniet",
        vraag="In een goede kunstanalyse kijk je enkel naar wat je ziet, en nooit naar de tijd of de kunstenaar.",
        antwoord=False,
        uitleg="De richtvraag wie, waar en wanneer hoort er net bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kerkraam uit de 13de eeuw toont het leven van Christus in kleine vakjes. Welke functie past het best bij deze inhoud?",
        opties=[
            "een verhalende en religieuze functie, voor gelovigen die niet konden lezen",
            "een ontspannende functie, als vermaak bij het wachten op de mis",
            "een economische functie, om met reclame geld voor de kerk in te zamelen",
            "een functie als zonnewering, om de kerk koel te houden in de zomer",
        ],
        antwoord=0,
        uitleg="Inhoud en functie hangen hier sterk samen met de middeleeuwse context.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij een muziekstuk noteer je: trage maat, lage tonen, mineur. Welke richtvraag beantwoord je?",
        opties=["hoe en waarmee?", "wat?", "waarvoor?", "wie, waar en wanneer?"],
        antwoord=0,
        uitleg="Tempo, toonhoogte en toonsoort zijn bouwstenen van muziek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een affiche uit 1914 toont een soldaat die naar de kijker wijst, met de tekst 'Jouw land heeft je nodig'. Welke functie heeft het werk?",
        opties=[
            "een politieke functie: mensen overtuigen om soldaat te worden",
            "een decoratieve functie: een kamer gezellig maken",
            "een religieuze functie: het geloof uitleggen",
            "een ontspannende functie: de kijker laten lachen",
        ],
        antwoord=0,
        uitleg="Propaganda wil overtuigen. De wijzende vinger spreekt de kijker rechtstreeks aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vraag stel je bij de techniek van een beeld?",
        opties=[
            "is het gehouwen, gegoten, geboetseerd of samengesteld?",
            "wie heeft het werk besteld en waarom?",
            "in welk jaar en in welk land is het gemaakt?",
            "wat stelt het beeld precies voor?",
        ],
        antwoord=0,
        uitleg="Bij beeldhouwkunst kun je wegnemen (houwen), toevoegen (boetseren), gieten of samenvoegen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke factoren beïnvloeden hoe iemand een kunstwerk interpreteert?",
        opties=[
            "tijd en ruimte, en het persoonlijk referentiekader",
            "veranderende kennis en technologie, en modetrends",
            "het merk van de lamp waarmee het museum het werk verlicht",
            "de prijs van het ticket voor het museum",
        ],
        antwoord=[0, 1],
        uitleg="Dat zijn de vier beïnvloedende factoren uit de kunstreflectie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is je persoonlijk referentiekader?",
        opties=[
            "alles wat je meebrengt: je ervaringen, je opvoeding, je kennis en je smaak",
            "de lijst rond een schilderij die je zelf kiest om het thuis op te hangen",
            "de tekst naast het werk in het museum, met de naam en het jaartal",
            "de regels van een museum over wat je wel en niet mag aanraken",
        ],
        antwoord=0,
        uitleg="Twee mensen zien hetzelfde werk, maar door hun referentiekader begrijpen en voelen ze het anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een schilderij dat in 1863 schokkend werd gevonden, wordt vandaag als een meesterwerk bekeken. Welke factor speelt hier vooral?",
        opties=["tijd en ruimte", "modetrends", "het economisch perspectief", "het persoonlijk perspectief"],
        antwoord=0,
        uitleg="Wat in een bepaalde tijd en plaats als schokkend gold, kan later gewoon of zelfs vernieuwend lijken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Met röntgenfoto's ontdekt men dat er onder een schilderij een ouder schilderij zit. Welke factor verandert hier de interpretatie?",
        opties=[
            "veranderende kennis en technologie",
            "modetrends",
            "het persoonlijk referentiekader",
            "tijd en ruimte",
        ],
        antwoord=0,
        uitleg="Nieuwe technieken tonen soms wat de kunstenaar veranderde. Dat zegt iets over zijn werkwijze en bedoeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vergeten kunstenaar wordt plots populair omdat zijn stijl past bij wat vandaag in de mode is. Welke factor zie je?",
        opties=["modetrends", "veranderende technologie", "tijd en ruimte", "het economisch perspectief"],
        antwoord=0,
        uitleg="Smaak verandert. Wat in de mode is, krijgt meer aandacht en waardering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zegt: 'Dit werk maakt me rustig, want het doet me denken aan de zee bij mijn grootouders.' Vanuit welk perspectief spreek je?",
        opties=[
            "het persoonlijk perspectief",
            "het perspectief van de kunstcritici",
            "het economisch perspectief",
            "het perspectief van musea en galerieën",
        ],
        antwoord=0,
        uitleg="Je eigen gevoel en herinneringen zijn een subjectieve ervaring.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke perspectieven horen bij het derde persoonsperspectief, de meer objectieve observatie?",
        opties=[
            "het perspectief van de kunstcritici",
            "het perspectief van het grote publiek",
            "het perspectief van musea en galerieën",
            "je eigen gevoel bij het werk",
        ],
        antwoord=[0, 1, 2],
        uitleg="Je eigen gevoel is het persoonlijk perspectief, niet het derde persoonsperspectief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke invloed hebben musea en galerieën op de betekenis van kunst?",
        opties=[
            "wat ze kiezen om te tonen of aan te kopen, krijgt meer aandacht en waardering",
            "ze hebben geen enkele invloed, want ze tonen gewoon wat er toevallig is",
            "ze bepalen enkel de openingsuren en de prijs van het ticket",
            "ze mogen enkel werken van kunstenaars tonen die al lang dood zijn",
        ],
        antwoord=0,
        uitleg="Een werk in een bekend museum lijkt meteen belangrijker. Musea maken mee wat als kunst geldt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een krant schrijft: 'Het werk is technisch sterk, maar de boodschap blijft oppervlakkig.' Welk perspectief is dat?",
        opties=[
            "het perspectief van de kunstcritici",
            "het economisch perspectief",
            "het perspectief van het grote publiek",
            "het persoonlijk perspectief van de kunstenaar",
        ],
        antwoord=0,
        uitleg="Een criticus analyseert en beoordeelt een werk, vaak met argumenten over vorm en inhoud.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een schilderij wordt op een veiling voor miljoenen verkocht en daarna willen veel verzamelaars werk van dezelfde kunstenaar. Welk perspectief zie je?",
        opties=[
            "het economisch perspectief",
            "het persoonlijk perspectief",
            "het perspectief van de kunstcritici",
            "het perspectief van het grote publiek",
        ],
        antwoord=0,
        uitleg="Het economisch perspectief kijkt naar waarde, verkoop en de invloed op de kunstmarkt.",
    ),
    dict(
        type="invultekst",
        vraag="Het perspectief van je eigen, subjectieve ervaring bij een kunstwerk heet het ... perspectief.",
        antwoord=["persoonlijk", "persoonlijke"],
        uitleg="Daartegenover staat het derde persoonsperspectief, de meer objectieve observatie.",
    ),
    dict(
        type="invultekst",
        vraag="Alles wat je meebrengt als kijker, zoals je ervaringen en je kennis, noem je je persoonlijk ...",
        antwoord=["referentiekader"],
        uitleg="Het referentiekader kleurt hoe je een werk ziet en begrijpt.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee mensen kunnen hetzelfde kunstwerk op een heel verschillende manier interpreteren.",
        antwoord=True,
        uitleg="Hun referentiekader, tijd en kennis verschillen. Daarom is er vaak meer dan één interpretatie.",
    ),
    dict(
        type="waarofniet",
        vraag="De betekenis van een kunstwerk ligt vast voor altijd en verandert nooit door de tijd.",
        antwoord=False,
        uitleg="Nieuwe tijden, nieuwe kennis en andere smaak veranderen hoe we naar een werk kijken.",
    ),
    dict(
        type="waarofniet",
        vraag="De reactie van het grote publiek kan een kunstwerk bekend maken, ook als critici het werk minder goed vinden.",
        antwoord=True,
        uitleg="Het publiek en de critici zijn twee verschillende perspectieven, die niet altijd hetzelfde zeggen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een dure prijs op een veiling bewijst dat een kunstwerk het mooiste werk van zijn tijd is.",
        antwoord=False,
        uitleg="De prijs zegt iets over de markt en de vraag, niet zomaar over de kwaliteit of de schoonheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een werk van Van Gogh werd tijdens zijn leven bijna niet verkocht. Vandaag staan er lange rijen voor zijn werk. Wat toont dit?",
        opties=[
            "de waardering voor kunst verandert met de tijd, door critici, musea en publiek",
            "Van Gogh schilderde zijn werk na zijn dood helemaal opnieuw",
            "de werken van Van Gogh waren vroeger veel kleiner dan nu",
            "kunst die tijdens het leven van de kunstenaar niet verkocht, blijft altijd onbekend",
        ],
        antwoord=0,
        uitleg="Interpretatie en waardering zijn niet vast. Ze worden ook gemaakt door wie over kunst schrijft en wie ze toont.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een sociale-mediabericht over een kunstwerk gaat viraal en duizenden mensen gaan het werk zien. Welk perspectief speelt hier vooral?",
        opties=[
            "het perspectief van het grote publiek",
            "het perspectief van de kunstcritici",
            "het persoonlijk perspectief van één kijker",
            "het perspectief van de opdrachtgever",
        ],
        antwoord=0,
        uitleg="De reactie van veel mensen samen bepaalt hier de aandacht voor het werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig om vanuit meerdere perspectieven over een kunstwerk na te denken?",
        opties=[
            "zo zie je dat de betekenis van een werk niet van één mening afhangt",
            "zo kun je bewijzen dat jouw eigen mening de enige juiste is",
            "zo hoef je zelf niet meer naar het werk te kijken",
            "zo weet je meteen hoeveel het werk op een veiling waard is",
        ],
        antwoord=0,
        uitleg="Door perspectieven te vergelijken, kun je je eigen mening beter onderbouwen en die van anderen begrijpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand die zelf piano speelt, hoort andere dingen in een concert dan iemand die nooit muziek speelde. Welke factor speelt hier?",
        opties=[
            "het persoonlijk referentiekader",
            "veranderende technologie",
            "modetrends",
            "het economisch perspectief",
        ],
        antwoord=0,
        uitleg="Wat je zelf weet en kunt, bepaalt mee wat je opmerkt.",
    ),
]

# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Het periodiek systeem der elementen.

Hoort bij "atoom- en molecuulbouw" van de vakfiche chemie 2de graad
doorstroomfinaliteit, samen met [ch_atoom] en [ch_bindingen].

Deel 1 gaat over de opbouw van het systeem: de groepen en de perioden, de
valentie-elektronen, het aantal bezette schillen en de namen van de
hoofdgroepen. Deel 2 gaat over wat je uit de plaats van een element afleidt:
hoeveel elektronen het opneemt of afgeeft, zijn metaal- of niet-metaalkarakter
en zijn elektronegativiteit.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men een verticale kolom in het periodiek systeem?",
        opties=[
            "een groep",
            "een periode",
            "een schil",
            "een reeks",
        ],
        antwoord=0,
        uitleg="Een groep is een kolom, een periode een rij. Elementen uit dezelfde groep lijken sterk op elkaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hebben elementen uit dezelfde hoofdgroep gemeenschappelijk?",
        opties=[
            "het aantal valentie-elektronen",
            "het aantal bezette schillen",
            "hun massagetal",
            "hun aantal neutronen",
        ],
        antwoord=0,
        uitleg="Het groepsnummer van een hoofdgroep is net het aantal elektronen in de buitenste schil. Daarom reageren ze op dezelfde manier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt het periodenummer van een element?",
        opties=[
            "het aantal bezette schillen",
            "het aantal valentie-elektronen",
            "het aantal neutronen in de kern",
            "de lading van het ion",
        ],
        antwoord=0,
        uitleg="Elke nieuwe periode begint bij een nieuwe schil. Een element uit periode 3 heeft dus drie bezette schillen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men de elementen van groep IA, met uitzondering van waterstof?",
        opties=[
            "de alkalimetalen",
            "de halogenen",
            "de edelgassen",
            "de aardalkalimetalen",
        ],
        antwoord=0,
        uitleg="Lithium, natrium en kalium horen daarbij. Ze hebben één valentie-elektron en reageren daarom heftig met water.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe noemt men de elementen van groep VIIA?",
        opties=[
            "de halogenen",
            "de alkalimetalen",
            "de edelgassen",
            "de aardalkalimetalen",
        ],
        antwoord=0,
        uitleg="Fluor, chloor, broom en jood zijn halogenen. Ze hebben zeven valentie-elektronen en nemen er dus graag één op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke elementen zijn aardalkalimetalen? Kruis alles aan wat juist is.",
        opties=[
            "magnesium",
            "calcium",
            "natrium",
            "chloor",
        ],
        antwoord=[0, 1],
        uitleg="De aardalkalimetalen zijn groep IIA en hebben twee valentie-elektronen. Natrium staat in groep IA en chloor in groep VIIA.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel valentie-elektronen heeft een element uit groep VIA?",
        opties=[
            "zes",
            "twee",
            "vier",
            "acht",
        ],
        antwoord=0,
        uitleg="Bij een hoofdgroep is het groepsnummer in Romeinse cijfers gelijk aan het aantal elektronen in de buitenste schil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Zwavel staat in groep VIA en periode 3. Wat weet je daardoor over het atoom?",
        opties=[
            "het heeft drie bezette schillen en zes valentie-elektronen",
            "het heeft zes bezette schillen en drie valentie-elektronen",
            "het heeft drie protonen en zes neutronen",
            "het heeft zes bindingen en drie schillen",
        ],
        antwoord=0,
        uitleg="De periode geeft het aantal schillen, de groep het aantal valentie-elektronen. De configuratie is dus 2, 8, 6.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar in het periodiek systeem staan de niet-metalen vooral?",
        opties=[
            "rechtsboven",
            "linksonder",
            "in het midden",
            "in de onderste rij",
        ],
        antwoord=0,
        uitleg="De metalen staan links en in het midden, de niet-metalen rechtsboven. Tussen de twee liggen de elementen met een gemengd karakter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de edelgassen zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "ze staan in de laatste groep",
            "hun buitenste schil is volledig gevuld",
            "ze vormen graag ionen",
            "ze zijn allemaal metalen",
        ],
        antwoord=[0, 1],
        uitleg="Omdat hun buitenste schil al vol is, hebben ze niets te winnen bij een binding. Ze vormen dus geen ionen en zijn niet-metalen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een element heeft de elektronenconfiguratie 2, 8, 3. In welke groep en periode staat het?",
        opties=[
            "groep IIIA, periode 3",
            "groep IIA, periode 3",
            "groep IIIA, periode 2",
            "groep VIIIA, periode 3",
        ],
        antwoord=0,
        uitleg="Drie bezette schillen betekent periode 3, en drie valentie-elektronen betekent groep IIIA. Dat is aluminium.",
    ),
    dict(
        type="waarofniet",
        vraag="Het aantal elementen in een periode is in elke periode hetzelfde.",
        antwoord=False,
        uitleg="De eerste periode heeft maar twee elementen, de tweede en de derde acht, en daarna worden ze langer.",
    ),
    dict(
        type="waarofniet",
        vraag="Elementen uit dezelfde groep hebben gelijkaardige chemische eigenschappen.",
        antwoord=True,
        uitleg="Ze hebben hetzelfde aantal valentie-elektronen, en net die elektronen doen mee aan de reacties.",
    ),
    dict(
        type="waarofniet",
        vraag="Het atoomnummer stijgt van links naar rechts in een periode.",
        antwoord=True,
        uitleg="De elementen staan op volgorde van hun atoomnummer, dus van hun aantal protonen.",
    ),
    dict(
        type="waarofniet",
        vraag="Waterstof staat bovenaan in de kolom van de edelgassen.",
        antwoord=False,
        uitleg="Waterstof staat helemaal linksboven, in de kolom van groep IA, maar het is geen alkalimetaal.",
    ),
    dict(
        type="waarofniet",
        vraag="De elementen van groep IIA hebben acht valentie-elektronen.",
        antwoord=False,
        uitleg="Bij de hoofdgroepen geeft het groepsnummer het aantal valentie-elektronen, dus zijn het hier twee. Daarom vormen ze ionen met lading 2+.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een horizontale rij in het periodiek systeem?",
        antwoord=["periode", "een periode", "rij"],
        uitleg="Het periodenummer is gelijk aan het aantal bezette schillen van de atomen in die rij.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de elektronen in de buitenste schil van een atoom?",
        antwoord=["valentie-elektronen", "valentie elektronen", "valentieelektronen"],
        uitleg="Die elektronen doen mee aan de bindingen en bepalen dus hoe het element reageert.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel bezette schillen heeft een element uit periode 4?",
        antwoord=["4", "vier"],
        uitleg="Het periodenummer is precies het aantal bezette schillen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de groep waartoe fluor, chloor, broom en jood horen?",
        antwoord=["halogenen", "de halogenen", "groep VIIA"],
        uitleg="Halogeen betekent zoutvormer. Met een metaal vormen ze een zout, zoals natriumchloride.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Hoeveel elektronen geeft een atoom uit groep IA af om een ion te vormen?",
        opties=[
            "één",
            "twee",
            "zeven",
            "geen",
        ],
        antwoord=0,
        uitleg="Het heeft één valentie-elektron. Door dat af te geven houdt het de configuratie van het edelgas ervoor.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke lading krijgt een ion van een element uit groep IIA?",
        opties=[
            "2+",
            "2−",
            "1+",
            "6−",
        ],
        antwoord=0,
        uitleg="Het geeft zijn twee valentie-elektronen af, dus blijven er twee protonen zonder tegenlading over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke lading krijgt een ion van een element uit groep VIIA?",
        opties=[
            "1−",
            "1+",
            "7+",
            "7−",
        ],
        antwoord=0,
        uitleg="Met zeven valentie-elektronen heeft het er maar één nodig om aan acht te komen. Het neemt er dus één op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom neemt een zuurstofatoom twee elektronen op?",
        opties=[
            "dan heeft het een volle buitenste schil",
            "dan wordt het een metaal",
            "dan is zijn kern stabieler",
            "dan verliest het zijn lading",
        ],
        antwoord=0,
        uitleg="Zuurstof staat in groep VIA en heeft zes valentie-elektronen. Met twee erbij komt het aan acht, de edelgasconfiguratie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke ionen vormen de elementen van groep VIA? Kruis alles aan wat juist is.",
        opties=[
            "O²⁻",
            "S²⁻",
            "Cl¹⁻",
            "Na¹⁺",
        ],
        antwoord=[0, 1],
        uitleg="Zuurstof en zwavel staan in groep VIA en nemen elk twee elektronen op. Chloor staat in VIIA en natrium in IA.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de elektronegativiteit van een element?",
        opties=[
            "hoe sterk het elektronen naar zich toe trekt",
            "hoeveel elektronen het in totaal heeft",
            "hoeveel protonen er in de kern zitten",
            "hoe zwaar één atoom ervan is",
        ],
        antwoord=0,
        uitleg="Een element met een hoge elektronegativiteit trekt de elektronen van een binding naar zich toe. Fluor doet dat het sterkst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verandert de elektronegativiteit van links naar rechts in een periode?",
        opties=[
            "ze stijgt",
            "ze daalt",
            "ze blijft gelijk",
            "ze stijgt eerst en daalt dan",
        ],
        antwoord=0,
        uitleg="Naar rechts komen er protonen bij in de kern terwijl het aantal schillen gelijk blijft. De kern trekt de elektronen dus sterker aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke elementen hebben een hoge elektronegativiteit? Kruis alles aan wat juist is.",
        opties=[
            "fluor",
            "zuurstof",
            "natrium",
            "calcium",
        ],
        antwoord=[0, 1],
        uitleg="Fluor en zuurstof staan rechtsboven, de hoek met de hoogste waarden. Natrium en calcium zijn metalen en geven hun elektronen juist af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband tussen de elektronegativiteit en het metaalkarakter van een element?",
        opties=[
            "een lage elektronegativiteit hoort bij een metaal",
            "een hoge elektronegativiteit hoort bij een metaal",
            "er is geen verband tussen die twee",
            "alleen edelgassen hebben een metaalkarakter",
        ],
        antwoord=0,
        uitleg="Een metaal houdt zijn valentie-elektronen maar los vast en geeft ze liever af. Dat is precies een lage elektronegativiteit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een atoom links in het periodiek systeem zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het geeft makkelijk elektronen af",
            "het heeft een metaalkarakter",
            "het heeft een hoge elektronegativiteit",
            "het vormt een negatief ion",
        ],
        antwoord=[0, 1],
        uitleg="Links staan de metalen: lage elektronegativiteit, elektronen afgeven, en dus een positief ion vormen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een ion heeft tien elektronen en een lading van 1+. In welke groep staat het element?",
        opties=[
            "groep IA",
            "groep IIA",
            "groep VIA",
            "groep VIIA",
        ],
        antwoord=0,
        uitleg="Met lading 1+ heeft het één elektron afgegeven, dus had het atoom elf elektronen. Dat is natrium, groep IA.",
    ),
    dict(
        type="waarofniet",
        vraag="Een metaal vormt bij een reactie een positief ion.",
        antwoord=True,
        uitleg="Een metaal geeft zijn valentie-elektronen af. Er blijven dan meer protonen dan elektronen over.",
    ),
    dict(
        type="waarofniet",
        vraag="De elektronegativiteit stijgt als je in een groep naar onder gaat.",
        antwoord=False,
        uitleg="Ze daalt juist: de buitenste schil komt verder van de kern te liggen, dus wordt de aantrekking zwakker.",
    ),
    dict(
        type="waarofniet",
        vraag="Een niet-metaal geeft bij een reactie eerder elektronen af.",
        antwoord=False,
        uitleg="Een niet-metaal heeft veel valentie-elektronen en een hoge elektronegativiteit, dus vult het zijn schil liever aan door er op te nemen.",
    ),
    dict(
        type="waarofniet",
        vraag="Edelgassen vormen gemakkelijk ionen.",
        antwoord=False,
        uitleg="Hun buitenste schil is al vol, dus hebben ze er niets bij te winnen. Ze blijven bijna altijd neutrale atomen.",
    ),
    dict(
        type="waarofniet",
        vraag="Het ion Na¹⁺ heeft dezelfde elektronenconfiguratie als neon.",
        antwoord=True,
        uitleg="Natrium heeft 2, 8, 1 en geeft het laatste elektron af. Er blijft 2, 8 over, dus de configuratie van neon.",
    ),
    dict(
        type="invultekst",
        vraag="Hoeveel elektronen neemt een atoom uit groep VA op om een ion te vormen?",
        antwoord=["3", "drie"],
        uitleg="Met vijf valentie-elektronen heeft het er drie nodig om aan acht te komen. Het ion heeft dus lading 3−.",
    ),
    dict(
        type="invultekst",
        vraag="Welke lading heeft het ion van aluminium, dat in groep IIIA staat?",
        antwoord=["3+", "+3", "3 plus"],
        uitleg="Aluminium geeft zijn drie valentie-elektronen af en wordt dus Al³⁺.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de eigenschap die zegt hoe sterk een atoom de elektronen van een binding naar zich toe trekt?",
        antwoord=["elektronegativiteit", "de elektronegativiteit"],
        uitleg="Het verschil in elektronegativiteit tussen twee atomen bepaalt welk soort binding er ontstaat.",
    ),
    dict(
        type="invultekst",
        vraag="In welke hoek van het periodiek systeem staan de elementen met de hoogste elektronegativiteit?",
        antwoord=["rechtsboven", "rechts boven", "bovenaan rechts"],
        uitleg="Naar rechts stijgt de waarde en naar boven ook, dus ligt het hoogste punt rechtsboven. Fluor staat daar.",
    ),
]

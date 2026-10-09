# -*- coding: utf-8 -*-
"""Welzijn op het werk en waar je met vragen terechtkan.

Het derde thema uit "ik ga werken". Twee stukken van de fiche komen hier
samen: de maatregelen voor welzijn en veiligheid op het werk, en de instanties
en organisaties waar een werknemer of een student terechtkan.

De zes die de fiche noemt, met waarvoor je er bent:

    CPBW           Comité voor Preventie en Bescherming op het Werk: het
                   overlegorgaan in het bedrijf zelf over veiligheid en welzijn
    RSZ            Rijksdienst voor Sociale Zekerheid: de bijdragen
    RVA            Rijksdienst voor Arbeidsvoorziening: werkloosheid en
                   loopbaanonderbreking
    student@work   waar een student zijn gewerkte uren opvolgt
    vakbonden      verdedigen de belangen van werknemers en geven advies
    VDAB           Vlaamse Dienst voor Arbeidsbemiddeling en Beroepsopleiding:
                   werk zoeken en opleiding volgen

Die afkortingen uit elkaar houden is het halve werk van dit thema. RVA en VDAB
worden het vaakst verward: de RVA betaalt de uitkering, de VDAB helpt je aan
werk en aan een opleiding.

Deel 1 is welzijn en veiligheid op het werk.
Deel 2 is de zes instanties en organisaties.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wie is er verantwoordelijk voor een veilige werkplek?",
        opties=[
            "de werkgever, en de werknemer werkt veilig mee",
            "enkel de werknemer zelf",
            "enkel de overheid",
            "enkel de verzekeraar van het bedrijf",
        ],
        antwoord=0,
        uitleg="De werkgever moet voor de veiligheid zorgen, maar de werknemer moet de regels ook volgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is preventie op het werk?",
        opties=[
            "maatregelen nemen voordat er iets misgaat",
            "een ongeval melden bij de verzekering",
            "een gewonde collega verzorgen",
            "een ongeval onderzoeken achteraf",
        ],
        antwoord=0,
        uitleg="Preventie komt vooraf. Daarom heet het comité voor preventie zo.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn persoonlijke beschermingsmiddelen?",
        opties=[
            "spullen die je zelf draagt, zoals een helm of handschoenen",
            "de verzekering die je werkgever voor zijn personeel afsluit",
            "de regels over veiligheid in het arbeidsreglement",
            "de premies die je krijgt voor gevaarlijk werk",
        ],
        antwoord=0,
        uitleg="Ze beschermen jou persoonlijk, naast de maatregelen aan de machines zelf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staan er pictogrammen op een werkplek?",
        opties=[
            "ze waarschuwen in één oogopslag voor gevaar of een verplichting",
            "ze tonen wie op die afdeling de leiding heeft bij problemen",
            "ze vervangen het arbeidsreglement dat aan de muur hangt",
            "ze geven het uurrooster van de ploegen op die werkplek weer",
        ],
        antwoord=0,
        uitleg="Ze werken ook voor wie de taal niet vlot leest, en dat is net de bedoeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij welzijn op het werk, naast de lichamelijke veiligheid?",
        opties=[
            "de werkdruk en de sfeer in de ploeg",
            "de hoogte van het loon",
            "het aantal vakantiedagen",
            "de duur van het contract",
        ],
        antwoord=0,
        uitleg="Welzijn is breder dan ongevallen vermijden: ook stress en pesten op het werk horen erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een machine heeft een losse kap en iemand kan erbij. Wat doe je?",
        opties=[
            "je meldt het meteen en gebruikt de machine niet",
            "je gebruikt ze voorzichtig verder",
            "je wacht tot iemand anders het meldt",
            "je repareert ze zelf met wat je vindt",
        ],
        antwoord=0,
        uitleg="Melden is een plicht van de werknemer, herstellen een zaak voor wie het mag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staat de afkorting CPBW?",
        opties=[
            "Comité voor Preventie en Bescherming op het Werk",
            "Centrale Post voor Beroepsziekten en Werkongevallen",
            "Commissie voor Personeel, Begeleiding en Werk",
            "Controledienst voor Preventie en Bedrijfswelzijn",
        ],
        antwoord=0,
        uitleg="Het is het overlegorgaan binnen het bedrijf zelf, met werkgevers en werknemers samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient het CPBW?",
        opties=[
            "overleggen over veiligheid en welzijn in het bedrijf",
            "de lonen onderhandelen",
            "de werkloosheidsuitkering uitbetalen",
            "de vacatures in het bedrijf invullen",
        ],
        antwoord=0,
        uitleg="Preventie en bescherming op het werk, zoals de naam zegt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een werknemer wil melden dat de nooduitgang versperd staat. Waar kan hij in het bedrijf terecht?",
        opties=["bij het CPBW", "bij de RVA", "bij student@work", "bij de VDAB"],
        antwoord=0,
        uitleg="Het CPBW is het orgaan binnen het bedrijf voor precies dit soort meldingen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een werknemer valt op het werk en breekt zijn pols. Welk type uitkering komt in beeld?",
        opties=[
            "de arbeidsongevallenuitkering",
            "de werkloosheidsuitkering",
            "de uitkering beroepsziekte",
            "het jaarlijks vakantiegeld",
        ],
        antwoord=0,
        uitleg="Een ongeval tijdens het werk valt onder de arbeidsongevallen.",
    ),
    dict(
        type="waarofniet",
        vraag="Welzijn op het werk gaat enkel over het vermijden van ongevallen.",
        antwoord=False,
        uitleg="Ook werkdruk, sfeer en pesten op het werk horen bij welzijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Het CPBW is een overlegorgaan binnen het bedrijf zelf.",
        antwoord=True,
        uitleg="Werkgevers en werknemers zitten er samen rond de tafel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een werknemer die een gevaar opmerkt, hoeft dat niet te melden.",
        antwoord=False,
        uitleg="Veilig werken en gevaren melden hoort bij de plichten van de werknemer.",
    ),
    dict(
        type="waarofniet",
        vraag="Persoonlijke beschermingsmiddelen komen bovenop de veiligheid aan de machines zelf.",
        antwoord=True,
        uitleg="Eerst de machine veilig maken, dan pas de helm. Een helm maakt een onveilige machine niet veilig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij de maatregelen voor welzijn en veiligheid op het werk?",
        opties=[
            "persoonlijke beschermingsmiddelen",
            "pictogrammen en duidelijke waarschuwingen",
            "een overleg over preventie in het bedrijf",
            "een hoger loon voor gevaarlijk werk",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een toeslag maakt het werk niet veiliger. De fiche gaat over maatregelen, niet over vergoedingen.",
    ),
    dict(
        type="invultekst",
        vraag="Welk overlegorgaan in een bedrijf gaat over preventie en bescherming op het werk? Antwoord met de afkorting.",
        antwoord=["CPBW", "cpbw"],
        uitleg="Comité voor Preventie en Bescherming op het Werk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je maatregelen nemen voordat er iets misgaat? Antwoord met één woord.",
        antwoord=["preventie", "de preventie"],
        uitleg="Het eerste woord in de naam van het CPBW.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat veiligheid op het werk ook in het arbeidsreglement?",
        opties=[
            "omdat de regels voor iedereen in het bedrijf gelden",
            "omdat elke werknemer er zijn eigen afspraken over maakt",
            "omdat het anders niet verzekerd is",
            "omdat de wet het in de overeenkomst verbiedt",
        ],
        antwoord=0,
        uitleg="Wat voor iedereen geldt, staat in het reglement en niet in de persoonlijke overeenkomst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een nieuwe werknemer krijgt op zijn eerste dag uitleg over de nooduitgangen en de machines. Wat is dat?",
        opties=[
            "een preventiemaatregel",
            "een schorsing van de overeenkomst",
            "een bepaling uit zijn loonfiche",
            "een taak van de RVA",
        ],
        antwoord=0,
        uitleg="Onthaal en vorming horen bij het voorkomen van ongevallen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie moet volgens de wet de persoonlijke beschermingsmiddelen voorzien?",
        opties=[
            "de werkgever",
            "de werknemer zelf",
            "de vakbond",
            "de verzekeraar",
        ],
        antwoord=0,
        uitleg="De werkgever voorziet ze, de werknemer moet ze gebruiken.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarvoor staat de afkorting RVA?",
        opties=[
            "Rijksdienst voor Arbeidsvoorziening",
            "Raad voor Arbeid en Arbeidsrecht",
            "Rijksdienst voor Algemene Arbeidszaken",
            "Regeling voor Arbeidsvoorwaarden",
        ],
        antwoord=0,
        uitleg="De RVA gaat onder meer over werkloosheid en loopbaanonderbreking.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staat de afkorting VDAB?",
        opties=[
            "Vlaamse Dienst voor Arbeidsbemiddeling en Beroepsopleiding",
            "Vlaamse Diensten voor Arbeid en Bedrijven",
            "Vereniging van Dienstverleners en Arbeidsbureaus",
            "Vlaamse Databank voor Arbeid en Beroepen",
        ],
        antwoord=0,
        uitleg="Bemiddeling en opleiding: de VDAB helpt je aan werk en aan een cursus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je bent je werk kwijt en zoekt een nieuwe job en een opleiding. Waar ga je naartoe?",
        opties=["de VDAB", "de RVA", "het CPBW", "student@work"],
        antwoord=0,
        uitleg="De VDAB bemiddelt en leidt op. De RVA betaalt de uitkering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hebt een vraag over je werkloosheidsuitkering. Waar hoort die thuis?",
        opties=["bij de RVA", "bij de VDAB", "bij de RSZ", "bij het CPBW"],
        antwoord=0,
        uitleg="De RVA gaat over de uitkering zelf, de VDAB over het zoeken naar werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient student@work?",
        opties=[
            "je gewerkte uren als student opvolgen",
            "een studentenjob zoeken",
            "je loon als student laten uitbetalen",
            "je studiebeurs aanvragen",
        ],
        antwoord=0,
        uitleg="Het is de plek waar je ziet hoeveel uren je al gewerkt hebt en hoeveel je nog hebt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een student wil weten hoeveel uren hij dit jaar nog kan werken. Waar kijkt hij?",
        opties=["op student@work", "bij de RVA", "bij de RSZ", "bij het CPBW"],
        antwoord=0,
        uitleg="Dat is precies waarvoor student@work bestaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient de RSZ?",
        opties=[
            "de bijdragen voor de sociale zekerheid innen en beheren",
            "werklozen aan een job helpen",
            "de veiligheid in bedrijven controleren",
            "de lonen van alle sectoren vastleggen",
        ],
        antwoord=0,
        uitleg="De Rijksdienst voor Sociale Zekerheid. Ze int de bijdragen van werkgevers en werknemers.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor kan je bij een vakbond terecht?",
        opties=[
            "advies en verdediging van je belangen als werknemer",
            "het uitbetalen van je loon",
            "het innen van de sociale bijdragen",
            "het goedkeuren van je arbeidsovereenkomst",
        ],
        antwoord=0,
        uitleg="Vakbonden staan in het rijtje van de fiche naast de officiële instanties.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je denkt dat je werkgever je overloon niet correct betaalt. Bij wie kan je eerst advies vragen?",
        opties=["bij een vakbond", "bij de RSZ", "bij student@work", "bij de VDAB"],
        antwoord=0,
        uitleg="Een vakbond geeft advies en kan je verdedigen als het op een geschil uitdraait.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel instanties en organisaties noemt de fiche waar een werknemer of student terechtkan?",
        opties=["zes", "vier", "vijf", "zeven"],
        antwoord=0,
        uitleg="CPBW, RSZ, RVA, student@work, vakbonden en VDAB.",
    ),
    dict(
        type="waarofniet",
        vraag="De RVA betaalt de werkloosheidsuitkering en de VDAB helpt je aan werk.",
        antwoord=True,
        uitleg="Dat is het verschil dat het vaakst verward wordt.",
    ),
    dict(
        type="waarofniet",
        vraag="De RSZ helpt werklozen aan een nieuwe job.",
        antwoord=False,
        uitleg="De RSZ int de bijdragen. Werk zoeken is de VDAB.",
    ),
    dict(
        type="waarofniet",
        vraag="Een vakbond staat in de fiche bij de organisaties waar een werknemer terechtkan.",
        antwoord=True,
        uitleg="Ze staan er naast het CPBW, de RSZ, de RVA, student@work en de VDAB.",
    ),
    dict(
        type="waarofniet",
        vraag="Student@work is een website om een studentenjob te zoeken.",
        antwoord=False,
        uitleg="Het is de plek waar je je gewerkte uren als student opvolgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke instanties noemt de fiche?",
        opties=["de RVA", "de VDAB", "de RSZ", "de FOD Financiën"],
        antwoord=[0, 1, 2],
        uitleg="De FOD Financiën staat niet in dit rijtje. Het CPBW, student@work en de vakbonden wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor kan je bij de VDAB terecht?",
        opties=[
            "werk zoeken",
            "een beroepsopleiding volgen",
            "begeleiding bij je loopbaan",
            "je werkloosheidsuitkering ontvangen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De uitkering komt van de RVA, niet van de VDAB.",
    ),
    dict(
        type="invultekst",
        vraag="Welke dienst helpt je in Vlaanderen aan werk en aan een opleiding? Antwoord met de afkorting.",
        antwoord=["VDAB", "vdab"],
        uitleg="Vlaamse Dienst voor Arbeidsbemiddeling en Beroepsopleiding.",
    ),
    dict(
        type="invultekst",
        vraag="Welke rijksdienst gaat over de werkloosheidsuitkering? Antwoord met de afkorting.",
        antwoord=["RVA", "rva"],
        uitleg="Rijksdienst voor Arbeidsvoorziening.",
    ),
    dict(
        type="invultekst",
        vraag="Op welke website volgt een student zijn gewerkte uren op?",
        antwoord=["student@work", "studentatwork"],
        uitleg="Ze staat in het rijtje van zes instanties en organisaties.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een werknemer twijfelt of zijn werkgever wel bijdragen voor hem betaalt. Welke dienst gaat daarover?",
        opties=["de RSZ", "de RVA", "de VDAB", "het CPBW"],
        antwoord=0,
        uitleg="De RSZ int de bijdragen van werkgevers en werknemers.",
    ),
]

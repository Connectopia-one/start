# -*- coding: utf-8 -*-
"""Mediatheorieën, beeldvorming en persvrijheid.

Het laatste van vijf thema's over sociale wetenschappen. Het vorige thema
vroeg wat media doen; dit thema vraagt hoeveel invloed ze hebben, hoe ze een
beeld van de werkelijkheid maken, en waar hun vrijheid stopt.

De lijstjes staan letterlijk in de fiche:

    theorieën over de invloed en de macht van de massamedia
        de injectienaaldtheorie
        de functionalistische mediatheorie: Lasswell, Lazarsfeld,
            Merton en Wright
        de agendasettingtheorie: McCombs en Shaw
        de cultivatietheorie: Gerbner
        de mediatiseringstheorie: Stig Hjarvard
    mechanismen bij beeldvorming: framing, priming, het selectieproces en de
        selectiecriteria, stereotypering en sociale categorisering
    verder: vrijheid van meningsuiting, persvrijheid, hun beperkingen, waarom
        ze in een democratie thuishoren, en de verschillen daarin in de wereld

De vijf theorieën staan in de fiche in een logische orde: van een publiek dat
alles slikt (de injectienaald) naar een publiek dat zelf kiest (de
functionalistische theorie), en dan drie theorieën die elk een eigen soort
invloed aanwijzen: het onderwerp (agendasetting), het wereldbeeld
(cultivatie) en de hele samenleving (mediatisering).

Deel 1 zijn de vijf mediatheorieën.
Deel 2 zijn de mechanismen van beeldvorming, de persvrijheid en de privacy.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat zegt de injectienaaldtheorie over de invloed van media?",
        opties=[
            "media spuiten een boodschap in een publiek dat ze overneemt",
            "media hebben nauwelijks enige invloed op hun publiek",
            "media bepalen waarover mensen praten, niet wat ze denken",
            "media veranderen het wereldbeeld van zware kijkers",
        ],
        antwoord=0,
        uitleg="De oudste van de vijf theorieën. Ze gaat uit van een passief publiek, en wordt vandaag als veel te simpel beschouwd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wordt de injectienaaldtheorie vandaag als te simpel gezien?",
        opties=[
            "omdat een publiek zelf kiest en niet alles overneemt",
            "omdat media helemaal geen invloed hebben",
            "omdat ze alleen voor kranten geldt en niet voor televisie",
            "omdat ze alleen voor kinderen geldt en niet voor ouderen",
        ],
        antwoord=0,
        uitleg="Mensen kiezen wat zij bekijken, praten erover met anderen en lezen een boodschap vanuit hun eigen referentiekader.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke namen zet de fiche bij de functionalistische mediatheorie?",
        opties=[
            "Lasswell",
            "Lazarsfeld",
            "Merton en Wright",
            "McCombs en Shaw",
            "Stig Hjarvard",
        ],
        antwoord=[0, 1, 2],
        uitleg="Lasswell, Lazarsfeld, en Merton en Wright. McCombs en Shaw staan bij agendasetting, Hjarvard bij de mediatisering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de kern van de functionalistische mediatheorie?",
        opties=[
            "media vervullen functies die het publiek zelf opzoekt",
            "media spuiten een boodschap in een passief publiek",
            "media bepalen alleen waarover mensen nadenken",
            "media worden zelf een instituut in de samenleving",
        ],
        antwoord=0,
        uitleg="Het publiek is hier geen slachtoffer maar een gebruiker: mensen zoeken media op voor informatie, vermaak of gezelschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie staan in de fiche bij de agendasettingtheorie?",
        opties=[
            "McCombs en Shaw",
            "Gerbner",
            "Stig Hjarvard",
            "Lasswell en Lazarsfeld",
        ],
        antwoord=0,
        uitleg="McCombs en Shaw. Hun stelling is dat media bepalen waarover een samenleving nadenkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de agendasettingtheorie precies?",
        opties=[
            "media bepalen niet wat je denkt maar waarover je denkt",
            "media bepalen niet waarover je denkt maar wat je denkt",
            "media bepalen zowel wat als waarover je denkt",
            "media bepalen noch wat noch waarover je denkt",
        ],
        antwoord=0,
        uitleg="Dat is de klassieke formulering. Wat vier dagen op het nieuws staat, staat de hele week op de agenda van het land.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de cultivatietheorie?",
        opties=[
            "Gerbner",
            "McCombs",
            "Lazarsfeld",
            "Stig Hjarvard",
        ],
        antwoord=0,
        uitleg="Gerbner. Zijn theorie gaat over de lange termijn: wie veel kijkt, gaat de wereld zien zoals ze op het scherm verschijnt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de cultivatietheorie?",
        opties=[
            "veel kijken schuift je wereldbeeld naar het beeld op het scherm",
            "veel kijken verandert je mening over één onderwerp",
            "veel kijken heeft op lange termijn geen gevolgen",
            "veel kijken maakt mensen vooral socialer",
        ],
        antwoord=0,
        uitleg="Cultiveren is kweken. De invloed komt niet van één uitzending maar van jaren hetzelfde soort beelden zien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand kijkt elke avond naar misdaadreeksen en denkt dat haar buurt veel onveiliger is dan de cijfers aangeven. Welke theorie legt dat uit?",
        opties=[
            "de cultivatietheorie",
            "de agendasettingtheorie",
            "de injectienaaldtheorie",
            "de functionalistische mediatheorie",
        ],
        antwoord=0,
        uitleg="Jaren misdaadbeelden kweken een wereldbeeld dat onveiliger is dan de werkelijkheid. Dat is precies wat Gerbner onderzocht.",
    ),
    dict(
        type="invultekst",
        vraag="De theorie die zegt dat media bepalen waarover een samenleving nadenkt, heet de ...theorie.",
        antwoord=["agendasetting", "agendasettingtheorie"],
        uitleg="De agendasettingtheorie van McCombs en Shaw.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de mediatiseringstheorie?",
        opties=[
            "Stig Hjarvard",
            "George Gerbner",
            "Maxwell McCombs",
            "Paul Lazarsfeld",
        ],
        antwoord=0,
        uitleg="Stig Hjarvard. Bij hem worden de media zelf een instituut waar andere delen van de samenleving zich naar schikken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de mediatiseringstheorie van Hjarvard?",
        opties=[
            "andere maatschappelijke velden schikken zich naar de media",
            "de media schikken zich naar de andere velden",
            "de media hebben op de samenleving geen invloed",
            "de media beïnvloeden alleen zware kijkers",
        ],
        antwoord=0,
        uitleg="Politiek, sport en zelfs kerk en school passen hun werk aan wat in de media werkt. De media worden zo een logica op zich.",
    ),
    dict(
        type="waarofniet",
        vraag="De agendasettingtheorie en de cultivatietheorie wijzen een verschillend soort invloed aan.",
        antwoord=True,
        uitleg="Waar. Agendasetting gaat over welk onderwerp aan bod komt, cultivatie over het wereldbeeld op lange termijn.",
    ),
    dict(
        type="waarofniet",
        vraag="De functionalistische mediatheorie gaat van een passief publiek uit.",
        antwoord=False,
        uitleg="Niet waar. Juist niet: het publiek zoekt zelf op wat het nodig heeft. De injectienaaldtheorie gaat wel van een passief publiek uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een partij laat haar congres beginnen om twintig uur, zodat het in het journaal van acht past. Welke theorie past hier het best bij?",
        opties=[
            "de mediatiseringstheorie",
            "de injectienaaldtheorie",
            "de cultivatietheorie",
            "de functionalistische mediatheorie",
        ],
        antwoord=0,
        uitleg="De politiek schikt haar eigen werking naar de logica van de media. Dat is de mediatiseringstheorie van Hjarvard.",
    ),
    dict(
        type="meerkeuze",
        vraag="Vier dagen nieuws over één onderwerp maakt dat iedereen het er plots over heeft. Welke theorie past hier het best bij?",
        opties=[
            "de agendasettingtheorie",
            "de cultivatietheorie",
            "de mediatiseringstheorie",
            "de injectienaaldtheorie",
        ],
        antwoord=0,
        uitleg="Niet de mening maar het gespreksonderwerp verschuift. Dat is agendasetting.",
    ),
    dict(
        type="invultekst",
        vraag="De oudste mediatheorie, die een boodschap in een passief publiek spuit, heet de ...theorie.",
        antwoord=["injectienaald", "injectienaaldtheorie"],
        uitleg="De injectienaaldtheorie. Ze heet zo omdat de boodschap als een spuit in het publiek gaat.",
    ),
    dict(
        type="waarofniet",
        vraag="De vijf mediatheorieën van de fiche spreken elkaar niet volledig tegen: ze meten elk een ander soort invloed.",
        antwoord=True,
        uitleg="Waar. Een onderwerp op de agenda zetten, een wereldbeeld kweken en een samenleving doen schikken zijn drie verschillende dingen.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens de cultivatietheorie komt de invloed van media vooral van één sterke uitzending.",
        antwoord=False,
        uitleg="Niet waar. De cultivatietheorie kijkt juist naar de lange termijn: het gaat om jaren van dezelfde soort beelden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke twee theorieën gaan ervan uit dat het publiek zelf iets met de boodschap doet?",
        opties=[
            "de functionalistische mediatheorie",
            "de agendasettingtheorie",
            "de injectienaaldtheorie",
            "geen van de vijf",
        ],
        antwoord=[0, 1],
        uitleg="Bij de functionalistische theorie kiest het publiek zelf, en bij agendasetting bepaalt het nog altijd zelf wat het van een onderwerp vindt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is framing?",
        opties=[
            "een gebeurtenis in een bepaald kader zetten",
            "een gebeurtenis als eerste naar buiten brengen",
            "een gebeurtenis in een eerdere prikkel laten meespelen",
            "een gebeurtenis helemaal niet berichten",
        ],
        antwoord=0,
        uitleg="Frame betekent kader. Dezelfde betoging kan een opstand of een protest heten, en dat kader bepaalt mee hoe je ze leest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is priming?",
        opties=[
            "een eerdere prikkel die beïnvloedt hoe je iets daarna leest",
            "een gebeurtenis in een bepaald kader zetten",
            "een gebeurtenis weglaten uit het nieuws",
            "een groep in een vast beeld duwen",
        ],
        antwoord=0,
        uitleg="Wat je net gezien hebt, staat klaar in je hoofd. Een item over inbraken vlak voor een item over een wijk kleurt het tweede item mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het selectieproces in de media?",
        opties=[
            "het kiezen van wat wel en niet in het nieuws komt",
            "het kiezen van de kijkers waarop je mikt",
            "het kiezen van een kader voor een bericht",
            "het kiezen van een woord voor een groep",
        ],
        antwoord=0,
        uitleg="Er is altijd veel meer gebeurd dan er in een uitzending past. Wat overblijft, is gekozen volgens selectiecriteria.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zaken maken dat een gebeurtenis sneller in het nieuws komt?",
        opties=[
            "ze is dichtbij gebeurd",
            "ze is uitzonderlijk",
            "er is een bekende persoon bij betrokken",
            "ze lijkt op het nieuws van vorige maand",
        ],
        antwoord=[0, 1, 2],
        uitleg="Nabijheid, uitzonderlijkheid, bekende namen en conflict zijn klassieke selectiecriteria. Iets gewoons haalt het nieuws niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is stereotypering?",
        opties=[
            "een hele groep in hetzelfde vaste beeld duwen",
            "een gebeurtenis in een bepaald kader zetten",
            "een bericht als eerste naar buiten brengen",
            "een onderwerp op de agenda zetten",
        ],
        antwoord=0,
        uitleg="Een stereotype is een vast beeld van een hele groep, dat geen plaats laat voor de verschillen binnen die groep.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is sociale categorisering?",
        opties=[
            "mensen in groepen indelen om de wereld te ordenen",
            "mensen in het nieuws brengen met naam en foto",
            "mensen uit het nieuws weglaten",
            "mensen een eigen stem geven in de media",
        ],
        antwoord=0,
        uitleg="Indelen doen wij allemaal, het is hoe ons hoofd de wereld ordent. Het wordt een probleem als er een vast en negatief beeld aan hangt.",
    ),
    dict(
        type="invultekst",
        vraag="Een gebeurtenis in een bepaald kader zetten, zodat ze op een bepaalde manier gelezen wordt, heet ...",
        antwoord=["framing", "framen"],
        uitleg="Framing. Priming is iets anders: dat is een eerdere prikkel die doorwerkt.",
    ),
    dict(
        type="waarofniet",
        vraag="Framing kan ook gebeuren zonder dat een journalist het bewust doet.",
        antwoord=True,
        uitleg="Waar. Elke keuze van een woord, een foto of een bron zet een kader, of je het bedoelt of niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een selectieproces kan vermeden worden door simpelweg alles te berichten.",
        antwoord=False,
        uitleg="Niet waar. Alles berichten kan niet: er is meer gebeurd dan er tijd of plaats is. Daarom zijn de criteria zo belangrijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee kranten brengen dezelfde betoging, de ene met de titel protest en de andere met de titel rellen. Welk mechanisme is dit?",
        opties=[
            "framing",
            "priming",
            "stereotypering",
            "agendasetting",
        ],
        antwoord=0,
        uitleg="Dezelfde feiten, een ander kader. Dat is framing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een reportage over één bende wekt bij de kijker de indruk dat iedereen uit die wijk zo is. Welk mechanisme is dit?",
        opties=[
            "stereotypering",
            "priming",
            "framing",
            "cultivatie",
        ],
        antwoord=0,
        uitleg="Een vast beeld van een hele groep op basis van enkelen. Dat is stereotypering, vaak samen met sociale categorisering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is vrijheid van meningsuiting?",
        opties=[
            "het recht je mening te zeggen zonder straf vooraf",
            "het recht om alles te zeggen zonder enige grens",
            "het recht om alleen in de media te spreken",
            "het recht om van mening te veranderen",
        ],
        antwoord=0,
        uitleg="Het is een grondrecht: je mag je mening uiten en er is geen toelating vooraf nodig. Dat betekent niet dat er geen grenzen zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is persvrijheid?",
        opties=[
            "het recht van media om te berichten zonder censuur",
            "het recht van media om alles gratis te publiceren",
            "het recht van burgers om een krant te starten",
            "het recht van de overheid om nieuws te keuren",
        ],
        antwoord=0,
        uitleg="Persvrijheid betekent dat de overheid het nieuws niet mag keuren of tegenhouden. Zonder haar kan er geen waakhondfunctie bestaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zaken zijn beperkingen op de vrijheid van meningsuiting?",
        opties=[
            "aanzetten tot haat of geweld",
            "laster en eerroof",
            "het privéleven van iemand schenden",
            "een politicus scherp bekritiseren",
        ],
        antwoord=[0, 1, 2],
        uitleg="Haatspraak, laster en de schending van privacy zijn echte grenzen. Scherpe kritiek op een politicus is juist wat het recht beschermt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom horen vrijheid van meningsuiting en persvrijheid in een democratie thuis?",
        opties=[
            "omdat kiezers alleen kunnen kiezen met vrije informatie",
            "omdat de overheid dan geen verantwoording hoeft af te leggen",
            "omdat media zo meer kijkers kunnen halen",
            "omdat alle meningen dan even juist worden",
        ],
        antwoord=0,
        uitleg="Zonder vrije informatie en vrij debat kan een kiezer zijn keuze niet maken, en kan niemand de macht ter verantwoording roepen.",
    ),
    dict(
        type="invultekst",
        vraag="Het keuren of tegenhouden van berichten door een overheid heet ...",
        antwoord=["censuur"],
        uitleg="Censuur. Persvrijheid betekent juist dat er geen censuur vooraf is.",
    ),
    dict(
        type="waarofniet",
        vraag="De vrijheid van meningsuiting en de persvrijheid zijn in de wereld niet overal even groot.",
        antwoord=True,
        uitleg="Waar. De fiche vraagt uitdrukkelijk uit te leggen dat er verschillen in de wereld zijn. In sommige landen riskeert een journalist de gevangenis.",
    ),
    dict(
        type="waarofniet",
        vraag="Persvrijheid betekent dat een journalist niets meer hoeft na te trekken voor hij iets publiceert.",
        antwoord=False,
        uitleg="Niet waar. Geen censuur vooraf betekent niet geen verantwoordelijkheid achteraf. Feiten nagaan blijft de plicht van een journalist.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een krant wil de naam van een verdachte publiceren. Welk spanningsveld speelt hier?",
        opties=[
            "persvrijheid tegenover het recht op privacy",
            "persvrijheid tegenover de agendasetting",
            "privacy tegenover de cultuuroverdracht",
            "censuur tegenover de waakhondfunctie",
        ],
        antwoord=0,
        uitleg="De fiche vraagt dat spanningsveld uitdrukkelijk: persvrijheid en vrije meningsuiting aan de ene kant, privacy aan de andere.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom weegt het recht op privacy bij een verdachte zwaarder dan bij een minister in functie?",
        opties=[
            "omdat een minister publieke verantwoordelijkheid draagt",
            "omdat een verdachte geen enkel recht meer heeft",
            "omdat een minister geen privéleven heeft",
            "omdat een verdachte altijd schuldig is",
        ],
        antwoord=0,
        uitleg="Wie macht uitoefent, moet daarover verantwoording afleggen. Een burger die nog niets bewezen is, verdient bescherming.",
    ),
]

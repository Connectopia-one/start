# -*- coding: utf-8 -*-
"""De vragen voor "Feiten, meningen en betrouwbaarheid" (✨ Spark, Nederlands).

Uit de vakfiche: beoordelen of een tekst betrouwbaar, correct en bruikbaar is
aan de hand van criteria (auteur, uitgever, kanaal, bedoeling van de zender,
bronnen, feiten of meningen, hoe recent), het onderscheid tussen feiten en
meningen, het standpunt bepalen en zelf argumenten geven, en je bewust zijn van
stereotypering.

Deel 1 oefent feit tegenover mening en de criteria één voor één. Deel 2 past ze
samen toe op nepnieuws, clickbait, reclame en standpunten met argumenten.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke zin is een feit?",
        opties=[
            "België telt drie officiële landstalen.",
            "Nederlands is de mooiste taal.",
            "Iedereen zou Frans moeten leren.",
            "Dialect klinkt gezellig.",
        ],
        antwoord=0,
        uitleg="Een feit kan je controleren. De drie andere zinnen zijn meningen: daar kan je het mee oneens zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een feit en een mening?",
        opties=[
            "Een feit kan je nagaan, een mening is wat iemand ervan vindt",
            "Een feit is langer dan een mening",
            "Een mening staat altijd in de titel",
            "Een feit bevat altijd een cijfer",
        ],
        antwoord=0,
        uitleg="Feiten zijn controleerbaar. Meningen kunnen goed onderbouwd zijn, maar blijven een oordeel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zinnen zijn meningen?",
        opties=[
            "Die film is veel te lang.",
            "Fietsen is leuker dan wandelen.",
            "Deze gsm is zijn geld niet waard.",
            "Deze gsm weegt 180 gram.",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie zijn oordelen. Het gewicht van de gsm kan je nameten: dat is een feit.",
    ),
    dict(
        type="invultekst",
        vraag="Wie een tekst geschreven heeft, is de ___ van die tekst.",
        antwoord="auteur",
        uitleg="Staat er geen auteur bij, dan is dat een eerste reden om voorzichtig te zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tekst zonder vermelde auteur is daarom meteen onbetrouwbaar.",
        antwoord=False,
        uitleg="Het is een waarschuwingssignaal, geen bewijs. Je kijkt ook naar de uitgever, de bronnen en hoe recent de tekst is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen helpen je te beoordelen of een tekst betrouwbaar is?",
        opties=[
            "Wordt de auteur vermeld?",
            "Wie publiceert het artikel?",
            "Welke bronnen gebruikt de tekst?",
            "Staan er veel afbeeldingen in?",
        ],
        antwoord=[0, 1, 2],
        uitleg="Auteur, uitgever en bronnen zijn criteria. Mooie afbeeldingen zeggen niets over de juistheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bericht wordt alleen gedeeld via sociale media en niet door nieuwsmedia. Wat betekent dat?",
        opties=[
            "Je moet extra voorzichtig zijn en het elders nagaan",
            "Het is zeker waar",
            "Het is zeker gelogen",
            "Het betekent niets",
        ],
        antwoord=0,
        uitleg="Nieuwsredacties controleren hun berichten. Circuleert iets enkel op sociale media, ga het dan zelf na bij een betrouwbare bron.",
    ),
    dict(
        type="invultekst",
        vraag="Verzonnen nieuws dat zich voordoet als echt nieuws, noem je ___.",
        antwoord="nepnieuws",
        uitleg="Nepnieuws of fake news wil je misleiden, vaak om clicks of geld te verdienen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een titel als 'Je gelooft NOOIT wat deze leerling deed!' is vooral bedoeld om ...",
        opties=[
            "je te doen klikken",
            "je correct te informeren",
            "je iets te leren",
            "je een verhaal te vertellen",
        ],
        antwoord=0,
        uitleg="Zo'n titel heet clickbait. Een neutrale titel zegt waarover het gaat; een lokkende titel wil vooral bezoekers.",
    ),
    dict(
        type="waarofniet",
        vraag="Propaganda wil je op één bepaalde manier laten denken.",
        antwoord=True,
        uitleg="Propaganda brengt bewust maar één kant van het verhaal, om je mening te sturen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het belangrijk te weten of informatie recent is?",
        opties=[
            "Omdat cijfers en afspraken snel verouderen",
            "Omdat oude teksten altijd fout zijn",
            "Omdat nieuwe teksten altijd juist zijn",
            "Omdat dat niets uitmaakt",
        ],
        antwoord=0,
        uitleg="Een prijs, een record of een regel van vijf jaar geleden kan intussen niet meer kloppen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een influencer prijst enthousiast een crème aan en krijgt daarvoor betaald. Wat is die boodschap eigenlijk?",
        opties=["Reclame", "Nieuws", "Een onderzoek", "Een instructie"],
        antwoord=0,
        uitleg="Wie betaald wordt om iets aan te prijzen, maakt reclame. Daarom moet dat ook aangeduid worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over bronnen kloppen?",
        opties=[
            "Een tekst die zijn bronnen noemt, kan je beter controleren",
            "Een link naar een onderzoek is sterker dan 'men zegt'",
            "Een tekst zonder enkele bron vraagt extra voorzichtigheid",
            "Een tekst met veel bronnen is altijd juist",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bronnen maken een tekst controleerbaar, maar veel bronnen zijn geen garantie: je moet ze zelf ook kunnen vertrouwen.",
    ),
    dict(
        type="invultekst",
        vraag="Wat de zender met een tekst wil bereiken, noem je de ___ van de zender.",
        antwoord="bedoeling",
        uitleg="Wil hij informeren, verkopen of overtuigen? De bedoeling verandert hoe je de tekst moet lezen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een professioneel ogende website is daarom betrouwbaar.",
        antwoord=False,
        uitleg="Een mooie website is makkelijk te maken. Kijk naar wie erachter zit, welke bronnen er zijn en wat het doel is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een standpunt?",
        opties=[
            "Het oordeel dat iemand inneemt over een kwestie",
            "Een feit met een cijfer erbij",
            "De titel van een tekst",
            "De eerste alinea",
        ],
        antwoord=0,
        uitleg="Een standpunt is de mening die iemand verdedigt, bijvoorbeeld: 'Gsm's horen niet thuis op school.'",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een goed argument bij het standpunt 'Onze school moet een fietsenstalling met dak krijgen'?",
        opties=[
            "Wie nat op zijn zadel moet zitten, komt doorweekt in de les",
            "Ik vind dat gewoon",
            "Iedereen weet dat",
            "Een dak is mooi",
        ],
        antwoord=0,
        uitleg="Een argument geeft een reden die je standpunt ondersteunt. 'Ik vind dat' of 'iedereen weet dat' is geen reden.",
    ),
    dict(
        type="waarofniet",
        vraag="Een mening mag je onderbouwen met feiten.",
        antwoord=True,
        uitleg="Dat is net wat een mening sterk maakt: je standpunt plus argumenten die op feiten steunen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is stereotypering?",
        opties=[
            "Een vast, te algemeen beeld van een groep mensen",
            "Een spellingregel",
            "Een tekstsoort",
            "Een manier om een tekst in te delen",
        ],
        antwoord=0,
        uitleg="'Wie dialect spreekt, is minder slim' is zo'n vast beeld. Het klopt niet en het is oneerlijk tegenover mensen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest een tekst en je twijfelt of hij klopt. Wat doe je?",
        opties=[
            "Je zoekt dezelfde informatie bij een andere, betrouwbare bron",
            "Je deelt hem toch maar, voor het geval dat",
            "Je gelooft de langste versie",
            "Je kijkt hoeveel likes hij heeft",
        ],
        antwoord=0,
        uitleg="Informatie nakijken bij een tweede bron is de eenvoudigste controle. Likes zeggen niets over juistheid.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Een bericht heeft geen auteur, staat alleen op sociale media en linkt naar een site vol advertenties. Wat besluit je?",
        opties=[
            "Waarschijnlijk nepnieuws, bedoeld om bezoekers te lokken",
            "Zeker betrouwbaar nieuws",
            "Een instructieve tekst",
            "Een literaire tekst",
        ],
        antwoord=0,
        uitleg="Geen zender, een besloten kanaal en een doel dat geld oplevert: drie signalen samen maken het verdacht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke signalen wijzen op nepnieuws?",
        opties=[
            "Er wordt geen auteur vermeld",
            "Het bericht verschijnt nergens bij betrouwbare nieuwsmedia",
            "De titel is overdreven en wil je vooral doen klikken",
            "Het bericht bevat een datum",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie zijn alarmsignalen. Een datum vermelden is net een goed teken.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een tekst staat: 'Uit onderzoek van de KU Leuven (2025) blijkt dat 62 % van de leerlingen te weinig slaapt.' Wat maakt die zin sterk?",
        opties=[
            "Hij noemt zijn bron en het jaartal",
            "Hij bevat een groot getal",
            "Hij staat vetgedrukt",
            "Hij is lang",
        ],
        antwoord=0,
        uitleg="Een controleerbare bron met een jaartal maakt een bewering na te gaan. Zonder bron blijft een cijfer een bewering.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tekst die alleen maar voordelen van een product opsomt, is waarschijnlijk niet neutraal.",
        antwoord=True,
        uitleg="Wie enkel de goede kanten toont, wil overtuigen. Een informatieve tekst noemt ook de nadelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zinnen uit een productreview zijn feiten?",
        opties=[
            "De batterij gaat 12 uur mee.",
            "Het toestel weegt 240 gram.",
            "De levering duurde vier dagen.",
            "Het is het beste toestel van dit jaar.",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie kan je meten of nagaan. 'Het beste van dit jaar' is een oordeel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je wil weten of een gezondheidsartikel klopt. Welke bron kies je om het na te gaan?",
        opties=[
            "De website van een ziekenhuis of een officiële gezondheidsdienst",
            "Een reactie op een forum",
            "Een reclamefilmpje van een merk",
            "Een meme",
        ],
        antwoord=0,
        uitleg="Kies een zender met kennis van zaken die geen belang heeft bij de verkoop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een krantenkop luidt: 'Schokkend: zoveel suiker zit er écht in je ontbijt!' Wat zie je aan die titel?",
        opties=[
            "Hij is niet neutraal en wil je nieuwsgierig maken",
            "Hij is een feit",
            "Hij noemt zijn bron",
            "Hij is een instructie",
        ],
        antwoord=0,
        uitleg="Woorden als 'schokkend' en 'écht' zijn gevoelswoorden. Een neutrale titel zou zijn: 'Hoeveel suiker zit er in ontbijtgranen?'",
    ),
    dict(
        type="invultekst",
        vraag="Een tekst die zich voordoet als een reportage maar eigenlijk reclame is, heet een ___.",
        antwoord="publireportage",
        uitleg="Kijk altijd naar de zender: als de verkoper de tekst betaalt, is het reclame.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand zegt: 'Gsm's moeten weg op school, want uit onderzoek blijkt dat leerlingen dan beter opletten.' Wat is het argument?",
        opties=[
            "Uit onderzoek blijkt dat leerlingen beter opletten",
            "Gsm's moeten weg op school",
            "Onderzoek is belangrijk",
            "Leerlingen hebben gsm's",
        ],
        antwoord=0,
        uitleg="Het standpunt is wat hij wil ('gsm's moeten weg'), het argument is de reden die erachter staat, meestal na 'want' of 'omdat'.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke argumenten passen bij het standpunt 'Onze klas verdient een kraantjeswaterfontein'?",
        opties=[
            "Leerlingen drinken dan meer water en minder frisdrank",
            "We hoeven geen plastic flessen meer mee te brengen",
            "Water uit de kraan is goedkoper dan flessenwater",
            "Ik hou nu eenmaal van water",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eerste drie geven een reden die ook voor anderen telt. Wat jij lekker vindt, overtuigt niemand.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie een tekst schrijft om te overtuigen, geeft daarin best ook de nadelen toe.",
        antwoord=True,
        uitleg="Een tegenargument erkennen en weerleggen maakt je sterker: de lezer merkt dat je de zaak kent.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan herken je een mening die vermomd is als feit?",
        opties=[
            "Aan gevoelswoorden als 'schandalig', 'iedereen weet', 'veel te'",
            "Aan de aanwezigheid van een datum",
            "Aan een cijfer met een eenheid",
            "Aan de naam van de auteur",
        ],
        antwoord=0,
        uitleg="Zulke woorden dragen een oordeel. 'Veel te duur' is een mening, '24 euro' is een feit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tekst over elektrische steps komt van een fabrikant van steps. Wat doe je met de informatie?",
        opties=[
            "Je gebruikt ze, maar zoekt de nadelen elders op",
            "Je gooit ze helemaal weg",
            "Je neemt ze zonder meer over",
            "Je kijkt alleen naar de foto's",
        ],
        antwoord=0,
        uitleg="Een belanghebbende zender kan juiste informatie geven, maar geeft zelden het volledige beeld.",
    ),
    dict(
        type="invultekst",
        vraag="Een vast en te algemeen beeld van een hele groep mensen heet een ___.",
        antwoord="stereotype",
        uitleg="Stereotypen zitten vaak onopgemerkt in teksten en beelden. Wie ze herkent, leest scherper.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een voorbeeld van stereotypering in een tekst?",
        opties=[
            "'Zoals alle tieners hangt ook hij de hele dag aan zijn scherm.'",
            "'Drie op de tien tieners slapen minder dan acht uur.'",
            "'De school start om 8.30 uur.'",
            "'Hij fietst elke dag naar school.'",
        ],
        antwoord=0,
        uitleg="'Zoals alle tieners' maakt van een hele groep één figuur. De andere zinnen zijn gewoon feiten.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tekst kan tegelijk correct en onbruikbaar zijn voor jouw opdracht.",
        antwoord=True,
        uitleg="Betrouwbaar, correct én bruikbaar zijn drie verschillende dingen: een juiste tekst over een ander land helpt je niet met een vraag over België.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee betrouwbare teksten spreken elkaar tegen. Wat doe je?",
        opties=[
            "Je kijkt naar de datum, de bronnen en wat ze precies onderzocht hebben",
            "Je kiest de kortste",
            "Je kiest de tekst die jouw mening bevestigt",
            "Je gebruikt geen van beide",
        ],
        antwoord=0,
        uitleg="Vaak gaan ze over een andere periode of een andere groep. Wie kijkt naar wat er precies gemeten is, ziet het verschil.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over meningen kloppen?",
        opties=[
            "Een mening kan je onderbouwen met feiten",
            "Twee mensen kunnen een verschillende mening hebben over dezelfde feiten",
            "Een mening herken je vaak aan gevoelswoorden",
            "Een mening is altijd fout",
        ],
        antwoord=[0, 1, 2],
        uitleg="Meningen zijn niet fout: ze zijn alleen geen feiten. Sterke meningen steunen op feiten en argumenten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je schrijft zelf een reactie op een forum over zwerfvuil. Hoe maak je ze overtuigend?",
        opties=[
            "Je geeft je standpunt en drie argumenten, met een cijfer of een voorbeeld erbij",
            "Je schrijft in hoofdletters",
            "Je noemt wie het niet met je eens is dom",
            "Je herhaalt vier keer hetzelfde",
        ],
        antwoord=0,
        uitleg="Standpunt plus onderbouwde argumenten overtuigen. Hoofdletters lezen als schreeuwen en werken averechts.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zou je een bericht niet doorsturen als je niet zeker weet of het klopt?",
        opties=[
            "Omdat je dan zelf helpt verspreiden wat misschien onjuist is",
            "Omdat doorsturen verboden is",
            "Omdat berichten dan verdwijnen",
            "Omdat je dan geen likes krijgt",
        ],
        antwoord=0,
        uitleg="Wie deelt, wordt zelf een zender. Eerst nakijken, dan pas doorsturen.",
    ),
]

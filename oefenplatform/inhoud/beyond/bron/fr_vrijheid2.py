# -*- coding: utf-8 -*-
"""Vrijheid en determinisme in de 20ste eeuw.

Het vierde en laatste thema over wijsgerige antropologie. De fiche zet voor
de 20ste eeuw vijf denkers op een rij:

    Martin Heidegger
    Jean-Paul Sartre
    Michel Foucault
    Henry Frankfurt
    Jan Verplaetse

Eén opmerking bij die lijst: de filosoof die bekend is om de hiërarchie van
verlangens heet Harry Frankfurt. De fiche schrijft Henry. Omdat wij niet
weten of dat een vergissing is of een andere naam, staat hieronder in de
vragen enkel de familienaam Frankfurt, zonder voornaam. Zo staat er niets in
dat tegen de fiche ingaat én niets dat een echte filosoof een naam geeft die
niet de zijne is.

Bij elke naam staat alleen de bijdrage aan dít debat: Heidegger de mens die
in een situatie geworpen is en zich ertoe moet verhouden, Sartre de vrijheid
waaraan je niet kan ontsnappen en de kwade trouw, Foucault het subject dat
door macht en normen gevormd wordt, Frankfurt het willen van wat je wil, en
Verplaetse de afwijzing van de vrije wil met zijn gevolgen voor het
strafrecht.

Deel 1 zijn Heidegger en Sartre.
Deel 2 zijn Foucault, Frankfurt en Verplaetse, en de vergelijking.
"""

DEEL1 = [
    dict(type="meerkeuze",
         vraag="Wat bedoelt Martin Heidegger als hij zegt dat de mens geworpen is?",
         opties=["je kiest je lichaam, je tijd en je afkomst niet; je vindt je daarin terug",
                 "je kiest je lichaam en je afkomst zelf, voor je geboren wordt",
                 "je wordt door de mensen rondom jou gedwongen om een bepaald leven te leiden",
                 "je raakt je houvast kwijt zodra je over je eigen leven nadenkt"],
         antwoord=0,
         uitleg="Geworpenheid is het vertrekpunt dat je niet gekozen hebt. Daarbinnen moet je "
                "vervolgens iets met je leven doen."),
    dict(type="meerkeuze",
         vraag="Welke vrijheid blijft er bij Heidegger over, ondanks die geworpenheid?",
         opties=["je kan je verhouden tot je mogelijkheden en je eigen leven op je nemen",
                 "je kan je afkomst en je lichaam achteraf nog volledig veranderen",
                 "je kan kiezen in welke tijd en in welk land je opnieuw geboren wordt",
                 "je kan je volledig losmaken van de wereld waarin je bent beland"],
         antwoord=0,
         uitleg="Niet het vertrekpunt, maar wat je ermee doet. Je leven op je nemen in plaats van "
                "het aan de gewoonte over te laten, dat is bij hem de inzet."),
    dict(type="meerkeuze",
         vraag="Wat bedoelt Heidegger met een oneigenlijk bestaan?",
         opties=["je leeft zoals men nu eenmaal leeft, zonder het zelf op je te nemen",
                 "je leeft volgens strakke regels die een overheid je heeft opgelegd",
                 "je leeft in een leugen en vertelt anderen niet wie je bent",
                 "je leeft zonder enig doel en doet elke dag iets anders"],
         antwoord=0,
         uitleg="Het gaat niet over liegen maar over wegkijken: het leven laten lopen zoals het "
                "hoort te lopen, zonder er zelf voor in te staan."),
    dict(type="meerkeuze",
         vraag="Wat is de beroemde stelling van Jean-Paul Sartre over de mens?",
         opties=["de mens is vrij en kan aan die vrijheid niet ontsnappen",
                 "de mens is onvrij en moet leren dat te aanvaarden",
                 "de mens is vrij zolang hij geld en gezondheid heeft",
                 "de mens is vrij in zijn denken maar nooit in zijn daden"],
         antwoord=0,
         uitleg="Hij noemt de mens gedoemd tot vrijheid: ook niet kiezen is een keuze, en de "
                "verantwoordelijkheid kan je niet doorschuiven."),
    dict(type="meerkeuze",
         vraag="Wat betekent bij Sartre dat de existentie aan de essentie voorafgaat?",
         opties=["er ligt geen vaste menselijke natuur klaar; je wordt wie je bent door te handelen",
                 "er ligt een vaste menselijke natuur klaar die je leven lang hetzelfde blijft",
                 "er ligt een bestemming klaar die je in de loop van je leven ontdekt",
                 "er ligt niets klaar, en daarom heeft handelen geen enkel belang"],
         antwoord=0,
         uitleg="Eerst besta je, daarna maak je door je keuzes wat je bent. Bij een mes is het "
                "omgekeerd: daarvan ligt het doel vast voor het gemaakt wordt."),
    dict(type="meerkeuze",
         vraag="Wat is kwade trouw bij Sartre?",
         opties=["je doet alsof je niet kon kiezen, om je verantwoordelijkheid te ontlopen",
                 "je liegt bewust tegen iemand anders over wat je gedaan hebt",
                 "je kiest met opzet voor het kwade en verdedigt dat ook",
                 "je handelt zonder erbij na te denken en krijgt er veel later spijt van"],
         antwoord=0,
         uitleg="Het bedrog is naar binnen gericht. Ik moest wel, ik ben nu eenmaal zo: dat is bij "
                "hem geen verklaring maar een uitvlucht."),
    dict(type="meerkeuze",
         vraag="Een werknemer zegt: ik ben nu eenmaal een kelner, dus ik moet mij zo gedragen. "
               "Hoe zou Sartre dat lezen?",
         opties=["als kwade trouw, want hij verbergt zijn keuze achter zijn rol",
                 "als eerlijkheid, want zijn beroep legt hem die rol nu eenmaal op",
                 "als geworpenheid, want hij heeft zijn beroep niet zelf gekozen",
                 "als determinisme, want zijn karakter bepaalt zijn gedrag volledig"],
         antwoord=0,
         uitleg="Een rol is geen natuurwet. Wie zich erachter wegzet, verbergt dat hij er elke dag "
                "opnieuw voor kiest."),
    dict(type="meerkeuze",
         vraag="Welke uitspraken over Heidegger en Sartre kloppen?",
         opties=["beiden vertrekken van een mens die zijn situatie niet gekozen heeft",
                 "Sartre legt meer gewicht bij de keuze dan Heidegger doet",
                 "beiden vinden dat de mens door natuurwetten volledig vastligt",
                 "beiden ontkennen dat de mens ergens verantwoordelijk voor is"],
         antwoord=[0, 1],
         uitleg="De eerste twee. Het zijn twee stemmen uit dezelfde hoek, met een ander accent: "
                "geworpenheid tegenover keuze."),
    dict(type="meerkeuze",
         vraag="Waarom hoort het existentialisme niet bij het determinisme?",
         opties=["de mens blijft er verantwoordelijk voor wat hij van zijn situatie maakt",
                 "de mens kan er zijn afkomst en zijn lichaam vrij kiezen",
                 "de mens wordt er volledig door zijn omgeving bepaald",
                 "de mens heeft er geen enkele vaste situatie om van uit te vertrekken"],
         antwoord=0,
         uitleg="Ze aanvaarden dat je niet alles in de hand hebt, en houden toch vast dat je "
                "handelen van jou is."),
    dict(type="meerkeuze",
         vraag="Welke uitspraken over de vrijheid bij Sartre kloppen?",
         opties=["niet kiezen is bij hem ook een keuze",
                 "vrijheid gaat bij hem samen met verantwoordelijkheid, en dat weegt",
                 "vrijheid betekent bij hem dat je alles kan wat je wil",
                 "vrijheid geldt bij hem enkel voor wie geen zorgen heeft"],
         antwoord=[0, 1],
         uitleg="De eerste twee. Zijn vrijheid is geen gemak maar een last: er is niemand anders "
                "aan wie je je keuzes kan toeschrijven."),
    dict(type="meerkeuze",
         vraag="Wat is het verschil tussen de vrijheid bij de Stoïcijnen en die bij Sartre?",
         opties=["de Stoïcijnen leggen ze in je houding, Sartre in je keuze en je daad",
                 "de Stoïcijnen leggen ze in je keuze, Sartre in je houding",
                 "beiden leggen ze volledig buiten de mens, in de orde van de wereld",
                 "beiden ontkennen dat er zoiets als vrijheid bij de mens bestaat"],
         antwoord=0,
         uitleg="Bij de Stoïcijnen aanvaard je wat je niet in de hand hebt; bij Sartre kan je je "
                "achter niets verschuilen."),
    dict(type="meerkeuze",
         vraag="Waarom noemt Sartre de vrijheid van de mens ook een last?",
         opties=["omdat je de gevolgen van je keuzes aan niemand anders kan toeschrijven",
                 "omdat je nooit mag kiezen wat je zelf het liefst zou willen",
                 "omdat anderen altijd beter weten wat goed voor je is",
                 "omdat elke keuze die je maakt achteraf toch de verkeerde blijkt te zijn"],
         antwoord=0,
         uitleg="Vandaar zijn woord gedoemd: er is geen natuur, geen rol en geen God aan wie je je "
                "keuze kan overlaten."),
    dict(type="waarofniet",
         vraag="Geworpenheid bij Heidegger betekent dat je je vertrekpunt niet gekozen hebt.",
         antwoord=True,
         uitleg="Waar. Je tijd, je lichaam en je afkomst vind je aan; wat je ermee doet, is van "
                "jou."),
    dict(type="waarofniet",
         vraag="Volgens Sartre ligt er een vaste menselijke natuur klaar voor je geboren wordt.",
         antwoord=False,
         uitleg="Niet waar. Bij hem gaat de existentie aan de essentie voorbij: je maakt jezelf "
                "door te handelen."),
    dict(type="waarofniet",
         vraag="Kwade trouw bij Sartre is liegen tegen iemand anders.",
         antwoord=False,
         uitleg="Niet waar. Het is jezelf voorhouden dat je niet kon kiezen."),
    dict(type="waarofniet",
         vraag="Volgens Sartre is ook niet kiezen een keuze.",
         antwoord=True,
         uitleg="Waar. Daarom kan je volgens hem je verantwoordelijkheid niet afleggen."),
    dict(type="invultekst",
         vraag="Hoe noemt Heidegger het feit dat je je situatie niet gekozen hebt? De ...",
         antwoord=["geworpenheid"],
         uitleg="Je vindt je in een tijd, een lichaam en een afkomst terug die je niet koos."),
    dict(type="invultekst",
         vraag="Welke filosoof noemt de mens gedoemd tot vrijheid?",
         antwoord=["Sartre", "Jean-Paul Sartre"],
         uitleg="Bij hem kan je aan je vrijheid en aan je verantwoordelijkheid niet ontsnappen."),
    dict(type="invultekst",
         vraag="Hoe heet bij Sartre het zelfbedrog waarin je doet alsof je niet kon kiezen?",
         antwoord=["kwade trouw"],
         uitleg="Ik moest wel, ik ben nu eenmaal zo: dat is bij hem een uitvlucht."),
    dict(type="invultekst",
         vraag="Welke stroming uit de 20ste eeuw stelt de keuze van de mens centraal?",
         antwoord=["het existentialisme", "existentialisme"],
         uitleg="Heidegger en Sartre worden er beide bij gerekend."),
]

DEEL2 = [
    dict(type="meerkeuze",
         vraag="Waar legt Michel Foucault de nadruk op in dit debat?",
         opties=["op de macht en de normen die mee maken wie je geworden bent",
                 "op de natuurwetten die elke beweging van je lichaam vastleggen",
                 "op de keuze die je op elk moment volledig vrij kan maken",
                 "op het lot dat je leven van tevoren heeft uitgetekend"],
         antwoord=0,
         uitleg="Niet een keten van oorzaken in de natuur, maar scholen, wetten, gewoonten en "
                "woorden die bepalen wat normaal heet. Ook die beperken je vrijheid."),
    dict(type="meerkeuze",
         vraag="Wat betekent disciplinering bij Foucault?",
         opties=["mensen worden door instellingen en gewoonten gevormd tot wat normaal heet",
                 "mensen worden door een strenge overheid met geweld in het gareel gehouden",
                 "mensen leren zichzelf uit vrije wil een strakke dagindeling aan",
                 "mensen worden gestraft zodra zij een regel van de wet overtreden"],
         antwoord=0,
         uitleg="Zijn punt is juist dat het meestal zonder geweld gaat. School, werk en kliniek "
                "vormen je zonder dat iemand je dwingt."),
    dict(type="meerkeuze",
         vraag="Waarom is de visie van Foucault lastig voor het idee van een vrije keuze?",
         opties=["ook wat jij wil, is mee gevormd door de wereld waarin je bent opgegroeid",
                 "ook wat jij wil, ligt in je hersenen vast van bij je geboorte",
                 "ook wat jij wil, wordt door de overheid rechtstreeks opgelegd",
                 "ook wat jij wil, is volledig toeval en dus zonder enige grond"],
         antwoord=0,
         uitleg="Een keuze die vrij lijkt, kan nog altijd een keuze zijn tussen mogelijkheden die "
                "jou zijn aangereikt."),
    dict(type="meerkeuze",
         vraag="Welk onderscheid gebruikt Frankfurt om vrijheid uit te leggen?",
         opties=["tussen wat je wil en wat je zou willen willen",
                 "tussen wat je wil en wat je werkelijk kan",
                 "tussen wat je wil en wat anderen van je verwachten",
                 "tussen wat je wil en wat de wet je toestaat"],
         antwoord=0,
         uitleg="Verlangens van de eerste en van de tweede orde. Vrij ben je volgens hem als die "
                "twee samenvallen."),
    dict(type="meerkeuze",
         vraag="Volgens Frankfurt: wanneer handel je vrij?",
         opties=["als je verlangen er een is dat je ook wíl hebben",
                 "als je verlangen van buitenaf bij je is gekomen",
                 "als je verlangen door geen enkele oorzaak is ontstaan",
                 "als je verlangen door je omgeving wordt goedgekeurd"],
         antwoord=0,
         uitleg="Je erkent dat verlangen als het jouwe. Daarom kan vrijheid bij hem samengaan met "
                "een wereld waarin alles zijn oorzaken heeft."),
    dict(type="meerkeuze",
         vraag="Twee mensen hebben dezelfde drang naar een middel. De ene wil die drang niet "
               "hebben, de andere wel. Wat zegt Frankfurt?",
         opties=["enkel wie zijn drang ook wil, handelt daarin vrij",
                 "beiden handelen vrij, want beiden volgen hun verlangen",
                 "geen van beiden handelt vrij, want een drang is altijd dwang",
                 "enkel wie zijn drang niet wil, handelt daarin vrij"],
         antwoord=0,
         uitleg="Wie zijn eigen drang afwijst en er toch aan toegeeft, wordt meegesleept. Dat is "
                "bij Frankfurt het verschil."),
    dict(type="meerkeuze",
         vraag="Waarom heet de positie van Frankfurt verzoenend?",
         opties=["ze laat vrijheid en een wereld vol oorzaken naast elkaar bestaan",
                 "ze geeft zowel de deterministen als de gelovigen volledig hun gelijk",
                 "ze verzoent de mens met het feit dat hij nergens vrij in is",
                 "ze verzoent het strafrecht met de wens om niemand te straffen"],
         antwoord=0,
         uitleg="Hij verlegt de vraag. Niet of je keuze zonder oorzaak was, maar of ze echt van "
                "jou is."),
    dict(type="meerkeuze",
         vraag="Welke stelling verdedigt Jan Verplaetse?",
         opties=["er bestaat geen vrije wil, en ons strafrecht zou dat moeten verwerken",
                 "er bestaat een vrije wil, en ons strafrecht bouwt daar terecht op",
                 "er bestaat geen vrije wil, en dus kan er geen enkele maatregel meer volgen",
                 "er bestaat een vrije wil, maar enkel bij wie goed is opgevoed"],
         antwoord=0,
         uitleg="Hij neemt het vooral op tegen schuld als grondslag van de straf; maatregelen om "
                "anderen te beschermen blijven in zijn voorstel mogelijk."),
    dict(type="meerkeuze",
         vraag="Welk gevolg heeft die stelling voor het strafrecht?",
         opties=["straffen om iemand schuld te laten boeten, verliest zijn grond",
                 "straffen om de samenleving te beschermen, verliest zijn grond",
                 "elke maatregel tegen een dader wordt daarmee onmogelijk",
                 "rechters moeten dan zwaarder straffen dan vandaag het geval is"],
         antwoord=0,
         uitleg="Beschermen, behandelen en voorkomen hebben geen schuld nodig. Vergelden wel, en "
                "net dat staat dan onder druk."),
    dict(type="meerkeuze",
         vraag="Welke uitspraken over de vijf denkers van de 20ste eeuw kloppen?",
         opties=["Sartre legt het meeste gewicht bij de keuze, Verplaetse het minste",
                 "Frankfurt zoekt een vrijheid die met oorzaken verenigbaar is",
                 "alle vijf verdedigen dat de mens volledig vrij is",
                 "alle vijf ontkennen dat de mens ergens vrij in is"],
         antwoord=[0, 1],
         uitleg="De eerste twee. De vijf staan juist op een rij van heel veel naar heel weinig "
                "vrijheid."),
    dict(type="meerkeuze",
         vraag="Welke uitspraken over dit debat in de 20ste eeuw kloppen?",
         opties=["de beperking van de vrijheid wordt er vaak binnen de mens zelf gezocht",
                 "de vraag wordt er ook een vraag over straf en verantwoordelijkheid",
                 "de vraag is er door de wetenschap definitief beslecht",
                 "de natuurwetten zijn er het enige dat nog ter sprake komt"],
         antwoord=[0, 1],
         uitleg="De eerste twee. Waar de 17de eeuw naar de natuurwetten keek, kijkt de 20ste eeuw "
                "naar verlangens, gewoonten, macht en hersenen."),
    dict(type="meerkeuze",
         vraag="Een rechter zegt: ik straf niet om te vergelden maar om herhaling te voorkomen. "
               "Bij welke denker uit dit thema sluit dat aan?",
         opties=["bij Jan Verplaetse", "bij Jean-Paul Sartre",
                 "bij Martin Heidegger", "bij Frankfurt"],
         antwoord=0,
         uitleg="Voorkomen en beschermen heeft geen schuld nodig. Dat is precies het strafrecht "
                "dat Verplaetse voor ogen heeft."),
    dict(type="waarofniet",
         vraag="Foucault zoekt de beperking van onze vrijheid vooral in natuurwetten.",
         antwoord=False,
         uitleg="Niet waar. Hij zoekt ze in macht, normen en instellingen die mee maken wie je "
                "bent."),
    dict(type="waarofniet",
         vraag="Volgens Frankfurt ben je vrij als je verlangen er een is dat je ook wil hebben.",
         antwoord=True,
         uitleg="Waar. Dat is zijn tweede orde: willen wat je wil."),
    dict(type="waarofniet",
         vraag="Jan Verplaetse verdedigt dat de mens een vrije wil heeft.",
         antwoord=False,
         uitleg="Niet waar. Hij verdedigt het omgekeerde, en trekt daar gevolgen uit voor het "
                "strafrecht."),
    dict(type="waarofniet",
         vraag="Bij Frankfurt kan vrijheid samengaan met een wereld waarin alles oorzaken heeft.",
         antwoord=True,
         uitleg="Waar. Daarom heet zijn positie verzoenend: de vraag is niet of er oorzaken zijn, "
                "maar of de keuze van jou is."),
    dict(type="invultekst",
         vraag="Welke filosoof onderzoekt hoe macht en normen ons vormen?",
         antwoord=["Foucault", "Michel Foucault"],
         uitleg="Bij hem is het subject zelf mee gemaakt door scholen, wetten en gewoonten."),
    dict(type="invultekst",
         vraag="Welke filosoof legt vrijheid uit als willen wat je wil?",
         antwoord=["Frankfurt"],
         uitleg="Zijn verlangens van de tweede orde: je erkent je verlangen als het jouwe."),
    dict(type="invultekst",
         vraag="Welke Vlaamse filosoof pleit voor een strafrecht zonder schuld?",
         antwoord=["Jan Verplaetse", "Verplaetse"],
         uitleg="Hij wijst de vrije wil af en trekt daar de lijn van door naar de straf."),
    dict(type="invultekst",
         vraag="Welke filosoof uit dit thema spreekt over een oneigenlijk bestaan?",
         antwoord=["Heidegger", "Martin Heidegger"],
         uitleg="Leven zoals men nu eenmaal leeft, zonder je leven zelf op je te nemen."),
]

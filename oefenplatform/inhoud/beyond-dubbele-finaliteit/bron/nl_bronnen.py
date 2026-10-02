# -*- coding: utf-8 -*-
"""Bronnen beoordelen: betrouwbaarheid, nepnieuws en framing — dubbele finaliteit.

De criterialijst van de vakfiche, vraag per vraag: wordt de auteur vermeld, wie
publiceert, is het elders te vinden, wat is de bedoeling van de zender, is het
reclame, nepnieuws of propaganda, is de titel neutraal, welke bronnen gebruikt
de tekst, feiten of meningen, recent of verouderd, relevant voor mijn doel, en
is er framing. Deel 1: de criteria. Deel 2: ze toepassen op gevallen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarom kijk je bij een tekst eerst of de auteur vermeld wordt?",
        opties=[
            "omdat je anders niet weet wie voor de inhoud verantwoordelijk is",
            "omdat een tekst zonder auteur altijd verzonnen is",
            "omdat je de auteur dan kan aanschrijven",
            "omdat elke tekst wettelijk een auteur moet noemen",
        ],
        antwoord=0,
        uitleg="Een ontbrekende auteur is geen bewijs van onzin, maar het is wel een reden om voorzichtiger te zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het criterium 'wie publiceert het artikel'?",
        opties=[
            "welke organisatie of site de tekst naar buiten brengt",
            "wie de tekst als eerste op sociale media deelde",
            "welke journalist het stuk geschreven heeft",
            "hoeveel mensen de tekst al gelezen hebben",
        ],
        antwoord=0,
        uitleg="Een krant, een universiteit, een bedrijf of een belangengroep: elk heeft een ander belang bij wat er staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom controleer je of informatie ook in andere betrouwbare bronnen te vinden is?",
        opties=[
            "omdat één losse bron zich kan vergissen of liegen",
            "omdat een bericht pas waar is als het tien keer gedeeld is",
            "omdat je anders geen bronvermelding mag maken",
            "omdat de langste versie altijd de juiste is",
        ],
        antwoord=0,
        uitleg="Melden onafhankelijke bronnen hetzelfde, dan wordt het waarschijnlijker. Herhalen van elkaar is geen bevestiging.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je berichten die bewust onwaar zijn en toch als nieuws worden verspreid?",
        antwoord=["nepnieuws", "fake news"],
        uitleg="Nepnieuws leent de vorm van een nieuwsbericht om geloofd te worden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het bewust kiezen van een invalshoek, waardoor je iets in een bepaald licht ziet?",
        antwoord=["framing", "een frame"],
        uitleg="Niet door te liegen, maar door te kiezen wat je noemt en met welke woorden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met de bedoeling van de zender?",
        opties=[
            "wat hij met de tekst bij jou wil bereiken",
            "hoeveel tijd hij aan de tekst besteed heeft",
            "op welk kanaal hij de tekst gezet heeft",
            "hoe oud hij was toen hij de tekst schreef",
        ],
        antwoord=0,
        uitleg="Informeren, overtuigen, verkopen, vermaken of verwarren: dat verandert hoe je de tekst moet lezen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een website die er professioneel uitziet, is daarom betrouwbaar.",
        antwoord=False,
        uitleg="Een goede vormgeving is goedkoop. Het uitzicht is wel een criterium, maar het is nooit het enige.",
    ),
    dict(
        type="waarofniet",
        vraag="Een titel die vooral moet aanzetten tot klikken, is een reden om kritisch verder te lezen.",
        antwoord=True,
        uitleg="Zo'n titel belooft meestal meer dan de tekst geeft. Men noemt dat clickbait.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bericht van vijf jaar oud is voor elke vraag even bruikbaar als een bericht van vandaag.",
        antwoord=False,
        uitleg="Of informatie verouderd is, hangt af van je onderwerp. Bij prijzen en cijfers maakt het meestal veel uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen reclame en propaganda?",
        opties=[
            "reclame wil je iets laten kopen, propaganda iets laten denken",
            "reclame is altijd eerlijk, propaganda altijd gelogen",
            "reclame staat op televisie, propaganda in de krant",
            "er is geen verschil, het zijn twee woorden voor hetzelfde",
        ],
        antwoord=0,
        uitleg="Beide zijn persuasief. Het doel verschilt: een aankoop tegenover een politiek of ideologisch standpunt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke criteria helpen je bij de betrouwbaarheid van een bron?",
        opties=[
            "wordt de auteur vermeld?",
            "welke bronnen worden in de tekst gebruikt?",
            "hoeveel lezersreacties staan eronder?",
            "hoe lang is de tekst in totaal?",
        ],
        antwoord=[0, 1],
        uitleg="Reacties en lengte zeggen niets. Auteur en bronvermelding wel, want ze maken controleren mogelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen gaan over de bedoeling van een tekst en niet over zijn juistheid?",
        opties=[
            "is het bericht reclame, nepnieuws of propaganda?",
            "is de titel neutraal of dient hij om clicks te krijgen?",
            "is de informatie ook elders terug te vinden?",
            "is de informatie recent of verouderd?",
        ],
        antwoord=[0, 1],
        uitleg="De laatste twee gaan over de inhoud zelf. De eerste twee over wat de zender met je wil.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tekst met vooral meningen kan nog altijd nuttig zijn voor je opdracht.",
        antwoord=True,
        uitleg="Als je opdracht over standpunten gaat, is zo'n tekst net wat je nodig hebt. Je noemt ze dan ook een mening.",
    ),
    dict(
        type="waarofniet",
        vraag="Of een bron bruikbaar is, hangt mee af van het doel waarvoor jij ze nodig hebt.",
        antwoord=True,
        uitleg="De eerste vraag blijft: is de informatie relevant voor mijn doel?",
    ),
    dict(
        type="waarofniet",
        vraag="Een influencer die betaald wordt om positief te zijn over een spel, maakt daarmee geen reclame.",
        antwoord=False,
        uitleg="Hij maakt in feite reclame, ook al klinkt het als een mening.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als een bericht alleen op sociale media opduikt en nergens anders?",
        opties=[
            "je zoekt eerst of een onafhankelijke bron het ook meldt",
            "je deelt het en wacht op reacties van anderen",
            "je besluit meteen dat het verzonnen is",
            "je neemt het over, want nieuws is daar sneller",
        ],
        antwoord=0,
        uitleg="Afwezigheid elders is een waarschuwing, geen bewijs. Daarom check je het bij een bron die iets te verliezen heeft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kijk je welke bronnen in een tekst zelf gebruikt worden?",
        opties=[
            "omdat je dan kan nagaan waarop de uitspraken steunen",
            "omdat een tekst met veel bronnen altijd klopt",
            "omdat je de bronnen dan kan overnemen als je eigen bron",
            "omdat een tekst zonder bronnen niet gepubliceerd mag worden",
        ],
        antwoord=0,
        uitleg="Een verwijzing laat zich controleren. Dat een tekst verwijst, is nog geen garantie dat hij juist verwijst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over framing kloppen?",
        opties=[
            "framing kan werken zonder dat er iets onwaar is",
            "de woordkeuze van een bericht is al een vorm van framing",
            "framing is enkel mogelijk met verzonnen cijfers",
            "framing komt enkel in reclame voor",
        ],
        antwoord=[0, 1],
        uitleg="Belastingverlaging of besparing op de zorg kan hetzelfde besluit zijn. Het frame zit in wat je benoemt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een site noemt zich 'onafhankelijk nieuwsplatform' maar vermeldt nergens een auteur of redactie. Wat besluit je?",
        opties=[
            "de naam zegt niets, het ontbreken van een redactie wel iets",
            "de naam is een voldoende waarborg voor onafhankelijkheid",
            "de site is daarmee bewezen nepnieuws",
            "je mag de site enkel gebruiken voor meningen",
        ],
        antwoord=0,
        uitleg="Een naam kiest men zelf. Wie niemand noemt die verantwoordelijk is, kan ook niet op fouten aangesproken worden.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een titel die vooral bedoeld is om mensen te laten doorklikken?",
        antwoord=["clickbait", "een clickbaittitel"],
        uitleg="Hij belooft een onthulling of een schandaal en laat net het antwoord weg.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Een bericht zegt: 'Wetenschappers bewijzen dat chocolade slank maakt.' Wat valt je als eerste op?",
        opties=[
            "er wordt niet gezegd welke wetenschappers of welk onderzoek",
            "chocolade kan nooit met onderzoek verbonden worden",
            "de zin is te kort om een bericht te zijn",
            "het woord bewijzen bestaat niet in de wetenschap",
        ],
        antwoord=0,
        uitleg="Een vage verwijzing naar wetenschap is een klassiek middel. Zonder naam of studie kan je niets nagaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee sites melden hetzelfde, maar de tweede verwijst naar de eerste. Hoeveel bronnen heb je?",
        opties=[
            "één, want de tweede voegt niets toe",
            "twee, want het staat op twee sites",
            "geen enkele, want ze verwijzen naar elkaar",
            "dat valt niet te zeggen zonder de datum",
        ],
        antwoord=0,
        uitleg="Overnemen is geen bevestiging. Je hebt pas een tweede bron als iemand het zelf uitzocht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een folder van een bank legt uit hoe sparen werkt. Is dat bruikbaar?",
        opties=[
            "ja, voor de uitleg, met in gedachten dat de bank wil verkopen",
            "neen, een bank mag je nooit als bron gebruiken",
            "ja, zonder voorbehoud, want een bank kent het onderwerp",
            "neen, een folder van een bedrijf kan nooit een bron zijn",
        ],
        antwoord=0,
        uitleg="Een zender met een belang is niet waardeloos. Je weet alleen welk deel van het verhaal hij niet zal vertellen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tekst die enkel feiten bevat, kan toch een eenzijdig beeld geven.",
        antwoord=True,
        uitleg="Door te kiezen welke feiten je noemt, stuur je het beeld. Dat is ook framing.",
    ),
    dict(
        type="waarofniet",
        vraag="Een grafiek in een bericht maakt dat bericht automatisch betrouwbaar.",
        antwoord=False,
        uitleg="Een as die niet bij nul begint of een slim gekozen periode kan een grafiek laten zeggen wat de zender wil.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag een onbetrouwbare tekst gebruiken als bron over wat de zender wil laten geloven.",
        antwoord=True,
        uitleg="Voor de feiten is hij onbruikbaar, voor de bedoeling van de zender juist uitstekend.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke signalen wijzen samen op nepnieuws?",
        opties=[
            "geen auteur en geen bronvermelding",
            "enkel verspreid via sociale media, met een schreeuwende titel",
            "een lange tekst met tussentitels",
            "een datum bovenaan het artikel",
        ],
        antwoord=[0, 1],
        uitleg="De naam en het uitzicht zijn gratis. Lengte, tussentitels en een datum zeggen op zichzelf ook niets.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een krant schrijft 'de regering besliste', een andere 'de regering drukte door'. Wat is hier aan de hand?",
        opties=[
            "framing door woordkeuze",
            "een feitelijke tegenspraak",
            "een verschil in datum",
            "een verschil in kanaal",
        ],
        antwoord=0,
        uitleg="Het feit is hetzelfde. Doordrukken voegt een oordeel toe zonder het als oordeel te presenteren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tekst van een belangenorganisatie is per definitie onbruikbaar.",
        antwoord=False,
        uitleg="Je leest hem kritischer en je noemt zijn belang. Soms heeft die organisatie de beste cijfers van allemaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zoekt de huidige prijs van een treinticket en vindt een artikel uit 2019. Wat doe je?",
        opties=[
            "je zoekt verder, want dat cijfer is verouderd",
            "je neemt het cijfer over en vermeldt het jaar niet",
            "je verhoogt het cijfer zelf met een percentage",
            "je gebruikt het, want prijzen veranderen zelden",
        ],
        antwoord=0,
        uitleg="Voor een actuele prijs is 2019 onbruikbaar. Voor een vergelijking door de tijd is het juist nuttig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het verschijnsel dat een bericht pas betrouwbaar lijkt omdat je het al vaak zag?",
        antwoord=["herhaling", "het herhalingseffect"],
        uitleg="Vaak gezien is niet hetzelfde als vaak bevestigd: meestal is het dezelfde bron die doorgegeven wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over de bedoeling van de zender kloppen?",
        opties=[
            "dezelfde feiten kunnen met verschillende bedoelingen gebracht worden",
            "de bedoeling bepaalt hoe kritisch je moet lezen",
            "de bedoeling staat altijd bovenaan de tekst vermeld",
            "een zender met een bedoeling liegt altijd",
        ],
        antwoord=[0, 1],
        uitleg="Zelden staat er wat men met je wil. Je leidt het af uit de tekstsoort, het kanaal en de woordkeuze.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij het beoordelen van een luistertekst gelden dezelfde criteria als bij een leestekst.",
        antwoord=True,
        uitleg="Ook daar vraag je wie de zender is, met welk doel, en of het elders bevestigd wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een reclamespot gebruikt een man in een witte jas die het product aanraadt. Welke techniek is dat?",
        opties=[
            "een beroep op gezag dat hier niet bewezen is",
            "een vorm van framing door de datum",
            "een drogreden op basis van cijfers",
            "een narratieve tekststructuur",
        ],
        antwoord=0,
        uitleg="De jas moet voor wetenschap doorgaan. Niemand zegt wie de man is of waarin hij deskundig zou zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bericht zonder vermelde auteur is daarmee bewezen onwaar.",
        antwoord=False,
        uitleg="Het is een reden tot voorzichtigheid. Een persbureau of een redactie kan ook zonder naam juist berichten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een site over gezondheid verkoopt onderaan elke pagina dezelfde pillen. Wat besluit je?",
        opties=[
            "de informatie dient mee om die pillen te verkopen",
            "de informatie is daarmee volledig verzonnen",
            "de site mag wettelijk niets over gezondheid zeggen",
            "de pillen bewijzen dat de site deskundig is",
        ],
        antwoord=0,
        uitleg="Zender en verkoper zijn hier dezelfde. Dat maakt elke uitspraak over het nut van die pillen verdacht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de beste manier om een opvallende bewering te controleren?",
        opties=[
            "de oorspronkelijke bron van de bewering opzoeken",
            "kijken hoeveel mensen het bericht deelden",
            "de reacties onder het bericht doorlezen",
            "wachten tot iemand het tegenspreekt",
        ],
        antwoord=0,
        uitleg="Naar de bron teruggaan laat zien wat er echt onderzocht of gezegd werd, en wat er onderweg bijkwam.",
    ),
    dict(
        type="waarofniet",
        vraag="Framing kan ook ontstaan door iets juist niet te vermelden.",
        antwoord=True,
        uitleg="Wat je weglaat, bestaat voor de lezer niet. Dat stuurt even sterk als wat je wel zegt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vraag zegt niets over de betrouwbaarheid van een bron?",
        opties=[
            "hoeveel volgers heeft de zender?",
            "wordt het bericht door een betrouwbare bron verspreid?",
            "bevat de tekst vooral feiten of meningen?",
            "is er sprake van framing?",
        ],
        antwoord=0,
        uitleg="Volgers zijn te koop en zeggen niets over juistheid. De drie andere vragen helpen wel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een bericht dat eruitziet als een artikel maar door een bedrijf betaald is?",
        antwoord=["een publireportage", "publireportage"],
        uitleg="Ze hoort bij de persuasieve teksten, naast reclame en propaganda.",
    ),
]

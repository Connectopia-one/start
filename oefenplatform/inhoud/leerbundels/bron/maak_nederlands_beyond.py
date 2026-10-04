# -*- coding: utf-8 -*-
"""De leerbundels voor Nederlands op 🌍 Beyond-niveau.

Gebaseerd op de twee vakfiches Nederlands van de 3de graad
doorstroomfinaliteit, geldig vanaf 1 januari 2027. Fiche 1 is het receptieve
examen (lezen, luisteren, literatuur, taalbeschouwing), fiche 2 het
productieve (spreken, schrijven, schriftelijke interactie, gesprek). Beide
gelden voor bedrijfswetenschappen, economie-wiskunde, humane wetenschappen,
Latijn-wiskunde met extra wetenschappen, welzijnswetenschappen en
wiskunde-wetenschappen.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../beyond/nederlands.json` doet
daar het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-beyond". Nederlands bestaat ook op ✨ Spark en
op 🚀 Boost dubbele finaliteit, en daar komen thematitels in voor die hier
bijna of helemaal gelijk klinken.

Geen enkel citaat in deze bundels is van een bestaande dichter of schrijver.
Waar een voorbeeldregel of een voorbeeldzin staat, is die zelf geschreven en
staat er geen naam bij. Een verzonnen citaat in de mond van een echt auteur
is geen voorbeeld maar een vervalsing.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Nederlands"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 1. Tekstsoorten en teksttypes
BUNDELS["tekstsoorten-en-teksttypes-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Tekstsoorten en teksttypes",
    onder="De zeven tekstsoorten, hun doel, en hoe je ze aan een tekst of een luistertekst herkent.",
    secties=[
        dict(kop="Het doel bepaalt de soort", blokken=[
            ("p", "Een tekst wordt ingedeeld naar zijn <strong>doel</strong>: wat wil de maker bij jou "
                  "bereiken? <strong>De soort hangt dus af van het doel van de zender</strong>, niet van "
                  "het onderwerp. Over hetzelfde onderwerp kan je informeren, overtuigen, voorschrijven of "
                  "vertellen. <strong>De voorbeelden kunnen zowel geschreven als gesproken zijn</strong>: "
                  "op het examen kan je een interview, een gedicht of een reclameboodschap "
                  "<strong>zowel lezen als beluisteren</strong>."),
            ("p", tabel(["Tekstsoort", "Doel", "Voorbeeld"], [
                ["Informatief", "je iets laten weten over een onderwerp", "een krantenartikel, een interview, een reportage"],
                ["Persuasief", "je overtuigen of beïnvloeden", "een reclamefilmpje, een folder van een politieke partij"],
                ["Argumentatief", "argumenten dragen er een standpunt", "een betoog, een pleidooi, een debat"],
                ["Opiniërend", "een mening geven", "een column, een recensie, een productreview"],
                ["Prescriptief", "instructies geven over hoe je iets doet", "een handleiding, een recept uit een kookboek, een schoolreglement"],
                ["Narratief", "een verhaal vertellen", "een verslag, een reisverslag, een anekdote"],
                ["Literair", "raken door de esthetische waarde", "een roman, een gedicht, een strip"],
            ])),
            ("kader", "Let op het verschil tussen <strong>persuasief</strong> en "
                      "<strong>argumentatief</strong>. Allebei willen ze je overtuigen, maar een "
                      "persuasieve tekst werkt met gevoel, beeld en herhaling, en een argumentatieve met "
                      "<strong>argumenten die een standpunt dragen</strong>. Een "
                      "<strong>pleidooi</strong>, een <strong>betoog</strong> en een "
                      "<strong>debat</strong> zijn alle drie argumentatief."),
        ]),
        dict(kop="De soorten één voor één", blokken=[
            ("p", "Een <strong>informatieve</strong> tekst wil je <strong>iets laten weten over een "
                  "onderwerp</strong>. Een <strong>interview</strong> is doorgaans informatief. Let op: "
                  "<strong>een tekst met feiten erin is daarom nog geen informatieve tekst</strong>; ook "
                  "een reclamefilmpje en een betoog staan vol feiten."),
            ("p", "Een <strong>prescriptieve</strong> tekst geeft <strong>instructies</strong>. Een "
                  "<strong>recept in een kookboek</strong>, een <strong>instructiefilmpje op YouTube over "
                  "hoe je een fietsband plakt</strong>, een <strong>handleiding bij je telefoon</strong> en "
                  "een <strong>schoolreglement</strong> horen er allemaal bij: <strong>ze zeggen allebei "
                  "wat je moet doen</strong>. Een <strong>folder van de gemeente</strong> die uitlegt hoe "
                  "je je <strong>afval sorteert</strong>, met een <strong>schema per fractie</strong>, is "
                  "ook prescriptief."),
            ("p", "<strong>Narratieve</strong> teksten zijn teksten waarin een verhaal verteld wordt: een "
                  "<strong>reisverslag</strong>, een anekdote, een <strong>true crime podcast</strong>. "
                  "Een <strong>reisverslag en een handleiding horen dus niet bij dezelfde "
                  "tekstsoort</strong>, en een <strong>stukje uit een leerboek is geen narratieve "
                  "tekst</strong> maar een informatieve."),
            ("p", "<strong>Opiniërende</strong> teksten geven een mening: een column, een recensie, een "
                  "<strong>hotelbeoordeling op een online platform</strong>, een "
                  "<strong>productreview</strong>, een <strong>protestlied</strong>, of een "
                  "<strong>reactie op een discussieforum</strong> waarin iemand zegt wat hij ervan "
                  "<strong>vindt</strong>."),
            ("p", "<strong>Persuasieve</strong> teksten <strong>proberen je te overtuigen of te "
                  "beïnvloeden</strong>: een <strong>folder van een politieke partij</strong>, een "
                  "reclamefilmpje, en ook een <strong>publireportage</strong> die <strong>eruitziet als een "
                  "artikel maar betaald</strong> is door een merk. <strong>Propaganda en nepnieuws staan "
                  "bij dezelfde tekstsoort als een reclamefilmpje</strong>: ook zij willen je denken "
                  "sturen."),
            ("p", "Een <strong>literaire</strong> tekst <strong>kenmerkt</strong> zich door de "
                  "<strong>esthetische waarde, die vaak inspeelt op emoties</strong>. Een "
                  "<strong>gedicht over de dood van een grootvader</strong> dat je <strong>raakt</strong>, "
                  "is literair. Ook <strong>een strip kan een literaire tekst zijn</strong>."),
        ]),
        dict(kop="Meer dan één doel tegelijk", blokken=[
            ("p", "<strong>Eén tekst kan meer dan één doel tegelijk hebben.</strong> Een "
                  "<strong>recensie kan tegelijk informatief en opiniërend</strong> zijn. Een "
                  "<strong>opiniestuk</strong> dat betoogt dat de <strong>schooluren later moeten "
                  "beginnen</strong>, met cijfers uit <strong>slaaponderzoek</strong>, is "
                  "<strong>argumentatief, opiniërend én informatief</strong>."),
            ("p", "Een <strong>stand-upcomedian</strong> die vijf <strong>minuten</strong> over zijn jeugd "
                  "vertelt met veel <strong>woordspelingen</strong>, brengt iets dat tegelijk "
                  "<strong>literair</strong> en <strong>narratief</strong> is. Een <strong>essay van een "
                  "filosoof over vriendschap</strong> is <strong>argumentatief, literair én "
                  "opiniërend</strong>: je wijst <strong>daarin</strong> meerdere soorten aan. Lees je een "
                  "<strong>column</strong> die grappig <strong>begint</strong>, een "
                  "<strong>standpunt inneemt</strong> en <strong>eindigt</strong> met een oproep, dan "
                  "<strong>noem je de doelen die je erin terugvindt</strong> in plaats van één etiket te "
                  "kiezen."),
        ]),
        dict(kop="De tekstsoort gebruiken bij het lezen en luisteren", blokken=[
            ("p", "De tekstsoort <strong>bepalen</strong> bij het <strong>lezen</strong> is "
                  "<strong>nuttig</strong>, want <strong>je weet dan wat de schrijver van je wil</strong>. "
                  "De vraag die een persuasieve tekst het best verraadt: <strong>wat wil de zender dat ik "
                  "doe of denk?</strong>"),
            ("p", "<strong>Bij een luistertekst gebruik je dezelfde vragen over zender, doel en publiek "
                  "als bij een leestekst.</strong> Bekijk je een <strong>reportage over de haven van "
                  "Antwerpen</strong> voor een <strong>spreekbeurt</strong>, dan is je eerste vraag "
                  "<strong>wie de reportage maakte en waarom</strong>."),
            ("p", "Pas op met wie er <strong>spreekt</strong>: laat een <strong>fabrikant van "
                  "sportdrank</strong> een <strong>dokter</strong> in een filmpje <strong>uitleggen</strong> "
                  "waarom je moet <strong>bijtanken</strong>, dan <strong>spreekt de dokter, maar is de "
                  "fabrikant de echte zender</strong>. Publiceert een <strong>politieke partij</strong> op "
                  "haar <strong>eigen</strong> site een artikel over hoe andere <strong>partijen</strong> "
                  "de <strong>polarisatie aanwakkeren</strong>, dan lees je dat <strong>als propaganda, "
                  "want de zender heeft er belang bij</strong>."),
            ("p", "Wat zegt de tekstsoort over de <strong>betrouwbaarheid</strong>? <strong>Op zich niets, "
                  "maar ze zet je wel op je hoede.</strong> En <strong>de lees- en luisterteksten op het "
                  "examen zijn niet uitsluitend in het Standaardnederlands</strong>: je kan ook tussentaal "
                  "of dialect te horen krijgen."),
            ("p", "Men raadt aan om vóór het <strong>examen</strong> veel verschillende tekstsoorten te "
                  "<strong>lezen</strong> en te <strong>beluisteren</strong>, want <strong>je leert de vorm "
                  "en de bedoeling sneller herkennen</strong>. Die vraag <strong>helpt</strong> ook "
                  "onderweg: wie de <strong>zender</strong> en zijn bedoeling kent, <strong>herkent</strong> "
                  "de soort meteen."),
        ]),
    ],
    onthoud=[
        "De tekstsoort hangt af van het doel van de zender, niet van het onderwerp.",
        "Zeven tekstsoorten: informatief, persuasief, argumentatief, opiniërend, prescriptief, narratief en literair.",
        "Persuasief werkt met gevoel, beeld en herhaling; argumentatief met argumenten die een standpunt dragen.",
        "Een tekst met feiten erin is daarom nog geen informatieve tekst.",
        "Propaganda en nepnieuws staan bij dezelfde tekstsoort als een reclamefilmpje.",
        "Eén tekst kan meer dan één doel tegelijk hebben: noem de doelen die je erin terugvindt.",
        "Vraag bij lees- en luisterteksten: wat wil de zender dat ik doe of denk?",
        "De tekstsoort zegt op zich niets over de betrouwbaarheid, maar zet je wel op je hoede.",
    ],
)

# ───────────────────────── 2. Onderwerp, hoofdgedachte en samenvatten
BUNDELS["onderwerp-hoofdgedachte-en-samenvatten-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Onderwerp, hoofdgedachte en samenvatten",
    onder="Waar een tekst over gaat, wat hij erover beweert, en hoe je dat in eigen woorden terugbrengt.",
    secties=[
        dict(kop="Onderwerp, hoofdgedachte en hoofdpunten", blokken=[
            ("p", "Het <strong>onderwerp</strong> van een tekst is <strong>waarover de tekst gaat, in één "
                  "of enkele woorden</strong>. De <strong>hoofdgedachte</strong> is <strong>de "
                  "belangrijkste boodschap, in één zin</strong>. <strong>Het onderwerp en de hoofdgedachte "
                  "zijn dus niet hetzelfde.</strong>"),
            ("p", "Gaat een tekst over <strong>sociale</strong> <strong>media</strong> en "
                  "<strong>polarisatie</strong>, dan is dat het onderwerp. <em>Polarisatie wordt "
                  "<strong>versterkt</strong> door sociale media</em> is een hoofdgedachte: het is een hele "
                  "zin met een bewering erin. Zulke <strong>formuleringen</strong> herken je aan het "
                  "werkwoord."),
            ("p", "De <strong>hoofdpunten</strong> van een tekst zijn <strong>alle inhoudelijke elementen "
                  "die de hoofdgedachte ondersteunen</strong>. <strong>Een tekst heeft niet altijd maar één "
                  "hoofdpunt.</strong> De zin <em>Sociale media versterken de polarisatie doordat de "
                  "<strong>algoritmes echokamers creëren</strong></em> is zo'n <strong>hoofdpunt</strong>. "
                  "<strong>Kan je de hoofdpunten opsommen, dan heb je de hoofdgedachte vanzelf ook te "
                  "pakken.</strong>"),
            ("p", "<strong>De hoofdgedachte staat niet altijd in de eerste zin.</strong> Ze kan in de "
                  "inleiding staan, in het slot, of in de titel. Vragen die je helpen ze te vinden: "
                  "<strong>wat wil de schrijver dat ik onthoud</strong>, <strong>welke zin vat de hele "
                  "tekst samen</strong>, en <strong>waar wijzen alle hoofdpunten naartoe</strong>."),
            ("p", "<strong>Hoofd- en bijzaken onderscheiden</strong> betekent <strong>zien wat de kern "
                  "draagt en wat enkel illustreert</strong>."),
        ]),
        dict(kop="Voor en tijdens het lezen", blokken=[
            ("p", "Vóór je begint te lezen, stel je <strong>jezelf</strong> de vragen uit het "
                  "<strong>communicatiemodel</strong>: <strong>van wie is de tekst</strong>, "
                  "<strong>waarom heeft de schrijver de tekst gemaakt</strong>, en <strong>voor wie is de "
                  "tekst bedoeld</strong>. Vraag je ook af wat je al over het onderwerp weet: "
                  "<strong>je voorkennis helpt je de tekst sneller te volgen</strong>."),
            ("p", "<strong>Visuele hulpmiddelen</strong> die je helpen bij het <strong>begrijpen</strong>: "
                  "<strong>de titel en de tussentitels</strong>, <strong>benadrukte woorden</strong>, en "
                  "<strong>een grafiek of een foto bij de tekst</strong>."),
            ("p", "<strong>Signaalwoorden</strong> zijn woorden als <em>maar</em>, <em>dus</em>, <em>ten "
                  "eerste</em> en <em>hoewel</em>: ze <strong>geven de gedachtegang van een tekst "
                  "aan</strong>. Staat er <em><strong>Bovendien</strong> hebben sensationele berichten een "
                  "grotere kans om viraal te gaan</em>, dan verraadt <em>bovendien</em> dat <strong>er nog "
                  "een reden bij komt</strong>. <strong>Verwijswoorden</strong> zoals <em>zij</em>, "
                  "<em>hem</em> en <em>deze</em> <strong>helpen</strong> je eveneens <strong>om de "
                  "gedachtegang te volgen</strong>. Samen <strong>vormen</strong> ze de "
                  "<strong>structuuraanduiders</strong>."),
            ("p", "Kom je een <strong>onbekend</strong> woord tegen dat je niet nodig hebt om de tekst te "
                  "<strong>begrijpen</strong>, dan <strong>lees je door</strong>. En <strong>de betekenis "
                  "van een onbekend woord kan je soms afleiden uit de manier waarop het gevormd is</strong>."),
            ("p", "Moet je uit drie <strong>artikels</strong> de <strong>informatie halen</strong> die je "
                  "voor één vraag nodig hebt, dan <strong>zoek je per tekst wat op die vraag slaat</strong>. "
                  "Dat is een vorm van <strong>systematisch</strong> werken: <strong>je gaat volgens een "
                  "vaste werkwijze te werk</strong>."),
        ]),
        dict(kop="Notities nemen", blokken=[
            ("p", "<strong>Notities</strong> of <strong>noteren</strong> is het kort opschrijven van wat je "
                  "leest of hoort, als voorbereiding op een samenvatting. Goede notities <strong>sluiten "
                  "aan bij de inhoud van de tekst</strong>, zijn <strong>duidelijk genoeg om er daarna mee "
                  "te werken</strong>, en <strong>mogen afkortingen, symbolen en telegramstijl "
                  "bevatten</strong>. Daaraan moeten ze <strong>voldoen</strong>."),
            ("p", "<strong>Je notities hoeven niet leesbaar te zijn voor iemand anders</strong> zonder "
                  "uitleg: ze zijn voor jou. Je mag ze ook <strong>in een schema, een tabel of een mindmap "
                  "zetten</strong>. Het voordeel van een <strong>mindmap</strong> boven een lijstje: "
                  "<strong>je ziet de verbanden tussen de delen staan</strong>."),
            ("p", "Bekijk je een <strong>reportage</strong> en moet je er <strong>nadien</strong> vragen "
                  "over <strong>beantwoorden</strong>, dan <strong>neem</strong> je tijdens het kijken "
                  "<strong>korte notities</strong>. Bij een lange reportage helpen verder: <strong>op de "
                  "beelden letten die bij de uitleg horen</strong> en <strong>op signaalwoorden "
                  "letten</strong>."),
        ]),
        dict(kop="Samenvatten", blokken=[
            ("p", "Een <strong>samenvatting</strong> is een tekst die in minder woorden weergeeft wat er in "
                  "een langere tekst stond. Ze is <strong>korter dan de oorspronkelijke tekst</strong>, ze "
                  "heeft <strong>een duidelijke opbouw en structuur</strong>, en ze <strong>geeft de "
                  "hoofdgedachte en de hoofdpunten weer</strong>. Je maakt die structuur zichtbaar "
                  "<strong>met signaalwoorden</strong>."),
            ("p", "<strong>Je eigen mening over het onderwerp hoort niet in een samenvatting.</strong> En "
                  "<strong>je mag geen zinnen letterlijk uit de oorspronkelijke tekst overnemen</strong>: "
                  "samenvatten doe je in je eigen woorden. <strong>De volgorde van de oorspronkelijke tekst "
                  "mag je wél veranderen</strong> als dat helderder is."),
            ("p", "Moet je duizend woorden terugbrengen tot honderd, dan <strong>sneuvelen de voorbeelden "
                  "en de anekdotes eerst</strong>. Levert iemand een samenvatting in die bijna even lang is "
                  "als het origineel, dan <strong>zijn hoofd- en bijzaken niet gescheiden</strong>."),
            ("p", "Gebruik je je notities om een <strong>opiniërende tekst</strong> te schrijven, dan is "
                  "het verschil met een samenvatting dat <strong>je je eigen standpunt toevoegt</strong>. "
                  "Verwerk je meerdere bronnen, bijvoorbeeld vier teksten over de gezondheidsrisico's van "
                  "vapen, dan <strong>verwijs je er correct naar</strong>."),
        ]),
    ],
    onthoud=[
        "Het onderwerp is waarover de tekst gaat, in één of enkele woorden.",
        "De hoofdgedachte is de belangrijkste boodschap, in één zin.",
        "Hoofdpunten zijn alle inhoudelijke elementen die de hoofdgedachte ondersteunen.",
        "De hoofdgedachte staat niet altijd in de eerste zin.",
        "Signaalwoorden en verwijswoorden samen vormen de structuuraanduiders.",
        "Notities mogen afkortingen, symbolen en telegramstijl bevatten; ze zijn voor jou.",
        "Een samenvatting is korter dan het origineel en geeft de hoofdgedachte en de hoofdpunten weer.",
        "Geen eigen mening en geen letterlijk overgenomen zinnen in een samenvatting.",
    ],
)

# ───────────────────────── 3. Bronnen beoordelen
BUNDELS["bronnen-beoordelen-betrouwbaarheid-nepnieuws-en-framing-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Bronnen beoordelen: betrouwbaarheid, nepnieuws en framing",
    onder="De dertien criteria, en hoe nepnieuws, propaganda, framing en de filterbubbel werken.",
    secties=[
        dict(kop="De dertien criteria", blokken=[
            ("p", "Een bron beoordeel je niet op gevoel. Je loopt een vaste reeks "
                  "<strong>beoordelingscriteria</strong> af. Ze gaan over de zender, over de inhoud en over "
                  "jouw kant van de zaak. <strong>Geen enkel criterium beslist op zichzelf</strong>: je "
                  "<strong>weegt ze samen af</strong>, en <strong>ze gelden ook voor beeld en "
                  "geluid</strong>, niet enkel voor tekst."),
            ("p", tabel(["Vraag", "Waar het over gaat"], [
                ["Wordt de auteur vermeld?", "een naam maakt iemand aanspreekbaar"],
                ["Wie publiceert het?", "een redactie, een bedrijf, een partij, een privépersoon"],
                ["Wat is de bedoeling van de zender?", "informeren, verkopen, overtuigen, werven"],
                ["Heeft de zender belang bij het antwoord?", "wie wint erbij als jij dit gelooft?"],
                ["Wanneer is het gepubliceerd?", "is het nog actueel voor dit onderwerp?"],
                ["Is de informatie correct?", "kloppen de feiten die erin staan?"],
                ["Welke bronnen gebruikt de tekst zelf?", "waarop steunen de beweringen?"],
                ["Is het elders terug te vinden?", "bevestigen onafhankelijke bronnen het?"],
                ["Feiten of meningen?", "een tekst vol meningen levert weinig feitelijke informatie"],
                ["Is de tekst volledig?", "ontbreekt er een kant van het verhaal?"],
                ["Hoe is de toon?", "neutraal, lokkend, oordelend, dreigend"],
                ["Welk kanaal?", "een redactie kijkt na, een sociaal netwerk niet"],
                ["Is het relevant voor mijn doel?", "dit criterium gaat over jou, niet over de tekst"],
            ])),
            ("kader", "Let op de richting van elk criterium. Dat een artikel <strong>geen auteur "
                      "vermeldt</strong>, is een <strong>reden tot wantrouwen, geen bewijs</strong> van "
                      "onwaarheid. Dat een site er <strong>professioneel uitziet</strong>, bewijst "
                      "<strong>niets</strong>; een vormgeving is zo gekocht. Ook een artikel op de site van "
                      "een universiteit is <strong>niet automatisch betrouwbaar</strong>: kijk wie het "
                      "schreef en waarvoor."),
        ]),
        dict(kop="Actualiteit en bevestiging", blokken=[
            ("p", "<strong>Informatie die ouder is dan een paar jaar, is daarom niet onbruikbaar.</strong> "
                  "Voor een historisch onderwerp is een oude tekst vaak juist waardevol. Voor "
                  "<strong>regels die veranderen</strong>, zoals de voorwaarden van een studiebeurs, ga je "
                  "wél na of er sindsdien iets gewijzigd is."),
            ("p", "Dat dezelfde informatie in verschillende <strong>betrouwbare</strong> bronnen opduikt, "
                  "<strong>versterkt haar geloofwaardigheid</strong>. Maar let op: vind je op vijf sites "
                  "<strong>exact dezelfde zinnen</strong>, dan heb je waarschijnlijk <strong>vijf keer "
                  "dezelfde bron</strong> gevonden en geen vijf bevestigingen."),
            ("p", "Kan je de betrouwbaarheid van een bron niet inschatten, dan zoek je een "
                  "<strong>tweede bron</strong> over hetzelfde onderwerp. Bij een anoniem bericht dat "
                  "bijvoorbeeld beweert dat een bekende winkelketen sluit, is je eerste stap "
                  "<strong>kijken of een nieuwsredactie het ook bericht</strong>."),
        ]),
        dict(kop="Nepnieuws, propaganda en reclame", blokken=[
            ("p", "<strong>Nepnieuws</strong> is een bericht dat eruitziet als nieuws maar "
                  "<strong>bewust onwaar</strong> is. Signalen die samen sterk in die richting wijzen: "
                  "<strong>er wordt geen auteur vermeld</strong>, <strong>het bericht circuleert enkel op "
                  "sociale media</strong>, en <strong>de titel is sterk lokkend opgesteld</strong>."),
            ("p", "<strong>Propaganda</strong> wil een <strong>politieke of ideologische overtuiging</strong> "
                  "opdringen en <strong>je denken sturen</strong>. <strong>Reclame</strong> wil "
                  "<strong>je koopgedrag</strong> sturen: ze is er enkel om je iets te doen kopen. Een "
                  "<strong>publireportage</strong> ziet eruit als een artikel maar is betaald, en "
                  "<strong>moet herkenbaar zijn als betaalde inhoud</strong>."),
            ("p", "Een tekst van een <strong>belanghebbende zender</strong>, bijvoorbeeld een minister die "
                  "op de site van zijn partij over het beleid schrijft, lees je als "
                  "<strong>partijcommunicatie</strong>. Dat betekent <strong>niet</strong> dat zo'n tekst "
                  "<strong>per definitie onjuistheden bevat</strong>; het betekent dat je de selectie en de "
                  "toon met een korrel zout neemt."),
            ("p", "Een <strong>anonieme account</strong> die een bericht verspreidt dat je naar een "
                  "onbekende site met veel advertenties lokt, heeft meestal maar één doel: "
                  "<strong>bezoekers naar die site halen</strong>."),
        ]),
        dict(kop="Framing", blokken=[
            ("p", "<strong>Framing</strong> is een onderwerp zo voorstellen dat je het op een bepaalde "
                  "manier ziet. Het gebeurt met <strong>woordkeuze</strong>, met <strong>wat je "
                  "weglaat</strong> en met <strong>beeld</strong>. Voorbeelden: spreken over een "
                  "<em>belastingverlaging</em> of over een <em>besparing</em>, over "
                  "<em>klimaatverandering</em> of over <em>klimaatontwrichting</em>, over een "
                  "<em>vluchteling</em> of over een <em>gelukzoeker</em>."),
            ("p", "Ook hetzelfde cijfer kan in twee frames: <em>een stijging van 3 procent</em> en <em>de "
                  "derde stijging op rij</em> zijn allebei waar, maar roepen iets anders op. Daarom kan "
                  "<strong>een tekst die vol feiten staat, toch een vertekend beeld geven</strong>."),
            ("p", "Een <strong>lokkende</strong> of <strong>sensationele titel</strong> is zo opgesteld dat "
                  "je wel móet doorklikken. Het probleem: <strong>de titel dient het aantal clicks, niet de "
                  "inhoud</strong>. Dat betekent niet dat de titel <strong>altijd een regelrechte "
                  "onwaarheid</strong> bevat."),
            ("p", "<strong>Multimediale elementen</strong> kunnen de boodschap niet enkel versterken maar "
                  "ook <strong>veranderen</strong>: <strong>een grafiek met een afgesneden as</strong> "
                  "(begint de zij-as bij 95 in plaats van bij 0, dan lijkt een klein verschil enorm), "
                  "<strong>een foto die een extreem geval toont</strong>, en <strong>muziek die een "
                  "dreigende sfeer schept</strong>."),
        ]),
        dict(kop="Echokamer, filterbubbel en polarisatie", blokken=[
            ("p", "Een <strong>echokamer</strong> is een omgeving waarin je vooral <strong>je eigen mening "
                  "terughoort</strong>. Een <strong>filterbubbel</strong> is het verschijnsel dat een "
                  "<strong>algoritme</strong> je vooral toont wat bij je past, waardoor je de rest niet meer "
                  "ziet."),
            ("p", "Daar komt een menselijke neiging bij: <strong>een bericht dat jouw mening bevestigt, kijk "
                  "je minder streng na dan een bericht dat haar tegenspreekt</strong>. Wie dat van zichzelf "
                  "weet, leest scherper."),
            ("p", "<strong>Anonimiteit</strong> op sociale media voedt de <strong>polarisatie</strong>: "
                  "<strong>wie niet herkend wordt, schrijft harder</strong> dan hij tegenover iemand zou "
                  "spreken."),
            ("kader", "Bij het beoordelen van een <strong>luistertekst</strong> gelden "
                      "<strong>dezelfde criteria</strong> als bij een leestekst. Zender, doel, kanaal en "
                      "volledigheid veranderen niet omdat de boodschap klinkt in plaats van staat."),
        ]),
    ],
    onthoud=[
        "Geen enkel criterium beslist op zichzelf: je weegt ze samen af.",
        "Geen auteur vermeld is een reden tot wantrouwen, geen bewijs van onwaarheid.",
        "Vijf keer exact dezelfde zinnen is waarschijnlijk vijf keer dezelfde bron, geen vijf bevestigingen.",
        "Nepnieuws ziet eruit als nieuws maar is bewust onwaar.",
        "Propaganda wil je denken sturen, reclame je koopgedrag.",
        "Een publireportage ziet eruit als een artikel maar is betaald.",
        "Framing stuurt hoe je een onderwerp ziet, via woordkeuze, wat je weglaat en beeld.",
        "Een filterbubbel ontstaat doordat een algoritme je vooral toont wat bij je past.",
        "Voor een luistertekst gelden dezelfde criteria als voor een leestekst.",
    ],
)

# ───────────────────────── 4. Het communicatiemodel en ruis
BUNDELS["het-communicatiemodel-en-ruis-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Het communicatiemodel en ruis",
    onder="Zender, boodschap, ontvanger, kanaal, context, doel en effect, en alles wat ertussen kan komen.",
    secties=[
        dict(kop="De onderdelen van het model", blokken=[
            ("p", "Het <strong>communicatiemodel</strong> ontleedt elke boodschap in vaste onderdelen. Je "
                  "gebruikt het bij <strong>lezen, luisteren, schrijven en spreken</strong>: elke boodschap "
                  "heeft een zender en een ontvanger, en daarom staat het model op <strong>beide delen van "
                  "het vak</strong>. Het geldt dus <strong>niet enkel bij geschreven teksten</strong>."),
            ("p", tabel(["Onderdeel", "Wat het is"], [
                ["Zender", "wie de boodschap maakt en verstuurt"],
                ["Boodschap", "wat er precies overgebracht wordt"],
                ["Ontvanger", "degene voor wie de boodschap bedoeld is"],
                ["Kanaal", "het middel waarlangs ze verspreid wordt: een mail, een blog, een affiche"],
                ["Context", "de omstandigheden waarin de boodschap gegeven wordt"],
                ["Doel", "wat de zender wil bereiken"],
                ["Effect", "wat de boodschap bij de ontvanger teweegbrengt"],
            ])),
            ("p", "Een <strong>zender kan ook een organisatie zijn</strong> en niet enkel een persoon: een "
                  "bedrijf, een partij, een redactie. En een <strong>zender kan tegelijk ontvanger "
                  "zijn</strong>, zodra het een gesprek wordt. Zegt een leerkracht tegen een klas <em>mooi "
                  "werk</em>, dan is <strong>de klas</strong> de ontvanger."),
        ]),
        dict(kop="Doel is niet hetzelfde als effect", blokken=[
            ("p", "<strong>Het doel en het effect van een boodschap zijn niet hetzelfde.</strong> Het doel "
                  "zit bij de zender, het effect bij de ontvanger. Ze vallen vaak maar niet altijd samen."),
            ("p", "Gevallen waarin het effect afwijkt van het doel: <strong>een waarschuwing die mensen doet "
                  "lachen</strong>, <strong>een grap die iemand kwetst</strong>, <strong>een uitleg die de "
                  "ontvanger niet begrijpt</strong>. Ook een reclamespot die wil dat je iets koopt terwijl "
                  "jij enkel het liedje onthoudt, is zo'n geval."),
            ("p", "<strong>Dezelfde boodschap kan bij twee ontvangers een verschillend effect hebben.</strong> "
                  "Daarom vraag je je bij elke lees- en luisteropdracht af <strong>wie de ontvanger is</strong>: "
                  "de doelgroep verklaart de toon en de woordkeuze."),
        ]),
        dict(kop="Kanaal en context", blokken=[
            ("p", "De vraag <strong>via welk kanaal?</strong> hoort bij het beoordelen van een bericht, want "
                  "<strong>het kanaal zegt iets over de bedoeling van de zender</strong>. Verschijnt een "
                  "nieuwsbericht <strong>enkel via sociale media en nergens anders</strong>, dan heeft "
                  "<strong>geen enkele redactie het nagekeken</strong>."),
            ("p", "Een slecht gekozen kanaal maakt een goede boodschap waardeloos: stuurt een school een "
                  "belangrijke mededeling enkel via een app die de helft van de ouders niet gebruikt, dan "
                  "ligt de fout bij <strong>het kanaal</strong>."),
            ("p", "De <strong>context</strong> zijn de omstandigheden: de relatie tussen zender en "
                  "ontvanger, het moment, de plaats, wat eraan voorafging. Een mail van een bedrijf aan al "
                  "zijn klanten over een prijsstijging heeft als context <strong>de zakelijke relatie en het "
                  "moment van versturen</strong>. Staat een filmpje over een ernstig onderwerp tussen "
                  "grappige filmpjes op een platform, dan speelt <strong>de context waarin de boodschap "
                  "landt</strong> mee."),
            ("p", "Een <strong>affiche zonder afzender</strong> die je oproept om op iets te stemmen, valt "
                  "meteen op: <strong>de zender blijft verborgen</strong>. Ook <strong>emoji's horen bij de "
                  "boodschap</strong>: ze dragen betekenis, net als de woorden."),
        ]),
        dict(kop="Ruis", blokken=[
            ("p", "<strong>Ruis</strong> is alles wat de overdracht van een boodschap verstoort. Ze "
                  "<strong>zit niet altijd bij de ontvanger</strong>: ook de zender kan ze veroorzaken."),
            ("p", "<strong>Externe ruis</strong> is een storing <strong>van buitenaf</strong> die de "
                  "boodschap hindert: <strong>een haperende videoverbinding</strong>, <strong>een drilboor "
                  "voor het raam van het lokaal</strong>, <strong>een slecht leesbaar lettertype op een "
                  "affiche</strong>, lawaai in een café."),
            ("p", "<strong>Interne ruis</strong> zit <strong>in de persoon zelf</strong>: piekeren over een "
                  "ruzie, vermoeidheid, verstrooidheid, of te weinig voorkennis. <strong>Onbekend vakjargon "
                  "in een tekst kan voor de lezer als ruis werken</strong>. In één situatie kunnen beide "
                  "soorten tegelijk spelen: een luidruchtig café <em>en</em> een hoofd vol zorgen."),
            ("p", "Een zender beperkt <strong>externe ruis</strong> door <strong>een rustiger moment of "
                  "kanaal te kiezen</strong>. Interne ruis beperkt hij door rekening te houden met zijn "
                  "ontvanger. Legt een verpleegkundige in vaktaal uit wat een uitslag betekent en knikt de "
                  "patiënt zonder iets te begrijpen, dan <strong>hield de zender geen rekening met de "
                  "ontvanger</strong>."),
            ("kader", "<strong>Komt de boodschap niet aan, dan ligt dat niet altijd aan de "
                      "ontvanger.</strong> Zender, kanaal, context en boodschap zijn even goed kandidaat. "
                      "Het model is er net om die vraag open te houden."),
            ("p", "Het model is ook een <strong>schrijfstrategie</strong>: voor je een mail aan een "
                  "onbekende instantie schrijft, vraag je jezelf af <strong>wat wil ik bereiken en wie "
                  "leest dit</strong>. En wanneer je een bericht als nepnieuws herkent omdat er geen auteur "
                  "bij staat en het enkel op sociale media rondgaat, gebruik je drie onderdelen van het "
                  "model tegelijk: <strong>de zender, het kanaal en het doel</strong>."),
        ]),
    ],
    onthoud=[
        "Het model: zender, boodschap, ontvanger, kanaal, context, doel en effect.",
        "Het model geldt bij lezen, luisteren, schrijven en spreken.",
        "Een zender kan ook een organisatie zijn, en tegelijk ontvanger in een gesprek.",
        "Het doel zit bij de zender, het effect bij de ontvanger.",
        "Het kanaal zegt iets over de bedoeling van de zender.",
        "Externe ruis komt van buitenaf, interne ruis zit in de persoon zelf.",
        "Komt de boodschap niet aan, dan ligt dat niet altijd aan de ontvanger.",
    ],
)

# ───────────────────────── 5. Tekstopbouw, alineaverbanden en structuuraanduiders
BUNDELS["tekstopbouw-alineaverbanden-en-structuuraanduiders-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Tekstopbouw, alineaverbanden en structuuraanduiders",
    onder="De IMS-structuur, de verbanden tussen alinea's, de signaal- en verwijswoorden en de negen vaste tekststructuren.",
    secties=[
        dict(kop="De IMS-structuur", blokken=[
            ("p", "De drie letters van de <strong>IMS-structuur</strong> staan voor "
                  "<strong>inleiding, midden en slot</strong>. Elke goed gestructureerde tekst heeft die "
                  "drie delen, hoe kort of hoe lang hij ook is."),
            ("p", "Een goede <strong>inleiding</strong> <strong>zet het onderwerp neer en wekt "
                  "interesse</strong>. Het <strong>midden</strong> is het deel waarin de "
                  "<strong>deelonderwerpen uitgewerkt</strong> worden. In het <strong>slot</strong> vind je "
                  "doorgaans <strong>het besluit</strong>."),
            ("p", "Eén <strong>alinea</strong> behandelt <strong>één</strong> deelonderwerp. Een nieuwe "
                  "gedachte betekent een nieuwe alinea. Een <strong>tekst zonder enige alinea-indeling leest "
                  "niet even vlot</strong> als een tekst met alinea's."),
            ("p", "Wat een tekst mee opbouwt: <strong>tussentitels</strong> (ze maken een tekst "
                  "toegankelijker), <strong>paragrafen</strong> en <strong>witregels tussen de delen</strong>. "
                  "Een <strong>goede lay-out</strong> zegt op zichzelf echter <strong>niets over de "
                  "inhoud</strong>."),
        ]),
        dict(kop="Verbanden tussen alinea's", blokken=[
            ("p", "Tussen twee alinea's ligt altijd een <strong>verband</strong>. Je herkent het aan de "
                  "eerste woorden van de nieuwe alinea."),
            ("p", tabel(["Verband", "Herkenbaar aan", "Voorbeeld"], [
                ["Tegenstellend", "daar staat tegenover, maar, toch", "eerst de kosten, dan de baten"],
                ["Oorzakelijk", "daardoor, als gevolg daarvan", "de oorzaak en wat eruit volgde"],
                ["Redengevend", "want, omdat, immers", "de reden achter een bewering"],
                ["Concluderend", "daarom besloot, dus, kortom", "wat men uit het vorige afleidde"],
                ["Voorwaardelijk", "als, indien, op voorwaarde dat", "wat er geldt in welk geval"],
                ["Chronologisch", "in 1950, daarna, vervolgens", "1950, dan 1970, dan 2000"],
                ["Doel-middel", "om dat te bereiken, daartoe", "wat men deed om iets te halen"],
                ["Opsommend", "ten eerste, ten tweede, tot slot", "punten na elkaar"],
                ["Vergelijkend", "net als, in tegenstelling tot", "twee zaken naast elkaar"],
            ])),
            ("p", "Een tekst die eerst de <strong>voordelen</strong> en daarna de <strong>nadelen</strong> "
                  "behandelt, gebruikt dus een herkenbaar alineaverband: een tegenstellend."),
        ]),
        dict(kop="Structuuraanduiders", blokken=[
            ("p", "<strong>Structuuraanduiders</strong> zijn <strong>verwijswoorden en signaalwoorden "
                  "samen</strong>. Ze maken de draad van een tekst zichtbaar."),
            ("p", "<strong>Verwijswoorden</strong> zijn woorden als <em>zij</em>, <em>hem</em>, "
                  "<em>deze</em> en <em>hun</em>: ze slaan terug op iets wat eerder genoemd werd. "
                  "<strong>Signaalwoorden</strong> zijn woorden als <em>maar</em>, <em>dus</em>, "
                  "<em>hoewel</em> en <em>bovendien</em>: ze geven het verband aan. <em>Want</em> wijst op "
                  "een <strong>redengevend</strong> verband."),
            ("p", "<strong>Ten eerste, ten tweede en tot slot</strong> wijzen <strong>niet</strong> op een "
                  "tegenstellend verband maar op een <strong>opsommend</strong> verband. In een instructie "
                  "staan ze zo vaak omdat <strong>de volgorde van de stappen duidelijk moet zijn</strong>."),
            ("kader", "<strong>Hetzelfde signaalwoord kan in twee teksten een ander verband "
                      "aangeven.</strong> <em>Dus</em> kan concluderend zijn, maar ook gewoon de draad "
                      "oppakken. Lees het verband dus af van de inhoud, niet alleen van het woord."),
            ("p", "Waarom je bij het lezen op structuuraanduiders let: <strong>je reconstrueert zo de "
                  "gedachtegang</strong> van de schrijver, ook als de inhoud zelf moeilijk is."),
        ]),
        dict(kop="De negen vaste tekststructuren", blokken=[
            ("p", tabel(["Structuur", "Waaraan je ze herkent"], [
                ["Probleemstructuur", "een probleem, de oorzaken en mogelijke oplossingen"],
                ["Maatregelstructuur", "een probleem, en daarna wat de overheid of een instantie moet doen"],
                ["Vergelijkingsstructuur", "twee zaken naast elkaar op dezelfde punten"],
                ["Evaluatiestructuur", "een oordeel, afgewogen op meerdere criteria"],
                ["Argumentatiestructuur", "argumenten voor een standpunt, tegenargumenten weerlegd"],
                ["Verklaringsstructuur", "uitleg over hoe iets in elkaar zit of waarom iets gebeurt"],
                ["Handelingsstructuur", "een stappenplan, in de volgorde van de handeling"],
                ["Ontwikkelingsstructuur", "hoe iets over een langere periode veranderde"],
                ["Onderzoeksstructuur", "een vraag, een methode, resultaten en een besluit"],
            ])),
            ("p", "Voorbeelden: een recensie van een restaurant die het eten, de bediening en de prijs "
                  "afweegt, volgt de <strong>evaluatiestructuur</strong>. Een artikel over hoe het openbaar "
                  "vervoer in vijftig jaar veranderde, de <strong>ontwikkelingsstructuur</strong>. Een tekst "
                  "die elektrische en benzinewagens naast elkaar zet op prijs, verbruik en onderhoud, de "
                  "<strong>vergelijkingsstructuur</strong>."),
            ("p", "<strong>Eén tekst kan meerdere vaste tekststructuren bevatten.</strong> Een vaste "
                  "structuur gebruiken <strong>helpt je lezer de tekst sneller te volgen</strong>."),
        ]),
        dict(kop="Conventies en beeldmateriaal", blokken=[
            ("p", "Bij een <strong>verslag van een onderzoeksopdracht</strong> hoort "
                  "<strong>academische en objectieve taal</strong>. Bij een <strong>formele e-mail</strong> "
                  "horen <strong>een gepaste aanspreking</strong>, <strong>een verzorgde slotgroet</strong> "
                  "en <strong>correcte spelling en interpunctie</strong>."),
            ("p", "Een <strong>grafiek</strong> bij een tekst <strong>maakt cijfers in één oogopslag "
                  "vergelijkbaar</strong>. Maar <strong>multimediale elementen kunnen de boodschap ook "
                  "veranderen</strong> in plaats van haar enkel te versterken; lees ze dus even kritisch als "
                  "de tekst."),
            ("p", "Wil je snel weten of een tekst nuttig voor je is, bekijk dan eerst <strong>de "
                  "titel</strong>, <strong>de tussentitels</strong> en <strong>het slot</strong>."),
        ]),
    ],
    onthoud=[
        "IMS staat voor inleiding, midden en slot.",
        "Eén alinea behandelt één deelonderwerp.",
        "Het verband tussen alinea's herken je aan de eerste woorden van de nieuwe alinea.",
        "Structuuraanduiders zijn verwijswoorden en signaalwoorden samen.",
        "Ten eerste, ten tweede en tot slot wijzen op een opsommend verband.",
        "Hetzelfde signaalwoord kan in twee teksten een ander verband aangeven.",
        "Er zijn negen vaste tekststructuren; één tekst kan er meerdere bevatten.",
        "Multimediale elementen kunnen de boodschap ook veranderen; lees ze even kritisch als de tekst.",
    ],
)

# ───────────────────────── 6. Argumentatie en drogredenen
BUNDELS["argumentatie-en-drogredenen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Argumentatie en drogredenen",
    onder="Feit tegenover mening, stelling, argument en conclusie, de soorten argumentatie en de bekendste drogredenen.",
    secties=[
        dict(kop="Feit en mening", blokken=[
            ("p", "Een <strong>feit</strong> kan je nagaan; een <strong>mening</strong> niet. <em>Antwerpen "
                  "heeft meer inwoners dan Gent</em> is een feit: het staat vast of het klopt. <em>Dit boek "
                  "is veel te langdradig</em> is een mening."),
            ("p", "Herken een mening aan oordelende woorden en aan werkwoorden als <em>moeten</em>: een zin "
                  "met <strong>moeten</strong> erin is <strong>vaak</strong> een mening. <em>De schooldag "
                  "zou later moeten beginnen</em> en <em>jongeren slapen te weinig voor hun eigen bestwil</em> "
                  "zijn allebei meningen."),
            ("p", "<strong>Een mening is niet minder waard dan een feit</strong> en hoort wel degelijk in "
                  "een tekst thuis. Een opiniestuk bestaat er zelfs uit. Feiten en meningen uit elkaar "
                  "houden is nuttig omdat <strong>je dan ziet waarop de redenering echt steunt</strong>."),
        ]),
        dict(kop="Stelling, standpunt, argument, conclusie", blokken=[
            ("p", "De <strong>stelling</strong> is de bewering waarover de discussie gaat en die je wil "
                  "verdedigen. Je <strong>standpunt</strong> is de positie die je tegenover die stelling "
                  "inneemt, voor of tegen. Een <strong>argument</strong> is een reden die je aanvoert om je "
                  "standpunt te onderbouwen. Een <strong>tegenargument</strong> is een reden die tegen jouw "
                  "standpunt pleit."),
            ("p", "Voorbeeld: <em>Scholen moeten later beginnen</em> is de <strong>stelling</strong>; "
                  "<em>uit onderzoek blijkt dat tieners pas later in slaap vallen</em> is een "
                  "<strong>argument</strong>. En <em>de bibliotheek moet langer open omdat veel studenten "
                  "er 's avonds werken</em>: dat laatste stuk is het argument."),
            ("p", "Een goed opgebouwde argumentatieve tekst bevat <strong>een duidelijke stelling</strong>, "
                  "<strong>argumenten die de stelling dragen</strong> en <strong>een conclusie die eruit "
                  "volgt</strong>. Het <strong>verschil tussen stelling en conclusie</strong>: de stelling "
                  "opent, de conclusie sluit af. <strong>De conclusie hoort te volgen uit de argumenten die "
                  "eraan voorafgaan.</strong>"),
            ("p", "Wat maakt een argument sterk? Het is <strong>waar, ter zake en belangrijk genoeg</strong>. "
                  "Die drie samen: <strong>een argument dat waar is, is daarom nog niet relevant</strong> "
                  "voor de stelling. Zelf <strong>tegenargumenten noemen</strong> in je betoog is sterk, "
                  "want <strong>je toont dat je de andere kant kent en weerlegt</strong>. Je weerlegt een "
                  "tegenargument door <strong>te tonen waarom het niet opgaat</strong>."),
            ("kader", "In een debat luister je <strong>niet enkel naar je eigen argumenten</strong>. Wie "
                      "niet luistert, kan niet weerleggen. Hoor je een uitspraak als <em>deze maatregel is "
                      "onrechtvaardig</em>, dan is de beste reactie <strong>vragen op welke argumenten ze "
                      "steunt</strong>."),
        ]),
        dict(kop="Soorten argumentatie", blokken=[
            ("p", tabel(["Soort", "Voorbeeld"], [
                ["Op basis van wetenschappelijk onderzoek", "uit een studie bij drieduizend leerlingen blijkt dat later beginnen de resultaten verbetert"],
                ["Op basis van cijfers en statistieken", "in zeven op de tien gemeenten daalde het cijfer"],
                ["Op basis van een autoriteit", "een bekende acteur beweert in een spot dat een middel helpt"],
                ["Op basis van vergelijking", "in Finland werkt dit al jaren, dus bij ons zal het ook werken"],
                ["Op basis van oorzaak en gevolg", "door de maatregel daalde het aantal ongevallen"],
                ["Op basis van een voorbeeld", "in onze school zagen we precies hetzelfde gebeuren"],
            ])),
            ("p", "<strong>Argumenteren met cijfers is niet altijd betrouwbaar.</strong> Cijfers kunnen "
                  "onvolledig zijn, uit hun verband gehaald of op een vertekende manier getoond. Bij een "
                  "argument dat naar <strong>onderzoek</strong> verwijst, vraag je: <strong>wie voerde het "
                  "onderzoek uit</strong>, <strong>hoeveel mensen namen eraan deel</strong> en <strong>wie "
                  "heeft het onderzoek betaald</strong>."),
            ("p", "<strong>Argumentatie op basis van oorzaak en gevolg vraagt dat het verband ook echt "
                  "bestaat.</strong> Steeg in een gemeente zowel het aantal ooievaars als het aantal "
                  "geboorten, dan is er <strong>samenhang, maar geen bewezen oorzaak</strong>."),
        ]),
        dict(kop="Drogredenen", blokken=[
            ("p", "Een <strong>drogreden</strong> is een redenering die op het eerste gezicht klopt maar bij "
                  "nader inzien niet deugt."),
            ("p", tabel(["Drogreden", "Hoe ze klinkt", "Wat eraan schort"], [
                ["Persoonlijke aanval", "jij hebt daar geen verstand van, dus je hebt ongelijk", "de persoon wordt aangevallen in plaats van zijn argument"],
                ["Beroep op de massa", "iedereen vindt dit, dus het klopt", "dat velen iets vinden maakt het nog niet waar"],
                ["Hellend vlak", "als we dit toelaten, staan we morgen voor de afgrond", "een reeks gevolgen wordt verondersteld zonder bewijs"],
                ["Beroep op traditie", "dit is altijd zo geweest, dus het moet zo blijven", "ouderdom is geen reden"],
                ["Vals dilemma", "ofwel ben je voor, ofwel ben je tegen ons", "er wordt gedaan alsof er maar twee mogelijkheden zijn"],
                ["Cirkelredenering", "het is waar, want het staat er", "de stelling zelf dient als argument voor die stelling"],
                ["Ontwijken", "antwoorden met een verhaal over iets anders", "de vraag wordt ontweken in plaats van beantwoord"],
            ])),
            ("p", "Ook <em>dat zegt iemand die zelf nooit op tijd komt</em> is een drogreden: opnieuw een "
                  "persoonlijke aanval. Wil je in je eigen betoog drogredenen vermijden, controleer dan "
                  "<strong>of elk argument echt over de stelling gaat</strong>."),
        ]),
    ],
    onthoud=[
        "Een feit kan je nagaan, een mening niet.",
        "Een mening is niet minder waard dan een feit.",
        "De stelling opent, de conclusie sluit af en volgt uit de argumenten.",
        "Een sterk argument is waar, ter zake en belangrijk genoeg.",
        "Je weerlegt een tegenargument door te tonen waarom het niet opgaat.",
        "Argumenteren met cijfers is niet altijd betrouwbaar.",
        "Samenhang is nog geen bewezen oorzaak.",
        "Een drogreden klopt op het eerste gezicht maar deugt bij nader inzien niet.",
        "Een persoonlijke aanval valt de persoon aan in plaats van zijn argument.",
    ],
)

# ───────────────────────── 7. Literaire begrippen en genres
BUNDELS["literaire-begrippen-en-genres-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Literaire begrippen en genres",
    onder="Fictie en non-fictie, de drie hoofdgroepen, de verhalende genres en de vormen van humor.",
    secties=[
        dict(kop="Fictie, non-fictie en de drie hoofdgroepen", blokken=[
            ("p", "<strong>Fictie is verzonnen, non-fictie gaat over de werkelijkheid.</strong> "
                  "<strong>Literaire non-fictie</strong> is dus <strong>geen tegenspraak</strong>: een "
                  "reportage of een essay kan met literaire middelen geschreven zijn en toch over de "
                  "werkelijkheid gaan."),
            ("p", "De literatuur kent drie <strong>hoofdgroepen</strong>: de <strong>epiek</strong> (het "
                  "verhalende: de roman, de novelle, het kortverhaal), de <strong>lyriek</strong> (de "
                  "poëzie) en de <strong>dramatiek</strong> (het toneel). <strong>Proza</strong> is alle "
                  "tekst die niet in versvorm geschreven is."),
            ("p", "De <strong>gelaagdheid</strong> van een tekst betekent dat er "
                  "<strong>verschillende betekenislagen</strong> in zitten: je kan hem op meer dan één "
                  "manier lezen. De <strong>canon</strong> is de reeks werken die als belangrijk beschouwd "
                  "wordt. Een <strong>novelle</strong> is <strong>korter</strong> dan een roman, niet "
                  "langer."),
            ("p", "De juiste literaire term gebruiken loont: <strong>je zegt in één woord wat anders een "
                  "alinea kost</strong>."),
        ]),
        dict(kop="Korte en mondeling overgeleverde genres", blokken=[
            ("p", tabel(["Genre", "Wat het is"], [
                ["Aforisme", "een kort, kernachtig uitgedrukte levenswijsheid in één of twee zinnen"],
                ["Fabel", "een kort verhaal waarin dieren optreden en waar een les in zit"],
                ["Parabel", "een kort verhaal dat een geestelijke waarheid uitlegt aan de hand van een alledaags beeld"],
                ["Mythe", "een verhaal over goden en het ontstaan van de wereld, mondeling doorgegeven"],
                ["Sage", "een verhaal rond een plaats of een persoon, mondeling doorgegeven"],
                ["Volkssprookje", "een sprookje zonder bekende auteur, mondeling doorgegeven"],
                ["Cultuursprookje", "een sprookje dat wél door een bekende auteur geschreven is"],
                ["Epos", "een lang verhalend gedicht over de daden van een held"],
                ["Raamvertelling", "een verhaal in een verhaal, waarbij het ene de andere omsluit"],
                ["Allegorie", "een verhaal waarin alles voor iets anders staat"],
            ])),
            ("p", "Een <strong>stadssage</strong> of <strong>broodjeaapverhaal</strong> wordt verteld "
                  "<strong>alsof het echt gebeurd is</strong>, meestal met een kennis van een kennis als "
                  "bron. Het verschil tussen een volks- en een cultuursprookje zit dus in de auteur."),
        ]),
        dict(kop="Humor", blokken=[
            ("p", "Men onderscheidt <strong>situatiehumor</strong> (het komische zit in wat er gebeurt), "
                  "<strong>taalhumor</strong> (het zit in de woorden, bijvoorbeeld in een woordspeling) en "
                  "<strong>zwarte humor</strong> (lachen met wat eigenlijk pijnlijk of gruwelijk is)."),
            ("p", "<strong>Ironie</strong> is het tegenovergestelde zeggen van wat je bedoelt. "
                  "<strong>Sarcasme en ironie zijn niet precies hetzelfde</strong>: sarcasme is ironie die "
                  "bijt, bedoeld om iemand te raken."),
            ("p", "Een <strong>parodie</strong> imiteert een stijl om er de draak mee te steken; een "
                  "<strong>satire</strong> hekelt een misstand. Een parodie mikt op de vorm, een satire op "
                  "de wereld."),
        ]),
        dict(kop="Romangenres", blokken=[
            ("p", tabel(["Genre", "Wat het is"], [
                ["Bildungsroman", "een roman over het opgroeien van een personage"],
                ["Briefroman", "een roman die volledig uit brieven bestaat"],
                ["Sleutelroman", "een roman waarin echte personen achter de verzonnen personages staan"],
                ["Tendensroman", "een roman die een maatschappelijk standpunt wil uitdragen"],
                ["Autobiografische roman", "een roman waarin de schrijver zijn eigen leven verwerkt"],
                ["Psychologische roman", "een roman die vooral de binnenwereld van een personage onderzoekt"],
                ["Historische roman", "een roman die in het verleden speelt"],
                ["Dystopische roman", "een roman over een samenleving die is misgelopen"],
                ["Gothic novel", "een roman met een duistere sfeer, oude gebouwen en dreiging"],
                ["Graphic novel", "in het Nederlands een striproman"],
                ["Whodunit", "een detectiveroman waarin de vraag draait om wie het gedaan heeft"],
                ["Streekliteratuur", "literatuur die sterk geworteld is in één streek, ook heimatliteratuur"],
                ["Adolescentenliteratuur", "literatuur geschreven voor jongvolwassenen, ook Young Adult"],
            ])),
            ("p", "Een <strong>historische roman moet niet in alle details historisch kloppen</strong>: het "
                  "blijft fictie. En <strong>één roman kan tot meerdere genres tegelijk gerekend "
                  "worden</strong>: een boek kan evengoed een Bildungsroman als een migrantenroman zijn."),
            ("p", "<strong>Migrantenliteratuur</strong> en <strong>multiculturele literatuur</strong> gaan "
                  "over de ervaring van migratie en van het leven tussen meerdere culturen."),
            ("p", "Bij de <strong>middeleeuwse verhaalkunst</strong> horen de <strong>Karelepiek</strong> "
                  "(rond Karel de Grote), de <strong>Arthurroman</strong> (rond koning Arthur en zijn "
                  "ridders) en de <strong>dierenepiek</strong> (verhalen waarin dieren de mensenwereld "
                  "spiegelen)."),
        ]),
    ],
    onthoud=[
        "Fictie is verzonnen, non-fictie gaat over de werkelijkheid.",
        "De drie hoofdgroepen zijn epiek, lyriek en dramatiek.",
        "Een novelle is korter dan een roman, niet langer.",
        "Een volkssprookje heeft geen bekende auteur, een cultuursprookje wel.",
        "Een fabel is een kort verhaal waarin dieren optreden en waar een les in zit.",
        "Sarcasme is ironie die bijt.",
        "Een parodie mikt op de vorm, een satire op de wereld.",
        "Eén roman kan tot meerdere genres tegelijk gerekend worden.",
    ],
)

# ───────────────────────── 8. Verhaalkenmerken en vertelperspectief
BUNDELS["verhaalkenmerken-en-vertelperspectief-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Verhaalkenmerken en vertelperspectief",
    onder="Personages, ruimte, tijd, spanningsboog, thema en motief, en wie het verhaal vertelt.",
    secties=[
        dict(kop="Personages", blokken=[
            ("p", "De <strong>protagonist</strong> is het personage om wie het verhaal draait; de "
                  "<strong>antagonist</strong> is het personage dat hem tegenwerkt. Een "
                  "<strong>antiheld</strong> is een hoofdpersoon <strong>zonder heldhaftige "
                  "eigenschappen</strong>."),
            ("p", "Een <strong>rond personage</strong> verandert in de loop van het verhaal en heeft "
                  "meerdere kanten. Een <strong>vlak personage</strong> blijft zichzelf gelijk; "
                  "<strong>ook een vlak personage kan het hoofdpersonage zijn</strong>. Een "
                  "<strong>type</strong> valt helemaal samen met één eigenschap: de gierigaard, de "
                  "bemoeial."),
        ]),
        dict(kop="Ruimte", blokken=[
            ("p", "Men onderscheidt de <strong>geografische ruimte</strong> (waar het echt speelt), de "
                  "<strong>sociale ruimte</strong> (de maatschappelijke laag van de personages), de "
                  "<strong>symbolische ruimte</strong> (de plaats staat voor iets anders) en de "
                  "<strong>sfeerscheppende</strong> ruimte (de plaats zet de toon)."),
            ("p", "Een <strong>gesloten kamer zonder ramen</strong> duidt dus <strong>niet enkel</strong> "
                  "de echte plaats aan: ze kan evengoed de benauwdheid van een personage uitdrukken. Een "
                  "roman die speelt in <strong>een grauwe mijnstreek met eeuwig regenweer</strong> gebruikt "
                  "de ruimte vooral <strong>sfeerscheppend</strong>."),
            ("p", "Op de ruimte letten loont bij het lezen, want <strong>de ruimte zegt vaak iets over de "
                  "personages</strong>."),
        ]),
        dict(kop="Tijd", blokken=[
            ("p", "De <strong>vertelde tijd</strong> is de duur die het verhaal beslaat; de "
                  "<strong>verteltijd</strong> is de leestijd, de ruimte die de verteller eraan geeft. Is de "
                  "verteltijd veel langer dan de vertelde tijd, dan spreekt men van "
                  "<strong>vertraging</strong>. Vat een hoofdstuk twintig jaar samen in één bladzijde, dan "
                  "is dat <strong>versnelling</strong>."),
            ("p", "Een <strong>flashback</strong> is een sprong naar iets dat eerder gebeurde; een "
                  "<strong>flashforward</strong> een sprong vooruit in de tijd. Spelen twee verhaallijnen "
                  "zich op hetzelfde moment af en worden ze om beurten verteld, dan heet dat "
                  "<strong>gelijktijdigheid</strong>."),
            ("p", "Bij de tijd horen verder de <strong>chronologische volgorde</strong> en het "
                  "<strong>verteltempo</strong>. <strong>Een verhaal dat niet chronologisch verteld wordt, "
                  "is daarom niet slecht opgebouwd</strong>; de volgorde is een keuze van de verteller."),
            ("p", "<strong>Epische concentratie</strong> betekent dat het verhaal zich beperkt tot wat "
                  "ertoe doet: alles wat de lijn niet dient, valt weg."),
        ]),
        dict(kop="Opbouw en spanning", blokken=[
            ("p", "<strong>In medias res</strong> betekent dat het verhaal <strong>middenin de "
                  "gebeurtenissen begint</strong>. De <strong>spanningsboog</strong> bestaat uit de "
                  "<strong>expositie</strong> (de uitgangssituatie), de <strong>stijgende actie</strong>, de "
                  "<strong>climax</strong> (het hoogtepunt van de spanning) en de "
                  "<strong>ontknoping</strong>."),
            ("p", "Een <strong>cliffhanger</strong> is een hoofdstuk dat afbreekt op het spannendste "
                  "moment, bijvoorbeeld net als de deur opengaat. De <strong>pointe</strong> is de "
                  "onverwachte wending op het einde. Een <strong>open einde</strong> laat de lezer met "
                  "vragen achter. Een <strong>cyclische structuur</strong> betekent dat het verhaal eindigt "
                  "waar het begon, dus juist <strong>niet</strong> dat het strikt chronologisch verteld "
                  "wordt."),
        ]),
        dict(kop="Thema, motief en symbool", blokken=[
            ("p", "Het <strong>thema</strong> is waar het verhaal over gaat; een <strong>motief</strong> is "
                  "iets dat <strong>terugkeert</strong>: een voorwerp, een beeld, een zin. Een "
                  "<strong>motto</strong> is een citaat dat vooraan in het boek staat. Een "
                  "<strong>symbool</strong> is een concreet ding dat voor iets abstracts staat."),
            ("p", "<strong>Intertekstualiteit</strong> betekent dat een tekst naar een andere tekst "
                  "verwijst. <strong>Spleen</strong> is een zware, doelloze zwaarmoedigheid. De "
                  "<strong>tijdsgeest</strong> in een werk is de denkwijze en de sfeer van de tijd waarin "
                  "het ontstond."),
        ]),
        dict(kop="Vertelperspectief", blokken=[
            ("p", tabel(["Perspectief", "Wat het betekent"], [
                ["Ik-verteller", "een personage vertelt zelf, in de ik-vorm"],
                ["Belevende ik", "de ik staat middenin de gebeurtenissen"],
                ["Vertellende ik", "de ik kijkt terug op wat gebeurd is"],
                ["Auctoriële verteller", "staat buiten het verhaal, weet alles en geeft soms commentaar"],
                ["Personale verteller", "je kijkt mee over de schouder van één personage"],
                ["Onbetrouwbare verteller", "de verteller verzwijgt of verdraait dingen"],
                ["Meervoudig perspectief", "verschillende personages vertellen om beurten"],
            ])),
            ("p", "<strong>Een ik-verteller weet niet altijd wat alle andere personages denken</strong>; "
                  "dat is net het verschil met de auctoriële verteller. Merk je gaandeweg dat de ik-figuur "
                  "dingen verzwijgt of verdraait, dan heb je te maken met de "
                  "<strong>onbetrouwbare verteller</strong>."),
            ("p", "De <strong>monologue intérieur</strong> is de weergave van de ononderbroken "
                  "gedachtestroom van een personage, zonder dat een verteller ertussen komt."),
        ]),
    ],
    onthoud=[
        "De protagonist is het personage om wie het verhaal draait, de antagonist werkt hem tegen.",
        "Een rond personage verandert, een vlak personage blijft zichzelf gelijk.",
        "De ruimte kan geografisch, sociaal, symbolisch of sfeerscheppend zijn.",
        "Vertelde tijd is de duur van het verhaal, verteltijd is de leestijd.",
        "In medias res betekent middenin de gebeurtenissen beginnen.",
        "Spanningsboog: expositie, stijgende actie, climax en ontknoping.",
        "Een motief keert terug; een symbool is een concreet ding dat voor iets abstracts staat.",
        "Een ik-verteller weet niet altijd wat alle andere personages denken.",
        "De auctoriële verteller staat buiten het verhaal en weet alles.",
    ],
)

# ───────────────────────── 9. Poëzie
BUNDELS["poezie-dichtvormen-strofen-en-rijm-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Poëzie: dichtvormen, strofen en rijm",
    onder="De vaste vormen, de strofen, de rijmsoorten en wat klank en wit met een gedicht doen.",
    secties=[
        dict(kop="Dichtvormen", blokken=[
            ("p", tabel(["Vorm", "Wat ze is"], [
                ["Sonnet", "een gedicht van veertien verzen, met een wending"],
                ["Haiku", "een gedicht van drie verzen, van vijf, zeven en vijf lettergrepen"],
                ["Limerick", "een kort, grappig gedicht van vijf verzen met een vast rijmschema en een onverwachte afloop"],
                ["Ode", "een lofzang"],
                ["Elegie", "een klaagzang om een verlies"],
                ["Ballade", "een verhalend gedicht, vaak met een refrein"],
                ["Rondeel", "een vorm waarin bepaalde verzen letterlijk terugkeren"],
                ["Acrostichon", "een gedicht waarvan de eerste letters van de verzen samen een woord vormen"],
                ["Minnelied", "een lied waarin een ridder zijn liefde bezingt voor een onbereikbare vrouw"],
                ["Dierendicht", "een gedicht waarin dieren optreden of toegesproken worden"],
            ])),
            ("p", "<strong>Visuele poëzie</strong> is poëzie waarin <strong>de vorm op de bladzijde "
                  "meespeelt</strong>: de woorden tekenen mee wat ze zeggen. "
                  "<strong>Parlandopoëzie</strong> klinkt alsof iemand gewoon aan het praten is. Een "
                  "<strong>envoi</strong> is de korte slotstrofe met een opdracht."),
            ("p", "Mondeling of op een podium gebracht worden vooral <strong>slampoetry</strong>, het "
                  "<strong>minnelied</strong> en de <strong>ballade</strong>. De <strong>stok</strong> of "
                  "<strong>stokregel</strong> is het vers dat in een refrein telkens terugkeert."),
        ]),
        dict(kop="Strofen", blokken=[
            ("p", tabel(["Naam", "Aantal verzen"], [
                ["Distichon", "twee"], ["Terzine", "drie"], ["Kwatrijn", "vier"],
                ["Kwintet", "vijf"], ["Sextet", "zes"], ["Septet", "zeven"], ["Octaaf", "acht"],
            ])),
            ("p", "Een <strong>distichon</strong> telt dus <strong>twee</strong> verzen en geen drie. Een "
                  "sonnet van veertien verzen valt vaak uiteen in een <strong>octaaf</strong> van acht en "
                  "een <strong>sextet</strong> van zes."),
        ]),
        dict(kop="Rijm en klank", blokken=[
            ("p", "<strong>Eindrijm</strong> zijn de laatste klanken van verzen die overeenkomen. "
                  "<strong>Volrijm</strong> is rijm waarbij klinker én medeklinkers overeenkomen, zoals in "
                  "<em>boom</em> en <em>stroom</em>. <strong>Assonantie</strong> is rijm waarbij "
                  "<strong>enkel de klinkers</strong> overeenkomen. <strong>Alliteratie</strong> is "
                  "dezelfde beginklank bij opeenvolgende woorden; een ander woord daarvoor is "
                  "<strong>stafrijm</strong>."),
            ("p", "Bij <strong>mannelijk of staand rijm</strong> ligt de klemtoon op de "
                  "<strong>laatste</strong> lettergreep; bij vrouwelijk of slepend rijm op de voorlaatste."),
            ("p", "Een <strong>rijmschema</strong> noteer je met <strong>letters</strong>, waarbij "
                  "dezelfde letter dezelfde rijmklank aangeeft: <strong>aabb is gepaard rijm</strong>, "
                  "<strong>abba is omarmend rijm</strong>, <strong>abab is gekruist rijm</strong>."),
            ("p", "Begrippen die over <strong>klank</strong> gaan, zijn dus <strong>assonantie</strong>, "
                  "<strong>alliteratie</strong> en <strong>volrijm</strong>. Een gedicht "
                  "<strong>hardop</strong> lezen loont, want <strong>klank en ritme komen pas dan tot hun "
                  "recht</strong>."),
        ]),
        dict(kop="Vorm, ritme en wit", blokken=[
            ("p", "Een <strong>enjambement</strong> is een zin die over de versregel heen doorloopt. In een "
                  "fragment als <em>de wind / draagt wat de bomen / niet meer houden</em> valt op dat "
                  "<strong>de zin over de versgrenzen heen loopt</strong>."),
            ("p", "De <strong>volta</strong> is de <strong>wending</strong> in de gedachtegang, bekend uit "
                  "het sonnet maar ook elders mogelijk. Het <strong>ritme</strong> van een gedicht is de "
                  "afwisseling van <strong>sterke en zwakke lettergrepen</strong>."),
            ("p", "Zet een dichter <strong>één woord alleen op een regel met veel wit eromheen</strong>, "
                  "dan <strong>krijgt dat woord alle aandacht</strong>. <strong>Een gedicht zonder rijm en "
                  "zonder vaste maat bestaat wel degelijk</strong>: vrije verzen zijn al meer dan een eeuw "
                  "gewoon."),
            ("p", "Het <strong>lyrisch subject</strong> is de ik-figuur in een gedicht. Dat is "
                  "<strong>niet automatisch de dichter zelf</strong>, net zomin als een ik-verteller de "
                  "romanschrijver is. Een <strong>semantisch veld</strong> is een groep woorden rond "
                  "hetzelfde betekenisgebied; samen kleuren ze de sfeer van een gedicht."),
        ]),
    ],
    onthoud=[
        "Een sonnet telt veertien verzen, een haiku drie: vijf, zeven en vijf lettergrepen.",
        "Een limerick is een kort, grappig gedicht van vijf verzen.",
        "Distichon twee, terzine drie, kwatrijn vier en octaaf acht verzen.",
        "Volrijm: klinker én medeklinkers komen overeen; assonantie: enkel de klinkers.",
        "Alliteratie is dezelfde beginklank bij opeenvolgende woorden, ook stafrijm genoemd.",
        "Aabb is gepaard, abba omarmend en abab gekruist rijm.",
        "Een enjambement is een zin die over de versregel heen doorloopt.",
        "Het lyrisch subject is niet automatisch de dichter zelf.",
    ],
)

# ───────────────────────── 10. Dramatiek en theatertekens
BUNDELS["dramatiek-en-theatertekens-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Dramatiek en theatertekens",
    onder="De toneelvormen van de middeleeuwen tot nu, en alles op een scène dat betekenis draagt.",
    secties=[
        dict(kop="Waarom dramatiek apart staat", blokken=[
            ("p", "<strong>Dramatiek</strong> is een aparte hoofdgroep naast epiek en lyriek omdat "
                  "<strong>een toneeltekst geschreven is om gespeeld te worden</strong>. Daarom is zo'n "
                  "tekst ook <strong>nooit helemaal af op papier</strong>: <strong>de opvoering voegt een "
                  "hele laag tekens toe</strong>."),
            ("p", "Een <strong>klassiek drama</strong> wordt vaak verdeeld in <strong>bedrijven en "
                  "tonelen</strong>. Een <strong>monoloog</strong> is een toneeltekst waarin één personage "
                  "alleen aan het woord is; een <strong>polyloog</strong> is een gesprek tussen "
                  "<strong>meer dan twee</strong> personages."),
        ]),
        dict(kop="Toneelvormen", blokken=[
            ("p", tabel(["Vorm", "Wat ze is"], [
                ["Tragedie", "de hoofdfiguur gaat onafwendbaar ten onder, vaak door zijn eigen trots"],
                ["Komedie", "in het Nederlands ook het blijspel"],
                ["Klucht", "een kort, grof komisch stuk met veel verwarring en misverstanden"],
                ["Tragikomedie", "een stuk waarin het tragische en het komische samengaan"],
                ["Abel spel", "een ernstig, wereldlijk toneelstuk uit de middeleeuwen"],
                ["Mirakelspel", "een toneelstuk waarin een heilige een wonder verricht"],
                ["Mysteriespel", "een middeleeuws stuk met een religieus onderwerp"],
                ["Moraliteit", "een toneelstuk dat een zedenles uitbeeldt"],
                ["Commedia dell'arte", "de Italiaanse vorm met vaste typen, maskers en veel improvisatie"],
                ["Absurd theater", "de wereld op het toneel heeft geen zinvolle logica"],
                ["Episch theater", "het publiek moet juist afstand houden en nadenken"],
                ["Musical", "zang, dans en tekst dragen samen het verhaal"],
                ["Spoken word", "gesproken poëzie, gebracht voor een publiek"],
            ])),
            ("p", "Het verschil tussen een <strong>klucht</strong> en een <strong>komedie</strong>: "
                  "<strong>de klucht is grover en mikt enkel op de lach</strong>. Het "
                  "<strong>mysteriespel</strong> was <strong>niet</strong> wereldlijk maar religieus; het "
                  "<strong>abel spel</strong> was dat wel."),
            ("p", "<strong>Episch theater wil niet dat het publiek zich volledig inleeft.</strong> Het "
                  "doorbreekt de illusie met opzet: richt een speler zich <strong>plots rechtstreeks tot de "
                  "zaal</strong>, dan past dat bij die traditie. Een masker met een vast, overdreven gezicht "
                  "roept dan weer de <strong>commedia dell'arte</strong> op."),
        ]),
        dict(kop="Theatertekens", blokken=[
            ("p", "<strong>Theatertekens</strong> zijn <strong>alles op het toneel dat betekenis "
                  "draagt</strong>: niet enkel de woorden, maar ook wat je ziet en hoort."),
            ("p", tabel(["Groep", "Tekens"], [
                ["De speler zelf", "mimiek (de uitdrukking op het gezicht), gestiek (de gebaren), fysionomie (het uiterlijk)"],
                ["Stem", "paraverbale tekens: alles aan de stem behalve de woorden zelf"],
                ["Ruimte", "het decor, de belichting, de ruimtegestiek, de proxemiek (de afstand tussen de spelers)"],
                ["Voorwerpen", "rekwisieten: de voorwerpen die spelers op scène hanteren"],
                ["Verschijning", "kostuum, grime, kapsel"],
                ["Geluid", "muziek en geluidseffecten"],
            ])),
            ("p", "Voorbeelden: een <strong>schijnwerper die één personage uitlicht</strong>, kan zijn "
                  "<strong>isolement</strong> uitdrukken. <strong>Donkere kostuums</strong> kunnen de "
                  "mentale toestand van een personage weerspiegelen. Een speler die het hele stuk een "
                  "<strong>versleten koffer</strong> vasthoudt, hanteert een <strong>rekwisiet</strong>. "
                  "Staan twee personages het hele stuk aan weerszijden van de scène, dan wordt "
                  "<strong>de afstand tussen hen zichtbaar gemaakt</strong>."),
            ("kader", "<strong>Sombere muziek onder een scène is wel degelijk een theaterteken</strong>, "
                      "ook al staat ze niet in de tekst. Alles wat de toeschouwer waarneemt, draagt "
                      "betekenis."),
        ]),
        dict(kop="Opvoeringsanalyse", blokken=[
            ("p", "Bij een <strong>opvoeringsanalyse</strong> onderzoek je <strong>hoe de keuzes op scène "
                  "de tekst betekenis geven</strong>. <strong>Een toneeltekst lezen is dus niet hetzelfde "
                  "als een opvoering analyseren</strong>: bij het tweede kijk je naar de regie, de spelers, "
                  "het decor en het licht."),
            ("p", "Zet een regisseur een klassiek stuk in een <strong>hedendaags kantoor</strong>, dan "
                  "<strong>legt die ingreep een verband tussen toen en nu</strong>. Dat is een "
                  "interpretatie, en je kan ze bespreken aan de hand van de theatertekens die ze inzet."),
        ]),
    ],
    onthoud=[
        "Een toneeltekst is geschreven om gespeeld te worden.",
        "In een monoloog is één personage aan het woord, een polyloog telt meer dan twee.",
        "De klucht is grover dan de komedie en mikt enkel op de lach.",
        "Het mysteriespel was religieus, het abel spel wereldlijk.",
        "Episch theater wil niet dat het publiek zich volledig inleeft.",
        "Theatertekens zijn alles op het toneel dat betekenis draagt.",
        "Proxemiek is de afstand tussen de spelers; rekwisieten zijn voorwerpen op scène.",
        "Een opvoeringsanalyse onderzoekt hoe de keuzes op scène de tekst betekenis geven.",
    ],
)

# ───────────────────────── 11. Stijlfiguren en beeldspraak
BUNDELS["stijlfiguren-en-beeldspraak-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Stijlfiguren en beeldspraak",
    onder="Beelden, overdrijvingen, verzwakkingen en zinsbouwfiguren, en wat ze met een tekst doen.",
    secties=[
        dict(kop="Beeldspraak", blokken=[
            ("p", "Bij <strong>beeldspraak</strong> zeg je het ene en bedoel je het andere. Het verschil "
                  "tussen een <strong>vergelijking</strong> en een <strong>metafoor</strong>: "
                  "<strong>in een vergelijking staat een woordje als <em>zoals</em></strong>. <em>Zij is zo "
                  "stil als een steen</em> is een vergelijking; <em>zijn woorden waren messen</em> is een "
                  "metafoor."),
            ("p", tabel(["Stijlfiguur", "Wat ze doet", "Voorbeeld"], [
                ["Metafoor", "het beeld vervangt de zaak", "de voet van de berg, het hart van de stad, de arm van de wet"],
                ["Vergelijking", "het beeld staat naast de zaak, met zoals of als", "zo stil als een steen"],
                ["Personificatie", "iets levenloos krijgt menselijke eigenschappen", "de wind fluisterde door de bomen"],
                ["Synesthesie", "twee zintuigen door elkaar in één beeld", "het schreeuwende geel van de muren"],
                ["Allegorie", "een hele vertelling staat voor iets anders", "elk element verwijst naar iets buiten het verhaal"],
                ["Analogie", "een overeenkomst die iets uitlegt", "een netwerk werkt als een wegenkaart"],
                ["Klanknabootsing", "het woord bootst de klank na", "klets, sis, knars"],
            ])),
            ("p", "<strong>Antropomorfisme</strong> betekent <strong>niet</strong> dat een mens de "
                  "eigenschappen van een dier krijgt, maar omgekeerd: iets niet-menselijks krijgt "
                  "menselijke trekken. Een <strong>associatie</strong> is een woord dat een ander beeld "
                  "oproept. Een <strong>onomatopee</strong> is het andere woord voor klanknabootsing."),
            ("p", "In <em>de zon lachte boven het dorp</em> wijs je twee dingen tegelijk aan: "
                  "<strong>personificatie</strong> en, ruimer, <strong>beeldspraak</strong>. Een reclame die "
                  "een auto <em>een roofdier op vier wielen</em> noemt, gebruikt een "
                  "<strong>metafoor</strong>."),
            ("kader", "<strong>Beeldspraak komt niet enkel in poëzie voor</strong>, en <strong>een metafoor "
                      "kan ook in gewone spreektaal</strong> opduiken: <em>de poot van de tafel</em> merkt "
                      "niemand nog op. Een schrijver gebruikt beeldspraak omdat <strong>een beeld iets "
                      "abstracts voelbaar maakt</strong>."),
        ]),
        dict(kop="Vergroten en verkleinen", blokken=[
            ("p", "Een <strong>hyperbool</strong> is een <strong>overdrijving</strong>: <em>ik sterf van de "
                  "honger</em>. Het omgekeerde bestaat ook. Een <strong>litotes</strong> zegt iets door de "
                  "ontkenning van het tegendeel: <em>dat is niet slecht</em> voor <em>dat is uitstekend</em>, "
                  "of <em>hij is niet van gisteren</em> voor <em>hij is slim</em>."),
            ("p", "Een <strong>understatement</strong> <strong>verkleint</strong> bewust wat eigenlijk "
                  "groot is; het vergroot dus niets uit. Een <strong>eufemisme</strong> verzacht iets "
                  "onaangenaams. <strong>Litotes, understatement en eufemisme</strong> verzwakken samen wat "
                  "er bedoeld wordt."),
        ]),
        dict(kop="Zinsbouw en herhaling", blokken=[
            ("p", tabel(["Stijlfiguur", "Wat ze is"], [
                ["Anafoor", "hetzelfde woord aan het begin van opeenvolgende zinnen"],
                ["Parallellisme", "twee zinnen volgen hetzelfde bouwpatroon"],
                ["Chiasme", "de volgorde van de zinsdelen wordt gespiegeld"],
                ["Antithese", "twee tegengestelde zaken naast elkaar"],
                ["Ellips", "het weglaten van een woord dat de lezer zelf aanvult"],
                ["Retorische vraag", "een vraag zonder dat er een antwoord verwacht wordt"],
                ["Paradox", "een uitspraak die zichzelf lijkt tegen te spreken maar toch een waarheid bevat"],
                ["Woordspeling", "spel met de dubbele betekenis of de klank van een woord"],
            ])),
            ("p", "Een toespraak die drie zinnen na elkaar met <em>wij geloven dat</em> begint, gebruikt een "
                  "<strong>anafoor</strong>. Een krantenkop als <em>veel lawaai, weinig muziek</em> is een "
                  "<strong>antithese</strong>. Een spreker zet een <strong>retorische vraag</strong> in "
                  "omdat <strong>de luisteraar dan zelf het antwoord invult</strong> en zich zo bij de "
                  "redenering betrokken voelt."),
            ("p", "Een <strong>cliché</strong> is een beeld dat door veelvuldig gebruik zijn kracht "
                  "verloren heeft. Het effect ervan in een tekst: <strong>de zin leest vlot maar raakt "
                  "niemand</strong>."),
            ("p", "<strong>Stijlfiguren komen niet enkel in literaire teksten voor.</strong> Reclame, "
                  "politieke toespraken en krantenkoppen zitten er vol mee; vaak werken ze daar zelfs het "
                  "hardst."),
        ]),
    ],
    onthoud=[
        "In een vergelijking staat een woordje als zoals; in een metafoor vervangt het beeld de zaak.",
        "Bij personificatie krijgt iets levenloos menselijke eigenschappen.",
        "Synesthesie zet twee zintuigen door elkaar in één beeld.",
        "Onomatopee is het andere woord voor klanknabootsing.",
        "Een hyperbool overdrijft; een litotes ontkent het tegendeel.",
        "Litotes, understatement en eufemisme verzwakken wat er bedoeld wordt.",
        "Een anafoor is hetzelfde woord aan het begin van opeenvolgende zinnen.",
        "Een antithese zet twee tegengestelde zaken naast elkaar.",
        "Stijlfiguren komen niet enkel in literaire teksten voor.",
    ],
)

# ───────────────────────── 12. Literaire stromingen
BUNDELS["literaire-stromingen-van-de-middeleeuwen-tot-nu-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Literaire stromingen van de middeleeuwen tot nu",
    onder="Van de hoofse literatuur tot het postmodernisme, met de kenmerken waaraan je elke stroming herkent.",
    secties=[
        dict(kop="Hoe je met stromingen omgaat", blokken=[
            ("p", "Een <strong>stroming</strong> is een manier van schrijven die in een bepaalde periode "
                  "overheerst. <strong>Een stroming begint en eindigt niet op een scherp af te lijnen "
                  "jaartal</strong>: ze loopt op en af, en overlapt met de vorige en de volgende. "
                  "<strong>Een schrijver kan ook kenmerken van meerdere stromingen tegelijk "
                  "gebruiken.</strong>"),
            ("p", "De kenmerken kennen loont, want <strong>je plaatst een tekst dan in zijn eigen "
                  "tijd</strong>, en je begrijpt waarom hij doet wat hij doet."),
        ]),
        dict(kop="De middeleeuwen", blokken=[
            ("p", "De <strong>voorhoofse literatuur</strong> is ruwer en gaat over strijd en eer; de "
                  "<strong>hoofse literatuur</strong> is verfijnder en draait om <strong>de verheven liefde "
                  "voor een onbereikbare vrouw</strong>. Een middeleeuws verhaal over Karel de Grote en zijn "
                  "ridders hoort bij de <strong>voorhoofse</strong> traditie."),
            ("p", "De <strong>rederijkers</strong> zijn de leden van de stedelijke dichtersgilden aan het "
                  "einde van de middeleeuwen. Zij organiseerden wedstrijden en schreven volgens strakke "
                  "vormregels."),
        ]),
        dict(kop="De vroegmoderne tijd", blokken=[
            ("p", tabel(["Stroming", "Kenmerk"], [
                ["Renaissance", "teruggrijpen naar de klassieke oudheid"],
                ["Barok", "overvloed, beweging en de vergankelijkheid van alles"],
                ["Verlichting", "de rede, de wetenschap en het eigen oordeel centraal"],
            ])),
            ("p", "Een gedicht dat <strong>de vergankelijkheid van het aardse leven bezingt met rijke "
                  "beelden</strong>, verwacht je in de <strong>barok</strong>."),
        ]),
        dict(kop="De negentiende eeuw", blokken=[
            ("p", "De <strong>romantiek</strong> zette <strong>gevoel en verbeelding</strong> tegenover de "
                  "rede van de verlichting, met een verlangen naar het verre en het verleden. Het "
                  "<strong>realisme</strong> wil <strong>de werkelijkheid weergeven zoals ze is</strong>."),
            ("p", "Het <strong>naturalisme</strong> gaat een stap verder: <strong>afkomst en omgeving "
                  "bepalen het lot van een mens</strong>. Kenmerken: <strong>de hoofdfiguur is vaak nerveus "
                  "of zwak</strong>, <strong>taboeonderwerpen worden niet vermeden</strong>, en "
                  "<strong>erfelijkheid en milieu sturen het verhaal</strong>. <strong>Realisme en "
                  "naturalisme zijn dus niet precies hetzelfde.</strong>"),
            ("p", "Een roman over een arbeidersgezin dat ondanks alle pogingen niet uit de armoede raakt, "
                  "met veel aandacht voor ziekte en drank, hoort bij het <strong>naturalisme</strong>."),
            ("p", "De <strong>Tachtigers</strong> staan voor <strong>kunst om de kunst en de kracht van het "
                  "individu</strong>. Het <strong>impressionisme</strong> geeft <strong>vluchtige "
                  "zintuiglijke indrukken</strong> weer; het <strong>symbolisme</strong> werkt met "
                  "<strong>beelden die naar een diepere, niet rechtstreeks te benoemen werkelijkheid "
                  "verwijzen</strong>."),
        ]),
        dict(kop="De twintigste eeuw", blokken=[
            ("p", tabel(["Stroming", "Kenmerk"], [
                ["Expressionisme", "innerlijke gevoelens uitdrukken door de werkelijkheid te vervormen"],
                ["Vitalisme", "de levenskracht, de energie en het lichaam vieren"],
                ["Surrealisme", "het droombeeld en het onbewuste verkennen"],
                ["Nieuwe zakelijkheid", "een nuchtere, onopgesmukte stijl"],
                ["Existentialisme", "de mens moet zijn eigen betekenis maken"],
                ["Vijftigers", "associatie en experiment met taal en vorm"],
                ["Magisch-realisme", "het wonderlijke dringt de gewone wereld binnen"],
                ["Neorealisme", "juist het alledaagse en gewone als onderwerp"],
                ["Neoromantiek", "een hernieuwde aandacht voor gevoel en verbeelding"],
                ["Relationisme", "de aandacht gaat naar de band tussen mensen"],
                ["Postmodernisme", "twijfel aan één grote waarheid"],
            ])),
            ("p", "<strong>Avant-garde</strong> is een verzamelnaam voor stromingen die <strong>bewust met "
                  "de traditie breken</strong>. Het <strong>neorealisme keert zich niet af van het "
                  "alledaagse</strong>: het zoekt dat juist op."),
            ("p", "Bij het <strong>postmodernisme</strong> horen verder het <strong>spel met verwijzingen "
                  "naar andere teksten</strong> en <strong>het doorbreken van de illusie van het "
                  "verhaal</strong>. Zegt een verteller plots dat hij het verhaal zelf verzint, dan zit je "
                  "daar. Een gedicht vol ongewone woordcombinaties, zonder hoofdletters en met gebroken "
                  "zinsbouw, past het best bij de <strong>Vijftigers</strong>."),
        ]),
    ],
    onthoud=[
        "Een stroming begint en eindigt niet op een scherp af te lijnen jaartal.",
        "Voorhoofs gaat over strijd en eer, hoofs over de verheven liefde voor een onbereikbare vrouw.",
        "De renaissance grijpt terug naar de klassieke oudheid, de barok toont de vergankelijkheid.",
        "De verlichting zet de rede centraal, de romantiek gevoel en verbeelding.",
        "Naturalisme: afkomst en omgeving bepalen het lot van een mens.",
        "De Tachtigers staan voor kunst om de kunst en de kracht van het individu.",
        "Het expressionisme drukt innerlijke gevoelens uit door de werkelijkheid te vervormen.",
        "De Vijftigers staan voor associatie en experiment met taal en vorm.",
        "Het postmodernisme twijfelt aan één grote waarheid.",
    ],
)

# ───────────────────────── 13. Taalvariëteiten, registers en beleefdheid
BUNDELS["taalvarieteiten-registers-en-beleefdheid-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Taalvariëteiten, registers en beleefdheid",
    onder="Dialect, tussentaal, jargon en standaardtaal, en hoe je je toon kiest.",
    secties=[
        dict(kop="Variëteiten", blokken=[
            ("p", "<strong>Standaardtaal</strong> is de variëteit die <strong>overal in het taalgebied "
                  "aanvaard</strong> is. Ze is nuttig in het onderwijs en het bestuur omdat "
                  "<strong>iedereen in het taalgebied haar kan begrijpen</strong>."),
            ("p", tabel(["Soort variëteit", "Wat ze is", "Voorbeeld"], [
                ["Regionaal", "hoort bij één streek", "een dialect"],
                ["Sociaal", "hoort bij één groep mensen", "jongerentaal, de taal van een rapper"],
                ["Situationeel", "hoort bij een bepaalde situatie", "ambtelijke taal, sportcommentaar"],
                ["Vakjargon", "hoort bij één beroep of vakgebied", "medische of juridische termen"],
                ["Nationaal", "het Nederlands van Nederland en dat van België", "twee variëteiten van dezelfde taal"],
                ["Tussentaal", "zit tussen het dialect en de standaardtaal in", "de omgangstaal van alledag"],
            ])),
            ("p", "<strong>Een nationale variëteit en een regionale variëteit zijn niet hetzelfde.</strong> "
                  "Het Belgische Nederlands is een nationale variëteit; het Limburgse dialect een "
                  "regionale."),
            ("p", "<strong>Eén spreker kan verschillende taalvariëteiten beheersen en ze "
                  "afwisselen.</strong> Een variëteit kan <strong>de communicatie vlotter maken</strong>, "
                  "maar kan ook <strong>miscommunicatie veroorzaken</strong>, en <strong>sprekers wisselen "
                  "naargelang de situatie</strong>."),
            ("kader", "<strong>Wie standaardtaal spreekt, drukt zich niet automatisch duidelijker uit dan "
                      "wie dialect spreekt.</strong> Duidelijkheid hangt af van wie je voor je hebt, niet "
                      "van het prestige van de variëteit."),
            ("p", "<strong>Tussentaal</strong> is het meest op haar plaats in een <strong>gesprek met "
                  "vrienden</strong>, een <strong>praatje op een feestje</strong> of een "
                  "<strong>telefoontje met een kennis</strong>."),
        ]),
        dict(kop="Jargon en moeilijke taal", blokken=[
            ("p", "<strong>Jargon</strong> of <strong>vaktaal</strong> is de taal die binnen één beroep of "
                  "vakgebied gebruikt wordt. Ze is handig onder vakgenoten, maar zorgt voor "
                  "miscommunicatie omdat <strong>wie de woorden niet kent, afhaakt</strong>. Schrijft een "
                  "arts een brief vol medische termen aan een patiënt, dan <strong>haakt de patiënt af en "
                  "voelt hij zich buitengesloten</strong>."),
            ("p", "Een <strong>ambtelijke tekst</strong> lijkt vaak moeilijk doordat <strong>de "
                  "formuleringen lang en onpersoonlijk</strong> zijn. Een <strong>juridische tekst</strong> "
                  "gebruikt vaste, moeilijke formuleringen omdat daar <strong>precisie zwaarder weegt dan "
                  "leesbaarheid</strong>."),
            ("p", "Gebruikt een rapper woorden die veel ouderen niet kennen, dan zie je hoe <strong>een "
                  "sociale variëteit een groep insluit en een andere uitsluit</strong>."),
        ]),
        dict(kop="Register", blokken=[
            ("p", "Een <strong>taalregister</strong> is <strong>de toon die je kiest naargelang de "
                  "situatie</strong>. Een <strong>formeel</strong> register hoort bij een "
                  "<strong>sollicitatiebrief</strong>, een <strong>mail aan een schooldirectie</strong> en "
                  "een <strong>klacht bij een officiële instantie</strong>. Het <strong>informele</strong> "
                  "register gebruik je met vrienden en familie."),
            ("p", tabel(["Formeel", "Informeel"], [
                ["u gebruiken in plaats van je", "aanspreking met je of jij"],
                ["volledige zinnen schrijven", "korte, losse zinnen"],
                ["afkortingen vermijden", "afkortingen"],
                ["met vriendelijke groeten", "groetjes"],
            ])),
            ("p", "Een formele brief sluit je dus <strong>niet</strong> af met <em>groetjes</em>, maar met "
                  "<em>met vriendelijke groeten</em>. Tegen een volwassene met wie je geen nauwe band hebt, "
                  "gebruik je <strong>u</strong>, en dat geldt ook voor klanten in een winkel waar je "
                  "vakantiewerk doet. Weet je niet zeker welk register past, dan <strong>kies je het meest "
                  "formele van de twee</strong>."),
            ("p", "Het effect van een verkeerd register: begint een leerling een mail aan een leerkracht "
                  "met <em>hey</em>, dan <strong>botst de aanspreking met de verhouding</strong>. Een "
                  "<strong>smiley in een formele mail</strong> <strong>past niet bij het register</strong>. "
                  "Omgekeerd kan je, door in een informele situatie plots standaardtaal te spreken, "
                  "<strong>afstand scheppen tussen jezelf en de ander</strong>."),
            ("p", "<strong>Het register dat je kiest, heeft wel degelijk effect op hoe anderen je "
                  "inschatten.</strong> Het is geen detail maar een deel van je boodschap."),
        ]),
        dict(kop="Beleefdheidsconventies", blokken=[
            ("p", "<strong>Beleefdheidsconventies</strong> zijn <strong>de afspraken over hoe je iemand "
                  "aanspreekt en bejegent</strong>. Iets <strong>vriendelijk vragen in plaats van het te "
                  "bevelen</strong> hoort erbij, net als een gepaste aanspreking en een verzorgde slotgroet."),
            ("p", "<strong>Beleefdheidsconventies zijn niet overal ter wereld dezelfde.</strong> Wat in de "
                  "ene cultuur beleefd heet, kan in een andere afstandelijk of juist opdringerig "
                  "overkomen. Je register aanpassen aan je ontvanger is <strong>een vorm van "
                  "respect</strong>."),
        ]),
    ],
    onthoud=[
        "Standaardtaal is overal in het taalgebied aanvaard.",
        "Een nationale variëteit is niet hetzelfde als een regionale variëteit.",
        "Tussentaal zit tussen het dialect en de standaardtaal in.",
        "Wie standaardtaal spreekt, drukt zich niet automatisch duidelijker uit dan wie dialect spreekt.",
        "Jargon is handig onder vakgenoten, maar wie de woorden niet kent, haakt af.",
        "Een taalregister is de toon die je kiest naargelang de situatie.",
        "Twijfel je over het register, kies dan het meest formele van de twee.",
        "Beleefdheidsconventies zijn niet overal ter wereld dezelfde.",
    ],
)

# ───────────────────────── 14. Taal en identiteit
BUNDELS["taal-en-identiteit-stereotypering-inclusie-en-non-verbale-communicatie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Taal en identiteit: stereotypering, inclusie en non-verbale communicatie",
    onder="Hoe taal mensen insluit of buitensluit, en wat er naast de woorden nog meespreekt.",
    secties=[
        dict(kop="Stereotypering", blokken=[
            ("p", "Een <strong>stereotype</strong> is een versimpeld, overdreven beeld van een hele groep. "
                  "Stereotypes zijn gebaseerd op <strong>versimpeling, overdrijving en "
                  "veralgemening</strong>. <strong>Een stereotype is dus geen nuttige samenvatting en "
                  "meestal ook niet correct</strong>: het klopt hooguit voor sommigen en nooit voor allen."),
            ("p", "Stereotypering op basis van taal kom je tegen <strong>in stripverhalen</strong>, "
                  "<strong>in reclame</strong> en <strong>in humoristische tv-programma's</strong>. Spreekt "
                  "een personage in een sitcom met een zwaar accent en wordt het als dom neergezet, dan "
                  "wordt <strong>taal gekoppeld aan een karaktereigenschap</strong>."),
            ("p", "Inzicht hierin is nuttig omdat <strong>je dan opmerkt wanneer je zelf te snel "
                  "oordeelt</strong>. Merk je dat je iemand op zijn accent beoordeelde, dan <strong>stel je "
                  "je oordeel bij op wat hij zegt</strong>. <strong>Wie een andere variëteit spreekt dan "
                  "jij, denkt daarom niet anders over de wereld.</strong>"),
        ]),
        dict(kop="Inclusie en exclusie", blokken=[
            ("p", "<strong>Inclusie</strong> is mensen bij elkaar brengen; <strong>exclusie</strong> is het "
                  "buitensluiten van mensen. Taal doet allebei. <strong>Wie dezelfde taal deelt, voelt zich "
                  "deel van de groep.</strong>"),
            ("p", "Taal sluit uit door <strong>jargon dat buitenstaanders niet begrijpen</strong>, door "
                  "<strong>elitair taalgebruik in een openbaar gesprek</strong> (taal die afstand schept "
                  "door haar moeilijkheid) en door <strong>een variëteit die anderen niet beheersen</strong>. "
                  "Spreken twee collega's dialect in een vergadering met een nieuwe medewerker uit een "
                  "andere streek, dan <strong>valt die nieuwe medewerker buiten het gesprek</strong>. Dat "
                  "ouderen een tekst van jonge rappers niet begrijpen, is hetzelfde verschijnsel."),
            ("p", "<strong>Genderneutrale taal</strong> is een voorbeeld van taal die probeert <strong>in te "
                  "sluiten</strong>. Een gemeente die haar brieven in eenvoudige taal herschrijft, wil "
                  "<strong>dat meer inwoners de brief kunnen begrijpen</strong>."),
            ("p", "<strong>Je taalgebruik is een deel van wie je bent</strong>, <strong>je oordeelt ook zelf "
                  "over anderen op hun taal</strong>, en <strong>inzicht hierin leidt tot meer "
                  "begrip</strong>. <strong>Je taalgebruik beïnvloedt het beeld dat anderen van je "
                  "krijgen.</strong> Daarom hoort taalbeschouwing bij dit vak en niet enkel grammatica: "
                  "<strong>taal bepaalt mee hoe mensen met elkaar omgaan</strong>."),
        ]),
        dict(kop="Non-verbale en paraverbale communicatie", blokken=[
            ("p", "<strong>Non-verbale communicatie</strong> is alles wat je zonder woorden overbrengt: "
                  "<strong>lichaamstaal</strong>, <strong>oogcontact</strong>, <strong>kleding en "
                  "uiterlijk</strong>, <strong>mimiek</strong> (de uitdrukking op het gezicht) en "
                  "<strong>proxemiek</strong> (de afstand die je tot de ander bewaart). <strong>Je kleding "
                  "draagt dus wel degelijk bij</strong> aan de boodschap die je brengt."),
            ("p", "<strong>Paraverbale</strong> aspecten zijn <strong>intonatie, articulatie, tempo en "
                  "volume</strong>: alles aan de stem behalve de woorden zelf. <strong>Intonatie</strong> "
                  "is de melodie en de toonhoogte waarmee je een zin uitspreekt; "
                  "<strong>articulatie</strong> het duidelijk uitspreken van de klanken. "
                  "<strong>Dezelfde zin kan door de intonatie neutraal of spottend klinken.</strong>"),
            ("p", "Om nadruk te leggen kan een spreker <strong>een pauze laten vallen</strong>, <strong>het "
                  "volume verhogen</strong> of <strong>trager gaan spreken</strong>. Praat iemand heel snel "
                  "en zonder pauzes, dan is het risico dat <strong>de luisteraar niet kan volgen</strong>. "
                  "Wie een presentatie volledig van zijn blad afleest, <strong>verliest de band met zijn "
                  "publiek</strong>; lichaamstaal gebruiken helpt juist <strong>je boodschap beter over te "
                  "brengen</strong>."),
            ("p", "<strong>Non-verbale communicatie speelt niet enkel in gesproken gesprekken.</strong> "
                  "<strong>Emoji's</strong> zijn er een vorm van in geschreven taal, en woorden "
                  "<strong>in hoofdletters</strong> typen op een forum wordt als <strong>schreeuwen</strong> "
                  "opgevat. Dat is ook de reden waarom <strong>ironie in een appje vaker verkeerd begrepen "
                  "wordt dan in een gesprek</strong>: <strong>de toon en het gezicht ontbreken</strong>."),
            ("p", "Tijdens een gesprek let je op de lichaamstaal van je gesprekspartner, want <strong>je "
                  "ziet eraan hoe je boodschap aankomt</strong>. Leunt hij achteruit en kijkt hij weg, dan "
                  "<strong>pas je je tempo of je onderwerp aan</strong>. Zegt iemand <em>alles is in "
                  "orde</em> met een gespannen stem en afgewende blik, dan <strong>weeg je de woorden tegen "
                  "de signalen af</strong>."),
            ("p", "Een <strong>open, uitnodigende houding</strong> herken je aan <strong>oogcontact "
                  "maken</strong>, <strong>de armen niet gekruist houden</strong> en <strong>je naar de "
                  "spreker toe draaien</strong>."),
        ]),
    ],
    onthoud=[
        "Een stereotype is gebaseerd op versimpeling, overdrijving en veralgemening.",
        "Inclusie brengt mensen bij elkaar, exclusie sluit mensen buiten.",
        "Jargon, elitair taalgebruik en een variëteit die anderen niet beheersen, sluiten uit.",
        "Genderneutrale taal probeert in te sluiten.",
        "Non-verbaal: lichaamstaal, oogcontact, kleding en uiterlijk, mimiek en proxemiek.",
        "Paraverbaal: intonatie, articulatie, tempo en volume.",
        "Dezelfde zin kan door de intonatie neutraal of spottend klinken.",
        "Ironie in een appje wordt vaker verkeerd begrepen: de toon en het gezicht ontbreken.",
    ],
)

# ───────────────────────── 15. Klanken, spelling, diakritische tekens en interpunctie
BUNDELS["klanken-spelling-diakritische-tekens-en-interpunctie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Klanken, spelling, diakritische tekens en interpunctie",
    onder="Van klankbeeld tot leesteken: de regels die je op papier nodig hebt.",
    secties=[
        dict(kop="Klank en schrift", blokken=[
            ("p", "Het <strong>klankbeeld</strong> van een woord <strong>hoor</strong> je, het "
                  "<strong>schriftbeeld</strong> <strong>zie</strong> je. <strong>De spelling volgt niet "
                  "altijd precies de uitspraak</strong>, en daarom is dat verschil belangrijk: <strong>op "
                  "het gehoor afgaan leidt tot fouten</strong>."),
            ("p", "Men onderscheidt <strong>lange klanken</strong> (maan, boom, deur), <strong>korte "
                  "klanken</strong> en <strong>doffe klanken</strong>. De <strong>doffe klank</strong> is "
                  "de onbeklemtoonde e, bijvoorbeeld in <em>gemeente</em>. De <strong>a, e, i, o en u zijn "
                  "klinkers</strong>; de overige letters zijn medeklinkers."),
            ("p", "Een woord heeft een <strong>vast woordbeeld</strong>: <strong>het wordt altijd op "
                  "dezelfde manier geschreven</strong>, ook als de uitspraak in een zin verandert."),
        ]),
        dict(kop="Werkwoordspelling", blokken=[
            ("p", "De <strong>stam</strong> van een werkwoord is <strong>de infinitief zonder de uitgang "
                  "-en</strong>. De stam van <em>reizen</em> is dus <em>reis</em>."),
            ("p", tabel(["Vorm", "Regel", "Voorbeeld"], [
                ["ik + stam", "geen t erbij", "ik verwacht (de stam is verwacht)"],
                ["hij + stam", "stam + t", "hij wordt, hij antwoordt"],
                ["verleden tijd zwak", "stam + te of de", "hij werkte"],
                ["voltooid deelwoord", "ge + stam + d of t", "geantwoord, gebeurd"],
            ])),
            ("p", "<em>Hij antwoordt</em> krijgt dt omdat <strong>de stam op d eindigt en er bij "
                  "<em>hij</em> een t bij komt</strong>. In <em>ik verwacht</em> komt er <strong>geen</strong> "
                  "t bij de stam: die eindigt al op t. Het voltooid deelwoord van <em>verbranden</em> is "
                  "<em>verbrand</em>, dat van <em>gebeuren</em> is <em>gebeurd</em>, en dat van "
                  "<em>antwoorden</em> is <em>geantwoord</em>."),
        ]),
        dict(kop="Hoofdletters", blokken=[
            ("p", "Een hoofdletter krijgen onder meer <strong>namen van personen</strong>, <strong>namen "
                  "van landen</strong> en <strong>namen van talen</strong>. De taal die in Frankrijk "
                  "gesproken wordt, schrijf je dus als <strong>Frans</strong>."),
            ("p", "<strong>Namen van maanden krijgen in het Nederlands géén hoofdletter</strong>: "
                  "<em>december</em>, niet <em>December</em>. Dat is anders dan in het Engels."),
        ]),
        dict(kop="Diakritische tekens", blokken=[
            ("p", tabel(["Teken", "Waarvoor", "Voorbeeld"], [
                ["Trema", "laat zien dat een klinker apart gelezen wordt", "ruïne"],
                ["Apostrof", "duidt een weggelaten letter aan, of maakt een meervoud leesbaar", "zo'n, 's morgens, auto's"],
                ["Koppelteken", "in samenstellingen met een eigennaam, bij botsende klinkers", "Noord-Frankrijk, twee-eiig"],
                ["Accent", "geeft de uitspraak aan, of legt nadruk", "café, dát wil ik"],
            ])),
            ("p", "<strong>Een trema en een accent zijn niet hetzelfde teken.</strong> Een "
                  "<strong>uitspraakteken</strong> is een accent dat aangeeft hoe je iets uitspreekt; "
                  "daarnaast kan een accent dienen <strong>om nadruk te leggen op een woord</strong>."),
            ("p", "Een <strong>koppelteken</strong> gebruik je <strong>in samenstellingen met een "
                  "eigennaam</strong>, <strong>als er anders drie dezelfde klinkers botsen</strong> en "
                  "<strong>in woordgroepen als <em>twee-eiig</em></strong>. Het meervoud van <em>auto</em> "
                  "is <strong>auto's</strong>."),
        ]),
        dict(kop="Interpunctie", blokken=[
            ("p", "Tot de leestekens die je moet kennen horen onder meer <strong>de komma</strong>, "
                  "<strong>de dubbele punt</strong>, <strong>het aanhalingsteken</strong>, de punt, het "
                  "vraagteken, het uitroepteken en het puntkomma. <strong>Ook de spatie telt mee als "
                  "interpunctieteken.</strong>"),
            ("p", "Een <strong>punt</strong> sluit een mededelende zin af. Een <strong>dubbele punt</strong> "
                  "kondigt <strong>een opsomming of een citaat</strong> aan. <strong>Aanhalingstekens</strong> "
                  "zet je rond de letterlijke woorden van iemand anders. Een <strong>komma</strong> scheidt "
                  "onder meer een bijzin van de hoofdzin: <em>Toen hij binnenkwam, zweeg iedereen.</em>"),
            ("p", "<strong>Een uitroepteken hoort niet in elke alinea van een zakelijke tekst.</strong> "
                  "Gebruik het spaarzaam, anders verliest het zijn kracht. In een formele brief "
                  "<strong>pas je de interpunctie zorgvuldig en volgens de regels toe</strong>."),
            ("kader", "<strong>Leestekens zijn meer dan opsmuk: ze bepalen mee de betekenis van een "
                      "zin.</strong> Eén komma verschil kan van een uitnodiging een bevel maken."),
        ]),
    ],
    onthoud=[
        "Het klankbeeld hoor je, het schriftbeeld zie je.",
        "De doffe klank is de onbeklemtoonde e, zoals in gemeente.",
        "De stam is de infinitief zonder de uitgang -en.",
        "Hij antwoordt krijgt dt: de stam eindigt op d en bij hij komt er een t bij.",
        "Namen van maanden krijgen in het Nederlands geen hoofdletter.",
        "Een trema en een accent zijn niet hetzelfde teken.",
        "Een koppelteken gebruik je in samenstellingen met een eigennaam, zoals Noord-Frankrijk.",
        "Een dubbele punt kondigt een opsomming of een citaat aan.",
        "Leestekens bepalen mee de betekenis van een zin.",
    ],
)

# ───────────────────────── 16. Woordsoorten
BUNDELS["woordsoorten-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Woordsoorten",
    onder="De tien woordsoorten, de voornaamwoorden en de drie soorten werkwoorden.",
    secties=[
        dict(kop="De woordsoorten op een rij", blokken=[
            ("p", "Je bepaalt de woordsoort van een woord niet uit het woordenboek maar uit de zin: "
                  "<strong>je kijkt naar de rol die het in díe zin speelt</strong>. Daarom is <strong>het "
                  "woord <em>het</em> niet altijd een lidwoord</strong>, en kan <strong>hetzelfde woord in "
                  "de ene zin een voornaamwoord zijn en in de andere een lidwoord</strong>."),
            ("p", tabel(["Woordsoort", "Wat ze doet", "Voorbeeld"], [
                ["Zelfstandig naamwoord", "noemt een ding, een persoon of een begrip", "tafel in de tafel staat scheef"],
                ["Lidwoord", "staat bij een zelfstandig naamwoord", "de, het, een"],
                ["Bijvoeglijk naamwoord", "zegt iets over een zelfstandig naamwoord", "snel in de snelle trein"],
                ["Werkwoord", "noemt wat er gebeurt of is", "staan, lopen, zijn"],
                ["Bijwoord", "zegt iets over een werkwoord, een bijvoeglijk naamwoord of een hele zin", "morgen, erg"],
                ["Voorzetsel", "legt een verhouding", "onder, tussen, achter, tijdens, van"],
                ["Voegwoord", "verbindt woorden of zinnen", "en, want, omdat, hoewel"],
                ["Telwoord", "telt of ordent", "drie, derde"],
                ["Voornaamwoord", "vervangt of begeleidt een naamwoord", "hij, mijn, die"],
                ["Tussenwerpsel", "staat los in de zin en drukt een gevoel uit", "au"],
            ])),
            ("p", "Een <strong>lidwoord kan niet voor een werkwoord staan</strong>. Een <strong>bijvoeglijk "
                  "naamwoord kan wél achter het zelfstandig naamwoord staan</strong>: <em>de trein, snel en "
                  "stil</em>. Het verschil tussen een <strong>hoofdtelwoord</strong> en een "
                  "<strong>rangtelwoord</strong>: <strong>een hoofdtelwoord telt, een rangtelwoord "
                  "ordent</strong>."),
            ("p", "Woordsoorten benoemen is nuttig omdat <strong>je daardoor de bouw van een zin "
                  "begrijpt</strong>, en dat heb je nodig bij de zinsontleding en bij de "
                  "werkwoordspelling."),
        ]),
        dict(kop="Voornaamwoorden", blokken=[
            ("p", tabel(["Soort", "Voorbeeld"], [
                ["Persoonlijk", "hij ziet mij"],
                ["Bezittelijk", "dat is mijn jas"],
                ["Wederkerig", "hij wast zich"],
                ["Aanwijzend", "deze, die, dat"],
                ["Vragend", "wie, wat, welke"],
                ["Betrekkelijk", "de man die daar staat, de jongen wiens fiets gestolen werd"],
                ["Onbepaald", "iemand, niemand, alles"],
            ])),
            ("p", "<strong>Deze, die en dat zijn aanwijzende voornaamwoorden</strong>, geen bezittelijke. "
                  "Het <strong>antecedent</strong> is <strong>het woord waarnaar een betrekkelijk "
                  "voornaamwoord terugwijst</strong>."),
            ("p", "Het verschil tussen een <strong>zelfstandig</strong> en een <strong>bijvoeglijk "
                  "gebruikt</strong> voornaamwoord: <strong>het zelfstandige staat alleen, het bijvoeglijke "
                  "staat bij een naamwoord</strong>. Vergelijk <em>dat is van mij</em> met <em>mijn "
                  "jas</em>."),
        ]),
        dict(kop="Soorten werkwoorden", blokken=[
            ("p", "Het <strong>zelfstandig werkwoord</strong> draagt de eigenlijke betekenis. Een "
                  "<strong>hulpwerkwoord</strong> helpt bij de vervoeging: <em>hebben</em> in <em>hij heeft "
                  "gelopen</em>. <strong>Een hulpwerkwoord kan niet alleen in een zin staan</strong>, zonder "
                  "zelfstandig werkwoord."),
            ("p", "Een <strong>koppelwerkwoord</strong> verbindt het onderwerp met wat erover gezegd wordt: "
                  "<em>zijn</em> in <em>hij is leraar</em>, en verder onder meer <strong>worden</strong>, "
                  "<strong>blijven</strong> en <strong>lijken</strong>. Weten of een werkwoord "
                  "koppelwerkwoord of zelfstandig werkwoord is, is belangrijk omdat <strong>het bepaalt of "
                  "er een naamwoordelijk gezegde is</strong>."),
            ("p", "De <strong>infinitief</strong> is de onvervoegde grondvorm, zoals <em>lopen</em>. Een "
                  "<strong>voltooid deelwoord</strong> begint in het Nederlands <strong>vaak met ge</strong>."),
        ]),
    ],
    onthoud=[
        "De woordsoort bepaal je uit de rol die het woord in díe zin speelt.",
        "Hetzelfde woord kan in de ene zin een voornaamwoord zijn en in de andere een lidwoord.",
        "Een hoofdtelwoord telt, een rangtelwoord ordent.",
        "Deze, die en dat zijn aanwijzende voornaamwoorden.",
        "Het antecedent is het woord waarnaar een betrekkelijk voornaamwoord terugwijst.",
        "Een zelfstandig voornaamwoord staat alleen, een bijvoeglijk gebruikt staat bij een naamwoord.",
        "Een hulpwerkwoord kan niet alleen in een zin staan.",
        "Koppelwerkwoord of zelfstandig werkwoord bepaalt of er een naamwoordelijk gezegde is.",
    ],
)

# ───────────────────────── 17. Morfologie
BUNDELS["morfologie-samenstellingen-afleidingen-en-werkwoordstijden-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Morfologie: samenstellingen, afleidingen en werkwoordstijden",
    onder="Hoe woorden gebouwd zijn, en hoe werkwoorden door de tijden gaan.",
    secties=[
        dict(kop="Samenstelling en afleiding", blokken=[
            ("p", "Een <strong>samenstelling</strong> is een woord dat uit <strong>twee of meer "
                  "woorden</strong> bestaat: <em>boekenkast</em>, <em>pannenkoek</em>. <strong>In een "
                  "samenstelling kunnen ook drie woorden samengaan</strong>: <em>fietsenstallingbeheer</em>."),
            ("p", "Een <strong>afleiding</strong> ontstaat door een voor- of achtervoegsel bij een woord te "
                  "zetten: <em>vriendelijk</em>, <em>onmogelijk</em>, <em>werker</em>. Het verschil met een "
                  "samenstelling: <strong>een samenstelling bestaat uit zelfstandige woorden</strong>, een "
                  "afleiding niet."),
            ("p", "Een <strong>voorvoegsel</strong> wordt vooraan geplakt (<em>on-</em>, <em>ver-</em>); "
                  "een <strong>achtervoegsel</strong> achteraan (<em>-heid</em>, <em>-baar</em>). Het "
                  "voorvoegsel <strong>on-</strong> in <em>onvriendelijk</em> <strong>keert de betekenis "
                  "om</strong>. Het achtervoegsel <strong>-heid</strong> maakt van een bijvoeglijk "
                  "naamwoord een <strong>zelfstandig naamwoord</strong>; <strong>-baar</strong>, zoals in "
                  "<em>leesbaar</em>, levert een <strong>bijvoeglijk naamwoord</strong> op. Het woord "
                  "<em>onvriendelijkheid</em> bevat <strong>zowel een voorvoegsel als een "
                  "achtervoegsel</strong>."),
            ("p", "De <strong>tussenklank</strong> verbindt twee delen van een samenstelling. In "
                  "<em>boekenkast</em> is dat <strong>de en tussen boek en kast</strong>. Ook "
                  "<em>pannenkoek</em>, <em>zonnebloem</em> en <em>koninginnendag</em> bevatten een "
                  "<strong>tussenletter</strong>."),
            ("kader", "De bouw van een woord herkennen loont: <strong>je kan de betekenis vaak zelf "
                      "afleiden</strong>. Zie je <em>onbereikbaarheid</em> voor het eerst, dan "
                      "<strong>ontleed je het in zijn delen</strong>: on + bereik + baar + heid."),
        ]),
        dict(kop="Meervoud en verkleinwoord", blokken=[
            ("p", "<strong>Niet elk Nederlands meervoud wordt met -en of -s gevormd.</strong> Het meervoud "
                  "van <em>kind</em> is <strong>kinderen</strong>, met een extra -er-. Ook <em>ei</em> en "
                  "<em>blad</em> horen bij die groep."),
            ("p", "<strong>Verkleinwoorden</strong>: <em>huisje</em>, <em>bloempje</em>, "
                  "<em>koninkje</em>. Het verkleinwoord van <em>koning</em> is dus <strong>koninkje</strong>. "
                  "<strong>Een verkleinwoord houdt het lidwoord van het grondwoord niet</strong>: het is "
                  "altijd <em>het</em>, ook bij <em>de stoel</em> en <em>het stoeltje</em>."),
        ]),
        dict(kop="Werkwoordstijden", blokken=[
            ("p", tabel(["Tijd", "Voorbeeld"], [
                ["Onvoltooid tegenwoordige tijd", "hij werkt"],
                ["Onvoltooid verleden tijd", "hij liep, zij werkte, wij dachten"],
                ["Voltooid tegenwoordige tijd", "hij heeft gewerkt"],
                ["Voltooid verleden tijd", "hij had gewerkt"],
                ["Onvoltooid toekomende tijd", "hij zal morgen komen"],
                ["Voltooid toekomende tijd", "hij zal gewerkt hebben"],
            ])),
            ("p", "De <strong>onvoltooid tegenwoordige tijd</strong> gebruik je om iets te vertellen wat nu "
                  "bezig is. Goede schrijvers variëren met de tijden omdat <strong>de tijd stuurt hoe de "
                  "lezer de gebeurtenis plaatst</strong>."),
            ("p", "De <strong>imperatief</strong> of <strong>gebiedende wijs</strong> is de bevelvorm: "
                  "<em>loop!</em>, <em>werk!</em>"),
        ]),
        dict(kop="Stam, uitgang en vervoeging", blokken=[
            ("p", "De <strong>uitgang</strong> is <strong>het deel dat na de stam komt bij het "
                  "vervoegen</strong>. Het onderscheid tussen stam en uitgang is belangrijk omdat "
                  "<strong>de spelling van werkwoorden ervan afhangt</strong>. De stam van "
                  "<em>antwoorden</em> is <strong>antwoord</strong>."),
            ("p", "<strong>Vervoeging</strong> slaat op <strong>werkwoorden</strong> en "
                  "<strong>verbuiging</strong> op <strong>naamwoorden</strong>, niet omgekeerd. Een "
                  "<strong>bijvoeglijk naamwoord krijgt soms een extra e</strong>: <em>een snelle trein</em> "
                  "naast <em>een snel antwoord</em>."),
            ("p", "Een <strong>sterk werkwoord</strong> is een werkwoord dat <strong>in de verleden tijd "
                  "van klinker verandert</strong>: <em>lopen – liep</em>. Bij een <strong>zwak "
                  "werkwoord</strong> weet je of het <strong>-te</strong> of <strong>-de</strong> krijgt "
                  "door <strong>naar de laatste klank van de stam</strong> te kijken."),
            ("p", "<strong>Voltooide deelwoorden</strong>: <em>gewerkt</em>, <em>gelopen</em>, "
                  "<em>verwacht</em>. <strong>Het werkwoord <em>zijn</em> wordt niet volgens de gewone "
                  "regels vervoegd</strong>: het is onregelmatig. Een <strong>scheidbaar werkwoord</strong> "
                  "<strong>valt in sommige zinnen uiteen in twee delen</strong>: <em>opbellen</em> wordt "
                  "<em>ik bel je op</em>."),
        ]),
    ],
    onthoud=[
        "Een samenstelling bestaat uit zelfstandige woorden, een afleiding niet.",
        "On- keert de betekenis om, -heid maakt een zelfstandig naamwoord, -baar een bijvoeglijk naamwoord.",
        "De tussenklank verbindt twee delen van een samenstelling, zoals in boekenkast.",
        "Het meervoud van kind is kinderen, met een extra -er-.",
        "Een verkleinwoord krijgt altijd het lidwoord het.",
        "Hij had gewerkt is voltooid verleden tijd, hij zal gewerkt hebben voltooid toekomende tijd.",
        "Vervoeging slaat op werkwoorden, verbuiging op naamwoorden.",
        "Een sterk werkwoord verandert in de verleden tijd van klinker: lopen – liep.",
        "Een scheidbaar werkwoord valt in sommige zinnen uiteen in twee delen.",
    ],
)

# ───────────────────────── 18. Zinsontleding en zinsbouw
BUNDELS["zinsontleding-en-zinsbouw-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Zinsontleding en zinsbouw",
    onder="Zinssoorten, hoofdzin en bijzin, woordvolgorde, en alle zinsdelen met hun vraag.",
    secties=[
        dict(kop="Zinssoorten", blokken=[
            ("p", "Naar hun bedoeling onderscheidt men de <strong>mededelende zin</strong>, de "
                  "<strong>vragende zin</strong>, de <strong>bevelende zin</strong> en de "
                  "<strong>uitroepende zin</strong>. <em>Hij komt niet</em> is daarnaast een "
                  "<strong>ontkennende</strong> zin. <strong>Een uitroepende zin eindigt niet met een "
                  "vraagteken</strong> maar met een uitroepteken."),
            ("p", "Het verschil tussen een <strong>actieve</strong> en een <strong>passieve</strong> zin: "
                  "<strong>in een passieve zin ondergaat het onderwerp de handeling</strong>. <em>De brief "
                  "werd door de postbode bezorgd</em> is dus <strong>passief</strong>."),
        ]),
        dict(kop="Enkelvoudig en samengesteld", blokken=[
            ("p", "Een <strong>enkelvoudige zin</strong> is een zin met <strong>maar één "
                  "persoonsvorm</strong>. Zinnen met twee persoonsvormen zijn <strong>samengesteld</strong>: "
                  "<em>Hij komt en zij blijft.</em>, <em>Ik blijf thuis omdat het regent.</em>, <em>Toen hij "
                  "kwam, zweeg iedereen.</em>"),
            ("p", "Bij <strong>nevenschikking</strong> zijn de twee delen <strong>gelijkwaardig</strong> "
                  "(<em>en</em>, <em>maar</em>, <em>want</em>). Bij <strong>onderschikking</strong> hangt "
                  "<strong>een bijzin af van een hoofdzin</strong>. Woorden die een bijzin inleiden: "
                  "<strong>omdat</strong>, <strong>hoewel</strong>, <strong>die</strong>. Het "
                  "<strong>antecedent</strong> is het woord waarnaar een betrekkelijke bijzin "
                  "terugverwijst."),
            ("p", "<strong>In een Nederlandse bijzin staat de persoonsvorm meestal achteraan.</strong> In "
                  "een gewone mededelende hoofdzin staat ze <strong>op de tweede plaats</strong>."),
        ]),
        dict(kop="Woordvolgorde", blokken=[
            ("p", "<strong>Inversie</strong> is de omkering waarbij <strong>het onderwerp achter de "
                  "persoonsvorm</strong> belandt. Dat gebeurt zodra er iets anders vooraan staat: in "
                  "<em>Gisteren las ik een boek</em> <strong>treedt inversie op</strong>."),
            ("p", "Een <strong>tangconstructie</strong> is een zin waarin <strong>twee bij elkaar horende "
                  "delen ver uit elkaar staan</strong>. <strong>Een lange tangconstructie maakt een zin "
                  "juist moeilijker te volgen</strong>, want de lezer moet het eerste deel onthouden tot "
                  "het tweede eindelijk komt."),
            ("p", "<strong>Variatie in zinsbouw</strong> is een criterium bij schrijven omdat "
                  "<strong>afwisseling een tekst levendig houdt</strong>: korte en lange zinnen, actief en "
                  "passief, af en toe een vooropgeplaatste bepaling."),
        ]),
        dict(kop="De zinsdelen", blokken=[
            ("p", "Een <strong>zinsdeel</strong> is <strong>een groep woorden die samen één rol "
                  "speelt</strong>. <strong>Een zinsdeel kan ook uit één woord bestaan.</strong> Je test of "
                  "een groep woorden één zinsdeel vormt door <strong>ze samen naar voren in de zin te "
                  "verplaatsen</strong>."),
            ("p", tabel(["Zinsdeel", "Vraag", "Voorbeeld"], [
                ["Persoonsvorm", "welk werkwoord is vervoegd?", "gaf in de leraar gaf een toets"],
                ["Onderwerp", "wie of wat + persoonsvorm?", "de leraar"],
                ["Lijdend voorwerp", "wie of wat + gezegde + onderwerp?", "een boek in hij geeft zijn zus een boek"],
                ["Meewerkend voorwerp", "aan wie of voor wie?", "aan mijn zus in aan mijn zus heb ik een brief geschreven"],
                ["Voorzetselvoorwerp", "een voorwerp met een vast voorzetsel", "denken aan, rekenen op"],
                ["Handelend voorwerp", "door wie, in een passieve zin", "door de postbode"],
                ["Bijwoordelijke bepaling", "wanneer, waar, hoe?", "gisteren"],
            ])),
            ("p", "<strong>Niet elke zin heeft een lijdend voorwerp.</strong> In <em>De leraar gaf de "
                  "leerlingen gisteren een toets</em> vind je een <strong>onderwerp</strong>, een "
                  "<strong>meewerkend voorwerp</strong>, een <strong>bijwoordelijke bepaling</strong> en "
                  "een lijdend voorwerp. Een <strong>bijwoordelijke bepaling</strong> zegt iets over "
                  "<strong>de omstandigheden van de handeling</strong>."),
        ]),
        dict(kop="Het gezegde", blokken=[
            ("p", "Een <strong>naamwoordelijk gezegde</strong> is <strong>een koppelwerkwoord met een "
                  "naamwoordelijk deel</strong>: <em>hij is leraar</em>. Het <strong>werkwoordelijk "
                  "gezegde</strong> bestaat <strong>niet enkel uit de persoonsvorm</strong>: ook de "
                  "deelwoorden en infinitieven horen erbij, zoals in <em>hij heeft gelopen</em>."),
            ("p", "Zinsontleding helpt bij het spellen van werkwoorden, want <strong>je vindt zo het "
                  "onderwerp bij de persoonsvorm</strong>, en daarmee weet je of er een t bij moet."),
        ]),
    ],
    onthoud=[
        "In een passieve zin ondergaat het onderwerp de handeling.",
        "Een enkelvoudige zin heeft maar één persoonsvorm.",
        "Bij nevenschikking zijn de delen gelijkwaardig, bij onderschikking hangt een bijzin af van een hoofdzin.",
        "In een bijzin staat de persoonsvorm meestal achteraan, in een mededelende hoofdzin op de tweede plaats.",
        "Bij inversie belandt het onderwerp achter de persoonsvorm.",
        "Een lange tangconstructie maakt een zin moeilijker te volgen.",
        "Een zinsdeel test je door de woorden samen naar voren in de zin te verplaatsen.",
        "Niet elke zin heeft een lijdend voorwerp.",
        "Een naamwoordelijk gezegde is een koppelwerkwoord met een naamwoordelijk deel.",
    ],
)

# ───────────────────────── 19. Semantiek
BUNDELS["semantiek-betekenisrelaties-gevoelswaarde-en-herkomst-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Semantiek: betekenisrelaties, gevoelswaarde en herkomst",
    onder="Hoe woorden zich tot elkaar verhouden, welke bijklank ze dragen en waar ze vandaan komen.",
    secties=[
        dict(kop="Betekenisrelaties", blokken=[
            ("p", tabel(["Begrip", "Wat het is", "Voorbeeld"], [
                ["Synoniemen", "woorden met ongeveer dezelfde betekenis", "beginnen en starten"],
                ["Antoniemen", "woorden met een tegengestelde betekenis", "warm en koud, groot en klein, vroeg en laat"],
                ["Homoniemen", "dezelfde vorm, een heel andere betekenis", "bank om op te zitten of om geld te halen"],
                ["Hyperoniem", "het ruimere woord", "meubel, dier"],
                ["Hyponiem", "het engere woord", "stoel, tafel, kast; appel onder fruit"],
            ])),
            ("p", "Het hyperoniem van <em>hond</em>, <em>kat</em> en <em>konijn</em> kan <strong>dier</strong>, "
                  "<strong>huisdier</strong> of <strong>zoogdier</strong> zijn: een woord kan tegelijk "
                  "hyperoniem van het ene en hyponiem van het andere zijn."),
            ("p", "<strong>Een synoniem kan je niet altijd zomaar in de plaats van een ander woord "
                  "zetten.</strong> Twee synoniemen verschillen vaak in register of in gevoelswaarde. "
                  "Betekenisrelaties kennen is nuttig bij het schrijven omdat <strong>je daardoor kan "
                  "variëren zonder onduidelijk te worden</strong>."),
        ]),
        dict(kop="Letterlijk en figuurlijk", blokken=[
            ("p", "In <em>de poot van de tafel</em> is <em>poot</em> <strong>figuurlijk</strong> gebruikt. "
                  "<em>Hij heeft zijn handen vol</em> is een <strong>figuurlijke uitdrukking</strong>, en "
                  "<em>de voorzitter nam de benen</em> lees je <strong>figuurlijk: hij ging er snel "
                  "vandoor</strong>."),
            ("p", "Soms zit het verschil in een voorvoegsel: <em>ik ga me omkleden</em> tegenover <em>ik ga "
                  "me verkleden</em> verschilt <strong>in de betekenis van het voorvoegsel</strong>, niet in "
                  "het grondwoord."),
        ]),
        dict(kop="Taalfouten rond betekenis", blokken=[
            ("p", "Een <strong>pleonasme</strong> is <strong>een overbodige toevoeging die al in het woord "
                  "zit</strong>: <em>een witte schimmel</em>. Een <strong>tautologie</strong> zegt "
                  "<strong>hetzelfde twee keer met andere woorden</strong>: <em>nooit ofte nimmer</em>. "
                  "<strong>Een pleonasme is niet altijd een fout</strong>; als nadruk kan het bewust "
                  "ingezet worden."),
            ("p", "Een <strong>contaminatie</strong> is het versmelten van twee uitdrukkingen tot één "
                  "foute: <strong>optelefoneren</strong>, <strong>uitprinten</strong>, <strong>duur "
                  "kosten</strong> (uit <em>duur zijn</em> en <em>veel kosten</em>)."),
        ]),
        dict(kop="Gevoelswaarde", blokken=[
            ("p", "De <strong>denotatie</strong> is de <strong>kale betekenis</strong> van een woord; de "
                  "<strong>connotatie</strong> is <strong>de bijklank</strong>. <strong>Een woord met een "
                  "neutrale denotatie kan toch een negatieve connotatie krijgen.</strong> Negatief klinken "
                  "bijvoorbeeld <em>krot</em>, <em>bende</em> en <em>geklungel</em>."),
            ("p", "Een <strong>eufemisme</strong> is een verzachtend woord voor iets onaangenaams: "
                  "<em>heengaan</em> voor sterven, <em>senioren</em>, <em>sociale woning</em>, of "
                  "<em>herstructurering</em> in plaats van ontslagen. Een <strong>dysfemisme</strong> doet "
                  "het omgekeerde: het <strong>maakt iets ruwer of harder dan nodig</strong>."),
            ("p", "Daarom kiest een journalist bewust tussen <em>betoger</em> en <em>relschopper</em>: "
                  "<strong>de connotatie stuurt het oordeel van de lezer</strong>. Een tekst die "
                  "consequent over <em>het probleem</em> spreekt in plaats van over <em>de uitdaging</em>, "
                  "<strong>kleurt hoe de lezer de zaak inschat</strong>. Twijfel je in een zakelijke tekst "
                  "tussen twee synoniemen, let dan <strong>op de gevoelswaarde en op het register</strong>."),
        ]),
        dict(kop="Herkomst van woorden", blokken=[
            ("p", tabel(["Begrip", "Wat het is"], [
                ["Leenwoord", "een woord dat uit een andere taal is overgenomen"],
                ["Bastaardwoord", "een leenwoord dat aan het Nederlands is aangepast"],
                ["Anglicisme", "een woord of wending overgenomen uit het Engels"],
                ["Belgicisme", "een woord of wending die alleen in België gebruikt wordt"],
                ["Dialectisme", "een woord uit een dialect in de standaardtaal"],
                ["Purisme", "een zelf gevormd woord dat een leenwoord moet vervangen"],
                ["Neologisme", "een nieuw gevormd woord: appen, googelen, streamen"],
                ["Archaïsme", "een verouderd woord dat nauwelijks nog gebruikt wordt"],
            ])),
            ("p", "<strong>Een bastaardwoord is dus geen woord dat van oudsher in het Nederlands "
                  "bestaat</strong>, maar een ingeburgerd leenwoord. En <strong>een archaïsme is geen woord "
                  "dat pas ontstaan is</strong>: dat is juist een neologisme."),
        ]),
    ],
    onthoud=[
        "Synoniemen betekenen ongeveer hetzelfde, antoniemen het tegengestelde.",
        "Homoniemen hebben dezelfde vorm maar een heel andere betekenis.",
        "Het hyperoniem is het ruimere woord, het hyponiem het engere.",
        "In de poot van de tafel is poot figuurlijk gebruikt.",
        "Een pleonasme is een overbodige toevoeging die al in het woord zit: een witte schimmel.",
        "Een contaminatie versmelt twee uitdrukkingen tot één foute, zoals duur kosten.",
        "Denotatie is de kale betekenis, connotatie de bijklank.",
        "Een eufemisme verzacht, een dysfemisme maakt iets ruwer of harder dan nodig.",
        "Een bastaardwoord is een leenwoord dat aan het Nederlands is aangepast.",
    ],
)

# ───────────────────────── 20. Schrijven en schriftelijke interactie
BUNDELS["schrijven-en-schriftelijke-interactie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Schrijven en schriftelijke interactie",
    onder="De tekstdoelen, de beoordelingscriteria en de strategieën die een schrijfopdracht doen slagen.",
    secties=[
        dict(kop="Tekstdoelen", blokken=[
            ("p", "Een schrijfopdracht heeft altijd een <strong>tekstdoel</strong>: "
                  "<strong>informatie geven en vragen</strong>, <strong>iemand iets uitleggen</strong>, "
                  "<strong>je mening geven</strong>, <strong>iemand overtuigen</strong>, "
                  "<strong>iets vertellen</strong>, <strong>in dialoog gaan</strong> of "
                  "<strong>creatief zijn met taal</strong>. <strong>Een tekst zo lang mogelijk maken is "
                  "geen doel.</strong>"),
            ("p", tabel(["Opdracht", "Tekstdoel"], [
                ["Een brochure over een jeugdhuis", "informatie geven"],
                ["Een stappenplan voor een spel", "iemand iets uitleggen"],
                ["Een recensie van een film", "je mening geven"],
                ["Een antirookpamflet of een sollicitatie", "iemand overtuigen"],
                ["Een mail over je vakantiejob", "iets vertellen"],
                ["Een flyer voor een evenement", "creatief zijn met taal"],
            ])),
            ("p", "<strong>Creatief zijn met taal</strong> betekent technieken inzetten zoals "
                  "<strong>rijm, ritme en humor</strong>, en spelen met lay-out, met beeld en taal, met "
                  "tijd en ruimte, met verteltechnieken of met stijlfiguren. Een <strong>flyer</strong> "
                  "werkt daarom met <strong>lay-out en met korte, pakkende zinnen</strong>: hij moet in één "
                  "oogopslag werken."),
        ]),
        dict(kop="De beoordelingscriteria", blokken=[
            ("p", tabel(["Criterium", "Wat men nakijkt"], [
                ["Taakvoltooiing", "het tekstdoel is bereikt, de inhoud is volledig, helder, correct en ter zake"],
                ["Woordenschat", "frequente én minder frequente woorden uit het Standaardnederlands, en figuurlijke taal"],
                ["Grammatica en zinsbouw", "correcte en gevarieerde zinnen"],
                ["Tekststructuur en samenhang", "signaalwoorden, een herkenbare opbouw, één deelonderwerp per alinea"],
                ["Register en beleefdheidsconventies", "een formele of informele toon, passend bij de situatie"],
                ["Spelling en leestekengebruik", "alleen bij schrijven en schriftelijke interactie"],
                ["Tekstopbouw en lay-out", "titels en tussentitels waar dat nodig is"],
            ])),
            ("p", "<strong>Spelling en leestekengebruik</strong> en <strong>tekstopbouw en lay-out</strong> "
                  "zijn aparte criteria die enkel bij de geschreven vorm gelden; <strong>uitspraak en "
                  "intonatie</strong> horen bij spreken. <strong>Een inhoudelijk sterke tekst vol fouten "
                  "verliest punten op het spellingcriterium</strong>: het ene criterium goed doen "
                  "compenseert het andere niet."),
            ("p", "<strong>Woordenschat</strong> betekent niet alleen eenvoudige woorden; men verwacht ook "
                  "<strong>minder frequente</strong> en <strong>figuurlijke</strong> taal. "
                  "<strong>Register</strong> staat apart naast grammatica omdat <strong>een foutloze tekst "
                  "toch ongepast kan klinken</strong>."),
            ("p", "Een goed gestructureerde tekst telt <strong>drie</strong> delen: "
                  "<strong>inleiding, midden en slot</strong>. Even lange zinnen maken een tekst juist "
                  "eentonig; samenhang komt van <strong>signaalwoorden</strong>, <strong>een herkenbare "
                  "opbouw</strong> en <strong>één deelonderwerp per alinea</strong>."),
        ]),
        dict(kop="Schrijfstrategieën", blokken=[
            ("p", "Vóór je begint, bepaal je <strong>je doel, je ontvanger en je kanaal</strong>: het "
                  "communicatiemodel is ook een schrijfstrategie. Daarna maak je <strong>een schrijfplan "
                  "met kernwoorden</strong>, kies je <strong>een vaste tekststructuur</strong> en "
                  "<strong>stel je jezelf vragen over het onderwerp</strong>. <strong>Beginnen zonder enig "
                  "plan vooraf</strong> levert meestal een tekst zonder lijn op."),
            ("p", "Vind je de juiste formulering niet, dan <strong>omschrijf je het of zoek je het woord "
                  "op</strong>. Op het digitale examen mag je <strong>een spellingcontrole en een eenvoudig "
                  "woordenboek gebruiken</strong>; oefen er thuis mee, zodat je ze vlot hanteert. "
                  "<strong>Nalezen blijft nodig</strong>: een spellingcontrole vindt geen fouten die "
                  "toevallig bestaande woorden opleveren, zoals <em>word</em> in plaats van <em>wordt</em>."),
            ("p", "<strong>Je tekst grondig nalezen</strong> op helder, gepast, correct en vlot is de "
                  "laatste stap. Lees hem ook eens <strong>hardop</strong>: <strong>je hoort dan waar de "
                  "zinnen stroef lopen</strong>. Wat jij struikelend voorleest, leest je lezer ook "
                  "struikelend."),
            ("p", "Verwerk je informatie uit bronnen, dan <strong>verwijs je er correct naar</strong>, "
                  "<strong>weeg je af hoe betrouwbaar ze zijn</strong> en <strong>verwerk je ze in je eigen "
                  "woorden</strong>. <strong>Bronvermelding</strong> is het correct aangeven waar je "
                  "informatie vandaan komt; zonder vermelding lijkt andermans werk het jouwe."),
        ]),
        dict(kop="Schriftelijke interactie", blokken=[
            ("p", "Het verschil met een gewone schrijfopdracht: <strong>bij interactie reageer je op wat "
                  "een ander geschreven heeft</strong>. Op een online forum <strong>speel je in op wat de "
                  "ander geschreven heeft</strong>; wie enkel zijn eigen tekst plaatst, voert geen gesprek."),
            ("p", "Bij een <strong>formele mail aan een instantie</strong> horen <strong>een gepaste "
                  "aanspreking</strong>, <strong>een duidelijke onderwerpregel</strong> (kort en duidelijk, "
                  "want de ontvanger beslist er vaak op of hij de mail opent) en <strong>een verzorgde "
                  "slotgroet</strong>. <strong>Emoji's horen bij informele communicatie</strong>: een "
                  "smiley in een zakelijke mail <strong>botst met het register</strong>."),
            ("p", "Schrijf je een <strong>klacht aan een bedrijf</strong>, dan zet je in de inleiding "
                  "<strong>waarover je schrijft en wat er gebeurd is</strong>; wat je vraagt, komt daarna. "
                  "Een tekst die een <strong>probleem en een oplossing</strong> behandelt, volgt de "
                  "<strong>probleemstructuur</strong>."),
            ("p", "Je taal aanpassen aan je ontvanger loont, want <strong>de boodschap komt dan beter "
                  "aan</strong>. Bij een <strong>verslag van een onderzoeksopdracht</strong> hoort "
                  "<strong>academische en objectieve taal</strong>, geen losse spreektaal."),
        ]),
    ],
    onthoud=[
        "Een tekst zo lang mogelijk maken is geen doel.",
        "Creatief zijn met taal betekent technieken inzetten zoals rijm, ritme en humor.",
        "Spelling en leestekengebruik gelden enkel bij de geschreven vorm.",
        "Het ene criterium goed doen compenseert het andere niet.",
        "Een foutloze tekst kan toch ongepast klinken; daarom staat register apart.",
        "Bepaal vooraf je doel, je ontvanger en je kanaal, en maak een schrijfplan met kernwoorden.",
        "Een spellingcontrole vindt geen fouten die toevallig bestaande woorden opleveren.",
        "Bij interactie reageer je op wat een ander geschreven heeft.",
        "Een formele mail heeft een gepaste aanspreking, een duidelijke onderwerpregel en een verzorgde slotgroet.",
    ],
)

# ───────────────────────── 21. Spreken en gesprekken voeren
BUNDELS["spreken-en-gesprekken-voeren-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Spreken en gesprekken voeren",
    onder="De spreekopdracht, het gesprek, de criteria die enkel mondeling gelden en de gespreksstrategieën.",
    secties=[
        dict(kop="De spreekopdracht", blokken=[
            ("p", "Dezelfde <strong>tekstdoelen</strong> als bij schrijven gelden ook mondeling: "
                  "<strong>iets uitleggen</strong>, <strong>je mening geven</strong>, <strong>iets "
                  "vertellen</strong>, overtuigen, in dialoog gaan. <strong>Zo lang mogelijk aan het woord "
                  "blijven is geen doel.</strong>"),
            ("p", "Je maakt een <strong>spreekplan</strong> met kernwoorden. Je spreekbeurt volledig "
                  "<strong>uitschrijven en voorlezen</strong> is riskant: <strong>je klinkt monotoon en "
                  "verliest je publiek</strong>, want voorgelezen taal heeft een ander ritme dan gesproken "
                  "taal."),
            ("p", "De <strong>IMS-structuur</strong> geldt ook mondeling. Je begint met <strong>een "
                  "inleiding die je onderwerp aankondigt</strong>; in het <strong>slot</strong> hoort "
                  "<strong>een samenvatting of een besluit</strong>, geen nieuw argument. Je luisteraar "
                  "kan niet terugbladeren, dus maak je structuur hoorbaar met <strong>signaalwoorden zoals "
                  "<em>ten eerste</em> en <em>tot slot</em></strong>, <strong>een korte aankondiging van je "
                  "opbouw</strong> en <strong>een pauze tussen twee onderdelen</strong>."),
            ("p", "Wordt je spreekopdracht <strong>thuis opgenomen</strong>, dan <strong>kan je oefenen en "
                  "opnieuw opnemen</strong>. De beoordeling blijft dezelfde. Oefen <strong>hardop</strong>: "
                  "<strong>je hoort waar je struikelt en hoe lang je spreekt</strong>."),
        ]),
        dict(kop="De criteria bij spreken", blokken=[
            ("p", "Naast taakvoltooiing, woordenschat, grammatica en zinsbouw, tekststructuur en samenhang, "
                  "en register en beleefdheidsconventies gelden bij spreken <strong>drie criteria die "
                  "schrijven niet heeft</strong>: <strong>lichaamstaal</strong>, <strong>vlotheid</strong> "
                  "en <strong>uitspraak en intonatie</strong>. <strong>Spelling en leestekengebruik</strong> "
                  "horen juist alleen bij geschreven taal."),
            ("p", tabel(["Criterium", "Wat het betekent"], [
                ["Lichaamstaal", "oogcontact, houding en gebaren"],
                ["Vlotheid", "doorspreken zonder lange haperingen, niet zo snel mogelijk"],
                ["Uitspraak", "de klanken van de taal correct vormen"],
                ["Intonatie", "de melodie en de klemtoon in je zinnen"],
                ["Taakvoltooiing", "je boodschap is volledig en ter zake"],
                ["Grammatica en zinsbouw", "correcte en gevarieerde zinnen, mondeling én schriftelijk"],
            ])),
            ("p", "<strong>Vlotheid betekent niet dat je nooit een pauze mag laten vallen</strong>: een "
                  "bewuste pauze maakt je betoog juist sterker. Het gaat over haperen, niet over stilte. En "
                  "<strong>een spreker die vlot klinkt maar het onderwerp niet behandelt, scoort niet goed "
                  "op taakvoltooiing</strong>."),
            ("p", "<strong>Bij spreken wordt niet enkel gelet op wat je zegt.</strong> Lichaamstaal, "
                  "vlotheid, uitspraak en intonatie gaan allemaal over <strong>hoe</strong> je het zegt, en "
                  "ze worden alle vier beoordeeld. <strong>Oogcontact</strong> is belangrijk omdat <strong>je "
                  "je publiek betrekt en hun reactie ziet</strong>, en zo kan bijsturen. Merk je dat je "
                  "publiek je niet volgt, dan <strong>herneem je het punt in andere woorden</strong>."),
            ("p", "Ook <strong>register</strong> telt mondeling. Spreek je voor een onbekend publiek van "
                  "volwassenen, dan kies je <strong>verzorgde standaardtaal</strong>. En <strong>figuurlijke "
                  "taal</strong> mag: ze maakt je verhaal levendiger."),
        ]),
        dict(kop="Het gesprek", blokken=[
            ("p", "Het verschil met een spreekopdracht: <strong>bij een gesprek reageer je op een "
                  "ander</strong>. Luisteren, inpikken en doorvragen horen erbij. Op het examen krijg je "
                  "<strong>vijftien</strong> minuten voorbereiding voor een gesprek van ongeveer tien "
                  "minuten. Ook een gesprek <strong>over een boek van de lectuurlijst</strong> kan deel "
                  "uitmaken van het examen: de literaire competentie komt aan bod bij schrijven, bij "
                  "schriftelijke interactie of bij het gesprek."),
            ("p", "In een gesprek <strong>neem je zelf het woord</strong>, <strong>geef je het woord door "
                  "aan een ander</strong> en <strong>vat je samen wat er gezegd is</strong>. Samenvatten "
                  "loont: <strong>je toont dat je luistert en checkt of je het goed begreep</strong>. "
                  "<strong>Wie nooit doorvraagt, haalt niet het hoogste niveau van interactie.</strong>"),
            ("p", "Ben je het oneens, dan <strong>verwoord je je standpunt met argumenten</strong>. In "
                  "dialoog gaan betekent je eigen standpunt onderbouwen én dat van de ander laten staan."),
            ("p", "Een gesprek <strong>beleefd afsluiten</strong> doe je door <strong>te bedanken voor het "
                  "gesprek</strong>, <strong>kort samen te vatten waar jullie geraakt zijn</strong> en "
                  "<strong>een gepaste afscheidsformule te gebruiken</strong>. "
                  "<strong>Beleefdheidsconventies gelden niet alleen in geschreven taal.</strong>"),
        ]),
        dict(kop="Gespreksstrategieën", blokken=[
            ("p", "Begrijp je iets niet, dan <strong>vraag je om verduidelijking</strong>, <strong>vat je "
                  "samen wat je wel begrepen hebt</strong> of <strong>vraag je of de ander het wil "
                  "herhalen</strong>. <strong>Doen alsof je het begrepen hebt</strong> loopt verderop altijd "
                  "vast. Gebruikt je gesprekspartner een woord dat je niet kent, dan <strong>vraag je wat "
                  "het betekent</strong>."),
            ("p", "Krijg je een onverwachte vraag, dan <strong>neem je even de tijd en antwoord je "
                  "dan</strong>. Spontaan reageren mag een korte denkpauze bevatten; dat klinkt beter dan "
                  "een halsoverkop antwoord."),
            ("p", "Bereid een gesprek voor met <strong>kernwoorden en argumenten op papier</strong>, niet "
                  "met een volledig uitgeschreven script: een gesprek verloopt nooit zoals je het plant."),
            ("p", "Verwoord je je <strong>leeservaring</strong> bij een boek, dan <strong>zeg je wat het "
                  "boek bij je opriep en waarom</strong>. Dat is iets anders dan het verhaal navertellen of "
                  "de achterflap opzeggen."),
        ]),
    ],
    onthoud=[
        "Zo lang mogelijk aan het woord blijven is geen doel.",
        "Maak een spreekplan met kernwoorden; voorlezen klinkt monotoon.",
        "In het slot hoort een samenvatting of een besluit, geen nieuw argument.",
        "Alleen bij spreken: lichaamstaal, vlotheid en uitspraak en intonatie.",
        "Vlotheid gaat over haperen, niet over stilte.",
        "Bij een gesprek reageer je op een ander.",
        "Op het examen krijg je vijftien minuten voorbereiding voor een gesprek van ongeveer tien minuten.",
        "Wie nooit doorvraagt, haalt niet het hoogste niveau van interactie.",
        "Begrijp je iets niet, vraag dan om verduidelijking.",
    ],
)

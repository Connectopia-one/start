# -*- coding: utf-8 -*-
"""De leerbundels voor Nederlands op 🌍 Beyond dubbele finaliteit.

Gebaseerd op de twee vakfiches Nederlands van de 3de graad dubbele finaliteit,
geldig vanaf 1 januari 2027. Fiche 1 is het taalexamen (spreken, schriftelijke
interactie, schrijven, gesprekken voeren), fiche 2 het receptieve examen (lezen
40 %, luisteren 40 %, literatuur 10 %, taalbeschouwing 10 %).

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../beyond-dubbele-finaliteit/nederlands.json`
doet daar het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-beyond-dubbele-finaliteit". Nederlands bestaat
ook op ✨ Spark, op 🚀 Boost en op 🌍 Beyond doorstroom, en daar komen
thematitels in voor die hier bijna of helemaal gelijk klinken.

Geen enkel citaat in deze bundels is van een bestaande dichter of schrijver.
Waar een voorbeeldregel of een voorbeeldzin staat, is die zelf geschreven en
staat er geen naam bij.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Nederlands"
DF = "🌍 Beyond dubbele finaliteit — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────── 1. Onderwerp, hoofdgedachte en hoofdpunten
BUNDELS["onderwerp-hoofdgedachte-en-hoofdpunten-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Onderwerp, hoofdgedachte en hoofdpunten",
    onder="Waarover gaat de tekst, wat wil hij zeggen, en waarmee onderbouwt hij dat.",
    secties=[
        dict(kop="Drie vragen bij elke tekst", blokken=[
            ("p", "Bij elke lees- of luistertekst stel je dezelfde drie vragen. Ze horen bij elkaar en "
                  "ze zijn niet hetzelfde."),
            ("p", tabel(["Vraag", "Wat je zoekt", "In welke vorm"], [
                ["Het <strong>onderwerp</strong>", "waarover de tekst gaat", "in één of enkele woorden"],
                ["De <strong>hoofdgedachte</strong>", "de belangrijkste boodschap", "in één volledige zin"],
                ["De <strong>hoofdpunten</strong>", "de inhoudelijke elementen die de hoofdgedachte ondersteunen", "vaak één per alinea"],
            ])),
            ("p", "Het <strong>onderwerp en de hoofdgedachte zijn dus niet hetzelfde</strong>. "
                  "'Videogames' is een onderwerp. '<strong>Dit spel is een van de slechtste van het "
                  "jaar</strong>' is een hoofdgedachte: er zit een boodschap in. Een "
                  "<strong>hoofdgedachte formuleer je het best als een volledige zin</strong>, want pas "
                  "in een zin staat er iets."),
            ("p", "Een <strong>tekst kan maar één onderwerp hebben, maar wel verschillende "
                  "hoofdpunten</strong>. Lees je 'Het spel is een mix van genres. Het spel is niet "
                  "origineel. De makers pleegden plagiaat', dan heb je <strong>de hoofdpunten van de "
                  "tekst</strong> voor je: drie elementen die samen de boodschap dragen."),
            ("kader", "<strong>Wie het onderwerp kent, kent daarmee nog niet de hoofdpunten.</strong> "
                      "Het onderwerp zegt alleen waarover het gaat. De hoofdpunten moet je uit de tekst halen."),
        ]),
        dict(kop="Waar je ze vindt", blokken=[
            ("p", "In een <strong>goed gestructureerde tekst staat de hoofdgedachte meestal in de "
                  "inleiding of in het slot</strong>. De schrijver kondigt ze aan of hij besluit ermee."),
            ("p", "Een <strong>titel geeft niet altijd de hoofdgedachte weer</strong>. Veel titels willen "
                  "alleen de aandacht trekken. Maar het kan: heet een artikel <strong>'Wonen in de stad "
                  "wordt onbetaalbaar'</strong>, dan is <strong>het onderwerp de huurprijzen in de "
                  "stad</strong> en <strong>geeft de titel hier wél de hoofdgedachte weer</strong>."),
            ("p", "<strong>Tussentitels</strong> leveren je de hoofdpunten in één oogopslag. Staan er "
                  "'Te duur', 'Te klein' en 'Te ver' boven de delen, dan heb je <strong>de drie "
                  "hoofdpunten in één oogopslag</strong>."),
            ("p", "Twee vragen helpen je om de hoofdgedachte te vinden: <strong>wat wil de schrijver dat "
                  "ik hierover denk?</strong> en <strong>wat zou ik iemand zeggen die de tekst niet "
                  "las?</strong> Wat je dan antwoordt, is de hoofdgedachte. Moet je in één zin zeggen wat "
                  "een podcast van twintig minuten je vertelde, dan geef je <strong>de "
                  "hoofdgedachte</strong>."),
            ("p", "Bij een <strong>luistertekst zoek je precies hetzelfde als bij een leestekst: "
                  "onderwerp, hoofdgedachte en hoofdpunten</strong>. Hoor je een reportage over "
                  "slaaptekort bij jongeren en besluit de reporter dat scholen later moeten beginnen, dan "
                  "is dat besluit <strong>de hoofdgedachte van de reportage</strong>."),
            ("p", "Het <strong>verschil tussen een hoofdpunt en een detail</strong>: <strong>een "
                  "hoofdpunt draagt de boodschap, een detail vult aan</strong>. Valt het weg en staat de "
                  "boodschap nog, dan was het een detail."),
        ]),
        dict(kop="Relevante informatie selecteren", blokken=[
            ("p", "<strong>Relevante informatie selecteren</strong> betekent <strong>uit de tekst halen "
                  "wat je voor je opdracht nodig hebt</strong>. <strong>Wat relevant is, hangt af van de "
                  "vraag die je moet beantwoorden</strong>, en van niets anders."),
            ("p", "Noemt een tekst over elektrische auto's de prijs, het bereik en de laadtijd, en gaat "
                  "je opdracht over de kostprijs, dan is <strong>de prijs en wat het laden kost</strong> "
                  "relevant. Het bereik is dan interessant maar niet nodig. Moet je uit twee artikels de "
                  "openingsuren van een museum halen, dan <strong>zoek je in beide teksten enkel naar die "
                  "uren</strong>: dat is <strong>scannen</strong> of <strong>zoekend lezen</strong>, "
                  "snel over een tekst gaan tot je vindt wat je zoekt."),
            ("p", "Je mag bij een opdracht <strong>informatie uit meer dan één tekst door elkaar "
                  "gebruiken</strong>. Twee afspraken horen daarbij: <strong>je mag informatie uit "
                  "verschillende teksten combineren</strong>, en <strong>je vermeldt uit welke tekst je "
                  "iets haalt</strong>."),
            ("p", "Geven <strong>twee artikels over hetzelfde onderwerp verschillende cijfers</strong>, "
                  "dan <strong>kijk je van wanneer elk cijfer is en van wie</strong>. Meestal verklaart "
                  "dat het verschil al."),
        ]),
        dict(kop="Samenvatten en notities nemen", blokken=[
            ("p", "Een <strong>samenvatting</strong> is <strong>de hoofdgedachte en de hoofdpunten in "
                  "eigen woorden</strong>, een korte weergave van een tekst. <strong>De voorbeelden en de "
                  "details horen er niet in</strong>, en een <strong>samenvatting mag nooit langer zijn "
                  "dan de tekst zelf</strong>. <strong>Wie goed samenvat, gebruikt juist niet zo veel "
                  "zinnen als mogelijk uit de oorspronkelijke tekst</strong>: herformuleren bewijst dat "
                  "je het begrepen hebt."),
            ("p", "<strong>Notities</strong> nemen mag kort. <strong>Afkortingen, symbolen en "
                  "telegramstijl mogen</strong>, en zulke notities zijn <strong>even bruikbaar als "
                  "notities in volle zinnen</strong>. Twee eisen blijven: <strong>je notities sluiten aan "
                  "bij de inhoud van de tekst</strong>, en je kan ze achteraf nog lezen."),
            ("p", "Notities bij een instructiefilmpje kan je zetten <strong>in een schema, een tabel of "
                  "een mindmap</strong>. Bij een <strong>luistertekst neem je het best notities terwijl "
                  "je luistert</strong>, want je kan niet terugspoelen. Achteraf gebruik je ze "
                  "<strong>om een samenvatting te maken of een vraag te beantwoorden</strong>."),
        ]),
    ],
    onthoud=[
        "Onderwerp: enkele woorden. Hoofdgedachte: één volledige zin. Hoofdpunten: de elementen die ze dragen.",
        "De hoofdgedachte staat meestal in de inleiding of het slot; tussentitels geven je de hoofdpunten.",
        "Relevant is wat je opdracht nodig heeft; uit meerdere teksten mag, met vermelding van de bron.",
        "Een samenvatting: hoofdgedachte en hoofdpunten in eigen woorden, korter dan de tekst, zonder details.",
        "Notities in telegramstijl mogen, bij luisteren terwijl je luistert.",
    ],
)

# ───────────────────── 2. Tekstsoorten en teksttypes
BUNDELS["tekstsoorten-en-teksttypes-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Tekstsoorten en teksttypes",
    onder="Zeven soorten lees- en luisterteksten, en de vraag wat de zender met je wil.",
    secties=[
        dict(kop="De zeven soorten", blokken=[
            ("p", "Elke tekst die je leest of hoort, heeft een bedoeling. Naar die bedoeling deel je "
                  "teksten in. Zeven soorten komen steeds terug."),
            ("p", tabel(["Soort", "Wat ze doet", "Voorbeelden"], [
                ["<strong>Informatief</strong>", "geeft je informatie over een onderwerp", "een interview in de krant, een stuk uit een leerboek"],
                ["<strong>Persuasief</strong>", "probeert je te overtuigen of te beïnvloeden", "reclame, propaganda, nepnieuws, een publireportage"],
                ["<strong>Opiniërend</strong>", "iemand geeft er zijn mening", "een hotelbeoordeling op een reissite, een productreview op een webwinkel, een protestlied"],
                ["<strong>Argumentatief</strong>", "argumenten die een standpunt ondersteunen", "een betoog, een debat"],
                ["<strong>Prescriptief</strong>", "geeft je instructies over hoe je iets doet", "een handleiding, een bijsluiter, een schoolreglement"],
                ["<strong>Narratief</strong>", "een narratieve tekst vertelt een verhaal", "een true crime podcast, een reisverslag"],
                ["<strong>Literair</strong>", "heeft een esthetische waarde en speelt in op emoties", "een kortverhaal, een strip, stand-upcomedy"],
            ])),
            ("p", "<strong>Nepnieuws is een voorbeeld van een persuasieve tekst</strong>: het wil je iets "
                  "laten denken. Een <strong>interview in de krant is in de eerste plaats een "
                  "informatieve tekst</strong>. Een <strong>strip kan net zo goed een literaire tekst "
                  "zijn</strong>, en <strong>stand-upcomedy ook</strong>. Een <strong>debat is een "
                  "argumentatieve tekstvorm</strong>. Een <strong>schoolreglement en "
                  "veiligheidsvoorschriften in een bedrijf zijn beide prescriptieve teksten</strong>."),
            ("p", "Een <strong>protestlied hoort niet enkel bij de literaire teksten</strong>: het staat "
                  "in de eerste plaats bij de <strong>opiniërende</strong> teksten, want iemand zegt er "
                  "wat hij vindt. Als lied heeft het natuurlijk ook een esthetische kant."),
        ]),
        dict(kop="Waarom je de soort bepaalt", blokken=[
            ("p", "De vraag die je het best helpt om de soort te bepalen, is: <strong>wat wil de zender "
                  "met deze tekst bereiken?</strong> Daarom is het nuttig te weten tot welke soort een "
                  "tekst hoort: <strong>je weet dan wat de zender met je wil</strong>, en dus hoe "
                  "kritisch je moet lezen."),
            ("p", "Soms leent een schrijver de vorm van een andere soort. Een "
                  "<strong>publireportage</strong> ziet eruit als een artikel maar is <strong>betaald "
                  "door een bedrijf</strong>: het is een <strong>persuasieve tekst</strong>. Waarom doet "
                  "iemand dat? <strong>Omdat een neutraal uitziende tekst meer vertrouwen krijgt.</strong>"),
            ("p", "Zo lees je ook een <strong>campagne tegen te snel rijden die een zwaar ongeval "
                  "toont</strong> als een <strong>persuasieve tekst</strong>, en een "
                  "<strong>folder van een politieke partij met 'Genoeg is genoeg' in grote "
                  "letters</strong> als een <strong>persuasieve kreet die een gevoel moet "
                  "oproepen</strong>. Een <strong>reactie op een forum</strong> als 'Dit toestel ging bij "
                  "mij na twee maanden stuk, koop het niet' is een <strong>opiniërende tekst</strong>. "
                  "Een <strong>true crime podcast</strong> die een moordzaak van begin tot einde vertelt, "
                  "is <strong>narratief</strong>. Een <strong>bijsluiter van een geneesmiddel</strong> "
                  "die zegt hoeveel je mag innemen, is <strong>prescriptief</strong>."),
        ]),
        dict(kop="Teksten die soorten combineren", blokken=[
            ("p", "<strong>Veel teksten combineren meer dan één bedoeling</strong>, en een "
                  "<strong>tekst kan tegelijk informatief en opiniërend zijn</strong>. Je zoekt dan wat "
                  "de belangrijkste bedoeling is."),
            ("p", "Een <strong>recensie</strong> is het schoolvoorbeeld: <strong>ze kan zowel informatief "
                  "als opiniërend zijn</strong>, want <strong>ze zegt zowel waarover iets gaat als wat de "
                  "schrijver vindt</strong>. Een <strong>handleiding mag ook informatieve stukken "
                  "bevatten</strong> en blijft dan prescriptief. Een <strong>gedicht dat het verhaal van "
                  "een schipbreuk vertelt</strong>, is <strong>tegelijk literair en narratief</strong>. "
                  "En een <strong>videoblogger die vertelt wat hem die dag overkwam en dan een merk "
                  "aanraadt</strong>, laat zijn tekst <strong>van narratief naar persuasief "
                  "verschuiven</strong>."),
            ("kader", "De soort hangt af van de bedoeling, niet van het kanaal. Een <strong>reportage op "
                      "televisie en een krantenartikel horen daarom niet per definitie tot een andere "
                      "tekstsoort</strong>, ook al verschilt het kanaal."),
            ("p", "Bij een <strong>luistertekst gebruik je dezelfde indeling in soorten als bij een "
                  "leestekst</strong>. En let op de taal: de <strong>teksten op je examen staan niet "
                  "altijd in standaardtaal</strong>. Een <strong>tekst in dialect of jongerentaal kan er "
                  "wel degelijk in voorkomen</strong>."),
        ]),
    ],
    onthoud=[
        "Zeven soorten: informatief, persuasief, opiniërend, argumentatief, prescriptief, narratief, literair.",
        "De vraag die beslist: wat wil de zender met deze tekst bereiken?",
        "Nepnieuws, reclame, propaganda en een publireportage zijn persuasief.",
        "Veel teksten combineren soorten; een recensie is informatief én opiniërend.",
        "Het kanaal bepaalt de soort niet, en teksten staan niet altijd in standaardtaal.",
    ],
)

# ───────────────────── 3. Bronnen beoordelen
BUNDELS["bronnen-beoordelen-betrouwbaarheid-nepnieuws-en-framing-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Bronnen beoordelen: betrouwbaarheid, nepnieuws en framing",
    onder="Een lijst vragen bij elke bron, en wat framing met een waar bericht doet.",
    secties=[
        dict(kop="De criteria, vraag per vraag", blokken=[
            ("p", "Voor je een tekst gebruikt, loop je een vaste lijst vragen af. Ze gaan over twee "
                  "dingen: is dit juist, en wat wil de zender?"),
            ("p", tabel(["Criterium", "Waarom het telt"], [
                ["<strong>Wordt de auteur vermeld?</strong>", "anders weet je niet wie voor de inhoud verantwoordelijk is"],
                ["<strong>Wie publiceert het artikel?</strong>", "welke organisatie of site de tekst naar buiten brengt"],
                ["<strong>Welke bronnen worden in de tekst gebruikt?</strong>", "dan kan je nagaan waarop de uitspraken steunen"],
                ["<strong>Is het ook in andere betrouwbare bronnen te vinden?</strong>", "één losse bron kan zich vergissen of liegen"],
                ["<strong>Van wanneer is het bericht?</strong>", "een cijfer van vijf jaar oud is niet voor elke vraag bruikbaar"],
                ["<strong>Feiten of meningen?</strong>", "dat bepaalt hoe je de tekst mag gebruiken"],
                ["<strong>Wat is de bedoeling van de zender?</strong>", "wat hij met de tekst bij jou wil bereiken"],
                ["<strong>Is er sprake van framing?</strong>", "de invalshoek stuurt je, ook zonder onwaarheid"],
            ])),
            ("p", "Twee van die vragen gaan niet over de juistheid maar over de bedoeling: <strong>is het "
                  "bericht reclame, nepnieuws of propaganda?</strong> en <strong>is de titel neutraal of "
                  "dient hij om clicks te krijgen?</strong> Een <strong>titel die vooral moet aanzetten "
                  "tot klikken, is een reden om kritisch verder te lezen</strong>. Zo'n titel heet "
                  "<strong>clickbait</strong>, of een <strong>clickbaittitel</strong>: ze is er om mensen te "
                  "laten doorklikken."),
            ("kader", "Een <strong>website die er professioneel uitziet, is daarom niet "
                      "betrouwbaar</strong>: een goede vormgeving is goedkoop. En een "
                      "<strong>grafiek in een bericht maakt dat bericht niet automatisch "
                      "betrouwbaar</strong>. Ook <strong>hoeveel volgers de zender heeft</strong> zegt "
                      "niets: volgers zijn te koop."),
        ]),
        dict(kop="Nepnieuws, reclame en propaganda", blokken=[
            ("p", "<strong>Nepnieuws</strong> of <strong>fake news</strong> zijn <strong>berichten die "
                  "bewust onwaar zijn en toch als nieuws worden verspreid</strong>. Welke signalen "
                  "samen daarop wijzen: <strong>geen auteur en geen bronvermelding</strong>, en "
                  "<strong>enkel verspreid via sociale media, met een schreeuwende titel</strong>."),
            ("p", "Het <strong>verschil tussen reclame en propaganda</strong>: <strong>reclame wil je "
                  "iets laten kopen, propaganda iets laten denken</strong>. Een "
                  "<strong>publireportage</strong> is een bericht dat eruitziet als een artikel maar door "
                  "een bedrijf betaald is. Een <strong>influencer die betaald wordt om positief te zijn "
                  "over een spel, maakt daarmee wél reclame</strong>, ook al klinkt het als een mening. "
                  "Een <strong>reclamespot met een man in een witte jas</strong> die het product "
                  "aanraadt, gebruikt een <strong>techniek</strong>: <strong>een beroep op gezag dat hier niet bewezen is</strong>."),
            ("p", "Praktische regels. Duikt een bericht <strong>alleen op sociale media</strong> op en "
                  "nergens anders, dan <strong>zoek je eerst of een onafhankelijke bron het ook "
                  "meldt</strong>. Melden <strong>twee sites hetzelfde maar verwijst de tweede naar de "
                  "eerste</strong>, dan heb je <strong>één bron, want de tweede voegt niets toe</strong>. "
                  "De beste manier om een <strong>opvallende bewering te controleren</strong> is "
                  "<strong>de oorspronkelijke bron van de bewering opzoeken</strong>."),
            ("p", "Zegt een bericht '<strong>Wetenschappers bewijzen dat chocolade slank maakt</strong>', "
                  "dan valt als eerste op dat <strong>er niet gezegd wordt welke wetenschappers of welk "
                  "onderzoek</strong>. En noemt een site zich '<strong>onafhankelijk "
                  "nieuwsplatform</strong>' zonder ergens een auteur of redactie te vermelden, dan "
                  "besluit je: <strong>de naam zegt niets, het ontbreken van een redactie wel iets</strong>. "
                  "Let wel: een <strong>bericht zonder vermelde auteur is daarmee niet bewezen "
                  "onwaar</strong>. Het is een reden om verder te kijken, geen vonnis."),
        ]),
        dict(kop="Framing", blokken=[
            ("p", "<strong>Framing</strong> is <strong>het bewust kiezen van een invalshoek, waardoor je "
                  "iets in een bepaald licht ziet</strong>. Het bijzondere eraan: <strong>framing kan "
                  "werken zonder dat er iets onwaar is</strong>, en <strong>de woordkeuze van een bericht "
                  "is al een vorm van framing</strong>."),
            ("p", "Schrijft de ene krant '<strong>de regering besliste</strong>' en de andere '<strong>de "
                  "regering drukte door</strong>', dan is dat <strong>framing door woordkeuze</strong>. "
                  "Dezelfde beslissing, een ander beeld. <strong>Framing kan ook ontstaan door iets juist "
                  "niet te vermelden</strong>: wat je weglaat, bestaat voor de lezer niet. Daarom kan "
                  "<strong>een tekst die enkel feiten bevat, toch een eenzijdig beeld geven</strong>."),
            ("p", "Er is nog een verschijnsel: het <strong>herhalingseffect</strong>. Een bericht lijkt "
                  "betrouwbaar <strong>omdat je het al vaak zag</strong>, niet omdat het beter "
                  "onderbouwd is."),
            ("p", "Over de bedoeling van de zender gelden twee dingen: <strong>dezelfde feiten kunnen met "
                  "verschillende bedoelingen gebracht worden</strong>, en <strong>de bedoeling bepaalt "
                  "hoe kritisch je moet lezen</strong>."),
        ]),
        dict(kop="Bruikbaar voor jouw doel", blokken=[
            ("p", "<strong>Of een bron bruikbaar is, hangt mee af van het doel waarvoor jij ze nodig "
                  "hebt.</strong> Een tekst met <strong>vooral meningen kan nog altijd nuttig zijn voor "
                  "je opdracht</strong>, en je mag zelfs <strong>een onbetrouwbare tekst gebruiken als "
                  "bron over wat de zender wil laten geloven</strong>."),
            ("p", "Een <strong>folder van een bank die uitlegt hoe sparen werkt</strong> is bruikbaar "
                  "<strong>voor de uitleg, met in gedachten dat de bank wil verkopen</strong>. Een "
                  "<strong>tekst van een belangenorganisatie is dus niet per definitie "
                  "onbruikbaar</strong>. Maar verkoopt een <strong>site over gezondheid onderaan elke "
                  "pagina dezelfde pillen</strong>, dan besluit je dat <strong>de informatie mee dient om "
                  "die pillen te verkopen</strong>."),
            ("p", "De datum doet mee. Zoek je de <strong>huidige prijs van een treinticket</strong> en "
                  "vind je een artikel uit 2019, dan <strong>zoek je verder, want dat cijfer is "
                  "verouderd</strong>. Bij het beoordelen van een <strong>luistertekst gelden dezelfde "
                  "criteria als bij een leestekst</strong>."),
        ]),
    ],
    onthoud=[
        "Vast rijtje: auteur, uitgever, gebruikte bronnen, elders te vinden, datum, feiten of meningen, bedoeling.",
        "Nepnieuws: geen auteur, geen bronnen, enkel sociale media, schreeuwende titel. Clickbait is een waarschuwing.",
        "Reclame wil je laten kopen, propaganda laten denken; een publireportage is betaald.",
        "Framing werkt zonder onwaarheid, door woordkeuze en door weglaten; herhaling maakt niet waar.",
        "Bruikbaar hangt af van jouw doel; zelfs een gekleurde bron zegt iets over haar zender.",
    ],
)

# ───────────────────── 4. Het communicatiemodel en ruis
BUNDELS["het-communicatiemodel-en-ruis-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Het communicatiemodel en ruis",
    onder="Zeven onderdelen waarmee je elke tekst en elk gesprek kan uitpluizen.",
    secties=[
        dict(kop="De zeven onderdelen", blokken=[
            ("p", "Het <strong>communicatiemodel</strong> is <strong>bruikbaar bij elke lees- en "
                  "luisteropdracht</strong>. Het bestaat uit zeven onderdelen: <strong>zender, boodschap "
                  "en ontvanger</strong>, plus <strong>kanaal, context, doel en effect</strong>."),
            ("p", tabel(["Onderdeel", "Wat het is"], [
                ["<strong>De zender</strong>", "wie de boodschap maakt en verstuurt"],
                ["<strong>De boodschap</strong>", "wat er gezegd of geschreven wordt"],
                ["<strong>De ontvanger</strong>", "degene voor wie de boodschap bedoeld is"],
                ["<strong>Het kanaal</strong>", "het middel waarlangs de boodschap verspreid wordt"],
                ["<strong>De context</strong>", "de tijd en de omstandigheden waarin ze valt"],
                ["<strong>Het doel</strong>", "de bedoeling die de zender met zijn boodschap heeft"],
                ["<strong>Het effect</strong>", "wat de boodschap bij de ontvanger teweegbrengt"],
            ])),
            ("p", "De vragen die je stelt, zijn dus: <strong>wie is de zender van de boodschap?</strong> "
                  "en <strong>via welk kanaal wordt de boodschap verspreid?</strong>, en zo verder voor "
                  "elk onderdeel. Stuurt een <strong>school een brief over een uitstap naar de "
                  "ouders</strong>, dan zijn <strong>de ouders</strong> de ontvanger."),
            ("p", "De <strong>zender van een tekst is niet altijd één persoon</strong>: een redactie, een "
                  "bedrijf of een partij kan ook zender zijn. Het is nuttig te weten <strong>voor wie een "
                  "tekst bedoeld is, omdat de zender zijn taal en inhoud op dat publiek afstemt</strong>. "
                  "En het is nuttig te weten dat een zender een belang heeft, <strong>omdat je dan nagaat "
                  "wat hij misschien niet vertelt</strong>."),
            ("kader", "<strong>Wie het communicatiemodel toepast, heeft daarmee de tekst nog niet "
                      "samengevat.</strong> Het model zegt wie wat waarom zegt. De inhoud moet je er nog "
                      "bij lezen."),
        ]),
        dict(kop="Doel en effect zijn twee dingen", blokken=[
            ("p", "Het <strong>doel van een boodschap</strong> kan zijn: <strong>informeren, overtuigen, "
                  "vermaken of aanzetten tot iets</strong>. Een <strong>boodschap kan tegelijk informeren "
                  "en overtuigen</strong>. Plakt een <strong>gemeente affiches over een "
                  "wegomlegging</strong>, dan is het doel <strong>de bewoners informeren zodat ze hun weg "
                  "aanpassen</strong>."),
            ("p", "<strong>Doel en effect vallen niet altijd samen</strong>, en daarom staan ze apart in "
                  "het model: <strong>het doel hoort bij de zender en het effect bij de "
                  "ontvanger</strong>. In een <strong>reclamespot zijn het doel van de zender en het "
                  "effect bij de kijker vaak niet hetzelfde</strong>, en <strong>hetzelfde bericht kan "
                  "bij twee ontvangers een ander effect hebben</strong>. Een <strong>zender kan het "
                  "effect van zijn boodschap dus niet volledig voorspellen.</strong>"),
            ("p", "Ook de vorm doet mee. Een <strong>mail met een lange, boze alinea in "
                  "hoofdletters</strong> komt aan als een schreeuw: <strong>de vorm heeft het effect "
                  "veranderd</strong>."),
        ]),
        dict(kop="Het kanaal en de context", blokken=[
            ("p", "Elk bericht heeft een kanaal, ook zonder toestel: een <strong>gesprek aan tafel heeft "
                  "wel degelijk een kanaal</strong>, namelijk het gesproken woord van aangezicht tot "
                  "aangezicht. Twee dingen gelden: <strong>het kanaal bepaalt mee hoe formeel je "
                  "schrijft</strong>, en <strong>hetzelfde bericht kan via meer dan één kanaal "
                  "gaan</strong>."),
            ("p", "Stuurt een <strong>bedrijf hetzelfde nieuws per mail naar het personeel en per "
                  "persbericht naar de kranten</strong>, dan verschillen <strong>het kanaal en het "
                  "publiek</strong>. Kiest een bedrijf voor <strong>een korte video in plaats van een "
                  "brief</strong>, dan verandert vooral <strong>het kanaal, en daarmee de aandacht die "
                  "het bericht krijgt</strong>. Let op: <strong>wie het kanaal van een bericht kent, weet "
                  "daarmee nog niet wie de zender is</strong>."),
            ("p", "De <strong>context</strong> hoort bij het model <strong>omdat dezelfde boodschap in "
                  "een andere tijd anders begrepen wordt</strong>. Een zin over thuiswerk uit 2015 leest "
                  "vandaag anders dan toen."),
        ]),
        dict(kop="Ruis", blokken=[
            ("p", "<strong>Ruis</strong> is <strong>alles wat de boodschap onderweg verstoort</strong>. "
                  "Er zijn twee soorten."),
            ("p", tabel(["Soort ruis", "Waar ze zit", "Voorbeeld"], [
                ["<strong>Externe ruis</strong>", "een storing buiten de ontvanger", "lawaai of een slechte verbinding"],
                ["<strong>Interne ruis</strong>", "een storing in de ontvanger zelf", "moeheid of een vooroordeel"],
            ])),
            ("p", "Luister je <strong>naar een podcast in een drukke trein</strong> en mis je de helft, "
                  "dan speelt <strong>externe ruis</strong> op. Legt een <strong>leerkracht iets uit "
                  "terwijl buiten een grasmachine draait</strong>, dan spelen <strong>het kanaal en de "
                  "externe ruis</strong> mee. Leest iemand <strong>een mail boos omdat hij de dag ervoor "
                  "ruzie had met de afzender</strong>, dan is dat <strong>interne ruis</strong>."),
            ("p", "<strong>Ruis kan de boodschap veranderen zonder dat de zender of de ontvanger het "
                  "merkt.</strong> Dat is precies waarom ze in het model staat."),
        ]),
        dict(kop="Het model op een verdacht bericht", blokken=[
            ("p", "Wordt een bericht <strong>enkel via sociale media verspreid, noemt het geen auteur en "
                  "wil het je naar een site lokken met veel advertenties</strong>, dan herken je "
                  "<strong>kanaal, zender en doel</strong>: het kanaal verraadt het, de zender ontbreekt, "
                  "en het doel zijn de bezoekers."),
            ("p", "Over <strong>nepnieuws</strong> zegt het model twee dingen: <strong>de zender blijft "
                  "bewust onbekend</strong>, en <strong>het kanaal is meestal sociale media</strong>."),
            ("p", "Krijg je <strong>een anonieme brief in de bus over een nieuw windpark</strong>, dan "
                  "zet je als eerste in je analyse <strong>dat de zender onbekend is</strong>. Alles wat "
                  "volgt, hangt daarvan af."),
        ]),
    ],
    onthoud=[
        "Zeven onderdelen: zender, boodschap, ontvanger, kanaal, context, doel, effect.",
        "Doel hoort bij de zender, effect bij de ontvanger; ze vallen vaak niet samen.",
        "Elk bericht heeft een kanaal, ook een gesprek; het kanaal bepaalt mee de toon.",
        "Externe ruis zit buiten de ontvanger, interne ruis in de ontvanger zelf.",
        "Bij een verdacht bericht: kanaal, zender en doel zeggen het meest.",
    ],
)

# ───────────────────── 5. Tekstopbouw, alineaverbanden en vaste tekststructuren
BUNDELS["tekstopbouw-alineaverbanden-en-vaste-tekststructuren-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Tekstopbouw, alineaverbanden en vaste tekststructuren",
    onder="De IMS-structuur, de verbanden tussen alinea's en de zeven vaste structuren.",
    secties=[
        dict(kop="Inleiding, midden en slot", blokken=[
            ("p", "De <strong>IMS-structuur</strong> van een tekst staat voor <strong>inleiding, midden "
                  "en slot</strong>."),
            ("p", "Over de <strong>inleiding</strong> gelden twee dingen: <strong>ze kondigt het "
                  "onderwerp aan</strong> en <strong>ze kan de aandacht van de lezer trekken</strong>. "
                  "In de inleiding van een tekst wordt dus <strong>vaak het onderwerp "
                  "aangekondigd</strong>. Over het <strong>slot</strong> ook twee: <strong>daar staat "
                  "vaak het besluit</strong> van de schrijver, en <strong>daar wordt de hoofdgedachte "
                  "vaak herhaald</strong>."),
            ("p", "In <strong>één alinea</strong> hoort volgens de afspraak <strong>één deelonderwerp van "
                  "de tekst</strong>. Een nieuwe alinea geef je aan met een witregel of met een "
                  "inspringing: <strong>in een gedrukte tekst mag dat dus ook met een inspringing en "
                  "niet enkel met een witregel</strong>."),
            ("p", "<strong>Tussentitels</strong> zijn de kopjes boven de delen van een tekst, die je "
                  "helpen bij het overzicht. <strong>Alinea's en tussentitels verhogen je "
                  "tekstbegrip</strong> <strong>omdat je per stuk weet waarover het gaat</strong>. Maar "
                  "een <strong>tekst zonder tussentitels kan toch een duidelijke structuur "
                  "hebben</strong>."),
        ]),
        dict(kop="De verbanden tussen alinea's", blokken=[
            ("p", "De <strong>alinea's van een tekst staan niet los van elkaar</strong>. Tussen twee "
                  "alinea's zit een verband, en <strong>de gedachtegang van een tekst kan je "
                  "reconstrueren uit de verbanden tussen de alinea's</strong>. Vaak voorkomende "
                  "verbanden zijn <strong>chronologisch en oorzakelijk</strong>, en "
                  "<strong>tegenstellend en vergelijkend</strong>."),
            ("p", tabel(["Verband", "Hoe je het herkent", "Voorbeeld"], [
                ["<strong>Chronologisch</strong>", "de tijd loopt door", "'Eerst kwam de brief. Een week later volgde de factuur.'"],
                ["<strong>Oorzakelijk</strong> of causaal", "de ene alinea geeft de oorzaak van de andere", "'De prijzen stegen. Daardoor daalde de verkoop.'"],
                ["<strong>Tegenstellend</strong>", "twee zaken staan tegenover elkaar", "'In het noorden daalt de bevolking. In het zuiden stijgt ze juist.'"],
                ["<strong>Vergelijkend</strong>", "twee zaken worden naast elkaar gelegd", "'Net als in Gent kiest ook Hasselt voor een lage snelheid.'"],
                ["<strong>Doel-middel</strong>", "er staat een doel en een middel om het te halen", "'Om de files te verminderen verlaagt de stad de parkeerplaatsen.'"],
                ["<strong>Voorwaardelijk</strong>", "het ene geldt alleen als het andere waar is", "'Als de prijzen blijven stijgen, daalt de verkoop.'"],
                ["<strong>Opsommend</strong>", "delen volgen elkaar zonder voorkeur", "vier maatregelen na elkaar, zonder er een te verkiezen"],
                ["<strong>Concluderend</strong>", "er wordt een besluit getrokken", "'Alles samen blijkt de maatregel te werken.'"],
                ["<strong>Voordelen-nadelen</strong>", "de goede en de slechte kant van hetzelfde", "eerst wat het oplevert, dan wat het kost"],
            ])),
            ("p", "Let op: een <strong>voordelen-nadelenverband is niet hetzelfde als een tegenstellend "
                  "verband</strong>. Bij voordelen en nadelen gaat het over twee kanten van dezelfde "
                  "zaak; bij een tegenstelling staan twee zaken tegenover elkaar."),
            ("p", "Bij een <strong>luistertekst bestaat er wel degelijk een alinea-indeling</strong>: een "
                  "spreker maakt zijn delen hoorbaar met een pauze of een aankondiging, en dus bestaat "
                  "ook daar het verband tussen de delen."),
        ]),
        dict(kop="De zeven vaste tekststructuren", blokken=[
            ("p", "Naast de verbanden tussen alinea's bestaat er de <strong>vaste tekststructuur</strong>: "
                  "vormen waarin een hele tekst gegoten wordt. Er zijn er zeven."),
            ("p", tabel(["Structuur", "Hoe ze loopt"], [
                ["De <strong>probleemstructuur</strong>", "eerst het probleem, dan de oorzaken en de oplossingen"],
                ["De <strong>maatregelstructuur</strong>", "een maatregel wordt voorgesteld, uitgelegd en verdedigd"],
                ["De <strong>evaluatiestructuur</strong>", "iets wordt aan criteria getoetst en beoordeeld"],
                ["De <strong>onderzoeksstructuur</strong>", "vraag, methode, resultaten en besluit"],
                ["De <strong>argumentatiestructuur</strong>", "een stelling wordt met argumenten verdedigd"],
                ["De <strong>ontwikkelingsstructuur</strong>", "ze volgt een verloop in de tijd"],
                ["De <strong>vergelijkingsstructuur</strong>", "twee zaken worden met dezelfde criteria naast elkaar gelegd"],
            ])),
            ("p", "Voorbeelden. Een tekst die beschrijft <strong>hoe een stad in honderd jaar van dorp "
                  "tot stad groeide</strong>, heeft een <strong>ontwikkelingsstructuur</strong>. Een "
                  "tekst die <strong>twee soorten verwarming naast elkaar zet met dezelfde vier "
                  "criteria</strong>, heeft een <strong>vergelijkingsstructuur</strong>, en zo'n "
                  "structuur <strong>vraagt dat je voor beide zaken dezelfde criteria gebruikt</strong>. "
                  "Een <strong>recensie van een restaurant die eten, prijs, service en inrichting "
                  "beoordeelt</strong>, is een <strong>evaluatiestructuur</strong>: zonder criteria is ze "
                  "<strong>geen evaluatiestructuur meer</strong>. Een <strong>opiniestuk dat eerst drie "
                  "argumenten voor en dan twee tegen geeft en daarna kiest</strong>, heeft een "
                  "<strong>argumentatiestructuur</strong>. Een <strong>onderzoeksstructuur noemt ook de "
                  "manier waarop iets onderzocht werd</strong>."),
            ("p", "Een <strong>tekst kan meer dan één vaste structuur gebruiken</strong>. Begint een "
                  "artikel met 'Een op de vier jongeren slaapt te kort' en eindigt het met een voorstel "
                  "om later te beginnen, dan herken je <strong>een probleemstructuur en een "
                  "maatregelstructuur</strong>."),
            ("p", "Twee dingen maken die structuren waardevol: <strong>ze helpen je de opbouw van een "
                  "tekst sneller te zien</strong>, en <strong>je kan ze ook zelf gebruiken als je "
                  "schrijft</strong>. Het is nuttig om de structuur te zien <strong>voor</strong> je "
                  "grondig leest, want dan <strong>weet je waar je welke informatie mag "
                  "verwachten</strong> en <strong>kan je je notities meteen in de juiste vorm "
                  "zetten</strong>. De <strong>structuur van een tekst verraadt mee wat de bedoeling van "
                  "de zender is.</strong>"),
        ]),
    ],
    onthoud=[
        "IMS: inleiding kondigt aan, midden werkt uit, slot besluit en herhaalt de hoofdgedachte.",
        "Eén deelonderwerp per alinea; tussentitels helpen, maar zijn niet nodig voor structuur.",
        "Alineaverbanden: chronologisch, oorzakelijk, tegenstellend, vergelijkend, doel-middel, voorwaardelijk, opsommend, concluderend, voordelen-nadelen.",
        "Zeven vaste structuren: probleem, maatregel, evaluatie, onderzoek, argumentatie, ontwikkeling, vergelijking.",
        "Eén tekst kan er meerdere combineren, en de structuur verraadt de bedoeling.",
    ],
)

# ───────────────────── 6. Structuuraanduiders
BUNDELS["structuuraanduiders-verwijswoorden-en-signaalwoorden-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Structuuraanduiders: verwijswoorden en signaalwoorden",
    onder="De kleine woorden die een tekst aan elkaar houden, en hoe je ze leest.",
    secties=[
        dict(kop="Twee soorten, één naam", blokken=[
            ("p", "<strong>Verwijswoorden en signaalwoorden</strong> heten samen met één woord "
                  "<strong>structuuraanduiders</strong>. Het zijn <strong>geen twee namen voor "
                  "hetzelfde</strong>: een verwijswoord wijst terug, een signaalwoord kondigt een verband "
                  "aan."),
            ("p", "Structuuraanduiders zijn twee keer belangrijk voor je: <strong>je gebruikt ze bij het "
                  "lezen en je past ze toe bij het schrijven</strong>. Bij het lezen helpen ze je "
                  "begrijpen, bij het schrijven maken ze jouw tekst leesbaar. Maar let op: <strong>wie "
                  "let op structuuraanduiders, hoeft daarmee niet minder notities te nemen</strong>."),
        ]),
        dict(kop="Verwijswoorden", blokken=[
            ("p", "Een <strong>verwijswoord</strong> is <strong>een woord dat naar iets eerder in de "
                  "tekst verwijst</strong>. <strong>Deze en die</strong>, <strong>hun en zij</strong>, "
                  "<strong>hem, het, daar</strong>: het zijn <strong>woorden als zij, hem, deze en "
                  "hun</strong>. Een schrijver gebruikt ze <strong>om niet telkens hetzelfde woord te "
                  "moeten herhalen</strong>, en <strong>ze maken een tekst korter en vlotter</strong>. "
                  "Wel moeten <strong>ze in getal passen bij waarnaar ze verwijzen</strong>."),
            ("p", "Lees je 'De burgemeester sprak de inwoners toe. Daarna gaven zij hem een brief', dan "
                  "verwijst <strong>hem naar de burgemeester</strong>. In 'De leerlingen kregen hun "
                  "rapport. Ze mochten het meteen bekijken' verwijst <strong>het naar het "
                  "rapport</strong>. En in 'De gemeente bouwt twee scholen. ... worden volgend jaar "
                  "geopend' past <strong>Ze</strong>, want het gaat om twee scholen. In 'Hij kreeg een "
                  "boete. Daar was hij niet blij mee' verwijst <strong>Daar</strong> naar de boete."),
            ("p", "Een <strong>verwijswoord kan ook naar een hele zin of een heel idee verwijzen</strong>, "
                  "en het <strong>staat niet altijd vóór het woord waarnaar het verwijst</strong>: soms "
                  "komt het woord pas erna. Daarom <strong>let je bij lezen op verwijswoorden, omdat je "
                  "anders de draad van de tekst verliest</strong>. In een <strong>luistertekst gebruikt "
                  "een spreker ook verwijswoorden</strong>."),
            ("p", "Een <strong>onduidelijk verwijswoord kan een zin dubbelzinnig maken</strong>. In 'De "
                  "directie en de vakbonden overlegden. Zij kwamen tot een akkoord' is <strong>zij "
                  "dubbelzinnig, want het kan naar beide partijen of naar één ervan verwijzen</strong>. "
                  "Verwijswoorden zijn daarom lastig in een <strong>tekst met veel personen, omdat meer "
                  "kandidaten in getal en geslacht passen</strong>. Is een verwijswoord in een moeilijke "
                  "tekst onduidelijk, dan <strong>zoek je het laatst genoemde woord dat past in getal en "
                  "geslacht</strong>."),
            ("kader", "Een <strong>tekst zonder enig verwijswoord is niet onmogelijk</strong> om te schrijven, maar hij "
                      "leest als een opsomming: elk woord steeds opnieuw voluit."),
        ]),
        dict(kop="Signaalwoorden", blokken=[
            ("p", "Een <strong>signaalwoord</strong> is <strong>een woord dat een verband of een stap "
                  "aankondigt</strong>: <strong>woorden als maar, dus, want en hoewel</strong>. Twee "
                  "dingen maken ze waardevol: <strong>ze maken de gedachtegang van een tekst "
                  "zichtbaar</strong>, en <strong>ze helpen je ook bij een luisteropdracht</strong>."),
            ("p", tabel(["Signaalwoord", "Welk verband het aankondigt"], [
                ["<strong>want</strong>, omdat", "een reden"],
                ["<strong>hoewel</strong>, toch, maar", "een tegenstelling of een toegeving"],
                ["<strong>als</strong>, indien", "een voorwaarde"],
                ["<strong>dus, daarom, daardoor, bijgevolg</strong>", "een gevolg"],
                ["<strong>ten eerste, ten tweede, ten derde, tot slot, ten slotte</strong>", "een opsomming"],
                ["<strong>kortom, samengevat, alles samen</strong>", "een samenvatting"],
                ["<strong>enerzijds, anderzijds</strong>", "een vergelijking of een afweging van twee kanten"],
                ["<strong>echter</strong>", "de schrijver spreekt nu iets tegen"],
            ])),
            ("p", "In 'Het plan is duur. Toch gaat het door' is het verband een "
                  "<strong>tegenstelling</strong>. Het woord <strong>maar kan een hele alinea tegenover "
                  "de vorige zetten</strong>. In een handleiding zegt '<strong>Ten slotte sluit je het "
                  "deksel</strong>' <strong>dat dit de laatste stap is</strong>: in een instructie vind "
                  "je die opsommende aanduiders bijna altijd terug. Staat een tekst vol met "
                  "<strong>enerzijds en anderzijds</strong>, dan verwacht je <strong>een vergelijking of "
                  "een afweging van twee kanten</strong>. En <strong>echter</strong> is nuttig om op te "
                  "letten in een opiniestuk <strong>omdat het aankondigt dat de schrijver nu iets "
                  "tegenspreekt</strong>."),
            ("p", "<strong>Signaalwoorden kunnen je verraden welke tekststructuur een schrijver "
                  "gebruikt.</strong> Maar <strong>hetzelfde signaalwoord kan in twee teksten een ander "
                  "verband aanduiden</strong>, dus lees altijd mee wat er staat."),
            ("p", "Twee dingen die niet kloppen: een <strong>tekst zonder signaalwoorden is niet altijd "
                  "onbegrijpelijk</strong> (de verbanden kunnen ook uit de inhoud blijken), en een "
                  "<strong>spreker die geen signaalwoorden gebruikt, heeft nog andere middelen om een "
                  "verband aan te geven</strong>: een pauze, een handbeweging, een verandering van "
                  "stemhoogte."),
        ]),
    ],
    onthoud=[
        "Verwijswoorden en signaalwoorden heten samen structuuraanduiders.",
        "Een verwijswoord wijst terug; bij twijfel: het laatst genoemde woord dat past in getal en geslacht.",
        "Verwijswoorden kunnen dubbelzinnig worden in een tekst met veel personen.",
        "Signaalwoorden kondigen een verband aan: reden, tegenstelling, voorwaarde, gevolg, opsomming, samenvatting.",
        "Hetzelfde signaalwoord kan elders een ander verband aanduiden; lees mee wat er staat.",
    ],
)

# ───────────────────── 7. Argumentatie, feiten en meningen, en drogredenen
BUNDELS["argumentatie-feiten-en-meningen-en-drogredenen-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Argumentatie, feiten en meningen, en drogredenen",
    onder="Stelling, argument, conclusie: hoe een betoog werkt, en waar het scheef gaat.",
    secties=[
        dict(kop="Feiten en meningen", blokken=[
            ("p", "Een <strong>feit</strong> is <strong>een uitspraak die je kan nagaan</strong>, met een "
                  "bron of een meting. Of hij klopt, is een tweede vraag: <strong>een cijfer in een tekst "
                  "is niet automatisch juist</strong>, het is alleen controleerbaar. Een "
                  "<strong>mening</strong> is <strong>een uitspraak die een standpunt of waardering "
                  "bevat</strong>. Die kan je niet nagaan, alleen beargumenteren."),
            ("p", "'De bibliotheek sluit om achttien uur' is een feit: het staat aan de deur. '<strong>De "
                  "nieuwe brug is veel te duur geweest</strong>' en '<strong>de stad had het geld beter "
                  "aan scholen besteed</strong>' zijn meningen; het bedrag en de openingsdatum van die "
                  "brug zijn feiten."),
            ("p", "<strong>Een feit en een mening kunnen in dezelfde zin staan</strong>: 'De brug kostte "
                  "achttien miljoen, veel te veel voor zo'n klein dorp.' Eerst het feit, dan het oordeel. "
                  "En een <strong>mening is niet minder waard dan een feit</strong>: in een opiniestuk is "
                  "ze het punt. Ze moet alleen als mening te herkennen zijn. Gebruikt een tekst feiten en "
                  "meningen door elkaar zonder onderscheid, dan <strong>scheid je ze zelf en noem je welk "
                  "deel wat is</strong>."),
            ("p", "Een <strong>argumentatieve tekst kan ook feiten bevatten</strong> — de sterkste "
                  "argumenten steunen er juist op. En een <strong>tekst die zijn stelling nergens "
                  "uitspreekt, kan toch een standpunt hebben</strong>: door de keuze van woorden, "
                  "voorbeelden en getuigen."),
        ]),
        dict(kop="Stelling, argument, conclusie", blokken=[
            ("p", "Een <strong>stelling</strong> is <strong>de bewering die de schrijver wil "
                  "verdedigen</strong>. Een <strong>standpunt</strong> is de kant die je kiest tegenover "
                  "die stelling: <strong>een stelling is de bewering, een standpunt de kant die je "
                  "kiest</strong>. Een <strong>argument</strong> is <strong>een reden die een stelling "
                  "ondersteunt</strong>; een <strong>tegenargument</strong> pleit ertegen. De "
                  "<strong>conclusie</strong> is <strong>het besluit dat een schrijver uit zijn "
                  "argumenten trekt</strong>, meestal in het slot: 'Daarom moet de stad de fietspaden "
                  "verbreden.'"),
            ("p", "Over <strong>tegenargumenten</strong>: <strong>ze pleiten tegen de stelling van de "
                  "schrijver</strong>, en <strong>een schrijver kan ze noemen om ze te weerleggen</strong>. "
                  "Dat heet een <strong>tweezijdige argumentatie</strong>: <strong>een tekst die ook de "
                  "tegenargumenten behandelt</strong>. Dat <strong>maakt een betoog sterker, niet "
                  "zwakker</strong>. Het <strong>moet niet</strong>, maar een betoog dat de tegenkant "
                  "verzwijgt, valt om zodra de lezer er zelf aan denkt."),
            ("p", "Bij het beoordelen van een argumentatieve tekst zet je deze stappen: <strong>je "
                  "bepaalt eerst de stelling van de schrijver</strong>, en <strong>je zoekt de argumenten "
                  "en de tegenargumenten</strong>. Daarna geef je de conclusie weer en kijk je of de "
                  "argumenten die conclusie dragen. Want <strong>een tekst kan een juiste conclusie "
                  "hebben op basis van zwakke argumenten</strong>: je beoordeelt de argumenten en de "
                  "conclusie apart."),
        ]),
        dict(kop="De soorten argumentatie", blokken=[
            ("p", "Argumenten zijn van een paar vaste soorten. Elke soort heeft haar eigen zwakke plek."),
            ("p", tabel(["Soort argumentatie", "Voorbeeld", "Waar ze wankelt"], [
                ["op basis van <strong>vergelijking</strong>", "'In Nederland werkt het ook, dus bij ons zal het werken.'", "lijken die twee gevallen wel genoeg op elkaar?"],
                ["op basis van <strong>oorzaak en gevolg</strong>", "'Sinds de camera's er staan, zijn er minder inbraken.'", "wat na elkaar gebeurt, hoeft niet door elkaar te gebeuren"],
                ["op basis van <strong>wetenschappelijk onderzoek</strong>", "'Een studie wijst uit dat…'", "wie deed het onderzoek, en hoe groot was het?"],
                ["op basis van <strong>cijfers en statistieken</strong>", "'Tachtig procent van de gebruikers is tevreden.'", "hoeveel gebruikers werden bevraagd, en door wie?"],
                ["op basis van een <strong>autoriteit</strong>", "'Negen op de tien tandartsen raden dit aan.'", "gezag alleen is geen bewijs"],
            ])),
            ("p", "Een <strong>vergelijking als argument is sterker als de twee gevallen echt op elkaar "
                  "lijken</strong>; verschillen ze sterk, dan zegt het ene weinig over het andere. "
                  "'Negen op de tien tandartsen' is <strong>een beroep op een autoriteit met een cijfer "
                  "erbij</strong>: de vraag is dan welke tandartsen, hoeveel er gevraagd werden en door "
                  "wie betaald. En 'deze maatregel werkt, want de minister zegt het' is zwak omdat "
                  "<strong>gezag alleen geen bewijs is</strong>: een autoriteit moet deskundig én "
                  "onafhankelijk zijn."),
            ("p", "Een <strong>argument dat op onderzoek steunt</strong>, beoordeel je door te kijken "
                  "<strong>wie het onderzoek deed en hoe groot het was</strong>. Opdrachtgever, aantal "
                  "deelnemers en methode beslissen hoe zwaar het weegt. Bij een reclamecijfer stel je de "
                  "vraag: <strong>hoeveel gebruikers werden er bevraagd, en door wie?</strong>"),
            ("p", "Bij een <strong>luistertekst herken je dezelfde argumentatiesoorten als bij een "
                  "leestekst</strong>: in een debat of een podcast werken vergelijkingen, cijfers en "
                  "gezagsargumenten precies zo."),
        ]),
        dict(kop="Drogredenen", blokken=[
            ("p", "Een <strong>drogreden</strong> is <strong>een argument dat alleen lijkt te "
                  "kloppen</strong>. Het werkt op het gevoel of op de vorm van een redenering, niet op de "
                  "inhoud. <strong>Een drogreden kan overtuigend klinken en toch niets bewijzen</strong> "
                  "— dat is net het probleem."),
            ("p", tabel(["Drogreden", "Hoe ze klinkt"], [
                ["<strong>Een aanval op de persoon</strong> (ad hominem)", "'Jij hebt daar geen verstand van, dus je ongelijk is duidelijk.'"],
                ["<strong>Het hellend vlak</strong>", "'Als we dit toelaten, staan we morgen voor de afgrond.'"],
                ["<strong>Een cirkelredenering</strong>", "'Dat is zo omdat het nu eenmaal zo is.'"],
                ["<strong>Een beroep op de massa</strong>", "'Iedereen doet het' of 'veel mensen vinden dat'."],
            ])),
            ("p", "Een <strong>persoonlijke aanval</strong> laat het argument zelf ongemoeid. Gaat een "
                  "debat over een nieuwe taks en zegt één spreker enkel dat de tegenstander rijk is, dan "
                  "ontbreekt <strong>een argument over de taks zelf</strong>. '<strong>Iedereen doet "
                  "het</strong>' is <strong>geen geldig argument in een betoog</strong>, en '<strong>veel "
                  "mensen vinden dat</strong>' is zelden sterk <strong>omdat een grote groep zich ook kan "
                  "vergissen</strong>: het zegt iets over populariteit, niet over juistheid."),
            ("p", "Twee waarschuwingen. <strong>Wie een drogreden gebruikt, heeft daarmee niet bewezen "
                  "dat zijn stelling fout is</strong>: het argument sneuvelt, de stelling niet. En een "
                  "<strong>slecht argument voor iets dat toch waar is, bestaat</strong>."),
        ]),
    ],
    onthoud=[
        "Een feit kan je nagaan, een mening beargumenteren; ze kunnen in dezelfde zin staan.",
        "Stelling, argument, tegenargument, conclusie. Tweezijdig maakt een betoog sterker.",
        "Vijf soorten: vergelijking, oorzaak en gevolg, onderzoek, cijfers, autoriteit.",
        "Drogredenen: persoonlijke aanval, hellend vlak, cirkelredenering, beroep op de massa.",
        "Een drogreden ontkracht het argument, niet de stelling.",
    ],
)

# ───────────────────── 8. Lees- en luisterstrategieën en notities nemen
BUNDELS["lees-en-luisterstrategieen-en-notities-nemen-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Lees- en luisterstrategieën en notities nemen",
    onder="Scannen, skimmen of intensief lezen: je leesdoel beslist.",
    secties=[
        dict(kop="Voor je begint", blokken=[
            ("p", "Het eerste wat je bepaalt, is je <strong>leesdoel</strong>: <strong>het doel waarmee "
                  "je aan een tekst begint</strong>. Wie zoekt naar één getal leest anders dan wie zich "
                  "op een examen voorbereidt. <strong>Welke strategie je kiest, hangt af van wat je met "
                  "de tekst wil doen</strong>, en je <strong>leesdoel kan tijdens het lezen "
                  "veranderen</strong>: je begint te scannen, de tekst blijkt belangrijker dan gedacht, "
                  "en je gaat intensief lezen."),
            ("p", "Daarna <strong>activeer je je voorkennis</strong>: <strong>nagaan wat je al over het "
                  "onderwerp weet</strong>. Wat je al weet, geeft de nieuwe informatie een plaats om aan "
                  "te hangen. <strong>Voorspellen wat er komt, kan al op basis van de titel en de "
                  "afbeeldingen</strong>. Die voorspelling hoeft niet te kloppen; ze maakt je alleen "
                  "oplettend. Het helpt ook om <strong>vooraf vragen bij een tekst te bedenken</strong>, "
                  "want <strong>je leest dan gerichter, op zoek naar antwoorden</strong>."),
            ("p", "Ook bij luisteren kan dat: <strong>bij een luistertekst kan je wel degelijk je "
                  "voorkennis activeren</strong>. De titel van de lezing, de spreker of het onderwerp van "
                  "de les zeggen vaak al genoeg."),
        ]),
        dict(kop="Scannen, skimmen, intensief lezen", blokken=[
            ("p", tabel(["Strategie", "Wat je doet", "Wanneer"], [
                ["<strong>Scannen</strong> of zoekend lezen", "een tekst doorzoeken op één bepaald gegeven", "'om hoe laat vertrekt de laatste bus?'"],
                ["<strong>Skimmen</strong>", "snel door een tekst gaan om te weten waarover hij gaat", "om te beslissen of de tekst je dient"],
                ["<strong>Intensief lezen</strong>", "langzaam en nauwkeurig, met aandacht voor elk verband", "een tekst die je op een toets moet kennen"],
            ])),
            ("p", "Bij <strong>skimmen bekijk je de titel en de tussenkoppen</strong>, en <strong>de "
                  "eerste zin van elke alinea</strong>, plus het slot. Voetnoten en tabellen komen pas "
                  "als je echt binnengaat. Zoek je in een jaarverslag van vijftig bladzijden hoeveel "
                  "leden een vereniging heeft, dan <strong>scan je op het woord leden en op "
                  "getallen</strong>; de inhoudstafel helpt nog sneller."),
            ("p", "Bij <strong>intensief lezen</strong> sta je stil bij verwijswoorden, signaalwoorden en "
                  "bij elke stap in een redenering, en je combineert het met <strong>markeren en "
                  "samenvatten</strong>. Een <strong>goede lezer leest dus niet elke tekst even "
                  "grondig</strong>: hij kiest per tekst hoe diep hij gaat."),
            ("p", "Bij een lange studietekst die je moet kennen, doe je als eerste <strong>de tekst overlopen "
                  "om zijn opbouw te zien</strong>. Wie de opbouw kent, weet waar hij is terwijl hij "
                  "leest. <strong>Tussenkoppen geven je meteen de indeling van de tekst</strong>: van de "
                  "koppen alleen kan je al een skelet maken."),
        ]),
        dict(kop="Markeren, samenvatten, schematiseren", blokken=[
            ("p", "Het risico van veel markeren: <strong>als bijna alles gemarkeerd is, valt niets meer "
                  "op</strong>. Markeren is kiezen. In de marge zet je het best <strong>een kernwoord per "
                  "alinea</strong> en <strong>een vraagteken waar je iets niet begrijpt</strong>. Een "
                  "hele alinea in de marge herschrijven kost meer dan het opbrengt."),
            ("p", "In een goede <strong>samenvatting</strong> staan <strong>de hoofdgedachte en de "
                  "hoofdpunten</strong>; voorbeelden en uitweidingen laat je weg. Een "
                  "<strong>samenvatting in je eigen woorden werkt beter dan één met de woorden van de "
                  "tekst</strong>, want wie herformuleert moet begrijpen. Een <strong>samenvatting mag de "
                  "volgorde van de tekst veranderen</strong>, zolang de verbanden kloppen."),
            ("p", "Een <strong>schema of mindmap is ook een geldige manier om een tekst samen te "
                  "vatten</strong>. Het <strong>verschil tussen een samenvatting en een schema</strong>: "
                  "<strong>een schema toont de verbanden in beeld, een samenvatting in zinnen</strong>. "
                  "Welke van de twee past, hangt af van de tekst: veel verbanden vragen een schema."),
        ]),
        dict(kop="Notities bij een luistertekst", blokken=[
            ("p", "<strong>Notities nemen bij een luistertekst is moeilijker dan bij een leestekst, "
                  "omdat je niet kan terugkeren naar wat voorbij is.</strong> Daarom schrijf je kort en "
                  "in steekwoorden, niet in volle zinnen: bij een luistertekst van tien minuten over een "
                  "nieuwe wet neem je notities <strong>in steekwoorden, met ruimte om later aan te "
                  "vullen</strong>. Gaat een tekst te snel, dan <strong>noteer je enkel de kernwoorden en "
                  "vul je de rest achteraf aan</strong>: kernwoorden zijn haken."),
            ("p", "Twee afspraken helpen bij notities van een les of een lezing: <strong>vaste "
                  "afkortingen die je zelf altijd gebruikt</strong>, en <strong>witruimte laten om later "
                  "aan te vullen</strong>. Letterlijk meeschrijven lukt niet, en denken doe je dan ook "
                  "niet meer. Meteen <strong>na een lezing lees je je notities na en vul je de gaten "
                  "aan</strong>, want een week later is dat weg. <strong>Notities van iemand anders "
                  "werken niet even goed als je eigen notities</strong>: die van een ander moet je eerst "
                  "nog ontcijferen."),
            ("p", "<strong>Wie naar een lezing luistert, moet de structuur niet altijd zelf uit de "
                  "inhoud opmaken</strong>: veel sprekers kondigen ze zelf aan. 'Ik behandel drie punten' "
                  "is een geschenk voor wie notities neemt."),
        ]),
        dict(kop="Nagaan of je het begrepen hebt", blokken=[
            ("p", "Je gaat na of je een tekst begrepen hebt door hem <strong>samen te vatten zonder "
                  "ernaar te kijken</strong> en door <strong>de hoofdpunten aan iemand anders uit te "
                  "leggen</strong>. Snelheid en bekende woorden zeggen daar niets over. Wat je niet kan "
                  "navertellen, heb je gelezen maar niet begrepen."),
            ("p", "Bij een <strong>moeilijke alinea</strong> helpt het om <strong>de alinea in je eigen "
                  "woorden na te vertellen</strong>: herformuleren wijst precies aan waar het vastloopt. "
                  "<strong>Wie een tekst niet begrijpt, kan niet beter meteen stoppen met lezen</strong>: "
                  "er zijn tussenstappen, zoals de alinea opnieuw lezen, een woord opzoeken, de "
                  "tussenkoppen bekijken of iemand iets vragen. Kan je er niets over navertellen, dan "
                  "<strong>lees je de tekst opnieuw, nu met de koppen als leidraad</strong> — dezelfde "
                  "aanpak herhalen geeft hetzelfde resultaat."),
            ("p", "De volle cyclus van een strategische aanpak: <strong>eerst overlopen, dan intensief "
                  "lezen</strong>, en <strong>achteraf nagaan of je de tekst kan navertellen</strong>. "
                  "<strong>Wie weet waarom hij een tekst leest, leest doelmatiger.</strong>"),
        ]),
    ],
    onthoud=[
        "Eerst je leesdoel, dan je voorkennis, dan je strategie.",
        "Scannen voor één gegeven, skimmen voor het geheel, intensief lezen om te kennen.",
        "Markeren is kiezen; een samenvatting in eigen woorden werkt beter dan overschrijven.",
        "Bij luisteren: steekwoorden, witruimte, eigen afkortingen, en meteen erna aanvullen.",
        "Controle: navertellen zonder de tekst. Lukt dat niet, dan lees je opnieuw met de koppen als leidraad.",
    ],
)

# ───────────────────── 9. Multimediale elementen en non-verbale communicatie
BUNDELS["multimediale-elementen-en-non-verbale-communicatie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Multimediale elementen en non-verbale communicatie",
    onder="Wat beeld, geluid, kleur en lichaamstaal met een boodschap doen.",
    secties=[
        dict(kop="Wat een multimediaal element is", blokken=[
            ("p", "Een <strong>multimediaal element</strong> is <strong>een beeld, geluid of video naast "
                  "de woorden</strong>. Ook een kaart, een grafiek, een pictogram of een stukje muziek "
                  "hoort erbij. Een <strong>filmpje bij een artikel kan informatie geven die in de tekst "
                  "niet staat</strong>; daarom hoort het bij de tekst bekeken te worden en niet ernaast."),
            ("p", "Een <strong>foto bij een nieuwsbericht</strong> kan twee dingen doen: <strong>de lezer "
                  "naar de tekst toe trekken</strong> en <strong>een gevoel bij het bericht "
                  "meegeven</strong>. Een foto trekt de blik en zet een toon nog voor de eerste zin "
                  "gelezen is. Daarom kan <strong>een beeld bij een tekst de boodschap van die tekst "
                  "bijsturen</strong>: een neutraal bericht naast een dreigende foto leest alsof het "
                  "bericht zelf dreigend is."),
            ("p", "Een <strong>foto in een krant geeft niet altijd neutraal weer wat er gebeurd "
                  "is</strong>: iemand koos het moment, de hoek en de uitsnede. Zet een nieuwssite bij "
                  "een bericht over armoede een <strong>foto van een lachend gezin</strong>, dan "
                  "<strong>past het beeld niet bij de inhoud van het bericht</strong> — de samenhang "
                  "tussen woord en beeld is zoek."),
            ("p", "Daarom staat bij een grafiek of een foto een <strong>onderschrift</strong>: het zegt "
                  "<strong>wat de grafiek toont en waar de gegevens vandaan komen</strong>. Zonder bron "
                  "en eenheid is een grafiek alleen een mooie vorm. Beweert een <strong>onderschrift iets "
                  "anders dan de foto laat zien</strong>, dan <strong>vertrouw je de foto en zet je een "
                  "vraagteken bij het onderschrift</strong>. Staat er een beeld van iemand anders bij een "
                  "tekst, dan hoort er een <strong>bronvermelding</strong> bij, <strong>omdat de maker "
                  "van het beeld recht heeft op zijn naam</strong>."),
        ]),
        dict(kop="Beeld, geluid en camerahoek", blokken=[
            ("p", "Beeld werkt door wat het oproept. Laat een <strong>reclame voor een auto</strong> die "
                  "auto door een leeg berglandschap rijden, dan <strong>verbindt dat beeld het product "
                  "met vrijheid en ruimte</strong> — geen enkel woord zegt 'vrijheid'."),
            ("p", "<strong>Muziek onder een reportage</strong> kan <strong>de kijker in een bepaalde "
                  "stemming brengen</strong> en <strong>aangeven dat er een nieuw deel begint</strong>. "
                  "Dezelfde beelden klinken onder zware strijkers heel anders dan onder lichte piano. "
                  "Ook de <strong>camerahoek</strong> doet mee: <strong>een lage camerahoek, van onderaf, "
                  "laat een persoon groter en machtiger lijken</strong>; van bovenaf gebeurt het "
                  "omgekeerde. De <strong>toon van een reportage</strong> wordt dus mee bepaald door "
                  "<strong>de muziek onder de beelden</strong> en <strong>de camerahoek waaruit gefilmd "
                  "wordt</strong>, en ook door de montage en het licht."),
            ("p", "Zie je een <strong>video waarin een politicus spreekt met donkere muziek "
                  "eronder</strong>, dan <strong>scheid je als kritische kijker wat hij zegt van hoe het "
                  "gebracht wordt</strong>. De muziek komt van de makers, niet van de spreker."),
            ("p", "Een <strong>bewerkt beeld blijft geen betrouwbare weergave van de "
                  "werkelijkheid</strong>: uitsnede, kleurbewerking of een weggehaald detail veranderen "
                  "wat de kijker denkt te zien. En een <strong>grafiek kan misleiden zonder één onjuist "
                  "cijfer te bevatten</strong>: een zij-as die niet bij nul begint, maakt een klein "
                  "verschil tot een berg."),
        ]),
        dict(kop="Kleur, typografie en lay-out", blokken=[
            ("p", "<strong>Kleur in een tekst of op een affiche is meer dan versiering</strong>: rood "
                  "waarschuwt, groen stelt gerust, de huiskleur van een merk maakt de afzender "
                  "herkenbaar. Gebruikt een <strong>affiche enkel rood en zwart met grote "
                  "blokletters</strong>, dan is het effect dat het geheel <strong>dringend en waarschuwend</strong> "
                  "overkomt, nog voor iemand het eerste woord leest."),
            ("p", "Een <strong>vet gezet woord trekt de aandacht naar dat woord</strong>. Typografie "
                  "stuurt waar je blik heen gaat; te veel vet werkt daarom niet meer. In de lay-out "
                  "helpen <strong>tussenkoppen boven de delen van de tekst</strong> en <strong>witruimte "
                  "tussen de alinea's</strong> de lezer zijn weg te vinden, en een <strong>tekst met "
                  "tussenkoppen en witruimte wordt vaker helemaal gelezen dan een dichte lap "
                  "tekst</strong>."),
            ("p", "Een <strong>pictogram</strong> is <strong>een vereenvoudigde tekening die één ding "
                  "aanduidt</strong>, zoals bij een nooduitgang: het werkt zonder taal, en dat is de "
                  "bedoeling in een station of een ziekenhuis. Een <strong>infographic</strong> "
                  "<strong>zet veel gegevens in één overzichtelijk beeld</strong>; cijfers, verhoudingen "
                  "en stappen worden zichtbaar in plaats van opgesomd. Een <strong>handleiding met "
                  "genummerde tekeningen bij elke stap</strong> werkt omdat <strong>de lezer de stap ziet "
                  "en de uitleg ernaast leest</strong>."),
            ("p", "In een digitale tekst heeft een <strong>hyperlink wel een functie voor de "
                  "structuur</strong>: hij verbindt de tekst met achtergrond elders, en hij zegt waar de "
                  "schrijver zijn gegevens haalde."),
            ("p", "Bij een presentatie geldt: <strong>één gedachte per dia, in grote letters</strong>. "
                  "Het publiek kan lezen of luisteren, niet beide. En <strong>je dia's zijn niet even "
                  "belangrijk als wat je zegt</strong>: ze steunen je woorden."),
        ]),
        dict(kop="Non-verbale communicatie", blokken=[
            ("p", "Bij <strong>non-verbale communicatie</strong> horen <strong>lichaamshouding en "
                  "mimiek</strong>, en <strong>oogcontact en afstand tot de ander</strong>. Ook "
                  "stemvolume, tempo en stiltes horen erbij: alles wat meespreekt zonder woord te zijn. "
                  "<strong>Mimiek</strong> is <strong>de uitdrukking op iemands gezicht</strong>; ze kan "
                  "een gesproken boodschap bevestigen of juist tegenspreken."),
            ("p", "Zegt iemand '<strong>prima</strong>' met een strak gezicht en een afgewend hoofd, dan "
                  "<strong>spreken de woorden en de lichaamstaal elkaar tegen</strong>, en hecht een "
                  "luisteraar meestal meer aan wat hij ziet. <strong>Hoeveel afstand mensen tijdens een "
                  "gesprek houden, verschilt per cultuur</strong>, en <strong>oogcontact betekent niet in "
                  "elke situatie hetzelfde</strong>: het kan belangstelling tonen, maar ook uitdagend of "
                  "ongepast overkomen."),
            ("p", "<strong>Stemgebruik</strong> doet twee dingen: <strong>het geeft aan welk woord het "
                  "zwaarst weegt</strong> en <strong>het laat horen hoe de spreker zich voelt</strong>. "
                  "Volume, tempo en toonhoogte zijn de opmaak van het gesproken woord. Een <strong>korte "
                  "stilte voor het belangrijkste punt zet dat punt in de aandacht</strong>: een stilte "
                  "werkt als een vet gezet woord, maar dan hoorbaar. Een <strong>spreker kan met zijn "
                  "handen een verband tussen twee punten aangeven</strong>, als een schema dat je even "
                  "ziet."),
            ("p", "Wat een spreker voor een publiek helpt: <strong>de zaal rondkijken in plaats van naar "
                  "één punt</strong>, en <strong>spreken met een rustig tempo en hoorbare pauzes</strong>."),
        ]),
    ],
    onthoud=[
        "Beeld, geluid, kleur, typografie en lay-out zijn keuzes; ze sturen de boodschap mee.",
        "Een onderschrift zegt wat je ziet en waar het vandaan komt; het beeld is de bron, niet de tekst.",
        "Camerahoek, muziek en montage bepalen de toon; scheid wat iemand zegt van hoe het gebracht wordt.",
        "Een grafiek kan misleiden zonder één fout cijfer; let op de zij-as.",
        "Non-verbaal: houding, mimiek, oogcontact, afstand, stem en stilte. Bij tegenspraak wint wat men ziet.",
    ],
)

# ───────────────────── 10. Verhaallijn, personages en vertelperspectief
BUNDELS["verhaallijn-personages-en-vertelperspectief-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Verhaallijn, personages en vertelperspectief",
    onder="Wat er gebeurt, aan wie het gebeurt, en door wiens ogen je het ziet.",
    secties=[
        dict(kop="De verhaallijn", blokken=[
            ("p", "De <strong>verhaallijn</strong> van een boek is <strong>de opeenvolging van "
                  "gebeurtenissen van begin tot eind</strong>. Wie ze navertelt, zegt wat er gebeurt en "
                  "in welke orde. Om een verhaallijn na te vertellen <strong>moet je niet elk detail uit "
                  "het boek noemen</strong>: je noemt de gebeurtenissen die het verhaal vooruit duwen. "
                  "In vijf zinnen <strong>noem je de gebeurtenissen die het verhaal in gang zetten en "
                  "afsluiten</strong>: beginsituatie, conflict, wending, slot."),
            ("p", "Een <strong>conflict</strong> is <strong>de tegenstelling die het verhaal in beweging "
                  "zet</strong>. Het kan tussen twee personages zitten, maar ook in het hoofdpersonage "
                  "zelf. Een <strong>nevenverhaal</strong> is <strong>een tweede verhaallijn naast de "
                  "hoofdlijn</strong>; het goede nevenverhaal raakt de hoofdlijn ergens aan."),
            ("p", "Een <strong>verhaal moet niet in chronologische orde verteld worden om te "
                  "kloppen</strong>. Een <strong>flashback</strong> of <strong>terugblik</strong> is "
                  "<strong>een sprong terug in de tijd binnen een verhaal</strong>: de verhaallijn is "
                  "dan anders geordend dan de tijdlijn van de gebeurtenissen. Een schrijver begint met "
                  "het einde <strong>om de lezer te laten zoeken hoe het zover kwam</strong>: de vraag is "
                  "niet meer wat er gebeurt, maar waarom. Een <strong>verhaal kan ook goed zijn zonder "
                  "dat er veel gebeurt</strong>; soms zit het hele verhaal in wat er in één personage "
                  "verschuift."),
            ("p", "Het <strong>verschil tussen verteltijd en vertelde tijd</strong>: <strong>verteltijd "
                  "is hoe lang je erover leest, vertelde tijd hoeveel tijd er verstrijkt</strong>. Eén "
                  "bladzijde kan twintig jaar overslaan, en twintig bladzijden kunnen één minuut duren."),
        ]),
        dict(kop="Personages", blokken=[
            ("p", "Het <strong>hoofdpersonage</strong> is <strong>het personage om wie het verhaal "
                  "draait</strong>, ook de <strong>protagonist</strong> genoemd. Soms is dat ook de "
                  "verteller, maar dat hoeft niet: de twee rollen zijn verschillend. Een "
                  "<strong>nevenpersonage</strong> is <strong>een personage dat een rol speelt naast het "
                  "hoofdpersonage</strong>; een goed nevenpersonage laat iets zien over het "
                  "hoofdpersonage dat die zelf niet zegt."),
            ("p", "Een <strong>rond personage</strong> is <strong>een personage dat in de loop van het "
                  "verhaal verandert</strong>. Een <strong>vlak personage</strong> blijft van de eerste "
                  "tot de laatste bladzijde hetzelfde en <strong>vervult één duidelijke rol in het "
                  "verhaal</strong>: de strenge leraar, de trouwe vriend. Ze hoeven niet te veranderen "
                  "om nuttig te zijn."),
            ("p", "Je leert een personage kennen <strong>door wat het doet en zegt</strong> en "
                  "<strong>door wat andere personages erover zeggen</strong>, en ook door de gedachten "
                  "die de verteller weergeeft en door wat het personage juist niet zegt. Een schrijver "
                  "laat een personage zien <strong>door wat het doet op moeilijke momenten</strong> en "
                  "<strong>door hoe andere personages op hem reageren</strong>. Een <strong>personage dat "
                  "het hele verhaal niets zegt, kan werken, want zwijgen kan ook iets over hem "
                  "zeggen</strong>."),
            ("p", "Bij het beschrijven van een hoofdpersonage stel je twee vragen: <strong>wat wil dit "
                  "personage, en wat staat in de weg?</strong> en <strong>verandert dit personage in de "
                  "loop van het verhaal?</strong> Verlangen en verandering: daarmee heb je het skelet. "
                  "Om de <strong>verhouding tussen twee personages</strong> te beschrijven, vraag je "
                  "<strong>wat de ene van de andere wil, en of hij dat krijgt</strong>."),
            ("p", "Een <strong>personage kan sympathiek zijn en toch verkeerde keuzes maken</strong> — "
                  "juist die mengeling maakt het geloofwaardig. En <strong>twee lezers kunnen een "
                  "personage heel verschillend beoordelen</strong>: wat de een moedig vindt, vindt de "
                  "ander onnadenkend. Daarom is de onderbouwing het punt. <strong>Wie een boek "
                  "beoordeelt, moet zijn mening over de personages niet voor zich houden</strong>, maar "
                  "er wel bij zeggen waarom, met iets uit het boek zelf."),
        ]),
        dict(kop="Het vertelperspectief", blokken=[
            ("p", "Het <strong>perspectief</strong> is de deur waardoor je naar binnen kijkt. Het is "
                  "nuttig om het te benoemen <strong>omdat het bepaalt wat je als lezer te weten "
                  "krijgt</strong>."),
            ("p", tabel(["Perspectief", "Wat je ziet"], [
                ["Het <strong>ik-perspectief</strong>", "je weet alleen wat die ene persoon weet, voelt en durft te vertellen"],
                ["De <strong>alwetende verteller</strong>", "hij kent de gedachten van alle personages en kan vooruitkijken"],
                ["Een <strong>meervoudig perspectief</strong>", "elk hoofdstuk hoort bij een ander personage"],
            ])),
            ("p", "Een verhaal dat met 'ik' verteld wordt, heeft het <strong>ik-perspectief</strong>. "
                  "Voor de lezer betekent dat: <strong>je komt dicht bij de gevoelens van dat "
                  "personage</strong>, maar <strong>je weet niet wat de andere personages denken</strong>. "
                  "Een ik-verteller kan zich vergissen, liegen of iets verzwijgen, en daarom "
                  "<strong>kan de lezer in zo'n verhaal méér weten dan de verteller zelf</strong>. Zo'n "
                  "verteller heet dan <strong>een onbetrouwbare verteller</strong>: <strong>een verteller van wie de "
                  "lezer gaandeweg gaat twijfelen</strong>."),
            ("p", "Lees je 'Ze wist niet dat hij al vertrokken was', dan heb je <strong>een alwetende "
                  "verteller, want hij weet meer dan zij</strong>. Schakelt een verhaal van ik-"
                  "perspectief naar alwetend over, of overschakelt het halverwege, dan <strong>krijgt de lezer meer te weten dan één "
                  "personage</strong>: je verliest de nabijheid en je wint het overzicht."),
            ("p", "<strong>Eén boek kan tussen meerdere perspectieven wisselen.</strong> Wordt een "
                  "verhaal door drie personages verteld, elk in eigen hoofdstukken, dan <strong>komt "
                  "dezelfde gebeurtenis er in drie versies te staan</strong>, en ziet de lezer dat geen "
                  "van de drie het hele beeld heeft."),
            ("p", "Twee dingen die niet kloppen: de <strong>verteller en de schrijver van een boek zijn "
                  "niet hetzelfde</strong> — de schrijver bedenkt de verteller, zoals hij de personages "
                  "bedenkt — en een <strong>verhaal met een ik-verteller is niet altijd "
                  "waargebeurd</strong>: de ik-vorm maakt een verhaal dichterbij, niet waar."),
            ("p", "Een <strong>open einde</strong> betekent <strong>niet dat de schrijver zijn verhaal "
                  "niet afgewerkt heeft</strong>: het is een keuze, de lezer mag zelf verder denken. En "
                  "een gesprek over een boek dat je las, begint bij vragen als <strong>welk personage "
                  "bleef je het meest bij, en waarom?</strong> en <strong>welk moment in het verhaal "
                  "veranderde alles?</strong>"),
        ]),
    ],
    onthoud=[
        "Verhaallijn: beginsituatie, conflict, wending, slot. Het conflict zet het verhaal in beweging.",
        "Verteltijd is hoe lang je leest, vertelde tijd hoeveel tijd verstrijkt.",
        "Rond personage verandert, vlak personage blijft; verlangen en verandering zijn je twee vragen.",
        "Ik-perspectief: nabij maar beperkt, en soms onbetrouwbaar. Alwetend: overzicht.",
        "De verteller is niet de schrijver, en de ik-vorm maakt een verhaal niet waar.",
    ],
)

# ───────────────────── 11. Tijd, ruimte, thema en spanningsopbouw
BUNDELS["tijd-ruimte-thema-en-spanningsopbouw-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Tijd, ruimte, thema en spanningsopbouw",
    onder="Waar en wanneer het speelt, waarover het gaat, en waarom je doorleest.",
    secties=[
        dict(kop="De ruimte", blokken=[
            ("p", "De <strong>ruimte in een verhaal</strong> zijn <strong>de plaatsen waar het verhaal "
                  "zich afspeelt</strong>. De <strong>ruimte is niet enkel decor</strong>: een huis dat "
                  "steeds kleiner lijkt te worden, zegt iets over wie erin woont. Ze doet mee met de "
                  "sfeer: <strong>een gesloten ruimte kan beklemmend werken</strong> en <strong>een "
                  "weidse ruimte kan vrijheid of eenzaamheid oproepen</strong>. Een schrijver kiest ze "
                  "zoals een filmmaker een decor kiest."),
            ("p", "Speelt een <strong>verhaal volledig in één kamer</strong>, dan <strong>voelt de lezer "
                  "de beperking van de personages mee</strong>: wat niet weg kan, moet het met elkaar "
                  "uitvechten. Laat een schrijver <strong>het weer passen bij het gevoel van een "
                  "personage</strong>, dan <strong>laat hij de ruimte de binnenkant van het personage "
                  "spiegelen</strong>. Speelt een boek in een <strong>stad die niet bestaat</strong>, dan "
                  "<strong>kan de schrijver de ruimte helemaal naar zijn verhaal vormen</strong>."),
            ("p", "Om de ruimte te beschrijven, vraag je: <strong>welke plaatsen komen terug, en wat "
                  "gebeurt daar steeds?</strong> en <strong>is de ruimte open of gesloten, en wat doet "
                  "dat met de personages?</strong> Het gaat niet om een lijst plaatsen."),
        ]),
        dict(kop="De tijd", blokken=[
            ("p", "De <strong>tijd waarin een verhaal speelt, kan het gedrag van de personages "
                  "verklaren</strong>: wat in 1950 onmogelijk was voor een jonge vrouw, is dat vandaag "
                  "niet meer. Toch <strong>moet een verhaal niet in de eigen tijd van de lezer spelen om "
                  "te raken</strong>."),
            ("p", "Een <strong>tijdsprong</strong> is <strong>een stuk tijd dat de schrijver "
                  "overslaat</strong>: 'drie jaar later' en je bent verder, de lezer vult de tussentijd "
                  "zelf in. Het omgekeerde bestaat ook: de tijd <strong>vertragen</strong> met <strong>een "
                  "gedachte van een personage die een bladzijde beslaat</strong> of <strong>een "
                  "gedetailleerde beschrijving van één moment</strong>. Wie versnelt, slaat over; wie "
                  "vertraagt, zoomt in. Beslaat een boek <strong>twee weken in vierhonderd "
                  "bladzijden</strong>, dan <strong>neemt de schrijver veel ruimte voor korte "
                  "tijdspannes</strong>."),
            ("p", "Staat een verhaal in de <strong>tegenwoordige tijd</strong>, dan <strong>lijken de "
                  "gebeurtenissen zich nu voor je ogen af te spelen</strong>: het haalt de afstand weg."),
        ]),
        dict(kop="Het thema", blokken=[
            ("p", "Het <strong>thema</strong> van een boek is <strong>waar het boek ten diepste over "
                  "gaat</strong>: verraad, schuld, opgroeien, macht. Het <strong>verschil tussen het "
                  "onderwerp en het thema</strong>: <strong>het onderwerp is waarover het gaat, het thema "
                  "wat de schrijver erover zegt</strong>. Twee boeken over een oorlog kunnen heel "
                  "verschillende thema's hebben. Blijkt een boek over een verhuizing eigenlijk over "
                  "afscheid nemen te gaan, dan is afscheid nemen <strong>het thema van het boek</strong>: "
                  "de verhuizing is wat er gebeurt."),
            ("p", "Een <strong>boek kan meer dan één thema hebben</strong>: vaak is er een hoofdthema met "
                  "een of twee neventhema's. En <strong>een thema kan je zelden in één enkel woord "
                  "samenvatten zonder iets te verliezen</strong>: 'schuld' dekt niet hetzelfde als 'de "
                  "schuld die een kind van zijn ouders overneemt'."),
            ("p", "Je achterhaalt het thema door te <strong>kijken welke vraag in het hele boek "
                  "terugkomt</strong>. Het <strong>thema staat meestal niet met zoveel woorden in de "
                  "tekst</strong>; je leidt het af uit wat terugkomt. <strong>Twee lezers moeten niet tot "
                  "hetzelfde thema komen</strong>: ze kunnen een ander thema aanwijzen en beide gelijk "
                  "hebben, als ze het met het boek kunnen onderbouwen. Vragen die bij zo'n gesprek horen: "
                  "<strong>welke vraag moet het hoofdpersonage steeds opnieuw beantwoorden?</strong> en "
                  "<strong>welke scène zou je aanwijzen als het hart van het boek?</strong>"),
        ]),
        dict(kop="Spanningsopbouw", blokken=[
            ("p", "Een schrijver bouwt spanning op <strong>door informatie achter te houden voor de "
                  "lezer</strong> en <strong>door een gevaar aan te kondigen dat nog niet "
                  "toeslaat</strong>. <strong>Verzwijgen is een van de sterkste middelen die een "
                  "schrijver voor spanning heeft</strong>: wat de lezer niet weet, wil hij weten."),
            ("p", "Andere middelen. Een <strong>cliffhanger</strong> is <strong>een hoofdstuk dat eindigt "
                  "op het spannendste moment</strong>. Een <strong>voorafschaduwing</strong> of "
                  "<strong>vooruitwijzing</strong> is <strong>een detail dat vooruitwijst naar wat nog "
                  "komt</strong>; bij een tweede lezing zie je ze pas allemaal. Een "
                  "<strong>deadline</strong>, zoals een trein die om zes uur vertrekt, <strong>zet de "
                  "personages onder tijdsdruk en verhoogt de spanning</strong>. En laat een schrijver "
                  "<strong>de lezer meer weten dan het hoofdpersonage</strong>, dan levert dat "
                  "<strong>spanning, want de lezer ziet het gevaar al aankomen</strong>."),
            ("p", "Een <strong>opening</strong> doet veel: begint een boek met een storm die het dorp "
                  "bedreigt, dan <strong>zet ze meteen een dreiging neer die het verhaal draagt</strong> "
                  "— als de eerste noot van een lied."),
            ("p", "<strong>Een spannend boek moet niet van begin tot eind even spannend blijven.</strong> "
                  "Een schrijver laat de spanning eerst dalen voor het slot <strong>om de laatste wending "
                  "harder te laten aankomen</strong>: spanning werkt met golven, niet met één rechte "
                  "lijn. En <strong>spanning zit niet alleen in een thriller of een "
                  "avonturenboek</strong>: ook in een rustig familieverhaal kan je willen weten of iemand "
                  "zijn geheim zal zeggen. <strong>Een verhaal kan spannend zijn zonder dat er iemand in "
                  "gevaar is.</strong>"),
        ]),
        dict(kop="Je eigen leeservaring", blokken=[
            ("p", "<strong>Je leeservaring onderbouwen betekent zeggen waaróm een boek je raakte</strong>, "
                  "met iets uit het boek zelf: <strong>je noemt een scène of een personage en zegt waarom "
                  "precies die</strong>. Een leeservaring wordt pas een gesprek als je ze aan iets in het "
                  "boek kan ophangen."),
        ]),
    ],
    onthoud=[
        "De ruimte is geen decor: open of gesloten, en wat ze met de personages doet.",
        "Tijdsprong versnelt, een lange beschrijving vertraagt; de tegenwoordige tijd haalt afstand weg.",
        "Onderwerp is waarover het gaat, thema is wat de schrijver erover zegt. Meerdere thema's mogen.",
        "Spanning: verzwijgen, een aangekondigd gevaar, een cliffhanger, een voorafschaduwing, een deadline.",
        "Spanning werkt met golven; ook zonder gevaar kan een boek spannend zijn.",
    ],
)

# ───────────────────── 12. Genres, fictie en non-fictie
BUNDELS["genres-fictie-en-non-fictie-en-je-eigen-leeservaring-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Genres, fictie en non-fictie, en je eigen leeservaring",
    onder="Wat bedacht is en wat niet, in welke vorm, en hoe je erover spreekt.",
    secties=[
        dict(kop="Fictie en non-fictie", blokken=[
            ("p", "<strong>Fictie</strong> is <strong>een verhaal dat door de schrijver bedacht is</strong>. "
                  "Het mag naar de werkelijkheid verwijzen, maar het is niet het verslag ervan. "
                  "<strong>Non-fictie</strong> is <strong>een tekst die de werkelijkheid wil "
                  "weergeven</strong>: het is geen genre, maar een hele groep genres."),
            ("p", "Een <strong>boek over een echte gebeurtenis kan toch fictie zijn</strong>: zodra de "
                  "schrijver gesprekken en gedachten bedenkt, is het een roman en geen verslag. Lees je "
                  "een boek waarin een <strong>echte politicus bedachte gesprekken voert</strong>, dan is "
                  "dat <strong>fictie, want de gesprekken zijn verzonnen</strong>. Het <strong>verschil "
                  "tussen een roman en een reportage</strong> over hetzelfde onderwerp: <strong>de roman "
                  "mag bedenken wat de reportage moet kunnen aantonen</strong>. En <strong>fictie heeft "
                  "niet minder waarde dan non-fictie</strong>: een roman kan over de werkelijkheid iets "
                  "zeggen wat geen verslag kan zeggen. <strong>Non-fictie kan even meeslepend verteld "
                  "zijn als een roman.</strong>"),
        ]),
        dict(kop="De courante genres", blokken=[
            ("p", tabel(["Genre", "Wat het is"], [
                ["De <strong>roman</strong>", "een lang verhaal met meerdere verhaallijnen"],
                ["De <strong>novelle</strong>", "korter dan een roman, met minder verhaallijnen"],
                ["Het <strong>kortverhaal</strong>", "kort, en het draait vaak om één enkel moment"],
                ["De <strong>jeugdroman</strong>", "een roman die geschreven is voor jonge lezers"],
                ["De <strong>strip</strong>", "tekstballonnen en kaders, met wit ertussen"],
                ["De <strong>graphic novel</strong>", "de middelen van de strip, langer en voor een ouder publiek"],
                ["De <strong>toneeltekst</strong>", "haast volledig dialoog en regieaanwijzingen"],
                ["De <strong>poëzie</strong>", "werkt met ritme, regelval en beeldtaal"],
                ["De <strong>non-fictie</strong>", "biografie, autobiografie, reisverhaal, journalistiek boek, essay, handboek"],
            ])),
            ("p", "Het <strong>verschil tussen een roman en een novelle</strong>: <strong>een novelle is "
                  "korter en heeft minder verhaallijnen dan een roman</strong>. De grens is niet scherp. "
                  "Een <strong>kortverhaal is kort en draait vaak om één enkel moment</strong>; het staat "
                  "meestal in een bundel samen met andere, en zo'n <strong>bundel kortverhalen moet geen "
                  "doorlopende verhaallijn hebben</strong>. Een <strong>jeugdroman is een roman die "
                  "geschreven is voor jonge lezers</strong>: het gaat om het beoogde publiek, niet om de "
                  "leeftijd van de schrijver of van de personages."),
            ("p", "Een <strong>graphic novel is niet hetzelfde als een stripverhaal voor "
                  "kinderen</strong>: dezelfde middelen, maar langer en voor een ouder publiek. Een boek "
                  "met <strong>korte stukken met tekeningen en tekstballonnen, bedoeld voor "
                  "volwassenen</strong>, is dus <strong>een graphic novel</strong>. En een "
                  "<strong>graphic novel kan ook non-fictie zijn</strong>: er bestaan graphic novels over "
                  "een oorlog of een ziekte, met echte getuigenissen als grond. De <strong>middelen die "
                  "een strip heeft en een roman niet</strong>: <strong>tekstballonnen en de indeling in "
                  "kaders</strong>, en <strong>het wit tussen de kaders, waarin tijd verstrijkt</strong> "
                  "— de lezer vult zelf in wat er tussen twee kaders gebeurde."),
            ("p", "Een <strong>toneeltekst</strong> <strong>bestaat haast volledig uit dialoog en "
                  "regieaanwijzingen</strong>: wat een verteller in een roman zou zeggen, moet hier uit de "
                  "mond van personages komen. Zie je een toneelstuk en lees je daarna de tekst, dan is "
                  "het grootste verschil dat <strong>de opvoering stem, beweging en decor aan de tekst "
                  "toevoegt</strong>. De tekst is het plan."),
            ("p", "<strong>Poëzie hoeft niet te rijmen om poëzie te zijn</strong>, en een <strong>gedicht "
                  "moet niet altijd over gevoelens gaan</strong>: er bestaan gedichten over een stad, een "
                  "machine of een politiek feit. De <strong>regelval</strong> in een gedicht "
                  "<strong>bepaalt waar de lezer even stilvalt</strong>; een afgebroken regel kan een "
                  "woord nadruk geven dat het in een gewone zin niet zou krijgen."),
            ("p", "Bij non-fictie: een <strong>biografie</strong> is <strong>een boek over het leven van "
                  "een echte persoon</strong>, een <strong>autobiografie</strong> <strong>een boek dat "
                  "iemand over zijn eigen leven schrijft</strong>. Verder horen erbij: <strong>het "
                  "reisverhaal en het journalistieke boek</strong>, en ook een handboek, een essay en een "
                  "historisch overzicht."),
        ]),
        dict(kop="Waarom je een genre benoemt", blokken=[
            ("p", "Je benoemt het genre voor je leest <strong>omdat je dan weet wat je ongeveer mag "
                  "verwachten</strong>. Verwachting hoort bij lezen, en een boek dat die verwachting "
                  "breekt, kan je daarna net verrassen. Zegt iemand dat een boek <strong>'een genre "
                  "doorbreekt'</strong>, dan <strong>wijkt het boek bewust af van wat de lezer "
                  "verwacht</strong>: wie een genre breekt, rekent erop dat je het kent. Een "
                  "<strong>genre is een afspraak tussen schrijvers en lezers, niet een wet</strong>; "
                  "daarom schuiven de grenzen en komen er nieuwe genres bij."),
            ("p", "Twee vragen bepalen het genre: <strong>is dit bedacht of wil het de werkelijkheid "
                  "weergeven?</strong> en <strong>hoe wordt het verhaal gebracht: in tekst, in beeld of "
                  "op een toneel?</strong> Een <strong>boek hoort niet altijd tot precies één "
                  "genre</strong>: een jeugdroman kan ook een detectiveverhaal zijn. En <strong>wie een "
                  "boek beoordeelt, moet het genre ervan meerekenen</strong>: een jeugdroman afrekenen op "
                  "wat je van een dikke roman verwacht, is niet eerlijk."),
        ]),
        dict(kop="Je eigen leeservaring verwoorden", blokken=[
            ("p", "Bij het <strong>verwoorden van je leeservaring</strong> hoort <strong>zeggen wat het "
                  "boek bij je losmaakte en waarom precies</strong>. Bruikbare uitspraken zeggen iets "
                  "over het boek: '<strong>het slot liet me onvoldaan, omdat één vraag open bleef</strong>' "
                  "of '<strong>ik herkende mezelf in het hoofdpersonage, vooral in zijn twijfel</strong>'. "
                  "Hoeveel dagen je erover deed of uit wiens kast het boek kwam, zegt niets over het boek."),
            ("p", "Van '<strong>ik vond het saai</strong>' maak je een bruikbaar oordeel door te zeggen "
                  "<strong>welk deel je saai vond en wat er volgens jou ontbrak</strong>. Een oordeel "
                  "wordt een gesprek zodra er een waarom bij staat. Ligt een boek je niet maar moet je "
                  "erover spreken, dan <strong>zeg je wat niet werkte voor jou, en waar dat volgens jou "
                  "aan ligt</strong>: afkeer onderbouwen is even waardevol als bewondering onderbouwen."),
            ("p", "Een <strong>boek dat je niet graag las, kan je wél goed vinden</strong>: een boek kan "
                  "sterk gemaakt zijn en jou toch niet liggen. <strong>Twee mensen lezen hetzelfde boek "
                  "anders omdat ze er met een andere ervaring aan beginnen</strong>; dat is geen fout, "
                  "dat is lezen. Vraagt een vriend of hij een boek moet lezen, dan zeg je <strong>wat je "
                  "ervan vond, en voor wie je denkt dat het werkt</strong>."),
        ]),
    ],
    onthoud=[
        "Fictie is bedacht, non-fictie wil de werkelijkheid weergeven; beide kunnen meeslepend zijn.",
        "Roman, novelle, kortverhaal, jeugdroman, strip, graphic novel, toneel, poëzie, non-fictie.",
        "Een genre is een afspraak, geen wet; een boek kan tot meerdere genres horen.",
        "Benoem het genre om te weten wat je mag verwachten, en reken het mee in je oordeel.",
        "Een leeservaring verwoord je met een scène of een personage erbij, ook als je het boek niet graag las.",
    ],
)

# ───────────────────── 13. Taalvariëteiten, registers en beleefdheid
BUNDELS["taalvarieteiten-registers-en-beleefdheid-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Taalvariëteiten, registers en beleefdheid",
    onder="Dezelfde taal, andere toon: wanneer welke vorm past.",
    secties=[
        dict(kop="De variëteiten", blokken=[
            ("p", tabel(["Variëteit", "Wat ze is"], [
                ["<strong>Standaardtaal</strong>", "de taalvorm die overal in het taalgebied begrepen wordt"],
                ["<strong>Tussentaal</strong>", "een taalvorm tussen het dialect en de standaardtaal in"],
                ["<strong>Dialect</strong> of streektaal", "de taalvariant van een bepaalde streek"],
                ["<strong>Jongerentaal</strong>", "de taal van jongeren onderling"],
                ["<strong>Jargon</strong> of vaktaal", "de vaktaal van een bepaalde beroepsgroep"],
            ])),
            ("p", "<strong>Standaardtaal</strong> wordt op school geleerd en in officiële teksten "
                  "gebruikt; niemand spreekt ze de hele dag. Ze is ook <strong>niet in Vlaanderen en "
                  "Nederland op elk punt identiek</strong>: er zijn verschillen in woorden en in "
                  "uitspraak, en ze zijn beide standaardtaal. Een <strong>dialect</strong> heeft "
                  "<strong>zijn eigen klanken en woorden</strong> en soms zijn eigen grammatica. "
                  "<strong>Tussentaal</strong> spreken veel Vlamingen in een gesprek met iemand die ze "
                  "niet goed kennen."),
            ("p", "<strong>Jongerentaal verandert sneller dan de standaardtaal</strong>: woorden komen en "
                  "gaan in een paar jaar, en dat is net de bedoeling, want ze markeren een groep. Mensen "
                  "gebruiken soms bewust dialect <strong>om te laten zien dat ze bij dezelfde groep "
                  "horen</strong>: taal is ook een teken van verbondenheid."),
            ("p", "<strong>Wie dialect spreekt, beheerst de standaardtaal niet minder goed</strong>: veel "
                  "mensen beheersen beide en schakelen vlot, en <strong>iemand kan meerdere variëteiten "
                  "vlot beheersen</strong>. Dat heet <strong>code switching</strong> of "
                  "<strong>codewisseling</strong>: <strong>wisselen van taalvariant of taal binnen één "
                  "gesprek</strong>. Iemand spreekt dialect met zijn ouders en tussentaal op het werk, "
                  "soms in dezelfde kamer. En <strong>wie goed wil spreken, moet zijn dialect niet "
                  "afleren</strong>: je voegt de standaardtaal toe aan wat je al kan."),
            ("p", "<strong>Elke taalvariant is niet in elke situatie even geschikt.</strong> Dialect op "
                  "de speelplaats werkt. Dialect in een examenantwoord werkt niet."),
        ]),
        dict(kop="Het register", blokken=[
            ("p", "Een <strong>register</strong> is <strong>de toon en woordkeuze die bij een situatie "
                  "passen</strong>. Met je vrienden spreek je anders dan in een sollicitatiegesprek, met "
                  "dezelfde taal. <strong>Je register kiezen hoort bij taalvaardigheid, niet bij "
                  "hoffelijkheid alleen</strong>: wie in elke situatie dezelfde toon gebruikt, mist de "
                  "helft van wat taal kan."),
            ("p", "Bij <strong>formeel taalgebruik</strong> horen <strong>volledige zinnen en "
                  "standaardtaal</strong>, en <strong>u of een beroepstitel om iemand aan te "
                  "spreken</strong>; geen spreektaalwendingen en geen woorden die enkel in een "
                  "vriendengroep gelden. Een tekst wordt <strong>informeler</strong> door <strong>jij in "
                  "plaats van u te gebruiken</strong> en <strong>korte zinnen en spreektaalwendingen toe "
                  "te laten</strong>. Informeel is niet slordig: het is een andere toon, met evenveel "
                  "zorg. En <strong>een tekst in te formele taal kan ook storen</strong>: een bericht aan "
                  "je ploegmaats in ambtelijke taal leest als een grap of als afstand."),
            ("p", "Welk register je kiest, hangt af van <strong>wie je gesprekspartner is en hoe goed je "
                  "die kent</strong> en van <strong>wat je met je boodschap wil bereiken</strong>, en ook "
                  "van de plaats en het moment. Het <strong>medium waarin je schrijft, beïnvloedt het "
                  "register dat je kiest</strong>: een chatbericht, een mail en een brief vragen elk een "
                  "andere toon, ook bij dezelfde ontvanger. In een <strong>chatbericht aan een vriend "
                  "gelden dus niet dezelfde regels als in een mail aan een school</strong>."),
            ("p", "Schrijf je een <strong>mail naar een bedrijf waar je nooit eerder mee sprak</strong>, "
                  "dan kies je <strong>formeel, met u en volledige zinnen</strong>. Spreek je op een "
                  "<strong>vergadering met mensen die je niet kent</strong>, dan begin je <strong>in "
                  "standaardtaal, en je stemt af op wat de anderen doen</strong>. Standaardtaal is de "
                  "veilige start."),
            ("p", "Schrijft een leerling in een sollicitatiemail '<strong>hey, heb je nog werk?</strong>', "
                  "dan <strong>past het register niet bij de situatie</strong>: niets is fout gespeld, "
                  "het is de toon die de deur sluit. Een <strong>tekst kan dus correct gespeld zijn en "
                  "toch in het verkeerde register staan</strong>."),
        ]),
        dict(kop="Jargon en heldere taal", blokken=[
            ("p", "<strong>Jargon</strong> is onder vakgenoten precies en snel, maar tegenover een leek "
                  "sluit het buiten. Het <strong>risico in een tekst voor een breed publiek</strong>: "
                  "<strong>de lezer die de termen niet kent, valt af</strong>. Jargon kan ook gebruikt "
                  "worden om indruk te maken; dan sluit het bewust uit."),
            ("p", "Legt een <strong>arts een diagnose uit aan een patiënt</strong>, dan doet ze het best "
                  "dit: <strong>ze gebruikt gewone woorden en noemt de vakterm erbij</strong>. De patiënt "
                  "begrijpt het en kan het woord later terugvinden in een verslag. Herschrijft een "
                  "<strong>gemeente haar brieven in heldere taal</strong>, dan <strong>begrijpt de "
                  "inwoner meteen wat van hem gevraagd wordt</strong>: ambtelijke taal is geen voorwaarde "
                  "om officieel te zijn."),
        ]),
        dict(kop="Beleefdheid", blokken=[
            ("p", "Het <strong>verschil tussen u en jij</strong>: <strong>u houdt afstand, jij "
                  "veronderstelt nabijheid</strong>. Beide zijn correct; welke past, hangt af van wie je "
                  "voor je hebt. Schakelt je gesprekspartner van u naar jij over, dan <strong>volg je, "
                  "want hij geeft daarmee een signaal</strong>. Spreekt een <strong>bedrijf zijn klanten "
                  "aan met jij</strong>, dan <strong>wil het dichter en toegankelijker overkomen</strong> "
                  "— niet elke klant waardeert dat. Een mail die begint met '<strong>Geachte heer of "
                  "mevrouw</strong>' zegt: <strong>de afzender kent je naam niet en houdt het "
                  "formeel</strong>."),
            ("p", "Wat een vraag beleefder maakt: <strong>de vraag als vraag stellen in plaats van als "
                  "bevel</strong>, en <strong>een woordje als misschien of eventueel toevoegen</strong>. "
                  "'Zou je dit kunnen nakijken?' klinkt anders dan 'Kijk dit na.' Maar <strong>een vraag "
                  "indirect stellen is niet altijd beleefder</strong>: te veel omhaal kan onduidelijk of "
                  "ontwijkend overkomen."),
            ("p", "<strong>Beleefdheid zit niet alleen in woorden, maar ook in toon en houding</strong>: "
                  "'alsjeblieft' met een zucht erachter is geen beleefdheid meer. Bij een "
                  "<strong>beleefde weigering</strong> hoort <strong>de weigering uitspreken en er een "
                  "reden bij geven</strong>: duidelijkheid is een vorm van hoffelijkheid, ontwijken niet. "
                  "Een <strong>moeilijke boodschap</strong> blijft hoffelijk door <strong>eerst te zeggen "
                  "wat je begrijpt van de andere kant</strong> en <strong>de boodschap zelf duidelijk en "
                  "zonder omhaal te brengen</strong>: zacht in de vorm, helder in de inhoud."),
        ]),
    ],
    onthoud=[
        "Standaardtaal, tussentaal, dialect, jongerentaal en jargon zijn vormen van dezelfde taal.",
        "Code switching is wisselen binnen één gesprek; meerdere variëteiten beheersen is winst.",
        "Register = toon en woordkeuze bij de situatie; gesprekspartner, doel en medium beslissen.",
        "Bij een onbekende: formeel beginnen. Te formeel kan ook storen.",
        "Beleefdheid zit in vorm, toon en houding; een weigering met een reden is hoffelijk.",
    ],
)

# ───────────────────── 14. Taal en identiteit
BUNDELS["taal-en-identiteit-stereotypering-inclusie-en-exclusie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Taal en identiteit: stereotypering, inclusie en exclusie",
    onder="Hoe woorden mensen insluiten of buitensluiten, en wat je daar zelf aan doet.",
    secties=[
        dict(kop="Stereotypering en veralgemening", blokken=[
            ("p", "Een <strong>stereotype</strong> is <strong>een vast beeld dat aan een hele groep wordt "
                  "toegekend</strong>. Het hoeft niet kwaad bedoeld te zijn om toch te knellen: iedereen "
                  "van die groep wordt erop afgerekend. <strong>Stereotypering komt dus niet alleen voor "
                  "in teksten die kwaad bedoeld zijn</strong>: veel stereotypen staan in goedbedoelde "
                  "teksten en in reclame, zonder dat iemand het merkt. Een <strong>stereotype kan ook "
                  "positief klinken en toch beperkend zijn</strong>: 'die zijn allemaal muzikaal' klinkt "
                  "vriendelijk en zet toch vast wie je mag zijn. En <strong>wie een stereotype gebruikt, "
                  "is daarmee niet automatisch een slecht mens</strong>: stereotypen zitten in de taal "
                  "die we allemaal leerden, en ze opmerken is de eerste stap."),
            ("p", "Een <strong>veralgemening</strong> of <strong>generalisatie</strong> is <strong>een "
                  "uitspraak over allen op grond van enkelen</strong>. 'Jongeren lezen niet meer' zegt "
                  "iets over miljoenen mensen op grond van een handvol. Woorden die er vaak op wijzen: "
                  "<strong>altijd en nooit</strong>, <strong>iedereen en niemand</strong>. Soms, vaak en "
                  "meestal nuanceren juist."),
            ("p", "Formuleringen die een onnodige veralgemening vermijden: '<strong>veel jongeren in dit "
                  "onderzoek lezen minder dan vroeger</strong>' en '<strong>een deel van de ondervraagden "
                  "zegt dat het niet weet</strong>'. Je zegt over wie je spreekt en hoeveel; dat kost "
                  "vier woorden en het houdt stand. Je gaat na of je zelf stereotypen gebruikt door te "
                  "<strong>kijken of je uitspraak op elk lid van de groep klopt</strong>: zodra je 'ja "
                  "maar niet voor allemaal' moet denken, heb je een veralgemening staan. Merk je dat je "
                  "<strong>eigen tekst een groep veralgemeent</strong>, dan <strong>noem je over wie je "
                  "precies spreekt en op welke grond</strong>. Preciezer worden is bijna altijd de "
                  "oplossing, en <strong>nadenken over je woordkeuze maakt een tekst niet "
                  "zwakker</strong>: een uitspraak die klopt, is moeilijker te weerleggen."),
        ]),
        dict(kop="Insluiten en buitensluiten", blokken=[
            ("p", "Dat <strong>taal mensen kan uitsluiten</strong>, betekent dat <strong>woorden iemand "
                  "buiten de groep kunnen plaatsen</strong>. Een formulier dat maar twee hokjes heeft, "
                  "sluit uit wie in geen van de twee past. <strong>Inclusief taalgebruik</strong> is "
                  "<strong>taal die niemand onnodig buitensluit</strong>: het gaat niet om verboden "
                  "woorden, maar om nadenken over wie je aanspreekt. <strong>Inclusief schrijven betekent "
                  "niet dat je geen enkele mening meer mag geven</strong>: je mag scherp zijn over een "
                  "idee of een daad."),
            ("p", "Spreekt een tekst over '<strong>de gewone Vlaming</strong>', dan <strong>wordt een "
                  "groep als norm gesteld en een andere daarbuiten</strong>. Wie is dan de ongewone "
                  "Vlaming? Noemt een tekst de mannelijke arts 'de dokter' en de vrouwelijke 'de "
                  "vrouwelijke dokter', dan <strong>wordt de ene vorm als norm gesteld en de andere als "
                  "uitzondering</strong>. Gebruikt een tekst <strong>'wij' en 'zij' voor twee groepen "
                  "inwoners</strong>, dan <strong>zet dat een scheiding neer die de tekst niet "
                  "uitlegt</strong>: de lezer wordt aan één kant gezet nog voor er een argument gevallen "
                  "is. Zoekt een vacature '<strong>een jonge, dynamische kracht</strong>', dan wordt "
                  "<strong>wie ouder is buitengesloten, ook al heeft die de gevraagde ervaring</strong>."),
            ("p", "Een <strong>tekst kan een groep onzichtbaar maken door er gewoon niet over te "
                  "spreken</strong>: wie in geen enkel voorbeeld, geen enkele foto en geen enkel verhaal "
                  "voorkomt, bestaat in die tekst niet. Toont een <strong>reclame enkel gezinnen van "
                  "hetzelfde type</strong>, dan <strong>lijken andere gezinsvormen minder gewoon</strong>. "
                  "Wat je nooit ziet, lijkt zeldzaam."),
            ("p", "Keuzes die een tekst <strong>toegankelijker</strong> maken: <strong>moeilijke "
                  "vaktermen uitleggen bij het eerste gebruik</strong> en <strong>aanspreken op een "
                  "manier die iedereen insluit</strong>. Toegankelijkheid zit in de woorden en in de vorm."),
        ]),
        dict(kop="Gevoelswaarde van woorden", blokken=[
            ("p", "De <strong>gevoelswaarde</strong> of <strong>connotatie</strong> van een woord is "
                  "<strong>de positieve of negatieve kleur die het meedraagt</strong>. <strong>Zuinig en "
                  "gierig</strong> betekenen bijna hetzelfde, maar het ene is een compliment. Zo ook "
                  "<strong>koppig en volhardend</strong>: wie zelf doorgaat is volhardend, wie de ander "
                  "is, is koppig."),
            ("p", "Een <strong>woord kan op zich neutraal zijn en toch kwetsend worden in een bepaalde "
                  "context</strong>, en <strong>twee mensen kunnen hetzelfde woord verschillend "
                  "ervaren</strong>: wat voor de een gewoon is, raakt bij de ander aan een ervaring die "
                  "jij niet hebt. Een <strong>aanvaarde term voor een groep verandert soms na een tijd, "
                  "omdat een woord in gebruik een negatieve kleur kan krijgen</strong>; het woord sleept "
                  "dan mee wat ermee gedaan is. En een <strong>groep mag wel invloed hebben op het woord "
                  "waarmee ze benoemd wordt</strong>: veel woorden zijn net veranderd omdat de mensen "
                  "zelf aangaven welke term ze willen."),
            ("p", "Dat <strong>taal mee iemands identiteit draagt</strong>, betekent: <strong>hoe iemand "
                  "spreekt, hoort bij wie hij is</strong>. Daarom raakt kritiek op iemands taal vaak "
                  "harder aan dan bedoeld."),
        ]),
        dict(kop="Lezen en schrijven over groepen", blokken=[
            ("p", "<strong>Hoe je over een groep spreekt, kan beïnvloeden hoe anderen die groep "
                  "zien</strong>: wie steeds hetzelfde beeld hoort, gaat het voor de werkelijkheid "
                  "houden. Een <strong>schrijver is verantwoordelijk voor het beeld dat zijn woorden "
                  "oproepen</strong>: ook wat je niet bedoelde, komt bij de lezer aan."),
            ("p", "Noemt een nieuwsbericht <strong>bij één verdachte zijn afkomst en bij een andere "
                  "niet</strong>, dan <strong>verbindt de lezer de daad met die afkomst</strong>: "
                  "informatie die niets verklaart maar wel gekoppeld wordt, blijft toch hangen. Staat "
                  "boven een artikel de kop '<strong>Weer problemen in die wijk</strong>', dan "
                  "<strong>wordt een eigenschap toegeschreven aan een hele wijk</strong>: het woord "
                  "'weer' maakt van losse feiten een patroon. En stelt een schrijver <strong>steeds "
                  "dezelfde groep als slachtoffer</strong> voor, dan <strong>maakt hij van een rol een "
                  "eigenschap van die groep</strong>; ook een goedbedoeld beeld kan vastzetten."),
            ("p", "Vragen die je bij zo'n tekst stelt: <strong>wie komt hier aan het woord en wie "
                  "niet?</strong> en <strong>op welke gegevens steunen de uitspraken over die "
                  "groep?</strong> Het <strong>verschil tussen een mening over een idee en een uitspraak "
                  "over een groep mensen</strong>: <strong>een idee kan je weerleggen, een groep mensen "
                  "niet</strong>. Daarom richt een eerlijke discussie zich op wat gezegd wordt."),
            ("p", "Middelen om een groep eerlijk in beeld te brengen: <strong>mensen uit die groep zelf "
                  "aan het woord laten</strong> en <strong>meerdere verhalen naast elkaar zetten in plaats "
                  "van één</strong>. Eén verhaal wordt al snel het verhaal. Een <strong>tekst over een "
                  "groep hoort dus niet zonder medewerking van die groep geschreven te worden</strong>: "
                  "wie erover schrijft zonder met de mensen te spreken, mist bijna altijd iets wezenlijks."),
        ]),
    ],
    onthoud=[
        "Een stereotype is een vast beeld over een hele groep; ook positief bedoeld kan het beperken.",
        "Altijd, nooit, iedereen en niemand verraden een veralgemening. Zeg over wie je spreekt en hoeveel.",
        "Taal sluit uit door een norm te stellen, door wij-zij, en door iemand niet te vermelden.",
        "Gevoelswaarde: zuinig of gierig, volhardend of koppig. Woorden veranderen van kleur.",
        "Een groep eerlijk in beeld: de mensen zelf aan het woord, en meerdere verhalen naast elkaar.",
    ],
)

# ───────────────────── 15. Klanken, spelling, diakritische tekens en interpunctie
BUNDELS["klanken-spelling-diakritische-tekens-en-interpunctie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Klanken, spelling, diakritische tekens en interpunctie",
    onder="Wat je hoort, wat je schrijft, en de tekens die het verschil maken.",
    secties=[
        dict(kop="Klank en letter", blokken=[
            ("p", "Het <strong>verschil tussen een klank en een letter</strong>: <strong>een klank hoor "
                  "je, een letter schrijf je</strong>. In 'school' schrijf je zes letters en hoor je vier "
                  "klanken. In het woord '<strong>auto</strong>' hoor je <strong>drie</strong> klanken, "
                  "want de au is één klank; er staan vier letters."),
        ]),
        dict(kop="Werkwoordspelling", blokken=[
            ("p", "De regel voor de <strong>tegenwoordige tijd bij hij, zij of het</strong>: <strong>de "
                  "stam plus een t, ook als de stam al op een d eindigt</strong>. Daarom schrijf je "
                  "<strong>hij wordt</strong>, hij vindt en hij antwoordt. Bij <strong>ik</strong> blijft "
                  "het de stam alleen: <strong>ik vind het goed</strong> tegenover <strong>hij vindt het "
                  "goed</strong>."),
            ("p", "Daarom geldt: <strong>hoe je een werkwoordsvorm uitspreekt, bepaalt niet altijd hoe je "
                  "ze schrijft</strong>. 'Hij antwoordt' klinkt precies als 'hij antwoord'; de regel "
                  "beslist."),
            ("p", "Voor de verleden tijd en het deelwoord geldt de regel van <strong>'t kofschip</strong>: "
                  "<strong>eindigt de stam op een van die klanken, dan komt er een t in het "
                  "verleden</strong>. Werkte, blafte, hoopte. Anders komt er een d: geleerd, gebeld. "
                  "<strong>Hij heeft gewerkt</strong> (stam op k), <strong>hij heeft geleerd</strong> "
                  "(stam op r), <strong>hij heeft gebeld</strong> — <strong>bel eindigt niet op een klank "
                  "van 't kofschip</strong>. En <strong>hij heeft de brief verstuurd</strong> met een d, "
                  "maar <strong>hij heeft het antwoord verwacht</strong> met één t, want wacht eindigt al "
                  "op een t."),
            ("p", "Een <strong>consonant verdubbelt bij het vervoegen als de klinker ervoor kort moet "
                  "blijven klinken</strong>: wij bellen met dubbele l, want bel-en met één l zou beelen "
                  "klinken. Een <strong>werkwoordsvorm heeft niet altijd een stam én een uitgang</strong>: "
                  "bij 'ik werk' staat de stam er alleen."),
            ("p", "Twijfel je over een vorm, dan <strong>vervang je hem door een werkwoord waar je het "
                  "hoort</strong>. Twijfel je bij 'hij heeft geleerd', probeer dan 'hij heeft gewerkt': "
                  "daar hoor je de t wel."),
        ]),
        dict(kop="Samenstellingen en meervoud", blokken=[
            ("p", "Een <strong>samenstelling van twee zelfstandige naamwoorden schrijf je in het "
                  "Nederlands niet los</strong> maar aan elkaar: tuinstoel, voetbalclub, fietspad. In een "
                  "<strong>samenstelling kan een tussen-n staan</strong>: pannenkoek, bessensap, omdat "
                  "het eerste deel een meervoud op en heeft. Voor de <strong>tussen-s bestaat geen vaste "
                  "rekenregel</strong>: je schrijft wat je hoort, en stationsplein hoor je met een s."),
            ("p", "Het Nederlands vormt het <strong>meervoud meestal met en of met s</strong>: boeken en "
                  "tafels. Een paar woorden hebben eren: <strong>kinderen</strong>, eieren."),
        ]),
        dict(kop="Diakritische tekens", blokken=[
            ("p", tabel(["Teken", "Waarvoor het dient", "Voorbeeld"], [
                ["Het <strong>trema</strong>", "het scheidt twee klinkers die anders samen gelezen worden", "ruïne, geïnteresseerd"],
                ["Het <strong>koppelteken</strong>", "het scheidt delen van een samenstelling die anders verkeerd gelezen wordt", "zee-eend, 3-jarige"],
                ["De <strong>apostrof</strong>", "een weggelaten letter, of een meervoud op een klinker", "'s morgens, foto's, Anna's boek"],
                ["Het <strong>accent aigu</strong>", "nadruk, en het voorkomt verwarring met een ander woord", "één boek tegenover een boek"],
                ["De <strong>cedille</strong>", "ze zorgt dat de c als een s klinkt", "façade"],
            ])),
            ("p", "In '<strong>ruïne</strong>' zou ui samen gelezen worden; het trema houdt u en i apart. "
                  "In '<strong>geïnteresseerd</strong>' staat er een trema omdat <strong>anders de ei als "
                  "één klank gelezen zou worden</strong>: het scheidt de e van ge en de i van interesse. "
                  "Bij <strong>zee-eend</strong> gebruik je een <strong>koppelteken in plaats van een "
                  "trema</strong>, want er staan twee keer ee naast elkaar."),
            ("p", "Een <strong>apostrof</strong> dient <strong>om een weggelaten letter aan te "
                  "duiden</strong> en <strong>om het meervoud van een woord op een klinker te "
                  "vormen</strong>: 's morgens en 't huis laten een letter weg, foto's en taxi's maken "
                  "het meervoud leesbaar. In het Nederlands vormt een <strong>bezitsvorm niet met een "
                  "apostrof en een s</strong> zoals in het Engels: je schrijft 'van de meeste mensen', "
                  "niet 'de meeste mensen's'. Maar een <strong>eigennaam kan wel een apostrof plus s "
                  "krijgen</strong>: Anna's boek en Lucas' jas zijn correct."),
            ("p", "Een <strong>samenstelling met een cijfer erin schrijf je mét koppelteken</strong>: "
                  "3-jarige, 100-jarig. En je <strong>mag een koppelteken gebruiken om een lange "
                  "samenstelling leesbaar te maken</strong>: arbeidsongeschiktheidsuitkering mag een "
                  "streepje krijgen waar de lezer het nodig heeft. Zonder cedille zou je in "
                  "<strong>façade</strong> faKade zeggen."),
        ]),
        dict(kop="Interpunctie", blokken=[
            ("p", "Een <strong>dubbelepunt</strong> gebruik je <strong>om aan te kondigen wat erna "
                  "komt</strong>: een opsomming, een citaat of een uitleg. Een <strong>puntkomma "
                  "verbindt twee zinnen die nauw bij elkaar horen</strong>: sterker dan een komma, "
                  "zwakker dan een punt. Een <strong>gedachtestreepje</strong> kondigt een toevoeging "
                  "achteraan aan."),
            ("p", "Een <strong>komma kan de betekenis van een zin veranderen</strong>: 'We gaan eten, "
                  "oma' is iets heel anders dan 'we gaan eten oma'. In een opsomming van drie delen komt "
                  "een komma <strong>tussen de eerste twee delen, en voor het laatste komt 'en'</strong>: "
                  "brood, kaas en melk. Voor een <strong>bijvoeglijke bijzin die alleen extra uitleg "
                  "geeft</strong>, <strong>zet je er een komma voor en erachter</strong>: 'Mijn broer, "
                  "die in Gent woont, komt morgen.'"),
            ("p", "<strong>Aanhalingstekens dienen niet enkel om iemands woorden letterlijk weer te "
                  "geven</strong>: ze kunnen ook afstand aangeven, zoals bij een zogenaamde 'oplossing' "
                  "die er geen is. Staat een tekst <strong>vol uitroeptekens</strong>, dan <strong>valt "
                  "de nadruk weg, want alles schreeuwt even hard</strong>: een leesteken werkt door "
                  "uitzondering."),
            ("p", "Een <strong>punt achter een afkorting is niet altijd verplicht</strong>: letterwoorden "
                  "als NMBS en pdf krijgen geen punten, bij bv. en enz. wel."),
            ("p", "<strong>Spelling en interpunctie zijn niet alleen van belang in een examen</strong>: in "
                  "een sollicitatiemail of een verslag beslissen ze mee hoe je overkomt. De "
                  "<strong>spelling van het Nederlands wordt om de tien jaar opnieuw vastgelegd</strong>, "
                  "in een herziene woordenlijst; de grote regels blijven wel staan."),
            ("p", "Eén woord kan ook van rol veranderen. Het <strong>verschil tussen 'haar' in 'haar "
                  "boek' en 'haar' in 'ik geef haar het boek'</strong>: <strong>het eerste is een "
                  "bezittelijk voornaamwoord, het tweede een persoonlijk</strong>."),
        ]),
    ],
    onthoud=[
        "Klanken hoor je, letters schrijf je; 'auto' heeft vier letters en drie klanken.",
        "Hij + stam + t, ook achter een d. 't Kofschip beslist tussen t en d in het verleden.",
        "Samenstellingen aan elkaar; tussen-n volgt een regel, tussen-s volgt je oor.",
        "Trema scheidt klinkers, koppelteken scheidt delen, apostrof laat een letter weg, cedille maakt c tot s.",
        "Dubbelepunt kondigt aan, puntkomma verbindt, een komma kan de betekenis veranderen.",
    ],
)

# ───────────────────── 16. Woordsoorten
BUNDELS["woordsoorten-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Woordsoorten",
    onder="Tien soorten woorden, en waarom de zin beslist tot welke soort een woord hoort.",
    secties=[
        dict(kop="De tien soorten", blokken=[
            ("p", tabel(["Woordsoort", "Wat ze doet", "Voorbeelden"], [
                ["Het <strong>lidwoord</strong>", "staat voor een zelfstandig naamwoord", "de, het, een"],
                ["Het <strong>zelfstandig naamwoord</strong>", "noemt een persoon, een ding of een begrip", "tafel, school, vrijheid"],
                ["Het <strong>bijvoeglijk naamwoord</strong>", "zegt iets over een zelfstandig naamwoord", "de snelle trein"],
                ["Het <strong>werkwoord</strong>", "de enige soort die je kan vervoegen", "lopen, zijn, worden"],
                ["Het <strong>voornaamwoord</strong>", "vervangt of wijst aan", "hij, mijn, deze, wie, iemand"],
                ["Het <strong>bijwoord</strong>", "zegt iets over een werkwoord, een bijvoeglijk naamwoord of de hele zin", "snel, niet, zelf, gisteren"],
                ["Het <strong>voorzetsel</strong>", "geeft een plaats, een tijd of een verhouding aan", "onder, na, met"],
                ["Het <strong>voegwoord</strong>", "verbindt woorden of zinnen", "omdat, maar, want, hoewel"],
                ["Het <strong>telwoord</strong>", "noemt een aantal", "drie (bepaald), veel (onbepaald)"],
                ["Het <strong>tussenwerpsel</strong>", "staat los van de zin en drukt een gevoel uit", "au, hé"],
            ])),
            ("p", "Het <strong>Nederlands kent drie lidwoorden</strong>, niet vijf: <strong>de, het en "
                  "een</strong>. <strong>Tafel</strong> is een <strong>zelfstandig naamwoord</strong>: je "
                  "kan er de of het voor zetten, en dat is de eenvoudigste proef. Je gaat dus na of een "
                  "woord een zelfstandig naamwoord is <strong>door te proberen of je er de, het of een "
                  "voor kan zetten</strong>."),
            ("p", "In '<strong>onder de tafel</strong>' is <strong>onder</strong> het voorzetsel. "
                  "<strong>Omdat</strong> en <strong>maar</strong> zijn <strong>voegwoorden</strong>; "
                  "onder is een voorzetsel en zeer een bijwoord. <strong>Drie</strong> is een "
                  "<strong>telwoord</strong>: bepaalde telwoorden noemen een aantal, onbepaalde telwoorden "
                  "zoals <strong>veel</strong> of enkele niet — in 'veel mensen kwamen' is veel dus een "
                  "<strong>onbepaald telwoord</strong>. <strong>Au</strong> in 'au, dat doet pijn' is een "
                  "<strong>tussenwerpsel</strong>, en zo'n <strong>tussenwerpsel kan een hele zin "
                  "vervangen</strong>: 'Hé!' is een volledige boodschap. <strong>Niet</strong> is een "
                  "<strong>bijwoord</strong>, want het zegt iets over het werkwoord of over de hele zin. "
                  "<strong>Hoewel</strong> is een <strong>voegwoord</strong> dat een bijzin inleidt."),
        ]),
        dict(kop="De voornaamwoorden", blokken=[
            ("p", tabel(["Soort voornaamwoord", "Voorbeelden"], [
                ["<strong>Persoonlijk</strong>", "hij, zij, haar in 'ik geef haar het boek'"],
                ["<strong>Bezittelijk</strong>", "mijn, hun, haar in 'haar boek'"],
                ["<strong>Aanwijzend</strong>", "deze en die, dit en dat"],
                ["<strong>Betrekkelijk</strong>", "die in 'de man die ik ken', dat in 'het boek dat ik las'"],
                ["<strong>Vragend</strong>", "wie, wat"],
                ["<strong>Onbepaald</strong>", "iemand, niemand, iets"],
            ])),
            ("p", "<strong>Hij</strong> is een <strong>persoonlijk voornaamwoord</strong>: het verwijst "
                  "naar een persoon. <strong>Mijn</strong> en <strong>hun</strong> zijn "
                  "<strong>bezittelijk</strong>; deze is aanwijzend, iemand onbepaald. In '<strong>die "
                  "man ken ik</strong>' is die een <strong>aanwijzend voornaamwoord</strong>, in 'de man "
                  "die ik ken' is hetzelfde woord <strong>betrekkelijk</strong>. In '<strong>hij vroeg "
                  "wie er kwam</strong>' is wie een <strong>vragend voornaamwoord</strong>, al staat die "
                  "vraag binnen een grotere zin."),
            ("p", "Een <strong>betrekkelijk voornaamwoord begint een bijzin die bij een eerder woord "
                  "hoort</strong>: in 'het boek dat ik las' begint dat de bijzin en verwijst het naar het "
                  "boek. Een <strong>onbepaald voornaamwoord verwijst niet naar een persoon die eerder "
                  "genoemd is</strong>: het doet net het omgekeerde en laat open wie of wat bedoeld wordt."),
        ]),
        dict(kop="De zin beslist", blokken=[
            ("p", "<strong>Eén woord kan tot meerdere woordsoorten horen, afhankelijk van de zin.</strong> "
                  "In 'de <strong>snelle</strong> trein' is snel een <strong>bijvoeglijk "
                  "naamwoord</strong>, want het zegt iets over de trein. In 'hij loopt <strong>snel</strong>' "
                  "is het een <strong>bijwoord</strong>, want het zegt iets over het werkwoord lopen. In "
                  "'de oude man liep <strong>traag</strong> naar huis' is traag <strong>een bijwoord, want "
                  "het zegt iets over liep</strong>."),
            ("p", "Je onderscheidt de twee door te <strong>kijken waar het woord bij hoort: bij een "
                  "naamwoord of bij een werkwoord</strong>. De zin beslist, niet de vorm van het woord. "
                  "<strong>Zelf</strong> in 'ik doe het zelf' is dus een <strong>bijwoord</strong>, want "
                  "het versterkt wat er over het werkwoord gezegd wordt. Een <strong>bijwoord kan niet "
                  "enkel iets zeggen over een werkwoord</strong>: in 'een <strong>bijzonder</strong> "
                  "mooie dag' zegt bijzonder iets over mooi. Een <strong>bijwoord van tijd</strong> "
                  "<strong>zegt wanneer iets gebeurt</strong>: gisteren, straks, nooit."),
            ("p", "Een <strong>werkwoord kan ook als zelfstandig naamwoord gebruikt worden</strong>: 'Het "
                  "lezen gaat hem goed af.' Door het lidwoord wordt lezen een zelfstandig naamwoord. Een "
                  "<strong>voorzetsel staat niet altijd voor het woord waar het bij hoort</strong>: in "
                  "'het bos in' staat het erachter, en dan heet het een achterzetsel."),
            ("p", "Twee uitspraken die kloppen: <strong>de woordsoort hangt af van de rol in de "
                  "zin</strong>, en <strong>hetzelfde woord kan in twee zinnen tot twee soorten "
                  "horen</strong>. Daarom benoem je een woord altijd binnen zijn zin, en nooit op "
                  "zichzelf."),
            ("p", "Twee misverstanden. Een <strong>werkwoord staat niet altijd op de tweede plaats in een "
                  "Nederlandse zin</strong>: dat geldt voor de persoonsvorm in een hoofdzin, in een "
                  "bijzin staat hij achteraan. En een <strong>bijvoeglijk naamwoord kan ook na het "
                  "werkwoord staan</strong>: 'De trein is snel.'"),
            ("p", "Een <strong>bijvoeglijk naamwoord krijgt niet in elke zin een e</strong>: een mooi huis "
                  "heeft geen e, een mooie tuin wel. Het lidwoord en het woordgeslacht beslissen. En een "
                  "<strong>zin kan uit één woordsoort bestaan</strong>: 'Kom!' is een volledige zin met "
                  "enkel een werkwoord."),
        ]),
        dict(kop="Waarom je ze kent", blokken=[
            ("p", "<strong>Woordsoorten kennen helpt bij het spellen van werkwoordsvormen</strong>: wie "
                  "de persoonsvorm vindt, weet welke uitgang hij moet schrijven. Moet je in een examen de "
                  "woordsoorten in een zin benoemen, dan <strong>zoek je eerst de werkwoorden, want die "
                  "dragen de zin</strong>. Daarna valt de rest vlugger op zijn plaats. Het "
                  "<strong>werkwoord is ook de enige soort die je kan vervoegen</strong>: een zelfstandig "
                  "naamwoord kan je wel in het meervoud zetten, maar niet vervoegen."),
        ]),
    ],
    onthoud=[
        "Tien soorten: lidwoord, zelfstandig en bijvoeglijk naamwoord, werkwoord, voornaamwoord, bijwoord, voorzetsel, voegwoord, telwoord, tussenwerpsel.",
        "Drie lidwoorden: de, het, een. De proef voor een zelfstandig naamwoord: zet er de of het voor.",
        "Zes soorten voornaamwoord: persoonlijk, bezittelijk, aanwijzend, betrekkelijk, vragend, onbepaald.",
        "De zin beslist: snel is bijvoeglijk bij een naamwoord en bijwoord bij een werkwoord.",
        "Begin bij het werkwoord: dat draagt de zin en bepaalt de spelling van de persoonsvorm.",
    ],
)

# ───────────────────── 17. Morfologie
BUNDELS["morfologie-samenstellingen-afleidingen-en-werkwoordstijden-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Morfologie: samenstellingen, afleidingen en werkwoordstijden",
    onder="Woorden in hun delen uitpakken, en de tijden van het werkwoord.",
    secties=[
        dict(kop="Samenstelling of afleiding", blokken=[
            ("p", "Een <strong>samenstelling</strong> is <strong>een woord dat uit twee of meer "
                  "zelfstandige woorden bestaat</strong>: tuinstoel is tuin en stoel, en beide delen "
                  "kunnen ook alleen staan. <strong>Voetbalveld</strong>, <strong>boekenkast</strong>, "
                  "<strong>keukentafel</strong> en <strong>spoorweg</strong> zijn samenstellingen."),
            ("p", "Een <strong>afleiding</strong> is <strong>een woord met een voorvoegsel of een "
                  "achtervoegsel erbij</strong>. Onvriendelijk is vriend plus on en lijk, en die delen "
                  "kunnen niet alleen staan. <strong>Ongeluk</strong> en <strong>vriendschap</strong> zijn "
                  "dus afleidingen, net als <strong>bakker</strong> en <strong>onmogelijk</strong>. Ook "
                  "<strong>schrijver</strong> is een afleiding van schrijven: het achtervoegsel er maakt "
                  "van de handeling een persoon, terwijl schrijfmachine een samenstelling is."),
            ("p", "Een <strong>voorvoegsel</strong> of <strong>prefix</strong> is <strong>een woorddeel "
                  "dat vooraan een woord komt</strong>, zoals on in onvriendelijk. Een "
                  "<strong>achtervoegsel</strong> of <strong>suffix</strong> komt achteraan, zoals heid "
                  "in vrijheid. In '<strong>onbereikbaar</strong>' is on het voorvoegsel, bereik de stam "
                  "en <strong>baar</strong> het achtervoegsel."),
            ("p", "Een <strong>woord kan tegelijk een samenstelling en een afleiding bevatten</strong>: "
                  "<strong>werkloosheid</strong> bestaat uit <strong>werk, loos en heid</strong> — "
                  "werkloos is al een afleiding, en heid maakt er een toestand van. En het "
                  "<strong>laatste deel van een samenstelling bepaalt de woordsoort van het "
                  "geheel</strong>: een voetbalveld is een veld, een veldvoetbal zou een bal zijn. Het "
                  "<strong>verschil tussen 'een voetbalveld' en 'een veld voor voetbal'</strong>: "
                  "<strong>het eerste is één woord, het tweede een woordgroep</strong>; een samenstelling "
                  "is één begrip geworden."),
            ("p", "Het <strong>Nederlands maakt makkelijk nieuwe samenstellingen aan</strong>, en daarom "
                  "staan veel samenstellingen niet in het woordenboek en zijn ze toch correct. Een "
                  "<strong>samenstelling van drie woorden bestaat wel degelijk</strong>: "
                  "spoorwegovergang, basisschooldirecteur, arbeidsmarktbeleid. En <strong>nieuwe woorden "
                  "zijn niet vrijwel altijd leenwoorden uit het Engels</strong>: veel nieuwe woorden zijn "
                  "eigen samenstellingen of afleidingen, gemaakt met bestaande delen."),
            ("p", "De <strong>tussenletters in een samenstelling hangen af van het eerste deel</strong>: "
                  "pannenkoek heeft en omdat pan een meervoud op en heeft."),
        ]),
        dict(kop="Wat voor- en achtervoegsels doen", blokken=[
            ("p", tabel(["Woorddeel", "Wat het doet", "Voorbeeld"], [
                ["<strong>baar</strong>", "maakt er een bijvoeglijk naamwoord van", "bereiken wordt bereikbaar"],
                ["<strong>heid</strong>", "maakt van een eigenschap een zelfstandig naamwoord", "vrij wordt vrijheid, snel wordt snelheid"],
                ["<strong>er</strong>", "maakt van de handeling een persoon", "schrijven wordt schrijver"],
                ["<strong>on</strong>", "ontkenning", "onmogelijk, onherkenbaar"],
                ["<strong>her</strong>", "opnieuw", "herlezen, herbouwen, herhalen"],
                ["<strong>ver</strong>", "een verandering van toestand, of een verkeerde uitvoering", "vergroten; verslapen, verschrijven"],
            ])),
            ("p", "<strong>Her</strong> in herlezen betekent <strong>opnieuw</strong>. <strong>Ver</strong> "
                  "kan twee dingen: <strong>een verandering van toestand, zoals in verven of "
                  "vergroten</strong>, en <strong>een verkeerde uitvoering, zoals in verslapen of "
                  "verschrijven</strong>. Verlezen en vermogelijk bestaan niet."),
            ("p", "Een <strong>verkleinwoord</strong> vorm je met <strong>je en tje</strong>, of met "
                  "<strong>pje en kje</strong>: huisje, autootje, boompje, koninkje. Een "
                  "<strong>verkleinwoord is niet altijd kleiner dan het woord waar het van komt</strong>: "
                  "een biertje is geen kleiner bier, en een momentje geen korter moment. Het is vaak een "
                  "toon."),
            ("p", "<strong>Woorden ontleden in hun delen helpt bij het begrijpen van een onbekend "
                  "woord</strong>: wie on en baar kent, raadt de betekenis van onbetaalbaar zonder "
                  "woordenboek. <strong>Onherkenbaar</strong> is on plus herken plus baar, en "
                  "<strong>onvervangbaar</strong> splits je in <strong>on, vervang en baar</strong>: niet "
                  "te vervangen. Een <strong>onbekend woord kan je dus soms begrijpen door naar zijn "
                  "delen te kijken</strong>."),
        ]),
        dict(kop="De werkwoordstijden", blokken=[
            ("p", "Een <strong>stam</strong> is <strong>de infinitief zonder uitgang</strong>: de stam "
                  "van werken is werk. De <strong>stam is dus niet hetzelfde als de infinitief</strong>."),
            ("p", tabel(["Tijd", "Waarvoor", "Voorbeeld"], [
                ["De <strong>tegenwoordige tijd</strong>", "iets dat nu gebeurt, een gewoonte of een algemene waarheid", "hij loopt"],
                ["De <strong>verleden tijd</strong>", "iets dat voorbij is", "hij liep"],
                ["De <strong>voltooid tegenwoordige tijd</strong>", "iets dat afgelopen is en nu nog gevolgen heeft", "hij heeft gegeten"],
                ["De <strong>voltooid verleden tijd</strong>", "iets dat gebeurde vóór een ander moment in het verleden", "hij had gegeten voor ik aankwam"],
                ["De <strong>toekomende tijd</strong>", "iets dat nog komt", "hij zal gaan, of: morgen ga ik"],
            ])),
            ("p", "'<strong>Hij heeft gegeten</strong>' zegt iets over nu: hij heeft geen honger meer. De "
                  "vorm <strong>gegeten</strong> is een <strong>voltooid deelwoord</strong>; samen met "
                  "heeft of is vormt het de voltooide tijd. Het <strong>Nederlands heeft geen eigen vorm "
                  "voor de toekomende tijd</strong>: je gebruikt zullen plus de infinitief, of gewoon de "
                  "tegenwoordige tijd."),
            ("p", "De <strong>voltooid verleden tijd</strong> gebruik je <strong>voor iets dat gebeurde "
                  "vóór een ander moment in het verleden</strong>. Zonder die tijd kan je de orde van "
                  "twee gebeurtenissen in het verleden niet aangeven."),
            ("p", "Een <strong>sterk werkwoord</strong> is <strong>een werkwoord waarvan de klinker "
                  "verandert in de verleden tijd</strong>: <strong>lopen wordt liep</strong>, "
                  "<strong>breken wordt brak</strong>, zingen wordt zong en gezongen. Bij een "
                  "<strong>zwak</strong> werkwoord komt er alleen een uitgang bij en blijft de klinker "
                  "dezelfde: praten wordt praatte, wandelen wordt wandelde, werken blijft werkte en "
                  "gewerkt."),
            ("p", "Het Nederlands vervoegt sommige werkwoorden met <strong>zijn</strong> en andere met "
                  "<strong>hebben</strong>, <strong>omdat zijn bij een verandering van toestand of plaats "
                  "hoort</strong>: hij is gevallen, hij is gegaan, tegenover hij heeft gelezen en hij "
                  "heeft gewerkt."),
            ("p", "Een <strong>verhaal staat vaak in de verleden tijd omdat het verteld wordt als iets "
                  "dat al gebeurd is</strong>. Veel moderne romans kiezen juist de tegenwoordige tijd, om "
                  "dichter te komen."),
        ]),
    ],
    onthoud=[
        "Samenstelling: twee zelfstandige woorden. Afleiding: een voor- of achtervoegsel erbij.",
        "Het laatste deel van een samenstelling bepaalt de woordsoort van het geheel.",
        "baar maakt een eigenschap, heid een toestand, er een persoon; her is opnieuw, on is niet.",
        "Vijf tijden; het Nederlands heeft geen eigen toekomende tijd, maar gebruikt zullen of het heden.",
        "Sterk werkwoord: de klinker verandert. Zwak: er komt enkel een uitgang bij.",
    ],
)

# ───────────────────── 18. Zinsontleding en zinsbouw
BUNDELS["zinsontleding-en-zinsbouw-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Zinsontleding en zinsbouw",
    onder="De zinsdelen benoemen, en de fouten die een zin onleesbaar maken.",
    secties=[
        dict(kop="De zinsdelen", blokken=[
            ("p", "De <strong>persoonsvorm</strong> is <strong>het werkwoord dat verandert met het "
                  "onderwerp</strong>. Zet de zin in een andere tijd: het woord dat meeverandert, is de "
                  "persoonsvorm. Het <strong>onderwerp</strong> vind je door <strong>wie of wat te vragen "
                  "bij de persoonsvorm</strong>: 'De hond blaft.' Wie blaft? De hond."),
            ("p", tabel(["Zinsdeel", "Hoe je het vindt", "Voorbeeld"], [
                ["De <strong>persoonsvorm</strong>", "het werkwoord dat met het onderwerp meeverandert", "hij <em>leest</em> een boek"],
                ["Het <strong>onderwerp</strong>", "wie of wat bij de persoonsvorm", "<em>hij</em> leest een boek"],
                ["Het <strong>lijdend voorwerp</strong>", "wie of wat na onderwerp en werkwoord samen", "hij leest <em>een boek</em>"],
                ["Het <strong>meewerkend voorwerp</strong>", "aan wie; je kan 'aan' ervoor zetten", "hij geeft <em>zijn zus</em> een boek"],
                ["De <strong>bijwoordelijke bepaling</strong>", "waar, wanneer, hoe, waarom", "hij speelt <em>in de tuin</em>"],
                ["Het <strong>naamwoordelijk gezegde</strong>", "een koppelwerkwoord met een naamwoord erbij", "zijn vader is <em>leraar</em>"],
            ])),
            ("p", "In 'hij leest een boek' is <strong>een boek</strong> het lijdend voorwerp. In 'hij "
                  "geeft zijn zus een boek' is <strong>zijn zus</strong> het meewerkend voorwerp: aan wie "
                  "geeft hij het boek? In 'hij speelt in de tuin' is <strong>in de tuin</strong> een "
                  "<strong>bijwoordelijke bepaling van plaats</strong>. In 'morgen gaan wij naar de stad' "
                  "is <strong>morgen een bijwoordelijke bepaling van tijd</strong> en <strong>naar de "
                  "stad een bijwoordelijke bepaling van plaats</strong>; wij is het onderwerp en gaan de "
                  "persoonsvorm."),
            ("p", "<strong>Niet elke zin heeft een lijdend voorwerp</strong>: 'De hond blaft' heeft er "
                  "geen, want veel werkwoorden hebben er geen nodig. Een <strong>zin kan meer dan één "
                  "bijwoordelijke bepaling bevatten</strong>: 'Gisteren speelde hij lang in de tuin' "
                  "heeft er drie, van tijd, van duur en van plaats. En de <strong>plaats van een "
                  "bijwoordelijke bepaling kan de betekenis van een zin veranderen</strong>: 'Hij zei "
                  "gisteren dat hij kwam' is iets anders dan 'hij zei dat hij gisteren kwam'."),
            ("p", "Een <strong>naamwoordelijk gezegde</strong> is <strong>een gezegde met een "
                  "koppelwerkwoord en een naamwoord erbij</strong>. <strong>Zijn en worden</strong>, "
                  "<strong>blijven en lijken</strong> zijn koppelwerkwoorden, net als blijken, schijnen "
                  "en heten. In 'zijn vader is leraar' is <strong>leraar het naamwoordelijk deel van het "
                  "gezegde</strong>: na een koppelwerkwoord volgt geen voorwerp maar een eigenschap van "
                  "het onderwerp. Je weet dat een werkwoord een koppelwerkwoord is doordat <strong>het "
                  "woord erna iets zegt over het onderwerp zelf</strong>: 'hij wordt dokter' tegenover "
                  "'hij wordt geroepen'."),
            ("p", "Bij het ontleden volg je deze orde: <strong>eerst de persoonsvorm zoeken</strong>, en "
                  "<strong>daarna wie of wat vragen om het onderwerp te vinden</strong>. Dan het gezegde, "
                  "de voorwerpen en de bepalingen. <strong>Zinsontleding helpt bij het correct spellen "
                  "van werkwoorden</strong>: wie het onderwerp en de persoonsvorm vindt, weet welke "
                  "uitgang erbij hoort."),
        ]),
        dict(kop="Hoofdzin en bijzin", blokken=[
            ("p", "In een <strong>Nederlandse hoofdzin staat de persoonsvorm op de tweede plaats</strong>, "
                  "ook als er iets anders vooraan staat: 'Morgen gaan wij', niet 'morgen wij gaan'. Het "
                  "<strong>verschil met een bijzin</strong>: <strong>in een bijzin staat de persoonsvorm "
                  "achteraan</strong>. 'Hij bleef thuis omdat hij ziek was.'"),
            ("p", "Een <strong>bijzin</strong> is <strong>een zin die niet op zichzelf kan staan en die "
                  "met een voegwoord begint</strong>. Ze <strong>heeft wel een eigen onderwerp en een "
                  "eigen persoonsvorm</strong>; het verschil is dat ze niet alleen kan staan en dat de "
                  "persoonsvorm naar achteren schuift. Een <strong>bijzin kan voor de hoofdzin "
                  "staan</strong>: 'Omdat hij ziek was, bleef hij thuis' — de persoonsvorm van de "
                  "hoofdzin volgt dan meteen. Een <strong>zin mag dus met een voegwoord beginnen</strong>."),
            ("p", "Correct gebouwd zijn: '<strong>omdat het regende, bleven wij binnen</strong>' en "
                  "'<strong>wij bleven binnen, want het regende</strong>'. Na een bijzin vooraan komt de "
                  "persoonsvorm meteen; na want volgt een gewone hoofdzin. Een <strong>zin met twee "
                  "bijzinnen in elkaar is niet altijd fout</strong>, maar het wordt snel onleesbaar."),
        ]),
        dict(kop="De bedrijvende en de lijdende vorm", blokken=[
            ("p", "In '<strong>de wedstrijd werd door de regen afgelast</strong>' is <strong>de wedstrijd "
                  "het onderwerp van de zin</strong>: in een lijdende zin wordt wat de handeling ondergaat "
                  "het onderwerp. In een <strong>lijdende zin kan de handelende persoon helemaal "
                  "weggelaten worden</strong>, en daarom is die vorm zo geliefd in teksten die geen naam "
                  "willen noemen."),
            ("p", "Veel teksten schrijven liever in de <strong>bedrijvende vorm omdat je dan ziet wie "
                  "iets doet</strong>. 'Er werden fouten gemaakt' zegt niet door wie — soms is dat net "
                  "de bedoeling."),
        ]),
        dict(kop="Fouten in de zinsbouw", blokken=[
            ("p", "Een <strong>tangconstructie</strong> is <strong>twee woorden die bij elkaar horen en "
                  "te ver van elkaar staan</strong>: 'Hij heeft gisteren na een lange dag op het werk in "
                  "de regen gelopen.' Heeft en gelopen staan te ver uiteen. Je lost dat op door "
                  "<strong>de twee werkwoorden dichter bij elkaar te zetten</strong>, of door de zin in "
                  "twee te knippen. Hetzelfde geldt voor 'de brief die ik gisteren kreeg, en waarin stond "
                  "dat ik moest komen, lag nog op tafel': <strong>de twee bijzinnen tussen onderwerp en "
                  "persoonsvorm maken de zin zwaar</strong>."),
            ("p", "Andere veelgemaakte fouten: <strong>een deelwoord dat bij niemand in de zin "
                  "hoort</strong>, en <strong>twee zinsdelen die door en verbonden worden maar niet "
                  "dezelfde vorm hebben</strong>. In 'lopend door het bos viel de regen op mijn hoofd' "
                  "<strong>hoort het deelwoord bij iemand die niet in de zin staat</strong>: volgens de "
                  "zin loopt de regen door het bos. In 'hij houdt van lezen, wandelen en hij kookt graag' "
                  "<strong>hebben de drie delen van de opsomming niet dezelfde vorm</strong>: maak er "
                  "lezen, wandelen en koken van. <strong>Delen van een opsomming horen dezelfde vorm te "
                  "hebben.</strong>"),
            ("p", "Ook de tijden moeten kloppen. In 'hij vertelde dat hij kwam en dat hij blijft eten' "
                  "<strong>passen de werkwoordstijden in de twee bijzinnen niet bij elkaar</strong>."),
            ("p", "Een <strong>lange zin is niet altijd een slechte zin</strong>: een lange zin met een "
                  "heldere bouw leest prima, het probleem is verwarring. Maar 'door de regen werd de "
                  "wedstrijd afgelast, waardoor wij teleurgesteld waren en niemand kwam' <strong>rijgt te "
                  "veel delen aan elkaar en wordt onduidelijk</strong>. Is je tekst te zwaar, dan "
                  "<strong>knip je de zin in twee of drie kortere zinnen</strong>: wat jij niet in één "
                  "keer begrijpt, begrijpt je lezer ook niet."),
        ]),
    ],
    onthoud=[
        "Eerst de persoonsvorm, dan wie of wat voor het onderwerp. Daarna gezegde, voorwerpen, bepalingen.",
        "In een hoofdzin staat de persoonsvorm tweede, in een bijzin achteraan.",
        "Een koppelwerkwoord geeft een eigenschap van het onderwerp, geen voorwerp.",
        "Tangconstructie: woorden die bij elkaar horen staan te ver uiteen. Knip of schuif.",
        "Een foutief verbonden deelwoord en een scheve opsomming zijn de klassiekers.",
    ],
)

# ───────────────────── 19. Semantiek
BUNDELS["semantiek-betekenisrelaties-gevoelswaarde-en-humor-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Semantiek: betekenisrelaties, gevoelswaarde en humor",
    onder="Hoe woorden zich tot elkaar verhouden, en wat beeldspraak en humor doen.",
    secties=[
        dict(kop="Betekenisrelaties", blokken=[
            ("p", tabel(["Relatie", "Wat ze is", "Voorbeeld"], [
                ["<strong>Synoniem</strong>", "een woord met bijna dezelfde betekenis als een ander", "fiets en rijwiel, huis en woning"],
                ["<strong>Antoniem</strong>", "een woord met de tegengestelde betekenis", "warm en koud, aanwezig en afwezig, stijgen en dalen"],
                ["<strong>Homoniem</strong>", "een woord dat hetzelfde klinkt maar iets anders betekent", "bank, slot"],
                ["<strong>Hyperoniem</strong>", "een woord dat een hele groep aanduidt waar andere woorden in vallen", "meubel boven stoel, tafel en kast"],
            ])),
            ("p", "Een synoniem heeft <strong>bijna</strong> dezelfde betekenis, zelden helemaal: "
                  "<strong>twee synoniemen zijn niet altijd in dezelfde zin uitwisselbaar</strong>. "
                  "Zuinig en gierig duiden hetzelfde gedrag aan, maar het ene is een verwijt. "
                  "<strong>Bank</strong> is een homoniem, want je kan erop zitten en er geld halen; "
                  "<strong>slot</strong> ook, want het sluit een deur en het eindigt een verhaal. Twee "
                  "betekenissen die niets met elkaar te maken hebben, in dezelfde vorm."),
            ("p", "Het <strong>hyperoniem van roos, tulp en madelief is bloem</strong>. Plant is ook een "
                  "hyperoniem, maar een stap hoger."),
            ("p", "<strong>Niet elk woord heeft precies één betekenis</strong>: veel woorden hebben er "
                  "meerdere, en de zin beslist welke bedoeld is. Twee dingen die kloppen: <strong>de zin "
                  "beslist welke betekenis van een woord geldt</strong>, en <strong>een woord kan tegelijk "
                  "een letterlijke en een figuurlijke betekenis hebben</strong>. Een woordenboek geeft de "
                  "mogelijkheden, niet de bedoelde betekenis. En een <strong>woord kan zijn betekenis in "
                  "de loop van de tijd veranderen</strong>: leuk betekende eerst lauw, en vrouw betekende "
                  "eerst edele dame."),
            ("p", "De <strong>gevoelswaarde</strong> van een woord kan ook per zin verschillen: "
                  "'<strong>ambitieus</strong>' is een compliment bij een plan en een verwijt bij een "
                  "persoon."),
        ]),
        dict(kop="Letterlijk en figuurlijk", blokken=[
            ("p", "<strong>Figuurlijk taalgebruik</strong> is <strong>woorden gebruiken in een andere dan "
                  "hun eigenlijke betekenis</strong>: 'hij barstte in tranen uit' — niemand barst echt. "
                  "'<strong>De tijd vliegt voorbij</strong>' en '<strong>hij heeft een zware dag achter "
                  "zich</strong>' zijn figuurlijk: tijd heeft geen vleugels en een dag weegt niets. Een "
                  "vogel die over het dak vliegt en een koffer die zwaar is, zijn letterlijk."),
            ("p", "Zegt een reclame '<strong>onze prijzen zijn gevallen</strong>', dan is dat een "
                  "<strong>figuurlijk gebruik van vallen</strong>: prijzen vallen niet echt. Kom je het "
                  "woord '<strong>krimpen</strong>' tegen in een tekst over de economie, dan <strong>lees "
                  "je het figuurlijk, als een daling</strong>: het beeld komt uit de stof."),
        ]),
        dict(kop="Beeldspraak", blokken=[
            ("p", "Bij <strong>beeldspraak</strong> horen <strong>de metafoor en de vergelijking</strong> "
                  "en <strong>de personificatie</strong>."),
            ("p", tabel(["Middel", "Wat het is", "Voorbeeld"], [
                ["De <strong>metafoor</strong>", "een beeld dat in de plaats van het bedoelde woord komt", "'Die man is een leeuw.'"],
                ["De <strong>vergelijking</strong>", "hetzelfde beeld, mét als of zoals", "'Hij vecht als een leeuw.'"],
                ["De <strong>personificatie</strong>", "een ding of een begrip een menselijke eigenschap geven", "'De wind huilde de hele nacht.'"],
            ])),
            ("p", "Het <strong>verschil tussen een vergelijking en een metafoor</strong>: <strong>een "
                  "vergelijking gebruikt het woordje als of zoals, een metafoor niet</strong>. Bij een "
                  "metafoor neemt het beeld de plaats over."),
            ("p", "<strong>Beeldspraak komt niet alleen in gedichten voor</strong>: de economie krimpt, "
                  "een partij verliest terrein — ook een nieuwsbericht staat er vol van. Schrijvers "
                  "gebruiken beeldspraak <strong>om iets abstracts met iets vertrouwds te laten "
                  "begrijpen</strong>: een economie die krimpt, snap je zonder één cijfer te zien."),
            ("p", "Twee valkuilen. Een <strong>versleten metafoor valt de lezer niet meer op</strong>: de "
                  "poot van een tafel of de hals van een fles leest niemand nog als een beeld. En "
                  "<strong>twee beelden door elkaar gebruiken in één zin is meestal een fout</strong>: "
                  "'dat schip is uit de hand gelopen' mengt twee beelden en wordt lachwekkend. Een "
                  "<strong>tekst vol beelden is daarom niet een betere tekst</strong>: één beeld dat "
                  "klopt, werkt sterker dan vijf losse."),
        ]),
        dict(kop="Vaste uitdrukkingen", blokken=[
            ("p", "Een <strong>vaste uitdrukking</strong> is <strong>een groepje woorden met een "
                  "betekenis die je niet uit de delen leest</strong>: 'de kat uit de boom kijken' gaat "
                  "niet over katten of bomen. '<strong>Dat is een storm in een glas water</strong>' "
                  "betekent <strong>dat er veel drukte gemaakt wordt om iets kleins</strong>."),
            ("p", "Daarom <strong>kan je een vaste uitdrukking niet gewoon woord voor woord naar een "
                  "andere taal overzetten</strong>: wie 'de kat uit de boom kijken' letterlijk vertaalt, "
                  "wordt niet begrepen. Begrijp je een uitdrukking niet, dan <strong>lees je de hele zin "
                  "en kijk je wat er logisch past</strong>: de omringende zinnen geven bijna altijd de "
                  "richting aan."),
        ]),
        dict(kop="Humor in taal", blokken=[
            ("p", "Middelen waarmee schrijvers humor maken: <strong>woordspel op twee betekenissen</strong> "
                  "en <strong>overdrijving tot het ongeloofwaardige</strong>, en verder ironie en een "
                  "onverwachte wending in de laatste woorden van een zin."),
            ("p", "Een <strong>woordspeling</strong> is <strong>een grap die op twee betekenissen van "
                  "hetzelfde woord berust</strong>. Veel krantenkoppen zijn er een, en daarom zijn ze "
                  "moeilijk te vertalen. Je <strong>mag een vaste uitdrukking aanpassen om een grap te "
                  "maken</strong>: de lezer herkent het origineel en ziet de draai."),
            ("p", "Een <strong>overdrijving</strong> als stijlmiddel is <strong>iets veel groter "
                  "voorstellen dan het is, om een effect te bereiken</strong>: 'ik heb duizend keer "
                  "gebeld.' Niemand neemt het letterlijk."),
            ("p", "<strong>Ironie</strong> is <strong>iets zeggen en het tegendeel bedoelen</strong>: "
                  "'wat een prachtig weer' in een stortregen. De toon moet het verschil maken, en daarom "
                  "<strong>kan ironie in een geschreven tekst verkeerd begrepen worden</strong>: de toon "
                  "valt weg, en mensen plaatsen er online soms een teken bij."),
            ("p", "<strong>Humor in taal werkt niet in elke cultuur op dezelfde manier</strong>: wat "
                  "ergens een gewone grap is, valt elders stil of komt scherp aan."),
        ]),
    ],
    onthoud=[
        "Synoniem (bijna gelijk), antoniem (tegengesteld), homoniem (gelijke vorm), hyperoniem (de groep).",
        "De zin beslist welke betekenis geldt; woorden verschuiven ook in de tijd.",
        "Metafoor zonder als, vergelijking met als, personificatie geeft iets menselijks.",
        "Een vaste uitdrukking lees je als geheel en vertaal je nooit woord voor woord.",
        "Woordspel, overdrijving en ironie; ironie valt zonder toon makkelijk verkeerd.",
    ],
)

# ───────────────────── 20. Schrijven en schriftelijke interactie
BUNDELS["schrijven-en-schriftelijke-interactie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Schrijven en schriftelijke interactie",
    onder="Het schrijfproces, de vaste tekstvormen, en schriftelijk antwoorden.",
    secties=[
        dict(kop="Eerst je doel en je publiek", blokken=[
            ("p", "Wat je als eerste bepaalt voor je begint te schrijven, is <strong>je doel en je "
                  "publiek</strong>. Wie gaat dit lezen en wat moet die daarna weten of doen? Alles volgt "
                  "daaruit. <strong>Je publiek bepalen</strong> hoort dus bij de voorbereiding, samen met "
                  "je doel."),
            ("p", "Keuzes die van je publiek afhangen: <strong>hoeveel voorkennis je "
                  "veronderstelt</strong>, en <strong>of je vaktermen uitlegt of gewoon gebruikt</strong>. "
                  "Dezelfde inhoud voor een vakgenoot of voor een buitenstaander is een andere tekst. Een "
                  "<strong>tekst hoort dan ook niet bij elke lezer op dezelfde manier over te "
                  "komen</strong>: daarom kies je één publiek. Schrijf je een instructie <strong>voor "
                  "iemand die het toestel nooit zag</strong>, dan <strong>benoem je elk onderdeel voor je "
                  "het gebruikt</strong>."),
        ]),
        dict(kop="Het schrijfproces", blokken=[
            ("p", "<strong>Schrijven is een proces dat je in stappen kan opdelen</strong>: "
                  "<strong>plannen</strong>, schrijven, <strong>herwerken</strong> en <strong>nalezen</strong>. "
                  "Wie ze door elkaar doet, blijft steken. Bij het schrijfproces horen dus "
                  "<strong>plannen voor je begint te schrijven</strong> en <strong>nalezen en herwerken "
                  "na de eerste versie</strong>."),
            ("p", "<strong>Herwerken</strong> is de stap waarin je de opbouw van je tekst nog wijzigt; "
                  "<strong>nalezen op spelling en herwerken zijn twee verschillende stappen</strong>, en "
                  "<strong>herwerken komt eerst</strong>. Een alinea die sneuvelt, hoef je niet gespeld "
                  "te hebben. <strong>Een goede schrijver maakt in zijn eerste versie wel fouten</strong>: "
                  "een eerste versie mag rommelig zijn, het nalezen is er juist voor. Twee dingen die "
                  "kloppen: <strong>plannen kost tijd en levert tijd op bij het schrijven</strong>, en "
                  "<strong>een tekst wordt beter door hem opnieuw op te bouwen</strong>."),
            ("p", "Moet je een <strong>verslag schrijven van een gesprek met een klant</strong>, dan doe "
                  "je eerst dit: <strong>je zet je notities in de orde van wat besproken werd</strong>. "
                  "Van losse notities naar een lijn, dat is plannen."),
            ("p", "Bij het nalezen helpt het om je tekst <strong>luidop na te lezen</strong>, want "
                  "<strong>je hoort waar een zin niet loopt</strong>. En een <strong>tekst door iemand "
                  "anders laten nalezen levert méér op dan hem zelf nog eens lezen</strong>: je leest in "
                  "je eigen tekst wat je bedoelde, een ander leest wat er staat. Is je tekst <strong>te "
                  "lang geworden</strong>, dan <strong>schrap je wat de lezer niet nodig heeft voor je "
                  "doel</strong>: schrappen is kiezen."),
        ]),
        dict(kop="De vaste tekstvormen", blokken=[
            ("p", tabel(["Vorm", "Wat erin hoort"], [
                ["Het <strong>verslag</strong>", "wat beslist werd en wie wat doet"],
                ["De <strong>sollicitatiebrief</strong>", "waarom je deze job wil en wat je ervoor meebrengt"],
                ["De <strong>instructie</strong>", "stappen in de juiste orde, één handeling per stap, in de gebiedende wijs"],
                ["Het <strong>opiniestuk</strong>", "een standpunt dat met argumenten verdedigd wordt"],
                ["De <strong>zakelijke mail</strong>", "een onderwerpregel, een duidelijke vraag en een deadline"],
                ["De <strong>klacht</strong>", "de feiten, de data en wat je verwacht"],
            ])),
            ("p", "Een <strong>verslag</strong> dient om later terug te lezen wat er is afgesproken. Het "
                  "<strong>verschil met een opiniestuk</strong>: <strong>een verslag geeft weer wat er "
                  "gebeurde, een opiniestuk wat je vindt</strong>. Een verslag met een mening erin "
                  "verborgen is niet meer bruikbaar als verslag."),
            ("p", "In een <strong>sollicitatiebrief</strong> hoort te staan <strong>wat jij voor de "
                  "werkgever kan doen</strong>, niet enkel wat jij wil: je cv geeft de lijst, de brief "
                  "legt het verband met deze ene vacature."),
            ("p", "Een goede <strong>instructie</strong> heeft twee kenmerken: <strong>de stappen staan "
                  "in de orde waarin ze uitgevoerd worden</strong>, en <strong>elke stap bevat één "
                  "handeling, in de gebiedende wijs</strong>. Wie een instructie leest, staat met zijn "
                  "handen aan het werk."),
            ("p", "Een <strong>opiniestuk</strong> is <strong>een tekst die een standpunt verdedigt met "
                  "argumenten</strong>, ook wel een <strong>betoog</strong>. In het <strong>slot</strong> "
                  "zet je <strong>je conclusie, en wat er volgens jou moet gebeuren</strong>; nieuwe "
                  "argumenten horen daar niet meer."),
            ("p", "Bij een <strong>klacht</strong> over een product dat niet opgelost wordt, "
                  "<strong>schrijf je een klacht met de feiten, de data en wat je verwacht</strong>. Een "
                  "<strong>klacht wint kracht door de feiten met data en bedragen te noemen</strong>, "
                  "want dan is ze te controleren. Ze hoort je gevoel <strong>niet</strong> zo scherp "
                  "mogelijk uit te drukken: noem één keer wat het je kostte en vraag dan wat je verwacht."),
            ("p", "Over de opbouw van een langere tekst: <strong>één gedachte per alinea, met de "
                  "kerngedachte vooraan</strong>. De functie van een <strong>inleiding</strong> is "
                  "<strong>de lezer binnenhalen en zeggen waarover de tekst gaat</strong>. Middelen die "
                  "een tekst <strong>beter leesbaar</strong> maken: <strong>tussenkoppen boven de delen "
                  "van de tekst</strong>, en <strong>korte alinea's met één gedachte per alinea</strong>."),
            ("p", "Schrijf je dezelfde boodschap voor een <strong>mail en voor een affiche</strong>, dan "
                  "veranderen <strong>de lengte, de vorm en de toon van de boodschap</strong>: een "
                  "affiche wordt in drie seconden gelezen. Een <strong>zakelijke mail hoort niet minstens "
                  "een halve bladzijde lang te zijn</strong>: drie regels kunnen genoeg zijn."),
        ]),
        dict(kop="Schriftelijke interactie", blokken=[
            ("p", "In de <strong>onderwerpregel</strong> van een mail hoort <strong>in enkele woorden "
                  "waarover de mail gaat</strong>: de ontvanger moet in zijn lijst meteen zien of hij nu "
                  "moet openen. Schrijf je een mail met een vraag en een <strong>deadline</strong>, dan "
                  "zet je die <strong>duidelijk apart, zodat ze niet in de tekst verdwijnt</strong>."),
            ("p", "Je maakt een zakelijke mail makkelijk te beantwoorden door <strong>je vragen apart en "
                  "genummerd te stellen</strong>: genummerde vragen krijgen genummerde antwoorden, een "
                  "lange alinea krijgt er één. Een <strong>mail aan een onbekende begint het best "
                  "formeel</strong>: je kan altijd informeler worden."),
            ("p", "Een <strong>schriftelijk antwoord hoort elke vraag van de ander te behandelen</strong>: "
                  "wie één vraag overslaat, krijgt die gewoon opnieuw. Ken je het antwoord op één van drie "
                  "vragen, dan <strong>antwoord je op die ene en zeg je wanneer de rest volgt</strong>. "
                  "Reageer je schriftelijk op iemand <strong>met wie je niet akkoord gaat</strong>, dan "
                  "<strong>benoem je waar je het oneens bent en zeg je waarom</strong>: de inhoud scherp, "
                  "de toon rustig. En een <strong>mail die geen antwoord vraagt, hoort dat ook te "
                  "zeggen</strong>: één regel spaart de ander werk."),
        ]),
    ],
    onthoud=[
        "Eerst doel en publiek; die bepalen voorkennis, vaktermen, lengte en toon.",
        "Plannen, schrijven, herwerken, nalezen. Herwerken komt voor de spelling.",
        "Verslag zegt wat gebeurde, opiniestuk wat je vindt; een instructie één handeling per stap.",
        "Een klacht: feiten, data, bedragen en wat je verwacht. Rustig in de toon.",
        "Een mail: onderwerpregel, genummerde vragen, de deadline apart, en elke vraag beantwoord.",
    ],
)

# ───────────────────── 21. Spreken en gesprekken voeren
BUNDELS["spreken-en-gesprekken-voeren-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Spreken en gesprekken voeren",
    onder="Een presentatie houden, uitleg geven, en een gesprek met een doel voeren.",
    secties=[
        dict(kop="Een presentatie voorbereiden", blokken=[
            ("p", "Wat je het eerst doet bij de voorbereiding van een presentatie: <strong>je bepaalt wat "
                  "je publiek achteraf moet weten of doen</strong>. Dat is <strong>je doel</strong>, en "
                  "alles in je presentatie staat in dienst daarvan. Zonder dat ene doel wordt een "
                  "presentatie een opsomming van alles wat je vond."),
            ("p", "Je <strong>begint</strong> het best <strong>met iets dat de aandacht vangt en je "
                  "onderwerp aankondigt</strong>: een vraag, een cijfer of een kort voorval. De eerste "
                  "dertig seconden beslissen veel. Je <strong>sluit af met je kernboodschap en wat je van "
                  "het publiek verwacht</strong>: het laatste wat je zegt, blijft hangen."),
            ("p", "Middelen die je publiek helpen je <strong>structuur</strong> te volgen: <strong>vooraf "
                  "zeggen hoeveel punten je behandelt</strong>, en <strong>bij elk nieuw deel benoemen "
                  "waar je nu bent</strong>. Een luisteraar kan niet terugbladeren. Een <strong>korte "
                  "samenvatting midden in een lange uiteenzetting</strong> helpt ook: <strong>wie de "
                  "draad kwijt was, kan weer instappen</strong>."),
            ("p", "Een <strong>presentatie oefenen met een klok erbij verandert je tekst meestal "
                  "nog</strong>: bijna iedereen heeft te veel. Heb je <strong>tien minuten en vijftien "
                  "minuten stof</strong>, dan <strong>schrap je tot je kernboodschap overblijft</strong>. "
                  "Wat je sneller zegt, komt niet aan. Tegen <strong>zenuwen</strong> helpt: <strong>je "
                  "oefent je eerste zinnen tot die vastzitten</strong>."),
            ("p", "Een <strong>presentatie voorlezen werkt minder goed dan ze met steekwoorden "
                  "brengen</strong>: wie voorleest, kijkt niet. <strong>Oogcontact met je publiek maakt "
                  "je verhaal overtuigender</strong>; verdeel je blik over de zaal. En een "
                  "<strong>goede spreker spreekt niet zo snel als hij kan</strong>: een rustig tempo met "
                  "pauzes geeft het publiek tijd. Een <strong>spreker mag wel stil vallen</strong>: een "
                  "stilte voor een belangrijk punt werkt juist."),
            ("p", "Een <strong>presentatie met dia's is niet altijd beter dan één zonder</strong>: dia's "
                  "helpen als ze iets tonen dat je niet kan zeggen, anders leiden ze af. Merk je dat het "
                  "<strong>publiek afhaakt</strong>, dan <strong>stel je een vraag of kondig je je "
                  "volgende punt aan</strong>; volume helpt niet. Een vraag uit het publiek die je niet "
                  "kan beantwoorden, behandel je zo: <strong>je zegt dat je het niet weet en hoe je het "
                  "zal nazoeken</strong>."),
        ]),
        dict(kop="Uitleg en instructie geven", blokken=[
            ("p", "Goede mondelinge uitleg heeft twee kenmerken: <strong>je gaat van wat de ander kent "
                  "naar wat nieuw is</strong>, en <strong>je laat de ander navertellen wat hij begrepen "
                  "heeft</strong>. Pas als de ander het kan navertellen, weet je dat het overkwam."),
            ("p", "Een <strong>voorbeeld</strong> werkt goed <strong>omdat de ander het nieuwe aan iets "
                  "bekends kan ophangen</strong>: eerst het voorbeeld, dan de regel. Geef je iemand "
                  "<strong>telefonisch een instructie</strong>, dan <strong>laat je op het einde de ander "
                  "de stappen terug zeggen</strong>: op 'is het duidelijk?' antwoordt bijna iedereen ja."),
        ]),
        dict(kop="Een gesprek voeren", blokken=[
            ("p", "<strong>Beurten nemen</strong> betekent <strong>op het juiste moment spreken en de "
                  "ander laten uitspreken</strong>. Een vlot gesprek is een reeks beurten; wie altijd "
                  "neemt of altijd wacht, verstoort het. Vallen <strong>twee mensen elkaar in de "
                  "rede</strong>, dan <strong>vraag je om één voor één te spreken</strong>."),
            ("p", "Je laat merken dat je luistert door <strong>de ander aan te kijken en af en toe te "
                  "knikken</strong>, en door <strong>samen te vatten wat de ander zei voor je "
                  "antwoordt</strong>. <strong>Samenvatten</strong> of <strong>parafraseren</strong> is "
                  "<strong>het kort weergeven van wat de ander zei, in je eigen woorden</strong>: het "
                  "bewijst dat je geluisterd hebt en het haalt misverstanden eruit. Heb je iets niet "
                  "begrepen, dan <strong>vraag je het na met je eigen woorden erbij</strong>: 'bedoel je "
                  "dat…?'"),
            ("p", "Het <strong>verschil tussen een open en een gesloten vraag</strong>: <strong>een open "
                  "vraag vraagt een verhaal, een gesloten vraag een ja of een nee</strong>. Een "
                  "<strong>gesloten vraag is soms precies wat je nodig hebt</strong>, bijvoorbeeld om een "
                  "afspraak vast te leggen. Wil je de ander verder laten spreken, dan stel je "
                  "<strong>open vragen die met hoe of waarom beginnen</strong> en <strong>vragen die "
                  "doorgaan op wat de ander net zei</strong>."),
            ("p", "<strong>In een gesprek bereikt niet wie het meest spreekt het meest</strong>: wie de "
                  "goede vragen stelt en samenvat, stuurt het gesprek met minder woorden. <strong>Je kan "
                  "een gesprek sturen zonder het grootste deel van de tijd te spreken.</strong>"),
            ("p", "Bel je <strong>om een afspraak te maken</strong>, dan zeg je in je eerste zinnen "
                  "<strong>wie je bent en waarvoor je belt</strong>. Het doel van <strong>overleg</strong> "
                  "is <strong>samen tot een beslissing of een afspraak komen</strong>; een overleg zonder "
                  "afspraak op het einde is een gesprek geweest. Je maakt een afspraak concreet door "
                  "<strong>te noemen wie wat doet en tegen wanneer</strong>: zonder naam en datum is een "
                  "afspraak een intentie."),
            ("p", "<strong>Bemiddel</strong> je tussen twee mensen die ruzie hebben, dan <strong>laat je "
                  "eerst elk zijn kant vertellen zonder onderbreking</strong>: wie nog niet gehoord is, "
                  "luistert niet. Middelen die een <strong>moeilijk gesprek</strong> op gang houden: "
                  "<strong>samenvatten wat de ander zei voor je reageert</strong>, en <strong>benoemen "
                  "waar jullie het wel over eens zijn</strong>. In een discussie <strong>hoort je toon "
                  "niet mee te verharden als de ander scherper wordt</strong>: scherp mag de inhoud zijn, "
                  "niet de toon."),
            ("p", "Een <strong>presentatie houden en een gesprek voeren vragen niet hetzelfde van een "
                  "spreker</strong>: in een presentatie stuur jij alles, in een gesprek moet je ook ruimte "
                  "laten en volgen."),
            ("p", "Twee uitspraken die kloppen: <strong>wie zijn doel kent, kiest makkelijker wat hij "
                  "weglaat</strong>, en <strong>luisteren is een even actieve vaardigheid als "
                  "spreken</strong>. Meer inhoud maakt een presentatie zwakker; de keuze maakt ze sterk. "
                  "En een <strong>spreker die zijn publiek kent, maakt andere keuzes dan een spreker die "
                  "het niet kent</strong>: voorkennis, voorbeelden en vaktermen hangen volledig af van "
                  "wie er zit."),
        ]),
    ],
    onthoud=[
        "Eerst je doel: wat moet je publiek achteraf weten of doen?",
        "Open met iets dat de aandacht vangt, sluit met je kernboodschap, en zeg onderweg waar je bent.",
        "Steekwoorden in plaats van voorlezen, oogcontact, een rustig tempo en pauzes.",
        "Beurten nemen, samenvatten en navragen; open vragen voor een verhaal, gesloten om vast te leggen.",
        "Overleg eindigt in een afspraak met een naam en een datum; bij bemiddeling eerst laten vertellen.",
    ],
)

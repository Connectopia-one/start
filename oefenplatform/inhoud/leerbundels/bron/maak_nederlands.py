# -*- coding: utf-8 -*-
"""De leerbundels voor Nederlands, categorie Start (5de en 6de leerjaar)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel
tabel = bundel.tabel

VAK = "Nederlands"
BUNDELS = {}

BUNDELS["lezen"] = dict(
    vak=VAK, titel="Lezen",
    onder="Een tekst begrijpen, de hoofdgedachte vinden en niet verdrinken in de details.",
    secties=[
        dict(kop="Lees in drie rondes", blokken=[
            ("p", "Een tekst één keer van begin tot eind lezen werkt zelden. Wie goed leest, gaat er meerdere keren doorheen, telkens met een andere bedoeling."),
            ("fig", svg.stappen(["Kijk rond|titel, tussentitels,|afbeeldingen",
                                 "Lees door|van begin tot eind,|zonder te stoppen",
                                 "Lees gericht|zoek het antwoord|op je vraag"]),
             "De eerste ronde duurt tien seconden en scheelt achteraf het meeste tijd."),
            ("p", "Weet je vooraf wat je zoekt, dan hoef je de tekst niet helemaal te onthouden. Lees dus eerst de vragen, en pas daarna de tekst."),
        ]),
        dict(kop="Hoe een tekst in elkaar zit", blokken=[
            ("fig", svg.tekstopbouw([
                ("Titel", "waarover gaat het", 1),
                ("Inleiding", "het onderwerp, en waarom het je aanbelangt", 1.3),
                ("Middenstuk", "één gedachte per alinea", 2.2),
                ("Slot", "de conclusie of de samenvatting", 1.2),
            ]), "Elke alinea heeft één kerngedachte, en die staat meestal in de eerste of de laatste zin."),
            ("p", "Zoek je de <strong>hoofdgedachte</strong> van een hele tekst, kijk dan naar de titel, de inleiding en het slot samen. Die drie zeggen het bijna altijd."),
        ]),
        dict(kop="Signaalwoorden", blokken=[
            ("p", "Sommige woorden verklappen wat er komt. Herken je ze, dan lees je sneller en juister."),
            ("fig", tabel(["Signaalwoord", "Wat er komt"], [
                ["want, omdat, daardoor", "een reden of een gevolg"],
                ["maar, toch, hoewel, ondanks", "een tegenstelling"],
                ["eerst, daarna, ten slotte", "een volgorde"],
                ["bijvoorbeeld, zoals", "een voorbeeld"],
                ["kortom, dus, samengevat", "een conclusie"],
            ]), "Zie je kortom staan, dan komt de kern van de tekst eraan."),
        ]),
        dict(kop="Soorten teksten", blokken=[
            ("fig", tabel(["Soort", "Waarvoor dient hij", "Voorbeeld"], [
                ["informatief", "iets uitleggen", "een lesbladzijde, een artikel"],
                ["verhalend", "iets vertellen", "een boek, een kortverhaal"],
                ["instructief", "iets laten doen", "een recept, een handleiding"],
                ["overtuigend", "je van iets overtuigen", "reclame, een opiniestuk"],
            ]), "Weet je de soort, dan weet je ook wat je moet zoeken."),
            ("weetje", "Bij een overtuigende tekst is de vraag altijd: <em>wie</em> zegt dit, en wat heeft die eraan? Reclame vertelt zelden het volledige verhaal."),
        ]),
        dict(kop="Zoekend lezen", blokken=[
            ("p", "Soms moet je een tekst niet begrijpen maar doorzoeken: je wil één gegeven, bijvoorbeeld het telefoonnummer van de school in een brief. Dan lees je niet, dan <strong>scan</strong> je: je laat je ogen over de tekst gaan tot je de vorm ziet die je zoekt, hier een rij cijfers."),
            ("p", "Weet je op voorhand wat je zoekt, dan gaat dat razendsnel. Zoek je een datum, kijk dan naar getallen en maandnamen. Zoek je een naam, kijk dan naar de hoofdletters."),
            ("fig", tabel(["Waar je het zoekt", "Wat het doet"], [
                ["de inhoudstafel", "vooraan of achteraan: welk hoofdstuk staat waar"],
                ["het register", "achteraan: op welke bladzijde staat dit woord"],
                ["een woordenboek", "de betekenis en de spelling van een woord"],
                ["een atlas", "kaarten"],
                ["een encyclopedie of een betrouwbare website", "uitleg over een onderwerp"],
            ]), "Weten wáár je iets zoekt, scheelt meer tijd dan snel lezen."),
        ]),
        dict(kop="Feit, mening en betrouwbaarheid", blokken=[
            ("p", "Een <strong>feit</strong> kan je nagaan: het klopt of het klopt niet. Een <strong>mening</strong> is wat iemand ervan vindt, en daar kan je het mee oneens zijn."),
            ("kader", "<p style='margin:0 0 4px'><strong>Feit</strong> — België heeft drie landstalen. Dat kan je opzoeken.</p>"
                      "<p style='margin:0'><strong>Mening</strong> — Frans is de mooiste taal. Daar kan je niets aan nameten.</p>"),
            ("p", "Bij alles wat je leest, zeker op het internet, horen drie vragen: <em>wie</em> schrijft dit, <em>wanneer</em> is het geschreven, en <em>waarom</em>? Een tekst van een ziekenhuis over gezondheid is betrouwbaarder dan een folder van iemand die je iets wil verkopen. Een tekst van tien jaar geleden kan achterhaald zijn."),
            ("weetje", "In een reclametekst is alles wat er staat misschien waar, en toch krijg je niet het hele verhaal. Wat ontbreekt, is even belangrijk als wat er staat."),
        ]),
        dict(kop="Als woorden iets anders betekenen", blokken=[
            ("p", "Niet alles wat je leest, is letterlijk bedoeld. <strong>Het regende dat het goot</strong> betekent dat het heel hard regende, niet dat er een goot in de lucht hing. Zulke vaste beeldende zinnetjes heten uitdrukkingen."),
            ("fig", tabel(["Uitdrukking", "Wat er bedoeld wordt"], [
                ["het regende dat het goot", "het regende heel hard"],
                ["door het dolle heen zijn", "uitgelaten blij zijn"],
                ["de kat uit de boom kijken", "eerst afwachten hoe de zaken staan"],
                ["een appeltje voor de dorst", "iets opzijzetten voor later"],
            ]), "Ken je de uitdrukking niet, lees dan verder: de rest van de tekst legt ze meestal uit."),
            ("p", "Soms bedoelt iemand zelfs het omgekeerde van wat hij zegt. <em>\"Wat een schitterend idee\", zei hij, terwijl hij met zijn ogen rolde.</em> Zijn woorden zeggen ja, zijn gebaar zegt nee. Dat heet <strong>ironie</strong>. Let dus altijd op wat er rond de woorden staat."),
        ]),
        dict(kop="Een woord dat je niet kent", blokken=[
            ("p", "Sla niet meteen iets op. Lees eerst de zin ervoor en erna: vaak staat de betekenis er gewoon bij, of kan je ze raden uit de rest."),
            ("p", "Helpt dat niet, kijk dan of je stukken van het woord herkent. In <em>onbereikbaar</em> zitten <em>on</em> (niet), <em>bereiken</em> en <em>baar</em> (kan): iets dat je niet kan bereiken."),
        ]),
    ],
    onthoud=[
        "Kijk eerst rond in de tekst voor je begint te lezen.",
        "Lees de vragen voor je de tekst leest.",
        "Elke alinea heeft één kerngedachte.",
        "Titel, inleiding en slot geven samen de hoofdgedachte.",
        "Signaalwoorden verklappen wat er komt.",
        "Raad een onbekend woord eerst uit de zin eromheen.",
        "Zoek je één gegeven? Dan scan je, je leest niet.",
        "Een feit kan je nagaan, een mening niet.",
        "Vraag bij elke tekst: wie, wanneer en waarom.",
        "Een uitdrukking bedoelt iets anders dan wat er staat.",
    ])

BUNDELS["schrijven"] = dict(
    vak=VAK, titel="Schrijven",
    onder="Van een leeg blad naar een tekst die iemand anders begrijpt.",
    secties=[
        dict(kop="Schrijven in vier stappen", blokken=[
            ("fig", svg.stappen(["Denk|voor wie schrijf je?|wat wil je zeggen?",
                                 "Orden|zet je ideeën|in een volgorde",
                                 "Schrijf|in één ruk,|zonder te schaven",
                                 "Herlees|nu pas verbeter je"]),
             "Schrijven en verbeteren tegelijk doen is het moeilijkste wat er is. Doe het apart."),
            ("p", "Wie vastloopt, is meestal aan het schrijven en verbeteren tegelijk. Schrijf eerst alles op, hoe lelijk ook. Verbeteren komt daarna."),
        ]),
        dict(kop="De opbouw van je tekst", blokken=[
            ("fig", svg.tekstopbouw([
                ("Inleiding", "waarover gaat het, en waarom", 1.2),
                ("Midden", "je punten, één per alinea", 2.2),
                ("Slot", "wat je onthouden wil zien", 1.2),
            ]), "Nieuwe gedachte? Nieuwe alinea. Dat is de hele regel."),
            ("p", "Gebruik verbindingswoorden om je lezer mee te nemen: <em>eerst, daarna, bovendien, toch, ten slotte</em>."),
        ]),
        dict(kop="Leestekens", blokken=[
            ("fig", tabel(["Teken", "Wanneer"], [
                ["punt .", "einde van een zin"],
                ["komma ,", "een korte pauze, of bij een opsomming"],
                ["vraagteken ?", "einde van een vraag"],
                ["uitroepteken !", "bij een uitroep — spaarzaam gebruiken"],
                ["dubbelpunt :", "er komt een opsomming of een uitleg"],
                ["aanhalingstekens „ ”", "iemand zegt iets letterlijk"],
            ]), "Een hoofdletter na een punt, en ook bij namen, landen en talen."),
        ]),
        dict(kop="Werkwoorden schrijven", blokken=[
            ("p", "De meeste schrijffouten zitten in de werkwoorden. Twee regels lossen er al heel veel op."),
            ("kader", "<p style='margin:0 0 5px'><strong>Tegenwoordige tijd.</strong> Ik: de stam. Jij, hij, zij, het: stam + t. "
                      "Vraag je iets met <em>jij</em> erachter, dan valt die t weg: <em>Loop jij mee?</em></p>"
                      "<p style='margin:0'><strong>Verleden tijd.</strong> Eindigt de stam op een letter uit <strong>'t kofschip</strong> "
                      "(t, k, f, s, ch, p — en x), dan wordt het <strong>-te</strong>. Anders <strong>-de</strong>. "
                      "Werken → werkte. Horen → hoorde.</p>"),
            ("kader", "<p style='margin:0 0 5px'><strong>Toekomende tijd.</strong> Die maak je met <em>zullen</em> of <em>gaan</em> plus een werkwoord: "
                      "<em>ik zal komen</em>, <em>wij gaan zwemmen</em>.</p>"
                      "<p style='margin:0'><strong>Voltooid deelwoord.</strong> Meestal <em>ge-</em> vooraan: gewerkt, gehoord, gezien. "
                      "Eindigt de stam al op een d, dan komt er géén t meer bij: antwoorden → <strong>geantwoord</strong>, niet geantwoordt.</p>"),
            ("weetje", "Twijfel je tussen -d of -t op het einde? Zet het woord in het meervoud. <em>Hij wordt</em> → <em>zij worden</em>, dus met een d."),
        ]),
        dict(kop="Meervoud maken", blokken=[
            ("p", "De meeste woorden krijgen <strong>-en</strong> of <strong>-s</strong>. Welke van de twee, dat hoor je meestal: zeg het luidop en neem wat vlot klinkt."),
            ("fig", tabel(["Soort", "Voorbeeld"], [
                ["meestal -en", "boek → boeken, stoel → stoelen"],
                ["soms -s", "tafel → tafels, meisje → meisjes"],
                ["-eren, bij een handvol woorden", "kind → kinderen, ei → eieren, blad → bladeren"],
                ["de klinker verandert", "stad → steden, schip → schepen"],
                ["open lettergreep: één medeklinker", "raam → ramen, vuur → vuren"],
                ["gesloten lettergreep: verdubbelen", "pot → potten, bal → ballen"],
            ]), "De woorden op -eren zijn er maar een paar; die leer je uit het hoofd."),
        ]),
        dict(kop="Een brief of een e-mail", blokken=[
            ("p", "Wie de lezer is, bepaalt hoe je schrijft. Aan een vriend schrijf je los; aan iemand die je niet kent, of aan je leerkracht, schrijf je verzorgd. Dat is geen stijfheid, dat is rekening houden met wie het leest."),
            ("fig", tabel(["Onderdeel", "Aan iemand die je niet kent"], [
                ["aanspreking", "Geachte mevrouw, Geachte heer"],
                ["als je de naam kent", "Beste mevrouw Jansen"],
                ["de eerste zin", "zeg meteen waarover het gaat"],
                ["de aanspreekvorm", "u, en volledige zinnen"],
                ["afsluiting", "Met vriendelijke groeten, plus je naam"],
            ]), "Bij een e-mail hoort ook een onderwerpregel die in drie woorden zegt waarover het gaat."),
            ("p", "Afkortingen als <em>idd</em> of <em>mss</em>, emoji en zinnen zonder hoofdletter horen thuis in een bericht aan een vriend. Twijfel je? Schrijf dan verzorgd: te beleefd valt niemand tegen."),
        ]),
        dict(kop="Herlezen", blokken=[
            ("p", "Lees je tekst hardop. Struikel je over een zin, dan struikelt je lezer er ook over. Dat is de snelste test die er is."),
            ("fig", tabel(["Kijk na", "Vraag jezelf af"], [
                ["de opbouw", "staat alles in een logische volgorde?"],
                ["de zinnen", "zijn er zinnen die te lang zijn?"],
                ["de werkwoorden", "klopt elke d en t?"],
                ["de hoofdletters", "begint elke zin ermee?"],
                ["de lezer", "begrijpt iemand die er niets van weet dit?"],
            ]), None),
        ]),
    ],
    onthoud=[
        "Schrijven en verbeteren zijn twee aparte stappen.",
        "Nieuwe gedachte, nieuwe alinea.",
        "Tegenwoordige tijd: ik = stam, jij/hij/zij = stam + t.",
        "'t kofschip beslist tussen -te en -de.",
        "Twijfel over d of t? Zet het in het meervoud.",
        "Lees je tekst hardop na.",
        "Voltooid deelwoord: na een d komt er geen t meer bij.",
        "Toekomende tijd maak je met zullen of gaan.",
        "Schrijf je aan iemand die je niet kent, gebruik dan u.",
    ])

BUNDELS["spreken-en-luisteren"] = dict(
    vak=VAK, titel="Spreken en luisteren",
    onder="Iets vertellen zodat anderen het volgen, en luisteren zodat je het onthoudt.",
    secties=[
        dict(kop="Een spreekbeurt opbouwen", blokken=[
            ("fig", svg.tekstopbouw([
                ("Begin", "zeg waarover je het gaat hebben, en waarom het boeiend is", 1.4),
                ("Midden", "drie punten, niet meer", 1.8),
                ("Einde", "herhaal je belangrijkste punt en bedank je publiek", 1.4),
            ]), "Drie punten onthoudt je publiek. Zeven punten onthoudt niemand, jezelf inbegrepen."),
            ("p", "Schrijf je spreekbeurt niet woord voor woord uit. Maak een kaartje met steekwoorden: dan kijk je naar je publiek in plaats van naar je blad."),
        ]),
        dict(kop="Hoe je klinkt", blokken=[
            ("fig", tabel(["Doe dit", "Waarom"], [
                ["spreek trager dan je denkt", "van de zenuwen ga je vanzelf te snel"],
                ["las stiltes in", "een pauze geeft je publiek tijd om te volgen"],
                ["kijk rond, maak oogcontact", "dan luistert iedereen mee"],
                ["sta stil", "heen en weer lopen leidt af"],
                ["spreek luid genoeg", "vraag vooraf of ze je achteraan horen"],
                ["laat je stem dalen op het einde", "zo hoort men dat je zin af is"],
            ]), None),
            ("p", "Werk je met een scherm erbij, zet dan <strong>steekwoorden en beelden</strong> op je dia's, geen volledige zinnen. Staat er een hele tekst op, dan leest je publiek mee in plaats van naar jou te luisteren, en jij staat voor te lezen wat zij al gelezen hebben."),
            ("weetje", "Zenuwachtig zijn gaat niet weg door te oefenen, maar je wordt er wel beter in ondanks de zenuwen. Ook ervaren sprekers hebben hartkloppingen."),
        ]),
        dict(kop="Goed luisteren", blokken=[
            ("p", "Luisteren is niet hetzelfde als stil zijn. Wie goed luistert, is actief bezig."),
            ("fig", svg.stappen(["Kijk|naar wie spreekt", "Vang|de kern, niet elk woord", "Vraag|als je iets mist"]),
             "Noteer enkel steekwoorden. Alles opschrijven betekent dat je niet meer luistert."),
        ]),
        dict(kop="Een gesprek voeren", blokken=[
            ("fig", tabel(["In een gesprek", "Hoe dat klinkt"], [
                ["laat uitspreken", "wacht tot de ander klaar is"],
                ["vraag door", "Hoe bedoel je dat precies?"],
                ["vat samen in je eigen woorden", "Dus als ik het goed begrijp…"],
                ["geef je mening beleefd", "Ik zie dat anders, want…"],
                ["geef toe als je iets niet weet", "Dat weet ik niet, ik zoek het op."],
            ]), "Doorvragen is het verschil tussen praten en een gesprek voeren."),
        ]),
        dict(kop="Een discussie of een debat", blokken=[
            ("p", "In een <strong>debat</strong> verdedigen twee kanten een verschillende mening. Je wint daar niet door harder te praten, maar met <strong>argumenten</strong>: redenen waarom jouw standpunt klopt."),
            ("fig", tabel(["Wat je zegt", "Hoe dat klinkt"], [
                ["je standpunt", "Ik vind dat we…"],
                ["je argument", "…want daardoor…"],
                ["een voorbeeld", "Vorige week zag je dat: …"],
                ["oneens zijn", "Ik zie dat anders, want…"],
                ["toegeven", "Daar heb je gelijk in, maar…"],
            ]), "Van mening verschillen mag altijd. Iemand uitlachen of onderbreken niet."),
            ("p", "Een mening zonder argument is maar een uitroep. Zeg dus nooit alleen <em>dat vind ik stom</em>, maar altijd waaróm."),
        ]),
        dict(kop="Gesprekken in het echt", blokken=[
            ("p", "Een <strong>open vraag</strong> houdt een gesprek op gang, een gesloten vraag stopt het. <em>Hoe was het op kamp?</em> vraagt om een verhaal; <em>Was het leuk op kamp?</em> kan met ja beantwoord worden en dan is het stil."),
            ("fig", tabel(["Situatie", "Wat helpt"], [
                ["een telefoongesprek", "zeg eerst wie je bent, de ander ziet je niet"],
                ["je hebt iets niet verstaan", "vraag het gerust opnieuw, dat helpt iedereen"],
                ["iemand vertelt iets verdrietigs", "zeg dat je het erg vindt en laat de ander vertellen"],
                ["iemand zei nog niets in de groep", "vraag wat hij ervan denkt"],
                ["je wil weten of je het goed begrepen hebt", "vat samen: dus als ik het goed begrijp…"],
            ]), "Bij iemand die verdriet heeft, helpt meeleven meer dan meteen een oplossing aanreiken."),
        ]),
        dict(kop="Formeel en informeel", blokken=[
            ("p", "Tegen een vriend praat je anders dan tegen een directeur. Dat is geen onbeleefdheid, dat is aanvoelen waar je bent."),
            ("p", "Bij iemand die je niet kent: <strong>u</strong>, volledige zinnen, geen afkortingen. Bij vrienden mag alles losser. Twijfel je, begin dan formeel; naar beneden bijstellen is makkelijker dan omgekeerd."),
        ]),
    ],
    onthoud=[
        "Drie punten in een spreekbeurt, niet meer.",
        "Werk met steekwoorden, niet met een uitgeschreven tekst.",
        "Spreek trager dan je denkt en las stiltes in.",
        "Luisteren is actief: vang de kern en vraag door.",
        "Laat de ander uitspreken.",
        "Twijfel je over u of je? Begin formeel.",
        "Een mening zonder argument is maar een uitroep.",
        "Open vragen houden een gesprek op gang.",
        "Op een dia horen steekwoorden, geen zinnen.",
    ])

BUNDELS["taalsysteem-en-taalgebruik"] = dict(
    vak=VAK, titel="Taalsysteem en taalgebruik",
    onder="Woordsoorten, zinsdelen en de spellingregels die je het vaakst nodig hebt.",
    secties=[
        dict(kop="Woordsoorten", blokken=[
            ("fig", tabel(["Soort", "Wat het doet", "Voorbeeld"], [
                ["zelfstandig naamwoord", "noemt een ding, dier of persoon", "hond, school, Lien"],
                ["werkwoord", "zegt wat er gebeurt", "lopen, zijn, denken"],
                ["bijvoeglijk naamwoord", "zegt hoe iets is", "groot, rood, stil"],
                ["lidwoord", "staat voor een naamwoord", "de, het, een"],
                ["voornaamwoord", "vervangt een naamwoord", "ik, jij, hem, dit"],
                ["voorzetsel", "zegt waar of wanneer", "op, in, onder, na"],
                ["bijwoord", "zegt iets over het werkwoord", "snel, gisteren, graag"],
            ]), "Een goede test voor een werkwoord: kan je er ik, jij of wij voor zetten?"),
            ("p", "Het verschil tussen een bijvoeglijk naamwoord en een bijwoord zit in waar het iets over zegt. In <em>een snelle auto</em> zegt <em>snelle</em> iets over de auto: bijvoeglijk naamwoord. In <em>hij loopt snel</em> zegt <em>snel</em> iets over het lopen: bijwoord."),
        ]),
        dict(kop="De zin uit elkaar halen", blokken=[
            ("fig", svg.zinsdelen([
                ("De grote hond", "onderwerp", "#2f5d50"),
                ("blaft", "persoonsvorm", "#c17f2b"),
                ("in de tuin", "bepaling", "#3b6ea5"),
            ], 470), "Wie of wat blaft? De grote hond. Dat is het onderwerp."),
            ("kader", "<p style='margin:0 0 4px'><strong>De persoonsvorm vinden:</strong> maak van de zin een vraag. "
                      "Het werkwoord dat dan vooraan springt, is de persoonsvorm. <em>Blaft de grote hond in de tuin?</em></p>"
                      "<p style='margin:0'><strong>Het onderwerp vinden:</strong> vraag <em>wie of wat</em> + de persoonsvorm.</p>"),
            ("p", "Het <strong>gezegde</strong> is wat er over het onderwerp gezegd wordt: het werkwoordelijke deel van de zin. In <em>Mats leest een boek</em> is <em>Mats</em> het onderwerp en <em>leest</em> het gezegde."),
            ("p", "Het <strong>lijdend voorwerp</strong> vind je met de vraag <em>wie of wat</em> + gezegde + onderwerp. Wat leest Mats? Een boek. Dat is dus het lijdend voorwerp."),
            ("fig", tabel(["Soort zin", "Waaraan je hem herkent", "Voorbeeld"], [
                ["mededelend", "eindigt op een punt", "De kat slaapt."],
                ["vragend (een vraagzin)", "werkwoord vooraan, vraagteken achteraan", "Slaapt de kat?"],
                ["bevelend", "begint met het werkwoord, geen onderwerp", "Kom hier."],
                ["uitroepend", "eindigt op een uitroepteken", "Wat een mooie kat!"],
            ]), "Het werkwoord past zich aan het onderwerp aan: in het enkelvoud slaapt één kat, in het meervoud slapen twee katten."),
        ]),
        dict(kop="Werkwoordspelling", blokken=[
            ("fig", svg.stappen(["Zoek de stam|hele werkwoord min -en",
                                 "Welke tijd?|nu of vroeger",
                                 "Pas de regel toe|stam + t, of -te/-de"], kleur=svg.AMBER),
             "Werken → stam werk. Nu: ik werk, jij werkt. Vroeger: ik werkte."),
            ("p", "<strong>'t kofschip</strong>: eindigt de stam op t, k, f, s, ch of p (en ook x), dan wordt de verleden tijd <strong>-te</strong>. In alle andere gevallen <strong>-de</strong>."),
            ("weetje", "De t van <em>jij werkt</em> valt weg als jij <em>achter</em> het werkwoord staat: <em>Werk jij vandaag?</em> Dat is de fout die het vaakst gemaakt wordt."),
        ]),
        dict(kop="Meervoud en verkleinwoord", blokken=[
            ("fig", tabel(["Regel", "Voorbeeld"], [
                ["meestal -en", "boek → boeken"],
                ["soms -s", "tafel → tafels, meisje → meisjes"],
                ["klinker verdubbelt niet", "raam → ramen"],
                ["medeklinker verdubbelt wel", "pot → potten"],
                ["verkleinwoord", "boek → boekje, raam → raampje"],
            ]), "Of het -en of -s wordt, hoor je meestal: zeg het luidop."),
        ]),
        dict(kop="Lettergrepen en woordvorming", blokken=[
            ("p", "Een <strong>lettergreep</strong> is een stukje woord dat je in één keer uitspreekt. Klap mee met je handen terwijl je het woord zegt, dan tel je ze vanzelf: <em>va-kan-tie</em> is drie, <em>com-pu-ter</em> ook drie."),
            ("p", "Nieuwe woorden maak je op twee manieren:"),
            ("fig", tabel(["Manier", "Hoe het werkt", "Voorbeeld"], [
                ["samenstelling", "twee bestaande woorden aan elkaar", "boek + kast = boekenkast"],
                ["afleiding", "een stukje ervoor of erachter", "snel + -heid = snelheid"],
                ["", "", "on- + bereikbaar = onbereikbaar"],
            ]), "Bij een samenstelling kan je allebei de stukken los gebruiken, bij een afleiding niet: -heid bestaat niet op zichzelf."),
            ("weetje", "Woorden die bij elkaar horen noem je een woordveld. Fiets, auto en trein horen samen: het zijn vervoermiddelen. Boom hoort er niet bij."),
        ]),
        dict(kop="Uitdrukkingen en gezegden", blokken=[
            ("p", "Sommige zinnetjes betekenen iets heel anders dan wat er letterlijk staat. Je kan ze niet uitrekenen, je moet ze kennen — en ze maken je taal levendig."),
            ("fig", tabel(["Uitdrukking", "Wat het betekent"], [
                ["de kat uit de boom kijken", "eerst afwachten hoe de zaken staan"],
                ["een appeltje voor de dorst", "iets opzijzetten voor later, meestal geld"],
                ["de draad kwijt zijn", "niet meer weten waar je was"],
                ["met de deur in huis vallen", "meteen zeggen waarvoor je komt"],
                ["ergens geen kaas van gegeten hebben", "er niets van kennen"],
            ]), "Kom je er een tegen die je niet kent, vraag er dan naar. Raden loopt vaak mis."),
        ]),
        dict(kop="Hoofdletters", blokken=[
            ("p", "Een hoofdletter krijg je aan het begin van een zin, bij namen van mensen, bij landen, steden en talen, en bij feestdagen."),
            ("p", "Géén hoofdletter bij dagen en maanden — dat is net het verschil met het Engels. Bij ons: maandag, december. In het Engels: Monday, December."),
        ]),
    ],
    onthoud=[
        "Werkwoord? Zet er ik, jij of wij voor.",
        "Persoonsvorm vinden: maak van de zin een vraag.",
        "Onderwerp vinden: wie of wat + de persoonsvorm.",
        "'t kofschip beslist tussen -te en -de.",
        "Staat jij achter het werkwoord, dan valt de t weg.",
        "Dagen en maanden krijgen in het Nederlands géén hoofdletter.",
        "Lijdend voorwerp: wie of wat + gezegde + onderwerp.",
        "Lettergrepen tel je door mee te klappen.",
        "Samenstelling: twee losse woorden. Afleiding: een stukje ervoor of erachter.",
    ])

BUNDELS["literatuur"] = dict(
    vak=VAK, titel="Literatuur",
    onder="Verhalen en gedichten: hoe ze gebouwd zijn en waarom dat werkt.",
    secties=[
        dict(kop="De spanningsboog", blokken=[
            ("p", "Bijna elk verhaal volgt dezelfde lijn. Herken je die, dan zie je meteen waar je in een boek zit."),
            ("fig", svg.spanningsboog(470), "De spanning loopt op tot het hoogtepunt en zakt daarna snel."),
            ("p", "Het hoogtepunt komt meestal laat in het verhaal, niet in het midden. Daarna wil je als lezer nog maar één ding weten: hoe loopt het af?"),
        ]),
        dict(kop="De bouwstenen van een verhaal", blokken=[
            ("p", "Wie over een boek praat, heeft het altijd over dezelfde vijf dingen. Kan je die vijf benoemen, dan kan je over elk boek iets zinnigs zeggen."),
            ("fig", tabel(["Bouwsteen", "De vraag die erbij hoort"], [
                ["de personages", "over wie gaat het? wie is de hoofdpersoon?"],
                ["de plaats", "waar speelt het zich af?"],
                ["de tijd", "wanneer speelt het? hoeveel tijd gaat er voorbij?"],
                ["de gebeurtenissen", "wat gebeurt er, en in welke volgorde?"],
                ["de hoofdgedachte", "waar gaat het eigenlijk over?"],
            ]), "De hoofdgedachte is niet hetzelfde als het verhaal: een boek kan over een schoolreis gaan en eigenlijk over vriendschap."),
            ("p", "Eindigt een hoofdstuk precies op het spannendste moment, dan heet dat een <strong>cliffhanger</strong>. De schrijver laat je in de lucht hangen zodat je wil doorlezen. Series op televisie doen net hetzelfde."),
        ]),
        dict(kop="Wie vertelt het verhaal?", blokken=[
            ("fig", tabel(["Verteller", "Hoe je het merkt", "Wat dat doet"], [
                ["ik-verteller", "het verhaal zegt ik", "je kruipt in het hoofd van één personage"],
                ["hij- of zij-verteller", "het verhaal zegt hij of zij", "je ziet meer dan één personage"],
            ]), "Een ik-verteller weet niet alles — en vertelt soms iets anders dan wat er echt gebeurde."),
        ]),
        dict(kop="Soorten verhalen", blokken=[
            ("fig", tabel(["Genre", "Waaraan je het herkent"], [
                ["avontuur", "een reis, gevaar, een doel dat bereikt moet worden"],
                ["fantasy", "een wereld met eigen regels, magie"],
                ["sciencefiction", "toekomst, techniek die nog niet bestaat"],
                ["detective", "een raadsel dat opgelost moet worden"],
                ["historisch verhaal", "speelt in een echt verleden"],
                ["realistisch verhaal", "zou echt kunnen gebeuren"],
            ]), None),
            ("p", "Een <strong>sprookje</strong> (met magie, heksen en toverspreuken), een <strong>fabel</strong> (met dieren die voor mensen staan, en een les op het einde), een <strong>mythe</strong> (over goden, zoals de Griekse verhalen over Zeus) en een <strong>sage of legende</strong> (een oud verhaal over een plek of een persoon, van generatie op generatie doorverteld) zijn oude verhaalvormen. Ze werden eerst verteld en pas later opgeschreven."),
            ("p", "Een verhaal hoeft niet uit lopende tekst te bestaan. In een <strong>stripverhaal</strong> vertellen de prenten en de tekstballonnen samen; in een <strong>toneelstuk</strong> lees je vooral dialoog, met de naam van het personage ervoor en daartussen regieaanwijzingen over wat de spelers doen."),
            ("kader", "<p style='margin:0 0 4px'><strong>Fictie</strong> — verzonnen: een roman, een sprookje, een stripverhaal.</p>"
                      "<p style='margin:0'><strong>Non-fictie</strong> — over dingen die echt zijn: een biografie, een boek over dinosaurussen, een reisgids.</p>"),
        ]),
        dict(kop="Gedichten", blokken=[
            ("p", "Een gedicht zegt met weinig woorden veel. De vorm doet mee: waar de regel eindigt, waar een wit staat, hoe het klinkt."),
            ("fig", tabel(["Woord", "Wat het betekent"], [
                ["strofe", "een groepje regels, met wit ertussen"],
                ["rijm", "regels die op dezelfde klank eindigen"],
                ["beeldspraak", "iets zeggen door het met iets anders te vergelijken"],
                ["vergelijking", "de zon brandt <em>als</em> een oven"],
                ["metafoor", "de zon is een oven — zonder als"],
            ]), "Niet elk gedicht rijmt. Rijm is een keuze, geen voorwaarde."),
        ]),
        dict(kop="Wie maakt een boek", blokken=[
            ("fig", tabel(["Wie", "Wat die doet"], [
                ["de auteur", "schrijft de tekst — een ander woord voor schrijver"],
                ["de illustrator", "maakt de tekeningen bij de tekst"],
                ["de vertaler", "zet het boek om in een andere taal"],
                ["de uitgeverij", "drukt het boek en brengt het in de winkel"],
            ]), "Op het omslag staan meestal de auteur en de uitgeverij; de illustrator staat vaak binnenin."),
            ("p", "Achteraan staat de <strong>flaptekst</strong>: een kort stukje dat vertelt waarover het boek gaat, zonder het einde te verklappen. Die is er om je nieuwsgierig te maken, dus ze vertelt nooit het hele verhaal."),
        ]),
        dict(kop="Praten over een boek", blokken=[
            ("p", "Zeggen dat een boek leuk was, zegt nog niets. Zeg <em>waarom</em>: over het verhaal, over een personage, of over hoe het geschreven is."),
            ("fig", tabel(["In plaats van", "Zeg liever"], [
                ["het was spannend", "ik wist tot de laatste bladzijde niet hoe het zou aflopen"],
                ["saai", "er gebeurde te weinig in de eerste honderd bladzijden"],
                ["het hoofdpersonage was leuk", "ik herkende mezelf in hoe zij twijfelde"],
            ]), "Zo wordt je mening iets waar iemand anders ook wat aan heeft."),
        ]),
    ],
    onthoud=[
        "Elk verhaal heeft een begin, een probleem, een hoogtepunt en een einde.",
        "Het hoogtepunt komt laat, niet in het midden.",
        "Een ik-verteller weet niet alles.",
        "Een fabel heeft dieren die praten, een mythe komt uit een oude cultuur.",
        "Een vergelijking gebruikt als, een metafoor niet.",
        "Zeg altijd waarom je iets goed of slecht vond.",
        "Personages, plaats, tijd, gebeurtenissen en hoofdgedachte: dat zijn de vijf.",
        "Fictie is verzonnen, non-fictie gaat over wat echt is.",
        "Een cliffhanger stopt op het spannendste moment.",
        "De auteur schrijft, de illustrator tekent.",
    ])

if __name__ == "__main__":
    for naam, b in BUNDELS.items():
        bundel.schrijf(b, naam)

# -*- coding: utf-8 -*-
"""De leerbundels voor Nederlands op ✨ Spark-niveau.

Gebaseerd op de vakfiche Nederlands 1ste graad A-stroom die Kim aanleverde.
Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met moeilijkere vragen. De bundel wordt
dus twee keer geüpload, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../spark/nederlands.json` doet
daar het voorwerk voor; daarna gaat elke vraag nog één voor één naast de tekst.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel

VAK = "Nederlands"
SPARK = "✨ Spark — 1ste en 2de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ---------------------------------------------------------------------------

BUNDELS["onderwerp-hoofdgedachte-en-hoofdpunten"] = dict(
    vak=VAK, niveau=SPARK, titel="Onderwerp, hoofdgedachte en hoofdpunten",
    onder="Wat een tekst zegt in enkele woorden, in één zin, en in de punten die dat dragen.",
    secties=[
        dict(kop="Drie lagen in elke tekst", blokken=[
            ("p", "Het <strong>onderwerp</strong> is waarover een tekst gaat. Je zegt het in "
                  "één of enkele <strong>woorden</strong>: 'huidverzorging bij kinderen', "
                  "'zwerfvuil in onze straat', 'elektrische steps'. Je schrijft het dus niet "
                  "op in een volledige zin."),
            ("p", "De <strong>hoofdgedachte</strong> is de belangrijkste boodschap, in "
                  "één zin. Ze zegt wat de tekst over dat onderwerp beweert: 'Kinderen "
                  "gebruiken veel huidverzorging, terwijl dat niet nodig en soms ongezond is.' "
                  "Daar zit meteen het verschil: het onderwerp is waarover het gaat, de "
                  "hoofdgedachte is wat de tekst daarover zegt."),
            ("fig", svg.kernpiramide(),
             "De hoofdpunten dragen de hoofdgedachte; de details maken het geheel concreet."),
            ("p", "De <strong>hoofdpunten</strong> zijn de inhoudelijke elementen die de "
                  "hoofdgedachte <strong>ondersteunen</strong>: 'blauw licht houdt je wakker', "
                  "'meldingen onderbreken je slaap', 'wie te weinig slaapt, presteert slechter "
                  "op school'. Een <strong>detail</strong> kan je weglaten zonder dat de "
                  "boodschap wankelt — het precieze aantal ondervraagden bijvoorbeeld. Een "
                  "hoofdpunt kan dat net niet."),
            ("p", "Twee teksten over hetzelfde onderwerp kunnen een heel andere hoofdgedachte "
                  "hebben: de ene raadt elektrische steps aan, de andere noemt ze gevaarlijk."),
        ]),
        dict(kop="Waar je ze vindt", blokken=[
            ("p", "De hoofdgedachte staat meestal in de <strong>inleiding</strong> of in het "
                  "<strong>slot</strong>. In het slot vind je vaak ook het <strong>besluit</strong>. "
                  "Elke <strong>alinea</strong> heeft daarbinnen meestal één "
                  "<strong>kerngedachte</strong>, en die staat vaak in de eerste of de laatste "
                  "zin van die alinea. Daarom kan je een tekst samenvatten door per alinea één "
                  "<strong>kernzin</strong> te noteren."),
            ("p", "Vóór je een lange tekst helemaal leest, kijk je naar de "
                  "<strong>titel</strong>, de <strong>tussentitels</strong> en de "
                  "<strong>afbeeldingen</strong>. Ook woorden die vet gedrukt staan, een foto of "
                  "een grafiek helpen je de inhoud te vatten. De lengte van de zinnen of het "
                  "aantal bladzijden zegt daarover niets."),
            ("kader", "Een titel verklapt vaak al de soort inhoud. <strong>'Waarom slapen "
                      "tieners te weinig?'</strong> kondigt uitleg en oorzaken aan. Zo weet je "
                      "vooraf wat je mag verwachten."),
            ("p", "Stel jezelf vóór het lezen of luisteren een paar vragen: wat weet ik hier al "
                  "over? Waarover zou deze tekst kunnen gaan? Van wie is hij en waarom is hij "
                  "gemaakt?"),
        ]),
        dict(kop="Relevante informatie selecteren", blokken=[
            ("p", "Zoek je in een lange tekst het antwoord op één bepaalde vraag, dan noteer je "
                  "<em>alleen</em> de informatie die met die vraag te maken heeft. De rest laat "
                  "je staan. Krijg je twee teksten over hetzelfde onderwerp, dan zoek je in "
                  "allebei wat op jouw vraag antwoordt en legt dat naast elkaar: samen geven ze "
                  "een vollediger beeld."),
            ("p", "Een zin als 'In ons land gooit een gezin gemiddeld 60 kilo eten per jaar weg' "
                  "is een hoofdpunt met een cijfer dat het ondersteunt. Zulke zinnen zijn goud "
                  "waard in je antwoord."),
            ("p", "Past één alinea niet bij de hoofdgedachte die je gevonden hebt, herlees ze "
                  "dan: vaak is het een <strong>tegenargument</strong> of een "
                  "<strong>nuance</strong>, aangekondigd door 'maar' of 'hoewel'."),
        ]),
        dict(kop="Notities nemen", blokken=[
            ("p", "Je neemt notities om de belangrijkste informatie vast te houden en er daarna "
                  "mee te werken: een samenvatting maken of een vraag beantwoorden. Ze mogen "
                  "kort: <strong>afkortingen</strong>, <strong>symbolen</strong> en pijlen, "
                  "<strong>telegramstijl</strong>. Alles woord voor woord overschrijven lukt "
                  "niet en helpt niet."),
            ("fig", tabel(["zwakke notitie", "bruikbare notitie"], [
                ["slaap", "oorzaak: te weinig slaap → gevolg: slechtere punten"],
                ["het was interessant", "sluikstort kost stad 200 000 euro/jaar"],
                ["de spreker praatte snel", "3 oorzaken: licht, meldingen, laat sporten"],
            ]), "Noteer de inhoud, niet je indruk van de spreker."),
            ("p", "Duid tijdens het lezen de <strong>sleutelwoorden</strong> en de kernzinnen "
                  "aan. Ordenen doe je in een schema, een tabel of een <strong>mindmap</strong>: "
                  "een tekening waarin je vanuit één centraal woord vertakkingen maakt."),
            ("weetje", "Bij een luistertekst noteer je terwijl je luistert, niet achteraf. Je "
                       "kan een gesproken tekst niet terugbladeren, en details vergeet je snel."),
        ]),
        dict(kop="Samenvatten en onbekende woorden", blokken=[
            ("p", "Een <strong>samenvatting</strong> is de hoofdgedachte plus de belangrijkste "
                  "hoofdpunten, in je eigen woorden. Wat jij ervan vindt, hoort er niet in: je "
                  "mening zet je in een reactie of een recensie."),
            ("p", "Kom je een woord tegen dat je niet kent, zoals 'wateroverlast', dan leid je "
                  "de betekenis eerst zelf af: uit de zinnen eromheen, uit wat je al over het "
                  "onderwerp weet, uit de manier waarop het woord gevormd is (water + overlast), "
                  "en soms uit je kennis van het Engels of het Frans. Alleen een woord dat je "
                  "écht nodig hebt en niet kan afleiden, zoek je op in een "
                  "<strong>woordenboek</strong>. Op het examen mag dat digitaal, maar je hebt "
                  "geen tijd om elk woord op te zoeken."),
        ]),
    ],
    onthoud=[
        "Onderwerp: enkele woorden. Hoofdgedachte: één zin. Hoofdpunten: wat die zin draagt.",
        "Een detail mag weg in een samenvatting, een hoofdpunt niet.",
        "De hoofdgedachte staat meestal in de inleiding of het slot; elke alinea heeft één kerngedachte.",
        "Notities: afkortingen, symbolen, telegramstijl, een schema of een mindmap.",
        "Leid een onbekend woord eerst af uit de context, de voorkennis en de bouw van het woord.",
        "In een samenvatting staat de inhoud van de tekst, niet jouw mening.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["tekstsoorten-en-het-communicatiemodel"] = dict(
    vak=VAK, niveau=SPARK, titel="Tekstsoorten en het communicatiemodel",
    onder="Welke soorten teksten er zijn, wat ze willen bereiken, en hoe je dat aan de zender ziet.",
    secties=[
        dict(kop="Zes soorten teksten", blokken=[
            ("p", "Elke tekst heeft een <strong>doel</strong>: wat de zender ermee wil bereiken. "
                  "De vakfiche onderscheidt zes soorten lees- en luisterteksten."),
            ("fig", tabel(["soort tekst", "voorbeelden"], [
                ["informeren", "een krantenartikel, een stukje uit een leerboek, een interview, een reportage"],
                ["overtuigen of beïnvloeden", "een reclamefilmpje, een folder van een politieke partij, een campagne tegen te snel rijden, propaganda, fake news, een publireportage"],
                ["een mening geven", "een recensie, een hotelbeoordeling, een reactie op een forum, een productreview, een protestlied"],
                ["instructies geven", "een handleiding, een recept, een bijsluiter, een instructiefilmpje, een schoolreglement, veiligheidsvoorschriften"],
                ["een verhaal vertellen", "een videoblog, een reisverslag, een podcast, een verhalend gedicht"],
                ["literaire teksten", "een jeugdboek, een kortverhaal, een strip, een gedicht, een lied, stand-upcomedy"],
            ]), "Een literaire tekst heeft een esthetische waarde en speelt vaak in op je gevoel."),
            ("p", "Let op de valkuilen. Een stukje uit een leerboek is een "
                  "<strong>informatieve tekst</strong> en geen "
                  "<strong>instructieve tekst</strong>: het informeert, het geeft je geen "
                  "instructies. Een <strong>interview</strong> bestaat uit vragen en "
                  "antwoorden, maar is óók een informatieve tekst. Een <strong>protestlied</strong> brengt een "
                  "standpunt én is literair. En één tekst kan meer dan één doel hebben: een "
                  "publireportage informeert en verkoopt tegelijk, en een <strong>zoekertje</strong> "
                  "voor je oude gsm geeft informatie én wil iemand overtuigen om te kopen."),
        ]),
        dict(kop="Het communicatiemodel", blokken=[
            ("p", "Bij elke lees-, luister- en schrijfopdracht pas je het "
                  "<strong>communicatiemodel</strong> toe. Het heeft zes delen."),
            ("fig", svg.communicatiemodel(),
             "Zender, boodschap, ontvanger, kanaal, context en doel."),
            ("fig", tabel(["deel", "wat het is", "voorbeeld"], [
                ["zender", "wie de boodschap verstuurt", "jij, een redactie, een bedrijf"],
                ["boodschap", "wat de zender precies wil zeggen", "'ik ben tien minuten te laat'"],
                ["ontvanger", "voor wie de tekst bedoeld is", "je leerkracht, de bestuurders"],
                ["kanaal", "de weg waarlangs de boodschap gaat", "een mail, een blog, een telefoongesprek, een app"],
                ["context", "de situatie waarin je communiceert", "je bus is te laat"],
                ["doel", "wat de zender wil bereiken", "informeren, overtuigen, instrueren, vertellen"],
            ]), "Je vriendin is de ontvanger, niet het kanaal. Dat verschil wordt vaak verward."),
            ("kader", "<strong>Eén situatie, twee berichten.</strong> Je bus is te laat "
                      "(context). Je belt (kanaal) je leerkracht (ontvanger) beleefd op om te "
                      "laten weten dat je tien minuten te laat bent (boodschap). Je doel is "
                      "informeren, niet overtuigen. Naar je beste vriendin stuur je over "
                      "diezelfde bus een appje vol geïrriteerde emoji's: dezelfde boodschap, een "
                      "andere ontvanger en dus een ander register."),
        ]),
        dict(kop="De zender verraadt het doel", blokken=[
            ("p", "Wil je weten wat een tekst echt wil, kijk dan wie hem maakte. Is de zender een "
                  "redactie, dan is het doel informeren. Is de zender de verkoper, dan is het "
                  "doel verkopen, hoe informatief de tekst er ook uitziet. Een influencer die "
                  "betaald wordt om een crème aan te prijzen, maakt <strong>reclame</strong>."),
            ("p", "Ook de vorm helpt. Aanhef en ondertekening verraden zender en ontvanger: "
                  "'Beste ouders' met 'Met vriendelijke groeten, de directie' eronder is een "
                  "schoolbrief. En de opbouw verraadt de soort: genummerde stappen wijzen op een "
                  "instructie, argumenten op overtuigen, gebeurtenissen op een verhaal."),
            ("p", "Weten met welke tekstsoort je te maken hebt, is geen etiket plakken. Het zegt "
                  "je waarop je moet letten: bij een overtuigende tekst op argumenten en "
                  "eenzijdigheid, bij een instructie op de volgorde van de stappen."),
            ("weetje", "Het kanaal verandert de vorm van je boodschap. Dezelfde inhoud schrijf je "
                       "anders in een mail dan in een appbericht. Een mail aan de gemeente over "
                       "een kapot voetpad is formeel, met 'u' en een nette slotgroet."),
        ]),
    ],
    onthoud=[
        "Zes tekstsoorten: informeren, overtuigen, een mening geven, instrueren, vertellen, literair.",
        "Het communicatiemodel: zender, boodschap, ontvanger, kanaal, context en doel.",
        "Het kanaal is het middel (mail, app, telefoon); de ontvanger is de persoon.",
        "Kijk naar de zender om het doel te vinden: een verkoper wil verkopen.",
        "Eén tekst kan meer dan één doel hebben, zoals een publireportage.",
        "De opbouw verraadt de tekstsoort: stappen, argumenten of gebeurtenissen.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["feiten-meningen-en-betrouwbaarheid"] = dict(
    vak=VAK, niveau=SPARK, titel="Feiten, meningen en betrouwbaarheid",
    onder="Hoe je nagaat of een tekst klopt, en hoe je zelf een standpunt onderbouwt.",
    secties=[
        dict(kop="Feit of mening?", blokken=[
            ("p", "Een <strong>feit</strong> kan je nagaan: 'België telt drie officiële "
                  "landstalen', 'deze gsm weegt 180 gram', 'de batterij gaat 12 uur mee', 'de "
                  "levering duurde vier dagen'. Een <strong>mening</strong> is wat iemand ervan "
                  "vindt: 'die film is veel te lang', 'deze gsm is zijn geld niet waard', 'het is "
                  "het beste toestel van dit jaar'."),
            ("p", "Meningen zijn niet fout; ze zijn alleen geen feiten. Twee mensen kunnen over "
                  "dezelfde feiten een andere mening hebben, en een sterke mening steunt net op "
                  "feiten. Herken een mening die vermomd is als feit aan de "
                  "<strong>gevoelswoorden</strong>: 'schandalig', 'schokkend', 'iedereen weet', "
                  "'veel te'. 'Veel te duur' is een mening, '24 euro' is een feit. In een "
                  "<strong>productreview</strong> zijn 'de batterij gaat 12 uur mee' en 'het "
                  "toestel weegt 240 gram' dus feiten, en 'het beste toestel van dit jaar' een "
                  "mening."),
        ]),
        dict(kop="Is deze tekst betrouwbaar?", blokken=[
            ("p", "Je beoordeelt een tekst met een reeks vragen. Eén antwoord beslist niets; "
                  "samen geven ze een beeld."),
            ("fig", tabel(["waarnaar je kijkt", "waarom het telt"], [
                ["Wordt de auteur vermeld?", "zonder auteur weet je niet wie verantwoordelijk is"],
                ["Wie publiceert het artikel?", "een redactie controleert, een merk verkoopt"],
                ["Enkel via sociale media of ook bij nieuwsmedia?", "circuleert het alleen online, ga het dan zelf na"],
                ["Is de website professioneel?", "een mooie site is zo gemaakt: geen bewijs"],
                ["Wat is de bedoeling van de zender?", "informeren, verkopen of overtuigen"],
                ["Is het reclame, nepnieuws of propaganda?", "propaganda brengt bewust één kant"],
                ["Is de titel neutraal of wil hij clicks?", "'Je gelooft NOOIT wat…' is clickbait"],
                ["Welke bronnen gebruikt de tekst?", "met bron en jaartal kan je het controleren"],
                ["Vooral feiten of meningen?", "een oordeel is geen vaststelling"],
                ["Is de informatie recent of verouderd?", "cijfers, prijzen en regels verouderen snel"],
            ]), "Een tekst zonder auteur is niet meteen onbetrouwbaar: het is één signaal van de tien."),
            ("p", "<strong>Nepnieuws</strong> of fake news is verzonnen nieuws dat zich voordoet "
                  "als echt nieuws, vaak om clicks of geld te verdienen. Geen auteur, nergens bij "
                  "betrouwbare nieuwsmedia, en een overdreven titel die je vooral wil doen "
                  "klikken: drie signalen samen maken een bericht verdacht. Een "
                  "<strong>influencer</strong> die enthousiast een crème aanprijst en daarvoor "
                  "betaald wordt, maakt <strong>reclame</strong>, ook al leest het als een tip. "
                  "Een <strong>publireportage</strong> doet net hetzelfde: ze ziet eruit "
                  "als een reportage, maar de verkoper betaalt ze."),
            ("weetje", "Twijfel je, zoek dezelfde informatie dan bij een tweede, betrouwbare "
                       "bron: de site van een ziekenhuis of een officiële dienst, niet een "
                       "forumreactie of een meme. Likes zeggen niets over juistheid. En stuur "
                       "niets door dat je niet nagekeken hebt: wie deelt, wordt zelf een zender."),
            ("p", "Spreken twee betrouwbare teksten elkaar tegen, kijk dan naar de datum, de "
                  "bronnen en wat ze precies onderzocht hebben. Vaak gaan ze over een andere "
                  "periode of een andere groep. Komt een tekst van een fabrikant, gebruik hem "
                  "dan gerust, maar zoek de nadelen elders. En let op: een tekst kan tegelijk "
                  "correct én onbruikbaar zijn voor jouw opdracht, bijvoorbeeld als hij over een "
                  "ander land gaat."),
        ]),
        dict(kop="Standpunt, argumenten en stereotypen", blokken=[
            ("p", "Een <strong>standpunt</strong> is het oordeel dat iemand inneemt: 'Gsm's horen "
                  "niet thuis op school.' Een <strong>argument</strong> is de reden die dat "
                  "standpunt ondersteunt, meestal na 'want' of 'omdat': 'want uit onderzoek "
                  "blijkt dat leerlingen dan beter opletten'. 'Ik vind dat gewoon' en 'iedereen "
                  "weet dat' zijn geen redenen."),
            ("p", "Een goed argument telt ook voor iemand anders: 'leerlingen drinken dan meer "
                  "water en minder frisdrank', 'we hoeven geen plastic flessen mee te brengen', "
                  "'water uit de kraan is goedkoper'. Wil je écht overtuigen, geef dan ook de "
                  "nadelen toe en weerleg ze: de lezer merkt dat je de zaak kent. Schrijf je zelf "
                  "een reactie op een forum, geef dan je standpunt en drie argumenten, met een "
                  "cijfer of een voorbeeld erbij. Hoofdletters lezen als schreeuwen en werken "
                  "averechts."),
            ("p", "<strong>Stereotypering</strong> is een vast, te algemeen beeld van een hele "
                  "groep mensen: 'zoals alle tieners hangt ook hij de hele dag aan zijn scherm', "
                  "of 'wie een bepaald dialect spreekt, is minder slim'. Zo'n "
                  "<strong>stereotype</strong> klopt niet en is oneerlijk. Wie het herkent, leest "
                  "scherper."),
        ]),
    ],
    onthoud=[
        "Een feit kan je nagaan; een mening is een oordeel, vaak herkenbaar aan gevoelswoorden.",
        "Criteria: auteur, uitgever, kanaal, bedoeling, bronnen, feiten of meningen, hoe recent.",
        "Nepnieuws: geen auteur, alleen op sociale media, een titel die vooral clicks wil.",
        "Standpunt = je oordeel; argument = de reden erachter, meestal na 'want' of 'omdat'.",
        "Betrouwbaar, correct en bruikbaar zijn drie verschillende dingen.",
        "Een stereotype is een te algemeen beeld van een hele groep.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["tekststructuur-en-signaalwoorden"] = dict(
    vak=VAK, niveau=SPARK, titel="Tekststructuur en signaalwoorden",
    onder="Hoe een tekst in elkaar zit, en welke woorden je de weg wijzen.",
    secties=[
        dict(kop="Inleiding, midden en slot", blokken=[
            ("p", "Elke goed opgebouwde tekst bestaat uit drie delen: een "
                  "<strong>inleiding</strong>, een <strong>midden</strong> en een "
                  "<strong>slot</strong>. Dat is de <strong>IMS-structuur</strong>."),
            ("fig", svg.tekstopbouw([
                ("Inleiding", "wekt je belangstelling en zegt waarover het gaat", 1.3),
                ("Midden", "werkt uit, één gedachte per alinea", 2.2),
                ("Slot", "vat samen en trekt het besluit", 1.3),
            ]), "Een nieuw argument hoort in het midden, waar je het kan uitwerken, nooit in het slot."),
            ("p", "Een <strong>alinea</strong> heeft meestal één kerngedachte. Je begint er een "
                  "nieuwe bij een nieuw <strong>deelonderwerp</strong>, en je laat witruimte "
                  "ertussen, wat je lezer helpt. "
                  "Hoe lang een alinea is, ligt niet vast: de inhoud beslist."),
            ("p", "Krijg je losse alinea's en moet je er een tekst van maken, dan herken je de "
                  "inleiding daaraan dat ze het onderwerp voorstelt, en het slot aan woorden als "
                  "'kortom' of 'tot slot'. Schrijf je een <strong>betoog</strong>, een tekst "
                  "waarin je iemand met argumenten wil overtuigen, zet je sterkste argument dan "
                  "vooraan of helemaal achteraan: daar valt het het meest op en blijft het het "
                  "best hangen."),
        ]),
        dict(kop="Signaalwoorden: wat komt er?", blokken=[
            ("p", "<strong>Signaalwoorden</strong> geven het verband tussen zinnen aan. Ze zeggen "
                  "vooraf wat er komt, en zo kan je de gedachtegang van een tekst volgen."),
            ("fig", tabel(["verband", "signaalwoorden", "voorbeeld"], [
                ["reden", "want, omdat", "Ik was te laat omdat de trein vertraging had."],
                ["gevolg", "dus, daarom, daardoor, zodat", "Het was koud. Daarom trok hij zijn jas aan."],
                ["tegenstelling", "maar, toch, hoewel", "Hij had hard gestudeerd. Toch haalde hij een onvoldoende."],
                ["opsomming", "ten eerste, ten tweede, tot slot", "Ten eerste is het goedkoper."],
                ["toevoeging", "bovendien, daarnaast, ook", "Bovendien kost het minder."],
                ["voorbeeld", "bijvoorbeeld, zoals, denk maar aan", "Fruit, zoals een appel."],
                ["voorwaarde", "als, indien", "Als het morgen regent, gaat de sportdag niet door."],
                ["samenvatting", "kortom, samengevat, tot slot", "Kortom, de fiets wint."],
            ]), "Twee verschillende woorden kunnen hetzelfde verband aangeven."),
            ("p", "Bij een <strong>luistertekst</strong> zijn ze extra kostbaar: je kan niet "
                  "terugbladeren, en 'ten eerste' zegt je dat er nog punten volgen, 'kortom' dat "
                  "het slot begint."),
        ]),
        dict(kop="Verwijswoorden en samenhang", blokken=[
            ("p", "Een <strong>verwijswoord</strong> grijpt terug naar iets dat al genoemd is: "
                  "zij, hem, deze, hun, die, er. 'Mijn zus heeft een nieuwe fiets gekocht. Ze "
                  "rijdt er elke dag mee naar school': 'ze' is de zus, 'er' is de fiets. Vind je "
                  "niet terug naar wie of wat een verwijswoord verwijst, dan is de tekst op dat "
                  "punt onduidelijk en moet de schrijver het woord herhalen."),
            ("p", "Verwijswoorden en signaalwoorden heten samen de "
                  "<strong>structuuraanduiders</strong>. Zonder hen blijft een tekst een reeks "
                  "losse zinnen: 'Fietsen is gezond. Mijn fiets is blauw. In de stad staan veel "
                  "auto's.' Drie correcte zinnen, geen samenhang."),
            ("p", "Naast de woorden helpen ook de <strong>tekstopbouwende elementen</strong>: "
                  "titels en tussentitels, benadrukte woorden, witruimte, lay-out, een foto of "
                  "een grafiek. Alles in hoofdletters typen hoort daar niet bij: dat maakt het "
                  "net moeilijker."),
        ]),
    ],
    onthoud=[
        "IMS: inleiding, midden en slot. In het slot staat het besluit.",
        "Eén alinea, één kerngedachte, met witruimte ertussen.",
        "Signaalwoorden geven het verband: reden, gevolg, tegenstelling, opsomming, voorbeeld, voorwaarde.",
        "Verwijswoorden (zij, hem, deze, hun, er) grijpen terug naar iets dat al genoemd is.",
        "Signaalwoorden en verwijswoorden samen zijn de structuuraanduiders.",
        "Je sterkste argument staat vooraan of helemaal achteraan.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["schrijven-spreken-en-gesprekken-voeren"] = dict(
    vak=VAK, niveau=SPARK, titel="Schrijven, spreken en gesprekken voeren",
    onder="Wat een opdracht van je vraagt, hoe je ze voorbereidt en waarop je beoordeeld wordt.",
    secties=[
        dict(kop="Wat vraagt de opdracht?", blokken=[
            ("p", "Schrijven en spreken doe je altijd met een doel. De vakfiche noemt er zeven: "
                  "informatie geven en vragen, iets uitleggen, je mening geven, in gesprek gaan "
                  "over maatschappelijke thema's, iemand overtuigen, iets vertellen, en creatief "
                  "zijn met taal."),
            ("fig", tabel(["doel", "voorbeelden van opdrachten"], [
                ["informatie geven en vragen", "een zoekertje opstellen, iemand uitnodigen, een vraag stellen op een forum, informatie vragen over een product in een winkel"],
                ["iets uitleggen", "een korte handleiding schrijven, uitleggen hoe je een spel speelt, een recept uitwerken, tips geven"],
                ["je mening geven", "beschrijven wat je van een film vindt, een product beoordelen, je standpunt geven"],
                ["overtuigen", "een productadvertentie opstellen, met je ouders onderhandelen over een afspraak, een vriend warm maken voor de jeugdbeweging"],
                ["vertellen", "een mail over een uitstap, vertellen wat je meegemaakt hebt"],
                ["creatief met taal", "een verhaal, een gedicht, een reclameboodschap met rijm, ritme en lay-out"],
            ]), "Bij een schrijf- of spreekopdracht krijg je een kader dat je ondersteunt: voor wie, waarom, waarover."),
            ("p", "Ga je in gesprek over een <strong>maatschappelijk thema</strong> zoals "
                  "gezondheid, klimaat, sociale media, inspraak of mobiliteit, dan gebruik je "
                  "<strong>bronnen</strong>: lees vooraf iets en onthoud er een cijfer uit."),
            ("p", "Wil je creatief zijn met taal, dan maken drie <strong>technieken</strong> een "
                  "<strong>slogan</strong> sterk: <strong>rijm</strong>, <strong>ritme</strong> "
                  "en een korte, opvallende <strong>lay-out</strong>. Lang is niet beter: een "
                  "slogan werkt net omdat hij kort is."),
        ]),
        dict(kop="Eerst een plan", blokken=[
            ("p", "Begin nooit blind. Maak een <strong>schrijfplan</strong> of een "
                  "<strong>spreekplan</strong> met kernwoorden: welke stappen komen er, en in "
                  "welke volgorde? Voor een spreekopdracht neem je die kernwoorden mee, geen "
                  "volledig uitgeschreven tekst: met kernwoorden blijf je natuurlijk spreken en "
                  "kan je opkijken. Voorlezen klinkt vlak."),
            ("p", "Bij een instructie is de volgorde de structuur: genummerde stappen in de "
                  "volgorde waarin je ze uitvoert. Bij een <strong>recensie</strong> geef je je "
                  "mening met argumenten en voorbeelden uit de film — zonder het einde te "
                  "verklappen. Bij een <strong>zoekertje</strong> zet je wat je verkoopt, in "
                  "welke staat, en hoe men je bereikt: alles wat de ontvanger nodig heeft, en "
                  "niets meer."),
            ("p", "Vraag je iets, stel de vraag dan precies: 'Kan u me zeggen hoelang de garantie "
                  "op dit toestel loopt?' levert een bruikbaar antwoord op, 'hoe zit dat "
                  "allemaal?' niet. En houd je aan de gevraagde lengte: te lang schrijven kost "
                  "tijd en leidt af van je boodschap."),
        ]),
        dict(kop="Waarop je beoordeeld wordt", blokken=[
            ("fig", tabel(["vereiste", "wat men nakijkt"], [
                ["taakvoltooiing", "het tekstdoel is bereikt; je boodschap is volledig, helder, correct en ter zake"],
                ["woordenschat", "frequente én minder frequente woorden, eenvoudige figuurlijke taal"],
                ["grammatica en zinsbouw", "je maakt correcte zinnen"],
                ["tekststructuur en samenhang", "inleiding, midden en slot, met signaal- en verwijswoorden"],
                ["register en beleefdheid", "formeel of informeel, met de beleefdheidsconventies die bij je ontvanger passen"],
                ["spelling en leestekens", "alleen bij schrijven en schriftelijke interactie"],
                ["tekstopbouw en lay-out", "titels waar nodig, ingedeeld in alinea's met een witregel ertussen"],
                ["lichaamstaal, vlotheid, uitspraak", "alleen bij spreken: oogcontact, vlot spreken, verzorgd Standaardnederlands"],
            ]), "Op een digitaal examen typ je, dus je handschrift telt niet mee."),
            ("p", "<strong>Vlotheid</strong> betekent niet zo snel mogelijk praten: even nadenken "
                  "mag, als je verhaal maar blijft lopen. Zit je vast, laat je dan niet "
                  "ontmoedigen: er zijn <strong>strategieën</strong> die je verder helpen. "
                  "Zoek een <strong>omschrijving</strong> voor het woord dat je "
                  "mist, herlees een stukje en schrijf van daaruit verder, of gebruik een "
                  "woordenboek of een spellingcontrole."),
            ("p", "Variëren maakt je tekst levendig: gebruik <strong>synoniemen</strong> en "
                  "wissel je zinsbouw af."),
            ("p", "Schrijf je een formele mail, dan hoort daar een <strong>aanhef</strong> bij "
                  "('Geachte mevrouw') en een <strong>slotgroet</strong> ('Met vriendelijke "
                  "groeten'), met beleefde formuleringen ertussen: 'Ik zou graag willen weten "
                  "wanneer de inschrijvingen starten.' Een formele brief sluit je niet af met "
                  "'groetjes'."),
        ]),
        dict(kop="Een gesprek voeren", blokken=[
            ("p", "Bij een <strong>spreekopdracht</strong> ben je alleen aan het woord. Met "
                  "<strong>interactie</strong> bedoelen we dat je in gesprek gaat met iemand. Voor "
                  "beide <strong>mondelinge opdrachten</strong> krijg je "
                  "<strong>voorbereidingstijd</strong>, maar je moet ook spontaan kunnen "
                  "reageren op wat de ander zegt."),
            ("fig", svg.spreekballonnen([
                ("beginnen", "Goeiedag, ik ben Lotte. Ik kom voor de inschrijving.", True),
                ("gaande houden", "En hoe laat start de training dan precies?", False),
                ("beëindigen", "Dank u wel. Dan zie ik u zaterdag.", True),
            ]), "Een gesprek correct beginnen, gaande houden en beëindigen."),
            ("p", "Gaande houden doe je door vragen te stellen, te reageren op wat de ander zegt, "
                  "interesse te tonen en de ander te laten uitspreken. Krijg je een vraag die je "
                  "niet verwacht had, neem dan even tijd, zeg wat je wél weet en vraag gerust om "
                  "verduidelijking. Afronden doe je niet door weg te lopen: je bedankt, vat kort "
                  "samen wat afgesproken is en groet."),
            ("p", "Wil je iemand <strong>overtuigen</strong> of met je ouders "
                  "<strong>onderhandelen</strong>, geef dan argumenten en doe een voorstel waar "
                  "de ander ook iets aan heeft. Roepen dat het oneerlijk is of blijven herhalen "
                  "wat je wil, werkt niet."),
        ]),
        dict(kop="Nalezen", blokken=[
            ("p", "Lees je tekst grondig na vóór je hem indient of verstuurt: is de communicatie "
                  "<strong>helder, gepast, correct en vlot</strong>? Een verzonden mail haal je "
                  "niet meer terug, en fouten verzwakken je boodschap."),
            ("weetje", "Een <strong>spellingcontrole</strong> vindt onbestaande woorden. Ze ziet "
                       "niet dat je het verkeerde bestaande woord gebruikt: 'word' in plaats van "
                       "'wordt', 'ligt' in plaats van 'legt'. Dat blijft jouw werk."),
        ]),
    ],
    onthoud=[
        "Maak eerst een schrijf- of spreekplan met kernwoorden.",
        "Taakvoltooiing: het doel bereikt, de boodschap volledig, helder, correct en ter zake.",
        "Spreek met kernwoorden, niet met een uitgeschreven tekst: dan houd je oogcontact.",
        "Een gesprek begin je, houd je gaande en beëindig je netjes.",
        "Overtuigen doe je met argumenten, niet met herhaling.",
        "Lees na op helder, gepast, correct en vlot: een spellingcontrole vervangt dat niet.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["register-taalvariatie-en-non-verbale-communicatie"] = dict(
    vak=VAK, niveau=SPARK, titel="Register, taalvariatie en non-verbale communicatie",
    onder="Dezelfde boodschap klinkt anders bij een vriend dan bij een directeur. Hoe dat komt.",
    secties=[
        dict(kop="Register: de toon die past", blokken=[
            ("p", "Het <strong>register</strong> is de toon en de woordkeuze die bij de situatie "
                  "passen. <strong>Formeel</strong> is afstandelijk en verzorgd, "
                  "<strong>informeel</strong> is vertrouwd en losser. Allebei zijn ze juist; wie "
                  "je ontvanger is, beslist."),
            ("fig", svg.registerschaal(),
             "In een gesprek met een volwassene met wie je geen nauwe band hebt, gebruik je 'u'."),
            ("p", "Formeel kies je bij een sollicitatiemail voor een vakantiejob, een brief aan "
                  "de gemeente of een gesprek met een arts die je niet kent: 'Geachte heer of "
                  "mevrouw', 'u', en een slotgroet als 'Met vriendelijke groeten', "
                  "'Hoogachtend' of 'Met dank bij voorbaat'. Informeel mag het bij een "
                  "klasgenoot, een verjaardagskaartje voor je neef of een babbel met je trainer "
                  "die je al jaren kent."),
            ("kader", "<strong>Van informeel naar formeel herschrijven</strong> doe je zo: 'je' "
                      "wordt 'u', de emoji's gaan eruit, en je schrijft volledige zinnen met een "
                      "aanhef en een nette slotgroet. Alles wat te los klinkt, haal je weg."),
        ]),
        dict(kop="Variëteiten van het Nederlands", blokken=[
            ("p", "Het Nederlands wordt op veel manieren gebruikt, en elke "
                  "<strong>taalvariëteit</strong> heeft haar eigen plaats. Geen enkele is minderwaardig; wat past, hangt van de situatie af."),
            ("fig", tabel(["variëteit", "wat het is", "voorbeeld"], [
                ["Standaardnederlands", "overal in het taalgebied begrepen en aanvaard: school, nieuws, officiële teksten", "Ga je mee?"],
                ["tussentaal", "tussen dialect en standaardtaal in", "Ge gaat da nie doen, hè"],
                ["dialect", "streekgebonden, van één streek of dorp", "verschilt per gemeente"],
                ["jongerentaal", "onder jongeren, sterk beïnvloed door het Engels, Marokkaans of Surinaams", "verandert snel"],
                ["jargon of vakjargon", "de vaktaal van een beroep of een hobby", "buitenspel (voetbal), diagnose (geneeskunde), debet (boekhouding)"],
            ]), "'Ge' en 'gij' zijn de tussentalige varianten van 'je' en 'jij'."),
            ("p", "Binnen de standaardtaal bestaan er ook variëteiten: "
                  "<strong>Belgisch-Nederlands</strong> en "
                  "<strong>Nederlands-Nederlands</strong>. 'Ik heb mijn gsm in de auto laten "
                  "liggen' tegenover 'mijn mobieltje': allebei standaardtaal, andere kant van de "
                  "grens. Vlamingen en Nederlanders spreken ook sommige woorden anders uit."),
            ("p", "Wie tussen variëteiten kan schakelen, communiceert net sterk: twee vrienden "
                  "die onder elkaar dialect spreken en overschakelen op Standaardnederlands zodra "
                  "er iemand bijkomt die het niet begrijpt, passen hun <strong>taalvariëteit</strong> aan "
                  "hun gesprekspartner aan. Datzelfde doe je met jargon: tegenover iemand die het vak "
                  "niet kent, is vaktaal een muur. Leg uit in gewone woorden, ook als je aan je "
                  "oma schrijft over haar tablet."),
            ("weetje", "Tussentaal spreken heeft niets met spelfouten te maken: spreken en "
                       "schrijven zijn twee verschillende dingen. En wie een bepaald dialect "
                       "spreekt, wordt soms onterecht minder slim gevonden. Dat heet "
                       "<strong>stereotypering</strong>, en zo'n oordeel zegt alleen iets over "
                       "de vooroordelen van de luisteraar."),
            ("p", "Talen lijken bovendien op elkaar: water en <em>water</em>, kat en "
                  "<em>cat</em>, restaurant en <em>restaurant</em>. Wie dat verband ziet, raadt "
                  "de betekenis van een onbekend woord sneller."),
        ]),
        dict(kop="Wat je zegt zonder woorden", blokken=[
            ("p", "<strong>Non-verbale communicatie</strong> is alles wat je uitstuurt zonder "
                  "woorden: <strong>lichaamstaal</strong>, mimiek, <strong>oogcontact</strong>, "
                  "houding, afstand en bewegingen; <strong>intonatie</strong> (hoe je stem stijgt "
                  "en daalt), articulatie, tempo en volume; en zelfs je kleding en je uiterlijk."),
            ("p", "Die signalen veranderen je boodschap. Dezelfde zin — 'Dat is dan weer prachtig "
                  "gedaan' — kan met een bepaalde toon en gezichtsuitdrukking net het "
                  "tegenovergestelde betekenen. Kijk je tijdens een spreekbeurt de hele tijd naar "
                  "je blad, dan haakt je publiek af. Merk je dat je gesprekspartner zijn armen "
                  "kruist en wegkijkt, speel daar dan op in: vraag of iets niet duidelijk is."),
            ("p", "Ook in geschreven taal bestaat non-verbale communicatie. Een hele zin IN "
                  "HOOFDLETTERS wordt online gelezen als schreeuwen. Een "
                  "<strong>emoji</strong> kan je toon verduidelijken in een informeel bericht, "
                  "maar is ongepast in een formele mail, kan verkeerd begrepen worden, en "
                  "vervangt de leestekens niet. Zelfs een punt achter een kort appbericht — "
                  "'ok.' — voelt afstandelijk, hoe correct hij ook is."),
        ]),
    ],
    onthoud=[
        "Register: formeel bij onbekenden en officiële situaties, informeel bij wie je goed kent.",
        "Standaardnederlands, tussentaal, dialect, jongerentaal en jargon: elk hun eigen plaats.",
        "'Ge/gij' is tussentaal voor 'je/jij'; 'gsm' en 'mobieltje' zijn allebei standaardtaal.",
        "Jargon werkt alleen bij wie het vak kent.",
        "Non-verbaal: lichaamstaal, oogcontact, intonatie, tempo, volume, kleding, emoji's.",
        "Hoofdletters typen leest als schreeuwen; een smiley hoort niet in een formele mail.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["literatuur-en-beeldspraak"] = dict(
    vak=VAK, niveau=SPARK, titel="Literatuur en beeldspraak",
    onder="Verhalen lezen, erover praten, en taal die iets anders zegt dan ze lijkt te zeggen.",
    secties=[
        dict(kop="Fictie en non-fictie", blokken=[
            ("p", "<strong>Fictie</strong> is verzonnen: het verhaal van een meisje dat op een "
                  "onbewoond eiland belandt. <strong>Non-fictie</strong> gaat over de "
                  "werkelijkheid: een boek over de echte geschiedenis van de Titanic, of een blog "
                  "waarin iemand vertelt over zijn reis door Noorwegen — echt gebeurd, maar "
                  "verteld als een verhaal."),
            ("p", "Fictie mag zich gerust afspelen in een bestaande stad, en een verhaal in de "
                  "ik-vorm is daarom nog niet waargebeurd: de ik-verteller kan een verzonnen "
                  "personage zijn."),
            ("p", "Literaire teksten zijn niet alleen boeken. Een <strong>strip</strong>, een "
                  "<strong>lied</strong>, een <strong>gedicht</strong>, een verhaal en een blog "
                  "horen er allemaal bij. In een strip dragen tekening en tekst samen het "
                  "verhaal: gezichten, kaders en kleuren vertellen mee. Wie alleen de "
                  "tekstballonnen leest, mist de helft."),
        ]),
        dict(kop="De bouwstenen van een verhaal", blokken=[
            ("p", "Om over een verhaal te praten heb je een paar begrippen nodig: de "
                  "<strong>personages</strong>, de <strong>verhaallijn</strong>, en de "
                  "<strong>tijd</strong> en de <strong>ruimte</strong>."),
            ("fig", svg.spanningsboog(),
             "De verhaallijn: de rode draad van gebeurtenissen, van beginsituatie over probleem naar afloop."),
            ("fig", tabel(["bouwsteen", "wat het is"], [
                ["personages", "de figuren in het verhaal; het hoofdpersonage staat centraal"],
                ["verhaallijn", "de rode draad van gebeurtenissen, van begin tot afloop"],
                ["tijd", "de periode, de duur en de volgorde, met sprongen zoals een terugblik"],
                ["ruimte", "de plaats waar het speelt, en de sfeer die daarbij hoort"],
            ]), "Zonder probleem geen verhaal: dat is wat de verhaallijn op gang brengt."),
            ("p", "Schrijvers tónen vaak in plaats van te benoemen. Blijft het hoofdpersonage "
                  "rustig terwijl iedereen in paniek raakt, dan leer je iets over zijn karakter "
                  "zonder dat het er letterlijk staat. En begint een verhaal met de laatste "
                  "gebeurtenis om daarna te vertellen hoe het zover kwam, dan speelt de schrijver "
                  "met de tijd: de volgorde van het vertellen is niet altijd de volgorde van de "
                  "gebeurtenissen."),
            ("p", "Verandert de ruimte van een drukke stad naar een verlaten huis, dan verandert "
                  "de sfeer en de spanning mee. Sfeer beschrijf je met woorden als "
                  "<em>spannend</em>, <em>melancholisch</em> of <em>grappig</em>."),
            ("p", "De verhaallijn zit in het boek; de <strong>samenvatting</strong> maak jij "
                  "ervan. Dat is dus niet hetzelfde."),
        ]),
        dict(kop="Letterlijk en figuurlijk", blokken=[
            ("p", "<strong>Letterlijk</strong> betekent precies wat de woorden zeggen: 'hij at "
                  "zijn bord leeg', 'de kast staat in de gang'. <strong>Figuurlijk</strong> "
                  "taalgebruik bedoelt iets anders: 'hij is door het lint gegaan' (hij werd heel "
                  "kwaad), 'ze heeft een hart van goud', 'hij zit in zak en as', 'dat kost een "
                  "fortuin'. Uitdrukkingen en spreekwoorden zijn dus altijd figuurlijk."),
            ("p", "<strong>Beeldspraak</strong> is taal waarmee je met woorden een beeld oproept: "
                  "'het regende pijpenstelen', of 'mijn broer is een beer' als je bedoelt dat "
                  "hij groot en sterk of net knorrig is. Bij een "
                  "<strong>vergelijking</strong> staat het vergelijkingswoord er nog bij: 'ze "
                  "zwom als een vis', 'zijn handen waren zo koud als ijs', 'hij zong zoals een "
                  "vogel in de lente'. Laat je 'als' of 'zoals' weg en zet je het beeld "
                  "rechtstreeks in de plaats — 'hij is een beer' — dan wordt het sterker."),
            ("weetje", "Ken je een uitdrukking niet, zoals 'hij kreeg het op zijn heupen', leid "
                       "de betekenis dan af uit de situatie in de tekst. Wie letterlijk leest, "
                       "komt bij onzin uit."),
            ("p", "Ook de vorm doet mee. Een dichter gebruikt <strong>rijm</strong> en "
                  "<strong>ritme</strong> om zijn tekst te laten klinken en beter te laten "
                  "hangen — al rijmt niet elk gedicht. Korte regels, witruimte en herhaling zijn "
                  "betekenisvol: waar een regel afbreekt, hoor je een pauze. Een liedtekst "
                  "bespreek je op dezelfde manier als een gedicht; er komt alleen muziek bij."),
        ]),
        dict(kop="Je beleving verwoorden", blokken=[
            ("p", "Je leest literatuur om kennis te maken met andere mensen, ideeën en ervaringen: "
                  "een verhaal laat je kijken door de ogen van iemand anders. Dat staat zo in "
                  "de vakfiche."),
            ("p", "Voor het mondelinge deel van het examen lees je <strong>twee boeken</strong> "
                  "uit de lectuurlijst: je <strong>examenboeken</strong>. Je hoeft ze niet mee te brengen, maar je moet er wel over "
                  "kunnen vertellen. Denk tijdens het lezen na over deze vragen:"),
            ("kader", "Waarom spreken bepaalde aspecten van het boek je aan, of net niet? Waarom "
                      "herken je je in een bepaald personage, of net niet? Hoe zou jij reageren "
                      "in een gelijkaardige situatie? Waarom roept de tekst bij jou een bepaalde "
                      "emotie op? Wat vond je van het taalgebruik? Hoe zou jij het boek laten "
                      "eindigen?"),
            ("p", "Een sterke uitspraak zegt wat je raakte én waarom, met een voorbeeld erbij: "
                  "'Ik herkende mezelf in Sam, omdat hij ook niet durfde te zeggen wat hij "
                  "dacht.' 'Het was wel oké' zegt niets. Je mag een boek gerust saai vinden, "
                  "zolang je uitlegt waarom, en twee lezers mogen hetzelfde boek anders beleven: "
                  "een literaire tekst laat ruimte voor <strong>interpretatie</strong>, zolang je "
                  "je lezing kan steunen op wat er staat."),
            ("p", "Schrijf je zelf een kort verhaal, dan heb je diezelfde bouwstenen nodig: "
                  "personages, een plaats en een tijd, en een probleem dat het verhaal op gang "
                  "brengt. Een bronnenlijst hoort bij een informatieve tekst, niet hier."),
        ]),
    ],
    onthoud=[
        "Fictie is verzonnen, non-fictie gaat over de werkelijkheid.",
        "Bouwstenen: personages, verhaallijn, tijd en ruimte.",
        "Letterlijk = precies wat er staat; figuurlijk = iets anders, zoals in uitdrukkingen.",
        "Een vergelijking heeft 'als' of 'zoals'; beeldspraak zet het beeld er rechtstreeks voor in de plaats.",
        "Rijm, ritme en lay-out horen bij de vorm en dragen de betekenis mee.",
        "Je beleving verwoord je met een reden en een voorbeeld uit het boek.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["spelling-leestekens-en-werkwoordsvormen"] = dict(
    vak=VAK, niveau=SPARK, titel="Spelling, leestekens en werkwoordsvormen",
    onder="De regels die je niet hoort maar wel moet schrijven, en de tijden van het werkwoord.",
    secties=[
        dict(kop="De -t in de tegenwoordige tijd", blokken=[
            ("p", "De <strong>stam</strong> van een werkwoord is het hele werkwoord min -en: "
                  "werken wordt werk, worden wordt word. Vanaf die stam bouw je alle vormen."),
            ("fig", svg.werkwoord_nu(),
             "Ik werk, jij werkt, hij werkt, wij werken. Staat 'jij' áchter het werkwoord, dan valt de -t weg."),
            ("p", "Dus: 'hij wordt' met -t, maar 'word jij ook moe?' zonder. En 'wat vind jij "
                  "daarvan?' zonder, tegenover 'jij vindt dat leuk' mét. Bij een stam die al op "
                  "een t eindigt, komt er geen tweede bij: 'hij verwacht', nooit 'verwachtt'. "
                  "Eindigt de stam op een d, dan zie je wel -dt: 'hij antwoordt' (antwoord + t)."),
            ("weetje", "Je hóórt het verschil tussen 'hij wordt' en 'hij word' niet: je hoort maar "
                       "één t. Klankbeeld en schriftbeeld lopen hier uit elkaar, dus dit is een "
                       "regel die je met je hoofd toepast, niet met je oor."),
        ]),
        dict(kop="'t Kofschip: verleden tijd en deelwoord", blokken=[
            ("p", "<strong>'t Kofschip</strong> is een <strong>ezelsbruggetje</strong>: in dat "
                  "woord zitten precies de medeklinkers t, k, f, s, ch en p."),
            ("fig", svg.kofschip(),
             "Eindigt de stam op t, k, f, s, ch of p, dan -te(n) en -t. Anders -de(n) en -d."),
            ("p", "Werken → werkte, gewerkt (stam op k). Leren → leerde, geleerd (stam op r). "
                  "Fietsen → fietste, gefietst. Een <strong>voltooid deelwoord</strong> eindigt "
                  "nooit op -dt: het is gebeurd, geleerd, gewerkt."),
            ("p", "Daar zit meteen de bekendste valstrik. Na 'is' of 'heeft' staat een voltooid "
                  "deelwoord: <em>'Het is gisteren gebeurd'</em>, met een d. In de tegenwoordige "
                  "tijd is het de stam plus -t: <em>'Dat gebeurt elke week opnieuw.'</em>"),
        ]),
        dict(kop="De tijden van het werkwoord", blokken=[
            ("fig", tabel(["tijd", "hoe je ze maakt", "voorbeeld"], [
                ["onvoltooid tegenwoordige tijd", "stam (+ t) of het hele werkwoord", "ik werk, hij werkt"],
                ["onvoltooid verleden tijd", "stam + -te(n) of -de(n)", "hij fietste, wij leerden, zij speelden"],
                ["voltooid tegenwoordige tijd", "hebben of zijn in de tegenwoordige tijd + deelwoord", "ik heb gelopen, wij hebben gelopen"],
                ["voltooid verleden tijd", "had of was + deelwoord", "ik had mijn huiswerk al gemaakt"],
                ["onvoltooid toekomende tijd", "zullen + het hele werkwoord", "ik zal morgen komen"],
                ["gebiedende wijs of imperatief", "de kale stam, zonder onderwerp", "Sluit de deur."],
            ]), "Met 'heb' krijg je de voltooid tegenwoordige tijd, met 'had' de voltooid verleden tijd."),
        ]),
        dict(kop="Klank, woordbeeld en meervoud", blokken=[
            ("fig", svg.lettergrepen(),
             "Korte klank: verdubbelen (man → mannen). Lange klank: verenkelen (maan → manen)."),
            ("p", "'Manen' zijn de haren van een paard; 'mannen' zijn mensen. Eén letter "
                  "verschil, een andere betekenis."),
            ("p", "Sommige woorden hebben een <strong>veranderlijk woordbeeld</strong>: je hoort "
                  "iets anders dan je schrijft. Bij <em>hond</em> hoor je een t maar schrijf je "
                  "een d (honden), bij <em>web</em> hoor je een p maar schrijf je een b (webben), "
                  "bij <em>huis</em> wordt de s een z (huizen). Bij <em>boek</em> verandert er "
                  "niets: dat is een vast woordbeeld. Maak het woord langer, dan hoor je welke "
                  "letter je nodig hebt."),
        ]),
        dict(kop="Trema, apostrof, koppelteken en hoofdletters", blokken=[
            ("fig", tabel(["teken", "wanneer", "voorbeelden"], [
                ["trema (twee puntjes)", "als twee klinkers anders samen gelezen zouden worden", "zeeën, knieën, ruïne"],
                ["apostrof", "meervoud of verkleinwoord na een losse a, i, o, u of y", "foto's, taxi's, baby's, baby'tje, tv'tje"],
                ["koppelteken", "bij klinkerbotsing in een samenstelling", "zee-eend, auto-ongeluk, na-apen"],
                ["hoofdletter", "zinsbegin, namen, talen, landen, plaatsen", "Nederlands, België, Antwerpen — maar maandag klein"],
            ]), "Ik spreek Frans met mijn Franse buurvrouw: talen en afleidingen van landennamen krijgen een hoofdletter."),
            ("p", "Tussen de delen van een <strong>samenstelling</strong> staat geen spatie: "
                  "schoolreglement, handdoek, voetbalclub. Dat is het verschil met het Engels."),
        ]),
        dict(kop="Leestekens", blokken=[
            ("p", "Leestekens plaatsen heet <strong>interpunctie</strong>. Een zin die juist "
                  "<strong>geïnterpungeerd</strong> is, heeft al haar leestekens op de juiste "
                  "plaats staan."),
            ("fig", tabel(["leesteken", "waarvoor"], [
                ["punt", "sluit een mededelende zin af"],
                ["vraagteken", "sluit een vraag af"],
                ["uitroepteken", "sluit een uitroep of een bevel af"],
                ["komma", "scheidt zinsdelen en deelzinnen: 'Als het morgen regent, blijven we thuis.'"],
                ["dubbele punt", "kondigt een opsomming of een citaat aan"],
                ["aanhalingstekens", "rond een letterlijk citaat: Hij zei: 'Ik kom morgen.'"],
                ["spatie", "staat tussen woorden, niet binnen een samenstelling"],
            ]), "'Kom je mee, of blijf je hier?' — hoofdletter, komma tussen de twee zinnen, vraagteken."),
            ("weetje", "Een <strong>spellingcontrole</strong> markeert alleen woorden die niet "
                       "bestaan, zoals 'neiuwe'. 'Het is gisteren gebeurt', 'hij word morgen "
                       "veertien' en 'ik leg al een uur in bed' blijven onaangeroerd: die woorden "
                       "bestaan alle drie. Liggen doe je zelf, leggen doe je met iets anders. "
                       "Lees je tekst dus altijd zelf na op werkwoordsvormen."),
        ]),
    ],
    onthoud=[
        "Stam = werkwoord min -en. Hij/zij/het: stam + t; 'jij' áchter het werkwoord: geen t.",
        "'t Kofschip (t, k, f, s, ch, p): -te en -t; anders -de en -d.",
        "Een voltooid deelwoord eindigt nooit op -dt: gebeurd, geleerd, gewerkt.",
        "Korte klank verdubbelen (mannen), lange klank verenkelen (manen).",
        "Trema bij zeeën en knieën, apostrof bij foto's en baby'tje, koppelteken bij zee-eend.",
        "Zes tijden: ottt, ovt, vtt, vvt, otkt en de gebiedende wijs.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["woordsoorten-en-woordvorming"] = dict(
    vak=VAK, niveau=SPARK, titel="Woordsoorten en woordvorming",
    onder="Welke soort elk woord is, hoe woorden gemaakt worden en wat ze betekenen.",
    secties=[
        dict(kop="De woordsoorten", blokken=[
            ("fig", tabel(["woordsoort", "wat het doet", "voorbeelden"], [
                ["zelfstandig naamwoord", "noemt een ding, een wezen of een begrip", "hond, fiets, fietser, vriendschap"],
                ["bijvoeglijk naamwoord", "zegt iets over een zelfstandig naamwoord", "de oude toren, een snelle fiets"],
                ["werkwoord", "noemt een handeling of een toestand", "fietsen, zijn, worden"],
                ["lidwoord", "er zijn er maar drie", "de, het, een"],
                ["voornaamwoord", "vervangt of bepaalt een naamwoord", "ik, mijn, deze, wie"],
                ["voegwoord", "verbindt woorden of zinnen", "en, of, maar, want, omdat, hoewel"],
                ["voorzetsel", "geeft plaats, tijd of richting", "op, onder, tussen, met"],
                ["telwoord", "geeft een aantal of een rangorde", "drie, tien, eerste"],
                ["bijwoord", "zegt iets over een werkwoord, een bijvoeglijk naamwoord of de zin", "snel, gisteren, daar (een bijwoord van plaats)"],
                ["tussenwerpsel", "drukt een gevoel of een reactie uit", "oei, hè, hoera"],
            ]), "Zet je 'de' of 'het' voor een woord, dan heb je meestal een zelfstandig naamwoord te pakken."),
            ("p", "Let op het verschil tussen een <strong>bijvoeglijk naamwoord</strong> en een "
                  "<strong>bijwoord</strong>: 'een snelle fiets' hoort bij het naamwoord, 'hij "
                  "fietst snel' hoort bij het werkwoord. Hetzelfde woord kan dus in de ene zin "
                  "een andere woordsoort zijn dan in de andere: 'een harde bal' tegenover 'hij "
                  "loopt hard'. Kijk altijd naar de zin."),
            ("p", "Soms staat een bijvoeglijk naamwoord op de plaats van het naamwoord: 'De jonge "
                  "speelt beter dan de oude.' Dan is het <em>zelfstandig gebruikt</em>."),
        ]),
        dict(kop="De voornaamwoorden", blokken=[
            ("fig", tabel(["soort", "wat het doet", "voorbeelden"], [
                ["persoonlijk", "vervangt een persoon of zaak", "ik, jij, hij, zij, wij, hem, ons"],
                ["bezittelijk", "zegt van wie iets is", "mijn, jouw, zijn, haar, ons, hun"],
                ["aanwijzend", "wijst iets aan", "deze, dit (dichtbij), die, dat (verder weg)"],
                ["vragend", "vraagt naar een persoon of zaak", "wie, wat, welke, wiens"],
            ]), "In 'Wat een lawaai!' staat een vragend voornaamwoord in een uitroep."),
            ("p", "Hoort het voornaamwoord bij een zelfstandig naamwoord — 'Deze fiets is nieuw' "
                  "— dan is het <strong>bijvoeglijk</strong> gebruikt. Staat het er alleen — "
                  "'Deze is nieuw' — dan is het <strong>zelfstandig</strong> gebruikt."),
        ]),
        dict(kop="Samenstellingen en afleidingen", blokken=[
            ("p", "Een <strong>samenstelling</strong> bestaat uit twee (of meer) bestaande "
                  "woorden: voetbal, tandarts, boekentas. 'Voetbalclub' bestaat zelfs uit drie: "
                  "voet, bal en club."),
            ("p", "Een <strong>afleiding</strong> is een grondwoord met een "
                  "<strong>voorvoegsel</strong> ervoor of een <strong>achtervoegsel</strong> "
                  "erachter: on-vriendelijk, vriend-schap, en van bakken maak je met -er een <strong>bakker</strong>."),
            ("fig", svg.woordvolgorde([
                ("voorvoegsel", "on-", svg.FOREST),
                ("grondwoord", "vriend", svg.DARK),
                ("achtervoegsel", "-elijk", svg.AMBER),
            ]), "Onvriendelijk: voorvoegsels als on-, ver-, be- en her-, achtervoegsels als -schap, -heid, -ing en -er."),
            ("p", "Dat is handig bij het lezen: 'onbereikbaar' is on + bereik + baar, dus niet te "
                  "bereiken. De betekenis van een <strong>onbekend woord</strong> kan je zo vaak "
                  "raden aan de delen waaruit het bestaat."),
            ("p", "Ook de <strong>uitgang</strong> hoort hierbij: in 'werkte' is werk de stam en "
                  "-te de uitgang die er de verleden tijd van maakt."),
        ]),
        dict(kop="Meervoud en verkleinwoord", blokken=[
            ("p", "Naast het gewone meervoud op -en of -s zijn er onregelmatige vormen op "
                  "<strong>-eren</strong>: kind → kinderen, ei → eieren, blad → bladeren, lied → "
                  "liederen."),
            ("fig", svg.verkleinwoorden(),
             "Vijf uitgangen: -je, -tje, -pje, -etje en -kje. Na een m volgt -pje: boompje."),
            ("p", "Elk <strong>verkleinwoord</strong> is onzijdig: het is 'de bal', maar 'het "
                  "balletje'."),
        ]),
        dict(kop="Synoniemen en homoniemen", blokken=[
            ("p", "<strong>Synoniemen</strong> betekenen ongeveer hetzelfde: mooi, fraai, "
                  "prachtig, schitterend. Je gebruikt ze om je tekst levendig te maken en "
                  "herhaling te vermijden. 'Lelijk' is net het tegengestelde."),
            ("p", "Een <strong>homoniem</strong> heeft dezelfde vorm maar twee heel verschillende "
                  "betekenissen: een <em>bank</em> om op te zitten of een bank waar je geld "
                  "haalt, een <em>slot</em> op de deur of het slot van een tekst, een "
                  "<em>kussen</em> op de zetel of iemand kussen. Welke betekenis geldt, leid je "
                  "af uit de zin."),
            ("weetje", "Woordsoorten kennen is geen doel op zich: het is ondersteunende kennis. "
                       "Wie ziet dat 'wordt' een werkwoord is, weet welke spellingregel geldt; "
                       "wie het onderwerp vindt, controleert zijn zinsbouw."),
        ]),
    ],
    onthoud=[
        "Tien woordsoorten, van zelfstandig naamwoord tot tussenwerpsel.",
        "Voornaamwoorden: persoonlijk, bezittelijk, aanwijzend en vragend; bijvoeglijk of zelfstandig gebruikt.",
        "Samenstelling = twee woorden; afleiding = grondwoord + voor- of achtervoegsel.",
        "Kind, ei, blad en lied krijgen -eren in het meervoud.",
        "Vijf verkleinuitgangen; elk verkleinwoord krijgt 'het'.",
        "Synoniem = ongeveer dezelfde betekenis; homoniem = dezelfde vorm, andere betekenis.",
    ],
)

# ---------------------------------------------------------------------------

BUNDELS["zinsdelen-zinssoorten-en-congruentie"] = dict(
    vak=VAK, niveau=SPARK, titel="Zinsdelen, zinssoorten en congruentie",
    onder="Een zin uit elkaar halen: wie doet wat, en hoe de delen bij elkaar passen.",
    secties=[
        dict(kop="De persoonsvorm en het onderwerp", blokken=[
            ("p", "De <strong>persoonsvorm</strong> is het werkwoord dat van vorm verandert als "
                  "je de zin in een andere tijd zet: 'hij loopt' wordt 'hij liep'. Een tweede "
                  "trucje: maak er een ja-neevraag van. Het werkwoord dat dan vooraan springt, is "
                  "de persoonsvorm. In 'De directeur heeft de brief gisteren ondertekend' is dat "
                  "'heeft'; het deelwoord 'ondertekend' verandert niet mee."),
            ("p", "Het <strong>onderwerp</strong> vind je met <em>wie of wat</em> plus de "
                  "persoonsvorm. Wie wast? De buurvrouw. Het onderwerp mag gerust achter de "
                  "persoonsvorm staan: in 'Op zaterdag traint de ploeg in Genk' is 'de ploeg' "
                  "nog altijd het onderwerp, en in 'Er komen drie gasten' is dat 'drie gasten' "
                  "— 'er' vult alleen de eerste plaats op."),
        ]),
        dict(kop="De andere zinsdelen", blokken=[
            ("fig", svg.zinsdelen([
                ("Tom", "onderwerp", svg.FOREST),
                ("geeft", "persoonsvorm", svg.DARK),
                ("zijn zus", "meewerkend voorwerp", svg.AMBER),
                ("een boek", "lijdend voorwerp", svg.FOREST),
            ]), "Wie of wat geeft Tom? Een boek. Aan wie? Aan zijn zus."),
            ("fig", tabel(["zinsdeel", "vraag die je stelt", "voorbeeld"], [
                ["onderwerp", "wie of wat + persoonsvorm?", "De buurvrouw wast haar auto."],
                ["lijdend voorwerp", "wie of wat + persoonsvorm + onderwerp?", "Tom geeft een boek."],
                ["meewerkend voorwerp", "aan wie of voor wie? (je kan er 'aan' voor zetten)", "Hij schrijft zijn oma een kaartje."],
                ["bijwoordelijke bepaling", "waar, wanneer, hoe, waarom?", "Gisteren fietste hij rustig naar school."],
            ]), "Niet elke zin heeft een lijdend voorwerp: 'hij slaapt' heeft er geen."),
            ("p", "Pas op met bepalingen die op een meewerkend voorwerp lijken. In 'De kinderen "
                  "kregen van de directeur een diploma' is er géén meewerkend voorwerp: de "
                  "kinderen zijn het onderwerp, het diploma het lijdend voorwerp, en 'van de "
                  "directeur' zegt van wie ze het kregen."),
        ]),
        dict(kop="Doen-relatie en zijn-relatie", blokken=[
            ("p", "Het <strong>gezegde</strong> zegt wat er over het onderwerp beweerd wordt. Er "
                  "zijn twee soorten."),
            ("fig", tabel(["soort", "wat er gebeurt", "voorbeeld"], [
                ["doen-relatie", "het onderwerp voert een handeling uit", "Mijn zus repareert fietsen."],
                ["zijn-relatie", "het onderwerp wordt gelijkgesteld aan iets", "Mijn zus is verpleegkundige."],
            ]), "Bij een zijn-relatie doet het onderwerp niets: het krijgt een naam of een eigenschap."),
            ("p", "De werkwoorden van de zijn-relatie zijn <strong>zijn</strong>, "
                  "<strong>worden</strong>, <strong>blijven</strong>, blijken, lijken, schijnen "
                  "en heten. Wat erbij hoort, is het <strong>naamwoordelijk deel</strong>: in "
                  "'Het weer wordt beter' is dat 'beter', in 'Hij is de beste van de klas' is dat "
                  "'de beste van de klas'. In 'Mijn broer blijft rustig onder druk' vormen "
                  "'blijft' en 'rustig' samen het gezegde; 'onder druk' is een bepaling."),
        ]),
        dict(kop="Zinssoorten", blokken=[
            ("fig", tabel(["zinssoort", "voorbeeld"], [
                ["mededelend", "Hij komt morgen mee."],
                ["vragend", "Komt hij morgen mee?"],
                ["bevelend", "Sluit het raam."],
                ["uitroepend", "Wat een lawaai maakt die machine!"],
                ["bevestigend", "Ik heb veel tijd."],
                ["ontkennend", "Ik heb geen tijd."],
            ]), "Woorden als niet, geen, nooit en niemand maken een zin ontkennend; 'altijd' bevestigt net."),
            ("p", "Een <strong>bevelende</strong> zin heeft meestal geen onderwerp: 'Kom "
                  "binnen.' Soms is de vorm vragend maar de bedoeling een verzoek: 'Zou je het "
                  "raam even willen sluiten?' klinkt beleefder dan een bevel."),
            ("p", "Tel de persoonsvormen om te weten hoeveel zinnen er in elkaar zitten. Eén "
                  "persoonsvorm is een <strong>enkelvoudige</strong> zin. Twee of meer maken er "
                  "een <strong>samengestelde</strong> zin van: 'Hij bleef thuis omdat hij ziek "
                  "was' (bleef, was), 'Toen hij thuiskwam, was het al donker', 'Ze zei dat ze "
                  "later zou komen'. In 'Ik wist niet dat je ziek was, dus ik belde niet' staan "
                  "er drie: wist, was en belde."),
        ]),
        dict(kop="Congruentie", blokken=[
            ("p", "<strong>Congruentie</strong> betekent dat het onderwerp en de persoonsvorm bij "
                  "elkaar passen in enkelvoud of meervoud: 'de hond blaft', 'de honden blaffen', "
                  "'de leerlingen wachten op de bus'."),
            ("fig", svg.persoonsvormen([
                ("de hond|de leerling|de doos met boeken", "staat, blaft", svg.FOREST),
                ("de honden|de leerlingen|mijn ouders", "staan, blaffen", svg.AMBER),
            ]), "Zoek eerst het onderwerp: de rest van de zin mag je niet in de war brengen."),
            ("p", "Daar gaat het vaak mis bij lange zinnen. In 'De doos met boeken staat in de "
                  "gang' is het onderwerp 'de doos', enkelvoud; 'met boeken' is maar een "
                  "bepaling. Ook een groep mensen die je als één geheel noemt, is enkelvoud: de "
                  "regering heeft, de groep kinderen speelt, de rij wachtenden staat. En 'een van "
                  "de leerlingen heeft het gezien' blijft enkelvoud, want het onderwerp is 'een'."),
            ("weetje", "Zinsontleding is geen doel op zich. Het helpt je bij het schrijven: wie "
                       "bij een lange zin het onderwerp terugvindt, ziet meteen of de "
                       "persoonsvorm klopt."),
        ]),
    ],
    onthoud=[
        "De persoonsvorm verandert mee als je de tijd verandert of er een vraag van maakt.",
        "Onderwerp: wie of wat + persoonsvorm. Lijdend voorwerp: daar nog eens het onderwerp bij.",
        "Voor een meewerkend voorwerp kan je 'aan' of 'voor' zetten.",
        "Doen-relatie: het onderwerp handelt. Zijn-relatie: zijn, worden, blijven + naamwoordelijk deel.",
        "Eén persoonsvorm = enkelvoudige zin; twee of meer = samengestelde zin.",
        "Congruentie: zoek het onderwerp, ook in 'de doos met boeken staat'.",
    ],
)

# -*- coding: utf-8 -*-
"""De twee overige bundels voor geschiedenis, met eigen tekeningen."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel
tabel = bundel.tabel

BUNDELS = {}

BUNDELS["van-de-prehistorie-tot-de-romeinen"] = dict(
    vak="Geschiedenis", titel="Van de prehistorie tot de Romeinen",
    onder="Van de eerste stenen werktuigen tot de Romeinse wegen in onze streken.",
    secties=[
        dict(kop="Wat is de prehistorie?", blokken=[
            ("p", "<strong>Prehistorie</strong> betekent letterlijk: de tijd vóór de geschiedenis. "
                  "Niet omdat er toen niets gebeurde, maar omdat er nog niets werd opgeschreven. "
                  "Er zijn dus geen brieven, geen boeken, geen namen van mensen. Alles wat we over "
                  "die tijd weten, komt uit de grond: werktuigen, botten, resten van vuur, graven."),
            ("p", "Daarom is de <strong>archeoloog</strong> voor de prehistorie de enige getuige die "
                  "we hebben. Hij graaft voorzichtig laagje per laagje af en noteert precies waar "
                  "hij elk stukje vindt, want die plaats vertelt evenveel als het voorwerp zelf."),
            ("fig", svg.stappen(["steentijd", "bronstijd", "ijzertijd"]),
             "De prehistorie wordt ingedeeld naar het materiaal waarvan de mensen hun gereedschap maakten."),
            ("p", "Zodra mensen begonnen te schrijven, stopt de prehistorie en begint de "
                  "<strong>geschiedenis</strong>. Dat gebeurde niet overal op hetzelfde moment: in "
                  "<strong>Mesopotamië</strong> en <strong>Egypte</strong> al rond 3000 v.Chr., "
                  "bij ons pas toen de Romeinen kwamen. De prehistorie duurde hier dus veel langer."),
        ]),
        dict(kop="De oude steentijd: jagen en verzamelen", blokken=[
            ("p", "In de <strong>oude steentijd</strong> trokken mensen van plaats naar plaats. Ze "
                  "jaagden op dieren en verzamelden wat ze vonden: noten, bessen, wortels, eieren. "
                  "Als het voedsel op was, trok de groep verder. Ze volgden dus het voedsel — ze "
                  "reisden niet voor hun plezier."),
            ("p", "Ze sloegen hun kamp graag op <strong>dicht bij water</strong>. Daar konden ze "
                  "drinken en vissen, daar kwamen de dieren drinken zodat je ze makkelijker kon "
                  "bejagen, en over water kon je je met een boomstamboot verplaatsen."),
            ("fig", svg.stenen_werktuigen(),
             "Vuursteen splijt in scherpe schilfers. Aan die afslagvlakjes herken je een bewerkte steen van een gewone."),
            ("p", "We noemen het de steentijd, maar niet alles was van steen. Uit <strong>been</strong> "
                  "en <strong>gewei</strong> maakten ze naalden, harpoenen en priemen; uit "
                  "<strong>hout</strong> speren en stelen. Metaal kenden ze nog niet. Bot en hout "
                  "vergaan alleen sneller in de grond, dus vinden archeologen vooral de stenen terug."),
            ("p", "Een deel van de oude steentijd viel in een <strong>ijstijd</strong>: het was hier "
                  "veel kouder dan nu. In die koude vlakten leefde de <strong>mammoet</strong>, een "
                  "harig dier met lange gekromde slagtanden, familie van de olifant. De mammoet is "
                  "uitgestorven. Van één dier had een groep vlees, vet, huid én botten om mee te bouwen."),
            ("weetje", "De hond was het eerste dier dat de mens temde, nog vóór de landbouw begon. "
                       "Wolven die bij de kampen bleven rondhangen, werden over vele generaties honden."),
        ]),
        dict(kop="De nieuwe steentijd: boeren en dorpen", blokken=[
            ("p", "In de <strong>nieuwe steentijd</strong> veranderde alles. Mensen begonnen aan "
                  "<strong>landbouw</strong>: ze zaaiden graan en hielden dieren, zoals schapen, "
                  "geiten, runderen en varkens. Het voedsel kwam nu naar de mens toe in plaats van "
                  "omgekeerd."),
            ("p", "Wie zaait, moet blijven tot het graan rijp is. Daardoor konden mensen "
                  "<strong>op één plaats blijven wonen</strong>, en zo ontstonden de eerste "
                  "<strong>dorpen</strong>: huizen van hout, leem en stro, akkers eromheen, en een "
                  "voorraad voor de winter."),
            ("fig", svg.nomadisch_sedentair(),
             "Rondtrekken achter het voedsel aan, of blijven en het voedsel zelf kweken. Dat is het grote verschil tussen de oude en de nieuwe steentijd."),
            ("p", "Met vaste dorpen kwamen er ook nieuwe dingen: <strong>aardewerk</strong> om in te "
                  "koken en te bewaren, <strong>weefgetouwen</strong> voor kleren van wol en vlas, en "
                  "geslepen stenen bijlen om bos te rooien. En omdat niet iedereen meer op het land "
                  "hoefde te werken, konden sommigen zich toeleggen op één vak."),
        ]),
        dict(kop="Graven van steen en van aarde", blokken=[
            ("p", "De mensen van de nieuwe steentijd begroeven hun doden met zorg. Soms bouwden ze "
                  "daarvoor een <strong>megalietgraf</strong>: een grafkamer van enorme staande "
                  "stenen met platte dekstenen erop. Bij ons heet zo'n graf een "
                  "<strong>hunebed</strong>. In Drenthe, in Nederland, staan er nog tientallen."),
            ("p", "Later, vooral in de bronstijd, wierp men boven een graf een heuvel van aarde op: "
                  "een <strong>grafheuvel</strong>. Op heidegebieden liggen er nog altijd, als lage "
                  "ronde bulten in het landschap. Wie erin werd begraven, kreeg vaak voorwerpen mee."),
            ("fig", svg.oude_graven(),
             "Zulke graven zijn vaak het enige wat er van een hele gemeenschap overblijft. Ze vragen veel mensen en veel samenwerking: één deksteen weegt tonnen."),
        ]),
        dict(kop="Brons en ijzer", blokken=[
            ("p", "Op een dag ontdekten mensen dat je uit bepaalde stenen <strong>metaal</strong> kon "
                  "smelten. Zuiver koper is nog te zacht voor gereedschap, maar meng je koper met "
                  "<strong>tin</strong>, dan krijg je <strong>brons</strong>: veel harder, en je kan "
                  "het in een vorm gieten. Daarmee begint de <strong>bronstijd</strong>."),
            ("p", "Koper en tin liggen zelden in dezelfde streek. Wie brons wilde, moest dus "
                  "<strong>ruilhandel</strong> drijven over grote afstanden. Brons was duur, en wie "
                  "een bronzen zwaard had, liet dat zien."),
            ("p", "Daarna komt de <strong>ijzertijd</strong>. IJzer is nog harder dan brons, en "
                  "ijzererts zit bijna overal in de grond — ook bij ons, als moerasijzererts. Je moet "
                  "het alleen veel heter stoken en smeden in plaats van gieten. Daardoor werd goed "
                  "gereedschap betaalbaar voor gewone boeren."),
            ("fig", tabel(["Tijdvak", "Waarvan het gereedschap", "Wat er nieuw was"], [
                ["steentijd", "steen, been, gewei en hout", "vuur, jacht, later landbouw en dorpen"],
                ["bronstijd", "brons: koper gemengd met tin", "metaal gieten, handel over grote afstand, grafheuvels"],
                ["ijzertijd", "ijzer, gesmeed", "sterk gereedschap voor iedereen, grotere akkers"],
            ]), "De volgorde ligt vast: eerst steen, dan brons, dan ijzer. Elk tijdvak is genoemd naar het hardste materiaal dat de mensen toen konden bewerken."),
        ]),
        dict(kop="De eerste kunst", blokken=[
            ("p", "Diep in grotten schilderden mensen dieren op de wand: oerrunderen, paarden, herten. "
                  "Ze gebruikten oker voor geel en rood, en houtskool voor zwart. Soms legden ze hun "
                  "hand op de wand en bliezen er verf omheen."),
            ("fig", svg.grotschildering(),
             "Hier nagetekend. De echte schilderingen, zoals in Lascaux, zijn ongeveer 17 000 jaar oud."),
            ("p", "Waarom ze het deden, weten we niet zeker: er staat geen uitleg bij. Dat is meteen "
                  "het lastige aan de prehistorie — je kan wat je vindt alleen maar proberen te "
                  "begrijpen, niemand kan het je navertellen."),
        ]),
        dict(kop="Mesopotamië: hier begint het schrift", blokken=[
            ("p", "Tussen de rivieren de Eufraat en de Tigris lag <strong>Mesopotamië</strong>. De "
                  "naam betekent letterlijk 'het land tussen de rivieren'. Met water uit die rivieren "
                  "bevloeide men de akkers, en op die oogsten groeiden de eerste echte "
                  "<strong>steden</strong>."),
            ("fig", svg.irrigatie(),
             "Bevloeiing vraagt kanalen, en kanalen vragen mensen die samen graven, onderhouden en het water eerlijk verdelen. Daaruit groeit vanzelf een bestuur."),
            ("p", "In die steden werd zoveel verhandeld en opgeslagen dat men het moest bijhouden. "
                  "Daarvoor bedachten ze het <strong>spijkerschrift</strong>: met een rietstengel "
                  "drukte men wigvormige tekens in een tablet van natte klei. Die klei droogde hard "
                  "op, en daarom liggen er vandaag nog duizenden tabletten in musea."),
            ("p", "Mesopotamië en Egypte zijn dus de plaatsen waar het schrift voor het eerst werd "
                  "gebruikt. Vanaf dat moment spreken we niet meer van prehistorie, maar van geschiedenis."),
            ("fig", svg.ziggurat(),
             "Midden in een Mesopotamische stad stond een ziggurat: een tempeltoren in trappen, gebouwd van in de zon gedroogde kleitegels."),
        ]),
        dict(kop="Egypte en de Nijl", blokken=[
            ("p", "Egypte lag rond de <strong>Nijl</strong>. Die rivier overstroomde elk jaar en liet "
                  "vruchtbaar slib achter, waardoor er genoeg graan groeide om een heel rijk te voeden. "
                  "Zonder de Nijl was er in die woestijn niets geweest. De Nijl was ook de snelweg van "
                  "Egypte: alles ging per boot."),
            ("p", "Aan het hoofd stond de <strong>farao</strong>. Hij was koning én werd als een god "
                  "vereerd. Voor de farao's werden de <strong>piramides</strong> gebouwd, als graf. "
                  "De bekendste staan bij <strong>Gizeh</strong>, vlak bij de hoofdstad Caïro."),
            ("fig", svg.piramides(),
             "De grootste piramide, die van Cheops, is ongeveer 4 500 jaar oud en werd met de hand gebouwd uit miljoenen steenblokken."),
            ("p", "De Egyptenaren schreven met <strong>hiërogliefen</strong>: kleine tekeningen die "
                  "samen woorden vormen. Sommige tekens staan voor een klank, andere voor een heel "
                  "woord. Ze schreven op steen, en op papyrus, een soort papier van rietstengels."),
            ("fig", svg.hierogliefen(),
             "Een cartouche: het ovale kader waarin de naam van een koning werd gezet."),
        ]),
        dict(kop="De Grieken", blokken=[
            ("p", "In <strong>Griekenland</strong> ontstonden <strong>stadstaten</strong>: een stad "
                  "met het land eromheen, elk met een eigen bestuur en een eigen leger. "
                  "<strong>Athene</strong> en Sparta zijn de bekendste. Athene is vandaag nog altijd "
                  "de hoofdstad van Griekenland."),
            ("p", "In Athene mochten de burgers zelf meestemmen over de stad. Dat was toen heel "
                  "bijzonder, maar het was nog geen democratie zoals wij die kennen: alleen de "
                  "<strong>vrije mannen die burger waren</strong> mochten stemmen. Vrouwen, slaven en "
                  "vreemdelingen telden niet mee, en dat was het grootste deel van de bevolking."),
            ("fig", svg.griekse_tempel(),
             "Het Parthenon in Athene. Een Griekse tempel rust op zuilen, met bovenaan een driehoekig fronton. Die bouwstijl zie je vandaag nog aan gerechtsgebouwen en musea."),
            ("p", "De Grieken bedachten ook het <strong>theater</strong>: toneelstukken in een "
                  "openluchttheater, waar de hele stad naar tragedies en komedies kwam kijken. En de "
                  "<strong>Olympische Spelen</strong>, om de vier jaar gehouden in Olympia, ter ere "
                  "van hun goden. Daar komen onze Olympische Spelen vandaan."),
        ]),
        dict(kop="Het Romeinse Rijk", blokken=[
            ("p", "Het Romeinse Rijk had <strong>Rome</strong> als hoofdstad en groeide uit tot een "
                  "rijk rond de hele <strong>Middellandse Zee</strong>. Die zee lag er middenin, en "
                  "dat maakte reizen en handel drijven veel eenvoudiger dan over land. De Romeinen "
                  "noemden haar zelfs <em>mare nostrum</em>: onze zee."),
            ("p", "De Romeinen spraken <strong>Latijn</strong> en schreven met de letters die wij nu "
                  "nog gebruiken: het <strong>Latijnse alfabet</strong>. Ook deze leerbundel is "
                  "ermee geschreven."),
            ("p", "<strong>Julius Caesar</strong> was een beroemde veldheer die grote gebieden "
                  "veroverde en erover schreef. Hij was geen keizer. Zijn aangenomen zoon "
                  "<strong>Augustus</strong> kwam na hem aan de macht en geldt als de "
                  "<strong>eerste keizer</strong> van Rome."),
            ("weetje", "Op de munten stond de kop van de keizer. Zo wist iedereen in het hele rijk wie "
                       "er aan de macht was, ook wie niet kon lezen. Een munt was dus ook een bericht."),
            ("fig", svg.standenpiramide([
                ("keizer", "één man aan de top"),
                ("rijke burgers", "grond, bestuur, leger"),
                ("gewone burgers", "handel en ambacht"),
                ("slaven", "eigendom van een ander"),
            ]),
             "Een slaaf was geen werknemer met loon: hij was eigendom van iemand anders en kon verkocht worden. Vaak waren het krijgsgevangenen. Een groot deel van het werk in het rijk werd door slaven gedaan."),
        ]),
        dict(kop="Wonen en leven bij de Romeinen", blokken=[
            ("p", "Midden in een Romeinse stad lag het <strong>forum</strong>: het plein met de markt, "
                  "de tempels en de gebouwen van het bestuur. Daar dreef je handel, daar hoorde je het "
                  "nieuws, daar werd recht gesproken."),
            ("p", "De Romeinen bouwden ook wat een stad verder nodig heeft: <strong>aquaducten</strong> "
                  "die vers water van ver aanvoerden, en <strong>thermen</strong>, openbare badhuizen "
                  "waar iedereen ging baden, sporten en praten."),
            ("fig", svg.aquaduct(),
             "Het water liep bovenin, in een goot met een héél lichte helling, soms tientallen kilometers ver."),
            ("p", "Voor de ontspanning waren er de <strong>amfitheaters</strong>: ronde gebouwen met "
                  "oplopende zitrijen rond een arena. Het Colosseum in Rome is het bekendste. Er was "
                  "plaats voor tienduizenden toeschouwers."),
            ("fig", svg.amfitheater(),
             "Rond, zodat iedereen van overal goed zicht heeft op de arena in het midden. Onze voetbalstadions zijn nog altijd zo gebouwd."),
            ("p", "Woonden alle Romeinen in grote villa's? Nee. Alleen de rijken. In de steden woonden "
                  "gewone mensen dicht op elkaar in <strong>insulae</strong>: hoge huurblokken van "
                  "verschillende verdiepingen, met winkeltjes op de begane grond. Hoe hoger je woonde, "
                  "hoe goedkoper en hoe gevaarlijker."),
        ]),
        dict(kop="De Romeinen in onze streken", blokken=[
            ("p", "Vóór de Romeinen kwamen, woonden hier volkeren die bij de <strong>Kelten</strong> "
                  "horen. Ze leefden in boerderijen en versterkte dorpen, bewerkten ijzer en dreven "
                  "handel. De stammen in onze streken noemde Julius Caesar de <strong>Belgae</strong>."),
            ("p", "Caesar veroverde dit gebied en schreef er zelf een boek over. Onze streken kregen "
                  "de naam <strong>Gallia Belgica</strong>, en daar komt de naam België vandaan."),
            ("p", "Het leger moest snel van de ene plek naar de andere kunnen. Daarvoor legden de "
                  "Romeinen <strong>heirbanen</strong> aan: stenen wegen, zo recht mogelijk, want dat "
                  "is de kortste weg. Soldaten, post en handelswaar gingen erover."),
            ("fig", svg.heirbaan(),
             "Vier lagen op elkaar, en bovenaan bol gelegd zodat het regenwater naar de kant liep. Daarom lagen sommige stukken er eeuwen later nog."),
            ("p", "Rijke Romeinen bouwden hier grote landbouwbedrijven, de <strong>villa's</strong>: "
                  "een stenen woonhuis met stallen, schuren en akkers eromheen. Het graan en het vlees "
                  "gingen naar de steden en naar het leger."),
            ("weetje", "De Romeinen brachten hier steden, stenen wegen, badhuizen, munten, wijn en het "
                       "Latijn. Veel Nederlandse woorden komen er nog van: muur, straat, keuken, wijn, "
                       "kelder, venster, kaas en zolder."),
        ]),
    ],
    onthoud=[
        "Prehistorie = de tijd vóór het schrift. Alles wat we erover weten, komt uit de grond.",
        "De volgorde is: steentijd, bronstijd, ijzertijd — genoemd naar het materiaal van het gereedschap.",
        "In de steentijd werkte men met steen, been, gewei en hout; metaal kende men nog niet.",
        "Oude steentijd: rondtrekken, jagen en verzamelen, wonen dicht bij water. De mammoet leefde in de ijstijd.",
        "Nieuwe steentijd: landbouw, vaste dorpen. De hond was het eerste getemde dier.",
        "Hunebed = grafkamer van grote stenen; grafheuvel = een heuvel aarde over een graf.",
        "Brons = koper gemengd met tin. IJzer is harder en zit bijna overal in de grond.",
        "Het schrift begon in Mesopotamië (spijkerschrift) en Egypte (hiërogliefen).",
        "Egypte dankte alles aan de Nijl; de farao's kregen piramides als graf, zoals in Gizeh.",
        "In Athene mochten alleen vrije mannen die burger waren meestemmen.",
        "De Grieken bouwden tempels op zuilen en bedachten het theater en de Olympische Spelen.",
        "Rome was de hoofdstad; de Middellandse Zee lag midden in het rijk. De Romeinen spraken Latijn.",
        "Caesar was veldheer, Augustus was de eerste keizer. Een slaaf was geen vrij mens.",
        "Alleen de rijken woonden in villa's; in de stad woonde men in hoge huurblokken.",
        "De Romeinen legden heirbanen aan voor hun leger. Onze streken heetten Gallia Belgica.",
    ])


BUNDELS["van-de-middeleeuwen-tot-nu"] = dict(
    vak="Geschiedenis", titel="Van de middeleeuwen tot nu",
    onder="Van ridders en kloosters, via stoom en mijnen, tot de wereld van vandaag.",
    secties=[
        dict(kop="De middeleeuwen", blokken=[
            ("p", "Na de val van Rome viel het rijk uiteen in kleine gebieden. Er was geen keizer meer "
                  "die alles bestuurde, en ook geen leger dat overal de orde hield. Wie bescherming "
                  "wilde, moest die dichter bij huis zoeken."),
            ("p", "Zo ontstond het <strong>leenstelsel</strong>. Een <strong>leenheer</strong> gaf "
                  "grond aan iemand die hem daarvoor trouw en hulp in de oorlog beloofde. Die man heet "
                  "een leenman, en hij kon op zijn beurt weer stukken uitlenen. Zo hing alles aan "
                  "elkaar van afspraken tussen heren en hun leenmannen."),
            ("fig", svg.burcht(),
             "Een burcht op een heuvel of aan een rivier: van daaruit zie je de vijand van ver aankomen, je vecht bergaf, en water is een extra muur. Daarom koos men die plaatsen, niet voor het uitzicht."),
            ("p", "De meeste mensen waren <strong>boer</strong>. Zij werkten het land van de heer, "
                  "gaven een deel van de oogst af en verlieten hun dorp bijna nooit. Lezen en schrijven "
                  "konden ze niet; dat was voorbehouden aan een kleine groep."),
        ]),
        dict(kop="Steden, ambachten en de pest", blokken=[
            ("p", "In Vlaanderen groeiden de steden rijk door de <strong>lakenhandel</strong>: wol uit "
                  "Engeland werd hier tot fijn laken geweven en over heel Europa verkocht. Gent, Brugge "
                  "en Ieper hoorden bij de grootste steden van Europa."),
            ("p", "Wie een <strong>ambacht</strong> uitoefende — een beroep waarbij je met de hand iets "
                  "maakt, zoals smid, bakker, wever of schoenmaker — hoorde bij een "
                  "<strong>gilde</strong>. Dat gilde bepaalde wie het vak mocht uitoefenen, bewaakte de "
                  "kwaliteit, legde de prijzen vast en hielp leden die ziek werden."),
            ("weetje", "In 1302 versloegen Vlaamse stedelingen te voet een Frans ridderleger bij "
                       "Kortrijk: de Guldensporenslag. Dat voetvolk uit de steden won het van ridders "
                       "te paard, en dat was in die tijd hoogst ongewoon."),
            ("p", "Al die handel bracht ook iets mee wat niemand wilde. In de "
                  "<strong>14de eeuw</strong> trof de <strong>pest</strong> Europa: een ziekte die met "
                  "schepen en karavanen meereisde en zich in de volle steden razendsnel verspreidde. "
                  "Ongeveer een derde van alle inwoners van Europa stierf eraan. Men wist toen nog niet "
                  "waardoor de ziekte kwam en kon er dus bijna niets tegen doen."),
        ]),
        dict(kop="Kerk, klooster en kathedraal", blokken=[
            ("p", "De kerk speelde in de middeleeuwen een rol in bijna alles: geboorte, huwelijk, "
                  "feestdagen, school, zorg voor zieken en armen. In de <strong>kloosters</strong> "
                  "werd gebeden en gewerkt, en er werd ook geleerd."),
            ("p", "In het <strong>scriptorium</strong> van een klooster schreven <strong>monniken</strong> "
                  "boeken over, letter voor letter, met de hand. Aan één boek werkte iemand soms een "
                  "jaar. Daarom waren boeken zeldzaam en duur, en bezat bijna niemand er een."),
            ("fig", svg.verlucht_handschrift(),
             "Een verlucht handschrift: de beginletter van een hoofdstuk werd groot en met kleur versierd, soms met bladgoud."),
            ("p", "In de steden bouwde men grote kerken. Een <strong>kathedraal</strong> is de kerk "
                  "waar een <strong>bisschop</strong> zetelt, en dus de belangrijkste kerk van een hele "
                  "streek. Aan zo'n gebouw werd soms meer dan honderd jaar gewerkt: wie begon aan de "
                  "fundering, zag de toren nooit af. Generatie na generatie bouwde verder."),
        ]),
        dict(kop="De boekdrukkunst", blokken=[
            ("p", "Rond 1450 maakte <strong>Johannes Gutenberg</strong> in Duitsland de boekdrukkunst "
                  "met <strong>losse letters</strong> bekend. Je zet de letters één keer klaar in een "
                  "bak, en drukt er daarna honderden vellen mee. Daarna haal je ze uit elkaar en "
                  "gebruik je dezelfde letters voor de volgende bladzijde."),
            ("fig", svg.drukpers(),
             "De schroef duwt de pers op het papier. Wat vroeger een jaar overschrijven kostte, was nu een dag drukken."),
            ("p", "Daardoor werden boeken veel goedkoper en verspreidden ideeën zich sneller dan ooit. "
                  "Meer mensen leerden lezen, en een gedachte van iemand in de ene stad kon een paar "
                  "weken later in de andere gelezen worden. Dat had niemand eerder meegemaakt."),
        ]),
        dict(kop="De wereld wordt groter", blokken=[
            ("p", "In <strong>1492</strong> bereikte <strong>Christoffel Columbus</strong> Amerika, al "
                  "dacht hij zelf dat hij in Indië was aangekomen. Hij zocht namelijk een zeeweg naar "
                  "Azië, om daar specerijen te halen zonder over land te moeten."),
            ("p", "<strong>Magellaan</strong> vertrok in 1519; zijn expeditie voer als eerste rond de "
                  "hele aarde. Zulke ontdekkingsreizigers brachten <strong>zeeroutes</strong> in kaart. "
                  "Voor de mensen die al in Amerika woonden, was dat geen ontdekking maar het begin van "
                  "een harde tijd: ze verloren hun land en velen stierven aan meegebrachte ziekten."),
            ("p", "In de 18de eeuw kwam de <strong>Verlichting</strong>. Denkers vonden dat je niet "
                  "alles moet geloven omdat het altijd zo geweest is, maar dat je zelf moet nadenken, "
                  "vragen stellen en dingen onderzoeken. De <em>rede</em> en het onderzoek kwamen "
                  "centraal te staan. Veel van onze rechten en van onze manier van besturen komen "
                  "daaruit voort."),
        ]),
        dict(kop="De industriële revolutie", blokken=[
            ("p", "Vanaf het begin van de <strong>19de eeuw</strong> werd er niet meer thuis of in een "
                  "kleine werkplaats gewerkt, maar in <strong>fabrieken</strong>. Machines namen veel "
                  "handwerk over: één machine deed het werk van veel mensen, en veel sneller."),
            ("p", "De motor daarachter was de <strong>stoommachine</strong>. Met stoom konden machines, "
                  "treinen en schepen draaien zonder spierkracht van mens of dier. Het begon in "
                  "<strong>Engeland</strong>, dat steenkool, machines en havens had, en kwam daarna "
                  "naar onze streken."),
            ("fig", svg.stoommachine(),
             "Vuur kookt water tot stoom, de stoom duwt de zuiger op en neer, en het vliegwiel maakt daar een ronddraaiende beweging van."),
            ("p", "Rond de fabrieken groeiden de steden snel, vaak sneller dan er fatsoenlijke huizen "
                  "waren. Er werkten ook <strong>kinderen</strong> in die fabrieken en mijnen, soms "
                  "twaalf uur per dag, voor weinig geld en in gevaarlijke omstandigheden. Dat noemen we "
                  "<strong>kinderarbeid</strong>."),
            ("p", "Daar kwam pas verandering in met de <strong>leerplicht</strong>: kinderen moesten "
                  "naar school in plaats van naar het werk. In België werd dat rond de Eerste "
                  "Wereldoorlog wettelijk geregeld."),
        ]),
        dict(kop="De mijnen in Limburg", blokken=[
            ("p", "Fabrieken, treinen en kachels draaien op <strong>steenkool</strong>. In Limburg werd "
                  "die uit de grond gehaald: mijnwerkers gingen met een kooi honderden meters diep, en "
                  "werkten daar in smalle, warme en stoffige gangen."),
            ("fig", svg.mijnschacht(),
             "Boven de schacht staat de schachtbok. De wielen bovenaan winden de kabel op waaraan de kooi hangt."),
            ("p", "Er kwamen mensen uit heel Europa naar Limburg werken, en later ook van verder. Rond "
                  "de mijnen werden hele wijken gebouwd, de cités. De mijnen sloten in de jaren tachtig "
                  "en negentig, maar de gebouwen staan er nog, vaak met een nieuwe bestemming."),
        ]),
        dict(kop="België wordt een land", blokken=[
            ("p", "In <strong>1830</strong> werd België een onafhankelijk land. Daarvoor hoorde het bij "
                  "het Verenigd Koninkrijk der Nederlanden. Al vanaf het begin is België een "
                  "<strong>koninkrijk</strong>: kort na de onafhankelijkheid kwam er een koning aan het "
                  "hoofd, en dat is zo gebleven."),
            ("p", "België is óók een <strong>democratie</strong>. Dat woord komt uit het Grieks en "
                  "betekent: het volk beslist. In een democratie kiezen de inwoners zelf hun bestuur, "
                  "er zijn wetten die voor iedereen gelden, en je mag zeggen wat je denkt. Een land kan "
                  "dus tegelijk een koninkrijk én een democratie zijn: de koning is het staatshoofd, "
                  "maar de verkozen politici besturen."),
            ("p", "Dat stemrecht kwam er niet in één keer. Eerst mochten alleen rijke mannen stemmen. "
                  "Na de Eerste Wereldoorlog kregen alle mannen stemrecht, en <strong>vrouwen</strong> "
                  "mochten pas vanaf <strong>1948</strong> meestemmen bij de nationale verkiezingen."),
            ("weetje", "Stemrecht en leerplicht lijken vanzelfsprekend, maar ze zijn het niet. Mensen "
                       "hebben er jarenlang voor moeten vergaderen, staken en betogen. Rechten zijn "
                       "afgedwongen, niet gekregen."),
        ]),
        dict(kop="Twee wereldoorlogen", blokken=[
            ("p", "De 20ste eeuw kende <strong>twee wereldoorlogen</strong>. De "
                  "<strong>Eerste</strong> duurde van <strong>1914 tot 1918</strong>. In België werd "
                  "zwaar gevochten aan de IJzer, in de Westhoek, waar de soldaten jarenlang in "
                  "loopgraven tegenover elkaar lagen."),
            ("p", "De <strong>Tweede</strong> duurde van <strong>1939 tot 1945</strong>. Reken even na: "
                  "vier jaar tegenover zes jaar, de Tweede duurde dus langer. In Europa eindigde hij in "
                  "mei 1945."),
            ("p", "Tijdens de Tweede Wereldoorlog werden miljoenen mensen vervolgd en vermoord door het "
                  "naziregime, vooral <strong>Joden</strong>, maar ook Roma, mensen met een beperking, "
                  "politieke tegenstanders en anderen. Dat heet de <strong>Holocaust</strong>. Het is "
                  "een zwaar stuk geschiedenis, en juist daarom wordt het verteld: opdat mensen zouden "
                  "zien waartoe haat en onverschilligheid kunnen leiden."),
        ]),
        dict(kop="Van een verdeeld naar een verbonden Europa", blokken=[
            ("p", "Na 1945 kwam Europa in twee stukken te liggen: het westen en het oosten, met heel "
                  "verschillende besturen. In Duitsland liep die scheiding dwars door de hoofdstad. "
                  "Van <strong>1961 tot 1989</strong> deelde de <strong>Berlijnse Muur</strong> "
                  "Berlijn in twee. Wie aan de verkeerde kant woonde, kon niet zomaar naar de andere. "
                  "In november 1989 viel de muur."),
            ("p", "Tegelijk zochten Europese landen elkaar juist op. Uit die samenwerking groeide de "
                  "<strong>Europese Unie</strong>: een samenwerkingsverband van Europese landen, onder "
                  "meer opgericht om oorlog tussen die landen te voorkomen. Landen die samen handel "
                  "drijven en overleggen, vechten minder snel met elkaar. In veel van die landen betaal "
                  "je nu met de euro."),
            ("fig", svg.tijdlijn(
                [("middeleeuwen", 1000, 1500, "#c17f2b"),
                 ("nieuwe tijd", 1500, 1800, "#3b6ea5"),
                 ("nieuwste tijd", 1800, 2030, "#7a5230")],
                [(1302, "Guldensporenslag", "boven"), (1492, "Columbus", "onder"),
                 (1830, "België", "boven"), (1945, "einde WO II", "onder")],
                470),
             "Let op de schaal: de middeleeuwen duurden veel langer dan de nieuwste tijd, maar er staan minder jaartallen op. Hoe dichter bij vandaag, hoe meer we weten."),
            ("p", "In <strong>1969</strong> zette voor het eerst een mens voet op de maan. En met het "
                  "<strong>internet</strong> kan iedereen vandaag in een seconde informatie delen met "
                  "de hele wereld — iets waar een middeleeuwse monnik een jaar over deed voor één boek. "
                  "Daardoor vind je nu alles snel terug, maar moet je ook zelf nagaan of het klopt."),
        ]),
        dict(kop="Waarom we dit leren", blokken=[
            ("p", "Geschiedenis is niet het vanbuiten leren van jaartallen. Jaartallen zijn alleen "
                  "handig om dingen in de juiste volgorde te kunnen zetten."),
            ("kader", "<p>Je leert over het verleden om te <strong>begrijpen hoe onze wereld geworden "
                      "is wat ze is</strong>: waarom we stemmen, waarom je naar school gaat, waarom "
                      "landen samenwerken, waarom er in je straat een mijngebouw of een kathedraal "
                      "staat.</p><p>En je leert het om <strong>fouten niet te herhalen</strong>. Wie "
                      "weet hoe een oorlog begon of hoe mensen hun rechten kwijtraakten, herkent het "
                      "sneller als het opnieuw zou gebeuren.</p>"),
        ]),
    ],
    onthoud=[
        "Middeleeuwen: leenheren en leenmannen, boeren en kastelen; bijna niemand kon lezen.",
        "De Vlaamse steden werden rijk van de lakenhandel; ambachtslui zaten in gilden.",
        "In de 14de eeuw stierf ongeveer een derde van Europa aan de pest.",
        "Monniken schreven boeken over in het scriptorium; een kathedraal is de kerk van een bisschop.",
        "Gutenberg maakte rond 1450 het drukken met losse letters bekend.",
        "Columbus bereikte Amerika in 1492; Magellaans expeditie voer als eerste rond de aarde.",
        "De Verlichting zette de rede en het onderzoek centraal.",
        "De industriële revolutie begon in Engeland, in de 19de eeuw, op stoom en steenkool.",
        "Kinderarbeid verdween pas met de leerplicht.",
        "België werd onafhankelijk in 1830 en is sindsdien een koninkrijk én een democratie.",
        "Vrouwen stemden pas vanaf 1948 mee bij de nationale verkiezingen.",
        "WO I: 1914-1918. WO II: 1939-1945, dus de Tweede duurde langer. De Holocaust hoort bij WO II.",
        "De Berlijnse Muur deelde Berlijn van 1961 tot 1989.",
        "De Europese Unie ontstond onder meer om oorlog tussen Europese landen te voorkomen.",
        "1969: de eerste mens op de maan. Het internet laat ons wereldwijd informatie delen.",
    ])


if __name__ == "__main__":
    for naam, b in BUNDELS.items():
        bundel.schrijf(b, naam)

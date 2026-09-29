# -*- coding: utf-8 -*-
"""De leerbundels voor samenleving en economie op ✨ Spark-niveau.

Gebaseerd op de vakfiche samenleving en economie 1ste graad A-stroom (geldig
2027). Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde
thema behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de
bundel dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../spark/samenleving-en-economie.json`
doet daar het voorwerk voor.

Eén hoofdstuk kan dat niet halen: "Ik leef samen met anderen — deel 1" hangt aan
de prent van de speelplaats. Wat daarop staat, moet het kind zelf tellen en
zien; de bundel geeft de begrippen mee waarmee het kijkt, niet de inhoud van de
prent.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel

VAK = "Samenleving en economie"
SPARK = "✨ Spark — 1ste en 2de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────────────────────── 1. Ik ben wie ik ben
BUNDELS["ik-ben-wie-ik-ben"] = dict(
    vak=VAK, niveau=SPARK, titel="Ik ben wie ik ben",
    onder="Wat je identiteit is, uit welke lagen ze bestaat, en hoe de groepen om je heen haar mee kleuren.",
    secties=[
        dict(kop="Wat is identiteit?", blokken=[
            ("p", "Je <strong>identiteit</strong> is het geheel van wat jou tot die ene persoon maakt: je "
                  "lichaam, je karakter, waar je vandaan komt, wat je graag doet, bij welke groepen je hoort. "
                  "Alles samen. Niet één ding ervan is jouw identiteit; het geheel is dat wel."),
            ("p", "De vakfiche onderscheidt <strong>twee soorten identiteit</strong>. Je "
                  "<strong>persoonlijke identiteit</strong> gaat over jou als persoon. Je "
                  "<strong>groepsidentiteit</strong> gaat over de groepen waar je deel van uitmaakt. "
                  "Je hebt ze allebei tegelijk."),
            ("fig", tabel(["identiteit is …", "wat dat betekent"], [
                ["<strong>gelaagd</strong>", "ze bestaat uit verschillende lagen die samen bepalen wie je bent"],
                ["<strong>dynamisch</strong>", "ze ligt niet vast bij je geboorte, ze kan veranderen"],
                ["<strong>relationeel</strong>", "ze krijgt vorm in je contacten met anderen"],
                ["<strong>uniek</strong>", "twee mensen hebben nooit precies dezelfde persoonlijke identiteit"],
            ]), "Vier woorden die telkens terugkomen. Ze horen bij elkaar: net omdat identiteit gelaagd en relationeel is, kan ze ook veranderen."),
            ("kader", "Verhuis je naar een ander land en voel je je na een paar jaar anders over wie je bent? "
                      "Dan zie je dat identiteit <strong>dynamisch</strong> is. Je bent niet iemand anders "
                      "geworden: er zijn lagen bijgekomen en andere zijn verschoven."),
            ("p", "Let op wat géén identiteit is. \"De bus komt vandaag tien minuten te laat\" en \"de winkel "
                  "op de hoek sluit om zes uur\" zeggen niets over wie iemand is. Een uitspraak gaat pas over "
                  "identiteit als ze iets zegt over de persoon zelf of over de groepen waar hij bij hoort."),
        ]),
        dict(kop="Je persoonlijke identiteit in drie lagen", blokken=[
            ("p", "De fiche deelt je persoonlijke identiteit op in <strong>drie lagen</strong>. Je moet van "
                  "een gegeven voorbeeld kunnen zeggen bij welke laag het hoort."),
            ("fig", tabel(["laag", "wat zit erin?"], [
                ["<strong>biologische aspecten</strong>", "je leeftijd, je lichaam en je geslacht"],
                ["<strong>persoonlijke eigenschappen</strong>", "je karakter: geduldig, nieuwsgierig, verlegen, koppig, zorgzaam …"],
                ["<strong>familiale achtergrond</strong>", "of je broers of zussen hebt, het beroep van je ouders, de taal die bij jou thuis gesproken wordt"],
            ]), "Je leeftijd hoort altijd bij de biologische aspecten. Dat kies je niet zelf, en ook niet in welke laag het thuishoort."),
            ("p", "Eén zin kan meerdere lagen tegelijk raken. \"Hij is een goede zwemmer, houdt van tekenen en "
                  "woont bij zijn oma\": dat is zijn lichaam, zijn eigenschappen én zijn familiale achtergrond. "
                  "<strong>Drie</strong> lagen dus, in één zin."),
            ("kader", "De <strong>ID-cirkel</strong> of identiteitscirkel is de tekening waarin je de elementen "
                      "identiteit rond jezelf zet. In het midden staat één element: de persoon zelf. Daaromheen "
                      "komen de lagen. Zo zie je in één blik dat je uit veel meer bestaat dan het eerste woord "
                      "dat iemand over je zou zeggen."),
        ]),
        dict(kop="Identiteit en imago", blokken=[
            ("p", "Je <strong>imago</strong> is niet hetzelfde als je identiteit. Je identiteit is wie je "
                  "écht bent; je imago is het <strong>beeld dat anderen van je hebben</strong>. Die twee "
                  "kunnen ver uit elkaar liggen."),
            ("p", "Iemand die op sociale media doet alsof hij elk weekend op reis gaat terwijl dat niet zo is, "
                  "bouwt een imago op dat niet klopt met zijn identiteit. Dat is geen leugen om iemand te "
                  "bedriegen, maar het kost wel iets: hoe groter het verschil, hoe moeilijker het wordt om "
                  "gewoon jezelf te zijn."),
        ]),
        dict(kop="Groepsidentiteit", blokken=[
            ("p", "Je <strong>groepsidentiteit</strong> gaat over de groepen waar je deel van uitmaakt. Ook "
                  "die is gelaagd."),
            ("fig", tabel(["laag", "voorbeelden"], [
                ["de regio, het land of het gebied waar je vandaan komt", "opgegroeid in Limburg, met een accent dat je hoort"],
                ["de groepen waar je deel van uitmaakt", "je gender, je sociale klasse, je geloof of overtuiging"],
                ["de subculturen waar je bij hoort", "skaters, gamers, metalfans, een jeugdbeweging"],
            ]), "Je kan bij veel groepen tegelijk horen, en dat is normaal."),
            ("p", "Een <strong>subcultuur</strong> is een kleinere groep binnen de samenleving met een eigen "
                  "stijl: eigen kleren, eigen muziek, eigen woorden. Subculturen bestaan niet alleen bij "
                  "jongeren. Ook wielertoeristen, verzamelaars of koorzangers vormen er een."),
            ("weetje", "Je kan je in twee culturen tegelijk thuis voelen. Dat is geen tegenstrijdigheid: "
                       "groepsidentiteit is gelaagd, dus je kan bij meerdere groepen tegelijk horen zonder "
                       "er één te moeten opgeven."),
        ]),
        dict(kop="Wat groepen met mensen doen", blokken=[
            ("p", "Je persoonlijke identiteit en je groepsidentiteit beïnvloeden elkaar <strong>in twee "
                  "richtingen</strong>: de groep kleurt jou, en jij kleurt de groep. Je groepsidentiteit "
                  "heeft dus wel degelijk invloed op wie je als persoon wordt."),
            ("fig", tabel(["woord", "wat het betekent"], [
                ["<strong>verbondenheid</strong>", "het gevoel ergens bij te horen"],
                ["<strong>solidariteit</strong>", "elkaar steunen, ook als je er zelf niets bij wint"],
                ["<strong>wij-zij-denken</strong>", "de wereld opdelen in de eigen groep en de anderen"],
                ["<strong>discriminatie</strong>", "mensen anders en slechter behandelen om wie ze zijn"],
            ]), "De eerste twee brengen mensen samen, de laatste twee duwen ze uit elkaar."),
            ("p", "<strong>Wij-zij-denken</strong> heeft gevolgen. Mensen buiten de eigen groep worden sneller "
                  "uitgesloten, vooroordelen over de andere groep worden sterker, en de eigen groep voelt zich "
                  "hechter. Dat laatste is precies waarom het zo aantrekkelijk is: de band binnen de groep "
                  "wordt betaald met de afstand naar buiten."),
            ("p", "Een klas die geld inzamelt voor een medeleerling van wie het huis is afgebrand: dat is "
                  "<strong>solidariteit</strong>. Iemand die nooit gevraagd wordt voor een groepswerk omdat hij "
                  "een andere achtergrond heeft: dat is <strong>discriminatie</strong>. Het verschil zit niet "
                  "in de bedoeling die iemand zegt te hebben, maar in wat er met de ander gebeurt."),
            ("kader", "Discriminatie raakt niet alleen aan wat je mag doen, ze kan ook <strong>iemands beeld "
                      "van zichzelf veranderen</strong>. Wie vaak te horen krijgt dat hij er niet bij hoort, "
                      "gaat dat op den duur zelf geloven. Daarom is er geen onschuldige vorm van."),
        ]),
    ],
    onthoud=[
        "Identiteit is gelaagd, dynamisch, relationeel en uniek.",
        "Twee soorten: je persoonlijke identiteit en je groepsidentiteit.",
        "Drie lagen van je persoonlijke identiteit: biologische aspecten, persoonlijke eigenschappen, familiale achtergrond.",
        "In een ID-cirkel staat de persoon zelf in het midden.",
        "Je identiteit is wie je bent, je imago is het beeld dat anderen van je hebben.",
        "Groepsidentiteit: je regio, de groepen waar je bij hoort, en je subculturen.",
        "Verbondenheid en solidariteit brengen samen; wij-zij-denken en discriminatie duwen uit elkaar.",
    ],
)

# ───────────────────────────────────────── 2. Ik leef samen met anderen
BUNDELS["ik-leef-samen-met-anderen"] = dict(
    vak=VAK, niveau=SPARK, titel="Ik leef samen met anderen",
    onder="Diversiteit, pesten en plagen, groepsdruk en grenzen, en wat een samenwerking doet lukken.",
    secties=[
        dict(kop="Diversiteit", blokken=[
            ("p", "<strong>Diversiteit</strong> betekent dat mensen in een samenleving van elkaar verschillen. "
                  "Dat is geen uitzondering maar de regel: er bestaat geen klas, geen straat en geen land "
                  "waarin iedereen hetzelfde is."),
            ("fig", tabel(["vorm van diversiteit", "waarover ze gaat"], [
                ["<strong>sociale diversiteit</strong>", "verschillen in opleiding, werk, inkomen, gezinssituatie"],
                ["<strong>culturele diversiteit</strong>", "verschillen in taal, gewoontes, feesten, eten"],
                ["<strong>religieuze of levensbeschouwelijke diversiteit</strong>", "verschillen in geloof of overtuiging"],
                ["<strong>seksuele diversiteit</strong>", "verschillen in wie je aantrekkelijk vindt en hoe je jezelf beleeft"],
            ]), "De vier vormen die de vakfiche noemt. Ze staan naast elkaar, niet boven elkaar."),
            ("p", "Samenleven in diversiteit is soms <strong>moeilijk</strong>, omdat verschillen kunnen leiden "
                  "tot misverstanden en vooroordelen. Het is tegelijk <strong>waardevol</strong>: je leert "
                  "manieren van doen kennen die je zelf niet had bedacht. Allebei is waar, en het een heft het "
                  "ander niet op."),
        ]),
        dict(kop="Plagen, pesten en een meningsverschil", blokken=[
            ("p", "Deze drie worden vaak door elkaar gehaald, en toch zijn ze niet hetzelfde."),
            ("fig", svg.pijlrichting("plagen", "het gaat over|en weer", True),
             "Plagen gaat over en weer. Vandaag jij, morgen ik, en allebei vinden jullie het nog leuk."),
            ("fig", svg.pijlrichting("pesten", "één kant raakt|de andere", False),
             "Pesten gaat maar één kant op, het herhaalt zich, en er is een machtsverschil: één tegen een groep, of sterk tegen minder sterk."),
            ("p", "Een <strong>meningsverschil</strong> is iets anders dan allebei: twee mensen denken anders "
                  "over iets en zeggen dat tegen elkaar. Daar is niets mis mee. Het wordt pas pesten als het "
                  "niet meer over de zaak gaat maar over de persoon, en als het blijft terugkomen."),
            ("kader", "\"Op een speelplaats hoort dat erbij, daar moet je niets van zeggen.\" Dat klopt niet: "
                      "<strong>dat iets vaak gebeurt, maakt het nog niet aanvaardbaar</strong>. Hoe gewoon "
                      "iets geworden is, zegt niets over of het mag."),
        ]),
        dict(kop="Meedoen, toekijken of ingrijpen", blokken=[
            ("p", "Bij pesten zijn er zelden maar twee mensen betrokken. Er is de gepeste, er is wie pest, en "
                  "er zijn <strong>omstaanders</strong>: wie het ziet gebeuren en niets doet. Wie meelacht of "
                  "meedoet, zorgt ervoor dat het pesten doorgaat, ook zonder zelf iets te zeggen."),
            ("p", "<strong>Gepaste reacties</strong> zijn er wel, en ze zijn kleiner dan je denkt. Duidelijk "
                  "zeggen dat je het niet oké vindt. Er een volwassene bij halen die kan helpen. Achteraf naar "
                  "de gepeste toe gaan en vragen hoe het gaat. Aan de gepeste laten weten dat je achter hem "
                  "staat. Een hand op een schouder van wie het moeilijk heeft is ook al contact zoeken."),
            ("fig", tabel(["woord", "wat het betekent"], [
                ["<strong>groepsdruk</strong>", "de druk om iets te doen omdat de groep het doet of verwacht"],
                ["<strong>machtsmisbruik</strong>", "je positie gebruiken om iemand iets op te leggen"],
                ["<strong>uitsluiten</strong>", "iemand bewust niet uitnodigen om die persoon buiten de groep te houden"],
                ["<strong>racisme</strong>", "mensen minder behandelen om hun afkomst of huidskleur"],
                ["<strong>discriminatie</strong>", "mensen anders en slechter behandelen om wie ze zijn"],
            ]), "Iemand die een stage niet krijgt omdat zijn naam buitenlands klinkt, is gediscrimineerd."),
        ]),
        dict(kop="Emoties en grenzen", blokken=[
            ("p", "Er zijn vier <strong>basisemoties</strong>: <strong>blijdschap</strong>, "
                  "<strong>verdriet</strong>, <strong>angst</strong> en <strong>woede</strong>. Alle andere "
                  "gevoelens zijn mengsels of nuances daarvan. Je herkent ze bij anderen aan hun gezicht, hun "
                  "houding en hun stem."),
            ("p", "Naast een lichamelijke grens heb je ook een <strong>mentale grens</strong>: de grens van "
                  "wat je van binnen nog aankan. Die ligt bij iedereen ergens anders. Wat voor de ene een grap "
                  "is, is voor de andere te veel, en dan is het te veel. "
                  "<strong>Zelfrespect</strong> betekent dat je ook je eigen grenzen bewaakt, en niet alleen "
                  "die van anderen respecteert."),
            ("fig", tabel(["respectvol omgaan met elkaars lichaam", "wat dat vraagt"], [
                ["<strong>toestemming</strong>", "allebei akkoord en allebei goed erbij"],
                ["<strong>vrijwillig</strong>", "niemand zet de ander onder druk"],
                ["<strong>gelijkwaardigheid</strong>", "er is geen machtsverschil tussen de twee"],
            ]), "Alle drie tegelijk, of het telt niet."),
            ("kader", "Toestemming die onder druk gegeven wordt, telt <strong>niet</strong> als een echte "
                      "toestemming. Een ja die je alleen zegt omdat je niet durft te weigeren, is geen ja. "
                      "Twijfel je, dan is het antwoord nee, en dat is genoeg."),
        ]),
        dict(kop="Goed samenwerken", blokken=[
            ("p", "De vakfiche noemt een paar <strong>kenmerken van een goede samenwerking</strong>. Ze klinken "
                  "vanzelfsprekend, tot je ze ziet ontbreken."),
            ("fig", tabel(["kenmerk", "hoe je het ziet"], [
                ["<strong>luisteren naar elkaar</strong>", "iedereen krijgt zijn zin af"],
                ["<strong>om de beurt spreken</strong>", "niemand praat door de ander heen"],
                ["<strong>gepaste lichaamstaal</strong>", "je draait je naar wie spreekt, je kijkt niet weg"],
                ["<strong>afspraken nakomen</strong>", "wat je beloofde, breng je mee"],
                ["<strong>hulp vragen wanneer iets niet duidelijk is</strong>", "liever een vraag te veel dan werk voor niets"],
                ["<strong>rekening houden met de inbreng van anderen</strong>", "een idee van iemand anders wordt ook echt gebruikt"],
                ["<strong>duidelijk en rustig communiceren</strong>", "je zegt wat je bedoelt, zonder te roepen"],
            ]), "Deze zeven zijn ook wat je op een prent kan herkennen aan een groepje dat goed samenwerkt."),
        ]),
        dict(kop="Kijken naar een prent", blokken=[
            ("p", "Bij het eerste deel van dit hoofdstuk hoort een <strong>prent van een speelplaats</strong>. "
                  "Er wordt gevraagd wat je ziet, en dat is iets anders dan wat je vermoedt."),
            ("p", "Kijk <strong>verder dan het midden</strong>. In het midden gebeurt meestal het meest "
                  "opvallende, maar wie erbuiten valt zie je pas als je ook naar de randen kijkt: de bank "
                  "opzij, iemand die alleen voorbijloopt, iemand die van een afstand toekijkt."),
            ("kader", "Zeg alleen wat je <strong>zeker</strong> weet. Zie je iemand alleen op een bank zitten "
                      "met een bedrukt gezicht, dan weet je dat die persoon op dit moment alleen zit. Niet dat "
                      "ze geen vrienden heeft, niet dat ze gepest wordt, niet dat ze verdrietig is om iets "
                      "bepaalds. Wil je dat weten, dan is de beste eerste vraag heel gewoon: is er iets, wil "
                      "je erover praten?"),
            ("p", "Tel wat er te tellen valt en benoem wat er te benoemen valt: hoeveel mensen, welke "
                  "activiteiten, wie kijkt naar wie. Een prent waarop iedereen met dezelfde activiteit bezig "
                  "is, bestaat zelden; op een speelplaats lopen meestal verschillende spelen door elkaar."),
        ]),
    ],
    onthoud=[
        "Vier vormen van diversiteit: sociale, culturele, religieuze of levensbeschouwelijke, en seksuele.",
        "Plagen gaat over en weer; pesten gaat één kant op, herhaalt zich en heeft een machtsverschil.",
        "Een omstaander die meelacht, zorgt mee dat het pesten doorgaat.",
        "Vier basisemoties: blijdschap, verdriet, angst, woede.",
        "Toestemming telt alleen als ze vrijwillig en gelijkwaardig is; onder druk telt ze niet.",
        "Zelfrespect is ook je eigen grenzen bewaken.",
        "Bij een prent: zeg alleen wat je zeker ziet, en kijk ook naar de randen.",
    ],
)

# ───────────────────────────────────────── 3. Eerste hulp bij ongevallen
BUNDELS["eerste-hulp-bij-ongevallen"] = dict(
    vak=VAK, niveau=SPARK, titel="Eerste hulp bij ongevallen",
    onder="De vier stappen, het nummer 112, en wat je doet bij bewusteloosheid, verslikking, bloeding, brandwonde en verstuiking.",
    secties=[
        dict(kop="De vier stappen, altijd in deze volgorde", blokken=[
            ("fig", svg.stappen(["veiligheid", "toestand beoordelen", "hulp raadplegen", "verdere hulp"]),
             "Je doorloopt ze in die volgorde, elke keer opnieuw. Ook als het klein lijkt."),
            ("p", "<strong>Zorgen voor veiligheid</strong> komt vóór alle andere stappen, omdat je niemand kan "
                  "helpen als jij zelf gewond raakt. Ligt er rondslingerend glas, dan maak je het eerst veilig "
                  "of je zorgt dat je zelf veilig staat. Ligt iemand op de rijweg terwijl het verkeer gewoon "
                  "doorrijdt, dan is de plaats veilig maken de eerste zorg, bijvoorbeeld met een "
                  "<strong>gevarendriehoek</strong>."),
            ("p", "Bij stap twee, de <strong>toestand van het slachtoffer beoordelen</strong>, ga je drie "
                  "dingen na: reageert de persoon als je hem aanspreekt, ademt hij normaal, en is er ergens "
                  "zwaar bloedverlies. Pas daarna bel je, en daarna verleen je verdere hulp tot de hulpdiensten "
                  "er zijn. <strong>Eerste hulp verlenen betekent niet dat je het slachtoffer geneest</strong>: "
                  "je overbrugt de tijd en zorgt dat het niet erger wordt."),
        ]),
        dict(kop="112 bellen", blokken=[
            ("p", "In België bel je <strong>112</strong> voor een ambulance of de brandweer. Dat nummer werkt "
                  "in heel Europa en is gratis."),
            ("fig", tabel(["wat je zeker vertelt", "waarom"], [
                ["waar het gebeurd is, zo precies mogelijk", "zonder plaats komt er niemand"],
                ["wat er gebeurd is en hoeveel slachtoffers er zijn", "dan weten ze wat ze moeten meebrengen"],
                ["in welke toestand het slachtoffer is", "dan weten ze hoe dringend het is"],
            ]), "En je blijft aan de lijn: de operator legt eerst neer, jij niet."),
            ("kader", "Staan er meerdere mensen bij een ongeval, ga er dan <strong>niet</strong> van uit dat "
                      "iemand anders al gebeld heeft. Dat denkt iedereen tegelijk, en dan belt er niemand. "
                      "Wijs één persoon aan en zeg: bel jij 112. "
                      "Bij twijfel over hoe ernstig iets is, bel je beter toch."),
        ]),
        dict(kop="Bewustzijn en de stabiele zijligging", blokken=[
            ("p", "Of iemand <strong>bij bewustzijn</strong> is, controleer je door de persoon luid aan te "
                  "spreken en aan de schouders te schudden. Reageert hij niet, maar ademt hij wel normaal, dan "
                  "leg je hem in de <strong>stabiele zijligging</strong>. Dat is de houding waarin een "
                  "bewusteloos maar ademend slachtoffer veilig ligt."),
            ("p", "Dat doe je zodat de <strong>luchtweg vrij blijft</strong> en braaksel kan weglopen. Het "
                  "slachtoffer ligt op zijn zij, met het hoofd lichtjes achterover en de mond naar beneden "
                  "gericht. Daarna <strong>blijf je bij hem</strong> en controleer je of hij blijft ademen: "
                  "alleen achterlaten doe je nooit."),
            ("weetje", "Iemand die niet reageert, geef je <strong>nooit iets te drinken</strong>. De drank kan "
                       "in de luchtweg komen in plaats van in de slokdarm, en dan maak je het erger."),
            ("p", "Valt een klasgenoot flauw en reageert hij niet als je hem aanspreekt, maar ademt hij wel "
                  "rustig? Dan leg je hem in stabiele zijligging en bel je 112. Heeft iemand zijn arm gebroken "
                  "maar is hij helder en praat hij gewoon, dan hoef je hem niet te verplaatsen, maar de stap "
                  "<strong>gespecialiseerde hulp raadplegen</strong> sla je ook dan niet over."),
        ]),
        dict(kop="Verslikking: rugslagen en buikstoten", blokken=[
            ("p", "Verslikt iemand zich en <strong>hoest hij luid en krachtig</strong>, dan moedig je hem aan "
                  "om te blijven hoesten. Hoesten is de sterkste manier om iets weg te krijgen; jij doet dan "
                  "niets anders."),
            ("p", "Bij een <strong>ernstige verslikking</strong>, als iemand niet meer kan hoesten of spreken, "
                  "grijp je wel in. <strong>Rugslagen</strong> zijn stevige slagen met de hiel van je hand "
                  "tussen de schouderbladen. Een <strong>buikstoot</strong> is een stevige ruk naar binnen en "
                  "naar boven onder de ribben. Je <strong>wisselt rugslagen en buikstoten met elkaar af</strong> "
                  "tot het voorwerp eruit is of tot de hulpdiensten er zijn."),
            ("kader", "Bij een <strong>baby jonger dan één jaar</strong> geef je <strong>geen "
                      "buikstoten</strong>. Het buikje is daar te kwetsbaar voor. Daar wissel je rugslagen af "
                      "met borstcompressies, en je belt altijd 112."),
        ]),
        dict(kop="Bloeding, brandwonde en huidwonde", blokken=[
            ("p", "Bij een wonde die <strong>hevig bloedt</strong> druk je stevig op de wonde met een verband "
                  "of een propere doek. Dat is meteen de eerste handeling, ook als iemand zich in de keuken "
                  "gesneden heeft en er veel bloed uit zijn hand stroomt: eerst drukken, dan pas de rest."),
            ("fig", tabel(["symptomen van een ernstige bloeding", ""], [
                ["bloed dat blijft doorstromen ondanks druk", "de druk volstaat niet, bel 112"],
                ["een bleke, klamme huid", "het lichaam verliest te veel bloed"],
                ["een slachtoffer dat duizelig wordt", "idem; laat hem liggen, niet rechtstaan"],
            ]), "Drie tekens die samen zeggen: dit is meer dan een snee."),
            ("p", "Een <strong>brandwonde</strong> koel je <strong>tien tot twintig minuten met lauw zacht "
                  "stromend water</strong>. Niet met ijs, niet met boter, niet met tandpasta. Kleding die aan "
                  "de brandwonde <strong>vastgekleefd</strong> zit, laat je zitten: eraf trekken scheurt de "
                  "huid mee."),
            ("p", "Een gewone <strong>huidwonde</strong>, zoals een schaafwonde, spoel je met water, ontsmet "
                  "je en dek je af. In die volgorde."),
        ]),
        dict(kop="Verstuiking en breuk", blokken=[
            ("p", "Bij een <strong>verstuiking</strong> zijn de banden rond een gewricht gerekt. Bij een "
                  "<strong>breuk</strong> is het bot zelf gebroken. Van buitenaf lijken ze soms op elkaar."),
            ("fig", tabel(["symptomen van een verstuiking", ""], [
                ["pijn bij het bewegen van het gewricht", "vooral bij steunen of draaien"],
                ["een zwelling rond het gewricht", "die komt vaak snel op"],
                ["een blauwe verkleuring rond het gewricht", "die komt meestal pas later"],
            ]), "Een verstuikte enkel is het bekendste voorbeeld."),
            ("p", "Bij een verstuikte enkel geef je <strong>rust</strong>, je <strong>koelt</strong>, je legt "
                  "een <strong>drukverband</strong> aan en je legt de enkel <strong>hoog</strong>. Een "
                  "<strong>koelzak leg je nooit rechtstreeks op de blote huid</strong>: doe er altijd een doek "
                  "tussen, anders vries je de huid kapot."),
            ("kader", "Twijfel je tussen een verstuiking en een breuk? Dan laat je het gewricht met rust en "
                      "laat je het nakijken. Je hoeft het verschil niet zelf te kunnen vaststellen; je hoeft "
                      "alleen niet te doen alsof het niets is."),
            ("p", "De vakfiche vraagt dat je de symptomen kan herkennen bij drie soorten ongevallen: een "
                  "<strong>bloeding</strong>, een <strong>verslikking</strong> en een "
                  "<strong>verstuiking</strong>."),
        ]),
    ],
    onthoud=[
        "De vier stappen: veiligheid, toestand beoordelen, hulp raadplegen, verdere hulp verlenen.",
        "112 is het nummer; zeg waar, wat, hoeveel slachtoffers en in welke toestand, en leg niet als eerste neer.",
        "Bewusteloos maar normaal ademend: stabiele zijligging, 112 bellen, en blijven.",
        "Hoest iemand nog krachtig, laat hem hoesten; kan hij niet meer hoesten of spreken, wissel rugslagen en buikstoten af.",
        "Hevige bloeding: stevig drukken met een propere doek.",
        "Brandwonde: tien tot twintig minuten lauw stromend water, vastgekleefde kleding laten zitten.",
        "Verstuiking: rust, koelen (nooit op de blote huid), drukverband, hoog leggen.",
    ],
)

# ───────────────────────────────────────── 4. Democratie en dictatuur
BUNDELS["democratie-en-dictatuur"] = dict(
    vak=VAK, niveau=SPARK, titel="Democratie en dictatuur",
    onder="De principes van een democratische rechtsstaat, het verschil met een autoritair regime, en je eigen rechten en plichten.",
    secties=[
        dict(kop="Wat democratie letterlijk betekent", blokken=[
            ("p", "<strong>Democratie</strong> komt uit het Grieks: <em>demos</em> is volk en <em>kratos</em> "
                  "is macht. Letterlijk betekent het dus: <strong>het volk regeert</strong>. De macht ligt bij "
                  "de bevolking, en die geeft ze tijdelijk uit handen aan mensen die ze zelf kiest."),
            ("p", "Een <strong>democratische rechtsstaat</strong> is meer dan alleen verkiezingen. Het is een "
                  "land waarin de macht gecontroleerd wordt en waarin ook de overheid zelf zich aan de wet moet "
                  "houden."),
            ("fig", tabel(["principe", "wat het inhoudt"], [
                ["<strong>stemrecht</strong>", "iedereen die aan de voorwaarden voldoet, mag mee kiezen"],
                ["<strong>vrije verkiezingen</strong>", "iedereen stemt zonder dwang en in het geheim"],
                ["<strong>scheiding van de machten</strong>", "de drie machten zijn van elkaar gescheiden"],
                ["<strong>individuele vrijheid</strong>", "je mag je eigen leven inrichten, binnen de wet"],
                ["<strong>een grondwet</strong>", "de hoogste wet, waar alle andere wetten zich aan moeten houden"],
                ["<strong>vrije meningsuiting en persvrijheid</strong>", "je mag zeggen en schrijven wat je denkt, ook over de macht"],
                ["<strong>gelijkheid voor de wet</strong>", "dezelfde wet geldt voor iedereen, ook voor wie macht of geld heeft"],
            ]), "De zeven principes uit de vakfiche. Je moet kunnen beoordelen of ze in een situatie gerespecteerd worden."),
        ]),
        dict(kop="De drie machten", blokken=[
            ("fig", svg.stappen(["wetgevende macht", "uitvoerende macht", "rechterlijke macht"]),
             "Het parlement maakt de wet, de regering voert ze uit, de rechter past ze toe op één geval."),
            ("fig", tabel(["macht", "wie", "wat"], [
                ["<strong>wetgevende</strong>", "het parlement", "maakt en stemt de wetten"],
                ["<strong>uitvoerende</strong>", "de regering", "zorgt ervoor dat de wetten in de praktijk gebracht worden"],
                ["<strong>rechterlijke</strong>", "de rechters in de rechtbanken en de hoven", "spreken recht in een conflict"],
            ]), "Een minister hoort bij de uitvoerende macht, een volksvertegenwoordiger bij de wetgevende."),
            ("p", "Waarom zijn ze <strong>gescheiden</strong>? Zodat ze elkaar kunnen controleren en niemand "
                  "alle macht krijgt. Een macht die zichzelf controleert, controleert niets. Het is dus "
                  "uitdrukkelijk <strong>niet</strong> de bedoeling dat dezelfde persoon alle drie de machten "
                  "tegelijk in handen heeft."),
            ("kader", "Een regering die beslist dat rechters voortaan door haar benoemd en ontslagen worden, "
                      "brengt de <strong>scheiding van de machten</strong> in gevaar. Een rechter die zijn job "
                      "kan verliezen als hij de regering tegenspreekt, spreekt de regering niet meer tegen."),
        ]),
        dict(kop="De principes toepassen op een situatie", blokken=[
            ("p", "Op het examen krijg je een situatie en moet je zeggen welk principe daar geschonden wordt. "
                  "Een paar die telkens terugkomen:"),
            ("fig", tabel(["wat er gebeurt", "welk principe"], [
                ["een journalist wordt opgepakt om een kritisch artikel over een minister", "de persvrijheid"],
                ["een rechter spreekt een vriend van de eerste minister vrij omdat hij zijn vriend is", "de gelijkheid voor de wet"],
                ["er mag maar één partij deelnemen aan de verkiezingen", "vrije verkiezingen, het stemrecht en de individuele vrijheid om te kiezen"],
                ["de regering bepaalt vooraf wie zich kandidaat mag stellen", "de verkiezingen zijn niet echt vrij"],
            ]), "Kijk telkens wat er precies onmogelijk gemaakt wordt: kiezen, weten, of gelijk behandeld worden."),
            ("p", "Twee dingen die vaak verkeerd begrepen worden. Je "
                  "<strong>individuele vrijheid loopt tot waar de vrijheid van iemand anders begint</strong>; "
                  "vrijheid is geen vrijgeleide. En <strong>vrije meningsuiting</strong> heeft grenzen: kritiek "
                  "geven mag altijd, oproepen tot geweld tegen een groep niet."),
            ("weetje", "In België is er <strong>stemplicht</strong> voor het federale parlement, het Vlaams "
                       "Parlement en het Europees Parlement: je moet gaan stemmen, al kies je zelf op wie. "
                       "Voor de gemeenteraad in Vlaanderen is die opkomstplicht sinds 2024 afgeschaft. Rechters "
                       "worden trouwens nooit verkozen maar <strong>benoemd</strong>, juist om hen "
                       "onafhankelijk te houden."),
        ]),
        dict(kop="Democratie tegenover een autoritair regime", blokken=[
            ("p", "Een <strong>autoritair regime</strong> is een bestuur waarin één persoon of groep alle macht "
                  "heeft. Een <strong>dictatuur</strong> is daar de bekendste vorm van."),
            ("p", "In een dictatuur worden er <strong>soms wel verkiezingen gehouden</strong>, maar dan liggen "
                  "de uitslagen op voorhand vast of is er maar één partij. De vorm is er, de inhoud niet. Je "
                  "ziet er ook journalisten die opgepakt worden om wat ze schrijven, en rechters die doen wat "
                  "de leider hun opdraagt."),
            ("kader", "Verdwijnt in een land de grondwet, worden rechters door de leider benoemd en mag er nog "
                      "maar één krant verschijnen? Dan is dat land een <strong>autoritair regime</strong> "
                      "geworden. Drie principes tegelijk weg, en van de rechtsstaat blijft niets over."),
            ("p", "Het <strong>grootste verschil</strong> zit hier: in een democratie wordt de macht "
                  "gecontroleerd en kan ze wisselen. Wie verliest, gaat weg. Dat is precies wat een autoritair "
                  "regime onmogelijk maakt."),
        ]),
        dict(kop="Inspraak, rechten en plichten", blokken=[
            ("p", "<strong>Inspraak hebben</strong> betekent dat je mening meetelt in een beslissing die ook "
                  "over jou gaat. Het betekent <strong>niet</strong> dat jouw voorstel altijd wordt uitgevoerd: "
                  "er zijn ook andere meningen."),
            ("p", "Je hebt inspraak als de leerlingenraad vraagt wat er op de speelplaats moet komen, als je "
                  "gezin samen bespreekt waar jullie op vakantie gaan, of als je sportclub de leden laat "
                  "stemmen over nieuwe trainingsuren. Laat een school de leerlingen stemmen over het thema van "
                  "het schoolfeest en kiest de directie achteraf zelf iets anders zonder uitleg, dan was de "
                  "inspraak <strong>maar schijn</strong>: de uitslag telde niet mee."),
            ("fig", tabel(["rechten die je in België hebt", "plichten die je in België hebt"], [
                ["het recht op onderwijs", "naar school gaan tot je achttien bent"],
                ["het recht om je mening te uiten", "anderen die van hen laten uiten"],
                ["het recht op een eerlijk proces", "belastingen betalen"],
            ]), "Rechten en plichten horen bij elkaar: waar de een stopt, begint vaak de ander."),
            ("p", "Waarom is het belangrijk dat mensen <strong>gaan stemmen</strong>? Omdat de samenstelling "
                  "van het parlement er rechtstreeks van afhangt. En waarom is <strong>vrije "
                  "meningsuiting</strong> belangrijk? Omdat je alleen kan kiezen als je vrij kan horen en "
                  "zeggen wat er speelt."),
            ("p", "Mag je nog niet stemmen? Dan kan je toch meewegen: je kandidaat stellen voor de "
                  "leerlingenraad, meedoen aan een jeugdraad in je gemeente, of je mening geven op een "
                  "inspraakmoment. En je mag in een democratie <strong>betogen</strong> tegen een beslissing "
                  "van de regering, zolang het vreedzaam blijft. Kritiek op de regering is net waar dat recht "
                  "voor bestaat."),
        ]),
    ],
    onthoud=[
        "Democratie betekent letterlijk: het volk regeert.",
        "Zeven principes: stemrecht, vrije verkiezingen, scheiding van de machten, individuele vrijheid, een grondwet, vrije meningsuiting en persvrijheid, gelijkheid voor de wet.",
        "Wetgevend = parlement, uitvoerend = regering, rechterlijk = de rechters.",
        "De machten zijn gescheiden zodat ze elkaar kunnen controleren.",
        "In een dictatuur zijn er soms verkiezingen, maar ze zijn niet vrij.",
        "Inspraak is meetellen, niet altijd je zin krijgen.",
        "Rechters worden benoemd, niet verkozen.",
    ],
)

# ───────────────────────────────────────── 5. Hoe België bestuurd wordt
BUNDELS["hoe-belgie-bestuurd-wordt"] = dict(
    vak=VAK, niveau=SPARK, titel="Hoe België bestuurd wordt",
    onder="De vier bestuursniveaus met hun organen en hun bevoegdheden, van het gemeentehuis tot de federale regering.",
    secties=[
        dict(kop="Vier niveaus", blokken=[
            ("fig", svg.bestuurslagen(), "De vier bestuursniveaus van België, met bij elk een paar van zijn bevoegdheden."),
            ("p", "België wordt op <strong>vier niveaus</strong> bestuurd: de <strong>gemeente of stad</strong>, "
                  "de <strong>provincie</strong>, de <strong>gemeenschappen en de gewesten</strong>, en de "
                  "<strong>federale overheid</strong>. Elk niveau heeft zijn eigen lijst bevoegdheden, en "
                  "buiten die lijst mag het niets beslissen. Geen enkel niveau mag dus over alles beslissen "
                  "wat het wil."),
            ("kader", "Op <strong>elk</strong> niveau vind je dezelfde twee soorten organen terug: een "
                      "<strong>verkozen raad die beslist</strong> en een <strong>bestuur dat uitvoert</strong>. "
                      "Alleen de namen verschillen. Ken je dat patroon, dan ken je meteen de helft van dit "
                      "hoofdstuk."),
        ]),
        dict(kop="De gemeente of stad", blokken=[
            ("p", "De gemeente is het bestuursniveau dat <strong>het dichtst bij de inwoners</strong> staat."),
            ("fig", tabel(["orgaan", "wat het doet"], [
                ["<strong>de gemeenteraad</strong>", "neemt de beslissingen en keurt de regels van de gemeente goed"],
                ["<strong>het college van burgemeester en schepenen</strong>", "of schepencollege; het dagelijks bestuur, dat uitvoert"],
            ]), "De leden van de gemeenteraad worden verkozen door de inwoners. Uit die raad komt daarna het college."),
            ("p", "Je stemt dus <strong>niet rechtstreeks op een burgemeester</strong>. Je stemt op kandidaten "
                  "voor de gemeenteraad, en wie daarna burgemeester wordt, hangt af van de meerderheid die "
                  "gevormd wordt."),
            ("p", "Naar het <strong>gemeentehuis</strong> ga je voor een nieuwe identiteitskaart, voor een "
                  "bouwvergunning, en om je te laten inschrijven als je verhuist. De gemeente regelt verder "
                  "het ophalen van het <strong>huisvuil</strong>, het onderhoud van de <strong>straten</strong> "
                  "in de gemeente en de <strong>gemeentelijke basisschool</strong>. Wil je een carport bouwen "
                  "naast je huis, dan vraag je bij je gemeente een <strong>omgevingsvergunning</strong> aan."),
        ]),
        dict(kop="De provincie", blokken=[
            ("p", "België telt <strong>tien provincies</strong>: vijf in Vlaanderen en vijf in Wallonië. Het "
                  "<strong>Brussels Hoofdstedelijk Gewest</strong> hoort bij géén enkele provincie."),
            ("fig", svg.gewesten(), "De tien provincies met hun hoofdplaats, en Brussel dat er los van staat."),
            ("fig", tabel(["orgaan", "wat het doet"], [
                ["<strong>de provincieraad</strong>", "de verkozen vergadering; neemt op provinciaal niveau de beslissingen"],
                ["<strong>de deputatie</strong>", "het dagelijks bestuur, met de gouverneur als voorzitter"],
                ["<strong>de gouverneur</strong>", "wordt benoemd, niet verkozen"],
            ]), "De provincieraad wordt op dezelfde dag verkozen als de gemeenteraad. Je krijgt die dag dus meer dan één stembiljet."),
            ("p", "Een provincie zorgt onder meer voor <strong>provinciale wegen en fietspaden</strong>, "
                  "<strong>provinciale domeinen en natuurgebieden</strong> en <strong>provinciale "
                  "scholen</strong>. Je identiteitskaart krijg je er niet: die komt van de gemeente."),
            ("weetje", "Zowel de gemeente als de provincie mag <strong>eigen belastingen</strong> heffen, "
                       "bovenop de federale. Daarom verschilt de belasting die je betaalt een beetje van "
                       "gemeente tot gemeente."),
        ]),
        dict(kop="De gemeenschappen en de gewesten", blokken=[
            ("p", "België telt <strong>drie gemeenschappen</strong> (de Vlaamse, de Franse en de Duitstalige) "
                  "en <strong>drie gewesten</strong> (het Vlaamse, het Waalse en het Brussels Hoofdstedelijk "
                  "Gewest). Het verschil is de moeite om vast te houden."),
            ("fig", tabel(["", "waarover het gaat", "voorbeelden"], [
                ["<strong>gemeenschap</strong>", "zaken die met <strong>personen en hun taal</strong> te maken hebben",
                 "onderwijs, cultuur, media, welzijn en gezondheidszorg"],
                ["<strong>gewest</strong>", "zaken die met het <strong>grondgebied</strong> te maken hebben",
                 "milieu en natuur, ruimtelijke ordening en wonen, economie, openbaar vervoer binnen het gewest"],
            ]), "Gaat het over grond, dan is het het gewest. Gaat het over mensen en taal, dan is het de gemeenschap."),
            ("p", "In <strong>Vlaanderen</strong> zijn de gemeenschap en het gewest samengevoegd tot één "
                  "<strong>Vlaams Parlement</strong> en één <strong>Vlaamse Regering</strong>. Het parlement "
                  "maakt de <strong>decreten</strong>; de regering met haar ministers voert uit wat het "
                  "parlement beslist."),
            ("p", "Een <strong>decreet</strong> is de wet van een gemeenschap of een gewest. Binnen zijn eigen "
                  "bevoegdheden heeft het <strong>evenveel kracht als een federale wet</strong>. Wie beslist "
                  "over jouw schooldoelen en je diploma? De <strong>Vlaamse Gemeenschap</strong>, want onderwijs "
                  "is gemeenschapsmaterie. De federale overheid mag daar niets over beslissen."),
            ("kader", "Er wordt beslist dat er een nieuw natuurgebied komt langs de Maas. Welk niveau? Het "
                      "<strong>gewest</strong>, want natuur is grondgebonden. Zo'n vraag los je altijd op met "
                      "diezelfde toets: gaat het over de grond, of over de mensen?"),
        ]),
        dict(kop="De federale overheid", blokken=[
            ("p", "De <strong>federale overheid</strong> regelt wat voor het hele land samen geldt: "
                  "<strong>justitie en de rechtbanken</strong>, <strong>defensie en het leger</strong>, "
                  "<strong>asiel en migratie</strong>, de <strong>pensioenen</strong>, de sociale zekerheid, "
                  "de buitenlandse handel en de volksgezondheid."),
            ("p", "Ook hier zijn er twee organen: het <strong>federale parlement</strong> met de "
                  "<strong>volksvertegenwoordigers</strong> (de wetgevende macht) en de <strong>federale "
                  "regering</strong> met haar <strong>ministers</strong> (de uitvoerende macht). Een "
                  "volksvertegenwoordiger is verkozen om in het parlement mee wetten te stemmen; een minister "
                  "hoort bij de uitvoerende macht en niet bij de wetgevende."),
            ("p", "De <strong>koning</strong> is het <strong>staatshoofd</strong>, maar hij bestuurt het land "
                  "niet zelf. Zijn rol is vooral symbolisch; de echte beslissingen liggen bij het parlement en "
                  "de regering."),
            ("weetje", "Verhuist je gezin naar een andere gemeente, dan schrijf je je in bij je nieuwe "
                       "<strong>gemeente</strong>, in het <strong>bevolkingsregister</strong>. Die inschrijving "
                       "past meteen je <strong>identiteitsgegevens</strong> aan, en die worden "
                       "<strong>federaal</strong> beheerd. Eén verhuis raakt dus twee niveaus tegelijk."),
        ]),
    ],
    onthoud=[
        "Vier niveaus: gemeente of stad, provincie, gemeenschappen en gewesten, federale overheid.",
        "Overal hetzelfde patroon: een verkozen raad die beslist en een bestuur dat uitvoert.",
        "Gemeente: gemeenteraad en het college van burgemeester en schepenen.",
        "Provincie: provincieraad en deputatie; de gouverneur wordt benoemd. Tien provincies, Brussel hoort bij geen enkele.",
        "Gemeenschap = personen en taal (onderwijs, cultuur, welzijn). Gewest = grondgebied (milieu, wonen, mobiliteit).",
        "Het Vlaams Parlement maakt decreten; die zijn even sterk als een federale wet.",
        "Federaal: justitie, defensie, asiel en migratie, pensioenen. De koning is staatshoofd maar bestuurt niet.",
    ],
)

# ───────────────────────────────────────── 6. De economische kringloop
BUNDELS["de-economische-kringloop"] = dict(
    vak=VAK, niveau=SPARK, titel="De economische kringloop",
    onder="Hoe gezinnen, bedrijven en de overheid met elkaar verbonden zijn, en wat er binnen een bedrijf en een gezin gebeurt.",
    secties=[
        dict(kop="Drie spelers, twee soorten stromen", blokken=[
            ("fig", svg.kringloop(),
             "De eenvoudige economische kringloop. Volg één pijl tegelijk en vraag je telkens af: bij wie begint hij, en bij wie eindigt hij?"),
            ("p", "De eenvoudige economische kringloop bestaat uit drie spelers: de <strong>gezinnen</strong>, "
                  "de <strong>bedrijven</strong> en de <strong>overheid</strong>. Tussen hen bewegen goederen, "
                  "diensten en geld: drie soorten stromen."),
            ("fig", tabel(["stroom", "wat er beweegt"], [
                ["<strong>goederenstroom</strong>", "het verplaatsen van een product van de ene speler naar de andere"],
                ["<strong>dienstenstroom</strong>", "een prestatie die geleverd wordt, zoals knippen of vervoeren"],
                ["<strong>geldstroom</strong>", "geld dat van de ene speler naar de andere gaat"],
            ]), "Bij elke goederenstroom loopt er in de omgekeerde richting meestal een geldstroom."),
            ("p", "Op het examen moet je van een gegeven stroom kunnen aanwijzen <strong>bij welke speler die "
                  "begint en bij welke speler die eindigt</strong>. Koop je brood bij de bakker, dan begint de "
                  "geldstroom bij het <strong>gezin</strong> en eindigt ze bij het <strong>bedrijf</strong>. "
                  "Krijgt je vader zijn loon van zijn werkgever, dan begint die geldstroom bij het "
                  "<strong>bedrijf</strong> en eindigt ze bij het <strong>gezin</strong>."),
            ("p", "Tussen een gezin en een bedrijf lopen er drie stromen tegelijk: <strong>arbeid</strong> van "
                  "het gezin naar het bedrijf, <strong>loon</strong> van het bedrijf naar het gezin, en "
                  "<strong>goederen en diensten</strong> van het bedrijf naar het gezin (met jouw betaling "
                  "terug). Zonder de gezinnen zouden de bedrijven dus geen arbeidskrachten én geen klanten "
                  "hebben."),
            ("kader", "De <strong>overheid</strong> hoort er wel degelijk bij, ook al verkoopt ze niets. Ze int "
                      "belastingen bij de gezinnen (belasting op het inkomen) én bij de bedrijven (belasting op "
                      "de winst), en ze geeft dat terug in uitkeringen, wegen en scholen. Ze koopt ook zelf "
                      "goederen en diensten en betaalt lonen aan haar personeel."),
            ("p", "Een <strong>consument</strong> is wie goederen en diensten koopt om zelf te gebruiken. Dat "
                  "zijn de gezinnen. De bedrijven zijn de <strong>producenten</strong>."),
        ]),
        dict(kop="Wat er in een bedrijf gebeurt", blokken=[
            ("p", "Elk bedrijf heeft dezelfde <strong>kernactiviteiten</strong>, of het nu twintig werknemers "
                  "heeft of twee. In een groot bedrijf is elke kernactiviteit een eigen "
                  "<strong>afdeling</strong>."),
            ("fig", tabel(["kernactiviteit", "wat er gebeurt"], [
                ["<strong>de aankoop</strong>", "zorgt ervoor dat de grondstoffen en het materiaal binnenkomen"],
                ["<strong>de algemene directie of zaakvoerder</strong>", "neemt de grote beslissingen en stuurt het geheel aan"],
                ["<strong>de boekhouding</strong>", "houdt bij wat er binnenkomt en buitengaat aan geld"],
                ["<strong>het magazijn</strong>", "bewaart de producten en grondstoffen tot ze nodig zijn"],
                ["<strong>de marketing</strong>", "zorgt dat klanten het product leren kennen en willen kopen"],
                ["<strong>het onthaal</strong>", "ontvangt de bezoekers en de telefoon"],
                ["<strong>de productie</strong>", "maakt het product"],
                ["<strong>de verkoop</strong>", "brengt het product bij de klant"],
            ]), "Het opslaan van de voorraad is dus het magazijn, niet de directie."),
            ("p", "In een <strong>klein bedrijf</strong> mag één persoon gerust meerdere kernactiviteiten "
                  "tegelijk doen. In een eenmanszaak doet de zaakvoerder vaak de aankoop, de verkoop en de "
                  "boekhouding zelf. De taken bestaan allemaal, alleen zijn de mensen dezelfde."),
        ]),
        dict(kop="De vier sectoren", blokken=[
            ("fig", svg.stappen(["primaire sector", "secundaire sector", "tertiaire sector", "quartaire sector"]),
             "Van grondstof naar product naar dienst. De quartaire sector staat er los van: dat zijn de diensten zonder winstoogmerk."),
            ("fig", tabel(["sector", "wat er gebeurt", "voorbeelden"], [
                ["<strong>primaire</strong>", "grondstoffen worden uit de natuur gehaald", "landbouw, visserij, bosbouw, mijnbouw"],
                ["<strong>secundaire</strong>", "grondstoffen worden verwerkt tot producten", "een fabriek die meubels maakt uit hout, de bouw"],
                ["<strong>tertiaire</strong>", "diensten waarvoor betaald wordt", "een kapsalon, een supermarkt, een transportbedrijf, een bank"],
                ["<strong>quartaire</strong>", "diensten zonder winstoogmerk", "een ziekenhuis, een school, het openbaar bestuur"],
            ]), "Een landbouwer die melk levert aan een zuivelfabriek zit in de primaire sector; de zuivelfabriek die er yoghurt van maakt, in de secundaire."),
        ]),
        dict(kop="Soorten goederen en soorten bedrijven", blokken=[
            ("fig", tabel(["soort", "wat het is", "voorbeeld"], [
                ["<strong>consumentengoed</strong>", "een goed dat een gezin koopt om zelf te gebruiken", "een paar schoenen, een brood, een gsm"],
                ["<strong>consumentendienst</strong>", "een dienst die je koopt voor jezelf", "een knipbeurt, een treinrit, een verzekering"],
                ["<strong>investeringsgoed</strong>", "een goed dat een bedrijf gebruikt om iets mee te maken", "een oven in een bakkerij, een vrachtwagen"],
            ]), "Hetzelfde voorwerp kan allebei zijn: een auto van een gezin is een consumentengoed, een auto van een koeriersdienst een investeringsgoed."),
            ("fig", tabel(["soort bedrijf", "wat het doet"], [
                ["<strong>productiebedrijf</strong>", "maakt zelf producten uit grondstoffen"],
                ["<strong>handelsbedrijf</strong>", "koopt producten in en verkoopt ze zonder ze te bewerken"],
                ["<strong>dienstenbedrijf</strong>", "levert diensten in plaats van producten"],
            ]), "Een supermarkt is een handelsbedrijf: ze maakt de yoghurt niet zelf."),
            ("p", "Een <strong>profitbedrijf</strong> heeft winst maken als doel; een "
                  "<strong>non-profitorganisatie</strong> niet. Een vzw of een ziekenfonds mag wel geld "
                  "overhouden, maar dat gaat terug naar de werking. Het verschil zit in het <strong>doel</strong>, "
                  "niet in wie er werkt: ook een non-profitorganisatie neemt personeel in dienst, en ook een "
                  "profitbedrijf mag dat natuurlijk."),
        ]),
        dict(kop="De inkomsten en uitgaven van een gezin", blokken=[
            ("fig", tabel(["soort inkomsten", "wat het is", "voorbeeld"], [
                ["<strong>terugkerende</strong>", "komen regelmatig binnen", "een loon, een pensioen, een uitkering, het groeipakket"],
                ["<strong>toevallige</strong>", "komen onverwacht en niet elke maand", "een erfenis, de opbrengst van iets dat je tweedehands verkoopt, een prijs die je wint"],
            ]), "Op terugkerende inkomsten kan een gezin rekenen, op toevallige niet."),
            ("fig", tabel(["soort uitgaven", "wat het is", "voorbeeld"], [
                ["<strong>vaste</strong>", "kosten telkens hetzelfde bedrag", "de huur, een abonnement, een verzekering"],
                ["<strong>variabele</strong>", "het bedrag verschilt elke keer", "de boodschappen van de week, de brandstof voor de auto"],
                ["<strong>onvoorziene</strong>", "je zag ze niet aankomen", "de wasmachine die stukgaat en vervangen moet worden"],
                ["<strong>uitzonderlijke</strong>", "groot en zeldzaam, maar je ziet ze aankomen", "een nieuwe keuken, een auto"],
            ]), "Let op het verschil tussen de laatste twee: een nieuwe keuken is uitzonderlijk, niet onvoorzien."),
        ]),
    ],
    onthoud=[
        "Drie spelers: de gezinnen, de bedrijven en de overheid.",
        "Bij elke goederenstroom loopt er meestal een geldstroom in de omgekeerde richting.",
        "Gezinnen leveren arbeid en krijgen loon; bedrijven leveren goederen en diensten en krijgen je betaling.",
        "Acht kernactiviteiten, van de aankoop tot de verkoop; het magazijn bewaart, de boekhouding telt.",
        "Vier sectoren: primair (grondstoffen), secundair (verwerken), tertiair (diensten met winst), quartair (diensten zonder winstoogmerk).",
        "Consumentengoed voor het gezin, investeringsgoed voor het bedrijf.",
        "Inkomsten: terugkerend of toevallig. Uitgaven: vast, variabel, onvoorzien of uitzonderlijk.",
    ],
)

# ───────────────────────────────────────── 7. De overheid in de economie
BUNDELS["de-overheid-in-de-economie"] = dict(
    vak=VAK, niveau=SPARK, titel="De overheid in de economie",
    onder="Waar de overheid haar geld haalt en waaraan ze het besteedt, en hoe de sociale zekerheid ongelijkheid kleiner maakt.",
    secties=[
        dict(kop="Waar de overheid haar geld haalt", blokken=[
            ("p", "De overheid haalt haar geld uit <strong>belastingen</strong> die gezinnen en bedrijven "
                  "betalen. De vakfiche noemt er zes."),
            ("fig", tabel(["inkomst", "wie betaalt ze, en wanneer"], [
                ["<strong>belasting op het gezinsinkomen</strong>", "elk gezin, op wat het verdient"],
                ["<strong>belasting op de bedrijfswinst</strong>", "elk bedrijf, op wat het overhoudt"],
                ["<strong>btw op een aankoop</strong>", "iedereen, bij bijna elke aankoop"],
                ["<strong>milieubelasting</strong>", "wie vervuilt; ze maakt vervuilend gedrag duurder"],
                ["<strong>belasting op een huis of gebouw</strong>", "wie een huis of gebouw in eigendom heeft"],
                ["<strong>wegenbelasting</strong>", "wie een auto heeft, elk jaar opnieuw"],
            ]), "Btw staat voor belasting over de toegevoegde waarde."),
            ("p", "De <strong>btw</strong> zit al in de prijs die op het prijskaartje staat: je betaalt ze mee "
                  "zonder het te merken. Het tarief is <strong>niet op alle producten hetzelfde</strong>. Het "
                  "gewone tarief is 21 procent, maar op onder meer voeding en boeken geldt een lager tarief, "
                  "zodat wat iedereen nodig heeft minder zwaar belast wordt."),
            ("weetje", "Het verschil tussen <strong>btw</strong> en <strong>wegenbelasting</strong> op een auto: "
                       "de btw betaal je één keer, bij de aankoop. De wegenbelasting betaal je elk jaar opnieuw, "
                       "zolang je de auto hebt."),
        ]),
        dict(kop="Waaraan de overheid haar geld besteedt", blokken=[
            ("fig", tabel(["uitgave", "waar je ze ziet"], [
                ["<strong>huisvesting en infrastructuur</strong>", "een nieuwe brug, een vernieuwde sociale woonwijk, wegen"],
                ["<strong>milieubescherming</strong>", "natuurbeheer, waterzuivering, afvalverwerking"],
                ["<strong>onderwijs</strong>", "de scholen en de leerkrachten"],
                ["<strong>recreatie, sport en cultuur</strong>", "de subsidie voor een gemeentelijk zwembad, een bibliotheek, een sporthal"],
                ["<strong>sociale bescherming</strong>", "uitkeringen en pensioenen"],
                ["<strong>veiligheid</strong>", "de politie, de brandweer, justitie"],
            ]), "De zes uitgavenposten uit de vakfiche. Onderwijs en sociale bescherming zijn de grootste."),
            ("p", "Geeft de overheid <strong>meer uit dan ze ontvangt</strong>, dan heeft dat gevolgen: ze moet "
                  "lenen, haar schuld groeit, en op die schuld betaalt ze rente. Dat geld kan ze nadien niet "
                  "meer aan iets anders besteden. Een gemeente met 8 miljoen euro inkomsten en 9 miljoen euro "
                  "uitgaven heeft dus een tekort van <strong>1 miljoen euro</strong>."),
            ("kader", "Op het examen krijg je cijfers en grafieken over de inkomsten en uitgaven. Onthoud één "
                      "rekenregel: <strong>procent betekent per honderd</strong>. Gaat er van elke 100 euro "
                      "30 euro naar onderwijs, dan is dat <strong>30 procent</strong>."),
            ("p", "De keuzes van de overheid <strong>werken door in de samenleving</strong>. Je ziet het aan "
                  "hoeveel je moet betalen voor school en openbaar vervoer, aan hoeveel fietspaden en groen er "
                  "in je gemeente zijn, en aan hoe lang je moet wachten op een sociale woning. Wordt er minder "
                  "aan openbaar vervoer besteed, dan merken de inwoners dat meteen: minder bussen, langer "
                  "wachten, of geen verbinding meer."),
            ("p", "Waarom is het belangrijk dat iedereen belastingen betaalt? Omdat we er samen de "
                  "<strong>voorzieningen</strong> mee betalen die we allemaal gebruiken: wegen, scholen, "
                  "ziekenhuizen, de brandweer. Vergeet daarbij niet dat de overheid <strong>naast een "
                  "speler die geld int ook zelf goederen en diensten koopt</strong>: ze bestelt bussen, "
                  "computers en bouwwerken en betaalt lonen aan haar personeel."),
        ]),
        dict(kop="Sociale ongelijkheid", blokken=[
            ("p", "<strong>Sociale ongelijkheid</strong> betekent dat mensen niet dezelfde kansen en middelen "
                  "hebben in een samenleving. De vakfiche noemt zes zaken die ze kunnen "
                  "<strong>veroorzaken</strong>."),
            ("fig", tabel(["oorzaak", "hoe je het ziet"], [
                ["<strong>discriminatie</strong>", "iemand wordt niet aangenomen voor een job omwille van zijn afkomst"],
                ["<strong>gewoontes in een cultuur</strong>", "wat in een groep als normaal geldt, sluit anderen uit"],
                ["<strong>gezondheid</strong>", "een langdurige ziekte brengt iemand in een moeilijkere positie"],
                ["<strong>inkomen en rijkdom</strong>", "wie meer heeft, kan meer opvangen"],
                ["<strong>onderwijs en de kansen om te leren</strong>", "een rustige plek en hulp bij het huiswerk thuis, of niet"],
                ["<strong>wetten en regels van de overheid</strong>", "een regel die voor iedereen gelijk lijkt, valt toch ongelijk uit"],
            ]), "De zes oorzaken uit de vakfiche."),
            ("p", "Twee kinderen met dezelfde punten op dezelfde school hebben daarom nog niet dezelfde kansen. "
                  "Heeft het ene thuis een rustige plek en hulp bij het huiswerk en het andere niet, dan is dat "
                  "<strong>sociale ongelijkheid door een verschil in kansen om te leren</strong>."),
        ]),
        dict(kop="De sociale zekerheid", blokken=[
            ("p", "De <strong>sociale zekerheid</strong> vangt op wat mensen niet zelf kunnen dragen. Ze werkt "
                  "op het <strong>solidariteitsprincipe</strong>: wie kan draagt bij, wie het nodig heeft wordt "
                  "geholpen. Je krijgt dus niet per se terug wat je zelf betaalde."),
            ("p", "Ze wordt <strong>niet</strong> volledig door de overheid alleen betaald. Van elk loon gaat "
                  "er een deel naartoe, de werkgever legt bij, en de overheid vult aan met belastinggeld. Ze "
                  "bestaat omdat <strong>iedereen ooit ziek, werkloos of oud kan worden</strong>. Wie dat nooit "
                  "overkomt, heeft niet voor niets bijgedragen: hij droeg mee voor anderen, en had zelf de "
                  "zekerheid dat hij opgevangen zou worden."),
            ("fig", tabel(["soort uitkering", "wat ze doet", "voorbeelden"], [
                ["<strong>vervangingsuitkering</strong>", "komt in de plaats van een inkomen dat weggevallen is",
                 "de werkloosheidsuitkering en het leefloon, het rust- en overlevingspensioen, de ziekte- en invaliditeitsuitkering, de arbeidsongevallenuitkering"],
                ["<strong>aanvullende uitkering</strong>", "komt bovenop het inkomen om bepaalde kosten te helpen dragen",
                 "het groeipakket, de ondersteuning voor mensen met een beperking, een sociaal tarief op basis van het inkomen, de tegemoetkoming voor medische kosten"],
            ]), "Het groeipakket is dus aanvullend en geen vervangingsuitkering."),
            ("p", "Verliest iemand zijn werk en krijgt hij maandelijks geld van de overheid tot hij nieuw werk "
                  "vindt, dan is dat een <strong>werkloosheidsuitkering</strong> en dus een "
                  "vervangingsuitkering. Betaalt een gezin met een laag inkomen minder voor elektriciteit dan "
                  "een gezin met een hoog inkomen, dan is dat een <strong>sociaal tarief op basis van het "
                  "inkomen</strong>, en dus aanvullend."),
            ("kader", "Zo <strong>vermindert de overheid sociale ongelijkheid</strong>: met uitkeringen voor "
                      "wie zijn inkomen verliest, met onderwijs dat voor iedereen toegankelijk is, en met een "
                      "sociaal tarief voor wie weinig verdient. Ze maakt de verschillen niet weg, ze maakt ze "
                      "kleiner."),
        ]),
    ],
    onthoud=[
        "Zes inkomsten: belasting op gezinsinkomen, op bedrijfswinst, btw, milieubelasting, belasting op een huis of gebouw, wegenbelasting.",
        "Zes uitgaven: huisvesting en infrastructuur, milieubescherming, onderwijs, recreatie sport en cultuur, sociale bescherming, veiligheid.",
        "Btw zit in de prijs; het tarief is niet overal hetzelfde.",
        "Meer uitgeven dan ontvangen betekent lenen, en lenen kost rente.",
        "Zes oorzaken van sociale ongelijkheid, van discriminatie tot de regels van de overheid zelf.",
        "Solidariteitsprincipe: wie kan draagt bij, wie het nodig heeft wordt geholpen.",
        "Vervangingsuitkering komt in de plaats van een loon; een aanvullende uitkering komt erbovenop.",
    ],
)

# ───────────────────────────────────────── 8. Ik beheer mijn financiën
BUNDELS["ik-beheer-mijn-financien"] = dict(
    vak=VAK, niveau=SPARK, titel="Ik beheer mijn financiën",
    onder="Waarom je koopt wat je koopt, hoe je een budget maakt, wat lenen kost, en hoe je veilig betaalt.",
    secties=[
        dict(kop="Reële en gecreëerde behoeften", blokken=[
            ("fig", tabel(["soort behoefte", "wat het is", "voorbeelden"], [
                ["<strong>reële behoefte</strong>", "iets dat je echt nodig hebt om te leven of te functioneren",
                 "eten en drinken, een warme jas in de winter, een plek om te wonen"],
                ["<strong>gecreëerde behoefte</strong>", "een behoefte die pas ontstaat door reclame of door je omgeving",
                 "de nieuwste kleur van een sneaker die je al hebt"],
            ]), "Het verschil zit niet in het voorwerp maar in de reden: heb je het nodig, of wil je het sinds je het zag?"),
            ("p", "Een gecreëerde behoefte is <strong>niet altijd iets slechts</strong> waar je nooit aan mag "
                  "toegeven. Je mag gerust eens iets kopen dat je niet strikt nodig hebt. Het punt is dat je "
                  "weet <em>waarom</em> je het koopt en dat het in je budget past."),
        ]),
        dict(kop="Wat je koopgedrag beïnvloedt", blokken=[
            ("p", "Er duwen voortdurend dingen aan je beslissing: <strong>reclame en influencers</strong>, "
                  "<strong>wat je vrienden hebben of vinden</strong>, een <strong>korting of een aanbod dat "
                  "bijna stopt</strong>, een merk, de verpakking, je gewoonte, of gewoon je humeur van dat "
                  "moment."),
            ("kader", "Staat er in een webshop \"nog 2 op voorraad, aanbod verloopt in 5 minuten\"? Dan word je "
                      "<strong>onder tijdsdruk gezet om snel te beslissen</strong>. Schaarste en haast zijn "
                      "verkooptrucs: ze halen het nadenken eruit. Neem juist dan even afstand."),
            ("p", "Wie <strong>vooraf nadenkt of hij iets echt nodig heeft</strong>, koopt doorgaans "
                  "doordachter. Dat is geen preek: het is gewoon zo dat een beslissing die je een dag laat "
                  "liggen er de volgende dag vaak anders uitziet."),
        ]),
        dict(kop="Een budgetplan en sparen", blokken=[
            ("p", "Een <strong>budgetplan</strong> is een overzicht van je inkomsten en je uitgaven. Zet ze "
                  "naast elkaar en je ziet meteen wat er overblijft."),
            ("fig", tabel(["rekenen met je budget", "hoe je het doet"], [
                ["hoeveel kan ik sparen?", "inkomsten min uitgaven. 40 euro zakgeld min 25 euro uitgaven is <strong>15 euro</strong>"],
                ["hoelang duurt mijn spaardoel?", "bedrag gedeeld door wat je per maand spaart. 300 euro fiets gedeeld door 25 euro is <strong>twaalf maanden</strong>"],
            ]), "Twee sommen die het hele onderdeel dragen."),
            ("p", "Wie elke maand een klein bedrag opzij zet, heeft een <strong>buffer voor onvoorziene "
                  "uitgaven</strong>. Precies dat spaarpotje maakt dat je niet moet lenen als de wasmachine "
                  "stukgaat."),
        ]),
        dict(kop="Lenen, rente en schuld", blokken=[
            ("p", "Een <strong>lening</strong> is geld dat je van iemand krijgt en later moet terugbetalen. "
                  "<strong>Rente</strong> is de prijs die je betaalt om dat geld te mogen lenen. Een "
                  "<strong>schuld</strong> is wat je nog moet terugbetalen."),
            ("fig", tabel(["onderdeel van een lening", "wat het is"], [
                ["<strong>het geleende bedrag</strong>", "wat je ontvangt bij de start"],
                ["<strong>de looptijd</strong>", "hoelang je erover doet om alles terug te betalen"],
                ["<strong>de rentevoet</strong>", "het percentage per jaar dat het lenen kost"],
                ["<strong>de totale rente</strong>", "alle rente samen, bovenop het geleende bedrag"],
                ["<strong>de totale terugbetaling</strong>", "het geleende bedrag plus de totale rente"],
                ["<strong>het maandelijks afbetalingsbedrag</strong>", "wat je elke maand overmaakt"],
                ["<strong>de nog openstaande schuld</strong>", "het deel van de lening dat je nog moet terugbetalen"],
            ]), "Leen je 1000 euro en betaal je in totaal 1150 euro terug, dan is de totale rente 150 euro."),
            ("p", "Een lening met een <strong>langere looptijd</strong> kost in totaal meestal meer, ook al is "
                  "het maandbedrag lager. Je betaalt namelijk langer rente. Een lager maandbedrag is dus niet "
                  "automatisch goedkoper: kijk naar de <em>totale terugbetaling</em>."),
            ("kader", "De <strong>risico's van te veel lenen</strong>: je kan je afbetalingen niet meer volgen, "
                      "je moet steeds meer rente betalen, en je kan in een <strong>schuldenspiraal</strong> "
                      "terechtkomen, waarbij je leent om af te betalen. Lenen voor iets dat je eigenlijk niet "
                      "nodig hebt, is daarom geen verstandige keuze: dan betaal je rente voor een gecreëerde "
                      "behoefte."),
            ("p", "Maak je een <strong>aankoopkeuze</strong>, hou dan rekening met drie dingen: je "
                  "<strong>budget</strong>, je <strong>spaardoel</strong>, en de eventuele <strong>kost van een "
                  "lening</strong>."),
        ]),
        dict(kop="Waar je koopt: de verkoopkanalen", blokken=[
            ("fig", tabel(["verkoopkanaal", "waar je op let"], [
                ["<strong>fysieke winkel</strong>", "je ziet en voelt het product voor je betaalt; wettelijke garantie"],
                ["<strong>webshop</strong>", "je ziet het product niet; wel veertien dagen bedenktijd"],
                ["<strong>markt</strong>", "vaak cash en zonder bewijs; vraag een ticket"],
                ["<strong>evenementen</strong>", "idem: haast en cash maken terugkomen moeilijk"],
                ["<strong>sociale media</strong>", "een particuliere verkoper geeft je geen garantie van een winkel"],
                ["<strong>teleshopping</strong>", "er wordt druk gezet om meteen te bestellen"],
            ]), "De zes verkoopkanalen uit de vakfiche."),
            ("p", "Bij een <strong>online aankoop</strong> heb je in principe <strong>veertien dagen "
                  "bedenktijd</strong> om ze terug te sturen. Dat heet het herroepingsrecht en het geldt bij "
                  "verkoop op afstand. Voor sommige zaken, zoals iets dat op maat gemaakt is, geldt het niet."),
            ("kader", "Ken je een <strong>webshop</strong> niet? Kijk dan of er een <strong>adres en een "
                      "telefoonnummer</strong> op de site staan, of de <strong>prijs niet verdacht veel "
                      "lager</strong> is dan elders, en of het <strong>webadres met https begint en juist "
                      "gespeld</strong> is. Mooie foto's zeggen niets: die kan iedereen kopiëren."),
        ]),
        dict(kop="Waarmee je betaalt: de betaalmiddelen", blokken=[
            ("fig", tabel(["betaalmiddel", "veiligheid, risico's en kosten"], [
                ["<strong>cash geld</strong>", "veilig tegen online fraude, maar kwijt of gestolen is definitief weg"],
                ["<strong>contactloos betalen</strong>", "snel; een klein bedrag kan doorgaans zonder je pincode, dus blokkeer een verloren kaart meteen"],
                ["<strong>debetkaart</strong>", "het geld gaat meteen van je rekening"],
                ["<strong>kredietkaart</strong> zoals Visa of Mastercard", "je betaalt later, dus je geeft makkelijker te veel uit"],
                ["<strong>overschrijving</strong>", "je stuurt het geld zelf weg; het is heel moeilijk terug te halen"],
                ["<strong>mobiele betaalapp</strong> zoals Bancontact Pay", "beveiligd met een code, je vingerafdruk of je gezicht"],
                ["<strong>prepaidkaart</strong>", "je zet er eerst geld op; je kan nooit meer verliezen dan wat erop staat"],
            ]), "De zeven betaalmiddelen uit de vakfiche."),
            ("p", "Koop je bij een <strong>onbekende verkoper</strong>, let dan op drie dingen: of je de "
                  "betaling kan laten <strong>terugdraaien</strong> als er iets misloopt, of er "
                  "<strong>kosten</strong> aan het betaalmiddel verbonden zijn, en of je <strong>niet meer kan "
                  "verliezen dan het bedrag van de aankoop</strong>."),
        ]),
        dict(kop="Fraude en bedrog herkennen", blokken=[
            ("p", "<strong>Signalen van bedrog</strong> bij een betaling: je moet betalen <strong>buiten het "
                  "systeem van de website om</strong>, er wordt <strong>haast</strong> op gezet en je krijgt "
                  "geen tijd, of er wordt naar je <strong>pincode of je codes</strong> gevraagd. Een factuur "
                  "met een btw-nummer is juist een teken van een echte verkoper."),
            ("p", "Krijg je een bericht dat je bankkaart geblokkeerd is en dat je via een link je gegevens moet "
                  "bevestigen? Dan is dat <strong>phishing</strong>: een vals bericht of een valse mail die je "
                  "gegevens of je codes wil bemachtigen. <strong>Klik niet op de link</strong> en contacteer "
                  "zelf je bank, via de app of het nummer dat je al kende. Je "
                  "<strong>pincode</strong> geef je nooit door aan de telefoon, ook niet aan iemand die zegt "
                  "dat hij van je bank is."),
            ("kader", "Merk je dat er <strong>geld van je rekening verdwenen</strong> is? Laat eerst je kaart "
                      "<strong>blokkeren</strong> en verwittig je bank, zodat het niet erger wordt. Doe daarna "
                      "<strong>aangifte bij de politie</strong>. Dat is niet zinloos: zonder aangifte kan je "
                      "bank je meestal niet vergoeden en kan de fraude niet opgespoord worden."),
        ]),
    ],
    onthoud=[
        "Reële behoefte: je hebt het nodig. Gecreëerde behoefte: reclame of je omgeving maakte ze.",
        "Tijdsdruk en schaarste in een webshop zijn verkooptrucs.",
        "Budgetplan = inkomsten naast uitgaven; wat overblijft, kan je sparen.",
        "Zeven onderdelen van een lening; een langere looptijd kost in totaal meestal meer.",
        "Zes verkoopkanalen; online heb je veertien dagen bedenktijd, in de winkel niet.",
        "Zeven betaalmiddelen; een overschrijving naar een onbekende is het moeilijkst terug te halen.",
        "Bij fraude: eerst blokkeren en je bank verwittigen, daarna aangifte doen.",
    ],
)

# ───────────────────────────────────────── 9. Digitaal communiceren en bestanden beheren
BUNDELS["digitaal-communiceren-en-bestanden-beheren"] = dict(
    vak=VAK, niveau=SPARK, titel="Digitaal communiceren en bestanden beheren",
    onder="De vormen van digitaal communiceren, de onderdelen van een e-mail, en hoe je mappen en bestanden ordent.",
    secties=[
        dict(kop="Vormen van digitaal communiceren", blokken=[
            ("fig", tabel(["vorm", "wat het is"], [
                ["<strong>e-mail</strong>", "een bericht dat blijft staan, met bijlagen; geschikt voor iets formeel"],
                ["<strong>sociale media</strong>", "berichten en beelden delen met een groep of met iedereen"],
                ["<strong>fora</strong>", "een plek online waar mensen per onderwerp vragen en antwoorden posten"],
                ["<strong>blogwebsites</strong>", "een site waarop iemand regelmatig eigen stukken publiceert"],
                ["<strong>online meeting</strong>", "een gesprek met beeld en geluid tussen meerdere mensen"],
                ["<strong>chatten</strong>", "korte berichten, met een snel antwoord verwacht"],
            ]), "De zes vormen uit de vakfiche. Op een forum zijn alle deelnemers gelijk; op een blog schrijft er één en lezen de anderen."),
            ("p", "Wanneer kies je een <strong>e-mail</strong> boven een chatbericht? Als je iets "
                  "<strong>formeel</strong> wil vragen en het <strong>bijgehouden</strong> moet worden. Een "
                  "mail blijft staan, kan bijlagen meenemen en mag wat langer op een antwoord wachten. Chatten "
                  "is voor het snelle en het losse."),
        ]),
        dict(kop="De onderdelen van een e-mail", blokken=[
            ("fig", tabel(["onderdeel", "wat je erin zet"], [
                ["<strong>aan</strong>", "wie de mail moet krijgen"],
                ["<strong>CC</strong>", "wie zichtbaar in kopie staat; iedereen ziet elkaars adres"],
                ["<strong>BCC</strong>", "wie onzichtbaar in kopie staat; de ontvangers zien elkaars adres niet"],
                ["<strong>de onderwerpregel</strong>", "kort waar de mail over gaat"],
                ["<strong>de aanhef</strong>", "Geachte mevrouw, Beste meneer, Hallo …"],
                ["<strong>de inhoud</strong>", "je boodschap zelf"],
                ["<strong>de slotgroet</strong>", "Met vriendelijke groeten"],
                ["<strong>de ondertekening</strong>", "je naam eronder"],
                ["<strong>de bijlage</strong>", "een bestand dat je met je e-mail meestuurt"],
            ]), "Stuur je een mail naar twintig mensen die elkaar niet kennen, gebruik dan BCC."),
            ("p", "Schrijf je aan iemand die je <strong>niet kent</strong>, begin dan met een nette aanhef zoals "
                  "<em>Geachte mevrouw</em>. Naar een vriend mag <em>Hallo</em>, maar niet naar een school of "
                  "een bedrijf. Sluit af met een <strong>slotgroet en je naam eronder</strong>, zodat de "
                  "ontvanger zeker weet van wie de mail komt. En vergeet de bijlage niet echt toe te voegen als "
                  "je ze vermeldt."),
        ]),
        dict(kop="Netjes en respectvol digitaal communiceren", blokken=[
            ("p", "Dezelfde regels gelden bij chatten, berichten sturen, sociale media, e-mail en "
                  "videogesprekken."),
            ("fig", tabel(["regel", "waarom"], [
                ["je bericht nalezen voor je het verstuurt", "een typfout of een verkeerd woord haal je er niet meer uit"],
                ["niet reageren in het heetst van je kwaadheid", "een bericht uit kwaadheid blijft staan"],
                ["geen kwetsende taal of scheldwoorden gebruiken", "online komt alles harder aan dan bedoeld"],
                ["niet alles in hoofdletters typen", "dat wordt online als roepen gelezen"],
            ]), "Ben je kwaad over een bericht van een klasgenoot? Wacht even en antwoord er pas later kalm op."),
            ("p", "Bij een <strong>online meeting</strong> test je vooraf je camera en je microfoon, kies je "
                  "een rustige plek en een neutrale achtergrond, en log je enkele minuten vroeger in. Je "
                  "<strong>microfoon zet je uit als je niet spreekt</strong>, zodat niemand jouw "
                  "achtergrondgeluid hoort."),
            ("kader", "Een bericht dat je in een <strong>groepschat</strong> zet, blijft daar niet vanzelf: "
                      "iedereen in de groep kan het doorsturen of er een schermafdruk van maken. En een "
                      "<strong>foto van een klasgenoot</strong> zet je niet online zonder het te vragen. Dat is "
                      "niet alleen hoffelijk, het is ook de wet."),
        ]),
        dict(kop="De Verkenner: mappen en bestanden", blokken=[
            ("p", "De <strong>Verkenner</strong> is het programma van Windows waarmee je mappen en bestanden "
                  "bekijkt en beheert."),
            ("fig", tabel(["begrip", "wat het is"], [
                ["<strong>de verkenner</strong>", "het programma waarin je je mappen en bestanden beheert"],
                ["<strong>het navigatievenster</strong>", "links: de boomstructuur van je schijven en mappen"],
                ["<strong>het detailvenster</strong>", "extra informatie over het bestand dat je geselecteerd hebt"],
                ["<strong>het bestand</strong>", "een verzameling gegevens met een naam en een extensie"],
            ]), "Aan de extensie zie je met welk soort bestand je te maken hebt: .docx is Word, .xlsx is Excel, .pdf is een pdf, .jpg een foto."),
            ("p", "Je kan mappen en bestanden <strong>maken, selecteren, verplaatsen, kopiëren, herbenoemen en "
                  "verwijderen</strong>. Bij <strong>kopiëren</strong> blijft het origineel staan, bij "
                  "<strong>verplaatsen</strong> niet. <strong>Herbenoemen</strong> verandert alleen de naam, "
                  "niet de inhoud. En een bestand dat je <strong>verwijdert</strong>, is niet meteen voorgoed "
                  "weg: het gaat eerst naar de prullenbak."),
            ("p", "Wil je meerdere bestanden in één keer naar een andere map verplaatsen, dan "
                  "<strong>selecteer je ze eerst allemaal samen</strong>: met de Ctrl-toets kies je losse "
                  "bestanden, met de Shift-toets een hele reeks. Daarna versleep je ze in één beweging. Twee "
                  "bestanden in <strong>dezelfde map</strong> mogen trouwens niet exact dezelfde naam hebben; "
                  "in twee verschillende mappen mag dat wel."),
        ]),
        dict(kop="Ordenen: structuur, namen en back-ups", blokken=[
            ("p", "Een <strong>logische mappenstructuur</strong> zet je mappen in duidelijke lagen, van "
                  "algemeen naar specifiek: School, dan het vak, dan het schooljaar. Zo weet je altijd waar "
                  "iets hoort, ook als je het een jaar later terugzoekt."),
            ("p", "Een goede <strong>bestandsnaam</strong> zegt waar het bestand over gaat, is kort en zonder "
                  "rare tekens, en gebruikt de <strong>datum in dezelfde vorm</strong> als de andere bestanden. "
                  "Schrijf je de datum als <strong>2027-03-08</strong>, dus jaar-maand-dag, dan sorteren je "
                  "bestanden vanzelf netjes op chronologische volgorde. Met 8-3-2027 loopt die volgorde door "
                  "elkaar."),
            ("fig", svg.pijlrichting("uploaden", "van jouw toestel|naar het internet", False),
             "Uploaden gaat omhoog, van jou naar een server. Downloaden is precies het omgekeerde: van het internet naar je eigen toestel."),
            ("p", "Haal je een werkblad van de website van je school naar je laptop, dan ben je aan het "
                  "<strong>downloaden</strong>. Zet je een taak op het leerplatform, dan ben je aan het "
                  "<strong>uploaden</strong>."),
            ("p", "Een <strong>back-up</strong> of <strong>reservekopie</strong> is een kopie op een "
                  "<strong>andere plaats</strong>, voor als het origineel verloren gaat. Een reservekopie op "
                  "dezelfde computer als het origineel beschermt je dus <strong>niet</strong>: gaat die "
                  "computer stuk of wordt hij gestolen, dan ben je allebei kwijt."),
            ("kader", "<strong>Cloudopslag</strong> zoals OneDrive of Google Drive bewaart je bestanden op een "
                      "server die je via het internet bereikt. De voordelen: je geraakt aan je bestanden van op "
                      "elk toestel, ze blijven bestaan als je laptop stukgaat, en je kan een map delen met "
                      "iemand anders. Het nadeel: zonder internetverbinding geraak je er niet aan."),
        ]),
    ],
    onthoud=[
        "Zes vormen: e-mail, sociale media, fora, blogwebsites, online meeting, chatten.",
        "E-mail: aan, CC, BCC, onderwerpregel, aanhef, inhoud, slotgroet, ondertekening, bijlage.",
        "CC is zichtbaar, BCC niet. Naar een grote groep onbekenden gebruik je BCC.",
        "Nalezen, afkoelen, geen scheldwoorden, geen hoofdletters: dat is netjes communiceren.",
        "Verkenner: links het navigatievenster, en het detailvenster met de gegevens van je bestand.",
        "Kopiëren laat het origineel staan, verplaatsen niet; herbenoemen verandert alleen de naam.",
        "Uploaden gaat naar het internet, downloaden komt ervandaan. Een back-up staat elders.",
    ],
)

# ───────────────────────────────────────── 10. Word, Excel, PowerPoint en veilig online
BUNDELS["word-excel-powerpoint-en-veilig-online"] = dict(
    vak=VAK, niveau=SPARK, titel="Word, Excel, PowerPoint en veilig online",
    onder="De drie kantoorprogramma's van het examen, en de regels in de digitale wereld.",
    secties=[
        dict(kop="Word: structuur en opmaak", blokken=[
            ("p", "De <strong>structuurelementen van een tekst</strong> zijn: een <strong>teken</strong>, een "
                  "<strong>woord</strong>, een <strong>regel</strong>, een <strong>zin</strong>, een "
                  "<strong>alinea</strong> en een <strong>pagina</strong>. Een <strong>alinea</strong> is een "
                  "stuk tekst dat eindigt waar je op Enter duwt: alles daartussen krijgt dezelfde "
                  "alineaopmaak."),
            ("fig", tabel(["soort opmaak", "wat erbij hoort"], [
                ["<strong>tekenopmaak</strong> (werkt op letters)",
                 "lettertype, tekengrootte, vet, cursief, onderstrepen, tekstkleur, markeren, superscript en subscript, doorhalen"],
                ["<strong>alineaopmaak</strong> (werkt op een hele alinea)", "regelafstand, uitlijning, inspringen"],
                ["<strong>paginaopmaak</strong> (werkt op de pagina van je document)", "marges, afdrukstand (staand of liggend)"],
            ]), "De marges en de afdrukstand horen dus bij de paginaopmaak, niet bij de alineaopmaak."),
            ("p", "<strong>Subscript</strong> zet een teken kleiner en lager (H<sub>2</sub>O), "
                  "<strong>superscript</strong> kleiner en hoger (m<sup>2</sup>). Een alinea die "
                  "<strong>uitgevuld</strong> is, sluit links én rechts recht aan op de marge; bij links "
                  "uitlijnen blijft de rechterkant rafelig."),
            ("p", "Verder kan je in Word een <strong>opsomming</strong> invoegen of wijzigen, een "
                  "<strong>koptekst en voettekst</strong> zetten, en een <strong>tabel</strong> ontwerpen met "
                  "randen en arcering. Een <strong>voettekst</strong> is tekst die onderaan elke pagina "
                  "herhaald wordt, bijvoorbeeld het paginanummer; een koptekst staat bovenaan."),
            ("weetje", "Bij het <strong>afdrukken</strong> kies je zelf de instellingen: de sortering, "
                       "enkelzijdig of dubbelzijdig, en in kleur of niet. Ben je klaar, sla je document dan op als "
                       "<strong>pdf</strong>: dan blijft de opmaak bij iedereen hetzelfde en kan niemand er "
                       "zomaar iets in veranderen."),
        ]),
        dict(kop="Excel: het rekenblad", blokken=[
            ("fig", tabel(["structuurelement", "wat het is"], [
                ["<strong>cel</strong>", "één vakje in het rekenblad"],
                ["<strong>celadres</strong>", "de kolomletter met het rijnummer, zoals B4"],
                ["<strong>bereik</strong>", "een groep cellen die bij elkaar horen, zoals A1 tot A10"],
                ["<strong>rij</strong>", "een horizontale lijn cellen, met een nummer"],
                ["<strong>kolom</strong>", "een verticale lijn cellen, met een letter"],
                ["<strong>werkblad</strong>", "één tabblad onderaan"],
                ["<strong>werkmap</strong>", "het bestand zelf, met al zijn werkbladen erin"],
            ]), "Een werkmap is dus het bestand; een werkblad is één tabblad daarin."),
            ("p", "Je kan die elementen <strong>opmaken</strong>: lettertype, randen en opvulling, de celinhoud "
                  "uitlijnen, de rijhoogte en de kolombreedte aanpassen, cellen samenvoegen en centreren, en de "
                  "tekststand draaien. Je kiest ook de juiste <strong>getalnotatie</strong>: "
                  "<strong>valuta</strong>, <strong>percentage</strong>, een aantal <strong>decimalen</strong>, "
                  "of <strong>datum en tijd</strong>."),
            ("fig", tabel(["formule", "wat ze doet"], [
                ["<strong>=SOM(A1:A10)</strong>", "telt alle getallen van A1 tot en met A10 op"],
                ["<strong>=A1+B1</strong>", "optellen"],
                ["<strong>=A1-B1</strong>", "aftrekken"],
                ["<strong>=A1*B1</strong>", "vermenigvuldigen, met het sterretje"],
                ["<strong>=A1/B1</strong>", "delen, met het schuine streepje"],
                ["<strong>=(A1+B1)*2</strong>", "met haakjes bepaal je wat eerst gerekend wordt"],
            ]), "Een formule in Excel begint altijd met een gelijkheidsteken. Zonder dat teken ziet Excel je formule als gewone tekst."),
        ]),
        dict(kop="PowerPoint: een presentatie", blokken=[
            ("p", "Bij een presentatie hou je rekening met het <strong>KISS-principe</strong>: "
                  "<em>keep it short and simple</em>."),
            ("fig", tabel(["KISS", "de regel"], [
                ["per dia", "maximaal <strong>zeven regels</strong>"],
                ["per regel", "maximaal <strong>zeven woorden</strong>"],
                ["het lettertype", "duidelijk leesbaar, meestal <strong>14 punt</strong>"],
            ]), "Op de dia staan steekwoorden; de uitleg komt van jou."),
            ("p", "Je <strong>volledige tekst op de dia zetten</strong> is dus geen goed idee, ook al vergeet "
                  "je dan niets: je publiek begint te lezen in plaats van te luisteren."),
            ("p", "De basisbewerkingen die je moet kennen: een <strong>nieuwe dia invoegen</strong>, dia's "
                  "<strong>verwijderen of dupliceren</strong>, <strong>diaovergangen en animaties</strong> "
                  "toevoegen, <strong>tekstvakken en vormen</strong> invoegen, en de "
                  "<strong>diavoorstelling starten</strong>."),
        ]),
        dict(kop="Ongepast gedrag op het internet", blokken=[
            ("fig", tabel(["wat het is", "waarover het gaat"], [
                ["<strong>haatberichten</strong>", "berichten die aanzetten tot haat tegen een persoon of een groep"],
                ["<strong>doxing</strong>", "iemands privégegevens online zetten zonder toestemming"],
                ["<strong>shaming</strong>", "iemand publiek vernederen of belachelijk maken"],
                ["<strong>exposing</strong>", "iets privé van iemand openbaar maken om die persoon te schaden"],
                ["<strong>sexting</strong>", "intieme foto's of berichten sturen"],
                ["<strong>fake news</strong>", "nieuws dat vals is maar als echt verspreid wordt"],
                ["<strong>canceling</strong>", "iemand collectief uitsluiten of boycotten na een uitspraak of daad"],
                ["<strong>grooming</strong>", "een volwassene die online het vertrouwen van een kind zoekt om misbruik te maken"],
            ]), "De acht vormen uit de vakfiche."),
            ("kader", "Vraagt iemand die je online leerde kennen om een <strong>intieme foto</strong> en zegt "
                      "hij dat het tussen jullie blijft? <strong>Niet sturen, het gesprek stoppen, en het aan "
                      "een vertrouwenspersoon zeggen.</strong> Zo'n belofte kan niemand houden. En een intieme "
                      "foto van iemand anders <strong>doorsturen is strafbaar</strong>, ook als je die zelf "
                      "gekregen hebt: verwijder ze en zeg het aan een volwassene die je vertrouwt."),
            ("p", "Word je online lastiggevallen, maak dan een <strong>schermafdruk</strong> en "
                  "<strong>meld</strong> het. De schermafdruk is je bewijs, ook als het bericht later "
                  "verdwijnt. Meld het bij het platform zelf én vertel het aan iemand die je vertrouwt."),
        ]),
        dict(kop="Internetfraude en je gegevens beschermen", blokken=[
            ("fig", tabel(["vorm van internetfraude", "hoe ze binnenkomt"], [
                ["<strong>phishing</strong>", "via een e-mail"],
                ["<strong>smishing</strong>", "via een sms"],
                ["<strong>quishing</strong>", "via een QR-code die naar een valse website leidt"],
                ["<strong>vishing</strong>", "via een telefoongesprek; <em>voice</em>"],
            ]), "Alle vier probeert een bedrieger je er hetzelfde mee te vangen: je gegevens of je codes."),
            ("p", "Krijg je een mail met een link en de melding dat je pakje vastzit tot je een klein bedrag "
                  "betaalt? <strong>Negeer de mail en kijk zelf je zending na bij de vervoerder.</strong> Ga "
                  "altijd zelf naar de app of de site die je al kende; klik nooit op de link in zo'n bericht. "
                  "Bij een telefoontje leg je op en bel je zelf terug naar een nummer dat je al had."),
            ("p", "Je <strong>persoonlijke gegevens bescherm je</strong> met een <strong>sterk "
                  "wachtwoord</strong>, met <strong>authenticatie of verificatie</strong>, en met "
                  "<strong>tweestapsverificatie</strong>. Bij tweestapsverificatie geef je naast je wachtwoord "
                  "nog een tweede bewijs, zoals een code op je gsm. Zelfs wie je wachtwoord kent, geraakt er "
                  "dan niet in."),
            ("fig", tabel(["de regels van een sterk wachtwoord", ""], [
                ["minstens <strong>8</strong> karakters lang", "maximaal <strong>24</strong> karakters lang"],
                ["minstens één <strong>hoofdletter</strong>", "minstens één <strong>kleine letter</strong>"],
                ["minstens één <strong>cijfer</strong>", "minstens één <strong>teken</strong>, zoals ! # $ % &amp; * + - ? @"],
            ]), "Een wachtwoord als wachtwoord123 voldoet niet: er zit geen hoofdletter en geen teken in, en het staat in elke lijst van meest gebruikte wachtwoorden."),
        ]),
    ],
    onthoud=[
        "Tekenopmaak werkt op letters, alineaopmaak op een alinea, paginaopmaak op de pagina.",
        "Subscript is lager (H2O), superscript is hoger (m2). Uitgevuld sluit links en rechts recht aan.",
        "Excel: cel, celadres, bereik, rij, kolom, werkblad, werkmap. Een werkmap is het bestand.",
        "Elke formule begint met een gelijkheidsteken; =SOM(A1:A10) telt een bereik op.",
        "KISS: zeven regels per dia, zeven woorden per regel, meestal 14 punt.",
        "Acht vormen van ongepast gedrag, van haatberichten tot grooming.",
        "Phishing via mail, smishing via sms, quishing via QR-code, vishing via telefoon.",
        "Sterk wachtwoord: 8 tot 24 karakters, met hoofdletter, kleine letter, cijfer en teken.",
    ],
)

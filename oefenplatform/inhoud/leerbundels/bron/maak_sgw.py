# -*- coding: utf-8 -*-
"""De leerbundels bij sociale en gedragswetenschappen op 🌍 Beyond doorstroom.

Gebaseerd op de vakfiche `2027_Sociale_en_gedragswetenschappen_3DDG`, geldig
vanaf 1 januari 2027. Bladzijde 1 zegt voor welke richting ze geldt:
welzijnswetenschappen. Er bestaat een tweede fiche voor humane wetenschappen
(`_3DDO`), die voor ongeveer drie kwart gelijk is aan deze.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim laadt de bundel dus
twee keer op, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../beyond/sociale-en-gedragswetenschappen.json`
doet daar het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-beyond-doorstroom", de slug van de categorie.
Beheer → Leerstof leest die slug uit de bestandsnaam en zoekt dan enkel in die
categorie naar het hoofdstuk.

Wat hier vastligt en door niemand aangevuld mag worden, zijn de eigennamen en
hun theorieën. Deze fiche noemt er veertig, van Freud tot Hjarvard, en bij elke
naam staat er precies één theorie. Zet er geen naam bij die niet in de fiche
staat, en hang aan een naam geen onderzoek dat de fiche niet vermeldt. Dat is
hier de gevaarlijkste fout die je kan maken: een verzonnen experiment bij een
echte onderzoeker leest als een feit.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, svg

VAK = "Sociale en gedragswetenschappen"
BEYOND = "🌍 Beyond doorstroom — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 1. Ontwikkelingspsychologie: begrippen en basisvragen
BUNDELS["ontwikkelingspsychologie-de-begrippen-en-de-drie-basisvragen-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Ontwikkelingspsychologie: de begrippen en de drie basisvragen",
    onder="Wat ontwikkeling is, in welke levensloopfase iemand zit, welke vijf domeinen er zijn, en de drie vragen waarmee je elke theorie kan meten.",
    secties=[
        dict(kop="Groeien, rijpen en leren", blokken=[
            ("p", "De fiche vat <strong>ontwikkeling</strong> samen als een combinatie van drie dingen: "
                  "<strong>groeien</strong>, <strong>rijpen</strong> en <strong>leren</strong>. Die drie "
                  "woorden komen bij elke benadering terug, dus het is de moeite ze scherp te houden."),
            ("p", tabel(["Woord", "Wat het is", "Voorbeeld"], [
                ["groeien", "de zichtbare toename van je lichaam",
                 "in een jaar zeven centimeter langer worden"],
                ["rijpen", "ontwikkeling die van binnenuit komt en een vaste orde volgt",
                 "kunnen stappen zodra de zenuwbanen klaar zijn"],
                ["leren", "verandering door ervaring en oefening",
                 "de tafel van zeven uit het hoofd kennen"],
            ])),
            ("kader", "<strong>Rijpen kan je niet versnellen door te oefenen.</strong> Een baby van zes "
                      "maanden leert niet stappen omdat je meer oefent, maar omdat zijn lichaam er klaar "
                      "voor is. Dat is het verschil met leren."),
            ("p", "Het verband met <strong>nature</strong> en <strong>nurture</strong> is eenvoudig: "
                  "<strong>groeien en rijpen horen bij nature</strong>, de erfelijke kant, en "
                  "<strong>leren hoort bij nurture</strong>, alles wat de omgeving aanbrengt."),
        ]),
        dict(kop="De negen levensloopfasen", blokken=[
            ("p", "De fiche noemt <strong>negen</strong> levensloopfasen, in deze orde:"),
            ("p", tabel(["Fase", "Andere naam uit de fiche"], [
                ["prenatale fase", "de tijd voor de geboorte"],
                ["babytijd", ""],
                ["peutertijd", ""],
                ["vroege kindertijd", "de kleutertijd"],
                ["midden kindertijd", "de lagere schoolkindfase"],
                ["adolescentie", ""],
                ["vroege volwassenheid", ""],
                ["midden volwassenheid", ""],
                ["late volwassenheid", ""],
            ])),
            ("p", "Het woord <strong>levensloop</strong>fase is belangrijk: ontwikkeling begint al "
                  "<strong>voor de geboorte</strong> en stopt <strong>niet</strong> aan het einde van de "
                  "adolescentie. Er komen nog drie fasen van volwassenheid na."),
            ("weetje", "De fiche zet bij twee fasen zelf een tweede naam: de vroege kindertijd is de "
                       "kleutertijd, de midden kindertijd is de lagere schoolkindfase. Beide namen kunnen "
                       "in een vraag staan."),
        ]),
        dict(kop="De vijf ontwikkelingsdomeinen", blokken=[
            ("p", "Binnen elke fase kijkt de ontwikkelingspsychologie naar <strong>vijf domeinen</strong>:"),
            ("p", tabel(["Domein", "Waarover het gaat", "Voorbeeld"], [
                ["fysieke ontwikkeling", "lichaam, groei, motoriek", "zelf je veters knopen"],
                ["cognitieve ontwikkeling", "denken, onthouden, taal, rekenen", "een som in je hoofd maken"],
                ["morele ontwikkeling", "goed en kwaad, eerlijkheid",
                 "uitleggen waarom spieken niet eerlijk is"],
                ["socio-emotionele ontwikkeling", "gevoelens en omgang met anderen",
                 "je boosheid in woorden zeggen"],
                ["persoonlijkheidsontwikkeling", "wie je wordt als persoon", "weten waar je voor staat"],
            ])),
            ("kader", "De domeinen staan <strong>niet los van elkaar</strong>. Wie moeilijk spreekt, durft "
                      "minder zeggen in de klas en maakt daardoor minder vrienden: het fysieke domein werkt "
                      "door in het socio-emotionele. Die <strong>wisselwerking</strong> moet je in een "
                      "voorbeeld kunnen aanwijzen."),
            ("p", "Je kan ook de andere kant op kijken: <strong>één domein door verschillende fasen "
                  "heen</strong> volgen, en de fasen zo met elkaar vergelijken. De fiche vraagt dat met "
                  "zoveel woorden."),
        ]),
        dict(kop="De drie basisvragen", blokken=[
            ("p", "De ontwikkelingspsychologie stelt <strong>drie basisvragen</strong>. Ze zijn je "
                  "<strong>meetlat</strong>: leg je ze bij elke benadering, dan zie je waar de theorieën "
                  "verschillen."),
            ("p", tabel(["Basisvraag", "Wat ze tegenover elkaar zet"], [
                ["1. Verloopt ontwikkeling continu of discontinu?",
                 "beetje bij beetje, of in duidelijke stadia met een overgang ertussen"],
                ["2. Wat is de rol van nature, nurture en zelfbepaling?",
                 "de genen, de omgeving, en wat iemand zelf kiest"],
                ["3. Is ontwikkeling cultureel bepaald of universeel?",
                 "verschillend per samenleving, of hetzelfde bij alle mensen"],
            ])),
            ("p", "Bij de tweede vraag staan er <strong>drie</strong> dingen, geen twee. Naast de "
                  "genetische en de omgevingsfactoren noemt de fiche uitdrukkelijk de "
                  "<strong>zelfbepaling</strong>: een mens kiest ook zelf mee."),
            ("p", "Een voorbeeld waarin je alle drie ziet: iemand komt uit een muzikaal gezin "
                  "(nature én nurture), zat van haar zesde in de muziekschool (nurture) en koos op haar "
                  "vijftiende zelf om drum te spelen in plaats van piano (zelfbepaling)."),
            ("weetje", "Dat baby's over de hele wereld eerst kruipen en dan stappen, wijst op een "
                       "<strong>universele</strong> factor. Op welke leeftijd een kind geacht wordt zelf te "
                       "beslissen, verschilt sterk van samenleving tot samenleving: dat is een "
                       "<strong>culturele</strong> factor."),
        ]),
    ],
    onthoud=[
        "Ontwikkeling is groeien plus rijpen plus leren. Groeien en rijpen horen bij nature, leren bij nurture.",
        "Rijpen volgt een eigen orde en is niet te versnellen met oefenen.",
        "Negen levensloopfasen, van de prenatale fase tot de late volwassenheid.",
        "Vijf domeinen: fysiek, cognitief, moreel, socio-emotioneel en persoonlijkheid. Ze beïnvloeden elkaar.",
        "Drie basisvragen: continu of discontinu, nature-nurture-zelfbepaling, cultureel of universeel.",
    ],
)

# ───────────────────────── 2. Biologische en psychodynamische benadering
BUNDELS["ontwikkeling-de-biologische-en-de-psychodynamische-benadering-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Ontwikkeling: de biologische en de psychodynamische benadering",
    onder="Twee van de zes benaderingen: de ene begint bij de genen, de andere bij wat binnen in iemand speelt. Met Darwin, Gesell, Waddington, Freud en Erikson.",
    secties=[
        dict(kop="De biologische benadering", blokken=[
            ("p", "De <strong>biologische benadering</strong> legt het begin van ontwikkeling in het "
                  "<strong>lichaam zelf</strong>: de genen, de rijping en de erfelijkheid. Drie theorieën "
                  "horen erbij, elk met één naam uit de fiche:"),
            ("p", tabel(["Theorie", "Naam", "Kern"], [
                ["evolutionaire psychologie", "Charles Darwin",
                 "gedrag dat onze voorouders hielp overleven, is doorgegeven"],
                ["rijpingstheorie", "Arnold Gesell",
                 "ontwikkeling komt van binnenuit en volgt een vaste orde"],
                ["epigenetica", "Conrad Waddington",
                 "de omgeving zet genen aan of uit, zonder het DNA te veranderen"],
            ])),
            ("p", "De <strong>evolutionaire psychologie</strong> verklaart bijvoorbeeld waarom baby's over "
                  "de hele wereld schrikken van een plots hard geluid: dat hielp overleven. Ze legt dus de "
                  "nadruk op <strong>nature</strong>."),
            ("p", "De <strong>rijpingstheorie</strong> van Gesell werkt met gemiddelde leeftijden: op welke "
                  "leeftijd kinderen doorgaans zitten, kruipen en stappen. Omdat ze met vaste stappen in een "
                  "vaste orde werkt, antwoordt ze op de eerste basisvraag eerder <strong>discontinu</strong>."),
            ("p", "De <strong>epigenetica</strong> is de meest verrassende van de drie. Ze hoort bij de "
                  "biologische benadering omdat ze bij de genen vertrekt, en tóch geeft ze de omgeving veel "
                  "plaats: zware stress tijdens een zwangerschap kan bepaalde genen van het kind anders doen "
                  "werken. <strong>Het DNA zelf blijft hetzelfde</strong>; wat verandert is welke genen aan "
                  "of uit staan."),
            ("kader", "Daarom moet je de drie theorieën <strong>vergelijken</strong> en niet op één hoop "
                      "gooien: de epigenetica laat veel meer ruimte voor de omgeving dan de rijpingstheorie. "
                      "Ze geven dus niet hetzelfde antwoord op de drie basisvragen. Ze kijken wel alle drie "
                      "vooral naar wat <strong>universeel</strong> is, want wat in de genen zit, geldt in "
                      "principe voor alle mensen."),
            ("p", "Het bezwaar tegen een volledig biologische verklaring: ze krijgt het moeilijk om uit te "
                  "leggen waarom <strong>twee kinderen met dezelfde genen</strong> in een ander gezin zo "
                  "anders opgroeien. Van de drie theorieën kan enkel de <strong>epigenetica</strong> dat."),
        ]),
        dict(kop="De psychodynamische benadering", blokken=[
            ("p", "<strong>Psychodynamisch</strong> betekent dat er <strong>krachten binnen in iemand "
                  "werken</strong>, en dat die de ontwikkeling in beweging zetten. Twee theorieën horen erbij:"),
            ("p", tabel(["Theorie", "Naam", "Aantal fasen"], [
                ["de psychoanalyse", "Sigmund Freud", "5"],
                ["de psychosociale ontwikkelingstheorie", "Erik Erikson", "8"],
            ])),
            ("p", "Dat verschil tussen <strong>vijf en acht</strong> fasen wordt vaak gevraagd, dus zet het "
                  "goed vast."),
        ]),
        dict(kop="Freud: zones en fixatie", blokken=[
            ("p", "Bij Freud hangt elke fase aan een <strong>erogene lichaamszone</strong>: het lichaamsdeel "
                  "waar het plezier en de aandacht in die periode op gericht zijn."),
            ("p", "Loopt een fase niet goed af, dan kan er een <strong>fixatie</strong> ontstaan: iemand "
                  "blijft met een stuk van zich in die vroegere fase hangen, ook later in zijn leven."),
            ("p", "Het veelgenoemde bezwaar tegen de psychoanalyse: wat ze beschrijft is "
                  "<strong>moeilijk met onderzoek te meten</strong>, en Freud bouwde zijn theorie op de "
                  "mensen die bij hem in behandeling waren."),
        ]),
        dict(kop="Erikson: crisis, positieve en negatieve pool", blokken=[
            ("p", "Bij Erikson hoort bij elke fase een <strong>crisis</strong>: een vraag of spanning die in "
                  "die fase opgelost moet worden om verder te kunnen. Een crisis is dus "
                  "<strong>geen ramp maar een opdracht</strong>."),
            ("p", "Elke crisis heeft twee uitkomsten, die de fiche de <strong>positieve pool</strong> en de "
                  "<strong>negatieve pool</strong> noemt. Loopt de crisis goed af, dan kom je bij de "
                  "positieve pool. Loopt ze slecht af, dan laat de fase iets achter waar iemand later nog "
                  "last van kan hebben."),
            ("p", "Twee verschillen met Freud zijn belangrijk. Ten eerste lopen de fasen van Erikson "
                  "<strong>door tot in de late volwassenheid</strong>: ook een zestiger die terugkijkt op "
                  "zijn leven, zit in een fase. Ten tweede geeft Erikson veel meer plaats aan de "
                  "<strong>mensen rond iemand</strong>. Daarom heet zijn theorie <strong>psycho</strong>, "
                  "voor wat binnen in iemand speelt, plus <strong>sociaal</strong>, voor de omgeving."),
            ("kader", "Op de <strong>eerste basisvraag</strong> antwoorden Freud en Erikson beide "
                      "<strong>discontinu</strong>: ze werken met vaste fasen. Op de "
                      "<strong>tweede</strong> antwoorden ze <strong>niet</strong> hetzelfde: Erikson "
                      "rekent de omgeving veel zwaarder mee."),
            ("p", "Wat de biologische en de psychodynamische benadering met elkaar gemeen hebben: beide "
                  "leggen het begin van ontwikkeling <strong>in het individu zelf</strong>. Bij de ene zit "
                  "de motor in de genen, bij de andere binnen in de persoon. Geen van beide begint bij de "
                  "omgeving."),
        ]),
    ],
    onthoud=[
        "Biologisch: Darwin (evolutionair), Gesell (rijping), Waddington (epigenetica).",
        "Epigenetica: de omgeving zet genen aan of uit; het DNA zelf verandert niet.",
        "Psychodynamisch: Freud met 5 fasen, erogene zone en fixatie; Erikson met 8 fasen, crisis en twee polen.",
        "Erikson loopt door tot de late volwassenheid en rekent de omgeving mee; Freud niet.",
        "Beide benaderingen leggen de motor van ontwikkeling in het individu zelf.",
    ],
)

# ───────────────────────── 3. Behavioristische en cognitieve benadering
BUNDELS["ontwikkeling-de-behavioristische-en-de-cognitieve-benadering-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Ontwikkeling: de behavioristische en de cognitieve benadering",
    onder="Twee benaderingen over leren: de ene kijkt naar wat je van buitenaf kan meten, de andere naar wat er in het hoofd gebeurt. Met Pavlov, Watson, Skinner, Bandura en Piaget.",
    secties=[
        dict(kop="Klassieke conditionering", blokken=[
            ("p", "Het <strong>behaviorisme</strong> wil alleen uitspraken doen over wat je kan "
                  "<strong>waarnemen</strong>: gedrag. Twee vormen van conditionering horen erbij, en de "
                  "eerste is de <strong>klassieke conditionering</strong> van <strong>Ivan Pavlov</strong> "
                  "en <strong>John B. Watson</strong>."),
            ("p", "Ze werkt met het <strong>S-R-schema</strong>: een <strong>S</strong>timulus is een "
                  "prikkel, een <strong>R</strong>espons is de reactie erop. Het beroemde experiment van "
                  "Pavlov met zijn honden laat de vier begrippen zien:"),
            ("p", tabel(["Begrip", "In het experiment van Pavlov"], [
                ["ongeconditioneerde stimulus", "het vlees: het werkt vanzelf, zonder iets te leren"],
                ["ongeconditioneerde reflex", "het kwijlen bij het vlees"],
                ["neutrale stimulus", "het belletje, voor het experiment begint: het doet nog niets"],
                ["geconditioneerde stimulus", "hetzelfde belletje, na vele keren koppelen aan het vlees"],
                ["geconditioneerde reflex", "het kwijlen bij het belletje alleen"],
            ])),
            ("kader", "Een <strong>neutrale</strong> stimulus wordt dus een <strong>geconditioneerde</strong> "
                      "stimulus door ze telkens samen met de ongeconditioneerde stimulus aan te bieden. "
                      "<strong>On</strong>geconditioneerd betekent niet geleerd, geconditioneerd betekent wel."),
            ("p", "Het <strong>Little Albert-experiment</strong> van Watson hoort bij diezelfde klassieke "
                  "conditionering: een jongetje werd bang gemaakt voor iets waar het eerst niet bang voor "
                  "was, door dat te koppelen aan een hard geluid. De fiche noemt het experiment als "
                  "geschiedenis van het vak. <strong>Vandaag zou het nooit door een ethische commissie "
                  "komen</strong>: een kind opzettelijk bang maken, kan niet."),
        ]),
        dict(kop="Operante conditionering", blokken=[
            ("p", "<strong>B.F. Skinner</strong> voegt aan het schema een derde letter toe: het "
                  "<strong>S-R-C-schema</strong>, waar de <strong>C</strong> staat voor "
                  "<strong>consequentie</strong>, het gevolg van het gedrag. Bij hem wordt gedrag dus "
                  "gestuurd door wat erna komt, en niet door het koppelen van prikkels."),
            ("p", "Hij werkte met de <strong>Skinner-box</strong>, een kooitje waarin een proefdier zelf "
                  "ontdekt dat duwen op een knop voedsel oplevert."),
            ("p", "Er zijn vier soorten gevolg, en hier zit de klassieke valkuil. "
                  "<strong>Positief betekent toevoegen, negatief betekent wegnemen.</strong> Ze zeggen dus "
                  "niets over leuk of niet leuk. <strong>Bekrachtiging</strong> doet gedrag "
                  "<strong>toenemen</strong>, <strong>straf</strong> doet het <strong>afnemen</strong>:"),
            ("p", tabel(["Soort", "Wat gebeurt er", "Gevolg voor het gedrag", "Voorbeeld"], [
                ["positieve bekrachtiging", "iets aangenaams komt bij", "neemt toe",
                 "een sticker voor wie opruimt"],
                ["negatieve bekrachtiging", "iets onaangenaams gaat weg", "neemt toe",
                 "geen vaat in de week dat je al je taken maakt"],
                ["positieve straf", "iets onaangenaams komt bij", "neemt af",
                 "een standje als de hond op de zetel springt"],
                ["negatieve straf", "iets aangenaams gaat weg", "neemt af",
                 "een week niet gamen na een leugen"],
            ])),
            ("kader", "Werk altijd in twee stappen. <strong>Eerst</strong>: neemt het gedrag toe of af? Toe "
                      "is bekrachtiging, af is straf. <strong>Dan</strong>: komt er iets bij of gaat er iets "
                      "weg? Bij is positief, weg is negatief."),
            ("p", "Op de <strong>tweede basisvraag</strong> antwoordt het behaviorisme duidelijk "
                  "<strong>nurture</strong>: voor het behaviorisme is bijna alles geleerd, en leren komt van "
                  "buitenaf."),
        ]),
        dict(kop="Bandura, de voorloper", blokken=[
            ("p", "De <strong>cognitieve benadering</strong> kijkt naar wat er <strong>in het hoofd</strong> "
                  "met informatie gebeurt. De fiche noemt de <strong>sociaal-cognitieve leertheorie</strong> "
                  "van <strong>Albert Bandura</strong> een <strong>voorloper</strong> van die benadering."),
            ("p", "Bij Bandura leert iemand door te <strong>kijken</strong> naar wat een ander doet. Dat "
                  "heet <strong>modelleren</strong> of <strong>imitatieleren</strong>. Zijn bekendste "
                  "experiment is het <strong>Bobo doll experiment</strong>: kinderen die een volwassene "
                  "zagen slaan op een opblaaspop, sloegen daarna zelf ook."),
            ("p", "Waarom is hij geen zuiver behaviorist? Omdat bij hem leren ook gebeurt "
                  "<strong>zonder dat het kind zelf bekrachtigd wordt</strong>. Er gebeurt dus iets in het "
                  "hoofd: kijken, opslaan, later toepassen."),
        ]),
        dict(kop="Piaget: vier stadia", blokken=[
            ("p", "<strong>Jean Piaget</strong> onderscheidt <strong>vier stadia</strong> in de cognitieve "
                  "ontwikkeling. Ze volgen een <strong>vaste orde</strong> en een kind slaat er geen over. "
                  "Daarom is zijn theorie een antwoord van <strong>discontinuïteit</strong> op de eerste "
                  "basisvraag."),
            ("p", tabel(["Stadium", "Wat erin kan", "Voorbeeld"], [
                ["sensomotorisch", "leren via de zintuigen en de beweging",
                 "een baby die alles in zijn mond stopt"],
                ["pre-operationeel", "denken met beelden en woorden, nog niet logisch",
                 "een kleuter die denkt dat een hoge smalle beker meer bevat"],
                ["concreet-operationeel", "logisch denken over tastbare dingen",
                 "rekenen met blokjes lukt, met letters niet"],
                ["formeel-operationeel", "abstract denken, over wat er niet is",
                 "nadenken over een wet die nog niet bestaat"],
            ])),
            ("weetje", "Senso staat voor de zintuigen, motorisch voor de beweging. Vandaar de naam van het "
                       "eerste stadium."),
        ]),
        dict(kop="De informatieverwerkingstheorie", blokken=[
            ("p", "De derde theorie van de cognitieve benadering heeft geen naam van een persoon bij zich. "
                  "Ze beschrijft hoe informatie door <strong>drie soorten geheugen</strong> gaat:"),
            ("p", tabel(["Geheugen", "Wat het doet"], [
                ["sensorisch geheugen", "vangt heel kort op wat je zintuigen binnenbrengen"],
                ["kortetermijngeheugen", "houdt even vast waar je nu mee bezig bent"],
                ["langetermijngeheugen", "bewaart wat blijft"],
            ])),
            ("p", "Het <strong>langetermijngeheugen</strong> valt in twee delen uiteen:"),
            ("p", tabel(["Deel", "Onderdeel", "Wat erin zit"], [
                ["expliciet (je kan het zeggen)", "episodisch geheugen",
                 "gebeurtenissen die jij zelf meemaakte"],
                ["expliciet", "semantisch geheugen", "feiten en betekenissen, los van wanneer je ze leerde"],
                ["impliciet (je kan het niet uitleggen)", "procedureel geheugen",
                 "vaardigheden zoals fietsen en veters knopen"],
            ])),
            ("kader", "Weten waar je was toen je een bericht kreeg, is <strong>episodisch</strong>. Weten "
                      "dat Brussel de hoofdstad van België is, zonder te weten wanneer je dat leerde, is "
                      "<strong>semantisch</strong>. Kunnen fietsen zonder erbij na te denken, is "
                      "<strong>procedureel</strong>."),
            ("p", "Bandura en Skinner geven op de tweede basisvraag <strong>niet</strong> een volledig "
                  "verschillend antwoord: beiden leggen de nadruk op <strong>nurture</strong>. Het verschil "
                  "zit elders: bij Bandura gebeurt er ook iets in het hoofd."),
        ]),
    ],
    onthoud=[
        "Klassiek: prikkels koppelen (Pavlov, Watson, S-R). Operant: leren van het gevolg (Skinner, S-R-C).",
        "Positief is toevoegen, negatief is wegnemen. Bekrachtiging doet gedrag toenemen, straf afnemen.",
        "Bandura: modelleren en imitatieleren, Bobo doll. Voorloper van de cognitieve benadering.",
        "Piaget: sensomotorisch, pre-operationeel, concreet-operationeel, formeel-operationeel.",
        "Geheugen: sensorisch, korte termijn, lange termijn (expliciet episodisch en semantisch, impliciet procedureel).",
    ],
)

# ───────────────────────── 4. Humanistische en systemische benadering
BUNDELS["ontwikkeling-de-humanistische-en-de-systemische-benadering-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Ontwikkeling: de humanistische en de systemische benadering",
    onder="De laatste twee van de zes benaderingen: de ene vertrekt bij wat een mens zelf wil worden, de andere bij alles wat rond iemand staat. Met Maslow, Rogers, Bronfenbrenner en Vygotsky.",
    secties=[
        dict(kop="De humanistische benadering", blokken=[
            ("p", "De <strong>humanistische benadering</strong> gaat ervan uit dat een mens "
                  "<strong>zelf richting geeft</strong> aan zijn leven en wil groeien. Twee theorieën horen "
                  "erbij: de <strong>motivatietheorie</strong> van <strong>Abraham Maslow</strong> en de "
                  "<strong>client centered therapy</strong> van <strong>Carl Rogers</strong>."),
            ("p", "Maslow zet de behoeften van een mens in een orde, vaak getekend als een piramide. "
                  "<strong>Onderaan</strong> staan de lichamelijke behoeften, <strong>bovenaan</strong> de "
                  "zelfontplooiing:"),
            ("p", tabel(["Laag", "Wat ze vraagt"], [
                ["zelfontplooiing", "worden wie je kan worden"],
                ["waardering en erkenning", "gezien en gewaardeerd worden"],
                ["contact en verbondenheid", "ergens bij horen"],
                ["veiligheid en zekerheid", "weten waar je morgen woont"],
                ["lichamelijke behoeften", "eten, drinken, slapen"],
            ])),
            ("kader", "De gedachte achter die orde: wie honger heeft of zich onveilig voelt, komt "
                      "<strong>niet aan de hogere behoeften toe</strong>. Daarom is deze theorie zo nuttig "
                      "op school. Een school die eerst voor een ontbijt en een vast klasritme zorgt en pas "
                      "daarna voor extra uitdaging, volgt de orde van Maslow."),
            ("p", "Het bezwaar dat vaak terugkomt: <strong>de vaste orde houdt niet bij iedereen "
                  "stand</strong>. Mensen zetten soms een hogere behoefte voorop terwijl een lagere niet "
                  "vervuld is."),
            ("weetje", "<strong>Zelfontplooiing</strong> of <strong>zelfactualisatie</strong> betekent "
                       "worden wie <em>jij</em> kan worden. Het is géén vergelijking met anderen."),
            ("p", "Bij <strong>Rogers</strong> staat de persoon zelf in het midden: dat is wat "
                  "<strong>client centered</strong> betekent. De begeleider schrijft geen plan voor maar "
                  "gaat mee. Drie houdingen horen daarbij: de ander "
                  "<strong>aanvaarden</strong> zoals hij is, <strong>echt</strong> en open zijn, en je "
                  "kunnen <strong>inleven</strong>. Beslissen voor de ander hoort er juist niet bij."),
            ("p", "Op de <strong>eerste basisvraag</strong> antwoordt de humanistische benadering eerder "
                  "<strong>continu</strong>: ze werkt niet met vaste stadia maar met een groei die "
                  "doorloopt. Op de <strong>tweede</strong> geeft ze veel plaats aan de "
                  "<strong>zelfbepaling</strong>. Dat is ook het grote verschil met het behaviorisme: daar "
                  "zit de sturing <em>buiten</em> de persoon, bij prikkels en gevolgen; hier zit ze "
                  "<em>bij</em> de persoon."),
        ]),
        dict(kop="Bronfenbrenner: vijf systemen", blokken=[
            ("p", "De <strong>systemische benadering</strong> kijkt naar <strong>alles wat rond iemand "
                  "staat</strong>: het gezin, de klas, de buurt, de samenleving. Die systemen beïnvloeden "
                  "ook elkaar."),
            ("p", "Het <strong>bio-ecologisch model</strong> van <strong>Urie Bronfenbrenner</strong> "
                  "onderscheidt <strong>vijf</strong> systemen:"),
            ("p", tabel(["Systeem", "Wat erin zit", "Voorbeeld"], [
                ["microsysteem", "waar het kind zelf dagelijks in zit", "het gezin, de klas"],
                ["mesosysteem", "de verbinding tussen twee microsystemen",
                 "de juf die met de ouders belt"],
                ["exosysteem", "wat het kind raakt zonder dat het erin zit",
                 "de nachtdienst van een ouder"],
                ["macrosysteem", "de cultuur, de wetten, de waarden van een land", "de leerplicht"],
                ["chronosysteem", "de tijd en wat erin verandert",
                 "opgroeien met een smartphone, anders dan je ouders"],
            ])),
            ("p", "De fiche noemt daarnaast <strong>directe</strong> en <strong>indirecte "
                  "interacties</strong> en de <strong>structurele kenmerken van de omgeving</strong>. In het "
                  "<strong>microsysteem</strong> zijn de interacties <strong>direct</strong>, want het kind "
                  "zit er zelf in. In het <strong>exosysteem</strong> zijn ze <strong>indirect</strong>."),
            ("kader", "De systemen werken <strong>door elkaar</strong>, niet één na één. Een wet uit het "
                      "macrosysteem verandert het werk van een ouder (exosysteem), en dat verandert het "
                      "gezin (microsysteem)."),
            ("weetje", "Dit model komt in deze vakfiche <strong>twee keer</strong> voor: hier als "
                       "systemische benadering van ontwikkeling, en later bij pedagogiek als pedagogisch "
                       "model. Dezelfde vijf systemen, dus dubbel de moeite om te kennen."),
        ]),
        dict(kop="Vygotsky: zones en scaffolding", blokken=[
            ("p", "De <strong>sociaal-culturele theorie</strong> van <strong>Lev Vygotsky</strong> legt de "
                  "nadruk op <strong>leren samen met anderen</strong> en op de rol van de cultuur. Hij "
                  "werkt met <strong>zones</strong>:"),
            ("p", tabel(["Zone", "Wat erin zit", "Wat het leren doet"], [
                ["comfortzone", "wat je al zelfstandig kan", "er valt niets bij te leren"],
                ["zone van de naaste ontwikkeling", "wat je nog niet alleen kan, maar wel met hulp",
                 "hier zit de leerwinst"],
                ["groeizone", "de ruimte waarin je met steun vooruitgaat", "hier gebeurt het leren"],
                ["angstzone", "wat veel te moeilijk is", "het leren valt stil"],
            ])),
            ("p", "Twee begrippen horen daarbij. <strong>Scaffolding</strong>, van het Engelse woord voor "
                  "steiger: je geeft hulp en bouwt die <strong>stap voor stap weer af</strong>. Eerst een "
                  "voorbeeld, dan een half voorbeeld, dan niets meer. Een steiger gaat weg als het gebouw "
                  "staat; de hulp zo lang mogelijk blijven geven is dus géén scaffolding."),
            ("p", "En het <strong>interiorisatieproces</strong>: wat eerst <strong>samen met anderen</strong> "
                  "gebeurt, wordt <strong>eigen denken</strong>. Een kind telt eerst luidop met de juf, en "
                  "later in zijn hoofd. Interioriseren betekent letterlijk naar binnen nemen."),
            ("kader", "Op de <strong>derde basisvraag</strong> antwoordt Vygotsky dat ontwikkeling eerder "
                      "<strong>cultureel bepaald</strong> is. Dat zit al in de naam van zijn theorie: "
                      "sociaal-<strong>cultureel</strong>. Wat een kind leert en hoe het leert, hangt af van "
                      "de cultuur rond hem."),
        ]),
    ],
    onthoud=[
        "Humanistisch: Maslow (behoeften in een orde) en Rogers (client centered therapy).",
        "Eerst de lagere behoeften, dan de hogere. Zelfontplooiing staat bovenaan.",
        "Bronfenbrenner: micro, meso, exo, macro, chrono. Micro is direct, exo indirect.",
        "Vygotsky: comfortzone, zone van de naaste ontwikkeling, groeizone, angstzone.",
        "Scaffolding is hulp die je afbouwt. Interiorisatie is samen doen dat eigen denken wordt.",
    ],
)

# ───────────────────────── 5. Prosociaal, antisociaal en sociale cognitie
BUNDELS["prosociaal-gedrag-antisociaal-gedrag-en-sociale-cognitie-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Prosociaal gedrag, antisociaal gedrag en sociale cognitie",
    onder="Het eerste van drie thema's over sociale psychologie: twee lijstjes gedrag, en hoe wij verklaringen verzinnen voor wat mensen doen. Met Heider, Weiner en Dweck.",
    secties=[
        dict(kop="Prosociaal en antisociaal gedrag", blokken=[
            ("p", "De <strong>sociale psychologie</strong> onderzoekt hoe mensen door anderen "
                  "<strong>beïnvloed</strong> worden: de druk van een groep, de invloed van een gezagsfiguur, "
                  "en wat anderen denken."),
            ("p", "Ze begint bij twee lijstjes van elk <strong>zes</strong> vormen van gedrag. "
                  "<strong>Pro</strong> betekent voor, <strong>anti</strong> betekent tegen:"),
            ("p", tabel(["Prosociaal gedrag", "Antisociaal gedrag"], [
                ["delen", "agressie"],
                ["helpen en ondersteunen", "liegen en bedriegen"],
                ["positief groepsgedrag", "ongepast groepsgedrag"],
                ["samenwerken", "pesten"],
                ["troosten", "regels overtreden"],
                ["verantwoordelijkheid opnemen", "vandalisme"],
            ])),
            ("kader", "De fiche kijkt naar het <strong>gedrag zelf</strong>, niet naar de reden erachter. "
                      "Iets voor iemand doen in de hoop er zelf iets aan over te houden, blijft dus "
                      "prosociaal gedrag."),
            ("p", "Let op de twee die over een groep gaan: de fiche noemt zowel "
                  "<strong>positief</strong> als <strong>ongepast</strong> groepsgedrag. "
                  "<strong>Samen iets doen zegt dus niets over goed of slecht.</strong>"),
            ("p", "Twee verwarringen om te vermijden. <strong>Agressie</strong> is gericht op een "
                  "<strong>persoon</strong>, <strong>vandalisme</strong> op <strong>spullen</strong>. En "
                  "<strong>delen</strong> gaat over spullen, <strong>helpen</strong> over iemand bijstaan, "
                  "<strong>troosten</strong> over iemand met verdriet, <strong>samenwerken</strong> over "
                  "samen aan één doel werken."),
            ("weetje", "Waarom spreekt de fiche van prosociaal en antisociaal en niet van goed en slecht? "
                       "Omdat die twee woorden naar het <strong>effect op anderen</strong> kijken, zonder "
                       "een moreel oordeel over de persoon."),
        ]),
        dict(kop="Sociale cognitie en de attitude", blokken=[
            ("p", "<strong>Sociale cognitie</strong> is de manier waarop wij <strong>over mensen "
                  "nadenken</strong>: hoe wij informatie over anderen en over onszelf verwerken. De fiche "
                  "noemt <strong>drie</strong> mentale processen die erbij horen: de "
                  "<strong>attitude</strong>, de <strong>attributie</strong> en de "
                  "<strong>cognitieve dissonantie</strong>. De dissonantie krijgt in dit vak een eigen "
                  "bundel, bij de groepsprocessen."),
            ("p", "Een <strong>attitude</strong> is een <strong>houding</strong> tegenover iets of iemand: "
                  "hoe je erover denkt, wat je erbij voelt, en hoe geneigd je bent ernaar te handelen."),
            ("p", "Het verband met gedrag is <strong>niet absoluut</strong>. Een attitude maakt bepaald "
                  "gedrag <strong>waarschijnlijker</strong>, maar beslist niet: wie milieubewust denkt, "
                  "neemt niet altijd de trein. En een attitude kan <strong>veranderen</strong>, onder andere "
                  "om een cognitieve dissonantie weg te werken."),
        ]),
        dict(kop="Heider: intern, extern en de attributiefout", blokken=[
            ("p", "Een <strong>causale attributie</strong> is de <strong>oorzaak die je aan gedrag "
                  "toeschrijft</strong>. Attribueren betekent toeschrijven. Let op: het is de verklaring die "
                  "<em>jij</em> maakt, en dus niet noodzakelijk de echte oorzaak."),
            ("p", "<strong>Fritz Heider</strong> onderscheidt er twee:"),
            ("p", tabel(["Attributie", "Ander woord", "De oorzaak ligt bij", "Voorbeeld"], [
                ["intern", "dispositioneel", "de persoon zelf: karakter, inzet, kunnen",
                 "wat een onbeschofte chauffeur"],
                ["extern", "situationeel", "de omstandigheden", "er was file"],
            ])),
            ("p", "De <strong>fundamentele attributiefout</strong> is de neiging om bij "
                  "<strong>anderen</strong> de persoon de schuld te geven en bij <strong>jezelf</strong> de "
                  "situatie. Je bent zelf te laat en zegt: er was file. Een klasgenoot is te laat en je "
                  "denkt: die is ongeorganiseerd."),
            ("kader", "Bij Heider staan er <strong>twee</strong> soorten attributie, niet drie. "
                      "<strong>Stabiliteit</strong> is een begrip van Weiner."),
        ]),
        dict(kop="Weiner: drie dimensies", blokken=[
            ("p", "<strong>Bernard Weiner</strong> beschrijft een attributie met <strong>drie "
                  "dimensies</strong> in zijn attributietheorie van motivatie en emoties:"),
            ("p", tabel(["Dimensie", "De vraag erachter", "Voorbeeld"], [
                ["locus van controle", "ligt de oorzaak binnen of buiten de persoon?",
                 "mijn inzet, of het geluk"],
                ["stabiliteit", "blijft de oorzaak, of kan ze morgen anders zijn?",
                 "ik ben niet goed in wiskunde, dat verandert toch nooit"],
                ["controleerbaarheid", "kan iemand er zelf iets aan doen?",
                 "niet geleerd hebben wel, een griep niet"],
            ])),
            ("weetje", "<strong>Locus</strong> is het Latijnse woord voor plaats. Daarom heet de eerste "
                       "dimensie de locus van controle: waar de oorzaak zit."),
        ]),
        dict(kop="Dweck: fixed en growth mindset", blokken=[
            ("p", "<strong>Carol Dweck</strong> werkt met de theorie van de <strong>impliciete "
                  "overtuigingen</strong>, en met twee begrippen die je overal terugziet:"),
            ("p", tabel(["Mindset", "Wat iemand gelooft", "Wat een fout betekent"], [
                ["fixed mindset", "mijn kunnen ligt vast en groeit niet",
                 "bewijs dat ik het niet kan"],
                ["growth mindset", "mijn kunnen groeit door te oefenen",
                 "iets dat ik nog niet kan, dus anders aanpakken"],
            ])),
            ("p", "De twee woordjes die je hoort: <em>nog niet</em> en <em>het anders aanpakken</em> wijzen "
                  "op een growth mindset."),
            ("kader", "Een <strong>fixed mindset</strong> past bij een attributie die "
                      "<strong>stabiel</strong> en <strong>oncontroleerbaar</strong> is. Dat is de brug "
                      "tussen Dweck en Weiner: wie denkt dat zijn kunnen vastligt, ziet de oorzaak als "
                      "blijvend en als iets waar hij zelf niets aan kan doen."),
            ("p", "Volgens Dweck heeft iemand <strong>niet in alle vakken dezelfde mindset</strong>: over "
                  "taal kan iemand een growth mindset hebben en over wiskunde een fixed mindset."),
        ]),
    ],
    onthoud=[
        "Zes vormen prosociaal gedrag en zes antisociaal; de fiche kijkt naar het gedrag, niet naar de reden.",
        "Sociale cognitie bestaat uit attitude, attributie en cognitieve dissonantie.",
        "Heider: interne of dispositionele en externe of situationele attributie, plus de fundamentele attributiefout.",
        "Weiner: locus van controle, stabiliteit en controleerbaarheid.",
        "Dweck: fixed mindset (kunnen ligt vast) en growth mindset (kunnen groeit).",
    ],
)

# ───────────────────────── 6. Cognitieve dissonantie en groepsprocessen
BUNDELS["cognitieve-dissonantie-en-processen-in-een-groep-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Cognitieve dissonantie en processen in een groep",
    onder="De spanning tussen wat je denkt en wat je doet, en wat een groep met een mens doet. Met Festinger en Tuckman.",
    secties=[
        dict(kop="Consonantie en dissonantie", blokken=[
            ("p", "<strong>Leon Festinger</strong> zette twee woorden naast elkaar die uit de muziek komen:"),
            ("p", tabel(["Begrip", "Wat het is"], [
                ["cognitieve consonantie", "samenklank: je denken en je doen passen bij elkaar, er is rust"],
                ["cognitieve dissonantie", "wanklank: je denkt het ene en doet het andere, en dat wringt"],
            ])),
            ("p", "Die spanning willen mensen <strong>graag kwijt</strong>, en dáár komt het verband met "
                  "gedrag: de dissonantie <strong>drijft iemand tot een aanpassing</strong>. De fiche noemt "
                  "<strong>drie</strong> manieren om haar te verminderen:"),
            ("p", tabel(["Manier", "Bij een roker die weet dat roken schadelijk is"], [
                ["je gedrag veranderen", "hij stopt met roken"],
                ["je attitude veranderen", "hij besluit dat het gevaar sterk overdreven wordt"],
                ["een cognitie toevoegen", "hij zegt: mijn opa rookte en werd negentig"],
            ])),
            ("kader", "<strong>Gedrag veranderen is vaak het moeilijkst.</strong> Daarom veranderen mensen "
                      "vaker hun houding, of voegen ze een gedachte toe die de spanning verzacht."),
        ]),
        dict(kop="Dissonantie in het dagelijks leven", blokken=[
            ("p", "De fiche noemt <strong>drie</strong> situaties waarin dissonantiereductie elke dag "
                  "gebeurt:"),
            ("p", tabel(["Situatie", "Wat er gebeurt", "Voorbeeld"], [
                ["na het maken van een keuze", "de gekozen kant wordt mooier, de afgewezen kant slechter",
                 "wie voor een richting koos, vertelt wat er mis is met de andere"],
                ["na het instemmen met een verzoek", "wie ja zei, vindt het verzoek achteraf redelijker",
                 "daarom werken beïnvloedingstechnieken"],
                ["na het leveren van inspanningen", "wie veel moeite deed, vindt het waardevoller",
                 "anders was al die inspanning voor niets"],
            ])),
            ("p", "Deze theorie legt ook uit hoe reclame werkt: na een duurdere aankoop zoekt een klant "
                  "<strong>zelf</strong> argumenten dat het de goede keuze was."),
            ("weetje", "Verwar een <strong>attitude</strong> niet met een <strong>dissonantie</strong>: de "
                       "eerste is een houding, de tweede is de spanning als twee dingen niet samengaan."),
        ]),
        dict(kop="Tuckman: vijf fasen in een groep", blokken=[
            ("p", "<strong>Bruce Tuckman</strong> beschrijft hoe een groep zich vormt, in "
                  "<strong>vijf</strong> fasen. De fiche geeft bij elke fase de Nederlandse en de Engelse "
                  "naam:"),
            ("p", tabel(["Fase", "Engels", "Wat er gebeurt"], [
                ["oriëntatiefase", "forming", "de leden kennen elkaar nog niet en zoeken hun plaats"],
                ["machtsfase", "storming", "er wordt uitgevochten wie welke plaats krijgt"],
                ["normeringsfase", "norming", "de groep maakt haar eigen afspraken"],
                ["prestatiefase", "performing", "de groep werkt vlot en haalt haar doelen"],
                ["afscheidsfase", "adjourning", "de groep valt uiteen en neemt afscheid"],
            ])),
            ("kader", "De <strong>machtsfase is geen probleem dat een goede groep overslaat</strong>. Ze "
                      "hoort bij de ontwikkeling: zonder botsen komen de afspraken van de normeringsfase "
                      "er niet. Eerst botsen, dan afspreken, dan presteren."),
        ]),
        dict(kop="Wat een groep met een mens doet", blokken=[
            ("p", "De fiche noemt vijf groepsprocessen. Het eerste is het "
                  "<strong>groepslidmaatschap</strong>, met de <strong>ingroup</strong> en de "
                  "<strong>outgroup</strong>: de ingroup is <em>wij</em>, de outgroup is <em>zij</em>. "
                  "Mensen beoordelen hun eigen groep bijna altijd gunstiger."),
            ("p", "Dan drie processen die over <strong>presteren</strong> gaan:"),
            ("p", tabel(["Proces", "Wat er gebeurt", "Wanneer"], [
                ["sociale facilitatie", "je presteert beter omdat anderen meekijken",
                 "bij een eenvoudige of goed ingeoefende taak"],
                ["sociale belemmering", "je presteert slechter omdat anderen meekijken",
                 "bij een moeilijke of nieuwe taak"],
                ["social loafing", "je levert minder inzet omdat je in een groep werkt",
                 "als je eigen bijdrage niet opvalt"],
            ])),
            ("p", "Een gevorderde pianist speelt dus <strong>beter</strong> voor publiek en een beginner net "
                  "<strong>slechter</strong>: hetzelfde publiek, een ander effect, want het hangt af van hoe "
                  "goed de taak al zit."),
            ("kader", "<strong>Social loafing</strong> heet in het Nederlands <strong>sociaal "
                      "parasiteren</strong>. Verwar het niet met sociale belemmering: bij loafing doe je "
                      "<em>minder</em> omdat je aandeel niet opvalt, bij belemmering presteer je "
                      "<em>slechter</em> door de druk van publiek."),
            ("p", "Het vijfde proces is <strong>groepsdenken</strong>: een groep neemt een slechte "
                  "beslissing <strong>om eensgezind te blijven</strong>. Iemand denkt dat het plan niet gaat "
                  "lukken, maar zwijgt omdat iedereen enthousiast is. Een goede tegenzet is iemand "
                  "<strong>uitdrukkelijk de rol geven om tegen te spreken</strong>: dan hoeft niemand zijn "
                  "twijfel nog in te slikken."),
        ]),
    ],
    onthoud=[
        "Consonantie is rust, dissonantie is spanning tussen denken en doen (Festinger).",
        "Dissonantie verminderen: gedrag veranderen, attitude veranderen, of een cognitie toevoegen.",
        "Ze speelt na een keuze, na een ja op een verzoek, en na veel inspanning.",
        "Tuckman: forming, storming, norming, performing, adjourning.",
        "Facilitatie is beter door publiek, belemmering slechter, loafing is minder inzet in een groep.",
        "Groepsdenken: eensgezindheid weegt zwaarder dan de kwaliteit van de beslissing.",
    ],
)

# ───────────────────────── 7. Sociale beïnvloeding
BUNDELS["sociale-beinvloeding-conformisme-inwilliging-en-gehoorzaamheid-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Sociale beïnvloeding: conformisme, inwilliging en gehoorzaamheid",
    onder="Drie niveaus van sociale druk, drie manieren om weerstand te bieden, vier technieken om iemand te doen toegeven, en vijf onderzoeken die de fiche bij naam noemt.",
    secties=[
        dict(kop="Een continuüm van sociale druk", blokken=[
            ("p", "<strong>Sociale beïnvloeding</strong> is wat anderen met je gedrag doen. De fiche zet "
                  "haar neer als een <strong>continuüm</strong>: een lijn van zachte naar harde druk. "
                  "Toegeven kan op <strong>drie</strong> niveaus:"),
            ("p", tabel(["Niveau", "De druk komt van", "Is er een vraag?"], [
                ["conformisme", "een groep", "nee, niemand vraagt iets"],
                ["inwilliging", "iemand die iets vraagt", "ja, een verzoek"],
                ["gehoorzaamheid", "een gezagsfiguur", "ja, een bevel"],
            ])),
            ("kader", "Dit is <strong>de</strong> valkuil van dit thema. Je past je aan een groep aan "
                      "<em>zonder</em> dat iemand iets vroeg: conformisme. Iemand <em>vraagt</em> je iets en "
                      "je zegt ja: inwilliging. Iemand <em>met gezag</em> zegt het je: gehoorzaamheid."),
            ("p", "Tegenover toegeven staat <strong>weerstand bieden</strong>, ook in drie vormen:"),
            ("p", tabel(["Vorm", "Wat iemand doet"], [
                ["onafhankelijkheid", "zijn eigen weg gaan, zonder zich tegen de groep te keren"],
                ["assertiviteit", "zijn eigen mening of grens duidelijk uitspreken"],
                ["trotseren", "zich openlijk tegen de druk of het gezag verzetten"],
            ])),
        ]),
        dict(kop="Waarom mensen zich conformeren", blokken=[
            ("p", "De fiche onderscheidt twee redenen, en ze zien er van buiten hetzelfde uit:"),
            ("p", tabel(["Soort conformisme", "De reden", "Wat je denkt"], [
                ["informatief", "je gelooft dat de anderen het beter weten", "zij zullen wel juist zijn"],
                ["normatief", "je wil erbij horen en niet opvallen", "ik wil er niet uitliggen"],
            ])),
            ("p", "Bij <strong>informatief</strong> conformisme verandert je <strong>overtuiging</strong> "
                  "echt; bij <strong>normatief</strong> conformisme vaak alleen je "
                  "<strong>gedrag</strong>. Je zegt in de groep hetzelfde als iedereen en denkt alleen thuis "
                  "nog het tegendeel."),
        ]),
        dict(kop="Drie theorieën over conformisme", blokken=[
            ("p", "<strong>Muzafer Sherif</strong> liet mensen in een donkere kamer schatten hoeveel een "
                  "lichtpuntje bewoog. Het puntje bewoog <strong>niet</strong>, maar het leek zo. Eerst gaf "
                  "iedereen een eigen schatting; na een paar rondes in groep <strong>schoven de "
                  "schattingen naar elkaar toe</strong> tot er één groepsnorm was. En die norm hielden ze "
                  "ook achteraf, alleen, nog aan."),
            ("kader", "De situatie bij Sherif was <strong>onduidelijk</strong>: niemand kon het weten. "
                      "Daarom is dit het voorbeeld van <strong>informatief</strong> conformisme."),
            ("p", "<strong>Solomon Asch</strong> deed het omgekeerde. Hij liet mensen zeggen welke van drie "
                  "lijnen even lang was als een voorbeeldlijn. Dat was "
                  "<strong>makkelijk</strong>, maar de andere deelnemers waren helpers van de "
                  "onderzoeker en gaven samen een duidelijk <strong>fout</strong> antwoord. Een groot deel "
                  "van de echte deelnemers ging minstens één keer mee in dat foute antwoord."),
            ("kader", "De situatie bij Asch was <strong>duidelijk</strong>: iedereen zag wat juist was. "
                      "Daarom is dit het voorbeeld van <strong>normatief</strong> conformisme. "
                      "<strong>Sherif en Asch door elkaar halen is de klassieke fout.</strong>"),
            ("p", "<strong>John Darley</strong> en <strong>Bibb Latané</strong> beschreven het "
                  "<strong>omstandereffect</strong>: hoe <strong>meer</strong> omstaanders er bij een "
                  "noodgeval zijn, hoe <strong>kleiner</strong> de kans dat iemand helpt. De verantwoorde"
                  "lijkheid wordt over de aanwezigen <strong>gespreid</strong>, en iedereen denkt dat een "
                  "ander het wel doet."),
            ("p", "Daarom werkt het om bij een ongeval <strong>één iemand aan te wijzen</strong>: "
                  "<em>jij in de blauwe jas, bel 112</em>. Dan kan die ene persoon de verantwoordelijkheid "
                  "niet meer doorschuiven."),
        ]),
        dict(kop="Vier beïnvloedingstechnieken", blokken=[
            ("p", "Technieken om iemand tot <strong>inwilliging</strong> te brengen. De namen staan in de "
                  "fiche, en ze zijn te raden als je weet wat ze beschrijven:"),
            ("p", tabel(["Techniek", "Hoe ze werkt", "Voorbeeld"], [
                ["voet-tussen-de-deur", "eerst een heel klein verzoek, daarna het grote",
                 "eerst een enquête van één vraag, dan een gift"],
                ["deur-in-het-gezicht", "eerst een overdreven groot verzoek, dan het echte",
                 "eerst elke week helpen, dan één zaterdag"],
                ["zodra-de-bal-aan-het-rollen-is", "eerst een voordelige prijs, daarna komen de kosten erbij",
                 "de goedkope reis waar achteraf nog toeslagen op komen"],
                ["dat-is-nog-niet-alles", "er onverwacht iets bij geven voor de ander kan antwoorden",
                 "en u krijgt er dit nog gratis bij"],
            ])),
            ("weetje", "Voet-tussen-de-deur werkt via de <strong>cognitieve dissonantie</strong>: wie één "
                       "keer ja zei, ziet zichzelf als iemand die helpt, en nee zeggen past daar niet meer "
                       "bij. Deur-in-het-gezicht werkt anders: het tweede verzoek lijkt "
                       "<strong>klein</strong> naast het eerste."),
        ]),
        dict(kop="Twee onderzoeken over gehoorzaamheid", blokken=[
            ("p", "<strong>Stanley Milgram</strong> vroeg deelnemers om iemand in een andere kamer "
                  "stroomstoten te geven bij een fout antwoord, bij elke fout een stapje sterker. Er werd "
                  "<strong>niemand echt geschokt</strong>: de leerling was een helper van de onderzoeker. "
                  "Een <strong>groot deel</strong> van de deelnemers ging door tot het hoogste niveau, ook "
                  "al hoorden ze protest, zolang de onderzoeker in zijn witte jas zei dat ze moesten "
                  "doorgaan."),
            ("p", "Milgram onderzocht dus <strong>gehoorzaamheid aan een gezagsfiguur</strong>, en niet de "
                  "druk van een groep."),
            ("p", "<strong>Philip Zimbardo</strong> deed het <strong>Stanford gevangenisexperiment</strong>. "
                  "Studenten werden door het lot verdeeld in <strong>bewakers</strong> en "
                  "<strong>gevangenen</strong> in een nagemaakte gevangenis. De bewakers gingen zich zo hard "
                  "gedragen dat het onderzoek <strong>vroeger werd stopgezet</strong> dan gepland."),
            ("kader", "Bij Zimbardo gaat het niet over een bevel, maar over de "
                      "<strong>rol</strong> die iemand krijgt: wie een uniform en macht krijgt, gedraagt "
                      "zich daarnaar. Dat sluit aan bij de <strong>rollen</strong> uit het thema over "
                      "socialisatie."),
            ("p", "Beide onderzoeken zijn ook <strong>ethisch</strong> zwaar bekritiseerd: de deelnemers "
                  "wisten niet waar ze aan begonnen en kwamen er niet onbeschadigd uit. Daarom mag een "
                  "onderzoek vandaag niet meer zo gebeuren."),
        ]),
    ],
    onthoud=[
        "Conformisme is groepsdruk, inwilliging is ja op een verzoek, gehoorzaamheid is doen wat gezag beveelt.",
        "Weerstand: onafhankelijkheid, assertiviteit, trotseren.",
        "Sherif: onduidelijke situatie, informatief conformisme. Asch: duidelijke situatie, normatief conformisme.",
        "Darley en Latané: hoe meer omstaanders, hoe kleiner de kans dat iemand helpt.",
        "Technieken: voet-tussen-de-deur, deur-in-het-gezicht, zodra-de-bal-aan-het-rollen-is, dat-is-nog-niet-alles.",
        "Milgram: gehoorzaamheid aan gezag. Zimbardo: de kracht van een rol.",
    ],
)

# ───────────────────────── 8. Persoonlijkheid: wat ze is en het brein
BUNDELS["persoonlijkheid-wat-ze-is-en-hoe-een-brein-reageert-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Persoonlijkheid: wat ze is en hoe een brein reageert",
    onder="Vijf elementen van persoonlijkheid, de invloed van cultuur, en de biologische benadering met Gray en Eysenck.",
    secties=[
        dict(kop="Wat persoonlijkheid is", blokken=[
            ("p", "De <strong>persoonlijkheidspsychologie</strong> is het derde onderdeel van "
                  "gedragswetenschappen, naast de ontwikkelings- en de sociale psychologie. Ze vraagt niet "
                  "hoe mensen op elkaar lijken, maar <strong>waarin ze van elkaar verschillen</strong>, en "
                  "waarom iemand <strong>doorheen situaties en doorheen de jaren</strong> herkenbaar "
                  "dezelfde blijft."),
            ("p", "De fiche noemt <strong>vijf elementen</strong> van persoonlijkheid:"),
            ("p", tabel(["Element", "Wat het is"], [
                ["karakter", "het geheel van eigenschappen waarmee iemand denkt, voelt en handelt"],
                ["motivatie", "wat iemand in beweging zet en waar hij naartoe wil"],
                ["temperament", "de aangeboren kant: hoe snel en hoe sterk iemand reageert"],
                ["trekken of disposities", "de geneigdheden die over situaties heen terugkomen"],
                ["zelfbeeld", "het beeld dat iemand van zichzelf heeft"],
            ])),
            ("kader", "<strong>Temperament</strong> is de kant die er al vroeg is en die weinig verandert; "
                      "<strong>karakter</strong> is wat daar met de jaren en met opvoeding bij groeit. "
                      "<strong>Trekken</strong> zijn geen gedrag, maar de <strong>neiging</strong> tot "
                      "gedrag: iemand met de trek vriendelijkheid is niet élk moment vriendelijk."),
            ("weetje", "<strong>Dispositie</strong> betekent letterlijk geneigdheid. Dat woord kwam al "
                       "voorbij bij Heider: een <strong>dispositionele attributie</strong> is er een die de "
                       "oorzaak bij de persoon legt."),
        ]),
        dict(kop="Cultuur vormt mee", blokken=[
            ("p", "De fiche vraagt uitdrukkelijk naar de invloed van <strong>culturele factoren</strong> op "
                  "de vorming van persoonlijkheid. Cultuur bepaalt mee welke eigenschappen gewaardeerd "
                  "worden, en dus welke een kind leert tonen."),
            ("p", "<strong>Cross-cultureel onderzoek</strong> vergelijkt daarom dezelfde vragenlijst in "
                  "verschillende landen. De grote lijn: de <strong>trekken zelf</strong> worden in heel veel "
                  "culturen teruggevonden, maar <strong>hoe hoog</strong> men gemiddeld scoort en "
                  "<strong>welke</strong> trek als een deugd geldt, verschilt."),
            ("p", "De klassieke tegenstelling is die tussen een "
                  "<strong>individualistische</strong> en een <strong>collectivistische</strong> cultuur. In "
                  "de eerste staat het eigen doel en de eigen prestatie vooraan; in de tweede de groep, de "
                  "familie en de harmonie. Dezelfde assertiviteit kan daardoor op de ene plaats een sterkte "
                  "zijn en op de andere onhoffelijk."),
            ("kader", "Cultuur <strong>vervangt</strong> de biologie niet. Persoonlijkheid komt uit "
                      "<strong>beide</strong>: wat iemand meekrijgt én waarin hij opgroeit. Dat is "
                      "opnieuw de nature-nurture-vraag uit de ontwikkelingspsychologie."),
        ]),
        dict(kop="Gray: twee systemen in het brein", blokken=[
            ("p", "De <strong>biologische benadering</strong> zoekt de persoonlijkheid in het lichaam zelf: "
                  "in het zenuwstelsel, de hersenen en de erfelijkheid."),
            ("p", "<strong>Jeffrey Gray</strong> bouwde de <strong>reinforcement sensitivity theory</strong>, "
                  "de theorie van de gevoeligheid voor bekrachtiging. Hij beschrijft "
                  "<strong>twee</strong> systemen in het brein:"),
            ("p", tabel(["Systeem", "Afkorting", "Waarop het reageert", "Wat het doet"], [
                ["Behavioral Inhibition System", "BIS", "straf, gevaar, iets nieuws",
                 "remt het gedrag af: stop, pas op"],
                ["Behavioral Activation System", "BAS", "beloning, iets dat lokt",
                 "zet het gedrag aan: ga erop af"],
            ])),
            ("p", "<strong>Inhibition</strong> betekent remming, <strong>activation</strong> betekent "
                  "aanzetten. Bij wie een sterk <strong>BIS</strong> heeft, slaat de rem snel aan: die is "
                  "voorzichtig, let op wat fout kan gaan en is gevoelig voor straf. Bij wie een sterk "
                  "<strong>BAS</strong> heeft, geeft het gas: die gaat op een beloning af en neemt makkelijker "
                  "een risico."),
            ("kader", "De twee systemen zijn <strong>geen tegenpolen op één lijn</strong>. Iemand kan beide "
                      "sterk hebben, en dan er tegelijk naartoe willen en voor terugdeinzen."),
        ]),
        dict(kop="Eysenck: arousal", blokken=[
            ("p", "<strong>Hans Eysenck</strong> bouwde de <strong>biologische theorie van "
                  "persoonlijkheid</strong> rond <strong>arousal</strong>: het "
                  "<strong>prikkelingsniveau</strong> van de hersenen, hoe wakker en geprikkeld het brein in "
                  "rust al staat."),
            ("p", "Zijn gedachte is dat iedereen een aangenaam middenniveau zoekt:"),
            ("p", tabel(["", "Arousal in rust", "Gevolg", "Wat iemand opzoekt"], [
                ["introvert", "al hoog", "prikkels komen snel te veel aan",
                 "rust, een kleine groep, een stille kamer"],
                ["extravert", "laag", "prikkels komen er moeilijk door",
                 "drukte, gezelschap, iets spannends"],
            ])),
            ("kader", "<strong>Dit is de omgekeerde uitleg van wat je zou verwachten.</strong> Een "
                      "extravert zoekt drukte op <em>omdat</em> zijn brein in rust te weinig geprikkeld is, "
                      "en een introvert zoekt rust <em>omdat</em> zijn brein al hoog staat. Niet omdat "
                      "de een graag en de ander ongraag onder mensen komt."),
            ("p", "Dat verklaart ook waarom dezelfde drukke zaal voor de ene fijn en voor de andere slopend "
                  "is: de zaal is even luid, het brein staat anders."),
            ("weetje", "Eysenck komt in dit vak <strong>twee keer</strong> voor: hier met de arousal, en bij "
                       "de trekken met zijn <strong>PEN-model</strong>. Dezelfde onderzoeker, twee "
                       "verschillende stukken leerstof."),
        ]),
    ],
    onthoud=[
        "Vijf elementen: karakter, motivatie, temperament, trekken of disposities, zelfbeeld.",
        "Temperament is aangeboren, karakter groeit; een trek is een neiging, geen gedrag.",
        "Cross-cultureel: de trekken komen overal terug, de gemiddelde scores en de waardering verschillen.",
        "Gray: BIS remt bij straf en gevaar, BAS zet aan bij beloning.",
        "Eysenck: introvert heeft een hoge arousal in rust en zoekt rust; extravert een lage en zoekt prikkels.",
    ],
)

# ───────────────────────── 9. Freud, Bandura, Rogers
BUNDELS["persoonlijkheid-van-freud-over-bandura-naar-rogers-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Persoonlijkheid: van Freud over Bandura naar Rogers",
    onder="Drie benaderingen die dezelfde vraag anders beantwoorden: wat houdt een persoonlijkheid in beweging? Met Freud, Bandura, Rotter, Maslow en Rogers.",
    secties=[
        dict(kop="Freud: drie bewustzijnsniveaus", blokken=[
            ("p", "De <strong>psychodynamische benadering</strong> ziet een persoonlijkheid als een spel van "
                  "<strong>krachten</strong> die tegen elkaar induwen. Het bekendste voorbeeld is de "
                  "<strong>psychoanalyse van Sigmund Freud</strong>."),
            ("p", "Freud verdeelt het psychische leven in <strong>drie niveaus</strong>:"),
            ("p", tabel(["Niveau", "Wat er zit", "Kan je eraan?"], [
                ["het bewuste", "waar je nu aan denkt", "ja, meteen"],
                ["het onder- of voorbewuste", "wat je niet nú denkt maar wel kan ophalen",
                 "ja, als je het zoekt"],
                ["het onbewuste", "wat weggedrukt is en toch meespeelt", "nee, niet rechtstreeks"],
            ])),
            ("p", "<strong>Verdringing</strong> is het mechanisme waarmee iets in het "
                  "<strong>onbewuste</strong> terechtkomt: een herinnering of een verlangen dat te "
                  "pijnlijk is, wordt weggeduwd. Volgens Freud is het daarmee niet weg; het werkt verder, en "
                  "het komt naar buiten in dromen, verspreken en symptomen."),
            ("kader", "Let op het woord <strong>voorbewust</strong>. Dat is níet hetzelfde als onbewust: "
                      "voorbewust kan je ophalen, onbewust niet. Je eigen adres is voorbewust."),
        ]),
        dict(kop="Freud: de drie instanties", blokken=[
            ("p", "Daarnaast beschrijft Freud een <strong>persoonlijkheidsstructuur</strong> van drie delen, "
                  "elk met zijn eigen principe:"),
            ("p", tabel(["Deel", "Andere naam", "Principe", "Wat het wil"], [
                ["het Es", "het Id", "lustprincipe", "nu, en volledig"],
                ["het Ich", "het Ego", "realiteitsprincipe", "wat haalbaar is in de echte wereld"],
                ["het Über-ich", "het Superego", "moraliteitsprincipe", "wat hoort"],
            ])),
            ("p", "In het <strong>Es</strong> zitten de twee driften: de <strong>eros</strong> of "
                  "levensdrift, en de <strong>thanatos</strong> of doodsdrift. Het "
                  "<strong>Ich</strong> staat ertussen: het moet de drift van het Es en de eis van het "
                  "Über-ich met de werkelijkheid verzoenen. Het Ich is dus de "
                  "<strong>onderhandelaar</strong>, niet de strengste van de drie."),
            ("kader", "Het <strong>Über-ich</strong> is het strenge deel, niet het Ich. Een stem die zegt "
                      "<em>dat hoort niet</em>, is het Über-ich; een stem die zegt <em>dit kan nu niet, "
                      "straks wel</em>, is het Ich."),
        ]),
        dict(kop="Bandura en Rotter: de cognitieve benadering", blokken=[
            ("p", "De <strong>cognitieve benadering</strong> legt het gewicht bij het "
                  "<strong>denken</strong>: wat iemand gelooft over zichzelf en over de wereld."),
            ("p", "<strong>Albert Bandura</strong> bouwde de <strong>sociaal-cognitieve "
                  "leertheorie</strong> rond het <strong>wederzijds determinisme</strong>: drie factoren "
                  "beïnvloeden elkaar <strong>in alle richtingen</strong>."),
            ("p", tabel(["De drie factoren", "Voorbeeld"], [
                ["cognities en eigenschappen", "ik denk dat ik slecht ben in wiskunde"],
                ["de omgeving", "een klas waar snel antwoorden geroepen worden"],
                ["het gedrag", "ik steek mijn hand niet meer op"],
            ])),
            ("p", "Het woord <strong>wederzijds</strong> is hier de kern: het gaat niet in één richting. "
                  "Je gedrag verandert ook je omgeving, en je omgeving verandert wat je over jezelf denkt."),
            ("p", "<strong>Zelfeffectiviteit</strong> is het geloof dat je een bepaalde taak "
                  "<strong>kan</strong>. Het is <strong>taakgebonden</strong>: iemand kan een hoge "
                  "zelfeffectiviteit hebben voor zwemmen en een lage voor spreken voor een groep. En het is "
                  "iets anders dan zelfbeeld of zelfwaarde, die over de persoon in zijn geheel gaan."),
            ("p", "<strong>Julian Rotter</strong> bouwde de <strong>locus of control theory</strong>: waar "
                  "iemand de controle over zijn leven ziet liggen."),
            ("p", tabel(["Locus of control", "Wat iemand gelooft"], [
                ["intern", "wat mij overkomt, hangt grotendeels van mij af"],
                ["extern", "wat mij overkomt, hangt van geluk, anderen of het lot af"],
            ])),
            ("kader", "Bij <strong>Weiner</strong> (sociale psychologie) is de locus van controle een "
                      "<strong>dimensie van één attributie</strong>, voor dat ene geval. Bij "
                      "<strong>Rotter</strong> is ze een <strong>vaste eigenschap van een persoon</strong>, "
                      "die je overal terugziet. Zelfde woord, twee theorieën."),
        ]),
        dict(kop="Maslow en Rogers: de humanistische benadering", blokken=[
            ("p", "De <strong>humanistische benadering</strong> vertrekt van een mens die "
                  "<strong>zelf</strong> wil groeien. Beide auteurs noemen dat "
                  "<strong>zelfactualisatie</strong>: worden wie je ten volle kan zijn."),
            ("p", "<strong>Abraham Maslow</strong> maakte een <strong>motivatietheorie</strong> met zijn "
                  "<strong>behoeftepiramide</strong>. Onderaan de lichamelijke behoeften, dan veiligheid, "
                  "dan ergens bij horen, dan waardering, en bovenaan de "
                  "<strong>zelfactualisatie</strong>. Zijn gedachte: wat laag staat, vraagt eerst "
                  "aandacht. Een kind dat honger heeft of zich niet veilig voelt, komt niet aan leren toe."),
            ("p", "<strong>Carl Rogers</strong> werkte met <strong>client-centered therapy</strong>, "
                  "cliëntgerichte therapie: niet de therapeut maar de persoon zelf weet waar het over moet "
                  "gaan. Zijn begrippen:"),
            ("p", tabel(["Begrip", "Wat het is"], [
                ["het fenomenale veld", "de wereld zoals die persoon ze zelf beleeft"],
                ["het actuele zelf", "wie iemand vindt dat hij nu is"],
                ["het ideale zelf", "wie iemand zou willen zijn"],
                ["congruentie", "die twee liggen dicht bij elkaar; dat geeft rust"],
                ["incongruentie", "die twee liggen ver uit elkaar; dat geeft spanning"],
            ])),
            ("kader", "<strong>Congruentie betekent niet dat het ideale zelf verdwijnt.</strong> Het "
                      "betekent dat de afstand klein genoeg is om ermee te leven. Een doel hebben hoort bij "
                      "groeien; de spanning komt van een beeld dat onbereikbaar ver ligt."),
            ("weetje", "Rogers' <strong>fenomenale veld</strong> legt uit waarom twee kinderen in dezelfde "
                       "klas een heel andere dag hebben gehad. Wat telt, is niet de klas zoals een camera "
                       "ze ziet, maar de klas zoals zij ze beleefden."),
        ]),
    ],
    onthoud=[
        "Freud: bewust, voorbewust en onbewust; verdringing duwt iets naar het onbewuste.",
        "Es (lustprincipe), Ich (realiteitsprincipe), Über-ich (moraliteitsprincipe); eros en thanatos zitten in het Es.",
        "Bandura: wederzijds determinisme tussen cognities, omgeving en gedrag; zelfeffectiviteit is taakgebonden.",
        "Rotter: interne of externe locus of control als vaste eigenschap.",
        "Maslow: behoeftepiramide met zelfactualisatie bovenaan.",
        "Rogers: fenomenaal veld, actueel en ideaal zelf, congruentie en incongruentie.",
    ],
)

# ───────────────────────── 10. Trekken, big five, HEXACO
BUNDELS["persoonlijkheid-trekken-de-big-five-en-hexaco-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Persoonlijkheid: trekken, de big five en HEXACO",
    onder="De trektheoretische benadering: een persoonlijkheid beschrijven in een beperkt aantal eigenschappen. Van Allport over Eysenck naar de Big Five en HEXACO.",
    secties=[
        dict(kop="Allport: drie soorten trekken", blokken=[
            ("p", "De <strong>trektheoretische benadering</strong> wil een persoonlijkheid "
                  "<strong>beschrijven</strong> in een beperkt aantal eigenschappen, zodat je mensen op "
                  "dezelfde lijnen met elkaar kan vergelijken."),
            ("p", "<strong>Gordon Allport</strong> is de grondlegger. Hij deelt trekken in naar hoe veel "
                  "ze van iemands gedrag bepalen:"),
            ("p", tabel(["Soort trek", "Hoeveel", "Wat ze doet"], [
                ["cardinale trek", "zelden, soms geen enkele", "beheerst zowat het hele leven van iemand"],
                ["centrale trekken", "een handvol", "de eigenschappen waarmee je iemand beschrijft"],
                ["secundaire trekken", "veel", "komen alleen in bepaalde situaties naar boven"],
            ])),
            ("p", "Iemand beschrijven als behulpzaam, ordelijk en nieuwsgierig: dat zijn "
                  "<strong>centrale</strong> trekken. Zenuwachtig worden van spreken voor een groep is een "
                  "<strong>secundaire</strong> trek: ze laat zich alleen daar zien."),
            ("kader", "<strong>Een cardinale trek is uitzonderlijk.</strong> Volgens Allport heeft niet "
                      "iedereen er een. De meeste mensen beschrijf je met hun centrale trekken."),
        ]),
        dict(kop="Eysenck: het PEN-model", blokken=[
            ("p", "<strong>Hans Eysenck</strong> bracht het terug tot <strong>drie</strong> brede "
                  "dimensies. De beginletters vormen het woord <strong>PEN</strong>:"),
            ("p", tabel(["Dimensie", "Hoog betekent"], [
                ["psychoticisme", "weinig geremd, ongevoelig voor regels en voor anderen, op risico uit"],
                ["extraversie", "naar buiten gericht, gezelschap en prikkels opzoekend"],
                ["neuroticisme", "snel en sterk reageren op spanning, piekeren, emotioneel wisselend"],
            ])),
            ("p", "De fiche vraagt deze drie met hun naam. Let op de volgorde van de letters: "
                  "<strong>P</strong>sychoticisme, <strong>E</strong>xtraversie, "
                  "<strong>N</strong>euroticisme."),
            ("weetje", "Eysenck koppelde zijn dimensies aan het lichaam. Daarom staat hij in dit vak "
                       "<strong>twee keer</strong>: bij de biologische benadering met de "
                       "<strong>arousal</strong>, en hier bij de trekken met het <strong>PEN-model</strong>."),
        ]),
        dict(kop="Costa en McCrae: de Big Five", blokken=[
            ("p", "<strong>Costa en McCrae</strong> kwamen op <strong>vijf</strong> factoren uit, de "
                  "<strong>Big Five</strong>. De fiche noemt ze zo:"),
            ("p", tabel(["Factor", "Hoog betekent"], [
                ["openheid voor ervaringen", "nieuwsgierig, graag iets nieuws, open voor ideeën"],
                ["zorgvuldigheid", "ordelijk, plannend, afspraken nakomend"],
                ["extraversie", "naar buiten gericht, gezelschap opzoekend"],
                ["vriendelijkheid", "meegaand, behulpzaam, vertrouwend"],
                ["emotionele stabiliteit versus neuroticisme",
                 "rustig blijven onder spanning; laag is net het omgekeerde"],
            ])),
            ("kader", "De vijfde factor is <strong>één</strong> lijn met twee uiteinden: hoog is "
                      "<strong>emotionele stabiliteit</strong>, laag is <strong>neuroticisme</strong>. Het "
                      "zijn geen twee aparte factoren, dus de Big Five blijft vijf."),
            ("p", "Een <strong>factor</strong> is breder dan een trek: hij bundelt een reeks trekken die "
                  "in onderzoek samen bewegen. Daarom zijn vijf factoren genoeg voor een beschrijving waar "
                  "Allport nog honderden woorden voor nodig had."),
        ]),
        dict(kop="Lee en Ashton: HEXACO", blokken=[
            ("p", "<strong>Lee en Ashton</strong> maakten het <strong>HEXACO-model</strong>, met "
                  "<strong>zes</strong> factoren. Vijf ervan ken je al; er komt er <strong>één</strong> bij:"),
            ("p", tabel(["Factor", "In de Big Five?"], [
                ["integriteit", "nieuw"],
                ["emotionaliteit", "ja"],
                ["extraversie", "ja"],
                ["vriendelijkheid", "ja"],
                ["zorgvuldigheid", "ja"],
                ["openheid voor ervaringen", "ja"],
            ])),
            ("p", "De nieuwe factor is de <strong>integriteit</strong>, in het Engels "
                  "<strong>honesty-humility</strong>: eerlijkheid en bescheidenheid. Hoog betekent oprecht, "
                  "niet uit op eigen voordeel en niet geneigd anderen te gebruiken; laag betekent het "
                  "omgekeerde."),
            ("kader", "<strong>Dit is de vraag die in dit thema het vaakst terugkomt: het verschil tussen "
                      "de Big Five en HEXACO is de integriteit.</strong> HEXACO is dus niet een ander "
                      "model, maar hetzelfde met één factor erbij."),
            ("p", "Dat die factor erbij kwam, heeft een reden: hij voorspelt gedrag dat de vijf andere "
                  "niet goed dekken, zoals bedrog en misbruik maken van een ander. Iemand kan vriendelijk "
                  "overkomen en toch laag op integriteit scoren."),
            ("weetje", "<strong>HEXACO</strong> is een letterwoord van de zes factoren in het Engels: "
                       "<strong>H</strong>onesty-humility, <strong>E</strong>motionality, "
                       "e<strong>X</strong>traversion, <strong>A</strong>greeableness, "
                       "<strong>C</strong>onscientiousness, <strong>O</strong>penness. Zo onthoud je "
                       "meteen dat er zes zijn."),
        ]),
    ],
    onthoud=[
        "Allport: cardinaal (beheerst een heel leven, uitzonderlijk), centraal (een handvol), secundair (situatiegebonden).",
        "PEN van Eysenck: psychoticisme, extraversie, neuroticisme.",
        "Big Five van Costa en McCrae: openheid, zorgvuldigheid, extraversie, vriendelijkheid, emotionele stabiliteit versus neuroticisme.",
        "HEXACO van Lee en Ashton is de Big Five plus de integriteit (honesty-humility).",
    ],
)

# ───────────────────────── 11. Opvoeden: milieus, dimensies, stijlen, middelen
BUNDELS["opvoeden-milieus-dimensies-stijlen-en-middelen-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Opvoeden: milieus, dimensies, stijlen en middelen",
    onder="Het gereedschap van de pedagogiek: wie opvoedt, waar het gebeurt, met welke houding en met welke middelen. De stijlen volgen uit de dimensies.",
    secties=[
        dict(kop="Actoren en milieus", blokken=[
            ("p", "<strong>Pedagogiek</strong> is de wetenschap van het opvoeden. Opvoeden is een "
                  "<strong>proces</strong>: het loopt over jaren, in twee richtingen, en het eindigt niet "
                  "op één moment."),
            ("p", "De fiche noemt <strong>drie actoren</strong>: het <strong>kind</strong>, de "
                  "<strong>opvoeder(s)</strong> en de <strong>omgeving</strong>. Het kind staat er "
                  "uitdrukkelijk bij: het ondergaat de opvoeding niet alleen, het stuurt ze mee. Een kind "
                  "dat heftig reageert, krijgt een andere opvoeder tegenover zich dan een kind dat alles "
                  "laat gebeuren."),
            ("p", "Het opvoeden gebeurt in <strong>drie milieus</strong>:"),
            ("p", tabel(["Milieu", "Waar", "Wie"], [
                ["primair", "thuis", "ouders, broers en zussen, grootouders"],
                ["secundair", "waar het kind bewust naartoe gaat", "school, jeugdbeweging, club, academie"],
                ["tertiair", "wat het kind bereikt zonder dat het ergens naartoe gaat",
                 "media, sociale media, reclame, de buurt"],
            ])),
            ("kader", "Het verschil tussen <strong>secundair</strong> en <strong>tertiair</strong>: in een "
                      "secundair milieu <strong>ga</strong> je ergens naartoe, en er is iemand die opvoedt. "
                      "Een tertiair milieu <strong>komt naar jou</strong>, en niemand bedoelde het als "
                      "opvoeding."),
        ]),
        dict(kop="Drie opvoedingsdimensies", blokken=[
            ("p", "Een <strong>dimensie</strong> is een lijn waarop een opvoeder hoog of laag kan zitten. De "
                  "fiche noemt er drie, en die drie zijn de bouwstenen van de stijlen:"),
            ("p", tabel(["Dimensie", "Wat ze is", "Hoog betekent"], [
                ["responsiviteit", "ingaan op wat het kind nodig heeft en voelt",
                 "warm, luisterend, beschikbaar"],
                ["gedragsmatige controle", "sturen van wat een kind dóet, met regels en toezicht",
                 "duidelijke regels, weten waar je kind is"],
                ["psychologische controle", "sturen van wat een kind denkt en voelt, van binnenuit",
                 "schuldgevoel inzetten, liefde intrekken bij tegenspraak"],
            ])),
            ("kader", "<strong>Dit is de belangrijkste nuance van het hele thema.</strong> "
                      "<strong>Gedragsmatige</strong> controle is in onderzoek meestal "
                      "<strong>gunstig</strong>: een kind weet waar het aan toe is. "
                      "<strong>Psychologische</strong> controle is meestal <strong>schadelijk</strong>: ze "
                      "raakt het kind in zijn gevoel van eigenwaarde. Twee soorten controle, twee heel "
                      "andere gevolgen."),
            ("p", "Een regel als <em>om tien uur ben je thuis</em> is gedragsmatige controle. "
                  "<em>Als je nu gaat, doe je mij verdriet</em> is psychologische controle."),
        ]),
        dict(kop="Vier opvoedingsstijlen", blokken=[
            ("p", "De fiche zegt met zoveel woorden dat een <strong>opvoedingsstijl een combinatie van "
                  "dimensies</strong> is. Zet responsiviteit en controle naast elkaar en de vier stijlen "
                  "vallen op hun plaats:"),
            ("p", tabel(["Stijl", "Responsiviteit", "Controle", "Hoe het klinkt"], [
                ["autoritair", "laag", "hoog", "omdat ik het zeg"],
                ["democratisch-autoritatief", "hoog", "hoog", "dit is de regel, en dit is waarom"],
                ["permissief of toegeeflijk", "hoog", "laag", "doe maar wat je wil, ik ben er voor je"],
                ["onverschillig of laissez-faire", "laag", "laag", "zoek het zelf uit"],
            ])),
            ("kader", "<strong>Autoritair en autoritatief lijken op elkaar en zijn bijna tegengesteld.</strong> "
                      "<strong>Autoritair</strong> is streng <em>zonder</em> warmte. "
                      "<strong>Autoritatief</strong> is streng <em>met</em> warmte en met uitleg: de stijl "
                      "die in onderzoek het best uitpakt. Lees het woord dus twee keer."),
            ("p", "<strong>Laissez-faire</strong> is Frans voor laten doen. Het verschil met "
                  "<strong>permissief</strong> zit in de warmte: een permissieve opvoeder is er wél, maar "
                  "legt niets op; een onverschillige opvoeder is er niet."),
        ]),
        dict(kop="Negen opvoedingsmiddelen", blokken=[
            ("p", "De fiche geeft een lijst van <strong>negen</strong> middelen, in alfabetische orde:"),
            ("p", tabel(["Middel", "Wat de opvoeder doet"], [
                ["aanmoedigen of stimuleren", "het kind aanzetten om iets te proberen of door te zetten"],
                ["afleiden", "de aandacht van het kind naar iets anders brengen"],
                ["belonen", "gewenst gedrag iets aangenaams laten opleveren"],
                ["gewoontevorming", "iets zo vaak herhalen dat het vanzelf gaat"],
                ["informatieoverdracht", "uitleggen, vertellen waarom iets zo is"],
                ["negeren en time-out", "geen aandacht geven, of het kind even uit de situatie halen"],
                ["regels en grenzen stellen", "zeggen wat kan en wat niet"],
                ["straffen", "ongewenst gedrag iets onaangenaams laten opleveren"],
                ["voorbeeldgedrag of modelleren", "zelf doen wat je van het kind verwacht"],
            ])),
            ("p", "Twee van die middelen komen rechtstreeks uit de leertheorieën. "
                  "<strong>Belonen</strong> en <strong>straffen</strong> zijn "
                  "<strong>operante conditionering</strong> (Skinner), en "
                  "<strong>voorbeeldgedrag</strong> is <strong>observerend leren</strong> (Bandura). "
                  "Pedagogiek haalt haar gereedschap bij de psychologie."),
            ("weetje", "<strong>Afleiden</strong> staat niet voor niets in de lijst: bij een jong kind is "
                       "het vaak het meest werkzame middel van alle negen, omdat uitleggen nog niet "
                       "aankomt."),
        ]),
    ],
    onthoud=[
        "Actoren: kind, opvoeder(s), omgeving. Het kind stuurt mee.",
        "Milieus: primair (thuis), secundair (waar je naartoe gaat), tertiair (wat naar jou komt).",
        "Dimensies: responsiviteit, gedragsmatige controle (meestal gunstig), psychologische controle (meestal schadelijk).",
        "Stijlen: autoritair, democratisch-autoritatief, permissief, onverschillig. Een stijl is een combinatie van dimensies.",
        "Negen middelen, van aanmoedigen tot voorbeeldgedrag.",
    ],
)

# ───────────────────────── 12. Pedagogische modellen en bijzondere contexten
BUNDELS["pedagogische-modellen-en-opvoeden-in-bijzondere-contexten-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Pedagogische modellen en opvoeden in bijzondere contexten",
    onder="De visies achter het opvoeden, de factoren die meespelen, twee pedagogische modellen, en het opvoeden waar het niet vanzelf gaat.",
    secties=[
        dict(kop="Vier historische visies", blokken=[
            ("p", "Opvoeden is geen nieuwe vraag. De fiche noemt <strong>vier</strong> historische "
                  "pedagogische visies:"),
            ("p", tabel(["Visie", "De kern"], [
                ["de leer van Confucius", "opvoeden tot deugd en tot de juiste verhouding tot anderen; "
                 "leren door studie en navolging"],
                ["de leer van Plato", "de rede vormen; opvoeding als weg van de schijn naar het inzicht"],
                ["Abu Hamid ibn Muhammad Al-Ghazali", "kennis en geloof samen; het karakter van het kind "
                 "vormen, niet enkel zijn hoofd"],
                ["Jean-Jacques Rousseau", "het kind is geen kleine volwassene; opvoeden volgt de natuurlijke "
                 "ontwikkeling van het kind"],
            ])),
            ("p", "Bij <strong>Rousseau</strong> komt de gedachte naar boven die vandaag nog meespeelt: het "
                  "<strong>kind heeft een eigen aard en een eigen tempo</strong>, en opvoeding moet daarbij "
                  "aansluiten in plaats van er tegenin te duwen."),
        ]),
        dict(kop="Twee hedendaagse visies", blokken=[
            ("p", tabel(["Visie", "Wat ze inhoudt"], [
                ["behoefteondersteunende opvoeding",
                 "opvoeden vanuit de basisbehoeften van het kind: zich verbonden voelen, iets kunnen, "
                 "en zelf keuzes maken"],
                ["nieuwe autoriteit",
                 "gezag zonder machtsstrijd: de opvoeder blijft aanwezig en vasthoudend, zoekt steun bij "
                 "anderen rond het kind, en gaat geen gevecht aan dat hij niet kan winnen"],
            ])),
            ("kader", "<strong>Nieuwe autoriteit is geen zachtere autoriteit.</strong> De opvoeder geeft "
                      "niet toe; hij verzet zich <em>zonder</em> het gevecht aan te gaan, en hij staat er "
                      "niet alleen. Dat is het verschil met de autoritaire stijl, die het van macht "
                      "verwacht."),
            ("p", "De fiche noemt bij deze twee visies <strong>geen namen</strong> van auteurs. Ken dus wat "
                  "ze inhouden."),
        ]),
        dict(kop="Risico- en beschermende factoren", blokken=[
            ("p", "De fiche noemt opvoeding een <strong>multifactorieel proces</strong>: er werken "
                  "altijd <strong>meerdere factoren samen</strong> in, en je kan nooit één oorzaak "
                  "aanwijzen. Rond elke opvoeding staan factoren die het makkelijker of moeilijker "
                  "maken:"),
            ("p", tabel(["Soort factor", "Wat ze doet"], [
                ["risicofactor", "vergroot de kans dat het moeilijk loopt"],
                ["beschermende factor", "verkleint die kans, of vangt een risico op"],
            ])),
            ("p", "Ze spelen op <strong>drie niveaus</strong>: het "
                  "<strong>microniveau</strong>, het <strong>mesoniveau</strong> en het "
                  "<strong>macroniveau</strong>."),
            ("p", tabel(["Niveau", "Waar", "Risico", "Bescherming"], [
                ["micro", "het kind en het gezin", "ziekte, een scheiding, veel ruzie",
                 "een warme band met één ouder"],
                ["meso", "school, buurt, vrienden", "pesten, een school die niet mee wil",
                 "een leerkracht die het ziet, een club"],
                ["macro", "de samenleving", "armoede, discriminatie, een wachtlijst",
                 "een wet, een toelage, goede hulpverlening"],
            ])),
            ("kader", "<strong>Een risicofactor is geen voorspelling.</strong> Het gaat over "
                      "<em>kansen</em>, niet over wat er met dit kind zal gebeuren. Daarom staat de "
                      "beschermende factor er altijd naast: één stevige band kan veel risico opvangen."),
        ]),
        dict(kop="Bronfenbrenner en het balansmodel", blokken=[
            ("p", "De fiche noemt <strong>twee</strong> pedagogische modellen. Het eerste is het "
                  "<strong>bio-ecologisch model van Urie Bronfenbrenner</strong>, met zijn "
                  "<strong>vijf systemen</strong> rond het kind: het micro-, meso-, exo-, macro- en "
                  "chronosysteem. Dat model staat ook bij de ontwikkelingspsychologie, in de bundel over de "
                  "systemische benadering; het is dezelfde leerstof, hier gebruikt om een "
                  "opvoedingssituatie uit elkaar te halen."),
            ("p", "Het tweede is het <strong>balansmodel van Bakker et al.</strong> Dat zet twee stapels "
                  "op een weegschaal:"),
            ("p", tabel(["Kant", "Wat erin zit", "Voorbeeld"], [
                ["draaglast", "alles wat weegt", "ziekte, geldzorgen, een kind dat veel vraagt"],
                ["draagkracht", "alles wat je kan dragen", "gezondheid, een partner, familie die bijspringt, "
                 "ervaring"],
            ])),
            ("p", "Het model zegt: het gaat niet mis door de last alleen, maar door de "
                  "<strong>verhouding</strong> tussen de twee. Twee gezinnen met dezelfde zorg kunnen er "
                  "heel anders in staan omdat de draagkracht verschilt."),
            ("kader", "Daar volgt een praktische les uit: je kan een opvoedingssituatie op "
                      "<strong>twee</strong> manieren verbeteren. De last verlichten, of de kracht "
                      "versterken. Vaak is het tweede het enige dat kan."),
        ]),
        dict(kop="Bijzondere contexten", blokken=[
            ("p", "De fiche geeft een lijst van contexten waarin het opvoeden extra vraagt:"),
            ("p", tabel(["Context", "Wat eronder valt"], [
                ["handicap", "fysiek, zintuiglijk, verstandelijk, meervoudig"],
                ["ontwikkelingsstoornissen", "ADHD, ASS"],
                ["leerstoornissen", "dyslexie, dyscalculie"],
                ["verontrustende opvoedingssituaties", "afgekort VOS"],
                ["maatschappelijke kwetsbaarheid en kansarmoede", ""],
            ])),
            ("p", "<strong>Zintuiglijk</strong> gaat over zien en horen, <strong>fysiek</strong> over het "
                  "lichaam en het bewegen, <strong>verstandelijk</strong> over het cognitief functioneren, "
                  "en <strong>meervoudig</strong> is een combinatie. Een "
                  "<strong>leerstoornis</strong> zit op één schools domein (lezen bij dyslexie, rekenen bij "
                  "dyscalculie); een <strong>ontwikkelingsstoornis</strong> raakt het functioneren veel "
                  "breder."),
            ("p", "Een <strong>verontrustende opvoedingssituatie (VOS)</strong> is een situatie waarin de "
                  "ontwikkeling van een kind bedreigd is en er daarom hulp nodig is. "
                  "<strong>Kansarmoede</strong> is ruimer dan weinig geld: ze gaat over achterstand op "
                  "meerdere terreinen tegelijk, zoals wonen, gezondheid, werk en onderwijs."),
        ]),
        dict(kop="Twee orthopedagogische modellen", blokken=[
            ("p", "<strong>Orthopedagogiek</strong> is de pedagogiek voor wie extra ondersteuning nodig "
                  "heeft. <em>Ortho</em> betekent recht of juist."),
            ("p", "Het model <strong>kwaliteit van bestaan van Schalock en Verdugo</strong> vraagt niet wat "
                  "iemand mankeert, maar hoe goed zijn leven is. De fiche noemt drie velden:"),
            ("p", tabel(["Veld", "Waarover het gaat"], [
                ["onafhankelijkheid", "zelf kunnen beslissen en zelf dingen doen"],
                ["sociale participatie", "erbij horen, meedoen, relaties hebben"],
                ["welbevinden", "zich goed voelen, lichamelijk en emotioneel"],
            ])),
            ("p", "Het <strong>viervariabelenmodel van Jacobus E. Rink</strong> haalt een "
                  "opvoedingssituatie uit elkaar in vier letters: <strong>K</strong>, <strong>O</strong>, "
                  "<strong>Sc</strong> en <strong>St</strong>, voor het kind, de opvoeder, de "
                  "<strong>sc</strong>ene of situatie waarin het gebeurt, en de "
                  "<strong>st</strong>ructuur eromheen."),
            ("kader", "Beide modellen kijken <strong>naast</strong> de beperking. Dat is de kern van de "
                      "orthopedagogiek: een diagnose zegt wat iemand moeilijk heeft, en nog niets over wat "
                      "zijn leven goed maakt."),
        ]),
    ],
    onthoud=[
        "Historisch: Confucius, Plato, Al-Ghazali, Rousseau. Hedendaags: behoefteondersteunende opvoeding en nieuwe autoriteit.",
        "Risico- en beschermende factoren op micro-, meso- en macroniveau; een risico is een kans, geen voorspelling.",
        "Bronfenbrenner: vijf systemen. Balansmodel van Bakker: draaglast tegenover draagkracht.",
        "Bijzondere contexten: handicap, ontwikkelingsstoornissen, leerstoornissen, VOS, kansarmoede.",
        "Schalock en Verdugo: onafhankelijkheid, sociale participatie, welbevinden. Rink: K, O, Sc en St.",
    ],
)

# ───────────────────────── 13. Communicatieve vaardigheden
BUNDELS["communicatieve-vaardigheden-kaders-en-gesprekstechnieken-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Communicatieve vaardigheden: kaders en gesprekstechnieken",
    onder="Het enige thema van gedragswetenschappen dat niet vraagt om iets uit te leggen maar om iets te doen: een gesprek voeren met een empathische basishouding.",
    secties=[
        dict(kop="Een empathische basishouding", blokken=[
            ("p", "<strong>Empathie</strong> is je in de ander verplaatsen: zien hoe iets voor hem is, "
                  "zonder het over te nemen. De fiche vraagt uitdrukkelijk om een gesprek te voeren "
                  "<strong>met</strong> die houding, en noemt er <strong>zes</strong> onderdelen bij:"),
            ("p", tabel(["Onderdeel", "Wat je doet"], [
                ["actief luisteren", "echt volgen wat de ander zegt, en laten merken dat je volgt"],
                ["inlevingsvermogen", "aanvoelen wat iets voor de ander betekent"],
                ["open houding", "niet meteen oordelen of een oplossing klaar hebben"],
                ["echtheid", "jezelf blijven, niet een rol spelen"],
                ["respect", "de ander laten staan zoals hij is"],
                ["emotionele beschikbaarheid", "er zijn als er emotie komt, en die er mogen laten zijn"],
            ])),
            ("p", "Daar hoort één begrip bij dat je in elk gesprek terugziet: je "
                  "<strong>persoonlijk referentiekader</strong>. Dat is het geheel van ervaringen, "
                  "waarden en gewoonten waarmee jij naar de wereld kijkt. Het bepaalt wat je in een "
                  "verhaal opmerkt en hoe je het inschat, en het van de ander is nooit hetzelfde als "
                  "het jouwe. Daarom kan dezelfde zin bij twee mensen heel anders aankomen, en daarom "
                  "is doorvragen nodig in plaats van aannemen dat je het al begrijpt."),
            ("kader", "<strong>Empathie is niet hetzelfde als sympathie of medelijden.</strong> Bij "
                      "empathie begrijp je hoe het voor de ander is; je hoeft het niet eens te zijn en je "
                      "zakt er zelf niet in weg. <em>Dat moet lastig zijn voor jou</em> is empathie; "
                      "<em>ach, arme jij</em> is medelijden."),
        ]),
        dict(kop="Drie communicatiekaders", blokken=[
            ("p", "De fiche noemt <strong>drie</strong> interpersoonlijke communicatiekaders:"),
            ("p", tabel(["Kader", "Van wie", "De kern"], [
                ["verbindend communiceren", "Marshall B. Rosenberg",
                 "zeggen wat je ziet, voelt, nodig hebt en vraagt, zonder verwijt"],
                ["de geen-verliesmethode", "Thomas Gordon",
                 "een conflict oplossen zodat niemand verliest, in plaats van een winnaar aanwijzen"],
                ["geweldloze communicatie", "—",
                 "spreken zonder de ander aan te vallen, ook als je het oneens bent"],
            ])),
            ("p", "De <strong>geen-verliesmethode</strong> zoekt dus geen compromis waarin beiden iets "
                  "opgeven, maar een oplossing waarin beiden hun behoefte terugvinden. Daarvoor moet eerst "
                  "op tafel komen wat elk van de twee écht nodig heeft, en dat is zelden hetzelfde als wat "
                  "elk van de twee eist."),
            ("p", "<strong>Verbindend communiceren</strong> en een <strong>geweldloze boodschap</strong> "
                  "hebben in de fiche <strong>dezelfde vier stappen</strong>:"),
            ("p", tabel(["Stap", "De vraag", "Voorbeeld"], [
                ["waarneming", "wat zie of hoor ik, zonder oordeel?", "de afwas van drie dagen staat er nog"],
                ["gevoel", "wat voel ik daarbij?", "ik word daar moedeloos van"],
                ["behoefte", "wat heb ik nodig?", "ik heb nodig dat we dat samen dragen"],
                ["verzoek", "wat vraag ik concreet?", "wil jij vanavond afwassen?"],
            ])),
            ("kader", "De eerste stap is de moeilijkste. <strong>Een waarneming is wat een camera zou "
                      "zien</strong>: <em>de afwas staat er nog</em>. <em>Jij laat altijd alles staan</em> "
                      "is al een oordeel, en daar begint de ruzie."),
            ("p", "De fiche noemt <strong>vijf kenmerken</strong> van geweldloze communicatie: ze is "
                  "<strong>direct</strong>, <strong>doeltreffend</strong>, <strong>emotioneel</strong>, "
                  "<strong>empathisch</strong> en <strong>respectvol</strong>. <em>Geweldloos</em> betekent "
                  "dus niet vaag of voorzichtig: je zegt het rechtuit, alleen zonder aanval."),
        ]),
        dict(kop="De LSD-methode", blokken=[
            ("p", "<strong>LSD</strong> staat voor <strong>luisteren</strong>, "
                  "<strong>samenvatten</strong> en <strong>doorvragen</strong>: drie stappen die je in die "
                  "orde zet."),
            ("p", tabel(["Stap", "Soorten", "Wat je doet"], [
                ["luisteren", "non-verbaal en verbaal",
                 "non-verbaal met je lichaam (knikken, oogcontact), verbaal met kleine woordjes (ja, hm)"],
                ["samenvatten", "papegaaien, parafraseren, reflecteren", "teruggeven wat je gehoord hebt"],
                ["doorvragen", "open en gesloten vragen", "verder vragen op wat er ligt"],
            ])),
            ("p", "De drie manieren van samenvatten gaan steeds een stap dieper:"),
            ("p", tabel(["Manier", "Wat je teruggeeft", "Voorbeeld"], [
                ["papegaaien", "exact dezelfde woorden", "je zegt: het loopt niet"],
                ["parafraseren", "dezelfde inhoud in je eigen woorden", "dus het lukt op dit moment niet"],
                ["reflecteren", "het gevoel eronder", "ik hoor dat je er moedeloos van wordt"],
            ])),
            ("kader", "<strong>Reflecteren gaat over het gevoel, parafraseren over de inhoud.</strong> Dat "
                      "verschil is het makkelijkst te zien aan de woorden: in een reflectie staat een "
                      "gevoelswoord, in een parafrase niet."),
            ("p", "En het verschil tussen de twee soorten vragen:"),
            ("p", tabel(["Soort vraag", "Antwoord", "Voorbeeld", "Waarvoor"], [
                ["open vraag", "een verhaal", "hoe is dat voor jou?", "een gesprek openen"],
                ["gesloten vraag", "ja, nee, of één woord", "heb je het al gezegd?", "iets vastleggen"],
            ])),
            ("p", "In een gesprek met een empathische basishouding staan de "
                  "<strong>open</strong> vragen vooraan: een gesloten vraag levert één woord en legt het "
                  "gesprek stil."),
        ]),
        dict(kop="De ik-boodschap en het 4G-model", blokken=[
            ("p", "Twee schema's die sterk op elkaar lijken. De fiche noemt bij beide "
                  "<strong>vier</strong> onderdelen:"),
            ("p", tabel(["Een ik-boodschap", "Het 4G-model voor feedback"], [
                ["het gedrag", "gedrag"],
                ["het gevolg", "gevoel"],
                ["het gevoel", "gevolg"],
                ["een alternatief", "gewenst gedrag"],
            ])),
            ("p", "Het <strong>4G-model</strong> heeft zijn naam van de vier g's: "
                  "<strong>g</strong>edrag, <strong>g</strong>evoel, <strong>g</strong>evolg en "
                  "<strong>g</strong>ewenst gedrag. In de ik-boodschap staat op die vierde plaats een "
                  "<strong>alternatief</strong>, wat op hetzelfde neerkomt: zeggen wat je liever ziet."),
            ("kader", "Ken <strong>uit welke delen</strong> elk van de twee bestaat. De fiche zet gevoel en "
                      "gevolg in een verschillende orde, dus de orde van buiten leren helpt je niet."),
            ("p", "Het beslissende woord is <strong>ik</strong>. <em>Jij luistert nooit</em> is een "
                  "jij-boodschap en zet de ander in het verweer. <em>Ik merk dat ik twee keer moet vragen, "
                  "daar word ik ongeduldig van, want ik wil op tijd klaar zijn; wil je het meteen "
                  "doen?</em> is dezelfde boodschap, met alle vier de onderdelen erin."),
            ("weetje", "Zet de twee schema's naast de vier stappen van Rosenberg en je ziet dat het drie "
                       "keer hetzelfde idee is: <strong>eerst het feit, dan wat het met je doet, dan de "
                       "vraag</strong>. Wie dat patroon vasthoudt, heeft de drie schema's samen."),
        ]),
    ],
    onthoud=[
        "Empathische basishouding: actief luisteren, inlevingsvermogen, open houding, echtheid, respect, emotionele beschikbaarheid.",
        "Kaders: verbindend communiceren (Rosenberg), de geen-verliesmethode (Gordon), geweldloze communicatie.",
        "Vier stappen: waarneming, gevoel, behoefte, verzoek. Een waarneming is wat een camera ziet.",
        "LSD: luisteren, samenvatten (papegaaien, parafraseren, reflecteren), doorvragen (open en gesloten).",
        "Ik-boodschap: gedrag, gevolg, gevoel, alternatief. 4G: gedrag, gevoel, gevolg, gewenst gedrag.",
    ],
)

# ───────────────────────── 14. Socialisatie
BUNDELS["socialisatie-posities-rollen-en-vier-visies-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Socialisatie: posities, rollen en vier visies",
    onder="Het eerste van vijf thema's over sociale wetenschappen. Niet één mens, maar de samenleving waarin die mens staat. Met Durkheim, Mead, Parsons en Merton.",
    secties=[
        dict(kop="Vier sociologische begrippen", blokken=[
            ("p", "De <strong>sociologie</strong> kijkt niet naar één mens maar naar de "
                  "<strong>samenleving</strong>. Ze begint bij vier begrippen die je goed uit elkaar moet "
                  "houden:"),
            ("p", tabel(["Begrip", "Wat het is", "Voorbeeld"], [
                ["sociale positie", "de plaats die iemand in een geheel inneemt", "leerling, moeder, trainer"],
                ["sociale rol", "wat er bij die positie van je verwacht wordt",
                 "van een leerling: op tijd komen, taken maken"],
                ["sociale status", "het aanzien dat aan een positie hangt", "een arts geniet veel aanzien"],
                ["macht", "de mogelijkheid om het gedrag van anderen te bepalen",
                 "een directeur die een beslissing neemt"],
            ])),
            ("kader", "<strong>Positie en rol door elkaar halen is de klassieke fout.</strong> Een "
                      "<strong>positie</strong> is de plaats, een <strong>rol</strong> is de verwachting. "
                      "Je <em>hebt</em> een positie en je <em>speelt</em> een rol. Eén persoon heeft "
                      "verschillende posities tegelijk, en bij elke hoort een eigen rol."),
            ("p", "Daarom bestaat er een <strong>rolconflict</strong>: wat de ene positie van je vraagt, "
                  "botst met wat de andere vraagt. Een leerkracht die ook de mama van een leerling in zijn "
                  "klas is, zit in twee rollen die niet samengaan."),
            ("p", "<strong>Status</strong> is geen rol: ze zegt niets over wat je moet doen, alleen over "
                  "hoeveel aanzien de positie oplevert. En <strong>macht</strong> is weer iets anders: "
                  "aanzien en macht gaan vaak samen, maar niet altijd. Een geliefde leraar heeft status; "
                  "wie over het budget beslist, heeft macht."),
        ]),
        dict(kop="Drie vormen van socialisatie", blokken=[
            ("p", "<strong>Socialisatie</strong> is het proces waarin iemand de normen, waarden en "
                  "gewoonten van zijn samenleving overneemt. Ze gebeurt in drie vormen:"),
            ("p", tabel(["Vorm", "Waar", "Wat je er leert"], [
                ["primaire socialisatie", "het gezin, de eerste jaren",
                 "praten, wat hoort en niet hoort, basisvertrouwen"],
                ["secundaire socialisatie", "school, jeugdbeweging, later werk",
                 "omgaan met regels van buiten het gezin, een plaats in een groep"],
                ["tertiaire socialisatie", "media, sociale media, reclame",
                 "beelden van hoe je hoort te zijn, van buiten je eigen kring"],
            ])),
            ("kader", "Deze drie lopen <strong>gelijk met de drie opvoedingsmilieus</strong> uit de "
                      "pedagogiek: primair thuis, secundair waar je naartoe gaat, tertiair wat naar jou "
                      "komt. Twee vakken, één indeling."),
            ("p", "<strong>Primaire socialisatie is niet de belangrijkste omdat ze eerst komt alleen</strong>: "
                  "ze legt de basis waarop al de rest gebouwd wordt, want ze leert een kind de taal en de "
                  "eerste regels waarmee het de andere milieus binnengaat."),
        ]),
        dict(kop="Durkheim en Parsons: de samenleving eerst", blokken=[
            ("p", "<strong>Emile Durkheim</strong> kijkt naar de invloed van "
                  "<strong>instituties</strong> op het vormen van het individu: het gezin, de school, de "
                  "kerk, het recht. Zijn gedachte is dat die instituties "
                  "<strong>bestaan voor jij geboren bent</strong> en dat ze je vormen. Zonder gedeelde "
                  "normen valt een samenleving uit elkaar."),
            ("p", "<strong>Talcott Parsons</strong> staat voor het <strong>functionalisme</strong>: elk "
                  "onderdeel van een samenleving heeft een <strong>functie</strong> in het geheel, zoals "
                  "een orgaan in een lichaam. Socialisatie is in die visie de functie waarmee een "
                  "samenleving zichzelf in stand houdt: ze geeft haar normen door aan de volgende "
                  "generatie."),
            ("kader", "Durkheim en Parsons kijken <strong>van de samenleving naar de mens</strong>. Dat is "
                      "het omgekeerde van Mead, die van de mens en zijn gesprekken naar de samenleving "
                      "kijkt."),
        ]),
        dict(kop="Mead en Merton: de mens eerst", blokken=[
            ("p", "<strong>George Herbert Mead</strong> staat voor het <strong>symbolisch "
                  "interactionisme</strong>. Drie woorden met elk een betekenis: "
                  "<strong>symbolisch</strong> (we werken met symbolen, vooral met taal), "
                  "<strong>interactie</strong> (tussen mensen), en de gedachte dat "
                  "<strong>daarin</strong> de werkelijkheid gemaakt wordt."),
            ("p", "Volgens Mead leer je jezelf kennen <strong>door de ogen van anderen</strong>: je neemt "
                  "hun houding tegenover jou over en bouwt daarmee een beeld van wie je bent. Daarom is "
                  "spel bij kinderen zo belangrijk: wie vadertje en moedertje speelt, oefent erin zich in "
                  "de rol van een ander te zetten."),
            ("p", "<strong>Robert K. Merton</strong> leverde zijn bijdrage aan de "
                  "<strong>referentiegroepentheorie</strong>. Een "
                  "<strong>referentiegroep</strong> is de groep waarmee je je <strong>vergelijkt</strong> "
                  "en waaraan je je meet. En dat hoeft niet de groep te zijn waar je "
                  "<strong>bij</strong> hoort."),
            ("p", "Dat laatste is de kern: een leerling kan in de ene klas zitten en zich meten aan een "
                  "heel andere groep. Daarom kan iemand zich tekortgedaan voelen terwijl het hem objectief "
                  "goed gaat: hij vergelijkt zich met een groep die hoger ligt."),
            ("kader", "<strong>Een referentiegroep is niet noodzakelijk je eigen groep.</strong> Verwar ze "
                      "dus niet met de <strong>ingroup</strong> uit de sociale psychologie: die is de groep "
                      "waartoe je behoort, een referentiegroep is de groep waaraan je je spiegelt."),
        ]),
    ],
    onthoud=[
        "Positie is de plaats, rol is de verwachting, status is het aanzien, macht is kunnen bepalen wat anderen doen.",
        "Primaire (gezin), secundaire (school en werk) en tertiaire (media) socialisatie, gelijk met de drie opvoedingsmilieus.",
        "Durkheim: instituties vormen het individu. Parsons: functionalisme, elk deel heeft een functie.",
        "Mead: symbolisch interactionisme, je wordt jezelf in de omgang met anderen.",
        "Merton: referentiegroepentheorie; de groep waarmee je je vergelijkt hoeft niet je eigen groep te zijn.",
    ],
)

# ───────────────────────── 15. Sociale stratificatie
BUNDELS["sociale-stratificatie-en-de-verklaringsmodellen-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Sociale stratificatie en de verklaringsmodellen",
    onder="De gelaagdheid van een samenleving: wie staat waar, en waarom. Vier stratificatiesystemen, vijf verklaringsmodellen en de indeling van vandaag.",
    secties=[
        dict(kop="Wat stratificatie is", blokken=[
            ("p", "<strong>Sociale stratificatie</strong> is de <strong>gelaagdheid</strong> van een "
                  "samenleving: mensen staan niet naast elkaar maar in lagen boven elkaar, met ongelijke "
                  "toegang tot geld, aanzien en macht. Het woord komt van "
                  "<em>stratum</em>, Latijn voor laag, net als in de aardlagen."),
            ("p", "Stratificatie is daarom <strong>geen kwestie van individueel verschil</strong>: ze zit "
                  "in de <strong>structuur</strong> van een samenleving. Ze gaat niet over wie slimmer of "
                  "harder werkt, maar over het feit dat er lagen bestaan waarin mensen geboren worden."),
            ("p", "De fiche noemt <strong>vier</strong> stratificatiesystemen, van het meest naar het "
                  "minst vastliggende:"),
            ("p", tabel(["Systeem", "Hoe je laag bepaald wordt", "Kan je veranderen?"], [
                ["slavenmaatschappij", "een mens is iemands bezit", "nee, je bent eigendom"],
                ["kastenmaatschappij", "je wordt in je kaste geboren, vaak religieus onderbouwd",
                 "nee, ook niet met geld"],
                ["standenmaatschappij", "geboorte en stand, met eigen rechten per stand",
                 "nauwelijks, soms via de kerk of het leger"],
                ["klassenmaatschappij", "je plaats in het economisch leven", "ja, in principe"],
            ])),
            ("kader", "<strong>Kaste en stand lijken op elkaar en zijn niet hetzelfde.</strong> Een "
                      "<strong>kaste</strong> ligt volledig vast en is religieus onderbouwd; een "
                      "<strong>stand</strong> (adel, geestelijkheid, derde stand) is wettelijk vastgelegd "
                      "met eigen rechten en plichten, en er was heel beperkt beweging mogelijk."),
        ]),
        dict(kop="Vier conflictsociologische modellen", blokken=[
            ("p", "Het <strong>conflictsociologisch perspectief</strong> ziet een samenleving als een "
                  "plaats van <strong>strijd</strong> om schaarse goederen. De fiche zet er vier "
                  "verklaringsmodellen onder, met hun eeuw erbij. In die orde zie je het denken "
                  "verschuiven:"),
            ("p", tabel(["Model", "Eeuw", "Waarin zit de ongelijkheid?"], [
                ["Marx", "19de eeuw", "in het <strong>bezit</strong> van de productiemiddelen: "
                 "wie de fabriek bezit tegenover wie er werkt"],
                ["Weber", "begin 20ste eeuw", "in <strong>drie</strong> dingen samen: economische klasse, "
                 "status of aanzien, en partij of macht"],
                ["Dahrendorf", "20ste eeuw", "in <strong>gezag</strong>: wie mag bevelen en wie moet "
                 "gehoorzamen, ook zonder bezit"],
                ["Bourdieu", "20ste eeuw", "in verschillende vormen van <strong>kapitaal</strong>: "
                 "economisch, cultureel en sociaal"],
            ])),
            ("p", "<strong>Marx</strong> werkt met <strong>twee</strong> klassen en één lijn: bezit of geen "
                  "bezit. <strong>Weber</strong> maakt er drie lijnen van, en legt daarmee uit waarom "
                  "iemand rijk kan zijn met weinig aanzien, of veel aanzien met weinig geld."),
            ("p", "<strong>Dahrendorf</strong> verschuift het naar <strong>gezag</strong>. Dat verklaart de "
                  "moderne werkgever die zelf niets bezit: een afdelingshoofd in loondienst heeft gezag "
                  "zonder eigenaar te zijn."),
            ("p", "<strong>Bourdieu</strong> voegt toe dat je kan erven wat geen geld is:"),
            ("p", tabel(["Soort kapitaal", "Wat het is", "Voorbeeld"], [
                ["economisch", "geld en bezit", "een spaarrekening, een huis"],
                ["cultureel", "kennis, taal, diploma's, weten hoe het hoort",
                 "thuis boeken en de taal van de school horen"],
                ["sociaal", "je netwerk, wie je kent", "een oom die je aan een stage helpt"],
            ])),
            ("kader", "<strong>Cultureel kapitaal is het begrip waarmee Bourdieu de school uitlegt.</strong> "
                      "Twee kinderen met dezelfde verstandelijke mogelijkheden komen niet gelijk binnen: "
                      "het ene kende de taal van de school al van thuis."),
        ]),
        dict(kop="Davis en Moore: het functionalistische antwoord", blokken=[
            ("p", "Tegenover die vier staat <strong>één</strong> functionalistisch model: "
                  "<strong>Davis en Moore</strong>, 20ste eeuw. Zij zeggen: ongelijkheid heeft een "
                  "<strong>functie</strong>. Sommige posities zijn moeilijker en belangrijker, dus moet de "
                  "samenleving ze beter belonen, anders wil niemand er de lange opleiding voor doen."),
            ("p", "De tegenwerping is even belangrijk om te kennen: dan zouden de best betaalde beroepen "
                  "ook de nuttigste moeten zijn, en dat klopt niet. Bovendien kiest niet iedereen vrij: wie "
                  "geen middelen heeft, komt aan die lange opleiding niet toe."),
            ("kader", "<strong>Dit is het grote onderscheid van het thema.</strong> Conflictsociologie ziet "
                      "ongelijkheid als een <strong>probleem dat uit strijd komt</strong>; functionalisme "
                      "ziet haar als een <strong>nuttig mechanisme</strong>. Vier modellen in het eerste "
                      "kamp, één in het tweede."),
        ]),
        dict(kop="Stratificatie vandaag", blokken=[
            ("p", "De <strong>EGP-klassenindeling van Goldthorpe</strong> deelt mensen in naar hun "
                  "<strong>beroep</strong> en naar de <strong>arbeidsverhouding</strong> die erbij "
                  "hoort: in loondienst of zelfstandig, met of zonder gezag, vast of los. Zo komt ze op "
                  "<strong>meerdere</strong> groepen uit, waar Marx er twee had: bovenaan de dienstklasse "
                  "van hogere beroepen en leidinggevenden, onderaan de ongeschoolde arbeid, met daartussen "
                  "de routinematige hoofdarbeid, de zelfstandigen en de geschoolde arbeid."),
            ("p", "De <strong>sociaal-economische status</strong> of <strong>SES</strong> vat iemands "
                  "positie samen uit meestal <strong>drie</strong> gegevens: "
                  "<strong>opleiding</strong>, <strong>beroep</strong> en <strong>inkomen</strong>."),
            ("p", "De SES wordt zoveel gebruikt omdat ze samenhangt met bijna alles: met gezondheid en "
                  "levensverwachting, met schoolresultaten, met wonen en met deelname aan het verenigings"
                  "leven. Daarom staat ze in zowat elk sociaal onderzoek als achtergrondgegeven."),
            ("kader", "<strong>SES is niet hetzelfde als inkomen.</strong> Inkomen is er één van de drie. "
                      "Iemand met een hoog diploma en een laag loon heeft een andere SES dan iemand met "
                      "hetzelfde loon zonder diploma."),
        ]),
    ],
    onthoud=[
        "Stratificatie is gelaagdheid in de structuur van een samenleving, niet een individueel verschil.",
        "Vier systemen: slaven-, kasten-, standen- en klassenmaatschappij.",
        "Conflictsociologisch: Marx (bezit), Weber (klasse, status, partij), Dahrendorf (gezag), Bourdieu (economisch, cultureel en sociaal kapitaal).",
        "Functionalistisch: Davis en Moore, ongelijkheid beloont de moeilijke en belangrijke posities.",
        "Vandaag: de EGP-indeling van Goldthorpe naar beroep, en de SES uit opleiding, beroep en inkomen.",
    ],
)

# ───────────────────────── 16. Sociale mobiliteit
BUNDELS["sociale-mobiliteit-meritocratie-en-het-matheuseffect-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Sociale mobiliteit, meritocratie en het matheüseffect",
    onder="Kan je van laag veranderen, en voor wie is dat moeilijker? Vier soorten mobiliteit, tien factoren, en waarom voordelen terechtkomen bij wie al voorop zit.",
    secties=[
        dict(kop="Vier soorten mobiliteit", blokken=[
            ("p", "<strong>Sociale mobiliteit</strong> is beweging van de ene sociale positie naar de "
                  "andere. Het vorige thema vroeg <em>hoe</em> een samenleving in lagen ligt; dit thema "
                  "vraagt of je van laag kan <strong>veranderen</strong>."),
            ("p", "De fiche kruist twee vragen: gaat het <strong>omhoog of omlaag</strong>, en gebeurt het "
                  "<strong>binnen één leven of tussen generaties</strong>?"),
            ("p", tabel(["Soort", "Wat het betekent", "Voorbeeld"], [
                ["horizontale mobiliteit", "een andere positie op <strong>dezelfde</strong> hoogte",
                 "van verpleegkundige naar leerkracht"],
                ["verticale mobiliteit", "naar een <strong>hogere of lagere</strong> positie",
                 "van arbeider naar ploegbaas, of een faillissement"],
                ["intragenerationele mobiliteit", "beweging in <strong>één eigen</strong> loopbaan",
                 "beginnen aan de kassa en eindigen als filiaalhouder"],
                ["intergenerationele mobiliteit", "verschil <strong>tussen ouder en kind</strong>",
                 "de dochter van een poetsvrouw wordt arts"],
            ])),
            ("kader", "<strong>Intra betekent binnen, inter betekent tussen.</strong> Dat ene letterverschil "
                      "is hier het hele antwoord. Intra blijft bij één persoon, inter vergelijkt twee "
                      "generaties."),
            ("p", "De twee paren staan los van elkaar en combineren. Wie in zijn eigen loopbaan opklimt, "
                  "maakt <strong>verticale en intragenerationele</strong> mobiliteit tegelijk."),
        ]),
        dict(kop="Tien factoren", blokken=[
            ("p", "De fiche noemt tien factoren die mobiliteit beïnvloeden, in alfabetische orde: "
                  "<strong>afkomst</strong>, <strong>beroep</strong>, <strong>gender</strong>, "
                  "<strong>handicap</strong>, <strong>huwelijk en echtscheiding</strong>, "
                  "<strong>inkomen</strong>, <strong>rijkdom of bezit</strong>, "
                  "<strong>kennis</strong>, <strong>leeftijd</strong> en "
                  "<strong>migratiegeschiedenis</strong>."),
            ("p", "Twee daarvan verdienen een woord. <strong>Inkomen</strong> is wat er binnenkomt, "
                  "<strong>rijkdom of bezit</strong> is wat er al staat; ze staan niet voor niets apart, "
                  "want bezit kan geërfd worden en geeft een buffer die een loon niet geeft. En "
                  "<strong>huwelijk en echtscheiding</strong> kunnen in beide richtingen werken: een "
                  "huwelijk kan een positie optrekken, een scheiding kan er een doen zakken, vaker bij "
                  "vrouwen met kinderen."),
            ("weetje", "<strong>Leeftijd</strong> staat er ook bij, en dat is makkelijk te vergeten. Wie op "
                       "zijn vijftigste zijn werk verliest, komt veel moeilijker terug op niveau dan wie "
                       "dat op zijn vijfentwintigste overkomt."),
        ]),
        dict(kop="Onderwijs en meritocratie", blokken=[
            ("p", "<strong>Onderwijs</strong> is in theorie de grote <strong>motor</strong> van opwaartse "
                  "mobiliteit: een diploma opent deuren die afkomst sluit. Maar onderzoek laat ook zien dat "
                  "het onderwijs ongelijkheid <strong>doorgeeft</strong>: de studierichting die een kind "
                  "terechtkomt hangt mee samen met de opleiding van zijn ouders, en kinderen uit gezinnen "
                  "met minder middelen stromen vaker af naar een kortere opleiding."),
            ("kader", "Onderwijs doet dus <strong>beide</strong>. Het is tegelijk de belangrijkste weg naar "
                      "boven én de plaats waar bestaande ongelijkheid bevestigd wordt. Wie maar één van die "
                      "twee zegt, heeft maar de helft van het antwoord."),
            ("p", "Een <strong>meritocratie</strong> is een samenleving waarin je plaats bepaald wordt door "
                  "je <strong>verdienste</strong>: je talent en je inzet. <em>Meritum</em> is Latijn voor "
                  "verdienste."),
            ("p", tabel(["Voor meritocratie", "Tegen meritocratie"], [
                ["afkomst en geboorte beslissen niet meer",
                 "talent en inzet zijn zelf ongelijk verdeeld bij de start"],
                ["de juiste mensen komen op de juiste plaats",
                 "wie het niet haalt, krijgt de schuld: je hebt het zelf niet goed genoeg gedaan"],
                ["het moedigt inzet en opleiding aan",
                 "verdienste wordt gemeten met middelen die niet iedereen heeft"],
            ])),
            ("p", "Het zwaarste argument tegen is dat laatste: een meritocratie verandert de ongelijkheid "
                  "van een <strong>onrecht</strong> in iets dat je zelf <strong>verdiend</strong> hebt. Dat "
                  "maakt haar moeilijker aan te klagen."),
        ]),
        dict(kop="Uitsluiting en het matheüseffect", blokken=[
            ("p", "<strong>Sociale uitsluiting</strong> is niet mee kunnen doen aan wat in een samenleving "
                  "gewoon is: niet mee op reis, geen lidmaatschap, geen netwerk, geen uitnodiging. Een "
                  "lagere sociale positie verhoogt die kans, en uitsluiting "
                  "<strong>versterkt op haar beurt die lage positie</strong>: wie niet meedoet, bouwt geen "
                  "netwerk op, en net dat netwerk helpt aan werk."),
            ("p", "Zo ontstaat een <strong>vicieuze cirkel</strong>: de positie leidt tot uitsluiting, de "
                  "uitsluiting houdt de positie vast."),
            ("p", "Het <strong>matheüseffect</strong> zet daar nog iets bovenop: de "
                  "<strong>voordelen van sociaal beleid</strong> komen in de praktijk vooral terecht bij "
                  "wie al het best geplaatst is."),
            ("p", tabel(["Maatregel voor iedereen", "Wie er het meest aan heeft"], [
                ["studietoelagen en goedkoop hoger onderwijs",
                 "gezinnen die hun kind tot daar brengen"],
                ["gesubsidieerde cultuur, muziekschool, sportclub",
                 "wie de weg kent en het aanbod vindt"],
                ["een belastingvoordeel voor pensioensparen",
                 "wie geld kan wegzetten"],
                ["kinderopvang met korting", "wie een plaats weet te krijgen"],
            ])),
            ("kader", "<strong>Het matheüseffect gaat niet over wie recht heeft op de maatregel.</strong> "
                      "De maatregel staat open voor iedereen; het gaat over <strong>wie ze in de praktijk "
                      "weet te gebruiken</strong>. Daarom is een maatregel voor iedereen soms minder "
                      "herverdelend dan ze lijkt."),
            ("weetje", "De naam komt uit het evangelie van Matteüs, waar staat dat wie heeft nog meer zal "
                       "krijgen. Vandaar <strong>matheüseffect</strong>: aan wie veel heeft, wordt nog "
                       "gegeven."),
        ]),
    ],
    onthoud=[
        "Horizontaal is dezelfde hoogte, verticaal omhoog of omlaag, intra binnen één loopbaan, inter tussen generaties.",
        "Tien factoren, van afkomst en gender tot leeftijd en migratiegeschiedenis.",
        "Onderwijs is tegelijk de motor van opwaartse mobiliteit en de plaats waar ongelijkheid doorgegeven wordt.",
        "Meritocratie: verdienste beslist. Tegenargument: verdienste is zelf ongelijk verdeeld, en wie faalt krijgt de schuld.",
        "Matheüseffect: de voordelen van beleid komen terecht bij wie al het best geplaatst is.",
    ],
)

# ───────────────────────── 17. Mediatisering en de functies van de massamedia
BUNDELS["mediatisering-en-de-functies-van-de-massamedia-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Mediatisering en de functies van de massamedia",
    onder="Wat media voor jou doen en wat ze voor een samenleving doen. Vijf functies plus twee mengvormen, vijf politieke functies, en de media als vierde macht.",
    secties=[
        dict(kop="Mediatisering", blokken=[
            ("p", "<strong>Mediatisering</strong> is het verschijnsel dat steeds meer van het "
                  "maatschappelijke leven <strong>langs de media loopt</strong>: de politiek, het "
                  "onderwijs, de sport, de vrije tijd en het contact met vrienden."),
            ("p", "Het gaat dus niet enkel over <em>meer</em> media. Het gaat erover dat andere domeinen "
                  "zich <strong>naar de media gaan gedragen</strong>: een politicus bouwt zijn boodschap "
                  "op maat van een kort fragment, een club plant zijn wedstrijd op het uur dat de televisie "
                  "wil, een museum maakt een zaal die goed op een foto staat."),
            ("kader", "<strong>Mediatisering is niet hetzelfde als veel media gebruiken.</strong> Het gaat "
                      "over de <strong>logica</strong> van de media die buiten de media gaat gelden: "
                      "kort, zichtbaar, en met een beeld erbij."),
            ("p", "<strong>Massamedia</strong> zijn de media die een groot en onbekend publiek tegelijk "
                  "bereiken: krant, radio, televisie, en vandaag ook de grote platformen online."),
        ]),
        dict(kop="Vijf functies voor het individu", blokken=[
            ("p", "De fiche kijkt eerst naar wat media voor <strong>jou</strong> doen:"),
            ("p", tabel(["Functie", "Wat ze doet", "Voorbeeld"], [
                ["informatieve functie", "je op de hoogte brengen", "het journaal, een weerbericht"],
                ["educatieve functie", "je iets bijleren", "een documentaire, een uitleg over de hersenen"],
                ["ontspannende functie", "je vermaken", "een reeks, een spelprogramma"],
                ["persuasieve functie", "je overtuigen van een standpunt",
                 "een opiniestuk, een campagne tegen roken"],
                ["commerciële functie", "je iets doen kopen", "reclame"],
            ])),
            ("p", "Daarnaast noemt de fiche <strong>twee mengvormen</strong>:"),
            ("p", tabel(["Mengvorm", "Wat er mengt", "Voorbeeld"], [
                ["infotainment", "informatie en ontspanning", "een nieuwsquiz, een praatshow over de actualiteit"],
                ["edutainment", "educatie en ontspanning", "een programma waarin je leert terwijl je lacht"],
            ])),
            ("kader", "<strong>Persuasief en commercieel liggen dicht bij elkaar.</strong> Bij "
                      "<strong>persuasief</strong> willen ze je <em>mening</em> veranderen, bij "
                      "<strong>commercieel</strong> willen ze je iets <em>verkopen</em>. Een campagne tegen "
                      "roken is persuasief; een advertentie voor een gsm is commercieel."),
            ("weetje", "Eén uitzending kan verschillende functies tegelijk hebben. Een documentaire over "
                       "het klimaat informeert, leert bij, en wil je overtuigen: drie functies in één "
                       "programma."),
        ]),
        dict(kop="Functies voor de samenleving", blokken=[
            ("p", "Daarnaast heeft de fiche een tweede, <strong>aparte</strong> lijst: wat media voor de "
                  "<strong>samenleving</strong> doen. Daar staan er vier, en de eerste valt in vijf uiteen:"),
            ("p", tabel(["Functie voor de samenleving", "Wat ze doet"], [
                ["de politieke functie", "valt uiteen in vijf (zie hieronder)"],
                ["de cultuuroverdrachtfunctie", "waarden, gewoonten en verhalen doorgeven"],
                ["de vrijetijdsfunctie", "de vrije tijd van een hele samenleving vullen en mee indelen"],
                ["de sociale functie", "mensen met elkaar verbinden en gespreksstof geven"],
            ])),
            ("kader", "<strong>Dit onderscheid wordt het vaakst gevraagd.</strong> Dezelfde uitzending kan "
                      "voor <strong>jou</strong> ontspanning zijn en voor de <strong>samenleving</strong> "
                      "cultuuroverdracht. Lees dus eerst voor wie de functie geldt."),
            ("p", "De <strong>politieke functie</strong> bestaat uit vijf delen:"),
            ("p", tabel(["Deel", "Wat de media doen"], [
                ["informerende functie", "burgers de feiten geven die ze nodig hebben om te kiezen"],
                ["woordvoerder- of spreekbuisfunctie", "groepen en meningen aan het woord laten"],
                ["onderzoeksfunctie", "zelf uitzoeken wat niet in de openbaarheid lag"],
                ["commentaarfunctie", "de feiten wegen en er een standpunt bij geven"],
                ["controlerende of waakhondfunctie", "de macht in het oog houden en rekenschap vragen"],
            ])),
            ("p", "<strong>Informerend</strong> en <strong>onderzoek</strong> liggen niet even dicht bij "
                  "elkaar als het lijkt: informeren is doorgeven wat er is, onderzoeken is "
                  "<strong>zelf opgraven</strong> wat iemand liever verborgen hield. En "
                  "<strong>commentaar</strong> is niet hetzelfde als de "
                  "<strong>waakhondfunctie</strong>: commentaar geeft een mening, de waakhond vraagt "
                  "rekenschap."),
        ]),
        dict(kop="De vierde macht", blokken=[
            ("p", "In een democratie zijn er <strong>drie</strong> staatsmachten, en ze houden elkaar in "
                  "evenwicht:"),
            ("p", tabel(["Macht", "Wie", "Wat ze doet"], [
                ["wetgevende macht", "het parlement", "maakt de wetten"],
                ["uitvoerende macht", "de regering", "voert de wetten uit"],
                ["rechterlijke macht", "de rechtbanken", "spreekt recht"],
            ])),
            ("p", "De <strong>media als vierde macht</strong> staan daar <strong>naast</strong>: ze zijn "
                  "geen staatsmacht en ze zijn niet verkozen, maar ze hebben wel invloed, omdat ze de drie "
                  "andere in het oog houden en aan het publiek laten zien wat er gebeurt."),
            ("kader", "<strong>De vierde macht is geen vierde staatsmacht.</strong> Dat is het hele punt "
                      "van de uitdrukking: de media hebben hun invloed juist omdát ze onafhankelijk van de "
                      "staat staan. Wie ze bij de drie zou rekenen, zou hun functie onmogelijk maken."),
            ("p", "Precies daarom hangt die vierde macht aan de <strong>waakhondfunctie</strong>: zonder "
                  "media die durven onderzoeken en rekenschap vragen, blijft de controle op de macht in de "
                  "handen van de macht zelf."),
        ]),
    ],
    onthoud=[
        "Mediatisering: steeds meer van het leven loopt langs de media, en andere domeinen nemen hun logica over.",
        "Voor het individu: informatief, educatief, ontspannend, persuasief, commercieel, plus infotainment en edutainment.",
        "Voor de samenleving: de politieke functie, cultuuroverdracht, vrije tijd en de sociale functie.",
        "De politieke functie: informerend, spreekbuis, onderzoek, commentaar, waakhond.",
        "De media als vierde macht staan naast de wetgevende, uitvoerende en rechterlijke macht, niet erbij.",
    ],
)

# ───────────────────────── 18. Mediatheorieën en beeldvorming
BUNDELS["mediatheorieen-beeldvorming-en-persvrijheid-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Mediatheorieën, beeldvorming en persvrijheid",
    onder="Hoeveel invloed hebben media echt? Vijf theorieën, vijf mechanismen van beeldvorming, en waar de vrijheid van de pers stopt.",
    secties=[
        dict(kop="Van een publiek dat slikt naar een publiek dat kiest", blokken=[
            ("p", "De <strong>injectienaaldtheorie</strong> is de oudste en de eenvoudigste: de media "
                  "<strong>spuiten</strong> een boodschap in een publiek dat die zonder meer opneemt. Het "
                  "beeld is dat van een injectie: erin, en het werkt."),
            ("p", "Die theorie is <strong>achterhaald</strong>. Mensen blijken zelf te kiezen wat ze "
                  "bekijken, te praten met anderen, en niet te geloven wat niet bij hen past. Toch is ze "
                  "belangrijk om te kennen: ze is het <strong>vertrekpunt</strong> waar de andere "
                  "theorieën tegenin gaan."),
            ("p", "De <strong>functionalistische mediatheorie</strong> van "
                  "<strong>Lasswell</strong>, <strong>Lazarsfeld</strong>, <strong>Merton</strong> en "
                  "<strong>Wright</strong> draait de vraag om. Niet: wat doen de media met mensen? Maar: "
                  "<strong>wat doen mensen met de media?</strong> Het publiek kiest, gebruikt en haalt "
                  "eruit wat het nodig heeft."),
            ("kader", "<strong>Dit is de kantelvraag van het hele thema.</strong> Bij de injectienaald is "
                      "het publiek <strong>passief</strong>; bij de functionalistische theorie is het "
                      "<strong>actief</strong>. Wie dat verschil vasthoudt, heeft de orde van de vijf "
                      "theorieën vast."),
        ]),
        dict(kop="Drie theorieën over een eigen soort invloed", blokken=[
            ("p", "De drie volgende theorieën zeggen niet dat media alles bepalen, maar wijzen elk één "
                  "soort invloed aan:"),
            ("p", tabel(["Theorie", "Van wie", "Waarop de media invloed hebben"], [
                ["agendasettingtheorie", "McCombs en Shaw",
                 "op <strong>waarover</strong> we praten, niet op wat we vinden"],
                ["cultivatietheorie", "Gerbner",
                 "op ons <strong>wereldbeeld</strong>, door jarenlang kijken"],
                ["mediatiseringstheorie", "Stig Hjarvard",
                 "op de <strong>hele samenleving</strong>, die de logica van de media overneemt"],
            ])),
            ("p", "<strong>Agendasetting</strong> gaat over de <strong>agenda</strong>, de lijst van "
                  "onderwerpen. Als het nieuws drie weken over de files gaat, vindt het land de files "
                  "plots een belangrijk probleem, ook al waren ze er vorig jaar even erg. Wat je "
                  "<em>denkt</em> over de files bepalen de media daarmee niet."),
            ("p", "<strong>Cultivatie</strong> betekent cultiveren, telen: iets dat langzaam groeit. "
                  "Gerbners bekendste voorbeeld is wie veel televisie met geweld ziet en daardoor de wereld "
                  "<strong>gevaarlijker</strong> gaat inschatten dan ze is. Het effect komt niet van één "
                  "uitzending, maar van <strong>jaren</strong> kijken."),
            ("kader", "<strong>Agendasetting werkt snel, cultivatie langzaam.</strong> Een nieuwsgolf van "
                      "drie weken verandert de agenda; een wereldbeeld verandert in jaren. En "
                      "cultivatie gaat over een <strong>beeld van de werkelijkheid</strong>, niet over een "
                      "onderwerp."),
        ]),
        dict(kop="Vijf mechanismen bij beeldvorming", blokken=[
            ("p", "<strong>Beeldvorming</strong> is het beeld dat bij een publiek ontstaat. De fiche noemt "
                  "vijf mechanismen die daarin meespelen:"),
            ("p", tabel(["Mechanisme", "Wat er gebeurt", "Voorbeeld"], [
                ["framing", "hetzelfde feit in een kader zetten dat de betekenis stuurt",
                 "een betoging als een <em>protest</em> of als een <em>rel</em>"],
                ["priming", "een eerdere boodschap maakt wat erna komt klaar om zo gelezen te worden",
                 "na een reeks over fraude lees je een bericht over een ondernemer anders"],
                ["het selectieproces", "van alles wat gebeurt, komt maar een klein deel in het nieuws",
                 "één aanslag haalt het journaal, tien gewone dagen niet"],
                ["de selectiecriteria", "de maatstaven waarmee die keuze gemaakt wordt",
                 "nabijheid, bekende namen, hoe uitzonderlijk, hoeveel mensen het raakt"],
                ["stereotypering en sociale categorisering",
                 "mensen in groepen indelen en aan die groep vaste eigenschappen hangen",
                 "een hele groep beschrijven alsof allen hetzelfde zijn"],
            ])),
            ("kader", "<strong>Framing en priming door elkaar halen is hier de val.</strong> "
                      "<strong>Framing</strong> zit in de boodschap <em>zelf</em>: het kader waarin ze "
                      "verteld wordt. <strong>Priming</strong> zit in wat er <em>daarvoor</em> kwam: het "
                      "maakt de lezer klaar."),
            ("p", "<strong>Sociale categorisering</strong> is op zich niet kwaadwillig: ons brein deelt "
                  "nu eenmaal in om de wereld te kunnen overzien. Het wordt een probleem zodra er "
                  "<strong>vaste eigenschappen</strong> aan die categorie worden gehangen, want dan is het "
                  "een <strong>stereotype</strong>, en dat kan uitlopen op vooroordeel en discriminatie."),
        ]),
        dict(kop="Vrijheid van meningsuiting en persvrijheid", blokken=[
            ("p", tabel(["Vrijheid", "Van wie", "Wat ze beschermt"], [
                ["vrijheid van meningsuiting", "iedereen", "je mening mogen uiten en informatie mogen krijgen"],
                ["persvrijheid", "de pers", "zonder voorafgaande controle van de overheid kunnen berichten"],
            ])),
            ("p", "Beide horen in een <strong>democratie</strong> thuis, en om dezelfde reden: zonder "
                  "vrije informatie kan een burger niet weten waarover hij kiest, en zonder vrije pers "
                  "kan niemand de macht controleren. Dat is de <strong>waakhondfunctie</strong>, en zonder "
                  "persvrijheid bestaat ze niet."),
            ("p", "Maar ze zijn <strong>niet onbeperkt</strong>. De grenzen liggen bij onder andere:"),
            ("p", tabel(["Beperking", "Waarom"], [
                ["aanzetten tot haat of geweld", "de vrijheid van de ene mag de veiligheid van de andere "
                 "niet aantasten"],
                ["laster en eerroof", "een onwaarheid die iemands eer beschadigt"],
                ["het privéleven en de privacy", "ook wie in het nieuws komt, heeft een privéleven"],
                ["het beroepsgeheim en de bronnen", "wat iemand in vertrouwen zei, blijft beschermd"],
            ])),
            ("kader", "<strong>Persvrijheid betekent geen voorafgaande controle, niet geen "
                      "verantwoordelijkheid.</strong> Een journalist mag publiceren zonder dat iemand hem "
                      "op voorhand toelating geeft, en kan achteraf wel voor de rechter verantwoording "
                      "afleggen. Dat verschil tussen vooraf en achteraf is de kern van het begrip."),
            ("p", "In de wereld verschilt dat sterk. In sommige landen is er geen persvrijheid: de "
                  "overheid beslist wat er verschijnt, journalisten worden bedreigd of opgesloten, en "
                  "websites worden afgesloten. Organisaties stellen daarom ranglijsten van persvrijheid "
                  "op, waar landen van jaar tot jaar op stijgen en dalen."),
        ]),
    ],
    onthoud=[
        "Injectienaald: passief publiek, achterhaald. Functionalistisch (Lasswell, Lazarsfeld, Merton, Wright): actief publiek.",
        "Agendasetting (McCombs en Shaw): waarover we praten. Cultivatie (Gerbner): ons wereldbeeld, over jaren. Mediatisering (Hjarvard): de hele samenleving.",
        "Beeldvorming: framing (in de boodschap), priming (wat eraan voorafging), selectieproces, selectiecriteria, stereotypering en sociale categorisering.",
        "Persvrijheid is geen voorafgaande controle; verantwoordelijkheid achteraf blijft.",
    ],
)

# ───────────────────────── 19. Maatschappelijke vraagstukken
BUNDELS["maatschappelijke-vraagstukken-en-de-redeneeractiviteiten-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Maatschappelijke vraagstukken en de redeneeractiviteiten",
    onder="Twaalf vraagstukken, vijf invalshoeken om ze te beschrijven, en het schema van vier redeneeractiviteiten waarmee je er iets zinnigs over zegt.",
    secties=[
        dict(kop="Twaalf maatschappelijke vraagstukken", blokken=[
            ("p", "Een <strong>maatschappelijk vraagstuk</strong> is een kwestie die een hele samenleving "
                  "aangaat, waar meningen over verschillen en waar geen eenvoudige oplossing voor is. De "
                  "fiche noemt er twaalf, in alfabetische orde:"),
            ("p", tabel(["", "", ""], [
                ["arbeid", "diversiteit", "individualisering"],
                ["kansenongelijkheid", "klimaat", "media"],
                ["migratie", "mobiliteit", "onderwijs"],
                ["privacy", "rationalisering", "samenlevingsvormen"],
            ])),
            ("p", "Twee van die woorden worden makkelijk verkeerd gelezen. "
                  "<strong>Individualisering</strong> is het verschijnsel dat mensen minder in vaste "
                  "verbanden en meer als individu door het leven gaan: minder lidmaatschap, meer eigen "
                  "keuzes, en ook meer op jezelf aangewezen zijn. "
                  "<strong>Rationalisering</strong> is het verschijnsel dat steeds meer van het leven "
                  "geregeld wordt volgens berekening, efficiëntie en regels, en minder volgens gewoonte of "
                  "traditie: de wachtrij die een nummertje wordt, de zorg die in minuten per handeling "
                  "gaat."),
            ("p", "<strong>Mobiliteit</strong> betekent hier het verplaatsen van mensen en goederen: "
                  "verkeer, files, openbaar vervoer. Dat is niet de "
                  "<strong>sociale mobiliteit</strong> uit het eerdere thema, die over stijgen en dalen op "
                  "de sociale ladder gaat. Zelfde woord, ander vraagstuk."),
        ]),
        dict(kop="Vijf invalshoeken", blokken=[
            ("p", "Om een vraagstuk te <strong>beschrijven</strong> gebruik je invalshoeken. Dezelfde "
                  "kwestie ziet er van elke kant anders uit:"),
            ("p", tabel(["Invalshoek", "De vraag", "Bij het klimaat"], [
                ["economisch", "wat kost het, wat brengt het op, wie betaalt?",
                 "de prijs van energie, de kost van een overstroming"],
                ["sociaal", "wie wordt geraakt, en hoe verhouden mensen zich tot elkaar?",
                 "wie een slecht geïsoleerd huis huurt, voelt het eerst"],
                ["cultureel", "wat vinden mensen normaal, welke waarden spelen?",
                 "vliegen als vanzelfsprekend of niet meer"],
                ["politiek", "wie beslist, en welke keuzes liggen op tafel?",
                 "een klimaatwet, een akkoord tussen landen"],
                ["juridisch", "wat zegt de wet, welke rechten en plichten?",
                 "een vonnis dat een staat tot maatregelen verplicht"],
            ])),
            ("kader", "<strong>Sociaal en cultureel liggen het dichtst bij elkaar.</strong> "
                      "<strong>Sociaal</strong> gaat over <em>mensen en hun verhoudingen</em>: wie raakt "
                      "het, en hoe staan groepen tegenover elkaar. <strong>Cultureel</strong> gaat over "
                      "<em>waarden, gewoonten en betekenis</em>: wat men normaal vindt."),
            ("p", "En let op <strong>politiek</strong> tegenover <strong>juridisch</strong>: politiek is "
                  "wat er <em>beslist</em> wordt en door wie, juridisch is wat er in de wet "
                  "<em>staat</em> en wat een rechter ermee doet."),
        ]),
        dict(kop="Het schema van vier redeneeractiviteiten", blokken=[
            ("p", "De fiche heeft in haar bijlage een schema met <strong>vier "
                  "redeneeractiviteiten</strong>. Die vier staan in een <strong>vaste orde</strong>, en de "
                  "orde is de les: je kan niets oplossen wat je niet eerst beschreven en verklaard hebt."),
            ("p", tabel(["", "Activiteit", "De vraag", "Wat je doet"], [
                ["1", "een maatschappelijk probleem beschrijven", "wat is er aan de hand?",
                 "feiten, cijfers, wie het raakt, hoe groot het is"],
                ["2", "een maatschappelijk probleem verklaren", "waarom is het zo?",
                 "oorzaken zoeken, verbanden leggen, een theorie gebruiken"],
                ["3", "creatieve ideeën genereren", "wat zou kunnen helpen?",
                 "veel ideeën bedenken, nog zonder te schrappen"],
                ["4", "oplossingen evalueren", "zou het werken, en kan het?",
                 "de ideeën tegen criteria afwegen en kiezen"],
            ])),
            ("kader", "Stap <strong>3</strong> en stap <strong>4</strong> zijn met opzet apart gehouden. In "
                      "stap 3 <strong>mag je niets afkeuren</strong>: wie meteen begint te oordelen, houdt "
                      "twee saaie ideeën over. Het wegen gebeurt pas in stap 4."),
            ("p", "Bij <strong>elke</strong> stap hoort hetzelfde: <strong>redeneren met bewijs</strong>. "
                  "Elke bewering die je doet, hangt aan iets waar iemand ze aan kan nakijken: een cijfer, "
                  "een onderzoek, een wettekst, een getuigenis. Een bewering zonder bewijs is een mening, "
                  "en die kan wel in het gesprek, maar ze kan geen stap in het schema dragen."),
        ]),
        dict(kop="Vier criteria voor uitvoerbaarheid", blokken=[
            ("p", "In stap 4 weeg je een oplossing. De fiche geeft vier criteria om de "
                  "<strong>uitvoerbaarheid</strong> te beoordelen:"),
            ("p", tabel(["Criterium", "De vraag"], [
                ["tijd", "kan het binnen een redelijke termijn, en wanneer zie je resultaat?"],
                ["middelen", "is er genoeg geld, personeel, kennis en materiaal?"],
                ["ethische principes", "mag dit, is het eerlijk, raakt het niemands rechten?"],
                ["duurzaamheidsprincipes", "houdt het stand, en wat laat het na voor later?"],
            ])),
            ("p", "De twee laatste zijn de criteria die mensen vergeten. Een oplossing kan "
                  "<strong>snel en goedkoop</strong> zijn en toch afvallen: omdat ze een groep onrecht doet "
                  "(ethisch), of omdat ze het probleem naar later doorschuift (duurzaam)."),
            ("kader", "<strong>Uitvoerbaar is niet hetzelfde als doeltreffend.</strong> Een oplossing kan "
                      "werken en onuitvoerbaar zijn, en ze kan goed uitvoerbaar zijn en niets oplossen. In "
                      "stap 4 weeg je <strong>beide</strong> vragen."),
            ("weetje", "Het schema uit de bijlage krijgt het kind volgens de fiche "
                       "<strong>niet</strong> op het examen; het is er om mee voor te bereiden. De vier "
                       "activiteiten zelf worden wel gevraagd, dus die ken je van buiten."),
        ]),
    ],
    onthoud=[
        "Twaalf vraagstukken, van arbeid tot samenlevingsvormen; mobiliteit is hier verkeer, niet de sociale ladder.",
        "Vijf invalshoeken: economisch, sociaal, cultureel, politiek, juridisch.",
        "Vier redeneeractiviteiten in orde: beschrijven, verklaren, ideeën genereren, oplossingen evalueren.",
        "Bij elke stap: redeneren met bewijs.",
        "Uitvoerbaarheid wegen met tijd, middelen, ethische principes en duurzaamheidsprincipes.",
    ],
)

# ───────────────────────── 20. De onderzoekscyclus
BUNDELS["de-onderzoekscyclus-van-orienteren-tot-rapporteren-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De onderzoekscyclus van oriënteren tot rapporteren",
    onder="Vier fasen, zes criteria voor een goede onderzoeksvraag, en de soorten onderzoek. Het laatste thema van het vak.",
    secties=[
        dict(kop="Vier fasen", blokken=[
            ("p", "De <strong>onderzoekscyclus</strong> is de weg die een onderzoek aflegt. De fiche deelt "
                  "hem in <strong>vier</strong> fasen:"),
            ("p", tabel(["", "Fase", "Wat je doet"], [
                ["1", "oriënteren", "je thema verkennen, lezen wat er al is, en je onderzoeksvraag opstellen"],
                ["2", "voorbereiden", "kiezen hoe je het aanpakt: welke methode, welke mensen, welk "
                 "meetinstrument"],
                ["3", "uitvoeren", "de gegevens verzamelen en verwerken"],
                ["4", "rapporteren", "je besluit opschrijven en je werk zichtbaar maken"],
            ])),
            ("p", "Het heet een <strong>cyclus</strong> omdat het einde geen einde is: een besluit roept "
                  "nieuwe vragen op, en daar begint een volgend onderzoek. Rapporteren is dus niet alleen "
                  "afsluiten, het is ook het vertrekpunt voor wie na jou komt."),
            ("kader", "<strong>De onderzoeksvraag hoort bij oriënteren, niet bij voorbereiden.</strong> "
                      "Eerst weet je wát je wil weten, dan pas kies je hóe je het gaat onderzoeken. Wie de "
                      "methode eerst kiest, buigt zijn vraag naar zijn methode."),
        ]),
        dict(kop="Zes criteria voor een onderzoeksvraag", blokken=[
            ("p", "Een goede onderzoeksvraag moet aan <strong>zes</strong> criteria voldoen. De fiche zegt "
                  "dat het kind die lijst <strong>op het examen krijgt</strong>: ze moet ze niet van buiten "
                  "kennen, maar wel kunnen <strong>toepassen</strong> op een gegeven vraag."),
            ("p", tabel(["Criterium", "Wat het betekent", "Een vraag die eraan faalt"], [
                ["open", "er is meer dan ja of nee mogelijk",
                 "<em>Zijn jongeren veel op hun gsm?</em>"],
                ["enkelvoudig", "er zit maar één vraag in",
                 "<em>Hoeveel lezen jongeren en wat vinden hun ouders daarvan?</em>"],
                ["objectief", "er zit geen oordeel of sturing in",
                 "<em>Waarom is sociale media zo schadelijk voor kinderen?</em>"],
                ["haalbaar", "je kan ze met jouw tijd en middelen echt onderzoeken",
                 "<em>Hoe leven alle jongeren in Europa?</em>"],
                ["onderzoekbaar", "ze is met gegevens te beantwoorden, niet met een mening",
                 "<em>Mag een kind een gsm hebben?</em>"],
                ["relevant", "het antwoord doet iets voor iemand",
                 "<em>Hoeveel letters staan er in de schoolnaam van elke leerling?</em>"],
            ])),
            ("kader", "<strong>Objectief en onderzoekbaar worden het vaakst verward.</strong> Een "
                      "<strong>niet objectieve</strong> vraag zit het antwoord al in: ze veronderstelt dat "
                      "het schadelijk is. Een <strong>niet onderzoekbare</strong> vraag kan met geen "
                      "enkel gegeven beslecht worden, want ze vraagt wat mág, en dat is een "
                      "ethische vraag."),
            ("p", "<strong>Haalbaar</strong> gaat over jóu: je tijd, je geld, je bereik. "
                  "<strong>Onderzoekbaar</strong> gaat over de <strong>vraag zelf</strong>: ook met "
                  "onbeperkte middelen blijft <em>mag een kind een gsm hebben</em> onbeantwoordbaar met "
                  "gegevens."),
            ("p", "Twee hulpjes om vragen snel te betrappen. Een vraag die met <em>is</em>, <em>zijn</em> "
                  "of <em>heeft</em> begint, is vaak <strong>gesloten</strong>. En staat er een "
                  "<strong>en</strong> in het midden, dan is ze vaak niet <strong>enkelvoudig</strong>."),
        ]),
        dict(kop="Soorten onderzoek", blokken=[
            ("p", "De fiche zet twee paren naast elkaar. Het eerste gaat over <strong>waar je je "
                  "gegevens haalt</strong>:"),
            ("p", tabel(["Soort", "Waar de gegevens vandaan komen", "Voorbeeld"], [
                ["deskresearch", "uit wat er al bestaat; je zit aan je bureau",
                 "cijfers van Statbel, een bestaand rapport, vakliteratuur"],
                ["fieldresearch", "uit het veld; je gaat ze zelf halen",
                 "een enquête, een interview, een observatie"],
            ])),
            ("p", "Het tweede paar gaat over <strong>wat voor gegevens</strong> het zijn:"),
            ("p", tabel(["Soort", "Wat je verzamelt", "De vraag erachter", "Methode"], [
                ["kwantitatief", "getallen, van veel mensen", "hoeveel, hoe vaak, hoe sterk?",
                 "een enquête met gesloten vragen"],
                ["kwalitatief", "woorden en betekenis, van weinig mensen", "hoe en waarom?",
                 "een diepte-interview, een gesprek in groep"],
            ])),
            ("kader", "<strong>De twee paren staan los van elkaar en combineren.</strong> Je kan "
                      "kwantitatieve deskresearch doen (bestaande cijfers verwerken) én kwalitatieve "
                      "fieldresearch (zelf tien mensen interviewen). Vier combinaties, niet twee soorten "
                      "onderzoek."),
            ("p", "<strong>Kwantitatief</strong> levert breedte: je kan iets over een grote groep zeggen, "
                  "maar niet waarom iemand het doet. <strong>Kwalitatief</strong> levert diepte: je "
                  "begrijpt waarom, maar je kan het niet doortrekken naar iedereen. Daarom combineren veel "
                  "onderzoekers de twee: eerst gesprekken om te weten wat er speelt, dan een enquête om te "
                  "weten hoe vaak het speelt."),
            ("weetje", "<strong>Deskresearch is bijna altijd de eerste stap</strong>, ook als je een "
                       "veldonderzoek plant. Je wil niet zelf tweehonderd mensen bevragen over iets dat "
                       "iemand vorig jaar al uitzocht."),
        ]),
        dict(kop="Uitvoeren en rapporteren", blokken=[
            ("p", "Bij het <strong>uitvoeren</strong> horen een paar vaste zorgen. Je "
                  "<strong>steekproef</strong> moet lijken op de groep waarover je iets wil zeggen; anders "
                  "geldt je besluit enkel voor wie je bevroeg. Je vragen mogen niet "
                  "<strong>sturen</strong>, want een sturende vraag levert het antwoord dat erin zat. En "
                  "wie met mensen werkt, vraagt hun <strong>toestemming</strong>, zegt waarvoor de "
                  "gegevens dienen en houdt ze <strong>anoniem</strong>."),
            ("p", "Bij het <strong>rapporteren</strong> hoort dat je je "
                  "<strong>bronnen</strong> vermeldt, je <strong>werkwijze</strong> beschrijft zodat iemand "
                  "ze kan nakijken, en ook meldt wat er <strong>niet</strong> gelukt is. De beperkingen van "
                  "je onderzoek horen in je verslag; ze maken het sterker, niet zwakker."),
            ("kader", "<strong>Een verband is geen oorzaak.</strong> Twee dingen die samen bewegen, kunnen "
                      "beide door een derde veroorzaakt zijn. Wie meer ijsjes eet, verdrinkt vaker; het "
                      "ijsje is niet de oorzaak, de warme zomerdag is het. Dat is de fout die in een "
                      "verslag het vaakst gemaakt wordt."),
            ("p", "Dit blok weegt <strong>tien procent</strong> van het examen, en de fiche zegt erbij dat "
                  "<strong>alle leerinhouden van sociale wetenschappen</strong> in dat deel verwerkt kunnen "
                  "zijn. Een onderzoeksvraag over socialisatie, over stratificatie of over media kan dus "
                  "even goed komen."),
        ]),
    ],
    onthoud=[
        "Vier fasen: oriënteren (met de onderzoeksvraag), voorbereiden, uitvoeren, rapporteren.",
        "Zes criteria: open, enkelvoudig, objectief, haalbaar, onderzoekbaar, relevant. Je krijgt ze op het examen, dus pas ze toe.",
        "Haalbaar gaat over jouw middelen, onderzoekbaar over de vraag zelf.",
        "Deskresearch of fieldresearch, kwantitatief of kwalitatief; de twee paren combineren.",
        "Een verband is geen oorzaak.",
    ],
)

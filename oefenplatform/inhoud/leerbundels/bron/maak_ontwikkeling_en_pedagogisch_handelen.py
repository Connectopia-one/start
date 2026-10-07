# -*- coding: utf-8 -*-
"""De leerbundels voor ontwikkeling en pedagogisch handelen op 🚀 Boost
dubbele finaliteit.

Gebaseerd op de vakfiche 2DU ontwikkeling en pedagogisch handelen, geldig
vanaf 1 januari 2027. Zestien thema's: twee over welzijn en gezondheid, zes
over de ontwikkeling van baby tot oudere, twee over observeren en
rapporteren, één over gedrag en behoeften, drie over communiceren, en drie
over vrije tijd, spel en activiteiten.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde hoofdstuk
behandelen dezelfde stof met andere vragen. Kim laadt de bundel dus twee keer
op, één keer bij elk deel.

Elk getalvoorbeeld dat hier beweerd wordt, staat ook in controleer.py.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel
import svg

VAK = "Ontwikkeling en pedagogisch handelen"
DF = "🚀 Boost dubbele finaliteit — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", DF)
    BUNDELS[slug + "-boost-dubbele-finaliteit"] = b


# ───────────────────────── 1. Welzijn en welbevinden
zet("welzijn-en-welbevinden",
    titel="Welzijn en welbevinden",
    onder="Wat welzijn is, de vier soorten welbevinden, de geluksdriehoek, en het verschil tussen zelfzorg, mantelzorg en professionele zorg.",
    secties=[
        dict(kop="Welzijn", blokken=[
            ("p", "<strong>Welzijn is tevreden zijn.</strong> Niet alleen over wat je hebt, maar ook over "
                  "hoe je leeft. Daarom zitten er <strong>twee soorten tevredenheid</strong> in: "
                  "<strong>materiële en immateriële tevredenheid</strong>."),
            ("kader", tabel(["soort tevredenheid", "waar het over gaat", "voorbeeld"],
                            [["<strong>materiële tevredenheid</strong>", "wat je hebt: bezit, inkomen, voorzieningen", "<strong>een eigen woning</strong>"],
                             ["<strong>immateriële tevredenheid</strong>", "wat je voelt en beleeft: relaties, erkenning, zin, vrije tijd", "<strong>je gewaardeerd voelen</strong>"]])),
            ("p", "<strong>Welzijn gaat dus niet alleen over geld en bezit.</strong> Wie alles heeft maar "
                  "zich nergens thuis voelt, heeft weinig welzijn. En omgekeerd."),
        ]),
        dict(kop="De vier soorten welbevinden", blokken=[
            ("p", "Welbevinden is hoe je je voelt, en dat heeft <strong>vier kanten</strong>. "
                  "Financieel welbevinden staat niet in het rijtje."),
            ("kader", tabel(["soort", "waar het over gaat"],
                            [["<strong>fysiek welbevinden</strong>", "<strong>je lichaam voelt goed</strong>: gezond zijn, uitgerust zijn, geen pijn hebben"],
                             ["<strong>psychisch welbevinden</strong>", "je gevoelens en je gedachten: rustig in je hoofd zijn"],
                             ["<strong>sociaal welbevinden</strong>", "<strong>je hoort ergens bij</strong>: je plaats in een groep en je relaties met anderen"],
                             ["<strong>existentieel welbevinden</strong>", "<strong>je leven heeft zin</strong>: waarden en het gevoel dat je leven ergens over gaat"]])),
            ("p", "Let op het verschil tussen de eerste twee. <strong>Fysiek welbevinden gaat over je "
                  "lichaam, niet over je gevoelens</strong>; gevoelens horen bij het psychische welbevinden."),
        ]),
        dict(kop="De geluksdriehoek", blokken=[
            ("p", "<strong>De geluksdriehoek heeft drie bouwstenen</strong>, en samen tonen ze waar je zelf "
                  "aan kan werken om je beter te voelen."),
            ("fig", svg.driehoekmodel([("je goed voelen", "tevreden zijn met jezelf"),
                                       ("goed omringd zijn", "mensen om je heen"),
                                       ("jezelf kunnen zijn", "je niet hoeven te verstoppen")],
                                      "de geluksdriehoek")),
            ("p", "<strong>Goed omringd zijn</strong> gaat over mensen om je heen hebben, ergens bij horen "
                  "en steun krijgen. Het gaat niet over geld. <strong>Jezelf kunnen zijn betekent dat je "
                  "mag zijn wie je bent</strong>, zonder je te verstoppen voor de mensen om je heen. "
                  "<strong>De driehoek dient om het welbevinden te verhogen</strong>: haakt er één hoek, "
                  "dan weet je waar je kan beginnen."),
        ]),
        dict(kop="Gezondheid en de drie soorten zorg", blokken=[
            ("p", "<strong>Gezondheid is een toestand van volledig fysiek, psychisch en sociaal "
                  "welbevinden</strong>, dus <strong>drie dimensies</strong>. Daaruit volgt meteen dat "
                  "<strong>gezondheid meer is dan niet ziek zijn</strong>, en dat <strong>iemand met een "
                  "chronische ziekte niet per se ongezond is</strong>: wie diabetes heeft, kan zich "
                  "psychisch en sociaal uitstekend voelen."),
            ("p", "De omgeving maakt de gezonde keuze makkelijker of moeilijker. <strong>Een hefboom maakt "
                  "de gezonde keuze voor een gezonde levensstijl makkelijker</strong>, zoals een veilig fietspad in de buurt, een "
                  "gezonde kantine of water op school. <strong>Een drempel maakt ze moeilijker</strong>, "
                  "zoals geen veilig fietspad of een automaat vol frisdrank."),
            ("kader", tabel(["soort zorg", "wie het doet", "betaald?"],
                            [["<strong>zelfzorg</strong>", "<strong>je zorgt voor jezelf</strong>: eten, bewegen, tanden poetsen, rusten", "niet van toepassing"],
                             ["<strong>mantelzorg</strong>", "<strong>een naaste</strong>: familie, vrienden of buren, bijvoorbeeld de dochter die helpt", "<strong>meestal niet</strong>"],
                             ["<strong>professionele zorg</strong>", "<strong>iemand met een opleiding</strong> en een beroep in de zorg", "ja, het is zijn werk"]])),
            ("p", "<strong>Een mantelzorger is dus geen opgeleide beroepskracht</strong> maar een naaste die "
                  "zorg opneemt uit betrokkenheid. <strong>Zelfzorg is belangrijk omdat je er jezelf mee "
                  "gezond houdt</strong>: wat je zelf doet, bepaalt een groot deel van je gezondheid."),
        ]),
    ])


# ───────────────────────── 2. Wat bepaalt onze gezondheid
zet("wat-bepaalt-onze-gezondheid",
    titel="Wat bepaalt onze gezondheid",
    onder="De vier gezondheidsdeterminanten van Lalonde, het gedragswiel met zijn drie gedragsdeterminanten, en waarom een goed voornemen zo vaak niet lukt.",
    secties=[
        dict(kop="De vier determinanten van Lalonde", blokken=[
            ("p", "<strong>Lalonde onderscheidt vier gezondheidsdeterminanten</strong>: vier kanten "
                  "waarlangs je gezondheid bepaald wordt."),
            ("fig", svg.kwadranten([("biologische factoren", ["de erfelijkheid", "het geslacht", "de leeftijd"]),
                                    ("de omgeving", ["de woning", "de buurt", "het werk en de lucht"]),
                                    ("de voorzieningen van de gezondheidszorg", ["een huisarts in de buurt", "ziekenhuis en apotheek", "de prijs van de zorg"]),
                                    ("de leefstijl", ["eten en bewegen", "roken of niet roken", "slapen"])],
                                   onder="de vier samen bepalen hoe gezond iemand is")),
            ("p", "<strong>Biologische factoren zijn wat in je lichaam zit</strong>: erfelijkheid, geslacht "
                  "en leeftijd. <strong>De omgeving is alles buiten je lichaam</strong>: de woning, de "
                  "buurt, het werk, de lucht die je inademt. <strong>De leefstijl is wat je doet</strong>: "
                  "eten, bewegen, roken, slapen. <strong>Bij de voorzieningen horen artsen, ziekenhuizen, "
                  "apotheken en de prijs van de zorg.</strong>"),
            ("kader", tabel(["determinant", "kan je ze zelf veranderen?"],
                            [["<strong>de leefstijl</strong>", "<strong>het meest van de vier</strong>: je kiest wat je eet, hoeveel je beweegt en of je rookt"],
                             ["<strong>de omgeving</strong>", "deels, en vooral via de overheid: fietspaden, propere lucht"],
                             ["<strong>de voorzieningen</strong>", "zelf nauwelijks; de overheid maakt zorg toegankelijk en betaalbaar"],
                             ["<strong>de biologische factoren</strong>", "<strong>niet</strong>: je erfelijkheid ligt vast"]])),
            ("p", "<strong>Het model is nuttig omdat het laat zien dat gezondheid veel oorzaken heeft.</strong> "
                  "<strong>Niet alles is een eigen keuze</strong>: wie in een buurt zonder winkel of "
                  "fietspad woont, heeft minder keuze dan iemand anders. <strong>De overheid werkt daarom "
                  "aan de omgeving en de voorzieningen.</strong>"),
        ]),
        dict(kop="Het gedragswiel", blokken=[
            ("p", "Lalonde zegt wat je gezondheid bepaalt. Het gedragswiel zegt waarom gedrag wel of niet "
                  "lukt. <strong>Het gedragswiel heeft drie gedragsdeterminanten</strong>: "
                  "<strong>competenties, drijfveren en context</strong>."),
            ("fig", svg.driehoekmodel([("competenties", "wat je kan en kent"),
                                       ("drijfveren", "wat je wil en voelt"),
                                       ("context", "alles om je heen")],
                                      "het gedragswiel")),
            ("p", "<strong>Competenties zijn je kennis en je vaardigheden</strong>: weet je hoe het moet en "
                  "kan je het? <strong>Drijfveren zijn je motivatie, je gewoonten en je gevoelens.</strong> "
                  "<strong>De context is de omgeving</strong>: de mensen, de regels, het aanbod, de "
                  "prijzen. <strong>De context is dus alles buiten de persoon</strong>, terwijl de drijfveer "
                  "in de persoon zelf zit."),
            ("kader", tabel(["de situatie", "wat ontbreekt"],
                            [["iemand wil sporten, maar er is geen club in de buurt", "<strong>de context</strong>: de wil is er wel, het aanbod niet"],
                             ["iemand weet niet hoe hij gezond kookt", "<strong>de competentie</strong>: kennis en vaardigheid"],
                             ["iemand kan koken en heeft alles in huis, maar heeft geen zin", "<strong>de drijfveer</strong>: de motivatie"]])),
            ("p", "<strong>Het wiel is nuttig omdat je ziet waar het haakt</strong>: ligt het aan kunnen, "
                  "aan willen of aan de omgeving? <strong>Alleen willen volstaat niet</strong>; "
                  "<strong>gedrag verandert pas echt als je de drie samen aanpakt</strong>. <strong>Een "
                  "goed voornemen lukt vaak niet omdat de omgeving tegenwerkt</strong>: wie wil bewegen "
                  "maar in een buurt zonder veilig pad woont, houdt het niet lang vol."),
            ("weetje", "<strong>Gezondheidsgedrag</strong> is alles wat je doet of laat met gevolgen voor je "
                       "gezondheid: bewegen, gezond eten, voldoende slapen. Je lengte is geen gedrag maar "
                       "een biologisch gegeven."),
        ]),
    ])


# ───────────────────────── 3. Ontwikkeling: de basisbegrippen
zet("ontwikkeling-de-basisbegrippen",
    titel="Ontwikkeling: de basisbegrippen",
    onder="Groeien, rijpen en leren, de negen levensloopfasen, de drie ontwikkelingsfactoren nature, nurture en zelfbepaling, en de vijf ontwikkelingsdomeinen met hun auteurs.",
    secties=[
        dict(kop="Groeien, rijpen en leren", blokken=[
            ("p", "<strong>Ontwikkeling is altijd groeien, rijpen en leren samen.</strong> Het is dus niet "
                  "alleen groeien. De drie zijn makkelijk uit elkaar te houden."),
            ("kader", tabel(["deel", "wat het is", "voorbeeld"],
                            [["<strong>groeien</strong>", "<strong>groter worden</strong>: groter, zwaarder en anders van verhouding", "een kind wordt tien centimeter langer"],
                             ["<strong>rijpen</strong>", "<strong>klaar worden voor iets</strong>, vanzelf, zonder oefenen", "een baby stapt plots zonder dat iemand het hem leerde"],
                             ["<strong>leren</strong>", "<strong>door ervaring veranderen</strong>, door oefening en door wat de omgeving aanbiedt", "een kind leert zijn veters knopen"]])),
            ("p", "<strong>Rijpen gebeurt vanzelf, zonder oefenen</strong>, want het volgt uit de aanleg. "
                  "Leren vraagt wel oefening. Daar zit het verschil."),
        ]),
        dict(kop="De negen levensloopfasen", blokken=[
            ("p", "<strong>De levensloop telt negen fasen.</strong> Je deelt de levensloop in fasen in "
                  "<strong>omdat elke fase haar eigen kenmerken heeft</strong>: haar eigen typische "
                  "ontwikkeling, behoeften en aandachtspunten."),
            ("kader", tabel(["fase", "wanneer"],
                            [["<strong>de prenatale fase</strong>", "<strong>van de bevruchting tot de geboorte</strong>, dus voor de geboorte"],
                             ["<strong>de babytijd</strong>", "vanaf de geboorte"],
                             ["<strong>de peutertijd</strong>", "de jaren van het zelf willen doen"],
                             ["<strong>de kleutertijd</strong>", "de jaren van de kleuterschool"],
                             ["<strong>de midden-kindertijd</strong>", "<strong>ook de lagereschoolkindfase</strong> genoemd"],
                             ["<strong>de adolescentie</strong>", "<strong>na de midden-kindertijd</strong>, tussen kindertijd en volwassenheid"],
                             ["<strong>de vroege volwassenheid</strong>", "de eerste jaren als volwassene"],
                             ["<strong>de midden-volwassenheid</strong>", "de middenleeftijd"],
                             ["<strong>de late volwassenheid</strong>", "de oudere, met onder meer de pensioentijd"]])),
            ("p", "<strong>De prenatale fase begint dus niet bij de geboorte maar eindigt erbij</strong>; "
                  "daarna begint de babytijd."),
        ]),
        dict(kop="Nature, nurture en zelfbepaling", blokken=[
            ("p", "<strong>Er zijn drie ontwikkelingsfactoren</strong>, en de eerste twee hebben een "
                  "Engelse naam die je moet kennen."),
            ("kader", tabel(["factor", "wat het is", "voorbeeld"],
                            [["<strong>nature</strong>", "<strong>de erfelijkheid</strong>: wat je meekrijgt van je ouders, je aanleg", "een kind lijkt op zijn moeder"],
                             ["<strong>nurture</strong>", "<strong>de omgeving</strong>: opvoeding, school, vrienden, cultuur", "een kind leert thuis twee talen"],
                             ["<strong>zelfbepaling</strong>", "<strong>je kiest zelf mee</strong>: het kind geeft zelf richting aan zijn ontwikkeling", "een kind kiest zelf zijn hobby"]])),
            ("p", "Verwar de twee Engelse woorden niet: <strong>nature staat niet voor de omgeving maar voor "
                  "de erfelijkheid</strong>. <strong>Zelfbepaling betekent dat een kind ook zelf richting "
                  "geeft</strong>, naast wat het meekrijgt en wat het aangeboden krijgt."),
        ]),
        dict(kop="De vijf ontwikkelingsdomeinen", blokken=[
            ("p", "Ontwikkeling gebeurt op <strong>vijf domeinen</strong> tegelijk. Bij drie ervan hoort een "
                  "naam die je moet kennen."),
            ("kader", tabel(["domein", "waar het over gaat", "wie het beschreef"],
                            [["<strong>de fysieke ontwikkeling</strong>", "het lichaam: de lichamelijke, de sensorische, <strong>de motorische</strong> en de sensomotorische ontwikkeling", ""],
                             ["<strong>de cognitieve ontwikkeling</strong>", "<strong>het denken</strong>", "<strong>Piaget</strong>"],
                             ["<strong>de socio-emotionele ontwikkeling</strong>", "<strong>de sociale ontwikkeling</strong>, omgaan met emoties, vriendschappen maken", ""],
                             ["<strong>de morele ontwikkeling</strong>", "wat je juist en verkeerd vindt", "<strong>Kohlberg</strong>"],
                             ["<strong>de persoonlijkheidsontwikkeling</strong>", "wie je wordt", "<strong>Erikson</strong>"]])),
            ("p", "<strong>De motoriek hoort bij de fysieke ontwikkeling</strong>, niet bij de cognitieve. "
                  "En de lengte van een kind hoort bij de lichamelijke ontwikkeling, niet bij de "
                  "socio-emotionele."),
        ]),
    ])


# ───────────────────────── 4. De fysieke en motorische ontwikkeling
zet("de-fysieke-en-motorische-ontwikkeling",
    titel="De fysieke en motorische ontwikkeling",
    onder="De groeicurve, de drie groeiprincipes, de groeispurt, de zintuigen van een pasgeborene, de babyreflexen, en de mijlpalen van de grove en de fijne motoriek.",
    secties=[
        dict(kop="De groeicurve", blokken=[
            ("p", "<strong>Een groeicurve is een lijn met de groei van een kind erop.</strong> Ze zet de "
                  "<strong>lengte of het gewicht</strong> van een kind uit tegenover de "
                  "<strong>leeftijd</strong>, en <strong>vergelijkt het kind met zijn "
                  "leeftijdsgenoten</strong>. <strong>Je leest er dus van af of de groei normaal is</strong>: "
                  "volgt het kind de verwachte lijn, of wijkt het er plots van af?"),
            ("fig", svg.groeicurveschets()),
            ("p", "<strong>Een groeispurt is een periode waarin een kind heel snel groeit.</strong> In korte "
                  "tijd wordt het veel langer en zwaarder, vooral in de puberteit. <strong>Niet alle "
                  "kinderen hebben hun groeispurt op dezelfde leeftijd</strong>: de ene heeft een vroege, "
                  "de andere een late."),
            ("kader", tabel(["", "wat je voelt"],
                            [["<strong>een vroege groeispurt</strong>", "<strong>je valt uit de toon</strong>: wie veel eerder groeit dan de klas, krijgt opmerkingen en wordt ouder behandeld dan hij is"],
                             ["<strong>een late groeispurt</strong>", "<strong>je voelt je kleiner</strong> en jonger dan je leeftijdsgenoten"]])),
            ("p", "<strong>Een groeispurt is moeilijk voor een tiener omdat hij opvalt in de groep, zich "
                  "anders voelt en onhandiger wordt.</strong> Het lichaam verandert sneller dan de motoriek "
                  "volgt, en dat valt op."),
        ]),
        dict(kop="De drie groeiprincipes", blokken=[
            ("p", "De ontwikkeling van het lichaam volgt altijd dezelfde drie richtingen. Ze verklaren "
                  "waarom een kind de dingen in die volgorde leert."),
            ("kader", tabel(["principe", "wat het betekent"],
                            [["<strong>van kop naar staart</strong>", "<strong>het hoofd ontwikkelt eerst</strong>: een baby heeft eerst controle over hoofd en nek, dan over de romp, dan over de benen"],
                             ["<strong>van midden naar buiten</strong>", "<strong>de romp komt voor de hand</strong>: van het midden van het lichaam naar de uiteinden toe"],
                             ["<strong>van grof naar fijn</strong>", "<strong>eerst grote bewegingen</strong>: een kind grijpt eerst met de hele hand en pas later met duim en wijsvinger"]])),
        ]),
        dict(kop="De zintuigen van een pasgeborene", blokken=[
            ("p", "<strong>Het gehoor, de reuk en de smaak werken al goed rond de geboorte.</strong> Het "
                  "zicht en het dieptezicht hebben nog maanden nodig: <strong>een pasgeboren baby ziet nog "
                  "erg onscherp</strong> en op korte afstand. <strong>Het zicht ontwikkelt zich dus het "
                  "laatst</strong>, en een baby ziet zeker niet even scherp als een volwassene."),
            ("p", "<strong>Een baby herkent zijn moeder aan de reuk.</strong> Reuk en gehoor zijn vroeg "
                  "klaar, dus daaraan herkent een baby zijn vertrouwde mensen."),
        ]),
        dict(kop="De babyreflexen", blokken=[
            ("p", "Een baby komt met een aantal reflexen ter wereld. <strong>De babyreflexen verdwijnen "
                  "weer</strong>: de meeste in het eerste levensjaar, zodra de bewuste beweging het "
                  "overneemt. Ze blijven dus niet je hele leven."),
            ("kader", tabel(["reflex", "wat er gebeurt"],
                            [["<strong>de zuigreflex</strong>", "<strong>raak je de mond van een baby aan, dan begint hij te zuigen</strong>, zodat hij meteen kan drinken"],
                             ["<strong>de zoekreflex</strong>", "de baby draait zijn hoofd naar waar zijn wang aangeraakt wordt"],
                             ["<strong>de grijpreflex</strong>", "<strong>leg je een vinger in het handje, dan sluit de hand zich</strong> eromheen"],
                             ["<strong>de schrikreflex</strong>", "bij een hard geluid spreidt de baby plots armen en benen"],
                             ["<strong>de stapreflex</strong>", "houd je de baby rechtop met zijn voetjes op een vlak, dan maakt hij stapbewegingen"]])),
        ]),
        dict(kop="Grove en fijne motoriek", blokken=[
            ("p", "<strong>De grove motoriek zijn de grote bewegingen</strong> van armen, benen en romp. "
                  "<strong>De fijne motoriek zijn de kleine, precieze bewegingen</strong> van de handen en "
                  "de vingers. <strong>De grove motoriek ontwikkelt zich voor de fijne</strong>, want dat is "
                  "net het principe van grof naar fijn."),
            ("kader", tabel(["grove motoriek", "fijne motoriek"],
                            [["<strong>het hoofd optillen</strong>, en dat komt eerst", "<strong>met de hand grijpen</strong>"],
                             ["rollen en <strong>zitten</strong>", "<strong>de pincetgreep</strong>"],
                             ["<strong>kruipen</strong>", "<strong>leren tekenen</strong>"],
                             ["<strong>stappen</strong> en lopen", "schrijven"]])),
            ("p", "<strong>Zitten komt voor stappen</strong>, want de controle gaat van boven naar onder. "
                  "Een kind leert dus niet eerst stappen en daarna zitten. <strong>De pincetgreep is de "
                  "greep met duim en wijsvinger</strong>, waarmee een kind kleine dingen kan oppakken, "
                  "zoals een erwtje."),
            ("p", "<strong>Sensomotorische ontwikkeling is de zintuigen en de beweging samen</strong>: wat "
                  "je ziet of hoort, stuurt wat je doet. <strong>Een bal zien aankomen en hem vangen</strong> "
                  "is sensomotorisch handelen: je oog volgt de bal en je handen bewegen mee."),
        ]),
    ])


# ───────────────────────── 5. Het denken volgens Piaget
zet("het-denken-volgens-piaget",
    titel="Het denken volgens Piaget",
    onder="De vier stadia van de cognitieve ontwikkeling, de begrippen van de baby, de typische denkfouten van de kleuter, wat een lagereschoolkind erbij leert, en de taalontwikkeling van nul tot drie jaar.",
    secties=[
        dict(kop="De vier stadia", blokken=[
            ("p", "<strong>Piaget onderscheidt vier stadia</strong> in de ontwikkeling van het denken. Ze "
                  "volgen elkaar altijd in dezelfde volgorde op."),
            ("fig", svg.ladder([("formeel-operationeel", "de adolescent: abstract en hypothetisch"),
                                ("concreet-operationeel", "het lagereschoolkind: logisch, maar concreet"),
                                ("pre-operationeel", "de peuter en de kleuter: symbolisch"),
                                ("sensomotorisch", "de baby: zintuigen en beweging")],
                               bovenaan="het laatst", onderaan="het eerst")),
        ]),
        dict(kop="De baby: het sensomotorische stadium", blokken=[
            ("p", "<strong>Een baby zit in het sensomotorische stadium</strong> en leert de wereld kennen "
                  "<strong>met zijn zintuigen en zijn bewegingen</strong>. Drie begrippen horen hierbij."),
            ("kader", tabel(["begrip", "wat het betekent"],
                            [["<strong>objectpermanentie</strong>", "<strong>iets bestaat ook als je het niet ziet</strong>: een baby van acht maanden zoekt een bal die onder een doek verdwijnt"],
                             ["<strong>persoonspermanentie</strong>", "<strong>mama bestaat ook als ze weg is</strong>: een vertrouwd persoon blijft bestaan als die de kamer uit gaat"],
                             ["<strong>intentioneel handelen</strong>", "<strong>met een doel handelen</strong>: de baby schuift een kussen weg om bij zijn speeltje te komen"]])),
            ("p", "<strong>Objectpermanentie ontstaat in het sensomotorische stadium</strong>, in het eerste "
                  "levensjaar. Abstract denken komt pas veel later, in het formeel-operationele stadium."),
        ]),
        dict(kop="De kleuter: het pre-operationele stadium", blokken=[
            ("p", "<strong>Een peuter of kleuter zit in het pre-operationele stadium</strong>, met "
                  "<strong>symbolisch denken, veel fantasie en typische denkfouten</strong>. "
                  "<strong>Symbolisch denken is dat een stok een zwaard wordt</strong>: het kind laat het "
                  "ene ding voor het andere staan, en daar komt het doen-alsof-spel uit. <strong>Logisch "
                  "en abstract denken kan een kleuter nog niet.</strong>"),
            ("kader", tabel(["denkfout", "wat je ziet"],
                            [["<strong>animisme</strong>", "<strong>dingen hebben gevoelens</strong>: de pop heeft pijn, de stoel is stout"],
                             ["<strong>magisch denken</strong>", "het kind denkt dat zijn wens of zijn gedachte iets kan doen gebeuren"],
                             ["<strong>egocentrisme</strong>", "<strong>enkel zijn eigen kijk</strong>: het denkt dat iedereen ziet en voelt wat het zelf ziet en voelt. Dat is geen egoïsme"],
                             ["<strong>centratie</strong>", "<strong>op één kenmerk letten</strong>: het ziet alleen dat het glas hoger is, niet dat het ook smaller is"],
                             ["<strong>niet-reversibel denken</strong>", "het kan een handeling in gedachten nog <strong>niet</strong> terugdraaien"]])),
        ]),
        dict(kop="Het lagereschoolkind: het concreet-operationele stadium", blokken=[
            ("p", "<strong>Een lagereschoolkind denkt logisch, maar nog over dingen die het kan zien of "
                  "vastnemen.</strong> Dat is <strong>concreet denken</strong>: het rekent met blokjes of "
                  "met geld, niet met een letter in een formule."),
            ("kader", tabel(["wat erbij komt", "wat het betekent"],
                            [["<strong>seriatie</strong>", "<strong>op grootte ordenen</strong>: stokjes van klein naar groot leggen"],
                             ["<strong>classificatie</strong>", "<strong>in groepen indelen</strong>: alle rode blokken bij elkaar, alle blauwe apart"],
                             ["<strong>de conservatienotie</strong>", "<strong>de hoeveelheid blijft gelijk</strong>: giet je water in een smaller glas, dan blijft het evenveel water"],
                             ["<strong>decentreren</strong>", "<strong>ook de andere kant zien</strong>: op meer dan één kenmerk letten"],
                             ["<strong>reversibel denken</strong>", "<strong>in twee richtingen denken</strong>: wie drie plus vier kan, kan ook zeven min vier"],
                             ["<strong>systematisch denken</strong>", "stap voor stap te werk gaan"]])),
            ("p", "<strong>Een kleuter begrijpt de conservatienotie nog niet</strong>, net door de centratie: "
                  "hij ziet alleen dat het glas hoger is, niet dat het ook smaller is."),
        ]),
        dict(kop="De adolescent en de taal", blokken=[
            ("p", "<strong>Een adolescent zit in het formeel-operationele stadium</strong> en kan "
                  "<strong>abstract denken, logisch redeneren, hypothetisch denken en experimenteel "
                  "denken</strong>. <strong>Hypothetisch denken is denken in wat als</strong>: nadenken over "
                  "iets dat nog niet bestaat of niet zo is."),
            ("p", "De taal volgt zijn eigen weg van nul tot drie jaar: <strong>eerst huilen en brabbelen, "
                  "dan losse woorden, dan korte zinnen.</strong> <strong>Het eerste woordje komt meestal rond "
                  "één jaar</strong>, rond de eerste verjaardag. Rond twee jaar komen de tweewoordzinnen, "
                  "dus <strong>een kind van twee spreekt nog niet in volledige zinnen</strong>."),
        ]),
    ])


# ───────────────────────── 6. Kohlberg en Erikson
zet("kohlberg-en-erikson",
    titel="Kohlberg en Erikson",
    onder="De drie stadia van de morele ontwikkeling bij Kohlberg, en de acht conflicten met hun krachten bij Erikson.",
    secties=[
        dict(kop="Kohlberg: de morele ontwikkeling", blokken=[
            ("p", "<strong>Kohlberg beschrijft de morele ontwikkeling</strong>: hoe iemand leert bepalen "
                  "wat juist en wat verkeerd is. <strong>Hij onderscheidt drie stadia.</strong> Het "
                  "operationele stadium komt van Piaget, niet van Kohlberg."),
            ("fig", svg.ladder([("post-conventioneel", "eigen waarden wegen het zwaarst"),
                                ("conventioneel", "de regels en de groep tellen"),
                                ("pre-conventioneel", "straf en beloning tellen")],
                               bovenaan="het laatst", onderaan="het eerst")),
            ("kader", tabel(["stadium", "wat telt", "voorbeeld"],
                            [["<strong>het pre-conventionele</strong>", "<strong>straf, beloning en het eigen voordeel</strong>", "<strong>een kind doet iets niet omdat het straf krijgt</strong>"],
                             ["<strong>het conventionele</strong>", "<strong>de regels, de wet en wat anderen van je vinden</strong>", "<strong>iemand houdt zich aan de wet omdat het de wet is</strong>"],
                             ["<strong>het post-conventionele</strong>", "<strong>eigen waarden</strong> als rechtvaardigheid en menselijkheid, en de mensenrechten", "<strong>iemand overtreedt een regel omdat die onrechtvaardig is</strong>"]])),
            ("p", "<strong>Een jong kind zit meestal in het pre-conventionele stadium</strong> en kijkt "
                  "vooral naar de gevolgen voor zichzelf; <strong>het denkt dus nog niet aan de wet</strong>. "
                  "<strong>Niet iedereen bereikt het post-conventionele stadium</strong>: volgens Kohlberg "
                  "blijven veel mensen in het conventionele."),
        ]),
        dict(kop="Erikson: de persoonlijkheidsontwikkeling", blokken=[
            ("p", "<strong>Erikson beschrijft de persoonlijkheidsontwikkeling</strong>, met <strong>bij "
                  "elke levensfase een conflict</strong> van twee polen. <strong>Raakt het conflict "
                  "opgelost, dan komt de kracht van die fase vrij</strong>, gaat het kind verder en wordt de "
                  "volgende stap mogelijk. <strong>Wat niet opgelost raakt, speelt in de volgende fasen "
                  "mee.</strong>"),
            ("kader", tabel(["fase", "het conflict", "de kracht"],
                            [["<strong>de baby</strong>", "<strong>vertrouwen tegenover wantrouwen</strong>", "<strong>hoop</strong>"],
                             ["<strong>de peuter</strong>", "<strong>autonomie tegenover twijfel</strong> en schaamte", "<strong>de wil</strong>"],
                             ["<strong>de kleuter</strong>", "<strong>initiatief tegenover schuld</strong>", "<strong>doelgerichtheid</strong>"],
                             ["<strong>het lagereschoolkind</strong>", "<strong>handvaardigheid tegenover minderwaardigheid</strong>", "competentie"],
                             ["<strong>de adolescent</strong>", "<strong>identiteit tegenover identiteitsverwarring</strong>", "<strong>trouw</strong>"],
                             ["<strong>de vroege volwassene</strong>", "<strong>intimiteit tegenover isolatie</strong>", "<strong>de liefde</strong>"],
                             ["<strong>de midden-volwassene</strong>", "<strong>generativiteit tegenover stagnatie</strong>", "zorg"],
                             ["<strong>de oudere</strong>", "<strong>integriteit tegenover wanhoop</strong>", "<strong>wijsheid</strong>"]])),
            ("p", "<strong>Hoop</strong> is het vertrouwen dat het goed komt. <strong>De wil</strong> is zelf "
                  "willen en zelf kunnen. <strong>Trouw</strong> is weten wie je bent en daarbij blijven. "
                  "<strong>Liefde</strong> is een band aangaan zonder jezelf te verliezen."),
            ("p", "<strong>Generativiteit is iets doorgeven aan anderen</strong>: zorgen voor de volgende "
                  "generatie, op het werk of in het gezin. <strong>Het betekent dus net niet dat je alleen "
                  "aan jezelf denkt</strong>; dat is stagnatie, de andere pool."),
        ]),
    ])


# ───────────────────────── 7. De socio-emotionele ontwikkeling
zet("de-socio-emotionele-ontwikkeling",
    titel="De socio-emotionele ontwikkeling",
    onder="De zeven soorten spel, de peergroep en de groepsdruk, de vormen van gehechtheid, scheidingsangst en angst voor vreemden, en wat sensitieve responsiviteit is.",
    secties=[
        dict(kop="De soorten spel", blokken=[
            ("p", "Hoe een kind speelt, zegt veel over zijn sociale ontwikkeling. Van alleen spelen groeit "
                  "het naar echt samenspelen."),
            ("kader", tabel(["soort spel", "wat je ziet"],
                            [["<strong>solitair spel</strong> of solospel", "<strong>alleen spelen</strong>, zonder de anderen nodig te hebben. <strong>Dit hoort bij een baby.</strong>"],
                             ["<strong>toekijkend spel</strong>", "<strong>kijken naar anderen</strong> die spelen, en zelf nog niet meedoen"],
                             ["<strong>parallel spel</strong>", "<strong>naast elkaar spelen</strong>: twee peuters bouwen met blokken, elk aan zijn eigen toren"],
                             ["<strong>associatief spel</strong>", "met elkaar bezig zijn zonder dat er al één doel is"],
                             ["<strong>samenspel</strong>", "echt samen spelen. <strong>Vanaf de lagere school met regels en afspraken.</strong>"],
                             ["<strong>coöperatief spel</strong>", "<strong>samen naar een doel</strong>: de kinderen verdelen rollen en werken aan hetzelfde"],
                             ["<strong>doen-alsof-spel</strong>", "<strong>de stoel is een auto</strong>; het komt uit het symbolisch denken van de kleuter"]])),
            ("p", "<strong>Bij parallel spel werken kinderen dus niet samen aan één bouwwerk</strong>: ze "
                  "spelen naast elkaar, elk aan hun eigen ding."),
        ]),
        dict(kop="Vrienden en de peergroep", blokken=[
            ("p", "<strong>Vriendschappen zijn belangrijk omdat kinderen er leren samenleven, ruzie maken "
                  "en goedmaken.</strong> Ze leren er ook delen en voor zichzelf opkomen. "
                  "<strong>Vriendschappen zijn een van de belangrijkste motoren van de sociale "
                  "ontwikkeling</strong>, niet iets dat er los naast staat."),
            ("p", "<strong>Een peergroep is een groep leeftijdsgenoten</strong> uit de klas, de club of de "
                  "buurt, waarmee een tiener zich vergelijkt. <strong>De peergroep bepaalt mee zijn "
                  "gedrag</strong>: kleding, taal, muziek en keuzes worden in de adolescentie sterk door de "
                  "groep gestuurd."),
            ("kader", tabel(["soort groepsdruk", "wat het is"],
                            [["<strong>directe groepsdruk</strong>", "iemand zegt het met zoveel woorden: doe mee"],
                             ["<strong>indirecte groepsdruk</strong>", "niemand zegt iets, maar je voelt wat er verwacht wordt"],
                             ["<strong>positieve groepsdruk</strong>", "<strong>de groep trekt je mee</strong> in gezond of verstandig gedrag: een ploeg waar iedereen studeert of sport"],
                             ["<strong>negatieve groepsdruk</strong>", "de groep trekt je mee in iets wat je eigenlijk niet wil"]])),
            ("p", "<strong>Groepsdruk kan dus ook positief zijn.</strong> Het is niet per se iets slechts."),
        ]),
        dict(kop="Gehechtheid", blokken=[
            ("p", "<strong>Gehechtheid is de veilige band tussen een kind en zijn vaste zorgfiguur.</strong> "
                  "<strong>Een baby bouwt zijn eerste band met wie dagelijks voor hem zorgt.</strong>"),
            ("kader", tabel(["hechtingspatroon", "wat je ziet"],
                            [["<strong>veilige hechting</strong>", "<strong>het kind durft op verkenning, zoekt troost bij angst en keert terug naar zijn basis</strong>"],
                             ["<strong>angstig-vermijdend</strong>", "<strong>het kind zoekt geen troost</strong>; het lijkt onverschillig en vraagt geen hulp, ook al heeft het die nodig"],
                             ["<strong>angstig-ambivalent</strong>", "<strong>het kind twijfelt en klampt</strong>: het zoekt troost en duwt die tegelijk weg"],
                             ["<strong>gedesorganiseerd en gedesoriënteerd</strong>", "het kind weet helemaal niet waar het terecht kan"]])),
            ("p", "<strong>Een veilig gehecht kind durft juist méér op verkenning</strong>, niet minder: "
                  "omdat het weet dat zijn ouder er is, durft het verder weg. <strong>Bij angst zoekt het "
                  "zijn ouder op</strong>, want die is de veilige basis."),
        ]),
        dict(kop="Scheidingsangst en sensitieve responsiviteit", blokken=[
            ("p", "<strong>Scheidingsangst is de angst van een kind als zijn ouder weggaat.</strong> Rond "
                  "het eerste jaar protesteert een baby als zijn vertrouwde figuur verdwijnt. <strong>Angst "
                  "voor vreemden betekent dat het kind huilt bij onbekenden</strong>, en die "
                  "<strong>begint meestal rond acht maanden</strong>, net wanneer de hechting goed op gang "
                  "komt."),
            ("p", "<strong>Die twee angsten zijn niet slecht: ze horen erbij.</strong> Ze zijn net een "
                  "<strong>gevolg van een veilige hechting</strong>, want het kind weet wie zijn mensen "
                  "zijn. Scheidingsangst is dus een teken van gehechtheid, en angst voor vreemden is een "
                  "normale stap in de ontwikkeling."),
            ("p", "<strong>Sensitieve responsiviteit is de signalen van een baby zien, ze juist begrijpen en "
                  "er snel op ingaan.</strong> Laten huilen is net het omgekeerde. <strong>Het is belangrijk "
                  "omdat het vertrouwen bouwt</strong>: een baby die merkt dat er altijd iemand reageert, "
                  "bouwt een veilige hechting op."),
        ]),
    ])


# ───────────────────────── 8. De volwassene en de oudere
zet("de-volwassene-en-de-oudere",
    titel="De volwassene en de oudere",
    onder="Uiterlijke en inwendige veroudering, primair en secundair verouderen, wat er met de hersenen gebeurt, het verschil tussen vergeetachtigheid en dementie, en de levensgebeurtenissen van de volwassene en de oudere.",
    secties=[
        dict(kop="Verouderen", blokken=[
            ("p", "<strong>Uiterlijke veroudering zie je</strong>: rimpels, grijze haren en een krommere "
                  "rug. <strong>Inwendige veroudering betekent dat de organen minder werken</strong>: hart, "
                  "longen, nieren en spijsvertering gaan langzaam achteruit. <strong>Verouderen begint al "
                  "bij de jonge volwassene</strong>, alleen merk je er dan weinig van."),
            ("kader", tabel(["soort", "wat het is"],
                            [["<strong>primair verouderen</strong>", "<strong>het gebeurt bij iedereen</strong>: het natuurlijke verouderen dat niemand ontloopt"],
                             ["<strong>secundair verouderen</strong>", "<strong>het komt door de leefstijl</strong>, door ziekte en door de omgeving, en is deels te vermijden"]])),
            ("p", "<strong>De bewegingen worden trager</strong> bij een oudere: minder kracht en een minder "
                  "zeker evenwicht horen bij de ouderdomsmotoriek. Ook het zicht, het gehoor en de "
                  "spierkracht gaan achteruit."),
        ]),
        dict(kop="De hersenen van een oudere", blokken=[
            ("p", "Ouder worden brengt niet alleen achteruitgang mee. Bij de hersenen gaat er iets weg en "
                  "komt er iets bij."),
            ("kader", tabel(["wat afneemt", "wat toeneemt"],
                            [["<strong>de snelheid van denken</strong>", "<strong>het overzicht</strong>"],
                             ["", "<strong>de woordenschat</strong>"],
                             ["", "<strong>de levenswijsheid</strong>"]])),
            ("p", "<strong>Een oudere denkt dus trager, maar weet meer en overziet beter.</strong> Daarom "
                  "<strong>werkt hij trager en toch vaak even goed</strong>: wat aan tempo verloren gaat, "
                  "wordt opgevangen door ervaring en overzicht."),
            ("kader", tabel(["", "wat het is", "hindert het het dagelijkse leven?"],
                            [["<strong>ouderdomsvergeetachtigheid</strong>", "<strong>je vindt een woord of een naam even niet</strong>", "<strong>nee</strong>"],
                             ["<strong>dementie</strong>", "<strong>de hersenen gaan blijvend achteruit</strong>", "<strong>ja</strong>"]])),
            ("p", "<strong>Vergeetachtigheid en dementie zijn dus niet hetzelfde</strong>: het verschil is "
                  "net dat <strong>dementie verder gaat</strong> en wel ingrijpt in het dagelijkse leven."),
        ]),
        dict(kop="Levensgebeurtenissen van de volwassene", blokken=[
            ("kader", tabel(["gebeurtenis", "wat het is"],
                            [["<strong>gezinsvorming</strong>", "<strong>een eigen gezin starten</strong>: samenwonen, trouwen of kinderen krijgen"],
                             ["<strong>de midlifecrisis</strong>", "<strong>twijfel rond de middenleeftijd</strong>: rond de veertig of vijftig stelt iemand zijn werk, relatie en keuzes in vraag"],
                             ["<strong>het legenestsyndroom</strong>", "<strong>de kinderen gaan weg</strong>, en ouders voelen het gemis en de leegte"],
                             ["<strong>boemerangkinderen</strong>", "<strong>kinderen die terugkomen</strong>: ze waren het huis uit en komen weer bij hun ouders wonen"],
                             ["<strong>de sandwichgeneratie</strong>", "<strong>zorg voor twee generaties</strong>: tegelijk voor de eigen kinderen en voor de ouder wordende ouders"]])),
            ("p", "<strong>Het legenestsyndroom betekent dus niet dat de kinderen terugkeren</strong>; dat "
                  "zijn boemerangkinderen. <strong>Langdurige stress maakt een volwassene ziek</strong>: "
                  "slecht slapen, hoofdpijn en een opgebrand gevoel."),
        ]),
        dict(kop="Levensgebeurtenissen van de oudere", blokken=[
            ("p", "<strong>Bij de oudere horen de pensionering, de eenzaamheid en de kleinkinderen.</strong> "
                  "Gezinsvorming hoort bij de volwassene."),
            ("p", "<strong>Bij een pensionering valt de dagindeling weg.</strong> Het vaste ritme van het "
                  "werk verdwijnt en moet opnieuw opgebouwd worden. <strong>Een oudere voelt zich soms "
                  "eenzaam omdat vrienden wegvallen</strong>: collega's, vrienden en soms een partner, "
                  "waardoor de wereld kleiner wordt."),
            ("p", "<strong>Afhankelijk worden betekent dat een oudere hulp nodig heeft</strong> voor wassen, "
                  "koken of boodschappen. <strong>Rouw is het verdriet na een verlies</strong>, en dat "
                  "verwerken <strong>gaat bij iedereen anders</strong>, in tempo en in vorm."),
            ("p", "<strong>Bij een verhuis naar een woonzorgcentrum helpt het om eigen spullen mee te nemen, "
                  "mee te mogen beslissen en bezoek te krijgen.</strong> Dat maakt de stap draaglijker."),
        ]),
    ])


# ───────────────────────── 9. Waarnemen en observeren
zet("waarnemen-en-observeren",
    titel="Waarnemen en observeren",
    onder="Het verschil tussen waarnemen en observeren, wat je waarneming kleurt, de valkuilen bij het observeren, de criteria van een goede observatie, en de soorten observatie.",
    secties=[
        dict(kop="Waarnemen tegenover observeren", blokken=[
            ("p", "<strong>Waarnemen is informatie opnemen</strong>: wat je zintuigen binnenbrengen, zonder "
                  "dat je er iets voor doet. <strong>Observeren is doelgericht waarnemen</strong>: je weet "
                  "vooraf waarom en waarop je kijkt, en je doet het systematisch. <strong>Dat is het "
                  "verschil</strong>: waarnemen gebeurt zomaar, observeren met een doel."),
            ("p", "<strong>Je waarnemen wordt beïnvloed door je zintuigen, je lichaam en je psyche</strong>: "
                  "zintuiglijke, fysiologische en psychologische factoren samen bepalen wat je opmerkt."),
            ("kader", tabel(["begrip", "wat het betekent"],
                            [["<strong>de drempelwaarde</strong>", "<strong>de prikkel moet sterk genoeg zijn</strong>: eronder merk je hem niet op, erboven wel"],
                             ["<strong>gewenning</strong>", "<strong>je merkt de prikkel niet meer</strong>: het tikken van een klok hoor je na vijf minuten niet meer"],
                             ["<strong>contrast</strong>", "<strong>een groot verschil valt op</strong>: één kind in een rode trui tussen twintig blauwe truien zie je meteen"]])),
            ("p", "<strong>Bij het observeren spelen ook aandacht, voorkennis en emoties mee.</strong> "
                  "Emoties <strong>kleuren wat je ziet, sturen je aandacht en maken je minder streng</strong>: "
                  "wie zelf moe of geïrriteerd is, ziet ander gedrag dan wie uitgeslapen is."),
        ]),
        dict(kop="De valkuilen", blokken=[
            ("kader", tabel(["valkuil", "wat er misgaat"],
                            [["<strong>de attributiefout</strong>", "<strong>je legt de oorzaak fout</strong>: je schrijft gedrag toe aan de persoon terwijl de situatie de oorzaak is"],
                             ["<strong>het verwachtingspatroon</strong>", "<strong>je ziet wat je verwacht</strong>: wie een kind druk vindt, ziet vooral de drukke momenten"],
                             ["<strong>de veralgemening</strong>", "<strong>een besluit over iedereen</strong>: uit één voorval een besluit trekken over een hele groep"],
                             ["<strong>het individueel referentiekader</strong>", "<strong>je eigen bril op de wereld</strong>: je opvoeding, cultuur en ervaringen bepalen mee hoe je gedrag leest"]])),
            ("p", "<strong>Een veralgemening is dus geen betrouwbaar besluit</strong>, en <strong>je eigen "
                  "ervaringen hebben wel degelijk invloed</strong> op wat je ziet. <strong>Je beperkt de "
                  "invloed van je eigen kader door bij de feiten te blijven</strong>: noteer wat je ziet en "
                  "hoort, niet wat je ervan denkt."),
        ]),
        dict(kop="Een goede observatie", blokken=[
            ("p", "<strong>Een goede observatie is doelgericht, objectief, nauwkeurig, opnieuw uitvoerbaar "
                  "en representatief.</strong> Vijf criteria dus."),
            ("kader", tabel(["criterium", "wat het vraagt"],
                            [["<strong>doelgericht</strong>", "je weet vooraf waarom je kijkt"],
                             ["<strong>objectief</strong>", "<strong>je noteert enkel feiten, je laat je mening weg en je schrijft gedrag op</strong>: niet \"hij was boos\" maar \"hij duwde zijn stoel weg en zweeg\""],
                             ["<strong>nauwkeurig en controleerbaar</strong>", "<strong>iemand anders kan het nakijken</strong> en volgen"],
                             ["<strong>opnieuw uitvoerbaar</strong>", "een collega kan dezelfde observatie overdoen"],
                             ["<strong>representatief</strong>", "<strong>het beeld is typisch</strong>: één uitzonderlijke dag geeft geen beeld van hoe een kind meestal is"]])),
        ]),
        dict(kop="De soorten observatie", blokken=[
            ("kader", tabel(["soort", "wat het betekent"],
                            [["<strong>bedekt</strong> of verdoken", "<strong>de persoon weet het niet</strong>"],
                             ["<strong>niet-bedekt</strong>", "<strong>de persoon is op de hoogte</strong>, en dat kan zijn gedrag beïnvloeden"],
                             ["<strong>gesloten</strong>", "<strong>je weet waarop je let</strong>: één afgebakend punt, meestal met een schema"],
                             ["<strong>open</strong>", "<strong>je noteert alles wat opvalt</strong>, zonder iets vooraf vast te leggen"],
                             ["<strong>participerend</strong>", "<strong>je doet zelf mee, je zit in de groep, je speelt mee</strong>"],
                             ["<strong>niet-participerend</strong>", "je kijkt van een afstand toe"],
                             ["<strong>in een natuurlijke omgeving</strong>", "<strong>de gewone omgeving</strong>: de klas, de leefgroep of thuis"]])),
            ("p", "Pas op bij het woord bedekt: <strong>bij een bedekte observatie weet de persoon juist "
                  "niet dat hij geobserveerd wordt.</strong>"),
            ("p", "<strong>Een observatieschema is een lijst om aan te duiden</strong>, met vooraf bepaalde "
                  "punten die je aanduidt of scoort. <strong>Een observatieverslag is een tekst met je "
                  "bevindingen</strong>, waarin je in woorden beschrijft wat je gezien en gehoord hebt. "
                  "<strong>Een schema kies je dus pas als je weet waarop je let</strong>; heb je nog geen "
                  "doel, dan werk je open."),
        ]),
    ])


# ───────────────────────── 10. Rapporteren en respectvol omgaan
zet("rapporteren-en-respectvol-omgaan",
    titel="Rapporteren en respectvol omgaan",
    onder="De soorten rapportering, wat wel en niet in een rapport hoort, waarden en normen, en respectvol omgaan met privacy, diversiteit en gevoelige onderwerpen.",
    secties=[
        dict(kop="Rapporteren", blokken=[
            ("p", "Wat je observeert, moet ergens terechtkomen. Dat heet rapporteren, en het kan op "
                  "<strong>twee assen</strong>: mondeling of schriftelijk, en intern of extern."),
            ("kader", tabel(["soort", "wat het is"],
                            [["<strong>mondeling</strong>", "<strong>je vertelt het door</strong>, in een overleg of een overdracht"],
                             ["<strong>schriftelijk</strong>", "<strong>je legt het vast op papier</strong> of digitaal"],
                             ["<strong>intern</strong>", "<strong>het blijft binnen de werking, voor de collega's</strong>, en het kan ook mondeling"],
                             ["<strong>extern</strong>", "<strong>naar iemand buiten de dienst</strong>: ouders, een arts, een CLB of een andere dienst"]])),
            ("p", "<strong>Schriftelijk rapporteren is belangrijk omdat het blijft bestaan</strong>: wat op "
                  "papier staat, kan later nagelezen en opgevolgd worden."),
            ("kader", tabel(["hoort wel in een rapport", "hoort er niet in"],
                            [["<strong>de feiten</strong>", "<strong>je eigen oordeel of mening</strong>"],
                             ["<strong>de datum</strong>", ""],
                             ["<strong>wie erbij was</strong>", ""]])),
            ("p", "Wat, wanneer en wie: zo is het rapport controleerbaar. <strong>In een rapport schrijf je "
                  "dus niet vooral je eigen mening</strong>, maar wat er feitelijk gebeurd is."),
        ]),
        dict(kop="Waarden en normen", blokken=[
            ("p", "<strong>Waarden zijn wat je belangrijk vindt</strong>: eerlijkheid, respect of vrijheid. "
                  "<strong>Normen zijn de regels voor je gedrag</strong>, bijvoorbeeld dat je niet liegt. "
                  "<strong>Normen komen uit waarden voort</strong>: uit de waarde eerlijkheid volgt de norm "
                  "dat je niet liegt."),
            ("p", "<strong>Waarden verschillen van gezin tot gezin door cultuur en opvoeding.</strong> "
                  "Cultuur, geloof, opvoeding en ervaring bepalen mee wat belangrijk is, dus "
                  "<strong>waarden zijn niet voor iedereen hetzelfde</strong>. <strong>Zijn de waarden van "
                  "een gezin anders dan de jouwe, dan blijf je respectvol</strong>: je hoeft het niet eens "
                  "te zijn, maar je gaat respectvol met het verschil om."),
        ]),
        dict(kop="Respectvol omgaan", blokken=[
            ("p", "<strong>Respectvol omgaan met iemand betekent dat je hem laat uitspreken, hem ernstig "
                  "neemt en zijn mening vraagt.</strong> <strong>Openstaan voor diversiteit betekent dat "
                  "verschillen er mogen zijn</strong>: taal, geloof, gezinsvorm en mogelijkheden horen erbij "
                  "en krijgen plaats."),
            ("p", "<strong>Een gevoelig onderwerp</strong> is bijvoorbeeld een scheiding thuis, ziekte, geld "
                  "of een overlijden. <strong>Je gaat er voorzichtig op in</strong>, in je eigen woorden, en "
                  "je dringt niet aan. <strong>Je vermijdt ze dus niet helemaal</strong>, want dan doe je "
                  "alsof ze er niet zijn."),
            ("p", "<strong>De emoties van een kind benoem je.</strong> \"Ik zie dat je verdrietig bent\" "
                  "geeft het kind het gevoel dat het gezien wordt."),
            ("kader", tabel(["begrip", "wat het betekent"],
                            [["<strong>privacy</strong>", "<strong>gegevens blijven binnen</strong>: wat je over een kind of een gezin weet, blijft bij wie het nodig heeft"],
                             ["<strong>het beroepsgeheim</strong> of de zwijgplicht", "<strong>je zwijgt over wat je weet</strong> door je werk"],
                             ["<strong>een vooroordeel</strong>", "<strong>een mening zonder kennis</strong>: je oordeelt over iemand voordat je hem kent"]])),
            ("p", "<strong>Je deelt informatie over een kind enkel met wie die echt nodig heeft</strong> om "
                  "goed te kunnen zorgen. <strong>Met je eigen vooroordeel ga je om door het bij jezelf na "
                  "te gaan</strong>: iedereen heeft vooroordelen, het verschil zit in of je ze onderzoekt."),
            ("p", "<strong>Een veilige sfeer in een groep betekent dat iedereen mag meedoen, niemand "
                  "uitgelachen wordt en de afspraken duidelijk zijn.</strong> <strong>Afspraken geven "
                  "duidelijkheid</strong>, en wie weet wat mag en wat niet, voelt zich veiliger. "
                  "<strong>Opbouwend omgaan betekent dat je naar wat kan kijkt, de sterktes benoemt en "
                  "samen een weg zoekt</strong>, niet dat je de fouten opsomt."),
        ]),
    ])


# ───────────────────────── 11. Gedrag en behoeften
zet("gedrag-en-behoeften",
    titel="Gedrag en behoeften",
    onder="De soorten gedrag en wat het beïnvloedt, wat achter moeilijk gedrag zit, de behoeftepiramide van Maslow, en de zes basisbehoeften van Kind en Gezin.",
    secties=[
        dict(kop="Wat gedrag is", blokken=[
            ("p", "<strong>Gedrag is alles wat een mens doet, zegt, denkt en voelt.</strong> Denken en voelen "
                  "horen er dus ook bij, ook al zie je ze niet."),
            ("kader", tabel(["soort gedrag", "wat het is"],
                            [["<strong>waarneembaar gedrag</strong>", "<strong>je kan het zien</strong>: lopen, praten, lachen, wegduwen"],
                             ["<strong>niet-waarneembaar gedrag</strong>", "<strong>denken en voelen</strong>, en willen; je ziet het niet en toch is het gedrag"],
                             ["<strong>reflexmatig gedrag</strong>", "<strong>het gaat automatisch</strong>: je hand wegtrekken van een hete pan"]])),
            ("p", "<strong>Reflexmatig gedrag kies je dus niet zelf</strong>: het gebeurt zonder dat je erover "
                  "nadenkt."),
        ]),
        dict(kop="Wat gedrag beïnvloedt", blokken=[
            ("p", "<strong>Gedrag wordt beïnvloed door biologische, psychologische, cognitieve en sociale "
                  "factoren</strong> samen."),
            ("kader", tabel(["factor", "voorbeeld"],
                            [["<strong>biologisch</strong>", "<strong>honger of moeheid</strong>, en ook dorst, pijn of ziekte"],
                             ["<strong>psychologisch</strong>", "je gevoelens, je karakter, je zelfvertrouwen"],
                             ["<strong>cognitief</strong>", "<strong>wat je denkt en weet</strong>: je kennis en wat je van een situatie begrijpt"],
                             ["<strong>sociaal</strong>", "<strong>de mening van de groep</strong>, en wat het gezin of de cultuur verwacht"]])),
            ("p", "<strong>Twee kinderen reageren anders op hetzelfde omdat hun factoren verschillen</strong>: "
                  "elk kind brengt een ander lichaam, een andere ervaring en een andere omgeving mee. "
                  "<strong>Honger kan het gedrag van een kind dus echt veranderen.</strong>"),
            ("p", "<strong>Stelt een kind moeilijk gedrag, dan zoek je eerst de oorzaak.</strong> Gedrag is "
                  "een signaal: eerst kijken wat eronder zit, dan pas handelen. <strong>Achter moeilijk "
                  "gedrag zit vaak een behoefte die niet vervuld is</strong>: honger, moeheid, angst of te "
                  "weinig aandacht komen er als gedrag uit."),
            ("p", "<strong>Een behoefte is iets wat je nodig hebt</strong>, en dat is niet hetzelfde als een "
                  "wens: een behoefte is noodzakelijk, een wens is iets wat leuk zou zijn."),
        ]),
        dict(kop="De behoeftepiramide van Maslow", blokken=[
            ("p", "<strong>Maslow maakte de behoeftepiramide</strong> en ordende daarin de behoeften van de "
                  "mens. <strong>De onderste komt eerst</strong>: pas als de lagere behoeften vervuld zijn, "
                  "komen de hogere aan de beurt."),
            ("fig", svg.standenpiramide([("zelfactualisatie", "worden wie je ten volle kan zijn"),
                                         ("erkenning", "gewaardeerd worden om wie je bent"),
                                         ("sociaal contact", "ergens bij horen, vrienden hebben"),
                                         ("zekerheid", "veiligheid, een dak, een vast ritme"),
                                         ("fysieke behoeften", "eten, drinken, slapen, warmte")])),
            ("p", "<strong>De fysieke behoeften staan onderaan</strong> en <strong>de zelfactualisatie "
                  "bovenaan</strong>. <strong>Zelfactualisatie of zelfontplooiing is worden wie je kan zijn, je "
                  "talenten gebruiken en jezelf ontplooien.</strong>"),
            ("p", "<strong>Een hongerig kind kan niet goed leren omdat de fysieke behoefte voorgaat.</strong> "
                  "De onderste laag van de piramide eist eerst aandacht, dus het leert niet even goed als "
                  "een ander."),
        ]),
        dict(kop="De zes basisbehoeften van Kind en Gezin", blokken=[
            ("kader", tabel(["basisbehoefte", "wat het kind nodig heeft"],
                            [["<strong>de lichamelijke behoeften</strong>", "eten, drinken, slapen, verzorging"],
                             ["<strong>affectie</strong>", "<strong>warmte en liefde krijgen</strong>: knuffels en nabijheid"],
                             ["<strong>veiligheid</strong>", "<strong>duidelijkheid en continuïteit</strong>: vaste mensen, vaste afspraken"],
                             ["<strong>erkenning</strong>", "gezien en bevestigd worden om wie het is"],
                             ["<strong>zichzelf als kundig ervaren</strong>", "<strong>het kind voelt dat het iets kan</strong>: zijn jas dichtdoen, een toren bouwen"],
                             ["<strong>zingeving</strong>", "<strong>weten waarom iets telt</strong>: zin en morele waarden"]])),
            ("p", "<strong>Affectie betekent warmte en liefde, geen regels en grenzen</strong>; die horen bij "
                  "veiligheid en duidelijkheid. <strong>Je helpt een kind zichzelf als kundig te voelen door "
                  "het zelf te laten proberen</strong>, met hulp in de buurt."),
        ]),
    ])


# ───────────────────────── 12. Communiceren en actief luisteren
zet("communiceren-en-actief-luisteren",
    titel="Communiceren en actief luisteren",
    onder="Verbale en non-verbale communicatie, de fasen van een gesprek, praten met een kind en met een oudere, de drie manieren van luisteren en de LSD-methode.",
    secties=[
        dict(kop="Verbaal en non-verbaal", blokken=[
            ("p", "<strong>Verbale communicatie zijn de woorden die je zegt</strong> of schrijft. "
                  "<strong>Non-verbale communicatie is alles behalve de woorden zelf</strong>: je "
                  "<strong>lichaamshouding, je gezichtsuitdrukking, je stemtoon</strong>, je gebaren en de "
                  "afstand die je houdt. <strong>Gebaren zijn dus non-verbaal</strong>, geen verbale "
                  "communicatie."),
            ("p", "<strong>Lichaamstaal is belangrijk omdat ze vaak meer zegt dan woorden.</strong> Een kind "
                  "dat zegt dat het goed gaat maar met gebogen hoofd zit, vertelt iets anders. <strong>Gaan "
                  "woorden en lichaamstaal niet samen, dan vraag je ernaar</strong>: \"Je zegt dat het goed "
                  "gaat, maar je kijkt verdrietig. Klopt dat?\""),
        ]),
        dict(kop="De fasen van een gesprek", blokken=[
            ("fig", svg.stappen(["groeten", "jezelf|voorstellen", "kennismaken", "het dagelijkse|gesprek",
                                 "afscheid|nemen"])),
            ("p", "<strong>Je begint een gesprek met groeten</strong>, en dat is meteen de eerste indruk. "
                  "<strong>Kennismaken is elkaar leren kennen</strong>: je vraagt en vertelt om en om. "
                  "<strong>Je eindigt met afscheid nemen</strong>, want dat sluit het gesprek netjes af."),
            ("p", "<strong>Een respectvolle begroeting is goedendag zeggen, de ander aankijken en zijn naam "
                  "noemen.</strong> <strong>Oogcontact is de ander aankijken</strong>, en dat laat zien dat "
                  "je er echt bij bent. <strong>Het maakt een gesprek dus niet onbeleefd</strong>, "
                  "integendeel."),
            ("kader", tabel(["met wie", "hoe je het best praat"],
                            [["<strong>een jong kind</strong>", "<strong>korte zinnen op ooghoogte</strong>: zak door je knieën en kijk het kind aan"],
                             ["<strong>een oudere</strong>", "<strong>rustig en duidelijk</strong>: een rustig tempo, duidelijke woorden, en hem aankijken"],
                             ["<strong>een slechthorende oudere</strong>", "<strong>je kijkt hem aan</strong>, zodat hij kan meelezen op je lippen"]])),
        ]),
        dict(kop="Drie manieren van luisteren", blokken=[
            ("kader", tabel(["manier", "wat je doet"],
                            [["<strong>oppervlakkig luisteren</strong>", "<strong>je hoort het maar half</strong>: je hoort de klank, maar je neemt niet op wat gezegd wordt"],
                             ["<strong>inhoudelijk luisteren</strong>", "<strong>je volgt wat er gezegd wordt</strong>, maar je laat nog niet merken dat je luistert"],
                             ["<strong>actief luisteren</strong>", "<strong>je toont dat je luistert</strong>: je knikt, je vat samen en je vraagt door"]])),
            ("p", "<strong>Bij een actieve lichaamshouding draai je je naar de ander, knik je af en toe en "
                  "kijk je hem aan.</strong> Gekruiste armen lezen als afstand. <strong>Kleine "
                  "aanmoedigingen zijn een knikje, een \"hm\" of een \"ja\"</strong>: zo laat je merken dat "
                  "je nog mee bent."),
        ]),
        dict(kop="De LSD-methode", blokken=[
            ("p", "<strong>LSD staat voor Luisteren, Samenvatten en Doorvragen.</strong>"),
            ("fig", svg.stappen(["L|luisteren", "S|samenvatten", "D|doorvragen"])),
            ("kader", tabel(["letter", "wat je doet"],
                            [["<strong>de L</strong>", "<strong>je luistert actief</strong>, met je houding, je ogen en kleine aanmoedigingen"],
                             ["<strong>de S</strong>", "<strong>je vat samen</strong>: je herhaalt in je eigen woorden wat je begrepen hebt"],
                             ["<strong>de D</strong>", "<strong>je vraagt door</strong> met open vragen en gevoelsvragen"]])),
            ("p", "<strong>Je vat samen om na te gaan of je goed begreep</strong>: het geeft de ander de "
                  "kans om je recht te zetten."),
            ("p", "<strong>Een open vraag vraagt om meer uitleg</strong> en kan je dus <strong>niet</strong> "
                  "met ja of nee beantwoorden: \"Hoe was dat voor jou?\" levert meer op dan \"Was dat "
                  "leuk?\". <strong>Een gevoelsvraag peilt naar het gevoel</strong>: \"Hoe voelde je je "
                  "toen?\""),
            ("p", "<strong>Stiltes zijn nuttig omdat de ander tijd krijgt</strong> om verder te denken en te "
                  "spreken. <strong>Je vult ze dus niet meteen op.</strong>"),
        ]),
    ])


# ───────────────────────── 13. Feedback en verbindend communiceren
zet("feedback-en-verbindend-communiceren",
    titel="Feedback en verbindend communiceren",
    onder="Het 4G-model, de ik-boodschap, de vier stappen van verbindend communiceren, en herstelgericht werken.",
    secties=[
        dict(kop="Feedback geven", blokken=[
            ("p", "<strong>Feedback is zeggen wat je opvalt</strong>: je koppelt terug wat je ziet of merkt, "
                  "zodat de ander ermee verder kan. <strong>Ze kan positief of negatief zijn, en verbaal of "
                  "non-verbaal.</strong> <strong>Positieve feedback is benoemen wat goed gaat</strong>, en "
                  "dat werkt even sterk als zeggen wat beter kan. <strong>Feedback kan dus ook positief "
                  "zijn.</strong>"),
            ("p", "<strong>Het 4G-model heeft vier G's</strong>, en ze komen in deze volgorde."),
            ("fig", svg.stappen(["gedrag|wat je zag", "gevoel|wat het met je deed",
                                 "gevolg|wat er gebeurde", "gewenst gedrag|wat je anders wil"])),
            ("kader", tabel(["de G", "wat je zegt"],
                            [["<strong>de eerste G: gedrag</strong>", "<strong>je benoemt het gedrag dat je gezien hebt</strong>"],
                             ["<strong>de tweede G: gevoel</strong>", "<strong>wat dat gedrag bij jou teweegbracht</strong>"],
                             ["<strong>de derde G: gevolg</strong>", "<strong>wat er door dat gedrag gebeurd is</strong>"],
                             ["<strong>de vierde G: gewenst gedrag</strong>", "<strong>wat je graag anders zou zien</strong>"]])),
            ("p", "<strong>Feedback gaat over gedrag, nooit over wie iemand is.</strong>"),
            ("p", "<strong>Een ik-boodschap is een boodschap waarin je over jezelf spreekt</strong>: \"Ik "
                  "schrik als er geroepen wordt\" in plaats van \"Jij roept altijd\". <strong>Ze begint dus "
                  "met ik</strong>, niet met jij. <strong>Ze werkt beter omdat de ander zich veiliger "
                  "voelt</strong>: wie geen verwijt hoort, hoeft zich niet te verdedigen en kan luisteren."),
            ("p", "<strong>Krijg je zelf feedback, dan luister je eerst, vraag je wat hij bedoelt en denk je "
                  "erover na.</strong> <strong>Feedback geef je liefst onder vier ogen</strong> en niet voor "
                  "de hele groep, want dan voelt ze als een afrekening."),
        ]),
        dict(kop="Verbindend communiceren", blokken=[
            ("p", "<strong>Verbindend of geweldloos communiceren gaat in vier stappen</strong>: "
                  "<strong>waarneming, gevoel, behoefte en verzoek</strong>. Straffen hoort er niet bij."),
            ("fig", svg.stappen(["de waarneming|wat je ziet", "het gevoel|wat het met je doet",
                                 "de behoefte|wat je nodig hebt", "het verzoek|wat je vraagt"])),
            ("p", "<strong>Je begint bij de waarneming</strong>: <strong>wat je ziet of hoort, zonder "
                  "oordeel</strong>. \"Je kwam tien minuten later\" in plaats van \"Je bent onbetrouwbaar\". "
                  "<strong>Daarna benoem je je gevoel</strong>, want <strong>zo begrijpt de ander je "
                  "beter</strong> en weet hij wat zijn gedrag teweegbrengt. <strong>Na het gevoel komt de "
                  "behoefte</strong>, en <strong>je sluit af met een verzoek</strong>."),
            ("p", "<strong>Een verzoek is een vraag om iets te doen, geen bevel.</strong> <strong>Het "
                  "verschil met een eis is dat de ander bij een verzoek ook nee mag zeggen.</strong> Is nee "
                  "geen optie, dan is het geen verzoek maar een eis."),
            ("p", "<strong>Geweldloze communicatie is direct, doeltreffend, emotioneel, empathisch en "
                  "respectvol.</strong> Dwingen hoort er niet bij. <strong>Empathisch communiceren is je "
                  "inleven in de ander</strong>, dus net niet enkel aan jezelf denken."),
        ]),
        dict(kop="Herstelgericht werken", blokken=[
            ("p", "<strong>Herstelgericht werken richt zich op het herstellen van de schade</strong>: wat "
                  "kapot ging tussen mensen, wordt samen hersteld. <strong>Het draait dus niet om "
                  "straffen.</strong>"),
            ("kader", tabel(["de vraag", "waarom je ze stelt"],
                            [["<strong>wat is er gebeurd?</strong>", "<strong>die vraag komt eerst</strong>: eerst het verhaal, van beide kanten, voor er iets beslist wordt"],
                             ["<strong>wie heeft er last van?</strong>", "zo komt in beeld wie geraakt werd"],
                             ["<strong>wat heb je nodig?</strong>", "zo kom je bij het herstel in plaats van bij de straf"]])),
            ("p", "<strong>Het doel van herstelgerichte vragen is samen een oplossing vinden</strong>: "
                  "iedereen krijgt zijn verhaal, en samen zoek je hoe het hersteld raakt."),
        ]),
    ])


# ───────────────────────── 14. Vrije tijd, spel en expressie
zet("vrije-tijd-spel-en-expressie",
    titel="Vrije tijd, spel en expressie",
    onder="Wat vrije tijd is en wat de invulling bepaalt, waarom vervelen nuttig is, de vier ervaringsgebieden en de vijf expressievormen.",
    secties=[
        dict(kop="Vrije tijd", blokken=[
            ("p", "<strong>Vrije tijd is de tijd die je zelf invult</strong>: wat overblijft na school, werk "
                  "en verplichtingen."),
            ("kader", tabel(["factor", "wat ze betekent"],
                            [["<strong>de leeftijd</strong> of levensfase", "<strong>een peuter speelt anders</strong> dan een tiener: de peuter stapelt blokken, de tiener spreekt af met vrienden"],
                             ["<strong>het moment van de dag</strong>", "<strong>na school hoeft het rustig</strong>: na een volle schooldag past iets rustigs beter"],
                             ["<strong>de mogelijkheden en beperkingen</strong>", "<strong>wat iemand wel en niet kan</strong>: geld, vervoer, gezondheid en vaardigheden"],
                             ["<strong>de wensen en verwachtingen</strong>", "<strong>wie mee kiest, doet veel liever mee</strong>"]])),
            ("p", "<strong>Een goed vrijetijdsaanbod past bij de leeftijd, geeft keuze en is haalbaar.</strong> "
                  "Verplichten hoort niet bij vrije tijd."),
            ("p", "<strong>Een kind mag ook niets doen in zijn vrije tijd: vervelen mag.</strong> "
                  "<strong>Vervelen is zelfs nuttig, want het zet de fantasie aan</strong>: uit verveling "
                  "ontstaat het mooiste zelfbedachte spel."),
            ("p", "<strong>Bij vrij spel kiest het kind zelf wat het doet, met wie en hoe lang.</strong> De "
                  "begeleider bepaalt dat dus niet. <strong>Vrij spel is belangrijk omdat het kind er leert "
                  "kiezen</strong>, en ook onderhandelen, verzinnen en doorzetten. <strong>Kinderen bewegen "
                  "het best elke dag een tijd.</strong>"),
        ]),
        dict(kop="De vier ervaringsgebieden", blokken=[
            ("fig", svg.kwadranten([("ik en de ander", ["samen spelen", "delen", "rekening houden met elkaar"]),
                                    ("lichaam en beweging", ["klimmen en springen", "grove en fijne motoriek", "kracht en evenwicht"]),
                                    ("communicatie en expressie", ["een toneeltje spelen", "praten en luisteren", "zingen en tekenen"]),
                                    ("de wereld verkennen", ["de natuur onderzoeken", "techniek en materialen", "de buurt ontdekken"])],
                                   onder="een goed aanbod laat alle vier aan bod komen")),
            ("p", "<strong>Lichaam en beweging is het ervaringsgebied over bewegen en de motoriek.</strong> "
                  "<strong>Bij het verkennen van de wereld ontdekt een kind hoe de wereld in elkaar "
                  "zit.</strong>"),
        ]),
        dict(kop="De vijf expressievormen", blokken=[
            ("p", "<strong>Expressie is jezelf uitdrukken</strong>: uiten wat in je leeft, in beweging, "
                  "taal, beeld of muziek. Er zijn <strong>vijf vormen</strong>."),
            ("kader", tabel(["vorm", "wat je doet"],
                            [["<strong>bewegingsexpressie</strong>", "dansen, bewegen op muziek"],
                             ["<strong>dramatische expressie</strong>", "<strong>een rol spelen</strong>: toneel, poppenkast of doen-alsof"],
                             ["<strong>manuele expressie</strong>", "<strong>iets maken met je handen</strong>: knutselen, tekenen, boetseren, bouwen"],
                             ["<strong>muzikale expressie</strong>", "zingen, een instrument bespelen, luisteren"],
                             ["<strong>verbale expressie</strong>", "vertellen, voorlezen, een verhaal verzinnen; de verbale vorm werkt met woorden"]])),
            ("p", "<strong>Zingen is dus muzikale expressie, geen manuele</strong>; bij manuele expressie "
                  "werk je met je handen. <strong>Expressie is belangrijk omdat een kind zich kan "
                  "uiten</strong>: wat het nog niet in woorden kan zeggen, komt er in spel, beeld of "
                  "beweging uit."),
            ("p", "<strong>Bewegen maakt een kind sterker, het slaapt er beter van en het leert zijn lichaam "
                  "kennen.</strong> Het bouwt spieren, evenwicht, uithouding en zelfvertrouwen op."),
            ("p", "<strong>Een activiteit voor een groep kies je door naar hun leeftijd te kijken</strong>, "
                  "en verder naar hun mogelijkheden, hun wensen en het moment van de dag. <strong>Wil een "
                  "kind niet meedoen, dan vraag je waarom</strong>: daarachter zit vaak onzekerheid of "
                  "vermoeidheid. <strong>Je biedt verschillende soorten activiteiten aan omdat elk kind "
                  "anders is</strong>, zodat elk ervaringsgebied aan bod komt."),
        ]),
    ])


# ───────────────────────── 15. Spelvormen en speelgoed
zet("spelvormen-en-speelgoed",
    titel="Spelvormen en speelgoed",
    onder="De zes spelvormen en bij welke leeftijd ze passen, wat een kind nodig heeft om te spelen, speelgoed kiezen, en het verloop van een activiteit van voorbereiding tot opruimen.",
    secties=[
        dict(kop="De zes spelvormen", blokken=[
            ("kader", tabel(["spelvorm", "wat het kind doet"],
                            [["<strong>spelen met dingen</strong>", "<strong>bouwen met blokken</strong>: stapelen, sorteren, in elkaar steken. <strong>Dit past bij een peuter.</strong>"],
                             ["<strong>spelen door bewegen</strong>", "<strong>klimmen en fietsen</strong>, rennen, springen: het lichaam is het speelgoed"],
                             ["<strong>creatief spelen</strong>", "<strong>knutselen, boetseren, zelf iets bouwen</strong>: het kind maakt iets dat er nog niet was"],
                             ["<strong>fantasiespelletjes</strong>", "<strong>doen alsof je iemand bent</strong>: winkeltje, dokter of papa en mama. <strong>Dit past bij een kleuter.</strong>"],
                             ["<strong>tekenen</strong>", "<strong>het kind geeft vorm aan ideeën</strong>, lang voor het die kan opschrijven"],
                             ["<strong>spelen met taal</strong>", "<strong>rijmen en woordgrapjes</strong>, versjes, moppen en zelfverzonnen woorden; ook taalspel of woordspel genoemd"]])),
            ("p", "<strong>Tekenen hoort dus wel degelijk bij de spelvormen</strong>: het is een van de zes. "
                  "<strong>Fantasiespel past bij de kleuter</strong>, want die denkt symbolisch, en daar "
                  "hoort doen-alsof helemaal bij. <strong>Van fantasiespel leert een kind zich inleven, "
                  "taal gebruiken en samen afspreken</strong>: in een rol kruipen is oefenen in het "
                  "standpunt van een ander."),
        ]),
        dict(kop="Wat een kind nodig heeft om te spelen", blokken=[
            ("p", "<strong>Een kind heeft vooral tijd en ruimte nodig.</strong> Zonder die twee komt spel "
                  "niet op gang, hoeveel speelgoed er ook ligt."),
            ("p", "<strong>Een begeleider mag meespelen als het kind dat wil</strong>, zolang het spel van "
                  "het kind blijft. <strong>Loopt een spel vast, dan help je even op weg</strong>: een "
                  "kleine zet is genoeg, daarna laat je het kind weer zelf verder."),
        ]),
        dict(kop="Speelgoed kiezen", blokken=[
            ("p", "<strong>Bij de keuze van speelgoed let je op de leeftijd, de veiligheid en wat het kind "
                  "ermee leert.</strong> De prijs alleen is geen goede maatstaf."),
            ("kader", tabel(["speelgoed", "waarvoor het goed is"],
                            [["<strong>een rammelaar</strong>", "<strong>past bij een baby</strong>, die met ogen, oren, mond en handen ontdekt"],
                             ["<strong>een verkleedkoffer</strong>", "<strong>past bij een kleuter</strong>, die graag doen-alsof speelt"],
                             ["<strong>kralen rijgen</strong>", "<strong>de fijne motoriek</strong>: kleine, precieze bewegingen van vingers en handen"],
                             ["<strong>een bal</strong>", "<strong>de grove motoriek</strong>: grote bewegingen met armen, benen en heel het lichaam"],
                             ["<strong>een prentenboek</strong>", "<strong>de taalontwikkeling</strong>: samen kijken en benoemen levert woorden, zinnen en verhalen op"]])),
            ("p", "<strong>Bij de veiligheid let je op kleine losse stukjes</strong>, want die kunnen "
                  "ingeslikt worden; kijk ook naar scherpe randen en stevigheid. <strong>Speelgoed voor een "
                  "baby mag dus zeker geen kleine losse stukjes bevatten</strong>, want een baby stopt alles "
                  "in zijn mond."),
        ]),
        dict(kop="Het verloop van een activiteit", blokken=[
            ("fig", svg.stappen(["voorbereiden|alles klaar", "begeleiden|de kinderen opvolgen",
                                 "afronden|samen opruimen", "nabespreken|hoe was het?"])),
            ("kader", tabel(["wanneer", "wat je doet"],
                            [["<strong>voor de activiteit</strong>", "<strong>je zet alles klaar, je kijkt de ruimte na en je legt de afspraken uit</strong>"],
                             ["<strong>tijdens de activiteit</strong>", "<strong>je volgt de kinderen op</strong>: je kijkt, helpt waar nodig en past aan als iets niet loopt"],
                             ["<strong>na de activiteit</strong>", "<strong>je ruimt samen op, je bespreekt het na en je bergt het materiaal op</strong>"]])),
            ("p", "<strong>Je laat kinderen mee opruimen omdat ze zo zorg leren dragen.</strong> Opruimen is "
                  "geen straf maar een deel van het spel, en <strong>het hoort bij de activiteit</strong>."),
            ("p", "<strong>Of een activiteit geslaagd was, zie je door te kijken en na te vragen</strong>: "
                  "observeren tijdens de activiteit en achteraf vragen hoe het was. <strong>Blijkt ze te "
                  "moeilijk, dan pas je ze aan</strong>: je maakt de opdracht kleiner of je helpt mee, zodat "
                  "het toch lukt."),
        ]),
    ])


# ───────────────────────── 16. Activiteiten voor volwassenen
zet("activiteiten-voor-volwassenen",
    titel="Activiteiten voor volwassenen",
    onder="De vier soorten activiteiten voor volwassenen en ouderen, waarom zelf doen belangrijk blijft, en kwaliteitsbewust werken: veilig, hygiënisch, ergonomisch, economisch en duurzaam.",
    secties=[
        dict(kop="De vier soorten activiteiten", blokken=[
            ("kader", tabel(["soort", "wat het is", "voorbeeld"],
                            [["<strong>belevingsgericht</strong>", "<strong>ze spreekt de zintuigen aan</strong>: ruiken, voelen, horen en proeven; de beleving zelf is het doel", "<strong>samen muziek beluisteren</strong>, een geur, een handmassage"],
                             ["<strong>ADL</strong>", "<strong>activiteiten van het dagelijks leven</strong>", "<strong>zich wassen, zich aankleden, zelf eten</strong>, zich verplaatsen"],
                             ["<strong>functiebehoudend</strong>", "<strong>ze houdt een vaardigheid wakker</strong>: wat iemand nog kan, blijft hij doen", "<strong>samen een maaltijd klaarmaken</strong>, groenten snijden, de tafel dekken"],
                             ["<strong>recreatief</strong>", "een recreatieve activiteit: <strong>ze is er voor het plezier</strong>: ontspanning is het doel", "een spelnamiddag, een uitstap, een optreden"]])),
            ("p", "<strong>Een functiebehoudende activiteit leert dus niets volledig nieuws aan</strong>; ze "
                  "houdt net wakker wat iemand al kan."),
        ]),
        dict(kop="Zelf blijven doen", blokken=[
            ("p", "<strong>Bij een activiteit voor een oudere let je op zijn tempo, zijn mogelijkheden en "
                  "zijn wensen.</strong> Het getal van zijn leeftijd zegt weinig."),
            ("p", "<strong>Je biedt ADL-activiteiten aan zodat de persoon zelfstandig blijft.</strong> Door "
                  "zelf te blijven doen, houdt iemand zijn zelfstandigheid langer vast. <strong>Kan een "
                  "bewoner iets zelf, dan laat je hem begaan</strong>: overnemen gaat sneller, maar het "
                  "kost hem een stukje kunnen. <strong>Je neemt dus niet alles over.</strong>"),
            ("p", "<strong>Zelf doen is belangrijk omdat een oudere zo zijn kunnen behoudt</strong>: wat je "
                  "niet meer gebruikt, verlies je, en dat geldt voor het lichaam en voor het hoofd. "
                  "<strong>Lukt een activiteit niet, dan pas je ze aan hem aan</strong>: maak de stap "
                  "kleiner of help een deel, zodat er toch iets lukt."),
        ]),
        dict(kop="Kwaliteitsbewust werken", blokken=[
            ("p", "<strong>Kwaliteitsbewust handelen is veilig, hygiënisch, ergonomisch, economisch en "
                  "duurzaam werken.</strong> Snelheid is geen kwaliteit."),
            ("kader", tabel(["manier", "wat het betekent"],
                            [["<strong>veilig</strong>", "<strong>je maakt de ruimte vrij</strong>: een vrije doorgang, genoeg licht en niets om over te struikelen"],
                             ["<strong>hygiënisch</strong>", "<strong>je voorkomt besmetting</strong>, zeker bij ouderen en bij voedsel"],
                             ["<strong>ergonomisch</strong>", "<strong>je spaart je rug</strong>: je houding en je werkplek zo schikken dat je lichaam het volhoudt"],
                             ["<strong>economisch</strong>", "<strong>je gebruikt niet te veel</strong>: zuinig met materiaal, water, energie en tijd"],
                             ["<strong>duurzaam</strong>", "<strong>je denkt aan later</strong>: duurzaamheid is wat je gebruik betekent voor het milieu"]])),
            ("p", "<strong>Ergonomisch tillen doe je door door je knieën te zakken</strong>, met je "
                  "rug recht en de last dicht tegen je lichaam."),
            ("p", "<strong>Duurzaam werken bij een activiteit is materiaal hergebruiken, het afval sorteren "
                  "en water sparen.</strong> Alles meteen weggooien is net het tegenovergestelde."),
            ("p", "<strong>Voor je met voedsel werkt, was je je handen.</strong> Dat is de eerste en de "
                  "belangrijkste stap. <strong>Na een activiteit maak je het materiaal schoon, berg je het "
                  "op en kijk je het na</strong>, zodat het bruikbaar blijft voor de volgende keer."),
            ("p", "<strong>Bij een bewoner die slecht te been is, neem je losse matten weg.</strong> Losse "
                  "matten, snoeren en natte vloeren zijn de grootste valrisico's. <strong>Zie je een "
                  "onveilige situatie, dan grijp je meteen in</strong>: eerst het gevaar wegnemen, daarna "
                  "melden aan wie het moet weten. <strong>Je laat ze dus niet tot morgen liggen.</strong>"),
            ("p", "<strong>Je bereidt een activiteit goed voor omdat ze dan vlotter verloopt</strong>: alles "
                  "klaar betekent dat je tijdens de activiteit bij de mensen kan blijven."),
        ]),
    ])

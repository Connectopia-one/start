# -*- coding: utf-8 -*-
"""De leerbundels voor wetenschap en techniek, categorie Start.

Zeven bundels, één per hoofdstuk. Ze zijn op 23 september 2026 fors
uitgebreid omdat er vragen in het platform stonden waarover niets in de
bundel te vinden was. Elke vraag uit `inhoud/start/wetenschap-en-techniek.json`
moet hier haar antwoord vinden; zie de memory connectopia-leerbundel-dekt-vragen.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel
tabel = bundel.tabel

VAK = "Wetenschap en techniek"
BUNDELS = {}

BUNDELS["biologie-leven-en-ecologie"] = dict(
    vak=VAK, titel="Biologie: leven en ecologie",
    onder="Planten, dieren, en hoe alles in de natuur met elkaar samenhangt.",
    secties=[
        dict(kop="Wat leeft, en wat niet", blokken=[
            ("p", "Iets leeft als het aan alle vijf de kenmerken voldoet: het <strong>groeit</strong>, "
                  "het <strong>voedt zich</strong>, het <strong>ademt</strong>, het "
                  "<strong>plant zich voort</strong> en het <strong>reageert op zijn omgeving</strong>."),
            ("weetje", "Een vlam groeit, verbruikt zuurstof en beweegt, maar plant zich niet voort. "
                       "Daarom leeft vuur niet, hoe levend het er ook uitziet."),
            ("p", "Planten leven dus ook. Een boom is een plant, net zoals gras en een paardenbloem. "
                  "<strong>Schimmels</strong> zijn geen planten: ze hebben geen bladgroen en maken geen "
                  "eigen voedsel. Ze vormen een eigen groep."),
        ]),
        dict(kop="Een plant van dichtbij", blokken=[
            ("fig", svg.plantdelen(340), "Elk deel van de plant heeft zijn eigen taak."),
            ("fig", tabel(["Deel", "Waarvoor het dient"], [
                ["wortel", "water en voedingsstoffen opnemen, en de plant vasthouden"],
                ["stengel", "alles rechthouden en het water naar boven brengen"],
                ["blad", "zonlicht opvangen en voedsel maken"],
                ["bloem", "zaadjes maken, met hulp van insecten of de wind"],
            ]), None),
            ("p", "In het blad maakt de plant zelf haar voedsel. Dat heet <strong>fotosynthese</strong>: "
                  "uit <strong>licht</strong>, <strong>water</strong> en <strong>koolstofdioxide</strong> "
                  "maakt ze suiker, en daarbij komt <strong>zuurstof</strong> vrij. Foto betekent licht, "
                  "synthese betekent samenstellen."),
            ("p", "Dat is precies omgekeerd aan wat wij doen bij het ademen. Zonder planten zou er geen "
                  "zuurstof in de lucht zitten."),
        ]),
        dict(kop="Bloemen, bestuiving en zaden", blokken=[
            ("p", "Bij de <strong>bestuiving</strong> komt stuifmeel van de meeldraden op de stamper "
                  "terecht. Pas daarna kunnen er zaadjes en vruchten groeien. Insecten doen dat werk, "
                  "vooral <strong>bijen</strong>, en bij sommige planten de wind."),
            ("p", "Daarna moet het zaad weg van de moederplant, anders staan ze elkaar in de weg. "
                  "Planten laten hun zaden meereizen met de <strong>wind</strong> (een paardenbloem), "
                  "met <strong>water</strong>, of met <strong>dieren</strong>: een klit haakt vast in "
                  "een vacht, en een vogel eet een bes en poept de pit verderop weer uit."),
            ("weetje", "Verdwijnen de bijen, dan worden veel planten niet meer bestoven, en komen er "
                       "dus ook minder vruchten. Een derde van ons voedsel hangt aan bestuivers vast."),
        ]),
        dict(kop="Dieren indelen", blokken=[
            ("p", "De eerste vraag die een bioloog stelt is: heeft het dier een <strong>ruggengraat</strong>? "
                  "Dieren mét ruggengraat heten <strong>gewervelde</strong> dieren, dieren zonder heten "
                  "ongewerveld. Insecten, spinnen, wormen en slakken zijn ongewerveld."),
            ("fig", tabel(["Groep", "Waaraan je ze herkent", "Voorbeeld"], [
                ["zoogdieren", "haren, jongen drinken melk bij de moeder", "hond, vleermuis, walvis"],
                ["vogels", "veren, snavel, leggen eieren", "mus, struisvogel, pinguïn"],
                ["vissen", "schubben, kieuwen, leven in water", "karper, haai"],
                ["reptielen", "droge huid met schubben, koudbloedig", "hagedis, slang, schildpad"],
                ["amfibieën", "eerst in het water, later ook op het land", "kikker, salamander"],
            ]), "Alleen vogels hebben veren. Vleugels heeft een vleermuis ook, en eieren legt bijna iedereen."),
            ("p", "Niet alle vogels vliegen: een struisvogel loopt en een pinguïn zwemt met zijn vleugels. "
                  "En een <strong>spin is geen insect</strong>: een insect heeft zes poten en drie "
                  "lichaamsdelen, een spin acht poten en twee."),
        ]),
        dict(kop="Groeien en veranderen", blokken=[
            ("p", "Sommige dieren veranderen volledig van vorm tijdens hun leven. Dat heet een "
                  "<strong>gedaanteverwisseling</strong> of metamorfose."),
            ("fig", svg.stappen(["Eitje", "Rups", "Pop", "Vlinder"], kleur=svg.AMBER),
             "Bij een kikker gaat het net zo: eitje, dikkopje, kikker."),
        ]),
        dict(kop="Aangepast aan de seizoenen", blokken=[
            ("p", "In de winter is er weinig licht en weinig voedsel. Elk dier en elke plant heeft daar "
                  "zijn eigen oplossing voor."),
            ("fig", tabel(["Oplossing", "Wie het doet", "Waarom het werkt"], [
                ["bladeren laten vallen", "loofbomen", "geen verdamping als er weinig water opneembaar is"],
                ["winterslaap", "egel, vleermuis, marmot", "lichaam koelt af, hart klopt trager, bijna geen voedsel nodig"],
                ["wegtrekken", "zwaluw, ooievaar", "in het zuiden zijn er in de winter nog insecten"],
                ["blijven en zaden eten", "mees, merel", "zaden en bessen zijn er ook in de winter"],
            ]), None),
            ("p", "Er is nog een aanpassing die het hele jaar meespeelt: <strong>camouflage</strong>. "
                  "Een kleur of vorm waardoor een dier opgaat in zijn omgeving. Een rups die op een takje "
                  "lijkt, wordt niet opgegeten; een sneeuwhaas die wit wordt, wordt niet gezien."),
        ]),
        dict(kop="Voedselketens en voedselwebben", blokken=[
            ("p", "In de natuur eet alles van iets anders. Zo'n rij noem je een <strong>voedselketen</strong>, "
                  "en ze begint altijd bij een plant, want alleen planten maken hun eigen voedsel. Zij heten "
                  "de <strong>producenten</strong>."),
            ("fig", svg.stappen(["Gras|maakt zelf voedsel", "Konijn|eet planten", "Vos|eet dieren"]),
             "De pijl wijst naar wie eet. Gras → konijn → vos."),
            ("fig", tabel(["Naam", "Wat het dier eet", "Voorbeeld"], [
                ["herbivoor", "alleen planten", "konijn, koe, rups"],
                ["carnivoor", "alleen vlees", "vos, leeuw, havik"],
                ["omnivoor of alleseter", "planten én vlees", "mens, beer, varken"],
                ["afbreker", "dode resten", "schimmel, bacterie, pissebed, regenworm"],
            ]), "Zonder afbrekers zou een bos onder zijn eigen bladeren bedolven raken."),
            ("p", "In het echt eet bijna geen enkel dier maar één ding. Alle ketens haken dus in elkaar, "
                  "en samen vormen ze een <strong>voedselweb</strong>. Verdwijnt één schakel, dan voelt "
                  "de rest dat ook."),
        ]),
        dict(kop="Ecosysteem en biodiversiteit", blokken=[
            ("p", "De plaats waar een dier leeft met alles wat het nodig heeft, heet zijn "
                  "<strong>habitat</strong> of leefgebied. Een <strong>ecosysteem</strong> is ruimer: "
                  "alles wat in één gebied samenleeft, samen met de bodem, het water en het weer. Een "
                  "vijver, een bos en een duin zijn ecosystemen."),
            ("p", "<strong>Biodiversiteit</strong> is hoeveel verschillende soorten er in zo'n gebied "
                  "leven. Het gaat om de verscheidenheid, niet om het aantal: honderd konijnen zijn "
                  "minder divers dan tien verschillende soorten."),
            ("p", "Dat is meer dan een mooi cijfer. Leven er veel soorten, dan kan de natuur een "
                  "tegenslag beter opvangen: valt er één weg, dan zijn er andere die haar taak "
                  "overnemen. Bij weinig soorten stort de boel veel sneller in."),
            ("weetje", "Uitgestorven is voorgoed. Van een soort waarvan het laatste dier dood is, komt "
                       "er nooit meer één bij. Daarom proberen mensen soorten te beschermen vóór het "
                       "zover komt."),
        ]),
        dict(kop="Zorg dragen voor de natuur", blokken=[
            ("p", "<strong>Regenwormen</strong> maken gangen in de grond, zodat er lucht en water bij "
                  "de wortels raakt, en ze trekken bladeren de grond in. Een boswachter laat "
                  "<strong>dood hout</strong> liggen om dezelfde reden: er leven insecten en schimmels "
                  "in die het afbreken tot voeding voor de bodem."),
            ("p", "In je eigen tuin werkt hetzelfde. Bloemen laten bloeien, een hoekje laten "
                  "verwilderen, een takkenhoop laten liggen en wat water zetten is voor insecten en "
                  "vogels meer waard dan een perfect kortgemaaid gazon."),
        ]),
    ],
    onthoud=[
        "Leven betekent: groeien, voeden, ademen, voortplanten en reageren.",
        "Bij de fotosynthese maakt het blad suiker uit licht, water en koolstofdioxide, en komt zuurstof vrij.",
        "Bij de bestuiving komt stuifmeel van de meeldraden op de stamper.",
        "Gewervelde dieren hebben een ruggengraat. Insecten hebben 6 poten, spinnen 8.",
        "Alleen vogels hebben veren, en niet alle vogels vliegen.",
        "Een voedselketen begint altijd bij een plant; de pijl wijst naar wie eet.",
        "Herbivoor eet planten, carnivoor vlees, omnivoor allebei; afbrekers eten dode resten.",
        "Biodiversiteit is hoeveel verschillende soorten er leven — en dat maakt de natuur sterker.",
        "In een ecosysteem hangt alles aan elkaar vast.",
    ])

BUNDELS["biologie-het-menselijk-lichaam"] = dict(
    vak=VAK, titel="Biologie: het menselijk lichaam",
    onder="Wat er binnenin gebeurt terwijl je er niet aan denkt — en hoe je er goed voor zorgt.",
    secties=[
        dict(kop="Je lichaam als één geheel", blokken=[
            ("p", "Je lichaam is opgebouwd uit <strong>stelsels</strong>: groepen organen die samen één "
                  "taak uitvoeren. Ze werken allemaal tegelijk, en ze hebben elkaar nodig."),
            ("fig", tabel(["Stelsel", "Wat het doet", "Belangrijkste organen"], [
                ["ademhaling", "zuurstof binnen, koolstofdioxide buiten", "neus, luchtpijp, longen"],
                ["bloedsomloop", "zuurstof en voedsel rondbrengen", "hart, slagaders, aders"],
                ["spijsvertering", "voedsel afbreken tot bruikbare stoffen", "maag, darmen, lever"],
                ["skelet en spieren", "rechthouden en bewegen", "botten, spieren, gewrichten"],
                ["zenuwstelsel", "alles aansturen en waarnemen", "hersenen, ruggenmerg, zenuwen"],
                ["uitscheiding", "afvalstoffen kwijtraken", "nieren, blaas, huid"],
            ]), "Je hart klopt ongeveer 100 000 keer per dag, zonder dat je eraan denkt."),
        ]),
        dict(kop="De spijsvertering", blokken=[
            ("p", "Verteren is: je eten zo klein maken dat het door de darmwand naar je bloed kan. Dat "
                  "begint al in je <strong>mond</strong>, bij het kauwen en het speeksel. Goed kauwen "
                  "loont dus echt."),
            ("fig", svg.stappen(["Mond|kauwen en|speeksel", "Slokdarm|duwen", "Maag|kneden en|maagsap",
                                 "Dunne darm|opname in|het bloed", "Dikke darm|water eruit"]),
             "De slokdarm duwt met spierbewegingen. Daarom kan je ook drinken terwijl je op je kop hangt."),
            ("p", "<strong>Maagsap</strong> is zuur. Het breekt het voedsel verder af en doodt meteen "
                  "veel ziektekiemen. In de <strong>dunne darm</strong>, bij een volwassene wel vijf "
                  "meter lang en vanbinnen geplooid, gaan de voedingsstoffen naar het bloed. Wat "
                  "overblijft, gaat naar de <strong>dikke darm</strong>, waar vooral water uit gehaald wordt."),
            ("p", "De <strong>lever</strong> is het grootste orgaan binnenin je lichaam. Hij haalt "
                  "schadelijke stoffen uit je bloed en maakt gal, die helpt om vetten af te breken."),
        ]),
        dict(kop="Het bloed en het hart", blokken=[
            ("p", "Het <strong>hart</strong> is een spier met <strong>vier holten</strong>: twee "
                  "boezems bovenaan en twee kamers onderaan. De rechterkant stuurt het bloed naar de "
                  "longen, de linkerkant naar de rest van je lichaam."),
            ("fig", svg.bloedsomloop(),
             "Het bloed passeert twee keer langs het hart voor het één volledig rondje gemaakt heeft."),
            ("p", "<strong>Slagaders</strong> voeren bloed wég van het hart en hebben dikke wanden, want "
                  "daar staat druk op — je voelt er je pols mee. <strong>Aders</strong> voeren het bloed "
                  "ernaartoe."),
            ("fig", tabel(["In je bloed", "Wat het doet"], [
                ["rode bloedcellen", "zuurstof vervoeren, en ze geven het bloed zijn kleur"],
                ["witte bloedcellen", "ziektekiemen opruimen"],
                ["bloedplaatjes", "wondjes dichten, zodat een schaafwonde stopt met bloeden"],
                ["bloedplasma", "de vloeistof waarin alles meereist"],
            ]), "Sport je, dan vragen je spieren meer zuurstof. Daarom klopt je hart dan sneller."),
        ]),
        dict(kop="De ademhaling", blokken=[
            ("p", "Adem je door je <strong>neus</strong>, dan wordt de lucht verwarmd, bevochtigd en "
                  "gefilterd: de haartjes en het slijm houden stof en ziektekiemen tegen. Via de "
                  "<strong>luchtpijp</strong> komt de lucht in je <strong>longen</strong>."),
            ("p", "Daar zitten honderden miljoenen <strong>longblaasjes</strong>. Daar gaat zuurstof "
                  "naar je bloed en komt koolstofdioxide eruit. Allemaal samen hebben die blaasjes een "
                  "oppervlakte zo groot als een tennisveld."),
            ("weetje", "Onder je longen ligt het <strong>middenrif</strong>, een grote platte spier. "
                       "Die trekt naar beneden en zuigt zo lucht binnen. De hik is niets anders dan een "
                       "plotse samentrekking van die spier."),
        ]),
        dict(kop="Botten en gewrichten", blokken=[
            ("p", "Een volwassene heeft ongeveer <strong>206 botten</strong>. Een baby heeft er meer, "
                  "ongeveer 300; tijdens het opgroeien groeien sommige aan elkaar vast."),
            ("fig", tabel(["Bot", "Wat het beschermt of doet"], [
                ["schedel", "de hersenen"],
                ["ribben", "het hart en de longen"],
                ["wervelkolom", "het ruggenmerg, en ze houdt je recht"],
                ["bekken", "de organen onderaan de buik"],
                ["arm- en beenbotten", "dragen je gewicht en laten je bewegen"],
            ]), None),
            ("p", "Waar twee botten ten opzichte van elkaar kunnen bewegen, zit een "
                  "<strong>gewricht</strong>: je knie, je elleboog, je schouder. Een laagje "
                  "<strong>kraakbeen</strong> zorgt ervoor dat de botten er niet op elkaar schuren."),
            ("weetje", "Een bot is geen dood stuk steen. Binnenin zit <strong>beenmerg</strong>, en daar "
                       "worden je bloedcellen aangemaakt."),
        ]),
        dict(kop="Spieren", blokken=[
            ("p", "Een spier kan maar één ding: <strong>samentrekken</strong>. Duwen kan ze niet. "
                  "Daarom zitten spieren in paren."),
            ("fig", svg.spierpaar(),
             "De buigspier plooit je arm, de strekspier strekt hem weer. Terwijl de ene trekt, ontspant de andere."),
            ("p", "Een <strong>pees</strong> is het stevige koordje dat een spier aan een bot vastmaakt. "
                  "De achillespees, boven je hiel, is de dikste van je lichaam."),
            ("p", "Sommige spieren stuur je zelf aan, zoals die in je armen en benen. Andere werken "
                  "vanzelf, zonder dat je eraan denkt: je hartspier, je darmen en je middenrif."),
        ]),
        dict(kop="Het zenuwstelsel", blokken=[
            ("p", "Het zenuwstelsel bestaat uit de <strong>hersenen</strong>, het "
                  "<strong>ruggenmerg</strong> en de <strong>zenuwen</strong>. De zenuwen zijn de draden "
                  "die berichten heen en weer sturen, aan meer dan honderd meter per seconde."),
            ("p", "Raak je iets heets aan, dan trek je je hand weg nog vóór je het beseft. Dat is een "
                  "<strong>reflex</strong>: dat bericht gaat via het ruggenmerg en niet eerst langs de "
                  "hersenen. Zo win je een fractie van een seconde, en dat scheelt bij een brandwonde. "
                  "Pas daarna voel je de pijn."),
        ]),
        dict(kop="De zintuigen", blokken=[
            ("fig", tabel(["Zintuig", "Waar", "Hoe het werkt"], [
                ["zien", "de ogen", "de pupil laat licht binnen, het netvlies vangt het beeld op"],
                ["horen", "de oren", "het trommelvlies trilt mee met het geluid"],
                ["ruiken", "de neus", "geurdeeltjes uit de lucht komen op het slijmvlies"],
                ["proeven", "de tong", "smaakpapillen herkennen zoet, zout, zuur en bitter"],
                ["voelen", "de huid", "voelt aanraking, warmte, koude en pijn"],
            ]), "Vijf zintuigen. Je hebt daarnaast ook nog een gevoel voor evenwicht."),
            ("p", "De <strong>pupil</strong> is het gaatje waar het licht binnenkomt. Bij fel licht "
                  "knijpt hij dicht, in het donker gaat hij wijd open. Zo komt er nooit te veel of te "
                  "weinig licht binnen."),
            ("weetje", "Diep in je oor zitten kanaaltjes met vocht die voelen hoe je hoofd beweegt. "
                       "Daarom helpt je oor je ook bij het evenwicht, en word je duizelig van rondtollen."),
        ]),
        dict(kop="Nieren, blaas en huid", blokken=[
            ("p", "Je <strong>nieren</strong> filteren afvalstoffen uit je bloed en maken er "
                  "<strong>urine</strong> van. Die wordt opgeslagen in de <strong>blaas</strong> tot je "
                  "naar het toilet gaat."),
            ("p", "De <strong>huid</strong> is het grootste orgaan van je hele lichaam. Ze houdt "
                  "ziektekiemen buiten, regelt je temperatuur en voelt. <strong>Zweten</strong> koelt je "
                  "af, want het zweet verdampt op je huid, en verdampen kost warmte."),
        ]),
        dict(kop="Gezond leven", blokken=[
            ("fig", tabel(["Wat", "Waarom"], [
                ["gevarieerd eten", "geen enkel voedingsmiddel bevat alle stoffen die je nodig hebt"],
                ["genoeg drinken", "je lichaam bestaat voor meer dan de helft uit water"],
                ["9 tot 11 uur slaap", "je groeit in je slaap en je hersenen ruimen op wat je leerde"],
                ["elke dag bewegen", "houdt je hart, je spieren en je botten sterk"],
                ["twee keer per dag tanden poetsen", "tandbederf komt niet meer goed"],
                ["handen wassen", "de eenvoudigste manier om ziektekiemen tegen te houden"],
            ]), "Eiwitten om te bouwen, koolhydraten en vetten voor energie, vitaminen en mineralen om alles te laten werken."),
        ]),
        dict(kop="Ziek worden en beter worden", blokken=[
            ("p", "Een <strong>bacterie</strong> is een levend wezentje van één cel. Een "
                  "<strong>virus</strong> is veel kleiner en kan zich alleen vermenigvuldigen binnenin "
                  "een cel. Daarom werken antibiotica wel tegen bacteriën en niet tegen een virus, "
                  "zoals een verkoudheid."),
            ("p", "<strong>Koorts</strong> is geen pech maar een wapen: bij een hogere temperatuur werkt "
                  "je afweer beter en hebben veel ziektekiemen het moeilijker."),
            ("p", "Een <strong>vaccin</strong> leert je afweersysteem een ziektekiem herkennen nog vóór "
                  "je ziek wordt. Kom je de echte kiem later tegen, dan is je lichaam al voorbereid."),
        ]),
    ],
    onthoud=[
        "De weg van je eten: mond, slokdarm, maag, dunne darm, dikke darm.",
        "In de dunne darm gaan de voedingsstoffen naar je bloed; de dikke darm haalt er water uit.",
        "Het hart heeft vier holten. Slagaders gaan wég van het hart, aders ernaartoe.",
        "Rode bloedcellen vervoeren zuurstof, witte ruimen ziektekiemen op, bloedplaatjes dichten wondjes.",
        "In de longblaasjes gaat zuurstof naar je bloed en komt koolstofdioxide eruit.",
        "Een volwassene heeft ongeveer 206 botten; in het beenmerg wordt bloed aangemaakt.",
        "Een spier kan alleen trekken. Daarom werken spieren in paren.",
        "Een reflex loopt via het ruggenmerg, niet via de hersenen.",
        "Vijf zintuigen: zien, horen, ruiken, proeven en voelen. De huid is je grootste orgaan.",
        "De nieren filteren je bloed en maken urine.",
        "Antibiotica werken op bacteriën, niet op een virus. Een vaccin leert je afweer een kiem herkennen.",
    ])

BUNDELS["chemie-stoffen-en-mengsels"] = dict(
    vak=VAK, titel="Chemie: stoffen en mengsels",
    onder="Waaruit dingen bestaan, hoe ze van vorm veranderen en hoe je een mengsel weer uit elkaar haalt.",
    secties=[
        dict(kop="Drie toestanden", blokken=[
            ("p", "Alles om je heen bestaat uit piepkleine deeltjes. Hoe die deeltjes liggen, bepaalt of "
                  "een stof vast, vloeibaar of gasvormig is."),
            ("fig", svg.deeltjes(470), "Dezelfde deeltjes, alleen anders geordend."),
            ("p", "Water is daar het mooiste voorbeeld van: als ijs is het vast, als water vloeibaar en "
                  "als waterdamp een gas. Het blijft telkens water."),
        ]),
        dict(kop="Van de ene toestand naar de andere", blokken=[
            ("fig", tabel(["Verandering", "Hoe het heet", "Wanneer"], [
                ["vast → vloeibaar", "smelten", "ijs in je hand"],
                ["vloeibaar → vast", "stollen of bevriezen", "water in de diepvries"],
                ["vloeibaar → gas", "verdampen", "een plas die opdroogt"],
                ["gas → vloeibaar", "condenseren", "damp op een koude ruit"],
                ["vast → gas", "sublimeren", "droogijs, dat is bevroren koolstofdioxide"],
            ]), "Water bevriest bij 0 °C en kookt bij 100 °C."),
            ("weetje", "Bij al die veranderingen blijft de stof zelf dezelfde. Er komt of gaat alleen "
                       "warmte bij. Verbranden is iets heel anders: daar ontstaan nieuwe stoffen, en dat "
                       "kan je niet terugdraaien."),
        ]),
        dict(kop="Atomen en moleculen", blokken=[
            ("p", "<strong>Atomen</strong> zijn de allerkleinste bouwstenen. Zitten er een paar aan "
                  "elkaar vast, dan heet dat een <strong>molecule</strong>. Eén watermolecule bestaat "
                  "uit twee waterstofatomen en één zuurstofatoom. Daarom schrijven we water als H₂O."),
            ("p", "Ook lucht bestaat uit deeltjes, en lucht is een <strong>mengsel</strong>: ongeveer "
                  "78 % stikstof, 21 % zuurstof, en een heel klein beetje koolstofdioxide en andere gassen."),
        ]),
        dict(kop="Mengsels", blokken=[
            ("p", "Meng je twee stoffen, dan blijven het twee stoffen. Soms zie je dat nog (zand in "
                  "water), soms niet (suiker in water)."),
            ("fig", tabel(["Soort mengsel", "Voorbeeld", "Zie je de delen nog?"], [
                ["oplossing", "suiker in water", "nee"],
                ["troebel mengsel", "zand in water", "ja, het zakt naar beneden"],
                ["mengsel van vaste stoffen", "muesli", "ja"],
                ["mengsel van gassen", "lucht", "nee"],
                ["emulsie", "mayonaise: olie en water", "nee, maar ze zitten er allebei in"],
            ]), "In mayonaise houdt het eigeel de olie en het water aan elkaar. Zonder dat scheidt het meteen."),
            ("p", "Olie drijft op water omdat evenveel olie lichter is dan water. Wat lichter is voor "
                  "hetzelfde volume, komt bovenaan."),
        ]),
        dict(kop="Oplossen", blokken=[
            ("p", "Los je suiker op in water, dan is de suiker niet verdwenen; ze is alleen te klein "
                  "geworden om te zien. Weeg je 100 gram water en 10 gram suiker, dan weegt het geheel "
                  "achteraf nog altijd 110 gram."),
            ("p", "In <strong>warm</strong> water bewegen de deeltjes sneller, en lost suiker dus "
                  "sneller én in grotere hoeveelheid op. Blijft er toch suiker op de bodem liggen, dan "
                  "is de oplossing <strong>verzadigd</strong>: er kan niets meer bij."),
        ]),
        dict(kop="Een mengsel scheiden", blokken=[
            ("p", "Omdat de stoffen in een mengsel zichzelf blijven, kan je ze er weer uit halen. Welke "
                  "manier werkt, hangt af van wat erin zit."),
            ("fig", tabel(["Manier", "Waarvoor", "Voorbeeld"], [
                ["zeven", "grote en kleine stukken scheiden", "pasta uit kookwater"],
                ["filteren", "een vaste stof uit een vloeistof", "koffiefilter"],
                ["indampen", "een opgeloste stof terugwinnen", "zout uit zeewater"],
                ["bezinken", "zwaardere deeltjes laten zakken", "modder in een emmer"],
                ["magneet", "ijzer uit een mengsel halen", "ijzervijlsel uit zand"],
            ]), None),
            ("p", "Een mooi proefje: zet een streepje viltstift op een strook filtreerpapier en hang het "
                  "puntje in water. De kleur kruipt mee omhoog en splitst zich in de kleurstoffen waaruit "
                  "ze gemaakt is. Zwarte stift blijkt vaak uit blauw, rood en geel te bestaan."),
            ("weetje", "Die witte laag in je waterkoker is <strong>kalk</strong>: die zat opgelost in het "
                       "water en blijft achter als het water verdampt. Precies hetzelfde als zout uit "
                       "zeewater halen."),
        ]),
        dict(kop="Zuur en basisch", blokken=[
            ("p", "Sommige stoffen zijn <strong>zuur</strong>, zoals azijn en citroensap. Andere zijn "
                  "<strong>basisch</strong>, zoals zeep en soda. En sommige zijn neutraal, zoals zuiver "
                  "water en keukenzout."),
            ("p", "Hoe zuur of hoe basisch iets is, druk je uit met de <strong>pH</strong>. Onder 7 is "
                  "zuur, precies 7 is neutraal, boven 7 is basisch."),
            ("weetje", "Sap van rode kool verandert van kleur: rood of roze in een zuur, groen of geel "
                       "in een base. Zo'n stof heet een <strong>indicator</strong>, en daarmee kan je "
                       "thuis alles in de keuken testen."),
        ]),
        dict(kop="Verbranden en blussen", blokken=[
            ("p", "Om iets te laten branden heb je altijd drie dingen tegelijk nodig: "
                  "<strong>brandstof</strong>, <strong>zuurstof</strong> en <strong>warmte</strong>. Dat "
                  "heet de <strong>branddriehoek</strong>. Neem er één van weg, en het vuur dooft."),
            ("p", "Daarom dooft een kaars onder een omgekeerd glas: de zuurstof raakt op. En daarom leg "
                  "je een deksel op een brandende pan. <strong>Water op brandend frituurvet is "
                  "levensgevaarlijk</strong>: het water wordt in een flits stoom en slingert het "
                  "brandende vet in het rond."),
            ("p", "<strong>Roesten</strong> is eigenlijk een heel trage verbranding: ijzer dat langzaam "
                  "met zuurstof en water reageert. Ook dat kan je niet terugdraaien."),
        ]),
        dict(kop="Water op reis", blokken=[
            ("p", "Water uit de zee <strong>verdampt</strong> door de warmte van de zon, "
                  "<strong>condenseert</strong> hoog in de lucht tot wolken en valt weer naar beneden "
                  "als <strong>neerslag</strong>. Via beken en rivieren komt het terug in zee."),
            ("weetje", "Dat is de waterkringloop, en ze draait al miljarden jaren. Het water dat je "
                       "vandaag drinkt, is hetzelfde water dat de dinosaurussen dronken."),
        ]),
        dict(kop="Veilig werken", blokken=[
            ("p", "Op de verpakking van een gevaarlijk product staan waarschuwingstekens: een vlam voor "
                  "brandbaar, een doodshoofd voor giftig, een druppel die inbijt voor bijtend."),
            ("p", "Vind je thuis een fles die je niet kent: <strong>afblijven en het aan een volwassene "
                  "vragen</strong>. Niet eraan ruiken, niet uitgieten, en zeker niet verdunnen met water "
                  "— dat maakt het niet veilig. Ook doodgewone producten uit de badkamer kunnen samen "
                  "een schadelijk gas vormen."),
        ]),
    ],
    onthoud=[
        "Vast, vloeibaar en gas: dezelfde deeltjes, anders geordend.",
        "Smelten, stollen, verdampen, condenseren en sublimeren.",
        "Water bevriest bij 0 °C en kookt bij 100 °C. Eén watermolecule is H₂O.",
        "Lucht is een mengsel: ongeveer 78 % stikstof en 21 % zuurstof.",
        "In een mengsel blijft elke stof zichzelf, en niets gaat verloren bij het oplossen.",
        "Zeven, filteren, indampen, bezinken en de magneet scheiden een mengsel.",
        "pH onder 7 is zuur, 7 is neutraal, boven 7 is basisch.",
        "Branden vraagt brandstof, zuurstof én warmte. Nooit water op brandend vet.",
        "Smelten kan je terugdraaien, verbranden niet.",
        "Meng nooit iets waarvan je het etiket niet gelezen hebt.",
    ])

BUNDELS["natuurkunde-energie-en-krachten"] = dict(
    vak=VAK, titel="Natuurkunde: energie en krachten",
    onder="Wat dingen doet bewegen, hoe je slim kracht wint, en waar energie vandaan komt.",
    secties=[
        dict(kop="Krachten", blokken=[
            ("p", "Een kracht is een <strong>duw of een trek</strong>. Je ziet een kracht nooit zelf, "
                  "wel wat ze doet: iets gaat bewegen, stoppen, sneller gaan, van richting veranderen "
                  "of van vorm veranderen — denk aan een spons die je indrukt."),
            ("fig", tabel(["Kracht", "Wat je ervan merkt"], [
                ["zwaartekracht", "alles valt naar beneden"],
                ["wrijving", "een bal rolt uit en stopt"],
                ["spierkracht", "jij duwt of trekt zelf"],
                ["magnetische kracht", "een magneet trekt ijzer aan"],
                ["veerkracht", "een elastiek springt terug"],
            ]), "Een kracht druk je uit in newton, afgekort N, genoemd naar Isaac Newton."),
            ("p", "Trekken twee ploegen even hard aan hetzelfde touw, maar in tegengestelde richting, "
                  "dan beweegt er niets: de krachten houden elkaar in <strong>evenwicht</strong>. Pas "
                  "als één ploeg harder trekt, komt er beweging."),
        ]),
        dict(kop="Zwaartekracht, massa en gewicht", blokken=[
            ("p", "De <strong>zwaartekracht</strong> trekt alles naar de aarde toe. Op de maan is die "
                  "kracht ongeveer zes keer kleiner. Je <strong>massa</strong> — hoeveel materie er in "
                  "je zit — blijft daar gelijk, maar je <strong>gewicht</strong> wordt kleiner: de "
                  "weegschaal wijst minder aan."),
            ("weetje", "Een zwaar voorwerp valt <em>niet</em> sneller dan een licht voorwerp. Laat een "
                       "steen en een propje papier samen vallen en het lijkt wel zo, maar dat komt door "
                       "de luchtweerstand. Zonder lucht komen ze samen aan."),
        ]),
        dict(kop="Slim kracht winnen", blokken=[
            ("p", "Met een <strong>hefboom</strong> til je iets zwaars met minder kracht. Het punt "
                  "waarrond de hefboom draait, heet het <strong>steunpunt</strong>. Hoe verder van het "
                  "steunpunt je duwt, hoe makkelijker het gaat."),
            ("fig", svg.hefboom(400), "Een wip, een kruiwagen, een schaar en een flesopener zijn allemaal hefbomen."),
            ("fig", tabel(["Hulpmiddel", "Wat je wint", "Wat je inlevert"], [
                ["hefboom", "kracht", "je moet je kant veel verder duwen"],
                ["katrol aan een balk", "een handigere richting: trekken in plaats van tillen", "niets, de kracht blijft even groot"],
                ["meerdere katrollen", "kracht", "je moet veel meer touw binnenhalen"],
                ["hellend vlak", "kracht", "je legt een veel langere weg af"],
            ]), "Daarom slingert een bergweg heen en weer in plaats van recht omhoog te gaan."),
        ]),
        dict(kop="Wrijving en luchtweerstand", blokken=[
            ("p", "<strong>Wrijving</strong> ontstaat waar twee dingen langs elkaar schuiven. Soms is ze "
                  "lastig, soms onmisbaar: zonder wrijving kan je niet stappen en niet remmen. Op glad "
                  "ijs merk je meteen wat er gebeurt als ze wegvalt. De remmen van je fiets werken er "
                  "net op."),
            ("p", "Wil je wrijving <strong>kleiner</strong> maken, dan smeer je met olie of zet je er "
                  "wieltjes onder — rollen gaat veel makkelijker dan schuiven."),
            ("p", "Ook lucht remt af. Dat heet <strong>luchtweerstand</strong>. Een parachute vangt met "
                  "zijn grote doek veel lucht en remt de val af; een raceauto heeft juist een gladde, "
                  "<strong>gestroomlijnde</strong> vorm zodat de lucht netjes langs hem glijdt."),
        ]),
        dict(kop="Drijven, zinken en druk", blokken=[
            ("p", "Water duwt van onderaf terug: dat is de <strong>opwaartse kracht</strong>. Daarom "
                  "voelt een steen onder water lichter aan. Een boot van staal drijft omdat hij vanbinnen "
                  "hol is: schip én lucht samen zijn lichter dan het water dat ze verplaatsen. Een massieve "
                  "spijker van datzelfde staal zinkt wel."),
            ("p", "<strong>Druk</strong> is kracht verdeeld over een oppervlak. Dezelfde kracht op een "
                  "groter oppervlak geeft minder druk — daarom zak je met sneeuwschoenen minder diep weg. "
                  "Een naald doet net het omgekeerde: alle kracht op één piepklein puntje."),
        ]),
        dict(kop="Beweging", blokken=[
            ("p", "<strong>Snelheid</strong> is altijd afstand gedeeld door tijd. Fiets je 12 kilometer "
                  "in 1 uur, dan is dat 12 km per uur; doe je er 2 uur over, dan 6 km per uur."),
            ("p", "Alles wat beweegt, wil vanzelf verder bewegen. Dat heet <strong>traagheid</strong>. "
                  "Remt de auto waarin je zit plots, dan vliegt jouw lichaam door aan dezelfde snelheid. "
                  "Daarvoor dient de veiligheidsgordel."),
            ("weetje", "Duw je iets weg, dan duwt het even hard terug. Laat een opgeblazen ballon los: "
                       "de lucht spuit er achteraan uit en de ballon schiet de andere kant op. Een raket "
                       "werkt precies zo, ook in de lege ruimte."),
        ]),
        dict(kop="Energie", blokken=[
            ("p", "Energie is wat nodig is om iets te laten gebeuren. Ze gaat <strong>nooit "
                  "verloren</strong>, ze verandert alleen van vorm."),
            ("fig", tabel(["Vorm van energie", "Waar je ze tegenkomt"], [
                ["bewegingsenergie", "alles wat beweegt: een fietser, een bal"],
                ["hoogte-energie", "een bal bovenaan een helling, water in een stuwmeer"],
                ["chemische energie", "in je boterham, in benzine, in een batterij"],
                ["warmte-energie", "een kachel, een warme motor"],
                ["elektrische energie", "alles wat aan het stopcontact hangt"],
                ["licht- en geluidsenergie", "een lamp, een luidspreker"],
            ]), None),
            ("fig", svg.stappen(["Zon|licht", "Zonnepaneel|elektriciteit", "Lamp|licht en warmte"], kleur=svg.AMBER),
             "Bij elke omzetting gaat een deel als warmte weg. Daarom wordt een lamp warm, en je gsm ook."),
        ]),
        dict(kop="Waar onze energie vandaan komt", blokken=[
            ("fig", tabel(["Hernieuwbaar", "Niet hernieuwbaar"], [
                ["zon, wind, water", "steenkool, aardolie, aardgas"],
                ["raakt niet op", "raakt op, en geeft CO₂ bij het verbranden"],
            ]), "Steenkool, aardolie en aardgas heten fossiele brandstoffen: ze ontstonden miljoenen jaren geleden uit resten van planten en dieren."),
            ("p", "Een <strong>zonnepaneel</strong> zet licht om in elektriciteit. Een "
                  "<strong>waterkrachtcentrale</strong> vangt de energie van stromend water op met een "
                  "turbine, en een windmolen doet hetzelfde met wind."),
            ("p", "Energie besparen doe je thuis het meest bij de <strong>verwarming</strong>: een "
                  "graadje lager en een goed geïsoleerd dak sparen meer dan al je lampjes samen."),
        ]),
        dict(kop="Warmte", blokken=[
            ("p", "Warmte gaat <strong>altijd van warm naar koud</strong>. Je hand wordt niet koud door "
                  "de ijsblok: de warmte van je hand gaat naar het ijs. Het voelt alleen andersom."),
            ("fig", tabel(["Manier", "Hoe het gaat", "Voorbeeld"], [
                ["geleiding", "door een materiaal heen", "een metalen lepel in de soep"],
                ["stroming", "warme lucht of vloeistof verplaatst zich", "warme lucht stijgt op boven een radiator"],
                ["straling", "dwars door de lege ruimte", "de warmte van de zon"],
            ]), None),
            ("p", "Een dikke winterjas houdt je warm omdat er veel <strong>stilstaande lucht</strong> in "
                  "zit, en die laat warmte slecht door. Dubbel glas en de vacht van een dier werken op "
                  "datzelfde idee."),
            ("weetje", "Bijna alles <strong>zet uit</strong> als het warmer wordt en krimpt als het "
                       "afkoelt. Een metalen staaf wordt langer, en in een thermometer kruipt de "
                       "vloeistof daardoor omhoog."),
        ]),
    ],
    onthoud=[
        "Een kracht is een duw of een trek, en je drukt ze uit in newton.",
        "Massa blijft overal gelijk; gewicht hangt af van de zwaartekracht ter plaatse.",
        "Bij een hefboom en een hellend vlak win je kracht en verlies je afstand.",
        "Zonder wrijving kan je niet stappen en niet remmen.",
        "De opwaartse kracht laat een holle boot van staal drijven.",
        "Druk is kracht per oppervlak: sneeuwschoenen spreiden, een naald concentreert.",
        "Snelheid = afstand gedeeld door tijd. Traagheid is waarom je een gordel draagt.",
        "Energie gaat niet verloren, ze verandert van vorm — en een deel wordt altijd warmte.",
        "Zon, wind en water zijn hernieuwbaar; steenkool, aardolie en aardgas niet.",
        "Warmte gaat altijd van warm naar koud, door geleiding, stroming of straling.",
    ])

BUNDELS["natuurkunde-licht-geluid-en-elektriciteit"] = dict(
    vak=VAK, titel="Natuurkunde: licht, geluid en elektriciteit",
    onder="Drie dingen die je niet kan vastpakken, en die toch overal zijn.",
    secties=[
        dict(kop="Licht gaat rechtdoor", blokken=[
            ("p", "Licht verplaatst zich in <strong>rechte lijnen</strong>. Precies daarom krijg je een "
                  "schaduw: het licht kan niet om een voorwerp heen buigen."),
            ("fig", svg.schaduw(),
             "Staat het voorwerp dichter bij de lamp, dan houdt het een breder deel van de bundel tegen en wordt de schaduw groter."),
            ("p", "Niet alles wat licht geeft, is een <strong>lichtbron</strong>. De zon en een lamp "
                  "maken zelf licht. De maan, een spiegel en een witte muur niet: die kaatsen het licht "
                  "van iets anders terug."),
            ("weetje", "Licht gaat ongeveer 300 000 kilometer per seconde. Het licht van de zon doet er "
                       "zo'n acht minuten over om bij ons te raken. Niets gaat sneller dan licht."),
        ]),
        dict(kop="Weerkaatsing", blokken=[
            ("fig", svg.spiegel_weerkaatsing(),
             "De hoek waaronder het licht aankomt, is precies de hoek waaronder het weer vertrekt."),
            ("p", "Waarom zie je jezelf wel in een spiegel en niet in een witte muur? Een spiegel is zo "
                  "glad dat alle stralen netjes in dezelfde richting terugkaatsen. Een ruwe muur strooit "
                  "het licht alle kanten op: je ziet hem wel, maar er staat geen beeld in."),
        ]),
        dict(kop="Breking en lenzen", blokken=[
            ("fig", svg.breking(),
             "Het rietje is kaarsrecht. Het licht verandert van richting waar het het water verlaat, en dus zie je een knik."),
            ("p", "Datzelfde verschijnsel maakt een zwembad ondieper dan het is. En het is ook wat een "
                  "<strong>lens</strong> doet: die buigt lichtstralen zodat je iets groter of scherper "
                  "ziet. In je oog zit er ook een; werkt die niet helemaal goed, dan helpt een bril de "
                  "stralen op de juiste plek samen te brengen."),
            ("weetje", "Kijk <strong>nooit</strong> met een verrekijker of telescoop naar de zon. Die "
                       "bundelt het zonlicht en kan je ogen in één seconde blijvend beschadigen."),
        ]),
        dict(kop="Kleuren", blokken=[
            ("p", "Wit licht is een <strong>mengsel van alle kleuren</strong>. Laat je het door een "
                  "prisma vallen, dan splitst het in de kleuren van de regenboog. Regendruppels doen "
                  "precies hetzelfde, en dan zie je een regenboog aan de hemel."),
            ("p", "Gras ziet er groen uit omdat het het groene licht <strong>terugkaatst</strong> en de "
                  "andere kleuren opslikt. De kleur die je ziet, is dus net de kleur die een voorwerp "
                  "niet houdt. Iets zwarts slikt bijna alles op, en wordt daarom warm in de zon."),
            ("fig", tabel(["Soort materiaal", "Wat het met licht doet", "Voorbeeld"], [
                ["doorzichtig", "licht gaat erdoor, je ziet het beeld", "helder glas, water"],
                ["doorschijnend", "licht gaat erdoor, maar het beeld niet", "melkglas, vetvrij papier"],
                ["ondoorzichtig", "licht wordt tegengehouden", "een muur, hout, je hand"],
            ]), None),
        ]),
        dict(kop="Geluid is trilling", blokken=[
            ("p", "Geluid ontstaat doordat iets <strong>trilt</strong>. Leg je hand op je keel terwijl "
                  "je praat, dan voel je het. Bij een trommel trilt het strakke vel, bij een gitaar de "
                  "snaar, bij een fluit de lucht in de buis."),
            ("fig", svg.geluidsgolf(),
             "Een geluid is altijd een trilling. Deze twee dingen kan je er los van elkaar aan veranderen."),
            ("p", "Hoe luid een geluid is, druk je uit in <strong>decibel</strong>. Een gesprek zit rond "
                  "60 decibel, een drukke straat rond 80. Vanaf ongeveer 85 decibel wordt lang luisteren "
                  "schadelijk."),
            ("weetje", "Gehoorschade herstelt niet: de haarcelletjes in je oor die kapot gaan, groeien "
                       "nooit meer terug. Zet je koptelefoon dus niet voluit, en draag oordopjes op een "
                       "festival."),
        ]),
        dict(kop="Hoe geluid reist", blokken=[
            ("p", "Geluid heeft altijd een <strong>stof</strong> nodig om zich voort te planten: lucht, "
                  "water of iets vasts. In de ruimte, waar geen lucht is, hoor je niets. Door water gaat "
                  "geluid sneller dan door lucht, en door een vaste stof nog sneller — vroeger legde men "
                  "zijn oor op de rails."),
            ("p", "Hoe verder je van de bron staat, hoe zachter je het hoort. En geluid <strong>kaatst "
                  "terug</strong>: tegen een muur of een rots krijg je een <strong>echo</strong>. In een "
                  "lege kamer galmt het, want kale muren kaatsen terug terwijl zachte spullen het geluid "
                  "opslorpen."),
            ("weetje", "Licht gaat veel sneller dan geluid. Daarom zie je de bliksem eerst en hoor je de "
                       "donder pas daarna. Geluid legt ongeveer een kilometer per drie seconden af: tel "
                       "de seconden, deel door drie, en je weet hoe ver het onweer is."),
        ]),
        dict(kop="De stroomkring", blokken=[
            ("p", "Stroom loopt alleen door een <strong>gesloten kring</strong>. Zit er ergens een "
                  "onderbreking, dan gebeurt er niets. Een <strong>schakelaar</strong> is niets anders "
                  "dan een onderbreking die je zelf kan maken en opheffen."),
            ("fig", svg.stroomkring(380), "Open kring, geen licht."),
            ("p", "Een batterij heeft altijd een <strong>pluspool</strong> en een "
                  "<strong>minpool</strong>. Zet je haar omgekeerd in een zaklamp, dan werkt ze meestal "
                  "niet. Spanning druk je uit in <strong>volt</strong>: een gewone batterij geeft 1,5 volt."),
        ]),
        dict(kop="In serie of parallel", blokken=[
            ("fig", svg.serie_parallel(),
             "Hetzelfde aantal lampjes, een heel ander gevolg als er één stuk gaat."),
            ("p", "Daarom staat in een huis alles parallel geschakeld. Anders viel bij één kapotte lamp "
                  "het hele huis in het donker."),
        ]),
        dict(kop="Geleiders, isolatoren en veiligheid", blokken=[
            ("p", "<strong>Metalen geleiden</strong> stroom, en daarom zijn de draden van metaal. "
                  "Plastic, rubber, glas en hout geleiden niet: dat zijn <strong>isolatoren</strong>, en "
                  "die zitten er net rond als bescherming."),
            ("p", "Bij een <strong>kortsluiting</strong> neemt de stroom een veel te korte weg en wordt "
                  "hij veel te groot. De draden worden dan gloeiend heet. Daarom zit er een "
                  "<strong>zekering</strong> of automaat in je huis: die onderbreekt de stroom als hij "
                  "te groot wordt. Beter dat een zekering doorslaat dan dat de draden gaan smeulen."),
            ("weetje", "Uit het stopcontact komt 230 volt, en dat is levensgevaarlijk. Proeven doe je "
                       "<strong>uitsluitend</strong> met een batterij."),
            ("p", "Een <strong>ledlamp</strong> geeft evenveel licht met veel minder stroom dan een "
                  "gloeilamp. Een gloeilamp maakt van bijna alle stroom warmte en maar een beetje licht; "
                  "bij een led is dat net omgekeerd."),
        ]),
        dict(kop="Magneten en elektriciteit", blokken=[
            ("fig", svg.staafmagneet(), None),
            ("p", "Een magneet trekt <strong>ijzer</strong> aan, en ook nikkel en kobalt. Hout, glas, "
                  "plastic en de meeste andere metalen niet. Een kompasnaald wijst naar het noorden "
                  "omdat de <strong>aarde zelf als een grote magneet werkt</strong>."),
            ("p", "Magnetisme en elektriciteit horen bij elkaar. Wikkel je een draad rond een ijzeren "
                  "staaf en laat je er stroom door lopen, dan heb je een <strong>elektromagneet</strong>. "
                  "Het handige eraan: zet je de stroom af, dan is de magneet weg. Zo tilt een kraan op "
                  "een schroothoop auto's op en laat ze weer los."),
            ("p", "Het werkt ook omgekeerd: beweeg je een magneet langs een spoel, dan ontstaat er "
                  "stroom. Dat is wat de <strong>dynamo</strong> op je fiets doet, en wat in een "
                  "windmolen en een waterkrachtcentrale gebeurt. Beweging erin, stroom eruit."),
        ]),
    ],
    onthoud=[
        "Licht gaat in rechte lijnen; daarom krijg je een schaduw.",
        "Op een spiegel kaatst licht terug onder dezelfde hoek als het aankwam.",
        "Licht breekt als het van water naar lucht gaat — vandaar het 'geknikte' rietje.",
        "Wit licht bestaat uit alle kleuren. Je ziet de kleur die een voorwerp terugkaatst.",
        "Geluid is trilling: sneller trillen klinkt hoger, groter trillen klinkt luider.",
        "Geluid heeft lucht, water of een vaste stof nodig. In de ruimte hoor je niets.",
        "Licht gaat veel sneller dan geluid: eerst de bliksem, dan de donder.",
        "Stroom loopt alleen door een gesloten kring.",
        "In serie: één lampje stuk en alles gaat uit. Parallel: de rest brandt door.",
        "Metalen geleiden, plastic en rubber isoleren. Een zekering breekt de kring bij te veel stroom.",
        "Gelijke polen van een magneet stoten af, verschillende trekken aan.",
        "Beweging kan stroom maken: dat doet een dynamo.",
    ])

BUNDELS["techniek-ontwerpen-en-maken"] = dict(
    vak=VAK, titel="Techniek: ontwerpen en maken",
    onder="Van een probleem naar iets dat werkt — en waarom het zelden in één keer lukt.",
    secties=[
        dict(kop="De ontwerpcyclus", blokken=[
            ("p", "Techniek begint nooit bij een idee, maar bij een <strong>probleem</strong>. Daarna "
                  "doorloop je telkens dezelfde stappen — en na de laatste begin je vaak opnieuw."),
            ("fig", svg.ontwerpcyclus(380), "Dat het na het testen terugkeert naar het begin, is geen mislukking. Zo hoort het."),
            ("p", "Vóór je begint te tekenen, maak je een <strong>programma van eisen</strong>: de lijst "
                  "met wat je ontwerp moet kunnen. Bijvoorbeeld: het moet 20 kg dragen, in een rugzak "
                  "passen en niet meer dan 10 euro kosten. Achteraf kan je eraan aftoetsen of het gelukt is."),
            ("p", "Een eerste versie om mee te testen heet een <strong>prototype</strong>. Dat maak je "
                  "vaak uit karton of piepschuim: een fout ontdekken in karton kost tien minuten, "
                  "diezelfde fout in metaal kost je het hele werkstuk. Werkt je test niet, dan ga je na "
                  "wat er misloopt, past dat aan en test je opnieuw."),
        ]),
        dict(kop="Tekenen en meten", blokken=[
            ("p", "Een <strong>schets</strong> maak je snel uit de hand, om ideeën te vergelijken. Kies "
                  "je er één, dan maak je een <strong>technische tekening</strong>: met juiste maten en "
                  "op schaal. Staat er schaal 1:10 bij, dan is alles in het echt tien keer groter dan op "
                  "het blad."),
            ("p", "Maten zet je meestal in <strong>millimeter</strong>. Zo hoef je geen kommagetallen te "
                  "gebruiken, en dat scheelt fouten: 1 250 mm leest duidelijker dan 1,25 m."),
            ("fig", tabel(["Gereedschap", "Waarvoor"], [
                ["meetlat of rolmeter", "afstanden meten"],
                ["winkelhaak", "nagaan of een hoek precies recht is"],
                ["waterpas", "nagaan of iets horizontaal staat"],
                ["potlood en priem", "aftekenen waar je moet zagen of boren"],
            ]), "Meet twee keer, zaag één keer: je kan er achteraf niets weer aanplakken."),
        ]),
        dict(kop="Materiaal kiezen", blokken=[
            ("p", "Elk materiaal heeft eigenschappen die het geschikt of ongeschikt maken. Je kiest op "
                  "basis van wat je voorwerp moet kunnen."),
            ("fig", tabel(["Materiaal", "Sterk punt", "Zwak punt"], [
                ["hout", "sterk, makkelijk te bewerken", "rot in water"],
                ["metaal", "heel sterk, geleidt stroom", "zwaar, kan roesten"],
                ["kunststof", "licht, goedkoop, roest niet", "slecht voor het milieu"],
                ["glas", "doorzichtig", "breekt makkelijk"],
                ["textiel", "soepel, licht", "scheurt, houdt niet tegen"],
            ]), "Een fietsframe uit glas zou doorzichtig zijn, maar één keer bruikbaar."),
        ]),
        dict(kop="Verbinden", blokken=[
            ("fig", tabel(["Verbinding", "Los te maken?", "Waarvoor"], [
                ["schroef of bout", "ja", "alles wat je ooit wil herstellen of demonteren"],
                ["scharnier", "beweegt", "een deur, een bril, een laptop"],
                ["nagel", "moeilijk", "snel timmerwerk"],
                ["lijm", "nee", "grote vlakken, of materiaal dat je niet wil doorboren"],
                ["lassen of klinken", "nee", "metaal dat veel kracht moet dragen"],
            ]), "Een schroef houdt in hout veel beter vast dan een gladde nagel: de schroefdraad bijt zich in het hout."),
            ("p", "Wil je iets ooit herstellen of recycleren, kies dan een <strong>losneembare</strong> "
                  "verbinding. Gelijmd en gelast krijg je er niet meer netjes uit."),
        ]),
        dict(kop="Constructies stevig maken", blokken=[
            ("p", "De <strong>driehoek</strong> is de stevigste vorm die er is: hij kan niet vervormen "
                  "zonder dat er een zijde breekt. Een vierkant kan wel scheeftrekken. Zet een schuine "
                  "balk in een vierkant en je hebt twee driehoeken, en dus iets dat stevig staat."),
            ("p", "Daarom zie je driehoeken in bruggen, kraanarmen, daken en steigers."),
            ("p", "Een tweede truc: een <strong>holle buis</strong> is vaak steviger dan een even zware "
                  "volle staaf. Het materiaal zit verder van het midden, en net daar telt het mee tegen "
                  "doorbuigen. Daarom zijn fietsframes en steigers uit buizen gemaakt."),
        ]),
        dict(kop="Beweging doorgeven", blokken=[
            ("fig", tabel(["Overbrenging", "Waar je het ziet", "Wat het doet"], [
                ["tandwielen", "een klok, een boormachine", "draaien in elkaar, tegengestelde richting"],
                ["ketting", "een fiets", "draaien in dezelfde richting, over afstand"],
                ["riem", "een wasmachine", "zachter en stiller dan een ketting"],
                ["katrol", "een takel", "tillen met minder kracht"],
            ]), None),
            ("p", "Drijft een <strong>klein</strong> tandwiel een <strong>groot</strong> aan, dan draait "
                  "dat grote trager maar met meer kracht. Omgekeerd draait een klein wiel sneller en met "
                  "minder kracht. Dat is precies wat de versnellingen van je fiets doen."),
            ("p", "Een ketting kan meer kracht doorgeven en slipt niet, maar maakt lawaai en heeft olie "
                  "nodig. Een riem loopt stiller en soepeler. Op een fiets kies je dus een ketting, in "
                  "een wasmachine een riem."),
        ]),
        dict(kop="Elektriciteit en sturing", blokken=[
            ("p", "Een <strong>schakelaar</strong> opent of sluit een stroomkring, en een "
                  "<strong>zekering</strong> onderbreekt hem als de stroom te groot wordt."),
            ("p", "Een <strong>sensor</strong> meet iets — licht, warmte, beweging, afstand — zodat een "
                  "toestel erop kan reageren. Een straatlantaarn met een lichtsensor gaat vanzelf aan "
                  "als het donker wordt."),
            ("p", "Een <strong>robot</strong> doet precies wat er in zijn programma staat, en niets "
                  "anders. Werkt een robot verkeerd, dan zit de fout bijna altijd in het programma of in "
                  "wat de sensoren meten."),
        ]),
        dict(kop="Veilig en netjes werken", blokken=[
            ("fig", tabel(["Regel", "Waarom"], [
                ["meet twee keer, zaag één keer", "je kan er niets weer aanplakken"],
                ["klem je werkstuk vast", "een bewegend stuk hout is gevaarlijk"],
                ["bril op bij zagen of boren", "splinters komen recht op je af"],
                ["lees eerst de gebruiksaanwijzing", "daar staan de veiligheidsregels die je vooraf moet kennen"],
                ["ruim op terwijl je bezig bent", "op een volle tafel gebeuren de ongelukken"],
            ]), None),
        ]),
        dict(kop="Nieuwe manieren van maken", blokken=[
            ("p", "Een <strong>3D-printer</strong> bouwt een voorwerp laagje na laagje op, in plaats van "
                  "het uit een blok te snijden. Daardoor kan hij vormen maken die je met zagen of frezen "
                  "nooit uit één stuk krijgt."),
        ]),
        dict(kop="Techniek, mens en milieu", blokken=[
            ("p", "Een ontwerp is <strong>ergonomisch</strong> als het gemaakt is naar de mens die het "
                  "gebruikt: een schaar voor linkshandigen, een schroevendraaier met een dikke greep. "
                  "Wie het gebruikt, bepaalt dus mee hoe het eruitziet."),
            ("p", "De <strong>levensduur</strong> is hoe lang iets meegaat voor het stuk of onbruikbaar "
                  "is. Een product dat twee keer zo lang meegaat, is voor het milieu bijna twee keer zo "
                  "goed. <strong>Herstellen</strong> gaat dus vóór vervangen — in een repair café helpen "
                  "ze je daarbij."),
            ("p", "De grondstoffen voor een gsm komen uit mijnen, vaak ver weg en soms onder slechte "
                  "werkomstandigheden. <strong>Recycleren</strong> betekent dat een materiaal opnieuw als "
                  "grondstof gebruikt wordt. Daarom is een oude gsm inleveren zoveel waard."),
            ("p", "Elke uitvinding lost iets op en brengt iets nieuws mee. De auto maakte afstanden "
                  "klein, maar bracht files en uitstoot. Wie iets ontwerpt, denkt dus verder dan of het "
                  "werkt: wat kost het aan grondstoffen, hoe lang gaat het mee, en wat gebeurt ermee als "
                  "het kapot is?"),
        ]),
    ],
    onthoud=[
        "Techniek begint bij een probleem, niet bij een idee.",
        "Eerst een programma van eisen, dan schetsen, dan een technische tekening op schaal.",
        "Testen en verbeteren horen bij het ontwerpen; een prototype maak je van goedkoop materiaal.",
        "Kies je materiaal op basis van wat het moet kunnen.",
        "Een schroef is losneembaar, lijm en las niet.",
        "De driehoek is de stevigste vorm; een holle buis is steviger dan een even zware volle staaf.",
        "Een klein tandwiel dat een groot aandrijft: trager, maar met meer kracht.",
        "Een sensor meet, een robot voert alleen zijn programma uit.",
        "Meet twee keer, zaag één keer. Bril op bij zagen of boren.",
        "Herstellen gaat vóór vervangen; recycleren maakt van afval weer grondstof.",
    ])

BUNDELS["de-aarde-en-de-ruimte"] = dict(
    vak=VAK, titel="De aarde en de ruimte",
    onder="Waarom het dag en nacht wordt, waarom er seizoenen zijn, en wat er verder nog rond ons draait.",
    secties=[
        dict(kop="De aarde draait", blokken=[
            ("p", "De aarde draait in <strong>24 uur</strong> één keer rond haar as. De kant die naar de "
                  "zon gekeerd staat, heeft dag; de andere kant heeft nacht."),
            ("fig", svg.dag_en_nacht(),
             "De zon staat stil; wij draaien. Daarom zie je haar 's ochtends in het oosten opkomen en 's avonds in het westen ondergaan."),
            ("p", "Dat de aarde een <strong>bol</strong> is, kan je zelf zien aan zee: een schip dat "
                  "wegvaart, verdwijnt van onder naar boven achter de horizon. Je ziet eerst de romp "
                  "verdwijnen en het laatst de mast. Op een vlakke aarde zou het gewoon steeds kleiner "
                  "worden."),
        ]),
        dict(kop="Rond de zon in een jaar", blokken=[
            ("p", "Tegelijk draait de aarde in een grote baan rond de zon. Daar doet ze ongeveer "
                  "<strong>365 dagen en 6 uur</strong> over, en dat is ons jaar."),
            ("p", "Die zes uur sparen we vier jaar op. Samen is dat één dag, en die zetten we er dan bij "
                  "als <strong>29 februari</strong>: een <strong>schrikkeljaar</strong>. Zonder die "
                  "extra dag zou de kalender langzaam verschuiven ten opzichte van de seizoenen."),
        ]),
        dict(kop="De seizoenen", blokken=[
            ("p", "De seizoenen komen <em>niet</em> doordat de aarde in de zomer dichter bij de zon "
                  "staat. Ze komen doordat de <strong>as van de aarde scheef staat</strong> ten opzichte "
                  "van haar baan — en altijd in dezelfde richting."),
            ("fig", svg.seizoenen(),
             "Staat het noordelijk halfrond naar de zon gekeerd, dan valt het licht hier steil en krachtig: zomer."),
            ("p", "Daarom is het bij ons zomer wanneer het in Australië winter is: het zuidelijk halfrond "
                  "staat dan juist van de zon weg gekeerd. Daar valt Kerstmis midden in de zomer."),
        ]),
        dict(kop="Warm en koud op aarde", blokken=[
            ("fig", svg.aardbolgordels(),
             "Aan de evenaar valt het zonlicht recht op de aarde, aan de polen heel schuin."),
            ("p", "Schuin licht wordt over een veel groter stuk grond uitgesmeerd, en warmt dus veel "
                  "minder op. Dat is de hele reden waarom het aan de evenaar heet is en aan de polen koud."),
        ]),
        dict(kop="De dampkring", blokken=[
            ("p", "Rond de aarde ligt een laag lucht: de <strong>atmosfeer</strong> of dampkring. Ze "
                  "levert de lucht die we ademen, houdt warmte vast en vangt de meeste brokstukken uit "
                  "de ruimte op."),
            ("p", "Het is de <strong>zwaartekracht</strong> van de aarde die die lucht vasthoudt. Zonder "
                  "haar zou onze atmosfeer de ruimte in drijven. De maan is te licht en heeft haar lucht "
                  "dan ook niet kunnen houden."),
        ]),
        dict(kop="De maan", blokken=[
            ("p", "De maan draait om de <strong>aarde</strong>, en reist dus samen met ons om de zon mee. "
                  "Over één rondje doet ze ongeveer een maand — daar komt dat woord vandaan."),
            ("p", "De maan maakt <strong>zelf geen licht</strong>. Ze kaatst het licht van de zon terug. "
                  "Zelf is ze een donkere, grijze bol van steen."),
            ("fig", svg.maanfasen(), None),
            ("weetje", "Op de maan is geen lucht. Er is dus geen wind en geen regen, en daarom staan de "
                       "voetstappen van de astronauten er nog altijd. Horen zou je er ook niets: geluid "
                       "heeft lucht nodig."),
        ]),
        dict(kop="Verduisteringen en getijden", blokken=[
            ("fig", tabel(["Wat", "Wie staat er in het midden", "Wat je ziet"], [
                ["zonsverduistering", "de maan, tussen zon en aarde", "midden op de dag wordt het even schemerdonker"],
                ["maansverduistering", "de aarde, tussen zon en maan", "de maan kleurt koperrood"],
            ]), "Bij een maansverduistering raakt alleen nog rood licht via onze atmosfeer tot bij de maan."),
            ("p", "De maan trekt ook aan het water van de oceanen. Daardoor komt het water tweemaal per "
                  "dag op en gaat het tweemaal per dag terug: <strong>eb en vloed</strong>."),
        ]),
        dict(kop="Ons zonnestelsel", blokken=[
            ("p", "De <strong>zon</strong> is een gewone <strong>ster</strong>, alleen veel dichter bij "
                  "ons dan alle andere. Daarom lijkt zij zo groot en zijn de andere sterren maar puntjes."),
            ("fig", svg.zonnestelsel(),
             "Acht planeten. Pluto telde vroeger mee, maar geldt sinds 2006 als dwergplaneet."),
            ("fig", tabel(["Planeet", "Waarom je ze onthoudt"], [
                ["Mercurius", "staat het dichtst bij de zon"],
                ["Venus", "de heetste planeet: een dikke wolkendeken houdt de warmte vast, meer dan 400 graden"],
                ["aarde", "de derde, en de enige met vloeibaar water en leven"],
                ["Mars", "de rode planeet, door het roestige ijzer in de grond"],
                ["Jupiter", "de grootste: er zouden meer dan duizend aardes in passen"],
                ["Saturnus", "bekend om haar brede ringen van ijs en steen"],
                ["Uranus en Neptunus", "de twee verste, ijskoud en blauwgroen"],
            ]), None),
            ("p", "Wat houdt ze in hun baan? De <strong>zwaartekracht van de zon</strong>. Ze vallen "
                  "eigenlijk voortdurend naar de zon toe, maar ze schuiven er tegelijk zo snel langs dat "
                  "ze er netjes omheen blijven draaien."),
            ("weetje", "Een jaar is één rondje om de zon, en dat duurt dus niet overal even lang. Op "
                       "Mercurius is een jaar 88 aardse dagen, op Neptunus ruim 160 aardse jaren."),
        ]),
        dict(kop="Sterren en het heelal", blokken=[
            ("p", "Een <strong>ster</strong> maakt zelf licht; een <strong>planeet</strong> niet, die "
                  "zie je door weerkaatst sterrenlicht. De sterren die je 's nachts ziet, zijn dus zonnen "
                  "zoals de onze, sommige veel groter. Ze lijken alleen puntjes omdat ze onvoorstelbaar "
                  "ver weg staan."),
            ("p", "Een <strong>sterrenbeeld</strong> is een groepje sterren waarin mensen vroeger een "
                  "figuur zagen. Die sterren horen vaak helemaal niet bij elkaar: de ene staat twee keer "
                  "zo ver als de andere. Het is puur wat je vanaf de aarde ziet."),
            ("p", "Ons zonnestelsel ligt in de <strong>Melkweg</strong>, een sterrenstelsel van "
                  "miljarden sterren. Op een donkere nacht zie je hem als een vage lichtband."),
            ("p", "Afstanden in de ruimte reken je in <strong>lichtjaren</strong>: de afstand die licht "
                  "in één jaar aflegt, ongeveer 9 500 miljard kilometer. Het is dus een afstand, geen tijd."),
            ("weetje", "Overdag staan de sterren er gewoon nog. Je ziet ze niet omdat het zonlicht dat in "
                       "onze atmosfeer verstrooit, veel feller is. Een <strong>telescoop</strong> helpt "
                       "'s nachts door veel meer licht op te vangen: hoe groter de spiegel, hoe zwakker "
                       "de dingen die je nog kan zien."),
        ]),
        dict(kop="De mens in de ruimte", blokken=[
            ("p", "Een <strong>raket</strong> moet loskomen van de zwaartekracht van de aarde en dwars "
                  "door de atmosfeer. Daarvoor is enorm veel kracht nodig: bijna heel de raket is "
                  "brandstof, en onderweg valt ze in stukken uit elkaar zodra die leeg zijn."),
            ("p", "Rond de aarde draaien duizenden <strong>satellieten</strong>, voor gps, "
                  "weersvoorspellingen, televisie en internet. Je gps op de fiets werkt dankzij signalen "
                  "van verschillende satellieten tegelijk."),
            ("p", "In het <strong>ISS</strong>, een ruimtestation ongeveer 400 kilometer boven ons, wonen "
                  "en werken astronauten. Het doet er anderhalf uur over om één keer rond de aarde te gaan."),
            ("p", "Waarom zweven die astronauten? Niet omdat er geen zwaartekracht is — die is daar nog "
                  "bijna even sterk als op de grond. Wel omdat het station en de astronaut "
                  "<strong>samen vallen</strong> rond de aarde. En dat voelt als zweven."),
            ("weetje", "Op 20 juli <strong>1969</strong> zette voor het eerst een mens voet op de maan, "
                       "met de missie Apollo 11. Sindsdien zijn er in totaal twaalf mensen op de maan geweest."),
        ]),
    ],
    onthoud=[
        "De aarde draait in 24 uur rond haar as: dag en nacht.",
        "Eén rondje om de zon duurt 365 dagen en 6 uur; daarom is er om de vier jaar een schrikkeljaar.",
        "De seizoenen komen door de scheve as, niet door de afstand tot de zon.",
        "Aan de evenaar valt het licht recht, aan de polen schuin. Daarom is het daar koud.",
        "De maan draait om de aarde, doet daar ongeveer een maand over en maakt zelf geen licht.",
        "Zonsverduistering: de maan in het midden. Maansverduistering: de aarde in het midden.",
        "Eb en vloed komen door de aantrekking van de maan.",
        "Acht planeten: Mercurius, Venus, aarde, Mars, Jupiter, Saturnus, Uranus, Neptunus.",
        "De zon is een ster. Een ster maakt zelf licht, een planeet niet.",
        "Een lichtjaar is een afstand, niet een tijd.",
        "Astronauten zweven omdat ze samen met hun station rond de aarde vallen.",
        "1969: de eerste mens op de maan.",
    ])

if __name__ == "__main__":
    for naam, b in BUNDELS.items():
        bundel.schrijf(b, naam)

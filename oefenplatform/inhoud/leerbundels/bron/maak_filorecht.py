# -*- coding: utf-8 -*-
"""De leerbundels bij filosofie en recht op 🌍 Beyond doorstroom.

Gebaseerd op de vakfiche `2027_filosofie_en_recht_3DDG`, geldig vanaf
1 januari 2027. Bladzijde 1 zegt voor welke richting ze geldt:
welzijnswetenschappen, en enkel die.

Het examen duurt 120 minuten en is volledig digitaal. De fiche weegt
filosofie op 60 procent en recht op 40 procent; daarom twaalf thema's
filosofie en acht thema's recht.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim laadt de bundel
dus twee keer op, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../beyond/filosofie-en-recht.json`
doet daar het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

WAT HIER VASTLIGT. De fiche noemt ruim veertig filosofen bij naam, en bij de
meeste staat enkel die naam. Zet bij een naam dus niets wat de fiche niet
zegt: geen citaat, geen boektitel, geen experiment. Een verzonnen citaat in de
mond van een echte filosoof is geen voorbeeld maar een vervalsing. Waar de
fiche enkel een naam geeft, staat hier wat die denker in dát debat heeft
ingebracht en niets meer.

Twee dingen die uit de fiche zelf komen en die je niet moet rechtzetten:
de fiche schrijft "Henry Frankfurt" waar de bekende filosoof Harry Frankfurt
heet, en "Filippa Foot" waar zij Philippa Foot heet. In de bundels staat
daarom enkel hun familienaam.

De bundelsleutels eindigen op "-beyond-doorstroom", de slug van de categorie.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Filosofie en recht"
BEYOND = "🌍 Beyond doorstroom — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 1. De eigenheid van de filosofie
BUNDELS["de-eigenheid-van-de-filosofie-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De eigenheid van de filosofie",
    onder="Wat filosofie anders maakt dan wetenschap, waar ze vandaan komt, en hoe je een filosofische vraag herkent.",
    secties=[
        dict(kop="Wat filosofie is, en wat ze niet is", blokken=[
            ("p", "Filosofie betekent letterlijk <strong>liefde voor de wijsheid</strong>. Dat klinkt "
                  "vaag, en toch zit het verschil met de andere vakken er al in: een filosoof bezit de "
                  "wijsheid niet, hij zoekt ze. Hij begint met een vraag en niet met een antwoord."),
            ("p", "De wetenschappen vallen in twee grote groepen uiteen, en de filosofie hoort bij geen "
                  "van beide."),
            ("p", tabel(["Soort", "Wat ze onderzoekt", "Voorbeelden"], [
                ["natuurwetenschappen", "de natuur en haar wetten",
                 "de natuurkunde, de scheikunde, de sterrenkunde, de biologie"],
                ["menswetenschappen", "de mens en de samenleving",
                 "de psychologie, de sociologie, de geschiedenis"],
                ["filosofie", "vragen die je met meten niet beslecht",
                 "wat is rechtvaardig, wat is een mens, wat kan ik weten"],
            ])),
            ("kader", "<strong>Het verschil zit in de methode.</strong> Een wetenschapper beantwoordt zijn "
                      "vraag met waarneming, meting en experiment. Een filosoof kan dat niet: zijn vragen "
                      "laten zich niet meten. Hij werkt met <strong>argumenten</strong>, met "
                      "<strong>begrippen</strong> die hij scherp maakt, en met <strong>redeneringen</strong> "
                      "die je kan nakijken."),
            ("p", "Daarom is filosofie ook geen mening. Een mening mag je hebben; een filosofisch "
                  "standpunt moet je <strong>verdedigen</strong>. Wie geen reden kan geven, heeft wel een "
                  "overtuiging maar nog geen filosofie."),
        ]),
        dict(kop="Van mythologie naar filosofie", blokken=[
            ("p", "Lang voor de filosofie bestond, verklaarden mensen de wereld met <strong>mythen</strong>: "
                  "verhalen waarin goden de donder, de zee en de ziekte veroorzaken. Zo'n verhaal verklaart "
                  "alles, en precies daarom kan je het nergens op nakijken."),
            ("p", "In het oude Griekenland komt daar verandering in. De eerste denkers zoeken een "
                  "verklaring <strong>binnen de natuur zelf</strong>, zonder naar de goden te wijzen. Die "
                  "stap heet de <strong>natuurfilosofie</strong>, en daarmee begint de westerse filosofie."),
            ("p", tabel(["", "Mythologie", "Natuurfilosofie"], [
                ["verklaring", "de wil van de goden", "oorzaken in de natuur zelf"],
                ["houding", "het verhaal aanvaarden", "de verklaring bevragen"],
                ["te toetsen?", "nee", "ja, met argumenten en later met onderzoek"],
            ])),
            ("weetje", "Uit diezelfde natuurfilosofie zijn later álle wetenschappen gegroeid. Wat wij "
                       "vandaag natuurkunde noemen, heette eeuwenlang gewoon filosofie van de natuur."),
        ]),
        dict(kop="Verwondering, en wat een filosofische vraag is", blokken=[
            ("p", "Filosofie begint bij <strong>verwondering</strong>: je staat stil bij iets dat voor "
                  "iedereen vanzelfsprekend is. Waarom is er iets en niet niets? Waarom vinden wij dit "
                  "eerlijk? Wie zich nergens meer over verwondert, stelt ook geen vragen meer."),
            ("p", "Een filosofische vraag herken je aan drie dingen tegelijk:"),
            ("p", tabel(["Kenmerk", "Wat het betekent"], [
                ["niet met meten te beslechten", "geen enkel experiment geeft het antwoord"],
                ["over begrippen en waarden", "wat bedoelen wij eigenlijk met vrijheid, geluk, recht?"],
                ["het antwoord blijft bevraagbaar", "een goed antwoord roept nieuwe vragen op"],
            ])),
            ("kader", "<strong>Een feitenvraag of een filosofische vraag?</strong> Hoeveel mensen liegen, "
                      "is een feitenvraag: dat kan je onderzoeken. Of liegen hier mag, is een filosofische "
                      "vraag. Leer dat onderscheid vlot maken, want het komt in elk thema terug."),
            ("p", "De filosofie werkt in verschillende <strong>domeinen</strong>, en die van deze fiche "
                  "zijn er drie: de <strong>kenleer</strong> (wat kunnen wij weten), de "
                  "<strong>wijsgerige antropologie</strong> (wat is een mens) en de "
                  "<strong>ethiek</strong> (wat is goed handelen). De argumentatieleer loopt er als "
                  "gereedschap doorheen."),
        ]),
    ],
    onthoud=[
        "Filosofie is liefde voor de wijsheid: je begint met een vraag, niet met een antwoord.",
        "Natuurwetenschappen onderzoeken de natuur, menswetenschappen de mens; filosofie stelt vragen die je niet kan meten.",
        "Haar methode is argumenteren en begrippen scherp maken, niet meten.",
        "Mythologie verklaart met goden, natuurfilosofie zoekt oorzaken in de natuur zelf. Daar begint de westerse filosofie.",
        "Filosofie begint bij verwondering over wat vanzelfsprekend lijkt.",
        "Een feitenvraag kan je onderzoeken; een filosofische vraag gaat over begrippen en waarden.",
    ],
)

# ───────────────────────── 2. Bronnen van kennis, rationalisme en empirisme
BUNDELS["bronnen-van-kennis-rationalisme-en-empirisme-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Bronnen van kennis, rationalisme en empirisme",
    onder="Waar onze kennis vandaan komt, waarom elke bron kan haperen, en het verschil tussen rationalisme en empirisme.",
    secties=[
        dict(kop="De vijf bronnen van kennis", blokken=[
            ("p", "Hoe weet je wat je weet? De fiche somt vijf <strong>bronnen van kennis</strong> op. "
                  "Bij elke bron hoort een manier waarop ze je kan bedriegen, en dat tweede is het "
                  "belangrijkste om te kennen."),
            ("p", tabel(["Bron", "Wat ze doet", "Waar ze hapert"], [
                ["zintuigen", "je ziet, hoort en voelt de wereld",
                 "een zinsbegoocheling, een stok die in het water geknikt lijkt"],
                ["afleiding", "je leidt uit wat je weet iets nieuws af",
                 "een redenering die klopt, maar van een onware premisse vertrekt"],
                ["geheugen", "je herinnert je wat er gebeurd is",
                 "herinneringen verschuiven en vullen zichzelf aan"],
                ["introspectie", "je kijkt naar je eigen denken en voelen",
                 "je kan je over je eigen beweegredenen vergissen"],
                ["verhalen", "je verneemt van anderen wat jij niet zag",
                 "je kan de bron niet zelf nakijken"],
            ])),
            ("kader", "<strong>Verreweg het meeste van wat jij weet, komt uit verhalen van anderen.</strong> "
                      "Dat de aarde om de zon draait, heb je niet zelf vastgesteld. Daarom is de vraag "
                      "welke bron betrouwbaar is, geen schoolse vraag maar een dagelijkse."),
        ]),
        dict(kop="De grotallegorie", blokken=[
            ("p", "De bekendste vertelling over kennis is de <strong>grotallegorie</strong> van Plato. "
                  "Mensen zitten vastgeketend in een grot, met hun rug naar de uitgang. Op de wand voor "
                  "hen zien ze schaduwen, en die schaduwen houden ze voor de werkelijkheid."),
            ("p", "Komt er één los en draait hij zich om, dan ziet hij dat die beelden maar schaduwen "
                  "waren. Gaat hij naar buiten, dan verblindt het licht hem eerst. En vertelt hij het "
                  "binnen, dan geloven de anderen hem niet."),
            ("kader", "<strong>Waar het om gaat:</strong> wat je dagelijks waarneemt, hoeft niet de hele "
                      "werkelijkheid te zijn. Het verhaal waarschuwt tegelijk dat wie iets anders komt "
                      "vertellen, op weerstand botst."),
        ]),
        dict(kop="Rationalisme: de rede als bron", blokken=[
            ("p", "Het <strong>rationalisme</strong> zegt dat zekere kennis uit de <strong>rede</strong> "
                  "komt en niet uit de zintuigen. De grote naam is <strong>René Descartes</strong>."),
            ("p", "Zijn werkwijze heet de <strong>methodische twijfel</strong>: hij twijfelt met opzet aan "
                  "alles wat ook maar een beetje onzeker is, om te zien wat overblijft. Zijn zintuigen "
                  "bedriegen hem soms, dus die gaan eruit. Zijn dromen voelen echt, dus ook de buitenwereld "
                  "gaat eruit. Wat blijft staan, is dat hij twijfelt, en dus dat hij denkt."),
            ("p", "Het rationalisme redeneert met <strong>deductie</strong>: van een algemene regel naar "
                  "een bijzonder geval. Alle mensen zijn sterfelijk, jij bent een mens, dus jij bent "
                  "sterfelijk. Als de regel klopt, is het besluit zeker."),
        ]),
        dict(kop="Empirisme: de ervaring als bron", blokken=[
            ("p", "Het <strong>empirisme</strong> zegt het omgekeerde: alle kennis begint bij de "
                  "<strong>ervaring</strong>. De namen hier zijn <strong>John Locke</strong> en "
                  "<strong>David Hume</strong>."),
            ("p", "Locke staat voor de gedachte dat een mens bij zijn geboorte nog geen kennis "
                  "meebrengt: de ervaring moet alles aanbrengen. Hume onderzoekt vooral waar onze kennis "
                  "haar grenzen heeft."),
            ("p", "Het empirisme redeneert met <strong>inductie</strong>: van losse waarnemingen naar een "
                  "algemene regel. Elke zwaan die ik zag was wit, dus alle zwanen zijn wit. Handig, maar "
                  "nooit zeker: één zwarte zwaan volstaat om de regel om te gooien."),
            ("p", tabel(["", "Rationalisme", "Empirisme"], [
                ["bron van kennis", "de rede", "de ervaring"],
                ["naam", "Descartes", "Locke en Hume"],
                ["redeneert met", "deductie, van algemeen naar bijzonder",
                 "inductie, van bijzonder naar algemeen"],
                ["zekerheid", "zeker als de premissen kloppen", "nooit helemaal zeker"],
            ])),
            ("weetje", "De twee sluiten elkaar niet uit. De moderne wetenschap doet allebei: ze "
                       "bedenkt met de rede een hypothese en toetst die aan de ervaring."),
        ]),
        dict(kop="Je argument opbouwen met AUB", blokken=[
            ("p", "Om een argument goed uit te leggen gebruikt de fiche de <strong>AUB-methode</strong>, "
                  "drie stappen die je ook op het examen kan zetten."),
            ("p", tabel(["Stap", "Wat je doet", "Hoe je begint"], [
                ["A — argument", "je noemt je argument", "mijn argument is dat ..."],
                ["U — uitleg", "je legt uit waarom het zo is en waarom dat goed of slecht is",
                 "want ... / dit is goed, want ..."],
                ["B — bijvoorbeeld", "je geeft zelf een voorbeeld", "stel je voor ..."],
            ])),
            ("p", "Daarnaast onderscheidt de fiche <strong>soorten argumenten</strong>: een feitelijk "
                  "argument, een gezagsargument, een argument op basis van een kenmerk, van een voorbeeld, "
                  "van een vergelijking, van voor- en nadelen, en van een oorzaak-gevolgrelatie."),
        ]),
    ],
    onthoud=[
        "Vijf bronnen van kennis: zintuigen, afleiding, geheugen, introspectie en verhalen van anderen.",
        "Verreweg het meeste van wat je weet, komt uit verhalen die je zelf niet kan nakijken.",
        "De grotallegorie: wat je waarneemt, hoeft de werkelijkheid niet te zijn.",
        "Rationalisme = de rede (Descartes, methodische twijfel, deductie).",
        "Empirisme = de ervaring (Locke en Hume, inductie). Inductie geeft nooit volle zekerheid.",
        "AUB: argument, uitleg, bijvoorbeeld.",
    ],
)

# ───────────────────────── 3. Van natuurfilosofie naar wetenschap
BUNDELS["van-natuurfilosofie-naar-wetenschap-falsificatie-en-demarcatie-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Van natuurfilosofie naar wetenschap: falsificatie en demarcatie",
    onder="Hoe de wetenschap uit de filosofie groeide, waar de grens met pseudowetenschap ligt, en hoe je een filosofische tekst leest.",
    secties=[
        dict(kop="Hoe de wetenschap uit de filosofie groeide", blokken=[
            ("p", "De natuurfilosofie zocht verklaringen in de natuur zelf. Daaruit is in de loop van "
                  "eeuwen de <strong>wetenschap</strong> gegroeid, met een eigen manier van werken: "
                  "waarnemen, meten, een vermoeden formuleren en het toetsen."),
            ("p", "<strong>Aristoteles</strong> staat aan het begin van die traditie. Hij keek, ordende "
                  "en deelde in: planten, dieren, bewegingen, staatsvormen. Dat ordenen van waarnemingen "
                  "hoort bij de start van elk onderzoek."),
            ("p", "<strong>Francis Bacon</strong> dringt er eeuwen later op aan dat kennis uit "
                  "<strong>waarneming en experiment</strong> moet komen, en niet uit het gezag van oude "
                  "boeken. Dat is de houding waarop de moderne wetenschap gebouwd is."),
            ("kader", "<strong>Wetenschap is geen verzameling feiten maar een manier van werken.</strong> "
                      "Wat haar kenmerkt, is niet dat ze gelijk heeft, maar dat ze zichzelf kan "
                      "verbeteren."),
        ]),
        dict(kop="Verificatie, falsificatie en het demarcatieprobleem", blokken=[
            ("p", "Het <strong>demarcatieprobleem</strong> is de vraag waar je de grens trekt tussen "
                  "wetenschap en wat zich als wetenschap voordoet. Demarcatie betekent afbakening."),
            ("p", "Een eerste antwoord was <strong>verificatie</strong>: een uitspraak is "
                  "wetenschappelijk als je ze kan bevestigen. Dat loopt stuk op de inductie. Hoeveel "
                  "witte zwanen je ook telt, je krijgt de uitspraak alle zwanen zijn wit nooit zeker "
                  "bevestigd."),
            ("p", "<strong>Karl Popper</strong> draait het om. Zijn maatstaf is <strong>falsificatie</strong>: "
                  "een uitspraak is wetenschappelijk als je kan zeggen welke waarneming haar zou "
                  "weerleggen. Eén zwarte zwaan volstaat."),
            ("p", tabel(["", "Verificatie", "Falsificatie"], [
                ["de vraag", "kan ik dit bevestigen?", "wat zou dit weerleggen?"],
                ["probleem", "bevestiging kan altijd toevallig zijn", "één tegenvoorbeeld is beslissend"],
                ["gevolg", "nooit volle zekerheid", "een theorie blijft voorlopig, maar is toetsbaar"],
            ])),
            ("kader", "<strong>Een theorie die niets uitsluit, verklaart niets.</strong> Wie op elke "
                      "mogelijke uitkomst zegt dat ze zijn theorie bevestigt, heeft geen sterke theorie "
                      "maar een onweerlegbare. Dat is bij Popper juist het zwaktebod."),
        ]),
        dict(kop="Pseudowetenschap", blokken=[
            ("p", "<strong>Pseudowetenschap</strong> lijkt op wetenschap maar werkt er niet zoals ze. Je "
                  "herkent ze aan een paar vaste trekken."),
            ("p", tabel(["Kenmerk", "Hoe het eruitziet"], [
                ["niet te weerleggen", "elke uitkomst past in de theorie"],
                ["uitvluchten", "bij een tegenvoorbeeld wordt de theorie wat bijgedraaid"],
                ["vage voorspellingen", "zo ruim geformuleerd dat ze altijd uitkomen"],
                ["beroep op gezag", "de grondlegger heeft het gezegd, dus het klopt"],
                ["geen controle", "geen onafhankelijk onderzoek, geen gepubliceerde methode"],
            ])),
            ("p", "Let op: pseudowetenschap is niet hetzelfde als <strong>ongelijk hebben</strong>. Een "
                  "wetenschappelijke theorie die weerlegd wordt, was wel degelijk wetenschappelijk. Het "
                  "verschil zit in de toetsbaarheid, niet in de uitkomst."),
        ]),
        dict(kop="Een filosofische tekst lezen in drie stappen", blokken=[
            ("p", "De fiche geeft een stappenplan om een filosofische tekst te analyseren. Je krijgt het "
                  "niet op het examen, maar de vaardigheid zelf wordt wel getoetst."),
            ("p", tabel(["Stap", "Wat je doet"], [
                ["1. oriënterend lezen",
                 "de tekst in zijn geheel lezen, letten op de indeling, de signaalwoorden en de "
                 "kernbegrippen, en in elke alinea een kernzin aanduiden"],
                ["2. grondig lezen",
                 "herlezen, onbekende woorden opzoeken, moeilijke zinnen ontleden, verbanden aanduiden, "
                 "en een samenvatting in enkele zinnen maken"],
                ["3. reflectie",
                 "tegenvoorbeelden zoeken, je eigen kritiek formuleren, en bedenken hoe de auteur daarop "
                 "zou antwoorden"],
            ])),
            ("kader", "<strong>De toets van stap 2:</strong> je moet daarna met je eigen woorden aan een "
                      "vriend kunnen uitleggen hoe de auteur zijn stelling verdedigt. Lukt dat niet, dan "
                      "ben je nog niet klaar met lezen."),
        ]),
    ],
    onthoud=[
        "Aristoteles ordende zijn waarnemingen; Bacon eiste waarneming en experiment in plaats van gezag.",
        "Demarcatie = de grens tussen wetenschap en pseudowetenschap.",
        "Verificatie vraagt: kan ik dit bevestigen? Falsificatie vraagt: wat zou dit weerleggen?",
        "Popper koos falsificatie. Een theorie die niets uitsluit, verklaart niets.",
        "Pseudowetenschap is niet te weerleggen, werkt met uitvluchten en beroept zich op gezag.",
        "Een tekst lezen: oriënterend lezen, grondig lezen, reflectie.",
    ],
)

# ───────────────────────── 4. Lichaam en geest
BUNDELS["lichaam-en-geest-monisme-en-dualisme-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Lichaam en geest: monisme en dualisme",
    onder="Eén werkelijkheid of twee? Parmenides, Plato, Aristoteles, Descartes en Spinoza, en de blik van buiten het westen.",
    secties=[
        dict(kop="Twee mensvisies", blokken=[
            ("p", "De vraag is eenvoudig te stellen en moeilijk te beantwoorden: zijn jouw denken en jouw "
                  "lichaam twee verschillende dingen, of twee kanten van één ding?"),
            ("p", tabel(["", "Dualisme", "Monisme"], [
                ["woord", "van duo: twee", "van monos: één"],
                ["stelling", "lichaam en geest zijn twee werkelijkheden",
                 "er is één werkelijkheid; lichaam en geest horen er beide bij"],
                ["sterk punt", "het verschil tussen denken en stof is echt",
                 "geen onverklaarbare brug tussen twee werelden nodig"],
                ["zwak punt", "hoe werken die twee dan op elkaar in?",
                 "hoe verklaar je dan dat denken zo anders aanvoelt?"],
            ])),
            ("kader", "<strong>Wat de twee gemeen hebben:</strong> ze beantwoorden dezelfde vraag, "
                      "namelijk hoe denken en lichaam samenhangen. Ze geven er een ander antwoord op."),
        ]),
        dict(kop="De oudheid: Parmenides, Plato en Aristoteles", blokken=[
            ("p", "<strong>Parmenides</strong> is het vroege voorbeeld van het monisme in zijn strengste "
                  "vorm: het zijnde is <strong>één en onveranderlijk</strong>, en wat op verandering "
                  "lijkt, misleidt ons."),
            ("p", "<strong>Plato</strong> is een dualist. De <strong>ziel</strong> staat bij hem los van "
                  "het lichaam en is <strong>onsterfelijk</strong>; het lichaam is haar verblijfplaats, "
                  "haast een gevangenis. Dat past bij zijn grotallegorie: het echte ligt elders."),
            ("p", "<strong>Aristoteles</strong> leunt naar de andere kant. Bij hem is de ziel de "
                  "<strong>vorm van het lichaam</strong>: je kan ze onderscheiden, maar niet scheiden. "
                  "Sterft het lichaam, dan is er geen ziel die ergens verder reist."),
        ]),
        dict(kop="De nieuwe tijd: Descartes en Spinoza", blokken=[
            ("p", "<strong>René Descartes</strong> geeft het dualisme zijn bekendste vorm: er is een "
                  "<strong>denkende</strong> werkelijkheid en een <strong>uitgebreide</strong>, "
                  "stoffelijke werkelijkheid. Dat sluit aan bij zijn methodische twijfel: aan zijn "
                  "lichaam kan hij twijfelen, aan zijn denken niet."),
            ("p", "Daar hoort meteen het bekendste bezwaar bij, het <strong>interactieprobleem</strong>: "
                  "als die twee zo verschillend zijn, hoe kan een gedachte dan je benen in beweging "
                  "zetten?"),
            ("p", "<strong>Benedictus de Spinoza</strong> lost dat op door de knip ongedaan te maken. Bij "
                  "hem is er <strong>één werkelijkheid</strong>, en zijn denken en uitgebreidheid twee "
                  "<strong>kanten</strong> van diezelfde werkelijkheid. Moet er niets meer oversteken, "
                  "dan is er ook geen brug nodig."),
            ("p", tabel(["Filosoof", "Kant", "Kern"], [
                ["Parmenides", "monist", "het zijnde is één en onveranderlijk"],
                ["Plato", "dualist", "de ziel staat los van het lichaam en is onsterfelijk"],
                ["Aristoteles", "dicht bij het monisme", "de ziel is de vorm van het lichaam"],
                ["Descartes", "dualist", "denken en uitgebreidheid zijn twee werkelijkheden"],
                ["Spinoza", "monist", "twee kanten van één werkelijkheid"],
            ])),
        ]),
        dict(kop="Westers en niet-westers", blokken=[
            ("p", "De scherpe tweedeling tussen lichaam en geest is een westerse gewoonte. In veel "
                  "<strong>niet-westerse tradities</strong> is die scheiding veel minder scherp of "
                  "ontbreekt ze: mens, lichaam en omgeving worden er als één samenhangend geheel gezien."),
            ("p", "Het <strong>boeddhisme</strong> gaat nog een stap verder dan het monisme: daar is er "
                  "<strong>geen vast, blijvend zelf</strong>. Wat jij bent, is een geheel dat voortdurend "
                  "verandert. Dat staat ver van de westerse ziel die het lichaam overleeft."),
            ("kader", "<strong>Waarom vergelijken?</strong> Omdat je dan ziet dat de westerse indeling "
                      "zelf een keuze is en niet vanzelfsprekend. Wat je altijd voor de werkelijkheid "
                      "hield, blijkt één manier om de mens te bekijken."),
            ("p", "En vandaag? Hersenonderzoek toont steeds nauwkeuriger <strong>samenhang</strong> tussen "
                  "wat je brein doet en wat je ervaart. Maar samenhang aantonen is iets anders dan "
                  "aantonen dat geest en brein <strong>hetzelfde</strong> zijn. Die laatste stap is een "
                  "filosofische stap, geen meting, en daarom blijft het debat open."),
        ]),
    ],
    onthoud=[
        "Dualisme: twee werkelijkheden (duo). Monisme: één werkelijkheid (monos).",
        "Parmenides en Spinoza zijn monisten; Plato en Descartes dualisten; Aristoteles leunt naar het monisme.",
        "Plato: de ziel is onsterfelijk en los van het lichaam. Aristoteles: de ziel is de vorm van het lichaam.",
        "Descartes: denken tegenover uitgebreidheid, met het interactieprobleem als bezwaar.",
        "Spinoza: denken en uitgebreidheid zijn twee kanten van één werkelijkheid.",
        "In veel niet-westerse tradities is de scheiding minder scherp; het boeddhisme kent geen vast zelf.",
    ],
)

# ───────────────────────── 5. Cultuur en natuur
BUNDELS["cultuur-en-natuur-mens-dier-en-machine-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Cultuur en natuur: mens, dier en machine",
    onder="Wat alleen van de mens is, drie manieren om naar emoties te kijken, en de mens tegenover het dier en de machine.",
    secties=[
        dict(kop="Wat is exclusief menselijk?", blokken=[
            ("p", "<strong>Exclusief menselijk</strong> betekent: bij de mens en bij geen enkel ander "
                  "wezen. Niet vaker, niet sterker, maar uitsluitend. Dat woordje maakt de vraag zo "
                  "lastig."),
            ("p", "De fiche noemt twee <strong>mogelijke</strong> kandidaten: <strong>emoties</strong> en "
                  "de <strong>rede</strong>. Let op dat woord mogelijk, want bij de eerste houdt het "
                  "niet goed stand."),
            ("p", tabel(["Kandidaat", "Argument ervoor", "Argument ertegen"], [
                ["emoties", "mensen benoemen hun gevoelens en praten erover",
                 "ook dieren vertonen angst, woede en wat op rouw lijkt"],
                ["rede", "mensen kunnen over hun eigen denken nadenken en redenen afwegen",
                 "ook dieren leren, gebruiken werktuigen en werken samen"],
            ])),
            ("kader", "<strong>Dit is een filosofische en geen biologische vraag.</strong> Vaststellen "
                      "wat dieren kunnen, is onderzoek. Beslissen welk van die verschillen echt telt om "
                      "de mens mens te noemen, gaat over begrippen en waarden."),
            ("p", "De tegenstelling <strong>natuur tegenover cultuur</strong> houdt bij de mens nergens "
                  "helemaal stand. Ons lichaam legt grenzen vast, en daarbinnen maakt cultuur van alles "
                  "mogelijk. Wat natuur is en wat cultuur, valt niet netjes uit elkaar te halen."),
        ]),
        dict(kop="Drie benaderingen van emoties", blokken=[
            ("p", "De fiche laat je over emoties nadenken vanuit drie benaderingen. Ze sluiten elkaar "
                  "niet uit: lichaam, cultuur en oordeel kunnen alle drie in één emotie meespelen."),
            ("p", tabel(["Benadering", "Wat ze zegt", "Voorbeeld"], [
                ["naturalistisch", "emoties zijn aangeboren en lichamelijk, en komen overal voor",
                 "schrikken van een harde knal, waar je ook geboren bent"],
                ["cultureel en historisch", "welke emoties je voelt en toont, leer je van je omgeving en je tijd",
                 "luid huilen op een begrafenis hoort in het ene land en niet in het andere"],
                ["cognitief", "een emotie hangt samen met wat je over de situatie denkt",
                 "je schrikt van de knal en lacht als blijkt dat het een ballon was"],
            ])),
            ("kader", "<strong>De cognitieve benadering is het makkelijkst te herkennen:</strong> de "
                      "gebeurtenis blijft dezelfde, je oordeel verandert, en de emotie verandert mee."),
        ]),
        dict(kop="Mens en dier", blokken=[
            ("p", "Drie filosofen, drie posities, en samen een glijdende schaal van heel veel verschil "
                  "naar heel weinig."),
            ("p", tabel(["Filosoof", "Mens tegenover dier"], [
                ["Aristoteles", "de mens is een dier dat over rede beschikt; het verschil zit binnen de natuur"],
                ["René Descartes", "een dier werkt als een machine; enkel de mens heeft daarnaast een denkende geest"],
                ["Friedrich Nietzsche", "de mens krijgt geen ereplaats boven de natuur; hij hoort er helemaal bij"],
            ])),
            ("p", "Bij Aristoteles past dat onderscheid bij zijn visie op de ziel: de rede is geen "
                  "vreemde gast in het lichaam maar een kenmerk van dit soort wezen. Bij Descartes volgt "
                  "het uit zijn dualisme: wie geen denkende werkelijkheid heeft, blijft stof, en stof "
                  "werkt mechanisch."),
            ("kader", "<strong>Het bezwaar tegen Descartes gaat over pijn.</strong> Als een dier niets "
                      "ervaart, waarom gedraagt het zich dan precies zoals een wezen dat pijn heeft? "
                      "Nietzsche keert zich op zijn manier tegen hetzelfde: tegen het vleiende zelfbeeld "
                      "waarin de rede ons buiten de natuur zet."),
        ]),
        dict(kop="Mens en machine", blokken=[
            ("p", "Dezelfde vraag, maar nu naar de andere kant. De maatstaf die de fiche kiest, is "
                  "<strong>bewustzijn</strong>."),
            ("p", tabel(["Denker", "Stelling"], [
                ["Julien Offray de La Mettrie",
                 "de mens is een machine; voor zijn denken is geen aparte ziel nodig"],
                ["Dick Swaab",
                 "wat wij ons zelf noemen, is het werk van onze hersenen"],
            ])),
            ("p", "La Mettrie leefde in de 18de eeuw en Swaab is een hedendaagse hersenonderzoeker. Toch "
                  "staan ze in hetzelfde rijtje, want ze gaan dezelfde richting uit: de mens valt uit "
                  "stof te verklaren, zonder een geest van een andere orde."),
            ("kader", "<strong>Waarom bewustzijn en niet kunnen?</strong> Wat een machine kán, schuift "
                      "voortdurend op: rekenen, schaken, spreken. Of er iets is dat het is om die machine "
                      "te zijn, is de vraag die blijft. Gedrag dat op bewustzijn lijkt, bewijst nog geen "
                      "bewustzijn, en van buitenaf is dat moeilijk te beslechten."),
        ]),
    ],
    onthoud=[
        "Exclusief menselijk = uitsluitend bij de mens, niet enkel sterker of vaker.",
        "Emoties en rede zijn de twee kandidaten; bij emoties houdt het niet goed stand.",
        "Drie benaderingen van emoties: naturalistisch (lichaam), cultureel en historisch (geleerd), cognitief (je oordeel).",
        "Aristoteles: de mens is een dier met rede. Descartes: het dier is een machine zonder geest. Nietzsche: geen ereplaats boven de natuur.",
        "La Mettrie: de mens is een machine. Swaab: bewustzijn is hersenwerk.",
        "Gedrag dat op bewustzijn lijkt, bewijst nog geen bewustzijn.",
    ],
)

# ───────────────────────── 6. Vrijheid en determinisme tot de 19de eeuw
BUNDELS["vrijheid-en-determinisme-van-de-oudheid-tot-de-19de-eeuw-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Vrijheid en determinisme van de oudheid tot de 19de eeuw",
    onder="Lot tegenover toeval, en vijf periodes waarin telkens iets anders onze vrijheid inperkt.",
    secties=[
        dict(kop="Lot, toeval en determinisme", blokken=[
            ("p", "Drie woorden die op elkaar lijken en drie verschillende dingen zeggen. Het verschil "
                  "zit in twee vragen: zit er een <strong>bedoeling</strong> achter, en lag het "
                  "<strong>vast</strong>?"),
            ("p", tabel(["Woord", "Bedoeling?", "Lag het vast?", "Voorbeeld"], [
                ["lot", "ja, er is een bestemming", "ja", "de voorspelling die uitkomt hoe je ook vlucht"],
                ["toeval", "nee", "nee", "jij wint de lotto; niets had dat voor jou bestemd"],
                ["determinisme", "niet noodzakelijk", "ja",
                 "je keuze volgt uit oorzaken, zonder dat iemand het zo wilde"],
            ])),
            ("kader", "<strong>Determinisme is kaler dan het lot en strenger dan toeval.</strong> Van "
                      "determineren: vastleggen. Alles wat gebeurt, ligt vast door wat eraan voorafging, "
                      "maar er hoeft geen bedoeling achter te zitten."),
        ]),
        dict(kop="De Griekse mythologie en de oudheid", blokken=[
            ("p", "In de <strong>Griekse mythologie</strong> staat het <strong>lot</strong> boven alles, "
                  "en zelfs de goden kunnen het niet omkeren. Ze kennen het, ze kondigen het aan, en ook "
                  "zij ondergaan het."),
            ("p", "In verhalen als dat van <strong>Oedipus</strong> zit de wrange kern: wie zijn "
                  "voorspelling probeert te ontlopen, vervult ze juist daardoor. De vlucht voor het lot "
                  "blijkt een deel van het lot."),
            ("p", "<strong>Democritus</strong> brengt in de oudheid de eerste strikt deterministische "
                  "verklaring: alles bestaat uit <strong>atomen</strong> die volgens <strong>vaste "
                  "wetten</strong> bewegen. Wie dat aanneemt, moet aannemen dat ook jouw volgende beweging "
                  "vastligt."),
            ("p", "De <strong>Stoïcijnen</strong> aanvaarden dat de wereld een vaste orde volgt, en "
                  "zoeken de vrijheid ergens anders: in je <strong>houding</strong>. Hun onderscheid is "
                  "dat tussen wat <strong>in je macht</strong> ligt en wat niet. Je bagage verliezen lag "
                  "niet in je macht; wat je erover denkt, wel."),
        ]),
        dict(kop="Middeleeuwen en 17de eeuw", blokken=[
            ("p", "In de middeleeuwen krijgt de vraag een nieuwe vorm: hoe kan de mens vrij zijn terwijl "
                  "<strong>God alles weet en voorziet</strong>? <strong>Thomas van Aquino</strong> houdt "
                  "beide vast. De mens heeft een <strong>vrije wil</strong> en kiest werkelijk, en dat "
                  "past binnen de orde die God gewild heeft. Geloof en rede hoeven elkaar niet te bijten."),
            ("p", "In de 17de eeuw levert de natuurwetenschap een nieuw beeld: het "
                  "<strong>mechanisch determinisme</strong>. De wereld werkt als een <strong>machine</strong> "
                  "waarin natuurwetten alles vastleggen. Wie de wetten en de beginstand kent, kent alles "
                  "wat volgt."),
            ("kader", "<strong>Daar zit de hele moeilijkheid in één vraag:</strong> zit de mens ook in "
                      "die machine? Zo ja, dan ligt ook zijn keuze vast. Zo nee, dan moet je uitleggen "
                      "waarom hij een uitzondering is."),
        ]),
        dict(kop="De 19de eeuw: Schopenhauer en Nietzsche", blokken=[
            ("p", "<strong>Arthur Schopenhauer</strong> legt de onvrijheid niet buiten maar binnen de "
                  "mens. Achter onze keuzes zit een <strong>wil</strong> die wij zelf niet gekozen "
                  "hebben. Je kan doen wat je wil, maar je kan niet kiezen wát je wil."),
            ("p", "<strong>Friedrich Nietzsche</strong> stelt een andere vraag. Niet alleen of de vrije "
                  "wil bestaat, maar ook waaraan dat idee ons dient. Zijn antwoord: het is een "
                  "<strong>bedenksel</strong> dat vooral dient om iemand <strong>schuld</strong> te "
                  "kunnen toewijzen."),
            ("p", tabel(["Periode", "Wat onze vrijheid inperkt"], [
                ["Griekse mythologie", "het lot, dat boven de goden staat"],
                ["oudheid: Democritus", "atomen die volgens vaste wetten bewegen"],
                ["oudheid: de Stoïcijnen", "de vaste orde van de wereld, met vrijheid in je houding"],
                ["middeleeuwen: Thomas van Aquino", "niets: de vrije wil en de voorzienigheid gaan samen"],
                ["17de eeuw", "de natuurwetten van de wereldmachine"],
                ["19de eeuw: Schopenhauer", "de wil in jezelf, die je niet koos"],
                ["19de eeuw: Nietzsche", "de vrije wil zelf is een bedenksel"],
            ])),
            ("weetje", "Deze vraag is niet schools. Ons strafrecht gaat ervan uit dat iemand anders had "
                       "kunnen handelen. Een streng determinisme maakt het begrip schuld moeilijk te "
                       "verdedigen, en daarover gaat het volgende thema verder."),
        ]),
    ],
    onthoud=[
        "Lot heeft een bedoeling, toeval geen van beide, determinisme legt vast zonder bedoeling.",
        "In de mythologie staat het lot boven de goden; Oedipus vervult zijn voorspelling door ze te ontlopen.",
        "Democritus: atomen volgens vaste wetten. De Stoïcijnen: vrijheid zit in je houding, niet in de gebeurtenis.",
        "Thomas van Aquino verzoent de vrije wil met de voorzienigheid.",
        "17de eeuw: de wereld als machine, dus mechanisch determinisme.",
        "Schopenhauer: je kan niet kiezen wát je wil. Nietzsche: de vrije wil is een bedenksel om schuld toe te wijzen.",
    ],
)

# ───────────────────────── 7. Vrijheid en determinisme in de 20ste eeuw
BUNDELS["vrijheid-en-determinisme-in-de-20ste-eeuw-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Vrijheid en determinisme in de 20ste eeuw",
    onder="Heidegger, Sartre, Foucault, Frankfurt en Verplaetse: van gedoemd tot vrijheid tot een strafrecht zonder schuld.",
    secties=[
        dict(kop="Heidegger: geworpen in een situatie", blokken=[
            ("p", "<strong>Martin Heidegger</strong> vertrekt van de <strong>geworpenheid</strong>: je "
                  "hebt je tijd, je lichaam en je afkomst niet gekozen. Je vindt je daarin terug, en "
                  "daarbinnen moet je iets met je leven doen."),
            ("p", "De vrijheid die overblijft, is dat je je tot je mogelijkheden kan <strong>verhouden</strong> "
                  "en je eigen leven op je kan nemen. Doe je dat niet, dan spreekt hij van een "
                  "<strong>oneigenlijk bestaan</strong>: leven zoals men nu eenmaal leeft, zonder er zelf "
                  "voor in te staan."),
            ("kader", "<strong>Oneigenlijk is niet hetzelfde als liegen.</strong> Het gaat over wegkijken: "
                      "je leven laten lopen zoals het hoort te lopen, met de gewoonte als stuurman."),
        ]),
        dict(kop="Sartre: gedoemd tot vrijheid", blokken=[
            ("p", "<strong>Jean-Paul Sartre</strong> noemt de mens <strong>gedoemd tot vrijheid</strong>. "
                  "Ook niet kiezen is een keuze, en de verantwoordelijkheid kan je aan niemand "
                  "doorschuiven."),
            ("p", "Bij hem gaat de <strong>existentie aan de essentie voorbij</strong>: er ligt geen "
                  "vaste menselijke natuur klaar, je wordt wie je bent door te handelen. Bij een mes is "
                  "het omgekeerd: daarvan ligt het doel vast voor het gemaakt wordt."),
            ("p", "Wie zich achter zijn rol of zijn aard wegzet, is in <strong>kwade trouw</strong>: hij "
                  "doet alsof hij niet kon kiezen. Ik moest wel, ik ben nu eenmaal zo — dat is bij Sartre "
                  "geen verklaring maar een uitvlucht."),
            ("kader", "<strong>Zijn vrijheid is geen gemak maar een last.</strong> Er is geen natuur, geen "
                      "rol en geen God aan wie je je keuze kan overlaten, dus draag je de gevolgen zelf."),
        ]),
        dict(kop="Foucault: macht en normen", blokken=[
            ("p", "<strong>Michel Foucault</strong> zoekt de beperking van onze vrijheid niet in "
                  "natuurwetten maar in <strong>macht en normen</strong>. Scholen, wetten, klinieken, "
                  "gewoonten en woorden bepalen mee wat normaal heet, en vormen zo wie je geworden bent."),
            ("p", "Dat heet <strong>disciplinering</strong>, en zijn punt is dat het meestal "
                  "<strong>zonder geweld</strong> gebeurt. Niemand dwingt je, en toch wordt je verlangen "
                  "mee gevormd door de wereld waarin je bent opgegroeid. Een keuze die vrij lijkt, kan "
                  "nog altijd een keuze zijn tussen mogelijkheden die jou zijn aangereikt."),
        ]),
        dict(kop="Frankfurt: willen wat je wil", blokken=[
            ("p", "<strong>Frankfurt</strong> verlegt de vraag. Niet of je keuze zonder oorzaak was, maar "
                  "of ze <strong>echt van jou</strong> is. Daarvoor onderscheidt hij twee lagen: wat je "
                  "wil, en wat je zou <strong>willen willen</strong>."),
            ("p", tabel(["Twee mensen", "Eerste orde", "Tweede orde", "Vrij?"], [
                ["de ene", "drang naar een middel", "wil die drang niet hebben", "nee, hij wordt meegesleept"],
                ["de andere", "drang naar een middel", "wil die drang ook hebben", "ja, het verlangen is het zijne"],
            ])),
            ("kader", "<strong>Daarom heet zijn positie verzoenend:</strong> vrijheid en een wereld vol "
                      "oorzaken kunnen bij hem naast elkaar bestaan."),
        ]),
        dict(kop="Verplaetse: een strafrecht zonder schuld", blokken=[
            ("p", "<strong>Jan Verplaetse</strong> gaat het verst de andere kant op: er bestaat geen "
                  "vrije wil, en ons <strong>strafrecht</strong> zou dat moeten verwerken. Straffen om "
                  "iemand <strong>schuld</strong> te laten boeten, verliest dan zijn grond."),
            ("p", "Dat betekent niet dat er geen maatregel meer mogelijk is. Beschermen, behandelen en "
                  "voorkomen hebben geen schuld nodig. Enkel <strong>vergelden</strong> heeft dat wel, en "
                  "net dat komt onder druk."),
            ("p", tabel(["Denker", "Waar de vrijheid of de grens ligt"], [
                ["Heidegger", "je situatie koos je niet; je leven op je nemen wel"],
                ["Sartre", "je bent vrij en kan er niet aan ontsnappen; niet kiezen is kiezen"],
                ["Foucault", "macht en normen vormen mee wat je wil"],
                ["Frankfurt", "vrij ben je als je wil wat je wil willen"],
                ["Verplaetse", "er is geen vrije wil; het strafrecht moet zonder schuld kunnen"],
            ])),
            ("weetje", "Waar de 17de eeuw naar de natuurwetten keek, kijkt de 20ste eeuw naar verlangens, "
                       "gewoonten, macht en hersenen. De beperking wordt vaker binnen de mens zelf "
                       "gezocht."),
        ]),
    ],
    onthoud=[
        "Heidegger: geworpenheid (je situatie koos je niet) en het oneigenlijke bestaan.",
        "Sartre: gedoemd tot vrijheid, existentie voor essentie, en kwade trouw als zelfbedrog.",
        "Foucault: macht, normen en disciplinering vormen mee wie je bent en wat je wil.",
        "Frankfurt: vrij ben je als je verlangen er een is dat je ook wil hebben. Verzoenend met oorzaken.",
        "Verplaetse: geen vrije wil, dus een strafrecht zonder schuld; beschermen kan wel, vergelden niet.",
        "De vijf staan op een rij van heel veel vrijheid (Sartre) naar heel weinig (Verplaetse).",
    ],
)

# ───────────────────────── 8. Ethiek: basisbegrippen en vier benaderingen
BUNDELS["ethiek-basisbegrippen-en-vier-benaderingen-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Ethiek: basisbegrippen en vier benaderingen",
    onder="Waarden en normen, universalisme en relativisme, het morele dilemma, de vier richtingen en het is-ought probleem.",
    secties=[
        dict(kop="Waarden en normen", blokken=[
            ("p", "Een <strong>waarde</strong> is wat je belangrijk vindt: eerlijkheid, vrijheid, "
                  "respect. Een <strong>norm</strong> is de concrete regel die daaruit volgt: je mag "
                  "niet spieken, je laat iemand uitspreken."),
            ("p", "De waarde komt eerst en is algemeen; de norm is concreter. Dezelfde waarde kan in twee "
                  "landen <strong>andere normen</strong> opleveren: respect voor ouderen is overal een "
                  "waarde, maar hoe je dat hoort te laten zien, verschilt."),
        ]),
        dict(kop="Universalisme, relativisme en cultuurrelativisme", blokken=[
            ("p", tabel(["Standpunt", "Wat het zegt", "Lastige vraag"], [
                ["moreel universalisme", "er zijn morele regels die overal en voor iedereen gelden",
                 "wie bepaalt welke regels dat zijn?"],
                ["moreel relativisme", "wat goed is, hangt af van wie het zegt of van welke groep",
                 "kan je dan nog iets afkeuren?"],
                ["cultuurrelativisme", "morele opvattingen horen bij een cultuur en zijn niet van "
                 "buitenaf te beoordelen",
                 "en wat met onrecht in een andere cultuur?"],
            ])),
            ("kader", "<strong>Het bekendste bezwaar tegen het cultuurrelativisme:</strong> wie zegt dat "
                      "je een cultuur niet van buitenaf mag beoordelen, haalt daarmee ook de grond onder "
                      "elke kritiek op onrecht weg. Een universalist kan de culturele verschillen gerust "
                      "vaststellen; hij vindt enkel dat sommige regels daar niet van afhangen."),
            ("p", "Ook de <strong>vrije wil</strong> hoort bij de basisbegrippen. Verwijten dat iemand "
                  "anders had moeten handelen, heeft alleen zin als hij anders <strong>kón</strong> "
                  "handelen. Zonder keuzevrijheid valt er niemand nog verantwoordelijk te stellen."),
        ]),
        dict(kop="Het morele dilemma en de ethische vraag", blokken=[
            ("p", "Een <strong>moreel dilemma</strong> is een keuze waarbij <strong>elke</strong> "
                  "mogelijkheid iets van waarde kost. Het pijnlijke zit erin dat er geen schone uitweg "
                  "is: ook de beste keuze laat iets achter dat je niet wou opgeven."),
            ("p", "Een <strong>ethische vraag</strong> gaat over wat je zou moeten doen, niet over wat er "
                  "feitelijk gebeurt. Hoeveel mensen liegen, is een feitenvraag. Of liegen hier mag, is "
                  "een ethische vraag."),
        ]),
        dict(kop="Twee benaderingen, en vier richtingen", blokken=[
            ("p", "De ethiek valt eerst in twee uiteen."),
            ("p", tabel(["Benadering", "Wat ze doet", "Voorbeeld"], [
                ["descriptieve ethiek", "beschrijft welke moraal mensen er feitelijk op nahouden",
                 "een bevraging over wat mensen van orgaandonatie vinden"],
                ["normatieve ethiek", "zoekt wat je zou moeten doen",
                 "is orgaandonatie een plicht?"],
            ])),
            ("p", "Binnen de normatieve ethiek onderscheidt de fiche vier richtingen. Ze stellen bij "
                  "hetzelfde geval elk een andere vraag."),
            ("p", tabel(["Richting", "Waar ze naar kijkt", "Haar vraag"], [
                ["gevolgenethiek", "de uitkomst van je daad", "wat brengt dit teweeg?"],
                ["plichtethiek", "de regel of de plicht", "welke regel bindt mij hier?"],
                ["deugdethiek", "de persoon die handelt", "wat voor mens word ik hiermee?"],
                ["zorgethiek", "de concrete relatie", "wat heeft deze mens van mij nodig?"],
            ])),
            ("kader", "<strong>Leer deze vier vragen uit het hoofd.</strong> Bij elke casus op het examen "
                      "kan je ze aflopen, en dan heb je vier verschillende antwoorden klaar."),
        ]),
        dict(kop="Het is-ought probleem van Hume", blokken=[
            ("p", "<strong>David Hume</strong> wijst op een sprong die veel mensen zonder nadenken maken: "
                  "uit wat <strong>is</strong>, volgt niet zonder meer wat <strong>zou moeten</strong>. "
                  "Een beschrijving en een voorschrift zijn twee soorten uitspraken, en tussen beide zit "
                  "een stap die je apart moet verdedigen."),
            ("p", tabel(["Uitspraak", "Soort"], [
                ["mensen eten al duizenden jaren vlees", "een beschrijving"],
                ["wij zouden minder vlees moeten eten", "een voorschrift"],
                ["mensen eten al duizenden jaren vlees, dus mogen we dat blijven doen",
                 "de sprong die Hume aanwijst"],
            ])),
            ("kader", "<strong>Het woordje dus doet het werk.</strong> Dat iets zo is of zo was, zegt op "
                      "zich niet dat het zo mag blijven. Deze kritiek komt terug bij de gevolgenethiek: "
                      "dat mensen naar geluk streven, bewijst nog niet dat geluk de maatstaf moet zijn."),
        ]),
    ],
    onthoud=[
        "Een waarde is wat je belangrijk vindt; een norm is de concrete regel die eruit volgt.",
        "Universalisme: regels voor iedereen. Relativisme: het hangt ervan af. Cultuurrelativisme: niet van buitenaf te beoordelen.",
        "Een moreel dilemma: elke keuze kost iets van waarde.",
        "Descriptieve ethiek beschrijft, normatieve ethiek schrijft voor.",
        "Vier richtingen: gevolgen, plicht, deugd, zorg. Vier verschillende vragen bij hetzelfde geval.",
        "Is-ought (Hume): uit wat is, volgt niet zonder meer wat zou moeten.",
    ],
)

# ───────────────────────── 9. Gevolgenethiek en plichtethiek
BUNDELS["gevolgenethiek-en-plichtethiek-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Gevolgenethiek en plichtethiek",
    onder="Bentham en Singer tegenover Kant en Levinas: telt de uitkomst, of de regel die je bindt?",
    secties=[
        dict(kop="De gevolgenethiek of het utilitarisme", blokken=[
            ("p", "De <strong>gevolgenethiek</strong> beoordeelt een daad op wat ze "
                  "<strong>teweegbrengt</strong>. Ze heet ook het <strong>utilitarisme</strong>, van "
                  "utilitas: nut."),
            ("p", "<strong>Jeremy Bentham</strong> geldt als haar grondlegger. Zijn stelregel: streef "
                  "naar het <strong>grootste geluk voor het grootste aantal</strong>. Hij wil moraal "
                  "rekenbaar maken door <strong>genot en pijn</strong> tegen elkaar af te wegen, en "
                  "niemands geluk weegt daarbij van tevoren zwaarder dan dat van een ander."),
            ("p", "<strong>Peter Singer</strong> blijft binnen diezelfde benadering en verandert "
                  "<strong>wie meetelt</strong>. Zijn maatstaf is het vermogen om te <strong>lijden</strong>, "
                  "en dus tellen ook dieren mee. Het vooroordeel dat enkel de eigen soort meetelt, noemt "
                  "hij <strong>soortisme</strong>."),
            ("kader", "<strong>De onpartijdigheid is haar sterke en haar koude kant.</strong> Jouw geluk "
                      "telt niet zwaarder omdat het het jouwe is. Maar een optelsom vertelt ook niet wie "
                      "de rekening betaalt: tien mensen heel gelukkig en één diep ongelukkig geeft een "
                      "positieve som."),
            ("p", "Daar komen twee bezwaren bij. Een <strong>praktisch</strong> bezwaar: je kent de "
                  "gevolgen van je daad vooraf niet volledig, want je moet de toekomst inschatten. En het "
                  "bezwaar van <strong>Hume</strong>: de vaststelling dát mensen geluk zoeken, levert nog "
                  "geen norm op dat geluk de maatstaf móét zijn."),
        ]),
        dict(kop="De plichtethiek: Kant", blokken=[
            ("p", "De <strong>plichtethiek</strong> vertrekt van het omgekeerde: sommige daden zijn goed "
                  "of fout <strong>los van wat ze opleveren</strong>. <strong>Immanuel Kant</strong> is "
                  "haar grondlegger."),
            ("p", "Zijn <strong>categorische imperatief</strong> luidt: handel enkel volgens een regel "
                  "waarvan je kan willen dat ze voor allen geldt. Categorisch betekent "
                  "<strong>onvoorwaardelijk</strong>: er hangt geen als-dan aan vast."),
            ("p", tabel(["", "Categorische imperatief", "Hypothetische imperatief"], [
                ["vorm", "doe dit", "wil je dat bereiken, doe dan dit"],
                ["geldt", "onvoorwaardelijk, voor iedereen", "enkel zolang je dat doel wil"],
                ["moreel?", "ja", "nee, het is een nuttige raad"],
                ["voorbeeld", "lieg niet", "wil je slagen, dan moet je studeren"],
            ])),
            ("p", "Een tweede formulering zegt: behandel een mens nooit <strong>louter als een "
                  "middel</strong> voor jouw doel. Een mens is geen instrument, ook niet voor een mooi "
                  "doel."),
            ("p", "Kant is daarmee een <strong>moreel universalist</strong>: de toets van de algemene wet "
                  "zit al in zijn imperatief. Wat niet voor allen kan gelden, is geen plicht."),
            ("kader", "<strong>Twee bekende bezwaren tegen Kant.</strong> Hij is zo streng dat hij ook in "
                      "uitzonderlijke gevallen geen leugen toelaat, zelfs niet tegen iemand die je vriend "
                      "komt zoeken om hem kwaad te doen. En zijn imperatief zegt welke <strong>vorm</strong> "
                      "een regel moet hebben, maar niet wat je concreet moet doen: het is een toets en "
                      "geen lijst."),
        ]),
        dict(kop="De plichtethiek: Levinas", blokken=[
            ("p", "<strong>Emmanuel Levinas</strong> komt bij dezelfde onvoorwaardelijkheid uit langs een "
                  "heel andere weg. Bij hem begint de moraal niet bij een regel die je met je rede toetst, "
                  "maar bij het <strong>gelaat van de ander</strong> dat je aanspreekt. De ander gaat aan "
                  "jouw afweging vooraf en maakt je verantwoordelijk."),
            ("p", tabel(["", "Kant", "Levinas"], [
                ["plicht komt van", "een algemene regel die de rede toetst", "de ontmoeting met de ander"],
                ["gelijkenis", "onvoorwaardelijk", "onvoorwaardelijk"],
                ["gelijkenis", "geen afweging van gevolgen", "geen afweging van gevolgen"],
                ["verschil", "vertrekt van het algemene", "vertrekt van deze ene mens"],
            ])),
        ]),
        dict(kop="De twee naast elkaar", blokken=[
            ("p", tabel(["", "Gevolgenethiek", "Plichtethiek"], [
                ["beslissend", "de uitkomst", "de regel of de plicht"],
                ["kijkt", "vooruit", "naar wat je bindt"],
                ["belofte nakomen", "enkel als het goed uitvalt", "ook als het nadelig uitvalt"],
                ["op voorhand verboden daden", "geen", "ja"],
                ["zwak punt", "de minderheid kan geofferd worden", "ze kan onbuigzaam worden"],
            ])),
            ("kader", "<strong>Ze kunnen bij hetzelfde geval tot een tegengesteld besluit komen.</strong> "
                      "Juist daarom zijn morele dilemma's zo lastig, en daarom vraagt een casus op het "
                      "examen dat je beide kanten uitwerkt."),
        ]),
    ],
    onthoud=[
        "Gevolgenethiek = utilitarisme: de uitkomst beslist.",
        "Bentham: het grootste geluk voor het grootste aantal, genot min pijn.",
        "Singer: wie kan lijden telt mee, ook dieren. Soortisme is het vooroordeel van de eigen soort.",
        "Bezwaren: de minderheid kan geofferd worden, de gevolgen zijn niet te voorzien, en de sprong van Hume.",
        "Kant: de categorische imperatief (onvoorwaardelijk) tegenover de hypothetische (enkel bij een doel); nooit louter als middel.",
        "Levinas: de plicht komt van het gelaat van de ander, niet van een algemene regel.",
    ],
)

# ───────────────────────── 10. Deugdethiek en zorgethiek
BUNDELS["deugdethiek-en-zorgethiek-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Deugdethiek en zorgethiek",
    onder="Aristoteles, Nussbaum, Hume en Foot over deugden, en Gilligan en Tronto over zorg.",
    secties=[
        dict(kop="De deugdethiek: wat voor mens wil je zijn?", blokken=[
            ("p", "De <strong>deugdethiek</strong> stelt niet de vraag wat moet ik doen, maar "
                  "<strong>wat voor mens wil ik zijn</strong>. Goed handelen volgt dan uit een goed "
                  "karakter."),
            ("p", "<strong>Aristoteles</strong> is haar grondlegger. Hij noemt vier "
                  "<strong>kardinale deugden</strong>, van cardo: spil. Het zijn de deugden waarom de "
                  "andere draaien."),
            ("p", tabel(["Deugd", "Wat ze is", "Het midden tussen"], [
                ["verstandigheid", "weten wat hier het juiste is", "onbezonnenheid en besluiteloosheid"],
                ["rechtvaardigheid", "ieder geven wat hem toekomt", "voortrekken en benadelen"],
                ["moed", "doen wat nodig is ondanks je angst", "lafheid en overmoed"],
                ["matigheid", "maat houden in genot", "onthouding en onmatigheid"],
            ])),
            ("kader", "<strong>Een deugd is het midden tussen een tekort en een overdaad</strong>, en "
                      "niet het gemiddelde van wat mensen doen. Het juiste midden hangt van de situatie "
                      "af."),
            ("p", "Een deugd krijg je niet cadeau: je bouwt ze op door ze te <strong>oefenen tot ze een "
                  "gewoonte wordt</strong>, zoals je een instrument leert bespelen."),
        ]),
        dict(kop="Nussbaum, Hume en Foot", blokken=[
            ("p", "<strong>Martha Nussbaum</strong> werkt die lijn modern uit met tien "
                  "<strong>capaciteiten</strong>: wat elke mens moet <strong>kunnen</strong> om een "
                  "menswaardig leven te leiden. Denk aan gezondheid, veiligheid, denken en voelen, bij "
                  "anderen horen, spelen en meebeslissen. Het zijn mogelijkheden en geen prestaties."),
            ("p", "<strong>David Hume</strong> splitst de deugden in twee."),
            ("p", tabel(["Soort deugd", "Waar ze vandaan komt", "Voorbeeld"], [
                ["natuurlijke deugd", "ons gevoel; ze komt vanzelf op",
                 "medelijden, vriendelijkheid, zorg voor wie je graag ziet"],
                ["artificiële deugd", "afspraken die een samenleving heeft opgebouwd",
                 "rechtvaardigheid, je woord houden"],
            ])),
            ("p", "<strong>Foot</strong> noemt drie kenmerken waaraan je een deugd herkent: ze is "
                  "<strong>goed</strong> voor de mens en zijn omgeving, ze zit in je <strong>wil</strong> "
                  "en niet enkel in je kunnen, en ze <strong>vangt een zwakke plek</strong> in onze "
                  "neigingen op."),
            ("kader", "<strong>Dat derde verklaart waarom de lijst eruitziet zoals ze eruitziet.</strong> "
                      "Moed is nodig omdat wij angst kennen, matigheid omdat wij verleid worden. Waar "
                      "geen bekoring is, is geen deugd nodig."),
            ("p", "De deugdethiek heet <strong>universalistisch</strong> omdat wat een mens nodig heeft "
                  "om te bloeien, bij alle mensen grotendeels gelijk is. Moed, matigheid en "
                  "rechtvaardigheid komen in heel verschillende tijden en culturen terug, al verschilt de "
                  "vorm waarin ze geprezen worden."),
        ]),
        dict(kop="De zorgethiek: kwetsbaar en van elkaar afhankelijk", blokken=[
            ("p", "De <strong>zorgethiek</strong> vertrekt van een ander mensbeeld: mensen zijn "
                  "<strong>kwetsbaar</strong> en <strong>van elkaar afhankelijk</strong>. Niemand komt "
                  "alleen door het leven. Moraal begint daar bij het feit dat mensen zorg geven en zorg "
                  "nodig hebben."),
            ("p", "Daarmee verschilt ze van de plicht- en de gevolgenethiek. Die kijken van buitenaf en "
                  "<strong>onpartijdig</strong>: een regel voor allen, of een som over allen. De "
                  "zorgethiek begint bij <strong>deze mens, in deze relatie</strong>. Dat je voor je "
                  "eigen kind opkomt, is hier geen zwakte in je moraal maar een deel ervan."),
            ("p", "Haar wortels liggen in het <strong>feminisme</strong>. De ethiek vertrok lang van een "
                  "onafhankelijke, redelijke burger; wie afhankelijk was en wie voor hem zorgde, kwam in "
                  "dat beeld niet voor, want zorg gold als vrouwenwerk."),
            ("p", "<strong>Carol Gilligan</strong> bracht daar verandering in. Waar meisjes in bestaand "
                  "onderzoek naar morele ontwikkeling lager uitkwamen, lag volgens haar de fout niet bij "
                  "hen maar bij de <strong>maatstaf</strong>: er was maar één stem in beeld. Naast de "
                  "stem van de rechtvaardigheid staat een <strong>stem van de zorg</strong>."),
        ]),
        dict(kop="De vier fasen van Tronto", blokken=[
            ("p", "<strong>Joan Tronto</strong> ontleedt zorg in vier fasen, elk met een morele "
                  "kwaliteit die erbij hoort."),
            ("p", tabel(["Fase", "Wat er gebeurt", "Morele kwaliteit"], [
                ["zorgen om", "je merkt dat er nood is", "betrokkenheid"],
                ["zorgen voor", "je neemt er verantwoordelijkheid voor op", "verantwoordelijkheid"],
                ["zorg verlenen", "je doet het werk", "bekwaamheid"],
                ["zorg ontvangen", "je kijkt hoe het aankomt bij wie het krijgt", "wederkerigheid"],
            ])),
            ("kader", "<strong>De vier hangen aan elkaar.</strong> Een nood zien zonder er iets mee te "
                      "doen, blijft steken bij de eerste fase. Goed bedoelen zonder het te kunnen, "
                      "strandt bij de derde. En zorg die niet nakijkt hoe ze aankomt, is "
                      "eenrichtingsverkeer."),
            ("p", "Deugdethiek en zorgethiek hebben iets gemeen: beide kijken minder naar de "
                  "<strong>losse daad</strong> dan de twee andere richtingen. De ene kijkt naar de "
                  "persoon, de andere naar de relatie."),
        ]),
    ],
    onthoud=[
        "Deugdethiek vraagt: wat voor mens wil ik zijn? Goed handelen volgt uit een goed karakter.",
        "Aristoteles: vier kardinale deugden (verstandigheid, rechtvaardigheid, moed, matigheid); een deugd is het midden.",
        "Nussbaum: tien capaciteiten, mogelijkheden en geen prestaties.",
        "Hume: natuurlijke deugden uit het gevoel, artificiële uit afspraken (rechtvaardigheid).",
        "Foot: een deugd is goed voor mens en omgeving, zit in je wil, en vangt een zwakke plek op.",
        "Zorgethiek: mensen zijn kwetsbaar en afhankelijk; Gilligan bracht de stem van de zorg binnen.",
        "Tronto: zorgen om (betrokkenheid), zorgen voor (verantwoordelijkheid), zorg verlenen (bekwaamheid), zorg ontvangen (wederkerigheid).",
    ],
)

# ───────────────────────── 11. Ethiek en geluk
BUNDELS["ethiek-en-geluk-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Ethiek en geluk",
    onder="Negen visies op geluk, van Aristoteles tot Dirk De Wachter, en de vraag of goed leven en gelukkig leven samenvallen.",
    secties=[
        dict(kop="Goed handelen en geluk", blokken=[
            ("p", "Bij de meeste klassieke filosofen vallen <strong>goed leven</strong> en "
                  "<strong>gelukkig leven</strong> grotendeels samen: wie goed leeft, leeft ook goed voor "
                  "zichzelf. Dat de twee kunnen <strong>botsen</strong>, is een latere gedachte."),
            ("p", "Geluk is in de ethiek geen gevoelskwestie. Zodra je vraagt wat een "
                  "<strong>geslaagd leven</strong> is, ben je aan het nadenken over wat zou moeten en "
                  "niet over wat nu eenmaal zo is."),
        ]),
        dict(kop="De oudheid: bloeien, rust en gemoedsrust", blokken=[
            ("p", "<strong>Aristoteles</strong> noemt geluk <strong>bloeien</strong>, met het Griekse "
                  "woord <strong>eudaimonia</strong>: je leven goed en volledig leven volgens de deugd. "
                  "Dat is geen stemming maar een manier van leven, en je beoordeelt het over een "
                  "<strong>heel leven</strong>. Eén zwaluw maakt de lente niet."),
            ("p", "<strong>Epicurus</strong> ziet geluk als de <strong>rust die overblijft als pijn en "
                  "onrust weg zijn</strong>. Hij wordt vaak als een genotzoeker voorgesteld, maar zijn "
                  "genot is sober: geen pijn, geen angst, geen honger, en goede vrienden. Zijn raad: "
                  "<strong>beperk je verlangens</strong> tot wat je echt nodig hebt, want wie weinig "
                  "nodig heeft, is moeilijk ongelukkig te maken."),
            ("p", "Het <strong>stoïcisme</strong> zoekt geluk in <strong>gemoedsrust</strong>, langs "
                  "hetzelfde onderscheid als bij hun visie op vrijheid: scheiden wat in je macht ligt van "
                  "wat niet in je macht ligt. De beslissing over jouw promotie lag niet in jouw macht; je "
                  "oordeel erover wel."),
            ("p", "<strong>Oosterse wijsheden</strong> verbinden het lijden met <strong>verlangen</strong> "
                  "en met het vasthouden aan wat niet blijft. Alles verandert; wie zich vastklampt aan wat "
                  "verdwijnt, lijdt. Vandaar de nadruk op matigheid, aandacht en loslaten."),
            ("kader", "<strong>Epicurus, het stoïcisme en de oosterse wijsheden gaan dezelfde richting "
                      "uit:</strong> minder aan de haak van het geluk dat van buiten moet komen. De weg "
                      "verschilt, de richting niet."),
        ]),
        dict(kop="Kant en Bentham: is geluk de maatstaf?", blokken=[
            ("p", "Hier staan twee visies recht tegenover elkaar."),
            ("p", tabel(["", "Immanuel Kant", "Jeremy Bentham"], [
                ["geluk als maatstaf?", "nee", "ja"],
                ["waarom", "wat iemand gelukkig maakt verschilt van mens tot mens, en een moreel gebod "
                 "moet voor allen gelden", "genot min pijn, voor zoveel mensen als mogelijk"],
                ["je plicht doe je", "om de plicht", "om wat ze opbrengt"],
            ])),
            ("p", "Kant sluit geluk niet helemaal uit: wie zijn plicht doet, <strong>verdient</strong> "
                  "volgens hem geluk. Maar de twee vallen niet samen, en een daad die je stelt omdat ze "
                  "jou gelukkig maakt, is bij hem niet moreel."),
            ("kader", "<strong>Het bezwaar tegen geluk als optelsom:</strong> een getal zegt niet wie van "
                      "de betrokkenen de prijs betaalt. De som verbergt de verdeling."),
        ]),
        dict(kop="Schopenhauer, Levinas en De Wachter", blokken=[
            ("p", "<strong>Arthur Schopenhauer</strong> is de somberste van de rij. Geluk is bij hem "
                  "hoogstens het <strong>tijdelijk ontbreken van gemis</strong>. De wil drijft ons van "
                  "verlangen naar verlangen: onvervuld verlangen doet pijn, vervuld verlangen laat "
                  "verveling achter. Daarom noemt men zijn visie pessimistisch; mededogen en kunst geven "
                  "bij hem verlichting."),
            ("p", "<strong>Emmanuel Levinas</strong> legt het geluk buiten jezelf: niet in jou, maar in "
                  "de <strong>verantwoordelijkheid voor de ander</strong>. Een leven dat alleen om "
                  "jezelf draait, loopt bij hem dood."),
            ("p", "<strong>Dirk De Wachter</strong> zegt als psychiater dat <strong>verdriet en "
                  "tegenslag bij een leven horen</strong> en er mogen zijn. Zijn kritiek richt zich op de "
                  "<strong>druk om altijd gelukkig te moeten zijn</strong>, want juist die druk maakt "
                  "mensen ongelukkig. Waar hij geluk wel zoekt: in <strong>verbondenheid</strong> met "
                  "anderen en in kleine, gewone dingen. Iemand die naar je vraagt en bij wie je terechtkan."),
            ("p", tabel(["Visie", "Geluk is ..."], [
                ["Aristoteles", "bloeien: een geslaagd leven volgens de deugd"],
                ["Epicurus", "rust: geen pijn, geen onrust, met vrienden"],
                ["stoïcisme", "gemoedsrust door te scheiden wat in je macht ligt"],
                ["oosterse wijsheden", "loslaten van verlangen en van wat niet blijft"],
                ["Kant", "geen maatstaf voor moraal; wel verdiend door wie zijn plicht doet"],
                ["Bentham", "de maatstaf zelf: genot min pijn, optelbaar"],
                ["Schopenhauer", "hoogstens het tijdelijk ontbreken van gemis"],
                ["Levinas", "verantwoordelijkheid voor de ander"],
                ["De Wachter", "verbondenheid, met verdriet dat erbij hoort"],
            ])),
            ("kader", "<strong>Zet bij een vergelijkingsvraag twee dingen naast elkaar:</strong> zoekt "
                      "deze filosoof het geluk <strong>binnen</strong> de mens of <strong>bij de "
                      "ander</strong>, en is geluk bij hem <strong>wel of niet</strong> de maatstaf van "
                      "de moraal. Met die twee vragen krijg je de hele rij uit elkaar."),
        ]),
    ],
    onthoud=[
        "Bij de klassieken vallen goed leven en gelukkig leven grotendeels samen.",
        "Aristoteles: eudaimonia, bloeien over een heel leven. Epicurus: rust en sobere verlangens.",
        "Stoïcisme: gemoedsrust door wat in je macht ligt te scheiden van wat niet. Oosterse wijsheden: loslaten van verlangen.",
        "Kant: geluk is geen maatstaf. Bentham: geluk is net wél de maatstaf, en optelbaar.",
        "Schopenhauer: hoogstens het tijdelijk ontbreken van gemis. Levinas: bij de ander.",
        "De Wachter: verdriet hoort bij het leven; de druk om gelukkig te zijn maakt ongelukkig.",
    ],
)

# ───────────────────────── 12. Argumentatieleer
BUNDELS["argumentatieleer-redeneervormen-en-drogredenen-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Argumentatieleer: redeneervormen en drogredenen",
    onder="De vier basisvormen van een als-dan-redenering, welke twee geldig zijn, en de klassieke drogredenen.",
    secties=[
        dict(kop="Antecedens en consequens", blokken=[
            ("p", "Neem de uitspraak: <strong>als het regent, is de straat nat</strong>. Die bestaat uit "
                  "twee delen, en je moet de namen ervan vlot kennen."),
            ("p", tabel(["Deel", "Naam", "Betekenis van het woord"], [
                ["het regent", "het antecedens", "wat voorafgaat"],
                ["de straat is nat", "het consequens", "wat volgt"],
            ])),
            ("p", "Met die twee delen kan je vier dingen doen: het antecedens bevestigen of ontkennen, "
                  "en het consequens bevestigen of ontkennen. Dat zijn de <strong>vier basisvormen</strong>, "
                  "en twee ervan zijn geldig."),
        ]),
        dict(kop="De vier basisvormen", blokken=[
            ("p", tabel(["Vorm", "Je weet erbij", "Besluit", "Geldig?"], [
                ["bevestiging van het antecedens (modus ponens)", "het regent",
                 "de straat is nat", "ja"],
                ["bevestiging van het consequens", "de straat is nat",
                 "het regent", "nee"],
                ["ontkenning van het antecedens", "het regent niet",
                 "de straat is niet nat", "nee"],
                ["ontkenning van het consequens (modus tollens)", "de straat is niet nat",
                 "het regent niet", "ja"],
            ])),
            ("kader", "<strong>Waarom de twee middelste niet werken:</strong> de straat kan ook nat zijn "
                      "van een schoonmaakwagen. Uit het gevolg volgt de voorwaarde niet, en zonder de "
                      "voorwaarde kan het gevolg er nog altijd zijn."),
            ("p", "Een voorbeeld dat vaker opduikt dan het weer. Als je studeert, slaag je."),
            ("p", tabel(["Redenering", "Vorm", "Geldig?"], [
                ["je studeert, dus je slaagt", "modus ponens", "ja"],
                ["je bent geslaagd, dus je hebt gestudeerd", "bevestiging van het consequens", "nee"],
                ["je studeerde niet, dus je slaagt niet", "ontkenning van het antecedens", "nee"],
                ["je bent niet geslaagd, dus je studeerde niet", "modus tollens", "ja"],
            ])),
        ]),
        dict(kop="Geldig is niet hetzelfde als waar", blokken=[
            ("p", "<strong>Geldigheid</strong> gaat over de <strong>vorm</strong>: als de premissen waar "
                  "zijn, moet het besluit ook waar zijn. Over de inhoud zegt dat niets."),
            ("p", tabel(["Vraag", "Antwoord"], [
                ["kan een geldige redenering een onwaar besluit hebben?",
                 "ja, als een van de premissen onwaar is"],
                ["maakt een waar besluit een redenering geldig?",
                 "nee, dat kan toeval zijn"],
                ["heeft een ongeldige redenering altijd een onwaar besluit?",
                 "nee, ze bewijst het alleen niet"],
            ])),
            ("kader", "<strong>In het voorbeeld hierboven zit trouwens een onware premisse.</strong> Dat "
                      "studeren altijd tot slagen leidt, is niet waar. De modus tollens blijft geldig, "
                      "maar je besluit staat of valt met die eerste regel."),
        ]),
        dict(kop="Drogredenen", blokken=[
            ("p", "Een <strong>drogreden</strong> is een argument dat <strong>overtuigend lijkt maar niet "
                  "deugt</strong>. Precies die schijn maakt ze zo effectief in een discussie. Ze worden "
                  "vaak zonder opzet gebruikt, en het besluit kan om een andere reden best juist zijn."),
            ("p", tabel(["Drogreden", "Hoe ze klinkt", "Wat eraan mankeert"], [
                ["op de persoon", "jouw voorstel is niets waard, want jij hebt nooit gestudeerd",
                 "de aanval richt zich op wie het zegt in plaats van op wat er gezegd wordt"],
                ["de stroman", "je wil minder vlees eten? dus je wil geen boerderijen meer",
                 "er wordt een standpunt in je mond gelegd dat je niet innam"],
                ["de valse tweedeling", "je bent voor dit plan, of je bent tegen vooruitgang",
                 "er zijn meer mogelijkheden dan de twee die je krijgt"],
                ["het hellend vlak", "laten we dit toe, dan staan we morgen alles toe",
                 "dat die glijbaan er is, moet je eerst aantonen"],
                ["de cirkel", "dit boek is waar, want er staat in dat het waar is",
                 "wat bewezen moet worden, zit al in het bewijs"],
                ["het beroep op de massa", "iedereen doet het, dus kan het geen kwaad",
                 "hoeveel mensen iets doen, zegt niets over of het mag"],
                ["het beroep op een onbevoegde autoriteit",
                 "een bekende zanger zegt dat dit middel werkt",
                 "een deskundige aanhalen mag; iemand die hier geen deskundige is, niet"],
                ["de overhaaste generalisatie", "mijn twee buren rijden slecht, dus die straat rijdt slecht",
                 "twee gevallen zijn te weinig om over een groep te besluiten"],
                ["het beroep op de natuur", "het is natuurlijk, dus het is goed",
                 "uit wat van nature zo is, volgt niet dat het zo moet zijn"],
            ])),
            ("kader", "<strong>Het beroep op de natuur is het is-ought probleem van Hume in "
                      "zakformaat.</strong> Gif is ook natuurlijk. En de overhaaste generalisatie is "
                      "dezelfde zwakte als bij de inductie uit het thema over kennis."),
            ("p", "Een drogreden weerleg je niet door harder te spreken, maar door te "
                  "<strong>benoemen wat er aan de stap zelf mankeert</strong>: waarom volgt het besluit "
                  "niet uit wat er gezegd is?"),
        ]),
    ],
    onthoud=[
        "Antecedens = het als-deel, consequens = het dan-deel.",
        "Geldig: bevestiging van het antecedens (modus ponens) en ontkenning van het consequens (modus tollens).",
        "Ongeldig: bevestiging van het consequens en ontkenning van het antecedens.",
        "Geldigheid gaat over de vorm; een geldige redenering kan van iets onwaars vertrekken.",
        "Een drogreden lijkt overtuigend maar deugt niet; haar besluit kan toch juist zijn.",
        "Ken de negen klassieke drogredenen en kan er bij elke een voorbeeld geven.",
    ],
)

# ───────────────────────── 13. De democratische rechtsstaat
BUNDELS["de-democratische-rechtsstaat-en-haar-principes-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De democratische rechtsstaat en haar principes",
    onder="Wat een rechtsstaat is, wat democratie daaraan toevoegt, en de vijf principes die elkaar dragen.",
    secties=[
        dict(kop="Twee woorden, twee dingen", blokken=[
            ("p", "Een <strong>rechtsstaat</strong> is een staat waarin <strong>ook de overheid zelf aan "
                  "het recht gebonden is</strong>. Wie de macht uitoefent, staat niet boven de wet, en "
                  "een burger kan zijn eigen overheid voor de rechter brengen."),
            ("p", "<strong>Democratisch</strong> voegt daar iets anders aan toe: de macht komt van het "
                  "<strong>volk</strong>, dat zijn vertegenwoordigers verkiest."),
            ("kader", "<strong>Die twee zijn niet hetzelfde.</strong> Een staat kan netjes zijn wetten "
                      "volgen zonder verkiezingen, en een staat kan verkiezingen houden en zich daarna "
                      "niet aan het recht houden. Een land waar de winnaar rechters kan afzetten die hem "
                      "tegenspreken, heeft wel verkiezingen maar geen rechtsstaat."),
            ("p", "De waarden waarop onze rechtsstaat rust, komen uit de <strong>Verlichting</strong>: "
                  "<strong>vrijheid</strong>, <strong>gelijkheid</strong> en de "
                  "<strong>waardigheid</strong> van elke mens. Je vindt ze terug aan het begin van de "
                  "grondwet en in de mensenrechten."),
        ]),
        dict(kop="De vijf principes", blokken=[
            ("p", tabel(["Principe", "Wat het zegt"], [
                ["het meerderheidsprincipe", "een beslissing geldt als de meerderheid ze steunt"],
                ["een constitutie of grondwet", "de hoogste wet, die de macht afbakent"],
                ["de scheiding der machten", "wetten maken, uitvoeren en recht spreken liggen in "
                 "verschillende handen"],
                ["onafhankelijke en onpartijdige rechtspraak",
                 "een rechter die geen bevel krijgt en geen belang heeft"],
                ["fundamentele rechten en vrijheden",
                 "rechten die elke mens heeft en die de overheid moet eerbiedigen"],
            ])),
            ("kader", "<strong>De vijf dragen elkaar.</strong> Grondrechten zonder onafhankelijke rechter "
                      "zijn tekst op papier. Een grondwet zonder scheiding der machten geeft niemand "
                      "tegengewicht. Valt er één weg, dan verliezen de andere hun kracht."),
            ("p", "Het <strong>meerderheidsprincipe</strong> zorgt dat er een beslissing komt zonder dat "
                  "iedereen het eens moet zijn. De keerzijde is dat een meerderheid een minderheid kan "
                  "overstemmen. Daarom mag een meerderheid niet alles beslissen: de "
                  "<strong>grondrechten</strong> beschermen de minderheid tegen haar wil."),
            ("p", "De <strong>grondwet</strong> staat boven de gewone wetten, want ze legt de spelregels "
                  "vast waaraan de wetgever zelf gebonden is. Daarom is ze ook "
                  "<strong>moeilijker te wijzigen</strong>: een meerderheid van vandaag mag de spelregels "
                  "niet in haar eigen voordeel omgooien. Ze bevat niet alle wetten van een land; haar "
                  "taak is de macht afbakenen."),
        ]),
        dict(kop="Grondrechten", blokken=[
            ("p", "<strong>Fundamentele rechten en vrijheden</strong> staan in de grondwet en in "
                  "internationale verdragen, zoals het Europees Verdrag voor de Rechten van de Mens. "
                  "Denk aan de vrijheid van meningsuiting, van vereniging en van godsdienst, en aan het "
                  "recht op een eerlijk proces."),
            ("p", "Mogen ze <strong>beperkt</strong> worden? Ja, maar binnen grenzen: de beperking moet "
                  "in de <strong>wet</strong> staan, een doel dienen, en door een <strong>rechter</strong> "
                  "te toetsen zijn. Vrijheid van meningsuiting dekt geen laster, en een regering die "
                  "tijdens een crisis de pers beperkt, moet zich aan die voorwaarden houden."),
            ("kader", "<strong>Waarom het recht op een eerlijk proces zo zwaar weegt:</strong> zonder dat "
                      "recht zijn al je andere rechten niet te verdedigen. Een recht dat je nergens kan "
                      "laten gelden, is geen recht."),
        ]),
        dict(kop="Onafhankelijk en onpartijdig", blokken=[
            ("p", "Twee woorden die vaak samen staan en twee verschillende eisen zijn."),
            ("p", tabel(["Eis", "Gaat over", "Voorbeeld van een probleem"], [
                ["onafhankelijkheid", "de verhouding met de andere machten",
                 "een minister die een rechter zegt wat hij moet beslissen"],
                ["onpartijdigheid", "de verhouding met de partijen in de zaak",
                 "een rechter die moet oordelen over een zaak van zijn eigen zus"],
            ])),
            ("p", "Een onafhankelijke rechter is wél aan de <strong>wet</strong> gebonden. Zijn "
                  "onafhankelijkheid betekent dat niemand hem kan voorschrijven <strong>hoe</strong> hij "
                  "die wet toepast. En bij twijfel over onpartijdigheid trekt hij zich terug, niet omdat "
                  "hij zeker partijdig zou zijn, maar omdat de schijn al genoeg is."),
            ("p", "Daarmee is de rechtsstaat in de eerste plaats een <strong>bescherming van de "
                  "burger</strong>: hij kan zich op het recht beroepen tegen wie macht over hem heeft. "
                  "Gelijk krijgen is niet gegarandeerd; gehoord worden door een onafhankelijke rechter wel."),
        ]),
    ],
    onthoud=[
        "Rechtsstaat = ook de overheid is aan het recht gebonden. Democratie = de macht komt van het volk.",
        "De twee zijn niet hetzelfde en vullen elkaar aan.",
        "Vijf principes: meerderheid, grondwet, scheiding der machten, onafhankelijke rechtspraak, grondrechten.",
        "Grondrechten beschermen de minderheid tegen de meerderheid; beperken kan enkel bij wet en toetsbaar.",
        "Een grondwet is moeilijker te wijzigen dan een gewone wet.",
        "Onafhankelijk = geen bevel van de andere machten. Onpartijdig = geen band met de partijen.",
    ],
)

# ───────────────────────── 14. De scheiding der machten
BUNDELS["de-scheiding-der-machten-en-de-rechterlijke-macht-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De scheiding der machten en de rechterlijke macht",
    onder="Drie machten met hun instellingen, hoe ze elkaar in het oog houden, en wat een schending is.",
    secties=[
        dict(kop="Drie machten, drie instellingen", blokken=[
            ("p", "De <strong>scheiding der machten</strong> betekent dat wetten maken, wetten uitvoeren "
                  "en recht spreken in <strong>verschillende handen</strong> liggen. Zo kan niemand "
                  "tegelijk de regel maken, hem toepassen en over zijn eigen fouten oordelen. De "
                  "gedachte wordt verbonden met <strong>Montesquieu</strong>, in de 18de eeuw."),
            ("p", tabel(["Macht", "Instelling", "Functie"], [
                ["de wetgevende macht", "de parlementen",
                 "de wetten maken en de regering controleren"],
                ["de uitvoerende macht", "de regeringen en hun administratie",
                 "de wetten uitvoeren en het land besturen"],
                ["de rechterlijke macht", "de hoven en de rechtbanken",
                 "de wet toepassen op een concreet geschil en recht spreken"],
            ])),
            ("p", "In België is er niet één parlement maar meerdere: het federale parlement en die van "
                  "de gemeenschappen en gewesten, elk met hun regering."),
            ("kader", "<strong>Waarom dit zo belangrijk is:</strong> macht die zichzelf controleert, "
                      "controleert niets. Dat het bestuur daardoor trager werkt, is hier geen fout maar "
                      "een bedoeling."),
            ("p", "Let op het woord <strong>scheiding</strong>, niet afzondering. De machten houden "
                  "elkaar juist <strong>in het oog</strong> en werken op elkaar in. Elkaar controleren "
                  "hoort bij het ontwerp."),
        ]),
        dict(kop="Controle en evenwicht", blokken=[
            ("p", "Controle en evenwicht betekent dat elke macht <strong>middelen</strong> heeft om de "
                  "andere twee binnen hun grenzen te houden. Niet een gelijke grootte, wel een "
                  "wederzijdse rem."),
            ("p", tabel(["Wie controleert", "Wat hij kan"], [
                ["het parlement", "de regering ondervragen, onderzoek doen en over de begroting stemmen"],
                ["het Grondwettelijk Hof", "nagaan of een wet met de grondwet in overeenstemming is"],
                ["de Raad van State", "beslissingen van het bestuur nakijken en vernietigen"],
                ["de hoven en rechtbanken", "de daden van de overheid in een concreet geschil toetsen"],
            ])),
            ("kader", "<strong>Zonder de steun van het parlement geraakt een regering niet aan haar geld "
                      "en niet aan haar wetten.</strong> Dat is het sterkste controlemiddel dat er is."),
        ]),
        dict(kop="De rechterlijke macht beschermd", blokken=[
            ("p", "Rechters worden in België <strong>niet verkozen</strong>. Een rechter die stemmen moet "
                  "halen, wordt afhankelijk van wat populair is; zijn benoeming loopt daarom via een "
                  "onafhankelijke instelling die op <strong>bekwaamheid</strong> selecteert."),
            ("p", "Daar hoort de <strong>vaste benoeming</strong> bij: wie niet afgezet kan worden, kan "
                  "onbevangen tegen de macht in oordelen. Een rechter die zijn plaats kan verliezen door "
                  "een onwelkom vonnis, is geen onafhankelijke rechter."),
            ("p", "En hij moet zijn vonnis <strong>motiveren</strong>, zodat iedereen kan nagaan waarop "
                  "zijn beslissing berust. Een gemotiveerd vonnis is te controleren en in beroep aan te "
                  "vechten; dat hoort bij een eerlijk proces."),
            ("weetje", "De minister van Justitie organiseert justitie als dienst: gebouwen, personeel, "
                       "middelen. Hij beslist nooit hoe een rechter moet oordelen."),
        ]),
        dict(kop="Schendingen", blokken=[
            ("p", "Een <strong>schending</strong> van de scheiding der machten is geen abstracte zaak. "
                  "Herken de voorbeelden, en herken ook wat géén schending is."),
            ("p", tabel(["Situatie", "Schending?"], [
                ["een minister zet een rechter onder druk over een vonnis", "ja"],
                ["een parlement stemt een wet die één lopende rechtszaak beslecht",
                 "ja, een wet is algemeen"],
                ["een regering weigert een vonnis uit te voeren dat haar niet past",
                 "ja, de weg tegen een vonnis is het beroep"],
                ["het parlement ondervraagt de regering", "nee, dat is de controle zoals bedoeld"],
                ["een rechter motiveert zijn vonnis", "nee, dat is zijn plicht"],
            ])),
            ("kader", "<strong>De niet-uitvoering van vonnissen staat niet toevallig in de lijst van "
                      "actuele thema's.</strong> Wie een uitspraak hoort en daarna niets ziet gebeuren, "
                      "vraagt zich af waarvoor het proces diende."),
        ]),
    ],
    onthoud=[
        "Scheiding der machten: maken, uitvoeren en recht spreken in verschillende handen. Verbonden met Montesquieu.",
        "Wetgevende macht = parlementen, uitvoerende = regeringen, rechterlijke = hoven en rechtbanken.",
        "Controle en evenwicht: het parlement controleert de regering, het Grondwettelijk Hof toetst wetten, de Raad van State het bestuur.",
        "Rechters worden niet verkozen en zijn vast benoemd, zodat ze onbevangen kunnen oordelen.",
        "Een rechter moet zijn vonnis motiveren.",
        "Schending: druk op een rechter, een wet voor één zaak, een vonnis niet uitvoeren.",
    ],
)

# ───────────────────────── 15. De functies van justitie en de deontologie
BUNDELS["de-functies-van-justitie-de-rechtspraak-en-de-deontologie-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De functies van justitie, de rechtspraak en de deontologie",
    onder="Vijf functies van justitie, vier principes van de rechtspraak, en beroepsgeheim, discretieplicht en meldingsplicht.",
    secties=[
        dict(kop="Vijf functies van justitie", blokken=[
            ("p", "Justitie doet meer dan straffen. De fiche noemt vijf functies naast elkaar, en "
                  "bestraffing is er maar <strong>één</strong> van."),
            ("p", tabel(["Functie", "Wat ze doet", "Voorbeeld"], [
                ["preventie", "voorkomen dat er misdrijven en conflicten ontstaan",
                 "dat de wet bestaat en overtredingen gevolgen hebben, houdt al veel mensen tegen"],
                ["veiligheid", "mensen beschermen tegen gevaar",
                 "iemand uit de buurt van zijn slachtoffer houden"],
                ["ordehandhaving", "de orde herstellen en bewaren",
                 "optreden na rellen of bij een bezetting"],
                ["conflictbeslechting", "een geschil tussen partijen met een beslissing afsluiten",
                 "een vonnis over een huurgeschil"],
                ["bestraffing", "een dader een passende straf opleggen",
                 "een werkstraf, een boete of een gevangenisstraf"],
            ])),
            ("kader", "<strong>Preventie is het werk dat je niet ziet omdat het lukt.</strong> En "
                      "conflictbeslechting is typisch voor het burgerlijk recht: zonder rechter zou een "
                      "geschil blijven duren of met geweld eindigen."),
        ]),
        dict(kop="Vier principes van de hedendaagse rechtspraak", blokken=[
            ("p", tabel(["Principe", "Wat het betekent"], [
                ["het vermoeden van onschuld",
                 "je bent onschuldig tot een rechter je schuld heeft vastgesteld; het bewijs moet komen "
                 "van wie vervolgt en twijfel valt in jouw voordeel uit"],
                ["onafhankelijkheid en onpartijdigheid",
                 "de rechter krijgt geen bevel van de andere machten en heeft geen band met de partijen"],
                ["openbaarheid",
                 "een zitting en een uitspraak zijn in beginsel voor iedereen toegankelijk"],
                ["hoor en wederhoor",
                 "elke partij krijgt de kans om op de argumenten van de andere te antwoorden"],
            ])),
            ("p", "<strong>Openbaarheid</strong> is de regel, met uitzonderingen waar een zwaarder belang "
                  "meespeelt. Een zitting kan met <strong>gesloten deuren</strong> doorgaan, bijvoorbeeld "
                  "in het belang van een kind of van de privacy. De zittingen van de jeugdrechtbank zijn "
                  "daarom niet openbaar."),
            ("kader", "<strong>Trial by media raakt aan het vermoeden van onschuld.</strong> Een krant die "
                      "een verdachte al een dader noemt, spreekt een oordeel uit dat nog niet gevallen is. "
                      "Dat thema komt terug bij de actuele thema's."),
        ]),
        dict(kop="De rol van justitie in de samenleving", blokken=[
            ("p", "De fiche laat je over drie dingen nadenken."),
            ("p", tabel(["Rol", "Hoe je dat ziet"], [
                ["bij veranderende maatschappelijke normen",
                 "wat vroeger strafbaar was, is dat vandaag soms niet meer, en omgekeerd; recht en "
                 "samenleving bewegen samen, al loopt het recht meestal achter"],
                ["bij het regelen van ons dagelijks leven",
                 "een huurcontract, een aankoop, een scheiding, een nalatenschap: het recht zit in "
                 "duizend gewone dingen zonder dat er een rechter aan te pas komt"],
                ["bij meer rechtvaardigheid en gelijkheid",
                 "iedereen volgens dezelfde regels behandelen, ongeacht wie hij is"],
            ])),
            ("weetje", "Gelijkheid voor de wet is de belofte. Dat die in de praktijk niet altijd uitkomt, "
                       "omdat een procedure geld en kennis vraagt, is precies waarover de fiche je laat "
                       "nadenken. Daarom bestaat juridische bijstand."),
        ]),
        dict(kop="Deontologie in de welzijnssector", blokken=[
            ("p", "<strong>Deontologie</strong> zijn de <strong>beroepsregels</strong> die een "
                  "beroepsgroep voor zichzelf opstelt. Elke beroepsgroep heeft eigen vragen: een "
                  "hulpverlener, een arts en een advocaat hebben elk hun code."),
            ("p", tabel(["", "Wetgeving", "Deontologische code"], [
                ["komt van", "de wetgever", "de beroepsgroep zelf"],
                ["geldt voor", "iedereen", "wie dat beroep uitoefent"],
                ["bij schending", "een sanctie van de rechter",
                 "een sanctie van de beroepsorde of de werkgever"],
            ])),
            ("kader", "<strong>Een code komt bovenop de wet en nooit in haar plaats.</strong> Dezelfde "
                      "handeling kan tegelijk tegen de code en tegen de wet ingaan; het beroepsgeheim is "
                      "daar het voorbeeld van."),
            ("p", "Drie aspecten moet je uit elkaar kunnen houden."),
            ("p", tabel(["Aspect", "Wat het is", "Hoe streng"], [
                ["het beroepsgeheim",
                 "wat iemand je in vertrouwen vertelt, mag je niet verder vertellen",
                 "het strengst, en voor sommige beroepen ook in de wet, met een straf erop"],
                ["de discretieplicht",
                 "terughoudend zijn over alles wat je op je werk verneemt",
                 "ruimer maar minder streng; ook over een collega of een dossier dat niet het jouwe is"],
                ["de meldingsplicht",
                 "in bepaalde ernstige situaties moet je spreken in plaats van zwijgen",
                 "ze doorbreekt het zwijgen bij ernstig en dreigend gevaar"],
            ])),
            ("p", "Het <strong>beroepsgeheim</strong> beschermt niet de hulpverlener maar "
                  "<strong>wie hulp zoekt</strong>: zonder die zekerheid durft niemand nog iets te "
                  "vertellen. En het is <strong>geen vrijgeleide om weg te kijken</strong>: wie een kind "
                  "in acuut gevaar ziet, kan zich er niet achter verschuilen. Hulp weigeren aan iemand "
                  "in groot gevaar is strafbaar."),
            ("kader", "<strong>Twee casussen om te herkennen.</strong> Een kind vertelt dat het thuis "
                      "geslagen wordt en dat het vanavond opnieuw dreigt te gebeuren: ernstig en dreigend "
                      "gevaar, dus de meldingsplicht. Een medewerker vertelt op een feestje over een "
                      "dossier zonder de naam te noemen: de discretieplicht, want details maken een mens "
                      "herkenbaar en wie dit hoort weet voortaan dat je over je cliënten praat."),
            ("p", "Daarom is een code nooit een lijst met kant-en-klare antwoorden: plichten kunnen in "
                  "één situatie <strong>tegen elkaar in gaan</strong>. Zwijgen en melden kunnen in "
                  "dezelfde casus beide opkomen, en dan vraagt het een afweging."),
        ]),
    ],
    onthoud=[
        "Vijf functies: preventie, veiligheid, ordehandhaving, conflictbeslechting, bestraffing.",
        "Vier principes: vermoeden van onschuld, onafhankelijkheid en onpartijdigheid, openbaarheid, hoor en wederhoor.",
        "Openbaarheid is de regel; gesloten deuren bij een zwaarder belang, zoals bij de jeugdrechtbank.",
        "Deontologie komt van het beroep zelf, wetgeving van de wetgever; de code komt bovenop de wet.",
        "Beroepsgeheim is het strengst, discretieplicht is ruimer en minder streng, meldingsplicht doorbreekt het zwijgen.",
        "Het beroepsgeheim beschermt wie hulp zoekt, en is geen vrijgeleide om weg te kijken.",
    ],
)

# ───────────────────────── 16. Actuele thema's binnen recht
BUNDELS["actuele-thema-s-binnen-recht-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Actuele thema's binnen recht",
    onder="Het schema met de redeneeractiviteiten, en de dertien thema's die de fiche oplijst, telkens met de argumenten van beide kanten.",
    secties=[
        dict(kop="Het schema met de redeneeractiviteiten", blokken=[
            ("p", "Bij een actueel thema bestaat er geen juist antwoord over wat je ervan moet denken. "
                  "Wat wel gevraagd wordt, is dat je er <strong>ordelijk</strong> over nadenkt. Daarvoor "
                  "geeft de fiche een schema met drie activiteiten."),
            ("p", tabel(["Activiteit", "Wat je doet"], [
                ["1. beschrijven",
                 "de context schetsen: voor wie is het een probleem, waarom, waar speelt het zich af, "
                 "en hoe is het ontstaan; en standpunten vergelijken"],
                ["2. verklaren",
                 "meerdere oorzaken inbrengen en die ordenen per invalshoek"],
                ["3. oplossingen evalueren",
                 "oplossingen herkennen met hun verschillende perspectieven, en ook de ongewenste "
                 "gevolgen van een aanpak benoemen"],
            ])),
            ("p", "Bij het beschrijven gebruik je vijf <strong>invalshoeken</strong>: "
                  "<strong>economisch</strong>, <strong>sociaal</strong>, <strong>cultureel</strong>, "
                  "<strong>politiek</strong> en <strong>juridisch</strong>. Dezelfde kwestie ziet van "
                  "elke kant anders uit."),
            ("p", "Daarnaast vraagt het schema <strong>redeneren met bewijs</strong>: meerdere bronnen "
                  "inzetten en vergelijken, letten op betrouwbare en valide data, en gegevens uit "
                  "onderzoek gebruiken om je uitspraken over oorzaken en oplossingen te onderbouwen."),
            ("kader", "<strong>Elke oplossing heeft een prijs.</strong> Die erkennen is geen zwakte van "
                      "je betoog maar een sterkte, en het staat met zoveel woorden in het schema."),
        ]),
        dict(kop="Thema's rond het proces", blokken=[
            ("p", tabel(["Thema", "Waar het over gaat", "Argumenten"], [
                ["afschaffing van de volksjury",
                 "twaalf burgers, bij lot aangewezen uit de kiezerslijsten, oordelen in een "
                 "assisenzaak over de schuld",
                 "vóór behouden: recht spreken blijft iets van de samenleving zelf. Vóór afschaffen: "
                 "een assisenproces duurt lang, kost veel en weegt zwaar op de juryleden"],
                ["procedurefouten",
                 "een fout tegen de vormregels van het onderzoek of het proces",
                 "de vormregels beschermen de rechten van de verdediging, en toch kan een gestrande "
                 "zaak voor een slachtoffer heel onrechtvaardig voelen"],
                ["media en justitie, trial by media",
                 "een zaak wordt in de pers al beslecht voor de rechter oordeelde",
                 "het vermoeden van onschuld tegenover de persvrijheid, twee grondrechten die tegen "
                 "elkaar in gaan"],
                ["de kloof tussen burger en justitie",
                 "vertrouwen en wantrouwen",
                 "traagheid, kostprijs en moeilijke taal spelen alle drie mee; wie justitie niet "
                 "begrijpt, vertrouwt haar ook moeilijker"],
                ["hervorming van de gerechtelijke procedure",
                 "procedures sneller, eenvoudiger en begrijpelijker maken",
                 "een zaak die jaren duurt, voelt voor niemand als recht"],
                ["(niet)uitvoering van vonnissen",
                 "straffen die niet of te laat uitgevoerd worden",
                 "een straf die niet uitgevoerd wordt, ondermijnt het vertrouwen in justitie"],
            ])),
            ("kader", "<strong>Enkel het Hof van Assisen werkt met een jury.</strong> In alle andere "
                      "rechtbanken beslissen beroepsrechters."),
        ]),
        dict(kop="Thema's rond de straf en haar uitvoering", blokken=[
            ("p", tabel(["Thema", "Waar het over gaat"], [
                ["alternatieve straffen",
                 "een straf die niet in een gevangenis wordt uitgezeten: de enkelband (elektronisch "
                 "toezicht waarbij je je straf thuis uitzit onder controle) en de werkstraf (onbetaalde "
                 "arbeid voor de samenleving, met een vervangende straf als je ze niet uitvoert)"],
                ["strengere strafmaten",
                 "voorstanders wijzen op afschrikking en op het gevoel van rechtvaardigheid; "
                 "tegenstanders op overbevolkte gevangenissen en op herval na de straf"],
                ["internering",
                 "een maatregel, geen straf, voor wie een misdrijf pleegde maar door een stoornis niet "
                 "toerekeningsvatbaar is; met behandeling en met het oog op de veiligheid"],
                ["nieuwe vormen van strafuitvoering",
                 "transitiehuizen en detentiehuizen: kleine huizen in de buurt, gericht op de terugkeer "
                 "naar de samenleving"],
                ["uithandengeving bij minderjarigen",
                 "een jeugdrechter geeft een zaak van een oudere minderjarige uit handen aan het "
                 "strafrecht; het kan vanaf zestien jaar en bij zware feiten"],
                ["verjaring",
                 "na een bepaalde termijn kan een misdrijf niet meer vervolgd worden, omdat bewijs "
                 "verdwijnt en getuigen vergeten; voor sommige zeer ernstige misdrijven geldt vandaag "
                 "geen verjaring meer"],
                ["vervroegde en voorwaardelijke vrijlating",
                 "iemand komt vrij voor het einde van zijn straf, met voorwaarden erbij; wie zich er "
                 "niet aan houdt, kan terug"],
            ])),
            ("kader", "<strong>Het argument voor alternatieve straffen in één zin:</strong> wie na zijn "
                      "straf nog een huis, werk en een gezin heeft, hervalt minder snel."),
            ("p", "Bij <strong>internering</strong> raakt het recht aan het debat over de vrije wil uit "
                  "de filosofie. Een <strong>straf</strong> veronderstelt <strong>schuld</strong>; een "
                  "<strong>maatregel</strong> vertrekt van zorg en veiligheid. Wie niet anders kón, kan "
                  "je moeilijk schuldig noemen."),
            ("weetje", "Bij transitiehuizen is de gedachte dat iemand die vanuit een cel plots buiten "
                       "staat, veel sneller hervalt dan wie stap voor stap terugkeert. Let op het "
                       "verschil met een justitiehuis: dat is een dienst waar je met vragen terechtkan, "
                       "geen woonplaats."),
        ]),
    ],
    onthoud=[
        "Drie redeneeractiviteiten: beschrijven, verklaren, oplossingen evalueren. In die orde.",
        "Vijf invalshoeken: economisch, sociaal, cultureel, politiek, juridisch.",
        "Redeneren met bewijs: meerdere bronnen vergelijken en op betrouwbaarheid nakijken.",
        "Noem bij elk thema de argumenten van beide kanten; er is geen juist antwoord over wat je moet denken.",
        "Enkel assisen werkt met een volksjury van twaalf burgers.",
        "Internering is een maatregel en geen straf; uithandengeving kan vanaf zestien jaar bij zware feiten.",
    ],
)

# ───────────────────────── 17. Buitengerechtelijke procedures en juridische bijstand
BUNDELS["buitengerechtelijke-procedures-en-juridische-bijstand-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Buitengerechtelijke procedures en juridische bijstand",
    onder="Bemiddeling, verzoening en arbitrage, en waar je terechtkan voor juridisch advies.",
    secties=[
        dict(kop="Een conflict oplossen zonder vonnis", blokken=[
            ("p", "Niet elk conflict hoort voor een rechter. Een procedure duurt lang, kost geld en "
                  "eindigt met een winnaar en een verliezer. Daarom bestaan er "
                  "<strong>buitengerechtelijke</strong> wegen: oplossingen <strong>buiten</strong> de "
                  "rechtbank om."),
            ("p", tabel(["Weg", "Wat gebeurt er", "Wie beslist"], [
                ["bemiddeling",
                 "een neutrale bemiddelaar begeleidt het gesprek tussen de partijen en helpt hen zelf "
                 "tot een akkoord te komen",
                 "de partijen zelf; de bemiddelaar beslist niets"],
                ["verzoening of minnelijke schikking",
                 "de partijen regelen hun geschil zelf met een afspraak, soms met een akkoord dat door "
                 "de rechter bekrachtigd wordt",
                 "de partijen zelf"],
                ["arbitrage",
                 "de partijen leggen hun geschil voor aan een of meer arbiters die ze samen kiezen, "
                 "buiten de rechtbank",
                 "de arbiter, en zijn uitspraak bindt de partijen"],
            ])),
            ("kader", "<strong>Het verschil in één vraag: wie beslist?</strong> Bij bemiddeling en "
                      "verzoening beslissen de partijen zelf. Bij arbitrage beslist een derde, net als "
                      "bij een rechter, maar die derde is door de partijen zelf gekozen."),
            ("p", "De voordelen van bemiddeling: <strong>sneller</strong>, meestal "
                  "<strong>goedkoper</strong>, <strong>vertrouwelijk</strong>, en de relatie blijft "
                  "beter overeind. Dat laatste weegt zwaar waar mensen daarna nog met elkaar verder "
                  "moeten, bijvoorbeeld ouders na een scheiding of twee buren."),
            ("p", "De keerzijde: het werkt <strong>alleen als beide partijen willen</strong>. Wie "
                  "weigert te praten, kan niet verplicht worden tot een akkoord. Lukt de bemiddeling "
                  "niet, dan staat de weg naar de rechter nog altijd open; je verliest je recht om te "
                  "procederen er niet mee."),
            ("weetje", "Bemiddeling bestaat ook <strong>binnen</strong> een procedure. Een rechter kan "
                       "voorstellen om eerst te bemiddelen, en in de familie- en jeugdrechtbank gebeurt "
                       "dat vaak, omdat de partijen daar bijna altijd met elkaar verder moeten."),
        ]),
        dict(kop="Juridische bijstand: twee lijnen", blokken=[
            ("p", "Rechten hebben is één ding; weten welke je hebt is iets anders. Daarom bestaat er "
                  "juridische bijstand in <strong>twee lijnen</strong>."),
            ("p", tabel(["", "Eerstelijnsbijstand", "Tweedelijnsbijstand"], [
                ["wat je krijgt", "een eerste advies, een algemene inlichting, een doorverwijzing",
                 "een advocaat die je dossier opneemt en je voor de rechtbank bijstaat"],
                ["hoe lang", "een kort gesprek", "zolang je zaak duurt"],
                ["prijs", "gratis en voor iedereen", "gratis of gedeeltelijk gratis als je inkomen laag genoeg is"],
            ])),
            ("p", "De tweede lijn noemen mensen vaak de <strong>pro deo advocaat</strong>. Hij wordt "
                  "dan door de overheid vergoed in plaats van door jou. Of je er recht op hebt, hangt "
                  "van je inkomen af; het is dus geen gunst maar een recht als je eronder zit."),
            ("kader", "<strong>Waarom dit bestaat:</strong> zonder bijstand zou gelijkheid voor de wet "
                      "in de praktijk afhangen van je bankrekening. Dat is precies het bezwaar dat bij "
                      "de rol van justitie terugkomt."),
        ]),
        dict(kop="Waar kan je terecht", blokken=[
            ("p", tabel(["Waar", "Waarvoor"], [
                ["het justitiehuis",
                 "een dienst van de overheid met informatie over justitie, slachtofferonthaal en de "
                 "opvolging van straffen en maatregelen"],
                ["de wetswinkel", "gratis juridisch eerstelijnsadvies"],
                ["het CAW, het centrum algemeen welzijnswerk",
                 "hulp bij problemen die veel breder gaan dan het juridische: wonen, geld, relaties, "
                 "geweld; vaak de eerste plaats waar iemand binnenstapt"],
                ["het OCMW", "sociale hulp en bijstand van de gemeente, ook financieel"],
                ["het Bureau voor Juridische Bijstand", "een pro deo advocaat aanvragen"],
            ])),
            ("weetje", "Een <strong>justitiehuis</strong> is geen rechtbank en geen woonplaats. Verwar "
                       "het niet met een <strong>detentiehuis</strong> of een "
                       "<strong>transitiehuis</strong>, waar iemand een straf uitzit."),
            ("p", "De fiche vraagt je ook om een <strong>casus</strong> te kunnen plaatsen. Iemand met "
                  "een huurgeschil en weinig inkomen gaat eerst naar de eerste lijn voor advies, en kan "
                  "daarna via het Bureau voor Juridische Bijstand een advocaat krijgen. Twee buren die "
                  "ruzie maken over een haag hebben meer aan bemiddeling dan aan een proces: ze blijven "
                  "buren."),
        ]),
    ],
    onthoud=[
        "Bemiddeling en verzoening: de partijen beslissen zelf. Arbitrage: de arbiter beslist en bindt hen.",
        "Bemiddeling is sneller, goedkoper en vertrouwelijk, en spaart de relatie, maar vraagt dat beiden willen.",
        "Mislukt een bemiddeling, dan kan je nog altijd naar de rechter.",
        "Eerste lijn: gratis eerste advies voor iedereen. Tweede lijn: een advocaat, gratis bij een laag inkomen.",
        "Pro deo betekent dat de overheid de advocaat vergoedt, niet dat hij minder waard is.",
        "Justitiehuis, wetswinkel, CAW, OCMW en het Bureau voor Juridische Bijstand zijn de adressen.",
    ],
)

# ───────────────────────── 18. De gerechtelijke piramide
BUNDELS["de-gerechtelijke-piramide-rechtbanken-en-hoven-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De gerechtelijke piramide: rechtbanken en hoven",
    onder="Welke rechtbank waarvoor bevoegd is, van het vredegerecht tot het Hof van Cassatie.",
    secties=[
        dict(kop="Twee soorten bevoegdheid", blokken=[
            ("p", "Voor je weet naar welke rechtbank je moet, moet je twee vragen stellen."),
            ("p", tabel(["Vraag", "Naam", "Antwoord"], [
                ["Waarover gaat het?", "de materiële bevoegdheid",
                 "de aard van de zaak bepaalt de soort rechtbank: een huurgeschil, een verkeersboete, "
                 "een ontslag en een faillissement gaan elk naar een andere"],
                ["Waar is het gebeurd?", "de territoriale bevoegdheid",
                 "het gebied bepaalt welke rechtbank van die soort; meestal de plaats van de woonplaats "
                 "van de verweerder of van de feiten"],
            ])),
            ("kader", "<strong>Pas de twee samen toe.</strong> Een conflict van 3.000 euro tussen twee "
                      "mensen uit Hasselt hoort bij het vredegerecht (materieel) van het kanton Hasselt "
                      "(territoriaal)."),
        ]),
        dict(kop="De eerste verdieping: rechtbanken", blokken=[
            ("p", tabel(["Rechtbank", "Waarvoor"], [
                ["het vredegerecht",
                 "de rechtbank het dichtst bij de burger: kleinere geschillen tot 5.000 euro, "
                 "huurzaken, geschillen tussen buren; één vrederechter, zonder jury"],
                ["de politierechtbank",
                 "verkeersovertredingen en verkeersongevallen"],
                ["de rechtbank van eerste aanleg",
                 "de grote rechtbank met vijf afdelingen (zie hieronder)"],
                ["de arbeidsrechtbank",
                 "geschillen over werk en over sociale zekerheid: een ontslag, een arbeidsongeval, "
                 "een uitkering"],
                ["de ondernemingsrechtbank",
                 "geschillen tussen ondernemingen, en faillissementen"],
            ])),
            ("p", "De <strong>rechtbank van eerste aanleg</strong> heeft vijf afdelingen."),
            ("p", tabel(["Afdeling", "Waarvoor"], [
                ["de burgerlijke rechtbank", "geschillen tussen burgers of ondernemingen"],
                ["de correctionele rechtbank", "misdrijven, de zwaardere strafzaken"],
                ["de familierechtbank", "scheiding, onderhoudsgeld, de regeling voor de kinderen"],
                ["de jeugdrechtbank", "minderjarigen in een zorgwekkende situatie of met een als misdrijf omschreven feit"],
                ["de strafuitvoeringsrechtbank", "beslissingen over hoe een straf verder wordt uitgevoerd"],
            ])),
            ("weetje", "De zittingen van de <strong>jeugdrechtbank</strong> zijn niet openbaar. Dat is "
                       "een uitzondering op de openbaarheid van de rechtspraak, in het belang van het "
                       "kind."),
        ]),
        dict(kop="De hogere verdiepingen: hoven", blokken=[
            ("p", tabel(["Hof", "Waarvoor"], [
                ["het hof van beroep",
                 "behandelt de zaak een tweede keer, over de feiten én het recht, nadat een partij "
                 "beroep aantekende tegen het vonnis van de rechtbank van eerste aanleg"],
                ["het Hof van Assisen",
                 "de zwaarste misdaden, met een volksjury van twaalf burgers die over de schuld "
                 "beslist; het komt samen per zaak en is dus geen vaste rechtbank"],
                ["het Hof van Cassatie",
                 "het hoogste hof; kijkt niet meer naar de feiten maar naar de vraag of het recht "
                 "juist is toegepast, en verbreekt een uitspraak die de wet schendt"],
            ])),
            ("kader", "<strong>Cassatie oordeelt niet opnieuw over de zaak.</strong> Het verbreekt een "
                      "uitspraak en stuurt de zaak terug naar een ander hof, dat ze dan opnieuw "
                      "behandelt. Dat is het hele verschil met beroep."),
            ("p", "Daarnaast staan er twee hoven <strong>naast</strong> de piramide, met een eigen "
                  "taak: het <strong>Grondwettelijk Hof</strong> toetst wetten aan de Grondwet, en de "
                  "<strong>Raad van State</strong> beoordeelt beslissingen van de overheid. Die horen "
                  "bij de scheiding der machten."),
        ]),
        dict(kop="Vonnis of arrest, en de weg omhoog", blokken=[
            ("p", "Een uitspraak van een <strong>rechtbank</strong> heet een "
                  "<strong>vonnis</strong>; een uitspraak van een <strong>hof</strong> heet een "
                  "<strong>arrest</strong>. Dat is een kwestie van woordgebruik, niet van inhoud."),
            ("p", tabel(["Van", "Beroep bij"], [
                ["het vredegerecht of de politierechtbank", "de rechtbank van eerste aanleg"],
                ["de rechtbank van eerste aanleg", "het hof van beroep"],
                ["het hof van beroep", "het Hof van Cassatie, en enkel over de toepassing van het recht"],
            ])),
            ("p", "Dat <strong>beroep in twee instanties</strong> bestaat omdat een rechter zich kan "
                  "vergissen. Een tweede volledige behandeling vangt een fout op, en dat is een "
                  "waarborg voor de rechtzoekende, niet een vertragingstruc."),
            ("weetje", "Je moet beroep aantekenen binnen een <strong>termijn</strong>. Laat je die "
                       "voorbijgaan, dan wordt het vonnis definitief, ook als het fout was."),
        ]),
    ],
    onthoud=[
        "Materiële bevoegdheid: waarover gaat het. Territoriale bevoegdheid: waar is het gebeurd.",
        "Vredegerecht: kleinere geschillen tot 5.000 euro, huur, buren. Politierechtbank: verkeer.",
        "Eerste aanleg heeft vijf afdelingen: burgerlijk, correctioneel, familie, jeugd, strafuitvoering.",
        "Arbeidsrechtbank voor werk en sociale zekerheid, ondernemingsrechtbank voor ondernemingen.",
        "Assisen heeft een volksjury van twaalf burgers; alleen daar.",
        "Cassatie kijkt enkel naar het recht, niet naar de feiten, en verbreekt; beroep behandelt opnieuw.",
        "Een rechtbank spreekt een vonnis uit, een hof een arrest.",
    ],
)

# ───────────────────────── 19. Burgerlijk recht en strafrecht
BUNDELS["burgerlijk-recht-en-strafrecht-het-verloop-van-een-procedure-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Burgerlijk recht en strafrecht: het verloop van een procedure",
    onder="Het verschil tussen de twee, en wat er stap na stap gebeurt in een burgerlijke zaak en in een strafzaak.",
    secties=[
        dict(kop="Twee takken, twee logica's", blokken=[
            ("p", tabel(["", "Burgerlijk recht", "Strafrecht"], [
                ["gaat over", "een geschil tussen twee partijen", "een misdrijf tegen de samenleving"],
                ["wie start", "de benadeelde partij zelf, de eiser", "het openbaar ministerie, in naam van de samenleving"],
                ["tegen wie", "de verweerder", "de beklaagde of de verdachte"],
                ["wat de rechter beslist", "wie recht heeft op wat: een schadevergoeding, een regeling",
                 "schuldig of niet, en welke straf"],
                ["voorbeeld", "een huurgeschil, een scheiding, een onbetaalde factuur",
                 "diefstal, geweld, rijden onder invloed"],
            ])),
            ("kader", "<strong>Dezelfde feiten kunnen in beide takken terechtkomen.</strong> Wie bij "
                      "een vechtpartij iemand verwondt, kan strafrechtelijk gestraft worden én "
                      "burgerlijk de schade moeten vergoeden. Daarom kan een slachtoffer zich in de "
                      "strafzaak <strong>burgerlijke partij</strong> stellen: dan behandelt de "
                      "strafrechter ook de schadevergoeding en hoeft het slachtoffer geen tweede "
                      "procedure te beginnen."),
        ]),
        dict(kop="Een burgerlijke procedure, stap na stap", blokken=[
            ("p", tabel(["Stap", "Wat gebeurt er"], [
                ["1. de inleiding",
                 "de eiser brengt de zaak voor de rechtbank, meestal met een dagvaarding door een "
                 "gerechtsdeurwaarder, soms met een eenvoudiger verzoekschrift"],
                ["2. de uitwisseling van stukken",
                 "elke partij legt haar argumenten en bewijzen schriftelijk neer, in conclusies; de "
                 "andere kan daarop antwoorden, en dat is hoor en wederhoor"],
                ["3. de zitting en de pleidooien",
                 "de advocaten komen hun standpunt mondeling verdedigen voor de rechter"],
                ["4. het vonnis", "de rechter beslist, en motiveert waarom"],
                ["5. de uitvoering",
                 "wie in het ongelijk gesteld is, moet het vonnis uitvoeren; gebeurt dat niet, dan kan "
                 "een gerechtsdeurwaarder het afdwingen"],
            ])),
            ("p", "Tussen stap 1 en stap 4 kan de rechter nog altijd "
                  "<strong>bemiddeling</strong> voorstellen. In de familie- en jeugdrechtbank gebeurt "
                  "dat vaak: een akkoord dat de partijen zelf maken, houdt beter stand dan een vonnis "
                  "dat hen wordt opgelegd, en ze moeten daarna nog met elkaar verder."),
            ("weetje", "Een procedure stopt ook wanneer de partijen tussentijds een "
                       "<strong>minnelijke schikking</strong> maken. Dan is er geen vonnis nodig."),
        ]),
        dict(kop="Van feit tot proces: het strafrecht", blokken=[
            ("p", "Een <strong>misdrijf</strong> is een gedraging die de wet strafbaar stelt. Zonder "
                  "wet die iets verbiedt, is er geen misdrijf: dat is het legaliteitsbeginsel."),
            ("p", tabel(["Stap", "Wat gebeurt er", "Wie"], [
                ["1. de vaststelling",
                 "de politie stelt het feit vast en maakt een proces-verbaal, een officieel verslag "
                 "dat naar het parket gaat",
                 "de politie"],
                ["2. het vooronderzoek",
                 "er wordt uitgezocht wat er gebeurd is en wie het deed",
                 "het openbaar ministerie, en bij ernstige zaken de onderzoeksrechter"],
                ["3. de beslissing van het parket",
                 "seponeren, een minnelijke schikking voorstellen, of vervolgen",
                 "het openbaar ministerie"],
                ["4. de regeling van de procedure",
                 "de raadkamer beslist of de zaak naar de rechtbank gaat",
                 "de raadkamer"],
                ["5. het onderzoek ter terechtzitting",
                 "het eigenlijke proces: de zaak wordt openbaar behandeld, met getuigen en pleidooien",
                 "de strafrechter"],
                ["6. het vonnis", "schuldig of niet, en de straf", "de strafrechter"],
            ])),
            ("p", "Het vooronderzoek bestaat in <strong>twee vormen</strong>."),
            ("p", tabel(["", "Het opsporingsonderzoek", "Het gerechtelijk onderzoek"], [
                ["wie leidt", "het openbaar ministerie", "de onderzoeksrechter"],
                ["wanneer", "de gewone gang van zaken", "bij ernstige zaken, of wanneer er zware "
                                                        "onderzoeksdaden nodig zijn"],
                ["waarom zo", "snel en soepel",
                 "een onafhankelijke rechter moet beslissen over maatregelen die diep in iemands "
                 "rechten snijden, zoals een huiszoeking of een aanhouding"],
            ])),
            ("p", "Het parket heeft na het vooronderzoek <strong>drie wegen</strong>: "
                  "<strong>seponeren</strong> (de zaak zonder gevolg laten, bijvoorbeeld bij te weinig "
                  "bewijs of een te klein feit), een <strong>minnelijke schikking</strong> voorstellen, "
                  "of <strong>vervolgen</strong>."),
            ("kader", "<strong>Seponeren is geen vrijspraak.</strong> Een vrijspraak komt van een "
                      "rechter na een proces; seponeren is een beslissing van het parket om geen proces "
                      "te starten."),
            ("p", "Twee kamers horen bij dit traject. De <strong>raadkamer</strong> regelt de "
                  "procedure: ze beslist of er genoeg is om de zaak naar de rechtbank te sturen, en ze "
                  "beslist ook over de aanhouding. De <strong>kamer van inbeschuldigingstelling</strong> "
                  "is haar tegenhanger bij het hof van beroep en behandelt het beroep tegen die "
                  "beslissingen."),
            ("weetje", "Bij <strong>assisen</strong> loopt het anders: daar volgt de zaak de weg naar "
                       "het hof en beslist een jury van twaalf burgers over de schuld."),
        ]),
    ],
    onthoud=[
        "Burgerlijk recht: een geschil tussen partijen, gestart door de eiser. Strafrecht: een misdrijf, vervolgd door het openbaar ministerie.",
        "Een slachtoffer kan zich burgerlijke partij stellen, en krijgt dan ook de schadevergoeding in de strafzaak.",
        "Burgerlijke procedure: inleiding, stukken, pleidooien, vonnis, uitvoering.",
        "Strafzaak: vaststelling met proces-verbaal, vooronderzoek, beslissing van het parket, raadkamer, proces, vonnis.",
        "Opsporingsonderzoek leidt het parket; een gerechtelijk onderzoek leidt de onderzoeksrechter, bij zware zaken.",
        "Drie wegen voor het parket: seponeren, minnelijke schikking, vervolgen. Seponeren is geen vrijspraak.",
    ],
)

# ───────────────────────── 20. Juridische termen en actoren
BUNDELS["juridische-termen-en-actoren-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Juridische termen en actoren",
    onder="Wie wie is in een rechtszaal, en wat de woorden betekenen die je in een dossier tegenkomt.",
    secties=[
        dict(kop="Wie staat er tegenover wie", blokken=[
            ("p", "De namen van de partijen hangen af van de <strong>soort zaak</strong>. Dezelfde "
                  "mens heet in een burgerlijke zaak anders dan in een strafzaak."),
            ("p", tabel(["In een burgerlijke zaak", "Wie"], [
                ["de eiser", "wie de zaak begint en iets vraagt"],
                ["de verweerder", "wie zich tegen die eis verdedigt"],
            ])),
            ("p", tabel(["In een strafzaak", "Wie"], [
                ["de verdachte", "wie tijdens het vooronderzoek in het vizier staat"],
                ["de beklaagde", "wie voor de strafrechter terechtstaat"],
                ["het slachtoffer", "wie schade leed door het misdrijf"],
                ["de burgerlijke partij",
                 "het slachtoffer dat in de strafzaak zelf een schadevergoeding vraagt"],
            ])),
            ("kader", "<strong>Een verdachte is geen dader.</strong> Dat is het vermoeden van onschuld. "
                      "En wie voor assisen staat, heet geen beklaagde maar "
                      "<strong>beschuldigde</strong>."),
        ]),
        dict(kop="De mensen van justitie", blokken=[
            ("p", tabel(["Wie", "Wat die doet"], [
                ["de rechter", "oordeelt onafhankelijk en onpartijdig, en motiveert zijn uitspraak"],
                ["het openbaar ministerie, ook het parket",
                 "vervolgt misdrijven in naam van de samenleving; de procureur staat aan het hoofd"],
                ["de onderzoeksrechter",
                 "leidt een gerechtelijk onderzoek bij ernstige zaken; hij is rechter, geen vervolger, "
                 "en zoekt zowel wat belast als wat ontlast"],
                ["de advocaat",
                 "staat een partij bij, geeft raad en pleit; hij is gebonden aan zijn beroepsgeheim en "
                 "aan de deontologie van de balie"],
                ["de griffier",
                 "houdt het dossier bij, schrijft op wat er op de zitting gebeurt en bewaart de "
                 "stukken; zonder griffier is er geen geldige zitting"],
                ["de gerechtsdeurwaarder",
                 "betekent officiële stukken zoals een dagvaarding, en voert een vonnis uit als iemand "
                 "dat niet vrijwillig doet"],
                ["de juryleden",
                 "twaalf burgers, bij lot aangewezen, die bij assisen over de schuld beslissen"],
            ])),
            ("weetje", "De <strong>onderzoeksrechter</strong> is de lastigste om te plaatsen. Hij werkt "
                       "niet voor het parket en niet voor de verdediging. Hij zoekt de waarheid, en dus "
                       "ook het bewijs dat iemand onschuldig is."),
        ]),
        dict(kop="De woorden in een dossier", blokken=[
            ("p", tabel(["Woord", "Wat het betekent"], [
                ["een dagvaarding", "de officiële uitnodiging om voor de rechtbank te verschijnen"],
                ["een proces-verbaal", "het officiële verslag van de politie over een vaststelling"],
                ["het strafdossier", "alle stukken die in een strafzaak verzameld zijn"],
                ["een vonnis", "de uitspraak van een rechtbank"],
                ["een arrest", "de uitspraak van een hof"],
                ["beroep", "een zaak opnieuw laten behandelen door een hogere rechter"],
                ["cassatie", "een uitspraak laten nakijken op de toepassing van het recht"],
                ["seponeren", "de zaak zonder gevolg laten, door het parket"],
                ["een minnelijke schikking", "een geschil of een zaak regelen met een afspraak, zonder vonnis"],
                ["het vooronderzoek", "alles wat gebeurt voor de zaak voor de rechter komt; het dekt zowel het opsporingsonderzoek als het gerechtelijk onderzoek"],
                ["het onderzoek ter terechtzitting", "het eigenlijke proces, openbaar, met getuigen en pleidooien"],
                ["de raadkamer", "beslist of een strafzaak naar de rechtbank gaat, en over de aanhouding"],
                ["de kamer van inbeschuldigingstelling", "de tegenhanger van de raadkamer bij het hof van beroep; ze behandelt het beroep tegen haar beslissingen en verwijst een zaak naar assisen"],
            ])),
            ("kader", "<strong>Waarom deze woorden leren?</strong> Omdat een brief van een advocaat of "
                      "een deurwaarder in deze taal geschreven is. Wie ze niet begrijpt, weet niet wat "
                      "er van hem gevraagd wordt en mist een termijn. De moeilijke taal van justitie is "
                      "een van de redenen voor de kloof met de burger, en net daarom is het nuttig om "
                      "ze te kennen."),
        ]),
    ],
    onthoud=[
        "Burgerlijk: eiser tegen verweerder. Straf: verdachte in het onderzoek, beklaagde voor de rechter.",
        "Een slachtoffer dat zelf vergoeding vraagt in de strafzaak, is de burgerlijke partij.",
        "Het openbaar ministerie vervolgt in naam van de samenleving; de onderzoeksrechter zoekt onafhankelijk de waarheid.",
        "De griffier houdt het dossier bij, de gerechtsdeurwaarder betekent stukken en voert vonnissen uit.",
        "Een rechtbank spreekt een vonnis uit, een hof een arrest.",
        "Raadkamer: gaat de zaak naar de rechtbank. Kamer van inbeschuldigingstelling: het beroep daartegen.",
    ],
)

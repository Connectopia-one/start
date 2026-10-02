# -*- coding: utf-8 -*-
"""De leerbundels voor natuurwetenschappen op 🌍 Beyond dubbele finaliteit.

Gebaseerd op de vakfiche natuurwetenschappen van de 3de graad dubbele
finaliteit, geldig vanaf 1 januari 2027. Die fiche noemt bovenaan zelf twee
toepassingen: basisvorming dubbele finaliteit en commerciële organisatie. Het
is de enige fiche natuurwetenschappen voor die graad en finaliteit.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De veertien thema's volgen de weging van het examen zelf: zes over biologie,
vier over chemie, drie over fysica en één over veilig werken en onderzoeken.
Biologie weegt er 45 %, chemie en fysica samen 45 %, en onderzoek en STEM 10 %.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py
../../beyond-dubbele-finaliteit/natuurwetenschappen.json` doet daar het
voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-beyond-dubbele-finaliteit". Natuurwetenschappen bestaat ook op
✨ Spark, op 🚀 Boost en op 🌍 Beyond doorstroom, en daar klinken sommige
thematitels bijna gelijk.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Natuurwetenschappen"
DF = "🌍 Beyond dubbele finaliteit — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 1. Bevruchting en de ontwikkeling van embryo en foetus
BUNDELS["bevruchting-en-de-ontwikkeling-van-embryo-en-foetus-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Bevruchting en de ontwikkeling van embryo en foetus",
    onder="Van de hormonen die de cyclus sturen tot de bevalling, en wat een zwangere vrouw het best vermijdt.",
    secties=[
        dict(kop="De hormonen van de cyclus", blokken=[
            ("p", "De <strong>hypofyse</strong> in je hoofd maakt zelf <strong>twee</strong> hormonen die de "
                  "cyclus sturen: het <strong>follikelstimulerend hormoon FSH</strong> en het "
                  "<strong>luteïniserend hormoon LH</strong>. FSH is het hormoon dat "
                  "<strong>een follikel in de eierstok doet rijpen</strong>."),
            ("p", "Halfweg de cyclus komt er een <strong>plotse, sterke stijging van LH</strong>. Die heet de "
                  "<strong>LH-piek</strong>, en zij <strong>lokt de eisprong uit</strong>. De eisprong gebeurt "
                  "<strong>ongeveer veertien dagen vóór de volgende menstruatie</strong>, en dat is "
                  "betrouwbaarder om op te rekenen dan veertien dagen ná de vorige."),
            ("p", "<strong>Nadat de eicel uit de follikel vertrokken is, wordt die follikel het geel "
                  "lichaam</strong>. Het geel lichaam maakt vooral <strong>progesteron</strong>, en dat houdt "
                  "het baarmoederslijmvlies dik. <strong>Is er geen bevruchting, dan valt het geel lichaam weg "
                  "en begint de menstruatie</strong>."),
            ("kader", "Een eicel blijft na de eisprong <strong>ongeveer een halve tot een hele dag</strong> "
                      "bevruchtbaar. Zaadcellen houden het in het lichaam van de vrouw veel langer uit, en "
                      "daarom liggen de vruchtbare dagen vóór de eisprong, niet erna."),
        ]),
        dict(kop="De eicel en de zaadcel", blokken=[
            ("p", "Bij de man maakt de <strong>teelbal</strong> of testikel, de klier die daarvoor dient, het geslachtshormoon "
                  "<strong>testosteron</strong>. In diezelfde teelballen worden ook de zaadcellen gemaakt."),
            ("p", "Een zaadcel heeft <strong>drie</strong> onderdelen die je moet kennen: een "
                  "<strong>flagel of staart</strong> om mee te zwemmen, een <strong>kop met een enzym</strong>, "
                  "en <strong>mitochondriën in het middenstuk</strong>. Dat "
                  "<strong>middenstuk of die hals levert de energie om te zwemmen</strong>, want daar zitten "
                  "die mitochondriën. Het <strong>enzym in de kop dient om de vliezen rond de eicel open te "
                  "maken</strong>."),
            ("p", "<strong>Een zaadcel is niet groter dan een eicel, maar veel kleiner</strong>: de eicel is de "
                  "grootste cel van het menselijk lichaam. De eicel heeft dan ook twee dingen die de zaadcel "
                  "niet heeft: <strong>reservevoedsel in het cytoplasma</strong> en "
                  "<strong>een laag eiwit rondom de cel</strong>."),
            ("fig", tabel(["", "Eicel", "Zaadcel"], [
                ["Grootte", "de grootste cel van het lichaam", "heel klein"],
                ["Beweging", "wordt meegevoerd", "zwemt met een flagel"],
                ["Energie", "reservevoedsel in het cytoplasma", "mitochondriën in het middenstuk"],
                ["Buitenkant", "een laag eiwit rondom", "een kop met een enzym"],
            ]), "De twee geslachtscellen naast elkaar."),
        ]),
        dict(kop="Bevruchting en innesteling", blokken=[
            ("p", "De <strong>zaadcellen leggen hun weg naar de eicel af door de baarmoeder heen</strong>, en "
                  "daarna verder in de eileider. <strong>De bevruchting gebeurt in het vrouwelijk voortplantingsstelsel meestal in de "
                  "eileider</strong>, niet in de baarmoeder."),
            ("p", "<strong>Meteen nadat één zaadcel binnen is, sluit het bevruchtingsmembraan de eicel "
                  "af</strong>. Zo kan er geen tweede zaadcel meer bij. Als de kernen van de eicel en de "
                  "zaadcel versmelten, ontstaat de <strong>zygote</strong> of zygoot: de eerste cel van een nieuw mens."),
            ("p", "De zygote deelt zich onderweg en wordt een kiemblaas. Het "
                  "<strong>vastzetten van die kiemblaas in het baarmoederslijmvlies</strong> heet de "
                  "<strong>innesteling</strong>. <strong>Dat gebeurt niet terwijl de bevruchte eicel nog in de "
                  "eileider zit</strong>, maar enkele dagen later, in de baarmoeder. Nestelt ze zich wél in de "
                  "eileider in, dan spreekt men van een buitenbaarmoederlijke zwangerschap."),
        ]),
        dict(kop="Embryo, foetus en placenta", blokken=[
            ("p", "De <strong>embryonale fase</strong> duurt <strong>de eerste acht weken</strong>. Wat die "
                  "fase kenmerkt, is dat <strong>de organen worden aangelegd</strong>. Dat aanleggen van de "
                  "organen in de eerste weken heet de <strong>organogenese</strong>. Daarna spreekt men van "
                  "een foetus, en groeit alles vooral verder. "
                  "<strong>De vrucht is pas levensvatbaar vanaf ongeveer vierentwintig weken.</strong>"),
            ("p", "De <strong>placenta bestaat uit een deel van de moeder en een deel van de vrucht</strong>. "
                  "<strong>Het bloed van de moeder en het bloed van de vrucht lopen er niet door elkaar</strong>: "
                  "ze worden door een dun vlies gescheiden, en de stoffen gaan daar doorheen."),
            ("p", "Van de moeder naar de vrucht gaan er <strong>twee</strong> dingen die je moet kennen: "
                  "<strong>zuurstof uit het bloed van de moeder</strong> en "
                  "<strong>voedingsstoffen zoals glucose</strong>. In de andere richting gaan koolstofdioxide "
                  "en afvalstoffen."),
            ("p", "In de <strong>navelstreng</strong> zitten <strong>twee slagaders en één ader</strong>. De "
                  "vrucht drijft in de vloeistof die het <strong>vruchtwater</strong> heet, en die haar "
                  "<strong>beschermt tegen stoten</strong> en op temperatuur houdt."),
        ]),
        dict(kop="De bevalling", blokken=[
            ("p", "De bevalling verloopt in drie fasen. <strong>De ontsluiting komt eerst</strong>: de "
                  "baarmoedermond gaat open. Daarna volgt de uitdrijving, waarbij de baby geboren wordt. "
                  "De laatste fase, <strong>waarin de placenta naar buiten komt, heet de "
                  "nageboorte</strong>."),
            ("p", "<strong>Weeën zijn samentrekkingen van de spierwand van de baarmoeder.</strong> Ze worden "
                  "sterker en volgen elkaar sneller op naarmate de bevalling vordert."),
        ]),
        dict(kop="Wat de vrucht kan schaden", blokken=[
            ("p", "<strong>Teratogene stoffen</strong> zijn <strong>stoffen die de ontwikkeling van de vrucht "
                  "verstoren</strong>. <strong>Alcohol wordt afgeraden tijdens de zwangerschap omdat alcohol "
                  "door de placenta naar de vrucht gaat.</strong> Hetzelfde geldt voor roken, en "
                  "<strong>passief roken is ook een probleem, want de schadelijke stoffen komen ook zo in het "
                  "bloed van de moeder</strong>."),
            ("p", "<strong>Foliumzuur</strong>, ook vitamine B11 genoemd, wordt <strong>vóór en in het begin "
                  "van de zwangerschap aangeraden om afwijkingen aan de ruggengraat te voorkomen</strong>."),
            ("p", "Drie ziekteverwekkers zijn gevaarlijk voor een ongeboren kind: "
                  "<strong>het rubellavirus of rodehond</strong>, <strong>de toxoplasmose-parasiet</strong> en "
                  "<strong>het zikavirus</strong>. Daarom worden "
                  "<strong>rauwe melkproducten en onvoldoende verhit vlees tijdens de zwangerschap "
                  "afgeraden</strong>: daar kan de toxoplasmose-parasiet in zitten."),
            ("p", "<strong>Hoe ouder de moeder, hoe gróter de kans op een chromosoomafwijking bij de "
                  "vrucht</strong>, niet kleiner. Van alle aanpassingen in haar levensstijl helpt "
                  "<strong>stoppen met roken en met alcohol</strong> een zwangere vrouw het meest."),
        ]),
    ],
    onthoud=[
        "FSH laat een follikel rijpen, de LH-piek lokt de eisprong uit.",
        "De eisprong is ongeveer veertien dagen vóór de volgende menstruatie.",
        "De follikel wordt het geel lichaam en maakt progesteron.",
        "Bevruchting gebeurt in de eileider, innesteling in de baarmoeder.",
        "De embryonale fase duurt acht weken; dan worden de organen aangelegd.",
        "In de placenta raken het bloed van moeder en vrucht elkaar niet.",
        "De navelstreng heeft twee slagaders en één ader.",
        "Alcohol, roken, rodehond, toxoplasmose en zika schaden de vrucht.",
    ],
)

# ───────────────────────── 2. Vruchtbaarheid, anticonceptie en kinderwens
BUNDELS["vruchtbaarheid-anticonceptie-en-kinderwens-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Vruchtbaarheid, anticonceptie en kinderwens",
    onder="De methoden om zwangerschap te voorkomen, en wat er mogelijk is als een zwangerschap uitblijft.",
    secties=[
        dict(kop="Natuurlijke methoden", blokken=[
            ("p", "<strong>Drie</strong> methoden zijn natuurlijk, dus <strong>zonder middel of "
                  "ingreep</strong>: de <strong>kalendermethode</strong>, de "
                  "<strong>temperatuurmethode</strong> en de <strong>ovulatiemethode</strong>."),
            ("p", "De <strong>kalendermethode berust op het schatten van de vruchtbare dagen uit vorige "
                  "cycli</strong>. Bij de <strong>temperatuurmethode merk je dat de temperatuur licht stijgt "
                  "na de eisprong</strong>. De methode waarbij je <strong>het slijm van de baarmoederhals "
                  "bekijkt om de eisprong te herkennen</strong>, heet de <strong>ovulatiemethode</strong> of "
                  "billingsmethode."),
            ("kader", "<strong>Coïtus interruptus is géén betrouwbare methode om zwangerschap te "
                      "voorkomen.</strong> Er komen al zaadcellen vrij voor de zaadlozing, en het hangt "
                      "volledig af van het juiste moment."),
        ]),
        dict(kop="Hormonale methoden", blokken=[
            ("p", "<strong>Drie</strong> middelen werken met hormonen: de <strong>combinatiepil</strong>, het "
                  "<strong>hormoonstaafje</strong> en de <strong>vaginale ring</strong>. De "
                  "<strong>combinatiepil voorkomt een zwangerschap doordat ze de eisprong tegenhoudt</strong>."),
            ("p", "<strong>Het verschil tussen de minipil en de combinatiepil is dat de minipil maar één soort "
                  "hormoon bevat.</strong> Een <strong>hormoonstaafje in de arm werkt enkele jaren</strong>, en "
                  "een <strong>prikpil werkt ongeveer drie maanden</strong>."),
            ("p", "De <strong>morning-afterpil</strong> is de pil die je <strong>ná onbeschermd vrijen inneemt "
                  "om een zwangerschap nog te voorkomen</strong>. Ze heet ook noodanticonceptie, en ze werkt "
                  "beter hoe sneller je ze neemt."),
            ("p", "Niet alle anticonceptiemiddelen werken met hormonen: er bestaat ook een spiraaltje zónder. Daarin zit het metaal <strong>koper</strong>, en dat "
                  "<strong>maakt zaadcellen onbeweeglijk</strong>."),
        ]),
        dict(kop="Barrièremethoden en sterilisatie", blokken=[
            ("p", "<strong>Drie</strong> methoden zijn barrièremethoden, die <strong>de zaadcellen mechanisch "
                  "tegenhouden</strong>: het <strong>mannencondoom</strong>, het "
                  "<strong>vrouwencondoom</strong> en het <strong>pessarium of diafragma</strong>."),
            ("p", "Van al die methoden beschermen er <strong>twee ook tegen soa's</strong>: het "
                  "<strong>mannencondoom</strong> en het <strong>vrouwencondoom</strong>. "
                  "<strong>Wie de pil neemt, heeft daarnaast dus wél bescherming tegen soa's nodig</strong>, "
                  "want de pil houdt geen enkele infectie tegen."),
            ("p", "Een <strong>zaaddodend middel gebruik je het best samen met een barrièremethode</strong>; "
                  "alleen is het te onzeker."),
            ("p", "<strong>Sterilisatie is de betrouwbaarste methode.</strong> "
                  "<strong>Bij een sterilisatie bij de man worden de zaadleiders onderbroken</strong>, bij de "
                  "vrouw de eileiders. Je gaat er het best van uit dat het blijvend is."),
            ("p", "<strong>De betrouwbaarheid is in de praktijk vaak lager dan op papier, omdat een methode "
                  "verkeerd of onregelmatig gebruikt wordt.</strong> En "
                  "<strong>anticonceptie is een keuze die bij de persoon zelf past, omdat gezondheid, leeftijd "
                  "en levensritme per persoon verschillen</strong>."),
        ]),
        dict(kop="Als een zwangerschap uitblijft", blokken=[
            ("p", "Men spreekt van <strong>onvruchtbaarheid als er na een jaar onbeschermd vrijen geen "
                  "zwangerschap is</strong>. <strong>Onvruchtbaarheid ligt ongeveer even vaak bij de man als "
                  "bij de vrouw</strong>, en soms bij beiden samen of bij geen van de twee duidelijk."),
            ("p", "<strong>Bij de man onderzoekt men eerst het sperma, op aantal en beweeglijkheid.</strong> "
                  "Dat is een eenvoudig onderzoek en het sluit meteen veel uit."),
            ("p", "De <strong>menopauze</strong> is het moment <strong>waarop de eierstokken stoppen met werken "
                  "en de menstruatie wegblijft</strong>. Ze heet ook de overgang."),
        ]),
        dict(kop="Behandelingen bij een kinderwens", blokken=[
            ("p", "<strong>Hormonale stimulatie</strong> heeft als doel <strong>de eierstok aan te zetten om "
                  "eicellen te laten rijpen</strong>. Omdat er dan meerdere eicellen rijpen, "
                  "<strong>verhoogt hormonale stimulatie de kans op een meerling</strong>."),
            ("p", "Bij <strong>kunstmatige inseminatie of KI wordt sperma rechtstreeks in de baarmoeder "
                  "gebracht</strong>. De afkorting <strong>IVF</strong> staat voor <strong>in vitro fertilisatie</strong> of in-vitrofertilisatie: "
                  "de bevruchting gebeurt buiten het lichaam, in het labo. "
                  "<strong>Het verschil met ICSI is dat bij ICSI één zaadcel in de eicel geprikt wordt</strong>, "
                  "terwijl bij gewone IVF de zaadcellen zelf de eicel moeten binnendringen."),
            ("p", "<strong>Bij IVF groeit de vrucht niet de hele zwangerschap in het labo.</strong> Na enkele "
                  "dagen wordt het embryo in de baarmoeder geplaatst, en daar verloopt de zwangerschap verder "
                  "zoals altijd. <strong>Men haalt vaak meerdere eicellen, omdat niet elke eicel bevrucht "
                  "raakt of goed doorgroeit.</strong>"),
            ("p", "<strong>Eicellen of sperma invriezen</strong> heeft als doel "
                  "<strong>de vruchtbaarheid te bewaren voor later</strong>, bijvoorbeeld voor een behandeling "
                  "die ze kan aantasten."),
        ]),
        dict(kop="Wat de vruchtbaarheid aantast", blokken=[
            ("p", "<strong>Drie</strong> gewoonten verlagen de vruchtbaarheid bij <strong>man én "
                  "vrouw</strong>: <strong>roken</strong>, <strong>veel alcohol drinken</strong> en "
                  "<strong>drugsgebruik</strong>. <strong>Wie met een kinderwens rookt, stopt dus het best "
                  "vóór de zwangerschap en niet pas als ze er is</strong>: zaadcellen en eicellen rijpen "
                  "maanden vooraf."),
            ("p", "<strong>De leeftijd van de vrouw verlaagt de kans op zwangerschap doordat de voorraad "
                  "eicellen daalt en hun kwaliteit afneemt.</strong> Ook het gewicht speelt mee, en "
                  "<strong>niet alleen overgewicht kan de cyclus verstoren: ondergewicht evengoed</strong>."),
            ("p", "<strong>Warmte is slecht voor de aanmaak van zaadcellen, omdat zaadcellen het best rijpen "
                  "net onder de lichaamstemperatuur.</strong> Daarom hangen de teelballen buiten het lichaam."),
            ("p", "<strong>Chemotherapie</strong> en bestraling of radiotherapie zijn behandelingen tegen kanker die "
                  "<strong>de vruchtbaarheid blijvend kunnen aantasten</strong>. Daarom wordt invriezen soms "
                  "vooraf voorgesteld."),
            ("p", "<strong>Twee</strong> invloeden van buitenaf kunnen de vruchtbaarheid aantasten: "
                  "<strong>zware metalen zoals lood en cadmium</strong> en "
                  "<strong>langdurige, zware stress</strong>. En "
                  "<strong>een soa die niet behandeld wordt, kan tot onvruchtbaarheid leiden</strong>, doordat "
                  "de eileiders of de zaadleiders beschadigd raken."),
        ]),
    ],
    onthoud=[
        "Kalender-, temperatuur- en ovulatiemethode zijn de natuurlijke methoden.",
        "De combinatiepil houdt de eisprong tegen; een koperspiraal werkt zonder hormonen.",
        "Alleen het mannen- en het vrouwencondoom beschermen ook tegen soa's.",
        "Sterilisatie is het betrouwbaarst, coïtus interruptus het onzekerst.",
        "Onvruchtbaarheid: na een jaar onbeschermd vrijen geen zwangerschap.",
        "Bij IVF gebeurt de bevruchting in het labo, de zwangerschap in de baarmoeder.",
        "Bij ICSI wordt één zaadcel in de eicel geprikt.",
        "Roken, alcohol, drugs, leeftijd, gewicht, warmte en stress verlagen de vruchtbaarheid.",
    ],
)

# ───────────────────────── 3. Van DNA naar eiwit: genexpressie
BUNDELS["van-dna-naar-eiwit-genexpressie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Van DNA naar eiwit: genexpressie",
    onder="Hoe DNA gebouwd is, hoe een gen een eiwit oplevert, en waarom je fenotype meer is dan je genen.",
    secties=[
        dict(kop="De bouw van DNA", blokken=[
            ("p", "Het DNA-molecule heeft de vorm van een <strong>dubbele helix</strong> of dubbelhelix: "
                  "twee strengen die om elkaar draaien. De <strong>twee lange zijkanten van die helix bestaan "
                  "uit suikers en fosfaatgroepen</strong>; de sporten van de ladder ertussen zijn de basen."),
            ("p", "In DNA horen <strong>vier</strong> basen: <strong>adenine</strong>, "
                  "<strong>cytosine</strong>, <strong>guanine</strong> en <strong>thymine</strong>. Ze staan "
                  "altijd per twee tegenover elkaar: <strong>tegenover adenine staat in DNA altijd "
                  "thymine</strong>, en <strong>tegenover cytosine staat altijd guanine</strong>."),
            ("fig", tabel(["", "DNA", "RNA"], [
                ["Strengen", "twee, in een dubbele helix", "maar één streng"],
                ["Suiker", "desoxyribose", "ribose"],
                ["Basen", "A, C, G en T", "A, C, G en U"],
            ]), "DNA en RNA verschillen in drie dingen."),
            ("p", "<strong>RNA verschilt in drie dingen van DNA</strong>: "
                  "<strong>RNA heeft maar één streng</strong>, "
                  "<strong>RNA bevat uracil in plaats van thymine</strong> en "
                  "<strong>RNA bevat ribose in plaats van desoxyribose</strong>. De suiker in RNA is dus "
                  "<strong>ribose</strong>, en de base die er <strong>de plaats van thymine</strong> inneemt is "
                  "<strong>uracil</strong>. <strong>RNA bestaat dus niet, zoals DNA, uit twee strengen die om "
                  "elkaar draaien.</strong>"),
        ]),
        dict(kop="Gen, allel en chromosoom", blokken=[
            ("p", "Een <strong>gen</strong> is <strong>een stuk DNA met de code voor één eigenschap</strong>. "
                  "<strong>Elk gen ligt bij elke mens op dezelfde plaats van hetzelfde chromosoom.</strong> "
                  "Daarom kan men van een gen zeggen waar het zit."),
            ("p", "De verschillende versies van hetzelfde gen heten <strong>allelen</strong>, vroeger ook erffactoren. "
                  "<strong>Het verschil tussen een gen en een allel is dus dat een allel één van de mogelijke "
                  "versies van dat gen is.</strong> <strong>Een kind lijkt op allebei zijn ouders omdat het van "
                  "elke ouder één allel per gen krijgt.</strong>"),
            ("p", "<strong>Een lichaamscel bevat niet één gen tegelijk</strong>, maar het hele erfelijk "
                  "materiaal: tienduizenden genen, in elke cel dezelfde."),
        ]),
        dict(kop="Genotype en fenotype", blokken=[
            ("p", "Het <strong>genotype</strong> van een organisme is <strong>het geheel van zijn erfelijk "
                  "materiaal</strong>. Het <strong>fenotype</strong> is <strong>alles wat je aan een organisme "
                  "kan waarnemen of meten</strong>. <strong>De kleur van je ogen</strong> en "
                  "<strong>je lengte op volwassen leeftijd</strong> horen dus bij het fenotype."),
            ("p", "<strong>Naast je genen bepaalt ook de omgeving waarin je opgroeit je fenotype mee.</strong> "
                  "Daarom hebben <strong>twee mensen met hetzelfde genotype voor een kenmerk niet altijd exact "
                  "hetzelfde fenotype</strong>: voeding, beweging en ziekte spelen mee. "
                  "<strong>Omgevingsfactoren kunnen zelfs mee bepalen hoe sterk een gen tot uiting komt.</strong>"),
        ]),
        dict(kop="Van gen naar eiwit", blokken=[
            ("p", "<strong>Genexpressie</strong> betekent dat <strong>de informatie in een gen wordt omgezet in "
                  "een eiwit</strong>. Dat gebeurt in twee stappen, op twee plaatsen in de cel."),
            ("p", "Eerst wordt <strong>in de celkern het mRNA van het DNA afgelezen</strong>. Het "
                  "<strong>mRNA</strong>, het messenger-RNA of boodschapper-RNA, is het molecule dat <strong>de code van het DNA "
                  "uit de kern naar buiten brengt</strong>. <strong>Het DNA zelf verlaat de celkern "
                  "niet</strong>: het blijft veilig binnen, en alleen de kopie reist."),
            ("p", "Tussen het aflezen van het gen en het klaar zijn van het eiwit zit dus één stap: "
                  "<strong>het mRNA reist naar een ribosoom</strong>. "
                  "<strong>Aan het ribosoom wordt het eiwit zelf in elkaar gezet.</strong> Het proces waarbij "
                  "<strong>het ribosoom aminozuren aan elkaar koppelt tot een eiwit</strong>, heet de "
                  "<strong>eiwitsynthese</strong> of translatie."),
            ("p", "De bouwstenen van een eiwit zijn <strong>aminozuren</strong>, en "
                  "<strong>een eiwit is opgebouwd uit aminozuren in een vaste volgorde</strong>. "
                  "<strong>Een gen zonder eiwit is meestal zonder gevolg, want het eiwit doet het werk in de "
                  "cel.</strong>"),
            ("kader", "<strong>Een gen dat in een cel aanwezig is, staat daar niet altijd aan.</strong> "
                      "Daarom <strong>ziet een spiercel er anders uit dan een huidcel terwijl ze hetzelfde DNA "
                      "hebben: in elke cel staan andere genen aan</strong>."),
        ]),
        dict(kop="Erfelijk of niet, en wat de mens eraan verandert", blokken=[
            ("p", "<strong>Twee</strong> van de genoemde eigenschappen zijn erfelijk: "
                  "<strong>je bloedgroep</strong> en <strong>je natuurlijke haarkleur</strong>. "
                  "<strong>Een litteken is geen erfelijke eigenschap, omdat het niets verandert aan het DNA in "
                  "je geslachtscellen.</strong> Alleen wat in de geslachtscellen zit, gaat door naar een "
                  "volgende generatie."),
            ("p", "Het <strong>bewust veranderen van het erfelijk materiaal van een organisme</strong> heet "
                  "<strong>genetische manipulatie</strong>, genetische modificatie of gentechnologie. "
                  "<strong>Recombinant DNA-technologie</strong> is de techniek waarbij "
                  "<strong>DNA van verschillende organismen wordt samengebracht</strong>. "
                  "<strong>Bacteriën die menselijke insuline aanmaken</strong> zijn daarvan het bekendste "
                  "voorbeeld."),
            ("p", "<strong>Veredeling</strong> is iets anders: <strong>doelgericht kruisen en de beste "
                  "nakomelingen uitkiezen</strong>. <strong>Veredeling en genetische modificatie zijn dus geen "
                  "twee namen voor hetzelfde</strong>: bij veredeling blijf je binnen wat de natuur zelf kan "
                  "kruisen, bij modificatie grijp je rechtstreeks in het DNA in."),
        ]),
    ],
    onthoud=[
        "DNA is een dubbele helix van suikers en fosfaatgroepen met A, C, G en T.",
        "A staat tegenover T, C tegenover G.",
        "RNA: één streng, ribose, en uracil in plaats van thymine.",
        "Een allel is één versie van een gen; je krijgt er één van elke ouder.",
        "Genotype is het erfelijk materiaal, fenotype is wat je ziet en meet.",
        "mRNA brengt de code uit de kern naar het ribosoom; het DNA blijft binnen.",
        "Aan het ribosoom worden aminozuren tot een eiwit gekoppeld.",
        "Veredeling is kruisen en kiezen; genetische modificatie grijpt in het DNA in.",
    ],
)

# ───────────────────────── 4. Overerving van kenmerken
BUNDELS["overerving-van-kenmerken-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Overerving van kenmerken",
    onder="Chromosomen en celdelingen, de wetten van Mendel, bloedgroepen en X-gebonden aandoeningen.",
    secties=[
        dict(kop="Chromosomen", blokken=[
            ("p", "Een <strong>chromosoom</strong> bestaat <strong>uit sterk opgerold DNA met "
                  "eiwitten</strong>. Het punt waar de <strong>twee chromatiden van een chromosoom aan elkaar "
                  "vastzitten</strong>, heet het <strong>centromeer</strong>."),
            ("p", "In een <strong>menselijke lichaamscel zitten 46 chromosomen</strong>, in "
                  "<strong>drieëntwintig</strong> paren. Zo'n cel is <strong>diploïd of 2n</strong>, en dat "
                  "betekent dat ze <strong>van elk chromosoom twee exemplaren heeft</strong>. Cellen met "
                  "<strong>maar één exemplaar van elk chromosoom</strong> heten "
                  "<strong>haploïd</strong>: in een <strong>menselijke eicel zitten dus 23 "
                  "chromosomen</strong>."),
            ("p", "<strong>Homologe chromosomen</strong> zijn <strong>twee chromosomen van hetzelfde "
                  "paar</strong>. De foto <strong>waarop alle chromosomen van een cel per paar geordend "
                  "staan</strong>, heet een <strong>karyogram</strong> of karyotype."),
            ("p", "Eén paar, de geslachtschromosomen, bepaalt het geslacht. Een <strong>man heeft een X en een Y</strong>, een vrouw twee "
                  "X-chromosomen. <strong>Het geslacht van een kind wordt dus bepaald door de zaadcel</strong>: "
                  "de eicel draagt altijd een X, de zaadcel een X of een Y."),
        ]),
        dict(kop="Mitose, meiose en mutaties", blokken=[
            ("p", "Het resultaat van een <strong>mitose of gewone celdeling</strong> is "
                  "<strong>twee cellen met hetzelfde erfelijk materiaal</strong>. Het resultaat van een "
                  "<strong>meiose of reductiedeling</strong> is <strong>vier haploïde cellen die onderling "
                  "verschillen</strong>."),
            ("p", "De meiose dient in ons lichaam voor <strong>twee</strong> dingen: "
                  "<strong>geslachtscellen maken</strong> en <strong>variatie tussen de nakomelingen "
                  "brengen</strong>. <strong>Ze komt in het menselijk lichaam alleen voor in de eierstokken en "
                  "de teelballen.</strong>"),
            ("p", "<strong>Het DNA moet verdubbelen vóór een cel deelt, anders krijgt niet elke dochtercel een "
                  "volledige set.</strong> Bij dat kopiëren kan het misgaan."),
            ("p", "Een <strong>mutatie</strong> is <strong>een blijvende verandering in de volgorde van de "
                  "basen in het DNA</strong>. <strong>Drie</strong> dingen kunnen er een veroorzaken: "
                  "<strong>uv-straling van de zon</strong>, <strong>bepaalde chemische stoffen</strong> en "
                  "<strong>een fout bij het kopiëren van DNA</strong>."),
            ("p", "Een mutatie is <strong>erfelijk als ze in een geslachtscel zit</strong>. "
                  "<strong>Een mutatie in een lichaamscel kan dus niet doorgegeven worden aan je "
                  "kinderen.</strong> En <strong>niet elke mutatie is schadelijk</strong>: de meeste doen "
                  "niets, en een enkele is zelfs nuttig. Juist daarop werkt de evolutie."),
        ]),
        dict(kop="Homozygoot, heterozygoot en de wetten van Mendel", blokken=[
            ("p", "Iemand is <strong>homozygoot</strong> voor een kenmerk als <strong>de twee allelen voor dat "
                  "kenmerk gelijk zijn</strong>. Iemand <strong>met twee verschillende allelen voor hetzelfde "
                  "kenmerk</strong> is <strong>heterozygoot</strong>, ook wel hybride."),
            ("p", "Een <strong>recessief allel komt alleen tot uiting in dubbele vorm</strong>. Een dominant "
                  "allel volstaat in enkelvoud. Daarom heet iemand "
                  "<strong>die een recessief allel voor een aandoening draagt zonder zelf ziek te zijn</strong> "
                  "een <strong>drager</strong>, of bij een vrouw een draagster."),
            ("p", "De <strong>uniformiteitswet van Mendel</strong> zegt: <strong>kruis je twee raszuivere "
                  "ouders, dan lijkt de F1 op elkaar</strong>. De <strong>splitsingswet</strong> zegt: "
                  "<strong>in de F2 duikt het verborgen kenmerk weer op</strong>. Bij dominant-recessieve "
                  "overerving <strong>splitsen de fenotypes zich in de F2 in de verhouding 3 op 1</strong>."),
            ("fig", tabel(["Kruising Aa × Aa", "AA", "Aa", "aA", "aa"], [
                ["Genotype", "25 %", "25 %", "25 %", "25 %"],
                ["Vertoont het kenmerk", "nee", "nee", "nee", "ja"],
            ]), "Twee heterozygote ouders: één kind op vier vertoont het recessieve kenmerk."),
            ("p", "<strong>Twee heterozygote ouders, Aa en Aa, krijgen statistisch gezien 25 % kinderen die het "
                  "recessieve kenmerk vertonen</strong>, en <strong>50 % die het recessieve allel dragen maar "
                  "het niet tonen</strong>. De overige 25 % heeft het allel helemaal niet."),
        ]),
        dict(kop="Intermediair, codominant en de bloedgroepen", blokken=[
            ("p", "Bij <strong>intermediaire overerving zit de heterozygoot tussen de twee ouders in</strong>: "
                  "een rode en een witte bloem geven een roze. Bij "
                  "<strong>codominante overerving zijn beide kenmerken naast elkaar zichtbaar</strong>."),
            ("p", "<strong>Bloedgroep AB is dus geen voorbeeld van intermediaire overerving</strong>, maar van "
                  "codominantie: A en B zijn er beide, niet iets ertussen."),
            ("p", "<strong>Drie</strong> allelen bepalen de ABO-bloedgroepen: "
                  "<strong>het allel voor A</strong>, <strong>het allel voor B</strong> en "
                  "<strong>het allel voor O</strong>. A en B zijn dominant over O. Bij "
                  "<strong>bloedgroep O</strong> hoort dus het genotype met <strong>twee keer het allel "
                  "O</strong>."),
            ("p", "<strong>Twee ouders met bloedgroep A kunnen een kind met bloedgroep O krijgen</strong>, als "
                  "ze beide heterozygoot zijn en elk het O-allel doorgeven."),
        ]),
        dict(kop="X-gebonden overerving en stambomen", blokken=[
            ("p", "Dat een aandoening <strong>X-gebonden overerft</strong>, betekent dat "
                  "<strong>het gen op het X-chromosoom ligt</strong>. <strong>Twee</strong> van de genoemde "
                  "aandoeningen erven zo over: <strong>hemofilie</strong> en "
                  "<strong>rood-groenkleurenblindheid</strong>."),
            ("p", "<strong>Rood-groenkleurenblindheid komt veel vaker voor bij jongens, omdat een jongen maar "
                  "één X-chromosoom heeft.</strong> Een meisje met één afwijkend allel heeft nog een gezond "
                  "X-chromosoom dat het opvangt."),
            ("p", "Niet elke aandoening is recessief. <strong>De ziekte van Huntington erft dominant over, dus "
                  "één afwijkend allel volstaat.</strong>"),
            ("p", "In een stamboom <strong>staat een vierkantje niet voor een vrouw en een cirkel niet voor een "
                  "man</strong>: het is net omgekeerd. Het vierkantje is de man, de cirkel de vrouw."),
        ]),
    ],
    onthoud=[
        "46 chromosomen in een lichaamscel (2n), 23 in een geslachtscel (n).",
        "Een man heeft X en Y; de zaadcel bepaalt het geslacht.",
        "Mitose geeft twee gelijke cellen, meiose vier verschillende haploïde.",
        "Een mutatie is alleen erfelijk als ze in een geslachtscel zit.",
        "Aa × Aa geeft 25 % met het recessieve kenmerk en 50 % dragers.",
        "In de F2 splitsen de fenotypes 3 op 1.",
        "Bloedgroep AB is codominant, niet intermediair.",
        "X-gebonden aandoeningen treffen jongens vaker: zij hebben maar één X.",
    ],
)

# ───────────────────────── 5. Biologische evolutie
BUNDELS["biologische-evolutie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Biologische evolutie",
    onder="De argumenten uit anatomie, fossielen en DNA, en waarom ze samen zo sterk staan.",
    secties=[
        dict(kop="Wat evolutie is", blokken=[
            ("p", "<strong>Biologische evolutie</strong> betekent dat <strong>soorten veranderen over vele "
                  "generaties heen</strong>. <strong>Evolutie gebeurt bij populaties, niet bij één "
                  "individu</strong>: een <strong>populatie</strong> zijn <strong>alle individuen van één soort "
                  "in één gebied</strong>."),
            ("p", "<strong>Evolutie heeft geen vooraf bepaald doel waar ze naartoe werkt.</strong> Ze is geen "
                  "ladder naar iets beters; ze is wat er overblijft van wat er gebeurde. Met de "
                  "<strong>oercel</strong> bedoelt men <strong>de eerste cel waaruit al het leven zou zijn "
                  "ontstaan</strong>."),
            ("p", "<strong>Tijd is belangrijk in de evolutietheorie omdat kleine veranderingen zich opstapelen "
                  "over vele generaties.</strong> Daar is ruimte voor: "
                  "<strong>de aarde is volgens het huidige natuurwetenschappelijke onderzoek ongeveer "
                  "4,6 miljard jaar oud</strong>."),
        ]),
        dict(kop="Argumenten uit de anatomie", blokken=[
            ("p", "<strong>Homologe organen</strong> zijn <strong>organen met dezelfde bouw maar een andere "
                  "functie</strong>. <strong>Analoge organen</strong> zijn net omgekeerd: "
                  "<strong>organen met dezelfde functie maar een andere bouw</strong>."),
            ("p", "<strong>De botten in de voorpoot van verschillende zoogdieren lijken zo sterk op elkaar "
                  "omdat ze van dezelfde voorouder komen.</strong> Een mensenarm, een vleermuisvleugel en een "
                  "walvisvin hebben dezelfde beenderen in dezelfde orde."),
            ("p", "Een <strong>rudimentair orgaan</strong> is een orgaan dat <strong>bij een soort nog aanwezig "
                  "is maar zijn functie verloren heeft</strong>. Bij de mens zijn er "
                  "<strong>twee</strong> zulke kenmerken: <strong>het staartbeentje</strong> en "
                  "<strong>de spiertjes die de oorschelp bewegen</strong>."),
            ("p", "<strong>Een walvis heeft kleine heupbeentjes die niets dragen.</strong> Daaruit besluit je "
                  "<strong>twee</strong> dingen: <strong>zijn voorouders hadden achterpoten</strong> en "
                  "<strong>die beentjes zijn rudimentaire kenmerken</strong>."),
            ("p", "Het <strong>argument uit de embryologie</strong> is dat "
                  "<strong>embryo's van verwante soorten sterk op elkaar lijken</strong>, ook als de volwassen "
                  "dieren dat helemaal niet meer doen."),
        ]),
        dict(kop="Argumenten uit de fossielen", blokken=[
            ("p", "<strong>Fossielen</strong> zijn de <strong>versteende resten of afdrukken van organismen uit "
                  "het verleden</strong>. De wetenschap <strong>die fossielen bestudeert</strong>, heet de "
                  "<strong>paleontologie</strong>. <strong>Fossielen in diepere aardlagen zijn meestal ouder "
                  "dan die in hogere lagen.</strong>"),
            ("p", "<strong>Archaeopteryx is een belangrijke vondst omdat hij kenmerken van reptielen én van "
                  "vogels heeft.</strong> Zo'n fossiel, dat <strong>kenmerken van twee groepen "
                  "combineert</strong>, heet een <strong>overgangsvorm</strong> of tussenvorm."),
            ("p", "Een <strong>evolutiereeks</strong> is <strong>een rij fossielen die de verandering van een "
                  "soort toont</strong>. Zulke reeksen zijn zeldzaam, want "
                  "<strong>van niet elke soort uit het verleden bestaat er een fossiel</strong>: fossiel worden "
                  "vraagt bijzondere omstandigheden."),
        ]),
        dict(kop="Argumenten uit DNA en biochemie", blokken=[
            ("p", "Het <strong>argument uit de biochemie</strong> is dat "
                  "<strong>alle organismen dezelfde soort DNA-code gebruiken</strong>. "
                  "<strong>Alle organismen gebruiken ook dezelfde vier basen in hun DNA.</strong>"),
            ("p", "<strong>Hoe meer het DNA van twee soorten op elkaar lijkt, hoe nauwer ze verwant zijn.</strong> "
                  "Omgekeerd zegt <strong>een groot verschil in DNA tussen twee soorten dat hun "
                  "gemeenschappelijke voorouder lang geleden leefde</strong>."),
            ("p", "De <strong>gemeenschappelijke voorouder</strong> is de soort <strong>waarvan twee huidige "
                  "soorten allebei afstammen</strong>. <strong>Die voorouder is niet altijd een soort die "
                  "vandaag nog leeft</strong>: meestal is ze uitgestorven. Daarom "
                  "<strong>stamt de mens ook niet af van de chimpansee zoals die vandaag leeft</strong>, maar "
                  "hebben mens en chimpansee een gemeenschappelijke voorouder."),
        ]),
        dict(kop="De evolutieboom lezen", blokken=[
            ("p", "Het schema <strong>waarin soorten als takken van één boom getekend worden</strong>, heet een "
                  "<strong>evolutieboom</strong> of verwantschapsdiagram. Je leest eraan af "
                  "<strong>welke soorten een recentere voorouder delen</strong>. Met de "
                  "<strong>tree of life</strong> bedoelt men <strong>het schema dat alle bekende soorten "
                  "verbindt</strong>."),
            ("p", "<strong>Splitsen twee soorten pas heel recent af in de boom, dan lijken ze genetisch sterk "
                  "op elkaar.</strong> Maar <strong>de soorten die het hoogst in de boom staan, staan niet het "
                  "verst in hun ontwikkeling</strong>: elke tak die vandaag nog leeft, is even lang bezig. Een "
                  "boom toont verwantschap, geen rangorde."),
            ("p", "Onderzoekers gebruiken vandaag <strong>twee</strong> soorten gegevens om een evolutieboom te "
                  "maken: <strong>de volgorde van de basen in het DNA</strong> en "
                  "<strong>de bouw van skeletten en organen</strong>. "
                  "<strong>Het feit dat anatomie en DNA tot dezelfde stamboom leiden, maakt die stamboom "
                  "betrouwbaarder.</strong>"),
            ("p", "Argumenten komen uit <strong>drie</strong> vakgebieden: <strong>de anatomie</strong>, "
                  "<strong>de paleontologie</strong> en <strong>de moleculaire biologie</strong>. "
                  "<strong>Ze vullen elkaar aan omdat ze los van elkaar op dezelfde verwantschap wijzen.</strong>"),
        ]),
        dict(kop="Waarom het een wetenschappelijke theorie is", blokken=[
            ("p", "<strong>De evolutietheorie is een wetenschappelijke theorie omdat ze op waarnemingen steunt "
                  "en getoetst kan worden.</strong> Een theorie in de wetenschap is geen gok, maar een "
                  "verklaring die veel bewijs achter zich heeft."),
            ("p", "<strong>Creationisme en Intelligent Design worden niet als wetenschappelijke theorieën "
                  "beschouwd omdat hun verklaring niet met waarnemingen te toetsen is.</strong> Dat zegt niets "
                  "over wat iemand persoonlijk gelooft; het zegt dat het geen natuurwetenschap is."),
            ("p", "<strong>De moderne evolutietheorie is sinds Darwin niet ongewijzigd gebleven.</strong> "
                  "Genetica, DNA-onderzoek en nieuwe fossielen hebben er veel aan toegevoegd. Dat een theorie "
                  "bijgestuurd wordt, is juist hoe wetenschap werkt."),
        ]),
    ],
    onthoud=[
        "Evolutie gebeurt bij populaties, over vele generaties, zonder vooraf bepaald doel.",
        "Homoloog: zelfde bouw, andere functie. Analoog: zelfde functie, andere bouw.",
        "Rudimentair: nog aanwezig, functie verloren (staartbeentje, walvisheupen).",
        "Fossielen in diepere lagen zijn ouder; Archaeopteryx is een overgangsvorm.",
        "Meer gelijkenis in DNA betekent nauwere verwantschap.",
        "Mens en chimpansee hebben een gemeenschappelijke voorouder, de een stamt niet van de ander af.",
        "Anatomie, paleontologie en moleculaire biologie wijzen samen dezelfde richting uit.",
        "De aarde is ongeveer 4,6 miljard jaar oud.",
    ],
)

# ───────────────────────── 6. Natuurlijke selectie en het ontstaan van soorten
BUNDELS["natuurlijke-selectie-en-het-ontstaan-van-soorten-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Natuurlijke selectie en het ontstaan van soorten",
    onder="Lamarck tegenover Darwin, hoe selectie werkt, hoe soorten splitsen, en de menswording.",
    secties=[
        dict(kop="Lamarck tegenover Darwin", blokken=[
            ("p", "<strong>Lamarck dacht over de lange hals van de giraf dat elk dier zich uitrekte en die "
                  "langere hals doorgaf.</strong> Eigenschappen die een dier tijdens zijn leven ontwikkelt en "
                  "volgens hem doorgeeft, noemde hij <strong>verworven eigenschappen</strong>. "
                  "<strong>Lamarck zou de kleine ogen van een mol dus verklaren doordat ze onder de grond niet "
                  "gebruikt werden en daardoor kleiner werden.</strong> Zo werkt het niet: wat je tijdens je "
                  "leven verandert, komt niet in je geslachtscellen."),
            ("p", "De <strong>kern van de theorie van Darwin</strong> is dat <strong>wie het best past bij de "
                  "omgeving, zich het meest voortplant</strong>. Twee uitspraken horen daarbij en niet bij "
                  "Lamarck: <strong>binnen een soort bestaat er variatie</strong> en "
                  "<strong>er worden meer jongen geboren dan er overleven</strong>."),
            ("p", "<strong>Darwin wist nog niet hoe eigenschappen precies worden doorgegeven.</strong> In de "
                  "moderne evolutietheorie zijn er <strong>twee</strong> dingen bijgekomen: "
                  "<strong>mutaties als bron van nieuwe variatie</strong> en "
                  "<strong>de genetica als verklaring voor overerving</strong>."),
        ]),
        dict(kop="Hoe natuurlijke selectie werkt", blokken=[
            ("p", "<strong>Survival of the fittest</strong> betekent dat <strong>wie het best bij zijn omgeving "
                  "past, het best overleeft</strong>. Het gaat dus niet over de sterkste of de snelste, maar "
                  "over wie past. Een kenmerk waarmee <strong>een organisme goed past bij zijn omgeving</strong>, "
                  "heet een <strong>aanpassing</strong> of adaptatie. De "
                  "<strong>strijd om voedsel, ruimte en partners binnen een populatie</strong> heet de "
                  "<strong>struggle for life</strong> of struggle for existence."),
            ("p", "Natuurlijke selectie heeft <strong>twee</strong> dingen nodig: "
                  "<strong>erfelijke variatie tussen individuen</strong> en "
                  "<strong>verschil in overlevings- of voortplantingskans</strong>. "
                  "<strong>Variatie binnen een populatie is belangrijk omdat er dan meer kans is dat sommigen "
                  "een verandering overleven</strong>, en daarom "
                  "<strong>maakt een kleine populatie een soort kwetsbaar: er is weinig variatie om op terug te "
                  "vallen</strong>."),
            ("kader", "Twee veelgemaakte fouten. <strong>Natuurlijke selectie maakt zelf geen nieuwe "
                      "eigenschappen aan</strong>: ze kiest uit wat er al is, en mutaties leveren het nieuwe. "
                      "En <strong>ze werkt niet even goed op aangeleerde als op erfelijke kenmerken</strong>, "
                      "maar <em>alleen</em> op erfelijke, want alleen die gaan door naar de volgende generatie. "
                      "<strong>Een organisme kan zich ook niet doelbewust aanpassen aan zijn omgeving om beter "
                      "te overleven.</strong>"),
            ("p", "Er bestaat ook <strong>seksuele selectie</strong>: <strong>partners kiezen voor bepaalde "
                  "kenmerken</strong>. Zo wordt een pauwenstaart groter zonder dat hij helpt om te overleven."),
        ]),
        dict(kop="Twee voorbeelden die je kan narekenen", blokken=[
            ("p", "<strong>De peper-en-zoutvlinders werden in de industriële streken donkerder, omdat donkere "
                  "vlinders op roetzwarte boomstammen minder opvielen.</strong> De lichte vielen op en werden "
                  "opgegeten. <strong>Toen de lucht schoner werd, nam het aandeel lichte peper-en-zoutvlinders "
                  "weer toe.</strong> De vlinders veranderden zelf niet van kleur; de verhouding in de "
                  "populatie veranderde."),
            ("p", "<strong>Antibioticaresistentie bij bacteriën ontstaat doordat enkele bacteriën al ongevoelig "
                  "waren en de kuur overleven.</strong> Die enkele vermenigvuldigen zich daarna ongestoord. "
                  "<strong>Een antibioticakuur vroegtijdig stoppen vergroot de kans op resistentie</strong>, "
                  "want dan blijven net de minst gevoelige bacteriën achter."),
        ]),
        dict(kop="Hoe een nieuwe soort ontstaat", blokken=[
            ("p", "Een <strong>soort</strong> is in de biologie <strong>een groep die onderling vruchtbare "
                  "nakomelingen krijgt</strong>. <strong>Een muildier is onvruchtbaar, en daarom zijn paard en "
                  "ezel twee verschillende soorten.</strong>"),
            ("p", "Nieuwe erfelijke variatie ontstaat uit <strong>twee</strong> bronnen: "
                  "<strong>uit mutaties in het DNA</strong> en "
                  "<strong>uit het herschikken van chromosomen bij de meiose</strong>. "
                  "<strong>Een mutatie draagt bij aan de evolutie van een soort doordat ze een nieuw allel "
                  "levert waarop selectie kan werken.</strong> Maar "
                  "<strong>een mutatie ontstaat niet omdat het organisme ze nodig heeft</strong>: ze valt "
                  "toevallig, en pas daarna blijkt of ze helpt."),
            ("p", "Het <strong>ontstaan van een nieuwe soort uit een bestaande</strong> heet "
                  "<strong>soortvorming</strong> of speciatie. <strong>Isolatie is daarvoor nodig, want zonder "
                  "isolatie blijven de groepen hun genen mengen.</strong>"),
            ("fig", tabel(["Soort isolatie", "Voorbeeld"], [
                ["Geografische isolatie", "een rivier verandert van loop en snijdt een populatie muizen in twee"],
                ["Temporele isolatie", "twee kikkersoorten in dezelfde vijver paren in verschillende maanden"],
                ["Gedragsisolatie", "twee vogelsoorten herkennen elkaars baltsroep niet"],
                ["Ecologische isolatie", "twee groepen in hetzelfde gebied gebruiken de boomtop en de bodem"],
                ["Morfologische isolatie", "de bouw van de dieren maakt paren onmogelijk"],
            ]), "De vormen van isolatie, elk met het voorbeeld waaraan je ze herkent."),
            ("p", "<strong>Morfologische isolatie betekent inderdaad dat de bouw van de dieren paren onmogelijk "
                  "maakt.</strong> Bij <strong>ecologische isolatie</strong> leven de groepen in hetzelfde "
                  "gebied, maar op een andere leefplek."),
        ]),
        dict(kop="De menswording", blokken=[
            ("p", "Het geheel van stappen <strong>waarbij de mens uit zijn voorouders ontstond</strong>, heet de "
                  "<strong>hominisatie</strong> of menswording. <strong>Rechtop lopen kwam daarin het "
                  "eerst</strong>, nog vóór de hersenen sterk groeiden. Het "
                  "<strong>voordeel van rechtop lopen was dat de handen vrijkwamen om dingen te dragen</strong>."),
            ("p", "Mens en mensapen hebben <strong>drie</strong> dingen gemeenschappelijk: "
                  "<strong>een grote hersenschors</strong>, <strong>handen met een tegenstelbare duim</strong> "
                  "en <strong>zorg voor de jongen gedurende jaren</strong>."),
            ("p", "<strong>Drie</strong> soorten horen bij de menselijke evolutie: "
                  "<strong>Australopithecus</strong>, <strong>Homo habilis</strong> en "
                  "<strong>Homo erectus</strong>. <strong>Homo neanderthalensis en Homo sapiens hebben een tijd "
                  "naast elkaar geleefd</strong>, en de evolutie van de mens is dus geen rechte rij."),
            ("p", "<strong>Biodiversiteit gaat niet alleen over het aantal soorten, maar ook over de variatie "
                  "binnen een soort</strong> en over de verscheidenheid aan leefgebieden."),
        ]),
    ],
    onthoud=[
        "Lamarck: verworven eigenschappen worden doorgegeven. Dat klopt niet.",
        "Darwin: er is variatie, er worden meer jongen geboren dan er overleven.",
        "Selectie heeft erfelijke variatie én verschil in overlevingskans nodig.",
        "Selectie kiest uit wat er is; mutaties leveren het nieuwe.",
        "Peper-en-zoutvlinders en antibioticaresistentie zijn de schoolvoorbeelden.",
        "Een soort krijgt onderling vruchtbare nakomelingen.",
        "Soortvorming vraagt isolatie: geografisch, temporeel, gedrag, ecologisch of morfologisch.",
        "In de hominisatie kwam rechtop lopen eerst; de handen kwamen vrij.",
    ],
)

# ───────────────────────── 7. Productlabels, pictogrammen en risico's van stoffen
BUNDELS["productlabels-pictogrammen-en-risico-s-van-stoffen-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Productlabels, pictogrammen en risico's van stoffen",
    onder="Pictogrammen, P- en H-zinnen, afval sorteren, kook- en smeltpunt, oplosmiddelen en de pH-schaal.",
    secties=[
        dict(kop="Pictogrammen en zinnen op een etiket", blokken=[
            ("p", "Van een <strong>gevarenpictogram</strong> lees je af <strong>welk soort gevaar de stof "
                  "oplevert</strong>. De <strong>H in een H-zin staat voor hazard</strong>, dus gevaar: die zin "
                  "zegt waarom de stof gevaarlijk is. In een <strong>P-zin</strong> staat "
                  "<strong>wat je moet doen om veilig met de stof om te gaan</strong>."),
            ("p", "<strong>Drie</strong> dingen horen bij de voorzorgen die je op een etiket terugvindt: "
                  "<strong>handschoenen dragen</strong>, <strong>buiten het bereik van kinderen houden</strong> "
                  "en <strong>bij contact met de ogen spoelen met water</strong>."),
            ("p", "Bij een stof <strong>die de huid wegvreet</strong> hoort "
                  "<strong>het pictogram voor bijtend of corrosief</strong>. Het "
                  "<strong>pictogram voor oxiderende stoffen</strong> betekent dat "
                  "<strong>de stof een brand kan voeden of versterken</strong>. En "
                  "<strong>een stof met het pictogram voor gassen onder druk mag je nooit in de zon laten "
                  "staan</strong>: warmte doet de druk in de fles stijgen."),
            ("p", "Op een fles <strong>ethanol staat het pictogram voor ontvlambaar, omdat de damp erboven vlam "
                  "kan vatten</strong>. Niet de vloeistof zelf brandt eerst, maar de damp."),
        ]),
        dict(kop="Concentratie en gevaar", blokken=[
            ("p", "<strong>Geconcentreerde ontstopper is corrosief en verdunde ontstopper alleen irriterend, "
                  "omdat hoe hoger de concentratie, hoe sterker het effect.</strong> Het is dezelfde stof, "
                  "alleen minder sterk. Daarom "
                  "<strong>kan dezelfde stof in een andere concentratie een ander gevarenpictogram "
                  "krijgen</strong>."),
            ("p", "Moet je kiezen tussen <strong>twee ontvetters, de ene bijtend en de andere alleen "
                  "irriterend, dan kies je om thuis te gebruiken de irriterende, want die geeft minder ernstige "
                  "schade</strong>. Diezelfde regel geldt algemeen: moet je kiezen "
                  "<strong>tussen twee producten die even goed werken, dan is het doorslaggevende argument het "
                  "product met het minst zware gevarenpictogram</strong>."),
        ]),
        dict(kop="Bewaren en sorteren", blokken=[
            ("p", "Een <strong>ontvlambare stof zoals thinner bewaar je goed gesloten, koel en ver van "
                  "vuur</strong>. En <strong>een product overgieten in een lege drankfles is géén veilige "
                  "manier om het te bewaren</strong>: dan staat er geen etiket meer op, en iemand kan ervan "
                  "drinken."),
            ("p", "<strong>Een restje chemisch product hoort bij het klein gevaarlijk afval en niet in de "
                  "gootsteen.</strong> Een <strong>halfvolle fles ontstopper of verf breng je naar het "
                  "kga</strong>, het klein gevaarlijk afval op het containerpark. En "
                  "<strong>ontstopper en bleekwater mag je zeker niet samen in dezelfde afvoer gieten</strong>: "
                  "samen kunnen ze giftige gassen vormen."),
            ("p", "<strong>Twee</strong> van de genoemde soorten afval horen bij het <strong>gft</strong>: "
                  "<strong>aardappelschillen</strong> en <strong>gemaaid gras</strong>. De afkorting "
                  "<strong>pmd</strong> staat voor <strong>plastic verpakkingen, metaal en "
                  "drankkartons</strong>."),
            ("p", "Het <strong>cijfer in de driehoek van pijltjes op een plastic verpakking</strong> zegt "
                  "<strong>uit welke kunststof de verpakking gemaakt is</strong>. "
                  "<strong>Die driehoek betekent dus niet dat de verpakking zeker gerecycleerd wordt</strong>: "
                  "het is een identificatiecode, geen belofte. Bij "
                  "<strong>recyclagecode 1</strong>, de code van de meeste drinkflessen, hoort "
                  "<strong>PET</strong> of polyethyleentereftalaat."),
        ]),
        dict(kop="Kookpunt en smeltpunt", blokken=[
            ("p", "Het <strong>kookpunt</strong> van een stof is <strong>de temperatuur waarbij ze overgaat van "
                  "vloeistof naar gas</strong>. <strong>Aceton is zo geschikt om glaswerk snel droog te maken, "
                  "omdat het een laag kookpunt heeft en dus vlot verdampt.</strong> "
                  "<strong>Een stof met een laag kookpunt is ook meestal gemakkelijk ontvlambaar</strong>, want "
                  "de damp staat er altijd boven. <strong>Het kookpunt zegt dus wél iets over hoe gevaarlijk "
                  "een stof kan zijn.</strong>"),
            ("p", "Zoek je <strong>een stof die bij kamertemperatuur vast is, dan let je erop dat het smeltpunt "
                  "boven de kamertemperatuur ligt</strong>."),
        ]),
        dict(kop="Oplossen", blokken=[
            ("p", "De vuistregel over oplossen luidt in drie woorden: <strong>soort lost soort</strong> op, ook "
                  "wel gelijk lost gelijk. Wat in water oplost, lost niet op in een organisch oplosmiddel, en "
                  "omgekeerd. <strong>Een stof die goed in water oplost, lost dus meestal niet goed op in "
                  "thinner.</strong>"),
            ("p", "<strong>Drie</strong> van de genoemde oplosmiddelen zijn vetoplosbaar of organisch: "
                  "<strong>thinner</strong>, <strong>terpentine</strong> en <strong>white spirit</strong>. "
                  "Wasbenzine hoort in dezelfde rij; water is het bekendste wateroplosbare middel."),
            ("p", "Heb je <strong>een vetvlek van olie op je kleren</strong>, dan verdwijnt die het best "
                  "<strong>met een vetoplosbaar oplosmiddel of afwasmiddel</strong>. Water alleen pakt vet niet "
                  "aan."),
        ]),
        dict(kop="Zuren, basen en de pH-schaal", blokken=[
            ("p", "De <strong>pH van een zure stof ligt onder 7</strong>. Een "
                  "<strong>neutrale stof zoals zuiver water heeft pH 7</strong>. Een stof "
                  "<strong>met een pH boven 7</strong> is een <strong>base</strong>."),
            ("p", "<strong>Een indicator geeft met een kleur aan of een stof zuur of basisch is.</strong> "
                  "<strong>Rode koolsap wordt in een zure vloeistof rood tot roze</strong>, en in een basische "
                  "eerder groen tot geel."),
            ("p", "<strong>Drie</strong> van de genoemde stoffen zijn zuren: "
                  "<strong>azijnzuur in huishoudazijn</strong>, <strong>citroenzuur in citroensap</strong> en "
                  "<strong>zoutzuur in maagsap</strong>. <strong>Zuren worden ook in voeding gebruikt, "
                  "bijvoorbeeld als bewaarmiddel.</strong>"),
            ("p", "<strong>Een partje citroen pak je beter niet in aluminiumfolie, omdat het zuur met het "
                  "aluminium reageert.</strong> Je ziet dan gaatjes in de folie en een rare smaak aan de "
                  "citroen."),
            ("kader", "<strong>Komt er een bijtende stof op je huid, dan spoel je meteen lang met veel "
                      "water.</strong> Niet neutraliseren met iets anders, niet afwachten: spoelen, en lang."),
        ]),
    ],
    onthoud=[
        "H-zin: het gevaar (hazard). P-zin: wat je moet doen.",
        "Dezelfde stof kan door een hogere concentratie een zwaarder pictogram krijgen.",
        "Chemische restjes horen bij het kga, nooit in de gootsteen.",
        "De driehoek met een cijfer zegt wélke kunststof, niet dat er gerecycleerd wordt.",
        "Code 1 is PET, de kunststof van de meeste drinkflessen.",
        "Een laag kookpunt betekent snel verdampen en vaak ontvlambaar.",
        "Soort lost soort: wat in water lost, lost niet in thinner.",
        "pH onder 7 is zuur, 7 is neutraal, boven 7 is basisch.",
    ],
)

# ───────────────────────── 8. Voedingsbestanddelen en etiketten
BUNDELS["voedingsbestanddelen-en-etiketten-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Voedingsbestanddelen en etiketten",
    onder="De voedingsstoffen en hun functie, en wat er op een etiket staat: nutriscore, ecoscore en allergenen.",
    secties=[
        dict(kop="Voedingsstof of voedingsmiddel", blokken=[
            ("p", "<strong>Het verschil tussen een voedingsstof en een voedingsmiddel is dat een voedingsmiddel "
                  "is wat je eet en een voedingsstof erin zit.</strong> Een appel is een voedingsmiddel; de "
                  "koolhydraten en vitaminen erin zijn de voedingsstoffen."),
            ("p", "<strong>Drie</strong> voedingsstoffen leveren energie: <strong>koolhydraten</strong>, "
                  "<strong>vetten</strong> en <strong>eiwitten</strong>. <strong>Water levert geen energie, "
                  "maar is toch onmisbaar</strong>, en <strong>vitaminen leveren evenmin energie</strong>."),
            ("p", "De <strong>voedingsdriehoek</strong> laat zien <strong>waarvan je veel mag eten en waarvan "
                  "beter weinig</strong>. Sterk bewerkte producten staan erbuiten, in de restgroep."),
        ]),
        dict(kop="Koolhydraten", blokken=[
            ("p", "Een koolhydraat dat <strong>uit één suikermolecule bestaat, zoals glucose</strong>, heet een "
                  "<strong>monosacharide</strong>. <strong>Zetmeel</strong> is daarentegen "
                  "<strong>een lange keten van suikermoleculen</strong>, dus een polysacharide."),
            ("p", "<strong>Zetmeel geeft trager energie dan glucose, omdat de lange keten eerst afgebroken moet "
                  "worden.</strong> Daarom <strong>komen glucose en fructose sneller in je bloed dan "
                  "zetmeel</strong>. <strong>Ga je zo meteen een uur lopen, dan eet je een paar uur vooraf dus "
                  "het best iets met zetmeel, zoals pasta of brood</strong>, en niet iets met losse suiker."),
            ("p", "<strong>Drie</strong> voedingsmiddelen zijn rijk aan zetmeel: "
                  "<strong>aardappelen</strong>, <strong>rijst</strong> en <strong>brood</strong>."),
        ]),
        dict(kop="Eiwitten, vetten, water, mineralen en vitaminen", blokken=[
            ("p", "Een <strong>eiwit bestaat uit aminozuren</strong>. De "
                  "<strong>belangrijkste functie van eiwitten in het lichaam is dat ze weefsels bouwen en "
                  "herstellen</strong>, en <strong>eiwitten zijn dus ook de belangrijkste bouwstof van je "
                  "spieren</strong>."),
            ("p", "Wat <strong>kenmerkend is voor een onverzadigd vetzuur</strong>, is dat "
                  "<strong>er minstens één dubbele binding in de keten zit</strong>. Daardoor krijgt de keten "
                  "een knik. <strong>Verzadigde vetten zijn bij kamertemperatuur dus niet vloeibaar maar "
                  "vast</strong>: boter en kokosvet zijn vast, olijfolie en zonnebloemolie vloeibaar."),
            ("p", "<strong>Twee</strong> voedingsmiddelen uit de reeks zijn rijk aan onverzadigde vetten: "
                  "<strong>olijfolie</strong> en <strong>noten</strong>. Vetten dienen in het lichaam voor "
                  "<strong>drie</strong> dingen: <strong>energie opslaan</strong>, "
                  "<strong>het lichaam isoleren tegen de kou</strong> en "
                  "<strong>bepaalde vitaminen opnemen</strong>, namelijk A, D, E en K."),
            ("p", "<strong>Calcium heb je nodig voor stevige botten en tanden.</strong> Het mineraal dat je "
                  "nodig hebt <strong>om hemoglobine te maken, de stof die zuurstof vervoert</strong>, is "
                  "<strong>ijzer</strong>."),
        ]),
        dict(kop="Het etiket lezen", blokken=[
            ("p", "De ingrediënten staan op een etiket <strong>van het meest naar het minst aanwezige</strong>. "
                  "<strong>Staat suiker als eerste in de ingrediëntenlijst, dan bevat het product er dus veel "
                  "van.</strong>"),
            ("p", "<strong>De allergenen herken je in een ingrediëntenlijst doordat ze in het vet of met "
                  "hoofdletters staan.</strong> Dat is wettelijk verplicht voor de veertien bekendste. "
                  "<strong>Op veel verpakkingen staat ook dat het product sporen van noten kan bevatten, omdat "
                  "er in dezelfde fabriek ook noten verwerkt worden.</strong>"),
            ("p", "De <strong>energiewaarde slaat op een etiket meestal op honderd gram of honderd "
                  "milliliter</strong>, en staat er <strong>in kilojoule</strong>, vaak met de kilocalorie "
                  "ernaast. <strong>Een etiket moet vermelden hoeveel energie, vet, koolhydraten, eiwit en zout "
                  "het product bevat.</strong>"),
            ("p", "Staat er <strong>suiker 32 g per 100 g</strong>, dan betekent dat dat "
                  "<strong>bijna een derde van het product suiker is</strong>. In "
                  "<strong>een pot van 250 gram zit dan 80 g suiker</strong>: 32 maal 2,5."),
        ]),
        dict(kop="Nutriscore en ecoscore", blokken=[
            ("p", "De <strong>nutriscore</strong> zegt <strong>hoe gezond de samenstelling van een product "
                  "is</strong>. Het is het systeem <strong>met de letters A tot E</strong>. "
                  "<strong>Drie</strong> bestanddelen trekken hem naar beneden: <strong>veel suiker</strong>, "
                  "<strong>veel zout</strong> en <strong>veel verzadigd vet</strong>. Vezels, eiwit, fruit en "
                  "groenten tellen in de gunstige richting."),
            ("p", "<strong>Een product met nutriscore A mag je niet in onbeperkte hoeveelheden eten.</strong> "
                  "De score vergelijkt producten binnen dezelfde groep en zegt niets over de hoeveelheid."),
            ("p", "In de <strong>ecoscore</strong> telt <strong>de belasting van het milieu over de hele "
                  "levenscyclus</strong> mee. De <strong>levenscyclus</strong> is "
                  "<strong>de hele weg van een product, van grondstof tot afval</strong>. "
                  "<strong>Twee</strong> dingen kunnen er een bonus opleveren in de ecoscore: "
                  "<strong>een biologische teelt</strong> en "
                  "<strong>een goed recycleerbare verpakking</strong>. "
                  "<strong>De ecoscore hangt dus mee af van de verpakking.</strong>"),
            ("p", "<strong>Nutriscore en ecoscore meten niet hetzelfde</strong>: de ene gaat over jouw "
                  "gezondheid, de andere over het milieu. Zijn "
                  "<strong>twee producten even voedzaam en komt het ene van hier terwijl het andere overgevlogen "
                  "is, dan haalt het product van hier een betere ecoscore</strong>; de nutriscore blijft "
                  "dezelfde."),
            ("p", "Heb je <strong>midden in de namiddag een energiedip, dan helpt een stuk fruit het "
                  "snelst</strong>: daarin zitten glucose en fructose, die meteen opgenomen worden."),
        ]),
    ],
    onthoud=[
        "Koolhydraten, vetten en eiwitten leveren energie; water en vitaminen niet.",
        "Zetmeel is een lange keten en geeft daarom tragere energie dan glucose.",
        "Eiwitten bouwen en herstellen; vetten slaan op, isoleren en nemen vitaminen op.",
        "Calcium voor botten en tanden, ijzer voor hemoglobine.",
        "Ingrediënten staan van meest naar minst; allergenen staan in het vet.",
        "De energiewaarde staat per 100 g of 100 mL, in kilojoule.",
        "Nutriscore gaat over gezondheid, ecoscore over het milieu.",
        "De ecoscore kijkt naar de hele levenscyclus, met bonussen en malussen.",
    ],
)

# ───────────────────────── 9. Dosis en concentratie van stoffen
BUNDELS["dosis-en-concentratie-van-stoffen-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Dosis en concentratie van stoffen",
    onder="Massaprocent, volumeprocent en massaconcentratie, met de rekenwerkjes, en daarna de ADI en de LD50.",
    secties=[
        dict(kop="Dosis of concentratie", blokken=[
            ("p", "<strong>Het verschil tussen de dosis en de concentratie van een stof is dat de dosis is "
                  "hoeveel je binnenkrijgt en de concentratie hoe sterk het is.</strong> De concentratie is een "
                  "eigenschap van het product, de dosis van wat er in jouw lichaam komt."),
            ("p", "<strong>De concentratie van een product zegt op zich dus nog niet hoeveel je ervan "
                  "binnenkrijgt.</strong> En <strong>je kan de dosis die je binnenkrijgt niet gewoon van het "
                  "etiket aflezen zonder te rekenen</strong>: op het etiket staat de concentratie, en je moet "
                  "de hoeveelheid er zelf bij rekenen."),
        ]),
        dict(kop="De concentratie-uitdrukkingen", blokken=[
            ("p", "<strong>Drie</strong> van de vier genoemde uitdrukkingen zijn concentratie-uitdrukkingen: "
                  "<strong>massaprocent</strong>, <strong>volumeprocent</strong> en "
                  "<strong>massaconcentratie</strong>. Het lichaamsgewicht hoort bij de dosis."),
            ("fig", tabel(["Uitdrukking", "Wat ze vergelijkt", "Voorbeeld"], [
                ["Massaprocent", "massa met massa, per 100 g", "15 g zout in 300 g pekel is 5 %"],
                ["Volumeprocent", "volume met volume, per 100 mL", "12 % vol is 12 mL alcohol per 100 mL"],
                ["Massaconcentratie", "massa met volume, in g/L", "20 g in 500 mL is 40 g/L"],
            ]), "De drie uitdrukkingen, en hoe je ze uit elkaar houdt."),
            ("p", "Het <strong>massaprocent</strong> is de uitdrukking die zegt "
                  "<strong>hoeveel gram stof er in 100 gram mengsel zit</strong>. Los je "
                  "<strong>15 g zout op in water en krijg je 300 g pekel, dan is het massaprocent 5 %</strong>: "
                  "15 gedeeld door 300, maal honderd. Let op dat je deelt door de massa van de hele oplossing. "
                  "<strong>Vijf massaprocent betekent dus niet vijf gram stof per liter mengsel</strong>; dat "
                  "laatste zou een massaconcentratie zijn."),
            ("p", "Staat er op een fles wijn <strong>12 % vol</strong>, dan betekent dat "
                  "<strong>12 mL alcohol in elke 100 mL wijn</strong>. "
                  "<strong>Volumeprocent wordt vooral gebruikt als je twee vloeistoffen mengt</strong>, want "
                  "volume is dan het makkelijkst te meten. Het getal "
                  "<strong>op een fles drank dat zegt welk deel van het volume alcohol is</strong>, heet het "
                  "<strong>alcoholpercentage</strong>."),
            ("p", "Een <strong>massaconcentratie</strong> druk je meestal uit in <strong>g/L</strong>, gram per "
                  "liter."),
        ]),
        dict(kop="Rekenen met concentratie", blokken=[
            ("p", "Een <strong>flesje bier van 250 mL met 5 % vol</strong> bevat "
                  "<strong>12,5 mL alcohol</strong>: 250 maal 0,05. Een "
                  "<strong>fles wijn van 750 mL met 12 % vol</strong> bevat "
                  "<strong>90 mL alcohol</strong>: 750 maal 0,12."),
            ("p", "Los je <strong>20 g suiker op tot 500 mL drank, dan is de massaconcentratie 40 g/L</strong>, "
                  "want een halve liter wordt verdubbeld naar een hele. Een "
                  "<strong>drankje met 2 g vitamine C per 250 mL</strong> heeft een massaconcentratie van "
                  "<strong>8 g/L</strong>, want een kwart liter wordt vier keer genomen."),
            ("p", "Omgekeerd kan je uit een concentratie de hoeveelheid halen. Een "
                  "<strong>oplossing van 30 g/L zout bevat in 200 mL 6 g zout</strong>: een vijfde liter, dus "
                  "dertig gedeeld door vijf."),
            ("p", "Om te berekenen <strong>hoeveel alcohol er in een glas zit, moet je twee dingen "
                  "kennen</strong>: <strong>het volume van het glas</strong> en "
                  "<strong>het alcoholpercentage van de drank</strong>. Staan er "
                  "<strong>twee glazen met dezelfde drank, één van 100 mL en één van 200 mL, dan zit er in het "
                  "grote glas twee keer zoveel alcohol</strong>; de concentratie is in beide gelijk."),
            ("p", "<strong>Hoe hoger de concentratie van een oplossing, hoe méér stof er in elke liter "
                  "zit</strong>, niet minder. Verdunnen verlaagt de concentratie."),
        ]),
        dict(kop="Concentratie en gevaar", blokken=[
            ("p", "<strong>Geconcentreerde ontstopper is bijtend en verdunde ontstopper enkel irriterend.</strong> "
                  "Daaruit leer je dat <strong>het gevaar van een stof afhangt van de concentratie</strong>, en "
                  "dus <strong>kan dezelfde stof een ander gevarenpictogram krijgen als de concentratie "
                  "verandert</strong>."),
            ("p", "<strong>Twee stoffen met dezelfde concentratie kunnen toch een heel verschillend gevaar "
                  "inhouden.</strong> De concentratie zegt alleen hoeveel stof er in het mengsel zit, niet hoe "
                  "giftig die stof is."),
        ]),
        dict(kop="ADI en LD50", blokken=[
            ("p", "De hoeveelheid van een stof <strong>die je elke dag zonder gevaar binnen mag krijgen</strong>, "
                  "heet de <strong>ADI</strong>, de aanvaardbare dagelijkse inname. "
                  "<strong>De ADI geldt per dag en per kilogram lichaamsgewicht.</strong> Ze is "
                  "<strong>per kilogram uitgedrukt omdat een zwaarder lichaam meer van een stof "
                  "verdraagt</strong>: dezelfde hoeveelheid wordt er sterker verdund."),
            ("p", "Is de <strong>ADI van een zoetstof 7 mg per kg per dag, dan mag een kind van 30 kg 210 mg "
                  "per dag</strong>. Is de <strong>ADI van een kleurstof 4 mg per kg per dag, dan mag een "
                  "volwassene van 70 kg 280 mg per dag</strong>."),
            ("p", "De <strong>LD50</strong> van een stof is <strong>de dosis waarbij de helft van de "
                  "proefdieren sterft</strong>. <strong>LD</strong> staat voor "
                  "<strong>lethale dosis</strong> of letale dosis, de dodelijke dosis, en 50 voor die helft."),
            ("p", "<strong>Een stof met een lage LD50 is giftiger dan een stof met een hoge LD50.</strong> Heeft "
                  "<strong>stof A een LD50 van 50 mg per kg en stof B van 5000 mg per kg, dan is stof A honderd "
                  "keer giftiger dan stof B</strong>. Is de "
                  "<strong>LD50 2000 mg per kg, dan is dat voor een mens van 60 kg een dosis van 120 g</strong>: "
                  "2000 maal 60 is 120 000 mg, en dat gedeeld door duizend geeft gram."),
            ("p", "<strong>Een stof met een hoge LD50 kan je dus niet zonder zorgen in elke hoeveelheid "
                  "gebruiken.</strong> Een hoge LD50 zegt alleen dat er veel van nodig is."),
        ]),
        dict(kop="Waarom de dosis alles bepaalt", blokken=[
            ("p", "<strong>Of een stof jou schade doet, hangt van twee dingen af</strong>: "
                  "<strong>hoeveel je ervan binnenkrijgt</strong> en <strong>hoeveel je zelf weegt</strong>. "
                  "Daarom <strong>krijgen twee mensen die dezelfde hoeveelheid van een stof binnenkrijgen niet "
                  "altijd precies dezelfde dosis per kilogram</strong>: bij een lichter lichaam is het meer."),
            ("p", "De concentratie maal het volume geeft de dosis. Bevat "
                  "<strong>een drank 40 g suiker per liter, dan krijg je met een glas van 200 mL 8 g "
                  "binnen</strong>."),
            ("p", "<strong>Men zegt dat elke stof giftig kan zijn, omdat boven een bepaalde dosis elke stof "
                  "schade doet.</strong> Zelfs water. En "
                  "<strong>een vitamine die nodig is maar in te grote hoeveelheid schadelijk, leert je dat ook "
                  "een nuttige stof een veilige bovengrens heeft</strong>."),
            ("p", "<strong>Op een geneesmiddel voor kinderen staat een andere dosering dan voor volwassenen, "
                  "omdat kinderen minder wegen en dus minder verdragen.</strong>"),
            ("p", "<strong>Een ADI geldt voor dagelijks gebruik, een LD50 voor één keer. Dat verschil is "
                  "belangrijk omdat een kleine hoeveelheid op lange termijn kan ophopen.</strong>"),
        ]),
    ],
    onthoud=[
        "Concentratie is hoe sterk het is, dosis is hoeveel je binnenkrijgt.",
        "Massaprocent per 100 g, volumeprocent per 100 mL, massaconcentratie in g/L.",
        "Volume maal percentage geeft de hoeveelheid; concentratie maal volume geeft de dosis.",
        "Hoe hoger de concentratie, hoe zwaarder het gevaar van dezelfde stof.",
        "De ADI geldt per dag en per kilogram lichaamsgewicht.",
        "De LD50 is de dosis waarbij de helft van de proefdieren sterft.",
        "Hoe lager de LD50, hoe giftiger de stof.",
        "Boven een bepaalde dosis doet elke stof schade, ook een nuttige.",
    ],
)

# ───────────────────────── 10. Duurzame chemie
BUNDELS["duurzame-chemie-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Duurzame chemie",
    onder="Lineair of circulair, de ladder van Lansink, greenwashing, kunststoffen en de kleuren van waterstof.",
    secties=[
        dict(kop="Van lineair naar circulair", blokken=[
            ("p", "Een <strong>lineaire economie</strong> is: <strong>grondstof nemen, product maken, afval "
                  "weggooien</strong>. Dat patroon heet ook take make waste, en "
                  "<strong>cradle to grave is een andere naam voor zo'n lineaire keten</strong>."),
            ("p", "Een economie <strong>waarin afval opnieuw grondstof wordt</strong>, is een "
                  "<strong>circulaire economie</strong> of keteneconomie. Met "
                  "<strong>cradle to cradle</strong> bedoelt men dat <strong>elk materiaal na gebruik opnieuw "
                  "grondstof wordt</strong>: <strong>in het cradle to cradle-denken bestaat afval niet, alleen "
                  "grondstof</strong>."),
            ("p", "<strong>Het verschil tussen een keteneconomie met en zonder recyclage is dat het materiaal "
                  "met recyclage terugkeert in de keten.</strong> Zonder recyclage wordt het product wel lang "
                  "gebruikt, maar eindigt het materiaal toch als afval. In "
                  "<strong>twee</strong> ketens gaat het materiaal dus na gebruik verloren: bij "
                  "<strong>take make waste</strong> en bij de "
                  "<strong>keteneconomie zonder recyclage</strong>."),
            ("p", "<strong>De duurzaamheid van een proces meet je aan drie dingen</strong>: "
                  "<strong>hoeveel grondstoffen het verbruikt</strong>, "
                  "<strong>hoeveel energie het verbruikt</strong> en "
                  "<strong>hoe goed het materiaal recycleerbaar is</strong>. Daar komt de milieubelasting nog "
                  "bij."),
        ]),
        dict(kop="Up-, down- en recycleren", blokken=[
            ("p", "<strong>Downcycling</strong> is <strong>recycleren tot een materiaal van mindere "
                  "kwaliteit</strong>: <strong>het gerecycleerde materiaal levert dan een product van mindere "
                  "kwaliteit op</strong>. <strong>Upcycling</strong> is het omgekeerde: "
                  "<strong>er iets van hogere waarde van maken</strong>."),
            ("p", "<strong>Het verschil tussen hergebruiken en recycleren is dat bij hergebruik het voorwerp "
                  "blijft zoals het is.</strong> Een glazen fles opnieuw vullen is hergebruik, ze versmelten "
                  "tot nieuw glas is recyclage."),
        ]),
        dict(kop="De ladder van Lansink", blokken=[
            ("p", "De ladder <strong>die de stappen van afvalverwerking van best naar slechtst zet</strong>, is "
                  "de <strong>ladder van Lansink</strong>. Bovenaan staat "
                  "<strong>voorkomen dat er afval ontstaat</strong>, dus preventie. Onderaan staat storten."),
            ("fig", tabel(["Trede", "Wat het is"], [
                ["1. Preventie", "voorkomen dat er afval ontstaat"],
                ["2. Hergebruik", "het voorwerp blijft zoals het is"],
                ["3. Recyclage", "het materiaal wordt opnieuw grondstof"],
                ["4. Verbranden", "de warmte wordt nog benut"],
                ["5. Storten", "het materiaal gaat verloren"],
            ]), "De ladder van Lansink, van best naar slechtst."),
            ("p", "<strong>Drie</strong> stappen staan hoger dan verbranden: <strong>preventie</strong>, "
                  "<strong>hergebruik</strong> en <strong>recyclage</strong>. En let op de orde: "
                  "<strong>recycleren staat niet hoger dan hergebruiken</strong>, maar lager, want recycleren "
                  "kost extra energie."),
        ]),
        dict(kop="Greenwashing, SDG's en de vijf P's", blokken=[
            ("p", "<strong>Greenwashing</strong> is <strong>zich groener voordoen dan men werkelijk is</strong>. "
                  "<strong>Staat er een groen blaadje op een verpakking, dan is het product dus niet daardoor "
                  "duurzaam</strong>: een blaadje is geen keurmerk en wordt door niemand gecontroleerd."),
            ("p", "De Verenigde Naties heeft <strong>17</strong> duurzame ontwikkelingsdoelstellingen of SDG's "
                  "opgesteld, te halen tegen 2030. De <strong>vijf P's</strong> van duurzaamheid zijn people, "
                  "planet, prosperity, peace en partnership; <strong>planet staat voor de zorg voor het milieu "
                  "en de natuur</strong>."),
        ]),
        dict(kop="Kunststoffen", blokken=[
            ("p", "Wat <strong>kenmerkend is voor een thermoplast</strong>, is dat "
                  "<strong>de ketens los naast elkaar liggen en smelten</strong>. Daarom "
                  "<strong>kan je een thermoplast omsmelten en opnieuw tot een ander product vormen</strong>."),
            ("p", "De bruggen <strong>die de ketens van een kunststof aan elkaar vastmaken</strong>, heten "
                  "<strong>crosslinks</strong> of dwarsverbindingen. <strong>Een thermoharder smelt niet omdat de ketens met "
                  "crosslinks aan elkaar vastzitten</strong> en zo één groot netwerk vormen. Een "
                  "<strong>elastomeer</strong> heeft er weinig: het is "
                  "<strong>rekbaar en springt weer in vorm</strong>."),
            ("p", "<strong>Twee</strong> materialen zijn daardoor moeilijk te recycleren: "
                  "<strong>een thermoharder</strong> en <strong>een elastomeer</strong>. "
                  "<strong>Gewone kunststof wordt gemaakt uit twee grondstoffen</strong>: "
                  "<strong>aardolie</strong> en <strong>aardgas</strong>, en die groeien niet aan."),
            ("p", "<strong>Biogebaseerd</strong> betekent <strong>gemaakt uit plantaardige "
                  "grondstoffen</strong>. <strong>Biodegradeerbaar</strong> betekent dat "
                  "<strong>micro-organismen het kunnen afbreken</strong>. "
                  "<strong>Een biogebaseerd product is daarom nog niet biodegradeerbaar</strong>: het ene gaat "
                  "over het begin, het andere over het einde van het leven van het materiaal. "
                  "<strong>Composteerbaar is strenger dan biodegradeerbaar, want het moet binnen een "
                  "afgesproken tijd afbreken.</strong>"),
            ("p", "De heel kleine plasticdeeltjes <strong>die in het milieu achterblijven</strong>, heten "
                  "<strong>microplastics</strong>. Afbreken tot kleine stukjes is dus niet hetzelfde als "
                  "verdwijnen."),
        ]),
        dict(kop="Energie, waterstof en water", blokken=[
            ("p", "<strong>Twee</strong> van de genoemde energievormen zijn hernieuwbaar: "
                  "<strong>windenergie</strong> en <strong>zonne-energie</strong>. "
                  "<strong>Kernenergie is geen fossiele energievorm</strong>, maar een aparte vorm naast fossiel "
                  "en hernieuwbaar. <strong>Groene stroom komt uit hernieuwbare bronnen zoals zon, wind en "
                  "water</strong>; grijze stroom uit fossiele brandstoffen."),
            ("fig", tabel(["Waterstof", "Waaruit", "De CO2"], [
                ["Grijs", "uit aardgas", "komt vrij"],
                ["Blauw", "uit aardgas", "wordt afgevangen en opgeslagen"],
                ["Groen", "uit water, met hernieuwbare stroom", "komt niet vrij"],
            ]), "De drie kleuren waterstof."),
            ("p", "Men spreekt van <strong>groene waterstof als ze met hernieuwbare stroom uit water "
                  "komt</strong>. <strong>Grijze waterstof</strong> is "
                  "<strong>waterstof uit aardgas, waarbij de CO2 vrijkomt</strong>. En "
                  "<strong>blauwe waterstof komt uit aardgas, maar de koolstofdioxide wordt afgevangen en "
                  "opgeslagen</strong>."),
            ("p", "<strong>Zwart water</strong> is <strong>afvalwater van het toilet</strong>. Grijs water komt "
                  "van bad, lavabo en wasmachine; wit water is zuiver water dat je kan drinken."),
            ("p", "<strong>Het verschil tussen CO2-neutrale en CO2-negatieve productie is dat negatief meer CO2 "
                  "uit de lucht haalt dan het uitstoot.</strong> Bij neutraal heffen uitstoot en opname elkaar "
                  "op."),
        ]),
    ],
    onthoud=[
        "Lineair is take make waste, ook cradle to grave genoemd.",
        "Cradle to cradle: afval bestaat niet, alles wordt opnieuw grondstof.",
        "Downcycling verliest kwaliteit, upcycling wint waarde.",
        "Ladder van Lansink: preventie, hergebruik, recyclage, verbranden, storten.",
        "Greenwashing is zich groener voordoen dan men is.",
        "Thermoplasten smelten en zijn recycleerbaar; crosslinks maken dat onmogelijk.",
        "Biogebaseerd gaat over de grondstof, biodegradeerbaar over het afbreken.",
        "Grijze waterstof uit aardgas, blauw met opslag van CO2, groen uit water.",
    ],
)

# ───────────────────────── 11. Elektromagnetisme
BUNDELS["elektromagnetisme-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Elektromagnetisme",
    onder="Ferromagnetische stoffen en weissgebieden, de polen en het aardmagnetisch veld, veldlijnen en de elektromagneet.",
    secties=[
        dict(kop="Welke stoffen magnetisch zijn", blokken=[
            ("p", "<strong>Drie</strong> metalen zijn <strong>ferromagnetisch</strong>: "
                  "<strong>ijzer</strong>, <strong>nikkel</strong> en <strong>kobalt</strong>. Dat een stof "
                  "ferromagnetisch is, <strong>betekent dat ze sterk door een magneet aangetrokken "
                  "wordt</strong>."),
            ("p", "<strong>Een magneet trekt dus niet élk metaal aan</strong>: koper, aluminium, zilver en goud "
                  "zijn metalen die blijven liggen, en <strong>een magneet trekt ook geen aluminium blikje "
                  "aan</strong>. Van de genoemde voorwerpen trekt hij er <strong>twee</strong> aan: "
                  "<strong>een ijzeren spijker</strong> en <strong>een stalen schroef</strong>, want staal "
                  "bestaat grotendeels uit ijzer."),
        ]),
        dict(kop="Magnetisme op atoomschaal", blokken=[
            ("p", "De kleine gebiedjes in ijzer <strong>die elk als een piepklein magneetje werken</strong>, "
                  "heten <strong>weissgebieden</strong>, elementaire magneetjes of magneculen. <strong>Magnetisme komt op atomaire schaal van de "
                  "elektronenspin en de kringstromen</strong>: elk elektron draait om zichzelf en om de kern."),
            ("p", "<strong>Een gewone ijzeren spijker is niet zelf een magneet, omdat de weissgebieden alle "
                  "richtingen uit wijzen.</strong> Ze heffen elkaar dan op. Zet je ze op één lijn, dan heb je "
                  "wel een magneet."),
            ("p", "<strong>Magnetische influentie</strong> is dat <strong>een stuk ijzer bij een magneet zelf "
                  "tijdelijk magnetisch wordt</strong>. Daarom "
                  "<strong>kan een paperclip die aan een magneet hangt zelf een tweede paperclip "
                  "aantrekken</strong>."),
            ("p", "Je kan <strong>een permanente magneet zijn magnetisme doen verliezen door hem sterk te "
                  "verhitten of er hard op te slaan</strong>. <strong>Een magneet verliest zijn magnetisme als "
                  "je hem sterk verhit</strong>, want de weissgebieden gaan weer door elkaar liggen."),
        ]),
        dict(kop="Polen", blokken=[
            ("p", "De <strong>twee uiteinden van een magneet, waar het veld het sterkst is</strong>, heten de "
                  "<strong>polen</strong>. <strong>Breng je twee noordpolen bij elkaar, dan stoten ze elkaar "
                  "af</strong>. <strong>Leg je de zuidpool van de ene magneet tegen de noordpool van de andere, "
                  "dan trekken ze elkaar aan.</strong> "
                  "<strong>Ongelijksoortige magneetpolen stoten elkaar dus niet af</strong>, maar trekken aan."),
            ("p", "<strong>Breek je een staafmagneet middendoor, dan heb je twee magneten met elk een noord- en "
                  "een zuidpool.</strong> Een losse pool bestaat niet."),
            ("p", "<strong>Bij de geografische noordpool ligt de magnetische zuidpool</strong> van het "
                  "aardmagnetisch veld, en bij de geografische zuidpool de magnetische noordpool. Precies "
                  "daarom <strong>wijst de noordpool van een kompasnaald naar de geografische "
                  "noordpool</strong>. <strong>Een kompasnaald staat niet willekeurig stil, want ze richt zich "
                  "naar het magneetveld van de aarde.</strong>"),
        ]),
        dict(kop="Het magneetveld en zijn veldlijnen", blokken=[
            ("p", "<strong>Buiten een magneet lopen de magnetische veldlijnen van de noordpool naar de "
                  "zuidpool</strong>, en binnenin terug. <strong>Magnetische veldlijnen kunnen elkaar niet "
                  "kruisen</strong>: op een kruispunt zou het veld twee richtingen hebben."),
            ("p", "<strong>De veldlijnen van een staafmagneet liggen het dichtst bij elkaar bij de "
                  "polen</strong>, en daar is het veld dus het sterkst."),
            ("p", "Ook rond een draad is er een veld: <strong>rond een draad waar stroom door loopt staat wél "
                  "een magneetveld</strong>, en het heeft de vorm van <strong>cirkels rond de draad</strong>. "
                  "Zo'n draad noem je een <strong>stroomvoerende draad</strong>: er loopt stroom door. "
                  "<strong>Rond een rechte stroomvoerende draad zijn de veldlijnen dus cirkels rond de "
                  "draad</strong>, en een kompasnaald ernaast draait weg zodra je de stroom aanzet."),
        ]),
        dict(kop="De elektromagneet", blokken=[
            ("p", "Een draad <strong>die in vele wikkelingen rond een as gedraaid is</strong>, heet een "
                  "<strong>spoel</strong> of solenoïde. Een <strong>elektromagneet</strong> is "
                  "<strong>een spoel die magnetisch wordt door een stroom</strong>, en hij is "
                  "<strong>enkel magnetisch zolang er stroom door loopt</strong>."),
            ("p", "Je maakt hem sterker op <strong>twee</strong> manieren: "
                  "<strong>meer wikkelingen rond de spoel leggen</strong> en "
                  "<strong>een grotere stroom door de spoel sturen</strong>. Daarnaast "
                  "<strong>maakt de ferromagnetische kern het magneetveld veel sterker</strong>, doordat de "
                  "weissgebieden in die kern mee op één lijn gaan staan."),
            ("p", "De <strong>rechterhandregel</strong> gebruik je bij een spoel <strong>om te vinden waar de "
                  "noordpool zit</strong>: je vingers volgen de stroom, je duim wijst naar de noordpool. "
                  "<strong>Weet je welke kant de stroom in een spoel rondgaat, dan vind je dus aan welk uiteinde "
                  "de noordpool ligt.</strong> En "
                  "<strong>draai je de stroomrichting om, dan wisselen de noord- en de zuidpool van "
                  "plaats</strong>."),
        ]),
        dict(kop="Toepassingen", blokken=[
            ("p", "In <strong>twee</strong> van de genoemde toepassingen zit een elektromagneet: "
                  "<strong>een elektrische deurbel</strong> en <strong>een relais</strong>. "
                  "<strong>Een bordmagneet is géén elektromagneet</strong>, maar een permanente magneet, net "
                  "als een kastsluiting of een kompas."),
            ("p", "Een <strong>elektrische deurbel werkt doordat een spoel een hamertje tegen een klankschaal "
                  "trekt</strong>, waarbij ze het contact verbreekt en weer sluit. Een "
                  "<strong>relais zet met een kleine stroom een grote stroom aan</strong>. Een "
                  "<strong>automatische zekering gebruikt een elektromagneet om de stroom te "
                  "onderbreken</strong> als die te groot wordt. In een luidspreker "
                  "<strong>laat de elektromagneet de conus heen en weer trillen</strong>."),
            ("p", "<strong>Een schrootkraan gebruikt een elektromagneet en geen permanente magneet, zodat de "
                  "lading ook weer gelost kan worden.</strong> Je zet de stroom af en het schroot valt waar het "
                  "moet zijn."),
        ]),
    ],
    onthoud=[
        "Ferromagnetisch: ijzer, nikkel en kobalt. Koper en aluminium niet.",
        "Weissgebieden op één lijn maken een magneet; warmte of een schok verstoort ze.",
        "Gelijksoortige polen stoten af, ongelijksoortige trekken aan.",
        "Bij de geografische noordpool ligt de magnetische zuidpool.",
        "Veldlijnen lopen buiten van noord naar zuid en kruisen elkaar nooit.",
        "Een elektromagneet werkt enkel met stroom; meer wikkelingen en meer stroom maken hem sterker.",
        "De rechterhandregel geeft de noordpool van een spoel.",
        "Deurbel, relais, zekering, luidspreker en schrootkraan werken met een elektromagneet.",
    ],
)

# ───────────────────────── 12. Golven, geluid en het elektromagnetisch spectrum
BUNDELS["golven-geluid-en-het-elektromagnetisch-spectrum-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Golven, geluid en het elektromagnetisch spectrum",
    onder="Wat een golf is en hoe je haar beschrijft, geluid en de decibelschaal, en de soorten straling.",
    secties=[
        dict(kop="Wat een golf is", blokken=[
            ("p", "Een golf vervoert <strong>energie</strong> van de ene plaats naar de andere. "
                  "<strong>Een golf vervoert geen materie</strong>: een kurk op het water gaat op en neer en "
                  "blijft liggen waar hij lag."),
            ("p", "<strong>Het verschil tussen een mechanische en een elektromagnetische golf is dat een "
                  "mechanische golf een middenstof nodig heeft.</strong> <strong>Twee</strong> van de genoemde "
                  "golven zijn mechanisch: <strong>geluid</strong> en <strong>een golf op het water</strong>. "
                  "Licht en radiogolven komen ook door het vacuüm."),
            ("p", "Wat <strong>kenmerkend is voor een transversale golf</strong>, is dat "
                  "<strong>de deeltjes dwars op de voortplantingsrichting trillen</strong>. "
                  "<strong>Geluid is een longitudinale golf, omdat de lucht in dezelfde richting trilt als de "
                  "golf loopt.</strong>"),
        ]),
        dict(kop="Een golf in cijfers", blokken=[
            ("p", "De <strong>afstand tussen twee opeenvolgende golftoppen</strong> is de "
                  "<strong>golflengte</strong>, met het symbool lambda. De "
                  "<strong>amplitude</strong> is <strong>de grootste uitwijking uit de "
                  "evenwichtsstand</strong>. De frequentie is het aantal trillingen per seconde, in hertz, en "
                  "de periode de tijd van één trilling."),
            ("kader", "De formules: <strong>f = 1 / T</strong> en <strong>v = λ · f</strong>, en dus ook "
                      "v = λ / T."),
            ("p", "Heeft een trilling <strong>een periode van 0,004 s, dan is de frequentie 250 Hz</strong>: "
                  "één gedeeld door 0,004. Heeft een golf <strong>een golflengte van 2 m en een frequentie van "
                  "170 Hz, dan is de golfsnelheid 340 m/s</strong>: 2 maal 170, precies de snelheid van geluid "
                  "in lucht."),
            ("p", "<strong>Hoe hoger de frequentie van een geluidsgolf, hoe hoger de toon die je hoort.</strong> "
                  "<strong>Draai je de muziek luider, dan verandert de amplitude</strong>, niet de frequentie."),
        ]),
        dict(kop="Geluidssnelheid, breking, buiging en weerkaatsing", blokken=[
            ("p", "<strong>Geluid gaat het snelst in een vaste stof</strong>, daarna in een vloeistof, dan in "
                  "een gas, en in het vacuüm helemaal niet. "
                  "<strong>Geluid plant zich ook sneller voort in warme lucht dan in koude lucht.</strong>"),
            ("p", "<strong>Een regenboog ontstaat doordat licht in een waterdruppel van richting "
                  "verandert</strong>, en die eigenschap van golven heet <strong>breking</strong>. Breking "
                  "gebeurt doordat de golfsnelheid verandert bij de overgang naar een andere middenstof; bij "
                  "geluid gebeurt dat tussen luchtlagen van verschillende temperatuur."),
            ("p", "<strong>Een golf buigt sterk af rond een opening als de opening even klein is als de "
                  "golflengte.</strong> Daarom hoor je iemand achter een hoek wel, maar zie je die niet: "
                  "geluidsgolven zijn veel langer dan lichtgolven."),
            ("p", "<strong>Twee</strong> materialen slorpen geluid op in plaats van het terug te kaatsen: "
                  "<strong>een dik gordijn</strong> en <strong>een zachte tapijtvloer</strong>. "
                  "<strong>Een zacht materiaal kaatst geluid dus niet beter terug dan een hard materiaal</strong>, "
                  "maar juist slechter: hard en glad weerkaatst."),
            ("p", "Het geluid dat je <strong>na de weerkaatsing tegen een verre muur opnieuw hoort</strong>, is "
                  "een <strong>echo</strong>. <strong>Twee</strong> toepassingen gebruiken die weerkaatsing: "
                  "<strong>sonar op een schip</strong> en <strong>echolocatie bij een vleermuis</strong>."),
        ]),
        dict(kop="De decibelschaal en je gehoor", blokken=[
            ("p", "De eenheid van het geluidsniveau is de <strong>decibel</strong>. De "
                  "<strong>gehoordrempel</strong> van een mens ligt bij <strong>0 dB</strong>, "
                  "<strong>vanaf 80 dB is gehoorbescherming nodig</strong> (de gevaargrens), en de "
                  "<strong>pijndrempel</strong> ligt rond <strong>120 dB</strong>."),
            ("p", "<strong>Hoe langer je in lawaai staat, hoe groter de kans op gehoorschade.</strong> Wat er "
                  "beschadigt, zijn <strong>de haarcellen in het binnenoor</strong>, en die groeien bij de mens "
                  "niet terug: <strong>gehoorschade door lawaai geneest dus niet altijd volledig</strong>."),
            ("p", "<strong>Ga je twee keer zo ver van een geluidsbron staan, dan daalt het geluidsniveau met "
                  "6 dB.</strong> <strong>Wordt de geluidsintensiteit twee keer zo groot, dan stijgt het niveau "
                  "met 3 dB.</strong> Een vier keer kleinere intensiteit geeft dus zes decibel minder."),
            ("p", "Op een fuif bescherm je je gehoor op <strong>twee</strong> manieren: "
                  "<strong>oordopjes dragen</strong> en <strong>verder van de boxen gaan staan</strong>."),
            ("p", "<strong>Resonantie</strong> is dat <strong>een voorwerp meetrilt op zijn eigen "
                  "frequentie</strong>. Komt de frequentie van buiten overeen met die eigenfrequentie, dan wordt "
                  "de trilling steeds groter."),
            ("p", "Een mens hoort normaal <strong>van 20 Hz tot 20 000 Hz</strong>. Geluid "
                  "<strong>met een frequentie boven 20 000 Hz, dat de mens niet meer hoort</strong>, is "
                  "<strong>ultrasoon</strong> geluid of ultrageluid; onder twintig hertz is het infrasoon."),
        ]),
        dict(kop="Het elektromagnetisch spectrum", blokken=[
            ("p", "Voor een <strong>elektromagnetische golf in het vacuüm</strong> geldt dat "
                  "<strong>ze met de lichtsnelheid beweegt</strong>, ongeveer 300 000 kilometer per seconde. In "
                  "glas of water gaat ze trager."),
            ("fig", tabel(["Straling", "Energie", "Ioniserend?"], [
                ["Radiogolven", "laagst, langste golven", "nee"],
                ["Microgolven", "laag", "nee"],
                ["Infraroodstraling", "laag", "nee"],
                ["Zichtbaar licht", "midden", "nee"],
                ["Ultraviolette straling", "hoog", "de hoogenergetische wel"],
                ["Röntgenstraling", "hoger", "ja"],
                ["Gammastraling", "hoogst, kortste golven", "ja"],
            ]), "Het spectrum van laag naar hoog."),
            ("p", "<strong>Gammastraling heeft de hoogste energie</strong>, radiogolven de laagste. "
                  "<strong>Radiogolven hebben dus een grotere golflengte dan röntgenstraling</strong>: "
                  "golflengte en frequentie gaan omgekeerd samen."),
            ("p", "<strong>Twee</strong> soorten straling uit de reeks zijn ioniserend: "
                  "<strong>röntgenstraling</strong> en <strong>gammastraling</strong>. "
                  "<strong>Infraroodstraling is geen ioniserende straling</strong>: je voelt ze gewoon als "
                  "warmte."),
            ("p", "<strong>Twee</strong> van de genoemde toestellen werken met infraroodstraling: "
                  "<strong>een afstandsbediening</strong> en <strong>een warmtelamp</strong>. Een microgolfoven "
                  "werkt met microgolven, een bagagescanner met röntgenstraling."),
            ("p", "<strong>Tegen röntgenstraling bij een medisch onderzoek bescherm je je met een "
                  "loodschort.</strong> Tegen uv helpen kleding, zonnebril en zonnecrème."),
        ]),
    ],
    onthoud=[
        "Een golf vervoert energie, geen materie.",
        "Mechanisch heeft een middenstof nodig, elektromagnetisch niet.",
        "Transversaal trilt dwars, longitudinaal mee; geluid is longitudinaal.",
        "f = 1/T en v = λ · f.",
        "Frequentie geeft de toonhoogte, amplitude de sterkte.",
        "0 dB gehoordrempel, 80 dB gevaargrens, 120 dB pijndrempel.",
        "Afstand verdubbelen is −6 dB; intensiteit verdubbelen is +3 dB.",
        "Van radio naar gamma stijgt de energie; röntgen en gamma zijn ioniserend.",
    ],
)

# ───────────────────────── 13. Kernfysica, kernenergie en straling
BUNDELS["kernfysica-kernenergie-en-straling-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Kernfysica, kernenergie en straling",
    onder="Nucliden en isotopen, de halfwaardetijd, fusie en splijting, en wat straling met een mens doet.",
    secties=[
        dict(kop="De atoomkern in getallen", blokken=[
            ("p", "Het <strong>massagetal</strong> van een kern geeft <strong>het aantal protonen plus "
                  "neutronen</strong> aan. <strong>Twee</strong> soorten deeltjes zijn "
                  "<strong>nucleonen</strong>: <strong>protonen</strong> en <strong>neutronen</strong>. Het "
                  "atoomnummer telt alleen de protonen."),
            ("p", "Heeft <strong>koolstof-14 massagetal 14 en atoomnummer 6, dan zitten er 8 neutronen</strong> "
                  "in die kern: 14 min 6."),
            ("p", "Kernen van hetzelfde element <strong>met een verschillend aantal neutronen</strong> heten "
                  "<strong>isotopen</strong>; één zo'n kern is een isotoop. <strong>Twee isotopen van hetzelfde element hebben hetzelfde "
                  "aantal protonen</strong>, want dat bepaalt om welk element het gaat."),
            ("p", "Op de nuclidenkaart zie je welke kernen stabiel zijn. "
                  "<strong>Een lichte kern met minder dan twintig protonen is stabiel als er ongeveer evenveel "
                  "neutronen als protonen zijn.</strong> Een "
                  "<strong>zware kern met meer dan twintig protonen heeft meer neutronen dan protonen "
                  "nodig</strong> om stabiel te zijn, want de protonen stoten elkaar af."),
        ]),
        dict(kop="Halfwaardetijd", blokken=[
            ("p", "De <strong>halfwaardetijd</strong> van een radioactieve stof is <strong>de tijd waarin de "
                  "helft van de kernen vervalt</strong>. Na één halfwaardetijd is de helft over, na twee een "
                  "vierde, na drie een achtste."),
            ("p", "Heeft <strong>een stof een halfwaardetijd van 8 dagen, dan is er na 24 dagen een achtste "
                  "over</strong>, want dat zijn drie halfwaardetijden. "
                  "<strong>Na één halfwaardetijd is dus niet alle straling van een stof verdwenen</strong>: de "
                  "andere helft straalt verder."),
            ("p", "<strong>Hoe langer de halfwaardetijd van een stof, hoe lánger ze blijft stralen</strong>, en "
                  "dus niet hoe sneller ze onschadelijk is. Juist daarom is langlevend afval zo lastig."),
        ]),
        dict(kop="Fusie, splijting en de kerncentrale", blokken=[
            ("p", "<strong>Het verschil tussen kernfusie en kernsplijting is dat bij fusie kernen samensmelten "
                  "en bij splijting breken.</strong> Bij <strong>twee</strong> soorten reacties komt er energie "
                  "vrij: <strong>het samensmelten van lichte kernen</strong> en "
                  "<strong>het splijten van zware kernen</strong>. <strong>Die energie komt uit het "
                  "massaverlies van de kernen</strong>: na de reactie is er een beetje massa verdwenen, en de "
                  "formule van Einstein, E is m maal c in het kwadraat, zegt hoeveel energie dat oplevert."),
            ("p", "In een Belgische kerncentrale wordt <strong>uranium</strong> gespleten. De "
                  "<strong>regelstaven</strong> in de kernreactor dienen om <strong>de kettingreactie af te remmen of stil te "
                  "leggen</strong>: ze slorpen neutronen op. <strong>Twee</strong> onderdelen zijn er voor de "
                  "veiligheid: <strong>de regelstaven</strong> en <strong>de betonnen koepel</strong>."),
            ("p", "<strong>De kernreactie drijft de generator niet rechtstreeks aan.</strong> "
                  "Zo wordt de warmte van de kernreactor elektriciteit: <strong>de warmte maakt stoom, de stoom draait een turbine en die draait een "
                  "generator</strong>: een kerncentrale is in dat opzicht een stoomcentrale met een andere "
                  "warmtebron."),
        ]),
        dict(kop="Radioactief afval", blokken=[
            ("p", "Het afval wordt ingedeeld naar hoe sterk het straalt en hoe lang. "
                  "<strong>Bij categorie A hoort kortlevend laag- en middelactief afval</strong>, dat in België "
                  "aan de oppervlakte geborgen wordt in Dessel. Categorie B is langlevend laag- en middelactief "
                  "afval, en <strong>hoogactief radioactief afval hoort bij categorie C</strong>. Voor B en C "
                  "wordt berging diep in de kleilaag voorbereid."),
        ]),
        dict(kop="Alfa, bèta en gamma", blokken=[
            ("p", "<strong>Alfastraling</strong> is <strong>een heliumkern die de kern verlaat</strong>: twee "
                  "protonen en twee neutronen. <strong>Bètamin-straling</strong> is "
                  "<strong>een elektron dat de kern verlaat</strong>. <strong>Gammastraling</strong> is "
                  "<strong>elektromagnetische straling met heel hoge energie</strong>. "
                  "<strong>Twee</strong> soorten bestaan dus uit deeltjes en niet uit een golf: "
                  "<strong>alfastraling</strong> en <strong>bètastraling</strong>."),
            ("fig", tabel(["Straling", "Ioniserend vermogen", "Tegengehouden door"], [
                ["Alfa", "het grootst", "een blad papier"],
                ["Bèta", "middelmatig", "een plaatje aluminium"],
                ["Gamma", "het kleinst, maar dringt diep door", "een dikke laag lood of beton"],
            ]), "De drie soorten straling naast elkaar."),
            ("p", "<strong>Alfastraling wordt al door een blad papier tegengehouden</strong> en heeft "
                  "<strong>het grootste ioniserend vermogen van de drie soorten</strong>: ze geeft al haar "
                  "energie over een korte afstand af. <strong>Gammastraling houd je tegen met twee dingen</strong>: "
                  "<strong>een dikke laag lood</strong> of <strong>een dikke betonnen wand</strong>."),
            ("p", "Straling <strong>die elektronen uit atomen kan losmaken</strong>, heet "
                  "<strong>ioniserende straling</strong>; dat losmaken zelf heet ionisatie. Daardoor raken moleculen beschadigd, ook het DNA."),
            ("p", "Welke straling een kern uitzendt, lees je van de nuclidenkaart af. "
                  "<strong>Een kern met te veel neutronen om stabiel te zijn, zendt bètamin-straling uit</strong>: "
                  "een neutron wordt dan een proton. Daarom geldt: "
                  "<strong>vervalt koolstof-14 via bètamin-straling, dan stijgt het atoomnummer met één en "
                  "blijft het massagetal gelijk</strong>, en wordt het stikstof-14. Bij alfaverval gaat er meer "
                  "weg: <strong>zendt uranium-238 een alfadeeltje uit, dan blijft een kern over met massagetal "
                  "234 en atoomnummer 90</strong>, dus thorium-234."),
        ]),
        dict(kop="Straling en de mens", blokken=[
            ("p", "<strong>Het verschil tussen bestraling en besmetting is dat bij besmetting de stof op of in "
                  "je lichaam zit.</strong> <strong>Bij bestraling komt de radioactieve stof dus niet in je "
                  "lichaam terecht</strong>: alleen de straling bereikt je, en het stopt zodra je weggaat. Van "
                  "een <strong>inwendige besmetting</strong> spreek je <strong>als je de radioactieve stof "
                  "inademt of inslikt</strong>; op de huid is het uitwendig."),
            ("p", "Je beschermt je tegen ioniserende straling op <strong>twee</strong> manieren uit de reeks: "
                  "<strong>verder van de bron gaan staan</strong> en "
                  "<strong>een laag lood tussen jou en de bron zetten</strong>. Afstand, afscherming en tijd "
                  "zijn samen de drie manieren. <strong>Jodiumpillen dienen bij een kernongeval om je "
                  "schildklier te vullen met gewoon jodium</strong>, zodat ze het radioactieve jodium niet meer "
                  "opneemt."),
            ("p", "De eenheid van de <strong>geabsorbeerde stralingsdosis</strong> is de <strong>gray</strong>: "
                  "hoeveel energie het weefsel per kilogram opneemt. De eenheid van de <strong>effectieve dosis</strong> staat "
                  "in <strong>sievert</strong>, net als de equivalente dosis, en die houden rekening met de "
                  "soort straling en met het weefsel. <strong>Alfastraling krijgt een hogere "
                  "stralingsweegfactor dan gammastraling</strong>, twintig tegen één, omdat ze bij dezelfde "
                  "opgenomen energie veel meer schade aanricht. De weefselweegfactor doet hetzelfde voor het "
                  "orgaan dat geraakt wordt."),
        ]),
    ],
    onthoud=[
        "Massagetal = protonen + neutronen; atoomnummer = protonen.",
        "Isotopen hebben hetzelfde aantal protonen, een ander aantal neutronen.",
        "Na n halfwaardetijden is er (1/2) tot de n-de over.",
        "Fusie van lichte en splijting van zware kernen leveren energie, uit massaverlies.",
        "Warmte maakt stoom, stoom draait de turbine en de generator.",
        "Categorie A is kortlevend laag- en middelactief, C is hoogactief.",
        "Alfa stopt op papier maar ioniseert het sterkst; gamma dringt diep door.",
        "Bestraling blijft buiten, besmetting zit op of in je lichaam.",
        "Dosis in gray, equivalente en effectieve dosis in sievert.",
    ],
)

# ───────────────────────── 14. Veilig werken, meten en onderzoeken
BUNDELS["veilig-werken-meten-en-onderzoeken-beyond-dubbele-finaliteit"] = dict(
    vak=VAK, niveau=DF, titel="Veilig werken, meten en onderzoeken",
    onder="P- en H-zinnen, meetinstrumenten en meetbereik, eenheden en voorvoegsels, en de stappen van een onderzoek.",
    secties=[
        dict(kop="Veilig en duurzaam werken", blokken=[
            ("p", "In een <strong>H-zin</strong> op een etiket staat <strong>waarom de stof gevaarlijk "
                  "is</strong>; de H staat voor hazard. In een <strong>P-zin</strong> staat "
                  "<strong>welke voorzorgen je moet nemen</strong>. "
                  "<strong>Een H-zin vertelt je dus niet welke voorzorgsmaatregelen je moet nemen</strong>, dat "
                  "doet de P-zin."),
            ("p", "<strong>Twee</strong> van de genoemde werkwijzen horen bij veilig en duurzaam werken: "
                  "<strong>een gemorst product onmiddellijk opkuisen</strong> en "
                  "<strong>glaswerk na gebruik schoonmaken en wegzetten</strong>. "
                  "<strong>Je kuist een gemorst product onmiddellijk op</strong>, want wie later langskomt weet "
                  "niet wat er ligt."),
            ("p", "<strong>Je bedient een elektrisch toestel nooit met natte handen, omdat water de stroom "
                  "geleidt en je een schok kan krijgen.</strong> En "
                  "<strong>glasscherven ruim je veilig op met een borstel en een blad, in een harde "
                  "doos</strong>, nooit met je blote handen."),
            ("p", "<strong>Hygiënisch omgaan met biologisch materiaal hoort bij veilig werken</strong>, want "
                  "daar kunnen micro-organismen in zitten."),
            ("p", "Bij een bunsenbrander neem je <strong>twee</strong> voorzorgen uit de reeks: "
                  "<strong>lange haren vastbinden</strong> en "
                  "<strong>losse kledij en mouwen wegsteken</strong>. Je doet de brander uit met de gaskraan, "
                  "niet met je hand, en de ondergrond is hittebestendig."),
            ("p", "<strong>Je zet een meetinstrument uit als je even niet meet, om energie te sparen en het "
                  "toestel te sparen.</strong> En <strong>je gebruikt zo weinig chemische stoffen als mogelijk, "
                  "want minder verbruik geeft minder afval en minder risico</strong>."),
            ("p", "Met de <strong>restproducten van een proef</strong> doe je dit: "
                  "<strong>sorteren volgens de aanwijzingen op het etiket</strong>, vaak bij het klein "
                  "gevaarlijk afval."),
        ]),
        dict(kop="Meten met het juiste toestel", blokken=[
            ("p", "Het <strong>meetbereik</strong> is <strong>het gebied tussen de kleinste en de grootste "
                  "waarde die een meettoestel kan meten</strong>. "
                  "<strong>Je mag een meetinstrument niet boven zijn meetbereik gebruiken, ook niet als je "
                  "voorzichtig doet</strong>: de waarde is dan niet betrouwbaar en het toestel raakt beschadigd."),
            ("p", "Meet <strong>je balans tot 500 g en moet je 2 kg wegen, dan zoek je een balans met een "
                  "groter meetbereik</strong>. Wil je <strong>een temperatuurverschil van een halve graad meten, "
                  "dan kies je een thermometer met streepjes van 0,1 °C</strong>: je toestel moet nauwkeuriger "
                  "zijn dan het verschil dat je wil zien."),
            ("p", "<strong>Voor je een massa op een digitale balans afleest, zet je de balans met het leeg "
                  "recipiënt op nul.</strong> Zo weeg je alleen de stof. "
                  "<strong>Je leest een maatbeker af op ooghoogte, aan de onderkant van de "
                  "meniscus.</strong>"),
            ("fig", tabel(["Grootheid", "Toestel"], [
                ["Massa", "een balans"],
                ["Tijd", "een chronometer"],
                ["Temperatuur", "een thermometer"],
                ["Druk", "een manometer"],
                ["Spanning en stroom", "een multimeter"],
                ["Geluidsniveau", "een decibelmeter"],
            ]), "Welk toestel bij welke grootheid hoort."),
            ("p", "<strong>Hoe lang een proef duurt, meet je met een chronometer.</strong> De "
                  "<strong>massa van een stof meet je met een balans</strong> of weegschaal."),
        ]),
        dict(kop="Grootheden, eenheden en voorvoegsels", blokken=[
            ("p", "Elke grootheid heeft haar eigen eenheid. Energie meet je in "
                  "<strong>joule (J)</strong>: <strong>2 MJ is 2 000 000 joule</strong>, want mega betekent een "
                  "miljoen keer."),
            ("p", "De <strong>SI-eenheid van massa is de kilogram</strong>. "
                  "<strong>Twee</strong> van de genoemde eenheden zijn SI-basiseenheden: "
                  "<strong>de meter</strong> en <strong>de seconde</strong>. De liter en de graad Celsius zijn "
                  "dat niet; de kelvin en de ampère wel."),
            ("fig", tabel(["Voorvoegsel", "Betekent", "Voorbeeld"], [
                ["mega (M)", "een miljoen keer", "2 MJ is 2 000 000 J"],
                ["kilo (k)", "duizend keer", "2,5 km is 2500 m"],
                ["milli (m)", "een duizendste", "500 mg is 0,5 g"],
                ["micro (µ)", "een miljoenste", "1 µm is 0,000001 m"],
                ["nano (n)", "een miljardste", "1 nm is 0,000000001 m"],
            ]), "De voorvoegsels van mega tot nano."),
            ("p", "<strong>2,5 km is 2500 m</strong>, want <strong>kilo</strong> is het voorvoegsel voor "
                  "<strong>duizend keer een eenheid</strong>. <strong>500 mg is 0,5 g</strong>, want "
                  "<strong>het voorvoegsel milli betekent een duizendste van de eenheid</strong>. "
                  "<strong>Micro betekent een miljoenste</strong>, en <strong>2 MJ is 2 000 000 J</strong>."),
            ("p", "Twee grootheden zijn <strong>recht evenredig</strong> als geldt: "
                  "<strong>verdubbelt de ene, dan verdubbelt de andere</strong>. In een grafiek is dat een "
                  "rechte, en <strong>bij een recht evenredig verband gaat die rechte door de oorsprong</strong>. "
                  "Twee grootheden zijn <strong>omgekeerd evenredig</strong> als "
                  "<strong>de andere halveert wanneer de ene verdubbelt</strong>; dan blijft hun product gelijk."),
        ]),
        dict(kop="De stappen van een onderzoek", blokken=[
            ("p", "Een onderzoek begint bij een probleemstelling en een onderzoeksvraag. "
                  "<strong>Een goede onderzoeksvraag is scherp afgebakend</strong> en "
                  "<strong>je kan ze met metingen beantwoorden</strong>: twee eisen samen. Een vraag als is "
                  "water gezond, kan je met geen enkele proef beantwoorden."),
            ("p", "Een <strong>hypothese</strong> is <strong>een verwachting die je met je proef kan "
                  "testen</strong>. Ze mag fout blijken, en dat is geen probleem: "
                  "<strong>een onderzoek waarvan de uitkomst je hypothese tegenspreekt, is niet "
                  "mislukt</strong>. Je hebt dan geleerd dat je verwachting fout was."),
            ("p", "<strong>Twee</strong> van de genoemde stappen horen bij wetenschappelijk onderzoek: "
                  "<strong>een hypothese formuleren</strong> en <strong>data verzamelen en analyseren</strong>. "
                  "Het besluit vooraf vastleggen hoort er niet bij, en "
                  "<strong>passen je metingen niet bij je hypothese, dan pas je de metingen niet aan</strong>: "
                  "de metingen zijn wat ze zijn."),
            ("p", "<strong>Je verandert in een proef maar één factor tegelijk, anders weet je niet wat het "
                  "verschil veroorzaakt.</strong> Al de rest houd je gelijk."),
            ("p", "Het besluit <strong>dat je aan het einde van een onderzoek uit je gegevens haalt</strong>, is "
                  "de <strong>conclusie</strong>: het antwoord op je onderzoeksvraag. Daarna kijk je terug op je "
                  "methode en vertel je wat je vond."),
        ]),
        dict(kop="Ontwerpen en STEM", blokken=[
            ("p", "Bij het ontwerpen van een oplossing definieer je eerst het probleem. "
                  "<strong>De volgende stap is criteria opstellen waaraan de oplossing moet voldoen.</strong> "
                  "Daarna splits je het probleem indien nodig in deelproblemen, bedenk je oplossingen, en "
                  "evalueer en stuur je bij."),
            ("p", "<strong>Voor een vaccin was kennis nodig van de werking van het virus, van de koeling en van "
                  "de verspreidingscijfers.</strong> Dat toont dat "
                  "<strong>de STEM-domeinen samenwerken aan één probleem</strong>: wetenschap, technologie, "
                  "engineering en wiskunde leveren elk een stuk van de oplossing. Grote maatschappelijke vragen "
                  "zijn bijna nooit van één vak alleen, en omgekeerd maakt een nieuwe techniek nieuw onderzoek "
                  "mogelijk."),
        ]),
    ],
    onthoud=[
        "H-zin: waarom gevaarlijk. P-zin: wat je moet doen.",
        "Opkuisen, opruimen, droge handen, haren vast: dat is veilig werken.",
        "Blijf binnen het meetbereik en kies een toestel dat nauwkeurig genoeg is.",
        "Zet een balans op nul met het leeg recipiënt; lees een maatbeker op ooghoogte af.",
        "kilo is duizend keer, milli een duizendste, micro een miljoenste, mega een miljoen.",
        "Recht evenredig: een rechte door de oorsprong. Omgekeerd evenredig: het product blijft gelijk.",
        "Een hypothese mag fout blijken; metingen pas je nooit aan.",
        "Verander één factor tegelijk en houd de rest gelijk.",
    ],
)

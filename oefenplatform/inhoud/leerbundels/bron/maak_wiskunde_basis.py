# -*- coding: utf-8 -*-
"""De leerbundels voor wiskunde basis op 🚀 Boost doorstroom.

Gebaseerd op de vakfiche wiskunde basis 2DO, geldig vanaf 1 januari 2027. Dit
is het vak voor de richtingen die géén wiskunde gevorderd volgen; de stof
overlapt dus deels met [[maak_wiskunde_boost.py]], maar de bundels staan apart
omdat het een ander vak is met eigen vragen.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde hoofdstuk
behandelen dezelfde stof met andere vragen. Kim laadt de bundel dus twee keer
op, één keer bij elk deel.

Elk getalvoorbeeld dat hier beweerd wordt, staat ook in controleer.py, waar het
uitgerekend wordt in plaats van uitgeschreven. Zet je hier een voorbeeld bij,
zet het daar dan ook bij.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel
import svg

VAK = "Wiskunde basis"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}


def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BOOST)
    BUNDELS[slug + "-boost-doorstroom"] = b


# ───────────────────────── 1. De reële getallen, wortels en machten
zet("de-reele-getallen-wortels-en-machten",
    titel="De reële getallen, wortels en machten",
    onder="De getallenverzamelingen en hun decimale vormen, de wetenschappelijke notatie, rekenen met wortels en machten, en de drie bewerkingseigenschappen.",
    secties=[
        dict(kop="De getallenverzamelingen", blokken=[
            ("p", "De verzamelingen zitten in elkaar als Russische poppetjes: elke kleinere zit volledig in "
                  "de grotere. <strong>Het getal 7 is dus tegelijk natuurlijk, geheel, rationaal én "
                  "reëel.</strong>"),
            ("kader", tabel(["verzameling", "teken", "wat erbij komt", "voorbeelden"],
                            [["de natuurlijke getallen", "ℕ", "de telgetallen", "0, 1, 2, 7"],
                             ["<strong>de gehele getallen</strong>", "ℤ", "<strong>de negatieve getallen</strong>; <strong>alle natuurlijke getallen zitten erin</strong>",
                              "<strong>min 5</strong>, min 1, 0, 7"],
                             ["<strong>de rationale getallen</strong>", "ℚ", "alles wat je <strong>als breuk van twee gehele getallen</strong> kan schrijven",
                              "<strong>0,75</strong>, <strong>min twee derde</strong>, <strong>4</strong>, 3/4"],
                             ["<strong>de reële getallen</strong>", "ℝ", "ook <strong>de irrationale</strong>: wat géén breuk is",
                              "<strong>de wortel van 2</strong>, <strong>pi</strong>, <strong>de wortel van 3</strong>"]])),
            ("p", "<strong>Niet elk reëel getal is dus rationaal</strong>; het is net omgekeerd: de reële "
                  "getallen omvatten de rationale én de irrationale. <strong>De reële getallen zijn nodig om "
                  "de getallenas vol te maken</strong>: tussen de breuken zitten gaten, want de wortel van 2 "
                  "en pi liggen wel op de as maar zijn geen breuk. <strong>De wortel van 2 staat niet bij de "
                  "rationale getallen omdat ze geen breuk is</strong> — men kan bewijzen dat geen enkele "
                  "breuk haar precies gelijk is."),
        ]),
        dict(kop="De decimale vorm verraadt de soort", blokken=[
            ("kader", tabel(["decimale vorm", "wat ze betekent", "voorbeeld"],
                            [["<strong>begrensd</strong> (eindig)", "na enkele cijfers stopt ze", "<strong>0,25</strong>"],
                             ["<strong>onbegrensd repeterend</strong>", "de cijfers stoppen niet maar herhalen een patroon",
                              "<strong>een derde</strong> = 0,333…"],
                             ["<strong>onbegrensd niet-repeterend</strong>", "de cijfers stoppen nooit en herhalen nooit — <strong>dan is het getal irrationaal</strong>",
                              "<strong>pi</strong>"]])),
            ("p", "De vakfiche noemt vier <strong>vormen</strong> van een getal: de <strong>decimale "
                  "vorm</strong>, de <strong>wortelvorm</strong>, de <strong>breuk en het procent</strong>. "
                  "Een lettervorm is geen getalvorm. Omzetten van de ene vorm naar de andere "
                  "<strong>mag met ICT</strong>; de vakfiche vraagt dat zelfs uitdrukkelijk."),
            ("p", "Van breuk naar procent deel je gewoon uit. <strong>Drie vijfde is 0,6, dus 60 "
                  "procent.</strong> En omgekeerd werkt een procent als een kommagetal: <strong>12 procent "
                  "van 250 is 0,12 × 250 = 30</strong>."),
        ]),
        dict(kop="De wetenschappelijke notatie", blokken=[
            ("p", "Een getal in wetenschappelijke notatie is een getal <strong>tussen 1 en 10</strong>, maal "
                  "een macht van tien. <strong>Voor de macht mag dus niet elk getal staan</strong>: 45 × 10³ "
                  "is niet correct genoteerd, want 45 ligt niet tussen 1 en 10."),
            ("kader", tabel(["getal", "wetenschappelijke notatie", "waarom"],
                            [["<strong>45 000</strong>", "<strong>4,5 × 10⁴</strong>", "4,5 maal 10 000 is 45 000"],
                             ["<strong>0,003</strong>", "<strong>3 × 10⁻³</strong>", "een getal kleiner dan 1 krijgt een <strong>negatieve</strong> exponent"]])),
        ]),
        dict(kop="Wortels", blokken=[
            ("p", "De vierkantswortel vraagt welk getal maal zichzelf je getal geeft; de derdemachtswortel "
                  "welk getal drie keer maal zichzelf. <strong>De wortel van 81 is 9</strong> (9 × 9 = 81), "
                  "<strong>de derdemachtswortel van 27 is 3</strong> en <strong>de derdemachtswortel van 64 "
                  "is 4</strong>."),
            ("p", "<strong>Je vereenvoudigt een wortel door er een kwadraat uit te halen.</strong> "
                  "<strong>De wortel van 50 is 5 maal de wortel van 2</strong>, want 50 = 25 × 2 en de "
                  "wortel van 25 is 5. Net zo is <strong>de wortel van 8 gelijk aan 2 maal de wortel van "
                  "2</strong>, want 8 = 4 × 2."),
            ("kader", tabel(["regel", "wat ze zegt", "voorbeeld"],
                            [["wortels vermenigvuldigen", "de wortel van een product is het product van de wortels",
                              "<strong>de wortel van 3 maal de wortel van 12</strong> is de wortel van 36, dus <strong>6</strong>"],
                             ["gelijke wortelvormen optellen", "je telt ze op als gelijke termen",
                              "<strong>de wortel van 2 plus 3 maal de wortel van 2 is 4 maal de wortel van 2</strong>"],
                             ["<strong>de noemer wortelvrij maken</strong>", "<strong>vermenigvuldig boven en onder met die wortel</strong>",
                              "1 gedeeld door de wortel van 3 wordt de wortel van 3 gedeeld door 3"]])),
            ("p", "En één valstrik: <strong>de wortel van een som is níét de som van de wortels</strong>. "
                  "Het tegenvoorbeeld staat klaar: de wortel van 9 + 16 is de wortel van 25, dus 5, terwijl "
                  "3 + 4 gelijk is aan 7."),
        ]),
        dict(kop="Machten", blokken=[
            ("kader", tabel(["regel", "voorbeeld"],
                            [["bij een product tel je de exponenten op", "<strong>2³ × 2² = 2⁵ = 32</strong>; in lettervorm <strong>a³ × a⁵ = a⁸</strong>"],
                             ["bij een quotiënt trek je ze af", "<strong>2⁶ gedeeld door 2 is 2⁵</strong>; <strong>3⁴ gedeeld door 3² is 3² = 9</strong>"],
                             ["<strong>een negatieve exponent</strong> is één gedeeld door de macht", "<strong>10⁻² = 0,01</strong>"],
                             ["<strong>een macht nul is altijd 1</strong>", "zolang het grondtal niet nul is; het volgt uit de aftrekregel"],
                             ["een <strong>oneven</strong> exponent houdt het minteken", "<strong>(min 2)³ = min 8</strong>"],
                             ["een <strong>even</strong> exponent maakt het positief", "<strong>(min 3)² = 9</strong>, dus niet min 9 — let op de haakjes"]])),
            ("p", "Let op het verschil tussen een macht en een vermenigvuldiging: 2 × 5 is gewoon 10, en dat "
                  "is iets heel anders dan 2⁵."),
        ]),
        dict(kop="De bewerkingseigenschappen", blokken=[
            ("p", "De vakfiche noemt er <strong>drie</strong>, elk in woorden en in symbolen."),
            ("kader", tabel(["eigenschap", "wat ze zegt", "voorbeeld"],
                            [["<strong>de commutativiteit</strong> (de wisseleigenschap)", "<strong>de orde van twee factoren maakt niet uit</strong>",
                              "3 × 5 = 5 × 3"],
                             ["<strong>de associativiteit</strong>", "de manier van groeperen maakt niet uit",
                              "(2 + 3) + 4 = 2 + (3 + 4)"],
                             ["<strong>de distributiviteit</strong>", "je verdeelt een factor over elke term, of je haalt hem er juist buiten",
                              "<strong>3 × 7 + 3 × 3 = 3 × 10</strong>: de gemeenschappelijke factor 3 buiten haakjes"]])),
            ("weetje", "<strong>Werk zo lang mogelijk exact</strong>, want <strong>afronden onderweg "
                       "vervalst je resultaat</strong>. De vakfiche zegt het letterlijk: hoe onnauwkeuriger "
                       "je tussenresultaten, hoe meer je eindresultaat afwijkt."),
        ]),
    ])


# ───────────────────────── 2. Getallen ordenen, afronden en intervallen
zet("getallen-ordenen-afronden-en-intervallen",
    titel="Getallen ordenen, afronden en intervallen",
    onder="De ongelijkheidstekens en de getallenas, de afrondregel, en de drie soorten intervallen met hun notatie.",
    secties=[
        dict(kop="Ordenen op de getallenas", blokken=[
            ("p", "Over de getallenas klopt: <strong>rechts is groter</strong>, <strong>elk reëel getal "
                  "heeft er een plaats</strong> en <strong>ze loopt in beide richtingen door</strong>. Dat "
                  "eerste punt beslist alles: <strong>hoe verder naar links, hoe kleiner</strong>."),
            ("p", "Bij negatieve getallen keert je gevoel dus om. <strong>Min 10 is kleiner dan min "
                  "3</strong>, en <strong>min 0,5 is groter dan min 1,5</strong>. In een rij als min 5, min "
                  "2, min 0,5 is <strong>min 5 het kleinste</strong>: bij negatieve getallen is het getal "
                  "met de grootste cijferwaarde net het kleinste. Van klein naar groot staat dus: "
                  "<strong>min 2, min 0,5, 0, 1,5</strong>."),
            ("kader", tabel(["teken", "wat het betekent", "let op"],
                            [["&lt;", "strikt kleiner dan", "de grens doet niet mee"],
                             ["<strong>&gt;</strong>", "<strong>strikt groter dan</strong>", "het teken <strong>zonder streepje</strong> eronder"],
                             ["≤", "<strong>kleiner dan of gelijk aan</strong>", "<strong>het streepje eronder voegt de gelijkheid toe</strong>: 3 ≤ 3 is waar"],
                             ["≥", "groter dan of gelijk aan", "mét streepje, dus de grens doet mee"]])),
            ("p", "<strong>Vergelijk breuken door ze eerst naar de decimale vorm om te zetten, dan zie je de "
                  "orde meteen</strong>: twee kommagetallen vergelijk je cijfer per cijfer. Van 0,8, 0,75, "
                  "0,7 en twee derde is <strong>0,8 het grootste</strong>. <strong>Twee derde is "
                  "0,6666…</strong>, en daarvan is <strong>0,67</strong> de beste benadering. Let wel: "
                  "afronden maakt het minder exact."),
            ("p", "Nog twee bakens. <strong>Het getal precies tussen 4 en 7 is 5,5</strong>, het gemiddelde "
                  "van de twee. En tussen 1 en 2 liggen onder meer <strong>1,5</strong>, <strong>de wortel "
                  "van 2</strong> (ongeveer 1,41) en <strong>zeven vijfden</strong> (1,4)."),
            ("p", "Een breuk herken je ook terug in een kommagetal: <strong>0,375 is drie achtsten</strong>, "
                  "want 375 duizendsten gedeeld door 125 boven en onder geeft 3/8."),
        ]),
        dict(kop="Afronden", blokken=[
            ("p", "De regel is kort: <strong>je kijkt enkel naar het eerste cijfer dat wegvalt</strong>. "
                  "<strong>Is dat 5 of meer, dan rond je naar boven af</strong>; <strong>is het minder dan "
                  "5, dan naar beneden</strong>. De cijfers daarachter spelen geen rol."),
            ("kader", tabel(["opgave", "antwoord", "waarom"],
                            [["<strong>3,476 op twee cijfers na de komma</strong>", "<strong>3,48</strong>",
                              "het derde cijfer is een 6, dus de 7 gaat naar 8"],
                             ["<strong>12,3449 op één cijfer na de komma</strong>", "<strong>12,3</strong>",
                              "het tweede cijfer is een 4, dus naar beneden; dat de cijfers erna groter zijn, doet niet mee"],
                             ["<strong>1 999 op honderdtallen</strong>", "<strong>2 000</strong>",
                              "het tientalcijfer is 9, dus 19 honderdtallen worden er 20"]])),
            ("p", "<strong>Altijd naar boven afronden zou de resultaten systematisch te groot maken.</strong> "
                  "Een winkel die elke prijs naar boven afrondt op 5 cent, komt dus telkens iets te hoog uit, "
                  "en daarom bestaat de regel van 5 of meer."),
        ]),
        dict(kop="Intervallen", blokken=[
            ("p", "De vakfiche noemt <strong>drie</strong> soorten. Een <strong>dubbel interval</strong> "
                  "bestaat niet als begrip, en <strong>één enkel getal is geen interval</strong>: een "
                  "interval is een aaneengesloten stuk van de getallenas met twee grenzen."),
            ("kader", tabel(["soort", "de grenzen", "haakjes", "op de getallenas"],
                            [["<strong>open</strong>", "<strong>horen er niet bij</strong>", "<strong>ronde</strong> haakjes", "open bolletjes"],
                             ["<strong>halfopen</strong> (of halfgesloten)", "<strong>één grens hoort erbij, de andere niet</strong>",
                              "één rond en één vierkant", "één open en één vol bolletje"],
                             ["<strong>gesloten</strong>", "<strong>horen erbij</strong>", "vierkante haakjes naar binnen",
                              "<strong>volle bolletjes aan de grenzen</strong>"]])),
            ("p", "<strong>Aan de kant van oneindig staat een interval altijd open</strong>, want oneindig "
                  "is geen getal en kan dus nooit tot de verzameling horen."),
            ("kader", tabel(["ongelijkheid of situatie", "het interval", "waarom"],
                            [["<strong>x &gt; 3</strong>", "<strong>van 3 open tot plus oneindig</strong>", "strikt groter, dus 3 zelf valt erbuiten"],
                             ["<strong>x ≤ 5</strong>", "<strong>van min oneindig tot 5 gesloten</strong>", "het isgelijkteken zit erin, dus 5 hoort erbij"],
                             ["<strong>een temperatuur tussen min 2 en 8 graden, grenzen meegerekend</strong>",
                              "<strong>gesloten van min 2 tot 8</strong>", "grenzen meegerekend is gesloten aan beide zijden"],
                             ["<strong>een korting vanaf 50 euro</strong>", "<strong>gesloten vanaf 50</strong>",
                              "vanaf 50 betekent dat 50 meedoet; <em>vanaf meer dan</em> 50 zou open zijn"]])),
            ("p", "In het gesloten interval van 2 tot 5 horen <strong>2</strong>, <strong>3,5</strong> en "
                  "<strong>5</strong> thuis, maar 5,5 niet. In het open interval van 0 tot 1 horen "
                  "<strong>0,01</strong>, <strong>0,5</strong> en <strong>0,99</strong>, maar 0 en 1 zelf "
                  "niet."),
            ("p", "Daar zit ook het verschil dat het woordje <strong>strikt</strong> maakt: <strong>de grens "
                  "valt weg</strong>. <strong>Bij x strikt groter dan 0 hoort nul dus niet bij de "
                  "oplossingen</strong>; bij groter dan of gelijk aan 0 wel."),
            ("p", "<strong>De oplossingenverzameling van een ongelijkheid mag je als interval "
                  "noteren</strong>, en de vakfiche vraagt ook om ze op een getallenas voor te stellen. Dat "
                  "is handig omdat <strong>een interval de oplossing in één blik toont</strong>: je ziet "
                  "meteen waar ze begint en eindigt, en of de grenzen meedoen."),
        ]),
    ])


# ───────────────────────── 3. Logica: bewerkingen en waarheidstabellen
zet("logica-bewerkingen-en-waarheidstabellen",
    titel="Logica: bewerkingen en waarheidstabellen",
    onder="De vijf logische bewerkingen, de waarheidstabel met haar rijen, tautologie en contradictie, de kwantoren en de logische poorten.",
    secties=[
        dict(kop="Uitspraken en bewerkingen", blokken=[
            ("p", "Een <strong>logische uitspraak</strong> is <strong>een bewering die waar of vals "
                  "is</strong>. Ze heeft precies <strong>twee</strong> mogelijke waarheidswaarden, en een "
                  "derde bestaat in deze logica niet. Een vraag of een bevel is dus geen uitspraak."),
            ("p", "De vakfiche noemt <strong>vijf</strong> bewerkingen: <strong>negatie en "
                  "conjunctie</strong>, <strong>disjunctie</strong>, <strong>implicatie en "
                  "equivalentie</strong>. Substitutie is een methode bij stelsels en geen logische "
                  "bewerking."),
            ("kader", tabel(["bewerking", "het woord", "wanneer ze waar is"],
                            [["<strong>de negatie</strong> (de ontkenning)", "niet",
                              "<strong>ze keert de waarheidswaarde om</strong>: was de uitspraak waar, dan is de negatie vals"],
                             ["<strong>de conjunctie</strong>", "<strong>en</strong>",
                              "<strong>als beide delen waar zijn</strong>; één vals deel maakt het geheel vals"],
                             ["<strong>de disjunctie</strong>", "of",
                              "<strong>als minstens één deel waar is</strong>; <strong>ook als beide waar zijn</strong>"],
                             ["<strong>de implicatie</strong>", "als … dan",
                              "altijd, <strong>behalve als het eerste waar en het tweede vals is</strong>"],
                             ["<strong>de equivalentie</strong>", "dan en slechts dan als",
                              "<strong>als beide delen dezelfde waarde hebben</strong>: twee keer waar of twee keer vals"]])),
            ("p", "<strong>Het of van de logica sluit niet uit dat beide delen waar zijn.</strong> Daar "
                  "verschilt het van het of in de omgangstaal, waar men vaak een keuze bedoelt."),
            ("p", "Bij de implicatie zit nog een valstrik: <strong>een implicatie met een vals eerste deel "
                  "is niet vals maar juist waar</strong>. Als het regent, dan draag ik een jas — regent het "
                  "niet, dan is de belofte niet geschonden. Daar zit meteen het verschil met het als-dan van "
                  "de omgangstaal: <strong>het logische als-dan zegt niets over een oorzaak</strong>."),
            ("p", "Zo zet je een zin om in symbolen: <em>p is waar en q is vals</em> wordt <strong>p en de "
                  "negatie van q</strong>."),
        ]),
        dict(kop="Tautologie en contradictie", blokken=[
            ("p", "Een <strong>tautologie</strong> is <strong>een uitspraak die altijd waar is</strong>: "
                  "bij elke combinatie komt waar uit, dus haar kolom staat vol waar. Een "
                  "<strong>contradictie</strong> is het omgekeerde: <strong>altijd vals</strong>."),
            ("p", "Tautologieën zijn bijvoorbeeld <strong>p of niet p</strong>, <strong>p impliceert "
                  "p</strong> en <strong>p is equivalent met p</strong>. <strong>Dat het regent of niet "
                  "regent, is dus geen contradictie maar een tautologie</strong>; een contradictie zou zijn: "
                  "het regent én het regent niet."),
            ("p", "<strong>Je bewijst een tautologie met een tabel waarin alle rijen waar geven.</strong> "
                  "Eén rij met vals volstaat om haar te weerleggen."),
        ]),
        dict(kop="Nodig en voldoende", blokken=[
            ("kader", tabel(["soort voorwaarde", "wat ze betekent", "voorbeeld"],
                            [["<strong>nodig</strong>", "<strong>zonder haar geldt het besluit niet</strong>",
                              "een cijfer halen is nodig om te slagen, maar niet voldoende"],
                             ["<strong>voldoende</strong>", "<strong>met haar geldt het besluit zeker</strong>",
                              "<strong>deelbaar zijn door 4 is voldoende om even te zijn</strong>, maar niet nodig: 6 is ook even"]])),
            ("p", "<strong>Bij een equivalentie is de voorwaarde zowel nodig als voldoende</strong>: de pijl "
                  "gaat in beide richtingen, en daarom staat de equivalentie voor <em>dan en slechts dan "
                  "als</em>."),
            ("p", "De vakfiche noemt <strong>twee</strong> kwantoren: <strong>voor elke</strong> en "
                  "<strong>er bestaat</strong>. <em>Precies één</em> staat er niet bij. Let op het omkeren: "
                  "<strong>de negatie van <em>elk getal is positief</em> is <em>er bestaat een getal dat niet "
                  "positief is</em></strong>. Niet-voor-elke keert de kwantor om naar er-bestaat."),
        ]),
        dict(kop="De waarheidstabel", blokken=[
            ("p", "Elke extra uitspraak <strong>verdubbelt</strong> het aantal rijen, want elke uitspraak kan "
                  "waar of vals zijn."),
            ("kader", tabel(["aantal uitspraken", "aantal rijen", "rekenwijze"],
                            [["twee", "<strong>vier</strong>", "2 × 2"],
                             ["drie", "<strong>acht</strong>", "2 × 2 × 2"],
                             ["vier", "<strong>16</strong>", "2⁴"]])),
            ("p", "In een tabel met twee uitspraken is <strong>de conjunctie in één rij waar</strong> "
                  "(alleen als beide waar zijn), <strong>de disjunctie in drie rijen</strong> (overal "
                  "behalve waar beide vals zijn) en <strong>de implicatie ook in drie rijen</strong> (ze is "
                  "enkel vals bij waar-dan-vals)."),
            ("p", "Het opstellen gaat in drie stappen: <strong>alle combinaties opschrijven</strong>, "
                  "<strong>de deeluitdrukkingen uitwerken</strong> en <strong>de eindkolom bepalen</strong>. "
                  "Over waarheidstabellen klopt: <strong>ze tonen alle gevallen</strong>, <strong>ze bewijzen "
                  "een tautologie</strong> en <strong>hun aantal rijen verdubbelt per uitspraak</strong>. Ze "
                  "werken met waar en vals, of met 1 en 0 bij poorten, niet met gewone getallen."),
        ]),
        dict(kop="Logische poorten", blokken=[
            ("p", "<strong>De werking van een logische poort kan je wél in een waarheidstabel zetten</strong>, "
                  "en de vakfiche vraagt dat ook uitdrukkelijk."),
            ("kader", tabel(["poort", "bij welke bewerking", "wanneer de uitgang 1 is"],
                            [["<strong>de en-poort</strong>", "de conjunctie", "<strong>enkel als beide ingangen 1 zijn</strong>"],
                             ["<strong>de of-poort</strong>", "<strong>de disjunctie</strong>", "zodra minstens één ingang 1 is"],
                             ["<strong>de niet-poort</strong>", "de negatie", "<strong>ze keert het signaal om</strong>: een 1 wordt 0 en een 0 wordt 1"]])),
            ("p", "<strong>Twee en-poorten op een rij geven 1 als alle ingangen 1 zijn</strong>, want elke "
                  "en-poort eist dat al haar ingangen 1 zijn."),
            ("p", "Zo herken je ze in het echt. <strong>Een lamp die enkel brandt als twee schakelaars samen "
                  "aan staan, is een en-poort.</strong> <strong>Een lamp die brandt als minstens één "
                  "schakelaar aan staat, is dus geen en-poort maar een of-poort.</strong> En <strong>een "
                  "schakeling met drie ingangen vraagt een tabel van acht rijen</strong>."),
        ]),
    ])


# ───────────────────────── 4. Redeneren, bewijzen en tegenvoorbeelden
zet("redeneren-bewijzen-en-tegenvoorbeelden",
    titel="Redeneren, bewijzen en tegenvoorbeelden",
    onder="Waarom voorbeelden geen bewijs zijn, hoe je met één tegenvoorbeeld weerlegt, hoe een bewijs eruitziet, en wat je op het examen mag gebruiken.",
    secties=[
        dict(kop="Voorbeeld tegenover bewijs", blokken=[
            ("p", "<strong>Voorbeelden bewijzen niets; ze maken een uitspraak enkel geloofwaardiger.</strong> "
                  "Ze geven je een idee van de correctheid, maar <strong>honderd voorbeelden vormen geen "
                  "bewijs</strong>. Wie uit twee voorbeelden besluit dat een eigenschap altijd geldt, maakt "
                  "dus een fout: <strong>misschien bestaat er een derde geval dat ze wel schendt</strong>."),
            ("p", "<strong>Een bewijs moet voor alle gevallen gelden, niet enkel voor je voorbeeld.</strong> "
                  "Daarom werk je <strong>met letters in plaats van met getallen</strong>: met a en b staat "
                  "je redenering voor elk getal, met 3 en 5 enkel voor dat ene geval."),
            ("p", "Dat loopt gelijk met de twee kwantoren. <strong>Voor elke</strong> betekent dat "
                  "<strong>de uitspraak voor alle gevallen geldt</strong>, dus <strong>één tegenvoorbeeld "
                  "maakt ze vals</strong>. <strong>Er bestaat</strong> betekent dat <strong>er minstens één "
                  "geval is</strong>, dus <strong>om zo'n uitspraak te bewijzen volstaat één "
                  "voorbeeld</strong>."),
        ]),
        dict(kop="Het tegenvoorbeeld", blokken=[
            ("p", "<strong>Een foutieve wiskundige uitspraak weerleg je met een tegenvoorbeeld</strong>, en "
                  "<strong>één volstaat</strong>. Maar het moet wel een tegenvoorbeeld bij díé uitspraak "
                  "zijn: <strong>een tegenvoorbeeld dat buiten de uitspraak valt, zegt niets over de "
                  "uitspraak</strong>. Een cirkel weerlegt niets over rechthoeken."),
            ("kader", tabel(["foutieve uitspraak", "tegenvoorbeeld", "waarom het werkt"],
                            [["<strong>de wortel van een som is de som van de wortels</strong>",
                              "<strong>de wortel van 9 plus 16</strong>", "de wortel van 25 is 5, maar 3 + 4 is 7"],
                             ["<strong>elk kwadraat is groter dan nul</strong>", "<strong>het getal 0</strong>",
                              "0² is 0, en dat is niet groter dan nul"],
                             ["<strong>min a is altijd negatief</strong>", "a = min 3",
                              "min (min 3) is 3, dus positief"],
                             ["<strong>delen maakt altijd kleiner</strong>", "delen door een half",
                              "6 gedeeld door een half is 12, dus groter"],
                             ["<strong>elke rechthoek is een vierkant</strong>", "<strong>een rechthoek van 2 bij 5</strong>",
                              "ongelijke zijden, dus geen vierkant"],
                             ["<strong>dubbele lengte geeft dubbele oppervlakte</strong>", "een vierkant van 2 naar 4",
                              "de oppervlakte gaat van 4 naar 16, dus <strong>vier keer zo groot</strong>: de oppervlakte volgt het kwadraat van de factor"]])),
            ("p", "De vakfiche laat je twee soorten fouten weerleggen: <strong>rekenregels die fout worden "
                  "toegepast</strong> en <strong>uitspraken over schaalverandering</strong>, dus "
                  "<strong>allebei</strong>. Een klassieker van het eerste soort: wie schrijft dat 2 + 3 × 4 "
                  "gelijk is aan 20, miste <strong>de volgorde van de bewerkingen</strong> — eerst maal, dan "
                  "plus, dus 3 × 4 = 12 en daarbij 2 geeft <strong>14</strong>. Met haakjes zou er wel 20 "
                  "staan."),
        ]),
        dict(kop="Hoe een bewijs eruitziet", blokken=[
            ("p", "Drie stappen horen erbij: <strong>de gegevens benoemen</strong>, <strong>elke stap "
                  "verantwoorden</strong> en <strong>het besluit formuleren</strong>. Raden hoort nergens in "
                  "een bewijs. Het laatste deel heet <strong>het besluit</strong> of de conclusie; daar "
                  "herneem je wat je wou aantonen."),
            ("p", "Over bewijzen klopt dus: <strong>ze gelden voor alle gevallen</strong>, <strong>elke stap "
                  "wordt verantwoord</strong> en <strong>ze eindigen met een besluit</strong>."),
            ("p", "Verantwoorden betekent zeggen waarom een stap mag. Trek je bij een vergelijking aan beide "
                  "kanten 3 af, dan steun je op <strong>een eigenschap van gelijkheden</strong>: wat je links "
                  "doet, doe je rechts, en zo blijft de gelijkheid gelden. Wil je aantonen dat twee "
                  "driehoeken gelijkvormig zijn, dan wijs je <strong>een gelijkvormigheidskenmerk</strong> "
                  "aan: HH, ZHZ, ZZZ of het geval met een rechte hoek."),
            ("p", "De vakfiche vraagt bij een aangereikte redenering om <strong>de redeneerstappen te "
                  "beargumenteren</strong>, en <strong>redeneerstappen aan te vullen</strong> in de bewijzen "
                  "uit de lijst met bewijzen. Ze vraagt ook <strong>een bewijs te reconstrueren in een "
                  "gewijzigde situatie</strong>, en dat betekent: <strong>met andere symbolen of een andere "
                  "tekening</strong>, of voor een specifiek geval."),
        ]),
        dict(kop="Noteren, en wat mag mee op het examen", blokken=[
            ("p", "Bij een correct genoteerde redenering hoort <strong>vaktaal gebruiken</strong>, <strong>de "
                  "symbolen correct zetten</strong> en <strong>tussenstappen verklaren</strong>, met haakjes "
                  "en bewerkingstekens op de juiste plaats. Enkel het antwoord volstaat niet. <strong>Je "
                  "tussenstappen tellen mee omdat ze je redenering tonen</strong>: de fiche vraagt "
                  "uitdrukkelijk je werkwijze en redenering volledig uit te schrijven, en <strong>de correcte "
                  "notatie van begrippen en symbolen bepaalt mee je resultaat</strong>."),
            ("p", "<strong>Een berekening uitschrijven met de juiste symbolen is dus zelf al een wiskundige "
                  "redenering</strong>; de fiche noemt dat uitdrukkelijk zo. Welke symbolen ze vraagt: "
                  "<strong>en, of, niet</strong>, <strong>de pijl voor impliceert</strong> en <strong>de "
                  "dubbele pijl</strong> voor de equivalentie, plus de twee kwantoren. Een sommatieteken "
                  "staat er niet bij. <strong>De dubbele pijl moet je niet systematisch gebruiken bij het "
                  "oplossen van vergelijkingen</strong>; dat zegt de fiche zelf. Waar je de symbolen gebruikt, "
                  "moeten ze wel correct zijn."),
            ("kader", tabel(["bijlage", "mag mee op het examen"],
                            [["<strong>het formularium</strong>", "<strong>ja</strong>, als enige"],
                             ["de lijst met bewijzen", "<strong>neen</strong>"],
                             ["de lijst met begrippen en notaties", "<strong>neen</strong>"]])),
            ("weetje", "<strong>Reflectie over je oplossing hoort bij het werk</strong>, want <strong>zo "
                       "controleer je of je antwoord klopt</strong>. De vier stappen zijn: begrijp het "
                       "probleem, maak een plan, voer het uit, en reflecteer. Die vierde is volwaardig."),
        ]),
    ])


# ───────────────────────── 5. Ruimtefiguren, vlakke voorstellingen en vectoren
zet("ruimtefiguren-vlakke-voorstellingen-en-vectoren",
    titel="Ruimtefiguren, vlakke voorstellingen en vectoren",
    onder="De onderlinge ligging van rechten en vlakken, hoe je een ruimtefiguur plat tekent, en vectoren met hun richting, zin en grootte.",
    secties=[
        dict(kop="Rechten en vlakken in de ruimte", blokken=[
            ("p", "In de ruimte komt er één ligging bij die in het platte vlak niet bestaat: "
                  "<strong>kruisend</strong>. Twee rechten zijn kruisend als <strong>ze niet snijden en niet "
                  "evenwijdig lopen</strong>; ze liggen dan in geen enkel gemeenschappelijk vlak. "
                  "<strong>Twee kruisende rechten liggen dus nooit in hetzelfde vlak</strong> — was er zo'n "
                  "vlak, dan zouden ze snijden of evenwijdig zijn."),
            ("kader", tabel(["wat tegenover wat", "welke liggingen"],
                            [["<strong>twee rechten</strong>", "<strong>evenwijdig</strong>, samenvallend, <strong>snijdend</strong>, <strong>kruisend</strong> of loodrecht"],
                             ["<strong>twee vlakken</strong>", "<strong>evenwijdig</strong>, <strong>samenvallend</strong>, <strong>snijdend of loodrecht</strong>"],
                             ["<strong>een rechte en een vlak</strong>", "<strong>evenwijdig, erin, snijdend of loodrecht</strong> (loodrecht is een bijzonder geval van snijdend)"]])),
            ("p", "<strong>Twee vlakken kunnen niet kruisend zijn</strong>: dat begrip bestaat alleen voor "
                  "rechten. Vlakken snijden, vallen samen of zijn evenwijdig."),
            ("p", "De doorsnede zegt wat ze gemeen hebben. <strong>Twee snijdende vlakken hebben een rechte "
                  "als doorsnede</strong>; <strong>twee snijdende rechten hebben een punt</strong>, en precies "
                  "één, want met meer gemeenschappelijke punten zouden ze samenvallen."),
            ("p", "De vakfiche gebruikt hierbij begrippen uit de verzamelingenleer: element, "
                  "<strong>deelverzameling</strong>, <strong>doorsnede</strong>, <strong>unie en "
                  "verschil</strong>. Een functie hoort bij een ander onderdeel."),
        ]),
        dict(kop="Ruimtefiguren plat tekenen", blokken=[
            ("p", "Een <strong>ruimtefiguur</strong> heeft <strong>hoogte, breedte én diepte</strong>; ze is "
                  "driedimensionaal. <strong>Een balk</strong>, <strong>een kegel</strong> en <strong>een "
                  "bol</strong> zijn ruimtefiguren, een vierkant niet — dat is vlak."),
            ("kader", tabel(["manier", "wat ze doet"],
                            [["<strong>het cavalièreperspectief</strong>", "<strong>een manier om ruimte te tekenen</strong>: de diepte komt onder een hoek en vaak verkort op papier"],
                             ["<strong>de aanzichten</strong>", "<strong>vooraanzicht</strong>, <strong>zijaanzicht</strong> en <strong>bovenaanzicht</strong>; een binnenaanzicht bestaat niet"],
                             ["<strong>de ontwikkeling</strong>", "<strong>de figuur uitgeplooid in het vlak</strong>, zoals het bouwplan van een doos"]])),
            ("p", "<strong>Men tekent drie aanzichten omdat ze samen alle maten tonen</strong>: hoogte, "
                  "breedte en diepte."),
            ("p", "Tel de onderdelen van een kubus goed uit elkaar: <strong>zes zijvlakken</strong> (en dus "
                  "zes vlakken in haar ontwikkeling), <strong>twaalf ribben</strong> en <strong>acht "
                  "hoekpunten</strong>. En pas op met te algemene uitspraken: <strong>de ribben van het "
                  "bovenvlak en die van het ondervlak zijn niet allemaal kruisend</strong> — elke ribbe boven "
                  "is evenwijdig met of kruisend met een ribbe onder."),
        ]),
        dict(kop="Vectoren", blokken=[
            ("p", "Een vector heeft <strong>drie</strong> kenmerken: <strong>richting</strong> (de stand van "
                  "de lijn), <strong>zin</strong> (de kant waarop de pijl wijst) en <strong>grootte</strong> "
                  "(de lengte). <strong>Twee vectoren zijn gelijk als die drie gelijk zijn</strong>; hun "
                  "plaats in het vlak doet niet mee, en daarom mag je een vector verschuiven."),
            ("p", "Over vectoren klopt dus: <strong>hun plaats doet niet mee</strong>, <strong>ze hebben "
                  "richting, zin en grootte</strong> en <strong>ze beschrijven een verschuiving</strong>. Dat "
                  "laatste is het verband dat de vakfiche legt: <strong>een vector beschrijft een "
                  "verschuiving of translatie</strong> — zo veel die kant op."),
            ("kader", tabel(["begrip of bewerking", "wat het betekent"],
                            [["<strong>de nulvector</strong>", "<strong>een vector met grootte nul</strong>: begin- en eindpunt vallen samen, richting en zin zijn onbepaald"],
                             ["<strong>de tegengestelde vector</strong>", "<strong>dezelfde grootte, de andere zin</strong>; <strong>samen met de vector zelf geeft ze de nulvector</strong>"],
                             ["<strong>optellen</strong>", "<strong>kop aan staart zetten</strong>; de somvector loopt van het begin van de eerste naar het einde van de tweede"],
                             ["<strong>aftrekken</strong>", "<strong>de tegengestelde erbij optellen</strong>: je keert de tweede pijl om en telt op"],
                             ["<strong>maal 3</strong>", "<strong>drie keer zo lang</strong>, richting en zin blijven"],
                             ["<strong>maal min 2</strong>", "<strong>dubbel zo lang en omgekeerd</strong> van zin"],
                             ["<strong>maal een half</strong>", "<strong>de grootte wordt gehalveerd</strong>, dus korter en niet langer"]])),
            ("p", "De vakfiche gebruikt vectoren bij <strong>krachten</strong>, <strong>verplaatsing</strong> "
                  "en <strong>snelheid</strong>. <strong>Temperatuur is geen vectorgrootheid</strong>: ze "
                  "heeft wel een grootte maar geen richting."),
            ("kader", tabel(["situatie", "uitkomst"],
                            [["<strong>twee krachten van 5 newton in dezelfde zin</strong>", "<strong>10 newton</strong>: de groottes tellen op"],
                             ["<strong>twee krachten van 5 newton in tegengestelde zin</strong>", "<strong>de nulvector</strong>: ze heffen elkaar op, het voorwerp blijft in evenwicht"],
                             ["<strong>een boot vaart naar het noorden, de stroming duwt naar het oosten</strong>",
                              "<strong>tel de twee vectoren op</strong>: de somvector loopt schuin naar het noordoosten, en dat is de werkelijke koers"]])),
            ("p", "<strong>De som van twee vectoren kan dus kleiner zijn dan elk van de twee "
                  "afzonderlijk</strong>, namelijk als ze tegen elkaar in werken. Denk aan twee mensen die "
                  "elk aan een kant van een touw trekken."),
        ]),
    ])


# ───────────────────────── 6. Schaalverandering en gelijkvormige figuren
zet("schaalverandering-en-gelijkvormige-figuren",
    titel="Schaalverandering en gelijkvormige figuren",
    onder="De gelijkvormigheidsfactor en wat ze doet met lengte, oppervlakte en volume, werken met een schaal, en de vier gelijkvormigheidskenmerken van driehoeken.",
    secties=[
        dict(kop="De gelijkvormigheidsfactor", blokken=[
            ("p", "Twee figuren zijn <strong>gelijkvormig</strong> als ze <strong>dezelfde vorm hebben in een "
                  "andere grootte</strong>: alle hoeken zijn gelijk en alle zijden staan in dezelfde "
                  "verhouding. <strong>De gelijkvormigheidsfactor is de verhouding van de lengtes</strong>: "
                  "je deelt een lengte van de nieuwe figuur door de overeenkomstige lengte van de oude. "
                  "<strong>Gaat een figuur van 3 cm naar 12 cm, dan is de factor 4</strong>; <strong>bij "
                  "zijden 2 en 10 is de factor 5</strong>."),
            ("p", "<strong>Bij een factor kleiner dan 1 wordt de figuur kleiner</strong>: een factor van een "
                  "half halveert elke lengte, en dan wordt de oppervlakte een vierde."),
        ]),
        dict(kop="Lengte, oppervlakte en volume gaan niet gelijk op", blokken=[
            ("p", "Dit is de kern van het hoofdstuk, en meteen de klassieke misvatting. <strong>Niet alles "
                  "gaat met dezelfde factor.</strong>"),
            ("kader", tabel(["grootheid", "hoe ze meegaat", "bij factor 2", "bij factor 3"],
                            [["<strong>de lengte</strong>", "<strong>met de factor</strong>", "<strong>verdubbelt</strong>", "maal 3"],
                             ["<strong>de oppervlakte</strong>", "<strong>met het kwadraat</strong>", "<strong>vier keer zo groot</strong>", "<strong>negen keer zo groot</strong>"],
                             ["<strong>het volume</strong>", "<strong>met de derde macht</strong>", "<strong>acht keer zo groot</strong>", "<strong>27 keer zo groot</strong>"],
                             ["<strong>de hoeken</strong>", "<strong>ze blijven gelijk</strong>", "gelijk", "gelijk"]])),
            ("p", "<strong>Bij een dubbele lengte wordt het volume dus niet dubbel zo groot maar acht keer "
                  "zo groot.</strong> Dat is precies het soort uitspraak dat de vakfiche je laat weerleggen. "
                  "<strong>Een blikje dat in alle richtingen dubbel zo groot wordt, heeft acht keer zoveel "
                  "inhoud.</strong> En <strong>een foto op dubbele breedte, met dezelfde vorm, vraagt vier "
                  "keer zoveel inkt</strong>, want de inkt volgt de oppervlakte."),
            ("p", "Reken het na op een vierkant: <strong>een vierkant van 2 cm zijde, vergroot met factor 4, "
                  "krijgt een zijde van 8 cm en dus een oppervlakte van 64 cm²</strong>. Of korter: 4 × 4 "
                  "maal de oude oppervlakte van 4 cm²."),
            ("p", "<strong>Gelijkvormige driehoeken hebben dus ook niet dezelfde omtrek</strong>: die gaat "
                  "gewoon met de factor mee. Alleen de hoeken blijven gelijk. En <strong>twee driehoeken met "
                  "gelijke hoeken hebben niet automatisch dezelfde oppervlakte</strong>: ze zijn "
                  "gelijkvormig, niet gelijk."),
            ("weetje", "<strong>Grote dieren hebben dikkere botten omdat hun gewicht sneller groeit dan de "
                       "doorsnede van hun botten</strong>: het gewicht gaat met de derde macht, de doorsnede "
                       "met het kwadraat. Een mooi gevolg van schaalverandering."),
        ]),
        dict(kop="Werken met een schaal", blokken=[
            ("p", "<strong>Bij een schaal hoort geen eenheid</strong>: het is een verhouding, en 1 op 50 "
                  "geldt in welke eenheid je ook meet."),
            ("kader", tabel(["schaal", "op papier", "in het echt", "rekenwijze"],
                            [["<strong>1 op 50</strong>", "4 cm", "<strong>2 meter</strong>", "4 × 50 = 200 cm"],
                             ["<strong>1 op 100</strong>", "3 cm", "<strong>3 meter</strong>", "3 × 100 = 300 cm"],
                             ["<strong>1 op 25 000</strong>", "4 cm", "<strong>1 kilometer</strong>", "4 × 25 000 = 100 000 cm = 1 000 m"]])),
        ]),
        dict(kop="De gelijkvormigheidskenmerken van driehoeken", blokken=[
            ("p", "De vakfiche noemt <strong>HH</strong>, <strong>ZHZ</strong>, <strong>ZZZ</strong> en het "
                  "geval met een rechte hoek van 90 graden. Eén gelijke scherpe hoek volstaat niet."),
            ("kader", tabel(["kenmerk", "wat je moet weten"],
                            [["<strong>HH</strong>", "<strong>twee hoeken zijn gelijk</strong>"],
                             ["<strong>ZHZ</strong>", "<strong>twee zijden in verhouding met de hoek ertussen</strong> gelijk; <strong>de hoek moet er echt tussen liggen</strong>"],
                             ["<strong>ZZZ</strong>", "<strong>de drie zijden staan in verhouding</strong>"],
                             ["rechte hoek", "beide driehoeken hebben een hoek van 90 graden, plus nog een gegeven"]])),
            ("p", "<strong>Twee gelijke hoeken volstaan omdat de derde hoek eruit volgt</strong>: "
                  "<strong>de hoekensom van een driehoek is 180 graden</strong>, dus hij ligt vast. Heeft een "
                  "driehoek hoeken van 40 en 60 graden, dan is de derde <strong>80 graden</strong>."),
            ("p", "<strong>Bij gelijkvormige driehoeken staan de overeenkomstige zijden in dezelfde "
                  "verhouding</strong>, en daarmee bereken je de onbekende. Drie stappen: <strong>het "
                  "kenmerk aanwijzen</strong>, <strong>de verhouding opstellen</strong> en <strong>de "
                  "onbekende berekenen</strong>. De oppervlakte heb je er niet voor nodig."),
            ("kader", tabel(["opgave", "antwoord", "rekenwijze"],
                            [["<strong>factor 2, een zijde van 5 cm</strong>", "<strong>10 cm</strong>", "5 × 2"],
                             ["<strong>zijden 4 en 6, de tweede zijde van de kleine is 3</strong>", "<strong>4,5 cm</strong>",
                              "de factor is 6 : 4 = 1,5, en 3 × 1,5 = 4,5"],
                             ["<strong>een stok van 1 m geeft 1,5 m schaduw, een boom 12 m schaduw</strong>", "<strong>de boom is 8 m</strong>",
                              "12 : 1,5 = 8, en 1 × 8 = 8"],
                             ["<strong>een stok van 2 m geeft 3 m schaduw, hoeveel geeft een boom van 10 m?</strong>", "<strong>15 m</strong>",
                              "de verhouding is 3 op 2, dus 10 × 1,5 = 15"]])),
            ("p", "<strong>De twee driehoeken bij een schaduwmeting zijn gelijkvormig omdat de zonnestralen "
                  "gelijk invallen</strong>: dezelfde hoek met de grond, en beide keren een rechte hoek. Dat "
                  "is het kenmerk HH."),
            ("p", "<strong>De vakfiche vraagt het kenmerk te benoemen en niet enkel te rekenen, want het "
                  "kenmerk is de verantwoording.</strong> Zonder kenmerk weet je niet waarom je die "
                  "verhouding mag opstellen."),
        ]),
    ])


# ───────────────────────── 7. Pythagoras en de goniometrische verhoudingen
zet("pythagoras-en-de-goniometrische-verhoudingen",
    titel="Pythagoras en de goniometrische verhoudingen",
    onder="De stelling van Pythagoras en haar omgekeerde, afstanden en diagonalen berekenen, en sinus, cosinus en tangens met de grondformule.",
    secties=[
        dict(kop="De stelling van Pythagoras", blokken=[
            ("p", "De stelling zegt: <strong>de twee kleine kwadraten samen geven het grote</strong>. Ze "
                  "<strong>geldt enkel in een rechthoekige driehoek</strong>, dus niet in elke driehoek. "
                  "<strong>De schuine zijde ligt tegenover de rechte hoek, en ze is altijd de langste "
                  "zijde</strong>, want ze ligt tegenover de grootste hoek."),
            ("kader", tabel(["gegeven", "gevraagd", "rekenwijze", "antwoord"],
                            [["<strong>rechthoekszijden 3 en 4</strong>", "de schuine zijde", "9 + 16 = 25", "<strong>5</strong>"],
                             ["<strong>rechthoekszijden 6 en 8</strong>", "de schuine zijde", "36 + 64 = 100", "<strong>10</strong>"],
                             ["<strong>schuine zijde 13, rechthoekszijde 5</strong>", "de andere rechthoekszijde", "169 − 25 = 144", "<strong>12</strong>"]])),
            ("p", "Met de <strong>omgekeerde</strong> stelling toon je aan dát een driehoek rechthoekig is. "
                  "<strong>Bij zijden 9, 12 en 15: 81 + 144 = 225, en 15² is ook 225</strong>, dus de hoek is "
                  "recht. <strong>Een driehoek met zijden 5, 6 en 8 is niet rechthoekig</strong>: 25 + 36 = "
                  "61 en 8² = 64, en dat klopt niet."),
            ("p", "Drietallen die wél passen: <strong>3, 4 en 5</strong>, <strong>5, 12 en 13</strong> en "
                  "<strong>8, 15 en 17</strong>. Bij 2, 3 en 4 lukt het niet, want 4 + 9 is geen 16."),
        ]),
        dict(kop="Afstanden, diagonalen en problemen", blokken=[
            ("p", "<strong>De afstand tussen twee punten in het vlak bereken je met Pythagoras op de "
                  "verschillen</strong>: het verschil in x en het verschil in y zijn de rechthoekszijden, de "
                  "afstand is de schuine zijde. <strong>Van (0, 0) naar (3, 4) is dat 5</strong>, en "
                  "<strong>van (1, 1) naar (4, 5) ook 5</strong>, want de verschillen zijn weer 3 en 4."),
            ("p", "<strong>Pythagoras werkt ook in de ruimte</strong>, bijvoorbeeld voor de ruimtediagonaal "
                  "van een balk: je past hem twee keer toe, eerst in het grondvlak en dan met de hoogte "
                  "erbij. <strong>De ruimtediagonaal van een kubus met ribbe 1 is de wortel van 3</strong>: "
                  "de diagonaal van het grondvlak is de wortel van 2, en 2 + 1 = 3."),
            ("kader", tabel(["probleem", "antwoord", "rekenwijze"],
                            [["<strong>een ladder van 5 m, de voet 3 m van de muur</strong>", "<strong>4 meter hoog</strong>", "25 − 9 = 16"],
                             ["<strong>een kast van 2 bij 1 m, hoe schuin past ze</strong>", "<strong>de wortel van 5</strong>, ongeveer 2,24 m", "4 + 1 = 5"],
                             ["<strong>een rechthoekig veld van 30 bij 40 m</strong>", "<strong>de diagonaal is 50 m</strong>", "900 + 1 600 = 2 500"]])),
            ("p", "<strong>Bij een ladder tegen een muur is de muur niet de schuine zijde</strong>: de muur "
                  "en de grond vormen juist de rechte hoek, en de ladder ligt daar tegenover."),
            ("p", "Drie stappen helpen: <strong>een schets maken</strong>, <strong>de rechte hoek "
                  "aanwijzen</strong> en <strong>de schuine zijde benoemen</strong>. Meten hoeft niet, je "
                  "rekent. <strong>Je maakt eerst een schets omdat je dan ziet welke zijde de schuine "
                  "is</strong>; zonder schets verwissel je die gemakkelijk met een rechthoekszijde."),
        ]),
        dict(kop="Sinus, cosinus en tangens", blokken=[
            ("kader", tabel(["getal", "welke zijden", "bij de driehoek 3-4-5"],
                            [["<strong>de sinus</strong>", "<strong>overstaande zijde op schuine zijde</strong>", "<strong>3 : 5 = 0,6</strong>"],
                             ["<strong>de cosinus</strong>", "<strong>aanliggende zijde op schuine zijde</strong>", "<strong>4 : 5 = 0,8</strong>"],
                             ["<strong>de tangens</strong>", "<strong>overstaande op aanliggende zijde</strong>; <strong>ze gebruikt de schuine zijde niet</strong>", "<strong>3 : 4 = 0,75</strong>"]])),
            ("p", "Over die drie klopt: <strong>de tangens mist de schuine zijde</strong>, <strong>de sinus "
                  "gebruikt de overstaande zijde</strong> en <strong>de cosinus gebruikt de aanliggende "
                  "zijde</strong>."),
            ("p", "<strong>De sinus van een scherpe hoek is altijd kleiner dan 1</strong>, want de "
                  "overstaande zijde is korter dan de schuine. Om dezelfde reden <strong>kan de cosinus nooit "
                  "groter zijn dan 1</strong>."),
            ("p", "<strong>De grondformule van de goniometrie is sin²α + cos²α = 1.</strong> Ze staat "
                  "<strong>niet los van Pythagoras maar volgt er juist uit</strong>: deel bij Pythagoras "
                  "alles door het kwadraat van de schuine zijde. <strong>Sin² plus cos² van dezelfde hoek is "
                  "dus altijd 1.</strong> Ken je de sinus, dan ken je ook de cosinus: <strong>is de sinus "
                  "0,6, dan is de cosinus 0,8</strong> bij een scherpe hoek, want 1 − 0,36 = 0,64 en de "
                  "wortel daarvan is 0,8."),
        ]),
        dict(kop="Een rechthoekige driehoek oplossen", blokken=[
            ("p", "Drie stappen: <strong>de gegeven zijden benoemen</strong>, <strong>het juiste "
                  "goniometrische getal kiezen</strong> en <strong>de onbekende berekenen met ICT</strong>. "
                  "De vakfiche laat je de goniometrische getallen met ICT opzoeken; de oppervlakte heb je er "
                  "niet voor nodig."),
            ("kader", tabel(["je kent", "je zoekt", "welk getal"],
                            [["<strong>de hoek en de aanliggende zijde</strong>", "de overstaande zijde", "<strong>de tangens</strong>"],
                             ["<strong>de hoek en de schuine zijde</strong>", "de overstaande zijde", "<strong>de sinus</strong>: overstaande = sinus × schuine zijde"],
                             ["<strong>een bergpad van 200 m onder 30 graden</strong>", "het hoogteverschil", "<strong>de sinus</strong>: het pad is de schuine zijde, sin 30° is een half, dus 100 m"]])),
            ("p", "<strong>Met de tangens bereken je de hoogte van een boom uit de kijkhoek en de "
                  "afstand</strong>; de vakfiche noemt dat voorbeeld zelf. <strong>Sta je 20 m van een boom "
                  "en kijk je onder 45 graden naar de top, dan is de boom ongeveer 20 m hoog</strong>, want "
                  "<strong>de tangens van 45 graden is 1</strong>. Je ooghoogte komt er nog bij."),
            ("p", "Bij 45 graden klopt trouwens alles tegelijk: <strong>de tangens is 1</strong>, <strong>de "
                  "twee rechthoekszijden zijn even lang</strong> en <strong>de sinus en de cosinus zijn "
                  "gelijk</strong>. De schuine zijde blijft wel de langste."),
        ]),
    ])


# ───────────────────────── 8. Formules omvormen
zet("formules-omvormen",
    titel="Formules omvormen",
    onder="De eigenschappen van gelijkheden, een letter vrijmaken in de omgekeerde orde, en formules uit de wiskunde en de natuurwetenschappen omvormen.",
    secties=[
        dict(kop="Wat mag je met een gelijkheid doen", blokken=[
            ("p", "Eén regel draagt het hele hoofdstuk: <strong>doe aan beide kanten hetzelfde</strong>. "
                  "Optellen, aftrekken, vermenigvuldigen of delen aan beide kanten houdt de gelijkheid in "
                  "stand; één kant veranderen breekt ze."),
            ("p", "Met één voorbehoud: <strong>de deler mag niet nul zijn</strong>. <strong>Door nul mag je "
                  "nooit delen</strong>, dus bij een letter ga je altijd na of ze nul kan worden."),
            ("p", "<strong>Een letter vrijmaken en een formule omvormen zijn hetzelfde</strong>: je zet die "
                  "letter alleen aan één kant van het isgelijkteken. <strong>De betekenis van de formule "
                  "verandert daarbij niet</strong>; je schrijft dezelfde samenhang anders op."),
            ("p", "<strong>Je maakt een formule vrij in de omgekeerde orde van de bewerkingen</strong>: wat "
                  "het laatst bij de onbekende kwam, haal je eerst weg, net als bij het uitpakken van een "
                  "doos. In <strong>y = 3x + 6</strong> trek je dus eerst 6 af en deel je dan door 3: "
                  "<strong>x = (y − 6) : 3</strong>."),
            ("p", "Let nog op één ding: <strong>bij maal min 1 keert er in een gelijkheid geen teken "
                  "om</strong>, want er is geen ongelijkheidsteken. Bij een ongelijkheid gebeurt dat wel."),
        ]),
        dict(kop="Formules uit de wiskunde", blokken=[
            ("p", "De vakfiche noemt als wiskundige voorbeelden <strong>de eerstegraadsfunctie</strong>, "
                  "<strong>de vergelijking van een tweedegraadsfunctie</strong> en <strong>de formules voor "
                  "omtrek en oppervlakte</strong>. De wet van Ohm staat bij de natuurwetenschappen."),
            ("kader", tabel(["formule", "gevraagd", "omgevormd"],
                            [["omtrek rechthoek = 2 × l + 2 × b", "de lengte", "<strong>omtrek gedeeld door 2, min de breedte</strong>"],
                             ["oppervlakte rechthoek = l × b", "de breedte", "<strong>oppervlakte gedeeld door de lengte</strong>"],
                             ["oppervlakte vierkant = z²", "de zijde", "<strong>de vierkantswortel</strong> van de oppervlakte"],
                             ["oppervlakte driehoek = basis × hoogte : 2", "de hoogte", "<strong>2 × oppervlakte, gedeeld door de basis</strong>"],
                             ["omtrek cirkel = 2 × π × r", "de straal", "<strong>omtrek gedeeld door 2π</strong>"],
                             ["y = a × x", "a", "<strong>y gedeeld door x</strong>, mits x niet nul is"]])),
            ("p", "Reken twee gevallen na. <strong>Een driehoek met oppervlakte 12 en basis 6 heeft hoogte "
                  "4</strong> (2 × 12 = 24, gedeeld door 6). En <strong>een vierkant met oppervlakte 49 heeft "
                  "zijde 7</strong>."),
            ("p", "<strong>Bij een zuiver kwadratische formule krijg je twee oplossingen</strong>: de wortel "
                  "geeft een positieve en een negatieve waarde. <strong>Bij een lengte houd je enkel de "
                  "positieve, want een lengte is nooit negatief.</strong> De wiskunde geeft twee antwoorden, "
                  "de context sluit er één uit — dat heet demathematiseren."),
        ]),
        dict(kop="Formules uit de natuurwetenschappen", blokken=[
            ("p", "De vakfiche noemt <strong>massadichtheid</strong>, <strong>de wet van Ohm</strong>, en "
                  "<strong>veerkracht en druk</strong>. Pythagoras is wiskunde en geen "
                  "natuurwetenschappelijke formule."),
            ("kader", tabel(["formule", "gevraagd", "omgevormd", "voorbeeld"],
                            [["dichtheid = massa : volume", "de massa", "<strong>dichtheid × volume</strong>",
                              "<strong>20 g in 4 cm³ geeft 5 g per cm³</strong>"],
                             ["dezelfde formule", "het volume", "<strong>massa gedeeld door de dichtheid</strong>", ""],
                             ["<strong>de wet van Ohm: spanning = stroom × weerstand</strong>", "de weerstand", "<strong>spanning gedeeld door de stroom</strong>",
                              "<strong>12 volt bij 3 ampère geeft 4 ohm</strong>"],
                             ["zwaartekracht = massa × valversnelling", "de massa", "<strong>kracht gedeeld door de valversnelling</strong>", ""],
                             ["veerkracht = veerconstante × uitrekking", "de uitrekking", "<strong>kracht gedeeld door de veerconstante</strong>", ""],
                             ["concentratie = stofhoeveelheid : volume", "de stofhoeveelheid", "<strong>concentratie × volume</strong>",
                              "<strong>2 mol per liter in 3 liter is 6 mol</strong>"],
                             ["vermogen = energie : tijd", "de energie", "<strong>vermogen × tijd</strong>",
                              "<strong>100 watt gedurende 20 seconden is 2 000 joule</strong>"]])),
            ("p", "<strong>Druk is kracht gedeeld door oppervlakte</strong>, dus <strong>bij een kleinere "
                  "oppervlakte wordt de druk groter</strong>. Daarom prikt een speld zo goed. En omgekeerd: "
                  "<strong>bij dezelfde kracht geeft een grotere oppervlakte minder druk</strong>, en daarom "
                  "zakken brede sneeuwschoenen minder weg."),
            ("p", "<strong>Kinetische energie hangt af van het kwadraat van de snelheid</strong>, dus "
                  "<strong>een auto die dubbel zo snel rijdt heeft vier keer zoveel kinetische "
                  "energie</strong> — en daarom een veel langere remweg. Let op bij de potentiële energie: "
                  "<strong>die hangt niet van de hoogte alleen af</strong>, maar van massa, valversnelling "
                  "én hoogte samen."),
            ("p", "Drie stappen bij het omvormen: <strong>bepaal welke letter je zoekt</strong>, <strong>werk "
                  "met eigenschappen van gelijkheden</strong> en <strong>controleer de eenheden</strong>. "
                  "Snel afronden is net wat de vakfiche afraadt."),
            ("weetje", "<strong>Formules omvormen is buiten de wiskunde nuttig omdat je er elke grootheid "
                       "mee berekent</strong> die erin staat, zolang je de andere kent. Eén formule, zoveel "
                       "vragen als er letters in staan."),
        ]),
    ])


# ───────────────────────── 9. Eerstegraadsvergelijkingen en -ongelijkheden
zet("eerstegraadsvergelijkingen-en-ongelijkheden",
    titel="Eerstegraadsvergelijkingen en -ongelijkheden",
    onder="Vergelijkingen oplossen en het aantal oplossingen herkennen, ongelijkheden met de omkeerregel, en de grafische betekenis van positief en negatief.",
    secties=[
        dict(kop="Een eerstegraadsvergelijking oplossen", blokken=[
            ("p", "In een <strong>eerstegraadsvergelijking in één onbekende staat de onbekende in de eerste "
                  "macht</strong>: één letter, zonder kwadraat of hogere macht. Haar grafiek is een rechte."),
            ("p", "Oplossen steunt op één eigenschap: <strong>aan beide kanten mag je hetzelfde doen</strong>. "
                  "<strong>Aan beide kanten 5 bijtellen</strong>, <strong>aan beide kanten aftrekken</strong>, "
                  "<strong>met 3 vermenigvuldigen</strong> of <strong>door 2 delen</strong> — altijd aan "
                  "beide kanten tegelijk, want één kant veranderen breekt de gelijkheid."),
            ("p", "De stappen: <strong>haakjes uitwerken</strong>, <strong>de onbekenden "
                  "samenbrengen</strong> en <strong>delen door de coëfficiënt</strong>. Een grafiek hoeft "
                  "niet voor een algebraïsche oplossing, al helpt ze bij de controle."),
            ("kader", tabel(["vergelijking", "tussenstap", "oplossing"],
                            [["<strong>3x + 5 = 20</strong>", "20 − 5 = 15, dan : 3", "<strong>x = 5</strong>"],
                             ["<strong>2x − 4 = 10</strong>", "10 + 4 = 14, dan : 2", "<strong>x = 7</strong>"],
                             ["<strong>5x = 2x + 12</strong>", "2x naar links: 3x = 12", "<strong>x = 4</strong>"],
                             ["<strong>4(x − 1) = 12</strong>", "4x − 4 = 12, dus 4x = 16", "<strong>x = 4</strong>"]])),
            ("p", "<strong>Je noteert de oplossing als een oplossingenverzameling</strong>: bij een "
                  "vergelijking een verzameling met één of enkele getallen. Een interval hoort bij een "
                  "ongelijkheid."),
            ("p", "<strong>Controleer je oplossing in de oorspronkelijke vergelijking, want zo vind je "
                  "rekenfouten</strong>: vul je antwoord in, en komen links en rechts hetzelfde uit, dan "
                  "klopt het. Dat is de reflectiestap."),
        ]),
        dict(kop="Niet altijd één oplossing", blokken=[
            ("p", "<strong>Een eerstegraadsvergelijking heeft niet altijd precies één oplossing.</strong>"),
            ("kader", tabel(["vergelijking", "wat eruit komt", "oplossingenverzameling"],
                            [["<strong>x = x + 1</strong>", "0 = 1, en dat is vals", "<strong>de lege verzameling</strong>"],
                             ["<strong>x = x + 5</strong>", "0 = 5", "<strong>geen enkele oplossing</strong>"],
                             ["<strong>2x + 2 = 2(x + 1)</strong>", "links en rechts hetzelfde", "<strong>alle reële getallen</strong>"]])),
            ("p", "<strong>De oplossing van een vergelijking van de vorm f(x) = 0 is de nulwaarde van "
                  "f.</strong> Dat verband staat op de vakfiche; grafisch is het het snijpunt met de x-as."),
        ]),
        dict(kop="Vraagstukken vertalen", blokken=[
            ("p", "<strong>Een vraagstuk naar een vergelijking vertalen hoort wél bij de leerstof</strong>; "
                  "de vakfiche vraagt het uitdrukkelijk."),
            ("kader", tabel(["vraagstuk", "de vergelijking", "antwoord"],
                            [["<strong>een getal plus zijn dubbele is 21</strong>", "<strong>x + 2x = 21</strong>", "x = 7"],
                             ["<strong>drie opeenvolgende getallen met som 24</strong>", "(x − 1) + x + (x + 1) = 3x = 24", "<strong>het middelste is 8</strong>"],
                             ["<strong>twee getallen schelen 6, hun som is 20</strong>", "x + (x + 6) = 20", "<strong>het kleinste is 7</strong>, het andere 13"],
                             ["<strong>een abonnement van 20 euro plus 3 euro per uur, wanneer kost het 50 euro?</strong>", "20 + 3x = 50", "<strong>na 10 uur</strong>"]])),
        ]),
        dict(kop="Ongelijkheden", blokken=[
            ("p", "Bijna alles blijft hetzelfde, op één regel na: <strong>deel of vermenigvuldig je met een "
                  "negatief getal, dan keert het ongelijkheidsteken om</strong>. Dat is de klassieke valkuil. "
                  "<strong>Bij optellen aan beide kanten blijft het teken gewoon staan.</strong>"),
            ("kader", tabel(["ongelijkheid", "wat je doet", "oplossing"],
                            [["<strong>2x &gt; 10</strong>", "delen door 2, positief, teken blijft", "<strong>x &gt; 5</strong>"],
                             ["<strong>x + 4 &gt; 9</strong>", "4 aftrekken", "<strong>x &gt; 5</strong>, de 5 zelf hoort er niet bij"],
                             ["<strong>3x − 2 &lt; 7</strong>", "3x &lt; 9, delen door 3", "<strong>x &lt; 3</strong>"],
                             ["<strong>min 3x &gt; 9</strong>", "delen door min 3, <strong>teken omkeren</strong>", "<strong>x &lt; min 3</strong>"],
                             ["<strong>min x &gt; min 4</strong>", "maal min 1, <strong>teken omkeren</strong>", "<strong>x &lt; 4</strong>"]])),
            ("p", "<strong>Je mag dus niet zonder nadenken met min 1 vermenigvuldigen</strong>: vergeet je "
                  "het teken om te keren, dan krijg je precies de verkeerde helft van de getallenas. "
                  "<strong>Controleer daarom één getal uit je oplossing</strong>: klopt de ongelijkheid, dan "
                  "koos je de juiste kant."),
            ("p", "De stappen: <strong>de onbekende vrijmaken</strong>, <strong>het teken omkeren bij een "
                  "negatieve deler</strong> en <strong>de oplossing als interval noteren</strong>. Een top "
                  "hoort bij een parabool, niet hier."),
            ("p", "<strong>De oplossing van x ≥ 2 is het interval vanaf 2 gesloten</strong>, want het "
                  "isgelijkteken zit erin. Bij <strong>x &lt; 3</strong> zijn <strong>2</strong>, "
                  "<strong>0</strong> en <strong>min 5</strong> oplossingen, maar 3 zelf niet. <strong>Een "
                  "oplossing van een ongelijkheid bestaat meestal uit oneindig veel getallen</strong>, en "
                  "daarom noteer je ze als interval en niet als lijst. <strong>Op een getallenas kan je ze "
                  "ook voorstellen</strong>, met open of volle bolletjes aan de grens; de vakfiche vraagt "
                  "dat."),
            ("p", "Een voorbeeld uit het leven: <strong>een taxi kost 5 euro plus 2 euro per kilometer en je "
                  "hebt 25 euro</strong>, dus 5 + 2x ≤ 25, 2x ≤ 20 en je kan <strong>ten hoogste 10 "
                  "kilometer</strong>."),
        ]),
        dict(kop="Grafisch lezen", blokken=[
            ("p", "<strong>Een vergelijking los je grafisch op door het snijpunt van de grafieken te "
                  "zoeken</strong>: de x van dat punt is de oplossing. Bij f(x) = 0 is dat het snijpunt met "
                  "de x-as."),
            ("kader", tabel(["uitspraak", "waar de grafiek ligt"],
                            [["<strong>f(x) &gt; 0</strong>", "<strong>boven de x-as</strong>"],
                             ["<strong>f(x) &lt; 0</strong>", "<strong>onder de x-as</strong>"]])),
            ("p", "<strong>Een stijgende rechte die de x-as snijdt in 4, is positief rechts van 4.</strong> "
                  "<strong>Bij een dalende rechte is het net omgekeerd</strong>: ze komt van boven en duikt "
                  "na haar nulpunt onder de as, dus links is ze positief."),
        ]),
    ])


# ───────────────────────── 10. Stelsels van twee vergelijkingen
zet("stelsels-van-twee-vergelijkingen",
    titel="Stelsels van twee vergelijkingen",
    onder="De drie oplossingsmethodes, de drie soorten stelsels met hun grafische betekenis, en vraagstukken met twee onbekenden.",
    secties=[
        dict(kop="Wat een stelsel is, en hoe je het oplost", blokken=[
            ("p", "Een stelsel zijn <strong>twee vergelijkingen die samen gelden</strong>: je zoekt de "
                  "waarden die aan beide tegelijk voldoen. <strong>De oplossing noteer je niet als één getal "
                  "maar als een koppel</strong>, eerst de x en dan de y; de vakfiche noemt dat de "
                  "koppelvoorstelling."),
            ("p", "De vakfiche noemt <strong>drie</strong> algebraïsche methodes. De discriminant hoort bij "
                  "de tweedegraadsvergelijkingen en niet hier."),
            ("kader", tabel(["methode", "wat je doet", "voorbeeld"],
                            [["<strong>de combinatiemethode</strong>", "<strong>optellen of aftrekken</strong>, zodat <strong>één onbekende wegvalt</strong>",
                              "<strong>x + y = 10 en x − y = 2</strong>: optellen geeft 2x = 12, dus <strong>x = 6 en y = 4</strong>"],
                             ["<strong>de substitutiemethode</strong>", "<strong>een onbekende vervangen door een uitdrukking</strong>",
                              "<strong>y = 2x en x + y = 9</strong>: 3x = 9, dus <strong>x = 3 en y = 6</strong>"],
                             ["<strong>de gelijkstellingsmethode</strong>", "beide keren staat dezelfde letter alleen, dus stel je de rechterleden gelijk",
                              "<strong>y = 3x − 1 en y = x + 5</strong>: 2x = 6, dus <strong>x = 3 en y = 8</strong>"]])),
            ("p", "Nog drie om zelf na te rekenen. <strong>x + y = 12 en x − y = 4 geeft x = 8</strong> (en "
                  "y = 4). <strong>2x + y = 11 met y = 3 geeft x = 4.</strong> <strong>3x + y = 17 met y = 2 "
                  "geeft x = 5.</strong>"),
            ("p", "<strong>Controleer je oplossing in beide vergelijkingen</strong>, want ze moet aan allebei "
                  "voldoen: een koppel dat maar aan één vergelijking voldoet, is geen oplossing van het "
                  "stelsel."),
        ]),
        dict(kop="Drie soorten stelsels", blokken=[
            ("kader", tabel(["soort", "hoeveel oplossingen", "grafisch", "voorbeeld"],
                            [["<strong>bepaald</strong>", "<strong>precies één</strong>", "<strong>twee snijdende rechten</strong>, dus een <strong>verschillende richtingscoëfficiënt</strong>",
                              "x + y = 10 en x − y = 2"],
                             ["<strong>strijdig</strong>", "<strong>geen enkele</strong>; <strong>de lege verzameling</strong>",
                              "<strong>twee evenwijdige rechten</strong> die niet samenvallen: <strong>nul snijpunten</strong>",
                              "<strong>x + y = 5 en x + y = 7</strong>: dezelfde som kan niet 5 én 7 zijn"],
                             ["<strong>onbepaald</strong>", "<strong>oneindig veel</strong>", "<strong>twee samenvallende rechten</strong>: dezelfde richtingscoëfficiënt én hetzelfde snijpunt met de y-as",
                              "<strong>x + y = 5 en 2x + 2y = 10</strong>: de tweede is het dubbele van de eerste"]])),
            ("p", "<strong>Een stelsel met precies één oplossing heet dus bepaald, niet strijdig</strong>; "
                  "strijdig betekent juist dat er géén oplossing is. <strong>Twee rechten met dezelfde "
                  "richtingscoëfficiënt zijn evenwijdig</strong>: verschilt ook hun snijpunt met de y-as, dan "
                  "vallen ze niet samen en is het stelsel strijdig."),
            ("p", "Over stelsels klopt dus: <strong>ze kunnen geen oplossing hebben</strong>, <strong>ze "
                  "kunnen er oneindig veel hebben</strong> en <strong>ze kunnen er precies één "
                  "hebben</strong>. Precies twee oplossingen bestaat niet bij een stelsel van "
                  "eerstegraadsvergelijkingen."),
            ("p", "<strong>Het soort stelsel benoemen is nuttig omdat je dan weet wat je antwoord "
                  "betekent</strong>: komt er 0 = 5 uit, dan is het stelsel strijdig en is dát je antwoord, "
                  "geen rekenfout."),
        ]),
        dict(kop="Grafisch oplossen", blokken=[
            ("p", "<strong>Grafisch is de oplossing het snijpunt van twee rechten</strong>: het punt dat op "
                  "beide ligt, voldoet aan beide vergelijkingen. <strong>Grafisch oplossen mag met "
                  "ICT</strong>; de vakfiche vraagt zelfs uitdrukkelijk om stelsels grafisch op te lossen, "
                  "met en zonder ICT."),
            ("p", "Maar <strong>grafisch oplossen is niet even nauwkeurig als algebraïsch oplossen</strong>: "
                  "een snijpunt lees je af, en dat is zelden exact. Algebraïsch krijg je de precieze waarden."),
        ]),
        dict(kop="Vraagstukken met twee onbekenden", blokken=[
            ("p", "<strong>Een vraagstuk met twee onbekenden los je niet op met één vergelijking</strong>: "
                  "dan blijft het onbepaald. Je hebt evenveel vergelijkingen als onbekenden nodig."),
            ("p", "De stappen: <strong>twee onbekenden benoemen</strong>, <strong>twee vergelijkingen "
                  "opstellen</strong> en <strong>het stelsel oplossen</strong>. De vakfiche vraagt daarna "
                  "het antwoord terug in de context te plaatsen."),
            ("kader", tabel(["vraagstuk", "het stelsel", "antwoord"],
                            [["<strong>twee getallen met som 20 en verschil 4</strong>", "x + y = 20 en x − y = 4",
                              "<strong>het grootste is 12</strong>"],
                             ["<strong>twaalf stukken fruit, 4 peren meer dan appels</strong>", "a + p = 12 en p = a + 4",
                              "<strong>4 appels</strong> (en 8 peren)"],
                             ["<strong>abonnement A: 20 euro plus 2 per uur; abonnement B: 10 euro plus 4 per uur</strong>", "20 + 2x = 10 + 4x",
                              "<strong>na 5 uur kosten ze evenveel</strong>"],
                             ["<strong>een kaars van 20 cm die 2 cm per uur brandt, en een van 14 cm die 1 cm per uur brandt</strong>", "20 − 2x = 14 − x",
                              "<strong>na 6 uur</strong>, beide zijn dan 8 cm"]])),
            ("p", "Bij de abonnementen zegt het snijpunt waar de omslag ligt: <strong>bij veel uren is dat "
                  "met het laagste uurtarief het voordeligst</strong>, want dan weegt het uurtarief het "
                  "zwaarst."),
        ]),
    ])


# ───────────────────────── 11. Tweedegraadsvergelijkingen
zet("tweedegraadsvergelijkingen",
    titel="Tweedegraadsvergelijkingen",
    onder="De merkwaardige producten, ontbinden in factoren, de discriminant en wat ze zegt, en vraagstukken van de tweede graad.",
    secties=[
        dict(kop="De merkwaardige producten", blokken=[
            ("p", "Er zijn er <strong>drie</strong>, en je moet ze in beide richtingen kunnen lezen: van "
                  "product naar som om uit te werken, en van som naar product om te ontbinden."),
            ("kader", tabel(["product", "uitgewerkt", "voorbeeld"],
                            [["<strong>(a + b)²</strong>", "<strong>a² + 2ab + b²</strong>",
                              "<strong>x² + 2x + 1 is het kwadraat van (x + 1)</strong>"],
                             ["<strong>(a − b)²</strong>", "a² − 2ab + b²; <strong>het dubbele product is hier negatief</strong>",
                              "<strong>(x − 4)² = x² − 8x + 16</strong>"],
                             ["<strong>(a + b)(a − b)</strong>", "<strong>a² − b²</strong>: de twee middelste termen vallen weg",
                              "<strong>x² − 25 = (x − 5)(x + 5)</strong>"]])),
            ("p", "Let dus op het teken: <strong>bij (a − b)² is het dubbele product niet positief</strong> "
                  "maar negatief; het volgt het teken in de tweeterm."),
        ]),
        dict(kop="Ontbinden in factoren", blokken=[
            ("p", "<strong>Ontbinden in factoren betekent een som als een product schrijven.</strong> Dat is "
                  "handig omdat <strong>een product nul is zodra één factor nul is</strong>, en "
                  "<strong>elke factor dus een oplossing geeft</strong>."),
            ("p", "De stappen, in deze orde: <strong>eerst een gemeenschappelijke factor zoeken</strong>, "
                  "dan <strong>een merkwaardig product herkennen</strong>, dan <strong>twee getallen zoeken "
                  "met de juiste som en het juiste product</strong>. Letters vervangen door getallen is geen "
                  "ontbinding."),
            ("kader", tabel(["veelterm", "ontbonden", "hoe je erop komt"],
                            [["<strong>6x² + 9x</strong>", "<strong>3x</strong>(2x + 3)", "3x staat in beide termen"],
                             ["<strong>3x² + 6x</strong>", "<strong>3x(x + 2)</strong>", "controle: 3x · x = 3x² en 3x · 2 = 6x"],
                             ["<strong>2x² + 6x</strong>", "<strong>2x(x + 3)</strong>", "de oplossingen zijn dan <strong>0 en min 3</strong>"],
                             ["<strong>x² + 5x + 6</strong>", "<strong>(x + 2)(x + 3)</strong>", "twee getallen met <strong>som 5</strong> en product 6"],
                             ["<strong>x² − 7x + 12</strong>", "(x − 3)(x − 4)", "<strong>som 7</strong> en product 12"],
                             ["<strong>x² − 2x − 8</strong>", "<strong>(x − 4)(x + 2)</strong>", "som min 2 en product min 8"]])),
            ("p", "<strong>Niet elke veelterm van de tweede graad is te ontbinden in reële factoren</strong>: "
                  "dat lukt alleen als de discriminant niet negatief is. x² + 1 lukt dus niet in de reële "
                  "getallen."),
        ]),
        dict(kop="De vergelijking en haar discriminant", blokken=[
            ("p", "In een tweedegraadsvergelijking <strong>is de hoogste macht twee</strong>: de vorm is "
                  "<strong>ax² + bx + c = 0</strong>, met <strong>a niet nul</strong> — <strong>anders blijft "
                  "bx + c over, en dat is eerste graad</strong>."),
            ("p", "<strong>De discriminant is b² − 4ac.</strong> Ze <strong>geeft niet de oplossingen zelf "
                  "maar enkel het aantal</strong>; de oplossingen vind je daarna met de formule "
                  "<strong>min b, plus of min de wortel van D, gedeeld door 2a</strong>."),
            ("kader", tabel(["discriminant", "aantal reële oplossingen", "grafisch", "voorbeeld"],
                            [["<strong>positief</strong>", "<strong>twee</strong>", "de grafiek snijdt de x-as twee keer",
                              "<strong>x² − 5x + 6 heeft D = 1</strong> (25 − 24), met oplossingen 2 en 3"],
                             ["<strong>nul</strong>", "<strong>één</strong> (een dubbele wortel)", "de grafiek raakt de x-as",
                              "<strong>x² + 2x + 1 heeft D = 0</strong> (4 − 4), met x = min 1"],
                             ["<strong>negatief</strong>", "<strong>geen</strong>", "<strong>de grafiek snijdt de x-as niet</strong> en blijft er helemaal boven of onder",
                              "<strong>x² + 9 = 0 heeft geen reële oplossing</strong>: een kwadraat plus 9 is altijd groter dan nul"]])),
            ("p", "Twee vergelijkingen die je zonder formule oplost. <strong>x² = 49 geeft x = 7 of x = min "
                  "7</strong> — de negatieve oplossing vergeten is een klassieke fout. En <strong>x² − 4x = 0 "
                  "geeft x = 0 of x = 4</strong>: haal x buiten haakjes, want <strong>een product van twee "
                  "factoren is nul als minstens één factor nul is</strong>."),
            ("p", "Daarbij één waarschuwing: <strong>bij x² = 4x mag je niet door x delen, want x kan nul "
                  "zijn</strong>. Je zou de oplossing x = 0 kwijtspelen. Ontbind liever in factoren."),
        ]),
        dict(kop="Vraagstukken van de tweede graad", blokken=[
            ("p", "De stappen: <strong>de vergelijking opstellen</strong>, <strong>de discriminant "
                  "berekenen</strong> en <strong>de oplossingen toetsen aan het vraagstuk</strong>. Dat "
                  "laatste hoort er echt bij, want <strong>een vraagstuk van de tweede graad heeft niet "
                  "altijd twee bruikbare antwoorden</strong>: een negatieve lengte of tijd valt weg, en je "
                  "maakt ze niet positief."),
            ("p", "Een voorbeeld: <strong>een rechthoek met oppervlakte 40 waarvan de lengte 3 meer is dan de "
                  "breedte, heeft breedte 5</strong> (5 × 8 = 40). De andere oplossing is min 8, en die valt "
                  "weg."),
        ]),
    ])


# ───────────────────────── 12. Het functiebegrip en de eerstegraadsfunctie
zet("het-functiebegrip-en-de-eerstegraadsfunctie",
    titel="Het functiebegrip en de eerstegraadsfunctie",
    onder="Wat een functie is, domein en bereik, wat je uit een grafiek leest, en de eerstegraadsfunctie met haar richtingscoëfficiënt.",
    secties=[
        dict(kop="Wat een functie is", blokken=[
            ("p", "Een functie is een verband waarbij <strong>elke x precies één y krijgt</strong>: elk getal "
                  "uit het domein heeft juist één beeld. <strong>Eén x-waarde kan dus geen twee "
                  "verschillende beelden hebben</strong> — dan is het geen functie. Omgekeerd mag wel: "
                  "<strong>twee verschillende x-waarden mogen hetzelfde beeld hebben</strong>, zoals 2 en min "
                  "2 bij f(x) = x², die allebei 4 geven."),
            ("p", "Daarop steunt de <strong>verticale-lijntest</strong>: <strong>een verticale rechte mag de "
                  "grafiek maar in één punt snijden</strong>."),
            ("kader", tabel(["woord", "wat het betekent"],
                            [["<strong>het origineel</strong> (of het argument)", "<strong>de x-waarde waarvan je het beeld neemt</strong>"],
                             ["<strong>het beeld</strong>", "de bijhorende y-waarde; <strong>f(3) is het beeld van 3</strong>, en <strong>op de verticale as lees je de beelden af</strong>"],
                             ["<strong>het domein</strong>", "<strong>alle x-waarden die mogen</strong>"],
                             ["<strong>het bereik</strong>", "<strong>alle y-waarden die voorkomen</strong>"],
                             ["<strong>de nulwaarde</strong> (of het nulpunt)", "de x-waarde waar de grafiek de x-as snijdt, dus waar f(x) = 0"]])),
            ("p", "Rekenen met een voorschrift: <strong>voor f(x) = 2x + 1 is f(4) gelijk aan 9</strong>, en "
                  "<strong>voor f(x) = x² is f(min 3) gelijk aan 9</strong>, want een kwadraat is nooit "
                  "negatief. En <strong>als f(2) gelijk is aan 0, dan is 2 een nulwaarde</strong>: de grafiek "
                  "gaat door het punt (2, 0)."),
            ("p", "<strong>Het domein van elke functie is niet heel de reële rechte</strong>: over het domein "
                  "klopt dat <strong>het de x-waarden zijn</strong>, dat <strong>bij een breuk de noemer niet "
                  "nul mag zijn</strong> en dat <strong>bij een wortel wat eronder staat niet negatief mag "
                  "zijn</strong>."),
        ]),
        dict(kop="Vier manieren om een functie voor te stellen", blokken=[
            ("kader", tabel(["voorstelling", "wat ze geeft"],
                            [["<strong>een woordelijke beschrijving</strong>", "het verband in gewone taal"],
                             ["<strong>een tabel</strong>", "<strong>een rij x-waarden met hun beeld</strong>: boven de x, onder de beelden. Handig, maar nooit volledig"],
                             ["<strong>een grafiek</strong>", "het beeld in één oogopslag; punten noteer je als <strong>(1, 5)</strong>, <strong>eerst de x en dan de y</strong>"],
                             ["<strong>een voorschrift</strong>", "de regel zelf; <strong>het voordeel boven een tabel is dat je er elke x in kan invullen</strong>"]])),
            ("p", "Uit een grafiek lees je rechtstreeks af: <strong>de nulwaarden</strong>, <strong>waar de "
                  "functie stijgt</strong> en daalt, <strong>het hoogste punt</strong> en de andere extrema, "
                  "en het teken."),
        ]),
        dict(kop="De eerstegraadsfunctie", blokken=[
            ("p", "Haar voorschrift is <strong>f(x) = ax + b</strong>, met a niet nul, en haar grafiek is "
                  "<strong>altijd een rechte</strong>. Daarom <strong>teken je ze het snelst met twee punten "
                  "en een lat</strong>; een derde punt is een handige controle. En <strong>een "
                  "eerstegraadsfunctie kan geen twee nulwaarden hebben</strong>: een schuine rechte snijdt de "
                  "x-as precies één keer."),
            ("kader", tabel(["letter", "wat ze zegt"],
                            [["<strong>a, de richtingscoëfficiënt</strong>", "<strong>hoe steil de rechte loopt</strong>: de stijging per stap van 1 naar rechts"],
                             ["<strong>b</strong>", "<strong>het beeld van 0</strong>, dus f(0) en het snijpunt met de y-as"]])),
            ("p", "Over de richtingscoëfficiënt klopt: <strong>positief betekent stijgend</strong>, "
                  "<strong>negatief betekent dalend</strong> en <strong>nul geeft een horizontale "
                  "rechte</strong>. Het snijpunt met de y-as is b en niet a; b schuift de rechte enkel op of "
                  "neer."),
            ("p", "<strong>Uit twee punten bereken je a als het verschil in y gedeeld door het verschil in "
                  "x.</strong> Voor de rechte door <strong>(0, 1) en (2, 7)</strong> is dat <strong>6 : 2 = "
                  "3</strong>."),
            ("kader", tabel(["functie", "wat je meteen weet"],
                            [["<strong>f(x) = 3x − 2</strong>", "<strong>de richtingscoëfficiënt is 3</strong>: per stap naar rechts 3 omhoog"],
                             ["<strong>f(x) = min 2x + 7</strong>", "<strong>f(0) = 7</strong>; in nul blijft enkel b over"],
                             ["<strong>f(x) = min 3x + 4</strong>", "<strong>de functie is dalend</strong>, <strong>de grafiek snijdt de y-as in 4</strong> en <strong>de rechte zakt 3 per stap</strong>"],
                             ["<strong>f(x) = 2x − 6</strong>", "<strong>de nulwaarde is 3</strong>, want 2x = 6"],
                             ["<strong>f(x) = x + 5</strong>", "<strong>de nulwaarde is min 5</strong>"]])),
        ]),
        dict(kop="Recht en omgekeerd evenredig", blokken=[
            ("p", "<strong>Een recht evenredig verband is f(x) = ax, met b gelijk aan nul.</strong> Dan "
                  "<strong>gaat de grafiek door de oorsprong</strong>, want f(0) = 0, en dubbel zoveel x "
                  "geeft dubbel zoveel y."),
            ("p", "<strong>Bij een omgekeerd evenredig verband is de grafiek geen rechte maar een "
                  "hyperbool</strong>: daar blijft het product van x en y gelijk."),
        ]),
    ])


# ───────────────────────── 13. De tweedegraadsfunctie en haar parabool
zet("de-tweedegraadsfunctie-en-haar-parabool",
    titel="De tweedegraadsfunctie en haar parabool",
    onder="De parabool met haar top en symmetrieas, wat je uit het voorschrift leest, de topvorm en de verschuivingen, en het onderzoek van de functie.",
    secties=[
        dict(kop="De parabool", blokken=[
            ("p", "Het voorschrift is <strong>f(x) = ax² + bx + c</strong>, met a niet nul, en de grafiek "
                  "heet <strong>een parabool</strong>. Ze ligt spiegelgelijk rond haar "
                  "<strong>symmetrieas</strong>, de verticale rechte door de top; <strong>de top ligt dus "
                  "altijd op de symmetrieas</strong>."),
            ("p", "<strong>De top is het hoogste of het laagste punt.</strong> <strong>Bij een positieve a "
                  "opent de parabool naar boven</strong> en is de top het laagste punt; <strong>bij een "
                  "negatieve a is de top juist het hoogste punt</strong>."),
            ("kader", tabel(["wat je zoekt", "waar je het leest", "voorbeeld"],
                            [["<strong>de opening</strong>", "<strong>het teken van a</strong>", "bij min x² + 4 opent ze naar onder"],
                             ["<strong>het snijpunt met de y-as</strong>", "<strong>de waarde van c</strong>, want f(0) = c",
                              "<strong>2x² − 8 snijdt de y-as in (0, min 8)</strong>"],
                             ["<strong>de x-waarde van de top</strong>", "<strong>min b gedeeld door 2a</strong> (die formule staat in het formularium)",
                              "<strong>x² − 4x + 3 heeft top-x 2</strong>; <strong>x² − 6x heeft top-x 3</strong>"],
                             ["<strong>de y-waarde van de top</strong>", "die top-x invullen",
                              "<strong>f(2) = 4 − 8 + 3 = min 1, dus de top is (2, min 1)</strong>"],
                             ["<strong>de nulwaarden</strong>", "<strong>f(x) gelijk aan nul stellen</strong> en de vergelijking oplossen", "de snijpunten met de x-as"]])),
            ("p", "<strong>De top van f(x) = x² ligt in (0, 0)</strong>, de eenvoudigste parabool van "
                  "allemaal."),
            ("p", "<strong>Een parabool heeft niet altijd twee snijpunten met de x-as</strong>: dat hangt van "
                  "de discriminant af, dus twee, één of geen. <strong>Ligt de top op de x-as, dan is er "
                  "precies één nulwaarde</strong> en is de discriminant nul. En <strong>f(x) = x² + 2 heeft "
                  "er geen</strong>: haar top ligt in (0, 2) en ze opent naar boven, dus ze blijft boven de "
                  "x-as."),
            ("p", "Uit <strong>f(x) = min x² + 4</strong> lees je in één keer: <strong>de parabool opent naar "
                  "onder</strong>, <strong>de top ligt in (0, 4)</strong> en <strong>er zijn twee "
                  "nulwaarden</strong>, namelijk 2 en min 2."),
        ]),
        dict(kop="De topvorm en de verschuivingen", blokken=[
            ("p", "<strong>In de topvorm a(x − p)² + q is de top het punt (p, q).</strong> Daarom is die vorm "
                  "zo handig: je leest de top zonder te rekenen. <strong>De top van (x − 4)² + 1 is "
                  "(4, 1)</strong>, en <strong>x² − 4x + 3 wordt in topvorm (x − 2)² − 1</strong>."),
            ("kader", tabel(["wat je verandert", "wat er met de basisparabool gebeurt"],
                            [["<strong>x² + 3</strong>", "<strong>ze schuift 3 omhoog</strong>: een getal buiten het kwadraat verschuift verticaal"],
                             ["<strong>(x − 2)²</strong>", "<strong>ze schuift 2 naar rechts</strong>; dat voelt omgekeerd aan, maar de top ligt in x = 2"],
                             ["<strong>min x²</strong>", "<strong>ze spiegelt om de x-as</strong>: elke y-waarde keert om, dus ze opent naar onder"],
                             ["<strong>a × x² met a groter dan 1</strong>", "<strong>de parabool wordt smaller</strong>, dus steiler"],
                             ["<strong>a tussen 0 en 1</strong>", "<strong>ze wordt breder</strong>, dus vlakker"]])),
            ("p", "Uit <strong>f(x) = (x + 1)² − 2</strong> lees je dus: <strong>één naar links</strong>, "
                  "<strong>twee omlaag</strong>, en <strong>de top ligt in (min 1, min 2)</strong>."),
            ("p", "Twee dingen die je niet mag verwarren. <strong>De factor a verandert de plaats van de top "
                  "niet</strong>: bij f(x) = a × x² blijft de top in de oorsprong, alleen de breedte "
                  "verandert. En <strong>een verschuiving naar boven laat de nulwaarden niet "
                  "onveranderd</strong>: de grafiek komt hoger te liggen, dus de snijpunten met de x-as "
                  "verschuiven of verdwijnen. <strong>Bij een verschuiving naar rechts veranderen wél niet: "
                  "de vorm</strong>, <strong>de breedte</strong> en <strong>de richting van de "
                  "opening</strong> — alleen de plaats van de top verandert."),
        ]),
        dict(kop="De functie onderzoeken", blokken=[
            ("p", "Bij een functieonderzoek ga je na: <strong>de nulwaarden</strong>, <strong>waar de functie "
                  "stijgt en daalt</strong>, <strong>het extremum</strong> en het teken. Een grafiek heeft "
                  "geen lengte, dus die hoort er niet bij."),
            ("p", "<strong>Het extremum is de y-waarde van de top</strong>: <strong>een parabool die naar "
                  "boven opent heeft een minimum</strong>, een die naar onder opent een maximum. En "
                  "<strong>f(x) = x² stijgt rechts van de top</strong>; links daalt ze, want de top is het "
                  "keerpunt."),
            ("p", "<strong>Een tekenonderzoek is nagaan waar f(x) positief is</strong>: boven de x-as "
                  "positief, eronder negatief. <strong>f(x) = x² − 4 is negatief tussen min 2 en 2</strong>, "
                  "want tussen de twee nulwaarden ligt de parabool onder de as."),
        ]),
    ])


# ───────────────────────── 14. Telproblemen en problemen oplossen
zet("telproblemen-en-problemen-oplossen",
    titel="Telproblemen en problemen oplossen",
    onder="Het boomdiagram en het venndiagram, de som-, product- en complementregel, en de vierslag om een vraagstuk aan te pakken.",
    secties=[
        dict(kop="De drie telregels", blokken=[
            ("p", "De vakfiche noemt er <strong>drie</strong>: <strong>de somregel</strong>, <strong>de "
                  "productregel</strong> en <strong>de complementregel</strong>. Een wortelregel bestaat "
                  "hier niet."),
            ("kader", tabel(["regel", "wanneer je ze gebruikt", "voorbeeld"],
                            [["<strong>de productregel</strong>", "<strong>bij keuzes na elkaar</strong>: vermenigvuldigen",
                              "<strong>3 truien en 4 broeken geven 12 combinaties</strong>"],
                             ["<strong>de somregel</strong>", "<strong>bij keuzes die elkaar uitsluiten</strong>: het een of het ander, maar niet beide",
                              "de aantallen optellen"],
                             ["<strong>de complementregel</strong>", "<strong>tel het tegendeel en trek het af</strong> van het totaal",
                              "<strong>het complement van minstens één keer kop is twee keer munt</strong>"]])),
            ("p", "<strong>De somregel mag je niet gebruiken als de twee gevallen kunnen samenvallen</strong>: "
                  "dan tel je de overlap dubbel, en moet je ze aftrekken."),
            ("kader", tabel(["telprobleem", "antwoord", "rekenwijze"],
                            [["<strong>twee dobbelstenen</strong>", "<strong>36 uitkomsten</strong>", "6 × 6"],
                             ["<strong>een munt en een dobbelsteen</strong>", "<strong>12 uitkomsten</strong>", "2 × 6"],
                             ["<strong>drie keer een munt</strong>", "<strong>8 uitkomsten</strong>", "2 × 2 × 2"],
                             ["<strong>3 kinderen in een rij zetten</strong>", "<strong>6 manieren</strong>", "3 × 2 × 1: na elke keuze blijft er één kind minder over"],
                             ["<strong>pincodes van 4 cijfers</strong>", "<strong>10 000</strong>", "10 × 10 × 10 × 10: elk cijfer mag opnieuw"]])),
        ]),
        dict(kop="Boomdiagram en venndiagram", blokken=[
            ("p", "<strong>Een boomdiagram is een schema van alle mogelijkheden</strong>: elke tak is een "
                  "keuze, en door de takken te volgen tel je alles. Het is handig <strong>bij keuzes na "
                  "elkaar</strong>, <strong>bij een klein aantal mogelijkheden</strong> en <strong>om geen "
                  "geval te vergeten</strong>. Het telt mogelijkheden; gemiddelden berekent het niet."),
            ("p", "<strong>Een venndiagram toont overlappende groepen</strong>: twee of drie cirkels met hun "
                  "overlap. <strong>In de overlap staat wat in beide verzamelingen zit</strong>, en net "
                  "daarom zie je er dubbele tellingen in. <strong>Je telt die overlap niet twee keer "
                  "mee</strong>: je telt de twee groepen op en trekt de overlap één keer af."),
            ("kader", tabel(["situatie", "antwoord", "rekenwijze"],
                            [["<strong>12 kinderen voetballen, 9 zwemmen, 4 doen beide</strong>", "<strong>17 doen sport</strong>", "12 + 9 = 21, min de 4 die je dubbel telde"],
                             ["<strong>van 30 leerlingen spreken er 18 Frans en 7 twee talen</strong>", "<strong>11 spreken enkel Frans</strong>", "18 − 7"]])),
            ("p", "De fouten die je makkelijk maakt: <strong>gevallen dubbel tellen</strong>, <strong>een "
                  "geval vergeten</strong> en <strong>optellen in plaats van vermenigvuldigen</strong>. "
                  "Daarom helpt een schema zo: het maakt dubbels zichtbaar."),
        ]),
        dict(kop="Een probleem aanpakken", blokken=[
            ("p", "De klassieke vierslag: <strong>begrijpen wat gevraagd is</strong>, <strong>een plan "
                  "kiezen</strong>, <strong>het plan uitvoeren en controleren</strong>. <strong>De eerste "
                  "stap is dus de vraag goed lezen</strong>: wat is gegeven en wat is gevraagd? En "
                  "<strong>een vraagstuk heeft niet altijd maar één oplossingsweg</strong>; de fiche vraagt "
                  "net dat je een weg kiest en verantwoordt."),
            ("p", "<strong>Een heuristiek is een hulpmiddel om te zoeken</strong>: geen recept, maar een "
                  "manier van aanpakken."),
            ("kader", tabel(["heuristiek", "wat ze doet"],
                            [["<strong>een tekening of schema maken</strong>", "<strong>helpt ook zonder meetkunde</strong>: het maakt een verband zichtbaar dat in woorden verborgen zit"],
                             ["<strong>het probleem eerst vereenvoudigen</strong>", "<strong>een eenvoudiger geval proberen</strong> met kleine getallen; het patroon werkt vaak ook groot"],
                             ["<strong>van achteren naar voren werken</strong>", "<strong>terugwerken</strong>: je begint bij de gevraagde uitkomst en draait elke stap om"],
                             ["<strong>een tabel maken</strong>", "<strong>handig om een patroon op het spoor te komen</strong>: de gevallen staan naast elkaar"]])),
            ("p", "<strong>Schatten vóór je rekent is je controle</strong>: wijkt je uitkomst er ver van af, "
                  "dan zoek je de fout. Je merkt zo <strong>een rare uitkomst</strong> meteen."),
            ("p", "<strong>Op het einde controleer je.</strong> De vragen daarbij: <strong>is dit een "
                  "antwoord op de vraag</strong>, <strong>klopt de grootteorde</strong> en <strong>staat de "
                  "eenheid erbij</strong>? <strong>De eenheid mag je niet weglaten</strong>: 5 meter is niet "
                  "hetzelfde als 5 seconden. En <strong>een onmogelijke uitkomst, zoals een negatieve "
                  "leeftijd, wijst op een fout of op een oplossing die wegvalt</strong>."),
            ("p", "<strong>Je stappen opschrijven helpt je je fout te vinden</strong>, en de verbetering ziet "
                  "hoe je gedacht hebt. Op het examen levert dat punten op."),
            ("kader", tabel(["vraagstuk", "antwoord", "rekenwijze"],
                            [["<strong>ik denk aan een getal, tel er 5 bij en verdubbel; ik krijg 26</strong>", "<strong>8</strong>",
                              "terugwerken: 26 halveren is 13, min 5 is 8"],
                             ["<strong>een trui van 40 euro met 25 procent korting</strong>", "<strong>30 euro</strong>", "25 % van 40 is 10"],
                             ["<strong>een trui kost na 20 procent korting 40 euro</strong>", "<strong>de oude prijs was 50 euro</strong>", "40 is 80 % van de oude prijs, dus 40 : 0,8"],
                             ["<strong>10 procent van 250</strong>", "<strong>25</strong>", "tien procent nemen is delen door tien"],
                             ["<strong>drie vrienden delen 18 euro, één krijgt het dubbele van elk van de andere twee</strong>", "<strong>hij krijgt 9 euro</strong>",
                              "samen vier gelijke delen: 18 : 4 = 4,5, en het dubbele is 9"]])),
        ]),
    ])


# ───────────────────────── 15. Gegevens weergeven en samenvatten
zet("gegevens-weergeven-en-samenvatten",
    titel="Gegevens weergeven en samenvatten",
    onder="Categorische en numerieke gegevens, de frequentietabel, de grafiek die bij je gegevens past, de centrummaten en de spreidingsmaten, en hoe een grafiek je om de tuin kan leiden.",
    secties=[
        dict(kop="Twee soorten gegevens", blokken=[
            ("p", "Voor je iets tekent of berekent, kijk je eerst <strong>wat voor gegevens je hebt</strong>. "
                  "<strong>Categorische gegevens zijn gegevens in groepen</strong>: haarkleur, vervoermiddel, "
                  "lievelingsvak. Je kan ze tellen, maar <strong>je kan ze niet zinvol optellen</strong>: het "
                  "gemiddelde van blauw en groen bestaat niet. <strong>Numerieke gegevens zijn gegevens die je "
                  "meet of telt</strong>: lengte, leeftijd, het aantal broers en zussen. <strong>Daarmee kan "
                  "je wél rekenen.</strong>"),
            ("kader", tabel(["gegeven", "soort"],
                            [["<strong>de lengte in centimeter</strong>", "<strong>numeriek</strong>, je meet ze"],
                             ["<strong>het aantal broers en zussen</strong>", "<strong>numeriek</strong>, je telt ze"],
                             ["<strong>de leeftijd in jaren</strong>", "<strong>numeriek</strong>, je telt ze"],
                             ["<strong>de haarkleur</strong>", "<strong>categorisch</strong>, het is een groep"],
                             ["<strong>het vervoermiddel naar school</strong>", "<strong>categorisch</strong>, het is een groep"]])),
            ("p", "<strong>De frequentietabel zet elke waarde met haar aantal op een rij</strong>: links de "
                  "waarden, rechts hoe vaak ze voorkomen. <strong>De som van de frequenties is gelijk aan het "
                  "aantal gegevens</strong>, en dat is meteen je controle: komt die som niet uit, dan ben je "
                  "een gegeven vergeten."),
            ("p", "<strong>Zijn er te veel verschillende waarden, dan werk je met klassen.</strong> Bij "
                  "lengtes van 1,52 tot 1,89 meter heeft bijna elke leerling een eigen waarde; dan groepeer "
                  "je in klassen, bijvoorbeeld van 5 centimeter. <strong>Voor lengtes van 150 tot 190 "
                  "centimeter heb je vier klassen van 10 centimeter nodig</strong>: 150 tot 160, 160 tot 170, "
                  "170 tot 180 en 180 tot 190."),
            ("p", "<strong>De relatieve frequentie is het aandeel, meestal in procent</strong>: de frequentie "
                  "gedeeld door het totaal. <strong>Komen 20 van de 50 leerlingen met de bus, dan is de "
                  "relatieve frequentie 40 procent</strong>, want 20 : 50 = 0,4. Dat getal laat je twee groepen "
                  "van verschillende grootte toch vergelijken."),
            ("weetje", "Een percentage verzwijgt hoeveel gegevens erachter zitten. “67 procent beveelt het "
                       "aan” klinkt sterk, tot je leest dat er drie mensen bevraagd werden."),
        ]),
        dict(kop="De grafiek die bij je gegevens past", blokken=[
            ("p", "Elke grafiek hoort bij een soort gegevens. <strong>Kies je de verkeerde, dan is je grafiek "
                  "niet fout gerekend maar wel onleesbaar.</strong>"),
            ("kader", tabel(["grafiek", "waarvoor", "hoe ze eruitziet"],
                            [["<strong>staafdiagram</strong>", "<strong>categorische gegevens</strong>", "<strong>losse staven met ruimte ertussen</strong>, één per categorie"],
                             ["<strong>histogram</strong>", "<strong>numerieke gegevens in klassen</strong>", "<strong>staven tegen elkaar</strong>, want de klassen sluiten aan"],
                             ["<strong>cirkeldiagram</strong>", "<strong>delen van een geheel</strong>", "<strong>partjes die samen 100 procent vormen</strong>"],
                             ["<strong>lijndiagram</strong>", "<strong>een verloop in de tijd</strong>", "<strong>een lijn die opeenvolgende momenten verbindt</strong>"],
                             ["<strong>dotplot</strong>", "<strong>een kleine reeks metingen</strong>", "<strong>één stip per gegeven</strong>, zo zie je meteen de vorm"],
                             ["<strong>boxplot</strong>", "<strong>de spreiding van een reeks</strong>", "<strong>de kwartielen en de mediaan</strong> in één beeld"]])),
            ("p", "<strong>Het verschil tussen een staafdiagram en een histogram zit in die ruimte.</strong> "
                  "Bij een staafdiagram staan de staven los, want de categorieën staan los van elkaar. "
                  "<strong>Bij een histogram staan de staven tegen elkaar</strong>, want 160 tot 170 sluit aan "
                  "op 170 tot 180."),
            ("p", "<strong>Een cirkeldiagram is niet geschikt om twintig categorieën te vergelijken</strong>: "
                  "twintig partjes zijn niet van elkaar te onderscheiden. Een staafdiagram leest dan veel "
                  "beter. En <strong>een spreidingsdiagram toont geen verloop in de tijd</strong>, dat doet "
                  "een lijndiagram; daarover gaat het volgende hoofdstuk."),
            ("p", "<strong>Op elke grafiek horen drie dingen te staan</strong>: <strong>een titel</strong>, "
                  "<strong>een naam bij elke as</strong> en <strong>de eenheid van de getallen</strong>. "
                  "<strong>Zonder naam bij de as en zonder eenheid is een grafiek niet te lezen.</strong>"),
        ]),
        dict(kop="De centrummaten", blokken=[
            ("p", "<strong>Een centrummaat vat een hele reeks samen in één getal.</strong> Er zijn er drie, en "
                  "ze zeggen elk iets anders."),
            ("kader", tabel(["maat", "wat ze is", "voorbeeld"],
                            [["<strong>het gemiddelde</strong>", "<strong>de som gedeeld door het aantal</strong>",
                              "<strong>4, 6 en 8 hebben gemiddelde 6</strong>, want 18 : 3 = 6"],
                             ["<strong>de mediaan</strong>", "<strong>de middelste waarde</strong> als je ze van klein naar groot zet",
                              "<strong>de mediaan van 3, 5, 9, 11 en 12 is 9</strong>: vijf waarden, dus de derde"],
                             ["<strong>de modus</strong>", "<strong>de meest voorkomende waarde</strong>",
                              "<strong>ook bij categorische gegevens</strong>: de meest gekozen kleur"]])),
            ("p", "<strong>Bij een even aantal waarden neem je voor de mediaan het gemiddelde van de twee "
                  "middelste.</strong> <strong>De mediaan van 2, 4, 6 en 10 is dus 5</strong>: 4 + 6 = 10, en "
                  "10 : 2 = 5."),
            ("p", "<strong>Er kunnen ook twee modi zijn</strong>, als twee waarden even vaak voorkomen. En "
                  "<strong>de modus bestaat niet enkel bij numerieke gegevens</strong>: ook bij een kleur of "
                  "een vervoermiddel is er een waarde die het vaakst gekozen wordt."),
            ("p", "<strong>Bij een uitschieter zegt de mediaan meer dan het gemiddelde.</strong> Neem de "
                  "reeks 6, 7, 7, 8 en 32. <strong>Het gemiddelde is 12</strong>, want de som is 60; "
                  "<strong>de mediaan is 7</strong>. Niemand van de eerste vier zit in de buurt van 12: "
                  "<strong>die ene uitschieter trekt het gemiddelde mee omhoog, terwijl de mediaan amper "
                  "beweegt</strong>, want die ligt vast door de middelste waarde."),
            ("fig", svg.middelmaten([6, 7, 7, 8, 32]),
             "De vier lage waarden liggen dicht bij de mediaan, en het gemiddelde ligt een stuk rechts van "
             "alle vier."),
            ("p", "<strong>Een gemiddelde zegt dus niet altijd genoeg over een groep.</strong> Twee groepen "
                  "met hetzelfde gemiddelde kunnen heel anders gespreid zijn: daarvoor heb je de "
                  "spreidingsmaten nodig."),
        ]),
        dict(kop="De spreidingsmaten", blokken=[
            ("p", "<strong>Een spreidingsmaat zegt hoe ver de gegevens uiteen liggen.</strong> Ook hier zijn "
                  "er drie."),
            ("kader", tabel(["maat", "wat ze is", "voorbeeld"],
                            [["<strong>de variatiebreedte</strong>", "<strong>het grootste min het kleinste</strong>",
                              "<strong>bij 7, 12 en 20 is ze 13</strong>, want 20 − 7 = 13"],
                             ["<strong>de interkwartielafstand</strong>", "<strong>het derde kwartiel min het eerste</strong>",
                              "<strong>de breedte van de middelste helft</strong>; uitschieters tellen er niet in mee"],
                             ["<strong>de standaardafwijking</strong>", "<strong>hoe ver de gegevens gemiddeld van het gemiddelde liggen</strong>",
                              "<strong>klein</strong> is dicht bij het gemiddelde, <strong>groot</strong> is sterk gespreid"]])),
            ("p", "<strong>De boxplot tekent de spreiding.</strong> Je leest er <strong>de kwartielen en de "
                  "mediaan</strong> op af, en daarmee ook het minimum en het maximum: vijf getallen in één "
                  "beeld. <strong>De doos is de middelste helft van de gegevens</strong>, de streep erin is de "
                  "mediaan."),
            ("fig", svg.boxplot([2, 5, 6, 7, 8, 10, 11, 12, 14, 15, 20]),
             "Deze reeks loopt van 2 tot 20, de middelste helft ligt tussen 6 en 14, en de mediaan ligt op 10."),
            ("p", "Bij die reeks is <strong>de variatiebreedte 18</strong> (20 − 2) en <strong>de "
                  "interkwartielafstand 8</strong> (14 − 6). <strong>De interkwartielafstand is dus een stuk kleiner "
                  "dan de variatiebreedte, en net dat is haar nut</strong>: ze kijkt enkel naar de middelste "
                  "helft en laat de uiteinden links liggen."),
            ("weetje", "Op een boxplot zie je niet hoeveel gegevens erachter zitten. Een doos van tien "
                       "metingen ziet er precies hetzelfde uit als een doos van duizend."),
        ]),
        dict(kop="Een grafiek kritisch lezen", blokken=[
            ("p", "<strong>Een grafiek kan kloppen en toch misleiden.</strong> De bekendste manier is "
                  "<strong>een afgeknotte as</strong>: <strong>een y-as die niet bij nul begint kan een klein "
                  "verschil groot doen lijken</strong>. Zet je twee staven van 98 en 100 op een as die bij 97 "
                  "begint in plaats van bij nul, dan steekt de ene er 1 boven uit en de andere 3: "
                  "<strong>de tweede staaf lijkt zo drie keer zo hoog als de eerste</strong>, terwijl ze "
                  "maar 2 procent verschillen."),
            ("kader", tabel(["waar je op let", "waarom"],
                            [["<strong>waar de assen beginnen</strong>", "<strong>een afgeknotte as blaast een verschil op</strong>"],
                             ["<strong>welke eenheid er staat</strong>", "<strong>zonder eenheid betekent een getal niets</strong>"],
                             ["<strong>hoeveel gegevens erachter zitten</strong>", "<strong>een percentage van 4 mensen zegt iets heel anders dan een percentage van 4000</strong>"]])),
            ("p", "<strong>Dat kritisch lezen is zelf leerstof.</strong> Op het examen krijg je een grafiek "
                  "en de vraag wat je eruit mag besluiten; <strong>het juiste antwoord is vaak dat je er "
                  "minder uit mag besluiten dan de grafiek suggereert</strong>."),
        ]),
    ])


# ───────────────────────── 16. Verbanden tussen twee grootheden
zet("verbanden-tussen-twee-grootheden",
    titel="Verbanden tussen twee grootheden",
    onder="Het spreidingsdiagram en de puntenwolk, de trendlijn en wat je ermee mag voorspellen, de correlatiecoëfficiënt, en waarom samenhang nog geen oorzaak is.",
    secties=[
        dict(kop="Het spreidingsdiagram", blokken=[
            ("p", "Tot nu ging het over één grootheid tegelijk. <strong>Wil je twee grootheden naast elkaar "
                  "leggen, dan teken je een spreidingsdiagram: één punt per meetpaar.</strong> <strong>Elk punt "
                  "heeft twee waarden</strong>, een op de x-as en een op de y-as. <strong>Er horen dus twee "
                  "waarden bij elk punt</strong>, en die twee komen van dezelfde persoon of hetzelfde voorwerp."),
            ("p", "<strong>De wolk punten noem je de puntenwolk</strong>, en haar vorm verraadt het verband. "
                  "<strong>Je gebruikt een spreidingsdiagram net om een verband tussen twee grootheden te "
                  "zien</strong>: je merkt meteen of de punten een richting hebben."),
            ("fig", svg.puntenwolk([(152, 36), (156, 37), (160, 38), (163, 38), (165, 39),
                                    (168, 40), (170, 41), (174, 41), (178, 43), (182, 44)],
                                   xlabel="lengte in cm", ylabel="schoenmaat"),
             "Tien leerlingen: de kleinste meet 152 centimeter en heeft maat 36, de grootste meet 182 "
             "centimeter en heeft maat 44."),
            ("kader", tabel(["wat je ziet", "wat het betekent"],
                            [["<strong>de punten stijgen</strong>", "<strong>een positief verband</strong>: hoe hoger x, hoe hoger y"],
                             ["<strong>de punten dalen</strong>", "<strong>een negatief verband</strong>: hoe hoger x, hoe lager y"],
                             ["<strong>geen richting</strong>", "<strong>geen verband</strong>: de punten liggen verspreid"]])),
            ("p", "<strong>In een spreidingsdiagram van lengte en schoenmaat stijgen de punten: grotere "
                  "mensen hebben een grotere maat.</strong> Een dalend verband vind je bijvoorbeeld tussen "
                  "schermtijd en uren slaap. <strong>Een spreidingsdiagram toont geen verloop in de tijd</strong>, "
                  "dat doet een lijndiagram, uit het vorige hoofdstuk."),
            ("p", "<strong>Drie dingen lees je uit een spreidingsdiagram</strong>: <strong>de richting van het "
                  "verband</strong>, <strong>hoe sterk het verband is</strong> en <strong>of er uitschieters "
                  "zijn</strong>. Een percentage lees je er niet uit."),
            ("p", "<strong>Bij een goed spreidingsdiagram staat er een naam bij elke as, de eenheid erbij en "
                  "een passende schaal.</strong> <strong>De punten verbinden hoort er niet bij</strong>: dan "
                  "maak je er een lijndiagram van, en dat zegt iets anders."),
        ]),
        dict(kop="De trendlijn", blokken=[
            ("p", "<strong>De trendlijn is de rechte die het patroon van de puntenwolk volgt.</strong> "
                  "<strong>Ze loopt zo dicht mogelijk bij alle punten, zonder er per se door te gaan</strong>: "
                  "<strong>een trendlijn hoeft niet door alle punten te gaan</strong>, en door alle punten gaan "
                  "lukt meestal niet eens."),
            ("p", "<strong>Teken je ze met de hand, dan leg je ze zo dat er evenveel punten boven als onder "
                  "liggen.</strong> Zo ligt ze zo dicht mogelijk bij de hele wolk. Op de grafische "
                  "rekenmachine laat je ze berekenen; dan krijg je er meteen de vergelijking bij."),
            ("p", "<strong>Waarvoor dient ze? Om een voorspelling te doen.</strong> <strong>Met haar "
                  "vergelijking schat je een y bij een x die je niet gemeten hebt.</strong> In de tekening "
                  "hierboven lees je zo af welke maat je verwacht bij iemand van 172 centimeter."),
            ("kader", tabel(["valkuil", "waarom"],
                            [["<strong>ver buiten de gemeten waarden voorspellen</strong>", "<strong>het verband kan daar anders zijn</strong>: buiten het bereik van je metingen weet je niet of de rechte nog klopt"],
                             ["<strong>een uitschieter laten staan zonder te kijken</strong>", "<strong>één punt ver weg kan de trendlijn flink doen kantelen</strong>"],
                             ["<strong>een rechte opleggen aan een kromme wolk</strong>", "<strong>een trendlijn is niet altijd een rechte</strong>; vaak wel, maar een verband kan ook krom zijn"]])),
            ("p", "<strong>Kijk dus altijd eerst naar de wolk zelf</strong>, en pas daarna naar de rechte. "
                  "Daarom begint elke oefening met tekenen en niet met rekenen."),
            ("weetje", "Een trendlijn heet ook een regressielijn. Dat woord komt van een onderzoek uit 1886 "
                       "over de lengte van ouders en kinderen, waarin de kinderen telkens naar het gemiddelde "
                       "toe “terugkeerden”."),
        ]),
        dict(kop="De correlatiecoëfficiënt", blokken=[
            ("p", "<strong>Correlatie is samenhang tussen twee grootheden</strong>, meer niet. <strong>De "
                  "correlatiecoëfficiënt zet die samenhang in één getal</strong>, en <strong>dat getal ligt "
                  "altijd tussen min 1 en 1</strong>."),
            ("kader", tabel(["waarde", "wat ze zegt"],
                            [["<strong>1</strong>", "<strong>een perfect stijgend verband</strong>: alle punten liggen precies op een stijgende rechte"],
                             ["<strong>0,9</strong>", "<strong>een sterk stijgend verband</strong>: de punten liggen bijna op een stijgende rechte"],
                             ["<strong>0,1</strong>", "<strong>bijna geen verband</strong>: de punten liggen bijna richtingloos"],
                             ["<strong>0</strong>", "<strong>geen lineair verband</strong>: de punten liggen zonder richting verspreid"],
                             ["<strong>−0,8</strong>", "<strong>een sterk dalend verband</strong>"],
                             ["<strong>−1</strong>", "<strong>een perfect dalend verband</strong>"]])),
            ("p", "Onthoud de twee helften van dat getal: <strong>het teken geeft de richting, de grootte "
                  "geeft de sterkte</strong>. <strong>Een correlatie van min 1 is dus niet zwakker dan een van "
                  "0,5, maar net het sterkst mogelijke verband</strong>; <strong>de sterkst mogelijke waarden "
                  "zijn 1 en min 1</strong>. Kijk naar de grootte, niet naar het teken."),
            ("p", "<strong>Bij de tien leerlingen hierboven is de correlatiecoëfficiënt ongeveer 0,99</strong>: "
                  "bijna 1, en inderdaad liggen de punten bijna op een rechte."),
            ("p", "<strong>Eén beperking telt altijd mee: de correlatiecoëfficiënt zegt enkel iets over een "
                  "lineair verband.</strong> <strong>Een duidelijk krom verband kan toch een correlatie dicht "
                  "bij nul geven</strong>, en dan is nul niet “geen verband” maar “geen rechte”. Opnieuw: eerst "
                  "de wolk bekijken."),
        ]),
        dict(kop="Correlatie is geen causaliteit", blokken=[
            ("p", "<strong>Dit is het hart van het hoofdstuk: correlatie is geen causaliteit.</strong> "
                  "<strong>Samen bewegen is niet hetzelfde als elkaar veroorzaken</strong>, en <strong>een "
                  "sterke correlatie bewijst dus niet dat het ene het andere veroorzaakt</strong>."),
            ("kader", tabel(["mogelijke verklaring", "voorbeeld"],
                            [["<strong>het ene veroorzaakt het andere</strong>", "<strong>meer uren studeren en een beter resultaat</strong>"],
                             ["<strong>een derde factor verklaart beide</strong>", "<strong>ijsjes en zwemongevallen</strong>: de warmte duwt beide omhoog"],
                             ["<strong>het is toeval</strong>", "<strong>twee reeksen die een tijdlang toevallig samen stijgen</strong>"]])),
            ("p", "<strong>Een derde factor is iets dat beide verklaart</strong>, ook wel een "
                  "<strong>verstorende factor</strong> genoemd. <strong>Het aantal ijsjes "
                  "en het aantal zwemongevallen stijgen samen omdat het warm weer is</strong>, niet omdat "
                  "ijsjes gevaarlijk zijn. <strong>Stijgen het aantal ooievaars en het aantal geboorten samen "
                  "in een land, dan besluit je dus enkel dat er samenhang is</strong>: het bekendste "
                  "schijnverband uit de handboeken."),
            ("p", "<strong>Hoe toon je een oorzakelijk verband dan wel aan? Met een opgezet experiment</strong>: "
                  "je verandert één ding en houdt de rest gelijk. <strong>Dat kan een grafiek niet.</strong> "
                  "En <strong>voor je uit een grafiek een oorzaak besluit, zoek je naar een verklaring</strong>: "
                  "<strong>een verband zonder plausibele verklaring blijft een vermoeden</strong>."),
            ("p", "<strong>Uit een correlatiecoëfficiënt van 0,95 mag je drie dingen besluiten</strong>: "
                  "<strong>de punten liggen dicht bij een rechte</strong>, <strong>het verband is "
                  "stijgend</strong> en <strong>voorspellen lukt hier redelijk goed</strong>. <strong>Over "
                  "oorzaak zegt dat getal niets.</strong>"),
            ("weetje", "Er bestaan hele verzamelingen van zulke schijnverbanden, bijvoorbeeld tussen het "
                       "aantal films met een bepaalde acteur en het aantal echtscheidingen in een staat. "
                       "Zoek er lang genoeg, en je vindt altijd twee reeksen die samen bewegen."),
        ]),
    ])

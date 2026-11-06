# -*- coding: utf-8 -*-
"""De leerbundels voor natuurwetenschappen, richting welzijnswetenschappen (🌍 Beyond).

De vakfiche natuurwetenschappen voor welzijnswetenschappen (3de graad
doorstroom, 2027) bevat alles van de gewone fiche, waarvoor de bundels al in
maak_natuurwetenschappen_beyond.py staan, plus één extra blok biologie:
"Stofwisselingsfysiologie en secretie". Hier staan enkel de bundels van dat
blok, één per thema (Kim, 6 november 2026).

De hoofdstukken staan in een apart vak "Natuurwetenschappen
welzijnswetenschappen", categorie Beyond doorstroom, en heten "<thema> — deel
1/2". Eén bundel per thema, dus Kim uploadt elke pdf bij beide delen. De
bestandsnaam eindigt op "-beyond-doorstroom", zodat /beheer/leerstof enkel bij
die categorie zoekt.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. De vragen staan in ../../beyond/bron/ww_*.py.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Natuurwetenschappen welzijnswetenschappen"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 1. Enzymen
BUNDELS["enzymen-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Enzymen",
    onder="Wat een enzym is, hoe het werkt volgens het sleutel-slotprincipe, en wat zijn werking versnelt of remt.",
    secties=[
        dict(kop="Wat is een enzym?", blokken=[
            ("p", "Een <strong>enzym</strong> is een <strong>eiwit</strong> dat een reactie in het lichaam "
                  "<strong>versnelt zonder zelf verbruikt te worden</strong>. Daarom noemt men een enzym een "
                  "<strong>biokatalysator</strong>: een katalysator die in een levend organisme werkt. Na de "
                  "reactie <strong>komt het enzym onveranderd terug</strong> en kan het meteen een volgende "
                  "molecule omzetten. <strong>Eén enzymmolecule kan zo in korte tijd vele duizenden "
                  "substraatmoleculen omzetten</strong>."),
            ("p", "Een enzym versnelt een reactie doordat het <strong>de activeringsenergie verlaagt</strong>. "
                  "De <strong>activeringsenergie</strong> is <strong>de energie die nodig is om een reactie op "
                  "gang te brengen</strong>, ook als die reactie op het einde energie oplevert. Met een enzym "
                  "verloopt de reactie dus veel sneller bij lichaamstemperatuur."),
            ("kader", "Een enzym <strong>verandert de evenwichtsligging niet</strong>. Er ontstaat op het einde "
                      "niet meer product: het evenwicht wordt alleen sneller bereikt."),
        ]),
        dict(kop="Het sleutel-slotprincipe", blokken=[
            ("p", "De stof die een enzym omzet, heet het <strong>substraat</strong>. Het substraat bindt op "
                  "een klein deel van het enzym: het <strong>actief centrum</strong>. In het "
                  "<strong>sleutel-slotprincipe</strong> is het actief centrum <strong>het slot</strong> en het "
                  "substraat <strong>de sleutel</strong>. Zitten ze even aan elkaar vast, dan noemt men dat "
                  "tijdelijke geheel het <strong>enzym-substraatcomplex</strong> of enzymsubstraatcomplex. Daarna komen de producten vrij."),
            ("p", "Het actief centrum is <strong>een klein deel van het enzym waar het substraat bindt</strong>. "
                  "<strong>De vorm ervan bepaalt welk substraat het enzym omzet</strong>. Na de reactie blijft "
                  "het gewoon bestaan, maar <strong>het verandert van vorm als het enzym denatureert</strong>."),
            ("p", "Omdat alleen een passende sleutel in het slot past, zet een enzym maar één bepaald substraat "
                  "of één soort substraat om. Dat heet <strong>substraatspecificiteit</strong>. Lijkt een stof "
                  "sterk op het substraat maar <strong>past ze niet in het actief centrum</strong>, dan wordt ze "
                  "niet omgezet."),
        ]),
        dict(kop="De naam van een enzym", blokken=[
            ("p", "De naam van de meeste enzymen eindigt op de uitgang <strong>-ase</strong>. Vaak staat het "
                  "substraat ervoor: <strong>lactase breekt lactose af</strong>, <strong>lipase breekt lipiden "
                  "af</strong>, <strong>maltase breekt maltose af</strong>, sacharase breekt sacharose af en "
                  "amylase breekt zetmeel (amylum) af."),
            ("p", "Sommige enzymen hebben een oudere naam zonder -ase: <strong>pepsine</strong> en "
                  "<strong>trypsine</strong> zijn eiwitsplitsende enzymen: ze breken allebei <strong>eiwitten</strong> af, geen zetmeel of "
                  "triglyceriden."),
        ]),
        dict(kop="Denaturatie, cofactoren en co-enzymen", blokken=[
            ("p", "<strong>Enzymen zijn eiwitten, en hun werking hangt af van hun ruimtelijke vorm</strong>. Bij "
                  "<strong>denaturatie</strong> <strong>gaat de ruimtelijke vorm verloren</strong>, waardoor het "
                  "actief centrum niet meer past. Hoge temperatuur of een sterk afwijkende pH denatureert een "
                  "enzym. <strong>Denaturatie door hitte is blijvend</strong>: een enzym dat gedenatureerd is, "
                  "gaat niet opnieuw werken als het afkoelt."),
            ("p", "Sommige enzymen hebben een helper nodig. Een <strong>cofactor</strong> is <strong>een "
                  "niet-eiwitdeel, zoals een metaalion</strong> (zink, magnesium, ijzer). Een "
                  "<strong>co-enzym</strong> is <strong>een organische molecule, vaak afgeleid van een "
                  "vitamine</strong> van de B-groep."),
        ]),
        dict(kop="Wat beïnvloedt de werking?", blokken=[
            ("p", tabel(["Factor", "Wat er gebeurt"], [
                ["<strong>temperatuur</strong>",
                 "Bij <strong>lage temperatuur</strong> werkt een enzym traag: <strong>de moleculen bewegen "
                 "trager</strong>, zodat enzym en substraat elkaar minder vaak raken. Het enzym is niet kapot. "
                 "Bij het <strong>temperatuursoptimum</strong> werkt het enzym het snelst, bij menselijke enzymen "
                 "rond <strong>37 °C</strong>. Daarboven denatureert het. <strong>Bij koorts van 41 °C kunnen "
                 "sommige enzymen al minder goed werken.</strong>"],
                ["<strong>zuurtegraad of pH</strong>",
                 "Elk enzym heeft een eigen <strong>pH-optimum</strong>. <strong>Pepsine</strong> werkt in de maag "
                 "het best <strong>rond pH 2</strong>, <strong>speekselamylase</strong> rond pH 7 en "
                 "<strong>trypsine</strong> in de twaalfvingerige darm rond pH 8, licht basisch. Niet elk enzym "
                 "heeft dus hetzelfde pH-optimum."],
                ["<strong>substraatconcentratie</strong>",
                 "Meer substraat geeft eerst een hogere snelheid. Zijn <strong>alle actieve centra bezet</strong>, "
                 "dan bereikt de reactie haar <strong>maximale reactiesnelheid</strong>. Dat heet "
                 "<strong>verzadiging</strong> of de verzadigingstoestand: meer substraat helpt dan niet meer. Die maximale snelheid heet ook de maximumsnelheid of Vmax."],
                ["<strong>enzymconcentratie</strong>",
                 "Meer enzym geeft een hogere snelheid zolang er substraat genoeg is, want <strong>er zijn meer "
                 "actieve centra beschikbaar</strong>."],
                ["<strong>inhibitor</strong>",
                 "Een <strong>inhibitor</strong> <strong>remt de werking van een enzym</strong>. Een inhibitor "
                 "<strong>die op het substraat lijkt</strong>, kan in het actief centrum gaan zitten en het echte "
                 "substraat de plaats afnemen."],
            ])),
            ("p", "Een grafiek van de reactiesnelheid tegen de temperatuur <strong>stijgt geleidelijk tot rond "
                  "37 °C en valt daarna snel terug</strong>. Een grafiek tegen de substraatconcentratie stijgt "
                  "eerst en wordt dan vlak: daar is de verzadiging bereikt."),
            ("kader", "<strong>Een proef met amylase en zetmeel</strong> bij 0 °C, 37 °C en 90 °C: bij "
                      "<strong>37 °C</strong> gaat de afbraak het snelst. Zet je daarna alle buizen op 37 °C, "
                      "dan <strong>gaat het enzym in de buis die eerst koud was alsnog werken</strong>. In de "
                      "buis die heet was, is het enzym gedenatureerd en blijft het stil."),
            ("p", "Komt <strong>speekselamylase</strong> met het voedsel in de maag, dan <strong>stopt het "
                  "grotendeels, want de maag is veel te zuur</strong>."),
        ]),
        dict(kop="Enzymen in het lichaam", blokken=[
            ("p", "Enzymen zijn onmisbaar bij <strong>de spijsvertering</strong>, <strong>de "
                  "celademhaling</strong>, <strong>de fotosynthese</strong> en <strong>de "
                  "DNA-replicatie</strong>. Bij de DNA-replicatie bouwt <strong>DNA-polymerase</strong> een "
                  "nieuwe streng op en opent helicase de dubbele helix."),
        ]),
    ],
    onthoud=[
        "Een enzym is een eiwit dat als biokatalysator een reactie versnelt zonder verbruikt te worden.",
        "Een enzym verlaagt de activeringsenergie.",
        "Actief centrum = slot, substraat = sleutel; samen vormen ze het enzym-substraatcomplex.",
        "Substraatspecificiteit: een enzym zet maar één soort substraat om.",
        "Denaturatie: het enzym verliest zijn vorm en werkt niet meer.",
        "Temperatuur, pH, substraat- en enzymconcentratie beïnvloeden de werking; een inhibitor remt.",
        "Bij verzadiging zijn alle actieve centra bezet: maximale reactiesnelheid.",
    ],
)

# ───────────────────────── 2. Het spijsverteringsstelsel
BUNDELS["het-spijsverteringsstelsel-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Het spijsverteringsstelsel",
    onder="De bouw van het spijsverteringsstelsel, de verteringssappen en hun enzymen, de opname van voedingsstoffen en de bekendste aandoeningen.",
    secties=[
        dict(kop="De wand van het spijsverteringskanaal", blokken=[
            ("p", "De wand bestaat van binnen naar buiten uit de <strong>slijmvlieslaag of mucosa</strong>, "
                  "een <strong>bindweefsellaag</strong>, de <strong>spierlaag</strong> en tot slot een "
                  "<strong>bindweefsellaag of steunweefsel</strong>. De slijmvlieslaag ligt aan de binnenkant, "
                  "tegen de voedselbrij."),
            ("p", "<strong>De spierlaag kneedt het voedsel en duwt het verder door peristaltiek</strong>. <strong>Peristaltiek</strong> is een "
                  "golfvormige samentrekking die het voedsel voortstuwt: daarbij trekken de <strong>kringspieren</strong> en "
                  "<strong>lengtespieren</strong> beurtelings samen in een golfbeweging."),
        ]),
        dict(kop="De delen van het spijsverteringsstelsel", blokken=[
            ("p", "Het voedsel gaat van de <strong>mondholte</strong> met de speekselklieren naar de "
                  "<strong>keelholte</strong>. Bij het slikken sluit het <strong>strottenklepje</strong> de "
                  "luchtpijp af. Via de <strong>slokdarm</strong> komt het voedsel in de <strong>maag</strong>. "
                  "De <strong>maagportier</strong> is <strong>de kringspier tussen de maag en de "
                  "twaalfvingerige darm</strong>, niet tussen de slokdarm en de maag."),
            ("p", tabel(["Deel", "Wat erbij hoort"], [
                ["dunne darm", "<strong>de twaalfvingerige darm</strong>, <strong>de nuchtere darm of "
                               "jejunum</strong> en <strong>de kronkeldarm of ileum</strong>"],
                ["dikke darm", "<strong>de blinde darm of caecum met het wormvormig aanhangsel</strong>, "
                               "<strong>de karteldarm of colon</strong> (opstijgend, dwarslopend, afdalend en "
                               "S-vormig deel) en <strong>de endeldarm of rectum</strong>, tot de anus"],
                ["klieren", "de speekselklieren, de <strong>lever</strong> met de <strong>galblaas</strong> en de "
                            "<strong>alvleesklier of pancreas</strong>"],
            ])),
            ("p", "<strong>Vertering</strong> is <strong>het afbreken van grote voedingsmoleculen tot kleine die "
                  "opgenomen kunnen worden</strong>. Zetmeel, eiwitten en vetten passen niet door de darmwand; "
                  "hun bouwstenen wel."),
        ]),
        dict(kop="Maag, gal en alvleesklier", blokken=[
            ("p", "In de maagwand maken <strong>de pariëtale cellen</strong> het <strong>zoutzuur</strong> "
                  "(HCl) en de slijmcellen een beschermende slijmlaag. Het <strong>maagzuur</strong> "
                  "<strong>doodt veel bacteriën die met het voedsel binnenkomen</strong>, <strong>zet pepsinogeen "
                  "om in het actieve pepsine</strong> en <strong>zorgt voor de lage pH waarbij pepsine goed "
                  "werkt</strong>. <strong>Pepsine wordt eerst aangemaakt als het inactieve pepsinogeen</strong>, "
                  "zodat het de cellen die het maken niet zelf verteert."),
            ("p", "<strong>Gal wordt aangemaakt in de lever</strong> en opgeslagen in de galblaas. "
                  "<strong>Galzouten verdelen grote vetdruppels in kleine druppeltjes, zodat lipase beter kan "
                  "werken</strong>: ze <strong>emulgeren</strong>. <strong>Gal bevat zelf geen "
                  "enzymen</strong>."),
            ("p", "De alvleesklier geeft <strong>natriumwaterstofcarbonaat (NaHCO₃)</strong> af aan de "
                  "twaalfvingerige darm <strong>om het zure maagsap te neutraliseren, zodat de darmenzymen "
                  "kunnen werken</strong>. Het <strong>alvleeskliersap</strong> bevat <strong>amylase</strong>, "
                  "<strong>trypsine</strong> en <strong>lipase</strong>. <strong>Lactase</strong> zit in de wand "
                  "van de dunne darm, pepsine in de maag."),
        ]),
        dict(kop="Welk enzym breekt wat af?", blokken=[
            ("p", tabel(["Voedingsstof", "Enzymen", "Eindproduct"], [
                ["zetmeel", "amylase (tot maltose), dan <strong>maltase</strong>", "<strong>glucose</strong>"],
                ["melksuiker of lactose", "<strong>lactase</strong>", "glucose en galactose"],
                ["sacharose", "<strong>sacharase</strong>", "<strong>glucose en fructose</strong>"],
                ["eiwitten", "pepsine, trypsine (endopeptidasen), daarna exopeptidasen", "aminozuren"],
                ["vetten of triglyceriden", "lipase, na emulgeren door gal", "glycerol en vetzuren"],
            ])),
            ("p", "<strong>Endopeptidasen knippen midden in een eiwitketen, exopeptidasen knippen aminozuren van "
                  "de uiteinden</strong>."),
        ]),
        dict(kop="Opname en transport", blokken=[
            ("p", "De dunne darm heeft <strong>plooien, darmvlokken of villi en microvilli</strong>. Die "
                  "<strong>vergroten het oppervlak voor de opname van voedingsstoffen</strong>. De vele "
                  "microvilli samen vormen de <strong>borstelzoom</strong>."),
            ("p", tabel(["Transport", "Wat het is"], [
                ["<strong>diffusie</strong>", "passief, met het concentratieverschil mee"],
                ["<strong>gefaciliteerde diffusie</strong>", "<strong>passief transport via een transporteiwit, "
                 "met het concentratieverschil mee</strong>, zoals de glucosetransporter"],
                ["<strong>osmose</strong>", "<strong>water dat door een halfdoorlatend membraan naar de "
                 "geconcentreerdste kant gaat</strong>"],
                ["<strong>actief transport</strong>", "een stof gaat <strong>tegen het concentratieverschil "
                 "in</strong>, met een pomp en <strong>energie uit ATP</strong>; ook blaasjestransport hoort "
                 "hierbij"],
            ])),
            ("p", "Diffusie, gefaciliteerde diffusie en osmose zijn passief en kosten de cel geen ATP. Een "
                  "<strong>isotone</strong> of isotonische oplossing (isotoon) heeft dezelfde osmotische waarde als de cel. Komt een "
                  "<strong>rode bloedcel in zuiver water</strong>, dat hypotoon is, dan <strong>stroomt er water "
                  "de cel in, zodat ze opzwelt en kan barsten</strong>."),
            ("p", "<strong>Glucose en aminozuren</strong> gaan naar het bloed en <strong>via de "
                  "leverpoortader</strong> naar de lever. <strong>Glycerol en vetzuren</strong> worden in de "
                  "darmepitheelcel <strong>weer vetten, verpakt in lipoproteïnen</strong> (chylomicronen), en "
                  "<strong>gaan naar het lymfevat</strong>. <strong>Het meeste water wordt al in de dunne darm "
                  "opgenomen</strong>; de dikke darm neemt de rest op."),
        ]),
        dict(kop="Voedingsstoffen, vezels en darmflora", blokken=[
            ("p", "<strong>Essentiële voedingsstoffen</strong> zijn <strong>stoffen die het lichaam nodig heeft "
                  "maar niet zelf kan maken</strong>: essentiële aminozuren, essentiële vetzuren zoals "
                  "<strong>een omega-3-vetzuur</strong>, vitaminen en mineralen. De vetoplosbare vitaminen (vetoplosbaar) zijn "
                  "<strong>vitamine A</strong>, <strong>vitamine D</strong>, E en <strong>K</strong>; "
                  "<strong>vitamine B12</strong> en <strong>vitamine C</strong> zijn wateroplosbaar."),
            ("p", "<strong>Voedingsvezels</strong> worden niet verteerd. <strong>Ze geven volume aan de "
                  "darminhoud en houden de stoelgang vlot.</strong>"),
            ("p", "De <strong>darmflora</strong> <strong>maakt vitamine K aan</strong>, <strong>helpt het "
                  "immuunsysteem en houdt ziekteverwekkers weg</strong> en <strong>breekt een deel van de "
                  "voedingsvezels af</strong>. <strong>Escherichia coli</strong> komt normaal voor in de dikke "
                  "darm; <strong>Lactobacillus</strong> is een andere nuttige darmbacterie."),
        ]),
        dict(kop="Aandoeningen", blokken=[
            ("p", tabel(["Aandoening", "Oorzaak en behandeling"], [
                ["<strong>coeliakie</strong>", "<strong>een auto-immuunziekte waarbij gluten de darmvlokken "
                 "beschadigen</strong>; behandeling: strikt glutenvrij eten"],
                ["<strong>ziekte van Crohn</strong>", "<strong>een chronische ontsteking die overal in het "
                 "spijsverteringskanaal kan voorkomen</strong>"],
                ["gastritis en <strong>maagzweer</strong> (maagzweren)", "vaak door de bacterie <strong>Helicobacter "
                 "pylori</strong>; behandeling met antibiotica en maagzuurremmers"],
                ["salmonellose", "voedselvergiftiging door <strong>Salmonella</strong>, bijvoorbeeld uit "
                 "besmette eieren"],
            ])),
        ]),
    ],
    onthoud=[
        "Van binnen naar buiten: slijmvlies, bindweefsel, spierlaag, bindweefsel.",
        "Peristaltiek duwt het voedsel voort; het strottenklepje sluit de luchtpijp af.",
        "Maagzuur doodt bacteriën en activeert pepsinogeen tot pepsine.",
        "Gal komt uit de lever en emulgeert vetten; ze bevat geen enzymen.",
        "NaHCO₃ neutraliseert het maagzuur in de twaalfvingerige darm.",
        "Villi, microvilli en de borstelzoom vergroten het opnameoppervlak.",
        "Vetten gaan naar de lymfe, glucose en aminozuren via de leverpoortader naar de lever.",
    ],
)

# ───────────────────────── 3. Het uitscheidingsstelsel
BUNDELS["het-uitscheidingsstelsel-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Het uitscheidingsstelsel",
    onder="De bouw van de nieren en de urinewegen, hoe een nefron urine maakt, hoe ADH het water regelt, en de aandoeningen.",
    secties=[
        dict(kop="De urinewegen", blokken=[
            ("p", "Urine stroomt van de <strong>nier</strong> door de <strong>urineleider of ureter</strong> "
                  "naar de <strong>urineblaas</strong> en via de <strong>urinebuis of urethra</strong> naar "
                  "buiten. <strong>De urineleider brengt urine van de nier naar de blaas.</strong> Zijn wand "
                  "heeft <strong>drie</strong> lagen."),
            ("p", "De blaas wordt dichtgehouden door een interne en een externe kringspier. <strong>De externe "
                  "kringspier kan je bewust aansturen.</strong> Als een kapje bovenop elke nier ligt een klein orgaantje, de <strong>bijnier</strong>, "
                  "die onder meer adrenaline maakt."),
        ]),
        dict(kop="De bouw van de nier", blokken=[
            ("p", "Op een lengtedoorsnede zie je het nierkapsel, <strong>de nierschors of cortex</strong> aan de "
                  "buitenkant, <strong>het niermerg met de nierpiramides</strong> meer naar binnen, de "
                  "nierpapillen, de nierkelken en <strong>het nierbekken</strong>, waarin de urine samenkomt voor "
                  "ze de urineleider ingaat. Het niermerg ligt dus niet aan de buitenkant."),
            ("p", "Het bloed komt binnen via <strong>de nierslagader</strong> en verlaat de nier via de "
                  "nierader."),
        ]),
        dict(kop="Het nefron", blokken=[
            ("p", "Het <strong>nefron</strong> is de kleinste werkende eenheid van de nier. Het begint met het "
                  "<strong>nierlichaampje of lichaampje van Malpighi</strong>: <strong>de glomerulus met daarrond "
                  "het kapsel van Bowman</strong>. Het <strong>aanvoerend nierslagadertje</strong> brengt bloed "
                  "naar de glomerulus, het <strong>afvoerend nierslagadertje</strong> voert het weg."),
            ("p", "Het filtraat stroomt door <strong>kapsel van Bowman, eerste kronkelbuisje, lus van Henle, tweede "
                  "kronkelbuisje, verzamelbuis</strong>. <strong>De lus van Henle</strong> duikt diep het "
                  "niermerg in en ligt dus niet volledig in de nierschors."),
            ("p", "De nierfilter bestaat uit <strong>het endotheel van de haarvaten</strong>, <strong>het "
                  "basaalmembraan</strong> en <strong>de podocyten</strong>. Rode bloedcellen en grote eiwitten "
                  "gaan er niet door: <strong>ze zijn te groot om door de filter te passen</strong>. <strong>Bloed "
                  "of veel eiwit in de urine</strong> kan dus wijzen op een beschadigde nierfilter."),
        ]),
        dict(kop="Filtratie, resorptie en secretie", blokken=[
            ("p", tabel(["Proces", "Wat er gebeurt"], [
                ["<strong>filtratie</strong>", "<strong>water en kleine opgeloste stoffen worden uit de "
                 "glomerulus in het kapsel geperst</strong>; dat filtraat heet <strong>voorurine</strong>"],
                ["<strong>resorptie</strong>", "<strong>nuttige stoffen gaan uit het nierbuisje terug naar het "
                 "bloed</strong>; dat heet ook terugopname of reabsorptie, via diffusie, osmose en actief transport; <strong>alle glucose</strong> wordt "
                 "teruggeresorbeerd"],
                ["<strong>secretie</strong>", "<strong>extra stoffen actief vanuit het bloed in het nierbuisje "
                 "brengen</strong>"],
                ["excretie", "de urine verlaat het lichaam"],
            ])),
            ("p", "Een normale urine bevat <strong>water</strong>, <strong>ureum</strong>, urinezuur en zouten, "
                  "maar geen glucose of <strong>eiwitten zoals albumine</strong>. <strong>Ureum</strong> is de "
                  "stikstofhoudende afvalstof die de lever maakt uit de afbraak van aminozuren."),
            ("p", "Bij zuurstoftekort maakt de nier <strong>erytropoëtine (EPO)</strong>, dat de aanmaak van "
                  "rode bloedcellen stimuleert."),
        ]),
        dict(kop="Osmoregulatie en ADH", blokken=[
            ("p", "<strong>Osmoregulatie</strong> of de regeling van de waterhuishouding is <strong>het constant houden van de hoeveelheid water en "
                  "zouten in het lichaam</strong>. Het is een feedbacksysteem met <strong>osmoreceptoren als "
                  "sensor</strong>, <strong>de hypothalamus als controlecentrum</strong> en <strong>de nieren als "
                  "effector</strong>."),
            ("p", "Het <strong>antidiuretisch hormoon (ADH)</strong> wordt in de hypothalamus gemaakt en "
                  "<strong>door de hypofyse</strong> aan het bloed afgegeven. ADH <strong>maakt de wand van de "
                  "verzamelbuis beter doorlaatbaar voor water</strong>. Heb je veel gezweet en weinig gedronken, "
                  "dan <strong>komt er meer ADH, neemt de verzamelbuis meer water terug en plas je weinig en "
                  "geconcentreerd</strong>. Daarnaast zet de hypothalamus de <strong>dorst</strong> of "
                  "dorstprikkel in gang. <strong>Alcohol remt de afgifte van ADH</strong>, waardoor je meer moet "
                  "plassen."),
        ]),
        dict(kop="Aandoeningen", blokken=[
            ("p", tabel(["Aandoening", "Wat je moet weten"], [
                ["<strong>blaasontsteking</strong>", "meestal <strong>bacteriën die via de urinebuis "
                 "binnendringen</strong>"],
                ["<strong>nierstenen</strong>", "voorkomen door <strong>voldoende water drinken</strong>, "
                 "<strong>niet te veel zout eten</strong> en <strong>gezond en gevarieerd eten</strong>; "
                 "verkleinen <strong>met een toestel dat de steen met schokgolven in stukjes slaat</strong>, de "
                 "niersteenverbrijzelaar"],
                ["<strong>nierfalen</strong>", "afvalstoffen zoals <strong>ureum stapelen zich op in het "
                 "bloed</strong>; dan is dialyse of een transplantatie nodig"],
            ])),
            ("p", "Bij <strong>hemodialyse</strong> <strong>stroomt het bloed door een kunstnier en geeft het er "
                  "afvalstoffen af aan een spoelvloeistof</strong>, door een semipermeabel membraan. Een "
                  "<strong>shunt</strong> is een verbinding tussen een slagader en een ader in de arm, zodat "
                  "men vlot bloed kan afnemen."),
        ]),
    ],
    onthoud=[
        "Nier → urineleider → urineblaas → urinebuis.",
        "Een nefron: glomerulus en kapsel van Bowman, kronkelbuisjes, lus van Henle, verzamelbuis.",
        "Filtratie geeft voorurine; resorptie haalt nuttige stoffen terug; secretie voegt stoffen toe.",
        "ADH uit de hypofyse laat de verzamelbuis meer water terugnemen.",
        "Alcohol remt ADH; nierstenen voorkom je met veel water en weinig zout.",
        "Hemodialyse zuivert het bloed in een kunstnier, via een shunt.",
    ],
)

# ───────────────────────── 4. Het bloed
BUNDELS["het-bloed-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Het bloed",
    onder="De bestanddelen van het bloed, het werk van rode en witte bloedcellen, de bloedstolling en de bloedgroepen.",
    secties=[
        dict(kop="Wat zit er in het bloed?", blokken=[
            ("p", "Bloed bevat <strong>rode bloedcellen of erytrocyten</strong>, <strong>witte bloedcellen of "
                  "leukocyten</strong> en <strong>bloedplaatjes of trombocyten</strong>, in het "
                  "<strong>plasma</strong> of bloedplasma. Ze worden gevormd <strong>in het rode beenmerg</strong>. "
                  "<strong>De rode bloedcellen zijn het talrijkst.</strong>"),
            ("p", "Het plasma vervoert <strong>voedingsstoffen zoals glucose</strong>, <strong>hormonen</strong>, "
                  "<strong>afvalstoffen zoals ureum</strong>, zouten en eiwitten. Het meest voorkomende "
                  "plasma-eiwit is <strong>albumine</strong>, dat water in de bloedvaten houdt. De "
                  "<strong>immunoglobulines</strong> zijn <strong>de antilichamen</strong>."),
            ("p", "Wordt bloed met een middel tegen stolling <strong>gecentrifugeerd</strong>, dan zie je van "
                  "onder naar boven <strong>rode bloedcellen, een dun laagje witte bloedcellen en bloedplaatjes, "
                  "en bovenaan plasma</strong>. <strong>Serum of bloedserum is plasma zonder de stollingsfactoren zoals "
                  "fibrinogeen</strong>."),
        ]),
        dict(kop="De rode bloedcellen", blokken=[
            ("p", "<strong>Een rijpe rode bloedcel heeft geen celkern</strong> en leeft <strong>ongeveer 120 "
                  "dagen</strong>. Daarna wordt ze <strong>in de milt en de lever</strong> afgebroken. Ze is "
                  "<strong>een schijfje dat aan beide kanten ingedeukt is, met een groot oppervlak voor "
                  "gasuitwisseling</strong>."),
            ("p", "Rode bloedcellen bevatten <strong>hemoglobine</strong>, een ijzerhoudend eiwit met vier "
                  "subeenheden en vier heemgroepen. Eén hemoglobinemolecule bindt dus maximaal "
                  "<strong>vier</strong> zuurstofmoleculen. Met zuurstof erop heet het "
                  "<strong>oxyhemoglobine</strong>. Ongeveer 98 % van de zuurstof zit gebonden aan "
                  "hemoglobine; maar een klein deel is opgelost in het plasma. <strong>Het meeste CO₂ wordt als "
                  "waterstofcarbonaat in het plasma vervoerd.</strong>"),
            ("p", "De <strong>hematocrietwaarde</strong> is <strong>het percentage van het bloedvolume dat uit "
                  "rode bloedcellen bestaat</strong>, ongeveer 40 à 45 %. Op <strong>hoogtestage</strong> "
                  "<strong>maken de nieren in de ijle lucht meer EPO, zodat er meer rode bloedcellen "
                  "komen</strong>. <strong>EPO</strong> is <strong>een hormoon uit de nieren dat de aanmaak van "
                  "rode bloedcellen stimuleert</strong>. Een te hoge hematocriet is niet onschadelijk: het bloed "
                  "wordt dik en het risico op bloedklonters stijgt."),
        ]),
        dict(kop="De witte bloedcellen", blokken=[
            ("p", "<strong>De hoofdtaak van de witte bloedcellen is de afweer tegen ziekteverwekkers.</strong>"),
            ("p", tabel(["Soort", "Wat ze doen"], [
                ["granulocyten: <strong>neutrofielen</strong>", "de talrijkste; ruimen bij een ontsteking als "
                 "eersten bacteriën op door <strong>fagocytose</strong>, het opslokken van een bacterie"],
                ["granulocyten: <strong>eosinofielen</strong>", "bij allergieën en tegen parasieten zoals wormen"],
                ["granulocyten: basofielen", "maken histamine vrij bij allergische reacties"],
                ["agranulocyten: <strong>monocyten</strong>", "worden in het weefsel <strong>een macrofaag</strong>"],
                ["agranulocyten: <strong>lymfocyten</strong>", "<strong>B-lymfocyten</strong> worden plasmacellen "
                 "die <strong>antilichamen</strong> maken (humorale afweer); <strong>T-lymfocyten</strong> doden "
                 "zelf lichaamscellen die besmet zijn met een virus (<strong>cellulaire afweer</strong>)"],
            ])),
            ("p", "<strong>Eosinofielen maken dus geen antilichamen</strong>: dat doen de B-lymfocyten."),
        ]),
        dict(kop="De bloedstolling", blokken=[
            ("p", "<strong>Bloedplaatjes helpen bij de bloedstolling.</strong> Ze kleven tegen een beschadigde "
                  "wand en starten de <strong>stollingscascade</strong>. Die kan op twee manieren beginnen: via "
                  "de <strong>extrinsieke route vanuit beschadigd weefsel</strong> en via de <strong>intrinsieke "
                  "route vanuit het bloed zelf</strong>."),
            ("p", "Aan het einde zet protrombine zich om in trombine, en <strong>trombine zet fibrinogeen om in "
                  "fibrinedraden die het stolsel vormen</strong>. <strong>Fibrinogeen</strong> is het opgeloste "
                  "plasma-eiwit dat zo onoplosbaar fibrine wordt."),
        ]),
        dict(kop="Bloedgroepen", blokken=[
            ("p", tabel(["Bloedgroep", "Antigenen op de rode bloedcel", "Antilichamen in het plasma"], [
                ["A", "A-antigenen", "anti-B"],
                ["B", "B-antigenen", "anti-A"],
                ["AB", "A en B", "geen"],
                ["O", "geen A- en geen B-antigenen", "anti-A en anti-B"],
            ])),
            ("p", "Bij een bloedtransfusie moet de bloedgroep passen. Krijgt iemand met bloedgroep B bloed van groep A, dan <strong>doet het anti-A van de ontvanger "
                  "de rode bloedcellen van de donor klonteren</strong>. Dat samenklonteren heet "
                  "<strong>agglutinatie</strong> of klontering; daarna volgt hemolyse."),
            ("p", "Het <strong>resussysteem</strong> gaat over het D-antigeen. <strong>O-negatief is de universele "
                  "donor van rode bloedcellen</strong> en <strong>AB-positief is de universele "
                  "ontvanger</strong>. <strong>Iemand met bloedgroep O kan enkel bloed van groep O "
                  "krijgen</strong>; iemand met AB kan bloed van alle groepen krijgen."),
            ("kader", "<strong>Anti-D is er niet van nature.</strong> Een resusnegatieve persoon maakt het pas na "
                      "contact met resuspositief bloed. Is een <strong>resusnegatieve (resusnegatief) moeder zwanger van een "
                      "resuspositief kind</strong>, dan <strong>kan ze na de eerste bevalling anti-D maken tegen "
                      "een volgend resuspositief kind</strong>."),
        ]),
    ],
    onthoud=[
        "Rode bloedcellen: geen kern, 120 dagen, hemoglobine bindt vier O₂.",
        "Hematocriet = percentage rode bloedcellen; EPO uit de nieren doet hem stijgen.",
        "Serum is plasma zonder stollingsfactoren.",
        "Neutrofielen doen fagocytose, monocyten worden macrofagen, B-lymfocyten maken antilichamen.",
        "Trombine zet fibrinogeen om in fibrine.",
        "O-negatief is universele donor, AB-positief universele ontvanger.",
    ],
)

# ───────────────────────── 5. Het hart en de bloedsomloop
BUNDELS["het-hart-en-de-bloedsomloop-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Het hart en de bloedsomloop",
    onder="De bouw van het hart, de kleppen en de bloedstroom, de prikkelgeleiding en het ECG, en de dubbele bloedsomloop.",
    secties=[
        dict(kop="De bouw van het hart", blokken=[
            ("p", "Het hart ligt <strong>in de borstholte, tussen de twee longen in en een beetje naar "
                  "links</strong>. Het heeft <strong>vier holtes: twee boezems en twee kamers</strong>. "
                  "<strong>Het tussenschot of septum</strong> scheidt de linkerhelft van de rechterhelft. De punt heet de "
                  "<strong>apex</strong>; de brede bovenkant is de <strong>hartbasis</strong>."),
            ("p", "De hartwand bestaat van binnen naar buiten uit <strong>endocard, myocard, epicard</strong>. "
                  "Het <strong>myocard</strong> is de dikke spierlaag, de hartspier. Rond het hart zit "
                  "<strong>het hartzakje of pericard</strong>: <strong>een vlies rond het hart met wat vocht, "
                  "zodat het vlot kan bewegen</strong>."),
            ("p", "<strong>De linkerkamer heeft de dikste spierwand, want ze pompt het bloed door de hele grote "
                  "bloedsomloop.</strong> De hartspier zelf krijgt bloed <strong>via de kransslagaders</strong>, "
                  "die vlak boven de aortaklep van de aorta aftakken. <strong>Een hartinfarct ontstaat meestal "
                  "doordat een kransslagader verstopt raakt.</strong>"),
        ]),
        dict(kop="Bloedvaten en kleppen", blokken=[
            ("p", tabel(["Bloedvat", "Van waar naar waar"], [
                ["<strong>bovenste en onderste holle ader</strong>", "zuurstofarm bloed uit het lichaam naar de "
                 "rechterboezem"],
                ["<strong>longslagader</strong>", "vertrekt uit de <strong>rechterkamer</strong>, zuurstofarm bloed "
                 "naar de longen"],
                ["<strong>longaders</strong>", "<strong>zuurstofrijk bloed van de longen naar de "
                 "linkerboezem</strong>"],
                ["<strong>aorta</strong>", "vertrekt uit de linkerkamer, zuurstofrijk bloed naar het lichaam"],
            ])),
            ("p", "Bloedvaten die <strong>toekomen</strong> in het hart zijn de holle aders en de longaders; de "
                  "aorta en de longslagader vertrekken. Een slagader vervoert bloed van het hart weg, maar niet "
                  "altijd zuurstofrijk bloed: de longslagader vervoert zuurstofarm bloed."),
            ("p", "<strong>De hartkleppen laten het bloed maar in één richting stromen.</strong> De "
                  "atrioventriculaire kleppen liggen tussen boezem en kamer: <strong>de tricuspidalisklep</strong> "
                  "rechts en <strong>de mitralisklep</strong> links, tussen de linkerboezem en de linkerkamer. De "
                  "<strong>aortaklep</strong> en de <strong>pulmonalisklep</strong> liggen bij de slagaders."),
            ("p", "Rechts stroomt het bloed van <strong>holle aders, rechterboezem, tricuspidalisklep, "
                  "rechterkamer, pulmonalisklep, longslagader</strong>."),
        ]),
        dict(kop="Prikkelgeleiding en hartcyclus", blokken=[
            ("p", "Het impulsgeleidingssysteem of prikkelgeleidingssysteem van het hart start met de sinusknoop. De prikkels ontstaan <strong>in de sinusknoop, een groepje gangmakercellen in de "
                  "boezem</strong>. De prikkel loopt <strong>sinusknoop, AV-knoop, bundel van His, bundeltakken, "
                  "purkinjevezels</strong>. De AV-knoop houdt de prikkel even tegen, <strong>zodat de boezems "
                  "eerst leeglopen voor de kamers samentrekken</strong>. <strong>Het autonoom zenuwstelsel kan "
                  "de hartslag versnellen of vertragen, maar de sinusknoop bepaalt het basisritme.</strong>"),
            ("p", "Samentrekken heet <strong>systole</strong>, ontspannen diastole. Tijdens de "
                  "<strong>kamersystole</strong> <strong>trekken de kamers samen</strong>, <strong>sluiten de "
                  "atrioventriculaire kleppen</strong> en <strong>gaan de aortaklep en de pulmonalisklep "
                  "open</strong>. In de <strong>rustfase</strong> <strong>zijn boezems en kamers ontspannen en "
                  "loopt het bloed het hart in</strong>."),
            ("p", "Een <strong>elektrocardiogram of ECG</strong> registreert <strong>de elektrische activiteit "
                  "van het hart</strong>. De <strong>P-top</strong> hoort bij de prikkeling van de boezems, het "
                  "<strong>QRS-complex</strong> bij <strong>de prikkeling van de kamers, net voor ze "
                  "samentrekken</strong>, en de <strong>T-top</strong> bij het herstel van de kamers."),
        ]),
        dict(kop="De dubbele bloedsomloop", blokken=[
            ("p", "De <strong>kleine bloedsomloop</strong> is <strong>de weg van de rechterkamer via de longen "
                  "naar de linkerboezem</strong>. De grote bloedsomloop gaat van de linkerkamer door het lichaam "
                  "naar de rechterboezem. Bij een <strong>dubbele bloedsomloop</strong> passeert het bloed "
                  "<strong>twee keer door het hart</strong> bij één volledige rondgang."),
            ("p", "Een <strong>poortader</strong> is <strong>een ader tussen twee haarvatennetwerken, zoals tussen "
                  "darm en lever</strong>. Via de leverpoortader <strong>verwerkt de lever eerst de opgenomen "
                  "voedingsstoffen en ontgift ze het bloed</strong>."),
        ]),
        dict(kop="Slagaders, aders en haarvaten", blokken=[
            ("p", "Het bloed stroomt <strong>slagader, arteriolen, haarvaten, venulen, ader</strong>. De "
                  "<strong>haarvaten</strong> of capillairen hebben een wand van één cellaag; daar gebeurt de "
                  "uitwisseling met de weefsels."),
            ("p", "<strong>Een slagader heeft een dikke, gespierde wand, een ader een dunnere wand met "
                  "kleppen.</strong> In de wand van een slagader vind je <strong>een endotheellaag aan de "
                  "binnenkant</strong>, <strong>een laag glad spierweefsel</strong> en <strong>bindweefsel aan "
                  "de buitenkant</strong>. De druk is het hoogst in de slagaders en het laagst in de aders, "
                  "dus <strong>niet</strong> hoger in de aders."),
            ("p", "Het bloed in de aders van de benen komt terug dankzij <strong>de veneuze kleppen</strong>, "
                  "<strong>het samentrekken van de beenspieren rond de aders</strong> en <strong>de zuigwerking "
                  "bij het inademen</strong>: de veneuze terugstroom."),
        ]),
    ],
    onthoud=[
        "Vier holtes; de linkerkamer heeft de dikste wand.",
        "Holle aders → rechterboezem → rechterkamer → longslagader; longaders → linkerboezem → linkerkamer → aorta.",
        "Mitralisklep links, tricuspidalisklep rechts.",
        "Sinusknoop → AV-knoop → bundel van His → bundeltakken → purkinjevezels.",
        "P-top: boezems; QRS: kamers; T-top: herstel van de kamers.",
        "Kleine bloedsomloop: hart → longen → hart. Poortader: tussen twee haarvatennetwerken.",
    ],
)

# ───────────────────────── 6. De bloeddruk en het lymfestelsel
BUNDELS["de-bloeddruk-en-het-lymfestelsel-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De bloeddruk en het lymfestelsel",
    onder="Wat bloeddruk is, hoe het lichaam hem regelt, en hoe weefselvocht en lymfe ontstaan en worden afgevoerd.",
    secties=[
        dict(kop="Wat is bloeddruk?", blokken=[
            ("p", "De <strong>systolische bloeddruk of bovendruk</strong> is <strong>de hoogste druk in de "
                  "slagaders, als de kamers samentrekken</strong>. De diastolische druk of onderdruk is de "
                  "laagste druk, als het hart ontspant. Men drukt de bloeddruk uit in <strong>mmHg</strong>, "
                  "millimeter kwik."),
            ("p", "<strong>Ongeveer 120/80 mmHg</strong> is normaal bij een gezonde volwassene in rust. "
                  "<strong>Vanaf 140/90 mmHg</strong> spreekt men van <strong>hypertensie</strong>; een veel te "
                  "lage druk heet hypotensie. De bloeddruk is <strong>hoog in de aorta, dalend in de kleine "
                  "vaten en laag in de aders</strong>."),
            ("p", "Mee bepalend zijn <strong>het hartritme</strong>, <strong>het slagvolume</strong>, <strong>de "
                  "wijdte van de bloedvaten</strong> en <strong>het bloedvolume</strong>."),
        ]),
        dict(kop="De regeling van de bloeddruk", blokken=[
            ("p", "<strong>Baroreceptoren</strong> of drukreceptoren, zintuigcellen in de aorta en de halsslagaders meten de druk. Ze melden het "
                  "aan het <strong>cardiovasculair centrum in het verlengde merg</strong>. Dat werkt als een "
                  "<strong>negatief feedbacksysteem</strong>: het <strong>werkt de verandering tegen</strong> "
                  "en versterkt ze niet."),
            ("p", "Is de bloeddruk te hoog, dan <strong>gaat het hart trager kloppen</strong>, daalt het "
                  "slagvolume en <strong>verwijden de bloedvaten (vasodilatatie)</strong>. Het vernauwen heet "
                  "<strong>vasoconstrictie</strong>."),
            ("p", "Het <strong>orthosympatisch zenuwstelsel</strong> <strong>versnelt de hartslag en doet de "
                  "bloeddruk stijgen</strong>, bijvoorbeeld tijdens het sporten. Het <strong>parasympatisch "
                  "zenuwstelsel</strong> is het rustsysteem: na het sporten vertraagt het de hartslag."),
            ("p", "Is de bloeddruk te laag, dan start het renine-angiotensinesysteem: de nieren maken <strong>renine</strong>. <strong>Renine zet "
                  "angiotensinogeen om in angiotensine I, en het ACE-enzym zet dat om in angiotensine "
                  "II.</strong> <strong>Angiotensine II doet de bloedvaten vernauwen</strong> en maakt "
                  "<strong>aldosteron</strong> vrij. <strong>Aldosteron laat de nieren meer zout en water "
                  "terugnemen, dus meer bloedvolume</strong>."),
        ]),
        dict(kop="Te hoog of te laag", blokken=[
            ("p", "Een langdurig te hoge bloeddruk kan leiden tot <strong>een beroerte</strong>, <strong>een "
                  "hartinfarct</strong> en <strong>schade aan de nieren</strong>. Je voorkomt hem door "
                  "<strong>minder zout eten</strong>, <strong>regelmatig bewegen</strong> en <strong>niet "
                  "roken</strong>."),
            ("p", "Een typisch symptoom van een te lage bloeddruk is <strong>duizeligheid bij snel "
                  "rechtstaan</strong>."),
        ]),
        dict(kop="Weefselvocht en lymfe", blokken=[
            ("p", "Weefselvocht ontstaat doordat <strong>de bloeddruk plasma uit het begin van de haarvaten "
                  "perst</strong>, de hydrostatische druk. Aan het einde van het haarvat <strong>is de bloeddruk "
                  "gezakt en trekken de plasma-eiwitten water terug</strong>, de osmotische druk. Weefselvocht "
                  "bevat <strong>veel minder grote eiwitten</strong> dan plasma."),
            ("p", "Het overschot gaat in de <strong>lymfecapillairen</strong> of lymfehaarvaten, de kleinste lymfevaatjes, en heet dan <strong>lymfe</strong>: "
                  "<strong>water, zouten, wat eiwitten en lymfocyten</strong>. Het lymfevatenstelsel brengt "
                  "<strong>het overtollige weefselvocht terug in het bloed</strong>, via de borstbuis, die "
                  "<strong>in een grote ader onder het sleutelbeen</strong> uitmondt."),
            ("p", "<strong>Lymfevaten hebben kleppen</strong>, maar <strong>het lymfestelsel heeft geen eigen "
                  "pomp</strong>. <strong>Werkende spieren knijpen de lymfevaten samen en duwen de lymfe "
                  "vooruit.</strong>"),
        ]),
        dict(kop="De lymfeorganen", blokken=[
            ("p", "Bij het lymfestelsel horen <strong>de milt</strong>, de amandelen, <strong>de zwezerik of "
                  "thymus</strong>, het beenmerg en de lymfeklieren. De schildklier en de alvleesklier horen er "
                  "niet bij."),
            ("p", "In een lymfeklier <strong>wordt de lymfe gefilterd en ruimen lymfocyten ziektekiemen "
                  "op</strong>. <strong>In de thymus rijpen de T-lymfocyten</strong>, onder invloed van het "
                  "hormoon <strong>thymosine</strong>. <strong>De milt ruimt versleten rode bloedcellen "
                  "op</strong>, <strong>bevat veel lymfocyten die het bloed op ziekteverwekkers "
                  "controleren</strong> en <strong>slaat een voorraad bloed op</strong>."),
        ]),
        dict(kop="Oedeem", blokken=[
            ("p", "<strong>Lymfoedeem</strong> is <strong>een zwelling doordat lymfe niet goed afgevoerd "
                  "wordt</strong>. Het kan ontstaan <strong>na het wegnemen van lymfeklieren bij een "
                  "kankeroperatie</strong>, <strong>door bestraling die de lymfevaten beschadigt</strong> of "
                  "<strong>door een aangeboren afwijking aan de lymfevaten</strong>. Men behandelt het "
                  "<strong>met lymfedrainage, steunkousen of een drukverband</strong>, en blijven bewegen helpt."),
            ("p", "Bij <strong>hongeroedeem</strong>, bij kinderen met ernstige ondervoeding, gaat er <strong>door te weinig eiwitten in het bloed minder "
                  "vocht terug in de haarvaten</strong>, zodat de buik opzwelt."),
        ]),
    ],
    onthoud=[
        "Normaal ongeveer 120/80 mmHg; hypertensie vanaf 140/90.",
        "Baroreceptoren meten, het cardiovasculair centrum in het verlengde merg stuurt bij.",
        "Orthosympatisch: sneller; parasympatisch: rustiger.",
        "Renine → angiotensine I → (ACE) angiotensine II → vasoconstrictie en aldosteron.",
        "Lymfe brengt overtollig weefselvocht terug naar het bloed; spieren duwen haar vooruit.",
        "In de thymus rijpen T-lymfocyten (thymosine).",
    ],
)

# ───────────────────────── 7. Het ademhalingsstelsel
BUNDELS["het-ademhalingsstelsel-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Het ademhalingsstelsel",
    onder="De luchtwegen en de longen, hoe je in- en uitademt, hoe gaswisseling werkt, het spirogram en de aandoeningen.",
    secties=[
        dict(kop="De luchtwegen", blokken=[
            ("p", "Ingeademde lucht gaat van de <strong>neusholte</strong> naar de <strong>keelholte</strong>, "
                  "het <strong>strottenhoofd</strong>, de <strong>luchtpijp</strong>, de <strong>bronchiën</strong> "
                  "en <strong>bronchiolen</strong>, tot in de <strong>longblaasjes</strong>, luchtzakjes of alveolen."),
            ("p", "De neusholte <strong>verwarmt de lucht</strong>, bevochtigt ze en <strong>filtert "
                  "stofdeeltjes uit de lucht</strong>. Het <strong>trilhaarepitheel met slijmcellen</strong> "
                  "<strong>vangt stof en ziektekiemen in slijm en voert ze af naar de keel</strong>. Rook "
                  "<strong>beschadigt de trilharen, zodat het slijm niet meer goed afgevoerd wordt</strong>: de "
                  "rokershoest."),
            ("p", "<strong>Kraakbeenringen in de wand</strong> houden de luchtpijp open. Het "
                  "<strong>strottenhoofd</strong> ligt <strong>tussen de keelholte en de luchtpijp, met de "
                  "stembanden erin</strong>. Het <strong>strottenklepje</strong> sluit het strottenhoofd af bij "
                  "het slikken."),
        ]),
        dict(kop="De longen", blokken=[
            ("p", "<strong>De rechterlong heeft drie longkwabben en de linkerlong twee.</strong> Bij <strong>de "
                  "longhilus</strong> gaan de hoofdbronchus, de bloedvaten en de zenuwen de long binnen."),
            ("p", "De longblaasjes zijn ideaal voor gaswisseling: <strong>ze hebben samen een enorm groot "
                  "oppervlak</strong>, <strong>hun wand is erg dun</strong> en <strong>ze zijn omringd door een "
                  "dicht net van haarvaten</strong>. De gaswisseling gebeurt daar, niet in de luchtpijp of de "
                  "bronchiën."),
            ("p", "De <strong>pleuraholte</strong> is <strong>de dunne ruimte met vocht tussen het longvlies en "
                  "het borstvlies</strong>. Dankzij dat pleuravocht volgen de longen de borstkas."),
        ]),
        dict(kop="Inademen en uitademen", blokken=[
            ("p", "Bij de inademing <strong>trekken de ademhalingsspieren samen, wordt de borstholte groter, daalt "
                  "de druk in de longen en stroomt lucht naar binnen</strong>. <strong>De longen hebben geen "
                  "eigen spieren</strong> om zelf uit te zetten."),
            ("p", "Bij de <strong>middenrifademhaling</strong> of buikademhaling <strong>trekt het middenrif "
                  "samen en wordt het platter, zodat de borstholte groter wordt</strong>. Bij de "
                  "<strong>ribademhaling</strong> of borstademhaling heffen <strong>de tussenribspieren</strong> "
                  "de ribben op. <strong>De ware ribben</strong> zitten rechtstreeks aan het borstbeen; valse "
                  "en zwevende ribben niet."),
            ("p", "<strong>Bij een rustige uitademing ontspannen de ademhalingsspieren en veert de borstkas vanzelf "
                  "terug.</strong>"),
        ]),
        dict(kop="Gaswisseling en hemoglobine", blokken=[
            ("p", "Zuurstof en koolstofdioxide gaan <strong>door diffusie</strong> van lucht naar bloed en "
                  "omgekeerd. In de longblaasjes <strong>is de partiële druk van O₂ hoger dan in het bloed van "
                  "de haarvaten</strong>."),
            ("p", "Het evenwicht <strong>deoxyhemoglobine + O₂ ⇌ oxyhemoglobine</strong> volgt het principe van "
                  "Le Chatelier. In de longblaasjes verschuift het <strong>naar rechts, want de O₂-concentratie is "
                  "er hoog</strong>. In de weefsels verschuift het naar de kant van deoxyhemoglobine."),
            ("p", "De <strong>zuurstofaffiniteit</strong> is de mate waarin hemoglobine zuurstof bindt. Hemoglobine "
                  "laat zuurstof makkelijker los bij <strong>een hogere temperatuur</strong>, <strong>een hogere "
                  "CO₂-concentratie</strong> en een lagere pH, dus zuurder, zoals in werkende spieren."),
            ("p", "CO₂ reist <strong>opgelost in het plasma</strong>, <strong>gebonden aan hemoglobine</strong> en, "
                  "voor het grootste deel, <strong>als waterstofcarbonaat (HCO₃⁻) in het plasma</strong>."),
        ]),
        dict(kop="Het spirogram", blokken=[
            ("p", "Een <strong>spirogram</strong> is <strong>een grafiek van het volume lucht dat iemand in- en "
                  "uitademt in de tijd</strong>."),
            ("p", tabel(["Waarde", "Betekenis"], [
                ["<strong>ademvolume</strong> in rust", "de lucht bij een gewone, rustige ademhaling"],
                ["<strong>complementair volume</strong>", "de lucht die je na een gewone inademing nog extra kan "
                 "inademen"],
                ["uitademingsreservevolume", "de lucht die je na een gewone uitademing nog extra kan uitademen"],
                ["<strong>vitale capaciteit</strong>", "<strong>de grootste hoeveelheid lucht die je na een "
                 "maximale inademing kan uitademen</strong>"],
                ["<strong>restvolume</strong>", "<strong>de lucht die na een maximale uitademing nog in de longen "
                 "blijft</strong>"],
                ["<strong>totale longcapaciteit</strong>", "<strong>de vitale capaciteit plus het "
                 "restvolume</strong>"],
            ])),
            ("p", "De vitale capaciteit hangt af van <strong>de leeftijd</strong>, <strong>het geslacht</strong>, "
                  "<strong>roken</strong> en <strong>veel sporten</strong>. <strong>Regelmatig sporten kan de "
                  "vitale capaciteit vergroten.</strong>"),
        ]),
        dict(kop="Aandoeningen", blokken=[
            ("p", tabel(["Aandoening", "Wat er gebeurt"], [
                ["<strong>astma</strong>", "<strong>de bronchiolen vernauwen en zwellen op, zodat ademen moeilijk "
                 "gaat</strong>; een puffer verwijdt ze"],
                ["<strong>mucoviscidose</strong>", "<strong>een erfelijke ziekte waarbij taai slijm de luchtwegen "
                 "en de alvleesklier verstopt</strong>; ze is niet besmettelijk"],
                ["<strong>hyperventilatie</strong>", "<strong>je ademt te snel en te diep, zodat je te veel CO₂ "
                 "uitademt</strong>; rustig ademen helpt"],
            ])),
        ]),
    ],
    onthoud=[
        "Neus → keel → strottenhoofd → luchtpijp → bronchiën → bronchiolen → longblaasjes.",
        "Rechterlong drie kwabben, linkerlong twee.",
        "Inademen: spieren trekken samen, borstholte groter, druk daalt, lucht stroomt in.",
        "Gassen gaan door diffusie; in de longen ontstaat oxyhemoglobine.",
        "Warmte, CO₂ en zuur laten hemoglobine zuurstof loslaten.",
        "Totale longcapaciteit = vitale capaciteit + restvolume.",
    ],
)

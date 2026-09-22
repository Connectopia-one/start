# -*- coding: utf-8 -*-
"""De twee overige bundels voor aardrijkskunde, met eigen tekeningen.

Alle figuren zijn hier getekend en geen foto's. Een doorsnede van de kust of
de lagen van het regenwoud zijn schema's, geen beeld van één bepaalde plek,
dus daar is een tekening zelfs duidelijker dan een foto.

Wat hier bewust NIET in staat is een landkaart. Een kaart uit het hoofd
natekenen wordt scheef, en scheve grenzen horen niet in lesmateriaal. Komt er
later een kaart met een vrije licentie bij, dan hoort die in deze bundels
thuis — met de bronvermelding erbij, zoals in README.md beschreven staat.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import svg, bundel
tabel = bundel.tabel

BUNDELS = {}

BUNDELS["belgie-landschap-en-streken"] = dict(
    vak="Aardrijkskunde", titel="België: landschap en streken",
    onder="Van de duinen aan zee tot het hoogste punt in de Ardennen.",
    secties=[
        dict(kop="Drie gewesten, tien provincies", blokken=[
            ("p", "België is een <strong>federaal land</strong>. Dat betekent dat niet alles in "
                  "Brussel beslist wordt: er is een regering voor het hele land, en daarnaast "
                  "besturen de gewesten en gemeenschappen zelf een groot deel van wat er gebeurt, "
                  "zoals het onderwijs en het openbaar vervoer."),
            ("fig", svg.gewesten(),
             "De tien provincies, met achter elke naam de hoofdplaats van die provincie."),
            ("p", "Brussel is een apart geval. Het is de hoofdstad van België en ligt middenin "
                  "Vlaanderen, maar het hoort bij geen van beide andere gewesten en heeft geen "
                  "provincie. Het bestaat uit negentien gemeenten, en er wordt zowel Nederlands "
                  "als Frans gesproken."),
            ("p", "België heeft vier buurlanden. Aan drie ervan grenst maar een klein stukje land; "
                  "met Frankrijk deelt ons land de langste grens."),
            ("kader", tabel(["Buurland", "Hoofdstad", "Taal die er het meest gesproken wordt"],
                            [["Nederland", "Amsterdam", "Nederlands"],
                             ["Duitsland", "Berlijn", "Duits"],
                             ["Luxemburg", "Luxemburg", "Luxemburgs, Frans en Duits"],
                             ["Frankrijk", "Parijs", "Frans"]])),
            ("weetje", "Nederland heeft twee &#8216;hoofdsteden&#8217; die door elkaar gebruikt worden: "
                       "Amsterdam is officieel de hoofdstad, maar de regering en het parlement "
                       "zitten in Den Haag."),
        ]),
        dict(kop="Van laag naar hoog", blokken=[
            ("p", "Als je van de kust naar het zuidoosten reist, klim je stilaan. Aan zee sta je op "
                  "nul meter hoogte; in de Ardennen loop je boven de zeshonderd meter. Dat hele "
                  "verloop past in nog geen driehonderd kilometer."),
            ("fig", svg.reliefprofiel(),
             "Het hoogteprofiel van België. Let op: de hoogte is veel sterker uitvergroot dan de "
             "afstand, anders zou je van de helling niets zien."),
            ("p", "Geografen delen ons land daarom in drie stukken. <strong>Laag-België</strong> "
                  "ligt onder de honderd meter: de kust, de polders, de Vlaamse zandstreek en de "
                  "Kempen. <strong>Midden-België</strong> ligt tussen honderd en tweehonderd meter, "
                  "met de vruchtbare leemstreek waar veel akkerbouw zit. <strong>Hoog-België</strong> "
                  "ligt boven de tweehonderd meter: de Condroz, de Hoge Venen en de Ardennen."),
            ("p", "Het hoogste punt van België is het <strong>Signal de Botrange</strong> in de Hoge "
                  "Venen, 694 meter. Daar staat een trap van zes meter bovenop, zodat je toch even "
                  "op zevenhonderd meter kan staan."),
        ]),
        dict(kop="De kust en de polders", blokken=[
            ("p", "De Belgische kust is ongeveer <strong>65 kilometer</strong> lang: van De Panne aan "
                  "de Franse grens tot Knokke-Heist aan de Nederlandse. Dat is kort, maar er woont en "
                  "werkt veel volk."),
            ("fig", svg.kustdoorsnede(),
             "Een doorsnede van de kust. De duinenrij houdt de zee tegen; daarachter liggen de polders "
             "lager dan het water."),
            ("p", "De <strong>duinen</strong> zijn heuvels van zand die de wind heeft opgeblazen. Ze "
                  "houden de zee tegen, en daarom mag je er niet zomaar overlopen: het helmgras houdt "
                  "het zand vast, en zonder dat gras waait een duin stuk."),
            ("p", "Achter de duinen liggen de <strong>polders</strong>. Dat is land dat vroeger onder "
                  "water stond en dat mensen drooggelegd hebben met dijken en sloten. Omdat de polders "
                  "lager liggen dan de zee, moet het water er weggepompt worden."),
            ("weetje", "Eb en vloed komen door de aantrekkingskracht van de maan. Aan onze kust is het "
                       "ongeveer twee keer per dag hoogwater en twee keer per dag laagwater."),
        ]),
        dict(kop="Rivieren", blokken=[
            ("p", "Een rivier begint bij de <strong>bron</strong> en eindigt bij de <strong>monding</strong>. "
                  "Onderweg groeit ze aan, want er komen zijrivieren bij. Bovenaan is het water snel en "
                  "de bedding smal; onderaan is de rivier breed en traag en maakt ze bochten."),
            ("fig", svg.rivierloop(),
             "Van bron tot monding. De bochten onderaan heten meanders."),
            ("p", "De twee belangrijkste rivieren van België zijn de <strong>Schelde</strong> en de "
                  "<strong>Maas</strong>. Allebei ontspringen ze in Frankrijk, stromen ze door ons land "
                  "en gaan ze verder door Nederland, om uiteindelijk in de Noordzee te eindigen. De "
                  "Schelde stroomt langs Gent en Antwerpen, de Maas langs Namen en Luik."),
            ("p", "Rivieren bepalen waar steden ontstaan. Waar je kon oversteken of aanleggen, kwam "
                  "handel, en waar handel kwam, groeide een stad. Kijk maar hoeveel Belgische steden "
                  "aan het water liggen."),
        ]),
        dict(kop="Het weer en het klimaat", blokken=[
            ("p", "<strong>Weer</strong> is wat er vandaag buiten gebeurt: het regent, of het vriest. "
                  "<strong>Klimaat</strong> is hoe het weer over heel veel jaren gemiddeld is. Eén koude "
                  "week zegt dus niets over het klimaat."),
            ("fig", svg.klimaatdiagram([4, 4, 7, 10, 14, 16, 18, 18, 15, 11, 7, 4],
                                       [75, 60, 60, 50, 65, 75, 80, 80, 70, 75, 80, 85],
                                       plaats="afgeronde gemiddelden voor Ukkel"),
             "Een klimaatdiagram lees je zo: de blauwe balkjes zijn de neerslag per maand (links, in "
             "millimeter), de rode lijn is de temperatuur (rechts, in graden)."),
            ("p", "België heeft een <strong>zeeklimaat</strong>. De zee warmt traag op en koelt traag af, "
                  "en daardoor zijn onze zomers niet heet en onze winters niet streng. Het valt ook het "
                  "hele jaar door wat regen: er is bij ons geen droog seizoen."),
            ("weetje", "Het is bij ons niet natter in de herfst dan in de zomer, al voelt dat wel zo. "
                       "In de zomer valt de regen in korte, felle buien; in de herfst blijft het langer "
                       "miezeren."),
        ]),
        dict(kop="Wonen: steden en dorpen", blokken=[
            ("p", "Een stad is in de loop van eeuwen laag per laag gegroeid. In het midden ligt de "
                  "<strong>oude kern</strong>, met smalle kronkelende straten rond een markt en een kerk. "
                  "Daaromheen kwamen later bredere straten, en nog verder de <strong>woonwijken</strong> "
                  "met tuinen."),
            ("fig", svg.stadsplan(),
             "Een stad van bovenaf, schematisch. De ring is de weg die het doorgaand verkeer om de kern "
             "heen leidt."),
            ("p", "Bedrijven zitten meestal niet meer in de stad zelf maar op een "
                  "<strong>bedrijventerrein</strong> aan de rand, dicht bij de autosnelweg. Zo rijden de "
                  "vrachtwagens niet door de woonstraten."),
            ("p", "België is een van de dichtstbevolkte landen van Europa: er wonen veel mensen op weinig "
                  "oppervlakte. Daardoor lopen dorpen en steden hier vaak in elkaar over, en zie je "
                  "onderweg zelden een stuk waar helemaal niets staat."),
        ]),
        dict(kop="Werken: de haven", blokken=[
            ("p", "Antwerpen ligt aan de Schelde, tientallen kilometers van de zee, en is toch een "
                  "zeehaven: de Schelde is er diep genoeg voor grote schepen. Het is een van de "
                  "grootste havens van Europa."),
            ("fig", svg.haven(),
             "Een containerkraan tilt de containers van het schip op de kaai. Daar gaan ze verder met "
             "de vrachtwagen, de trein of het binnenschip."),
            ("p", "Bijna alles wat je koopt is ooit in een <strong>container</strong> vervoerd. Die "
                  "stalen kisten hebben allemaal hetzelfde formaat, en juist daardoor werkt het: elke "
                  "kraan, elk schip en elke vrachtwagen past erop."),
            ("weetje", "Een groot containerschip kan meer dan twintigduizend containers vervoeren. Achter "
                       "elkaar gezet zou die lading een file van meer dan honderd kilometer vormen."),
        ]),
    ],
    onthoud=[
        "België heeft drie gewesten (Vlaanderen, Wallonië, Brussel) en tien provincies.",
        "Buurlanden: Nederland, Duitsland, Luxemburg en Frankrijk.",
        "Laag-België tot 100 m, Midden-België 100 tot 200 m, Hoog-België hoger dan 200 m.",
        "Het hoogste punt is het Signal de Botrange, 694 m, in de Hoge Venen.",
        "De kust is ongeveer 65 km lang; achter de duinen liggen de polders, lager dan de zee.",
        "De Schelde en de Maas ontspringen allebei in Frankrijk en eindigen in de Noordzee.",
        "Weer is vandaag, klimaat is het gemiddelde over heel veel jaren.",
        "België heeft een zeeklimaat: zachte winters, koele zomers, het hele jaar neerslag.",
    ])


BUNDELS["europa-en-de-wereld"] = dict(
    vak="Aardrijkskunde", titel="Europa en de wereld",
    onder="Continenten, klimaatgordels en landschappen van ver buiten België.",
    secties=[
        dict(kop="Continenten en oceanen", blokken=[
            ("p", "Het land op aarde ligt in grote stukken bij elkaar: de <strong>continenten</strong>. "
                  "Meestal telt men er zes of zeven, en Europa is daarvan een van de kleinste — al "
                  "wonen er wel veel mensen."),
            ("fig", svg.staafdiagram(
                [("Azië", 45), ("Afrika", 30), ("Noord-Am.", 25), ("Zuid-Am.", 18),
                 ("Antarctica", 14), ("Europa", 10), ("Oceanië", 9)], 470, 190, stap=10),
             "De oppervlakte van de continenten, afgerond, in miljoen vierkante kilometer. "
             "Azië is groter dan Europa en Oceanië samen, vier keer over."),
            ("p", "Tussen de continenten liggen de <strong>oceanen</strong>. De grootste is de Stille "
                  "Oceaan, daarna komen de Atlantische Oceaan en de Indische Oceaan. Rond de polen "
                  "liggen nog de Noordelijke IJszee en de Zuidelijke Oceaan."),
            ("weetje", "Water bedekt ongeveer zeventig procent van de aarde. Van boven gezien is onze "
                       "planeet dus vooral blauw, en dat is ook waarom ze soms de blauwe planeet heet."),
        ]),
        dict(kop="De aardbol: evenaar, keerkringen en polen", blokken=[
            ("p", "Om plaatsen op aarde te kunnen aanduiden, zijn er denkbeeldige lijnen getrokken. De "
                  "belangrijkste is de <strong>evenaar</strong>: die deelt de aarde in een noordelijk "
                  "en een zuidelijk halfrond. België ligt op het noordelijk halfrond."),
            ("fig", svg.aardbolgordels(),
             "De aarde van opzij. Tussen de keerkringen staat de zon 's middags soms recht boven je "
             "hoofd; daarbuiten nooit."),
            ("p", "Hoe verder je van de evenaar af zit, hoe schuiner de zonnestralen op de aarde "
                  "vallen, en hoe kouder het gemiddeld is. Daardoor liggen de klimaten in gordels: "
                  "warm rond de evenaar, koud bij de polen, en daartussen het <strong>gematigde "
                  "gebied</strong> waar België in ligt."),
            ("p", "Op de <strong>noordpool</strong> en de <strong>zuidpool</strong> is het het hele jaar "
                  "koud. Daar gaat de zon in de zomer weken achter elkaar niet onder, en blijft het in "
                  "de winter weken achter elkaar donker."),
        ]),
        dict(kop="Dag en nacht, zomer en winter", blokken=[
            ("p", "De aarde draait in vierentwintig uur één keer rond haar eigen as. De kant die naar "
                  "de zon gekeerd staat heeft dag, de andere kant nacht. Daarnaast draait de aarde in "
                  "een jaar één keer rond de zon."),
            ("fig", svg.seizoenen(),
             "De seizoenen komen niet doordat de aarde dichter bij de zon staat, maar doordat haar as "
             "scheef staat."),
            ("p", "Die scheve as is de reden voor de <strong>seizoenen</strong>. Staat het noordelijk "
                  "halfrond naar de zon gekeerd, dan vallen de stralen daar recht en is het bij ons "
                  "zomer. Een half jaar later is het omgekeerd. Op het zuidelijk halfrond is het dus "
                  "altijd het tegenovergestelde seizoen van bij ons."),
            ("weetje", "In Australië valt Kerstmis midden in de zomer. Daar gaan mensen op 25 december "
                       "gerust naar het strand."),
        ]),
        dict(kop="Hoog in de bergen", blokken=[
            ("p", "Hoe hoger je klimt, hoe kouder het wordt: ongeveer een halve graad per honderd meter. "
                  "Daardoor verandert op een berg het landschap terwijl je stijgt, net alsof je naar "
                  "het noorden reist."),
            ("fig", svg.bergprofiel(),
             "Onderaan weiden en loofbos, daarboven naaldbos, dan alpenweide, en bovenaan sneeuw die "
             "nooit smelt."),
            ("p", "Boven de <strong>boomgrens</strong> groeien geen bomen meer: het is er te koud en de "
                  "wind is er te hard. Boven de <strong>sneeuwgrens</strong> blijft er het hele jaar door "
                  "sneeuw liggen, ook in de zomer."),
            ("p", "De bekendste bergketen van Europa zijn de <strong>Alpen</strong>, die door onder meer "
                  "Frankrijk, Zwitserland, Italië en Oostenrijk lopen. De hoogste top is de "
                  "<strong>Mont Blanc</strong>, ongeveer 4 800 meter — bijna zeven keer zo hoog als het "
                  "hoogste punt van België."),
        ]),
        dict(kop="In de woestijn", blokken=[
            ("p", "Een <strong>woestijn</strong> is een gebied waar bijna geen regen valt: vaak minder dan "
                  "honderdvijftig millimeter per jaar, terwijl er bij ons ruim achthonderd valt. Er "
                  "groeit daardoor bijna niets."),
            ("fig", svg.woestijnduinen(),
             "Bij een oase komt grondwater aan de oppervlakte. Daar kan wel iets groeien, en daar wonen "
             "dus ook mensen."),
            ("p", "De grootste warme woestijn is de <strong>Sahara</strong>, in het noorden van Afrika. "
                  "Overdag kan het er snikheet zijn en 's nachts koud, want zonder wolken en zonder "
                  "vocht houdt de lucht de warmte niet vast."),
            ("weetje", "Niet elke woestijn is warm. Antarctica is ook een woestijn, want er valt bijna "
                       "geen neerslag — alleen ligt daar sneeuw in plaats van zand."),
        ]),
        dict(kop="Het regenwoud", blokken=[
            ("p", "Rond de evenaar is het het hele jaar warm en valt er heel veel regen. Daar groeit het "
                  "<strong>tropisch regenwoud</strong>: het bos met de meeste soorten planten en dieren "
                  "ter wereld."),
            ("fig", svg.regenwoudlagen(),
             "Het regenwoud groeit in lagen. Bovenaan vangt het bladerdak bijna al het licht, zodat het "
             "op de bodem donker is."),
            ("p", "De grootste regenwouden liggen rond de <strong>Amazone</strong> in Zuid-Amerika en "
                  "rond de <strong>Congo</strong> in Afrika. Ze worden op veel plaatsen gekapt, voor hout "
                  "en om landbouwgrond te maken, en dat gaat snel."),
            ("p", "Dat is niet alleen jammer voor de dieren. Bomen halen koolstofdioxide uit de lucht, "
                  "en als het bos verdwijnt, blijft dat gas in de dampkring zitten en warmt de aarde "
                  "verder op."),
        ]),
        dict(kop="Vulkanen en aardbevingen", blokken=[
            ("p", "De buitenste schil van de aarde is geen geheel stuk, maar bestaat uit grote platen die "
                  "heel traag bewegen — enkele centimeter per jaar, ongeveer zo snel als je nagels "
                  "groeien. Waar die platen elkaar raken, beeft de grond en staan vulkanen."),
            ("fig", svg.vulkaan(),
             "Onder een vulkaan zit een kamer vol gesmolten gesteente. Heet dat nog binnenin, dan heet "
             "het magma; ligt het buiten, dan heet het lava."),
            ("p", "Bij een <strong>uitbarsting</strong> wordt er niet alleen lava uitgestoten, maar ook "
                  "as en gas. Die askolom kan kilometers hoog komen, en de as legt soms het vliegverkeer "
                  "van een heel werelddeel stil."),
            ("p", "In België beven er af en toe platen, maar zo licht dat je het zelden voelt. Vulkanen "
                  "zijn er niet meer actief; in de Eifel, net over de Duitse grens, liggen wel de "
                  "restanten van oude vulkanen."),
        ]),
        dict(kop="Europa en de Europese Unie", blokken=[
            ("p", "Na de Tweede Wereldoorlog zochten Europese landen elkaar op, met de gedachte: wie "
                  "samen handelt en samen beslist, voert geen oorlog meer tegen elkaar. Uit die "
                  "samenwerking is de <strong>Europese Unie</strong> gegroeid."),
            ("fig", svg.tijdlijn(
                [("samenwerking na de oorlog", 1945, 1993, "#3b6ea5"),
                 ("de Europese Unie", 1993, 2030, "#2f5d50")],
                [(1957, "Verdrag van Rome", "boven"), (1993, "Europese Unie", "onder"),
                 (2002, "de euro als muntstuk", "boven"), (2020, "Brexit", "onder")],
                470),
             "De EU is er dus niet in één keer gekomen, maar stap voor stap over meer dan zeventig jaar."),
            ("p", "Vandaag zijn er zevenentwintig lidstaten. In een groot deel daarvan betaal je met de "
                  "<strong>euro</strong>, en tussen veel van die landen kan je de grens over zonder dat "
                  "iemand je paspoort vraagt."),
            ("p", "<strong>Brussel</strong> is niet alleen de hoofdstad van België: er zitten ook de "
                  "belangrijkste gebouwen van de Europese Unie. Daardoor werken er duizenden mensen uit "
                  "heel Europa."),
            ("weetje", "Het Verenigd Koninkrijk stapte in 2020 als eerste land weer uit de Europese Unie. "
                       "Dat kreeg de naam Brexit, van <i>Britain</i> en <i>exit</i>."),
        ]),
    ],
    onthoud=[
        "Azië is het grootste continent, Europa een van de kleinste.",
        "De evenaar deelt de aarde in het noordelijk en het zuidelijk halfrond.",
        "Klimaatgordels: tropisch rond de evenaar, gematigd daarbuiten, koud bij de polen.",
        "De seizoenen komen door de scheve as van de aarde, niet door de afstand tot de zon.",
        "Boven de boomgrens groeien geen bomen; boven de sneeuwgrens smelt de sneeuw nooit.",
        "De Mont Blanc in de Alpen is ongeveer 4 800 m hoog.",
        "In een woestijn valt bijna geen regen; bij een oase komt grondwater naar boven.",
        "Magma zit binnenin de aarde, lava ligt buiten.",
        "De Europese Unie telt 27 lidstaten; in veel daarvan betaal je met de euro.",
    ])


if __name__ == "__main__":
    for naam, b in BUNDELS.items():
        bundel.schrijf(b, naam)

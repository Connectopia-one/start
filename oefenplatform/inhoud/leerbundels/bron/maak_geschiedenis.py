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
                  "Alles wat we over die tijd weten, komt uit de grond: werktuigen, botten, resten van vuur."),
            ("fig", svg.stappen(["steentijd", "bronstijd", "ijzertijd"]),
             "De prehistorie wordt ingedeeld naar het materiaal waarvan de mensen hun gereedschap maakten."),
            ("p", "Zodra mensen begonnen te schrijven, stopt de prehistorie. Dat gebeurde niet overal "
                  "op hetzelfde moment: in Mesopotamië en Egypte al rond 3000 v.Chr., bij ons pas toen "
                  "de Romeinen kwamen."),
        ]),
        dict(kop="Leven in de steentijd", blokken=[
            ("p", "In de <strong>oude steentijd</strong> trokken mensen van plaats naar plaats. Ze "
                  "jaagden en verzamelden wat ze vonden, en als het voedsel op was, trokken ze verder. "
                  "Ze woonden graag dicht bij water: daar kwamen de dieren drinken en daar groeiden planten."),
            ("fig", svg.stenen_werktuigen(),
             "Vuursteen splijt in scherpe schilfers. Aan die afslagvlakjes herken je een bewerkte steen van een gewone."),
            ("p", "In de <strong>nieuwe steentijd</strong> veranderde alles: mensen begonnen te boeren. "
                  "Ze zaaiden graan en hielden dieren, en daardoor konden ze op één plek blijven wonen. "
                  "Zo ontstonden de eerste dorpen."),
            ("weetje", "De hond was het eerste dier dat de mens temde, nog vóór de landbouw begon. "
                       "Wolven die bij de kampen bleven rondhangen, werden over vele generaties honden."),
        ]),
        dict(kop="De eerste kunst", blokken=[
            ("p", "Diep in grotten schilderden mensen dieren op de wand: oerrunderen, paarden, herten. "
                  "Ze gebruikten oker voor geel en rood, en houtskool voor zwart. Soms legden ze hun "
                  "hand op de wand en bliezen er verf omheen."),
            ("fig", svg.grotschildering(),
             "Hier nagetekend. De echte schilderingen, zoals in Lascaux, zijn ongeveer 17 000 jaar oud."),
        ]),
        dict(kop="Egypte", blokken=[
            ("p", "Egypte lag rond de <strong>Nijl</strong>. Die rivier overstroomde elk jaar en liet "
                  "vruchtbaar slib achter, waardoor er genoeg graan groeide om een heel rijk te voeden. "
                  "Zonder de Nijl was er in die woestijn niets geweest."),
            ("fig", svg.piramides(),
             "De piramides zijn graven voor de farao's. De grootste, van Cheops, is ongeveer 4 500 jaar oud."),
            ("p", "De Egyptenaren schreven met <strong>hiërogliefen</strong>: kleine tekeningen die samen "
                  "woorden vormen. Sommige tekens staan voor een klank, andere voor een heel woord."),
            ("fig", svg.hierogliefen(),
             "Een cartouche: het ovale kader waarin de naam van een koning werd gezet."),
        ]),
        dict(kop="De Grieken", blokken=[
            ("p", "In Griekenland ontstonden stadstaten, elk met hun eigen bestuur. In <strong>Athene</strong> "
                  "mochten de burgers meestemmen over de stad. Dat was toen bijzonder, al was het nog lang "
                  "geen democratie zoals wij die kennen: vrouwen, slaven en vreemdelingen telden niet mee."),
            ("fig", svg.griekse_tempel(),
             "Het Parthenon in Athene. Een Griekse tempel rust op zuilen, met bovenaan een driehoekig fronton."),
            ("p", "De Grieken bedachten ook het <strong>theater</strong>, met toneelstukken die mensen "
                  "samen kwamen bekijken, en de <strong>Olympische Spelen</strong>, die om de vier jaar "
                  "werden gehouden."),
        ]),
        dict(kop="De Romeinen", blokken=[
            ("p", "Het Romeinse Rijk had <strong>Rome</strong> als hoofdstad en strekte zich uit rond de "
                  "Middellandse Zee. Die zee lag er middenin, wat het reizen en handel drijven veel "
                  "eenvoudiger maakte. De Romeinen spraken Latijn en schreven met ons alfabet."),
            ("fig", svg.amfitheater(),
             "Een amfitheater: een rond gebouw met oplopende zitrijen rond een arena. Het Colosseum in Rome is het bekendste."),
            ("p", "Romeinen bouwden ook wat een stad nodig heeft: <strong>aquaducten</strong> die water "
                  "van ver aanvoerden, <strong>thermen</strong> waar iedereen ging baden, en het "
                  "<strong>forum</strong>, het plein waar men handel dreef en nieuws uitwisselde."),
            ("fig", svg.aquaduct(),
             "Het water liep bovenin, in een goot met een héél lichte helling, soms tientallen kilometers ver."),
        ]),
        dict(kop="De Romeinse wegen", blokken=[
            ("p", "De <strong>heirbanen</strong> waren aangelegd voor het leger: soldaten moesten snel van "
                  "de ene plek naar de andere kunnen. Ze liepen zo recht mogelijk, want dat is de kortste weg."),
            ("fig", svg.heirbaan(),
             "Vier lagen op elkaar, en bovenaan bol gelegd zodat het regenwater naar de kant liep. Daarom lagen sommige stukken er eeuwen later nog."),
            ("p", "Onze streken noemden de Romeinen <strong>Gallia Belgica</strong>, naar de Belgae die er "
                  "woonden. Julius Caesar schreef over hen. Rijke Romeinen bouwden hier grote "
                  "landbouwbedrijven, de <strong>villa's</strong>."),
            ("weetje", "De Romeinen brachten hier steden, stenen wegen, munten met de kop van de keizer, "
                       "en het Latijn. Veel Nederlandse woorden komen er nog van: muur, straat, keuken, wijn."),
        ]),
    ],
    onthoud=[
        "Prehistorie = de tijd vóór het schrift; steentijd, bronstijd, ijzertijd.",
        "In de nieuwe steentijd begon de landbouw, en gingen mensen op één plek wonen.",
        "Egypte dankte alles aan de Nijl; de farao's kregen piramides als graf.",
        "De Grieken bouwden tempels op zuilen en bedachten theater en Olympische Spelen.",
        "Rome was de hoofdstad van het Romeinse Rijk; de Middellandse Zee lag er middenin.",
        "De Romeinen legden heirbanen aan voor hun leger, in lagen en zo recht mogelijk.",
        "Onze streken heetten bij hen Gallia Belgica.",
    ])


BUNDELS["van-de-middeleeuwen-tot-nu"] = dict(
    vak="Geschiedenis", titel="Van de middeleeuwen tot nu",
    onder="Van ridders en kloosters, via stoom en mijnen, tot de wereld van vandaag.",
    secties=[
        dict(kop="De middeleeuwen", blokken=[
            ("p", "Na de val van Rome viel het rijk uiteen in kleine gebieden. Een <strong>leenheer</strong> "
                  "gaf grond aan iemand die hem daarvoor trouw en hulp in de oorlog beloofde. Zo hing alles "
                  "aan elkaar van afspraken tussen heren en hun leenmannen."),
            ("fig", svg.burcht(),
             "Een burcht op een heuvel of aan een rivier: van daaruit zie je de vijand van ver aankomen, en water is een extra muur."),
            ("p", "De meeste mensen waren <strong>boer</strong>. Zij werkten het land van de heer en "
                  "verlieten hun dorp bijna nooit. Lezen en schrijven konden ze niet; dat was voorbehouden "
                  "aan een kleine groep."),
        ]),
        dict(kop="Steden en ambachten", blokken=[
            ("p", "In Vlaanderen groeiden de steden rijk door de <strong>lakenhandel</strong>: wol uit "
                  "Engeland werd hier tot fijn laken geweven en over heel Europa verkocht. Gent, Brugge en "
                  "Ieper hoorden bij de grootste steden van Europa."),
            ("p", "Wie een <strong>ambacht</strong> uitoefende — smid, bakker, wever — hoorde bij een "
                  "<strong>gilde</strong>. Dat gilde bepaalde wie het vak mocht uitoefenen, bewaakte de "
                  "kwaliteit en hielp leden die ziek werden."),
            ("weetje", "In 1302 versloegen Vlaamse stedelingen te voet een Frans ridderleger bij Kortrijk: "
                       "de Guldensporenslag. Dat voetvolk uit de steden won het van ridders te paard, en "
                       "dat was in die tijd hoogst ongewoon."),
        ]),
        dict(kop="Boeken met de hand", blokken=[
            ("p", "In de kloosters schreven <strong>monniken</strong> boeken over, letter voor letter. "
                  "Aan één boek werkte iemand soms een jaar. Daarom waren boeken zeldzaam en duur, en "
                  "bezat bijna niemand er een."),
            ("fig", svg.verlucht_handschrift(),
             "Een verlucht handschrift: de beginletter van een hoofdstuk werd groot en met kleur versierd."),
        ]),
        dict(kop="De boekdrukkunst", blokken=[
            ("p", "Rond 1450 maakte <strong>Johannes Gutenberg</strong> in Duitsland de boekdrukkunst met "
                  "<strong>losse letters</strong> bekend. Je zet de letters één keer klaar in een bak, en "
                  "drukt er daarna honderden vellen mee."),
            ("fig", svg.drukpers(),
             "De schroef duwt de pers op het papier. Wat vroeger een jaar overschrijven kostte, was nu een dag drukken."),
            ("p", "Daardoor werden boeken veel goedkoper en verspreidden ideeën zich sneller dan ooit. "
                  "Meer mensen leerden lezen."),
        ]),
        dict(kop="De wereld wordt groter", blokken=[
            ("p", "In <strong>1492</strong> bereikte Christoffel Columbus Amerika, al dacht hij zelf dat "
                  "hij in Indië was aangekomen. <strong>Magellaan</strong> vertrok in 1519; zijn "
                  "expeditie voer als eerste rond de hele aarde."),
            ("p", "In de 18de eeuw kwam de <strong>Verlichting</strong>: denkers vonden dat je niet alles "
                  "moet geloven omdat het altijd zo geweest is, maar dat je zelf moet nadenken en dingen "
                  "moet onderzoeken. Daar komen veel van onze rechten uit voort."),
        ]),
        dict(kop="De industriële revolutie", blokken=[
            ("p", "Vanaf de 19de eeuw werd er niet meer thuis of in een werkplaats gewerkt, maar in "
                  "<strong>fabrieken</strong>. De motor daarachter was de <strong>stoommachine</strong>. "
                  "Het begon in Engeland en kwam daarna naar onze streken."),
            ("fig", svg.stoommachine(),
             "Vuur kookt water tot stoom, de stoom duwt de zuiger op en neer, en het vliegwiel maakt daar een ronddraaiende beweging van."),
            ("p", "Er werkten ook kinderen in die fabrieken, soms twaalf uur per dag, voor weinig geld en "
                  "in gevaarlijke omstandigheden. Pas met de <strong>leerplicht</strong> moesten kinderen "
                  "naar school in plaats van naar het werk."),
            ("weetje", "Vrouwen mochten in België pas vanaf 1948 meestemmen bij de nationale verkiezingen. "
                       "Stemrecht en leerplicht lijken vanzelfsprekend, maar er is lang voor gevochten."),
        ]),
        dict(kop="De mijnen in Limburg", blokken=[
            ("p", "Fabrieken en stoommachines draaien op <strong>steenkool</strong>. In Limburg werd die "
                  "uit de grond gehaald: mijnwerkers gingen met een kooi honderden meters diep, en werkten "
                  "daar in smalle gangen."),
            ("fig", svg.mijnschacht(),
             "Boven de schacht staat de schachtbok. De wielen bovenaan winden de kabel op waaraan de kooi hangt."),
            ("p", "Er kwamen mensen uit heel Europa naar Limburg werken. De mijnen sloten in de jaren "
                  "tachtig en negentig, maar de gebouwen staan er nog, vaak met een nieuwe bestemming."),
        ]),
        dict(kop="De 20ste eeuw en daarna", blokken=[
            ("p", "De 20ste eeuw kende <strong>twee wereldoorlogen</strong>. De Eerste duurde van 1914 tot "
                  "1918, de Tweede van 1939 tot 1945 — die laatste dus langer. Tijdens de Tweede "
                  "Wereldoorlog werden miljoenen Joden en andere groepen vermoord: de <strong>Holocaust</strong>."),
            ("fig", svg.tijdlijn(
                [("middeleeuwen", 1000, 1500, "#c17f2b"),
                 ("nieuwe tijd", 1500, 1800, "#3b6ea5"),
                 ("nieuwste tijd", 1800, 2030, "#7a5230")],
                [(1302, "Guldensporenslag", "boven"), (1492, "Columbus", "onder"),
                 (1830, "België", "boven"), (1945, "einde WO II", "onder")],
                470),
             "Let op de schaal: de middeleeuwen duurden veel langer dan de nieuwste tijd, maar er staan minder jaartallen op."),
            ("p", "Daarna zochten Europese landen elkaar juist op. Uit die samenwerking groeide de "
                  "<strong>Europese Unie</strong>, onder meer om oorlog tussen die landen te voorkomen. "
                  "In veel van die landen betaal je nu met de euro."),
            ("p", "In <strong>1969</strong> zette voor het eerst een mens voet op de maan. En met het "
                  "<strong>internet</strong> kan iedereen vandaag in een seconde informatie delen met de "
                  "hele wereld — iets waar een middeleeuwse monnik een jaar over deed voor één boek."),
        ]),
    ],
    onthoud=[
        "Middeleeuwen: leenheren, boeren en kastelen; bijna niemand kon lezen.",
        "De Vlaamse steden werden rijk van de lakenhandel; ambachtslui zaten in gilden.",
        "Gutenberg maakte rond 1450 het drukken met losse letters bekend.",
        "Columbus bereikte Amerika in 1492.",
        "De industriële revolutie draaide op de stoommachine en op steenkool.",
        "WO I: 1914-1918. WO II: 1939-1945, dus de Tweede duurde langer.",
        "België werd onafhankelijk in 1830; vrouwen stemden pas vanaf 1948 mee.",
    ])


if __name__ == "__main__":
    for naam, b in BUNDELS.items():
        bundel.schrijf(b, naam)

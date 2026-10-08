# -*- coding: utf-8 -*-
"""De leerbundels voor statistiek op 🌍 Beyond-niveau (doorstroomfinaliteit).

Gebaseerd op de vakfiche statistiek 3de graad doorstroom (2027_Statistiek_3DO),
geldig vanaf 1 januari 2027. Die fiche geldt voor één richting: humane
wetenschappen.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim laadt de bundel dus
twee keer op, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../beyond/statistiek.json` doet
daar het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

Twee dingen die dit vak anders maken dan de andere:

1. Zo goed als elk leerdoel van de fiche zegt "met ICT". De bundels zeggen er
   dus telkens bij welk scherm van GeoGebra je nodig hebt: de gewone
   rekenmachine, de kansrekenmachine of het rekenblad. Die drie knoppen staan
   in het tabblad Rekenmachine van elk hoofdstuk.
2. Telproblemen gaan hier enkel over faculteit en combinaties. Permutaties,
   variaties en herhalingen staan niet in de fiche en horen hier dus ook niet
   in, hoe verleidelijk ze ook zijn.

Wiskunde staat hier in woorden en niet in symbolen, zoals bij de andere
Beyond-vakken: het platform toont de vraagtekst als gewone tekst. Enkel de
notaties die de fiche zelf oplegt (X ~ B(n; p), Z, mu, sigma, p-dakje) staan
er als symbool, want die moet een leerling kunnen lezen.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, svg

VAK = "Statistiek"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 1. Problemen oplossen en ICT gebruiken
BUNDELS["problemen-oplossen-en-ict-gebruiken-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Problemen oplossen en ICT gebruiken",
    onder="Hoe je een opgave aanpakt, welke hulpmiddelen je mag gebruiken en hoe het examen eruitziet.",
    secties=[
        dict(kop="Een vraagstuk en een probleem zijn niet hetzelfde", blokken=[
            ("p", "De vakfiche maakt een onderscheid dat de moeite waard is. Bij een "
                  "<strong>vraagstuk</strong> weet je meteen welke werkwijze je moet gebruiken: de opgave "
                  "zegt het zowat zelf. Bij een <strong>probleem</strong> is dat niet zo. Je moet eerst "
                  "zelf uitzoeken welke aanpak hier past, en <strong>je kiest zelf welke strategie je "
                  "gebruikt</strong>. Twee leerlingen mogen dus een ander pad nemen naar hetzelfde juiste "
                  "antwoord."),
            ("p", "Een opgave kan ook <strong>met of zonder context</strong> gesteld worden. "
                  "Een <strong>opgave met context</strong> vertrekt van een concrete situatie uit de "
                  "wereld rondom ons: een enquête, een productielijn, een steekproef van zeshonderd "
                  "mensen. Een <strong>opgave zonder context</strong> is abstract en zuiver wiskundig: "
                  "bereken C(12, 5). Dezelfde leerstof kan je op allebei de manieren gevraagd worden, "
                  "afhankelijk van het leerdoel."),
        ]),
        dict(kop="De vier stappen", blokken=[
            ("fig", svg.stappen(["begrijp het|probleem", "maak een|plan",
                                 "voer het|plan uit", "reflecteer"]),
             "De vier stappen uit de vakfiche. De laatste wordt het vaakst overgeslagen."),
            ("p", "In de stap <strong>reflecteren</strong> kijk je of je uitkomst redelijk is en of je "
                  "werkwijze klopte. Dat is geen beleefdheidsformule maar een echte controle, en in "
                  "statistiek betrapt ze je bijna altijd. Een <strong>kans ligt tussen nul en één</strong>: "
                  "krijg je 1,25, dan zit er een fout in je berekening. Een "
                  "<strong>p-waarde is ook een kans</strong> en kan dus niet negatief zijn; vind je min "
                  "0,03, dan zoek je de fout in plaats van hem op te schrijven."),
            ("kader", "<p><strong>Mathematiseren</strong> is een concreet probleem omzetten in "
                      "wiskundetaal en wiskundige symbolen. <strong>Demathematiseren</strong> is het "
                      "omgekeerde: je wiskundige uitkomst terugvertalen naar de situatie.</p>"
                      "<p>Dat tweede vergeet men het vaakst. Reken je uit dat je steekproef 23,7 mensen "
                      "groot moet zijn, dan is je antwoord <strong>24</strong>: je rondt naar boven af, "
                      "want een steekproef bestaat uit hele mensen en 23 zijn er te weinig.</p>"),
            ("p", "Bij het mathematiseren helpt het om <strong>variabelen in te voeren</strong>. Je kan "
                  "dan het verband tussen de gegevens opschrijven zonder alle getallen al te kennen, en "
                  "pas op het einde invullen wat je weet."),
        ]),
        dict(kop="Heuristieken: manieren om op gang te komen", blokken=[
            ("p", "Een <strong>heuristiek</strong> is een oplossingsstrategie: een manier van aanpakken "
                  "die vaak werkt, zonder garantie. Je kiest er zelf een, en je mag er halverwege een "
                  "andere bij nemen."),
            ("p", tabel(["Heuristiek", "Wat je doet", "Wanneer handig"], [
                ["een schets of tabel maken", "je zet de gegevens in een tekening of in rijen en kolommen",
                 "als je door de tekst het verband niet ziet"],
                ["alle mogelijkheden opsommen", "je schrijft de gevallen één voor één op",
                 "bij een klein telprobleem, of om je formule te controleren"],
                ["patronen en regelmaat ontdekken", "je rekent enkele kleine gevallen uit en zoekt wat er telkens hetzelfde gaat",
                 "als de opgave over n gaat en n groot is"],
                ["slim gissen en testen", "je kiest een redelijke waarde, test ze en past ze aan",
                 "als je uit een fout gok leert welke richting je verder moet zoeken"],
                ["terugrekenen", "je vertrekt van het gevraagde eindresultaat naar de gegevens",
                 "als je weet waar je moet uitkomen"],
            ])),
            ("weetje", "Een schets of een tabel maken <strong>telt mee als wiskundig werk</strong>. Het "
                       "is geen kladwerk dat je achteraf uitgomt: het hoort bij je oplossing en levert "
                       "punten op."),
        ]),
        dict(kop="Het examen zelf", blokken=[
            ("p", tabel(["Wat", "Hoe het zit"], [
                ["duur", "150 minuten"],
                ["waar", "in het examencentrum in Brussel"],
                ["gewicht", "telproblemen, kansrekenen en statistiek 60 %, werken met grote datasets 40 %"],
                ["giscorrectie", "nee, een fout antwoord kost geen punten"],
                ["afsluiten", "pas vanaf een kwartier na de start"],
                ["je krijgt", "een balpen, kladpapier en een hoofdtelefoon"],
                ["hulpmiddelen", "de rekenapps van de examencommissie en een online wetenschappelijk rekentoestel"],
                ["eigen rekentoestel", "nee, dat mag je niet meebrengen"],
                ["samenvatting meebrengen", "nee, dat geldt als examenfraude"],
                ["sommige vragen", "noteer je met een digitale pen op een schrijftablet"],
            ])),
            ("p", "<strong>ICT is geen extraatje in dit vak.</strong> Je moet ermee grafische "
                  "voorstellingen kunnen maken, kengetallen berekenen en een volledig onderzoek kunnen "
                  "uitvoeren. Oefen er dus thuis mee: op het examen verlies je tijd als je de rekenapps "
                  "dan pas moet leren bedienen."),
            ("kader", "<p>Bij <strong>functioneel gebruik van ICT</strong> moet je je tussenstappen nog "
                      "altijd uitschrijven. Een antwoord dat enkel uit het resultaat van een rekenapp "
                      "bestaat, volstaat niet: bij open vragen kijkt de examencommissie ook naar je "
                      "werkwijze, niet enkel naar je eindantwoord.</p>"
                      "<p>Staat er een <strong>icoon dat zegt dat je de vraag zonder ICT moet "
                      "oplossen</strong>, dan reken je met de hand, toon je elke tussenstap en werk je "
                      "exact.</p>"),
            ("p", "<strong>Exact werken</strong> betekent dat je breuken, wortels en logaritmen laat "
                  "staan in plaats van ze te benaderen. Moet je toch met kommagetallen verder, werk dan "
                  "met zo nauwkeurig mogelijke tussenresultaten: een afgerond tussenresultaat brengt je "
                  "eindantwoord verder van de waarheid."),
            ("weetje", "Bij de vakfiche hoort een <strong>bijlage met begrippen en notaties</strong>. Die "
                       "staat er omdat handboeken en websites verschillende symbolen gebruiken voor "
                       "hetzelfde. Op het examen gelden de notaties van die bijlage."),
        ]),
    ],
    onthoud=[
        "Vier stappen: begrijp het probleem, maak een plan, voer het plan uit, reflecteer.",
        "Mathematiseren is de situatie in wiskundetaal zetten, demathematiseren is je uitkomst terugvertalen. 23,7 mensen worden 24 mensen.",
        "Een kans en een p-waarde liggen altijd tussen nul en één. Ligt je uitkomst erbuiten, dan is er een rekenfout.",
        "Het examen duurt 150 minuten, zonder giscorrectie, met de rekenapps van de examencommissie en niet met je eigen rekentoestel.",
        "60 % telproblemen, kansrekenen en statistiek; 40 % werken met grote datasets.",
        "Ook met ICT schrijf je je tussenstappen uit.",
    ],
)

# ───────────────────────── 2. De telregels: product, som en complement
BUNDELS["de-telregels-product-som-en-complement-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De telregels: product, som en complement",
    onder="Drie regels om te tellen zonder alles op te schrijven: en, of, en niet.",
    secties=[
        dict(kop="De productregel: eerst dit, dan dat", blokken=[
            ("p", "Je gebruikt de <strong>productregel</strong> als je <strong>na elkaar</strong> een "
                  "eerste en een tweede keuze maakt. Heeft de eerste keuze a mogelijkheden en de tweede "
                  "b, dan zijn er samen <strong>a maal b</strong> mogelijkheden. Het voegwoord dat je "
                  "hoort is <strong>en</strong>: een voorgerecht én een hoofdgerecht."),
            ("fig", svg.mogelijkhedenboom(["soep", "salade", "paté"], ["vis", "vlees"]),
             "Drie voorgerechten en twee hoofdgerechten: zes menu's. Elke tak bovenaan splitst in twee."),
            ("p", "Een menu met <strong>vier</strong> voorgerechten en <strong>zes</strong> "
                  "hoofdgerechten geeft dus <strong>vierentwintig</strong> menu's van twee gangen. Vijf "
                  "voorgerechten en vier hoofdgerechten geven er <strong>twintig</strong>."),
            ("p", "De regel geldt <strong>niet alleen voor twee keuzes</strong>: je mag hem zo vaak "
                  "herhalen als er stappen zijn. Drie soepen, vijf hoofdgerechten en twee desserts geven "
                  "3 · 5 · 2 = <strong>dertig</strong> driegangenmenu's. De twee keuzes moeten ook "
                  "<strong>niet evenveel mogelijkheden hebben</strong>; dat maakt niets uit."),
            ("p", tabel(["Opgave", "Berekening", "Aantal"], [
                ["code van 3 cijfers, 0 tot 9, herhaling mag", "10 · 10 · 10", "1000"],
                ["pincode van 4 cijfers, herhaling mag", "10 tot de vierde", "10 000"],
                ["fietsslot met 4 ringen van 0 tot 9", "10 tot de vierde", "10 000"],
                ["nummerplaat: 3 letters en dan 3 cijfers", "26 tot de derde maal 10 tot de derde", "17 576 000"],
                ["wachtwoord: 2 letters en dan 2 cijfers", "26 · 26 · 10 · 10", "67 600"],
                ["hoorntje met 2 bollen uit 10 smaken, volgorde telt, dezelfde smaak mag", "10 · 10", "100"],
                ["hetzelfde, maar niet twee keer dezelfde smaak", "10 · 9", "90"],
            ])),
            ("kader", "Bij dat laatste hoorntje valt er voor de tweede bol <strong>één smaak weg</strong>, "
                      "namelijk die van de eerste. Dat de tweede keuze van de eerste afhangt, is geen "
                      "probleem: zolang er voor de tweede keuze telkens <strong>even veel</strong> "
                      "mogelijkheden zijn, mag je gewoon vermenigvuldigen."),
        ]),
        dict(kop="De somregel: dit of dat", blokken=[
            ("p", "Kies je <strong>één</strong> ding uit twee groepen, dan <strong>tel je de aantallen "
                  "op</strong>. Het voegwoord is <strong>of</strong>. Drie talen en vijf sporten, en je "
                  "kiest één activiteit: <strong>acht</strong> keuzes. Twaalf meisjes en acht jongens, en "
                  "je vaardigt één leerling af: <strong>twintig</strong> keuzes. Zes keuzevakken waaruit "
                  "je er één neemt: <strong>zes</strong>."),
            ("p", "Er is wel een voorwaarde: de twee groepen <strong>mogen elkaar niet overlappen</strong>. "
                  "Overlappen ze wel, dan mag je de aantallen niet zomaar optellen, want wie in allebei "
                  "zit, tel je dan dubbel. Je trekt de overlap er één keer weer af."),
            ("fig", svg.venndiagram("Frans", "Duits", 11, 4, 8),
             "Vijftien volgen Frans, twaalf volgen Duits, vier volgen allebei. Samen 11 + 4 + 8 = 23 leerlingen."),
            ("p", "Dus: 15 + 12 − 4 = <strong>drieëntwintig</strong> leerlingen volgen minstens één van "
                  "de twee. Reken altijd even na of de stukken samen kloppen met het totaal; dat is de "
                  "snelste controle die er is."),
        ]),
        dict(kop="De complementregel: alles min wat niet telt", blokken=[
            ("p", "Het <strong>complement</strong> van een verzameling is alles wat <strong>niet</strong> "
                  "aan de voorwaarde voldoet. De <strong>complementregel</strong> zegt: het aantal "
                  "gevallen dat voldoet is <strong>het totaal min het aantal dat niet voldoet</strong>."),
            ("p", "Dat lijkt een omweg, en soms is het dat ook. Maar bij <strong>minstens</strong>-vragen "
                  "bestaat het tegengestelde geval vaak uit veel minder mogelijkheden, en dan is het de "
                  "kortste weg. Het complement van <strong>hoogstens twee</strong> is <strong>minstens "
                  "drie</strong>; het complement van <strong>minstens één</strong> is <strong>geen "
                  "enkele</strong>."),
            ("p", tabel(["Vraag", "Totaal", "Wat niet voldoet", "Antwoord"], [
                ["3 keer munt gooien, minstens één keer kop", "2 tot de derde = 8", "nul keer kop: 1", "7"],
                ["4 keer munt gooien, alle uitkomsten", "2 tot de vierde", "—", "16"],
                ["2 dobbelstenen, minstens één zes", "36", "geen zes: 5 · 5 = 25", "11"],
                ["code van 4 cijfers, niet 4 gelijke", "10 000", "4 gelijke: 10", "9990"],
                ["10 waar-of-niet-waarvragen invullen", "2 tot de tiende", "—", "1024"],
                ["daarvan met minstens één fout", "1024", "helemaal juist: 1", "1023"],
                ["25 leerlingen, 7 zonder fiets", "25", "7", "18"],
                ["getal van 3 cijfers dat niet met nul begint", "9 · 10 · 10", "—", "900"],
            ])),
            ("weetje", "De complementregel werkt <strong>alleen als je het totale aantal mogelijkheden "
                       "kent</strong>. Weet je dat niet, dan heb je niets om van af te trekken. En het "
                       "resultaat is altijd kleiner dan het totaal: wordt je antwoord groter, dan heb je "
                       "opgeteld in plaats van afgetrokken."),
            ("p", "Je hoeft het woordje <strong>niet</strong> niet letterlijk in de opgave te zien staan "
                  "om de regel te mogen gebruiken. <em>Minstens</em>, <em>op zijn minst</em> en "
                  "<em>ten minste één</em> zijn alle drie uitnodigingen om het tegengestelde te tellen."),
        ]),
        dict(kop="De drie regels door elkaar", blokken=[
            ("p", "Een opgave gebruikt vaak twee regels tegelijk. <strong>Splits ze dan in stukken</strong> "
                  "en kijk per stuk of het een <em>en</em>, een <em>of</em>, of een <em>niet</em> is."),
            ("p", "Een fietspad loopt via drie wegen naar het park en van daar via vier wegen naar school: "
                  "dat is een <em>en</em>, dus 3 · 4 = <strong>twaalf</strong> routes. Van vijftig mensen "
                  "fietsen er dertig, nemen er vijfentwintig de bus en doen er tien allebei: dat zijn "
                  "30 + 25 − 10 = 45 mensen, dus <strong>vijf</strong> doen geen van beide. Daar zitten "
                  "de somregel met overlap en de complementregel in één opgave."),
        ]),
    ],
    onthoud=[
        "Productregel: eerst dit én dan dat, dus vermenigvuldigen. Je mag hem zo vaak herhalen als er stappen zijn.",
        "Somregel: dit óf dat, dus optellen, maar alleen als de groepen elkaar niet overlappen. Overlappen ze wel, trek de overlap er één keer af.",
        "Complementregel: het totaal min wat niet voldoet. Bij minstens-vragen is dat bijna altijd de kortste weg.",
        "Het complement van minstens één is geen enkele; dat van hoogstens twee is minstens drie.",
        "Splits een gemengde opgave in stukken en kijk per stuk of het en, of, of niet is.",
    ],
)

# ───────────────────────── 3. Faculteit en combinaties
BUNDELS["faculteit-en-combinaties-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Faculteit en combinaties",
    onder="Kiezen zonder dat de volgorde telt, met de formule uit het formularium.",
    secties=[
        dict(kop="Faculteit", blokken=[
            ("p", "De <strong>faculteit</strong> van n, geschreven als n!, is het product van alle "
                  "getallen van één tot n. Dus <strong>5! is vijf maal vier maal drie maal twee maal "
                  "één</strong>, en dat is honderdtwintig. <strong>6! is 720</strong>."),
            ("p", "Eén afspraak moet je uit het hoofd kennen: <strong>0! is gelijk aan één</strong>. Dat "
                  "is geen grap maar een noodzaak, anders klopt de formule van de combinaties niet meer "
                  "in de randgevallen."),
            ("weetje", "Faculteiten lopen razendsnel op: 10! is al meer dan drie miljoen, 20! heeft "
                       "negentien cijfers. Bij <strong>C(18, 3)</strong> is het dus "
                       "<strong>geen goed idee</strong> om eerst 18! volledig uit te rekenen. Je deelt de "
                       "factoren tegen elkaar weg voor je vermenigvuldigt."),
        ]),
        dict(kop="Combinaties: de volgorde telt niet", blokken=[
            ("p", "Bij een <strong>combinatie</strong> maakt de volgorde van de gekozen elementen "
                  "<strong>niets</strong> uit. Een jury van vijf is dezelfde jury, in welke volgorde je "
                  "de namen ook opschrijft. Telt de volgorde wél, dan heb je geen combinatie nodig maar "
                  "de productregel uit het vorige thema."),
            ("kader", "<p>In het formularium staat: het aantal combinaties van <strong>p</strong> "
                      "elementen uit <strong>n</strong> elementen is</p>"
                      "<p style=\"text-align:center;\"><strong>C(n, p) = n! gedeeld door p! maal (n − p)!</strong></p>"
                      "<p>De <strong>p! in de noemer</strong> staat er om de volgordes van de gekozen "
                      "elementen weer weg te delen. Zonder die deling tel je elke keuze p! keer.</p>"),
            ("p", "Dat laatste is dé klassieke fout. Je moet uit vier vrienden er twee kiezen en je "
                  "rekent 4 · 3 = 12 uit. Dan heb je <strong>elk paar twee keer geteld</strong>, want "
                  "Anna-en-Bram is hetzelfde duo als Bram-en-Anna. Het antwoord is <strong>zes</strong>. "
                  "Dezelfde fout bij C(9, 4): wie 9 · 8 · 7 · 6 = 3024 opschrijft, is de deling door 4! "
                  "vergeten; het antwoord is <strong>honderdzesentwintig</strong>."),
            ("p", tabel(["Eigenschap", "Waarom", "Voorbeeld"], [
                ["C(n, 0) = 1", "er is precies één manier om niets te kiezen", "C(7, 0) = 1"],
                ["C(n, 1) = n", "je kiest er één, dus n keuzes", "C(10, 1) = 10"],
                ["C(n, p) = C(n, n − p)", "wie er p kiest, laat er juist n − p liggen", "C(8, 3) = C(8, 5) = 56"],
                ["C(n, p) is altijd een geheel getal", "de deling gaat altijd op, ook al staat er een breuk", "C(45, 6) = 8 145 060"],
            ])),
        ]),
        dict(kop="Rekenen met C(n, p)", blokken=[
            ("p", "Reken ze een keer met de hand uit, en daarna met de kansrekenmachine. Je vindt C(n, p) "
                  "op de gewone rekenmachine van GeoGebra als <strong>nCr(n, p)</strong>."),
            ("p", tabel(["Berekening", "Uitwerking", "Uitkomst"], [
                ["C(5, 2)", "(5 · 4) gedeeld door 2", "10"],
                ["C(6, 2)", "(6 · 5) gedeeld door 2", "15"],
                ["C(6, 3)", "(6 · 5 · 4) gedeeld door 6", "20"],
                ["C(7, 3)", "(7 · 6 · 5) gedeeld door 6", "35"],
                ["C(10, 2)", "(10 · 9) gedeeld door 2", "45"],
                ["C(11, 2)", "(11 · 10) gedeeld door 2", "55"],
                ["C(9, 5)", "gelijk aan C(9, 4)", "126"],
                ["C(12, 5)", "", "792"],
                ["C(20, 2)", "(20 · 19) gedeeld door 2", "190"],
                ["C(25, 3)", "(25 · 24 · 23) gedeeld door 6", "2300"],
                ["C(30, 2)", "(30 · 29) gedeeld door 2", "435"],
            ])),
            ("weetje", "Op het examen volstaat het <strong>niet</strong> om enkel de uitkomst van "
                       "C(n, p) te noteren. Schrijf erbij welke combinatie je berekent en waarom het een "
                       "combinatie is; dat is het deel waarvoor je punten krijgt."),
        ]),
        dict(kop="Herkennen in een opgave", blokken=[
            ("p", tabel(["Opgave", "Waarom een combinatie", "Berekening"], [
                ["drie boeken uit tien meenemen op reis", "de volgorde in je koffer telt niet", "C(10, 3) = 120"],
                ["twee leerlingen uit twintig het bord laten wissen", "geen rolverdeling", "C(20, 2) = 190"],
                ["een jury van vijf uit negen kandidaten", "een jury is een groep", "C(9, 5) = 126"],
                ["een ploeg van vijf uit twaalf spelers", "idem", "C(12, 5) = 792"],
                ["zes Lottogetallen uit vijfenveertig", "de trekvolgorde doet er niet toe", "C(45, 6)"],
                ["drie verschillende gebakjes uit acht soorten", "je zak is één geheel", "C(8, 3) = 56"],
                ["vier soorten fruit uit zeven", "idem", "C(7, 4) = 35"],
                ["drie rode knikkers uit zes rode", "de blauwe doen niet mee", "C(6, 3) = 20"],
                ["twee steden uit twaalf bezoeken", "", "C(12, 2) = 66"],
                ["twee vertegenwoordigers uit zestien kandidaten", "zonder onderscheid in rol", "C(16, 2) = 120"],
                ["drie afgevaardigden uit vijfentwintig", "zonder onderscheid in rol", "C(25, 3) = 2300"],
                ["een hand van vijf kaarten uit tweeënvijftig", "je hand is geen rij", "C(52, 5)"],
            ])),
            ("p", "<strong>Een toernooi waarin elke ploeg één keer tegen elke andere speelt</strong>, is "
                  "een combinatie van twee uit n: elke wedstrijd is een paar ploegen. Met tien ploegen "
                  "zijn dat C(10, 2) = <strong>vijfenveertig</strong> wedstrijden."),
            ("kader", "<p><strong>Twee voorwaarden met de complementregel.</strong> Bij "
                      "<em>minstens één</em> of <em>minstens twee</em> tel je de gevallen die het net "
                      "niet halen, en trek je die van het totaal af.</p>"
                      "<p>Een commissie van drie uit vijf vrouwen en vier mannen, met "
                      "<strong>minstens één vrouw</strong>: in totaal C(9, 3) = 84 commissies, waarvan "
                      "C(4, 3) = 4 met enkel mannen. Dus 84 − 4 = <strong>tachtig</strong>.</p>"
                      "<p>Bij <em>minstens twee</em> tel je de gevallen met nul én met één, en haal je "
                      "allebei van het totaal af.</p>"),
            ("p", "<strong>Let op als herhaling toegelaten is.</strong> Mag je twee keer hetzelfde kiezen, "
                  "dan geldt de formule van de combinaties niet meer en val je terug op de productregel. "
                  "Twee kinderen uit dertig kiezen geeft C(30, 2) = 435 mogelijkheden, niet 870; dat "
                  "laatste is het aantal als de volgorde wél zou tellen."),
        ]),
    ],
    onthoud=[
        "n! is het product van alle getallen van één tot n, en 0! is één.",
        "Bij een combinatie telt de volgorde niet. C(n, p) = n! gedeeld door p! maal (n − p)!.",
        "De p! in de noemer deelt de volgordes van de gekozen elementen weer weg; vergeet je ze, dan tel je elke keuze p! keer.",
        "C(n, 0) = 1, C(n, 1) = n en C(n, p) = C(n, n − p).",
        "Elke ploeg één keer tegen elke andere is C(n, 2).",
        "Minstens één? Tel het tegengestelde en trek het van het totaal af.",
    ],
)

# ───────────────────────── 4. Kansvariabelen en de binomiale verdeling
BUNDELS["kansvariabelen-en-de-binomiale-verdeling-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kansvariabelen en de binomiale verdeling",
    onder="Een getal hangen aan een toevallige uitkomst, en de verdeling die bij n keer proberen hoort.",
    secties=[
        dict(kop="Wat is een kansvariabele?", blokken=[
            ("p", "Een <strong>kansvariabele</strong> is een grootheid die aan elke uitkomst van een "
                  "experiment een getal hangt. Gooi je twee keer met een munt, dan kan je aan elke "
                  "uitkomst het aantal keer kop hangen: dat aantal is de kansvariabele. Een ander woord "
                  "ervoor is <strong>stochast</strong>."),
            ("p", "De bijlage met notaties schrijft de kans dat X de waarde x aanneemt als "
                  "<strong>P(X = x)</strong>. Een kans ligt altijd tussen nul en één: ze kan nooit "
                  "groter zijn dan één of kleiner dan nul."),
            ("p", tabel(["Soort", "Wat het betekent", "Voorbeelden"], [
                ["discreet", "je kan de mogelijke waarden opsommen, het zijn losse getallen",
                 "het aantal kinderen in een gezin, het aantal telefoontjes per uur in een callcenter, de schoenmaat"],
                ["continu", "elke waarde in een interval is mogelijk, ook met cijfers na de komma",
                 "de temperatuur om twaalf uur, de lengte van een volwassene, de wachttijd aan een loket"],
            ])),
            ("p", "Het <strong>aantal kop bij twintig muntworpen</strong> is discreet, want je kan alleen "
                  "de gehele getallen van nul tot twintig krijgen. Een <strong>schoenmaat</strong> is "
                  "ook discreet, hoe vreemd dat ook klinkt: tussen maat 41 en maat 42 zit niets. Bij een "
                  "<strong>continue</strong> kansvariabele is de kans op één exacte waarde "
                  "<strong>gelijk aan nul</strong>; je vraagt er dus altijd naar een interval."),
        ]),
        dict(kop="De kansverdeling", blokken=[
            ("p", "Een <strong>kansverdeling</strong> van een discrete kansvariabele is een overzicht van "
                  "alle waarden met de kans op elk van die waarden. Je zet ze in een tabel of in een "
                  "staafdiagram."),
            ("kader", "<p>De som van alle kansen in een kansverdeling is <strong>precies één</strong>. "
                      "Dat is je controle. Staat er P(X = 1) = 0,2, P(X = 2) = 0,5 en P(X = 3) = 0,4, dan "
                      "is de som 1,1 en klopt de tabel niet.</p>"),
            ("p", "Wordt er naar <strong>P(X ≤ 2)</strong> gevraagd, dan tel je de kansen van alle "
                  "waarden tot en met twee op. De waarden van een discrete kansvariabele "
                  "<strong>hoeven niet bij nul te beginnen</strong>: het aantal ogen van een dobbelsteen "
                  "begint bij één."),
            ("p", "Gooi je twee keer met een munt en is X het aantal keer kop, dan zijn er vier even "
                  "waarschijnlijke uitkomsten: KK, KM, MK en MM. Dus P(X = 0) is een kwart, "
                  "<strong>P(X = 1) is de helft</strong> en P(X = 2) is een kwart. Samen één."),
        ]),
        dict(kop="Het Bernoulli-experiment", blokken=[
            ("p", "Een <strong>Bernoulli-experiment</strong> is een experiment met <strong>juist twee "
                  "mogelijke uitkomsten</strong>: lukt het of lukt het niet, kop of munt, afgekeurd of "
                  "goedgekeurd. De twee uitkomsten moeten <strong>niet</strong> even waarschijnlijk zijn; "
                  "een machine die vijf procent afkeurt is een prima Bernoulli-experiment."),
            ("p", "De kansvariabele die erbij hoort, kan <strong>alleen nul of één</strong> zijn. De "
                  "bijlage gebruikt de letter <strong>p</strong> voor de kans op succes, en de kans op "
                  "geen succes is dan <strong>1 − p</strong>."),
        ]),
        dict(kop="De binomiale verdeling", blokken=[
            ("p", "Herhaal je hetzelfde Bernoulli-experiment <strong>n keer</strong>, onafhankelijk en "
                  "telkens met dezelfde kans p, en tel je hoe vaak het lukt, dan is dat aantal "
                  "<strong>binomiaal verdeeld</strong>. Je schrijft <strong>X ~ B(n, p)</strong>: X is "
                  "binomiaal verdeeld met n experimenten en kans p op succes. De <strong>n</strong> staat "
                  "voor het aantal experimenten."),
            ("p", tabel(["Voorwaarde", "Wat ze betekent"], [
                ["twee uitkomsten", "elk experiment lukt of lukt niet"],
                ["vast aantal n", "je weet vooraf hoe vaak je het doet"],
                ["dezelfde p", "de kans op succes verandert niet tussendoor"],
                ["onafhankelijk", "wat er bij de ene keer gebeurt, verandert niets aan de volgende"],
            ])),
            ("p", "De uitkomsten <strong>hoeven niet continu verdeeld te zijn</strong>; integendeel, het "
                  "aantal successen is net discreet. En <strong>p mag elke waarde tussen nul en één "
                  "hebben</strong>: er is geen ondergrens van nul komma één of iets dergelijks."),
            ("kader", "<p><strong>P(X = k) = C(n, k) maal p tot de k maal (1 − p) tot de (n − k)</strong></p>"
                      "<p>Daar zit de C(n, k) van het vorige thema in: het aantal manieren waarop die k "
                      "successen verspreid kunnen zitten. De k loopt van nul tot n; "
                      "<strong>n plus één kan k niet zijn</strong>.</p>"),
            ("fig", svg.staafdiagram([(str(k), c) for k, c in
                                      enumerate([1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1])],
                                     breedte=430, hoogte=200, stap=50),
             "Het aantal manieren om k keer kop te gooien bij tien worpen, samen 1024. Bij X ~ B(10; 0,5) is de kansverdeling symmetrisch rond vijf."),
            ("p", tabel(["Situatie", "Verdeling", "Waarom"], [
                ["aantal zessen bij 20 worpen met een eerlijke dobbelsteen", "B(20; 1/6)", "elke worp is onafhankelijk en p blijft 1/6"],
                ["10 meerkeuzevragen met vier opties, allemaal gegokt", "B(10; 0,25)", "elke vraag lukt met kans een kwart"],
                ["20 stukken van een machine die 5 % afkeurt", "B(20; 0,05)", "elk stuk is goed of afgekeurd"],
                ["50 inwoners vragen in een stad waar 40 % voor A stemt", "B(50; 0,4)", "de antwoorden zijn onafhankelijk en p blijft nagenoeg gelijk"],
                ["3 kaarten trekken zonder terugleggen, aantal harten", "géén binomiale verdeling", "de kans op harten verandert na elke trekking"],
            ])),
            ("p", "Dat laatste is de valkuil. <strong>Zonder terugleggen verandert p</strong>, en dan mag "
                  "je niet binomiaal rekenen. Bij een grote populatie, zoals de vijftig inwoners van een "
                  "stad, verandert p wel zo weinig dat je het toch mag doen."),
        ]),
        dict(kop="Kansen uitrekenen", blokken=[
            ("p", "Drie keer met een munt gooien geeft acht even waarschijnlijke uitkomsten. Juist twee "
                  "keer kop kan op C(3, 2) = 3 manieren, dus de kans is <strong>drie achtste</strong>. "
                  "Bij X ~ B(5; 0,5) is P(X = 0) gelijk aan 0,5 tot de vijfde, "
                  "<strong>een tweeëndertigste</strong>. Gooi je zes keer met een dobbelsteen, dan is de "
                  "kans op geen enkele zes (5/6) tot de zesde, ongeveer <strong>drieëndertig "
                  "procent</strong>."),
            ("weetje", "<strong>P(X ≥ 1) reken je het snelst als één min P(X = 0).</strong> Dat is de "
                       "complementregel, nu met kansen in plaats van met aantallen."),
            ("p", "Op het examen doe je dit met de <strong>kansrekenmachine</strong>: kies de binomiale "
                  "verdeling, vul n en p in en duid aan welk stuk je wil. Ze kan de "
                  "<strong>hele kansverdeling in één keer opstellen</strong>, dus je hoeft de formule "
                  "niet elf keer in te tikken. Krijg je een kans van 1,4 te zien, dan heb je iets fout "
                  "ingetikt; een kans ligt tussen nul en één."),
        ]),
    ],
    onthoud=[
        "Een kansvariabele hangt een getal aan elke uitkomst. Discreet = losse waarden, continu = elke waarde in een interval.",
        "Bij een continue kansvariabele is de kans op één exacte waarde nul.",
        "De som van alle kansen in een kansverdeling is precies één.",
        "Een Bernoulli-experiment heeft juist twee uitkomsten; ze hoeven niet even waarschijnlijk te zijn.",
        "X ~ B(n, p): n keer hetzelfde experiment, onafhankelijk, met dezelfde p. P(X = k) = C(n, k) · p tot de k · (1 − p) tot de (n − k).",
        "Zonder terugleggen is het niet binomiaal, want p verandert.",
        "P(X ≥ 1) is één min P(X = 0).",
    ],
)

# ───────────────────────── 5. Verwachtingswaarde, variantie en standaardafwijking
BUNDELS["verwachtingswaarde-variantie-en-standaardafwijking-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Verwachtingswaarde, variantie en standaardafwijking",
    onder="Het gemiddelde dat je op lange termijn verwacht, en hoe ver de uitkomsten daar gemiddeld van afliggen.",
    secties=[
        dict(kop="De verwachtingswaarde", blokken=[
            ("p", "De <strong>verwachtingswaarde</strong> E(X) is het gemiddelde dat je op lange termijn "
                  "verwacht. De bijlage noteert ze met de Griekse letter <strong>mu</strong>."),
            ("p", "Bij een discrete kansvariabele uit een tabel bereken je ze zo: "
                  "<strong>vermenigvuldig elke waarde met haar kans en tel alles op</strong>. Het is dus "
                  "een <strong>gewogen gemiddelde</strong> en geen gewoon gemiddelde: elke waarde telt "
                  "mee met haar eigen kans in plaats van even zwaar."),
            ("kader", "<p>Waarden nul, één en twee met kansen 0,1 / 0,3 / 0,6:</p>"
                      "<p style=\"text-align:center;\">E(X) = 0 · 0,1 + 1 · 0,3 + 2 · 0,6 = <strong>1,5</strong></p>"
                      "<p>Merk op: 1,5 is geen waarde die X kan aannemen. Dat hoeft ook niet — "
                      "<strong>de verwachtingswaarde moet geen waarde zijn die echt voorkomt</strong>. "
                      "Een winkel die gemiddeld 2,4 fietsen per dag verkoopt, verkoopt er elke dag een "
                      "geheel aantal; alleen het gemiddelde is een kommagetal.</p>"),
            ("p", "Bij een <strong>binomiale</strong> verdeling hoef je niets op te tellen. Het "
                  "formularium geeft <strong>E(X) = n · p</strong>."),
            ("p", tabel(["Verdeling", "E(X)", "In woorden"], [
                ["B(20; 0,5)", "10", "twintig muntworpen geven gemiddeld tien keer kop"],
                ["B(50; 0,2)", "10", ""],
                ["B(100; 0,3)", "30", ""],
                ["B(400; 0,25)", "100", ""],
                ["B(60; 1/6)", "10", "zestig worpen met een dobbelsteen geven gemiddeld tien zessen"],
                ["B(15; 0,8)", "12", "een schutter die 80 % raakt, scoort bij vijftien penalty's gemiddeld twaalf keer"],
                ["B(20; 0,2)", "4", "twintig vragen met vijf opties, alles gegokt"],
                ["B(10; 0,4)", "4", "doe je de reeks van tien vaak opnieuw, dan haal je gemiddeld vier successen"],
            ])),
            ("p", "Omdat E(X) gewoon n maal p is, <strong>verdubbelt de verwachtingswaarde als je het "
                  "aantal experimenten verdubbelt</strong>. En E(X) <strong>kan negatief zijn</strong>: "
                  "bij een spel waarin je geld kan verliezen, horen er negatieve waarden bij de "
                  "kansvariabele."),
            ("weetje", "Een loterijlot kost twee euro en de verwachtingswaarde van je winst is 1,20 euro. "
                       "Dat betekent dat wie heel veel loten koopt, <strong>gemiddeld tachtig cent per "
                       "lot verliest</strong>. Zo is een loterij ook bedacht."),
        ]),
        dict(kop="Variantie en standaardafwijking", blokken=[
            ("p", "De <strong>standaardafwijking</strong> meet hoeveel de uitkomsten gemiddeld van de "
                  "verwachtingswaarde afwijken. De bijlage noteert ze met <strong>sigma</strong>. De "
                  "<strong>variantie</strong> Var(X) is haar kwadraat; je komt van de variantie naar de "
                  "standaardafwijking door <strong>de vierkantswortel</strong> te nemen."),
            ("p", "Daarom is de variantie uitgedrukt in de <strong>eenheid van X in het kwadraat</strong>, "
                  "en de standaardafwijking in dezelfde eenheid als X zelf. Dat is ook de reden waarom "
                  "men liever de standaardafwijking gebruikt om een verdeling te beschrijven: vierkante "
                  "centimeters lengte zeggen niemand iets."),
            ("kader", "<p>Voor een binomiale verdeling staat in het formularium:</p>"
                      "<p style=\"text-align:center;\"><strong>Var(X) = n · p · (1 − p)</strong></p>"
                      "<p>Je hoeft dus <strong>niet</strong> eerst de hele kansverdeling op te stellen om "
                      "de standaardafwijking te kennen. Twee getallen volstaan.</p>"),
            ("p", tabel(["Verdeling", "E(X) = n · p", "Var(X) = n · p · (1 − p)", "sigma"], [
                ["B(20; 0,5)", "10", "20 · 0,5 · 0,5 = 5", "ongeveer 2,24"],
                ["B(50; 0,2)", "10", "50 · 0,2 · 0,8 = 8", "ongeveer 2,83"],
                ["B(100; 0,3)", "30", "100 · 0,3 · 0,7 = 21", "ongeveer 4,58"],
                ["B(12; 0,5)", "6", "12 · 0,5 · 0,5 = 3", "ongeveer 1,73"],
                ["B(200; 0,05)", "10", "200 · 0,05 · 0,95 = 9,5", "ongeveer 3,08"],
                ["B(80; 0,25)", "20", "80 · 0,25 · 0,75 = 15", "ongeveer 3,87"],
                ["B(60; 1/6)", "10", "60 · (1/6) · (5/6) = 8,33", "ongeveer 2,89"],
                ["B(40; 0,5)", "20", "40 · 0,5 · 0,5 = 10", "ongeveer 3,16"],
            ])),
            ("p", "Die laatste rij is een bekende valstrik. Wie bij B(40; 0,5) een standaardafwijking van "
                  "<strong>tien</strong> opschrijft, is <strong>de wortel vergeten</strong>: tien is de "
                  "variantie, de standaardafwijking is ongeveer 3,16."),
        ]),
        dict(kop="Wat de getallen je vertellen", blokken=[
            ("p", "De variantie <strong>kan nooit negatief zijn</strong>: ze is opgebouwd uit kwadraten. "
                  "Een <strong>standaardafwijking van nul</strong> betekent dat de uitkomst altijd "
                  "dezelfde is, dus dat er eigenlijk niets toevalligs aan is."),
            ("p", "Twee binomiale verdelingen kunnen dezelfde E(X) hebben en toch heel verschillend zijn. "
                  "Is E(X) bij allebei tien, maar heeft de ene sigma gelijk aan één en de andere drie, "
                  "dan <strong>liggen de uitkomsten bij de tweede veel verder uit elkaar</strong>."),
            ("p", "Bij een vast aantal n is Var(X) het <strong>grootst bij p gelijk aan nul komma "
                  "vijf</strong>: dan is de uitkomst het minst voorspelbaar. Hoe dichter p bij nul of bij "
                  "één komt, hoe zekerder je op voorhand weet wat er gaat gebeuren."),
            ("weetje", "<strong>Verviervoudig je n, dan verdubbelt de standaardafwijking.</strong> De "
                       "variantie wordt immers vier keer zo groot, en de wortel van vier is twee. Meer "
                       "metingen maken de spreiding dus wel groter in absolute zin, maar veel kleiner in "
                       "verhouding tot n: dat is precies waarom grote steekproeven betrouwbaarder zijn."),
        ]),
    ],
    onthoud=[
        "E(X) is het gemiddelde op lange termijn, genoteerd als mu. Uit een tabel: elke waarde maal haar kans, alles opgeteld.",
        "Bij een binomiale verdeling: E(X) = n · p en Var(X) = n · p · (1 − p).",
        "De standaardafwijking is de wortel uit de variantie en staat in dezelfde eenheid als X.",
        "E(X) hoeft geen waarde te zijn die echt kan voorkomen; 2,4 fietsen per dag kan perfect.",
        "De variantie is nooit negatief en is het grootst bij p = 0,5.",
        "Verviervoudig je n, dan verdubbelt sigma.",
    ],
)

# ───────────────────────── 6. De normale verdeling en standaardiseren
BUNDELS["de-normale-verdeling-en-standaardiseren-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De normale verdeling en standaardiseren",
    onder="De klokcurve, de vuistregels erbij, en hoe je waarden uit verschillende verdelingen vergelijkbaar maakt.",
    secties=[
        dict(kop="De klokcurve", blokken=[
            ("p", "De grafiek van een <strong>normale verdeling</strong> is een "
                  "<strong>symmetrische klokvorm met één top</strong>. Ze heet ook de "
                  "<strong>gausscurve</strong> of de klokcurve. Je schrijft "
                  "<strong>X ~ N(mu, sigma)</strong>: X is normaal verdeeld met gemiddelde mu en "
                  "standaardafwijking sigma."),
            ("fig", svg.normaalkromme(100, 15, van=70, tot=130, xlabel="X"),
             "N(100; 15). Tussen mu min twee sigma en mu plus twee sigma ligt ongeveer vijfennegentig procent van de waarden."),
            ("p", tabel(["Eigenschap", "Wat ze betekent"], [
                ["continu", "elke waarde in een interval kan voorkomen, ook met cijfers na de komma"],
                ["oppervlakte onder de hele curve", "precies één, want alle kansen samen zijn één"],
                ["symmetrisch", "gemiddelde, mediaan en modus vallen samen"],
                ["P(X &lt; mu)", "0,5, want de helft ligt links van het gemiddelde"],
                ["mu groter", "de curve schuift naar rechts, de vorm blijft"],
                ["sigma groter", "de curve wordt breder en platter"],
                ["de staarten", "ze lopen door en raken de horizontale as nooit"],
            ])),
            ("p", "Omdat de verdeling continu is, is <strong>P(X = 180) gelijk aan nul</strong>: één "
                  "exacte waarde heeft geen oppervlakte onder de curve. Je vraagt dus altijd naar een "
                  "stuk: tussen twee waarden, of boven of onder een waarde."),
            ("weetje", "Twee normale verdelingen met hetzelfde gemiddelde maar een andere "
                       "standaardafwijking hebben <strong>niet</strong> dezelfde top. De oppervlakte "
                       "onder allebei is één, dus wie breder is, moet lager zijn."),
        ]),
        dict(kop="De vuistregels", blokken=[
            ("fig", svg.normaalkromme(100, 15, van=85, tot=115),
             "Tussen mu min sigma en mu plus sigma ligt ongeveer achtenzestig procent van de waarden."),
            ("p", tabel(["Interval", "Ongeveer", "Bij N(100; 15)"], [
                ["mu min sigma tot mu plus sigma", "68 %", "tussen 85 en 115"],
                ["mu min 2 sigma tot mu plus 2 sigma", "95 %", "tussen 70 en 130"],
                ["mu min 3 sigma tot mu plus 3 sigma", "99,7 %", "tussen 55 en 145"],
            ])),
            ("p", "Omdat de curve symmetrisch is, geldt ook: <strong>P(X &gt; mu plus sigma) is gelijk "
                  "aan P(X &lt; mu min sigma)</strong>. De twee staarten zijn even groot."),
        ]),
        dict(kop="Past de normale verdeling wel?", blokken=[
            ("p", "De normale verdeling is een <strong>model</strong>, geen natuurwet. Je moet dus "
                  "kunnen beoordelen of ze bij je data past, en de fiche zegt hoe: "
                  "<strong>maak met ICT een grafische voorstelling en bekijk de vorm</strong>."),
            ("p", tabel(["Data", "Past?", "Waarom"], [
                ["de lengte van duizend volwassen mannen", "ja", "gemeten grootheden liggen van nature rond een gemiddelde"],
                ["een histogram met een lange staart naar rechts", "nee", "een normale verdeling is symmetrisch"],
                ["examenscores met twee duidelijke toppen", "nee", "een normale verdeling heeft één top; hier zitten er waarschijnlijk twee groepen in"],
                ["het aantal zessen bij tien worpen", "nee", "dat aantal is discreet, dus binomiaal en niet normaal verdeeld"],
            ])),
            ("p", "Dat laatste verschil is belangrijk genoeg om twee keer te lezen. "
                  "<strong>Tellen geeft een discrete verdeling, meten geeft een continue.</strong> Het "
                  "aantal zessen tel je; de lengte van een man meet je."),
        ]),
        dict(kop="Standaardiseren", blokken=[
            ("p", "De <strong>standaardnormale verdeling</strong> is de normale verdeling met gemiddelde "
                  "<strong>nul</strong> en standaardafwijking <strong>één</strong>. De bijlage gebruikt "
                  "daarvoor de letter <strong>Z</strong>, dus Z ~ N(0; 1). Daaruit volgt meteen dat "
                  "P(Z &lt; 0) gelijk is aan <strong>0,5</strong>."),
            ("kader", "<p style=\"text-align:center;\"><strong>Z = (X − mu) gedeeld door sigma</strong></p>"
                      "<p>Eerst het verschil met het gemiddelde, dan pas delen door de "
                      "standaardafwijking. Wie sigma min X door mu deelt, heeft de drie getallen op de "
                      "verkeerde plaats gezet.</p>"),
            ("p", "Een <strong>z-waarde</strong> zegt hoeveel standaardafwijkingen een waarde van het "
                  "gemiddelde af ligt. Plus twee betekent twee standaardafwijkingen "
                  "<strong>boven</strong> het gemiddelde, een <strong>negatieve z-waarde</strong> "
                  "betekent eronder. Een z-waarde van nul betekent dat de waarde precies op het "
                  "gemiddelde ligt; dat is iets anders dan een kans van nul."),
            ("p", tabel(["Verdeling", "Waarde X", "Z = (X − mu) / sigma", "Betekenis"], [
                ["N(70; 5)", "80", "(80 − 70) / 5 = 2", "twee sigma boven het gemiddelde"],
                ["N(50; 4)", "42", "(42 − 50) / 4 = −2", "twee sigma onder het gemiddelde"],
                ["N(500; 20)", "540", "(540 − 500) / 20 = 2", "twee sigma boven het gemiddelde"],
            ])),
            ("p", "<strong>Waarom standaardiseren?</strong> Om waarden uit verschillende verdelingen met "
                  "elkaar te kunnen vergelijken, zeker als ze een andere eenheid hebben. Ann haalt "
                  "zeventig op een toets met mu zestig en sigma vijf: haar z-waarde is twee. Bo haalt "
                  "tachtig op een toets met mu zeventig en sigma tien: zijn z-waarde is één. "
                  "<strong>Ann deed relatief beter</strong>, ook al is haar punt lager."),
            ("fig", svg.normaalkromme(0, 1, tot=-1.96, xlabel="z"),
             "De grens waaronder twee komma vijf procent valt, ligt bij z ongeveer min 1,96."),
            ("p", "Die z van ongeveer <strong>min 1,96</strong> is er een om te onthouden: een fabrikant "
                  "die wil dat slechts twee komma vijf procent van de pakken onder het gewicht valt, "
                  "legt zijn grens daar. Een z-waarde van <strong>drie komma vijf</strong> daarentegen "
                  "wijst op een uitzonderlijke waarde, mogelijk een uitschieter: minder dan één op "
                  "duizend ligt zo ver van het gemiddelde."),
            ("weetje", "Standaardiseren verandert de <strong>vorm niet</strong>. Je verschuift en "
                       "verschaalt de as, meer niet: de klok blijft een klok. Ze wordt dus zeker geen "
                       "rechthoek."),
        ]),
        dict(kop="Met de kansrekenmachine", blokken=[
            ("p", "Op het examen reken je een kans bij een normale verdeling uit <strong>met een "
                  "rekenapp</strong>: je kiest de normale verdeling, vult mu en sigma in en geeft de "
                  "grenzen op. Je hoeft dus niet eerst te standaardiseren en in een tabel te zoeken."),
            ("p", "Standaardiseren blijft wel nodig om <strong>te vergelijken</strong> en om te snappen "
                  "wat de rekenapp doet. Bij N(178; 7) voor de lengte van Belgische mannen is de kans op "
                  "een lengte <strong>tussen 171 en 185</strong> het grootst van alle intervallen van "
                  "die breedte: dat is net mu min sigma tot mu plus sigma, dus ongeveer achtenzestig "
                  "procent."),
        ]),
    ],
    onthoud=[
        "X ~ N(mu, sigma): een symmetrische klok met één top, continu, met oppervlakte één eronder.",
        "Gemiddelde, mediaan en modus vallen samen. P(X < mu) = 0,5.",
        "Vuistregels: 68 % binnen één sigma, 95 % binnen twee sigma, 99,7 % binnen drie sigma.",
        "Grotere sigma = breder en platter; grotere mu = dezelfde curve, naar rechts geschoven.",
        "Z = (X − mu) / sigma. Een z-waarde zegt hoeveel standaardafwijkingen je van het gemiddelde af zit.",
        "Standaardiseren maakt verdelingen met een andere eenheid vergelijkbaar, maar verandert de vorm niet.",
        "Tellen geeft een discrete verdeling (binomiaal), meten een continue (normaal).",
    ],
)

# ───────────────────────── 7. Populatie, steekproef en de steekproevenverdeling
BUNDELS["populatie-steekproef-en-de-steekproevenverdeling-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Populatie, steekproef en de steekproevenverdeling",
    onder="Van een deel naar het geheel, en hoe hard je zo'n uitspraak mag maken.",
    secties=[
        dict(kop="Populatie en steekproef", blokken=[
            ("p", "De <strong>populatie</strong> is de volledige groep waarover je een uitspraak wil "
                  "doen. De <strong>steekproef</strong> is het deel van die populatie dat je werkelijk "
                  "onderzoekt. Je neemt een steekproef omdat de hele populatie onderzoeken "
                  "<strong>te duur of onmogelijk</strong> is."),
            ("p", "De <strong>variabele</strong> is het kenmerk dat je bij elk element van de steekproef "
                  "meet: de lengte, het antwoord ja of nee, de wachttijd. In een stad van honderdduizend "
                  "inwoners waar je er vierhonderd bevraagt, is de <strong>steekproefgrootte "
                  "vierhonderd</strong> en niet honderdduizend."),
            ("kader", "<p><strong>Houd de symbolen uit elkaar.</strong> Links staat de populatie, rechts "
                      "de steekproef. Ze zijn in de regel <strong>niet precies gelijk</strong>, en dat "
                      "is geen fout maar de kern van het vak.</p>"),
            ("p", tabel(["Wat", "Populatie", "Steekproef"], [
                ["gemiddelde", "mu", "x met een streepje"],
                ["standaardafwijking", "sigma", "s"],
                ["proportie", "p", "p met een dakje"],
                ["grootte", "N", "n"],
            ])),
            ("p", "Schrijven dat het steekproefgemiddelde mu is, is dus fout: <strong>mu staat voor het "
                  "populatiegemiddelde</strong>. En dat populatiegemiddelde is meestal net wat je "
                  "<strong>niet</strong> kent; als je het kende, hoefde je geen steekproef te nemen."),
            ("p", "De <strong>steekproefproportie</strong> p met een dakje is het aandeel in je "
                  "steekproef, dus altijd een getal tussen nul en één. Zeggen van de vierhonderd "
                  "bevraagden er honderd ja, dan is p met een dakje gelijk aan "
                  "<strong>nul komma vijfentwintig</strong>."),
        ]),
        dict(kop="Een goede steekproef", blokken=[
            ("p", "Een <strong>aselecte</strong> steekproef is er een waarbij <strong>elk lid van de "
                  "populatie dezelfde kans heeft om gekozen te worden</strong>. Een steekproef die een "
                  "goede afspiegeling van de populatie is, heet <strong>representatief</strong>."),
            ("p", "Vraag je alleen aan bezoekers van een sportclub hoeveel ze bewegen, dan is je "
                  "steekproef <strong>niet representatief</strong> voor de hele bevolking, hoe veel "
                  "mensen je er ook bevraagt. Daarom is een aselecte steekproef van driehonderd "
                  "<strong>betrouwbaarder</strong> dan duizend mensen die je zelf uitkiest. "
                  "<strong>Groot is niet hetzelfde als goed.</strong>"),
            ("p", "<strong>Variabiliteit</strong> is het woord van de bijlage voor het verschijnsel dat "
                  "verschillende steekproeven uit dezelfde populatie verschillende resultaten geven. Een "
                  "grotere steekproef geeft meestal een betere schatting, maar nooit een zekerheid."),
        ]),
        dict(kop="De steekproevenverdeling", blokken=[
            ("p", "Stel dat je niet één maar <strong>alle mogelijke</strong> steekproeven van grootte n "
                  "zou nemen en van elk het gemiddelde zou opschrijven. Die gemiddelden vormen samen de "
                  "<strong>steekproevenverdeling van het steekproefgemiddelde</strong>. Je trekt ze "
                  "nooit allemaal, maar je weet wel hoe ze eruitziet, en daar heb je alles aan: ze zegt "
                  "je <strong>hoe ver het gemiddelde van jouw ene steekproef waarschijnlijk van mu af "
                  "ligt</strong>."),
            ("kader", "<p>Het formularium geeft twee benaderingen, elk met haar voorwaarden.</p>"
                      "<p><strong>Het steekproefgemiddelde</strong> is bij benadering "
                      "N(mu; sigma gedeeld door de wortel uit n), op voorwaarde dat "
                      "<strong>n minstens dertig</strong> is.</p>"
                      "<p><strong>De steekproefproportie</strong> is bij benadering normaal verdeeld met "
                      "standaardafwijking <strong>de wortel uit p maal (1 − p) gedeeld door n</strong>, "
                      "op <strong>drie</strong> voorwaarden: n is minstens dertig, "
                      "<strong>n · p is minstens tien</strong> én <strong>n · (1 − p) is minstens "
                      "tien</strong>.</p>"),
            ("p", "Het gemiddelde van de steekproevenverdeling van het steekproefgemiddelde is "
                  "<strong>gelijk aan mu</strong>. Je zit dus gemiddeld juist; de vraag is alleen hoe "
                  "ver je er in één steekproef naast kan zitten."),
            ("p", tabel(["Gegeven", "sigma gedeeld door de wortel uit n", "Uitkomst"], [
                ["sigma = 10 en n = 100", "10 gedeeld door 10", "1"],
                ["sigma = 15 en n = 225", "15 gedeeld door 15", "1"],
                ["p = 0,5 en n = 100", "wortel uit (0,5 · 0,5 gedeeld door 100)", "0,05"],
            ])),
            ("weetje", "In de noemer staat de <strong>wortel</strong> uit n. Wordt n vier keer groter, "
                       "dan wordt de spreiding van het steekproefgemiddelde "
                       "<strong>gehalveerd</strong>, niet gevierendeeld. Wil je dubbel zo nauwkeurig "
                       "meten, dan heb je vier keer zoveel mensen nodig."),
        ]),
        dict(kop="Eerst de voorwaarden controleren", blokken=[
            ("p", "Controleer de voorwaarden <strong>vóór</strong> je de normale benadering gebruikt. "
                  "Zijn ze niet voldaan, dan geldt de benadering niet en is je besluit niets waard."),
            ("p", tabel(["Geval", "n ≥ 30?", "n · p ≥ 10?", "n · (1 − p) ≥ 10?", "Mag het?"], [
                ["gemiddelde, n = 45", "ja", "—", "—", "ja"],
                ["gemiddelde, n = 25", "nee", "—", "—", "nee"],
                ["proportie, n = 100 en p = 0,2", "ja", "20, ja", "80, ja", "ja"],
                ["proportie, n = 100 en p = 0,6", "ja", "60, ja", "40, ja", "ja"],
                ["proportie, n = 40 en p = 0,05", "ja", "2, nee", "38, ja", "nee"],
                ["proportie, n = 200 en p = 0,02", "ja", "4, nee", "196, ja", "nee"],
                ["proportie, n = 50 en p = 0,08", "ja", "4, nee", "46, ja", "nee"],
                ["proportie, n = 500 en p = 0,03", "ja", "15, ja", "485, ja", "ja"],
            ])),
            ("p", "De klassieke fout bij een <strong>proportie</strong> is stoppen na de eerste "
                  "voorwaarde. n is dan wel groot genoeg, maar bij een kleine p kan n · p nog altijd "
                  "onder de tien blijven, en dan loopt het mis aan die kant."),
            ("weetje", "<strong>De grootte van de populatie doet er niet toe.</strong> Een steekproef van "
                       "duizend is in een land van elf miljoen even nauwkeurig als in een stad van "
                       "vijftigduizend. In de formules staat alleen n, nergens N."),
        ]),
    ],
    onthoud=[
        "Populatie = de hele groep, steekproef = het deel dat je onderzoekt. mu, sigma en p horen bij de populatie; x met een streepje, s en p met een dakje bij de steekproef.",
        "Aselect betekent dat iedereen dezelfde kans heeft om gekozen te worden; representatief betekent een goede afspiegeling.",
        "Een kleine aselecte steekproef verslaat een grote die je zelf uitkiest.",
        "Steekproefgemiddelde: N(mu; sigma / wortel uit n), op voorwaarde dat n minstens dertig is.",
        "Steekproefproportie: standaardafwijking wortel uit p(1 − p)/n, op drie voorwaarden: n ≥ 30, n · p ≥ 10 en n · (1 − p) ≥ 10.",
        "Vier keer meer metingen halveert de spreiding. De grootte van de populatie telt niet mee.",
    ],
)

# ───────────────────────── 8. Hypothesen opstellen
BUNDELS["hypothesen-opstellen-h0-h1-en-de-richting-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Hypothesen opstellen: H0, H1 en de richting",
    onder="Twee beweringen over de populatie, waarvan er maar één op de beklaagdenbank zit.",
    secties=[
        dict(kop="H0 en H1", blokken=[
            ("p", "De <strong>nulhypothese H0</strong> is de aanname die geldt zolang de data niet het "
                  "tegendeel aantonen. De <strong>alternatieve hypothese H1</strong> is de bewering die "
                  "je met je onderzoek wil aantonen."),
            ("p", "Waarom die kant op? Omdat je bij een toets <strong>enkel H0 kan verwerpen</strong>. "
                  "Door je eigen bewering in H1 te zetten, lever je bewijs vóór haar door H0 "
                  "onderuit te halen. Zet je ze in H0, dan kan je ze hoogstens zelf kapotmaken."),
            ("kader", "<p>Allebei de hypothesen gaan over de <strong>populatie</strong>, nooit over je "
                      "steekproef. Dus over <strong>mu</strong> bij een gemiddelde en over "
                      "<strong>p</strong> bij een proportie. Schrijf je H0: x met een streepje is gelijk "
                      "aan twintig, dan heb je een hypothese over je eigen meting opgeschreven, en die "
                      "ken je al.</p>"),
            ("p", "In H0 staat <strong>altijd een gelijkheid</strong>, dus het teken "
                  "<strong>=</strong>. Een ongelijkheid hoort in H1. H0: mu is groter dan honderd kan "
                  "dus niet. H0 en H1 mogen elkaar ook <strong>niet overlappen</strong>, en samen moeten "
                  "ze <strong>alle mogelijkheden dekken</strong> met <strong>hetzelfde getal</strong>. "
                  "H0: mu = 50 met H1: mu &gt; 60 is fout: wat als mu vijfenvijftig is?"),
        ]),
        dict(kop="De richting van H1", blokken=[
            ("p", tabel(["Soort toets", "H1", "Je kijkt naar"], [
                ["linkszijdig", "mu is kleiner dan het getal uit H0", "de linkerstaart"],
                ["rechtszijdig", "mu is groter dan het getal uit H0", "de rechterstaart"],
                ["tweezijdig", "mu verschilt van het getal uit H0", "allebei de staarten"],
            ])),
            ("p", "Een <strong>eenzijdige</strong> toets kijkt dus maar naar één kant. Bij een "
                  "<strong>eenzijdige toets naar rechts</strong> kijk je naar de kans op een resultaat "
                  "dat <strong>minstens zo groot</strong> is als wat je gevonden hebt."),
            ("p", tabel(["Situatie", "H0", "H1", "Soort"], [
                ["de controleur vermoedt dat de pakken te licht zijn (claim: 500 g)", "mu = 500", "mu &lt; 500", "linkszijdig"],
                ["de krant vermoedt dat minder dan 60 % slaagt", "p = 0,60", "p &lt; 0,60", "linkszijdig"],
                ["de nieuwe lesmethode moet het gemiddelde boven 70 tillen", "mu = 70", "mu &gt; 70", "rechtszijdig"],
                ["bewoners klagen dat de wachttijd langer is dan 10 minuten", "mu = 10", "mu &gt; 10", "rechtszijdig"],
                ["de arts wil weten of het medicijn een ánder effect heeft", "mu = de huidige waarde", "mu verschilt ervan", "tweezijdig"],
                ["het bedrijf wil weten of de verpakking de verkoop verandert", "mu = de huidige verkoop", "mu verschilt ervan", "tweezijdig"],
                ["de krant toetst of de maatregel werkt", "de maatregel heeft geen effect", "hij heeft wel effect", "hangt af van de vraag"],
            ])),
            ("kader", "<p><strong>Drie dingen die niet mogen.</strong></p>"
                      "<p>Je kiest de richting van H1 <strong>vóór</strong> je de steekproefresultaten "
                      "ziet. Anders kies je achteraf de kant waar je toevallig uitkwam.</p>"
                      "<p>Je stapt <strong>niet</strong> van tweezijdig naar eenzijdig over omdat je "
                      "tweezijdige toets net niet significant uitkwam.</p>"
                      "<p>Je toetst <strong>niet twee verschillende alternatieve hypothesen "
                      "tegelijk</strong> met één toets.</p>"),
            ("p", "Bij een <strong>tweezijdige</strong> toets verdeel je het significantieniveau over de "
                  "twee staarten. Daardoor is een verschil er <strong>moeilijker</strong> mee aan te "
                  "tonen dan met een eenzijdige toets; dat is precies waarom de richting vooraf "
                  "vastligt. En de keuze tussen eenzijdig en tweezijdig volgt uit "
                  "<strong>je onderzoeksvraag</strong>, niet uit de grootte van je steekproef."),
        ]),
        dict(kop="De stappen van een toets", blokken=[
            ("fig", svg.stappen(["H0 en H1|opstellen", "voorwaarden|controleren",
                                 "p-waarde|berekenen", "besluiten en|formuleren"]),
             "De vier stappen. De tweede wordt het vaakst overgeslagen, en dan is de vierde waardeloos."),
            ("p", "<strong>Stap één:</strong> je formuleert H0 en H1 in woorden én in symbolen."),
            ("p", "<strong>Stap twee:</strong> je controleert of de voorwaarden om de "
                  "steekproevenverdeling te benaderen voldaan zijn. Bij een gemiddelde is dat n minstens "
                  "dertig, dus met n gelijk aan vijfenveertig zit je goed. Bij een "
                  "<strong>proportie</strong> controleer je ook n · p en n · (1 − p). Met n gelijk aan "
                  "honderd en p gelijk aan nul komma zestig is alles in orde; met n gelijk aan vijftig "
                  "en p gelijk aan nul komma nul acht is n · p gelijk aan vier en mag je niet verder."),
            ("p", "<strong>Stap drie:</strong> je rekent met de verdeling <strong>onder H0</strong>. De "
                  "steekproevenverdeling van het steekproefgemiddelde heeft dan het "
                  "<strong>gemiddelde uit H0</strong> en standaardafwijking sigma gedeeld door de wortel "
                  "uit n. Je rekent dus met het getal uit H0 en niet met dat van je steekproef, omdat je "
                  "wil weten <strong>hoe waarschijnlijk je data zijn in de wereld waar H0 geldt</strong>."),
        ]),
    ],
    onthoud=[
        "H0 is de aanname die blijft staan tot het tegendeel blijkt; H1 is wat je wil aantonen.",
        "Allebei gaan ze over de populatie: over mu of over p, nooit over je steekproefgemiddelde.",
        "In H0 staat altijd een gelijkheid. H0 en H1 overlappen niet en dekken samen alles, met hetzelfde getal.",
        "Linkszijdig = kleiner dan, rechtszijdig = groter dan, tweezijdig = verschilt van.",
        "De richting kies je vóór je de resultaten ziet, en ze volgt uit je onderzoeksvraag.",
        "Bij een tweezijdige toets verdeel je alfa over twee staarten, dus is een verschil moeilijker aan te tonen.",
        "Reken altijd met het getal uit H0.",
    ],
)

# ───────────────────────── 9. De p-waarde, het significantieniveau en de twee fouten
BUNDELS["de-p-waarde-het-significantieniveau-en-de-twee-fouten-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De p-waarde, het significantieniveau en de twee fouten",
    onder="Hoe je beslist, waar de grens ligt, en wat er mis kan gaan als je beslist.",
    secties=[
        dict(kop="De p-waarde", blokken=[
            ("p", "De <strong>p-waarde</strong> is de kans op een resultaat dat <strong>minstens zo "
                  "extreem</strong> is als het gevondene, <strong>als H0 waar is</strong>. Dat laatste "
                  "stukje is het belangrijkste van de hele zin."),
            ("p", "Vind je bij een rechtszijdige toets een steekproefgemiddelde van 52 terwijl H0 zegt "
                  "dat mu gelijk is aan 50, dan is de p-waarde de <strong>kans op een "
                  "steekproefgemiddelde van 52 of meer onder H0</strong>. Je rekent ze uit met de "
                  "rekenapps, maar je <strong>noteert wel je werkwijze en je redenering</strong>."),
            ("kader", "<p><strong>De fout die iedereen maakt.</strong> \"De p-waarde is 0,04, dus er is "
                      "vier procent kans dat H0 waar is.\" Dat staat er niet. De p-waarde is "
                      "<strong>de kans op de data als H0 waar is</strong>, niet de kans dat H0 waar "
                      "is.</p>"
                      "<p>Een p-waarde van 0,001 betekent dus: <strong>zulke data komen in één op de "
                      "duizend gevallen voor als H0 waar is</strong>.</p>"),
            ("p", "Een p-waarde is een kans, dus ze ligt tussen nul en één. Ze "
                  "<strong>kan nooit groter zijn dan één</strong>, hoe groot het gevonden verschil ook "
                  "is. Een <strong>kleinere p-waarde betekent sterker bewijs tegen H0</strong>."),
        ]),
        dict(kop="Het significantieniveau alfa", blokken=[
            ("p", "Het <strong>significantieniveau alfa</strong> is de grens waaronder je de "
                  "nulhypothese verwerpt. Het meest gebruikte niveau is <strong>0,05</strong>."),
            ("kader", "<p style=\"text-align:center;\"><strong>Verwerp H0 als de p-waarde kleiner is dan "
                      "of gelijk aan alfa.</strong></p>"
                      "<p>Is de p-waarde <strong>groter</strong> dan alfa, dan verwerp je H0 "
                      "<strong>niet</strong>. Bij een p-waarde van precies 0,05 met alfa gelijk aan "
                      "0,05 verwerp je H0 dus wél: de grens hoort erbij.</p>"),
            ("p", tabel(["p-waarde", "alfa", "Besluit"], [
                ["0,03", "0,05", "H0 verwerpen"],
                ["0,05", "0,05", "H0 verwerpen"],
                ["0,07", "0,05", "H0 niet verwerpen"],
                ["0,12", "0,05", "H0 niet verwerpen, er is te weinig bewijs tegen"],
            ])),
            ("p", "Alfa gelijk aan 0,01 is <strong>strenger</strong> dan 0,05: je hebt sterker bewijs "
                  "nodig voor je H0 verwerpt. Je kiest alfa <strong>vooraf</strong>. Kies je het pas "
                  "nadat je de p-waarde kent, dan kan je alfa zo kiezen dat je gewenste besluit "
                  "uitkomt, en dan is de hele toets theater."),
            ("weetje", "Bij een <strong>tweezijdige</strong> toets vergelijk je de p-waarde gewoon met "
                       "<strong>alfa</strong>, niet met alfa gedeeld door twee. Het opsplitsen gebeurt "
                       "al bij het berekenen van de p-waarde zelf: die telt allebei de staarten mee."),
        ]),
        dict(kop="De twee fouten", blokken=[
            ("fig", svg.kwadranten([
                ("H0 is waar — je verwerpt ze niet",
                 ["juiste beslissing", "de onschuldige gaat vrijuit"]),
                ("H0 is waar — je verwerpt ze",
                 ["type I-fout, kans gelijk aan alfa", "de onschuldige wordt veroordeeld"]),
                ("H0 is fout — je verwerpt ze niet",
                 ["type II-fout", "de rookmelder zwijgt terwijl er brand is"]),
                ("H0 is fout — je verwerpt ze",
                 ["juiste beslissing", "de schuldige wordt veroordeeld"]),
            ], onder="Links beslis je niet te verwerpen, rechts wel. Boven geldt H0 echt, onder niet."),
             "De vier mogelijke afloopjes van een toets. Per toets gebeurt er hoogstens één van de twee fouten, want H0 is waar of ze is het niet."),
            ("p", "Een <strong>type I-fout</strong> is H0 verwerpen terwijl ze waar is. De kans erop is "
                  "<strong>gelijk aan alfa</strong>. Bij alfa gelijk aan 0,05 verwerp je dus gemiddeld "
                  "<strong>één op de twintig keer</strong> een nulhypothese die waar is."),
            ("p", "Een <strong>type II-fout</strong> is H0 niet verwerpen terwijl ze fout is. Een "
                  "medische test die een gezonde patiënt ziek noemt, is een type I-fout als H0 zegt dat "
                  "de patiënt gezond is. Een rookmelder die niet afgaat terwijl er brand is, is een "
                  "type II-fout als H0 zegt dat er geen brand is."),
            ("p", "De twee fouten <strong>kunnen niet tegelijk gebeuren</strong> bij dezelfde toets: H0 "
                  "is waar of ze is het niet. Maar ze trekken wel aan elkaar. <strong>Kleiner alfa "
                  "kiezen verkleint de kans op een type I-fout en vergroot die op een type "
                  "II-fout.</strong> Een fabrikant die vooral wil vermijden dat hij een goede partij "
                  "afkeurt, <strong>maakt alfa kleiner</strong>."),
            ("weetje", "Er is één manier om de kans op <strong>allebei</strong> de fouten tegelijk te "
                       "verkleinen: <strong>een grotere steekproef nemen</strong>. Dat is de hele reden "
                       "waarom grote onderzoeken meer waard zijn."),
        ]),
        dict(kop="Je besluit correct opschrijven", blokken=[
            ("p", "<strong>H0 niet verwerpen is iets anders dan H0 aanvaarden.</strong> Het kan ook aan "
                  "een te kleine steekproef liggen in plaats van aan de waarheid van H0. Schrijf dus "
                  "niet \"er is geen verschil\" maar <strong>\"er is te weinig bewijs voor een "
                  "verschil\"</strong> — een verschil kan er wel degelijk zijn, je hebt het alleen niet "
                  "aangetoond."),
            ("p", "Een goed besluit noemt <strong>het niveau</strong> erbij: \"op het niveau van vijf "
                  "procent is er voldoende bewijs dat het gemiddelde hoger is\". Zonder dat niveau weet "
                  "je lezer niet hoe streng je was."),
            ("p", tabel(["Valkuil", "Wat er mis is"], [
                ["\"het effect is groot, want p is heel klein\"", "een significant resultaat zegt niet hoe groot het effect is"],
                ["een verschil van 0,1 % met p = 0,001 bij honderdduizend deelnemers", "significant, maar praktisch misschien onbelangrijk"],
                ["twintig verbanden toetsen op alfa = 0,05 en er één significant vinden", "bij twintig toetsen verwacht je er al één door toeval"],
                ["\"p = 0,07, dus er is geen verschil\"", "er is te weinig bewijs, dat is iets anders"],
            ])),
            ("p", "Dat eerste en dat tweede horen bij elkaar: bij een <strong>grote steekproef</strong> "
                  "wordt een klein verschil al snel significant. Twee onderzoeken die hetzelfde verschil "
                  "vinden, het ene met n gelijk aan dertig en het andere met n gelijk aan drieduizend, "
                  "geven bij het <strong>grote onderzoek de kleinste p-waarde</strong>. "
                  "<strong>Significant en belangrijk zijn twee verschillende dingen.</strong>"),
        ]),
    ],
    onthoud=[
        "De p-waarde is de kans op minstens zo'n extreem resultaat als H0 waar is. Niet de kans dat H0 waar is.",
        "Verwerp H0 als de p-waarde kleiner is dan of gelijk aan alfa. Alfa kies je vooraf, meestal 0,05.",
        "Type I-fout: H0 verwerpen terwijl ze waar is, met kans alfa. Type II-fout: H0 niet verwerpen terwijl ze fout is.",
        "Kleiner alfa verkleint de ene fout en vergroot de andere; een grotere steekproef verkleint allebei.",
        "H0 niet verwerpen is niet hetzelfde als H0 aanvaarden.",
        "Noem altijd het significantieniveau bij je besluit.",
        "Significant is niet hetzelfde als belangrijk, zeker niet bij een grote steekproef.",
    ],
)

# ───────────────────────── 10. Betrouwbaarheidsinterval en foutenmarge
BUNDELS["betrouwbaarheidsinterval-en-foutenmarge-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Betrouwbaarheidsinterval en foutenmarge",
    onder="Een schatting met haar onzekerheid erbij, en wat zo'n interval wel en niet zegt.",
    secties=[
        dict(kop="Wat het is", blokken=[
            ("p", "Een <strong>betrouwbaarheidsinterval</strong> is een interval dat met een bepaald "
                  "niveau de populatiewaarde bevat. Je geeft dus geen enkel getal maar een stuk van de "
                  "getallenlijn, want <strong>één getal doet alsof er geen onzekerheid is</strong>."),
            ("p", "De <strong>foutenmarge</strong> is de <strong>helft van de breedte</strong> van het "
                  "interval: de marge gaat immers naar twee kanten. Een marge van drie procent geeft "
                  "dus een interval van <strong>zes</strong> procent breed, en een marge van 2,5 procent "
                  "een interval van <strong>vijf</strong> procent breed. Het <strong>midden van het "
                  "interval is je steekproefresultaat</strong>."),
            ("fig", svg.getallenlijn(470, 42, 58, [
                (44, "44 %", "#2f5d50", False),
                (48, "48 %", "#c17f2b", True),
                (50, "50 %", "#6b7260", False),
                (52, "52 %", "#2f5d50", False),
            ]),
             "Achtenveertig procent met een foutenmarge van vier procent: het interval loopt van 44 tot 52 procent, en vijftig ligt erin."),
            ("p", "Die tekening is meteen een les in voorzichtig lezen. Een partij haalt 48 procent met "
                  "een marge van vier procent: je mag <strong>niet</strong> zeggen dat ze geen "
                  "meerderheid haalt, want vijftig zit in het interval. Omgekeerd: een partij met 53 "
                  "procent en een interval van 50 tot 56 procent heeft een meerderheid die "
                  "<strong>mogelijk maar niet aangetoond</strong> is, want vijftig is net de ondergrens."),
            ("p", "Uit een interval haal je omgekeerd ook de schatting en de marge. Loopt het van 44 tot "
                  "52 procent, dan is het midden <strong>48 procent</strong> en de marge "
                  "<strong>4 procent</strong>. Loopt het van 30 tot 40, dan is de marge "
                  "<strong>5</strong>."),
        ]),
        dict(kop="Wat de breedte bepaalt", blokken=[
            ("p", tabel(["Wat je verandert", "Wat er met het interval gebeurt"], [
                ["een grotere steekproef", "smaller"],
                ["een grotere standaardafwijking in de populatie", "breder"],
                ["een hoger betrouwbaarheidsniveau, bijvoorbeeld van 95 naar 99 %", "breder"],
                ["een lager betrouwbaarheidsniveau, bijvoorbeeld van 95 naar 90 %", "smaller"],
            ])),
            ("p", "Dat zijn de <strong>drie dingen</strong> die de breedte bepalen: de steekproefgrootte, "
                  "de standaardafwijking en het betrouwbaarheidsniveau. Het meest gebruikte niveau is "
                  "<strong>95 procent</strong>."),
            ("weetje", "Je marge <strong>halveren</strong> vraagt een <strong>vier keer zo grote</strong> "
                       "steekproef. In de formule staat de wortel uit n, en de wortel uit vier is twee. "
                       "Dat is waarom enquêtes bijna altijd rond de duizend mensen blijven hangen: "
                       "daarboven wordt het snel duur voor weinig winst."),
            ("p", "Twee onderzoeken die hetzelfde percentage schatten, het ene met een marge van twee "
                  "procent en het andere met zes procent: het eerste had waarschijnlijk een "
                  "<strong>grotere steekproef</strong>. Maar let op, <strong>smal is niet hetzelfde als "
                  "goed</strong>: de breedte zegt iets over de <strong>omvang</strong> van je steekproef, "
                  "niet over haar <strong>kwaliteit</strong>. Een scheve steekproef van tienduizend "
                  "mensen geeft een smal interval rond het verkeerde getal."),
            ("p", "Om dezelfde reden maakt een <strong>hoger betrouwbaarheidsniveau je schatting niet "
                  "nauwkeuriger</strong>. Je wordt zekerder dat de waarde erin zit door het net wijder "
                  "te maken, en wijder is net minder precies."),
        ]),
        dict(kop="Wat het níét zegt", blokken=[
            ("kader", "<p>Een betrouwbaarheidsniveau van vijfennegentig procent betekent: <strong>van "
                      "alle zulke intervallen bevat vijfennegentig procent de populatiewaarde</strong>. "
                      "Van de honderd zulke intervallen missen er dus gemiddeld <strong>vijf</strong> de "
                      "populatiewaarde. Jouw ene interval bevat ze dus "
                      "<strong>niet met zekerheid</strong>.</p>"),
            ("p", tabel(["Iemand zegt", "Wat er mis is"], [
                ["\"95 % van de Belgen ligt in dit interval\"", "het interval gaat over de populatiewaarde, niet over de individuen"],
                ["\"er is 95 % kans dat het echte gemiddelde ertussen ligt\"", "het populatiegemiddelde staat vast; het is de méthode die in 95 % van de gevallen lukt"],
                ["het interval voor het gemiddelde loopt van 18 tot 22 jaar, dus vrijwel iedereen is 18 tot 22", "het interval schat het gemiddelde, niet de leeftijd van de mensen zelf"],
                ["het interval loopt van 2 tot 9 procent, dus ongeveer 2 procent", "hij kiest één grens en negeert de hele onzekerheid"],
                ["\"mijn interval loopt van 40 tot 60, mijn onderzoek is mislukt\"", "breed betekent een kleine steekproef, niet een fout resultaat"],
                ["\"het interval bevat mijn steekproefwaarde, dus het klopt\"", "het ligt per constructie rond die waarde, dat bewijst niets"],
            ])),
            ("p", "Wat je er wél mee mag doen: <strong>alle waarden binnen het interval passen bij je "
                  "data</strong>. Loopt een interval van 46 tot 54 procent, dan passen alle percentages "
                  "daartussen erbij. Neem je een <strong>nieuwe steekproef</strong>, dan krijg je meestal "
                  "een <strong>ander</strong> interval."),
        ]),
        dict(kop="Een interval gebruiken om te beslissen", blokken=[
            ("p", "Een betrouwbaarheidsinterval kan je ook <strong>gebruiken om een hypothese te "
                  "beoordelen</strong>. Ligt het getal uit H0 buiten het interval, dan is dat een "
                  "aanwijzing tegen H0."),
            ("p", "Twee toepassingen die vaak terugkomen. <strong>Overlappen twee intervallen niet</strong>, "
                  "dan is er een aanwijzing dat de twee populatiewaarden verschillen. En ligt bij een "
                  "interval voor een <strong>verschil</strong> het getal <strong>nul erbuiten</strong>, "
                  "dan is er een aanwijzing voor een echt verschil."),
            ("weetje", "Een <strong>foutenmarge</strong> is iets anders dan een <strong>meetfout</strong>. "
                       "De foutenmarge komt van het steekproeven: je bevraagt niet iedereen. Een meetfout "
                       "komt van je instrument, en die verdwijnt niet door meer mensen te bevragen."),
            ("p", "Daarom vermeldt een goede krant altijd de <strong>steekproefgrootte</strong> bij een "
                  "enquête: de lezer kan dan inschatten hoe breed de foutenmarge is. Rapporteer je enkel "
                  "het midden van je interval, dan kan je lezer niet zien hoe onzeker je schatting is."),
        ]),
    ],
    onthoud=[
        "Een betrouwbaarheidsinterval is een schatting met haar onzekerheid erbij; het midden is je steekproefresultaat.",
        "De foutenmarge is de helft van de breedte, want ze gaat naar twee kanten.",
        "Breder wordt het bij een kleinere steekproef, een grotere spreiding of een hoger betrouwbaarheidsniveau.",
        "Je marge halveren vraagt vier keer zoveel metingen.",
        "95 % betekent: van alle zulke intervallen bevat 95 % de populatiewaarde. Niet: 95 % van de mensen zit erin.",
        "Een smal interval zegt dat je steekproef groot was, niet dat ze goed was.",
        "Ligt nul buiten een interval voor een verschil, dan is er een aanwijzing voor een echt verschil.",
    ],
)

# ───────────────────────── 11. Spreidingsdiagrammen, trendlijn en correlatie
BUNDELS["spreidingsdiagrammen-trendlijn-en-correlatie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Spreidingsdiagrammen, trendlijn en correlatie",
    onder="Twee grootheden tegen elkaar uitzetten, en voorzichtig zijn met wat je eruit besluit.",
    secties=[
        dict(kop="Het spreidingsdiagram", blokken=[
            ("p", "In een <strong>spreidingsdiagram</strong> zet je voor elk element <strong>één "
                  "punt</strong> met twee gemeten waarden. Je hebt er dus <strong>twee numerieke "
                  "variabelen</strong> voor nodig; voor één variabele in groepen gebruik je iets anders. "
                  "Een ander woord ervoor is <strong>puntenwolk</strong>."),
            ("p", "Op de <strong>horizontale as</strong> staat de <strong>onafhankelijke</strong> "
                  "variabele, op de <strong>verticale as</strong> de <strong>afhankelijke</strong>. "
                  "Onderzoek je of meer studietijd een hoger punt geeft, dan is de studietijd "
                  "onafhankelijk en het punt op de toets afhankelijk. Zet een leerling de "
                  "schoolresultaten horizontaal en de studietijd verticaal, dan horen de assen "
                  "omgewisseld."),
            ("fig", svg.puntenwolk([(2, 9), (3, 9), (4, 12), (5, 11), (6, 14),
                                    (7, 13), (8, 16), (9, 15), (10, 18)],
                                   breedte=430, hoogte=250, xlabel="studie-uren",
                                   ylabel="punt op 20", xstap=2, ystap=2),
             "Negen leerlingen. De trendlijn is y = 1,07x + 6,6 en r is 0,95: een sterke positieve samenhang."),
            ("p", "Volgens de fiche maak je zo'n diagram <strong>met ICT</strong>, dus met de rekenapps "
                  "van de examencommissie. Je tikt de twee kolommen in het rekenblad en vraagt het "
                  "diagram op."),
        ]),
        dict(kop="Welke vorm zie je?", blokken=[
            ("p", tabel(["Vorm van de wolk", "Soort verband"], [
                ["rond een rechte van links onder naar rechts boven", "positief lineair verband"],
                ["rond een rechte van links boven naar rechts onder", "negatief lineair verband"],
                ["de ene verdubbelt als de andere verdubbelt", "recht evenredig"],
                ["de ene halveert als de andere verdubbelt", "omgekeerd evenredig"],
                ["een parabool", "kwadratisch verband"],
                ["een omgekeerde U", "kwadratisch verband met een maximum in het midden"],
                ["geen zichtbaar patroon", "geen lineair verband — maar misschien wel een ander"],
            ])),
            ("p", "Een <strong>lineair</strong> verband hoeft <strong>niet door de oorsprong</strong> te "
                  "gaan; recht evenredig wel. En een spreidingsdiagram kan dus ook een verband tonen dat "
                  "<strong>niet rechtlijnig</strong> is: meet je bij vijftig auto's de snelheid en de "
                  "remafstand, dan groeit de remafstand sneller dan de snelheid en zie je een "
                  "<strong>kwadratisch</strong> verband."),
            ("p", "Ligt er één punt <strong>heel ver</strong> van de rest, dan gooi je het niet zomaar "
                  "weg: je onderzoekt of het een <strong>meetfout of een echt bijzonder geval</strong> is."),
        ]),
        dict(kop="De trendlijn", blokken=[
            ("p", "De <strong>trendlijn</strong> is de lijn die het verloop van de puntenwolk het best "
                  "weergeeft. Haar voorschrift bepaal je <strong>met ICT</strong>: de rekenapp geeft je "
                  "de vergelijking."),
            ("p", "Lees ze zoals elke rechte. Is de trendlijn <strong>y = 2x + 5</strong>, dan betekent "
                  "de twee: <strong>per eenheid die x stijgt, stijgt y met twee eenheden</strong>."),
            ("kader", "<p><strong>Niet buiten je gegevens voorspellen.</strong> Een trendlijn is "
                      "getrokken door de punten die je gemeten hebt. Buiten dat bereik weet je niet of "
                      "ze nog klopt, en dan hoort ze er ook niet te staan. Daarom loopt de trendlijn in "
                      "de tekening hierboven enkel van twee tot tien uur.</p>"),
        ]),
        dict(kop="De correlatiecoëfficiënt r", blokken=[
            ("p", "De <strong>correlatiecoëfficiënt r</strong> drukt in één getal uit hoe sterk het "
                  "<strong>lineaire</strong> verband is. Ze ligt <strong>altijd tussen min één en plus "
                  "één</strong>. Het teken zegt de richting, de grootte de sterkte."),
            ("p", tabel(["r", "Samenhang volgens het formularium"], [
                ["0", "geen samenhang"],
                ["tussen 0 en 0,3", "zwakke positieve samenhang"],
                ["tussen 0,3 en 0,7", "matige positieve samenhang"],
                ["boven 0,7", "sterke positieve samenhang"],
                ["tussen 0 en −0,3", "zwakke negatieve samenhang"],
                ["tussen −0,3 en −0,7", "matige negatieve samenhang"],
                ["onder −0,7", "sterke negatieve samenhang"],
            ])),
            ("p", "Dus r gelijk aan <strong>0,85</strong> is een sterke positieve samenhang, "
                  "<strong>0,35</strong> een matige, <strong>0,2</strong> een zwakke, en "
                  "<strong>min 0,5</strong> een matige negatieve. <strong>Min 0,9</strong> betekent een "
                  "sterk verband waarbij de ene daalt als de andere stijgt. Die vuistregels staan in "
                  "het <strong>formularium dat je bij het examen krijgt</strong>, dus je hoeft ze niet "
                  "uit het hoofd te kennen — ze lezen wel."),
            ("fig", svg.puntenwolk([(2, 12), (3, 9), (4, 14), (5, 11), (6, 16),
                                    (7, 10), (8, 15), (9, 13), (10, 17)],
                                   breedte=430, hoogte=250, xlabel="studie-uren",
                                   ylabel="punt op 20", xstap=2, ystap=2),
             "Dezelfde soort gegevens, maar nu met r gelijk aan 0,55: een matige positieve samenhang. De punten liggen veel losser rond de lijn."),
            ("kader", "<p><strong>Teken eerst, reken dan.</strong> Maak altijd eerst een "
                      "spreidingsdiagram vóór je r berekent: r zegt <strong>enkel iets over een lineair "
                      "verband</strong>, en je wil de vorm zien.</p>"
                      "<p>Daarom betekent <strong>r gelijk aan nul niet</strong> dat er zeker geen enkel "
                      "verband is: een mooie omgekeerde U kan r nul geven terwijl het verband "
                      "glashelder is. En een puntenwolk zonder zichtbaar patroon sluit een ander soort "
                      "verband niet uit.</p>"
                      "<p>Twee onderzoekers kunnen allebei r gelijk aan 0,8 vinden met heel verschillend "
                      "uitziende puntenwolken. Hetzelfde getal hoort bij verschillende vormen; "
                      "<strong>daarom kijk je altijd naar het diagram</strong>.</p>"),
        ]),
        dict(kop="Correlatie is geen causaliteit", blokken=[
            ("p", "<strong>Correlatie is samenhang, causaliteit is oorzaak en gevolg.</strong> Een sterke "
                  "correlatie <strong>bewijst niet</strong> dat de ene grootheid de andere veroorzaakt. "
                  "Dat is de belangrijkste zin van dit thema."),
            ("p", tabel(["Waarneming", "De echte verklaring"], [
                ["in de zomer worden meer ijsjes verkocht én verdrinken meer mensen", "de warmte verklaart allebei"],
                ["kinderen met grotere voeten lezen beter", "de leeftijd verklaart allebei"],
                ["wie meer melk drinkt, haalt hogere punten", "misschien ontbijten die leerlingen simpelweg beter"],
            ])),
            ("p", "In alle drie de gevallen zit er een <strong>derde grootheid</strong> achter die de "
                  "twee andere stuurt. \"Drink melk voor betere punten\" is dus een krantenkop en geen "
                  "besluit."),
        ]),
    ],
    onthoud=[
        "Een spreidingsdiagram zet twee numerieke variabelen tegen elkaar: onafhankelijk horizontaal, afhankelijk verticaal.",
        "De trendlijn geeft het verloop weer; haar richtingsgetal zegt hoeveel y stijgt per eenheid x. Voorspel er niet mee buiten je meetbereik.",
        "r ligt tussen −1 en 1. Tot 0,3 zwak, tot 0,7 matig, daarboven sterk. De vuistregels staan in het formularium.",
        "r meet enkel een líneair verband, dus teken eerst het diagram en reken dan.",
        "r gelijk aan nul betekent geen lineair verband, niet geen enkel verband.",
        "Correlatie bewijst geen oorzaak: zoek altijd naar een derde grootheid.",
    ],
)

# ───────────────────────── 12. Kansen berekenen met de kansrekenmachine
BUNDELS["kansen-berekenen-met-de-kansrekenmachine-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kansen berekenen met de kansrekenmachine",
    onder="Het scherm dat je het vaakst nodig hebt, en de kansen die er bij dit vak uit moeten komen.",
    secties=[
        dict(kop="Waar je het vindt", blokken=[
            ("p", "In het tabblad <strong>Rekenmachine</strong> bij elk hoofdstuk staan drie knoppen. De "
                  "middelste, <strong>Kansrekenmachine</strong>, is degene waar dit thema over gaat. Je "
                  "kiest er bovenaan een verdeling, vult de getallen in en duidt aan welk stuk je wil."),
            ("p", tabel(["Je wil", "Wat je kiest", "Wat je invult"], [
                ["een binomiale kans", "de binomiale verdeling", "n en p, daarna de grenzen voor k"],
                ["een kans bij een normale verdeling", "de normale verdeling", "mu en sigma, daarna de grenzen"],
                ["een kans bij Z", "de normale verdeling", "mu is nul en sigma is één"],
                ["een grenswaarde bij een gegeven kans", "dezelfde verdeling, omgekeerd", "de kans; de app geeft de grens"],
            ])),
            ("kader", "<p><strong>Drie knopjes voor het stuk dat je wil.</strong> De kansrekenmachine "
                      "laat je kiezen tussen de <strong>linkerstaart</strong> (tot een grens), de "
                      "<strong>rechterstaart</strong> (vanaf een grens) en het stuk "
                      "<strong>tussen twee grenzen</strong>. Negen van de tien fouten op dit examen zijn "
                      "de verkeerde knop.</p>"),
            ("p", "Bij een <strong>normale</strong> verdeling geeft de app <strong>nooit de kans op "
                  "precies één waarde</strong>: die is nul. Je vraagt dus altijd een stuk. Bij een "
                  "<strong>binomiale</strong> verdeling kan P(X = k) wel, want die is discreet."),
        ]),
        dict(kop="Binomiale kansen", blokken=[
            ("p", "Afronden doe je <strong>pas op het einde</strong>, en op het aantal decimalen dat de "
                  "vraag noemt."),
            ("p", tabel(["Opgave", "Wat je invult", "Antwoord"], [
                ["X ~ B(20; 0,3), P(X = 6)", "n = 20, p = 0,3, van 6 tot 6", "0,192"],
                ["tien keer munt, precies vijf keer kop", "n = 10, p = 0,5, van 5 tot 5", "0,246"],
                ["X ~ B(20; 0,3), P(X ≤ 4)", "linkerstaart tot en met 4", "0,24"],
                ["twaalf worpen, precies twee zessen", "n = 12, p = 1/6, van 2 tot 2", "0,296"],
                ["X ~ B(50; 0,2), P(X ≥ 15)", "rechterstaart vanaf 15", "0,061"],
                ["acht schoten, 75 % raak, precies zes keer raak", "n = 8, p = 0,75, van 6 tot 6", "0,31"],
                ["X ~ B(100; 0,4), P(X ≤ 35)", "linkerstaart tot en met 35", "0,179"],
                ["vijftien tests die elk in 90 % slagen, allemaal goed", "n = 15, p = 0,9, van 15 tot 15", "0,21"],
                ["25 stukken, 4 % afgekeurd, geen enkel afgekeurd", "n = 25, p = 0,04, van 0 tot 0", "0,36"],
                ["X ~ B(30; 0,5), P(X ≥ 20)", "rechterstaart vanaf 20", "0,049"],
                ["zes worpen, minstens één zes", "n = 6, p = 1/6, vanaf 1", "0,67"],
                ["X ~ B(40; 0,25), P(X = 10)", "van 10 tot 10", "0,144"],
                ["200 mensen, ziekte bij 5 %, P(X ≤ 5)", "linkerstaart tot en met 5", "0,062"],
                ["X ~ B(16; 0,5), P(X ≥ 12)", "rechterstaart vanaf 12", "0,038"],
                ["vijf keer munt, geen enkele keer kop", "n = 5, p = 0,5, van 0 tot 0", "0,031"],
            ])),
            ("weetje", "Heeft je app alleen een <strong>cumulatieve</strong> kans (tot en met k), dan "
                       "vind je P(X ≥ 15) als <strong>één min de cumulatieve kans tot en met 14</strong>. "
                       "Let op de 14: tot en met 15 zou de vijftien er dubbel in zetten."),
        ]),
        dict(kop="Kansen bij een normale verdeling", blokken=[
            ("p", tabel(["Opgave", "Wat je invult", "Antwoord"], [
                ["X ~ N(180; 8), P(X > 192)", "mu = 180, sigma = 8, rechterstaart vanaf 192", "0,067"],
                ["N(178; 7), P(171 &lt; X &lt; 185)", "tussen 171 en 185", "0,683"],
                ["N(100; 15), P(X > 130)", "rechterstaart vanaf 130", "0,023"],
                ["N(500; 20), P(X &lt; 480)", "linkerstaart tot 480", "0,159"],
                ["Z ~ N(0; 1), P(Z &lt; 1,96)", "mu = 0, sigma = 1, linkerstaart tot 1,96", "0,975"],
                ["N(72; 8), P(X > 80)", "rechterstaart vanaf 80", "0,159"],
                ["N(20; 4), P(X &lt; 15)", "linkerstaart tot 15", "0,106"],
                ["N(37; 0,5), P(X > 38)", "rechterstaart vanaf 38", "0,0228"],
                ["N(1000; 50), P(950 &lt; X &lt; 1050)", "tussen 950 en 1050", "0,683"],
                ["N(100; 15), welke waarde heeft 2,5 % boven zich?", "de omgekeerde vraag, kans 0,975 links", "129,4"],
            ])),
            ("fig", svg.normaalkromme(72, 8, van=80, xlabel="punt"),
             "N(72; 8) met de rechterstaart vanaf 80: dat is de 0,159 uit de tabel hierboven."),
            ("p", "Die laatste rij van de tabel is de <strong>omgekeerde</strong> vraag: je geeft een "
                  "kans en je vraagt de grens. Bij N(100; 15) heeft de waarde <strong>129,4</strong> "
                  "nog 2,5 procent boven zich."),
        ]),
        dict(kop="Van z naar een p-waarde", blokken=[
            ("p", "Bij een hypothesetoets reken je eerst je z uit en vraag je dan de staart op. Werk met "
                  "<strong>Z ~ N(0; 1)</strong>."),
            ("p", tabel(["Toets", "Wat je opvraagt", "p-waarde"], [
                ["rechtszijdig, z = 2", "rechterstaart vanaf 2", "0,0228"],
                ["linkszijdig, z = −2,5", "linkerstaart tot −2,5", "0,0062"],
                ["tweezijdig, z = 2", "de rechterstaart maal twee", "0,0455"],
            ])),
            ("p", "Bij een <strong>symmetrische</strong> verdeling is de p-waarde van een tweezijdige "
                  "toets dus <strong>het dubbele</strong> van die van de eenzijdige."),
            ("kader", "<p><strong>Een volledig voorbeeld.</strong> H0 zegt mu = 50. Je vindt x met een "
                      "streepje gelijk aan 52, bij n = 100 en sigma = 10, en je toetst rechtszijdig.</p>"
                      "<p>De standaardafwijking van het steekproefgemiddelde is 10 gedeeld door de "
                      "wortel uit 100, dus 1. Dan is z gelijk aan (52 − 50) gedeeld door 1, dus "
                      "<strong>2</strong>. De rechterstaart vanaf 2 geeft "
                      "<strong>p = 0,0228</strong>.</p>"
                      "<p>En met een proportie: H0 zegt p = 0,5, je vindt 112 van de 200, dus p met een "
                      "dakje gelijk aan 0,56. De standaardafwijking is de wortel uit 0,5 · 0,5 gedeeld "
                      "door 200, dus ongeveer 0,0354. Dan is z ongeveer 1,70 en is "
                      "<strong>p = 0,045</strong>. Bij alfa gelijk aan 0,05 verwerp je H0, want 0,045 is "
                      "kleiner dan 0,05.</p>"),
        ]),
        dict(kop="Controleer jezelf", blokken=[
            ("p", tabel(["Je ziet", "Wat er waarschijnlijk gebeurde"], [
                ["een kans groter dan één, bijvoorbeeld 1,19", "je las een ander getal van het scherm af; een kans ligt tussen nul en één"],
                ["een p-waarde van 0,9772 bij een rechtszijdige toets", "je nam de linkerstaart; de p-waarde is 0,0228"],
                ["een kans van nul bij een normale verdeling", "je vroeg één exacte waarde in plaats van een stuk"],
                ["een heel ander getal dan je schatting", "kijk na of je n en p niet verwisseld hebt"],
            ])),
            ("p", "Schat altijd eerst grof wat eruit moet komen. Bij X ~ B(20; 0,3) verwacht je zes "
                  "successen, dus P(X = 6) is de grootste van allemaal en P(X ≤ 4) duidelijk kleiner "
                  "dan de helft. Komt er iets heel anders uit, dan heb je je getallen verkeerd ingetikt "
                  "en niet de wiskunde verkeerd begrepen."),
        ]),
    ],
    onthoud=[
        "Kies eerst de verdeling, vul dan de getallen in en kies dan het stuk: linkerstaart, rechterstaart of tussen twee grenzen.",
        "Bij een normale verdeling vraag je nooit één exacte waarde; die kans is nul.",
        "P(X ≥ 15) is één min de cumulatieve kans tot en met 14.",
        "Een tweezijdige p-waarde is bij een symmetrische verdeling het dubbele van de eenzijdige.",
        "Afronden doe je pas op het einde, op het aantal decimalen dat de vraag vraagt.",
        "Schat vooraf grof wat eruit moet komen; dat vangt een tikfout op.",
    ],
)

# ───────────────────────── 13. Frequentietabellen en gegevens groeperen
BUNDELS["frequentietabellen-en-gegevens-groeperen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Frequentietabellen en gegevens groeperen",
    onder="Ruwe gegevens ordenen, en ze in klassen steken als het er te veel zijn.",
    secties=[
        dict(kop="Drie soorten frequentie", blokken=[
            ("p", tabel(["Frequentie", "Wat ze is"], [
                ["absolute", "het aantal keer dat die waarde voorkomt"],
                ["relatieve", "de absolute frequentie gedeeld door het totale aantal"],
                ["cumulatieve", "het aantal gegevens tot en met die waarde"],
            ])),
            ("fig", svg.frequentietabel([(5, 2), (6, 4), (7, 7), (8, 6), (9, 4), (10, 2)],
                                        koppen=("punt", "hoe vaak")),
             "De punten van vijfentwintig leerlingen. Zeven komt het vaakst voor."),
            ("p", tabel(["Punt", "Absoluut", "Relatief", "Cumulatief"], [
                ["5", "2", "8 %", "2"],
                ["6", "4", "16 %", "6"],
                ["7", "7", "28 %", "13"],
                ["8", "6", "24 %", "19"],
                ["9", "4", "16 %", "23"],
                ["10", "2", "8 %", "25"],
                ["samen", "25", "100 %", ""],
            ])),
            ("p", "Een <strong>absolute frequentie is altijd een geheel getal</strong>: je telt stuks. "
                  "De <strong>som van alle relatieve frequenties is één</strong>, dus honderd procent. "
                  "Vind je 1,04, dan zit er een rekenfout in. En de "
                  "<strong>laatste cumulatieve frequentie is het totale aantal</strong>, niet de "
                  "grootste absolute frequentie."),
            ("p", "Uit cumulatieve frequenties haal je de absolute terug door af te trekken. Staat er "
                  "bij de derde rij 45 en bij de vierde 62, dan is de absolute frequentie van de vierde "
                  "rij <strong>zeventien</strong>. Die kolom dient vooral om snel te zien "
                  "<strong>hoeveel gegevens onder een grens liggen</strong>."),
        ]),
        dict(kop="Waarom relatief?", blokken=[
            ("p", "Met <strong>relatieve</strong> frequenties worden datasets van "
                  "<strong>verschillende grootte vergelijkbaar</strong>. Zet een krant twee heel "
                  "verschillend grote groepen naast elkaar met enkel absolute aantallen, dan kan de "
                  "lezer ze niet eerlijk vergelijken."),
            ("p", tabel(["Gegeven", "Berekening", "Relatieve frequentie"], [
                ["8 keer in een dataset van 40", "8 gedeeld door 40", "20 %"],
                ["12 keer in een dataset van 50", "12 gedeeld door 50", "24 %"],
                ["5 van de 25 leerlingen haalden een tien", "5 gedeeld door 25", "20 %"],
            ])),
            ("p", "De frequenties 12, 18, 25 en 5 samen geven een totaal van <strong>zestig</strong>. En "
                  "een frequentietabel kan ook voor een <strong>niet-numerieke</strong> variabele: "
                  "haarkleur, studierichting, favoriete sport. Elke waarde van de dataset moet in "
                  "<strong>precies één rij</strong> terechtkomen."),
            ("weetje", "Bij een grote dataset stel je de tabel op <strong>met ICT</strong>, dus met de "
                       "rekenapps. In het rekenblad tik je de kolom in en vraag je de frequenties op; "
                       "met de hand tellen is bij duizend rijen geen optie."),
        ]),
        dict(kop="Groeperen in klassen", blokken=[
            ("p", "Zijn er <strong>heel veel verschillende waarden</strong>, dan groepeer je ze. Een "
                  "<strong>klasse</strong> is een interval waarin je verschillende waarden samen telt. "
                  "Het voordeel bij tienduizend waarden: je ziet de <strong>vorm van de verdeling in "
                  "één oogopslag</strong>."),
            ("fig", svg.histogram([(0, 10, 12), (10, 20, 18), (20, 30, 10)],
                                  xlabel="minuten", ylabel="aantal"),
             "Veertig wachttijden in drie klassen. Onder de twintig minuten liggen er 12 + 18 = 30."),
            ("p", tabel(["Begrip", "Betekenis", "Voorbeeld"], [
                ["klassenbreedte", "het verschil tussen de twee grenzen", "de klasse van 20 tot 30 is tien breed"],
                ["klassenmidden", "het gemiddelde van de twee grenzen", "bij 20 tot 30 is dat 25, bij 40 tot 50 is dat 45"],
                ["aantal klassen", "hoeveel intervallen je maakt", "de klassen 0–20, 20–40, 40–60 en 60–80 zijn er vier"],
            ])),
            ("p", "Je gebruikt het <strong>klassenmidden</strong> om uit een gegroepeerde tabel een "
                  "gemiddelde te berekenen, omdat je de <strong>afzonderlijke waarden niet meer "
                  "kent</strong> en het midden de beste gok is. Reken je zo 34,2 uit terwijl de ruwe "
                  "data 33,8 geven, dan is dat <strong>normaal</strong>: het klassenmidden is een "
                  "benadering."),
            ("kader", "<p><strong>Uit een gegroepeerde tabel kan je de oorspronkelijke waarden niet meer "
                      "terughalen.</strong> Dat is de prijs van het overzicht. Bewaar dus altijd je "
                      "ruwe gegevens.</p>"),
        ]),
        dict(kop="Klassen die niet deugen", blokken=[
            ("p", tabel(["Fout", "Wat er misloopt"], [
                ["klassen die overlappen: 10 tot 20 en 20 tot 30", "de waarde twintig past in twee klassen en wordt dubbel geteld"],
                ["klassen met een gat: 0 tot 10, 11 tot 20, 21 tot 30 bij een continue variabele", "de waarden tussen 10 en 11 vallen in geen enkele klasse"],
                ["ongelijke klassenbreedtes met de frequentie als hoogte", "het histogram wordt misleidend; een bredere klasse hoort een bredere staaf te krijgen"],
                ["groeperen wat niet gegroepeerd hoeft, zoals het aantal broers en zussen", "daar zijn maar een handvol waarden; een gewone tabel is duidelijker"],
            ])),
            ("p", "Een <strong>lege klasse mag</strong> wel degelijk. Komt er in een interval toevallig "
                  "niets voor, dan laat je die klasse gewoon met frequentie nul staan: dat gat is zelf "
                  "een bevinding."),
            ("p", "Voor vijfhonderd meetwaarden tussen nul en honderd zijn <strong>ongeveer tien klassen "
                  "van tien eenheden breed</strong> een redelijke keuze. Let wel: <strong>het aantal "
                  "klassen dat je kiest, verandert hoe de verdeling eruitziet</strong>. Met twee klassen "
                  "zie je niets, met honderd zie je ruis. Probeer er een paar en kies er een die de "
                  "vorm laat zien zonder hem te verzinnen."),
        ]),
    ],
    onthoud=[
        "Absoluut = hoe vaak, relatief = het aandeel, cumulatief = tot en met die waarde.",
        "De som van de relatieve frequenties is één; de laatste cumulatieve frequentie is het totaal.",
        "Relatieve frequenties maken groepen van verschillende grootte vergelijkbaar.",
        "Groeperen doe je bij heel veel verschillende waarden. Het klassenmidden is het gemiddelde van de twee grenzen.",
        "Klassen mogen niet overlappen en mogen geen gat laten; een lege klasse mag wel.",
        "Uit een gegroepeerde tabel haal je de ruwe waarden niet meer terug, en het aantal klassen verandert de vorm.",
    ],
)

# ───────────────────────── 14. De juiste grafische voorstelling kiezen
BUNDELS["de-juiste-grafische-voorstelling-kiezen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De juiste grafische voorstelling kiezen",
    onder="Zes soorten grafieken, wanneer je ze kiest, en hoe je er niet mee misleidt.",
    secties=[
        dict(kop="De zes die de fiche noemt", blokken=[
            ("p", "De vakfiche noemt er <strong>zes</strong> bij naam: <strong>staafdiagram, "
                  "lijndiagram, dotplot, histogram, spreidingsdiagram en boxplot</strong>. Een "
                  "cirkeldiagram staat er niet bij."),
            ("p", tabel(["Voorstelling", "Wanneer", "Voorbeeld"], [
                ["staafdiagram", "categorieën tellen; de staven staan los", "het aantal leerlingen per studierichting"],
                ["lijndiagram", "een verloop in de tijd", "het aantal werklozen per maand over tien jaar"],
                ["dotplot", "een kleine dataset; één stip per meting boven de getallenas", "de punten van één klas"],
                ["histogram", "een continue variabele in klassen; de staven raken elkaar", "de lengte van duizend leerlingen"],
                ["spreidingsdiagram", "het verband tussen twee numerieke variabelen", "slaapuren tegenover het punt op een toets"],
                ["boxplot", "de vijf kengetallen, of groepen vergelijken", "vier klassen naast elkaar op dezelfde as"],
            ])),
            ("fig", svg.staafdiagram([("Human.", 48), ("Econ.", 31), ("Wet.", 27), ("Talen", 19)],
                                     breedte=380, hoogte=190, stap=10, waarden=True),
             "Een staafdiagram: de richtingen zijn categorieën, dus de staven staan los."),
            ("fig", svg.dotplot([4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 10]),
             "Een dotplot van zestien punten. Vier stippen boven de zeven betekent dat die waarde vier keer voorkomt."),
            ("fig", svg.lijngrafiek([42, 45, 51, 49, 55, 61, 58, 64], breedte=380, hoogte=190,
                                    labels=["ja", "fe", "ma", "ap", "me", "ju", "jl", "au"], stap=20),
             "Een lijndiagram: de tijd loopt door, dus de punten mogen verbonden worden."),
        ]),
        dict(kop="Staafdiagram of histogram?", blokken=[
            ("p", "Het verschil is klein om te tekenen en groot van betekenis. Bij een "
                  "<strong>histogram staan de staven tegen elkaar</strong>, bij een "
                  "<strong>staafdiagram los</strong>. Die aansluitende staven tonen dat de waarden "
                  "<strong>doorlopen</strong>; dat is precies wat je bij een continue variabele wil "
                  "zeggen."),
            ("p", "Daarom is een histogram <strong>niet geschikt voor een niet-numerieke</strong> "
                  "variabele zoals haarkleur: tussen blond en bruin loopt niets door. En een "
                  "<strong>lijndiagram van het aantal leerlingen per studierichting</strong> is ook "
                  "fout, want tussen twee richtingen zit geen verloop; neem daar een staafdiagram."),
            ("p", "Uit de <strong>hoogte van een staaf in een histogram</strong> lees je af "
                  "<strong>hoeveel gegevens er in die klasse vallen</strong>. Wil je beoordelen of een "
                  "verdeling <strong>normaal</strong> is, dan kies je een histogram: daar zie je de "
                  "klokvorm."),
            ("weetje", "Een <strong>dotplot is onbruikbaar bij tienduizend waarden</strong>: je krijgt "
                       "torens van stippen die niemand kan tellen. Daar neem je een histogram. En voor "
                       "<strong>dezelfde dataset kan meer dan één voorstelling zinvol zijn</strong>; de "
                       "vraag is telkens wat je wil laten zien."),
        ]),
        dict(kop="De vorm beschrijven", blokken=[
            ("p", "Een histogram met één hoge staaf en veel lage staven rechts ervan noem je "
                  "<strong>scheef naar rechts</strong>, met een lange staart aan de rechterkant. Zie je "
                  "<strong>twee duidelijke toppen</strong>, dan is de eerste gedachte dat er "
                  "<strong>twee verschillende groepen</strong> in je data zitten."),
            ("fig", svg.histogram([(0, 10, 4), (10, 20, 17), (20, 30, 11), (30, 40, 6),
                                   (40, 50, 3), (50, 60, 2), (60, 70, 1)],
                                  xlabel="euro", ylabel="aantal"),
             "Vierenveertig bedragen, scheef naar rechts: de top ligt links en de staart loopt ver door naar rechts."),
            ("p", "Uit een <strong>boxplot</strong> lees je af waar de <strong>helft van de middelste "
                  "gegevens</strong> ligt: dat is de doos. Twee boxplots naast elkaar op dezelfde as "
                  "zijn ook de beste keuze om te laten zien dat <strong>één groep veel meer "
                  "uitschieters</strong> heeft."),
            ("p", "Uit een histogram kan je het gemiddelde <strong>enkel schatten</strong>, niet exact "
                  "aflezen: de afzonderlijke waarden zitten in de klassen verstopt."),
        ]),
        dict(kop="Eerlijk tekenen", blokken=[
            ("p", "Een grafische voorstelling kan <strong>statistisch juist zijn en de lezer toch "
                  "misleiden</strong>. Dit zijn de klassiekers."),
            ("p", tabel(["Wat je ziet", "Wat er mis is", "Wat je doet"], [
                ["de verticale as van een staafdiagram begint bij tachtig", "kleine verschillen lijken veel groter dan ze zijn", "laat ze bij nul beginnen"],
                ["geen getallen op de zij-as", "er valt niets af te lezen, ook al klopt de vorm", "zet er een schaalverdeling op"],
                ["één staaf torent ver boven de rest uit", "de kleine staven worden onleesbaar laag", "zet de waarden boven de staven"],
                ["een tijdsas die van 2020 naar 2021 naar 2025 springt", "de afstanden zijn ongelijk, dus de stijging is vertekend", "gebruik een gelijkmatige tijdsas"],
                ["twee histogrammen met een andere schaal naast elkaar", "je kan de vormen niet vergelijken", "maak de assen gelijk"],
                ["driedimensionale staven", "de diepte verstoort het aflezen", "teken ze vlak"],
                ["twee grootheden met een andere eenheid in één beeld", "de ene schaal verplettert de andere", "twee grafieken boven elkaar met dezelfde tijdsas"],
            ])),
            ("kader", "<p>Een grafiek hoort <strong>altijd een titel en een naam bij elke as</strong> te "
                      "hebben, en een <strong>onderschrift zegt wat je ziet</strong>. De theorie "
                      "erachter hoort in de tekst, niet onder de tekening.</p>"),
            ("weetje", "De nul hoort op de as van een <strong>staafdiagram</strong>, want de lengte van "
                       "een staaf is de waarde. Bij een <strong>lijndiagram van de temperatuur</strong> "
                       "hoeft dat niet: daar is nul geen natuurlijk nulpunt van de schaal, en een "
                       "grafiek van 0 tot 40 graden verbergt net het verloop dat je wil tonen."),
        ]),
    ],
    onthoud=[
        "De zes van de fiche: staafdiagram, lijndiagram, dotplot, histogram, spreidingsdiagram en boxplot. Geen cirkeldiagram.",
        "Staven los = categorieën, staven tegen elkaar = een continue variabele in klassen.",
        "Een lijndiagram enkel bij een verloop in de tijd; een dotplot enkel bij weinig gegevens.",
        "Scheef naar rechts = top links, lange staart rechts. Twee toppen = waarschijnlijk twee groepen.",
        "Laat de as van een staafdiagram bij nul beginnen, zet getallen op de zij-as en waarden boven een uitschieter.",
        "Een onderschrift zegt wat je ziet; de theorie hoort in de tekst.",
    ],
)

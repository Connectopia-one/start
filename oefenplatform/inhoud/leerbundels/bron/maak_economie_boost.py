# -*- coding: utf-8 -*-
"""De leerbundels voor economie op 🚀 Boost doorstroom-niveau.

Gebaseerd op de vakfiche economische wetenschappen 2de graad doorstroom, geldig
vanaf 1 januari 2027. Die fiche geldt enkel voor de richting economische
wetenschappen en bestaat uit twee delen: economische wetenschappen (de eerste
twaalf thema's) en bedrijfswetenschappen (de laatste zeven).

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde hoofdstuk
behandelen dezelfde stof met andere vragen. Kim laadt de bundel dus twee keer
op, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../boost-doorstroom/economie.json`
doet daar het voorwerk voor.

De bundelsleutels eindigen op "-boost-doorstroom", de volledige naam van de
categorie, want een titel alleen is binnen een vak geen sleutel.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, svg

VAK = "Economie"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

def zet(slug, **b):
    b.setdefault("vak", VAK)
    b.setdefault("niveau", BOOST)
    BUNDELS[slug + "-boost-doorstroom"] = b


# ───────────────────────── 1. De economische kringloop
zet("de-economische-kringloop", titel="De economische kringloop",
    onder="Wie wat levert aan wie, en welke twee stromen daarbij in tegengestelde richting lopen.",
    secties=[
        dict(kop="Waarover gaat economie?", blokken=[
            ("p", "Economie als wetenschap gaat over <strong>keuzes maken met beperkte middelen</strong>. "
                  "De behoeften van mensen zijn onbeperkt, maar geld, tijd, grond en machines zijn dat niet. "
                  "Dat spanningsveld heet <strong>schaarste</strong>, en elke economische vraag komt daarop neer: "
                  "wie krijgt wat, en waarom?"),
            ("p", "Om dat overzichtelijk te houden, tekent een econoom een <strong>kringloopschema</strong>. "
                  "In het eenvoudige binnenlandse schema staan drie <strong>actoren</strong>: de "
                  "<strong>gezinnen</strong>, de <strong>bedrijven</strong> en de <strong>overheid</strong>. "
                  "Het buitenland hoort daar niet bij; dat komt er pas bij in het open schema."),
            ("p", "Zo'n schema is een vereenvoudiging, en dat is precies de bedoeling. Het laat de "
                  "<strong>samenhang</strong> zien: wie van wie afhankelijk is, en hoe geld rondgaat. "
                  "Daarvoor hoef je niet elk bedrijf apart te tekenen."),
        ]),
        dict(kop="De drie actoren en wat ze doen", blokken=[
            ("fig", svg.kringloop(), "De drie actoren van het binnenlandse schema."),
            ("p", "De <strong>gezinnen</strong> doen twee dingen tegelijk. Ze <strong>verbruiken</strong> "
                  "goederen en diensten, en ze <strong>leveren de productiefactoren</strong>: hun arbeid, "
                  "hun spaargeld, hun grond. Ze zijn dus nooit alleen verbruiker. Een "
                  "<strong>zelfstandige kapster zonder personeel</strong> hoort in het schema bij de gezinnen: "
                  "ze levert haar eigen arbeid en krijgt daarvoor een inkomen."),
            ("p", "De <strong>bedrijven</strong> produceren goederen en diensten met die productiefactoren. "
                  "Koopt een bakker bloem bij een molenaar, dan staan er twee <strong>bedrijven</strong> "
                  "tegenover elkaar; dat heet een verrichting tussen bedrijven. Koopt een bedrijf een "
                  "<strong>nieuwe machine</strong>, dan is die uitgave een <strong>investering</strong>."),
            ("p", "De <strong>overheid</strong> doet drie dingen: ze <strong>heft belastingen</strong>, ze "
                  "<strong>betaalt uitkeringen en subsidies</strong>, en ze <strong>levert collectieve "
                  "goederen</strong> zoals wegen, scholen en veiligheid. Een <strong>werkloosheidsuitkering</strong> "
                  "is dus een geldstroom van de overheid naar de gezinnen, en een <strong>subsidie aan een "
                  "sportclub</strong> is er ook een. Bouwt de overheid een school en betaalt ze een aannemer, "
                  "dan gaat die geldstroom van de overheid naar een bedrijf."),
        ]),
        dict(kop="Twee stromen, in tegengestelde richting", blokken=[
            ("p", "In een kringloop lopen altijd <strong>twee stromen</strong>. De <strong>reële stroom</strong> "
                  "is alles wat echt van hand tot hand gaat: goederen, diensten en productiefactoren. De "
                  "<strong>geldstroom</strong> is de betaling daarvoor. Die twee lopen "
                  "<strong>tegengesteld</strong>: wat de ene kant uitgaat, wordt de andere kant betaald. Twee "
                  "stromen in dezelfde richting bestaan dus niet."),
            ("p", "Koopt een gezin brood bij de bakker, dan gaat er een <strong>geldstroom</strong> van het gezin "
                  "naar de bakker en een reële stroom (het brood) terug. Gaat een werknemer werken bij een "
                  "bedrijf, dan loopt er een <strong>reële stroom</strong> van het gezin naar het bedrijf: "
                  "zijn <strong>arbeid</strong>. De <strong>diensten van een kapper</strong> horen bij de reële "
                  "stroom, niet bij de geldstroom: een dienst is niet tastbaar, maar wel echt geleverd."),
            ("kader", "Geldstromen zijn: een loon, een belasting, een uitkering, een betaling voor goederen. "
                      "Reële stromen zijn: arbeid, goederen, diensten, het gebruik van grond of kapitaal. "
                      "Daarom tekent een econoom de kringloop vaak met <strong>pijlen in twee kleuren</strong>: "
                      "zo zie je in één oogopslag welke pijl geld is en welke niet."),
        ]),
        dict(kop="De vergoeding voor elke productiefactor", blokken=[
            ("p", "Wie een productiefactor levert, krijgt er een vergoeding voor. Die vier namen moet je uit "
                  "elkaar kunnen houden:"),
            ("kader", tabel(["productiefactor", "vergoeding"],
                            [["arbeid", "<strong>loon</strong>"],
                             ["kapitaal", "<strong>intrest</strong>"],
                             ["natuur of grond", "<strong>pacht</strong>"],
                             ["ondernemerschap", "<strong>winst</strong>"]])),
            ("p", "In de kringloop betaalt dus het <strong>bedrijf een vergoeding aan het gezin</strong> voor de "
                  "geleverde productiefactoren, en het gezin betaalt het bedrijf voor de goederen en diensten. "
                  "Daarom heet het een <strong>kringloop en geen rechte lijn</strong>: het geld komt telkens weer "
                  "terug bij wie het uitgegeven heeft. Elke <strong>uitgave van de ene actor is een inkomen voor "
                  "een andere</strong>, en dus: geeft de ene minder uit, dan verliest een andere inkomen."),
        ]),
        dict(kop="Lekken en injecties", blokken=[
            ("p", "Niet al het geld blijft rondgaan. Een <strong>lek</strong> is geld dat uit de binnenlandse "
                  "kringloop verdwijnt. Een <strong>injectie</strong> is geld dat erbij komt. Met die twee "
                  "woorden kan je uitleggen waarom de kringloop krimpt of groeit."),
            ("kader", tabel(["lekken", "injecties"],
                            [["sparen", "investeringen"],
                             ["belastingen", "overheidsuitgaven"],
                             ["invoer", "uitvoer"]])),
            ("p", "Spaart een gezin een deel van zijn inkomen, dan gaat dat deel <strong>niet</strong> naar de "
                  "bedrijven: er lekt geld weg. <strong>Invoer</strong> is dus een lek en geen injectie, want het "
                  "geld gaat naar het buitenland. Wat een gezin overhoudt om te besteden, reken je zo uit: van "
                  "2 500 euro loon gaan 600 euro belasting en 300 euro sparen af, dus blijft er "
                  "<strong>1 600 euro</strong> over."),
        ]),
        dict(kop="Het buitenland erbij", blokken=[
            ("p", "Neem je het buitenland mee, dan komen er twee stromen bij: <strong>invoer</strong> en "
                  "<strong>uitvoer</strong>. Invoer zijn de goederen die uit het buitenland het land "
                  "<strong>binnenkomen</strong>; uitvoer is wat het land verkoopt. Verkoopt een Belgisch bedrijf "
                  "machines aan een klant in Spanje, dan is dat voor België <strong>uitvoer</strong>, en komt er "
                  "geld van buiten de kringloop binnen."),
        ]),
    ],
    onthoud=[
        "Economie gaat over keuzes maken met schaarse middelen.",
        "Het eenvoudige binnenlandse schema heeft drie actoren: gezinnen, bedrijven en de overheid.",
        "Gezinnen verbruiken én leveren de productiefactoren; een zelfstandige zonder personeel hoort bij de gezinnen.",
        "De reële stroom (goederen, diensten, arbeid) en de geldstroom lopen tegengesteld.",
        "Arbeid geeft loon, kapitaal intrest, natuur pacht, ondernemerschap winst.",
        "Elke uitgave van de ene actor is een inkomen voor een andere.",
        "Lekken: sparen, belastingen, invoer. Injecties: investeringen, overheidsuitgaven, uitvoer.",
    ])


# ───────────────────────── 2. Productie, toegevoegde waarde en het bbp
zet("productie-toegevoegde-waarde-en-het-bbp",
    titel="Productie, toegevoegde waarde en het bbp",
    onder="Van wat één bedrijf toevoegt naar het cijfer van een heel land, nominaal en reëel.",
    secties=[
        dict(kop="Produceren en toegevoegde waarde", blokken=[
            ("p", "<strong>Produceren</strong> betekent in economische zin: <strong>waarde toevoegen</strong>. "
                  "Dat hoeft niets met een fabriek te maken te hebben. Een transportbedrijf dat goederen van de "
                  "haven naar een winkel brengt, voegt waarde toe: daar zijn ze meer waard dan in de haven."),
            ("p", "De <strong>toegevoegde waarde</strong> van een bedrijf is de <strong>omzet min de aankopen "
                  "bij andere bedrijven</strong>. Lonen trek je er niet af, want die zijn juist een deel van "
                  "wat het bedrijf toevoegt. Een meubelmaker die voor 400 euro hout koopt en een kast voor "
                  "1 100 euro verkoopt, voegt dus <strong>700 euro</strong> toe. Een garagist die onderdelen "
                  "voor 1 200 euro koopt, 2 000 euro lonen betaalt en 4 500 euro factureert, voegt "
                  "<strong>3 300 euro</strong> toe: 4 500 &minus; 1 200, en de lonen blijven erin."),
            ("weetje", "Veel omzet betekent niet automatisch veel toegevoegde waarde. Een handelaar die voor "
                       "miljoenen inkoopt en met een kleine marge doorverkoopt, heeft een grote omzet en een "
                       "kleine toegevoegde waarde."),
        ]),
        dict(kop="De bedrijfskolom", blokken=[
            ("p", "De keten van bedrijven van <strong>grondstof tot eindproduct</strong> heet een "
                  "<strong>bedrijfskolom</strong>. Elk bedrijf in die kolom voegt een stuk waarde toe."),
            ("fig", svg.stappen(["boer|graan 200", "maalderij|meel 350", "bakker|brood 800"]),
                    "Eén bedrijfskolom, met de verkoopprijs van elke schakel."),
            ("p", "De toegevoegde waarde van de <strong>maalderij</strong> is 350 &minus; 200 = "
                  "<strong>150</strong>. Die van de boer is 200, die van de bakker 800 &minus; 350 = 450. "
                  "Samen: 200 + 150 + 450 = <strong>800</strong>, en dat is precies de "
                  "<strong>waarde van het eindproduct</strong>."),
            ("p", "Daarom tel je in een bedrijfskolom de <strong>toegevoegde waarden</strong> op en niet de "
                  "omzetten: anders tel je het graan drie keer mee. Om diezelfde reden tellen "
                  "<strong>intermediaire goederen</strong> niet apart mee in het bbp. Papier dat een drukkerij "
                  "koopt om er boeken van te maken, is zo'n intermediair goed: zijn waarde zit al in het boek."),
        ]),
        dict(kop="Wat is het bbp?", blokken=[
            ("p", "Het <strong>bruto binnenlands product</strong> is de <strong>som van alle toegevoegde "
                  "waarden binnen de grenzen van een land in één jaar</strong>. Waar het eigendom zit, doet niet "
                  "mee: een <strong>Duits bedrijf met een fabriek in Gent</strong> telt mee in het Belgische "
                  "bbp, want de productie gebeurt hier."),
            ("p", "Het woord <strong>bruto</strong> zegt dat de <strong>afschrijvingen er nog niet af zijn</strong>: "
                  "de slijtage van machines en gebouwen is niet in mindering gebracht. En het bbp is een "
                  "<strong>stroomgrootheid</strong>: het meet wat er in een periode bijkomt, niet wat er op een "
                  "bepaald moment staat."),
            ("kader", "Deze zaken tellen <strong>niet</strong> mee in het bbp van dit jaar: "
                      "<strong>gratis werk thuis</strong> (koken voor je gezin), <strong>zwartwerk</strong>, de "
                      "verkoop van een <strong>tweedehandswagen</strong> (die productie zat in een eerder jaar) "
                      "en de <strong>intermediaire goederen</strong>."),
        ]),
        dict(kop="Nominaal, reëel en het basisjaar", blokken=[
            ("p", "Het <strong>nominale bbp</strong> rekent met de prijzen van <strong>dit</strong> jaar. Het "
                  "<strong>reële bbp</strong> rekent met de prijzen van een vast <strong>basisjaar</strong>, "
                  "zodat je twee jaren eerlijk kan vergelijken. In het basisjaar zelf zijn ze aan elkaar gelijk."),
            ("p", "Produceert een land evenveel stuks als vorig jaar, maar stijgen alle prijzen met 4 %, dan "
                  "stijgt het <strong>nominale</strong> bbp met ongeveer 4 % en blijft het "
                  "<strong>reële</strong> bbp gelijk. Een stijging van het nominale bbp betekent dus "
                  "<strong>niet</strong> automatisch dat er meer geproduceerd is."),
            ("kader", "De <strong>reële groei</strong> krijg je zo: neem de groei van het nominale bbp en haal "
                      "de <strong>prijsstijging</strong> eraf. Nominaal +5 % met prijzen +2 % geeft ongeveer "
                      "<strong>+3 %</strong>. Nominaal +2 % met prijzen +3 % geeft ongeveer "
                      "<strong>&minus;1 %</strong>: de reële groei is dan negatief."),
            ("p", "Een gewone <strong>groeivoet</strong> reken je altijd op het oude cijfer. Gaat het bbp van "
                  "400 naar 420 miljard euro, dan is de groei 20 op 400, dus <strong>5 %</strong>. Staat er in "
                  "een tabel: 2026 bbp 500, 2027 bbp 530 en prijzen +2 %, dan is de nominale groei 6 % en de "
                  "reële groei ongeveer 4 %."),
        ]),
        dict(kop="Bbp per capita", blokken=[
            ("p", "Het <strong>bbp per capita</strong> is het <strong>bbp gedeeld door het aantal "
                  "inwoners</strong>. Een land met 600 miljard euro bbp en 12 miljoen inwoners komt uit op "
                  "<strong>50 000 euro per inwoner</strong>."),
            ("p", "Daarmee vergelijk je landen eerlijker dan met het bbp zelf: een groot land heeft bijna altijd "
                  "een groter bbp, ook als zijn inwoners minder welvarend zijn. Let wel op de verhouding tussen "
                  "de twee cijfers: stijgt het bbp met 2 % en de bevolking met 3 %, dan <strong>daalt</strong> het "
                  "bbp per capita."),
        ]),
        dict(kop="Waar de cijfers staan, en wat ze niet zeggen", blokken=[
            ("p", "De Belgische cijfers komen van <strong>Statbel</strong>, de statistische dienst van de "
                  "federale overheid, en van de <strong>Nationale Bank van België</strong>, die de nationale "
                  "rekeningen en de economische vooruitzichten publiceert."),
            ("p", "Het bbp heeft <strong>beperkingen</strong> als maatstaf. Het zegt niets over de "
                  "<strong>verdeling</strong> van de welvaart, niets over het <strong>milieu</strong>, en het "
                  "negeert <strong>onbetaald werk</strong>. Het kan zelfs stijgen door iets slechts: worden na een "
                  "storm veel daken hersteld, dan <strong>stijgt</strong> het bbp, terwijl niemand er beter van "
                  "geworden is."),
            ("p", "Een grafiek met <strong>jaarlijkse groeicijfers</strong> lees je het best door naar het "
                  "<strong>teken en de trend</strong> te kijken: blijven de staven boven nul, dan groeit de "
                  "economie elk jaar, ook als de staven kleiner worden. Een kleinere staaf betekent "
                  "<strong>minder snelle groei</strong>, geen krimp."),
        ]),
    ],
    onthoud=[
        "Produceren is waarde toevoegen; toegevoegde waarde = omzet min de aankopen bij andere bedrijven.",
        "De lonen trek je niet af van de toegevoegde waarde.",
        "In een bedrijfskolom is de som van de toegevoegde waarden gelijk aan de waarde van het eindproduct.",
        "Het bbp is de som van alle toegevoegde waarden binnen de grenzen van een land in één jaar.",
        "Bruto betekent: de afschrijvingen zijn er nog niet af. Het bbp is een stroomgrootheid.",
        "Reële groei ≈ nominale groei min de prijsstijging; het reële bbp rekent met de prijzen van het basisjaar.",
        "Bbp per capita = bbp gedeeld door het aantal inwoners.",
        "Het bbp zegt niets over verdeling, milieu of onbetaald werk.",
    ])


# ───────────────────────── 3. Economische groei, welvaart en welzijn
zet("economische-groei-welvaart-en-welzijn",
    titel="Economische groei, welvaart en welzijn",
    onder="Waar groei vandaan komt, wat ze oplevert, en waarom welvaart en welzijn niet hetzelfde zijn.",
    secties=[
        dict(kop="Wat is economische groei?", blokken=[
            ("p", "<strong>Economische groei</strong> is een <strong>stijging van het reële bbp</strong>. Reëel, "
                  "want een stijging die enkel van hogere prijzen komt, is geen groei. Stijgt het reële bbp vijf "
                  "jaar na elkaar met 2 %, dan wordt er elk jaar <strong>meer</strong> geproduceerd dan het jaar "
                  "ervoor, en komt er dus elk jaar iets bij."),
        ]),
        dict(kop="Waar groei vandaan komt", blokken=[
            ("p", "Er zijn vijf oorzaken die je moet kunnen noemen:"),
            ("kader", tabel(["oorzaak", "wat het betekent"],
                            [["<strong>arbeidsproductiviteit</strong>", "de productie per werknemer stijgt"],
                             ["<strong>kapitaalvorming</strong>", "investeren in machines en gebouwen om later meer te kunnen produceren"],
                             ["<strong>technologische ontwikkeling</strong>", "nieuwe machines en methodes"],
                             ["<strong>menselijk kapitaal</strong>", "de kennis en de vaardigheden van de mensen in een land"],
                             ["<strong>bevolkingsgroei</strong>", "meer handen aan het werk"]])),
            ("p", "<strong>Arbeidsproductiviteit</strong> is de productie <strong>per werknemer</strong>. Bakt "
                  "een bakkerij met 4 werknemers eerst 800 en na een nieuwe oven 1 000 broden per dag, dan is de "
                  "<strong>productiviteit gestegen</strong>, niet het aantal mensen. Omgekeerd: een stijging van "
                  "de arbeidsproductiviteit betekent dus <strong>niet</strong> dat er meer mensen werken."),
            ("p", "<strong>Onderwijs</strong> is een oorzaak van groei omdat het het menselijk kapitaal "
                  "verhoogt: mensen die meer kunnen, produceren meer per uur. Een land dat zwaar investeert in "
                  "<strong>internetverbindingen en opleidingen</strong>, zet daarmee twee oorzaken in: "
                  "<strong>kapitaalvorming</strong> en <strong>menselijk kapitaal</strong>."),
            ("p", "<strong>Investeren</strong> kost vandaag geld en levert pas later meer productie op. Een land "
                  "dat veel <strong>spaart</strong>, kan daarmee ook meer investeren: het spaargeld van de "
                  "gezinnen is wat de bedrijven lenen. Koopt een bedrijf robots en ontslaat het niemand, dan is "
                  "het meest waarschijnlijke gevolg dat het <strong>meer produceert met dezelfde mensen</strong>."),
            ("p", "Groei kan niet eindeloos uit <strong>bevolkingsgroei alleen</strong> komen: komen er even veel "
                  "mensen bij als er productie bijkomt, dan blijft het bbp <strong>per inwoner</strong> gelijk. "
                  "Stijgt het bbp door bevolkingsgroei, dan gaat dus niet automatisch elke inwoner erop vooruit. "
                  "Een regering die de groei wil aanzwengelen, mikt daarom het best op "
                  "<strong>productiviteit</strong>: opleiding, onderzoek en investeringen."),
        ]),
        dict(kop="Welvaart en welzijn", blokken=[
            ("p", "<strong>Welvaart</strong> is de mate waarin je met de beschikbare middelen je behoeften kan "
                  "voldoen: het gaat over <strong>goederen en diensten</strong>, en je kan ze in geld uitdrukken. "
                  "<strong>Welzijn</strong> is breder: hoe <strong>goed</strong> iemand zich voelt, met zijn "
                  "gezondheid, zijn vrije tijd, zijn omgeving en zijn veiligheid erbij. Het zijn dus "
                  "<strong>geen synoniemen</strong>."),
            ("p", "Daarom gebruiken economen naast het bbp ook <strong>andere maatstaven</strong>: cijfers over "
                  "gezondheid, onderwijs, ongelijkheid en milieu. Een hoog bbp per capita is "
                  "<strong>geen waarborg</strong> dat een land ook hoog scoort op gezondheid of onderwijs, en het "
                  "<strong>bbp per capita zegt niets over de verdeling</strong>: één gemiddelde kan een heel "
                  "gelijke en een heel ongelijke samenleving beschrijven."),
            ("kader", "Zaken die het <strong>welzijn verhogen maar niet in het bbp komen</strong>: vrije tijd, "
                      "een gezonde leefomgeving, vrijwilligerswerk, mantelzorg, veiligheid op straat."),
        ]),
        dict(kop="Wat groei oplevert, en wat ze kost", blokken=[
            ("p", "Groei kan <strong>werk</strong> opleveren, <strong>hogere inkomens</strong>, en meer "
                  "belastinginkomsten waarmee de overheid scholen en zorg betaalt. Het meest genoemde "
                  "<strong>negatieve</strong> effect is de <strong>belasting van het milieu</strong>: meer "
                  "productie betekent vaak meer uitstoot, afval en grondstofgebruik."),
            ("p", "Stijgt het bbp van een land sterk terwijl de lucht in de steden slechter wordt, dan kan je "
                  "besluiten dat de <strong>welvaart stijgt en het welzijn daalt</strong>. Werkt een land minder "
                  "uren en houdt het meer vrije tijd over, waardoor het bbp licht daalt, dan is dat "
                  "<strong>niet noodzakelijk slechter</strong>: het bbp daalt, het welzijn kan stijgen. En groei "
                  "leidt er niet altijd toe dat <strong>iedereen</strong> erop vooruitgaat; dat hangt van de "
                  "verdeling af."),
        ]),
        dict(kop="Hoe welvaart verdeeld wordt", blokken=[
            ("p", "De <strong>primaire inkomensverdeling</strong> is de verdeling van de productie onder de "
                  "productiefactoren: <strong>loon, intrest, pacht en winst</strong>. Dat is de verdeling zoals "
                  "ze uit de markt komt, vóór de overheid iets doet."),
            ("p", "Daarna <strong>herverdeelt</strong> de overheid: ze heft <strong>belastingen</strong> volgens "
                  "draagkracht, betaalt <strong>uitkeringen</strong> en levert <strong>diensten</strong> zoals "
                  "onderwijs en gezondheidszorg die iedereen kan gebruiken."),
        ]),
        dict(kop="Schaarste en duurzame groei", blokken=[
            ("p", "<strong>Schaarste</strong> is het verschijnsel dat de middelen beperkt zijn tegenover de "
                  "behoeften. Het is het <strong>uitgangspunt van heel de economie</strong>: was er van alles "
                  "genoeg, dan hoefde niemand te kiezen en bestond er geen economische vraag."),
            ("p", "<strong>Duurzame groei</strong> is groei die ook <strong>rekening houdt met de generaties na "
                  "ons</strong>: ze gebruikt grondstoffen en milieu niet sneller op dan ze zich herstellen. Een "
                  "gezin dat een duurdere wasmachine kiest die minder energie verbruikt, denkt op die manier: het "
                  "betaalt vandaag meer om later minder te verbruiken."),
        ]),
    ],
    onthoud=[
        "Economische groei is een stijging van het reële bbp.",
        "De oorzaken: arbeidsproductiviteit, kapitaalvorming, technologie, menselijk kapitaal en bevolkingsgroei.",
        "Arbeidsproductiviteit is de productie per werknemer, niet het aantal werknemers.",
        "Groei uit bevolkingsgroei alleen laat het bbp per inwoner gelijk.",
        "Welvaart gaat over goederen en diensten, welzijn over hoe goed iemand het heeft.",
        "Het bbp per capita zegt niets over de verdeling, het milieu of onbetaald werk.",
        "De primaire inkomensverdeling is loon, intrest, pacht en winst; daarna herverdeelt de overheid.",
        "Duurzame groei houdt rekening met de generaties na ons.",
    ])


# ───────────────────────── 4. Behoeften, schaarste en soorten goederen
zet("behoeften-schaarste-en-soorten-goederen",
    titel="Behoeften, schaarste en soorten goederen",
    onder="Waarom er altijd gekozen moet worden, en hoe je goederen van elkaar onderscheidt.",
    secties=[
        dict(kop="Behoeften en schaarste", blokken=[
            ("p", "Een <strong>behoefte</strong> is in economische zin een <strong>gevoel van gemis dat je wil "
                  "wegnemen</strong>. Behoeften zijn volgens economen <strong>onbeperkt</strong>: zodra er één "
                  "voldaan is, komt er een nieuwe bij. Wie een fiets heeft, wil een betere fiets."),
            ("p", "<strong>Schaarste</strong> is het feit dat de middelen om die behoeften te voldoen "
                  "<strong>beperkt</strong> zijn. Daarom heeft elke consument een "
                  "<strong>keuzeprobleem</strong>: hij kan niet alles hebben en moet dus kiezen. Een gezin dat "
                  "3 000 euro verdient en voor 3 600 euro wil kopen, loopt precies tegen dat probleem aan."),
            ("p", "Schaarste <strong>verdwijnt niet</strong> omdat een land rijk is. Rijkere mensen hebben andere "
                  "en duurdere behoeften, en tijd blijft voor iedereen beperkt."),
        ]),
        dict(kop="Kiezen is iets anders opgeven", blokken=[
            ("p", "Wie kiest, geeft <strong>altijd iets anders op</strong>. De waarde van het "
                  "<strong>beste alternatief dat je opgeeft</strong>, heet de <strong>alternatieve kost</strong> "
                  "of opportuniteitskost."),
            ("p", "Een student die tussen een laptop en een weekend weg kiest en er maar één kan betalen, geeft "
                  "met zijn keuze het andere op: dat is zijn alternatieve kost. Legt een gemeente een "
                  "<strong>park</strong> aan in plaats van een <strong>parking</strong>, dan is de alternatieve "
                  "kost de <strong>parking</strong> die er niet komt."),
            ("p", "Volgens de economische theorie kiest een consument <strong>rationeel</strong>: hij weegt wat "
                  "elke optie hem oplevert tegen wat ze kost, en kiest wat hem het meeste oplevert."),
        ]),
        dict(kop="Soorten behoeften", blokken=[
            ("p", "<strong>Economische behoeften</strong> voldoe je met <strong>schaarse</strong> middelen; er "
                  "moet dus iets voor opgegeven worden. <strong>Niet-economische behoeften</strong> voldoe je met "
                  "iets wat er in overvloed is, zoals lucht om te ademen. Een behoefte die je met een "
                  "<strong>gratis goed</strong> voldoet, is dus <strong>geen</strong> economische behoefte."),
            ("kader", tabel(["soort", "wat het is", "voorbeeld"],
                            [["<strong>primair</strong>", "nodig om te overleven", "eten, drinken, onderdak"],
                             ["<strong>secundair</strong>", "niet nodig, wel gewoon geworden", "een fiets, een gsm"],
                             ["<strong>tertiair</strong>", "luxe", "een tweede verblijf"]])),
            ("p", "Die grens ligt niet vast: <strong>wat voor de ene een luxe is, kan voor de andere een gewone "
                  "behoefte zijn</strong>. Een auto is luxe in een stad met metro en noodzaak op het platteland."),
        ]),
        dict(kop="Goederen indelen", blokken=[
            ("p", "Dezelfde goederen kan je op verschillende manieren indelen. Elke indeling antwoordt op een "
                  "andere vraag."),
            ("kader", tabel(["indeling", "het verschil"],
                            [["<strong>individueel of collectief</strong>",
                              "een individueel goed gebruikt één persoon; een <strong>collectief goed</strong> gebruikt iedereen samen en je kan er niemand van uitsluiten"],
                             ["<strong>tastbaar of niet-tastbaar</strong>",
                              "een niet-tastbaar goed heet een <strong>dienst</strong>"],
                             ["<strong>verbruiks- of gebruiksgoed</strong>",
                              "een verbruiksgoed is na één keer op, een gebruiksgoed gaat mee"],
                             ["<strong>consumptie- of investeringsgoed</strong>",
                              "een investeringsgoed gebruik je om mee te <strong>produceren</strong>"]])),
            ("p", "<strong>Collectieve goederen</strong> zijn bijvoorbeeld straatverlichting, dijken, politie en "
                  "wegen. De <strong>overheid</strong> zorgt er meestal voor, want niemand kan er geld voor vragen "
                  "als je niemand kan uitsluiten. <strong>Verbruiksgoederen</strong> zijn brood, benzine en zeep; "
                  "een <strong>gebruiksgoed verdwijnt niet bij het eerste gebruik</strong>."),
            ("p", "Koopt een bakker een nieuwe <strong>oven</strong>, dan is die voor hem een "
                  "<strong>investeringsgoed</strong>. Dezelfde oven in een keuken thuis is een "
                  "consumptiegoed: <strong>hetzelfde goed kan voor de ene een investeringsgoed zijn en voor de "
                  "andere een consumptiegoed</strong>. Een auto die een gezin koopt om mee op vakantie te gaan is "
                  "een <strong>consumptiegoed</strong>, een <strong>gebruiksgoed</strong> en een "
                  "<strong>tastbaar</strong> goed tegelijk."),
            ("p", "Een <strong>vrij goed</strong> is een goed dat er in <strong>overvloed</strong> is en dat "
                  "<strong>niets kost</strong>, zoals zeewater aan de kust. <strong>Drinkbaar leidingwater is "
                  "dus geen vrij goed</strong>: het moet gezuiverd en getransporteerd worden en je betaalt ervoor."),
            ("p", "<strong>Onderwijs</strong> is voor wie er leert een <strong>dienst</strong>, dus niet-tastbaar, "
                  "en het is grotendeels een <strong>collectief</strong> goed dat de overheid aanbiedt. Een "
                  "<strong>intermediair goed</strong> is een goed dat een bedrijf koopt om er iets anders van te "
                  "maken, zoals het <strong>papier</strong> van een drukkerij. Die goederen tellen "
                  "<strong>niet apart mee in het bbp</strong>, want hun waarde zit al in het eindproduct."),
        ]),
        dict(kop="Waarom indelen nuttig is", blokken=[
            ("p", "De indelingen zijn geen woordspel. Ze bepalen <strong>wie iets aanbiedt en hoe het betaald "
                  "wordt</strong>: collectieve goederen komen van de overheid en worden met belastingen betaald, "
                  "investeringsgoederen worden afgeschreven, en intermediaire goederen mag je niet dubbel tellen. "
                  "Door een goed juist in te delen, weet je meteen welke regels erop van toepassing zijn."),
        ]),
    ],
    onthoud=[
        "Een behoefte is een gevoel van gemis; behoeften zijn onbeperkt, de middelen niet.",
        "Schaarste geeft een keuzeprobleem en verdwijnt ook in een rijk land niet.",
        "De alternatieve kost is de waarde van het beste alternatief dat je opgeeft.",
        "Economische behoeften voldoe je met schaarse middelen, niet-economische met vrije goederen.",
        "Primair is nodig om te overleven, secundair is gewoonte, tertiair is luxe — en die grens verschilt per persoon.",
        "Een collectief goed gebruikt iedereen samen; niemand is uit te sluiten, dus zorgt de overheid ervoor.",
        "Een dienst is een niet-tastbaar goed; een gebruiksgoed verdwijnt niet bij het eerste gebruik.",
        "Hetzelfde goed kan voor de ene een investeringsgoed en voor de andere een consumptiegoed zijn.",
        "Intermediaire goederen tellen niet apart mee in het bbp.",
    ])


# ───────────────────────── 5. Nut, preferentie en de indifferentiecurve
zet("nut-preferentie-en-de-indifferentiecurve",
    titel="Nut, preferentie en de indifferentiecurve",
    onder="Hoe een econoom tekent wat een consument even goed vindt, en waarom dat altijd daalt.",
    secties=[
        dict(kop="Nut, totaal nut en grensnut", blokken=[
            ("p", "<strong>Nut</strong> is de <strong>voldoening</strong> die een goed je geeft. Nut is "
                  "<strong>subjectief</strong>: het is voor iedereen anders en je kan het niet netjes in euro "
                  "uitdrukken. Geef een vegetariër en een vleesliefhebber hetzelfde stuk vlees, en het nut is "
                  "voor beiden totaal verschillend."),
            ("p", "Het <strong>totale nut</strong> is het nut van <strong>alle eenheden samen</strong>. Het "
                  "<strong>marginale nut</strong> of <strong>grensnut</strong> is het nut van "
                  "<strong>de laatste bijgekomen eenheid</strong>."),
            ("p", "De <strong>wet van het afnemende grensnut</strong> zegt: elke volgende eenheid levert "
                  "<strong>minder</strong> bij dan de vorige. Drinkt iemand op een warme dag glazen water met een "
                  "nut van 10, 7, 4 en 1, dan daalt het grensnut en <strong>stijgt het totale nut nog</strong> "
                  "(10, 17, 21, 22). Een dalend grensnut betekent dus <strong>niet</strong> dat het totale nut "
                  "daalt."),
            ("kader", "Het <strong>totale nut bereikt zijn maximum</strong> waar het <strong>grensnut nul "
                      "wordt</strong>. Eet iemand pannenkoeken met een grensnut van 8, 6, 3 en daarna "
                      "&minus;2, dan zegt die laatste waarde dat de vierde pannenkoek het totale nut "
                      "<strong>verlaagt</strong>: hij had beter gestopt na de derde."),
            ("p", "Dezelfde wet geldt ook voor <strong>geld</strong>: honderd euro extra betekent veel voor wie "
                  "weinig heeft en weinig voor wie veel heeft. Daarmee leg je ook de waterparadox uit: in de "
                  "woestijn betaalt iemand veel voor het <strong>eerste</strong> glas water en weinig voor het "
                  "tiende, want het grensnut van dat tiende glas is bijna nul."),
        ]),
        dict(kop="Preferentie en indifferentie", blokken=[
            ("p", "<strong>Preferentie</strong> is het <strong>verkiezen</strong> van de ene combinatie boven de "
                  "andere. <strong>Indifferentie</strong> is het omgekeerde: twee combinaties zijn "
                  "<strong>even goed</strong>, het maakt de consument niet uit welke hij krijgt."),
            ("p", "Wie 3 broden en 2 liter melk even goed vindt als 2 broden en 4 liter melk, is dus "
                  "<strong>indifferent</strong> tussen die twee combinaties."),
            ("p", "De theorie gaat uit van drie veronderstellingen over de consument: hij "
                  "<strong>kent zijn eigen voorkeuren</strong>, hij handelt <strong>rationeel</strong>, en hij "
                  "wil zijn <strong>nut maximaliseren</strong> met het geld dat hij heeft. Dat laatste is geen "
                  "morele uitspraak: het is de eenvoudigste aanname waarmee je gedrag kan voorspellen."),
        ]),
        dict(kop="De indifferentiecurve", blokken=[
            ("p", "Een <strong>indifferentiecurve</strong> stelt <strong>alle combinaties van twee goederen "
                  "voor die even veel nut geven</strong>. Langs één curve blijft het <strong>nut</strong> dus "
                  "gelijk."),
            ("fig", svg.indifferentiemap(), "Drie indifferentiecurven van dezelfde consument."),
            ("p", "Een indifferentiecurve <strong>daalt</strong>: krijg je van het ene goed meer, dan moet je van "
                  "het andere iets afgeven om even goed te blijven zitten. Ze is ook <strong>bol naar de "
                  "oorsprong</strong>, en dat komt recht uit het afnemende grensnut: wie al veel brood en weinig "
                  "melk heeft, geeft <strong>veel brood</strong> voor één liter melk, en omgekeerd. Was ze een "
                  "rechte, dan zou die ruilverhouding overal gelijk zijn, en dat klopt niet."),
            ("p", "De <strong>helling</strong> van de curve is precies die <strong>ruilverhouding</strong>: de "
                  "<strong>marginale substitutievoet</strong>. Naar rechts wordt de curve "
                  "<strong>vlakker</strong>, want daar heeft de consument al veel van het goed op de onderas en "
                  "geeft hij er makkelijker van af. Ziet hij twee goederen als bijna gelijkwaardig, dan ligt de "
                  "curve bijna als een <strong>rechte</strong> lijn."),
            ("p", "Twee combinaties op <strong>dezelfde</strong> curve geven even veel nut, en de consument is "
                  "er dus <strong>indifferent</strong> tussen: hij zal er geen van beide verkiezen. Vindt iemand "
                  "4 boeken met 1 spel even goed als 1 boek met 4 spellen, dan teken je die twee punten op "
                  "<strong>één en dezelfde</strong> curve."),
        ]),
        dict(kop="De indifferentiemap", blokken=[
            ("p", "Het geheel van <strong>alle</strong> indifferentiecurven van één consument heet een "
                  "<strong>indifferentiemap</strong>. Daarin geldt: hoe <strong>verder van de oorsprong</strong>, "
                  "hoe <strong>meer nut</strong>. Ligt punt A op een hogere curve dan punt B, dan geeft A dus "
                  "<strong>meer nut</strong> en verkiest de consument A."),
            ("p", "Twee curven van <strong>dezelfde</strong> consument kunnen elkaar <strong>niet "
                  "snijden</strong>: in het snijpunt zou dezelfde combinatie twee verschillende nutsniveaus "
                  "hebben, en dat kan niet. Krijgt een consument van allebei de goederen één eenheid meer, dan "
                  "schuift hij naar een <strong>hogere</strong> curve."),
            ("weetje", "Uit een indifferentiemap <strong>alleen</strong> kan je niet afleiden wat iemand koopt. "
                       "Je weet wel wat hij liever heeft, maar niet wat hij kan betalen. Daarvoor heb je de "
                       "<strong>budgetlijn</strong> nodig, en die staat in het volgende hoofdstuk."),
            ("p", "En waarom tekent men dit met <strong>twee</strong> goederen in plaats van met alle producten "
                  "samen? Omdat een tekening met twee assen te volgen is. Met drie goederen heb je een ruimtelijk "
                  "model nodig, en het <strong>inzicht blijft hetzelfde</strong>."),
        ]),
    ],
    onthoud=[
        "Nut is de voldoening die een goed geeft; het is subjectief en niet in euro te meten.",
        "Totaal nut is alle eenheden samen, grensnut is de laatste bijgekomen eenheid.",
        "De wet van het afnemende grensnut: elke volgende eenheid levert minder bij.",
        "Het totale nut is maximaal waar het grensnut nul wordt; een negatief grensnut verlaagt het totaal.",
        "Preferentie is verkiezen, indifferentie is even goed vinden.",
        "Een indifferentiecurve toont alle combinaties met hetzelfde nut: ze daalt en is bol naar de oorsprong.",
        "De helling van de curve is de marginale substitutievoet, de verhouding waarin je wil ruilen.",
        "In een indifferentiemap geeft de curve die het verst van de oorsprong ligt het meeste nut; twee curven snijden nooit.",
        "Uit een map alleen weet je wat iemand liever heeft, niet wat hij koopt.",
    ])


# ───────────────────────── 6. De budgetlijn en de optimale goederencombinatie
zet("de-budgetlijn-en-de-optimale-goederencombinatie",
    titel="De budgetlijn en de optimale goederencombinatie",
    onder="Wat een consument kan betalen, en waar dat samenvalt met wat hij het liefst heeft.",
    secties=[
        dict(kop="De budgetvergelijking", blokken=[
            ("p", "Een <strong>budgetvergelijking</strong> zegt dat alles wat een consument koopt samen "
                  "<strong>precies zijn budget</strong> opsoupeert. Ze heeft altijd dezelfde vorm: "
                  "<strong>prijs van x · aantal x + prijs van y · aantal y = het budget</strong>. Het "
                  "<strong>budget</strong> staat dus <strong>rechts</strong> van het gelijkheidsteken, in het <strong>rechterlid</strong>."),
            ("p", "Een consument met <strong>60 euro</strong>, boeken van 12 euro en films van 6 euro heeft als "
                  "budgetvergelijking <strong>12b + 6f = 60</strong>. Koopt hij niets anders, dan kan hij "
                  "<strong>5 boeken</strong> kopen. Koopt hij <strong>3 boeken</strong> (36 euro), dan blijft er "
                  "24 euro over voor <strong>4 films</strong>."),
            ("p", "Het bedrag dat een consument te besteden heeft, heet zijn <strong>budget</strong> of inkomen. "
                  "Nog een rekenvoorbeeld: een gezin met 240 euro, vlees aan 12 euro per kilo en groenten aan "
                  "4 euro per kilo kan bij 10 kilo vlees (120 euro) nog <strong>30 kilo groenten</strong> kopen."),
        ]),
        dict(kop="De budgetlijn", blokken=[
            ("p", "De <strong>budgetlijn</strong>, ook <strong>budgetrechte</strong> genoemd, is de lijn met "
                  "<strong>alle combinaties die de consument precies kan betalen</strong>. Om ze te tekenen heb je <strong>drie</strong> gegevens nodig: "
                  "het <strong>budget</strong> en de <strong>prijs van elk van de twee goederen</strong>. Wat hij "
                  "liever heeft, speelt hier nog geen rol."),
            ("fig", svg.budgetlijn(), "De budgetlijn en de hoogste indifferentiecurve die ze nog raakt."),
            ("p", "Een punt <strong>onder</strong> de budgetlijn is <strong>haalbaar</strong>, maar de consument "
                  "houdt er geld over: hij <strong>besteedt zijn budget niet volledig</strong>. Een punt "
                  "<strong>boven</strong> de lijn kan hij <strong>niet betalen</strong>. Daarom ligt het "
                  "<strong>optimum altijd óp de lijn</strong>: wie geld overhoudt, kan er altijd nog iets mee "
                  "kopen en zo meer nut halen."),
            ("p", "De budgetlijn is een <strong>rechte</strong> lijn zolang de prijzen vastliggen, en haar "
                  "<strong>helling</strong> wordt bepaald door de <strong>prijsverhouding</strong> van de twee "
                  "goederen. Kost een boek 12 euro en een film 6 euro, dan kost één boek extra hem "
                  "<strong>twee films</strong>, niet een halve. Met 100 euro, x aan 10 euro en y aan 20 euro "
                  "snijdt de lijn de <strong>y-as bij 5</strong>, want 100 gedeeld door 20 is 5."),
            ("kader", "Let op het verschil: de helling van de <strong>budgetlijn</strong> komt van de "
                      "<strong>prijzen op de markt</strong>, de helling van een <strong>indifferentiecurve</strong> "
                      "van de <strong>voorkeuren</strong> van de consument. In het optimum vallen die twee "
                      "hellingen samen. En alle punten op één budgetlijn geven zeker <strong>niet</strong> evenveel "
                      "nut; dat doen de punten op één indifferentiecurve."),
        ]),
        dict(kop="Wat de lijn doet verschuiven of kantelen", blokken=[
            ("p", "Verandert alleen het <strong>budget</strong>, dan schuift de lijn "
                  "<strong>parallel</strong> op: naar buiten bij meer geld, naar binnen bij minder. Die "
                  "beweging heet een <strong>parallelverschuiving</strong>, en de helling blijft gelijk."),
            ("p", "Verandert de <strong>prijs van één goed</strong>, dan <strong>kantelt</strong> de lijn: één "
                  "snijpunt met een as blijft staan, het andere schuift. Een prijswijziging van één goed "
                  "verandert dus wél de helling. Zakt bij een budget van 120 euro de prijs van x van 10 naar "
                  "<strong>6 euro</strong>, dan kan de consument maximaal <strong>20 stuks x</strong> kopen in "
                  "plaats van 12."),
            ("p", "Veranderen <strong>budget en prijzen in dezelfde verhouding</strong>, dan blijft de lijn "
                  "waar ze was. Verdubbelen prijzen én budget, dan zijn de <strong>haalbare combinaties exact "
                  "dezelfde</strong>. Een gezin dat 10 % opslag krijgt terwijl alle prijzen 10 % stijgen, heeft "
                  "dus <strong>dezelfde budgetlijn</strong> als daarvoor."),
        ]),
        dict(kop="De optimale goederencombinatie", blokken=[
            ("p", "Leg je de budgetlijn en de indifferentiemap over elkaar, dan ligt het "
                  "<strong>optimum</strong> waar de <strong>budgetlijn de hoogst bereikbare indifferentiecurve "
                  "raakt</strong>. Dat punt heet het <strong>raakpunt</strong>, en in dat punt zijn de "
                  "<strong>helling van de budgetlijn en die van de indifferentiecurve gelijk</strong>."),
            ("p", "De lijn <strong>raakt</strong> de curve in plaats van ze te snijden, en dat is geen detail: "
                  "bij een <strong>snijpunt</strong> ligt er altijd nog een stuk van de budgetlijn aan de andere "
                  "kant van de curve, en dus een <strong>hogere</strong> curve die ook haalbaar is. Een snijpunt "
                  "is dus <strong>nooit</strong> het optimum. En in het optimum kan de consument zijn nut "
                  "<strong>niet</strong> meer verhogen zonder zijn budget te overschrijden."),
            ("p", "Een combinatie die <strong>haalbaar maar niet optimaal</strong> is, zie je in de tekening zo: "
                  "ze ligt op of onder de budgetlijn, maar op een <strong>lagere</strong> indifferentiecurve dan "
                  "het raakpunt."),
            ("p", "Stijgt het <strong>budget</strong>, dan schuift het optimum naar een "
                  "<strong>hogere</strong> curve: de consument kan meer nut halen. Daalt de <strong>prijs van "
                  "goed x</strong>, dan zijn er twee gevolgen mogelijk: hij koopt meer van x, en hij kan ook "
                  "meer van y kopen, want hij houdt geld over."),
            ("p", "Twee consumenten met <strong>hetzelfde budget en dezelfde prijzen</strong> kunnen toch een "
                  "<strong>andere</strong> combinatie kiezen, want hun indifferentiemappen verschillen. Dat is "
                  "ook het antwoord op de vraag waarom deze theorie nuttig is, ook al rekent niemand zo in de "
                  "winkel: ze <strong>voorspelt de richting</strong> van het gedrag — wordt iets duurder, dan "
                  "kopen mensen er minder van — en meer moet een model niet doen."),
            ("weetje", "Een rekenvoorbeeld in het optimum: iemand besteedt 200 euro, x kost 20 euro en y kost "
                       "10 euro. Koopt hij 6 stuks x (120 euro), dan blijft er 80 euro over, dus "
                       "<strong>8 stuks y</strong>."),
        ]),
        dict(kop="Wat de overheid eraan verandert", blokken=[
            ("p", "De overheid kan de budgetlijn van een gezin <strong>naar buiten</strong> laten schuiven door "
                  "het <strong>budget te verhogen</strong> (een uitkering, een premie, minder belasting) of door "
                  "de <strong>prijzen te verlagen</strong> (een subsidie, een lagere btw). In beide gevallen "
                  "kan het gezin een hogere indifferentiecurve bereiken."),
        ]),
    ],
    onthoud=[
        "Budgetvergelijking: prijs x · aantal x + prijs y · aantal y = het budget.",
        "De budgetlijn toont alle combinaties die de consument precies kan betalen; je hebt het budget en twee prijzen nodig.",
        "Onder de lijn: haalbaar maar niet alles besteed. Boven de lijn: niet te betalen.",
        "De helling van de budgetlijn komt van de prijsverhouding, die van een indifferentiecurve van de voorkeuren.",
        "Alleen het budget wijzigt: parallelverschuiving. Eén prijs wijzigt: de lijn kantelt.",
        "Budget en prijzen in dezelfde verhouding: dezelfde budgetlijn.",
        "Het optimum is het raakpunt van de budgetlijn met de hoogst bereikbare indifferentiecurve.",
        "Een snijpunt is nooit het optimum, want dan is er nog een hogere curve haalbaar.",
    ])


# ───────────────────────── 7. Productiefactoren, productiefunctie en meeropbrengsten
zet("productiefactoren-productiefunctie-en-meeropbrengsten",
    titel="Productiefactoren, productiefunctie en meeropbrengsten",
    onder="Waarmee een bedrijf produceert, en waarom de twintigste werknemer minder toevoegt dan de tweede.",
    secties=[
        dict(kop="De vier productiefactoren", blokken=[
            ("p", "De economie onderscheidt <strong>vier</strong> productiefactoren: "
                  "<strong>arbeid</strong>, <strong>kapitaal</strong>, <strong>natuur</strong> en "
                  "<strong>ondernemerschap</strong>."),
            ("kader", tabel(["productiefactor", "wat eronder valt", "vergoeding"],
                            [["<strong>arbeid</strong>", "al het werk van mensen, met hoofd en handen", "loon"],
                             ["<strong>kapitaal</strong>", "machines, gebouwen, werktuigen, vervoer", "intrest"],
                             ["<strong>natuur</strong>", "grond, grondstoffen, water, wind", "pacht"],
                             ["<strong>ondernemerschap</strong>", "de andere drie samenbrengen en het risico dragen", "winst"]])),
            ("p", "Pas op met twee verwarringen. De <strong>machines</strong> die grondstoffen verwerken horen "
                  "bij <strong>kapitaal</strong>, niet bij natuur; de <strong>grondstoffen zelf</strong> horen "
                  "bij natuur. En <strong>geld is geen productiefactor</strong>: met geld koop je "
                  "productiefactoren, maar geld zelf maakt niets. Een landbouwer die grond huurt, betaalt dus "
                  "<strong>pacht</strong> voor de productiefactor <strong>natuur</strong>."),
            ("p", "De <strong>ondernemer</strong> staat apart omdat hij geen vast bedrag krijgt: hij draagt het "
                  "<strong>risico</strong> en houdt over wat er na alle andere vergoedingen overblijft. Zijn "
                  "beslissingen zijn: <strong>wat</strong> er geproduceerd wordt, <strong>hoeveel</strong>, "
                  "<strong>met welke combinatie</strong> van factoren, en <strong>of</strong> er geïnvesteerd "
                  "wordt. De theorie veronderstelt dat hij naar <strong>maximale winst</strong> streeft: dat is "
                  "de eenvoudigste aanname waarmee je zijn keuzes kan voorspellen."),
            ("p", "Een <strong>kapitaalgoed</strong> gaat <strong>jaren</strong> mee en wordt niet verwerkt (een "
                  "oven, een bestelwagen). Een <strong>intermediair goed</strong> wordt juist "
                  "<strong>verwerkt</strong> of verbruikt in de productie (bloem, papier, stroom). Schakelt een "
                  "bedrijf over op <strong>zonnepanelen</strong> voor zijn eigen stroom, dan spelen "
                  "<strong>kapitaal</strong> (de panelen) en <strong>natuur</strong> (de zon) samen."),
        ]),
        dict(kop="Korte en lange termijn", blokken=[
            ("p", "In de productietheorie is de <strong>korte termijn</strong> de periode waarin "
                  "<strong>minstens één productiefactor vastligt</strong>; op de <strong>lange termijn</strong> "
                  "kan een bedrijf <strong>al</strong> zijn factoren aanpassen."),
            ("p", "Een bakkerij kan snel een extra bakker aanwerven, maar niet snel een tweede oven plaatsen. "
                  "Daaruit volgt dat <strong>arbeid de variabele factor</strong> is en "
                  "<strong>kapitaal de factor die op korte termijn vastligt</strong>."),
            ("p", "Een <strong>productiefunctie</strong> is het verband tussen de ingezette productiefactoren en "
                  "de hoeveelheid die eruit komt. Dat verband is geen natuurwet: twee bedrijven met dezelfde "
                  "machines en evenveel werknemers kunnen toch een <strong>verschillende</strong> productie "
                  "halen, want organisatie, ervaring en motivatie spelen mee."),
            ("p", "Over <strong>arbeid</strong> moet je drie dingen weten: het is een <strong>menselijke</strong> "
                  "factor en dus geen voorraad die je kan opslaan, ze wordt vergoed met <strong>loon</strong>, en "
                  "ze is op korte termijn meestal de <strong>variabele</strong> factor."),
        ]),
        dict(kop="Totale, marginale en gemiddelde productie", blokken=[
            ("p", "De <strong>totale productie TP</strong> is alles wat een bedrijf bij een bepaalde inzet "
                  "maakt. De <strong>marginale productie MP</strong> is wat er bijkomt door "
                  "<strong>één eenheid arbeid meer</strong>; MP staat voor <strong>marginale productie</strong>. "
                  "De <strong>gemiddelde productie</strong> is de productie <strong>per eenheid arbeid</strong>: "
                  "TP gedeeld door het aantal werknemers."),
            ("p", "Produceert een bedrijf met 3 werknemers 90 stuks en met 4 werknemers 112 stuks, dan is de MP "
                  "van de vierde <strong>22</strong>. Maakt een bedrijf met 6 werknemers 150 stuks, dan is de "
                  "gemiddelde productie <strong>25 stuks</strong>."),
            ("p", "Uit de tabel TP = 10, 26, 48, 60, 65 bij 1 tot 5 werknemers lees je de MP af als het "
                  "<strong>verschil</strong> tussen twee opeenvolgende getallen: 10, 16, 22, 12, 5. De MP is dus "
                  "het grootst bij de <strong>derde</strong> werknemer."),
        ]),
        dict(kop="De wet van de toe- en afnemende meeropbrengsten", blokken=[
            ("p", "De <strong>wet van de toe- en afnemende meeropbrengsten</strong> zegt: voeg je bij een "
                  "<strong>vaste</strong> factor steeds meer van een variabele factor toe, dan "
                  "<strong>stijgt</strong> de meeropbrengst eerst en <strong>daalt</strong> ze daarna."),
            ("p", "MP <strong>stijgt in het begin</strong> omdat mensen kunnen samenwerken en zich "
                  "specialiseren: twee bakkers samen doen meer dan twee keer één. MP <strong>daalt vanaf een "
                  "bepaald punt</strong> omdat de vaste factor te klein wordt: er is maar één oven, en de "
                  "zevende bakker staat te wachten. Een restaurant met één keuken waar het bij 8 koks trager "
                  "begint te gaan, zit precies in dat <strong>afnemende</strong> deel."),
            ("p", "Zolang <strong>MP positief</strong> is, <strong>stijgt TP nog</strong>, ook als MP daalt. Een "
                  "dalende MP betekent dus <strong>niet</strong> dat het bedrijf minder produceert, enkel dat de "
                  "stijging kleiner wordt. <strong>TP bereikt zijn maximum waar MP nul is</strong>, en bij een "
                  "<strong>negatieve MP daalt TP</strong>."),
            ("kader", "Een reeks MP van 12, 20, 25, 18 en 9 zegt drie dingen: de meeropbrengst "
                      "<strong>stijgt eerst</strong> tot de derde werknemer, <strong>daalt daarna</strong>, en "
                      "<strong>TP blijft intussen stijgen</strong> omdat alle waarden positief zijn."),
            ("p", "Deze wet geldt <strong>alleen op korte termijn</strong>, want ze heeft een vaste factor nodig. "
                  "Op lange termijn kan een bedrijf alles aanpassen. Verdubbelt een tuinbedrijf dan zijn machines "
                  "<strong>én</strong> zijn personeel en stijgt de productie met <strong>meer</strong> dan het "
                  "dubbele, dan heet dat <strong>schaalvoordelen</strong>."),
            ("p", "Waarom dit voor de <strong>kosten</strong> belangrijk is: zolang elke extra werknemer "
                  "<strong>meer</strong> toevoegt, daalt de kost per stuk; zodra hij <strong>minder</strong> "
                  "toevoegt, stijgt ze. De vorm van de kostencurven in het volgende hoofdstuk komt dus recht uit "
                  "deze wet."),
        ]),
    ],
    onthoud=[
        "Vier productiefactoren: arbeid (loon), kapitaal (intrest), natuur (pacht), ondernemerschap (winst).",
        "Machines horen bij kapitaal, grondstoffen bij natuur, en geld is geen productiefactor.",
        "Korte termijn: minstens één factor ligt vast, meestal kapitaal. Lange termijn: alles kan mee.",
        "Een productiefunctie is het verband tussen de ingezette factoren en de productie.",
        "TP is de totale productie, MP de marginale productie (één eenheid arbeid meer), gemiddelde productie is TP per werknemer.",
        "De wet van de toe- en afnemende meeropbrengsten: MP stijgt eerst en daalt daarna.",
        "Zolang MP positief is, stijgt TP; TP is maximaal waar MP nul is.",
        "De wet geldt alleen op korte termijn; op lange termijn kan er van schaalvoordelen sprake zijn.",
    ])


# ───────────────────────── 8. De kosten- en de opbrengstencurven
zet("de-kosten-en-de-opbrengstencurven",
    titel="De kosten- en de opbrengstencurven",
    onder="Constant en variabel, totaal, gemiddeld en marginaal — en wat er bij volkomen concurrentie binnenkomt.",
    secties=[
        dict(kop="Constante en variabele kosten", blokken=[
            ("p", "De <strong>totale constante kosten TCK</strong> zijn de kosten die "
                  "<strong>niet van de productie afhangen</strong>. Ze lopen door, <strong>ook als een bedrijf "
                  "even niets produceert</strong>: huur, verzekering, afschrijvingen, het loon van de vaste "
                  "boekhouder. De <strong>variabele</strong> kosten bewegen wel mee: grondstoffen, verpakking, "
                  "energie voor de machines, uurlonen van tijdelijk personeel."),
            ("kader", tabel(["constante kosten", "variabele kosten"],
                            [["huur van het gebouw", "aankoop van grondstoffen"],
                             ["verzekering", "verpakking per stuk"],
                             ["afschrijving van de machines", "energie van de machines"]])),
            ("p", "De <strong>totale kosten TK</strong> zijn de <strong>constante plus de variabele</strong> "
                  "kosten. Een bedrijf met 2 000 euro constante kosten en 6 euro variabele kost per stuk heeft "
                  "bij 500 stuks TK van 2 000 + 3 000 = <strong>5 000 euro</strong>. TK staat voor "
                  "<strong>totale kosten</strong>."),
            ("p", "Het <strong>onderscheid</strong> tussen beide soorten is belangrijk, want het zegt wat er "
                  "gebeurt als de productie verandert. Wie zijn constante kosten kent, weet welk bedrag hij ook "
                  "bij nul productie kwijt is, en dus hoeveel hij minstens moet verkopen om die te dekken. Een "
                  "bakkerij met 1 500 euro huur per maand en 0,80 euro grondstof per brood heeft dus "
                  "<strong>1 500 euro constante kosten</strong>, een <strong>variabele kost van 0,80 euro per "
                  "brood</strong>, en ze betaalt die huur <strong>ook in een week zonder verkoop</strong>."),
        ]),
        dict(kop="Gemiddelde en marginale kosten", blokken=[
            ("p", "De <strong>gemiddelde kost GK</strong> is de <strong>kost per stuk</strong>: TK gedeeld door "
                  "de hoeveelheid. 5 000 euro totale kosten bij 500 stuks geeft een gemiddelde kost van "
                  "<strong>10 euro</strong>. De <strong>gemiddelde variabele kost</strong> kort je af als "
                  "<strong>GVK</strong>."),
            ("p", "De <strong>marginale kost MK</strong> is de <strong>extra kost van één stuk meer</strong>. "
                  "Het is dus <strong>niet</strong> het gemiddelde van alle stuks samen. Kost 100 stuks "
                  "1 200 euro en 101 stuks 1 209 euro, dan is MK van het 101ste stuk <strong>9 euro</strong>."),
            ("fig", svg.kostencurven(), "De gemiddelde totale kost, de gemiddelde variabele kost en de marginale kost."),
            ("p", "De <strong>gemiddelde constante kost GCK</strong> <strong>daalt</strong> voortdurend als de "
                  "productie stijgt: hetzelfde vaste bedrag wordt over meer stuks verdeeld. De "
                  "<strong>GK-curve</strong> heeft daardoor de vorm van een <strong>U</strong>: eerst dalend, "
                  "want de constante kost wordt uitgesmeerd, dan stijgend, want de variabele kost per stuk gaat "
                  "omhoog."),
            ("p", "<strong>MK stijgt vanaf een bepaald punt</strong>, en dat komt recht uit de wet van de "
                  "afnemende meeropbrengsten: elke extra werknemer voegt minder toe dan de vorige, dus kost elk "
                  "extra stuk meer. En onthoud de rekenregel tussen MK en GK: zolang <strong>MK onder GK</strong> "
                  "ligt, <strong>daalt</strong> GK; ligt MK erboven, dan stijgt GK. De MK-curve snijdt de GK-curve "
                  "dus precies in haar <strong>laagste punt</strong>."),
        ]),
        dict(kop="De opbrengsten bij volkomen concurrentie", blokken=[
            ("p", "De <strong>totale opbrengst TO</strong> is de <strong>prijs maal de hoeveelheid</strong>. "
                  "400 stuks aan 15 euro geeft een TO van <strong>6 000 euro</strong>. De "
                  "<strong>gemiddelde opbrengst GO</strong> is de opbrengst per stuk, en de "
                  "<strong>marginale opbrengst MO</strong> is wat er bijkomt door <strong>één stuk meer</strong> "
                  "te verkopen. MO staat voor <strong>marginale opbrengst</strong>."),
            ("p", "Bij <strong>volkomen concurrentie</strong> is een bedrijf te klein om de prijs te "
                  "beïnvloeden: het moet de marktprijs aanvaarden. Daardoor is <strong>GO gelijk aan de "
                  "prijs</strong> — elk stuk brengt hetzelfde op — en is <strong>MO óók gelijk aan de "
                  "prijs</strong>. Een landbouwer die aardappelen op de wereldmarkt verkoopt aan 0,35 euro per "
                  "kilo heeft bij de duizendste kilo dus een MO van <strong>0,35 euro</strong>."),
            ("p", "Daaruit volgt de vorm van de curven: <strong>TO</strong> is een "
                  "<strong>rechte stijgende</strong> lijn door de oorsprong, en <strong>MO</strong> een "
                  "<strong>horizontale</strong> lijn op de hoogte van de prijs. En wie bij volkomen concurrentie "
                  "meer wil verkopen, hoeft zijn prijs <strong>niet</strong> te verlagen: hij kan aan de "
                  "marktprijs alles kwijt wat hij maakt."),
        ]),
        dict(kop="Van kosten en opbrengsten naar winst", blokken=[
            ("p", "De <strong>totale winst</strong> kort je af als <strong>TW</strong>, en ze is "
                  "<strong>TO min TK</strong>. Een bedrijf met 8 000 euro TO en 7 200 euro TK maakt dus "
                  "<strong>800 euro winst</strong>. Een bedrijf maakt <strong>verlies</strong> zodra de "
                  "<strong>totale kosten hoger zijn dan de totale opbrengst</strong>; een hoge totale opbrengst "
                  "is dus <strong>geen</strong> waarborg voor winst."),
            ("p", "Om de winst bij een bepaalde hoeveelheid te berekenen, heb je <strong>drie</strong> gegevens "
                  "nodig: de <strong>prijs</strong>, de <strong>hoeveelheid</strong> en de "
                  "<strong>totale kosten</strong> (of de constante en variabele kosten waaruit je die berekent). "
                  "Voorbeeld: 250 stuks aan 20 euro geeft TO = 5 000 euro; met 3 000 euro constante kosten en "
                  "10 euro variabele kost per stuk is TK = 3 000 + 2 500 = 5 500 euro, dus een "
                  "<strong>verlies van 500 euro</strong>."),
            ("p", "Daarom tekent men de kosten- en de opbrengstencurven in <strong>dezelfde grafiek</strong>: zo "
                  "zie je in één blik bij welke hoeveelheden de opbrengst boven de kosten ligt, en waar het "
                  "verschil het grootst is. Ligt de prijs <strong>precies op de laagste gemiddelde kost</strong>, "
                  "dan maakt het bedrijf <strong>geen winst en geen verlies</strong>."),
        ]),
    ],
    onthoud=[
        "Constante kosten lopen door bij nul productie; variabele kosten bewegen mee met de productie.",
        "TK = constante kosten + variabele kosten. GK is TK per stuk.",
        "MK is de extra kost van één stuk meer, niet een gemiddelde.",
        "GCK daalt altijd; de GK-curve heeft de vorm van een U.",
        "Zolang MK onder GK ligt, daalt GK; MK snijdt GK in haar laagste punt.",
        "TO is prijs maal hoeveelheid; bij volkomen concurrentie zijn GO en MO gelijk aan de prijs.",
        "TO is dan een rechte door de oorsprong en MO een horizontale lijn.",
        "TW = TO − TK. Veel omzet is geen waarborg voor winst.",
    ])


# ───────────────────────── 9. De optimale productiegrootte en winstmaximalisatie
zet("de-optimale-productiegrootte-en-winstmaximalisatie",
    titel="De optimale productiegrootte en winstmaximalisatie",
    onder="Waarom een producent stopt waar MK gelijk is aan MO, en wanneer hij toch beter sluit.",
    secties=[
        dict(kop="Waar de winst het grootst is", blokken=[
            ("p", "De winst van een bedrijf is het grootst bij de hoeveelheid waar de "
                  "<strong>marginale kost gelijk is aan de marginale opbrengst</strong>: de twee "
                  "grootheden <strong>MK en MO</strong> zijn daar aan elkaar gelijk. Die hoeveelheid heet de <strong>optimale "
                  "productiegrootte</strong>."),
            ("p", "De reden is eenvoudig. Is <strong>MO groter dan MK</strong>, dan brengt het volgende stuk "
                  "<strong>meer op dan het kost</strong>: het bedrijf <strong>moet dus meer produceren</strong>, "
                  "en de winst stijgt nog. Is <strong>MK groter dan MO</strong>, dan kost het laatste stuk meer "
                  "dan het opbrengt, en kan het bedrijf zijn winst <strong>verhogen door minder te "
                  "produceren</strong>. Alleen waar ze gelijk zijn, valt er aan geen van beide kanten nog iets "
                  "te winnen. Wie per vergissing <strong>één stuk te veel</strong> maakt, verliest daar dus iets "
                  "op en moet terug naar het optimum."),
            ("p", "Verkoopt een bedrijf aan <strong>12 euro</strong> op een markt met volkomen concurrentie, dan "
                  "is MO gelijk aan 12 euro, en ligt zijn optimum waar <strong>MK 12 euro</strong> is. Staat er "
                  "in een tabel MK = 8 bij 5 stuks, 10 bij 6 stuks en 13 bij 7 stuks met een prijs van 10 euro, "
                  "dan is de optimale hoeveelheid <strong>6 stuks</strong>: bij 7 kost het extra stuk meer dan "
                  "het opbrengt."),
            ("p", "Een producent kijkt naar <strong>marginale</strong> en niet naar gemiddelde grootheden omdat "
                  "zijn beslissing altijd gaat over <strong>één stuk meer of minder</strong>. Een gemiddelde "
                  "zegt niets over dat laatste stuk. En het heet <strong>winst</strong>maximalisatie en geen "
                  "opbrengstmaximalisatie omdat de <strong>kosten meetellen</strong>: meer verkopen met verlies "
                  "op elk stuk maakt een bedrijf armer. In het optimum is de totale opbrengst dus "
                  "<strong>niet</strong> het hoogst; het <strong>verschil</strong> tussen opbrengst en kosten is "
                  "dat wel."),
            ("p", "Alleen het snijpunt in het <strong>stijgende</strong> deel van de MK-curve telt. In het "
                  "dalende deel zou één stuk meer juist <strong>minder</strong> kosten dan het opbrengt, en dan "
                  "is doorgaan nog altijd voordelig. Daarom is de <strong>stijgende tak van de MK-curve de "
                  "aanbodcurve van het bedrijf</strong>: ze zegt bij elke prijs hoeveel het wil aanbieden. "
                  "Stijgt de prijs van 10 naar <strong>14 euro</strong>, dan schuift het optimum naar rechts en "
                  "<strong>produceert het bedrijf meer</strong>."),
            ("kader", "Om het optimum <strong>grafisch</strong> te vinden heb je twee curven nodig: de "
                      "<strong>MK-curve</strong> en de <strong>MO-lijn</strong> (bij volkomen concurrentie de "
                      "prijs). Met een tabel van <strong>TO en TK</strong> per hoeveelheid vind je het ook: zoek "
                      "de rij waar <strong>TO &minus; TK</strong> het grootst is."),
            ("p", "Het <strong>optimum van de consument</strong> en dat van de <strong>producent</strong> lijken "
                  "op elkaar maar zijn niet hetzelfde: de consument maximaliseert zijn <strong>nut</strong> "
                  "binnen zijn budget, de producent zijn <strong>winst</strong>. En "
                  "<strong>niet alle bedrijven</strong> in een sector hebben dezelfde optimale "
                  "productiegrootte: hun kostenstructuur verschilt."),
        ]),
        dict(kop="Het break-evenpunt", blokken=[
            ("p", "Het <strong>break-evenpunt</strong> is de hoeveelheid waarbij de "
                  "<strong>winst nul</strong> is: de totale opbrengst dekt precies de totale kosten. Het heet ook "
                  "de <strong>kritische hoeveelheid</strong>."),
            ("p", "Je vindt het met de <strong>marge</strong>: het verschil tussen de <strong>prijs en de "
                  "variabele kost per stuk</strong>. Elk verkocht stuk levert die marge op om de constante "
                  "kosten te dekken. Een bedrijf met 4 000 euro constante kosten, een prijs van 20 euro en een "
                  "variabele kost van 12 euro heeft een marge van 8 euro per stuk, en moet dus "
                  "<strong>500 stuks</strong> verkopen om break-even te draaien."),
            ("p", "Verkoopt een bedrijf <strong>boven</strong> zijn break-evenpunt, dan weet je twee dingen: de "
                  "constante kosten zijn <strong>gedekt</strong> en elk extra stuk voegt zijn volle "
                  "<strong>marge</strong> aan de winst toe."),
        ]),
        dict(kop="Winst en verlies in beeld", blokken=[
            ("p", "In een grafiek met de prijs, de GK-curve en de hoeveelheid lees je de winst zo af: neem het "
                  "<strong>verschil tussen de prijs en GK</strong> bij de gekozen hoeveelheid en "
                  "<strong>vermenigvuldig het met die hoeveelheid</strong>. Dat is de oppervlakte van een "
                  "rechthoek. Een bedrijf dat 2 000 stuks maakt bij een prijs van 15 euro en een GK van "
                  "13 euro, maakt dus <strong>4 000 euro</strong> winst."),
            ("p", "Ligt de <strong>prijs boven GK</strong>, dan is er winst; ligt ze <strong>eronder</strong>, "
                  "dan verlies; vallen ze samen, dan is de winst nul. Een bedrijf kan dus in zijn optimum "
                  "<strong>toch verlies maken</strong>: MK = MO zegt alleen dat het <strong>zo weinig mogelijk "
                  "verliest</strong>, niet dat het winst maakt. Een bedrijf dat zijn <strong>omzet "
                  "verdubbelt</strong>, verdubbelt zijn winst dus niet automatisch: de kosten stijgen mee."),
        ]),
        dict(kop="Doorgaan of sluiten", blokken=[
            ("p", "Een bedrijf met verlies blijft op <strong>korte termijn</strong> soms toch produceren, en dat "
                  "is verstandig zolang de <strong>prijs boven de gemiddelde variabele kost</strong> ligt. Dan "
                  "dekt elke verkoop zijn eigen variabele kost én een stuk van de constante kosten, die toch "
                  "doorlopen. Sluiten zou <strong>meer</strong> verlies geven."),
            ("p", "Het punt waar de <strong>prijs gelijk is aan de laagste gemiddelde variabele kost</strong> "
                  "heet daarom het <strong>sluitingspunt op korte termijn</strong>. Zakt de prijs "
                  "<strong>daaronder</strong>, dan brengt elk stuk minder op dan het aan grondstof en energie "
                  "kost, en is <strong>stoppen</strong> het beste."),
            ("p", "Een bedrijf dat aan 9 euro verkoopt met een GVK van 7 euro en een GK van 11 euro, maakt "
                  "<strong>verlies</strong> maar <strong>blijft op korte termijn produceren</strong>: 9 ligt "
                  "boven 7. Op <strong>lange termijn</strong> stopt het beter als de prijs onder de "
                  "<strong>gemiddelde kost</strong> blijft liggen, want dan worden de constante kosten nooit "
                  "gedekt. Een restaurant dat 's winters met verlies open blijft, doet dat dus terecht zolang de "
                  "opbrengst de <strong>variabele</strong> kosten dekt — en zolang het in de zomer het verschil "
                  "ophaalt."),
            ("weetje", "Valt er in een markt met volkomen concurrentie <strong>winst</strong> te halen, dan "
                       "<strong>treden er nieuwe bedrijven toe</strong>. Het aanbod stijgt, de prijs zakt, en de "
                       "winst slinkt tot ze net nul is. Daarom blijft overwinst in zo'n markt niet duren."),
            ("p", "Op basis van deze theorie neemt een bedrijf drie soorten beslissingen: "
                  "<strong>hoeveel</strong> het produceert, <strong>of</strong> het bij een gegeven prijs nog "
                  "produceert, en <strong>wanneer</strong> het beter stopt."),
        ]),
    ],
    onthoud=[
        "De winst is maximaal waar MK = MO; dat is de optimale productiegrootte.",
        "MO > MK: meer produceren. MK > MO: minder produceren.",
        "Alleen het snijpunt in het stijgende deel van MK telt; die stijgende tak is de aanbodcurve van het bedrijf.",
        "Met een tabel van TO en TK vind je het optimum waar TO − TK het grootst is.",
        "Het break-evenpunt is de hoeveelheid met winst nul: constante kosten gedeeld door (prijs − variabele kost per stuk).",
        "Winst = (prijs − GK) × hoeveelheid. In het optimum kan er toch verlies zijn.",
        "Korte termijn: doorgaan zolang de prijs boven de gemiddelde variabele kost ligt.",
        "Lange termijn: stoppen als de prijs onder de gemiddelde kost blijft liggen.",
    ])


# ───────────────────────── 10. De markt met volkomen concurrentie en de overheid
zet("de-markt-met-volkomen-concurrentie-en-de-overheid",
    titel="De markt met volkomen concurrentie en de overheid",
    onder="Hoe vraag en aanbod samen een prijs maken, en wat een maximum- of minimumprijs daarmee doet.",
    secties=[
        dict(kop="Vraag, aanbod en het evenwicht", blokken=[
            ("p", "De <strong>vraagcurve daalt</strong>: bij een <strong>hogere prijs</strong> willen "
                  "consumenten <strong>minder</strong> kopen. De <strong>aanbodcurve stijgt</strong>: bij een "
                  "hogere prijs willen producenten <strong>meer</strong> aanbieden, want het wordt interessanter "
                  "om te produceren."),
            ("fig", svg.marktevenwicht(), "Het marktevenwicht is het snijpunt van de vraag- en de aanbodcurve."),
            ("p", "Het <strong>marktevenwicht</strong> is de toestand waarin <strong>de gevraagde en de "
                  "aangeboden hoeveelheid gelijk</strong> zijn. In de grafiek vind je het in het "
                  "<strong>snijpunt</strong> van de twee curven. De prijs daar heet de "
                  "<strong>evenwichtsprijs</strong>, de hoeveelheid de evenwichtshoeveelheid."),
            ("kader", "Rekenen met functies doe je door ze <strong>aan elkaar gelijk te stellen</strong>. Met "
                      "Qv = 200 &minus; 4P en Qa = 20 + 2P: 200 &minus; 4P = 20 + 2P geeft 180 = 6P, dus "
                      "<strong>P = 30</strong>. Vul dat in één van de twee functies in: Qa = 20 + 60 = "
                      "<strong>80</strong>. Dat is de evenwichtshoeveelheid. En één functie invullen kan ook "
                      "los: Qv = 120 &minus; 2P bij P = 25 geeft <strong>70</strong>, en Qa = 10 + 5P bij "
                      "P = 8 geeft <strong>50</strong>."),
            ("p", "Ligt de prijs <strong>boven</strong> het evenwicht, dan is er een <strong>overschot</strong>: "
                  "er wordt meer aangeboden dan gevraagd, en de prijs zakt. Ligt de prijs "
                  "<strong>onder</strong> het evenwicht, dan is er een <strong>tekort</strong>: de vraag is groter "
                  "dan het aanbod, en de prijs <strong>stijgt</strong>. Een tekort duwt de prijs dus "
                  "<strong>omhoog</strong>, niet omlaag."),
            ("p", "Daarom noemt men het marktmechanisme <strong>zelfregulerend</strong>: de prijs beweegt "
                  "<strong>zelf</strong> naar het evenwicht, zonder dat iemand ze oplegt. Maar het evenwicht is "
                  "<strong>geen vast punt voor altijd</strong>: zodra het inkomen, de smaak, de kosten of het "
                  "aantal aanbieders verandert, verschuift een curve en ligt het evenwicht elders."),
        ]),
        dict(kop="Langs de curve of de curve zelf", blokken=[
            ("p", "Hier moet je scherp zijn. Een <strong>prijsverandering</strong> doet je "
                  "<strong>langs</strong> de curve bewegen; ze <strong>verschuift de curve niet</strong>. Alleen "
                  "iets <strong>anders</strong> dan de prijs van het goed zelf verschuift een hele curve."),
            ("kader", tabel(["wat de vraagcurve verschuift", "wat de aanbodcurve verschuift"],
                            [["het inkomen van de gezinnen", "de prijs van de grondstoffen"],
                             ["de smaak en de mode", "de techniek en de productiviteit"],
                             ["de prijs van een vervangend goed", "het aantal aanbieders"],
                             ["het aantal consumenten", "belastingen en subsidies"]])),
            ("p", "Stijgt het <strong>inkomen</strong> van de gezinnen, dan schuift de vraagcurve bij een gewoon "
                  "goed naar <strong>rechts</strong>: de prijs <strong>en</strong> de hoeveelheid stijgen beide. "
                  "Worden de <strong>grondstoffen duurder</strong>, dan schuift de aanbodcurve naar "
                  "<strong>links</strong>: de prijs stijgt en de hoeveelheid daalt."),
            ("fig", svg.marktevenwicht(verschuiving="vraag rechts"),
                    "De vraagcurve schuift naar rechts; het evenwicht verschuift mee."),
            ("p", "Een <strong>hittegolf</strong> doet de vraag naar ijs stijgen. Het gevolg: de vraagcurve "
                  "schuift naar rechts, de <strong>prijs stijgt</strong> en de <strong>verkochte hoeveelheid "
                  "stijgt</strong> ook. Het is dus niet zo dat één van de twee gelijk blijft."),
        ]),
        dict(kop="Wat volkomen concurrentie betekent", blokken=[
            ("p", "<strong>Volkomen concurrentie</strong> is een markt met vier kenmerken: "
                  "<strong>veel kleine aanbieders en vragers</strong>, een <strong>homogeen product</strong>, "
                  "<strong>volledige informatie</strong> bij iedereen over prijs en kwaliteit, en "
                  "<strong>vrije toe- en uittreding</strong>."),
            ("p", "Een <strong>homogeen product</strong> is een product dat bij elke aanbieder "
                  "<strong>hetzelfde</strong> is, zodat het de koper niet uitmaakt bij wie hij koopt. Daardoor "
                  "is elke aanbieder een <strong>prijsnemer</strong>: hij <strong>moet de marktprijs "
                  "aanvaarden</strong> en kan zijn eigen prijs dus <strong>niet</strong> kiezen. Vraagt hij meer, "
                  "dan koopt niemand bij hem; vraagt hij minder, dan laat hij geld liggen."),
            ("p", "De markt die dit model het best benadert, is een markt voor "
                  "<strong>landbouwgrondstoffen</strong> zoals graan of aardappelen: duizenden aanbieders, een "
                  "product dat overal hetzelfde is, en een prijs die op de wereldmarkt tot stand komt. "
                  "Volkomen concurrentie blijft wel vooral een <strong>model</strong>: in de werkelijkheid zijn "
                  "producten bijna altijd een beetje verschillend en is de informatie nooit volledig. Het model "
                  "dient om te <strong>vergelijken</strong>, niet om de werkelijkheid te beschrijven."),
        ]),
        dict(kop="Maximum- en minimumprijzen", blokken=[
            ("p", "Een <strong>maximumprijs</strong> is een <strong>opgelegde bovengrens</strong>: de prijs mag "
                  "niet hoger. Een <strong>minimumprijs</strong> is een <strong>opgelegde ondergrens</strong>: de "
                  "prijs mag niet lager."),
            ("p", "Een maximumprijs werkt alleen <strong>onder</strong> de evenwichtsprijs. Dan is de prijs te "
                  "laag, wordt er <strong>meer gevraagd dan aangeboden</strong>, en ontstaat er een "
                  "<strong>tekort</strong>. Ligt de maximumprijs <strong>boven</strong> het evenwicht, dan "
                  "verandert er <strong>niets</strong>: de markt zat er al onder, en de grens knelt niet. Legt de "
                  "overheid bij een evenwicht van 10 euro een maximumprijs van <strong>7 euro</strong> op, dan "
                  "komt er dus een <strong>tekort</strong>."),
            ("p", "Zo'n tekort heeft gevolgen: <strong>wachtlijsten</strong>, <strong>rantsoenering</strong> en "
                  "een <strong>zwarte markt</strong> waar toch meer betaald wordt. En toch legt een overheid soms "
                  "een maximumprijs op, namelijk om een goed <strong>betaalbaar</strong> te houden voor wie het "
                  "nodig heeft, bijvoorbeeld bij huur, energie of geneesmiddelen."),
            ("p", "Een minimumprijs werkt omgekeerd: ze heeft alleen effect <strong>boven</strong> het evenwicht, "
                  "en dan ontstaat er een <strong>overschot</strong> en géén tekort. Een minimumprijs "
                  "<strong>onder</strong> de evenwichtsprijs verandert <strong>niets</strong>. Met het overschot "
                  "doet een overheid soms iets bijzonders: ze <strong>koopt het zelf op</strong> en slaat het op, "
                  "vernietigt het of voert het uit, zoals dat bij landbouwproducten gebeurd is."),
        ]),
    ],
    onthoud=[
        "De vraagcurve daalt, de aanbodcurve stijgt; hun snijpunt is het marktevenwicht.",
        "Boven het evenwicht: overschot, de prijs zakt. Onder het evenwicht: tekort, de prijs stijgt.",
        "Reken met functies door Qv en Qa aan elkaar gelijk te stellen.",
        "Een prijsverandering doet je langs de curve bewegen; alles behalve de prijs verschuift de curve.",
        "Volkomen concurrentie: veel kleine partijen, een homogeen product, volledige informatie, vrije toetreding.",
        "Een prijsnemer moet de marktprijs aanvaarden.",
        "Een maximumprijs werkt alleen onder het evenwicht en geeft een tekort.",
        "Een minimumprijs werkt alleen boven het evenwicht en geeft een overschot.",
    ])


# ───────────────────────── 11. De arbeidsmarkt en de collectieve afspraken
zet("de-arbeidsmarkt-en-de-collectieve-afspraken",
    titel="De arbeidsmarkt en de collectieve afspraken",
    onder="Wie op deze markt vraagt en wie aanbiedt, en wat er verandert als er samen onderhandeld wordt.",
    secties=[
        dict(kop="Vraag en aanbod van arbeid", blokken=[
            ("p", "Op de arbeidsmarkt staan de rollen <strong>omgekeerd</strong> ten opzichte van een gewone "
                  "markt. De <strong>bedrijven vragen</strong> arbeid, de <strong>gezinnen bieden</strong> ze "
                  "aan. De prijs op deze markt is het <strong>loon</strong>."),
            ("p", "De <strong>vraag naar arbeid daalt</strong> als het loon stijgt: arbeid wordt dan duurder en "
                  "een bedrijf neemt minder mensen aan. Het <strong>aanbod van arbeid stijgt</strong> als het "
                  "loon stijgt: werken wordt aantrekkelijker. Waar de twee elkaar kruisen, ligt het "
                  "<strong>evenwichtsloon</strong>."),
            ("kader", "Rekenen gaat zoals op elke markt. Met Qv = 1 000 &minus; 20W en Qa = 400 + 10W: "
                      "1 000 &minus; 20W = 400 + 10W geeft 600 = 30W, dus <strong>W = 20</strong>. Vul in: "
                      "Qa = 400 + 200 = <strong>600</strong> eenheden arbeid."),
            ("p", "De vraag naar arbeid is een <strong>afgeleide vraag</strong>: een bedrijf vraagt arbeid niet "
                  "voor zichzelf, maar omdat het <strong>goederen en diensten wil verkopen</strong>. Loopt de "
                  "verkoop terug, dan daalt de vraag naar arbeid mee, hoe laag het loon ook is."),
        ]),
        dict(kop="Wat de curven verschuift", blokken=[
            ("kader", tabel(["de vraag naar arbeid verschuift door", "het aanbod van arbeid verschuift door"],
                            [["de verkoop op de goederenmarkt", "de omvang van de bevolking"],
                             ["nieuwe technologie en machines", "de vergrijzing"],
                             ["de loonkosten en de bijdragen", "migratie"],
                             ["de productiviteit", "de pensioenleeftijd en de studieduur"]])),
            ("p", "<strong>Vergrijzing</strong> doet het <strong>aanbod van arbeid dalen</strong>: er gaan meer "
                  "mensen op pensioen dan er jongeren bijkomen. <strong>Migratie</strong> kan het aanbod juist "
                  "doen <strong>stijgen</strong>. <strong>Technologie</strong> werkt op de vraag: machines kunnen "
                  "werk overnemen, maar ze maken ook nieuwe soorten werk."),
            ("p", "Blijft er in een beroep een <strong>tekort</strong> bestaan omdat er te weinig geschoolde "
                  "mensen zijn, dan heet dat een <strong>knelpuntberoep</strong>. De vraag is daar groter dan het "
                  "aanbod, en het loon alleen lost dat niet op: er moeten eerst mensen opgeleid worden."),
        ]),
        dict(kop="Collectieve afspraken", blokken=[
            ("p", "Op de arbeidsmarkt onderhandelt niet iedereen voor zichzelf. Een <strong>cao</strong>, een "
                  "<strong>collectieve arbeidsovereenkomst</strong>, is een akkoord over <strong>loon en "
                  "arbeidsvoorwaarden</strong> tussen <strong>werkgevers en werknemers</strong>. Ze geldt voor een "
                  "hele sector of een heel bedrijf, en niet voor één persoon."),
            ("p", "Het <strong>interprofessioneel akkoord</strong> of <strong>ipa</strong> gaat nog breder: het "
                  "is een akkoord <strong>over alle sectoren heen</strong>, dat de grote lijnen voor twee jaar "
                  "vastlegt. De partijen die dat allemaal onderhandelen, heten de <strong>sociale "
                  "partners</strong>: de <strong>vakbonden</strong> aan de ene kant en de "
                  "<strong>werkgeversorganisaties</strong> aan de andere."),
            ("p", "Het <strong>minimumloon</strong> is een ondergrens: lager mag een loon niet. Het bestaat om "
                  "te vermijden dat mensen <strong>werken en toch niet rondkomen</strong>, en omdat "
                  "<strong>één werknemer zwak staat</strong> tegenover een werkgever. Daarom onderhandelen ze "
                  "samen: met duizenden achter zich weegt een vakbond even zwaar als de werkgever."),
            ("p", "Al die afspraken doen één ding met het marktmechanisme: ze <strong>leggen het loon deels "
                  "vast</strong>, zodat het niet meer vrij door vraag en aanbod beweegt. Ligt een minimumloon "
                  "<strong>boven</strong> het evenwichtsloon, dan ontstaat er net als bij elke minimumprijs een "
                  "<strong>overschot</strong> aan arbeid: werkloosheid in dat segment."),
            ("p", "<strong>Indexering</strong> is de automatische aanpassing van de lonen aan de prijzen. Ze "
                  "beschermt de koopkracht, maar voor de bedrijven betekent ze dat de "
                  "<strong>loonkosten stijgen</strong>, wat hun vraag naar arbeid kan drukken. Stijgt de "
                  "<strong>productiviteit</strong> mee, dan is er ruimte: de lonen kunnen dan stijgen "
                  "<strong>zonder hogere kost per stuk</strong>."),
            ("weetje", "Arbeid is geen gewoon product: je kan het <strong>niet opslaan</strong> en er zitten "
                       "<strong>mensen</strong> achter. Een dag die niemand gewerkt heeft, is weg. Daarom is deze "
                       "markt zwaarder gereglementeerd dan de markt voor aardappelen."),
        ]),
    ],
    onthoud=[
        "Op de arbeidsmarkt vragen de bedrijven en bieden de gezinnen aan; de prijs is het loon.",
        "De vraag naar arbeid daalt bij een hoger loon, het aanbod stijgt; het snijpunt is het evenwichtsloon.",
        "De vraag naar arbeid is een afgeleide vraag: ze volgt uit de verkoop van goederen en diensten.",
        "Vergrijzing verkleint het arbeidsaanbod, migratie kan het vergroten.",
        "Een knelpuntberoep is een beroep met een blijvend tekort aan geschoolde mensen.",
        "Een cao regelt loon en arbeidsvoorwaarden voor een sector of een bedrijf; een ipa gaat over alle sectoren.",
        "De sociale partners zijn de vakbonden en de werkgeversorganisaties.",
        "Een minimumloon boven het evenwichtsloon geeft een overschot aan arbeid.",
        "Indexering verhoogt de loonkosten; stijgende productiviteit maakt ruimte voor hogere lonen.",
    ])


# ───────────────────────── 12. Internationale handel en handelsbelemmeringen
zet("internationale-handel-en-handelsbelemmeringen",
    titel="Internationale handel en handelsbelemmeringen",
    onder="Invoer, uitvoer en de vier manieren waarop een land handel moeilijker maakt.",
    secties=[
        dict(kop="Invoer, uitvoer en de Europese Unie", blokken=[
            ("p", "<strong>Invoer</strong> of import zijn de <strong>aankopen in het buitenland</strong>; "
                  "<strong>uitvoer</strong> of export zijn de <strong>verkopen aan het buitenland</strong>. Bij "
                  "invoer gaat er geld naar buiten, bij uitvoer komt er geld binnen."),
            ("p", "Binnen de <strong>Europese Unie</strong> gebruikt men die woorden niet. Een "
                  "<strong>aankoop</strong> bij een leverancier in een ander EU-land is een "
                  "<strong>intracommunautaire verwerving</strong>; een <strong>verkoop</strong> aan een klant in "
                  "een ander EU-land is een <strong>intracommunautaire levering</strong>. Kaas kopen in Nederland "
                  "is dus een verwerving, machines verkopen aan Duitsland een levering, en een aankoop in Spanje "
                  "heet <strong>geen</strong> invoer. Verkopen aan de Verenigde Staten is wél uitvoer, want die "
                  "liggen buiten de Unie."),
        ]),
        dict(kop="Waarom landen handel drijven", blokken=[
            ("p", "De <strong>motieven</strong> voor internationale handel zijn er drie. Eén: een land heeft "
                  "bepaalde <strong>grondstoffen niet</strong>. <strong>Cacao</strong> groeit hier niet, dus "
                  "voeren we de bonen in en verwerken ze tot chocolade, die weer uitgevoerd wordt. Twee: een "
                  "<strong>groter afzetgebied</strong> betekent meer verkoop, grotere reeksen en een lagere kost "
                  "per stuk. Drie: er zijn <strong>verschillen in loonkosten en in techniek</strong>, waardoor "
                  "iets elders goedkoper te maken is."),
            ("p", "Daar zit het idee van <strong>specialisatie</strong> achter: <strong>elk land doet waar het "
                  "best in is</strong> en koopt de rest aan. Samen is er dan meer te verdelen dan wanneer elk "
                  "land alles zelf probeert te maken. Voor een bedrijf levert uitvoeren bovendien "
                  "<strong>meer klanten</strong>, <strong>schaalvoordelen</strong> en <strong>minder "
                  "afhankelijkheid van één markt</strong> op — concurrentie verdwijnt er niet door."),
        ]),
        dict(kop="Cijfers over de Belgische handel", blokken=[
            ("p", "De <strong>handelsbalans</strong> is de <strong>uitvoer min de invoer</strong>. Is ze "
                  "positief, dan spreekt men van een <strong>overschot</strong>; is ze negatief, van een "
                  "<strong>tekort</strong>. Een land dat voor 320 miljard euro uitvoerde en voor 290 miljard "
                  "invoerde, heeft een <strong>overschot van 30 miljard euro</strong>. Een tekort betekent "
                  "<strong>meer invoer dan uitvoer</strong>."),
            ("p", "België is een <strong>kleine open economie</strong>: de uitvoer is erg groot in verhouding "
                  "tot het bbp, en de binnenlandse markt is klein. Het <strong>grootste deel</strong> van onze "
                  "handel loopt met de <strong>Europese Unie</strong>, en vooral met de buurlanden "
                  "<strong>Duitsland, Nederland en Frankrijk</strong>: afstand speelt een grote rol. De grootste "
                  "uitvoergroep is de <strong>chemie en de farmacie</strong>, daarna komen onder meer "
                  "voertuigen en machines."),
            ("p", "Uit een tabel met de invoer en de uitvoer per jaar lees je de "
                  "<strong>handelsbalans per jaar</strong>, de <strong>groei</strong> van elke reeks en de "
                  "<strong>vergelijking</strong> tussen beide. Over de winst van een afzonderlijk bedrijf zegt "
                  "ze niets. En reken een groeivoet altijd op het <strong>oude</strong> cijfer: van 200 naar 210 "
                  "miljard is 10 op 200, dus <strong>5 %</strong>."),
        ]),
        dict(kop="De vier handelsbelemmeringen", blokken=[
            ("p", "Een land kan handel op vier manieren moeilijker maken:"),
            ("kader", tabel(["belemmering", "wat ze doet", "waarop ze werkt"],
                            [["<strong>invoerquotum</strong>", "een maximum op de ingevoerde hoeveelheid", "de hoeveelheid"],
                             ["<strong>importheffing</strong>", "een belasting op invoer", "de prijs"],
                             ["<strong>uitvoersubsidie</strong>", "steun van de overheid bij uitvoer", "de prijs"],
                             ["<strong>niet-tarifaire belemmering</strong>", "normen, keuringen, labels, papierwerk", "de regels"]])),
            ("p", "Een <strong>importheffing</strong> maakt het ingevoerde goed <strong>duurder</strong> op de "
                  "binnenlandse markt: het aanbod schuift naar boven, de <strong>prijs stijgt</strong> en de "
                  "ingevoerde hoeveelheid daalt. Een toestel van 100 euro met 15 % heffing kost de koper dus "
                  "<strong>115 euro</strong>. Een <strong>invoerquotum</strong> werkt op de "
                  "<strong>hoeveelheid</strong> en niet op de prijs: het snijdt een stuk van het aanbod weg, "
                  "waardoor de <strong>prijs stijgt</strong>, het <strong>aanbod kleiner</strong> wordt en de "
                  "<strong>binnenlandse producenten meer verkopen</strong>."),
            ("fig", svg.marktevenwicht(verschuiving="aanbod links"),
                    "Een belemmering duwt het aanbod naar links: de prijs stijgt, de hoeveelheid daalt."),
            ("p", "Een <strong>uitvoersubsidie</strong> helpt een binnenlands bedrijf om in het buitenland te "
                  "verkopen: de overheid legt geld bij, dus kan het een lagere prijs vragen dan de buitenlandse "
                  "concurrent. Een <strong>niet-tarifaire belemmering</strong> gebruikt geen geld en geen "
                  "hoeveelheid, maar <strong>regels</strong>: strenge technische normen, keuringen aan de grens, "
                  "labels, papierwerk."),
            ("p", "Wie <strong>wint</strong> erbij? De <strong>binnenlandse producent</strong> (minder "
                  "concurrentie), zijn <strong>personeel</strong> (werk) en bij een heffing ook de "
                  "<strong>overheid</strong> (inkomsten). Wie <strong>verliest</strong>? De "
                  "<strong>consument</strong>, die meer betaalt en minder keuze heeft. Handelsbelemmeringen zijn "
                  "dus <strong>niet</strong> goed voor de consument in het eigen land. Een land legt ze toch op "
                  "om <strong>eigen bedrijven en jobs te beschermen</strong>, of om inkomsten te halen."),
        ]),
        dict(kop="Het handelsakkoord", blokken=[
            ("p", "Een <strong>handelsakkoord</strong> is een <strong>afspraak tussen landen</strong> om "
                  "belemmeringen te verlagen of weg te nemen: <strong>lagere invoerheffingen</strong>, "
                  "<strong>dezelfde normen</strong> zodat één keuring volstaat, en <strong>ruimere of "
                  "afgeschafte quota</strong>."),
            ("p", "Het effect op de markt is het <strong>omgekeerde</strong> van een belemmering: zonder heffing "
                  "schuift het aanbod naar beneden, de <strong>invoer wordt goedkoper</strong> en de ingevoerde "
                  "hoeveelheid stijgt. De consument wint, de binnenlandse producent krijgt meer concurrentie."),
        ]),
    ],
    onthoud=[
        "Invoer is aankopen in het buitenland, uitvoer verkopen aan het buitenland.",
        "Binnen de EU: intracommunautaire verwerving (aankoop) en levering (verkoop).",
        "Motieven voor handel: ontbrekende grondstoffen, een groter afzetgebied, verschillen in kosten.",
        "Handelsbalans = uitvoer − invoer; positief is een overschot, negatief een tekort.",
        "België is een kleine open economie; de meeste handel loopt met de EU-buurlanden, en chemie en farmacie is de grootste uitvoergroep.",
        "Vier belemmeringen: invoerquotum (hoeveelheid), importheffing (prijs), uitvoersubsidie (prijs), niet-tarifaire belemmering (regels).",
        "Een belemmering verhoogt de prijs en verlaagt de ingevoerde hoeveelheid; de consument betaalt ze.",
        "Een handelsakkoord doet het omgekeerde: goedkopere invoer en meer concurrentie.",
    ])


# ───────────────────────── 13. Ondernemingsvormen en aansprakelijkheid
zet("ondernemingsvormen-en-aansprakelijkheid",
    titel="Ondernemingsvormen en aansprakelijkheid",
    onder="Eenmanszaak, bv en nv naast elkaar, op de zeven punten die een starter moet afwegen.",
    secties=[
        dict(kop="Natuurlijk persoon of rechtspersoon", blokken=[
            ("p", "Een <strong>natuurlijk persoon</strong> is een <strong>mens</strong> van vlees en bloed. Een "
                  "<strong>rechtspersoon</strong> is een constructie die het recht als persoon behandelt: een "
                  "<strong>vennootschap</strong> kan zelf eigendom hebben, zelf een contract ondertekenen en "
                  "zelf schulden maken. Het gebouw en de rekening van een bv zijn van de bv, "
                  "<strong>niet</strong> van de aandeelhouders."),
            ("p", "Een <strong>eenmanszaak</strong> is <strong>geen</strong> rechtspersoon: daar handelt een "
                  "<strong>natuurlijk persoon</strong> in eigen naam. Een bv, een nv en een cv zijn wel "
                  "rechtspersonen."),
        ]),
        dict(kop="Beperkte en onbeperkte aansprakelijkheid", blokken=[
            ("p", "Bij <strong>onbeperkte aansprakelijkheid</strong> sta je ook met je "
                  "<strong>privévermogen</strong> in voor de schulden van de zaak. Dat is de regel bij een "
                  "eenmanszaak: het vermogen van de zaak en het privévermogen zijn er "
                  "<strong>niet gescheiden</strong>. Heeft een bakker met een eenmanszaak 40 000 euro schulden "
                  "en zit er nog 15 000 euro in de zaak, dan kunnen de schuldeisers voor de rest "
                  "<strong>ook aan zijn privévermogen</strong>."),
            ("p", "Bij <strong>beperkte aansprakelijkheid</strong> <strong>verlies je enkel je inbreng</strong>. "
                  "Dat geldt bij een bv en een nv: de <strong>vennootschap zelf</strong> betaalt haar schulden "
                  "met haar eigen vermogen, en een aandeelhouder kan niet meer kwijtspelen dan wat hij "
                  "ingebracht heeft."),
        ]),
        dict(kop="De eenmanszaak", blokken=[
            ("p", "Een eenmanszaak start <strong>snel en eenvoudig</strong>: "
                  "<strong>geen notariële akte</strong>, <strong>geen minimumkapitaal</strong>, "
                  "<strong>één oprichter</strong>, en voor een kleine zaak volstaat een vereenvoudigde "
                  "boekhouding. Aandelen bestaan er niet, want er is geen vennootschap. De winst is een inkomen "
                  "van de eigenaar en gaat dus in de <strong>personenbelasting</strong>."),
            ("p", "De prijs daarvoor is de <strong>onbeperkte aansprakelijkheid</strong>. Wie vooral "
                  "<strong>weinig administratie</strong> wil en alleen begint, kiest meestal deze vorm."),
        ]),
        dict(kop="De bv en de nv naast elkaar", blokken=[
            ("kader", tabel(["punt", "eenmanszaak", "bv", "nv"],
                            [["oprichtingsakte", "geen", "notarieel", "notarieel"],
                             ["minimumkapitaal", "geen", "geen vast bedrag", "61 500 euro"],
                             ["aantal oprichters", "1", "1", "1"],
                             ["aansprakelijkheid", "onbeperkt", "beperkt", "beperkt"],
                             ["boekhouding", "vereenvoudigd mogelijk", "dubbel", "dubbel"],
                             ["aandelen", "bestaan niet", "besloten", "vrij overdraagbaar"],
                             ["fiscaliteit", "personenbelasting", "vennootschapsbelasting", "vennootschapsbelasting"]])),
            ("p", "Een <strong>bv</strong> heeft <strong>geen vast minimumkapitaal</strong> meer. Ze moet wel "
                  "een <strong>toereikend aanvangsvermogen</strong> hebben — genoeg startgeld voor wat ze van "
                  "plan is — en de oprichters verantwoorden dat in een <strong>financieel plan</strong>. Bij de "
                  "oprichting horen dus drie dingen klaar te zijn: het financieel plan, de "
                  "<strong>notariële akte</strong> — ook <strong>authentieke</strong> akte genoemd — en genoeg "
                  "aanvangsvermogen."),
            ("p", "Een <strong>nv</strong> heeft wel een minimumkapitaal: <strong>61 500 euro</strong>, volledig "
                  "volstort. Bij beide volstaat <strong>één</strong> oprichter."),
            ("p", "Het grote verschil zit in de <strong>aandelen</strong>. Een bv heeft een "
                  "<strong>besloten karakter</strong>: de <strong>aandelen gaan niet vrij over</strong>, want "
                  "voor een overdracht is in principe de toestemming van de andere aandeelhouders nodig. Bij een "
                  "<strong>nv</strong> zijn de aandelen <strong>vrij overdraagbaar</strong>."),
            ("p", "Daarom past een <strong>bv</strong> bij vier vrienden die niet willen dat er een onbekende "
                  "bij komt, en een <strong>nv</strong> bij een bedrijf dat met veel of wisselende "
                  "aandeelhouders werkt. Een <strong>beursgenoteerd</strong> bedrijf is daarom bijna altijd een "
                  "nv: op de beurs moeten aandelen van hand tot hand kunnen gaan."),
        ]),
        dict(kop="Waarom het uitmaakt", blokken=[
            ("p", "De voordelen van een vennootschap zijn de <strong>beperkte aansprakelijkheid</strong>, het "
                  "<strong>makkelijker ophalen van geld</strong> bij nieuwe aandeelhouders, en het feit dat ze "
                  "<strong>blijft bestaan</strong> als een oprichter wegvalt. Het nadeel is "
                  "<strong>meer administratie</strong>: een notaris, een dubbele boekhouding en elk jaar de "
                  "jaarrekening neerleggen."),
            ("p", "Je vergelijkt ondernemingsvormen dus altijd op dezelfde punten: "
                  "<strong>aansprakelijkheid</strong>, <strong>administratie</strong> en "
                  "<strong>fiscaliteit</strong>, met daarnaast kapitaal, aantal oprichters en de overdracht van "
                  "de aandelen. Hoeveel klanten je hebt, hangt niet van de vorm af."),
        ]),
    ],
    onthoud=[
        "Een natuurlijk persoon is een mens; een rechtspersoon is een vennootschap met een eigen vermogen.",
        "Een eenmanszaak is geen rechtspersoon: één vermogen, en onbeperkte aansprakelijkheid.",
        "Beperkte aansprakelijkheid betekent dat je enkel je inbreng kan verliezen.",
        "Eenmanszaak: geen akte, geen kapitaal, vereenvoudigde boekhouding, personenbelasting.",
        "Bv: notariële akte, geen vast kapitaal maar een toereikend aanvangsvermogen met financieel plan, besloten aandelen.",
        "Nv: notariële akte, 61 500 euro kapitaal, vrij overdraagbare aandelen.",
        "Bij bv en nv volstaat één oprichter, en beide betalen vennootschapsbelasting met een dubbele boekhouding.",
        "Vergelijk altijd op aansprakelijkheid, administratie en fiscaliteit.",
    ])


# ───────────────────────── 14. De balans en de resultatenrekening
zet("de-balans-en-de-resultatenrekening",
    titel="De balans en de resultatenrekening",
    onder="Een foto van één dag naast de film van een heel jaar.",
    secties=[
        dict(kop="De balans: actief en passief", blokken=[
            ("p", "Een <strong>balans</strong> is een <strong>foto op één bepaalde dag</strong>, meestal "
                  "31 december. Links staat het <strong>actief</strong>: alles wat de onderneming "
                  "<strong>bezit</strong>. Rechts staat het <strong>passief</strong>: de "
                  "<strong>financiering</strong>, dus waar het geld vandaan komt."),
            ("fig", svg.balansschema(
                ["Vaste activa", "- immaterieel (software)", "- materieel (gebouw, machine)",
                 "- financieel", "Vlottende activa", "- voorraden", "- handelsvorderingen",
                 "- liquide middelen"],
                ["Eigen vermogen", "- kapitaal", "- reserves", "- overgedragen resultaat",
                 "Schulden > 1 jaar", "- lening op lange termijn", "Schulden ≤ 1 jaar",
                 "- leveranciers, btw, lonen"]),
                    "De twee kanten van een balans, met hun onderverdelingen."),
            ("p", "Het <strong>totaal van het actief is altijd gelijk aan het totaal van het passief</strong>. "
                  "Dat komt niet van een afspraak maar van de logica: achter <strong>elk bezit zit een "
                  "bron</strong> — eigen inbreng, winst of schuld. Daarom heet het een balans."),
            ("kader", "Daaruit volgen twee rekenregels: <strong>actief = eigen vermogen + schulden</strong>, en "
                      "dus <strong>eigen vermogen = actief &minus; schulden</strong>. Met 150 000 euro actief en "
                      "60 000 euro eigen vermogen zijn er <strong>90 000 euro</strong> schulden; met 200 000 euro "
                      "actief en 120 000 euro schulden is het eigen vermogen <strong>80 000 euro</strong>."),
        ]),
        dict(kop="Wat waar staat", blokken=[
            ("p", "<strong>Vaste activa</strong> blijven <strong>langer dan een jaar</strong> in de onderneming: "
                  "een gebouw, een machine, een bestelwagen. Een <strong>immaterieel</strong> vast actief kan je "
                  "niet aanraken en is toch jaren bruikbaar, zoals een <strong>softwarelicentie</strong> of een "
                  "octrooi. <strong>Vlottende activa</strong> veranderen snel: de <strong>voorraad</strong>, de "
                  "<strong>handelsvorderingen</strong> (geld dat een klant nog moet betalen) en de "
                  "<strong>liquide middelen</strong> (geld in kas en op de bank). Een machine hoort dus "
                  "<strong>niet</strong> bij de vlottende activa."),
            ("p", "Aan de passiefzijde staan het <strong>eigen vermogen</strong> — wat de eigenaars inbrachten "
                  "plus de winst die in de zaak gebleven is, en wat niet terugbetaald moet worden — en de "
                  "<strong>schulden</strong>, opgesplitst volgens <strong>looptijd</strong>. Een lening op tien "
                  "jaar staat bij de schulden op <strong>meer dan één jaar</strong>; te betalen "
                  "<strong>leveranciers, btw en lonen</strong> bij de schulden op <strong>ten hoogste één "
                  "jaar</strong>. Het <strong>kapitaal</strong> is dus geen bezit maar financiering: het staat "
                  "<strong>rechts</strong>."),
        ]),
        dict(kop="De resultatenrekening", blokken=[
            ("p", "De <strong>resultatenrekening</strong> zet de <strong>kosten en de opbrengsten</strong> van "
                  "een <strong>hele periode</strong> naast elkaar, meestal een boekjaar. Ze geldt dus "
                  "<strong>niet</strong> voor één dag; dat is net de balans. Samen vormen de twee de "
                  "jaarrekening."),
            ("p", "Ze werkt in <strong>stappen</strong>:"),
            ("kader", tabel(["stap", "hoe je ze berekent"],
                            [["<strong>bedrijfsresultaat</strong>", "bedrijfsopbrengsten &minus; bedrijfskosten"],
                             ["<strong>financieel resultaat</strong>", "financiële opbrengsten &minus; financiële kosten"],
                             ["<strong>resultaat voor belastingen</strong>", "de twee vorige samen"],
                             ["<strong>resultaat van het boekjaar</strong>", "resultaat voor belastingen &minus; de belastingen"]])),
            ("p", "<strong>Bedrijfsopbrengsten en -kosten</strong> komen uit de gewone werking: de "
                  "<strong>omzet</strong> is een bedrijfsopbrengst, en de aankoop van handelsgoederen, de "
                  "<strong>lonen</strong> en de <strong>afschrijvingen</strong> zijn bedrijfskosten. Alles wat "
                  "met <strong>lenen en beleggen</strong> te maken heeft, hoort bij het financieel resultaat: de "
                  "intrest die je <strong>betaalt</strong>, de intrest die je <strong>ontvangt</strong>, een "
                  "ontvangen dividend. Intrest op een lening is dus <strong>geen</strong> bedrijfskost."),
            ("kader", "Rekenen met de stappen: 500 000 euro bedrijfsopbrengsten en 440 000 euro bedrijfskosten "
                      "geven een bedrijfsresultaat van <strong>60 000 euro winst</strong>. Met een financieel "
                      "resultaat van 10 000 euro negatief is het resultaat voor belastingen "
                      "<strong>50 000 euro</strong>. Daarvan 25 % belasting is 12 500 euro, dus blijft er "
                      "<strong>37 500 euro</strong> over."),
            ("p", "Een onderneming maakt <strong>verlies</strong> zodra de <strong>kosten hoger</strong> zijn "
                  "dan de opbrengsten. Een stijgende omzet met nog sneller stijgende kosten geeft dus nog altijd "
                  "verlies."),
        ]),
        dict(kop="Afschrijvingen en wat je eruit leest", blokken=[
            ("p", "Een <strong>afschrijving</strong> <strong>spreidt de kost</strong> van een machine "
                  "<strong>over de jaren</strong> waarin ze meegaat. Het is een <strong>kost</strong>, ook al "
                  "vertrekt er dat jaar <strong>geen geld</strong>: het geld ging eruit bij de aankoop. Zo staat "
                  "de kost in hetzelfde jaar als de opbrengst die ze helpt maken."),
            ("p", "Uit een resultatenrekening lees je of er <strong>winst</strong> gemaakt is, "
                  "<strong>waar de grootste kosten</strong> zitten en <strong>hoe zwaar de intresten</strong> "
                  "wegen. Hoeveel <strong>klanten</strong> er in de winkel kwamen, staat er niet in."),
            ("weetje", "In het <strong>MAR</strong>, het minimum algemeen rekeningstelsel, zijn de "
                       "<strong>kosten klasse 6</strong> en de <strong>opbrengsten klasse 7</strong>. Die twee "
                       "klassen vormen samen de resultatenrekening; de klassen 1 tot 5 vormen de balans."),
        ]),
    ],
    onthoud=[
        "De balans is een foto op één dag: links het actief (bezittingen), rechts het passief (financiering).",
        "Actief = eigen vermogen + schulden, dus eigen vermogen = actief − schulden.",
        "Vaste activa blijven langer dan een jaar; vlottende activa zijn voorraden, vorderingen en geld.",
        "Schulden staan op het passief, opgesplitst in meer en ten hoogste één jaar. Kapitaal staat ook rechts.",
        "De resultatenrekening gaat over een periode en werkt in stappen.",
        "Bedrijfsresultaat, dan financieel resultaat, samen het resultaat voor belastingen, en daarna na belastingen.",
        "Intrest is een financiële kost, geen bedrijfskost.",
        "Een afschrijving is een kost zonder dat er dat jaar geld vertrekt.",
        "In het MAR zijn de kosten klasse 6 en de opbrengsten klasse 7.",
    ])


# ───────────────────────── 15. Dubbel boekhouden
zet("dubbel-boekhouden-redeneerschema-journaal-en-grootboek",
    titel="Dubbel boekhouden: redeneerschema, journaal en grootboek",
    onder="Debet en credit, het redeneerschema in vier vragen, en waar een boeking daarna terechtkomt.",
    secties=[
        dict(kop="Debet en credit", blokken=[
            ("p", "<strong>Debet</strong> is de <strong>linkerkant</strong> van een rekening, "
                  "<strong>credit</strong> de <strong>rechterkant</strong>. Die twee woorden zeggen niets over "
                  "goed of slecht, en niets over schuld of bezit: ze duiden alleen een kant aan."),
            ("p", "In <strong>elke</strong> boeking is het <strong>totaal in het debet gelijk aan het totaal in "
                  "het credit</strong>. Klopt dat niet, dan zit er een fout in de boeking. Daarom heet het "
                  "<strong>dubbel</strong> boekhouden: <strong>elke verrichting raakt minstens twee "
                  "rekeningen</strong>, één links en één rechts, voor hetzelfde bedrag."),
            ("kader", tabel(["soort rekening", "stijgt", "daalt"],
                            [["actief", "<strong>debet</strong>", "credit"],
                             ["passief", "credit", "<strong>debet</strong>"],
                             ["kosten", "<strong>debet</strong>", "—"],
                             ["opbrengsten", "credit", "—"]])),
            ("p", "Een <strong>kost</strong> komt dus in het <strong>debet</strong> en een "
                  "<strong>opbrengst</strong> in het <strong>credit</strong>. Betaalt een klant zijn factuur, "
                  "dan <strong>daalt</strong> de vordering en komt ze in het <strong>credit</strong>; een nieuwe "
                  "schuld aan een leverancier <strong>stijgt</strong> en komt in het <strong>credit</strong>."),
        ]),
        dict(kop="Het redeneerschema", blokken=[
            ("p", "Het <strong>redeneerschema</strong> is de vaste reeks vragen die je bij elke verrichting "
                  "stelt:"),
            ("fig", svg.stappen(["welke|rekeningen?", "welke|soort?", "stijgt of|daalt ze?", "debet of|credit?"]),
                    "De vier vragen van het redeneerschema, altijd in deze orde."),
            ("p", "Pas als die vier vragen beantwoord zijn, schrijf je iets op. De winst volgt pas op het einde "
                  "van het boekjaar en speelt hier dus geen rol."),
        ]),
        dict(kop="Het MAR", blokken=[
            ("p", "Het <strong>MAR</strong>, het minimum algemeen rekeningstelsel, geeft "
                  "<strong>elke rekening een eigen nummer</strong> in zeven klassen. Daardoor boekt iedereen "
                  "dezelfde verrichting op dezelfde rekening, en kan je elke jaarrekening lezen."),
            ("kader", tabel(["klasse", "wat erin staat"],
                            [["1", "eigen vermogen en schulden op meer dan één jaar"],
                             ["2", "vaste activa"],
                             ["3", "voorraden"],
                             ["4", "vorderingen en schulden op ten hoogste één jaar"],
                             ["5", "geldbeleggingen en liquide middelen"],
                             ["6", "<strong>kosten</strong>"],
                             ["7", "<strong>opbrengsten</strong>"]])),
            ("p", "De klassen <strong>1 tot 5</strong> komen op de <strong>balans</strong>, de klassen "
                  "<strong>6 en 7</strong> vormen de <strong>resultatenrekening</strong>. Klasse 2 zijn dus de "
                  "<strong>vaste activa</strong> en niet de opbrengsten. In klasse 6 zitten bijvoorbeeld de "
                  "<strong>bezoldigingen</strong>, de <strong>aankopen van handelsgoederen</strong> en de "
                  "<strong>huur</strong>; <strong>verkopen</strong> horen bij klasse 7. En de "
                  "<strong>btw op je aankopen</strong> boek je op <strong>terug te vorderen btw</strong>: die "
                  "mag je van de staat terugvragen, dus is het een <strong>vordering</strong> in het debet."),
        ]),
        dict(kop="Journaal en grootboek", blokken=[
            ("p", "In het <strong>journaal</strong> komt <strong>elke verrichting op datum</strong>, in de orde "
                  "waarin ze gebeurd is. Het <strong>grootboek</strong> sorteert dezelfde boekingen "
                  "<strong>per rekening</strong>, zodat je het <strong>saldo</strong> van elke rekening ziet. Een "
                  "<strong>grootboekrekening</strong> is dus <strong>één rekening apart</strong>, met haar "
                  "debet- en haar creditkant."),
            ("p", "Het zijn twee manieren om naar <strong>dezelfde</strong> boekingen te kijken: een boeking in "
                  "het journaal komt daarna <strong>ook</strong> in het grootboek. Het verschil tussen de "
                  "debet- en de creditkant van een grootboekrekening heet het <strong>saldo</strong>; staat het "
                  "grootste bedrag links, dan is er een <strong>debetsaldo</strong>."),
        ]),
        dict(kop="De gewone verrichtingen", blokken=[
            ("p", "<strong>Een aankoopfactuur van handelsgoederen.</strong> In het debet: "
                  "<strong>Aankopen handelsgoederen</strong> (een kost) en de <strong>terug te vorderen "
                  "btw</strong>. In het credit: de <strong>leverancier</strong>, voor het hele factuurbedrag. "
                  "Bij 1 000 euro goederen met 21 % btw krijgt de leverancier dus "
                  "<strong>1 210 euro</strong> in het credit."),
            ("p", "<strong>Een verkoopfactuur van handelsgoederen.</strong> In het debet: de "
                  "<strong>handelsvordering</strong> op de klant. In het credit: de "
                  "<strong>verkopen</strong> en de <strong>te betalen btw</strong>. Bij 2 000 euro goederen met "
                  "21 % btw is het factuurtotaal <strong>2 420 euro</strong>."),
            ("p", "<strong>Betalingen.</strong> Betaal je een aankoopfactuur via de bank, dan "
                  "<strong>daalt</strong> de schuld — de leverancier komt in het <strong>debet</strong> — en "
                  "daalt de bank in het credit. Aan de <strong>kosten verandert er niets</strong>: die stonden al "
                  "in de boeken bij de factuur. Ontvang je een betaling van een klant, dan komt de "
                  "<strong>bank in het debet</strong> en de vordering in het credit."),
            ("p", "<strong>Creditnota's.</strong> Een <strong>inkomende</strong> creditnota is een "
                  "<strong>correctie van een aankoop</strong>: ze <strong>verlaagt</strong> je schuld aan de "
                  "leverancier, bijvoorbeeld na een terugzending. Een <strong>uitgaande</strong> creditnota "
                  "draait een stuk van een <strong>verkoop</strong> terug: de verkoop daalt, de "
                  "<strong>vordering</strong> op de klant daalt en de <strong>te betalen btw</strong> daalt mee. "
                  "Er komt géén geld binnen, dus de bank blijft ongemoeid."),
            ("p", "De <strong>btw</strong> boek je apart omdat het <strong>geld van de staat</strong> is: wat je "
                  "aanrekent stort je door, wat je betaalt vorder je terug. Ze hoort dus niet bij je kosten of "
                  "je opbrengsten."),
            ("p", "Een boekhouder deelt de <strong>aankopen</strong> in drie soorten in: "
                  "<strong>handelsgoederen</strong> (gaan door naar de klant), <strong>diensten en diverse "
                  "goederen</strong> (werkingskosten zoals huur en verzekering) en "
                  "<strong>investeringsgoederen</strong> (gaan jaren mee). Een <strong>bestelwagen</strong> voor "
                  "de zaak is dus een <strong>investering</strong>, in klasse 2, en de kost volgt via de "
                  "<strong>afschrijvingen</strong>."),
        ]),
    ],
    onthoud=[
        "Debet is links, credit is rechts; in elke boeking zijn de twee totalen gelijk.",
        "Actief stijgt in het debet en daalt in het credit; passief net omgekeerd.",
        "Kosten boek je in het debet, opbrengsten in het credit.",
        "Het redeneerschema: welke rekeningen, welke soort, stijgt of daalt, debet of credit.",
        "MAR: klassen 1 tot 5 vormen de balans, 6 zijn de kosten en 7 de opbrengsten.",
        "Het journaal staat op datum, het grootboek per rekening; het saldo is het verschil tussen de twee kanten.",
        "Aankoopfactuur: aankopen en terug te vorderen btw in het debet, de leverancier in het credit.",
        "Verkoopfactuur: de vordering in het debet, de verkoop en de te betalen btw in het credit.",
        "Een betaling raakt de kosten niet. Een creditnota corrigeert een eerdere factuur, btw inbegrepen.",
    ])


# ───────────────────────── 16. Facturen, kortingen en btw
zet("facturen-kortingen-en-btw",
    titel="Facturen, kortingen en btw",
    onder="De vaste orde waarin je een factuur narekent, van de brutoprijs tot het te betalen totaal.",
    secties=[
        dict(kop="De orde van rekenen", blokken=[
            ("p", "Een factuur reken je <strong>altijd in dezelfde orde</strong> na. Wie de stappen omwisselt, "
                  "komt op een ander bedrag uit."),
            ("fig", svg.stappen(["brutoprijs", "&minus; handels-|korting", "&minus; financiële|korting",
                                 "+ doorgerekende|kosten", "= maatstaf|van heffing"]),
                    "De weg naar de maatstaf van heffing."),
            ("p", "Daarna komt de <strong>btw</strong> op die maatstaf, en pas <strong>na</strong> de btw komt de "
                  "<strong>terugstuurbare verpakking</strong> bij het totaal."),
        ]),
        dict(kop="De twee kortingen", blokken=[
            ("p", "Een <strong>handelskorting</strong> is een korting op de <strong>prijs zelf</strong>: bij een "
                  "<strong>grote hoeveelheid</strong>, voor een <strong>vaste klant</strong> of tijdens een "
                  "<strong>actie</strong>. Ze kan op de factuur staan <strong>in procent of in euro</strong>, en "
                  "ze gaat als <strong>eerste</strong> van de brutoprijs af."),
            ("p", "Een <strong>financiële korting</strong> krijg je omdat je <strong>snel betaalt</strong>; ze "
                  "heet ook korting voor contante betaling. De leverancier geeft ze om "
                  "<strong>sneller zijn geld te hebben</strong>. Je rekent ze op de prijs "
                  "<strong>na</strong> de handelskorting, dus niet op de brutoprijs."),
            ("p", "<strong>Beide</strong> kortingen gaan van de <strong>maatstaf van heffing</strong> af, en de "
                  "financiële korting <strong>ook als de klant ze niet gebruikt</strong> en later gewoon het "
                  "volle bedrag betaalt. De maatstaf van heffing is het bedrag <strong>waarop je de btw "
                  "berekent</strong>."),
            ("kader", "Rekenen: 1 000 euro met 10 % handelskorting geeft <strong>900 euro</strong>. Daarvan 2 % "
                      "financiële korting is <strong>18 euro</strong>, dus blijft er "
                      "<strong>882 euro</strong> over — en let op: die 2 % reken je op 900, niet op 1 000. "
                      "Andere voorbeelden: 25 % op 2 000 euro laat <strong>1 500 euro</strong> over, en 20 % op "
                      "500 euro is <strong>100 euro</strong> korting."),
        ]),
        dict(kop="Kosten, verpakking en btw", blokken=[
            ("p", "<strong>Doorgerekende kosten</strong> horen bij de prijs van de levering en "
                  "<strong>verhogen</strong> de maatstaf van heffing: <strong>vervoer</strong>, een "
                  "<strong>verzekering</strong>, <strong>verpakking die niet terugkeert</strong>. Er komt dus "
                  "<strong>btw</strong> op. Een factuur met 1 000 euro goederen en 100 euro vervoer heeft een "
                  "maatstaf van <strong>1 100 euro</strong>."),
            ("p", "Een <strong>terugstuurbare verpakking</strong> werkt als een <strong>waarborg</strong>: stuurt "
                  "de klant de kratten terug, dan <strong>krijgt hij dat bedrag terug</strong>. Het is dus geen "
                  "verkoop, en er komt <strong>geen btw</strong> op. Ze staat apart op de factuur en komt "
                  "<strong>na</strong> de btw bij het totaal."),
            ("p", "Het <strong>gewone btw-tarief</strong> in België is <strong>21 %</strong>; er bestaan "
                  "verlaagde tarieven van 6 en 12 % voor onder meer voeding en woningwerken. Reken: 21 % van "
                  "1 000 euro is <strong>210 euro</strong>; van 950 euro is het "
                  "<strong>199,50 euro</strong>."),
            ("kader", "Een volledig voorbeeld: 500 euro goederen, 21 % btw en 60 euro terugstuurbare "
                      "verpakking. De btw is 105 euro, en de verpakking komt daarna erbij: "
                      "500 + 105 + 60 = <strong>665 euro</strong> te betalen."),
        ]),
        dict(kop="De creditnota", blokken=[
            ("p", "Een factuur mag je <strong>niet aanpassen</strong>. Wil je iets rechtzetten, dan maak je een "
                  "<strong>creditnota</strong>: bij een <strong>terugzending</strong>, bij een "
                  "<strong>te hoog aangerekend bedrag</strong> of bij een <strong>korting achteraf</strong>. Bij "
                  "een gewone betaling hoort er geen."),
            ("p", "Draait de creditnota een verkoop met btw terug, dan staat de <strong>btw er ook op</strong>. "
                  "Anders zou de staat te veel btw houden."),
        ]),
        dict(kop="Wat je op een factuur nakijkt", blokken=[
            ("p", "Op een factuur staan de <strong>goederen met hun prijs</strong>, de <strong>kortingen</strong>, "
                  "de <strong>doorgerekende kosten</strong>, de <strong>btw</strong> en de "
                  "<strong>vervaldag</strong>. Wat de leverancier eraan verdient, staat er niet op."),
            ("p", "Narekenen doe je dus op drie dingen: staan de <strong>afgesproken kortingen</strong> erop, "
                  "kloppen de <strong>aangerekende kosten</strong>, en is de <strong>btw</strong> juist berekend? "
                  "De <strong>vervaldag</strong> is de <strong>uiterste betaaldatum</strong>: staat er dertig "
                  "dagen, dan heb je dertig dagen om te betalen, en daarna kan de leverancier verwijlintresten "
                  "aanrekenen."),
            ("p", "Herhaal ten slotte de indeling van de <strong>aankopen</strong>: "
                  "<strong>handelsgoederen</strong> zijn goederen om <strong>door te verkopen</strong>, een "
                  "<strong>verzekeringspremie</strong> is een aankoop van <strong>diensten en diverse "
                  "goederen</strong>, en een <strong>computer die vijf jaar meegaat</strong> is een "
                  "<strong>investeringsgoed</strong>."),
        ]),
    ],
    onthoud=[
        "De orde: brutoprijs − handelskorting − financiële korting + doorgerekende kosten = maatstaf van heffing.",
        "Daarop komt de btw; de terugstuurbare verpakking komt pas na de btw bij het totaal.",
        "Een handelskorting hangt af van de aankoop, een financiële korting van het moment van betalen.",
        "De financiële korting reken je op de prijs na de handelskorting, en ze gaat altijd van de btw-basis af.",
        "Doorgerekend vervoer, verzekering en verloren verpakking verhogen de maatstaf; er komt btw op.",
        "Op een terugstuurbare verpakking komt geen btw: het is een waarborg.",
        "Het gewone btw-tarief is 21 %.",
        "Een creditnota corrigeert een eerdere factuur, met de btw erop.",
    ])


# ───────────────────────── 17. Bedrijfsstrategie
zet("bedrijfsstrategie-missie-visie-swot-en-stakeholders",
    titel="Bedrijfsstrategie: missie, visie, SWOT en stakeholders",
    onder="Waarvoor een bedrijf bestaat, waar het naartoe wil, en met wie het rekening houdt.",
    secties=[
        dict(kop="Missie en visie", blokken=[
            ("p", "De <strong>missie</strong> zegt <strong>waarvoor een bedrijf bestaat</strong>: "
                  "<strong>wat</strong> het doet, <strong>voor wie</strong>, en <strong>waarin het "
                  "anders</strong> is. Ze gaat over <strong>vandaag</strong> en bevat geen cijfers; die staan in "
                  "de jaarrekening. Ook een <strong>vzw</strong> heeft een missie — daar is ze zelfs nog "
                  "belangrijker, want winst is er het doel niet."),
            ("p", "De <strong>visie</strong> is het beeld van <strong>waar het bedrijf naartoe wil</strong>, "
                  "bijvoorbeeld binnen tien jaar. Ze kijkt dus <strong>vooruit</strong>."),
            ("kader", tabel(["uitspraak van een bakkerij", "wat het is"],
                            [["We bakken elke ochtend verse broden voor de buurt.", "<strong>missie</strong>"],
                             ["Over vijf jaar hebben we in elke stad een filiaal.", "<strong>visie</strong>"],
                             ["In 2035 werken we volledig zonder afval.", "<strong>visie</strong>"],
                             ["Deze maand 2 000 euro meer omzet dan vorige maand.", "<strong>doelstelling</strong>"]])),
            ("p", "Een <strong>doelstelling</strong> is iets anders dan een missie: ze is "
                  "<strong>meetbaar</strong> en heeft een <strong>datum</strong>. Een "
                  "<strong>kernwaarde</strong> is weer iets anders: dat is <strong>iets waar het bedrijf voor "
                  "staat</strong> en niet van afwijkt, zoals eerlijkheid of duurzaamheid."),
        ]),
        dict(kop="Waarom een strategie telt", blokken=[
            ("p", "Een <strong>bedrijfsstrategie</strong> gaat over de <strong>grote lijnen</strong>: "
                  "<strong>doelen op lange termijn</strong>, de <strong>keuze van de doelgroep</strong> en "
                  "<strong>hoe het bedrijf zich onderscheidt</strong>. De planning van de leveringen van morgen "
                  "hoort daar niet bij; dat is dagelijkse organisatie."),
            ("p", "Ze is belangrijk om drie redenen: <strong>iedereen trekt dezelfde kant uit</strong>, "
                  "<strong>keuzes maken wordt makkelijker</strong>, en de <strong>kans op succes stijgt</strong>. "
                  "Een strategie helpt ook om te kiezen <strong>wat je niet doet</strong>: welke klanten, "
                  "producten en markten je laat liggen, zodat je je kracht niet versnippert. Concurrenten "
                  "verdwijnen er natuurlijk niet door, en een bedrijf zonder strategie maakt niet "
                  "<strong>altijd</strong> verlies — de kans op verkeerde keuzes is wel groter."),
            ("p", "De <strong>leiding</strong> bepaalt de strategie: de zaakvoerder of de raad van bestuur, "
                  "vaak na overleg met het personeel. De missie wordt uitgeschreven <strong>zodat iedereen "
                  "hetzelfde weet</strong> en mensen dezelfde soort beslissingen nemen, ook zonder dat de baas "
                  "erbij staat."),
        ]),
        dict(kop="De SWOT-analyse", blokken=[
            ("p", "<strong>SWOT</strong> staat voor <strong>sterktes, zwaktes, kansen en bedreigingen</strong> "
                  "(strengths, weaknesses, opportunities, threats). <strong>Sterktes en zwaktes</strong> zijn "
                  "<strong>intern</strong>: ze gaan over het bedrijf zelf. <strong>Kansen en bedreigingen</strong> "
                  "komen van <strong>buiten</strong>."),
            ("fig", svg.swotvakken(
                ["vakkundig personeel", "een sterke merknaam", "een eigen recept"],
                ["oude machines", "één verkooppunt", "weinig reserves"],
                ["een groeiende vraag", "een nieuwe fietsroute langs de winkel", "goedkopere techniek"],
                ["een nieuwe wet", "een stijgende grondstofprijs", "een nieuwe concurrent"]),
                    "De vier vakken van een SWOT, met de interne links en de externe rechts."),
            ("p", "Een <strong>eigen recept dat niemand anders heeft</strong> is dus een "
                  "<strong>sterkte</strong>; een <strong>stijgende energieprijs</strong> is een "
                  "<strong>bedreiging</strong>; een <strong>nieuwe wet</strong> die het lastiger maakt is een "
                  "bedreiging, en een wet die deuren opent een <strong>kans</strong>. Een drukke "
                  "<strong>fietsroute</strong> langs de winkel is een kans: meer passage, van buiten gekomen."),
            ("p", "Een <strong>zwakte</strong> kan een bedrijf <strong>wel</strong> zelf aanpakken — ze zit in "
                  "het bedrijf: opleiding geven, machines vernieuwen, de website herbouwen. Een SWOT helpt "
                  "daarna om te <strong>kiezen waar je op inzet</strong>: leg je sterktes op de kansen om te zien "
                  "waar je kan groeien, en je zwaktes naast de bedreigingen om te zien waar je moet oppassen."),
        ]),
        dict(kop="Stakeholders", blokken=[
            ("p", "Een <strong>stakeholder</strong> of belanghebbende is <strong>iedereen met een belang</strong> "
                  "bij wat de onderneming doet. Dat zijn <strong>mensen en organisaties</strong>, geen machines. "
                  "<strong>Interne</strong> stakeholders zitten in de onderneming: het "
                  "<strong>personeel</strong>, de zaakvoerders, de aandeelhouders. "
                  "<strong>Externe</strong> staan erbuiten: klanten, leveranciers, de overheid, de buurt."),
            ("kader", tabel(["stakeholder", "zijn belang"],
                            [["de <strong>werknemers</strong>", "een goed loon, een veilige werkplek, werkzekerheid"],
                             ["de <strong>aandeelhouders</strong>", "winst en dividend, een aandeel dat in waarde stijgt"],
                             ["de <strong>klanten</strong>", "een goed product aan een redelijke prijs"],
                             ["de <strong>leveranciers</strong>", "op tijd betaald worden en vaste orders"],
                             ["de <strong>buurt</strong>", "weinig lawaai, geur en verkeer"],
                             ["de <strong>overheid</strong>", "belastingen, regels die nageleefd worden"]])),
            ("p", "Een onderneming houdt rekening met haar stakeholders omdat ze hen "
                  "<strong>nodig heeft</strong>: zonder personeel, klanten, leveranciers of een buurt die haar "
                  "aanvaardt, kan ze niet werken. Wie hun belangen negeert, komt dat vroeg of laat tegen. En die "
                  "belangen <strong>botsen</strong> soms: hogere lonen tegen een hoger dividend, een uitbreiding "
                  "tegen de rust van de buurt. Daarover gaat het overleg."),
        ]),
    ],
    onthoud=[
        "De missie zegt waarvoor een bedrijf bestaat: wat, voor wie en waarin het anders is.",
        "De visie kijkt vooruit; een doelstelling is meetbaar en heeft een datum.",
        "Een strategie gaat over doelen, doelgroep en eigen karakter, en zegt ook wat je niet doet.",
        "SWOT: sterktes en zwaktes zijn intern, kansen en bedreigingen komen van buiten.",
        "Een zwakte kan een bedrijf zelf aanpakken; een bedreiging niet.",
        "Leg sterktes op kansen om te groeien, en zwaktes naast bedreigingen om op te passen.",
        "Een stakeholder is iedereen met een belang; intern zijn personeel en aandeelhouders, extern klanten, buurt en overheid.",
        "Belangen van stakeholders botsen soms; daarover gaat het overleg.",
    ])


# ───────────────────────── 18. Marktonderzoek, doelgroep en de marketingmix
zet("marktonderzoek-doelgroep-en-de-marketingmix",
    titel="Marktonderzoek, doelgroep en de marketingmix",
    onder="Eerst weten voor wie je werkt, dan de vier P's — en dezelfde vier door de ogen van de klant.",
    secties=[
        dict(kop="Marktonderzoek", blokken=[
            ("p", "Het doel van een <strong>marktonderzoek</strong> is de <strong>markt leren kennen</strong>: "
                  "wie de klanten zijn, wat ze willen, wat ze willen betalen en wat de concurrenten doen. Zo kan "
                  "een bedrijf beslissen met minder gokwerk. Je doet het dus "
                  "<strong>vóór</strong> je een nieuw product start, niet nadat het gefaald is."),
            ("kader", tabel(["indeling", "soort", "wat het is"],
                            [["naar <strong>herkomst</strong>", "<strong>primair</strong>", "het bedrijf verzamelt de gegevens <strong>zelf</strong>: een enquête, een gesprek, een test in de winkel"],
                             ["", "<strong>secundair</strong>", "het gebruikt gegevens die <strong>al bestaan</strong>: cijfers van de overheid, een rapport van een studiebureau, een artikel in een vakblad"],
                             ["naar <strong>soort gegeven</strong>", "<strong>kwantitatief</strong>", "met <strong>cijfers</strong>: hoeveel, hoeveel procent, een enquête bij duizend mensen"],
                             ["", "<strong>kwalitatief</strong>", "met <strong>waarom</strong>: een diepte-interview, een groepsgesprek"]])),
            ("p", "De twee indelingen staan los van elkaar: een eigen enquête bij vijftig klanten met een cijfer "
                  "van 1 tot 10 is <strong>primair én kwantitatief</strong>. En primair onderzoek is meestal "
                  "<strong>duurder</strong> dan secundair, niet goedkoper: het bedrijf moet alles zelf opzetten."),
        ]),
        dict(kop="Segmentatie en doelgroep", blokken=[
            ("p", "<strong>Marktsegmentatie</strong> is de markt <strong>in groepen delen</strong> die op elkaar "
                  "lijken. Dat kan op <strong>leeftijd</strong>, gezinssamenstelling, <strong>woonplaats</strong>, "
                  "inkomen, <strong>levensstijl</strong> of gedrag — op kenmerken van <strong>mensen</strong> dus, "
                  "niet op de verpakking die het bedrijf zelf kiest."),
            ("p", "Uit die segmenten kiest het bedrijf er één of enkele: dat is de "
                  "<strong>doelgroep</strong>, de groep die het wil bereiken. Een merk dat schoenen maakt "
                  "<strong>speciaal voor lopers</strong>, doet precies dat."),
            ("p", "Waarom kiezen? Omdat de <strong>boodschap</strong> dan beter past, het "
                  "<strong>reclamegeld</strong> meer rendeert en het <strong>product</strong> beter aansluit. "
                  "Wie géén doelgroep kiest, maakt een boodschap voor iedereen, en die "
                  "<strong>raakt niemand echt</strong>."),
        ]),
        dict(kop="B2B, B2C, C2C en C2B", blokken=[
            ("kader", tabel(["afkorting", "van wie naar wie", "voorbeeld"],
                            [["<strong>B2B</strong>", "bedrijf aan bedrijf", "een groothandel levert aan een winkel; een drukkerij print voor een school"],
                             ["<strong>B2C</strong>", "bedrijf aan consument", "een bakker verkoopt brood aan een gezin; een webshop verkoopt kleren"],
                             ["<strong>C2C</strong>", "consument aan consument", "een tweedehandsplatform"],
                             ["<strong>C2B</strong>", "consument aan bedrijf", "iemand verkoopt zijn foto's of zijn mening aan een bedrijf"]])),
            ("p", "Let op de richting: <strong>C2B is niet hetzelfde als B2C</strong>. En of een verkoop in een "
                  "winkel of online gebeurt, verandert de soort <strong>niet</strong>: een webshop die aan "
                  "gezinnen verkoopt, blijft <strong>B2C</strong>."),
        ]),
        dict(kop="De marketingmix: vier P's en vier C's", blokken=[
            ("p", "De <strong>marketingmix</strong> zijn de vier knoppen waaraan een bedrijf draait. Eerst kiest "
                  "het zijn <strong>strategie</strong> — doelgroep en eigen plaats in de markt — en pas "
                  "<strong>daarna</strong> de mix, want <strong>de mix volgt uit die keuzes</strong>."),
            ("kader", tabel(["de vier P's", "wat eronder valt", "de vier C's"],
                            [["<strong>product</strong>", "wat je aanbiedt, met kwaliteit, merk en verpakking", "<strong>customer value</strong>: wat het de klant waard is"],
                             ["<strong>prijs</strong>", "wat het kost en welke strategie daarachter zit", "<strong>cost</strong>: wat het de klant kost, ook in tijd en verplaatsing"],
                             ["<strong>plaats</strong>", "de winkel, de webshop, de levering aan huis", "<strong>convenience</strong>: hoe makkelijk de klant eraan komt"],
                             ["<strong>promotie</strong>", "reclame, sociale media, een actie in de winkel", "<strong>communication</strong>: een gesprek in twee richtingen"]])),
            ("p", "De <strong>vier C's</strong> zijn dezelfde mix, maar <strong>door de ogen van de "
                  "klant</strong>. Dat helpt een bedrijf om niet enkel aan zijn eigen product te denken. Het "
                  "verschil met promotie is tekenend: <strong>promotie</strong> vertrekt van het bedrijf dat "
                  "zendt, <strong>communication</strong> van een gesprek waarin de klant ook antwoordt."),
            ("p", "Pas op met de grenzen tussen de P's: de <strong>ligging</strong> van de winkel hoort bij "
                  "<strong>plaats</strong> en niet bij promotie, en de <strong>prijs per stuk</strong> is een "
                  "eigen P. <strong>Personeel</strong> hoort niet bij deze vier."),
        ]),
    ],
    onthoud=[
        "Een marktonderzoek leert de markt kennen; je doet het vóór je start.",
        "Primair = zelf verzamelen, secundair = bestaande gegevens gebruiken.",
        "Kwantitatief werkt met cijfers, kwalitatief met het waarom.",
        "Marktsegmentatie deelt de markt in groepen; de gekozen groep is de doelgroep.",
        "Zonder doelgroep raakt de boodschap niemand echt.",
        "B2B bedrijf aan bedrijf, B2C bedrijf aan consument, C2C tussen consumenten, C2B consument aan bedrijf.",
        "De vier P's: product, prijs, plaats en promotie.",
        "De vier C's zijn dezelfde mix door de ogen van de klant: customer value, cost, convenience, communication.",
        "Eerst de strategie, dan de mix.",
    ])


# ───────────────────────── 19. Producten, merken, prijsstrategie en distributie
zet("producten-merken-prijsstrategie-en-distributie",
    titel="Producten, merken, prijsstrategie en distributie",
    onder="Soorten goederen, het assortiment, de merken, de levenscyclus, de prijs en de weg naar de klant.",
    secties=[
        dict(kop="Soorten consumptiegoederen", blokken=[
            ("kader", tabel(["indeling", "soorten", "voorbeeld"],
                            [["naar <strong>levensduur</strong>", "<strong>duurzaam</strong> / <strong>niet-duurzaam</strong>", "een wasmachine / een brood"],
                             ["naar <strong>koper</strong>", "<strong>consumenten</strong>- / <strong>industriële</strong> goederen", "een fiets voor thuis / een machine voor de productie"],
                             ["naar <strong>koopgedrag</strong>", "<strong>convenience</strong>", "brood, een krant, melk: vaak, dichtbij, zonder vergelijken"],
                             ["", "<strong>shopping</strong>", "een jas, een eetkamertafel: je vergelijkt eerst"],
                             ["", "<strong>speciality</strong>", "een duur horloge: je wil dat ene merk en rijdt er desnoods voor om"],
                             ["", "<strong>unsought</strong>", "een brandblusser, een verzekering: je zoekt ze niet"]])),
            ("p", "<strong>Industriële goederen</strong> koopt een bedrijf om er <strong>zelf mee te "
                  "werken</strong>: grondstoffen, machines, onderdelen."),
        ]),
        dict(kop="Breedte, diepte en merken", blokken=[
            ("p", "De <strong>breedte</strong> van een assortiment is het <strong>aantal "
                  "productgroepen</strong>: brood, zuivel, groenten, drank. De <strong>diepte</strong> is het "
                  "<strong>aantal varianten binnen één groep</strong>. Twaalf soorten yoghurt naast elkaar is "
                  "dus een <strong>diep</strong> assortiment."),
            ("p", "Een <strong>A-merk</strong> is het <strong>merk van de producent</strong>: het staat in veel "
                  "winkels en krijgt eigen reclame. Een <strong>winkelmerk</strong> is van de keten zelf en "
                  "bestaat vaak in drie lijnen: <strong>standaard</strong>, <strong>budget</strong> en "
                  "<strong>bio</strong>. Een A-merk is doorgaans <strong>duurder</strong> dan een winkelmerk, "
                  "niet goedkoper."),
            ("p", "Een winkel zet een budgetmerk náást een A-merk om <strong>elke beurs te bedienen</strong>, "
                  "om <strong>prijsbewuste klanten te houden</strong> in plaats van ze aan een goedkopere keten "
                  "te verliezen, en omdat ze op haar <strong>eigen merk meer marge</strong> houdt."),
            ("kader", tabel(["merkbeleid", "wat het is", "voorbeeld"],
                            [["<strong>lijnextensie</strong>", "een nieuwe <strong>variant</strong> onder hetzelfde merk, in dezelfde groep", "een nieuwe smaak, een ander formaat"],
                             ["<strong>merkextensie</strong>", "hetzelfde merk in een <strong>nieuwe productgroep</strong>", "een chocolademerk brengt ijs uit"],
                             ["<strong>multibrands</strong>", "<strong>meerdere eigen merken</strong> in dezelfde groep", "twee waspoeders van dezelfde fabrikant"],
                             ["<strong>nieuw merk</strong>", "een nieuw merk voor een nieuwe groep", "een volledig nieuwe naam"]])),
        ]),
        dict(kop="De productlevenscyclus", blokken=[
            ("fig", svg.levenscyclus(), "De vijf fases van een product, met de verkoop op de zij-as."),
            ("p", "De cyclus loopt van de <strong>ontwikkelingsfase</strong> (nog geen verkoop, enkel "
                  "kosten) naar de <strong>introductiefase</strong>, de <strong>groeifase</strong>, de "
                  "<strong>volwassenheidsfase</strong> en de <strong>neergangsfase</strong>. Na de "
                  "introductiefase komt dus de groeifase. In de <strong>groeifase</strong> stijgt de verkoop het "
                  "<strong>snelst</strong>; in de <strong>volwassenheidsfase</strong> blijft ze hoog maar "
                  "<strong>vlak</strong> en wordt de concurrentie het scherpst; in de "
                  "<strong>neergangsfase daalt</strong> ze, en kiest het bedrijf tussen vernieuwen of stoppen."),
        ]),
        dict(kop="Prijsstrategieën", blokken=[
            ("kader", tabel(["strategie", "wat ze doet"],
                            [["<strong>afroomstrategie</strong>", "<strong>hoog</strong> beginnen en de prijs later laten dalen; past bij een nieuw product zonder alternatief"],
                             ["<strong>penetratiestrategie</strong>", "<strong>laag</strong> beginnen om snel marktaandeel te pakken"],
                             ["<strong>cost-plus pricing</strong>", "de <strong>kostprijs plus een marge</strong>"],
                             ["<strong>consumer-based pricing</strong>", "wat de <strong>klant</strong> wil betalen"],
                             ["<strong>competitor-based pricing</strong>", "kijken naar de <strong>concurrent</strong>: eronder, gelijk of bewust erboven"],
                             ["<strong>premium pricing</strong>", "een <strong>hoge prijs als signaal</strong> van kwaliteit"]])),
            ("p", "Twee woorden die op elkaar lijken: bij <strong>prijsdifferentiatie</strong> hangt de prijs af "
                  "van <strong>tijd, plaats of hoeveelheid</strong> (een treinticket in de spits, korting per "
                  "doos). Bij <strong>prijsdiscriminatie</strong> betaalt de <strong>ene groep klanten</strong> "
                  "minder dan de andere voor net hetzelfde: studenten, senioren, kinderen."),
        ]),
        dict(kop="Distributie, e-commerce en push of pull", blokken=[
            ("kader", tabel(["intensiteit", "wat ze betekent", "past bij"],
                            [["<strong>intensieve</strong> distributie", "in zoveel verkooppunten als mogelijk", "convenience goederen"],
                             ["<strong>selectieve</strong> distributie", "in een beperkt aantal gekozen winkels", "shopping goederen"],
                             ["<strong>exclusieve</strong> distributie", "één verkooppunt per gebied", "speciality goederen"]])),
            ("p", "<strong>E-commerce</strong> is <strong>verkopen via het internet</strong>, met levering aan "
                  "huis of ophaling in een punt. Het verandert vooral de P van <strong>plaats</strong>."),
            ("p", "Tot slot twee manieren om een product de winkel in te krijgen. Bij een "
                  "<strong>pushstrategie</strong> <strong>duwt</strong> de producent zijn product bij de "
                  "<strong>tussenhandel</strong> binnen, met kortingen en premies voor de winkelier. Bij een "
                  "<strong>pullstrategie</strong> <strong>trekt</strong> hij de <strong>consument</strong> aan "
                  "met reclame en een sterke merknaam, zodat die <strong>er zelf in de winkel naar vraagt</strong> "
                  "en de winkelier het wel moet aanbieden."),
        ]),
    ],
    onthoud=[
        "Duurzaam gaat lang mee, niet-duurzaam is snel op; industriële goederen koopt een bedrijf om mee te werken.",
        "Convenience koop je zonder nadenken, shopping na vergelijken, speciality met een omrit, unsought zoek je niet.",
        "Breedte is het aantal productgroepen, diepte het aantal varianten binnen één groep.",
        "Een A-merk is van de producent; winkelmerken bestaan in standaard, budget en bio.",
        "Merkbeleid: lijnextensie, merkextensie, multibrands en een nieuw merk.",
        "De levenscyclus: ontwikkeling, introductie, groei, volwassenheid, neergang.",
        "Afroomstrategie begint hoog, penetratiestrategie begint laag.",
        "Prijsdifferentiatie volgt tijd, plaats of hoeveelheid; prijsdiscriminatie volgt de groep klanten.",
        "Distributie is intensief, selectief of exclusief. Push gaat via de winkelier, pull via de consument.",
    ])


if __name__ == "__main__":
    for naam, b in BUNDELS.items():
        bundel.schrijf(b, naam)

# -*- coding: utf-8 -*-
"""De leerbundels voor natuurwetenschappen op 🌍 Beyond-niveau.

Gebaseerd op de vakfiche natuurwetenschappen van de 3de graad
doorstroomfinaliteit, geldig vanaf 1 januari 2027. Die fiche noemt bovenaan
zelf vijf studierichtingen: moderne talen, humane wetenschappen, Latijn-moderne
talen, economie-wiskunde en bedrijfswetenschappen. De richtingen
wetenschappen-wiskunde en Latijn-wiskunde met extra wetenschappen hebben in de
plaats hiervan drie aparte fiches biologie, chemie en fysica.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De eenentwintig thema's volgen de weging van het examen zelf: negen over
biologie, vier over chemie, zes over fysica en twee over onderzoek en STEM.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../beyond/natuurwetenschappen.json`
doet daar het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-beyond". Natuurwetenschappen bestaat ook op
✨ Spark en op 🚀 Boost, en daar klinken sommige thematitels bijna gelijk.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Natuurwetenschappen"
BEYOND = "🌍 Beyond — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 10. Snelheid van een chemische reactie
BUNDELS["snelheid-van-een-chemische-reactie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Snelheid van een chemische reactie",
    onder="Wat reactiesnelheid is, hoe je ze aan een grafiek afleest, en de vier factoren die haar bepalen.",
    secties=[
        dict(kop="Wat is reactiesnelheid?", blokken=[
            ("p", "De <strong>snelheid van een chemische reactie</strong> druk je uit als de "
                  "<strong>verandering van een concentratie per tijdseenheid</strong>: de "
                  "<strong>afname</strong> van de concentratie van een <strong>reagens</strong> of de "
                  "<strong>toename</strong> van die van een <strong>reactieproduct</strong> in een "
                  "bepaalde tijd. Een massa of een volume "
                  "alleen is géén snelheid, want daar zit geen tijd in."),
            ("p", "Er is ook een tweede manier om hetzelfde te zeggen, vanuit de deeltjes: de snelheid is "
                  "het <strong>aantal effectieve botsingen per tijdseenheid</strong>. Het aantal deeltjes "
                  "in het vat alleen zegt niets over snelheid, want er staat geen tijd bij."),
            ("kader", "Snelheid en opbrengst zijn twee verschillende dingen. <strong>Hoeveel product er "
                      "uiteindelijk ontstaat, hangt af van hoeveel reagens er was</strong>, niet van hoe "
                      "snel het ging. Een trage en een snelle reactie kunnen op het einde precies hetzelfde "
                      "opleveren."),
        ]),
        dict(kop="Het botsingsmodel", blokken=[
            ("p", "Deeltjes reageren enkel als ze botsen, maar niet elke botsing helpt. Een "
                  "<strong>effectieve botsing</strong> is een botsing die wél tot een reactie leidt. "
                  "Daarvoor moet er twee dingen samen kloppen: de deeltjes moeten "
                  "<strong>genoeg energie</strong> hebben én <strong>met de juiste kant tegen elkaar "
                  "botsen</strong>. Ontbreekt er één van de twee, dan gebeurt er niets."),
            ("p", "Een botsing waarbij de deeltjes gewoon <strong>van elkaar wegstuiteren</strong> heet een "
                  "<strong>elastische botsing</strong> of een <strong>niet-effectieve botsing</strong>. "
                  "Daarbij <strong>ontstaat er geen nieuwe stof</strong>: aan de stoffen verandert niets."),
            ("weetje", "In een gewoon bekerglas botsen er per seconde onvoorstelbaar veel deeltjes tegen "
                       "elkaar. Dat er toch reacties zijn die dagen duren, komt doordat maar een heel klein "
                       "deel van al die botsingen effectief is."),
        ]),
        dict(kop="Grafieken lezen", blokken=[
            ("p", "Op een <strong>concentratie-tijdgrafiek</strong> staat de concentratie op de verticale "
                  "as en de tijd op de horizontale. Een <strong>steile daling</strong> van de lijn van een "
                  "reagens betekent dat de reactie op dat moment <strong>snel</strong> gaat; hoe steiler de "
                  "lijn, hoe meer de concentratie per tijdseenheid verandert. Loopt de lijn "
                  "<strong>vlak</strong>, dan verandert er niets meer: de reactie is "
                  "<strong>afgelopen of in evenwicht</strong>."),
            ("p", "De meeste reacties <strong>beginnen snel en worden daarna trager</strong>. In het begin "
                  "zijn er het meeste reagensdeeltjes en dus het meeste botsingen; hoe meer reagens "
                  "opgebruikt is, hoe minder botsingen en hoe trager de reactie."),
            ("p", "Op een <strong>snelheid-tijdgrafiek</strong> staat de snelheid zélf op de verticale as. "
                  "Daar lees je dus <strong>rechtstreeks af hoe snel de reactie op elk moment "
                  "verloopt</strong>, terwijl je op een concentratie-tijdgrafiek eerst naar de steilheid "
                  "van de lijn moet kijken."),
        ]),
        dict(kop="De vier factoren", blokken=[
            ("p", "Vier dingen bepalen de snelheid van een reactie: de "
                  "<strong>verdelingsgraad</strong>, de <strong>temperatuur</strong> (of "
                  "<strong>licht</strong>), de <strong>concentratie</strong> en een "
                  "<strong>katalysator</strong>. Het reactievat zelf doet niet mee aan de reactie en speelt "
                  "dus geen rol."),
            ("p", tabel(["Factor", "Wat je doet", "Waarom het sneller gaat"], [
                ["Verdelingsgraad", "een vaste stof fijner verdelen", "veel meer contactoppervlak, dus meer deeltjes die kunnen botsen"],
                ["Temperatuur", "opwarmen", "de deeltjes bewegen sneller, botsen vaker en harder"],
                ["Concentratie", "meer deeltjes in hetzelfde volume", "meer botsingen per seconde"],
                ["Katalysator", "een stof toevoegen die zelf niet opgebruikt wordt", "de activeringsenergie zakt, dus halen meer botsingen de drempel"],
            ])),
            ("p", "De <strong>verdelingsgraad</strong> is de mate waarin een vaste stof fijn verdeeld is. "
                  "Poeder heeft een hoge verdelingsgraad, één groot stuk een lage. Daarom "
                  "<strong>brandt zaagmeel sneller dan een dik blok van hetzelfde hout</strong>: er is veel "
                  "meer contactoppervlak met de lucht. Laat je <strong>eenzelfde hoeveelheid kalk</strong> "
                  "reageren met zuur, één keer als <strong>brokjes</strong> en één keer als "
                  "<strong>poeder</strong>, dan <strong>reageert het poeder sneller maar geeft het evenveel "
                  "gas</strong>: de verdelingsgraad verandert alleen de snelheid, niet de opbrengst."),
            ("p", "Bij een <strong>hogere temperatuur</strong> gaat een reactie sneller omdat de "
                  "<strong>deeltjes sneller bewegen, dus vaker en harder botsen</strong>. Twee dingen "
                  "tellen daar samen: er zijn meer botsingen per seconde én een groter deel daarvan heeft "
                  "genoeg energie. De <strong>activeringsenergie zelf blijft gelijk</strong>."),
            ("p", "Een <strong>hogere concentratie zorgt voor meer botsingen per seconde</strong>: zitten "
                  "er meer deeltjes in hetzelfde volume, dan komen ze elkaar vaker tegen. Daarom "
                  "<strong>stijgt de snelheid als je een gasmengsel in een kleiner vat perst</strong>: "
                  "evenveel deeltjes in een kleiner volume is een hogere concentratie. Een "
                  "<strong>groter vat</strong> verlaagt de concentratie juist en vertraagt dus."),
            ("p", "Bij <strong>lichtgevoelige reacties</strong> <strong>levert licht de energie om de "
                  "reactie te doen starten</strong>: een deeltje neemt energie uit het licht op. Daarom "
                  "bewaar je waterstofperoxide in een bruine fles."),
            ("kader", "Dezelfde stoffen geven altijd <strong>dezelfde reactievergelijking</strong>. Gaat "
                      "van twee proeven met dezelfde stoffen de ene sneller, dan ligt dat dus aan de "
                      "temperatuur, de concentratie, de verdelingsgraad of een katalysator, en nooit aan "
                      "een andere reactievergelijking."),
        ]),
        dict(kop="Het energiediagram", blokken=[
            ("p", "Op een <strong>energiediagram</strong> staat de <strong>inwendige energie</strong> op de "
                  "verticale as: links de reagentia, rechts de reactieproducten, en daartussen een berg. "
                  "De <strong>activeringsenergie</strong> is de <strong>energie die de deeltjes nodig "
                  "hebben om te kunnen reageren</strong>, dus de hoogte van die berg boven de reagentia. "
                  "Hoe hoger de berg, hoe minder botsingen genoeg energie hebben."),
            ("p", "Bovenaan de berg zit het <strong>geactiveerd complex</strong>: een onstabiele toestand "
                  "waarin de oude bindingen half los en de nieuwe half gelegd zijn. Het geactiveerd complex "
                  "heeft de <strong>hoogste inwendige energie</strong> van het hele verloop."),
            ("p", "De <strong>reactie-energie</strong> bepaal je als het <strong>verschil tussen de energie "
                  "van de producten en die van de reagentia</strong>, dus als het hoogteverschil tussen "
                  "begin en einde. Verwar dat niet met de hoogte van de top boven de reagentia: dat is de "
                  "activeringsenergie."),
            ("p", "Bij een <strong>exo-energetische</strong> reactie (ook <strong>exotherm</strong>) "
                  "<strong>liggen de producten lager dan de reagentia</strong>: het teveel aan energie gaat "
                  "naar de omgeving en het mengsel voelt <strong>warm</strong> aan. Bij een "
                  "<strong>endo-energetische</strong> reactie (<strong>endotherm</strong>) "
                  "<strong>neemt de reactie energie uit de omgeving op</strong>, hebben de "
                  "<strong>producten meer inwendige energie dan de reagentia</strong> en "
                  "<strong>koelt de omgeving af</strong>. Ook een endo-energetische reactie "
                  "<strong>heeft een activeringsenergie nodig</strong>."),
            ("p", "Een reactie met een <strong>hoge activeringsenergie</strong> verloopt bij "
                  "<strong>kamertemperatuur meestal traag</strong>, want weinig deeltjes raken over de "
                  "berg. Daarom moet je zo'n reactie vaak opwarmen om ze te zien gebeuren. Op een "
                  "energiediagram lees je trouwens enkel de <strong>activeringsenergie</strong> en de "
                  "<strong>reactie-energie</strong> af: tijd en concentratie staan er niet op."),
        ]),
        dict(kop="Katalysatoren en de Boltzmannverdeling", blokken=[
            ("p", "Een <strong>katalysator verlaagt de activeringsenergie</strong> van de reactie. Door de "
                  "lagere berg hebben meer botsingen genoeg energie, dus gaat de reactie sneller. Hoeveel "
                  "product er komt, verandert niet: <strong>een katalysator wordt tijdens de reactie niet "
                  "opgebruikt</strong>, want hij doet mee aan tussenstappen maar komt er achteraf "
                  "onveranderd uit. Daarom kan een kleine hoeveelheid heel lang blijven werken."),
            ("p", "Op het energiediagram <strong>ligt de top met een katalysator lager</strong>, terwijl de "
                  "<strong>energie van de reagentia</strong> en de <strong>energie van de producten "
                  "dezelfde blijven</strong>. Dus <strong>verandert een katalysator de reactie-energie "
                  "niet</strong>; enkel de activeringsenergie wordt kleiner."),
            ("p", "Een <strong>biokatalysator</strong> is een katalysator die in een levend organisme "
                  "werkt. Dat zijn de <strong>enzymen</strong>: proteïnen die een reactie in het lichaam "
                  "versnellen. Ze zijn belangrijk omdat ze <strong>reacties bij lichaamstemperatuur snel "
                  "genoeg laten verlopen</strong>; opwarmen is in een cel geen optie, dus moet de berg "
                  "lager. Daarom heeft bijna elke reactie in het lichaam haar eigen enzym."),
            ("p", "Een <strong>Boltzmannverdeling</strong> zet de <strong>kinetische energie van de "
                  "deeltjes</strong> op de horizontale as en het aantal deeltjes met die energie op de "
                  "verticale. De activeringsenergie zet je als een streep op die as: alles rechts daarvan "
                  "kan reageren. Een reactie gaat dus sneller als <strong>er een groter deel van de "
                  "deeltjes rechts van de activeringsenergie ligt</strong>."),
            ("p", "Bij een <strong>hogere temperatuur schuift de top naar rechts en wordt ze lager en "
                  "breder</strong>: de energie is over een breder gebied verspreid, en daardoor ligt er een "
                  "veel groter deel van de oppervlakte rechts van de activeringsenergie. Een "
                  "<strong>katalysator zet de streep van de activeringsenergie naar links</strong>, zodat "
                  "<strong>meer deeltjes genoeg energie hebben om te reageren</strong>; de verdeling van de "
                  "deeltjes zelf blijft daarbij gelijk."),
            ("kader", "Verloopt een proef te traag en mag je <strong>niet opwarmen</strong>, dan blijven er "
                      "drie factoren over: <strong>een katalysator toevoegen of de stof fijner "
                      "verdelen</strong>, of de concentratie verhogen."),
        ]),
    ],
    onthoud=[
        "Reactiesnelheid is de verandering van een concentratie per tijdseenheid.",
        "Alleen een effectieve botsing leidt tot een reactie: genoeg energie én de juiste kant.",
        "Hoe steiler de lijn op een concentratie-tijdgrafiek, hoe sneller de reactie; vlak betekent afgelopen of in evenwicht.",
        "Vier factoren: verdelingsgraad, temperatuur (of licht), concentratie en katalysator.",
        "De verdelingsgraad verandert alleen de snelheid, niet de opbrengst.",
        "Activeringsenergie is de hoogte van de berg boven de reagentia; reactie-energie is het verschil tussen producten en reagentia.",
        "Exo-energetisch: producten liggen lager dan de reagentia. Endo-energetisch: producten hebben meer inwendige energie.",
        "Een katalysator verlaagt de activeringsenergie, wordt niet opgebruikt en verandert de reactie-energie niet.",
        "Enzymen zijn biokatalysatoren: ze laten reacties bij lichaamstemperatuur snel genoeg verlopen.",
    ],
)

# ───────────────────────── 1. De cel
BUNDELS["de-cel-organellen-membranen-en-weefsels-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="De cel: organellen, membranen en weefsels",
    onder="Van organisatieniveau tot organel, van membraan tot weefsel: hoe de bouw van een cel haar taak verklaart.",
    secties=[
        dict(kop="De biologische organisatieniveaus", blokken=[
            ("p", "Een organisme is opgebouwd in <strong>organisatieniveaus</strong> die van klein naar "
                  "groot lopen: molecule, organel, cel, weefsel, orgaan, <strong>orgaanstelsel</strong>, "
                  "organisme. Het niveau dat <strong>meteen boven het orgaan</strong> komt, is dus het "
                  "<strong>orgaanstelsel</strong>: verschillende organen die samen één grote taak uitvoeren, "
                  "zoals het spijsverteringsstelsel."),
            ("p", "Bij elk niveau geldt dezelfde rode draad van dit thema: de "
                  "<strong>bouw past bij de functie</strong>. Wie weet hoe iets gebouwd is, kan raden wat "
                  "het doet, en omgekeerd."),
        ]),
        dict(kop="Prokaryoot en eukaryoot", blokken=[
            ("p", "Een <strong>prokaryote cel</strong>, zoals een <strong>bacterie</strong>, heeft geen "
                  "kernmembraan: haar <strong>DNA ligt vrij in het cytoplasma</strong>. Ze heeft wel "
                  "<strong>ribosomen</strong> waarmee ze <strong>eiwitten aanmaakt</strong>, en ze is "
                  "<strong>omgeven door een celmembraan</strong>. Wat ze niet heeft, zijn de organellen met "
                  "een eigen membraan: geen kern, geen mitochondriën, geen Golgi-apparaat."),
            ("p", "Een <strong>eukaryote cel</strong> heeft die membraanorganellen wel. Plantaardige en "
                  "dierlijke cellen zijn beide eukaryoot, maar ze zijn niet gelijk. "
                  "<strong>Wel in een plantaardige cel en niet in een dierlijke</strong>: een "
                  "<strong>celwand van cellulose</strong>, <strong>chloroplasten</strong> en een "
                  "<strong>grote centrale vacuole</strong>. Het centrosoom vind je omgekeerd bij dieren wel "
                  "en bij de meeste planten niet."),
            ("p", "De <strong>celwand van een plantencel</strong> is <strong>hoofdzakelijk uit "
                  "cellulose</strong> opgebouwd. <strong>Ook bacteriën hebben een celwand, maar die is niet "
                  "uit cellulose opgebouwd</strong>: bij hen bestaat ze uit andere ketens, en net daarop "
                  "grijpen sommige antibiotica in."),
        ]),
        dict(kop="De organellen en hun taak", blokken=[
            ("p", tabel(["Organel", "Taak"], [
                ["Celkern", "bewaart het DNA achter een kernmembraan"],
                ["Kernlichaampje", "maakt de ribosomen aan"],
                ["Ribosoom", "zet aminozuren aan elkaar tot een eiwit"],
                ["Ruw endoplasmatisch reticulum", "dankt zijn naam aan de ribosomen die erop vastzitten; eiwitten gaan er binnen"],
                ["Glad endoplasmatisch reticulum", "speelt een rol bij de aanmaak van vetten en het ontgiften van stoffen"],
                ["Golgi-apparaat", "rijpt, sorteert en verpakt eiwitten voor de uitvoer naar buiten"],
                ["Lysosoom", "ruimt versleten organellen op en verteert ze"],
                ["Mitochondrion", "de energiecentrale: hier gebeurt de aerobe celademhaling grotendeels"],
                ["Chloroplast", "vangt licht op voor de fotosynthese"],
                ["Vacuole", "een blaasje-achtige structuur die bij een rijpe plantencel het grootste deel van het volume inneemt en vocht en stoffen opslaat"],
                ["Centrosoom met centriolen", "legt de trekdraden voor de celdeling aan"],
            ])),
            ("p", "Een <strong>eiwit voor de uitvoer naar buiten</strong> volgt dus een vaste weg: ribosoom "
                  "op het ruw ER, daarna het <strong>Golgi-apparaat</strong>, en van daar in een blaasje "
                  "naar het celmembraan."),
            ("p", "<strong>Plastiden</strong> zijn de familie waartoe de chloroplast hoort. "
                  "<strong>Chromoplasten</strong> (met gele, oranje en rode pigmenten) en "
                  "<strong>amyloplasten</strong> (met zetmeel) horen er ook bij, en ze "
                  "<strong>komen enkel bij planten voor, niet bij dieren</strong>."),
            ("p", "Het <strong>cytoskelet</strong> is het geheel van <strong>microtubuli, "
                  "microfilamenten en intermediaire filamenten</strong> dat de cel haar "
                  "<strong>vorm en stevigheid</strong> geeft en waarlangs organellen zich verplaatsen."),
        ]),
        dict(kop="Het celmembraan", blokken=[
            ("p", "De grondlaag van <strong>elk biologisch membraan</strong> is een "
                  "<strong>dubbellaag van fosfolipiden</strong>: de waterminnende koppen naar buiten, de "
                  "waterafstotende staarten naar binnen. Daarin zitten nog andere stoffen "
                  "<strong>ingebouwd</strong>: <strong>cholesterol</strong>, dat het membraan soepel maar "
                  "stevig houdt, <strong>transmembraaneiwitten</strong> die als poort of pomp dienen, en "
                  "<strong>perifere herkenningseiwitten</strong> aan de buitenkant."),
            ("p", "Een membraan is <strong>semi-permeabel</strong> of halfdoorlatend. Dat betekent niet dat "
                  "het alles doorlaat: een <strong>semi-permeabel membraan laat niet alle stoffen even vlot "
                  "door</strong>. Kleine, apolaire moleculen glippen er zo door, grote en geladen deeltjes "
                  "hebben een eiwitpoort nodig."),
            ("p", "Legt men een <strong>plantencel in zuiver water</strong>, dan trekt het water naar binnen, "
                  "waar de concentratie aan opgeloste stoffen hoger is: de <strong>cel neemt water op en "
                  "wordt stevig of turgescent</strong>. De celwand houdt haar daarbij tegen, zodat ze niet "
                  "openbarst zoals een dierlijke cel zou doen."),
            ("weetje", "De <strong>verhouding tussen oppervlakte en volume</strong> zet een grens op de "
                       "grootte van een cel: <strong>een grote cel heeft per eenheid volume te weinig "
                       "membraan om stoffen uit te wisselen</strong>. Verdubbel je de straal, dan wordt het "
                       "oppervlak vier keer groter maar het volume acht keer. Daarom blijven cellen klein en "
                       "worden organismen groot door méér cellen te maken."),
        ]),
        dict(kop="Plantaardige weefsels", blokken=[
            ("p", "Cellen van hetzelfde type vormen samen een <strong>weefsel</strong>, en elk weefsel heeft zijn eigen celtypes. Bij een plant deelt "
                  "men ze in vier groepen in: huidweefsel, grondweefsel, steunweefsel en vaatweefsel."),
            ("p", "Bij het <strong>huidweefsel</strong> horen de <strong>epidermis</strong>, de "
                  "<strong>waslaag of cuticula</strong> en de <strong>rhizodermis met wortelharen</strong>. "
                  "De <strong>cuticula</strong> is het <strong>buitenste waslaagje op een blad dat het "
                  "waterverlies beperkt</strong>. <strong>Wortelharen vergroten het oppervlak waarmee de "
                  "wortel water en mineralen opneemt</strong>, precies dezelfde truc als de darmvlokken bij "
                  "een dier."),
            ("p", "Bij het <strong>grondweefsel</strong> van een blad horen het "
                  "<strong>palissadeparenchym</strong>, het <strong>sponsparenchym</strong> en het "
                  "<strong>steunweefsel</strong>. De cellen van het <strong>palissadeparenchym</strong> "
                  "staan <strong>dicht tegen elkaar onder de bovenkant van het blad, omdat daar het meeste "
                  "licht binnenvalt voor de fotosynthese</strong>. Het sponsparenchym eronder zit juist vol "
                  "luchtholtes voor de gassen."),
            ("p", "Het <strong>vaatweefsel</strong> bestaat uit twee delen. Het "
                  "<strong>xyleem of houtvatenweefsel vervoert water en opgeloste mineralen van de wortel "
                  "naar het blad</strong>. Het <strong>floëem vervoert de suikers niet uitsluitend van "
                  "boven naar beneden</strong>: het transport gaat naar waar de plant de suiker nodig heeft, "
                  "dus in het voorjaar ook van een wortelknol naar de ontluikende knoppen."),
            ("p", "In een wortel vervult de <strong>schors of cortex</strong> de taak van "
                  "<strong>opslag en transport van stoffen tussen de huid en de vaatbundel</strong>."),
        ]),
        dict(kop="Huidmondjes", blokken=[
            ("p", "De <strong>huidmondjes</strong> op een blad <strong>regelen de gasuitwisseling en de "
                  "waterafgifte</strong>. Ze liggen <strong>bij een gewoon blad vooral aan de onderkant van "
                  "het blad</strong>, in de schaduw, waar het water minder snel verdampt. De twee cellen die "
                  "samen een huidmondje vormen en het <strong>openen en sluiten</strong>, zijn de "
                  "<strong>sluitcellen</strong>."),
            ("p", "Blijven de huidmondjes <strong>bij droogte lang gesloten</strong>, dan zijn er drie "
                  "gevolgen samen: <strong>er komt te weinig koolstofdioxide binnen</strong>, "
                  "<strong>de fotosynthese valt grotendeels stil</strong> en "
                  "<strong>de plant verliest veel minder waterdamp</strong>. Dat laatste is precies de "
                  "bedoeling; de plant kiest dorst boven uitdroging."),
        ]),
        dict(kop="Dierlijke weefsels", blokken=[
            ("p", "Bij dieren onderscheidt men vier grote weefselgroepen: "
                  "<strong>epitheel-, spier-, zenuw- en transportweefsel</strong>."),
            ("p", tabel(["Weefsel", "Bouw", "Functie"], [
                ["Epitheelweefsel", "cellen dicht naast elkaar in één of meer lagen", "bedekt en beschermt; het komt niet enkel in de huid voor, maar ook in de darm, de luchtwegen en de klieren"],
                ["Spierweefsel", "lange cellen met samentrekbare draden", "spiercellen zijn zo gebouwd dat ze zich kunnen samentrekken"],
                ["Zenuwweefsel", "een zenuwcel met een lange uitloper", "die uitloper doorgeeft prikkels over grote afstand"],
                ["Transportweefsel", "vloeistof met cellen erin", "vervoert bij dieren stoffen door het lichaam, met bloed als bekendste voorbeeld"],
            ])),
            ("p", "Twee cellen laten de regel bouw-past-bij-functie goed zien. Een "
                  "<strong>rijpe rode bloedcel van de mens heeft geen kern meer</strong>, waardoor er meer "
                  "plaats is voor hemoglobine. En bij een <strong>zaadcel maakt de staart ze beweeglijk "
                  "terwijl de kleine kop het erfelijk materiaal draagt</strong>. Een "
                  "<strong>eicel is veel groter dan een zaadcel omdat ze reservestoffen voor de eerste "
                  "delingen bevat</strong>."),
        ]),
    ],
    onthoud=[
        "Organisatieniveaus: molecule, organel, cel, weefsel, orgaan, orgaanstelsel, organisme.",
        "Een prokaryote cel heeft geen kernmembraan: haar DNA ligt vrij in het cytoplasma.",
        "Wel in een plantaardige cel, niet in een dierlijke: celwand van cellulose, chloroplasten, grote centrale vacuole.",
        "Een eiwit voor de uitvoer gaat van het ribosoom op het ruw ER naar het Golgi-apparaat en dan naar het celmembraan.",
        "Elk biologisch membraan is een dubbellaag van fosfolipiden en is semi-permeabel.",
        "Een plantencel in zuiver water neemt water op en wordt turgescent.",
        "Xyleem vervoert water en mineralen van wortel naar blad; floëem vervoert suikers naar waar de plant ze nodig heeft.",
        "Huidmondjes regelen de gasuitwisseling en de waterafgifte; sluitcellen openen en sluiten ze.",
        "Vier dierlijke weefselgroepen: epitheel-, spier-, zenuw- en transportweefsel.",
    ],
)

# ───────────────────────── 2. Fotosynthese en celademhaling
BUNDELS["fotosynthese-en-celademhaling-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Fotosynthese en celademhaling",
    onder="Hoe een cel energie vastlegt en weer vrijmaakt, van ATP over de chloroplast tot de gisting.",
    secties=[
        dict(kop="Autotroof en heterotroof", blokken=[
            ("p", "Een <strong>autotroof organisme bouwt zijn eigen organische stoffen uit anorganische "
                  "stoffen op</strong>: een plant maakt glucose uit koolstofdioxide en water. Een "
                  "<strong>heterotroof organisme</strong> moet die organische stoffen opeten. Een "
                  "<strong>schimmel is een heterotroof organisme</strong>, ook al groeit hij als een plant "
                  "op één plek."),
        ]),
        dict(kop="ATP, de energiemunt", blokken=[
            ("p", "Energie uit voedsel kan een cel niet rechtstreeks gebruiken. Daarom werkt ze met "
                  "<strong>ATP</strong>, de <strong>energiemunt van de cel</strong>: ze "
                  "<strong>geeft haar energie er in kleine, bruikbare porties mee rond</strong>."),
            ("p", "In het <strong>ATP-ADP-systeem geeft ATP een fosfaatgroep af en wordt het ADP, en "
                  "omgekeerd</strong>. Bij het afsplitsen komt energie vrij, bij het aanhechten wordt "
                  "energie vastgelegd. Zo gaat hetzelfde molecule honderden keren per dag heen en weer: "
                  "een <strong>cel kan ATP niet in grote voorraad opslaan voor later gebruik</strong>, ze "
                  "maakt het aan op het moment dat ze het nodig heeft."),
            ("p", "<strong>ATP levert de energie</strong> voor onder meer de "
                  "<strong>spiercontractie</strong>, de <strong>zenuwimpulsgeleiding</strong> en de "
                  "<strong>synthese van biomoleculen</strong>."),
            ("p", "Een reactie waarbij er <strong>energie vrijkomt</strong>, zoals de celademhaling, heet "
                  "<strong>exo-energetisch</strong>. Een reactie die energie opneemt, heet "
                  "endo-energetisch."),
        ]),
        dict(kop="De fotosynthese", blokken=[
            ("p", "De fotosynthese legt lichtenergie vast in glucose. De reactievergelijking is "
                  "<strong>6 CO2 + 6 H2O geeft C6H12O6 + 6 O2</strong>. Omdat er energie in opgeslagen "
                  "wordt, is de <strong>fotosynthese een endo-energetische reactie</strong>."),
            ("p", "Ze loopt in twee stappen in de chloroplast. De <strong>lichtreacties</strong> lopen "
                  "<strong>in het thylakoïdmembraan</strong>, de donkerreacties in het "
                  "<strong>stroma</strong>, de <strong>kleurloze vloeistof in de chloroplast</strong>."),
            ("p", "De <strong>lichtreactie levert voor de donkerreactie</strong> drie dingen op: "
                  "<strong>ATP</strong>, <strong>energierijke waterstofdragers</strong> en "
                  "<strong>zuurstofgas als nevenproduct</strong>. Die zuurstof komt vrij doordat "
                  "<strong>water tijdens de lichtreactie gesplitst wordt</strong>."),
            ("p", "De naam donkerreactie is misleidend: de <strong>donkerreactie kan niet alleen in "
                  "volledige duisternis plaatsvinden</strong>. Ze heeft geen licht nodig, maar ze loopt "
                  "juist het best terwijl de lichtreactie ernaast ATP aanlevert."),
            ("p", "Het groene pigment dat het licht opvangt, is het <strong>chlorofyl</strong>. Een plant "
                  "kan <strong>met uitsluitend groen licht nauwelijks aan fotosynthese doen, omdat chlorofyl "
                  "groen licht grotendeels weerkaatst in plaats van opneemt</strong>; net daarom zien we het "
                  "blad groen. <strong>Naast chlorofyl bevat een blad nog andere pigmenten die licht "
                  "opvangen</strong>, zoals de carotenoïden die in de herfst zichtbaar worden."),
            ("p", "Een blad is helemaal op fotosynthese gebouwd: een <strong>plat, breed oppervlak dat veel "
                  "licht opvangt</strong>, <strong>palissadecellen vol chloroplasten onder de "
                  "bovenzijde</strong> en <strong>huidmondjes die koolstofdioxide binnenlaten</strong>."),
            ("p", "<strong>Blijft de lichtsterkte stijgen</strong>, dan <strong>stijgt de snelheid van de "
                  "fotosynthese eerst mee en loopt ze daarna tegen een grens aan</strong>: een andere factor, "
                  "zoals de hoeveelheid koolstofdioxide, wordt dan de rem. De suikers die de plant "
                  "overhoudt, <strong>bewaart ze als zetmeel</strong>."),
        ]),
        dict(kop="De celademhaling", blokken=[
            ("p", "Een <strong>plant doet niet alleen aan fotosynthese</strong>: ze doet ook aan "
                  "celademhaling, dag en nacht. <strong>Fotosynthese en celademhaling hangen samen doordat "
                  "de producten van de ene de grondstoffen van de andere zijn</strong>."),
            ("p", "De reactievergelijking van de <strong>aerobe celademhaling</strong> is "
                  "<strong>C6H12O6 + 6 O2 geeft 6 CO2 + 6 H2O en energie</strong>. Er komt dus "
                  "<strong>koolstofdioxide vrij bij de aerobe celademhaling</strong>."),
            ("p", "Ze verloopt in twee plaatsen. De <strong>glycolyse</strong> is de "
                  "<strong>reeks van reacties die glucose in het cytoplasma afbreekt tot twee moleculen "
                  "pyrodruivenzuur</strong>. Het <strong>pyrodruivenzuur</strong> gaat bij voldoende "
                  "zuurstof het <strong>mitochondrion</strong> in. De "
                  "<strong>glycolyse levert veel minder ATP op dan de reacties in het mitochondrion</strong>, "
                  "en niet omgekeerd: het grote werk gebeurt in het mitochondrion."),
        ]),
        dict(kop="Gisting", blokken=[
            ("p", "Is er te weinig zuurstof, dan blijft de glycolyse lopen en moet het pyrodruivenzuur "
                  "elders naartoe. In een <strong>spiercel bij intense inspanning wordt het "
                  "pyrodruivenzuur tot melkzuur omgezet</strong>. Het ophopen van dat melkzuur tijdens "
                  "zware inspanning heet de <strong>verzuring</strong> van de spieren."),
            ("p", "Voor de <strong>melkzuurgisting</strong> geldt: ze <strong>loopt zonder "
                  "zuurstof</strong>, ze <strong>gebeurt in het cytoplasma</strong> en ze "
                  "<strong>levert veel minder energie op dan de aerobe ademhaling</strong>. "
                  "<strong>Melkzuurbacteriën worden gebruikt om yoghurt van melk te maken</strong>."),
            ("p", "De <strong>alcoholische gisting van glucose</strong> levert <strong>ethanol</strong>, "
                  "<strong>koolstofdioxide</strong> en <strong>een kleine hoeveelheid energie</strong> op. "
                  "Laat een <strong>gistcultuur in suikerwater belletjes opborrelen</strong>, dan is dat gas "
                  "<strong>koolstofdioxide</strong>."),
            ("p", "<strong>Gisting levert veel minder energie op dan de aerobe celademhaling, omdat de "
                  "glucose maar gedeeltelijk afgebroken wordt</strong>: in melkzuur en in ethanol zit nog "
                  "een hoop energie die de cel laat liggen."),
        ]),
        dict(kop="Transport in de plant en twee proeven", blokken=[
            ("p", "Het transport van stoffen in een plant gebeurt door <strong>het xyleem voor water en "
                  "mineralen</strong>, <strong>het floëem voor opgeloste suikers</strong> en "
                  "<strong>de vaatbundel waarin beide samen liggen</strong>. Met "
                  "<strong>opwaarts transport</strong> bedoelt men het <strong>vervoer van water en "
                  "mineralen van de wortel naar het blad</strong>. De "
                  "<strong>verdamping in de bladeren helpt het water in de houtvaten omhoog te "
                  "trekken</strong>, als een zuigende draad."),
            ("p", "Twee klassieke proeven. Bij een experiment over fotosynthese zet men "
                  "<strong>een plant eerst een nacht in het donker om het aanwezige zetmeel uit de bladeren "
                  "te laten verdwijnen</strong>; anders weet je niet of het zetmeel van de proef komt. "
                  "Daarna toont men <strong>zetmeel in een blad aan met joodoplossing</strong>, die "
                  "blauwzwart kleurt."),
        ]),
    ],
    onthoud=[
        "Een autotroof organisme bouwt organische stoffen op uit anorganische; een schimmel is heterotroof.",
        "ATP is de energiemunt van de cel: het geeft een fosfaatgroep af en wordt ADP.",
        "Fotosynthese: 6 CO2 + 6 H2O geeft C6H12O6 + 6 O2, een endo-energetische reactie.",
        "De lichtreacties lopen in het thylakoïdmembraan, de donkerreacties in het stroma.",
        "De zuurstof komt vrij doordat water tijdens de lichtreactie gesplitst wordt.",
        "Aerobe celademhaling: C6H12O6 + 6 O2 geeft 6 CO2 + 6 H2O en energie.",
        "De glycolyse in het cytoplasma levert veel minder ATP op dan de reacties in het mitochondrion.",
        "Gisting levert weinig energie, omdat de glucose maar gedeeltelijk afgebroken wordt.",
        "Zetmeel in een blad toon je aan met joodoplossing, die blauwzwart kleurt.",
    ],
)

# ───────────────────────── 3. Bescherming en afweer
BUNDELS["bescherming-en-afweer-tegen-lichaamsvreemde-stoffen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Bescherming en afweer tegen lichaamsvreemde stoffen",
    onder="Drie verdedigingslijnen, de cellen die het werk doen, en waarom een vaccin werkt.",
    secties=[
        dict(kop="Waarom afweer nodig is", blokken=[
            ("p", "Het <strong>immuunsysteem is noodzakelijk om te overleven, omdat we voortdurend in "
                  "contact komen met ziekteverwekkers</strong>: in de lucht, in het eten, op elke deurklink. "
                  "Een <strong>pathogeen is een organisme dat ziekte kan veroorzaken</strong>. Een "
                  "<strong>antigeen</strong> is iets anders: een <strong>lichaamsvreemde stof die een "
                  "afweerreactie uitlokt</strong>, bijvoorbeeld een eiwit op de buitenkant van zo'n kiem."),
            ("p", "Het <strong>verschil tussen een infectie en een infectieziekte</strong>: "
                  "<strong>bij een infectie dringt de kiem binnen, bij een infectieziekte maakt hij ook "
                  "ziek</strong>. Veel infecties ruimt het lichaam op zonder dat je er iets van merkt."),
        ]),
        dict(kop="De eerste verdedigingslijn", blokken=[
            ("p", "De eerste lijn houdt indringers buiten. Daarbij horen de "
                  "<strong>opperhuid als fysische barrière</strong>, de <strong>zuurmantel en de talg op de "
                  "huid</strong> en <strong>lysozym in traanvocht en speeksel</strong>, een enzym dat "
                  "bacteriën aantast. Ook <strong>slijmvliezen horen bij de eerste "
                  "verdedigingslijn</strong>, met hun kleverige laag en hun trilhaartjes."),
            ("p", "Het <strong>microbioom</strong> is het <strong>geheel van micro-organismen dat van "
                  "nature op onze huid en in onze darm leeft</strong> en ons mee beschermt: die bewoners "
                  "nemen de plaats en het voedsel in waar een indringer zich zou willen vestigen."),
        ]),
        dict(kop="De niet-specifieke afweer", blokken=[
            ("p", "Raakt een kiem toch binnen, dan komt de <strong>niet-specifieke afweer</strong> in "
                  "actie. Die <strong>werkt tegen elke indringer op dezelfde manier</strong> en start "
                  "onmiddellijk: dringt <strong>een bacterie door een wonde binnen, dan komt de "
                  "niet-specifieke afweer meteen op gang</strong>."),
            ("p", tabel(["Cel of stof", "Wat ze doet"], [
                ["Fagocyt", "omsluit een indringer en verteert hem; dat heet fagocytose"],
                ["Macrofaag", "een grote fagocyt; na het verteren toont hij een stukje van de bacterie op zijn membraan"],
                ["Dendritische cel", "toont een stuk van de indringer aan de lymfocyten"],
                ["Mestcel", "geeft histamine af, waardoor de bloedvaten verwijden en er een ontsteking ontstaat"],
                ["Natural killer cel", "doorboort geïnfecteerde en kwaadaardige lichaamscellen"],
            ])),
            ("p", "Bij een <strong>ontsteking</strong> horen <strong>roodheid</strong>, "
                  "<strong>zwelling</strong> en <strong>warmte</strong>, en ook pijn. Dat lijkt hinder, maar "
                  "het is afweer: er stroomt meer bloed met meer afweercellen naartoe. Zo is ook "
                  "<strong>koorts niet altijd schadelijk</strong>: een hogere temperatuur remt veel kiemen af "
                  "en zet het eigen afweersysteem aan. Pas heel hoge of lang aanhoudende koorts is "
                  "gevaarlijk."),
            ("p", "<strong>Antigeenpresentatie</strong> is het <strong>tonen van een stukje van de "
                  "indringer op het membraan</strong>, waardoor de <strong>specifieke afweer kan "
                  "starten</strong>. Daar sluit de eerste lijn op de derde aan."),
        ]),
        dict(kop="Het lymfatisch systeem", blokken=[
            ("p", "Bij het <strong>lymfatisch systeem</strong> horen de <strong>thymus</strong>, de "
                  "<strong>milt</strong> en de <strong>lymfeknopen</strong>. De "
                  "<strong>lymfeknopen</strong> zijn de <strong>knooppunten in de lymfevaten waar "
                  "afweercellen samenkomen</strong>; bij een infectie <strong>kunnen ze "
                  "opzwellen</strong>, zoals de bultjes in je hals bij een keelontsteking."),
            ("p", "De <strong>witte bloedcellen worden in het rode beenmerg aangemaakt</strong>. "
                  "<strong>T-lymfocyten rijpen in de thymus, en daar komt hun letter vandaan</strong>; de "
                  "B van B-lymfocyt verwijst naar het beenmerg."),
            ("p", "<strong>Lymfe stroomt niet in gesloten kring rond zoals het bloed</strong>: ze begint in "
                  "de weefsels, loopt in één richting door de lymfevaten en mondt bij het hart in het bloed "
                  "uit. Er is dus geen lymfepomp; spierbewegingen duwen haar vooruit."),
        ]),
        dict(kop="De specifieke afweer", blokken=[
            ("p", "De <strong>specifieke afweer</strong> richt zich op één bepaald antigeen. Daarbij horen "
                  "de <strong>B-lymfocyten</strong>, de <strong>T-helperlymfocyten</strong> en de "
                  "<strong>cytotoxische T-lymfocyten</strong>."),
            ("p", "Een <strong>T-helperlymfocyt zet andere afweercellen met signaalstoffen aan het "
                  "werk</strong>. Die signaalstoffen waarmee afweercellen elkaar aansturen, heten "
                  "<strong>cytokines</strong>. Een <strong>cytotoxische T-lymfocyt brengt een besmette "
                  "lichaamscel tot afsterven</strong>, want een virus binnen een cel kan je niet met "
                  "antistoffen bereiken."),
            ("p", "<strong>B-lymfocyten maken antistoffen die op één bepaald antigeen passen</strong>, als "
                  "een sleutel op één slot. Die <strong>antistoffen binden op het antigeen</strong> van de "
                  "ziekteverwekker, <strong>klitten ziekteverwekkers samen</strong> en "
                  "<strong>maken hem herkenbaar voor fagocyten</strong>."),
            ("p", "De <strong>secundaire immuunrespons verloopt sneller en sterker dan de primaire</strong>, "
                  "en dat komt door het <strong>afweergeheugen</strong>, dat berust "
                  "<strong>op B- en T-geheugenlymfocyten die jaren blijven leven</strong>."),
        ]),
        dict(kop="Immunisatie", blokken=[
            ("p", "<strong>Immunisatie</strong> is het <strong>verwerven van bescherming tegen een bepaalde "
                  "ziekteverwekker</strong>. Men deelt ze in twee richtingen in: actief of passief, "
                  "natuurlijk of kunstmatig."),
            ("p", tabel(["", "Natuurlijk", "Kunstmatig"], [
                ["Actief: je maakt zelf antistoffen", "je maakt de mazelen door en bent daarna beschermd", "vaccinatie"],
                ["Passief: je krijgt antistoffen van elders", "antistoffen die een baby via de borstvoeding krijgt", "serumtherapie met kant-en-klare antistoffen"],
            ])),
            ("p", "Voor <strong>actieve immunisatie</strong> geldt: <strong>het lichaam maakt zelf "
                  "antistoffen aan</strong>, <strong>er ontstaat een afweergeheugen</strong> en "
                  "<strong>de bescherming houdt lang aan</strong>. <strong>Passieve immunisatie bouwt geen "
                  "afweergeheugen op dat jaren meegaat</strong>: de geleende antistoffen zijn na enkele "
                  "weken afgebroken, en dan ben je weer even kwetsbaar als voordien. Daarom is serumtherapie "
                  "een noodoplossing en geen vaccin."),
            ("p", "<strong>Vaccinatie</strong> is het <strong>kunstmatig toedienen van een verzwakte of "
                  "onschadelijk gemaakte ziekteverwekker om het afweergeheugen op te bouwen</strong>. Een "
                  "<strong>vaccinatiecampagne beschermt ook mensen die zelf niet gevaccineerd zijn, omdat de "
                  "ziekteverwekker veel minder kans krijgt om zich te verspreiden</strong>: hij komt te "
                  "weinig geschikte gastheren tegen om een ketting te vormen."),
            ("kader", "<strong>Antibiotica werken niet even goed tegen virussen als tegen "
                      "bacteriën.</strong> Ze grijpen in op dingen die alleen een bacterie heeft, zoals haar "
                      "celwand. Een virus heeft die niet, dus helpt een antibioticum bij griep of een "
                      "verkoudheid niets."),
        ]),
    ],
    onthoud=[
        "Een pathogeen kan ziekte veroorzaken; een antigeen is een lichaamsvreemde stof die een afweerreactie uitlokt.",
        "Bij een infectie dringt de kiem binnen, bij een infectieziekte maakt hij ook ziek.",
        "Eerste verdedigingslijn: opperhuid, zuurmantel en talg, lysozym en slijmvliezen.",
        "De niet-specifieke afweer werkt tegen elke indringer op dezelfde manier en start onmiddellijk.",
        "Bij een ontsteking horen roodheid, zwelling, warmte en pijn.",
        "Witte bloedcellen worden in het rode beenmerg aangemaakt; T-lymfocyten rijpen in de thymus.",
        "B-lymfocyten maken antistoffen die op één bepaald antigeen passen.",
        "De secundaire immuunrespons verloopt sneller en sterker dankzij B- en T-geheugenlymfocyten.",
        "Actieve immunisatie bouwt een afweergeheugen op, passieve immunisatie niet.",
    ],
)

# ───────────────────────── 4. Voortplanting, zwangerschap en vruchtbaarheid
BUNDELS["voortplanting-zwangerschap-en-vruchtbaarheid-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Voortplanting, zwangerschap en vruchtbaarheid",
    onder="Van bevruchting tot geboorte, en wat de vruchtbaarheid helpt of hindert.",
    secties=[
        dict(kop="De bevruchting", blokken=[
            ("p", "In het vrouwelijk voortplantingsstelsel <strong>gebeurt de bevruchting normaal in de eileider</strong>, "
                  "niet in de baarmoeder. "
                  "Een <strong>eicel kan bevrucht worden rond de eisprong, ongeveer in het midden van de "
                  "menstruele cyclus</strong>: ze blijft maar ongeveer een dag levensvatbaar, terwijl "
                  "zaadcellen enkele dagen kunnen overleven."),
            ("p", "Een zaadcel moet drie <strong>barrières overwinnen op weg naar de eicel</strong>: "
                  "<strong>het zure milieu van de vagina</strong>, <strong>het slijm van de "
                  "baarmoederhals</strong> en <strong>de corona radiata rond de eicel</strong>. Van de "
                  "miljoenen vertrokken zaadcellen raken er maar enkele honderden tot bij de eicel."),
            ("p", "Het <strong>acrosoom</strong> is het <strong>blaasje vooraan op de kop van een "
                  "zaadcel</strong> dat de <strong>enzymen bevat om door de eihulzen te dringen</strong>. "
                  "Zodra één zaadcel binnen is, volgt de <strong>corticale reactie</strong>, die "
                  "<strong>belet dat er nog een tweede zaadcel binnendringt</strong>; de eihuls wordt "
                  "ondoordringbaar."),
            ("p", "<strong>Amfimixie</strong> is het <strong>samensmelten van de kern van de zaadcel met die "
                  "van de eicel</strong>. Daarna is <strong>de zygote diploïd en bevat ze erfelijk materiaal "
                  "van beide ouders</strong>."),
        ]),
        dict(kop="De eerste dagen", blokken=[
            ("p", "De <strong>klievingsdelingen</strong> zijn de eerste delingen van de zygote, "
                  "<strong>waarbij de cellen wel talrijker maar niet groter worden</strong>: de bal blijft "
                  "even groot en bestaat alleen uit steeds meer, steeds kleinere cellen."),
            ("p", "De volgorde van de eerste dagen is: <strong>zygote, morula, blastula, "
                  "innesteling</strong>. De <strong>innesteling gebeurt in de wand van de "
                  "baarmoeder</strong>, ongeveer een week na de bevruchting."),
            ("p", "In de <strong>blastula</strong> onderscheidt men twee delen: de "
                  "<strong>embryoblast of kiemknop</strong>, waaruit het kind zelf groeit, en de "
                  "<strong>trofoblast</strong>, waaruit de placenta ontstaat. De trofoblast maakt "
                  "<strong>hCG</strong> aan, het hormoon <strong>waardoor een zwangerschapstest positief "
                  "wordt</strong>."),
            ("p", "In de eierstok blijft intussen het <strong>geel lichaam</strong> achter: het "
                  "<strong>ontstaat uit de resten van het gesprongen follikel</strong> en houdt met zijn "
                  "hormonen het baarmoederslijmvlies in stand."),
        ]),
        dict(kop="Embryonaal en foetaal", blokken=[
            ("p", "De <strong>embryonale fase</strong> is de eerste acht weken. Daarin "
                  "<strong>worden de kiembladen aangelegd</strong>, worden "
                  "<strong>de organen voor het eerst gevormd</strong> en is "
                  "<strong>de vrucht het gevoeligst voor schadelijke stoffen</strong>: wie nog niet weet dat "
                  "ze zwanger is, zit precies in die kwetsbaarste weken."),
            ("p", "<strong>Organogenese</strong> is de naam voor de <strong>aanleg van de organen uit de "
                  "kiemschijf</strong>. <strong>Differentiatie</strong> is het proces "
                  "<strong>waarbij stamcellen zich tot gespecialiseerde celtypes ontwikkelen</strong>: "
                  "dezelfde genen, maar een andere keuze welke ervan aan gaan."),
            ("p", "Vanaf de negende week spreekt men van de <strong>foetale fase</strong>. Daarin "
                  "<strong>worden niet alle organen voor het eerst aangelegd</strong>: die liggen er al, en "
                  "ze groeien en rijpen nu verder. Ook de <strong>geslachtsorganen van de vrucht zijn niet al "
                  "vanaf de bevruchting volledig gevormd</strong>; het geslacht ligt wel genetisch vast, "
                  "maar de organen zelf ontwikkelen zich pas in de loop van de eerste maanden. Men beschouwt "
                  "een foetus <strong>vanaf ongeveer 24 weken zwangerschap</strong> als levensvatbaar."),
            ("p", "Het <strong>vruchtwater vangt schokken op</strong>, <strong>houdt de temperatuur "
                  "gelijk</strong> en <strong>laat de vrucht vrij bewegen</strong>, wat nodig is om spieren "
                  "en gewrichten te ontwikkelen."),
        ]),
        dict(kop="De placenta", blokken=[
            ("p", "De <strong>placenta geeft zuurstof en voedingsstoffen door</strong>, "
                  "<strong>voert afvalstoffen van de vrucht af</strong> en "
                  "<strong>maakt hormonen aan die de zwangerschap in stand houden</strong>."),
            ("p", "<strong>Het bloed van de moeder en dat van de vrucht mengen zich niet met elkaar in de "
                  "placenta</strong>. Ze stromen dicht langs elkaar, met een dun laagje ertussen waarover de "
                  "stoffen wisselen; daarom kunnen moeder en kind ook een verschillende bloedgroep hebben. "
                  "De <strong>navelstrengslagaders vervoeren zuurstofarm bloed van de vrucht naar de "
                  "placenta</strong>, de navelstrengvene het zuurstofrijke bloed terug."),
            ("p", "De <strong>selectieve placentabarrière</strong> is de eigenschap van de placenta dat ze "
                  "<strong>sommige stoffen wel en andere niet doorlaat</strong>. Ze is helaas geen muur: "
                  "alcohol, nicotine en veel medicijnen glippen er zonder moeite door."),
        ]),
        dict(kop="De geboorte", blokken=[
            ("p", "De fasen van de geboorte volgen op elkaar als "
                  "<strong>indaling, ontsluiting, uitdrijving, nageboorte</strong>. Tijdens de "
                  "<strong>ontsluiting verstrijkt de baarmoederhals en gaat hij open</strong>, tot ongeveer "
                  "tien centimeter. De <strong>nageboorte is het naar buiten komen van de placenta en de "
                  "vliezen</strong>."),
        ]),
        dict(kop="Wat de vrucht kan schaden", blokken=[
            ("p", "<strong>Gewoontes van de moeder die de ontwikkeling van de vrucht kunnen schaden</strong>: "
                  "<strong>alcohol drinken</strong>, <strong>roken</strong> en "
                  "<strong>medicijnen zonder advies innemen</strong>. Een stof die "
                  "<strong>bij een ongeboren kind afwijkingen kan veroorzaken</strong>, heet een "
                  "<strong>teratogeen</strong>."),
            ("p", "Het <strong>foetaal alcoholsyndroom</strong> is <strong>blijvende schade bij een kind "
                  "door alcoholgebruik tijdens de zwangerschap</strong>: kleinere groei, kenmerkende "
                  "gelaatstrekken en moeilijkheden met leren en concentratie. Er is geen hoeveelheid alcohol "
                  "waarvan men weet dat ze veilig is."),
            ("p", "Ook infecties spelen mee. Men raadt een zwangere vrouw aan "
                  "<strong>geen rauw vlees te eten en geen kattenbak te verschonen wegens het risico op "
                  "besmetting met de toxoplasmoseparasiet</strong>. En een "
                  "<strong>besmetting met het rubellavirus tijdens de zwangerschap kan afwijkingen bij de "
                  "vrucht veroorzaken</strong>, wat de reden is dat rubella in het vaccinatieschema zit."),
        ]),
        dict(kop="Anticonceptie en vruchtbaarheid", blokken=[
            ("p", "Een <strong>anticonceptiemethode</strong> belet een zwangerschap, en er zijn vier "
                  "soorten. De laatste, de sterilisatie, is een <strong>ingreep</strong> en dus niet "
                  "zomaar terug te draaien."),
            ("p", tabel(["Soort", "Voorbeeld", "Bijzonderheid"], [
                ["Hormonaal", "de combinatiepil", "belet de eisprong"],
                ["Mechanisch", "het mannencondoom en het vrouwencondoom", "de enige die ook tegen seksueel overdraagbare aandoeningen beschermen"],
                ["Natuurlijk", "de kalendermethode en de temperatuurmethode", "natuurlijke methoden zonder hormonen, maar minder betrouwbaar"],
                ["Blijvend", "sterilisatie", "de zaadleiders of de eileiders worden blijvend afgesloten"],
            ])),
            ("p", "Lukt zwanger worden niet, dan bestaan er technieken om te helpen. Bij "
                  "<strong>in-vitrofertilisatie gebeurt de bevruchting buiten het lichaam in het "
                  "laboratorium</strong>. <strong>ICSI verschilt daarvan doordat er één zaadcel rechtstreeks "
                  "in de eicel ingebracht wordt</strong>, wat helpt als de zaadcellen zelf niet sterk genoeg "
                  "zijn. Bij <strong>kunstmatige inseminatie gebeurt de bevruchting niet buiten het lichaam "
                  "in een schaaltje</strong>: het zaad wordt in de baarmoeder gebracht en de bevruchting "
                  "verloopt verder gewoon in de eileider."),
            ("p", "<strong>Factoren die de vruchtbaarheid van man of vrouw kunnen verminderen</strong>: "
                  "<strong>roken</strong>, <strong>zware stress over lange tijd</strong> en "
                  "<strong>overgewicht</strong>, naast leeftijd en bepaalde aandoeningen."),
        ]),
    ],
    onthoud=[
        "De bevruchting gebeurt normaal in de eileider, rond de eisprong.",
        "Na de amfimixie is de zygote diploïd en bevat ze erfelijk materiaal van beide ouders.",
        "Volgorde: zygote, morula, blastula, innesteling in de wand van de baarmoeder.",
        "De trofoblast maakt hCG aan, waardoor een zwangerschapstest positief wordt.",
        "De embryonale fase is de eerste acht weken; dan is de vrucht het gevoeligst voor schadelijke stoffen.",
        "Het bloed van de moeder en dat van de vrucht mengen zich niet in de placenta.",
        "Geboorte: indaling, ontsluiting, uitdrijving, nageboorte.",
        "Een teratogeen is een stof die bij een ongeboren kind afwijkingen kan veroorzaken.",
        "Alleen het mannen- en het vrouwencondoom beschermen ook tegen seksueel overdraagbare aandoeningen.",
    ],
)

# ───────────────────────── 5. DNA, replicatie en celdelingen
BUNDELS["dna-replicatie-en-celdelingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="DNA, replicatie en celdelingen",
    onder="Hoe het DNA gebouwd is, hoe het zich verdubbelt, en waarin mitose en meiose verschillen.",
    secties=[
        dict(kop="De bouwsteen", blokken=[
            ("p", "Een <strong>nucleotide</strong> bestaat uit drie delen: <strong>een suiker</strong>, "
                  "<strong>een fosfaatgroep</strong> en <strong>een stikstofbase</strong>. In een "
                  "<strong>DNA-nucleotide</strong> is die suiker <strong>desoxyribose</strong>; in RNA is "
                  "het ribose. De stikstofbase die <strong>wel in RNA voorkomt en niet in DNA</strong>, is "
                  "<strong>uracil</strong>; in DNA staat op die plaats thymine."),
            ("p", "De basen passen twee aan twee op elkaar. <strong>Adenine vormt in DNA een paar met "
                  "thymine</strong>, met twee waterstofbruggen ertussen. "
                  "<strong>Tussen guanine en cytosine liggen drie waterstofbruggen</strong>, en net daarom "
                  "is een stuk DNA met veel G en C steviger."),
            ("p", "Daaruit volgt de complementaire streng van elke reeks. Leest een DNA-streng "
                  "<strong>ATGC</strong>, dan luidt de andere streng <strong>TACG</strong>: elke A krijgt "
                  "een T, elke G een C."),
            ("p", "De regel van de basenparen laat ook een rekensom toe. Is <strong>30 procent van de basen "
                  "adenine</strong>, dan is er evenveel thymine, dus samen 60 procent. Voor guanine en "
                  "cytosine blijft 40 procent over, gelijk verdeeld: "
                  "<strong>20 procent cytosine</strong>."),
            ("p", "De twee strengen liggen <strong>antiparallel</strong>: <strong>de ene loopt van 5 naar 3 "
                  "en de andere in de omgekeerde richting</strong>. Ze worden "
                  "<strong>door waterstofbruggen bij elkaar gehouden</strong> tot een dubbele helix. Die "
                  "bruggen zijn elk zwak, maar met miljoenen samen stevig genoeg, en toch los te wikkelen."),
        ]),
        dict(kop="Van DNA tot chromosoom", blokken=[
            ("p", "In de celkern zit het DNA opgerold rond eiwitten, de <strong>histonen</strong>. Het losse "
                  "mengsel van DNA en eiwitten in een kern <strong>die niet aan het delen is</strong>, heet "
                  "<strong>chromatine</strong>. Pas bij een deling rolt het strak op tot een zichtbaar "
                  "chromosoom, dus <strong>zijn chromosomen niet in elke fase van de celcyclus even goed "
                  "zichtbaar onder de microscoop</strong>."),
            ("p", "Een cel <strong>kan haar DNA niet voortdurend sterk opgerold houden, omdat de genen dan "
                  "niet afgelezen kunnen worden</strong>: een strak opgerolde streng laat de "
                  "leesmachine niet toe."),
            ("p", "Over het <strong>centromeer</strong>: <strong>het is de insnoering van een "
                  "chromosoom</strong>, <strong>het houdt de zusterchromatiden samen</strong> en "
                  "<strong>er zit een kinetochoor op waaraan de trekdraden aangrijpen</strong>. De "
                  "<strong>zusterchromatiden</strong> zijn de <strong>twee identieke helften van een "
                  "gedupliceerd chromosoom die aan het centromeer vastzitten</strong>."),
            ("p", "Een <strong>menselijke lichaamscel is diploïd en bevat 46 chromosomen</strong>, dus 23 "
                  "paren. <strong>Homologe chromosomen</strong> zijn <strong>twee chromosomen van hetzelfde "
                  "paar, één van elke ouder</strong>. Het <strong>verschil tussen een autosoom en een "
                  "heterosoom</strong>: <strong>een autosoom is een lichaamschromosoom, een heterosoom "
                  "bepaalt het geslacht</strong>."),
            ("p", "Op een <strong>karyogram</strong>, een foto van alle chromosomen op een rij gelegd, lees "
                  "je <strong>het aantal chromosomen van een cel</strong>, <strong>het geslacht van de "
                  "persoon</strong> en <strong>een afwijkend aantal chromosomen</strong> af. Welk gen aan of "
                  "uit staat, zie je er niet op."),
            ("weetje", "Elk gen heeft een vaste plaats, een locus. Daarom "
                       "<strong>kan een gen niet bij de ene mens op het ene en bij de andere mens op een heel "
                       "ander chromosoom liggen</strong>: zonder die vaste plaats zou een genetische test "
                       "nergens iets kunnen terugvinden."),
        ]),
        dict(kop="De celcyclus en de replicatie", blokken=[
            ("p", "De <strong>interfase omvat de G1-, de S- en de G2-fase</strong>. Het "
                  "<strong>DNA wordt in de S-fase verdubbeld</strong>. De <strong>G0-fase</strong> staat "
                  "daarbuiten: dat is <strong>een rusttoestand waarin een cel niet meer deelt</strong>, zoals "
                  "een zenuwcel."),
            ("p", tabel(["Speler", "Taak bij de replicatie"], [
                ["Helicase", "wikkelt de dubbele helix open bij het begin van de replicatie"],
                ["Primer", "dient als startpunt waarop het polymerase verder kan bouwen"],
                ["DNA-polymerase", "zet nieuwe nucleotiden tegen de oude streng aan, leest die oude streng als sjabloon en werkt altijd in de richting van 5 naar 3"],
                ["Ligase", "plakt losse stukjes aan elkaar tot één doorlopende streng"],
            ])),
            ("p", "Omdat het polymerase maar in één richting kan werken en de strengen antiparallel liggen, "
                  "verloopt de ene streng vlot en de andere met horten en stoten. Voor die "
                  "<strong>lagging strand</strong> geldt: ze <strong>wordt in stukjes "
                  "opgebouwd</strong>, die <strong>stukjes heten Okazaki-fragmenten</strong> en "
                  "<strong>ligase plakt de stukjes aan elkaar</strong>."),
            ("p", "<strong>Na de replicatie bestaat elke dubbele helix uit één oude en één nieuwe "
                  "streng</strong>. Dat heet semi-conservatief, en het is de reden dat een fout bij het "
                  "kopiëren meteen in alle volgende generaties zit."),
        ]),
        dict(kop="De mitose", blokken=[
            ("p", "Het <strong>belang van de mitose</strong> is <strong>groei en herstel met cellen die "
                  "genetisch identiek zijn</strong>. De fasen volgen op elkaar als "
                  "<strong>profase, metafase, anafase, telofase</strong>."),
            ("p", "In de metafase gaan de chromosomen in het <strong>evenaarsvlak</strong> staan, het "
                  "<strong>vlak in het midden van de cel</strong>. Tijdens de "
                  "<strong>anafase worden de zusterchromatiden naar de polen getrokken</strong>. "
                  "<strong>De cytokinese is niet de deling van de kern</strong>, maar juist het splitsen van "
                  "het cytoplasma, na de kerndeling."),
        ]),
        dict(kop="De meiose", blokken=[
            ("p", "<strong>Bij de meiose wordt het aantal chromosomen per cel gehalveerd</strong>. Het "
                  "<strong>resultaat van een volledige meiose uit één diploïde cel</strong> zijn "
                  "<strong>vier haploïde cellen die genetisch van elkaar verschillen</strong>. "
                  "<strong>Mitose en meiose leveren dus niet allebei cellen op met hetzelfde aantal "
                  "chromosomen als de moedercel</strong>: alleen de mitose doet dat."),
            ("p", "Bij <strong>crossing-over wisselen homologe chromosomen stukken met elkaar uit</strong>. "
                  "Het <strong>chiasma</strong> is het <strong>punt waar twee homologe chromosomen elkaar "
                  "raken en stukken uitwisselen</strong>."),
            ("p", "Drie dingen <strong>zorgen samen voor genetische variatie</strong>: "
                  "<strong>de crossing-over tussen homologe chromosomen</strong>, "
                  "<strong>de toevallige verdeling van de chromosomenparen</strong> over de dochtercellen en "
                  "<strong>de willekeurige combinatie bij de bevruchting</strong>. Daarom lijkt geen broer "
                  "of zus precies op de andere."),
            ("p", "De <strong>tweede meiotische deling gaat niet gepaard met een nieuwe verdubbeling van het "
                  "DNA, omdat de chromosomen dan nog uit twee chromatiden bestaan</strong>: die tweede "
                  "deling trekt ze gewoon los van elkaar."),
        ]),
    ],
    onthoud=[
        "Een nucleotide bestaat uit een suiker, een fosfaatgroep en een stikstofbase.",
        "A paart met T via twee waterstofbruggen, G met C via drie.",
        "De twee strengen liggen antiparallel en vormen samen een dubbele helix.",
        "Een menselijke lichaamscel is diploïd en bevat 46 chromosomen, dus 23 paren.",
        "Het centromeer houdt de zusterchromatiden samen.",
        "Het DNA wordt verdubbeld in de S-fase van de interfase.",
        "Na de replicatie bestaat elke dubbele helix uit één oude en één nieuwe streng.",
        "Mitose: profase, metafase, anafase, telofase; ze geeft genetisch identieke cellen.",
        "Een volledige meiose levert uit één diploïde cel vier haploïde cellen die genetisch verschillen.",
    ],
)

# ───────────────────────── 6. Overerving van genetisch materiaal
BUNDELS["overerving-van-genetisch-materiaal-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Overerving van genetisch materiaal",
    onder="De wetten van Mendel, het punnettvierkant, geslachtsgebonden overerving en stambomen.",
    secties=[
        dict(kop="De woorden eerst", blokken=[
            ("p", tabel(["Woord", "Wat het betekent"], [
                ["Gen", "de eenheid die Mendel een erffactor noemde"],
                ["Locus", "de vaste plaats op een chromosoom waar een bepaald gen ligt"],
                ["Allel", "een van de versies van hetzelfde gen"],
                ["Homozygoot", "een organisme dat voor een bepaald gen twee gelijke allelen draagt"],
                ["Heterozygoot", "twee verschillende allelen, bijvoorbeeld Aa"],
                ["Genotype", "de erfelijke aanleg"],
                ["Fenotype", "het zichtbare kenmerk"],
                ["P-generatie", "de generatie van de oorspronkelijke ouders in een kruisingsschema"],
                ["Hybride", "een nakomeling uit twee ouders die verschillen; dus niet uit ouders die voor elk kenmerk precies hetzelfde zijn"],
            ])),
            ("p", "Het <strong>verschil tussen genotype en fenotype</strong> is dus: "
                  "<strong>het genotype is de erfelijke aanleg, het fenotype het zichtbare kenmerk</strong>. "
                  "Een plant <strong>Aa</strong> ziet eruit als een plant AA, maar hij "
                  "<strong>kan het allel a aan zijn nakomelingen doorgeven</strong>."),
        ]),
        dict(kop="De drie wetten van Mendel", blokken=[
            ("p", "<strong>Mendel koos de erwtenplant voor zijn kruisingsproeven, omdat die zich makkelijk "
                  "zelf bestuift en duidelijke kenmerken heeft</strong>: groen of geel, rond of gerimpeld, "
                  "zonder tussenvormen die het tellen moeilijk maken."),
            ("p", "De <strong>uniformiteitswet</strong> zegt dat <strong>de F1 uit twee raszuivere ouders "
                  "onderling gelijk is</strong>. De <strong>splitsingswet beschrijft de verhouding die in de "
                  "F2-generatie opduikt</strong>: daar komt het weggedoken kenmerk weer boven. De "
                  "<strong>onafhankelijkheidswet</strong> zegt dat <strong>twee kenmerken los van elkaar "
                  "doorgegeven worden</strong>."),
        ]),
        dict(kop="Rekenen met een punnettvierkant", blokken=[
            ("p", "Het <strong>punnettvierkant</strong> is het <strong>schema met vakjes waarmee je de "
                  "mogelijke combinaties van een kruising uittekent</strong>: de gameten van de ene ouder "
                  "bovenaan, die van de andere links."),
            ("p", tabel(["Aa × Aa", "A", "a"], [
                ["A", "AA", "Aa"],
                ["a", "Aa", "aa"],
            ])),
            ("p", "<strong>Twee heterozygote planten Aa</strong> geven dus een "
                  "<strong>genotypische verhouding 1 op 2 op 1</strong> (AA, Aa, aa) en een "
                  "<strong>fenotypische verhouding 3 op 1</strong>, want AA en Aa zien er gelijk uit."),
            ("p", "Kruis je een <strong>plant Aa met een plant aa</strong>, dan krijg je Aa, Aa, aa, aa: "
                  "<strong>50 procent van het nageslacht toont het recessieve kenmerk</strong>."),
            ("p", "Zo'n kruising met een homozygoot recessief organisme heet een "
                  "<strong>terugkruising</strong>. Daarover geldt: ze <strong>toont of de onderzochte ouder "
                  "homozygoot of heterozygoot is</strong>, <strong>alle nakomelingen tonen het dominante "
                  "kenmerk als de ouder AA is</strong>, en <strong>de helft toont het recessieve kenmerk als "
                  "de ouder Aa is</strong>."),
            ("p", "Krijgen <strong>twee planten met het dominante kenmerk een nakomeling met het recessieve "
                  "kenmerk</strong>, dan weet je drie dingen zeker: <strong>beide ouders zijn "
                  "heterozygoot</strong>, <strong>beide ouders dragen het recessieve allel</strong> en "
                  "<strong>de nakomeling is homozygoot recessief</strong>."),
            ("kader", "Een <strong>kenmerk dat in een generatie overslaat, is niet zeker dominant</strong>; "
                      "het is juist typisch voor een recessief kenmerk, dat verborgen door de dragers "
                      "meereist. Omgekeerd <strong>kan een dominante aandoening geen generatie overslaan en "
                      "dan weer opduiken</strong>: wie het allel heeft, toont het."),
        ]),
        dict(kop="Als dominantie niet volledig is", blokken=[
            ("p", "Over <strong>intermediaire overerving</strong>: <strong>de heterozygoot vertoont een "
                  "tussenvorm</strong>, <strong>geen van beide allelen is dominant</strong> en "
                  "<strong>een rode en een witte leeuwenbek geven roze</strong>. Daardoor "
                  "<strong>vallen de genotypische en de fenotypische verhouding in de F2 samen</strong>: "
                  "1 rood, 2 roze, 1 wit. Kruis je dus <strong>twee roze leeuwenbekken</strong>, dan is "
                  "<strong>25 procent van het nageslacht wit</strong>."),
            ("p", "Bij <strong>codominantie komen beide allelen in de heterozygoot volledig tot "
                  "uiting</strong>, niet half zoals bij een tussenvorm. De bloedgroep AB is het voorbeeld: "
                  "zowel A als B staat volop op de rode bloedcel."),
            ("p", "Daarmee kan je bloedgroepen voorspellen. <strong>Twee ouders met bloedgroep AB</strong> "
                  "geven alleen de allelen A en B door, dus zijn "
                  "<strong>A, B of AB</strong> mogelijk en O niet. Bij een "
                  "<strong>man met bloedgroep O en een vrouw met bloedgroep AB</strong> krijgt elk kind een "
                  "O van de vader en een A of een B van de moeder, dus is het "
                  "<strong>A of B</strong>."),
        ]),
        dict(kop="Twee kenmerken samen", blokken=[
            ("p", "Een <strong>organisme met genotype AaBb maakt vier verschillende soorten gameten</strong>: "
                  "AB, Ab, aB en ab. Kruis je <strong>twee planten AaBb</strong>, dan geeft het vierkant van "
                  "zestien vakjes de <strong>fenotypische verhouding 9 op 3 op 3 op 1</strong>. "
                  "<strong>Bij de kruising AaBb met AaBb is één op de zestien nakomelingen homozygoot "
                  "recessief voor beide kenmerken</strong>, namelijk aabb."),
            ("p", "Kruis je een <strong>plant AaBb met een plant aabb</strong>, dan levert de tweede ouder "
                  "enkel ab, en krijg je de <strong>fenotypische verhouding 1 op 1 op 1 op 1</strong>."),
            ("p", "De onafhankelijkheidswet geldt alleen als de genen op verschillende chromosomen liggen. "
                  "<strong>Twee genen op hetzelfde chromosoom liggen vaak niet los van elkaar, omdat ze "
                  "samen in dezelfde gameet terechtkomen</strong>; alleen een crossing-over kan ze nog "
                  "scheiden."),
        ]),
        dict(kop="Geslachtsgebonden overerving", blokken=[
            ("p", "Bij de mens duidt men de geslachtschromosomen van een vrouw met <strong>XX</strong> aan "
                  "en die van een man met XY. <strong>De vader bepaalt het geslacht van het kind, want zijn "
                  "zaadcel draagt een X of een Y</strong>, en de helft van zijn zaadcellen draagt elk. "
                  "Daarom is <strong>de kans op een jongen bij elke zwangerschap ongeveer vijftig "
                  "procent</strong>, los van wat er al geboren is."),
            ("p", "<strong>Geslachtsgebonden recessieve aandoeningen komen vaker bij mannen voor</strong>, en "
                  "wel om drie redenen samen: <strong>een man heeft maar één X-chromosoom</strong>, "
                  "<strong>bij een man volstaat één aangedaan allel</strong>, en "
                  "<strong>een vrouw kan het gezonde allel op haar tweede X hebben</strong>. Een "
                  "<strong>drager</strong> is dan ook <strong>een persoon die een recessief allel draagt "
                  "zonder de aandoening zelf te hebben</strong>."),
            ("p", "<strong>Geslachtsgebonden recessief</strong> erven onder meer "
                  "<strong>rood-groen kleurenblindheid</strong>, <strong>hemofilie A</strong> en "
                  "<strong>de ziekte van Duchenne</strong> over."),
            ("p", "Krijgt een <strong>draagster van kleurenblindheid kinderen met een man die niet "
                  "kleurenblind is</strong>, dan geeft zij haar aangedane X aan de helft van haar kinderen. "
                  "Een zoon met die X heeft geen tweede X om het op te vangen, een dochter krijgt van haar "
                  "vader een gezonde X. Dus: <strong>de helft van de zonen is kleurenblind en geen enkele "
                  "dochter</strong>. En <strong>een vader kan zijn X-gebonden allel niet aan zijn zoon "
                  "doorgeven</strong>, want aan zijn zoon geeft hij juist de Y."),
        ]),
        dict(kop="Een stamboom lezen", blokken=[
            ("p", "Uit een <strong>stamboom</strong> kan je afleiden <strong>of een kenmerk dominant of "
                  "recessief is</strong>, <strong>of een kenmerk geslachtsgebonden is</strong> en "
                  "<strong>welke personen zeker drager zijn</strong>. Wat je er niet uit leest, is de plaats "
                  "van het gen op een chromosoom."),
            ("p", "Hebben <strong>twee ouders zonder het kenmerk een dochter met dat kenmerk</strong>, dan "
                  "besluit je: <strong>het kenmerk is recessief en niet geslachtsgebonden</strong>. "
                  "Recessief, want de ouders waren allebei drager; niet geslachtsgebonden, want een dochter "
                  "zou dan ook van haar vader een aangedane X moeten krijgen, en die toont het kenmerk niet."),
        ]),
    ],
    onthoud=[
        "Het genotype is de erfelijke aanleg, het fenotype het zichtbare kenmerk.",
        "De drie wetten van Mendel: uniformiteitswet, splitsingswet en onafhankelijkheidswet.",
        "Aa × Aa geeft genotypisch 1 op 2 op 1 en fenotypisch 3 op 1.",
        "Een terugkruising toont of de onderzochte ouder homozygoot of heterozygoot is.",
        "Bij intermediaire overerving geven een rode en een witte leeuwenbek roze.",
        "Bij codominantie komen beide allelen volledig tot uiting, zoals bij bloedgroep AB.",
        "AaBb × AaBb geeft de fenotypische verhouding 9 op 3 op 3 op 1.",
        "Geslachtsgebonden recessieve aandoeningen komen vaker bij mannen voor: een man heeft maar één X-chromosoom.",
        "Twee ouders zonder het kenmerk krijgen een dochter met het kenmerk: recessief en niet geslachtsgebonden.",
    ],
)

# ───────────────────────── 7. Genexpressie en DNA-technologie
BUNDELS["genexpressie-en-dna-technologie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Genexpressie en DNA-technologie",
    onder="Van gen tot eiwit, wat er bij een mutatie misloopt, en wat je met DNA in een laboratorium kan doen.",
    secties=[
        dict(kop="Van gen tot eiwit", blokken=[
            ("p", "Een <strong>gen</strong> is <strong>een stuk DNA met de code voor één product, meestal "
                  "een eiwit</strong>. De code wordt per drie basen gelezen: "
                  "<strong>één codon bestaat uit drie basen</strong>. De "
                  "<strong>genetische code is bij nagenoeg alle organismen dezelfde</strong>, en net daarom "
                  "kan een bacterie een menselijk gen aflezen."),
            ("p", "<strong>RNA verschilt van DNA</strong> op drie punten: "
                  "<strong>RNA heeft ribose in plaats van desoxyribose</strong>, "
                  "<strong>RNA heeft uracil in plaats van thymine</strong> en "
                  "<strong>RNA is meestal enkelstrengig</strong>."),
            ("p", "De <strong>transcriptie gebeurt in een eukaryote cel in de celkern</strong>. Het enzym dat "
                  "<strong>tijdens de transcriptie het mRNA aanmaakt</strong>, is het "
                  "<strong>RNA-polymerase</strong>. Het bindt op de <strong>promotor</strong>, de "
                  "<strong>plaats op het DNA waar het de transcriptie start</strong>."),
            ("p", "Bij de <strong>splicing van pre-mRNA worden de introns eruit geknipt en de exons aan "
                  "elkaar geplakt</strong>: alleen de stukken die voor het eiwit nodig zijn, blijven over."),
            ("p", "Daarna volgt de translatie: <strong>het mRNA wordt op het ribosoom afgelezen tijdens de "
                  "translatie</strong>. Een <strong>tRNA-molecule brengt met zijn anticodon het juiste "
                  "aminozuur aan</strong>. Het codon dat <strong>bijna altijd de translatie start</strong>, "
                  "is <strong>AUG</strong>. Bij de <strong>terminatie bezet een releasefactor het stopcodon "
                  "en komt het eiwit vrij</strong>."),
            ("p", "Overschrijven gaat per base, met uracil op de plaats van thymine en telkens de "
                  "complementaire base. Van de <strong>DNA-matrijsstreng TAC</strong> wordt dus "
                  "<strong>AUG</strong> afgelezen: T geeft A, A geeft U en C geeft G."),
            ("p", "Er zijn 64 codons voor 20 aminozuren, dus "
                  "<strong>wordt niet elk aminozuur door precies één codon aangeduid</strong>. Meerdere "
                  "codons wijzen hetzelfde aminozuur aan, en dat maakt de code wat robuuster tegen fouten."),
        ]),
        dict(kop="Mutaties", blokken=[
            ("p", "Een <strong>puntmutatie waarbij één base vervangen wordt door een andere</strong>, heet "
                  "een <strong>substitutie</strong>. Door de dubbele code loopt dat soms met een sisser af."),
            ("p", "Een <strong>deletie van één base heeft vaak zware gevolgen, omdat alle codons erna "
                  "verschoven worden afgelezen</strong>: vanaf dat punt staat er een heel ander eiwit."),
            ("p", "Bij de <strong>genoommutaties</strong>, waar het aantal chromosomen afwijkt, horen "
                  "<strong>trisomie 21</strong>, <strong>het syndroom van Turner</strong> en "
                  "<strong>het syndroom van Klinefelter</strong>."),
            ("p", "Een <strong>mutatie is erfelijk als ze in een geslachtscel zit</strong>; een mutatie in "
                  "een lichaamscel gaat met die cellijn mee en verdwijnt met de persoon."),
            ("p", "<strong>Mutagenen</strong> zijn stoffen of stralen die mutaties uitlokken: "
                  "<strong>uv-straling</strong>, <strong>röntgenstraling</strong> en "
                  "<strong>benzopyreen uit tabaksrook</strong>."),
            ("p", "<strong>Epigenetische wijzigingen veranderen de volgorde van de basen in het DNA "
                  "niet</strong>. Ze zetten er merktekens bij die bepalen of een gen afgelezen wordt, en zo "
                  "kan de omgeving meespelen zonder dat er één letter verandert."),
        ]),
        dict(kop="Bacteriën en hun genen", blokken=[
            ("p", "Het genetisch materiaal van een bacterie bestaat uit "
                  "<strong>één ringvormig chromosoom, vaak met plasmiden ernaast</strong>. Een "
                  "<strong>plasmide</strong> is dat <strong>kleine, ringvormige stukje DNA naast het "
                  "bacterieel chromosoom</strong>."),
            ("p", "Bacteriën kunnen genen uitwisselen. Bij <strong>conjugatie gaat er via een pilus een "
                  "plasmide van de ene naar de andere</strong>. <strong>Transductie</strong> is "
                  "<strong>genoverdracht tussen bacteriën door een bacteriofaag</strong>. Zo'n "
                  "<strong>bacteriofaag is een obligate parasiet en kan zich enkel in een gastheercel "
                  "vermenigvuldigen</strong>. Daardoor kan resistentie tegen een antibioticum van de ene "
                  "soort naar de andere overspringen."),
        ]),
        dict(kop="Knippen en plakken", blokken=[
            ("p", "Een <strong>restrictie-enzym zoals EcoRI</strong> <strong>knipt de dubbele streng DNA "
                  "door</strong>, <strong>herkent daarvoor een vaste basenvolgorde</strong> en "
                  "<strong>laat vaak sticky ends achter</strong>. Die "
                  "<strong>sticky ends zijn handig bij gentechnologie, omdat twee stukken met dezelfde "
                  "overhang op elkaar passen</strong>. Het enzym dat het "
                  "<strong>donor-DNA definitief in het opengeknipte plasmide vastplakt</strong>, is "
                  "<strong>ligase</strong>. Een <strong>plasmide dat een vreemd gen draagt, noemt men een "
                  "recombinant plasmide</strong>."),
            ("p", "Bij het maken van <strong>insulineproducerende bacteriën</strong> horen deze stappen: "
                  "<strong>het menselijke insulinegen wordt uitgeknipt</strong>, "
                  "<strong>een plasmide wordt met hetzelfde enzym opengeknipt</strong> en "
                  "<strong>het recombinante plasmide gaat een bacterie binnen</strong>. Daarna doet de "
                  "bacterie de rest van het werk."),
            ("p", "Bij planten gebruikt men vaak <strong>het Ti-plasmide van een bodembacterie, omdat die "
                  "bacterie van nature DNA in plantencellen inbouwt</strong>."),
            ("p", "Het <strong>verschil tussen een cisgeen en een transgeen organisme</strong>: "
                  "<strong>bij cisgeen komt het gen uit dezelfde of een kruisbare soort</strong>, bij "
                  "transgeen uit een soort die je nooit zou kunnen kruisen. "
                  "<strong>Insectresistente maïs en katoen zijn voorbeelden van transgene gewassen</strong>. "
                  "Daaruit volgt dat <strong>een genetisch gemodificeerd organisme niet altijd transgeen "
                  "is</strong>: een cisgeen gewas is ook gemodificeerd."),
            ("p", "<strong>CRISPR-Cas</strong> is de techniek <strong>waarmee men met een geleidend RNA en "
                  "een knipeiwit heel gericht in het DNA kan ingrijpen</strong>. Daarin verschilt "
                  "<strong>gene editing van het klassieke inbrengen van een gen</strong>: "
                  "<strong>er wordt heel gericht op één plaats in het genoom gewerkt</strong>, in plaats van "
                  "een gen ergens te laten invallen."),
        ]),
        dict(kop="DNA onderzoeken", blokken=[
            ("p", "Een <strong>PCR</strong> dient om <strong>een klein stukje DNA miljoenen keren te "
                  "kopiëren</strong>, zodat je er genoeg van hebt om mee te werken. Eén haar op een plaats "
                  "van een misdrijf is dan al voldoende."),
            ("p", "Bij <strong>gelelektroforese worden DNA-fragmenten door een elektrisch veld op lengte "
                  "gescheiden</strong>. Daarbij <strong>leggen de langste DNA-fragmenten niet de grootste "
                  "afstand af</strong>: ze blijven juist het snelst in de gel steken, dus de kortste komen "
                  "het verst."),
            ("p", "Een <strong>DNA-fingerprint</strong> gebruikt men om "
                  "<strong>sporen aan een verdachte te koppelen</strong>, "
                  "<strong>een vaderschap aan te tonen</strong> en "
                  "<strong>familieleden van elkaar te onderscheiden</strong>."),
        ]),
    ],
    onthoud=[
        "Eén codon bestaat uit drie basen; de genetische code is bij nagenoeg alle organismen dezelfde.",
        "RNA heeft ribose en uracil in plaats van desoxyribose en thymine, en is meestal enkelstrengig.",
        "Transcriptie gebeurt in de celkern, translatie op het ribosoom.",
        "Bij splicing worden de introns eruit geknipt en de exons aan elkaar geplakt.",
        "Na een deletie van één base worden alle codons erna verschoven afgelezen.",
        "Een mutatie is erfelijk als ze in een geslachtscel zit.",
        "Een plasmide is een klein, ringvormig stukje DNA naast het bacterieel chromosoom.",
        "Een restrictie-enzym knipt het DNA, ligase plakt het donor-DNA vast in het plasmide.",
        "Een PCR kopieert een klein stukje DNA miljoenen keren; gelelektroforese scheidt fragmenten op lengte.",
    ],
)

# ───────────────────────── 8. Ontstaan en evolutie van soorten
BUNDELS["ontstaan-en-evolutie-van-soorten-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Ontstaan en evolutie van soorten",
    onder="Waar het bewijsmateriaal uit komt, hoe de natuurlijke selectie werkt, en wanneer een nieuwe soort ontstaat.",
    secties=[
        dict(kop="Wat evolutie is", blokken=[
            ("p", "<strong>Biologische evolutie</strong> is <strong>de verandering van de erfelijke "
                  "eigenschappen van een populatie over generaties</strong>. Een individu evolueert dus niet; "
                  "een <strong>populatie</strong>, <strong>alle individuen van één soort in een bepaald "
                  "gebied</strong>, doet dat wel."),
            ("p", "Volgens de moderne evolutietheorie <strong>gaan alle soorten terug op een "
                  "gemeenschappelijke voorouder</strong>. Men noemt die eerste cel de "
                  "<strong>oercel</strong>: <strong>de eerste cel waaruit alle latere leven "
                  "voortkomt</strong>. De boom die <strong>de verwantschap tussen alle soorten "
                  "uittekent</strong>, heet de <strong>tree of life</strong>."),
            ("p", "<strong>De evolutietheorie is in de wetenschap geen losse gok zonder "
                  "bewijsmateriaal</strong>. Een theorie betekent in de wetenschap juist het omgekeerde van "
                  "wat het in het dagelijks taalgebruik betekent: een verklaring die honderdvijftig jaar lang "
                  "door duizenden onafhankelijke vondsten bevestigd is."),
        ]),
        dict(kop="Waar de argumenten vandaan komen", blokken=[
            ("p", "De argumenten voor evolutie komen uit verschillende vakgebieden samen: "
                  "<strong>de paleontologie</strong>, <strong>de embryologie</strong> en "
                  "<strong>de moleculaire biologie</strong>, en daarnaast ook uit de vergelijkende anatomie "
                  "en de biogeografie. Dat ze elkaar onafhankelijk bevestigen, is precies de kracht ervan."),
            ("p", tabel(["Vakgebied", "Wat het aanbrengt"], [
                ["Paleontologie", "fossielen, overgangsvormen en continue reeksen"],
                ["Vergelijkende anatomie", "homologe, analoge en rudimentaire organen"],
                ["Embryologie", "de embryo's van verschillende gewervelden lijken in een vroeg stadium sterk op elkaar"],
                ["Biochemie", "verwante soorten hebben sterk gelijkende aminozuursequenties"],
                ["Biogeografie", "de verspreiding van soorten past bij het uiteendrijven van de continenten"],
            ])),
            ("p", "Over <strong>homologe organen</strong> geldt: <strong>ze hebben dezelfde bouw</strong>, "
                  "<strong>ze gaan terug op dezelfde oorsprong</strong> en <strong>ze kunnen een heel andere "
                  "functie vervullen</strong>. De voorpoot van een mol, de vleugel van een vleermuis en de "
                  "arm van een mens zijn homoloog. Bij <strong>analogie</strong> is het net omgekeerd: "
                  "dezelfde functie, een andere oorsprong, zoals "
                  "<strong>de vleugel van een insect en de vleugel van een vogel</strong>."),
            ("p", "Een orgaan dat bij een soort <strong>nog aanwezig is maar zijn functie verloren "
                  "heeft</strong>, zoals de blinde darm bij de mens, noemt men "
                  "<strong>rudimentair</strong>."),
            ("p", "Een <strong>overgangsfossiel vertoont kenmerken van twee groepen tegelijk</strong>. "
                  "<strong>Archaeopteryx is zo'n bekend voorbeeld, omdat hij kenmerken van reptielen en "
                  "vogels combineert</strong>: tanden en een lange staart naast veren. "
                  "<strong>Continue reeksen fossielen, zoals bij de paardachtigen</strong>, tonen "
                  "<strong>dat soorten geleidelijk veranderen</strong>, <strong>dat tussenvormen echt bestaan "
                  "hebben</strong> en <strong>dat bouwkenmerken stap voor stap wijzigen</strong>."),
            ("p", "Twee voorzichtigheden bij fossielen. <strong>Fossielen in diepere aardlagen zijn in het "
                  "algemeen niet jonger dan die in de lagen erboven</strong>, maar juist ouder: wat later "
                  "bezinkt, ligt bovenop. En we vinden <strong>maar van een klein deel van de uitgestorven "
                  "soorten fossielen terug, omdat fossilisatie zeldzame omstandigheden vraagt</strong>: snel "
                  "bedekt worden, zonder zuurstof, in de juiste bodem."),
            ("p", "Hoe <strong>de biochemie de evolutietheorie ondersteunt</strong>, laat zich meten: "
                  "<strong>verwante soorten hebben sterk gelijkende aminozuursequenties</strong>. Vergelijkt "
                  "een onderzoeker het <strong>hemoglobine van mens, chimpansee en paard</strong>, dan "
                  "verwacht hij <strong>het minste verschil tussen mens en chimpansee</strong>."),
            ("p", "De <strong>continentendrift</strong> is <strong>de langzame beweging van de werelddelen "
                  "die de verspreiding van soorten mee verklaart</strong>: waarom buideldieren vooral in "
                  "Australië zitten, en waarom Zuid-Amerika en Afrika verwante groepen delen."),
        ]),
        dict(kop="Van Lamarck naar Darwin", blokken=[
            ("p", "<strong>Lamarck beweerde dat verworven eigenschappen aan de nakomelingen doorgegeven "
                  "worden</strong>: een giraf die rekt, zou langernekkige jongen krijgen. Dat bleek niet te "
                  "kloppen, want wat je in je leven met je lichaam doet, verandert je geslachtscellen niet."),
            ("p", "De kern van de theorie van Darwin bestaat uit drie gedachten samen: "
                  "<strong>variatie</strong>, <strong>selectie</strong> en <strong>erfelijkheid</strong>. "
                  "Er zijn verschillen tussen individuen, de omgeving laat sommige daarvan beter overleven, "
                  "en die verschillen worden doorgegeven."),
            ("p", "<strong>De moderne evolutietheorie heeft de ideeën van Darwin niet volledig "
                  "verworpen</strong>. Ze heeft ze aangevuld met wat Darwin niet kon weten: genen, mutaties "
                  "en de meiose."),
        ]),
        dict(kop="Waar variatie en verschuiving vandaan komen", blokken=[
            ("p", "De <strong>variatie in een populatie</strong> komt van "
                  "<strong>mutaties</strong>, <strong>crossing-over bij de meiose</strong> en "
                  "<strong>de willekeurige combinatie bij de bevruchting</strong>."),
            ("p", "De <strong>selectiedruk</strong> is de <strong>druk van de omgeving waardoor sommige "
                  "varianten meer kans maken dan andere</strong>. De <strong>fitness van een "
                  "fenotype</strong> is daarbij niet hoe sterk of hoe snel het is, maar "
                  "<strong>hoeveel vruchtbare nakomelingen het gemiddeld oplevert</strong>."),
            ("p", "Twee klassieke voorbeelden. <strong>Bacteriën worden resistent tegen een antibioticum, "
                  "omdat de toevallig ongevoelige bacteriën overleven en zich voortplanten</strong>; het "
                  "antibioticum maakt ze niet resistent, het ruimt alleen de gevoelige op. En bij de "
                  "<strong>peper-en-zoutvlinder tijdens de industriële revolutie werd de donkere vorm "
                  "talrijker omdat ze op beroete bomen minder opviel</strong>."),
            ("p", "Naast de natuurlijke selectie spelen nog drie krachten mee. "
                  "<strong>Seksuele selectie</strong> is <strong>selectie door de voorkeur van partners bij "
                  "de voortplanting</strong>. <strong>Genetische drift</strong> is "
                  "<strong>het toeval dat vooral in kleine populaties allelfrequenties verschuift</strong>; "
                  "<strong>genetische drift werkt sterker in een kleine populatie dan in een grote</strong>, "
                  "want daar weegt één toevallige dode zwaar door. En <strong>gene flow</strong> is "
                  "<strong>het uitwisselen van allelen tussen twee populaties doordat er individuen heen en "
                  "weer trekken</strong>."),
            ("p", "<strong>Een hoge genetische diversiteit maakt een populatie niet kwetsbaarder voor een "
                  "nieuwe ziekte</strong>, maar juist sterker: hoe meer verschillende varianten er zijn, hoe "
                  "groter de kans dat er enkele bij zijn die de ziekte doorstaan."),
        ]),
        dict(kop="Soortvorming", blokken=[
            ("p", "Men spreekt van <strong>twee aparte soorten als ze onder natuurlijke omstandigheden geen "
                  "vruchtbaar nageslacht meer geven</strong>. Een muilezel bestaat, maar hij is onvruchtbaar, "
                  "dus zijn een paard en een ezel twee soorten."),
            ("p", "Voor <strong>soortvorming</strong> is drie dingen samen nodig: "
                  "<strong>variatie in de populatie</strong>, <strong>isolatie tussen de groepen</strong> en "
                  "<strong>selectie die de groepen uit elkaar duwt</strong>."),
            ("p", tabel(["Isolatievorm", "Voorbeeld"], [
                ["Geografische isolatie", "twee populaties raken gescheiden door een nieuw gebergte"],
                ["Temporele isolatie", "twee kikkersoorten in dezelfde vijver paren in verschillende maanden"],
                ["Gedragsisolatie", "twee vogelsoorten hebben een heel andere baltsdans en reageren daardoor niet op elkaar"],
                ["Gametische isolatie", "de zaadcel van de ene soort kan de eicel van de andere niet bevruchten"],
            ])),
            ("p", "Tot slot het woord dat alles samenbindt: een <strong>adaptatie</strong> is "
                  "<strong>een erfelijk kenmerk dat een organisme beter doet passen bij zijn "
                  "omgeving</strong>. Een aangeleerde vaardigheid is dus geen adaptatie, hoe nuttig ze ook is."),
        ]),
    ],
    onthoud=[
        "Biologische evolutie is de verandering van de erfelijke eigenschappen van een populatie over generaties.",
        "Homologe organen hebben dezelfde bouw en oorsprong; analoge organen dezelfde functie maar een andere oorsprong.",
        "Archaeopteryx is een overgangsfossiel met kenmerken van reptielen en vogels.",
        "Verwante soorten hebben sterk gelijkende aminozuursequenties.",
        "Lamarck dacht dat verworven eigenschappen doorgegeven worden; dat bleek niet te kloppen.",
        "De kern van Darwins theorie: variatie, selectie en erfelijkheid.",
        "Fitness is hoeveel vruchtbare nakomelingen een fenotype gemiddeld oplevert.",
        "Genetische drift werkt sterker in een kleine populatie dan in een grote.",
        "Twee aparte soorten geven onder natuurlijke omstandigheden geen vruchtbaar nageslacht meer.",
    ],
)

# ───────────────────────── 9. Biomoleculen
BUNDELS["biomoleculen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Biomoleculen",
    onder="Suikers, lipiden en proteïnen: hun bouwstenen, hun vorm en hun taken, en de twee reacties die ze aan en af bouwen.",
    secties=[
        dict(kop="Suikers", blokken=[
            ("p", "<strong>Monosachariden</strong> zijn de kleinste suikers: "
                  "<strong>glucose</strong>, <strong>fructose</strong> en <strong>galactose</strong>. "
                  "<strong>Glucose en fructose hebben dezelfde brutoformule maar een andere "
                  "structuur</strong>, en net daarom smaken en werken ze anders."),
            ("p", "Twee monosachariden samen vormen een disacharide, verbonden door een "
                  "<strong>glycosidische binding</strong>. <strong>Sacharose bestaat uit glucose en "
                  "fructose</strong>; lactose uit glucose en galactose. Dat laatste verklaart waarom "
                  "<strong>sommige mensen buikklachten van melk krijgen: ze missen het enzym dat lactose "
                  "splitst</strong>."),
            ("p", "Veel monosachariden aan elkaar geven een polysacharide. "
                  "<strong>Zetmeel en cellulose zijn allebei polysachariden van glucose</strong>, en toch is "
                  "het ene voedsel en het andere hout. Het verschil zit in de binding: "
                  "<strong>de mens kan cellulose niet verteren, omdat hij het enzym mist dat die bindingen "
                  "verbreekt</strong>. <strong>Zetmeel bestaat niet uit één enkele soort keten zonder "
                  "vertakkingen</strong>: er zit zowel een rechte als een vertakte vorm in. "
                  "Een <strong>dier slaat zijn reservesuiker als glycogeen op</strong>, een nog sterker "
                  "vertakte keten."),
            ("p", "<strong>Polysachariden</strong> kunnen heel verschillende taken hebben: "
                  "<strong>energie opslaan in lever en spieren</strong>, "
                  "<strong>stevigheid geven aan een plantencel</strong> en "
                  "<strong>het pantser van een insect vormen</strong>."),
            ("weetje", "Men noemt een stuk brood met veel vezels een <strong>trage suiker</strong>, "
                       "<strong>omdat de glucose er traag uit vrijkomt en de bloedsuiker minder "
                       "piekt</strong>. Hetzelfde aantal gram koolhydraten geeft dus niet hetzelfde "
                       "verloop in je bloed."),
        ]),
        dict(kop="Lipiden", blokken=[
            ("p", "<strong>Triglyceriden</strong> zijn de lipiden die <strong>uit glycerol en drie vetzuren "
                  "opgebouwd</strong> zijn. Een <strong>onverzadigd vetzuur bevat een of meer dubbele "
                  "bindingen in zijn koolstofketen</strong>, en daardoor een knik die de ketens minder goed "
                  "op elkaar laat stapelen. Zo komt het dat "
                  "<strong>oliën over het algemeen meer onverzadigde vetzuren bevatten dan harde "
                  "vetten</strong>."),
            ("p", "Een <strong>fosfolipide is geschikt om een membraan te vormen, omdat het een waterminnende "
                  "kop en waterafstotende staarten heeft</strong>. Zo'n deel van een molecule dat water "
                  "afstoot, heet <strong>hydrofoob</strong>. Dat een "
                  "<strong>vogel zijn veren invet</strong>, gebruikt dezelfde eigenschap: "
                  "<strong>dat ze water afstoten</strong>."),
            ("p", "<strong>Cholesterol</strong> hoort tot de <strong>steroïden</strong>, een derde groep "
                  "lipiden naast de triglyceriden en de fosfolipiden."),
            ("p", "<strong>Lipiden leveren per gram meer energie dan suikers</strong>, ongeveer het dubbele. "
                  "In het lichaam <strong>slaan ze energie op lange termijn op</strong>, "
                  "<strong>isoleren ze het lichaam tegen koude</strong> en "
                  "<strong>slaan ze in vet oplosbare vitaminen op</strong>."),
        ]),
        dict(kop="Proteïnen", blokken=[
            ("p", "<strong>Elk aminozuur</strong> heeft altijd <strong>een carboxylgroep</strong>, "
                  "<strong>een aminogroep</strong> en <strong>een restgroep</strong>. Alleen die restgroep "
                  "verschilt van aminozuur tot aminozuur. Wat bepaalt <strong>of een restgroep polair, "
                  "apolair of ioniserend is</strong>, zijn <strong>de atomen waaruit die restgroep "
                  "bestaat</strong>. <strong>Apolaire restgroepen gaan bij een opgevouwen eiwit meestal naar "
                  "de binnenkant</strong>, weg van het water."),
            ("p", "De binding tussen twee aminozuren in een eiwit heet de "
                  "<strong>peptidebinding</strong>. Een eiwit vouwt zich daarna in lagen op."),
            ("p", tabel(["Structuur", "Wat ze is", "Wat ze samenhoudt"], [
                ["Primaire structuur", "de volgorde van de aminozuren in de keten", "peptidebindingen"],
                ["Secundaire structuur", "de alfahelix en de bètaplaat", "waterstofbruggen tussen de hoofdketen"],
                ["Tertiaire structuur", "de ruimtelijke vorm van de hele keten", "disulfidebindingen, ionbindingen en waterstofbruggen"],
                ["Quaternaire structuur", "meerdere ketens die samen één eiwit vormen; dus niet één enkele keten", "dezelfde soorten bindingen tussen de ketens"],
            ])),
            ("p", "Die vorm is alles. <strong>Eén verkeerd aminozuur in een eiwit kan de hele werking ervan "
                  "verstoren</strong>, en een <strong>eiwit dat te sterk verhit wordt, verliest zijn vorm en "
                  "daarmee zijn werking</strong>. Zo wordt een eiwit ook ongeschikt als enzym: "
                  "<strong>een enzym werkt maar op één bepaalde stof, omdat de vorm van zijn actieve plaats "
                  "op die stof past</strong>."),
            ("p", "Proteïnen doen heel verschillende dingen: <strong>reacties versnellen als enzym</strong>, "
                  "<strong>indringers herkennen als antilichaam</strong> en "
                  "<strong>de genexpressie regelen als transcriptiefactor</strong>. Daarnaast is er transport "
                  "en beweging: <strong>hemoglobine vervoert zuurstof in het bloed</strong>, "
                  "<strong>actine en myosine zorgen voor het samentrekken van een spier</strong>, en de "
                  "<strong>aquaporines</strong> zijn de <strong>eiwitten in het celmembraan waardoor water "
                  "vlot de cel in en uit kan</strong>."),
        ]),
        dict(kop="Opbouw en afbraak", blokken=[
            ("p", "Alle biomoleculen worden met dezelfde twee reacties aan en af gebouwd. Bij een "
                  "<strong>condensatiereactie worden twee bouwstenen verbonden en komt er water vrij</strong>. "
                  "Bij een <strong>hydrolysereactie wordt een binding met behulp van water "
                  "verbroken</strong>. Daarom <strong>verlopen de opbouw- en afbraakreacties van suikers, "
                  "eiwitten en vetten niet volgens heel verschillende principes</strong>, maar juist volgens "
                  "hetzelfde: één patroon dat je drie keer terugvindt."),
            ("p", "Dus kan je bij elke vertering voorspellen wat vrijkomt. Bij de "
                  "<strong>vertering van een triglyceride ontstaan glycerol en vetzuren</strong>. Wordt een "
                  "<strong>eiwit in de darm verteerd</strong>, dan komen er "
                  "<strong>aminozuren</strong> vrij. En een polysacharide valt uiteen in monosachariden."),
        ]),
    ],
    onthoud=[
        "Monosachariden zijn glucose, fructose en galactose.",
        "Sacharose bestaat uit glucose en fructose, verbonden door een glycosidische binding.",
        "Zetmeel en cellulose zijn allebei polysachariden van glucose; een dier slaat glycogeen op.",
        "Triglyceriden zijn opgebouwd uit glycerol en drie vetzuren.",
        "Een onverzadigd vetzuur bevat een of meer dubbele bindingen in zijn koolstofketen.",
        "Elk aminozuur heeft een carboxylgroep, een aminogroep en een restgroep.",
        "De primaire structuur van een eiwit is de volgorde van de aminozuren.",
        "Condensatie verbindt bouwstenen en maakt water vrij; hydrolyse verbreekt een binding met water.",
    ],
)

# ───────────────────────── 11. Chemisch evenwicht
BUNDELS["chemisch-evenwicht-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Chemisch evenwicht",
    onder="Aflopend, in evenwicht of geen reactie, en hoe je een evenwicht de kant op duwt die je wil.",
    secties=[
        dict(kop="Drie mogelijke uitkomsten", blokken=[
            ("p", "Meng je twee stoffen, dan zijn er drie uitkomsten mogelijk."),
            ("p", tabel(["Uitkomst", "Waaraan je het merkt", "Op een concentratie-tijdgrafiek"], [
                ["Aflopende reactie", "minstens één reagens raakt volledig op", "de lijn van een reagens zakt tot op de horizontale as"],
                ["Chemisch evenwicht", "de reagentia en de producten zijn allebei nog aanwezig", "twee concentratielijnen veranderen eerst en lopen daarna vlak naast elkaar door"],
                ["Geen reactie", "de concentraties veranderen helemaal niet", "alle lijnen blijven van het begin af vlak"],
            ])),
            ("p", "Bij een <strong>chemisch evenwicht</strong> geldt dus: <strong>de reagentia en de "
                  "producten zijn allebei nog aanwezig</strong>, <strong>de concentraties veranderen niet "
                  "meer</strong> en <strong>de heenreactie en de terugreactie gaan even snel</strong>. "
                  "Opgelet: <strong>in een chemisch evenwicht zijn de concentraties van reagentia en "
                  "producten niet altijd aan elkaar gelijk</strong>. Ze veranderen niet meer, maar ze mogen "
                  "heel verschillend zijn; een evenwicht kan ver naar links of ver naar rechts liggen."),
            ("p", "Daarom spreekt men van een <strong>dynamisch evenwicht</strong>: een evenwicht "
                  "<strong>waarbij de heen- en terugreactie blijven doorgaan</strong>. "
                  "<strong>Zodra een evenwicht bereikt is, worden er wel nog nieuwe productmoleculen "
                  "gevormd</strong>, alleen worden er op datzelfde ogenblik even veel weer afgebroken. Van "
                  "buiten lijkt er niets te gebeuren, van binnen gebeurt er voortdurend iets."),
            ("p", "Je kan in het labo nagaan of je <strong>met een evenwicht te doen hebt</strong> door "
                  "<strong>na te kijken of er op het einde nog van beide reagentia is</strong> en door "
                  "<strong>iets toe te voegen en te kijken of er nog iets verandert</strong>. Een "
                  "<strong>evenwicht kan je ook van rechts naar links bereiken, dus vertrekkend van de "
                  "producten</strong>: je komt bij dezelfde eindtoestand uit, van welke kant je ook start."),
        ]),
        dict(kop="Limiterend reagens en overmaat", blokken=[
            ("p", "Het <strong>limiterend reagens</strong> is <strong>het reagens dat als eerste opgebruikt "
                  "is en zo de reactie stopt</strong>. Het reagens waarvan er na de reactie nog overblijft, "
                  "is de <strong>overmaat</strong>: <strong>bij een aflopende reactie blijft er van het "
                  "reagens in overmaat nog over</strong>."),
            ("p", "Meng je <strong>2 mol van stof A met 5 mol van stof B, terwijl de reactie één op één "
                  "verloopt</strong>, dan kan er maar 2 mol reageren, dus is <strong>stof B</strong> in "
                  "overmaat. Het is bij een proef <strong>soms handig om één reagens in overmaat te "
                  "gebruiken, om zeker te zijn dat het andere reagens volledig reageert</strong>."),
        ]),
        dict(kop="De snelheden onderweg", blokken=[
            ("p", "Op weg naar het evenwicht veranderen beide snelheden tegelijk. "
                  "<strong>De heenreactie vertraagt onderweg naar het evenwicht</strong>, de "
                  "<strong>terugreactie versnelt onderweg naar het evenwicht</strong>, en "
                  "<strong>in het evenwicht zijn beide snelheden gelijk</strong>. De "
                  "<strong>snelheid van de heenreactie daalt, want de reagentia raken op</strong>, terwijl "
                  "er juist steeds meer product is om terug te reageren."),
            ("p", "Op een <strong>snelheid-tijdgrafiek van een evenwicht</strong> zie je dat aan de twee "
                  "lijnen: <strong>ze komen naar elkaar toe en lopen daarna samen verder</strong>."),
        ]),
        dict(kop="Kleur als venster op het evenwicht", blokken=[
            ("p", "Is de <strong>oplossing van het evenwicht van ijzerthiocyanaat bloedrood</strong>, dan "
                  "zegt die kleur <strong>dat er een duidelijke hoeveelheid gekleurd product aanwezig "
                  "is</strong>. Meer dan dat zegt ze niet: de kleur verraadt geen snelheid en geen "
                  "temperatuur."),
            ("p", "Juist daarom is <strong>een kleurverandering een handige manier om een verschuiving van een "
                  "evenwicht te volgen</strong>: je ziet met je ogen welke kant het op gaat, zonder te meten."),
        ]),
        dict(kop="De wet van Le Chatelier en Van 't Hoff", blokken=[
            ("p", "De wet die <strong>voorspelt in welke richting een evenwicht verschuift</strong>, is de "
                  "<strong>wet van Le Chatelier en Van 't Hoff</strong>: <strong>een evenwicht schuift zo op "
                  "dat het de verstoring tegenwerkt</strong>. Duw je ergens, dan duwt het evenwicht terug."),
            ("p", "<strong>Verstoringen die een evenwicht kunnen doen verschuiven</strong>: "
                  "<strong>de concentratie van één stof veranderen</strong>, "
                  "<strong>het volume van het vat veranderen bij een gasevenwicht</strong> en "
                  "<strong>de temperatuur veranderen</strong>."),
            ("p", "Een verschuiving <strong>naar de kant van de reagentia</strong> noemt men een verschuiving "
                  "<strong>naar links</strong>; naar de producten is naar rechts. Een "
                  "<strong>verschuiving naar rechts betekent dat de concentratie van alle producten "
                  "stijgt</strong>."),
            ("p", tabel(["Wat je doet", "Wat het evenwicht doet"], [
                ["extra reagens toevoegen", "het kiest de kant van de producten"],
                ["een reagens verwijderen", "het schuift naar links en er verdwijnt product"],
                ["product uit het evenwichtsmengsel weghalen", "het maakt nieuw product aan"],
                ["een katalysator toevoegen", "het evenwicht wordt sneller bereikt, maar het ligt niet anders"],
            ])),
            ("p", "Voeg je <strong>extra reagens toe aan een evenwicht waarvan het product gekleurd is</strong>, "
                  "dan wordt <strong>de kleur sterker</strong>."),
            ("p", "Kijk ook naar de snelheid vlak na een ingreep. Voeg je <strong>reagens toe</strong>, dan "
                  "<strong>stijgt de snelheid van de heenreactie eerst en zakt ze daarna naar de nieuwe "
                  "evenwichtswaarde</strong>. En <strong>na een verstoring komen de twee snelheden niet "
                  "opnieuw op dezelfde waarde als voor de verstoring uit</strong>: ze worden weer aan elkaar "
                  "gelijk, maar op een ander niveau."),
        ]),
        dict(kop="Temperatuur en druk", blokken=[
            ("p", "Bij temperatuur moet je weten welke kant warmte afgeeft. "
                  "<strong>Bij een exo-energetisch evenwicht verschuift opwarmen het evenwicht naar "
                  "links</strong>, want zo wordt de toegevoegde warmte weer opgenomen. "
                  "<strong>Koel je een evenwicht af waarvan de heenreactie exo-energetisch is</strong>, dan "
                  "<strong>schuift het naar rechts, want zo komt er warmte vrij</strong>."),
            ("p", "Die regel laat zich omdraaien tot een besluit. Wordt een "
                  "<strong>evenwicht met een bruin gas en een kleurloos gas bleker als je het "
                  "afkoelt</strong>, dan schuift het bij afkoelen naar het kleurloze gas, en dus: "
                  "<strong>de reactie naar het kleurloze gas geeft warmte af</strong>."),
            ("p", "Bij druk en volume tel je de gasdeeltjes links en rechts. Een gasevenwicht schuift bij een "
                  "hogere druk naar de kant met <strong>het kleinste</strong> aantal gasdeeltjes, want zo "
                  "neemt het mengsel minder plaats in. Heeft een "
                  "<strong>gasevenwicht links 3 mol gas en rechts 2 mol gas</strong> en pers je het "
                  "<strong>in een kleiner vat</strong>, dan <strong>schuift het naar rechts, naar de kant met "
                  "minder gasdeeltjes</strong>. Maar <strong>een volumeverandering verschuift niet elk "
                  "gasevenwicht</strong>: staan er links en rechts even veel gasdeeltjes, dan is er geen "
                  "kant die het drukverschil kan opvangen en blijft het evenwicht liggen waar het lag."),
        ]),
        dict(kop="Een grafiek ontleden en een fabriek sturen", blokken=[
            ("p", "Om <strong>uit een grafiek af te leiden welke factor een evenwicht verstoord heeft</strong>, "
                  "zet je drie stappen: <strong>kijken welke lijn als eerste plots verspringt</strong>, "
                  "<strong>kijken in welke richting de lijnen daarna evolueren</strong>, en "
                  "<strong>kijken of alle lijnen op hetzelfde moment van richting veranderen</strong>. Springt "
                  "er één lijn alleen, dan is er aan die stof geraakt; bewegen alle lijnen samen, dan is het "
                  "de temperatuur of het volume."),
            ("p", "Een fabriek gebruikt dezelfde wet om de opbrengst te verhogen: "
                  "<strong>het product onderweg uit het vat afvoeren</strong>, "
                  "<strong>extra reagens blijven toevoegen</strong> en "
                  "<strong>de temperatuur in de gunstige richting zetten</strong>. Zo haalt ze uit een "
                  "evenwicht toch bijna alles wat erin zit."),
        ]),
    ],
    onthoud=[
        "Een reactie is aflopend als minstens één reagens volledig opraakt.",
        "In een chemisch evenwicht gaan heen- en terugreactie even snel en veranderen de concentraties niet meer.",
        "In een evenwicht zijn de concentraties van reagentia en producten niet altijd aan elkaar gelijk.",
        "Het limiterend reagens is als eerste opgebruikt en stopt zo de reactie.",
        "Onderweg naar het evenwicht vertraagt de heenreactie en versnelt de terugreactie.",
        "Een kleurverandering is een handige manier om een verschuiving van een evenwicht te volgen.",
        "Le Chatelier en Van 't Hoff: een evenwicht schuift zo op dat het de verstoring tegenwerkt.",
        "Een katalysator laat het evenwicht sneller bereiken, maar het ligt niet anders.",
        "Bij een kleiner vat schuift een gasevenwicht naar de kant met minder gasdeeltjes.",
    ],
)

# ───────────────────────── 12. Organische stoffen
BUNDELS["organische-stoffen-classificatie-eigenschappen-en-toepassingen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Organische stoffen: classificatie, eigenschappen en toepassingen",
    onder="De elf stofklassen aan hun kenmerkende groep herkennen, en uit de bouw van een molecule haar eigenschappen voorspellen.",
    secties=[
        dict(kop="De stofklassen", blokken=[
            ("p", "Elke organische stofklasse heeft een <strong>kenmerkende groep</strong>. Vind je die "
                  "groep in een formule terug, dan weet je tot welke klasse de stof hoort."),
            ("p", tabel(["Stofklasse", "Kenmerkende groep", "Voorbeeld"], [
                ["Alkanen", "enkel koolstof en waterstof, met enkelvoudige bindingen", "CH4, C3H8, C4H10"],
                ["Alkenen", "een dubbele binding tussen twee koolstofatomen", "etheen"],
                ["Alkynen", "een drievoudige binding tussen twee koolstofatomen", "ethyn"],
                ["Alcoholen", "een OH-groep aan een koolstofketen", "CH3CH2OH"],
                ["Ethers", "een zuurstofatoom tussen twee koolstofketens", "di-ethylether"],
                ["Aldehyden", "een carbonylgroep aan het uiteinde van de keten", "methanal"],
                ["Ketonen", "een carbonylgroep middenin de keten", "CH3COCH3"],
                ["Carbonzuren", "een COOH-groep", "HCOOH, CH3COOH"],
                ["Esters", "de groep COO tussen twee koolstofketens", "ethylethanoaat"],
                ["Aminen", "een stikstofgroep aan de keten, dus geen OH-groep", "methaanamine"],
                ["Amiden", "zowel stikstof als zuurstof in de kenmerkende groep", "ethaanamide"],
            ])),
            ("p", "Een <strong>alkaan herken je doordat het enkel koolstof en waterstof bevat, met "
                  "enkelvoudige bindingen</strong>. We noemen alkanen <strong>verzadigde "
                  "koolwaterstoffen, omdat er geen waterstofatomen meer bij kunnen</strong>: elke plaats is al "
                  "bezet."),
            ("p", "Twee verwarringen om te vermijden. <strong>Een amine heeft niet, zoals een alcohol, een "
                  "OH-groep als kenmerkende groep</strong>, maar een stikstofgroep. En "
                  "<strong>CHCl3 hoort niet bij de alcoholen</strong>: er staat geen OH in, enkel chloor, dus "
                  "is het een gehalogeneerde koolwaterstof."),
            ("p", "Het <strong>verschil tussen een aldehyde en een keton</strong> is alleen de plaats: "
                  "<strong>bij een aldehyde staat de carbonylgroep aan het uiteinde van de keten</strong>."),
            ("p", "De naam verraadt de klasse mee: <strong>de uitgang -aan hoort bij de alkanen</strong>, "
                  "<strong>de uitgang -een hoort bij de alkenen</strong> en "
                  "<strong>de uitgang -ol hoort bij de alcoholen</strong>. Krijg je de naam "
                  "<strong>propaanzuur</strong>, dan zegt het woord zuur het al: het is een "
                  "<strong>carbonzuur</strong>."),
            ("p", "<strong>Twee stoffen met dezelfde brutoformule kunnen tot een andere stofklasse "
                  "horen</strong>: C2H6O is zowel ethanol als di-methylether. Daarom volstaat een "
                  "brutoformule niet en tekent men structuurformules."),
            ("p", "Het <strong>verschil tussen een uitgebreide en een beknopte structuurformule</strong>: "
                  "<strong>in de uitgebreide staat elke binding getekend, in de beknopte niet</strong>. Een "
                  "<strong>skeletnotatie</strong> gaat nog verder: <strong>een tekening met lijnen, waarbij "
                  "elke hoek een koolstofatoom is</strong>, en waar de waterstofatomen zelfs niet meer "
                  "opstaan."),
        ]),
        dict(kop="De intermoleculaire krachten", blokken=[
            ("p", "Of een stof vast, vloeibaar of gas is, en waarin ze oplost, hangt niet af van de bindingen "
                  "binnen een molecule maar van de krachten tussen de moleculen."),
            ("p", tabel(["Kracht", "Wanneer ze werkt", "Sterkte"], [
                ["Londondispersiekracht", "tussen alle moleculen, ook de apolaire", "de zwakste, maar ze telt op met de grootte van de molecule"],
                ["Dipoolkracht", "tussen polaire moleculen", "sterker dan de londondispersiekracht"],
                ["Waterstofbrug", "als waterstof aan zuurstof of stikstof hangt", "de sterkste intermoleculaire kracht"],
            ])),
            ("p", "Daarmee kan je kookpunten vergelijken. <strong>Het kookpunt van de alkanen stijgt als de "
                  "keten langer wordt</strong>, want <strong>de londondispersiekracht tussen de moleculen "
                  "wordt sterker</strong>: er is meer oppervlak dat raakt. Om dezelfde reden heeft "
                  "<strong>een sterk vertakt alkaan geen hoger kookpunt dan een rechte keten met dezelfde "
                  "formule</strong>, maar een lager: een bolvormige molecule raakt haar buren op minder "
                  "plaatsen aan."),
            ("p", "<strong>Ethanol heeft een veel hoger kookpunt dan ethaan</strong>, en dat komt doordat "
                  "<strong>ethanol waterstofbruggen vormt en ethaan niet</strong>. Eén OH-groep tilt het "
                  "kookpunt met meer dan honderd graden op."),
        ]),
        dict(kop="Polair en apolair", blokken=[
            ("p", "<strong>Apolaire stoffen</strong> zijn onder meer <strong>wasbenzine</strong>, "
                  "<strong>CCl4</strong> en <strong>een lang alkaan</strong>. "
                  "<strong>Een apolaire stof lost niet goed op in water</strong>, want water is polair, en "
                  "gelijk lost op in gelijk."),
            ("p", "Daarom <strong>mengt methanol wel met water en een lang alkaan niet</strong>: "
                  "<strong>methanol kan waterstofbruggen met water leggen</strong>. Maar het hangt van de "
                  "verhouding af: <strong>een alcohol met een heel lange keten lost bijna niet meer op in "
                  "water, omdat de lange apolaire staart zwaarder doorweegt dan de OH-groep</strong>."),
            ("p", "Moet je een <strong>vlek van een apolaire stof oplossen</strong>, kies dan een apolair "
                  "oplosmiddel, dus <strong>wasbenzine</strong> en geen water."),
            ("p", "Zeep lost dat probleem op door beide kanten te hebben. Over een "
                  "<strong>zeepmolecule</strong>: <strong>ze heeft een lange apolaire staart</strong>, "
                  "<strong>ze heeft een polaire kop</strong> en <strong>ze kan vet en water met elkaar "
                  "verbinden</strong>. Het bolletje dat zeepmoleculen rond een vetdruppel vormen, heet een "
                  "<strong>micel</strong>: de staarten in het vet, de koppen naar het water. "
                  "<strong>Een fosfolipide heeft net als zeep een polaire kop en apolaire staarten</strong>, "
                  "en dat is precies waarom een celmembraan zich van zelf vormt."),
        ]),
        dict(kop="Stoffen met een gebruiksnaam", blokken=[
            ("p", tabel(["Gebruiksnaam", "Stof"], [
                ["Hoofdbestanddeel van aardgas", "methaan"],
                ["Brandspiritus", "methanol"],
                ["Mierenzuur", "HCOOH"],
                ["Azijnzuur", "CH3COOH"],
                ["Aceton", "propanon is de wetenschappelijke naam van aceton"],
                ["Formol, om biologisch materiaal te bewaren", "methanal"],
            ])),
            ("p", "Over <strong>etheen</strong> geldt: <strong>het is een alkeen</strong>, "
                  "<strong>het heeft een dubbele binding</strong> en <strong>het is de bouwsteen van "
                  "polyetheen</strong>. Die dubbele binding is precies wat duizenden etheenmoleculen aan "
                  "elkaar laat haken tot een kunststof."),
        ]),
    ],
    onthoud=[
        "Elke organische stofklasse heeft een kenmerkende groep.",
        "Een alkaan bevat enkel koolstof en waterstof, met enkelvoudige bindingen.",
        "Bij een aldehyde staat de carbonylgroep aan het uiteinde van de keten, bij een keton middenin.",
        "Uitgangen: -aan bij de alkanen, -een bij de alkenen, -ol bij de alcoholen.",
        "De waterstofbrug is de sterkste intermoleculaire kracht, de londondispersiekracht de zwakste.",
        "Ethanol heeft een veel hoger kookpunt dan ethaan, omdat ethanol waterstofbruggen vormt.",
        "Een apolaire stof lost niet goed op in water: gelijk lost op in gelijk.",
        "Een zeepmolecule heeft een lange apolaire staart en een polaire kop.",
        "Propanon is de wetenschappelijke naam van aceton.",
    ],
)

# ───────────────────────── 13. Kunststoffen, nanomaterialen en duurzame chemie
BUNDELS["kunststoffen-nanomaterialen-en-duurzame-chemie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kunststoffen, nanomaterialen en duurzame chemie",
    onder="Hoe een kunststof gemaakt wordt, wat een nanomateriaal anders maakt, en hoe je duurzaamheid eerlijk beoordeelt.",
    secties=[
        dict(kop="Van monomeer tot polymeer", blokken=[
            ("p", "Een <strong>monomeer</strong> is <strong>de kleine molecule waaruit een kunststof "
                  "opgebouwd wordt</strong>. Twee ervan samen vormen een dimeer, duizenden een polymeer."),
            ("p", "Er zijn twee manieren om monomeren aan elkaar te rijgen. "
                  "<strong>Polyadditie gebruikt een dubbele binding om de monomeren aan elkaar te rijgen, "
                  "zonder dat er iets vrijkomt</strong>. Bij een <strong>polycondensatie komt er telkens "
                  "een kleine molecule vrij, meestal water</strong>."),
            ("p", tabel(["Afkorting", "Kunststof", "Waarvoor"], [
                ["PE", "polyetheen, opgebouwd uit etheen", "folie, flessen, zakken"],
                ["PP", "polypropeen", "potjes, autodelen, touw"],
                ["PVC", "polyvinylchloride", "buizen, vloeren, raamprofielen"],
                ["PS", "polystyreen", "isolatie en verpakking"],
                ["PTFE", "teflon", "de antiaanbaklaag van een pan"],
                ["PET", "polyethyleentereftalaat", "drankflessen en vezels voor kleding"],
                ["PA", "polyamide of nylon; PA is dus niet de afkorting van polyester", "kledingvezels, tandwielen"],
                ["PUR", "polyurethaan", "schuim, isolatie, matrassen"],
            ])),
            ("p", "<strong>Door polyadditie uit een monomeer met een dubbele binding</strong> worden onder "
                  "meer <strong>PE</strong>, <strong>PP</strong> en <strong>PVC</strong> gemaakt. PET en PA "
                  "ontstaan daarentegen door polycondensatie."),
        ]),
        dict(kop="Drie soorten gedrag", blokken=[
            ("p", "Dezelfde ketens kunnen heel anders aanvoelen, en dat komt door de dwarsverbindingen "
                  "ertussen, de <strong>crosslinks</strong>."),
            ("p", tabel(["Soort", "Kenmerk"], [
                ["Thermoplast", "hij wordt bij opwarmen week en kan opnieuw gevormd worden"],
                ["Thermoharder", "je kan hem niet opnieuw smelten, want de ketens zitten met veel crosslinks aan elkaar vast"],
                ["Elastomeer", "hij vervormt onder een kracht en komt daarna terug"],
            ])),
            ("p", "Heb je een <strong>soepele dichting nodig die na samenpersen terugkomt</strong>, dan kies "
                  "je <strong>een elastomeer</strong>. En voor de recyclage: "
                  "<strong>thermoplasten zijn makkelijker te recycleren dan thermoharders</strong>, precies "
                  "omdat je ze opnieuw kan smelten en vormen."),
        ]),
        dict(kop="Nanomaterialen", blokken=[
            ("p", "Een <strong>nanomateriaal</strong> is <strong>tussen 1 en 100 nanometer</strong> groot, "
                  "in minstens één richting. Men deelt ze in naar hoeveel richtingen die nanomaat "
                  "aanhoudt: <strong>een buckyball is een 0D-structuur</strong>, "
                  "<strong>een koolstofnanobuis is een 1D-structuur</strong> en "
                  "<strong>een laagje grafeen is een 2D-structuur</strong>. "
                  "<strong>Grafeen</strong> is dan ook het nanomateriaal dat "
                  "<strong>uit één laag koolstofatomen bestaat</strong>."),
            ("p", "Maken kan op twee manieren: top-down, door een groot stuk steeds fijner te verdelen, of "
                  "bottom-up. <strong>Bij een bottom-upproductie bouw je een nanomateriaal op uit atomen of "
                  "moleculen</strong>."),
            ("p", "<strong>Nanodeeltjes hebben geen kleinere verhouding van oppervlak tot volume dan grote "
                  "stukken van dezelfde stof</strong>, maar juist een veel grotere. Daaruit volgt bijna alles: "
                  "<strong>ze hebben een heel groot oppervlak per volume-eenheid</strong>, "
                  "<strong>ze zijn daardoor vaak veel reactiever</strong> en "
                  "<strong>hun smeltpunt kan lager liggen dan dat van een groot stuk</strong>."),
            ("p", "<strong>Eigenschappen van een nanomateriaal die anders kunnen zijn dan die van het grote "
                  "stuk</strong>: <strong>optische eigenschappen zoals een specifieke kleur</strong>, "
                  "<strong>elektrische eigenschappen</strong> en <strong>mechanische eigenschappen zoals "
                  "sterkte en hardheid</strong>. Dezelfde stof, een andere maat, ander gedrag."),
            ("p", "Twee toepassingen uit het dagelijks leven. Er zit "
                  "<strong>nanotitaandioxide of nanozinkoxide in zonnecrème, omdat het UV-licht tegenhoudt en "
                  "toch doorzichtig blijft</strong>, terwijl de grove vorm een witte laag geeft. En "
                  "<strong>zilver</strong> wordt als nanodeeltje gebruikt <strong>voor zijn antibacteriële "
                  "werking</strong>."),
            ("kader", "Een <strong>nadeel van nanodeeltjes is dat ze diep in een lichaam of in het milieu "
                      "kunnen terechtkomen</strong>. Precies hun kleine maat en hun reactiviteit, die ze "
                      "nuttig maken, maken ze ook moeilijk tegen te houden en moeilijk te volgen."),
        ]),
        dict(kop="Van lineair naar circulair", blokken=[
            ("p", "De <strong>lineaire economie</strong> is de economie die <strong>grondstoffen neemt, er "
                  "iets van maakt en het daarna weggooit</strong>. Daartegenover staat het circulaire denken, "
                  "en daarbinnen is er een rangorde."),
            ("p", "Bovenaan de <strong>Ladder van Lansink</strong> staat <strong>preventie, dus het afval "
                  "vermijden</strong>. <strong>Op de Ladder van Lansink staat hergebruiken hoger dan "
                  "recycleren</strong>, en recycleren weer hoger dan verbranden of storten."),
            ("p", "<strong>Downcycling</strong> is <strong>afval verwerken tot iets van lagere "
                  "kwaliteit</strong>, zoals een plastic fles die tot vulmateriaal wordt. "
                  "<strong>Upcycling</strong> is het omgekeerde: recyclage waarbij "
                  "<strong>het nieuwe product méér waard is dan het oude</strong>."),
            ("p", "Het kernidee van <strong>cradle to cradle</strong> is dat "
                  "<strong>afval van het ene product grondstof is voor het volgende</strong>. De "
                  "<strong>categorieën</strong> die daarbij horen, gaan verder dan materiaal alleen: "
                  "<strong>materiaalgezondheid</strong>, <strong>productcirculariteit</strong> en "
                  "<strong>sociale rechtvaardigheid</strong>, naast hernieuwbare energie en waterbeheer."),
        ]),
        dict(kop="De woorden van de duurzame chemie", blokken=[
            ("p", "<strong>Biogebaseerd</strong> betekent <strong>gemaakt uit plantaardige of dierlijke "
                  "grondstoffen</strong>. Dat zegt alleen waar de grondstof vandaan komt, dus "
                  "<strong>is een biogebaseerde kunststof niet altijd ook biodegradeerbaar</strong>: "
                  "bio-PE uit rietsuiker blijft even lang liggen als gewone PE. "
                  "<strong>Composteerbaar</strong> is nog strenger: een materiaal dat "
                  "<strong>onder composteeromstandigheden volledig afbreekt</strong>."),
            ("p", tabel(["Waterstof", "Hoe ze gemaakt wordt"], [
                ["Grijs", "uit aardgas, met uitstoot van CO2"],
                ["Blauw", "zoals grijs, maar met afvang en opslag van de CO2"],
                ["Groen", "met hernieuwbare stroom, en daarin verschilt groene waterstof van grijze"],
            ])),
            ("p", "Bij water onderscheidt men ook kleuren. <strong>Grijs water</strong> is "
                  "<strong>licht vervuild water van bad, lavabo of wasmachine</strong>; wit water is drinkbaar "
                  "en zwart water komt uit het toilet."),
            ("p", "<strong>Een CO2-neutraal proces neemt niet meer CO2 op dan het uitstoot</strong>: het "
                  "neemt er precies even veel op, in balans. Alleen een CO2-negatief proces neemt er meer op "
                  "dan het uitstoot."),
            ("p", "<strong>Greenwashing</strong> is <strong>een product duurzamer voorstellen dan het "
                  "is</strong>: een groen blaadje op de verpakking, zonder dat er in het proces iets "
                  "veranderd is."),
            ("p", "<strong>Microplastics zijn een probleem omdat ze heel lang in het milieu blijven en in de "
                  "voedselketen komen</strong>. Ze ontstaan niet alleen uit weggegooid afval, maar ook uit "
                  "autobanden, wasbeurten van synthetische kleding en afbrokkelende verf."),
            ("p", "Beoordeel je de duurzaamheid van een proces, dan bekijk je alle energievormen die erin "
                  "zitten: <strong>fossiele energie</strong>, <strong>kernenergie</strong> en "
                  "<strong>hernieuwbare energie</strong>. Pas dan weet je of een proces echt minder weegt."),
        ]),
    ],
    onthoud=[
        "Een monomeer is de kleine molecule waaruit een kunststof opgebouwd wordt.",
        "Polyadditie gebruikt een dubbele binding; bij polycondensatie komt een kleine molecule vrij, meestal water.",
        "Een thermoplast kan je opnieuw smelten, een thermoharder niet; een elastomeer komt na vervormen terug.",
        "Een nanomateriaal is tussen 1 en 100 nanometer groot, in minstens één richting.",
        "Nanodeeltjes hebben een veel grotere verhouding van oppervlak tot volume en zijn daardoor vaak reactiever.",
        "Op de Ladder van Lansink staat preventie bovenaan en hergebruiken hoger dan recycleren.",
        "Cradle to cradle: afval van het ene product is grondstof voor het volgende.",
        "Een biogebaseerde kunststof is niet altijd biodegradeerbaar.",
        "Greenwashing is een product duurzamer voorstellen dan het is.",
    ],
)

# ───────────────────────── 14. Elektrostatica
BUNDELS["elektrostatica-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Elektrostatica",
    onder="Hoe een voorwerp geladen raakt, hoe sterk de kracht tussen ladingen is, en waarom je in een auto veilig zit bij onweer.",
    secties=[
        dict(kop="Lading, geleiders en isolatoren", blokken=[
            ("p", "Over lading gelden drie basisregels: <strong>gelijksoortige ladingen stoten elkaar "
                  "af</strong>, <strong>ongelijksoortige ladingen trekken elkaar aan</strong>, en "
                  "<strong>evenveel protonen als elektronen betekent neutraal</strong>."),
            ("p", "Het <strong>verschil tussen een geleider en een isolator op atomaire schaal</strong> is "
                  "dat <strong>een geleider vrije elektronen heeft en een isolator niet</strong>. "
                  "<strong>Breng je lading op een geleider aan, dan verspreidt die zich over het hele "
                  "voorwerp</strong>; op een isolator blijft ze liggen waar je ze zette."),
        ]),
        dict(kop="Drie manieren om te laden", blokken=[
            ("p", "<strong>Laden door wrijving.</strong> De deeltjes die daarbij verhuizen, zijn de "
                  "<strong>elektronen</strong>; protonen blijven zitten. Wrijf je twee voorwerpen tegen "
                  "elkaar, dan geldt: <strong>het ene voorwerp wordt positief en het andere negatief</strong>, "
                  "<strong>de twee ladingen zijn even groot</strong> en "
                  "<strong>er zijn elektronen van het ene naar het andere voorwerp gegaan</strong>. De "
                  "<strong>tribo-elektrische reeks</strong> dient <strong>om te bepalen welk voorwerp na "
                  "wrijving positief en welk negatief wordt</strong>."),
            ("p", "<strong>Laden door contact.</strong> Raak je <strong>een neutrale metalen bol aan met een "
                  "negatief geladen pvc-staaf</strong>, dan wordt de bol <strong>negatief</strong>: er stromen "
                  "elektronen over. <strong>Na laden door contact hebben de twee voorwerpen een lading met "
                  "hetzelfde teken</strong>, en samen houden ze de lading die er was. Raken "
                  "<strong>twee identieke metalen bollen, de ene met een lading van 8 eenheden en de andere "
                  "neutraal, elkaar even aan</strong>, dan verdeelt de lading zich gelijk: "
                  "<strong>elk 4 eenheden</strong>."),
            ("p", "<strong>Laden door influentie.</strong> <strong>Elektrostatische influentie</strong>, ook elektrostatische inductie, is "
                  "<strong>het verschuiven van ladingen in een voorwerp door een geladen voorwerp in de "
                  "buurt</strong>. In een <strong>geleider schuiven de vrije elektronen naar één kant van het "
                  "voorwerp</strong>; in een <strong>isolator worden de moleculen dipolen: de lading schuift "
                  "binnenin op</strong>. Dat laatste heet polarisatie."),
            ("p", "<strong>Een neutraal voorwerp wordt door influentie zonder aarding niet echt "
                  "geladen</strong>: de lading schuift alleen op, en zodra de staaf weg is, is alles weer "
                  "zoals het was. Met aarding wordt het anders. Houd je een "
                  "<strong>negatief geladen staaf bij een geaarde metalen bol en verbreek je daarna eerst de "
                  "aarding</strong>, dan houdt de bol een <strong>positieve</strong> lading: de weggeduwde "
                  "elektronen zijn via de aarding vertrokken en kunnen niet terug."),
            ("p", "<strong>Een geladen voorwerp houdt zijn lading niet als je het aardt</strong>: de "
                  "overtollige lading loopt dan weg naar de aarde en het voorwerp wordt neutraal."),
            ("p", "Met welk toestel je <strong>in het labo aantoont dat een voorwerp geladen is</strong>: een "
                  "<strong>elektroscoop</strong>, waarvan de blaadjes uit elkaar wijken."),
        ]),
        dict(kop="Waarom een neutraal voorwerp toch aangetrokken wordt", blokken=[
            ("p", "Een <strong>geladen staaf trekt een neutraal snippertje papier aan, omdat door influentie "
                  "de tegengestelde lading dichterbij komt</strong>. Die dichtste kant trekt harder aan dan de "
                  "verste kant afstoot, en dus blijft er aantrekking over."),
            ("p", "Hetzelfde verklaart twee alledaagse dingen. Een "
                  "<strong>reinigingsdoekje trekt stof aan</strong> doordat "
                  "<strong>het doekje geladen is en het stof door influentie aantrekt</strong>. En wrijf je "
                  "<strong>een ballon in je haar</strong> waarna hij <strong>aan de muur blijft "
                  "hangen</strong>, dan komt dat doordat <strong>de geladen ballon de muur "
                  "polariseert</strong>."),
        ]),
        dict(kop="De wet van Coulomb", blokken=[
            ("p", "De elektrische kracht is een <strong>veldkracht</strong>: ze "
                  "<strong>werkt op afstand, zonder enig contact</strong>. De "
                  "<strong>wet van Coulomb</strong> geeft <strong>de grootte van de kracht tussen twee "
                  "ladingen</strong>. Daarover geldt: <strong>de kracht is groter bij grotere "
                  "ladingen</strong>, <strong>de kracht is kleiner bij een grotere afstand</strong>, en "
                  "<strong>de afstand staat in het kwadraat in de formule</strong>."),
            ("p", "Dat kwadraat maakt het rekenwerk. Verdubbel je de afstand, dan "
                  "<strong>wordt de kracht vier keer kleiner</strong>. Breng je ze "
                  "<strong>twee keer dichter bij elkaar, dan wordt de kracht vier keer groter</strong>. Op "
                  "<strong>afstand 3r is de kracht negen keer kleiner dan F</strong>. Bij de ladingen zelf is "
                  "er geen kwadraat: <strong>verdrievoudig je één van de twee ladingen en laat je de afstand "
                  "gelijk, dan wordt de kracht drie keer groter</strong>. En omgekeerd geldt de regel "
                  "ook: <strong>hoe verder twee ladingen van elkaar liggen, hoe zwakker de kracht tussen "
                  "hen</strong>, niet sterker."),
            ("p", "Bij het <strong>voorstellen van een elektrische kracht</strong> hoort: "
                  "<strong>ze heeft een grootte, een richting en een zin</strong>, "
                  "<strong>je tekent ze als een pijl die in de lading begint</strong>, en "
                  "<strong>bij meerdere ladingen tel je de vectoren samen</strong>. <strong>Twee positieve "
                  "ladingen naast elkaar stoten elkaar af</strong>, en tussen twee gelijksoortige ladingen "
                  "werkt dus <strong>afstoting</strong>. De <strong>kracht die lading A op lading B uitoefent, "
                  "is even groot als de kracht die B op A uitoefent</strong>, ook als de ene lading veel "
                  "groter is dan de andere."),
            ("p", "Zo lees je een tekening. Zie je <strong>een vector die van lading A weg wijst, naar "
                  "lading B toe</strong>, dan weet je dat <strong>A en B ongelijksoortig zijn, want ze "
                  "trekken elkaar aan</strong>. Liggen <strong>drie ladingen op een rij</strong>, dan bepaal "
                  "je de kracht op de middelste <strong>door de twee krachtvectoren samen te tellen</strong>."),
        ]),
        dict(kop="Schermwerking", blokken=[
            ("p", "<strong>Binnen een geladen holle geleider is er geen elektrisch veld</strong>, "
                  "<strong>omdat de lading op de buitenkant zit en de velden elkaar opheffen</strong>. Zo'n "
                  "holle geleider die <strong>het binnenste beschermt tegen een elektrisch veld</strong>, heet "
                  "een <strong>kooi van Faraday</strong>."),
            ("p", "Dat merk je ook: <strong>een gsm heeft binnen een volledig gesloten metalen kast geen goed "
                  "bereik</strong>, want de golven raken er niet in of uit. "
                  "<strong>Situaties die als een kooi van Faraday werken</strong>: "
                  "<strong>een auto met een metalen dak tijdens een onweer</strong>, "
                  "<strong>een metalen kast rond gevoelige elektronica</strong> en "
                  "<strong>het metalen rooster in de deur van een magnetron</strong>."),
        ]),
        dict(kop="Toepassingen", blokken=[
            ("p", "<strong>Toepassingen die op elektrostatica werken</strong>: "
                  "<strong>een fotokopietoestel</strong>, <strong>poedercoating van metaal</strong> en "
                  "<strong>een stoffilter in een luchtzuiveraar</strong>."),
            ("p", "<strong>Poedercoating werkt met geladen poeder, omdat het poeder naar het tegengesteld "
                  "geladen metaal getrokken wordt</strong>, ook rond de hoeken, zodat er bijna niets verloren "
                  "gaat. In een <strong>elektrostatische luchtzuiveraar worden de stofdeeltjes eerst "
                  "geladen</strong>, want <strong>zo haalt een tegengesteld geladen plaat ze uit de "
                  "lucht</strong>."),
        ]),
    ],
    onthoud=[
        "Gelijksoortige ladingen stoten elkaar af, ongelijksoortige trekken elkaar aan.",
        "Een geleider heeft vrije elektronen, een isolator niet.",
        "Bij laden door wrijving verhuizen elektronen: het ene voorwerp wordt positief, het andere even sterk negatief.",
        "Na laden door contact hebben de twee voorwerpen een lading met hetzelfde teken.",
        "Influentie is het verschuiven van ladingen in een voorwerp door een geladen voorwerp in de buurt.",
        "Een geladen staaf trekt een neutraal snippertje aan, omdat door influentie de tegengestelde lading dichterbij komt.",
        "Wet van Coulomb: verdubbel je de afstand, dan wordt de kracht vier keer kleiner.",
        "Binnen een geladen holle geleider is er geen elektrisch veld; zo werkt een kooi van Faraday.",
        "Een fotokopietoestel, poedercoating en een stoffilter in een luchtzuiveraar werken op elektrostatica.",
    ],
)

# ───────────────────────── 15. Elektromagnetisme en inductie
BUNDELS["elektromagnetisme-en-inductie-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Elektromagnetisme en inductie",
    onder="Van weissgebied tot veldlijn, van Laplacekracht tot wervelstroom: hoe magnetisme en stroom elkaar maken.",
    secties=[
        dict(kop="Waar magnetisme vandaan komt", blokken=[
            ("p", "<strong>Ferromagnetisch</strong> zijn maar enkele stoffen: <strong>ijzer</strong>, "
                  "<strong>nikkel</strong> en <strong>cobalt</strong>. In zo'n stof zitten "
                  "<strong>weissgebieden</strong>, <strong>kleine gebieden die elk als een magneetje "
                  "werken</strong>. Staan ze alle kanten op, dan heft het effect zich op; wijzen ze samen "
                  "dezelfde kant uit, dan is het stuk magnetisch."),
            ("p", "Het magnetisme van een weissgebied ontstaat op atomaire schaal "
                  "<strong>uit de kringstroom en de spin van de elektronen</strong>. Magnetisme is dus "
                  "eigenlijk altijd bewegende lading, ook in een gewone koelkastmagneet."),
            ("p", "Daarom kan je een magneet niet in een losse noord- en een losse zuidpool splitsen. "
                  "<strong>Breek je een staafmagneet in twee, dan heb je twee kleinere magneten met elk een "
                  "noord- en een zuidpool</strong>. Je kan een magneet wel kwijtspelen: "
                  "<strong>een magneet kan je demagnetiseren door hem sterk op te warmen</strong>, want dan "
                  "schudt de warmte de weissgebieden weer door elkaar."),
            ("p", "<strong>Magnetische influentie</strong> is het verschijnsel waarbij "
                  "<strong>een stuk ijzer bij een magneet zelf magnetisch wordt</strong>: de weissgebieden "
                  "richten zich naar het veld. Daarom kan een magneet een hele ketting paperclips dragen."),
            ("p", "<strong>Twee noordpolen die je naar elkaar toe brengt, trekken elkaar niet aan</strong>: ze "
                  "stoten elkaar af. En de <strong>magnetische kracht is wel een veldkracht</strong>; twee "
                  "magneten hoeven elkaar niet te raken om kracht uit te oefenen, zoals je aan de afstoting "
                  "door de lucht voelt."),
        ]),
        dict(kop="Permanente magneten en elektromagneten", blokken=[
            ("p", "Het <strong>verschil tussen een permanente magneet en een elektromagneet</strong> is dat "
                  "<strong>een elektromagneet enkel werkt zolang er stroom door loopt</strong>. Dat is net "
                  "zijn voordeel: je kan hem uitzetten."),
            ("p", "Over een <strong>elektromagneet</strong> geldt: <strong>meer stroom geeft een sterker "
                  "veld</strong>, <strong>meer windingen geeft een sterker veld</strong>, en "
                  "<strong>de polen wisselen als je de stroomzin omdraait</strong>. Een "
                  "<strong>ferromagnetische kern</strong> dient <strong>om het magnetisch veld van de spoel "
                  "veel sterker te maken</strong>."),
            ("p", "<strong>Toestellen die met een elektromagneet werken</strong>: "
                  "<strong>een elektrische deurbel</strong>, <strong>een schrootkraan</strong> en "
                  "<strong>een relais</strong>."),
        ]),
        dict(kop="Veldlijnen lezen", blokken=[
            ("p", "Buiten een magneet loopt een <strong>magnetische veldlijn van de noordpool naar de "
                  "zuidpool</strong>; binnen de magneet sluit ze de kring. "
                  "<strong>Hoe dichter de veldlijnen bij elkaar liggen, hoe sterker het magnetisch veld daar "
                  "is</strong>: de veldlijnendichtheid is de maat voor de sterkte."),
            ("p", tabel(["Vorm", "Hoe het veld eruitziet"], [
                ["Staafmagneet", "het veldpatroon heet een dipoolveld, met twee polen en gebogen veldlijnen"],
                ["Tussen de benen van een hoefijzermagneet", "een homogeen veld: overal even sterk en in dezelfde richting"],
                ["Rond een rechte stroomvoerende draad", "cirkels rond de draad"],
                ["In een spoel", "binnenin bijna homogeen, buiten als bij een staafmagneet"],
            ])),
            ("p", "De <strong>rechterhandregel bij een spoel</strong> gebruik je "
                  "<strong>om uit de stroomzin te bepalen waar de noordpool ligt</strong>: de vingers met de "
                  "stroom mee, de duim wijst naar de noordpool."),
            ("p", "Bij de aarde zit er een verrassing in de namen. De "
                  "<strong>zuidpool van het aardmagnetisch veld ligt in de buurt van de geografische "
                  "noordpool</strong>, en dat moet ook zo zijn: de "
                  "<strong>noordpool van een kompasnaald wijst naar het geografische noorden</strong>, en een "
                  "noordpool wordt door een zuidpool aangetrokken."),
        ]),
        dict(kop="Kracht op stroom en op ladingen", blokken=[
            ("p", "De magnetische kracht <strong>op een stroomvoerende geleider in een magnetisch veld</strong> "
                  "heet de <strong>Laplacekracht</strong>. De kracht "
                  "<strong>op een bewegende lading</strong> heet de <strong>Lorentzkracht</strong>. Het woord "
                  "bewegende is wezenlijk: <strong>een lading die stilstaat in een magnetisch veld, ondervindt "
                  "geen magnetische kracht</strong>."),
            ("p", "Hangt een <strong>draad met stroom in een magnetisch veld</strong> en krijgt hij een kracht, "
                  "dan <strong>wijst die kracht de andere kant op als je de stroomzin omdraait</strong>. Net "
                  "daarop berust een motor die blijft draaien."),
            ("p", "<strong>Toepassingen die berusten op een kracht op bewegende ladingen of op een "
                  "stroomdraad</strong>: <strong>een gelijkstroommotor</strong>, "
                  "<strong>een luidspreker</strong> en <strong>het noorderlicht</strong>, waar het "
                  "aardmagnetisch veld geladen deeltjes naar de polen stuurt. Een "
                  "<strong>massaspectrometer</strong> gebruikt het magnetisch veld "
                  "<strong>om geladen deeltjes af te buigen volgens hun massa</strong>: zwaardere deeltjes "
                  "buigen minder af."),
        ]),
        dict(kop="Inductie", blokken=[
            ("p", "De <strong>magnetische flux</strong> is de grootheid die zegt "
                  "<strong>hoeveel magnetisch veld er door een winding gaat</strong>. Ze hangt af "
                  "<strong>van de sterkte van het magnetisch veld</strong>, "
                  "<strong>van de oppervlakte van de winding</strong> en "
                  "<strong>van de hoek tussen het veld en de normaal op de winding</strong>."),
            ("p", "Verandert die flux, dan ontstaat er spanning. Daarom geldt het omgekeerde ook: "
                  "<strong>een spoel waarin de flux niet verandert, levert geen inductiespanning</strong>. "
                  "Een magneet die stil in een spoel ligt, levert niets op."),
            ("p", "De <strong>grootte van de inductiespanning</strong> hangt af "
                  "<strong>van hoe snel de flux verandert</strong>, "
                  "<strong>van het aantal windingen van de spoel</strong> en "
                  "<strong>van de grootte van de fluxverandering</strong>. Dus: "
                  "<strong>duw je een magneet sneller in dezelfde spoel, dan wordt de inductiespanning "
                  "groter</strong>, en <strong>een spoel met meer windingen levert bij dezelfde beweging geen "
                  "kleinere maar een grotere inductiespanning</strong>."),
            ("p", "De <strong>wet van Lenz</strong> zegt dat "
                  "<strong>de inductiestroom de verandering van de flux tegenwerkt</strong>. Daarom: "
                  "<strong>trek je een magneet uit een spoel in de plaats van hem erin te duwen, dan loopt de "
                  "inductiestroom in de omgekeerde zin</strong>."),
            ("p", "Een <strong>wisselspanningsgenerator wekt spanning op doordat een winding in een "
                  "magnetisch veld draait, waardoor de flux voortdurend verandert</strong>. Dat is de hele "
                  "truc achter elke centrale."),
        ]),
        dict(kop="Wervelstromen", blokken=[
            ("p", "<strong>Wervelstromen</strong> zijn <strong>de stroompjes die in een vol stuk metaal "
                  "ontstaan als de flux erdoor verandert</strong>. Ze volgen dezelfde wet van Lenz, en dus "
                  "werken ze de verandering tegen."),
            ("p", "Daarom valt een magneet die je <strong>door een koperen buis</strong> laat vallen, "
                  "<strong>veel trager dan verwacht</strong>: <strong>de wervelstromen in het koper maken een "
                  "veld dat de val tegenwerkt</strong>. En een "
                  "<strong>elektromagnetische rem heeft geen remblokken nodig die bij elke remming "
                  "verslijten</strong>: ze remt zonder contact, wat haar bij treinen en achtbanen zo "
                  "bruikbaar maakt."),
            ("p", "Een <strong>inductiekookplaat warmt een pan op door wervelstromen in de bodem van de pan "
                  "op te wekken</strong>. De plaat zelf blijft daarbij koud, op de warmte na die de pan "
                  "teruggeeft."),
            ("p", "<strong>Toestellen die op elektromagnetische inductie werken</strong>: "
                  "<strong>een dynamo op een fiets</strong>, <strong>een elektrische gitaar</strong> en "
                  "<strong>een draadloze oplader</strong>."),
        ]),
    ],
    onthoud=[
        "IJzer, nikkel en cobalt zijn ferromagnetisch; ze bevatten weissgebieden.",
        "Breek je een staafmagneet in twee, dan heb je twee magneten met elk een noord- en een zuidpool.",
        "Een elektromagneet werkt enkel zolang er stroom door loopt; meer stroom of meer windingen geven een sterker veld.",
        "Buiten een magneet loopt een veldlijn van de noordpool naar de zuidpool.",
        "Hoe dichter de veldlijnen bij elkaar liggen, hoe sterker het magnetisch veld.",
        "De Laplacekracht werkt op een stroomvoerende geleider, de Lorentzkracht op een bewegende lading.",
        "Alleen een veranderende flux levert een inductiespanning op.",
        "Wet van Lenz: de inductiestroom werkt de verandering van de flux tegen.",
        "Een inductiekookplaat warmt een pan op door wervelstromen in de bodem van de pan.",
    ],
)

# ───────────────────────── 16. Kracht en beweging
BUNDELS["kracht-en-beweging-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kracht en beweging",
    onder="De drie soorten bewegingen aan hun grafiek herkennen, en de drie wetten van Newton gebruiken.",
    secties=[
        dict(kop="Drie soorten bewegingen", blokken=[
            ("p", tabel(["Beweging", "Afkorting", "Kenmerk"], [
                ["Eenparig rechtlijnige beweging", "ERB", "de snelheid blijft gelijk en de baan is recht"],
                ["Eenparig veranderlijke rechtlijnige beweging", "EVRB", "een rechte baan en een constante versnelling die niet nul is"],
                ["Eenparig cirkelvormige beweging", "ECB", "de grootte van de snelheid blijft gelijk, de richting van de snelheid verandert voortdurend"],
            ])),
            ("p", "Bij een <strong>eenparig cirkelvormige beweging is er wel een versnelling</strong>, ook al "
                  "verandert de snelheid niet van grootte: de richting verandert, en dat is ook een "
                  "verandering van de snelheidsvector. Die <strong>versnelling wijst naar het middelpunt van "
                  "de cirkel</strong>."),
            ("p", "Van een <strong>vertraagde beweging</strong> spreek je "
                  "<strong>als de versnelling tegen de bewegingszin in wijst</strong>. Over de versnelling bij "
                  "een <strong>EVRB</strong> geldt: <strong>ze blijft tijdens de beweging gelijk</strong>, "
                  "<strong>ze wijst mee met de beweging bij versnellen</strong> en "
                  "<strong>ze wijst tegen de beweging in bij vertragen</strong>."),
            ("p", "Over de <strong>snelheidsvector</strong> geldt: <strong>ze ligt altijd langs de "
                  "baan</strong>, <strong>ze wijst in de zin van de beweging</strong>, en "
                  "<strong>bij een cirkel raakt ze de cirkel in dat punt</strong>."),
        ]),
        dict(kop="Elke beweging in een voorbeeld", blokken=[
            ("p", tabel(["Voorbeeld", "Welke beweging"], [
                ["een auto rijdt met een constante snelheid van 50 km per uur op een rechte weg", "een ERB"],
                ["een steen valt van een toren, met de luchtweerstand verwaarloosd", "een eenparig versnelde rechtlijnige beweging"],
                ["een trein remt gelijkmatig af tot stilstand op een recht spoor", "een eenparig vertraagde rechtlijnige beweging"],
                ["een kind op een draaimolen die rond draait aan een vaste snelheid", "een eenparig cirkelvormige beweging"],
            ])),
        ]),
        dict(kop="De grafieken", blokken=[
            ("p", "Een x(t)-grafiek zet de plaats tegen de tijd, een v(t)-grafiek de snelheid tegen de tijd. "
                  "Uit <strong>de steilheid van een x(t)-grafiek</strong> lees je "
                  "<strong>de snelheid</strong> af."),
            ("p", tabel(["Beweging", "x(t)-grafiek", "v(t)-grafiek"], [
                ["ERB", "een rechte schuine lijn", "op een v(t)-grafiek van een ERB is de lijn horizontaal"],
                ["Eenparig versneld", "een parabool, dus een x(t)-grafiek die een parabool vormt is een EVRB", "een rechte schuine lijn die stijgt"],
                ["Eenparig vertraagd", "een parabool die afbuigt", "een rechte lijn die daalt; op een v(t)-grafiek van een vertraagde beweging stijgt de lijn dus niet"],
            ])),
            ("p", "Over een <strong>ERB</strong> geldt daarmee: <strong>de versnelling is nul</strong>, "
                  "<strong>de resulterende kracht is nul</strong> en <strong>de x(t)-grafiek is een rechte "
                  "schuine lijn</strong>."),
        ]),
        dict(kop="De eerste wet van Newton", blokken=[
            ("p", "De eerste wet, ook de <strong>traagheidswet</strong>, zegt: "
                  "<strong>zonder resulterende kracht blijft de snelheid van een lichaam gelijk</strong>. "
                  "Stilstaan hoort daarbij: <strong>is de resulterende kracht op een lichaam nul, dan "
                  "verandert zijn bewegingstoestand niet</strong>."),
            ("p", "Remt <strong>een bus plots en vallen de passagiers naar voren</strong>, dan verklaart "
                  "<strong>de eerste wet van Newton</strong> dat: op hen werkt geen kracht die hen meteen mee "
                  "doet vertragen, dus houden ze hun snelheid nog even aan."),
        ]),
        dict(kop="De tweede wet van Newton", blokken=[
            ("p", "De tweede wet zegt: <strong>de resulterende kracht is de massa maal de "
                  "versnelling</strong>, dus F = m·a. Dat is de wet die je nodig hebt "
                  "<strong>als je uit een kracht en een massa de versnelling wil berekenen</strong>: "
                  "<strong>de tweede</strong>."),
            ("p", "Rekenen gaat dan rechtstreeks. Werkt op een "
                  "<strong>voorwerp van 4 kg een resulterende kracht van 12 N</strong>, dan is de versnelling "
                  "12 gedeeld door 4, dus <strong>3 meter per seconde kwadraat</strong>."),
            ("p", "De twee verbanden in die formule: "
                  "<strong>verdubbel je de resulterende kracht op een voorwerp, dan verdubbelt de "
                  "versnelling</strong>, en krijgen <strong>een vrachtwagen en een auto dezelfde kracht, dan "
                  "versnelt de vrachtwagen minder, want zijn massa is groter, en massa en versnelling zijn "
                  "omgekeerd verbonden</strong>. Ken je de versnelling van een lichaam, dan weet je over de "
                  "resulterende kracht dat <strong>ze in dezelfde zin als de versnelling wijst</strong>."),
        ]),
        dict(kop="De derde wet van Newton", blokken=[
            ("p", "De derde wet is de <strong>actie-reactiewet</strong>. Daarover geldt: "
                  "<strong>de twee krachten zijn even groot</strong>, "
                  "<strong>de twee krachten hebben een tegengestelde zin</strong>, en "
                  "<strong>de twee krachten werken op verschillende lichamen</strong>. Dat laatste is waarom "
                  "ze elkaar niet opheffen."),
            ("p", "<strong>Duw je tegen een muur</strong>, dan is de reactiekracht "
                  "<strong>de kracht waarmee de muur even hard tegen jou duwt</strong>."),
            ("p", "<strong>Een raket komt niet vooruit doordat de uitgestoten gassen tegen de lucht achter de "
                  "raket duwen</strong>: dan zou hij in het luchtledige niet werken, en hij werkt er juist "
                  "beter. Het is de actie-reactiewet: de raket duwt de gassen naar achteren, de gassen duwen "
                  "de raket naar voren."),
        ]),
        dict(kop="Soorten krachten en ze samentellen", blokken=[
            ("p", "<strong>Krachten</strong> zijn onder meer <strong>de zwaartekracht</strong>, "
                  "<strong>de spankracht</strong> en <strong>de veerkracht</strong>, en daarnaast de "
                  "normaalkracht en de wrijvingskracht. De "
                  "<strong>normaalkracht</strong> is <strong>de kracht waarmee een oppervlak loodrecht op een "
                  "voorwerp duwt</strong>."),
            ("p", "Over de <strong>wrijvingskracht</strong>: <strong>ze wijst tegen de beweging in</strong>, "
                  "<strong>ze ontstaat tussen oppervlakken die over elkaar schuiven</strong>, en "
                  "<strong>een auto moet ze overwinnen om zijn snelheid te houden</strong>."),
            ("p", "<strong>Een boek dat stil op een tafel ligt, ondervindt wel krachten</strong>: de "
                  "zwaartekracht naar beneden en de normaalkracht naar boven. Ze zijn even groot en heffen "
                  "elkaar op, en daarom blijft het boek liggen; nul resulterende kracht is niet nul kracht."),
            ("p", "De <strong>resulterende kracht op een lichaam bepaal je door alle krachtvectoren samen te "
                  "tellen</strong>. Werkt <strong>een kracht schuin op een voorwerp</strong>, dan "
                  "<strong>ontbind je ze in een x-component en een y-component</strong> en reken je elke "
                  "richting apart."),
        ]),
    ],
    onthoud=[
        "ERB: gelijke snelheid en rechte baan. EVRB: rechte baan en constante versnelling die niet nul is.",
        "Bij een eenparig cirkelvormige beweging wijst de versnelling naar het middelpunt van de cirkel.",
        "Bij een vertraagde beweging wijst de versnelling tegen de bewegingszin in.",
        "Een steen die valt zonder luchtweerstand voert een eenparig versnelde rechtlijnige beweging uit.",
        "De steilheid van een x(t)-grafiek geeft de snelheid; bij een ERB is de v(t)-grafiek horizontaal.",
        "Eerste wet van Newton: zonder resulterende kracht blijft de snelheid van een lichaam gelijk.",
        "Tweede wet van Newton: F = m·a, de resulterende kracht is de massa maal de versnelling.",
        "Derde wet: actie en reactie zijn even groot, tegengesteld van zin en werken op verschillende lichamen.",
        "De resulterende kracht bepaal je door alle krachtvectoren samen te tellen.",
    ],
)

# ───────────────────────── 17. Trillingen, golven en geluid
BUNDELS["trillingen-golven-en-geluid-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Trillingen, golven en geluid",
    onder="Van amplitude en periode naar resonantie, en van golflengte naar de decibelschaal.",
    secties=[
        dict(kop="De harmonische trilling", blokken=[
            ("p", "Een trilling beweegt heen en weer rond de <strong>evenwichtsstand</strong>, "
                  "<strong>de stand waarrond een trillend voorwerp heen en weer beweegt</strong>. De "
                  "<strong>amplitude</strong> is <strong>de grootste uitwijking vanuit de "
                  "evenwichtsstand</strong>. De <strong>periode</strong> is "
                  "<strong>de tijd die één volledige trilling duurt</strong>."),
            ("p", "De frequentie is het aantal trillingen per seconde, dus één gedeeld door de periode. Heeft "
                  "een <strong>trilling een periode van 0,5 seconde</strong>, dan is de frequentie "
                  "<strong>2 hertz</strong>."),
            ("p", "Amplitude en frequentie staan los van elkaar: <strong>een grotere amplitude betekent niet "
                  "altijd ook een grotere frequentie</strong>. Je kan harder duwen zonder sneller te duwen."),
            ("p", "Van de <strong>y(t)-grafiek van een trilling</strong> lees je "
                  "<strong>de amplitude</strong>, <strong>de periode</strong> en "
                  "<strong>de evenwichtslijn</strong> af."),
        ]),
        dict(kop="Resonantie", blokken=[
            ("p", "De <strong>eigenfrequentie</strong> is <strong>de frequentie waarmee een voorwerp vanzelf "
                  "het liefst trilt</strong>. <strong>Resonantie treedt op als de uitwendige kracht de "
                  "eigenfrequentie treft</strong>: dan wordt elke duw op het juiste moment gegeven en lopen de "
                  "uitwijkingen op."),
            ("p", "<strong>Voorbeelden van resonantie</strong>: "
                  "<strong>een schommel die hoger komt door op het juiste ritme te duwen</strong>, "
                  "<strong>een glas dat barst bij één bepaalde zangtoon</strong> en "
                  "<strong>een brug die schudt door marcherende voeten erop</strong>."),
        ]),
        dict(kop="Golven", blokken=[
            ("p", "Een golf <strong>transporteert energie, maar geen materie</strong>. "
                  "<strong>De deeltjes van een golf verhuizen niet met de golf mee naar het einde</strong>: "
                  "ze trillen op hun plaats en geven de beweging door, zoals het publiek in een stadion."),
            ("p", "Dat is ook het <strong>verschil tussen de trilrichting en de voortplantingsrichting</strong>: "
                  "<strong>de deeltjes bewegen in de trilrichting, de golf reist in de andere</strong>."),
            ("p", "<strong>Mechanische golven</strong> hebben een middenstof nodig: "
                  "<strong>geluid</strong>, <strong>golven op het water</strong> en "
                  "<strong>een golf in een gespannen touw</strong>. Daarom "
                  "<strong>kan een mechanische golf zich niet door het luchtloze heelal "
                  "voortplanten</strong>, en is het heelal stil; elektromagnetische golven raken er wel door."),
            ("p", "Een golf is transversaal of longitudinaal. Bij een <strong>transversale golf trillen de "
                  "deeltjes loodrecht op de golfrichting</strong>; "
                  "bij een longitudinale golf trillen ze in de golfrichting zelf. "
                  "<strong>Geluid in lucht is longitudinaal</strong>: opeenvolgende verdichtingen en "
                  "verdunningen."),
            ("p", "De <strong>golflengte</strong> is <strong>de afstand tussen twee punten in dezelfde "
                  "fase</strong>, bijvoorbeeld van top tot top. De golfsnelheid is de golflengte maal de "
                  "frequentie. Heeft een <strong>golf een golflengte van 2 meter en een frequentie van 5 "
                  "hertz</strong>, dan gaat ze <strong>10 meter per seconde</strong>. "
                  "<strong>Bij een vaste golfsnelheid hoort een grotere frequentie bij een kleinere "
                  "golflengte</strong>."),
            ("p", "Let op welke grafiek je bekijkt: van een "
                  "<strong>y(x)-grafiek van een golf</strong> lees je <strong>de golflengte</strong> af, en "
                  "dat lukt niet met een y(t)-grafiek, want daar staat de tijd op de horizontale as."),
        ]),
        dict(kop="Geluid", blokken=[
            ("p", "Geluid gaat het snelst <strong>in een vaste stof</strong>, omdat de deeltjes daar dicht bij "
                  "elkaar zitten en de beweging snel doorgeven; in een gas gaat het traagst. Ook de "
                  "temperatuur telt: <strong>geluid gaat sneller in warme lucht dan in koude lucht</strong>."),
            ("p", tabel(["Wat je hoort", "Waarvan het afhangt"], [
                ["Toonhoogte", "van de frequentie van de geluidsgolf"],
                ["Luidheid of toonsterkte", "van de amplitude"],
                ["Klankkleur", "van de vorm van het patroon op een y(t)-grafiek; zo zie je het verschil tussen een viool en een fluit die dezelfde toon spelen"],
            ])),
            ("p", "Hoor je <strong>een lage, zachte toon</strong>, dan weet je over de golf dat "
                  "<strong>ze een lage frequentie en een kleine amplitude heeft</strong>."),
            ("p", "Een mens hoort normaal <strong>van ongeveer 20 tot 20 000 hertz</strong>. Daarboven heet "
                  "geluid <strong>ultrasoon</strong>; daaronder infrasoon. "
                  "<strong>Infrasoon geluid heeft geen hogere frequentie dan geluid dat wij kunnen "
                  "horen</strong>, maar een lagere, zoals het gerommel van een aardbeving."),
        ]),
        dict(kop="De decibelschaal en je gehoor", blokken=[
            ("p", "De <strong>gehoordrempel</strong> ligt op <strong>0 decibel</strong>: het zachtste geluid "
                  "dat een mens nog kan horen. Vanaf ongeveer <strong>80 decibel</strong> is "
                  "<strong>gehoorbescherming nodig</strong>, en rond 120 decibel ligt de pijndrempel. "
                  "<strong>Hoe langer je aan luid geluid blootgesteld bent, hoe groter de kans op "
                  "gehoorschade</strong>, want niveau en tijd tellen samen."),
            ("p", "De schaal is niet recht. <strong>Twee keer zoveel geluidsintensiteit betekent niet twee keer "
                  "zoveel decibel</strong>: wordt <strong>de geluidsintensiteit twee keer groter</strong>, dan "
                  "<strong>stijgt het geluidsniveau met ongeveer 3 decibel</strong>. Ga je "
                  "<strong>twee keer zo ver van een geluidsbron staan</strong>, dan zakt het niveau "
                  "<strong>met ongeveer 6 decibel</strong>."),
            ("p", "<strong>Blijvende gehoorschade ontstaat in het binnenoor, bij de haarcellen</strong>. Die "
                  "groeien niet terug, en daarom is schade daar definitief. "
                  "<strong>Maatregelen die je gehoor beschermen</strong>: "
                  "<strong>oordopjes of een gehoorkap dragen</strong>, "
                  "<strong>verder van de geluidsbron gaan staan</strong> en "
                  "<strong>de blootstelling in tijd beperken</strong>."),
        ]),
        dict(kop="Toepassingen met geluid", blokken=[
            ("p", "Een <strong>echo</strong> is <strong>het terugkaatsen van geluid tegen een wand, waardoor "
                  "je het een tweede keer hoort</strong>. Uit de tijd tussen zenden en terugkomen kan je "
                  "afstand berekenen, en daarop berust het meeste."),
            ("p", "<strong>Toepassingen die met geluidsgolven werken</strong>: "
                  "<strong>echografie</strong>, <strong>sonar op een schip</strong> en "
                  "<strong>echolocatie bij een vleermuis</strong>."),
            ("p", "Over een <strong>echografie</strong> geldt: <strong>ze werkt met ultrasoon geluid</strong>, "
                  "<strong>ze meet wat er tegen de grens tussen weefsels terugkaatst</strong>, en "
                  "<strong>uit de tijd berekent het toestel de diepte</strong>. Er komt dus geen straling aan "
                  "te pas, en net daarom mag ze bij een zwangerschap."),
        ]),
    ],
    onthoud=[
        "De amplitude is de grootste uitwijking, de periode de tijd van één volledige trilling.",
        "Frequentie is één gedeeld door de periode: een periode van 0,5 seconde geeft 2 hertz.",
        "Resonantie treedt op als de uitwendige kracht de eigenfrequentie treft.",
        "Een golf transporteert energie, maar geen materie.",
        "Bij een transversale golf trillen de deeltjes loodrecht op de golfrichting; geluid in lucht is longitudinaal.",
        "De golfsnelheid is de golflengte maal de frequentie.",
        "Toonhoogte hangt af van de frequentie, luidheid van de amplitude.",
        "Vanaf ongeveer 80 decibel is gehoorbescherming nodig.",
        "Echografie werkt met ultrasoon geluid en meet wat tegen de grens tussen weefsels terugkaatst.",
    ],
)

# ───────────────────────── 18. Het elektromagnetisch spectrum
BUNDELS["het-elektromagnetisch-spectrum-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Het elektromagnetisch spectrum",
    onder="Het hele spectrum op een rij, wat straling met materie doet, en waar je elke soort tegenkomt.",
    secties=[
        dict(kop="Wat een elektromagnetische golf is", blokken=[
            ("p", "Een elektromagnetische golf is <strong>een transversale golf die geen middenstof nodig "
                  "heeft</strong>. In vacuüm beweegt ze met <strong>de lichtsnelheid</strong>, en wel allemaal "
                  "even snel: <strong>gammastraling gaat in vacuüm niet sneller dan radiogolven</strong>. "
                  "Wat wel verandert, is de snelheid in materie: "
                  "<strong>een elektromagnetische golf gaat trager als ze van vacuüm in glas komt</strong>."),
        ]),
        dict(kop="Het spectrum op een rij", blokken=[
            ("p", "Van lage naar hoge frequentie: "
                  "<strong>radio, microgolven, infrarood, zichtbaar licht, ultraviolet, röntgen, "
                  "gamma</strong>."),
            ("p", tabel(["Straling", "Golflengte", "Energie"], [
                ["Radiogolven", "de grootste golflengte van het hele spectrum", "de laagste energie"],
                ["Microgolven", "groot, niet zichtbaar, niet ioniserend", "laag"],
                ["Infrarood", "zit net naast het rode licht, aan de kant van de langere golven", "laag"],
                ["Zichtbaar licht", "het enige deel dat een mens kan zien, van rood tot violet", "midden"],
                ["Ultraviolet", "korter dan violet", "hoog; het hoogenergetische deel is ioniserend"],
                ["Röntgen", "heel klein", "heel hoog, ioniserend"],
                ["Gamma", "de kleinste golflengte", "de hoogste energie van het hele spectrum, en het grootste doordringend vermogen"],
            ])),
            ("p", "De drie grootheden hangen vast aan elkaar. <strong>Een grotere golflengte hoort bij een "
                  "lagere frequentie</strong>, en over een golf met een <strong>hoge frequentie</strong> geldt: "
                  "<strong>haar golflengte is klein</strong>, <strong>haar energie is groot</strong> en "
                  "<strong>ze zit aan de kant van röntgen en gamma</strong>."),
            ("p", "Er bestaan meerdere <strong>indelingen van elektromagnetische straling</strong> naast "
                  "elkaar: <strong>zichtbaar en niet-zichtbaar</strong>, "
                  "<strong>schadelijk en niet-schadelijk</strong> en "
                  "<strong>ioniserend en niet-ioniserend</strong>. Welke indeling je kiest, hangt af van "
                  "waarover je het hebt."),
            ("p", "<strong>Ioniserend</strong> zijn <strong>gammastraling</strong>, "
                  "<strong>röntgenstraling</strong> en <strong>hoogenergetische uv-straling</strong>: ze "
                  "hebben genoeg energie om elektronen uit atomen te slaan. Daarom is "
                  "<strong>uv-straling gevaarlijker voor je huid dan zichtbaar licht</strong>: "
                  "<strong>uv heeft meer energie per golf en kan in cellen schade aanrichten</strong>. Maar "
                  "<strong>niet elke soort elektromagnetische straling is schadelijk voor de mens</strong>: "
                  "radiogolven en infrarood dragen daarvoor te weinig energie, en "
                  "<strong>een gsm werkt met straling die niet ioniserend is</strong>."),
            ("p", "Het <strong>doordringend vermogen</strong> van een straling is "
                  "<strong>hoe diep ze in materie kan binnendringen</strong>. Dat is iets anders dan haar "
                  "energie, al lopen ze bij het spectrum samen op."),
            ("p", "Zo kan je raden welke straling bedoeld is. Weet je dat een straling "
                  "<strong>niet zichtbaar is, een lange golflengte heeft en niet ioniserend is</strong>, dan "
                  "kunnen dat <strong>microgolven</strong> zijn."),
        ]),
        dict(kop="Straling en materie", blokken=[
            ("p", "Valt straling op materie, dan kunnen er drie dingen gebeuren: "
                  "<strong>absorberen, doorlaten of weerkaatsen</strong>. "
                  "<strong>Transmissie</strong> is de naam voor het verschijnsel waarbij "
                  "<strong>straling door een stof heen gaat</strong>."),
            ("p", "Welke van de drie het wordt, verklaart wat je ziet. "
                  "<strong>Gras is groen omdat het het groene licht weerkaatst en de andere kleuren "
                  "absorbeert</strong>. En <strong>op een röntgenfoto zijn de botten wit omdat ze meer "
                  "straling absorberen dan het zachte weefsel</strong>."),
            ("p", "Een toepassing die <strong>straling door een voorwerp stuurt en meet wat er aan de andere "
                  "kant aankomt</strong>, gebruikt dus <strong>transmissie en absorptie</strong>. Meet men "
                  "<strong>in een fabriek de dikte van een metalen plaat met straling</strong>, dan is "
                  "<strong>straling die diep doordringt, zoals gamma</strong>, daarvoor logisch; licht zou al "
                  "aan de oppervlakte blijven."),
        ]),
        dict(kop="Waar je elke straling tegenkomt", blokken=[
            ("p", "<strong>Radiogolven gebruikt men voor communicatie over grote afstand, omdat ze ver dragen "
                  "en niet snel geabsorbeerd worden</strong>. Daarmee werken "
                  "<strong>een wifinetwerk</strong>, <strong>een gsm</strong> en "
                  "<strong>televisie via een antenne</strong>."),
            ("p", "Een <strong>magnetron gebruikt microgolven</strong>, want "
                  "<strong>de watermoleculen in het eten nemen die energie goed op</strong>. Het "
                  "<strong>metalen rooster in de deur houdt de microgolven binnen, omdat het als een kooi van "
                  "Faraday werkt</strong>."),
            ("p", "Met <strong>infrarood</strong> werkt <strong>een afstandsbediening van een "
                  "televisie</strong>, en ook <strong>een warmtebeeldcamera of een nachtkijker werkt met "
                  "infraroodstraling</strong>, want elk warm lichaam straalt infrarood uit."),
            ("p", "Met <strong>ultraviolette straling</strong> werken "
                  "<strong>een zonnebank</strong>, <strong>een valsgelddetector</strong> en "
                  "<strong>desinfectie van water of oppervlakken</strong>. Een toestel dat "
                  "<strong>met onzichtbare straling bacteriën doodt in een waterleiding</strong>, werkt dus met "
                  "<strong>ultraviolette straling</strong>. <strong>Een blacklight werkt niet met "
                  "infraroodstraling</strong> maar met uv, en net daarom licht wit wasgoed eronder op."),
            ("p", "Met <strong>röntgenstraling</strong> werkt onder meer "
                  "<strong>een bagagescanner op een luchthaven</strong>, naast de röntgenfoto bij de dokter. "
                  "<strong>Gammastraling gebruikt men om voedsel te steriliseren, want haar hoge energie doodt "
                  "de micro-organismen erin</strong>, en bij <strong>radiotherapie tegen kanker</strong> "
                  "gebruikt men <strong>gammastraling</strong> om kankercellen te doden."),
        ]),
        dict(kop="Bescherming", blokken=[
            ("p", "Tegen <strong>röntgen- en gammastraling</strong> bescherm je je "
                  "<strong>met een loodschort of een dikke betonnen wand</strong>. De drie maatregelen die bij "
                  "<strong>bescherming tegen hoogenergetische straling</strong> horen, zijn: "
                  "<strong>een loodschort dragen</strong>, <strong>afstand houden van de bron</strong> en "
                  "<strong>de tijd bij de bron zo kort mogelijk houden</strong>. Afscherming, afstand en tijd: "
                  "die drie samen."),
            ("p", "Tegen uv werkt iets eenvoudigers: "
                  "<strong>zonnecrème en een zonnebril met uv-filter beschermen tegen ultraviolette "
                  "straling</strong>."),
        ]),
    ],
    onthoud=[
        "Een elektromagnetische golf is transversaal en heeft geen middenstof nodig.",
        "In vacuüm gaan alle elektromagnetische golven even snel: met de lichtsnelheid.",
        "Van lage naar hoge frequentie: radio, microgolven, infrarood, zichtbaar licht, ultraviolet, röntgen, gamma.",
        "Een hoge frequentie hoort bij een kleine golflengte en een grote energie.",
        "Gammastraling, röntgenstraling en hoogenergetische uv-straling zijn ioniserend.",
        "Straling die op materie valt, wordt geabsorbeerd, doorgelaten of weerkaatst.",
        "Op een röntgenfoto zijn de botten wit, omdat ze meer straling absorberen dan het zachte weefsel.",
        "Een magnetron gebruikt microgolven; een afstandsbediening werkt met infrarood.",
        "Bescherming tegen hoogenergetische straling: afscherming, afstand en tijd.",
    ],
)

# ───────────────────────── 19. Kernfysica en radioactiviteit
BUNDELS["kernfysica-en-radioactiviteit-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Kernfysica en radioactiviteit",
    onder="Wat er in een kern gebeurt, hoe je met halveringstijd rekent, en hoe je je tegen straling beschermt.",
    secties=[
        dict(kop="De bouw van een kern", blokken=[
            ("p", "De <strong>nucleonen</strong>, of kerndeeltjes, zijn <strong>de protonen en de neutronen van "
                  "een kern samen</strong>. Over een <strong>nuclide</strong> geldt: "
                  "<strong>het atoomnummer Z is het aantal protonen</strong>, "
                  "<strong>het massagetal A is het aantal nucleonen</strong>, en "
                  "<strong>het aantal neutronen is A min Z</strong>. Het "
                  "<strong>massagetal A is dus het aantal protonen plus het aantal neutronen</strong>."),
            ("p", "Daarmee reken je meteen. Heeft een <strong>nuclide massagetal 23 en atoomnummer 11</strong>, "
                  "dan zitten er 23 min 11, dus <strong>12</strong> neutronen in de kern. Een nuclide "
                  "<strong>schrijf je met het massagetal en het atoomnummer bij het symbool</strong> van het "
                  "element."),
            ("p", "<strong>Isotopen</strong> van hetzelfde element hebben <strong>het aantal protonen</strong> "
                  "gemeen en <strong>een verschillend aantal neutronen</strong>. Ze zijn chemisch bijna "
                  "identiek, maar niet even stabiel."),
        ]),
        dict(kop="Stabiel of niet", blokken=[
            ("p", "In een atoomkern strijden <strong>twee krachten</strong> met elkaar: "
                  "<strong>de sterke kernkracht en de afstoting van de protonen</strong>. De kernkracht trekt "
                  "alle nucleonen samen maar werkt enkel over heel korte afstand; de coulombkracht tussen de "
                  "protonen stoot af en werkt verder."),
            ("p", "Daarom hangt stabiliteit af van de verhouding. Een "
                  "<strong>lichte kern met Z kleiner dan 20 is doorgaans stabiel als er ongeveer evenveel "
                  "neutronen als protonen zijn</strong>. Bij zware kernen schuift dat op: "
                  "<strong>een zware stabiele kern heeft niet meer protonen dan neutronen</strong>, maar juist "
                  "meer neutronen, want die verdunnen de afstoting zonder eraan bij te dragen."),
            ("p", "De <strong>nuclidenkaart</strong> is <strong>de kaart waarop je stabiele en onstabiele "
                  "nucliden terugvindt</strong>. De stabiele kernen vormen daarop een band. Ligt een "
                  "<strong>kern onder de stabiliteitsband en heeft ze te veel neutronen</strong>, dan vervalt "
                  "ze <strong>via bètaverval, want zo wordt een neutron een proton</strong>."),
            ("p", "<strong>Een stabiele kern vervalt niet na verloop van tijd</strong>: ze blijft zoals ze is. "
                  "Alleen onstabiele kernen vervallen."),
        ]),
        dict(kop="Halveringstijd en activiteit", blokken=[
            ("p", "De <strong>halveringstijd</strong> van een radionuclide is <strong>de tijd waarin de helft "
                  "van de kernen vervalt</strong>. De <strong>activiteit</strong> is "
                  "<strong>het aantal kernen dat per seconde vervalt</strong>."),
            ("p", "Rekenen met halveringstijden gaat met halveringen. Begin je met "
                  "<strong>800 onstabiele kernen</strong> en is de <strong>halveringstijd 5 jaar</strong>, dan "
                  "zijn er na 15 jaar drie halveringen gebeurd: 800, 400, 200, dus "
                  "<strong>100</strong> blijven er over."),
            ("p", "Over <strong>halveringstijd en activiteit</strong> geldt: "
                  "<strong>de activiteit zakt met de tijd</strong>, "
                  "<strong>een korte halveringstijd hoort bij een onstabiele kern</strong>, en "
                  "<strong>na twee halveringstijden blijft een kwart over</strong>. Bijgevolg heeft "
                  "<strong>een radionuclide met een korte halveringstijd bij dezelfde hoeveelheid een hogere "
                  "activiteit</strong>: dezelfde kernen in minder tijd."),
            ("p", "De <strong>grafiek van het aantal onstabiele kernen in functie van de tijd</strong> is "
                  "<strong>een kromme die steeds trager naar nul zakt</strong>, nooit een rechte. Om de "
                  "<strong>halveringstijd uit een N(t)-grafiek</strong> te halen: "
                  "<strong>je zoekt wanneer het aantal tot de helft gezakt is</strong>, "
                  "<strong>je mag van elk punt van de kromme vertrekken</strong> en "
                  "<strong>je leest het resultaat op de tijdas af</strong>. Dat je van elk punt mag vertrekken, "
                  "is juist het bijzondere aan een halveringstijd."),
        ]),
        dict(kop="Fusie, splijting en de kerncentrale", blokken=[
            ("p", "<strong>Kernfusie</strong> is <strong>twee lichte kernen die tot één zwaardere kern "
                  "samensmelten</strong>, zoals in de zon. <strong>Kernsplijting</strong> is het omgekeerde, en "
                  "dat is het proces dat <strong>een kerncentrale gebruikt om energie op te wekken</strong>. "
                  "<strong>Bij de fusie van lichte kernen en bij de splijting van zware kernen komt er energie "
                  "vrij</strong>, en dat lijkt tegenstrijdig tot je naar de specifieke rustenergie per nucleon "
                  "kijkt: beide bewegingen gaan naar het stabielere midden toe, en het massaverschil komt als "
                  "energie vrij volgens E = mc²."),
            ("p", "Een gewone kerncentrale gebruikt <strong>uraan</strong> als splijtstof. "
                  "<strong>Onderdelen van een kerncentrale</strong>: <strong>het reactorvat</strong>, "
                  "<strong>de stoomgenerator</strong> en <strong>de turbine</strong>. De "
                  "<strong>regelstaven in een kernreactor vangen neutronen weg en regelen zo de "
                  "kettingreactie</strong>: schuif ze "
                  "verder in, en de reactie zakt."),
            ("p", "<strong>Radioactief afval wordt ingedeeld volgens de intensiteit en de duur van de "
                  "straling</strong>. <strong>Categorie A</strong> is "
                  "<strong>kortlevend laag- en middelactief afval</strong>; categorie B en C zijn langlevend of "
                  "hoogactief. <strong>Hoogactief afval mag niet met dezelfde bescherming behandeld worden als "
                  "laagactief afval</strong>: het vraagt veel zwaardere afscherming en koeling."),
        ]),
        dict(kop="Drie soorten straling", blokken=[
            ("p", tabel(["Straling", "Wat ze is", "Ioniserend vermogen", "Doordringend vermogen"], [
                ["Alfa", "een heliumkern met twee protonen en twee neutronen", "groot", "klein: een blad papier houdt ze al tegen"],
                ["Bèta", "een elektron dat de kern verlaat", "middelmatig", "middelmatig: een plaatje aluminium stopt ze"],
                ["Gamma", "een elektromagnetische golf", "klein", "het grootste van de drie: lood of dik beton is nodig"],
            ])),
            ("p", "<strong>Alfastraling heeft een groot ioniserend vermogen maar een klein doordringend "
                  "vermogen</strong>. Daarom geldt: <strong>een blad papier houdt ze al tegen</strong>, "
                  "<strong>ze raakt niet door de buitenste laag van je huid</strong>, maar "
                  "<strong>ze is vooral gevaarlijk na inslikken of inademen</strong>, want binnen in je lichaam "
                  "staat er geen huid meer tussen."),
            ("p", "Bij verval veranderen massagetal en atoomnummer volgens vaste regels. Bij "
                  "<strong>alfaverval zakt het massagetal met 4 en het atoomnummer met 2</strong>. Bij "
                  "<strong>bètaverval wordt een neutron een proton en vertrekt er een elektron</strong>, dus "
                  "blijft het massagetal gelijk en stijgt het atoomnummer met 1."),
            ("p", "In een magnetisch veld verraden ze zich. Alfa en bèta zijn geladen en buigen af, in "
                  "tegengestelde richting, en bèta het sterkst omdat ze zo licht is. "
                  "<strong>Gammastraling buigt in een magnetisch veld niet even sterk af als "
                  "bètastraling</strong>: ze buigt helemaal niet af, want ze heeft geen lading."),
        ]),
        dict(kop="Dosis en bescherming", blokken=[
            ("p", "Het <strong>verschil tussen bestraling en besmetting</strong>: bij "
                  "<strong>besmetting</strong> komt de radioactieve stof op of in je lichaam, bij bestraling "
                  "sta je enkel in de straling en blijft er niets achter. Een besmetting kan uitwendig of "
                  "inwendig zijn, en blijft doorstralen tot de stof weg of vervallen is."),
            ("p", "De geabsorbeerde dosis meet je in gray. De "
                  "<strong>equivalente dosis en de effectieve dosis</strong> druk je uit in "
                  "<strong>sievert</strong>: daar zit de stralingsweegfactor in, die zegt hoe schadelijk een "
                  "soort straling per gray is. <strong>Alfastraling heeft een veel hogere stralingsweegfactor "
                  "dan bèta- of gammastraling, omdat ze al haar energie in een heel klein stukje weefsel "
                  "afgeeft</strong>."),
            ("p", "<strong>Toepassingen van ioniserende straling</strong>: "
                  "<strong>radiotherapie tegen kanker</strong>, "
                  "<strong>de koolstof-14-methode om ouderdom te bepalen</strong> en "
                  "<strong>een PET-scan met een radioactieve tracer</strong>."),
        ]),
    ],
    onthoud=[
        "Het massagetal A is het aantal nucleonen; het aantal neutronen is A min Z.",
        "Isotopen hebben hetzelfde aantal protonen en een verschillend aantal neutronen.",
        "In een kern strijden de sterke kernkracht en de afstoting van de protonen.",
        "Een kern met te veel neutronen vervalt via bètaverval: een neutron wordt een proton.",
        "De halveringstijd is de tijd waarin de helft van de kernen vervalt; na twee halveringstijden blijft een kwart over.",
        "Een kerncentrale gebruikt kernsplijting; regelstaven vangen neutronen weg en regelen zo de kettingreactie.",
        "Alfastraling heeft een groot ioniserend maar een klein doordringend vermogen: een blad papier houdt ze al tegen.",
        "Bij alfaverval zakt het massagetal met 4 en het atoomnummer met 2.",
        "De equivalente en de effectieve dosis druk je uit in sievert.",
    ],
)

# ───────────────────────── 20. Veilig en duurzaam werken, grootheden en eenheden
BUNDELS["veilig-en-duurzaam-werken-grootheden-en-eenheden-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Veilig en duurzaam werken, grootheden en eenheden",
    onder="Etiketten lezen, netjes meten, en met eenheden, voorvoegsels en verbanden werken.",
    secties=[
        dict(kop="Etiketten en veilig werken", blokken=[
            ("p", "Een <strong>gevarenpictogram op een fles met een chemische stof</strong> vertelt "
                  "<strong>waarom de stof gevaarlijk is</strong>. Daarnaast staan er twee soorten zinnen op "
                  "een etiket: in een <strong>H-zin</strong> staat <strong>welk gevaar de stof "
                  "oplevert</strong>, en de <strong>P-zinnen</strong> zeggen "
                  "<strong>hoe je veilig met een stof omgaat</strong>."),
            ("p", "Waarschuwt het etiket voor gevaar voor de huid, dan doe je drie dingen samen: "
                  "<strong>handschoenen dragen</strong>, <strong>een veiligheidsbril dragen</strong> en "
                  "<strong>de P-zinnen van het etiket volgen</strong>."),
            ("p", "<strong>Werkwijzen die bij veilig en duurzaam werken in een labo horen</strong>: "
                  "<strong>zuinig omgaan met chemische stoffen</strong>, "
                  "<strong>meetinstrumenten uitzetten als je niet meet</strong> en "
                  "<strong>glaswerk na gebruik schoonmaken</strong>. Je "
                  "<strong>zet een meetinstrument uit als je niet meet om energie te sparen en de batterij te "
                  "ontzien</strong>, en je <strong>leest de handleiding van een toestel voor je het gebruikt om "
                  "te weten hoe je het veilig gebruikt</strong>."),
            ("p", "Drie regels over opruimen. <strong>Een gemorst chemisch product ruim je beter onmiddellijk "
                  "op</strong>, voor iemand erin stapt of het indroogt. "
                  "<strong>Glasscherven</strong> ruim je op <strong>met een borstel en een blik, in het vat "
                  "voor glas</strong>, nooit met je handen. En "
                  "<strong>afval van een chemisch product mag je niet gewoon in de gootsteen gieten</strong>: "
                  "dat hoort in het vat voor chemisch afval."),
        ]),
        dict(kop="Meten", blokken=[
            ("p", "Het <strong>meetbereik</strong> van een meetinstrument is <strong>de kleinste en de grootste "
                  "waarde die het kan meten</strong>. De <strong>nauwkeurigheid</strong> is iets anders: "
                  "<strong>de kleinste verandering die een meetinstrument nog kan weergeven</strong>."),
            ("p", "Daarmee kies je je toestel. Moet je een "
                  "<strong>massa van ongeveer 2 gram op een tienden van een gram nauwkeurig wegen</strong>, "
                  "dan neem je <strong>een balans die tot op 0,01 gram nauwkeurig weegt</strong>: één stap "
                  "fijner dan wat je nodig hebt. Maar "
                  "<strong>een duurder meetinstrument is niet altijd het beste voor elk onderzoek</strong>; het "
                  "moet passen bij wat je meet."),
            ("p", tabel(["Meetinstrument", "Wat het meet"], [
                ["Dynamometer", "een kracht"],
                ["Voltmeter", "een elektrische spanning"],
                ["Chronometer", "een tijd"],
                ["Decibelmeter", "een geluidsniveau"],
                ["Balans", "een massa"],
            ])),
            ("p", "<strong>Een meting met een meetinstrument is nooit helemaal exact.</strong> Daarom let je op "
                  "twee dingen. Je leest <strong>een vloeistofniveau in een maatcilinder op ooghoogte af om een "
                  "fout door de kijkhoek te vermijden</strong>. En je schrijft niet meer cijfers op dan je kan "
                  "meten: <strong>meet je met een lintmeter in centimeters en schrijf je 12,3456 cm op, dan "
                  "schrijf je meer cijfers op dan je kan meten</strong>."),
        ]),
        dict(kop="Grootheden en eenheden", blokken=[
            ("p", "Het <strong>verschil tussen een grootheid en een eenheid</strong>: "
                  "<strong>een grootheid is wat je meet, een eenheid is waarin je het uitdrukt</strong>. Lengte "
                  "is een grootheid, de meter is haar eenheid."),
            ("p", "<strong>SI-eenheden</strong> zijn onder meer <strong>de meter</strong>, "
                  "<strong>de seconde</strong> en <strong>de ampère</strong>. De "
                  "<strong>SI-eenheid van massa</strong> is de <strong>kilogram</strong>, en niet de gram: dat "
                  "is de enige SI-eenheid met een voorvoegsel erin."),
            ("p", tabel(["Voorvoegsel", "Factor"], [
                ["mega", "een miljoen"],
                ["kilo", "duizend"],
                ["milli", "een duizendste"],
                ["micro", "een miljoenste"],
                ["nano", "een miljardste"],
            ])),
            ("p", "Omzetten doe je met die factoren. <strong>2,5 kilometer</strong> is "
                  "<strong>2500 meter</strong>, en <strong>0,25 milliseconde</strong> is "
                  "<strong>0,00025 seconde</strong>."),
            ("p", "Voor heel grote en heel kleine getallen gebruik je de "
                  "<strong>wetenschappelijke notatie</strong>, waarin "
                  "<strong>precies één cijfer voor de komma staat</strong>. Zo wordt "
                  "<strong>0,00042 meter</strong> geschreven als "
                  "<strong>4,2 maal tien tot de min vier</strong>."),
            ("p", "Bij het rekenen houd je je aan de beduidende cijfers. Meet je "
                  "<strong>3,0 cm en 4,00 cm en telt je die op</strong>, dan schrijf je het resultaat "
                  "<strong>met één cijfer na de komma</strong>, want de minst nauwkeurige meting bepaalt het "
                  "antwoord. <strong>Een rekenmachine die acht cijfers na de komma toont, maakt je meting niet "
                  "nauwkeuriger</strong>, en <strong>een schatting vooraf is niet overbodig zodra je met een "
                  "rekenmachine werkt</strong>: ze is juist je enige bescherming tegen een tikfout."),
        ]),
        dict(kop="Verbanden en formules", blokken=[
            ("p", tabel(["Verband", "Hoe je het herkent"], [
                ["Recht evenredig", "de grafiek is een rechte door de oorsprong"],
                ["Lineair", "de grafiek is een rechte, die niet door de oorsprong hoeft te gaan; elke stap in x geeft dezelfde stap in y"],
                ["Omgekeerd evenredig", "hun product blijft gelijk; de grafiek is een hyperbool"],
                ["Kwadratisch", "de grafiek is een parabool"],
            ])),
            ("p", "Zijn <strong>twee grootheden recht evenredig</strong>, dan is hun grafiek "
                  "<strong>een rechte door de oorsprong</strong>. Zijn ze "
                  "<strong>omgekeerd evenredig</strong>, dan blijft <strong>hun product</strong> gelijk."),
            ("p", "<strong>Modellen om een verband weer te geven</strong> zijn "
                  "<strong>een grafiek</strong>, <strong>een tabel</strong> en <strong>een formule</strong>. "
                  "Dezelfde werkelijkheid, drie talen."),
            ("p", "Een formule mag je omvormen. Wil je in de formule "
                  "<strong>F is m maal a</strong> de <strong>m</strong> uitdrukken, dan wordt het "
                  "<strong>m is F gedeeld door a</strong>."),
        ]),
    ],
    onthoud=[
        "Een H-zin zegt welk gevaar een stof oplevert, P-zinnen zeggen hoe je er veilig mee omgaat.",
        "Afval van een chemisch product hoort in het vat voor chemisch afval, niet in de gootsteen.",
        "Meetbereik: de kleinste en grootste meetbare waarde. Nauwkeurigheid: de kleinste verandering die het toestel nog weergeeft.",
        "Een vloeistofniveau in een maatcilinder lees je af op ooghoogte.",
        "Een grootheid is wat je meet, een eenheid is waarin je het uitdrukt.",
        "De SI-eenheid van massa is de kilogram, niet de gram.",
        "Mega is een miljoen, kilo duizend, milli een duizendste, micro een miljoenste, nano een miljardste.",
        "De minst nauwkeurige meting bepaalt het aantal cijfers in het antwoord.",
        "Recht evenredig: een rechte door de oorsprong. Omgekeerd evenredig: het product blijft gelijk.",
    ],
)

# ───────────────────────── 21. Onderzoeksvaardigheden en ontwerpen
BUNDELS["onderzoeksvaardigheden-en-ontwerpen-beyond"] = dict(
    vak=VAK, niveau=BEYOND, titel="Onderzoeksvaardigheden en ontwerpen",
    onder="De stappen van een onderzoek, de stappen van een ontwerp, en wat STEM met de samenleving te maken heeft.",
    secties=[
        dict(kop="De stappen van een onderzoek", blokken=[
            ("p", "Een wetenschappelijk onderzoek begint met <strong>het probleem definiëren en "
                  "afbakenen</strong>. Daarna volgen de <strong>stappen die bij een wetenschappelijk onderzoek "
                  "horen</strong>: <strong>een onderzoeksvraag opstellen</strong>, "
                  "<strong>data verzamelen en analyseren</strong>, en "
                  "<strong>over je methode reflecteren en communiceren</strong>."),
            ("p", "Een goede <strong>onderzoeksvraag</strong> noemt wat je verandert en wat je meet, zoals "
                  "<strong>hoe hangt de valtijd van een bal af van zijn hoogte?</strong>. Een vraag met ja of "
                  "nee als antwoord, of een vraag zonder meetbare grootheid, brengt je niet verder. En "
                  "<strong>een onderzoeksvraag stel je niet pas op nadat je de metingen gedaan hebt</strong>: "
                  "dan weet je niet wat je moest meten."),
            ("p", "Een <strong>hypothese</strong> is <strong>de verwachting die je vóór het onderzoek over de "
                  "uitkomst opschrijft</strong>. <strong>Een hypothese die door het onderzoek weerlegd wordt, "
                  "maakt het onderzoek niet waardeloos</strong>: je weet daarna iets wat je eerst niet wist, en "
                  "dat is precies de bedoeling."),
            ("p", "In een <strong>onderzoeksplan</strong> staat <strong>welk materiaal je nodig hebt</strong>, "
                  "<strong>welke stappen je in welke orde zet</strong> en "
                  "<strong>wat je gaat meten en met welk instrument</strong>."),
        ]),
        dict(kop="Variabelen en meten", blokken=[
            ("p", "De <strong>onafhankelijke variabele</strong> is <strong>de grootheid die je in een proef "
                  "zelf verandert</strong>. De <strong>afhankelijke variabele</strong> is "
                  "<strong>de grootheid die je meet, dus het gevolg van wat je veranderde</strong>. Al de rest "
                  "houd je constant: <strong>in een goede proef verander je één grootheid en houd je de andere "
                  "gelijk</strong>."),
            ("p", "Wil je bijvoorbeeld <strong>onderzoeken of plantengroei van de hoeveelheid licht "
                  "afhangt</strong>, dan houd je <strong>de soort plant, de grond en het water</strong> gelijk. "
                  "Een <strong>controleproef</strong> hoort er ook bij: "
                  "<strong>de proef zonder de behandeling, waarmee je je resultaat vergelijkt</strong>."),
            ("p", "Je <strong>herhaalt een meting meerdere keren om toevallige meetfouten te zien en uit te "
                  "vlakken</strong>. En <strong>een meting die niet bij je hypothese past, mag je niet gewoon "
                  "weglaten uit je resultaten</strong>: dat is geen onderzoek meer. Past een meting niet, dan "
                  "ga je na waarom, en je vermeldt ze."),
        ]),
        dict(kop="Van data naar besluit", blokken=[
            ("p", "Nadat je de data verzameld hebt, ga je ze <strong>ordenen in een tabel of een "
                  "grafiek</strong>. Krijg je <strong>een tabel met meetgegevens en moet je er een verband uit "
                  "halen</strong>, dan is <strong>de gegevens in een grafiek uitzetten</strong> een goede eerste "
                  "stap: een verband zie je veel sneller dan je het uit cijfers rekent. Lees je op een grafiek "
                  "<strong>twee grootheden af die samen stijgen in een rechte door de oorsprong</strong>, dan "
                  "besluit je dat <strong>ze recht evenredig met elkaar zijn</strong>."),
            ("p", "Een <strong>goede conclusie</strong> <strong>antwoordt op de onderzoeksvraag</strong>, "
                  "<strong>steunt op de verzamelde data</strong> en <strong>zegt ook of de hypothese "
                  "klopte</strong>."),
            ("p", "<strong>Reflecteren over je methode hoort bij het onderzoek om te zien wat beter kon aan je "
                  "opzet</strong>, en <strong>communiceren over je onderzoek hoort bij de wetenschappelijke "
                  "methode</strong>: een resultaat dat niemand te weten komt, kan ook niemand nakijken."),
        ]),
        dict(kop="Ontwerpen", blokken=[
            ("p", "Onderzoeken en ontwerpen lijken op elkaar maar hebben een ander doel: "
                  "<strong>onderzoeken antwoordt op een vraag, ontwerpen lost op</strong>."),
            ("p", "De <strong>eerste stap als je een oplossing voor een probleem moet ontwerpen</strong>, is "
                  "<strong>het probleem duidelijk definiëren</strong>. De "
                  "<strong>stappen die bij het ontwerpen van een oplossing horen</strong>: "
                  "<strong>het probleem definiëren</strong>, <strong>criteria opstellen</strong> en "
                  "<strong>de oplossing evalueren en bijsturen</strong>."),
            ("p", "De <strong>criteria</strong> zijn <strong>de eisen waaraan je ontwerp moet voldoen</strong>. "
                  "Vragen die je helpen om ze op te stellen: "
                  "<strong>hoe groot of hoe zwaar mag het worden?</strong>, "
                  "<strong>hoeveel mag het kosten?</strong> en "
                  "<strong>hoe veilig en hoe duurzaam moet het zijn?</strong>. Aan het einde van een "
                  "ontwerpproces <strong>dienen de criteria om te beoordelen of je oplossing volstaat</strong>, "
                  "en <strong>een ontwerp hoeft niet aan maar één criterium te voldoen om een goede oplossing "
                  "te zijn</strong>: het moet er aan allemaal voldoen. Heb je "
                  "<strong>twee ontwerpen die allebei werken</strong>, dan kies je "
                  "<strong>door ze naast je criteria te leggen en te vergelijken</strong>."),
            ("p", "Je <strong>splitst een groot probleem op in deelproblemen, omdat elk stuk apart makkelijker "
                  "op te lossen is</strong>. Zo'n <strong>deelprobleem</strong> is "
                  "<strong>het stuk van een groot probleem dat je apart oplost</strong>."),
            ("p", "Een ontwerp is nooit in één keer klaar. "
                  "<strong>Het ontwerpproces stopt niet zodra je eerste versie klaar is</strong>, en "
                  "<strong>nadat je je ontwerp geëvalueerd hebt, mag je het nog bijsturen</strong>. "
                  "<strong>Ontwerp je een waterfilter voor een school en is één criterium dat hij betaalbaar "
                  "moet zijn</strong>, dan ga je bij een te duur ontwerp "
                  "<strong>het ontwerp bijsturen met goedkoper materiaal</strong>. En "
                  "<strong>voor elk probleem moet je geen volledig nieuw systeem ontwerpen</strong>: een "
                  "bestaande oplossing aanpassen is vaak sneller en beter."),
        ]),
        dict(kop="STEM en de samenleving", blokken=[
            ("p", "De letters <strong>STEM</strong> staan voor <strong>wetenschappen, techniek, engineering en "
                  "wiskunde</strong>. Je <strong>bekijkt een probleem het best vanuit meerdere "
                  "STEM-disciplines, omdat een totaaloplossing kennis uit meerdere hoeken vraagt</strong>."),
            ("p", "Om <strong>een vaccin tegen corona te ontwikkelen en te verdelen</strong> waren er "
                  "verschillende disciplines nodig: <strong>wetenschappelijke kennis om het vaccin te "
                  "maken</strong>, <strong>technologische kennis om het koel te houden</strong> en "
                  "<strong>wiskundige kennis om de verspreiding te volgen</strong>."),
            ("p", "Wil <strong>een stad de luchtkwaliteit verbeteren</strong>, dan is er net zo'n mengeling "
                  "nodig: <strong>wetenschappelijke kennis over de stoffen in de lucht</strong>, "
                  "<strong>technische kennis over meettoestellen en filters</strong> en "
                  "<strong>wiskundige kennis om de metingen te verwerken</strong>."),
            ("p", "Wetenschap en samenleving duwen elkaar vooruit. "
                  "<strong>De samenleving beïnvloedt het wetenschappelijk onderzoek doordat uitdagingen mee "
                  "bepalen waar onderzoek naar gaat</strong>, en omgekeerd "
                  "<strong>kan een nieuwe techniek nieuw wetenschappelijk onderzoek mogelijk maken</strong>: "
                  "zonder microscoop geen celbiologie."),
        ]),
    ],
    onthoud=[
        "Een onderzoek begint met het probleem definiëren en afbakenen.",
        "Een hypothese is de verwachting die je vóór het onderzoek over de uitkomst opschrijft.",
        "De onafhankelijke variabele verander je zelf, de afhankelijke variabele meet je.",
        "In een goede proef verander je één grootheid en houd je de andere gelijk.",
        "Een meting die niet bij je hypothese past, mag je niet gewoon weglaten.",
        "Een goede conclusie antwoordt op de onderzoeksvraag, steunt op de data en zegt of de hypothese klopte.",
        "Onderzoeken antwoordt op een vraag, ontwerpen lost op.",
        "Criteria zijn de eisen waaraan je ontwerp moet voldoen.",
        "STEM staat voor wetenschappen, techniek, engineering en wiskunde.",
    ],
)

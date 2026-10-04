# -*- coding: utf-8 -*-
"""De leerbundels voor fysica op 🚀 Boost doorstroom-niveau.

Gebaseerd op de vakfiche fysica van de 2de graad doorstroomfinaliteit, geldig
vanaf 1 januari 2027. Die fiche geldt enkel voor de studierichting
natuurwetenschappen: die legt haar wetenschappen af in drie aparte examens,
biologie, chemie en fysica, in plaats van één examen natuurwetenschappen.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De twaalf thema's volgen de weging van het examen: vijf over grootheden,
beweging en krachten (35 %), twee over druk en de gaswetten (15 %), en één
over elk van energie, warmteleer, elektriciteit, optica en onderzoek (elk
10 %).

Drie afspraken van de fiche staan in de bundels overgenomen. De tweede wet van
Newton staat er niet, dus F = m.a komt in geen enkele bundel voor. Er staan ook
geen formules voor de eenparig veranderlijke beweging, dus die bundel werkt met
grafieken en met de gemiddelde versnelling als Δv/Δt. En de constanten blijven
die van het examen: g = 9,81 N/kg, ρ van water 1000 kg/m³, de luchtdruk
1013 hPa, c van water 4186 J/(kg.K), R = 8,31 J/(mol.K) en T₀ = 273,15 K.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../boost-doorstroom/fysica.json`
doet daar het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-fysica-boost-doorstroom".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Fysica"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────── 1. Grootheden, eenheden en nauwkeurig meten
BUNDELS["grootheden-eenheden-en-nauwkeurig-meten-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Grootheden, eenheden en nauwkeurig meten",
    onder="De grootheden en hun SI-eenheden, de voorvoegsels, omrekenen, beduidende cijfers, vectoren en verbanden tussen grootheden.",
    secties=[
        dict(kop="Grootheid, eenheid en symbool", blokken=[
            ("p", "Een <strong>grootheid</strong> is iets dat je kan meten, zoals een lengte of een "
                  "massa. Elke grootheid heeft een <strong>symbool</strong> en een "
                  "<strong>eenheid</strong>. Een getal zonder eenheid betekent in de fysica niets: een "
                  "5 kan 5 m, 5 kg of 5 s zijn. <strong>Twee metingen zijn alleen met elkaar te "
                  "vergelijken als ze in dezelfde eenheid staan.</strong>"),
            ("p", tabel(["Grootheid", "Symbool", "SI-eenheid", "Andere eenheid"], [
                ["lengte, hoogte, diepte", "l, h", "meter (m)", "—"],
                ["oppervlakte", "A", "vierkante meter (m²)", "—"],
                ["volume", "V", "kubieke meter (m³)", "liter (L)"],
                ["massa", "m", "kilogram (kg)", "ton (t)"],
                ["tijd, tijdsduur", "t, Δt", "seconde (s)", "minuut, uur"],
                ["temperatuur", "θ", "—", "graad Celsius (°C)"],
                ["absolute temperatuur", "T", "kelvin (K)", "—"],
                ["snelheid", "v, vg", "meter per seconde (m/s)", "km/h"],
                ["versnelling", "a, ag, g", "m/s²", "—"],
                ["kracht", "F", "newton (N)", "—"],
                ["druk", "p", "pascal (Pa)", "bar"],
                ["arbeid, energie, warmte", "W, E, Q", "joule (J)", "kWh, calorie"],
                ["vermogen", "P", "watt (W)", "—"],
                ["moment van een kracht", "M", "newtonmeter (Nm)", "—"],
                ["stroomsterkte", "I", "ampère (A)", "—"],
                ["spanning", "U", "volt (V)", "—"],
                ["weerstand", "R", "ohm (Ω)", "—"],
                ["massadichtheid", "ρ", "kg/m³", "g/L"],
            ])),
            ("p", "Een paar ervan zijn makkelijk te verwisselen. De <strong>newton is de "
                  "SI-eenheid van kracht</strong>, niet de kilogram: die hoort bij de massa. De "
                  "<strong>pascal</strong> is de eenheid van <strong>druk</strong>, want één pascal is "
                  "één newton per vierkante meter. De <strong>joule</strong> hoort bij de "
                  "<strong>arbeid, de energie en de warmte</strong>, en de <strong>watt</strong> bij "
                  "het <strong>vermogen</strong>: <strong>één watt is één joule per seconde</strong>. "
                  "De <strong>ohm</strong> hoort bij de weerstand."),
            ("kader", "<strong>De kilogram is een uitzondering.</strong> Ze is de SI-eenheid van "
                      "massa, ook al staat er al een voorvoegsel in. Alle andere SI-eenheden staan "
                      "zonder voorvoegsel."),
            ("p", "De <strong>liter en de kilometer per uur zijn geen SI-eenheden</strong>, maar je "
                  "mag ze gebruiken. De SI-eenheid van volume is de kubieke meter, die van snelheid de "
                  "meter per seconde. De <strong>ton is geen SI-eenheid</strong>, de kilogram wel."),
        ]),
        dict(kop="De voorvoegsels, van mega tot nano", blokken=[
            ("p", tabel(["Naam", "Symbool", "Waarde"], [
                ["mega", "M", "10⁶"],
                ["kilo", "k", "10³"],
                ["hecto", "h", "10²"],
                ["deca", "da", "10¹"],
                ["deci", "d", "10⁻¹"],
                ["centi", "c", "10⁻²"],
                ["milli", "m", "10⁻³"],
                ["micro", "μ", "10⁻⁶"],
                ["nano", "n", "10⁻⁹"],
            ])),
            ("p", "<strong>Kilo is duizend (10³)</strong>, <strong>mega een miljoen (10⁶)</strong>, "
                  "<strong>hecto honderd (10²)</strong> en <strong>deca tien (10¹)</strong>. Naar "
                  "beneden: <strong>milli een duizendste (10⁻³)</strong>, <strong>micro een "
                  "miljoenste (10⁻⁶)</strong> en <strong>nano 10⁻⁹</strong>. "
                  "<strong>Deca is dus niet honderd</strong>, dat is hecto."),
        ]),
        dict(kop="Omrekenen en de wetenschappelijke notatie", blokken=[
            ("p", tabel(["Omrekening", "Hoe", "Voorbeeld"], [
                ["km naar m", "× 1000", "2,5 km = 2500 m"],
                ["mm naar m", "÷ 1000", "45 mm = 0,045 m"],
                ["ton naar kg", "× 1000", "2,4 ton = 2400 kg"],
                ["liter naar m³", "÷ 1000", "500 L = 0,5 m³"],
                ["km/h naar m/s", "÷ 3,6", "72 km/h = 20 m/s"],
                ["m/s naar km/h", "× 3,6", "25 m/s = 90 km/h"],
                ["minuut naar s", "× 60", "een kwartier = 900 s"],
                ["°C naar K", "+ 273,15", "25 °C = 298 K"],
            ])),
            ("p", "De <strong>omrekening van km/h naar m/s</strong> komt van de twee eenheden samen: "
                  "in één kilometer zitten 1000 m en in één uur 3600 s, en 3600 / 1000 = 3,6. Daarom "
                  "<strong>deel je door 3,6</strong> om naar m/s te gaan en vermenigvuldig je met 3,6 "
                  "om terug te keren. <strong>Een snelheid in m/s is dus een grotere eenheid dan een "
                  "snelheid in km/h</strong>, hoewel er kilo in staat: de uren in de noemer maken het "
                  "verschil."),
            ("p", "In de <strong>wetenschappelijke notatie</strong> staat er <strong>één cijfer van "
                  "1 tot 9 voor de komma</strong>, maal een macht van tien. Zo wordt "
                  "<strong>0,00045 m gelijk aan 4,5 . 10⁻⁴ m</strong>: de komma schuift vier plaatsen "
                  "naar rechts, dus de exponent is −4. <strong>45 . 10⁻⁵ is dezelfde waarde maar geen "
                  "wetenschappelijke notatie</strong>, want er staan twee cijfers voor de komma."),
            ("p", "Een <strong>kwadraat van een eenheid rekent anders om</strong>. Een oppervlakte van "
                  "0,20 m bij 0,20 m is 0,040 m², niet 0,40 m²: je vermenigvuldigt de twee lengtes."),
        ]),
        dict(kop="Nauwkeurig meten", blokken=[
            ("p", "<strong>Een meting is nooit exact.</strong> Elk meetinstrument heeft een "
                  "<strong>beperkte nauwkeurigheid</strong>: dat zegt <strong>hoe fijn het kan "
                  "aflezen</strong>. Daarnaast heeft elk instrument een <strong>meetbereik</strong>: "
                  "<strong>het grootste getal dat het kan meten</strong>. Meet je daarboven, dan loopt "
                  "het instrument over of gaat het stuk."),
            ("p", "Je kiest een instrument dus op <strong>twee</strong> dingen: de waarde moet binnen "
                  "het meetbereik passen, én de streepjes moeten fijn genoeg zijn. Wil je "
                  "<strong>0,8 L water afmeten</strong>, dan is een <strong>cilinder van 1 L met "
                  "streepjes per 10 mL</strong> het geschiktst: in een cilinder van 100 mL of 50 mL "
                  "past het niet, en bij een cilinder van 5 L met streepjes per 100 mL zijn de "
                  "streepjes te grof."),
            ("p", "Het aantal <strong>beduidende cijfers</strong> van je antwoord moet bij die "
                  "nauwkeurigheid passen. <strong>Nullen vooraan tellen niet mee, nullen achteraan "
                  "wel</strong>: <strong>0,0250 m heeft drie beduidende cijfers</strong>, want die "
                  "laatste nul zegt dat er tot op de tiende millimeter gemeten is. Noteert iemand met "
                  "een gewoon meetlint <strong>1,2534 m</strong>, dan is dat vreemd: "
                  "<strong>een meetlint kan niet tot op een tiende millimeter meten</strong>, dus "
                  "1,253 m is het meest dat je mag opschrijven. Staan er achteraan nullen "
                  "<strong>zonder komma</strong>, dan tellen ze niet mee: "
                  "<strong>7000 kg zo geschreven heeft één beduidend cijfer</strong>, want je weet "
                  "niet of er tot op de kilogram gemeten is."),
            ("p", "<strong>Je antwoord heeft nooit meer beduidende cijfers dan het minst nauwkeurige "
                  "gegeven</strong>, en er staat <strong>altijd een eenheid bij</strong>. "
                  "<strong>Afronden doe je pas op het einde</strong>, niet bij elk tussenresultaat: "
                  "anders sleep je een afrondingsfout mee."),
            ("p", "Welk instrument waarvoor: een <strong>balans</strong> meet een <strong>massa</strong>, "
                  "een <strong>dynamometer</strong> een <strong>kracht</strong>, een "
                  "<strong>maatcilinder</strong> een <strong>volume</strong>, een "
                  "<strong>manometer</strong> een <strong>druk</strong> in een vat, een "
                  "<strong>barometer</strong> de <strong>luchtdruk</strong>, een "
                  "<strong>chronometer</strong> een <strong>tijd</strong>, een "
                  "<strong>thermometer</strong> een <strong>temperatuur</strong> en een "
                  "<strong>multimeter</strong> een <strong>spanning, stroomsterkte of weerstand</strong>."),
            ("p", "<strong>Een instrument dat je niet gebruikt, schakel je uit.</strong> Het verbruikt "
                  "anders zijn batterij, het kan warm worden, en een multimeter op de verkeerde stand "
                  "kan stuk gaan."),
            ("p", "<strong>Schatten hoort bij meten.</strong> Water heeft een massadichtheid van "
                  "1000 kg/m³, dus <strong>één liter water weegt ongeveer één kilogram</strong> en een "
                  "fles van 1,5 L ongeveer 1,5 kg. Een mens van 700 kg of een auto die 300 km/h door "
                  "de stad rijdt, kan niet: zo'n schatting verraadt een rekenfout."),
        ]),
        dict(kop="Vectoren en verbanden tussen grootheden", blokken=[
            ("p", "Sommige grootheden hebben een <strong>richting</strong>. Dat zijn de "
                  "<strong>vectoriële grootheden</strong>, en die hebben "
                  "<strong>vier kenmerken: grootte, richting, zin en aangrijpingspunt</strong>. "
                  "<strong>Verplaatsing, snelheid, versnelling en kracht</strong> zijn vectoren; "
                  "<strong>massa, temperatuur, druk en energie</strong> zijn gewone getallen met een "
                  "eenheid. Een <strong>pijltje boven het symbool</strong> zegt dat je de vector "
                  "bedoelt; zonder pijltje bedoel je enkel de grootte."),
            ("p", "Tussen twee gemeten grootheden zoek je een <strong>verband</strong>."),
            ("p", tabel(["Verband", "Wat blijft gelijk", "Grafiek"], [
                ["recht evenredig", "de verhouding y/x", "rechte door de oorsprong"],
                ["lineair", "de toename per stap", "rechte, niet door de oorsprong"],
                ["omgekeerd evenredig", "het product x.y", "dalende kromme"],
                ["kwadratisch", "y/x²", "parabool"],
            ])),
            ("p", "<strong>Een lineair verband is dus niet altijd recht evenredig</strong>: enkel een "
                  "rechte <em>door de oorsprong</em> is dat. Bij een <strong>omgekeerd evenredig "
                  "verband tussen p en V blijft p.V gelijk</strong>: wordt V twee keer zo groot, dan "
                  "wordt p twee keer zo klein. Bij een <strong>kwadratisch verband</strong>, zoals "
                  "Ek = m.v²/2, wordt <strong>Ek vier keer zo groot als v verdubbelt</strong>."),
            ("p", "De <strong>steilheid van een rechte</strong> betekent iets. Zet je de veerkracht uit "
                  "tegen de lengteverandering van een veer, dan is de <strong>steilheid de "
                  "veerconstante</strong>, want k = Fv / Δl."),
            ("p", "<strong>Een formule omvormen</strong> om één grootheid <strong>vrij te maken</strong>, "
                  "doe je stap voor stap. Uit <strong>p = F / A "
                  "volgt A = F / p</strong>: vermenigvuldig beide leden met A en deel daarna door p."),
            ("weetje", "Schatten vooraf is het goedkoopste nalezen dat bestaat. Weet je dat een "
                       "fles water ongeveer een kilo weegt, dan zie je meteen dat een antwoord van "
                       "15 kg niet kan, nog voor je je berekening nakijkt."),
        ]),
    ],
    onthoud=[
        "Een getal zonder eenheid betekent niets; twee metingen vergelijk je alleen in dezelfde eenheid.",
        "Newton voor kracht, pascal voor druk, joule voor energie, watt voor vermogen, ohm voor weerstand.",
        "De kilogram is de SI-eenheid van massa, ook al staat er kilo in.",
        "Kilo 10³, mega 10⁶, hecto 10², deca 10¹; milli 10⁻³, micro 10⁻⁶, nano 10⁻⁹.",
        "Van km/h naar m/s deel je door 3,6; omgekeerd vermenigvuldig je met 3,6.",
        "In de wetenschappelijke notatie staat één cijfer van 1 tot 9 voor de komma: 0,00045 m = 4,5.10⁻⁴ m.",
        "Nullen vooraan tellen niet mee bij de beduidende cijfers, nullen achteraan wel: 0,0250 m heeft er drie.",
        "Kies een instrument eerst op meetbereik, dan op nauwkeurigheid; zet het uit als je niet meet.",
        "Een vector heeft grootte, richting, zin en aangrijpingspunt; een rechte door de oorsprong betekent recht evenredig.",
    ],
)

# ───────────────────── 2. Eenparig rechtlijnige beweging
BUNDELS["eenparig-rechtlijnige-beweging-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Eenparig rechtlijnige beweging",
    onder="Afgelegde weg en verplaatsing, de snelheidsvector, de positiefunctie, x(t)- en v(t)-grafieken, en inhaal- en kruisingsproblemen.",
    secties=[
        dict(kop="Positie, baan en verplaatsing", blokken=[
            ("p", "Om een beweging te beschrijven zet je een <strong>x-as</strong> langs de baan. De "
                  "<strong>positie x</strong> zegt waar het voorwerp zich bevindt, het "
                  "<strong>tijdstip t</strong> wanneer. De <strong>baan</strong> is "
                  "<strong>de lijn die het voorwerp beschrijft</strong>; is die lijn een rechte, dan is "
                  "de beweging <strong>rechtlijnig</strong>."),
            ("p", "Een <strong>puntmassa</strong> is een model: <strong>je doet alsof de hele massa in "
                  "één punt zit</strong> en vergeet de vorm en de grootte. Dat "
                  "<strong>maakt het rekenen eenvoudiger</strong>. Een puntmassa heeft wel massa, en "
                  "<strong>ook een groot voorwerp mag je zo bekijken</strong> als je enkel naar zijn "
                  "plaats op het traject kijkt, zoals een trein op een spoorlijn."),
            ("p", "<strong>De verplaatsing kijkt enkel naar begin- en eindpunt</strong>: "
                  "<strong>Δx = x − x₀</strong>. De <strong>afgelegde weg Δs</strong> is de hele weg "
                  "die het voorwerp echt gelopen heeft. Loopt iemand <strong>één ronde van 400 m op "
                  "een piste</strong>, dan is <strong>de afgelegde weg 400 m en de verplaatsing "
                  "0 m</strong>: hij staat weer op zijn startplaats."),
            ("p", "<strong>Een verplaatsing kan negatief zijn</strong>, want het "
                  "<strong>teken hoort bij de zin</strong>: beweegt het voorwerp tegen de zin van de "
                  "x-as in, dan is Δx negatief. Een <strong>afgelegde weg is nooit negatief</strong>, "
                  "en <strong>ook de grootte van een snelheid niet</strong>. Vertrekt een wandelaar op "
                  "x₀ = 20 m en gaat hij in de positieve zin tot x = 95 m, dan is Δx = 95 − 20 = 75 m."),
        ]),
        dict(kop="De snelheid", blokken=[
            ("p", "De <strong>gemiddelde snelheid</strong> is <strong>vg = Δx / Δt</strong>, de "
                  "verplaatsing gedeeld door de tijdsduur. De SI-eenheid is de "
                  "<strong>meter per seconde</strong>."),
            ("p", "De <strong>ogenblikkelijke snelheid</strong> is <strong>de snelheid op één bepaald "
                  "tijdstip</strong>. Dat is wat je <strong>op de snelheidsmeter van een auto</strong> "
                  "afleest. De gemiddelde snelheid van de hele rit kan heel anders zijn, bijvoorbeeld "
                  "door een file."),
            ("p", tabel(["Vraag", "Rekenwerk", "Antwoord"], [
                ["150 km in 2,0 h", "150 / 2,0", "75 km/h"],
                ["60 km in een half uur", "60 / 0,5", "120 km/h"],
                ["480 m in 16 s", "480 / 16", "30 m/s"],
                ["25 m/s gedurende 4,0 s", "25 . 4,0", "100 m"],
                ["6,0 m/s gedurende 1,0 min", "6,0 . 60", "360 m"],
            ])),
            ("kader", "Reken de tijd altijd eerst om naar dezelfde eenheid als de snelheid. Een "
                      "minuut is 60 s, een half uur is 0,5 h."),
        ]),
        dict(kop="Wat een ERB is", blokken=[
            ("p", "Bij een <strong>eenparig rechtlijnige beweging (ERB)</strong> blijft de "
                  "<strong>snelheid gelijk</strong> in grootte, richting en zin, en is de "
                  "<strong>versnelling nul</strong>. De positie verandert juist wel, anders zou het "
                  "voorwerp stilstaan."),
            ("p", "Bij een ERB is de <strong>gemiddelde snelheid gelijk aan de ogenblikkelijke "
                  "snelheid</strong>, want er valt niets te gemiddelden. Een <strong>voorwerp in rust "
                  "heeft een snelheid van nul</strong>: de positie verandert niet."),
            ("p", "De <strong>snelheidsvector</strong> heeft vier kenmerken. Bij een ERB blijven "
                  "<strong>grootte, richting en zin gelijk</strong>; het "
                  "<strong>aangrijpingspunt schuift mee</strong> met het voorwerp, want dat verplaatst "
                  "zich. Rijdt een fietser <strong>in de zin tegengesteld aan de x-as</strong>, dan is "
                  "<strong>het teken van zijn snelheid negatief</strong>."),
            ("p", "De <strong>positiefunctie</strong> van een ERB is "
                  "<strong>x = x₀ + v.(t − t₀)</strong>, met <strong>x₀ de beginpositie</strong> op het "
                  "tijdstip t₀. In <strong>x = 10 + 3.t</strong> is 10 m de beginpositie en 3 m/s de "
                  "snelheid. In <strong>x = 40 − 5.t</strong> vertrekt het voorwerp op 40 m en "
                  "<strong>beweegt het tegen de zin van de x-as in</strong>, want de snelheid is "
                  "−5 m/s. Het is in de oorsprong als x = 0, dus na t = 40 / 5 = 8,0 s."),
        ]),
        dict(kop="De grafieken lezen", blokken=[
            ("p", tabel(["Grafiek", "Steilheid", "Oppervlakte eronder", "ERB ziet uit als"], [
                ["x(t)", "de snelheid", "betekent niets", "een schuine rechte"],
                ["v(t)", "de versnelling", "de verplaatsing", "een horizontale lijn"],
                ["a(t)", "—", "de verandering van v", "een lijn op nul"],
            ])),
            ("p", "In een <strong>x(t)-grafiek</strong> is de <strong>steilheid de snelheid</strong>: "
                  "een steilere rechte betekent sneller. Een <strong>horizontaal stuk betekent dat het "
                  "voorwerp stilstaat</strong>, een <strong>rustpauze</strong>. Een <strong>rechte die "
                  "naar beneden loopt, hoort bij een negatieve snelheid</strong>: de positie wordt "
                  "kleiner. Je kan uit een x(t)-grafiek <strong>de bijbehorende v(t)-grafiek "
                  "opstellen</strong>: per stuk bereken je de steilheid en die zet je als horizontale "
                  "lijn in de v(t)-grafiek."),
            ("p", "In een <strong>v(t)-grafiek</strong> is de <strong>oppervlakte onder de lijn de "
                  "verplaatsing</strong>, want snelheid maal tijd. De <strong>hoogte van de lijn is de "
                  "snelheid</strong>, niet de verplaatsing. Ligt het stuk onder de tijdas, dan is de "
                  "verplaatsing negatief: een lijn op −4 m/s gedurende 3,0 s geeft Δx = −12 m. Bij een "
                  "ERB is de lijn <strong>horizontaal</strong>, dus is de versnelling nul. Een "
                  "horizontaal stuk betekent dus een constante snelheid, niet per se stilstand: dat is "
                  "enkel zo als de lijn op nul ligt. <strong>De beginpositie kan je niet uit een "
                  "v(t)-grafiek aflezen</strong>; die moet in de opgave staan."),
            ("p", "Liggen <strong>twee lijnen in dezelfde v(t)-grafiek</strong>, dan hoort de "
                  "<strong>hogere lijn bij de grotere snelheid</strong> en dus bij de "
                  "<strong>grotere afgelegde weg</strong> in dezelfde tijd. Van versnellen is bij twee "
                  "horizontale lijnen geen sprake."),
        ]),
        dict(kop="Inhalen en kruisen", blokken=[
            ("p", "Twee voorwerpen op dezelfde baan los je op met hun <strong>positiefuncties</strong>, "
                  "of grafisch. <strong>Snijden twee rechten in een x(t)-grafiek, dan zijn de twee "
                  "voorwerpen op dat tijdstip op dezelfde plaats</strong>: ze kruisen of halen elkaar in."),
            ("p", "<strong>Inhalen</strong>: een wandelaar vertrekt om 9 uur met 5,0 km/h, een fietser om "
                  "10 uur op dezelfde plaats met 15 km/h. Bij het vertrek van de fietser heeft de "
                  "wandelaar <strong>5,0 km voorsprong</strong>. De fietser loopt "
                  "<strong>15 − 5,0 = 10 km/h</strong> in, dus heeft hij 5,0 / 10 = "
                  "<strong>0,50 h</strong> nodig."),
            ("p", "<strong>Kruisen</strong>: twee auto's rijden naar elkaar toe, 120 km van elkaar, met "
                  "70 km/h en 50 km/h. Samen naderen ze met <strong>70 + 50 = 120 km/h</strong>, dus "
                  "duurt het <strong>1,0 h</strong>."),
            ("kader", "Rijden twee voorwerpen dezelfde kant op, dan trek je hun snelheden van elkaar "
                      "af. Rijden ze naar elkaar toe, dan tel je ze op."),
            ("weetje", "Bij de marathon loopt iemand ruim 42 km, maar start en aankomst liggen soms "
                       "op dezelfde plaats. Zijn afgelegde weg is dan 42 km en zijn verplaatsing nul."),
        ]),
    ],
    onthoud=[
        "Verplaatsing Δx = x − x₀ kijkt enkel naar begin en eind; de afgelegde weg Δs is de hele weg.",
        "Eén ronde van 400 m: afgelegde weg 400 m, verplaatsing 0 m.",
        "vg = Δx / Δt; de snelheidsmeter geeft de ogenblikkelijke snelheid.",
        "Bij een ERB blijft de snelheid gelijk en is de versnelling nul.",
        "Positiefunctie: x = x₀ + v.(t − t₀), met x₀ de beginpositie.",
        "De steilheid van een x(t)-grafiek is de snelheid; een horizontaal stuk is een rustpauze.",
        "De oppervlakte onder een v(t)-grafiek is de verplaatsing; de hoogte is de snelheid.",
        "Een snijpunt in een x(t)-grafiek betekent: op dezelfde plaats op hetzelfde tijdstip.",
        "Inhalen: trek de snelheden van elkaar af. Kruisen: tel ze op.",
    ],
)

# ───────────────────── 3. Versnelde beweging, vrije val en verticale worp
BUNDELS["versnelde-beweging-vrije-val-en-verticale-worp-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Versnelde beweging, vrije val en verticale worp",
    onder="De EVRB, het teken van de versnelling, de grafieken van een versnelde beweging, de vrije val en de verticale worp naar boven.",
    secties=[
        dict(kop="Wat een EVRB is", blokken=[
            ("p", "Bij een <strong>eenparig veranderlijke rechtlijnige beweging (EVRB)</strong> "
                  "<strong>blijft de versnelling gelijk</strong>. De <strong>snelheid verandert dan "
                  "elke seconde met evenveel</strong>. Dat is net wat eenparig veranderlijk betekent."),
            ("p", "De <strong>versnelling</strong> zegt hoeveel de snelheid per seconde verandert. De "
                  "SI-eenheid is de <strong>meter per seconde kwadraat (m/s²)</strong>. De "
                  "<strong>gemiddelde versnelling</strong> krijgt het symbool <strong>ag</strong> en is "
                  "<strong>ag = Δv / Δt</strong>; de ogenblikkelijke versnelling krijgt gewoon a."),
            ("p", tabel(["Beweging", "Rekenwerk", "ag"], [
                ["van 0 naar 20 m/s in 5,0 s", "20 / 5,0", "4,0 m/s²"],
                ["van 4,0 naar 14 m/s in 5,0 s", "10 / 5,0", "2,0 m/s²"],
                ["van 30 naar 10 m/s in 8,0 s", "−20 / 8,0", "−2,5 m/s²"],
            ])),
            ("p", "Het <strong>teken</strong> hoort bij de zin. Rijdt een auto <strong>in de positieve "
                  "zin en vertraagt hij, dan is de versnelling negatief</strong>: de snelheid is "
                  "positief maar wordt kleiner. Snelheid en versnelling hebben dan een "
                  "<strong>tegengestelde zin</strong>."),
            ("kader", "<strong>Een negatieve versnelling betekent niet altijd vertragen.</strong> "
                      "Beweegt een voorwerp al in de negatieve zin, dan maakt een negatieve "
                      "versnelling het juist sneller. Wat telt, is of snelheid en versnelling dezelfde "
                      "zin hebben of niet."),
            ("p", "Bij <strong>vertragen liggen snelheid en versnelling op dezelfde rechte, dus hebben "
                  "ze dezelfde richting, maar met tegengestelde zin</strong>. Daarom wordt de snelheid "
                  "kleiner. Bij versnellen hebben ze dezelfde zin."),
            ("p", "Een <strong>voorwerp met een snelheid van nul kan toch een versnelling "
                  "hebben</strong>. Een bal die je recht omhoog gooit, staat op zijn hoogste punt een "
                  "ogenblik stil, maar de valversnelling werkt daar wel. Een ogenblik later valt hij."),
        ]),
        dict(kop="De grafieken van een versnelde beweging", blokken=[
            ("p", tabel(["Grafiek", "ERB", "versneld", "vertraagd"], [
                ["x(t)", "schuine rechte", "kromme die steiler wordt", "kromme die vlakker wordt"],
                ["v(t)", "horizontale lijn", "stijgende rechte", "dalende rechte"],
                ["a(t)", "lijn op nul", "horizontale lijn boven nul", "horizontale lijn onder nul"],
            ])),
            ("p", "De <strong>steilheid van een v(t)-grafiek is de versnelling</strong>, want Δv / Δt. "
                  "Een <strong>stijgende schuine rechte</strong> betekent dus <strong>gelijkmatig "
                  "versnellen</strong>. Staan er twee rechten in dezelfde v(t)-grafiek, dan hoort de "
                  "<strong>steilere rechte bij de grotere versnelling</strong>; over de beginsnelheid "
                  "zegt de steilheid niets."),
            ("p", "In een <strong>a(t)-grafiek van een EVRB is de lijn horizontaal</strong>, want de "
                  "versnelling verandert niet. Een schuine rechte zou betekenen dat de versnelling "
                  "zelf verandert. Ligt die horizontale lijn <strong>boven de tijdas</strong>, dan "
                  "<strong>blijft de versnelling gelijk en neemt de snelheid toe</strong>."),
            ("p", "In een <strong>x(t)-grafiek van een eenparig versnelde beweging is de lijn een "
                  "kromme die steeds steiler wordt</strong>, want de snelheid groeit. Bij vertragen "
                  "wordt de kromme juist vlakker."),
            ("p", "<strong>De oppervlakte onder een v(t)-grafiek is de verplaatsing</strong>, ook bij "
                  "een versnelde beweging. Bij een schuine rechte is dat een driehoek of een trapezium."),
        ]),
        dict(kop="De vrije val", blokken=[
            ("p", "Bij een <strong>vrije val werkt enkel de zwaartekracht</strong>, en "
                  "<strong>laat je de luchtweerstand buiten beschouwing</strong>. Het is dus een "
                  "model: in het echt is er altijd wat lucht. De kracht die voor de versnelling zorgt, "
                  "is de <strong>zwaartekracht</strong>."),
            ("p", "De <strong>valversnelling in België is g = 9,81 m/s²</strong>. Elke seconde komt er "
                  "dus <strong>9,81 m/s</strong> bij de snelheid. Na 2,0 s valt een steen met "
                  "2,0 . 9,81 = <strong>19,6 m/s</strong>, na 3,0 s met 29,4 m/s."),
            ("p", tabel(["Grafiek van een vrije val", "Hoe ze eruitziet"], [
                ["v(t), zin naar beneden positief", "stijgende rechte door de oorsprong"],
                ["a(t)", "horizontale lijn op 9,81 m/s²"],
                ["x(t), vanaf het startpunt", "kromme die steeds steiler wordt"],
            ])),
            ("p", "<strong>Op de maan valt een voorwerp langzamer</strong>: de zwaarteveldsterkte daar "
                  "is ongeveer 1,62 m/s², zes keer kleiner. <strong>Bij een vrije val neemt de "
                  "afgelegde weg niet elke seconde met evenveel toe</strong>: de snelheid groeit, dus "
                  "valt het voorwerp elke seconde verder dan de seconde ervoor. Enkel de snelheid "
                  "groeit gelijkmatig."),
            ("p", "<strong>Zonder luchtweerstand valt alles met dezelfde versnelling</strong>, hoe "
                  "zwaar het ook is. Staan een voorwerp van 1 kg en een van 5 kg in dezelfde "
                  "v(t)-grafiek, dan <strong>vallen de twee lijnen precies samen</strong>. "
                  "<strong>Een zwaar voorwerp valt dus niet altijd sneller dan een licht</strong>: in "
                  "de echte lucht valt een pluim trager dan een steen door de luchtweerstand, maar een "
                  "lichte en een zware kogel vallen even snel. In een buis zonder lucht vallen een "
                  "steen en een pluim samen."),
            ("p", "Daarom bereikt een <strong>parachutist</strong> na een tijd een constante snelheid. "
                  "Zodra de <strong>luchtweerstand even groot is als de zwaartekracht</strong>, is de "
                  "<strong>resulterende kracht nul</strong> en verandert de snelheid niet meer. De "
                  "zwaartekracht is dan niet verdwenen, en de versnelling is er niet 9,81 m/s² maar nul."),
        ]),
        dict(kop="De verticale worp naar boven", blokken=[
            ("p", "Het <strong>verschil met een vrije val zit enkel in de beginsnelheid</strong>: bij "
                  "een <strong>worp naar boven is die niet nul en omhoog gericht</strong>. De "
                  "versnelling is in beide gevallen dezelfde, naar beneden."),
            ("p", "Op de weg naar boven wordt de <strong>snelheid gelijkmatig kleiner</strong>, want de "
                  "valversnelling werkt tegen de beweging in. Elke seconde verdwijnt er 9,81 m/s. "
                  "Gooi je een bal met 15 m/s omhoog, dan is hij na 15 / 9,81 ≈ "
                  "<strong>1,5 s</strong> op zijn hoogste punt."),
            ("p", "<strong>Op het hoogste punt is de snelheid nul, maar de versnelling nog altijd "
                  "9,81 m/s² naar beneden.</strong> De zwaartekracht blijft werken, en "
                  "<strong>de zin van de versnelling verandert daar niet</strong>: enkel de zin van de "
                  "snelheid keert om."),
            ("p", "<strong>Zonder luchtweerstand komt de bal met dezelfde grootte van snelheid terug "
                  "in je hand</strong> als waarmee hij vertrok. De weg naar boven en de weg naar "
                  "beneden zijn even lang en hebben dezelfde versnelling; enkel de zin is omgekeerd."),
            ("weetje", "Op de maan hebben de astronauten van Apollo 15 een hamer en een valkenpluim "
                       "samen laten vallen. Ze raakten de grond op hetzelfde moment, want daar is "
                       "geen lucht die de pluim tegenhoudt."),
        ]),
    ],
    onthoud=[
        "Bij een EVRB blijft de versnelling gelijk; ag = Δv / Δt, in m/s².",
        "Een negatieve versnelling betekent enkel vertragen als de snelheid positief is.",
        "De steilheid van een v(t)-grafiek is de versnelling; een a(t)-grafiek van een EVRB is horizontaal.",
        "Een x(t)-grafiek wordt steiler bij versnellen en vlakker bij vertragen.",
        "Bij een vrije val werkt enkel de zwaartekracht; g = 9,81 m/s² in België.",
        "Zonder lucht vallen een zware en een lichte kogel even snel; de twee lijnen in een v(t)-grafiek vallen samen.",
        "Een parachutist houdt een constante snelheid zodra de luchtweerstand de zwaartekracht opheft.",
        "Op het hoogste punt van een worp is de snelheid nul en de versnelling nog 9,81 m/s² naar beneden.",
        "Een worp naar boven verschilt van een vrije val enkel door de beginsnelheid.",
    ],
)

# ───────────────────── 4. Krachten, krachtenbalans en zwaartekracht
BUNDELS["krachten-krachtenbalans-en-zwaartekracht-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Krachten, krachtenbalans en zwaartekracht",
    onder="De kracht als vector, krachten samenstellen en ontbinden, de krachtenbalans, en de zwaartekracht, de veerkracht en de wrijvingskracht.",
    secties=[
        dict(kop="De kracht als vector", blokken=[
            ("p", "Een <strong>kracht</strong> krijgt het symbool <strong>F</strong> en wordt gemeten "
                  "in <strong>newton (N)</strong>, met een <strong>dynamometer</strong>. Een "
                  "<strong>balans</strong> meet een massa in kilogram, geen kracht."),
            ("p", "Een kracht is een <strong>vector</strong> met vier kenmerken: een "
                  "<strong>grootte in newton</strong>, een richting, een zin en een "
                  "<strong>aangrijpingspunt op het voorwerp</strong>. Je tekent een krachtvector "
                  "<strong>op schaal</strong>, bijvoorbeeld 1 cm voor 10 N, dus "
                  "<strong>zegt de lengte van de pijl wel iets over de grootte</strong>. Een duwkracht "
                  "en een trekkracht teken je allebei met een <strong>vectorpijl</strong>; enkel de "
                  "zin van die pijl verschilt."),
            ("p", "<strong>Een kracht heeft altijd een voorwerp dat ze uitoefent en een voorwerp "
                  "waarop ze werkt.</strong> Daarom hoort bij de naam van een kracht altijd van wie op "
                  "wat."),
            ("p", tabel(["Kracht", "Symbool", "Van wie op wat"], [
                ["zwaartekracht", "Fz", "de aarde op het voorwerp"],
                ["normaalkracht", "Fn", "het oppervlak op het voorwerp"],
                ["wrijvingskracht", "Fw", "het oppervlak op het voorwerp, erlangs"],
                ["veerkracht", "Fv", "de veer op het voorwerp"],
                ["archimedeskracht", "FA", "de vloeistof op het voorwerp"],
            ])),
            ("p", "De <strong>normaalkracht</strong> is de <strong>kracht van het oppervlak op het "
                  "voorwerp, loodrecht op dat oppervlak</strong>; normaal betekent hier loodrecht. De "
                  "<strong>wrijvingskracht ligt langs het oppervlak</strong>, dus "
                  "<strong>staan die twee loodrecht op elkaar</strong>. Hun grootte heeft niets met "
                  "elkaar te maken behalve via de wrijvingscoëfficiënt."),
            ("p", "Ligt een <strong>boek stil op een tafel</strong>, dan werken er "
                  "<strong>twee krachten</strong>: de <strong>zwaartekracht</strong> trekt naar "
                  "beneden en de <strong>normaalkracht</strong> duwt terug. Die zijn even groot, dus "
                  "blijft het boek liggen."),
        ]),
        dict(kop="Krachten samenstellen en ontbinden", blokken=[
            ("p", "Alle krachten op een voorwerp samen geven de <strong>resulterende kracht</strong>, "
                  "of kort de <strong>resultante</strong>."),
            ("p", tabel(["Situatie", "Rekenwerk", "Resultante"], [
                ["120 N en 80 N, dezelfde zin", "120 + 80", "200 N, dezelfde zin"],
                ["150 N en 90 N, tegengesteld", "150 − 90", "60 N, zin van de grootste"],
                ["30 N en 45 N, tegengesteld", "45 − 30", "15 N, zin van de 45 N"],
                ["twee verschillende richtingen", "parallellogramregel", "de diagonaal"],
            ])),
            ("p", "Krachten met <strong>dezelfde richting en zin tel je op</strong>, met een "
                  "<strong>tegengestelde zin trek je ze van elkaar af</strong>, en de resultante wijst "
                  "dan <strong>in de zin van de grootste kracht</strong>. <strong>Twee krachten van "
                  "elk 50 N geven dus niet altijd 100 N</strong>: zijn ze tegengesteld, dan is de "
                  "resultante nul, en bij een hoek ertussen iets daartussen."),
            ("p", "Hebben de krachten een <strong>verschillende richting</strong>, dan gebruik je de "
                  "<strong>parallellogramregel</strong>: je tekent een parallellogram met de twee "
                  "vectoren als zijden, en de <strong>diagonaal vanuit het aangrijpingspunt is de "
                  "resultante</strong>."),
            ("p", "Omgekeerd kan je één kracht <strong>ontbinden in twee componenten</strong>. Wordt "
                  "een slee met een koord <strong>onder een hoek naar voren getrokken</strong>, dan "
                  "ontbind je die kracht in een <strong>horizontale en een verticale "
                  "component</strong>: de horizontale trekt de slee vooruit, de verticale tilt hem een "
                  "beetje op en vermindert zo de normaalkracht."),
            ("kader", "<strong>De resulterende kracht en de beweging.</strong> Is de resultante nul, "
                      "dan <strong>verandert de snelheid niet</strong> in grootte, richting of zin. Dat "
                      "kan rust zijn, maar ook een eenparige beweging: rijdt een auto met constante "
                      "snelheid, dan is de motorkracht even groot als de wrijving. Er werken dus wel "
                      "krachten, ze heffen elkaar enkel op."),
            ("p", "Hangt een <strong>voorwerp stil aan een veer</strong>, dan is de resultante nul, "
                  "dus is de <strong>veerkracht even groot als de zwaartekracht en omhoog "
                  "gericht</strong>."),
        ]),
        dict(kop="Zwaartekracht, massa en gewicht", blokken=[
            ("p", "De <strong>zwaartekracht</strong> is <strong>Fz = m . g</strong>, de massa maal de "
                  "<strong>zwaarteveldsterkte</strong>. In België is <strong>g = 9,81 N/kg</strong>. "
                  "Op een massa van 5,0 kg is dat Fz = 5,0 . 9,81 = <strong>49 N</strong>."),
            ("p", "<strong>De zwaarteveldsterkte en de valversnelling zijn hetzelfde getal met twee "
                  "eenheden</strong>: 9,81 N/kg en 9,81 m/s². Je bekijkt dezelfde g eens vanuit de "
                  "kracht en eens vanuit de beweging."),
            ("p", "<strong>De massa is een hoeveelheid materie, het gewicht is een kracht.</strong> De "
                  "massa in kilogram <strong>verandert niet van plaats tot plaats</strong>; het gewicht "
                  "is de kracht waarmee een lichaam op zijn steun duwt en wordt op de maan wel kleiner. "
                  "Daar is de zwaarteveldsterkte ongeveer 1,62 N/kg in plaats van 9,81 N/kg, dus is "
                  "<strong>de zwaartekracht er ongeveer zes keer kleiner</strong>."),
            ("p", "Een <strong>astronaut in een ruimtestation lijkt gewichtloos</strong>, maar zijn "
                  "<strong>massa blijft dezelfde als op aarde</strong>. Hij voelt zich gewichtloos "
                  "omdat hij samen met het station in een vrije val rond de aarde beweegt, niet omdat "
                  "de aarde niet meer aan hem trekt."),
            ("p", "Een <strong>balans die kilogram aangeeft, meet eigenlijk een kracht</strong> en "
                  "deelt die door 9,81. Op de maan zou dezelfde weegschaal daarom te weinig aangeven."),
            ("p", "Het <strong>zwaartepunt</strong> is <strong>het punt waar je de zwaartekracht mag "
                  "laten aangrijpen</strong>. Bij een regelmatig voorwerp van één materiaal ligt dat in "
                  "het midden, maar <strong>het ligt niet altijd binnen het voorwerp</strong>: bij een "
                  "ring of een hoefijzer ligt het in de lege ruimte ertussen."),
        ]),
        dict(kop="Veerkracht en wrijvingskracht", blokken=[
            ("p", "De <strong>veerkracht</strong> is <strong>Fv = k . Δl</strong>, met "
                  "<strong>k de veerconstante</strong> in <strong>newton per meter</strong> en Δl de "
                  "lengteverandering. De <strong>veerkracht is recht evenredig met de "
                  "lengteverandering</strong>: twee keer zo ver uitrekken vraagt twee keer zoveel "
                  "kracht, en in een grafiek geeft dat een rechte door de oorsprong."),
            ("p", tabel(["Gegeven", "Rekenwerk", "Antwoord"], [
                ["12 N rekt 4,0 cm uit", "12 / 0,040", "k = 300 N/m"],
                ["k = 250 N/m, F = 20 N", "20 / 250", "Δl = 8,0 cm"],
                ["2,0 kg aan k = 100 N/m", "19,62 / 100", "Δl = 19,6 cm"],
            ])),
            ("kader", "Reken de lengteverandering altijd eerst om naar meter: 4,0 cm is 0,040 m. "
                      "Vergeet je dat, dan zit je er een factor honderd naast."),
            ("p", "Hoe <strong>groter k, hoe stijver de veer</strong>. Hang je dezelfde massa aan twee "
                  "veren en <strong>rekt veer A verder uit, dan heeft A de kleinere "
                  "veerconstante</strong>."),
            ("p", "De <strong>statische wrijvingskracht</strong> is <strong>Fw = μ . Fn</strong>. De "
                  "<strong>wrijvingscoëfficiënt μ heeft geen eenheid</strong>, want het is een "
                  "verhouding van twee krachten, en ze <strong>hangt af van de twee materialen die "
                  "over elkaar schuiven</strong>, niet van de massa: die zit al in de normaalkracht."),
            ("p", "Op een <strong>horizontale vloer is Fn gelijk aan Fz</strong>. Voor een kist van "
                  "20 kg met μ = 0,30 is Fn = 20 . 9,81 = 196 N, dus Fw = 0,30 . 196 = "
                  "<strong>59 N</strong>. Een <strong>zwaarder voorwerp op dezelfde vloer ondervindt "
                  "dus een grotere wrijvingskracht</strong>, want de normaalkracht is groter. De "
                  "wrijvingscoëfficiënt blijft wel dezelfde, want de materialen veranderen niet."),
            ("weetje", "De wrijvingscoëfficiënt van rubber op droog asfalt ligt rond 0,8, maar op "
                       "ijs rond 0,1. Daarom heeft een auto op ijs een remweg die een veelvoud is van "
                       "die op droog wegdek, zonder dat zijn massa veranderd is."),
        ]),
    ],
    onthoud=[
        "Een kracht meet je in newton met een dynamometer; ze heeft grootte, richting, zin en aangrijpingspunt.",
        "Dezelfde zin: optellen. Tegengestelde zin: aftrekken, met de zin van de grootste. Verschillende richting: parallellogramregel.",
        "Resultante nul betekent dat de snelheid niet verandert, dus rust of een eenparige beweging.",
        "De normaalkracht staat loodrecht op het oppervlak, de wrijvingskracht erlangs.",
        "Fz = m . g, met g = 9,81 N/kg in België; dezelfde g is 9,81 m/s² als valversnelling.",
        "De massa verandert nooit van plaats tot plaats, het gewicht wel; een astronaut lijkt enkel gewichtloos.",
        "Fv = k . Δl, met Δl in meter; een kleine k betekent een slappe veer.",
        "Fw = μ . Fn; μ heeft geen eenheid en hangt af van de materialen, niet van de massa.",
        "Op een horizontale vloer is Fn gelijk aan Fz.",
    ],
)

# ───────────────────── 5. Archimedeskracht, moment en evenwicht
BUNDELS["archimedeskracht-moment-en-evenwicht-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Archimedeskracht, moment en evenwicht",
    onder="De wet van Archimedes, zinken, zweven, stijgen en drijven, het moment van een kracht, en het translatie- en rotatie-evenwicht.",
    secties=[
        dict(kop="De archimedeskracht", blokken=[
            ("p", "Een voorwerp in een vloeistof ondervindt een <strong>opwaartse kracht</strong>. Dat "
                  "is de <strong>archimedeskracht</strong>, genoemd naar de "
                  "<strong>wet van Archimedes</strong>: de "
                  "<strong>archimedeskracht is even groot als de zwaartekracht op de weggeduwde "
                  "vloeistof</strong>. Daarom staat in de formule de massadichtheid van de "
                  "<em>vloeistof</em> en niet die van het voorwerp."),
            ("p", "<strong>FA = ρ . g . Vond</strong>, met <strong>ρ</strong> de "
                  "<strong>massadichtheid</strong> van de vloeistof in <strong>kg/m³</strong>, g de "
                  "zwaarteveldsterkte en <strong>Vond het ondergedompelde volume</strong>. De "
                  "massadichtheid van <strong>water is 1000 kg/m³</strong>, of één kilogram per liter."),
            ("p", "De archimedeskracht is <strong>verticaal naar boven</strong> gericht. Daarom lijkt "
                  "een steen onder water lichter: hangt een <strong>steen van 50 N aan een dynamometer "
                  "en wijst die onder water 32 N aan</strong>, dan is de archimedeskracht "
                  "<strong>50 − 32 = 18 N</strong>."),
            ("p", tabel(["Gegeven", "Rekenwerk", "FA"], [
                ["0,0020 m³ volledig onder water", "1000 . 9,81 . 0,0020", "19,6 N"],
                ["0,0050 m³ volledig onder water", "1000 . 9,81 . 0,0050", "49 N"],
            ])),
            ("p", "<strong>Enkel ρ, g en Vond staan in de formule.</strong> De "
                  "<strong>massa en de vorm van het voorwerp tellen niet mee</strong>: twee voorwerpen "
                  "van hetzelfde volume ondervinden dezelfde archimedeskracht, ook als het ene veel "
                  "zwaarder is. <strong>De diepte staat er ook niet in</strong>: zolang het hele "
                  "voorwerp onder water zit, blijft FA dezelfde, ook tien meter lager. Drijft een blok "
                  "<strong>met driekwart van zijn volume onder water</strong>, dan gebruik je "
                  "<strong>driekwart van het volume</strong>, want enkel dat deel duwt water weg."),
            ("p", "<strong>Op de maan zou de archimedeskracht in hetzelfde bad water kleiner "
                  "zijn</strong>, want g staat in de formule. De zwaartekracht op het voorwerp wordt "
                  "wel even veel kleiner, dus drijft het nog altijd even diep."),
        ]),
        dict(kop="Zinken, zweven, stijgen en drijven", blokken=[
            ("p", tabel(["Wat gebeurt er", "Krachten", "Massadichtheid"], [
                ["zinken", "Fz groter dan FA", "ρ voorwerp groter dan ρ vloeistof"],
                ["zweven", "Fz gelijk aan FA", "ρ voorwerp gelijk aan ρ vloeistof"],
                ["stijgen", "FA groter dan Fz", "ρ voorwerp kleiner dan ρ vloeistof"],
                ["drijven", "FA gelijk aan Fz", "ρ voorwerp kleiner dan ρ vloeistof"],
            ])),
            ("p", "Een voorwerp dat <strong>zweeft</strong> blijft op dezelfde diepte hangen, dus is "
                  "de resulterende kracht nul en is de <strong>archimedeskracht even groot als de "
                  "zwaartekracht</strong>. Een voorwerp met een massadichtheid van "
                  "<strong>1200 kg/m³ zinkt in water</strong>, want dat is meer dan 1000 kg/m³. Een "
                  "<strong>voorwerp dat stijgt heeft juist een kleinere massadichtheid</strong> dan de "
                  "vloeistof."),
            ("p", "Bij <strong>drijven ligt het voorwerp stil</strong>, dus is de resultante ook nul: "
                  "het <strong>zakt net zo diep tot de archimedeskracht even groot is als zijn eigen "
                  "zwaartekracht</strong>."),
            ("p", "Een <strong>zwaar stalen schip drijft</strong> en een stalen bout zinkt, omdat het "
                  "<strong>schip hol is</strong>: binnenin zit lucht, dus komt zijn "
                  "<strong>gemiddelde massadichtheid onder 1000 kg/m³</strong>. Een "
                  "<strong>duikboot</strong> laat <strong>water in haar tanks om zwaarder te "
                  "worden</strong>: de massa stijgt terwijl het volume gelijk blijft, dus haalt de "
                  "zwaartekracht het van de archimedeskracht."),
            ("p", "Leg je hetzelfde voorwerp in <strong>zout water</strong>, dat een grotere "
                  "massadichtheid heeft, dan is de <strong>archimedeskracht groter bij hetzelfde "
                  "ondergedompelde volume</strong>, dus <strong>zit er een kleiner deel onder "
                  "water</strong>. De zwaartekracht hangt enkel van de massa af en verandert niet: het "
                  "voorwerp wordt in zout water niet zwaarder."),
        ]),
        dict(kop="Het moment van een kracht", blokken=[
            ("p", "Een kracht kan een voorwerp doen <strong>draaien</strong>. Hoeveel draaieffect ze "
                  "heeft, zegt het <strong>moment</strong>: <strong>M = F . d . sin α</strong>, met "
                  "<strong>d de krachtarm</strong> en α de hoek tussen de kracht en de arm. De eenheid "
                  "is de <strong>newtonmeter (Nm)</strong>, <strong>niet de joule</strong>: die hoort "
                  "bij arbeid en energie, ook al is ze eveneens een newton maal een meter."),
            ("p", "De <strong>krachtarm d</strong> is de <strong>afstand van het draaipunt tot het "
                  "aangrijpingspunt</strong> van de kracht. Een <strong>draaipunt heet ook een "
                  "steunpunt</strong> als het voorwerp erop rust, zoals bij een wip."),
            ("p", tabel(["Gegeven", "Rekenwerk", "M"], [
                ["40 N loodrecht op 0,50 m", "40 . 0,50 . sin 90°", "20 Nm"],
                ["25 N loodrecht op 0,80 m", "25 . 0,80 . 1", "20 Nm"],
                ["60 N onder 30° op 0,40 m", "60 . 0,40 . 0,50", "12 Nm"],
            ])),
            ("p", "<strong>Bij een hoek van 90° is het moment het grootst</strong>, want sin 90° is 1 "
                  "en blijft M = F . d over. Bij <strong>0° of 180° werkt de kracht langs de arm en is "
                  "het moment nul</strong>. Een <strong>kracht die door het draaipunt gaat, levert "
                  "geen moment</strong>: duwen op het hengsel van een deur doet ze niet draaien."),
            ("p", "Daarom gaat een <strong>moer losdraaien makkelijker met een lange sleutel</strong>: "
                  "de <strong>krachtarm is groter, dus wordt het moment groter</strong> bij dezelfde "
                  "kracht. Verdubbel je d, dan verdubbelt M."),
        ]),
        dict(kop="Statisch evenwicht", blokken=[
            ("p", "Een voorwerp in <strong>statisch evenwicht</strong> verschuift niet en draait niet. "
                  "Daar horen <strong>twee voorwaarden samen</strong> bij."),
            ("p", tabel(["Voorwaarde", "Balans", "Wat staat erin"], [
                ["translatie-evenwicht", "krachtenbalans", "de som van alle krachten is nul"],
                ["rotatie-evenwicht", "krachtmomentenbalans", "de som van alle momenten is nul"],
            ])),
            ("p", "<strong>Er mogen wel krachten werken, zolang ze elkaar opheffen.</strong> In een "
                  "<strong>krachtenbalans zet je enkel krachten in newton</strong>: voor een balk op "
                  "twee steunpunten zijn dat de <strong>zwaartekracht op de balk</strong> en de "
                  "<strong>twee steunkrachten</strong>. De momenten horen in de krachtmomentenbalans, "
                  "en een massa in kilogram is geen kracht."),
            ("kader", "<strong>Een krachtenbalans alleen is niet genoeg.</strong> Twee gelijke en "
                      "tegengestelde krachten op verschillende plaatsen heffen elkaar op als kracht, "
                      "maar kunnen het voorwerp wel doen draaien. Daarom bestaat er naast de "
                      "krachtenbalans ook een krachtmomentenbalans."),
            ("p", "Bij een <strong>wip</strong> moeten de momenten links en rechts gelijk zijn. Zit "
                  "links een kind van 30 kg op 1,2 m, dan geldt voor een kind van 36 kg rechts: "
                  "30 . 1,2 = 36 . d, dus <strong>d = 1,0 m</strong>. Het "
                  "<strong>zwaardere kind zit dus dichter bij het draaipunt</strong>."),
            ("p", "Het <strong>zwaartepunt bepaalt hoe stabiel</strong> iets staat. Een "
                  "<strong>bus met passagiers op het bovendek</strong> staat minder stabiel omdat zijn "
                  "<strong>zwaartepunt hoger ligt</strong>: hij moet minder ver kantelen voor het "
                  "zwaartepunt buiten het steunvlak komt, en dan doet het moment van de zwaartekracht "
                  "hem omvallen."),
            ("weetje", "Een hijskraan heeft een zwaar contragewicht aan de korte arm. Zo is het "
                       "moment van dat gewicht even groot als dat van de last aan de lange arm, en "
                       "blijft de kraan in rotatie-evenwicht."),
        ]),
    ],
    onthoud=[
        "FA = ρ . g . Vond; de massadichtheid van water is 1000 kg/m³.",
        "De massa, de vorm en de diepte van het voorwerp staan niet in die formule, enkel het ondergedompelde volume.",
        "Zinken: Fz groter dan FA. Zweven en drijven: even groot. Stijgen: FA groter.",
        "Een schip drijft omdat het hol is, dus met een gemiddelde massadichtheid onder 1000 kg/m³.",
        "M = F . d . sin α, in newtonmeter, niet in joule.",
        "Het moment is maximaal bij 90° en nul als de kracht door het draaipunt gaat.",
        "Een langere krachtarm geeft bij dezelfde kracht een groter moment.",
        "Statisch evenwicht: de som van de krachten is nul én de som van de momenten is nul.",
        "Op een wip: F₁ . d₁ = F₂ . d₂, dus het zwaardere kind zit dichter bij het draaipunt.",
    ],
)

# ───────────────────── 6. Druk bij vaste stoffen en in vloeistoffen
BUNDELS["druk-bij-vaste-stoffen-en-in-vloeistoffen-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Druk bij vaste stoffen en in vloeistoffen",
    onder="p = F/A en de eenheden van druk, de hydrostatische druk, de totale druk, het beginsel van Pascal en de hydraulische pers.",
    secties=[
        dict(kop="Druk op een oppervlak", blokken=[
            ("p", "De <strong>druk</strong> krijgt het symbool <strong>p</strong> (niet te verwarren "
                  "met P van vermogen) en is <strong>p = F / A</strong>: de kracht gedeeld door de "
                  "<strong>oppervlakte A</strong> waarop ze werkt. <strong>Druk is geen vector</strong>: "
                  "ze heeft geen richting, enkel een grootte en een eenheid. De kracht in de formule is "
                  "wel een vector."),
            ("p", "De <strong>SI-eenheid is de pascal (Pa)</strong>, en <strong>één pascal is één "
                  "newton per vierkante meter</strong>: twee namen voor dezelfde eenheid."),
            ("p", tabel(["Eenheid", "In pascal"], [
                ["1 Pa", "1 N/m²"],
                ["1 hPa (hectopascal)", "100 Pa"],
                ["1 mbar (millibar)", "100 Pa, dus even groot als 1 hectopascal"],
                ["1 kPa", "1000 Pa"],
                ["1 bar", "100 000 Pa, dus 1000 hPa"],
            ])),
            ("p", "Daarom staat op een weerkaart soms mbar en soms hPa voor hetzelfde getal. Een "
                  "<strong>fietsband op 4 bar staat op 400 000 Pa</strong>."),
            ("p", tabel(["Gegeven", "Rekenwerk", "p"], [
                ["600 N op 0,30 m²", "600 / 0,30", "2000 Pa"],
                ["240 N op 0,20 m bij 0,20 m", "240 / 0,040", "6000 Pa"],
                ["50 N op 0,010 m²", "50 / 0,010", "5000 Pa"],
            ])),
            ("p", "<strong>F staat in de teller en A in de noemer.</strong> Dus geeft "
                  "<strong>dezelfde kracht op een kleiner oppervlak een grotere druk</strong>, en een "
                  "<strong>grotere kracht op hetzelfde oppervlak ook</strong>. Leg je hetzelfde blok op "
                  "zijn <strong>kleinste zijde</strong>, dan blijft de kracht gelijk maar wordt A "
                  "kleiner, dus <strong>wordt de druk groter</strong>."),
        ]),
        dict(kop="Druk in het dagelijkse leven", blokken=[
            ("p", tabel(["Voorwerp", "Wat met A", "Gevolg"], [
                ["scherp mes, punaise, naald", "klein contactoppervlak", "veel druk bij weinig kracht"],
                ["sneeuwschoen, brede ski", "groot zooloppervlak", "weinig druk, je zakt niet"],
                ["plank onder een kraanpoot", "kracht uitspreiden", "de grond zakt niet in"],
                ["dubbele wielen op een vrachtwagen", "meer contactoppervlak", "minder schade aan het wegdek"],
            ])),
            ("p", "Met <strong>sneeuwschoenen zak je minder diep</strong> omdat het "
                  "<strong>zooloppervlak groter is, dus de druk kleiner</strong>. Je gewicht verandert "
                  "niet; het verdeelt zich enkel over een grotere oppervlakte. Een "
                  "<strong>naaldhak</strong> doet net het omgekeerde en is dus geen goed idee voor een "
                  "wandeling in de sneeuw."),
            ("p", "Staan <strong>twee mensen met dezelfde schoenmaat in de modder</strong>, dan zakt de "
                  "zwaarste dieper: de <strong>oppervlakte is gelijk, dus beslist de kracht</strong>, "
                  "en een grotere massa geeft een grotere zwaartekracht."),
            ("p", "Wil je met een gegeven kracht een <strong>zo grote druk mogelijk</strong>, dan maak "
                  "je het <strong>contactoppervlak zo klein mogelijk</strong>. Daarom slijpt men een "
                  "mes scherp."),
        ]),
        dict(kop="Druk in een vloeistof", blokken=[
            ("p", "In een vloeistof <strong>draagt elke laag het gewicht van alles erboven</strong>. "
                  "Daarom <strong>ontstaat er hydrostatische druk</strong>, en die groeit gelijkmatig "
                  "met de diepte: <strong>p = ρ . g . h</strong>."),
            ("p", "<strong>Enkel ρ, g en h staan in de formule.</strong> De "
                  "<strong>vorm van het vat en de totale hoeveelheid vloeistof tellen niet mee</strong>: "
                  "op dezelfde diepte is de druk in een <strong>smal buisje even groot als in een breed "
                  "bad</strong>."),
            ("p", tabel(["Diepte in water", "Rekenwerk", "Hydrostatische druk"], [
                ["2,0 m", "1000 . 9,81 . 2,0", "ongeveer 20 kPa"],
                ["5,0 m", "1000 . 9,81 . 5,0", "ongeveer 49 kPa"],
                ["ongeveer 10 m", "1000 . 9,81 . 10,3", "ongeveer 1013 hPa"],
            ])),
            ("p", "De <strong>totale druk</strong> op een diepte is de <strong>hydrostatische druk plus "
                  "de luchtdruk</strong>, want boven het water duwt de atmosfeer al met "
                  "<strong>1013 hPa</strong>. Op ongeveer <strong>10 m diepte is de hydrostatische druk "
                  "even groot als de luchtdruk</strong>, dus is de totale druk daar al bijna het dubbele "
                  "van aan het oppervlak."),
            ("p", "In <strong>zeewater</strong> is de <strong>massadichtheid groter</strong>, dus is de "
                  "<strong>hydrostatische druk op dezelfde diepte groter</strong>. De diepte telt nog "
                  "altijd mee, en de luchtdruk boven de zee is dezelfde."),
            ("p", "De <strong>druk in een vloeistof werkt in alle richtingen</strong>, dus ook "
                  "<strong>op de zijwanden van het vat</strong>. Daarom spuit er water uit een gaatje "
                  "in de zijkant van een emmer."),
            ("p", "Je meet de <strong>luchtdruk met een barometer</strong> en de druk in een vat of een "
                  "leiding met een <strong>manometer</strong>. <strong>Overdruk</strong> is wat er boven "
                  "de luchtdruk zit, <strong>onderdruk</strong> wat eronder zit. Een manometer die "
                  "<strong>2 bar overdruk</strong> aangeeft, hoort bij een totale druk van ongeveer "
                  "<strong>3 bar</strong>. <strong>Hoger in de atmosfeer wordt de luchtdruk "
                  "kleiner</strong>, want er zit minder lucht boven je: op een hoge berg is ze maar "
                  "twee derde van die aan de zee."),
            ("p", "Bij het <strong>duiken moet je je oren klaren</strong> omdat de "
                  "<strong>druk op het trommelvlies met de diepte groeit</strong> terwijl de druk "
                  "binnen gelijk blijft. Klaren laat lucht door de buis van Eustachius zodat de druk aan "
                  "beide kanten even groot wordt."),
        ]),
        dict(kop="Het beginsel van Pascal", blokken=[
            ("p", "Het <strong>beginsel van Pascal</strong> zegt dat een "
                  "<strong>drukverandering zich in heel de vloeistof voortplant</strong>. Duw je ergens "
                  "op een ingesloten vloeistof, dan stijgt de druk overal met hetzelfde bedrag."),
            ("p", "Daar werkt een <strong>hydraulische pers</strong> op, en ook een hydraulische "
                  "schijfrem. Uit p = F / A volgt <strong>F = p . A</strong>: de "
                  "<strong>druk is overal gelijk, dus geeft een grotere oppervlakte een grotere "
                  "kracht</strong>. Bij een tien keer grotere zuiger krijg je tien keer meer kracht."),
            ("kader", "<strong>Een pers maakt geen energie bij.</strong> De kracht wordt groter, maar "
                      "de weg wordt even veel kleiner: de grote zuiger komt tien keer minder ver. De "
                      "arbeid blijft dus dezelfde, op de wrijving na."),
            ("weetje", "Een autokrik met vloeistof werkt op dit beginsel. Je duwt tientallen keren op "
                       "een kleine hendel en de auto komt elke keer een paar millimeter hoger, want de "
                       "energie die je erin stopt, moet er ook weer uit."),
        ]),
    ],
    onthoud=[
        "p = F / A; de pascal is één newton per vierkante meter.",
        "1 hPa = 1 mbar = 100 Pa, en 1 bar = 100 000 Pa = 1000 hPa.",
        "Een kleiner oppervlak of een grotere kracht geeft meer druk: mes en punaise tegenover ski en plank.",
        "p = ρ . g . h voor de hydrostatische druk; de vorm van het vat telt niet mee.",
        "De totale druk is de hydrostatische druk plus de luchtdruk van 1013 hPa.",
        "Op ongeveer 10 m diepte in water is de hydrostatische druk even groot als de luchtdruk.",
        "De druk in een vloeistof werkt in alle richtingen, ook op de zijwanden.",
        "Barometer voor de luchtdruk, manometer voor de druk in een vat; overdruk zit boven de luchtdruk.",
        "Beginsel van Pascal: een drukverandering plant zich overal voort; een pers geeft meer kracht maar geen extra energie.",
    ],
)

# ───────────────────── 7. Gassen, temperatuur en de gaswetten
BUNDELS["gassen-temperatuur-en-de-gaswetten-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Gassen, temperatuur en de gaswetten",
    onder="Gasdruk volgens het deeltjesmodel, de kelvinschaal en het absolute nulpunt, de afzonderlijke gaswetten, de ideale gaswet en de grafieken.",
    secties=[
        dict(kop="Gasdruk en het deeltjesmodel", blokken=[
            ("p", "De <strong>deeltjes van een gas bewegen vrij door elkaar</strong> en "
                  "<strong>vullen altijd het hele volume van hun vat</strong>. Elk deeltje dat "
                  "<strong>tegen de wand botst</strong>, duwt er even tegen, en samen geven die "
                  "miljarden botsingen een constante <strong>druk</strong>."),
            ("p", "<strong>Hoe sneller de deeltjes bewegen, hoe groter de druk</strong>, want ze "
                  "botsen harder en vaker. Wordt een gas <strong>opgewarmd in een gesloten vat van vast "
                  "volume, dan stijgt de druk</strong>. Wordt het bij gelijke temperatuur "
                  "<strong>samengedrukt</strong>, dan stijgt de druk ook, want dezelfde deeltjes "
                  "botsen dan op een kleiner oppervlak. En <strong>meer deeltjes in hetzelfde volume "
                  "geven ook meer druk</strong>: dat is wat je doet bij het oppompen van een band. "
                  "Laat je <strong>lucht uit een fietsband ontsnappen</strong>, dan blijven er "
                  "<strong>minder deeltjes over, dus daalt de druk</strong>."),
            ("p", "<strong>Hoger in de atmosfeer wordt de luchtdruk kleiner</strong>, want de "
                  "luchtdruk komt van het gewicht van alle lucht erboven en daar zit er minder lucht "
                  "boven je."),
            ("p", "<strong>Overdruk</strong> is wat er boven de luchtdruk zit. Een gas op "
                  "<strong>1,5 bar overdruk</strong> staat dus op een totale druk van ongeveer "
                  "<strong>2,5 bar</strong>. Zit de druk onder de luchtdruk, dan heet het "
                  "<strong>onderdruk</strong>. De luchtdruk meet je met een <strong>barometer</strong>."),
        ]),
        dict(kop="De kelvinschaal en het absolute nulpunt", blokken=[
            ("p", "De <strong>absolute temperatuur T</strong> staat in <strong>kelvin (K)</strong>, de "
                  "SI-eenheid, en wordt zonder gradenteken geschreven. Reken om met "
                  "<strong>T = θ + 273,15</strong>."),
            ("p", tabel(["Omrekening", "Rekenwerk", "Antwoord"], [
                ["25 °C naar K", "25 + 273,15", "ongeveer 298 K"],
                ["0 °C naar K", "0 + 273,15", "273,15 K (de normtemperatuur)"],
                ["200 K naar °C", "200 − 273,15", "ongeveer −73 °C"],
                ["0 K naar °C", "0 − 273,15", "−273,15 °C"],
            ])),
            ("p", "<strong>Een temperatuursverschil van 20 °C is hetzelfde als een verschil van "
                  "20 K</strong>: de stappen van de twee schalen zijn even groot, enkel hun nulpunt "
                  "ligt anders, en bij een verschil valt dat weg."),
            ("p", "De <strong>absolute temperatuur is een maat voor de gemiddelde kinetische energie "
                  "van de deeltjes</strong>: warmer betekent gemiddeld sneller. Bij het "
                  "<strong>absolute nulpunt, 0 K of −273,15 °C</strong>, staan de deeltjes in het "
                  "model stil. Dan is de <strong>kinetische energie van de deeltjes nul</strong>, de "
                  "<strong>druk van het gas nul</strong> en het <strong>volume van een ideaal gas "
                  "nul</strong>. Hun massa blijft wel bestaan, en lager dan 0 K kan niet: de deeltjes "
                  "kunnen niet langzamer dan stil."),
            ("kader", "<strong>In de gaswetten vul je de temperatuur altijd in kelvin in.</strong> De "
                      "wetten gaan uit van het absolute nulpunt, en met graden Celsius kom je bij 0 °C "
                      "zelfs op een deling door nul."),
        ]),
        dict(kop="De gaswetten", blokken=[
            ("p", "De <strong>vier toestandsgrootheden</strong> van een gas zijn "
                  "<strong>druk p, volume V, absolute temperatuur T en stofhoeveelheid n</strong> (in "
                  "mol). De <strong>ideale gaswet</strong> bindt ze samen: "
                  "<strong>p . V = n . R . T</strong>, met <strong>R = 8,31 J/(mol.K)</strong>."),
            ("p", "De <strong>universele gasconstante R geldt voor elk gas</strong>. Enkel een "
                  "<em>specifieke</em> gasconstante per kilogram verschilt van gas tot gas."),
            ("p", "Blijft de <strong>stofhoeveelheid gelijk</strong>, dan geldt de "
                  "<strong>algemene gaswet p.V/T = constant</strong>. Daar mogen p, V en T alle drie "
                  "veranderen. Houd je er één vast, dan krijg je de <strong>afzonderlijke "
                  "gaswetten</strong>."),
            ("p", tabel(["Proces", "Wat blijft gelijk", "Wet", "Verband"], [
                ["isotherm", "de temperatuur", "p . V = constant", "omgekeerd evenredig"],
                ["isobaar", "de druk", "V / T = constant", "recht evenredig"],
                ["isochoor", "het volume", "p / T = constant", "recht evenredig"],
            ])),
            ("p", "<strong>Iso betekent gelijk.</strong> <strong>Therm</strong> hoort bij warmte, "
                  "<strong>baar</strong> bij druk en <strong>choor</strong> bij ruimte, dus bij het "
                  "volume."),
            ("p", tabel(["Opgave", "Rekenwerk", "Antwoord"], [
                ["3,0 L bij 2,0 bar naar 1,0 L, isotherm", "2,0 . 3,0 = p . 1,0", "6,0 bar"],
                ["4,0 L bij 1,0 bar naar 2,0 bar, isotherm", "1,0 . 4,0 = 2,0 . V", "2,0 L"],
                ["2,0 L bij 300 K naar 450 K, isobaar", "2,0 / 300 = V / 450", "3,0 L"],
                ["1,0 bar bij 290 K naar 580 K, isochoor", "T verdubbelt", "2,0 bar"],
            ])),
            ("p", "Gaat een gas van 2,0 bar in 5,0 L naar 4,0 bar in 2,5 L, dan "
                  "<strong>blijft het product p.V gelijk</strong> (10 in beide gevallen). Volgens "
                  "p.V/T = constant <strong>blijft T dan ook gelijk</strong>: het is een isotherm "
                  "proces, en er is geen gas weggelopen."),
            ("kader", "<strong>Een spuitbus hoort niet in de zon.</strong> Bij vast volume is "
                      "p/T constant, dus stijgt de druk mee met de temperatuur. Daarom staat er op de "
                      "bus dat ze niet boven 50 °C mag komen."),
        ]),
        dict(kop="De grafieken van een gas", blokken=[
            ("p", tabel(["Grafiek", "Wat constant blijft", "Vorm"], [
                ["p(V)", "de temperatuur", "dalende kromme die de assen niet raakt"],
                ["V(T), T in kelvin", "de druk", "rechte door de oorsprong"],
                ["p(T), T in kelvin", "het volume", "rechte door de oorsprong"],
            ])),
            ("p", "Bij een <strong>isotherm proces zijn p en V omgekeerd evenredig</strong>, dus blijft "
                  "hun product gelijk en krijg je een <strong>kromme die steeds vlakker daalt</strong>. "
                  "Bij een <strong>isobaar proces is V recht evenredig met T</strong>: in kelvin gaat "
                  "die rechte <strong>door de oorsprong</strong>, want bij 0 K zou het volume nul zijn. "
                  "Hetzelfde geldt voor <strong>p(T) bij vast volume</strong>."),
            ("p", "Je kan een <strong>p(V)-grafiek omzetten naar een p(T)-grafiek</strong> met "
                  "p.V/T = constant, punt per punt. Je moet wel weten "
                  "<strong>welke grootheid vastgehouden werd</strong>, anders kan je niet omrekenen."),
            ("p", "Bij <strong>normomstandigheden</strong> hoort de <strong>normdruk van 1013 hPa</strong> "
                  "en de <strong>normtemperatuur van 273,15 K</strong>. Een gasvolume dat men vergelijkt, "
                  "wordt meestal naar die omstandigheden herrekend."),
            ("weetje", "Een <strong>ideaal gas bestaat in het echt niet</strong>: in het model hebben "
                       "de deeltjes geen eigen volume en trekken ze elkaar niet aan. Echte gassen "
                       "volgen de wetten wel goed bij lage druk en hoge temperatuur, en gaan er pas "
                       "van afwijken als ze bijna vloeibaar worden."),
        ]),
    ],
    onthoud=[
        "Gasdruk komt van de botsingen van de deeltjes op de wand; sneller of meer deeltjes geeft meer druk.",
        "T = θ + 273,15; het absolute nulpunt is 0 K of −273,15 °C.",
        "Bij 0 K zijn de kinetische energie, de druk en het volume van een ideaal gas nul.",
        "Een verschil van 20 °C is hetzelfde als een verschil van 20 K.",
        "In de gaswetten vul je de temperatuur altijd in kelvin in.",
        "Isotherm: p . V = constant. Isobaar: V / T = constant. Isochoor: p / T = constant.",
        "Ideale gaswet: p . V = n . R . T, met R = 8,31 J/(mol.K) voor elk gas.",
        "Een p(V)-grafiek bij vaste T is een dalende kromme; V(T) en p(T) in kelvin zijn rechten door de oorsprong.",
        "Normdruk 1013 hPa en normtemperatuur 273,15 K zijn de normomstandigheden.",
    ],
)

# ───────────────────── 8. Arbeid, energie, vermogen en rendement
BUNDELS["arbeid-energie-vermogen-en-rendement-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Arbeid, energie, vermogen en rendement",
    onder="Arbeid met cos α, de energievormen en hun formules, de wet van behoud van energie, de energiedissipatie, het vermogen en het rendement.",
    secties=[
        dict(kop="Arbeid", blokken=[
            ("p", "De <strong>arbeid</strong> van een kracht is <strong>W = F . Δx . cos α</strong>, "
                  "met α de hoek tussen de kracht en de verplaatsing. Het symbool komt van het Engelse "
                  "<em>work</em>, en de <strong>eenheid is de joule (J)</strong>."),
            ("p", tabel(["Hoek", "cos α", "Arbeid", "Voorbeeld"], [
                ["0°", "1", "positief", "duwen in de zin van de beweging"],
                ["90°", "0", "geen arbeid", "een doos horizontaal dragen"],
                ["180°", "−1", "negatief", "wrijving, of de zwaartekracht bij optillen"],
            ])),
            ("p", "Duw je een kar <strong>8,0 m vooruit met 50 N in de zin van de beweging</strong>, "
                  "dan is W = 50 . 8,0 . 1 = <strong>400 J</strong>. Een kracht van 25 N over 4,0 m "
                  "geeft <strong>100 J</strong>."),
            ("p", "Een <strong>wrijvingskracht werkt tegen de beweging in</strong>, dus "
                  "<strong>verricht ze negatieve arbeid</strong>: ze haalt energie uit de beweging. "
                  "Ook de <strong>zwaartekracht verricht negatieve arbeid op een voorwerp dat je "
                  "optilt</strong>, want ze wijst naar beneden en de verplaatsing naar boven; jij "
                  "verricht dan positieve arbeid tegen haar in."),
            ("kader", "<strong>Een kracht loodrecht op de verplaatsing verricht geen arbeid.</strong> "
                      "Draag je een doos horizontaal door een kamer, dan is W nul, al voelt het zwaar "
                      "aan. Hetzelfde geldt voor de normaalkracht op een voorwerp dat over een vlakke "
                      "vloer schuift."),
        ]),
        dict(kop="De energievormen", blokken=[
            ("p", tabel(["Energievorm", "Formule"], [
                ["kinetische energie", "Ek = m . v² / 2"],
                ["potentiële gravitationele energie", "Ep,gr = m . g . h"],
                ["potentiële elastische energie", "Ep,el = k . Δl² / 2"],
            ])),
            ("p", "De andere energievormen die je moet kennen, hebben hier geen formule: "
                  "<strong>chemische energie, thermische energie of warmte, stralingsenergie, "
                  "kernenergie en elektrische energie</strong>. <strong>Wrijving is een kracht en druk "
                  "een grootheid</strong>, geen van beide een energievorm."),
            ("p", tabel(["Opgave", "Rekenwerk", "Antwoord"], [
                ["1200 kg met 20 m/s", "1200 . 400 / 2", "240 kJ"],
                ["5,0 kg, 3,0 m omhoog", "5,0 . 9,81 . 3,0", "147 J"],
                ["2,0 kg, 10 m hoog", "2,0 . 9,81 . 10", "196 J"],
            ])),
            ("p", "In Ek staat de <strong>snelheid in het kwadraat</strong>. Een auto die "
                  "<strong>twee keer zo snel rijdt, heeft dus vier keer zoveel kinetische "
                  "energie</strong>, niet twee keer. Daarom is een remweg bij dubbele snelheid vier "
                  "keer zo lang."),
            ("p", "Een <strong>voorwerp dat stilstaat kan toch potentiële energie hebben</strong>: een "
                  "steen bovenop een muur heeft Ep,gr door zijn hoogte. Enkel zijn kinetische energie "
                  "is nul."),
            ("p", "De <strong>eenheid van energie is de joule</strong>, maar je komt ook de "
                  "<strong>kilowattuur</strong> en de <strong>kilocalorie</strong> tegen. Een "
                  "<strong>kilowattuur is een eenheid van energie, niet van vermogen</strong>: het is "
                  "een vermogen maal een tijd, en één kWh is 3,6 miljoen joule."),
        ]),
        dict(kop="Energieomzettingen en de energiebalans", blokken=[
            ("p", "De <strong>wet van behoud van energie</strong> zegt dat "
                  "<strong>energie niet verdwijnt maar van vorm verandert</strong>. In een geïsoleerd "
                  "systeem blijft de som van alle energie gelijk."),
            ("p", tabel(["Soort systeem", "Materie", "Energie"], [
                ["open", "gaat erin en eruit", "gaat erin en eruit"],
                ["gesloten", "blijft binnen", "gaat erin en eruit"],
                ["geïsoleerd", "blijft binnen", "blijft binnen"],
            ])),
            ("p", "In een <strong>geïsoleerd systeem gaat er geen energie en geen materie in of "
                  "uit</strong>. Binnenin mag de energie wel van vorm veranderen, zolang de som gelijk "
                  "blijft."),
            ("p", tabel(["Wat gebeurt er", "Omzetting"], [
                ["een bal valt van een muur", "Ep,gr naar Ek"],
                ["een bal omhoog gooien", "Ek naar Ep,gr"],
                ["een elektrische waterkoker", "elektrisch naar thermisch"],
                ["een plant doet fotosynthese", "straling naar chemisch"],
                ["een ingedrukte veer schiet los", "Ep,el naar Ek"],
            ])),
            ("p", "Bij een <strong>vrije val zonder luchtweerstand blijft de som van Ek en Ep,gr "
                  "gelijk</strong>: de ene vorm wordt de andere, zonder verlies. Daarom kan je de "
                  "snelheid onderaan uit de hoogte berekenen."),
            ("p", "Bij elke omzetting in het dagelijkse leven gaat een deel naar een "
                  "<strong>minder bruikbare vorm, meestal warmte</strong>. Dat heet "
                  "<strong>energiedissipatie</strong>. Die energie <strong>bestaat nog, maar is zo "
                  "verspreid dat je ze niet meer nuttig kan gebruiken</strong>: ze is niet verdwenen."),
            ("p", "In een <strong>stroomdiagram</strong> zet je uit waar de energie naartoe gaat. De "
                  "<strong>breedte van een pijl hoort bij de hoeveelheid energie</strong>, en "
                  "<strong>alle uitgaande energie samen is zoveel als de ingaande</strong>, want niets "
                  "verdwijnt. De <strong>ongewenste energie hoort er dus ook in</strong>, niet enkel de "
                  "nuttige."),
            ("p", "Het <strong>arbeid-energietheorema</strong> zegt dat de "
                  "<strong>arbeid van de resulterende kracht gelijk is aan de verandering van de "
                  "kinetische energie</strong>. Verricht ze positieve arbeid, dan gaat het voorwerp "
                  "sneller; verricht ze negatieve arbeid, dan vertraagt het."),
        ]),
        dict(kop="Vermogen en rendement", blokken=[
            ("p", "Het <strong>vermogen</strong> is <strong>P = |ΔE| / Δt</strong>: de omgezette "
                  "energie gedeeld door de tijd die het duurde. De <strong>eenheid is de watt</strong>, "
                  "en <strong>één watt is één joule per seconde</strong>."),
            ("p", tabel(["Opgave", "Rekenwerk", "Antwoord"], [
                ["48 kJ in 20 s", "48 000 / 20", "2,4 kW"],
                ["500 W gedurende 60 s", "500 . 60", "30 000 J"],
            ])),
            ("kader", "<strong>Een groter vermogen betekent sneller, niet duurder.</strong> Doen twee "
                      "toestellen hetzelfde werk, dan gebruikt dat met het kleinste vermogen minder "
                      "energie, maar een krachtiger pomp verzet hetzelfde water in minder tijd met "
                      "ongeveer dezelfde energie."),
            ("p", "Het <strong>rendement</strong> is <strong>η = Enuttig / Etotaal</strong>, met de "
                  "Griekse letter eta. Het <strong>heeft geen eenheid</strong>, want het is een "
                  "verhouding, en wordt vaak als percentage geschreven."),
            ("p", tabel(["Opgave", "Rekenwerk", "η"], [
                ["lamp: 60 J in, 9,0 J licht", "9,0 / 60", "15 %"],
                ["motor: 2000 J in, 1400 J warmte", "600 / 2000", "30 %"],
                ["motor: 800 J in, 200 J nuttig", "200 / 800", "25 %"],
            ])),
            ("p", "<strong>Een rendement van meer dan 100 % kan niet bestaan.</strong> Je kan er niet "
                  "meer uithalen dan je erin stopt, en er gaat altijd een deel naar warmte."),
            ("p", "Het <strong>joule-effect</strong> is het opwarmen van een geleider door de stroom "
                  "erdoor. Dat is <strong>niet in elke toepassing ongewenst</strong>: in een gloeilamp "
                  "of een waterkoker heb je het net nodig, in een laadkabel of een stekkerdoos niet."),
            ("weetje", "Een ledlamp haalt ongeveer 40 % rendement en een oude gloeilamp maar 5 %. De "
                       "overige 95 % werd bij die gloeilamp warmte, en dat is net waarom de draad licht "
                       "gaf."),
        ]),
    ],
    onthoud=[
        "W = F . Δx . cos α; bij 0° positief, bij 90° geen arbeid, bij 180° negatief.",
        "Ek = m . v² / 2, Ep,gr = m . g . h, Ep,el = k . Δl² / 2.",
        "Twee keer zo snel geeft vier keer zoveel kinetische energie.",
        "Een kilowattuur is een eenheid van energie, geen vermogen.",
        "Energie verdwijnt niet, ze verandert van vorm; in een geïsoleerd systeem blijft de som gelijk.",
        "Energiedissipatie: bruikbare energie wordt warmte die je niet meer kan gebruiken.",
        "Arbeid-energietheorema: de arbeid van de resultante is de verandering van de Ek.",
        "P = |ΔE| / Δt, in watt; één watt is één joule per seconde.",
        "η = Enuttig / Etotaal, zonder eenheid en altijd onder 100 %.",
    ],
)

# ───────────────────── 9. Warmte, faseovergangen en de warmtebalans
BUNDELS["warmte-faseovergangen-en-de-warmtebalans-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Warmte, faseovergangen en de warmtebalans",
    onder="Temperatuur en warmte, het thermisch evenwicht, geleiding, convectie en straling, de merkbare en de latente warmte, en de warmtebalans.",
    secties=[
        dict(kop="Temperatuur, warmte en inwendige energie", blokken=[
            ("p", "<strong>Temperatuur en warmte zijn niet hetzelfde.</strong> De "
                  "<strong>temperatuur hoort bij de gemiddelde kinetische energie van de "
                  "deeltjes</strong>: ze zegt hoe snel die gemiddeld bewegen. "
                  "<strong>Warmte is energie die overgedragen wordt</strong>, met symbool "
                  "<strong>Q</strong> en als eenheid de <strong>joule</strong>. Dezelfde letter Q "
                  "staat ook voor elektrische lading, dus let op de context."),
            ("p", "De <strong>warmtestroom gaat altijd van het warme naar het koude voorwerp</strong>, "
                  "en <strong>stopt zodra beide dezelfde temperatuur hebben</strong>. Dat eindpunt heet "
                  "het <strong>thermisch evenwicht</strong>. De <strong>massa van de voorwerpen beslist "
                  "daar niets over</strong>: een kopje thee kan heter zijn dan een vol zwembad, dus "
                  "heeft een <strong>groot voorwerp niet altijd een hogere temperatuur</strong>."),
            ("p", "De <strong>inwendige energie</strong> van een voorwerp bestaat uit "
                  "<strong>twee delen</strong>: de <strong>inwendige kinetische energie</strong> van "
                  "de bewegende deeltjes en de <strong>inwendige potentiële energie</strong> van hun "
                  "onderlinge aantrekking. Ze <strong>stijgt als de absolute temperatuur "
                  "stijgt</strong>. Bij <strong>0 °C is ze niet nul</strong>: er is daar nog beweging, "
                  "pas bij 0 K zou die stoppen."),
            ("p", "De <strong>warmtebalans is een toepassing van de wet van behoud van energie</strong>: "
                  "de warmte die het warme voorwerp afgeeft, neemt het koude op. Je meet die op in een "
                  "<strong>calorimeter</strong> of <strong>joulevat</strong>, dat goed geïsoleerd is."),
        ]),
        dict(kop="Warmtetransport", blokken=[
            ("p", tabel(["Vorm", "Hoe het werkt", "Waar"], [
                ["geleiding", "de deeltjes geven hun beweging door", "vooral in vaste stoffen"],
                ["convectie of stroming", "de warme stof beweegt zelf", "in vloeistoffen en gassen"],
                ["straling", "zonder stof, door golven", "ook door de lege ruimte"],
            ])),
            ("p", "Bij <strong>convectie beweegt de warme stof zelf naar een andere plaats</strong>: "
                  "warme lucht of warm water is lichter en stijgt, koude stof zakt. In een vaste stof "
                  "kan de stof niet stromen, dus werkt daar geleiding."),
            ("p", "<strong>Straling heeft geen stof nodig</strong>, en dat is net het verschil met de "
                  "twee andere. Daarom kan de <strong>warmte van de zon ons door de lege ruimte "
                  "bereiken</strong>."),
            ("p", "<strong>Metaal en hout van dezelfde temperatuur voelen niet even koud aan.</strong> "
                  "Metaal <strong>geleidt de warmte van je hand snel weg</strong>, dus voelt het kouder. "
                  "Hout geleidt slecht, dus blijft je hand daar warm."),
        ]),
        dict(kop="Merkbare warmte", blokken=[
            ("p", "<strong>Merkbare warmte</strong> is de warmte die de "
                  "<strong>temperatuur van een stof doet veranderen</strong>: "
                  "<strong>Q = c . m . ΔT</strong> voor een stof, of <strong>Q = C . ΔT</strong> voor "
                  "een voorwerp."),
            ("p", tabel(["Grootheid", "Symbool", "Eenheid", "Waarvoor"], [
                ["specifieke warmtecapaciteit", "c", "J/(kg.K)", "per kilogram van een stof"],
                ["warmtecapaciteit", "C", "J/K", "van dat ene voorwerp"],
            ])),
            ("p", "<strong>C hoort dus bij een voorwerp en c bij één kilogram van een stof.</strong> De "
                  "specifieke warmtecapaciteit van <strong>water is 4186 J/(kg.K)</strong>: dat is net "
                  "de warmte die je nodig hebt om <strong>1,0 kg water 1,0 K op te warmen</strong>."),
            ("p", tabel(["Opgave", "Rekenwerk", "Antwoord"], [
                ["2,0 kg water 10 K opwarmen", "4186 . 2,0 . 10", "ongeveer 84 kJ"],
                ["0,50 kg met c = 900, Q = 9,0 kJ", "9000 / (900 . 0,50)", "ΔT = 20 K"],
                ["0,10 kg van 80 °C bij 0,10 kg van 20 °C", "(80 + 20) / 2", "50 °C"],
            ])),
            ("p", "Een <strong>grote c betekent dat er veel warmte nodig is per kilogram per "
                  "kelvin</strong>, dus dat de stof <strong>traag opwarmt</strong>. Water heeft een "
                  "grote c en blijft daarom lang koel in de lente en lang warm in de herfst. "
                  "<strong>Een kleine c betekent net snel opwarmen</strong>: een pan van metaal is "
                  "sneller heet dan het water erin."),
        ]),
        dict(kop="Faseovergangen en latente warmte", blokken=[
            ("p", tabel(["Faseovergang", "Van", "Naar", "Warmte"], [
                ["smelten", "vast", "vloeibaar", "nodig"],
                ["stollen", "vloeibaar", "vast", "komt vrij"],
                ["verdampen", "vloeibaar", "gas", "nodig"],
                ["condenseren", "gas", "vloeibaar", "komt vrij"],
                ["sublimeren", "vast", "gas", "nodig"],
                ["desublimeren", "gas", "vast", "komt vrij"],
            ])),
            ("p", "<strong>Stollen en condenseren geven warmte af</strong>, want de stof gaat naar een "
                  "meer gebonden toestand. <strong>Smelten en verdampen hebben juist warmte "
                  "nodig.</strong> <strong>Sublimeren slaat de vloeibare fase over</strong>: droogijs "
                  "doet dat, en <strong>rijp die verdwijnt zonder eerst te smelten</strong> ook."),
            ("p", "De <strong>latente warmte</strong> is <strong>Q = l . m</strong>. Er staat "
                  "<strong>geen ΔT in</strong>, want <strong>tijdens een faseovergang blijft de "
                  "temperatuur gelijk</strong>: alle warmte gaat naar het veranderen van de fase, niet "
                  "naar de beweging van de deeltjes. In een opwarmingscurve zie je daarom een "
                  "<strong>horizontaal stuk, een plateau</strong>."),
            ("p", tabel(["Soort latente warmte", "Symbool"], [
                ["specifieke smeltwarmte en stolwarmte", "ls"],
                ["specifieke verdampingswarmte en condensatiewarmte", "lv"],
            ])),
            ("p", "Ook <strong>sublimeren vraagt latente warmte</strong>. Omdat de stof de vloeibare "
                  "fase overslaat, is die <strong>ongeveer de som van de smeltwarmte en de "
                  "verdampingswarmte</strong>."),
            ("p", "De <strong>specifieke smeltwarmte en de specifieke stolwarmte van een stof zijn "
                  "dezelfde waarde</strong>: wat je bij het smelten moet toevoegen, komt bij het "
                  "stollen weer vrij. Enkel de zin van de warmtestroom is omgekeerd. De eenheid is "
                  "<strong>J/kg</strong>."),
            ("p", tabel(["Opgave", "Rekenwerk", "Antwoord"], [
                ["0,20 kg ijs smelten, ls = 334 kJ/kg", "334 000 . 0,20", "ongeveer 67 kJ"],
                ["0,50 kg smelten, ls = 200 kJ/kg", "200 000 . 0,50", "100 kJ"],
            ])),
            ("p", "Tijdens het <strong>smelten worden de cohesiekrachten tussen de deeltjes "
                  "losser</strong> en <strong>stijgt de inwendige potentiële energie</strong>. Hun "
                  "gemiddelde snelheid, en dus de temperatuur, blijft gelijk: "
                  "<strong>ijs van 0 °C blijft 0 °C terwijl het smelt</strong>."),
            ("p", "Daarom voelt <strong>verdampende alcohol op je hand koud aan</strong>: de alcohol "
                  "<strong>neemt warmte van je hand om te verdampen</strong>. Zweten werkt op dezelfde "
                  "manier."),
            ("kader", "<strong>Verdampen kost veel méér dan opwarmen.</strong> 1 kg water van 0 naar "
                      "100 °C brengen kost ongeveer 419 kJ; datzelfde water laten verdampen ongeveer "
                      "2260 kJ. En <strong>water verdampt niet enkel bij 100 °C</strong>: aan het "
                      "oppervlak gebeurt dat bij elke temperatuur, zoals natte was die droogt. Bij "
                      "100 °C, het <strong>kookpunt</strong>, begint het ook van binnenuit te "
                      "verdampen."),
            ("p", "Naast het kookpunt zijn er het <strong>smeltpunt</strong> en het "
                  "<strong>sublimatiepunt</strong>. Bij <strong>normale luchtdruk ligt het kookpunt van "
                  "water op 100 °C</strong> en zijn smeltpunt op 0 °C."),
            ("weetje", "Een warmtepomp gebruikt net deze twee faseovergangen: een vloeistof verdampt "
                       "buiten en neemt daar warmte op, en condenseert binnen en geeft die daar weer af."),
        ]),
    ],
    onthoud=[
        "Temperatuur hoort bij de gemiddelde kinetische energie van de deeltjes; warmte is overgedragen energie.",
        "Warmte stroomt van warm naar koud en stopt bij het thermisch evenwicht.",
        "Geleiding in vaste stoffen, convectie in vloeistoffen en gassen, straling ook zonder stof.",
        "Q = c . m . ΔT voor een stof, Q = C . ΔT voor een voorwerp; c van water is 4186 J/(kg.K).",
        "Een grote c betekent traag opwarmen, een kleine c snel.",
        "Q = l . m voor een faseovergang; tijdens die overgang blijft de temperatuur gelijk.",
        "Smelten, verdampen en sublimeren vragen warmte; stollen, condenseren en desublimeren geven ze af.",
        "De specifieke smeltwarmte en stolwarmte van een stof zijn dezelfde waarde.",
        "Water verdampt bij elke temperatuur aan het oppervlak; bij 100 °C begint het te koken.",
    ],
)

# ───────────────────── 10. Elektrische stroom, spanning en weerstand
BUNDELS["elektrische-stroom-spanning-en-weerstand-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Elektrische stroom, spanning en weerstand",
    onder="De wet van Ohm, geleiders en isolatoren, meten met een multimeter, het vermogen en het joule-effect, serie- en parallelschakelingen en de veiligheid.",
    secties=[
        dict(kop="De grootheden en de wet van Ohm", blokken=[
            ("p", tabel(["Grootheid", "Symbool", "Eenheid", "Meetinstrument"], [
                ["elektrische lading", "Q", "coulomb (C)", "—"],
                ["stroomsterkte", "I", "ampère (A)", "ampèremeter"],
                ["spanning", "U", "volt (V)", "voltmeter"],
                ["weerstand", "R", "ohm (Ω)", "ohmmeter"],
                ["vermogen", "P", "watt (W)", "—"],
            ])),
            ("p", "De <strong>wet van Ohm</strong> is <strong>R = U / I</strong>, of in de andere "
                  "vormen <strong>U = R . I</strong> en <strong>I = U / R</strong>."),
            ("p", tabel(["Opgave", "Rekenwerk", "Antwoord"], [
                ["230 V en 0,50 A", "230 / 0,50", "R = 460 Ω"],
                ["5,0 V over 25 Ω", "5,0 / 25", "I = 0,20 A"],
                ["40 Ω met 0,20 A", "40 . 0,20", "U = 8,0 V"],
            ])),
            ("p", "<strong>Bij een vaste weerstand zijn U en I recht evenredig</strong>: een dubbele "
                  "spanning geeft een dubbele stroom, en in een grafiek krijg je een rechte door de "
                  "oorsprong. <strong>Bij een vaste spanning zijn I en R omgekeerd evenredig</strong>: "
                  "een dubbele weerstand geeft de helft van de stroom."),
            ("p", "Een <strong>geleider heeft een kleine weerstand, een isolator een grote</strong>. "
                  "Bij dezelfde spanning loopt er door een geleider dus veel stroom en door een "
                  "isolator bijna geen. Daarom zit er rubber om een koperdraad. De "
                  "<strong>geleidbaarheid is omgekeerd aan de weerstand</strong>: een grote "
                  "geleidbaarheid hoort bij een kleine weerstand."),
            ("p", "De <strong>conventionele stroomzin</strong> loopt <strong>van de plus- naar de "
                  "minpool buiten de bron</strong>. De <strong>elektronen bewegen in werkelijkheid net "
                  "de andere kant op</strong>, van min naar plus. Die afspraak is ouder dan de kennis "
                  "over elektronen, en men heeft ze behouden."),
        ]),
        dict(kop="Meten en vermogen", blokken=[
            ("p", "Een <strong>ampèremeter sluit je in serie aan</strong> met het onderdeel, want de "
                  "stroom moet erdoor lopen. Een <strong>voltmeter sluit je parallel aan</strong>, dus "
                  "over het onderdeel heen."),
            ("kader", "<strong>Zet een ampèremeter nooit rechtstreeks over de polen van een "
                      "bron.</strong> Hij heeft een heel kleine weerstand, dus maak je zo een "
                      "kortsluiting: de stroom wordt enorm en het toestel gaat stuk."),
            ("p", "Een <strong>multimeter</strong> kan spanning, stroomsterkte en weerstand meten. Je "
                  "kiest met een draaiknop: <strong>DCV voor gelijkspanning</strong>, "
                  "<strong>DCA voor gelijkstroom</strong> en de <strong>Ω-stand voor een "
                  "weerstand</strong>. De afkorting <strong>DC</strong> staat voor gelijkspanning of "
                  "gelijkstroom."),
            ("p", "In een <strong>elektrisch schema</strong> staan de onderdelen met hun eigen symbool: "
                  "een (regelbare) gelijkspanningsbron, een (regelbare) weerstand, een lamp, een "
                  "schakelaar, een ampèremeter en een voltmeter."),
            ("p", "Het <strong>elektrisch vermogen</strong> is <strong>P = U . I</strong>, en net als "
                  "elk vermogen ook <strong>P = |ΔE| / Δt</strong>. Een toestel op 230 V dat 2,0 A "
                  "trekt, heeft een vermogen van <strong>460 W</strong>. Doen twee toestellen hetzelfde "
                  "werk, dan is <strong>het zuinigste dat met het kleinste vermogen</strong>."),
            ("p", "Het <strong>joule-effect</strong> is het <strong>opwarmen van een weerstand door de "
                  "stroom erdoor</strong>: de elektronen botsen op de deeltjes van de draad en geven "
                  "hun energie als warmte door. In een waterkoker is dat gewenst, in een kabel niet."),
        ]),
        dict(kop="Serie en parallel", blokken=[
            ("p", tabel(["", "Serieschakeling", "Parallelschakeling"], [
                ["stroomsterkte", "I = I₁ = I₂ = …", "I = I₁ + I₂ + …"],
                ["spanning", "U = U₁ + U₂ + …", "U = U₁ = U₂ = …"],
                ["substitutieweerstand", "Rs = R₁ + R₂ + …", "Rs = (1/R₁ + 1/R₂ + …)⁻¹"],
            ])),
            ("p", "In een <strong>serieschakeling is er maar één weg</strong>, dus loopt overal "
                  "<strong>dezelfde stroom</strong> en <strong>verdeelt de spanning zich</strong>. De "
                  "<strong>som van de spanningen over de onderdelen is de bronspanning</strong>, en "
                  "over de grootste weerstand staat de grootste spanning."),
            ("p", "In een <strong>parallelschakeling hangt elke tak tussen dezelfde twee punten</strong>, "
                  "dus staat er over elke tak <strong>dezelfde spanning</strong> en "
                  "<strong>verdeelt de stroom zich</strong>."),
            ("p", tabel(["Opgave", "Rekenwerk", "Rs"], [
                ["30 Ω en 60 Ω in serie", "30 + 60", "90 Ω"],
                ["50 Ω en 50 Ω in serie", "50 + 50", "100 Ω"],
                ["30 Ω en 60 Ω parallel", "(1/30 + 1/60)⁻¹", "20 Ω"],
                ["50 Ω en 50 Ω parallel", "50 / 2", "25 Ω"],
                ["drie keer 60 Ω parallel", "60 / 3", "20 Ω"],
                ["10 Ω in serie met twee keer 20 Ω parallel", "10 + 10", "20 Ω"],
            ])),
            ("p", "Bij <strong>gelijke weerstanden parallel deel je door hun aantal</strong>. De "
                  "<strong>substitutieweerstand van een parallelschakeling is altijd kleiner dan de "
                  "kleinste</strong> van de weerstanden, want elke extra tak geeft de stroom een weg "
                  "bij. Enkel bij serie wordt de totale weerstand groter."),
            ("p", "Een <strong>gemengde schakeling</strong> werk je <strong>van binnen naar buiten "
                  "uit</strong>: eerst de parallelle groep tot één weerstand, dan die in serie met de "
                  "rest. Over een serieschakeling van 20 Ω en 40 Ω met 12 V loopt I = 12 / 60 = "
                  "<strong>0,20 A</strong>, en over de 40 Ω staat dan U = 40 . 0,20 = "
                  "<strong>8,0 V</strong>; over de 20 Ω staat 4,0 V, samen weer 12 V."),
            ("p", "Een <strong>kerstboomsnoer in serie gaat helemaal uit als één lampje stuk is</strong>: "
                  "de <strong>kring is onderbroken, dus loopt er nergens stroom</strong>. "
                  "<strong>Parallel geschakelde lampjes blijven wel branden</strong>: elke lamp krijgt "
                  "de volle spanning van de bron en trekt even veel stroom als alleen. Daarom staan de "
                  "<strong>stopcontacten in een huis parallel</strong>, zodat op elk ervan 230 V staat."),
        ]),
        dict(kop="Risico's en veiligheid", blokken=[
            ("p", tabel(["Risico", "Wat er gebeurt"], [
                ["kortsluiting", "R wordt heel klein, dus I heel groot"],
                ["overbelasting", "te veel toestellen op één kring"],
                ["brandgevaar", "de draden worden heet door het joule-effect"],
                ["elektrocutie", "stroom door het lichaam van een mens"],
            ])),
            ("p", "Bij een <strong>kortsluiting is de weerstand in de kring heel klein "
                  "geworden</strong>, dus <strong>wordt de stroomsterkte heel groot</strong> volgens "
                  "I = U / R. De spanning van de bron verandert daar niet door. Door het joule-effect "
                  "worden de draden dan snel heet, met <strong>brandgevaar</strong>."),
            ("p", tabel(["Veiligheidsaspect", "Wat het doet"], [
                ["aarding en aarddraad", "leidt stroom op een metalen kast naar de aarde"],
                ["automatische zekering", "legt de kring af bij een te grote stroom"],
                ["smeltveiligheid", "een draad die doorsmelt bij te veel stroom"],
                ["verliesstroomschakelaar", "legt af als er stroom wegloopt die niet terugkomt"],
                ["elektrische isolatie, dubbele isolatie", "houdt de stroom in de draad"],
                ["veiligheidsspanning", "een spanning die laag genoeg is om geen gevaar te zijn"],
            ])),
            ("p", "Een <strong>aarddraad leidt een stroom die op de metalen kast van een toestel komt "
                  "veilig naar de aarde</strong>, zodat die niet door de persoon gaat die de kast "
                  "aanraakt. Een <strong>automatische zekering beschermt tegen een te grote "
                  "stroom</strong>; een <strong>verliesstroomschakelaar merkt dat er stroom wegloopt "
                  "die niet terugkomt</strong>, bijvoorbeeld door een mens, en legt de kring af. Dat "
                  "zijn dus twee verschillende dingen."),
            ("kader", "<strong>Nooit een elektrisch toestel met natte handen bedienen.</strong> Water "
                      "verlaagt de weerstand van je huid sterk, dus loopt er bij dezelfde spanning veel "
                      "meer stroom door je lichaam. Ook onder 230 V blijft dat gevaarlijk."),
            ("weetje", "Een verliesstroomschakelaar in een woning slaat af bij een verschil van "
                       "ongeveer 30 milliampère tussen de stroom die gaat en de stroom die terugkomt. "
                       "Dat is minder dan wat een spaarlamp trekt."),
        ]),
    ],
    onthoud=[
        "R = U / I; bij vaste R zijn U en I recht evenredig, bij vaste U zijn I en R omgekeerd evenredig.",
        "Een geleider heeft een kleine weerstand, een isolator een grote; geleidbaarheid is omgekeerd aan weerstand.",
        "De conventionele stroomzin gaat van plus naar min; de elektronen bewegen de andere kant op.",
        "Ampèremeter in serie, voltmeter parallel; DCV voor gelijkspanning, DCA voor gelijkstroom.",
        "P = U . I, en het joule-effect warmt een weerstand op: gewenst in een waterkoker, niet in een kabel.",
        "Serie: dezelfde I, de spanningen tellen op, Rs = R₁ + R₂.",
        "Parallel: dezelfde U, de stromen tellen op, Rs kleiner dan de kleinste weerstand.",
        "Een gemengde schakeling werk je van binnen naar buiten uit.",
        "Zekering tegen te veel stroom, verliesstroomschakelaar tegen stroom die wegloopt, aarddraad naar de aarde.",
    ],
)

# ───────────────────── 11. Licht: weerkaatsing, breking en lenzen
BUNDELS["licht-weerkaatsing-breking-en-lenzen-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Licht: weerkaatsing, breking en lenzen",
    onder="Het stralenmodel, de terugkaatsingswetten, de vlakke spiegel, schaduwvorming, de breking tussen twee middenstoffen en het beeld bij een dunne bolle lens.",
    secties=[
        dict(kop="Het stralenmodel", blokken=[
            ("p", "Licht <strong>plant zich in een doorzichtige stof rechtlijnig voort</strong>. "
                  "Daarom kan je <strong>een lichtstraal grafisch voorstellen "
                  "als een rechte met een pijl erop</strong>: de "
                  "rechte toont de weg, de pijl de <strong>voortplantingszin</strong>. Pas aan een "
                  "grensvlak met een andere stof verandert de richting."),
            ("p", tabel(["Soort voorwerp", "Wat het met licht doet", "Voorbeeld"], [
                ["ondoorschijnend", "laat geen licht door", "een plank"],
                ["doorschijnend", "laat licht door, maar niet scherp", "matglas"],
                ["doorzichtig", "laat licht scherp door", "helder glas"],
            ])),
            ("p", "Een <strong>ondoorschijnend voorwerp laat dus geen licht door</strong>, ook geen "
                  "beetje: een voorwerp dat wat licht doorlaat zonder scherp beeld, is "
                  "<strong>doorschijnend</strong>."),
            ("p", "De <strong>stralengang is omkeerbaar</strong>, en die "
                  "<strong>omkeerbaarheid</strong> betekent dat <strong>licht dezelfde weg "
                  "terug volgt als je de zin omkeert</strong>. Dat <strong>geldt bij weerkaatsing en bij "
                  "breking</strong>, en ook bij een lens, niet enkel bij een vlakke spiegel."),
        ]),
        dict(kop="Weerkaatsing", blokken=[
            ("p", "Bij een weerkaatsing duid je op de tekening aan: de "
                  "<strong>invallende straal</strong>, het <strong>invalspunt</strong>, de "
                  "<strong>normaal</strong>, de <strong>invalshoek</strong>, de "
                  "<strong>weerkaatsingshoek</strong> en de <strong>weerkaatste straal</strong>."),
            ("p", "Het <strong>invalspunt</strong> is <strong>het punt waar de invallende straal het "
                  "spiegeloppervlak raakt</strong>. De <strong>normaal</strong> is de "
                  "<strong>lijn loodrecht op het oppervlak in dat invalspunt</strong>."),
            ("kader", "<strong>De hoeken meet je ten opzichte van de normaal, niet ten opzichte van "
                      "de spiegel.</strong> Valt een straal onder 20° met de spiegel in, dan is zijn "
                      "invalshoek 70°."),
            ("p", "De <strong>eerste terugkaatsingswet</strong> zegt dat de invallende straal, de "
                  "weerkaatste straal en de normaal in <strong>hetzelfde vlak</strong> liggen. De "
                  "<strong>tweede terugkaatsingswet</strong> zegt dat de "
                  "<strong>invalshoek gelijk is aan de weerkaatsingshoek</strong>. Valt een straal "
                  "onder <strong>35°</strong> in, dan kaatst hij onder <strong>35°</strong> terug."),
            ("p", "Bij een <strong>regelmatige weerkaatsing is het oppervlak glad en vlak</strong>, "
                  "zoals een spiegel of stil water: de stralen blijven netjes samen. Bij een "
                  "<strong>diffuse weerkaatsing</strong> is het oppervlak <strong>onregelmatig</strong> "
                  "en kaatst elke straal een andere kant op. De wet geldt ook daar in elk punt, maar "
                  "er komt geen beeld tot stand: <strong>in een ruw vel papier zie je je spiegelbeeld "
                  "dus niet</strong>, al zie je het papier zelf wel."),
            ("p", tabel(["Kenmerk van het beeld bij een vlakke spiegel", "Welk"], [
                ["aard", "virtueel"],
                ["stand", "rechtopstaand"],
                ["grootte", "even groot als het voorwerp"],
                ["beeldafstand", "even ver achter de spiegel als het voorwerp ervoor staat"],
            ])),
            ("p", "Een <strong>virtueel beeld is een beeld dat je niet op een scherm kan "
                  "opvangen</strong>: de stralen komen er niet echt samen, ze lijken er enkel uit te "
                  "komen. Een <strong>reëel beeld vang je wel op</strong>, zoals het beeld van een "
                  "projector. Sta je <strong>1 m voor een spiegel</strong>, dan lijkt je beeld 1 m "
                  "erachter, dus 2 m van jou. Het <strong>gezichtsveld</strong> van een vlakke spiegel "
                  "is het gebied dat je er door kan zien; je bepaalt het met de stralen vanuit je oog "
                  "langs de twee randen van de spiegel."),
        ]),
        dict(kop="Schaduwvorming", blokken=[
            ("p", "Omdat licht rechtlijnig gaat, werpt een ondoorschijnend voorwerp een "
                  "<strong>schaduw</strong>. De <strong>kernschaduw is het donkerste deel</strong>: daar "
                  "<strong>komt helemaal geen licht van de bron</strong>, in de <strong>bijschaduw komt licht van een deel van de bron</strong>, "
                  "dus is het daar minder donker."),
            ("p", "Een <strong>kleine lichtbron geeft een scherpere schaduw</strong>: bij een puntbron "
                  "is er bijna geen bijschaduw. Een grote bron, zoals een tl-balk, geeft een brede "
                  "bijschaduw en dus een vage rand."),
            ("p", tabel(["Verduistering", "Wat staat ertussen"], [
                ["zonsverduistering", "de maan tussen de zon en de aarde"],
                ["maansverduistering", "de aarde tussen de zon en de maan"],
            ])),
            ("p", "Bij een <strong>zonsverduistering werpt de maan haar schaduw op de aarde</strong>. "
                  "Wie in de kernschaduw staat, ziet de zon helemaal verdwijnen; wie in de bijschaduw "
                  "staat, ziet er een stuk van."),
        ]),
        dict(kop="Breking", blokken=[
            ("p", "Gaat een lichtstraal <strong>schuin van de ene middenstof naar de andere</strong>, dan "
                  "<strong>breekt</strong> hij: hij verandert van richting. Dat is "
                  "<strong>breking</strong>. Je duidt aan: de "
                  "invallende straal, het invalspunt, de <strong>invalshoek</strong>, de "
                  "<strong>brekingshoek</strong>, de normaal en de <strong>gebroken straal</strong>. "
                  "De <strong>brekingshoek is de hoek tussen de gebroken straal en de normaal</strong>."),
            ("p", "De <strong>eerste brekingswet</strong> zegt dat de invallende straal, de gebroken "
                  "straal en de normaal <strong>in hetzelfde vlak</strong> liggen."),
            ("p", tabel(["Overgang", "Hoe de straal buigt", "De hoek"], [
                ["van optisch ijl naar dicht (lucht naar water)", "naar de normaal toe", "wordt kleiner"],
                ["van optisch dicht naar ijl (glas naar lucht)", "van de normaal weg", "wordt groter"],
                ["loodrecht op het grensvlak", "rechtdoor, zonder te breken", "blijft 0°"],
            ])),
            ("p", "Een <strong>optisch dichtere stof buigt een straal naar de normaal toe</strong>. "
                  "Valt een straal <strong>loodrecht op het grensvlak</strong>, dan "
                  "<strong>gaat hij rechtdoor</strong>: hij ligt al langs de normaal, dus is er niets "
                  "om naartoe of weg te buigen. Uit een gegeven constructie kan je zo "
                  "<strong>afleiden welke stof optisch dicht is en welke optisch ijl</strong>."),
            ("p", "Daarom lijkt een <strong>stok die schuin in het water staat geknikt</strong>: de "
                  "stralen van het ondergedompelde deel veranderen van richting aan het "
                  "<strong>wateroppervlak</strong>, en "
                  "je oog trekt die stralen rechtdoor door."),
            ("p", "Om dezelfde reden lijkt de <strong>bodem van een zwembad minder diep</strong> dan "
                  "hij is. Dat is de <strong>schijnbare verhoging</strong>: bij het verlaten van het "
                  "water <strong>buigen de stralen van de normaal weg</strong>, en je oog volgt ze "
                  "rechtdoor tot op een punt hoger dan de echte bodem."),
        ]),
        dict(kop="De dunne bolle lens", blokken=[
            ("p", "Een <strong>bolle lens is in het midden dikker dan aan de rand</strong>. Daardoor "
                  "buigt ze de stralen naar elkaar toe. De lijn loodrecht door de lens heet de "
                  "<strong>optische as</strong>; die <strong>gaat door het optisch middelpunt</strong>, "
                  "door de twee <strong>brandpunten F</strong> en door de "
                  "<strong>krommingsmiddelpunten</strong>, elk op een afstand gelijk aan de "
                  "<strong>kromtestraal</strong>."),
            ("p", "Het <strong>brandpunt F</strong> is <strong>het punt waar stralen die parallel met "
                  "de optische as invallen, na de lens samenkomen</strong>. De afstand van de lens tot "
                  "F heet de <strong>brandpuntsafstand</strong>. Een dunne bolle lens heeft "
                  "<strong>twee brandpunten</strong>, één aan elke kant, even ver van de lens."),
            ("p", tabel(["Kenmerkende straal", "Wat ze na de lens doet"], [
                ["parallel met de optische as", "gaat door het brandpunt"],
                ["door het optisch middelpunt", "gaat rechtdoor"],
                ["door het brandpunt vóór de lens", "gaat parallel met de optische as verder"],
            ])),
            ("p", "Met twee van die drie stralen construeer je het <strong>beeld</strong>."),
            ("p", tabel(["Waar het voorwerp staat", "Aard", "Stand", "Grootte", "Toepassing"], [
                ["verder dan 2 x de brandpuntsafstand", "reëel", "omgekeerd", "kleiner", "fototoestel"],
                ["tussen de lens en het brandpunt", "virtueel", "rechtopstaand", "groter", "loep"],
            ])),
            ("p", "Een <strong>bolle lens maakt dus niet enkel reële beelden</strong>: staat het "
                  "voorwerp binnen de brandpuntsafstand, dan is het beeld virtueel, rechtopstaand en "
                  "groter. Dat is net wat een loep doet."),
            ("p", "De <strong>vergrotingsfactor</strong> is de <strong>verhouding van de beeldgrootte "
                  "tot de voorwerpsgrootte</strong>, en die is even groot als de verhouding van de "
                  "<strong>beeldafstand tot de voorwerpsafstand</strong>. Dat volgt uit de "
                  "<strong>gelijkvormigheid van de driehoeken</strong> in de constructie. Is een beeld "
                  "<strong>drie keer zo groot</strong> als het voorwerp, dan is de vergrotingsfactor "
                  "<strong>3</strong>."),
            ("kader", "<strong>Hoe verder het voorwerp, hoe dichter het beeld bij het "
                      "brandpunt.</strong> Een voorwerp heel ver weg geeft een beeld precies in het "
                      "brandpunt. Een voorwerp dat verder weg staat, hoort dus niet bij een beeld dat "
                      "verder van de lens ligt, maar net omgekeerd."),
            ("weetje", "Een loep werkt enkel als je ze dicht genoeg bij het voorwerp houdt. Hou je "
                       "ze verder dan haar brandpuntsafstand, dan springt het beeld om en zie je alles "
                       "op zijn kop."),
        ]),
    ],
    onthoud=[
        "Licht gaat rechtlijnig; je tekent een straal als een rechte met een pijl.",
        "Ondoorschijnend laat geen licht door, doorschijnend wel maar niet scherp, doorzichtig scherp.",
        "De invalshoek is gelijk aan de weerkaatsingshoek, allebei gemeten ten opzichte van de normaal.",
        "Regelmatige weerkaatsing op een glad vlak oppervlak, diffuse weerkaatsing op een ruw oppervlak.",
        "Het beeld in een vlakke spiegel is virtueel, rechtopstaand, even groot en even ver erachter.",
        "In de kernschaduw komt geen licht van de bron, in de bijschaduw een deel.",
        "Van ijl naar dicht buigt een straal naar de normaal toe, van dicht naar ijl ervan weg.",
        "Een bolle lens: parallel met de as gaat door F, door het optisch middelpunt gaat rechtdoor.",
        "Ver van de lens: reëel, omgekeerd, kleiner. Binnen het brandpunt: virtueel, rechtopstaand, groter.",
    ],
)

# ───────────────────── 12. Veilig werken, meten en onderzoek
BUNDELS["veilig-werken-meten-en-onderzoek-fysica-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Veilig werken, meten en onderzoek",
    onder="Veilig en duurzaam werken, een meetinstrument kiezen en aflezen, de stappen van het wetenschappelijk onderzoek, de criteria voor een onderzoeksvraag en STEM.",
    secties=[
        dict(kop="Veilig en duurzaam werken", blokken=[
            ("p", "Tijdens een onderzoek werk je <strong>veilig en duurzaam</strong>. Op het examen "
                  "voer je die handelingen niet uit, maar <strong>leg je uit waarom</strong> iets een "
                  "goede of een slechte werkwijze is."),
            ("p", tabel(["Goede werkwijze", "Waarom"], [
                ["het meetbereik respecteren", "anders loopt het instrument over of gaat het stuk"],
                ["een instrument uitschakelen als je niet meet", "spaart de batterij, voorkomt schade"],
                ["geen natte handen bij elektrische toestellen", "water verlaagt de weerstand van je huid"],
                ["de handleiding en het onderhoudsvoorschrift lezen", "daar staan de grenzen en de volgorde in"],
                ["afval volgens het etiket verwerken", "niet alles mag in de gootsteen"],
            ])),
            ("p", "<strong>Water verlaagt de weerstand van je huid</strong> sterk, dus loopt er bij "
                  "dezelfde spanning veel meer stroom door je lichaam. Dat is net wat elektrocutie "
                  "gevaarlijk maakt."),
            ("p", "<strong>Een instrument dat aan blijft staan als je niet meet</strong>, verbruikt "
                  "zijn batterij en kan warm worden, en een multimeter op de verkeerde stand kan stuk "
                  "gaan. Een <strong>onderhoudsvoorschrift hoort bij veilig en duurzaam werken</strong>: "
                  "een goed onderhouden toestel meet betrouwbaarder en gaat langer mee. Ook een "
                  "<strong>werktekening of een handleiding juist kunnen lezen</strong> hoort daarbij, "
                  "want daar staat in welke grenzen het systeem aankan."),
            ("p", "<strong>De restvloeistof van een proef mag je niet altijd in de gootsteen "
                  "gieten.</strong> Dat hangt van de stof af, en wat op het etiket of in de handleiding "
                  "staat, bepaalt waar het afval naartoe moet."),
            ("p", "Op een <strong>dynamometer staat een maximale waarde</strong> omdat een "
                  "<strong>grotere kracht de veer blijvend uitrekt</strong>. De veer werkt enkel binnen "
                  "haar elastisch gebied; daarbuiten komt ze niet meer op haar oude lengte terug en "
                  "klopt de schaal niet meer."),
        ]),
        dict(kop="Meten en aflezen", blokken=[
            ("p", "Je kiest een instrument op <strong>twee</strong> dingen: eerst op "
                  "<strong>meetbereik</strong>, dan op <strong>nauwkeurigheid</strong>. Het "
                  "<strong>meetbereik is de grootste waarde die het instrument kan meten</strong>, en "
                  "<strong>meten boven het meetbereik kan het beschadigen</strong>. De nauwkeurigheid "
                  "zegt hoe fijn je kan aflezen; dat is <strong>niet hetzelfde als het "
                  "meetbereik</strong>, en een <strong>groter meetbereik gaat meestal juist samen met "
                  "grovere streepjes</strong>."),
            ("kader", "<strong>Een instrument met fijnere streepjes is niet altijd de beste "
                      "keuze.</strong> Past de waarde niet binnen het meetbereik, dan kan je er niets "
                      "mee meten of ga je het beschadigen."),
            ("p", "Meet je een <strong>stroom die mogelijk 2 A groot is met een multimeter</strong>, "
                  "dan <strong>kies je eerst het grootste meetbereik en verfijn je daarna</strong>. Op "
                  "een te klein bereik kan het instrument overbelast raken. Voor een "
                  "<strong>tijdsduur van ongeveer 2 s</strong> neem je een "
                  "<strong>chronometer tot op een honderdste seconde</strong>: met een klok die enkel "
                  "seconden toont, zou je meetfout even groot zijn als de helft van je meting."),
            ("p", "Je leest een <strong>maatcilinder op ooghoogte</strong> af, want "
                  "<strong>anders kijk je er schuin op en lees je verkeerd af</strong>. Die afleesfout "
                  "heet een <strong>parallaxfout</strong>. Het peil lees je af "
                  "<strong>onderaan de holle kromming van het oppervlak</strong>, en die kromming heet "
                  "de <strong>meniscus</strong>."),
            ("p", "<strong>Herhaal een meting en neem het gemiddelde.</strong> Zo verklein je de "
                  "invloed van toevallige afleesfouten. Een waarde die er helemaal naast ligt, mag je "
                  "wel apart bekijken."),
            ("p", "Bij een meetresultaat hoort <strong>altijd een eenheid</strong>, want "
                  "<strong>zonder eenheid weet je niet wat het getal betekent</strong>: een 5 kan 5 m, "
                  "5 kg of 5 s zijn. Zonder eenheid kan je twee metingen niet vergelijken en niet "
                  "verder rekenen."),
            ("p", "Welk instrument waarvoor: een <strong>thermometer</strong> voor een "
                  "<strong>temperatuur</strong> (laat hem lang genoeg zitten tot hij in thermisch "
                  "evenwicht is), een <strong>balans</strong> voor een massa, een "
                  "<strong>dynamometer</strong> voor een kracht, een <strong>maatcilinder</strong> voor "
                  "een volume, een <strong>manometer of barometer</strong> voor een druk, een "
                  "<strong>chronometer</strong> voor een tijd, een <strong>meetlint</strong> voor een "
                  "lengte en een <strong>multimeter</strong> voor spanning, stroomsterkte of weerstand."),
        ]),
        dict(kop="De stappen van een onderzoek", blokken=[
            ("p", tabel(["Stap", "Wat je doet"], [
                ["1", "de probleemstelling definiëren en afbakenen"],
                ["2", "een onderzoeksvraag opstellen en een hypothese formuleren"],
                ["3", "een onderzoeksplan opstellen"],
                ["4", "data waarnemen en verzamelen"],
                ["5", "de data analyseren, ook grafisch"],
                ["6", "conclusies trekken op basis van die data"],
                ["7", "de conclusie als antwoord op de onderzoeksvraag formuleren"],
                ["8", "over de methode en de resultaten reflecteren en communiceren"],
            ])),
            ("p", "<strong>De eerste stap is de probleemstelling definiëren en afbakenen.</strong> Pas "
                  "als je weet wat je precies wil onderzoeken, kan je een vraag en een plan maken; "
                  "zonder afbakening wordt het onderzoek te breed."),
            ("p", "Een <strong>hypothese</strong> is een <strong>voorlopig antwoord dat je gaat "
                  "nakijken</strong>. Ze <strong>mag ook fout blijken</strong>: een "
                  "<strong>verworpen hypothese maakt je onderzoek niet waardeloos</strong>, want je "
                  "weet nu dat het anders werkt. Je hypothese achteraf aanpassen mag juist niet."),
            ("p", "In een <strong>onderzoeksplan</strong> staat wat je gaat meten, waarmee, en "
                  "<strong>wat je gelijk houdt</strong>. Onderzoek je <strong>hoe snel water afkoelt in "
                  "verschillende bekers</strong>, dan houd je de <strong>begintemperatuur en de "
                  "hoeveelheid water gelijk</strong>: enkel wat je onderzoekt mag verschillen, hier het "
                  "soort beker."),
            ("p", "Bij het <strong>analyseren mag je geen metingen weglaten</strong> die niet in je "
                  "hypothese passen: dan stuur je je eigen resultaat. Een afwijkende meting noteer je "
                  "en je zoekt uit waar ze vandaan komt."),
            ("p", "Een <strong>conclusie geeft antwoord op de onderzoeksvraag</strong> en baseert zich "
                  "op je data. Nieuwe beweringen zonder data horen er niet in. "
                  "<strong>Reflecteren over je methode</strong> hoort erbij, want "
                  "<strong>zo zie je welke meetfouten je resultaat verklaren</strong> en hoe iemand "
                  "anders het beter kan doen."),
            ("p", "Een <strong>grafiek is een gepast model</strong> om een verband tussen twee gemeten "
                  "grootheden te laten zien: uit de vorm lees je af of het verband "
                  "<strong>recht evenredig, lineair, omgekeerd evenredig of kwadratisch</strong> is. "
                  "Een <strong>tabel, een schets of een formule</strong> kan ook, afhankelijk van wat "
                  "je wil tonen."),
        ]),
        dict(kop="De criteria voor een onderzoeksvraag", blokken=[
            ("p", tabel(["Criterium", "Dat wil zeggen"], [
                ["open", "de vraag is een open vraag, geen ja-of-nee-vraag"],
                ["enkelvoudig", "de vraag gaat over één onderwerp, één probleem"],
                ["objectief", "de vraag toont geen mening of overtuiging"],
                ["haalbaar", "het onderzoek is uitvoerbaar met genoeg tijd en middelen"],
                ["onderzoekbaar", "het is geen opzoekvraag en niet direct oplosbaar"],
                ["relevant", "het antwoord draagt bij aan bestaande kennis"],
            ])),
            ("p", "<strong>Enkelvoudig</strong> betekent dat de vraag over <strong>één onderwerp "
                  "gaat</strong>: zitten er twee in, dan weet je bij het antwoord niet meer waarover "
                  "het gaat. <strong>Objectief</strong> betekent dat de vraag "
                  "<strong>geen mening of overtuiging toont</strong>: \"Waarom is zonne-energie de "
                  "beste keuze?\" zit al vol overtuiging, \"Hoeveel energie levert een zonnepaneel per "
                  "maand?\" niet."),
            ("p", "<strong>Haalbaar</strong> betekent <strong>uitvoerbaar met genoeg tijd en "
                  "middelen</strong>: de temperatuur in de kern van de zon kan je niet zelf meten, de "
                  "afkoeling van water in een thermos wel. <strong>Onderzoekbaar</strong> betekent dat "
                  "het <strong>geen opzoekvraag mag zijn</strong>: kan je het antwoord gewoon in een "
                  "boek vinden, dan is er geen onderzoek nodig."),
            ("p", "<strong>Hoe spannend of hoe kort een vraag is, telt niet mee.</strong> Een vraag "
                  "waarop je enkel ja of nee kan antwoorden, heet een <strong>gesloten vraag</strong>, "
                  "en die voldoet dus niet aan het eerste criterium. Een goede vraag is bijvoorbeeld: "
                  "\"Hoe hangt de valtijd af van het aantal filters?\""),
            ("p", "De zes criteria uit de linkerkolom van die tabel krijg je ook op het examen."),
        ]),
        dict(kop="Een oplossing ontwerpen en STEM", blokken=[
            ("p", "<strong>STEM</strong> staat voor <strong>Science, Technology, Engineering en "
                  "Mathematics</strong>, in het Nederlands <strong>wetenschappen, technologie, "
                  "ingenieurswetenschappen en wiskunde</strong>. De <strong>M staat dus voor "
                  "wiskunde</strong>. Een STEM-probleem pak je vanuit die vier disciplines samen aan."),
            ("p", tabel(["Stap bij het ontwerpen", "Wat je doet"], [
                ["1", "het probleem definiëren"],
                ["2", "criteria geven waaraan de oplossing moet voldoen"],
                ["3", "het probleem indien nodig in deelproblemen splitsen"],
                ["4", "oplossingen bedenken en in een totaaloplossing integreren"],
                ["5", "de oplossing evalueren en indien nodig bijsturen"],
            ])),
            ("p", "<strong>Criteria opstellen en het probleem in deelproblemen splitsen</strong> horen "
                  "er dus bij; <strong>de eerste ingeving meteen uitvoeren</strong> niet, en "
                  "<strong>achteraf bijsturen hoort er wel bij</strong>."),
            ("p", "De <strong>STEM-disciplines werken samen met de maatschappij</strong>. Tijdens de "
                  "coronacrisis was <strong>wetenschappelijke kennis</strong> nodig voor een vaccin, "
                  "<strong>technologische kennis</strong> om het te maken en koel te houden, en "
                  "<strong>wiskundige kennis</strong> om de verspreiding van het virus in kaart te "
                  "brengen."),
            ("weetje", "Een onderzoeksvraag die aan de zes criteria voldoet, is vaak al half "
                       "opgelost: ze zegt zelf wat je moet meten en wat je gelijk moet houden."),
        ]),
    ],
    onthoud=[
        "Op het examen leg je uit waarom een werkwijze veilig en duurzaam is, je voert ze niet uit.",
        "Respecteer het meetbereik, schakel een instrument uit als je niet meet, en lees de handleiding.",
        "Nooit een elektrisch toestel met natte handen: water verlaagt de weerstand van je huid.",
        "Kies eerst op meetbereik, dan op nauwkeurigheid; begin op het grootste bereik en verfijn.",
        "Lees een maatcilinder op ooghoogte af, onderaan de meniscus, om een parallaxfout te vermijden.",
        "De stappen: probleemstelling, onderzoeksvraag en hypothese, plan, data, analyse, conclusie, reflectie.",
        "Een hypothese is een voorlopig antwoord; verworpen worden is ook een resultaat.",
        "Een onderzoeksvraag is open, enkelvoudig, objectief, haalbaar, onderzoekbaar en relevant.",
        "STEM is wetenschappen, technologie, ingenieurswetenschappen en wiskunde.",
    ],
)

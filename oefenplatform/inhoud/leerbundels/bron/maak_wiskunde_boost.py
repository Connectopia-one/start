# -*- coding: utf-8 -*-
"""De leerbundels en oefenbundels voor wiskunde gevorderd op 🚀 Boost doorstroom.

Gebaseerd op de vakfiche wiskunde gevorderd van de 2de graad
doorstroomfinaliteit, geldig vanaf 1 januari 2027. Die fiche geldt voor
economische wetenschappen, natuurwetenschappen, moderne talen en Latijn.
Humane wetenschappen volgt wiskunde basis, een andere fiche. Daarom is dit een
eigen vak naast het bestaande vak wiskunde van 🌱 Start en ✨ Spark.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim uploadt de bundel
dus twee keer, één keer bij elk deel.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../boost-doorstroom/wiskunde-gevorderd.json`
doet daar het voorwerk voor.

De bundelsleutels eindigen op "-boost-doorstroom", de volledige naam van de
categorie, zodat het uploadscherm en dekking.py ze niet met een gelijknamig
hoofdstuk van ✨ Spark verwarren. De oefenbundels dragen daarbovenop het
voorvoegsel "oefenbundel-".
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel

VAK = "Wiskunde gevorderd"
BOOST = "🚀 Boost doorstroom — 3de en 4de middelbaar"
tabel = bundel.tabel

BUNDELS = {}


# ───────────────────────── 1. Een opgave aanpakken
BUNDELS["een-opgave-aanpakken-van-context-naar-wiskunde-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Een opgave aanpakken: van context naar wiskunde",
    onder="Mathematiseren en demathematiseren, de vier stappen, de heuristieken en de vier vaardigheden van de vakfiche.",
    secties=[
        dict(kop="Van de wereld naar de wiskunde en terug", blokken=[
            ("p", "Een opgave met een verhaal erbij los je op in twee vertalingen. "
                  "<strong>Mathematiseren</strong> is de heenweg: een situatie uit de wereld omzetten in "
                  "<strong>wiskundetaal</strong> en symbolen. <strong>Demathematiseren</strong> is de "
                  "terugweg: je wiskundige uitkomst terugvertalen naar de situatie."),
            ("p", "Reken je uit dat een ladder 4,7 meter lang moet zijn en antwoord je dat een ladder van "
                  "5 meter volstaat, dan ben je aan het demathematiseren: zo'n ladder bestaat in de winkel, "
                  "4,7 meter niet. Je uitkomst betekent pas iets als je ze terugvertaalt."),
            ("kader", "Demathematiseren is <strong>niet</strong> hetzelfde als een opgave vereenvoudigen tot "
                      "je ze aankan. Het is de uitkomst terugvertalen naar het verhaal waar ze vandaan komt."),
        ]),
        dict(kop="Vraagstuk, probleem, met of zonder context", blokken=[
            ("p", "De fiche maakt twee onderscheiden die je moet kennen."),
            ("p", tabel(["Woord", "Wat de fiche ermee bedoelt"], [
                ["vraagstuk", "je lost het op met de leerstof van één hoofdstuk"],
                ["probleem", "je kan het niet aan één hoofdstuk koppelen en combineert leerinhouden"],
                ["met context", "de opgave vertrekt van een situatie uit de wereld"],
                ["zonder context", "de opgave is abstract en zuiver wiskundig"],
                ["meetkundig probleem", "de verzamelnaam voor vraagstukken en problemen waarvoor je meetkundige vaardigheden nodig hebt"],
            ])),
            ("p", "Op het examen komen <strong>allebei</strong> de soorten voor: opgaven met context én "
                  "zuiver wiskundige. Bij een probleem mag en moet je gegevens uit <strong>meerdere "
                  "hoofdstukken</strong> van de fiche combineren; dat is precies wat een probleem van een "
                  "vraagstuk onderscheidt. Bij een meetkundig probleem gaat het om de vaardigheden die je "
                  "nodig hebt, niet om de vorm van de opgave."),
        ]),
        dict(kop="De vier stappen", blokken=[
            ("p", "Om een opgave <strong>procedureel</strong> op te lossen noemt de fiche vier stappen, in "
                  "deze volgorde:"),
            ("p", tabel(["Stap", "Wat je doet", "Waar je op let"], [
                ["1. begrijp het probleem", "ga na wat gegeven is en wat gevraagd wordt",
                 "onderstreep de getallen én hun eenheid"],
                ["2. maak een plan", "kies een onbekende, een tekening, een formule of een schema",
                 "schrijf op waar je letter voor staat"],
                ["3. voer het plan uit", "reken stap voor stap en verantwoord je tussenstappen",
                 "werk netjes, één stap per regel"],
                ["4. reflecteer", "kijk of de uitkomst kan kloppen en of je aanpak elders bruikbaar is",
                 "past het bij de vraag, klopt de eenheid, is het realistisch"],
            ])),
            ("p", "Krijg je een tekening met een ladder tegen een muur, dan is je eerste stap dus "
                  "<strong>niet</strong> rekenen maar nagaan wat gegeven is en wat gevraagd wordt. Wie te "
                  "snel rekent, rekent vaak het verkeerde uit."),
            ("p", "Een goed plan verwijst vaak naar een ander hoofdstuk. Vraagt een opgave de hoogte van een "
                  "<strong>toren</strong> uit de <strong>kijkhoek</strong> en je afstand ertoe, dan is het plan: "
                  "een rechthoekige driehoek tekenen en met de <strong>tangens</strong> werken."),
            ("p", "<strong>Reflecteren hoort bij het oplossen, niet erna.</strong> Een fietser aan 340 "
                  "kilometer per uur, een oppervlakte die <strong>negatief</strong> uitvalt of een vijver van "
                  "0,004 kubieke meter — dat zijn maar vier liter — wijzen alle drie op een rekenfout of op "
                  "eenheden die je door elkaar haalde. Zo'n uitkomst stuurt je terug naar je berekening. Een "
                  "fietser die 24 kilometer in anderhalf uur aflegt, rijdt 24 : 1,5 = <strong>16</strong> "
                  "kilometer per uur; komt daar 36 uit, dan heb je vermenigvuldigd in plaats van gedeeld."),
            ("p", "De fiche vraagt ook dat je je <strong>tussenstappen verantwoordt</strong>: een lezer moet "
                  "kunnen volgen welke eigenschap je toepast en waar het misloopt. Een antwoord zonder "
                  "redenering is niet na te kijken, en jijzelf vindt er je eigen fout niet in terug."),
        ]),
        dict(kop="De heuristieken", blokken=[
            ("p", "Een <strong>heuristiek</strong> is een manier om zélf verder te geraken als je vastzit. De "
                  "fiche geeft er een lijst van, en je mag zelf kiezen welke "
                  "<strong>oplossingsstrategie</strong> je gebruikt, aan de hand van je eigen kennis en "
                  "vaardigheden."),
            ("p", tabel(["Heuristiek", "Wanneer ze helpt", "Voorbeeld"], [
                ["een schets, tekening of tabel maken", "bijna altijd, ook buiten de meetkunde",
                 "de ladder tegen de muur tekenen"],
                ["alle mogelijkheden opschrijven", "bij kleine aantallen",
                 "hoeveel broodjes je kan samenstellen"],
                ["variabelen invoeren", "als je iets niet weet",
                 "de leeftijd van de jongste zus x noemen"],
                ["gebruik maken van symmetrie", "als een helft op de andere lijkt",
                 "een vierkant patroon halveren"],
                ["terugrekenen", "als het eindpunt gegeven is",
                 "48 euro is 80 % van de oude prijs, dus 60 euro"],
                ["opsplitsen in deelproblemen", "bij een grote, vage vraag",
                 "een weekje kamperen: reis, kampeerplaats, eten"],
                ["schatten, slim gissen, testen en controleren", "als geen formule voor de hand ligt",
                 "een getal proberen en bijsturen"],
                ["patronen en regelmaat ontdekken", "bij een rij getallen",
                 "2, 6, 12, 20, 30: de verschillen zijn 4, 6, 8, 10"],
            ])),
            ("p", "Een <strong>schets maken telt als een volwaardige oplossingsstrategie</strong>: het is de "
                  "eerste heuristiek in de lijst, en niet iets wat je erbij doet."),
            ("p", "In die rij 2, 6, 12, 20, 30 lopen de verschillen op met telkens 2, dus het volgende "
                  "verschil is 12 en het volgende getal <strong>42</strong>. Slim gissen is trouwens geen "
                  "gokken: elke poging vertelt je in welke richting de volgende moet."),
            ("p", "Wat <strong>geen</strong> heuristiek is: het antwoord opzoeken in de oplossingen "
                  "achteraan. Dat brengt je geen stap vooruit."),
        ]),
        dict(kop="Schatten", blokken=[
            ("p", "<strong>Schatten</strong> met ronde getallen zegt je in welke "
                  "<strong>grootteorde</strong> het antwoord moet liggen. Wie 19 · 21 schat op ongeveer 400, "
                  "ziet meteen dat 3999 niet kan kloppen."),
            ("p", "Maar een schatting is een <strong>controle</strong>, geen antwoord: wie goed schat, moet "
                  "de exacte berekening nog altijd uitvoeren."),
            ("p", "Verf is een mooi voorbeeld van een plan dat werk spaart. Voor een muur van 4,2 m op 2,6 m "
                  "bereken je eerst de <strong>oppervlakte</strong> en kijk je pas daarna naar het verbruik "
                  "per liter: dan blijft er maar één deling over."),
        ]),
        dict(kop="De vier vaardigheden", blokken=[
            ("p", "De fiche noemt vier vaardigheden die je bij elke opgave gebruikt:"),
            ("p", tabel(["Vaardigheid", "Wat ze inhoudt"], [
                ["taalvaardigheid", "wiskundige uitdrukkingen, tekeningen, grafieken en diagrammen begrijpen"],
                ["rekenvaardigheid", "vlot en juist rekenen, met en zonder rekenmachine"],
                ["meet- en tekenvaardigheid", "hoeken meten met een geodriehoek, tekenen met passer en geodriehoek"],
                ["ICT-vaardigheid", "rekenapps gebruiken en constructies maken in GeoGebra"],
            ])),
            ("weetje", "Veel fouten zijn <strong>leesfouten</strong>: de opgave vroeg iets anders dan wat er "
                       "uitgerekend werd. Taalvaardigheid is bij wiskunde dus geen bijzaak. En ICT is hulp bij "
                       "het rekenen en het tekenen, nooit een vervanging van de redenering."),
        ]),
        dict(kop="Bewijzen en tegenvoorbeelden", blokken=[
            ("p", "Eén <strong>tegenvoorbeeld</strong> volstaat om aan te tonen dat een wiskundige uitspraak "
                  "<strong>vals</strong> is: één geval waarin het niet opgaat, breekt de uitspraak."),
            ("p", "Omgekeerd werkt het niet. Een paar voorbeelden die kloppen, bewijzen <strong>niet</strong> "
                  "dat een eigenschap altijd geldt. Voorbeelden illustreren; voor een bewijs heb je een "
                  "redenering nodig."),
        ]),
    ],
    onthoud=[
        "Mathematiseren is de situatie omzetten in wiskundetaal, demathematiseren is de uitkomst terugvertalen.",
        "Een vraagstuk past in één hoofdstuk, een probleem combineert hoofdstukken.",
        "Vier stappen: begrijp het probleem, maak een plan, voer het plan uit, reflecteer.",
        "Reflecteren hoort bij het oplossen: past het bij de vraag, klopt de eenheid, is het realistisch.",
        "Heuristieken: schets, alles opschrijven, variabelen invoeren, symmetrie, terugrekenen, opsplitsen, slim gissen, patronen zoeken.",
        "Je kiest zelf je oplossingsstrategie; een schets is een volwaardige strategie.",
        "Schatten geeft de grootteorde, maar vervangt de exacte berekening niet.",
        "Vier vaardigheden: taal, rekenen, meten en tekenen, ICT.",
        "Eén tegenvoorbeeld weerlegt; voorbeelden bewijzen nooit.",
        "Verantwoord je tussenstappen, anders is je antwoord niet na te kijken.",
    ],
)


# ───────────────────────── 2. Logica
BUNDELS["logica-symbolen-waarheidstabellen-en-poorten-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Logica: symbolen, waarheidstabellen en poorten",
    onder="Uitspraken, de bewerkingen met hun symbolen, waarheidstabellen, kwantoren, bewijzen en logische poorten.",
    secties=[
        dict(kop="Wat is een logische uitspraak?", blokken=[
            ("p", "Een <strong>logische uitspraak</strong> is een zin waarvan je kan zeggen of hij "
                  "<strong>waar of vals</strong> is. <em>Zeven is een priemgetal</em> is er een. <em>Hoe laat "
                  "is het?</em> niet: bij een vraag past geen waarheidswaarde. Bij een bevel evenmin. Ook "
                  "<em>x is groter dan 3</em> is pas een uitspraak als je weet wat x is."),
            ("p", "Uitspraken krijgen een letter: p, q, r. De <strong>waarheidswaarde</strong> is waar (1) of "
                  "vals (0)."),
        ]),
        dict(kop="De bewerkingen en hun symbolen", blokken=[
            ("p", tabel(["Naam", "Symbool", "Lees als", "Waar wanneer"], [
                ["negatie (ontkenning)", "¬p", "niet p", "als p vals is"],
                ["conjunctie", "p ∧ q", "p en q", "als p en q allebei waar zijn"],
                ["disjunctie", "p ∨ q", "p of q", "als minstens één van de twee waar is"],
                ["implicatie", "p ⇒ q", "als p dan q", "altijd, behalve als p waar is en q vals"],
                ["equivalentie", "p ⇔ q", "p als en slechts als q", "als p en q dezelfde waarheidswaarde hebben"],
            ])),
            ("p", "De <strong>negatie</strong>, ook <em>ontkenning</em> genoemd, keert de waarheidswaarde om "
                  "en doet niets anders: is p waar, dan is ¬p vals, en omgekeerd."),
            ("p", "Het dakje ∧ is <em>en</em>, het omgekeerde dakje ∨ is <em>of</em>. Een ezelsbruggetje: ∧ "
                  "lijkt op de A van <em>and</em>. Je mag ze dus nooit door elkaar gebruiken: p ∧ q vraagt "
                  "allebei, p ∨ q neemt genoegen met één."),
            ("kader", "De <strong>logische 'of' verschilt van de 'of' in de omgangstaal</strong>. "
                      "<em>Koffie of thee?</em> betekent in het dagelijks leven meestal één van beide. In de "
                      "logica is p ∨ q ook waar als p en q <strong>allebei</strong> waar zijn."),
            ("p", "Bij de <strong>equivalentie</strong> geldt: allebei waar of allebei vals maakt ze waar; "
                  "verschillen ze, dan is ze vals."),
        ]),
        dict(kop="Waarheidstabellen", blokken=[
            ("p", "Een <strong>waarheidstabel</strong> zet alle mogelijke combinaties onder elkaar. Elke "
                  "variabele <strong>verdubbelt</strong> het aantal rijen: twee variabelen geven "
                  "<strong>vier</strong> rijen, drie variabelen <strong>acht</strong>, vier variabelen "
                  "<strong>zestien</strong>, en n variabelen 2 tot de macht n."),
            ("p", tabel(["p", "q", "¬p", "p ∧ q", "p ∨ q", "p ⇒ q", "p ⇔ q"], [
                ["1", "1", "0", "1", "1", "1", "1"],
                ["1", "0", "0", "0", "1", "0", "0"],
                ["0", "1", "1", "0", "1", "1", "0"],
                ["0", "0", "1", "0", "0", "1", "1"],
            ])),
            ("p", "Is p waar en q vals, dan is p ∧ q dus <strong>vals</strong> (de conjunctie vraagt allebei) "
                  "en p ∨ q <strong>waar</strong> (de disjunctie neemt genoegen met één)."),
            ("weetje", "De implicatie is de lastigste rij. <em>Als het regent, neem ik mijn paraplu mee</em> "
                       "is pas gelogen op de dag dat het regent én je je paraplu thuis laat. Is p vals, dan is "
                       "de implicatie net <strong>waar</strong>: je hebt niets beloofd voor die dag."),
        ]),
        dict(kop="Tautologie en contradictie", blokken=[
            ("p", "Een <strong>tautologie</strong> is een uitspraak die <strong>bij elke mogelijke "
                  "invulling waar</strong> is. p ∨ ¬p is er een: het regent of het regent niet, wat er ook "
                  "gebeurt. In de waarheidstabel staat dan in de hele kolom een 1."),
            ("p", "Een <strong>contradictie</strong> is het omgekeerde: <strong>bij elke invulling "
                  "vals</strong>. p ∧ ¬p is er een: het regent én het regent niet, dat kan nooit samen."),
        ]),
        dict(kop="Kwantoren", blokken=[
            ("p", "Een <strong>kwantor</strong> zegt over hoeveel gevallen een uitspraak gaat."),
            ("p", tabel(["Kwantor", "Naam", "Lees als"], [
                ["∀", "universele kwantor", "voor alle, voor elke waarde geldt"],
                ["∃", "existentiële kwantor", "er bestaat minstens één"],
            ])),
            ("p", "<strong>Eén tegenvoorbeeld volstaat om een uitspraak met ∀ te weerleggen.</strong> "
                  "<em>Alle priemgetallen zijn oneven</em> sneuvelt op het getal 2."),
            ("p", "De <strong>negatie van ∀ is ∃ met een negatie erachter</strong>. De ontkenning van "
                  "<em>alle leerlingen slaagden</em> is dus niet <em>geen enkele leerling slaagde</em>, maar "
                  "<strong>minstens één leerling slaagde niet</strong>."),
        ]),
        dict(kop="Nodige en voldoende voorwaarden", blokken=[
            ("p", "Bij een implicatie p ⇒ q hoort een manier van spreken die je moet kunnen lezen."),
            ("p", "Een voorwaarde is <strong>nodig</strong> als ze niet gemist kan worden, en "
                  "<strong>voldoende</strong> als ze op zichzelf al genoeg is: is ze waar, dan is de uitspraak "
                  "zeker waar."),
            ("p", "<em>Als een vierhoek een vierkant is, dan heeft hij vier rechte hoeken.</em> Vier rechte "
                  "hoeken hebben is <strong>nodig</strong> om een vierkant te zijn: zonder die hoeken geen "
                  "vierkant. Maar het is niet <em>voldoende</em>, want een rechthoek heeft ze ook. Omgekeerd "
                  "is <em>een vierkant zijn</em> wél <strong>voldoende</strong> om vier rechte hoeken te "
                  "hebben, maar niet nodig."),
        ]),
        dict(kop="Rond de implicatie", blokken=[
            ("p", tabel(["Naam", "Vorm", "Zelfde waarde als p ⇒ q?"], [
                ["de implicatie zelf", "p ⇒ q", "—"],
                ["het omgekeerde", "q ⇒ p", "nee"],
                ["het tegengestelde", "¬p ⇒ ¬q", "nee"],
                ["de contrapositie", "¬q ⇒ ¬p", "ja, altijd"],
            ])),
            ("p", "<em>Als het een hond is, dan is het een dier</em> is waar. Het omgekeerde is dat duidelijk "
                  "niet. Maar de contrapositie, <em>als het geen dier is, dan is het geen hond</em>, is even "
                  "waar als de oorspronkelijke uitspraak."),
        ]),
        dict(kop="De wetten van De Morgan", blokken=[
            ("p", "¬(p ∧ q) is hetzelfde als ¬p ∨ ¬q, en ¬(p ∨ q) is hetzelfde als ¬p ∧ ¬q. Let op hoe "
                  "<em>en</em> en <em>of</em> daarbij van plaats wisselen."),
            ("p", "<em>Het is niet zo dat het regent en waait</em> vertaal je dus als "
                  "<strong>¬(p ∧ q)</strong>: de negatie staat voor het hele stuk."),
            ("kader", "<strong>¬(p ∧ q) is niet hetzelfde als ¬p ∧ ¬q.</strong> Het eerste zegt: "
                      "<em>niet allebei</em>. Het tweede zegt: <em>geen van beide</em>. Dat is iets anders."),
        ]),
        dict(kop="Tegenvoorbeelden", blokken=[
            ("p", "<em>Elk getal dat deelbaar is door 3, is ook deelbaar door 6.</em> Dat is vals, en je "
                  "weerlegt het met één getal: <strong>9</strong> is deelbaar door 3 maar niet door 6. Elk "
                  "oneven veelvoud van 3 doet het: 3, 9, 15, 21. Het getal <strong>12</strong> weerlegt niets, "
                  "want dat is door allebei deelbaar en past juist bij de uitspraak."),
            ("p", "<em>Als je de zijden van een vierkant verdubbelt, verdubbelt de oppervlakte.</em> Ook vals: "
                  "een zijde van 2 wordt 4, en de oppervlakte gaat van 4 naar <strong>16</strong>, dus vier "
                  "keer zo groot. Bij een kubus zou het volume zelfs acht keer zo groot worden."),
        ]),
        dict(kop="Wat je moet kunnen bewijzen", blokken=[
            ("p", "De vakfiche geeft een lijst met bewijzen die je moet kunnen aanvullen en verklaren:"),
            ("p", "de stelling van <strong>Pythagoras</strong>, de <strong>irrationaliteit van √2</strong>, de "
                  "eigenschappen van de <strong>tweedegraadsfuncties</strong>, de <strong>grondformule</strong> "
                  "van de goniometrie, en de <strong>sinus- en cosinusregel</strong>. De som van de hoeken in "
                  "een vierhoek staat er dus níét bij."),
            ("p", "Tijdens het examen mag je het <strong>formularium uit bijlage 1</strong> gebruiken, maar "
                  "<strong>niet</strong> de lijst met bewijzen. Die moet je zelf kunnen aanvullen en verklaren."),
        ]),
        dict(kop="Logische poorten", blokken=[
            ("p", "Een computer rekent met stroom die er is (1) of niet is (0), en met <strong>logische "
                  "poorten</strong> die precies de bewerkingen hierboven uitvoeren."),
            ("p", tabel(["Poort", "Wat ze doet", "Hoort bij"], [
                ["EN-poort", "geeft alleen een signaal door als beide ingangen een signaal krijgen", "de conjunctie ∧"],
                ["OF-poort", "geeft een signaal door zodra minstens één ingang een signaal krijgt", "de disjunctie ∨"],
                ["NIET-poort", "keert het signaal om dat op haar ingang binnenkomt", "de negatie ¬"],
                ["NEN-poort", "een EN-poort met een NIET erachter", "¬(p ∧ q)"],
                ["NOF-poort", "een OF-poort met een NIET erachter", "¬(p ∨ q)"],
            ])),
            ("p", "In een <strong>schakeling</strong> zet je die poorten achter elkaar, en met een waarheidstabel "
                  "reken je na wat er uitkomt. Een lamp die alleen brandt als de "
                  "<strong>hoofdschakelaar én de wandschakelaar</strong> aan "
                  "staan, vraagt een <strong>EN-poort</strong>. Een alarm dat afgaat als de deur "
                  "<strong>of</strong> het raam opengaat, vraagt een <strong>OF-poort</strong>: één van beide "
                  "volstaat."),
            ("weetje", "In het Engels heet de NIET-poort NOT of <em>inverter</em>. Alles wat een computer "
                       "doet, komt uiteindelijk neer op miljarden van deze poorten."),
        ]),
    ],
    onthoud=[
        "Een logische uitspraak is waar of vals; een vraag of een bevel is er geen.",
        "¬ is niet, ∧ is en, ∨ is of, ⇒ is als … dan, ⇔ is als en slechts als.",
        "De logische 'of' is ook waar als allebei waar zijn.",
        "Elke variabele verdubbelt de tabel: 2 geeft 4 rijen, 3 geeft 8, 4 geeft 16.",
        "p ⇒ q is enkel vals als p waar is en q vals.",
        "Een tautologie is altijd waar (p ∨ ¬p), een contradictie altijd vals (p ∧ ¬p).",
        "∀ is 'voor alle', ∃ is 'er bestaat'; de negatie van 'alle slaagden' is 'minstens één slaagde niet'.",
        "Nodig kan niet gemist worden, voldoende is op zichzelf genoeg.",
        "De contrapositie ¬q ⇒ ¬p heeft altijd dezelfde waarde; het omgekeerde q ⇒ p niet.",
        "De Morgan: ¬(p ∧ q) is ¬p ∨ ¬q, en dat is iets anders dan ¬p ∧ ¬q.",
        "Bewijzen op de fiche: Pythagoras, irrationaliteit van √2, tweedegraadsfuncties, grondformule, sinus- en cosinusregel.",
        "Het formularium uit bijlage 1 mag mee op het examen, de bewijzenlijst niet.",
        "EN-, OF- en NIET-poort; NEN en NOF zijn hun omgekeerden.",
    ],
)


# ───────────────────────── 3. Reële getallen, wortels en machten
BUNDELS["reele-getallen-wortels-en-machten-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Reële getallen, wortels en machten",
    onder="De getallenverzamelingen, rationaal tegenover irrationaal, rekenen met wortels en de rekenregels voor machten.",
    secties=[
        dict(kop="De getallenverzamelingen", blokken=[
            ("p", "De getallen zitten in elkaar als een reeks dozen. Elke doos bevat de vorige helemaal."),
            ("p", tabel(["Verzameling", "Teken", "Wat er nieuw bij komt", "Voorbeeld"], [
                ["natuurlijke getallen", "ℕ", "tellen vanaf 0", "0, 1, 2, 3"],
                ["gehele getallen", "ℤ", "de negatieve getallen", "min 7, min 1"],
                ["rationale getallen", "ℚ", "alles wat je als breuk kan schrijven", "3/4, 0,125, min 2/5"],
                ["reële getallen", "ℝ", "de getallen die géén breuk zijn", "√2, π"],
            ])),
            ("p", "Elk natuurlijk getal is dus ook een geheel getal, elk geheel getal ook rationaal, en elk "
                  "rationaal getal ook reëel. Omgekeerd geldt dat niet. Het getal <strong>min 7</strong> "
                  "hoort bij de gehele getallen maar niet bij de natuurlijke: dat is de eerste doos waarin "
                  "het past."),
        ]),
        dict(kop="Rationaal of irrationaal", blokken=[
            ("p", "Een <strong>rationaal</strong> getal kan je schrijven als een breuk van twee gehele "
                  "getallen. In decimale vorm is ze <strong>eindig</strong> (0,125) of "
                  "<strong>repeterend</strong>, dus met een stukje dat zich eindeloos herhaalt "
                  "(0,333… of 0,142857142857…). Allebei die vormen betekenen: het is een breuk."),
            ("p", "Een <strong>irrationaal</strong> getal heeft een decimale vorm die "
                  "<strong>oneindig én niet-repeterend</strong> is: ze stopt nooit en herhaalt nooit "
                  "een patroon. Je kan het dus niet als breuk van twee gehele "
                  "getallen schrijven. √2, √3, √5 en π zijn zo. En dáárom volstaan de rationale getallen "
                  "niet om de getallenas te vullen: er blijven gaten open, en juist daar liggen de "
                  "irrationale getallen."),
            ("weetje", "√9 is géén irrationaal getal: dat is gewoon 3. Enkel een wortel die niet mooi "
                       "uitkomt, is irrationaal."),
            ("p", "Over <strong>π</strong>: het is irrationaal, dus 22/7 en 3,14 zijn benaderingen en niet "
                  "de echte waarde. De decimalen van π zijn tot vandaag nooit in herhaling gevallen."),
        ]),
        dict(kop="Breuk, kommagetal en procent", blokken=[
            ("p", "Dezelfde waarde in drie kleren. Van breuk naar kommagetal deel je de teller door de "
                  "noemer; van kommagetal naar procent vermenigvuldig je met 100."),
            ("p", tabel(["Breuk", "Kommagetal", "Procent"], [
                ["1/2", "0,5", "50 %"],
                ["2/5", "0,4", "40 %"],
                ["3/5", "0,6", "60 %"],
                ["3/4", "0,75", "75 %"],
                ["3/8", "0,375", "37,5 %"],
                ["1/8", "0,125", "12,5 %"],
            ])),
            ("p", "Omgekeerd: 0,75 is 75/100, en dat vereenvoudig je door teller en noemer door 25 te delen "
                  "tot 3/4. 0,4 is 4/10, gedeeld door 2 wordt dat 2/5."),
        ]),
        dict(kop="Wortels", blokken=[
            ("p", "De <strong>vierkantswortel</strong> van a is het positieve getal dat in het kwadraat a "
                  "geeft. De <strong>derdemachtswortel</strong> van a is het getal dat tot de derde macht a "
                  "geeft: de derdemachtswortel van 27 is 3, van 64 is 4, van 125 is 5."),
            ("p", "<strong>Vereenvoudigen</strong> doe je door het grootste volkomen kwadraat uit de wortel "
                  "te halen:"),
            ("p", tabel(["Wortel", "Splitsen", "Vereenvoudigd"], [
                ["√18", "√(9 · 2)", "3√2"],
                ["√50", "√(25 · 2)", "5√2"],
                ["√72", "√(36 · 2)", "6√2"],
            ])),
            ("p", "De regel erachter: <strong>de wortel van een product is het product van de wortels</strong>. "
                  "Daarom is √3 · √12 gelijk aan √36, dus 6, en √5 · √20 gelijk aan √100, dus 10."),
            ("kader", "<strong>De wortel van een som is níét de som van de wortels.</strong> √(9 + 16) is "
                      "√25 en dus 5, niet 3 + 4 = 7. Reken de som eerst uit en trek daarna pas de wortel."),
            ("p", "Je kan wortels wel <strong>optellen</strong> als ze precies dezelfde wortel zijn, net als "
                  "gelijksoortige termen: √3 + √3 is 2√3."),
            ("p", "Een noemer <strong>wortelvrij maken</strong> doe je door teller en noemer met diezelfde "
                  "wortel te vermenigvuldigen. 1/√5 wordt zo √5/5."),
            ("p", "Let op met √(a²) als a negatief is: dat is niet a maar <strong>min a</strong>, want een "
                  "wortel is nooit negatief. In het algemeen is √(a²) gelijk aan de absolute waarde van a."),
        ]),
        dict(kop="Machten", blokken=[
            ("p", tabel(["Regel", "In symbolen", "Voorbeeld"], [
                ["zelfde grondtal, vermenigvuldigen", "aᵐ · aⁿ = aᵐ⁺ⁿ", "a⁴ · a³ = a⁷"],
                ["zelfde grondtal, delen", "aᵐ : aⁿ = aᵐ⁻ⁿ", "a⁶ : a² = a⁴"],
                ["macht van een macht", "(aᵐ)ⁿ = aᵐ·ⁿ", "(a³)² = a⁶"],
                ["macht van een product", "(ab)ⁿ = aⁿbⁿ", "(2a)³ = 8a³"],
                ["exponent nul", "a⁰ = 1", "5⁰ = 1"],
                ["negatieve exponent", "a⁻ⁿ = 1/aⁿ", "2⁻³ = 1/8, 3⁻² = 1/9"],
            ])),
            ("p", "Bij vermenigvuldigen <strong>tel je de exponenten op</strong>, je vermenigvuldigt ze niet. "
                  "Dat is de fout die het vaakst gemaakt wordt. Bij een <strong>macht van een macht</strong> "
                  "vermenigvuldig je ze wél."),
            ("p", "Bij (2a)³ krijgt élke factor de exponent: 2³ · a³, dus 8a³. Vergeet het getal vooraan niet."),
            ("weetje", "Een <strong>negatieve exponent</strong> maakt van de macht een breuk met 1 in de "
                       "teller. Het getal zelf wordt daar niet negatief van: 2⁻³ is 1/8, een positief getal."),
        ]),
        dict(kop="Rekeneigenschappen", blokken=[
            ("p", "Drie namen die je moet kunnen herkennen:"),
            ("p", tabel(["Naam", "Wat ze zegt", "Voorbeeld"], [
                ["commutativiteit", "de volgorde mag wisselen (commutatief)", "3 + 5 = 5 + 3"],
                ["associativiteit", "de haakjes mogen verschuiven (associatief)", "(2 + 8) + 5 = 2 + (8 + 5)"],
                ["distributiviteit", "de factor wordt over de som verdeeld (distributief)", "3 · (20 + 7) = 3 · 20 + 3 · 7"],
            ])),
            ("p", "De distributieve eigenschap is degene die je later bij het uitwerken van haakjes en bij "
                  "het ontbinden in factoren voortdurend gebruikt."),
            ("p", "Sommige berekeningen kunnen <strong>enkel in de reële getallen</strong>: de wortel van 2 "
                  "bestaat niet als breuk en dus niet in ℚ. De wortel van een negatief getal bestaat zelfs in "
                  "ℝ niet."),
        ]),
    ],
    onthoud=[
        "ℕ zit in ℤ, ℤ in ℚ, ℚ in ℝ; omgekeerd geldt het niet.",
        "Rationaal: de decimale vorm stopt of herhaalt zich. Irrationaal: geen van beide.",
        "√9 is 3, dus rationaal. √2, √3 en π zijn irrationaal.",
        "√a · √b = √(ab), maar √(a + b) is NIET √a + √b.",
        "√3 + √3 = 2√3: gelijke wortels mag je optellen.",
        "1/√5 wortelvrij maken: teller en noemer maal √5, dus √5/5.",
        "aᵐ · aⁿ = aᵐ⁺ⁿ (optellen), (aᵐ)ⁿ = aᵐⁿ (vermenigvuldigen).",
        "a⁰ = 1 en a⁻ⁿ = 1/aⁿ.",
        "(2a)³ = 8a³: elke factor krijgt de exponent.",
        "Commutatief is volgorde, associatief is haakjes verschuiven, distributief is uitdelen.",
    ],
)


# ───────────────────────── 4. Ordenen, afronden, intervallen, notatie
BUNDELS["ordenen-afronden-intervallen-en-wetenschappelijke-notatie-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Ordenen, afronden, intervallen en wetenschappelijke notatie",
    onder="Getallen vergelijken en schatten, netjes afronden, intervallen lezen en schrijven, en werken met machten van tien.",
    secties=[
        dict(kop="Ordenen op de getallenas", blokken=[
            ("p", "Op de <strong>getallenas</strong> staat het kleinste getal links. Staat min 3 links van 1, "
                  "dan betekent dat gewoon: min 3 is kleiner dan 1. Bij negatieve getallen draait je gevoel je "
                  "in de luren: <strong>min 8 is kleiner dan min 3</strong>, ook al is 8 groter dan 3. Hoe "
                  "verder van nul naar links, hoe kleiner."),
            ("p", tabel(["Teken", "Lees als"], [
                ["<", "is kleiner dan"],
                [">", "is groter dan"],
                ["≤", "is kleiner dan of gelijk aan"],
                ["≥", "is groter dan of gelijk aan"],
            ])),
            ("p", "Om getallen in verschillende kleren te ordenen, zet je ze eerst allemaal in dezelfde vorm. "
                  "0,5 tegenover 3/5 tegenover 45 %: maak er 0,5 — 0,6 — 0,45 van, en dan is de volgorde van "
                  "klein naar groot meteen duidelijk: 45 %, 0,5, 3/5."),
            ("weetje", "Tussen twee verschillende reële getallen ligt altijd nog een ander reëel getal. Tussen "
                       "2,4 en 2,5 ligt 2,45, en daartussen weer 2,445. Dat houdt nooit op."),
        ]),
        dict(kop="Afronden", blokken=[
            ("p", "De <strong>afrondingsregel</strong> van de vakfiche: kijk naar het <strong>eerste cijfer dat wegvalt</strong>. Is dat "
                  "<strong>5 of meer</strong>, dan rond je naar boven af; is het <strong>4 of minder</strong>, "
                  "naar beneden. Alle cijfers dáárachter doen niet mee."),
            ("p", tabel(["Getal", "Afronden op", "Eerste cijfer dat wegvalt", "Resultaat"], [
                ["3,4567", "twee cijfers na de komma", "6", "3,46"],
                ["2,3449", "twee cijfers na de komma", "4", "2,34"],
                ["7,3851", "twee cijfers na de komma", "5", "7,39"],
                ["0,449", "één cijfer na de komma", "4", "0,4"],
            ])),
            ("kader", "Bij 2,3449 is het verleidelijk om eerst 2,345 te maken en dán af te ronden naar 2,35. "
                      "Dat is fout: je rondt <strong>één keer</strong> af, en enkel het eerste wegvallende "
                      "cijfer telt. Om dezelfde reden rond je pas <strong>op het einde</strong> van een "
                      "berekening af: rond je tussendoor af, dan stapelen de afrondingsfouten zich op."),
            ("p", "Een afgerond getal is een <strong>bereik</strong>, geen punt. Een weegschaal die 2,5 kg "
                  "aangeeft en op honderd gram afrondt, kan alles tussen <strong>2,45 en 2,55 kg</strong> "
                  "wegen."),
        ]),
        dict(kop="Schatten", blokken=[
            ("p", "<strong>Schatten</strong> is vooraf ruw uitrekenen wat er ongeveer moet uitkomen, met "
                  "ronde getallen. 48 · 21 schat je als 50 · 20, dus ongeveer 1000. 19 · 31 schat je op "
                  "honderdtallen als 20 · 30, dus 600."),
            ("p", "Een schatting is een <strong>hulpmiddel vooraf</strong>, en vervangt de controle achteraf "
                  "niet. Ze vangt wel de grove fouten: wie 48 · 21 als 100,8 noteert, ziet meteen dat er een "
                  "komma verkeerd staat."),
            ("p", "Schatten helpt ook bij wortels. √2 ligt tussen 1 en 2 want 1² is 1 en 2² is 4, en dichter "
                  "bij 1,4 dan bij 1,5: 1,4² is 1,96, net onder 2."),
        ]),
        dict(kop="Intervallen", blokken=[
            ("p", "Een <strong>interval</strong> is een stuk van de getallenas. Het haakje zegt of de grens "
                  "meedoet: een haakje dat <strong>naar binnen</strong> wijst, [ of ], neemt de grens mee; "
                  "een haakje dat <strong>naar buiten</strong> wijst, ] of [, laat ze erbuiten."),
            ("p", tabel(["Interval", "Naam", "Betekenis"], [
                ["[0, 1]", "gesloten", "alle getallen van 0 tot 1, de grenzen inbegrepen"],
                ["]2, 5[", "open", "alle getallen tussen 2 en 5, de grenzen niet inbegrepen"],
                ["[0, 4[", "halfopen", "0 hoort erbij, 4 niet"],
                ["[3, →[", "onbegrensd", "alle getallen groter dan of gelijk aan 3"],
                ["]→, 7[", "onbegrensd", "alle getallen kleiner dan 7"],
                ["]5, →[", "onbegrensd", "alle getallen groter dan 5"],
                ["[−2, 3]", "gesloten", "x ligt tussen −2 en 3, grenzen inbegrepen"],
            ])),
            ("p", "Bij <strong>oneindig</strong> staat het haakje altijd naar buiten. Oneindig is geen getal, "
                  "dus het kan ook niet tot het interval behoren."),
            ("weetje", "Het interval [3, 3] is niet leeg: het bevat precies één getal, namelijk 3. Het "
                       "interval ]3, 3[ is wél leeg."),
        ]),
        dict(kop="Wetenschappelijke notatie", blokken=[
            ("p", "In de <strong>wetenschappelijke notatie</strong> schrijf je een getal als een getal tussen "
                  "1 en 10, maal een macht van tien. Er staat dus <strong>precies één cijfer voor de komma, "
                  "van 1 tot en met 9</strong>."),
            ("p", tabel(["Gewoon getal", "Wetenschappelijke notatie"], [
                ["45 000", "4,5 · 10⁴"],
                ["6 200 000", "6,2 · 10⁶"],
                ["0,00072", "7,2 · 10⁻⁴"],
                ["300 000", "3 · 10⁵"],
                ["0,0025", "2,5 · 10⁻³"],
            ])),
            ("p", "Zo is 12,5 · 10³ géén correcte wetenschappelijke notatie: er staan twee cijfers voor de "
                  "komma. Je schrijft het als 1,25 · 10⁴."),
            ("kader", "Een <strong>negatieve exponent</strong> betekent dat het getal <em>klein</em> is, niet "
                      "dat het negatief is. 2,5 · 10⁻³ is 0,0025, een positief getal."),
            ("p", "Terugrekenen naar een gewoon getal: 3 · 10⁵ is 300 000. En let op bij eenheden: 1,5 · 10¹¹ "
                  "meter is 1,5 · 10⁸ kilometer, want een kilometer is duizend meter, dus de exponent zakt "
                  "met 3."),
            ("p", "Wetenschappers gebruiken deze notatie omdat je met machten van tien even makkelijk over "
                  "een atoom als over een sterrenstelsel schrijft, zonder rijen nullen te tellen."),
        ]),
    ],
    onthoud=[
        "Op de getallenas staat het kleinste getal links; min 8 is kleiner dan min 3.",
        "≤ is kleiner dan of gelijk aan, ≥ is groter dan of gelijk aan.",
        "Afronden: eerste wegvallende cijfer 5 of meer naar boven, 4 of minder naar beneden.",
        "Rond één keer af, en pas op het einde van een berekening.",
        "Een haakje naar binnen neemt de grens mee, een haakje naar buiten niet.",
        "Bij oneindig wijst het haakje altijd naar buiten.",
        "Wetenschappelijke notatie: één cijfer van 1 tot 9 voor de komma, maal een macht van tien.",
        "Een negatieve exponent maakt het getal klein, niet negatief.",
    ],
)


# ───────────────────────── 5. Rechten, vlakken en gelijkvormigheid
BUNDELS["rechten-vlakken-en-gelijkvormigheid-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Rechten, vlakken en gelijkvormigheid",
    onder="Hoe rechten en vlakken in de ruimte liggen, hoe je een ruimtefiguur tekent, en wat schaal doet met lengte, oppervlakte en volume.",
    secties=[
        dict(kop="Rechten en vlakken in de ruimte", blokken=[
            ("p", "In het <strong>vlak</strong> kunnen twee rechten maar drie dingen doen: samenvallen, "
                  "elkaar snijden, of evenwijdig lopen. In de <strong>ruimte</strong> komt er een vierde "
                  "mogelijkheid bij die in het vlak niet bestaat: <strong>kruisende rechten</strong>. Die "
                  "snijden elkaar niet én liggen niet in hetzelfde vlak. Denk aan een weg en een brug die er "
                  "schuin boven loopt."),
            ("p", tabel(["Ligging", "Wat het betekent"], [
                ["twee rechten snijden", "ze hebben één punt gemeen"],
                ["twee rechten evenwijdig", "ze liggen in één vlak en snijden elkaar niet"],
                ["twee rechten kruisend", "ze liggen niet in één vlak en snijden elkaar niet"],
                ["rechte in een vlak", "elk punt van de rechte ligt in het vlak"],
                ["rechte evenwijdig met een vlak", "ze hebben geen enkel punt gemeen"],
                ["rechte snijdt een vlak", "ze hebben precies één punt gemeen"],
                ["twee vlakken evenwijdig", "ze snijden elkaar niet en vallen niet samen"],
                ["twee vlakken snijden", "hun doorsnede is een rechte"],
            ])),
            ("kader", "<strong>Twee vlakken snijden elkaar nooit in één punt.</strong> Raken ze elkaar, dan "
                      "is hun doorsnede meteen een hele <strong>rechte</strong>. Dat zie je aan twee muren "
                      "van een kamer: ze ontmoeten elkaar in een lijn, niet in een punt."),
        ]),
        dict(kop="Ruimtefiguren tekenen", blokken=[
            ("p", "Een <strong>ruimtefiguur</strong> heeft drie afmetingen: een kubus, een balk, een cilinder, "
                  "een kegel, een piramide, een bol. Een vierkant, een cirkel of een driehoek is een "
                  "<strong>vlakke</strong> figuur."),
            ("p", "Een <strong>balk</strong> heeft 6 zijvlakken, 12 ribben en 8 hoekpunten. De "
                  "<strong>ontwikkeling</strong> van een ruimtefiguur is het platte patroon dat je krijgt door "
                  "hem open te vouwen; bij een kubus zijn dat zes vierkanten aan elkaar. Daarmee reken je de "
                  "totale oppervlakte uit, en daarmee knip je hem ook uit karton."),
            ("p", "Om een ruimtefiguur op papier te zetten zijn er twee manieren die de fiche noemt:"),
            ("p", "<strong>Projecties op drie vlakken</strong>: het <strong>vooraanzicht</strong>, het "
                  "<strong>bovenaanzicht</strong> en het <strong>zijaanzicht</strong>. Elk aanzicht is een "
                  "vlakke tekening, en samen leggen ze de figuur volledig vast. Zo werkt een bouwplan."),
            ("p", "<strong>Cavalièreperspectief</strong>: het voorvlak teken je op ware grootte, en de ribben "
                  "naar achteren teken je schuin en vaak ingekort. Wat in het echt evenwijdig is, blijft in "
                  "deze tekening evenwijdig. Dat maakt het handig om te tekenen, maar het ziet er niet uit "
                  "zoals je oog het ziet: een echt perspectief laat evenwijdige lijnen naar een verdwijnpunt "
                  "lopen."),
        ]),
        dict(kop="Verzamelingen", blokken=[
            ("p", "Drie bewerkingen op verzamelingen, die je ook bij het tellen nodig hebt:"),
            ("p", tabel(["Bewerking", "Teken", "Wat erin zit"], [
                ["doorsnede", "A ∩ B", "de elementen die in A én in B zitten"],
                ["unie", "A ∪ B", "de elementen die in A of in B zitten, of in allebei"],
                ["verschil", "A \\ B", "de elementen van A die niet in B zitten"],
            ])),
            ("p", "<strong>A is een deelverzameling van B</strong> betekent: elk element van A zit ook in B. "
                  "De unie is dus níét wat ze gemeen hebben, dat is de doorsnede; de unie is alles samen."),
        ]),
        dict(kop="Gelijkvormigheid", blokken=[
            ("p", "Twee figuren zijn <strong>gelijkvormig</strong> als ze dezelfde vorm hebben maar niet "
                  "noodzakelijk dezelfde grootte: alle hoeken zijn gelijk en alle zijden staan in dezelfde "
                  "verhouding. Die verhouding heet de <strong>gelijkvormigheidsfactor</strong> k."),
            ("p", "Drie <strong>kenmerken</strong> om gelijkvormigheid vast te stellen:"),
            ("p", tabel(["Kenmerk", "Wat je nagaat"], [
                ["HH", "twee hoeken zijn gelijk; de derde is dat dan automatisch ook"],
                ["ZZZ", "de drie zijdeverhoudingen zijn gelijk"],
                ["ZHZ", "twee zijden staan in dezelfde verhouding en de hoek ertussen is gelijk"],
            ])),
            ("p", "Hebben twee driehoeken twee gelijke hoeken, dan zijn ze dus <strong>gelijkvormig</strong>, "
                  "en dan liggen alle verhoudingen vast. Maar gelijkvormig betekent niet gelijk: de hoeken "
                  "leggen de <em>vorm</em> vast, niet de <em>grootte</em>. Ken je alleen de drie hoeken, dan "
                  "liggen de zijden dus níét vast."),
            ("p", "Een driehoek met zijden 3, 4 en 5 en een gelijkvormige driehoek met kleinste zijde 9: de "
                  "factor is 3, dus de langste zijde is 15."),
        ]),
        dict(kop="Wat schaal doet met lengte, oppervlakte en volume", blokken=[
            ("p", "Dit is de kern van het hoofdstuk, en het gaat bijna altijd fout:"),
            ("p", tabel(["Bij factor k", "Wordt vermenigvuldigd met"], [
                ["elke lengte", "k"],
                ["elke oppervlakte", "k²"],
                ["elk volume", "k³"],
            ])),
            ("p", "Bij factor 3 worden de lengtes 3 keer zo groot, de oppervlakte 9 keer, het volume 27 keer. "
                  "Bij factor 4 wordt de oppervlakte 16 keer zo groot. Bij factor 5: 25 keer. Bij factor 2 "
                  "wordt het volume 8 keer zo groot, dus wie alle ribben van een kubus verdubbelt, krijgt "
                  "<strong>acht</strong> keer zoveel inhoud en niet het dubbele."),
            ("p", "Een foto van 10 op 15 die 20 op 30 wordt, heeft factor 2 en dus <strong>vier</strong> keer "
                  "zoveel oppervlakte. Een bol met een dubbel zo grote straal heeft vier keer zoveel "
                  "buitenkant, dus vier keer zoveel verf."),
            ("weetje", "Daarom zou een reus van drie keer een mens niet kunnen bestaan: zijn gewicht (volume) "
                       "wordt 27 keer zo groot, maar de doorsnede van zijn botten (oppervlakte) maar 9 keer. "
                       "De botten zouden de last niet dragen. Dat heet het vierkant-kubuswet-probleem."),
        ]),
        dict(kop="Schaal", blokken=[
            ("p", "Een <strong>schaal van 1 op 50</strong> betekent: wat op de tekening 1 is, is in het echt "
                  "50. De tekening is dus <strong>kleiner</strong> dan het voorwerp, niet groter."),
            ("p", tabel(["Schaal", "Op de tekening", "In het echt"], [
                ["1 : 50 (een maquette)", "een muur van 12 cm", "600 cm, dus 6 m"],
                ["1 : 200 (een bouwplan)", "een gevel van 7 cm", "1400 cm, dus 14 m"],
                ["1 : 25 000", "8 cm", "200 000 cm, dus 2 km"],
            ])),
            ("p", "Reken altijd eerst in dezelfde eenheid, en zet pas op het einde om naar meter of kilometer."),
        ]),
    ],
    onthoud=[
        "Kruisende rechten bestaan alleen in de ruimte: geen snijpunt en niet in één vlak.",
        "Twee snijdende vlakken hebben een rechte als doorsnede, nooit één punt.",
        "Een balk heeft 6 zijvlakken, 12 ribben en 8 hoekpunten.",
        "De ontwikkeling is het platte patroon van een opengevouwen ruimtefiguur.",
        "Drie aanzichten: vooraanzicht, bovenaanzicht, zijaanzicht.",
        "Bij cavalièreperspectief blijven evenwijdige ribben evenwijdig.",
        "Doorsnede is wat ze gemeen hebben, unie is alles samen.",
        "Gelijkvormigheidskenmerken: HH, ZZZ en ZHZ.",
        "Factor k: lengte maal k, oppervlakte maal k², volume maal k³.",
        "Schaal 1 op 100: de tekening is honderd keer kleiner dan het voorwerp.",
    ],
)


# ───────────────────────── 6. Pythagoras en de rechthoekige driehoek
BUNDELS["pythagoras-en-de-rechthoekige-driehoek-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Pythagoras en de rechthoekige driehoek",
    onder="De stelling van Pythagoras, de afstand tussen twee punten, en sinus, cosinus en tangens.",
    secties=[
        dict(kop="De stelling van Pythagoras", blokken=[
            ("p", "In een <strong>rechthoekige</strong> driehoek is het kwadraat van de schuine zijde gelijk "
                  "aan de som van de kwadraten van de twee rechthoekszijden: <strong>a² + b² = c²</strong>, "
                  "met c de schuine zijde."),
            ("p", "De <strong>schuine zijde</strong> (hypotenusa) ligt tegenover de rechte hoek en is altijd "
                  "de langste zijde van de driehoek. De stelling geldt <strong>alleen</strong> in een "
                  "rechthoekige driehoek; in andere driehoeken heb je de cosinusregel nodig."),
            ("p", tabel(["Gegeven", "Berekening", "Resultaat"], [
                ["rechthoekszijden 6 en 8", "√(36 + 64) = √100", "10"],
                ["rechthoekszijden 9 en 12", "√(81 + 144) = √225", "15"],
                ["schuine zijde 13, één zijde 5", "√(169 − 25) = √144", "12"],
                ["vierkant met zijde 1", "√(1 + 1) = √2", "√2"],
            ])),
            ("p", "<strong>Omgekeerd</strong> kan je met de stelling nagaan óf een driehoek rechthoekig is. "
                  "Zijden 9, 12 en 15: 81 + 144 is 225 en dat is 15², dus ja. Zijden 5, 12 en 13: 25 + 144 is "
                  "169 en dat is 13², dus ook. Zijden 4, 5 en 7: 16 + 25 is 41, maar 7² is 49, dus nee."),
            ("weetje", "Een televisie van 40 inch: dat is de <strong>diagonaal</strong> van het scherm, niet "
                       "de breedte. Met Pythagoras en de beeldverhouding reken je breedte en hoogte eruit."),
        ]),
        dict(kop="Toepassingen", blokken=[
            ("p", "<strong>De ladder tegen de muur.</strong> Een ladder van 5 meter met de voet 3 meter van "
                  "de muur reikt √(25 − 9) = 4 meter hoog. De ladder is de schuine zijde, de muur en de grond "
                  "zijn de rechthoekszijden."),
            ("p", "<strong>De afstand tussen twee punten</strong> in het vlak is niets anders dan Pythagoras "
                  "op het verschil in x en het verschil in y:"),
            ("p", "afstand AB = √((x₂ − x₁)² + (y₂ − y₁)²)"),
            ("p", tabel(["Punten", "Verschillen", "Afstand"], [
                ["A(1, 2) en B(4, 6)", "3 en 4", "√25 = 5"],
                ["A(−2, 1) en B(1, 5)", "3 en 4", "√25 = 5"],
                ["A(0, 0) en B(6, 8)", "6 en 8", "√100 = 10"],
            ])),
            ("p", "Een afstand is <strong>nooit negatief</strong>, ook niet als het ene punt links van het "
                  "andere ligt: de verschillen worden gekwadrateerd, en een kwadraat is positief."),
            ("p", "<strong>De ruimtediagonaal van een balk.</strong> Daar pas je Pythagoras <strong>twee "
                  "keer</strong> toe: eerst op de diagonaal van het grondvlak, en dan op die diagonaal samen "
                  "met de hoogte. Bij een balk 3 bij 4 bij 12: de grondvlakdiagonaal is √(9 + 16) = 5, en de "
                  "ruimtediagonaal √(25 + 144) = 13."),
        ]),
        dict(kop="Sinus, cosinus en tangens", blokken=[
            ("p", "In een rechthoekige driehoek horen bij elke scherpe hoek drie verhoudingen:"),
            ("p", tabel(["Naam", "Verhouding", "Ezelsbruggetje"], [
                ["sinus", "overstaande zijde op schuine zijde", "SOS"],
                ["cosinus", "aanliggende zijde op schuine zijde", "CAS"],
                ["tangens", "overstaande zijde op aanliggende zijde", "TOA"],
            ])),
            ("p", "Samen vormen ze <strong>SOSCASTOA</strong>. Welke je kiest, hangt af van wat je kent en "
                  "wat je zoekt. Ken je de <strong>kijkhoek</strong> naar de top van een boom en je "
                  "<strong>afstand</strong> tot de boom, dan ken je de aanliggende zijde en zoek je de "
                  "overstaande: dat is de <strong>tangens</strong>. Ken je de <strong>lengte van een "
                  "helling</strong> (de schuine zijde) en de hellingshoek, en zoek je het hoogteverschil (de "
                  "overstaande), dan is het de <strong>sinus</strong>."),
            ("p", "De <strong>tangens uitgedrukt in de andere twee</strong>: tan α = sin α / cos α."),
        ]),
        dict(kop="Waarden en eigenschappen", blokken=[
            ("p", tabel(["Hoek", "sinus", "cosinus", "tangens"], [
                ["0°", "0", "1", "0"],
                ["30°", "0,5", "√3/2", "√3/3"],
                ["45°", "√2/2", "√2/2", "1"],
                ["60°", "√3/2", "0,5", "√3"],
                ["90°", "1", "0", "bestaat niet"],
            ])),
            ("p", "De sinus en de cosinus van een scherpe hoek zijn <strong>altijd kleiner dan 1</strong>: ze "
                  "zijn een verhouding waarbij de schuine zijde de grootste is, dus de breuk is kleiner dan "
                  "één. De cosinus kan nooit groter dan 1 worden. De tangens kan dat wél, want daar staat de "
                  "schuine zijde niet in."),
            ("p", "De <strong>goniometrische cirkel</strong> is de cirkel met straal <strong>1</strong> rond "
                  "de oorsprong. Daarop lees je de cosinus af op de x-as en de sinus op de y-as, en daar zie "
                  "je ook meteen waarom geen van beide buiten het gebied van min 1 tot 1 kan komen."),
            ("p", "De <strong>grondformule van de goniometrie</strong>: sin²α + cos²α = 1. Het is Pythagoras "
                  "op de goniometrische cirkel. Daarmee bereken je de ene uit de andere: is de sinus 0,6, dan "
                  "is cos²α = 1 − 0,36 = 0,64 en dus de cosinus 0,8. Is de sinus 0,8, dan is de cosinus 0,6."),
        ]),
        dict(kop="Namen voor hoekenparen", blokken=[
            ("p", tabel(["Naam", "Samen", "Voorbeeld"], [
                ["complementaire hoeken", "90°", "30° en 60°"],
                ["supplementaire hoeken", "180°", "50° en 130°"],
            ])),
            ("p", "Twee <strong>complementaire</strong> hoeken hebben níét dezelfde sinus: de sinus van de "
                  "ene is de cosinus van de andere. sin 30° is 0,5 en sin 60° is √3/2."),
        ]),
    ],
    onthoud=[
        "a² + b² = c², enkel in een rechthoekige driehoek.",
        "De schuine zijde ligt tegenover de rechte hoek en is de langste zijde.",
        "Omgekeerd: klopt a² + b² = c², dan is de driehoek rechthoekig.",
        "Afstand AB = √((x₂ − x₁)² + (y₂ − y₁)²), en die is nooit negatief.",
        "Ruimtediagonaal: Pythagoras twee keer, eerst in het grondvlak.",
        "SOSCASTOA: sinus overstaande op schuine, cosinus aanliggende op schuine, tangens overstaande op aanliggende.",
        "tan α = sin α / cos α.",
        "sin²α + cos²α = 1, de grondformule.",
        "sin 30° = 0,5, cos 0° = 1, tan 45° = 1.",
        "De goniometrische cirkel heeft straal 1.",
        "Complementair is samen 90°, supplementair is samen 180°.",
    ],
)


# ───────────────────────── 7. Sinusregel, cosinusregel en vectoren
BUNDELS["sinusregel-cosinusregel-en-vectoren-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Sinusregel, cosinusregel en vectoren",
    onder="Een willekeurige driehoek oplossen, en rekenen met grootheden die ook een richting hebben.",
    secties=[
        dict(kop="Wat je altijd weet over een driehoek", blokken=[
            ("p", "De som van de hoeken van <strong>elke</strong> driehoek is <strong>180 graden</strong>. "
                  "Ken je er twee, dan ken je de derde: bij 40 en 65 graden is de derde 75 graden, bij 55 en "
                  "72 graden is ze 53 graden."),
            ("p", "De <strong>langste zijde</strong> ligt altijd tegenover de <strong>grootste hoek</strong>. "
                  "En de <strong>driehoeksongelijkheid</strong> zegt dat elke zijde kleiner moet zijn dan de "
                  "twee andere samen: zijden 3, 4 en 9 kunnen dus geen driehoek vormen, want 3 + 4 is kleiner "
                  "dan 9."),
            ("p", "<strong>Een driehoek oplossen</strong> betekent: alle zijden en alle hoeken berekenen uit "
                  "wat je gegeven krijgt."),
        ]),
        dict(kop="De cosinusregel", blokken=[
            ("p", "<strong>a² = b² + c² − 2bc · cos α</strong>, met α de hoek tegenover zijde a."),
            ("p", "Je gebruikt hem in twee gevallen: als je <strong>twee zijden en de ingesloten hoek</strong> "
                  "kent en de derde zijde zoekt, of als je <strong>alle drie de zijden</strong> kent en een "
                  "hoek zoekt. In dat tweede geval vorm je de formule om naar cos α en gebruik je daarna de "
                  "inverse cosinus."),
            ("p", "Ken je de zijden 7 en 9 en de hoek van 40 graden ertussen, dan bereken je met de "
                  "cosinusregel <strong>eerst de derde zijde</strong>. Pas daarna kan je met de sinusregel de "
                  "overige hoeken zoeken."),
            ("kader", "<strong>De cosinusregel is een uitbreiding van de stelling van Pythagoras naar elke driehoek.</strong> Is de ingesloten "
                      "hoek recht, dan is cos 90° gelijk aan 0, valt de hele laatste term weg, en blijft "
                      "a² = b² + c² over. Pythagoras is dus het bijzondere geval."),
        ]),
        dict(kop="De sinusregel", blokken=[
            ("p", "<strong>a / sin α = b / sin β = c / sin γ</strong>: in elke driehoek staat elke zijde in "
                  "dezelfde verhouding tot de sinus van de hoek ertegenover."),
            ("p", "Je gebruikt hem als je een <strong>zijde met de hoek ertegenover</strong> kent, plus nog "
                  "één zijde of één hoek. De regel werkt in <strong>elke</strong> driehoek, niet alleen in "
                  "rechthoekige."),
            ("p", "Eén valkuil: in een <strong>stomphoekige</strong> driehoek heeft de vergelijking "
                  "sin α = 0,6 twee oplossingen onder de 180 graden, een scherpe en een stompe. Kijk altijd "
                  "welke van de twee bij de tekening past; de langste zijde verraadt welke hoek de grootste is."),
            ("p", "<strong>Twee landmeters</strong> die 200 meter uit elkaar staan en elk de hoek naar "
                  "dezelfde boom meten, kennen één zijde en twee hoeken. Met de sinusregel berekenen ze de "
                  "afstand tot de boom, zonder er ooit naartoe te stappen."),
        ]),
        dict(kop="Welke regel wanneer", blokken=[
            ("p", tabel(["Je kent", "Je gebruikt"], [
                ["twee zijden en de hoek ertussen", "de cosinusregel"],
                ["drie zijden", "de cosinusregel"],
                ["een zijde en de hoek ertegenover, plus nog iets", "de sinusregel"],
                ["twee hoeken", "180° min de twee, voor de derde"],
            ])),
            ("weetje", "cos 90° is 0, sin 90° is 1. Die twee waarden verklaren waarom de cosinusregel in een "
                       "rechthoekige driehoek in Pythagoras verandert."),
        ]),
        dict(kop="Wat is een vector?", blokken=[
            ("p", "Sommige grootheden hebben genoeg aan een getal: een massa van 3 kilogram, een temperatuur "
                  "van 18 graden. Andere niet: een kracht van 5 newton zegt niets zolang je niet weet "
                  "waarheen. Zo'n grootheid is een <strong>vector</strong>."),
            ("p", "Een vector heeft drie kenmerken: <strong>richting</strong>, <strong>zin</strong> en "
                  "<strong>grootte</strong>."),
            ("p", tabel(["Kenmerk", "Wat het is", "Voorbeeld"], [
                ["richting", "de rechte waarop hij ligt", "de noord-zuidlijn"],
                ["zin", "welke van de twee kanten op die rechte", "naar het noorden of naar het zuiden"],
                ["grootte (norm)", "hoe lang de pijl is", "5 newton"],
            ])),
            ("p", "Richting en zin zijn dus niet hetzelfde: twee vectoren op dezelfde rechte maar tegengesteld "
                  "gericht hebben <em>dezelfde richting</em> en een <em>tegengestelde zin</em>."),
            ("p", "Twee vectoren zijn <strong>gelijk</strong> als ze dezelfde richting, zin en grootte hebben, "
                  "ook al liggen ze ergens anders in het vlak. Een vector heeft geen vast aangrijpingspunt."),
            ("p", "De <strong>nulvector</strong> is de vector met grootte nul; hij heeft geen richting en "
                  "geen zin. Een <strong>eenheidsvector</strong> is een vector met grootte precies 1."),
        ]),
        dict(kop="Rekenen met vectoren", blokken=[
            ("p", "Met <strong>coördinaten</strong> wordt rekenen eenvoudig. De <strong>norm</strong> (de "
                  "grootte) van een vector (x, y) is √(x² + y²): dat is Pythagoras."),
            ("p", tabel(["Vector", "Berekening", "Norm"], [
                ["(3, 4)", "√(9 + 16)", "5"],
                ["(−6, 8)", "√(36 + 64)", "10"],
                ["(5, 12)", "√(25 + 144)", "13"],
            ])),
            ("p", "Een norm is een lengte en kan dus <strong>nooit negatief</strong> zijn."),
            ("p", "<strong>Optellen</strong> doe je componentsgewijs: je telt de x'en bij elkaar en de y's bij "
                  "elkaar op. Grafisch teken je de som met de <strong>kop-staartmethode</strong>: zet de "
                  "staart van de tweede vector aan de kop van de eerste, en de som loopt van de eerste staart "
                  "naar de tweede kop. (Met de parallellogrammethode kom je op hetzelfde uit.)"),
            ("p", "De <strong>vector van A naar B</strong> vind je door de coördinaten van A van die van B af "
                  "te trekken. Van A(1, 2) naar B(4, 7) is dat (3, 5). Van A(2, 3) naar B(7, 3) is dat (5, 0), "
                  "met norm 5."),
            ("p", "De <strong>formule van Chasles-Möbius</strong> zegt dat je een vector van A naar B mag "
                  "opsplitsen via elk tussenpunt: de vector van A naar B is de vector van A naar C plus die "
                  "van C naar B. Handig om een omweg in stukken te knippen."),
            ("p", "Een vector <strong>met een getal vermenigvuldigen</strong> maakt hem langer of korter maar "
                  "verandert de richting niet. Bij een <strong>negatief</strong> getal draait wel de "
                  "<em>zin</em> om: maal min 2 wordt de vector dubbel zo lang en wijst hij de andere kant op."),
            ("kader", "<strong>De som van twee vectoren is niet altijd langer dan elk van de twee.</strong> "
                      "Wijzen ze tegen elkaar in, dan heffen ze elkaar gedeeltelijk of helemaal op. Twee "
                      "gelijke vectoren met tegengestelde zin geven samen de nulvector."),
        ]),
        dict(kop="Vectoren in de natuurkunde", blokken=[
            ("p", "Werken twee krachten van 3 en 4 newton <strong>loodrecht</strong> op elkaar, dan is de "
                  "<strong>resulterende kracht</strong> √(9 + 16) = 5 newton. De kop-staartmethode maakt er "
                  "een rechthoekige driehoek van, en dan is het gewoon Pythagoras."),
            ("p", "Een vector <strong>ontbinden in zijn componenten</strong> is het omgekeerde: je splitst één "
                  "vector op in een horizontaal en een verticaal stuk. Zo reken je bij een helling uit welk "
                  "deel van de zwaartekracht langs de helling trekt en welk deel erin drukt."),
        ]),
    ],
    onthoud=[
        "De hoeken van elke driehoek zijn samen 180 graden.",
        "Elke zijde is kleiner dan de twee andere samen; 3, 4 en 9 kan dus niet.",
        "Cosinusregel a² = b² + c² − 2bc·cos α: bij twee zijden met de hoek ertussen, of bij drie zijden.",
        "Bij een rechte hoek valt de laatste term weg en blijft Pythagoras over.",
        "Sinusregel a/sin α = b/sin β = c/sin γ, geldig in elke driehoek.",
        "In een stomphoekige driehoek heeft sin α = k twee mogelijke hoeken: kijk welke past.",
        "Een vector heeft richting, zin en grootte; richting is de rechte, zin is de kant.",
        "De norm van (x, y) is √(x² + y²) en is nooit negatief.",
        "Vector van A naar B: coördinaten van B min die van A.",
        "Chasles-Möbius: AB is AC plus CB, via elk tussenpunt.",
        "Maal een negatief getal draait de zin om, niet de richting.",
    ],
)


# ───────────────────────── 8. Formules omvormen en eerstegraadsvergelijkingen
BUNDELS["formules-omvormen-en-eerstegraadsvergelijkingen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Formules omvormen en eerstegraadsvergelijkingen",
    onder="Termen en factoren, haakjes uitwerken en ontbinden, vergelijkingen en ongelijkheden oplossen, en formules naar een andere letter omvormen.",
    secties=[
        dict(kop="Termen en factoren", blokken=[
            ("p", "Een <strong>term</strong> is een stuk dat door een plus of een min van de rest gescheiden "
                  "is; een <strong>factor</strong> is een stuk dat vermenigvuldigd wordt. In 3x + 5y zijn 3x "
                  "en 5y de twee termen; in 3xy zijn 3, x en y de factoren."),
            ("p", "<strong>Gelijksoortige termen</strong> hebben precies dezelfde letters met dezelfde "
                  "exponenten. Alleen die mag je samennemen: 3x + 5x is 8x, maar 3x + 5y blijft staan zoals "
                  "het staat, en 3x + 3x² ook."),
            ("p", "De <strong>graad</strong> van een vergelijking is de hoogste exponent van de onbekende. "
                  "Een formule is <strong>lineair in x</strong> als x enkel in de <strong>eerste macht</strong> "
                  "voorkomt, dus zonder kwadraat en zonder wortel. Een lineair verband tussen twee grootheden "
                  "geeft een <strong>rechte</strong> als grafiek."),
        ]),
        dict(kop="Haakjes uitwerken", blokken=[
            ("p", "Met de distributieve eigenschap: elke term binnen de haakjes wordt met de factor ervoor "
                  "vermenigvuldigd."),
            ("p", tabel(["Uitdrukking", "Uitgewerkt"], [
                ["3(x + 4)", "3x + 12"],
                ["2(x + 4)", "2x + 8"],
                ["−2(x − 5)", "−2x + 10"],
                ["(x + 3)(x + 2)", "x² + 5x + 6"],
                ["(x + 3)²", "x² + 6x + 9"],
                ["(x − 3)²", "x² − 6x + 9"],
                ["(x + 3)(x − 3)", "x² − 9"],
            ])),
            ("kader", "<strong>Let op het minteken vóór de haakjes.</strong> Bij −2(x − 5) verandert élke "
                      "term van teken: je krijgt −2x + 10 en niet −2x − 10. Dat is de fout die het vaakst "
                      "gemaakt wordt."),
            ("p", "De laatste drie regels zijn de <strong>merkwaardige producten</strong>: "
                  "(a + b)² = a² + 2ab + b², (a − b)² = a² − 2ab + b², en (a + b)(a − b) = a² − b². Je herkent "
                  "ze zowel om uit te werken als om te ontbinden."),
        ]),
        dict(kop="Ontbinden in factoren", blokken=[
            ("p", "Ontbinden is het omgekeerde van uitwerken: van een som een product maken."),
            ("p", tabel(["Techniek", "Voorbeeld", "Ontbonden"], [
                ["gemeenschappelijke factor", "6x + 9", "3(2x + 3)"],
                ["verschil van twee kwadraten", "x² − 16", "(x + 4)(x − 4)"],
                ["volkomen kwadraat", "x² + 10x + 25", "(x + 5)²"],
            ])),
            ("p", "Ontbinden is nuttig omdat een <strong>product nul is zodra één factor nul is</strong>."),
        ]),
        dict(kop="De eigenschappen van gelijkheden", blokken=[
            ("p", "Een vergelijking is een <strong>balans</strong>: <strong>wat je links doet, moet je rechts "
                  "ook doen, anders klopt de gelijkheid niet meer</strong>. Je mag bij beide leden hetzelfde "
                  "optellen of aftrekken, en beide leden met hetzelfde getal vermenigvuldigen of erdoor delen."),
            ("p", "Vermenigvuldig je beide leden met <strong>min 1</strong>, dan blijft de gelijkheid gewoon "
                  "kloppen: alle tekens draaien om, links én rechts."),
            ("kader", "<strong>Wat nooit mag: beide leden delen door nul.</strong> En dus ook niet delen door "
                      "een <em>letter</em> waarvan je niet weet of ze nul is: daarmee laat je stiekem een "
                      "oplossing verdwijnen."),
        ]),
        dict(kop="Een vergelijking oplossen", blokken=[
            ("p", tabel(["Stap", "Wat je doet"], [
                ["1", "haakjes uitwerken"],
                ["2", "noemers wegwerken door met de kleinste gemene veelvoud te vermenigvuldigen"],
                ["3", "alle termen met x naar links, alle getallen naar rechts"],
                ["4", "gelijksoortige termen samennemen"],
                ["5", "delen door de coëfficiënt van x"],
                ["6", "de oplossing invullen in de oorspronkelijke vergelijking om te controleren"],
            ])),
            ("p", tabel(["Vergelijking", "Tussenstap", "Oplossing"], [
                ["3x + 5 = 20", "3x = 15", "x = 5"],
                ["5x − 3 = 12", "5x = 15", "x = 3"],
                ["2x − 7 = x + 3", "x = 10", "x = 10"],
                ["2(x + 4) = 18", "2x + 8 = 18", "x = 5"],
                ["x/3 + 2 = 5", "x/3 = 3", "x = 9"],
            ])),
            ("p", "Een eerstegraadsvergelijking heeft dus <strong>niet altijd precies één</strong> oplossing. "
                  "Komt er <strong>0 = 0</strong> uit, dan is élke waarde van x een oplossing; komt er "
                  "<strong>0 = 5</strong> uit, dan heeft de vergelijking <strong>geen</strong> oplossing."),
            ("p", "<strong>Grafisch oplossen</strong> kan ook: teken het linkerlid en het rechterlid elk als "
                  "een functie en zoek het <strong>snijpunt</strong>. De x-waarde van dat snijpunt is de "
                  "oplossing."),
        ]),
        dict(kop="Nulwaarden en tekenverloop", blokken=[
            ("p", "De <strong>nulwaarde</strong> van een functie is de x-waarde waarvoor de functiewaarde nul "
                  "is. De oplossing van <strong>f(x) = 0</strong> is dus precies de x-waarde waar de grafiek "
                  "de <strong>x-as snijdt</strong>."),
            ("p", "De oplossing van <strong>f(x) > 0</strong> lees je af uit het "
                  "<strong>tekenverloop</strong>: waar staat de functie positief? Zo wordt een ongelijkheid "
                  "een vraag over de grafiek."),
        ]),
        dict(kop="Ongelijkheden", blokken=[
            ("p", "Een <strong>ongelijkheid</strong> los je op zoals een vergelijking, met één extra regel: "
                  "<strong>vermenigvuldig of deel je door een negatief getal, dan draait het teken om</strong>. "
                  "Bij delen door een <em>positief</em> getal gebeurt er niets met het teken."),
            ("p", "Uit −3x > 9 volgt dus x < −3, en uit −2x > 6 volgt x < −3."),
            ("p", "De <strong>oplossingenverzameling</strong> van een ongelijkheid noteer je meestal als een "
                  "<strong>interval</strong>:"),
            ("p", tabel(["Ongelijkheid", "In woorden", "Als interval"], [
                ["x ≥ 3", "alle x groter dan of gelijk aan 3", "[3, +∞["],
                ["x ≤ 4", "alle x kleiner dan of gelijk aan 4", "]−∞, 4]"],
                ["x < −3", "alle x kleiner dan min 3", "]−∞, −3["],
            ])),
        ]),
        dict(kop="Formules omvormen", blokken=[
            ("p", "Een formule omvormen is hetzelfde spel, maar met letters: je isoleert de letter die je "
                  "zoekt. Werk van buiten naar binnen: eerst de breuk weg, dan de optelling, dan de "
                  "vermenigvuldiging, en pas op het einde de wortel of het kwadraat."),
            ("p", tabel(["Formule", "Wat het is", "Omgevormd"], [
                ["ρ = m / V", "massadichtheid is massa gedeeld door volume", "m = ρ · V"],
                ["U = I · R", "de wet van Ohm: spanning is stroom maal weerstand", "R = U / I"],
                ["F = m · g", "de zwaartekracht is massa maal valversnelling", "m = F / g"],
                ["p = F / A", "druk is kracht gedeeld door oppervlakte", "A = F / p"],
                ["x = x₀ + v · t", "eenparig rechtlijnige beweging", "t = (x − x₀) / v"],
                ["c = n / V", "molaire concentratie is aantal mol per volume", "V = n / c"],
                ["F = k · u", "veerkracht is veerconstante maal uitrekking", "u = F / k"],
                ["O = z²", "de oppervlakte van een vierkant", "z = √O, de vierkantswortel van O"],
                ["y = ax + b", "de eerstegraadsfunctie", "x = (y − b) / a"],
            ])),
            ("p", "Met die omgevormde formules reken je meteen: 3 liter water met een dichtheid van 1 kg per "
                  "liter weegt <strong>3 kg</strong>; bij 12 volt en 3 ampère is de weerstand "
                  "12 : 3 = <strong>4 ohm</strong>; een vierkant met oppervlakte 49 heeft een zijde van "
                  "<strong>7</strong>."),
            ("p", "Uit p = F / A lees je ook af wat er gebeurt als je de <strong>oppervlakte kleiner</strong> "
                  "maakt bij dezelfde kracht: de <strong>druk wordt groter</strong>. Daarom prikt een naald "
                  "wel en een vingertop niet."),
            ("kader", "Niet elke formule is lineair. Bij de <strong>kinetische energie</strong>, "
                      "E = ½ · m · v², staat de snelheid in het <strong>kwadraat</strong>. Verdubbelt de "
                      "snelheid, dan wordt de energie <strong>vier</strong> keer zo groot. De energie is dus "
                      "<em>niet</em> recht evenredig met de snelheid."),
            ("weetje", "Controleer je omvorming altijd met een <strong>getallenvoorbeeld</strong> dat je al "
                       "kent: een tekenfout of een verkeerde bewerking valt dan meteen op, en dat merk je "
                       "liever nu dan op het examen."),
        ]),
        dict(kop="Vraagstukken met één onbekende", blokken=[
            ("p", "Kies een onbekende, schrijf op waar ze voor staat, vertaal de zinnen in een vergelijking, "
                  "los op, en controleer of het antwoord bij het verhaal past."),
            ("p", "<em>De som van drie opeenvolgende getallen is 48.</em> Noem het kleinste x, dan zijn de "
                  "andere x + 1 en x + 2. Samen 3x + 3 = 48, dus x = 15 en de getallen zijn 15, 16 en 17."),
            ("p", "<em>Een taxi vraagt 4 euro opstap en 1,5 euro per kilometer.</em> Bij een rit van 19 euro "
                  "hoort de vergelijking <strong>4 + 1,5x = 19</strong>, dus 1,5x = 15 en x = <strong>10 "
                  "kilometer</strong>."),
            ("p", "<em>Twee abonnementen: A kost 20 euro plus 0,10 euro per minuut, B kost 8 euro plus 0,20 "
                  "euro per minuut. Vanaf wanneer is A goedkoper?</em> Zet ze gelijk: 20 + 0,10x = 8 + 0,20x "
                  "geeft 12 = 0,10x en dus x = 120. Vanaf <strong>meer dan 120 minuten</strong> is A "
                  "goedkoper. Het snijpunt van de twee rechten is precies het omslagpunt."),
        ]),
    ],
    onthoud=[
        "Alleen gelijksoortige termen mag je samennemen: 3x + 5x = 8x, maar 3x + 5y niet.",
        "Lineair in x betekent: x enkel in de eerste macht, dus de grafiek is een rechte.",
        "Bij een minteken voor de haakjes verandert elke term van teken.",
        "(a + b)² = a² + 2ab + b², (a − b)² = a² − 2ab + b², (a + b)(a − b) = a² − b².",
        "Wat je links doet, doe je rechts; delen door nul of door een letter die nul kan zijn mag nooit.",
        "0 = 0 betekent elke x is een oplossing; 0 = 5 betekent geen enkele.",
        "Grafisch oplossen: teken beide leden als functie en zoek het snijpunt.",
        "De nulwaarde is de x waar de grafiek de x-as snijdt; f(x) > 0 lees je uit het tekenverloop.",
        "Bij delen door een negatief getal draait het ongelijkheidsteken om; bij een positief niet.",
        "De oplossingenverzameling van een ongelijkheid noteer je als interval: x ≤ 4 wordt ]−∞, 4].",
        "Een formule omvormen: de gezochte letter isoleren, van buiten naar binnen.",
        "Controleer elke omvorming met een getallenvoorbeeld.",
        "E = ½mv²: bij dubbele snelheid vier keer zoveel energie, dus niet recht evenredig.",
    ],
)


# ───────────────────────── 9. Stelsels en tweedegraadsvergelijkingen
BUNDELS["stelsels-en-tweedegraadsvergelijkingen-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Stelsels en tweedegraadsvergelijkingen",
    onder="Twee vergelijkingen met twee onbekenden, en vergelijkingen waarin een kwadraat staat.",
    secties=[
        dict(kop="Wat is een stelsel?", blokken=[
            ("p", "Een <strong>stelsel</strong> van twee eerstegraadsvergelijkingen in twee onbekenden zijn "
                  "twee vergelijkingen die <strong>tegelijk</strong> moeten kloppen. De oplossing is dus geen "
                  "los getal maar een <strong>koppel</strong> (x, y) dat in allebei de vergelijkingen past."),
            ("p", "<strong>Grafisch</strong> is elke vergelijking een rechte, en de oplossing is hun "
                  "<strong>snijpunt</strong>. Daar liggen de drie mogelijke uitkomsten meteen voor je:"),
            ("p", tabel(["Grafisch", "Naam", "Aantal oplossingen"], [
                ["de rechten snijden in één punt", "bepaald stelsel", "precies één"],
                ["de rechten zijn evenwijdig, niet samenvallend", "strijdig stelsel", "geen"],
                ["de rechten vallen samen", "onbepaald stelsel", "oneindig veel"],
            ])),
            ("kader", "Grafisch oplossen laat je <strong>zien</strong> wat er gebeurt, maar geeft geen exact "
                      "antwoord: een snijpunt op (2,37; 1,84) lees je niet van een ruitjesblad. Voor het exacte "
                      "antwoord heb je een algebraïsche methode nodig."),
        ]),
        dict(kop="De drie algebraïsche methodes", blokken=[
            ("p", tabel(["Methode", "Wat je doet", "Handig als"], [
                ["substitutiemethode", "druk één onbekende uit en vul die in de andere vergelijking in",
                 "één vergelijking al y = … of x = … is"],
                ["combinatiemethode", "tel de vergelijkingen op of trek ze af zodat één onbekende wegvalt",
                 "de coëfficiënten mooi tegen elkaar wegvallen"],
                ["gelijkstellingsmethode", "druk in allebei dezelfde onbekende uit en stel de twee aan elkaar gelijk",
                 "allebei de vergelijkingen al naar dezelfde letter opgelost zijn"],
            ])),
            ("p", "Welke je kiest, maakt voor het antwoord niets uit: de <strong>drie methodes geven altijd "
                  "dezelfde oplossing</strong>. Ze verschillen alleen in hoeveel rekenwerk ze kosten."),
            ("p", "<strong>Substitutie in de praktijk.</strong> Bij y = 2x en x + y = 9 vul je 2x in voor y: "
                  "x + 2x = 9, dus 3x = 9 en x = 3, en dan y = 6. Bij y = 3x en x + y = 16 net zo: 4x = 16, "
                  "dus x = 4 en y = 12."),
            ("p", "<strong>Combinatie in de praktijk.</strong> Bij x + y = 10 en x − y = 2 tel je de twee "
                  "vergelijkingen op: de y valt weg en je houdt 2x = 12 over, dus x = 6 en y = 4. Bij "
                  "x + y = 12 en x − y = 4 geeft dat 2x = 16, dus x = 8."),
        ]),
        dict(kop="Wat een vreemd resultaat betekent", blokken=[
            ("p", "Verdwijnen tijdens het oplossen allebei de onbekenden, dan zegt wat overblijft je welk "
                  "soort stelsel je had:"),
            ("p", "komt er <strong>0 = 7</strong> uit (of iets anders dat niet klopt), dan is het stelsel "
                  "<strong>strijdig</strong> en is er geen enkele oplossing; komt er <strong>0 = 0</strong> "
                  "uit, dan is het <strong>onbepaald</strong> en zijn er oneindig veel oplossingen: de twee "
                  "rechten vallen samen."),
        ]),
        dict(kop="Vraagstukken met twee onbekenden", blokken=[
            ("p", "<em>Twee broden en drie koeken kosten 7 euro, één brood en drie koeken kosten 5 euro. Wat "
                  "kost een brood?</em> Noem b de prijs van een brood en k die van een koek. Dan is "
                  "2b + 3k = 7 en b + 3k = 5. Trek de tweede van de eerste af: de koeken vallen weg en je "
                  "houdt b = 2 over. Een brood kost dus 2 euro."),
            ("p", "Het patroon: twee onbekenden vragen om twee vergelijkingen. Schrijf eerst netjes op waar "
                  "elke letter voor staat."),
        ]),
        dict(kop="Tweedegraadsvergelijkingen", blokken=[
            ("p", "De <strong>standaardvorm</strong> is <strong>ax² + bx + c = 0</strong>, met a niet gelijk "
                  "aan nul. Een vergelijking heet <strong>onvolledig</strong> als b of c ontbreekt, zoals "
                  "x² − 9 = 0 of x² − 5x = 0. Die los je op zonder formule:"),
            ("p", tabel(["Vergelijking", "Aanpak", "Oplossingen"], [
                ["x² − 9 = 0", "x² = 9", "3 en −3"],
                ["x² = 49", "x² = 49", "7 en −7"],
                ["x² − 5x = 0", "x(x − 5) = 0", "0 en 5"],
            ])),
            ("p", "Daarachter zit één regel: <strong>is een product van twee factoren nul, dan is minstens "
                  "één van de factoren nul</strong>. Dat is waarom ontbinden zo nuttig is."),
        ]),
        dict(kop="De discriminant", blokken=[
            ("p", "De <strong>discriminant</strong> is <strong>D = b² − 4ac</strong>. Haar teken zegt hoeveel "
                  "reële oplossingen er zijn, nog vóór je ze berekent."),
            ("p", tabel(["Discriminant", "Aantal reële oplossingen", "De parabool"], [
                ["D > 0", "twee", "snijdt de x-as in twee punten"],
                ["D = 0", "één (een dubbele)", "raakt de x-as"],
                ["D < 0", "geen", "ligt helemaal naast de x-as"],
            ])),
            ("p", "Bij x² − 4x + 4 is D = 16 − 16 = 0, dus er is één oplossing: x = 2. Een "
                  "vierkantsvergelijking heeft dus <strong>niet altijd</strong> twee reële oplossingen."),
            ("p", "Is D groter dan of gelijk aan nul, dan geeft de formule de oplossingen: "
                  "x = (−b ± √D) / (2a)."),
            ("weetje", "De oplossingen van ax² + bx + c = 0 zijn precies de <strong>nulwaarden</strong> van "
                       "de parabool y = ax² + bx + c. Algebra en grafiek vertellen hetzelfde verhaal."),
        ]),
        dict(kop="Ontbinden en oplossen", blokken=[
            ("p", "De <strong>ontbinding</strong> van een uitdrukking geeft haar nulwaarden cadeau:"),
            ("p", tabel(["Uitdrukking", "Ontbinding", "Nulwaarden"], [
                ["x² − 16", "(x + 4)(x − 4)", "4 en −4"],
                ["x² + 6x + 9", "(x + 3)²", "−3 (dubbel)"],
                ["x² − 5x + 6", "(x − 2)(x − 3)", "2 en 3"],
            ])),
            ("kader", "<strong>x² + 9 is níét te ontbinden als (x + 3)(x − 3).</strong> Dat laatste geeft "
                      "uitgewerkt x² − 9. Alleen een <em>verschil</em> van twee kwadraten ontbindt zo; een "
                      "som van twee kwadraten heeft in de reële getallen geen nulwaarden."),
        ]),
        dict(kop="Toepassen en controleren", blokken=[
            ("p", "<em>Een rechthoek is 3 meter langer dan breed en heeft een oppervlakte van 40 vierkante "
                  "meter.</em> Noem de breedte x, dan is de lengte x + 3 en luidt de vergelijking "
                  "<strong>x(x + 3) = 40</strong>, dus x² + 3x − 40 = 0. De oplossingen zijn 5 en −8. De "
                  "breedte is dus <strong>5 meter</strong>."),
            ("p", "En daar zie je meteen waarom je de oplossingen altijd in het oorspronkelijke probleem "
                  "controleert: −8 is wiskundig een geldige oplossing van de vergelijking, maar een rechthoek "
                  "met een breedte van min 8 meter bestaat niet. Bij een omgevormde vergelijking kunnen er "
                  "bovendien oplossingen bij komen die in de oorspronkelijke vorm niet mogen, bijvoorbeeld "
                  "omdat je ergens door nul zou delen."),
            ("p", "<strong>Een ongelijkheid van de tweede graad.</strong> x² < 9 betekent dat x tussen −3 en "
                  "3 ligt: de oplossingenverzameling is het open interval ]−3, 3[. Wie hier alleen x < 3 "
                  "schrijft, vergeet de negatieve kant."),
        ]),
    ],
    onthoud=[
        "De oplossing van een stelsel is een koppel (x, y), niet één getal.",
        "Drie methodes: substitutie, combinatie en gelijkstelling; ze geven altijd hetzelfde antwoord.",
        "Bepaald is één snijpunt, strijdig is evenwijdig, onbepaald is samenvallend.",
        "0 = 7 betekent strijdig, 0 = 0 betekent onbepaald.",
        "Grafisch oplossen is aanschouwelijk maar niet exact.",
        "Standaardvorm ax² + bx + c = 0; onvolledig als b of c ontbreekt.",
        "Is een product nul, dan is minstens één factor nul.",
        "D = b² − 4ac: positief twee oplossingen, nul één, negatief geen.",
        "x² − 16 = (x + 4)(x − 4), maar x² + 9 ontbindt niet.",
        "De oplossingen zijn de nulwaarden van de bijhorende parabool.",
        "x² < 9 geeft ]−3, 3[, niet enkel x < 3.",
    ],
)


# ───────────────────────── 10. Functies en de rechte
BUNDELS["functies-en-de-rechte-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Functies en de rechte",
    onder="Het functiebegrip met domein en bereik, de vier voorstellingswijzen, en alles over de eerstegraadsfunctie.",
    secties=[
        dict(kop="Wat is een functie?", blokken=[
            ("p", "Een verband tussen twee grootheden is een <strong>functie</strong> als er bij elke x "
                  "<strong>hoogstens één</strong> y hoort. Eén invoer, één uitkomst. Op de grafiek betekent "
                  "dat: een <strong>verticale lijn</strong> mag de grafiek maar één keer snijden. Dat heet de "
                  "verticalelijntest, en daarom is een verticale rechte zelf géén functie."),
            ("p", "Omgekeerd mag het wél: dezelfde y bij verschillende x'en. Bij y = x² hoort y = 4 bij zowel "
                  "x = 2 als x = −2, en dat is prima."),
            ("p", "De <strong>onafhankelijke variabele</strong> kies je zelf en staat op de "
                  "<strong>horizontale</strong> as; de <strong>afhankelijke</strong> volgt eruit en staat op "
                  "de <strong>verticale</strong> as. Bij <em>de kost hangt af van het aantal kilometer</em> is "
                  "het aantal kilometer de onafhankelijke variabele."),
        ]),
        dict(kop="Functiewaarde, domein en bereik", blokken=[
            ("p", "<strong>f(4)</strong> lees je als <em>de functiewaarde in 4</em>: vul 4 in voor x. Voor "
                  "f(x) = 3x − 2 is f(4) = 10, en voor f(x) = 2x + 7 is f(5) = 17."),
            ("p", "De omgekeerde vraag is een vergelijking: <em>voor welke x is f(x) = 13?</em> Dan los je "
                  "3x − 2 = 13 op en vind je x = 5. Voor f(x) = 4x − 1 en f(x) = 11 vind je x = 3."),
            ("p", "Het <strong>domein</strong> is de verzameling van alle x-waarden waarvoor de functie een "
                  "waarde geeft. Het <strong>bereik</strong> is de verzameling van alle y-waarden die ze "
                  "aanneemt. Bij f(x) = 1/x is het domein alle reële getallen <strong>behalve nul</strong>, "
                  "want delen door nul mag niet."),
        ]),
        dict(kop="De vier voorstellingswijzen", blokken=[
            ("p", "Dezelfde functie kan er op vier manieren staan, en je moet van elke naar elke kunnen "
                  "overstappen: de <strong>verwoording</strong>, een <strong>tabel</strong>, een "
                  "<strong>grafiek</strong> en het <strong>voorschrift</strong>."),
            ("p", tabel(["Vorm", "Voorbeeld"], [
                ["verwoording", "je betaalt 5 euro opstap en 3 euro per kilometer"],
                ["tabel", "1 → 8, 2 → 11, 3 → 14"],
                ["grafiek", "een rechte die de y-as snijdt in 5 en per stap 3 stijgt"],
                ["voorschrift", "f(x) = 3x + 5"],
            ])),
            ("p", "Bij een <strong>grafiek</strong> hoort altijd een <strong>ijk</strong> op de assen: zonder "
                  "getallen op de assen kan je geen enkele waarde aflezen en toont de tekening alleen nog een "
                  "vorm."),
            ("p", "Uit een <strong>tabel</strong> lees je af wat voor groei het is. Bij 1 → 4, 2 → 7, 3 → 10 "
                  "komt er telkens 3 bij: dat is <strong>lineaire groei</strong>, met voorschrift 3x + 1. Bij "
                  "1 → 1, 2 → 4, 3 → 9 zijn de verschillen 3 en 5, dus <strong>niet lineair</strong>: hier "
                  "staat y = x²."),
        ]),
        dict(kop="De eerstegraadsfunctie", blokken=[
            ("p", "Het voorschrift <strong>f(x) = ax + b</strong> geeft altijd een <strong>rechte</strong>."),
            ("p", "<strong>a</strong> is de <strong>richtingscoëfficiënt</strong>: hoeveel y stijgt per "
                  "eenheid x. Is a = 3, dan gaat de rechte drie omhoog per stap naar rechts. Is a negatief, "
                  "dan <strong>daalt</strong> de rechte van links naar rechts. Is a nul, dan loopt ze "
                  "<strong>horizontaal</strong> en luidt het voorschrift y = b."),
            ("p", "<strong>b</strong> is de y-waarde waar de rechte de <strong>verticale as</strong> snijdt. "
                  "Vul x = 0 in en je houdt b over. Bij een taxirit is b de opstapprijs."),
            ("p", "Twee rechten zijn <strong>evenwijdig</strong> als hun richtingscoëfficiënten "
                  "<strong>gelijk</strong> zijn. (Staan ze loodrecht op elkaar, dan is het product van hun "
                  "richtingscoëfficiënten min één.)"),
        ]),
        dict(kop="Lineair of recht evenredig", blokken=[
            ("p", "Een verband is <strong>recht evenredig</strong> als een verdubbeling van de ene een "
                  "verdubbeling van de andere geeft. Het voorschrift is dan y = ax, dus <strong>zonder "
                  "b</strong>, en de rechte gaat <strong>door de oorsprong</strong>."),
            ("p", "Een verband is <strong>lineair</strong> zodra de grafiek een rechte is, met of zonder b. "
                  "Elk recht evenredig verband is dus lineair, maar niet omgekeerd: bij y = 2x + 5 betaal je "
                  "bij nul kilometer al 5 euro, en dan verdubbelt het totaal niet mee."),
        ]),
        dict(kop="De vergelijking van een rechte opstellen", blokken=[
            ("p", "De <strong>richtingscoëfficiënt uit twee punten</strong> is het verschil in y gedeeld door "
                  "het verschil in x:"),
            ("p", tabel(["Punten", "Verschil y op verschil x", "rico"], [
                ["(1, 2) en (4, 11)", "9 op 3", "3"],
                ["(2, 3) en (5, 12)", "9 op 3", "3"],
                ["(0, 5) en (2, 1)", "−4 op 2", "−2"],
            ])),
            ("p", "<strong>Met een rico en een punt.</strong> Ligt het punt op de y-as, zoals (0, 3), dan lees "
                  "je b meteen af: rico 2 geeft y = 2x + 3. Ligt het punt elders, zoals (1, 6) bij rico 4, dan "
                  "vul je in: 6 = 4 · 1 + b, dus b = 2 en y = 4x + 2."),
            ("p", "<strong>Twee punten volstaan</strong> om een rechte vast te leggen: bereken eerst de rico, "
                  "vul daarna één van de twee punten in om b te vinden."),
            ("p", "<strong>Snijpunt met de x-as.</strong> Stel y gelijk aan nul. Bij y = 2x − 8 geeft dat "
                  "x = 4, dus het punt (4, 0); het snijpunt met de y-as is (0, −8). Bij y = 3x − 12 ligt het "
                  "snijpunt met de x-as bij x = 4."),
        ]),
        dict(kop="Modellen uit de praktijk", blokken=[
            ("p", "De fiche noemt uitdrukkelijk een aantal situaties waarin een eerstegraadsfunctie het model is:"),
            ("p", tabel(["Situatie", "Model", "Wat a en b zijn"], [
                ["rechtlijnige beweging", "s = 18t + 5", "a is de snelheid, b de beginpositie"],
                ["vaste en variabele kosten", "k = 0,40n + 60", "a is de prijs per stuk, b de opstartkosten"],
                ["hydrostatische druk", "p = 0,1d + 1", "1 bar per 10 meter diepte, plus 1 bar lucht"],
                ["energiegebruik", "kost = prijs per kWh · verbruik + vast abonnement", "a is de eenheidsprijs"],
                ["lineaire afschrijving", "w = 20000 − 2000t", "a is het jaarlijkse verlies"],
            ])),
            ("p", "Een fietser aan 18 km/u die al 5 kilometer ver is: s = 18t + 5. Een drukkerij met 60 euro "
                  "opstartkosten en 0,40 euro per affiche: k = 0,40n + 60. Bij 30 meter diepte is de druk "
                  "1 + 3 = <strong>4 bar</strong>. Een machine van 20 000 euro die in tien jaar lineair tot "
                  "nul wordt afgeschreven, verliest <strong>2000 euro per jaar</strong> en is na vier jaar nog "
                  "12 000 euro waard."),
            ("kader", "Bij vaste én variabele kosten is de totale kost wél <strong>lineair</strong>, maar "
                      "<strong>niet recht evenredig</strong>: door de vaste kosten gaat de rechte niet door de "
                      "oorsprong, en tweemaal zoveel affiches kost dus geen tweemaal zoveel geld."),
        ]),
    ],
    onthoud=[
        "Functie: bij elke x hoogstens één y. Verticale lijn snijdt de grafiek maar één keer.",
        "Onafhankelijke variabele horizontaal, afhankelijke verticaal.",
        "Domein zijn de x-waarden, bereik zijn de y-waarden.",
        "Vier voorstellingswijzen: verwoording, tabel, grafiek, voorschrift.",
        "f(x) = ax + b: a is de richtingscoëfficiënt, b het snijpunt met de y-as.",
        "Rico uit twee punten: verschil in y gedeeld door verschil in x.",
        "Evenwijdige rechten hebben dezelfde richtingscoëfficiënt.",
        "Recht evenredig gaat door de oorsprong (y = ax); lineair hoeft dat niet.",
        "Lineaire groei: elke stap komt er hetzelfde bij.",
        "Snijpunt met de x-as: stel y gelijk aan nul.",
    ],
)


# ───────────────────────── 11. De parabool
BUNDELS["de-parabool-transformaties-en-functiekenmerken-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="De parabool, transformaties en functiekenmerken",
    onder="Nulwaarden, top en symmetrieas, het opbouwen van a(x − p)² + q, en de kenmerken van een functie aflezen.",
    secties=[
        dict(kop="De parabool", blokken=[
            ("p", "De grafiek van een <strong>tweedegraadsfunctie</strong> heet een <strong>parabool</strong>. "
                  "(De grafiek van f(x) = c/x heet een hyperbool; verwar die twee niet.)"),
            ("p", "Het teken van <strong>a</strong> bepaalt de opening: is a groter dan nul, dan opent de "
                  "parabool <strong>naar boven</strong>; is a kleiner dan nul, naar beneden. Daarom spiegelt "
                  "y = −x² de parabool y = x² om de horizontale as."),
            ("p", "De <strong>top</strong> is het hoogste of laagste punt. Opent de parabool naar beneden, dan "
                  "is de top het hoogste punt en dus het <strong>maximum</strong>; opent ze naar boven, dan is "
                  "de top het minimum en is er <strong>geen maximum</strong>, want ze loopt aan beide kanten "
                  "onbeperkt omhoog."),
            ("p", "De <strong>symmetrieas</strong> is de <strong>verticale</strong> rechte door de top. Bij "
                  "een top (4, −1) is dat de rechte x = 4. Een parabool is dus symmetrisch: twee punten met "
                  "dezelfde y-waarde liggen even ver van die as."),
        ]),
        dict(kop="Nulwaarden", blokken=[
            ("p", "Een <strong>nulwaarde</strong> is een x-waarde waarvoor f(x) = 0: op de grafiek is dat een "
                  "snijpunt met de x-as. Een parabool kan er <strong>twee, één of geen</strong> hebben."),
            ("p", tabel(["Functie", "Nulwaarden", "Waarom"], [
                ["f(x) = x² − 9", "twee: 3 en −3", "x² = 9"],
                ["f(x) = x² + 4", "geen", "x² + 4 is altijd groter dan nul"],
                ["f(x) = (x − 2)²", "één (dubbel): 2", "de parabool raakt de as"],
            ])),
            ("p", "De <strong>symmetrieas ligt precies in het midden tussen de twee nulwaarden</strong>. Bij "
                  "nulwaarden −2 en 6 is dat x = 2; bij nulwaarden 1 en 9 is dat x = 5."),
            ("p", "Het <strong>snijpunt met de verticale as</strong> vind je door x = 0 in te vullen. Bij "
                  "f(x) = x² − 2x − 8 is dat het punt (0, −8): gewoon de c."),
        ]),
        dict(kop="De vorm a(x − p)² + q", blokken=[
            ("p", "In deze vorm lees je de <strong>top meteen af</strong>: ze ligt in het punt "
                  "<strong>(p, q)</strong>."),
            ("p", tabel(["Voorschrift", "Top", "Let op"], [
                ["(x − 3)² + 5", "(3, 5)", "min in de haakjes, dus p is positief"],
                ["(x + 2)² − 7", "(−2, −7)", "x + 2 is x − (−2)"],
                ["(x − 6)² + 2", "(6, 2)", "de kleinste functiewaarde is 2"],
            ])),
            ("p", "Je bouwt deze grafiek stap voor stap op vanuit y = x²:"),
            ("p", tabel(["Wat er verandert", "Wat de grafiek doet"], [
                ["p", "schuift horizontaal; (x − 5)² gaat vijf naar RECHTS"],
                ["q", "schuift verticaal, omhoog bij positieve q"],
                ["a groter dan 1", "rekt verticaal uit: de parabool wordt smaller"],
                ["a tussen 0 en 1", "drukt samen: de parabool wordt breder"],
                ["a negatief", "spiegelt om de horizontale as"],
            ])),
            ("kader", "Het minteken in de haakjes is contra-intuïtief: <strong>(x − 5)² ligt vijf eenheden "
                      "rechts</strong> van x², niet links. Vul maar in: bij x = 5 is de waarde nul, en daar "
                      "ligt dus de top."),
        ]),
        dict(kop="De functiekenmerken", blokken=[
            ("p", "Van elke functie moet je een rij kenmerken kunnen aflezen uit haar grafiek of voorschrift:"),
            ("p", tabel(["Kenmerk", "Wat het is"], [
                ["domein", "de x-waarden waarvoor ze bestaat"],
                ["bereik", "de y-waarden die ze aanneemt"],
                ["nulwaarden", "waar de grafiek de x-as snijdt"],
                ["tekenverloop", "waar de functiewaarde positief, nul of negatief is"],
                ["verloopschema", "waar de functie stijgt en waar ze daalt"],
                ["extrema", "de grootste of kleinste functiewaarde"],
                ["symmetrie", "de as waarom de grafiek zichzelf spiegelt"],
            ])),
            ("p", "Het <strong>domein van elke veeltermfunctie</strong>, en dus ook van een parabool, is "
                  "<strong>alle reële getallen</strong>: je mag elk getal invullen."),
            ("p", "Het <strong>bereik</strong> wordt door de top begrensd. Bij f(x) = x² is dat alle getallen "
                  "groter dan of gelijk aan nul; bij g(x) = (x − 1)² + 4 alle getallen groter dan of gelijk "
                  "aan 4. Het bereik van een tweedegraadsfunctie is dus <strong>nooit</strong> de hele "
                  "verzameling van de reële getallen."),
            ("p", "<strong>Stijgen en dalen.</strong> Bij f(x) = x² − 4x ligt de top bij x = 2 en opent de "
                  "parabool naar boven, dus daalt ze <strong>links van x = 2</strong> en stijgt ze daarna. "
                  "Dat lees je af in het verloopschema, niet in het tekenverloop."),
            ("p", "Een <strong>extremum</strong> is een grootste of kleinste functiewaarde. Een parabool heeft "
                  "er precies één, namelijk in de top."),
        ]),
        dict(kop="De vormen op een rij", blokken=[
            ("p", tabel(["Voorschrift", "Grafiek", "Wat je er direct uit leest"], [
                ["f(x) = ax + b", "rechte", "rico a, snijpunt met de y-as b"],
                ["f(x) = ax²", "parabool met top in de oorsprong", "de opening"],
                ["f(x) = ax² + bx + c", "parabool", "het snijpunt met de y-as (de c)"],
                ["f(x) = a(x − p)² + q", "parabool", "de top (p, q)"],
                ["f(x) = a(x − x₁)(x − x₂)", "parabool", "de nulwaarden x₁ en x₂"],
                ["f(x) = c/x", "hyperbool met twee takken", "het omgekeerd evenredige verband"],
            ])),
            ("p", "Welke vorm het handigst is, hangt af van wat je zoekt: de <strong>productvorm</strong> "
                  "geeft de nulwaarden cadeau (een product is nul zodra één factor nul is, dus bij nulwaarden "
                  "2 en 5 hoort f(x) = (x − 2)(x − 5)), de <strong>topvorm</strong> geeft de top."),
            ("p", "Omgekeerd kan je uit een <strong>grafiek het voorschrift afleiden</strong>: lees de top af "
                  "voor p en q, en gebruik één ander punt om a te berekenen."),
        ]),
        dict(kop="De omgekeerd evenredige functie", blokken=[
            ("p", "Bij <strong>f(x) = 6/x</strong> blijft het <strong>product</strong> van x en y telkens 6: "
                  "verdubbelt x, dan halveert y. Dat is een <strong>omgekeerd evenredig</strong> verband."),
            ("p", "De grafiek is een <strong>hyperbool met twee takken</strong>: één bij de positieve, één bij "
                  "de negatieve x-waarden. Het getal <strong>nul hoort niet bij het domein</strong>, want je "
                  "mag niet door nul delen; de grafiek nadert de verticale as wel maar raakt hem nooit."),
            ("p", "Deze functie heeft <strong>geen nulwaarde</strong>: een breuk met een teller die niet nul "
                  "is, wordt zelf nooit nul."),
        ]),
    ],
    onthoud=[
        "De grafiek van een tweedegraadsfunctie is een parabool; die van c/x een hyperbool.",
        "a > 0 opent naar boven, a < 0 naar beneden.",
        "Bij a(x − p)² + q is de top (p, q); (x + 2)² geeft p = −2.",
        "(x − 5)² ligt vijf eenheden naar RECHTS.",
        "Een parabool heeft twee, één of geen nulwaarden.",
        "De symmetrieas is de verticale rechte door de top, in het midden tussen de nulwaarden.",
        "Domein van elke veeltermfunctie: alle reële getallen. Het bereik wordt door de top begrensd.",
        "Tekenverloop is positief of negatief; verloopschema is stijgen of dalen.",
        "Productvorm geeft de nulwaarden, topvorm geeft de top.",
        "Bij f(x) = c/x hoort x = 0 niet bij het domein en is er geen nulwaarde.",
    ],
)


# ───────────────────────── 12. Telproblemen
BUNDELS["telproblemen-met-boom-en-venndiagram-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Telproblemen met boom- en venndiagram",
    onder="Tellen met een boomdiagram en de productregel, en met een venndiagram, de somregel en de complementregel.",
    secties=[
        dict(kop="Het boomdiagram", blokken=[
            ("p", "Een <strong>boomdiagram</strong> toont alle mogelijke uitkomsten van keuzes die je na "
                  "elkaar maakt. Uit het beginpunt vertrekken <strong>evenveel takken als er keuzes zijn in "
                  "de eerste stap</strong>; elke tak splitst daarna opnieuw voor de tweede stap, en zo verder."),
            ("p", "Eén <strong>pad</strong> van boven naar onder is één volledige uitkomst. Daarom tel je de "
                  "paden en niet de takken: een tak is maar één keuze, een pad is de hele reeks. Een "
                  "boomdiagram toont elke uitkomst precies één keer, dus je hoeft niet op dubbels te letten."),
        ]),
        dict(kop="De productregel", blokken=[
            ("p", "Wat het boomdiagram je laat <em>zien</em>, zegt de <strong>productregel</strong> in één "
                  "zin: <strong>vermenigvuldig het aantal keuzes van elke stap met elkaar</strong>."),
            ("p", tabel(["Situatie", "Berekening", "Aantal"], [
                ["4 broeken en 6 truien", "4 · 6", "24"],
                ["5 truien en 3 broeken", "5 · 3", "15"],
                ["3 voorgerechten, 4 hoofdgerechten, 2 desserts", "3 · 4 · 2", "24"],
                ["drie cijferschijven met 0 tot 9", "10 · 10 · 10", "1000"],
                ["vier schijven met zes tekens", "6⁴", "1296"],
                ["twee dobbelstenen", "6 · 6", "36"],
                ["drie muntworpen", "2 · 2 · 2", "8"],
            ])),
            ("p", "Bij tien muntworpen zouden er 1024 paden zijn. Dat tekent niemand nog uit, en dan gebruik "
                  "je <strong>alleen</strong> nog de productregel: 2¹⁰. Een boomdiagram is dus niet voor "
                  "elk <strong>telprobleem</strong> de beste aanpak."),
        ]),
        dict(kop="Met of zonder terugleggen", blokken=[
            ("p", "Bij <strong>terugleggen</strong> blijft het aantal keuzes elke stap gelijk: elke tak "
                  "splitst telkens in evenveel takken. Bij <strong>trekken zonder terugleggen</strong> "
                  "<strong>daalt</strong> het aantal keuzes bij elke stap, want wat je getrokken hebt, ligt "
                  "eruit."),
            ("p", "Vijf lopers en drie plaatsen op het podium: wie goud haalt, kan geen zilver meer halen. "
                  "Dus 5 · 4 · 3 = <strong>60</strong> mogelijke volgordes."),
            ("weetje", "Bij twee dobbelstenen zijn er 36 uitkomsten, en in <strong>zes</strong> daarvan is de "
                       "som 7: 1-6, 2-5, 3-4 en die drie ook omgekeerd. Zeven is daarmee de som die het vaakst "
                       "valt, en daar draaien heel wat gezelschapsspelen op."),
        ]),
        dict(kop="Het venndiagram", blokken=[
            ("p", "Een <strong>venndiagram</strong> toont twee (of meer) groepen als kringen die elkaar "
                  "overlappen. De overlapping is de <strong>doorsnede</strong>: de elementen die in "
                  "<strong>allebei</strong> zitten. Alles samen heet de <strong>vereniging</strong>. Wat "
                  "<strong>buiten</strong> de kringen staat, voldoet aan geen van de twee voorwaarden."),
            ("p", "Zijn de groepen <strong>disjunct</strong>, dan hebben ze <strong>geen enkel element "
                  "gemeen</strong> en raken de kringen elkaar niet; hun doorsnede is leeg."),
            ("p", "Het werkt het vlotst als je <strong>eerst de doorsnede</strong> invult: de rest van elke "
                  "kring is dan het aantal van die groep min de doorsnede, en zo tel je niets dubbel."),
        ]),
        dict(kop="De somregel en de complementregel", blokken=[
            ("p", "De <strong>somregel</strong>: tel de twee groepen op en trek de doorsnede <strong>één "
                  "keer</strong> af. Wie in allebei zit, heb je anders twee keer geteld. Alleen bij "
                  "<strong>disjuncte</strong> groepen mag je gewoon optellen, want dan is er niets dubbel."),
            ("p", "De <strong>complementregel</strong>: het aantal dat <em>niet</em> aan de voorwaarde "
                  "voldoet is het <strong>geheel min</strong> het aantal dat er wel aan voldoet."),
            ("p", tabel(["Situatie", "Somregel", "Complement"], [
                ["25 leerlingen, 14 voetbal, 11 zwemmen, 5 allebei", "14 + 11 − 5 = 20", "25 − 20 = 5 doen niets"],
                ["40 leerlingen, 22 Frans, 18 Duits, 6 allebei", "22 + 18 − 6 = 34", "40 − 34 = 6 doen geen van beide"],
                ["30 leerlingen, 12 piano, 9 gitaar, 4 allebei", "12 + 9 − 4 = 17", "30 − 17 = 13 spelen niets"],
            ])),
            ("p", "Wil je weten hoeveel er <strong>enkel</strong> tot één groep horen, dan trek je de "
                  "doorsnede van die groep af. Bij 30 mensen, 18 vlees, 14 vis en 7 allebei eten er "
                  "14 − 7 = <strong>7</strong> enkel vis."),
            ("p", "Ook bij getallen werkt dit. Van 1 tot en met 20 zijn er 10 deelbaar door 2, 6 door 3 en 3 "
                  "door allebei (6, 12 en 18). Deelbaar door 2 <em>of</em> door 3 zijn er dus "
                  "10 + 6 − 3 = <strong>13</strong>."),
            ("kader", "Soms is het <strong>veel sneller te tellen wat er niet aan de voorwaarde voldoet</strong> "
                      "en dat van het geheel af te trekken. Bij <em>minstens één keer zes in vier worpen</em> "
                      "tel je liever de worpenreeksen zónder zes; dat is één berekening in plaats van vier."),
        ]),
        dict(kop="Welk diagram wanneer", blokken=[
            ("p", tabel(["Vraag", "Gereedschap"], [
                ["keuzes na elkaar", "boomdiagram en productregel"],
                ["overlappende groepen", "venndiagram en somregel"],
                ["hoeveel vallen erbuiten", "complementregel"],
            ])),
            ("p", "Een venndiagram is dus <strong>niet</strong> het gereedschap voor opeenvolgende keuzes, en "
                  "een boomdiagram is <strong>niet</strong> altijd de beste aanpak: bij veel stappen wordt de "
                  "tekening onhandelbaar en gebruik je enkel nog de regels."),
        ]),
    ],
    onthoud=[
        "Boomdiagram: elke tak is één keuze, elk pad is één volledige uitkomst.",
        "Productregel: vermenigvuldig het aantal keuzes van elke stap.",
        "Met terugleggen blijft het aantal keuzes gelijk, zonder terugleggen daalt het.",
        "Venndiagram: de overlapping is de doorsnede, alles samen is de vereniging.",
        "Disjunct betekent geen enkel element gemeen.",
        "Somregel: A + B min de doorsnede, één keer afgetrokken.",
        "Complementregel: het geheel min wie wel voldoet.",
        "Bij 'minstens één' is het vaak sneller het tegendeel te tellen.",
    ],
)


# ───────────────────────── 13. Statistiek
BUNDELS["statistiek-voorstellingen-centrum-en-spreiding-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Statistiek: voorstellingen, centrum en spreiding",
    onder="Soorten gegevens, frequentietabellen en diagrammen, en de maten voor centrum en spreiding.",
    secties=[
        dict(kop="Soorten gegevens", blokken=[
            ("p", tabel(["Soort", "Wat het is", "Voorbeeld"], [
                ["numeriek", "getallen waarmee je kan rekenen", "de lengte in centimeter"],
                ["categorisch, niet-geordend", "categorieën zonder volgorde", "haarkleur, gemeente, merk"],
                ["categorisch, geordend", "categorieën met een natuurlijke volgorde", "zeer goed, goed, zwak"],
            ])),
            ("p", "Gegevens staan <strong>niet-gegroepeerd</strong> (elke losse waarde apart) of "
                  "<strong>gegroepeerd</strong> in <strong>klassen</strong>. Bij veel verschillende waarden is "
                  "groeperen overzichtelijker. Het <strong>klassenmidden</strong> is het gemiddelde van de twee "
                  "grenzen: bij de klasse van 10 tot 20 is dat 15, bij 20 tot 30 is dat 25. Daarmee reken je "
                  "verder als je de losse waarden niet meer hebt."),
        ]),
        dict(kop="De frequentietabel", blokken=[
            ("p", "De <strong>absolute frequentie</strong> is hoeveel keer een waarde voorkomt. De "
                  "<strong>relatieve frequentie</strong> is welk deel van het geheel dat is, meestal in "
                  "procent: 10 fietsers op 25 leerlingen is 10/25 = <strong>40 %</strong>; 20 op 50 is ook "
                  "40 %. Alle relatieve frequenties samen geven <strong>100 %</strong>."),
        ]),
        dict(kop="De voorstellingen", blokken=[
            ("p", tabel(["Diagram", "Waarvoor", "Kenmerk"], [
                ["staafdiagram", "categorieën vergelijken", "de staven staan LOS van elkaar"],
                ["histogram", "gegevens in klassen", "de staven RAKEN elkaar"],
                ["cirkeldiagram", "het aandeel in één geheel", "alles samen is 100 %"],
                ["lijndiagram", "een verloop in de tijd", "de lijn toont stijging of daling"],
                ["boxplot", "spreiding in vijf getallen", "kleinste, drie kwartielen, grootste"],
                ["dotplot", "elke meting apart", "één punt per meting boven haar waarde"],
            ])),
            ("p", "Het verschil tussen een staafdiagram en een histogram zit in de ruimte tussen de staven: "
                  "bij <strong>klassen</strong> sluiten de intervallen op elkaar aan, dus raken de staven "
                  "elkaar. Bij losse categorieën niet."),
            ("p", "Een <strong>cirkeldiagram</strong> is niet geschikt voor een verloop in de tijd; daarvoor "
                  "neem je een lijndiagram. En bij veel categorieën wordt een cirkeldiagram onleesbaar."),
            ("p", "Een <strong>dotplot</strong> zet elke meting als een punt boven haar waarde. Zo zie je "
                  "meteen waar de waarden zich opstapelen en welke er ver vanaf liggen."),
        ]),
        dict(kop="De vorm van een verdeling", blokken=[
            ("p", "Een verdeling is <strong>symmetrisch</strong> als links en rechts van het midden ongeveer "
                  "evenveel ligt, en <strong>scheef</strong> als dat niet zo is. Bij een "
                  "<strong>rechtsscheve</strong> verdeling ligt het grootste deel links en loopt er een lange "
                  "staart naar rechts. Zo zien lonen eruit: veel mensen rond een gewoon loon, enkelen met heel "
                  "veel meer."),
            ("p", "Een <strong>uitschieter</strong> is een waarde die ver van de rest ligt. Ga altijd na of "
                  "het een meetfout is of een echte waarneming. Toont een dotplot twee "
                  "<strong>clusters</strong>, twee opstapelingen ver uit elkaar, dan zit er vaak een verborgen "
                  "verschil achter: twee klassen samen, twee toestellen, twee meetdagen."),
        ]),
        dict(kop="De centrummaten", blokken=[
            ("p", tabel(["Maat", "Hoe je ze vindt", "Voorbeeld"], [
                ["rekenkundig gemiddelde", "de som gedeeld door het aantal", "4, 8, 10, 14 geeft 36 : 4 = 9"],
                ["mediaan", "de middelste van de gerangschikte reeks", "3, 7, 8, 12, 20 geeft 8"],
                ["modus", "de waarde die het vaakst voorkomt", "2, 3, 3, 5, 9 geeft 3"],
            ])),
            ("p", "Bij een <strong>even</strong> aantal waarden is de mediaan het gemiddelde van de twee "
                  "middelste: bij 4, 6, 9 en 11 is dat 7,5."),
            ("p", "Een reeks kan <strong>twee modi</strong> hebben, als twee waarden even vaak én het vaakst "
                  "voorkomen. En de modus is de enige centrummaat die ook bij "
                  "<strong>categorische</strong> gegevens werkt: met haarkleuren kan je niet rekenen, maar je "
                  "kan wel tellen welke het vaakst voorkomt."),
            ("kader", "Het <strong>gemiddelde is gevoelig voor uitschieters</strong>, de mediaan niet. Bij "
                      "lonen trekken een paar heel hoge bedragen het gemiddelde omhoog, terwijl de mediaan "
                      "enkel kijkt wie in het midden staat. Alleen bij een symmetrische verdeling vallen de "
                      "twee ongeveer samen."),
        ]),
        dict(kop="De spreidingsmaten", blokken=[
            ("p", "Het centrum alleen zegt te weinig. Twee klassen kunnen hetzelfde gemiddelde hebben terwijl "
                  "de punten in de ene klas veel verder uit elkaar liggen. Daarvoor heb je een "
                  "<strong>spreidingsmaat</strong> nodig."),
            ("p", tabel(["Maat", "Wat ze is", "Gevoelig voor uitschieters?"], [
                ["variatiebreedte", "de grootste min de kleinste waarde", "ja, heel erg"],
                ["kwartielen", "de waarden die een kwart, de helft en drie kwart onder zich laten", "nee"],
                ["interkwartielafstand", "het derde kwartiel min het eerste", "nee"],
                ["standaardafwijking", "hoe ver de waarden gemiddeld van het gemiddelde liggen", "ja"],
            ])),
            ("p", "Het <strong>eerste kwartiel</strong> laat een kwart van de gegevens onder zich, het "
                  "<strong>tweede</strong> is de mediaan, het <strong>derde</strong> laat driekwart onder zich. "
                  "De <strong>interkwartielafstand</strong> is de breedte van de <strong>doos van de "
                  "boxplot</strong>, en die doos bevat precies de <strong>middelste helft</strong> van de "
                  "gegevens. Omdat de uiterste waarden erbuiten vallen, is die maat ongevoelig voor één "
                  "uitschieter, terwijl de variatiebreedte er meteen door opblaast."),
            ("p", "Een <strong>kleine standaardafwijking</strong> betekent dat de waarden dicht bij elkaar "
                  "liggen. Heeft klas A bij hetzelfde gemiddelde een grotere standaardafwijking dan klas B, "
                  "dan liggen in klas A de punten verder uit elkaar."),
        ]),
    ],
    onthoud=[
        "Numeriek is rekenbaar; categorisch is geordend (zeer goed, goed, zwak) of niet.",
        "Klassenmidden is het gemiddelde van de twee klassengrenzen.",
        "Absolute frequentie is het aantal, relatieve het aandeel; samen 100 %.",
        "Staafdiagram: staven los. Histogram: staven raken elkaar.",
        "Cirkeldiagram voor aandelen, lijndiagram voor verloop in de tijd.",
        "Boxplot: kleinste, drie kwartielen, grootste. De doos is de middelste helft.",
        "Gemiddelde is de som gedeeld door het aantal; mediaan is de middelste; modus komt het vaakst voor.",
        "Bij een even aantal is de mediaan het gemiddelde van de twee middelste.",
        "Het gemiddelde is gevoelig voor uitschieters, de mediaan niet.",
        "Interkwartielafstand is Q3 min Q1 en is ongevoelig voor uitschieters.",
        "De standaardafwijking meet hoe ver de waarden gemiddeld van het gemiddelde liggen.",
    ],
)


# ───────────────────────── 14. Misleiding en puntenwolk
BUNDELS["misleiding-met-cijfers-en-verbanden-in-een-puntenwolk-boost-doorstroom"] = dict(
    vak=VAK, niveau=BOOST, titel="Misleiding met cijfers, en verbanden in een puntenwolk",
    onder="Hoe een grafiek kan kloppen en toch liegen, en wat een correlatie wel en niet bewijst.",
    secties=[
        dict(kop="Procent en procentpunt", blokken=[
            ("p", "Een partij gaat van 20 naar 25 procent van de stemmen. Twee manieren om dat te zeggen, "
                  "allebei waar, en ze klinken heel verschillend:"),
            ("p", tabel(["Uitdrukking", "Berekening", "Resultaat"], [
                ["gegroeid met", "25 − 20", "5 procentpunt"],
                ["gegroeid met", "5 gedeeld door 20", "25 procent"],
            ])),
            ("p", "<strong>Procentpunt</strong> is het gewone verschil tussen twee percentages. "
                  "<strong>Procent</strong> is de groei ten opzichte van de beginwaarde. Van 12 naar 18 procent "
                  "is <strong>6 procentpunt</strong> — en 50 procent groei."),
            ("p", "Een krant schrijft liever <em>25 procent groei</em>: het getal klinkt indrukwekkender "
                  "terwijl de groei dezelfde is. Lees dus altijd welk van de twee woorden er staat."),
            ("kader", "<strong>Procenten van verschillende bedragen tel je niet op.</strong> Een prijs van "
                      "100 euro die 20 procent stijgt en daarna 20 procent korting krijgt, kost geen 100 euro "
                      "maar <strong>96</strong>: de korting van 24 euro geldt op de hogere prijs van 120."),
        ]),
        dict(kop="Wat een grafiek kan verbergen", blokken=[
            ("p", tabel(["Truc", "Wat je ziet", "Wat je moet nakijken"], [
                ["de as begint niet bij nul", "een minuscuul verschil lijkt enorm", "waar de verticale as begint"],
                ["de as is foutief geijkt", "gelijke afstanden, ongelijke sprongen", "of de stappen even groot zijn"],
                ["tekening in drie dimensies", "het oog vergelijkt volumes", "of de hoogtes wel kloppen"],
                ["gegevens weggelaten", "een mooie rechte lijn", "of er jaren of groepen ontbreken"],
                ["de verkeerde centrummaat", "een te rooskleurig midden", "of er uitschieters zijn, en of het gemiddelde of de mediaan past"],
            ])),
            ("p", "Bij een <strong>staafdiagram</strong> met een as die vlak onder de laagste waarde begint, lijkt een staafje van 98 twee keer zo "
                  "hoog als een staafje van 97. Bij stappen als 0, 10, 20, 50 en 100 op gelijke afstanden lijkt "
                  "een kromme plots recht. En bij blokken in perspectief lijkt een dubbel zo hoge staaf veel "
                  "meer dan dubbel zo groot, want het oog kijkt naar het volume."),
            ("p", "Toont een grafiek de verkoop van 2022 tot 2024 maar ontbreekt 2023, vraag je dan af waarom. "
                  "Net dat jaar kan de stijging tegenspreken."),
            ("p", "Een <strong>cirkeldiagram waarvan de delen samen 118 procent geven</strong> klopt niet, of "
                  "de delen overlappen elkaar. Eén geheel is honderd procent."),
        ]),
        dict(kop="Getallen zonder context", blokken=[
            ("p", "<strong>Een percentage zonder het aantal vertelt het halve verhaal.</strong> Vijftig "
                  "procent kan twee mensen op vier zijn of duizend op tweeduizend. Bij kleine aantallen "
                  "schommelt een percentage enorm."),
            ("p", "<em>Negen op de tien tandartsen raden dit aan.</em> De eerste vraag is: "
                  "<strong>hoeveel</strong> tandartsen zijn er bevraagd, en <strong>door wie</strong>? Tien "
                  "tandartsen die de fabrikant zelf koos, zeggen iets heel anders dan duizend willekeurige."),
            ("p", "Daarom hoort bij elke grafiek de <strong>bron</strong>: zo kan de lezer de cijfers nagaan "
                  "en zien wie ze verzamelde. Wie de cijfers verzamelt, heeft vaak ook belang bij de uitkomst."),
        ]),
        dict(kop="De puntenwolk", blokken=[
            ("p", "In een <strong>spreidingsdiagram</strong> (ook <strong>puntenwolk</strong> genoemd) zet je "
                  "<strong>twee variabelen tegen elkaar uit, met één punt per waarneming</strong>. Zo zie je "
                  "of er een verband is."),
            ("p", "De <strong>trendlijn</strong> is de rechte die de vorm van de wolk het best samenvat. Ze "
                  "gaat meestal <strong>door geen enkel punt precies</strong>, maar ligt er zo dicht mogelijk "
                  "bij."),
            ("p", "Eén <strong>uitschieter</strong> ver van de wolk kan die lijn flink naar zich toe trekken. "
                  "Ga dus ook hier na of dat punt een meetfout is of een echte waarneming."),
            ("p", "<strong>Ver buiten het gemeten gebied voorspellen</strong> is riskant: daar kan het verband "
                  "er heel anders uitzien. Een groei die tien jaar rechtlijnig was, hoeft dat de volgende tien "
                  "jaar niet te blijven."),
        ]),
        dict(kop="De correlatiecoëfficiënt", blokken=[
            ("p", "De <strong>correlatiecoëfficiënt</strong> ligt altijd <strong>tussen min 1 en 1</strong>. "
                  "Het <strong>teken</strong> geeft de richting, het <strong>getal</strong> de sterkte."),
            ("p", tabel(["Waarde", "Wat ze betekent", "De wolk"], [
                ["1", "perfect positief verband", "alle punten op één stijgende rechte"],
                ["ongeveer 0,9", "sterk positief", "allebei stijgen mee"],
                ["ongeveer 0", "nauwelijks rechtlijnig verband", "punten zonder duidelijke richting"],
                ["ongeveer −0,9", "sterk negatief", "de ene daalt als de andere stijgt"],
                ["−1", "perfect negatief verband", "alle punten op één dalende rechte"],
            ])),
            ("p", "Bij een <strong>positieve</strong> correlatie loopt de wolk van linksonder naar "
                  "rechtsboven, bij een <strong>negatieve</strong> van linksboven naar rechtsonder."),
            ("p", "Een coëfficiënt dicht bij nul betekent dat er nauwelijks een <em>rechtlijnig</em> verband "
                  "is. Er kan nog altijd een ander soort verband zijn, bijvoorbeeld een gebogen."),
        ]),
        dict(kop="Correlatie is geen oorzaak", blokken=[
            ("p", "Twee zaken kunnen samen bewegen zonder dat de ene de andere veroorzaakt. Er kan een "
                  "<strong>derde factor</strong> achter zitten, of het verband kan omgekeerd lopen."),
            ("p", tabel(["Waarneming", "De echte verklaring"], [
                ["meer ooievaars, meer geboortes", "grotere landelijke gemeenten hebben meer van allebei"],
                ["meer ijsverkoop, meer verdrinkingen", "warm weer, want dan eet en zwemt iedereen meer"],
            ])),
            ("p", "Hoe je het dan wél zegt: <em>wie meer studeert, haalt in deze groep meestal hogere "
                  "punten</em>. Je beschrijft wat je ziet, in de groep die je gemeten hebt, zonder een "
                  "oorzaak te beweren. Een sterke correlatie bewijst geen oorzakelijk verband."),
        ]),
    ],
    onthoud=[
        "Procentpunt is het verschil tussen twee percentages, procent is de groei ten opzichte van het begin.",
        "20 procent erbij en dan 20 procent korting brengt je op 96 procent, niet op 100.",
        "Kijk bij elke grafiek waar de verticale as begint en of de ijking gelijkmatig is.",
        "Een tekening in drie dimensies laat het oog volumes vergelijken in plaats van hoogtes.",
        "Een percentage zonder het aantal erachter vertelt maar het halve verhaal.",
        "Een spreidingsdiagram zet twee variabelen tegen elkaar, één punt per waarneming.",
        "De trendlijn vat de wolk samen en gaat vaak door geen enkel punt.",
        "De correlatiecoëfficiënt ligt tussen min 1 en 1; teken is richting, getal is sterkte.",
        "Correlatie is geen oorzakelijk verband: denk aan een derde factor.",
        "Ver buiten de gemeten waarden voorspellen is riskant.",
    ],
)

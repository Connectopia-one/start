# -*- coding: utf-8 -*-
"""De leerbundels bij samenleving en economie op 🌍 Beyond doorstroom.

Gebaseerd op de vakfiche `2027_samenleving_en_economie_3DODU`, geldig vanaf
1 januari 2027. Die ene fiche geldt voor acht studierichtingen van de
doorstroomfinaliteit — bedrijfswetenschappen, economie-wiskunde, humane
wetenschappen, Latijn-moderne talen, Latijn-wiskunde-wetenschappen, moderne
talen, welzijnswetenschappen en wetenschappen-wiskunde — en voor twee van de
dubbele finaliteit. Bijna elk kind in doorstroom heeft ze dus nodig.

Eén bundel per thema, niet per deel: deel 1 en deel 2 van hetzelfde thema
behandelen dezelfde leerstof, alleen met andere vragen. Kim laadt de bundel dus
twee keer op, één keer bij elk deel. Sinds 9 oktober 2026 zegt het platform dat
ook zelf onder de titel van het hoofdstuk, na een melding van een ouder die
dacht dat deel 1 en deel 2 hetzelfde hoofdstuk waren.

De afspraak: een bundel dekt élke vraag van zijn hoofdstuk, met dezelfde
woorden als de vraag. `python3 dekking.py ../../beyond/samenleving-en-economie.json`
doet daar het voorwerk voor; het nalezen gebeurt daarna vraag per vraag.

De bundelsleutels eindigen op "-beyond-doorstroom", de slug van de categorie.
Beheer → Leerstof leest die slug uit de bestandsnaam en zoekt dan enkel in die
categorie naar het hoofdstuk. Zonder dat zou "Identiteit" van hier kunnen
botsen met een gelijknamig hoofdstuk elders.

Drie dingen liggen vast en mogen door niemand aangevuld worden, want ze komen
woordelijk uit de fiche: de rijtjes van de overheidsinkomsten en -uitgaven, de
noodnummers (101, 112, 070 245 245 en 1733) en de stappen van de eerste hulp
en de reanimatie. Bij eerste hulp kan een verzonnen stap echt schaden.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import bundel, svg

VAK = "Samenleving en economie"
BEYOND = "🌍 Beyond doorstroom — 5de en 6de middelbaar"
tabel = bundel.tabel

BUNDELS = {}

# ───────────────────────── 1. Identiteit
BUNDELS["identiteit-de-lagen-de-factoren-en-het-wereldbeeld-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Identiteit: de lagen, de factoren en het wereldbeeld",
    onder="Wat identiteit is, uit welke lagen ze bestaat, wat haar vormt, en hoe je mens- en wereldbeeld erin meespelen.",
    secties=[
        dict(kop="Wat identiteit is", blokken=[
            ("p", "<strong>Identiteit</strong> is het geheel van wie iemand is, <strong>in verhouding tot "
                  "anderen</strong>. Die laatste woorden zijn niet versiering: de fiche noemt identiteit "
                  "uitdrukkelijk <strong>relationeel</strong>. Wie je bent, krijgt vorm in de omgang met de "
                  "mensen rond je, en niet alleen bij jou vanbinnen."),
            ("p", "Drie woorden beschrijven volgens de fiche hoe een identiteit in elkaar zit:"),
            ("p", tabel(["Woord", "Wat het betekent"], [
                ["relationeel", "ze krijgt vorm in de omgang met andere mensen"],
                ["gelaagd", "ze bestaat uit meerdere lagen samen"],
                ["dynamisch", "ze kan in de loop van je leven veranderen"],
            ])),
            ("kader", "Een identiteit <strong>ligt dus niet vast vanaf je geboorte</strong>. Verhuis je, maak "
                      "je nieuwe vrienden en kleed je je anders, dan is dat precies wat <strong>dynamisch</strong> "
                      "betekent."),
        ]),
        dict(kop="De twee soorten en hun lagen", blokken=[
            ("p", "De fiche onderscheidt <strong>twee</strong> soorten identiteit, niet meer: de "
                  "<strong>persoonlijke identiteit</strong> en de <strong>groepsidentiteit</strong>."),
            ("p", "De <strong>persoonlijke identiteit</strong> is verbonden met drie dingen: de "
                  "<strong>biologische aspecten</strong>, de <strong>persoonlijkheidstrekken</strong> en de "
                  "<strong>familiale achtergrond</strong>."),
            ("p", tabel(["Laag", "Wat eronder valt", "Voorbeeld"], [
                ["biologische aspecten", "alles wat met je lichaam zelf te maken heeft",
                 "geboren zijn met een hartafwijking"],
                ["persoonlijkheidstrekken", "trekken van je karakter", "van jongs af aan erg verlegen zijn"],
                ["familiale achtergrond", "het gezin waar je uit komt", "de jongste van drie zijn"],
            ])),
            ("p", "De <strong>groepsidentiteit</strong> heeft er ook drie: de <strong>regionale, nationale "
                  "en supranationale aspecten</strong>, de <strong>groepen waar je deel van uitmaakt</strong>, "
                  "en de <strong>subculturen waar je bij hoort</strong>. Wie zich in de eerste plaats "
                  "<strong>Europeaan</strong> noemt, zit bij het <strong>supranationale</strong> aspect: "
                  "supranationaal betekent boven het niveau van één land."),
            ("p", "Bij de <strong>groepen</strong> noemt de fiche met zoveel woorden "
                  "<strong>gendergerelateerde</strong>, <strong>sociaaleconomische</strong> en "
                  "<strong>levensbeschouwelijke</strong> groepen. Een <strong>subcultuur</strong> is een "
                  "kleinere groep met eigen gewoonten binnen een grotere cultuur, zoals een muziekscene of "
                  "een sportwereld: eigen taal, eigen gebruiken, binnen het grotere geheel."),
            ("kader", "Persoonlijke identiteit en groepsidentiteit staan <strong>niet</strong> los van elkaar: "
                      "ze beïnvloeden elkaar, en ook de lagen onderling beïnvloeden elkaar. Over die "
                      "wederzijdse invloed moet je kunnen reflecteren. <strong>Welke laag het meest bepalend "
                      "is, verschilt van persoon tot persoon</strong>; de fiche geeft daar geen vast antwoord op."),
        ]),
        dict(kop="Wat een identiteit vormt", blokken=[
            ("p", "De fiche noemt <strong>drie factoren</strong> die een identiteit vormen en beïnvloeden: "
                  "<strong>verbondenheid</strong>, <strong>discriminatie</strong> en "
                  "<strong>wij-zij-denken</strong>."),
            ("p", "<strong>Verbondenheid</strong> is het gevoel ergens bij te horen en erkend te worden. Wie "
                  "zich met een groep verbonden voelt, neemt iets van die groep mee in de eigen identiteit."),
            ("p", "<strong>Discriminatie</strong> is mensen <strong>anders behandelen om een kenmerk van hun "
                  "identiteit</strong>: gender, geloof, lichaam, afkomst. Wordt iemand op de sportclub nooit "
                  "gekozen omdat ze een hoofddoek draagt, dan is dat discriminatie. Ze "
                  "<strong>breekt het gevoel van verbondenheid af</strong> en kan het "
                  "<strong>wij-zij-denken versterken</strong>."),
            ("p", "<strong>Wij-zij-denken</strong> is mensen indelen in een eigen groep en een andere groep. "
                  "Dat komt <strong>niet altijd van buitenaf</strong>: een groep kan die scherpe grens ook "
                  "zelf trekken."),
        ]),
        dict(kop="Mensbeeld en wereldbeeld", blokken=[
            ("p", "Je <strong>mensbeeld</strong> is de manier waarop je naar de mens en zijn aard kijkt: is "
                  "de mens goed, vrij, verantwoordelijk? Je <strong>wereldbeeld</strong> is de manier waarop "
                  "je naar de wereld als geheel kijkt. Die twee hangen samen, maar ze zijn "
                  "<strong>niet hetzelfde</strong>."),
            ("p", "Mens- en wereldbeeld en identiteit <strong>bepalen elkaar in twee richtingen</strong>. De "
                  "fiche zegt het letterlijk: hoe het mens- en wereldbeeld de identiteit bepaalt en andersom. "
                  "En een wereldbeeld <strong>kan veranderen</strong>; over die verandering moet je kunnen "
                  "nadenken."),
        ]),
        dict(kop="Hoe het examen eruitziet", blokken=[
            ("p", "Je krijgt <strong>fictieve situaties</strong> in plaats van echte. Twee redenen staan in "
                  "de fiche: zo blijft het <strong>neutraal</strong> en zijn "
                  "<strong>persoonsgegevens beschermd</strong>. Dat betekent niet dat de actualiteit er niet "
                  "toe doet: je moet ze <strong>opvolgen op lokaal, regionaal en nationaal vlak</strong>."),
        ]),
    ],
    onthoud=[
        "Identiteit is het geheel van wie iemand is, in verhouding tot anderen.",
        "Drie woorden: relationeel, gelaagd en dynamisch.",
        "Twee soorten: de persoonlijke identiteit en de groepsidentiteit.",
        "Persoonlijk: biologische aspecten, persoonlijkheidstrekken en familiale achtergrond.",
        "Groep: regionaal, nationaal en supranationaal, de groepen, en de subculturen.",
        "Een subcultuur is een kleinere groep met eigen gewoonten binnen een grotere cultuur.",
        "Drie factoren: verbondenheid, discriminatie en wij-zij-denken.",
        "Discriminatie behandelt mensen anders om een kenmerk van hun identiteit.",
        "Mensbeeld gaat over de mens, wereldbeeld over de wereld; ze bepalen de identiteit en andersom.",
        "De situaties op het examen zijn fictief, om neutraliteit en persoonsgegevens te beschermen.",
    ],
)

# ───────────────────────── 2. Samenleven in diversiteit
BUNDELS["samenleven-in-diversiteit-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Samenleven in diversiteit",
    onder="Vijf vormen van diversiteit, vijf begrippen om erover te praten, en wat samenleven in diversiteit oplevert en vraagt.",
    secties=[
        dict(kop="Wat diversiteit is", blokken=[
            ("p", "<strong>Diversiteit</strong> is de <strong>verscheidenheid die er tussen mensen "
                  "bestaat</strong>: het gegeven dat mensen van elkaar verschillen, op heel veel vlakken "
                  "tegelijk. De fiche noemt <strong>vijf vormen</strong>."),
            ("p", tabel(["Vorm", "Waarover ze gaat", "Voorbeeld"], [
                ["lichaamsdiversiteit", "alle verschillen in lichaam, ook beperkingen",
                 "een ploeg met heel verschillende lichaamsbouw, met en zonder beperking"],
                ["sociale diversiteit", "verschillen in sociale en economische positie",
                 "twee kinderen in dezelfde klas met heel verschillende financiële omstandigheden"],
                ["culturele diversiteit", "verschillen in gewoonten, taal en gebruiken", "feesten die niet iedereen viert"],
                ["religieuze of levensbeschouwelijke diversiteit", "verschillen in geloof én in niet-geloven",
                 "leden die katholiek, moslim, atheïst of zoekend zijn"],
                ["seksuele diversiteit", "verschillen in seksuele oriëntatie", "koppels van verschillende samenstelling"],
            ])),
            ("kader", "De fiche schrijft <strong>religieuze of levensbeschouwelijke diversiteit</strong>, met "
                      "een schuine streep ertussen. Dat tweede woord is er niet voor niets: <strong>ook wie "
                      "niet gelooft, heeft een levensbeschouwing</strong>, en hoort dus bij deze vorm."),
        ]),
        dict(kop="Vijf begrippen om over samenleven te praten", blokken=[
            ("p", tabel(["Begrip", "Wat het betekent"], [
                ["multiculturalisme", "meerdere culturen die naast elkaar bestaan in één samenleving"],
                ["monoculturalisme", "het idee dat één cultuur in de samenleving de norm is"],
                ["integratie", "de nieuwkomer past zich aan de bestaande groep aan"],
                ["inclusie", "de groep past zich mee aan, zodat iedereen echt kan meedoen"],
                ["exclusie", "mensen buiten de groep of de samenleving houden"],
            ])),
            ("p", "<strong>Multi</strong> betekent veel, <strong>mono</strong> betekent één: die twee zijn "
                  "elkaars tegengestelde. <strong>Inclusie en exclusie</strong> zijn dat ook, en ze betekenen "
                  "dus zeker niet ongeveer hetzelfde: erbij halen tegenover buitensluiten."),
            ("p", "Het verschil tussen <strong>integratie</strong> en <strong>inclusie</strong> zit in de "
                  "vraag <strong>wie zich aanpast</strong>. Zegt een vereniging tegen een nieuw lid dat het "
                  "zich maar moet schikken naar de bestaande gewoonten, dan komt de aanpassing van één kant: "
                  "<strong>integratie</strong>. Bouwt een school een hellend vlak en past ze de lessen aan "
                  "zodat een leerling in een rolstoel alles kan volgen, dan verandert de omgeving zelf mee: "
                  "<strong>inclusie</strong>."),
        ]),
        dict(kop="Wat diversiteit oplevert", blokken=[
            ("p", "De fiche noemt <strong>drie voordelen</strong>, en niets anders: "
                  "<strong>culturele verrijking</strong>, het <strong>uitwisselen van ideeën</strong> en "
                  "<strong>economische uitwisseling</strong>."),
            ("p", "<strong>Culturele verrijking</strong> betekent dat je in contact komt met gewoonten en "
                  "kunst die je anders niet kende. Dat gaat over wat je erbij krijgt aan cultuur, "
                  "<strong>niet over geld</strong>. <strong>Economische uitwisseling</strong> is wel de "
                  "handel en het werk die ontstaan doordat mensen verschillende dingen meebrengen: andere "
                  "kennis, andere producten, andere contacten. Vraagt een vereniging elk nieuw lid om een "
                  "idee voor het jaarprogramma, dan gebruikt ze het <strong>uitwisselen van ideeën</strong>."),
        ]),
        dict(kop="Wat diversiteit vraagt", blokken=[
            ("p", "Daarnaast staan <strong>vijf uitdagingen</strong>: <strong>meningsverschillen</strong>, "
                  "<strong>verschillende belangen</strong>, <strong>verschillende referentiekaders</strong>, "
                  "het risico van <strong>groepsdenken</strong> en het risico van "
                  "<strong>uitsluiting</strong>."),
            ("p", "Een <strong>referentiekader</strong> is het geheel van ervaringen en waarden waarmee je "
                  "iets beoordeelt. Twee mensen kunnen <strong>dezelfde situatie heel anders zien</strong> "
                  "omdat ze van een ander kader vertrekken."),
            ("p", "<strong>Groepsdenken</strong> is dat een groep tot één mening komt omdat niemand nog "
                  "tegenspreekt. Durft in een werkgroep niemand nog iets anders voor te stellen omdat de "
                  "voorzitter al een richting gekozen heeft, dan is dat groepsdenken. Het is "
                  "<strong>geen voordeel</strong>: wie niets meer tegenspreekt, ziet de fouten niet."),
            ("p", "<strong>Verschillende belangen</strong> herken je als twee partijen iets anders willen van "
                  "hetzelfde goed: de ene buurtbewoner wil een speeltuin op het pleintje, de andere "
                  "parkeerplaatsen."),
            ("kader", "Een <strong>meningsverschil</strong> is in de fiche geen probleem maar een "
                      "<strong>uitdaging</strong>: het hoort bij samenleven in diversiteit. Het leerdoel "
                      "vraagt dan ook de <strong>twee kanten samen</strong>: toelichten hoe diversiteit "
                      "<strong>verrijkend én uitdagend</strong> is voor het samenleven. Niet kiezen tussen de "
                      "twee."),
        ]),
    ],
    onthoud=[
        "Diversiteit is de verscheidenheid die er tussen mensen bestaat.",
        "Vijf vormen: lichaams-, sociale, culturele, religieuze of levensbeschouwelijke en seksuele diversiteit.",
        "Levensbeschouwelijke diversiteit gaat ook over wie niet gelooft.",
        "Multiculturalisme tegenover monoculturalisme, inclusie tegenover exclusie.",
        "Bij integratie past de nieuwkomer zich aan, bij inclusie past de groep zich mee aan.",
        "Drie voordelen: culturele verrijking, uitwisselen van ideeën en economische uitwisseling.",
        "Vijf uitdagingen: meningsverschillen, belangen, referentiekaders, groepsdenken en uitsluiting.",
        "Een referentiekader is het geheel van ervaringen en waarden waarmee je iets beoordeelt.",
        "Groepsdenken: de groep komt tot één mening omdat niemand nog tegenspreekt.",
        "Het leerdoel vraagt beide kanten: diversiteit is verrijkend én uitdagend.",
    ],
)

# ───────────────────────── 3. Respectvol samenleven
BUNDELS["respectvol-samenleven-communicatie-grenzen-en-samenwerken-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Respectvol samenleven: communicatie, grenzen en samenwerken",
    onder="Constructief tegenover destructief, pesten en racisme herkennen, de zes kenmerken van geldige toestemming, en samenwerken.",
    secties=[
        dict(kop="Respectvol en constructief", blokken=[
            ("p", "Een <strong>sociale interactie verloopt respectvol</strong> als <strong>beide personen "
                  "rekening houden met elkaars grenzen</strong>. Respect betekent niet dat je het eens wordt, "
                  "maar dat je elkaars grenzen erkent."),
            ("p", "<strong>Constructieve communicatie</strong> brengt het gesprek en de relatie vooruit "
                  "(constructief komt van bouwen: na het gesprek staat er iets, ook als je het oneens "
                  "blijft). <strong>Destructieve communicatie</strong> breekt de ander of de relatie af."),
            ("p", "Zegt Milan in een discussie: <em>ik begrijp dat je dit anders ziet, maar ik maak me zorgen "
                  "over het tijdstip</em>, dan is dat <strong>constructief</strong>: hij benoemt zijn zorg "
                  "zonder de ander af te breken. <strong>Tegenspreken mag</strong>; het gaat erom hoe je het "
                  "doet. Een <strong>meningsverschil is dus niet hetzelfde als destructieve "
                  "communicatie</strong>, en een gevoelig onderwerp aansnijden evenmin."),
            ("p", "Bij een respectvolle en constructieve interactie hoort: <strong>rekening houden met de "
                  "grenzen van de ander</strong>, <strong>je eigen standpunt rustig kunnen uitleggen</strong> "
                  "en <strong>kunnen luisteren zonder meteen te oordelen</strong>. Altijd toegeven is geen "
                  "respect voor jezelf, en lost het meningsverschil niet op."),
        ]),
        dict(kop="Pesten, uitsluiting, discriminatie en racisme", blokken=[
            ("p", "De fiche vraagt dat je <strong>vier soorten situaties</strong> kan analyseren: "
                  "<strong>pestgedrag</strong>, <strong>uitsluiting</strong>, <strong>discriminatie</strong> "
                  "en <strong>racisme</strong>."),
            ("p", "<strong>Pesten</strong> is <strong>herhaald en gericht</strong> kwetsend gedrag tegen "
                  "dezelfde persoon. Wordt Yara in een groepschat <strong>elke dag</strong> belachelijk "
                  "gemaakt om haar stem, dan is dat pestgedrag. De <strong>herhaling en het "
                  "machtsverschil</strong> maken het verschil met een eenmalige ruzie: maken twee leerlingen "
                  "ruzie over een opdracht en praten ze het daarna uit, dan is dat een "
                  "<strong>meningsverschil dat constructief eindigt</strong>."),
            ("p", "<strong>Uitsluiting</strong> is iemand systematisch buiten de groep houden, bijvoorbeeld "
                  "één speler nooit laten meedoen aan de gesprekken en de activiteiten."),
            ("p", "<strong>Discriminatie</strong> is het bredere woord; <strong>racisme</strong> is "
                  "<strong>één vorm ervan</strong>, namelijk discriminatie op basis van "
                  "<strong>afkomst of huidskleur</strong>."),
            ("p", "De <strong>impact van pesten</strong> op het slachtoffer <strong>raakt het welzijn en kan "
                  "lang nawerken</strong>. En wie toekijkt zonder iets te doen, heeft wel degelijk een rol: "
                  "de fiche vraagt te beoordelen welke <strong>handelingsopties het meest helpend</strong> "
                  "zijn. Zie je een klasgenoot online uitgelachen worden, dan is <strong>het slachtoffer "
                  "steunen en de situatie melden</strong> het antwoord, niet wegkijken."),
            ("kader", "Je gedrag en je keuzes hebben <strong>gevolgen voor het welzijn van anderen</strong>, "
                      "en de fiche vraagt dat je die gevolgen voor jezelf én voor anderen kan beoordelen."),
        ]),
        dict(kop="De zes kenmerken van geldige toestemming", blokken=[
            ("p", "De fiche noemt <strong>zes</strong> kenmerken. Ontbreekt er één, dan is de toestemming "
                  "niet geldig."),
            ("p", tabel(["Kenmerk", "Wat het betekent", "Wat er misgaat"], [
                ["vrijwillig", "zonder druk, manipulatie, intimidatie of dwang",
                 "ja zeggen nadat de vrienden een halfuur aandrongen"],
                ["duidelijk", "expliciet of ondubbelzinnig kenbaar gemaakt", "niets zeggen en stil blijven"],
                ["geïnformeerd", "de persoon begrijpt waarvoor ze toestemming geeft", "niet weten waarover het gaat"],
                ["specifiek", "toestemming voor het ene is geen toestemming voor het andere",
                 "een ja voor de ene situatie uitbreiden naar een andere"],
                ["actueel", "ze geldt voor het huidige moment en de huidige situatie",
                 "de foto van vorige maand nu nog gebruiken"],
                ["bekwaam gegeven", "de persoon kan een vrije en bewuste keuze maken",
                 "iemand die zo ziek is dat hij het niet kan overzien"],
            ])),
            ("kader", "Twee gevolgen van <strong>actueel</strong>: toestemming van vorige week is geen "
                      "toestemming voor vandaag, en ze kan <strong>achteraf nog ingetrokken</strong> worden. "
                      "En <strong>stilzwijgen is nooit toestemming</strong>: dat botst met het kenmerk "
                      "duidelijk."),
            ("p", "<strong>Groepsdruk</strong> is de invloed van een groep die je tot iets brengt wat je "
                  "alleen niet zou doen. De fiche vraagt situaties rond <strong>grenzen, groepsdruk en de "
                  "invloed van anderen</strong> te analyseren."),
        ]),
        dict(kop="Formeel, informeel en samenwerken", blokken=[
            ("p", "Een <strong>formele context</strong> is een situatie met <strong>vaste regels en "
                  "verwachtingen</strong>, zoals een sollicitatie. Formeel gaat over de <strong>regels van de "
                  "situatie</strong>, niet over het middel dat je gebruikt. Stuur je een mail naar een "
                  "mogelijke werkgever, dan past een <strong>formele stijl met een correcte "
                  "aanspreking</strong>. In een <strong>informele context</strong> zijn de omgangsvormen "
                  "losser, maar er blijven verwachtingen, en <strong>respect geldt altijd</strong>."),
            ("p", "Aan een <strong>effectieve samenwerking</strong> dragen bij: <strong>duidelijke afspraken "
                  "over wie wat doet</strong>, <strong>elkaar op de hoogte houden van de voortgang</strong> en "
                  "<strong>elkaars sterke kanten gebruiken</strong>. De fiche vraagt te beoordelen welke "
                  "aanpak de samenwerking in een situatie <strong>het meest bevordert</strong>."),
        ]),
    ],
    onthoud=[
        "Respectvol: beide personen houden rekening met elkaars grenzen.",
        "Constructief brengt vooruit, destructief breekt af. Tegenspreken mag.",
        "Pesten is herhaald en gericht tegen dezelfde persoon; een eenmalige ruzie is dat niet.",
        "Racisme is discriminatie op basis van afkomst of huidskleur.",
        "Een omstaander heeft wel een rol: steunen en melden is het meest helpend.",
        "Zes kenmerken van toestemming: vrijwillig, duidelijk, geïnformeerd, specifiek, actueel, bekwaam gegeven.",
        "Stilzwijgen is geen toestemming, en toestemming kan ingetrokken worden.",
        "Groepsdruk brengt je tot iets wat je alleen niet zou doen.",
        "Een formele context heeft vaste regels en verwachtingen, zoals een sollicitatie.",
        "Samenwerken: duidelijke afspraken, de voortgang delen en elkaars sterke kanten gebruiken.",
    ],
)

# ───────────────────────── 4. Ongevallen en eerste hulp
BUNDELS["ongevallen-herkennen-en-eerste-hulp-geven-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Ongevallen herkennen en eerste hulp geven",
    onder="De vier noodnummers, de letsels en noodsituaties uit de fiche, en de zes basisprincipes naast de vier stappen.",
    secties=[
        dict(kop="De vier noodnummers", blokken=[
            ("p", "De fiche noemt <strong>vier</strong> nummers. Leer ze uit het hoofd: op het examen is dit "
                  "het soort vraag waar geen redenering bij helpt."),
            ("p", tabel(["Nummer", "Waarvoor", "Voorbeeld"], [
                ["101", "de politie", "een inbraak of een vechtpartij"],
                ["112", "de ziekenwagen én de brandweer", "iemand bloedt zwaar, of er is brand"],
                ["070 245 245", "het antigifcentrum", "een kind dronk een product uit de kelder"],
                ["1733", "de huisarts of de huisartsenwachtpost", "zondagavond, dringend maar geen levensgevaar"],
            ])),
            ("kader", "Twee valkuilen. <strong>101 is niet voor een ziekenwagen</strong>: wie zwaar bloedt, "
                      "heeft 112 nodig. En het antigifcentrum bel je bij een vergiftiging "
                      "<strong>zonder</strong> bewustzijnsverlies; is het kind bewusteloos, dan bel je "
                      "<strong>112</strong>. Het nummer 100 staat niet in de fiche."),
        ]),
        dict(kop="Letsels en noodsituaties", blokken=[
            ("p", "Bij <strong>botten, spieren en gewrichten</strong> noemt de fiche vier letsels: de "
                  "<strong>botbreuk</strong>, de <strong>kneuzing</strong>, de <strong>ontwrichting</strong> "
                  "en de <strong>verstuiking</strong>. Dat zijn vier <strong>verschillende</strong> dingen; "
                  "een kneuzing en een botbreuk zijn niet hetzelfde letsel."),
            ("p", tabel(["Letsel", "Wat er gebeurd is"], [
                ["ontwrichting", "een bot is uit het gewricht geschoven"],
                ["verstuiking", "de banden rond een gewricht zijn te ver uitgerekt"],
            ])),
            ("p", "Een <strong>verstuiking zit in de banden</strong>, een <strong>ontwrichting in de stand "
                  "van het bot</strong>. Valt iemand van een ladder en staat de arm in een vreemde hoek, dan "
                  "vermoed je een <strong>botbreuk of een ontwrichting</strong>."),
            ("p", "Bij <strong>wonden</strong> noemt de fiche er twee, en niet meer: de "
                  "<strong>huidwonde</strong> en de <strong>brandwonde</strong>."),
            ("p", "Bij de <strong>ongevallen en noodsituaties</strong> staan onder meer de "
                  "<strong>bloeding</strong>, de <strong>verslikking</strong>, de "
                  "<strong>verdrinking</strong> en de <strong>hart- en ademhalingsstilstand</strong>. Bij een "
                  "hart- en ademhalingsstilstand <strong>pompt het hart niet meer en valt de ademhaling "
                  "stil</strong>. Verslikt iemand zich en kan hij niet meer praten of hoesten, dan is dat een "
                  "<strong>noodsituatie</strong>. Uitdroging staat niet in dat rijtje."),
        ]),
        dict(kop="Zes basisprincipes", blokken=[
            ("p", "Let op het verschil tussen <strong>zes basisprincipes</strong> en <strong>vier "
                  "stappen</strong>. Die twee aantallen worden het vaakst door elkaar gehaald."),
            ("p", "De <strong>basisprincipes</strong> zijn de houding waarmee je hulp verleent:"),
            ("p", tabel(["Basisprincipe", "Wat het betekent"], [
                ["blijf rustig in een noodsituatie", "het eerste van de zes"],
                ["vermijd besmetting", "bescherm jezelf én het slachtoffer tegen overdracht van ziekten"],
                ["handel als eerste hulpverlener", "doe wat je kan tot de hulpdiensten er zijn"],
                ["zorg voor het comfort van het slachtoffer", "ook de houding en de warmte tellen mee"],
                ["verleen psychosociale hulp", "sta het slachtoffer bij met woorden en nabijheid"],
                ["houd rekening met emotionele reacties achteraf", "ook jij kan achteraf nog reageren"],
            ])),
            ("kader", "<strong>Vermijd besmetting</strong> gaat in twee richtingen: van jou naar het "
                      "slachtoffer en omgekeerd. En <strong>getuigen noteren</strong> hoort hier niet thuis: "
                      "dat gaat over een schadegeval en een verzekering."),
        ]),
        dict(kop="Vier stappen, in deze volgorde", blokken=[
            ("p", tabel(["Stap", "Wat je doet", "Waarom"], [
                ["1", "zorg voor veiligheid", "anders word jij het tweede slachtoffer"],
                ["2", "beoordeel de toestand van het slachtoffer", "pas als het veilig is, kijk je hoe hij eraan toe is"],
                ["3", "raadpleeg gespecialiseerde hulp", "zo is de ambulance onderweg terwijl jij verder helpt"],
                ["4", "verleen verdere eerste hulp", "je blijft helpen tot de hulpdiensten er zijn"],
            ])),
            ("p", "Staat er een auto midden op de rijweg met een gewonde erin, dan zorg je "
                  "<strong>eerst dat de plaats veilig is</strong>. Je beoordeelt de toestand dus "
                  "<strong>niet</strong> voor je voor veiligheid zorgt, en gespecialiseerde hulp inroepen is "
                  "<strong>niet de laatste</strong> stap maar de derde."),
            ("p", "Loopt iemand de gewonde zonder iets te zeggen voorbij om van thuis uit een ambulance te "
                  "bellen, dan slaat hij <strong>stap 2</strong> over: hij "
                  "<strong>beoordeelde de toestand niet</strong>, en zonder die beoordeling weet de centrale "
                  "ook niet wat ze moet sturen."),
        ]),
    ],
    onthoud=[
        "101 politie, 112 ziekenwagen en brandweer, 070 245 245 antigifcentrum, 1733 huisarts.",
        "Bij bewustzijnsverlies na vergiftiging bel je 112, niet het antigifcentrum.",
        "Vier letsels: botbreuk, kneuzing, ontwrichting en verstuiking.",
        "Ontwrichting: bot uit het gewricht. Verstuiking: banden te ver uitgerekt.",
        "Twee wonden: de huidwonde en de brandwonde.",
        "Noodsituaties: bloeding, verslikking, verdrinking, hart- en ademhalingsstilstand.",
        "Zes basisprincipes, en daarnaast vier stappen. Verwar die aantallen niet.",
        "Vermijd besmetting werkt in twee richtingen.",
        "De vier stappen: veiligheid, toestand beoordelen, hulp raadplegen, verdere eerste hulp.",
        "Gespecialiseerde hulp inroepen is stap 3, niet de laatste.",
    ],
)

# ───────────────────────── 5. Hartstilstand, reanimatie en de AED
BUNDELS["een-hartstilstand-reanimatie-en-de-aed-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Een hartstilstand, reanimatie en de AED",
    onder="De twee alarmtekens, de zes stappen in volgorde, en hoe je borstcompressies, beademing en de AED juist uitvoert.",
    secties=[
        dict(kop="Wat een hartstilstand is", blokken=[
            ("p", "Bij een <strong>hartstilstand stopt het hart met pompen, waardoor het bloed niet meer "
                  "rondgaat</strong>. Het hart klopt dus <strong>niet te snel</strong>: het pompt niet meer. "
                  "Zonder rondgaand bloed <strong>krijgen de hersenen geen zuurstof</strong>, en daarom telt "
                  "elke seconde."),
            ("p", "<strong>Twee tekens samen</strong> zijn het alarmsignaal: de persoon "
                  "<strong>reageert niet</strong> en <strong>ademt niet normaal</strong>. Wie dat ziet, moet "
                  "aan een hartstilstand denken."),
        ]),
        dict(kop="De zes stappen, in deze volgorde", blokken=[
            ("p", tabel(["Stap", "Wat je doet", "Waarom"], [
                ["1", "bepaal of de persoon bewusteloos is", "anders duw je op de borstkas van iemand die slaapt"],
                ["2", "bel 112", "de ambulance moet zo vroeg mogelijk vertrekken"],
                ["3", "kijk of er een AED in de buurt is", "dan staat hij er al wanneer je hem nodig hebt"],
                ["4", "start met borstcompressies", "de compressies komen vóór de beademing"],
                ["5", "beadem", "mond-op-mond, na de compressies"],
                ["6", "ga door tot de ambulancier het overneemt", "je stopt dus niet zelf"],
            ])),
            ("p", "Begint iemand <strong>onmiddellijk met borstcompressies</strong> en belt hij pas daarna "
                  "112, dan loopt het mis: <strong>bellen is stap 2</strong> en komt dus voor de compressies. "
                  "Hoe later de ambulance vertrekt, hoe langer de persoon zonder professionele hulp blijft."),
            ("p", "Ben je <strong>alleen</strong>, bel dan 112 en <strong>zet de luidspreker aan</strong>, "
                  "zodat je handen vrij blijven en de centrale je door de stappen loodst. Zijn er "
                  "<strong>omstaanders</strong>, verdeel dan de taken: <strong>één iemand belt 112, één "
                  "iemand zoekt een AED</strong>, en jij begint."),
            ("kader", "<strong>Je stopt niet als de persoon een keer zucht.</strong> De fiche zegt: doorgaan "
                      "tot de ambulance er is en de ambulancier het overneemt. Ben je uitgeput, "
                      "<strong>laat dan iemand anders overnemen</strong> in plaats van te stoppen. De "
                      "<strong>stabiele zijligging</strong> staat niet in dit rijtje van zes."),
        ]),
        dict(kop="Borstcompressies", blokken=[
            ("p", "Je handen gaan <strong>midden op de borstkas</strong>, niet links: het hart ligt meer in "
                  "het midden dan de meesten denken. Je armen houd je <strong>gestrekt, met je schouders "
                  "recht boven je handen</strong>, want zo duw je met je bovenlichaam en houd je het veel "
                  "langer vol. Gebogen ellebogen kosten juist meer kracht en maken de compressies ondiep."),
            ("p", "Tussen twee compressies laat je de borstkas <strong>volledig terugkomen</strong>. Komt ze "
                  "niet terug, dan kan het hart zich ook niet opnieuw vullen."),
            ("p", "Je reanimeert op een <strong>harde ondergrond</strong>: op een matras of een zetel zakt "
                  "het lichaam mee en duw je vooral de ondergrond in, zodat de compressies niet aankomen."),
        ]),
        dict(kop="Beademen", blokken=[
            ("p", "Voor je beademt, <strong>kantel je het hoofd achterover en til je de kin op</strong>. Die "
                  "twee handelingen maken de luchtweg vrij; zonder die handeling gaat de lucht niet naar de "
                  "longen. De <strong>neus knijp je dicht</strong>, anders ontsnapt de lucht daarlangs."),
            ("p", "Dat een beademing aankomt, zie je aan <strong>de borstkas die zichtbaar omhoogkomt</strong>. "
                  "Dat is het enige betrouwbare teken."),
        ]),
        dict(kop="De AED", blokken=[
            ("p", "<strong>AED</strong> staat voor <strong>automatische externe defibrillator</strong>: een "
                  "toestel dat met een stroomstoot het hartritme kan herstellen. Heb je er een gehaald, dan "
                  "<strong>zet je hem aan en volg je de gesproken instructies</strong>."),
            ("p", "De AED <strong>meet zelf het hartritme en beslist zelf</strong> of er een stroomstoot "
                  "nodig is. Daarom heet hij automatisch; jij volgt wat hij zegt."),
            ("kader", "<strong>Terwijl de AED meet, raak je het slachtoffer niet aan</strong>, ook niet om "
                      "door te duwen. Aanraken verstoort de meting, en bij een stoot is het ook voor jou "
                      "gevaarlijk."),
        ]),
    ],
    onthoud=[
        "Hartstilstand: het hart pompt niet meer, het bloed gaat niet meer rond.",
        "Twee tekens: de persoon reageert niet en ademt niet normaal.",
        "Zes stappen: bewustzijn, 112 bellen, AED zoeken, compressies, beademen, doorgaan.",
        "Bellen is stap 2 en komt dus vóór de compressies.",
        "Je gaat door tot de ambulancier het overneemt, ook na een zucht.",
        "Handen midden op de borstkas, armen gestrekt, borstkas volledig laten terugkomen.",
        "Reanimeer op een harde ondergrond.",
        "Beademen: hoofd achterover, kin op, neus dicht; de borstkas komt omhoog.",
        "AED is de automatische externe defibrillator; hij meet en beslist zelf.",
        "Raak het slachtoffer niet aan terwijl de AED meet.",
    ],
)

# ───────────────────────── 6. De overheid
BUNDELS["de-inkomsten-en-de-uitgaven-van-de-overheid-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De inkomsten en de uitgaven van de overheid",
    onder="Vier soorten inkomsten en vier soorten uitgaven, met de voorbeelden die de fiche er zelf bij geeft.",
    secties=[
        dict(kop="Vier soorten inkomsten", blokken=[
            ("p", "Een overheid heft belastingen <strong>om haar uitgaven voor de samenleving te kunnen "
                  "betalen</strong>. De fiche deelt haar inkomsten in <strong>vier</strong> soorten in."),
            ("p", tabel(["Soort", "Wat het is", "Voorbeelden uit de fiche"], [
                ["directe belasting", "gaat rechtstreeks van jou naar de overheid, op je inkomen of bezit",
                 "de bedrijfsvoorheffing, de onroerende voorheffing"],
                ["indirecte belasting", "zit in de prijs van een product of dienst",
                 "de btw, de milieubelasting, de accijnzen op brandstof"],
                ["diverse inkomsten", "boetes en vergoedingen voor diensten",
                 "een boete voor te snel rijden, betalen voor een paspoort"],
                ["inkomsten uit overheidskapitaal", "uit wat de overheid zelf bezit",
                 "de verkoop of de verhuur van gronden en gebouwen"],
            ])),
            ("p", "<strong>Direct</strong> wil zeggen zonder tussenstap. Bij een "
                  "<strong>indirecte</strong> belasting betaal jij ze aan de verkoper, en die stort ze door. "
                  "Daarom is de <strong>btw indirect</strong> en de <strong>bedrijfsvoorheffing "
                  "direct</strong>, ook al staan ze allebei op een papier met jouw naam erop."),
            ("kader", "De <strong>verkoop van een stuk grond</strong> door de overheid is "
                      "<strong>geen belasting</strong> maar een inkomst uit overheidskapitaal. En "
                      "<strong>giften</strong> staan niet in de fiche."),
        ]),
        dict(kop="Vier soorten uitgaven", blokken=[
            ("p", tabel(["Soort uitgave", "Voorbeelden uit de fiche"], [
                ["voorzien in de collectieve behoeften", "veiligheid, onderwijs en openbaar vervoer"],
                ["investeren in economische groei en ontwikkeling",
                 "handel, transport, digitale infrastructuur en duurzaamheid"],
                ["bijdragen aan het maatschappelijk en culturele leven", "cultuur, sport en infocampagnes"],
                ["sociale uitgaven", "de financiering van de sociale zekerheid, sociale woningen, projecten tegen armoede"],
            ])),
            ("p", "<strong>Collectieve behoeften</strong> zijn behoeften waar <strong>de hele samenleving "
                  "van gebruikmaakt</strong>. Legt de overheid glasvezel aan in een industriezone, dan is dat "
                  "<strong>digitale infrastructuur</strong> en dus <strong>economische groei</strong>. Betaalt "
                  "ze een festival of een sporthal, of voert ze een infocampagne over gezond eten, dan is dat "
                  "het <strong>maatschappelijk leven</strong>. Bouwt ze sociale woningen, dan is dat een "
                  "<strong>sociale uitgave</strong>."),
            ("p", "Kiest een gemeente tussen een <strong>bibliotheek</strong> en een "
                  "<strong>fietsbrug</strong>, dan staan twee soorten tegenover elkaar: het "
                  "<strong>maatschappelijk leven</strong> tegenover een <strong>collectieve behoefte</strong> "
                  "(mobiliteit)."),
            ("kader", "Twee verwarringen. <strong>Cultuur en sport zijn geen sociale uitgaven</strong> maar "
                      "maatschappelijk leven. En de <strong>financiering van de sociale zekerheid is een "
                      "uitgave</strong>, geen inkomst."),
        ]),
        dict(kop="Waarom de twee samen", blokken=[
            ("p", "De uitgaven van de overheid <strong>bepalen mee wat er voor iedereen beschikbaar is</strong>: "
                  "van scholen tot bussen tot sociale woningen. De fiche vraagt naar de invloed van "
                  "<strong>inkomsten én uitgaven samen</strong>, <strong>omdat de overheid met die twee de "
                  "ongelijkheid probeert te beperken</strong>. Dat staat zo in het leerdoel."),
        ]),
    ],
    onthoud=[
        "Vier inkomsten: directe en indirecte belastingen, diverse inkomsten, inkomsten uit overheidskapitaal.",
        "Direct gaat rechtstreeks naar de overheid, indirect zit in de prijs.",
        "Btw, milieubelasting en accijnzen zijn indirect; bedrijfsvoorheffing en onroerende voorheffing direct.",
        "Boetes en vergoedingen voor een dienst zijn diverse inkomsten.",
        "Vier uitgaven: collectieve behoeften, economische groei, maatschappelijk leven en sociale uitgaven.",
        "Collectieve behoeften: veiligheid, onderwijs en openbaar vervoer.",
        "Economische groei: handel, transport, digitale infrastructuur en duurzaamheid.",
        "Maatschappelijk leven: cultuur, sport en infocampagnes.",
        "Sociale uitgaven: sociale zekerheid, sociale woningen en projecten tegen armoede.",
        "Met inkomsten en uitgaven samen probeert de overheid de ongelijkheid te beperken.",
    ],
)

# ───────────────────────── 7. Sociale zekerheid en herverdeling
BUNDELS["sociale-zekerheid-uitkeringen-en-herverdeling-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Sociale zekerheid, uitkeringen en herverdeling",
    onder="Solidariteit en de RSZ, de zes uitkeringen, het verschil vervangings- of aanvullend inkomen, en de fiscale en sociale herverdeling.",
    secties=[
        dict(kop="Waarop de sociale zekerheid steunt", blokken=[
            ("p", "De sociale zekerheid steunt op <strong>solidariteit</strong>: wie werkt, draagt bij voor "
                  "wie op dat moment niet kan werken."),
            ("p", "De <strong>RSZ</strong> is de <strong>Rijksdienst voor Sociale Zekerheid</strong>. Ze int "
                  "de bijdragen waarmee de sociale zekerheid betaald wordt, en ze wordt gefinancierd door "
                  "<strong>de werkgevers, de werknemers en de overheid</strong> samen — dus "
                  "<strong>niet enkel door de werkgevers</strong>. Op je loonbriefje zie je de bijdrage van "
                  "de werknemer en die van de werkgever apart staan."),
        ]),
        dict(kop="De uitkeringen", blokken=[
            ("p", tabel(["Uitkering", "Wanneer"], [
                ["werkloosheidsuitkering", "iemand verliest zijn werk"],
                ["ziekte- en invaliditeitsuitkering", "iemand kan door ziekte niet werken"],
                ["arbeidsongevallenuitkering", "een ongeval tijdens het werk, zoals een val van een ladder"],
                ["uitkering beroepsziekte", "ziek worden door jarenlang met een schadelijke stof te werken"],
                ["rust- en overlevingspensioen", "stoppen op pensioenleeftijd, of een partner die overlijdt"],
                ["jaarlijks vakantiegeld", "elk jaar, bovenop het loon"],
            ])),
            ("p", "Een <strong>arbeidsongeval</strong> en een <strong>beroepsziekte</strong> zijn dus "
                  "<strong>niet hetzelfde</strong>: het ene komt van een plots ongeval, het andere van het "
                  "werk zelf over langere tijd. Het <strong>rustpensioen</strong> is voor wie stopt met "
                  "werken, het <strong>overlevingspensioen</strong> voor de achterblijvende partner."),
        ]),
        dict(kop="Vervangingsinkomen of aanvullend inkomen", blokken=[
            ("p", "Een <strong>vervangingsinkomen</strong> is een bedrag dat een <strong>weggevallen loon "
                  "vervangt</strong>: de werkloosheidsuitkering, de ziekte- en invaliditeitsuitkering en het "
                  "pensioen. Een <strong>aanvullend inkomen</strong> komt <strong>bovenop</strong> een "
                  "inkomen: het vakantiegeld en het groeipakket."),
            ("kader", "Het <strong>vakantiegeld</strong> staat wél in het rijtje van zes uitkeringen, maar "
                      "het is <strong>aanvullend</strong> en geen vervangingsinkomen: het komt bovenop je "
                      "loon en vervangt dus niets."),
        ]),
        dict(kop="Herverdeling", blokken=[
            ("p", "<strong>Herverdeling</strong> is dat de overheid <strong>middelen verschuift van sterkere "
                  "naar zwakkere schouders</strong>, om de sociale ongelijkheid te beperken. Het systeem "
                  "bestaat uit <strong>twee soorten maatregelen</strong>: <strong>fiscale</strong> (via de "
                  "belastingen) en <strong>sociale</strong> (via uitkeringen, premies en tarieven)."),
            ("p", tabel(["Fiscaal", "Sociaal"], [
                ["de progressieve personenbelasting via belastingschijven", "het leefloon, een sociale bijstandsuitkering"],
                ["belastingvrijstellingen en -verminderingen", "uitkeringen met herverdelingseffect, zoals pensioenen"],
                ["belastingheffingen op vermogen", "sociale woningen en huurpremies"],
                ["verschillende tarieven bij indirecte belastingen", "energiepremies en renovatiesteun"],
                ["", "studiebeurzen en vermindering van inschrijvingsgeld"],
                ["", "het groeipakket, de Vlaamse steun voor gezinnen met kinderen"],
                ["", "kansentarieven voor sport en cultuur"],
                ["", "de verhoogde tegemoetkoming in de gezondheidszorg"],
            ])),
            ("p", "Een <strong>progressieve personenbelasting</strong> betekent dat <strong>wie meer "
                  "verdient een hoger percentage betaalt</strong>, en dat gebeurt via "
                  "<strong>belastingschijven</strong>: elk stuk van je inkomen valt in een eigen schijf. "
                  "Betaalde iedereen hetzelfde percentage, dan was ze vlak en niet progressief."),
            ("p", "De <strong>verschillende tarieven bij indirecte belastingen</strong> bestaan "
                  "<strong>zodat noodzakelijke producten lichter belast worden dan luxe</strong>. Daarom "
                  "staat ook die maatregel bij de fiscale herverdeling."),
            ("kader", "Het onderscheid blijft eenvoudig: werkt de maatregel <strong>via de belastingen</strong>, "
                      "dan is ze fiscaal; krijg je er <strong>geld of korting</strong> door, dan is ze "
                      "sociaal. Een belastingheffing op vermogen is dus fiscaal, een kansentarief sociaal."),
        ]),
    ],
    onthoud=[
        "De sociale zekerheid steunt op solidariteit.",
        "RSZ is de Rijksdienst voor Sociale Zekerheid, betaald door werkgevers, werknemers en overheid.",
        "Zes uitkeringen: werkloosheid, ziekte en invaliditeit, arbeidsongeval, beroepsziekte, pensioen, vakantiegeld.",
        "Een arbeidsongeval is een plots ongeval, een beroepsziekte komt van het werk over langere tijd.",
        "Vervangingsinkomen vervangt een weggevallen loon, aanvullend inkomen komt erbovenop.",
        "Het vakantiegeld staat in het rijtje maar is aanvullend.",
        "Herverdeling verschuift middelen van sterkere naar zwakkere schouders.",
        "Twee soorten: fiscale en sociale maatregelen.",
        "Progressief: wie meer verdient betaalt een hoger percentage, via belastingschijven.",
        "Leefloon, groeipakket, huurpremies en kansentarieven zijn sociale maatregelen.",
    ],
)

# ───────────────────────── 8. Vraag, aanbod en evenwicht
BUNDELS["vraag-aanbod-en-het-marktevenwicht-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Vraag, aanbod en het marktevenwicht",
    onder="Wie vraagt en wie aanbiedt, hoe de twee curven lopen, en hoe je een overschot of een tekort berekent.",
    secties=[
        dict(kop="De twee partijen en de twee assen", blokken=[
            ("p", "Op de <strong>productmarkt</strong> — de markt waarop goederen en diensten verhandeld "
                  "worden — staan twee partijen tegenover elkaar. De <strong>vrager</strong> is de "
                  "<strong>koper</strong>, die het product wil hebben. De <strong>aanbieder</strong> is de "
                  "<strong>verkoper</strong>, die het product op de markt brengt. Vragen is hier dus "
                  "hetzelfde als willen kopen."),
            ("p", "Op een vraag- en aanbodgrafiek staat de <strong>prijs op de verticale as</strong> en de "
                  "<strong>hoeveelheid op de horizontale as</strong>. Dat is de vaste afspraak."),
            ("fig", svg.marktevenwicht(),
             "De vraagcurve V en de aanbodcurve A, met het snijpunt E."),
        ]),
        dict(kop="Hoe de curven lopen", blokken=[
            ("p", tabel(["Als de prijs stijgt", "Wat er gebeurt", "Hoe de curve loopt"], [
                ["de gevraagde hoeveelheid", "daalt: hoe duurder, hoe minder mensen willen kopen", "de vraagcurve daalt"],
                ["de aangeboden hoeveelheid", "stijgt: verkopen wordt interessanter", "de aanbodcurve stijgt"],
            ])),
            ("kader", "Een veelgemaakte fout: de <strong>aanbodcurve daalt niet</strong> als de prijs stijgt. "
                      "Ze doet precies het omgekeerde van de vraagcurve."),
        ]),
        dict(kop="Het evenwicht", blokken=[
            ("p", "De <strong>evenwichtsprijs</strong> is de prijs waarbij <strong>vraag en aanbod gelijk "
                  "zijn</strong>. Daar snijden de twee curven elkaar. De hoeveelheid die daarbij hoort, is "
                  "de <strong>evenwichtshoeveelheid</strong>."),
            ("p", "Bij de evenwichtsprijs is er <strong>geen overschot en geen tekort</strong>, en blijft er "
                  "dus <strong>geen onverkochte voorraad</strong> over. De prijs ligt daarmee niet voor "
                  "altijd vast: verschuift een curve, dan komt er een nieuw evenwicht."),
            ("p", "Een voorbeeld om af te lezen: bij 6 euro vragen de kopers 100 stuks en bieden de "
                  "verkopers er 180 aan; bij 5 euro vragen én bieden ze er 140. De evenwichtsprijs is dan "
                  "<strong>5 euro</strong> en de evenwichtshoeveelheid <strong>140 stuks</strong>."),
        ]),
        dict(kop="Overschot en tekort berekenen", blokken=[
            ("p", tabel(["Situatie", "Wanneer", "Hoe je het berekent", "Waar de prijs ligt"], [
                ["overschot", "het aanbod is groter dan de vraag", "aanbod min vraag", "boven de evenwichtsprijs"],
                ["tekort", "de vraag is groter dan het aanbod", "vraag min aanbod", "onder de evenwichtsprijs"],
            ])),
            ("p", "Bij 8 euro vragen de kopers 90 stuks en bieden de verkopers er 150 aan: 150 min 90 geeft "
                  "een <strong>overschot van 60 stuks</strong>. Bij 3 euro vragen ze er 220 en bieden ze er "
                  "160 aan: 220 min 160 geeft een <strong>tekort van 60 stuks</strong>. Zijn vraag en "
                  "aanbod gelijk, dan is er <strong>geen overschot</strong>: dan zit je in het evenwicht."),
            ("p", "Bij één prijs is het dus <strong>het een of het ander</strong>, of geen van beide. "
                  "Een overschot en een tekort tegelijk op dezelfde markt bij dezelfde prijs kan niet."),
        ]),
        dict(kop="Wat de markt zelf doet", blokken=[
            ("p", "Doet de overheid niets, dan zoekt de markt haar evenwicht. Bij een "
                  "<strong>overschot zakt de prijs</strong> naar het evenwicht: verkopers met onverkochte "
                  "voorraad zakken met hun prijs. Bij een <strong>tekort stijgt de prijs</strong>: kopers "
                  "zijn bereid meer te betalen."),
            ("p", "Daaraan herken je in een verhaal waar de prijs zit. Houdt een marktkramer elke avond "
                  "kratten over, dan ligt zijn prijs <strong>boven</strong> de evenwichtsprijs. Is een "
                  "winkel al om tien uur uitverkocht en moet ze mensen wegsturen, dan ligt haar prijs "
                  "<strong>onder</strong> de evenwichtsprijs."),
        ]),
    ],
    onthoud=[
        "De vrager is de koper, de aanbieder is de verkoper.",
        "Prijs op de verticale as, hoeveelheid op de horizontale as.",
        "Stijgt de prijs, dan daalt de vraag en stijgt het aanbod.",
        "De evenwichtsprijs is de prijs waarbij vraag en aanbod gelijk zijn.",
        "Bij het evenwicht is er geen overschot en geen tekort.",
        "Overschot = aanbod min vraag, bij een prijs boven het evenwicht.",
        "Tekort = vraag min aanbod, bij een prijs onder het evenwicht.",
        "Bij een overschot zakt de prijs, bij een tekort stijgt ze.",
        "Overblijvende voorraad betekent een te hoge prijs.",
        "Te snel uitverkocht betekent een te lage prijs.",
    ],
)

# ───────────────────────── 9. Verschuivingen en de overheid
BUNDELS["verschuivingen-op-de-markt-en-de-overheid-die-ingrijpt-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Verschuivingen op de markt en de overheid die ingrijpt",
    onder="Bewegen op de curve of de curve verschuiven, wat dat met het evenwicht doet, en de drie maatregelen van de overheid.",
    secties=[
        dict(kop="Op de curve of van de curve", blokken=[
            ("p", "Dit is het onderscheid waar het hier om draait."),
            ("p", tabel(["Wat verandert", "Wat er gebeurt"], [
                ["de prijs van het product zelf", "een <b>beweging op</b> de curve: je schuift langs dezelfde lijn naar een ander punt"],
                ["iets anders dan die prijs", "een <b>verschuiving van</b> de curve: de hele lijn verhuist"],
            ])),
            ("p", "Dat \"iets anders\" is bij de <strong>vraag</strong>: het <strong>inkomen</strong> van de "
                  "kopers, hun <strong>smaak</strong>, het <strong>aantal kopers</strong>, of de "
                  "<strong>prijs van een ander product</strong>. Bij het <strong>aanbod</strong>: de "
                  "<strong>productiekosten</strong>, een <strong>betere techniek</strong>, of het "
                  "<strong>aantal verkopers</strong>."),
            ("kader", "Een <strong>prijsdaling van het product zelf verschuift de vraagcurve niet</strong>. "
                      "Dan beweeg je langs dezelfde curve naar een ander punt. Een "
                      "<strong>inkomensstijging</strong> verschuift ze wél, want het inkomen is de prijs van "
                      "het product niet."),
        ]),
        dict(kop="Naar links of naar rechts", blokken=[
            ("p", tabel(["Wat er gebeurt", "Welke curve", "Naar waar"], [
                ["de lonen stijgen, men koopt bij elke prijs meer", "vraag", "rechts"],
                ["een product raakt uit de mode", "vraag", "links"],
                ["er komen kopers bij", "vraag", "rechts"],
                ["een vergelijkbaar product wordt veel goedkoper", "vraag", "links"],
                ["de grondstoffen worden duurder", "aanbod", "links"],
                ["een nieuwe machine maakt produceren goedkoper", "aanbod", "rechts"],
            ])),
            ("fig", svg.marktevenwicht(verschuiving="vraag rechts"),
             "De vraagcurve verschuift naar rechts; het snijpunt verhuist van E naar E′."),
        ]),
        dict(kop="Wat dat met het evenwicht doet", blokken=[
            ("p", tabel(["Verschuiving", "De andere blijft gelijk", "Prijs", "Hoeveelheid"], [
                ["vraag naar rechts", "aanbod gelijk", "stijgt", "stijgt"],
                ["vraag naar links", "aanbod gelijk", "daalt", "daalt"],
                ["aanbod naar rechts", "vraag gelijk", "daalt", "stijgt"],
                ["aanbod naar links", "vraag gelijk", "stijgt", "daalt"],
            ])),
            ("p", "Bederft een zomer met slecht weer een groot deel van de oogst, dan verschuift het "
                  "<strong>aanbod naar links</strong> en <strong>stijgt de prijs</strong> van die groente."),
        ]),
        dict(kop="Drie maatregelen van de overheid", blokken=[
            ("p", "De fiche noemt er <strong>drie</strong>: <strong>btw en accijnzen heffen</strong>, "
                  "<strong>premies en subsidies uitkeren</strong>, en <strong>minimum- en maximumprijzen "
                  "invoeren</strong>. De productie zelf overnemen staat er niet bij."),
            ("p", "Een <strong>accijns</strong> is een <strong>extra belasting op bepaalde producten</strong>, "
                  "zoals brandstof, tabak of alcohol. Ze komt bovenop de btw en maakt die producten bewust "
                  "duurder."),
            ("p", tabel(["Maatregel", "Wat er met de curve gebeurt", "Gevolg"], [
                ["een belasting op een product", "het aanbod verschuift naar links", "de prijs stijgt"],
                ["een subsidie aan producenten", "het aanbod verschuift naar rechts", "de prijs daalt"],
                ["een premie aan de kopers", "de vraag verschuift naar rechts", "de prijs stijgt en er wordt meer verkocht"],
            ])),
            ("p", "Geeft de overheid een premie voor zonnepanelen, dan willen meer mensen kopen bij elke "
                  "prijs: <strong>meer vraag, dus een hogere prijs en meer verkochte panelen</strong>."),
        ]),
        dict(kop="Minimumprijs en maximumprijs", blokken=[
            ("p", tabel(["Vaste prijs", "Waar ze ligt", "Wat ze geeft", "Waarom"], [
                ["minimumprijs", "boven de evenwichtsprijs", "een overschot",
                 "om de producenten een leefbaar inkomen te garanderen"],
                ["maximumprijs", "onder de evenwichtsprijs", "een tekort",
                 "om een noodzakelijk product betaalbaar te houden"],
            ])),
            ("p", "Een <strong>minimumprijs onder</strong> het evenwicht verandert niets, want de markt zit "
                  "er al boven. Een <strong>maximumprijs boven</strong> het evenwicht verandert evenmin iets. "
                  "Een vaste prijs doet dus pas iets als ze aan de <strong>juiste kant</strong> van het "
                  "evenwicht ligt."),
            ("kader", "Verwar de twee niet: een <strong>minimumprijs geeft een overschot</strong>, geen "
                      "tekort. Een bodemprijs voor landbouwproducten is het bekende voorbeeld; een "
                      "maximumprijs ken je van energie of huur."),
        ]),
    ],
    onthoud=[
        "Verandert de prijs van het product zelf, dan beweeg je op de curve.",
        "Verandert er iets anders, dan verschuift de curve zelf.",
        "Vraag verschuift door inkomen, smaak, aantal kopers en de prijs van een ander product.",
        "Aanbod verschuift door productiekosten, techniek en het aantal verkopers.",
        "Vraag naar rechts: prijs en hoeveelheid stijgen. Aanbod naar rechts: prijs daalt, hoeveelheid stijgt.",
        "Drie maatregelen: btw en accijnzen, premies en subsidies, minimum- en maximumprijzen.",
        "Een accijns is een extra belasting op brandstof, tabak of alcohol.",
        "Een belasting duwt het aanbod naar links, een subsidie naar rechts.",
        "Een minimumprijs ligt boven het evenwicht en geeft een overschot.",
        "Een maximumprijs ligt onder het evenwicht en geeft een tekort.",
    ],
)

# ───────────────────────── 10. De arbeidsovereenkomst
BUNDELS["de-arbeidsovereenkomst-en-het-arbeidsreglement-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De arbeidsovereenkomst en het arbeidsreglement",
    onder="De drie indelingen van een contract, het verschil met het reglement, en de arbeidssituaties uit de fiche.",
    secties=[
        dict(kop="Overeenkomst of reglement", blokken=[
            ("p", "Een <strong>arbeidsovereenkomst</strong> is de afspraak tussen <strong>één werknemer en "
                  "zijn werkgever</strong>. Een <strong>arbeidsreglement</strong> zijn de regels die "
                  "<strong>voor iedereen in het bedrijf</strong> gelden. Kort: het reglement is van het "
                  "bedrijf, de overeenkomst is van jou."),
            ("p", tabel(["In de arbeidsovereenkomst", "In het arbeidsreglement"], [
                ["jouw functie", "het uurrooster van de hele ploeg"],
                ["jouw brutoloon", "hoe je ziekte in dit bedrijf moet melden"],
                ["de duur van jouw contract", "de openingsuren"],
            ])),
            ("p", "De overeenkomst is belangrijk voor <strong>allebei</strong> de partijen: voor de "
                  "werknemer legt ze <strong>zijn loon, uren en taken zwart op wit vast</strong>, voor de "
                  "werkgever legt ze vast <strong>wat hij van de werknemer mag verwachten</strong>."),
        ]),
        dict(kop="Drie indelingen, en ze staan los van elkaar", blokken=[
            ("p", "De fiche deelt arbeidsovereenkomsten op <strong>drie manieren</strong> in: naar de "
                  "<strong>aard van het werk</strong>, naar de <strong>duur</strong> en naar de "
                  "<strong>omvang van de prestaties</strong>. Elk contract valt in <strong>alle drie</strong> "
                  "een vakje."),
            ("p", tabel(["Indeling", "Soorten"], [
                ["aard van het werk", "arbeider of bediende"],
                ["duur", "bepaalde duur, onbepaalde duur, vervangingsduur, welomschreven werk"],
                ["omvang van de prestaties", "deeltijds of voltijds"],
            ])),
            ("p", "Daarom kan je van één contract alle drie de dingen zeggen: wie drie dagen per week als "
                  "bediende voor onbepaalde tijd werkt, heeft een <strong>deeltijdse "
                  "bediendenovereenkomst van onbepaalde duur</strong>. En daarom kan "
                  "<strong>deeltijds</strong> ook perfect <strong>voor onbepaalde tijd</strong>: de omvang "
                  "en de duur staan los van elkaar."),
            ("kader", "<strong>Arbeider en bediende gaan over de aard van het werk</strong>, niet over de "
                      "duur. Dat wordt het vaakst door elkaar gehaald."),
        ]),
        dict(kop="De vier soorten duur", blokken=[
            ("p", tabel(["Duur", "Wanneer het contract eindigt", "Voorbeeld"], [
                ["bepaalde duur", "op een einddatum of een duidelijk eindpunt", "van 1 maart tot en met 31 augustus"],
                ["onbepaalde duur", "pas als een van de twee partijen het beëindigt", "een contract zonder einddatum"],
                ["vervangingsduur", "als de afwezige collega terug is", "iemand vervangen die met ziekteverlof is"],
                ["welomschreven werk", "als de opdracht af is", "aangenomen om één dak te vernieuwen"],
            ])),
            ("p", "De <strong>vervangingsduur</strong> en het <strong>welomschreven werk</strong> worden het "
                  "vaakst vergeten, en bij allebei staat er <strong>geen vaste datum</strong> in het "
                  "contract: niet de datum maar de terugkeer of de opdracht bepaalt het einde. Een "
                  "<strong>proefduur</strong> staat niet als eigen soort in dit rijtje."),
        ]),
        dict(kop="Arbeidssituaties", blokken=[
            ("p", "De fiche noemt een rijtje <strong>arbeidssituaties</strong> die je moet kunnen "
                  "herkennen: de <strong>beëindiging</strong> van de arbeidsovereenkomst, de "
                  "<strong>schorsing</strong> ervan, <strong>overwerk en overloon</strong>, de "
                  "<strong>proefperiode bij studenten</strong>, het <strong>verbod op nachtarbeid</strong> "
                  "en de <strong>loonnormen</strong>. Een evaluatie staat er niet bij."),
            ("p", "Bij een <strong>schorsing</strong> blijft het contract bestaan maar ligt het werk "
                  "<strong>tijdelijk stil</strong>, bijvoorbeeld bij ziekte of zwangerschapsrust. Het "
                  "contract is dus <strong>niet beëindigd</strong>."),
            ("p", "<strong>Overloon</strong> is een <strong>toeslag bovenop het gewone loon voor "
                  "overwerk</strong>. Het <strong>verbod op nachtarbeid</strong> betekent dat werken tijdens "
                  "de nacht in principe niet mag, <strong>met wettelijke uitzonderingen</strong>, "
                  "bijvoorbeeld in de zorg. De <strong>proefperiode bij studenten</strong> laat beide "
                  "partijen eerst even proberen."),
            ("kader", "Op het examen kan je <strong>bronmateriaal</strong> krijgen: een "
                      "<strong>arbeidsovereenkomst</strong>, een <strong>arbeidsreglement</strong>, een "
                      "<strong>loonfiche</strong>, een <strong>krantenartikel</strong>, een "
                      "<strong>brochure</strong> of een <strong>wettekst</strong>."),
        ]),
        dict(kop="Rechten en plichten", blokken=[
            ("p", "Bij de <strong>rechten van de werknemer</strong> hoort onder meer <strong>op tijd zijn "
                  "loon ontvangen</strong>. Bij de <strong>plichten van de werkgever</strong> hoort "
                  "<strong>zorgen voor een veilige werkplek</strong>. Let bij zo'n vraag goed op wie het "
                  "onderwerp is: hetzelfde rijtje bevat vaak de plichten van de wérknemer als afleiders."),
        ]),
    ],
    onthoud=[
        "De overeenkomst is van jou, het reglement geldt voor iedereen in het bedrijf.",
        "Drie indelingen: aard van het werk, duur, en omvang van de prestaties.",
        "Arbeider en bediende gaan over de aard van het werk.",
        "Vier soorten duur: bepaald, onbepaald, vervanging en welomschreven werk.",
        "Deeltijds kan ook voor onbepaalde tijd: omvang en duur staan los van elkaar.",
        "Bij een schorsing blijft het contract bestaan, alleen het werk ligt stil.",
        "Overloon is de toeslag voor overwerk.",
        "Nachtarbeid is in principe verboden, met wettelijke uitzonderingen.",
        "Bronmateriaal kan een overeenkomst, reglement, loonfiche, artikel, brochure of wettekst zijn.",
        "Op tijd je loon krijgen is een recht van de werknemer; een veilige werkplek een plicht van de werkgever.",
    ],
)

# ───────────────────────── 11. Van bruto naar netto
BUNDELS["van-brutoloon-naar-nettoloon-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Van brutoloon naar nettoloon",
    onder="De twee inhoudingen in de juiste volgorde, wat ze doen, en waarom een student, een arbeider en een ouder elk anders uitkomen.",
    secties=[
        dict(kop="De weg van bruto naar netto", blokken=[
            ("p", "Het <strong>brutoloon</strong> is het loon <strong>voor er iets van afgehouden "
                  "wordt</strong>. Het <strong>nettoloon</strong> is het bedrag dat je "
                  "<strong>werkelijk op je rekening krijgt</strong>. Daartussen zitten twee inhoudingen, en "
                  "de <strong>volgorde ligt vast</strong>."),
            ("fig", svg.stappen(["brutoloon", "belastbaar loon|na de sociale bijdrage",
                                        "nettoloon|na de bedrijfsvoorheffing"]),
             "De drie bedragen op een loonfiche, in de volgorde waarin ze berekend worden."),
            ("p", tabel(["Stap", "Wat ervan af gaat", "Waarvoor dient het", "Wat je overhoudt"], [
                ["1", "de sociale zekerheidsbijdrage", "de sociale zekerheid mee financieren", "het belastbaar loon"],
                ["2", "de bedrijfsvoorheffing", "een voorschot op je personenbelasting", "het nettoloon"],
            ])),
            ("p", "De <strong>bedrijfsvoorheffing komt dus na</strong> de sociale bijdrage, nooit ervoor. En "
                  "het <strong>belastbaar loon is niet hetzelfde als het nettoloon</strong>: het staat "
                  "ertussenin."),
            ("p", "<strong>Voorheffing</strong> betekent <strong>vooraf geheven</strong>: in de plaats van "
                  "alles pas bij de aangifte te betalen. Houdt je werkgever er te veel in, dan "
                  "<strong>krijg je het verschil terug na je belastingaangifte</strong>. De berekening van "
                  "bruto naar netto vind je terug op de <strong>loonfiche</strong>."),
            ("p", "Een voorbeeld: iemand verdient 2 400 euro bruto, na de sociale bijdrage blijft 2 086 euro "
                  "over en na de bedrijfsvoorheffing 1 720 euro. Het <strong>belastbaar loon is 2 086 "
                  "euro</strong> en de <strong>bedrijfsvoorheffing 366 euro</strong> (2 086 min 1 720)."),
        ]),
        dict(kop="Arbeider of bediende", blokken=[
            ("p", "Bij een <strong>bediende</strong> wordt de sociale bijdrage berekend op zijn "
                  "<strong>brutoloon</strong>. Bij een <strong>arbeider</strong> op <strong>108 procent van "
                  "zijn brutoloon</strong>: een oude regel uit de tijd dat arbeiders per dag of per uur "
                  "betaald werden."),
            ("p", "Verdienen een arbeider en een bediende allebei 2 000 euro bruto, dan betaalt de "
                  "<strong>arbeider de hoogste sociale bijdrage</strong>. Het percentage is hetzelfde, maar "
                  "het bedrag waarop gerekend wordt, ligt bij hem hoger."),
        ]),
        dict(kop="Een student", blokken=[
            ("p", "Binnen een <strong>studentencontract</strong> houdt de werkgever <strong>enkel een "
                  "solidariteitsbijdrage</strong> in, die lager ligt dan de gewone sociale "
                  "zekerheidsbijdrage. En er gaat <strong>geen bedrijfsvoorheffing</strong> af."),
            ("p", "Daarom ligt het <strong>nettoloon van een student dicht bij zijn brutoloon</strong>: de "
                  "twee gewone inhoudingen vallen voor een groot deel weg."),
        ]),
        dict(kop="De gezinssituatie", blokken=[
            ("p", "De <strong>gezinssituatie</strong> van de werknemer beïnvloedt de hoogte van de "
                  "<strong>bedrijfsvoorheffing</strong>, en dus het nettoloon. Hebben twee mensen hetzelfde "
                  "brutoloon maar heeft de ene <strong>twee kinderen ten laste</strong>, dan houdt die "
                  "<strong>netto meer over</strong>."),
            ("kader", "Het verschil zit in de <strong>bedrijfsvoorheffing</strong>, niet in de sociale "
                      "bijdrage: die staat los van je gezin."),
        ]),
        dict(kop="Wat de werkgever er nog bovenop betaalt", blokken=[
            ("p", "Niet alleen de werknemer draagt bij aan de RSZ: de <strong>werkgever betaalt er bovenop "
                  "een eigen bijdrage</strong>. De <strong>loonkost</strong> voor een werkgever is dus het "
                  "<strong>brutoloon plus zijn eigen bijdrage aan de RSZ</strong>, en daarmee hoger dan het "
                  "bruto dat op het contract staat."),
            ("p", "Op een loonfiche staan daarom <strong>twee verschillende inhoudingen met een ander "
                  "doel</strong>: de RSZ financiert de sociale zekerheid, de voorheffing is een voorschot op "
                  "je personenbelasting."),
        ]),
    ],
    onthoud=[
        "Bruto is voor de inhoudingen, netto is wat op je rekening komt.",
        "Eerst de sociale zekerheidsbijdrage, dan pas de bedrijfsvoorheffing.",
        "Na de sociale bijdrage houd je het belastbaar loon over.",
        "De bedrijfsvoorheffing is een voorschot op je personenbelasting.",
        "Te veel ingehouden voorheffing krijg je terug na je aangifte.",
        "Bij een arbeider rekent men op 108 procent van het brutoloon, bij een bediende op het brutoloon.",
        "Een student betaalt enkel een solidariteitsbijdrage en geen bedrijfsvoorheffing.",
        "De gezinssituatie verandert de bedrijfsvoorheffing, niet de sociale bijdrage.",
        "De werkgever betaalt bovenop het bruto nog een eigen RSZ-bijdrage.",
        "De loonkost is het brutoloon plus de werkgeversbijdrage.",
    ],
)

# ───────────────────────── 12. Welzijn op het werk
BUNDELS["welzijn-op-het-werk-en-waar-je-met-vragen-terechtkan-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Welzijn op het werk en waar je met vragen terechtkan",
    onder="Preventie, beschermingsmiddelen en het CPBW, en de zes instanties waar een werknemer of student naartoe kan.",
    secties=[
        dict(kop="Veilig werken", blokken=[
            ("p", "De <strong>werkgever is verantwoordelijk voor een veilige werkplek</strong>, en de "
                  "<strong>werknemer werkt veilig mee</strong>. Allebei dus, elk met een eigen rol: de "
                  "werkgever moet voor de veiligheid zorgen, de werknemer moet de regels volgen en "
                  "<strong>gevaren melden</strong>."),
            ("p", "<strong>Preventie</strong> is <strong>maatregelen nemen voordat er iets misgaat</strong>. "
                  "Krijgt een nieuwe werknemer op zijn eerste dag uitleg over de nooduitgangen en de "
                  "machines, dan is dat een <strong>preventiemaatregel</strong>: onthaal en vorming horen "
                  "bij het voorkomen van ongevallen."),
            ("p", "<strong>Persoonlijke beschermingsmiddelen</strong> zijn spullen die je <strong>zelf "
                  "draagt</strong>, zoals een helm of handschoenen. Ze <strong>komen bovenop</strong> de "
                  "veiligheid aan de machines zelf: eerst de machine veilig maken, dan pas de helm. De "
                  "<strong>werkgever voorziet</strong> ze, de werknemer gebruikt ze."),
            ("p", "<strong>Pictogrammen</strong> waarschuwen <strong>in één oogopslag voor gevaar of een "
                  "verplichting</strong>, ook voor wie de taal niet vlot leest."),
            ("kader", "Heeft een machine een losse kap waar iemand bij kan, dan <strong>meld je het meteen "
                      "en gebruik je de machine niet</strong>. Melden is een plicht van de werknemer; "
                      "herstellen is een zaak voor wie het mag."),
        ]),
        dict(kop="Welzijn is breder dan veiligheid", blokken=[
            ("p", "<strong>Welzijn op het werk gaat niet enkel over het vermijden van ongevallen</strong>. "
                  "Ook de <strong>werkdruk</strong>, de <strong>sfeer in de ploeg</strong> en pesten op het "
                  "werk horen erbij."),
            ("p", "Het <strong>CPBW</strong> is het <strong>Comité voor Preventie en Bescherming op het "
                  "Werk</strong>: een <strong>overlegorgaan binnen het bedrijf zelf</strong>, waar "
                  "werkgevers en werknemers samen rond de tafel zitten om te <strong>overleggen over "
                  "veiligheid en welzijn</strong>. Staat een nooduitgang versperd, dan is het CPBW de plek "
                  "binnen het bedrijf om dat te melden."),
            ("p", "Veiligheid staat ook in het <strong>arbeidsreglement</strong>, <strong>omdat die regels "
                  "voor iedereen in het bedrijf gelden</strong>. Valt iemand op het werk en breekt hij zijn "
                  "pols, dan komt de <strong>arbeidsongevallenuitkering</strong> in beeld."),
        ]),
        dict(kop="Zes plekken waar je terechtkan", blokken=[
            ("p", "De fiche noemt <strong>zes</strong> instanties en organisaties."),
            ("p", tabel(["Naam", "Voluit", "Waarvoor"], [
                ["CPBW", "Comité voor Preventie en Bescherming op het Werk", "overleg over veiligheid en welzijn in het bedrijf"],
                ["RSZ", "Rijksdienst voor Sociale Zekerheid", "de bijdragen innen en beheren"],
                ["RVA", "Rijksdienst voor Arbeidsvoorziening", "de werkloosheidsuitkering, loopbaanonderbreking"],
                ["VDAB", "Vlaamse Dienst voor Arbeidsbemiddeling en Beroepsopleiding", "werk zoeken, een opleiding, loopbaanbegeleiding"],
                ["student@work", "", "je gewerkte uren als student opvolgen"],
                ["vakbonden", "", "advies en verdediging van je belangen als werknemer"],
            ])),
            ("kader", "De verwarring die het vaakst gemaakt wordt: de <strong>RVA betaalt de "
                      "werkloosheidsuitkering</strong>, de <strong>VDAB helpt je aan werk</strong>. En de "
                      "<strong>RSZ int de bijdragen</strong>; ze zoekt geen werk voor je."),
            ("p", "<strong>student@work</strong> is <strong>geen vacaturesite</strong>: het is de plek waar "
                  "je ziet hoeveel uren je al gewerkt hebt en hoeveel je er nog hebt. Twijfel je of je "
                  "werkgever wel bijdragen voor jou betaalt, dan gaat dat over de <strong>RSZ</strong>. "
                  "Denk je dat je overloon niet klopt, vraag dan eerst advies bij een "
                  "<strong>vakbond</strong>."),
        ]),
    ],
    onthoud=[
        "De werkgever zorgt voor een veilige werkplek, de werknemer werkt veilig mee en meldt gevaren.",
        "Preventie is maatregelen nemen voordat er iets misgaat.",
        "Persoonlijke beschermingsmiddelen komen bovenop de veiligheid aan de machine.",
        "Pictogrammen waarschuwen in één oogopslag, ook zonder taal.",
        "Welzijn gaat ook over werkdruk, sfeer en pesten op het werk.",
        "CPBW is het Comité voor Preventie en Bescherming op het Werk, binnen het bedrijf.",
        "RVA betaalt de uitkering, VDAB helpt je aan werk en opleiding.",
        "RSZ int de bijdragen voor de sociale zekerheid.",
        "Op student@work volg je je gewerkte uren als student op.",
        "Een vakbond geeft advies en verdedigt je belangen als werknemer.",
    ],
)

# ───────────────────────── 13. De totale aankoopkost en het krediet
BUNDELS["de-totale-aankoopkost-en-het-consumentenkrediet-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="De totale aankoopkost en het consumentenkrediet",
    onder="Wat er allemaal in een prijs zit, de vier consumentenkredieten, en waarom je enkel op het JKP vergelijkt.",
    secties=[
        dict(kop="De totale kostprijs", blokken=[
            ("p", "De <strong>totale kostprijs</strong> is de <strong>prijs na korting, met alle bijkomende "
                  "kosten en de btw erbij</strong>. De prijs op het etiket is dus "
                  "<strong>niet</strong> altijd wat je betaalt."),
            ("p", "Een <strong>commerciële korting</strong> is een vermindering die de <strong>verkoper zelf "
                  "toestaat</strong>. Ze gaat van de prijs af <strong>voor</strong> je de rest berekent."),
            ("p", tabel(["Soort bijkomende kost", "Welke", "Hoe je ze telt"], [
                ["eenmalig", "de inschrijvingskost en de leveringskost", "één keer bij de prijs"],
                ["terugkerend", "het abonnement en de verzekering", "maal het aantal maanden of jaren"],
            ])),
            ("p", "De <strong>btw hangt af van het product</strong>, want er bestaan "
                  "<strong>verschillende tarieven</strong>. Niet alle producten hebben hetzelfde "
                  "btw-tarief."),
            ("p", "Drie rekenvoorbeelden, telkens in dezelfde volgorde: eerst de korting, dan de kosten."),
            ("p", tabel(["Aankoop", "Berekening", "Totaal"], [
                ["fiets van 800 euro, 10 % korting, 25 euro levering", "800 − 80 + 25", "745 euro"],
                ["toestel van 240 euro, 15 euro inschrijving, abonnement 12 euro per maand, één jaar",
                 "240 + 15 + 12 × 12", "399 euro"],
                ["laptop van 600 euro, 50 euro korting, verzekering 5 euro per maand, twee jaar",
                 "600 − 50 + 24 × 5", "670 euro"],
            ])),
            ("kader", "Daarom vraagt de fiche naar de <strong>totale kostprijs</strong> en niet naar de "
                      "prijs alleen: <strong>pas met de totale kost maak je een eerlijke keuze</strong>. "
                      "Een printer van 180 euro met gratis levering is voordeliger dan een van 165 euro met "
                      "20 euro levering, want 185 is meer dan 180."),
            ("p", "In een <strong>verkoopovereenkomst</strong> heeft de koper ook <strong>rechten</strong>: "
                  "een product krijgen <strong>dat is wat er beloofd werd</strong>. De "
                  "<strong>plicht van de verkoper</strong> is <strong>leveren wat is afgesproken, in de "
                  "afgesproken staat</strong>; de plicht van de koper is betalen."),
        ]),
        dict(kop="Vier consumentenkredieten", blokken=[
            ("p", tabel(["Krediet", "Wat het is", "Voorbeeld"], [
                ["verkoop op afbetaling", "het krediet hangt vast aan dat ene product", "een wasmachine in twaalf schijven"],
                ["lening op afbetaling", "je krijgt geld, geen product", "een bedrag lenen en in vaste schijven terugbetalen"],
                ["kredietopening", "via een kaart of een geoorloofde debetstand", "tot een bepaald bedrag onder nul gaan"],
                ["financieringshuur of leasing", "je huurt, met vaak de kans het achteraf over te kopen", "een wagen voor vier jaar"],
            ])),
            ("p", "Een <strong>verkoop op afbetaling</strong> en een <strong>lening op afbetaling</strong> "
                  "zijn dus <strong>niet hetzelfde</strong>. En bij een <strong>leasing ben je niet meteen "
                  "eigenaar</strong>: je huurt."),
        ]),
        dict(kop="De vijf onderdelen en het JKP", blokken=[
            ("p", "Een consumentenkrediet heeft <strong>vijf onderdelen</strong>: de "
                  "<strong>looptijd</strong>, de <strong>rentevoet</strong>, het <strong>geleende "
                  "bedrag</strong>, het <strong>JKP</strong> en het <strong>maandbedrag</strong>."),
            ("p", "Het <strong>JKP</strong> is het <strong>jaarlijks kostenpercentage</strong>. Het verschil "
                  "met de rentevoet: het <strong>JKP telt alle kosten van het krediet mee</strong>, de "
                  "rentevoet enkel de rente. Daarom <strong>ligt het JKP nooit lager</strong> dan de "
                  "rentevoet, en daarom is het <strong>het enige getal waarmee je twee kredieten eerlijk "
                  "vergelijkt</strong>: een lage rentevoet met veel dossierkosten blijft duur."),
            ("p", "Rekenen doe je met het maandbedrag en de looptijd. Leen je 3 000 euro en betaal je 36 "
                  "maanden lang 95 euro, dan is de <strong>totale terugbetaling 3 420 euro</strong> "
                  "(36 × 95) en de <strong>rente 420 euro</strong> (3 420 − 3 000). Heb je er al 12 betaald, "
                  "dan moet je nog <strong>2 280 euro</strong> betalen (24 × 95)."),
            ("kader", "Een <strong>langere looptijd</strong> maakt je <strong>maandbedrag kleiner</strong> "
                      "maar je <strong>totale kost groter</strong>: je betaalt langer rente, en de meerprijs "
                      "van de financiering loopt op."),
        ]),
        dict(kop="Problemen vermijden", blokken=[
            ("p", "Wat helpt: een <strong>spaarbuffer aanleggen</strong> voor onverwachte kosten, je "
                  "<strong>uitgaven en inkomsten opvolgen in een budgetplan</strong>, en "
                  "<strong>kredieten vergelijken op hun JKP</strong> voor je tekent. Kredieten "
                  "<strong>stapelen</strong> is net wat je in de problemen brengt."),
            ("p", "Gaat het mis, dan zijn de gevolgen van te veel lenen: je <strong>raakt je maandelijkse "
                  "aflossingen niet meer betaald</strong>, je komt in een <strong>schuldenspiraal</strong> "
                  "terecht, en je moet een beroep doen op <strong>schuldbemiddeling</strong>."),
        ]),
    ],
    onthoud=[
        "Totale kostprijs = prijs na korting, plus alle bijkomende kosten, plus btw.",
        "Een commerciële korting gaat eerst van de prijs af.",
        "Eenmalig: inschrijving en levering. Terugkerend: abonnement en verzekering.",
        "Er bestaan verschillende btw-tarieven.",
        "Vier kredieten: verkoop op afbetaling, lening op afbetaling, kredietopening en financieringshuur.",
        "Bij leasing huur je; je bent niet meteen eigenaar.",
        "Vijf onderdelen: looptijd, rentevoet, geleend bedrag, JKP en maandbedrag.",
        "Het JKP telt alle kosten mee en ligt nooit lager dan de rentevoet.",
        "Langere looptijd: kleiner maandbedrag, grotere totale kost.",
        "Te veel lenen leidt tot een schuldenspiraal en schuldbemiddeling.",
    ],
)


BUNDELS["het-persoonlijk-budget-en-je-administratie-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Het persoonlijk budget en je administratie",
    onder="Twee soorten inkomsten, vier soorten uitgaven, de zeven factoren bij een aankoopkeuze en de papieren die je bijhoudt.",
    secties=[
        dict(kop="Twee soorten inkomsten", blokken=[
            ("p", "Een budgetplan begint bij wat er binnenkomt. De fiche onderscheidt "
                  "<strong>twee soorten inkomsten</strong>:"),
            ("p", tabel(["Inkomst", "Wat ze is", "Voorbeeld"], [
                ["terugkerende inkomst", "ze komt regelmatig terug, dus je kan erop rekenen", "je loon elke maand"],
                ["toevallige inkomst", "ze komt één keer, dus je kan er niet op rekenen", "je verkoopt je oude fiets"],
            ])),
            ("kader", "Let op de woorden: <strong>terugkerend en toevallig</strong> gaan over de "
                      "<strong>inkomsten</strong>. <strong>Vast en variabel</strong> gaan over de "
                      "<strong>uitgaven</strong>. Dat is de verwisseling die in een examen het vaakst "
                      "wordt gemaakt."),
        ]),
        dict(kop="Vier soorten uitgaven", blokken=[
            ("p", "Bij de uitgaven zijn het er <strong>vier</strong>, niet twee."),
            ("p", tabel(["Uitgave", "Kenmerk", "Voorbeeld"], [
                ["vaste uitgave", "keert terug, altijd hetzelfde bedrag", "750 euro huur per maand"],
                ["variabele uitgave", "keert terug, met een wisselend bedrag", "je boodschappen"],
                ["onvoorziene uitgave", "je zag ze niet aankomen", "je ketel valt vandaag stuk"],
                ["uitzonderlijke uitgave", "ze komt zelden, maar je ziet ze aankomen", "een grote reis volgend jaar"],
            ])),
            ("p", "Het verschil tussen de laatste twee zit in dat <strong>aankomen</strong>: een "
                  "<strong>onvoorziene</strong> uitgave zie je <strong>niet</strong> aankomen, een "
                  "<strong>uitzonderlijke wel</strong>. Daarom kan je voor een uitzonderlijke uitgave "
                  "<strong>sparen</strong>, en kan je voor een onvoorziene enkel een "
                  "<strong>buffer</strong> klaarhouden."),
            ("weetje", "Een variabele uitgave is géén uitgave die wegblijft. Ze keert elke maand terug, "
                       "alleen staat er niet elke maand hetzelfde bedrag."),
        ]),
        dict(kop="Het budgetplan", blokken=[
            ("p", "Een <strong>budgetplan</strong> dient om <strong>zicht te krijgen op je inkomsten en "
                  "uitgaven</strong> en om te berekenen <strong>hoeveel je kan sparen</strong>. Het rekenwerk "
                  "is één aftrekking: alle inkomsten min alle uitgaven."),
            ("p", tabel(["Budget", "Berekening", "Blijft over"], [
                ["1 750 euro in, 1 480 euro uit", "1 750 − 1 480", "270 euro"],
                ["2 100 euro in, 900 euro vast, 650 euro variabel", "2 100 − 900 − 650", "550 euro"],
            ])),
            ("kader", "Wie in zijn budget <strong>enkel met zijn vaste uitgaven rekent</strong>, laat er "
                      "<strong>drie van de vier soorten</strong> uit: de variabele, de onvoorziene en de "
                      "uitzonderlijke. Zijn plan ziet er goed uit en klopt niet."),
        ]),
        dict(kop="Zeven factoren bij een aankoopkeuze", blokken=[
            ("p", "Wil je een grote aankoop <strong>verantwoorden</strong>, dan noemt de fiche "
                  "<strong>zeven factoren</strong>. Ze staan hier alfabetisch, zoals in de fiche."),
            ("p", tabel(["Factor", "De vraag die je stelt"], [
                ["aankoopkost", "wat kost het product zelf"],
                ["duurzaamheid", "hoelang gaat het mee, en wat betekent het voor het milieu"],
                ["financieringskost", "wat kost het me extra om te lenen in plaats van te betalen"],
                ["inflatie", "geld wordt minder waard, dus wat betekent wachten of sparen"],
                ["noodzakelijkheid", "heb ik dit echt nodig of wil ik het graag"],
                ["spaarbuffer", "hou ik genoeg over voor wat ik niet zag aankomen"],
                ["terugbetalingscapaciteit", "hoeveel kan ik maandelijks afbetalen zonder in de problemen te komen"],
            ])),
            ("p", "Twee van die zeven worden vaak door elkaar gehaald. De <strong>aankoopkost</strong> is "
                  "wat het <strong>product</strong> kost; de <strong>financieringskost</strong> is wat het "
                  "<strong>lenen</strong> erbovenop kost, dus de totale rente over de looptijd."),
            ("weetje", "Twijfel je tussen een wasmachine van 400 euro die zes jaar meegaat en een van "
                       "700 euro die vijftien jaar meegaat, dan weegt de <strong>duurzaamheid</strong> het "
                       "zwaarst: per jaar kost de duurste minder."),
            ("kader", "De <strong>terugbetalingscapaciteit</strong> is het bedrag dat je maandelijks kan "
                      "afbetalen zonder in de problemen te komen. De bank kijkt ernaar. Kijk er "
                      "<strong>zelf eerst</strong> naar."),
        ]),
        dict(kop="Je administratie", blokken=[
            ("p", "Drie documenten gelden volgens de fiche als <strong>aankoopbewijs</strong>: de "
                  "<strong>factuur</strong>, het <strong>kasticket</strong> en de "
                  "<strong>aankoopovereenkomst</strong>."),
            ("p", "Daarnaast hoort er meer bij je <strong>persoonlijke administratie</strong>:"),
            ("p", tabel(["Document", "Waarvoor je het bijhoudt"], [
                ["garantiebewijs", "een defect binnen de garantieperiode laten herstellen"],
                ["rekeninguittreksel", "nakijken wat er van je rekening ging en wat erop kwam"],
                ["verzekeringspolis", "weten wat er verzekerd is en wat niet"],
                ["loonstrook", "bewijzen wat je per maand verdiende"],
                ["individuele rekening", "het jaaroverzicht van wat je werkgever je betaalde"],
            ])),
            ("kader", "Het <strong>arbeidsreglement</strong> hoort hier <strong>niet</strong> bij: dat is "
                      "een document <strong>van het bedrijf</strong>, geen papier van je eigen "
                      "administratie."),
        ]),
    ],
    onthoud=[
        "Inkomsten zijn terugkerend of toevallig. Dat zijn er twee.",
        "Uitgaven zijn vast, variabel, onvoorzien of uitzonderlijk. Dat zijn er vier.",
        "Vast is elke maand hetzelfde bedrag; variabel keert terug met een wisselend bedrag.",
        "Onvoorzien zie je niet aankomen, uitzonderlijk wel. Daarom kan je voor uitzonderlijk sparen.",
        "Een budgetplan is inkomsten min uitgaven, en toont hoeveel je kan sparen.",
        "Zeven factoren: aankoopkost, duurzaamheid, financieringskost, inflatie, noodzakelijkheid, spaarbuffer, terugbetalingscapaciteit.",
        "De aankoopkost is het product, de financieringskost is het lenen.",
        "De terugbetalingscapaciteit is wat je maandelijks kan afbetalen zonder problemen.",
        "Aankoopbewijs: factuur, kasticket of aankoopovereenkomst.",
        "Het arbeidsreglement is van het bedrijf, niet van je eigen administratie.",
    ],
)


BUNDELS["sparen-beleggen-en-de-invloed-van-inflatie-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Sparen, beleggen en de invloed van inflatie",
    onder="Drie rekeningen, rente en samengestelde rente, vier beleggingsvormen en de vijf factoren bij de keuze.",
    secties=[
        dict(kop="Drie rekeningen", blokken=[
            ("p", "De fiche zet <strong>drie rekeningen</strong> naast elkaar. Ze verschillen in één ding: "
                  "<strong>hoe vlug je aan je geld kan</strong>."),
            ("p", tabel(["Rekening", "Waarvoor ze dient", "Aan je geld"], [
                ["zichtrekening", "je dagelijkse verrichtingen: loon ontvangen, facturen betalen", "altijd"],
                ["spaarrekening", "geld opzij zetten en toch nog kunnen opvragen", "snel, met rente"],
                ["termijnrekening", "geld een afgesproken tijd vastzetten", "pas na de termijn"],
            ])),
            ("p", "Daarom <strong>levert een termijnrekening meestal meer op</strong>: de bank weet "
                  "<strong>hoelang ze over je geld kan beschikken</strong> en betaalt daar meer voor. "
                  "<strong>Vroeger opvragen</strong> kan je er geld of rente kosten."),
            ("p", "Kiezen gaat dus op <strong>wanneer je het geld nodig hebt</strong>:"),
            ("p", tabel(["Situatie", "Rekening"], [
                ["ik moet er volgende maand een reis mee betalen", "zicht- of spaarrekening"],
                ["ik wil elke maand iets opzij zetten en er altijd aan kunnen", "spaarrekening"],
                ["ik heb dit geld de komende drie jaar zeker niet nodig", "termijnrekening"],
            ])),
        ]),
        dict(kop="Rente en samengestelde rente", blokken=[
            ("p", "<strong>Rente</strong> is de <strong>vergoeding voor het gebruik van geld</strong>. "
                  "Wie <strong>spaart krijgt</strong> ze; wie <strong>leent betaalt</strong> ze."),
            ("p", "Rekenen is een percentage nemen van het bedrag:"),
            ("p", tabel(["Bedrag", "Rentevoet", "Rente na één jaar"], [
                ["2 000 euro", "2 %", "40 euro"],
                ["5 000 euro", "3 %", "150 euro"],
            ])),
            ("p", "<strong>Samengestelde rente</strong> is rente die je <strong>ook op de rente van de "
                  "vorige jaren</strong> krijgt. Daardoor groeit een spaarpot "
                  "<strong>sneller naarmate hij langer blijft staan</strong>."),
            ("weetje", "Bij samengestelde rente werkt de tijd voor je. Dat is de enige reden waarom vroeg "
                       "beginnen sparen echt iets uithaalt."),
        ]),
        dict(kop="Inflatie", blokken=[
            ("p", "<strong>Inflatie</strong> is de <strong>algemene stijging van de prijzen</strong>, "
                  "waardoor <strong>geld minder waard wordt</strong>. Met hetzelfde bedrag koop je na een "
                  "jaar inflatie <strong>minder</strong> dan ervoor."),
            ("kader", "Staat je spaarrente op <strong>2 procent</strong> en de inflatie op "
                      "<strong>3 procent</strong>, dan <strong>daalt je koopkracht</strong>: je hebt meer "
                      "euro's en je kan er minder mee kopen. Je spaargeld groeit in cijfers en krimpt in "
                      "waarde."),
            ("p", "Daarom staat de inflatie <strong>twee keer</strong> in dit vak: bij de "
                  "<strong>zeven factoren van een aankoopkeuze</strong> en bij de <strong>vijf factoren "
                  "van sparen of beleggen</strong>."),
        ]),
        dict(kop="Vier beleggingsvormen", blokken=[
            ("p", "De fiche noemt <strong>vier</strong> beleggingsvormen. Een spaarrekening staat er niet "
                  "bij: <strong>sparen is geen beleggen</strong>."),
            ("p", tabel(["Vorm", "Wat je hebt", "Risico"], [
                ["obligatie", "een lening aan een bedrijf of een overheid, met een afgesproken rente", "doorgaans lager"],
                ["beleggingsfonds", "een mand met veel verschillende beleggingen samen", "gespreid"],
                ["beursaandeel", "een stukje eigendom van een bedrijf", "hoger"],
                ["cryptomunt", "een digitale munt zonder centrale bank", "het hoogst van de vier"],
            ])),
            ("p", "Het verschil tussen de eerste en de derde is wie je bent: bij een "
                  "<strong>obligatie</strong> ben je <strong>schuldeiser</strong>, bij een "
                  "<strong>aandeel mede-eigenaar</strong>. Gaat het bedrijf goed, dan stijgt je aandeel; "
                  "gaat het slecht, dan daalt het."),
            ("p", "Een <strong>beleggingsfonds</strong> bestaat <strong>niet</strong> uit één belegging: "
                  "het is net een <strong>mand</strong>, zodat <strong>één slechte belegging minder zwaar "
                  "doorweegt</strong>. Dat heet spreiden."),
            ("kader", "<strong>Risico en rendement</strong> gaan samen: meer <strong>kans</strong> op "
                      "opbrengst betekent meer <strong>kans</strong> op verlies. Let op dat woord "
                      "<strong>kans</strong>. Een hoger risico <strong>garandeert geen</strong> hogere "
                      "opbrengst."),
        ]),
        dict(kop="Vijf factoren bij de keuze", blokken=[
            ("p", "Sparen of beleggen? De fiche noemt <strong>vijf factoren</strong>:"),
            ("p", tabel(["Factor", "De vraag die je stelt"], [
                ["de duur", "hoelang kan ik dit geld missen"],
                ["de rentevoet en de inflatie", "wat houd ik er netto aan over"],
                ["het risico", "hoeveel schommeling kan ik aan"],
                ["mijn financieel doel", "waarvoor spaar of beleg ik, een studie of een woning"],
                ["mijn kennis van de markt", "begrijp ik waarin ik stap"],
            ])),
            ("p", "De laatste is de eenvoudigste beschermingsregel die bestaat: "
                  "<strong>beleg niet in iets wat je niet begrijpt</strong>."),
            ("weetje", "Iemand van achttien die spaart voor een woning over twintig jaar en tegen "
                       "schommelingen kan, mag volgens die factoren <strong>een deel beleggen</strong>: de "
                       "lange termijn en de risicobereidheid wijzen die kant op. Alles in één munt steken is "
                       "geen spreiding, maar een gok."),
        ]),
    ],
    onthoud=[
        "Zichtrekening: dagelijkse verrichtingen. Spaarrekening: opzij en toch beschikbaar. Termijnrekening: vastgezet.",
        "Een termijnrekening levert meer op omdat de bank weet hoelang ze over je geld beschikt.",
        "Rente is de vergoeding voor het gebruik van geld: sparen levert ze op, lenen kost ze.",
        "Samengestelde rente is rente op je eerder verdiende rente.",
        "Inflatie is de algemene prijsstijging; je spaargeld verliest koopkracht.",
        "Rente 2 % en inflatie 3 %: meer euro's, minder koopkracht.",
        "Vier beleggingen: obligatie, beleggingsfonds, beursaandeel en cryptomunt.",
        "Obligatie: je bent schuldeiser. Aandeel: je bent mede-eigenaar.",
        "Meer risico geeft meer kans op winst én meer kans op verlies.",
        "Vijf factoren: duur, rentevoet en inflatie, risico, financieel doel en je kennis van de markt.",
    ],
)


BUNDELS["verzekeringen-een-schadegeval-en-de-polis-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Verzekeringen, een schadegeval en de polis",
    onder="Vijf verzekeringen, het verschil tussen verantwoordelijk en aansprakelijk, de schadeaangifte en wie wie is in een polis.",
    secties=[
        dict(kop="Waarom je je verzekert", blokken=[
            ("p", "Een verzekering bestaat om een <strong>schade te kunnen dragen die je zelf niet zou "
                  "kunnen betalen</strong>. Je betaalt een <strong>kleine premie</strong> om een "
                  "<strong>groot risico</strong> niet alleen te moeten dragen."),
            ("p", "Twee woorden die in dit thema nooit hetzelfde betekenen:"),
            ("p", tabel(["Woord", "Wat het betekent"], [
                ["verantwoordelijk", "wie het gedaan heeft"],
                ["juridisch aansprakelijk", "wie er volgens de wet voor opdraait en de schade vergoedt"],
            ])),
            ("kader", "Een <strong>kind van zes</strong> trapt een bal door het raam van de buren. Het "
                      "<strong>kind is verantwoordelijk</strong> voor wat het deed, de "
                      "<strong>ouders zijn juridisch aansprakelijk</strong> voor de schade. Verantwoordelijk "
                      "en aansprakelijk zijn dus niet altijd dezelfde persoon."),
        ]),
        dict(kop="Vijf verzekeringen", blokken=[
            ("p", "De fiche noemt <strong>vijf</strong> verzekeringen. Een hospitalisatie- of "
                  "reisverzekering staat er niet bij."),
            ("p", tabel(["Verzekering", "Wat ze dekt", "Voorbeeld"], [
                ["autoverzekering", "schade met een auto", "je rijdt tegen een paaltje"],
                ["verzekering bromfiets", "schade met een bromfiets", "je rijdt tegen een geparkeerde auto"],
                ["brandverzekering", "schade aan de woning, en meer dan brand alleen", "waterschade door brand bij de buren"],
                ["familiale verzekering", "schade die jij of je gezin aan iemand anders toebrengt in het dagelijks leven", "een bal door het raam van de buren"],
                ["rechtsbijstandsverzekering", "de kosten van een advocaat en een juridische procedure", "een geschil na een ongeval"],
            ])),
            ("kader", "De <strong>familiale verzekering</strong> dekt <strong>nooit</strong> schade met een "
                      "<strong>motorvoertuig</strong>. Een auto en een bromfiets hebben hun eigen "
                      "verzekering; de familiale is er voor het dagelijks leven."),
        ]),
        dict(kop="De schadeaangifte", blokken=[
            ("p", "Loopt er iets mis, dan doe je een <strong>schadeaangifte</strong>. Deze gegevens "
                  "noemt de fiche:"),
            ("p", tabel(["Gegeven", "Waarvoor het dient"], [
                ["de datum en het uur", "vastleggen wanneer het precies gebeurde"],
                ["de aard van de schade", "wat er precies beschadigd is en hoe"],
                ["de getuige", "achteraf kunnen vaststellen wat er gebeurd is"],
                ["de verantwoordelijke", "wie het gedaan heeft"],
                ["de juridisch aansprakelijke", "wie er volgens de wet voor moet opdraaien"],
                ["de begunstigde", "wie de uitbetaling ontvangt"],
            ])),
            ("weetje", "Bij <strong>onenigheid</strong> over wie wat deed, weegt een "
                       "<strong>onafhankelijke getuige</strong> zwaar. Daarom vraagt een aangifte er "
                       "uitdrukkelijk naar."),
        ]),
        dict(kop="Wie wie is in een polis", blokken=[
            ("p", "De <strong>polis</strong> is het <strong>contract</strong> waarin je verzekering "
                  "beschreven staat: <strong>wie verzekerd is, waartegen, en voor hoeveel</strong>. "
                  "Vier rollen, en ze vallen niet altijd samen."),
            ("p", tabel(["Rol", "Wie dat is"], [
                ["de verzekeringsnemer", "wie het contract afsluit en de premie betaalt"],
                ["de verzekerde", "de persoon die door de verzekering gedekt is"],
                ["de verzekeraar", "de maatschappij die het risico draagt en uitbetaalt"],
                ["de begunstigde", "wie de uitbetaling ontvangt"],
            ])),
            ("kader", "Een <strong>moeder</strong> sluit een familiale verzekering af waarin ook haar "
                      "<strong>dochter</strong> gedekt is. De moeder is "
                      "<strong>verzekeringsnemer</strong>, de dochter is <strong>verzekerde</strong>. "
                      "Nemer en verzekerde zijn dikwijls dezelfde persoon, maar niet altijd."),
        ]),
        dict(kop="Premie, franchise en het verzekerd risico", blokken=[
            ("p", "Twee bedragen die de tegengestelde richting opgaan: de <strong>premie</strong> is "
                  "<strong>wat je betaalt om verzekerd te zijn</strong>, en gaat van jou naar de "
                  "verzekeraar. De <strong>schadevergoeding</strong> is wat je ontvangt, en gaat de "
                  "andere kant op."),
            ("p", "De <strong>franchise</strong> is het <strong>deel van de schade dat je zelf "
                  "draagt</strong>. Ze wordt van de schadevergoeding afgetrokken:"),
            ("p", tabel(["Schade", "Franchise", "De verzekeraar betaalt"], [
                ["800 euro", "200 euro", "600 euro"],
                ["1 500 euro", "250 euro", "1 250 euro"],
                ["900 euro", "150 euro", "750 euro"],
            ])),
            ("p", "Een franchise bestaat om <strong>kleine schades niet door de verzekering te laten "
                  "lopen</strong>. Daardoor blijft de premie lager voor iedereen, en gaat een "
                  "<strong>hogere franchise meestal samen met een lagere premie</strong>: je draagt meer "
                  "zelf, dus de verzekeraar loopt minder risico."),
            ("p", "Het <strong>verzekerd risico</strong> is <strong>waartegen je precies verzekerd "
                  "bent</strong> volgens de polis."),
            ("kader", "Staat iets <strong>niet</strong> bij het verzekerd risico, dan is het "
                      "<strong>niet gedekt</strong>. Hoe ernstig de schade ook is: de polis bepaalt wat "
                      "verzekerd is, niet de omvang van het ongeluk."),
        ]),
    ],
    onthoud=[
        "Verantwoordelijk is wie het deed; juridisch aansprakelijk is wie er volgens de wet voor opdraait.",
        "Bij een jong kind: het kind verantwoordelijk, de ouders aansprakelijk.",
        "Vijf verzekeringen: auto, bromfiets, brand, familiale en rechtsbijstand.",
        "De familiale dekt het dagelijks leven, nooit schade met een motorvoertuig.",
        "In een schadeaangifte: datum en uur, aard van de schade, getuige, verantwoordelijke, aansprakelijke en begunstigde.",
        "De polis is het contract: wie verzekerd is, waartegen en voor hoeveel.",
        "Nemer sluit af en betaalt, verzekerde is gedekt, verzekeraar betaalt uit, begunstigde ontvangt.",
        "De premie betaal je; de schadevergoeding ontvang je.",
        "De franchise draag je zelf en gaat van de vergoeding af. Hogere franchise, lagere premie.",
        "Wat niet in het verzekerd risico staat, is niet gedekt.",
    ],
)


BUNDELS["tekstverwerking-met-word-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Tekstverwerking met Word",
    onder="Tekenopmaak tegenover alineaopmaak, de paginaopmaak, tabellen en opslaan als PDF.",
    secties=[
        dict(kop="Geen computerwerk, wel kennis", blokken=[
            ("p", "Dit thema vraagt <strong>geen werk in het programma zelf</strong>. De vakfiche zegt het "
                  "letterlijk: je werkt niet met de programma's, je krijgt "
                  "<strong>schermafdrukken</strong> uit Windows 10 en MS Office 365. Je moet dus "
                  "<strong>weten hoe iets heet en wat een knop doet</strong>."),
        ]),
        dict(kop="Tekenopmaak tegenover alineaopmaak", blokken=[
            ("p", "Dit is het onderscheid waar het hele thema op draait. "
                  "<strong>Tekenopmaak</strong> werkt op de <strong>geselecteerde letters</strong>, "
                  "<strong>alineaopmaak</strong> op de <strong>hele alinea</strong>."),
            ("p", tabel(["Tekenopmaak", "Alineaopmaak"], [
                ["vet, cursief, onderstrepen", "uitlijning"],
                ["lettertype en tekengrootte", "regelafstand"],
                ["tekstkleur en markeren", "inspringen"],
                ["doorhalen", "de afstand tussen alinea's"],
                ["superscript en subscript", "tekstdoorloop"],
            ])),
            ("kader", "Een gevolg dat je moet kennen: voor <strong>regelafstand hoef je niets te "
                      "selecteren</strong>, want het is alineaopmaak en je <strong>cursor in de "
                      "alinea</strong> volstaat. Wil je <strong>één woord</strong> midden in een zin vet, "
                      "dan moet je dat woord wél <strong>selecteren</strong>: vet is tekenopmaak."),
        ]),
        dict(kop="Tekenopmaak van dichtbij", blokken=[
            ("p", tabel(["Opmaak", "Wat ze doet", "Voorbeeld"], [
                ["superscript", "kleine tekens iets boven de regel", "m²"],
                ["subscript", "kleine tekens iets onder de regel", "H₂O"],
                ["markeren", "een gekleurde achtergrond achter de tekst, als met een fluostift", None],
                ["tekstkleur", "de letters zelf een kleur geven", None],
                ["doorhalen", "een streep door de tekst, die leesbaar blijft", None],
            ])),
            ("p", "<strong>Markeren en tekstkleur</strong> doen dus <strong>niet</strong> hetzelfde: "
                  "markeren <strong>verft de achtergrond</strong>, tekstkleur <strong>verft de "
                  "letters</strong>."),
            ("weetje", "<strong>Doorhalen</strong> is handig om te tonen wat geschrapt is zonder het weg "
                       "te gooien. De lezer ziet nog wat er stond."),
        ]),
        dict(kop="Alineaopmaak van dichtbij", blokken=[
            ("p", "Er zijn <strong>vier uitlijningen</strong>: <strong>links</strong>, "
                  "<strong>gecentreerd</strong>, <strong>rechts</strong> en <strong>uitvullen</strong>. "
                  "Bij <strong>uitvullen</strong> sluit de tekst <strong>links én rechts</strong> netjes "
                  "aan: Word rekt de spaties op zodat beide kanten recht zijn."),
            ("p", "<strong>Inspringen</strong> laat de alinea <strong>verder van de marge "
                  "beginnen</strong> — links, rechts, of enkel op de eerste regel."),
            ("p", "En twee afstanden die vlug verward worden:"),
            ("p", tabel(["Afstand", "Waar ze zit"], [
                ["regelafstand", "tussen de regels binnen één alinea"],
                ["afstand tussen alinea's", "de witruimte boven en onder een alinea"],
            ])),
            ("p", "Een <strong>opsomming</strong> kan je invoegen én achteraf nog "
                  "<strong>wijzigen</strong>; dat vraagt de fiche uitdrukkelijk."),
        ]),
        dict(kop="Paginaopmaak en kop- en voettekst", blokken=[
            ("p", "De <strong>paginaopmaak</strong> bestaat uit <strong>drie</strong> dingen:"),
            ("p", tabel(["Onderdeel", "Wat je instelt"], [
                ["marges", "de witte rand rond de tekst op een blad"],
                ["afdrukstand", "staand of liggend, ook portret of landschap"],
                ["formaat", "de bladgrootte, bijvoorbeeld A4 of A5"],
            ])),
            ("p", "Een <strong>kop- en voettekst</strong> is tekst die <strong>bovenaan of onderaan op "
                  "elke bladzijde</strong> terugkomt. Ideaal voor een paginanummer of de naam van je "
                  "document."),
            ("kader", "Gebruik <strong>automatische paginanummering</strong>: de nummers "
                      "<strong>passen zich aan</strong> als het document langer of korter wordt. Voeg je "
                      "vooraan een blad toe aan een document van twaalf bladzijden, dan schuiven alle "
                      "nummers vanzelf op. Zelf nummers typen betekent alles hertypen."),
        ]),
        dict(kop="Tabellen, afdrukken en PDF", blokken=[
            ("p", "Bij een tabel hoort een <strong>ontwerp</strong> en een <strong>indeling</strong>:"),
            ("p", tabel(["Wat je doet", "Wat het betekent"], [
                ["randen", "de lijnen rond en in de cellen"],
                ["arcering", "een kleur of patroon als achtergrond van een cel"],
                ["rijen en kolommen toevoegen of verwijderen", "de tabel groter of kleiner maken"],
                ["cellen samenvoegen", "van meerdere cellen één grotere maken"],
                ["cellen splitsen", "van één cel meerdere maken"],
            ])),
            ("p", "<strong>Samenvoegen en splitsen</strong> zijn dus het omgekeerde van elkaar. Wil je een "
                  "<strong>titel over drie kolommen</strong> laten lopen, dan "
                  "<strong>voeg je de drie cellen van de bovenste rij samen</strong>."),
            ("p", "Bij het <strong>afdrukken</strong> stel je volgens de fiche in: de "
                  "<strong>sortering</strong>, <strong>enkel- of dubbelzijdig</strong>, en "
                  "<strong>kleur</strong>."),
            ("kader", "Je slaat op als <strong>PDF</strong> zodat de <strong>opmaak overal hetzelfde "
                      "blijft</strong> en niemand het document zomaar wijzigt. Daarom stuur je een PDF "
                      "door of laat je er iets mee drukken — en daarom bewerk je een PDF in Word "
                      "<strong>niet</strong> even makkelijk als een gewoon document."),
        ]),
    ],
    onthoud=[
        "Tekenopmaak werkt op de selectie, alineaopmaak op de hele alinea.",
        "Tekenopmaak: vet, cursief, onderstrepen, lettertype, tekengrootte, tekstkleur, markeren, doorhalen, super- en subscript.",
        "Alineaopmaak: uitlijning, regelafstand, inspringen, afstand tussen alinea's en tekstdoorloop.",
        "Superscript staat boven de regel (m²), subscript eronder (H₂O).",
        "Markeren kleurt de achtergrond, tekstkleur kleurt de letters.",
        "Uitvullen laat de tekst links én rechts aansluiten.",
        "Paginaopmaak: marges, afdrukstand en formaat.",
        "Automatische paginanummering schuift mee als er een blad bijkomt.",
        "Arcering is de vulling van een cel, randen zijn de lijnen.",
        "PDF zet de opmaak vast; je bewerkt het niet zomaar.",
    ],
)


BUNDELS["het-rekenblad-excel-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Het rekenblad Excel",
    onder="De bouw van een rekenblad, getalnotaties, formules met relatieve en absolute adressen, zes functies en vijf grafieken.",
    secties=[
        dict(kop="De bouw van een rekenblad", blokken=[
            ("p", "Ook hier geldt: <strong>geen computerwerk</strong>. Je krijgt "
                  "<strong>schermafdrukken</strong> en je moet <strong>weten hoe iets heet</strong> en "
                  "wat het doet."),
            ("p", tabel(["Begrip", "Wat het is", "Voorbeeld"], [
                ["cel", "het vakje waar een rij en een kolom elkaar kruisen", None],
                ["celadres", "de kolomletter en het rijnummer samen", "B7"],
                ["bereik", "een groep cellen samen, met een dubbelpunt genoteerd", "A1:A10"],
                ["werkblad", "één tabblad in het bestand", None],
                ["werkmap", "het bestand zelf, met al zijn tabbladen", None],
            ])),
            ("kader", "Twee notatiefouten die vaak gemaakt worden. Een celadres zet "
                      "<strong>eerst de letter</strong> en dan het nummer: B7, niet 7B. En een bereik "
                      "krijgt een <strong>dubbelpunt</strong>, geen puntkomma: <strong>C2:C9</strong>. "
                      "De puntkomma dient om <strong>losse argumenten</strong> in een functie te scheiden."),
            ("p", "De <strong>vulgreep</strong> is het <strong>vierkantje rechtsonder in de "
                  "selectie</strong>. Sleep eraan en je trekt <strong>gegevens of formules</strong> door "
                  "naar de volgende cellen."),
            ("weetje", "Wil je een <strong>nieuwe rij tussen rij 4 en rij 5</strong>, dan selecteer je "
                       "<strong>rij 5</strong> en voeg je een rij in: een nieuwe rij komt "
                       "<strong>boven</strong> de geselecteerde rij."),
        ]),
        dict(kop="Getalnotatie en celopmaak", blokken=[
            ("p", "Een <strong>getalnotatie</strong> bepaalt <strong>hoe</strong> een getal in beeld komt, "
                  "niet wat het is."),
            ("p", tabel(["Notatie", "Waarvoor", "Je typt 0,25 en ziet"], [
                ["valuta", "een bedrag, met het muntteken erbij en netjes uitgelijnd", None],
                ["percentage", "een percentage: het getal maal honderd met een procentteken", "25%"],
                ["datum en tijd", "een datum of een uur", None],
                ["aantal decimalen", "hoeveel cijfers er na de komma komen", None],
            ])),
            ("p", "Bij de <strong>celopmaak</strong> horen nog drie dingen:"),
            ("p", tabel(["Opmaak", "Wat ze doet"], [
                ["voorwaardelijke opmaak", "een cel automatisch opmaken als de inhoud aan een voorwaarde voldoet"],
                ["samenvoegen en centreren", "van meerdere cellen één cel maken met de tekst in het midden"],
                ["tekststand", "de hoek waaronder de tekst in de cel staat"],
            ])),
            ("kader", "<strong>Voorwaardelijke opmaak verandert de waarde niet</strong>, enkel het "
                      "uitzicht. Zet je alle negatieve getallen in het rood, dan blijft er "
                      "gewoon −45 staan; het is alleen rood."),
        ]),
        dict(kop="Formules", blokken=[
            ("p", "Elke formule begint met een <strong>isgelijkteken</strong>. Zonder dat teken ziet Excel "
                  "<strong>enkel tekst</strong> en rekent het niets uit."),
            ("p", "De <strong>operatoren</strong> van de fiche: <strong>*</strong> (maal), "
                  "<strong>−</strong> (min), <strong>+</strong> (plus), <strong>/</strong> (gedeeld door) "
                  "en <strong>( )</strong> (haakjes)."),
            ("p", "Het belangrijkste onderscheid in dit thema is dat tussen "
                  "<strong>relatief</strong> en <strong>absoluut</strong> adresseren:"),
            ("p", tabel(["Verwijzing", "Wat er gebeurt als je de formule kopieert"], [
                ["A1", "relatief: ze schuift mee"],
                ["$A$1", "absoluut: ze blijft naar dezelfde cel wijzen"],
            ])),
            ("p", "Het <strong>dollarteken zet vast wat erachter komt</strong>: de kolom, de rij of "
                  "allebei."),
            ("kader", "Staat in <strong>C1 het btw-percentage</strong> en wil je in een hele kolom de btw "
                      "berekenen, dan verwijs je met <strong>dollartekens</strong> naar C1. Zonder zou C1 "
                      "mee opschuiven naar C2, C3 en zo verder, en dan reken je met een leeg vakje."),
            ("p", "Staat in <strong>B2</strong> de formule <strong>=SOM(A1:A3)</strong> en sleep je ze "
                  "naar <strong>B3</strong>, dan staat er <strong>=SOM(A2:A4)</strong>: de verwijzingen "
                  "zijn relatief, dus ze schuiven één rij mee naar beneden."),
        ]),
        dict(kop="Zes functies", blokken=[
            ("p", tabel(["Functie", "Wat ze doet", "Voorbeeld"], [
                ["SOM", "alle getallen in een bereik optellen", "=SOM(B2:B10)"],
                ["GEMIDDELDE", "de getallen optellen en delen door hun aantal", None],
                ["MIN", "het kleinste getal uit een bereik geven", None],
                ["MAX", "het grootste getal uit een bereik geven", None],
                ["ALS", "een ander resultaat geven naargelang een voorwaarde waar of niet waar is",
                 '=ALS(B2&gt;=50;"geslaagd";"niet geslaagd")'],
                ["VERT.ZOEKEN", "een waarde opzoeken in de eerste kolom van een tabel en iets uit dezelfde rij teruggeven", None],
            ])),
            ("p", "<strong>Vert</strong> staat voor <strong>verticaal</strong>: VERT.ZOEKEN zoekt "
                  "<strong>naar beneden in een kolom</strong>."),
            ("weetje", "<strong>GEMIDDELDE</strong> is niet het middelste getal: dat is de "
                       "<strong>mediaan</strong>, en daarvoor bestaat een andere functie. En GEMIDDELDE en "
                       "MIN vallen enkel samen als <strong>alle getallen gelijk</strong> zijn."),
        ]),
        dict(kop="Grafieken", blokken=[
            ("p", "De fiche noemt <strong>vijf</strong> grafiektypes. De vraag is altijd: "
                  "<strong>wat wil je tonen</strong>?"),
            ("p", tabel(["Grafiek", "Waarvoor ze past"], [
                ["kolomgrafiek", "waarden naast elkaar vergelijken, staand"],
                ["staafgrafiek", "waarden naast elkaar vergelijken, liggend"],
                ["lijngrafiek", "een evolutie in de tijd: hoe iets stijgt of daalt"],
                ["cirkeldiagram", "het aandeel van elk deel in een geheel, samen honderd procent"],
                ["spreiding", "het verband tussen twee reeksen getallen"],
            ])),
            ("kader", "Een <strong>boxplot</strong> staat <strong>niet</strong> in deze fiche. Noem er dus "
                      "geen bij wat Excel volgens dit vak kan: de vijf hierboven zijn de lijst."),
        ]),
    ],
    onthoud=[
        "Cel, celadres (B7), bereik met een dubbelpunt (A1:A10), werkblad en werkmap.",
        "De werkmap is het bestand, een werkblad is één tabblad erin.",
        "De vulgreep is het vierkantje rechtsonder; ze trekt gegevens én formules door.",
        "Notaties: valuta, percentage, datum en tijd, en het aantal decimalen.",
        "Voorwaardelijke opmaak verandert het uitzicht, nooit de waarde.",
        "Elke formule begint met een isgelijkteken.",
        "A1 schuift mee als je kopieert, $A$1 blijft staan.",
        "Functies: SOM, GEMIDDELDE, MIN, MAX, ALS en VERT.ZOEKEN.",
        "VERT.ZOEKEN zoekt verticaal in de eerste kolom van een tabel.",
        "Grafieken: kolom, staaf, lijn, cirkel en spreiding. Cirkel voor delen van een geheel, lijn voor evolutie.",
    ],
)


BUNDELS["presenteren-met-powerpoint-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Presenteren met PowerPoint",
    onder="Dia's bewerken, overgang tegenover animatie, hyperlinks en actieknoppen, de weergaven, de afdrukken en pptx tegenover ppsm.",
    secties=[
        dict(kop="Een dia en zijn indeling", blokken=[
            ("p", "Een <strong>dia</strong> is <strong>één bladzijde van je presentatie</strong>, die je "
                  "straks op het scherm toont. Een presentatie is een reeks dia's na elkaar."),
            ("p", "De <strong>indeling</strong> van een dia is het <strong>vaste patroon van vakken</strong> "
                  "voor een titel, tekst en beeld. In het Engels de <strong>lay-out</strong>. Je kiest ze "
                  "per dia en je kan ze <strong>achteraf nog wijzigen</strong>."),
            ("p", "De <strong>basisbewerkingen</strong> van de fiche:"),
            ("p", tabel(["Bewerking", "Wat ze doet"], [
                ["een nieuwe dia invoegen", "er een dia bij zetten"],
                ["de indeling en de opmaak aanpassen", "de vakken en het uitzicht van die dia veranderen"],
                ["een dia verwijderen", "de dia weghalen"],
                ["een dia dupliceren", "er een exacte kopie bij zetten, met dezelfde inhoud en opmaak"],
                ["diaovergangen aanpassen", "het effect tussen twee dia's instellen"],
                ["animaties toevoegen", "iets op de dia zelf laten bewegen of verschijnen"],
            ])),
            ("kader", "<strong>Dupliceren is niet verwijderen.</strong> Dupliceren zet er een kopie bij, "
                      "verwijderen haalt de dia weg. Verwijder je dia 3 uit een presentatie van tien, dan "
                      "hou je <strong>negen</strong> dia's over en <strong>schuift dia 4 op naar "
                      "plaats 3</strong>."),
            ("weetje", "Dupliceren is net handig als je een dia wil die <strong>bijna</strong> hetzelfde "
                       "is: eerst kopiëren, dan het ene stuk aanpassen."),
        ]),
        dict(kop="Overgang tegenover animatie", blokken=[
            ("p", "Dit is het verschil waarop in schermafdrukken het vaakst getoetst wordt:"),
            ("p", tabel(["Effect", "Waar het werkt"], [
                ["diaovergang", "tussen twee dia's, bij het wisselen naar de volgende"],
                ["animatie", "op de dia zelf, op een tekstvak, een beeld of een vorm"],
            ])),
            ("p", "Omdat een animatie op iets <strong>op</strong> de dia werkt, kan je er op één dia "
                  "<strong>verschillende na elkaar</strong> laten lopen. Wil je dat de tekst "
                  "<strong>één regel per keer verschijnt</strong>, dan voeg je dus een "
                  "<strong>animatie</strong> toe, geen overgang."),
            ("kader", "Een <strong>diaovergang</strong> stel je <strong>per dia</strong> in, of met één "
                      "knop op <strong>alle</strong> dia's tegelijk. Het is dus niet alles of niets."),
        ]),
        dict(kop="Tekstvakken, vormen en het ontwerp", blokken=[
            ("p", "Een <strong>tekstvak</strong> is een <strong>kader waarin je tekst zet</strong> en dat "
                  "je op de dia kan <strong>verplaatsen</strong>, vergroten en opmaken. Zonder tekstvak "
                  "krijg je geen tekst op een dia."),
            ("p", "Een <strong>vorm</strong> voeg je in om met een <strong>pijl, kader of cirkel</strong> "
                  "iets aan te duiden. Een pijl naar het belangrijkste cijfer doet meer dan een zin erbij."),
            ("p", "Wil je op <strong>elke</strong> dia dezelfde achtergrond en hetzelfde lettertype, dan "
                  "kies je een <strong>thema of ontwerp dat voor de hele presentatie geldt</strong>. Zo "
                  "blijft alles één geheel en doe je het niet dia per dia."),
            ("weetje", "Staat een dia <strong>volgeschreven in kleine letters</strong>, dan is de beste "
                       "aanpassing de tekst <strong>over meerdere dia's verdelen</strong> en groter laten "
                       "staan. Een dia is geen blad papier: wat je voorleest hoort niet voluit op het "
                       "scherm."),
        ]),
        dict(kop="Hyperlinks en actieknoppen", blokken=[
            ("p", tabel(["Element", "Wat het doet"], [
                ["hyperlink", "je klikt erop en komt op een website, of op een andere dia uit"],
                ["actieknop", "een knop die je zelf op de dia zet en die bij een klik iets uitvoert"],
            ])),
            ("p", "Een <strong>hyperlink</strong> wijst dus <strong>niet alleen naar buiten</strong>: hij "
                  "kan ook naar een <strong>dia in dezelfde presentatie</strong> verwijzen. Zo bouw je een "
                  "presentatie waarin je zelf kan kiezen waar je naartoe gaat."),
            ("kader", "Wil je tijdens het presenteren <strong>met één klik naar een dia achteraan</strong> "
                      "springen, dan zet je daarvoor vooraf een <strong>hyperlink of een "
                      "actieknop</strong> klaar. Anders moet je door alle dia's ertussen klikken."),
        ]),
        dict(kop="Presenteren en de weergaven", blokken=[
            ("p", "Een <strong>diavoorstelling</strong> kan je starten <strong>vanaf de eerste dia</strong> "
                  "of <strong>vanaf de dia waar je staat</strong>. Dat tweede is handig bij het nakijken."),
            ("p", tabel(["Weergave", "Waarvoor ze dient"], [
                ["presentatorweergave", "jij ziet de dia met je notities erbij, het publiek enkel de dia"],
                ["diasorteerder", "alle dia's als miniaturen naast elkaar, om de volgorde te veranderen"],
            ])),
            ("p", "In de <strong>diasorteerder</strong> sleep je een dia naar zijn nieuwe plaats."),
        ]),
        dict(kop="Afdrukken en bewaren", blokken=[
            ("p", "De fiche noemt <strong>drie</strong> soorten afdrukken. Het verschil zit in "
                  "<strong>voor wie</strong> ze zijn:"),
            ("p", tabel(["Afdruk", "Wat erop staat", "Voor wie"], [
                ["hand-out", "meerdere dia's op één blad", "het publiek, om mee te lezen en bij te schrijven"],
                ["notitiepagina", "één dia met jouw notities eronder", "de spreker"],
                ["overzicht", "enkel de tekst van de dia's, zonder beelden en opmaak", "om je verhaal na te lezen"],
            ])),
            ("kader", "Een <strong>hand-out en een notitiepagina</strong> zijn dus <strong>niet</strong> "
                      "hetzelfde: de hand-out is <strong>voor het publiek</strong>, de notitiepagina "
                      "<strong>voor jou</strong>. En <strong>etiketten</strong> horen bij een "
                      "tekstverwerker, niet bij een presentatie."),
            ("p", "Bewaren kan in verschillende <strong>bestandsindelingen</strong>:"),
            ("p", tabel(["Indeling", "Wat er gebeurt bij het openen"], [
                ["pptx", "de presentatie opent om te bewerken"],
                ["ppsm", "de presentatie start meteen als diavoorstelling"],
            ])),
            ("p", "De <strong>s</strong> in ppsm staat voor <strong>show</strong>. Handig op een beurs of "
                  "in een wachtzaal: dubbelklikken en het loopt."),
        ]),
    ],
    onthoud=[
        "Een dia is één bladzijde; de indeling is het patroon van vakken erop, en je kan ze achteraf wijzigen.",
        "Dupliceren zet een kopie bij, verwijderen haalt de dia weg en de volgende schuiven op.",
        "Een diaovergang werkt tussen twee dia's, een animatie op de dia zelf.",
        "Een overgang stel je per dia in of met één knop op alle dia's.",
        "Een tekstvak is het kader voor tekst; een vorm duidt iets aan met een pijl of kader.",
        "Een hyperlink kan ook naar een andere dia in dezelfde presentatie wijzen.",
        "Een actieknop zet je zelf op de dia en voert bij een klik iets uit.",
        "Presentatorweergave: jij ziet je notities. Diasorteerder: je verandert de volgorde.",
        "Hand-out voor het publiek, notitiepagina voor de spreker, overzicht is enkel de tekst.",
        "Een pptx opent om te bewerken, een ppsm start meteen als voorstelling.",
    ],
)


BUNDELS["veilig-en-correct-online-recht-phishing-en-netiquette-beyond-doorstroom"] = dict(
    vak=VAK, niveau=BEYOND, titel="Veilig en correct online: recht, phishing en netiquette",
    onder="Auteursrecht, creative commons, portretrecht en privacy, en daarnaast wachtwoorden, phishing, nepnieuws, cyberpesten en netiquette.",
    secties=[
        dict(kop="Auteursrecht", blokken=[
            ("p", "Het <strong>auteursrecht</strong> is het recht van <strong>wie een werk gemaakt "
                  "heeft</strong> om erover te beslissen. Je krijgt het "
                  "<strong>automatisch</strong>, zodra je iets eigen gemaakt hebt: "
                  "<strong>aanvragen hoeft niet</strong>."),
            ("p", "Het blijft gelden tot <strong>zeventig jaar na het overlijden van de maker</strong>. "
                  "Daarna is het werk vrij, en daarom kan je oude boeken en schilderijen wel vrij "
                  "gebruiken."),
            ("kader", "Vind je online een mooie foto <strong>zonder enige vermelding</strong>, ga er dan "
                      "van uit dat ze <strong>beschermd</strong> is en dat je <strong>toelating "
                      "nodig</strong> hebt. <strong>Geen vermelding betekent niet vrij</strong>: de "
                      "bescherming is er ook als niemand het erbij schrijft."),
            ("weetje", "Een <strong>kort citaat met bronvermelding</strong> mag, bijvoorbeeld in een werkje "
                       "of een bespreking. Een <strong>heel hoofdstuk</strong> overnemen is geen citaat."),
        ]),
        dict(kop="Creative commons", blokken=[
            ("p", "<strong>Creative commons</strong> is een <strong>licentie waarmee de maker vooraf "
                  "toelating geeft</strong>, onder voorwaarden. Je hoeft hem dus niets meer apart te "
                  "vragen, maar je moet je wel aan die voorwaarden houden."),
            ("p", tabel(["Voorwaarde", "Wat ze vraagt"], [
                ["naamsvermelding", "de naam van de maker erbij zetten waar je het werk gebruikt"],
                ["niet commercieel", "het werk niet gebruiken om er geld mee te verdienen"],
                ["niet bewerken", "het werk niet aanpassen of veranderen"],
            ])),
            ("kader", "Creative commons betekent <strong>niet</strong> dat je het werk "
                      "<strong>zonder voorwaarden</strong> mag gebruiken. De "
                      "<strong>naamsvermelding</strong> is de lichtste voorwaarde en meteen die "
                      "<strong>die het vaakst vergeten wordt</strong>. In de licenties staat ze als "
                      "<strong>BY</strong>."),
        ]),
        dict(kop="Portretrecht en privacy", blokken=[
            ("p", "Bij een foto van een persoon spelen <strong>twee rechten tegelijk</strong>:"),
            ("p", tabel(["Recht", "Van wie het is"], [
                ["auteursrecht", "van wie de foto maakte"],
                ["portretrecht", "van wie herkenbaar op de foto staat"],
            ])),
            ("p", "Neem je op een feest een foto van een vriendin en wil je die op je verhaal zetten, dan "
                  "heb je <strong>haar toelating</strong> nodig: jij hebt het auteursrecht, zij heeft het "
                  "portretrecht. Vragen is dus niet alleen vriendelijk, het hoort. Zet iemand "
                  "<strong>zonder te vragen</strong> een foto van jou online, dan mag je hem vragen die "
                  "<strong>weg te halen</strong>; lukt dat niet, dan kan je het <strong>bij het platform "
                  "zelf melden</strong>."),
            ("p", "Het <strong>privacyrecht</strong> beschermt je <strong>persoonsgegevens</strong> en "
                  "<strong>wat er met die gegevens mag gebeuren</strong>. Gegevens over jou zijn van jou, "
                  "en wie ze bijhoudt moet zeggen <strong>waarvoor</strong>."),
            ("kader", "Daaruit volgen twee regels. <strong>Niet meer gegevens vragen dan voor het doel "
                      "nodig is</strong>: voor een nieuwsbrief is een mailadres genoeg, een "
                      "rijksregisternummer hoort daar niet bij. En gegevens die een bedrijf over jou "
                      "bijhoudt, mag je <strong>opvragen, laten verbeteren</strong> en in veel gevallen "
                      "<strong>laten verwijderen</strong>."),
        ]),
        dict(kop="Wachtwoorden", blokken=[
            ("p", "Een <strong>sterk wachtwoord</strong> is <strong>lang</strong>, <strong>niet te "
                  "raden</strong> en je gebruikt het <strong>maar op één plaats</strong>. "
                  "<strong>Lengte helpt meer dan rare tekens.</strong>"),
            ("p", "Hergebruik is de grootste fout: <strong>raakt je wachtwoord op één site buiten, dan "
                  "liggen al je andere rekeningen open</strong>, want wie het heeft, probeert het gewoon "
                  "elders."),
            ("p", "<strong>Tweestapsverificatie</strong> (ook tweefactorauthenticatie) zet "
                  "<strong>naast je wachtwoord nog een code of een vinger</strong> als tweede slot. Ook "
                  "met je wachtwoord komt iemand er dan niet in."),
            ("kader", "Je <strong>wachtwoord deel je nooit</strong>, ook niet met iemand die zegt dat hij "
                      "van de helpdesk is. Een <strong>echte helpdesk heeft je wachtwoord niet "
                      "nodig</strong>."),
        ]),
        dict(kop="Phishing", blokken=[
            ("p", "<strong>Phishing</strong> is een <strong>nagemaakt bericht dat je gegevens of je geld "
                  "wil loskrijgen</strong>, naar het Engelse woord voor vissen. Het doet zich voor als je "
                  "bank, de post of een bekende dienst."),
            ("p", "Wat een phishingbericht vaak verraadt:"),
            ("p", tabel(["Teken", "Waar je op let"], [
                ["de afzender", "een adres dat net niet juist is"],
                ["haast", "je moet nu iets doen of je rekening gaat dicht"],
                ["de link", "hij gaat naar een adres dat je niet herkent"],
            ])),
            ("kader", "<strong>De taal zegt niets.</strong> Een nepbericht kan vlekkeloos Nederlands zijn "
                      "en het juiste logo dragen. Kijk naar de <strong>afzender en de link</strong>, niet "
                      "naar de opmaak."),
            ("p", "Krijg je een mail van je bank met de vraag om <strong>via een link</strong> je gegevens "
                  "te bevestigen, dan <strong>klik je niet</strong> en ga je <strong>zelf naar de site of "
                  "de app</strong> van je bank. Een bank vraagt je nooit om via een link je codes te "
                  "bevestigen."),
        ]),
        dict(kop="Nepnieuws", blokken=[
            ("p", "<strong>Nepnieuws</strong> zijn <strong>onjuiste berichten die met opzet als echt "
                  "nieuws verspreid worden</strong>. Een vergissing in een krant is geen nepnieuws: de "
                  "<strong>opzet</strong> maakt het verschil."),
            ("p", tabel(["Twijfel", "Wat je doet"], [
                ["een schokkend bericht zonder bron", "nakijken of ernstige media hetzelfde brengen"],
                ["een foto die verdacht lijkt", "de foto omgekeerd opzoeken en zien waar ze eerder opdook"],
            ])),
            ("p", "Oude foto's duiken vaak bij een nieuwe gebeurtenis op; omgekeerd zoeken laat dat meteen "
                  "zien."),
            ("kader", "<strong>Deel nooit iets dat je niet nagekeken hebt.</strong> En let op: "
                      "<strong>hoeveel keer iets gedeeld is, zegt niets over de waarheid</strong>."),
        ]),
        dict(kop="Cyberpesten en netiquette", blokken=[
            ("p", "Wordt iemand in een groepsgesprek <strong>dag na dag belachelijk gemaakt</strong>, dan "
                  "is de beste reactie: <strong>bewijs bewaren, melden, en de persoon zelf niet alleen "
                  "laten</strong>. Een <strong>schermafbeelding</strong> is je bewijs, want berichten "
                  "worden vaak gewist."),
            ("kader", "<strong>Niet meedoen is nodig, maar niet genoeg.</strong> Wie gepest wordt, heeft "
                      "iemand nodig die er <strong>iets van zegt</strong>."),
            ("p", "Een <strong>foto doorsturen</strong> die duidelijk niet bedoeld was om gedeeld te "
                  "worden, mag niet — <strong>ook al heb je ze zelf gekregen</strong>. Een foto krijgen is "
                  "geen toelating om ze verder te sturen; daar gaan het portretrecht en de privacy over."),
            ("p", "<strong>Netiquette</strong> zijn de <strong>omgangsregels voor hoe je je online "
                  "gedraagt</strong>, uit net en etiquette. Een bericht <strong>volledig in "
                  "hoofdletters</strong> hoort daar niet bij: hoofdletters lezen online als "
                  "<strong>roepen</strong>."),
        ]),
    ],
    onthoud=[
        "Het auteursrecht ontstaat automatisch bij het maken en loopt tot zeventig jaar na het overlijden.",
        "Geen vermelding bij een foto betekent niet dat ze vrij is.",
        "Creative commons: de maker geeft vooraf toelating, met voorwaarden als naamsvermelding, niet commercieel of niet bewerken.",
        "Het auteursrecht is van de fotograaf, het portretrecht van wie erop staat.",
        "Het privacyrecht beschermt je persoonsgegevens; er mag niet meer gevraagd worden dan nodig.",
        "Een sterk wachtwoord is lang, niet te raden en maar op één plaats in gebruik.",
        "Tweestapsverificatie zet een tweede slot naast je wachtwoord.",
        "Phishing verraadt zich door de afzender, de haast en de link, nooit door de taal.",
        "Nepnieuws is onjuist én met opzet verspreid. Kijk na voor je deelt.",
        "Bij cyberpesten: schermafbeelding, melden, en de persoon niet alleen laten. Hoofdletters zijn roepen.",
    ],
)

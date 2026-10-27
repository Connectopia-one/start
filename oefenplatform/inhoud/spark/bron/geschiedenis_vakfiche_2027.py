# -*- coding: utf-8 -*-
"""Nieuwe vragen bij de leerstof die op 27 oktober 2026 in de Spark-bundels kwam.

Kim legde de vakfiche geschiedenis 1A (2027) naast de leerbundels. Wat ontbrak
(de Egyptische goden, Kreta en Mycene, de Atheense democratie, de Romeinse
magistraten, de kenmerken per domein...) staat nu in de bundel, en hier staan
de vragen erbij: drie per thema in deel 1, drie in deel 2.

    python3 inhoud/spark/bron/geschiedenis_vakfiche_2027.py

Dat schrijft twee dingen:
- inhoud/herstel/geschiedenis-spark-nieuw-2027.json, met enkel deze vragen.
  Importeren met "Bestaande vragen vervangen" UIT: ze komen erbij, en de
  vragen in de examenvormen in diezelfde hoofdstukken blijven staan.
- dezelfde vragen achteraan in inhoud/spark/geschiedenis.json, zodat wie later
  het hele vak opnieuw inlaadt ze ook krijgt. Twee keer draaien zet ze er niet
  twee keer in.
"""
import json, pathlib

HIER = pathlib.Path(__file__).resolve().parent
INHOUD = HIER.parent.parent

def mk(vraag, opties, antwoord, uitleg):
    return {"type": "meerkeuze", "vraag": vraag, "opties": opties, "antwoord": antwoord, "uitleg": uitleg}

def wn(vraag, antwoord, uitleg):
    return {"type": "waarofniet", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}

def inv(vraag, antwoord, uitleg):
    return {"type": "invultekst", "vraag": vraag, "antwoord": antwoord, "uitleg": uitleg}

NIEUW = {
"Het historisch referentiekader — deel 1": [
    mk("Hoe heet de periode die op de middeleeuwen volgt?",
       ["de vroegmoderne tijd", "de moderne tijd", "de nieuwste tijd", "de hedendaagse of eigen tijd"], 0,
       "Na de middeleeuwen komt de vroegmoderne tijd, van ongeveer 1500 tot 1789. In oudere boeken heet die nog de nieuwe tijd."),
    wn("Na het jaar 1 v.C. komt meteen het jaar 1 n.C.", True,
       "Klopt. Een jaar 0 bestaat niet in onze tijdrekening."),
    mk("Een samenleving waarin de man het hoofd van het gezin is en beslist, noem je...",
       ["een patriarchale samenleving", "een aristocratie", "een standenmaatschappij met vaste lagen", "een monotheïsme"], 0,
       "Patriarchaal komt van pater, vader. In Rome had de pater familias het gezag over zijn hele gezin."),
],
"Het historisch referentiekader — deel 2": [
    mk("Welke van deze begrippen horen bij het economische domein?",
       ["ruileconomie", "geldeconomie", "autocratie", "polytheïsme"], [0, 1],
       "Ruilen en betalen met munten gaan over hoe mensen aan goederen komen: economisch. Autocratie is politiek, polytheïsme cultureel."),
    mk("De farao en de Romeinse keizer hadden allebei alle macht in handen. Welk begrip past daarbij?",
       ["autocratie", "aristocratie", "democratie", "republiek"], 0,
       "Bij een autocratie heeft één persoon alle macht. Bij een aristocratie is dat de adel."),
    wn("Monotheïsme is het geloof in veel goden.", False,
       "Nee, dat is polytheïsme. Monotheïsme is het geloof in één god, zoals bij het christendom."),
],
"De prehistorie — deel 1": [
    mk("Welke mensachtige maakte de eerste eenvoudige stenen werktuigen?",
       ["Homo habilis", "Homo sapiens", "de neanderthaler", "Australopithecus"], 0,
       "Habilis betekent handig. De Homo habilis leefde zo'n 2,4 tot 1,4 miljoen jaar geleden."),
    wn("De laatste ijstijd eindigde ongeveer 12 000 jaar geleden, en daarna werd het warmer.", True,
       "Klopt. In het warmere klimaat groeiden wilde granen in overvloed, en dat hielp de landbouw op gang."),
    inv("Hoe heet één grote, rechtopstaande steen uit de prehistorie? (één woord)", "menhir",
       "Een menhir staat alleen rechtop. Bij een dolmen of hunebed liggen grote stenen boven een graf. In Wéris staan ze allebei."),
],
"De prehistorie — deel 2": [
    mk("Waarom begonnen mensen na de laatste ijstijd zelf te zaaien?",
       ["Het werd warmer, wilde granen groeiden en hun aantal nam toe", "Ze hadden de ploeg uitgevonden en wilden die eindelijk eens gebruiken",
        "De jacht was verboden geraakt", "Ze wilden munten verdienen"], 0,
       "Een warmer klimaat, veel wilde granen en een groeiende groep: jagen en verzamelen alleen werd te weinig."),
    mk("Waar in België vind je prehistorische vuursteenmijnen die werelderfgoed zijn?",
       ["Spiennes", "Tongeren", "Wéris in de Ardennen", "Lascaux"], 0,
       "In Spiennes bij Bergen groeven de eerste boeren schachten om vuursteen voor hun bijlen te halen. Lascaux ligt in Frankrijk."),
    wn("De landbouw kwam in onze streken tegelijk aan als in het Midden-Oosten.", False,
       "Nee. De eerste boeren kwamen hier pas rond 5300 v.C., zo'n vijfduizend jaar later. De landbouw verspreidde zich heel traag."),
],
"Mesopotamië en Egypte — deel 1": [
    mk("Welke Egyptische god heeft een jakhalskop en zorgt voor het balsemen?",
       ["Anoebis", "Horus", "Toth", "de zonnegod Re"], 0,
       "Anoebis heeft een jakhalskop. Horus heeft een valkenkop, Toth een ibiskop, en Re een valkenkop met de zonneschijf."),
    mk("Wie was in Egypte de hoogste ambtenaar, de rechterhand van de farao?",
       ["de vizier", "de priester", "de schrijver", "de gouwvorst"], 0,
       "De vizier bestuurde het land in naam van de farao. De gouwvorsten bestuurden elk een deel, de schrijvers hielden de boeken bij."),
    wn("Howard Carter vond in 1922 het graf van Toetanchamon.", True,
       "Klopt. Het lag in de Vallei der Koningen en was als enige bijna ongeschonden."),
],
"Mesopotamië en Egypte — deel 2": [
    mk("Wat gebeurde er volgens de Egyptenaren bij de hartweging?",
       ["Het hart werd gewogen tegen een veer", "De farao woog het goud van het graf",
        "De priesters wogen de oogst voor de goden", "De mummie werd gewogen voor het balsemen"], 0,
       "Anoebis legde het hart op een weegschaal tegen een veer, en Toth schreef de uitslag op. Een licht hart mocht naar het rijk van Osiris."),
    mk("Waarom spreken we bij de Egyptische godsdienst van een natuurgodsdienst?",
       ["Veel goden staan voor krachten van de natuur", "Ze baden enkel buiten, in de vrije natuur, en nooit in een tempel",
        "Ze kenden maar één god", "De farao was geen god"], 0,
       "De zon (Re), het water van de Nijl (Sobek), de woestijn en de storm (Seth): de natuur bepaalde hun leven, en hun goden."),
    mk("Welke voorwerpen hield de farao vast als teken van zijn macht?",
       ["een kromstaf en een dorsvlegel", "een lauwerkrans en een toga", "een zwaard en een schild", "een kleitablet en een rietstengel"], 0,
       "Samen met de dubbele kroon, de valse baard en de cobra op zijn voorhoofd. De lauwerkrans hoort bij de Romeinse keizer."),
],
"Het oude Griekenland — deel 1": [
    mk("Op welk eiland bloeide de Minoïsche beschaving?",
       ["Kreta", "Sicilië", "Cyprus", "Rhodos"], 0,
       "Op Kreta, ongeveer van 2000 tot 1450 v.C., met het paleis van Knossos. De naam komt van de sagenkoning Minos."),
    mk("Hoe heetten de vreemdelingen in Athene die vrij waren, belasting betaalden, maar niet mochten stemmen?",
       ["metoiken", "heloten", "perioiken", "Spartiaten"], 0,
       "Metoiken woonden in Athene. Perioiken en heloten hoorden bij Sparta."),
    wn("In de Atheense democratie werden veel bestuurders door loting gekozen.", True,
       "Klopt. De leden van de Raad van 500 en de rechters werden geloot uit de burgers."),
],
"Het oude Griekenland — deel 2": [
    mk("Wat is een paleiseconomie?",
       ["Het paleis verzamelt de oogst, bewaart ze en verdeelt ze", "Iedereen ruilt vrij op de markt",
        "Het paleis betaalt de boeren elke maand met zilveren munten voor hun werk", "Elke familie houdt haar oogst zelf"], 0,
       "Zo werkte het bij de Minoërs op Kreta en bij de Myceners: alles liep langs het paleis, met schrijvers die het bijhielden."),
    mk("Wat kon de Atheense volksvergadering met het schervengericht doen?",
       ["een te machtige politicus tien jaar verbannen", "een nieuwe koning kiezen", "een oorlog verklaren aan Sparta zonder dat de Raad van 500 meestemt", "de goden een offer brengen"], 0,
       "Elke burger kraste een naam op een potscherf. Wie de meeste stemmen kreeg, moest de stad tien jaar verlaten."),
    wn("De Peloponnesische oorlog tussen Athene en Sparta duurde minder dan tien jaar.", False,
       "Nee. Ze duurde van 431 tot 404 v.C., dus 27 jaar."),
],
"Het Romeinse Rijk — deel 1": [
    mk("Welke Romeinse magistraat beheerde de staatskas?",
       ["de quaestor", "de praetor", "de censor", "de volkstribuun"], 0,
       "De quaestor beheerde het geld. De praetor sprak recht, de censor hield de volkstelling bij, de volkstribuun beschermde de plebejers."),
    mk("Welke Carthaagse generaal trok met olifanten over de Alpen?",
       ["Hannibal", "Odoaker", "Spartacus", "Pompeius"], 0,
       "Dat was in de tweede Punische oorlog. Hij versloeg de Romeinen in Italië zelf, maar Rome hield stand."),
    inv("Hoe heet de oudste stad van België, uit de Romeinse tijd? (één woord)", "Tongeren",
       "Tongeren lag aan de heirbaan van Boulogne naar Keulen. Je ziet er nog resten van de Romeinse stadsmuur."),
],
"Het Romeinse Rijk — deel 2": [
    mk("Wat deden Romeinse priesters om de wil van de goden te kennen?",
       ["Ze keken naar voortekens, zoals de vlucht van vogels", "Ze lazen het Dodenboek",
        "Ze vroegen het aan het orakel van Delphi", "Ze telden de sterren in een ziggurat"], 0,
       "Voortekens lezen namen de Romeinen over van de Etrusken. Het Dodenboek hoort bij Egypte, de ziggurat bij Mesopotamië."),
    wn("In 380 werd het christendom de staatsgodsdienst van het Romeinse Rijk.", True,
       "Klopt, onder keizer Theodosius. Constantijn had het in 313 al toegelaten."),
    mk("Wat had de pater familias in een Romeins gezin?",
       ["het gezag over zijn vrouw, zijn kinderen en zijn slaven", "enkel het recht om te stemmen",
        "de taak om het huishouden te doen", "geen enkele macht over zijn kinderen"], 0,
       "Rome was een patriarchale samenleving: de vader besliste, tot zelfs of een pasgeboren kind mocht blijven leven."),
],
"Bronnen, kunst en beeldvorming — deel 1": [
    mk("Uit hoeveel stappen bestaat het stappenplan om een kunstwerk te analyseren?",
       ["vier", "drie", "twee", "vijf"], 0,
       "Info verzamelen, beschrijven wat je ziet of hoort, interpreteren, en je analyse toelichten."),
    wn("Informatie die je zelf uit een bron moet afleiden, heet onrechtstreekse informatie.", True,
       "Klopt. Rechtstreekse informatie staat er letterlijk in."),
    mk("Een mozaïek op de vloer van een Romeinse villa is vooral gemaakt om te...",
       ["decoreren", "bekritiseren", "informeren", "entertainen"], 0,
       "Het versiert de ruimte. Een spotprent bekritiseert, een komedie entertaint."),
],
"Bronnen, kunst en beeldvorming — deel 2": [
    mk("Suetonius schreef meer dan honderd jaar na de dood van Julius Caesar over hem. Wat betekent dat voor zijn verslag?",
       ["Hij was geen ooggetuige en moest steunen op andere bronnen", "Zijn verslag is daarom volledig betrouwbaar",
        "Hij was een ooggetuige van de moord", "Zijn tekst is daardoor geen historische bron"], 0,
       "Hij leefde niet in Caesars tijd. Zijn boek blijft een bron, maar je vergelijkt het best met andere bronnen."),
    mk("In welke stap van de bronnenanalyse beoordeel je de bruikbaarheid en de betrouwbaarheid van een bron?",
       ["stap 3: de bron interpreteren", "stap 1: de context verzamelen", "stap 2: de inhoud bestuderen", "stap 4: een antwoord geven"], 0,
       "In stap 3 interpreteer je: je kijkt hoe de context de inhoud kleurt, je beoordeelt bruikbaarheid en betrouwbaarheid en je vergelijkt de bronnen."),
    wn("Een bron die maar een deel van je historische vraag beantwoordt, is niet bruikbaar.", False,
       "Nee. Een bron kan een volledig, een gedeeltelijk of geen antwoord geven. Een gedeeltelijk antwoord is ook bruikbaar."),
],
}

def main():
    bron = INHOUD / "spark" / "geschiedenis.json"
    d = json.loads(bron.read_text(encoding="utf-8"))
    per_titel = {h["titel"]: h for h in d["hoofdstukken"]}
    herstel = {"hoofdstukken": []}
    for titel, vragen in NIEUW.items():
        h = per_titel[titel]
        bekend = {v["vraag"] for v in h["vragen"]}
        h["vragen"] += [v for v in vragen if v["vraag"] not in bekend]
        herstel["hoofdstukken"].append({"titel": titel, "niveau": "spark", "gratis": False, "vragen": vragen})
    bron.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    doel = INHOUD / "herstel" / "geschiedenis-spark-nieuw-2027.json"
    doel.write_text(json.dumps(herstel, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(sum(len(v) for v in NIEUW.values()), "vragen")

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Prosociaal gedrag, antisociaal gedrag en sociale cognitie.

Het eerste van drie thema's over sociale psychologie. Sociale psychologie
onderzoekt hoe mensen door anderen beïnvloed worden, en begint bij twee
lijstjes en bij de vraag hoe wij verklaringen verzinnen voor wat mensen doen.

De lijstjes staan letterlijk in de fiche:

    prosociaal gedrag: delen, helpen en ondersteunen, positief groepsgedrag,
        samenwerken, troosten, verantwoordelijkheid opnemen
    antisociaal gedrag: agressie, liegen en bedriegen, ongepast groepsgedrag,
        pesten, regels overtreden, vandalisme
    sociale cognitie bestaat uit drie mentale processen: attitude, attributie
        en cognitieve dissonantie
    attributietheorie: Fritz Heider - interne of dispositionele attributie,
        externe of situationele attributie, de fundamentele attributiefout
    attributietheorie van motivatie en emoties: Bernard Weiner - locus van
        controle, stabiliteit, controleerbaarheid
    theorie van impliciete overtuigingen: Carol Dweck - fixed mindset,
        growth mindset

De cognitieve dissonantie van Festinger is het derde mentale proces van de
sociale cognitie, maar krijgt bij ons een eigen thema samen met de
groepsprocessen, omdat er veel in zit.

Deel 1 is prosociaal en antisociaal gedrag, en wat sociale cognitie en een
attitude zijn.
Deel 2 zijn de drie attributietheorieën.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat onderzoekt de sociale psychologie?",
        opties=[
            "hoe mensen door anderen beïnvloed worden",
            "hoe het geheugen informatie opslaat",
            "hoe genen het gedrag van iemand vastleggen",
            "hoe een mens zich in fasen ontwikkelt",
        ],
        antwoord=0,
        uitleg="Sociale psychologie gaat over gedrag in gezelschap van anderen: de invloed van een groep, van een gezagsfiguur en van wat anderen denken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is prosociaal gedrag?",
        opties=[
            "gedrag waarmee je anderen helpt of goed doet",
            "gedrag dat je alleen doet wanneer niemand kijkt",
            "gedrag dat door een groep wordt afgekeurd",
            "gedrag dat je zonder nadenken stelt",
        ],
        antwoord=0,
        uitleg="Pro betekent voor. Prosociaal gedrag is gericht op het welzijn van iemand anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze gedragingen noemt de fiche prosociaal?",
        opties=[
            "delen",
            "troosten",
            "verantwoordelijkheid opnemen",
            "regels overtreden",
            "vandalisme",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt zes vormen van prosociaal gedrag: delen, helpen en ondersteunen, positief groepsgedrag, samenwerken, troosten en verantwoordelijkheid opnemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze gedragingen noemt de fiche antisociaal?",
        opties=[
            "pesten",
            "vandalisme",
            "liegen en bedriegen",
            "samenwerken",
            "troosten",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche noemt zes vormen van antisociaal gedrag: agressie, liegen en bedriegen, ongepast groepsgedrag, pesten, regels overtreden en vandalisme.",
    ),
    dict(
        type="meerkeuze",
        vraag="Milan blijft na de les bij een klasgenoot die aan het huilen is en praat met haar. Welk gedrag is dit?",
        opties=[
            "troosten, een vorm van prosociaal gedrag",
            "samenwerken, een vorm van prosociaal gedrag",
            "positief groepsgedrag in de volledige klasgroep",
            "verantwoordelijkheid opnemen voor een opdracht",
        ],
        antwoord=0,
        uitleg="Bij iemand blijven die verdriet heeft, is troosten. De fiche noemt dat als een aparte vorm van prosociaal gedrag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een groep leerlingen maakt met opzet de bankjes van de bushalte stuk. Welk gedrag is dit?",
        opties=[
            "vandalisme, een vorm van antisociaal gedrag",
            "agressie, een vorm van antisociaal gedrag",
            "regels overtreden zonder iets te beschadigen",
            "ongepast groepsgedrag zonder enige schade",
        ],
        antwoord=0,
        uitleg="Opzettelijk iets stukmaken is vandalisme. Agressie is gericht op een persoon, vandalisme op spullen.",
    ),
    dict(
        type="invultekst",
        vraag="Gedrag waarmee je anderen schade toebrengt of waarmee je tegen de regels van samenleven ingaat, heet ... gedrag.",
        antwoord=["antisociaal", "antisociale"],
        uitleg="Antisociaal gedrag. Anti betekent tegen, pro betekent voor.",
    ),
    dict(
        type="waarofniet",
        vraag="Iets voor iemand doen in de hoop er zelf iets aan over te houden, blijft prosociaal gedrag.",
        antwoord=True,
        uitleg="Waar. De fiche kijkt naar het gedrag zelf, niet naar de reden erachter. Helpen blijft helpen, ook met een eigen bedoeling erbij.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle gedrag in een groep is volgens de fiche prosociaal, want je doet het samen.",
        antwoord=False,
        uitleg="Niet waar. De fiche noemt zowel positief groepsgedrag als ongepast groepsgedrag. Samen iets doen zegt niets over goed of slecht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is sociale cognitie?",
        opties=[
            "de manier waarop wij over mensen nadenken",
            "de manier waarop wij samen een taak uitvoeren",
            "de manier waarop een groep beslissingen neemt",
            "de manier waarop een kind leren overneemt",
        ],
        antwoord=0,
        uitleg="Cognitie is denken. Sociale cognitie is hoe wij informatie over andere mensen en over onszelf verwerken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie mentale processen horen volgens de fiche bij sociale cognitie?",
        opties=[
            "attitude",
            "attributie",
            "cognitieve dissonantie",
            "conformisme",
        ],
        antwoord=[0, 1, 2],
        uitleg="Attitude, attributie en cognitieve dissonantie. Conformisme hoort bij sociale beïnvloeding, niet bij sociale cognitie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een attitude?",
        opties=[
            "een vaste houding tegenover iets of iemand",
            "een verklaring die je voor gedrag verzint",
            "de spanning tussen twee gedachten",
            "de druk die een groep op je zet",
        ],
        antwoord=0,
        uitleg="Een attitude is een houding: hoe je over iets denkt en voelt, en hoe geneigd je bent ernaar te handelen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband tussen een attitude en gedrag?",
        opties=[
            "een attitude maakt bepaald gedrag waarschijnlijker",
            "een attitude leidt altijd tot het bijbehorende gedrag",
            "een attitude heeft met gedrag niets te maken",
            "een attitude ontstaat pas na het gedrag zelf",
        ],
        antwoord=0,
        uitleg="Een attitude duwt in een richting, maar beslist niet. Wie milieubewust denkt, neemt niet altijd de trein.",
    ),
    dict(
        type="invultekst",
        vraag="De houding die iemand tegenover iets of iemand heeft, en die zijn gedrag mee stuurt, heet een ...",
        antwoord=["attitude"],
        uitleg="Een attitude. Ze bestaat uit wat je denkt, wat je voelt en wat je neigt te doen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een attitude ligt voor altijd vast en kan niet veranderen.",
        antwoord=False,
        uitleg="Niet waar. Een attitude kan veranderen, onder andere om een cognitieve dissonantie weg te werken.",
    ),
    dict(
        type="waarofniet",
        vraag="De fiche noemt zes vormen van prosociaal gedrag en zes vormen van antisociaal gedrag.",
        antwoord=True,
        uitleg="Waar. Zes en zes, en ze staan allebei in de fiche met hun namen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Nora vertelt haar ouders dat ze bij een vriendin was, terwijl ze op een feest zat. Welk gedrag is dit volgens de fiche?",
        opties=[
            "liegen en bedriegen",
            "regels overtreden",
            "ongepast groepsgedrag",
            "agressie",
        ],
        antwoord=0,
        uitleg="Iets anders zeggen dan de waarheid is liegen. De fiche noemt liegen en bedriegen als één vorm van antisociaal gedrag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Drie leerlingen maken samen een werkstuk en verdelen de taken eerlijk. Welk gedrag is dit?",
        opties=[
            "samenwerken",
            "delen",
            "helpen en ondersteunen",
            "verantwoordelijkheid opnemen",
        ],
        antwoord=0,
        uitleg="Samen aan één doel werken is samenwerken. Delen gaat over spullen, helpen over iemand bijstaan.",
    ),
    dict(
        type="invultekst",
        vraag="Gedrag dat gericht is op het goed doen van iemand anders, heet ... gedrag.",
        antwoord=["prosociaal", "prosociale"],
        uitleg="Prosociaal gedrag. Delen, helpen, troosten en samenwerken horen erbij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vraagt de fiche om gedrag te beoordelen als prosociaal of antisociaal, en niet als goed of slecht?",
        opties=[
            "omdat de twee begrippen naar het effect op anderen kijken",
            "omdat goed en slecht in de psychologie niet bestaan",
            "omdat alleen groepsgedrag beoordeeld mag worden",
            "omdat een attitude nooit goed of slecht kan zijn",
        ],
        antwoord=0,
        uitleg="Prosociaal en antisociaal zijn vakbegrippen: ze zeggen of gedrag anderen goed doet of schaadt, zonder een moreel oordeel over de persoon.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een causale attributie?",
        opties=[
            "de oorzaak die je aan gedrag toeschrijft",
            "de houding die je tegenover iemand hebt",
            "de druk die een groep op iemand zet",
            "de spanning tussen twee gedachten",
        ],
        antwoord=0,
        uitleg="Attribueren is toeschrijven. Een causale attributie is de oorzaak die jij bedenkt voor wat iemand doet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de attributietheorie met de interne en de externe attributie?",
        opties=[
            "Fritz Heider",
            "Bernard Weiner",
            "Carol Dweck",
            "Leon Festinger",
        ],
        antwoord=0,
        uitleg="Heider. Hij onderscheidt de interne of dispositionele en de externe of situationele attributie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een interne of dispositionele attributie?",
        opties=[
            "de oorzaak bij de persoon zelf leggen",
            "de oorzaak bij de omstandigheden leggen",
            "de oorzaak bij het toeval leggen",
            "de oorzaak bij de groep leggen",
        ],
        antwoord=0,
        uitleg="Intern betekent in de persoon: zijn karakter, zijn inzet, zijn kunnen. Dispositie is het andere woord voor die eigen kant.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een externe of situationele attributie?",
        opties=[
            "de oorzaak bij de omstandigheden leggen",
            "de oorzaak bij het karakter leggen",
            "de oorzaak bij de inzet leggen",
            "de oorzaak bij het talent leggen",
        ],
        antwoord=0,
        uitleg="Extern betekent buiten de persoon: de situatie, de drukte, het weer, de opdracht die te moeilijk was.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand rijdt je voorbij en snijdt je af. Je denkt meteen: wat een onbeschofte chauffeur. Welke attributie maak je?",
        opties=[
            "een interne attributie",
            "een externe attributie",
            "een stabiele attributie",
            "een controleerbare attributie",
        ],
        antwoord=0,
        uitleg="Je legt de oorzaak in de persoon, in zijn karakter. Dat is intern of dispositioneel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de fundamentele attributiefout?",
        opties=[
            "bij anderen de persoon de schuld geven en bij jezelf de situatie",
            "bij anderen de situatie de schuld geven en bij jezelf de persoon",
            "bij iedereen altijd de situatie de schuld geven",
            "bij iedereen altijd de persoon de schuld geven",
        ],
        antwoord=0,
        uitleg="Wij schatten bij anderen het karakter te zwaar in en bij onszelf de omstandigheden. Dat is de fundamentele attributiefout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je bent zelf te laat en zegt: er was file. Een klasgenoot is te laat en je denkt: die is ongeorganiseerd. Welk verschijnsel is dit?",
        opties=[
            "de fundamentele attributiefout",
            "cognitieve dissonantie",
            "een fixed mindset",
            "een normatief conformisme",
        ],
        antwoord=0,
        uitleg="Bij jezelf extern, bij de ander intern: dat is precies de fundamentele attributiefout.",
    ),
    dict(
        type="invultekst",
        vraag="Het andere woord voor een interne attributie, dat naar de eigenschappen van de persoon verwijst, is een ... attributie.",
        antwoord=["dispositionele", "dispositioneel"],
        uitleg="Een dispositionele attributie. De externe heet ook een situationele attributie.",
    ),
    dict(
        type="waarofniet",
        vraag="Een attributie is niet altijd juist: het is de verklaring die jij maakt, niet noodzakelijk de echte oorzaak.",
        antwoord=True,
        uitleg="Waar. Daarom spreekt de fiche van een fout: de fundamentele attributiefout.",
    ),
    dict(
        type="waarofniet",
        vraag="Heider onderscheidt drie soorten attributie: de interne, de externe en de stabiele.",
        antwoord=False,
        uitleg="Niet waar. Bij Heider staan er twee, de interne en de externe. Stabiliteit is een begrip van Weiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de attributietheorie van motivatie en emoties?",
        opties=[
            "Bernard Weiner",
            "Fritz Heider",
            "Carol Dweck",
            "Solomon Asch",
        ],
        antwoord=0,
        uitleg="Weiner. Hij zet drie assen naast elkaar: de locus van controle, de stabiliteit en de controleerbaarheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie dimensies gebruikt Weiner om een attributie te beschrijven?",
        opties=[
            "de locus van controle",
            "de stabiliteit",
            "de controleerbaarheid",
            "de attitude",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie. De attitude hoort bij de sociale cognitie in het algemeen, niet bij Weiner.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling zegt: ik ben nu eens niet goed in wiskunde, dat verandert toch nooit. Welke dimensie van Weiner hoor je vooral?",
        opties=[
            "de stabiliteit, want hij houdt de oorzaak voor onveranderlijk",
            "de locus van controle, want hij legt het buiten zichzelf",
            "de controleerbaarheid, want hij kan er zelf iets aan doen",
            "de attitude, want hij heeft een mening over wiskunde",
        ],
        antwoord=0,
        uitleg="Dat verandert toch nooit gaat over stabiliteit. Een stabiele oorzaak blijft, een onstabiele kan morgen anders zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt de dimensie controleerbaarheid bij Weiner?",
        opties=[
            "of iemand zelf iets aan de oorzaak kan doen",
            "of de oorzaak bij de persoon of de situatie zit",
            "of de oorzaak blijft of verandert",
            "of de oorzaak door anderen gezien wordt",
        ],
        antwoord=0,
        uitleg="Controleerbaar betekent: ik heb het in de hand. Niet geleerd hebben is controleerbaar, een griep is dat niet.",
    ),
    dict(
        type="invultekst",
        vraag="De dimensie van Weiner die zegt of de oorzaak binnen of buiten de persoon ligt, is de ... van controle.",
        antwoord=["locus"],
        uitleg="De locus van controle. Locus is het Latijnse woord voor plaats.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wie hoort in de fiche bij de theorie van de impliciete overtuigingen, met de fixed en de growth mindset?",
        opties=[
            "Carol Dweck",
            "Bernard Weiner",
            "Fritz Heider",
            "Leon Festinger",
        ],
        antwoord=0,
        uitleg="Dweck. Haar twee begrippen zijn de fixed mindset en de growth mindset.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een fixed mindset volgens Dweck?",
        opties=[
            "geloven dat je kunnen vastligt en niet groeit",
            "geloven dat je kunnen groeit door te oefenen",
            "geloven dat anderen je kunnen bepalen",
            "geloven dat fouten maken nooit erg is",
        ],
        antwoord=0,
        uitleg="Fixed betekent vast. Wie zo denkt, ziet een fout als bewijs dat hij het niet kan, en durft minder proberen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling zegt na een slechte toets: dit kan ik nog niet, ik ga het anders aanpakken. Welke mindset hoor je?",
        opties=[
            "een growth mindset",
            "een fixed mindset",
            "een stabiele attributie",
            "een externe attributie",
        ],
        antwoord=0,
        uitleg="Nog niet en het anders aanpakken wijzen op een growth mindset: kunnen groeit door inzet en oefening.",
    ),
    dict(
        type="waarofniet",
        vraag="Een fixed mindset past bij een attributie die stabiel en oncontroleerbaar is.",
        antwoord=True,
        uitleg="Waar. Wie denkt dat zijn kunnen vastligt, ziet de oorzaak als blijvend en als iets waar hij zelf niets aan kan doen.",
    ),
    dict(
        type="waarofniet",
        vraag="Volgens Dweck heeft iedereen altijd in alle vakken dezelfde mindset.",
        antwoord=False,
        uitleg="Niet waar. Iemand kan over taal een growth mindset hebben en over wiskunde een fixed mindset.",
    ),
]

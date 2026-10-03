# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Veilig werken, meten en levensreddend handelen.

De koppen "Veilig en duurzaam werken" en "Meetinstrumenten en hulpmiddelen"
uit het onderdeel wetenschappelijk onderzoek en STEM, en de kop
"Levensreddend handelen" uit de biologie van de vakfiche natuurwetenschappen
2de graad doorstroom. Deel 1 gaat over veilig werken in het labo, de
pictogrammen en de meetinstrumenten; deel 2 over eerste hulp bij een
hartstilstand, een verdrinking en een verslikking.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent een pictogram met een vlam op een oranje of rode achtergrond?",
        opties=[
            "de stof is ontvlambaar",
            "de stof is giftig bij inslikken",
            "de stof is bijtend voor je huid",
            "de stof is gevaarlijk voor het water",
        ],
        antwoord=0,
        uitleg="Zo'n stof vat gemakkelijk vuur. Je houdt ze dus weg van een bunsenbrander of een vlam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor staan de H-zinnen op een flesje met een chemische stof?",
        opties=[
            "ze beschrijven het gevaar van de stof",
            "ze beschrijven hoe je de stof veilig gebruikt",
            "ze geven de houdbaarheidsdatum van de stof",
            "ze geven de molaire massa van de stof",
        ],
        antwoord=0,
        uitleg="De H staat voor hazard, dus gevaar. De P-zinnen zeggen daarna wat je moet doen om dat gevaar te vermijden.",
    ),
    dict(
        type="waarofniet",
        vraag="De P-zinnen op een etiket zeggen welke voorzorgen je bij die stof moet nemen.",
        antwoord=True,
        uitleg="P staat voor precaution. Daar lees je bijvoorbeeld dat je handschoenen en een bril moet dragen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke werkwijzen horen bij veilig en duurzaam werken in een labo? Kruis alles aan wat juist is.",
        opties=[
            "gemorste producten onmiddellijk opkuisen",
            "zuinig omgaan met chemische stoffen",
            "meetinstrumenten uitschakelen als je niet meet",
            "elektrische toestellen met natte handen bedienen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Die drie horen bij zorgvuldig werken. Natte handen aan een elektrisch toestel is juist een van de gevaarlijkste fouten.",
    ),
    dict(
        type="invultekst",
        vraag="Met welk instrument meet je de massa van een stof in het labo?",
        antwoord="balans",
        uitleg="Je kiest een balans met genoeg nauwkeurigheid voor je meting. Voor kleine hoeveelheden gebruik je een analytische balans.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het meetbereik van een meetinstrument?",
        opties=[
            "de kleinste en de grootste waarde die het kan meten",
            "de nauwkeurigheid waarmee het de waarde weergeeft",
            "de tijd die het nodig heeft voor één meting",
            "het aantal metingen dat het achter elkaar kan doen",
        ],
        antwoord=0,
        uitleg="Meet je buiten dat bereik, dan is het resultaat onbruikbaar of gaat het toestel stuk. Daarom kies je een instrument dat bij je meting past.",
    ),
    dict(
        type="waarofniet",
        vraag="Een meting is nooit helemaal exact, want elk meetinstrument heeft een beperkte nauwkeurigheid.",
        antwoord=True,
        uitleg="Daarom schrijf je een resultaat in het juiste aantal beduidende cijfers. Meer cijfers opschrijven suggereert een nauwkeurigheid die er niet is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet 25 milliliter vloeistof heel nauwkeurig afmeten. Wat gebruik je?",
        opties=[
            "een pipet, want die is voor dat volume veel nauwkeuriger",
            "een maatbeker, want die staat stabieler op de tafel",
            "een erlenmeyer, want daarin kan je ook goed mengen",
            "een proefbuis, want die is net groot genoeg daarvoor",
        ],
        antwoord=0,
        uitleg="Een maatbeker is bedoeld om te mengen, niet om nauwkeurig af te meten. Voor een precieze hoeveelheid neem je een pipet of een maatkolf.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je met glasscherven in het labo?",
        opties=[
            "je ruimt ze op in de daarvoor bestemde bak voor scherp afval",
            "je gooit ze bij het gewone afval zodra ze afgekoeld zijn",
            "je laat ze liggen tot de les gedaan is en meldt het dan",
            "je veegt ze met je hand bij elkaar en legt ze op de tafel",
        ],
        antwoord=0,
        uitleg="Scherp glas hoort nooit bij het gewone afval, want wie het nadien aanraakt kan zich snijden. Je gebruikt er een borstel en een blad voor, niet je handen.",
    ),
    dict(
        type="invultekst",
        vraag="Met welk instrument meet je de zuurtegraad van een oplossing nauwkeurig?",
        antwoord="pH-meter",
        uitleg="Een indicator geeft alleen een kleur en dus een ruwe aanwijzing. Een pH-meter geeft de waarde als getal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent de wetenschappelijke notatie van een getal?",
        opties=[
            "je schrijft het als een getal tussen 1 en 10 maal een macht van tien",
            "je schrijft het altijd met precies drie cijfers na de komma",
            "je schrijft het zonder de eenheid erbij om verwarring te vermijden",
            "je schrijft het als een breuk met een teller en een noemer",
        ],
        antwoord=0,
        uitleg="Zo blijft een heel groot of heel klein getal leesbaar. 0,000045 meter wordt dan 4,5 maal tien tot de macht min vijf meter.",
    ),
    dict(
        type="waarofniet",
        vraag="Het voorvoegsel milli betekent een miljoenste.",
        antwoord=False,
        uitleg="Milli is een duizendste; een miljoenste is micro. De reeks loopt van mega over kilo, centi en milli tot micro en nano.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel meter is 2,5 kilometer?",
        opties=["2500 meter", "250 meter", "25 000 meter", "0,0025 meter"],
        antwoord=0,
        uitleg="Kilo betekent duizend, dus vermenigvuldig je met 1000. Omgekeerd deel je door 1000 om van meter naar kilometer te gaan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schakel je een meetinstrument uit als je niet meet?",
        opties=[
            "je spaart energie en de batterij blijft langer goed",
            "het instrument wordt daardoor veel nauwkeuriger bij de volgende meting",
            "het instrument onthoudt zo zijn laatste meting voor de volgende keer",
            "je voorkomt daarmee dat het instrument een verkeerd bereik kiest",
        ],
        antwoord=0,
        uitleg="Dat hoort bij duurzaam werken in het labo. Een multimeter op de weerstandsstand loopt bovendien snel leeg.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag biologisch materiaal met je blote handen vastnemen zolang je er daarna niets meer mee doet.",
        antwoord=False,
        uitleg="Bij biologisch materiaal werk je altijd hygiënisch, met handschoenen en met gewassen handen nadien. Anders breng je micro-organismen over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk pictogram verwacht je op een flesje met een sterk zuur?",
        opties=[
            "het pictogram voor bijtende stoffen",
            "het pictogram voor ontvlambare stoffen",
            "het pictogram voor stoffen onder druk",
            "het pictogram voor radioactieve stoffen",
        ],
        antwoord=0,
        uitleg="Een sterk zuur tast je huid en je ogen aan. Daarom staan er ook P-zinnen over handschoenen en een veiligheidsbril op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke instrumenten gebruik je om een tijdsduur, een kracht en een temperatuur te meten? Kruis alles aan wat juist is.",
        opties=[
            "een chronometer voor de tijd",
            "een dynamometer voor de kracht",
            "een thermometer voor de temperatuur",
            "een manometer voor de temperatuur",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een manometer meet druk, niet temperatuur. Elk instrument heeft zijn eigen grootheid en zijn eigen eenheid.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de cijfers van een meetresultaat die echt iets zeggen over de nauwkeurigheid?",
        antwoord="beduidende cijfers",
        uitleg="Meet je 12,3 centimeter, dan heb je drie beduidende cijfers. Je mag er in je antwoord niet meer bij schrijven dan je gemeten hebt.",
    ),
    dict(
        type="waarofniet",
        vraag="Een schatting maken voor je begint te rekenen, helpt om een onzinnig antwoord te herkennen.",
        antwoord=True,
        uitleg="Weet je ongeveer wat eruit moet komen, dan zie je een fout van een factor duizend meteen. Dat hoort bij wetenschappelijk rekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest op een etiket: H314, veroorzaakt ernstige brandwonden en oogletsel. Wat doe je?",
        opties=[
            "je draagt handschoenen en een veiligheidsbril bij het werken",
            "je houdt de stof enkel weg van een vlam of een warmtebron",
            "je giet de stof na gebruik gewoon in de gootsteen weg",
            "je gebruikt de stof zonder voorzorgen in kleine hoeveelheden",
        ],
        antwoord=0,
        uitleg="De H-zin zegt wat het gevaar is, de P-zinnen wat je ertegen doet. Bij bijtende stoffen is bescherming van je huid en ogen het eerste.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waarvoor leg je een slachtoffer in stabiele zijligging?",
        opties=[
            "zodat de luchtweg vrij blijft bij een slachtoffer dat zelf ademt",
            "zodat je gemakkelijker een hartmassage kan uitvoeren",
            "zodat het slachtoffer sneller weer bij bewustzijn komt",
            "zodat je het slachtoffer makkelijker naar een warme plaats kan dragen",
        ],
        antwoord=0,
        uitleg="Op de rug kan de tong of braaksel de luchtweg afsluiten. In zijligging loopt alles naar buiten en blijft de weg open.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan herken je een hartstilstand? Kruis alles aan wat juist is.",
        opties=[
            "het slachtoffer reageert niet",
            "het slachtoffer ademt niet of niet normaal",
            "het hart pompt geen bloed meer rond",
            "het slachtoffer klaagt over pijn in de arm",
        ],
        antwoord=[0, 1, 2],
        uitleg="Niet reageren en niet normaal ademen zijn de twee dingen die je zelf vaststelt. Pijn in de arm kan een waarschuwing vooraf zijn, maar is geen hartstilstand.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een hartstilstand moet je binnen enkele minuten beginnen te reanimeren.",
        antwoord=True,
        uitleg="Zonder bloedcirculatie krijgen de hersenen geen zuurstof meer. Elke minuut die verloren gaat, kost overlevingskans.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je eerst bij een slachtoffer dat niet reageert?",
        opties=[
            "je roept om hulp en controleert of het normaal ademt",
            "je begint onmiddellijk met mond-op-mond beademing",
            "je legt het meteen in stabiele zijligging op de grond",
            "je geeft het water te drinken om het bij te brengen",
        ],
        antwoord=0,
        uitleg="Eerst kijken en roepen, dan pas handelen. Zo weet je of je moet reanimeren of in zijligging moet leggen, en komt er hulp onderweg.",
    ),
    dict(
        type="invultekst",
        vraag="Welk noodnummer bel je in België bij een hartstilstand?",
        antwoord="112",
        uitleg="Dat nummer werkt in heel Europa en is gratis. Zet je telefoon op de luidspreker zodat je handen vrij blijven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar duw je bij een hartmassage?",
        opties=[
            "midden op de borstkas, op het onderste deel van het borstbeen",
            "links op de borstkas, net boven de plaats van het hart",
            "onder de borstkas, op de bovenkant van de buik",
            "boven de borstkas, net onder het kuiltje tussen de sleutelbeenderen",
        ],
        antwoord=0,
        uitleg="Je duwt met de hiel van je hand, recht naar beneden en diep genoeg. Zo pers je het hart samen tussen het borstbeen en de rug.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een reanimatie wissel je dertig hartmassages af met twee beademingen.",
        antwoord=True,
        uitleg="Je houdt daarbij een tempo van ongeveer honderd tot honderdtwintig duwbewegingen per minuut aan. Kan je niet beademen, dan blijf je toch doorduwen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je bij iemand die zich verslikt en nog krachtig kan hoesten?",
        opties=[
            "je moedigt het hoesten aan en blijft erbij kijken",
            "je geeft onmiddellijk vijf stevige rugslagen",
            "je geeft onmiddellijk vijf buikstoten achter elkaar",
            "je legt de persoon plat op de rug op de grond",
        ],
        antwoord=0,
        uitleg="Hoesten is de krachtigste manier om een voorwerp los te krijgen. Pas als dat niet meer gaat, geef je rugslagen en buikstoten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn rugslagen bij een verslikking?",
        opties=[
            "vijf slagen met de hiel van je hand tussen de schouderbladen",
            "vijf slagen met je vlakke hand midden op de onderrug",
            "vijf stoten met je vuist in de buik onder het borstbeen",
            "vijf duwbewegingen op het borstbeen zoals bij een hartmassage",
        ],
        antwoord=0,
        uitleg="Je laat de persoon daarbij voorover buigen zodat het voorwerp naar buiten kan. Helpt dat niet, dan volgen de buikstoten.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de stoten in de buik waarmee je een voorwerp uit de luchtweg probeert te duwen?",
        antwoord="buikstoten",
        uitleg="Je staat daarbij achter de persoon en trekt je vuist schuin naar boven. Je wisselt ze af met rugslagen tot het voorwerp loskomt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over hulp bij een verdrinking zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "je zorgt eerst voor je eigen veiligheid",
            "je haalt het slachtoffer uit het water als dat veilig kan",
            "je begint bij een slachtoffer dat niet ademt met beademen",
            "je springt altijd meteen zelf het water in",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een hulpverlener die zelf verdrinkt helpt niemand. Reik dus eerst iets aan of roep hulp, en spring alleen als het echt veilig is.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een verdrinking is het zuurstoftekort het grootste gevaar.",
        antwoord=True,
        uitleg="Water in de luchtweg belet de opname van zuurstof. Daarom begint de hulp bij een verdrinking met beademen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet iemand in elkaar zakken die niet reageert en niet ademt. Wat is de juiste volgorde?",
        opties=[
            "hulp bellen, dan onmiddellijk starten met hartmassage",
            "eerst in stabiele zijligging leggen, dan hulp bellen",
            "eerst water geven, dan kijken of het beter gaat",
            "eerst de pols voelen, dan tien minuten wachten",
        ],
        antwoord=0,
        uitleg="Elke minuut zonder bloedcirculatie kost overlevingskans. Hulp bellen en duwen gaan daarom samen, met iemand anders aan de telefoon als dat kan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom leg je iemand die wel ademt maar niet reageert niet op de rug?",
        opties=[
            "op de rug kan de tong of braaksel de luchtweg afsluiten",
            "op de rug koelt het slachtoffer veel sneller af dan op de zij",
            "op de rug kan je de ademhaling helemaal niet controleren",
            "op de rug is het veel moeilijker om de pols te kunnen voelen",
        ],
        antwoord=0,
        uitleg="In zijligging blijft de luchtweg open en kan vocht naar buiten lopen. Daarom is dat de juiste houding voor wie zelf ademt.",
    ),
    dict(
        type="waarofniet",
        vraag="Je mag een reanimatie stoppen zodra je moe wordt, ook als er nog geen hulp is.",
        antwoord=False,
        uitleg="Je gaat door tot de hulpdiensten overnemen of het slachtoffer weer normaal ademt. Wissel liever af met iemand anders dan te stoppen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe diep duw je bij een hartmassage bij een volwassene?",
        opties=[
            "ongeveer vijf tot zes centimeter",
            "ongeveer één tot twee centimeter",
            "ongeveer tien tot twaalf centimeter",
            "net genoeg om de huid in te drukken",
        ],
        antwoord=0,
        uitleg="Minder diep duwen pompt te weinig bloed rond. Je laat de borstkas tussen twee duwbewegingen ook volledig terugkomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan herken je dat iemand zich ernstig verslikt heeft?",
        opties=[
            "de persoon kan niet meer hoesten, spreken of goed ademen",
            "de persoon hoest krachtig en kan nog gewoon antwoorden",
            "de persoon heeft het warm en begint sterk te zweten",
            "de persoon klaagt over hoofdpijn en gaat even zitten",
        ],
        antwoord=0,
        uitleg="Dan is de luchtweg bijna of volledig afgesloten. Je begint onmiddellijk met rugslagen en buikstoten, en laat 112 bellen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de houding waarin je een slachtoffer legt dat niet reageert maar wel normaal ademt?",
        antwoord="stabiele zijligging",
        uitleg="Het hoofd ligt daarbij achterover en iets naar beneden. Zo blijft de luchtweg open en kan vocht uit de mond lopen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hartstilstand kan je herkennen doordat het slachtoffer luid en snel ademt.",
        antwoord=False,
        uitleg="Bij een hartstilstand ademt het slachtoffer niet of niet normaal, en reageert het niet. Een paar happende bewegingen zijn geen normale ademhaling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand verslikt zich en de rugslagen helpen niet. Wat doe je dan?",
        opties=[
            "je geeft vijf buikstoten en wisselt daarna weer af met rugslagen",
            "je laat de persoon rustig gaan zitten en wacht op de hulpdiensten",
            "je geeft de persoon water te drinken om het voorwerp mee te slikken",
            "je legt de persoon in stabiele zijligging en blijft ernaast zitten",
        ],
        antwoord=0,
        uitleg="Je blijft afwisselen tot het voorwerp loskomt of de persoon het bewustzijn verliest. Verliest hij het bewustzijn, dan begin je te reanimeren.",
    ),
]

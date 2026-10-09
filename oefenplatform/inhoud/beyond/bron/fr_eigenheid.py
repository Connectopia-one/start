# -*- coding: utf-8 -*-
"""De eigenheid van de filosofie.

Het eerste van twaalf thema's over filosofie. De fiche begint niet bij een
filosoof maar bij de vraag wat filosofie eigenlijk is, en waarin ze verschilt
van de wetenschappen ernaast.

De lijstjes staan letterlijk in de fiche:

    gelijkenissen en verschillen tussen: natuurwetenschappen en
        menswetenschappen (sociale en gedragswetenschappen)
    de eigenheid van de filosofie binnen de menswetenschappen
    filosofische verwondering, en waarom ze noodzakelijk is
    de oorsprong van de filosofie: westerse filosofie onderscheiden van
        mythologie en van natuurfilosofie
    de kenmerken van filosofische vragen, en daarmee filosofische van
        niet-filosofische vragen onderscheiden
    de verschillende filosofische domeinen

De fiche noemt de domeinen niet bij naam. Daarom vragen de vragen hieronder
naar de domeinen die de fiche zélf behandelt (wijsgerige antropologie, ethiek,
wetenschapsfilosofie, kennisleer en logica) en naar wat een domein tot een
domein maakt, en niet naar een lijstje dat de fiche niet geeft.

Deel 1 zijn de wetenschappen, de eigenheid van de filosofie en de verwondering.
Deel 2 zijn de oorsprong, de kenmerken van filosofische vragen en de domeinen.
"""

DEEL1 = [
    dict(type="meerkeuze",
         vraag="Wat onderzoeken de natuurwetenschappen?",
         opties=["de natuur en haar verschijnselen, zoals stof, leven en beweging",
                 "de mens en zijn samenleven met anderen",
                 "de vragen waar geen enkel onderzoek ooit een antwoord op geeft",
                 "de geschiedenis van het denken over goed en kwaad"],
         antwoord=0,
         uitleg="Natuurwetenschappen zoals fysica, chemie en biologie onderzoeken de natuur. "
                "Menswetenschappen onderzoeken de mens en de samenleving."),
    dict(type="meerkeuze",
         vraag="Welke twee wetenschappen noemt de fiche bij de menswetenschappen?",
         opties=["de sociale wetenschappen en de gedragswetenschappen",
                 "de natuurkunde, de scheikunde en de sterrenkunde",
                 "de geneeskunde en de biologie",
                 "de rechtswetenschap, de economie en de geneeskunde"],
         antwoord=0,
         uitleg="De fiche zet het er met zoveel woorden bij: menswetenschappen zijn de sociale en "
                "de gedragswetenschappen."),
    dict(type="meerkeuze",
         vraag="Wat hebben de natuur- en de menswetenschappen met elkaar gemeen?",
         opties=["ze werken beide met onderzoek, met gegevens en met een methode",
                 "ze zoeken beide naar de zin van het bestaan van de mens",
                 "ze kunnen beide hun uitkomsten in een laboratorium nameten",
                 "ze doen beide uitspraken over wat goed en kwaad is"],
         antwoord=0,
         uitleg="Beide zijn wetenschappen: ze onderbouwen hun uitspraken met gegevens die volgens "
                "een methode verzameld zijn, en ze laten zich nakijken."),
    dict(type="meerkeuze",
         vraag="Waarin verschillen de menswetenschappen van de natuurwetenschappen?",
         opties=["hun onderwerp denkt zelf mee, en een experiment in een labo kan vaak niet",
                 "zij maken helemaal geen gebruik van cijfers of statistiek",
                 "zij hebben geen methode nodig om tot een uitspraak te komen",
                 "zij onderzoeken enkel wat vroeger gebeurd is en niet het heden"],
         antwoord=0,
         uitleg="Het onderwerp van een menswetenschap is een mens: die weet dat hij onderzocht "
                "wordt en past zich aan. Een zuiver experiment is daardoor veel moeilijker."),
    dict(type="meerkeuze",
         vraag="Wat is de eigenheid van de filosofie binnen de menswetenschappen?",
         opties=["ze onderzoekt niet met gegevens maar met redeneren en met begrippen",
                 "ze onderzoekt de mens met vragenlijsten en met statistiek",
                 "ze onderzoekt uitsluitend teksten van filosofen uit de oudheid",
                 "ze onderzoekt het brein en zijn werking met beeldvorming"],
         antwoord=0,
         uitleg="Een filosoof verzamelt geen gegevens maar denkt na: hij onderzoekt begrippen, "
                "veronderstellingen en redeneringen. Zijn gereedschap is het argument."),
    dict(type="meerkeuze",
         vraag="Een socioloog en een filosoof werken beide over het begrip rechtvaardigheid. Wat "
               "doet de filosoof?",
         opties=["hij vraagt wat rechtvaardigheid betekent en waarop dat begrip steunt",
                 "hij meet hoeveel mensen hun loon rechtvaardig vinden",
                 "hij beschrijft hoe het begrip in de wetgeving staat",
                 "hij vergelijkt de lonen van twee groepen met elkaar"],
         antwoord=0,
         uitleg="De socioloog meet wat mensen vinden; de filosoof onderzoekt het begrip zelf en de "
                "argumenten eronder."),
    dict(type="meerkeuze",
         vraag="Welke uitspraken over de verhouding tussen filosofie en wetenschap kloppen?",
         opties=["filosofie onderzoekt ook de veronderstellingen waarop een wetenschap rust",
                 "filosofie kan vragen stellen die met geen enkele meting te beslechten zijn",
                 "filosofie vervangt de wetenschappen zodra die een vraag niet kunnen oplossen",
                 "filosofie levert zelf meetgegevens aan over de natuur"],
         antwoord=[0, 1],
         uitleg="De eerste twee: ze onderzoekt de grond onder een wetenschap en ze stelt vragen "
                "die buiten het bereik van een meting liggen. Ze vervangt geen wetenschap en ze "
                "meet zelf niet."),
    dict(type="meerkeuze",
         vraag="Wat is filosofische verwondering?",
         opties=["je verbazen over iets dat zo gewoon is dat niemand er nog bij stilstaat",
                 "je verbazen over iets dat nog nooit eerder gebeurd is",
                 "het gevoel dat je iets helemaal niet kan begrijpen en het daarom maar opgeeft",
                 "de bewondering die je voelt bij een mooi kunstwerk"],
         antwoord=0,
         uitleg="Verwondering is niet schrikken van iets zeldzaams. Ze is het vreemd gaan vinden "
                "van het alledaagse: dat er iets is, dat ik besta, dat tijd verstrijkt."),
    dict(type="meerkeuze",
         vraag="Waarom is filosofische verwondering noodzakelijk binnen de filosofie?",
         opties=["zonder verwondering komt er geen vraag, en zonder vraag geen filosofie",
                 "zonder verwondering kan je geen gegevens verzamelen",
                 "zonder verwondering kan je geen filosofen uit de oudheid lezen",
                 "zonder verwondering kan een redenering niet geldig zijn"],
         antwoord=0,
         uitleg="Verwondering is het vertrekpunt: ze maakt het gewone weer een vraag. Wie zich "
                "nergens over verwondert, heeft niets om over na te denken."),
    dict(type="meerkeuze",
         vraag="Welk van deze uitspraken wijst op filosofische verwondering?",
         opties=["waarom zou ik eigenlijk doen wat afgesproken is?",
                 "hoeveel leerlingen van onze school komen met de bus?",
                 "wanneer sluit de bibliotheek vandaag?",
                 "hoeveel graden is het buiten?"],
         antwoord=0,
         uitleg="De eerste vraag maakt iets alledaags tot een vraag en is met geen meting te "
                "beslechten. De drie andere zijn gewoon op te zoeken."),
    dict(type="meerkeuze",
         vraag="Een wetenschapper vraagt zich af of zijn vak wel echt objectief is. Wat doet hij?",
         opties=["hij filosofeert over zijn eigen wetenschap",
                 "hij doet een experiment binnen zijn eigen wetenschap",
                 "hij verlaat de wetenschap en kiest voor de mythologie",
                 "hij stelt een vraag die niemand mag stellen"],
         antwoord=0,
         uitleg="Een vraag over de veronderstellingen van een wetenschap is geen vraag ván die "
                "wetenschap maar een filosofische vraag: dat is wetenschapsfilosofie."),
    dict(type="meerkeuze",
         vraag="Waarom is het moeilijk om in de menswetenschappen een wet te formuleren die altijd "
               "opgaat?",
         opties=["mensen verschillen van elkaar en veranderen hun gedrag als ze iets weten",
                 "menswetenschappers mogen geen statistiek gebruiken van hun vakgebied",
                 "er bestaat in de menswetenschappen geen enkele vorm van onderzoek",
                 "menswetenschappen bestaan nog te kort om wetten te hebben"],
         antwoord=0,
         uitleg="Mensen zijn geen stenen: ze verschillen, ze kiezen zelf mee, en ze passen hun "
                "gedrag aan als ze weten wat er van hen verwacht wordt."),
    dict(type="waarofniet",
         vraag="Volgens de fiche horen de sociale en de gedragswetenschappen bij de "
               "menswetenschappen.",
         antwoord=True,
         uitleg="Waar. De fiche noemt de menswetenschappen en zet er de sociale en de "
                "gedragswetenschappen bij."),
    dict(type="waarofniet",
         vraag="Filosofie onderscheidt zich van de andere menswetenschappen doordat ze haar "
               "uitspraken met meetgegevens onderbouwt.",
         antwoord=False,
         uitleg="Niet waar. Juist niet: de filosofie werkt met redeneren en met begrippen. Het "
                "onderbouwen met meetgegevens is wat de andere menswetenschappen doen."),
    dict(type="waarofniet",
         vraag="Filosofische verwondering gaat over wat zeldzaam en spectaculair is.",
         antwoord=False,
         uitleg="Niet waar. Ze gaat juist over het alledaagse: dat er iets is, dat ik er ben, dat "
                "tijd verstrijkt."),
    dict(type="waarofniet",
         vraag="Een vraag over de veronderstellingen van een wetenschap is zelf een filosofische "
               "vraag.",
         antwoord=True,
         uitleg="Waar. Die vraag kan je met het onderzoek van die wetenschap niet beslechten; ze "
                "hoort bij de wetenschapsfilosofie."),
    dict(type="invultekst",
         vraag="Hoe heet het je verbazen over wat zo gewoon is dat niemand er nog bij stilstaat? "
               "De filosofische ...",
         antwoord=["verwondering"],
         uitleg="Filosofische verwondering is het vertrekpunt van elke filosofische vraag."),
    dict(type="invultekst",
         vraag="Welke twee wetenschappen rekent de fiche tot de menswetenschappen? De sociale en "
               "de ...",
         antwoord=["gedragswetenschappen"],
         uitleg="De fiche noemt de sociale en de gedragswetenschappen als de menswetenschappen."),
    dict(type="invultekst",
         vraag="Fysica, chemie en biologie horen samen bij de ...",
         antwoord=["natuurwetenschappen"],
         uitleg="Die drie onderzoeken de natuur en haar verschijnselen."),
    dict(type="invultekst",
         vraag="Met welk gereedschap onderbouwt een filosoof zijn uitspraak, in plaats van met "
               "meetgegevens? Met een ...",
         antwoord=["argument", "redenering"],
         uitleg="De filosofie werkt met argumenten en redeneringen, niet met metingen."),
]

DEEL2 = [
    dict(type="meerkeuze",
         vraag="Wat kenmerkt een verklaring uit de mythologie?",
         opties=["ze verklaart de wereld met verhalen over goden en bovennatuurlijke krachten",
                 "ze verklaart de wereld met oorzaken die je in de natuur zelf kan nagaan",
                 "ze verklaart de wereld met redeneringen die je kan nakijken",
                 "ze verklaart de wereld met gegevens uit een experiment"],
         antwoord=0,
         uitleg="Een mythe geeft een verhaal: de bliksem komt van een god die kwaad is. Dat "
                "verhaal valt niet na te gaan en vraagt geen argument."),
    dict(type="meerkeuze",
         vraag="Wat deden de natuurfilosofen anders dan de mythologie?",
         opties=["zij zochten een verklaring in de natuur zelf, zonder goden erbij te halen",
                 "zij schreven hun verklaringen op in verhalen over helden",
                 "zij deden hun uitspraken enkel over goed en kwaad",
                 "zij weigerden iedere uitspraak over de natuur te doen"],
         antwoord=0,
         uitleg="Dat is de stap die de fiche aanwijst: van een verhaal over goden naar een "
                "verklaring binnen de natuur zelf, waarover je kan redetwisten."),
    dict(type="meerkeuze",
         vraag="Waarom ziet de fiche de overgang van mythologie naar natuurfilosofie als het begin "
               "van de westerse filosofie?",
         opties=["omdat een verklaring vanaf dan met argumenten verdedigd en betwist kon worden",
                 "omdat de mythen vanaf dan niet meer verteld werden",
                 "omdat de natuurfilosofen al met een laboratorium werkten",
                 "omdat de goden vanaf dan uit de verhalen verdwenen waren"],
         antwoord=0,
         uitleg="Het beslissende is niet dat de goden wegvielen maar dat er een "
                "<em>argument</em> kwam: een verklaring die je kan tegenspreken en verbeteren."),
    dict(type="meerkeuze",
         vraag="Welke kenmerken heeft een filosofische vraag?",
         opties=["ze is niet met een meting of een opzoeking te beslechten",
                 "ze raakt aan de begrippen en de veronderstellingen zelf",
                 "ze heeft precies één antwoord waar iedereen het over eens is",
                 "ze gaat altijd over een gebeurtenis uit het verleden"],
         antwoord=[0, 1],
         uitleg="De eerste twee. Een filosofische vraag valt niet met een meting te beslechten en "
                "raakt aan de begrippen zelf. Eén antwoord waar iedereen het over eens is, is er "
                "net niet."),
    dict(type="meerkeuze",
         vraag="Welke van deze vragen zijn filosofische vragen?",
         opties=["wat maakt een straf rechtvaardig?",
                 "mag een samenleving iemand straffen om anderen af te schrikken?",
                 "hoeveel gevangenen zitten er vandaag in België?",
                 "welke rechtbank behandelt een diefstal van een fiets?"],
         antwoord=[0, 1],
         uitleg="De eerste twee raken aan een begrip en zijn met geen opzoeking te beslechten. Het "
                "aantal gevangenen en de bevoegde rechtbank zijn gewoon op te zoeken."),
    dict(type="meerkeuze",
         vraag="Welke van deze vragen is géén filosofische vraag?",
         opties=["op welke leeftijd mag je in België stemmen?",
                 "bestaat er iets als een vrije wil?",
                 "mag je iemand pijn doen om een ander te sparen?",
                 "kan een machine bewustzijn hebben?"],
         antwoord=0,
         uitleg="De stemleeftijd staat in de wet: dat is een opzoeking. De drie andere zijn met "
                "geen enkel gegeven te beslechten."),
    dict(type="meerkeuze",
         vraag="Een vriend zegt: dat is gewoon een kwestie van smaak, daar valt niets over te "
               "zeggen. Wat is het filosofische bezwaar?",
         opties=["ook over een smaakoordeel kan je argumenten geven en die wegen",
                 "een smaakoordeel bestaat niet, er is altijd één juist antwoord",
                 "smaak hoort niet bij de filosofie maar bij de natuurwetenschappen",
                 "over smaak kan enkel een wetenschapper een uitspraak doen"],
         antwoord=0,
         uitleg="De filosofie zegt niet dat er één juist antwoord is, maar wel dat er "
                "<em>betere en slechtere argumenten</em> zijn. Daarmee valt er wel iets te zeggen."),
    dict(type="meerkeuze",
         vraag="Welk filosofisch domein onderzoekt wat goed handelen is?",
         opties=["de ethiek", "de kennisleer", "de logica", "de wijsgerige antropologie"],
         antwoord=0,
         uitleg="De ethiek onderzoekt goed handelen en rechtvaardig samenleven. Dat is in deze "
                "fiche het grootste filosofische onderdeel."),
    dict(type="meerkeuze",
         vraag="Welk filosofisch domein onderzoekt wat de mens is?",
         opties=["de wijsgerige antropologie", "de ethiek", "de logica",
                 "de kennisleer of epistemologie"],
         antwoord=0,
         uitleg="De wijsgerige antropologie vraagt wat een mens is: lichaam en geest, mens en "
                "dier, vrijheid en determinisme."),
    dict(type="meerkeuze",
         vraag="Welk filosofisch domein onderzoekt wanneer een redenering geldig is?",
         opties=["de logica", "de ethiek", "de wijsgerige antropologie",
                 "de wetenschapsfilosofie"],
         antwoord=0,
         uitleg="De logica onderzoekt de vorm van een redenering: de argumentatieleer van deze "
                "fiche hoort daar thuis."),
    dict(type="meerkeuze",
         vraag="Welk filosofisch domein onderzoekt hoe wij aan kennis komen?",
         opties=["de kennisleer", "de ethiek", "de esthetica", "de wijsgerige antropologie"],
         antwoord=0,
         uitleg="De kennisleer vraagt waar kennis vandaan komt. Het rationalisme en het empirisme "
                "van deze fiche horen daar thuis."),
    dict(type="meerkeuze",
         vraag="Wat maakt van een reeks vragen een filosofisch domein?",
         opties=["de vragen gaan over hetzelfde soort onderwerp en hangen met elkaar samen",
                 "de vragen zijn alle door een en dezelfde filosoof gesteld en beantwoord",
                 "de vragen hebben alle een antwoord gekregen",
                 "de vragen komen alle uit dezelfde eeuw"],
         antwoord=0,
         uitleg="Een domein bundelt vragen die over hetzelfde soort onderwerp gaan: over kennis, "
                "over goed handelen, over de mens, over geldige redeneringen."),
    dict(type="waarofniet",
         vraag="De natuurfilosofen zochten hun verklaringen in de natuur zelf in plaats van bij de "
               "goden.",
         antwoord=True,
         uitleg="Waar. Dat is precies de stap die de fiche als de oorsprong van de westerse "
                "filosofie aanwijst."),
    dict(type="waarofniet",
         vraag="Een vraag is filosofisch zodra niemand het antwoord kent.",
         antwoord=False,
         uitleg="Niet waar. Hoeveel sterren er zijn, weet niemand precies, en dat is geen "
                "filosofische vraag. Het gaat erom dat een meting de vraag niet kan beslechten."),
    dict(type="waarofniet",
         vraag="De wetenschapsfilosofie onderzoekt de methode en de grenzen van de wetenschap.",
         antwoord=True,
         uitleg="Waar. Dat is het domein waarin de falsificatie en het demarcatievraagstuk van "
                "deze fiche thuishoren."),
    dict(type="waarofniet",
         vraag="Omdat filosofische vragen geen vast antwoord hebben, is het ene antwoord even goed "
               "als het andere.",
         antwoord=False,
         uitleg="Niet waar. Er zijn wel betere en slechtere <em>argumenten</em>, en daarover valt "
                "wel te beslissen. Dat is waarom de fiche de argumentatieleer vraagt."),
    dict(type="invultekst",
         vraag="Hoe heet een verklaring van de wereld met verhalen over goden?",
         antwoord=["mythologie", "een mythe"],
         uitleg="De westerse filosofie onderscheidt zich van de mythologie doordat ze met "
                "argumenten werkt."),
    dict(type="invultekst",
         vraag="Hoe heet de denkers die als eersten een verklaring in de natuur zelf zochten? De ...",
         antwoord=["natuurfilosofen"],
         uitleg="De natuurfilosofie staat tussen de mythologie en de latere wetenschap in."),
    dict(type="invultekst",
         vraag="Welk filosofisch domein onderzoekt goed handelen en rechtvaardig samenleven?",
         antwoord=["de ethiek", "ethiek"],
         uitleg="De ethiek is in deze fiche het grootste filosofische onderdeel."),
    dict(type="invultekst",
         vraag="Welk filosofisch domein onderzoekt of een redenering geldig is?",
         antwoord=["de logica", "logica"],
         uitleg="De argumentatieleer van deze fiche hoort bij de logica."),
]

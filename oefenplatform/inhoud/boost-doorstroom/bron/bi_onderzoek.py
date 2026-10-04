# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Wetenschappelijk onderzoek en STEM.

Hoort bij de kop "wetenschappelijk onderzoek en STEM" van de vakfiche
biologie 2de graad doorstroomfinaliteit, die 10 % van het examen weegt.

Deel 1 gaat over de onderzoekscyclus: vraag, hypothese, variabelen,
controlegroep, metingen, besluit en de kritiek op een opzet. Deel 2 gaat
over het gereedschap en de omgang met gegevens: de microscoop, een
preparaat, veiligheid in het labo, tabellen en grafieken, en wat wetenschap
onderscheidt van een los vermoeden.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat is een goede onderzoeksvraag?",
        opties=[
            "een vraag die je met een meting kan beantwoorden",
            "een vraag waarop iedereen het antwoord al kent",
            "een vraag over wat het mooist is",
            "een vraag die je enkel met je mening kan beantwoorden",
        ],
        antwoord=0,
        uitleg="Een onderzoeksvraag moet toetsbaar zijn. Of iets mooi is, kan je niet meten; hoeveel iets groeit, wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een hypothese?",
        opties=[
            "een beredeneerde verwachting die je kan toetsen",
            "het besluit dat je na het onderzoek opschrijft",
            "een vermoeden dat altijd juist blijkt te zijn",
            "de lijst materialen die je nodig hebt",
        ],
        antwoord=0,
        uitleg="Een hypothese is een verwachting met een reden erbij. Dat ze onderuit gehaald kan worden, is net haar kracht.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hypothese die door het onderzoek weerlegd wordt, maakt het onderzoek mislukt.",
        antwoord=False,
        uitleg="Een weerlegde hypothese is een resultaat. Je weet dan iets wat je voordien niet wist.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de factor die je in een proef bewust verandert?",
        antwoord=["onafhankelijke variabele", "onafhankelijke veranderlijke", "onafhankelijke"],
        uitleg="De onafhankelijke variabele is wat je zelf instelt, bijvoorbeeld de hoeveelheid licht. Wat je dan meet, is de afhankelijke variabele.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt of meer licht een plant sneller doet groeien. Wat is de afhankelijke variabele?",
        opties=[
            "de lengte van de plant na enkele weken",
            "de lichtsterkte van de lamp",
            "de hoeveelheid water die je geeft",
            "de soort potgrond",
        ],
        antwoord=0,
        uitleg="De afhankelijke variabele is wat je meet en wat van je instelling afhangt. De lichtsterkte stel je zelf in, dus die is onafhankelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat houd je in zo'n proef constant? Kruis alles aan wat juist is.",
        opties=[
            "de hoeveelheid water",
            "de soort potgrond",
            "de temperatuur",
            "de lichtsterkte",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alles behalve de variabele die je onderzoekt, houd je gelijk. Anders weet je niet waar een verschil van komt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de groep in een proef die de behandeling niet krijgt, zodat je kan vergelijken?",
        antwoord=["controlegroep", "de controlegroep", "controle"],
        uitleg="Zonder controlegroep weet je niet wat er zonder behandeling gebeurd zou zijn. Zij is de meetlat van je proef.",
    ),
    dict(
        type="waarofniet",
        vraag="Een proef zonder controlegroep laat geen betrouwbaar besluit toe.",
        antwoord=True,
        uitleg="Je weet dan niet of het effect van je behandeling kwam of gewoon van het verstrijken van de tijd. De vergelijking is de kern van een proef.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom herhaal je een meting meerdere keren?",
        opties=[
            "om de invloed van toeval en meetfouten te verkleinen",
            "om het resultaat te laten kloppen met je hypothese",
            "om het onderzoek langer te laten duren",
            "om minder planten nodig te hebben",
        ],
        antwoord=0,
        uitleg="Eén meting kan er net naast zitten. Door te herhalen en te gemiddelden zie je het werkelijke verband beter.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom gebruik je meerdere planten per groep in plaats van één?",
        opties=[
            "individuen verschillen, en met meer valt dat weg",
            "een enkele plant groeit altijd trager",
            "meer planten betekent een hogere nauwkeurigheid van de meetlat",
            "zo hoef je niet te herhalen in de tijd",
        ],
        antwoord=0,
        uitleg="De ene plant is van nature sterker dan de andere. Door er meerdere te nemen, meet je het verband en niet het toeval.",
    ),
    dict(
        type="waarofniet",
        vraag="Een onderzoeker die zijn metingen aanpast omdat ze niet bij zijn hypothese passen, pleegt wetenschappelijke fraude.",
        antwoord=True,
        uitleg="De gegevens zijn de werkelijkheid; de hypothese is slechts een verwachting. Wie de gegevens bijschaaft, maakt het onderzoek waardeloos.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een waarneming en een gevolgtrekking?",
        opties=[
            "een waarneming is wat je vaststelt, een gevolgtrekking wat je besluit",
            "een waarneming gebeurt met een toestel, een gevolgtrekking met het oog",
            "een waarneming komt na het besluit",
            "er is geen verschil tussen de twee",
        ],
        antwoord=0,
        uitleg="Het blad is geel is een waarneming. De plant krijgt te weinig water is een gevolgtrekking, en die kan fout zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de verzameling gegevens die je tijdens een proef opschrijft?",
        antwoord=["meetresultaten", "resultaten", "meetgegevens"],
        uitleg="Je noteert meteen en onbewerkt, in een tabel met de eenheden erbij. Pas daarna ga je rekenen en tekenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke onderdelen horen in een verslag van een onderzoek? Kruis alles aan wat juist is.",
        opties=[
            "de onderzoeksvraag en de hypothese",
            "de werkwijze en het materiaal",
            "de resultaten en het besluit",
            "de naam van de klasgenoot die je het best kan helpen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een verslag moet iemand anders in staat stellen je proef over te doen. Daarvoor zijn vraag, werkwijze, resultaten en besluit nodig.",
    ),
    dict(
        type="waarofniet",
        vraag="Een werkwijze is goed beschreven als iemand anders je proef ermee kan overdoen.",
        antwoord=True,
        uitleg="Herhaalbaarheid is de toets. Daarom horen hoeveelheden, tijden en toestellen er precies in.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een leerling besluit uit een proef met twee planten dat licht de groei bevordert. Wat is de belangrijkste kritiek?",
        opties=[
            "twee planten zijn te weinig om toeval uit te sluiten",
            "licht heeft niets met groei te maken",
            "de hypothese was te duidelijk opgeschreven",
            "de proef duurde te kort om een tabel te maken",
        ],
        antwoord=0,
        uitleg="Met twee planten kan één sterke of zwakke plant het hele resultaat bepalen. Meer exemplaren en een herhaling lossen dat op.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een proef met twee groepen plantjes geeft een verschil in lengte, maar de ene groep stond ook warmer. Wat is het probleem?",
        opties=[
            "er veranderden twee factoren tegelijk, dus weet je de oorzaak niet",
            "er waren te weinig metingen per dag",
            "de hypothese was niet opgeschreven",
            "de lengtes zijn in centimeter gemeten in plaats van in millimeter",
        ],
        antwoord=0,
        uitleg="Verandert er meer dan één ding, dan is het verband niet meer eenduidig. Dat heet een storende variabele.",
    ),
    dict(
        type="waarofniet",
        vraag="Een verband dat je in een proef vindt, betekent altijd dat het ene het andere veroorzaakt.",
        antwoord=False,
        uitleg="Twee dingen kunnen samen veranderen door een derde oorzaak. Een verband is dus nog geen bewijs van oorzaak en gevolg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent STEM?",
        opties=[
            "wetenschappen, technologie, ingenieurswetenschappen en wiskunde",
            "studie, techniek, elektronica en metaalbewerking samen",
            "een vak waarin je enkel proeven doet",
            "het samengaan van sport, techniek en muziek",
        ],
        antwoord=0,
        uitleg="STEM brengt die vier samen rond een echt probleem. Je gebruikt dan biologie, techniek en wiskunde in één opdracht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een klas wil een oplossing ontwerpen om een vijver gezonder te maken. Wat is de goede eerste stap?",
        opties=[
            "de huidige toestand meten, zodat je later kan vergelijken",
            "meteen een filter bouwen en die in de vijver zetten",
            "de mooiste oplossing kiezen en die uitwerken",
            "wachten tot de vijver van zelf verbetert",
        ],
        antwoord=0,
        uitleg="Zonder beginmeting weet je nooit of je oplossing werkte. Meten, ontwerpen, uitvoeren, opnieuw meten: dat is de cyclus.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat kan je met een lichtmicroscoop bekijken?",
        opties=[
            "cellen en hun grootste celonderdelen",
            "losse atomen van een element",
            "virussen tot in hun details",
            "moleculen van water en zout",
        ],
        antwoord=0,
        uitleg="Een lichtmicroscoop vergroot genoeg voor cellen, celkernen en chloroplasten. Voor virussen en moleculen is een elektronenmicroscoop nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe bereken je de totale vergroting van een lichtmicroscoop?",
        opties=[
            "de vergroting van het oculair maal die van het objectief",
            "de vergroting van het oculair plus die van het objectief",
            "de vergroting van het objectief gedeeld door die van het oculair",
            "altijd honderd keer, ongeacht de lenzen",
        ],
        antwoord=0,
        uitleg="Een oculair van tien keer met een objectief van veertig keer geeft vierhonderd keer. De twee lenzen werken na elkaar.",
    ),
    dict(
        type="invultekst",
        vraag="Je kijkt door een oculair van 10 keer met een objectief van 40 keer. Hoeveel keer is de totale vergroting?",
        antwoord=["400", "400 keer", "vierhonderd"],
        uitleg="Tien maal veertig is vierhonderd. Zo'n cel van twintig micrometer lijkt dan acht millimeter groot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom begin je bij een microscoop met het zwakste objectief?",
        opties=[
            "het beeldveld is dan het grootst, zodat je je voorwerp makkelijker vindt",
            "het sterkste objectief werkt enkel met gekleurde preparaten",
            "het zwakste objectief geeft het scherpste beeld",
            "anders breekt het objectief altijd",
        ],
        antwoord=0,
        uitleg="Bij een sterke vergroting zie je maar een heel klein stukje. Je zoekt dus eerst grof en schakelt daarna op.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe sterker de vergroting van een microscoop, hoe groter het stukje preparaat dat je in beeld krijgt.",
        antwoord=False,
        uitleg="Het is omgekeerd: bij een sterke vergroting zie je een veel kleiner stukje. Daarom verlies je je voorwerp bij het opschakelen zo makkelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom legt men een dekglaasje op een preparaat?",
        opties=[
            "om het preparaat vlak te houden en uitdrogen te voorkomen",
            "om het preparaat sterker te vergroten",
            "om het licht te kleuren",
            "om het objectief te beschermen tegen krassen",
        ],
        antwoord=0,
        uitleg="Het dekglaasje drukt het preparaat tot één laagje en houdt het vocht erin. Daardoor is er maar één scherptevlak.",
    ),
    dict(
        type="invultekst",
        vraag="Waarom gebruikt men een kleurstof bij het maken van een preparaat?",
        antwoord=["contrast", "meer contrast", "om contrast"],
        uitleg="Veel celonderdelen zijn doorzichtig. Een kleurstof zoals methyleenblauw of jood maakt bepaalde delen zichtbaar.",
    ),
    dict(
        type="waarofniet",
        vraag="Een preparaat met een luchtbel erin bekijk je best opnieuw, want zo'n bel lijkt op een cel.",
        antwoord=True,
        uitleg="Een luchtbel heeft een scherpe donkere rand en is rond. Wie dat voor een cel aanziet, meet en besluit verkeerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke veiligheidsregels gelden in een labo? Kruis alles aan wat juist is.",
        opties=[
            "een bril en handschoenen dragen waar nodig",
            "niet eten of drinken in het labo",
            "lange haren vastmaken bij het werken met een vlam",
            "zelf nieuwe stoffen mengen om te zien wat er gebeurt",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bescherming, geen voedsel en geen loshangende haren of kleren. Op eigen initiatief mengen hoort nooit bij een proef.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stof die je niet kan benoemen, laat je staan en je meldt het aan de leraar.",
        antwoord=True,
        uitleg="Een onbekende stof kan bijtend of brandbaar zijn. Je ruikt er niet aan en je probeert er niets mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zet je bij een grafiek op de horizontale as?",
        opties=[
            "de onafhankelijke variabele, die je zelf instelde",
            "de afhankelijke variabele, die je gemeten hebt",
            "altijd de tijd, ook als die niet gevarieerd werd",
            "de grootste van de twee getallen",
        ],
        antwoord=0,
        uitleg="Wat je instelt, komt op de horizontale as; wat je meet, op de verticale. Zo lees je het verband in de juiste richting.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort bij elke as van een grafiek? Kruis alles aan wat juist is.",
        opties=[
            "de naam van de grootheid",
            "de eenheid",
            "een schaal met getallen",
            "de hypothese van het onderzoek",
        ],
        antwoord=[0, 1, 2],
        uitleg="Zonder naam, eenheid en schaal kan niemand je grafiek lezen. De hypothese hoort in de tekst, niet op een as.",
    ),
    dict(
        type="waarofniet",
        vraag="Een staafdiagram past bij een grootheid die vloeiend verandert en een lijndiagram bij losse categorieën.",
        antwoord=False,
        uitleg="Het is net omgekeerd. Soorten vogels zijn categorieën, dus staven; een temperatuur die stijgt is vloeiend, dus een lijn.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een meetpunt dat sterk van de rest afwijkt?",
        antwoord=["uitschieter", "een uitschieter", "uitbijter"],
        uitleg="Een uitschieter kan een meetfout zijn of iets echt bijzonders. Je laat hem staan en je zegt erbij dat hij er is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet een blad en noteert 4. Waarom is dat onvoldoende?",
        opties=[
            "de eenheid ontbreekt bij het getal",
            "4 is een te klein getal voor een blad",
            "je mag enkel in gehele getallen noteren",
            "een lengte hoort niet in een tabel",
        ],
        antwoord=0,
        uitleg="Een getal zonder eenheid betekent niets. Noteer 4 cm, en zet de eenheid één keer bovenaan de kolom.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén enkele meting uit een reeks zegt meer over die reeks dan het gemiddelde ervan.",
        antwoord=False,
        uitleg="Het gemiddelde zegt meer, want het vlakt toevallige afwijkingen uit. Daarbij vermeld je best ook hoe sterk de metingen onderling verschilden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat maakt een wetenschappelijke uitspraak anders dan een los vermoeden?",
        opties=[
            "ze is getoetst en kan weerlegd worden",
            "ze komt van iemand met een diploma",
            "ze staat in een boek afgedrukt",
            "ze wordt door veel mensen geloofd",
        ],
        antwoord=0,
        uitleg="Niet wie het zegt is beslissend, maar of het getoetst is en of het weerlegd kan worden. Daardoor kan wetenschap zichzelf verbeteren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest op een website dat een plant beter groeit met muziek. Wat doe je als onderzoeker?",
        opties=[
            "je kijkt of er een proef met controlegroep achter zit",
            "je neemt het over, want het stond op een website",
            "je verwerpt het meteen zonder te kijken",
            "je vraagt wat de mening van je klas erover is",
        ],
        antwoord=0,
        uitleg="Je beoordeelt de opzet: hoeveel planten, welke controle, wie het onderzoek betaalde. Pas dan weet je wat de bewering waard is.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie een onderzoek financiert, kan een belang hebben bij de uitkomst, en dat hoort bij de beoordeling.",
        antwoord=True,
        uitleg="Een belang maakt een onderzoek niet automatisch fout, maar het is wel een reden om de opzet nauwer te bekijken. Daarom moet een financiering vermeld worden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee groepen in de klas doen dezelfde proef en komen tot een ander besluit. Wat doe je?",
        opties=[
            "de twee werkwijzen naast elkaar leggen en zoeken waar ze verschilden",
            "de groep met het mooiste verslag gelijk geven",
            "allebei de besluiten naast elkaar in het verslag zetten zonder uitleg",
            "de proef opgeven, want er is geen antwoord",
        ],
        antwoord=0,
        uitleg="Een verschil in uitkomst zit bijna altijd in een verschil in uitvoering. Dat opsporen is zelf een stuk wetenschap.",
    ),
]

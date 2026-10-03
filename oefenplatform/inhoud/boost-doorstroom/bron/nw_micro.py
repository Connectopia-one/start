# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Biodiversiteit en micro-organismen.

Biologie, de kop "Biodiversiteit en micro-organismen" van de vakfiche
natuurwetenschappen 2de graad doorstroom. Deel 1 gaat over de indeling van het
leven en over de bouw, de voortplanting en het metabolisme van bacteriën,
schimmels en virussen. Deel 2 gaat over wat micro-organismen voor ons en voor
de natuur betekenen, in het goede en in het slechte.

Het driedomeinensysteem, het vijfrijkensysteem, de tree of life en het
onderscheid prokaryoot tegenover eukaryoot staan alleen in de uitgebreide
fiche (moderne talen en Latijn). Ze zitten daarom samen vooraan in deel 1.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Uit welke drie domeinen bestaat het driedomeinensysteem?",
        opties=[
            "archaea, bacteriën en eukaryoten",
            "planten, dieren en schimmels",
            "bacteriën, virussen en schimmels",
            "prokaryoten, protisten en dieren",
        ],
        antwoord=0,
        uitleg="Het driedomeinensysteem deelt al het leven in drie grote takken in: de archaea, de bacteriën en de eukaryoten. Dat is de bovenste indeling van de tree of life.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rijken horen bij het vijfrijkensysteem? Kruis alles aan wat juist is.",
        opties=["het plantenrijk", "het dierenrijk", "het prokaryotenrijk", "het virusrijk"],
        antwoord=[0, 1, 2],
        uitleg="De vijf rijken zijn planten, dieren, schimmels, prokaryoten en protisten. Virussen staan in geen enkel rijk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een prokaryote cel heeft geen kernmembraan.",
        antwoord=True,
        uitleg="Bij een prokaryoot ligt het erfelijk materiaal vrij in de cel. Een eukaryoot heeft wel een kern met een membraan eromheen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staan virussen niet in de tree of life?",
        opties=[
            "ze hebben geen eigen stofwisseling en vermeerderen zich niet alleen",
            "ze zijn te klein om met een gewone lichtmicroscoop te kunnen bekijken",
            "ze zijn pas ontdekt nadat de hele indeling al vastgelegd was",
            "ze horen tegelijk bij de bacteriën en bij de schimmels thuis",
        ],
        antwoord=0,
        uitleg="Een virus is geen cel. Het heeft geen eigen metabolisme en kan zich alleen vermeerderen in een gastheercel, dus het past niet in een indeling van levende wezens.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een organisme waarvan de cel wél een echte kern met kernmembraan heeft?",
        antwoord="eukaryoot",
        uitleg="Planten, dieren, schimmels en protisten zijn eukaryoot. Bacteriën en archaea zijn prokaryoot.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaruit bestaat een virus in zijn eenvoudigste vorm?",
        opties=[
            "genetisch materiaal met een eiwitmantel eromheen",
            "een celmembraan met daarin organellen en een kern",
            "een celwand van cellulose met daarin een vacuole",
            "een draad van suikers met daaromheen een vetlaag",
        ],
        antwoord=0,
        uitleg="Een virus heeft geen celmembraan, geen organellen en geen vacuole. Het is erfelijk materiaal in een eiwitjas, soms met een vetlaagje eromheen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bacterie heeft een celwand.",
        antwoord=True,
        uitleg="Rond het celmembraan van een bacterie ligt een stevige celwand. Veel antibiotica grijpen juist daarop aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vermeerdert een bacterie zich?",
        opties=[
            "door celsplitsing, waarbij één cel in twee gelijke cellen deelt",
            "door knopvorming, waarbij een kleine uitstulping zich afsnoert",
            "door geslachtscellen te maken en die te laten versmelten",
            "door een gastheercel te gebruiken die al het werk doet",
        ],
        antwoord=0,
        uitleg="Bacteriën delen zich ongeslachtelijk door celsplitsing. Gisten doen aan knopvorming, en een virus heeft altijd een gastheercel nodig.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de deling waarbij een gistcel een kleine uitstulping vormt die daarna loskomt?",
        antwoord="knopvorming",
        uitleg="Bij knopvorming ontstaat er een ongelijke deling: een kleine dochtercel groeit uit de moedercel en snoert zich af.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat een organisme anaëroob leeft?",
        opties=[
            "het kan leven zonder zuurstofgas",
            "het heeft juist veel zuurstofgas nodig",
            "het maakt zijn eigen voedsel uit licht",
            "het leeft uitsluitend in heel koud water",
        ],
        antwoord=0,
        uitleg="Anaëroob betekent zonder zuurstofgas. Aërobe organismen hebben zuurstofgas net wel nodig voor hun celademhaling.",
    ),
    dict(
        type="waarofniet",
        vraag="Een autotroof organisme haalt zijn energierijke stoffen uit andere organismen.",
        antwoord=False,
        uitleg="Net omgekeerd: een autotroof maakt die stoffen zelf, bijvoorbeeld met fotosynthese. Een heterotroof is het die van andere organismen moet leven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke organismen horen bij de micro-organismen? Kruis alles aan wat juist is.",
        opties=["bacteriën", "gisten en schimmels", "protozoa en eencellige algen", "mossen"],
        antwoord=[0, 1, 2],
        uitleg="Bacteriën, gisten en schimmels, protozoa en eencellige algen zijn micro-organismen. Mossen zijn gewone, met het blote oog zichtbare planten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bacterie vormt een spore. Waarom doet ze dat?",
        opties=[
            "om een periode met slechte omstandigheden te overleven",
            "om zich sneller te kunnen verplaatsen door een vloeistof",
            "om haar erfelijk materiaal met een andere bacterie te delen",
            "om meteen veel dochtercellen tegelijk te kunnen maken",
        ],
        antwoord=0,
        uitleg="Een spore is een rustvorm met een harde wand. Droogte, hitte of gebrek aan voedsel overleeft ze zo, tot het weer beter gaat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een bacteriekweek groeit vanaf het begin even snel en blijft dat doen zolang er voedsel is.",
        antwoord=False,
        uitleg="Een kweek doorloopt groeifasen. Eerst is er een aanloopfase, dan een fase van snelle groei, daarna een stilstand en ten slotte een afname.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke groeivoorwaarden heeft een bacterie nodig?",
        opties=[
            "voedsel, vocht en een geschikte temperatuur",
            "licht, zuurstofgas en een lage temperatuur",
            "droogte, zout en een hoge zuurtegraad",
            "kou, duisternis en zuiver gedestilleerd water",
        ],
        antwoord=0,
        uitleg="Voedingsstoffen, water en warmte laten bacteriën snel groeien. Bewaringstechnieken halen net een van die voorwaarden weg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe vermeerdert een virus zich?",
        opties=[
            "het laat een gastheercel nieuwe virusdeeltjes maken",
            "het deelt zich net als een bacterie door celsplitsing",
            "het vormt knoppen die als nieuwe virussen loskomen",
            "het maakt geslachtscellen die later samensmelten",
        ],
        antwoord=0,
        uitleg="Een virus heeft geen eigen machinerie. Het sluist zijn erfelijk materiaal binnen en laat de gastheercel de nieuwe deeltjes in elkaar zetten.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de eiwitjas rond het erfelijk materiaal van een virus?",
        antwoord="eiwitmantel",
        uitleg="De eiwitmantel beschermt het erfelijk materiaal en helpt het virus zich aan de juiste gastheercel vast te hechten.",
    ),
    dict(
        type="waarofniet",
        vraag="Schimmels zijn eukaryoot.",
        antwoord=True,
        uitleg="Schimmelcellen hebben een echte kern en organellen. Ze horen daarom bij het domein van de eukaryoten en vormen een eigen rijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je krijgt een organisme te zien dat eencellig is, geen kernmembraan heeft en zich door celsplitsing vermeerdert. Waar hoort het thuis?",
        opties=[
            "bij de prokaryoten",
            "bij de protisten",
            "bij de schimmels",
            "bij de virussen",
        ],
        antwoord=0,
        uitleg="Geen kernmembraan betekent prokaryoot. Protisten en schimmels zijn eukaryoot, en een virus is geen cel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een indeling als het driedomeinensysteem nuttig?",
        opties=[
            "ze toont hoe soorten met elkaar verwant zijn",
            "ze zegt welke soorten de mens nuttig vindt",
            "ze telt hoeveel soorten er op aarde leven",
            "ze bepaalt welke soorten beschermd moeten worden",
        ],
        antwoord=0,
        uitleg="Een indeling in domeinen en rijken brengt de verwantschap in beeld. Hoe dichter twee groepen bij elkaar staan, hoe meer bouw en erfelijk materiaal ze delen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welk micro-organisme laat brood rijzen?",
        opties=["bakkersgist", "een melkzuurbacterie", "een azijnzuurbacterie", "een schimmel op kaas"],
        antwoord=0,
        uitleg="Bakkersgist zet suikers om en maakt daarbij koolstofdioxide. Die gasbelletjes doen het deeg rijzen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Bij welke voedingsmiddelen spelen micro-organismen een rol? Kruis alles aan wat juist is.",
        opties=["yoghurt", "zuurkool", "schimmelkaas", "gekookt water"],
        antwoord=[0, 1, 2],
        uitleg="Yoghurt en zuurkool danken hun zure smaak aan melkzuurbacteriën, en schimmelkaas aan een schimmel. In gekookt water zit juist zo min mogelijk leven.",
    ),
    dict(
        type="waarofniet",
        vraag="Melkzuurbacteriën maken melk zuur en dik, en zo ontstaat yoghurt.",
        antwoord=True,
        uitleg="Ze zetten de melksuiker om in melkzuur. Door die verzuring klonteren de eiwitten samen en wordt de melk dik.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er bij pasteuriseren?",
        opties=[
            "het product wordt kort verhit zodat de meeste micro-organismen sterven",
            "het product wordt volledig steriel gemaakt en kan jaren blijven staan",
            "het product wordt ingevroren zodat de groei helemaal stilvalt",
            "het product wordt in zout gelegd zodat het water eruit trekt",
        ],
        antwoord=0,
        uitleg="Pasteuriseren doodt niet alles; het verlengt alleen de houdbaarheid. Steriliseren gaat verder en doodt ook sporen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke bewaringstechniek haalt het water uit een product zodat micro-organismen niet meer kunnen groeien?",
        antwoord="drogen",
        uitleg="Zonder vocht groeit er niets. Daarom blijven gedroogde kruiden, pasta en melkpoeder zo lang goed.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom werkt een antibioticum niet tegen griep?",
        opties=[
            "griep wordt veroorzaakt door een virus, en een antibioticum werkt op bacteriën",
            "griep wordt veroorzaakt door een schimmel, en die is te klein voor een antibioticum",
            "een antibioticum werkt alleen bij kinderen en niet bij volwassenen",
            "een antibioticum werkt pas nadat de koorts volledig weg is",
        ],
        antwoord=0,
        uitleg="Antibiotica grijpen aan op structuren van bacteriën, zoals de celwand. Een virus heeft die niet, dus er is niets om op aan te grijpen.",
    ),
    dict(
        type="waarofniet",
        vraag="Antibioticaresistentie ontstaat doordat bacteriën die het middel overleven zich verder vermenigvuldigen.",
        antwoord=True,
        uitleg="Wie overleeft, geeft zijn eigenschappen door. Hoe vaker en hoe slordiger antibiotica gebruikt worden, hoe sneller resistente stammen de bovenhand krijgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet een vaccin?",
        opties=[
            "het laat het afweersysteem oefenen zodat je later sneller reageert",
            "het doodt alle ziekteverwekkers die op dat ogenblik in je lichaam zitten",
            "het vervangt de antibiotica die je anders zou moeten innemen",
            "het geeft je meteen koorts zodat de ziekteverwekker eraan sterft",
        ],
        antwoord=0,
        uitleg="Een vaccin bevat onschadelijk gemaakt materiaal van de ziekteverwekker. Het afweersysteem leert het herkennen en kan bij een echte infectie veel sneller ingrijpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke rollen spelen micro-organismen in de natuur? Kruis alles aan wat juist is.",
        opties=[
            "ze breken dood materiaal af bij het composteren",
            "ze zuiveren water in een waterzuiveringsinstallatie",
            "ze helpen planten aan stikstof via mycorrhiza",
            "ze maken met hun bladgroen zuurstof voor de hele bodem",
        ],
        antwoord=[0, 1, 2],
        uitleg="Composteren, waterzuivering en de samenwerking met plantenwortels zijn klassieke voorbeelden. Bladgroen hebben bacteriën en schimmels niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het geheel van micro-organismen dat in je darm leeft?",
        antwoord="darmmicrobioom",
        uitleg="Het darmmicrobioom helpt bij de vertering, maakt vitamines aan en houdt ziekteverwekkers op afstand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is eutrofiëring?",
        opties=[
            "water raakt overbemest, algen bloeien op en het zuurstofgehalte daalt",
            "water wordt zo zuiver dat er helemaal geen organisme meer in leven kan",
            "water verdampt zo snel dat alle zouten achterblijven in de droge bodem",
            "water bevriest zo diep dat de waterplanten op de bodem eronder afsterven",
        ],
        antwoord=0,
        uitleg="Te veel voedingsstoffen laten algen woekeren. Als die massaal afsterven, verbruiken de afbrekende bacteriën zo veel zuurstof dat vissen stikken.",
    ),
    dict(
        type="waarofniet",
        vraag="Probiotica zijn levende micro-organismen die je inneemt om je microbioom te ondersteunen.",
        antwoord=True,
        uitleg="Probiotica bevatten nuttige bacteriën. Prebiotica zijn geen organismen maar voedingsstoffen die de goede bacteriën helpen groeien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gist wordt gebruikt om bier te brouwen. Welke eigenschap maakt haar daarvoor geschikt?",
        opties=[
            "ze zet suikers zonder zuurstofgas om in alcohol en koolstofdioxide",
            "ze zet alcohol met behulp van zuurstofgas om in azijnzuur en water",
            "ze maakt melkzuur, waardoor de drank dik en behoorlijk zuur wordt",
            "ze maakt antibiotica, waardoor er niets anders meer in kan groeien",
        ],
        antwoord=0,
        uitleg="Dat anaërobe proces heet gisting. Azijnzuurbacteriën doen het omgekeerde en maken van alcohol juist azijn.",
    ),
    dict(
        type="waarofniet",
        vraag="Een schimmelinfectie behandel je met een antibioticum.",
        antwoord=False,
        uitleg="Tegen schimmels gebruik je een antimycoticum. Antibiotica werken op bacteriën.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom blijft ingemaakte groente in zuur of in zout zo lang goed?",
        opties=[
            "de meeste micro-organismen kunnen in die omstandigheden niet groeien",
            "het zuur en het zout voeden juist de nuttige bacteriën die bederf tegenhouden",
            "het zout verwarmt de groente zodat alle sporen doodgaan",
            "het zuur sluit de pot luchtdicht af zodat er niets meer bij kan",
        ],
        antwoord=0,
        uitleg="Een lage zuurtegraad of een hoog zoutgehalte maakt de omgeving onleefbaar voor de meeste bederfveroorzakers. Zo win je weken of maanden houdbaarheid.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over het huidmicrobioom zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "het bestaat uit micro-organismen die normaal op je huid leven",
            "het houdt ziekteverwekkers mee op afstand",
            "het hoort bij een gezonde huid",
            "het moet je zo volledig mogelijk wegwassen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De bewoners van je huid horen erbij en beschermen je. Alles wegboenen verzwakt die bescherming eerder dan dat het helpt.",
    ),
    dict(
        type="waarofniet",
        vraag="De zelfzuiverende capaciteit van een waterloop komt van de stroming, niet van micro-organismen.",
        antwoord=False,
        uitleg="Het zijn juist bacteriën die het organische afval in het water afbreken. Zolang de vuilvracht niet te groot is, maakt een beek zichzelf zo weer schoon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een microbioomtransplantatie?",
        opties=[
            "darmbacteriën van een gezonde donor overbrengen naar een patiënt",
            "een heel orgaan van een gezonde donor overbrengen naar een patiënt",
            "een vaccin inspuiten dat uit gedode darmbacteriën gemaakt is",
            "alle darmbacteriën van een patiënt met antibiotica doden",
        ],
        antwoord=0,
        uitleg="Bij sommige hardnekkige darminfecties herstelt een gezond microbioom van een donor het evenwicht waar antibiotica tekortschieten.",
    ),
    dict(
        type="invultekst",
        vraag="Welk middel gebruik je tegen een infectie door een schimmel?",
        antwoord="antimycoticum",
        uitleg="Een antimycoticum remt schimmels af of doodt ze. Tegen bacteriën gebruik je een antibioticum.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zijn hygiënemaatregelen zoals handen wassen zo doeltreffend?",
        opties=[
            "ze onderbreken de weg waarlangs ziekteverwekkers zich verspreiden",
            "ze doden in één beweging alle bacteriën op en in het lichaam",
            "ze maken het lichaam voorgoed immuun voor elke nieuwe infectie",
            "ze vervangen een vaccinatie volledig bij wie verder gezond is",
        ],
        antwoord=0,
        uitleg="Een ziekteverwekker moet van de ene gastheer naar de andere raken. Breek je die weg, dan stopt de besmetting, hoe gevaarlijk de kiem ook is.",
    ),
]

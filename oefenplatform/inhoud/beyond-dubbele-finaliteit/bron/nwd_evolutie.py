# -*- coding: utf-8 -*-
"""🌍 Beyond dubbele finaliteit — Biologische evolutie.

Biologie, de onderkop "Biologische evolutie" van de kop "Ontstaan en evolutie
van soorten" uit de vakfiche natuurwetenschappen 3DU. Deel 1 gaat over wat
evolutie is en over de argumenten uit de anatomie, de embryologie en de
paleontologie. Deel 2 gaat over de argumenten uit de biochemie en de
moleculaire biologie, over het lezen van een verwantschapsdiagram, en over het
verschil tussen een wetenschappelijke verklaring en een levensbeschouwelijke.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat betekent biologische evolutie?",
        opties=[
            "soorten veranderen over vele generaties heen",
            "een individu past zich tijdens zijn leven aan",
            "soorten blijven altijd precies dezelfde",
            "een soort wordt in één generatie een andere",
        ],
        antwoord=0,
        uitleg="Evolutie speelt zich af op het niveau van de populatie, over generaties heen. Eén dier evolueert niet; de samenstelling van zijn soort doet dat wel.",
    ),
    dict(
        type="waarofniet",
        vraag="Evolutie gebeurt bij populaties, niet bij één individu.",
        antwoord=True,
        uitleg="Een individu heeft zijn genen bij de geboorte gekregen en houdt die. Wat verandert, is hoe vaak bepaalde allelen in de hele populatie voorkomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn homologe organen?",
        opties=[
            "organen met dezelfde bouw maar een andere functie",
            "organen met dezelfde functie maar een andere bouw",
            "organen die bij geen enkel dier nog werken",
            "organen die alleen bij zoogdieren voorkomen",
        ],
        antwoord=0,
        uitleg="De voorpoot van een hond, de vleugel van een vleermuis en de arm van een mens hebben dezelfde botten in dezelfde volgorde. Dat wijst op een gemeenschappelijke voorouder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn analoge organen?",
        opties=[
            "organen met dezelfde functie maar een andere bouw",
            "organen met dezelfde bouw maar een andere functie",
            "organen die bij de mens verdwenen zijn",
            "organen die bij alle soorten hetzelfde zijn",
        ],
        antwoord=0,
        uitleg="De vleugel van een insect en de vleugel van een vogel doen hetzelfde, maar zijn totaal anders gebouwd. Ze wijzen niet op verwantschap, wel op een gelijkaardig probleem dat apart is opgelost.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een orgaan dat bij een soort nog aanwezig is maar zijn functie verloren heeft?",
        antwoord=["rudimentair orgaan", "rudimentair", "een rudimentair orgaan"],
        uitleg="Een rudimentair kenmerk is een restant. De blindedarm bij de mens en de kleine heupbeentjes bij een walvis zijn bekende voorbeelden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke zijn rudimentaire kenmerken bij de mens? Er zijn er twee.",
        opties=[
            "het staartbeentje",
            "de spiertjes die de oorschelp bewegen",
            "de lens in het oog",
            "het middenrif onder de longen",
        ],
        antwoord=[0, 1],
        uitleg="Het staartbeentje is wat er van een staart overblijft, en de oorspiertjes bewegen bij ons nauwelijks nog. De lens en het middenrif doen juist voluit hun werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het argument uit de embryologie?",
        opties=[
            "embryo's van verwante soorten lijken sterk op elkaar",
            "embryo's groeien bij alle soorten even snel",
            "embryo's hebben allemaal dezelfde grootte",
            "embryo's van verwante soorten verschillen sterk",
        ],
        antwoord=0,
        uitleg="In een vroeg stadium zijn een visje, een kip en een mens moeilijk uit elkaar te houden; ze hebben zelfs kieuwbogen. Die gelijkenis wijst op een gemeenschappelijke bouwtekening.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de versteende resten of afdrukken van organismen uit het verleden?",
        antwoord=["fossielen", "fossiel", "een fossiel"],
        uitleg="Fossielen zijn het bewijsmateriaal van de paleontologie. Ze tonen welke soorten wanneer geleefd hebben en hoe ze eruitzagen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is Archaeopteryx een belangrijke vondst?",
        opties=[
            "hij heeft kenmerken van reptielen én van vogels",
            "hij is het oudste fossiel dat ooit gevonden is",
            "hij toont dat vogels niet geëvolueerd zijn",
            "hij is het enige fossiel met veren",
        ],
        antwoord=0,
        uitleg="Archaeopteryx had veren en vleugels, maar ook tanden, klauwen aan de vleugels en een benige staart. Zo'n tussenvorm verbindt twee groepen met elkaar.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een fossiel dat kenmerken van twee groepen combineert, zoals Archaeopteryx?",
        antwoord=["overgangsvorm", "een overgangsvorm", "tussenvorm"],
        uitleg="Een overgangsvorm laat zien hoe de ene groep stilaan in de andere overgaat. Zulke vondsten zijn sterke argumenten voor gemeenschappelijke afstamming.",
    ),
    dict(
        type="waarofniet",
        vraag="Fossielen in diepere aardlagen zijn meestal ouder dan die in hogere lagen.",
        antwoord=True,
        uitleg="Lagen stapelen zich van onder naar boven op. Daardoor zie je in een reeks lagen de volgorde waarin soorten verschenen en weer verdwenen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een evolutiereeks?",
        opties=[
            "een rij fossielen die de verandering van een soort toont",
            "een rij dieren die vandaag naast elkaar leven",
            "een rij organen met dezelfde functie",
            "een rij kruisingen in het labo",
        ],
        antwoord=0,
        uitleg="De reeks fossielen van het paard toont hoe het dier groter werd en hoe het aantal tenen daalde. Zo'n reeks laat de verandering stap voor stap zien.",
    ),
    dict(
        type="waarofniet",
        vraag="Van elke soort uit het verleden bestaat er een fossiel.",
        antwoord=False,
        uitleg="Fossiliseren is uitzonderlijk: meestal verteert alles. Daarom is het fossielenarchief onvolledig, en vullen anatomie en moleculaire biologie de gaten aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Uit welke vakgebieden komen argumenten voor evolutie? Er zijn er drie.",
        opties=[
            "de anatomie",
            "de paleontologie",
            "de moleculaire biologie",
            "de wiskundige statistiek alleen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De kracht van de evolutietheorie is juist dat verschillende vakgebieden tot dezelfde stamboom komen. Statistiek is een hulpmiddel, geen apart argument.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vullen de verschillende argumenten elkaar aan?",
        opties=[
            "los van elkaar wijzen ze op dezelfde verwantschap",
            "ze komen allemaal uit hetzelfde onderzoek",
            "ze zijn alle drie gebaseerd op fossielen",
            "ze zijn alleen geldig voor zoogdieren",
        ],
        antwoord=0,
        uitleg="Botten, embryo's, fossielen en DNA zijn onafhankelijke bronnen. Dat ze tot dezelfde boom leiden, maakt de verklaring sterk.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de soort waarvan twee huidige soorten allebei afstammen?",
        antwoord=["gemeenschappelijke voorouder", "voorouder", "de gemeenschappelijke voorouder"],
        uitleg="Op elk vertakkingspunt van de evolutieboom staat een gemeenschappelijke voorouder. Hoe recenter die splitsing, hoe nauwer de twee soorten verwant zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="De mens stamt af van de chimpansee zoals die vandaag leeft.",
        antwoord=False,
        uitleg="Mens en chimpansee hebben een gemeenschappelijke voorouder die miljoenen jaren geleden leefde. Ze zijn dus neven, niet ouder en kind.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een populatie?",
        opties=[
            "alle individuen van één soort in één gebied",
            "alle dieren die in één gebied leven",
            "alle soorten die met elkaar verwant zijn",
            "alle nakomelingen van één ouderpaar",
        ],
        antwoord=0,
        uitleg="Een populatie is de groep soortgenoten die samenleven en zich onderling kunnen voortplanten. Evolutie meet je aan de genen van zo'n groep.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met de oercel?",
        opties=[
            "de eerste cel waaruit al het leven zou zijn ontstaan",
            "de eerste cel van een nieuw embryo",
            "de grootste cel van een organisme",
            "de cel waarmee een bacterie zich deelt",
        ],
        antwoord=0,
        uitleg="Alle bekende organismen gebruiken hetzelfde DNA-alfabet en bijna dezelfde code. Dat wijst erop dat al het leven teruggaat op één gemeenschappelijke oorsprong.",
    ),
    dict(
        type="waarofniet",
        vraag="Evolutie heeft een vooraf bepaald doel waar ze naartoe werkt.",
        antwoord=False,
        uitleg="Evolutie werkt met wat er toevallig aan variatie is, en met wat in die omgeving toevallig voordeel geeft. Verandert de omgeving, dan verandert ook wat voordelig is.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welk argument komt uit de biochemie?",
        opties=[
            "alle organismen gebruiken dezelfde soort DNA-code",
            "alle organismen hebben een skelet van botten",
            "alle organismen ademen met longen",
            "alle organismen leven in dezelfde omgeving",
        ],
        antwoord=0,
        uitleg="Van bacterie tot mens wordt dezelfde genetische code gebruikt en komen dezelfde bouwstenen voor. Dat is moeilijk te verklaren zonder gemeenschappelijke afstamming.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zegt een groot verschil in DNA tussen twee soorten?",
        opties=[
            "hun gemeenschappelijke voorouder leefde lang geleden",
            "ze leven vandaag ver van elkaar op de wereldbol",
            "ze hebben een duidelijk verschillend aantal organen",
            "de ene soort is rechtstreeks uit de andere ontstaan",
        ],
        antwoord=0,
        uitleg="Hoe langer twee lijnen apart evolueren, hoe meer verschillen er zich in het DNA opstapelen. Het aantal verschillen werkt dus zowat als een klok.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe meer het DNA van twee soorten op elkaar lijkt, hoe nauwer ze verwant zijn.",
        antwoord=True,
        uitleg="Mens en chimpansee delen bijna al hun DNA, mens en gist veel minder. Die volgorde komt overeen met wat botten en fossielen aangeven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat lees je af van een verwantschapsdiagram?",
        opties=[
            "welke soorten een recentere voorouder delen",
            "welke soort het nuttigst is voor de mens",
            "welke soort het grootst geworden is",
            "in welk gebied elke soort vandaag leeft",
        ],
        antwoord=0,
        uitleg="Elke vertakking is een splitsing. Soorten die pas laat uit elkaar gaan, staan dicht bij elkaar in de boom en zijn dus nauw verwant.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het schema waarin soorten als takken van één boom getekend worden?",
        antwoord=["evolutieboom", "verwantschapsdiagram", "stamboom"],
        uitleg="Een evolutieboom of verwantschapsdiagram zet de splitsingen in de tijd. De stam onderaan is de oudste gemeenschappelijke voorouder.",
    ),
    dict(
        type="waarofniet",
        vraag="In een evolutieboom staan de soorten die het hoogst staan het verst in hun ontwikkeling.",
        antwoord=False,
        uitleg="Hoogte in de tekening zegt niets over beter of verder. Elke tak die vandaag bestaat, is even lang geëvolueerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee soorten splitsen pas heel recent af in de boom. Wat volgt daaruit?",
        opties=[
            "ze lijken genetisch sterk op elkaar",
            "ze leven zeker in hetzelfde gebied",
            "ze hebben evenveel nakomelingen",
            "ze kunnen zich nog met elkaar voortplanten",
        ],
        antwoord=0,
        uitleg="Weinig tijd apart betekent weinig opgestapelde verschillen in het DNA. Of ze zich nog kunnen kruisen, hangt af van de isolatie en volgt er niet vanzelf uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat maakt van de evolutietheorie een wetenschappelijke theorie?",
        opties=[
            "ze steunt op waarnemingen en kan getoetst worden",
            "ze wordt door zowat iedereen aanvaard",
            "ze staat in zowat alle handboeken biologie",
            "ze is sinds haar ontstaan nooit aangepast",
        ],
        antwoord=0,
        uitleg="Een wetenschappelijke theorie doet voorspellingen die je kan nagaan en bijstellen. Vond men een zoogdierfossiel tussen de oudste lagen, dan zou de theorie in de problemen komen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom worden creationisme en Intelligent Design niet als wetenschappelijke theorieën beschouwd?",
        opties=[
            "hun verklaring is niet met waarnemingen te toetsen",
            "ze worden door veel te weinig mensen gevolgd",
            "ze gaan over gebeurtenissen van heel lang geleden",
            "ze gebruiken geen enkel moeilijk vakwoord",
        ],
        antwoord=0,
        uitleg="Wetenschap werkt met uitspraken die je met waarnemingen kan weerleggen. Een verklaring die buiten dat bereik valt, kan oprecht geloofd worden, maar hoort bij levensbeschouwing en niet bij de natuurwetenschappen.",
    ),
    dict(
        type="waarofniet",
        vraag="De moderne evolutietheorie is sinds Darwin ongewijzigd gebleven.",
        antwoord=False,
        uitleg="Darwin kende genen en DNA nog niet. De erfelijkheidsleer en later de moleculaire biologie zijn erbij gekomen, en dat samen heet de moderne evolutietheorie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met de tree of life?",
        opties=[
            "het schema dat alle bekende soorten verbindt",
            "de oudste boom die ooit op aarde gevonden is",
            "de voedselketen van een bos in kaart gebracht",
            "het geheel van alle gevonden fossielen samen",
        ],
        antwoord=0,
        uitleg="De tree of life is de grote boom waarin bacteriën, planten, schimmels en dieren allemaal takken zijn. Zij vertrekt bij één gemeenschappelijke oorsprong.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gegevens gebruiken onderzoekers vandaag om een evolutieboom te maken? Er zijn er twee.",
        opties=[
            "de volgorde van de basen in het DNA",
            "de bouw van skeletten en organen",
            "het gewicht van de volwassen dieren",
            "de kleur van de vacht of de veren",
        ],
        antwoord=[0, 1],
        uitleg="DNA-volgordes en bouw zijn de twee stevigste bronnen. Gewicht en kleur veranderen te makkelijk en zeggen weinig over verwantschap.",
    ),
    dict(
        type="waarofniet",
        vraag="Het feit dat anatomie en DNA tot dezelfde stamboom leiden, maakt die stamboom betrouwbaarder.",
        antwoord=True,
        uitleg="Twee onafhankelijke methodes die hetzelfde antwoord geven, versterken elkaar. Juist dat maakt de verwantschapsbomen zo stevig onderbouwd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lijken de botten in de voorpoot van verschillende zoogdieren zo sterk op elkaar?",
        opties=[
            "ze komen van dezelfde voorouder",
            "ze worden op dezelfde manier gebruikt",
            "ze zijn allemaal even zwaar",
            "ze groeien in dezelfde omgeving",
        ],
        antwoord=0,
        uitleg="Opperarmbeen, ellepijp, spaakbeen en handwortelbeentjes zitten overal in dezelfde volgorde, of de poot nu graaft, zwemt of vliegt. Dat erfde elke soort van dezelfde voorouder.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de wetenschap die fossielen bestudeert?",
        antwoord=["paleontologie", "de paleontologie"],
        uitleg="De paleontologie onderzoekt resten van leven uit het verleden. Zij levert de tijdlijn waarop de andere argumenten passen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een walvis heeft kleine heupbeentjes die niets dragen. Wat besluit je daaruit? Er zijn er twee.",
        opties=[
            "zijn voorouders hadden achterpoten",
            "die beentjes zijn rudimentaire kenmerken",
            "hij kan vandaag nog op het land lopen",
            "hij is nauwer verwant aan de vissen dan aan ons",
        ],
        antwoord=[0, 1],
        uitleg="De beentjes dragen niets meer, dus zijn ze rudimentair, en ze wijzen erop dat de voorouders van de walvis achterpoten hadden en op het land leefden. Een walvis is een zoogdier en dus nauwer verwant aan ons dan aan de vissen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gemeenschappelijke voorouder is altijd een soort die vandaag nog leeft.",
        antwoord=False,
        uitleg="Meestal is die voorouder uitgestorven en kennen we hem hoogstens uit fossielen. De soorten die vandaag leven, staan allemaal aan het uiteinde van een tak.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe oud is de aarde volgens het huidige natuurwetenschappelijke onderzoek?",
        opties=[
            "ongeveer 4,6 miljard jaar",
            "ongeveer 4,6 miljoen jaar",
            "ongeveer 460 miljoen jaar",
            "ongeveer 46 miljard jaar",
        ],
        antwoord=0,
        uitleg="Die leeftijd volgt uit de radioactieve datering van gesteenten en meteorieten. Zo'n tijdspanne maakt trage evolutie ook mogelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is tijd zo belangrijk in de evolutietheorie?",
        opties=[
            "kleine veranderingen stapelen zich op over vele generaties",
            "soorten veranderen enkel in hun eerste duizend jaar",
            "elke generatie verandert zichtbaar van vorm en kleur",
            "zonder genoeg tijd blijven alle mutaties zonder effect",
        ],
        antwoord=0,
        uitleg="Per generatie is het verschil nauwelijks te zien. Over duizenden generaties worden die kleine stapjes samen een groot verschil.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle organismen gebruiken dezelfde vier basen in hun DNA.",
        antwoord=True,
        uitleg="A, C, G en T komen voor in bacteriën, planten, schimmels en dieren. Die gedeelde taal is een van de sterkste biochemische argumenten.",
    ),
]

# -*- coding: utf-8 -*-
"""Argumenten voor evolutie en de evolutietheorieën — 🌍 Beyond, biologie.

Deel 1 gaat over de argumenten waarop de moderne evolutietheorie steunt: uit
de anatomie, de embryologie, de paleontologie, de biochemie en de moleculaire
biologie, en uit de biogeografie. Deel 2 gaat over de theorieën zelf, van
Lamarck over Darwin naar de moderne evolutietheorie, en over variatie,
selectie en erfelijkheid als de drie dragende gedachten.

De fiche vraagt dat de leerling bij een gegeven voorbeeld uitlegt hoe het een
argument voor evolutie kan zijn. Daarom vertrekt de helft van de vragen in
deel 1 van een concreet geval en niet van de naam van het argument.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met biologische evolutie?",
        opties=[
            "de erfelijke eigenschappen van een populatie veranderen over de generaties",
            "een individu past zich tijdens zijn leven volledig aan zijn omgeving aan",
            "een soort wordt in de loop van zijn leven ingewikkelder",
            "een populatie groeit in aantal tot ze te groot wordt",
        ],
        antwoord=0,
        uitleg="Evolutie speelt zich af in een populatie, niet in één individu. Wat "
        "verandert, is hoe vaak bepaalde allelen voorkomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn homologe organen?",
        opties=[
            "organen met dezelfde bouw en een gemeenschappelijke oorsprong",
            "organen met dezelfde functie maar met een heel andere bouw",
            "organen die bij een soort geen functie meer hebben",
            "organen die alleen bij het embryo te zien zijn",
        ],
        antwoord=0,
        uitleg="De voorpoot van een hond, de vleugel van een vleermuis en de arm van een "
        "mens hebben dezelfde beenderen. Dat wijst op een gemeenschappelijke voorouder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zijn analoge organen?",
        opties=[
            "organen met dezelfde functie maar een andere bouw",
            "organen met dezelfde bouw en dezelfde oorsprong",
            "organen die bij de mens verdwenen zijn",
            "organen die alleen bij planten voorkomen",
        ],
        antwoord=0,
        uitleg="De vleugel van een insect en die van een vogel doen hetzelfde, maar zijn "
        "heel anders gebouwd. Analogie wijst dus niet op verwantschap.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een orgaan dat bij een soort geen functie meer heeft, zoals de staartbeentjes bij de mens?",
        antwoord=[
            "rudimentair orgaan",
            "rudimentair",
            "een rudimentair orgaan",
        ],
        uitleg="Rudimentaire kenmerken zijn overblijfsels van een orgaan dat bij de "
        "voorouders wel werkte. Ze zijn moeilijk te verklaren zonder evolutie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke argumenten voor evolutie komen uit de anatomie? Kruis alles aan wat juist is.",
        opties=[
            "homologe organen bij verschillende soorten",
            "rudimentaire organen zonder functie",
            "dezelfde volgorde van aminozuren in een eiwit",
            "de verspreiding van soorten over de continenten",
        ],
        antwoord=[0, 1],
        uitleg="Anatomie kijkt naar de bouw van het lichaam. Eiwitten horen bij de "
        "biochemie en de verspreiding bij de biogeografie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het op elkaar lijken van embryo's een argument voor evolutie?",
        opties=[
            "verwante soorten doorlopen een gelijkaardige ontwikkeling",
            "alle embryo's zijn even groot bij de geboorte",
            "embryo's leven altijd in precies hetzelfde milieu als elkaar",
            "embryo's hebben geen DNA van hun ouders",
        ],
        antwoord=0,
        uitleg="Een vis-, een kip- en een mensenembryo hebben alle kieuwbogen. Die "
        "gemeenschappelijke bouwplannen wijzen op een gemeenschappelijke oorsprong.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de resten of sporen van organismen die bewaard bleven in de gesteentelagen?",
        antwoord=["fossielen", "fossiel", "een fossiel"],
        uitleg="Fossielen laten zien welke soorten er wanneer leefden. Hoe dieper de laag, "
        "hoe ouder de vondst.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat maakt Archaeopteryx zo belangrijk? Kruis alles aan wat juist is.",
        opties=[
            "hij had veren, zoals een vogel",
            "hij had tanden en een benige staart, zoals een reptiel",
            "hij is het oudste fossiel dat ooit gevonden is",
            "hij leeft vandaag nog in kleine aantallen",
        ],
        antwoord=[0, 1],
        uitleg="Omdat hij kenmerken van twee groepen draagt, heet zo'n vondst een "
        "overgangsfossiel. Hij is niet het oudste fossiel en hij is uitgestorven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een continue reeks van fossielen?",
        opties=[
            "een reeks vondsten die een soort stap voor stap ziet veranderen",
            "een reeks soorten die vandaag nog naast elkaar leven in één gebied",
            "een reeks lagen zonder enig fossiel erin",
            "een reeks vondsten uit dezelfde dag",
        ],
        antwoord=0,
        uitleg="Bij de paardachtigen is zo'n reeks goed bewaard: van een klein bosdier met "
        "meerdere tenen naar het paard met één hoef. Hetzelfde geldt voor de walvisachtigen.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe dieper een gesteentelaag ligt, hoe jonger de fossielen die erin zitten.",
        antwoord=False,
        uitleg="De lagen stapelen zich op, dus liggen de oudste onderaan. Daarom kan men "
        "aan de volgorde van de lagen de ouderdom aflezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het vergelijken van DNA een sterk argument voor evolutie?",
        opties=[
            "hoe verwanter twee soorten, hoe meer hun DNA gelijkt",
            "alle soorten hebben precies hetzelfde DNA",
            "DNA verandert bij elk individu tijdens zijn leven",
            "DNA zit alleen bij gewervelde dieren in de kern",
        ],
        antwoord=0,
        uitleg="Mens en chimpansee verschillen maar in enkele procenten van hun DNA. Hoe "
        "langer twee lijnen gescheiden zijn, hoe meer verschillen er opgestapeld zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat laat het vergelijken van aminozuursequenties zien?",
        opties=[
            "hetzelfde eiwit verschilt minder bij nauwe verwanten",
            "elk organisme gebruikt zijn eigen soort aminozuren",
            "eiwitten zijn bij alle soorten precies gelijk",
            "eiwitten veranderen bij elke maaltijd",
        ],
        antwoord=0,
        uitleg="Cytochroom c van een mens en van een aap verschilt in heel weinig "
        "aminozuren, dat van een gist in veel meer. Die graduele verschillen volgen de "
        "verwantschap.",
    ),
    dict(
        type="waarofniet",
        vraag="Alle bekende organismen gebruiken dezelfde genetische code.",
        antwoord=True,
        uitleg="Op enkele uitzonderingen na geldt dezelfde code van bacterie tot mens. Dat "
        "wijst erop dat alles teruggaat op een gemeenschappelijke oercel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke argumenten komen uit de moleculaire biologie? Kruis alles aan wat juist is.",
        opties=[
            "het vergelijken van DNA-sequenties",
            "de universele genetische code",
            "de ligging van de continenten",
            "het aantal tenen bij fossiele paarden",
        ],
        antwoord=[0, 1],
        uitleg="Moleculaire biologie werkt op het niveau van DNA en eiwitten. Continenten "
        "horen bij de biogeografie, fossiele paarden bij de paleontologie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lijken de buideldieren van Australië zo weinig op die van elders?",
        opties=[
            "Australië raakte vroeg van de andere continenten los",
            "buideldieren verplaatsen zich over de oceaan",
            "Australië heeft een ander soort zwaartekracht",
            "buideldieren hebben geen DNA van hun voorouders",
        ],
        antwoord=0,
        uitleg="Door de continentendrift evolueerde de fauna daar apart verder. Dat soort "
        "verspreidingspatronen is het argument uit de biogeografie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het traag uit elkaar schuiven van de continenten?",
        antwoord=["continentendrift", "de continentendrift", "continentdrift"],
        uitleg="Soorten die samen op één landmassa leefden, raakten zo van elkaar "
        "gescheiden. Daarna evolueerden ze elk hun eigen kant op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gemeenschappelijke voorouder betekent dat de ene soort uit de andere ontstaan is.",
        antwoord=False,
        uitleg="Mens en chimpansee stammen allebei af van een derde, uitgestorven soort. De "
        "mens komt dus niet van de chimpansee.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men, met de Engelse term, de boom die de verwantschap tussen alle soorten voorstelt?",
        antwoord=["tree of life", "levensboom", "de levensboom"],
        uitleg="Elke splitsing in die boom is een gemeenschappelijke voorouder. De "
        "vertakkingen worden bepaald met fossielen én met DNA-vergelijkingen.",
    ),
    dict(
        type="waarofniet",
        vraag="De antibioticaresistentie van bacteriën is een voorbeeld van evolutie die vandaag te volgen is.",
        antwoord=True,
        uitleg="Bacteriën delen snel, dus gaat de verandering van allelfrequenties zichtbaar "
        "snel. Dat is evolutie in rechtstreekse waarneming.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een onderzoeker vindt in een oude laag een vis met pootachtige vinnen. Waarom is dat een argument voor evolutie?",
        opties=[
            "het is een overgangsvorm tussen twee groepen",
            "het bewijst dat vissen nooit veranderd zijn",
            "het toont aan dat de laag heel jong is",
            "het bewijst dat vissen en vogels verwant zijn",
        ],
        antwoord=0,
        uitleg="Zo'n vondst draagt kenmerken van vissen én van landdieren. Dat is net wat je "
        "verwacht als de ene groep uit de andere voortkomt.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat dacht Lamarck over het ontstaan van nieuwe kenmerken?",
        opties=[
            "wat een dier gebruikt groeit, en dat geeft het door",
            "wie het best aangepast is, krijgt meer nakomelingen",
            "nieuwe kenmerken ontstaan door toevallige mutaties",
            "soorten veranderen helemaal niet in de tijd",
        ],
        antwoord=0,
        uitleg="Lamarck geloofde in gebruik en onbruik van lichaamsdelen én in de "
        "erfelijkheid van verworven eigenschappen. Die tweede gedachte bleek fout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom klopt de erfelijkheid van verworven eigenschappen niet?",
        opties=[
            "wat je tijdens je leven verandert, zit niet in je gameten",
            "verworven eigenschappen bestaan niet",
            "alleen planten kunnen hun eigenschappen zomaar doorgeven",
            "gameten krijgen hun DNA pas na de geboorte",
        ],
        antwoord=0,
        uitleg="Een smid die sterke armen kweekt, verandert zijn spiercellen, niet zijn "
        "geslachtscellen. Alleen wat in de gameten zit, gaat naar het kind.",
    ),
    dict(
        type="invultekst",
        vraag="Welke bioloog beschreef de evolutie door natuurlijke selectie?",
        antwoord=["Darwin", "Charles Darwin", "darwin"],
        uitleg="Darwin zag dat er meer jongen geboren worden dan er kunnen overleven, en "
        "dat niet iedereen evenveel kans maakt. Dat noemde hij natuurlijke selectie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke drie gedachten dragen de theorie van Darwin?",
        opties=[
            "variatie, selectie en erfelijkheid",
            "mutatie, deling en groei",
            "isolatie, drift en migratie",
            "gebruik, onbruik en overerving",
        ],
        antwoord=0,
        uitleg="Er is verschil tussen individuen, niet iedereen plant zich even goed voort, "
        "en wat telt wordt doorgegeven. Samen geeft dat verandering over de generaties.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelde Darwin met survival of the fittest?",
        opties=[
            "wie het best past bij zijn omgeving krijgt meer nakomelingen",
            "wie het sterkste is wint altijd elk gevecht dat hij aangaat",
            "wie het langst leeft heeft de meeste jongen",
            "wie het grootst is overleeft als enige",
        ],
        antwoord=0,
        uitleg="Fit betekent passend, niet gespierd. Soms is onopvallend zijn of goed "
        "kunnen vluchten de beste aanpassing.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is er binnen een populatie altijd variatie? Kruis alles aan wat juist is.",
        opties=[
            "door mutaties in het DNA",
            "door mixing en crossing-over bij de meiose",
            "doordat elk dier zich tijdens zijn leven aanpast",
            "doordat elk dier hetzelfde eet",
        ],
        antwoord=[0, 1],
        uitleg="Mutaties leveren nieuwe allelen, de meiose en de bevruchting mengen ze "
        "telkens anders. Zonder die variatie valt er niets te selecteren.",
    ),
    dict(
        type="waarofniet",
        vraag="Zonder variatie tussen individuen kan er geen natuurlijke selectie plaatsvinden.",
        antwoord=True,
        uitleg="Als alle individuen gelijk zijn, maakt iedereen evenveel kans. Variatie is "
        "dus de grondstof van de evolutie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat voegt de moderne evolutietheorie toe aan het werk van Darwin? Kruis alles aan wat juist is.",
        opties=[
            "mutaties als bron van nieuwe allelen",
            "het rekenen met allelfrequenties in een populatie",
            "het begrip natuurlijke selectie",
            "het idee dat soorten in de tijd veranderen",
        ],
        antwoord=[0, 1],
        uitleg="Selectie en verandering in de tijd had Darwin zelf al. Wat hij niet kende, "
        "was de oorzaak van de variatie: mutaties en de genetica van Mendel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men een kenmerk waarmee een organisme beter bij zijn omgeving past?",
        antwoord=["adaptatie", "een adaptatie", "aanpassing"],
        uitleg="Een adaptatie ontstaat niet omdat een dier het wil, maar doordat wie ze "
        "toevallig heeft meer nakomelingen krijgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe verklaart de moderne theorie dat de peper-en-zoutvlinder donkerder werd?",
        opties=[
            "op roetzwarte bomen werden donkere vlinders minder opgegeten",
            "de vlinders werden zwart van het roet op hun vleugels",
            "de vlinders pasten hun kleur aan de bomen aan",
            "de lichte vlinders verhuisden naar een ander land zonder roet",
        ],
        antwoord=0,
        uitleg="Het donkere allel bestond al en was zeldzaam. Toen de bomen zwart werden, "
        "had het ineens een voordeel en nam het in de populatie toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen de verklaring van Lamarck en die van Darwin voor een lange giraffennek?",
        opties=[
            "bij Lamarck rekt het dier zijn nek, bij Darwin had het die al",
            "bij Darwin rekt het dier zijn nek tijdens zijn leven",
            "bij Lamarck telt alleen het toeval van de mutaties in het DNA",
            "de twee verklaringen komen op hetzelfde neer",
        ],
        antwoord=0,
        uitleg="Lamarck dacht dat het rekken zelf doorgegeven werd. Darwin zag dat er "
        "toevallig langere nekken bestonden en dat die dieren meer jongen kregen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een individu kan tijdens zijn leven evolueren.",
        antwoord=False,
        uitleg="Evolutie gebeurt in een populatie, over generaties heen. Eén individu kan "
        "zich wel aanpassen, maar zijn erfelijk materiaal verandert daar niet van.",
    ),
    dict(
        type="waarofniet",
        vraag="Een populatie zijn alle soorten die samen in hetzelfde gebied leven.",
        antwoord=False,
        uitleg="Een populatie zijn alle individuen van één soort in hetzelfde gebied. "
        "Binnen zo'n groep wordt er onderling voortgeplant, en daar verschuiven de "
        "allelfrequenties.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het aandeel van een bepaald allel in een populatie?",
        antwoord=["allelfrequentie", "de allelfrequentie", "allelfrequenties"],
        uitleg="Evolutie is in feite een verschuiving van allelfrequenties. Blijven die "
        "stabiel, dan evolueert de populatie niet.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de kracht waarmee de omgeving bepaalde kenmerken bevoordeelt?",
        antwoord=["selectiedruk", "de selectiedruk"],
        uitleg="Een roofdier, een ziekte of een antibioticum zet druk op de populatie. Hoe "
        "sterker die druk, hoe sneller de allelfrequenties verschuiven.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over mutaties en evolutie zijn juist? Kruis alles aan wat juist is.",
        opties=[
            "mutaties ontstaan toevallig, niet op bestelling",
            "de omgeving bepaalt welke mutaties een voordeel zijn",
            "een dier maakt de mutatie die het nodig heeft",
            "elke mutatie geeft een nieuwe soort",
        ],
        antwoord=[0, 1],
        uitleg="Een bacterie wordt niet resistent omdat er een antibioticum is. De "
        "resistente mutant bestond al en blijft als enige over.",
    ),
    dict(
        type="waarofniet",
        vraag="De moderne evolutietheorie verklaart de variatie met mutaties en herverdeling van allelen.",
        antwoord=True,
        uitleg="Mutaties maken nieuwe allelen, de meiose en de bevruchting mengen ze. Dat "
        "is precies het stuk dat Darwin nog niet kende.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom worden bacteriën die aan een antibioticum blootstaan vaak resistent?",
        opties=[
            "de resistente exemplaren overleven en planten zich voort",
            "de bacteriën leren het antibioticum te herkennen",
            "het antibioticum maakt de bacteriën resistent",
            "de bacteriën geven hun ervaring door aan hun jongen",
        ],
        antwoord=0,
        uitleg="Het antibioticum veroorzaakt de resistentie niet, het selecteert ze. Wie "
        "toevallig resistent was, heeft het veld voor zich alleen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is biodiversiteit?",
        opties=[
            "de verscheidenheid aan soorten, genen en ecosystemen",
            "het aantal individuen van één soort",
            "het aantal chromosomen van een soort",
            "de hoeveelheid planten in een gebied",
        ],
        antwoord=0,
        uitleg="Biodiversiteit gaat van genetische diversiteit binnen een soort tot de "
        "verscheidenheid aan ecosystemen. Verdwijnt ze, dan verdwijnt ook het materiaal "
        "waarmee soorten zich kunnen aanpassen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een populatie met weinig genetische diversiteit kwetsbaar?",
        opties=[
            "er is weinig variatie om op te selecteren bij verandering",
            "de dieren kunnen zich niet meer voortplanten",
            "de dieren krijgen meer mutaties dan normaal",
            "de dieren hebben minder chromosomen",
        ],
        antwoord=0,
        uitleg="Komt er een nieuwe ziekte, dan is de kans klein dat iemand toevallig "
        "weerstand heeft. Daarom is genetische diversiteit een vorm van verzekering.",
    ),
]

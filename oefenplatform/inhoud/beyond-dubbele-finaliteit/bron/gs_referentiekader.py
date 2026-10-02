# -*- coding: utf-8 -*-
"""Het historisch referentiekader: situeren in tijd, ruimte en domeinen.

Uit de bouwsteen "het historisch referentiekader" van de vakfiche geschiedenis,
3 dubbele finaliteit: de zeven periodes van het courante westerse
referentiekader, de structuurbegrippen rond tijd en rond ruimte, de vier
maatschappelijke domeinen, de scharnierpunten en de principes en beperkingen
van periodisering.

Dit onderdeel weegt 7,5 procent van het examen, maar het is het gereedschap
waarmee elk ander thema gelezen wordt: wie niet kan situeren, kan ook een bron
niet plaatsen.
"""

DEEL1 = [
    dict(
        type="invultekst",
        vraag="Hoeveel periodes telt het courante westerse historisch referentiekader?",
        antwoord=["7", "zeven"],
        uitleg="Prehistorie, het oude nabije oosten, de klassieke oudheid, de middeleeuwen, de vroegmoderne tijd, de moderne tijd en de hedendaagse tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke periode komt na de middeleeuwen?",
        opties=[
            "de vroegmoderne tijd",
            "de klassieke oudheid",
            "de hedendaagse tijd",
            "het oude nabije oosten",
        ],
        antwoord=0,
        uitleg="De volgorde is middeleeuwen, vroegmoderne tijd, moderne tijd, hedendaagse tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke periode komt het eerst?",
        opties=[
            "de prehistorie",
            "het oude nabije oosten",
            "de klassieke oudheid",
            "de middeleeuwen",
        ],
        antwoord=0,
        uitleg="De prehistorie is de tijd voor het schrift. Met het schrift begint het oude nabije oosten.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke periode situeer je de Reformatie?",
        opties=[
            "de vroegmoderne tijd",
            "de middeleeuwen",
            "de moderne tijd",
            "de klassieke oudheid",
        ],
        antwoord=0,
        uitleg="Luther treedt in 1517 op, en dat valt na de middeleeuwen en voor de moderne tijd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vier maatschappelijke domeinen gebruik je om te situeren?",
        opties=[
            "het culturele, het economische, het politieke en het sociale domein",
            "het militaire, het kerkelijke, het stedelijke en het landelijke domein",
            "het nationale, het Europese, het mondiale en het westerse domein",
            "het geschreven, het mondelinge, het materiële en het audiovisuele domein",
        ],
        antwoord=0,
        uitleg="Cultureel, economisch, politiek en sociaal. De laatste rij noemt soorten bronnen, niet domeinen.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welk maatschappelijk domein situeer je de invoering van het algemeen enkelvoudig stemrecht?",
        opties=[
            "het politieke domein",
            "het economische domein",
            "het culturele domein",
            "het sociale domein",
        ],
        antwoord=0,
        uitleg="Het gaat over de inrichting van het bestuur en over wie mag beslissen. Dat is politiek.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welk maatschappelijk domein situeer je de opkomst van de stoommachine in de fabrieken?",
        opties=[
            "het economische domein",
            "het politieke domein",
            "het culturele domein",
            "het sociale domein",
        ],
        antwoord=0,
        uitleg="Het gaat over produceren en over energie in bedrijven, en dus over de economie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zaken horen bij het sociale domein?",
        opties=[
            "de verhoudingen tussen bevolkingsgroepen",
            "de leef- en werkomstandigheden van arbeiders",
            "de verkiezing van een parlement door de burgers",
            "de bouw van een kathedraal in een stad",
        ],
        antwoord=[0, 1],
        uitleg="Het sociale domein gaat over groepen en hun onderlinge verhoudingen. Een verkiezing is politiek, een kathedraal cultureel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het structuurbegrip voor zaken die over een lange tijd hetzelfde blijven?",
        antwoord=["continuïteit", "continuiteit"],
        uitleg="Het tegenovergestelde is verandering. Een breuk is een heel plotse verandering.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verschil tussen een evolutie en een revolutie?",
        opties=[
            "een evolutie gaat traag, een revolutie gaat snel en ingrijpend",
            "een evolutie gaat over techniek, een revolutie over politiek",
            "een evolutie is gepland, een revolutie gebeurt per ongeluk",
            "een evolutie duurt een eeuw, een revolutie precies één jaar",
        ],
        antwoord=0,
        uitleg="Het gaat om het tempo en de diepgang van de verandering, niet om het onderwerp of om een vaste duur.",
    ),
    dict(
        type="waarofniet",
        vraag="De val van de Berlijnse Muur in 1989 wijst op verandering in de naoorlogse periode in Europa.",
        antwoord=True,
        uitleg="Het IJzeren Gordijn viel weg en de verhoudingen in Europa werden grondig anders. Dat is verandering, geen continuïteit.",
    ),
    dict(
        type="waarofniet",
        vraag="Gelijktijdigheid betekent dat twee gebeurtenissen in dezelfde periode op verschillende plaatsen voorkomen.",
        antwoord=True,
        uitleg="Ongelijktijdigheid is dan dat een ontwikkeling ergens al begonnen is terwijl ze elders nog niet op gang is.",
    ),
    dict(
        type="waarofniet",
        vraag="Een breuk en een continuïteit kunnen in dezelfde periode naast elkaar bestaan.",
        antwoord=True,
        uitleg="Het bestuur kan plots veranderen terwijl de manier van boeren op het platteland hetzelfde blijft.",
    ),
    dict(
        type="waarofniet",
        vraag="Tijdrekening en chronologie betekenen precies hetzelfde.",
        antwoord=False,
        uitleg="Een tijdrekening is het stelsel waarmee je jaren nummert. Chronologie is de ordening van gebeurtenissen in de tijd.",
    ),
    dict(
        type="waarofniet",
        vraag="De industriële revolutie begon overal in Europa op hetzelfde moment.",
        antwoord=False,
        uitleg="Dat is een voorbeeld van ongelijktijdigheid: ze begint in Engeland, daarna in België, en pas veel later elders.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een gebeurtenis of evolutie die de overgang vormt tussen twee historische periodes?",
        antwoord=["een scharnierpunt", "scharnierpunt"],
        uitleg="De Franse Revolutie en het einde van de Tweede Wereldoorlog zijn zulke scharnierpunten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom laat het einde van de Tweede Wereldoorlog een nieuwe historische periode beginnen?",
        opties=[
            "de machtsverhoudingen in de wereld werden grondig anders",
            "er werd op die dag een nieuwe tijdrekening ingevoerd",
            "de oorlog eindigde precies op een rond jaartal",
            "historici hadden daar al in 1900 over beslist",
        ],
        antwoord=0,
        uitleg="Europa verdween uit het centrum, twee supermachten namen het over, en er kwam een hele nieuwe internationale orde.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke ruimte situeer je de Franse Revolutie het best?",
        opties=[
            "West-Europees, met een mondiale uitstraling",
            "mondiaal, want ze gebeurde op alle continenten",
            "niet-westers, buiten Europa",
            "maritiem, vooral op zee",
        ],
        antwoord=0,
        uitleg="Ze speelt zich af in Frankrijk, dus West-Europees, maar haar ideeën reikten veel verder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke structuurbegrippen gebruik je om een gebeurtenis in de ruimte te situeren?",
        opties=[
            "stedelijk en ruraal",
            "continentaal en maritiem",
            "evolutie en revolutie",
            "chronologie en tijdrekening",
        ],
        antwoord=[0, 1],
        uitleg="Evolutie, revolutie, chronologie en tijdrekening horen bij tijd, niet bij ruimte.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je met één woord een gebied buiten de steden, op het platteland?",
        antwoord=["ruraal", "landelijk"],
        uitleg="Het tegenovergestelde is stedelijk. Beide woorden zijn structuurbegrippen rond ruimte.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke periode komt na de moderne tijd?",
        opties=[
            "de hedendaagse tijd",
            "de vroegmoderne tijd",
            "de middeleeuwen",
            "de klassieke oudheid",
        ],
        antwoord=0,
        uitleg="De hedendaagse tijd is de laatste van de zeven en loopt tot vandaag.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een periodisering?",
        opties=[
            "een indeling van het verleden in periodes, achteraf gemaakt",
            "een lijst met alle jaartallen uit één bepaalde eeuw",
            "een kaart met de grenzen van een land op één moment",
            "de volledige verzameling bronnen over één gebeurtenis",
        ],
        antwoord=0,
        uitleg="Niemand beleefde de middeleeuwen als de middeleeuwen; die naam en die grenzen kwamen er later bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken horen bij de principes van periodisering?",
        opties=[
            "een periode wordt afgebakend op basis van een selectie van kenmerken en gebeurtenissen",
            "een periode krijgt een symbolische begin- en einddatum",
            "een periode is een constructie die achteraf gemaakt wordt",
            "een periode duurt in elke beschaving precies even lang",
        ],
        antwoord=[0, 1, 2],
        uitleg="De laatste optie klopt niet: periodes verschillen sterk in lengte, en elders ligt de indeling anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het dat een begin- en einddatum van een periode symbolisch is?",
        opties=[
            "de datum staat voor een verandering die veel langer duurde",
            "de datum is verzonnen en er gebeurde toen helemaal niets",
            "de datum staat in geen enkele bewaarde bron vermeld",
            "de datum verandert met elke nieuwe studie",
        ],
        antwoord=0,
        uitleg="1492 of 1789 zijn handige markeringen, maar de verandering waar ze voor staan ging over tientallen jaren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke beperking heeft de keuze voor het Congres van Wenen als scharnierpunt tussen de vroegmoderne en de moderne tijd?",
        opties=[
            "het is een westers en vooral politiek ijkpunt, dat elders weinig betekent",
            "het congres heeft volgens recent onderzoek nooit plaatsgevonden",
            "er zijn van het congres geen betrouwbare bronnen bewaard gebleven",
            "het congres duurde te kort om in Europa iets wezenlijk te veranderen",
        ],
        antwoord=0,
        uitleg="Voor China of Afrika zegt 1815 niets, en in het economische of culturele domein lag het keerpunt elders.",
    ),
    dict(
        type="waarofniet",
        vraag="De westerse periodisering in zeven periodes past even goed op de geschiedenis van China.",
        antwoord=False,
        uitleg="China wordt vaak per dynastie ingedeeld. De westerse scharnierpunten vallen daar niet samen met een breuk.",
    ),
    dict(
        type="waarofniet",
        vraag="Een periodisering is nooit volledig neutraal, want ze hangt af van welke kenmerken je kiest.",
        antwoord=True,
        uitleg="Kies je het bestuur, dan krijg je andere grenzen dan wanneer je de techniek of de kunst kiest.",
    ),
    dict(
        type="waarofniet",
        vraag="Een periodisering met politieke scharnierpunten geeft dezelfde grenzen als een periodisering met economische scharnierpunten.",
        antwoord=False,
        uitleg="Dat is precies een van de beperkingen: welke kenmerken je selecteert, bepaalt waar de grens ligt.",
    ),
    dict(
        type="waarofniet",
        vraag="Je kan dezelfde gebeurtenis in meer dan één maatschappelijk domein situeren.",
        antwoord=True,
        uitleg="De afschaffing van de kinderarbeid is sociaal én politiek: het raakt de arbeiders en het is een wet.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gebeurtenis die je mondiaal situeert, raakt per definitie heel Europa niet.",
        antwoord=False,
        uitleg="Mondiaal betekent wereldwijd, en Europa hoort daarbij. Het is geen tegenstelling met Europees maar een ruimere schaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je leest in bronnen dat Wilhelm II een vloot bouwt en kolonies zoekt in Afrika en Azië. Op welk niveau situeer je zijn ambities?",
        opties=[
            "mondiaal",
            "stedelijk",
            "ruraal",
            "uitsluitend West-Europees",
        ],
        antwoord=0,
        uitleg="Wie overzee kolonies wil en een vloot bouwt, kijkt verder dan Europa. Dat is een mondiale ambitie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom situeer je de eerste industriële revolutie in de regio's met steenkool en ijzererts?",
        opties=[
            "steenkool en ijzererts waren nodig voor stoom en staal",
            "daar woonden de rijkste fabrikanten van het land",
            "daar lag in elk land ook de hoofdstad van het bestuur",
            "daar was het klimaat het warmst en het droogst",
        ],
        antwoord=0,
        uitleg="Steenkool leverde de energie, ijzererts het metaal. Transport was duur, dus de industrie kwam naar de grondstof.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het structuurbegrip niet-westers?",
        opties=[
            "samenlevingen buiten Europa en de westerse wereld",
            "alle samenlevingen die geen steden gebouwd hebben",
            "alle samenlevingen uit de prehistorie en de oudheid",
            "alle samenlevingen die aan een zee of oceaan liggen",
        ],
        antwoord=0,
        uitleg="Westers verwijst naar Europa en bijvoorbeeld de Verenigde Staten; niet-westers naar de rest van de wereld.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het structuurbegrip voor een plotse, diepe verandering op korte tijd?",
        antwoord=["een breuk", "breuk", "revolutie"],
        uitleg="Een breuk of een revolutie staat tegenover een trage evolutie en tegenover continuïteit.",
    ),
    dict(
        type="invultekst",
        vraag="Welk maatschappelijk domein onderzoek je als je naar handel, productie en werk kijkt?",
        antwoord=["het economische domein", "economisch", "economische"],
        uitleg="Handel, productie, grondstoffen en werk horen bij de economie.",
    ),
    dict(
        type="invultekst",
        vraag="Welk maatschappelijk domein onderzoek je als je naar kunst, religie en onderwijs kijkt?",
        antwoord=["het culturele domein", "cultureel", "culturele"],
        uitleg="Kunst, geloof, taal, onderwijs en vermaak horen bij het culturele domein.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een tijdlijn zet 1517, 1789, 1815 en 1945 naast elkaar. Welke van die jaartallen gebruikt men als scharnierpunt tussen periodes?",
        opties=[
            "1789 of 1815, aan het begin van de moderne tijd",
            "1945, aan het begin van de hedendaagse tijd",
            "1517, want toen begon de hedendaagse tijd",
            "geen enkel, want scharnierpunten hebben geen jaartal",
        ],
        antwoord=[0, 1],
        uitleg="1517 hoort in de vroegmoderne tijd en begint geen nieuwe periode. Scharnierpunten krijgen wel een symbolisch jaartal.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke maatschappelijke domeinen situeer je een wet die kinderarbeid verbiedt?",
        opties=[
            "het sociale domein, want het raakt de arbeidersgezinnen",
            "het politieke domein, want het is een beslissing van de staat",
            "het culturele domein, want het gaat over kunst en geloof",
            "geen enkel domein, want een wet staat erbuiten",
        ],
        antwoord=[0, 1],
        uitleg="Veel gebeurtenissen horen in meer dan één domein. Dat de domeinen samenhangen, is net de reden: een economische verandering brengt sociale en politieke eisen mee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je moet een gebeurtenis situeren in tijd, ruimte en domein. Wat lever je dan af?",
        opties=[
            "wanneer, waar en op welk terrein het speelde",
            "alleen het juiste jaartal van de gebeurtenis",
            "een lijst van alle mensen die erbij aanwezig waren",
            "een beoordeling of het goed of slecht geweest is",
        ],
        antwoord=0,
        uitleg="Situeren is drie dingen tegelijk: de periode of het jaartal, de plaats of de schaal, en het domein.",
    ),
    dict(
        type="waarofniet",
        vraag="Het historisch referentiekader is een hulpmiddel om nieuwe informatie een plaats te geven.",
        antwoord=True,
        uitleg="Wie de periodes, de schalen en de domeinen kent, kan een bron of een gebeurtenis meteen ergens hangen.",
    ),
]

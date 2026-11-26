# -*- coding: utf-8 -*-
"""Inhoud, functies en context van een kunstuiting.

Tweede thema kunstbeschouwing (fiche 3DDO). De fiche vraagt:

    de inhoud van een kunstuiting: het onderwerp en de functies
        (decoratief, economisch, filosofisch, maatschappijkritisch, narratief,
        ontspannend, politiek)
    de context: tijd, ruimte, de politieke, sociale en culturele context,
        de persoonlijke context van de kunstenaar

Deel 1 zijn het onderwerp en de zeven functies.
Deel 2 is de context.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Uit welke twee delen bestaat de inhoud van een kunstuiting?",
        opties=["het onderwerp", "de functies", "de bouwstenen", "de techniek"],
        antwoord=[0, 1],
        uitleg="De inhoud is wat er te zien of te horen is (onderwerp) en waarvoor het dient (functies). Bouwstenen en techniek zijn middelen van vormgeving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een rijk versierd tapijt hangt in een kasteelzaal, vooral om de ruimte mooier te maken. Welke functie staat voorop?",
        opties=["decoratieve functie", "narratieve functie", "politieke functie", "filosofische functie"],
        antwoord=0,
        uitleg="Decoratief betekent versierend: het werk maakt een ruimte of voorwerp mooier.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een reeks glasramen in een kerk vertelt stap voor stap het leven van een heilige. Welke functie staat voorop?",
        opties=["narratieve functie", "decoratieve functie", "economische functie", "ontspannende functie"],
        antwoord=0,
        uitleg="Narratief betekent verhalend. Het werk vertelt een verhaal.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een straatkunstenaar schildert een muurschildering die kritiek geeft op de manier waarop vluchtelingen behandeld worden. Welke functie staat voorop?",
        opties=["maatschappijkritische functie", "decoratieve functie", "ontspannende functie", "economische functie"],
        antwoord=0,
        uitleg="Het werk zet de kijker aan het denken over een probleem in de samenleving. Dat is maatschappijkritisch.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vorst laat zichzelf afbeelden in een groot ruiterstandbeeld op het plein, om zijn macht te tonen. Welke functie staat voorop?",
        opties=["politieke functie", "narratieve functie", "filosofische functie", "decoratieve functie"],
        antwoord=0,
        uitleg="Kunst die macht toont of een machthebber verheerlijkt, heeft een politieke functie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een schilderij van een schedel naast een kaars die opbrandt, laat de kijker nadenken over de vergankelijkheid van het leven. Welke functie staat voorop?",
        opties=["filosofische functie", "economische functie", "politieke functie", "ontspannende functie"],
        antwoord=0,
        uitleg="Het werk zet aan tot nadenken over grote levensvragen. Dat is de filosofische functie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kunstenaar maakt honderd kleine prints van zijn bekendste werk om ze te verkopen. Welke functie staat voorop?",
        opties=["economische functie", "narratieve functie", "maatschappijkritische functie", "filosofische functie"],
        antwoord=0,
        uitleg="Kunst als handelswaar of bron van inkomen heeft een economische functie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een vrolijke komedie wil het publiek vooral een avond laten lachen. Welke functie staat voorop?",
        opties=["ontspannende functie", "filosofische functie", "politieke functie", "decoratieve functie"],
        antwoord=0,
        uitleg="Kunst die vooral amuseert en ontspant, heeft een ontspannende functie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn functies van kunst die je moet kennen?",
        opties=["narratief", "economisch", "ontspannend", "medisch"],
        antwoord=[0, 1, 2],
        uitleg="De zeven functies zijn decoratief, economisch, filosofisch, maatschappijkritisch, narratief, ontspannend en politiek. Medisch hoort er niet bij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het onderwerp van een kunstuiting?",
        opties=[
            "wat er afgebeeld, verteld of gebracht wordt, zoals een landschap of een liefdesverhaal",
            "de prijs waarvoor het werk op een veiling verkocht werd",
            "het materiaal waarmee de kunstenaar heeft gewerkt",
            "het museum waar het werk vandaag tentoongesteld wordt",
        ],
        antwoord=0,
        uitleg="Het onderwerp is waarover het werk gaat. Samen met de functies vormt het de inhoud.",
    ),
    dict(
        type="invultekst",
        vraag="Kunst die een verhaal vertelt, heeft een ... functie.",
        antwoord=["narratieve", "narratief"],
        uitleg="Narratief komt van het Latijnse narrare, vertellen.",
    ),
    dict(
        type="invultekst",
        vraag="Kunst die vooral een ruimte of een voorwerp mooier maakt, heeft een ... functie.",
        antwoord=["decoratieve", "decoratief"],
        uitleg="Decoratief betekent versierend.",
    ),
    dict(
        type="waarofniet",
        vraag="Een kunstwerk kan tegelijk meerdere functies hebben.",
        antwoord=True,
        uitleg="Een kerkraam kan tegelijk een verhaal vertellen, versieren en een geloofsboodschap brengen. Je zoekt dan welke functie voorop staat.",
    ),
    dict(
        type="waarofniet",
        vraag="Een werk met een politieke functie wil vooral een ruimte gezellig aankleden.",
        antwoord=False,
        uitleg="Dat is de decoratieve functie. Een politieke functie toont of steunt macht, of een politieke boodschap.",
    ),
    dict(
        type="waarofniet",
        vraag="Een affiche die de kijker oproept om tegen oorlog te protesteren, heeft een maatschappijkritische functie.",
        antwoord=True,
        uitleg="Het werk stelt een probleem in de samenleving aan de kaak.",
    ),
    dict(
        type="waarofniet",
        vraag="Het onderwerp van een kunstuiting is hetzelfde als de techniek waarmee het gemaakt is.",
        antwoord=False,
        uitleg="Het onderwerp hoort bij de inhoud, de techniek bij de middelen van vormgeving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een stripverhaal over een jongen die op avontuur gaat in de ruimte, wil vooral spannend vermaken. Welke twee functies passen het best?",
        opties=["narratieve functie", "ontspannende functie", "politieke functie", "economische functie"],
        antwoord=[0, 1],
        uitleg="Het vertelt een verhaal en wil vooral ontspannen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een regering bestelt een film die het eigen leger als heldhaftig toont, om de bevolking achter een oorlog te krijgen. Welke functie staat voorop?",
        opties=["politieke functie", "ontspannende functie", "decoratieve functie", "economische functie"],
        antwoord=0,
        uitleg="Kunst als propaganda heeft een politieke functie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een dichter schrijft over de vraag of de mens een vrije wil heeft. Welke functie staat voorop?",
        opties=["filosofische functie", "decoratieve functie", "economische functie", "politieke functie"],
        antwoord=0,
        uitleg="Het gedicht stelt een grote levensvraag. Dat is de filosofische functie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig om de functie van een kunstwerk te kennen?",
        opties=[
            "je begrijpt beter waarom het gemaakt werd en wat het wil bereiken",
            "dan weet je meteen hoeveel het werk vandaag op een veiling opbrengt",
            "dan hoef je niet meer naar de vorm en de kleuren te kijken",
            "dan weet je precies in welk jaar het werk gemaakt werd",
        ],
        antwoord=0,
        uitleg="De functie vertelt waarvoor het werk dient. Dat helpt om de keuzes van de kunstenaar te begrijpen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke elementen horen bij de context van een kunstuiting?",
        opties=["tijd", "ruimte", "de persoonlijke context van de kunstenaar", "de kleur van de lijst waarin het werk vandaag in het museum hangt"],
        antwoord=[0, 1, 2],
        uitleg="De context is tijd, ruimte, de politieke, sociale en culturele context en de persoonlijke context van de kunstenaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met de ruimte als deel van de context?",
        opties=[
            "de plaats of de streek waar en waarvoor het werk gemaakt werd",
            "de lege plekken die de schilder tussen de figuren op het doek liet",
            "de afmetingen van het doek in centimeter",
            "de zaal van het museum waarin je het werk vandaag gaat bekijken",
        ],
        antwoord=0,
        uitleg="Bij context gaat ruimte over waar een werk ontstond, bijvoorbeeld in Vlaanderen, Italië of Japan. Ruimte als bouwsteen bij beeld is iets anders.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een schilder maakte zijn donkerste werken in de jaren nadat zijn kind gestorven was. Welke context speelt hier?",
        opties=[
            "de persoonlijke context van de kunstenaar",
            "de politieke context van het land waarin hij woonde",
            "de ruimte waarvoor het werk gemaakt werd",
            "de economische functie van het schilderij",
        ],
        antwoord=0,
        uitleg="Wat de kunstenaar zelf meemaakte, is zijn persoonlijke context.",
    ),
    dict(
        type="meerkeuze",
        vraag="Tijdens een oorlog maken veel kunstenaars werken over geweld, angst en verwoesting. Welke context speelt hier vooral?",
        opties=[
            "de politieke en sociale context",
            "de persoonlijke context van één kunstenaar",
            "de decoratieve context van het werk",
            "de techniek die de kunstenaars gebruiken",
        ],
        antwoord=0,
        uitleg="Wat er in de samenleving en de politiek gebeurt, beïnvloedt de kunst. Dat is de politieke en sociale context.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom moet je de tijd kennen waarin een werk gemaakt werd?",
        opties=[
            "wat toen gewoon, nieuw of verboden was, verklaart veel keuzes van de kunstenaar",
            "omdat oude werken altijd mooier zijn dan nieuwe",
            "omdat de tijd alleen bepaalt hoeveel geld het werk vandaag op een veiling waard is",
            "omdat elk werk uit dezelfde tijd er precies hetzelfde uitziet, welke kunstenaar het ook maakte",
        ],
        antwoord=0,
        uitleg="Een werk dat vandaag gewoon lijkt, kon in zijn eigen tijd schokkend of vernieuwend zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een werk wordt gemaakt in een tijd waarin de kerk de grootste opdrachtgever is en bijna iedereen gelovig is. Welke context beschrijf je?",
        opties=[
            "de culturele en sociale context",
            "de persoonlijke context van de kunstenaar",
            "de ruimte waarin het werk vandaag hangt",
            "de narratieve functie van het werk",
        ],
        antwoord=0,
        uitleg="Welke waarden en instellingen in een samenleving belangrijk zijn, is de culturele en sociale context.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een Japanse prent uit de 19de eeuw wordt vergeleken met een Vlaams schilderij uit dezelfde eeuw. Welk element van de context verschilt vooral?",
        opties=["de ruimte", "de tijd", "de techniek", "de functie"],
        antwoord=0,
        uitleg="Ze komen uit dezelfde tijd, maar uit een andere plaats en cultuur.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vertelt de persoonlijke context niet altijd alles over een werk?",
        opties=[
            "een werk wordt ook gevormd door de tijd, de plaats en de samenleving rond de kunstenaar",
            "kunstenaars maken nooit iets over hun eigen leven",
            "de persoonlijke context bestaat enkel bij kunstenaars die vandaag nog leven en werken",
            "de persoonlijke context gaat enkel over het geld en de schulden van de kunstenaar, verder niets",
        ],
        antwoord=0,
        uitleg="Je bekijkt de context best breed: persoonlijk, maar ook tijd, ruimte en samenleving.",
    ),
    dict(
        type="invultekst",
        vraag="Wat de kunstenaar zelf meemaakte, zoals een ziekte of een verhuis, hoort bij de ... context.",
        antwoord=["persoonlijke", "persoonlijk"],
        uitleg="De persoonlijke context is een van de vier elementen van de context.",
    ),
    dict(
        type="invultekst",
        vraag="De tijd, de ruimte, de samenleving en het leven van de kunstenaar vormen samen de ... van een kunstuiting.",
        antwoord=["context"],
        uitleg="De context vertelt in welke omstandigheden een werk ontstond.",
    ),
    dict(
        type="waarofniet",
        vraag="De politieke context kan bepalen wat een kunstenaar wel en niet mag tonen.",
        antwoord=True,
        uitleg="In een dictatuur kan kunst gecensureerd worden, of juist ingezet als propaganda.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee werken uit dezelfde eeuw hebben altijd dezelfde context.",
        antwoord=False,
        uitleg="Ze kunnen uit een andere plaats, samenleving of persoonlijke situatie komen.",
    ),
    dict(
        type="waarofniet",
        vraag="Ruimte als element van de context gaat over waar het werk ontstond.",
        antwoord=True,
        uitleg="Ruimte als bouwsteen bij beeld gaat over perspectief en diepte. Dat is iets anders.",
    ),
    dict(
        type="waarofniet",
        vraag="De context van een kunstuiting is enkel belangrijk bij oude kunst, niet bij hedendaagse kunst.",
        antwoord=False,
        uitleg="Ook hedendaagse kunst reageert op haar tijd, plaats en samenleving.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een fotograaf toont in de jaren 1930 de armoede van boerengezinnen tijdens een economische crisis. Welke twee elementen van de context spelen het sterkst?",
        opties=["de tijd", "de sociale context", "de decoratieve functie", "het materiaal"],
        antwoord=[0, 1],
        uitleg="De crisisjaren (tijd) en de armoede in de samenleving (sociale context) verklaren het werk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een kunstenares die opgroeide tussen twee culturen, mengt in haar werk patronen van allebei. Welke context verklaart dit het best?",
        opties=[
            "de persoonlijke context van de kunstenaar",
            "de politieke context van het land",
            "de economische functie van haar werk",
            "de ontspannende functie van de patronen",
        ],
        antwoord=0,
        uitleg="Haar eigen achtergrond kleurt haar werk. Dat is de persoonlijke context.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men inhoud, functie, context en vormgeving best in samenhang?",
        opties=[
            "ze beïnvloeden elkaar: de context verklaart de functie, en de functie verklaart de vormgeving",
            "ze hebben niets met elkaar te maken en worden daarom altijd elk apart en los van elkaar beoordeeld",
            "de vormgeving bepaalt altijd alleen de prijs van een werk",
            "de context is enkel belangrijk als de kunstenaar nog leeft",
        ],
        antwoord=0,
        uitleg="Een propagandaschilderij (functie) uit een dictatuur (context) zal groots en duidelijk geschilderd zijn (vormgeving).",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk voorbeeld hoort bij de culturele context?",
        opties=[
            "in een samenleving gelden heldendichten als de hoogste vorm van kunst",
            "de kunstenaar verloor zijn huis en al zijn schetsen in een grote brand",
            "het werk is geschilderd met olieverf op doek",
            "het schilderij is 2 meter hoog en hangt in een grote zaal",
        ],
        antwoord=0,
        uitleg="Wat een samenleving als waardevol of normaal ziet, is de culturele context.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een beeldhouwer werkt in een land waar religieuze afbeeldingen van mensen niet gebruikelijk zijn, en maakt daarom vooral geometrische patronen. Welke context speelt?",
        opties=[
            "de culturele context",
            "de persoonlijke context van de beeldhouwer",
            "de economische functie van de patronen",
            "de ontspannende functie van het werk",
        ],
        antwoord=0,
        uitleg="De gewoonten en waarden van de samenleving bepalen hier wat er afgebeeld wordt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer kijk je naar de tijd als element van de context?",
        opties=[
            "als je nagaat in welke periode het werk gemaakt werd en wat er toen speelde",
            "als je meet hoe lang een film of een muziekstuk duurt",
            "als je nagaat hoe snel de kunstenaar het werk afwerkte",
            "als je bekijkt hoeveel jaar het werk al in hetzelfde museum aan de muur hangt",
        ],
        antwoord=0,
        uitleg="Bij context gaat tijd over de periode. Tempo of duur als bouwsteen is iets anders.",
    ),
]

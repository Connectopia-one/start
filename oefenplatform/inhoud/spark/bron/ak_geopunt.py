# -*- coding: utf-8 -*-
"""De vragen voor "Onderzoeken met kaartlagen" (✨ Spark, aardrijkskunde).

Uit de vakfiche 1ste graad A-stroom, rubriek "geografisch onderzoek" (17,5 % van
het examen, samen met [[ak_terrein]]).

Deel 1 gaat over wat een GIS-viewer is en wat je ermee kan: een gebied opzoeken
met de zoekbalk, kaartlagen aan- en uitzetten met het lagenpaneel, de legende
erbij halen, afstanden en oppervlakten meten met het meetgereedschap, hoogtes
aflezen en een kaartlaag transparant maken.
Deel 2 gaat over het onderzoek zelf: een onderzoeksvraag of een hypothese
opstellen, de juiste lagen kiezen, ze naast elkaar leggen en er een antwoord
uit afleiden.

Belangrijk bij het bijschrijven: gebruik alleen de woorden die de fiche zelf
gebruikt (zoekbalk, lagenpaneel, linkerpaneel, meetgereedschap, kaartlaag,
transparant maken). De knoppen van een website veranderen, en een vraag die
naar een knopnaam of een menupad vraagt, is binnen een jaar fout. Vraag naar
wat je ermee doet, niet naar waar het staat.

Geopunt gaat over Vlaanderen. Wie een vraag schrijft over een gebied in
Wallonië of het buitenland, doet dat niet met Geopunt maar met een atlas of een
andere bron.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Je wil weten of er vroeger een beek liep waar nu een straat ligt. Wat helpt je het meest?",
        opties=[
            "Kaarten van dat gebied naast elkaar leggen",
            "In de straat zelf naar water gaan kijken",
            "De inwoners van de straat opbellen",
            "De temperatuur in de straat gaan meten",
        ],
        antwoord=0,
        uitleg="Wie een oude kaart en een luchtfoto van vandaag over elkaar legt, ziet meteen wat er verdwenen of bijgekomen is. Dat is precies waar een kaartviewer voor dient.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een kaartlaag?",
        opties=[
            "Eén soort gegevens die je over de kaart legt",
            "De papieren laag waarop een kaart gedrukt wordt",
            "De hoogte van een gebied boven de zeespiegel",
            "Het aantal kaarten dat in een atlas past",
        ],
        antwoord=0,
        uitleg="Een kaartlaag toont één ding: de bodemsoort, het reliëf, de waterlopen, de gebouwen. Door lagen te stapelen, zie je verbanden die op één kaart niet zichtbaar zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor gebruik je de zoekbalk in een kaartviewer? Er zijn er meerdere juist.",
        opties=[
            "Om een adres te vinden",
            "Om coördinaten in te geven",
            "Om naar een gemeente te springen",
            "Om de kleuren van de kaart te wijzigen",
            "Om de kaart af te drukken op papier",
        ],
        antwoord=[0, 1, 2],
        uitleg="Met de zoekbalk bepaal je wélk gebied je bekijkt: een adres, een plaatsnaam of een paar coördinaten. Wat je daarna te zien krijgt, regel je met de lagen.",
    ),
    dict(
        type="invultekst",
        vraag="Het paneel waarin je kaartlagen aan- en uitzet, heet het ___.",
        antwoord="lagenpaneel",
        uitleg="In het lagenpaneel vink je aan wat je wil zien. Zet je te veel lagen tegelijk aan, dan wordt de kaart onleesbaar; vaak zijn twee lagen genoeg.",
    ),
    dict(
        type="waarofniet",
        vraag="Geopunt bevat geografische informatie over Vlaanderen.",
        antwoord=True,
        uitleg="Geopunt is het kaartportaal van de Vlaamse overheid. Voor Wallonië, Brussel of het buitenland heb je een andere bron of een atlas nodig.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom zou je een kaartlaag transparant maken?",
        opties=[
            "Om te zien wat eronder ligt",
            "Om de kaart sneller te laten laden",
            "Om de kleuren beter te kunnen afdrukken",
            "Om de laag daarna te kunnen verwijderen",
        ],
        antwoord=0,
        uitleg="Zet je een oude kaart half doorzichtig over een luchtfoto van vandaag, dan zie je allebei tegelijk. Zo vergelijk je twee tijdstippen op dezelfde plek.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor dient het meetgereedschap in een kaartviewer? Er zijn er meerdere juist.",
        opties=[
            "Een afstand tussen twee punten meten",
            "De oppervlakte van een perceel meten",
            "De lengte van een wandelweg meten",
            "De hoogte van een gebouw meten",
            "De temperatuur op die plaats meten",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het meetgereedschap meet lengtes en oppervlakten op de kaart. De hoogte lees je van een hoogtelaag af, en de temperatuur staat er helemaal niet in.",
    ),
    dict(
        type="waarofniet",
        vraag="In een kaartviewer heb je geen meetlat nodig om een afstand te kennen.",
        antwoord=True,
        uitleg="Het toestel rekent zelf om naar meter of kilometer, want het kent de schaal. Op een papieren kaart moet je nog altijd meten en zelf vermenigvuldigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarvoor heb je de legende van een kaartlaag nodig?",
        opties=[
            "Om te weten wat de kleuren betekenen",
            "Om de laag doorzichtig te kunnen maken",
            "Om te weten wie de kaart gemaakt heeft",
            "Om de kaart op de juiste schaal te zetten",
        ],
        antwoord=0,
        uitleg="Een bodemkaart in vijf kleuren zegt niets zonder legende. Daar staat welke kleur voor zand, leem, klei of veen staat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zet de laag met de waterlopen aan én de laag met de bebouwing. Wat kan je daarmee onderzoeken?",
        opties=[
            "Of er gebouwd is vlak bij het water",
            "Hoeveel mensen er in elk huis wonen",
            "Wanneer de huizen gebouwd werden",
            "Hoe diep het water in de beek staat",
        ],
        antwoord=0,
        uitleg="Twee lagen over elkaar tonen een verband in de ruimte. Hoeveel mensen, van wanneer of hoe diep zijn gegevens die in andere lagen of bronnen staan.",
    ),
    dict(
        type="invultekst",
        vraag="Een luchtfoto van vroeger naast een luchtfoto van nu leggen, noemt men beelden ___.",
        antwoord="vergelijken",
        uitleg="Vergelijken is de kern van dit soort onderzoek. Pas als je twee tijdstippen naast elkaar hebt, zie je wat er veranderd is en hoe snel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke bronnen vind je in een kaartportaal zoals Geopunt? Er zijn er meerdere juist.",
        opties=[
            "Kaarten",
            "Luchtfoto's",
            "Satellietbeelden",
            "Krantenartikels over de streek",
            "Foto's die bewoners zelf namen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een kaartportaal verzamelt kaarten, luchtfoto's en satellietbeelden van een gebied. Artikels en privéfoto's horen daar niet in.",
    ),
    dict(
        type="waarofniet",
        vraag="Een luchtfoto in een kaartviewer is altijd van vandaag.",
        antwoord=False,
        uitleg="Luchtfoto's worden om de zoveel tijd genomen en bewaard. Juist daardoor kan je reeksen van verschillende jaren naast elkaar leggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat kan je aflezen van een hoogtelaag?",
        opties=[
            "Hoe hoog een plaats boven de zeespiegel ligt",
            "Hoeveel verdiepingen een gebouw telt",
            "Hoe diep het grondwater onder je voeten zit",
            "Hoe steil een dak van een huis staat",
        ],
        antwoord=0,
        uitleg="Een hoogtelaag geeft de hoogte van het terrein. Daarmee zie je waar het water naartoe zal lopen en welke stukken laag genoeg liggen om onder te lopen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een kaartviewer handiger dan een papieren kaart om lagen te vergelijken?",
        opties=[
            "Omdat je lagen kan aan- en uitzetten en stapelen",
            "Omdat een papieren kaart altijd verouderd is",
            "Omdat een papieren kaart geen legende heeft",
            "Omdat je op papier geen afstanden kan meten",
        ],
        antwoord=0,
        uitleg="Op papier is elke kaart vast. In een viewer bepaal je zelf welke combinatie je ziet, en dat maakt verbanden zichtbaar.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je zoekt een gebied op met coördinaten in plaats van met een adres. Wanneer is dat handiger?",
        opties=[
            "Als het gebied geen adres heeft, zoals midden in een bos",
            "Als het gebied middenin een grote stad met veel straten ligt",
            "Als je de gemeentenaam niet kan spellen",
            "Als de kaartlaag nog niet geladen is",
        ],
        antwoord=0,
        uitleg="Een bosperceel, een akker of een punt in de zee heeft geen huisnummer. Met coördinaten leg je zo'n plek toch exact vast.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee kaartlagen over elkaar leggen lukt enkel als ze even oud zijn.",
        antwoord=False,
        uitleg="Het is juist interessant om lagen van verschillende jaren te combineren. Zo zie je wat er tussen die twee momenten veranderd is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zie je op een satellietbeeld dat op een gewone kaart niet staat?",
        opties=[
            "Hoe het gebied er in werkelijkheid uitziet",
            "De namen van alle straten in het gebied",
            "De grenzen tussen de gemeenten",
            "De hoogte van het terrein in meter",
        ],
        antwoord=0,
        uitleg="Een satellietbeeld toont de werkelijkheid: kleuren, patronen, gewassen op het veld. Namen, grenzen en hoogtecijfers komen van getekende lagen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom moet je bij een kaartlaag altijd kijken van wanneer ze dateert?",
        opties=[
            "Omdat het landschap intussen veranderd kan zijn",
            "Omdat oude lagen altijd verkeerd getekend zijn",
            "Omdat je anders de legende niet kan lezen",
            "Omdat de schaal per jaar verschillend is",
        ],
        antwoord=0,
        uitleg="Een bodemkaart blijft lang bruikbaar, maar een laag met gebouwen of landgebruik veroudert snel. Wie dat niet nakijkt, trekt een besluit over een landschap dat niet meer bestaat.",
    ),
    dict(
        type="invultekst",
        vraag="Een computerprogramma waarin je kaartlagen kan bekijken, stapelen en meten, noemt men een ___.",
        antwoord="GIS-viewer",
        uitleg="GIS staat voor geografisch informatiesysteem. Geopunt is er zo een: een viewer waarin de kaartlagen van de Vlaamse overheid samenkomen.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Je wil met kaarten uitzoeken waarom een bepaalde straat elk jaar onder water loopt. Waarmee begin je?",
        opties=[
            "Met een duidelijke onderzoeksvraag",
            "Met het meten van de straat",
            "Met het aanzetten van alle lagen tegelijk",
            "Met het besluit dat je verwacht",
            "Met een foto van de straat",
        ],
        antwoord=0,
        uitleg="Zonder vraag weet je niet welke lagen je nodig hebt. De vraag bepaalt het onderzoek, niet omgekeerd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een hypothese?",
        opties=[
            "Een verwacht antwoord dat je nog moet nakijken",
            "Het besluit waarmee je onderzoek uiteindelijk eindigt",
            "De vraag die je aan het begin opschrijft",
            "De bron waarin je het antwoord opzoekt",
        ],
        antwoord=0,
        uitleg="Een hypothese is een vermoeden dat je vooraf opschrijft. Daarna ga je met kaarten na of het klopt, en je mag ze gerust weerleggen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn goede onderzoeksvragen voor een kaartonderzoek? Er zijn er meerdere juist.",
        opties=[
            "Ligt de wijk die onderloopt lager dan de rest?",
            "Is er sinds 1990 meer verhard in deze gemeente?",
            "Liggen de boomgaarden op de leembodem?",
            "Is deze gemeente een fijne plek om te wonen?",
            "Welke muziek luisteren de inwoners het liefst?",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een goede onderzoeksvraag kan je met kaartlagen beantwoorden. Of een gemeente fijn is, en wat mensen graag horen, staat op geen enkele kaart.",
    ),
    dict(
        type="invultekst",
        vraag="Een vermoeden dat je vooraf opschrijft en daarna toetst, heet een ___.",
        antwoord="hypothese",
        uitleg="Een hypothese die onderuit gaat, is geen mislukking. Je weet dan iets wat je voordien nog niet wist.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hypothese die door het onderzoek weerlegd wordt, maakt het onderzoek waardeloos.",
        antwoord=False,
        uitleg="Een weerlegde hypothese levert evengoed kennis op. Het besluit wordt dan gewoon: het vermoeden klopte niet, en dit is wat er wél te zien is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je hypothese luidt: de overstroomde straat ligt lager dan de omgeving. Welke laag zet je aan?",
        opties=[
            "De hoogtelaag",
            "De laag met de gemeentegrenzen",
            "De laag met de bushaltes",
            "De laag met de gebouwnummers",
        ],
        antwoord=0,
        uitleg="De vraag gaat over hoogte, dus je hebt de hoogtelaag nodig. Elke andere laag kost tijd en maakt de kaart alleen maar drukker.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt of boomgaarden vooral op leemgrond liggen. Welke twee lagen leg je over elkaar?",
        opties=[
            "De bodemkaart en het landgebruik",
            "De hoogtekaart en de wegenkaart",
            "De bevolkingskaart en de bodemkaart",
            "De wegenkaart en de gemeentegrenzen",
        ],
        antwoord=0,
        uitleg="Je wil twee dingen tegelijk zien: waar de leem ligt en waar de boomgaarden staan. Vallen die vlakken samen, dan is er een verband.",
    ),
    dict(
        type="waarofniet",
        vraag="Twee patronen die op de kaart samenvallen, bewijzen altijd dat het ene het andere veroorzaakt.",
        antwoord=False,
        uitleg="Samenvallen is nog geen oorzaak. Misschien komt het door een derde factor, of is het toeval. Je hebt een verklaring nodig die ook steek houdt.",
    ),
    dict(
        type="meerkeuze",
        vraag="In welke volgorde verloopt een geografisch onderzoek?",
        opties=[
            "Vraag stellen, lagen kiezen, analyseren, besluiten",
            "Besluiten, vraag stellen, lagen kiezen, analyseren",
            "Lagen kiezen, besluiten, vraag stellen, analyseren",
            "Analyseren, lagen kiezen, besluiten, vraag stellen",
        ],
        antwoord=0,
        uitleg="Eerst de vraag of de hypothese, dan de juiste lagen, dan kijken wat je ziet, en pas daarna het besluit. Wie met het besluit begint, zoekt alleen nog bevestiging.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat hoort er in het besluit van een kaartonderzoek? Er zijn er meerdere juist.",
        opties=[
            "Een antwoord op de onderzoeksvraag",
            "Waarop je dat antwoord baseert",
            "Of je hypothese klopte of niet",
            "Hoeveel tijd je eraan besteed hebt",
            "Welke kleur de kaartlagen hadden",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een besluit geeft het antwoord, zegt waaruit het blijkt, en komt terug op de hypothese. Hoelang je gewerkt hebt, doet niet ter zake.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je ziet dat een wijk die onderloopt in een oude beekvallei ligt. Wat is daar het beste besluit uit?",
        opties=[
            "De wijk ligt op een plek waar het water van nature samenkomt",
            "De bewoners van die wijk hebben bij het bouwen iets fout gedaan",
            "De gemeente heeft de riolering te klein gemaakt",
            "In die wijk valt er meer regen dan in de rest",
        ],
        antwoord=0,
        uitleg="De kaart toont waar het water van nature naartoe loopt. Over riolering of schuld zegt ze niets, en dus hoort dat niet in het besluit.",
    ),
    dict(
        type="invultekst",
        vraag="De stap waarin je bekijkt wat de kaartlagen samen tonen, heet ___.",
        antwoord="analyseren",
        uitleg="Analyseren is meer dan kijken: je zoekt patronen, je vergelijkt, en je let ook op wat er níét te zien is.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een geografisch onderzoek hoort altijd vermeld te worden welke bronnen je gebruikt hebt.",
        antwoord=True,
        uitleg="Zonder bron kan niemand je werk nakijken. Noteer welke kaartlagen je gebruikte en van wanneer ze dateren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig om bij een onderzoek naar verharding twee luchtfoto's van verschillende jaren te nemen?",
        opties=[
            "Omdat je dan de verandering ziet, niet alleen de toestand",
            "Omdat één luchtfoto altijd te onscherp is",
            "Omdat luchtfoto's om de tien jaar van kleur wisselen",
            "Omdat je anders de legende niet kan lezen",
        ],
        antwoord=0,
        uitleg="Eén foto zegt hoe het nu is. Twee foto's zeggen wat erbij gekomen en verdwenen is, en dat is meestal waar de vraag over gaat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je meet met het meetgereedschap dat een perceel 0,8 hectare groot is. Hoeveel vierkante meter is dat?",
        opties=[
            "8000 vierkante meter",
            "800 vierkante meter",
            "80 vierkante meter",
            "80 000 vierkante meter",
        ],
        antwoord=0,
        uitleg="Eén hectare is 10 000 vierkante meter. Acht tienden daarvan is 8000 vierkante meter, ongeveer een voetbalveld.",
    ),
    dict(
        type="waarofniet",
        vraag="Hoe meer kaartlagen je tegelijk aanzet, hoe beter je onderzoek wordt.",
        antwoord=False,
        uitleg="Te veel lagen maken de kaart onleesbaar. Kies de lagen die bij je vraag horen en laat de rest uit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doe je als de kaartlagen je hypothese niet bevestigen?",
        opties=[
            "Je schrijft op wat je wél ziet en trekt daaruit je besluit",
            "Je zoekt net zolang tot je toch gelijk krijgt",
            "Je laat het onderzoek onafgewerkt liggen",
            "Je verandert de hypothese achteraf naar het resultaat",
        ],
        antwoord=0,
        uitleg="Je hypothese achteraf aanpassen aan het resultaat is geen onderzoek meer. Noteer eerlijk dat het vermoeden niet klopte en zeg wat de kaart wel toont.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom volstaat een kaartonderzoek soms niet en moet je toch ter plaatse gaan kijken?",
        opties=[
            "Omdat niet alles op een kaart terechtkomt",
            "Omdat kaarten altijd op de verkeerde schaal staan",
            "Omdat je de legende ter plaatse beter leest",
            "Omdat de kaartlagen enkel buiten laden",
        ],
        antwoord=0,
        uitleg="Een dichtgeslibde gracht, een pas gekapte haag of een geur staan op geen enkele laag. Daarvoor bestaan de terreintechnieken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke uitspraken over een onderzoeksvraag kloppen? Er zijn er meerdere juist.",
        opties=[
            "Ze is zo nauwkeurig mogelijk geformuleerd",
            "Ze gaat over een afgebakend gebied",
            "Ze is met de gekozen bronnen te beantwoorden",
            "Ze bevat het antwoord al in de vraag zelf",
            "Ze gaat over zoveel mogelijk onderwerpen tegelijk",
        ],
        antwoord=[0, 1, 2],
        uitleg="Een bruikbare vraag is scherp, begrensd en beantwoordbaar. Een vraag die het antwoord al bevat, of die alles tegelijk wil weten, levert niets op.",
    ),
    dict(
        type="invultekst",
        vraag="Het gebied dat je in je onderzoek bekijkt, noemt men het onderzoeks___.",
        antwoord="onderzoeksgebied",
        uitleg="Bak je onderzoeksgebied duidelijk af, bijvoorbeeld tot één wijk of één vallei. Anders wordt de vraag te groot om te beantwoorden.",
    ),
]

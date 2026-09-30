# -*- coding: utf-8 -*-
"""De vragen voor "Stad en platteland" (🚀 Boost doorstroom, aardrijkskunde).

Uit de vakfiche 2de graad doorstroom, rubriek "stad, platteland en
verstedelijking" (10 % van het examen).

Deel 1 gaat over wonen en verhuizen: waarom mensen in de stad of op het
platteland wonen en waarom ze in de ene of de andere richting verhuizen, met de
beïnvloedende factoren die de fiche opsomt, en over de hiërarchie van steden op
economische, culturele en politieke gronden.
Deel 2 gaat over wat er daardoor in de stad en op het platteland verandert:
sociale segregatie, multiculturaliteit en functiewijziging, en de vijf
landschapsveranderingen uit de fiche: verstedelijking van het platteland,
ontvolking van het platteland, inbreiding en groei van de steden, veranderende
mobiliteit en stadslandbouw.

De voorbeelden blijven zoveel mogelijk bij wat een kind hier kan herkennen:
een verkaveling aan de rand van een dorp, een oude fabriek die lofts wordt, een
winkelstraat die leegloopt. De fiche vraagt immers uitdrukkelijk om vanuit
concrete situaties te werken.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waarom trekken steden mensen aan?",
        opties=[
            "Er is meer werk, onderwijs en voorzieningen bij elkaar",
            "Er is meer open ruimte en groen per inwoner",
            "De woningen zijn er bijna altijd goedkoper",
            "Er is er minder verkeer en minder lawaai",
        ],
        antwoord=0,
        uitleg="Een stad bundelt werk, scholen, ziekenhuizen, winkels en cultuur op korte afstand. Ruimte, rust en groen zijn juist de troeven van het platteland.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke redenen brengen mensen ertoe om net op het platteland te gaan wonen? (meerdere antwoorden mogelijk)",
        opties=[
            "Meer ruimte voor hetzelfde geld",
            "Meer rust en minder lawaai",
            "Meer groen in de directe omgeving",
            "Meer universiteiten in de buurt",
            "Meer hoofdkantoren van bedrijven",
        ],
        antwoord=[0, 1, 2],
        uitleg="Ruimte, rust en groen zijn de klassieke pullfactoren van het platteland. Universiteiten en hoofdkantoren liggen juist in de stad, dat is een reden om er net wel te wonen.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie op het platteland woont en in de stad werkt, legt meestal meer kilometers af dan wie in de stad zelf woont.",
        antwoord=True,
        uitleg="Ruimte en rust koop je met reistijd. Dat pendelen is een van de redenen waarom verstedelijking van het platteland de files doet groeien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gezin verhuist van de stad naar een dorp twintig kilometer verderop, voor een tuin en een rustiger straat. Hoe noem je dat?",
        opties=[
            "Stadsvlucht",
            "Verstedelijking",
            "Inbreiding",
            "Segregatie",
        ],
        antwoord=0,
        uitleg="Stadsvlucht is het vertrek van stadsbewoners naar de rand en het platteland. Het is een van de motoren achter de verstedelijking van dorpen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke beïnvloedende factoren noemt de vakfiche bij de keuze tussen stad en platteland? (meerdere antwoorden mogelijk)",
        opties=[
            "Het klimaat en de klimaatverandering",
            "De politieke en de oorlogssituatie",
            "De welvaart, het welzijn en armoede",
            "Het aantal meridianen over het land",
            "De kleurkeuze van de kaartmaker",
        ],
        antwoord=[0, 1, 2],
        uitleg="De fiche somt klimaat en klimaatverandering, reliëf, bodemkwaliteit, de politieke situatie, de oorlogssituatie, welvaart en welzijn, en armoede op.",
    ),
    dict(
        type="waarofniet",
        vraag="In veel landen met een lagere ontwikkelingsgraad trekken mensen vooral van het platteland naar de stad.",
        antwoord=True,
        uitleg="Werk, onderwijs en zorg zitten daar in de stad. Groeit die stad sneller dan haar woningen en riolering, dan ontstaan er sloppenwijken aan de rand.",
    ),
    dict(
        type="meerkeuze",
        vraag="Op welke gronden bepaalt men de hiërarchie tussen steden?",
        opties=[
            "Hun economisch, cultureel en politiek belang",
            "Hun oppervlakte in vierkante kilometer",
            "Hun ouderdom en het jaar van hun stichting",
            "Hun ligging ten opzichte van de nulmeridiaan",
        ],
        antwoord=0,
        uitleg="Niet grootte maar belang telt. Een kleinere stad met een regeringszetel of een wereldhaven kan hoger in de hiërarchie staan dan een grotere stad zonder die functies.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken wijzen op het economische belang van een stad? (meerdere antwoorden mogelijk)",
        opties=[
            "Hoofdkwartieren van grote ondernemingen",
            "Internationale banken in de stad",
            "Belangrijke handelszaken en beurzen",
            "Grote musea en onderzoeksinstellingen",
            "De zetel van de regering van het land",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bedrijven, banken en handel zijn economische criteria. Musea en onderzoek horen bij het culturele belang, een regeringszetel bij het politieke.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je met één woord de rangorde tussen steden op basis van hun belang?",
        antwoord=["hiërarchie", "de hiërarchie", "stedenhiërarchie"],
        uitleg="Bovenaan de hiërarchie staan de wereldsteden, onderaan de kleine stadjes die vooral hun eigen streek bedienen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke kenmerken wijzen op het culturele belang van een stad? (meerdere antwoorden mogelijk)",
        opties=[
            "Universiteiten en hogescholen",
            "Grote musea en theaters",
            "Ruime recreatiemogelijkheden",
            "Internationale banken en beurzen",
            "Hoofdkwartieren van de regering",
        ],
        antwoord=[0, 1, 2],
        uitleg="Onderwijs, musea en ontspanning zijn culturele criteria. Banken zijn economisch, regeringszetels politiek.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stad kan tegelijk hoog scoren op economisch, cultureel én politiek belang.",
        antwoord=True,
        uitleg="Parijs, Londen en Tokio combineren de drie. Die stapeling is juist wat een wereldstad tot een wereldstad maakt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom staat Brussel hoog in de Europese stedenhiërarchie, ook al is het niet de grootste stad van Europa?",
        opties=[
            "Er zetelen belangrijke Europese instellingen",
            "Het ligt precies in het midden van het continent",
            "Het heeft de grootste haven van het continent",
            "Het heeft het oudste stadscentrum van Europa",
        ],
        antwoord=0,
        uitleg="Politiek belang weegt zwaar in de hiërarchie. Door de Europese instellingen en de NAVO trekt Brussel diplomaten, lobbyisten en internationale bedrijven aan.",
    ),
    dict(
        type="waarofniet",
        vraag="De grootste stad van een land is altijd ook de hoofdstad van dat land.",
        antwoord=False,
        uitleg="In de Verenigde Staten is New York veel groter dan Washington, en in Australië is Sydney groter dan Canberra. Politiek belang en inwonersaantal vallen niet samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een dorp krijgt er in twintig jaar drie verkavelingen bij, maar geen enkele nieuwe winkel. Wat gebeurt er?",
        opties=[
            "Het wordt een woondorp waar men voor alles wegrijdt",
            "Het klimt daardoor in de hiërarchie van de steden",
            "Het wordt daardoor een stad met een eigen centrum",
            "De bevolkingsdichtheid van het dorp daalt erdoor",
        ],
        antwoord=0,
        uitleg="Wonen komt erbij, voorzieningen niet. De inwoners werken, winkelen en gaan naar school elders, en de autoafhankelijkheid van het dorp neemt toe.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom blijft het reliëf ook vandaag meespelen bij waar steden groeien?",
        opties=[
            "Bouwen en wegen aanleggen is in vlak gebied goedkoper",
            "In de bergen is het klimaat altijd te koud om te wonen",
            "Op hoogte is er wettelijk geen bebouwing toegestaan",
            "Steile hellingen hebben altijd een onvruchtbare bodem",
        ],
        antwoord=0,
        uitleg="Technisch kan er veel, maar kosten sturen. In dalen en vlaktes liggen de wegen, de sporen en het water, en daar groeien de steden dus het snelst.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de dagelijkse verplaatsing van mensen tussen hun woonplaats en hun werkplaats?",
        antwoord=["pendelen", "het pendelen", "pendelverkeer"],
        uitleg="Pendelen verbindt het platteland met de stad. Hoe meer mensen buiten de stad wonen en erin werken, hoe zwaarder dat verkeer weegt.",
    ),
    dict(
        type="waarofniet",
        vraag="Armoede kan zowel een reden zijn om naar de stad te trekken als om er juist weg te blijven.",
        antwoord=True,
        uitleg="In de stad is er meer kans op werk, maar het wonen is er duurder. Dat is precies waarom armere gezinnen vaak in de goedkoopste, oudste wijken terechtkomen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je onderzoekt of een gemeente verstedelijkt. Welke bronnen helpen je daarbij? (meerdere antwoorden mogelijk)",
        opties=[
            "Luchtfoto's van vroeger en nu naast elkaar",
            "Cijfers over het aantal inwoners per jaar",
            "Kaarten van het bodemgebruik door de jaren heen",
            "Een klimatogram van het dichtstbijzijnde weerstation",
            "Een leeftijdshistogram van een buurland",
        ],
        antwoord=[0, 1, 2],
        uitleg="Verstedelijking zie je aan bebouwing, inwoners en bodemgebruik over de tijd. Een klimatogram gaat over het weer, een histogram van een buurland over iets heel anders.",
    ),
    dict(
        type="waarofniet",
        vraag="Verstedelijking betekent alleen dat steden meer inwoners krijgen.",
        antwoord=False,
        uitleg="Verstedelijking is even goed het opschuiven van stedelijke kenmerken naar het platteland: verkavelingen, winkelcentra langs de invalsweg, bedrijventerreinen bij de afrit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf kiest voor een terrein vlak bij een snelwegafrit buiten de stad. Waarom?",
        opties=[
            "Grond is er goedkoper en bereikbaar voor vrachtwagens",
            "De bevolkingsdichtheid is er hoger dan in de stad",
            "De werknemers wonen er allemaal op wandelafstand",
            "Er gelden daar geen regels over bodemgebruik meer",
        ],
        antwoord=0,
        uitleg="Ruimte en bereikbaarheid wegen zwaarder dan nabijheid van klanten. Het gevolg is dat werk uit de stad wegtrekt en dat de open ruimte verder versnippert.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met sociale segregatie in een stad?",
        opties=[
            "Bevolkingsgroepen wonen in gescheiden wijken",
            "De stad groeit sneller dan haar omliggende dorpen",
            "Oude gebouwen krijgen er een nieuwe functie",
            "Het aantal inwoners van de stad neemt af",
        ],
        antwoord=0,
        uitleg="Segregatie is ruimtelijke scheiding: arm en rijk, of groepen van verschillende afkomst, komen in verschillende wijken terecht. Dat gebeurt zelden bewust, maar via woningprijzen en kansen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de belangrijkste motor achter sociale segregatie in West-Europese steden?",
        opties=[
            "De verschillen in woningprijs tussen wijken",
            "De ligging van de wijken ten opzichte van het noorden",
            "De keuze van de gemeente om wijken toe te wijzen",
            "Het reliëf van de bodem waarop de stad gebouwd is",
        ],
        antwoord=0,
        uitleg="Wie weinig kan betalen, belandt in de goedkoopste woningen, en die liggen bij elkaar. Zo ontstaat scheiding zonder dat iemand ze oplegt.",
    ),
    dict(
        type="waarofniet",
        vraag="Multiculturaliteit en sociale segregatie zijn twee woorden voor hetzelfde.",
        antwoord=False,
        uitleg="Multiculturaliteit gaat over wie er samen in een stad woont, segregatie over de vraag of die groepen ook door elkaar wonen. Een stad kan heel divers zijn en tegelijk sterk gescheiden, of net niet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een oude textielfabriek in het centrum wordt omgebouwd tot appartementen. Hoe noem je dat?",
        opties=[
            "Een functiewijziging",
            "Een ontvolking",
            "Een segregatie",
            "Een schaalvergroting",
        ],
        antwoord=0,
        uitleg="Het gebouw blijft, het gebruik verandert: van industrie naar wonen. Zulke functiewijzigingen zijn een van de duidelijkste sporen van de de-industrialisatie in stadscentra.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke veranderingen horen bij de verstedelijking van het platteland? (meerdere antwoorden mogelijk)",
        opties=[
            "Nieuwe verkavelingen rond de dorpskern",
            "Winkelcentra en bedrijven langs de invalswegen",
            "Meer bebouwing op wat vroeger akkerland was",
            "Meer weilanden en hagen dan dertig jaar geleden",
            "Minder autoverkeer dan dertig jaar geleden",
        ],
        antwoord=[0, 1, 2],
        uitleg="Verstedelijking van het platteland is stedelijke bebouwing en stedelijke functies die opschuiven naar het dorp. Meer open ruimte en minder verkeer zijn precies het omgekeerde.",
    ),
    dict(
        type="waarofniet",
        vraag="Ontvolking van het platteland gebeurt vooral in afgelegen streken zonder werk of voorzieningen.",
        antwoord=True,
        uitleg="Jongeren trekken weg voor studie en werk, de school en de bakker sluiten, en dat maakt blijven nog moeilijker. In delen van Spanje en Zuid-Italië staan zo hele dorpen leeg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is inbreiding?",
        opties=[
            "Bouwen op open plekken binnen de bestaande stad",
            "Bouwen op akkerland aan de rand van de stad",
            "Een oud gebouw slopen zonder er iets voor terug te bouwen",
            "Woningen omvormen tot kantoren in het centrum",
        ],
        antwoord=0,
        uitleg="Inbreiding vult lege plekken en oude bedrijfsterreinen binnen de stad op. Het alternatief is uitbreiding, en dat kost telkens open ruimte buiten de stad.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kiezen veel steden vandaag voor inbreiding in plaats van uitbreiding?",
        opties=[
            "Zo blijft de open ruimte buiten de stad gespaard",
            "Zo wordt bouwen binnen de stad altijd goedkoper",
            "Zo daalt het aantal inwoners van de stad sneller",
            "Zo verdwijnt de sociale segregatie uit de wijken",
        ],
        antwoord=0,
        uitleg="Open ruimte is in Vlaanderen schaars geworden. Inbreiding houdt bovendien de voorzieningen dicht bij de mensen, waardoor er minder autokilometers nodig zijn.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het opdelen van de open ruimte in kleine, van elkaar gescheiden stukken door wegen en bebouwing?",
        antwoord=["versnippering", "de versnippering"],
        uitleg="Versnippering is een van de grootste problemen van de Vlaamse ruimte. Kleine losse stukken natuur werken veel minder goed dan één groot aaneengesloten gebied.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is stadslandbouw?",
        opties=[
            "Voedsel telen in of vlak bij de stad zelf",
            "Landbouwgrond verkavelen voor nieuwe woningen",
            "Landbouwbedrijven samenvoegen tot grotere bedrijven",
            "Voedsel invoeren uit andere werelddelen",
        ],
        antwoord=0,
        uitleg="Volkstuinen, daktuinen, serres op oude bedrijventerreinen: voedsel wordt geteeld waar het ook gegeten wordt. Dat scheelt transport en maakt de stad groener.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke voordelen worden aan stadslandbouw toegeschreven? (meerdere antwoorden mogelijk)",
        opties=[
            "Kortere afstand tussen teelt en bord",
            "Meer groen en minder verharding in de stad",
            "Meer contact tussen buurtbewoners onderling",
            "Genoeg opbrengst om de hele stad te voeden",
            "Lagere grondprijzen in het stadscentrum",
        ],
        antwoord=[0, 1, 2],
        uitleg="Stadslandbouw wint op transport, groen en sociaal contact. Een stad helemaal voeden lukt er niet mee, en op de grondprijs heeft ze geen invloed.",
    ),
    dict(
        type="waarofniet",
        vraag="Veranderende mobiliteit verandert ook het landschap.",
        antwoord=True,
        uitleg="Een nieuwe ring, een fietssnelweg of een gesloten spoorlijn herschikt waar mensen wonen en werken. Wat goed bereikbaar wordt, wordt bebouwd; wat afgesneden raakt, loopt leeg.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een winkelstraat in het centrum staat een derde van de panden leeg. Welke verklaringen zijn geloofwaardig? (meerdere antwoorden mogelijk)",
        opties=[
            "Winkelcentra aan de rand trekken de klanten weg",
            "Meer mensen kopen online in plaats van in de winkel",
            "De straat is moeilijk bereikbaar geworden met de auto",
            "De bevolking van het land is gehalveerd",
            "De winkelstraat ligt op een te hoge breedtegraad",
        ],
        antwoord=[0, 1, 2],
        uitleg="Concurrentie aan de rand, online kopen en bereikbaarheid zijn de klassieke oorzaken van leegstand. De twee laatste opties slaan nergens op.",
    ),
    dict(
        type="waarofniet",
        vraag="Een stad die inwoners verliest, verliest daarom ook haar economische functie.",
        antwoord=False,
        uitleg="Er zijn steden die leeglopen maar hun kantoren, haven en universiteit houden. Woonfunctie en economische functie kunnen apart van elkaar bewegen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een gevolg van verharding in de stad?",
        opties=[
            "Regenwater loopt sneller weg en dringt niet in de bodem",
            "De grondwatervoorraad onder de stad wordt aangevuld",
            "De temperatuur in de stad daalt tijdens een hittegolf",
            "Er groeien meer bomen tussen de straten en pleinen",
        ],
        antwoord=0,
        uitleg="Beton en asfalt laten geen water door. Het water stroomt naar de riool, het grondwater vult niet aan, en bij hevige regen loopt het riool over.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe heet het verschijnsel waarbij het in een stad meetbaar warmer is dan op het platteland eromheen?",
        antwoord=["hitte-eilandeffect", "het hitte-eilandeffect", "hitte-eiland"],
        uitleg="Steen en asfalt slaan warmte op en geven ze 's nachts weer af, en er is weinig groen dat verkoelt. Het verschil loopt tijdens een hittegolf op tot enkele graden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een gemeente breekt een betonnen plein open en plant er bomen. Welk probleem pakt ze daarmee aan?",
        opties=[
            "De hitte en het wegstromen van regenwater",
            "De sociale segregatie tussen de wijken",
            "De hiërarchie van de stad in de regio",
            "De ontvolking van het platteland eromheen",
        ],
        antwoord=0,
        uitleg="Minder verharding betekent meer schaduw, meer verdamping en water dat in de bodem trekt. Aan segregatie of hiërarchie verandert een plein niets.",
    ),
    dict(
        type="waarofniet",
        vraag="Functiewijziging in een stad gebeurt alleen bij oude fabrieksgebouwen.",
        antwoord=False,
        uitleg="Kerken worden bibliotheken, kantoren worden appartementen, scholen worden woningen. Elk gebouw kan een nieuwe functie krijgen als de vraag verandert.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vergelijkt twee luchtfoto's van dezelfde gemeente uit 1970 en nu. Waaraan zie je verstedelijking het snelst?",
        opties=[
            "Aan de oppervlakte die bebouwd en verhard is",
            "Aan de kleur van de daken op de foto's",
            "Aan de hoogte waarop de foto genomen is",
            "Aan het aantal wolken boven de gemeente",
        ],
        antwoord=0,
        uitleg="Verstedelijking lees je af aan bebouwing en verharding die toenemen ten koste van akkers en weiden. Let er wel op dat beide foto's in hetzelfde seizoen en op dezelfde schaal genomen zijn.",
    ),
    dict(
        type="waarofniet",
        vraag="In een multiculturele wijk kan het straatbeeld zelf een bron zijn voor geografisch onderzoek.",
        antwoord=True,
        uitleg="Winkels, opschriften, gebedshuizen en marktkramen vertellen wie er woont en hoe dat veranderd is. Dat aflezen op het terrein heet terreinkartering.",
    ),
]

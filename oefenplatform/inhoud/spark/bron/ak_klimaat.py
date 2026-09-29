# -*- coding: utf-8 -*-
"""De vragen voor "Het klimaat verandert" (✨ Spark, aardrijkskunde).

Uit de vakfiche 1ste graad A-stroom, rubriek "veranderingen in het landschap",
onderdeel "verandering door klimaat" (deel van de 40 %, samen met
[[ak_aardkorst]], [[ak_weer]] en [[ak_mens]]).

Deel 1 gaat over de oorzaak: wat fossiele brandstoffen zijn, wat broeikasgassen
zijn, hoe het natuurlijke broeikaseffect werkt en waardoor het versterkt raakt.
Deel 2 gaat over de gevolgen voor het landschap en voor de mens in België,
Europa en de wereld, waaronder de zeespiegelstijging, en over wat duurzaam
handelen daaraan kan doen.

Twee dingen die de fiche uitdrukkelijk vraagt en die hier dus scherp staan.
Ten eerste: het broeikaseffect is op zich natuurlijk en noodzakelijk; zonder
zou het op aarde gemiddeld ver onder nul zijn. Het probleem is het vérsterkte
broeikaseffect. Een vraag mag die twee nooit door elkaar halen.
Ten tweede: de zeespiegel stijgt om twee redenen, en smeltend zee-ijs is er
geen van. Water dat opwarmt zet uit, en ijs dat op land ligt voegt water toe.
Drijvend ijs verplaatste dat water al.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Steenkool, aardolie en aardgas krijgen samen één naam. Welke?",
        opties=[
            "Fossiele brandstoffen",
            "Hernieuwbare brandstoffen",
            "Vaste grondstoffen",
            "Natuurlijke bouwstoffen",
        ],
        antwoord=0,
        uitleg="Ze heten fossiel omdat ze uit resten van planten en dieren ontstaan zijn, diep onder de grond, over miljoenen jaren.",
    ),
    dict(
        type="waarofniet",
        vraag="Fossiele brandstoffen raken op, want er wordt er veel sneller van verbruikt dan er bij komt.",
        antwoord=True,
        uitleg="Nieuwe voorraden vormen zich over miljoenen jaren. Wat wij in één jaar opstoken, heeft de aarde in een onvoorstelbaar veelvoud daarvan opgebouwd.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke van deze zijn broeikasgassen? Er zijn er meerdere juist.",
        opties=[
            "Koolstofdioxide",
            "Methaan",
            "Waterdamp",
            "Zuurstof",
            "Stikstofgas",
        ],
        antwoord=[0, 1, 2],
        uitleg="Koolstofdioxide, methaan, waterdamp en lachgas houden warmte vast. Zuurstof en stikstof vormen samen bijna de hele dampkring, maar werken niet als broeikasgas.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat komt er vrij als je fossiele brandstoffen verbrandt?",
        opties=[
            "Koolstofdioxide",
            "Zuurstof",
            "Stikstofgas",
            "Waterstof",
        ],
        antwoord=0,
        uitleg="Bij verbranding komt de koolstof die miljoenen jaren in de grond zat, als koolstofdioxide in de lucht terecht. Juist dat gas versterkt het broeikaseffect.",
    ),
    dict(
        type="invultekst",
        vraag="De laag gassen rond de aarde waarin het weer zich afspeelt, heet de ___.",
        antwoord="atmosfeer",
        uitleg="De atmosfeer of dampkring houdt warmte vast en beschermt tegen straling. Zonder dat laagje gas zou er geen leven mogelijk zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt het broeikaseffect?",
        opties=[
            "Gassen houden een deel van de warmte van de aarde vast",
            "Gassen houden het zonlicht tegen voor het binnenkomt",
            "Gassen maken de aarde zelf warmer van binnenuit",
            "Gassen laten alle warmte de ruimte in ontsnappen",
        ],
        antwoord=0,
        uitleg="Zonlicht komt binnen en warmt het oppervlak op. De aarde straalt die warmte weer uit, en broeikasgassen houden een deel ervan tegen, zoals het glas van een serre.",
    ),
    dict(
        type="waarofniet",
        vraag="Zonder broeikaseffect zou het op aarde gemiddeld ver onder nul zijn.",
        antwoord=True,
        uitleg="Het natuurlijke broeikaseffect is er altijd geweest en is noodzakelijk: zonder die gassen zou de gemiddelde temperatuur rond de min achttien graden liggen in plaats van rond de vijftien.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt men met het versterkt broeikaseffect?",
        opties=[
            "Er zitten meer broeikasgassen in de lucht dan vroeger",
            "De zon straalt sinds enkele jaren veel krachtiger",
            "De aarde draait sneller rond en warmt daardoor op",
            "De dampkring is dikker geworden door de bewolking",
        ],
        antwoord=0,
        uitleg="Door het verbranden van fossiele brandstoffen komt er extra koolstofdioxide bij. Daardoor wordt er meer warmte vastgehouden dan van nature het geval was.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke menselijke activiteiten brengen extra broeikasgassen in de lucht? Er zijn er meerdere juist.",
        opties=[
            "Rijden met een benzine- of dieselwagen",
            "Verwarmen met aardgas of stookolie",
            "Bossen kappen en verbranden",
            "Stroom opwekken met zonnepanelen",
            "Fietsen naar school in plaats van rijden",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alles waarbij fossiele brandstof verbrandt, voegt koolstofdioxide toe. Bossen kappen telt dubbel: het gaat de lucht in én de bomen kunnen niets meer opnemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom noemt men bossen en oceanen koolstofputten?",
        opties=[
            "Omdat ze koolstofdioxide uit de lucht opnemen",
            "Omdat er koolstof in de grond onder hen zit",
            "Omdat ze zelf veel koolstofdioxide uitstoten",
            "Omdat ze warmte uit de dampkring wegnemen",
        ],
        antwoord=0,
        uitleg="Bomen nemen koolstofdioxide op om te groeien, en zeewater lost het gas op. Daardoor halen ze een deel van onze uitstoot uit de lucht.",
    ),
    dict(
        type="invultekst",
        vraag="Het gas dat vrijkomt bij het verbranden van steenkool, olie en gas en dat het meest bijdraagt aan het versterkt broeikaseffect, is ___.",
        antwoord="koolstofdioxide",
        uitleg="Koolstofdioxide wordt ook CO2 geschreven. Het blijft heel lang in de dampkring hangen, en daarom telt wat er vandaag bij komt nog decennia mee.",
    ),
    dict(
        type="waarofniet",
        vraag="Klimaatverandering en het weer van vandaag zijn hetzelfde.",
        antwoord=False,
        uitleg="Eén koude winter bewijst niets over het klimaat, en één hete dag evenmin. Klimaat gaat over gemiddelden over tientallen jaren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar komt het methaan vandaan dat mee het broeikaseffect versterkt?",
        opties=[
            "Uit veeteelt, rijstvelden en stortplaatsen",
            "Uit de motoren van elektrische wagens",
            "Uit de zonnepanelen op daken",
            "Uit het zeewater rond de evenaar",
        ],
        antwoord=0,
        uitleg="Methaan ontstaat waar organisch materiaal vergaat zonder zuurstof: in de maag van runderen, in natte rijstvelden en onder een afvalberg.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke energiebronnen zijn hernieuwbaar? Er zijn er meerdere juist.",
        opties=[
            "Wind",
            "Zon",
            "Waterkracht",
            "Aardolie",
            "Steenkool",
        ],
        antwoord=[0, 1, 2],
        uitleg="Wind, zon, water, aardwarmte en biomassa raken niet op. Aardolie en steenkool wel, en bij de verbranding ervan komt bovendien koolstofdioxide vrij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom stoot een windmolen tijdens het draaien geen koolstofdioxide uit?",
        opties=[
            "Omdat er niets verbrand wordt om stroom te maken",
            "Omdat de wieken het gas uit de lucht filteren",
            "Omdat windmolens buiten in de open lucht staan",
            "Omdat de stroom pas later gebruikt wordt",
        ],
        antwoord=0,
        uitleg="Een windmolen zet bewegende lucht rechtstreeks om in stroom. Er komt geen verbranding aan te pas, dus ook geen koolstofdioxide.",
    ),
    dict(
        type="waarofniet",
        vraag="Het klimaat van de aarde is in het verleden nooit veranderd.",
        antwoord=False,
        uitleg="Er zijn ijstijden en warme perioden geweest. Wat nu anders is, is de snelheid: de opwarming gaat veel sneller dan bij de natuurlijke schommelingen van vroeger.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe weten wetenschappers hoe warm het duizenden jaren geleden was?",
        opties=[
            "Uit luchtbelletjes in diepe ijslagen",
            "Uit oude weerberichten in de kranten",
            "Uit de hoogte van de bergen destijds",
            "Uit de kleur van de gesteenten",
        ],
        antwoord=0,
        uitleg="In het ijs van Groenland en Antarctica zit lucht van toen opgesloten. Door die belletjes te meten, weet men hoeveel koolstofdioxide er destijds in de dampkring zat.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is het verband tussen fossiele brandstoffen en het klimaat?",
        opties=[
            "Verbranden geeft broeikasgassen, die houden warmte vast",
            "Verbranden geeft rook, en rook houdt het zonlicht tegen",
            "Ontginnen maakt putten, en die vangen het regenwater op",
            "Vervoeren kost energie, en die energie verwarmt de lucht",
        ],
        antwoord=0,
        uitleg="De keten is kort: verbranden, koolstofdioxide in de dampkring, meer warmte vastgehouden, hogere gemiddelde temperatuur.",
    ),
    dict(
        type="invultekst",
        vraag="Brandstoffen die ontstaan zijn uit resten van planten en dieren van miljoenen jaren geleden, noemt men ___ brandstoffen.",
        antwoord="fossiele",
        uitleg="Steenkool komt uit oude moerasbossen, aardolie en aardgas vooral uit zeeorganismen. Alle drie zitten ze diep in de ondergrond.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom helpt een goed geïsoleerd huis tegen klimaatverandering?",
        opties=[
            "Omdat er minder gestookt moet worden",
            "Omdat het de koolstofdioxide tegenhoudt",
            "Omdat het de zonnewarmte weerkaatst",
            "Omdat het minder plaats inneemt in de straat",
        ],
        antwoord=0,
        uitleg="Isolatie houdt de warmte binnen. Er is dan minder gas of stookolie nodig, en dus komt er minder koolstofdioxide in de lucht.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="De gletsjers in de Alpen worden elk jaar korter. Waarvan is dat een gevolg?",
        opties=[
            "Van de opwarming van het klimaat",
            "Van de wind die er de sneeuw wegblaast",
            "Van de toeristen die er komen skiën",
            "Van het reliëf dat er langzaam daalt",
        ],
        antwoord=0,
        uitleg="Een gletsjer krimpt als er in de zomer meer smelt dan er in de winter bij komt. Dat gebeurt overal ter wereld, en het landschap dat vrijkomt is kaal gesteente.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom stijgt de zeespiegel door klimaatverandering? Er zijn er meerdere juist.",
        opties=[
            "Water zet uit als het warmer wordt",
            "IJs op het land smelt en loopt naar zee",
            "Gletsjers in de bergen worden kleiner",
            "Zee-ijs dat drijft, smelt weg",
            "Er valt meer regen boven de oceanen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Warmer water neemt meer plaats in, en ijs dat op land lag voegt water toe. Drijvend zee-ijs niet: dat verplaatste zijn water al, net zoals een ijsblokje een glas niet doet overlopen.",
    ),
    dict(
        type="waarofniet",
        vraag="Als al het drijvende zee-ijs rond de noordpool smelt, stijgt de zeespiegel daardoor sterk.",
        antwoord=False,
        uitleg="Drijvend ijs duwt nu al evenveel water opzij als het zelf zal worden. Het is het ijs op land, op Groenland en Antarctica, dat de zeespiegel doet stijgen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is zeespiegelstijging juist voor België een probleem?",
        opties=[
            "Omdat de polders achter de kust heel laag liggen",
            "Omdat België geen dijken langs de kust heeft",
            "Omdat de Belgische kust bijna volledig uit klif bestaat",
            "Omdat er in België geen havens aan zee liggen",
        ],
        antwoord=0,
        uitleg="Achter de duinen ligt een brede strook laagland, deels onder het niveau van de zeespiegel. Stijgt de zee, dan moeten dijken en duinen hoger en breder.",
    ),
    dict(
        type="invultekst",
        vraag="Een muur of dam die het land tegen het water beschermt, heet een ___.",
        antwoord="dijk",
        uitleg="Langs onze kust en langs de Schelde liggen dijken. Ze worden stelselmatig verhoogd, want de zee komt hoger te staan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke gevolgen van klimaatverandering merkt men in België? Er zijn er meerdere juist.",
        opties=[
            "Drogere zomers met lage waterstanden",
            "Hevigere buien die wateroverlast geven",
            "Meer hittegolven dan vroeger",
            "Strengere winters dan ooit tevoren",
            "Meer orkanen boven de Noordzee",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bij ons uit de opwarming zich in drogere zomers, hevigere buien en meer hitte. Orkanen ontstaan boven veel warmer zeewater dan de Noordzee.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom schuiven plant- en diersoorten op naar het noorden?",
        opties=[
            "Omdat hun leefgebied mee opschuift met de warmte",
            "Omdat er in het noorden meer plaats vrij is",
            "Omdat de dagen er in de zomer langer duren",
            "Omdat de bodem er vruchtbaarder aan het worden is",
        ],
        antwoord=0,
        uitleg="Elke soort heeft een temperatuurbereik waarin ze het goed doet. Wordt het zuiden te warm, dan verschuift die zone naar het noorden, en de soort schuift mee.",
    ),
    dict(
        type="waarofniet",
        vraag="Klimaatverandering treft alle landen even hard.",
        antwoord=False,
        uitleg="Lage eilandstaten, droge streken en arme landen worden het zwaarst getroffen, terwijl ze het minst hebben uitgestoten. Rijke landen kunnen zich beter beschermen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met een landschap als de droogte er toeneemt?",
        opties=[
            "Beken vallen droog en de vegetatie verandert",
            "De bodem wordt er vruchtbaarder van",
            "Het reliëf wordt er hoger door de droogte",
            "Er valt daarna automatisch meer regen",
        ],
        antwoord=0,
        uitleg="Bij aanhoudende droogte zakt het grondwater, vallen beken droog, sterven bomen af en verdort het gras. Wat overblijft is een schraler landschap.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is verwoestijning?",
        opties=[
            "Vruchtbaar land dat stilaan woestijn wordt",
            "Woestijn die door irrigatie vruchtbaar wordt",
            "Een woestijn die zich in de zomer uitbreidt",
            "Een landschap dat door zand bedekt raakt",
        ],
        antwoord=0,
        uitleg="Door droogte, overbegrazing en ontbossing verliest de bodem zijn plantendek en waait of spoelt hij weg. Wat overblijft, kan geen landbouw meer dragen.",
    ),
    dict(
        type="invultekst",
        vraag="Mensen die hun streek moeten verlaten door aanhoudende droogte of door overstroming, noemt men ___.",
        antwoord="klimaatvluchtelingen",
        uitleg="Wie geen water of geen oogst meer heeft, trekt weg. Dat gebeurt meestal niet naar een ander werelddeel, maar naar de stad of naar een buurland.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een koraalrif gevoelig voor opwarming?",
        opties=[
            "Warm water doet het koraal verbleken en afsterven",
            "Warm water maakt het koraal juist sneller groeien",
            "Warm water spoelt het koraal van de rotsen",
            "Warm water maakt het rif zwaarder dan het water",
        ],
        antwoord=0,
        uitleg="Koraal leeft samen met kleine algen. Wordt het water te warm, dan stoot het koraal die algen af, verbleekt het en sterft het als de warmte aanhoudt.",
    ),
    dict(
        type="waarofniet",
        vraag="Meer bomen planten helpt tegen klimaatverandering.",
        antwoord=True,
        uitleg="Bomen nemen koolstofdioxide op terwijl ze groeien, geven schaduw en houden water vast. Het volstaat niet op zich, maar het helpt wel degelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke maatregelen verminderen de uitstoot van broeikasgassen? Er zijn er meerdere juist.",
        opties=[
            "Woningen beter isoleren",
            "Stroom opwekken met wind en zon",
            "Vaker de trein of de fiets nemen",
            "Meer wegen aanleggen voor het autoverkeer",
            "Oude bossen kappen voor nieuwe verkavelingen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Minder verbranden en minder rijden verlaagt de uitstoot. Extra wegen en gekapte bossen doen precies het omgekeerde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het als een land zijn uitstoot wil verminderen?",
        opties=[
            "Minder broeikasgassen in de lucht brengen",
            "Minder inwoners laten binnenkomen per jaar",
            "Minder goederen naar het buitenland verkopen",
            "Minder energie uit het buitenland invoeren",
        ],
        antwoord=0,
        uitleg="Uitstoot is wat een land aan broeikasgassen de lucht in stuurt. Verminderen betekent anders verwarmen, anders rijden en anders produceren.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom wordt klimaatverandering een probleem genoemd dat geen land alleen oplost?",
        opties=[
            "Omdat de dampkring van de hele wereld gedeeld is",
            "Omdat elk land dezelfde hoeveelheid uitstoot",
            "Omdat er maar één land fossiele brandstoffen gebruikt",
            "Omdat alleen arme landen maatregelen kunnen nemen",
        ],
        antwoord=0,
        uitleg="Koolstofdioxide blijft niet boven het land dat het uitstoot. Daarom hoort dit bij de P van Partnership: landen moeten samen afspraken maken.",
    ),
    dict(
        type="waarofniet",
        vraag="Wat je zelf doet, telt niet mee, want de uitstoot van één gezin is te klein.",
        antwoord=False,
        uitleg="Alle huishoudens samen zijn een groot deel van het verbruik. Bovendien stuurt wat mensen kiezen, mee wat bedrijven en overheden aanbieden.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is een ontharding in een straat of op een plein?",
        opties=[
            "Verharding wegnemen zodat water in de grond kan",
            "Een straat opnieuw asfalteren met een zachter mengsel",
            "Een plein verlagen zodat het water er blijft staan",
            "De ondergrond verstevigen met een laag steenslag",
        ],
        antwoord=0,
        uitleg="Bij ontharding gaan tegels en beton eruit en komt er grond of groen in de plaats. Het water kan dan insijpelen in plaats van naar de riool te lopen.",
    ),
    dict(
        type="invultekst",
        vraag="Zich aanpassen aan een klimaat dat al veranderd is, noemt men ___.",
        antwoord="adaptatie",
        uitleg="Adaptatie is bijvoorbeeld hogere dijken bouwen, schaduwbomen planten in de stad of gewassen kiezen die tegen droogte kunnen. Uitstoot verminderen heet mitigatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="In een stad is het op een zomerse dag warmer dan op het platteland eromheen. Waarom?",
        opties=[
            "Steen en asfalt houden de warmte langer vast",
            "In de stad valt er meer zonlicht op de grond",
            "Op het platteland waait het altijd veel harder",
            "In de stad wonen meer mensen dicht bij elkaar",
        ],
        antwoord=0,
        uitleg="Verharde oppervlakken slaan overdag warmte op en geven ze 's nachts weer af. Groen en water koelen juist af, en daarom helpt ontharden ook tegen hitte.",
    ),
]

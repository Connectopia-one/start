# -*- coding: utf-8 -*-
"""Gametogenese en de hormonale regeling — 🌍 Beyond, biologie.

Deel 1 gaat over het vrouwelijk voortplantingsstelsel, de oögenese met haar
follikels, en de hormonale regeling van de cyclus. Deel 2 gaat over het
mannelijk voortplantingsstelsel, de spermatogenese, de bouw van een zaadcel en
de hormonen die daarbij horen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Waar in het vrouwelijk voortplantingsstelsel rijpt een eicel?",
        opties=[
            "in de eierstok",
            "in de eileider",
            "in de baarmoeder",
            "in de baarmoederhals",
        ],
        antwoord=0,
        uitleg="De follikels met de eicellen zitten in de eierstok. Na de ovulatie wordt "
        "de eicel door de trechter van de eileider opgevangen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de franjes aan de trechter van de eileider die de eicel opvangen?",
        antwoord=["franjes", "fimbriae", "de franjes"],
        uitleg="De franjes strijken over de eierstok en vegen de vrijgekomen eicel de "
        "eileider in. Zonder dat zou ze in de buikholte verdwijnen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe heten de cellen waaruit de oögenese vertrekt?",
        opties=["oögoniën", "spermatogonia", "poollichaampjes", "follikelcellen"],
        antwoord=0,
        uitleg="De oögoniën zijn de diploïde voorlopercellen. Ze zijn bij de geboorte al "
        "aanwezig en worden primaire oöcyten.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij een meisje liggen de primaire oöcyten al bij de geboorte in de eierstok klaar.",
        antwoord=True,
        uitleg="Ze zijn al aan de eerste meiotische deling begonnen en staan daar stil. "
        "Pas vanaf de puberteit gaat er elke cyclus één verder.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke follikel is het verst in haar rijping en staat op het punt te barsten?",
        opties=[
            "de Graafse follikel",
            "de primordiale follikel",
            "de primaire follikel",
            "de secundaire follikel",
        ],
        antwoord=0,
        uitleg="De reeks loopt van primordiaal over primair en secundair naar de Graafse "
        "follikel. Die laatste bolt uit tegen de wand van de eierstok.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat ontstaat er bij de eerste meiotische deling van een primaire oöcyt? Kruis alles aan wat juist is.",
        opties=[
            "een secundaire oöcyt",
            "een poollichaampje",
            "twee gelijke eicellen",
            "vier rijpe eicellen",
        ],
        antwoord=[0, 1],
        uitleg="De deling is ongelijk: bijna al het cytoplasma gaat naar de secundaire "
        "oöcyt, en het poollichaampje krijgt enkel chromosomen en gaat verloren.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men het kleine celletje dat bij de oögenese het cytoplasma niet meekrijgt?",
        antwoord=["poollichaampje", "poolcel", "poollichaampjes"],
        uitleg="Een poollichaampje bevat wel chromosomen, maar bijna geen cytoplasma. Het "
        "sterft af, zodat één eicel alle voorraad krijgt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de ongelijke verdeling van het cytoplasma bij de oögenese nuttig?",
        opties=[
            "de eicel heeft voorraad nodig voor het begin van de ontwikkeling",
            "de eicel moet zich sneller door de eileider kunnen bewegen",
            "de eicel heeft dan geen celmembraan meer nodig om zich te delen",
            "de eicel kan dan door meerdere zaadcellen bevrucht worden",
        ],
        antwoord=0,
        uitleg="Na de bevruchting deelt de zygote zich dagen zonder eten. Al die "
        "voorraad, mitochondria inbegrepen, komt uit de eicel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wanneer maakt de secundaire oöcyt haar tweede meiotische deling af?",
        opties=[
            "pas als ze bevrucht wordt",
            "al in de eierstok voor de ovulatie",
            "altijd precies bij de ovulatie",
            "nooit, ook niet na een bevruchting",
        ],
        antwoord=0,
        uitleg="De tweede deling staat stil in de metafase. Dringt een zaadcel binnen, "
        "dan wordt ze afgewerkt en ontstaat de oötide met een tweede poollichaampje.",
    ),
    dict(
        type="waarofniet",
        vraag="Wordt de secundaire oöcyt niet bevrucht, dan blijft ze tot de volgende cyclus in de eileider liggen.",
        antwoord=False,
        uitleg="Ze sterft binnen een dag af. Daarna verdwijnt het geel lichaam, dalen de "
        "hormonen en laat het baarmoederslijmvlies los: de menstruatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke lagen liggen rond een vrijgekomen eicel? Kruis alles aan wat juist is.",
        opties=[
            "de zona pellucida",
            "de corona radiata",
            "het baarmoederslijmvlies",
            "de slijmprop van de baarmoederhals",
        ],
        antwoord=[0, 1],
        uitleg="De zona pellucida of glashuid ligt tegen de eicel en de corona radiata is "
        "de krans follikelcellen daarrond. Een zaadcel moet er door.",
    ),
    dict(
        type="invultekst",
        vraag="Welk klierachtig weefsel blijft na de ovulatie in de eierstok achter en maakt progesteron?",
        antwoord=["geel lichaam", "het geel lichaam", "corpus luteum"],
        uitleg="De leeggelopen follikel wordt het geel lichaam. Het houdt het "
        "baarmoederslijmvlies op peil tot de placenta dat overneemt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke klier stuurt met GnRH de hypofyse aan?",
        opties=["de hypothalamus", "de eierstok", "de schildklier", "de bijnier"],
        antwoord=0,
        uitleg="De hypothalamus geeft GnRH af aan de hypofyse. Die maakt dan FSH en LH, "
        "die op hun beurt de eierstok aansturen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet FSH in de eerste helft van de cyclus? Kruis alles aan wat juist is.",
        opties=[
            "de follikels laten rijpen",
            "de follikels oestrogeen laten maken",
            "de ovulatie meteen uitlokken",
            "het baarmoederslijmvlies afbreken",
        ],
        antwoord=[0, 1],
        uitleg="FSH staat voor follikelstimulerend hormoon. Het laat een groep follikels "
        "groeien, waarvan er één de Graafse follikel wordt.",
    ),
    dict(
        type="invultekst",
        vraag="Welk hormoon veroorzaakt met een plotse piek de ovulatie?",
        antwoord=["LH", "lh", "luteïniserend hormoon"],
        uitleg="De LH-piek laat de Graafse follikel barsten. Daarna vormt het "
        "achtergebleven weefsel onder invloed van LH het geel lichaam.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet oestrogeen in de folliculaire fase?",
        opties=[
            "het baarmoederslijmvlies laten opbouwen",
            "het baarmoederslijmvlies laten loslaten",
            "de eicel haar tweede deling laten afmaken",
            "de zaadcellen in de eileider tegenhouden",
        ],
        antwoord=0,
        uitleg="De rijpende follikels maken oestrogeen. Dat bouwt het slijmvlies op, "
        "zodat een bevruchte eicel zich kan innestelen.",
    ),
    dict(
        type="waarofniet",
        vraag="Een hoge concentratie oestrogeen en progesteron remt de afgifte van FSH en LH.",
        antwoord=True,
        uitleg="Dat is negatieve feedback. Daar steunt ook de combinatiepil op: hoge "
        "hormoonwaarden houden FSH en LH laag, dus komt er geen ovulatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke fase van de cyclus volgt op de ovulatie?",
        opties=[
            "de luteale fase",
            "de folliculaire fase",
            "de menstruatiefase",
            "de innestelingsfase",
        ],
        antwoord=0,
        uitleg="Luteaal verwijst naar het corpus luteum, het geel lichaam. Die fase duurt "
        "ongeveer veertien dagen, ongeacht hoe lang de eerste helft duurde.",
    ),
    dict(
        type="waarofniet",
        vraag="De menstruatie komt doordat het progesteron sterk stijgt.",
        antwoord=False,
        uitleg="Het is net omgekeerd: het geel lichaam verdwijnt, het progesteron zakt en "
        "daardoor laat het slijmvlies los.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk hormoon houdt bij een zwangerschap het geel lichaam in stand?",
        opties=["hCG", "FSH", "GnRH", "inhibine"],
        antwoord=0,
        uitleg="Het jonge embryo maakt hCG. Daardoor blijft het geel lichaam progesteron "
        "maken en laat het slijmvlies niet los. Een zwangerschapstest zoekt dat hCG.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Waar worden de zaadcellen gemaakt?",
        opties=[
            "in de zaadbuisjes van de teelbal",
            "in de prostaatklier",
            "in de zaadblaasjes",
            "in de zaadleider",
        ],
        antwoord=0,
        uitleg="De spermatogenese loopt in de wand van de zaadbuisjes. De bijbal slaat de "
        "zaadcellen daarna op tot ze rijp zijn.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom hangen de teelballen buiten de buikholte, in de balzak?",
        opties=[
            "daar is het een paar graden koeler",
            "daar is er meer plaats om te groeien",
            "daar komen ze dichter bij de prostaat",
            "daar is de bloeddruk veel hoger",
        ],
        antwoord=0,
        uitleg="De spermatogenese verloopt het best een paar graden onder de "
        "lichaamstemperatuur. Bij warmte daalt de aanmaak van zaadcellen.",
    ),
    dict(
        type="invultekst",
        vraag="Welke cellen in de zaadbuisjes voeden en ondersteunen de rijpende zaadcellen?",
        antwoord=["cellen van Sertoli", "Sertolicellen", "Sertoli"],
        uitleg="De cellen van Sertoli voeden de rijpende cellen en vormen een barrière "
        "tussen het bloed en de zaadbuisjes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke cellen tussen de zaadbuisjes maken testosteron?",
        opties=[
            "de cellen van Leydig",
            "de cellen van Sertoli",
            "de spermatogonia",
            "de follikelcellen",
        ],
        antwoord=0,
        uitleg="De cellen van Leydig liggen in het bindweefsel tussen de buisjes. LH zet "
        "ze aan tot de productie van testosteron.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke reeks beschrijft de spermatogenese?",
        opties=[
            "spermatogonium, spermatocyt, spermatide, spermatozoïde",
            "spermatozoïde, spermatide, spermatocyt, spermatogonium",
            "spermatide, spermatogonium, spermatocyt, spermatozoïde",
            "spermatocyt, spermatozoïde, spermatogonium, spermatide",
        ],
        antwoord=0,
        uitleg="Het diploïde spermatogonium wordt een primaire spermatocyt. Na de meiose "
        "volgen de haploïde spermatiden, die uitgroeien tot spermatozoïden.",
    ),
    dict(
        type="waarofniet",
        vraag="Uit één primaire spermatocyt ontstaan vier bruikbare zaadcellen.",
        antwoord=True,
        uitleg="De twee meiotische delingen geven vier gelijke haploïde cellen. Bij de "
        "oögenese blijft er maar één eicel over, met drie poollichaampjes.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zit er in het acrosoom van een zaadcel?",
        opties=[
            "enzymen om door de lagen rond de eicel te geraken",
            "de mitochondria die de staart van energie voorzien",
            "het erfelijk materiaal dat naar de eicel moet",
            "de voedingsvoorraad voor de eerste celdelingen",
        ],
        antwoord=0,
        uitleg="Het acrosoom is een blaasje met enzymen op de kop. Die maken een weg door "
        "de corona radiata en de zona pellucida.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat zit er in het middenstuk van een zaadcel?",
        opties=[
            "de mitochondria",
            "het acrosoom",
            "de kern met de chromosomen",
            "de voedingsvoorraad van de eicel",
        ],
        antwoord=0,
        uitleg="De mitochondria in het middenstuk leveren het ATP voor de zweepslag van "
        "de staart. De kop draagt de kern, de staart is een flagel.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noemt men de staart van een zaadcel met een vakwoord?",
        antwoord=["flagel", "zweepstaart", "flagellum"],
        uitleg="De flagel is opgebouwd uit microtubuli. Haar golfbeweging duwt de zaadcel "
        "vooruit.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke klieren leveren vocht aan het sperma? Kruis alles aan wat juist is.",
        opties=[
            "de zaadblaasjes",
            "de prostaatklier",
            "de bijnieren",
            "de schildklier",
        ],
        antwoord=[0, 1],
        uitleg="De zaadblaasjes, de prostaat en de klieren van Cowper leveren het vocht. "
        "Dat voedt de zaadcellen en maakt het zure milieu in de vagina minder zuur.",
    ),
    dict(
        type="waarofniet",
        vraag="Het voorvocht uit de klieren van Cowper kan al zaadcellen bevatten.",
        antwoord=True,
        uitleg="Er kunnen zaadcellen uit de zaadleider in meegekomen zijn. Daarom is "
        "terugtrekken geen betrouwbare methode.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welk hormoon stuurt bij de man de cellen van Leydig aan?",
        opties=["LH", "FSH", "inhibine", "progesteron"],
        antwoord=0,
        uitleg="LH werkt op de cellen van Leydig, die testosteron maken. FSH werkt samen "
        "met testosteron op de cellen van Sertoli.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet testosteron? Kruis alles aan wat juist is.",
        opties=[
            "de spermatogenese op gang houden",
            "de secundaire geslachtskenmerken vormen",
            "de ovulatie elke maand uitlokken",
            "het baarmoederslijmvlies opbouwen",
        ],
        antwoord=[0, 1],
        uitleg="Testosteron houdt de aanmaak van zaadcellen aan de gang en zorgt voor "
        "baardgroei, een lagere stem en spiergroei.",
    ),
    dict(
        type="invultekst",
        vraag="Welk hormoon van de cellen van Sertoli remt de afgifte van FSH?",
        antwoord=["inhibine"],
        uitleg="Zijn er genoeg zaadcellen in de maak, dan geven de cellen van Sertoli "
        "inhibine af. Dat remt FSH: negatieve feedback.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is negatieve feedback bij de hormonale regeling?",
        opties=[
            "het product remt zijn eigen aanmaak",
            "het product versterkt zijn eigen aanmaak",
            "het hormoon werkt alleen in het donker",
            "het hormoon wordt in de lever gemaakt",
        ],
        antwoord=0,
        uitleg="Stijgt het testosteron, dan daalt GnRH en dus LH, en zakt het testosteron "
        "weer. Zo blijft de waarde rond een vast niveau.",
    ),
    dict(
        type="waarofniet",
        vraag="De spermatogenese bij de man loopt in cycli van ongeveer 28 dagen, zoals de eicelrijping.",
        antwoord=False,
        uitleg="De spermatogenese loopt onafgebroken, van de puberteit tot op hoge "
        "leeftijd. Het is de vrouwelijke cyclus die in maandelijkse golven werkt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarin verschillen de twee gametogenesen? Kruis alles aan wat juist is.",
        opties=[
            "een eicel krijgt veel cytoplasma, een zaadcel bijna niets",
            "uit één voorlopercel komt één eicel maar vier zaadcellen",
            "enkel de spermatogenese gebruikt meiose",
            "enkel de oögenese geeft haploïde cellen",
        ],
        antwoord=[0, 1],
        uitleg="Beide gebruiken meiose en geven haploïde cellen. Het verschil zit in de "
        "ongelijke verdeling van het cytoplasma en in het aantal bruikbare cellen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoeveel chromosomen heeft een menselijke zaadcel?",
        opties=["23", "46", "22", "92"],
        antwoord=0,
        uitleg="Een gameet is haploïd: 23 chromosomen. Bij de bevruchting worden het weer "
        "46, de helft van elke ouder.",
    ),
    dict(
        type="waarofniet",
        vraag="Bij de man dalen de hormonen op latere leeftijd even plots als bij de vrouw in de menopauze.",
        antwoord=False,
        uitleg="Bij de man zakt het testosteron heel traag en blijft de aanmaak van "
        "zaadcellen doorgaan. Bij de vrouw stopt de eicelrijping wel.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een arts vindt in een spermastaal heel weinig beweeglijke zaadcellen. Welk onderdeel werkt dan slecht?",
        opties=[
            "het middenstuk met zijn mitochondria",
            "het acrosoom met zijn enzymen",
            "de kern met haar chromosomen",
            "de zona pellucida rond de cel",
        ],
        antwoord=0,
        uitleg="Zonder genoeg ATP uit het middenstuk beweegt de staart niet goed. Het "
        "acrosoom speelt pas een rol bij de eicel, en de zona pellucida hoort bij de eicel.",
    ),
]

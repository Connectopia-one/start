# -*- coding: utf-8 -*-
"""🚀 Boost doorstroom — Voortplanting en de menstruatiecyclus.

Hoort bij de kop "voortplanting" van de vakfiche biologie 2de graad
doorstroomfinaliteit, die 10 % van het examen weegt.

Deel 1 gaat over de geslachtsorganen, de gameten, de bevruchting en de
eerste weken van de zwangerschap. Deel 2 gaat over de menstruatiecyclus in
haar drie fasen (folliculaire fase, luteale fase, menstruatiefase) met de
hormonen die haar sturen; dat deel staat niet in de fiche
natuurwetenschappen.

De toon blijft zakelijk en wetenschappelijk, zoals in een leerboek biologie.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Hoe noem je de geslachtscellen van de mens?",
        opties=[
            "gameten",
            "zygoten",
            "neuronen",
            "gameetklieren",
        ],
        antwoord=0,
        uitleg="De eicel en de zaadcel zijn gameten. Ze hebben elk de helft van het aantal chromosomen van een gewone lichaamscel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een gameet heeft de helft van het aantal chromosomen van een gewone lichaamscel.",
        antwoord=True,
        uitleg="Een lichaamscel van de mens heeft 46 chromosomen, een gameet 23. Bij de bevruchting komen die twee helften samen tot 46.",
    ),
    dict(
        type="invultekst",
        vraag="In welk orgaan worden de zaadcellen gevormd?",
        antwoord=["teelbal", "de teelballen", "testis"],
        uitleg="De zaadcellen ontstaan in de kronkelige buisjes van de teelballen. Die liggen buiten de buikholte omdat de vorming een iets lagere temperatuur vraagt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke taken heeft de eierstok? Kruis alles aan wat juist is.",
        opties=[
            "eicellen laten rijpen",
            "oestrogeen afgeven",
            "progesteron afgeven",
            "de bevruchte eicel laten innestelen",
        ],
        antwoord=[0, 1, 2],
        uitleg="De eierstok levert de eicel en de twee hormonen die de cyclus sturen. Het innestelen gebeurt in het baarmoederslijmvlies.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waar vindt de bevruchting bij de mens meestal plaats?",
        opties=[
            "in de eileider",
            "in de baarmoeder",
            "in de eierstok",
            "in de vagina",
        ],
        antwoord=0,
        uitleg="De eicel wordt na de ovulatie door de eileider opgenomen, en daar komt de zaadcel haar tegemoet. De bevruchte eicel reist daarna naar de baarmoeder.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de cel die ontstaat als een zaadcel en een eicel samensmelten?",
        antwoord=["zygote", "de zygote", "bevruchte eicel"],
        uitleg="De zygote is de eerste cel van een nieuw individu, met 46 chromosomen. Zij begint onmiddellijk te delen.",
    ),
    dict(
        type="waarofniet",
        vraag="Eén zaadcel volstaat om een eicel te bevruchten.",
        antwoord=True,
        uitleg="Zodra één zaadcel binnen is, verandert de buitenlaag van de eicel zodat er geen tweede meer door kan. De andere zaadcellen helpen enkel de weg vrij te maken.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de dagen na de bevruchting?",
        opties=[
            "de zygote deelt zich herhaaldelijk en reist naar de baarmoeder om in te nestelen",
            "de zygote blijft in de eileider liggen tot de geboorte",
            "de zygote keert terug naar de eierstok",
            "de zygote wordt in de vagina door de vruchtwand omgeven",
        ],
        antwoord=0,
        uitleg="Onderweg door de eileider deelt de zygote zich tot een bolletje cellen. Dat nestelt zich na ongeveer een week in het baarmoederslijmvlies.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het vastzetten van het celklompje in het baarmoederslijmvlies?",
        antwoord=["innesteling", "de innesteling", "nidatie"],
        uitleg="Bij de innesteling groeit het klompje het slijmvlies in. Vanaf dat moment kan het voedsel en zuurstof uit het bloed van de moeder halen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de taak van de placenta?",
        opties=[
            "stoffen uitwisselen tussen het bloed van de moeder en dat van het kind",
            "het bloed van de moeder en van het kind met elkaar vermengen",
            "de baarmoeder bij de bevalling doen samentrekken",
            "de eicellen bewaren tot de puberteit",
        ],
        antwoord=0,
        uitleg="In de placenta liggen de bloedbanen heel dicht bij elkaar, gescheiden door een dun laagje. Zuurstof en voeding gaan door, maar het bloed vermengt niet.",
    ),
    dict(
        type="waarofniet",
        vraag="Het bloed van de moeder en het bloed van het kind vermengen zich in de placenta.",
        antwoord=False,
        uitleg="Ze blijven gescheiden door een dunne wand. Enkel stoffen gaan erdoor, en dat is nodig omdat de bloedgroepen kunnen verschillen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke stoffen kunnen van de moeder naar het kind door de placenta? Kruis alles aan wat juist is.",
        opties=[
            "zuurstof",
            "voedingsstoffen",
            "alcohol en nicotine",
            "rode bloedcellen van de moeder",
        ],
        antwoord=[0, 1, 2],
        uitleg="Kleine moleculen gaan door, en dus ook schadelijke. Bloedcellen zijn te groot en blijven aan de kant van de moeder.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het koord dat het kind met de placenta verbindt?",
        antwoord=["navelstreng", "de navelstreng"],
        uitleg="In de navelstreng lopen twee slagaders en een vene. Daardoor gaan zuurstof en voeding heen en afvalstoffen terug.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat is de functie van het vruchtwater?",
        opties=[
            "het beschermt het kind tegen stoten en houdt de temperatuur gelijk",
            "het voorziet het kind van al zijn zuurstof",
            "het houdt de baarmoeder op zijn plaats in de buik",
            "het voert de afvalstoffen van de moeder af",
        ],
        antwoord=0,
        uitleg="Het vruchtwater werkt als een kussen en als een stabiele omgeving. De zuurstof komt via de placenta en de navelstreng.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tweeling uit één bevruchte eicel heeft hetzelfde erfelijk materiaal.",
        antwoord=True,
        uitleg="Bij een eeneiige tweeling splitst het celklompje in twee. Bij een twee-eiige tweeling zijn er twee eicellen en twee zaadcellen, dus verschillen ze zoals broers en zussen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom lijkt een kind op beide ouders?",
        opties=[
            "het krijgt de helft van zijn chromosomen van elke ouder",
            "het krijgt alle chromosomen van de moeder en de kenmerken van de vader",
            "het krijgt alle chromosomen van beide ouders dubbel",
            "het neemt tijdens de zwangerschap kenmerken van de moeder over",
        ],
        antwoord=0,
        uitleg="De eicel brengt 23 chromosomen aan en de zaadcel ook. Daardoor komen de erfelijke eigenschappen van beide kanten samen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke veranderingen horen bij de puberteit? Kruis alles aan wat juist is.",
        opties=[
            "de geslachtsklieren beginnen hormonen af te geven",
            "de geslachtsorganen worden rijp",
            "er ontstaan secundaire geslachtskenmerken",
            "het aantal chromosomen in de lichaamscellen verdubbelt",
        ],
        antwoord=[0, 1, 2],
        uitleg="De puberteit maakt het lichaam geschikt voor voortplanting, onder leiding van hormonen. Het aantal chromosomen blijft levenslang hetzelfde.",
    ),
    dict(
        type="waarofniet",
        vraag="De geslachtshormonen bij de puberteit worden door de schildklier aangestuurd.",
        antwoord=False,
        uitleg="Dat doet de hypofyse: zij zet de eierstokken en de teelballen aan het werk. De schildklier regelt de snelheid van de stofwisseling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is de vorming van gameten een bijzondere celdeling?",
        opties=[
            "het aantal chromosomen wordt gehalveerd en elke gameet is uniek",
            "er ontstaan twee cellen die precies gelijk zijn aan de moedercel",
            "de cellen krijgen dubbel zoveel chromosomen als de moedercel",
            "er komt geen celkern aan te pas",
        ],
        antwoord=0,
        uitleg="Bij de rijpingsdeling wordt het aantal gehalveerd en worden de chromosomen van beide ouders doorgemengd. Daarom zijn broers en zussen niet gelijk.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een paar wil weten wanneer de kans op zwangerschap het grootst is. Wat is biologisch het antwoord?",
        opties=[
            "rond de ovulatie, want de eicel is maar een korte tijd bevruchtbaar",
            "tijdens de menstruatie, want dan is de baarmoeder leeg",
            "altijd even groot, want de eicel is de hele maand aanwezig",
            "vlak voor de menstruatie, want dan is het slijmvlies het dikst",
        ],
        antwoord=0,
        uitleg="De eicel blijft maar ongeveer een dag bevruchtbaar, zaadcellen enkele dagen. Daardoor ligt de kans rond de ovulatie het hoogst.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Welke drie fasen onderscheidt men in de menstruatiecyclus?",
        opties=[
            "de menstruatiefase, de folliculaire fase en de luteale fase",
            "de eerste, de tweede en de derde week",
            "de rijpingsfase, de bevruchtingsfase en de innestelingsfase",
            "de groeifase, de bloeifase en de rustfase",
        ],
        antwoord=0,
        uitleg="De cyclus begint met de menstruatie, daarna rijpt een follikel, en na de ovulatie volgt de luteale fase. Gemiddeld duurt het geheel 28 dagen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het blaasje in de eierstok waarin een eicel rijpt?",
        antwoord=["follikel", "een follikel", "de follikel"],
        uitleg="De follikel is een holte met vocht en cellen rond de rijpende eicel. Die cellen maken ook oestrogeen aan.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er in de folliculaire fase?",
        opties=[
            "een follikel rijpt en het baarmoederslijmvlies wordt opnieuw opgebouwd",
            "het baarmoederslijmvlies wordt met wat bloed afgestoten",
            "het geel lichaam geeft grote hoeveelheden progesteron af",
            "de bevruchte eicel nestelt zich in de baarmoeder in",
        ],
        antwoord=0,
        uitleg="Onder invloed van oestrogeen rijpt de follikel en groeit het slijmvlies weer aan. Zo is de baarmoeder klaar als er een bevruchting komt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het vrijkomen van de eicel uit de eierstok?",
        antwoord=["ovulatie", "de ovulatie", "eisprong"],
        uitleg="Bij de ovulatie barst de rijpe follikel open en komt de eicel vrij. Dat gebeurt bij een cyclus van 28 dagen rond dag veertien.",
    ),
    dict(
        type="waarofniet",
        vraag="De ovulatie valt tussen de folliculaire fase en de luteale fase.",
        antwoord=True,
        uitleg="Het rijpen gaat eraan vooraf, en wat van de follikel overblijft bepaalt de fase erna. De ovulatie is dus het keerpunt van de cyclus.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat blijft er na de ovulatie van de follikel over?",
        opties=[
            "het geel lichaam, dat progesteron afgeeft",
            "een nieuwe eicel, die volgende maand rijpt",
            "een lege holte zonder enige functie",
            "een nieuw stukje baarmoederslijmvlies",
        ],
        antwoord=0,
        uitleg="De achtergebleven cellen vormen het geel lichaam. Dat maakt vooral progesteron, het hormoon van de luteale fase.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet progesteron in de luteale fase?",
        opties=[
            "het houdt het baarmoederslijmvlies dik en klaar",
            "het laat in de eierstok een nieuwe follikel rijpen",
            "het stoot het baarmoederslijmvlies met wat bloed af",
            "het laat de rijpe eicel uit de eierstok vrijkomen",
        ],
        antwoord=0,
        uitleg="Progesteron houdt het slijmvlies in stand en remt tegelijk de rijping van een nieuwe follikel. Zo komt er geen tweede ovulatie in dezelfde cyclus.",
    ),
    dict(
        type="waarofniet",
        vraag="Blijft een bevruchting uit, dan sterft het geel lichaam af en daalt het progesteron.",
        antwoord=True,
        uitleg="Zonder bevruchting houdt het geel lichaam na ongeveer twee weken op. Het progesteron zakt, het slijmvlies wordt afgestoten en de menstruatie begint.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom treedt er een menstruatie op?",
        opties=[
            "het progesteron daalt en houdt het slijmvlies niet meer in stand",
            "de eicel is te groot geworden en wordt samen met het slijmvlies afgevoerd",
            "de eierstok ruimt op om plaats te maken voor een volgende rijpe follikel",
            "het oestrogeen stijgt zo sterk dat het slijmvlies van de wand loskomt",
        ],
        antwoord=0,
        uitleg="Het slijmvlies had een hormoon nodig om te blijven. Valt dat weg, dan laat het los en verlaat het samen met wat bloed de baarmoeder.",
    ),
    dict(
        type="invultekst",
        vraag="Welk hormoon van de eierstok overheerst in de eerste helft van de cyclus?",
        antwoord=["oestrogeen", "het oestrogeen", "oestrogenen"],
        uitleg="Oestrogeen komt uit de rijpende follikel en bouwt het baarmoederslijmvlies op. Na de ovulatie neemt progesteron de hoofdrol over.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke hormonen van de hypofyse sturen de cyclus? Kruis alles aan wat juist is.",
        opties=[
            "het hormoon dat de follikel laat rijpen",
            "het hormoon dat de ovulatie uitlokt",
            "er is er geen, de eierstok regelt alles zelf",
            "insuline",
        ],
        antwoord=[0, 1],
        uitleg="De hypofyse stuurt de eierstok met twee hormonen aan: het ene laat de follikel rijpen, het andere geeft het startschot voor de ovulatie. Insuline hoort bij de bloedglucose.",
    ),
    dict(
        type="waarofniet",
        vraag="De hypofyse stuurt de eierstok aan, maar de eierstok beïnvloedt de hypofyse niet.",
        antwoord=False,
        uitleg="Het werkt in twee richtingen. De hormonen van de eierstok remmen of stimuleren op hun beurt de hypofyse, en dat is net de terugkoppeling.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat gebeurt er met het geel lichaam als er wel een bevruchting en innesteling is?",
        opties=[
            "het blijft nog weken progesteron afgeven zodat het slijmvlies behouden blijft",
            "het verdwijnt meteen, want een beginnende zwangerschap heeft het niet nodig",
            "het groeit in de wand van de baarmoeder uit tot de placenta",
            "het laat een tweede eicel vrijkomen uit dezelfde eierstok",
        ],
        antwoord=0,
        uitleg="Het ingenestelde klompje geeft een hormoon af dat het geel lichaam in leven houdt. Daardoor blijft het progesteron hoog en komt er geen menstruatie.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een cyclus duurt bij iemand 32 dagen in plaats van 28. Welke fase is dan meestal langer?",
        opties=[
            "de folliculaire fase, want die kan sterk in lengte verschillen",
            "de luteale fase, want die duurt bij iedereen anders",
            "de menstruatiefase, want die duurt dan twee weken",
            "geen enkele, de cyclus is bij iedereen precies 28 dagen",
        ],
        antwoord=0,
        uitleg="De luteale fase ligt vrij vast rond veertien dagen, omdat het geel lichaam ongeveer zo lang leeft. De rijping van de follikel varieert wel.",
    ),
    dict(
        type="waarofniet",
        vraag="Een cyclus van precies 28 dagen is de enige normale lengte.",
        antwoord=False,
        uitleg="28 dagen is een gemiddelde. Een cyclus van 24 tot 35 dagen komt vaak voor en is gewoon.",
    ),
    dict(
        type="meerkeuze",
        vraag="Hoe werkt de gecombineerde anticonceptiepil?",
        opties=[
            "de hormonen erin remmen de hypofyse, zodat er geen ovulatie komt",
            "ze maakt de baarmoeder ondoordringbaar voor zaadcellen",
            "ze verwijdert de eicellen uit de eierstok",
            "ze verkort de cyclus tot zeven dagen",
        ],
        antwoord=0,
        uitleg="Door voortdurend oestrogeen en progesteron aan te voeren, denkt de hypofyse dat de luteale fase bezig is. Er rijpt dan geen follikel en er volgt geen ovulatie.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het einde van de vruchtbare periode, wanneer de cyclus ophoudt?",
        antwoord=["menopauze", "de menopauze", "overgang"],
        uitleg="Bij de menopauze raakt de voorraad follikels op en daalt het oestrogeen. De cyclus stopt dan definitief.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke lichaamstekens kunnen rond de ovulatie wijzen? Kruis alles aan wat juist is.",
        opties=[
            "een lichte stijging van de lichaamstemperatuur",
            "een verandering van het baarmoederhalsslijm",
            "soms een lichte pijn in de onderbuik",
            "een daling van het aantal rode bloedcellen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Temperatuur, slijm en soms een steek zijn de klassieke tekens. Met het aantal rode bloedcellen heeft de ovulatie niets te maken.",
    ),
    dict(
        type="waarofniet",
        vraag="De menstruatiecyclus is een voorbeeld van een proces dat door hormonen met terugkoppeling geregeld wordt.",
        antwoord=True,
        uitleg="Hypofyse en eierstok sturen elkaar heen en weer. Daardoor verloopt de cyclus telkens opnieuw in dezelfde orde.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand met een onregelmatige cyclus wil de ovulatie opsporen. Waarom is enkel de kalender onvoldoende?",
        opties=[
            "de folliculaire fase varieert, dus valt de ovulatie niet elke maand op dezelfde dag",
            "de ovulatie valt altijd op dag veertien, ook bij een onregelmatige cyclus",
            "de kalender zegt niets over het aantal eicellen in de eierstok",
            "de menstruatie begint bij een onregelmatige cyclus zonder hormonen",
        ],
        antwoord=0,
        uitleg="Omdat de eerste fase in lengte wisselt, schuift de ovulatie mee. Daarom kijkt men ook naar de temperatuur en het slijm.",
    ),
]

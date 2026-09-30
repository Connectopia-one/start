# -*- coding: utf-8 -*-
"""De vragen voor "Bronnen wegen: objectief, gekleurd of nep" (🚀 Boost doorstroom, Nederlands).

Uit de vakfiche van Nederlands 2, het lijstje criteria om te beoordelen of een
tekst betrouwbaar, correct en bruikbaar is: wie is de zender, is die deskundig,
wat is zijn bedoeling, welke bronnen gebruikt hij, is hij objectief of
subjectief, is de informatie actueel, via welk kanaal komt ze, zitten er
dubbele bodems in, is er sprake van framing.

Deel 1 zijn de criteria zelf. Deel 2 gaat over framing en over de talige
middelen waarmee een schrijver kleurt zonder te liegen.
"""

DEEL1 = [
    dict(
        type="meerkeuze",
        vraag="Welke vraag stel je als eerste wanneer je de betrouwbaarheid van een tekst wil inschatten?",
        opties=[
            "Wie is de zender van deze tekst?",
            "Hoeveel alinea's telt deze tekst?",
            "Welk lettertype is er gebruikt?",
            "Hoe lang deed ik erover om te lezen?",
        ],
        antwoord=0,
        uitleg="Zonder zender kan je niets wegen: geen deskundigheid, geen bedoeling, geen belang.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke vragen helpen je de betrouwbaarheid van een tekst te beoordelen?",
        opties=[
            "Is de zender deskundig in dit onderwerp?",
            "Welke bronnen gebruikt de tekst zelf?",
            "Wat wil de zender met deze tekst bereiken?",
            "Hoeveel tussentitels staan er in de tekst?",
        ],
        antwoord=[0, 1, 2],
        uitleg="Het aantal tussentitels zegt iets over de opbouw, niet over de betrouwbaarheid.",
    ),
    dict(
        type="invultekst",
        vraag="Een zender met echte kennis van zaken over het onderwerp noemen we ___.",
        antwoord=["deskundig", "een deskundige"],
        uitleg="Deskundigheid geldt per vakgebied. Buiten zijn terrein weegt het woord van een deskundige niet zwaarder dan dat van iemand anders.",
    ),
    dict(
        type="waarofniet",
        vraag="Veel spelfouten in een tekst zijn een reden om voorzichtiger met de inhoud om te gaan.",
        antwoord=True,
        uitleg="Ze wijzen erop dat er geen redactie overheen ging. Dat bewijst niets, maar het is wel een waarschuwingslicht.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom kijk je of de informatie in een tekst nog actueel is?",
        opties=[
            "omdat gegevens en regels ondertussen veranderd kunnen zijn",
            "omdat oude teksten altijd slechter geschreven zijn",
            "omdat een oude tekst nooit een deskundige zender heeft",
            "omdat je dan weet hoeveel de tekst gekost heeft",
        ],
        antwoord=0,
        uitleg="Cijfers over bevolking, prijzen of wetgeving verouderen snel. Een tekst uit 2012 kan correct geweest zijn en vandaag fout.",
    ),
    dict(
        type="meerkeuze",
        vraag="Je vindt een artikel zonder auteur en zonder datum. Wat besluit je daaruit?",
        opties=[
            "je kan twee belangrijke criteria niet nagaan",
            "de tekst is zeker verzonnen",
            "de tekst is zeker betrouwbaar",
            "de tekst is zeker een publireportage",
        ],
        antwoord=0,
        uitleg="Het is geen bewijs van iets, maar je kan zender noch actualiteit wegen. Dan zoek je de informatie elders na.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een eenzijdige, meestal politieke tekst die je met opzet maar één kant van een zaak toont?",
        antwoord=["propaganda"],
        uitleg="Propaganda is persuasief: ze wil je beïnvloeden, niet informeren.",
    ),
    dict(
        type="waarofniet",
        vraag="Een tekst van een deskundige is daarom altijd objectief.",
        antwoord=False,
        uitleg="Een deskundige kan ook een belang hebben, of maar één school binnen zijn vak vertegenwoordigen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke signalen wijzen erop dat een tekst subjectief is?",
        opties=[
            "waardewoorden zoals schandalig of geniaal",
            "uitroeptekens middenin de lopende tekst",
            "zinnen die beginnen met 'ik vind'",
            "voetnoten met bronvermeldingen",
        ],
        antwoord=[0, 1, 2],
        uitleg="Bronvermeldingen wijzen net op een poging tot onderbouwing. De drie andere verraden het oordeel van de schrijver.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom vraag je je af wat de bedoeling van de zender is?",
        opties=[
            "omdat het doel bepaalt wat er weggelaten wordt",
            "omdat de bedoeling altijd bovenaan de tekst staat",
            "omdat een zender zonder bedoeling niet bestaat",
            "omdat je dan het kanaal kan achterhalen",
        ],
        antwoord=0,
        uitleg="Wie iets wil verkopen, laat de nadelen weg. Wie wil informeren, zet ze erbij. Wat ontbreekt, zegt vaak evenveel als wat er staat.",
    ),
    dict(
        type="waarofniet",
        vraag="Zodra een tekst bronnen vermeldt, is hij betrouwbaar.",
        antwoord=False,
        uitleg="Je moet die bronnen ook wegen: bestaan ze, zijn ze recent, en zeggen ze werkelijk wat de schrijver beweert?",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom telt het kanaal mee als je betrouwbaarheid inschat?",
        opties=[
            "omdat sommige kanalen redactionele controle hebben en andere niet",
            "omdat een bericht op papier altijd waar is",
            "omdat een bericht op een scherm sneller geschreven is",
            "omdat het kanaal bepaalt wie de zender is",
        ],
        antwoord=0,
        uitleg="Een krantenartikel passeerde een eindredactie. Een doorgestuurd bericht in een groepschat passeerde niemand.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een verborgen betekenis die onder de letterlijke tekst schuilgaat?",
        antwoord=["een dubbele bodem", "dubbele bodem"],
        uitleg="Wie een dubbele bodem mist, leest een tekst letterlijk terwijl hij ironisch of symbolisch bedoeld is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een recensie eindigt met: 'Kortom, een meesterwerk, als je van drie uur stilstaande beelden houdt.' Wat gebeurt hier?",
        opties=[
            "de schrijver is ironisch en bedoelt het omgekeerde",
            "de schrijver prijst de film oprecht de hemel in",
            "de schrijver geeft een neutrale samenvatting",
            "de schrijver citeert een andere recensent",
        ],
        antwoord=0,
        uitleg="De lof wordt in de tweede helft van de zin onderuitgehaald. Wie de ironie mist, leest het oordeel precies verkeerd.",
    ),
    dict(
        type="waarofniet",
        vraag="Een deskundige kan tegelijk een belang hebben bij wat hij vertelt.",
        antwoord=True,
        uitleg="Een onderzoeker die betaald wordt door de sector waarover hij publiceert, is deskundig én partij.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is het nuttig te weten wie een onderzoek betaald heeft?",
        opties=[
            "omdat de opdrachtgever belang kan hebben bij de uitkomst",
            "omdat onderzoek zonder geld nooit gebeurt",
            "omdat de opdrachtgever de tekst geschreven heeft",
            "omdat je dan weet hoe oud het onderzoek is",
        ],
        antwoord=0,
        uitleg="Het maakt het onderzoek niet meteen waardeloos, maar het is een reden om extra kritisch te lezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke teksten doen zich voor als iets anders dan ze zijn?",
        opties=[
            "een publireportage",
            "een satirisch nieuwsbericht",
            "een verzonnen bericht op sociale media",
            "een artikel met bronvermelding en auteursnaam",
        ],
        antwoord=[0, 1, 2],
        uitleg="Alle drie lenen ze de vorm van het nieuws. Alleen het laatste presenteert zich als wat het is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een frisdrankmerk publiceert een lange tekst over 'bewust bewegen'. Waarop let je?",
        opties=[
            "op wat er níét in staat over suiker",
            "op het aantal alinea's in de tekst",
            "op de kleur van de afbeeldingen",
            "op de lengte van de zinnen",
        ],
        antwoord=0,
        uitleg="De zender heeft een belang. Wat hij weglaat, verraadt zijn doel duidelijker dan wat hij opschrijft.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat bedoelt de fiche met 'welke opvattingen en waardeoordelen bevat de tekst'?",
        opties=[
            "welke overtuigingen de schrijver als vanzelfsprekend aanneemt",
            "hoeveel bronnen de schrijver onderaan vermeldt",
            "welk kanaal de schrijver gekozen heeft",
            "hoe recent de gegevens in de tekst zijn",
        ],
        antwoord=0,
        uitleg="Achter elke tekst zitten aannames. Wie ze herkent, ziet waar de schrijver vertrekt zonder het te bewijzen.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je verzonnen informatie die zich voordoet als echt nieuws?",
        antwoord=["nepnieuws", "fake news"],
        uitleg="Nepnieuws leunt op de vorm van een nieuwsbericht en op snelle verspreiding via sociale media.",
    ),
]

DEEL2 = [
    dict(
        type="meerkeuze",
        vraag="Wat is framing?",
        opties=[
            "een onderwerp in een bepaald kader zetten door je woordkeuze en invalshoek",
            "een tekst opdelen in duidelijke alinea's met tussentitels",
            "een bron citeren die je zelf niet gelezen hebt",
            "een tekst schrijven zonder enige spelfout erin",
        ],
        antwoord=0,
        uitleg="Framing hoeft niet te liegen. Door te kiezen wát je belicht en met welke woorden, stuur je toch hoe de lezer het ziet.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een bedrijf schrijft 'prijsaanpassing' waar 'prijsverhoging' bedoeld is. Wat gebeurt daar?",
        opties=[
            "een onaangenaam feit krijgt een neutraler klinkend woord",
            "een neutraal feit krijgt een negatiever klinkend woord",
            "een feit wordt vervangen door een uitgesproken mening",
            "een woord wordt letterlijk in plaats van figuurlijk gebruikt",
        ],
        antwoord=0,
        uitleg="'Aanpassing' kan ook omlaag betekenen, en dat is precies waarom het gekozen wordt.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je een verzachtend woord voor iets onaangenaams?",
        antwoord=["eufemisme", "een eufemisme"],
        uitleg="Heengaan voor sterven, prijsaanpassing voor prijsverhoging, herstructurering voor ontslagen.",
    ),
    dict(
        type="waarofniet",
        vraag="Framing zit vooral in de woordkeuze en in de invalshoek die gekozen wordt.",
        antwoord=True,
        uitleg="Dezelfde feiten kunnen 'duizenden op straat' of 'verkeerschaos in het centrum' worden, zonder dat er iets onwaar is.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke talige middelen drukken subjectiviteit uit?",
        opties=[
            "beeldspraak",
            "de connotatie van woorden",
            "modaliteit",
            "de bladspiegel",
        ],
        antwoord=[0, 1, 2],
        uitleg="De bladspiegel is vormgeving. De drie andere sturen hoe de lezer het bericht voelt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarin verschilt 'Zwijg eens even!' van 'Zwijg!'?",
        opties=[
            "het woordje 'eens' maakt het bevel zachter",
            "de eerste zin is een vraag geworden",
            "de tweede zin staat in de verleden tijd",
            "de eerste zin is in het meervoud gezet",
        ],
        antwoord=0,
        uitleg="Zulke kleine woordjes heten modale partikels. Ze veranderen de toon zonder de inhoud te veranderen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee kranten berichten over dezelfde betoging: 'Duizenden op straat voor het klimaat' en 'Klimaatbetoging legt centrum lam'. Wat toont dat aan?",
        opties=[
            "dezelfde feiten kunnen heel verschillend geframed worden",
            "een van de twee kranten heeft de feiten verzonnen",
            "de eerste krant is betrouwbaar, de tweede niet",
            "framing komt alleen in reclame voor",
        ],
        antwoord=0,
        uitleg="Allebei kloppen ze. De ene kop kiest de deelnemers als invalshoek, de andere de hinder.",
    ),
    dict(
        type="waarofniet",
        vraag="Wie framing gebruikt, liegt.",
        antwoord=False,
        uitleg="Framing werkt net omdat alles wat er staat waar kan zijn. Het zit in de keuze van woorden en invalshoek.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je de gevoelswaarde die aan een woord kleeft, naast zijn letterlijke betekenis?",
        antwoord=["connotatie", "de connotatie"],
        uitleg="'Goedkoop' en 'voordelig' betekenen hetzelfde, maar het eerste klinkt negatiever.",
    ),
    dict(
        type="invultekst",
        vraag="Hoe noem je het bewust kiezen van een invalshoek die de lezer in een bepaalde richting duwt?",
        antwoord=["framing"],
        uitleg="Het woord komt van frame, kader: je zet een kader rond de feiten en laat de rest buiten beeld.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waaraan herken je vaak een nepnieuwsbericht?",
        opties=[
            "er wordt geen auteur vermeld",
            "het circuleert alleen via sociale media",
            "de kop belooft veel meer dan de tekst waarmaakt",
            "er wordt verwezen naar een studie met naam en jaartal",
        ],
        antwoord=[0, 1, 2],
        uitleg="De laatste is juist een teken van onderbouwing, al moet je die studie nog altijd nagaan.",
    ),
    dict(
        type="waarofniet",
        vraag="Satire wil je misleiden.",
        antwoord=False,
        uitleg="Satire wil je aan het lachen brengen en iets aan de kaak stellen. Het misverstand ontstaat pas als je het los van zijn bron leest.",
    ),
    dict(
        type="meerkeuze",
        vraag="Een influencer toont een product zonder te zeggen dat hij ervoor betaald wordt. Welk criterium kan je daardoor niet toepassen?",
        opties=[
            "de bedoeling van de zender",
            "de actualiteit van de informatie",
            "het kanaal van de boodschap",
            "de spelling van de tekst",
        ],
        antwoord=0,
        uitleg="Je denkt een eerlijke mening te lezen terwijl het reclame is. Daarom bestaat de verplichting om zo'n samenwerking te vermelden.",
    ),
    dict(
        type="waarofniet",
        vraag="Dezelfde gebeurtenis kan in twee betrouwbare kranten heel verschillend geframed worden.",
        antwoord=True,
        uitleg="Betrouwbaar betekent dat de feiten kloppen, niet dat de invalshoek dezelfde is. Daarom loont het om meerdere bronnen te lezen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Iemand schrijft over 'het verkwisten van belastinggeld' in plaats van over 'overheidsuitgaven'. Wat doet hij?",
        opties=[
            "hij kiest een woord met een negatievere gevoelswaarde",
            "hij kiest een woord met een zachtere gevoelswaarde",
            "hij gebruikt een woord in zijn letterlijke betekenis",
            "hij vervangt een mening door een controleerbaar feit",
        ],
        antwoord=0,
        uitleg="Dat heet een dysfemisme: het omgekeerde van een eufemisme. Het oordeel zit al in het woord.",
    ),
    dict(
        type="meerkeuze",
        vraag="Waarom is een publireportage lastiger te herkennen dan een gewone reclamespot?",
        opties=[
            "omdat hij de vorm en de opmaak van een artikel leent",
            "omdat hij altijd korter is dan een spot",
            "omdat hij nooit een merknaam vermeldt",
            "omdat hij enkel op papier verschijnt",
        ],
        antwoord=0,
        uitleg="Bij een spot weet je dat het reclame is. Bij een publireportage moet je op het kleine woordje 'advertorial' letten.",
    ),
    dict(
        type="meerkeuze",
        vraag="Welke woorden in een krantenkop kleuren het bericht?",
        opties=["schandalig", "eindelijk", "zogenaamd", "dinsdag"],
        antwoord=[0, 1, 2],
        uitleg="'Dinsdag' is een gegeven. De drie andere leggen er een oordeel bovenop.",
    ),
    dict(
        type="meerkeuze",
        vraag="Twee betrouwbare bronnen spreken elkaar tegen. Wat doe je?",
        opties=[
            "je zoekt een derde bron en vergelijkt hoe ze aan hun gegevens komen",
            "je kiest de bron die het kortste artikel heeft",
            "je gaat ervan uit dat allebei de bronnen onbetrouwbaar zijn",
            "je neemt het gemiddelde van de twee cijfers",
        ],
        antwoord=0,
        uitleg="Vaak meten ze iets anders of over een andere periode. Dat zie je pas als je hun methode naast elkaar legt.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat doet de metafoor in 'een golf van klachten overspoelde de dienst'?",
        opties=[
            "ze laat de klachten aanvoelen als een natuurramp",
            "ze geeft het precieze aantal klachten weer",
            "ze maakt de zin objectiever dan zonder beeldspraak",
            "ze noemt de zender van de klachten bij naam",
        ],
        antwoord=0,
        uitleg="Beeldspraak is een van de talige middelen waarmee je subjectiviteit binnenbrengt zonder één cijfer te noemen.",
    ),
    dict(
        type="meerkeuze",
        vraag="Wat betekent het als de fiche vraagt of een tekst 'bruikbaar' is?",
        opties=[
            "of hij een antwoord geeft op de vraag die jij hebt",
            "of hij in een mooi lettertype gezet is",
            "of hij korter is dan twee bladzijden",
            "of hij door een bekende schrijver geschreven is",
        ],
        antwoord=0,
        uitleg="Betrouwbaar, correct en bruikbaar zijn drie verschillende dingen. Een perfect correcte tekst kan voor jouw opdracht volstrekt nutteloos zijn.",
    ),
]
